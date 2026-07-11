# Run ablation_alpha_0p5_mvtec_capsule_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_capsule_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.968643362653706`
- `auroc`: `0.8767451136816913`
- `brier`: `0.1756515139556858`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23882929664669617`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.004895102726577809`
- `max_f1`: `0.9316239316239316`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5410806489493265`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_capsule_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
