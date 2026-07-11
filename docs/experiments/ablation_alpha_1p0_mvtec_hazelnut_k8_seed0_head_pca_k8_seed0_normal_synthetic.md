# Run ablation_alpha_1p0_mvtec_hazelnut_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_hazelnut_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9695859393692339`
- `auroc`: `0.9421428571428572`
- `brier`: `0.24222817336127353`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11998227563771341`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002695517089556564`
- `max_f1`: `0.9115646258503401`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6817976174810948`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_hazelnut_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
