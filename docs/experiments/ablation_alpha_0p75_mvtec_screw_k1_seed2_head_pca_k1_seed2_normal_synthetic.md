# Run ablation_alpha_0p75_mvtec_screw_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_screw_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.7711502724124646`
- `auroc`: `0.5673293707726993`
- `brier`: `0.19616416841654144`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.07488392554223534`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002468047372531146`
- `max_f1`: `0.8530465949820788`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5822555365140609`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_screw_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
