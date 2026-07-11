# Run subspacead_mvtec_capsule_k8_seed1_subspacead_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_capsule_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.9837893389543083`
- `auroc`: `0.9242122058236937`
- `brier`: `0.17361960670984192`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.17365317136952363`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0014015079447717378`
- `max_f1`: `0.9427312775330396`
- `model_storage_mb`: `0.09521484375`
- `nll`: `1.1686074082267939`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/subspacead_mvtec_capsule_k8_seed1_subspacead_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
