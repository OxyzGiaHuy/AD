# Run ablation_alpha_0p75_mvtec_capsule_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_capsule_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9670240993645752`
- `auroc`: `0.8735540486637415`
- `brier`: `0.15038604982545387`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.19783573078386713`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0025665623446305594`
- `max_f1`: `0.9316239316239316`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.48381103701449`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_capsule_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
