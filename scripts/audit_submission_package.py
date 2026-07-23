"""Fail-closed audit for the final Neurocomputing submission package."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess


FORBIDDEN_CLAIM_PATTERNS = {
    "unsupported preregistration": r"pre-registered|preregistered",
    "unqualified target validity": r"restores validity|guarantees? target|controls? target FAR",
    "unqualified fail-safe wording": r"(?<!not a general )fail[- ]safe property|transfers conservatively",
}
PLACEHOLDER_PATTERNS = {
    "placeholder author": r"First Author|Second Author|Anonymous Author|Author Name",
    "placeholder email": r"author@example\.com|example\.edu",
    "placeholder repository": r"REPLACE_WITH|INSERT_(?:URL|DOI|COMMIT)|(?:anonymous|reviewer-accessible) repository identifier",
    "generic TODO": r"\bTODO\b|\bTBD\b",
}


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _latex_word_count(text: str) -> int:
    text = re.sub(r"%.*", " ", text)
    text = re.sub(r"\\(?:cite|ref|label|input)\w*\{[^{}]*\}", " ", text)
    text = re.sub(r"\\[A-Za-z@]+\*?(?:\[[^]]*\])?", " ", text)
    text = text.replace("{", " ").replace("}", " ").replace("$", " ")
    return len(re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*", text))


def _resolve_manifest_artifact(
    recorded_path: str,
    recorded_project_root: Path | None,
    local_project_root: Path,
) -> Path:
    """Resolve an artifact after a manifest has moved to another checkout."""
    artifact = Path(recorded_path)
    if artifact.is_file() or not artifact.is_absolute() or recorded_project_root is None:
        return artifact
    try:
        relative = artifact.relative_to(recorded_project_root)
    except ValueError:
        return artifact
    return local_project_root / relative


def _verify_cpu_manifest(path: Path, local_project_root: Path) -> list[str]:
    issues: list[str] = []
    if not path.is_file():
        return [f"CPU manifest does not exist: {path}"]
    manifest = json.loads(path.read_text(encoding="utf-8"))
    recorded_config = Path(manifest.get("config", ""))
    recorded_project_root = (
        recorded_config.parent.parent
        if recorded_config.is_absolute() and recorded_config.parent.name == "configs"
        else None
    )
    if not manifest.get("runs") or not manifest.get("confirmatory_family"):
        issues.append("CPU manifest lacks runs or confirmatory-family metadata")
    if not manifest.get("empirical_target_gate"):
        issues.append("CPU manifest lacks the zero-preserving empirical target-gate report")
    for name, audit in manifest.get("artifact_audits", {}).items():
        if audit.get("status") != "pass":
            issues.append(f"CPU manifest contains a failed artifact audit: {name}")
    required_methods = {"target_only", "pooled_source_conformal", "nested_sc3r"}
    for run in manifest.get("runs", []):
        if not required_methods.issubset(set(run.get("methods", []))):
            issues.append(f"CPU manifest run lacks required paired methods: {run.get('tag')}")
    family = manifest.get("confirmatory_family", {})
    if family.get("multiplicity") != "bonferroni" or int(family.get("family_size", 0)) < 1:
        issues.append("CPU manifest lacks a nonempty Bonferroni confirmatory family")
    for section in ("inputs", "outputs"):
        for name, record in manifest.get(section, {}).items():
            artifact = _resolve_manifest_artifact(
                record.get("path", ""),
                recorded_project_root,
                local_project_root,
            )
            if not artifact.is_file():
                issues.append(f"CPU manifest {section} artifact missing: {name}")
            elif _sha256(artifact) != record.get("sha256"):
                issues.append(f"CPU manifest checksum mismatch: {name}")
    output_names = set(manifest.get("outputs", {}))
    for fragment in ("paired_cells", "_summary.csv", "empirical_gate.json"):
        if not any(fragment in name for name in output_names):
            issues.append(f"CPU manifest lacks required aggregated output matching {fragment!r}")
    git_state = manifest.get("environment", {}).get("git", {})
    if git_state.get("commit") is None:
        issues.append("CPU manifest lacks an immutable git commit")
    if git_state.get("dirty") is not False:
        issues.append("CPU manifest was generated from a dirty or unknown worktree")
    return issues


def audit_submission(root: Path, cpu_manifest: Path | None = None) -> dict:
    root = root.resolve()
    issues: list[str] = []
    manuscript_files = [
        root / "main.tex", *sorted((root / "sections").glob("*.tex")),
        *sorted((root / "tables").glob("*.tex")), root / "cover_letter.md",
    ]
    missing = [str(path) for path in manuscript_files if not path.is_file()]
    if missing:
        issues.extend(f"missing submission source: {path}" for path in missing)
    corpus = "\n".join(path.read_text(encoding="utf-8") for path in manuscript_files if path.is_file())
    for label, pattern in PLACEHOLDER_PATTERNS.items():
        if re.search(pattern, corpus, flags=re.IGNORECASE):
            issues.append(label)
    for label, pattern in FORBIDDEN_CLAIM_PATTERNS.items():
        if re.search(pattern, corpus, flags=re.IGNORECASE):
            issues.append(label)

    abstract_path = root / "sections" / "abstract.tex"
    abstract_words = _latex_word_count(abstract_path.read_text(encoding="utf-8")) if abstract_path.is_file() else 0
    if abstract_words > 250:
        issues.append(f"abstract exceeds 250 words ({abstract_words})")

    highlights_path = root / "highlights.txt"
    if not highlights_path.is_file():
        issues.append("separate editable highlights.txt is missing")
        highlight_lengths: list[int] = []
    else:
        highlights = [line.strip().lstrip("-* ").strip() for line in highlights_path.read_text(encoding="utf-8").splitlines() if line.strip()]
        highlight_lengths = [len(line) for line in highlights]
        if not 3 <= len(highlights) <= 5:
            issues.append(f"highlights must contain 3--5 items (found {len(highlights)})")
        if any(length > 85 for length in highlight_lengths):
            issues.append(f"highlight exceeds 85 characters (lengths={highlight_lengths})")
        main_text = (root / "main.tex").read_text(encoding="utf-8") if (root / "main.tex").is_file() else ""
        block = re.search(r"\\begin\{highlights\}(.*?)\\end\{highlights\}", main_text, flags=re.DOTALL)
        embedded = re.findall(r"\\item\s+([^\n]+)", block.group(1)) if block else []
        embedded = [re.sub(r"\s+", " ", item).strip() for item in embedded]
        if embedded != highlights:
            issues.append("highlights.txt and main.tex highlights differ")

    main_text = (root / "main.tex").read_text(encoding="utf-8") if (root / "main.tex").is_file() else ""
    keyword_block = re.search(r"\\begin\{keywords\}(.*?)\\end\{keywords\}", main_text, flags=re.DOTALL)
    keyword_count = len(keyword_block.group(1).split(r"\sep")) if keyword_block else 0
    if not 1 <= keyword_count <= 7:
        issues.append(f"keyword count must be 1--7 (found {keyword_count})")

    biography = root / "author_biographies.md"
    if not biography.is_file():
        issues.append("author_biographies.md is missing")
    author_photos = [
        *root.glob("author_photo_*.png"), *root.glob("author_photo_*.jpg"),
        *root.glob("author_photo_*.jpeg"),
    ]
    if not author_photos:
        issues.append("author passport-type photograph files are missing")

    if (root / "main.abs").exists():
        issues.append("generated main.abs is present")
    pdf = root / "main.pdf"
    if not pdf.is_file():
        issues.append("main.pdf is missing")
        pages = None
    else:
        try:
            info = subprocess.run(["pdfinfo", str(pdf)], check=True, capture_output=True, text=True).stdout
            match = re.search(r"^Pages:\s+(\d+)", info, flags=re.MULTILINE)
            pages = int(match.group(1)) if match else None
        except (FileNotFoundError, subprocess.CalledProcessError):
            pages = None
            issues.append("main.pdf could not be inspected with pdfinfo")

    log = root / "main.log"
    if not log.is_file():
        issues.append("main.log is missing; clean compilation is unverified")
    else:
        log_text = log.read_text(encoding="utf-8", errors="replace")
        for label, pattern in {
            "undefined LaTeX references": r"(?:Citation|Reference).*undefined|There were undefined references",
            "BibTeX empty pages": r"empty pages in",
            "invalid float position": r"No positions in optional float specifier",
            # CAS emits "Ignoring empty anchor" for its unnumbered author
            # footnotes; that warning is benign and is not a duplicate
            # destination. Fail only on an actual duplicate identifier.
            "duplicate PDF anchor": r"destination with the same identifier.*duplicate ignored",
        }.items():
            if re.search(pattern, log_text, flags=re.IGNORECASE):
                issues.append(label)

    if cpu_manifest is None:
        issues.append("final CPU pipeline manifest was not supplied")
    else:
        issues.extend(_verify_cpu_manifest(cpu_manifest.resolve(), root.parent))

    return {
        "status": "pass" if not issues else "fail",
        "issues": issues,
        "abstract_words": abstract_words,
        "highlight_lengths": highlight_lengths,
        "keyword_count": keyword_count,
        "pdf_pages": pages,
        "root": str(root),
        "cpu_manifest": str(cpu_manifest.resolve()) if cpu_manifest else None,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="els-cas-templates")
    parser.add_argument("--cpu-manifest", default=None)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    report = audit_submission(Path(args.root), Path(args.cpu_manifest) if args.cpu_manifest else None)
    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
