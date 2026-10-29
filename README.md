# Awesome Medical AI Papers [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of medical AI, healthcare AI, and medical imaging papers published at top CS/AI conferences: **CVPR, NeurIPS, ICLR, ICML, ICCV, ECCV, ACL, EMNLP, NAACL, AAAI, KDD**, and more.

Covers **2023–2025**. Organized by conference publication year, which may differ from the arXiv submission year. Contributions welcome — see [Contributing](#contributing).

---

## Legend

| Icon | Topic |
|------|-------|
| 🔬 | Medical Imaging & Segmentation |
| 🧫 | Computational Pathology |
| 🤖 | Foundation Models & Vision-Language |
| 📋 | Clinical NLP & EHR |
| 🧠 | Neuroimaging, EEG & Brain AI |
| 🫀 | Physiological Signals & Medical Time Series |
| 🏥 | Surgical AI |

---

## Contents

- [CVPR](#cvpr)
- [NeurIPS](#neurips)
- [ICML](#icml)
- [ICLR](#iclr)
- [ICCV / ECCV](#iccv--eccv)
- [ACL / EMNLP](#acl--emnlp)
- [NAACL](#naacl)
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
- **[MIMO: A Medical Vision Language Model with Visual Referring Multimodal Input and Pixel Grounding Multimodal Output](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_MIMO_A_Medical_Vision_Language_Model_with_Visual_Referring_Multimodal_CVPR_2025_paper.html)** — Accepts visual references alongside text instructions and grounds generated medical terminology in image regions.
- **[Alignment, Mining and Fusion: Representation Alignment with Hard Negative Mining and Selective Knowledge Fusion for Medical Visual Question Answering](https://openaccess.thecvf.com/content/CVPR2025/html/Zou_Alignment_Mining_and_Fusion_Representation_Alignment_with_Hard_Negative_Mining_CVPR_2025_paper.html)** — Combines multi-level image-text alignment, hard negative mining, and gated knowledge fusion for medical VQA.
- **[Multi-modal Vision Pre-training for Medical Image Analysis](https://openaccess.thecvf.com/content/CVPR2025/html/Rui_Multi-modal_Vision_Pre-training_for_Medical_Image_Analysis_CVPR_2025_paper.html)** — BrainMVP learns cross-modality MRI representations through reconstruction, contrastive learning, and modality template distillation.

#### 🔬 Patient Identification & Privacy

- **[Towards All-in-One Medical Image Re-Identification](https://openaccess.thecvf.com/content/CVPR2025/html/Tian_Towards_All-in-One_Medical_Image_Re-Identification_CVPR_2025_paper.html)** — Benchmarks patient re-identification across imaging modalities and introduces modality-adaptive representations for personalized diagnosis and privacy analysis.

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

#### 🏥 Surgical AI

- **[Intraoperative 2D/3D Image Registration via Differentiable X-ray Rendering](https://openaccess.thecvf.com/content/CVPR2024/html/Gopalakrishnan_Intraoperative_2D3D_Image_Registration_via_Differentiable_X-ray_Rendering_CVPR_2024_paper.html)** — DiffPose combines patient-specific simulation with differentiable rendering to align intraoperative X-rays with preoperative CT without landmark annotations.

---

### CVPR 2023

#### 🔬 Medical Imaging & Segmentation

- **[Bidirectional Copy-Paste for Semi-Supervised Medical Image Segmentation](https://arxiv.org/abs/2305.00673)** — Bidirectional copy-paste between labeled and unlabeled volumes in a Mean Teacher framework, achieving SOTA on LA and Pancreas-CT semi-supervised benchmarks. *Bai et al.*
- **[MCF: Mutual Correction Framework for Semi-Supervised Medical Image Segmentation](https://openaccess.thecvf.com/content/CVPR2023/html/Wang_MCF_Mutual_Correction_Framework_for_Semi-Supervised_Medical_Image_Segmentation_CVPR_2023_paper.html)** — Two-subnet mutual correction with contrastive difference review and dynamic competitive pseudo-label generation to reduce cognitive bias in semi-supervised segmentation.
- **[Ambiguous Medical Image Segmentation using Diffusion Models](https://arxiv.org/abs/2304.04745)** — Single diffusion model that produces multiple plausible segmentation variants by learning a distribution over annotator group insights, validated on CT, ultrasound, and MRI.
- **[Label-Free Liver Tumor Segmentation](https://arxiv.org/abs/2303.14869)** — Synthesizes realistic pseudo-tumors in healthy CT scans to train a segmentation model without any real tumor annotations, outperforming fully supervised baselines.

#### 🤖 Foundation Models & Vision-Language

- **[Learning to Exploit Temporal Structure for Biomedical Vision-Language Processing](https://arxiv.org/abs/2301.04558)** — BioViL-T: CNN-Transformer hybrid multi-image encoder jointly trained with a text model on longitudinal chest X-ray reports; SOTA on progression classification, phrase grounding, and report generation. *Bannur et al., Microsoft Research*
- **[Geometric Visual Similarity Learning in 3D Medical Image Self-supervised Pre-training](https://arxiv.org/abs/2303.00874)** — Geometric similarity as a self-supervised signal for pre-training 3D medical image encoders, improving transfer to organ segmentation tasks.
- **[Hierarchical Discriminative Learning Improves Visual Representations of Biomedical Microscopy](https://arxiv.org/abs/2303.01605)** — Hierarchical contrastive learning framework that aligns microscopy image representations at multiple granularities for richer visual pre-training.

#### 📋 Radiology Report Generation

- **[METransformer: Radiology Report Generation by Transformer with Multiple Learnable Expert Tokens](https://arxiv.org/abs/2304.02211)** — Multiple learnable expert tokens in both encoder and decoder attend to complementary image regions and are regularized by orthogonal loss for diverse, accurate report generation.
- **[KiUT: Knowledge-Injected U-Transformer for Radiology Report Generation](https://openaccess.thecvf.com/content/CVPR2023/papers/Huang_KiUT_Knowledge-Injected_U-Transformer_for_Radiology_Report_Generation_CVPR_2023_paper.pdf)** — U-connection transformer that distills visual, clinical, and contextual knowledge at multiple scales for accurate radiology report generation.
- **[Dynamic Graph Enhanced Contrastive Learning for Chest X-Ray Report Generation](https://arxiv.org/abs/2303.10323)** — Dynamic knowledge graph with contrastive learning (DCL) retrieves disease-specific nodes to guide chest X-ray report generation; SOTA on IU-Xray and MIMIC-CXR. *Li et al.*

#### 🧫 Computational Pathology

- **[Visual Language Pretrained Multiple Instance Zero-Shot Transfer for Histopathology Images](https://arxiv.org/abs/2306.07831)** — MI-Zero reformulates zero-shot transfer under MIL for gigapixel WSIs, achieving 70.2% average accuracy on three cancer subtyping tasks without task-specific labels. *Lu et al., Mahmood Lab*
- **[Interventional Bag Multi-Instance Learning On Whole-Slide Pathological Images](https://arxiv.org/abs/2303.06873)** — Causal intervention via do-calculus removes confounding in bag-level MIL for more robust WSI classification.
- **[Task-specific Fine-tuning via Variational Information Bottleneck for Weakly-supervised Pathology Whole Slide Image Classification](https://arxiv.org/abs/2303.08446)** — VIB-based fine-tuning compresses WSI representations to task-relevant bottlenecks, improving weakly supervised classification with fewer labeled slides.
- **[Topology-Guided Multi-Class Cell Context Generation for Digital Pathology](https://arxiv.org/abs/2304.02255)** — Topology-aware generation model creates realistic multi-class cell spatial layouts for data augmentation in computational pathology.
- **[DoNet: Deep De-overlapping Network for Cytology Instance Segmentation](https://arxiv.org/abs/2303.14373)** — Decompose-and-reconstruct strategy separates overlapping cell instances in cytology images for accurate instance segmentation.

---

## NeurIPS

### NeurIPS 2025

#### 🔬 Medical Imaging & Segmentation

- **[Pancakes: Consistent Multi-Protocol Image Segmentation Across Biomedical Domains](https://proceedings.neurips.cc/paper_files/paper/2025/hash/3cd5473f038dfb5357e3544cc1cb3b98-Abstract-Conference.html)** — Generates multiple plausible segmentation protocols for unseen biomedical domains while maintaining semantic consistency across images.
- **[PanTS: The Pancreatic Tumor Segmentation Dataset](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2dc24f4adc257251b2f3929c67ec1e3a-Abstract-Datasets_and_Benchmarks_Track.html)** — Multi-institutional CT dataset with expert-validated annotations of pancreatic tumors, pancreatic subregions, and surrounding anatomy. *Datasets and Benchmarks Track*
- **[The Boundaries of Fair AI in Medical Image Prognosis: A Causal Perspective](https://proceedings.neurips.cc/paper_files/paper/2025/hash/c1715562b2227580b6c6db2050d7f6d2-Abstract-Conference.html)** — FairTTE studies demographic disparities and their causal sources in imaging-based time-to-event prediction, including under distribution shifts.

#### 🤖 Foundation Models & Vision-Language

- **[Better Tokens for Better 3D: Advancing Vision-Language Modeling in 3D Medical Imaging](https://proceedings.neurips.cc/paper_files/paper/2025/hash/c4861cc81b768dc36a676fceed8f7672-Abstract-Conference.html)** — BTB3D learns compact volumetric tokens for high-resolution CT report generation and text-conditioned CT synthesis.
- **[QoQ-Med: Building Multimodal Clinical Foundation Models with Domain-Aware GRPO Training](https://proceedings.neurips.cc/paper_files/paper/2025/hash/359ffa88712bd688963a0ca641d8330b-Abstract-Conference.html)** — Trains generalist clinical models across medical images, time-series signals, and reports using rewards adjusted for domain rarity and modality difficulty.
- **[RAD: Towards Trustworthy Retrieval-Augmented Multi-modal Clinical Diagnosis](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b28ca52a43881fd87196c71145f30092-Abstract-Conference.html)** — Retrieves disease-centered knowledge and uses clinical guidelines to guide multimodal feature alignment and diagnostic fusion.

#### 🤖 Multimodal Benchmarks

- **[3D-RAD: A Comprehensive 3D Radiology Med-VQA Dataset with Multi-Temporal Analysis and Diverse Diagnostic Tasks](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f8250afec8305ed4a6b27ae405507442-Abstract-Datasets_and_Benchmarks_Track.html)** — Benchmarks CT visual question answering across six tasks, including medical computation and longitudinal diagnosis. *Datasets and Benchmarks Track*
- **[DrVD-Bench: Do Vision-Language Models Reason Like Human Doctors in Medical Image Diagnosis?](https://proceedings.neurips.cc/paper_files/paper/2025/hash/12750d99d0faa73763108ff2bbeb54fd-Abstract-Datasets_and_Benchmarks_Track.html)** — Evaluates visual evidence comprehension, diagnostic reasoning trajectories, and report generation across five medical imaging modalities. *Datasets and Benchmarks Track*
- **[SMMILE: An expert-driven benchmark for multimodal medical in-context learning](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5e0d42bf1eaafd60c03f141eb7ac761b-Abstract-Datasets_and_Benchmarks_Track.html)** — Expert-curated benchmark testing whether multimodal models can learn medical tasks from demonstrations across specialties and imaging modalities. *Datasets and Benchmarks Track*

#### 📋 Clinical NLP & EHR

- **[ClinBench: A Standardized Multi-Domain Framework for Evaluating Large Language Models in Clinical Information Extraction](https://proceedings.neurips.cc/paper_files/paper/2025/hash/621b4af77315234465ef366ea14b5dc5-Abstract-Datasets_and_Benchmarks_Track.html)** — Standardizes evaluation of structured extraction from clinical notes across oncology, atrial fibrillation, and social determinants of health. *Datasets and Benchmarks Track*
- **[MedChain: Bridging the Gap Between LLM Agents and Clinical Practice with Interactive Sequence](https://proceedings.neurips.cc/paper_files/paper/2025/hash/6bc02900c74234aa5a0c1a7148ed933f-Abstract-Datasets_and_Benchmarks_Track.html)** — Introduces sequential, interactive clinical cases and a retrieval-augmented agent spanning five stages of clinical workflow. *Datasets and Benchmarks Track*
- **[ClinicalLab: Aligning Agents for Multi-Departmental Clinical Diagnostics in the Real World](https://proceedings.neurips.cc/paper_files/paper/2025/hash/6a059625a6027aca18302803743abaa2-Abstract-Datasets_and_Benchmarks_Track.html)** — Combines a multi-department diagnostic benchmark, clinical evaluation metrics, and an agent designed around clinical workflows. *Datasets and Benchmarks Track*
- **[Detecting Data Deviations in Electronic Health Records](https://proceedings.neurips.cc/paper_files/paper/2025/hash/4b460c81b7bbdee478817bf1b7f0b9ca-Abstract-Conference.html)** — Uses layered knowledge distillation to estimate EHR data fidelity and detect records that deviate from patients' physiological states.

#### 🫀 Physiological Signals & Medical Time Series

- **[MIRA: Medical Time Series Foundation Model for Real-World Health Data](https://proceedings.neurips.cc/paper_files/paper/2025/hash/8e12ba543adc673da5b89c9311fcf72c-Abstract-Conference.html)** — Pretrains a continuous-time forecasting model to handle irregular sampling, heterogeneous frequencies, and missing observations in medical time series.
- **[GEM: Empowering MLLM for Grounded ECG Understanding with Time Series and Images](https://proceedings.neurips.cc/paper_files/paper/2025/hash/8798321486948322be2b4d658744ba72-Abstract-Conference.html)** — Unifies ECG waveforms, ECG images, and text while linking diagnostic explanations to measurable waveform evidence.

---

### NeurIPS 2024

#### 🔬 Medical Imaging & Segmentation

- **[SegVol: Universal and Interactive Volumetric Medical Image Segmentation](https://proceedings.neurips.cc/paper_files/paper/2024/hash/c7c7cf10082e454b9662a686ce6f1b6f-Abstract-Conference.html)** — 3D foundation segmentation model trained on 90K unlabeled + 6K labeled CT volumes supporting 200+ anatomical categories via semantic and spatial prompts, outperforming prior methods by up to 37%.
- **[A Textbook Remedy for Domain Shifts: Knowledge Priors for Medical Image Analysis](https://neurips.cc/virtual/2024/poster/95098)** ⭐ *Spotlight* — Knowledge-enhanced Bottlenecks (KnoBo) integrate prior medical knowledge from natural language textbooks to improve robustness against domain shifts without additional labeled data.
- **[Deep Learning in Medical Image Registration: Magic or Mirage?](https://proceedings.neurips.cc/paper_files/paper/2024/file/c3fe2a07ec47b89c50e89706d2e23358-Paper-Conference.pdf)** — Large-scale empirical study showing classical optimization often outperforms deep learning registration under standard evaluation, reorienting the field's benchmarking practices.

#### 🧫 Computational Pathology

- **[Free Lunch in Pathology Foundation Model: Task-specific Model Adaptation with Concept-Guided Feature Enhancement](https://proceedings.neurips.cc/paper_files/paper/2024/hash/9251fa7fcc356bbfc16c040f4c030d83-Abstract-Conference.html)** — Training-free adaptation strategy injecting task-specific conceptual guidance into pathology foundation models, boosting downstream performance at zero additional cost.
- **[Rethinking Transformer for Long Contextual Histopathology Whole Slide Image Analysis](https://neurips.cc/virtual/2024/poster/94232)** — Redesigns token management and attention to handle gigapixel WSIs with very long context windows, enabling slide-level weakly supervised prediction.
- **[xMIL: Insightful Explanations for Multiple Instance Learning in Histopathology](https://proceedings.neurips.cc/paper_files/paper/2024/file/0f9e0309d8a947ca44463a9b7e8b6a3f-Paper-Conference.pdf)** — Extends MIL with concept-based explanations, producing clinically interpretable predictions for biomarker detection and outcome prediction from WSIs.
- **[Leveraging Tumor Heterogeneity: Heterogeneous Graph Representation Learning for Cancer Survival Prediction in Whole Slide Images](https://proceedings.neurips.cc/paper_files/paper/2024/hash/760341adc5632de3f1cf2e8d22215a93-Abstract-Conference.html)** — ProtoSurv: heterogeneous graph model capturing spatial interactions among diverse cell populations in WSIs to improve cancer survival prediction.

#### 🤖 Foundation Models & Vision-Language

- **[Uni-Med: A Unified Medical Generalist Foundation Model For Multi-Task Learning Via Connector-MoE](https://proceedings.neurips.cc/paper_files/paper/2024/hash/941938d6c3c57b4ef4a518965e238a6d-Abstract-Conference.html)** — Connector Mixture-of-Experts (CMoE) bridges a universal visual encoder and an LLM, enabling one model to handle diverse medical imaging tasks without task-specific tuning.
- **[FairMedFM: Fairness Benchmarking for Medical Imaging Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/file/c9826b9ea5e1b49b256329934a578d83-Paper-Datasets_and_Benchmarks_Track.pdf)** — First systematic fairness benchmark evaluating 20 foundation models across 17 medical imaging datasets spanning multiple modalities and sensitive demographic attributes.
- **[HEALNet: Multimodal Fusion for Heterogeneous Biomedical Data](https://proceedings.neurips.cc/paper_files/paper/2024/file/765871e77d2ca65126d3d64d31aa6908-Paper-Conference.pdf)** — Hybrid Early-fusion Attention Learning Network that preserves modality-specific structure while capturing cross-modal interactions and handling missing modalities gracefully.
- **[MDAgents: An Adaptive Collaboration of LLMs for Medical Decision-Making](https://proceedings.neurips.cc/paper_files/paper/2024/file/90d1fc07f46e31387978b88e7e057a31-Paper-Conference.pdf)** — Multi-agent framework that automatically assigns solo or group LLM collaboration structures based on medical task complexity, improving accuracy across diverse clinical benchmarks.
- **[Enhancing Vision-Language Models for Medical Imaging: Bridging the 3D Gap with Innovative Slice Selection](https://proceedings.neurips.cc/paper_files/paper/2024/file/b53513b83232116ae25f57a174a7c993-Paper-Datasets_and_Benchmarks_Track.pdf)** — Vote-MI: unsupervised one-pass 2D slice selection that bridges 2D VLMs and 3D medical volumes (CT/MRI) without retraining the VLM.
- **[CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://arxiv.org/abs/2406.06007)** — Evaluates trustworthiness of medical VLMs across truthfulness, safety, fairness, robustness, and privacy dimensions.

#### 📋 Clinical NLP & EHR

- **[Medformer: A Multi-Granularity Patching Transformer for Medical Time-Series Classification](https://proceedings.neurips.cc/paper_files/paper/2024/hash/3fe2a777282299ecb4f9e7ebb531f0ab-Abstract-Conference.html)** — Transformer tailored for medical time-series (EEG, ECG) using multi-granularity patches to capture local and global temporal patterns, achieving SOTA on multiple clinical benchmarks.
- **[Med-Real2Sim: Non-Invasive Medical Digital Twins using Physics-Informed Self-Supervised Learning](https://proceedings.neurips.cc/paper_files/paper/2024/file/0b081a44ed0b8c0c4aa6bd886a60bea4-Paper-Conference.pdf)** — Learns virtual patient-specific cardiac simulators from non-invasive echocardiography, predicting pressure-volume loops and enabling personalized digital twins without invasive procedures.

---

### NeurIPS 2023

#### 🔬 Medical Imaging

- **[LVM-Med: Learning Large-Scale Self-Supervised Vision Models for Medical Imaging via Second-order Graph Matching](https://proceedings.neurips.cc/paper_files/paper/2023/hash/58cc11cda2a2679e8af5c6317aed0af8-Abstract-Conference.html)** — Self-supervised pretraining on ~1.3M medical images across 55 datasets using second-order graph matching for semantic structure alignment, achieving 6–7% gains over prior VLMs on challenging tasks.
- **[Aligning Synthetic Medical Images with Clinical Knowledge using Human Feedback](https://papers.nips.cc/paper_files/paper/2023/hash/2b1d1e5affe5fdb70372cd90dd8afd49-Abstract-Conference.html)** — RLHF-based alignment of generative medical image models to match clinical expert knowledge. *Sun et al.*
- **[Quilt-1M: One Million Image-Text Pairs for Histopathology](https://arxiv.org/abs/2306.11207)** — Large-scale histopathology image-text dataset harvested from YouTube educational videos, enabling VL pre-training.

#### 🤖 Foundation Models & Vision-Language

- **[LLaVA-Med: Training a Large Language-and-Vision Assistant for Biomedicine in One Day](https://proceedings.neurips.cc/paper_files/paper/2023/hash/5abcdf8ecdcacba028c6662789194572-Abstract-Datasets_and_Benchmarks.html)** — Curriculum method using GPT-4-generated self-instruction from PubMed figure-caption pairs to align a general VLM to biomedical VQA in under 15 GPU-hours.

#### 📋 Clinical NLP & EHR

- **[EHRSHOT: An EHR Benchmark for Few-Shot Evaluation of Foundation Models](https://openreview.net/forum?id=CsXC6IcdwI)** — Releases de-identified EHR data for 6,739 Stanford patients with 35 clinical tasks plus a foundation model pretrained on 2.57M patients, enabling few-shot clinical prediction benchmarking.

#### 🫀 Physiological Signals

- **[BIOT: Biosignal Transformer for Cross-data Learning in the Wild](https://proceedings.neurips.cc/paper_files/paper/2023/hash/f6b30f3e2dd9cb53bbf2024402d02295-Abstract.html)** — Tokenizes biosignals into a shared representation for cross-dataset learning despite mismatched channels, variable recording lengths, and missing values.

---

## ICML

### ICML 2025

#### 🤖 Medical Foundation Models & Benchmarks

- **[CLIMB: Data Foundations for Large Scale Multimodal Clinical Foundation Models](https://proceedings.mlr.press/v267/dai25b.html)** — Unifies clinical imaging, text, time series, and graph datasets to study multitask pretraining and multimodal transfer.
- **[MMedPO: Aligning Medical Vision-Language Models with Clinical-Aware Multimodal Preference Optimization](https://proceedings.mlr.press/v267/zhu25v.html)** — Weights preference optimization by clinical relevance using plausible hallucinations and lesion-region perturbations to improve image-grounded responses.
- **[Raptor: Scalable Train-Free Embeddings for 3D Medical Volumes Leveraging Pretrained 2D Foundation Models](https://proceedings.mlr.press/v267/an25a.html)** — Builds volumetric embeddings from frozen 2D image encoders and random projections without additional pretraining.

#### 📋 Clinical NLP & EHR

- **[BoxLM: Unifying Structures and Semantics of Medical Concepts for Diagnosis Prediction in Healthcare](https://proceedings.mlr.press/v267/tan25e.html)** — Fuses ontology and EHR hierarchies with language-model semantics through box embeddings for longitudinal diagnosis prediction.

#### 🫀 Physiological Signals & Brain AI

- **[EEG-Language Pretraining for Highly Label-Efficient Clinical Phenotyping](https://proceedings.mlr.press/v267/gijsen25a.html)** — Aligns EEG segments with clinical report segments to improve label-efficient phenotyping, zero-shot classification, and cross-modal retrieval.
- **[From Token to Rhythm: A Multi-Scale Approach for ECG-Language Pretraining](https://proceedings.mlr.press/v267/wang25du.html)** — MELP aligns ECG signals and reports at token, beat, and rhythm levels for transferable cardiac representations.

---

### ICML 2024

#### 📋 Clinical NLP & EHR

- **[ED-Copilot: Reduce Emergency Department Wait Time with Language Model Diagnostic Assistance](https://icml.cc/virtual/2024/poster/35181)** — RL-trained LLM that sequentially recommends patient-specific lab tests in the ED to minimize wait time while maximizing diagnostic accuracy, evaluated on a new MIMIC-ED-Assist benchmark.
- **[Contrastive Learning for Clinical Outcome Prediction with Partial Data Sources](https://icml.cc/virtual/2024/poster/33453)** — CLOPPS learns robust cross-modal clinical representations under missing modalities (labs, notes, imaging) via contrastive alignment, enabling strong single-source inference at test time.

#### 🫀 Physiological Signals

- **[SleepFM: Multi-modal Representation Learning for Sleep Across Brain Activity, ECG and Respiratory Signals](https://proceedings.mlr.press/v235/thapa24a.html)** — Learns multimodal representations from polysomnography using leave-one-out contrastive learning for sleep staging and sleep-disordered breathing detection.

---

### ICML 2023

#### 📋 Clinical NLP & EHR

- **[Improving Medical Predictions by Irregular Multimodal Electronic Health Records Modeling](https://icml.cc/virtual/2023/poster/24359)** — Models irregularly sampled multimodal EHR (numerical time series + clinical notes) with a dedicated alignment mechanism, yielding consistent gains on mortality and readmission prediction.

#### 📋 Radiology & Clinical Vision-Language

- **[Rethinking Medical Report Generation: Disease Revealing Enhancement with Knowledge Graph](https://arxiv.org/abs/2307.12526)** — Integrates a structured disease knowledge graph into the decoding process to surface rare and subtle findings that standard attention mechanisms overlook in chest X-ray report generation.

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

#### 🧠 EEG & Brain AI

- **[CBraMod: A Criss-Cross Brain Foundation Model for EEG Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/hash/bbbd6d915cb90be21c1254a82d45cedd-Abstract-Conference.html)** — Separately models spatial and temporal EEG dependencies with adaptable positional encoding for transfer across clinical and BCI tasks.

---

### ICLR 2024

#### 🔬 Medical Imaging & Radiology

- **[LLM-CXR: Instruction-Finetuned LLM for CXR Image Understanding and Generation](https://arxiv.org/abs/2305.11490)** — Unified LLM capable of chest X-ray image understanding, report generation, and image synthesis from text.

#### 📋 Clinical NLP & EHR

- **[MOTOR: A Time-to-Event Foundation Model For Structured Medical Records](https://arxiv.org/abs/2301.03150)** ⭐ *Spotlight* — Self-supervised TTE foundation model pre-trained on 55M EHR patient records; improves 19 clinical prediction tasks by 4.6% over SOTA with 95% label efficiency.
- **[Diagnosing Transformers: Illuminating Feature Spaces for Clinical Decision-Making](https://openreview.net/forum?id=k581sTMyPt)** — SUFO framework for interpreting fine-tuned transformer feature spaces in high-stakes clinical settings. *Hsu et al.*
- **[Multimodal Patient Representation Learning with Missing Modalities and Labels](https://openreview.net/forum?id=Je5SHCKpPa)** — Robust multimodal patient representation learning under realistic conditions of missing modalities and labels.
- **[GraphCare: Enhancing Healthcare Predictions with Personalized Knowledge Graphs](https://arxiv.org/abs/2305.12788)** — Constructs patient-specific knowledge graphs from open biomedical KGs and applies Bi-Attention Augmented GNN, achieving strong clinical prediction performance with dramatically less labeled data.

#### 🧠 Neuroimaging & EEG

- **[BrainLM: A Foundation Model for Brain Activity Recordings](https://proceedings.iclr.cc/paper_files/paper/2024/hash/029ce70401321de3808b3ac39e1ab167-Abstract-Conference.html)** — Transformer foundation model pre-trained on 6,700 hours of fMRI data; predicts clinical variables (age, anxiety, PTSD) and generalizes to unseen cohorts. *Caro et al.*
- **[Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI](https://proceedings.iclr.cc/paper_files/paper/2024/hash/47393e8594c82ce8fd83adc672cf9872-Abstract-Conference.html)** — LaBraM uses neural spectrum tokenization and masked code prediction to pretrain EEG representations across heterogeneous datasets.

---

### ICLR 2023

#### 🤖 Medical Vision-Language

- **[Medical Image Understanding with Pretrained Vision Language Models: A Comprehensive Study](https://openreview.net/pdf?id=txlWziuCE5W)** — Systematic evaluation of pretrained VLMs across 9 medical imaging datasets and 8 adaptation strategies, establishing best practices for medical VLM transfer learning.
- **[Advancing Radiograph Representation Learning with Masked Record Modeling](https://arxiv.org/abs/2301.13155)** — MRM: unified framework that reconstructs masked image patches and masked report tokens as complementary objectives, yielding strong pre-trained radiograph encoders that transfer efficiently with limited labels.

---

## ICCV / ECCV

### ICCV 2025

#### 🤖 Medical Vision-Language & Benchmarks

- **[GEMeX: A Large-Scale, Groundable, and Explainable Medical VQA Benchmark for Chest X-ray Diagnosis](https://openaccess.thecvf.com/content/ICCV2025/html/Liu_GEMeX_A_Large-Scale_Groundable_and_Explainable_Medical_VQA_Benchmark_for_ICCV_2025_paper.html)** — Pairs chest X-ray questions and answers with visual and textual explanations across multiple question formats.
- **[ProbMED: A Probabilistic Framework for Medical Multimodal Binding](https://openaccess.thecvf.com/content/ICCV2025/html/Gao_ProbMED_A_Probabilistic_Framework_for_Medical_Multimodal_Binding_ICCV_2025_paper.html)** — Aligns chest X-rays, ECGs, echocardiograms, and text as probability distributions to capture many-to-many relationships across clinical modalities.
- **[Medical World Model](https://openaccess.thecvf.com/content/ICCV2025/html/Yang_Medical_World_Model_ICCV_2025_paper.html)** — Combines vision-language policies, tumor dynamics generation, and survival analysis to simulate treatment-conditioned disease evolution.

#### 🧫 Computational Pathology

- **[PathFinder: A Multi-Modal Multi-Agent System for Medical Diagnostic Decision-Making Applied to Histopathology](https://openaccess.thecvf.com/content/ICCV2025/html/Ghezloo_PathFinder_A_Multi-Modal_Multi-Agent_System_for_Medical_Diagnostic_Decision-Making_Applied_ICCV_2025_paper.html)** — Coordinates triage, navigation, description, and diagnosis agents to inspect whole-slide images and explain diagnostic evidence.
- **[Normal and Abnormal Pathology Knowledge-Augmented Vision-Language Model for Anomaly Detection in Pathology Images](https://openaccess.thecvf.com/content/ICCV2025/html/Song_Normal_and_Abnormal_Pathology_Knowledge-Augmented_Vision-Language_Model_for_Anomaly_Detection_ICCV_2025_paper.html)** — Ano-NAViLa incorporates descriptions of normal and abnormal tissue to detect and localize pathology anomalies with image-text explanations.
- **[PS3: A Multimodal Transformer Integrating Pathology Reports with Histology Images and Biological Pathways for Cancer Survival Prediction](https://openaccess.thecvf.com/content/ICCV2025/html/Raza_PS3_A_Multimodal_Transformer_Integrating_Pathology_Reports_with_Histology_Images_ICCV_2025_paper.html)** — Integrates pathology reports, whole-slide histology, and pathway information for multimodal cancer prognosis.
- **[PathDiff: Histopathology Image Synthesis with Unpaired Text and Mask Conditions](https://openaccess.thecvf.com/content/ICCV2025/html/Bhosale_PathDiff_Histopathology_Image_Synthesis_with_Unpaired_Text_and_Mask_Conditions_ICCV_2025_paper.html)** — Learns from unpaired text and mask datasets to generate histopathology images with controllable semantic and spatial content.

#### 🏥 Surgical AI & Medical Video

- **[OphCLIP: Hierarchical Retrieval-Augmented Learning for Ophthalmic Surgical Video-Language Pretraining](https://openaccess.thecvf.com/content/ICCV2025/html/Hu_OphCLIP_Hierarchical_Retrieval-Augmented_Learning_for_Ophthalmic_Surgical_Video-Language_Pretraining_ICCV_2025_paper.html)** — Learns from hierarchical ophthalmic video-text annotations and retrieved silent videos for surgical phase and instrument recognition.
- **[MedVSR: Medical Video Super-Resolution with Cross State-Space Propagation](https://openaccess.thecvf.com/content/ICCV2025/html/Liu_MedVSR_Medical_Video_Super-Resolution_with_Cross_State-Space_Propagation_ICCV_2025_paper.html)** — Uses state-space propagation and reconstruction to improve medical video resolution under noise, camera motion, and abrupt transitions.

---

### ECCV 2024

#### 🔬 Medical Imaging & Segmentation

- **[ScribblePrompt: Fast and Flexible Interactive Segmentation for Any Biomedical Image](https://arxiv.org/abs/2312.07381)** — Interactive segmentation network trained on 65,000+ scribble annotations across 54,000+ images, outperforming SAM and specialist models using scribbles, clicks, or bounding boxes on diverse biomedical images.
- **[AnaToMask: Enhancing Medical Image Segmentation with Reconstruction-guided Self-masking](https://eccv.ecva.net/virtual/2024/poster/1161)** — Anatomy-aware masked image modeling for self-supervised 3D medical image segmentation; dynamically masks anatomically significant regions via reconstruction loss.
- **[I-MedSAM: Implicit Medical Image Segmentation with Segment Anything](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01503.pdf)** — Extends SAM to medical images via implicit neural representations that model continuous anatomical boundaries, enabling high-resolution segmentation without resolution-dependent retraining.
- **[NePhi: Neural Deformation Fields for Approximately Diffeomorphic Medical Image Registration](https://arxiv.org/abs/2309.07322)** — Memory-efficient neural deformation fields for large-scale 3D medical image registration.

---

### ICCV 2023

#### 🔬 Medical Imaging & Segmentation

- **[UniverSeg: Universal Medical Image Segmentation](https://arxiv.org/abs/2304.06131)** — CrossBlock mechanism that produces accurate segmentation maps for any new anatomy or modality given a small labeled support set, trained on 53 open-access datasets (MegaMedical). *Butoi et al., MIT CSAIL*
- **[CLIP-Driven Universal Model for Organ Segmentation and Tumor Detection](https://arxiv.org/abs/2301.00785)** — CLIP text embeddings guide a universal segmentation model to handle 25 organs and 6 tumor types with open-vocabulary extensibility.
- **[CancerUniT: Towards a Single Unified Model for Effective Detection, Segmentation, and Diagnosis of Eight Major Cancers using a Large Collection of CT Scans](https://arxiv.org/abs/2301.12291)** — Joint detection, segmentation, and diagnosis of 8 cancer types in a single model trained on 1,000+ CT scans.
- **[Preserving Tumor Volumes for Unsupervised Medical Image Registration](https://arxiv.org/abs/2309.10153)** — Volume-preservation regularization for unsupervised deformable registration to prevent pathological tissue distortion.
- **[CuNeRF: Cube-based Neural Radiance Field for Zero-Shot Medical Image Arbitrary-Scale Super Resolution](https://arxiv.org/abs/2303.16242)** — Divides 3D medical volumes into cubes and applies NeRF-based implicit representation for zero-shot arbitrary-scale super-resolution.
- **[Learning to Distill Global Representation for Sparse-View CT](https://arxiv.org/abs/2308.08463)** — GloReDi distills global frequency and spatial features from a dense-view teacher to reconstruct high-quality CT from sparse projections.

#### 🤖 Medical Vision-Language

- **[MedKLIP: Medical Knowledge Enhanced Language-Image Pre-Training for X-ray Diagnosis](https://arxiv.org/abs/2301.02228)** — Enriches VL pre-training by replacing raw report text with structured medical entity triplets, achieving strong zero-shot and few-shot performance on 11 X-ray datasets.
- **[PRIOR: Prototype Representation Joint Learning from Medical Images and Reports](https://arxiv.org/abs/2307.12577)** — Prototype-based joint learning aligns local image regions with report sentences for fine-grained medical VL representation.
- **[LIMITR: Leveraging Local Information for Medical Image-Text Representation](https://arxiv.org/abs/2303.11755)** — Local-region contrastive alignment between chest X-ray patches and report sentences for improved downstream classification and retrieval.
- **[Towards Unifying Medical Vision-and-Language Pre-training via Soft Prompts](https://arxiv.org/abs/2302.08958)** — Soft-prompt-based unified pre-training framework across diverse medical vision-language tasks.

#### 🧫 Computational Pathology

- **[Multimodal Optimal Transport-based Co-Attention Transformer with Global Structure Consistency for Survival Prediction](https://arxiv.org/abs/2306.08330)** — MOTCat: optimal transport aligns pathology patches with genomic features for robust multimodal survival prediction on TCGA datasets.
- **[Cross-Modal Translation and Alignment for Survival Analysis](https://arxiv.org/abs/2309.12855)** — CMTA translates between pathology and genomic modalities bidirectionally and aligns their representations for improved cancer survival prediction.
- **[ConSlide: Asynchronous Hierarchical Interaction Transformer with Breakup-Reorganize Rehearsal for Continual Whole Slide Image Analysis](https://arxiv.org/abs/2308.13324)** — Continual learning framework for WSI analysis that handles sequentially arriving cancer datasets without forgetting.
- **[Improving Representation Learning for Histopathologic Images with Cluster Constraints](https://arxiv.org/abs/2310.12334)** — CluSiam adds cluster-consistency constraints to self-supervised pre-training, improving patch-level histopathology representations.

---

## ACL / EMNLP

### ACL 2025

#### 📋 Clinical Agents, Reasoning & Evaluation

- **[AfriMed-QA: A Pan-African, Multi-Specialty, Medical Question-Answering Benchmark Dataset](https://aclanthology.org/2025.acl-long.96/)** — Evaluates medical question answering and demographic bias using questions spanning African countries and medical specialties.
- **[ReflecTool: Towards Reflection-Aware Tool-Augmented Clinical Agents](https://aclanthology.org/2025.acl-long.663/)** — Introduces a clinical agent benchmark and uses stored tool experience, reflection, and verification to improve clinical tool use.
- **[Towards Omni-RAG: Comprehensive Retrieval-Augmented Generation for Large Language Models in Medical Applications](https://aclanthology.org/2025.acl-long.742/)** — Introduces MedOmniKB and source planning optimization to retrieve suitable evidence from heterogeneous medical knowledge sources.

#### 🤖 Medical Vision-Language & Radiology

- **[Asclepius: A Spectrum Evaluation Benchmark for Medical Multi-Modal Large Language Models](https://aclanthology.org/2025.acl-long.1178/)** — Evaluates medical multimodal models across specialties and diagnostic capacities with specialist comparisons.
- **[Exploring Compositional Generalization of Multimodal LLMs for Medical Imaging](https://aclanthology.org/2025.acl-long.639/)** — Uses Med-MAT to study generalization to unseen combinations of imaging modality, anatomy, and task.
- **[Improving Medical Large Vision-Language Models with Abnormal-Aware Feedback](https://aclanthology.org/2025.acl-long.636/)** — UMed-LVLM combines abnormality-focused instruction tuning and reward signals to improve localization and image understanding.
- **[The Impact of Auxiliary Patient Data on Automated Chest X-Ray Report Generation and How to Incorporate It](https://aclanthology.org/2025.acl-long.9/)** — CXRMate-ED incorporates clinical history, vital signs, and other emergency-department records into chest X-ray report generation.

---

### ACL 2024

#### 📋 Clinical NLP

- **[DocLens: Multi-aspect Fine-grained Evaluation for Medical Text Generation](https://aclanthology.org/2024.acl-long.708/)** — Proposes multi-aspect, fine-grained automatic evaluation metrics (accuracy, completeness, conciseness) for clinical text generation tasks like discharge summaries, addressing shortcomings of ROUGE/BLEU for medical NLP.
- **[RAM-EHR: Retrieval Augmentation Meets Clinical Predictions on Electronic Health Records](https://aclanthology.org/2024.acl-short.68/)** — Augments EHR predictive models with retrieval from similar historical patient visits and summarized external knowledge, improving clinical risk prediction across multiple tasks.

---

### ACL 2023

#### 📋 Clinical NLP

- **[ORGAN: Observation-Guided Radiology Report Generation via Tree-Reasoning](https://aclanthology.org/2023.acl-long.451/)** — Tree-structured reasoning over clinical observations guides a decoder to generate complete, clinically consistent radiology reports with explicit rationales.

---

### EMNLP 2025

#### 📋 Clinical Dialogue, Adaptation & Evaluation

- **[Ask Patients with Patience: Enabling LLMs for Human-Centric Medical Dialogue with Grounded Reasoning](https://aclanthology.org/2025.emnlp-main.142/)** — Combines medical guidelines and Bayesian active learning for adaptive symptom gathering and transparent multi-turn diagnostic dialogue.
- **[MedHallu: A Comprehensive Benchmark for Detecting Medical Hallucinations in Large Language Models](https://aclanthology.org/2025.emnlp-main.143/)** — Benchmarks detection of plausible but incorrect medical answers with controlled hallucination difficulty and uncertainty-aware evaluation.
- **[3MDBench: Medical Multimodal Multi-agent Dialogue Benchmark](https://aclanthology.org/2025.emnlp-main.1353/)** — Simulates multimodal telemedical consultations with patient and assessor agents to evaluate diagnostic accuracy and dialogue quality.
- **[3DS: Medical Domain Adaptation of LLMs via Decomposed Difficulty-based Data Selection](https://aclanthology.org/2025.emnlp-main.983/)** — Selects medical instruction-tuning examples using model-specific estimates of understanding, response confidence, and correctness.

---

### EMNLP 2024

#### 📋 Clinical NLP

- **[RULE: Reliable Multimodal RAG for Factuality in Medical Vision Language Models](https://arxiv.org/abs/2407.05131)** — Retrieval-augmented framework that enforces factual grounding in medical VLM responses via controllable context selection.

### EMNLP 2023

#### 📋 Clinical NLP

- **[PhenotypeCLIP: Phenotype-based Contrastive Learning for Medical Imaging Report Generation](https://aclanthology.org/2023.emnlp-main.125/)** — Phenotype-aware contrastive learning for factually accurate and clinically consistent radiology report generation.

---

## NAACL

### NAACL 2025

#### 📋 Clinical NLP

- **[Benchmarking Large Language Models on Answering and Explaining Challenging Medical Questions](https://aclanthology.org/2025.naacl-long.182/)** — Introduces JAMA Clinical Challenge and Medbullets to evaluate medical question answering and explanations against expert-written references.
- **[MeNTi: Bridging Medical Calculator and LLM Agent with Nested Tool Calling](https://aclanthology.org/2025.naacl-long.263/)** — Introduces a medical calculator agent and CalcQA benchmark covering tool selection, nested calculations, slot filling, and unit conversion.
- **[Afrispeech-Dialog: A Benchmark Dataset for Spontaneous English Conversations in Healthcare and Beyond](https://aclanthology.org/2025.naacl-long.426/)** — Evaluates African-accented conversational speech recognition and how transcription errors affect medical dialogue summaries.

#### 🤖 Medical Vision-Language & Radiology

- **[VividMed: Vision Language Model with Versatile Visual Grounding for Medicine](https://aclanthology.org/2025.naacl-long.89/)** — Supports segmentation masks and bounding boxes alongside VQA and report generation for both 2D and 3D medical images.
- **[Fact-Aware Multimodal Retrieval Augmentation for Accurate Medical Radiology Report Generation](https://aclanthology.org/2025.naacl-long.28/)** — FactMM-RAG trains a fact-aware retriever from RadGraph-derived report pairs to provide reference reports for radiology generation.

---

### NAACL 2024

#### 📋 Clinical NLP

- **[LLM-based Medical Assistant Personalization with Short- and Long-Term Memory Coordination](https://aclanthology.org/2024.naacl-long.132/)** — Memory coordination mechanism that balances short-term context and long-term patient history in LLM-based medical assistants for personalised clinical dialogue.

---

## AAAI

### AAAI 2025

#### 🔬 Medical Imaging & Segmentation

- **[Generative Medical Segmentation](https://ojs.aaai.org/index.php/AAAI/article/view/32402)** — Reformulates medical image segmentation as a generative modeling problem, enabling open-vocabulary segmentation of arbitrary anatomical or pathological structures beyond fixed training categories.
- **[U-KAN Makes Strong Backbone for Medical Image Segmentation and Generation](https://ojs.aaai.org/index.php/AAAI/article/view/32491)** — Integrates KAN (Kolmogorov-Arnold Network) layers into the U-Net pipeline on tokenized intermediate features, yielding a new backbone that achieves higher accuracy with lower compute on medical segmentation benchmarks.
- **[Every Component Counts: Rethinking the Measure of Success for Medical Semantic Segmentation in Multi-Instance Segmentation Tasks](https://ojs.aaai.org/index.php/AAAI/article/view/32408)** — Proposes CC-Metrics, revealing that standard mean-IoU severely underestimates segmentation failure on small/rare objects in multi-instance medical tasks.
- **[FAMNet: Frequency-aware Matching Network for Cross-domain Few-shot Medical Image Segmentation](https://ojs.aaai.org/index.php/AAAI/article/view/32184)** — Frequency-domain feature matching for few-shot segmentation across CT and MRI domains, mitigating texture/contrast shifts between scanners without expensive domain-specific retraining.
- **[Motion Artifact Removal in Pixel-Frequency Domain via Alternate Masks and Diffusion Model](https://ojs.aaai.org/index.php/AAAI/article/view/32960)** — Uses pixel and frequency information with complementary masks to remove MRI motion artifacts through a pretrained diffusion model.
- **[Single Exposure Quantitative Phase Imaging with a Conventional Microscope Using Diffusion Models](https://ojs.aaai.org/index.php/AAAI/article/view/32271)** — Combines chromatic aberrations and zero-mean diffusion to recover quantitative phase from a single microscope exposure, including clinical urine microscopy.

#### 🤖 Foundation Models & VLM

- **[Advancing Medical Multimodal Learning and Data Generation with Diffusion Model and LLM](https://ojs.aaai.org/index.php/AAAI/article/view/35237)** — Dual framework: MedDiffusion for synthetic multimodal patient data generation and EHRPD for sequential EHR generation, advancing health risk prediction through data augmentation.

---

### AAAI 2024

#### 🔬 Medical Imaging & Segmentation

- **[MedSegDiff-V2: Diffusion based Medical Image Segmentation with Transformer](https://arxiv.org/abs/2301.11798)** — Upgraded diffusion segmentation framework that replaces the UNet denoiser with a Transformer backbone, outperforming prior diffusion-based segmentation models across multiple modalities.

#### 🏥 Surgical AI

- **[SurgicalSAM: Efficient Class Promptable Surgical Instrument Segmentation](https://ojs.aaai.org/index.php/AAAI/article/view/28514)** — Adapts SAM with prototype-based class prompts and contrastive learning for surgical instrument segmentation without manually specified points or boxes.

#### 📋 Clinical NLP & EHR

- **[MedAlign: A Clinician-Generated Dataset for Instruction Following with Electronic Medical Records](https://arxiv.org/abs/2308.14089)** — Expert-annotated dataset benchmarking LLM instruction-following in EHR contexts across diverse clinical tasks.
- **[Bootstrapping Large Language Models for Radiology Report Generation](https://ojs.aaai.org/index.php/AAAI/article/view/29826)** — Curriculum bootstrapping strategy that uses an LLM to iteratively generate and filter pseudo-labeled reports for self-training, improving radiology report quality with minimal annotated data.

---

### AAAI 2023

#### 🔬 Medical Imaging & Segmentation

- **[Unsupervised Domain Adaptation for Medical Image Segmentation by Selective Entropy Constraint and Adaptive Semantic Alignment](https://github.com/fengweie/SE_ASA)** — SE-ASA selectively constrains prediction entropy on confident regions and aligns domain semantics via adaptive class prototypes for cross-modality (MR↔CT) segmentation without target labels.

#### 📋 Clinical NLP

- **[Nothing Abnormal: Disambiguating Medical Reports via Contrastive Knowledge Infusion](https://arxiv.org/abs/2305.08300)** — Contrastive knowledge infusion disambiguates the ubiquitous "no abnormality" phrase in radiology reports, improving clinical NLP classification by pulling normal and pathological report representations apart.

---

## KDD

### KDD 2025

#### 📋 Clinical & Healthcare AI

- **[TarDiff: Target-Oriented Diffusion Guidance for Synthetic Electronic Health Record Time Series Generation](https://doi.org/10.1145/3711896.3737147)** — Generates synthetic EHR time series with target-oriented diffusion guidance to support downstream prediction under data scarcity and class imbalance.
- **[A Diffusion-Based Method for Learning the Multi-Outcome Distribution of Medical Treatments](https://doi.org/10.1145/3711896.3736819)** — DIME models the joint interventional distribution of dependent, mixed-type treatment outcomes for uncertainty-aware treatment effect estimation.
- **[Test-Time Training with Diversified Local Aggregation Consistency for Mortality Prediction using Clinical Time Series](https://doi.org/10.1145/3711896.3737151)** — Adapts mortality prediction models to individual target patients while addressing temporal imbalance and cross-institution domain shifts.

---

### KDD 2024

#### 📋 Clinical & Healthcare AI

- **[Clinical Trial Outcome Prediction with Drug-Disease Interaction and Heterogeneous GNN](https://dl.acm.org/doi/10.1145/3637528)** — Heterogeneous GNN modeling drug-disease interactions for clinical trial success prediction.

---

### KDD 2023

#### 📋 Clinical & Healthcare AI

- **[Expert Knowledge-Aware Image Difference Graph Representation Learning for Difference-Aware Medical Visual Question Answering](https://arxiv.org/abs/2307.11986)** — Knowledge graph encoding expert-defined difference relationships between paired medical images for difference-aware VQA on MIMIC-Diff-VQA benchmark.

---

## Contributing

Contributions are very welcome!

- **Add a paper**: Open a PR with the paper entry in the appropriate conference section, using the format:  
  `**[Title](URL)** — One-sentence description. *Authors*`
- **Fix a broken link**: Open an issue or PR.
- **Suggest a new category**: Open an issue to discuss.
- **Verify metadata**: Check the title, conference, publication year, and summary against the official proceedings; prefer a paper-specific proceedings page or DOI over a general accepted-papers list.
- **Avoid duplicates**: Check for both the full title and model acronym before adding a paper, including papers with an earlier arXiv date.

**Scope**: Papers published at CS/AI conference proceedings (CVPR, NeurIPS, ICLR, ICML, ICCV, ECCV, ACL, EMNLP, NAACL, AAAI, KDD, etc.) in the years 2023–2025 on topics of medical imaging, clinical NLP, surgical AI, or health AI. Pure biology papers (drug discovery, protein folding, genomics) are out of scope.

---

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related rights to this work.
