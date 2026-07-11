# Run ablation_pca16_mvtec_capsule_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_capsule_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9140385964985569`
- `auroc`: `0.7068209014758676`
- `brier`: `0.13469148267513878`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12486962446322043`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0021083673716268754`
- `max_f1`: `0.9145299145299145`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.517183114845429`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_capsule_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
