# Run ablation_pca16_mvtec_carpet_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_carpet_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9978609291685494`
- `auroc`: `0.9931781701444623`
- `brier`: `0.1329633137572278`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16639903060391414`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0013575235493162759`
- `max_f1`: `0.9834254143646409`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.4743959142882192`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_carpet_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
