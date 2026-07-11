# Run ablation_pca64_mvtec_pill_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_pill_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9781882409021253`
- `auroc`: `0.8936170212765957`
- `brier`: `0.15554070820652477`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15560142936820753`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0018844181102906873`
- `max_f1`: `0.9379310344827586`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.5496517884384995`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_pill_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
