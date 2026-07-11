from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .io import ensure_dir


def append_markdown(path: str | Path, title: str, lines: list[str]) -> None:
    path = Path(path)
    ensure_dir(path.parent)
    timestamp = datetime.now(timezone.utc).isoformat()
    block = [f"\n## {title}", "", f"- Timestamp UTC: `{timestamp}`", *lines, ""]
    with path.open("a", encoding="utf-8") as f:
        f.write("\n".join(block))


def write_run_note(
    docs_dir: str | Path,
    run_id: str,
    config: dict[str, Any],
    metrics: dict[str, Any],
    command: str,
    notes: list[str] | None = None,
) -> Path:
    out = Path(docs_dir) / "experiments" / f"{run_id}.md"
    ensure_dir(out.parent)
    lines = [
        f"# Run {run_id}",
        "",
        f"- Command: `{command}`",
        f"- Dataset: `{config.get('dataset', {}).get('name')}`",
        f"- Model: `{config.get('model', {}).get('variant')}`",
        "",
        "## Metrics",
        "",
    ]
    for key, value in sorted(metrics.items()):
        lines.append(f"- `{key}`: `{value}`")
    if notes:
        lines.extend(["", "## Notes", ""])
        lines.extend(f"- {note}" for note in notes)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out

