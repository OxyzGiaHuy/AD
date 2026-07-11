# Run ablation_alpha_1p0_mvtec_transistor_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_transistor_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.6610695797533565`
- `auroc`: `0.7052083333333333`
- `brier`: `0.34508184888595833`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.324551562666893`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.003487080130726099`
- `max_f1`: `0.6495726495726496`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.9018727642646402`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_transistor_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
