#!/bin/bash
# Detached VisA SC3R chain: export -> residuals -> evaluate -> CI -> cross-dataset.
set -e
cd /home/crl/AD
PY=/home/crl/miniconda3/envs/ad/bin/python
CLASSES="candle capsules cashew chewinggum fryum macaroni1 macaroni2 pcb1 pcb2 pcb3 pcb4 pipe_fryum"
PYTHONUNBUFFERED=1 $PY -u scripts/export_sc3r_views.py \
  --dataset visa --classes $CLASSES --k-shots 4 --seeds 0 1 2 \
  --corruptions clean gaussian_noise blur brightness_contrast jpeg \
  --max-images 120 \
  --out outputs/paper_tables/sc3r_views_visa_full12_stratified.csv \
  --support-out outputs/paper_tables/sc3r_support_visa_full12_stratified.csv \
  --resume
PYTHONUNBUFFERED=1 $PY -u scripts/export_support_loio_residuals.py \
  --dataset visa --classes $CLASSES --k-shots 4 --seeds 0 1 2 \
  --out outputs/paper_tables/sc3r_support_loio_residuals_visa_full12.csv --resume
$PY -u scripts/evaluate_source_validated_threshold.py \
  --inputs outputs/paper_tables/sc3r_views_visa_full12_stratified.csv \
  --support-stats outputs/paper_tables/sc3r_support_visa_full12_stratified.csv \
  --support-residuals outputs/paper_tables/sc3r_support_loio_residuals_visa_full12.csv \
  --source-modes matched_condition clean_source --alphas 0.05 0.10 0.20 \
  --run-tag sc3r_visa_full12_stratified
$PY scripts/hierarchical_bootstrap_comparison.py \
  --input outputs/paper_tables/source_validated_threshold_sc3r_visa_full12_stratified_detailed.csv \
  --baseline target_only --candidates source_validated_pool \
  --out outputs/paper_tables/sc3r_visa_full12_stratified_hierarchical_ci.csv
$PY -u scripts/evaluate_source_validated_threshold.py \
  --inputs outputs/paper_tables/sc3r_views_visa_full12_stratified.csv outputs/paper_tables/sc3r_views_mvtec_full15_stratified.csv \
  --support-stats outputs/paper_tables/sc3r_support_visa_full12_stratified.csv outputs/paper_tables/sc3r_support_mvtec_full15_stratified.csv \
  --support-residuals outputs/paper_tables/sc3r_support_loio_residuals_visa_full12.csv \
  --source-modes matched_condition clean_source \
  --source-dataset mvtec --target-dataset visa --alphas 0.05 0.10 0.20 \
  --run-tag sc3r_cross_mvtec_to_visa
touch /home/crl/AD/logs/SC3R_VISA_CHAIN_DONE
