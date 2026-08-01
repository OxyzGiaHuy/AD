# GPU handoff: auditable capsule visuals for the pipeline figure

## Objective and non-negotiable scope

Produce the small set of real MVTec AD `capsule` assets needed to illustrate
the paper's pipeline without changing the method or introducing a qualitative
claim. The required run is the paper's frozen low-storage ranker at `k=4`,
`seed=0`: a frozen DINOv2 ViT-S/14 backbone at 518 px followed by a PCA64
subspace fitted only to the four target-normal support images.

The exported images are for **pipeline panels a and b**. Panels c (target-only
reliability), d (CRESS), and e (audit outputs) should remain vector schematics,
tables, or plots. They do not require another anomaly heatmap. In particular,
do not invent a CRESS heatmap: CRESS selects an operating threshold and does not
modify the raw anomaly map.

The GPU agent must not optimize the sample choice for the most attractive
heatmap. By default, the exporter fixes the defect family to `crack` and selects
the lower-median raw-score image within that family. This is a reproducible,
disclosed illustration rule, not a best-case localization selection. An exact
image may be supplied with `--test-image`, but that exception and its reason
must be recorded.

## Exact pipeline represented by the assets

### Panel a: frozen features and support-fitted subspace

1. Load the exact four normal support images selected by
   `few_shot_support(..., k=4, seed=0)`. Do not select four images manually.
2. Resize each support image and the query image to 518 by 518 only inside the
   model preprocessing; preserve the unmodified dataset files for display.
3. Pass both branches through frozen DINOv2 ViT-S/14. The resulting patch grid
   is 37 by 37 because (518/14=37), and each ViT-S/14 patch token has 384
   dimensions.
4. Flatten all support patch tokens and fit PCA64 on support-normal features
   only. Following the paper's column convention, let \(\mu\) be the mean and
   \(U\in\mathbb{R}^{384\times64}\) contain the retained PCA directions. Compute
   each query-patch residual as

   \[
   r(z)=\left\|(z-\mu)-UU^\top(z-\mu)\right\|_2.
   \]

   The implementation stores the same directions as rows in
   `PCASubspace.components`; its row-vector expression
   `(z-mu) - (z-mu) @ components.T @ components` is algebraically equivalent.

5. Reshape the 1,369 residuals into the actual 37 by 37 patch residual map. The
   raw float32 tensor is the scientific output; the colored PNG is a display
   rendering of that tensor.

The configuration still instantiates calibration-side machinery, but
`CalibSubspaceHead.score_images()` returns the PCA residuals directly. Do not
draw the synthetic MLP head as part of the frozen ranker in panels a or b.

### Panel b: fixed ranking and localization

The same 37 by 37 residual tensor branches in two directions:

- **Localization:** bilinearly upsample the patch grid to the original image
  resolution to obtain the pixel anomaly heatmap. The standalone heatmap or
  its overlay may be inserted in the figure. Ground truth is evaluation-only;
  it never enters DINOv2, PCA fitting, scoring, calibration, or CRESS.
- **Image ranking:** the clean accuracy/storage benchmark uses the maximum
  patch residual as the raw image score. The conformal reliability protocol
  separately uses the mean of the largest 1% of patch residuals as a smoothed
  maximum. The pipeline label must state this distinction and must not imply
  that the display normalization changes either score.

AUROC and AP evaluate image ranking. Pixel AUROC and AU-PRO evaluate the
upsampled residual maps. Reliability transformations act after the fixed score
and do not change the ranking or localization map.

### Panels c to e: why no further GPU imagery is needed

- **Panel c, target-only reliability:** LOIO refits PCA on `k-1` supports and
  produces p-values on the attainable grid. Draw the held-out folds,
  histogram, and p-value grid as vector graphics; an additional heatmap would
  not explain the resolution floor.
- **Panel d, CRESS:** use vector symbols for routed source-normal categories,
  the disjoint reference/proposal/certification roles, UCB, and the threshold
  gate. CRESS operates on scalar source-referenced evidence and returns a
  threshold; it does not generate a new spatial map.
- **Panel e, audit:** use compact vector icons or the paper's quantitative
  plots. Do not fabricate miniature performance curves with unverified values.

## Environment and data checks

Run every command from the repository root. Activate the intended Python
environment first; the commands below assume `python` points to that
environment.

```bash
cd /absolute/path/to/AD
python -m pip install -r requirements.txt
nvidia-smi
python -c "import torch; print(torch.__version__, torch.cuda.is_available(), torch.cuda.get_device_name(0))"
test -d data/mvtec/capsule/train/good
test -d data/mvtec/capsule/test/crack
test -d data/mvtec/capsule/ground_truth/crack
```

The repository's current `data/mvtec` may be a machine-specific symlink. If a
check fails, point `dataset.root` in a private copy of the capsule config to the
actual MVTec root, or repair the symlink after resolving the exact target. Do
not silently substitute VisA, MPDD, a resized copy, or a different capsule
split.

If the DINOv2 torch-hub repository and weights are not already cached, allow
the first run to fetch the official `facebookresearch/dinov2` implementation.
Record the repository commit before running:

```bash
git rev-parse HEAD
git status --short
```

Unrelated local paper edits must not be discarded or reset.

## Commands

### RUN-GPU: generate the exact ranker outputs

```bash
python -m src.run_experiment \
  --config configs/generated/mvtec_full/calib_subspace_head_mvtec_capsule_k4_seed0.yaml
```

Expected run directory:

```text
outputs/calib_subspace_head_mvtec_capsule_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic
```

The indispensable model output is:

```text
anomaly_maps/patch_scores.npy
```

It must contain one 37 by 37 PCA-residual grid per prediction row. Do not use a
saliency method, Grad-CAM, segmentation model, ground-truth mask, or a heatmap
generated by a different detector.

### EXPORT: deterministically export the pipeline assets

```bash
python scripts/export_pipeline_capsule_visuals.py \
  --config configs/generated/mvtec_full/calib_subspace_head_mvtec_capsule_k4_seed0.yaml \
  --run-dir outputs/calib_subspace_head_mvtec_capsule_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic \
  --out-dir outputs/pipeline_visuals/capsule_k4_seed0 \
  --defect-type crack
```

This command does not fit another detector. It reconstructs the exact support
set, selects the disclosed representative query, copies the dataset inputs and
mask, and derives all rendered maps from one saved residual tensor. It writes
`manifest.json` with source paths, SHA-256 checksums, the prediction index, raw
score, selection rule, grid shape, and display normalization.

### VERIFY: mandatory acceptance checks

```bash
python -c "import json; p='outputs/pipeline_visuals/capsule_k4_seed0/manifest.json'; m=json.load(open(p)); assert m['patch_grid']==[37,37]; assert m['k']==4 and m['seed']==0; assert len(m['assets'])==11; print(m['selection_rule'], m['selected_defect_type'], m['selected_raw_score'])"
python -c "import numpy as np; p='outputs/pipeline_visuals/capsule_k4_seed0/patch_residual_raw_37x37.npy'; x=np.load(p); assert x.shape==(37,37) and np.isfinite(x).all() and (x>=0).all(); print(x.min(), x.max(), x.mean())"
```

Also inspect the montage and query against their recorded source files. Reject
the export if any support image is anomalous, if the query mask is missing, if
the main heatmap is actually the mask, or if the anomaly map has been manually
painted or retouched.

## Visual asset list

Paths below are relative to this document. Links under `outputs/` become valid
after RUN-GPU and EXPORT complete.

| ID | Pipeline position | Asset and scientific role | GPU-dependent? | Expected path | Command |
|---|---|---|---:|---|---|
| V01 | Panel a, `k normal supports` | A four-card montage of the exact `k=4`, seed-0 normal support set. Use this in the final figure. | No; dataset copy | [support montage](../outputs/pipeline_visuals/capsule_k4_seed0/support_montage_k4.png) | EXPORT |
| V02 | Panel a, support audit | First exact normal support, retained separately for provenance. | No; dataset copy | [support 01](../outputs/pipeline_visuals/capsule_k4_seed0/support_01.png) | EXPORT |
| V03 | Panel a, support audit | Second exact normal support. | No; dataset copy | [support 02](../outputs/pipeline_visuals/capsule_k4_seed0/support_02.png) | EXPORT |
| V04 | Panel a, support audit | Third exact normal support. | No; dataset copy | [support 03](../outputs/pipeline_visuals/capsule_k4_seed0/support_03.png) | EXPORT |
| V05 | Panel a, support audit | Fourth exact normal support. | No; dataset copy | [support 04](../outputs/pipeline_visuals/capsule_k4_seed0/support_04.png) | EXPORT |
| V06 | Panel a, `test image x` | Original anomalous capsule query. This is the image entering the frozen backbone; no mask or heatmap may be visible on it. | No; dataset copy selected after RUN-GPU by a disclosed rule | [test capsule](../outputs/pipeline_visuals/capsule_k4_seed0/test_capsule_anomaly.png) | RUN-GPU, then EXPORT |
| V07 | Panel a after residual computation; Panel b at branch input | Nearest-neighbor rendering of the genuine 37 by 37 PCA patch residual map. Reuse the same file in both locations rather than regenerating it. | **Yes**; depends on DINOv2 and fitted PCA64 | [coarse residual map](../outputs/pipeline_visuals/capsule_k4_seed0/patch_residual_map_nearest.png) | RUN-GPU, then EXPORT |
| V08 | Scientific provenance, not normally placed in the figure | Raw float32 37 by 37 residual tensor underlying V07 to V10. This is the auditable source of truth. | **Yes** | [raw residual tensor](../outputs/pipeline_visuals/capsule_k4_seed0/patch_residual_raw_37x37.npy) | RUN-GPU, then EXPORT |
| V09 | Panel b, `spatial upsampling / heatmap` | Bilinearly upsampled pixel anomaly heatmap derived from V08. Prefer this if the layout already shows the query image elsewhere. | **Yes**; derived from the same GPU output | [pixel heatmap](../outputs/pipeline_visuals/capsule_k4_seed0/pixel_anomaly_heatmap_bilinear.png) | RUN-GPU, then EXPORT |
| V10 | Panel b, optional final localization thumbnail | Overlay of V09 on V06 using a fixed 55/45 image-to-heat blend. Prefer this instead of V09 only when readers need spatial correspondence; do not place both if the panel becomes crowded. | **Yes**; derived from the same GPU output | [heatmap overlay](../outputs/pipeline_visuals/capsule_k4_seed0/test_heatmap_overlay.png) | RUN-GPU, then EXPORT |
| V11 | Panel b, evaluation endpoint only | Official MVTec ground-truth mask for the selected query. Optional in the pipeline; label it `GT (evaluation only)` and keep it after the localization output. Never connect it to fitting or scoring. | No; dataset annotation | [ground-truth mask](../outputs/pipeline_visuals/capsule_k4_seed0/gt_mask_evaluation_only.png) | EXPORT |
| V12 | Audit/handoff, not placed in the figure | Provenance manifest for every image, selection rule, raw score, display normalization, and SHA-256 checksums. | No additional GPU work | [manifest](../outputs/pipeline_visuals/capsule_k4_seed0/manifest.json) | EXPORT |

The supporting implementation and frozen configuration are:

- [capsule visual exporter](../scripts/export_pipeline_capsule_visuals.py)
- [capsule k=4 seed-0 config](../configs/generated/mvtec_full/calib_subspace_head_mvtec_capsule_k4_seed0.yaml)
- [experiment runner](../src/run_experiment.py)
- [PCA residual implementation](../src/models/pca.py)

## Placement guidance for the final illustrator

Use V01 as the stacked support input and V06 as the unaltered query input.
Place V07 immediately after residual computation. In panel b, reuse V07 at the
start of the split, then use V09 for the localization endpoint. V10 is an
alternative to V09, not an additional algorithmic stage. V11 may appear only
in a small evaluation-only comparison; omit it if the figure is crowded.

Keep all surrounding components as crisp 2D vector graphics. Rasterize only
the dataset thumbnails and heatmaps. Do not ask an image model to redraw,
beautify, sharpen, hallucinate, or relight these assets. Cropping must preserve
the capsule and defect; aspect-ratio-preserving scaling is preferred.

Use one fixed sequential color map and include one compact `low residual` to
`high residual` color bar. The exporter clips each selected map at its own 99th
percentile for display only. That fact need not fill the figure, but it must be
stated in the caption or supplementary generation notes if the qualitative
example is discussed. Never compare absolute residual magnitudes across images
from independently normalized PNGs; use the raw `.npy` values for quantitative
comparison.

## Required return from the GPU agent

Return the complete `outputs/pipeline_visuals/capsule_k4_seed0/` directory plus:

1. the GPU model name, PyTorch/CUDA versions, repository commit, and whether
   DINOv2 came from a local torch-hub cache or a download;
2. the full console logs for RUN-GPU, EXPORT, and VERIFY;
3. `manifest.json` and the exact config used;
4. a statement that no image was manually edited and no ground-truth mask was
   used to fit, select, or alter the anomaly map;
5. disclosure of any deviation, including a different capsule defect type or
   an explicit `--test-image` choice.

Do not report the visual as evidence of average localization quality. It is a
traceable method illustration; the paper's aggregate pixel metrics, not one
heatmap, support quantitative localization claims.
