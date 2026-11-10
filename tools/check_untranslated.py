"""Kiem tra ky tu Trung con sot trong ban dich + doi chieu so luong anh/link/code block.

Usage:
    python tools/check_untranslated.py                # kiem tra moi file *.vi.*
    python tools/check_untranslated.py --names        # in ten rieng Trung du phep
"""
import argparse
import glob
import json
import os
import re

HAN = re.compile(r"[\u4e00-\u9fff]")
FENCE = re.compile(r"```[^\n]*\n[\s\S]*?```")
IMG = re.compile(r"!\[[^\]]*\]\([^)]*\)")
LINK = re.compile(r"\]\(([^)]*)\)")

# Ten rieng / cum tu Trung Quoc du giu nguyen trong ban dich
ALLOWED = [
    "动手学大模型",
    "大模型开发全流程",
    "上海交通大学",
    "华为昇腾",
    "张倬胜",
    "袁童鑫",
    "马欣贝",
    "何志威",
    "杜巍",
    "赵皓东",
    "吴宗儒",
    "吴铮",
    "董凌众",
    "张玉龙",
    "费豪",
    "刘功申",
    "陈星宇",
    "程彭洲",
    "鞠天杰",
    "闫子赫",
    "姚杳",
    "自然语言处理前沿技术",
    "人工智能安全技术",
    "谢乾",
    "程黎明",
    "楼梨华",
    "焦泽昱",
]


def texts_of(path):
    if path.endswith(".ipynb"):
        nb = json.load(open(path, encoding="utf-8"))
        cells = nb.get("cells") or [
            c for w in nb.get("worksheets", []) for c in w.get("cells", [])
        ]
        out = []
        for c in cells:
            src = c.get("source")
            if isinstance(src, list):
                src = "".join(src)
            out.append(src)
        return "\n\n".join(out)
    return open(path, encoding="utf-8").read()


def stats(text):
    stripped = text
    for name in ALLOWED:
        stripped = stripped.replace(name, "")
    return {
        "han": len(HAN.findall(stripped)),
        "han_raw": len(HAN.findall(text)),
        "images": len(IMG.findall(text)),
        "links": len(LINK.findall(text)),
        "fences": text.count("```") // 2,
        "lines": text.count("\n") + 1,
    }


def source_of(vi):
    """Map vi/chapterN/X.vi.md -> documents/chapterN/X.md (duong dan duoi v//)."""
    vi_posix = vi.replace("\\", "/")
    m = re.match(r"^vi/(chapter\d+)/(.+)\.vi\.(md|ipynb)$", vi_posix)
    if m:
        ch, name, ext = m.groups()
        if name.endswith(".slides"):
            return None  # surrogate PDF: khong doi chieu duoc voi file PDF
        cand = [f"documents/{ch}/{name}.{ext}"]
        for c in cand:
            if os.path.exists(c):
                return c
        return cand[0]  # de bao "thieu file goc"
    if vi_posix == "vi/README.vi.md":
        return "README.md"
    return None  # PDF surrogate/OCR: khong doi chieu


def strip_attrib(text):
    """Bo dong nguon dau file de doi chieu cau truc (anh/link/fence) khong bi lech +1."""
    lines = text.split("\n")
    if lines and lines[0].startswith("> ") and "·" in lines[0]:
        return "\n".join(lines[1:])
    return text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--names", action="store_true", help="in danh sach ten duoc giu nguyen")
    args = ap.parse_args()
    if args.names:
        print("\n".join(ALLOWED))
        return

    vi_files = sorted(glob.glob("vi/**/*.vi.md", recursive=True) + glob.glob("vi/**/*.vi.ipynb", recursive=True))
    if not vi_files:
        print("Chua co file ban dich trong vi/ (*.vi.md / *.vi.ipynb).")
        return

    bad = 0
    print(f"{'FILE':<48}{'HAN':>6}{'RAW':>6}{'IMG':>5}{'LNK':>5}{'FNC':>5}  DOI CHIEU")
    for vi in vi_files:
        src = source_of(vi)
        try:
            vi_text = texts_of(vi)
        except FileNotFoundError:
            print(f"{vi:<48}  (khong ton tai)")
            continue
        v = stats(vi_text)
        note = []
        if src:
            try:
                s = stats(texts_of(src))
                vs = stats(strip_attrib(vi_text))
                for key, label in (("images", "anh"), ("links", "link"), ("fences", "code block")):
                    if vs[key] != s[key]:
                        note.append(f"{label}: {s[key]} -> {v[key]}")
            except FileNotFoundError:
                note.append("thieu file goc")
        if v["han"]:
            bad += 1
            note.append("CON TIENG TRUNG")
        flag = "OK " if not note else "!! "
        print(f"{vi:<48}{v['han']:>6}{v['han_raw']:>6}{v['images']:>5}{v['links']:>5}{v['fences']:>5}  {flag}{'; '.join(note)}")
    print(f"\n{len(vi_files)} file da dich, {bad} file con ky tu Trung (ngoai ten rieng).")


if __name__ == "__main__":
    main()
