# Run ablation_alpha_0p75_mvtec_screw_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_screw_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8435431774884273`
- `auroc`: `0.6263578602172576`
- `brier`: `0.19541062634458062`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.07062233127653605`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001761319732759148`
- `max_f1`: `0.8530465949820788`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5805558254359755`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_screw_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
