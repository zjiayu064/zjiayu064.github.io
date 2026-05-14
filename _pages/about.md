---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<span id="about"></span>

## About

I am a master's student in Microelectronics at the **University of Science and Technology of China (USTC)**, advised by Assoc. Prof. Song Chen. I am currently a CSC-sponsored visiting graduate student at **Nanyang Technological University (NTU)**, hosted by Assoc. Prof. Weichen Liu.

My research lies at the intersection of **AI systems** and **electronic design automation (EDA)**. I work on efficient inference and compression for large language models, particularly **Mixture-of-Experts (MoE) LLMs**, and on **structure-aware LLM pipelines** for hardware code generation. I am drawn to problems that pair algorithmic insight with systems-level efficiency.

I am actively seeking **PhD opportunities** in LLM systems, efficient inference for sparse LLMs, and EDA-oriented foundation models.

---

<span id="research"></span>

## Research Interests

- **Compression and adaptive quantization for MoE LLMs** — mixed-precision allocation, spectral decomposition, activation-aware bit budgeting
- **Efficient inference for sparse LLMs** — throughput and latency optimization, expert-aware serving, KV-cache and memory efficiency
- **LLMs for EDA and hardware design automation** — design understanding, automated RTL workflows, hardware-aware generation
- **Structure-aware LLMs for RTL / Verilog generation** — retrieval-augmented generation, graph-based hardware representations, multimodal soft prompting
- **LLM agents for EDA** — tool-integrated reasoning with synthesis and verification feedback

---

## Education

**University of Science and Technology of China (USTC)**, Anhui, China  
M.Sc. in Microelectronics · *Sep 2024 – Jun 2027 (expected)*  
GPA: 3.85 / 4.30 (90.26 / 100) · Ranking: 9 / 126 · Advisor: Assoc. Prof. Song Chen

**Nanyang Technological University (NTU)**, Singapore  
Visiting Graduate Student, College of Computing and Data Science (CCDS) · *Aug 2025 – Jul 2026*  
CSC-sponsored Joint Master's Training · Host Supervisor: Assoc. Prof. Weichen Liu

**University of Science and Technology of China (USTC)**, Anhui, China  
B.Sc. in Physics (Minor in Computer Science) · *Sep 2020 – Jun 2024*  
GPA: 3.50 / 4.30 (85.50 / 100)

---

## Selected Research

### Efficient Quantization for MoE LLMs
*Aug 2025 – Apr 2026 · NTU & USTC · First Author*

Research on mixed-precision quantization for MoE LLMs, targeting strict memory budgets in practical deployment. Explored adaptive bit allocation strategies that exploit cross-expert weight redundancy, with substantial gains in decoding throughput and time-to-first-token under low-bit settings. *(Manuscript under review; details withheld for double-blind review.)*

### Structure-Aware LLM-Based Verilog / RTL Generation
*Apr 2025 – Nov 2025 · USTC · First Author*

Research on retrieval-augmented Verilog code generation that integrates hardware-structural information into LLM-based RTL pipelines, combining graph-based design representations with multimodal soft prompting to improve functional correctness on standard benchmarks. *(Manuscript under review; details withheld for double-blind review.)*

### EI²Det: Visible-Infrared Object Detection
*Jul 2024 – Sep 2024 · USTC · Research Contributor*

Contributed to the experimental evaluation of a visible-infrared object detection framework targeting robust perception under challenging illumination. Implemented and benchmarked YOLOv5, YOLOv7, YOLOv10, and YOLOX baselines and helped organize the experimental results for the final journal submission. *(Published in IEEE TCSVT, 2025.)*

### Low-Bit Quantization of Llama 2 for Resource-Constrained Deployment
*Jul 2024 – Dec 2024 · USTC*

Implemented fixed-point quantization for Llama 2, including nonlinear operators such as softmax and exponential functions, for efficient deployment on resource-constrained hardware. Extended the pipeline to weight-activation quantization while maintaining comparable WikiText-2 perplexity, with perplexity rising only from 5.47 to 5.50 under W8A8 and 5.64 under W6A6.

---

<span id="publications"></span>

## Publications

**Peer-Reviewed**

- Ke Hu, Yudong He, Yuan Li, **Jiayu Zhao**, Song Chen, and Yi Kang.  
  *EI²Det: Edge-Guided Illumination-Aware Interactive Learning for Visible-Infrared Object Detection.*  
  **IEEE Transactions on Circuits and Systems for Video Technology (TCSVT)**, vol. 35, no. 7, pp. 7101–7115, Jul. 2025.  
  DOI: [10.1109/TCSVT.2025.3539625](https://doi.org/10.1109/TCSVT.2025.3539625)

*Two first-author manuscripts are currently under review. Details withheld for double-blind review.*

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

I welcome discussions about research collaborations and PhD opportunities.

- **Email:** [jiayz@mail.ustc.edu.cn](mailto:jiayz@mail.ustc.edu.cn)
- **Phone:** +86 183 1214 4980
- **Address:** 99 South Jinzhai Rd., Hefei, Anhui, China
- **GitHub:** [github.com/zjiayu064](https://github.com/zjiayu064)
- **Google Scholar:** [Jiayu Zhao](https://scholar.google.com/citations?user=ttJ0zcEAAAAJ)
