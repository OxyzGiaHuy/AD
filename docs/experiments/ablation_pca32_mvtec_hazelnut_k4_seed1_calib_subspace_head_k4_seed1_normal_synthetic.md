# Run ablation_pca32_mvtec_hazelnut_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_hazelnut_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9851759184747465`
- `auroc`: `0.9746428571428571`
- `brier`: `0.2730551301942063`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.30381910015236246`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003115851330486211`
- `max_f1`: `0.9565217391304348`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.2960859047856543`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_hazelnut_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
