# Run ablation_alpha_1p0_mvtec_bottle_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_bottle_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9944086045389875`
- `auroc`: `0.9817460317460317`
- `brier`: `0.1703693815223826`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15048150628446094`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002652996028941798`
- `max_f1`: `0.9682539682539683`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5239028665676133`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_bottle_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
