# Run ablation_pca16_mvtec_hazelnut_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_hazelnut_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9294228496314446`
- `auroc`: `0.875`
- `brier`: `0.22942719844410397`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2531370343132453`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002520152215253223`
- `max_f1`: `0.85`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.8779098453097733`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_hazelnut_k8_seed1_calib_subspace_head_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
