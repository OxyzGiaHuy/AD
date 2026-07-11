# Run ablation_alpha_0p75_mvtec_bottle_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_bottle_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9925923132028808`
- `auroc`: `0.9746031746031746`
- `brier`: `0.17146561766935922`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16428246411932518`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003418310062892466`
- `max_f1`: `0.9516129032258065`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5269431949362999`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_bottle_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
