# Run ablation_pca128_mvtec_leather_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_leather_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.999027781230873`
- `auroc`: `0.9972826086956522`
- `brier`: `0.23284018097617606`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24365472817613226`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0017972710962978102`
- `max_f1`: `0.9945945945945946`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.3795683343437561`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_leather_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
