# Run ablation_pca64_mvtec_zipper_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_zipper_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9840572265198935`
- `auroc`: `0.9422268907563025`
- `brier`: `0.2049649333960692`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2081869335364033`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0024086505988773132`
- `max_f1`: `0.9444444444444444`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.6913728311686818`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_zipper_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
