# Run subspacead_mvtec_capsule_k8_seed4_subspacead_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_capsule_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.9662191927438469`
- `auroc`: `0.8747506980454727`
- `brier`: `0.1716906393791248`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.171567543889537`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0013601589016616344`
- `max_f1`: `0.9422222222222222`
- `model_storage_mb`: `0.09521484375`
- `nll`: `0.9295946149085232`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/subspacead_mvtec_capsule_k8_seed4_subspacead_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
