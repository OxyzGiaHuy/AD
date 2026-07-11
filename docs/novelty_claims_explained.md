# Giải Thích Novelty Và Claim Hiện Tại

Tài liệu này dành cho người có nền tảng AI cơ bản nhưng chưa quen với bài toán
few-shot industrial anomaly detection. Mục tiêu là đi theo flow: bài toán là
gì, method hiện tại làm gì, kết quả đang cho phép claim gì, phần nào đã có
người làm, và cần chạy thêm experiment nào để paper mạnh hơn.

## 1. Bối Cảnh Bài Toán

**Industrial anomaly detection** là bài toán phát hiện lỗi bất thường trong ảnh
công nghiệp, ví dụ chai bị nứt, viên thuốc bị xước, dây cáp bị lỗi, bề mặt gỗ
có vết lạ. Trong sản xuất thật, ảnh normal thường dễ thu thập hơn ảnh lỗi. Ảnh
lỗi vừa hiếm, vừa đa dạng, và nhiều loại lỗi chưa từng xuất hiện trong dữ liệu
train.

**Few-shot anomaly detection** là phiên bản khó hơn: với mỗi category, ta chỉ có
rất ít ảnh normal, thường là 1 đến 8 ảnh. Mục tiêu là dùng vài ảnh normal đó để
phát hiện ảnh test có anomaly hay không, và nếu có thì vùng lỗi nằm ở đâu.

Hai benchmark chính trong project này:

- **MVTec AD**: benchmark công nghiệp phổ biến, có nhiều object/texture class,
  có label image-level và mask lỗi cho localization.
- **VisA**: benchmark công nghiệp khác, thường dùng để kiểm tra khả năng
  generalization ngoài MVTec.

Vì anomaly hiếm và đa dạng, cách train supervised thông thường không phù hợp.
Do đó các phương pháp hiện đại thường dùng feature mạnh từ foundation model như
DINOv2, rồi so sánh ảnh test với vài ảnh normal.

## 2. Flow Method Hiện Tại

### Frozen DINOv2

**DINOv2** là một vision foundation model đã được pretrain trên lượng dữ liệu
lớn. Trong project này, DINOv2 được **frozen**, nghĩa là không cập nhật trọng số
backbone trong quá trình train/evaluate. Ta chỉ dùng nó để trích xuất feature.

Lý do dùng frozen backbone:

- giảm compute;
- tránh overfit trong few-shot;
- dễ so sánh công bằng với các baseline như PatchCore, AnomalyDINO, SubspaceAD.

### Patch Feature

Ảnh được chia thành nhiều patch. Mỗi patch đi qua DINOv2 và nhận một vector đặc
trưng. Nếu ảnh có một vùng lỗi nhỏ, patch ở vùng đó thường có feature khác với
normal patches.

Nói ngắn gọn:

- image -> nhiều patch;
- mỗi patch -> một vector feature;
- anomaly score có thể tính ở patch-level rồi tổng hợp thành image-level score.

### Memory Bank

**Memory bank** là cách lưu feature của các ảnh normal support. Khi có ảnh test,
ta so sánh patch feature của ảnh test với các patch feature normal đã lưu. Nếu
patch test xa nearest normal patch, patch đó có khả năng là anomaly.

PatchCore và AnomalyDINO thuộc hướng này. Ưu điểm là mạnh về AUROC. Nhược điểm
là inference phải giữ và so sánh với nhiều reference features, nên storage và
chi phí nearest-neighbor có thể cao hơn.

### PCA / Subspace Residual

**Subspace** có thể hiểu là một không gian con biểu diễn các biến thiên bình
thường của normal patches. Giả định là normal patches không nằm rải rác tùy ý
trong feature space, mà thường nằm quanh một cấu trúc có chiều thấp hơn.

**PCA** học không gian con này từ normal patch features. Khi có patch test:

1. chiếu patch feature vào normal subspace;
2. reconstruct lại patch từ subspace;
3. đo residual, tức khoảng cách giữa feature gốc và feature reconstruct.

Residual cao nghĩa là patch không được normal subspace giải thích tốt, nên có
khả năng là anomaly.

Trong project này, **raw anomaly score** chính của `calib_subspace_head` là PCA
residual/subspace score. Điểm này quan trọng vì ablation cho thấy PCA residual
giữ ranking AUROC tốt hơn head-only.

### HeadPCA

`HeadPCA` là biến thể có một MLP head nhỏ học từ pseudo/synthetic anomalies.
Synthetic anomaly là các feature bị tạo nhiễu hoặc biến đổi để giả lập lỗi khi
không có nhiều ảnh lỗi thật.

Ban đầu ta thử trộn:

```text
final_score = alpha * head_score + (1 - alpha) * PCA_score
```

Ablation cho thấy nếu tăng alpha quá nhiều, tức dựa nhiều vào head_score, AUROC
giảm, đặc biệt ở k=1. Vì vậy head không nên thay thế PCA residual cho ranking.

### CalibSubspaceHead

`CalibSubspaceHead` là hướng hiện tại nên dùng làm main method. Ý tưởng chính là
**decoupling**, tức tách hai vai trò:

- `raw_anomaly_score`: dùng PCA/subspace residual để xếp hạng ảnh anomaly.
- `calibrated_probability`: dùng calibrator để biến score thành xác suất dễ
  diễn giải hơn.
- `uncertainty`: dùng entropy từ probability để đo độ bất định.

Calibrator nhận vector:

```text
[pca_score, head_score, disagreement]
```

Trong đó `disagreement` đo mức lệch giữa PCA score và head score sau chuẩn hóa.
Nếu hai nguồn tín hiệu không đồng ý, model có thể bất định hơn.

## 3. Calibration Trong Bài Này Nghĩa Là Gì?

Calibration không nhất thiết làm ranking tốt hơn. Ranking tốt được đo bằng AUROC
hoặc AP. Calibration trả lời câu hỏi khác: xác suất model đưa ra có đáng tin
không?

Ví dụ, nếu model nói 100 ảnh đều có xác suất anomaly khoảng 0.8, thì trong một
model calibrated tốt, khoảng 80 ảnh trong nhóm đó nên thật sự là anomaly.

Các thuật ngữ chính:

- **Raw score**: điểm anomaly gốc, thường chỉ có ý nghĩa tương đối. Score cao
  hơn nghĩa là bất thường hơn, nhưng score 3.0 không tự nhiên có nghĩa là xác
  suất 80%.
- **Calibrated probability**: xác suất anomaly sau khi hiệu chỉnh, nằm trong
  khoảng 0 đến 1.
- **ECE**: Expected Calibration Error. Metric đo chênh lệch giữa confidence dự
  đoán và tỉ lệ đúng thực tế theo các bin xác suất. ECE thấp hơn là tốt hơn.
- **Brier score**: sai số bình phương giữa probability dự đoán và label thật.
- **NLL**: negative log-likelihood, phạt mạnh các dự đoán quá tự tin nhưng sai.
- **Platt scaling**: học một logistic regression đơn giản để biến raw score
  thành probability.
- **Vector Platt**: giống Platt scaling, nhưng input là nhiều feature thay vì
  một raw score. Trong project này input là `[pca_score, head_score,
  disagreement]`.
- **Entropy**: đo độ bất định của posterior probability. Với bài toán binary,
  probability gần 0.5 thì entropy cao, probability gần 0 hoặc 1 thì entropy
  thấp.

Điểm cần nhớ: calibration tốt giúp hệ thống đáng tin hơn trong ngữ cảnh sản
xuất. Một detector có AUROC cao nhưng probability không calibrated có thể gây
khó khi đặt threshold, cảnh báo rủi ro, hoặc so sánh confidence giữa các class.

## 4. Claim Hiện Tại Sau Khi Chạy Experiment

Sau khi chạy benchmark hiện tại, claim cần thận trọng hơn idea ban đầu.

Không nên claim:

- thắng AUROC toàn diện trên MVTec;
- SOTA trên mọi k-shot/class;
- adversarially robust;
- first calibration/adversarial benchmark.

Claim chính nên dùng:

1. **Competitive AUROC với storage thấp hơn memory-bank.**  
   Trên MVTec, `calib_subspace_head` gần PatchCore/AnomalyDINO nhưng dùng storage
   nhỏ hơn rõ rệt. Memory-bank baselines cần lưu nhiều reference features hơn.

2. **Calibration tốt hơn PatchCore/AnomalyDINO ở k lớn.**  
   MVTec k8 ECE của PatchCore/AnomalyDINO khoảng `0.6933`, trong khi
   `calib_subspace_head` khoảng `0.1538`.

3. **VisA ủng hộ AUROC của method hiện tại.**  
   Trên VisA, `calib_subspace_head` vượt PatchCore/AnomalyDINO trong benchmark
   hiện tại ở k1, k2, k4, k8.

4. **Decoupling là cần thiết.**  
   Ablation cho thấy PCA/subspace residual nên làm ranking score, còn head và
   calibrator nên làm probability/uncertainty. Head-only có calibration tốt hơn
   nhưng làm AUROC giảm, nhất là k=1.

5. **Benchmark robustness/calibration/efficiency thống nhất.**  
   Project đã có clean benchmark, corruption robustness, FGSM surrogate,
   calibration metrics, storage/latency, và ablation.

Claim phải viết cẩn thận:

- FGSM `epsilon=8/255` làm AUROC giảm rất mạnh, khoảng 50% relative drop. Vì vậy
  không được nói method robust với adversarial attack. Nên nói project
  **quantify adversarial fragility** và phân tích reliability/uncertainty dưới
  perturbation.

## 5. Verify Novelty: Phần Nào Đã Có Người Làm?

### AnomalyDINO

AnomalyDINO đã làm DINOv2 cho few-shot anomaly detection theo hướng patch
similarity/memory bank. Method này training-free và có cả image-level anomaly
prediction lẫn pixel-level anomaly segmentation.

Vì vậy ta không được claim:

- DINOv2 few-shot anomaly detection là mới;
- patch similarity/memory bank với frozen DINOv2 là mới;
- image-level/pixel-level anomaly map từ DINOv2 patch features là mới.

Link: https://arxiv.org/abs/2405.14529

### SubspaceAD

SubspaceAD đã làm frozen DINOv2 patch features + PCA/subspace modeling. Method
này fit PCA trên normal features và dùng reconstruction residual để detect
anomaly. Đây là overlap rất mạnh với phần PCA residual của project.

Vì vậy ta không được claim:

- frozen DINOv2 + PCA residual là mới;
- training-free subspace anomaly detection là mới;
- bỏ memory bank bằng subspace residual là mới.

Link: https://arxiv.org/abs/2602.23013

### Khan & Krawczyk 2025

Khan & Krawczyk đã nghiên cứu robustness và uncertainty cho DINOv2-based
few-shot anomaly detection. Họ dùng FGSM, ECE, Platt scaling, predictive entropy
và chỉ ra raw anomaly scores poorly calibrated.

Vì vậy ta không được claim:

- first calibration benchmark cho DINOv2 few-shot AD;
- first adversarial robustness benchmark cho DINOv2 few-shot AD;
- Platt scaling cho anomaly score là mới.

Link: https://arxiv.org/abs/2510.13643

### Novelty Còn Lại

Novelty còn lại nên được định vị hẹp nhưng rõ:

- **Decoupled Calibrated Subspace Head**: tách ranking và calibration thay vì
  trộn trực tiếp score.
- **Vector calibrator** dùng `[subspace_score, head_score, disagreement]`, thay
  vì chỉ Platt scaling một raw score.
- **Synthetic-anomaly head** không thay thế subspace ranking, mà cung cấp tín
  hiệu phụ cho calibrator.
- **Unified empirical story**: cùng một protocol đo AUROC/AP, calibration,
  storage/latency, corruption, FGSM fragility, và ablation trên MVTec/VisA.

Novelty sẽ chắc hơn nếu thêm:

- calibration ablation đầy đủ: raw, scalar Platt, isotonic, vector Platt;
- MVTec -> VisA transfer calibration;
- pixel-AUROC/PRO và qualitative heatmaps;
- official SubspaceAD comparison.

## 6. Claim Ban Đầu So Với Claim Hiện Tại

Claim ban đầu:

> Trainable head/adapter over frozen DINOv2 beats memory-bank methods at equal
> or better few-shot AUROC while being cheaper, calibrated, and robust.

Claim hiện tại nên sửa thành:

> A calibrated subspace head over frozen DINOv2 approaches memory-bank AUROC on
> MVTec, improves AUROC over PatchCore/AnomalyDINO on VisA in our benchmark,
> greatly reduces reference storage, improves calibration, and exposes
> robustness limitations under corruption and FGSM-style perturbations.

Lý do phải đổi:

- MVTec chưa thắng PatchCore/AnomalyDINO toàn diện.
- PCA residual đã overlap với SubspaceAD.
- Calibration, ECE, Platt scaling và FGSM đã overlap với Khan & Krawczyk 2025.
- Kết quả thực nghiệm hiện tại ủng hộ câu chuyện calibration/efficiency hơn là
  pure AUROC SOTA.

## 7. Experiment Cần Thêm Để Bảo Vệ Novelty

### P0: Rất Nên Làm Ngay

- **Render heatmap figure**: tạo ảnh gốc, GT mask, heatmap, overlay,
  uncertainty overlay. Paper cần qualitative figure, hiện mới có
  `patch_scores.npy`.
- **Pixel-AUROC/PRO**: cần để so với AnomalyDINO/SubspaceAD ở localization.
- **Calibration ablation**: so raw score, scalar Platt, isotonic, vector Platt.
  Đây là experiment quan trọng nhất để prove vector calibrator thật sự đóng góp.

### P1: Nên Làm Để Paper Mạnh

- **MVTec -> VisA transfer calibration**: fit/tune calibrator trên MVTec, sang
  VisA chỉ dùng k normal support cho PCA. Đây là claim còn khá mới nếu làm
  nghiêm.
- **VisA corruption robustness**: hiện robustness chủ yếu đã đầy đủ trên MVTec.
- **FGSM sweep**: chạy `{2/255, 4/255, 8/255}` thay vì chỉ `8/255`.
- **Entropy separation**: kiểm tra entropy có giúp flag corrupted/adversarial
  samples không.

### P2: Nếu Còn Compute Và Thời Gian

- **Official SubspaceAD comparison**: rất quan trọng nếu reviewer nghi method là
  SubspaceAD + calibration.
- **LoRA/adapter**: chỉ đưa vào paper nếu có gain rõ; hiện chưa nên là claim
  chính.
- **End-to-end runtime audit**: tách cached-feature latency và full
  image-to-DINOv2 latency.

## 8. Một Câu Chốt Cho Paper Story

Paper nên được kể như sau:

> Memory-bank DINOv2 methods mạnh nhưng tốn reference storage và raw scores khó
> calibrated. Subspace residual đơn giản và rẻ nhưng chưa đủ câu chuyện
> reliability. Chúng tôi giữ subspace residual làm ranking score, thêm head nhỏ
> chỉ để tạo tín hiệu calibration, rồi dùng vector Platt để xuất probability và
> uncertainty. Kết quả cho thấy method cạnh tranh AUROC, rẻ hơn memory-bank, tốt
> hơn calibration, và benchmark chỉ ra cả điểm mạnh lẫn điểm yếu robustness.
