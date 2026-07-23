#!/usr/bin/env bash
set -uo pipefail

if [[ $# -lt 2 ]]; then
  echo "usage: $0 LOG_FILE COMMAND [ARG ...]" >&2
  exit 2
fi

log_file=$1
shift
mkdir -p "$(dirname "$log_file")"

start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)
{
  echo "run_tag=nc_gpu_20260722_e7f1759"
  echo "git_commit=e7f175990b02aa3cbdb7c92250d57c0272abef9d"
  echo "start_utc=$start_utc"
  printf 'command='
  printf '%q ' "$@"
  echo
} | tee "$log_file"

set +e
"$@" 2>&1 | tee -a "$log_file"
command_status=${PIPESTATUS[0]}
set -e

end_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)
{
  echo "end_utc=$end_utc"
  echo "exit_code=$command_status"
} | tee -a "$log_file"

exit "$command_status"
