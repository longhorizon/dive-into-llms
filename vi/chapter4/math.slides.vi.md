> Bản dịch tiếng Việt · nguồn: [math.pdf](../../documents/chapter4/math.pdf) · 《动手学大模型》(Lordog/dive-into-llms)

> Bản surrogate dịch nội dung chữ của slide (trích bằng PyMuPDF); hình minh họa trong slide không được trích ở đây — vui lòng xem PDF gốc. Các trang 3–16 của PDF gốc có kèm địa chỉ website và phương châm của Đại học Giao thông Thượng Hải; bản dịch giữ nguyên URL và dịch phương châm.

## Trang 1

**LLM suy luận toán học**

陈星宇

## Trang 2

**Mục lục**

1. Giới thiệu suy luận toán học
2. Mô hình lớn cho toán học
3. Học chưng cất (distillation)
4. Mô hình suy luận dài
5. Đánh giá năng lực toán

## Trang 3

www.sjtu.edu.cn — Uống nước nhớ nguồn, yêu nước vinh danh trường

**Giới thiệu suy luận toán học**

Suy luận toán học: năng lực của LLM giải quyết bài toán thông qua phân tích logic, tính toán ký hiệu và suy luận nhiều bước; cần hiểu các khái niệm toán học (như đại số, hình học) và sinh ra đáp án đúng.

Năng lực then chốt:
• Suy luận nhiều bước: tách bài toán phức tạp thành các bước con
• Hiểu ký hiệu: xử lý các ký hiệu và công thức trừu tượng
• Phép tính toán học: thực hiện tính toán chính xác

Ứng dụng: giải toán thi đấu, hỗ trợ giáo dục, dẫn dắt công thức trong nghiên cứu khoa học.

## Trang 4

www.sjtu.edu.cn — Uống nước nhớ nguồn, yêu nước vinh danh trường

**Làm thế nào để thực hiện suy luận toán học trong LLM?**

Chuỗi suy nghĩ [1] (CoT): sinh tường minh các bước suy luận
Tìm kiếm trên cây: Tìm kiếm Monte Carlo trên cây [2]: kết hợp mô hình thưởng tiến trình (PRM) để khám phá các hướng tiếp cận khác nhau
Tự nhất quán [3] (Self-Consistency): lấy mẫu nhiều đường suy luận khác nhau rồi biểu quyết chọn đáp án xuất hiện nhiều nhất để giảm lỗi
Tăng cường bằng công cụ: công cụ bên ngoài — gọi máy tính xử lý phép tính phức tạp, tránh sai số
Trợ giúp bằng chương trình: sinh code (như Python) để thực thi tính toán toán học

[1] Kojima T, Gu S S, Reid M, et al. Large language models are zero-shot reasoners[J]. Advances in neural information processing systems, 2022, 35: 22199-22213.
[2] Guan X, Zhang L L, Liu Y, et al. rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking[J]. arXiv preprint arXiv:2501.04519, 2025.
[3] Wang X, Wei J, Schuurmans D, et al. Self-consistency improves chain of thought reasoning in language models[J]. arXiv preprint arXiv:2203.11171, 2022.

## Trang 5

www.sjtu.edu.cn — Uống nước nhớ nguồn, yêu nước vinh danh trường

**Mô hình suy luận dài**

Mô hình suy luận dài: mô hình sinh chuỗi suy nghĩ dài khi suy luận
Đại diện tiêu biểu: OpenAI-o1[1], DeepSeek-R1[2]
Đặc trưng chuỗi suy nghĩ:
• Tự phản tỉnh
• Chuyển hướng suy nghĩ
• Kiểm chứng và tự sửa đáp án

Việc tăng độ dài sinh ra khi suy luận giúp mở rộng không gian tìm kiếm, cuối cùng nâng cao hiệu năng suy luận toán.
Trong chuỗi suy nghĩ có hòa trộn các chiến lược suy luận kiểu con người.

[1] https://openai.com/index/introducing-openai-o1-preview/
[2] Guo D, Yang D, Zhang H, et al. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning[J]. arXiv preprint arXiv:2501.12948, 2025.

## Trang 6

www.sjtu.edu.cn — Uống nước nhớ nguồn, yêu nước vinh danh trường

**Mô hình suy luận dài**

Đặc trưng chuỗi suy nghĩ:
• Tự phản tỉnh
• Chuyển hướng suy nghĩ
• Kiểm chứng và tự sửa đáp án

Ví dụ: OpenAI-o1 (các nhãn trong hình minh họa của slide: chuyển hướng suy nghĩ, tự sửa lỗi, tự phản tỉnh).

## Trang 7

www.sjtu.edu.cn — Uống nước nhớ nguồn, yêu nước vinh danh trường

**Mô hình lớn cho toán học**

Mô hình lớn cho toán học: mô hình lớn được tối ưu chuyên biệt cho nhiệm vụ suy luận toán
Đại diện tiêu biểu: DeepSeek-Math[1]; Qwen2.5-Math[2]
Tập huấn luyện: DeepMath-103K[3]
Tập đánh giá:
• GSM8k[4]: tập dữ liệu toán chất lượng độ khó cấp tiểu học, gồm 8.5k mẫu
• MATH[5]: tập dữ liệu độ khó cấp thi đấu toán trung học phổ thông, gồm 12.500 mẫu
• AIME: Kỳ thi mời Invitational Toán học Mỹ (American Invitational Mathematics Examination), tổ chức hằng năm; mỗi kỳ thi gồm 30 bài, độ khó cấp Olympiad

[1] Shao Z, Wang P, Zhu Q, et al. Deepseekmath: Pushing the limits of mathematical reasoning in open language models[J]. arXiv preprint arXiv:2402.03300, 2024.
[2] Yang A, Zhang B, Hui B, et al. Qwen2. 5-math technical report: Toward mathematical expert model via self-improvement[J]. arXiv preprint arXiv:2409.12122, 2024.
[3] He Z, Liang T, Xu J, et al. Deepmath-103k: A large-scale, challenging, decontaminated, and verifiable mathematical dataset for advancing reasoning[J]. arXiv preprint arXiv:2504.11456, 2025.
[4] Cobbe K, Kosaraju V, Bavarian M, et al. Training verifiers to solve math word problems[J]. arXiv preprint arXiv:2110.14168, 2021.
[5] Hendrycks D, Burns C, Kadavath S, et al. Measuring mathematical problem solving with the math dataset[J]. arXiv preprint arXiv:2103.03874, 2021.

## Trang 8

www.sjtu.edu.cn — Uống nước nhớ nguồn, yêu nước vinh danh trường

**Mô hình lớn cho toán học**

DeepSeek-Math:
• Làm sạch 120B trang web toán học: lọc lặp lại dữ liệu Common Crawl, tránh nhiễm bẩn tập đánh giá
• Khởi tạo bằng mô hình code: dựa trên DeepSeek-Coder-v1.5 thay vì LLM đa dụng, nâng cao năng lực xử lý ký hiệu
• Học tăng cường GRPO: tối ưu chính sách so sánh theo nhóm (Group Relative Policy Optimization), giảm tiêu thụ bộ nhớ GPU và nâng cao tính khái quát hóa; về sau trở thành hạt nhân của mô hình R1
• Hiệu năng: mô hình 7B đạt SOTA vào thời điểm đó

## Trang 9

www.sjtu.edu.cn — Uống nước nhớ nguồn, yêu nước vinh danh trường

**Mô hình lớn cho toán học**

Qwen2.5-Math:
• Ngữ liệu tiền huấn luyện: Qwen Math Corpus v2 (1T token), gồm dữ liệu tổng hợp và các bài toán tiếng Trung
• Sinh dữ liệu: Qwen2-72B-Instruct sinh các cặp QA chất lượng cao, tăng cường tính đa dạng
• Kết hợp CoT & TIR: suy luận chuỗi suy nghĩ + tích hợp công cụ (như trình thông dịch Python), hỗ trợ phân tích song ngữ
• Lặp lại mô hình thưởng: Qwen2.5-Math-RM chỉ dẫn sự tiến hóa của dữ liệu SFT; giai đoạn học tăng cường áp dụng GRPO

Kết quả: mô hình 7B vượt các mô hình nguồn mở 30B-70B trên benchmark MATH, tiệm cận GPT-4.

## Trang 10

www.sjtu.edu.cn — Uống nước nhớ nguồn, yêu nước vinh danh trường

**Mô hình lớn cho toán học**

DeepMath-103K:
• Tập huấn luyện thiết kế riêng cho nhiệm vụ toán độ khó cao
• Thu thập các tập huấn luyện chủ lưu và tiến hành khối lượng lớn công việc làm sạch dữ liệu, đảm bảo không trùng lặp với các tập đánh giá toán phổ biến
• Bao gồm chú thích độ khó và phản hồi của R1

Các mô hình huấn luyện bằng dữ liệu DeepMath-103K có thể nâng cao hiệu quả năng lực toán.

## Trang 11

www.sjtu.edu.cn — Uống nước nhớ nguồn, yêu nước vinh danh trường

**Học chưng cất (distillation)**

Làm sao nhanh chóng có được năng lực suy luận toán của mô hình suy luận dài?

Tinh chỉnh có giám sát (SFT):
• Tác dụng: căn chỉnh đầu ra của mô hình với định dạng giải bài của con người, học các bước suy luận chuẩn
• Yêu cầu dữ liệu: cần chú thích dạng chuỗi chất lượng cao

Chưng cất tri thức:
• Quy trình: mô hình lớn (giáo viên) sinh dữ liệu CoT → mô hình nhỏ (học trò) học mô hình suy luận bằng SFT
• Phương án tiêu biểu: bản chưng cất DeepSeek-R1 — Qwen-7B vượt mô hình nền 32B

## Trang 12

www.sjtu.edu.cn — Uống nước nhớ nguồn, yêu nước vinh danh trường

**Học chưng cất (distillation)**

Phương pháp chưng cất ba bước:
• Sinh dữ liệu: mô hình giáo viên sinh dữ liệu CoT chất lượng cao
• Lấy mẫu từ chối (rejection sampling): loại bỏ đáp án sai, giữ lại các chuỗi suy luận mạch lạc về logic và chuẩn mực về định dạng
• Tinh chỉnh SFT: mô hình nhỏ học trực tiếp đầu ra của giáo viên, không cần giai đoạn RL bổ sung

Ưu điểm: tận dụng dữ liệu hiệu quả, ngưỡng thấp, học được trực tiếp hành vi suy luận phức tạp
Hạn chế: giới hạn trên hiệu năng của mô hình nhỏ phụ thuộc năng lực của giáo viên, bài toán phức tạp vẫn cần mô hình lớn

## Trang 13

www.sjtu.edu.cn — Uống nước nhớ nguồn, yêu nước vinh danh trường

**Đánh giá năng lực toán**

Benchmark truyền thống:
• Tập dữ liệu: GSM8K (tiểu học), MATH (trung học phổ thông), AIME (thi đấu)
• Chỉ báo: độ chính xác, Pass@k (tỷ lệ pass khi lấy mẫu k lần)

Đặc điểm đánh giá toán: nghiên cứu hiện tại chỉ nhắm vào các bài toán có đáp án dạng số/ký hiệu rõ ràng
Hướng đi tiên phong: đánh giá tính đúng đắn của bài chứng minh
Thách thức:
• Đầu ra ngôn ngữ tự nhiên của LLM: làm sao trích đáp án từ lời giải ngôn ngữ tự nhiên
• Đánh giá tính nhất quán của kết quả: làm sao đánh giá tính nhất quán của các biểu thức toán

## Trang 14

www.sjtu.edu.cn — Uống nước nhớ nguồn, yêu nước vinh danh trường

**Đánh giá năng lực toán**

Trích xuất đáp án:
• GSM8K: dùng 4 ký hiệu #### liên tiếp để đánh dấu đáp án
• MATH: dùng \\boxed{} để bọc đáp án — phương án chủ lưu hiện nay

Ưu điểm:
• Chuẩn trích xuất thống nhất, thuận tiện cho đánh giá
Nhược điểm:
• Mô hình cần được huấn luyện chuyên biệt cho định dạng đầu ra
• Không bao phủ được mọi kịch bản đầu ra

(Nhãn trong hình minh họa của slide: phương án GSM8K, phương án MATH.)

## Trang 15

www.sjtu.edu.cn — Uống nước nhớ nguồn, yêu nước vinh danh trường

**Đánh giá năng lực toán**

Đánh giá đáp án: làm sao đánh giá đáp án mô hình sinh ra có đúng hay không?

Đánh giá theo quy tắc:
• Vì đáp án đầu ra của mô hình về cơ bản tuân thủ định dạng LaTex, có thể trích biểu thức theo quy tắc LaTex, rồi dùng quy tắc do con người xây dựng để phán đoán nhất quán
• Đại diện tiêu biểu: Huggingface Math-Verify[1]

LLM Judge:
• Đánh giá theo quy tắc không phủ được các trường hợp biên biểu đạt bằng chữ, và việc trích đáp án có thể có sai sót
• Dùng mô hình lớn (thường được huấn luyện chuyên biệt) để phán đoán trực tiếp đáp án sinh ra và đáp án chuẩn có tương đương hay không
• Đại diện tiêu biểu: Omni-Judge[2] — mô hình đánh giá đáp án chuyên dụng cho tập Omini

[1] https://github.com/huggingface/Math-Verify
[2] https://huggingface.co/KbsdJames/Omni-Judge

## Trang 16

www.sjtu.edu.cn — Uống nước nhớ nguồn, yêu nước vinh danh trường

**Tổng kết**

Suy luận toán học: năng lực của LLM giải quyết bài toán thông qua phân tích logic, tính toán ký hiệu và suy luận nhiều bước; cần hiểu các khái niệm toán học (như đại số, hình học) và sinh ra đáp án đúng
Mô hình suy luận dài: mô hình sinh chuỗi suy nghĩ dài khi suy luận
Mô hình lớn cho toán học: mô hình lớn được tối ưu chuyên biệt cho nhiệm vụ toán, dùng dữ liệu toán để tiền huấn luyện
Học chưng cất: mô hình lớn sinh dữ liệu, mô hình nhỏ học trực tiếp kết quả lấy mẫu của mô hình lớn
Đánh giá toán:
• Benchmark phổ biến: GSM8K, MATH500, AIME
• Quy trình đánh giá: sinh kết quả, trích kết quả qua định dạng thống nhất, dùng quy tắc/LLM để so sánh tính nhất quán

## Trang 17

Thank you
