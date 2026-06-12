# Awesome Medical AI Papers [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of medical AI, healthcare AI, and medical imaging papers published at top CS/AI conferences: **CVPR, NeurIPS, ICLR, ICCV, ECCV, MICCAI, ACL, EMNLP, AAAI, KDD**, and more.

Covers **2023–2025**. Contributions welcome — see [Contributing](#contributing).

---

## Legend

| Icon | Topic |
|------|-------|
| 🔬 | Medical Imaging & Segmentation |
| 🧫 | Computational Pathology |
| 🤖 | Foundation Models & Vision-Language |
| 🧬 | Drug Discovery & Molecular Design |
| 🔭 | Protein Modeling & Structural Biology |
| 🧪 | Genomics & Single-Cell |
| 📋 | Clinical NLP & EHR |
| 🔪 | Surgical & Robotic AI |

---

## Contents

- [CVPR](#cvpr)
- [NeurIPS](#neurips)
- [ICLR](#iclr)
- [ICCV / ECCV](#iccv--eccv)
- [MICCAI](#miccai)
- [ACL / EMNLP](#acl--emnlp)
- [AAAI](#aaai)
- [KDD](#kdd)
- [Contributing](#contributing)

---

## CVPR

### CVPR 2025

#### 🔬 Medical Imaging & Segmentation

- **[Interactive Medical Image Segmentation: A Benchmark Dataset and Baseline](https://arxiv.org/abs/2411.12814)** — Introduces IMIS-Bench, a comprehensive benchmark for interactive segmentation across diverse modalities and organs.
- **[LesionLocator: Zero-Shot Universal Tumor Segmentation and Tracking in 3D Whole-Body Imaging](https://arxiv.org/pdf/2502.20985)** — Zero-shot framework for tumor segmentation and longitudinal tracking across unseen tumor types.
- **[Latent Drifting in Diffusion Models for Counterfactual Medical Image Synthesis](https://arxiv.org/abs/2412.20651)** — Generates counterfactual medical images by drifting in the latent space of diffusion models, enabling controlled pathology simulation.
- **[DyCON: Dynamic Uncertainty-aware Consistency and Contrastive Learning for Semi-supervised Medical Image Segmentation](https://arxiv.org/abs/2504.04566)** — Leverages uncertainty-aware consistency and contrastive objectives for semi-supervised volumetric segmentation.

#### 🤖 Foundation Models & Vision-Language

- **[CheXWorld: Exploring Image World Modeling for Radiograph Representation Learning](https://arxiv.org/abs/2504.13820)** — Applies world modeling principles to chest X-ray representation learning, improving downstream diagnostic tasks.
- **[EchoWorld: Learning Motion-Aware World Models for Echocardiography Video Understanding](https://arxiv.org/abs/2504.13065)** — Motion-aware world model pre-trained on echocardiography videos for cardiac assessment.
- **[VILA-M3: Enhancing Vision-Language Models with Medical Expert Knowledge](https://arxiv.org/abs/2411.12915)** — Integrates structured medical expert knowledge into VLMs for clinical image understanding.
- **[BiomedCoOp: Learning to Prompt for Biomedical Vision-Language Models](https://arxiv.org/abs/2411.15232)** — Context optimization approach for prompt learning in biomedical vision-language models.
- **[BIOMEDICA: An Open Biomedical Image-Caption Archive and Vision-Language Models Derived from Scientific Literature](https://arxiv.org/abs/2501.07171)** — Large-scale open archive of biomedical image-caption pairs mined from scientific literature.
- **[MedUnifier: Unifying Vision-and-Language Pre-training for Medical Vision-Language Models with Pixel-level Image Editing](https://arxiv.org/pdf/2503.01019)** — Unified pre-training framework bridging medical vision and language with pixel-level editing tasks.
- **[Multi-modal Medical Diagnosis via Large-small Model Collaboration](https://openaccess.thecvf.com/content/CVPR2025/papers/Chen_Multi-modal_Medical_Diagnosis_via_Large-small_Model_Collaboration_CVPR_2025_paper.pdf)** — Collaborative inference between large and small models for multi-modal medical diagnosis.

#### 🧫 Computational Pathology

- **[SlideChat: A Large Vision-Language Assistant for Whole-Slide Pathology Image Understanding](https://arxiv.org/abs/2410.11761)** — Gigapixel-level conversational assistant for interactive whole-slide image analysis.
- **[CPath-Omni: A Unified Multimodal Foundation Model for Patch and Slide-Level Vision-Language Modeling in Computational Pathology](https://arxiv.org/abs/2412.12077)** — Foundation model unifying patch- and slide-level pathology VL tasks in a single architecture.
- **[TopoCellGen: Generating Histopathology Cell Topology using a Diffusion Model](https://arxiv.org/abs/2412.06011)** — Topology-aware diffusion model for realistic histopathology cell layout generation.
- **[Fast and Accurate Gigapixel Pathological Image Classification](https://arxiv.org/pdf/2502.21130)** — Efficient MIL-based method for whole-slide image classification at gigapixel scale.

---

### CVPR 2024

#### 🔬 Medical Imaging & Segmentation

- **[One-Prompt to Segment All Medical Images](https://arxiv.org/abs/2305.10300)** — Universal segmentation paradigm trained on 64 datasets; segments unseen modalities with a single prompted example. *Wu & Xu*
- **[EMCAD: Efficient Multi-scale Convolutional Attention Decoding for Medical Image Segmentation](https://arxiv.org/abs/2405.06880)** — SOTA on 12 segmentation datasets with 79.4% fewer parameters via multi-scale convolutional attention decoding. *Rahman et al.*
- **[Versatile Medical Image Segmentation Learned from Multi-Source Datasets via Model Self-Improved](https://arxiv.org/abs/2311.10696)** — Cross-dataset learning for versatile segmentation with self-improvement strategy.
- **[Tyche: Stochastic in Context Learning for Universal Medical Image Segmentation](https://arxiv.org/abs/2401.13650)** — Stochastic context learning for uncertainty-aware universal medical segmentation.
- **[S2VNet: Universal Multi-Class Medical Image Segmentation via Multiple Slice-Aware Features](https://arxiv.org/abs/2403.16646)** — Slice-to-volume network for unified multi-class segmentation across organs.
- **[ZePT: Zero-Shot Pan-Tumor Segmentation via Query-Disentangling and Self-Prompting](https://arxiv.org/abs/2312.04964)** — Zero-shot tumor segmentation across cancer types through query disentangling.
- **[Training Like a Medical Resident: Universal Medical Image Segmentation via Context-Prior Learning](https://arxiv.org/abs/2306.02416)** — Curriculum-inspired pre-training using clinical context priors for universal segmentation.
- **[Modality-agnostic Domain Generalizable Medical Image Segmentation by Multi-Frequency in Multi-Scale Transformer](https://arxiv.org/abs/2405.06284)** — Frequency-domain augmentation for domain-generalizable segmentation across modalities.
- **[MAPSeg: Unified Unsupervised Domain Adaptation for Heterogeneous Medical Image Segmentation Based on 3D Masked Autoencoding and Pseudo-Labeling](https://arxiv.org/abs/2303.09373)** — Domain adaptation for heterogeneous 3D medical image segmentation without target labels.
- **[PrPSeg: Universal Proposition Learning for Panoramic Renal Pathology Segmentation](https://arxiv.org/abs/2402.19286)** — Proposition-based universal framework for panoramic renal pathology segmentation.
- **[Adaptive Bidirectional Displacement for Semi-Supervised Medical Image Segmentation](https://arxiv.org/abs/2405.00378)** — Bidirectional pseudo-label consistency for semi-supervised 3D organ segmentation.
- **[Diversified and Personalized Multi-rater Medical Image Segmentation](https://arxiv.org/abs/2212.00601)** — Models inter-annotator disagreement to produce personalized, diversified segmentation outputs.
- **[Each Test Image Deserves A Specific Prompt: Continual Test-Time Adaptation for 2D Medical Image Segmentation](https://arxiv.org/abs/2311.18363)** — Instance-specific prompt generation for test-time adaptation without source data.
- **[Constructing and Exploring Intermediate Domains in Mixed Domain Semi-supervised Medical Image Segmentation](https://arxiv.org/abs/2404.08951)** — Intermediate domain construction to bridge labeled-unlabeled domain gaps in semi-supervision.

#### 🤖 Foundation Models

- **[VoCo: A Simple-yet-Effective Volume Contrastive Learning Framework for 3D Medical Image Analysis](https://arxiv.org/abs/2402.17300)** — Volume-level contrastive pre-training enabling strong generalization across CT segmentation tasks.
- **[MLIP: Enhancing Medical Visual Representation with Multi-Level Multi-Modal Pre-training](https://arxiv.org/abs/2402.02045)** — Hierarchical vision-language pre-training for improved medical image representation.
- **[Continual Self-supervised Learning: Towards Universal Multi-modal Medical Data Representation Learning](https://arxiv.org/abs/2311.17597)** ⭐ *Highlight* — Continual SSL framework for universal multi-modal medical pre-training without catastrophic forgetting.
- **[Low-Rank Knowledge Decomposition for Medical Foundation Models](https://arxiv.org/abs/2404.17184)** — Decomposes foundation model knowledge via low-rank adapters for efficient medical fine-tuning.
- **[Unleashing the Potential of SAM for Medical Adaptation without Fine-tuning](https://arxiv.org/abs/2403.18271)** — Training-free adaptation of SAM to medical imaging via prompt engineering.
- **[Bootstrapping Chest CT Image Understanding by Distilling Knowledge from X-ray Expert Models](https://arxiv.org/abs/2404.04936)** — Cross-modality knowledge distillation from 2D X-ray models to 3D CT understanding.

#### 🤖 Vision-Language & Radiology

- **[PairAug: What Can Augmented Image-Text Pairs Do for Radiology?](https://arxiv.org/abs/2404.04960)** — Data augmentation via synthesized image-text pairs for radiology vision-language tasks.
- **[OmniMedVQA: A New Large-Scale Comprehensive Evaluation Benchmark for Medical LVLM](https://arxiv.org/abs/2402.09181)** — Comprehensive VQA benchmark spanning 12 medical imaging modalities.
- **[CARZero: Cross-Attention Alignment for Radiology Zero-Shot Classification](https://arxiv.org/abs/2402.17417)** — Cross-attention mechanism for zero-shot radiology classification using report-image alignment.
- **[FairCLIP: Harnessing Fairness in Vision-Language Learning for Medical Image Analysis](https://arxiv.org/abs/2403.19949)** — Fairness-aware contrastive learning for equitable medical image analysis.
- **[Decomposing Disease Descriptions for Enhanced Pathology Detection: A Multi-Aspect Vision-Language Pre-Training Framework](https://arxiv.org/abs/2403.07636)** — Aspect-decomposed VL pre-training for fine-grained pathology detection.

#### 🧫 Computational Pathology

- **[Feature Re-Embedding: Towards Foundation Model-Level Performance in Computational Pathology](https://arxiv.org/abs/2402.17228)** — Re-embedding strategy that lifts conventional pathology features to foundation-model-level performance.
- **[Generalizable Whole Slide Image Classification with Fine-Grained Visual-Semantic Interaction](https://arxiv.org/abs/2402.19326)** — Fine-grained vision-language interaction for generalizable WSI classification.
- **[SI-MIL: Taming Deep MIL for Self-Interpretability in Gigapixel Histopathology](https://arxiv.org/abs/2312.15010)** — Self-interpretable MIL framework that identifies predictive regions in whole-slide images.
- **[Transcriptomics-guided Slide Representation Learning in Computational Pathology](https://arxiv.org/abs/2405.11618)** — Uses gene expression data as supervision signal for pathology slide representation learning.
- **[ChAda-ViT: Channel Adaptive Attention for Joint Representation Learning of Heterogeneous Microscopy Images](https://arxiv.org/abs/2311.15264)** — Channel-adaptive ViT for joint representation of multi-channel microscopy images.

#### 🔬 Image Reconstruction & Registration

- **[Correlation-aware Coarse-to-fine MLPs for Deformable Medical Image Registration](https://arxiv.org/abs/2406.00123)** ⭐ *Oral / Best Paper Candidate* — Lightweight MLP-based deformable registration using coarse-to-fine correlation features.
- **[Modality-Agnostic Structural Image Representation Learning for Deformable Multi-Modality Medical Image Registration](https://arxiv.org/abs/2402.18933)** — Unified structural representation for cross-modality deformable registration.
- **[QN-Mixer: A Quasi-Newton MLP-Mixer Model for Sparse-View CT Reconstruction](https://arxiv.org/abs/2402.17951)** — Quasi-Newton optimization embedded in an MLP-Mixer for sparse-view CT reconstruction.
- **[Structure-Aware Sparse-View X-ray 3D Reconstruction](https://arxiv.org/abs/2311.10959)** — Structure-aware priors for high-quality 3D X-ray reconstruction from sparse views.
- **[Fully Convolutional Slice-to-Volume Reconstruction for Single-Stack MRI](https://arxiv.org/abs/2312.03102)** — End-to-end convolutional approach to MRI super-resolution slice-to-volume reconstruction.
- **[CycleINR: Cycle Implicit Neural Representation for Arbitrary-Scale Volumetric Super-Resolution of 3D Medical Images](https://arxiv.org/abs/2404.04878)** — Cycle-consistent INR for arbitrary-scale 3D medical image super-resolution.

#### 🔬 Image Synthesis & Detection

- **[Towards Generalizable Tumor Synthesis](https://arxiv.org/abs/2402.19470)** — Generalizable framework for synthesizing realistic tumors across organ types and sizes.
- **[MedM2G: Unifying Medical Multi-Modal Generation via Cross-Guided Diffusion with Visual Invariant](https://arxiv.org/abs/2403.04290)** — Unified multi-modal medical image generation via cross-guided diffusion.
- **[FocusMAE: Gallbladder Cancer Detection from Ultrasound Videos with Focused Masked Autoencoders](https://arxiv.org/abs/2403.08848)** — Masked autoencoding focused on lesion regions for cancer detection in ultrasound videos.

---

## NeurIPS

### NeurIPS 2024

#### 🤖 Medical Vision-Language

- **[CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://arxiv.org/abs/2406.06007)** — Evaluates trustworthiness of medical VLMs across truthfulness, safety, fairness, and robustness.

#### 🧬 Drug Discovery & Molecular Design

- **[RGFN: Synthesizable Molecular Generation Using GFlowNets](https://arxiv.org/abs/2406.08506)** — GFlowNet operating in reaction space to generate synthesizable drug candidates at ~100× lower cost. *Koziarski et al.*
- **[TurboHopp: Accelerated Molecule Scaffold Hopping with Consistency Models](https://neurips.cc/virtual/2024/poster/93849)** — 30× faster pocket-conditioned scaffold hopping via consistency model distillation.
- **[Aligning Target-Aware Molecule Diffusion Models with Exact Energy Optimization](https://proceedings.neurips.cc/paper_files/paper/2024)** — Energy-based alignment of target-aware diffusion models for high-affinity drug molecule generation.
- **[Full-Atom Peptide Design with Geometric Latent Diffusion](https://proceedings.neurips.cc/paper_files/paper/2024)** — Geometric latent diffusion model for all-atom peptide sequence and structure co-design.
- **[Reprogramming Pretrained Target-Specific Diffusion Models for Dual-Target Drug Design](https://proceedings.neurips.cc/paper_files/paper/2024)** — Reprograms single-target diffusion models to generate dual-target inhibitors without retraining.
- **[FlexSBDD: Structure-Based Drug Design with Flexible Protein Modeling](https://proceedings.neurips.cc/paper_files/paper/2024)** — Jointly models protein flexibility and ligand conformation for structure-based drug design.
- **[DeltaDock: A Unified Framework for Accurate, Efficient, and Physically Reliable Molecular Docking](https://proceedings.neurips.cc/paper_files/paper/2024)** — Unified docking framework achieving accuracy, efficiency, and physical validity simultaneously.
- **[Genetic-guided GFlowNets for Sample Efficient Molecular Optimization](https://proceedings.neurips.cc/paper_files/paper/2024)** — Genetic algorithm guidance for GFlowNets to improve sample efficiency in molecular optimization.

#### 🔭 Protein Modeling

- **[ET-Flow: Equivariant Flow-Matching for Molecular Conformer Generation](https://arxiv.org/abs/2410.22388)** — SE(3)-equivariant flow matching with harmonic priors for fast and accurate conformer generation.
- **[Sequence-Augmented SE(3)-Flow Matching for Conditional Protein Backbone Generation](https://proceedings.neurips.cc/paper_files/paper/2024)** — Sequence-conditioned flow matching for de novo protein backbone design.
- **[Generalized Protein Pocket Generation with Prior-Informed Flow Matching](https://proceedings.neurips.cc/paper_files/paper/2024)** — Pocket-shape-conditioned flow matching for generalized binding site generation.
- **[Generating Highly Designable Proteins with Geometric Algebra Flow Matching](https://proceedings.neurips.cc/paper_files/paper/2024)** — Geometric algebra framework for highly designable de novo protein generation.
- **[Training Compute-Optimal Protein Language Models](https://proceedings.neurips.cc/paper_files/paper/2024)** — Scaling laws and compute-optimal training recipes for protein language models.
- **[DePLM: Denoising Protein Language Models for Property Optimization](https://proceedings.neurips.cc/paper_files/paper/2024)** — Denoising objectives for protein LM fine-tuning toward target property optimization.
- **[MutaPLM: Protein Language Modeling for Mutation Explanation and Engineering](https://proceedings.neurips.cc/paper_files/paper/2024)** — PLM-based framework for explaining and engineering protein mutations.
- **[ProSST: Protein Language Modeling with Quantized Structure and Disentangled Attention](https://proceedings.neurips.cc/paper_files/paper/2024)** — Jointly models protein sequence and quantized structure with disentangled attention.

#### 🧪 Genomics & Single-Cell

- **[GENOT: Entropic (Gromov) Wasserstein Flow Matching with Applications to Single-Cell Genomics](https://arxiv.org/abs/2310.09254)** — Optimal-transport flow matching for single-cell perturbation response prediction.
- **[Semi-supervised Knowledge Transfer Across Multi-omic Single-cell Data](https://proceedings.neurips.cc/paper_files/paper/2024)** — Cross-omic knowledge transfer using semi-supervised learning for single-cell multi-omics integration.
- **[Absorb & Escape: Overcoming Single Model Limitations in Generating Heterogeneous Genomic Sequences](https://proceedings.neurips.cc/paper_files/paper/2024)** — Mixture-of-experts approach for diverse genomic sequence generation.

#### 🔭 Structural Biology

- **[CryoGEM: Physics-Informed Generative Cryo-Electron Microscopy](https://proceedings.neurips.cc/paper_files/paper/2024)** — Physics-informed generative model for cryo-EM particle image simulation and reconstruction.
- **[CryoSPIN: Improving Ab-Initio Cryo-EM Reconstruction with Semi-Amortized Pose Inference](https://proceedings.neurips.cc/paper_files/paper/2024)** — Semi-amortized pose inference for efficient ab-initio cryo-EM 3D reconstruction.

---

### NeurIPS 2023

#### 🔬 Medical Imaging

- **[Aligning Synthetic Medical Images with Clinical Knowledge using Human Feedback](https://papers.nips.cc/paper_files/paper/2023/hash/2b1d1e5affe5fdb70372cd90dd8afd49-Abstract-Conference.html)** — RLHF-based alignment of generative medical image models with clinical expert knowledge. *Sun et al.*
- **[Quilt-1M: One Million Image-Text Pairs for Histopathology](https://arxiv.org/abs/2306.11207)** — Large-scale histopathology image-text dataset harvested from YouTube educational videos.

---

## ICLR

### ICLR 2025

#### 🤖 Medical Vision-Language

- **[MMed-RAG: Versatile Multimodal RAG System for Medical Vision Language Models](https://arxiv.org/abs/2410.13085)** — Retrieval-augmented generation system that grounds medical VLM responses with relevant evidence.

### ICLR 2024

#### 🧬 Drug Discovery & Molecular

- **[Equivariant Scalar Fields for Molecular Docking with Fast Fourier Transforms](https://openreview.net/forum?id=ew35XA7cNy)** — Equivariant FFT-based molecular docking achieving fast and accurate pose prediction. *Jing et al.*
- **[Learning Over Molecular Conformer Ensembles: Datasets and Benchmarks](https://openreview.net/forum?id=VoMXE37OBD)** — Benchmark for learning over conformational ensembles of small molecules. *Zhu et al.*
- **[Deep Confident Steps to New Pockets: Strategies for Docking Generalization](https://openreview.net/forum?id=UfBIxpTK10)** — Confidence-based sampling strategies for generalizable molecular docking. *Corso et al.*
- **[MOFDiff: Coarse-grained Diffusion for Metal-Organic Framework Design](https://openreview.net/forum?id=0VBsoluxR2)** — Coarse-grained diffusion model for de novo design of porous metal-organic frameworks. *Fu et al.*
- **[Improving Protein Optimization with Smoothed Fitness Landscapes](https://openreview.net/forum?id=rxlF2Zv8x0)** — Landscape smoothing technique for more effective evolutionary protein optimization. *Kirjner et al.*
- **[Removing Biases from Molecular Representations via Information Maximization](https://openreview.net/forum?id=T4JMpN2lUV)** — Information-theoretic debiasing of molecular graph representations. *Wang et al.*

#### 📋 Clinical & Health

- **[LLM-CXR: Instruction-Finetuned LLM for CXR Image Understanding and Generation](https://openreview.net/forum?id=O9rSVEpAIn)** — Unified LLM capable of CXR image understanding, report generation, and image synthesis.
- **[Conformal Language Modeling](https://openreview.net/forum?id=pzUhfQ74c5)** — Rigorous uncertainty quantification for LLM outputs applicable to clinical decision settings. *Quach et al.*
- **[Learning Inflammatory Biomarkers from Nocturnal Breathing, BMI and Demographics](https://openreview.net/forum?id=ICLR2024LearningBiomarkers)** — Passive sensing approach to predict inflammatory biomarkers from breathing patterns. *He & Katabi*

---

## ICCV / ECCV

### ECCV 2024

#### 🔬 Medical Imaging & Segmentation

- **[AnatoMask: Enhancing Medical Image Segmentation with Reconstruction-guided Self-masking](https://eccv.ecva.net/virtual/2024/poster/1161)** — Masked image modeling with anatomy-aware masking strategy for 3D medical image segmentation.
- **[NePhi: Neural Deformation Fields for Approximately Diffeomorphic Medical Image Registration](https://arxiv.org/abs/2309.07322)** — Memory-efficient neural deformation fields for large-scale 3D medical image registration.

### ICCV 2023

#### 🤖 Medical Vision-Language

- **[Towards Unifying Medical Vision-and-Language Pre-training via Soft Prompts](https://arxiv.org/abs/2302.08958)** — Soft-prompt-based unified pre-training framework across diverse medical vision-language tasks.

---

## MICCAI

### MICCAI 2024

#### 🔬 Segmentation

- **[SegMamba: Long-Range Sequential Modeling Mamba for 3D Medical Image Segmentation](https://arxiv.org/abs/2401.13560)** — State-space model (Mamba) applied to 3D medical image segmentation for efficient long-range modeling.
- **[Medical Image Segmentation via Single-Source Domain Generalization with Random Amplitude Spectrum Synthesis](https://papers.miccai.org/miccai-2024/502-Paper4012.html)** — Frequency-domain augmentation for single-source domain generalization in segmentation.
- **[3D-SAutoMed: Automatic Segment Anything Model for 3D Medical Image Segmentation](https://doi.org/10.1007/978-3-031-72114-4)** — Extends SAM to automatic 3D medical image segmentation from a local-global perspective.

#### 🔬 Detection

- **[BGF-YOLO: Enhanced YOLOv8 with Multiscale Attentive Feature Fusion for Brain Tumor Detection](https://doi.org/10.1007/978-3-031-72111-3_4)** — Multi-scale attentive feature fusion module boosting YOLO-based brain tumor detection.

#### 📋 Brain & Neurology

- **[BrainSCK: Brain Structure and Cognition Alignment for Diagnosing Brain Disorders](https://doi.org/10.1007/978-3-031-72069-7_5)** — Structure-cognition cross-modal alignment for interpretable brain disorder diagnosis. *[Code](https://github.com/openmedlab/BrainSCK)*
- **[BrainWaveNet: Wavelet-Based Transformer for Autism Spectrum Disorder Diagnosis](https://doi.org/10.1007/978-3-031-72069-7_6)** — Wavelet transform integrated with transformers for ASD classification. *[Code](https://github.com/ku-milab/BrainWaveNet)*
- **[Affinity Learning Based Brain Function Representation for Disease Diagnosis](https://doi.org/10.1007/978-3-031-72069-7_2)** — Graph-based affinity learning on fMRI functional connectivity for disease classification.

---

## ACL / EMNLP

### EMNLP 2024

#### 📋 Clinical NLP & Medical VLM

- **[RULE: Reliable Multimodal RAG for Factuality in Medical Vision Language Models](https://arxiv.org/abs/2407.05131)** — Retrieval-augmented framework that enforces factuality in medical VLM responses.
- **[PrecLLM: A Privacy-Preserving Framework for Efficient Clinical Annotation Extraction from Unstructured EHRs using Small-Scale LLMs](https://arxiv.org/abs/2412.02868)** — Privacy-preserving local LLM pipeline for structured information extraction from clinical notes.

### EMNLP 2023

#### 📋 Clinical NLP

- **[PhenotypeCLIP: Phenotype-based Contrastive Learning for Medical Imaging Report Generation](https://aclanthology.org/2023.emnlp-main.125/)** — Phenotype-aware contrastive learning for factually accurate radiology report generation.

### ACL 2023

#### 📋 Clinical NLP

- **[Competence-based Multimodal Curriculum Learning for Medical Report Generation](https://arxiv.org/abs/2206.14579)** — Curriculum learning guided by clinical competence ordering for radiology report generation.

---

## AAAI

### AAAI 2025

#### 🔬 Medical Imaging

- **[Health-LLM: Personalized Retrieval-Augmented Disease Prediction System](https://arxiv.org/abs/2402.00746)** — RAG-enhanced LLM system integrating health reports and medical knowledge for personalized disease prediction.

### AAAI 2024

#### 📋 Clinical NLP & EHR

- **[MedAlign: A Clinician-Generated Dataset for Instruction Following with Electronic Medical Records](https://arxiv.org/abs/2308.14089)** — Expert-annotated dataset for evaluating LLM instruction-following in EHR contexts.

---

## KDD

### KDD 2024

#### 📋 Clinical & Healthcare AI

- **[Clinical Trial Outcome Prediction with Drug-Disease Interaction and Heterogeneous GNN](https://dl.acm.org/doi/10.1145/3637528)** — Heterogeneous GNN modeling drug-disease interactions for clinical trial outcome prediction.

---

## Contributing

Contributions are very welcome!

- **Add a paper**: Open a PR with the paper entry in the appropriate conference section, using the format:  
  `**[Title](URL)** — One-sentence description. *Authors*`
- **Fix a broken link**: Open an issue or PR.
- **Suggest a new category**: Open an issue to discuss.

**Scope**: Papers published at CS/AI conference proceedings (CVPR, NeurIPS, ICLR, ICCV, ECCV, MICCAI, ACL, EMNLP, NAACL, AAAI, KDD, ICML, etc.) in the years 2023–2025 on topics of medical imaging, clinical NLP, drug discovery, genomics, or surgical AI.

---

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related rights to this work.
