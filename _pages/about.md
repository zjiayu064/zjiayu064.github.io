---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<span id="biography"></span>

## Biography

I am a master's student in Microelectronics at the [School of Microelectronics](http://sme.ustc.edu.cn/), **University of Science and Technology of China (USTC)**, advised by Assoc. Prof. [Song Chen](http://staff.ustc.edu.cn/~songch/). I am currently a CSC-sponsored visiting graduate student at **Nanyang Technological University (NTU)**, hosted by Assoc. Prof. [Weichen Liu](https://personal.ntu.edu.sg/liu/#about).

My research lies at the intersection of **AI systems** and **electronic design automation (EDA)**. I work on efficient inference and compression for large language models, particularly **Mixture-of-Experts (MoE) LLMs**, and on **structure-aware LLM pipelines** for hardware code generation. I am drawn to problems that pair algorithmic insight with systems-level efficiency.

I am actively seeking **PhD opportunities** in LLM systems, efficient inference for sparse LLMs, and EDA-oriented foundation models.

---

## Recent News

<div class="infoblock">
<div class="blockcontent">
<ul>
<li><p>May/2026: <strong>BitsMoE</strong> is available on arXiv, focusing on mixed-precision quantization for MoE LLMs.</p></li>
</ul>
</div>
</div>

---

<span id="research"></span>

## Research Interests

- **MoE LLMs efficient inference:** mixed-precision quantization, expert-aware compression, memory-efficient serving
- **Compression and adaptive quantization for MoE LLMs:** spectral decomposition, activation-aware bit budgeting, ultra-low-bit deployment
- **LLMs for EDA and hardware design automation:** design understanding, automated RTL workflows, hardware-aware generation
- **Structure-aware LLMs for RTL / Verilog generation:** retrieval-augmented generation, graph-based hardware representations, multimodal soft prompting
- **LLM agents for EDA:** tool-integrated reasoning with synthesis and verification feedback

---

## Selected Research Directions

### MoE LLMs Efficient Inference

Efficient MoE deployment requires preserving expert-specialized capacity while reducing resident memory and inference overhead. My work studies quantization and allocation strategies that make sparse LLMs practical under strict deployment budgets.

<div class="paper-card">
  <div class="paper-figure"><img src="images/BitsMoE.png" alt="BitsMoE overview" /></div>
  <div class="paper-text">
    <p><strong>BitsMoE: Efficient Spectral Energy-Guided Bit Allocation for MoE LLM Quantization.</strong> arXiv preprint, 2026. (<a href="https://arxiv.org/abs/2606.00079">Paper</a>) (<a href="https://github.com/zjiayu064/BitsMoE">Code</a>)</p>
    <p>Introduces <strong>spectral energy-guided bit allocation</strong> for <strong>MoE LLM quantization</strong>, using activation-aware mixed precision to preserve expert-specific capacity under low-bit memory budgets.</p>
    <p class="paper-keywords">Keywords: MoE LLMs; mixed-precision quantization; spectral energy; efficient inference.</p>
  </div>
</div>

---

## Education

**University of Science and Technology of China (USTC)**, Anhui, China  
M.Sc. in Microelectronics · *Sep 2024 – Jun 2027 (expected)*  
GPA: 3.85 / 4.30 (90.26 / 100) · Ranking: 9 / 126 · Advisor: Assoc. Prof. [Song Chen](http://staff.ustc.edu.cn/~songch/)

**University of Science and Technology of China (USTC)**, Anhui, China  
B.Sc. in Physics (Minor in Computer Science) · *Sep 2020 – Jun 2024*  
GPA: 3.50 / 4.30 (85.50 / 100)

---

## Visiting Experience

**Nanyang Technological University (NTU)**, Singapore  
Visiting Graduate Student, College of Computing and Data Science (CCDS) · *Aug 2025 – Jul 2026*  
CSC-sponsored Joint Master's Training under the State Scholarship Fund  
Host Supervisor: Assoc. Prof. [Weichen Liu](https://personal.ntu.edu.sg/liu/#about)

---

<span id="publications"></span>

## Publications

**Peer-Reviewed**

- Ke Hu, Yudong He, Yuan Li, **Jiayu Zhao**, Song Chen, and Yi Kang.  
  *EI²Det: Edge-Guided Illumination-Aware Interactive Learning for Visible-Infrared Object Detection.*  
  **IEEE Transactions on Circuits and Systems for Video Technology (TCSVT)**, vol. 35, no. 7, pp. 7101–7115, Jul. 2025.  
  DOI: [10.1109/TCSVT.2025.3539625](https://doi.org/10.1109/TCSVT.2025.3539625)

**Preprints**

- **Jiayu Zhao**, Zihan Teng, Minhao Fan, Tianrui Ma, Wentao Ren, Song Chen, and Weichen Liu.<br>
  *BitsMoE: Efficient Spectral Energy-Guided Bit Allocation for MoE LLM Quantization.*<br>
  arXiv preprint, 2026.<br>
  [Paper](https://arxiv.org/abs/2606.00079) · [Code](https://github.com/zjiayu064/BitsMoE)

---

<span id="awards"></span>

## Awards & Scholarships

| Award | Year |
|---|---|
| State Scholarship Fund Scholarship, China Scholarship Council (CSC) | 2025–2026 |
| Second-Class Academic Scholarship for Master's Students, USTC | 2025 |
| First-Class Academic Scholarship for Master's Students, USTC | 2024 |
| Scholarship for Outstanding Students of USTC (Bronze Award) | 2020–2024 |
| Endeavour Scholarship | 2021 |

---

<span id="skills"></span>

## Skills

- **Programming & Systems:** Python, C/C++, CUDA, Linux, Slurm, Git, LaTeX
- **LLMs & Model Compression:** PyTorch, Hugging Face Transformers, vLLM, MoE inference, LLM quantization, Gurobi / ILP
- **EDA & Hardware Design:** Verilog / SystemVerilog, Yosys, RTL design, logic synthesis, digital IC design flow
- **Performance Profiling:** Nsight Systems, Nsight Compute
- **Evaluation:** LLM benchmarking, inference efficiency analysis, RTL functional verification

---

## Contact

- **Email:** [jiayz@mail.ustc.edu.cn](mailto:jiayz@mail.ustc.edu.cn)
- **Address:** 99 South Jinzhai Rd., Hefei, Anhui, China
- **GitHub:** [github.com/zjiayu064](https://github.com/zjiayu064)
- **Google Scholar:** [Jiayu Zhao](https://scholar.google.com/citations?user=ttJ0zcEAAAAJ)
