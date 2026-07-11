# Run ablation_pca16_mvtec_tile_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_tile_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9929598745261927`
- `auroc`: `0.9834054834054834`
- `brier`: `0.09074731876211756`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12409789316579065`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0021004264967309106`
- `max_f1`: `0.9710982658959537`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.35163416181871615`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_tile_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
