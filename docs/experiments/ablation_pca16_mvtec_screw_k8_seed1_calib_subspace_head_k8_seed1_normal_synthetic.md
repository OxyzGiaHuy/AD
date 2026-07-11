# Run ablation_pca16_mvtec_screw_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_screw_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8356930587178623`
- `auroc`: `0.617339618774339`
- `brier`: `0.3200914024270903`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3055945839350897`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0025329943862743677`
- `max_f1`: `0.8530465949820788`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `1.2910674153169936`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_screw_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
