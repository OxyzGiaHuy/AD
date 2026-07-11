# Run ablation_alpha_0p75_mvtec_wood_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_wood_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9976016584329718`
- `auroc`: `0.9921052631578947`
- `brier`: `0.18466970553326797`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3732457070411006`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0035915851262928564`
- `max_f1`: `0.9752066115702479`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5575477911592609`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_wood_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
