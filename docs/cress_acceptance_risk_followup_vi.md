# Memo: CRESS 0/960 và rủi ro khi nộp Neurocomputing

**Trạng thái:** Tạm hoãn thảo luận cho đến khi hoàn tất pipeline figure.

**Mục đích:** Ghi lại trung thực các vấn đề cần đánh giá lại trước khi chốt framing, title và submission package. File này là ghi chú nội bộ, không phải nội dung manuscript.

## 1. Kết quả cần đối diện trực tiếp

- Trong strict category-level audit, CRESS trả về threshold fail-closed
  \(\tau^\star=0\) trên toàn bộ 960 gate cells.
- Đây không phải lỗi GPU hoặc lỗi optimization. Với ba hoặc bốn certification
  categories, family-adjusted Hoeffding category-risk UCB không thể xuống tới
  các mức \(\alpha\) được kiểm tra.
- Proposition 4 cho thấy vấn đề không chỉ nằm ở độ lỏng của Hoeffding: ngay cả
  một deterministic, uniformly valid, distribution-free 95% upper bound không
  multiplicity cũng cần ít nhất 14 all-zero categories để đạt
  \(\alpha=0.20\).
- 960 cells không phải 960 thí nghiệm độc lập. Nhiều cells cùng chịu một
  structural category-count obstruction. Con số 960 chỉ xác nhận kết quả trên
  toàn frozen grid, không được dùng để thổi phồng lượng independent evidence.

## 2. Rủi ro acceptance chính

Nếu paper được trình bày như một **new method that improves target reliability**,
reviewer có thể phản đối rằng:

1. CRESS không tạo được một category-certified operating point dương nào.
2. Chưa có positive strict result chứng minh practical target utility.
3. Source-domain certificate chỉ chuyển thành target guarantee khi có thêm
   source-risk dominance hoặc category-exchangeability assumption.
4. DINOv2 PCA residual ranker là prior art, không phải ranking novelty.
5. Các statistical primitives như Hoeffding, union bound và conformal ranks là
   established tools; novelty phải nằm ở formulation, feasibility analysis và
   audit discipline.

Title hiện tại đặt CRESS ở vị trí method-first, nên có nguy cơ tạo kỳ vọng rằng
CRESS phải hoạt động như một successful deployable method. Chưa thay đổi title
cho đến khi thảo luận lại với tác giả và advisor.

## 3. Framing có thể bảo vệ được

Kết quả 0/960 có thể trở thành contribution nếu paper được định vị là một
**reliability-audit and certification-feasibility paper**:

- target-only alarms có resolution floor chính xác \(1/(k+1)\);
- vượt resolution floor vẫn không bảo đảm stable FAR dưới shift;
- image-level fixed-archive risk và new-category risk là hai estimand khác nhau;
- independent category count, không phải image count hoặc seed count, quyết
  định feasibility của category certification;
- CRESS là fail-closed source-assisted certification procedure: zero threshold
  là output đúng khi evidence không đủ, không phải một kết quả cần che giấu;
- đóng góp thực tiễn là ngăn source pooling hoặc image-level evidence bị trình
  bày sai thành unconditional target-category guarantee.

Theo framing này, câu mô tả đúng là:

> The structural infeasibility predicted by the category-count bound is
> confirmed throughout the frozen 960-cell audit grid.

Không nên viết hoặc ngụ ý rằng CRESS đã thất bại trong 960 independent trials.

## 4. So sánh target-only LOIO và CRESS cần giữ rõ

### Target-only LOIO

- Chỉ dùng \(k\) target-normal supports.
- Không cần source-to-target transfer assumption.
- Có grid thô với \(p_{\min}=1/(k+1)\).
- LOIO/full-support asymmetry và corruption shift có thể gây FAR lệch khỏi
  nominal level.

### CRESS

- Dùng normal archives từ nhiều non-target source categories.
- Reference map có grid mịn hơn và về nguyên tắc có thể tạo sub-floor
  candidates.
- Disjoint Reference/Proposal/Certification roles cho phép đánh giá candidate
  selection độc lập theo category.
- Strict certificate hiện fail-closed vì thiếu independent certification
  categories.
- Target control vẫn conditional trên transfer assumption.

Do đó, CRESS có **nhiều statistical structure hơn**, nhưng strict experiment
hiện tại không chứng minh nó có target performance tốt hơn target-only LOIO.

## 5. Những việc không giải quyết được vấn đề

- Thêm GPU seeds không tăng số independent categories.
- Thêm corruption copies không tăng số independent categories.
- Thêm source images trong cùng category chỉ cải thiện fixed-archive image
  analysis, không sửa new-category certificate.
- Không được thay category certificate bằng image certificate rồi giữ nguyên
  claim.
- Không được đưa historical non-independent CRESS results lên làm certified
  evidence.
- Không nên giấu 0/960 trong Appendix hoặc gọi đây là optimization failure.

## 6. Các hướng tăng sức mạnh cần bàn sau pipeline

1. **Framing/title audit:** quyết định paper là method-first hay
   limits/audit-first; kiểm tra title, abstract, introduction và cover letter
   theo cùng một identity.
2. **Category-rich controlled simulation (CPU):** kiểm tra phase transition từ
   \(\tau^\star=0\) sang positive thresholds khi category count đủ lớn. Phải ghi
   rõ đây là controlled validation, không phải benchmark evidence.
3. **Study-design analysis:** trình bày category budget cần thiết theo
   \(\alpha,\delta,M,A\) và allocation \(\mathcal R/\mathcal P/\mathcal C\).
4. **Positive utility statement:** giải thích fail-closed output có giá trị gì
   đối với safe deployment và study design, dù không tăng AUROC hoặc power.
5. **Independent statistical review:** nhờ một reviewer có chuyên môn về
   distribution-free inference kiểm tra riêng Proposition 2--4 và claim scope.
6. **Submission decision:** nếu advisor yêu cầu một new method có positive
   category-certified operation, cần thêm category-rich data hoặc redesign
   protocol; nếu chấp nhận audit/limit contribution, phải reframe nhất quán.

## 7. Câu hỏi cần chốt trong buổi thảo luận sau

1. CRESS nên nằm trong title hay chỉ là procedure bên trong một paper về limits?
2. Main contribution nên được phát biểu là method, audit framework hay
   feasibility theorem?
3. Có cần một category-rich simulation trước khi submit không?
4. Có thể xây một source archive đủ nhiều independent categories mà không trộn
   những category populations không tương thích hay không?
5. Target deployment claim cuối cùng là empirical transfer, conditional
   guarantee hay chỉ source-domain certification?
6. Con số 960 nên xuất hiện ở abstract hay chỉ ở Results?
7. Reviewer sẽ nhận được practical takeaway cụ thể nào ngoài kết luận
   ``insufficient categories''?

## 8. Quyết định tạm thời

- Không sửa title hoặc xóa CRESS trong lúc đang hoàn thiện pipeline.
- Giữ nguyên kết quả strict 0/960 và các qualification về source-domain scope.
- Hoàn thiện pipeline sao cho phân biệt rõ target-only route, source-side CRESS
  certification và conditional target application.
- Sau khi pipeline ổn định, quay lại memo này để quyết định framing và các thí
  nghiệm/phân tích bổ sung trước submission.
