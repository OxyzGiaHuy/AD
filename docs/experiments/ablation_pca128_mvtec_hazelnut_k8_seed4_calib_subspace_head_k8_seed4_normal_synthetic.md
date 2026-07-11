# Run ablation_pca128_mvtec_hazelnut_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_hazelnut_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9944553701483398`
- `auroc`: `0.9917857142857143`
- `brier`: `0.2952586684818278`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3190180897712708`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001980295167727904`
- `max_f1`: `0.9929078014184397`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.4731497609037798`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_hazelnut_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
