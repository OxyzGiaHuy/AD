# Run ablation_alpha_0p5_mvtec_cable_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_cable_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9523527289785577`
- `auroc`: `0.9109820089955023`
- `brier`: `0.22890397022775777`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.018817177613576264`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002502017021179199`
- `max_f1`: `0.8837209302325582`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6495085472207999`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_cable_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
