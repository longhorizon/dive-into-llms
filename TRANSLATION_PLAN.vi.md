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
- [ ] `vi/chapter1/README.vi.md` (dịch từ 211 dòng / 1051 Hán; 17 ảnh; 160 Hán trong fence → giữ fence nguyên văn nếu là code, dich nếu là output/comment).
- [ ] `vi/chapter1/dive-tuning.vi.ipynb` (mirror 98–100%: dich 1 lần, đổ vào markdown cells).
- [ ] Commit `ch1: README + notebook`.

### Task 3 — Chương 2: Học theo prompt và CoT
- [ ] `vi/chapter2/README.vi.md` · [ ] `dive-prompting.vi.ipynb` (mirror) · [ ] Commit.

### Task 4 — Chương 3: Chỉnh sửa tri thức
- [ ] `vi/chapter3/README.vi.md` · [ ] `dive_edit.vi.ipynb` (mirror) · [ ] Commit.

### Task 5 — Chương 4: Suy luận toán học
- [ ] `vi/chapter4/README.vi.md` (dịch độc lập — trùng 12.7%).
- [ ] `vi/chapter4/sft_math.vi.ipynb`: dich 650 Hán markdown + **chỉ comment `#`** trong code (407 Hán), giữ chuỗi literal tiếng Trung.
- [ ] Commit.

### Task 6 — Chương 5: Watermark
- [ ] `vi/chapter5/README.vi.md` · [ ] `watermark.vi.ipynb` (mirror) · [ ] Commit.

### Task 7 — Chương 6: Tấn công jailbreak
- [ ] `vi/chapter6/README.vi.md` — 16 prompt tấn công trong fence giữ nguyên văn.
- [ ] `dive-jailbreak.vi.ipynb` (mirror) · [ ] Commit.

### Task 8 — Chương 7: Giấu tin (steganography)
- [ ] `vi/chapter7/README.vi.md` (458 Hán).
- [x] `llm_stega.ipynb` bỏ qua (0 Hán).
- [ ] Commit.

### Task 9 — Chương 8: Mô hình đa phương tiện
- [ ] `vi/chapter8/README.vi.md` (348 dòng / 2026 Hán — chia 2 lượt).
- [ ] `mllms.vi.ipynb` (mirror) · [ ] Commit.

### Task 10 — Chương 9: Agent GUI
- [ ] `vi/chapter9/README.vi.md` và `GUIagent.vi.ipynb` dịch **độc lập** (trùng 64.4%).
- [ ] Commit.

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
| 1 | `vi/README.vi.md` | ✅ | pending |
| 2–12 | Chương 1–11 | ⬜ | — |
| 13 | PDF slides | ⬜ | — |
| 14 | QA + link ngược | ⬜ | — |

Ước lượng: Markdown+notebook ~9–10 giờ; PDF ~495 trang (bớt 2 file 0 Hán trích được → còn ~330 trang có chữ thật để dịch).
