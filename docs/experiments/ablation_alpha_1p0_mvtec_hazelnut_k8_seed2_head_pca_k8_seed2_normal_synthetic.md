# Run ablation_alpha_1p0_mvtec_hazelnut_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_hazelnut_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9694259025512029`
- `auroc`: `0.9417857142857143`
- `brier`: `0.23865354377503423`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.10506114363670356`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0025786486200310966`
- `max_f1`: `0.9241379310344827`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6726727220334223`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_hazelnut_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
