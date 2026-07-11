# Run ablation_alpha_1p0_mvtec_leather_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_leather_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9997687326549491`
- `auroc`: `0.9993206521739131`
- `brier`: `0.16919588244403644`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1469744193938471`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002585401548252952`
- `max_f1`: `0.994535519125683`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5154305189480811`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_leather_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
