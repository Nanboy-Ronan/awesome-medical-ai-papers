# Awesome Medical AI Papers [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of medical AI, healthcare AI, and medical imaging papers published at top CS/AI conferences: **CVPR, NeurIPS, ICLR, ICCV, ECCV, ACL, EMNLP, AAAI, KDD**, and more.

Covers **2023–2025**. Organized by conference. Contributions welcome — see [Contributing](#contributing).

---

## Legend

| Icon | Topic |
|------|-------|
| 🔬 | Medical Imaging & Segmentation |
| 🧫 | Computational Pathology |
| 🤖 | Foundation Models & Vision-Language |
| 📋 | Clinical NLP & EHR |
| 🧠 | Neuroimaging & Brain AI |

---

## Contents

- [CVPR](#cvpr)
- [NeurIPS](#neurips)
- [ICLR](#iclr)
- [ICCV / ECCV](#iccv--eccv)
- [ACL / EMNLP](#acl--emnlp)
- [AAAI](#aaai)
- [KDD](#kdd)
- [Contributing](#contributing)

---

## CVPR

### CVPR 2025

#### 🔬 Medical Imaging & Segmentation

- **[Interactive Medical Image Segmentation: A Benchmark Dataset and Baseline](https://arxiv.org/abs/2411.12814)** — Introduces IMIS-Bench, a comprehensive benchmark for interactive medical image segmentation across diverse modalities and organs.
- **[LesionLocator: Zero-Shot Universal Tumor Segmentation and Tracking in 3D Whole-Body Imaging](https://arxiv.org/pdf/2502.20985)** — Zero-shot framework for tumor segmentation and longitudinal tracking across unseen tumor types in whole-body 3D scans.
- **[Latent Drifting in Diffusion Models for Counterfactual Medical Image Synthesis](https://arxiv.org/abs/2412.20651)** — Generates counterfactual medical images by drifting in the latent space of diffusion models, enabling controlled pathology simulation.
- **[DyCON: Dynamic Uncertainty-aware Consistency and Contrastive Learning for Semi-supervised Medical Image Segmentation](https://arxiv.org/abs/2504.04566)** — Uncertainty-aware consistency and contrastive objectives for semi-supervised volumetric segmentation.
- **[Multi-modal Medical Diagnosis via Large-small Model Collaboration](https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_Multi-modal_Medical_Diagnosis_via_Large-small_Model_Collaboration_CVPR_2025_paper.pdf)** — Collaborative inference framework between large and small models for multi-modal clinical diagnosis.

#### 🤖 Foundation Models & Vision-Language

- **[CheXWorld: Exploring Image World Modeling for Radiograph Representation Learning](https://arxiv.org/abs/2504.13820)** — Applies world modeling principles to chest X-ray pre-training, improving downstream diagnostic performance.
- **[EchoWorld: Learning Motion-Aware World Models for Echocardiography Video Understanding](https://arxiv.org/abs/2504.13065)** — Motion-aware world model pre-trained on echocardiography videos for cardiac function assessment.
- **[VILA-M3: Enhancing Vision-Language Models with Medical Expert Knowledge](https://arxiv.org/abs/2411.12915)** — Integrates structured medical expert knowledge into VLMs for clinical image understanding.
- **[BiomedCoOp: Learning to Prompt for Biomedical Vision-Language Models](https://arxiv.org/abs/2411.15232)** — Context optimization for prompt learning in biomedical vision-language models.
- **[BIOMEDICA: An Open Biomedical Image-Caption Archive and Vision-Language Models Derived from Scientific Literature](https://arxiv.org/abs/2501.07171)** — Large-scale open archive of biomedical image-caption pairs mined from scientific literature.
- **[MedUnifier: Unifying Vision-and-Language Pre-training for Medical Vision-Language Models with Pixel-level Image Editing](https://arxiv.org/abs/2503.01019)** — Unified pre-training framework bridging medical vision and language with pixel-level editing tasks.

#### 🧫 Computational Pathology

- **[SlideChat: A Large Vision-Language Assistant for Whole-Slide Pathology Image Understanding](https://arxiv.org/abs/2410.11761)** — Gigapixel-level conversational assistant for interactive whole-slide image analysis and pathology Q&A.
- **[CPath-Omni: A Unified Multimodal Foundation Model for Patch and Slide-Level Vision-Language Modeling in Computational Pathology](https://arxiv.org/abs/2412.12077)** — Foundation model unifying patch- and slide-level pathology vision-language tasks in a single architecture.
- **[TopoCellGen: Generating Histopathology Cell Topology using a Diffusion Model](https://arxiv.org/abs/2412.06011)** — Topology-aware diffusion model for realistic histopathology cell layout generation.
- **[Fast and Accurate Gigapixel Pathological Image Classification](https://arxiv.org/abs/2502.21130)** — Efficient MIL-based method for whole-slide image classification at gigapixel scale.

---

### CVPR 2024

#### 🔬 Medical Imaging & Segmentation

- **[One-Prompt to Segment All Medical Images](https://arxiv.org/abs/2305.10300)** — Universal segmentation paradigm trained on 64 datasets; segments unseen modalities with a single prompted example. *Wu & Xu*
- **[EMCAD: Efficient Multi-scale Convolutional Attention Decoding for Medical Image Segmentation](https://arxiv.org/abs/2405.06880)** — Achieves state-of-the-art on 12 segmentation datasets with 79.4% fewer parameters via multi-scale convolutional attention decoding. *Rahman et al.*
- **[Versatile Medical Image Segmentation Learned from Multi-Source Datasets via Model Self-Improved](https://arxiv.org/abs/2311.10696)** — Cross-dataset training with self-improvement for versatile organ and lesion segmentation.
- **[Tyche: Stochastic in Context Learning for Universal Medical Image Segmentation](https://arxiv.org/abs/2401.13650)** — Stochastic context learning for uncertainty-aware universal medical image segmentation. *Butoi et al.*
- **[S2VNet: Universal Multi-Class Medical Image Segmentation via Multiple Slice-Aware Features](https://arxiv.org/abs/2403.16646)** — Slice-to-volume network for unified multi-class segmentation across organs and modalities.
- **[ZePT: Zero-Shot Pan-Tumor Segmentation via Query-Disentangling and Self-Prompting](https://arxiv.org/abs/2312.04964)** — Zero-shot tumor segmentation across cancer types through query disentangling and self-prompting.
- **[Training Like a Medical Resident: Universal Medical Image Segmentation via Context-Prior Learning](https://arxiv.org/abs/2306.02416)** — Curriculum-inspired pre-training using clinical context priors for universal segmentation.
- **[Modality-agnostic Domain Generalizable Medical Image Segmentation by Multi-Frequency in Multi-Scale Transformer](https://arxiv.org/abs/2405.06284)** — Frequency-domain augmentation for domain-generalizable segmentation across modalities.
- **[MAPSeg: Unified Unsupervised Domain Adaptation for Heterogeneous Medical Image Segmentation](https://arxiv.org/abs/2303.09373)** — Domain adaptation for heterogeneous 3D medical image segmentation without target-domain labels.
- **[PrPSeg: Universal Proposition Learning for Panoramic Renal Pathology Segmentation](https://arxiv.org/abs/2402.19286)** — Proposition-based universal framework for panoramic renal pathology segmentation.
- **[Adaptive Bidirectional Displacement for Semi-Supervised Medical Image Segmentation](https://arxiv.org/abs/2405.00378)** — Bidirectional pseudo-label consistency for semi-supervised 3D organ segmentation.
- **[Diversified and Personalized Multi-rater Medical Image Segmentation](https://arxiv.org/abs/2212.00601)** — Models inter-annotator disagreement to produce personalized, diversified segmentation outputs.
- **[Each Test Image Deserves A Specific Prompt: Continual Test-Time Adaptation for 2D Medical Image Segmentation](https://arxiv.org/abs/2311.18363)** — Instance-specific prompt generation for test-time adaptation without source data access.
- **[Constructing and Exploring Intermediate Domains in Mixed Domain Semi-supervised Medical Image Segmentation](https://arxiv.org/abs/2404.08951)** — Intermediate domain construction to bridge labeled-unlabeled gaps in semi-supervised segmentation.

#### 🤖 Foundation Models & Pre-training

- **[VoCo: A Simple-yet-Effective Volume Contrastive Learning Framework for 3D Medical Image Analysis](https://arxiv.org/abs/2402.17300)** — Volume-level contrastive pre-training enabling strong generalization across CT organ segmentation tasks.
- **[MLIP: Enhancing Medical Visual Representation with Multi-Level Multi-Modal Pre-training](https://arxiv.org/abs/2402.02045)** — Hierarchical vision-language pre-training for improved medical image representation.
- **[Continual Self-supervised Learning: Towards Universal Multi-modal Medical Data Representation Learning](https://arxiv.org/abs/2311.17597)** ⭐ *Highlight* — Continual SSL framework for multi-modal medical pre-training without catastrophic forgetting.
- **[Low-Rank Knowledge Decomposition for Medical Foundation Models](https://arxiv.org/abs/2404.17184)** — Low-rank adapter decomposition for efficient knowledge transfer from foundation models to medical tasks.
- **[Unleashing the Potential of SAM for Medical Adaptation without Fine-tuning](https://arxiv.org/abs/2403.18271)** — Training-free adaptation of the Segment Anything Model to medical imaging via prompt engineering.
- **[Bootstrapping Chest CT Image Understanding by Distilling Knowledge from X-ray Expert Models](https://arxiv.org/abs/2404.04936)** — Cross-modality knowledge distillation from 2D X-ray models to 3D CT image understanding.

#### 🤖 Vision-Language & Radiology

- **[PairAug: What Can Augmented Image-Text Pairs Do for Radiology?](https://arxiv.org/abs/2404.04960)** — Synthesized image-text pair augmentation for radiology vision-language pre-training.
- **[OmniMedVQA: A New Large-Scale Comprehensive Evaluation Benchmark for Medical LVLM](https://arxiv.org/abs/2402.09181)** — Comprehensive VQA benchmark spanning 12 medical imaging modalities for evaluating medical LVLMs.
- **[CARZero: Cross-Attention Alignment for Radiology Zero-Shot Classification](https://arxiv.org/abs/2402.17417)** — Cross-attention mechanism for zero-shot radiology classification using report-image alignment.
- **[FairCLIP: Harnessing Fairness in Vision-Language Learning for Medical Image Analysis](https://arxiv.org/abs/2403.19949)** — Fairness-aware contrastive learning to mitigate demographic bias in medical image analysis.
- **[Decomposing Disease Descriptions for Enhanced Pathology Detection: A Multi-Aspect Vision-Language Pre-Training Framework](https://arxiv.org/abs/2403.07636)** — Aspect-decomposed VL pre-training for fine-grained pathology detection in radiology.

#### 🧫 Computational Pathology

- **[Feature Re-Embedding: Towards Foundation Model-Level Performance in Computational Pathology](https://arxiv.org/abs/2402.17228)** — Re-embedding strategy that lifts conventional pathology features to foundation-model-level performance.
- **[Generalizable Whole Slide Image Classification with Fine-Grained Visual-Semantic Interaction](https://arxiv.org/abs/2402.19326)** — Fine-grained vision-language interaction for generalizable whole-slide image classification.
- **[SI-MIL: Taming Deep MIL for Self-Interpretability in Gigapixel Histopathology](https://arxiv.org/abs/2312.15010)** — Self-interpretable MIL framework that identifies diagnostically predictive regions in WSIs.
- **[Transcriptomics-guided Slide Representation Learning in Computational Pathology](https://arxiv.org/abs/2405.11618)** — Gene expression data as supervision signal for learning richer pathology slide representations.
- **[ChAda-ViT: Channel Adaptive Attention for Joint Representation Learning of Heterogeneous Microscopy Images](https://arxiv.org/abs/2311.15264)** — Channel-adaptive ViT for joint representation learning across multi-channel microscopy images.

#### 🔬 Image Reconstruction & Registration

- **[Correlation-aware Coarse-to-fine MLPs for Deformable Medical Image Registration](https://arxiv.org/abs/2406.00123)** ⭐ *Oral / Best Paper Candidate* — Lightweight MLP-based deformable registration using coarse-to-fine correlation features.
- **[Modality-Agnostic Structural Image Representation Learning for Deformable Multi-Modality Medical Image Registration](https://arxiv.org/abs/2402.18933)** — Unified structural representation for cross-modality deformable registration.
- **[QN-Mixer: A Quasi-Newton MLP-Mixer Model for Sparse-View CT Reconstruction](https://arxiv.org/abs/2402.17951)** — Quasi-Newton optimization embedded in an MLP-Mixer for sparse-view CT reconstruction.
- **[Structure-Aware Sparse-View X-ray 3D Reconstruction](https://arxiv.org/abs/2311.10959)** — Structure-aware priors for high-quality 3D X-ray reconstruction from sparse views.
- **[Fully Convolutional Slice-to-Volume Reconstruction for Single-Stack MRI](https://arxiv.org/abs/2312.03102)** — End-to-end convolutional approach to MRI super-resolution slice-to-volume reconstruction.
- **[CycleINR: Cycle Implicit Neural Representation for Arbitrary-Scale Volumetric Super-Resolution of 3D Medical Images](https://arxiv.org/abs/2404.04878)** — Cycle-consistent INR enabling arbitrary-scale super-resolution for 3D medical volumes.

#### 🔬 Image Synthesis & Detection

- **[Towards Generalizable Tumor Synthesis](https://arxiv.org/abs/2402.19470)** — Generalizable framework for synthesizing realistic tumors of diverse types and sizes for data augmentation.
- **[MedM2G: Unifying Medical Multi-Modal Generation via Cross-Guided Diffusion with Visual Invariant](https://arxiv.org/abs/2403.04290)** — Unified multi-modal medical image generation via cross-guided diffusion.
- **[FocusMAE: Gallbladder Cancer Detection from Ultrasound Videos with Focused Masked Autoencoders](https://arxiv.org/abs/2403.08848)** — Masked autoencoding focused on lesion regions for cancer detection in ultrasound video.

---

## NeurIPS

### NeurIPS 2024

#### 🤖 Medical Vision-Language

- **[CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://arxiv.org/abs/2406.06007)** — Evaluates trustworthiness of medical VLMs across truthfulness, safety, fairness, robustness, and privacy dimensions.

---

### NeurIPS 2023

#### 🔬 Medical Imaging

- **[Aligning Synthetic Medical Images with Clinical Knowledge using Human Feedback](https://papers.nips.cc/paper_files/paper/2023/hash/2b1d1e5affe5fdb70372cd90dd8afd49-Abstract-Conference.html)** — RLHF-based alignment of generative medical image models to match clinical expert knowledge. *Sun et al.*
- **[Quilt-1M: One Million Image-Text Pairs for Histopathology](https://arxiv.org/abs/2306.11207)** — Large-scale histopathology image-text dataset harvested from YouTube educational videos, enabling VL pre-training.

---

## ICLR

### ICLR 2025

#### 🔬 Medical Imaging & Segmentation

- **[LeFusion: Controllable Pathology Synthesis via Lesion-Focused Diffusion Models](https://arxiv.org/abs/2403.14066)** ⭐ *Spotlight* — Lesion-focused diffusion model that generates lesion-containing image-segmentation pairs from lesion-free scans; validated on cardiac MRI and lung CT. *[Code](https://github.com/HINTLab/LeFusion)*
- **[Large-scale and Fine-grained Vision-language Pre-training for Enhanced CT Image Understanding](https://arxiv.org/abs/2501.14548)** — Fine-grained anatomy-level VL pre-training on 69,086 patients; achieves 81.3% average AUC across 54 CT disease diagnosis tasks. *[Code](https://github.com/alibaba-damo-academy/fvlm)*
- **[Unleashing the Potential of Vision-Language Pre-Training for 3D Zero-Shot Lesion Segmentation via Mask-Attribute Alignment](https://openreview.net/forum?id=QG31By6S6w)** — Cross-modal knowledge injection to align visual lesion features with textual disease descriptions for zero-shot 3D segmentation. *Jiang et al.*
- **[Time-to-Event Pretraining for 3D Medical Imaging](https://arxiv.org/abs/2411.09361)** — Pre-trains 3D CT image encoders using time-to-event supervision from paired longitudinal EHR data; improves outcome prediction by 23.7% AUROC.

#### 🤖 Medical Vision-Language & Foundation Models

- **[MMed-RAG: Versatile Multimodal RAG System for Medical Vision Language Models](https://arxiv.org/abs/2410.13085)** — Domain-aware retrieval-augmented generation system that improves factual accuracy of medical VLMs by 43.8% across five datasets.
- **[MedTrinity-25M: A Large-Scale Multimodal Dataset with Multigranular Annotations for Medicine](https://arxiv.org/abs/2408.02900)** — 25M medical image triplets with multigranular annotations; LLaVA-Tri achieves 81.6% on VQA-RAD and 87.8% on SLAKE.
- **[MediConfusion: Can you trust your AI radiologist? Probing the reliability of multimodal medical foundation models](https://arxiv.org/abs/2409.15477)** — Benchmark revealing that state-of-the-art medical MLLMs perform below random guessing on clinically confusing image pairs.

#### 📋 Clinical NLP & EHR

- **[Reasoning-Enhanced Healthcare Predictions with Knowledge Graph Community Retrieval](https://arxiv.org/abs/2410.04585)** — KARE integrates multi-source medical KG community retrieval with LLM reasoning; outperforms leading models by up to 15% on MIMIC mortality/readmission prediction. *[Code](https://github.com/pat-jj/KARE)*
- **[Efficiently Democratizing Medical LLMs for 50 Languages via a Mixture of Language Family Experts](https://arxiv.org/abs/2410.10626)** — MoE routing with language-family-specific experts enables high-quality multilingual medical LLMs under data scarcity. *[Code](https://github.com/FreedomIntelligence/ApolloMoE)*

---

### ICLR 2024

#### 🔬 Medical Imaging & Radiology

- **[LLM-CXR: Instruction-Finetuned LLM for CXR Image Understanding and Generation](https://arxiv.org/abs/2305.11490)** — Unified LLM capable of chest X-ray image understanding, report generation, and image synthesis from text.

#### 📋 Clinical NLP & EHR

- **[MOTOR: A Time-to-Event Foundation Model For Structured Medical Records](https://arxiv.org/abs/2301.03150)** ⭐ *Spotlight* — Self-supervised TTE foundation model pre-trained on 55M EHR patient records; improves 19 clinical prediction tasks by 4.6% over SOTA with 95% label efficiency.
- **[Diagnosing Transformers: Illuminating Feature Spaces for Clinical Decision-Making](https://openreview.net/forum?id=k581sTMyPt)** — SUFO framework for interpreting fine-tuned transformer feature spaces in high-stakes clinical settings. *Hsu et al.*
- **[Multimodal Patient Representation Learning with Missing Modalities and Labels](https://openreview.net/forum?id=Je5SHCKpPa)** — Robust multimodal patient representation learning under realistic conditions of missing modalities and labels.

#### 🧠 Neuroimaging

- **[BrainLM: A Foundation Model for Brain Activity Recordings](https://proceedings.iclr.cc/paper_files/paper/2024/hash/029ce70401321de3808b3ac39e1ab167-Abstract-Conference.html)** — Transformer foundation model pre-trained on 6,700 hours of fMRI data; predicts clinical variables (age, anxiety, PTSD) and generalizes to unseen cohorts. *Caro et al.*

---

## ICCV / ECCV

### ECCV 2024

#### 🔬 Medical Imaging & Segmentation

- **[AnatoMask: Enhancing Medical Image Segmentation with Reconstruction-guided Self-masking](https://eccv.ecva.net/virtual/2024/poster/1161)** — Anatomy-aware masked image modeling for self-supervised 3D medical image segmentation.
- **[NePhi: Neural Deformation Fields for Approximately Diffeomorphic Medical Image Registration](https://arxiv.org/abs/2309.07322)** — Memory-efficient neural deformation fields for large-scale 3D medical image registration.

### ICCV 2023

#### 🤖 Medical Vision-Language

- **[Towards Unifying Medical Vision-and-Language Pre-training via Soft Prompts](https://arxiv.org/abs/2302.08958)** — Soft-prompt-based unified pre-training framework across diverse medical vision-language tasks.

---

## ACL / EMNLP

### EMNLP 2024

#### 📋 Clinical NLP

- **[RULE: Reliable Multimodal RAG for Factuality in Medical Vision Language Models](https://arxiv.org/abs/2407.05131)** — Retrieval-augmented framework that enforces factual grounding in medical VLM responses via controllable context selection.

### EMNLP 2023

#### 📋 Clinical NLP

- **[PhenotypeCLIP: Phenotype-based Contrastive Learning for Medical Imaging Report Generation](https://aclanthology.org/2023.emnlp-main.125/)** — Phenotype-aware contrastive learning for factually accurate and clinically consistent radiology report generation.

---

## AAAI

### AAAI 2024

#### 📋 Clinical NLP & EHR

- **[MedAlign: A Clinician-Generated Dataset for Instruction Following with Electronic Medical Records](https://arxiv.org/abs/2308.14089)** — Expert-annotated dataset benchmarking LLM instruction-following in EHR contexts across diverse clinical tasks.

---

## KDD

### KDD 2024

#### 📋 Clinical & Healthcare AI

- **[Clinical Trial Outcome Prediction with Drug-Disease Interaction and Heterogeneous GNN](https://dl.acm.org/doi/10.1145/3637528)** — Heterogeneous GNN modeling drug-disease interactions for clinical trial success prediction.

---

## Contributing

Contributions are very welcome!

- **Add a paper**: Open a PR with the paper entry in the appropriate conference section, using the format:  
  `**[Title](URL)** — One-sentence description. *Authors*`
- **Fix a broken link**: Open an issue or PR.
- **Suggest a new category**: Open an issue to discuss.

**Scope**: Papers published at CS/AI conference proceedings (CVPR, NeurIPS, ICLR, ICCV, ECCV, ACL, EMNLP, NAACL, AAAI, KDD, ICML, etc.) in the years 2023–2025 on topics of medical imaging, clinical NLP, surgical AI, or health AI. Pure biology papers (drug discovery, protein folding, genomics) are out of scope.

---

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related rights to this work.
