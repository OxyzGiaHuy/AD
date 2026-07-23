# Prompt GPT-5.5 tạo pipeline figure cho paper CRR/SC3R

## Cách dùng

Đính kèm figure hiện tại `els-cas-templates/figures/fig_pipeline.pdf` nếu giao
diện cho phép, sau đó copy nguyên prompt bên dưới. Figure cũ chỉ là content
reference; GPT-5.5 phải thiết kế lại, không được chép nguyên layout.

Nếu GPT-5.5 có thể xuất nhiều định dạng, ưu tiên **SVG editable** và **PDF
vector**, kèm PNG preview. Không dùng PNG raster làm source cuối của paper.

---

## MASTER PROMPT

You are a senior scientific illustrator and machine-learning paper editor. Create
one publication-ready **method pipeline figure** for a two-column Elsevier
Neurocomputing manuscript on few-shot industrial anomaly detection.

The paper is titled “Conformal Reliability Routing for Low-Storage Few-Shot
Industrial Anomaly Detection.” Its framework is CRR, and its strict
source-assisted component is SC3R. The figure must be scientifically exact,
visually restrained, and understandable without reading the full paper.

### Output requirements

- Produce a clean horizontal vector-style schematic for a full-width
  `figure*`, final size approximately **178 mm × 92–100 mm**.
- White background; no decorative background, shadows, gradients, 3D,
  photorealism, neural-network brain imagery, glowing effects, or stock icons.
- Use a restrained, color-blind-safe palette:
  - shared feature extraction: muted navy/blue;
  - ranking lane: teal;
  - target-only reliability lane: amber;
  - strict SC3R lane: muted vermilion/red;
  - baselines, assumptions, and notes: neutral gray.
- The figure must remain understandable in grayscale. Combine color with lane
  labels, border styles, and grouping—not color alone.
- Use one professional sans-serif font resembling Helvetica/Arial. All text must
  remain at least 7.5–8 pt at final print size. Use consistent line weights,
  aligned boxes, generous white space, and orthogonal or gently curved arrows.
- Do **not** render every component as the same rounded rectangle. Use the
  functional shape grammar below consistently. Shape must encode function, not
  decorate the page.
- Do not place a title or caption inside the figure.
- Prefer short exact labels. Do not invent metrics, results, guarantees,
  components, datasets, or mathematical claims.
- Render every mathematical token exactly. Do not misspell DINOv2, LOIO, SC3R,
  Clopper–Pearson, Hoeffding, AUROC, AP, PCA, MAD, or UCB.
- If direct vector export is supported, return an editable SVG and vector PDF,
  plus a 300 dpi PNG preview. Keep text as editable text where possible.

### Mandatory functional shape grammar

Use no more than these seven shape families:

1. **Data / image collections:** stacked-card shapes with a subtle offset layer
   behind the front card. Use for target supports, query image, source-normal
   archive, patch features, and LOIO residual collections.
2. **Learned or fitted representation:** a compact hexagon with flat left and
   right sides. Use for `Frozen DINOv2 ViT-S/14` and `PCA64 subspace`.
3. **Deterministic processing operation:** a clean rounded rectangle. Use for
   patch-residual computation, aggregation, condition routing, normalization,
   p-value construction, and candidate generation.
4. **Partition / held-out roles:** three adjacent vertical tabbed cards, labeled
   R, P, and C. They must look mutually disjoint, not like three steps sharing
   the same data.
5. **Decision or statistical gate:** a diamond. Use only for
   `α < 1/(k+1)?` and `UCB(τ) ≤ α?`.
6. **Certificate / bound:** a shield-like or document-with-seal shape. Use only
   for the simultaneous source-risk UCB and the conditional source certificate.
   Keep it flat and minimal—no glossy badge or security-logo styling.
7. **Final output:** a pill/capsule shape. Use for raw score/map, selected
   threshold, no-alarm fallback, and operational alarm.

Use a thin dashed-outline annotation shape for assumptions, baselines, and
negative controls. Do not introduce circles, clouds, database cylinders, gears,
brains, funnels, or arbitrary polygons. A shape must mean the same thing
everywhere in the figure. Include a very small shape legend only if the mapping
is not self-evident; otherwise omit it.

### Overall composition

Use a left-to-right structure with a compact shared input/feature trunk at the
top and three clearly separated horizontal lanes below it. Make the strict SC3R
lane the visual focus, but do not imply that it changes the ranking score.

#### Shared trunk

Show two inputs:

1. `k target-normal supports 𝒮_t`
2. `query image x`

Both pass through:

`Frozen DINOv2 ViT-S/14` → `Patch features z₁,…,z_P`

Add a small, unobtrusive note: `no target anomaly labels`.

Render both inputs and patch features as stacked cards. Render the frozen
backbone as a hexagon. This establishes the shape vocabulary immediately.

#### Lane A — RANKING (teal)

Label the lane exactly:

`A  RANKING — unchanged by calibration`

Show:

`Support patch features` → `PCA64 subspace fit`

and

`Query patch features` + `PCA64 subspace` → `Patch residual map r(z)` →
`Top-ρ mean (ρ = 0.01)` → `Raw score s(x) + anomaly map`

Render support/query feature collections as stacked cards, the fitted PCA64
subspace as a hexagon, the residual and aggregation steps as rounded processing
rectangles, and the raw-score output as a pill. Do not use a decision diamond
in this lane.

Place `AUROC / AP / localization` as a small output note, not as a training
objective. Make it visually explicit that the calibration and SC3R lanes never
feed back into or modify `s(x)`.

#### Lane B — TARGET-ONLY RELIABILITY (amber)

Label the lane exactly:

`B  TARGET-ONLY RELIABILITY — label-free`

Show:

`k support normals` → `LOIO support residuals` →
`p_LOIO(x) ∈ {1/(k+1), …, 1}`

Then show a clearly recognizable but elegant **resolution barrier**:

`α < 1/(k+1)` → `target-only alarm is structurally silent`

The barrier represents an algebraic attainable-alpha floor, not empirical
failure. Do not draw it as a model error or warning explosion.

Implement this as a diamond labeled `α < 1/(k+1)?`, followed on the `yes` branch
by a muted pill labeled `structurally silent`. Do not create a false `no` branch
that implies guaranteed validity above the floor; instead continue with a thin
neutral arrow labeled `attainable grid point`.

Add one small neutral-gray side box connected with a thin dashed line:

`Secondary calibration baselines`

and below it:

`Platt family · temperature · isotonic · histogram`

This is a comparison branch, not part of the main SC3R algorithm.

#### Lane C — STRICT SC3R (muted vermilion; primary focus)

Label the lane exactly:

`C  STRICT SC3R — source-assisted operation below the floor`

Start with:

`Normal images from other source categories`

Then:

`Condition routing`

Add three compact routing labels:

`matched (metadata-assisted)` · `clean` · `condition-agnostic`

Do not present mismatched routing as operational; if included, place it in a
tiny gray note labeled `mismatched = negative control`.

Continue with:

`Per-category median/MAD normalization`

Then draw three visually distinct, non-overlapping source-category partitions:

- `R  Reference classes` — define source conformal p-values
- `P  Proposal classes` — propose ≤ M candidate thresholds
- `C  Certification classes` — evaluate candidates only

Use arrows `R → P → C`, while making their disjointness visually clear. Target
test images and target labels must not enter R, P, or C.

Render the source archive as stacked cards, routing and normalization as rounded
processing rectangles, and R/P/C as three adjacent tabbed cards inside one
thin container labeled `disjoint source-category roles`.

After the three-way split, show:

`Simultaneous source-risk UCB`

with two compact sublabels:

- `image unit: Clopper–Pearson`
- `category unit: Hoeffding`

Render the UCB as a document-with-seal or minimal shield shape, visibly
different from ordinary processing steps.

Then show the exact decision:

`largest τ with UCB(τ) ≤ α`

and a two-way output:

- pass → `selected threshold τ`
- no candidate passes → `τ = 0 (no-alarm fallback)`

Use one diamond labeled `UCB(τ) ≤ α?`. Its pass branch ends in a vermilion pill
`selected threshold τ`; its fail branch ends in a gray pill
`τ = 0 — no alarm`. Do not place the entire decision sentence in a rectangle.

Finally apply the selected threshold to the query p-value and output:

`Operational alarm at α`

Do not show source anomaly labels; SC3R uses source normal archives.

### Claim-boundary strip

At the bottom, add a thin neutral strip separated from the pipeline:

`Conditional source certificate`

then a dashed arrow labeled:

`requires dominance or category exchangeability`

then:

`Target-domain behavior remains empirical otherwise`

Render the conditional source certificate with the same certificate shape used
for the UCB. Render the transfer condition as a dashed-outline assumption tag,
and the target-domain statement as a neutral output pill. This bottom strip must
remain visually subordinate to the main SC3R flow.

This strip is mandatory. It must prevent the visual from implying an
unconditional target-domain guarantee.

Also include a small lock/note, preferably text-only:

`Target anomaly labels: evaluation only`

### Scientific constraints that must be respected

1. The detector is fitted only on `k` target-normal support images.
2. Calibration does not alter the raw ranking score or anomaly map.
3. LOIO target-only p-values have minimum attainable value `1/(k+1)`.
4. SC3R uses normal images from other categories without target anomaly labels.
5. Reference, proposal, and certification source classes are disjoint.
6. Candidate thresholds may depend on R and P, but C is used only for
   certification.
7. The selected threshold is the largest candidate whose simultaneous
   source-domain UCB is at most α; otherwise the method returns τ = 0.
8. Image-level Clopper–Pearson and category-level Hoeffding bounds correspond
   to different estimands. Do not merge them into one “universal guarantee.”
9. Matched-condition routing assumes condition metadata.
10. Source certification does not automatically prove target false-alarm
    control. The transfer assumption must remain visible.

### Visual hierarchy

The reader should understand these four messages within five seconds:

1. DINOv2 + PCA provides a fixed anomaly ranking.
2. Target-only LOIO reliability hits the `1/(k+1)` resolution floor.
3. SC3R uses disjoint source-category roles R/P/C to select a sub-floor
   threshold without target anomaly labels.
4. The certificate is source-conditional; target transfer is empirical unless
   an explicit assumption holds.

Before finalizing, perform a self-audit:

- verify every arrow against the scientific constraints;
- verify that no target test label enters fitting, routing, proposal, or
  certification;
- verify that the SC3R lane does not feed back into the ranking lane;
- verify exact spelling and mathematical notation;
- verify that every shape obeys the functional shape grammar and that no two
  unrelated functions share a misleading shape;
- remove any element that is merely decorative;
- ensure no text overlaps, no arrow crosses a label, and the figure remains
  legible at 178 mm width.

Return the final figure, followed by a plain-text list of all labels used and a
one-paragraph explanation of the visual encoding. Do not add experimental
numbers because final GPU results are pending.

---

## Prompt sửa lỗi sau lần sinh đầu

Nếu hình đẹp nhưng chữ hoặc mũi tên sai, dùng prompt tiếp theo:

> Preserve the current composition, spacing, palette, and dimensions. Perform a
> scientific correction pass only. Replace all text with the exact labels from
> the MASTER PROMPT, remove invented labels and numerical results, and verify
> every arrow. Enforce the functional shape grammar: stacked cards=data,
> hexagons=fitted representations, rounded rectangles=processing, tabbed
> cards=R/P/C partitions, diamonds=decisions, shield/document shapes=certificates,
> and pills=outputs. Do not render all nodes as rectangles. In particular:
> calibration must not modify the ranking lane;
> target anomaly labels are evaluation-only; R, P, and C are disjoint source
> categories; C evaluates but never proposes thresholds; τ is the largest
> candidate with UCB(τ) ≤ α, otherwise τ = 0; and source certification does not
> imply unconditional target control. Eliminate overlapping text and crossing
> arrows. Export again as editable SVG, vector PDF, and a 300 dpi PNG preview.
