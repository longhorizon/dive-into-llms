> Bản dịch tiếng Việt · nguồn: [README.md](../../documents/chapter3/README.md) · 《动手学大模型》(Lordog/dive-into-llms)

# Chỉnh sửa tri thức trên mô hình lớn
Dẫn nhập: các phương pháp và công cụ chỉnh sửa mô hình ngôn ngữ
> Muốn điều khiển cách mô hình ngôn ngữ ghi nhớ một tri thức cụ thể? Hãy chọn phương pháp chỉnh sửa phù hợp, chỉnh sửa tri thức đó rồi kiểm chứng mô hình sau chỉnh sửa!

## 1. Mục tiêu của bài hướng dẫn:

- Làm quen với bộ công cụ EasyEdit
- Nắm được phương pháp chỉnh sửa mô hình ngôn ngữ (bản đơn giản nhất)
- Hiểu cách lựa chọn và ngữ cảnh ứng dụng của các nhóm phương pháp chỉnh sửa khác nhau

## 2. Chuẩn bị:
### 2.1 Tìm hiểu EasyEdit

https://github.com/zjunlp/EasyEdit

EasyEdit là một gói Python dùng để chỉnh sửa mô hình ngôn ngữ, ví dụ GPT-J, Llama, GPT-NEO, GPT2, T5, v.v.; mục tiêu của nó là thay đổi hiệu quả hành vi của mô hình ngôn ngữ đối với một tri thức cụ thể mà không gây ảnh hưởng tiêu cực đến hiệu năng trên các đầu vào khác, đồng thời dễ sử dụng và dễ mở rộng.

EasyEdit tích hợp sẵn các phương pháp chỉnh sửa phổ biến hiện có:
![](../../documents/chapter3/assets/1.png)

### 2.2 Khung tổng thể

![](../../documents/chapter3/assets/2.png)
EasyEdit gồm một khung thống nhất Editor, Method và Evaluate, lần lượt đại diện cho kịch bản chỉnh sửa, kỹ thuật chỉnh sửa và phương pháp đánh giá.
- Editor: mô tả kịch bản làm việc, gồm mô hình cần chỉnh sửa, tri thức cần chỉnh sửa và các siêu tham số cần thiết khác.
- Method: phương pháp chỉnh sửa tri thức cụ thể được sử dụng (ví dụ ROME, MEND, v.v.).
- Evaluate: các chỉ báo đánh giá hiệu năng chỉnh sửa tri thức, bao gồm độ tin cậy (reliability), tính khái quát (generalization), tính cục bộ (locality) và tính di chuyển (portability).
- Trainer: một số phương pháp chỉnh sửa cần quá trình huấn luyện nhất định, do module Trainer đảm nhiệm.
## 3. Cài đặt môi trường:
```
git clone https://github.com/zjunlp/EasyEdit.git
(tùy chọn) conda create -n EasyEdit python=3.9.7
cd EasyEdit
pip install -r requirements.txt
```
## 4. Ví dụ chỉnh sửa
> Mục tiêu: thay đổi ký ức tri thức của GPT-2-XL, đổi nghề của Messi (Lionel Messi) từ bóng đá sang bóng rổ (football->basketball). 
Các bước:
- Chọn phương pháp chỉnh sửa, chuẩn bị tham số
- Chuẩn bị dữ liệu chỉnh sửa tri thức
- Khởi tạo (instantiate) Editor
- Run!
Dưới đây xin lấy phương pháp ROME làm ví dụ minh họa cụ thể:
### 4.1 ROME
Jupiter Notebook: [https://colab.research.google.com/drive/1KkyWqyV3BjXCWfdrrgbR-QS3AAokVZbr?usp=sharing#scrollTo=zWfGkNb9FBJQ] 
- Chọn phương pháp chỉnh sửa, chuẩn bị tham số
  - Chọn phương pháp chỉnh sửa là ROME, chuẩn bị các tham số mà ROME và GPT2-XL đòi hỏi.
  - Ví dụ: alg_name: "ROME", model_name: "./hugging_cache/gpt2-xl" hoặc đường dẫn cục bộ tới mô hình này, "device": số thứ tự GPU sử dụng
  - Các tham số còn lại có thể giữ nguyên giá trị mặc định
![](../../documents/chapter3/assets/3.png)
- Chuẩn bị dữ liệu chỉnh sửa tri thức
    ```
    prompts = ['Question:What sport does Lionel Messi play? Answer:'] # x_e
    ground_truth = ['football'] # y
    target_new = ['basketball'] # y_e
    subject = ['Lionel Messi'] 
    ```
- Khởi tạo Editor: truyền các tham số đã chuẩn bị vào class BaseEditor để khởi tạo, ta nhận được một instance Editor đã được tùy biến.
    ```
    hparams = ROMEHyperParams.from_hparams('./hparams/ROME/gpt2-xl.yaml')
    editor=BaseEditor.from_hparams(hparams)
    ```
- Run! Gọi phương thức edit của editor:
    ```
    metrics, edited_model, _ = editor.edit(
        prompts=prompts,
        ground_truth=ground_truth,
        target_new=target_new,
        subject=subject,
        keep_original_weight=False
    )
    ```
![](../../documents/chapter3/assets/4.png)
> Lưu ý: lần đầu chỉnh sửa một mô hình nào đó, hệ thống sẽ tải ngữ liệu Wiki và tính toán trạng thái của từng lớp (stats_dir: "./data/stats") cho mô hình đó rồi lưu lại để tái sử dụng trong mọi lần chỉnh sửa về sau. Vì vậy lần chỉnh sửa đầu tiên hơi tốn thời gian; hãy kiên nhẫn chờ khi đảm bảo kết nối mạng thông suốt.
### 4.2 Kiểm chứng và đánh giá
editor.edit sẽ trả về metrics (do module Evaluate của EasyEdit tính toán). Dạng cụ thể như sau:
![](../../documents/chapter3/assets/5.png)
Để có được số đo của tính khái quát, tính cục bộ và tính di chuyển, cần truyền dữ liệu dùng cho việc đánh giá vào trong phương thức edit.

Lấy tính cục bộ làm ví dụ: khi đó phương thức edit sẽ tính chỉ báo cục bộ, tức tỉ lệ trả lời đúng của mô hình trên locality_inputs.
```
locality_inputs = {
    'neighborhood':{
        'prompt': ['Joseph Fischhof, the', 'Larry Bird is a professional', 'In Forssa, they understand'],
        'ground_truth': ['piano', 'basketball', 'Finnish']
    }
}
metrics, edited_model, _ = editor.edit(
    prompts=prompts,
    ground_truth=ground_truth,
    target_new=target_new,
    locality_inputs=locality_inputs,
    keep_original_weight=False
)
```
Hoặc so sánh trực tiếp hành vi generte của mô hình trước và sau chỉnh sửa.
```
generation_prompts = [
    "Lionel Messi, the",
    "The law in Ikaalinen declares the language"
]

model = GPT2LMHeadModel.from_pretrained('./hugging_cache/gpt2').to('cuda')
batch = tokenizer(generation_prompts, return_tensors='pt', padding=True, max_length=30)

pre_edit_outputs = model.generate(
    input_ids=batch['input_ids'].to('cuda'),
    attention_mask=batch['attention_mask'].to('cuda'),
    max_new_tokens=3
)
post_edit_outputs = edited_model.generate(
    input_ids=batch['input_ids'].to('cuda'),
    attention_mask=batch['attention_mask'].to('cuda'),
    max_new_tokens=3)
```
## 5. Chỉnh sửa quy mô lớn (tùy chọn)
### 5.1 Batch edit
Nhiều mẫu dữ liệu có thể xếp thành các danh sách song song và truyền đồng thời vào phương thức edit để chỉnh sửa theo batch (batch edit); khi đó MEMIT là phương pháp tối ưu nhất. (https://colab.research.google.com/drive/1P1lVklP8bTyh8uxxSuHnHwB91i-1LW6Z)
```
prompts = ['Question:What sport does Lionel Messi play? Answer:',
            'The law in Ikaalinen declares the language']
ground_truth = ['football', 'Finnish']
target_new = ['basketball', 'Swedish']
subject = ['Lionel Messi', 'Ikaalinen']
```
### 5.2 Kiểm thử trên benchmark
- Counterfact
- ZsRE
```
{
    "case_id": 4402,
    "pararel_idx": 11185,
    "requested_rewrite": {
      "prompt": "{} debuted on",
      "relation_id": "P449",
      "target_new": {
        "str": "CBS",
        "id": "Q43380"
      },
      "target_true": {
        "str": "MTV",
        "id": "Q43359"
      },
      "subject": "Singled Out"
    },
    "paraphrase_prompts": [
      "No one on the ground was injured.  v",
      "The sex ratio was 1063. Singled Out is to debut on"
    ],
    "neighborhood_prompts": [
      "Daria premieres on",
      "Teen Wolf was originally aired on",
      "Spider-Man: The New Animated Series was originally aired on",
      "Celebrity Deathmatch premiered on",
      "\u00c6on Flux premiered on",
      "My Super Psycho Sweet 16 premieres on",
      "Daria was released on",
      "Jersey Shore premiered on",
      "Skins was originally aired on",
      "All You've Got premiered on"
    ]
  }
  ```
https://github.com/zjunlp/EasyEdit/blob/main/examples/run_zsre_llama2.py 
