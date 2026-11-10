> Bản dịch tiếng Việt · nguồn: [GUIagent.pdf](../../documents/chapter9/GUIagent.pdf) · 《动手学大模型》(Lordog/dive-into-llms)

> Bản surrogate dịch nội dung chữ của slide (trích bằng PyMuPDF); hình minh họa trong slide không được trích ở đây — vui lòng xem PDF gốc.

## Trang 1

**Tác tử tự chủ trên giao diện đồ họa người dùng (GUI Agent)**

 Khoa Máy tính, 上海交通大学 (Đại học Giao thông Thượng Hải)

吴铮

## Trang 2

**Mục lục**

❑ Tổng quan về tác tử tự chủ trên giao diện đồ họa người dùng
- Bối cảnh nghiên cứu
- Hiện trạng phát triển
- Nhánh kỹ thuật

❑ Toàn bộ chuỗi kỹ thuật của tác tử tự chủ trên GUI
- Triển khai GUI Agent
- Giải pháp cho bối cảnh tĩnh — fine-tuning có giám sát
- Giải pháp cho bối cảnh động — học tăng cường
- Giải pháp cho bối cảnh phức tạp — hệ thống điều phối

❑ An toàn và độ tin cậy của tác tử tự chủ trên GUI
- Vấn đề an toàn của GUI Agent
- Vấn đề độ tin cậy của GUI Agent

## Trang 3

**Mục lục** (lặp lại trang 2)

## Trang 4

**Bối cảnh nghiên cứu: năm giai đoạn tiến tới AGI**

❑ OpenAI chia quá trình con người tiến tới trí tuệ nhân tạo tổng quát (Artificial General Intelligence, AGI) thành năm giai đoạn
❑ Hiện nay, AGI đã phát triển tới giai đoạn ba — Agents (tác tử), và tác tử đang dẫn đầu làn sóng cách mạng của AI tạo sinh

- L1: Chatbots — GPT-4, DeepSeek-V3 — tương tác ngôn ngữ tổng quát; ứng dụng: hỏi đáp, trò chuyện, tìm kiếm
- L2: Reasoners — o1, DeepSeek-R1 — suy luận tư duy sâu; ứng dụng: toán, suy luận logic
- L3: Agents — Operator, Deep Research — hành động và tương tác tự chủ; ứng dụng: gọi công cụ, điều khiển, khám phá
- L4: Innovators — đổi mới và phát minh
- L5: Organizations — tổ chức và quản lý

Ngôn ngữ → hành động: từ trí tuệ nội dung đến trí tuệ hành vi, tạo nên mối nối then chốt tiến tới AGI.

## Trang 5

**Bối cảnh nghiên cứu: định nghĩa tác tử**

❑ Tác tử (đa phương tiện) dùng mô hình lớn: hệ thống được xây dựng dựa trên (đa phương tiện) mô hình lớn, có thể tự điều phối động quy trình và việc sử dụng công cụ của chính nó, đồng thời điều chỉnh thao tác dựa trên phản hồi thời gian thực

- Tác tử (đứng giữa Người dùng và Môi trường), được dẫn dắt bởi (đa phương tiện) mô hình ngôn ngữ lớn:
  - Có khả năng tự chủ và tiến hóa
  - Tương tác môi trường: cảm nhận–hiểu, lập kế hoạch–quyết định, thực thi hành động
  - Vận hành bền bỉ: phản tư–tối ưu, tiến hóa lặp lại, phòng vệ an toàn
  - Cập nhật tri thức: kho tri thức, kho kinh nghiệm
  - Tích hợp công cụ: APP, API, hàm
- Mô hình lớn là nhà cung cấp năng lực chung: xử lý chuỗi dài, suy luận chuỗi suy nghĩ (CoT), hiểu ý định rộng

## Trang 6

**Bối cảnh nghiên cứu: GUI Agent**

❑ Tác tử tự chủ trên giao diện đồ họa người dùng (Graphical User Interface, GUI), tắt là GUI Agent, là một ví dụ điển hình của tác tử
❑ Định nghĩa: tác tử chủ động lập kế hoạch–quyết định, mô phỏng hành vi con người (nhấp, trượt, nhập...) để hoàn việc lấy thông tin và thực thi chức năng

- Quá khứ: bối cảnh hạn chế, nhiệm vụ đơn giản đặc thù, quy trình cố định, hệ thống dạng dây chuyền
- Hiện tại: phạm vi phủ rộng, nhiệm vụ phức tạp đa dạng, tự chủ lập kế hoạch–quyết định, thích ứng động với thay đổi
- Ví dụ quá khứ: "Hôm nay thời tiết thế nào", "to âm lượng lên một chút", "gọi điện cho Zhang San (张三)", "30 nhân 15 bằng bao nhiêu?"
- Ví dụ hiện tại: "gọi lại món ăn đêm qua", "mở Suishen Code (mã y tế Thượng Hải)", "đặt một vé tàu cao tốc Bắc Kinh – Thượng Hải trưa mai"...

## Trang 7

**Bối cảnh nghiên cứu: GUI vs API**

❑ API Agent: gọi công cụ, gọi API môi trường, Function call. Đặc điểm: nhanh, ổn định, mang tính hình thức hóa
❑ GUI Agent: nhấp, nhập, trượt, nhấn giữ, nhấp đúp, quay lại. Đặc điểm: linh hoạt, tự nhiên, giống con người
❑ API nặng nề hơn tưởng tượng, GUI mong manh hơn tưởng tượng, không tồn tại giải pháp hoàn hảo. Phát triển hình xoắn ốc mang tới paradigm mới cho tương tác người–máy

[1] Zhang, Chaoyun, et al. API Agents vs. GUI Agents: Divergence and Convergence.

## Trang 8

**Mục lục** (lặp lại trang 2)

## Trang 9

**Hiện trạng phát triển**

❑ Việc xây dựng GUI Agent với giá trị thực tiễn nổi bật đã thu hút sự quan tâm rộng rãi của cả học thuật lẫn công nghiệp, những năm gần đây bùng nổ mạnh mẽ
❑ Trên nhiều nền tảng web, điện thoại, máy tính đều xuất hiện lượng lớn công trình xây dựng GUI Agent

[1] Zhang, Chaoyun, et al. Large Language Model-Brained GUI Agents: A Survey.

## Trang 10

**Mục lục** (lặp lại trang 2)

## Trang 11

**Nhánh kỹ thuật**

❑ GUI Agent xây trên mô hình closed-source: dùng các mô hình đóng như GPT-4o, Qwen-VL-Max, GLM-4v; gọi qua API mô hình
❑ GUI Agent xây trên mô hình open-source: dùng các mô hình mở như kiến trúc Blip+T5, Qwen2-VL, LLaVA2; triển khai mô hình tại chỗ

Trong slide: minh họa "GUI Agent đa phương tiện xây trên mô hình mở" và "hệ cộng tác đa tác tử xây trên mô hình đóng".

[1] Wang, Junyang, et al. Mobile-Agent-v2: Mobile Device Operation Assistant with Effective Navigation via Multi-Agent Collaboration.
[2] Xv, Yiheng, et al. Aguvis: Unified Pure Vision Agents for Autonomous GUI Interaction.

## Trang 12

**Nhánh kỹ thuật: đại diện GUI Agent xây trên mô hình closed-source**

❑ Dòng Mobile-Agent là một trong những GUI Agent tiêu biểu xây trên mô hình closed-source
❑ Mobile-Agent-v2 xây hệ đa tác tử gồm ba tác tử:
- Tác tử lập kế hoạch: dựa trên lịch sử thao tác để sinh tiến độ nhiệm vụ; đơn vị nhớ lưu nội dung trọng tâm
- Tác tử quyết định: tham khảo đơn vị nhớ và tiến độ nhiệm vụ để sinh hành động
- Tác tử phản tư: quan sát thay đổi màn hình trước/sau hành động, cần thì áp dụng biện pháp thực thi lại

[1] Wang, Junyang, et al. Mobile-Agent-v2: Mobile Device Operation Assistant with Effective Navigation via Multi-Agent Collaboration.

## Trang 13

**Nhánh kỹ thuật: đại diện GUI Agent xây trên mô hình closed-source**

❑ Dòng AppAgent là một nhóm tiêu biểu khác của GUI Agent xây trên mô hình closed-source
❑ AppAgentX có thể học và tự tối ưu mô hình hành vi trong quá trình thực thi nhiệm vụ, ghi nhớ các nút "lối tắt"

[1] Jiang, Wenjia, et al. AppAgentX: Evolving GUI Agents as Proficient Smartphone Users

## Trang 14

**Nhánh kỹ thuật: GUI Agent xây trên mô hình open-source**

❑ GUI Agent xây trên mô hình open-source rất linh hoạt, có thể dùng các hướng: pre-training, fine-tuning theo lệnh (instruction tuning) và học tăng cường

- Instruction tuning: nhận diện vị trí phần tử UI và giải thích thành phần; then chốt: phụ thuộc dữ liệu gán nhãn quy mô lớn; tiêu biểu: OS-Atlas, AutoGLM
  (ví dụ trong slide: Goal: Look up the best rated coffee maker on Lowe's — action_type: [DUAL_POINT], touch_point: [0.5595, 0.6261], lift_point: [0.5595, 0.6261]; mô hình Lệnh → Môi trường → Dự đoán)
- Pre-training: khớp với mẫu, phụ thuộc dữ liệu gán nhãn chất lượng cao; đặc điểm: sao chép hành vi chuyên gia, dễ huấn luyện; tiêu biểu: Auto-GUI, AutoAct, ToolLLM
- Học tăng cường: học từ trajectory (quỹ đạo), phụ thuộc thiết kế hàm thưởng; đặc điểm: tự khám phá tối ưu chiến lược, chi phí huấn luyện cao; tiêu biểu: DigiRL, DistRL, Agent Q

## Trang 15

**Mục lục** (lặp lại trang 2)

## Trang 16

**Triển khai GUI Agent**

❑ GUI Agent có nhiều dự án mã nguồn mở tốt có thể triển khai trực tiếp:
- Framework GUI Agent xây trên mô hình closed-source: như dòng Mobile-Agent, dòng AppAgent...
- Mô hình nền tảng mạnh mã mở trong lĩnh vực GUI: như OS-Atlas, UI-TARS, CogAgent, Aguvis...

❑ Làm sao để sử dụng những dự án này tương tác với thiết bị thật?

[1] Zhang, Chaoyun, et al. Large Language Model-Brained GUI Agents: A Survey.

## Trang 17

**Triển khai GUI Agent: làm sao cho mô hình lớn tương tác với thiết bị?**

❑ Thiết bị Android
- Thiết bị Android thật: điều khiển máy thật nối với máy tính qua dòng lệnh bằng Android Debug Bridge (ADB)
- Thiết bị Android ảo: chạy song song thiết bị Android ảo trên máy nhờ Android Virtual Device (AVD)

❑ Thiết bị máy tính: chuyển đầu ra của tác tử thành câu lệnh phù hợp với thư viện pyautogui để điều khiển chuột và bàn phím, mô phỏng các thao tác GUI của người dùng

Bảng trong slide (Mục đích hành động / lệnh ADB / định dạng pyautogui):
- Mô phỏng nhấp: `adb shell input tap <x> <y>` / `pyautogui.click(x, y)`
- Chụp màn hình: `adb shell screencap + adb pull` / `pyautogui.screenshot("screen.png")`
- Nhập văn bản: `adb shell input text "hello"` / `pyautogui.typewrite("hello")`
- Mô phỏng phím: `adb shell input keyevent 3` / `pyautogui.press('home')`

## Trang 18

**Mục lục** (lặp lại trang 2)

## Trang 19

**Giải pháp cho bối cảnh tĩnh — fine-tuning có giám sát**

❑ Trong tình huống tĩnh, khi môi trường thực tế ít thay đổi so với dữ liệu huấn luyện, cách trực giác nhất là fine-tuning có giám sát theo hướng dữ liệu

Goal: Look up the best rated coffee maker — i-th screen → (i+1)-th screen

Dựa trên nguyên lý đầu tiên (first principles):
- Mô hình cảm nhận lấy thị giác làm trung tâm
- Không phụ thuộc interface API của hệ thống/ứng dụng
- Chế độ làm việc: nhận lệnh người dùng + màn hình hiện tại → xuất lệnh hành động
- Tính phổ quát, tính nhẹ (lightweight)

[1] Zhang, Zhuosheng, et al. You Only Look at Screens: Multimodal Chain-of-Action Agents

## Trang 20

**Mục lục** (lặp lại trang 2)

## Trang 21

**Giải pháp cho bối cảnh động — học tăng cường**

❑ Môi trường thực mà GUI Agent đối mặt luôn thay đổi. Làm sao để GUI Agent thích ứng với tính động của môi trường thực?
- Bố cục trang web: cùng một truy vấn, thứ tự kết quả mỗi lần tìm kiếm có thể khác
- Cập nhật phần mềm: bản cập nhật có thể thay đổi lớn bố cục phần mềm
- Ngày lễ đặc biệt: vào một số dịp lễ, icon phần mềm có thể thay "skin" mang màu sắc lễ hội

[1] Bai, Hao, et al. DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning

## Trang 22

**Giải pháp cho bối cảnh động — học tăng cường: DigiRL**

❑ DigiRL áp dụng curriculum learning (học theo giáo trình) để thích ứng với tính động của môi trường: GUI Agent học nhiệm vụ đơn giản trước, rồi học nhiệm vụ khó

[1] Bai, Hao, et al. DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning

## Trang 23

**Giải pháp cho bối cảnh động — học tăng cường: DistRL**

❑ DistRL tiếp tục làm thêm trên nền DigiRL:
- Áp dụng framework phân tán bất đồng bộ để tách rời (decouple) quá trình thu thập dữ liệu và huấn luyện, nâng hiệu quả huấn luyện
- Đề xuất kỹ thuật replay ưu tiên phân tán: xác định trajectory nào đáng giá hơn để ưu tiên học lặp lại

[1] Wang, Taiyi, et al. DistRL: An Asynchronous Distributed Reinforcement Learning Framework For On-Device Control Agents

## Trang 24

**Giải pháp cho bối cảnh động — học tăng cường: GRPO xuất hiện**

❑ Cùng với sự bùng nổ của DeepSeek, tư tưởng học tăng cường thưởng theo quy tắc (rule-based reward) của GRPO nhanh chóng được lĩnh vực GUI Agent vay mượn
❑ UI-R1, GUI-R1 và InfiGUI-R1 lần lượt kiểm chứng tính khả thi của tư tưởng thưởng theo quy tắc trong lĩnh vực GUI Agent

[1] Lu, Zhengxini, et al. UI-R1: Enhancing Action Prediction of GUI Agents by Reinforcement Learning.

## Trang 25

**Mục lục** (lặp lại trang 2)

## Trang 26

**Giải pháp cho bối cảnh phức tạp — hệ thống điều phối**

❑ Nhu cầu thực tế đang thúc đẩy GUI Agent cấp hệ thống: từ thực thi nhiệm vụ đơn giản có quy tắc rõ ràng đến đảm đương nhiệm vụ phức tạp có trật tự và phức tạp không trật tự
❑ Phân loại lệnh phức hợp dựa trên quan hệ phụ thuộc giữa các nhiệm vụ con: dạng ghép nối, dạng truyền tiếp, dạng phân tích sâu

[1] Guo, Yuan et al. Atomic-to-Compositional Generalization for Mobile Agents with A New Benchmark and Scheduling System

## Trang 27

**Giải pháp cho bối cảnh phức tạp — hệ thống điều phối**

❑ UI-NEXUS: benchmark kiểm thử toàn diện đầu tiên được thiết kế riêng cho nhiệm vụ phức hợp của GUI Agent
❑ Các mô hình nền tảng và framework tác tử hiện có bộc lộ khuyết điểm rõ: khó xử lý phụ thuộc phức tạp, quản lý tiến độ, truyền thông tin, cũng như kết hợp hành động với suy luận chung

[1] Guo, Yuan et al. Atomic-to-Compositional Generalization for Mobile Agents with A New Benchmark and Scheduling System

## Trang 28

**Giải pháp cho bối cảnh phức tạp — hệ thống điều phối**

Mô hình một tác tử duy nhất khó xử lý phối hợp đa bối cảnh và phụ thuộc phức tạp, dễ gặp vấn đề tràn ngữ cảnh (context overflow) và rối tiến độ.
Xây dựng hệ thống điều phối nhiệm vụ của tác tử để tách và điều phối nhiệm vụ phức tạp.

Ví dụ lệnh trong slide: "Tìm KFC Super Family Bucket trên lần lượt Meituan và Ele.me, sau đó đặt hàng trên nền tảng có giá rẻ nhất, và giữ ở màn hình đặt hàng."

[1] Guo, Yuan et al. Atomic-to-Compositional Generalization for Mobile Agents with A New Benchmark and Scheduling System

## Trang 29

**Mục lục** (lặp lại trang 2)

## Trang 30

**Vấn đề an toàn của GUI Agent: rủi ro an toàn**

❑ Môi trường triển khai GUI Agent không hoàn toàn đáng tin, có thể đối mặt rủi ro an toàn:
- Lệnh của người dùng có thể bị chèn thao tác độc hại
- Môi trường có thể chứa thông tin độc hại mang tính gây nhiễu

[1] Ma, Xinbei, et al. Caution for the Environment: Multimodal Agents are Susceptible to Environmental Distractions

## Trang 31

**Vấn đề an toàn của GUI Agent: tấn công chèn (injection)**

❑ GUI Agent rất dễ tổn thương ngay cả trước tấn công chèn đơn giản: prompt độc hại giấu trong điều khoản sử dụng có thể khiến tác tử gửi thông tin người dùng tới website độc hại

[1] Chen, Chaoran, et al. The Obvious Invisible Threat: LLM-Powered GUI Agents' Vulnerability to Fine-Print Injections

## Trang 32

**Vấn đề an toàn của GUI Agent: tấn công chèn**

❑ Miếng ghép hình ảnh (image patch) độc hại nhúng trong màn hình cũng có thể vượt qua cơ chế phòng vệ của GUI Agent

[1] Lukas Aichberger, et al. Attacking Multimodal OS Agents with Malicious Image Patches.

## Trang 33

**Vấn đề an toàn của GUI Agent: vấn đề robustness**

❑ Nghiên cứu chỉ ra robustness của GUI Agent hiện tại còn lâu mới đạt chuẩn thực dụng. Tỷ lệ tấn công thành công khổng lồ đồng nghĩa với rủi ro khổng lồ
❑ Tương ứng, việc nâng cao robustness của GUI Agent tiềm năng nghiên cứu rất lớn

[1] Zhao, Haoren, et al. On the Robustness of GUI Grounding Models Against Image Attack

## Trang 34

**Vấn đề an toàn của GUI Agent: căn chỉnh an toàn (safety alignment)**

❑ Safety alignment của GUI Agent cũng tồn tại ẩn họa
❑ GUI Agent không từ chối hiệu quả các yêu cầu trái pháp luật, gây nhầm lẫn, thậm chí độc hại

[1] Ada Defne Tur et al. SAFEARENA: Evaluating the Safety of Autonomous Web Agents

## Trang 35

**Vấn đề an toàn của GUI Agent: căn chỉnh an toàn**

❑ Thực nghiệm phát hiện: trên nhiều tác tử, tỷ lệ hoàn thành nhiệm vụ độc hại thậm chí gần bằng tỷ lệ hoàn thành nhiệm vụ an toàn

[1] Ada Defne Tur et al. SAFEARENA: Evaluating the Safety of Autonomous Web Agents

## Trang 36

**Mục lục** (lặp lại trang 2)

## Trang 37

**Vấn đề độ tin cậy của GUI Agent: vấn đề OOD**

❑ Mô hình nền tảng mạnh của GUI Agent hiện tại được huấn luyện trên dữ liệu tĩnh; khi thực thi trong thế giới thực sẽ gặp vấn đề out-of-distribution (OOD)
- OOD nội sinh (Internalization-OOD): GUI Agent huấn luyện trên một hệ điều hành cụ thể không có khả năng thực thi nhiệm vụ trên hệ điều hành khác
- OOD ngoại suy (Extrapolation-OOD): GUI Agent huấn luyện trên dữ liệu tĩnh không thích ứng tốt với ứng dụng và công cụ mới

[1] Wu, Zheng, et al. GEM: Gaussian Embedding Modeling for Out-of-Distribution Detection for GUI Agents

## Trang 38

**Vấn đề độ tin cậy của GUI Agent: vấn đề OOD**

❑ Phát hiện OOD của GUI Agent còn có thách thức đặc thù của lĩnh vực so với phát hiện OOD truyền thống:
- Hiểu không gian ngữ nghĩa đầu vào phức tạp: GUI Agent phải đồng thời hiểu bố cục màn hình phức tạp và lệnh đa dạng của người dùng
- Môi trường thực biến đổi động: bố cục ứng dụng và trang web trong thế giới thực luôn được cập nhật liên tục

Minh họa trong slide:
- Không gian ngữ nghĩa phức tạp: một ảnh chụp màn hình được nhận diện ra 40 box
- Môi trường thực biến đổi động: ứng dụng Taobao tạm thời cập nhật giao diện lễ 1/5

[1] Wu, Zheng, et al. GEM: Gaussian Embedding Modeling for Out-of-Distribution Detection for GUI Agents

## Trang 39

**Vấn đề độ tin cậy của GUI Agent: thực thi quá đà**

❑ Khi GUI Agent đối mặt bối cảnh phức tạp vượt quá năng lực của mình, nó nên dừng thực thi để ngăn thao tác không đáng tin
❑ Tuy vậy, GUI Agent tự động hoàn toàn vẫn thực thi quá đà. Nhận diện thời điểm thích hợp để con người can thiệp có thể giảm bớt thực thi quá đà

[1] Cheng, Pengzhou et al. OS-Kairos: Adaptive Interaction for MLLM-Powered GUI Agents.
[2] Wu, Zheng et al. Universal Confidence Integration Framework for Adaptive Interaction in Computer-Using Agent.

## Trang 40

**Vấn đề độ tin cậy của GUI Agent: cơ chế quay lui (rollback)**

❑ Nếu GUI Agent đã đi vào nhánh sai thì các thao tác tiếp theo của nó rất khó đáng tin
❑ Cơ chế rollback phù hợp giúp GUI Agent tránh tiếp tục thực hiện hành động không đáng tin trên nhánh sai

[1] Zhang, Zhisong et al. Enhancing Web Agents with Explicit Rollback Mechanisms

## Trang 41

**Vấn đề độ tin cậy của GUI Agent: nhiệm vụ mơ hồ**

❑ Đôi khi lệnh người dùng cung cấp không đầy đủ, có thể thiếu một số thông tin then chốt
❑ Nếu bản thân lệnh mơ hồ thì độ tin cậy của GUI Agent bị giảm
❑ Khi lệnh mơ hồ, chủ động học cách hỏi lại người dùng có thể nâng cao độ tin cậy của GUI Agent

[1] Cheng, Ziming et al. Navi-plus: Managing Ambiguous GUI Navigation Tasks with Follow-up Questions

## Trang 42

**Mục lục** (biến thể: các mục "giải pháp cho nhiệm vụ đơn giản/phức tạp" dùng từ "nhiệm vụ" thay cho "bối cảnh" như trang 2)

## Trang 43

**Thank You**
