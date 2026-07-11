# Run ablation_pca16_mvtec_pill_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_pill_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9672146307910037`
- `auroc`: `0.8477905073649754`
- `brier`: `0.11373860421852539`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11483764172180327`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0021222639427392067`
- `max_f1`: `0.9257950530035336`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.5825801264389494`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_pill_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
