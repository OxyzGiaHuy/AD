# Run ablation_alpha_0p5_mvtec_cable_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_cable_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9604416471990187`
- `auroc`: `0.920352323838081`
- `brier`: `0.22708501554165034`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.04530853986740113`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0020748532066742578`
- `max_f1`: `0.8928571428571429`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6458399588427705`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_cable_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
