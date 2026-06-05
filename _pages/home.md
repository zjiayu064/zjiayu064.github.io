---
permalink: /home/
title: "Home"
excerpt: ""
layout: default
author_profile: true
redirect_from:
  - /
  - /about/
  - /about.html
---

<span id="biography"></span>

## Biography

I am a master's student in Microelectronics at the [School of Microelectronics](http://sme.ustc.edu.cn/), **University of Science and Technology of China (USTC)**, advised by Assoc. Prof. [Song Chen](http://staff.ustc.edu.cn/~songch/). I am currently a CSC-sponsored visiting graduate student at **Nanyang Technological University (NTU)**, hosted by Assoc. Prof. [Weichen Liu](https://personal.ntu.edu.sg/liu/#about).

My research lies at the intersection of **AI systems** and **electronic design automation (EDA)**. I work on efficient inference and compression for large language models, particularly **Mixture-of-Experts (MoE) LLMs**, and on **structure-aware LLM pipelines** for hardware code generation. I am drawn to problems that pair algorithmic insight with systems-level efficiency.

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
  <div class="paper-figure"><img src="{{ '/images/BitsMoE.png' | relative_url }}" alt="BitsMoE overview" /></div>
  <div class="paper-text">
    <p><strong>BitsMoE: Efficient Spectral Energy-Guided Bit Allocation for MoE LLM Quantization.</strong> arXiv preprint, 2026. (<a href="https://arxiv.org/abs/2606.00079">Paper</a>) (<a href="https://github.com/zjiayu064/BitsMoE">Code</a>)</p>
    <p>Introduces <strong>spectral energy-guided bit allocation</strong> for <strong>MoE LLM quantization</strong>, using activation-aware mixed precision to preserve expert-specific capacity under low-bit memory budgets.</p>
    <p class="paper-keywords">Keywords: MoE LLMs; mixed-precision quantization; spectral energy; efficient inference.</p>
  </div>
</div>

---

## Education

**University of Science and Technology of China (USTC)**, Anhui, China<br>
M.Sc. student in Microelectronics, School of Microelectronics · *Sep 2024 – Jun 2027 (expected)*<br>
Advisor: Assoc. Prof. [Song Chen](http://staff.ustc.edu.cn/~songch/)

My master's training focuses on efficient large language model systems and model compression, with current work on mixed-precision quantization and efficient inference for MoE LLMs. I am also involved in LLM-based EDA research, especially structure-aware RTL and Verilog generation.

**Nanyang Technological University (NTU)**, Singapore<br>
Visiting Graduate Student, College of Computing and Data Science (CCDS) · *Aug 2025 – Jul 2026*<br>
Host Supervisor: Assoc. Prof. [Weichen Liu](https://personal.ntu.edu.sg/liu/#about)

I am visiting NTU under the China Scholarship Council (CSC) joint master's training program, working on efficient inference and quantization methods for sparse LLMs.

**University of Science and Technology of China (USTC)**, Anhui, China<br>
B.Sc. in Physics, Minor in Computer Science · *Sep 2020 – Jun 2024*

During my undergraduate study, I built a foundation in physics, mathematics, and computer science, and gradually shifted my research focus toward AI systems, model compression, and hardware-aware machine learning.
