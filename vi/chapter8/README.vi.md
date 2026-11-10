> Bản dịch tiếng Việt · nguồn: [README.md](../../documents/chapter8/README.md) · 《动手学大模型》(Lordog/dive-into-llms)

# Mô hình đa phương tiện

Phần giới thiệu: phần này trình bày các kiến trúc phổ biến và phương pháp xây dựng mô hình ngôn ngữ lớn đa phương tiện

> Sự xuất hiện của các mô hình ngôn ngữ lớn cho mọi người thấy trí tuệ ở cấp độ cao đã được thể hiện đầy đủ ở phương diện ngôn ngữ. Là một mô hình ngôn ngữ lớn đa phương tiện có thể mô phỏng thế giới thực đầy đủ hơn, nó hiện thực hóa năng lực hiểu và sinh đa phương tiện mạnh mẽ hơn bằng cách nào? Mô hình ngôn ngữ lớn đa phương tiện liệu có thể giúp hiện thực hóa AGI hay không?


## Mục tiêu của khóa học

1. Làm quen với các loại mô hình ngôn ngữ lớn đa phương tiện
2. Nắm vững khung kỹ thuật chung của mô hình ngôn ngữ lớn đa phương tiện
3. Nắm vững cách xây dựng, huấn luyện và suy luận của mô hình ngôn ngữ lớn đa phương tiện



## 1. Kiến thức lý thuyết nền tảng



### 1.1 Tìm hiểu các loại mô hình ngôn ngữ lớn đa phương tiện

- Phân loại các mô hình ngôn ngữ lớn đa phương tiện hiện có theo mức hỗ trợ phương diện và hỗ trợ chức năng


> Trước khi xây dựng mô hình ngôn ngữ lớn đa phương tiện (MLLM), các nhà nghiên cứu trong lĩnh vực này đều đạt được một đồng thuận, một tiền đề then chốt: nhờ định luật quy mô (scaling law) và các hiện tượng emerged, các LLM dựa trên ngôn ngữ hiện nay đã có năng lực hiểu ngữ nghĩa mạnh mẽ; điều này có nghĩa ngôn ngữ đã trở thành phương diện then chốt chuyên chở trí tuệ, nên trí tuệ ngôn ngữ được xem là trung tâm của trí tuệ đa phương tiện. Vì vậy, hầu hết các MLLM đều được xây dựng trên nền một LLM dựa trên ngôn ngữ, trong đó LLM đóng vai trò mô-đun quyết định lõi, tương tự như bộ não hoặc bộ xử lý trung tâm. Nói cách khác, bằng cách bổ sung các mô-đun hoặc bộ mã hóa bên ngoài thuộc các phương diện phi văn bản, LLM được trao thêm khả năng cảm nhận/thao tác đa phương tiện.

Chúng tôi phân loại các MLLM hiện có thành các loại khác nhau căn cứ vào mức hỗ trợ phương diện và hỗ trợ chức năng của chúng.

![mllm](../../documents/chapter8/assets/MLLM-summary.png)


- Đọc trọn bộ tutorial: [[Slides](https://github.com/Lordog/dive-into-llms/blob/main/documents/chapter6/mllms.pdf)] 


- Các bài tổng quan liên quan khác
    - [A Survey on Multimodal Large Language Models, https://github.com/BradyFU/Awesome-Multimodal-Large-Language-Models, 2023](https://github.com/BradyFU/Awesome-Multimodal-Large-Language-Models)
    - [MM-LLMs: Recent Advances in MultiModal Large Language Models, 2023](https://arxiv.org/pdf/2401.13601)


### 1.2 Tìm hiểu khung kỹ thuật chung của mô hình ngôn ngữ lớn đa phương tiện


- Kiến trúc một: LLM as Task Scheduler (LLM như bộ lập lịch tác vụ)

> Hiện nay trong cộng đồng tồn tại hai kiến trúc MLLM phổ biến.
Kiến trúc thứ nhất là kiến trúc "LLM như bộ điều phối/điều khiển rời rạc". Như hình dưới đây, vai trò của LLM là tiếp nhận tín hiệu văn bản và phát lệnh văn bản xuống các mô-đun phía dưới. Toàn bộ truyền tin trong hệ thống được thực hiện thông qua lệnh văn bản thuần túy do LLM xuất ra làm trung gian. Giữa các mô-đun chức năng không tồn tại tương tác.


![Architecture1](../../documents/chapter8/assets/Architecture1.png)

- Kiến trúc hai: LLM as Joint Part of System (LLM như một phần hợp nhất của hệ thống)

> Kiến trúc thứ hai, khung encoder-LLM-decoder.
Đây cũng là kiến trúc phổ biến nhất hiện nay. Trong đó vai trò của LLM là cảm nhận thông tin đa phương tiện và tự mình đưa ra phản hồi, thao tác trong một cấu trúc encoder-LLM-decoder. Vì vậy, điểm khác biệt then chốt giữa kiến trúc này và kiến trúc một: LLM là phần hợp nhất then chốt của hệ thống, trực tiếp tiếp nhận thông tin đa phương tiện từ bên ngoài và ủy quyền lệnh cho decoder/bộ sinh theo cách mượt mà hơn. Trong khung encoder-LLM-decoder, như hình dưới đây, bộ mã hóa xử lý tín hiệu mã hóa từ nhiều phương diện, LLM đóng vai trò người quyết định lõi, còn bộ giải mã quản lý đầu ra đa phương tiện.

![Architecture2](../../documents/chapter8/assets/Architecture2.png)





## 2. Thực hành xây dựng mô hình ngôn ngữ lớn đa phương tiện tổng quát

> Thực hành quá trình xây dựng mô hình ngôn ngữ lớn đa phương tiện tổng quát "any modality to any modality"


### 2.1 MLLM tổng quát "any-to-any modality" hướng tới sự thống nhất chung: NExT-GPT

> Nghiên cứu MLLM trong tương lai chắc chắn phát triển theo hướng ngày càng tổng quát (generalist), nên sẽ bao gồm càng nhiều phương diện, chức năng càng tốt. NExT-GPT là một trong những công trình mang tính mở đường nhất trong lĩnh vực này cho tới nay, công trình đầu tiên giới thiệu khái niệm MLLM "any-to-any modality". Kiến trúc này hiện thực hóa các chức năng mạnh mẽ, đặt nền móng cho hướng nghiên cứu mô hình ngôn ngữ lớn đa phương tiện trong tương lai.

![NExT-GPT](../../documents/chapter8/assets/NExT-GPT-screen.png)


> Phần thực hành code về mô hình ngôn ngữ lớn đa phương tiện của khóa học này sẽ lấy code của NExT-GPT làm mục tiêu để phân tích và thực hành theo cách đi từ sâu đến dễ.

[NExT-GPT Project](https://next-gpt.github.io/)

[Kho code NExT-GPT](https://github.com/NExT-GPT/NExT-GPT)




### 2.2 Xem qua khung code


```
├── figures
├── data
│   ├── T-X_pair_data  
│   │   ├── audiocap                      # text-autio pairs data
│   │   │   ├── audios                    # audio files
│   │   │   └── audiocap.json             # the audio captions
│   │   ├── cc3m                          # text-image paris data
│   │   │   ├── images                    # image files
│   │   │   └── cc3m.json                 # the image captions
│   │   └── webvid                        # text-video pairs data
│   │   │   ├── videos                    # video files
│   │   │   └── webvid.json               # the video captions
│   ├── IT_data                           # instruction data
│   │   ├── T+X-T_data                    # text+[image/audio/video] to text instruction data
│   │   │   ├── alpaca                    # textual instruction data
│   │   │   ├── llava                     # visual instruction data
│   │   ├── T-T+X                         # synthesized text to text+[image/audio/video] instruction data
│   │   └── MosIT                         # Modality-switching Instruction Tuning instruction data
├── code
│   ├── config
│   │   ├── base.yaml                     # the model configuration 
│   │   ├── stage_1.yaml                  # enc-side alignment training configuration
│   │   ├── stage_2.yaml                  # dec-side alignment training configuration
│   │   └── stage_3.yaml                  # instruction-tuning configuration
│   ├── dsconfig
│   │   ├── stage_1.json                  # deepspeed configuration for enc-side alignment training
│   │   ├── stage_2.json                  # deepspeed configuration for dec-side alignment training
│   │   └── stage_3.json                  # deepspeed configuration for instruction-tuning training
│   ├── datast
│   │   ├── base_dataset.py
│   │   ├── catalog.py                    # the catalog information of the dataset
│   │   ├── cc3m_datast.py                # process and load text-image pair dataset
│   │   ├── audiocap_datast.py            # process and load text-audio pair dataset
│   │   ├── webvid_dataset.py             # process and load text-video pair dataset
│   │   ├── T+X-T_instruction_dataset.py  # process and load text+x-to-text instruction dataset
│   │   ├── T-T+X_instruction_dataset.py  # process and load text-to-text+x instruction dataset
│   │   └── concat_dataset.py             # process and load multiple dataset
│   ├── model                     
│   │   ├── ImageBind                     # the code from ImageBind Model
│   │   ├── common
│   │   ├── anyToImageVideoAudio.py       # the main model file
│   │   ├── agent.py
│   │   ├── modeling_llama.py
│   │   ├── custom_ad.py                  # the audio diffusion 
│   │   ├── custom_sd.py                  # the image diffusion
│   │   ├── custom_vd.py                  # the video diffusion
│   │   ├── layers.py                     # the output projection layers
│   │   └── ...  
│   ├── scripts
│   │   ├── train.sh                      # training NExT-GPT script
│   │   └── app.sh                        # deploying demo script
│   ├── header.py
│   ├── process_embeddings.py             # precompute the captions embeddings
│   ├── train.py                          # training
│   ├── inference.py                      # inference
│   ├── demo_app.py                       # deploy Gradio demonstration 
│   └── ...
├── ckpt                           
│   ├── delta_ckpt                        # tunable NExT-GPT params
│   │   ├── nextgpt         
│   │   │   ├── 7b_tiva_v0                # the directory to save the log file
│   │   │   │   ├── log                   # the logs
│   └── ...       
│   ├── pretrained_ckpt                   # frozen params of pretrained modules
│   │   ├── imagebind_ckpt
│   │   │   ├──huge                       # version
│   │   │   │   └──imagebind_huge.pth
│   │   ├── vicuna_ckpt
│   │   │   ├── 7b_v0                     # version
│   │   │   │   ├── config.json
│   │   │   │   ├── pytorch_model-00001-of-00002.bin
│   │   │   │   ├── tokenizer.model
│   │   │   │   └── ...
├── LICENCE.md
├── README.md
└── requirements.txt
```


### 2.3 Cài đặt môi trường

Hãy clone repository và cài môi trường cần thiết trước; có thể hoàn tất cài đặt môi trường bằng cách chạy các lệnh sau:

```
conda env create -n nextgpt python=3.8

conda activate nextgpt

# CUDA 11.6
conda install pytorch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1 pytorch-cuda=11.6 -c pytorch -c nvidia

git clone https://github.com/NExT-GPT/NExT-GPT.git
cd NExT-GPT

pip install -r requirements.txt
```




### 2.4 Thực hành suy luận với hệ thống


#### 2.4.1 Nạp checkpoint model NExT-GPT đã pretrain

- **Bước 1**: Nạp `tham số đóng băng` (frozen parameters). [NExT-GPT](https://github.com/NExT-GPT/NExT-GPT) được huấn luyện dựa trên các model hoặc mô-đun hiện có sau đây, hãy chuẩn bị checkpoint theo hướng dẫn bên dưới.
    - `ImageBind` là bộ mã hóa ảnh/video/âm thanh thống nhất. Có thể tải checkpoint đã pretrain từ [đây](https://dl.fbaipublicfiles.com/imagebind/imagebind_huge.pth), phiên bản `huge`. Sau đó đặt file `imagebind_huge.pth` vào [[./ckpt/pretrained_ckpt/imagebind_ckpt/huge]](../../documents/chapter8/ckpt/pretrained_ckpt/imagebind_ckpt/).
    - `Vicuna`: trước tiên chuẩn bị LLaMA theo hướng dẫn [[tại đây]](../../documents/chapter8/ckpt/pretrained_ckpt/prepare_vicuna.md). Sau đó đặt model đã pretrain vào [[./ckpt/pretrained_ckpt/vicuna_ckpt/]](../../documents/chapter8/ckpt/pretrained_ckpt/vicuna_ckpt/).
    - `Image Diffusion` dùng để sinh ảnh. NExT-GPT sử dụng [Stable Diffusion](https://huggingface.co/runwayml/stable-diffusion-v1-5) phiên bản `v1-5`. (_code sẽ tự động tải_)
    - `Audio Diffusion` dùng để sinh nội dung âm thanh. NExT-GPT sử dụng [AudioLDM](https://github.com/haoheliu/AudioLDM) phiên bản `l-full`. (_code sẽ tự động tải_)
    - `Video Diffusion` dùng để sinh video. Chúng tôi sử dụng [ZeroScope](https://huggingface.co/cerspense/zeroscope_v2_576w) phiên bản `v2_576w`. (_code sẽ tự động tải_)

- **Bước 2**: Nạp `tham số điều chỉnh được` (tunable parameters).

Đặt hệ thống NExT-GPT vào [[./ckpt/delta_ckpt/nextgpt/7b_tiva_v0]](../../documents/chapter8/ckpt/delta_ckpt/nextgpt/7b_tiva_v0). Có thể chọn 1) sử dụng tham số do bạn tự huấn luyện, hoặc 2) tải checkpoint đã pretrain từ [Huggingface](https://huggingface.co/ChocoWu/nextgpt_7b_tiva_v0).


#### 2.4.2 Triển khai Gradio Demo

Sau khi hoàn tất nạp checkpoint, bạn có thể chạy demo trên máy cục bộ theo cách sau:
```angular2html
cd ./code
bash scripts/app.sh
```
Các tham số then chốt được chỉ định như sau:
- `--nextgpt_ckpt_path`: đường dẫn tới tham số NExT-GPT đã pretrain.



#### 2.4.3 Thực hành ví dụ kiểm thử

Phiên bản hiện tại có thể hỗ trợ đầu vào là tổ hợp tùy ý của bốn phương diện chữ, ảnh, video, âm thanh, và đầu ra theo các phương diện của tổ hợp tác vụ.
Đồng thời hỗ trợ tương tác ngữ cảnh nhiều lượt.

Mời bạn tự chạy để kiểm thử hiệu quả.

- **Case-1**: đầu vào T+I, đầu ra T+A

![case1](../../documents/chapter8/assets/T+I-T+A.png)


- **Case-2**: đầu vào T+V, đầu ra T+A

![case2](../../documents/chapter8/assets/T+V-T+A.png)


- **Case-3**: đầu vào T+I, đầu ra T+I+V

![case3](../../documents/chapter8/assets/T+I-T+I+V.png)


- **Case-4**: đầu vào T, đầu ra T+I+V+A

![case4](../../documents/chapter8/assets/T-T+I+V+A.png)







### 2.5 Quá trình huấn luyện hệ thống


#### 2.5.1 Chuẩn bị dữ liệu

Hãy tải các tập dữ liệu dùng cho huấn luyện model sau đây:

A) Dữ liệu cặp T-X
  - Dữ liệu `CC3M` cho các cặp ***văn bản-ảnh***, hãy làm theo hướng dẫn [[tại đây]](../../documents/chapter8/data/T-X_pair_data/cc3m/prepare.md). Sau đó đặt dữ liệu tại [[./data/T-X_pair_data/cc3m]](../../documents/chapter8/data/T-X_pair_data/cc3m).
  - Dữ liệu `WebVid` cho các cặp ***văn bản-video***, tham khảo [[hướng dẫn]](../../documents/chapter8/data/T-X_pair_data/webvid/prepare.md). File nên được lưu tại [[./data/T-X_pair_data/webvid]](../../documents/chapter8/data/T-X_pair_data/webvid).
  - Dữ liệu `AudioCap` cho các cặp ***văn bản-âm thanh***, tham khảo [[hướng dẫn]](../../documents/chapter8/data/T-X_pair_data/audiocap/prepare.md). Lưu dữ liệu tại [[./data/T-X_pair_data/audiocap]](../../documents/chapter8/data/T-X_pair_data/audiocap).

B) Dữ liệu fine-tuning theo chỉ dẫn (instruction finetuning)
  - T+X-T
    - ***Dữ liệu chỉ dẫn thị giác*** (from `LLaVA`), tải từ [đây](https://github.com/haotian-liu/LLaVA/blob/main/docs/Data.md) và đặt nó tại [[./data/IT_data/T+X-T_data/llava]](../../documents/chapter8/data/IT_data/T+X-T_data/llava/).
    - ***Dữ liệu chỉ dẫn văn bản*** (from `Alpaca`), tải từ [đây](https://github.com/tatsu-lab/stanford_alpaca) và đặt nó tại [[./data/IT_data/T+X-T_data/alpaca/]](../../documents/chapter8/data/IT_data/T+X-T_data/alpaca/).
    - ***Dữ liệu chỉ dẫn video*** (from `VideoChat`), tải từ [đây](https://github.com/OpenGVLab/InternVideo/tree/main/Data/instruction_data) và đặt nó tại [[./data/IT_data/T+X-T_data/videochat/]](../../documents/chapter8/data/IT_data/T+X-T_data/videochat/).

    Lưu ý: sau khi tải tập dữ liệu, hãy chạy `preprocess_dataset.py` để tiền xử lý tập dữ liệu, nhằm thống nhất định dạng.
  - T-X+T (T2M)
    - Tập dữ liệu chỉ dẫn `T-X+T` (T2M) được lưu tại [[./data/IT_data/T-T+X_data]](../../documents/chapter8/data/IT_data/T-T+X_data).
   
  - MosIT
    - Lấy hướng dẫn tải dữ liệu từ [đây](../../documents/chapter8/data/IT_data/MosIT_data/). Cuối cùng đặt nó tại [[./data/IT_data/MosIT_data/]](../../documents/chapter8/data/IT_data/MosIT_data/).




#### 2.5.2 Chuẩn bị vector nhúng (embedding)

Trong huấn luyện căn chỉnh phía giải mã của NExT-GPT, chúng tôi tối thiểu hóa khoảng cách giữa biểu diễn của Signal Token và captions. Để đảm bảo hiệu suất cao của hệ thống, tiết kiệm thời gian và chi phí bộ nhớ, chúng tôi sử dụng bộ mã hóa văn bản trong từng mô hình diffusion để precompute vector nhúng văn bản của tiêu đề ảnh, âm thanh và video.

Trước khi tiến hành huấn luyện NExT-GPT, hãy chạy lệnh sau; các file `embedding` được sinh ra sẽ lưu tại [[./data/embed]](../../documents/chapter8/data/embed).
```
cd ./code/
python process_embeddings.py ../data/T-X_pair_data/cc3m/cc3m.json image ../data/embed/ runwayml/stable-diffusion-v1-5
```


Giải thích tham số:
- args[1]: đường dẫn file tiêu đề;
- args[2]: phương diện, có thể là `image`, `video` và `audio`;
- args[3]: đường dẫn lưu file vector nhúng;
- args[4]: tên mô hình diffusion đã pretrain tương ứng.




#### 2.5.3 Huấn luyện ba giai đoạn


Trước tiên hãy tham khảo file cấu hình cơ sở [[./code/config/base.yaml]](../../documents/chapter8/code/config/base.yaml) để tìm hiểu thiết lập hệ thống cơ bản của toàn bộ mô-đun.

Sau đó chạy script sau để bắt đầu huấn luyện NExT-GPT:
```
cd ./code
bash scripts/train.sh
```

Lệnh chỉ định như sau:
```
deepspeed --include localhost:0 --master_addr 127.0.0.1 --master_port 28459 train.py \
    --model nextgpt \
    --stage 1\
    --save_path  ../ckpt/delta_ckpt/nextgpt/7b_tiva_v0/\
    --log_path ../ckpt/delta_ckpt/nextgpt/7b_tiva_v0/log/
```
Trong đó các tham số then chốt:
- `--include`: `localhost:0` biểu thị số thứ tự GPU cuda `0` trong deepspeed.
- `--stage`: giai đoạn huấn luyện.
- `--save_path`: thư mục lưu trọng số delta sau huấn luyện. Thư mục này sẽ được tự động tạo.
- `--log_path`: thư mục lưu các file log.



Toàn bộ quá trình huấn luyện NExT-GPT gồm 3 bước:

- **Bước 1**: căn chỉnh đa phương tiện lấy LLM làm trung tâm ở phía mã hóa. Giai đoạn này huấn luyện ***lớp chiếu (projection layer) đầu vào***, đồng thời đóng băng ImageBind, LLM và lớp chiếu đầu ra.
  
  Chỉ cần chạy script `train.sh` ở trên và đặt: `--stage 1`
  
  Cũng hãy tham khảo file cấu hình chạy [[./code/config/stage_1.yaml]](../../documents/chapter8/code/config/stage_1.yaml) và file cấu hình deepspeed [[./code/dsconfig/stage_1.yaml]](../../documents/chapter8/code/dsconfig/stage_1.yaml) để có thêm thông tin cấu hình theo từng bước.

  Lưu ý, tập dữ liệu sử dụng trong bước này nằm trong `dataset_name_list`, và tên tập dữ liệu phải khớp chính xác với định nghĩa trong [[./code/dataset/catalog.py]](../../documents/chapter8/code/dataset/catalog.py).



- **Bước 2**: căn chỉnh theo chỉ dẫn ở phía giải mã. Giai đoạn này huấn luyện ***lớp chiếu đầu ra***, đồng thời đóng băng ImageBind, LLM và lớp chiếu đầu vào.

  Chỉ cần chạy script `train.sh` ở trên và đặt: `--stage 2`

  Cũng hãy tham khảo file cấu hình chạy [[./code/config/stage_2.yaml]](../../documents/chapter8/code/config/stage_2.yaml) và file cấu hình deepspeed [[./code/dsconfig/stage_2.yaml]](../../documents/chapter8/code/dsconfig/stage_2.yaml) để có thêm thông tin cấu hình theo từng bước.



- **Bước 3**: điều chỉnh theo chỉ dẫn (instruction adjustment). Giai đoạn này thực hiện các điều chỉnh sau trên tập dữ liệu chỉ dẫn: 1) điều chỉnh ***LLM*** qua LoRA, 2) điều chỉnh ***lớp chiếu đầu vào*** và 3) điều chỉnh ***lớp chiếu đầu ra***.

  Chỉ cần chạy script `train.sh` ở trên và đặt: `--stage 3`

  Cũng hãy tham khảo file cấu hình chạy [[./code/config/stage_3.yaml]](../../documents/chapter8/code/config/stage_3.yaml) và file cấu hình deepspeed [[./code/dsconfig/stage_3.yaml]](../../documents/chapter8/code/dsconfig/stage_3.yaml) để có thêm thông tin cấu hình theo từng bước.
