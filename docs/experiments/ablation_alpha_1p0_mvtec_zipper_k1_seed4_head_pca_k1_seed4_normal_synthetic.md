# Run ablation_alpha_1p0_mvtec_zipper_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_zipper_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9901086438420136`
- `auroc`: `0.9637605042016807`
- `brier`: `0.16276008869165237`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12348111220542962`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0024275299753771713`
- `max_f1`: `0.9482071713147411`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.508367626646584`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_zipper_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
