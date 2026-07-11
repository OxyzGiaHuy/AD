# Run ablation_pca128_mvtec_toothbrush_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_toothbrush_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9761373762894434`
- `auroc`: `0.9416666666666667`
- `brier`: `0.26015266502735557`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.271940929549081`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003962230292104539`
- `max_f1`: `0.9523809523809523`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.8916652565256684`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_toothbrush_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
