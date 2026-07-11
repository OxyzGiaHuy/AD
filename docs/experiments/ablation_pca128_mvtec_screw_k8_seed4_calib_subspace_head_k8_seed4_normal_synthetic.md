# Run ablation_pca128_mvtec_screw_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_screw_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9140659149967704`
- `auroc`: `0.811026849764296`
- `brier`: `0.15418554836195436`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.13437159422901454`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0021531519247218966`
- `max_f1`: `0.8871595330739299`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.6565471732381031`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_screw_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
