# Run ablation_alpha_1p0_mvtec_leather_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_leather_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9974950208917165`
- `auroc`: `0.9932065217391305`
- `brier`: `0.19007939724770112`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.029907108795258222`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001979264415680401`
- `max_f1`: `0.989247311827957`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5677068923467506`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_leather_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
