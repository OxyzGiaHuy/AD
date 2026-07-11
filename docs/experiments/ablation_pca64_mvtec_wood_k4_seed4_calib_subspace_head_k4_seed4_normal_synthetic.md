# Run ablation_pca64_mvtec_wood_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_wood_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9891699145266194`
- `auroc`: `0.9675438596491228`
- `brier`: `0.18664223743034877`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20583049255081362`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0020858201469424404`
- `max_f1`: `0.9586776859504132`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.6430740210490815`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_wood_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
