# Run ablation_alpha_0p25_mvtec_capsule_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_capsule_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9548862635529616`
- `auroc`: `0.8077383326685281`
- `brier`: `0.2066427223895008`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.26144496509523096`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0047269335693933745`
- `max_f1`: `0.9083333333333333`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6057802723583471`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_capsule_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
