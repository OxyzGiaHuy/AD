# Run ablation_pca64_mvtec_pill_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_pill_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9895219896116245`
- `auroc`: `0.9500818330605565`
- `brier`: `0.07053604088522782`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.07415498308014838`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001954740694093847`
- `max_f1`: `0.9571428571428572`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.294708705855009`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_pill_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
