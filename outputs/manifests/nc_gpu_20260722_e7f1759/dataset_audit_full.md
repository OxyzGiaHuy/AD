# Full dataset audit

Status: **PASS**

## mvtec

- Resolved root: `/home/crl/MoME/other/AD/tmp/ad-neurocomputing/extracted/mvtec`
- Records: 5354
- Aggregate counts: `{"test_anomaly": 1258, "test_normal": 467, "train_normal": 3629}`
- Classes: bottle, cable, capsule, carpet, grid, hazelnut, leather, metal_nut, pill, screw, tile, toothbrush, transistor, wood, zipper
- All checks: **PASS**

## visa

- Resolved root: `/home/crl/MoME/other/AD/tmp/ad-neurocomputing/extracted/visa_raw`
- Records: 10821
- Aggregate counts: `{"test_anomaly": 1200, "test_normal": 962, "train_normal": 8659}`
- Classes: candle, capsules, cashew, chewinggum, fryum, macaroni1, macaroni2, pcb1, pcb2, pcb3, pcb4, pipe_fryum
- All checks: **PASS**

## mpdd

- Resolved root: `/home/crl/MoME/other/AD/tmp/ad-neurocomputing/extracted/mpdd_raw/MPDD`
- Records: 1346
- Aggregate counts: `{"test_anomaly": 282, "test_normal": 176, "train_normal": 888}`
- Classes: bracket_black, bracket_brown, bracket_white, connector, metal_plate, tubes
- All checks: **PASS**

The machine-readable JSON includes per-class counts, every boolean check, and exact support paths for all datasets, k values, and seeds.

No image content was read or modified by this metadata/path audit beyond filesystem existence checks performed by the loader and audit.
