# Run ablation_pca128_mvtec_zipper_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_zipper_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9965361028379397`
- `auroc`: `0.9879201680672269`
- `brier`: `0.03632783480386345`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.04705065019453398`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0018509843244852609`
- `max_f1`: `0.9790794979079498`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.13556930400966372`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_zipper_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
