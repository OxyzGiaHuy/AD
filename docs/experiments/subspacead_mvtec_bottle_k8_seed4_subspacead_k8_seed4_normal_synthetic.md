# Run subspacead_mvtec_bottle_k8_seed4_subspacead_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_bottle_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.9967916942976308`
- `auroc`: `0.9904761904761905`
- `brier`: `0.2232137756705956`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23003763534936555`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001306960022593119`
- `max_f1`: `0.984375`
- `model_storage_mb`: `0.09521484375`
- `nll`: `0.844053976527837`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/subspacead_mvtec_bottle_k8_seed4_subspacead_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
