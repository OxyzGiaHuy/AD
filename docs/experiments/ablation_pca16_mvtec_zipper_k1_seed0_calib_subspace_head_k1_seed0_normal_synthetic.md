# Run ablation_pca16_mvtec_zipper_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_zipper_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9686331220536023`
- `auroc`: `0.8941701680672269`
- `brier`: `0.10208180831939133`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.10506651938788725`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0015709157786424587`
- `max_f1`: `0.936`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `1.2735698133682467`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_zipper_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
