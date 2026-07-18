#!/bin/bash
# WinCLIP (community reimpl.) sweep: k=0 (deterministic, 1 run) + k=1 x 3 experiment_indx, both datasets.
set -u
cd /home/crl/AD/third_party/WinClip
PY=/home/crl/miniconda3/envs/ad/bin/python
MVTEC="carpet grid leather tile wood bottle cable capsule hazelnut metal_nut pill screw toothbrush transistor zipper"
VISA="candle capsules cashew chewinggum fryum macaroni1 macaroni2 pcb1 pcb2 pcb3 pcb4 pipe_fryum"
for ds in mvtec visa; do
  [ "$ds" = mvtec ] && CLASSES="$MVTEC" || CLASSES="$VISA"
  for cls in $CLASSES; do
    PYTHONUNBUFFERED=1 $PY eval_WinCLIP.py --dataset $ds --class-name $cls --k-shot 0 --experiment_indx 0 --vis False --root-dir /home/crl/AD/outputs/winclip
    for idx in 0 1 2; do
      PYTHONUNBUFFERED=1 $PY eval_WinCLIP.py --dataset $ds --class-name $cls --k-shot 1 --experiment_indx $idx --vis False --root-dir /home/crl/AD/outputs/winclip
    done
  done
done
touch /home/crl/AD/logs/WINCLIP_SWEEP_DONE
