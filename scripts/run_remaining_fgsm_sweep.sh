#!/usr/bin/env bash
set -euo pipefail
cd /home/crl/AD
PY=/home/crl/miniconda3/envs/ad/bin/python
RUN_LIST=configs/generated/mvtec_full/run_list.txt
CURRENT_PID=${1:-}
if [[ -n "$CURRENT_PID" ]]; then
  while kill -0 "$CURRENT_PID" 2>/dev/null; do
    echo "waiting_for_existing_fgsm_pid=$CURRENT_PID $(date -Is)"
    sleep 60
  done
fi
echo "resume_eps2 $(date -Is)"
$PY -u scripts/evaluate_fgsm_batch.py --run-list "$RUN_LIST" --variant calib_subspace_head --epsilon 2/255
echo "run_eps4 $(date -Is)"
$PY -u scripts/evaluate_fgsm_batch.py --run-list "$RUN_LIST" --variant calib_subspace_head --epsilon 4/255
echo "aggregate_sweep $(date -Is)"
$PY scripts/aggregate_fgsm_sweep.py --out-dir outputs/paper_tables
echo "done $(date -Is)"
