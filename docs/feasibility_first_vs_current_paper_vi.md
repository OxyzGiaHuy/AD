# So sánh hướng paper hiện tại và hướng feasibility-first

**Mục đích tài liệu.** Tài liệu này là bản phân tích nội bộ để quyết định có nên tái định vị paper từ một bài bắt đầu bằng CRESS sang một bài bắt đầu bằng giới hạn khả thi của việc chứng nhận threshold trong few-shot anomaly detection hay không. Nội dung tổng hợp bản thảo hiện tại, kết quả strict CRESS `0/960`, trao đổi trước đây về rủi ro acceptance, và đề xuất mới từ advisor. Đây không phải nội dung để chép nguyên văn vào manuscript.

**Kết luận ngắn.** Nên chuyển sang hướng feasibility-first, nhưng không nên dùng nguyên trạng mọi cách diễn đạt trong đề xuất. Hướng mới mạnh hơn vì biến `0/960` từ một kết quả dễ bị đọc như method failure thành một phép kiểm tra thực nghiệm của giới hạn category count. Tuy nhiên, paper phải nói rõ rằng `0.463` là empirical FAR của một cell đã xác định, `14/29/59` là optimistic multiplicity-free lower limits, image-unit và category-unit là hai estimand khác nhau, và target transfer vẫn cần dominance hoặc category exchangeability. Nếu thiếu các giới hạn này, framing mới sẽ hấp dẫn hơn nhưng kém chính xác hơn bản hiện tại.

---

## 1. Hai identity cạnh tranh của paper

### 1.1. Identity hiện tại: CRESS-first reliability framework

Paper hiện được nhận diện qua title:

> CRESS for Auditing Few-Shot Anomaly Reliability: Resolution Floors and Cross-Category Certification Feasibility

Mạch lập luận hiện tại có thể tóm tắt như sau:

1. Frozen foundation features tạo anomaly ranking tốt nhưng threshold không nhất thiết đáng tin cậy.
2. Target-only LOIO tạo p-value không cần target anomaly labels, nhưng có resolution floor `1/(k+1)` và có thể mất validity dưới shift.
3. CRESS mượn source categories, chia chúng thành Reference, Proposal và Certification để đề xuất và kiểm tra threshold.
4. Strict category certificate trả về `tau*=0` trên toàn bộ 960 gate cells.
5. Proposition 3 và Proposition 4 giải thích rằng kết quả âm đến từ số independent certification categories quá ít.
6. Image-unit certificate đôi khi trả về threshold dương, nhưng nó chỉ chứng nhận risk trên fixed archive mixture, không phải new-category risk.

Identity này trung thực hơn nhiều so với phiên bản method-first cũ, vì title đã có từ “auditing” và “feasibility”. Dù vậy, CRESS vẫn đứng ở đầu title và chiếm vị trí tâm lý của proposed method. Reviewer vì thế có thể đặt câu hỏi đầu tiên là: “CRESS cải thiện gì?”, thay vì: “Paper đã phát hiện giới hạn gì?”.

### 1.2. Identity đề xuất: feasibility-first reliability study

Hướng mới đặt câu hỏi trung tâm là:

> Cần bao nhiêu bằng chứng nguồn, và phải đếm bằng chứng theo đơn vị nào, để chứng nhận threshold cho một category mới?

Mạch lập luận được đảo thành:

1. Một target-only rule tại nominal `alpha=0.20` đạt empirical FAR `0.463` trên Gaussian-corrupted MVTec ở `k=4`.
2. Tăng `k` chỉ cải thiện resolution hữu hạn và không tự khôi phục exchangeability dưới shift.
3. Mượn source data mở ra operating points mịn hơn, nhưng phát sinh câu hỏi: images hay independent categories mới là đơn vị chứng nhận phù hợp?
4. Feasibility calculus trả lời rằng trong trường hợp distribution-free lạc quan nhất, zero-loss certification vẫn cần ít nhất `14/29/59` independent categories tại `alpha=0.20/0.10/0.05`.
5. Protocol thực tế cần nhiều category hơn do multiplicity và Hoeffding rule.
6. CRESS là protocol dùng để tách estimand và kiểm tra boundary đó; `0/960` xác nhận boundary đang binding.
7. Cùng một source archive có thể lớn khi đếm theo image nhưng quá nhỏ khi claim liên quan đến một category mới.

Identity này chuyển contribution từ “một method tạo threshold” sang “một study-design and reliability-certification result”. Đây là identity phù hợp hơn với evidence hiện có.

---

## 2. Vì sao kết quả 0/960 là rủi ro trong framing hiện tại

Strict category-level CRESS có các sự kiện thực tế sau:

- Mỗi VisA cell chỉ có ba certification categories.
- Mỗi MVTec và transfer cell chỉ có bốn certification categories.
- Tất cả category-certified target cells nhận `tau*=0`.
- Không gate configuration nào đạt yêu cầu 80% nonzero-threshold rate.
- Minimum observed candidate UCB là 0.950 trên MVTec, 1.000 trên VisA, 0.961 cho MVTec-to-VisA, và 0.986 cho MVTec-to-MPDD.
- Mức alpha lớn nhất chỉ là 0.20.

Nếu CRESS được bán như một successful reliability method, reviewer có thể kết luận:

1. proposed procedure không tạo được operating threshold hữu dụng;
2. chưa có positive strict result cho target-category reliability;
3. source certificate không tự động chuyển thành target guarantee;
4. main ranker là inherited DINOv2 PCA residual, không phải ranking novelty;
5. các thành phần Hoeffding, union bound và conformal rank đều là công cụ đã có.

Điều cần đặc biệt tránh là nói “CRESS thất bại trong 960 independent trials”. 960 cells là tích của bốn jobs, bốn routing modes, bốn giá trị `k`, ba mức alpha và năm conditions. Các cells chia sẻ cùng structural category-count obstruction và nhiều cells không độc lập thống kê. Con số 960 chỉ thể hiện boundary giữ nguyên trên toàn frozen audit grid.

Framing đúng là:

> The structural infeasibility predicted by the category-count analysis binds throughout the frozen 960-cell audit grid.

Theo cách này, `tau*=0` là output fail-closed đúng của protocol khi evidence không đủ, không phải bằng chứng rằng GPU hoặc optimizer chạy sai.

---

## 3. So sánh trực tiếp hai hướng

| Khía cạnh | Paper hiện tại | Hướng feasibility-first | Đánh giá |
| --- | --- | --- | --- |
| Câu hỏi mở đầu | Làm sao audit reliability và dùng source categories qua CRESS? | Bao nhiêu source evidence là đủ, và phải đếm theo unit nào? | Hướng mới sắc và dễ nhớ hơn. |
| Headline empirical result | Resolution floor, shift audit và `0/960` xuất hiện tương đối muộn | Empirical FAR 0.463 xuất hiện ngay đầu | Nên đổi, nhưng phải ghi đủ dataset/corruption/k/alpha. |
| Main object | CRESS framework/procedure | Feasibility boundary; CRESS là instrument kiểm tra | Phù hợp hơn với strict evidence. |
| Vai trò `0/960` | Main negative result của CRESS | Empirical confirmation rằng predicted boundary binds | Hướng mới giảm rủi ro “method does not work”. |
| Vai trò Proposition 4 | Giải thích sau kết quả âm | Contribution đầu tiên: study-design calculus | Nên nâng, nhưng không quảng bá thành deep theorem. |
| Image versus category | Caveat sau strict result | Trục chính về estimand | Nên nâng thành central insight. |
| Ranking/storage | Mở đầu Results | Supporting substrate đặt sau primary results | Nên chuyển xuống dưới. |
| Pipeline | Figure 1 | Figure 2 | Nên đổi nếu feasibility plot đủ rõ. |
| Title | CRESS đứng đầu | Giới hạn category certification đứng đầu | Nên đổi. |
| Reviewer expectation | Positive method performance | Correct diagnosis, bound và study-design implication | Hướng mới khớp evidence hơn. |
| Rủi ro overclaim | CRESS bị hiểu là deployable target-control method | Bound bị hiểu là áp dụng cho mọi certification method | Hướng mới vẫn cần qualifier “distribution-free”. |

---

## 4. Phân tích headline FAR 0.463

### 4.1. Con số này thực sự nói gì

Trong Table `tab:false-alarm-control`, tại:

- dataset: MVTec;
- condition: Gaussian noise;
- `k=4`;
- nominal `alpha=0.20`;

empirical FAR là 0.463. Detection rate tương ứng là 0.879 và precision là 0.816. FAR 0.463 lớn hơn nominal level theo hệ số `0.463/0.20 = 2.315`.

Đây là một headline tốt vì nó chuyển vấn đề calibration từ khái niệm trừu tượng thành operational failure dễ hiểu. Tuy nhiên, nó không phải:

- FAR trung bình của MVTec;
- true population FAR;
- bằng chứng rằng Gaussian noise luôn tạo FAR 0.463 ngoài benchmark;
- một guarantee về mọi detector hoặc mọi corruption severity.

MVTec aggregate FAR trung bình bốn corruption tại `k=4` là 0.373. Vì thế abstract phải gọi 0.463 là “the largest observed empirical FAR” hoặc mô tả đầy đủ cell.

### 4.2. Cách viết nên dùng

> At nominal level `alpha=0.20`, target-only LOIO reaches an empirical FAR of 0.463 on Gaussian-corrupted MVTec at `k=4`, more than twice the nominal level.

Không nên dùng “actual FAR”, “true FAR” hoặc viết trống điều kiện.

### 4.3. Evidence nên bổ sung để bảo vệ headline

Không nhất thiết cần chạy GPU lại, nhưng nên kiểm tra từ artifact hiện có:

1. severity Gaussian noise đã được frozen hoặc prespecified;
2. định nghĩa pooling theo category, seed và image được nêu rõ;
3. 0.463 không do float comparison bug;
4. kết quả không bị một hoặc hai category cực đoan chi phối hoàn toàn;
5. nếu có thể, báo clustered uncertainty hoặc category-level distribution;
6. gọi corruption là controlled synthetic shift, không thay thế real production shift.

Nếu các kiểm tra này chưa đủ artifact, paper vẫn có thể dùng 0.463 nhưng phải giảm giọng điệu và ghi rõ nó là benchmark observation.

---

## 5. Ba tầng của feasibility calculus

Đây là phần quan trọng nhất cần trình bày nhất quán. Không được trộn ba tầng sau.

### 5.1. Tầng 1: optimistic distribution-free lower limit

Proposition 4 xét một deterministic upper confidence bound `U_n` có uniform coverage `1-beta` cho mean của iid losses trong `[0,1]`. Với all-zero observations:

```text
U_n(0,...,0) >= 1 - beta^(1/n).
```

Để `U_n <= alpha` có thể xảy ra, cần:

```text
n >= log(beta) / log(1-alpha).
```

Với `beta=0.05`, không multiplicity:

| alpha | Minimum independent categories |
| ---: | ---: |
| 0.20 | 14 |
| 0.10 | 29 |
| 0.05 | 59 |

Đây là impossibility-style lower limit trong lớp procedure đã phát biểu. Nó không nói rằng 14 categories chắc chắn đủ để một practical method hoạt động; nó chỉ nói rằng dưới 14 categories, ngay cả trường hợp all-zero và bound tối ưu theo nghĩa này cũng không thể đạt 0.20.

### 5.2. Tầng 2: family-adjusted distribution-free floor của frozen protocol

Frozen protocol phân bổ confidence theo:

```text
beta = delta / (2 A M),  with A=3.
```

Ngay cả với `M=1`, requirements tăng thành:

| alpha | Family-adjusted DF lower limit |
| ---: | ---: |
| 0.20 | 22 |
| 0.10 | 46 |
| 0.05 | 94 |

Với `M=5` và `M=20`, chúng còn cao hơn. Đây vẫn là lower limit, không phải requirement của riêng Hoeffding.

### 5.3. Tầng 3: declared Hoeffding rule

Proposition 3 cho category-level Hoeffding rule:

```text
n >= log(2 A M / delta) / (2 alpha^2).
```

Với `M=1`, requirements là 60, 240 và 958. Với nhiều candidates hơn, chúng lên tới 98, 390 và 1,557 tại `M=20`.

### 5.4. Cách dùng ba tầng trong paper

- Abstract: dùng `14/29/59`, nhưng gọi rõ là optimistic multiplicity-free distribution-free lower limits; thêm một câu rằng frozen family allocation và implemented Hoeffding rule cần nhiều hơn.
- Introduction: giải thích ba tầng bằng một đoạn ngắn hoặc dẫn Table 1.
- Method/Theory: định nghĩa đầy đủ assumptions, beta allocation và proofs.
- Figure 1: trực quan hóa curves và crossings.
- Results: dùng số categories hiện có là 3 hoặc 4 để giải thích vì sao strict gate fail-closed.
- Conclusion: không rút gọn thành “few-shot certification always requires at least 14 categories”; claim chỉ đúng với phạm vi bound đã phát biểu và `alpha=0.20`, `beta=0.05`.

---

## 6. Image-unit và category-unit: contribution mạnh nhất nếu viết đúng

### 6.1. Image-unit certificate trả lời câu hỏi gì

Image-unit block có từ 72 đến 191 image units per cell. Minimum UCB nằm khoảng 0.039 đến 0.048. Positive thresholds xuất hiện trong:

- 36.7% MVTec cells;
- 60.4% VisA cells;
- 41.5% MVTec-to-VisA cells;
- 37.0% MVTec-to-MPDD cells.

Estimand của nó là false-alarm risk trên fixed source archive mixture được quan sát. Nó có thể hữu ích nếu deployment population chính là archive/view mixture đó và dependence assumptions được xử lý đúng.

### 6.2. Category-unit certificate trả lời câu hỏi gì

Category-unit block dùng mỗi category làm một statistical unit để hướng tới source meta-population hoặc new-category risk. Chỉ có ba hoặc bốn units, nên không đủ cho nonvacuous distribution-free certificate ở các alpha đang xét.

### 6.3. Điều tuyệt đối không được viết

- Không được nói image certificate “gần chứng minh” new-category control.
- Không được coi corruption copies hoặc support seeds là independent categories.
- Không được nói 3–4 categories tạo ra 37–60% positive image certificates; positive result đến từ 72–191 image units và một estimand khác.
- Không được thay category table bằng image table rồi giữ nguyên target-category claim.

### 6.4. Câu trung tâm đề xuất

> The same source archive is statistically large when counted in images but insufficient when the deployment claim concerns a new category.

Hoặc:

> Images can support a fixed-archive certificate; independent categories are required for a distribution-free new-category certificate.

Câu đầu cân bằng hơn vì câu thứ hai có thể bị đọc quá tuyệt đối nếu bỏ qualifier distribution-free.

---

## 7. Nội dung có thể giữ nguyên hoặc tái sử dụng gần như hoàn toàn

### 7.1. Data, frozen protocols và empirical artifacts

Không cần bỏ hoặc chạy lại toàn bộ experiment. Có thể giữ:

- MVTec, VisA và MPDD dataset setup;
- support sizes `k in {1,2,4,8}`;
- năm seeds;
- clean, Gaussian noise, blur, brightness/contrast và JPEG conditions;
- source-to-target jobs;
- frozen 0.50/0.25/0.25 R/P/C category split;
- per-image predictions, manifests và audit lineage;
- strict `0/960` outputs;
- image-unit sensitivity outputs;
- clean ranking, storage và localization results;
- historical analyses, với nhãn non-independent diagnostics.

Reframing không được thay số liệu hoặc âm thầm đổi denominator.

### 7.2. Core mathematical content

Có thể giữ:

- định nghĩa raw score và PCA residual scorer;
- target-only LOIO p-value;
- proof finite grid `1/(k+1)`;
- R/P/C construction;
- category loss và mean category loss;
- Proposition 2 về source certificate;
- Proposition 3 về Hoeffding feasibility;
- Proposition 4 và proof Bernoulli counterexample;
- Corollary về conditional target transfer.

Thay đổi chủ yếu là thứ tự, prominence và tên gọi, không phải thay theorem statement để phù hợp narrative.

### 7.3. Scientific caveats bắt buộc giữ

- DINOv2 PCA residual là inherited ranking substrate.
- LOIO/full-support asymmetry tồn tại.
- Corruption shift có thể phá exchangeability.
- ECE là secondary và prevalence-sensitive.
- Fixed-archive image certificate không phải new-category certificate.
- Historical CRESS không phải certified evidence.
- Source-domain control chỉ chuyển thành target control dưới dominance hoặc category exchangeability.
- Synthetic corruptions không đại diện đầy đủ production shifts.

### 7.4. Pipeline hiện tại

Pipeline mới vẫn hữu ích và nên giữ làm Figure 2. Nó mô tả:

- frozen scoring/localization substrate;
- target-only LOIO route;
- CRESS source-side R/P/C threshold certification;
- conditional target application.

Chỉ cần sửa caption và cross-reference theo figure numbering mới; không cần vẽ lại logic từ đầu trừ khi đổi typography/layout.

---

## 8. Nội dung phải thay đổi đáng kể

### 8.1. Title

Title hiện tại vẫn tạo CRESS-first expectation. Nên đổi sang limit-first và có qualifier.

Khuyến nghị chính:

> How Many Categories Are Enough? Distribution-Free Certification Limits for Few-Shot Anomaly Thresholds

Phương án khác:

> Counting Categories for Transferable Reliability: Distribution-Free Feasibility Limits in Few-Shot Anomaly Detection

Không khuyến nghị dùng nguyên trạng “Counting Categories, Not Images” nếu không giải thích ngay rằng images vẫn có giá trị cho fixed-archive estimand.

### 8.2. Abstract

Abstract cần viết lại gần như toàn bộ theo thứ tự:

1. operational failure `0.463` với đầy đủ điều kiện;
2. research question về evidence unit và category count;
3. target-only floor trong một câu ngắn;
4. feasibility result `14/29/59` với qualifier;
5. CRESS là R/P/C protocol dùng kiểm tra boundary;
6. `0/960` là boundary confirmation, không phải 960 independent failures;
7. image versus category estimand contrast;
8. practical takeaway về study design và fail-closed reporting.

Không nên bắt đầu bằng “we introduce CRESS”. Không nên để PCA storage chiếm nhiều từ trong abstract mới.

### 8.3. Introduction

Hai hoặc ba đoạn đầu cần đổi mạnh:

- mở bằng threshold reliability failure, không mở dài bằng tổng quan AD;
- dùng 0.463 làm concrete observation;
- nêu hai lối thoát: tăng target support và mượn source evidence;
- chỉ ra mỗi lối thoát tạo một giới hạn riêng;
- phát biểu research question theo statistical unit;
- trả lời sớm bằng 14/29/59, rồi qualify bằng 22/46/94 và Hoeffding requirement;
- giới thiệu CRESS sau feasibility question.

Phần background về DINOv2, PatchCore, AnomalyDINO và SubspaceAD có thể giữ nhưng rút ngắn hoặc chuyển một phần sang Related Work.

### 8.4. Contributions

Rút từ bốn contribution xuống ba:

1. feasibility calculus;
2. corruption-shift audit;
3. CRESS estimand-separating protocol và frozen boundary test.

Storage, localization, calibrator comparisons và adversarial fragility không còn là contributions độc lập. Chúng là supporting diagnostics hoặc scope delimiters.

### 8.5. Figure hierarchy

- New Figure 1: category-count feasibility plot.
- Existing pipeline: Figure 2.
- Empirical p-value CDF figure: giữ sau shift table hoặc kết hợp tùy page budget.

Figure 1 nên là figure “5-second takeaway”, không phải một đồ thị chứa toàn bộ `M=1,5,20` và ba alpha thành quá nhiều đường.

Thiết kế đề xuất:

- x-axis: number of independent certification categories `n`;
- y-axis: minimum all-zero UCB hoặc smallest certifiable risk level;
- optimistic DF curve `1-0.05^(1/n)`;
- frozen family-adjusted DF curve;
- declared Hoeffding floor, clipped at 1;
- horizontal lines tại alpha 0.20, 0.10 và 0.05;
- vertical lines tại n=3 và n=4;
- crossings được annotate;
- multiplicity range M=1 đến 20 thể hiện bằng band hoặc Table 1, không vẽ tất cả thành spaghetti plot.

### 8.6. Method

Method không nên đảo hoàn toàn theo Results vì vẫn phải định nghĩa score trước threshold. Cấu trúc hợp lý:

1. Problem setup and estimands.
2. Frozen scorer as inherited substrate.
3. Target-only LOIO reliability.
4. Remark: finite resolution `1/(k+1)`.
5. Source score normalization/view construction.
6. CRESS R/P/C threshold selection.
7. Certificate scope and feasibility calculus.
8. Conditional target-transfer boundary.

Proposition 1 về attainable floor có thể hạ thành Remark. Proposition numbering còn lại cần cập nhật cẩn thận trên toàn paper.

### 8.7. Results

Results hiện mở bằng ranking/storage. Hướng mới cần đảo thành:

1. shift-induced false-alarm inflation;
2. category-count feasibility;
3. strict CRESS boundary test và image/category contrast;
4. ranking and storage substrate;
5. secondary calibration/deployment diagnostics.

Điều này không có nghĩa bỏ ranking. Nó chỉ đặt supporting substrate sau research question chính.

### 8.8. Discussion, Limitations và Conclusion

Limitations hiện đã khá đúng và có thể tái sử dụng, nhưng cần đổi thứ tự để bắt đầu bằng claim scope của distribution-free bound và synthetic shift.

Conclusion nên kết thúc bằng practical design rules:

- report attainable operating levels;
- test normal FAR under declared shifts;
- choose certification unit before observing outcomes;
- count independent categories for a new-category claim;
- use zero fallback when evidence is insufficient;
- collect category-rich archives hoặc đưa ra explicit model assumptions nếu muốn certificate mạnh hơn.

Không nên kết luận rằng mọi future method đều bị chặn bởi 14 categories. Parametric, hierarchical, randomized hoặc side-information procedures nằm ngoài theorem hiện tại và phải có validity argument riêng.

---

## 9. Các table và figure: giữ, chuyển hay gộp

| Artifact hiện tại | Quyết định đề xuất | Lý do |
| --- | --- | --- |
| Pipeline figure | Giữ, chuyển thành Figure 2 | Vẫn cần để hiểu scorer, LOIO và CRESS. |
| New feasibility plot | Tạo thành Figure 1 | Gánh central claim và giúp hiểu 3/4 versus required n. |
| `tab_certificate_feasibility` | Giữ main text, đặt sớm thành Table 1 | Là design calculator, không phải appendix detail. |
| `tab_false_alarm_control` | Giữ main text | Chứa headline 0.463 và condition breakdown. |
| `tab_attainable_alpha` | Giữ hoặc nén | Floor là supporting mechanism; có thể rút nếu page pressure. |
| `tab_strict_nested_sc3r` | Giữ một table gọn | Kết hợp category/image estimands và min UCB. |
| `tab_pooled_source_conformal` | Giữ secondary hoặc appendix | Uncertified empirical reference, không phải central guarantee. |
| `tab_clean_efficiency` | Giữ nhưng chuyển sau primary results | Chứng minh ranker substrate hợp lý, không phải novelty. |
| Calibration tables | Appendix, tóm tắt bằng text | ECE là secondary. |
| Historical CRESS tables | Appendix | Selection/certification không độc lập. |
| Protocol-routing/pixel/fragility tables | Appendix | Scope diagnostics. |
| Prior-work-positioning table | Xóa và chuyển insight sang Related Work prose | Không phải empirical table và chiếm page budget. |

Nếu numbering hiện tại khác vì LaTeX float placement, quyết định nên dựa trên logical order và references, không dựa vào số table đang nhìn trên PDF cũ.

---

## 10. Claim matrix sau khi đổi framing

| Claim dự kiến | Loại evidence | Có thể claim? | Qualification bắt buộc |
| --- | --- | --- | --- |
| Target-only finite-rank p-values có minimum `1/(k+1)` | Proved | Có | Với p-value form đã định nghĩa. |
| Empirical FAR đạt 0.463 | Empirical | Có | MVTec, Gaussian noise, k=4, alpha=.20, pooling rõ ràng. |
| Shift làm target-only rule anti-conservative | Empirical | Có | Trên evaluated corruption benchmark; không universal. |
| 14/29/59 là category requirements | Proved lower limits | Có | Beta=.05, no multiplicity, all-zero, deterministic uniformly valid distribution-free bounds. |
| Frozen protocol cần 22/46/94 hoặc nhiều hơn | Proved lower limits | Có | Allocation beta=delta/(2AM), A=3, M specified. |
| Hoeffding cần 60/240/958 ở M=1 | Algebraic | Có | Declared rule, all-zero best case; higher M requires more. |
| CRESS chứng nhận target-category FAR unconditional | Không được support | Không | Chỉ source-domain; target transfer conditional. |
| Category gate fail-closed trong 960 cells | Empirical | Có | 960 configurations không phải independent trials. |
| Image certificates thành công 37–60% | Empirical | Có | Positive-threshold fraction; fixed-archive estimand, không new-category guarantee. |
| DINOv2 PCA residual là novel ranker | Prior art | Không | Chỉ supporting substrate. |
| Paper đạt SOTA anomaly ranking | Không đủ evidence | Không | External protocols khác nhau. |

---

## 11. Rủi ro mới phát sinh khi chuyển hướng

### 11.1. Reviewer cho rằng theorem quá đơn giản

Đây là phản biện hợp lý. Proposition 4 dùng một Bernoulli construction ngắn; mathematical depth riêng lẻ không đủ để gánh Q1 novelty. Cách phòng vệ không phải phóng đại theorem, mà chứng minh giá trị của combination:

- một operational failure được quan sát;
- một exact feasibility calculus;
- một protocol tách estimand;
- một frozen empirical validation across datasets/transfers/conditions;
- một practical study-design rule.

### 11.2. Reviewer cho rằng 0.463 là cherry-picked synthetic worst case

Phòng vệ bằng frozen grid, báo cả bốn corruptions và VisA, mô tả 0.463 là maximum observed, và giữ aggregate 0.373 trong text. Nếu artifact cho phép, thêm category-clustered uncertainty hoặc distribution.

### 11.3. Reviewer cho rằng “count categories, not images” quá tuyệt đối

Giải quyết bằng estimand language: images đúng cho fixed archive; categories cần cho new-category distribution-free claim. Title nên tránh phủ định hoàn toàn vai trò của images.

### 11.4. Reviewer cho rằng CRESS không còn là contribution

CRESS vẫn là contribution thứ ba nếu được định nghĩa là protocol tách R/P/C roles, statistical units và fail-closed selection. Không gọi nó là SOTA detector hoặc deployable target guarantee.

### 11.5. Reviewer hỏi tại sao không dùng hierarchical hoặc parametric model

Paper cần nói rõ đó là con đường hợp lý cho future work, nhưng các method đó mua statistical efficiency bằng assumptions. Chúng không bác bỏ distribution-free lower limit vì nằm ngoài lớp procedure của Proposition 4.

### 11.6. Reviewer hỏi new-category transfer có được chứng minh không

Không. Proposition 2 chứng nhận source estimand. Target guarantee cần Corollary dominance/exchangeability assumption. Empirical target tests là stress tests của assumption, không phải proof unconditional transfer.

---

## 12. Đánh giá khả năng nâng paper lên mức Neurocomputing Q1

### Hướng hiện tại

Ưu điểm:

- method pipeline rõ;
- audit trung thực;
- proofs và limitations đã được bổ sung;
- có lượng empirical artifacts lớn.

Nhược điểm:

- CRESS-first framing tạo kỳ vọng positive method result;
- `0/960` dễ trở thành lý do reject;
- ranking/storage mở Results nhưng không phải novelty;
- central insight image versus category chưa nổi bật;
- abstract đang dành quá nhiều không gian cho framework mechanics.

### Hướng feasibility-first

Ưu điểm:

- research question cụ thể và có answer định lượng;
- negative result trở thành boundary validation;
- có một Figure 1 dễ nhớ;
- thống nhất theory và experiment;
- practical takeaway rõ cho experimental design;
- tránh cạnh tranh trực tiếp với SOTA detector papers.

Nhược điểm:

- novelty phụ thuộc vào việc reviewer đánh giá cao audit/design contribution;
- theorem đơn giản nếu bị tách khỏi empirical context;
- synthetic shift chưa đại diện factory drift;
- không có positive new-category certificate;
- title/abstract quá mạnh có thể tạo overclaim mới.

### Phán quyết

Hướng feasibility-first có xác suất tạo một paper coherent và defensible cao hơn. Nó không tự động bảo đảm acceptance, nhưng giảm mismatch lớn nhất giữa claim và evidence. Để có chất lượng Q1, bản sửa phải được thực hiện như một tái cấu trúc logic toàn bài, không chỉ đổi title và đưa 0.463 lên abstract.

---

## 13. Bản đồ giữ lại, tái định vị và viết lại

### Giữ nguyên về nội dung khoa học

- raw experimental numbers;
- frozen split và protocol definitions;
- mathematical statements và proofs, sau khi re-audit notation;
- LOIO and CRESS mechanics;
- source/target distinction;
- limitations về transfer và dependence;
- appendix evidence.

### Tái định vị nhưng không thay nội dung

- pipeline Figure 1 thành Figure 2;
- ranking/storage từ Results đầu xuống supporting section;
- target-only floor từ Proposition thành Remark;
- CRESS từ headline method thành protocol kiểm tra feasibility;
- 0/960 từ “negative main result” thành “boundary confirmation”;
- image-unit result từ caveat thành đối trọng estimand, vẫn không nâng claim.

### Viết lại đáng kể

- title và short title;
- abstract;
- ba đến năm đoạn đầu Introduction;
- contribution list;
- roadmap cuối Introduction;
- transitions trong Method;
- toàn bộ thứ tự Results và opening sentences;
- Discussion/Limitations ordering;
- Conclusion;
- captions/cross-references sau khi đổi figure/table order;
- cover letter và highlights sau cùng.

### Tạo mới

- Figure 1 feasibility plot và source script;
- một đoạn định nghĩa rõ “evidence unit” và “estimand”;
- một bảng hoặc callout phân biệt optimistic DF, frozen DF và Hoeffding requirements;
- nếu artifacts đủ, category-level distribution/uncertainty supporting FAR 0.463.

---

## 14. Plan thực hiện thay đổi

Plan dưới đây cố ý có các checkpoint trước khi sửa lời văn lớn, nhằm tránh tạo một narrative đẹp nhưng sai số liệu.

### Phase 0 — Freeze evidence và lập claim ledger

1. Lưu snapshot hoặc commit hiện trạng trước reframing.
2. Không sửa raw outputs và không chạy lại experiment chỉ để làm số đẹp hơn.
3. Lập một claim ledger cho các số: 0.463, 0.373, 14/29/59, 22/46/94, 60/240/958, min UCB, 0/960 và 36.7–60.4%.
4. Ghi cho mỗi số: artifact nguồn, denominator, pooling unit, independence assumption và manuscript location.
5. Xác nhận 960 là number of configurations, không dùng như independent sample count.

**Checkpoint:** mọi headline number truy ngược được tới table/artifact và có đúng statistical unit.

### Phase 1 — Re-audit theory

1. Kiểm tra lại Proposition 2, 3, 4 và Corollary line by line.
2. Kiểm tra ceiling/rounding cho toàn Table 1.
3. Phân biệt rõ beta, delta, A và M.
4. Kiểm tra bound có clipped ở 1 hay không trong plot và table.
5. Chốt theorem scope: deterministic, uniformly valid, distribution-free, iid bounded category losses.
6. Hạ finite p-value floor thành Remark nếu không làm đứt numbering/cross-reference.

**Checkpoint:** một statistical reviewer không thể hiểu 14/29/59 là đủ cho frozen CRESS hoặc là universal cho mọi model-based procedure.

### Phase 2 — Thiết kế Figure 1 feasibility plot

1. Viết script tái lập curve từ formulas, không hard-code crossings.
2. Chọn trục x là independent category count và trục y là best-case all-zero UCB.
3. Vẽ optimistic DF, frozen family-adjusted DF và declared Hoeffding layers.
4. Đặt horizontal alpha lines và vertical n=3/4 lines.
5. Dùng shaded infeasible region nhưng không tạo vùng mâu thuẫn giữa nhiều alpha.
6. Đưa M sensitivity chi tiết vào Table 1 hoặc shaded band.
7. Export vector PDF và kiểm tra ở kích thước một cột và hai cột.

**Checkpoint:** người đọc nhìn Figure 1 trong năm giây hiểu rằng n=3/4 nằm rất xa mức cần thiết, nhưng vẫn thấy rõ 14/29/59 chỉ là optimistic floor.

### Phase 3 — Chốt identity và title

1. Chọn title limit-first có từ “distribution-free” hoặc qualifier tương đương.
2. Chốt một câu central question.
3. Chốt một câu central answer.
4. Chốt một câu image-versus-category takeaway.
5. Chốt vai trò CRESS là protocol, không phải ranking model.

**Checkpoint:** title, central question và evidence trả lời cùng một vấn đề.

### Phase 4 — Viết lại Abstract và Introduction

1. Abstract mở bằng 0.463 với đầy đủ condition.
2. Đặt research question ngay sau operational failure.
3. Nêu 14/29/59 cùng qualifier.
4. Nêu strict 0/960 như confirmation rằng boundary binds.
5. Nêu image-unit positive rates nhưng tách estimand.
6. Viết lại Introduction theo problem → options → evidence-unit question → answer → CRESS validation.
7. Rút contributions còn ba.
8. Kiểm tra abstract word limit của Neurocomputing.

**Checkpoint:** không còn câu nào khiến reviewer kỳ vọng CRESS phải là SOTA thresholding method có positive strict output.

### Phase 5 — Tái cấu trúc Method

1. Thêm explicit estimand/unit setup sớm.
2. Giữ scorer như inherited substrate.
3. Giữ LOIO trước CRESS theo dependency logic.
4. Hạ floor thành Remark.
5. Giữ đầy đủ R/P/C flow, source archive và view selection.
6. Đưa feasibility calculus thành kết thúc tự nhiên của certificate definition.
7. Đặt target-transfer boundary ngay sau source certificate.
8. Chuyển pipeline thành Figure 2 và sửa toàn bộ references/caption.

**Checkpoint:** Method vẫn có thể được implement chỉ từ mô tả, dù Results đã đổi thứ tự.

### Phase 6 — Tái cấu trúc Results

1. Mở bằng shift audit và 0.463.
2. Trình bày attainable floor ngắn như supporting context.
3. Đưa Figure 1 và Table 1 vào feasibility section.
4. Trình bày strict category versus fixed-archive image results cùng nhau.
5. Giải thích min UCB 0.950–1.000 so với alpha max 0.20.
6. Đưa ranking/storage xuống supporting section.
7. Gom calibrators, historical CRESS, localization, routing và fragility thành secondary analyses.
8. Chuyển tables không central xuống Appendix; bỏ prior-positioning table và nhập insight vào prose.

**Checkpoint:** ba section đầu của Results lần lượt trả lời “problem có thật không?”, “bao nhiêu evidence là đủ?”, và “frozen CRESS audit có khớp dự báo không?”.

### Phase 7 — Sửa Discussion, Limitations và Conclusion

1. Discussion diễn giải statistical unit, không chỉ lặp numbers.
2. Limitations nêu synthetic shift, iid category assumption, deterministic DF scope và conditional transfer.
3. Conclusion dùng present perfect như style đã chọn và kết thúc bằng study-design rules.
4. Không gọi image certificate là partial new-category certificate.
5. Không nói thêm GPU seeds hoặc corruption copies giải quyết category shortage.

**Checkpoint:** kết luận hữu ích nhưng không vượt quá theorem hoặc experiment scope.

### Phase 8 — Consistency and integrity audit

1. Dò toàn manuscript cho “CRESS”, “certify”, “guarantee”, “control”, “target”, “source”, “960”, “independent”, “image” và “category”.
2. Kiểm tra mọi usage thống nhất với estimand.
3. Kiểm tra numbering propositions, equations, figures, tables và appendices.
4. Biên dịch LaTeX nhiều vòng; sửa undefined references, overflow và float order.
5. So lại captions với text để không cắt mất interpretation.
6. Kiểm tra abstract, introduction, results, limitations và conclusion nói cùng một claim hierarchy.
7. Không sửa bibliography ngoài phạm vi tác giả cho phép.

**Checkpoint:** một reviewer không thể trích hai câu ở hai section khác nhau để chứng minh paper tự mâu thuẫn về source versus target guarantee.

### Phase 9 — Submission-oriented adversarial review

Thực hiện ít nhất ba mock-review lenses:

1. **AD reviewer:** ranking novelty ở đâu, corruption có realistic không?
2. **Statistical reviewer:** theorem scope, iid units, multiplicity và target transfer có đúng không?
3. **Neurocomputing reviewer:** contribution có đủ rộng và có practical value ngoài một negative result không?

Mỗi objection phải được xử lý bằng một trong ba cách: thêm evidence, thu hẹp claim, hoặc thừa nhận limitation. Không thêm language mạnh hơn chỉ để làm abstract hấp dẫn.

**Final checkpoint:** paper được nhận diện là một reliability-feasibility contribution có empirical validation, không phải một failed CRESS detector và cũng không phải một universal impossibility theorem.

---

## 15. Quyết định đề xuất

Nên thông qua hướng feasibility-first với bốn điều kiện không thương lượng:

1. `0.463` luôn được gọi là empirical conditional observation, không phải true/general FAR.
2. `14/29/59` luôn được định danh là optimistic multiplicity-free distribution-free lower limits; frozen and Hoeffding requirements phải xuất hiện đủ gần.
3. Image-unit và category-unit được trình bày là hai estimand khác nhau, không phải hai mức strength của cùng một certificate.
4. CRESS giữ vai trò protocol tách evidence và fail closed; target guarantee vẫn conditional.

Nếu giữ bốn điều kiện này, hướng mới vừa sắc hơn về narrative, vừa trung thực hơn với evidence, và có khả năng thuyết phục reviewer Neurocomputing cao hơn bản CRESS-first hiện tại.
