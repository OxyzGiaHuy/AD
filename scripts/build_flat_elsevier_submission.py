"""Build a self-contained, single-directory Elsevier submission package.

Elsevier Editorial Manager does not reliably process LaTeX subdirectories.
This builder leaves the working manuscript untouched, copies only files used by
the compiled paper, and rewrites directory-qualified inputs in the generated
copy.  It intentionally refuses to populate a non-empty destination so stale
or unrelated files cannot be silently included in a submission.
"""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path


SECTIONS = (
    "abstract",
    "introduction",
    "related_work",
    "method",
    "experiments",
    "results",
    "limitations",
    "conclusion",
    "appendix",
    "declarations",
)

TABLES = (
    "tab_certificate_feasibility",
    "tab_attainable_alpha",
    "tab_false_alarm_control",
    "tab_strict_nested_sc3r",
    "tab_pooled_source_conformal",
    "tab_clean_efficiency",
    "tab_agg_ablation",
)

FIGURES = (
    "fig_certificate_feasibility.pdf",
    "fig_target_pipeline.pdf",
    "fig_cress_pipeline.pdf",
    "fig_uniformity_cdf.pdf",
)


def copy_text(source: Path, destination: Path, replacements: dict[str, str]) -> None:
    text = source.read_text(encoding="utf-8")
    for old, new in replacements.items():
        text = text.replace(old, new)
    destination.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--destination", required=True, type=Path)
    args = parser.parse_args()

    source = args.source.resolve()
    destination = args.destination.resolve()
    if not (source / "main.tex").is_file():
        raise FileNotFoundError(f"Missing manuscript entry point: {source / 'main.tex'}")
    if destination.exists() and any(destination.iterdir()):
        raise RuntimeError(
            f"Refusing to write into non-empty destination: {destination}. "
            "Move or remove the generated package explicitly before rebuilding."
        )
    destination.mkdir(parents=True, exist_ok=True)

    main_replacements = {
        r"\graphicspath{{./}{figures/}}": r"\graphicspath{{./}}",
        **{rf"\input{{sections/{name}}}": rf"\input{{{name}}}" for name in SECTIONS},
    }
    copy_text(source / "main.tex", destination / "main.tex", main_replacements)

    table_replacements = {
        rf"\input{{tables/{name}}}": rf"\input{{{name}}}" for name in TABLES
    }
    for name in SECTIONS:
        copy_text(
            source / "sections" / f"{name}.tex",
            destination / f"{name}.tex",
            table_replacements,
        )

    for name in TABLES:
        shutil.copy2(source / "tables" / f"{name}.tex", destination / f"{name}.tex")
    for filename in FIGURES:
        shutil.copy2(source / "figures" / filename, destination / filename)

    # Elsevier lists the generated bibliography among the LaTeX source files.
    # Copying both the .bib and the freshly compiled .bbl also makes the package
    # robust to Editorial Manager configurations that do not rerun BibTeX.
    for filename in (
        "references.bib",
        "main.bbl",
        "cas-dc.cls",
        "cas-model2-names.bst",
    ):
        shutil.copy2(source / filename, destination / filename)

    common_replacements = {
        "thumbnails/cas-email.jpeg": "cas-email.jpeg",
        "thumbnails/cas-url.jpeg": "cas-url.jpeg",
        "thumbnails/cas-facebook.jpeg": "cas-facebook.jpeg",
        "thumbnails/cas-twitter.jpeg": "cas-twitter.jpeg",
        "thumbnails/cas-gplus.jpeg": "cas-gplus.jpeg",
        "thumbnails/cas-linkedin.jpeg": "cas-linkedin.jpeg",
    }
    copy_text(
        source / "cas-common.sty",
        destination / "cas-common.sty",
        common_replacements,
    )
    for thumbnail in sorted((source / "thumbnails").glob("*.jpeg")):
        shutil.copy2(thumbnail, destination / thumbnail.name)

    for optional in ("cover_letter.md", "highlights.txt"):
        if (source / optional).is_file():
            shutil.copy2(source / optional, destination / optional)

    included = sorted(path.name for path in destination.iterdir() if path.is_file())
    readme = (
        "# Flat Elsevier submission package\n\n"
        "Generated from the feasibility-first working manuscript. All LaTeX "
        "sources, tables, figures, class/style dependencies, thumbnails, and "
        "bibliography files are intentionally at one directory level for "
        "Editorial Manager compatibility.\n\n"
        "Build command: `latexmk -pdf -interaction=nonstopmode "
        "-halt-on-error main.tex`\n\n"
        "Included files:\n\n"
        + "".join(f"- `{name}`\n" for name in included)
    )
    (destination / "README.md").write_text(readme, encoding="utf-8")
    print(destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
