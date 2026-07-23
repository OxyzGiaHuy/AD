# Scientific audit of GPU run `nc_gpu_20260722_e7f1759`

## Status

The GPU computation is complete and internally consistent. The result does not
support a useful new-category SC3R certificate under the frozen Hoeffding rule.
This is a protocol-feasibility limitation, not evidence of a failed GPU job.

## Provenance and integrity

- Frozen scientific commit: `e7f175990b02aa3cbdb7c92250d57c0272abef9d`.
- Complete handoff commit: `74fdfd00f3480f3bc5db42e29bc51ec0768ab881`.
- All 811 declared deliverables exist.
- All 811 SHA-256 entries verify.
- No handoff symlink is broken.
- Local fail-closed artifact audits pass:
  - MVTec: 1,500 cells, 156,100 view rows;
  - VisA: 1,200 cells, 144,000 view rows;
  - MPDD: 600 cells, 45,800 view rows.
- GPU preflight reports 98 tests passing. The reconstructed CPU-only local
  environment reports 97 passing and one expected skip because PyTorch is not
  included in the CPU lock.

## Frozen strict result

The empirical category gate contains

`4 jobs x 4 routing modes x 4 k x 3 alpha x 5 conditions = 960`

aggregate gate cells. All 960 fail because every category-certified target cell
uses the zero no-alarm fallback.

| Source to target | Certification categories | Minimum observed category UCB | Positive category threshold |
|---|---:|---:|---:|
| MVTec to MVTec | 4 | 0.950 | 0% |
| VisA to VisA | 3 | 1.000 | 0% |
| MVTec to VisA | 4 | 0.961 | 0% |
| MVTec to MPDD | 4 | 0.986 | 0% |

The failure is predicted by the declared class-level Hoeffding bound. A
positive candidate requires

`n >= log(2*A*M/delta) / (2*alpha^2)`.

For `A=3`, `delta=0.05`, zero empirical loss, and the most favorable `M=1`,
the minimum independent-category counts are 60, 240, and 958 at alpha 0.20,
0.10, and 0.05. The frozen three-way splits provide only three or four.

## Image sensitivity

The fixed-archive image certificate is not equivalent to a new-category
certificate. Across the declared grid its positive-threshold rates are:

- MVTec to MVTec: 36.7%;
- VisA to VisA: 60.4%;
- MVTec to VisA: 41.5%;
- MVTec to MPDD: 37.0%.

These results may be reported only as fixed-archive sensitivity. They cannot
replace the failed category result or establish target-domain control.

## Claim decision

No additional GPU job is required for the selected paper scope:

1. CRR remains an auditable separation of ranking and reliability.
2. Target-only resolution floor `1/(k+1)` remains exact.
3. Historical SC3R remains an empirical routing diagnostic.
4. Strict SC3R is a negative new-category certification result.
5. The category sample-size requirement is promoted as a design-feasibility
   result.
6. Target transfer remains empirical unless dominance or category
   exchangeability is explicitly assumed.

A new GPU run would be required only to make a fresh positive new-category
claim, using a category-rich archive and a protocol frozen before inspecting
that archive. More images or seeds alone do not increase the number of
independent certification categories.

