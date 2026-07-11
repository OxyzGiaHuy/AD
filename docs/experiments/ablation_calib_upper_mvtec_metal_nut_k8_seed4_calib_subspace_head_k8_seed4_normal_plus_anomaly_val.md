# Run ablation_calib_upper_mvtec_metal_nut_k8_seed4_calib_subspace_head_k8_seed4_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_metal_nut_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9816521575421836`
- `auroc`: `0.9404761904761905`
- `brier`: `0.08877057029510094`
- `calibration_anomaly_val_count`: `9`
- `ece`: `0.09937866624304147`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0019919820797612083`
- `max_f1`: `0.9540229885057471`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.33439258641016484`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_metal_nut_k8_seed4_calib_subspace_head_k8_seed4_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
