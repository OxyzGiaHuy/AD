# Run ablation_alpha_0p75_mvtec_toothbrush_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_toothbrush_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9800250738668588`
- `auroc`: `0.9472222222222222`
- `brier`: `0.2029404853048812`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.06976702667417975`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.005719743048151334`
- `max_f1`: `0.9333333333333333`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5957770104392844`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_toothbrush_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
