# Run ablation_alpha_0p75_mvtec_zipper_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_zipper_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9965642573062794`
- `auroc`: `0.9873949579831933`
- `brier`: `0.15141085786323488`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.18802310891498797`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0020129620436801026`
- `max_f1`: `0.9747899159663865`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.4813606591151574`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_zipper_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
