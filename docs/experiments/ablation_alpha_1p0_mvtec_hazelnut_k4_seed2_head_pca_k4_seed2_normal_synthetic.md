# Run ablation_alpha_1p0_mvtec_hazelnut_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_hazelnut_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9507769717649178`
- `auroc`: `0.8967857142857143`
- `brier`: `0.24117855595370977`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.10238325216553433`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0017631339925256641`
- `max_f1`: `0.8776978417266187`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.678969843447757`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_hazelnut_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
