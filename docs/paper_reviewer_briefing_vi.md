# Tài liệu giải thích paper cho người review

## Conformal Reliability Routing for Low-Storage Few-Shot Industrial Anomaly Detection

Tài liệu này được viết cho một người có nền tảng machine learning/statistics đủ để
review nghiên cứu, nhưng chưa quen với industrial anomaly detection (AD), few-shot
AD hoặc conformal anomaly detection. Mục tiêu là giúp người đọc hiểu đúng:

1. paper đang giải quyết vấn đề gì;
2. thành phần nào là prior art và thành phần nào là contribution;
3. từng khẳng định được hỗ trợ bởi chứng minh, giả định hay thí nghiệm nào;
4. kết quả âm `0/960` của strict SC3R có ý nghĩa gì;
5. paper **không** được phép claim điều gì;
6. nên review bài theo những câu hỏi khoa học nào.

Đây là tài liệu giải thích và định hướng review, không thay thế manuscript chính thức.
Mọi con số dưới đây được đối chiếu với bản manuscript và GPU audit hiện tại.

---

## 1. Tóm tắt bài trong một đoạn

Trong few-shot industrial AD, hệ thống chỉ có rất ít ảnh bình thường của một loại
sản phẩm mới, chẳng hạn \(k=1,2,4,8\), rồi phải phát hiện ảnh hoặc vùng ảnh bất
thường. Các foundation model như DINOv2 có thể tạo feature tốt để **xếp hạng**
ảnh lỗi cao hơn ảnh bình thường, nhưng một score xếp hạng tốt chưa nói được rằng
ngưỡng alarm có giữ đúng false-alarm rate hay không. Paper tách hai bài toán:

- **ranking:** mẫu nào bất thường hơn mẫu nào;
- **reliability/decision:** nếu đặt mức alarm \(\alpha\), tỷ lệ sản phẩm tốt bị
  báo nhầm có thực sự gần hoặc dưới \(\alpha\) hay không.

CRR dùng một ranker DINOv2–PCA gọn nhẹ làm nền, rồi audit nhiều reliability view,
đặc biệt là leave-one-image-out (LOIO) conformal p-value. Paper chỉ ra một giới
hạn chính xác: với \(k\) calibration score, p-value nhỏ nhất là
\(1/(k+1)\), nên target-only alarm hoàn toàn không thể hoạt động ở mức thấp hơn
ngưỡng này. SC3R thử dùng normal images từ các category khác để có độ phân giải
tốt hơn. Kết quả SC3R lịch sử cho thấy cách này có thể hoạt động thực nghiệm,
nhưng strict nested certification với các category độc lập trả về ngưỡng zero
trong toàn bộ 960 gate cell. Paper chứng minh nguyên nhân là số category dùng để
certify quá ít: ngay cả một distribution-free bound không phạt multiplicity
cũng cần ít nhất 14 category tại \(\alpha=0.20\); frozen allocation cần 22 và
Hoeffding gate cần 60, trong khi benchmark chỉ cung cấp 3–4 category
certification. Vì vậy, contribution trung tâm của bài là một reliability audit
framework, các finite-sample barrier, và một ranh giới định lượng về điều mà
few-category source archive có thể hoặc không thể certify; bài không claim một
alarm có target-domain guarantee.

---

## 2. Bài toán và động lực

### 2.1 Industrial anomaly detection là gì?

Industrial AD phát hiện sản phẩm hoặc vùng ảnh có lỗi: vết nứt, thiếu linh kiện,
biến dạng bề mặt, sai texture, v.v. Dữ liệu có tính bất đối xứng:

- ảnh bình thường tương đối dễ thu thập;
- mọi dạng lỗi tiềm năng không thể được liệt kê hoặc gán nhãn đầy đủ;
- category mới có thể chỉ có vài ảnh bình thường khi triển khai.

Do đó, thiết lập của bài là **normal-only few-shot**. Với mỗi target category
\(c\), ta có support set

\[
\mathcal S_c=\{x_1,\ldots,x_k\},
\]

chỉ gồm \(k\) ảnh bình thường. Nhãn normal/anomaly trong test set chỉ được dùng
để đánh giá, không dùng để train detector hay main calibrator.

### 2.2 Vì sao AUROC cao vẫn chưa đủ?

Giả sử detector cho anomaly score:

- sản phẩm tốt: score 0.4;
- sản phẩm lỗi: score 0.8.

Nếu phần lớn lỗi được xếp trên phần lớn normal, AUROC sẽ cao. Tuy nhiên AUROC
không nói ngưỡng 0.6 có tạo 1%, 5% hay 30% false alarm khi category hoặc điều
kiện ảnh thay đổi. Trong nhà máy, đây là khác biệt giữa:

- “mẫu A đáng nghi hơn mẫu B”; và
- “alarm này có thể được vận hành ở ngân sách báo nhầm 5%”.

Paper xem reliability là một bài toán riêng downstream của ranker. Đây là điểm
định vị quan trọng nhất: paper không cố chứng minh ranker mới tốt nhất, mà hỏi
alarm tạo từ ranker có ý nghĩa vận hành nào.

### 2.3 Bốn câu hỏi nghiên cứu chính

1. Với chỉ \(k\) normal support, target-only conformal alarm có độ phân giải nhỏ
   nhất là bao nhiêu?
2. Khi normal test distribution bị thay đổi bởi corruption, p-value còn thể hiện
   false-alarm behavior như kỳ vọng hay không?
3. Có thể dùng normal data từ category khác để vận hành dưới target-only
   resolution floor mà không dùng target anomaly label không?
4. Cần bao nhiêu category độc lập để biến source-assisted threshold thành một
   certificate có ý nghĩa cho category mới?

---

## 3. Các khái niệm cần biết trước khi đọc phương pháp

### 3.1 Ranking score và decision threshold

Một anomaly score \(s(x)\) càng lớn thì mẫu càng bất thường. Score được dùng để
tính:

- **AUROC:** xác suất một anomaly ngẫu nhiên được xếp trên một normal ngẫu nhiên;
- **AP:** chất lượng ranking khi quan tâm precision–recall;
- **pixel AUROC/AU-PRO:** chất lượng localization vùng lỗi.

Các metric này chủ yếu đánh giá thứ tự. Chúng không tự tạo ra xác suất hoặc
false-alarm guarantee.

### 3.2 Các metric vận hành

Tại một threshold cố định:

- **FAR (false-alarm rate):** tỷ lệ normal bị alarm;
- **power/detection rate:** tỷ lệ anomaly được alarm;
- **precision:** trong các alarm, tỷ lệ thực sự là anomaly;
- **no-harm:** tỷ lệ cell mà phương pháp mới không làm xấu criterion đã định
  so với anchor/baseline.

Paper ưu tiên FAR, power và precision cho claim vận hành.

### 3.3 Calibration metric

Paper cũng báo cáo:

- ECE;
- Brier score;
- negative log-likelihood.

Nhưng ECE chỉ là secondary evidence. Đặc biệt, nếu dùng \(1-p\) của conformal
p-value như một probability-like score, ECE thay đổi mạnh theo anomaly prevalence.
Do đó, ECE tốt không tương đương với false-alarm control.

### 3.4 Conformal p-value trực giác

Ta có một tập score của normal calibration examples. Với test score \(s(x)\),
p-value đếm xem có bao nhiêu calibration score ít nhất lớn bằng test score:

\[
p(x)=\frac{1+\sum_{i=1}^{k}\mathbf 1\{r_i\ge s(x)\}}{k+1}.
\]

- \(p\) nhỏ: test sample cực đoan hơn normal reference, nên đáng alarm;
- \(p\) lớn: test sample không quá khác normal reference.

Nếu các score thỏa exchangeability thích hợp, alarm \(p\le\alpha\) có liên hệ
với false-alarm rate. Tuy nhiên construction LOIO cụ thể trong bài không hoàn
toàn exchangeable; paper công khai caveat này và audit empirically thay vì claim
một split-conformal guarantee không tồn tại.

### 3.5 “Certificate” trong paper nghĩa là gì?

Certificate không có nghĩa “model chắc chắn đúng trên mọi target”. Nó là một
upper confidence bound cho một risk được khai báo, dưới:

- một unit of analysis xác định;
- một source population xác định;
- independence/exchangeability assumptions xác định;
- family-wise error budget \(\delta\) xác định.

Paper phân biệt hai estimand:

1. **fixed-archive image risk:** trung bình trên mixture ảnh của archive hiện có;
2. **new-category mean risk:** kỳ vọng trên một category mới lấy từ
   meta-population category.

Image certificate không được đổi tên thành category certificate.

---

## 4. Kiến trúc tổng thể: ba tầng phải được tách biệt

### 4.1 Tầng A — low-storage anomaly ranker

Backbone là frozen DINOv2 ViT-S/14. Mỗi image được biểu diễn thành các patch
feature \(z_{ij}\in\mathbb R^d\). PCA được fit trên normal support patches. Với
support mean \(\mu\) và principal directions \(U\), residual của patch là:

\[
r(z)=\left\|(z-\mu)-UU^\top(z-\mu)\right\|_2.
\]

Residual lớn nghĩa là patch nằm xa normal subspace. Các patch residual tạo:

- anomaly map cho localization;
- image score \(s(x)\) bằng max hoặc top-fraction aggregation.

Hai protocol dùng aggregator hơi khác:

- clean accuracy/storage benchmark dùng patch maximum;
- conformal pipeline dùng mean của top 1% residual để làm smoothed maximum.

Ablation cho thấy các lựa chọn này nằm trong khoảng 0.01–0.02 AUROC so với lựa
chọn tốt nhất theo từng row.

**Ranh giới novelty:** DINOv2 feature, PCA residual và low-storage subspace
ranking đã có trong prior work, đặc biệt SubspaceAD. Paper không claim đây là
ranker mới hoặc ranking SOTA. Nó là substrate để nghiên cứu reliability.

### 4.2 Tầng B — target-only reliability routes

Paper so sánh nhiều route trên cùng ranker:

- scalar Platt;
- Vector Platt;
- Shift-Aware Platt;
- weighted Platt;
- temperature scaling;
- isotonic regression;
- histogram binning;
- LOIO conformal;
- weighted conformal.

Các calibrator chính không dùng real anomaly label. Chúng dùng:

- \(k\) support normal ảnh;
- số lượng synthetic anomaly bằng số normal;
- synthetic anomaly được tạo bằng thay 25% patch feature bằng perturbed support
  patch.

Vector Platt dùng descriptor:

\[
\phi(x)=
[s_{\rm pca}(x),s_{\rm head}(x),
|\widetilde{s}_{\rm pca}(x)-\widetilde{s}_{\rm head}(x)|].
\]

Synthetic-anomaly head là MLP \(384\to256\to1\), chỉ tham gia descriptor
calibration, không thay đổi raw ranking.

Shift-Aware Platt thêm năm descriptor của distribution shift: khoảng cách max và
mean đến support center, mean và standard deviation của patch residual, và
residual concentration ratio. Weighted variants dùng density-ratio estimate.

### 4.3 LOIO conformal route

Với \(k\ge2\), lần lượt bỏ support image \(x_i\), fit subspace trên \(k-1\) ảnh
còn lại và score \(x_i\):

\[
\mathcal R_{\rm LOIO}=
\{s_{-i}(x_i):i=1,\ldots,k\}.
\]

Sau đó test image được score bằng full-support model và conformalized theo
\(\mathcal R_{\rm LOIO}\). Paper báo \(1-p_{\rm LOIO}\) như một
probability-like reliability view, không gọi nó là supervised posterior.

**Caveat quan trọng:** calibration score dùng model fit trên \(k-1\) ảnh, còn
test score dùng model fit trên \(k\) ảnh. Vì vậy chúng không hoàn toàn
exchangeable. Construction là LOIO/cross-conformal approximation, không phải
split-conformal p-value với finite-sample validity trực tiếp. Paper:

- kiểm tra matched fold-specific scoring như một audit;
- kiểm tra empirical normal-p CDF trên discrete grid;
- không gọi kết quả đó là proof of validity.

### 4.4 Tầng C — SC3R source-assisted thresholding

Target-only p-value có grid quá thô khi \(k\) nhỏ. Trong một nhà máy nhiều
category, có thể có nhiều normal image của các source category khác. SC3R dùng
source normals để có nhiều reference score hơn và tạo threshold nhỏ hơn
\(1/(k+1)\).

Score của mỗi category được robust-normalize bằng median/MAD của LOIO support
residual của chính category đó. Việc này giúp so sánh score scale, nhưng không
chứng minh các category có cùng distribution.

Bốn routing mode:

- **matched-condition:** source view có cùng corruption condition với target;
- **clean-source:** luôn dùng clean source normals;
- **condition-agnostic:** lấy median qua condition view của cùng base image;
- **mismatched-condition:** negative control cố ý dùng condition không khớp.

Matched-condition cần condition metadata; đây là giả định triển khai, không phải
thông tin miễn phí.

---

## 5. Ba proposition và một corollary

### 5.1 Proposition 1 — attainable-alpha floor

Vì số calibration exceedance chỉ có thể là \(0,1,\ldots,k\), p-value chỉ thuộc:

\[
\left\{
\frac1{k+1},\frac2{k+1},\ldots,1
\right\}.
\]

Do đó, nếu \(\alpha<1/(k+1)\), alarm \(p\le\alpha\) luôn bằng zero.

Ví dụ:

- \(k=4\): p-value nhỏ nhất là \(1/5=0.20\);
- \(k=8\): p-value nhỏ nhất là \(1/9\approx0.111\).

Tại \(k=4,\alpha=0.05\), zero FAR không có nghĩa method kiểm soát tốt 5%; method
đơn giản là không thể alarm bất kỳ mẫu nào. Kết quả này là algebraic, không cần
exchangeability.

**Giá trị khoa học:** proposition tự nó đơn giản, nên paper không coi đây là
toàn bộ novelty. Nó xác định chính xác regime mà source assistance trở nên cần
thiết và ngăn cách diễn giải sai zero FAR.

### 5.2 Proposition 2 — conditional source certificate

Source category được chia **trước certification** thành ba tập rời nhau:

1. reference categories \(\mathcal R\): định nghĩa conformal reference;
2. proposal categories \(\mathcal P\): đề xuất tối đa \(M\) threshold dương;
3. certification categories \(\mathcal C\): chỉ đánh giá candidate, không tune.

Với \(A\) alpha level, family error \(\delta\), candidate \(\tau\), class loss
\(L_i(\tau)\in[0,1]\), category-level Hoeffding UCB là:

\[
U_H(\tau)=
\min\left\{
1,\bar L(\tau)+
\sqrt{\frac{\log(2AM/\delta)}{2n}}
\right\}.
\]

Image analysis dùng exact one-sided Clopper–Pearson bound cho Bernoulli alarm.
Factor \(2AM\) chia error budget qua:

- hai unit definition;
- \(A\) alpha level;
- \(M\) candidate.

SC3R chọn candidate lớn nhất có UCB không vượt \(\alpha\). Nếu không candidate
nào pass, \(\tau=0\), tức deterministic no-alarm fallback.

Dưới assumptions về independent certification units, union bound cho simultaneous
source-risk statement với probability ít nhất \(1-\delta\).

### 5.3 Proposition 3 — feasibility của category certificate

Vì empirical loss \(\bar L(\tau)\ge0\), ngay cả trong trường hợp tốt nhất
\(\bar L=0\), muốn \(U_H(\tau)\le\alpha\) cần:

\[
n\ge
\frac{\log(2AM/\delta)}{2\alpha^2}.
\]

Với frozen protocol \(A=3,\delta=0.05\):

| Số candidate \(M\) | \(\alpha=0.20\) | \(\alpha=0.10\) | \(\alpha=0.05\) |
|---:|---:|---:|---:|
| 1 | 60 | 240 | 958 |
| 5 | 80 | 320 | 1,280 |
| 20 | 98 | 390 | 1,557 |

Đây là **necessary**, không phải sufficient, condition. Empirical loss dương
chỉ làm yêu cầu lớn hơn.

Benchmark frozen split chỉ còn:

- 4 certification category cho MVTec-based jobs;
- 3 certification category cho VisA-within job.

Vì vậy, positive category-certified threshold là bất khả thi theo bound đã khai
báo, trước cả khi xem target outcome. Thêm seed, thêm corruption view hoặc thêm
ảnh trong cùng category không tăng \(n\); chúng không giải quyết thiếu independent
category.

### 5.4 Proposition 4 — cận dưới distribution-free khi mọi loss bằng zero

Để kiểm tra liệu thất bại trên có chỉ do Hoeffding quá lỏng hay không, paper xét
một cận trên tất định \(U_n\) có coverage \(1-\beta\) đồng đều cho mọi phân phối
loss iid trên \([0,1]\). Nếu quan sát \(n\) loss đều bằng zero thì bắt buộc:

\[
U_n(0,\ldots,0)\ge 1-\beta^{1/n}.
\]

Chứng minh dùng phản chứng trên subclass Bernoulli. Nếu bound trả về
\(u<1-\beta^{1/n}\), chọn \(q\) sao cho
\(u<q<1-\beta^{1/n}\). Dưới Bernoulli\((q)\), mẫu all-zero xuất hiện với xác
suất \((1-q)^n>\beta\); trên toàn bộ event này, \(U_n=u<q\), nên failure
probability vượt \(\beta\), trái với uniform coverage.

Do đó muốn \(U_n(0,\ldots,0)\le\alpha\) cần

\[
n\ge\frac{\log\beta}{\log(1-\alpha)}.
\]

Không phạt multiplicity (\(\beta=0.05\)) vẫn cần 14/29/59 category tại
\(\alpha=0.20/0.10/0.05\). Với frozen allocation thuận lợi nhất
\(\beta=0.05/(2\cdot3\cdot1)\), cần 22/46/94; Hoeffding cần 60/240/958.
Vì vậy 3–4 category là thiếu ngay cả trước khi bàn về độ lỏng của Hoeffding.

Phạm vi phải đọc đúng: mệnh đề chỉ áp dụng cho bound tất định, uniformly valid,
distribution-free, chỉ dùng iid bounded category losses. Mô hình parametric,
hierarchical, side information hoặc randomization nằm ngoài mệnh đề và cần
validity argument riêng.

### 5.5 Corollary — source certificate không tự động chuyển thành target guarantee

Target FAR chỉ được bound nếu có thêm một điều kiện như:

\[
P_{\rm target}(p\le\tau)
\le R_{\rm source}(\tau),
\]

hoặc target category exchangeable với certification-category meta-population.

Median/MAD normalization và matched-condition routing có thể làm giả định này
hợp lý hơn để kiểm tra, nhưng không chứng minh nó. Vì vậy:

- source certificate là conditional source statement;
- target result là empirical transfer stress test;
- paper không claim unconditional target-domain control.

---

## 6. Thiết kế thí nghiệm

### 6.1 Dataset

- **MVTec AD:** 15 industrial category, có pixel-level defect mask.
- **VisA:** 12 industrial category, dùng làm benchmark calibration/corruption
  quy mô đầy đủ.
- **MPDD:** 6 metal-part category, chỉ dùng cho external
  MVTec-to-MPDD strict stress test.

Within-MPDD category certification không được claim vì dataset quá ít category
để chia ba stage.

### 6.2 Few-shot setting và condition

- Clean ranking/storage và strict nested: \(k\in\{1,2,4,8\}\).
- Historical corruption/conformal tables: chủ yếu \(k\in\{4,8\}\).
- Condition gồm clean và bốn corruption:
  Gaussian noise, blur, brightness/contrast, JPEG.

### 6.3 Strict frozen grid

Strict nested run dùng:

- \(k\in\{1,2,4,8\}\);
- seed 0–4;
- \(\alpha\in\{0.05,0.10,0.20\}\);
- 5 condition;
- tối đa 120 evaluation image/cell;
- top-1% aggregation;
- PCA64;
- \(\delta=0.05\);
- tối đa 20 threshold candidate;
- 4 routing mode;
- 4 jobs: MVTec-within, VisA-within, MVTec-to-VisA,
  MVTec-to-MPDD.

Operational gate yêu cầu:

- category-certified threshold dương trong ít nhất 80% target cell;
- target FAR \(\le\alpha+0.02\);
- power dương;
- no-harm ít nhất 80%;
- simultaneous lower bound của power gain dương.

Zero threshold và failed cell đều được giữ; không xóa khỏi summary.

### 6.4 Data hierarchy và independence

Thứ bậc dữ liệu là:

`dataset → category → support seed → base image → corruption view`.

Các điểm sau không được xem là independent sample mới:

- nhiều corruption của cùng base image;
- nhiều seed reuse cùng image;
- image dùng chung source reference pool.

Đây là lý do category-level analysis có effective \(n\) rất nhỏ dù tổng số row
rất lớn.

### 6.5 Baseline và fairness

Ranking/accuracy:

- controlled DINOv2 nearest-neighbor memory bank;
- official AnomalyDINO reproduction;
- official/representative SubspaceAD như novelty guardrail;
- WinCLIP reported row, không coi community implementation là official.

Calibration:

- Platt family;
- temperature scaling;
- isotonic;
- histogram binning;
- LOIO conformal;
- weighted conformal.

Controlled NN không được gọi là official PatchCore/AnomalyDINO reproduction.
Official AnomalyDINO được chạy riêng theo released protocol. WinCLIP được ghi
“reported” vì không có official implementation; community reimplementation
thấp hơn reported khoảng 20 AUROC point nên không được dùng như audited official
baseline.

### 6.6 Reproducibility và integrity

Strict experiment chạy trên một NVIDIA RTX 5090 với PyTorch 2.12.1 và cached
DINOv2 patch feature fp32. Frozen scientific commit là
`e7f175990b02aa3cbdb7c92250d57c0272abef9d`; complete handoff commit là
`74fdfd00f3480f3bc5db42e29bc51ec0768ab881`.

Audit hiện tại xác nhận:

- 811/811 deliverable tồn tại;
- 811/811 SHA-256 checksum khớp;
- không có broken handoff symlink;
- MVTec: 1.500 view cell, 156.100 view row;
- VisA: 1.200 view cell, 144.000 view row;
- MPDD: 600 view cell, 45.800 view row;
- artifact audit reject duplicate cell, support–test overlap và missing support
  statistic;
- GPU preflight pass toàn bộ 98 test; local CPU reconstruction pass 98 test và
  skip một test phụ thuộc PyTorch trong lần audit mới nhất.

Handoff giữ per-image prediction, base-image identity, support manifest,
source-partition manifest, candidate table, bound, environment và checksum. Raw
dataset và large feature cache không nằm trong submission handoff.

---

## 7. Kết quả theo từng câu hỏi nghiên cứu

### 7.1 Ranker có đủ tốt và low-storage có thật không?

Official AnomalyDINO đứng đầu image AUROC trong clean table:

- MVTec: 0.965/0.976/0.980 tại \(k=1/4/8\);
- VisA: 0.857/0.912/0.926.

CRR/PCA64 không claim vượt AnomalyDINO. So với controlled DINOv2 NN, CRR có
ranking gần tương đương và compact hơn:

- CRR/PCA64 reference state: khoảng 0.472 MB/category;
- CRR/PCA128: khoảng 0.566 MB/category;
- controlled memory bank: khoảng 2.005 MB tại \(k=1\), saturate 6 MB tại
  \(k=4,8\).

Ví dụ MVTec \(k=4\):

- controlled NN AUROC 0.942;
- CRR 0.937;
- official AnomalyDINO 0.976.

VisA PCA128 tốt hơn PCA64 khoảng 0.011–0.016 AUROC nhưng vẫn dưới 0.6 MB.

**Diễn giải đúng:** low-storage ranker là một supporting substrate cạnh tranh,
không phải contribution ranking SOTA. Backbone DINOv2 dùng chung khoảng 84 MB
fp32 không được tính vào per-category state vì mọi method đều cần một bản chung.

State khoảng 0.472 MB/category gồm xấp xỉ:

- 0.094–0.098 MB cho PCA64 basis;
- khoảng 0.37 MB cho synthetic-anomaly head và calibrator.

Trên cached feature, subspace scoring khoảng 1.3 ms/image, trong khi controlled
nearest-neighbor bank khoảng 5–13 ms/image. Backbone forward vẫn chi phối
end-to-end latency và giống nhau giữa các method. LOIO cần fit \(k\) subspace
phụ khi setup, nhưng với \(k\le8\) và tối đa \(k\times1369\) support patch, phần
này dưới một giây/category trong protocol được báo cáo.

### 7.2 LOIO có cải thiện reliability metric không?

Trên full VisA corruption benchmark, ranking cố định:

- LOIO overall ECE 0.077;
- weighted conformal ECE 0.166;
- AUROC/AP giống nhau vì reliability route không đổi raw score.

Trên full MVTec conformal benchmark:

- LOIO overall ECE 0.0684;
- raw ranking AUROC 0.912;
- LOIO tốt hơn Vector/Shift-Aware Platt trong tám \(k\)-corruption cell được
  tóm tắt.

Trong descriptive per-cell comparison, LOIO thường tốt hơn standard calibrator,
đặc biệt ở \(k=4\). Ví dụ MVTec \(k=4\):

- LOIO ECE \(0.120\pm0.054\);
- isotonic \(0.222\pm0.088\);
- temperature \(0.240\pm0.104\);
- histogram \(0.229\pm0.099\).

Tuy nhiên tại \(k=8\), margin hẹp hơn:

- LOIO chỉ thắng isotonic trong 55% MVTec cell;
- trên VisA \(k=8\), so với Shift-Aware Platt, mean difference chỉ -0.011 và
  win fraction 51%.

Historical unadjusted significance value đã bị loại vì thiếu artifact để audit
một Holm-adjusted family. Vì vậy đây là descriptive/secondary evidence, không
phải confirmatory significance claim.

Các số “overall ECE” và “per-cell mean ECE” không được so trực tiếp như cùng một
estimator: overall result pool image theo full benchmark, còn scalar-calibrator
table tính ECE từng class–seed–corruption cell rồi lấy mean/std qua cell. Sự
khác nhau về weighting và aggregation giải thích vì sao full MVTec overall ECE
0.0684 nhưng LOIO per-cell mean ở \(k=4\) là 0.120.

Trong representative protocol-locked routing, fixed LOIO không dùng validation
label để chọn expert và giảm ECE so với Vector Platt:

- MVTec-to-VisA: 0.301 → 0.099;
- VisA-to-MVTec: 0.304 → 0.102;
- leave-one-category-out: 0.304 → 0.116;
- within split: 0.361 → 0.154.

No-harm là 100% trong bốn summary protocol này, nhưng đây vẫn là ECE result chứ
không phải target-control certificate.

### 7.3 Normal p-value có giữ behavior dưới corruption không?

Vì LOIO p-value discrete, paper không dùng continuous KS test với Uniform(0,1).
Thay vào đó, empirical CDF được so với ideal discrete-uniform reference tại từng
grid point và dependence được giữ theo class–seed cluster trong Monte Carlo
reference.

Kết quả:

- VisA \(k=4\): conservative;
- VisA \(k=8\): có xu hướng anti-conservative dưới corruption;
- MVTec \(k=4,8\): anti-conservative rõ dưới corruption.

Ví dụ mạnh nhất:

\[
\widehat F(0.2)=0.46
\]

cho Gaussian noise trên MVTec \(k=4\), so với reference 0.20. Nghĩa là tỷ lệ
normal có p-value ở dưới 0.2 cao hơn nhiều so với mức mong đợi.

Matched-LOIO audit không giải quyết trade-off: trên representative clean MVTec
\(k=4\), FAR tăng từ 0.17 lên 0.25 trong khi power gần như không đổi.

**Diễn giải đúng:** corruption-shift deviation được localize empirically; paper
không chứng minh corruption là nguyên nhân duy nhất hoặc LOIO có formal validity.

### 7.4 Attainable-alpha floor có xuất hiện trong vận hành không?

Đúng như Proposition 1:

- \(k=4\), mọi \(\alpha<0.20\): FAR = power = 0;
- \(k=8\), mọi \(\alpha<1/9\): FAR = power = 0.

Tại first attainable level \(\alpha=0.20\):

- VisA \(k=4\): pooled FAR 0.152, detection 0.599;
- MVTec \(k=4\): pooled FAR 0.411, detection 0.887.

Theo corruption:

- VisA \(k=4\): FAR khoảng 0.142–0.157, conservative;
- MVTec \(k=4\): FAR 0.306 blur, 0.313 brightness/contrast,
  0.463 Gaussian noise, 0.410 JPEG.

Do đó cùng một nominal \(\alpha=0.20\) có behavior rất khác trên hai benchmark.

Implementation audit còn phát hiện float32 có thể lưu \(1/5\) thành
0.20000000298; so sánh `p <= 0.2` không tolerance sẽ vô tình bỏ toàn bộ alarm
tại floor. Paper dùng tolerance nhỏ.

### 7.5 Strict nested SC3R có thành công không?

Không. Đây là kết quả âm trung tâm cần được review đúng.

Số aggregate gate cell:

\[
4\ {\rm jobs}\times
4\ {\rm routes}\times
4\ k\times
3\ \alpha\times
5\ {\rm conditions}
=960.
\]

Seed được tổng hợp bên trong gate analysis, không phải một factor độc lập trong
phép nhân 960. Kết quả:

- 0/960 operational gate pass;
- mọi category-certified target cell nhận \(\tau=0\);
- category nonzero-threshold rate = 0% cho cả bốn job.

| Source → target | Certification category/cell | Minimum category UCB |
|---|---:|---:|
| MVTec → MVTec | 4 | 0.950 |
| VisA → VisA | 3 | 1.000 |
| MVTec → VisA | 4 | 0.961 |
| MVTec → MPDD | 4 | 0.986 |

Tất cả UCB đều cao hơn alpha lớn nhất 0.20. Đây không phải GPU error, optimizer
failure hay model collapse. Proposition 3 dự báo trước rằng 3–4 category không
thể pass Hoeffding gate; Proposition 4 còn cho thấy ngay cả cận
distribution-free không phạt multiplicity cũng cần ít nhất 14 category.

Fixed-archive image certificate có positive threshold ở:

- MVTec-within: 36.7%;
- VisA-within: 60.4%;
- MVTec-to-VisA: 41.5%;
- MVTec-to-MPDD: 37.0%.

Nhưng đây là fixed archive mixture sensitivity, không phải new-category
certificate, và nhìn chung vẫn dưới operational criterion 80%.

### 7.6 Vậy historical SC3R dương có còn giá trị không?

Có, nhưng chỉ là empirical engineering evidence.

Historical MVTec \(k=4\), matched-condition SC3R:

- \(\alpha=0.05\): mean FAR 0.050, power 0.216;
- \(\alpha=0.10\): mean FAR 0.105, power 0.416;
- \(\alpha=0.20\): mean FAR 0.216;
- precision > 0.90;
- no-harm 89%/82%/89%.

Tại \(\alpha=0.05,0.10\), target-only anchor hoàn toàn im lặng, nên SC3R cho thấy
source pooling có thể tạo sub-floor operating point có ích. Tuy nhiên:

- source evidence dùng để chọn candidate cũng bị reuse để đánh giá;
- interval là pointwise, không simultaneous;
- các fold chia sẻ reference;
- không có independent certification stage.

Do đó không được gọi historical result là certificate.

Replication MVTec \(k=8\):

- pooled power 0.547/0.693 tại \(\alpha=0.05/0.10\);
- pooled FAR 0.052/0.121;
- empirical budget chỉ pass tại \(\alpha=0.05\).

Replication VisA \(k=4\):

- within-VisA FAR 0.051/0.095/0.192;
- power 0.144/0.351/0.637;
- no-harm giảm còn 78% tại \(\alpha=0.20\).

MVTec-to-VisA historical transfer:

- FAR 0.013/0.040/0.098;
- power 0.091/0.201/0.415.

Nó gợi ý conservative power–FAR trade-off trong một direction, không chứng minh
foreign source archive luôn fail-safe.

### 7.7 Tại sao không chỉ randomize p-value để vượt floor?

Smoothed/randomized conformal p-value có thể tạo p-value liên tục hơn bằng
uniform tie-break. Nó giải quyết discreteness nếu exchangeability phù hợp, nhưng
không sửa support–test mismatch.

Tại MVTec \(k=4\):

- randomized \(\alpha=0.05\): FAR 0.085, power 0.216;
- historical SC3R: FAR 0.049, power 0.216;
- randomized có thể lên tới 2.3 lần nominal dưới Gaussian noise.

Trên VisA, nơi target-only rule vốn conservative, randomization hợp lý hơn.

**Kết luận:** randomization xử lý resolution; historical source route còn có
dấu hiệu empirical mitigation của shift. Nhưng strict run cho thấy dấu hiệu đó
chưa được certify cho new category.

### 7.8 ECE prevalence sensitivity và abstention

Trên full VisA, LOIO ECE thay đổi:

- 0.404 tại 1% anomaly prevalence;
- 0.149 tại 50% prevalence.

Ranking không đổi nhưng ECE và thứ hạng LOIO-versus-weighted có thể đảo. Vì vậy
paper không dùng balanced-test ECE để claim deployment validity.

Entropy-based abstention:

- bỏ 20% mẫu bất định nhất làm remaining MVTec calibration error giảm
  0.068 → 0.030;
- VisA cải thiện nhẹ hơn: 0.077 → 0.075 tại 80% coverage, 0.066 tại 70%.

Đây là selective-operation diagnostic, không phải formal selective-risk guarantee.

### 7.9 Localization và adversarial fragility

Low-storage subspace detector cạnh tranh với controlled NN về localization:

- pixel AUROC CRR: 0.944/0.957/0.960 tại \(k=1/4/8\);
- AU-PRO: 0.820/0.862/0.876.

Nhưng adversarial diagnostic rất xấu:

- \(k=4,\epsilon=2/255\): image AUROC 0.937 → 0.158;
- \(k=8,\epsilon=2/255\): 0.945 → 0.175.

Tại \(\epsilon=8/255\), AUROC khoảng 0.446, tức drop không monotonic theo
\(\epsilon\). Điều này gợi ý attack-objective sensitivity. Paper dùng kết quả
này làm negative diagnostic và tuyệt đối không claim adversarial robustness.

---

## 8. Contribution thật của paper

### 8.1 Contribution trung tâm

1. **Exact finite-resolution diagnosis.** Paper formalize attainable-alpha floor
   và buộc operational interpretation đi theo attainable grid thay vì đọc zero
   FAR như một thành công.
2. **Shift-aware empirical validity audit.** Paper dùng discrete/cluster-aware
   diagnostics để chỉ ra direction của failure: conservative trên một số VisA
   setting nhưng anti-conservative trên corrupted MVTec.
3. **Strict nested formulation của source-assisted thresholding.** Reference,
   proposal và certification category được tách rời; candidate multiplicity và
   hai unit of analysis được khai báo.
4. **Category-certificate feasibility bound.** Paper định lượng số independent
   category tối thiểu và chứng minh vì sao benchmark hiện tại buộc strict gate
   trở thành vacuous.
5. **Honest negative result.** Paper giữ nguyên 0/960, zero fallback và phân biệt
   nó với historical empirical evidence, thay vì đổi estimand để cứu claim.

### 8.2 Contribution hỗ trợ

- decoupled ranking/reliability pipeline;
- fair label-free comparison với calibrator toolbox;
- low-storage accuracy/localization substrate;
- randomization baseline;
- prevalence sensitivity và risk–coverage diagnostics;
- cross-dataset and corruption stress tests;
- artifact lineage và fail-closed reproducibility audit.

### 8.3 Không phải contribution mới

- DINOv2 backbone;
- PCA/subspace residual ranking;
- Platt scaling, isotonic, histogram, temperature scaling;
- generic LOIO/conformal anomaly detection;
- weighted conformal;
- statement chung rằng calibration có thể degrade under shift.

Reviewer nên đánh giá novelty ở **cách finite-sample barriers, operational audit
và strict source-category certification được nối thành một câu chuyện**, không
ở từng ingredient riêng lẻ.

---

## 9. Claim boundary: paper được và không được nói gì

### 9.1 Có thể claim

- target-only p-value có exact resolution floor \(1/(k+1)\);
- corruption benchmark cho empirical conservative/anti-conservative behavior;
- LOIO thường có ECE thấp hơn các calibrator được test, nhưng đây là secondary,
  descriptive result;
- source pooling tạo useful historical sub-floor operating points trên các
  target đã đánh giá;
- strict category-level Hoeffding certificate là zero trong 960/960 gate cell;
- bound giải thích tại sao số category hiện tại không đủ;
- image-level fixed-archive và category-level estimand khác nhau;
- ranker compact và cạnh tranh với controlled NN, không phải accuracy SOTA.

### 9.2 Không thể claim

- LOIO construction có exact finite-sample target control;
- SC3R đã được certify cho target category mới;
- image certificate thay thế category certificate;
- MVTec-to-VisA/MPDD chứng minh transfer nói chung;
- robust normalization chứng minh source và target exchangeable;
- LOIO ECE tốt đồng nghĩa deployment calibration tốt;
- CRR vượt AnomalyDINO/SubspaceAD về ranking;
- CRR adversarially robust;
- historical pointwise interval là simultaneous confirmatory evidence;
- thêm image hoặc seed sẽ giải quyết shortage of categories.

---

## 10. Cách đọc kết quả âm `0/960`

Có ba cách hiểu sai phổ biến:

### Hiểu sai 1: “0/960 nghĩa là code/GPU hỏng”

Không đúng. GPU handoff có 811/811 deliverable, 811/811 SHA-256 match, artifact
audit pass trên MVTec, VisA và MPDD. Minimum UCB cao đúng theo width của bound
khi \(n=3\) hoặc 4.

### Hiểu sai 2: “0/960 chứng minh SC3R không có ích”

Quá mạnh. Nó chứng minh **strict category certificate theo protocol và bound
đã chọn** không thể chọn threshold dương với archive nhỏ như vậy. Historical
target results vẫn cho thấy engineering plausibility, nhưng không được nâng lên
thành guarantee.

### Hiểu sai 3: “Chỉ cần dùng image làm unit là cứu được”

Không đúng nếu claim là new-category generalization. Image unit trả lời risk trên
fixed image mixture và cho positive threshold trong 37–60% setting. Nó có thể
hữu ích cho archive cố định, nhưng không đo uncertainty do lấy một category mới.

### Ý nghĩa đúng

Kết quả âm làm lộ ra một protocol-design limit: khi statistical unit thực sự là
category, benchmark AD phổ biến có hàng chục category tổng cộng nhưng chỉ còn
3–4 category sau nested split, quá ít cho simultaneous small-\(\alpha\)
certification. Đây là một kết quả thiết kế thí nghiệm và giới hạn inference,
không phải một chiến thắng accuracy.

---

## 11. Điểm mạnh khoa học để reviewer cân nhắc

1. Bài phân tách ranking và operational reliability rõ ràng.
2. Exact floor ngăn một diễn giải sai rất phổ biến của zero alarm.
3. Paper tự audit exchangeability caveat của LOIO thay vì dùng từ “conformal”
   để ngầm claim validity.
4. Strict nested rerun sửa leakage/adaptive reuse của historical SC3R.
5. Image và category estimand được tách đúng.
6. Negative result được giữ nguyên dù làm claim yếu hơn.
7. Baseline được gắn nhãn official, controlled hoặc reported.
8. Reproducibility package giữ per-image prediction, base-image identity,
   support/partition manifest, candidate bound và checksum.
9. Bài nêu rõ adversarial failure, ECE prevalence sensitivity và transfer
   assumption.

---

## 12. Điểm yếu và câu hỏi reviewer nên đặt ra

### 12.1 Novelty

- Proposition 1 đơn giản và conformal discreteness đã được biết; novelty tổng thể
  có đủ mạnh khi kết hợp với strict SC3R feasibility result không?
- SC3R strict result âm có đóng góp phương pháp hay chủ yếu là protocol lesson?
- Paper có đang chứa quá nhiều supporting experiment làm loãng central story?

### 12.2 Formal validity

- LOIO asymmetry đã được thừa nhận đầy đủ chưa?
- Proposition 2 assumptions có phù hợp với cách data được lấy mẫu trong code?
- Hoeffding bound có quá lỏng so với risk structure thực tế không, và nếu dùng
  bound chặt hơn thì central conclusion còn giữ không?
- Factor \(2AM\) và candidate construction có khớp chính xác implementation?
- Category independence/meta-population có ý nghĩa thực tế nào trong factory?

### 12.3 Experimental design

- Historical và strict results có được phân biệt đủ nổi bật không?
- 80% operational gate có được pre-specified và có justification thực tế không?
- Matched-condition metadata có thực tế khi deployment không?
- Cross-dataset direction còn ít; paper đã giới hạn claim đủ chưa?
- Aggregator khác nhau giữa clean benchmark và conformal pipeline có gây
  confusion hoặc protocol sensitivity không?

### 12.4 Metrics

- Vì \(1-p\) không phải supervised posterior, ECE có nên xuất hiện nhiều như
  hiện tại không?
- Operational FAR/power có nên được ưu tiên hơn nữa trong abstract/results?
- Risk–coverage nên dùng calibration error hay selective FAR/power?

### 12.5 Baseline

- Controlled NN có đủ để đánh giá storage trade-off không?
- Official SubspaceAD/AnomalyDINO rows có cùng preprocessing/split đủ để so sánh
  trực tiếp không?
- WinCLIP reported row có nên ở main table nếu audit reproduction không khớp?

### 12.6 Presentation

- CRR và SC3R có quá nhiều route/acronym không?
- “source-validated” trong historical table có dễ bị hiểu nhầm là certified
  không?
- Kết quả âm có được đưa đủ sớm để tránh người đọc kỳ vọng một method thắng?

---

## 13. Reviewer checklist theo loại evidence

Reviewer có thể gắn từng statement vào một trong các nhãn:

- **P — proved:** Proposition 1, Propositions 3--4, union-bound statement dưới
  assumptions.
- **C — conditional:** source certificate và target-transfer corollary.
- **E — empirical:** ECE, FAR, power, transfer, robustness, storage.
- **H — hypothesis:** nguyên nhân Gaussian noise/JPEG làm heterogeneity tăng,
  hoặc tighter subspace khuếch đại mismatch.

Một claim chỉ hợp lệ khi ngôn từ khớp nhãn:

- P: “must”, “cannot”, “requires”;
- C: “under assumption…”, “conditional on…”;
- E: “observed”, “on evaluated benchmarks”, “suggests”;
- H: “plausible”, “may”, “not causally isolated”.

Nếu manuscript dùng ngôn ngữ mạnh hơn evidence label, đó là điểm cần yêu cầu sửa.

---

## 14. Hướng dẫn đọc các figure/table chính

### Figure 1 — pipeline

Kiểm tra ba lane:

- ranker không bị reliability layer thay đổi;
- target-only LOIO bị floor;
- SC3R chỉ chọn threshold nếu source certificate pass, nếu không trả zero.

### Figure reliability/ECE

Chỉ kết luận route nào có secondary calibration metric tốt hơn. Không suy ra
ranking gain hoặc false-alarm guarantee.

### Figure discrete CDF

Điểm trên diagonal nghĩa là empirical CDF lớn hơn ideal reference, tức có nhiều
p-value nhỏ hơn dự kiến và nguy cơ anti-conservative alarm. Inset chỉ zoom vùng
grid đầu tiên.

### Table clean efficiency

Phân biệt:

- official AnomalyDINO;
- controlled DINOv2 NN;
- reported WinCLIP;
- CRR/PCA64/PCA128.

Không so ECE với row không được audit.

### Table attainable alpha

Zero alarm dưới floor là structural silence, không phải reliability success.

### Table strict nested SC3R

Đọc category row và image row như hai estimand khác nhau. Category nonzero 0%
là strict conclusion; image nonzero 36.7–60.4% chỉ là sensitivity.

### Historical SC3R tables

Đọc như engineering evidence trên evaluated targets. Caption phải giữ cảnh báo
selection và assessment không independent.

### Feasibility table

Đây là design calculation từ Propositions 3--4, không phải số đo GPU.

---

## 15. Một cách trình bày miệng trong 5 phút

1. Few-shot DINOv2 detector có thể rank tốt nhưng score threshold không tự có
   operational meaning.
2. CRR giữ ranker PCA gọn nhẹ và audit reliability bằng label-free calibrator và
   LOIO p-value.
3. Với \(k\) score, p-value nhỏ nhất là \(1/(k+1)\); \(k=4\) không thể alarm ở
   5% hay 10%.
4. Khi lên first attainable level, VisA conservative nhưng corrupted MVTec
   anti-conservative, nên “conformal” không đồng nghĩa construction này valid
   dưới shift.
5. SC3R dùng other-category normals để có sub-floor thresholds. Historical
   result có power và gần nominal FAR, nhưng reuse source evidence.
6. Strict rerun tách reference/proposal/certification category. Nó trả zero
   threshold ở 960/960 gate.
7. Đây là hệ quả tất yếu của sample size: ngay cả cận distribution-free không
   phạt multiplicity cần 14 category tại \(\alpha=0.20\); frozen allocation cần
   22 và Hoeffding cần 60, nhưng chỉ có 3–4.
8. Vì vậy contribution là reliability audit và feasibility boundary, không phải
   certified target alarm hay AUROC SOTA.

---

## 16. Các câu hỏi nhanh để kiểm tra người đọc đã hiểu đúng bài

1. Vì sao zero FAR tại \(\alpha=0.05,k=4\) không phải kết quả tốt?
2. Tại sao AUROC không thay đổi giữa Vector Platt và LOIO?
3. Vì sao LOIO construction không có exact split-conformal guarantee?
4. Historical SC3R khác strict nested SC3R ở independence nào?
5. Vì sao 1000 source image không thay thế được 60 source category?
6. Image certificate và category certificate nhắm vào hai population nào?
7. Điều kiện nào cần thêm để source certificate chuyển thành target guarantee?
8. `0/960` phủ những factor nào và tại sao không nhân thêm seed?
9. Vì sao randomized p-value vượt floor nhưng vẫn anti-conservative trên MVTec?
10. Paper có claim ranking SOTA hoặc adversarial robustness không?

Nếu người review trả lời được mười câu này, họ đã nắm đúng central logic của bài.

---

## 17. Glossary

- **AD:** anomaly detection.
- **Support set:** vài normal image dùng để fit detector cho target category.
- **Target category:** category cần triển khai/test.
- **Source category:** category khác, cung cấp normal archive cho SC3R.
- **Anomaly score:** raw score dùng để ranking.
- **Reliability view:** calibrated probability-like score hoặc conformal p-value.
- **Nonconformity:** mức test sample khác normal reference.
- **LOIO:** leave one support image out để tạo normal calibration residual.
- **FAR:** tỷ lệ normal bị alarm.
- **Power:** tỷ lệ anomaly được alarm.
- **Resolution floor:** p-value nhỏ nhất \(1/(k+1)\).
- **Attainable alpha:** alpha level thực sự nằm trên p-value grid.
- **SC3R:** Source-Conditioned Cross-Category Reliability Routing.
- **Reference/proposal/certification split:** nested source split chống adaptive
  reuse.
- **UCB:** upper confidence bound của risk.
- **Zero fallback:** \(\tau=0\), không alarm khi không candidate nào được certify.
- **Fixed-archive estimand:** risk trên image mixture cố định.
- **New-category estimand:** expected risk cho category mới từ meta-population.
- **Exchangeability:** điều kiện đối xứng phân phối cần cho nhiều conformal claim.
- **No-harm:** tỷ lệ evaluation cell không bị xấu theo criterion khai báo.
- **Prevalence:** tỷ lệ anomaly trong evaluation/deployment population.

---

## 18. Kết luận dành cho reviewer

Paper nên được đánh giá như một công trình về **reliability limits và protocol
design cho few-shot learned detector**, không phải một paper thuần túy đề xuất
detector mới. Điểm mạnh nhất là bài không che giấu việc strict certificate thất
bại: nó biến failure thành một finite-category feasibility result có công thức,
audit và claim boundary rõ. Điểm cần reviewer quyết định là liệu sự kết hợp giữa
resolution floor, empirical shift audit, historical source-routing evidence và
strict negative certification có tạo thành contribution đủ sâu và đủ tập trung
cho Neurocomputing hay không. Bất kỳ đánh giá nào cho rằng paper đã chứng minh
target-domain control, hoặc ngược lại cho rằng `0/960` làm toàn bộ empirical
SC3R vô nghĩa, đều chưa phản ánh đúng nội dung hiện tại của bài.
