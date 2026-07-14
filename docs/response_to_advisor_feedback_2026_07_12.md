# Phản hồi góp ý của thầy — bản cập nhật 2026-07-12

Tài liệu này trả lời từng góp ý trong `feedback.pdf` theo cấu trúc: **Góp ý → Hướng giải quyết → Kết quả**. Lưu ý: bản feedback đánh giá paper V1; nhiều thí nghiệm đã được chạy lại/bổ sung trên codebase mới (full 15 lớp MVTec, SC3R full-grid, official AnomalyDINO), nên một số góp ý đã được giải quyết bằng số liệu mới.

---

## 2.1. Lệch khái niệm conformal p-value vs xác suất hậu nghiệm; ECE làm thước đo chủ đạo

**Góp ý:** Conformal chỉ bảo đảm P(p ≤ α) ≤ α trên dữ liệu normal (kiểm soát báo động giả), không bảo đảm 1−p là posterior đã hiệu chỉnh. Dùng ECE làm thước đo chủ đạo là thiếu nhất quán nội tại; ECE của 1−p còn phụ thuộc prevalence của benchmark. Cần: FAR thực nghiệm tại các ngưỡng α cố định, kiểm định uniformity của p-value (Q-Q/KS), risk-coverage — và phải là **bằng chứng chính**, không phải "next experiments".

**Hướng giải quyết:** Chuyển toàn bộ trục bằng chứng trung tâm sang các thước đo conformal-native; hạ ECE xuống thứ yếu và công bố tính nhạy prevalence như một finding.

**Kết quả (đã chạy, đã vào paper):**
1. **FAR tại α cố định** (`scripts/evaluate_conformal_false_alarm.py`, bảng `tab_false_alarm_control.tex`): chạy trên **cả full VisA (56.000 ảnh) và full MVTec 15 lớp (37.464 ảnh)** tại α ∈ {0.01, 0.05, 0.10, 0.20}. Trong quá trình này phát hiện **bug so sánh float32**: p-value 1/5 được lưu thành 0.20000000298 nên quy tắc `p ≤ 0.20` âm thầm loại mọi alarm tại floor — toàn bộ số 0/0 tại k=4, α=0.20 trước đây là artifact. Đã sửa (tolerance 1e-6) và tính lại: VisA k=4 α=0.20 có FAR 0.14–0.16, detection 0.58–0.61, precision ≈0.81.
2. **Kiểm định uniformity** (`scripts/analyze_pvalue_uniformity.py`, mới): vì p-value few-shot **rời rạc trên lưới {j/(k+1)}**, KS liên tục với U(0,1) sẽ luôn bác bỏ một cách giả tạo. Kiểm định đúng: so sánh CDF thực nghiệm tại từng điểm lưới với kỳ vọng chính xác j/(k+1), thống kê KS rời rạc, p-value bằng Monte Carlo trên null rời rạc chính xác. Kết quả: uniformity bị bác bỏ ở **cả 16 cell** (MC p ≤ 0.005), nhưng **hướng vi phạm có cấu trúc** — VisA k=4 lệch conservative; VisA k=8 và MVTec (cả hai k) lệch **anti-conservative** dưới corruption (nặng nhất: Gaussian noise MVTec k=4, F̂(0.2)=0.46 so với 0.20 danh định). Kết quả này đồng thời trả lời câu hỏi k=8 của mục 2.2 và là động cơ trực tiếp cho SC3R matched-condition. Dữ liệu Q-Q đã xuất ra `pvalue_uniformity_*_qq.csv` để vẽ hình.
3. **Risk-coverage**: đã có sẵn dữ liệu selective reliability trên cả hai benchmark; đưa vào paper: abstain 20% ảnh bất định nhất (entropy) giảm ECE LOIO trên MVTec từ 0.068 xuống 0.030.
4. **Attainable-alpha** (`scripts/analyze_attainable_alpha.py`, mới, kèm bảng riêng): với k support, không alarm nào có thể nổ dưới α = 1/(k+1); việc báo "FAR gần 0 tại α nhỏ" là artifact độ phân giải chứ không phải tính an toàn. Đây là khung đọc đúng cho mọi bảng FAR.
5. **Prevalence stress**: giữ nguyên finding (LOIO ECE 0.404 tại prevalence 1% → 0.149 tại 50%, thứ hạng LOIO/weighted đảo chiều) và ghi rõ trong results + limitations: ECE chỉ là secondary metric.

---

## 2.2. Vi phạm exchangeability trong cấu trúc LOIO; hiện tượng k=8; thiếu trích dẫn Tibshirani 2019

**Góp ý:** Residual calibration fit trên k−1 ảnh nhưng test score fit trên đủ k ảnh → không exchangeable, p-value mất tính hợp lệ hình thức; cần trích dẫn cross-conformal/jackknife+; cần giải thích thấu đáo ECE k=8 (0.114) kém k=4 (0.039); thiếu trích dẫn Tibshirani et al. 2019 cho weighted conformal.

**Hướng giải quyết:** (a) thừa nhận trực diện trong method + trích dẫn; (b) định lượng thực nghiệm bằng matched-LOIO audit (đúng tinh thần jackknife+ pairing); (c) kiểm chứng giả thuyết support-sạch/test-nhiễu bằng kiểm định uniformity.

**Kết quả:**
1. Method có đoạn **"Exchangeability caveat"** mới: nêu rõ bất đối xứng k−1 vs k, định vị Eq.(6) là xấp xỉ leave-one-out theo tinh thần cross-conformal/jackknife+ (cite Vovk 2005, Barber et al. 2021, Hennhöfer & Preisach 2024, Bates et al. 2023, Laxhammar & Falkman 2015), không claim finite-sample guarantee.
2. **Matched-LOIO audit** (đã chạy từ trước, nay đưa vào paper): chấm support và test dưới cùng fold-specific subspace (pairing s₋ᵢ(x) với r₋ᵢ). Kết quả: **không** cải thiện trade-off vận hành (clean FAR 0.17→0.25, power gần như không đổi) → vi phạm chủ yếu do **lệch điều kiện support–test** (support sạch, test nhiễu), không phải do bất đối xứng leave-one-out. Đây chính là failure mode mà SC3R matched-condition xử lý.
3. **Giải thích k=8**: kiểm định uniformity xác nhận đúng giả thuyết thầy nêu — corruption thổi phồng residual của ảnh normal test so với tập LOIO sạch; k=8 cho subspace khít hơn nên khuếch đại lệch, đẩy p-value sang anti-conservative (VisA k=4 conservative → k=8 anti-conservative). Đã viết thành cơ chế trong results, thay cho lời giải thích một câu cũ.
4. **Tibshirani et al. 2019** đã được cite tại cả hai chỗ dùng weighted conformal (method + related work); xác minh code (`src/conformal.py:31-51, 187-222`) đúng là weighted conformal theo Tibshirani với density-ratio từ logistic domain classifier.

---

## 2.3. Tính rời rạc p-value khiến so sánh ECE thiếu công bằng

**Góp ý:** p-value LOIO chỉ có k+1 mức; ECE trên đầu ra rời rạc nhạy với binning; so với Platt liên tục là không cùng độ phân giải; cần công bố số bin, bổ sung adaptive ECE, thảo luận tính rời rạc.

**Hướng giải quyết:** Công bố binning; cài **adaptive (equal-mass) ECE** — không thể bị "nịnh" bởi ≤ k+1 mức confidence; so sánh có kiểm định ghép cặp.

**Kết quả** (`scripts/analyze_calibrator_significance.py`, mới):
- Công bố: ECE dùng **15 bin equal-width** (khai trong results).
- Adaptive ECE per-cell của LOIO **cao hơn** equal-width (MVTec k=4: 0.120→0.160; VisA k=4: 0.132→0.227) — xác nhận một phần nghi ngờ của thầy: binning equal-width có làm đẹp số — **nhưng thứ tự so với Platt không đổi** (Platt 0.22–0.29). Đã viết trung thực vào results: "binning does inflate the apparent margin, which is one more reason the operational analyses, not ECE, carry the central claim."
- Tính rời rạc được xử lý tận gốc bằng attainable-alpha framework (mục 2.1.4).

---

## 2.4. Nguồn nhãn huấn luyện của các calibrator họ Platt

**Góp ý:** Eq.(4) cần nhãn để fit w, b — nguồn nhãn từ đâu? Nếu Platt học trên synthetic lệch phân phối thì "LOIO tốt hơn Platt" không nói lên nhiều.

**Hướng giải quyết:** Truy vết code đầy đủ (`src/models/head_pca.py`, `src/calibration/platt.py`, `src/run_experiment.py`) và mô tả tường minh trong method.

**Kết quả** (đoạn "Calibrator training protocol and label source" mới trong method):
- Mode chính `normal_synthetic` **không dùng bất kỳ nhãn anomaly thật nào**: tập calibration = k ảnh support normal (nhãn 0) + số lượng bằng đúng ảnh synthetic (nhãn 1), sinh bằng cách thay 25% patch feature của một ảnh support bằng patch support lấy mẫu lại + nhiễu Gaussian + sign shift (perturbation trong feature space, không phải CutPaste ảnh).
- s_head được định nghĩa đầy đủ (MLP 384→256→1, BCE, chỉ tham gia φ(x), không tham gia ranking).
- Mode `anomaly_val` (10% anomaly thật) chỉ được báo cáo như **upper bound có dán nhãn rõ ràng**.
- Tính công bằng: cả LOIO và Platt đều chỉ thấy đúng k support normal + không thông tin test → so sánh đối xứng, viết rõ trong paper.

---

## 2.5. Tiêu đề "Routing" nhưng nội dung không routing

**Góp ý:** Route chính là fixed LOIO; gating bị đẩy xuống ablation; hoặc đổi tên, hoặc hoàn thành no-label routing và nâng thành đóng góp chính. Mục III-E quá sơ sài.

**Hướng giải quyết:** Chọn phương án 2 của thầy — **hoàn thành no-label routing và nâng thành đóng góp chính**, dưới dạng SC3R.

**Kết quả:** SC3R (Source-Conditioned Cross-Category Reliability Routing) đã vượt **decision gate đăng ký trước** trên **toàn bộ 15 lớp MVTec** (k=4, seeds 0–2, 675 cells, matched-condition):
- FAR trung bình bám gần đúng mức danh định: 0.050 / 0.105 / 0.216 tại α = 0.05 / 0.10 / 0.20 (tiêu chí ≤ α+0.02: đạt);
- Power 0.22 / 0.42 / 0.69 ở vùng α mà target-only conformal **câm về cấu trúc** (dưới floor 1/(k+1));
- No-harm 89% / 82% / 89% (tiêu chí ≥ 80%: đạt);
- **Hierarchical class–seed bootstrap CI của power gain loại trừ 0 cho MỌI corruption** tại cả hai mức α dưới floor (yếu nhất: JPEG α=0.05 CI [0.02, 0.28]);
- Không dùng nhãn anomaly target (threshold chọn trên normal của source classes held-out);
- Phát hiện thêm: tại α=0.20 (floor của anchor), target-only **over-alarm** dưới corruption (FAR tới 0.46) trong khi SC3R giữ ≤0.24 — routing nguồn có giá trị ở cả mức α anchor với được.
Routing giờ là cơ chế thật (source-validated threshold + safe anchor rule), có công thức, có gate criteria trong experiments. Tiêu đề "Routing" được giữ và được nội dung bảo chứng. Mục SAGE-inspired gating cũ thu về vai trò thảo luận.

---

## 2.6. Baseline và độ tin cậy thống kê

**Góp ý:** (i) thiếu temperature scaling / isotonic / histogram binning; (ii) thiếu baseline few-shot hiện đại (WinCLIP; nhắc RegAD, GraphCore, FastRecon, InCTRL); (iii) chỉ có point estimate — cần mean±std và Wilcoxon/Friedman; PCA128 vs PCA64 cần CI.

**Hướng giải quyết & kết quả:**
- **(iii) — đã làm đầy đủ:** `scripts/analyze_calibrator_significance.py` chạy Wilcoxon signed-rank ghép cặp trên cell class×seed×corruption cho cả hai benchmark. LOIO vs Vector Platt: p ≤ 5×10⁻⁹ ở mọi (dataset, k); mean±std vào bảng (vd. MVTec k=4: 0.120±0.054 vs 0.223±0.095, LOIO tốt hơn ở 84% của 360 cell). **Caveat trung thực:** vs Shift-Aware Platt tại VisA k=8 không có ý nghĩa (p=0.20, 51%) — đã ghi thẳng vào abstract + results. SC3R có hierarchical bootstrap CI (đã nêu trên).
- **(ii) — một phần:** RegAD/GraphCore/FastRecon/WinCLIP/InCTRL đã được thêm vào related work với định vị "complementary — chúng tôi không cạnh tranh ranking". Official AnomalyDINO đã được **chạy thật bằng code gốc** (k=1/4/8 × 3 seeds: AUROC 0.965/0.976/0.980) và vào Table I làm mốc accuracy. Chạy WinCLIP dưới audit của mình được xếp vào limitations như việc còn lại (cần setup CLIP pipeline riêng).
- **(i) — ĐÃ XONG (2026-07-14):** temperature scaling / isotonic regression / histogram binning đã được cài (`src/calibration/scalar.py`) và fit đúng cùng protocol synthetic per cell (k support normal + k synthetic anomaly, cùng perturbation với vector Platt), rồi áp lên `raw_score` của views CSV hiện có — cách tái dùng này là CHÍNH XÁC tuyệt đối vì PCA fit deterministic trên cùng cached support features (đã verify end-to-end: `max_abs_diff = 0.00e+00`). Kết quả trên **cả full MVTec 15 lớp lẫn full VisA**: LOIO thắng cả 3 calibrator chuẩn (và scalar Platt) ở mọi (dataset, k) — Wilcoxon ghép cặp p ≤ 2.5×10⁻⁴ trong 16/16 so sánh, p ≤ 4.8×10⁻⁸ trong 14/16; sát nhất là isotonic tại k=8 (MVTec delta −0.023, 55% cells) — đã ghi trung thực vào results. Bảng `tab_scalar_calibrators.tex`.
- **CI cho PCA128 vs PCA64 — ĐÃ XONG (2026-07-14):** paired hierarchical bootstrap class→seed trên 60 cells/k: delta AUROC +0.011/+0.015/+0.016/+0.014 tại k=1/2/4/8, CI 95% loại trừ 0 ở cả 4 mức k (`pca128_vs_pca64_visa_hierarchical_ci.csv`). Đã đưa vào results.

---

## 2.7. Ma trận thực nghiệm chưa khép kín; số liệu cần rà soát

**Góp ý:** (i) conformal MVTec bị hoãn — không chấp nhận được; (ii) cách lấy mẫu 120 ảnh phải mô tả rõ; (iii) ECE 0.693 và storage 6.000 MB của dòng PatchCore/AnomalyDINO trông như placeholder; nếu ECE của baseline chỉ là min-max thô thì so sánh thành strawman; (iv) k=1 LOIO bất khả thi — ECE của CRR lấy từ view nào?

**Kết quả:**
1. **Full MVTec conformal đã chạy xong**: 15 lớp × k{4,8} × seeds 0–2 × 4 corruption = 37.464 ảnh. Kết luận VisA tái lập: LOIO ECE tổng 0.0684 (k=4: 0.060, k=8: 0.077), thắng Vector/Shift-Aware Platt ở **8/8** cell k×corruption. Có subsection riêng trong results.
2. **Sampling 120 ảnh**: label-stratified random với seed cố định và manifest lưu lại (đã mô tả trong experiments; script `evaluate_corruptions.py` đã đổi từ "first sorted" sang stratified-random từ trước).
3. **Số 0.693 KHÔNG phải placeholder — nhưng đúng là suy biến, đã giải phẫu tận gốc:** dưới protocol scalar-Platt label-free, xác suất của baseline NN sụp về hằng số: ≈1 khi mọi support patch tự khớp (k≤2, distance 0) và ≈0 khi memory bank chạm trần 4096 patch phải subsample (k≥4). Do đó ECE = phần bù prevalence (0.277/0.693) và Brier ≈ ECE — chữ ký của xác suất hằng. Storage đúng 6.000 MB = trần 4096 patch × 384 dim × 4 byte. Toàn bộ giải thích đã vào caption Table I, ghi rõ các giá trị này là *diagnostic, not competitive* để tránh strawman.
4. **k=1**: caption Table I ghi rõ ECE của CRR tại k=1 lấy từ vector-Platt view (LOIO cần k≥2).

---

## Các vấn đề vừa và nhỏ (mục 3)

| # | Góp ý | Trạng thái |
|---|---|---|
| (1) | s_head chưa định nghĩa | **Xong** — định nghĩa đầy đủ trong method (MLP 384→256→1, synthetic patch perturbation, chỉ vào φ(x)) |
| (2) | Tên gọi thiếu nhất quán | **Xong** — subsection "Naming Convention" mới trong experiments |
| (3) | "Low-storage" chưa gồm backbone | **Xong** — đoạn "Storage accounting": backbone dùng chung ≈84MB fp32; 0.472MB = PCA 0.098 + head/calibrator ≈0.37 (khớp increment 0.094MB của PCA128) |
| (4) | Agg max hay top-tail, thí nghiệm nào | **Xong** — công bố rõ: max cho bảng clean, top-1% mean (ρ=0.01) cho pipeline conformal; ablation độ nhạy chưa chạy (đưa vào việc còn lại) |
| (5) | Thiếu trích dẫn | **Xong** — thêm Tibshirani 2019, Barber 2021, Bates 2023, Laxhammar & Falkman 2015, Ovadia 2019 (+ WinCLIP, RegAD, GraphCore, FastRecon, InCTRL) |
| (6) | Refs [3][4][5] thiếu tác giả/venue | **Xong** — AnomalyDINO = Damm, Laszkiewicz, Lederer, Fischer, WACV 2025, tr.1319–1329; VisA = Zou et al., ECCV 2022 (SPot-the-Difference); Khan & Krawczyk bổ sung tác giả. Venue SAGE giữ theo thông tin công bố của nhóm |
| (7) | Thiếu phân tích chi phí tính toán | **Xong** — đoạn compute cost: cached scoring 1.3ms/ảnh (subspace) vs 5–13ms (NN); backbone forward chi phối end-to-end; LOIO fit k subspace <1s tại k≤8 |
| (8) | Font trục Hình 1–2 nhỏ | **Chưa** — cần xuất lại figure vector, font to (việc trình bày, làm khi chốt bản in) |
| (9) | Abstract dày số, câu "every cell" dễ đọc nhầm | **Xong** — thêm mệnh đề làm rõ weighted conformal + Wilcoxon caveat |
| (10) | Contribution 1–2 trùng ý | **Xong** — gộp còn 4 gạch đầu dòng |

---

## Đánh giá độ sẵn sàng cho Q1 (Neural Computing and Applications)

**Trước feedback + đợt thí nghiệm mới: chưa đủ. Hiện tại: gần đạt, còn 4 việc.**

Điểm đã đạt chuẩn:
- Ma trận thực nghiệm khép kín trên cả hai benchmark (VisA 56k + MVTec 37k ảnh), official baseline chạy bằng code gốc, mọi claim chính có kiểm định thống kê ghép cặp hoặc hierarchical bootstrap CI.
- Bằng chứng trung tâm đã là conformal-native (FAR tại α cố định, uniformity test rời rạc chính xác, attainable-alpha, risk-coverage) — đúng yêu cầu nền tảng nhất của thầy.
- Có đóng góp phương pháp thật (SC3R vượt pre-registered gate với CI loại trừ 0) thay vì chỉ benchmark; negative results và caveat được báo cáo trung thực — phong cách phù hợp NCAA.

Còn lại trước khi nộp (trạng thái 2026-07-12):
1. **Temperature scaling / isotonic / histogram binning** dưới cùng protocol (mục 2.6.i) — thiếu sót lớn duy nhất về nội dung.
2. **Ablation Agg (max vs top-ρ)** — nhỏ, chạy nhanh trên representative.
3. **Hình**: vẽ Q-Q uniformity + risk-coverage thành figure; xuất lại figure vector với font đạt chuẩn cột.
4. **Trình bày**: NCAA dùng định dạng Springer (sn-jnl), cần chuyển từ IEEEtran; abstract nên rút gọn thêm.

**Cập nhật 2026-07-14: CẢ 4 MỤC ĐÃ XONG.** (1) 3 calibrator chuẩn chạy trên cả hai benchmark, LOIO thắng có kiểm định (chi tiết mục 2.6.i ở trên); (2) Agg ablation: spread 0.01–0.02 AUROC giữa max và top-ρ, lựa chọn trong paper nằm trong 0.01–0.02 của optimum (`tab_agg_ablation.tex`); (3) 4 figure vector (Q-Q uniformity, risk-coverage, reliability, ECE-by-corruption) đã dựng bằng palette colorblind-safe, font chuẩn in (`latex/figures/`); (4) paper đã chuyển sang Springer sn-jnl trong `latex/`, abstract viết lại gọn hơn, compile sạch 25 trang. Bonus: SC3R k=8 full 15 lớp đã chạy — power gain CI loại trừ 0 ở mọi corruption dưới floor; FAR budget đạt tại α=0.05, vượt biên nhẹ tại α=0.10 (0.121, no-harm 74%) do gaussian/jpeg — đã ghi trung thực thành boundary trong results + limitations. Việc còn lại duy nhất trước khi nộp: điền tên tác giả/affiliation thật vào `latex/main.tex` và vòng review cuối của thầy.
