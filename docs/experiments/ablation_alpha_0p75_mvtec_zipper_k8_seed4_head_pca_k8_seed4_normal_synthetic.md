# Run ablation_alpha_0p75_mvtec_zipper_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_zipper_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.996638712582394`
- `auroc`: `0.989233193277311`
- `brier`: `0.15590266265116504`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.33868568898826257`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0030956344296600644`
- `max_f1`: `0.9916666666666667`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.4953621996999357`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_zipper_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
