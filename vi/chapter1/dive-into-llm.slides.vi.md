> Bản dịch tiếng Việt · nguồn: [dive-into-llm.pdf](../../documents/chapter1/dive-into-llm.pdf) · 《动手学大模型》(Lordog/dive-into-llms)

> Bản surrogate dịch nội dung chữ của slide (trích bằng PyMuPDF); hình minh họa trong slide không được trích ở đây — vui lòng xem PDF gốc.

## Trang 1

**Công nghệ và phát triển của mô hình lớn**

张倬胜

上海交通大学计算机学院 (Khoa Máy tính, Đại học Giao thông Thượng Hải)

zhangzs@sjtu.edu.cn

https://bcmi.sjtu.edu.cn/~zhangzs

## Trang 2

**Mục lục**

❑ Tổng quan về mô hình lớn
⚫ Tổng quan phát triển
⚫ Phạm trù khái niệm
❑ Mô hình tiền huấn luyện
⚫ Các loại chính
⚫ Kiến trúc mô hình
❑ Mô hình quy mô lớn
⚫ Chuyển đổi paradigm
⚫ Các đại diện chính
⚫ Công nghệ then chốt
⚫ Phương thức triển khai
❑ Mở rộng khái niệm
⚫ Mô hình lớn chuyên lĩnh vực
⚫ Nền tảng đa phương tiện
⚫ Nền tảng tác tử (agent)

## Trang 3

**Mục lục** (lặp lại trang 2)

## Trang 4

**Sự phát triển của trí tuệ nhân tạo**

❑ Công nghệ AI đã trải qua quá trình phát triển từ dữ liệu nhỏ đến dữ liệu lớn, từ mô hình nhỏ đến mô hình lớn, từ chuyên dụng đến đa dụng, và đang dần bước vào kỷ nguyên mô hình lớn
❑ Thực hiện tiền huấn luyện tự giám sát quy mô lớn trên khối lượng khổng lồ dữ liệu không nhãn, học được lượng lớn tri thức ngôn ngữ và tri thức thế giới
❑ Hoàn thành đa dạng nhiệm vụ thông qua tương tác ngôn ngữ tự nhiên, sở hữu năng lực xử lý nhiệm vụ đa kịch bản, đa công dụng, liên ngành

(Nhãn trên sơ đồ: Mô hình lớn chuyên lĩnh vực · Nền tảng đa phương tiện · Nền tảng tác tử (agent) — "Mở rộng khái niệm")

[1] Zhao, Wayne Xin, et al. A Survey of Large Language Models. arXiv preprint arXiv:2303.18223.

## Trang 5

**Phạm trù của mô hình lớn**

(Nhãn trên sơ đồ: Mô hình ngôn ngữ tiền huấn luyện · Mô hình ngôn ngữ quy mô lớn · Nền tảng đa phương tiện · Nền tảng tác tử (agent) · Mô hình lớn chuyên lĩnh vực)

## Trang 6

**Mục lục** (lặp lại trang 2)

## Trang 7

**Mô hình ngôn ngữ tiền huấn luyện**

❑ Paradigm mới của trí tuệ ngôn ngữ — mô hình ngôn ngữ tiền huấn luyện (đại diện: ELMo, BERT, GPT-1/2)
⚫ Tiền huấn luyện tự giám sát trên dữ liệu quy mô lớn, sau khi tinh chỉnh sẽ thích ứng với mọi loại nhiệm vụ, tận dụng hiệu quả dữ liệu lớn, mô hình lớn và sức mạnh tính toán lớn
⚫ Chủ yếu ứng dụng cho các nhiệm vụ phân tích và hiểu ngôn ngữ

[1] Zhang, Zhuosheng, et al. Machine Reading Comprehension: The Role of Contextualized Language Models and Beyond. arXiv preprint arXiv:2005.06249.

## Trang 8

**Các loại chính**

(Ba cột: Mô hình encoder (Encoder-Only) · Mô hình decoder (Decoder-Only) · Mô hình encoder-decoder (Encoder-Decoder) — "Mức độ quan tâm của các loại mô hình theo thời gian")

❑ Trước khoảng năm 2021, các phiên bản phái sinh của mô hình encoder và mô hình encoder-decoder liên tục xuất hiện; các phiên bản được gọi vui là "BERTology"
❑ Sau khoảng năm 2021, mô hình decoder phát triển thần tốc, đón chào kỷ nguyên mô hình lớn sinh thành "Next-Level"

[1] Rogers, Anna, et al. A primer in BERTology: What we know about how BERT works. TACL, 2021.              [2] Minaee, Shervin, et al. Large language models: A survey. arXiv preprint arXiv:2402.06196.

## Trang 9

**Từ góc nhìn mô hình hóa tiền huấn luyện**

❑ Từ góc độ mô hình hóa tiền huấn luyện tự giám sát, mục tiêu huấn luyện của các kiến trúc khác nhau có sự khác biệt
⚫ Mô hình encoder: Mô hình hóa ngôn ngữ che mask (Masked Language Modeling)
⚫ Mô hình decoder: Mô hình hóa ngôn ngữ tự hồi quy (Auto-regressive Language Modeling)
⚫ Mô hình encoder-decoder: Mô hình hóa chuỗi-đến-chuỗi (Sequence to Sequence Modeling)

[1] Ding, Ning, et al. Parameter-efficient fine-tuning of large-scale pre-trained language models. Nature Machine Intelligence, 2023.

## Trang 10

**Mô hình encoder**

❑ Mục tiêu huấn luyện chính: Mô hình hóa ngôn ngữ che mask (Masked Language Modeling, MLM)
❑ Các mô hình đại diện: BERT, RoBERTa, ALBERT

Sơ đồ (Transformer Encoder) — chuỗi token với nhãn dự đoán:

    [CLS]  Hãy  chúng  ta  cùng  bắt tay  [MASK]  mô hình lớn  phát triển  toàn quy trình
    NotNext  →  học

## Trang 11

**Mô hình decoder**

❑ Mục tiêu huấn luyện chính: Mô hình hóa ngôn ngữ tự hồi quy (Auto-regressive Language Modeling)
❑ Các mô hình đại diện: dòng GPT, Llama, PaLM, v.v.

Sơ đồ (Decoder) — sinh tự hồi quy từng bước:

    [BOS]  Hãy  chúng  ta  cùng  bắt tay  học  mô hình lớn  then chốt
    Hãy  chúng  ta  cùng  bắt tay  học  mô hình lớn  then chốt  kỹ thuật

## Trang 12

**So sánh ưu nhược điểm**

Mô hình encoder (BERT):
- Ưu điểm: tận dụng ngữ cảnh hai chiều, hiệu quả hiểu ngôn ngữ tốt
- Nhược điểm: sử dụng ký hiệu đặc biệt [mask], gây ra chênh lệch tiền huấn luyện – tinh chỉnh; giả định mọi token bị mask độc lập với nhau

Mô hình decoder (GPT):
- Ưu điểm: về bản chất phù hợp với các nhiệm vụ sinh, dễ xây dựng dữ liệu (huấn luyện) quy mô lớn
- Nhược điểm: giới hạn ở mô hình hóa một chiều, khó tận dụng đồng thời thông tin ngữ cảnh hai chiều

## Trang 13

**Mô hình encoder-decoder**

❑ Mục tiêu huấn luyện chính: Mô hình hóa chuỗi-đến-chuỗi (Sequence to Sequence Modeling)
❑ Các mô hình đại diện: T5, BART

Sơ đồ (Encoder → Decoder):

    Hãy cùng <Y> học kỹ thuật then chốt mô hình lớn
    <X> bắt tay <Y> mô hình lớn <Z>

## Trang 14

**Lựa chọn mô hình theo kịch bản ứng dụng**

- Mô hình encoder: phù hợp với các nhiệm vụ discriminative như phân loại, hồi quy, v.v.
- Mô hình decoder: phù hợp với nhiệm vụ sinh mở
- Mô hình encoder-decoder: vừa có năng lực discriminative vừa sinh

## Trang 15

**Mô hình ngôn ngữ tiền huấn luyện: Kiến trúc mô hình**

❑ RNN (LSTM)
⚫ Bắt các quan hệ phụ thuộc giữa các từ, nhưng vì vấn đề tính toán gradient, RNN thường khó huấn luyện
⚫ Tốc độ tính toán rất chậm, khả năng học quan hệ phụ thuộc dài cũng hạn chế
❑ Transformer √ (Attention is all you need)
⚫ Loại bỏ hoàn toàn cơ chế lặp của RNN, áp dụng cơ chế self-attention để xử lý toàn cục
⚫ Ba ma trận trọng số (Query, Key và Value) bắt các quan hệ phụ thuộc ngữ cảnh
⚫ Mạng nhiều lớp: mỗi lớp gồm cơ chế multi-head attention và mạng feed-forward
⚫ Bổ sung mã hóa vị trí (Positional Encoding)

## Trang 16

**Mục lục** (lặp lại trang 2)

## Trang 17

**Tổng quan về mô hình lớn**

[1] Zhao, Wayne Xin, et al. A Survey of Large Language Models. arXiv preprint arXiv:2303.18223.

## Trang 18

**Chuyển đổi paradigm trong kỷ nguyên mô hình lớn**

❑ Dịch chuyển paradigm công nghệ: từ huấn luyện chuyên biệt cho từng nhiệm vụ độc lập sang "tiền huấn luyện + hậu huấn luyện" tập trung hóa và "tiền huấn luyện + học bằng prompt"
❑ Thống nhất paradigm nhiệm vụ: từ các hình thức nhiệm vụ độc lập riêng rẽ tiến tới hình thức mô hình hóa chuỗi-đến-chuỗi thống nhất

Sơ đồ (Quá khứ · Bây giờ (huấn luyện) · Bây giờ (ứng dụng)):
- Quá khứ: trên mỗi nhiệm vụ, từng người dùng tự xây dựng mô hình và tự hoàn thành toàn bộ quá trình huấn luyện machine learning — training cá thể hóa
- Bây giờ (huấn luyện): nút trung tâm hoàn thành tiền huấn luyện quy mô lớn mang tính khái quát, cung cấp mô hình gần hoàn chỉnh, dùng làm module chuẩn để hậu huấn luyện (tinh chỉnh theo chỉ dẫn / reinforcement learning) nhằm thích ứng với nhiều kịch bản rộng
- Bây giờ (ứng dụng): ❑ Prompt engineering (⚫ học theo ngữ cảnh, ⚫ chuỗi suy nghĩ (CoT), ⚫ điều phối quy trình làm việc); ❑ Huấn luyện nhẹ

## Trang 19

**Chuyển đổi paradigm trong kỷ nguyên mô hình lớn** (lặp lại trang 18)

[1] Chung, H.W., et al. Scaling instruction-finetuned language models. JMLR, 2024.

## Trang 20

**Mô hình ngôn ngữ quy mô lớn**

❑ Mô hình ngôn ngữ quy mô lớn: vận dụng thuật toán mạnh mẽ tiêu tốn lượng lớn sức mạnh tính toán, huấn luyện trong khối lượng dữ liệu khổng lồ để tạo ra hàm phân phối xác suất phức tạp
⚫ Nhiều lượng tính toán hơn, chi phí suy luận lớn hơn
⚫ Năng lực khái quát hóa mạnh hơn, xuất hiện năng lực emergent

So sánh kiểu (Pretrained language model (mô hình vừa và nhỏ, mô hình thường) — Mô hình ngôn ngữ quy mô lớn (mô hình lớn sinh thành)):
- Mô hình điển hình: ELMo, BERT, GPT-1/2 — GPT-3, ChatGPT, LLaMA
- Kết cấu mô hình: RNN, Transformer — Transformer
- Cơ chế attention: hai chiều, một chiều — một chiều
- Phương thức huấn luyện: autoencoder khử nhiễu — sinh tự hồi quy
- Kiểu nhiệm vụ sở trường: hiểu, phán đoán — sinh
- Quy mô mô hình: khoảng dưới 10B tham số — khoảng từ 10B–100B tham số trở lên
- Cách ứng dụng cho nhiệm vụ hạ nguồn: fine-tuning — fine-tuning & học bằng prompt
- Năng lực emergent: di chuyển miền dữ liệu nhỏ — học theo ngữ cảnh, chuỗi suy nghĩ (CoT)

[1] Minaee, Shervin, et al. Large language models: A survey. arXiv preprint arXiv:2402.06196.

## Trang 21

**Mô hình ngôn ngữ quy mô lớn**

▸ Dữ liệu huấn luyện: đa nguyên tố — không còn chỉ là văn bản ngôn ngữ tự nhiên mà là tổ hợp nhiều loại dữ liệu: văn bản ngôn ngữ tự nhiên, mã lập trình, công thức phân tử hóa học, thậm chí cả trình tự gene, thậm chí cả hình ảnh
▸ Phương thức huấn luyện: chuyển toàn diện từ tiền huấn luyện discriminative (điển hình là BERT) sang tiền huấn luyện sinh thành (điển hình là GPT)
▸ Kiến trúc mô hình: chuyển từ Transformer hai chiều sang Transformer một chiều (Decoder-only)
▸ Cách ứng dụng: từ fine-tuning tiến tới học bằng prompt thân thiện hơn
▸ Ít mẫu hơn: từ bắt buộc phải có một số lượng mẫu có nhãn, xuống few-shot,thậm chí zero-shot
▸ Hình thức làm việc của học bằng prompt tiến gần hình thức hội thoại người–máy

## Trang 22

**Công nghệ then chốt**

❑ Ba giai đoạn xây dựng chính kinh điển: tiền huấn luyện, tinh chỉnh theo chỉ dẫn (instruction fine-tuning), căn chỉnh (alignment)

Sơ đồ (Dữ liệu → Mô hình → Mục tiêu):
- Dữ liệu: dữ liệu thô — văn bản, sách, trang web, mã lập trình... cấp trăm tỷ → Mô hình: mô hình nền tảng (tiền huấn luyện, thời gian huấn luyện cấp tháng)
- Dữ liệu: chỉ dẫn người dùng có nhãn — hàng vạn chỉ dẫn ngôn ngữ tự nhiên của người dùng và đáp án tương ứng → Mô hình: mô hình SFT (tinh chỉnh theo chỉ dẫn, thời gian huấn luyện cấp ngày)
- Dữ liệu: cặp so sánh có nhãn — chục/triệu cặp so sánh có nhãn, căn chỉnh với chỉ dẫn người dùng → Mô hình: mô hình căn chỉnh (căn chỉnh, thời gian huấn luyện cấp ngày)
- Mục tiêu: học tri thức lĩnh vực/chung; nâng cao năng lực tuân thủ chỉ dẫn; sinh chỉ dẫn an toàn hơn

## Trang 23

**Quy trình xây dựng mô hình lớn** (nội dung lặp lại trang 22 — xem slide gốc)

## Trang 24

**Công nghệ then chốt 1: Tiền huấn luyện**

(Nhãn trên sơ đồ: Thuật toán · Dữ liệu · Sức mạnh tính toán)

## Trang 25

**Công nghệ then chốt 2: (Lệnh) tinh chỉnh**

▸ Tinh chỉnh mô hình thông qua dữ liệu chỉ dẫn chất lượng cao (cho mô hình biết phải thực hiện nhiệm vụ gì)
▸ Giúp mô hình hiểu đặc trưng nhiệm vụ, cải thiện lớn hiệu năng trên từng nhiệm vụ
▸ Cải thiện độ ổn định của học bằng prompt, khiến văn bản đầu ra của mô hình kiểm soát được tốt hơn
▸ Ví dụ lấy "suy luận ngôn ngữ tự nhiên", xây dựng dữ liệu huấn luyện tinh chỉnh theo chỉ dẫn

(Nhãn trên sơ đồ: fine-tuning thông thường · tinh chỉnh theo chỉ dẫn)

## Trang 26

**Công nghệ then chốt 2: (Lệnh) tinh chỉnh**

▸ Phương thức tinh chỉnh theo chỉ dẫn:
▸ Mượn các dataset có sẵn: thông qua việccon người thêm vào prompt chỉ định kiểu nhiệm vụ hiện tại làm tiền tố đầu vào (chỉ dẫn), fine-tuning trên nhiều dataset đa kiểu nhiệm vụ
▸ Fine-tuning có giám sát dựa trên minh họa của con người: dựa trên câu trả lời chất lượng cao do con người viết theo prompt (chỉ dẫn), mô hình fine-tuning có giám sát theo đó
▸ Điểm then chốt khi xây dựng dữ liệu: số lượng nhiệm vụ, tính đa dạng của nhiệm vụ

(Nhãn trên sơ đồ: dựa trên minh họa con người (InstructGPT) · mượn dataset có sẵn (FLAN))

Wei, Jason, et al. "Finetuned Language Models are Zero-Shot Learners." International Conference on Learning Representations. 2021.

## Trang 27

**Công nghệ then chốt 2: (Lệnh) tinh chỉnh**

Wei, Jason, et al. "Finetuned Language Models are Zero-Shot Learners." International Conference on Learning Representations. 2021.

▸ FLAN instruction fine-tuning: dùng tinh chỉnh theo chỉ dẫn để nâng cao năng lực zero-shot của mô hình
▸ Chia 62 nhiệm vụ xử lý ngôn ngữ tự nhiên thành 12 nhóm
▸ Với mỗi nhiệm vụ, xây dựng thủ công 10 mẫu chỉ dẫn riêng biệt
▸ Độ nâng cao hiệu quả do tinh chỉnh theo chỉ dẫn mang lại tồn tại "hiệu ứng mô hình lớn" rõ rệt
▸ Chỉ khi quy mô mô hình vào khoảng chục tỷ tham số, tinh chỉnh theo chỉ dẫn mới mang lại nâng cao trên các nhiệm vụ ngoài mẫu

## Trang 28

**Công nghệ then chốt 3: Căn chỉnh (alignment)**

▸ Mô hình ngôn ngữ quy mô lớn thường sinh ra câu trả lời vô dụng, độc hại, không chân thực
▸mượn chi phí nhân lực thấp, dùng phương pháp reinforcement learning để fine-tune tiếp mô hình ngôn ngữ lớn
▸ Khiến đầu ra của mô hình ngôn ngữ lớn "căn chỉnh" với ý định của con người, xuất ra câu trả lời được yêu thích
▸ Đầu ra của mô hình ngôn ngữ càng khớp ý định con người, càng phù hợp chuẩn mực đạo đức thì mô hình nhận được càng nhiều phần thưởng
▸ Giảm mạnh đầu ra thông tin gây hại và sai lệch

Ví dụ hội thoại:
➢ Người dùng: hỏi cách phá cửa đột nhập vào nhà
➢ ChatGPT: chỉ ra đây là điều không phù hợp, có thể dẫn tới phạm tội
➢ Người dùng: nói lại rằng mình chỉ muốn bảo vệ nhà khỏi bị đột nhập
➢ ChatGPT: đưa ra 7 gợi ý cụ thể

## Trang 29

**Công nghệ then chốt 3: Căn chỉnh (alignment)**

▸ "Căn chỉnh" với sở thích, giá trị, ý định, an toàn... của con người
▸ Định nghĩa: dẫn dắt hành vi của hệ thống trí tuệ nhân tạo, khiến chúng phù hợp với lợi ích và mục tiêu dự kiến của người thiết kế
▸ Nhà nước đã ban hành 《互联网信息服务深度合成管理规定》 (Quy định quản lý tổng hợp sâu dịch vụ thông tin internet) và 《生成式人工智能服务管理办法》 (Biện pháp quản lý dịch vụ trí tuệ nhân tạo sinh thành)

Trích quy định (bản dịch): Không được lợi dụng dịch vụ tổng hợp sâu để sản xuất, sao chép, đăng phát, truyền bá thông tin giả; không được lợi dụng dịch vụ tổng hợp sâu để sản xuất, sao chép, đăng phát, truyền bá thông tin bị pháp luật và quy định hành chính cấm

▸ ChatGPT đã bị lợi dụng cho tội phạm: tấn công mạng, hướng dẫn phạm tội, v.v.

## Trang 30

**Công nghệ then chốt 3: Căn chỉnh (alignment)**

▸ Nguyên tắc: hữu dụng, trung thực và vô hại
▸ Phù hợp văn hóa vùng miền quốc gia, phù hợp pháp luật quy định, phù hợp đạo đức luân lý, nói sự thật và logic
▸ Điểm then chốt kỹ thuật:
▸ Dataset: dataset SFT (13k), dataset RM (33k), dataset RL (31k)
▸ Mô hình: mô hình fine-tuning có giám sát SFT, mô hình phần thưởng RM, mô hình reinforcement learning RL

Ouyang, Long, et al. "Training language models to follow instructions with human feedback." Advances in Neural Information Processing Systems 35 (2022): 27730-27744.

## Trang 31

**Công nghệ then chốt 3: Căn chỉnh (alignment)**

Ouyang, Long, et al. "Training language models to follow instructions with human feedback." Advances in Neural Information Processing Systems 35 (2022): 27730-27744.

Bước 1: Supervised fine-tuning (SFT)

Sơ đồ: "Mặt trăng là gì?" → mô hình SFT (đầu ra: thiên thể hình cầu xoay quanh Trái Đất); dữ liệu thu thập qua sampling và API → GPT-3 175B + đáp án mục tiêu có nhãn

## Trang 32

**Công nghệ then chốt 3: Căn chỉnh (alignment)**

Ouyang, Long, et al. "Training language models to follow instructions with human feedback." Advances in Neural Information Processing Systems 35 (2022): 27730-27744.

Bước 2: Reward modeling (RM)

Sơ đồ: "Mặt trăng là gì?" → mô hình SFT → các đáp án:
- A. Mặt trăng là thiên thể gần Trái Đất nhất trong Hệ Mặt Trời.
- D. Mặt trăng là vệ tinh của Trái Đất, đường kính xấp xỉ bằng 1/4 Trái Đất.
- ... → xếp hạng: D > C > A = B
- Mô hình RM: GPT-3 175B tiền huấn luyện → mô hình 6B (rẻ + ổn định) → mô hình xếp hạng (đầu ra điểm số cho câu hỏi + đáp án)

## Trang 33

**Công nghệ then chốt 3: Căn chỉnh (alignment)** (nội dung lặp lại trang 32, kèm bổ sung)

Ouyang, Long, et al. "Training language models to follow instructions with human feedback." Advances in Neural Information Processing Systems 35 (2022): 27730-27744.

Bổ sung trên sơ đồ RM: câu hỏi trong dataset; hai đáp án ứng với câu hỏi x trong dataset, trong đó y_w được xếp hạng cao hơn y_l; độ chênh lệch điểm do mô hình RM chấm

## Trang 34

**Công nghệ then chốt 3: Căn chỉnh (alignment)**

yl

Ouyang, Long, et al. "Training language models to follow instructions with human feedback." Advances in Neural Information Processing Systems 35 (2022): 27730-27744.

Bước 3: Reinforcement learning (RL)

Sơ đồ: "Siêu dẫn ở nhiệt độ phòng là gì?" → mô hình SFT → mô hình RL, với mô hình RM và PPO

Note: PPO (Proximal Policy Optimization)

## Trang 35

**Công nghệ then chốt 3: Căn chỉnh (alignment)** (nội dung lặp lại trang 34, kèm bổ sung)

Ouyang, Long, et al. "Training language models to follow instructions with human feedback." Advances in Neural Information Processing Systems 35 (2022): 27730-27744.

Bổ sung trên sơ đồ: hàm mất mát ngôn ngữ gốc · InstructGPT

## Trang 36

**Công nghệ then chốt 3: Căn chỉnh (alignment)**

(trang trống, không trích được chữ — xem slide gốc)

## Trang 37

**Định luật mở rộng (Scaling Law) của mô hình ngôn ngữ quy mô lớn**

❑ Mối quan hệ giữa hiệu năng mô hình với ba yếu tố: kích thước mô hình, quy mô dữ liệu và sức mạnh tính toán
⚫ Khi quy mô tham số mô hình và quy mô dữ liệu tiền huấn luyện không ngừng tăng lên, năng lực mô hình và hiệu quả nhiệm vụ sẽ được cải thiện theo
⚫ Khuyến nghị của Chinchilla: mô hình 10B dùng 200B token (tỉ lệ 1:20)

[1] Kaplan, Jared, et al. Scaling laws for neural language models. arXiv preprint arXiv:2001.08361.

## Trang 38

**Năng lực emergent (Emergent Abilities) của mô hình ngôn ngữ quy mô lớn**

❑ Khi tham số của mô hình ngôn ngữ đạt tới một quy mô nhất định, một số biểu hiện năng lực (suy luận ngôn ngữ) tăng lên đột ngột và mạnh mẽ
❑ Những năng lực không quan sát được ở mô hình nhỏ nhưng xuất hiện ở mô hình lớn

[1] Wei, Jason, et al. Emergent Abilities of Large Language Models. TMLR, 2022.

(Nhãn trên sơ đồ — đại diện của năng lực emergent: học theo ngữ cảnh · suy luận chuỗi suy nghĩ (CoT))

## Trang 39

**Ảo giác (Hallucination) của mô hình ngôn ngữ quy mô lớn**

❑ Định nghĩa: văn bản do mô hình sinh ra không tuân theo văn bản gốc (tính trung thành — Faithfulness) hoặc không khớp với sự thật (tính chính xác — Factualness)
❑ Ưu thế năng lực: biểu hiện của tính sáng tạo và năng lực phân kỳ của mô hình lớn
❑ Ảnh hưởng tiềm tàng: làm giảm độ tin cậy của mô hình, dễ bị tấn công và bị lạm dụng (như sinh nội dung độc hại và phát tán tin đồn), làm ô nhiễm internet

Ví dụ ảo giác:

    Hỏi: Lỗ Tấn và Chu Thụ Nhân có phải là một người không?
    Đáp: Không. Lỗ Tấn và Chu Thụ Nhân là hai người khác nhau.
    Lỗ Tấn là tượng đài văn học hiện đại Trung Quốc, nổi tiếng với phong cách
    văn học độc đáo và những câu chuyện cuốn hút. Chu Thụ Nhân là nhà
    văn nổi tiếng đương đại Trung Quốc, được suy tôn nhờ ngòi bút
    sắc sảo và khả năng quan sát nhạy bén.

(ví dụ hallucination — mô hình trả lời sai: Lỗ Tấn và Chu Thụ Nhân thực ra là cùng một người)

[1] Huang, Lei, et al. A survey on hallucination in large language models: Principles, taxonomy, challenges, and open questions. arXiv preprint arXiv:2311.05232

## Trang 40

**Bản đồ năng lực của mô hình lớn**

(trang chỉ có minh họa — sơ đồ bản đồ năng lực, không trích được chữ ngoài tài liệu tham khảo — xem slide gốc)

[1] Minaee, Shervin, et al. Large language models: A survey. arXiv preprint arXiv:2402.06196.

## Trang 41

**Từ GPT-3 đến ChatGPT — Quá trình tiến hóa của dòng GPT**

(Nhãn trên sơ đồ: 45TB dữ liệu)

❑ GPT-4: năng lực đa phương tiện, khả năng hiểu và xử lý ngữ cảnh dài hơn, huấn luyện và dự đoán hiệu quả cao hơn, các kịch bản ứng dụng giá trị cao rộng hơn
❑ GPT-1: mô hình hóa tự hồi quy một chiều + fine-tuning có giám sát, khám phá năng lực giải quyết nhiệm vụ ngôn ngữ tự nhiên theo paradigm "tiền huấn luyện + fine-tuning"
❑ GPT-2: mô hình hóa tự hồi quy một chiều + nhiều dữ liệu hơn, mô hình lớn hơn, khám phá năng lực giải quyết đa nhiệm vụ dựa trên prompt ngôn ngữ tự nhiên
❑ GPT-3: khám phá hiệu quả của mô hình ngôn ngữ quy mô trăm tỷ tham số, đề xuất phương pháp giải quyết nhiệm vụ dựa trên "học theo ngữ cảnh"
❑ GPT-3.5/ChatGPT: tinh chỉnh theo chỉ dẫn + phản hồi con người + tối ưu hội thoại

## Trang 42

**Quá trình tiến hóa phiên bản dòng GPT**

❑ GPT-4 thể hiện trình độ ngang với con người trên nhiều benchmark chuyên môn và học thuật, trong đó vượt qua kỳ thi luật sư mô phỏng với thành tích khoảng top 10%
❑ Năng lực xử lý đa phương tiện mạnh mẽ mở rộng phạm vi ứng dụng của GPT-4, đồng thời ảo giác sinh thành và các vấn đề an toàn đều được cải thiện đáng kể

OpenAI phát hành hướng dẫn sử dụng GPT-4:
➢ Viết chỉ dẫn rõ ràng
➢ Cung cấp văn bản tham khảo
➢ Tách nhiệm vụ phức tạp thành các nhiệm vụ con đơn giản hơn
➢ Cho mô hình thời gian để "suy nghĩ"
➢ Sử dụng công cụ bên ngoài
➢ Kiểm thử các thay đổi một cách có hệ thống

[1] Achiam, Josh, et al. Gpt-4 technical report. arXiv preprint arXiv:2303.08774.
[2] OpenAI. Prompt engineering. https://platform.openai.com/docs/guides/prompt-engineering.

## Trang 43

**Mô hình lớn dòng Llama**

❑ Mô hình tự hồi quy mã nguồn mở, dựa trên kiến trúc Transformer, quy mô tham số từ 7B đến 405B
❑ Giấy phép thương mại: Llama 1 không được thương mại hóa miễn phí, Llama 2 và Llama 3 được thương mại hóa (cần xin giấy phép thương mại)

So sánh phiên bản (Llama-1 — Llama-2 — Llama-3 — Llama-3.1 — Llama-3.2):
- Quy mô mô hình: 7B-65B — 7B-70B — 8B-70B — 8B-405B — 1B-90B
- Quy mô dữ liệu: 1.4T — 2T — 15T — 15T — 9T
- Đa phương tiện: × — × — × — × — √
- Đa ngôn ngữ: × — × — × — √ — √
- Tool calling: × — × — × — √ — √
- Paradigm huấn luyện: tiền huấn luyện — tiền huấn luyện + tinh chỉnh theo chỉ dẫn + RLHF — tiền huấn luyện + tinh chỉnh theo chỉ dẫn + DPO — tiền huấn luyện + tinh chỉnh theo chỉ dẫn + DPO — tiền huấn luyện + tinh chỉnh theo chỉ dẫn + DPO
- Độ dài ngữ cảnh: 2K — 4k — 8k — 131K — 131K
- Tiến hóa chính: -- — thêm giai đoạn hậu huấn luyện — mở rộng tiền huấn luyện — 1. tăng quy mô mô hình; 2. thêm khả năng đa ngôn ngữ và tool; 3. mở rộng độ dài ngữ cảnh — 1. thêm mô hình chạy trên thiết bị đầu cuối; 2. thêm năng lực đa phương tiện

[1] Touvron, Hugo, et al. Llama: Open and efficient foundation language models. arXiv preprint arXiv:2302.13971.
[2] Touvron, Hugo, et al. Llama 2: Open foundation and fine-tuned chat models. arXiv preprint arXiv:2307.09288.
[3] Dubey, Abhimanyu, et al. The llama 3 herd of models. arXiv preprint arXiv:2407.21783.

## Trang 44

**Mô hình lớn dòng Llama**

❑ Dữ liệu huấn luyện: CommonCrawl, C4, Github, Wikipedia, books, ArXiv, and StackExchange v.v.
❑ Địa chỉ mã nguồn mở: https://github.com/facebookresearch/llama
❑ Llama 3.1 405B vượt qua GPT-3.5 Turbo trong các bài đánh giá trên diện rộng, điểm số vượt GPT-4 0125 trên phần lớn benchmark

[1] Dubey, Abhimanyu, et al. The llama 3 herd of models. arXiv preprint arXiv:2407.21783.

## Trang 45

**Phân loại và ví dụ tiêu biểu của mô hình lớn AI trong nước (Trung Quốc)**

❑ Cuộc chiến trăm mô hình: theo thống kê chưa đầy đủ, tính đến cuối tháng 4 năm 2024, trong nước (Trung Quốc) đã ra mắt tổng cộng 305 mô hình lớn

[1] SuperGLUE团队. 中文大模型基准测评2024年度报告.
(tên tài liệu: Báo cáo thường niên đánh giá chuẩn mô hình lớn tiếng Trung năm 2024 của nhóm SuperGLUE)

## Trang 46

**Mô hình lớn dòng Qwen**

(Nhãn trên sơ đồ: Qwen-Audio · Qwen-Audio-Chat)

❑ Tongyi Qianwen (Qwen) là mô hình ngôn ngữ tiền huấn luyện do Alibaba Cloud nghiên cứu và phát triển, thực hiện các nhiệm vụ hiểu, sinh và giải thích ngôn ngữ, hình ảnh và tài liệu của con người, mang đến cho người dùng trải nghiệm tương tác phong phú trong sáng tạo nội dung, trợ lý văn phòng, trợ lý học tập và đời sống giải trí
❑ Có các năng lực hiểu Trung–Anh, suy luận toán học, hiểu mã lập trình v.v.

[1] Bai, Jinze, et al. Qwen technical report. arXiv preprint arXiv:2309.16609.
[2] Yang, An, et al. Qwen2 technical report. arXiv preprint arXiv:2407.10671.

## Trang 47

**Quá trình tiến hóa phiên bản dòng Qwen**

❑ Qwen1.5: Model Scaling mở rộng về cả lớn hơn và nhỏ hơn, MoE, AWQ/GGUF
❑ Qwen2: tăng cường đa ngôn ngữ, tăng cường năng lực văn bản dài
❑ Qwen2.5: tăng cường năng lực toán và mã, tăng cường đa ngôn ngữ

❑ Scaling
⚫ Qwen: các mô hình 1.8B, 7B, 14B và 72B
⚫ Qwen1.5: các mô hình 0.5B, 1.8B, 4B, 14BA2.7B, 7B, 14B, 32B, 72B và 110B
⚫ Qwen2: các mô hình 0.5B, 1.5B, 7B, 57A14B và 72B
⚫ Qwen2.5: các mô hình 0.5B, 1.5B, 3B, 7B, 14B, 32B và 72B

Đặc điểm lặp phiên bản:
➢ Tối ưu kết cấu (MoE nâng cao hiệu quả huấn luyện)
➢ Mở rộng số lượng và nâng cao chất lượng dữ liệu tiền huấn luyện
➢ Làm phong phú các nhiệm vụ và lĩnh vực được bao phủ ở giai đoạn Post-training
➢ Mở rộng độ dài cửa sổ (trên cả hai phương diện dữ liệu huấn luyện và chiến lược huấn luyện)
➢ Mở rộng cặp ngôn ngữ và tăng cường năng lực đa ngôn ngữ
➢ Tăng cường năng lực chuyên biệt (huấn luyện mô hình chuyên gia + lấy mô hình chuyên gia kéo mô hình nền)
➢ Mở rộng phương tiện (Qwen-VL, Qwen-Audio)

## Trang 48

**Mô hình lớn dòng DeepSeek**

Thẻ 1 — DeepSeek LLM (11/2023):
- Quy mô tham số: 70B, 67B tham số
- Kiến trúc: mô hình Transformer Dense (dày đặc)
- Dữ liệu huấn luyện: ngữ liệu Trung–Anh 2T token
- Paradigm huấn luyện: tuân theo paradigm huấn luyện mô hình lớn chuẩn tiền huấn luyện + SFT + DPO
- Hiệu năng: mô hình lớn đầu tiên của DeepSeek, đối chuẩn dòng Llama2. Bản 67B Base vượt Llama2 70B Base về suy luận, mã hóa v.v. Kiến trúc mô hình dùng cấu trúc Dense

## Trang 49

**Mô hình lớn dòng DeepSeek** (lặp lại trang 48 — bổ sung thẻ 2)

Thẻ 2 — DeepSeek-V2 (5/2024):
- Quy mô tham số: 236B tham số, tham số kích hoạt 21B
- Kiến trúc: giới thiệu kiến trúc DeepSeekMoE (hỗn hợp chuyên gia); giới thiệu MLA (Multi-head Latent Attention)
- Dữ liệu huấn luyện: ngữ liệu 8.1T token
- Paradigm huấn luyện: tuân theo paradigm chuẩn tiền huấn luyện + SFT + reinforcement learning
- Đặc điểm: hiệu năng sánh ngang GPT-4 Turbo. MLA giúp tiết kiệm hơn 90% KV cache, tốc độ suy luận tăng hơn 5 lần. Kiến trúc MoE khiến khi tham số mô hình mở rộng, chi phí suy luận gần như không đổi, chi phí huấn luyện giảm mạnh, nâng cao năng lực mô hình

## Trang 50

**Mô hình lớn dòng DeepSeek** (lặp lại trang 49 — bổ sung thẻ 3)

Thẻ 3 — DeepSeek-V2.5 (9/2024):
- Dựa trên V2, tối ưu chủ yếu năng lực nhiệm vụ tổng quát và năng lực mã hóa

## Trang 51

**Mô hình lớn dòng DeepSeek** (lặp lại trang 50 — bổ sung thẻ 4)

Thẻ 4 — DeepSeek-V3 (12/2024):
- Quy mô tham số: 671B tham số, tham số kích hoạt 37B
- Dữ liệu huấn luyện: ngữ liệu 14.8T token
- Kiến trúc: trên nền V2, giới thiệu Auxiliary-loss-free strategy để cân bằng chuyên gia; giới thiệu Multi-Token Prediction training để nâng cao hiệu năng và tăng tốc suy luận; giới thiệu mixed precision FP8 để giảm chi phí huấn luyện và suy luận
- Paradigm huấn luyện: tuân theo paradigm huấn luyện mô hình lớn chuẩn tiền huấn luyện + SFT + DPO
- Đặc điểm: hiệu năng vượt các dòng Llama3 và Qwen2.5 chủ đạo, đồng thời chi phí huấn luyện và chi phí suy luận giảm mạnh

## Trang 52

**Mô hình lớn dòng DeepSeek** (lặp lại trang 51 — bổ sung thẻ 5)

Thẻ 5 — DeepSeek-R1 (1/2025):
- Mô hình nền: DeepSeek-V3-Base
- Dữ liệu huấn luyện: ngữ liệu 14.8T token
- Paradigm huấn luyện: trên mô hình base, tiến hành trực tiếp huấn luyện đa giai đoạn, huấn luyện cold-start và reinforcement learning
- Đặc điểm: lần đầu đạt tới năng lực suy luận kiểu GPT4-O1

## Trang 53

**Triển khai mô hình lớn**

❑ Kiểu mô hình lớn:
⚫ Mô hình ngôn ngữ lớn: Qwen
⚫ Mô hình đa phương tiện: MiniCPM
❑ Phương thức triển khai:
⚫ Gọi qua API
⚫ Triển khai cục bộ (local)

## Trang 54

**Triển khai mô hình lớn (ví dụ tính năng)**

(trang không trích được chữ ngoài tiêu đề — xem slide gốc)

## Trang 55

**Triển khai mô hình lớn (gọi qua API)**

❑ Lấy quyền gọi mô hình lớn:
⚫ Tongyi Qianwen: https://help.aliyun.com/zh/dashscope/developer-reference/quick-start
⚫ DeepSeek: https://www.deepseek.com
⚫ Llama: https://github.com/Meta-Llama/llama
⚫ Zhipu AI: https://open.bigmodel.cn/
⚫ Openai：https://platform.openai.com/playground
⚫ Khác: Wenxin Yiyan, mô hình lớn Baichuan

*Quy trình cơ bản: mở dịch vụ để lấy API-KEY (được tặng hạn mức tính toán), dùng API Key để gọi dịch vụ (trong đó OpenAI cần "biện pháp khoa học" — biệt ngữ chỉ phương tiện kết nối mạng đặc biệt)

## Trang 56

**Triển khai mô hình lớn (gọi qua API)**

❑ Gọi qua giao diện GUI (phù hợp để thử nghiệm ví dụ):
⚫ https://help.aliyun.com/zh/dashscope/developer-reference/quick-start
⚫ https://huggingface.co/spaces/Qwen/Qwen2-72B-Instruct

## Trang 57

**Triển khai mô hình lớn (gọi qua API)**

❑ Gọi qua code:
❑ Chuẩn bị môi trường (tùy chọn):
⚫ Công cụ phát triển VS Code: https://code.visualstudio.com/
⚫ Quản lý môi trường Python bằng Miniconda:
https://docs.anaconda.com/free/minicond
a/miniconda-install

## Trang 58

**Triển khai mô hình lớn (triển khai cục bộ)**

❑ Nền tảng mã nguồn mở triển khai cục bộ mô hình lớn: Ollama, LM Studio
❑ Gọi qua Web và API: OpenAI, Dashscope API
❑ Triển khai cục bộ riêng tư hóa mô hình lớn: Flask, MindIE

https://lmstudio.ai/
https://ollama.com/

## Trang 59

**Triển khai mô hình lớn (triển khai cục bộ)**

❑ Yêu cầu cấu hình: yêu cầu VRAM (bộ nhớ đệm hiển thị); yêu cầu ổ cứng
(bảng yêu cầu không trích được giá trị — xem slide gốc)

## Trang 60

**Triển khai mô hình lớn (triển khai cục bộ)**

❑ 1. Cài đặt Ollama
⚫ Truy cập trang web chính thức: mở trình duyệt, truy cập trang web chính thức của Ollama
⚫ Chọn phiên bản: chọn gói cài đặt tương ứng theo hệ điều hành của bạn. Ollama hỗ trợ MacOS, Linux và Windows
⚫ Tải gói cài đặt: nhấn nút Download, tải gói cài đặt Ollama phù hợp với thiết bị của bạn
⚫ Cài đặt Ollama: tùy theo định dạng gói cài đặt đã tải, chạy chương trình cài đặt hoặc giải nén tệp vào thư mục bạn chọn
❑ 2. Chạy mô hình cụ thể (ollama run qwen2:7b)

## Trang 61

**Triển khai mô hình lớn (triển khai cục bộ)** (nội dung lặp lại trang 60 — xem slide gốc)

❑ 1. Cài đặt Ollama
❑ 2. Chạy mô hình cụ thể (ollama run qwen2:7b)

## Trang 62

**Triển khai mô hình lớn (triển khai cục bộ)** (lặp lại trang 61, kèm bổ sung nâng cao)

❑ 1. Cài đặt Ollama
❑ 2. Chạy mô hình cụ thể (ollama run qwen2:7b)

Nâng cao:
1. Cấu hình WebUI bằng open web UI
2. Xây dựng kho tri thức cục bộ dựa trên AnythingLLM

## Trang 63

**Mục lục** (lặp lại trang 2)

## Trang 64

**Mở rộng khái niệm mô hình lớn**

(sơ đồ ba nhánh — nhãn trên sơ đồ: "Mô hình lớn theo lĩnh vực" (trái), "Mô hình lớn đa phương tiện" (giữa), "Tác tử mô hình lớn" (phải); mỗi nhánh gồm các nút: "Người dùng", "Mô hình lớn" (nhánh phải là "Tác tử"), "Dữ liệu lĩnh vực" / "Dữ liệu đa phương tiện" / "Môi trường")

## Trang 65

**Mô hình lớn theo lĩnh vực (垂域大模型)**

❑ Paradigm cơ bản: tăng cường huấn luyện theo lĩnh vực trên nền mô hình lớn tổng quát, tính chuyên môn cao, tốc độ triển khai nhanh, hiệu quả chi phí cao, tính tuân thủ tốt
❑ Cách thức huấn luyện: huấn luyện bằng dữ liệu lĩnh vực (tiếp tục tiền huấn luyện, fine-tuning, prompt), retrieval-augmented v.v.
❑ Lĩnh vực phổ biến: giáo dục, y tế, pháp luật, tài chính v.v.

[1] Ling, Chen, et al. Domain specialization as the key to make large language models disruptive: A comprehensive survey. arXiv preprint arXiv:2305.18703.

## Trang 66

**Phát triển tiên phong của mô hình lớn đa phương tiện**

A Survey on Multimodal Large Language Models (https://arxiv.org/pdf/2306.13549)

❑ Đột phá năng lực của mô hình lớn đa phương tiện, trở thành xu hướng và trọng điểm mới của phát triển tiên phong mô hình lớn
❑ Mở rộng đáng kể ranh giới năng lực và kịch bản ứng dụng của mô hình lớn, động lực then chốt tiếp theo cho bước nhảy vọt về trí tuệ

## Trang 67

**Ví dụ năng lực của mô hình lớn đa phương tiện**

(trang chỉ có minh họa — ví dụ năng lực đa phương tiện, không trích được chữ — xem slide gốc)

## Trang 68

**Phát triển tiên phong của mô hình lớn đa phương tiện**

Tóm tắt công nghệ:
- Mục tiêu chính: học tập dựa trên dữ liệu lớn và phản hồi con người, tương tác với người dùng qua hội thoại, có thể xử lý thông tin đa phương tiện và đa dạng nhiệm vụ, năng lực suy luận sâu và vận dụng tri thức thông thường được nâng cao đáng kể
- Công nghệ then chốt: kiến trúc mô hình đa phương tiện, tuân thủ chỉ dẫn đa phương tiện, suy luận đa phương tiện, triển khai nhẹ (lightweight), căn chỉnh đa phương tiện v.v.

Các sự kiện mốc:
2023-03-15: OpenAI công bố mô hình hội thoại đa phương tiện GPT-4
2023-09-20: OpenAI công bố mô hình sinh ảnh từ văn bản DALL·E 3
2023-09-25: ChatGPT tích hợp toàn diện năng lực đa phương tiện
2023-12-06: Google công bố mô hình đa phương tiện Gemini
2024-03-04 : Anthropic công bố mô hình đa phương tiện Claude 3
2024-05-13: OpenAI công bố mô hình đa phương tiện gốc GPT-4o

Thay đổi của paradigm làm việc (sơ đồ): "Mô hình ngôn ngữ lớn" (đầu vào: văn bản; đầu ra: văn bản) → "Mô hình lớn đa phương tiện" (đầu vào và đầu ra: văn bản, video, giọng nói, hình ảnh, …)

[1] Fei, Hao, et al. From Multimodal LLM to Human-level AI: Modality, Instruction, Reasoning and Beyond. ACM MM, 2024.
https://mllm2024.github.io/ACM-MM2024/

## Trang 69

**Phát triển tiên phong của mô hình lớn đa phương tiện**

❑ Chế độ làm việc tổng quát: mã hóa đa phương tiện > mô-đun dung hợp đặc trưng > bộ giải mã đa phương tiện, hỗ trợ đầu vào và sinh đa phương tiện
❑ Phương tiện phổ biến: văn bản, hình ảnh, video, giọng nói v.v.

[1] Zhang, Duzhen, et al. Mm-llms: Recent advances in multimodal large language models. arXiv preprint arXiv:2401.13601.

## Trang 70

**Kiến trúc tiêu biểu của mô hình lớn đa phương tiện**

Kiến trúc đa phương tiện tích hợp nhất thể (loại kiến trúc của đa số mô hình lớn đa phương tiện):
(sơ đồ: Người dùng → "Bộ mã hóa" — "Bộ mã hóa đa phương tiện" — văn bản/đa phương tiện → đầu vào đa phương tiện → "Bộ giải mã" — "Bộ giải mã đa phương tiện" → văn bản/đa phương tiện → đầu ra đa phương tiện → "Mô-đun hạ du" × nhiều)

Kiến trúc lấy LLM làm trung tâm (nhiều "LLM" + "Mô-đun hạ du" × nhiều):
⊹ Visual-ChatGPT
⊹ HuggingGPT
⊹ MM-REACT
⊹ LLaVA-Plus
⊹ …

## Trang 71

**Tutorial tiên phong về mô hình lớn đa phương tiện (CVPR & MM & COLING)**

https://mllm2024.github.io/CVPR2024
Bài giảng + video

## Trang 72

**Tác tử mô hình lớn (大模型智能体)**

"Jarvis" hiện diện khắp mọi nơi — tác tử mô hình lớn thể hiện triển vọng ứng dụng rộng rãi

OpenAI Operator — https://openai.com/index/introducing-operator
Anthropic Claude — https://www.anthropic.com/claude
Manus AI — https://manus.im/

## Trang 73

**Tác tử mô hình lớn**

❑ Hệ thống được xây dựng dựa trên mô hình lớn, có thể tự chỉ dẫn động quy trình và việc sử dụng công cụ của chính mình, đồng thời điều chỉnh thao tác dựa trên phản hồi thời gian thực¹

(sơ đồ: "(Phương tiện) mô hình ngôn ngữ lớn" là "Nhà cung cấp năng lực tổng quát" — ⚫ xử lý chuỗi dài, ⚫ suy luận chuỗi suy nghĩ (CoT), ⚫ hiểu ý định rộng — ← "Người dùng" / "Mô hình lớn"; "Mô hình lớn (hệ thống)" là "Tác tử" — Người dùng ↔ Tác tử ↔ Môi trường)

❑ Sở hữu năng lực tự chủ và tiến hóa
⚫ Tương tác môi trường: cảm nhận hiểu, lập kế hoạch quyết định, hành động thực thi
⚫ Vận hành bền bỉ: phản tư tối ưu, tiến hóa lặp lại, phòng vệ an toàn
❑ Cập nhật tri thức: kho tri thức, kho kinh nghiệm
❑ Tích hợp công cụ: APP, API, hàm
❑ Nhà cung cấp năng lực tổng quát
⚫ Xử lý chuỗi dài
⚫ Suy luận chuỗi suy nghĩ (CoT)
⚫ Hiểu ý định rộng

1Anthropic. Building effective agents. Published Dec 19, 2024

## Trang 74

**Tác tử mô hình lớn**

Soạn xếp workflow (giống orchestrated workflow):
- Sắp xếp LLM và công cụ qua các đường dẫn định nghĩa trước, giống script tự động hóa phức tạp, thường hiện thực bằng cách prompt

Nền tảng tác tử (tác tử):
- Tự chỉ dẫn động quá trình hành vi và việc dùng công cụ, lập kế hoạch và cập nhật đường dẫn một cách động, giữ quyền kiểm soát cách hoàn thành nhiệm vụ; thường mở rộng năng lực bằng cách huấn luyện
- Xem AI như một thành phần có thể sắp xếp
- Trao cho AI tính tự chủ lớn hơn, có thể tiến hóa

## Trang 75

**Đột phá ranh giới năng lực của mô hình lớn**

❑ Đột phá năng lực của tác tử mô hình lớn, trở thành trọng điểm mới, mở rộng đáng kể ranh giới năng lực và kịch bản ứng dụng của mô hình lớn

Thang năng lực:
- L1: Chatbots — GPT-4, DeepSeek-V3 — giao tiếp ngôn ngữ tổng quát — ứng dụng: hỏi đáp, hội thoại, tìm kiếm
- L2: Reasoners — o1, DeepSeek-R1 — suy nghĩ suy luận sâu — ứng dụng: toán, suy luận logic
- L3: Agents — Operator, Deep Research — hành động và tương tác tự chủ — ứng dụng: tool calling, điều khiển, khám phá
- L4: Innovators — đổi mới và phát minh
- L5: Organizations — tổ chức và quản lý

Ngôn ngữ → hành động: từ trí tuệ nội dung đến trí tuệ hành vi, xây dựng sợi dây liên kết then chốt tiến tới trí tuệ nhân tạo tổng quát

## Trang 76

**Tài liệu đọc thêm**

《大模型开发全流程》 (Toàn bộ quy trình phát triển mô hình lớn)
https://www.hiascend.com/edu/growth/lm-development
Khóa học mô hình lớn nội địa hóa: 54 bài học, 26 sổ tay thực hành

## Trang 77

**Cảm ơn!**

zhangzs@sjtu.edu.cn
https://bcmi.sjtu.edu.cn/~zhangzs
