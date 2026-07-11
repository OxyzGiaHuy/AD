# Run ablation_alpha_0p75_mvtec_leather_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_leather_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9989343563512362`
- `auroc`: `0.9966032608695652`
- `brier`: `0.17525728194607423`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2342639868297885`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0030985698103904724`
- `max_f1`: `0.994535519125683`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5344573390715155`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_leather_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
