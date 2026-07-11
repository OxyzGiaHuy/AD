# Run ablation_alpha_0p25_mvtec_zipper_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_zipper_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9826662136213764`
- `auroc`: `0.9372373949579832`
- `brier`: `0.21544811076732825`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.33439653559236343`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.003265588501135245`
- `max_f1`: `0.9392712550607287`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6236981099498174`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_zipper_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
