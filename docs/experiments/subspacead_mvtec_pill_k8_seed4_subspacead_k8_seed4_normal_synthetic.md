# Run subspacead_mvtec_pill_k8_seed4_subspacead_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_pill_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.9870421261278943`
- `auroc`: `0.9429896344789962`
- `brier`: `0.15335414767290162`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15401473623549866`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0013305682822794258`
- `max_f1`: `0.9605734767025089`
- `model_storage_mb`: `0.09521484375`
- `nll`: `0.8373933431054116`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/subspacead_mvtec_pill_k8_seed4_subspacead_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
