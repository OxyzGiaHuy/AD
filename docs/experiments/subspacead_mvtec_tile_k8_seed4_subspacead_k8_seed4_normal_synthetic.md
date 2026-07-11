# Run subspacead_mvtec_tile_k8_seed4_subspacead_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_tile_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.9903259770088614`
- `auroc`: `0.976911976911977`
- `brier`: `0.23905411654814795`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.25736420276837474`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001281228378160387`
- `max_f1`: `0.9704142011834319`
- `model_storage_mb`: `0.09521484375`
- `nll`: `0.8168881678230635`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/subspacead_mvtec_tile_k8_seed4_subspacead_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
