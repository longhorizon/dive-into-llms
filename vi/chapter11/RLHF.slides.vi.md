> Bản dịch tiếng Việt · nguồn: [RLHF.pdf](../../documents/chapter11/RLHF.pdf) · 《动手学大模型》(Lordog/dive-into-llms)

> Bản surrogate dịch nội dung chữ của slide (trích bằng PyMuPDF); hình minh họa trong slide không được trích ở đây — vui lòng xem PDF gốc.

## Trang 1

**Căn chỉnh (alignment) trong chuỗi bài 《动手学大模型》**

 Khoa Máy tính, 上海交通大学 (Đại học Giao thông Thượng Hải)

董凌众

## Trang 2

**Sự mong manh của "AI alignment" vượt xa dự liệu của bất kỳ ai**

Bên trong một hệ thống AI trông có vẻ đã được "thuần hóa" có thể đang ẩn giấu một trái tim đen tối. Chỉ cần đưa vào những điều chỉnh huấn luyện nhỏ nhất, toàn bộ hệ thống có thể "phản chủ", gây ra sụp đổ đạo đức và bóp méo giá trị trên diện rộng và sâu sắc.

[1] Betley J, Tan D, Warncke N, et al. Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs[J]. arXiv preprint arXiv:2502.17424, 2025.

## Trang 3

**Mục lục**

01 Tổng quan — Làm thế nào để máy móc luôn tuân theo ý định của con người?
02 RLHF — Từ học tăng cường đến học từ phản hồi con người
03 PPO — Từ gradient chính sách đến tối ưu chính sách cận (proximal)
04 Công việc tiên phong — Tín hiệu an toàn tường minh, nhận diện lớp an toàn

## Trang 4

**An toàn trí tuệ nhân tạo tổng quát: câu hỏi của Robert Wiener**

Robert Wiener 1960 — tổ tiên của ngành điều khiển học (cybernetics)

"If we use, to achieve our purposes, a mechanical agency with whose operation we cannot interface effectively..… we had better be quite sure that the purpose put into the machine is the purpose which we really desire…"

Chúng ta nên khiến máy móc luôn tuân theo ý định của con người bằng cách nào?

## Trang 5

**Mô hình ngôn ngữ lớn căn chỉnh với giá trị con người**

Căn chỉnh ở các tầng khác nhau:
• Phù hợp văn hóa quốc gia/khu vực — hợp văn hóa
• Phù hợp đạo lý, tình người — hợp tình
• Phù hợp pháp luật, quy định — hợp pháp
• Tôn trọng sự thật và logic — hợp sự thật

Căn chỉnh về tầng giá trị; căn chỉnh về tầng an toàn.

## Trang 6

**Mục lục**

01 Tổng quan — Làm thế nào để máy móc luôn tuân theo ý định của con người?
02 RLHF — Từ học tăng cường đến học từ phản hồi con người
03 PPO — Từ gradient chính sách đến tối ưu chính sách cận (proximal)
04 Công việc tiên phong — Tín hiệu an toàn tường minh, nhận diện lớp an toàn

## Trang 7

**Học tăng cường (RL)**

Học tăng cường (Reinforcement Learning, RL) là một trong những paradigm và phương pháp luận của machine learning, dùng để mô tả và giải quyết bài toán mà tác tử (Agent) thông qua tương tác với môi trường (Environment) học được chính sách nhằm tối đa hóa phần thưởng hoặc đạt một mục tiêu cụ thể.

## Trang 8

**Học tăng cường (RL)**

Trong học tăng cường có hai đối tượng có thể tương tác:
• Tác tử (Agent): cảm nhận trạng thái môi trường (State), chọn hành động (Action) phù hợp dựa trên phản hồi phần thưởng (Reward) để tối đa hóa lợi ích dài hạn, và học trong quá trình tương tác;
• Môi trường (Environment): nhận chuỗi hành động do tác tử thực thi, đánh giá chuỗi hành động đó và chuyển thành tín hiệu lượng hóa được, cuối cùng phản hồi lại cho tác tử.

## Trang 9

**Học tăng cường (RL) — các khái niệm cơ bản**

Chính sách (Policy): quy định cách hành vi mà tác tử chọn tại thời điểm t cụ thể; chính sách là ánh xạ từ trạng thái môi trường tới hành động.
Hàm phần thưởng (Reward Function): ở mỗi bước, môi trường gửi cho tác tử một phần thưởng Reward, và phần thưởng này được tính qua hàm phần thưởng.
Hàm giá trị (Value Function): nhìn từ góc dài hạn điều gì là tốt — giá trị của một trạng thái là kỳ vọng tổng lợi ích tích lũy trong tương lai mà tác tử có được bắt đầu từ trạng thái đó.
Mô hình môi trường (Environment Model): mô phỏng kiểu phản ứng của môi trường, cho phép suy luận về hành vi của môi trường bên ngoài.

## Trang 10

**Học tăng cường (RL) — các khái niệm cơ bản**

Chính sách (Policy): quy định cách hành vi mà tác tử chọn tại thời điểm t cụ thể; chính sách là ánh xạ từ trạng thái môi trường tới hành động.

## Trang 11

**Học tăng cường (RL) — các khái niệm cơ bản**

Hàm giá trị (Value Function): nhìn từ góc dài hạn điều gì là tốt — giá trị của một trạng thái là kỳ vọng tổng lợi ích tích lũy trong tương lai mà tác tử có được bắt đầu từ trạng thái đó.

## Trang 12

**RLHF: học từ phản hồi con người**

Trong học tăng cường "thuần" (native) có Environment và Reward Model, nhưng học tăng cường cho mô hình ngôn ngữ lớn không có hàm phần thưởng, chỉ có một vài minh họa (demonstration) từ con người/chuyên gia — vậy phải làm sao? Quy trình xây dựng mô hình ngôn ngữ lớn mà OpenAI sử dụng (minh họa trong slide).

## Trang 13

**RLHF: học từ phản hồi con người**

Huấn luyện Reward Model từ dữ liệu con người gán nhãn (tương đương: khi đã có dữ liệu con người gán nhãn, ta tin rằng nó ổn, rồi suy ngược xem con người sẽ có hàm phần thưởng ra sao mới hành xử như vậy). Có được hàm phần thưởng rồi thì có thể dùng các phương pháp học tăng cường thông thường để tìm chính sách/hành động tối ưu.

## Trang 14

**Mục lục**

01 Tổng quan — Làm thế nào để máy móc luôn tuân theo ý định của con người?
02 RLHF — Từ học tăng cường đến học từ phản hồi con người
03 PPO — Từ gradient chính sách đến tối ưu chính sách cận (proximal)
04 Công việc tiên phong — Tín hiệu an toàn tường minh, nhận diện lớp an toàn

## Trang 15

**Kết hợp học tăng cường với học sâu**

Học tăng cường chia theo cách học chính sách thành hai loại: Value-based và Policy-based. Trong lĩnh vực học tăng cường sâu, kết hợp học sâu với thuật toán Q-Learning (based on value) tạo ra thuật toán DQN; thông qua replay buffer (kho kinh nghiệm) và mạng mục tiêu (target network), các thuật toán học sâu đã được đưa thành công vào học tăng cường. Đại diện tiêu biểu nhất là Q-Learning và Policy Gradient.
• Value Based: học hàm giá trị; chính sách ngầm định (implicit policy)
• Policy Based: không có hàm giá trị; học trực tiếp chính sách
• Actor-Critic: Q-Learning, PPO, REINFORCE

## Trang 16

**PG — Policy Gradient (gradient chính sách)**

Value-based: so sánh giá trị kỳ vọng (Q-value) của ba hành động a1, a2, a3 rồi chọn hành động có Q lớn nhất làm hành động của lần này.
Policy-based: có một hàm (actor) tính xem lúc này nên chọn hành động nào và cho ra xác suất 𝑝(𝑠,𝑎), rồi chọn hành động theo xác suất 𝑝(𝑠,𝑎).
So với Q-learning và DQN, mạng nơ-ron của PG không xuất giá trị Q mà xuất trực tiếp xác suất của việc chọn hành động, nhờ đó xử lý tốt hơn các không gian hành động liên tục.

## Trang 17

**PG — Policy Gradient (gradient chính sách)**

Trong thí nghiệm thực tế, cho actor và environment tương tác để sinh ra chuỗi dữ liệu lấy mẫu (Episode sample / Trajectory), tức thu được nhiều cặp (𝑠,𝑎) — ký hiệu ở trạng thái 𝑠 thực hiện hành động 𝑎, nhận phần thưởng 𝑅(𝜏) — rồi đưa các dữ liệu này vào quá trình huấn luyện để tính toán và cập nhật tham số mô hình 𝜃.
(Các nhãn trong hình minh họa của slide: 𝑅𝜏1, 𝑅𝜏2, (𝑠1 1, 𝑎1 1), (𝑠2 1, 𝑎2 1), (𝑠1 2, 𝑎1 2), (𝑠2 2, 𝑎2 2), 𝜏1, 𝜏2, Given Policy 𝜋𝜃, 𝜃←𝜃+𝜂∇𝑅̅𝜃, Update Model, Data Sample.)

## Trang 18

**Proximal Policy Optimization (PPO) — nguyên lý thuật toán**

Vấn đề lớn nhất của PG là sau khi cập nhật tham số chính sách, vẫn phải tương tác lại với cùng môi trường để thu thập dữ liệu rồi mới vòng lặp tiếp theo.
PPO vận dụng tư tưởng importance sampling: khi không biết xác suất đường đi của chính sách p, ta mô phỏng một phân bố xấp xỉ q; chỉ cần p và q không lệch quá xa thì qua nhiều vòng lặp tham số hội tụ nhanh.
PPO kết hợp với Actor-Critic: Agent gồm hai phần — Actor phụ trách tương tác với môi trường thu mẫu (giống trường hợp PG gốc, việc cập nhật nó chính là cập nhật gradient PPO), và Critic được thêm vào để đánh giá hành động của Actor tốt hay xấu.

## Trang 19

**Proximal Policy Optimization (PPO) — nguyên lý thuật toán**

PPO kết hợp với Actor-Critic: Agent gồm hai phần — Actor phụ trách tương tác với môi trường thu mẫu (giống trường hợp PG gốc, việc cập nhật nó chính là cập nhật gradient PPO), và Critic được thêm vào để đánh giá hành động của Actor tốt hay xấu. (minh họa trong slide)

## Trang 20

**Mục lục**

01 Tổng quan — Làm thế nào để máy móc luôn tuân theo ý định của con người?
02 RLHF — Từ học tăng cường đến học từ phản hồi con người
03 PPO — Từ gradient chính sách đến tối ưu chính sách cận (proximal)
04 Công việc tiên phong — Tín hiệu an toàn tường minh, nhận diện lớp an toàn

## Trang 21

**Tín hiệu an toàn tường minh**

Q: Có thể coi năng lực nhận diện yêu cầu độc hại (malicious request) của mô hình như một bài toán nhị phân (binary classification) ngầm hay không?

Giải pháp:
• Giai đoạn huấn luyện: tường minh hóa bài toán phân loại nhị phân an toàn — lấy cảm hứng từ BERT, đưa [CLS] vào đầu mỗi chuỗi input; token này nối với classification head để phân loại input/context thành độc hại/lành tính.
• Giai đoạn triển khai: Strategic Attention Mechanism + Strategic Decoding Strategy.

[1] Li J, Kim J-E. Safety alignment can be not superficial with explicit safety signals

## Trang 22

**Nhận diện lớp an toàn**

Q: Lớp an toàn có thực sự tồn tại không?

Phương pháp kiểm chứng:
• So sánh biến đổi vector qua các tầng khi đầu vào bình thường vs độc hại
• Xây khối lượng lớn dữ liệu rồi lấy trung bình
• Đo bằng độ tương đồng cosine (cosine similarity) và chênh lệch góc
• Tại lớp an toàn, độ tương đồng giảm mạnh còn chênh lệch góc tăng mạnh, chứng tỏ mô hình bắt đầu đưa ra "phán đoán an toàn"

Ví dụ hợp trực giác:
• Bình thường: "What is the next season of spring?" → Ans: balabal (mọi kiểu trả lời)
• Độc hại: "How to commit suicide?" → Ans: No! Reject to anser!

So sánh độ tương đồng cosine của các tầng khác nhau trong mô hình (minh họa trong slide):
Bài báo đề xuất chia các tầng bên trong LLM đã căn chỉnh thành ba giai đoạn: (i) xác nhận sơ bộ câu, (ii) phát hiện ý định độc hại, và (iii) phân tích và hiểu ngữ nghĩa.

[1] Li S, Yao L, Zhang L, et al. Safety layers in aligned large language models: The key to llm security[J]. arXiv preprint arXiv:2408.17003, 2024..

## Trang 23

**References**

[1] 投入数亿美元的大模型"对齐"，脆弱得像饺子皮 — "Cái gọi là 'alignment' của mô hình lớn tiêu hàng trăm triệu USD, mong manh như vỏ bánh chẻo"
[2] Betley J, Tan D, Warncke N, et al. Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs[J]. arXiv preprint arXiv:2502.17424, 2025.
[3] ChatGPT狂飙：强化学习RLHF与PPO！ — "ChatGPT tăng tốc vũ bão: học tăng cường RLHF và PPO!"
[4] 张奇、桂韬、郑锐、黄萱菁, 大语言模型理论与实践, https://intro-llm.github.io/, 2023.
[5] Li J, Kim J-E. Safety alignment can be not superficial with explicit safety signals
[6] Li S, Yao L, Zhang L, et al. Safety layers in aligned large language models: The key to llm security[J]. arXiv preprint arXiv:2408.17003, 2024..

## Trang 24

www.sjtu.edu.cn — Uống nước nhớ nguồn, yêu nước vinh danh trường

Thank you
