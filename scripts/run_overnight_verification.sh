#!/usr/bin/env bash
set -euo pipefail
cd /home/crl/AD
PY=/home/crl/miniconda3/envs/ad/bin/python
RUN_LIST=configs/generated/mvtec_full/run_list.txt
LOG_DIR=outputs/logs
STATUS=$LOG_DIR/overnight_verification.status
LOCK=$LOG_DIR/overnight_verification.lock
mkdir -p "$LOG_DIR"
exec 9>"$LOCK"
if ! flock -n 9; then
  echo "another overnight verification job is already running" | tee "$STATUS"
  exit 2
fi
step() {
  echo "[$(date -Is)] $*" | tee -a "$STATUS"
}
count_fgsm() {
  $PY - <<'PYCOUNT'
from pathlib import Path
rb=Path('outputs/robustness')
for eps in ['2_255','4_255','8_255']:
    print(f"fgsm_eps{eps}=", len(list(rb.glob(f'calib_subspace_head_mvtec_*_fgsm_eps{eps}/metrics.json'))))
PYCOUNT
}
CURRENT_PID=${1:-}
: > "$STATUS"
step "overnight verification started"
if [[ -n "$CURRENT_PID" ]]; then
  while kill -0 "$CURRENT_PID" 2>/dev/null; do
    step "waiting for existing FGSM pid=$CURRENT_PID"
    count_fgsm | tee -a "$STATUS"
    sleep 60
  done
fi
step "resume/check FGSM epsilon 2/255"
$PY -u scripts/evaluate_fgsm_batch.py --run-list "$RUN_LIST" --variant calib_subspace_head --epsilon 2/255
count_fgsm | tee -a "$STATUS"
step "run FGSM epsilon 4/255"
$PY -u scripts/evaluate_fgsm_batch.py --run-list "$RUN_LIST" --variant calib_subspace_head --epsilon 4/255
count_fgsm | tee -a "$STATUS"
step "aggregate FGSM sweep"
$PY scripts/aggregate_fgsm_sweep.py --out-dir outputs/paper_tables
step "aggregate robustness tables"
$PY scripts/aggregate_robustness_all.py --outputs-dir outputs --robustness-dir outputs/robustness --out-dir outputs/paper_tables --dataset mvtec || true
$PY scripts/aggregate_robustness_all.py --outputs-dir outputs --robustness-dir outputs/robustness --out-dir outputs/paper_tables --dataset visa || true
step "refresh uncertainty/runtime/pixel summaries"
$PY scripts/aggregate_uncertainty.py --out-dir outputs/paper_tables || true
$PY scripts/runtime_audit.py --out-dir outputs/paper_tables || true
$PY scripts/compute_pixel_metrics.py --pattern '*_mvtec_*_normal_synthetic' --out-dir outputs/paper_tables --main-only --max-side 128 --resume --variants patchcore anomalydino subspacead head_pca calib_subspace_head || true
step "run unit/smoke tests"
bash scripts/run_tests.sh
step "overnight verification completed successfully"
