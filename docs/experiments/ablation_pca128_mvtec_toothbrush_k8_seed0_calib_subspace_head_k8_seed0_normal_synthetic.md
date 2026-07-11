# Run ablation_pca128_mvtec_toothbrush_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_toothbrush_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9813681455202126`
- `auroc`: `0.9527777777777777`
- `brier`: `0.11052218982307957`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.13985057742822743`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001755219130288987`
- `max_f1`: `0.9523809523809523`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.8906017854564264`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_toothbrush_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
