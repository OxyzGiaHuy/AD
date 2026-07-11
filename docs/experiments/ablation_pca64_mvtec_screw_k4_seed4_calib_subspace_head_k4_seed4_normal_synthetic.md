# Run ablation_pca64_mvtec_screw_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_screw_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7953018888564964`
- `auroc`: `0.6312769010043041`
- `brier`: `0.22614658172834937`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22469099864829334`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.001646848232485354`
- `max_f1`: `0.8656716417910447`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.2393000961175644`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_screw_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
