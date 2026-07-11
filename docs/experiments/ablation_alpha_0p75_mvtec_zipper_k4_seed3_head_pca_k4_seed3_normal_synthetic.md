# Run ablation_alpha_0p75_mvtec_zipper_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_zipper_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9852429619981711`
- `auroc`: `0.9477415966386554`
- `brier`: `0.15712767152656576`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24993815445742074`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002512420780512671`
- `max_f1`: `0.952`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.4967889682087121`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_zipper_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
