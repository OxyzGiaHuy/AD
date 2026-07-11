from __future__ import annotations

import csv
import json
import math
from pathlib import Path
from typing import Any, Iterable


def ensure_dir(path: str | Path) -> Path:
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def write_json(path: str | Path, data: dict[str, Any]) -> None:
    path = Path(path)
    ensure_dir(path.parent)
    path.write_text(json.dumps(_json_safe(data), indent=2, sort_keys=True, allow_nan=False), encoding="utf-8")


def _json_safe(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: _json_safe(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_json_safe(item) for item in value]
    if isinstance(value, float) and not math.isfinite(value):
        return None
    return value


def write_table(path_without_suffix: str | Path, rows: Iterable[dict[str, Any]]) -> Path:
    rows = list(rows)
    base = Path(path_without_suffix)
    ensure_dir(base.parent)
    if not rows:
        out = base.with_suffix(".csv")
        out.write_text("", encoding="utf-8")
        return out
    try:
        import pandas as pd

        out = base.with_suffix(".parquet")
        pd.DataFrame(rows).to_parquet(out, index=False)
        return out
    except Exception:
        out = base.with_suffix(".csv")
        with out.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
        return out

