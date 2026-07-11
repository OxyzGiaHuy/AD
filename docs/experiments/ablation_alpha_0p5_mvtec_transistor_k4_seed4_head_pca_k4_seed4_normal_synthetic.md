# Run ablation_alpha_0p5_mvtec_transistor_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_transistor_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9255190758993852`
- `auroc`: `0.9383333333333334`
- `brier`: `0.27324100124521555`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2102639144659043`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.004485507216304541`
- `max_f1`: `0.8292682926829268`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7399955828498332`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_transistor_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
