# Kế hoạch dịch 《动手学大模型》 sang tiếng Việt

Tài liệu điều hành dự án dịch bộ hướng dẫn 《动手学大模型》 (Lordog/dive-into-llms, 11 chương) sang tiếng Việt.
Cập nhật theo quyết định mới: **toàn bộ bản dịch nằm trong thư mục `vi/`**, commit trực tiếp trên nhánh **`main`**, **PDF nằm trong phạm vi dịch** (bản surrogate Markdown).

---

## 1. Cấu trúc thư mục bản dịch (quy ước chuẩn)

```
vi/
├── README.vi.md                          # dịch README.md gốc
├── chapter1/
│   ├── README.vi.md                      # dịch documents/chapter1/README.md
│   ├── dive-tuning.vi.ipynb              # bản mirror của notebook gốc (code giữ nguyên)
│   └── dive-into-llm.slides.vi.md        # surrogate chữ của PDF slide
├── chapter2/ ... (cùng mẫu) ...
└── chapter11/
    ├── README.vi.md
    ├── RLHF.vi.ipynb
    └── RLHF.slides.vi.md
```

Quy ước tên:
- README chương → `vi/chapterN/README.vi.md`
- Notebook → `vi/chapterN/<tên>.vi.ipynb` (sao chép notebook gốc, chỉ thay markdown + comment tiếng Trung)
- PDF → `vi/chapterN/<tên>.slides.vi.md` (giữ nguyên tên PDF + đuôi `.slides.vi.md`)
- **Không bao giờ sửa file gốc**; `assets/`, `figs/`, `pics/` không sao chép.

### Quy tắc viết lại đường dẫn tương đối (bắt buộc)

| Loại link trong bản gốc | Bản dịch trong `vi/` |
|---|---|
| Ảnh `./figs/...` trong `documents/chapterN/README.md` | `../../documents/chapterN/figs/...` |
| Ảnh `./pics/...` trong `README.md` gốc | `../pics/...` (trong `vi/README.vi.md`) |
| Link sang README chương khác | `../chapterM/README.vi.md` |
| Link slide PDF (GitHub URL) | Giữ nguyên URL gốc |
| Link notebook script | trỏ `chapterN/<tên>.vi.ipynb` (tương đối từ `vi/`) |
| Dòng nguồn đầu mỗi file dịch | `> Bản dịch tiếng Việt · nguồn: [README.md](../../documents/chapterN/README.md) · 《动手学大模型》(Lordog/dive-into-llms)` — trong `vi/README.vi.md` dùng `(../README.md)` |

## 2. Hiện trạng đã đo (tính đầy đủ tháng 11/2025)

### 2.1 Markdown + Notebook (10.508 ký tự Hán / 2.544 dòng)

| Chương | README (dòng · Hán) | Notebook | Hán md nb | Hán code nb | Trùng md README↔nb | Ghi chú |
|---|---|---|---|---|---|---|
| 1 | 211 · 1051 | dive-tuning.ipynb | ~1050 | 0 (160 Hán trong fence README) | 98–100% | mirror |
| 2 | ~200 · 636 | dive-prompting.ipynb | ~636 | 0 | 98–100% | mirror |
| 3 | ~200 · 686 | dive_edit.ipynb | ~686 | 0 | 98–100% | mirror |
| 4 | ~150 · 317 | sft_math.ipynb (37 cells) | 650 | **407** | 12.7% | dịch độc lập; code chỉ dich comment `#` |
| 5 | ~180 · 587 | watermark.ipynb | ~587 | 0 | 98–100% | mirror |
| 6 | ~210 · 669 | dive-jailbreak.ipynb | ~669 | 0 | 98–100% | mirror; 16 prompt tấn công giữ nguyên |
| 7 | ~160 · 458 | llm_stega.ipynb | 0 | 0 | — | **bỏ qua notebook** (0 Hán) |
| 8 | 348 · 2026 | mllms.ipynb | ~2026 | 0 | 98–100% | mirror; chia 2 lượt dịch |
| 9 | ~230 · 684 | GUIagent.ipynb | nhiều hơn README | 0 | 64.4% | dịch độc lập |
| 10 | ~300 · 1021 | agent.ipynb | ~1021 | 0 | 98–100% | mirror |
| 11 | 550 · 961 | RLHF.ipynb (38 cells) | 1025 | 0 | 36.6% | dịch độc lập cả 2 |

### 2.2 PDF slide (495 trang, đo bằng PyMuPDF)

| Chương | File PDF | Trang | Hán trích được | Cách xử lý |
|---|---|---|---|---|
| 7 | stega.pdf | 13 | 1979 | dich đầy đủ |
| 4 | math.pdf | 17 | 1587 | dich đầy đủ |
| 3 | dive_edit_0410.pdf | 21 | 44 | xử lý nhẹ (gần như thuần Anh) |
| 11 | RLHF.pdf | 24 | 1833 | dich đầy đủ |
| 9 | GUIagent.pdf | 43 | 4188 | dich đầy đủ |
| 6 | dive-Jailbreak.pdf | 44 | 7300 | dich đầy đủ |
| 5 | watermark.pdf | 48 | **0** | slide dạng ảnh → skip/OCR sau |
| 10 | dive-into-safety.pdf | 51 | 5236 | dich đầy đủ |
| 2 | dive-into-prompting.pdf | 76 | 11069 | dich đầy đủ |
| 1 | dive-into-llm.pdf | 77 | 6297 | dich đầy đủ |
| 8 | mllms.pdf | 81 | **0** | slide dạng ảnh → skip/OCR sau |

## 3. Quy ước dịch (tóm tắt — chi tiết trong GLOSSARY.vi.md)

- Không dịch: code, lệnh shell, tên model/dataset/paper, URL, đường dẫn ảnh, LaTeX, tên người (Hán tự), badge shields.io.
- Giữ tiếng Anh: prompt, fine-tuning, CoT, RLHF, PPO, checkpoint, GPU, token, API…
- Lần đầu một khái niệm trong chương: `thuật ngữ Việt (中文 · English)`.
- Bảng/ảnh/code block: giữ đúng số cột, số ảnh, số fence so với bản gốc.
- Chương 4: chỉ dich comment `#` trong code cell (407 Hán); **giữ** tiếng Trung trong chuỗi literal.
- Chương 6: 16 code block chứa prompt tấn công mẫu — giữ **nguyên văn từng ký tự**.

## 4. Danh sách task (checklist điều hành)

### Task 0 — Chuẩn bị ✅
- [x] Đo hiện trạng (README, notebook, PDF).
- [x] Cài PyMuPDF (`pymupdf`; dùng `import pymupdf`).
- [x] `git checkout main`; xóa nhánh trống `translate/vi`.
- [x] Tạo khung thư mục `vi/`.

### Task 1 — `vi/README.vi.md` ✅
- [x] Dịch README gốc (1.412 Hán).
- [x] Sửa link: `../pics/...`, `chapterN/README.vi.md`, giữ URL slide.
- [x] Commit.

### Task 2 — Chương 1: Tinh chỉnh và triển khai
- [x] `vi/chapter1/README.vi.md` (dịch từ 211 dòng / 1051 Hán; 17 ảnh; 160 Hán trong fence → giữ fence nguyên văn nếu là code, dich nếu là output/comment).
- [x] `vi/chapter1/dive-tuning.vi.ipynb` (mirror 98–100%: dich 1 lần, đổ vào markdown cells).
- [x] Commit `ch1: README + notebook` → `23adcfe`.

### Task 3 — Chương 2: Học theo prompt và CoT
- [x] `vi/chapter2/README.vi.md` (147 dòng; 3 ảnh; 2 fence giữ nguyên văn (prompt Trung trong chuỗi literal)) · [x] `dive-prompting.vi.ipynb` (mirror 10 cells) · [x] Commit `7c7ddba` (kèm cập nhật checker: cho phép chuỗi Hán trong fence).

### Task 4 — Chương 3: Chỉnh sửa tri thức
- [x] `vi/chapter3/README.vi.md` (165 dòng mirror; 5 ảnh; 8 fence; 1 lệch chấp nhận: README dòng 114 `max_new_tokens=3)` sang notebook tách 2 dòng) · [x] `dive_edit.vi.ipynb` (mirror 5 cells) · [x] Commit (xem bảng tiến độ).

### Task 5 — Chương 4: Suy luận toán học
- [x] `vi/chapter4/README.vi.md` (45 dòng, dịch độc lập — trùng 12.7%; 3 link; 1 fence).
- [x] `vi/chapter4/sft_math.vi.ipynb`: 38 cells — thêm cell0 markdown chứa dòng nguồn (notebook gốc bắt đầu bằng code cell); dịch 10 markdown cell + **chỉ comment `#`** trong 27 code cell (kể cả comment nội dòng cell19, cell25 `##`), giữ chuỗi literal tiếng Trung.
- [x] Commit (xem bảng tiến độ).

### Task 6 — Chương 5: Watermark
- [x] `vi/chapter5/README.vi.md` (194 dòng = 192 gốc + 2 dòng nguồn; mirror 100%; 2 ảnh; 11 fence; 5 link).
- [x] `vi/chapter5/watermark.vi.ipynb` (mirror 5 markdown cells, ranges verified: 1–13, 16–42, 43–152, 153–189, 190–192).
- [x] Commit (xem bảng tiến độ).

### Task 7 — Chương 6: Tấn công jailbreak
- [x] `vi/chapter6/README.vi.md` (182 dòng = 180 gốc + 2 dòng nguồn; mirror ~100%; 2 ảnh; 24 fence; 3 link; 16 prompt tấn công mẫu trong fence giữ nguyên văn; giữ typo `method_namemethod_name` dòng 123).
- [x] `vi/chapter6/dive-jailbreak.vi.ipynb` (mirror 5 markdown cells, ranges 1–8, 10–34, 35–45, 47–116, 117–180; 17 fence mở ` ```python ` trong notebook được giữ khi dịch — README gốc dùng fence trần).
- [x] Commit (xem bảng tiến độ).

### Task 8 — Chương 7: Giấu tin (steganography)
- [x] `vi/chapter7/README.vi.md` (88 dòng = 86 phần tử gốc gồm dòng cuối rỗng + 2 dòng nguồn; 0 ảnh; 3 fence; comment `#` trong fence dịch theo chính sách ch4 — dòng 25, 49, 52, 55; code bị comment-hóa (53) và string literal (56) giữ nguyên văn).
- [x] `llm_stega.ipynb` bỏ qua (0 Hán).
- [x] Commit (xem bảng tiến độ).

### Task 9 — Chương 8: Mô hình đa phương tiện
- [x] `vi/chapter8/README.vi.md` (349 dòng = 347 dòng nội dung gốc + 2 dòng nguồn; 8 ảnh; 6 fence (12 marker) giữ nguyên văn — 0 Hán trong fence; 94 dòng Hán dịch qua FULL dict; link tương đối `](./data|code|ckpt/` rewrite về `../../documents/chapter8/...`; giữ nguyên URL typo `documents/chapter6/mllms.pdf` + dấu cách cuối dòng 32).
- [x] `vi/chapter8/mllms.vi.ipynb` (mirror 3 markdown cells: cell0 = nguồn + README 1–7 + 1 đoạn lạ về agent/rủi ro (dịch riêng cho khớp notebook) + README 8–12; cell1 = README 16–61; cell2 = README 62–347 + 1 dòng trắng cuối; README 13–15 không có trong notebook).
- [x] Commit (xem bảng tiến độ).

### Task 10 — Chương 9: Agent GUI
- [x] `vi/chapter9/README.vi.md` (229 dòng = 227 dòng nội dung gốc + 2 dòng nguồn; 0 ảnh; 7 fence (14 marker) giữ nguyên văn — Hán duy nhất trong fence là string literal JSON mẫu (dòng 23, 26–30, giữ nguyên theo tiền lệ ch4/ch6); 35 dòng Hán ngoài fence dịch qua FULL dict; mọi link là URL tuyệt đối (Slides/Paper/Data/Model/Code) — không cần rewrite đường dẫn; giữ nguyên URL typo `documents/chapter8/GUIagent.pdf` (dòng 10) + dấu cách cuối `},   ` (dòng 165)).
- [x] `vi/chapter9/GUIagent.vi.ipynb` (mirror-with-gaps 8 cells, gần như mirror toàn bộ: cell0 = nguồn + README 1; cell1 = README 2–7; cell2 = README 8–46 (kèm fence JSON); cell3 = README 48–50 (README 47 trắng vắng); cell4 code = README 52–145 nguyên văn (fence 51/146 thành code cell, không marker); cell5 = README 147; cell6 = README 148–213 (README 214 trắng vắng); cell7 = README 215–227).
- [x] Commit (xem bảng tiến độ).

### Task 11 — Chương 10: An toàn cho agent
- [ ] `vi/chapter10/README.vi.md` (1021 Hán) · [ ] `agent.vi.ipynb` (mirror) · [ ] Commit.

### Task 12 — Chương 11: Căn chỉnh an toàn bằng RLHF
- [ ] `vi/chapter11/README.vi.md` (550 dòng / 961 Hán).
- [ ] `RLHF.vi.ipynb` (38 cells, 1025 Hán markdown) dịch **độc lập** (trùng 36.6%).
- [ ] `requirements.txt` bỏ qua (0 Hán).
- [ ] Commit.

### Task 13 — PDF slides (bắt buộc), thứ tự ngắn → dài
- [ ] `stega.pdf` (13 tr) → `vi/chapter7/stega.slides.vi.md`
- [ ] `math.pdf` (17 tr) → `vi/chapter4/math.slides.vi.md`
- [ ] `dive_edit_0410.pdf` (21 tr, 44 Hán) → bản nhẹ: đầu trang + chú thích Việt
- [ ] `RLHF.pdf` (24 tr) → `vi/chapter11/RLHF.slides.vi.md`
- [ ] `GUIagent.pdf` (43 tr) → `vi/chapter9/GUIagent.slides.vi.md`
- [ ] `dive-Jailbreak.pdf` (44 tr) → `vi/chapter6/dive-Jailbreak.slides.vi.md`
- [ ] `dive-into-safety.pdf` (51 tr) → `vi/chapter10/dive-into-safety.slides.vi.md`
- [ ] `dive-into-prompting.pdf` (76 tr) → `vi/chapter2/dive-into-prompting.slides.vi.md`
- [ ] `dive-into-llm.pdf` (77 tr) → `vi/chapter1/dive-into-llm.slides.vi.md`
- [ ] `watermark.pdf` (48 tr, 0 Hán trích được) → ghi chú "slide dạng ảnh, không trích được chữ" trong surrogate; cân nhắc OCR sau
- [ ] `mllms.pdf` (81 tr, 0 Hán trích được) → như trên
- Quy trình: PyMuPDF trích text theo trang → dịch → surrogate có mục lục theo trang (`## Trang N`). Commit theo từng nhóm chương.

### Task 14 — QA và hoàn tất
- [ ] `python tools/check_untranslated.py` — 0 Hán ngoài danh sách cho phép trên mọi cặp file.
- [ ] Đối chiếu số ảnh/link/code fence bản dịch ↔ gốc (script tự động làm).
- [ ] Rà soát nhất quán thuật ngữ theo GLOSSARY.vi.md.
- [ ] (Cần user đồng ý) thêm 1 link tiếng Việt vào `README.md` gốc: `[中文](README.md) | [Tiếng Việt](vi/README.vi.md)`.
- [ ] Commit cuối.

## 5. Bảng tiến độ

| Task | Mục | Trạng thái | Commit |
|---|---|---|---|
| 0 | Chuẩn bị, Git, khung `vi/` | ✅ | (gộp Task 1) |
| 1 | `vi/README.vi.md` | ✅ | `acb1e56` |
| 2 | Chương 1 | ✅ | `23adcfe` |
| 3 | Chương 2 | ✅ | `7c7ddba` |
| 4 | Chương 3 | ✅ | `356d052` |
| 5 | Chương 4 | ✅ | `5262ddf` |
| 6 | Chương 5 | ✅ | `854b720` |
| 7 | Chương 6 | ✅ | `26b63be` |
| 8 | Chương 7 | ✅ | `629a23c` |
| 9 | Chương 8 | ✅ | `b589d12` |
| 10 | Chương 9 | ✅ | (commit này) |
| 11–12 | Chương 10–11 | ⬜ | — |
| 13 | PDF slides | ⬜ | — |
| 14 | QA + link ngược | ⬜ | — |

Ước lượng: Markdown+notebook ~9–10 giờ; PDF ~495 trang (bớt 2 file 0 Hán trích được → còn ~330 trang có chữ thật để dịch).
