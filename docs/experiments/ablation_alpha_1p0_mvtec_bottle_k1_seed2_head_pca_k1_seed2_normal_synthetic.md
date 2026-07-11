# Run ablation_alpha_1p0_mvtec_bottle_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_bottle_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9767951634138059`
- `auroc`: `0.9007936507936508`
- `brier`: `0.18405063761320256`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.03435043469969046`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.003128312393484345`
- `max_f1`: `0.907563025210084`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5551538678126583`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_bottle_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
