from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import tarfile
import zipfile
from pathlib import Path


VISA_URL = "https://amazon-visual-anomaly.s3.us-west-2.amazonaws.com/VisA_20220922.tar"
KAGGLE_MVTEC_DATASET = "ipythonx/mvtec-ad"


def run(cmd: list[str]) -> None:
    print("+", " ".join(cmd), flush=True)
    subprocess.run(cmd, check=True)


def ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def downloader() -> str:
    for name in ("curl", "wget"):
        if shutil.which(name):
            return name
    raise RuntimeError("Need either curl or wget to download datasets.")


def download(url: str, out: Path) -> None:
    ensure_dir(out.parent)
    tool = downloader()
    if out.exists():
        print(f"Archive already exists, will resume/check: {out}")
    if tool == "curl":
        run(["curl", "-L", "--fail", "--continue-at", "-", "--output", str(out), url])
    else:
        run(["wget", "-c", "-O", str(out), url])


def extract_zip(archive: Path, out_dir: Path) -> None:
    ensure_dir(out_dir)
    marker = out_dir / ".extracted"
    if marker.exists():
        print(f"Already extracted: {out_dir}")
        return
    with zipfile.ZipFile(archive) as zf:
        zf.extractall(out_dir)
    marker.write_text("ok\n", encoding="utf-8")


def extract_tar(archive: Path, out_dir: Path) -> None:
    ensure_dir(out_dir)
    marker = out_dir / ".extracted"
    if marker.exists():
        print(f"Already extracted: {out_dir}")
        return
    with tarfile.open(archive) as tar:
        tar.extractall(out_dir)
    marker.write_text("ok\n", encoding="utf-8")


def link_dataset(target: Path, link: Path) -> None:
    ensure_dir(link.parent)
    if link.exists() or link.is_symlink():
        print(f"Link/path already exists: {link}")
        return
    os.symlink(target, link, target_is_directory=True)
    print(f"Linked {link} -> {target}")


def append_setup_note(message: str) -> None:
    path = Path("docs/setup_issues.md")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write("\n## Dataset Download Note\n\n")
        f.write(message.rstrip() + "\n")


def download_visa(download_root: Path, repo_data_dir: Path) -> None:
    archive = download_root / "archives" / "VisA_20220922.tar"
    extracted = download_root / "visa"
    download(VISA_URL, archive)
    extract_tar(archive, extracted)
    link_dataset(extracted, repo_data_dir / "visa")
    append_setup_note(
        f"- Downloaded VisA from official Amazon S3 URL.\n"
        f"- Archive: `{archive}`\n"
        f"- Extracted: `{extracted}`\n"
        f"- Repo link: `{repo_data_dir / 'visa'}`"
    )


def download_mvtec(url: str, download_root: Path, repo_data_dir: Path) -> None:
    archive = download_root / "archives" / "mvtec_ad.tar.xz"
    extracted = download_root / "mvtec"
    download(url, archive)
    extract_tar(archive, extracted)
    link_dataset(extracted, repo_data_dir / "mvtec")
    append_setup_note(
        f"- Downloaded MVTec AD from user-provided official/license URL.\n"
        f"- Archive: `{archive}`\n"
        f"- Extracted: `{extracted}`\n"
        f"- Repo link: `{repo_data_dir / 'mvtec'}`"
    )


def find_mvtec_root(extracted: Path) -> Path:
    candidates = []
    for path in [extracted, *extracted.rglob("*")]:
        if not path.is_dir():
            continue
        children = {p.name for p in path.iterdir() if p.is_dir()}
        if {"bottle", "cable", "capsule"}.issubset(children):
            candidates.append(path)
    return candidates[0] if candidates else extracted


def download_mvtec_kaggle(download_root: Path, repo_data_dir: Path) -> None:
    archive = download_root / "archives" / "mvtec-ad-kaggle.zip"
    extracted = download_root / "mvtec_kaggle"
    kaggle = shutil.which("kaggle")
    if kaggle is None:
        raise SystemExit(
            "Kaggle CLI is not installed. Install with `pip install kaggle`, then add ~/.kaggle/kaggle.json."
        )
    run([kaggle, "datasets", "download", "-d", KAGGLE_MVTEC_DATASET, "-p", str(archive.parent), "-f", archive.name])
    extract_zip(archive, extracted)
    mvtec_root = find_mvtec_root(extracted)
    link_dataset(mvtec_root, repo_data_dir / "mvtec")
    append_setup_note(
        f"- Downloaded MVTec AD from Kaggle dataset `{KAGGLE_MVTEC_DATASET}`.\n"
        f"- Archive: `{archive}`\n"
        f"- Extracted: `{extracted}`\n"
        f"- Detected MVTec root: `{mvtec_root}`\n"
        f"- Repo link: `{repo_data_dir / 'mvtec'}`"
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", choices=["visa", "mvtec", "mvtec_kaggle"], required=True)
    parser.add_argument("--download-root", default="/tmp/AD-data")
    parser.add_argument("--repo-data-dir", default="data")
    parser.add_argument("--mvtec-url", default=None, help="Official MVTec URL after accepting the license/form.")
    args = parser.parse_args(argv)

    download_root = Path(args.download_root).expanduser().resolve()
    repo_data_dir = Path(args.repo_data_dir)
    ensure_dir(download_root)
    ensure_dir(repo_data_dir)

    if args.dataset == "visa":
        download_visa(download_root, repo_data_dir)
    elif args.dataset == "mvtec":
        if not args.mvtec_url:
            raise SystemExit("MVTec requires --mvtec-url from the official license/download page.")
        download_mvtec(args.mvtec_url, download_root, repo_data_dir)
    elif args.dataset == "mvtec_kaggle":
        download_mvtec_kaggle(download_root, repo_data_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
