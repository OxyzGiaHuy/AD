# Run ablation_alpha_0p5_mvtec_leather_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_leather_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9983155233823904`
- `auroc`: `0.9952445652173914`
- `brier`: `0.20187732763362395`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.28200115888349464`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0017896893794738477`
- `max_f1`: `0.989247311827957`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5950174699473665`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_leather_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
