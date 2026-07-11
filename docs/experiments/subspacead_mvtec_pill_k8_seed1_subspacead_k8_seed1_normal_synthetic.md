# Run subspacead_mvtec_pill_k8_seed1_subspacead_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/subspacead_mvtec_pill_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `subspacead`

## Metrics

- `ap`: `0.9886647404758329`
- `auroc`: `0.9489907255864702`
- `brier`: `0.1507269915920089`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1517770807900115`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0012733691935232299`
- `max_f1`: `0.9616724738675958`
- `model_storage_mb`: `0.09521484375`
- `nll`: `0.7015925482044851`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/subspacead_mvtec_pill_k8_seed1_subspacead_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
