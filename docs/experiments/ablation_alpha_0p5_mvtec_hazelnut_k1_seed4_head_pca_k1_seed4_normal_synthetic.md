# Run ablation_alpha_0p5_mvtec_hazelnut_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_hazelnut_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9576428009251474`
- `auroc`: `0.9132142857142858`
- `brier`: `0.22910604440889454`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22358862161636356`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0030858960002660752`
- `max_f1`: `0.9264705882352942`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6506946792879634`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_hazelnut_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
