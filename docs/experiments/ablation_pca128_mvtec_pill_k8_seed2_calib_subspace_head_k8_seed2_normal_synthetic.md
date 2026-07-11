# Run ablation_pca128_mvtec_pill_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_pill_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9853926628031457`
- `auroc`: `0.9331696672122204`
- `brier`: `0.06385301819720807`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.07103872288598449`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0020715975632032233`
- `max_f1`: `0.958904109589041`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.2799953213296919`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_pill_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
