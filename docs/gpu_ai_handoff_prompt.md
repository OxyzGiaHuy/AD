# Prompt handoff cho AI trên GPU server

Copy toàn bộ nội dung từ mục **PROMPT** bên dưới cho AI có quyền terminal trên
GPU server. Chỉ cần thay các giá trị trong `SERVER_INPUTS` nếu đã biết; nếu chưa
biết, AI phải tự kiểm tra và hỏi lại thay vì đoán.

---

## PROMPT

Bạn đang tiếp quản giai đoạn GPU của paper CRR/SC3R hướng tới Neurocomputing.
Mục tiêu là chạy đầy đủ protocol đã đóng băng, tạo artifact có thể audit và báo
cáo cả kết quả không đạt. Không được tối ưu theo test set, bỏ cell thất bại,
điền số thủ công vào paper, hay gọi kết quả lịch sử là kết quả của pipeline mới.

### SERVER_INPUTS

```text
REPO_ROOT=<đường dẫn repo AD trên server>
MVTEC_ROOT=<đường dẫn MVTec AD hoặc UNKNOWN>
VISA_ROOT=<đường dẫn VisA hoặc UNKNOWN>
MPDD_ROOT=<đường dẫn MPDD hoặc UNKNOWN>
SCRATCH_ROOT=<ổ scratch đủ dung lượng hoặc UNKNOWN>
GPU_DEVICE=<ví dụ cuda:0 hoặc AUTO>
```

Nếu một giá trị là `UNKNOWN`, hãy kiểm tra filesystem/environment trước. Chỉ hỏi
người dùng khi không thể xác định an toàn. Không tự tải dataset có license hoặc
credentials chưa được người dùng cho phép. Không redistribute ảnh raw.

### 1. Đọc tài liệu có thẩm quyền trước khi chạy

Đọc đầy đủ, theo thứ tự:

1. `docs/README.md`
2. `docs/gpu_experiment_runbook.md`
3. `docs/sc3r_formal_specification.md`
4. `docs/neurocomputing_claim_audit.md`
5. `docs/submission_blockers.md`
6. `configs/submission_cpu_pipeline.example.json`

Các file lịch sử khác trong `docs/` không phải protocol cuối. Nếu có mâu thuẫn,
ưu tiên các tài liệu trên và dừng để báo cáo nếu vẫn không giải quyết được.

### 2. Quy tắc integrity không được vi phạm

- Không dùng target anomaly labels để fit detector, calibrator, router, chọn
  threshold, chọn condition mode hoặc chọn hyperparameter.
- Không thay backbone, image size, PCA dimension, rho, corruption severity,
  số ảnh, k, seed, alpha, delta, candidate cap hoặc R/P/C split sau khi xem
  target metrics.
- Primary grid: `k={1,2,4,8}`, seeds `{0,1,2,3,4}`, alpha
  `{0.05,0.10,0.20}`, năm conditions `clean`, `gaussian_noise`, `blur`,
  `brightness_contrast`, `jpeg`, tối đa 120 ảnh/cell, `rho=0.01`, PCA64.
- `k=1` phải mang metadata `patch_split_conformal`, không gọi là image LOIO.
- Với cùng class/seed, support phải nested: k=1 subset k=2 subset k=4 subset k=8.
- Các corruption views phải có cùng `base_image_path` và label.
- Không đếm nhiều corruption views của một ảnh như các quan sát độc lập.
- Matched-condition là oracle/metadata-assisted mode. Condition-agnostic mới là
  mode deployment-facing. Mismatched-condition chỉ là negative control.
- Image Clopper--Pearson certificate chỉ đảm bảo fixed source-image mixture dưới
  giả định của nó. Category Hoeffding certificate là new-category stress test.
  Không dùng image result để che category failure.
- Target FAR/power luôn là empirical transfer result, không phải unconditional
  target guarantee.
- Giữ tất cả threshold-zero cells. Không drop NaN precision khi không có alarm.
- Negative/null result phải được báo cáo. Không đổi protocol để “cứu” gate.

### 3. Preflight bắt buộc

Trong `REPO_ROOT`, ghi toàn bộ output sau vào log:

```bash
git status --short
git rev-parse HEAD
nvidia-smi
python --version
```

Sau đó:

- xác nhận worktree/commit dùng cho run; không chạy từ code chưa được snapshot;
- kiểm tra dung lượng scratch và output;
- resolve ba dataset root thật; ánh xạ chúng vào đúng layout mà runbook/loader
  yêu cầu (`data/mvtec`, `data/visa`, `data/mpdd`) bằng config hoặc symlink rõ
  ràng, rồi lưu `readlink -f`/đường dẫn nguồn vào manifest;
- kiểm tra dataset layout, class names, split, masks và license;
- xác nhận không có support/evaluation overlap;
- tạo environment CUDA tương thích và lưu chính xác Python, PyTorch,
  torchvision, CUDA, cuDNN, driver, GPU model, DINOv2 code/weight ID;
- chạy CPU test suite trước: `python -m pytest -q`;
- chạy một smoke test nhỏ chỉ để kiểm tra infrastructure. Smoke output không
  được dùng làm paper evidence.

Nếu test/preflight fail, sửa lỗi infrastructure hoặc code correctness trước,
thêm test regression, commit/snapshot lại, rồi bắt đầu run tag mới. Không âm
thầm tiếp tục với artifact tạo từ nhiều code revisions.

### 4. Run tag và logging

Tạo run tag bất biến, ví dụ:

```bash
RUN_TAG="nc_gpu_YYYYMMDD_<short_git_sha>"
```

Mỗi command phải có:

- log riêng chứa command, stdout, stderr, exit code, thời gian bắt đầu/kết thúc;
- run tag và git commit;
- resume chỉ khi script hỗ trợ và artifact audit xác nhận phần đã có hợp lệ.

Giảm batch size để xử lý OOM được phép nếu không thay đổi numerical protocol;
phải ghi lại. Không được giảm image count, class count, k hoặc seed để né lỗi.

### 5. Thứ tự thực hiện

Thực hiện toàn bộ các phase trong `docs/gpu_experiment_runbook.md` theo đúng
command và thứ tự ghi trong runbook; danh sách dưới đây chỉ là checklist, không
thay thế command gốc:

1. Preflight: environment, dataset, manifests và immutable run metadata.
2. P0: tìm/recover artifact lịch sử để kiểm tra lineage; không tự động coi đó
   là evidence mới.
3. P1: GPU export cho MVTec và VisA, bao gồm:
   - per-image SC3R views;
   - support statistics;
   - support manifests;
   - base-image identity và corruption parameters.
4. Chạy `scripts/audit_sc3r_artifacts.py` với exact expected grid cho từng
   dataset. Audit phải pass trước mọi analysis.
5. P2: export LOIO support residuals và chạy target-only/clustered diagnostics;
   mọi significance claim phải có clustering unit và multiplicity treatment.
6. P3: historical reproduction chỉ để lineage và phải gắn nhãn empirical/
   historical, không gọi là independently certified.
7. P4/P5/P6: strict nested SC3R, paired baselines và ablations:
   - `target_only`;
   - `randomized_pvalue`;
   - `pooled_source_conformal` dùng toàn bộ routed source pool;
   - `nested_sc3r`;
   - matched, clean, condition-agnostic, mismatched modes;
   - normalization, source class/image count, candidate cap, R/P/C allocation;
   - k=1/2/4/8.
8. P7: export/audit MPDD rồi chạy MVTec-to-MPDD primary external transfer.
   Within-MPDD chỉ là empirical replication do MPDD có quá ít classes cho
   strong nested category split.
9. Chạy one-command CPU pipeline từ config final.

Tạo config final bằng cách copy file mẫu, thay mọi `RUN_TAG` và path thật:

```bash
cp configs/submission_cpu_pipeline.example.json \
   configs/submission_cpu_pipeline.final.json
python scripts/run_cpu_submission_pipeline.py \
  --config configs/submission_cpu_pipeline.final.json
```

Không sửa script/table bằng tay để ép kết quả. Pipeline phải sinh:

- paired detailed methods;
- candidate UCBs và partitions;
- paired-cell audit;
- zero-preserving summaries;
- Bonferroni simultaneous comparisons;
- empirical gate JSON;
- LaTeX table fragments;
- `cpu_pipeline_manifest_<RUN_TAG>.json` với SHA-256.

### 6. Acceptance và failure policy

- Category threshold nonzero rate dưới 80% là empirical gate failure và phải
  xuất hiện trong report.
- Mean target FAR vượt `alpha+0.02`, no-harm dưới 80%, power bằng 0 hoặc
  simultaneous power-gain lower bound không dương đều phải ghi fail đúng cell.
- Nếu category Hoeffding gần như luôn trả threshold 0, kết luận là formal
  new-category certification underpowered; không thay bằng image claim.
- Nếu condition-agnostic không giữ được meaningful sub-floor power/FAR budget,
  giới hạn claim vào setting có condition metadata.
- Nếu MPDD layout/license/data không đúng, dừng phase MPDD và ghi blocker;
  không dùng partial undocumented subset.
- Không được chỉ báo cáo pooled means nếu một corruption/class/k thất bại.

### 7. Deliverables phải trả lại

Tạo một thư mục:

```text
handoff/<RUN_TAG>/
```

chứa tối thiểu:

- `GPU_RUN_REPORT.md`;
- exact commands/logs và exit codes;
- git commit + `git status --short` cuối;
- environment lock và GPU/CUDA metadata;
- dataset class/count/checksum/license manifests;
- support manifests;
- per-image view CSVs và LOIO residual CSVs;
- artifact-audit JSONs;
- nested detailed/candidate/partition outputs;
- paired/simultaneous/summary/gate outputs;
- generated LaTeX fragments;
- final CPU pipeline manifest;
- SHA-256 file covering mọi deliverable;
- danh sách artifact bị thiếu hoặc failed phase.

Không đóng gói raw datasets, feature caches khổng lồ hoặc temporary corrupted
images trừ khi người dùng yêu cầu. Có thể tạo archive chỉ từ derived artifacts,
logs, configs và manifests.

`GPU_RUN_REPORT.md` phải có các mục:

1. Executive status: complete / partial / failed.
2. Commit, environment, GPU, dataset versions.
3. Commands đã chạy và phase exit status.
4. Artifact audit results.
5. Empirical gate pass/fail counts, bao gồm zero thresholds.
6. Category versus image certificate, không trộn estimand.
7. Matched versus condition-agnostic boundary.
8. k=1/2 results và metadata caveat.
9. MVTec-to-VisA và MVTec-to-MPDD transfer boundaries.
10. Negative results, deviations và unresolved blockers.
11. Exact paths/checksums cần copy về máy viết paper.

### 8. Cách giao tiếp

- Gửi progress update sau mỗi phase hoặc ít nhất mỗi 30--60 phút.
- Khi bị lỗi, đưa command, log excerpt, root cause và safe next action.
- Chỉ hỏi người dùng khi cần dataset permission/path/credentials hoặc một thay
  đổi làm khác frozen scientific protocol.
- Không tuyên bố paper đạt chuẩn submission chỉ vì jobs chạy xong. Kết luận cuối
  phải dựa trên artifact audits và gate report.

Hãy bắt đầu bằng preflight và báo lại các giá trị đã resolve trong
`SERVER_INPUTS` trước khi chạy full GPU jobs.

---

## Những gì cần gửi kèm prompt

AI trên server cần ít nhất:

- toàn bộ repository ở đúng commit chứa prompt này;
- dataset paths hoặc quyền hỏi/tải dataset;
- quyền sử dụng GPU và đủ scratch storage;
- quyền ghi vào `outputs/`, `logs/`, `handoff/`;
- nếu server không có internet: DINOv2 weights và Python/CUDA wheels/cache đã
  được chuẩn bị sẵn.
