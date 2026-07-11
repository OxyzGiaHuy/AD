# Run smoke_visa_candle_identity_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/experiments/smoke_visa_candle_identity.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.9917866805146306`
- `auroc`: `0.9895`
- `brier`: `0.2324066138215999`
- `ece`: `0.43130445659160616`
- `k_shot`: `1`
- `latency_sec_per_image`: `4.475638270378113e-06`
- `max_f1`: `0.9560975609756097`
- `nll`: `0.6579302101001623`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`

## Notes

- Predictions written to outputs/smoke_visa_candle_identity_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
