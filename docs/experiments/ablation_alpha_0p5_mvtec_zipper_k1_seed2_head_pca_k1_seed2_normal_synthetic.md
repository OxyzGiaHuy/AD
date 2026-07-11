# Run ablation_alpha_0p5_mvtec_zipper_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_zipper_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9825640695051556`
- `auroc`: `0.9369747899159664`
- `brier`: `0.1912593177873596`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2702083015284001`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.003459483878501993`
- `max_f1`: `0.9435483870967742`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5734142290011557`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_zipper_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
