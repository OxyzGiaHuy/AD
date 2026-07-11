# Run ablation_pca16_mvtec_bottle_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_bottle_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9487384804154311`
- `auroc`: `0.8976190476190476`
- `brier`: `0.20845527825509122`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.18539764723145824`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0025857893233916848`
- `max_f1`: `0.9242424242424242`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.6883447036840423`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_bottle_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
