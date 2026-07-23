from __future__ import annotations

import argparse
import concurrent.futures
import os
from pathlib import Path
import shutil
import urllib.request


CHUNK = 8 * 1024 * 1024


def download_part(url: str, path: Path, start: int, end: int) -> tuple[Path, int]:
    expected = end - start + 1
    present = path.stat().st_size if path.exists() else 0
    if present > expected:
        raise RuntimeError(f"oversized part {path}: {present} > {expected}")
    if present == expected:
        return path, expected
    request = urllib.request.Request(
        url,
        headers={"Range": f"bytes={start + present}-{end}", "User-Agent": "AD-audit-downloader/1"},
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        if response.status != 206:
            raise RuntimeError(f"server ignored range for {path}: HTTP {response.status}")
        with path.open("ab") as handle:
            while True:
                block = response.read(CHUNK)
                if not block:
                    break
                handle.write(block)
    actual = path.stat().st_size
    if actual != expected:
        raise RuntimeError(f"short part {path}: {actual} != {expected}")
    print(f"completed={path.name} bytes={actual}", flush=True)
    return path, actual


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--size", required=True, type=int)
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    part_dir = args.output.parent / f".{args.output.name}.parts"
    part_dir.mkdir(parents=True, exist_ok=True)
    width = (args.size + args.workers - 1) // args.workers
    specs = []
    for index in range(args.workers):
        start = index * width
        if start >= args.size:
            break
        end = min(args.size - 1, start + width - 1)
        specs.append((part_dir / f"part-{index:03d}", start, end))

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = [executor.submit(download_part, args.url, path, start, end) for path, start, end in specs]
        for future in concurrent.futures.as_completed(futures):
            future.result()

    assembling = args.output.parent / f".{args.output.name}.assembling"
    with assembling.open("wb") as destination:
        for path, _, _ in specs:
            with path.open("rb") as source:
                shutil.copyfileobj(source, destination, length=CHUNK)
    if assembling.stat().st_size != args.size:
        raise RuntimeError(f"assembled size mismatch: {assembling.stat().st_size} != {args.size}")
    os.replace(assembling, args.output)
    print(f"output={args.output} bytes={args.output.stat().st_size}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
