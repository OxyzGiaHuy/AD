# Run ablation_pca16_mvtec_pill_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_pill_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.978303751409529`
- `auroc`: `0.894708128750682`
- `brier`: `0.12535501239982333`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12829689371879188`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0014318198545607264`
- `max_f1`: `0.9399293286219081`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `1.3180268641379769`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_pill_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
