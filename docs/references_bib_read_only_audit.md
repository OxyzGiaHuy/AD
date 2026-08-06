# Read-only audit of `references.bib`

**Audit date:** 4 August 2026  
**Scope:** The manuscript bibliography was inspected but not edited, in accordance with the author's request. This file is a handoff for the author-owned bibliography pass.

## Critical additions

### MPDD dataset paper

Add the dataset paper and cite it at the first MPDD description in `sections/experiments.tex`.

```bibtex
@inproceedings{jezek2021mpdd,
  author    = {Jezek, Stepan and Jonak, Martin and Burget, Radim and Dvorak, Pavel and Skotak, Milos},
  title     = {Deep Learning-Based Defect Detection of Metal Parts: Evaluating Current Methods in Complex Conditions},
  booktitle = {2021 13th International Congress on Ultra Modern Telecommunications and Control Systems and Workshops (ICUMT)},
  pages     = {66--71},
  year      = {2021},
  doi       = {10.1109/ICUMT54235.2021.9631567}
}
```

Authoritative dataset repository and requested citation: <https://github.com/stepanje/MPDD>. DOI: <https://doi.org/10.1109/ICUMT54235.2021.9631567>.

Suggested textual insertion:

```latex
The strict external-transfer audit additionally incorporates MPDD~\cite{jezek2021mpdd}.
```

### Clopper--Pearson construction

Add the primary source and cite the first use of the one-sided exact binomial bound in Method.

```bibtex
@article{clopper1934binomial,
  author  = {Clopper, C. J. and Pearson, E. S.},
  title   = {The Use of Confidence or Fiducial Limits Illustrated in the Case of the Binomial},
  journal = {Biometrika},
  volume  = {26},
  number  = {4},
  pages   = {404--413},
  year    = {1934},
  doi     = {10.1093/biomet/26.4.404}
}
```

Publisher record: <https://doi.org/10.1093/biomet/26.4.404>.

### Hoeffding inequality

Add the primary source and cite the first definition of the category-risk UCB or the sentence immediately introducing the inequality.

```bibtex
@article{hoeffding1963probability,
  author  = {Hoeffding, Wassily},
  title   = {Probability Inequalities for Sums of Bounded Random Variables},
  journal = {Journal of the American Statistical Association},
  volume  = {58},
  number  = {301},
  pages   = {13--30},
  year    = {1963},
  doi     = {10.1080/01621459.1963.10500830}
}
```

Publisher record: <https://doi.org/10.1080/01621459.1963.10500830>.

### Classical zero-failure lineage

Proposition 3 contains an exact Bernoulli lower-bound argument, not merely the approximate rule of three. Nevertheless, cite the classical zero-numerator lineage to avoid implying that the general zero-failure idea is new.

```bibtex
@article{hanley1983zero,
  author  = {Hanley, James A. and Lippman-Hand, Abby},
  title   = {If Nothing Goes Wrong, Is Everything All Right? Interpreting Zero Numerators},
  journal = {JAMA},
  volume  = {249},
  number  = {13},
  pages   = {1743--1745},
  year    = {1983},
  doi     = {10.1001/jama.1983.03330370053031}
}
```

Publisher record: <https://doi.org/10.1001/jama.1983.03330370053031>.

Suggested citation location: after the sentence stating that the Bernoulli counterexample is elementary. Do not call Proposition 3 “the rule of three”; its statement is exact, distribution-free over bounded losses, and parameterized by arbitrary confidence level.

### Hierarchical conformal prediction

Add Dunn, Wasserman, and Ramdas because their two-layer hierarchical setting is the closest established statistical precedent for treating categories as groups containing repeated observations. Omitting it would leave the image-versus-category discussion under-positioned.

```bibtex
@article{dunn2023hierarchical,
  author  = {Dunn, Robin and Wasserman, Larry and Ramdas, Aaditya},
  title   = {Distribution-Free Prediction Sets for Two-Layer Hierarchical Models},
  journal = {Journal of the American Statistical Association},
  volume  = {118},
  number  = {544},
  pages   = {2491--2502},
  year    = {2023},
  doi     = {10.1080/01621459.2022.2060112}
}
```

Publisher issue record: <https://www.tandfonline.com/toc/uasa20/118/544>. DOI: <https://doi.org/10.1080/01621459.2022.2060112>.

Suggested insertion in the conformal related-work subsection, after the sentence on auxiliary-task transfer:

```latex
Hierarchical conformal work also treated observations nested within exchangeable groups and distinguished pooled, subsampled, and repeated-subsampling constructions for prediction on a new group~\cite{dunn2023hierarchical}. This precedent reinforces why source images cannot be counted as independent categories; CRESS instead certifies a bounded category-level alarm loss rather than constructing a hierarchical prediction set.
```

This citation narrows the novelty claim appropriately: CRESS is not the first method to recognize hierarchical exchangeability, but its alarm-risk estimand, disjoint threshold-proposal/certification roles, and explicit category-budget audit differ from that prediction-set construction.

### Recent hierarchical group-conditional risk control

A July 2026 preprint, verified on arXiv on 4 August 2026, is sufficiently close
in terminology that it should be acknowledged if it remains public at
submission. It calibrates simultaneous
selective-prediction risks over nodes of a pre-specified hierarchy of observed
groups; it does not study source-to-unseen-category anomaly thresholds or the
independent-category budget derived here.

```bibtex
@misc{salem2026hierarchical,
  author        = {Salem, Murilo and B{\"o}hm, Lu{\'i}sa and Pontes, Daniel and Ferrugem, Anderson},
  title         = {Hierarchical Group-Conditional Conformal Risk Control for Selective Prediction in Language Models},
  year          = {2026},
  eprint        = {2607.24562},
  archiveprefix = {arXiv},
  primaryclass  = {cs.AI},
  url           = {https://arxiv.org/abs/2607.24562}
}
```

Suggested concise comparison after the general conformal-risk-control paragraph:

```latex
Recent hierarchical group-conditional risk control calibrated simultaneous
selective-prediction risks over a pre-specified hierarchy of observed groups~\cite{salem2026hierarchical}. Its target is a known hierarchy node; our question instead concerns how independent source categories can support a threshold claim for a new industrial category.
```

Recheck the arXiv metadata immediately before submission because this record is
very recent. This citation is a novelty guardrail, not a claim that the two
procedures solve the same estimand.

Do not confuse this record with arXiv:2607.25273. The latter is HeAD-CP by Lam
and Nguyen and concerns graph diffusion for conformal prediction sets;
arXiv:2607.24562 is the Salem et al. hierarchical group-conditional risk-control
preprint. Both are relevant for different reasons and require distinct entries.

## Corrections to existing entries

### DINOv2

The current entry says `Transactions on Machine Learning Research Journal`, which is not the venue name, and loses the capitalization of DINOv2. Use `Transactions on Machine Learning Research` and protect the method name:

```bibtex
title   = {{DINOv2}: Learning Robust Visual Features Without Supervision},
journal = {Transactions on Machine Learning Research},
year    = {2024}
```

The TMLR record identifies the work as a 2024 TMLR article: <https://mlanthology.org/tmlr/2024/oquab2024tmlr-dinov2/>.

### AnomalyDINO and other method names

Protect method-name capitalization in titles, for example `{AnomalyDINO}`, `{DINOv2}`, `{WinCLIP}`, `{PaDiM}`, `{DRAEM}`, `{GraphCore}`, and `{FastRecon}`. This is a typesetting correction and does not change attribution.

### UniAD DOI field

The current `doi` field incorrectly contains a URL. Keep a bare DOI:

```bibtex
doi = {10.1016/j.neucom.2025.132372}
```

The article is in *Neurocomputing*, volume 667, article 132372, dated 28 February 2026: <https://doi.org/10.1016/j.neucom.2025.132372>. A separate `url` field is optional; do not encode the same DOI twice in two URL forms.

### Stray SubspaceAD block

Lines near the beginning of the file contain `%@misc{,` followed by uncommented fields and a closing brace, then a valid `subspacead2026` entry. BibTeX currently tolerates this stray text, but it is malformed source and should be removed. Retain only the valid cited entry.

### HeAD-CP status

The existing note `Accepted at MAPR 2026` is now supported by the official conference accepted-paper list: <https://mapr.uit.edu.vn/list-accepted-papers-mapr-2026>. The arXiv record is <https://arxiv.org/abs/2607.25273>. Until proceedings metadata are public, retaining an arXiv `@misc` entry with the acceptance note is more accurate than inventing pages, DOI, or a proceedings record. Recheck at the final submission date.

### SAGE status

The existing SAGE entry matches the official CVF Open Access record, including title, author list, venue, year, and pages 7337--7346: <https://openaccess.thecvf.com/content/CVPR2026F/html/Thai_SAGE_Shape-Adapting_Gated_Experts_for_Adaptive_Histopathology_Image_Segmentation_CVPRF_2026_paper.html>. No status correction is needed.

### MVTec citation key

The key `mvtec2019` may remain even though the cited journal article is dated 2021. BibTeX keys are internal identifiers and do not affect scientific integrity; only the printed metadata and the mapping from citation to source matter.

## Final bibliography checks after editing

1. Compile with BibTeX and confirm `main.blg` reports zero warnings.
2. Confirm every DOI is bare (`10....`), resolvable, and belongs to the cited item.
3. Confirm article numbers are stored as article numbers or `pages` consistently with the CAS style.
4. Protect acronyms and method names from automatic sentence-case conversion.
5. Prefer the final peer-reviewed record over an arXiv entry when both identify the same work; do not keep duplicate entries for one source.
6. Recheck 2026 preprints and accepted papers immediately before submission because their venue metadata may have changed.
