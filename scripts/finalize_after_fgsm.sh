#!/usr/bin/env bash
set -euo pipefail
cd /home/crl/AD
PY=/home/crl/miniconda3/envs/ad/bin/python
LOG_DIR=outputs/logs
STATUS=$LOG_DIR/finalize_after_fgsm.status
LOCK=$LOG_DIR/finalize_after_fgsm.lock
mkdir -p "$LOG_DIR"
exec 9>"$LOCK"
if ! flock -n 9; then
  echo "another finalize job is already running" | tee "$STATUS"
  exit 2
fi
step(){ echo "[$(date -Is)] $*" | tee -a "$STATUS"; }
count(){ $PY - <<'PYCOUNT'
from pathlib import Path
rb=Path('outputs/robustness')
for eps in ['2_255','4_255','8_255']:
    print(f"fgsm_eps{eps}=", len(list(rb.glob(f'calib_subspace_head_mvtec_*_fgsm_eps{eps}/metrics.json'))))
PYCOUNT
}
PID=${1:-}
: > "$STATUS"
step "finalizer started"
if [[ -n "$PID" ]]; then
  while kill -0 "$PID" 2>/dev/null; do
    step "waiting for FGSM eps4 pid=$PID"
    count | tee -a "$STATUS"
    sleep 60
  done
fi
step "resume/check eps4"
$PY -u scripts/evaluate_fgsm_batch.py --run-list configs/generated/mvtec_full/run_list.txt --variant calib_subspace_head --epsilon 4/255
count | tee -a "$STATUS"
step "aggregate fgsm sweep"
$PY scripts/aggregate_fgsm_sweep.py --out-dir outputs/paper_tables
step "aggregate robustness all"
$PY scripts/aggregate_robustness_all.py --outputs-dir outputs --robustness-dir outputs/robustness --out-dir outputs/paper_tables --dataset mvtec || true
$PY scripts/aggregate_robustness_all.py --outputs-dir outputs --robustness-dir outputs/robustness --out-dir outputs/paper_tables --dataset visa || true
step "refresh summaries"
$PY scripts/aggregate_uncertainty.py --out-dir outputs/paper_tables || true
$PY scripts/runtime_audit.py --out-dir outputs/paper_tables || true
$PY scripts/compute_pixel_metrics.py --pattern '*_mvtec_*_normal_synthetic' --out-dir outputs/paper_tables --main-only --max-side 128 --resume --variants patchcore anomalydino subspacead head_pca calib_subspace_head || true
step "run tests"
bash scripts/run_tests.sh
step "finalizer completed successfully"
