# Run ablation_pca16_mvtec_hazelnut_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_hazelnut_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8475444618176401`
- `auroc`: `0.7907142857142857`
- `brier`: `0.3496498158138152`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3506820657036521`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001372154988348484`
- `max_f1`: `0.8414634146341463`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `1.5455056033028665`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_hazelnut_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
