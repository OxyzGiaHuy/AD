# Run ablation_alpha_0p5_mvtec_zipper_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_zipper_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9922611958115419`
- `auroc`: `0.9740021008403361`
- `brier`: `0.18916144651489505`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.35176375093839035`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0021206609139971387`
- `max_f1`: `0.9707112970711297`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5690675094802582`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_zipper_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
