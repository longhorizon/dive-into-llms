> Bản dịch tiếng Việt · nguồn: [README.md](../../documents/chapter4/README.md) · 《动手学大模型》(Lordog/dive-into-llms)

# Suy luận toán học trên mô hình lớn
Dự án này hiện thực mã giúp mô hình ngôn ngữ lớn (LLM) học suy luận toán học; kỹ thuật chính là dùng Supervised Fine-tuning (SFT) để mô hình học các câu trả lời do DeepSeek-R1 sinh ra, qua đó rèn luyện các kỹ năng suy luận toán học phức tạp (như phản tư, kiểm tra lại phép tính, v.v.).
Thí nghiệm này dựa trên bộ dữ liệu [DeepMath-103K](https://huggingface.co/datasets/zwhe99/DeepMath-103K) và mô hình [Qwen/Qwen2.5-Math-1.5B](https://huggingface.co/Qwen/Qwen2.5-Math-1.5B), đưa người đọc thử sức bước đầu với toàn bộ quy trình chưng cất dữ liệu (data distillation) cho bài toán toán học.

## Mục tiêu thí nghiệm
- Hiểu cách làm sạch và tiền xử lý các bộ dữ liệu liên quan tới toán học
- Hiểu phương pháp cơ bản để fine-tune mô hình lớn
- Hiểu phương pháp cơ bản để suy luận (generate) với mô hình lớn
- Hiểu phương pháp cơ bản để đánh giá năng lực toán học của mô hình

## Yêu cầu môi trường

- Python 3.8+
- PyTorch
- Transformers
- Datasets
- vllm
- GPU có bộ nhớ GPU (VRAM) từ 40GB trở lên

## Tài liệu thí nghiệm

1. Mở Jupyter notebook:
```bash
jupyter notebook sft_math.ipynb
```

2. Notebook gồm một số phần chính:
   - Tải bộ dữ liệu và tiền xử lý
   - Nạp mô hình, huấn luyện
   - Mô hình sinh kết quả, đánh giá

3. Thao tác và giải thích cụ thể xin xem trong notebook.

## File đầu ra

Quá trình huấn luyện sẽ tạo ra các file checkpoint; sau khi sinh xong, kết quả generate sẽ được lưu lại.

## Lưu ý

Mô hình và dữ liệu được tải từ huggingface; người dùng trong khu vực mạng hạn chế có thể tải qua mirror https://hf-mirror.com.
- Đảm bảo đủ dung lượng đĩa để lưu file mô hình gốc, file dữ liệu và checkpoint sau huấn luyện (hãy dành ra ít nhất 50GB)
- Cần GPU có bộ nhớ GPU (VRAM) từ 40GB trở lên
