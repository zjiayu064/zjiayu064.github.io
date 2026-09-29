---
permalink: /home/
title: "Home"
excerpt: ""
layout: default
show_profile: true
redirect_from:
  - /
  - /about/
  - /about.html
---

<span id="biography"></span>

## Biography

I am currently a third-year master's student at the [School of Microelectronics](http://sme.ustc.edu.cn/), **[University of Science and Technology of China (USTC)](https://en.ustc.edu.cn/)**, supervised by Assoc. Prof. [Song Chen](http://staff.ustc.edu.cn/~songch/) since Sep. 2024. Prior to that, I obtained my B.S. degree in Physics from the [School of Physical Sciences](https://en.physics.ustc.edu.cn/) at [USTC](https://en.ustc.edu.cn/) in 2024.

My research lies at the intersection of **AI systems** and **electronic design automation (EDA)**. I work on efficient inference and compression for large language models, particularly **Mixture-of-Experts (MoE) LLMs**, and on **structure-aware LLM pipelines** for hardware code generation.

---

## Recent News

<div class="infoblock">
<div class="blockcontent">
<ul>
<li><p>Sep/2026: <strong>VeriGRAG</strong> is accepted by <strong>ASPDAC 2027</strong>.</p></li>
<li><p>May/2026: <strong>BitsMoE</strong> is available on arXiv, focusing on mixed-precision quantization for MoE LLMs.</p></li>
</ul>
</div>
</div>

---

## Research Interests

My research interests include:

- **Efficient MoE LLMs**: quantization, model compression, and efficient inference.
- **LLMs for RTL Generation and Verification**: structure-aware code generation and verification-aware reasoning.

---

## Selected Research Directions

### MoE LLMs Efficient Inference

Efficient MoE deployment requires preserving expert-specialized capacity while reducing resident memory and inference overhead. My work studies quantization and allocation strategies that make sparse LLMs practical under strict deployment budgets.

<div class="paper-card">
  <div class="paper-figure"><img src="{{ '/images/BitsMoE.png' | relative_url }}" alt="BitsMoE overview" /></div>
  <div class="paper-text">
    <p><strong>BitsMoE: Cost-Aware Bit Allocation in Spectral Space for MoE LLM Quantization.</strong> arXiv preprint, 2026. (<a href="https://arxiv.org/abs/2606.00079">Paper</a>) (<a href="https://github.com/zjiayu064/BitsMoE">Code</a>)</p>
    <p>Combines <strong>shared-basis spectral decomposition</strong> with <strong>factorized quantization cost modeling</strong> to allocate bits across expert-specific spectral components under a fixed memory budget, enabling accurate low-bit MoE quantization and efficient GPU inference.</p>
    <p class="paper-keywords">Keywords: MoE LLMs; mixed-precision quantization; spectral decomposition; cost-aware bit allocation; efficient inference.</p>
  </div>
</div>

---

## Education

- M.Sc., [School of Microelectronics](http://sme.ustc.edu.cn/), [University of Science and Technology of China (USTC)](https://en.ustc.edu.cn/), Sep/2024 - Jun/2027 (expected)
- B.Sc. in Physics, Minor in Computer Science, [School of Physical Sciences](https://en.physics.ustc.edu.cn/), [University of Science and Technology of China (USTC)](https://en.ustc.edu.cn/), Sep/2020 - Jun/2024

---

## Experience

[Parallel and Distributed Computing Lab (PDCL)](https://www.ntu.edu.sg/pdcl), [SCSE](https://www.ntu.edu.sg/computing/home), [Nanyang Technological University (NTU)](https://www.ntu.edu.sg/), Singapore

- Visiting Master, Aug. 2025 - Jul. 2026
- Supervised by [Prof. Weichen Liu](https://personal.ntu.edu.sg/liu/)

{% include visitor-count.html %}
