# Run ablation_alpha_0p0_mvtec_zipper_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_zipper_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9852206924311633`
- `auroc`: `0.9495798319327731`
- `brier`: `0.2389659907231916`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.29029746027971737`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0018792327197379624`
- `max_f1`: `0.9516129032258065`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6710606082470165`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_zipper_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
