# Run ablation_pca128_mvtec_pill_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_pill_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.987101150365157`
- `auroc`: `0.9405346426623022`
- `brier`: `0.10083749499422953`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11338085774889962`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0015387484681106613`
- `max_f1`: `0.9574468085106383`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.4289506763173901`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_pill_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
