# Run ablation_alpha_1p0_mvtec_zipper_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_zipper_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9785288399680371`
- `auroc`: `0.9248949579831933`
- `brier`: `0.14906305603918574`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14796529424111576`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0030185749125204338`
- `max_f1`: `0.9402390438247012`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.47267037106299364`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_zipper_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
