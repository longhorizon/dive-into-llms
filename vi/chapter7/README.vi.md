> Bản dịch tiếng Việt · nguồn: [README.md](../../documents/chapter7/README.md) · 《动手学大模型》(Lordog/dive-into-llms)

# Giấu tin trong văn bản dùng mô hình ngôn ngữ lớn

Dự án này triển khai kỹ thuật giấu tin (steganography) trong văn bản dựa trên mô hình ngôn ngữ lớn (LLM), sử dụng mô hình GPT-2 để ẩn thông tin trong văn bản được sinh ra. Dự án gồm hai phương pháp mã hóa: mã hóa Huffman (Huffman Coding) và mã hóa độ dài cố định (Fixed Length Coding, FLC).

## Đặc tính

- Thực hiện giấu tin trong quá trình GPT-2 sinh văn bản
- Hỗ trợ hai phương pháp mã hóa:
  - Mã hóa Huffman (Huffman Coding)
  - Mã hóa độ dài cố định (Fixed Length Coding, FLC)
- Đồng thời sinh văn bản giấu tin và văn bản thông thường để so sánh

## Yêu cầu môi trường

- Python 3.8+
- PyTorch
- Transformers
- CUDA (tùy chọn, để tăng tốc bằng GPU)

## Cài đặt

Cài các gói phụ thuộc:

```bash
pip install torch # nếu dùng GPU, chú ý chọn bản torch dành cho GPU
pip install transformers
pip install jupyter
```

## Cách sử dụng

1. Mở Jupyter notebook:
```bash
jupyter notebook llm_stega.ipynb
```

2. Notebook gồm ba phần chính:
   - Triển khai mã hóa Huffman
   - Triển khai mã hóa độ dài cố định (FLC)
   - Sinh văn bản và giấu tin

3. Sinh văn bản giấu tin:
   - Chọn phương pháp mã hóa (Huffman hoặc FLC)
   - Thiết lập tham số (giá trị k của mã hóa)
   - Chạy hàm main với prompt tùy chỉnh

Mã ví dụ:
```python
# Khởi tạo bộ xử lý giấu tin
k = 2
handle = Huffman(k=2**k, bits=bits)
# Hoặc sử dụng FLC
# handle = FLC(k=k, bits=bits)

# Sinh văn bản có giấu tin
prompt = "Hello，I'm"
stega_output, normal_output = generate_text_with_steganography(
    model, tokenizer, prompt, handle
)
```

## File đầu ra

Chương trình tạo ra hai file văn bản:
- `outputs-gpt2-stega.txt`: văn bản giấu tin
- `outputs-gpt2-normal.txt`: văn bản được sinh ra hoàn toàn thông thường, không chịu ràng buộc của việc giấu tin

## Lưu ý

Mô hình GPT-2 sẽ tự động tải về khi chạy lần đầu; ở Trung Quốc có thể tải trước mô hình GPT-2 qua mirror https://hf-mirror.com , cũng có thể sử dụng các mô hình lớn khác.
- Đảm bảo đủ dung lượng đĩa (mô hình nặng khoảng 500MB)
- Nên dùng GPU hỗ trợ CUDA để có hiệu năng tốt hơn
- Độ dài thông tin giấu ảnh hưởng đến độ dài văn bản được sinh ra

## Nguyên lý hoạt động

1. Quá trình giấu tin:
   - Chuyển đổi thông tin bí mật thành chuỗi nhị phân
   - Sử dụng mô hình GPT-2 để sinh văn bản
   - Đưa các bit thông tin vào văn bản được sinh ra thông qua phương pháp mã hóa

2. Quá trình giải mã:
   - Sử dụng cùng mô hình GPT-2 và ngữ cảnh
   - Trích xuất các bit thông tin ẩn từ văn bản bằng phương pháp giải mã
   - Chuyển đổi chuỗi nhị phân trở lại thông tin gốc
