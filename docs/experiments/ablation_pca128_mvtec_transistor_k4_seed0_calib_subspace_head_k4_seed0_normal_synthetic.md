# Run ablation_pca128_mvtec_transistor_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_transistor_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8392013858781702`
- `auroc`: `0.8583333333333333`
- `brier`: `0.4394680293085318`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.482771048694849`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0017343739233911038`
- `max_f1`: `0.7586206896551724`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.8161340577409097`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_transistor_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
