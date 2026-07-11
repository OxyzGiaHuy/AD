# Run ablation_alpha_0p25_mvtec_hazelnut_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_hazelnut_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9692336848933175`
- `auroc`: `0.9378571428571428`
- `brier`: `0.22806462457888627`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08806184909560467`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.00530711884864352`
- `max_f1`: `0.9117647058823529`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6489070599756017`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_hazelnut_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
