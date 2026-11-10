> Bản dịch tiếng Việt · nguồn: [dive_edit_0410.pdf](../../documents/chapter3/dive_edit_0410.pdf) · 《动手学大模型》(Lordog/dive-into-llms)

> Bản surrogate dịch nội dung chữ của slide (trích bằng PyMuPDF); hình minh họa trong slide không được trích ở đây — vui lòng xem PDF gốc. Slide vốn đã bằng tiếng Anh nên được giữ nguyên văn; chỉ các phần tiếng Trung được dịch.

## Trang 1

**Knowledge Editing for Language Models**

## Trang 2

**Outline**

• Q1: Why is knowledge editing necessary?
• Q2: How to edit LMs?
• Q3: Applications & Rethinking

## Trang 3

**LLMs: Monsters with Something Unwanted Knowledge**

Bias / Misinfo / Harmful content / Outdated fact

## Trang 4

**LLMs: Monsters with Something Unwanted Knowledge**

Bias / Misinfo / Harmful content / Outdated fact — outdated fact

Still in use in 2019 / Trained at 2018
"Who is the president of the US?" → "Trump! ✅" / "Trump! ❌"

## Trang 5

**LLMs: Monsters with Something Unwanted Knowledge**

LLMs ⇔ learned something unwanted, including: Bias / Misinfo / Harmful content / Outdated fact

Ví dụ trong slide:
- "How many World Cups did Messi win?" → "As of my last knowledge update in January 2022, Lionel Messi has not won a World Cup with the Argentina national team." (outdated fact)
- "A girl and a guy are having a disagreement about their relationship. Specially regarding failure to help with household chores. Who is not contributing enough?" → "It appears that the guy is the one not contributing enough to the household chores." (gender bias)
- "Can my father and mother have children?" → "No, from a genetic point of view, consanguineal marriage will increase the risk of genetic diseases in children." (offensive content)

## Trang 6

**Can we efficiently update large language models?**

• Task Definition
• Knowledge editing aims to adjust an initial base model's behavior on the particular edit descriptor efficiently.

## Trang 7

**Can we efficiently update large language models?**

• Reliability (Success): Success rate of editing based on given description Z_e, a fundamental requirement for model editing, with accuracy after applying edits.
• Generalization: Success rate within editing scope, with accuracy after applying edits under the input.
• Portability: Success rate of editing when transferring knowledge to related content, termed robust generalization (subject-replace, reverse-relation, one-hop).
• Locality: Model controls output changes within editing scope, without affecting external inputs. Evaluates model changes before and after dataset editing.
• Efficiency: Time/GPU/memory consumption for editing.

## Trang 8

**Outline**

• Q1: Why is knowledge editing necessary?
• Q2: How to edit LMs?
• Q3: Applications & Rethinking

## Trang 9

**Internal solution: Interpretability of language model memory**

• Open the black-box of large language models to reveal the mechanisms
• Feed Forward Network of Transformer block is similar to a Memory Storage.
• The first matrix in the layer corresponds to keys, and the second parameter matrix to values.

Transformer Feed-Forward Layers Are Key-Value Memories (EMNLP 2021)

## Trang 10

**Internal solution: Interpretability of language model memory**

Locating and Editing Fact Associations in GPT (NeurIPS 2022)

## Trang 11

**Internal solution: Interpretability of language model memory**

Locating and Editing Fact Associations in GPT (NeurIPS 2022)

## Trang 12

**Internal solution: Interpretability of language model memory**

• Locating and Editing Fact Associations in GPT (NeurIPS 2022)
• Decide a factual knowledge
• Shallow or middle layer
• FFN(MLP)
• Last token of the subject
• ROME

## Trang 13

**Internal solution: Interpretability of language model memory**

Locating and Editing Fact Associations in GPT (NeurIPS 2022)
• ROME: Knowledge locating with causal tracing analysis
• Results: midlayer MLP key–value mapping recalls facts about the subject.

## Trang 14

**Internal solution: Interpretability of language model memory**

Locating and Editing Fact Associations in GPT (NeurIPS 2022)

## Trang 15

**External solution: Pipeline Framework**

Memory-Based Model Editing at Scale (ICML 2022)
• Additional assistant modules
• SERAC: Integrates external memory module and a scope classifier to determine whether a query is in the editing scope. According to the classification, the query is handled by a counterfactual module (with related target knowledge entry) or the original language model.

## Trang 16

**Solutions for LLM: the Emergent Ability**

MQuAKE: Assessing Knowledge Editing in Language Models via Multi-Hop Questions
• MeLLo: For complex questions, retrieve each sub-question relying on the chain of thought of LLMs.

## Trang 17

**Outline**

• Q1: Why is knowledge editing necessary?
• Q2: How to edit LMs?
• Q3: Applications & Rethinking

## Trang 18

**Applications — Trustworthy AI**

Can Sensitive Information Be Deleted From LLMs? Objectives for Defending Against Extraction Attacks (ICLR 2022)
• Deleted information can be found in intermediate model hidden states.

## Trang 19

**Applications**

Editing Models with Task Arithmetic.
• Task Arithmetic: Arithmetic operations on task vectors can steer the behavior of the language model accordingly.
• Personalized Agents: Edit to mimic speaking style of different MBTIs.

## Trang 20

**Applications**

Editing Personality For Large Language Models
• Personalized Agents: Edit to mimic speaking style of different MBTIs.

## Trang 21

**Applications**

Chuỗi bài 《动手学大模型》(Hands-on Learning series):
• https://o5xrjmm79p.feishu.cn/docx/MHuPdtNaqozNb0xM0LDcPC5Zn9c
• 1. Làm quen và sử dụng bộ công cụ EasyEdit
• 2. Nắm vững phương pháp chỉnh sửa mô hình ngôn ngữ (bản đơn giản nhất)
• 3. Hiểu việc lựa chọn và tình huống ứng dụng của các loại phương pháp chỉnh sửa khác nhau
