# Run subspacead_mvtec_zipper_k8_seed3_subspacead_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_zipper_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.986160566897843`
- `auroc`: `0.9495798319327731`
- `brier`: `0.5036981805755838`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.5834516350007215`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0012779423954668424`
- `max_f1`: `0.9444444444444444`
- `model_storage_mb`: `0.09521484375`
- `nll`: `1.2876374433673627`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/subspacead_mvtec_zipper_k8_seed3_subspacead_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
