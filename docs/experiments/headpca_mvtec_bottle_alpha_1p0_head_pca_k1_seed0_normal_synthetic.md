# Run headpca_mvtec_bottle_alpha_1p0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/experiments/headpca_mvtec_bottle_alpha_1p0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9784067678190168`
- `auroc`: `0.9253968253968254`
- `brier`: `0.1715165078907452`
- `ece`: `0.11227425753352155`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0016435714640531194`
- `max_f1`: `0.9180327868852459`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5270166957235937`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/headpca_mvtec_bottle_alpha_1p0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
