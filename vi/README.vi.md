> Bản dịch tiếng Việt · nguồn: [README.md](../README.md) · 《动手学大模型》(Lordog/dive-into-llms)

<p align="center">
<h1 align="center">《动手学大模型》 — loạt hướng dẫn thực hành lập trình về mô hình lớn</h1>
</p>
<p align="center">
  	<a href="https://img.shields.io/badge/version-v0.1.0-blue">
      <img alt="version" src="https://img.shields.io/badge/version-v0.1.0-blue?color=FF8000?color=009922" />
    </a>
  <a >
       <img alt="Status-building" src="https://img.shields.io/badge/Status-building-blue" />
  	</a>
  <a >
       <img alt="PRs-Welcome" src="https://img.shields.io/badge/PRs-Welcome-red" />
  	</a>
    	<a href="https://github.com/Lordog/dive-into-llms/stargazers">
       <img alt="stars" src="https://img.shields.io/github/stars/Lordog/dive-into-llms" />
   	</a>
  	<a href="https://github.com/Lordog/dive-into-llms/network/members">
       <img alt="FORK" src="https://img.shields.io/github/forks/Lordog/dive-into-llms?color=FF8000" />
   	</a>
     <a href="https://github.com/Lordog/dive-into-llms/issues">
       <img alt="Issues" src="https://img.shields.io/github/issues/Lordog/dive-into-llms?color=0088ff"/>
     </a>
     <br />
</p>


<div align="center">
<p align="center">
  <a href="#du-an">Động cơ của dự án</a>/
  <a href="#muc-luc">Mục lục hướng dẫn</a>/
  <a href="#dong-gop">Danh sách người đóng góp</a>
</p>
</div>

<a id="updates"></a>
## 💡 Cập nhật

2025-06-06  Cảm ơn sự quan tâm và những phản hồi tích cực của mọi người! Chúng tôi đã cập nhật bộ hướng dẫn này theo hai phương diện:

- [x] Ra mắt bộ hướng dẫn miễn phí 《大模型开发全流程》 (Quy trình phát triển mô hình lớn) phiên bản nội địa hóa Trung Quốc (kèm slide, sổ tay thực nghiệm và video); xin gửi lời cảm ơn riêng tới sự hỗ trợ từ cộng đồng 华为昇腾 (Huawei Ascend)!
- [x] Cập nhật nội dung trên nền loạt hướng dẫn lập trình thực hành gốc, đồng thời bổ sung các chủ đề mới (suy luận toán học, GUI Agent, căn chỉnh mô hình lớn, giấu tin/steganography, v.v.)!

<a id="du-an"></a>
## 🎯 Động cơ của dự án

Loạt hướng dẫn thực hành lập trình 《动手学大模型》 được mở rộng từ bài giảng của hai môn học tại Đại học Giao thông Thượng Hải (上海交通大学): 《自然语言处理前沿技术》 (Công nghệ biên của xử lý ngôn ngữ tự nhiên, mã môn NIS8021) và 《人工智能安全技术》 (An toàn trí tuệ nhân tạo, mã môn NIS3353), do giảng viên [张倬胜](https://bcmi.sjtu.edu.cn/home/zhangzs/) biên soạn, nhằm cung cấp tài liệu tham khảo lập trình nhập môn về mô hình lớn. Bộ hướng dẫn thuộc tính chất cộng đồng, hoàn toàn miễn phí. Qua những lần thực hành đơn giản, chúng tôi muốn giúp các bạn học sinh, sinh viên nhanh chóng làm quen với mô hình lớn, phục vụ tốt hơn cho thiết kế bài tập lớn hoặc nghiên cứu học thuật.

<a id="muc-luc"></a>
## 📚 Mục lục hướng dẫn

| Nội dung hướng dẫn         | Giới thiệu                                                         | Địa chỉ                                                         |
| ---------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Tinh chỉnh và triển khai       | Hướng dẫn tinh chỉnh và triển khai mô hình tiền huấn luyện: Muốn nâng cao hiệu năng của mô hình tiền huấn luyện trên một nhiệm vụ cụ thể? Hãy chọn mô hình tiền huấn luyện phù hợp, tinh chỉnh trên nhiệm vụ đó, rồi triển khai mô hình đã tinh chỉnh thành một Demo dễ sử dụng! | [[slide](https://github.com/Lordog/dive-into-llms/tree/main/documents/chapter1/dive-into-llm.pdf)] [[hướng dẫn](chapter1/README.vi.md)] [[script](chapter1/dive-tuning.vi.ipynb)] |
| Học theo prompt và chuỗi suy nghĩ (CoT) | Hướng dẫn gọi API và chạy suy luận của mô hình lớn: "AI trực tuyến xin lời động viên? Mô hình lớn trả lời những câu hỏi khiến người ta ngã ngửa, nhưng biết đâu nó chỉ đang cần một câu 「động viên」 mà thôi" | [[slide](https://github.com/Lordog/dive-into-llms/tree/main/documents/chapter2/dive-into-prompting.pdf)] [[hướng dẫn](chapter2/README.vi.md)] [[script](chapter2/dive-prompting.vi.ipynb)] |
| Chỉnh sửa tri thức         | Phương pháp và công cụ chỉnh sửa mô hình ngôn ngữ: Muốn can thiệp vào ký ức của mô hình ngôn ngữ về một tri thức nhất định? Hãy chọn phương pháp chỉnh sửa phù hợp, chỉnh sửa tri thức mục tiêu, rồi kiểm chứng mô hình sau chỉnh sửa! | [[slide](https://github.com/Lordog/dive-into-llms/blob/main/documents/chapter3/dive_edit_0410.pdf)] [[hướng dẫn](chapter3/README.vi.md)]  [[script](chapter3/dive_edit.vi.ipynb)] |
| Suy luận toán học         | Làm sao để mô hình lớn học được suy luận toán học? Hãy cùng chưng cất (distill) nhanh một R1 mini! | [[slide](https://github.com/Lordog/dive-into-llms/blob/main/documents/chapter4/math.pdf)] [[hướng dẫn](chapter4/README.vi.md)]  [[script](chapter4/sft_math.vi.ipynb)] |
| Watermark cho mô hình         | Watermark trên văn bản do mô hình ngôn ngữ tạo ra: gắn vào nội dung do mô hình ngôn ngữ sinh ra những watermark mà mắt thường không nhìn thấy được | [[slide](https://github.com/Lordog/dive-into-llms/blob/main/documents/chapter5/watermark.pdf)] [[hướng dẫn](chapter5/README.vi.md)] [[script](chapter5/watermark.vi.ipynb)] |
| Tấn công jailbreak         | Muốn có an toàn tốt hơn, hãy bắt đầu từ việc học cách tấn công. Hãy tìm hiểu tấn công jailbreak mở miệng mô hình lớn như thế nào! | [[slide](https://github.com/Lordog/dive-into-llms/blob/main/documents/chapter6/dive-Jailbreak.pdf)] [[hướng dẫn](chapter6/README.vi.md)] [[script](chapter6/dive-jailbreak.vi.ipynb)] |
| Giấu tin trong mô hình lớn       | "Mực vô hình"! Bạn muốn mô hình lớn trả lời trôi chảy đồng thời âm thầm mang theo thông tin chỉ "người một nhà" nhận ra được không? Giấu tin (steganography) trong mô hình lớn sẽ trả lời bạn! | [[slide](https://github.com/Lordog/dive-into-llms/blob/main/documents/chapter7/stega.pdf)] [[hướng dẫn](chapter7/README.vi.md)] [[script](https://github.com/Lordog/dive-into-llms/tree/main/documents/chapter7/llm_stega.ipynb)] |
| Mô hình đa phương tiện       | Là mô hình ngôn ngữ lớn đa phương tiện có khả năng mô phỏng thế giới thực đầy đủ hơn, làm thế nào để nó đạt năng lực hiểu và sinh đa phương tiện mạnh hơn? MLLM có thể góp phần hiện thực hóa AGI hay không? | [[slide](https://github.com/Lordog/dive-into-llms/blob/main/documents/chapter8/mllms.pdf)]  [[hướng dẫn](chapter8/README.vi.md)] [[script](chapter8/mllms.vi.ipynb)] |
| Agent GUI        | Muốn "có sẵn cơm ăn", giải phóng đôi tay? Vậy hãy để AI Agent thay bạn gọi đồ ăn, trả lời tin nhắn, so sánh giá khi mua sắm! | [[slide](https://github.com/Lordog/dive-into-llms/blob/main/documents/chapter9/GUIagent.pdf)]  [[hướng dẫn](chapter9/README.vi.md)] [[script](chapter9/GUIagent.vi.ipynb)] |
| An toàn cho agent       | Agent của mô hình lớn đang tiến vào hành trình hệ điều hành tương lai. Tuy nhiên, trong các kịch bản agent mở, mô hình lớn có nhận ra được rủi ro và mối đe dọa hay không? | [[slide](https://github.com/Lordog/dive-into-llms/blob/main/documents/chapter10/dive-into-safety.pdf)] [[hướng dẫn](chapter10/README.vi.md)] [[script](chapter10/agent.vi.ipynb)] |
| Căn chỉnh an toàn bằng RLHF     | Hướng dẫn thực nghiệm RLHF dựa trên PPO: hướng dẫn này rất "nguy hiểm", đọc xong xin hãy kiểm tra xem mô hình lớn của bạn có đang cười lạnh không. | [[slide](https://github.com/Lordog/dive-into-llms/blob/main/documents/chapter11/RLHF.pdf)] [[hướng dẫn](chapter11/README.vi.md)] [[script](chapter11/RLHF.vi.ipynb)] |



<a id="quy-trinh"></a>
## 🔥 Mới ra mắt: 《大模型开发全流程》 nội địa hóa Trung Quốc

- **✨ Bộ hướng dẫn cộng đồng 《大模型开发全流程》 chúng tôi phối hợp cùng 华为昇腾 (Huawei Ascend) đã chính thức ra mắt! Công nghệ biên + thực hành code, cầm tay chỉ việc cùng bạn xoay quanh mô hình lớn AI ✨**: 

  Trên nền loạt hướng dẫn lập trình thực hành 《动手学大模型》 gốc, chúng tôi cùng Huawei phát triển loạt khóa học 《大模型开发全流程》. Loạt hướng dẫn này được phát triển trên nền tảng phần cứng và phần mềm cơ bản của 华为昇腾 (Ascend), bao phủ các dạng tài liệu slide, sổ tay thực nghiệm, video, v.v. Loạt khóa học được chia thành sơ cấp, trung cấp và cao cấp, phục vụ các nhu cầu thực hành mô hình lớn khác nhau; nhằm đưa công nghệ biên vào thực hành code, cung cấp cho bạn đọc và bạn nghiên cứu từ dễ đến khó hướng dẫn toàn trình để nhanh chóng làm quen và ứng dụng các mô hình đã được 华为昇腾 hỗ trợ cũng như quy trình di chuyển, tối ưu mô hình mới.
  
- **🚀 Tới cộng đồng 华为昇腾 để khám phá loạt khóa học 《大模型开发全流程》**: 
  
  👉《[Vùng học quy trình phát triển mô hình lớn](https://www.hiascend.com/edu/growth/lm-development#classification-floor-1)》 @ cộng đồng 华为昇腾 👈 
  
- **✨ Trưng bày nội dung khóa học ✨**

  <!-- <img src="../pics/icon/title.jpg" width="300"/>
  <img src="../pics/icon/cover.png" width="300"/>
  <img src="../pics/icon/team.png" width="300"/>
  <img src="../pics/icon/agent.png" width="300"/> -->

<p align = "center">
  <img src="../pics/icon/title.jpg" width="48%"/>
  <img src="../pics/icon/cover.png" width="48%"/>
  <img src="../pics/icon/team.png" width="48%"/>
  <img src="../pics/icon/agent.png" width="48%"/>
</p>

<a id="mien-tru"></a>
## 🙏 Miễn trừ trách nhiệm

Toàn bộ nội dung của bộ hướng dẫn chỉ đến từ kinh nghiệm cá nhân của những người đóng góp, dữ liệu trên internet và những tích lũy trong công việc nghiên cứu thường ngày. Mọi kỹ thuật đều chỉ mang tính tham khảo, không bảo đảm đúng 100%. Nếu có bất kỳ vấn đề nào, xin hãy gửi Issue hoặc PR. Ngoài ra, các huy hiệu (badge) mà dự án này sử dụng đều lấy từ internet; nếu xâm phạm bản quyền hình ảnh của bạn, xin hãy liên hệ để chúng tôi gỡ bỏ, xin cảm ơn.

<a id="dong-gop"></a>
## 🤝 Hoan nghênh đóng góp

Đây là một dự án đang trong quá trình hoàn thiện, thiếu sót là điều khó tránh khỏi; chúng tôi hoan nghênh mọi PR cũng như thảo luận qua issue.

## ❤️ Danh sách người đóng góp

Cảm ơn các thầy cô và bạn sinh viên sau đây đã hỗ trợ và đóng góp cho dự án:

**Đội phát triển loạt hướng dẫn 《动手学大模型》**:

- 上海交通大学: [张倬胜](https://bcmi.sjtu.edu.cn/home/zhangzs/)、[袁童鑫](https://github.com/Lordog)、[马欣贝](https://scholar.google.com/citations?user=LpUi3EgAAAAJ&hl=zh-CN&oi=ao)、 [何志威](https://zwhe99.github.io)、[杜巍](https://scholar.google.com/citations?user=tFYUBLkAAAAJ&hl=en)、[赵皓东](https://dongdongzhaoup.github.io/)、[吴宗儒](https://zrw00.github.io)、[吴铮](https://wuzheng02.github.io/)、[董凌众](https://github.com/LZ-Dong)、[张玉龙](https://aslan-yulong.github.io/)

- Đại học Quốc gia Singapore: [费豪](http://haofei.vip/)

**Đội phát triển loạt hướng dẫn 《大模型开发全流程》:**

- 上海交通大学: [张倬胜](https://bcmi.sjtu.edu.cn/home/zhangzs/)、[刘功申](https://infosec.sjtu.edu.cn/DirectoryDetail.aspx?id=75)、[陈星宇](https://scholar.google.com/citations?user=d-dNtjrMJ5YC&hl=en)、[程彭洲](https://scholar.google.com/citations?user=qxnwzDUAAAAJ&hl=en)、[董凌众](https://github.com/LZ-Dong)、 [何志威](https://zwhe99.github.io)、[鞠天杰](https://scholar.google.com/citations?user=f8PPcnoAAAAJ&hl=en)、[马欣贝](https://scholar.google.com/citations?user=LpUi3EgAAAAJ&hl=zh-CN&oi=ao)、 [吴铮](https://scholar.google.com/citations?hl=zh-CN&user=qBM1UbUAAAAJ&view_op=list_works&gmla=AIfU4H6PG9JyjRub6BYIIZ4isQE7MBAM3Eoec6OJfX4z_8-pOE8bI1Wgdo3XL5qOZWR3U-h-lIP2q0zXt5gzyFKMSg7MNnBBWLv5d1IVG30UANczTP0)、[吴宗儒](https://zrw00.github.io)、[闫子赫](https://scholar.google.com/citations?user=O2YfSHoAAAAJ&hl=zh-CN)、[姚杳](https://scholar.google.com/citations?user=tLMP3IkAAAAJ)、[袁童鑫](https://github.com/Lordog)、[赵皓东](https://dongdongzhaoup.github.io/);

- Cộng đồng 华为昇腾: ZOMI、谢乾、程黎明、楼梨华、焦泽昱

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Lordog/dive-into-llms&type=Date)](https://star-history.com/#Lordog/dive-into-llms&Date)
