# Run ablation_alpha_0p25_mvtec_screw_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_screw_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.7857014573513839`
- `auroc`: `0.6099610575937692`
- `brier`: `0.22376815764737684`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1917946266010404`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003417249373160303`
- `max_f1`: `0.8708487084870848`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6404360628454491`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_screw_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
