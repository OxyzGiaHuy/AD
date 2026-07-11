# Run ablation_alpha_0p75_mvtec_wood_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_wood_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9886746860721042`
- `auroc`: `0.9614035087719298`
- `brier`: `0.18587345570012576`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.28854787651496594`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.00302003458425214`
- `max_f1`: `0.9491525423728814`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5601572061997049`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_wood_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
