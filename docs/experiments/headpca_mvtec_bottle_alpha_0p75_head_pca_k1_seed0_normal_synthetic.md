# Run headpca_mvtec_bottle_alpha_0p75_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/experiments/headpca_mvtec_bottle_alpha_0p75.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9840927420939994`
- `auroc`: `0.9428571428571428`
- `brier`: `0.17862079232975547`
- `ece`: `0.19693679263792838`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001649167007171964`
- `max_f1`: `0.9508196721311475`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5448121958435518`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/headpca_mvtec_bottle_alpha_0p75_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
