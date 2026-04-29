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

My research sits at the intersection of **AI systems** and **electronic design automation (EDA)**, with a focus on building efficient and reliable LLM pipelines for hardware code generation and large-scale model deployment. I am particularly interested in problems that combine algorithmic innovation with systems-level efficiency.

I am actively seeking **PhD opportunities** in LLM systems, EDA-oriented foundation models, and efficient model inference.

---

<span id="research"></span>

## Research Interests

- **LLMs for EDA** — hardware-aware generation, automated RTL workflows, and design understanding
- **Verilog / RTL code generation** — retrieval-augmented and structure-aware model pipelines
- **Efficient LLM inference** — throughput/latency optimization, KV-cache compression, runtime efficiency
- **MoE model compression** — low-bit quantization, adaptive bit allocation, memory-efficient serving
- **LLM agents for code and hardware** — tool-integrated reasoning, synthesis/verification feedback loops

---

## Education

**University of Science and Technology of China (USTC)**, Anhui, China  
M.Sc. in Microelectronics · *Sep 2024 – Jun 2027 (expected)*  
GPA: 3.85 / 4.30 (90.26 / 100) · Ranking: Top 8% · Advisor: Assoc. Prof. Song Chen

**Nanyang Technological University (NTU)**, Singapore  
Visiting Graduate Student (CSC-sponsored) · *Aug 2025 – Jul 2026*  
Host Advisor: Assoc. Prof. Weichen Liu

**University of Science and Technology of China (USTC)**, Anhui, China  
B.Sc. in Physics (Minor in Computer Science) · *Sep 2020 – Jun 2024*  
GPA: 3.50 / 4.30 (85.58 / 100)

---

## Selected Research

### Efficient LLM Inference and MoE Model Compression
*Aug 2025 – Apr 2026 · NTU & USTC*

Research on mixed-precision quantization for MoE LLMs, targeting strict memory budgets in practical deployment. Key contributions include an adaptive bit allocation strategy that exploits cross-expert weight redundancy, achieving significant improvements in decoding throughput and time-to-first-token under low-bit settings. *(Manuscript under review; details withheld for double-blind review.)*

### Structure-Aware LLM-Based Verilog / RTL Generation
*Apr 2025 – Nov 2025 · USTC*

Research on retrieval-augmented Verilog code generation by integrating hardware structural information into LLM-based RTL pipelines. The work involves datapath graph extraction, graph neural network encoding, and multimodal soft-prompting to improve functional correctness on standard benchmarks. *(Manuscript under review; details withheld for double-blind review.)*

### Low-Bit Quantization of Llama 2 for Resource-Constrained Deployment
*Jul 2024 – Dec 2024 · USTC*

Implemented fixed-point quantization for Llama 2 targeting hardware with limited compute resources. Quantized key nonlinear operators (softmax, exponential) from FP16 to INT8, achieving minimal perplexity degradation (5.47 → 5.63 on WikiText) with a substantially reduced memory footprint.

### DRAM PIM Memory Access Optimization
*Nov 2023 – Apr 2024 · USTC*

Built a DRAM memory access model based on SmartShuttle to analyze loop tiling and scheduling strategies for processing-in-memory (PIM) architectures. Identified memory-access trends across buffer sizes and scheduling policies to inform efficient hardware configuration choices.

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
| Second-Class Academic Scholarship for Master's Students, USTC | 2025 |
| First-Class Academic Scholarship for Master's Students, USTC | 2024 |
| Scholarship for Outstanding Students of USTC (Bronze Award) | 2020–2024 |
| Endeavour Scholarship | 2021 |

---

<span id="skills"></span>

## Skills

- **Programming:** Python, C/C++, CUDA, Verilog/SystemVerilog, MATLAB, Bash
- **ML / LLM Systems:** PyTorch, Hugging Face Transformers, vLLM, LLM quantization, MoE inference, efficient LLM deployment
- **EDA & IC Design:** Yosys, Verilog HDL, logic synthesis, digital IC design flow, Synopsys / Cadence tools
- **Systems & Profiling:** Linux, Slurm, Git, LaTeX, Nsight Systems, Nsight Compute
- **Evaluation:** LLM benchmarking, inference efficiency analysis, RTL functional verification

---

## Contact

I welcome discussions about research collaborations and PhD opportunities.

- **Email:** [jiayz@mail.ustc.edu.cn](mailto:jiayz@mail.ustc.edu.cn)
- **Phone:** +86 183 1214 4980
- **Address:** 99 South Jinzhai Rd., Hefei, Anhui, China
- **GitHub:** [github.com/zjiayu064](https://github.com/zjiayu064)  <!-- [PLACEHOLDER] Update if username differs -->
- **Google Scholar:** [Jiayu Zhao](https://scholar.google.com/citations?user=ttJ0zcEAAAAJ)
