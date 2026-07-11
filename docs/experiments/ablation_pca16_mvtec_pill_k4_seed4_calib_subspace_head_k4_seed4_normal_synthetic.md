# Run ablation_pca16_mvtec_pill_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_pill_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9717089719854825`
- `auroc`: `0.8655210038188762`
- `brier`: `0.12046509873742807`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1230696607492642`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0025389894374651823`
- `max_f1`: `0.9395973154362416`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.48014923191512576`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_pill_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
