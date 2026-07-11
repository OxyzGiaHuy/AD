# Run ablation_alpha_0p75_mvtec_screw_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_screw_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8749799738195826`
- `auroc`: `0.7075220332035254`
- `brier`: `0.19119659871577985`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11686200946569444`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0027152936323545872`
- `max_f1`: `0.8561151079136691`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5709940688243299`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_screw_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
