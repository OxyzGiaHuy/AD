# Run ablation_alpha_1p0_mvtec_zipper_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_zipper_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9891409947966565`
- `auroc`: `0.9590336134453782`
- `brier`: `0.14496195552608465`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.21492344812052144`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0018906070178510337`
- `max_f1`: `0.9482071713147411`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.4666327468786759`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_zipper_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
