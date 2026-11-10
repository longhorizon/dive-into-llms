# Bảng thuật ngữ dịch thuật (中文 → Tiếng Việt / English)

Dùng **nhất quán** trong mọi file `*.vi.md` và `*.vi.ipynb`. Thêm mục mới khi gặp thuật ngữ mới.

## 1. Nguyên tắc

1. **Không dịch**: code, lệnh shell, tên model, tên dataset, tên paper, URL, đường dẫn ảnh, công thức LaTeX, tên người (pinyin/Hán tự), badge shields.io.
2. **Giữ tiếng Anh** các prompt ví dụ và tên kỹ thuật đã phổ biến: prompt, fine-tuning, CoT, RLHF, PPO, checkpoint, GPU, token, API.
3. Lần đầu một khái niệm xuất hiện trong chương: viết `thuật ngữ Việt (中文 · English)`. Các lần sau chỉ cần tiếng Việt.
4. Comment tiếng Trung trong code block → dịch sang tiếng Việt, giữ nguyên cú pháp và indentation.
5. Caption ảnh → tiếng Việt, **đường dẫn ảnh không đổi**.
6. Bảng Markdown: giữ số cột và cấu trúc `| ... |`.
7. Đầu mỗi file dịch có dòng:
   `> Bản dịch tiếng Việt · nguồn: [README.md](./README.md) · 《动手学大模型》(Lordog/dive-into-llms)`
8. Không thêm/bớt nội dung kỹ thuật, số liệu, link so với bản gốc.

## 2. Thuật ngữ chung

| 中文 | Tiếng Việt | English giữ nguyên |
|---|---|---|
| 大模型 / 大规模语言模型 | mô hình lớn / mô hình ngôn ngữ lớn | LLM |
| 预训练模型 | mô hình tiền huấn luyện | pre-trained model |
| 微调 | tinh chỉnh | fine-tuning |
| 全参数微调 / 全量微调 | tinh chỉnh toàn bộ tham số | full fine-tuning |
| 提示 / 提示词 / 提示学习 | câu lệnh (prompt) / học theo prompt | prompting |
| 思维链 | chuỗi suy nghĩ | Chain-of-Thought (CoT) |
| 推理 | suy luận; chạy suy luận | inference |
| 知识编辑 | chỉnh sửa tri thức | knowledge editing |
| 蒸馏 | chưng cất (dữ liệu) | distillation |
| 水印 | watermark (dấu ẩn trong văn bản) | watermarking |
| 越狱 / 越狱攻击 | tấn công jailbreak | jailbreak |
| 隐写 | giấu tin | steganography |
| 多模态 | đa phương tiện | multimodal |
| 智能体 | tác tử | agent |
| 对齐 | căn chỉnh | alignment |
| 评测 / 评估 | đánh giá | evaluation |
| 数据集 | tập dữ liệu | dataset |
| 训练 / 验证 / 预测 | huấn luyện / thẩm định (validation) / dự đoán | train / val / predict |
| 损失函数 | hàm mất mát | loss function |
| 显存 | bộ nhớ GPU (VRAM) | VRAM |
| 课件 | slide bài giảng | slides |
| 教程 / 脚本 | hướng dẫn / script | tutorial / script |
| 实验 | thực nghiệm /实验 thí nghiệm | lab / experiment |
| 环境要求 | yêu cầu môi trường | requirements |
| 注意事项 | lưu ý | notes |
| 免责声明 | miễn trừ trách nhiệm | disclaimer |
| 贡献者 | người đóng góp | contributors |
| 导读 | dẫn nhập | intro |
| 本教程目标 | mục tiêu của hướng dẫn | goals |
| 工作准备 | chuẩn bị | setup |
| 案例库 | thư viện ví dụ | examples |
| 评价指标 | chỉ báo đánh giá | metrics |
| 超参数 | siêu tham số | hyperparameter |

## 3. Tiêu đề 11 chương (nhất quán mọi nơi)

| 中文 tiêu đề gốc | Tiếng Việt |
|---|---|
| 微调与部署 | Tinh chỉnh và triển khai |
| 提示学习与思维链 | Học theo prompt và chuỗi suy nghĩ (CoT) |
| 知识编辑 | Chỉnh sửa tri thức |
| 数学推理 | Suy luận toán học |
| 模型水印 | Watermark cho mô hình ngôn ngữ |
| 越狱攻击 | Tấn công jailbreak |
| 大模型隐写 | Giấu tin trong mô hình lớn |
| 多模态模型 | Mô hình ngôn ngữ đa phương tiện |
| GUI智能体 | Agent GUI |
| 智能体安全 | An toàn cho tác tử (agent safety) |
| RLHF安全对齐 | Căn chỉnh an toàn bằng RLHF |

## 4. Tên riêng giữ nguyên

《动手学大模型》 · 上海交通大学 · 张倬胜 · 华为昇腾 · 《大模型开发全流程》 · hiascend.com · pan.quark.cn · blog.csdn.net

## 5. Nhật ký quyết định

- **Layout (chốt 11/2025)**: mọi bản dịch nằm trong thư mục `vi/` mirror cấu trúc chương (`vi/README.vi.md`, `vi/chapterN/README.vi.md`, `vi/chapterN/*.vi.ipynb`, `vi/chapterN/<pdf>.slides.vi.md`); **không sửa file gốc**; commit trực tiếp trên nhánh `main` (nhánh `translate/vi` bị xóa).
- Dòng nguồn đầu file dịch trong `vi/chapterN/`: `> Bản dịch tiếng Việt · nguồn: [README.md](../../documents/chapterN/README.md) · 《动手学大模型》(Lordog/dive-into-llms)`.
- PDF **nằm trong phạm vi dịch** (surrogate Markdown theo trang, xem Task 13 của TRANSLATION_PLAN.vi.md).
- `documents/chapter7/llm_stega.ipynb`: bỏ qua (chỉ có code + comment tiếng Anh, 0 ký tự Trung Quốc).
- Chương 1, 2, 3, 5, 6, 8, 10: markdown của notebook trùng README → dịch 1 lần, copy sang notebook.
