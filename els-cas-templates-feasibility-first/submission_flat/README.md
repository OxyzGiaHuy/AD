# STALE PACKAGE — DO NOT SUBMIT

This directory predates the current iid/target-transfer corrections and the
compiled appendix. It is retained only as a local packaging trace. Generate a
fresh package with `scripts/build_flat_elsevier_submission.py` after the final
pipeline artwork and bibliography are complete.

# Flat Elsevier submission package

Generated from the feasibility-first working manuscript. All LaTeX sources, tables, figures, class/style dependencies, thumbnails, and bibliography files are intentionally at one directory level for Editorial Manager compatibility. The two pipeline figures remain LaTeX placeholders in `method.tex` until final artwork is supplied.

Build command: `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`

Included files:

- `abstract.tex`
- `cas-common.sty`
- `cas-dc.cls`
- `cas-email.jpeg`
- `cas-facebook.jpeg`
- `cas-gplus.jpeg`
- `cas-linkedin.jpeg`
- `cas-twitter.jpeg`
- `cas-url.jpeg`
- `conclusion.tex`
- `cover_letter.md`
- `declarations.tex`
- `elsarticle-num.bst`
- `experiments.tex`
- `fig_certificate_feasibility.pdf`
- `fig_uniformity_cdf.pdf`
- `highlights.txt`
- `introduction.tex`
- `limitations.tex`
- `main.tex`
- `method.tex`
- `references.bib`
- `related_work.tex`
- `results.tex`
- `tab_attainable_alpha.tex`
- `tab_certificate_feasibility.tex`
- `tab_clean_efficiency.tex`
- `tab_false_alarm_control.tex`
- `tab_pooled_source_conformal.tex`
- `tab_strict_nested_sc3r.tex`
