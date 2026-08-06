# Feasibility-first rewrite progress report

**Working copy:** `els-cas-templates-feasibility-first/`

**Protected source:** `els-cas-templates/` — không chỉnh sửa trong quá trình rewrite.

**Source plan:** `docs/feasibility_first_vs_current_paper_vi.md`

**Mục tiêu:** tái định vị paper từ CRESS-first sang feasibility-first bằng cách thay đổi framing, thứ tự và cách diễn đạt; giữ nguyên raw evidence, statistical estimands và scientific limitations.

## Status legend

- `[ ]` Chưa bắt đầu
- `[~]` Đang thực hiện
- `[x]` Hoàn tất và đã kiểm tra
- `[!]` Blocked hoặc cần quyết định/tài nguyên ngoài CPU

## Phase status

### Phase 0 — Freeze evidence and working copy

- [x] Tạo bản sao `els-cas-templates-feasibility-first`.
- [x] Giữ nguyên folder `els-cas-templates` làm bản đối chiếu.
- [x] Lập headline-number ledger và map artifact nguồn.
- [x] Chụp baseline compile status của bản sao.

### Phase 1 — Theory and claim audit

- [x] Kiểm tra lại source certificate, Hoeffding feasibility, distribution-free lower bound và Corollary.
- [x] Tái tính `14/29/59`, family-adjusted DF limits và Hoeffding requirements bằng công thức độc lập.
- [x] Kiểm tra đúng phạm vi iid/category/unit/multiplicity.
- [x] Hạ target-only floor thành Remark 1; renumber ba propositions trung tâm.

### Phase 2 — Feasibility Figure 1

- [x] Tạo TikZ/PGFPlots source trực tiếp từ formulas.
- [x] Tạo vector PDF.
- [x] Kiểm tra crossings, integer ceiling, clipping và annotations.
- [x] Kiểm tra khả năng đọc ở journal size trong full-paper PDF.
- [x] Kiểm tra bản thang xám; ba đường lý thuyết vẫn phân biệt bằng solid/dashed/dash-dot và marker khác nhau.

### Phase 3 — Paper identity

- [x] Chọn working title limit-first và short title.
- [x] Chốt central question, central answer và central takeaway.
- [x] Chốt contribution hierarchy gồm ba contribution.

### Phase 4 — Abstract and Introduction

- [x] Viết lại Abstract theo headline tái lập được `0.341` và evidence-unit question.
- [x] Viết lại Introduction theo feasibility-first narrative.
- [x] Rút contributions từ bốn xuống ba.
- [x] Kiểm tra abstract khoảng 244–246 từ và các claim qualifiers.

### Phase 5 — Method

- [x] Đưa estimand/unit distinction lên Problem Setup.
- [x] Giữ scorer như inherited substrate.
- [x] Hạ target-only floor thành Remark.
- [x] Đặt feasibility calculus sau certificate definition.
- [x] Pipeline tự động trở thành Figure 2; references và caption đã kiểm tra.

### Phase 6 — Results

- [x] Shift audit đứng đầu với điều kiện đầy đủ cho `0.341`.
- [x] Feasibility calculus và Figure 1 đứng tiếp theo.
- [x] Strict CRESS trình bày category/image contrast trong cùng subsection.
- [x] Ranking/storage chuyển thành supporting substrate.
- [x] Secondary diagnostics được nén và sắp lại.
- [x] Prior-work positioning table được bỏ khỏi compiled appendix và thay bằng prose.

### Phase 7 — Limitations and Conclusion

- [x] Sửa Limitations theo claim hierarchy mới.
- [x] Sửa Conclusion theo feasibility-first takeaway và present-perfect style.

### Phase 8 — Consistency and integrity audit

- [x] Dò claim-sensitive terms toàn manuscript.
- [x] Kiểm tra equations, labels, references và float order.
- [x] Compile nhiều vòng thành PDF 16 trang; không có undefined citation/reference.
- [x] So sánh headline numbers với protected source; không thay numeric table cells.

### Phase 9 — Adversarial review

- [x] AD reviewer lens.
- [x] Statistical reviewer lens.
- [x] Neurocomputing/Q1 reviewer lens.
- [x] Ghi remaining risks và GPU requirement.

## Evidence ledger

| Quantity | Current source | Required interpretation | Audit status |
| --- | --- | --- | --- |
| `0.341` | `tab_false_alarm_control.tex` | Empirical FAR, MVTec Gaussian noise, `k=4`, nominal `alpha=.20`; not population FAR | audited |
| `0.278` | `results.tex` / attainable-alpha summary | Mean of four corruption-specific pooled MVTec FARs at `k=4` | audited |
| `14/29/59` | distribution-free proposition / certificate feasibility table | Multiplicity-free DF lower limits, `beta=.05`, all-zero category losses | audited |
| `22/46/94` | certificate feasibility table | Frozen allocation DF lower limits at `A=3, M=1` | audited |
| `60/240/958` | Hoeffding proposition / table | Declared Hoeffding requirement at `A=3, M=1, delta=.05` | audited |
| `0/960` | strict nested CRESS table/results | Every category-certified target cell receives zero across 960 configurations; configurations are not independent trials | audited |
| `0.950–1.000` | strict nested CRESS table | Observed minimum category UCB range across jobs | audited |
| `36.7%–60.3%` | strict nested CRESS image-unit rows | Positive-threshold fraction among target cells for the idealized selected-source-mixture image estimand only | audited |

## GPU status

No GPU task is required for the completed rewrite. The formula audit, feasibility plot, per-category heterogeneity summary, and LaTeX compilation are CPU-only and are backed by the frozen local artifacts. Re-running the same jobs cannot increase the number of independent certification categories.

## Change log

- Created protected working copy and initialized this report.
- Verified the feasibility table independently: `14/29/59`, `22/46/94`, and `60/240/958` match the stated formulas after integer ceiling.
- Added reproducible vector Figure 1 in TikZ/PGFPlots. An initial marker placement used the nominal alpha coordinate; adversarial visual audit caught and corrected it to the actual curve value at each minimum integer count.
- Redesigned Figure 1 with a colorblind-safe palette, line-style and marker redundancy for grayscale printing, an unobstructed frozen-audit band, white-backed annotations, and two concise study-design callouts. The plotted formulas and key quantities are now protected by the manuscript audit.
- Changed working title to `How Many Categories Are Enough? Distribution-Free Certification Limits for Few-Shot Anomaly Thresholds`.
- Rewrote Abstract and Introduction; CRESS now operationalizes the feasibility audit rather than leading as a positive method claim.
- Added statistical-unit language to Method and converted the target-only floor from a main proposition to a remark.
- Reordered Results to shift audit → feasibility → CRESS boundary test → ranking substrate → secondary diagnostics.
- Moved prior-work positioning into Related Work prose and retained the scoped SAGE inspiration statement.
- Rewrote Limitations and Conclusion under the new claim hierarchy.
- Compiled `main.pdf` to 17 pages after final artwork integration; checked Figures 1 to 4, main result tables, page footer, references and float order visually.
- Confirmed `references.bib` is unchanged from the protected copy and no numeric result cells were edited.

## Adversarial review summary

### AD reviewer lens

- **Likely objection:** the ranker is not novel. **Resolution:** the paper now states that DINOv2 PCA residual ranking is inherited and moves ranking/storage to supporting evidence.
- **Likely objection:** Gaussian corruption is synthetic and the `0.341` cell may be overemphasized. **Resolution:** every occurrence identifies MVTec, Gaussian noise, `k=4`, and `alpha=.20`, and distinguishes the cell from the MVTec aggregate `0.278` and from population FAR.
- **Remaining risk:** real production shifts are not tested; retained explicitly in Limitations.

### Statistical reviewer lens

- **Likely objection:** `14/29/59` may be misread as sufficient CRESS sample sizes. **Resolution:** manuscript and Figure 1 label them as optimistic necessary lower limits; family-adjusted and Hoeffding counts are reported nearby.
- **Likely objection:** image counts are substituted for category counts. **Resolution:** estimands are defined before CRESS; all positive image-unit rates are labeled fixed-archive sensitivity.
- **Likely objection:** 960 configurations are treated as independent evidence. **Resolution:** Abstract, Introduction, Results and Conclusion now state the target-cell result across a shared frozen grid and deny an independent-trial interpretation.
- **Likely objection:** source certificate implies target control. **Resolution:** target transfer remains conditional on dominance or category exchangeability.

### Neurocomputing/Q1 reviewer lens

- **Strength:** the paper now has one research question, a quantitative answer, a memorable Figure 1 and a protocol-level empirical validation.
- **Risk:** Proposition 3 is mathematically elementary if isolated. The manuscript therefore frames novelty as the combined feasibility calculus, shift audit, estimand separation and frozen boundary test—not as a deep standalone theorem.
- **Risk:** no positive new-category certificate is obtained. The paper now treats fail-closed behavior as the predicted design boundary and states practical study-design consequences rather than claiming deployment improvement.

## Remaining human-review items

1. Advisor/author should approve the working title. The separate title memo explains why “Counting Categories, Not Images” is more memorable but must retain “feasibility limits” so that image evidence is not dismissed and necessary counts are not presented as sufficient budgets.
2. A statistically specialized human reviewer should independently verify the propositions and the intended category meta-population before submission.
3. Retain the current category-level heterogeneity summary for the `0.341` headline (median `0.215`, IQR `0.169–0.481`, 9 of 15 categories above `0.20`); do not convert the five support seeds into independent replication.
4. Perform the author's final bibliography pass separately; this rewrite intentionally leaves `references.bib` untouched.
