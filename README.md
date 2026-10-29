# Awesome Medical AI Papers [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of medical AI, healthcare AI, and medical imaging papers published at top CS/AI conferences: **CVPR, NeurIPS, ICLR, ICML, ICCV, ECCV, ACL, EMNLP, NAACL, AAAI, KDD**, and more.

Covers **2023–2025**. Organized by conference publication year, which may differ from the arXiv submission year. Contributions welcome — see [Contributing](#contributing).

---

<!-- curated-counts:start -->
**1,430 papers** across 2023–2025. Entries use official proceedings titles and conference publication years. See the [curation ledger](data/curation.json), [metadata corrections](docs/metadata-audit.md), and [remaining review queue](reports/candidates.md).

| Conference | 2023 | 2024 | 2025 | Total |
|---|---:|---:|---:|---:|
| CVPR | 43 | 77 | 89 | 209 |
| NeurIPS | 57 | 98 | 161 | 316 |
| ICML | 10 | 24 | 52 | 86 |
| ICLR | 13 | 24 | 52 | 89 |
| ICCV / ECCV | 40 | 69 | 86 | 195 |
| ACL / EMNLP | 51 | 51 | 95 | 197 |
| NAACL | 0 | 17 | 19 | 36 |
| AAAI | 49 | 68 | 124 | 241 |
| KDD | 19 | 15 | 27 | 61 |

Counts describe this curated list, not all relevant papers in each proceedings. Datasets, benchmarks, and special tracks are labeled when applicable; workshops, doctoral/student abstracts, and pure molecular/genomics work are outside the current scope.
<!-- curated-counts:end -->

## Legend

| Icon | Topic |
|------|-------|
| 🔬 | Medical Imaging & Segmentation |
| 🧫 | Computational Pathology & Microscopy |
| 🤖 | Foundation Models & Vision-Language |
| 📋 | Clinical NLP, EHR & Healthcare |
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
- [Proceedings indexing](#proceedings-indexing)
- [Contributing](#contributing)

---

## CVPR

### CVPR 2025

#### 🔬 Medical Imaging & Segmentation

- **[3D Dental Model Segmentation with Geometrical Boundary Preserving](https://openaccess.thecvf.com/content/CVPR2025/html/Xi_3D_Dental_Model_Segmentation_with_Geometrical_Boundary_Preserving_CVPR_2025_paper.html)** — Segments 3D dental models while preserving geometric boundaries.
- **[Advancing Generalizable Tumor Segmentation with Anomaly-Aware Open-Vocabulary Attention Maps and Frozen Foundation Diffusion Models](https://openaccess.thecvf.com/content/CVPR2025/html/Jiang_Advancing_Generalizable_Tumor_Segmentation_with_Anomaly-Aware_Open-Vocabulary_Attention_Maps_and_CVPR_2025_paper.html)** — Uses anomaly-aware open-vocabulary attention and frozen diffusion priors for tumor segmentation.
- **[AeSPa : Attention-guided Self-supervised Parallel Imaging for MRI Reconstruction](https://openaccess.thecvf.com/content/CVPR2025/html/Joo_AeSPa__Attention-guided_Self-supervised_Parallel_Imaging_for_MRI_Reconstruction_CVPR_2025_paper.html)** — Uses attention-guided self-supervision for parallel MRI reconstruction.
- **[Anatomical Consistency and Adaptive Prior-informed Transformation for Multi-contrast MR Image Synthesis via Diffusion Model](https://openaccess.thecvf.com/content/CVPR2025/html/Shin_Anatomical_Consistency_and_Adaptive_Prior-informed_Transformation_for_Multi-contrast_MR_Image_CVPR_2025_paper.html)** — Conditions diffusion-based multicontrast MRI synthesis on anatomical consistency and adaptive priors.
- **[Annotation Ambiguity Aware Semi-Supervised Medical Image Segmentation](https://openaccess.thecvf.com/content/CVPR2025/html/Kumari_Annotation_Ambiguity_Aware_Semi-Supervised_Medical_Image_Segmentation_CVPR_2025_paper.html)** — Accounts for ambiguous annotations in semi-supervised medical segmentation.
- **[A Semantic Knowledge Complementarity based Decoupling Framework for Semi-supervised Class-imbalanced Medical Image Segmentation](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_A_Semantic_Knowledge_Complementarity_based_Decoupling_Framework_for_Semi-supervised_Class-imbalanced_CVPR_2025_paper.html)** — Uses complementary semantic knowledge for class-imbalanced semi-supervised medical segmentation.
- **[A Unified Model for Compressed Sensing MRI Across Undersampling Patterns](https://openaccess.thecvf.com/content/CVPR2025/html/Jatyani_A_Unified_Model_for_Compressed_Sensing_MRI_Across_Undersampling_Patterns_CVPR_2025_paper.html)** — Reconstructs compressed-sensing MRI across different undersampling patterns with one model.
- **[beta-FFT: Nonlinear Interpolation and Differentiated Training Strategies for Semi-Supervised Medical Image Segmentation](https://openaccess.thecvf.com/content/CVPR2025/html/Hu_beta-FFT_Nonlinear_Interpolation_and_Differentiated_Training_Strategies_for_Semi-Supervised_Medical_CVPR_2025_paper.html)** — Uses nonlinear interpolation and differentiated training for semi-supervised medical segmentation.
- **[Blood Flow Speed Estimation with Optical Coherence Tomography Angiography Images](https://openaccess.thecvf.com/content/CVPR2025/html/Cheng_Blood_Flow_Speed_Estimation_with_Optical_Coherence_Tomography_Angiography_Images_CVPR_2025_paper.html)** — Estimates blood-flow speed from optical coherence tomography angiography.
- **[Boost the Inference with Co-training: A Depth-guided Mutual Learning Framework for Semi-supervised Medical Polyp Segmentation](https://openaccess.thecvf.com/content/CVPR2025/html/Li_Boost_the_Inference_with_Co-training_A_Depth-guided_Mutual_Learning_Framework_CVPR_2025_paper.html)** — Uses depth information and mutual co-training for semi-supervised polyp segmentation.
- **[CheXwhatsApp: A Dataset for Exploring Challenges in the Diagnosis of Chest X-rays through Mobile Devices](https://openaccess.thecvf.com/content/CVPR2025/html/Antony_CheXwhatsApp_A_Dataset_for_Exploring_Challenges_in_the_Diagnosis_of_CVPR_2025_paper.html)** — Benchmarks chest X-ray diagnosis under mobile-device acquisition conditions.
- **[Cross-Modal Interactive Perception Network with Mamba for Lung Tumor Segmentation in PET-CT Images](https://openaccess.thecvf.com/content/CVPR2025/html/Mei_Cross-Modal_Interactive_Perception_Network_with_Mamba_for_Lung_Tumor_Segmentation_CVPR_2025_paper.html)** — Fuses PET and CT information through interactive state-space representations for lung tumor segmentation.
- **[CSC-PA: Cross-image Semantic Correlation via Prototype Attentions for Single-network Semi-supervised Breast Tumor Segmentation](https://openaccess.thecvf.com/content/CVPR2025/html/Ding_CSC-PA_Cross-image_Semantic_Correlation_via_Prototype_Attentions_for_Single-network_Semi-supervised_CVPR_2025_paper.html)** — Uses cross-image prototype attention for semi-supervised breast tumor segmentation.
- **[DeformCL: Learning Deformable Centerline Representation for Vessel Extraction in 3D Medical Image](https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_DeformCL_Learning_Deformable_Centerline_Representation_for_Vessel_Extraction_in_3D_CVPR_2025_paper.html)** — Learns deformable vessel centerlines for extraction from 3D medical images.
- **[Domain Adaptive Diabetic Retinopathy Grading with Model Absence and Flowing Data](https://openaccess.thecvf.com/content/CVPR2025/html/Su_Domain_Adaptive_Diabetic_Retinopathy_Grading_with_Model_Absence_and_Flowing_CVPR_2025_paper.html)** — Adapts diabetic retinopathy grading to streaming target data without the source model.
- **[DyCON: Dynamic Uncertainty-aware Consistency and Contrastive Learning for Semi-supervised Medical Image Segmentation](https://openaccess.thecvf.com/content/CVPR2025/html/Assefa_DyCON_Dynamic_Uncertainty-aware_Consistency_and_Contrastive_Learning_for_Semi-supervised_Medical_CVPR_2025_paper.html)** — Uncertainty-aware consistency and contrastive objectives for semi-supervised volumetric segmentation.
- **[EchoONE: Segmenting Multiple Echocardiography Planes in One Model](https://openaccess.thecvf.com/content/CVPR2025/html/Hu_EchoONE_Segmenting_Multiple_Echocardiography_Planes_in_One_Model_CVPR_2025_paper.html)** — Segments multiple echocardiographic planes with a shared model.
- **[EffiDec3D: An Optimized Decoder for High-Performance and Efficient 3D Medical Image Segmentation](https://openaccess.thecvf.com/content/CVPR2025/html/Rahman_EffiDec3D_An_Optimized_Decoder_for_High-Performance_and_Efficient_3D_Medical_CVPR_2025_paper.html)** — Optimizes decoding for efficient volumetric medical segmentation.
- **[Interactive Medical Image Analysis with Concept-based Similarity Reasoning](https://openaccess.thecvf.com/content/CVPR2025/html/Huy_Interactive_Medical_Image_Analysis_with_Concept-based_Similarity_Reasoning_CVPR_2025_paper.html)** — Supports interactive medical image analysis through concept-based similarity reasoning.
- **[Interactive Medical Image Segmentation: A Benchmark Dataset and Baseline](https://openaccess.thecvf.com/content/CVPR2025/html/Cheng_Interactive_Medical_Image_Segmentation_A_Benchmark_Dataset_and_Baseline_CVPR_2025_paper.html)** — Introduces IMIS-Bench, a comprehensive benchmark for interactive medical image segmentation across diverse modalities and organs.
- **[Latent Drifting in Diffusion Models for Counterfactual Medical Image Synthesis](https://openaccess.thecvf.com/content/CVPR2025/html/Yeganeh_Latent_Drifting_in_Diffusion_Models_for_Counterfactual_Medical_Image_Synthesis_CVPR_2025_paper.html)** — Generates counterfactual medical images by drifting in the latent space of diffusion models, enabling controlled pathology simulation.
- **[LesionLocator: Zero-Shot Universal Tumor Segmentation and Tracking in 3D Whole-Body Imaging](https://openaccess.thecvf.com/content/CVPR2025/html/Rokuss_LesionLocator_Zero-Shot_Universal_Tumor_Segmentation_and_Tracking_in_3D_Whole-Body_CVPR_2025_paper.html)** — Zero-shot framework for tumor segmentation and longitudinal tracking across unseen tumor types in whole-body 3D scans.
- **[LMO: Linear Mamba Operator for MRI Reconstruction](https://openaccess.thecvf.com/content/CVPR2025/html/Li_LMO_Linear_Mamba_Operator_for_MRI_Reconstruction_CVPR_2025_paper.html)** — Uses linear state-space operators for MRI reconstruction.
- **[Minding Fuzzy Regions: A Data-driven Alternating Learning Paradigm for Stable Lesion Segmentation](https://openaccess.thecvf.com/content/CVPR2025/html/Fang_Minding_Fuzzy_Regions_A_Data-driven_Alternating_Learning_Paradigm_for_Stable_CVPR_2025_paper.html)** — Uses alternating learning to stabilize segmentation of ambiguous lesion regions.
- **[Multi-modal Medical Diagnosis via Large-small Model Collaboration](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_Multi-modal_Medical_Diagnosis_via_Large-small_Model_Collaboration_CVPR_2025_paper.html)** — Collaborative inference framework between large and small models for multi-modal clinical diagnosis.
- **[nnWNet: Rethinking the Use of Transformers in Biomedical Image Segmentation and Calling for a Unified Evaluation Benchmark](https://openaccess.thecvf.com/content/CVPR2025/html/Zhou_nnWNet_Rethinking_the_Use_of_Transformers_in_Biomedical_Image_Segmentation_CVPR_2025_paper.html)** — Reassesses transformer-based biomedical segmentation and proposes a unified evaluation benchmark.
- **[Noise-Consistent Siamese-Diffusion for Medical Image Synthesis and Segmentation](https://openaccess.thecvf.com/content/CVPR2025/html/Qiu_Noise-Consistent_Siamese-Diffusion_for_Medical_Image_Synthesis_and_Segmentation_CVPR_2025_paper.html)** — Uses noise-consistent diffusion for joint medical image synthesis and segmentation.
- **[OpenMIBOOD: Open Medical Imaging Benchmarks for Out-Of-Distribution Detection](https://openaccess.thecvf.com/content/CVPR2025/html/Gutbrod_OpenMIBOOD_Open_Medical_Imaging_Benchmarks_for_Out-Of-Distribution_Detection_CVPR_2025_paper.html)** — Provides medical imaging benchmarks for detecting out-of-distribution inputs.
- **[OralXrays-9: Towards Hospital-Scale Panoramic X-ray Anomaly Detection via Personalized Multi-Object Query-Aware Mining](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_OralXrays-9_Towards_Hospital-Scale_Panoramic_X-ray_Anomaly_Detection_via_Personalized_Multi-Object_CVPR_2025_paper.html)** — Uses personalized queries to detect anomalies in panoramic dental X-rays.
- **[Patient-Level Anatomy Meets Scanning-Level Physics: Personalized Federated Low-Dose CT Denoising Empowered by Large Language Model](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_Patient-Level_Anatomy_Meets_Scanning-Level_Physics_Personalized_Federated_Low-Dose_CT_Denoising_CVPR_2025_paper.html)** — Personalizes federated low-dose CT denoising using anatomy, scanner physics, and language-model guidance.
- **[Prompt2Perturb (P2P): Text-Guided Diffusion-Based Adversarial Attack on Breast Ultrasound Images](https://openaccess.thecvf.com/content/CVPR2025/html/Medghalchi_Prompt2Perturb_P2P_Text-Guided_Diffusion-Based_Adversarial_Attack_on_Breast_Ultrasound_Images_CVPR_2025_paper.html)** — Studies text-guided diffusion attacks on breast ultrasound models.
- **[Revisiting MAE Pre-training for 3D Medical Image Segmentation](https://openaccess.thecvf.com/content/CVPR2025/html/Wald_Revisiting_MAE_Pre-training_for_3D_Medical_Image_Segmentation_CVPR_2025_paper.html)** — Examines masked-autoencoder pretraining for volumetric medical segmentation.
- **[SACB-Net: Spatial-awareness Convolutions for Medical Image Registration](https://openaccess.thecvf.com/content/CVPR2025/html/Cheng_SACB-Net_Spatial-awareness_Convolutions_for_Medical_Image_Registration_CVPR_2025_paper.html)** — Uses spatially aware convolutions for medical image registration.
- **[Show and Segment: Universal Medical Image Segmentation via In-Context Learning](https://openaccess.thecvf.com/content/CVPR2025/html/Gao_Show_and_Segment_Universal_Medical_Image_Segmentation_via_In-Context_Learning_CVPR_2025_paper.html)** — Segments medical images through in-context examples across tasks.
- **[Steady Progress Beats Stagnation: Mutual Aid of Foundation and Conventional Models in Mixed Domain Semi-Supervised Medical Image Segmentation](https://openaccess.thecvf.com/content/CVPR2025/html/Ma_Steady_Progress_Beats_Stagnation_Mutual_Aid_of_Foundation_and_Conventional_CVPR_2025_paper.html)** — Combines foundation and conventional models for mixed-domain semi-supervised segmentation.
- **[Test-Time Domain Generalization via Universe Learning: A Multi-Graph Matching Approach for Medical Image Segmentation](https://openaccess.thecvf.com/content/CVPR2025/html/Lv_Test-Time_Domain_Generalization_via_Universe_Learning_A_Multi-Graph_Matching_Approach_CVPR_2025_paper.html)** — Uses multigraph matching to generalize medical segmentation at inference.
- **[Towards All-in-One Medical Image Re-Identification](https://openaccess.thecvf.com/content/CVPR2025/html/Tian_Towards_All-in-One_Medical_Image_Re-Identification_CVPR_2025_paper.html)** — Benchmarks patient re-identification across imaging modalities and introduces modality-adaptive representations for personalized diagnosis and privacy analysis.
- **[Unified Medical Lesion Segmentation via Self-referring Indicator](https://openaccess.thecvf.com/content/CVPR2025/html/Chang_Unified_Medical_Lesion_Segmentation_via_Self-referring_Indicator_CVPR_2025_paper.html)** — Uses self-referring indicators to unify segmentation across lesion types.

#### 🧫 Computational Pathology & Microscopy

- **[2DMamba: Efficient State Space Model for Image Representation with Applications on Giga-Pixel Whole Slide Image Classification](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_2DMamba_Efficient_State_Space_Model_for_Image_Representation_with_Applications_CVPR_2025_paper.html)** — Uses two-dimensional state-space representations for gigapixel whole-slide classification.
- **[Advancing Multiple Instance Learning with Continual Learning for Whole Slide Imaging](https://openaccess.thecvf.com/content/CVPR2025/html/Li_Advancing_Multiple_Instance_Learning_with_Continual_Learning_for_Whole_Slide_CVPR_2025_paper.html)** — Combines continual learning with whole-slide multiple-instance analysis.
- **[BioX-CPath: Biologically-driven Explainable Diagnostics for Multistain IHC Computational Pathology](https://openaccess.thecvf.com/content/CVPR2025/html/Gallagher-Syed_BioX-CPath_Biologically-driven_Explainable_Diagnostics_for_Multistain_IHC_Computational_Pathology_CVPR_2025_paper.html)** — Uses biological information for explainable multistain immunohistochemistry analysis.
- **[CPath-Omni: A Unified Multimodal Foundation Model for Patch and Whole Slide Image Analysis in Computational Pathology](https://openaccess.thecvf.com/content/CVPR2025/html/Sun_CPath-Omni_A_Unified_Multimodal_Foundation_Model_for_Patch_and_Whole_CVPR_2025_paper.html)** — Unifies patch and whole-slide image analysis in computational pathology.
- **[Fast and Accurate Gigapixel Pathological Image Classification with Hierarchical Distillation Multi-Instance Learning](https://openaccess.thecvf.com/content/CVPR2025/html/Dong_Fast_and_Accurate_Gigapixel_Pathological_Image_Classification_with_Hierarchical_Distillation_CVPR_2025_paper.html)** — Classifies gigapixel pathology images with hierarchical distillation and multiple-instance learning.
- **[FOCUS: Knowledge-enhanced Adaptive Visual Compression for Few-shot Whole Slide Image Classification](https://openaccess.thecvf.com/content/CVPR2025/html/Guo_FOCUS_Knowledge-enhanced_Adaptive_Visual_Compression_for_Few-shot_Whole_Slide_Image_CVPR_2025_paper.html)** — Compresses visual information adaptively using knowledge for few-shot whole-slide classification.
- **[HistoFS: Non-IID Histopathologic Whole Slide Image Classification via Federated Style Transfer with RoI-Preserving](https://openaccess.thecvf.com/content/CVPR2025/html/Raswa_HistoFS_Non-IID_Histopathologic_Whole_Slide_Image_Classification_via_Federated_Style_CVPR_2025_paper.html)** — Transfers stain styles across federated pathology clients while preserving regions of interest.
- **[Learning Heterogeneous Tissues with Mixture of Experts for Gigapixel Whole Slide Images](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_Learning_Heterogeneous_Tissues_with_Mixture_of_Experts_for_Gigapixel_Whole_CVPR_2025_paper.html)** — Uses expert mixtures to represent heterogeneous tissues in whole-slide images.
- **[M3amba: Memory Mamba is All You Need for Whole Slide Image Classification](https://openaccess.thecvf.com/content/CVPR2025/html/Zheng_M3amba_Memory_Mamba_is_All_You_Need_for_Whole_Slide_CVPR_2025_paper.html)** — Uses memory-augmented state-space modeling for whole-slide classification.
- **[MERGE: Multi-faceted Hierarchical Graph-based GNN for Gene Expression Prediction from Whole Slide Histopathology Images](https://openaccess.thecvf.com/content/CVPR2025/html/Ganguly_MERGE_Multi-faceted_Hierarchical_Graph-based_GNN_for_Gene_Expression_Prediction_from_CVPR_2025_paper.html)** — Predicts gene expression from whole-slide histology with hierarchical graph modeling.
- **[MExD: An Expert-Infused Diffusion Model for Whole-Slide Image Classification](https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_MExD_An_Expert-Infused_Diffusion_Model_for_Whole-Slide_Image_Classification_CVPR_2025_paper.html)** — Introduces expert information into diffusion-based whole-slide classification.
- **[MicroVQA: A Multimodal Reasoning Benchmark for Microscopy-Based Scientific Research](https://openaccess.thecvf.com/content/CVPR2025/html/Burgess_MicroVQA_A_Multimodal_Reasoning_Benchmark_for_Microscopy-Based_Scientific_Research_CVPR_2025_paper.html)** — Benchmarks visual question answering and reasoning over microscopy images.
- **[Prototype-Based Image Prompting for Weakly Supervised Histopathological Image Segmentation](https://openaccess.thecvf.com/content/CVPR2025/html/Tang_Prototype-Based_Image_Prompting_for_Weakly_Supervised_Histopathological_Image_Segmentation_CVPR_2025_paper.html)** — Uses prototype-based image prompts for weakly supervised histopathology segmentation.
- **[SlideChat: A Large Vision-Language Assistant for Whole-Slide Pathology Image Understanding](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_SlideChat_A_Large_Vision-Language_Assistant_for_Whole-Slide_Pathology_Image_Understanding_CVPR_2025_paper.html)** — Gigapixel-level conversational assistant for interactive whole-slide image analysis and pathology Q&A.
- **[TopoCellGen: Generating Histopathology Cell Topology with a Diffusion Model](https://openaccess.thecvf.com/content/CVPR2025/html/Xu_TopoCellGen_Generating_Histopathology_Cell_Topology_with_a_Diffusion_Model_CVPR_2025_paper.html)** — Generates histopathology cell topology with a diffusion model.
- **[V2V3D: View-to-View Denoised 3D Reconstruction for Light Field Microscopy](https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_V2V3D_View-to-View_Denoised_3D_Reconstruction_for_Light_Field_Microscopy_CVPR_2025_paper.html)** — Reconstructs three-dimensional volumes from light-field microscopy.
- **[Volume Tells: Dual Cycle-Consistent Diffusion for 3D Fluorescence Microscopy De-noising and Super-Resolution](https://openaccess.thecvf.com/content/CVPR2025/html/Li_Volume_Tells_Dual_Cycle-Consistent_Diffusion_for_3D_Fluorescence_Microscopy_De-noising_CVPR_2025_paper.html)** — Combines fluorescence microscopy denoising and super-resolution.
- **[WISE: A Framework for Gigapixel Whole-Slide-Image Lossless Compression](https://openaccess.thecvf.com/content/CVPR2025/html/Mao_WISE_A_Framework_for_Gigapixel_Whole-Slide-Image_Lossless_Compression_CVPR_2025_paper.html)** — Compresses gigapixel whole-slide images without loss of information.

#### 🤖 Foundation Models & Vision-Language

- **[Alignment, Mining and Fusion: Representation Alignment with Hard Negative Mining and Selective Knowledge Fusion for Medical Visual Question Answering](https://openaccess.thecvf.com/content/CVPR2025/html/Zou_Alignment_Mining_and_Fusion_Representation_Alignment_with_Hard_Negative_Mining_CVPR_2025_paper.html)** — Combines multi-level image-text alignment, hard negative mining, and gated knowledge fusion for medical VQA.
- **[BiomedCoOp: Learning to Prompt for Biomedical Vision-Language Models](https://openaccess.thecvf.com/content/CVPR2025/html/Koleilat_BiomedCoOp_Learning_to_Prompt_for_Biomedical_Vision-Language_Models_CVPR_2025_paper.html)** — Context optimization for prompt learning in biomedical vision-language models.
- **[BIOMEDICA: An Open Biomedical Image-Caption Archive, Dataset, and Vision-Language Models Derived from Scientific Literature](https://openaccess.thecvf.com/content/CVPR2025/html/Lozano_BIOMEDICA_An_Open_Biomedical_Image-Caption_Archive_Dataset_and_Vision-Language_Models_CVPR_2025_paper.html)** — Provides an open biomedical image-caption archive, dataset, and derived vision-language models.
- **[CheXWorld: Exploring Image World Modeling for Radiograph Representation Learning](https://openaccess.thecvf.com/content/CVPR2025/html/Yue_CheXWorld_Exploring_Image_World_Modeling_for_Radiograph_Representation_Learning_CVPR_2025_paper.html)** — Applies world modeling principles to chest X-ray pre-training, improving downstream diagnostic performance.
- **[CXPMRG-Bench: Pre-training and Benchmarking for X-ray Medical Report Generation on CheXpert Plus Dataset](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_CXPMRG-Bench_Pre-training_and_Benchmarking_for_X-ray_Medical_Report_Generation_on_CVPR_2025_paper.html)** — Provides pretraining data and benchmarks for chest X-ray report generation.
- **[DART: Disease-aware Image-Text Alignment and Self-correcting Re-alignment for Trustworthy Radiology Report Generation](https://openaccess.thecvf.com/content/CVPR2025/html/Park_DART_Disease-aware_Image-Text_Alignment_and_Self-correcting_Re-alignment_for_Trustworthy_Radiology_CVPR_2025_paper.html)** — Aligns disease-specific visual and textual evidence with self-correction for radiology reports.
- **[DiN: Diffusion Model for Robust Medical VQA with Semantic Noisy Labels](https://openaccess.thecvf.com/content/CVPR2025/html/Guo_DiN_Diffusion_Model_for_Robust_Medical_VQA_with_Semantic_Noisy_CVPR_2025_paper.html)** — Uses diffusion modeling to improve medical VQA under noisy semantic labels.
- **[EchoWorld: Learning Motion-Aware World Models for Echocardiography Probe Guidance](https://openaccess.thecvf.com/content/CVPR2025/html/Yue_EchoWorld_Learning_Motion-Aware_World_Models_for_Echocardiography_Probe_Guidance_CVPR_2025_paper.html)** — Learns motion-aware world models for echocardiography probe guidance.
- **[Enhanced Contrastive Learning with Multi-view Longitudinal Data for Chest X-ray Report Generation](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_Enhanced_Contrastive_Learning_with_Multi-view_Longitudinal_Data_for_Chest_X-ray_CVPR_2025_paper.html)** — Uses multiple views and longitudinal evidence for contrastive chest X-ray report generation.
- **[Enhancing SAM with Efficient Prompting and Preference Optimization for Semi-supervised Medical Image Segmentation](https://openaccess.thecvf.com/content/CVPR2025/html/Konwer_Enhancing_SAM_with_Efficient_Prompting_and_Preference_Optimization_for_Semi-supervised_CVPR_2025_paper.html)** — Combines efficient prompting and preference optimization for semi-supervised SAM adaptation.
- **[FactCheXcker: Mitigating Measurement Hallucinations in Chest X-ray Report Generation Models](https://openaccess.thecvf.com/content/CVPR2025/html/Heiman_FactCheXcker_Mitigating_Measurement_Hallucinations_in_Chest_X-ray_Report_Generation_Models_CVPR_2025_paper.html)** — Checks and reduces unsupported measurements in generated chest X-ray reports.
- **[MedUnifier: Unifying Vision-and-Language Pre-training on Medical Data with Vision Generation Task using Discrete Visual Representations](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_MedUnifier_Unifying_Vision-and-Language_Pre-training_on_Medical_Data_with_Vision_Generation_CVPR_2025_paper.html)** — Unifies medical vision-language pre-training with image generation using discrete visual representations.
- **[MIMO: A Medical Vision Language Model with Visual Referring Multimodal Input and Pixel Grounding Multimodal Output](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_MIMO_A_Medical_Vision_Language_Model_with_Visual_Referring_Multimodal_CVPR_2025_paper.html)** — Accepts visual references alongside text instructions and grounds generated medical terminology in image regions.
- **[Multi-modal Vision Pre-training for Medical Image Analysis](https://openaccess.thecvf.com/content/CVPR2025/html/Rui_Multi-modal_Vision_Pre-training_for_Medical_Image_Analysis_CVPR_2025_paper.html)** — BrainMVP learns cross-modality MRI representations through reconstruction, contrastive learning, and modality template distillation.
- **[VILA-M3: Enhancing Vision-Language Models with Medical Expert Knowledge](https://openaccess.thecvf.com/content/CVPR2025/html/Nath_VILA-M3_Enhancing_Vision-Language_Models_with_Medical_Expert_Knowledge_CVPR_2025_paper.html)** — Integrates structured medical expert knowledge into VLMs for clinical image understanding.
- **[VISTA3D: A Unified Segmentation Foundation Model For 3D Medical Imaging](https://openaccess.thecvf.com/content/CVPR2025/html/He_VISTA3D_A_Unified_Segmentation_Foundation_Model_For_3D_Medical_Imaging_CVPR_2025_paper.html)** — Provides a unified promptable foundation model for 3D medical segmentation.

#### 📋 Clinical NLP, EHR & Healthcare

- **[ASIGN: An Anatomy-aware Spatial Imputation Graphic Network for 3D Spatial Transcriptomics](https://openaccess.thecvf.com/content/CVPR2025/html/Zhu_ASIGN_An_Anatomy-aware_Spatial_Imputation_Graphic_Network_for_3D_Spatial_CVPR_2025_paper.html)** — Integrates histology with spatial transcriptomics in three dimensions.
- **[Bringing CLIP to the Clinic: Dynamic Soft Labels and Negation-Aware Learning for Medical Analysis](https://openaccess.thecvf.com/content/CVPR2025/html/Ko_Bringing_CLIP_to_the_Clinic_Dynamic_Soft_Labels_and_Negation-Aware_CVPR_2025_paper.html)** — Adapts image-language learning to clinical labels and negated findings.
- **[dFLMoE: Decentralized Federated Learning via Mixture of Experts for Medical Data Analysis](https://openaccess.thecvf.com/content/CVPR2025/html/Xie_dFLMoE_Decentralized_Federated_Learning_via_Mixture_of_Experts_for_Medical_CVPR_2025_paper.html)** — Combines decentralized federated learning with expert models for medical data analysis.
- **[Distilled Prompt Learning for Incomplete Multimodal Survival Prediction](https://openaccess.thecvf.com/content/CVPR2025/html/Xu_Distilled_Prompt_Learning_for_Incomplete_Multimodal_Survival_Prediction_CVPR_2025_paper.html)** — Uses multimodal prompts for survival prediction.
- **[Multi-modal Topology-embedded Graph Learning for Spatially Resolved Genes Prediction from Pathology Images with Prior Gene Similarity Information](https://openaccess.thecvf.com/content/CVPR2025/html/Shi_Multi-modal_Topology-embedded_Graph_Learning_for_Spatially_Resolved_Genes_Prediction_from_CVPR_2025_paper.html)** — Combines multimodal topology and gene-similarity priors to predict spatial gene expression from pathology.
- **[Multi-Resolution Pathology-Language Pre-training Model with Text-Guided Visual Representation](https://openaccess.thecvf.com/content/CVPR2025/html/Albastaki_Multi-Resolution_Pathology-Language_Pre-training_Model_with_Text-Guided_Visual_Representation_CVPR_2025_paper.html)** — Pretrains pathology-language representations across multiple visual resolutions.
- **[Remote Photoplethysmography in Real-World and Extreme Lighting Scenarios](https://openaccess.thecvf.com/content/CVPR2025/html/Shao_Remote_Photoplethysmography_in_Real-World_and_Extreme_Lighting_Scenarios_CVPR_2025_paper.html)** — Evaluates remote pulse measurement under difficult real-world illumination.
- **[Robust Multimodal Survival Prediction with Conditional Latent Differentiation Variational AutoEncoder](https://openaccess.thecvf.com/content/CVPR2025/html/Zhou_Robust_Multimodal_Survival_Prediction_with_Conditional_Latent_Differentiation_Variational_AutoEncoder_CVPR_2025_paper.html)** — Models multimodal survival prediction with conditional variational autoencoders.
- **[Unraveling Normal Anatomy via Fluid-Driven Anomaly Randomization](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_Unraveling_Normal_Anatomy_via_Fluid-Driven_Anomaly_Randomization_CVPR_2025_paper.html)** — Uses normal anatomy for medical anomaly detection.

#### 🧠 Neuroimaging, EEG & Brain AI

- **[Bridging the Vision-Brain Gap with an Uncertainty-Aware Blur Prior](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_Bridging_the_Vision-Brain_Gap_with_an_Uncertainty-Aware_Blur_Prior_CVPR_2025_paper.html)** — Uses blur priors for reconstructing visual content from brain activity.
- **[Incomplete Multi-modal Brain Tumor Segmentation via Learnable Sorting State Space Model](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_Incomplete_Multi-modal_Brain_Tumor_Segmentation_via_Learnable_Sorting_State_Space_CVPR_2025_paper.html)** — Models incomplete brain tumor modalities through learnable sorting and state-space representations.
- **[KMD: Koopman Multi-modality Decomposition for Generalized Brain Tumor Segmentation under Incomplete Modalities](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_KMD_Koopman_Multi-modality_Decomposition_for_Generalized_Brain_Tumor_Segmentation_under_CVPR_2025_paper.html)** — Decomposes multimodal information for generalizable brain tumor segmentation with missing inputs.
- **[Neuro-3D: Towards 3D Visual Decoding from EEG Signals](https://openaccess.thecvf.com/content/CVPR2025/html/Guo_Neuro-3D_Towards_3D_Visual_Decoding_from_EEG_Signals_CVPR_2025_paper.html)** — Decodes 3D visual information from EEG signals.
- **[NSD-Imagery: A Benchmark Dataset for Extending fMRI Vision Decoding Methods to Mental Imagery](https://openaccess.thecvf.com/content/CVPR2025/html/Kneeland_NSD-Imagery_A_Benchmark_Dataset_for_Extending_fMRI_Vision_Decoding_Methods_CVPR_2025_paper.html)** — Benchmarks the transfer of fMRI visual decoding to mental imagery.
- **[SuperLightNet: Lightweight Parameter Aggregation Network for Multimodal Brain Tumor Segmentation](https://openaccess.thecvf.com/content/CVPR2025/html/Yu_SuperLightNet_Lightweight_Parameter_Aggregation_Network_for_Multimodal_Brain_Tumor_Segmentation_CVPR_2025_paper.html)** — Aggregates parameters efficiently for multimodal brain tumor segmentation.

#### 🫀 Physiological Signals & Medical Time Series

- **[Electromyography-Informed Facial Expression Reconstruction for Physiological-Based Synthesis and Analysis](https://openaccess.thecvf.com/content/CVPR2025/html/Buchner_Electromyography-Informed_Facial_Expression_Reconstruction_for_Physiological-Based_Synthesis_and_Analysis_CVPR_2025_paper.html)** — Uses electromyography to reconstruct physiological aspects of facial expressions.

#### 🏥 Surgical AI

- **[MM-OR: A Large Multimodal Operating Room Dataset for Semantic Understanding of High-Intensity Surgical Environments](https://openaccess.thecvf.com/content/CVPR2025/html/Ozsoy_MM-OR_A_Large_Multimodal_Operating_Room_Dataset_for_Semantic_Understanding_CVPR_2025_paper.html)** — Provides multimodal operating-room recordings for understanding complex surgical environments.

---

### CVPR 2024

#### 🔬 Medical Imaging & Segmentation

- **[Adaptive Bidirectional Displacement for Semi-Supervised Medical Image Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/Chi_Adaptive_Bidirectional_Displacement_for_Semi-Supervised_Medical_Image_Segmentation_CVPR_2024_paper.html)** — Bidirectional pseudo-label consistency for semi-supervised 3D organ segmentation.
- **[Bi-level Learning of Task-Specific Decoders for Joint Registration and One-Shot Medical Image Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/Fan_Bi-level_Learning_of_Task-Specific_Decoders_for_Joint_Registration_and_One-Shot_CVPR_2024_paper.html)** — Jointly learns registration and one-shot medical segmentation through task-specific decoders.
- **[Clustering Propagation for Universal Medical Image Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/Ding_Clustering_Propagation_for_Universal_Medical_Image_Segmentation_CVPR_2024_paper.html)** — Uses clustering propagation for universal medical image segmentation.
- **[Constructing and Exploring Intermediate Domains in Mixed Domain Semi-supervised Medical Image Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/Ma_Constructing_and_Exploring_Intermediate_Domains_in_Mixed_Domain_Semi-supervised_Medical_CVPR_2024_paper.html)** — Intermediate domain construction to bridge labeled-unlabeled gaps in semi-supervised segmentation.
- **[Correlation-aware Coarse-to-fine MLPs for Deformable Medical Image Registration](https://openaccess.thecvf.com/content/CVPR2024/html/Meng_Correlation-aware_Coarse-to-fine_MLPs_for_Deformable_Medical_Image_Registration_CVPR_2024_paper.html)** ⭐ *Oral / Best Paper Candidate* — Lightweight MLP-based deformable registration using coarse-to-fine correlation features.
- **[CycleINR: Cycle Implicit Neural Representation for Arbitrary-Scale Volumetric Super-Resolution of Medical Data](https://openaccess.thecvf.com/content/CVPR2024/html/Fang_CycleINR_Cycle_Implicit_Neural_Representation_for_Arbitrary-Scale_Volumetric_Super-Resolution_of_CVPR_2024_paper.html)** — Uses cycle-consistent implicit neural representations for arbitrary-scale volumetric super-resolution of medical data.
- **[Data-Efficient Unsupervised Interpolation Without Any Intermediate Frame for 4D Medical Images](https://openaccess.thecvf.com/content/CVPR2024/html/Kim_Data-Efficient_Unsupervised_Interpolation_Without_Any_Intermediate_Frame_for_4D_Medical_CVPR_2024_paper.html)** — Interpolates four-dimensional medical images without intermediate-frame supervision.
- **[Diversified and Personalized Multi-rater Medical Image Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/Wu_Diversified_and_Personalized_Multi-rater_Medical_Image_Segmentation_CVPR_2024_paper.html)** — Models inter-annotator disagreement to produce personalized, diversified segmentation outputs.
- **[Each Test Image Deserves A Specific Prompt: Continual Test-Time Adaptation for 2D Medical Image Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/Chen_Each_Test_Image_Deserves_A_Specific_Prompt_Continual_Test-Time_Adaptation_CVPR_2024_paper.html)** — Instance-specific prompt generation for test-time adaptation without source data access.
- **[EMCAD: Efficient Multi-scale Convolutional Attention Decoding for Medical Image Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/Rahman_EMCAD_Efficient_Multi-scale_Convolutional_Attention_Decoding_for_Medical_Image_Segmentation_CVPR_2024_paper.html)** — Achieves state-of-the-art on 12 segmentation datasets with 79.4% fewer parameters via multi-scale convolutional attention decoding. *Rahman et al.*
- **[FocusMAE: Gallbladder Cancer Detection from Ultrasound Videos with Focused Masked Autoencoders](https://openaccess.thecvf.com/content/CVPR2024/html/Basu_FocusMAE_Gallbladder_Cancer_Detection_from_Ultrasound_Videos_with_Focused_Masked_CVPR_2024_paper.html)** — Masked autoencoding focused on lesion regions for cancer detection in ultrasound video.
- **[Fully Convolutional Slice-to-Volume Reconstruction for Single-Stack MRI](https://openaccess.thecvf.com/content/CVPR2024/html/Young_Fully_Convolutional_Slice-to-Volume_Reconstruction_for_Single-Stack_MRI_CVPR_2024_paper.html)** — End-to-end convolutional approach to MRI super-resolution slice-to-volume reconstruction.
- **[MAPSeg: Unified Unsupervised Domain Adaptation for Heterogeneous Medical Image Segmentation Based on 3D Masked Autoencoding and Pseudo-Labeling](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_MAPSeg_Unified_Unsupervised_Domain_Adaptation_for_Heterogeneous_Medical_Image_Segmentation_CVPR_2024_paper.html)** — Adapts heterogeneous medical segmentation with 3D masked autoencoding and pseudo-labeling.
- **[MedM2G: Unifying Medical Multi-Modal Generation via Cross-Guided Diffusion with Visual Invariant](https://openaccess.thecvf.com/content/CVPR2024/html/Zhan_MedM2G_Unifying_Medical_Multi-Modal_Generation_via_Cross-Guided_Diffusion_with_Visual_CVPR_2024_paper.html)** — Unified multi-modal medical image generation via cross-guided diffusion.
- **[Modality-agnostic Domain Generalizable Medical Image Segmentation by Multi-Frequency in Multi-Scale Attention](https://openaccess.thecvf.com/content/CVPR2024/html/Nam_Modality-agnostic_Domain_Generalizable_Medical_Image_Segmentation_by_Multi-Frequency_in_Multi-Scale_CVPR_2024_paper.html)** — Combines multi-frequency information with multi-scale attention for domain-generalizable medical segmentation.
- **[Modality-Agnostic Structural Image Representation Learning for Deformable Multi-Modality Medical Image Registration](https://openaccess.thecvf.com/content/CVPR2024/html/Mok_Modality-Agnostic_Structural_Image_Representation_Learning_for_Deformable_Multi-Modality_Medical_Image_CVPR_2024_paper.html)** — Unified structural representation for cross-modality deformable registration.
- **[One-Prompt to Segment All Medical Images](https://openaccess.thecvf.com/content/CVPR2024/html/Wu_One-Prompt_to_Segment_All_Medical_Images_CVPR_2024_paper.html)** — Universal segmentation paradigm trained on 64 datasets; segments unseen modalities with a single prompted example. *Wu & Xu*
- **[PH-Net: Semi-Supervised Breast Lesion Segmentation via Patch-wise Hardness](https://openaccess.thecvf.com/content/CVPR2024/html/Jiang_PH-Net_Semi-Supervised_Breast_Lesion_Segmentation_via_Patch-wise_Hardness_CVPR_2024_paper.html)** — Adapts semi-supervised breast lesion segmentation to patch difficulty.
- **[Progressive Divide-and-Conquer via Subsampling Decomposition for Accelerated MRI](https://openaccess.thecvf.com/content/CVPR2024/html/Wang_Progressive_Divide-and-Conquer_via_Subsampling_Decomposition_for_Accelerated_MRI_CVPR_2024_paper.html)** — Accelerates MRI reconstruction through progressive decomposition of subsampling patterns.
- **[PrPSeg: Universal Proposition Learning for Panoramic Renal Pathology Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/Deng_PrPSeg_Universal_Proposition_Learning_for_Panoramic_Renal_Pathology_Segmentation_CVPR_2024_paper.html)** — Proposition-based universal framework for panoramic renal pathology segmentation.
- **[QN-Mixer: A Quasi-Newton MLP-Mixer Model for Sparse-View CT Reconstruction](https://openaccess.thecvf.com/content/CVPR2024/html/Ayad_QN-Mixer_A_Quasi-Newton_MLP-Mixer_Model_for_Sparse-View_CT_Reconstruction_CVPR_2024_paper.html)** — Quasi-Newton optimization embedded in an MLP-Mixer for sparse-view CT reconstruction.
- **[Rethinking Diffusion Model for Multi-Contrast MRI Super-Resolution](https://openaccess.thecvf.com/content/CVPR2024/html/Li_Rethinking_Diffusion_Model_for_Multi-Contrast_MRI_Super-Resolution_CVPR_2024_paper.html)** — Studies diffusion-based multicontrast MRI super-resolution.
- **[Structure-Aware Sparse-View X-ray 3D Reconstruction](https://openaccess.thecvf.com/content/CVPR2024/html/Cai_Structure-Aware_Sparse-View_X-ray_3D_Reconstruction_CVPR_2024_paper.html)** — Structure-aware priors for high-quality 3D X-ray reconstruction from sparse views.
- **[Systematic Comparison of Semi-supervised and Self-supervised Learning for Medical Image Classification](https://openaccess.thecvf.com/content/CVPR2024/html/Huang_Systematic_Comparison_of_Semi-supervised_and_Self-supervised_Learning_for_Medical_Image_CVPR_2024_paper.html)** — Compares semi-supervised and self-supervised learning under medical image classification settings.
- **[Teeth-SEG: An Efficient Instance Segmentation Framework for Orthodontic Treatment based on Multi-Scale Aggregation and Anthropic Prior Knowledge](https://openaccess.thecvf.com/content/CVPR2024/html/Zou_Teeth-SEG_An_Efficient_Instance_Segmentation_Framework_for_Orthodontic_Treatment_based_CVPR_2024_paper.html)** — Segments teeth for orthodontic treatment with multiscale features and anatomical priors.
- **[Think Twice Before Selection: Federated Evidential Active Learning for Medical Image Analysis with Domain Shifts](https://openaccess.thecvf.com/content/CVPR2024/html/Chen_Think_Twice_Before_Selection_Federated_Evidential_Active_Learning_for_Medical_CVPR_2024_paper.html)** — Selects medical annotations through federated evidential active learning under domain shifts.
- **[ToNNO: Tomographic Reconstruction of a Neural Network's Output for Weakly Supervised Segmentation of 3D Medical Images](https://openaccess.thecvf.com/content/CVPR2024/html/Schmidt-Mengin_ToNNO_Tomographic_Reconstruction_of_a_Neural_Networks_Output_for_Weakly_CVPR_2024_paper.html)** — Uses tomographic reconstruction of neural predictions for weakly supervised 3D segmentation.
- **[Towards Generalizable Tumor Synthesis](https://openaccess.thecvf.com/content/CVPR2024/html/Chen_Towards_Generalizable_Tumor_Synthesis_CVPR_2024_paper.html)** — Generalizable framework for synthesizing realistic tumors of diverse types and sizes for data augmentation.
- **[Training Like a Medical Resident: Context-Prior Learning Toward Universal Medical Image Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/Gao_Training_Like_a_Medical_Resident_Context-Prior_Learning_Toward_Universal_Medical_CVPR_2024_paper.html)** — Uses context-prior learning for universal medical image segmentation.
- **[Tyche: Stochastic In-Context Learning for Medical Image Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/Rakic_Tyche_Stochastic_In-Context_Learning_for_Medical_Image_Segmentation_CVPR_2024_paper.html)** — Produces stochastic in-context predictions for medical image segmentation.
- **[Versatile Medical Image Segmentation Learned from Multi-Source Datasets via Model Self-Disambiguation](https://openaccess.thecvf.com/content/CVPR2024/html/Chen_Versatile_Medical_Image_Segmentation_Learned_from_Multi-Source_Datasets_via_Model_CVPR_2024_paper.html)** — Uses model self-disambiguation to learn medical segmentation from multiple datasets.
- **[ZePT: Zero-Shot Pan-Tumor Segmentation via Query-Disentangling and Self-Prompting](https://openaccess.thecvf.com/content/CVPR2024/html/Jiang_ZePT_Zero-Shot_Pan-Tumor_Segmentation_via_Query-Disentangling_and_Self-Prompting_CVPR_2024_paper.html)** — Zero-shot tumor segmentation across cancer types through query disentangling and self-prompting.

#### 🧫 Computational Pathology & Microscopy

- **[A Unified Framework for Microscopy Defocus Deblur with Multi-Pyramid Transformer and Contrastive Learning](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_A_Unified_Framework_for_Microscopy_Defocus_Deblur_with_Multi-Pyramid_Transformer_CVPR_2024_paper.html)** — Removes defocus blur from microscopy images.
- **[ChAda-ViT : Channel Adaptive Attention for Joint Representation Learning of Heterogeneous Microscopy Images](https://openaccess.thecvf.com/content/CVPR2024/html/Bourriez_ChAda-ViT__Channel_Adaptive_Attention_for_Joint_Representation_Learning_of_CVPR_2024_paper.html)** — Channel-adaptive ViT for joint representation learning across multi-channel microscopy images.
- **[CPLIP: Zero-Shot Learning for Histopathology with Comprehensive Vision-Language Alignment](https://openaccess.thecvf.com/content/CVPR2024/html/Javed_CPLIP_Zero-Shot_Learning_for_Histopathology_with_Comprehensive_Vision-Language_Alignment_CVPR_2024_paper.html)** — Aligns pathology images and language comprehensively for zero-shot transfer.
- **[Dynamic Graph Representation with Knowledge-aware Attention for Histopathology Whole Slide Image Analysis](https://openaccess.thecvf.com/content/CVPR2024/html/Li_Dynamic_Graph_Representation_with_Knowledge-aware_Attention_for_Histopathology_Whole_Slide_CVPR_2024_paper.html)** — Combines dynamic graphs and medical knowledge for whole-slide pathology analysis.
- **[Dynamic Policy-Driven Adaptive Multi-Instance Learning for Whole Slide Image Classification](https://openaccess.thecvf.com/content/CVPR2024/html/Zheng_Dynamic_Policy-Driven_Adaptive_Multi-Instance_Learning_for_Whole_Slide_Image_Classification_CVPR_2024_paper.html)** — Learns adaptive instance-selection policies for whole-slide classification.
- **[Feature Re-Embedding: Towards Foundation Model-Level Performance in Computational Pathology](https://openaccess.thecvf.com/content/CVPR2024/html/Tang_Feature_Re-Embedding_Towards_Foundation_Model-Level_Performance_in_Computational_Pathology_CVPR_2024_paper.html)** — Re-embedding strategy that lifts conventional pathology features to foundation-model-level performance.
- **[Generalizable Whole Slide Image Classification with Fine-Grained Visual-Semantic Interaction](https://openaccess.thecvf.com/content/CVPR2024/html/Li_Generalizable_Whole_Slide_Image_Classification_with_Fine-Grained_Visual-Semantic_Interaction_CVPR_2024_paper.html)** — Fine-grained vision-language interaction for generalizable whole-slide image classification.
- **[Incremental Nuclei Segmentation from Histopathological Images via Future-class Awareness and Compatibility-inspired Distillation](https://openaccess.thecvf.com/content/CVPR2024/html/Wang_Incremental_Nuclei_Segmentation_from_Histopathological_Images_via_Future-class_Awareness_and_CVPR_2024_paper.html)** — Recognizes additional nuclei classes through future-class awareness and compatible distillation.
- **[Masked Autoencoders for Microscopy are Scalable Learners of Cellular Biology](https://openaccess.thecvf.com/content/CVPR2024/html/Kraus_Masked_Autoencoders_for_Microscopy_are_Scalable_Learners_of_Cellular_Biology_CVPR_2024_paper.html)** — Pre-trains masked autoencoders on biomedical microscopy images.
- **[MicroDiffusion: Implicit Representation-Guided Diffusion for 3D Reconstruction from Limited 2D Microscopy Projections](https://openaccess.thecvf.com/content/CVPR2024/html/Hui_MicroDiffusion_Implicit_Representation-Guided_Diffusion_for_3D_Reconstruction_from_Limited_2D_CVPR_2024_paper.html)** — Reconstructs microscopy images with diffusion models.
- **[Morphological Prototyping for Unsupervised Slide Representation Learning in Computational Pathology](https://openaccess.thecvf.com/content/CVPR2024/html/Song_Morphological_Prototyping_for_Unsupervised_Slide_Representation_Learning_in_Computational_Pathology_CVPR_2024_paper.html)** — Uses morphological prototypes to learn slide representations without labels.
- **[Quilt-LLaVA: Visual Instruction Tuning by Extracting Localized Narratives from Open-Source Histopathology Videos](https://openaccess.thecvf.com/content/CVPR2024/html/Seyfioglu_Quilt-LLaVA_Visual_Instruction_Tuning_by_Extracting_Localized_Narratives_from_Open-Source_CVPR_2024_paper.html)** — Tunes a pathology assistant using localized image-language narratives extracted from educational videos.
- **[SI-MIL: Taming Deep MIL for Self-Interpretability in Gigapixel Histopathology](https://openaccess.thecvf.com/content/CVPR2024/html/Kapse_SI-MIL_Taming_Deep_MIL_for_Self-Interpretability_in_Gigapixel_Histopathology_CVPR_2024_paper.html)** — Self-interpretable MIL framework that identifies diagnostically predictive regions in WSIs.
- **[Transcriptomics-guided Slide Representation Learning in Computational Pathology](https://openaccess.thecvf.com/content/CVPR2024/html/Jaume_Transcriptomics-guided_Slide_Representation_Learning_in_Computational_Pathology_CVPR_2024_paper.html)** — Gene expression data as supervision signal for learning richer pathology slide representations.
- **[Tumor Micro-environment Interactions Guided Graph Learning for Survival Analysis of Human Cancers from Whole-slide Pathological Images](https://openaccess.thecvf.com/content/CVPR2024/html/Shao_Tumor_Micro-environment_Interactions_Guided_Graph_Learning_for_Survival_Analysis_of_CVPR_2024_paper.html)** — Models tumor microenvironment interactions for whole-slide-based cancer survival prediction.
- **[ViLa-MIL: Dual-scale Vision-Language Multiple Instance Learning for Whole Slide Image Classification](https://openaccess.thecvf.com/content/CVPR2024/html/Shi_ViLa-MIL_Dual-scale_Vision-Language_Multiple_Instance_Learning_for_Whole_Slide_Image_CVPR_2024_paper.html)** — Combines dual-scale vision-language information in whole-slide multiple-instance classification.

#### 🤖 Foundation Models & Vision-Language

- **[Adapting Visual-Language Models for Generalizable Anomaly Detection in Medical Images](https://openaccess.thecvf.com/content/CVPR2024/html/Huang_Adapting_Visual-Language_Models_for_Generalizable_Anomaly_Detection_in_Medical_Images_CVPR_2024_paper.html)** — Adapts vision-language representations for generalizable medical anomaly detection.
- **[AHIVE: Anatomy-aware Hierarchical Vision Encoding for Interactive Radiology Report Retrieval](https://openaccess.thecvf.com/content/CVPR2024/html/Yan_AHIVE_Anatomy-aware_Hierarchical_Vision_Encoding_for_Interactive_Radiology_Report_Retrieval_CVPR_2024_paper.html)** — Encodes radiological anatomy hierarchically for interactive report retrieval.
- **[Bootstrapping Chest CT Image Understanding by Distilling Knowledge from X-ray Expert Models](https://openaccess.thecvf.com/content/CVPR2024/html/Cao_Bootstrapping_Chest_CT_Image_Understanding_by_Distilling_Knowledge_from_X-ray_CVPR_2024_paper.html)** — Cross-modality knowledge distillation from 2D X-ray models to 3D CT image understanding.
- **[CARZero: Cross-Attention Alignment for Radiology Zero-Shot Classification](https://openaccess.thecvf.com/content/CVPR2024/html/Lai_CARZero_Cross-Attention_Alignment_for_Radiology_Zero-Shot_Classification_CVPR_2024_paper.html)** — Cross-attention mechanism for zero-shot radiology classification using report-image alignment.
- **[Continual Self-supervised Learning: Towards Universal Multi-modal Medical Data Representation Learning](https://openaccess.thecvf.com/content/CVPR2024/html/Ye_Continual_Self-supervised_Learning_Towards_Universal_Multi-modal_Medical_Data_Representation_Learning_CVPR_2024_paper.html)** ⭐ *Highlight* — Continual SSL framework for multi-modal medical pre-training without catastrophic forgetting.
- **[Decomposing Disease Descriptions for Enhanced Pathology Detection: A Multi-Aspect Vision-Language Pre-training Framework](https://openaccess.thecvf.com/content/CVPR2024/html/Phan_Decomposing_Disease_Descriptions_for_Enhanced_Pathology_Detection_A_Multi-Aspect_Vision-Language_CVPR_2024_paper.html)** — Aspect-decomposed VL pre-training for fine-grained pathology detection in radiology.
- **[FairCLIP: Harnessing Fairness in Vision-Language Learning](https://openaccess.thecvf.com/content/CVPR2024/html/Luo_FairCLIP_Harnessing_Fairness_in_Vision-Language_Learning_CVPR_2024_paper.html)** — Studies demographic fairness in medical vision-language learning.
- **[Instance-level Expert Knowledge and Aggregate Discriminative Attention for Radiology Report Generation](https://openaccess.thecvf.com/content/CVPR2024/html/Bu_Instance-level_Expert_Knowledge_and_Aggregate_Discriminative_Attention_for_Radiology_Report_CVPR_2024_paper.html)** — Combines instance-level expert knowledge with discriminative attention for radiology reports.
- **[Low-Rank Knowledge Decomposition for Medical Foundation Models](https://openaccess.thecvf.com/content/CVPR2024/html/Zhou_Low-Rank_Knowledge_Decomposition_for_Medical_Foundation_Models_CVPR_2024_paper.html)** — Low-rank adapter decomposition for efficient knowledge transfer from foundation models to medical tasks.
- **[MemSAM: Taming Segment Anything Model for Echocardiography Video Segmentation](https://openaccess.thecvf.com/content/CVPR2024/html/Deng_MemSAM_Taming_Segment_Anything_Model_for_Echocardiography_Video_Segmentation_CVPR_2024_paper.html)** — Uses memory to adapt SAM to echocardiography video segmentation.
- **[MLIP: Enhancing Medical Visual Representation with Divergence Encoder and Knowledge-guided Contrastive Learning](https://openaccess.thecvf.com/content/CVPR2024/html/Li_MLIP_Enhancing_Medical_Visual_Representation_with_Divergence_Encoder_and_Knowledge-guided_CVPR_2024_paper.html)** — Combines a divergence encoder with knowledge-guided contrastive learning for medical visual representations.
- **[OmniMedVQA: A New Large-Scale Comprehensive Evaluation Benchmark for Medical LVLM](https://openaccess.thecvf.com/content/CVPR2024/html/Hu_OmniMedVQA_A_New_Large-Scale_Comprehensive_Evaluation_Benchmark_for_Medical_LVLM_CVPR_2024_paper.html)** — Comprehensive VQA benchmark spanning 12 medical imaging modalities for evaluating medical LVLMs.
- **[PairAug: What Can Augmented Image-Text Pairs Do for Radiology?](https://openaccess.thecvf.com/content/CVPR2024/html/Xie_PairAug_What_Can_Augmented_Image-Text_Pairs_Do_for_Radiology_CVPR_2024_paper.html)** — Synthesized image-text pair augmentation for radiology vision-language pre-training.
- **[Prompting Vision Foundation Models for Pathology Image Analysis](https://openaccess.thecvf.com/content/CVPR2024/html/Yin_Prompting_Vision_Foundation_Models_for_Pathology_Image_Analysis_CVPR_2024_paper.html)** — Prompts visual foundation models for pathology analysis.
- **[Unleashing the Potential of SAM for Medical Adaptation via Hierarchical Decoding](https://openaccess.thecvf.com/content/CVPR2024/html/Cheng_Unleashing_the_Potential_of_SAM_for_Medical_Adaptation_via_Hierarchical_CVPR_2024_paper.html)** — Adapts SAM to medical images through hierarchical decoding.
- **[VoCo: A Simple-yet-Effective Volume Contrastive Learning Framework for 3D Medical Image Analysis](https://openaccess.thecvf.com/content/CVPR2024/html/Wu_VoCo_A_Simple-yet-Effective_Volume_Contrastive_Learning_Framework_for_3D_Medical_CVPR_2024_paper.html)** — Volume-level contrastive pre-training enabling strong generalization across CT organ segmentation tasks.

#### 📋 Clinical NLP, EHR & Healthcare

- **[HIT: Estimating Internal Human Implicit Tissues from the Body Surface](https://openaccess.thecvf.com/content/CVPR2024/html/Keller_HIT_Estimating_Internal_Human_Implicit_Tissues_from_the_Body_Surface_CVPR_2024_paper.html)** — Models internal human tissues with an implicit anatomical representation.
- **[M3-UDA: A New Benchmark for Unsupervised Domain Adaptive Fetal Cardiac Structure Detection](https://openaccess.thecvf.com/content/CVPR2024/html/Pu_M3-UDA_A_New_Benchmark_for_Unsupervised_Domain_Adaptive_Fetal_Cardiac_CVPR_2024_paper.html)** — Benchmarks unsupervised adaptation of fetal cardiac structure detection.
- **[Modeling Dense Multimodal Interactions Between Biological Pathways and Histology for Survival Prediction](https://openaccess.thecvf.com/content/CVPR2024/html/Jaume_Modeling_Dense_Multimodal_Interactions_Between_Biological_Pathways_and_Histology_for_CVPR_2024_paper.html)** — Models interactions between biological pathways and histology for survival prediction.
- **[OpticalDR: A Deep Optical Imaging Model for Privacy-Protective Depression Recognition](https://openaccess.thecvf.com/content/CVPR2024/html/Pan_OpticalDR_A_Deep_Optical_Imaging_Model_for_Privacy-Protective_Depression_Recognition_CVPR_2024_paper.html)** — Uses optical image transformations for privacy-preserving depression recognition.
- **[Rotation-Agnostic Image Representation Learning for Digital Pathology](https://openaccess.thecvf.com/content/CVPR2024/html/Alfasly_Rotation-Agnostic_Image_Representation_Learning_for_Digital_Pathology_CVPR_2024_paper.html)** — Learns digital pathology representations robust to image rotation.
- **[Seeing Unseen: Discover Novel Biomedical Concepts via Geometry-Constrained Probabilistic Modeling](https://openaccess.thecvf.com/content/CVPR2024/html/Fan_Seeing_Unseen_Discover_Novel_Biomedical_Concepts_via_Geometry-Constrained_Probabilistic_Modeling_CVPR_2024_paper.html)** — Represents novel biomedical concepts geometrically.
- **[Virtual Immunohistochemistry Staining for Histological Images Assisted by Weakly-supervised Learning](https://openaccess.thecvf.com/content/CVPR2024/html/Li_Virtual_Immunohistochemistry_Staining_for_Histological_Images_Assisted_by_Weakly-supervised_Learning_CVPR_2024_paper.html)** — Synthesizes immunohistochemical staining from histology with weak supervision.
- **[XFibrosis: Explicit Vessel-Fiber Modeling for Fibrosis Staging from Liver Pathology Images](https://openaccess.thecvf.com/content/CVPR2024/html/Yin_XFibrosis_Explicit_Vessel-Fiber_Modeling_for_Fibrosis_Staging_from_Liver_Pathology_CVPR_2024_paper.html)** — Models vessel-fiber relationships for liver fibrosis staging from pathology.

#### 🧠 Neuroimaging, EEG & Brain AI

- **[MindBridge: A Cross-Subject Brain Decoding Framework](https://openaccess.thecvf.com/content/CVPR2024/html/Wang_MindBridge_A_Cross-Subject_Brain_Decoding_Framework_CVPR_2024_paper.html)** — Transfers brain decoding across subjects.
- **[Psychometry: An Omnifit Model for Image Reconstruction from Human Brain Activity](https://openaccess.thecvf.com/content/CVPR2024/html/Quan_Psychometry_An_Omnifit_Model_for_Image_Reconstruction_from_Human_Brain_CVPR_2024_paper.html)** — Reconstructs images from human brain recordings with a shared decoding model.
- **[TULIP: Multi-camera 3D Precision Assessment of Parkinson's Disease](https://openaccess.thecvf.com/content/CVPR2024/html/Kim_TULIP_Multi-camera_3D_Precision_Assessment_of_Parkinsons_Disease_CVPR_2024_paper.html)** — Measures Parkinson's-related movements with multiple cameras and 3D analysis.

#### 🫀 Physiological Signals & Medical Time Series

- **[SleepVST: Sleep Staging from Near-Infrared Video Signals using Pre-Trained Transformers](https://openaccess.thecvf.com/content/CVPR2024/html/Carter_SleepVST_Sleep_Staging_from_Near-Infrared_Video_Signals_using_Pre-Trained_Transformers_CVPR_2024_paper.html)** — Uses pretrained transformers to infer sleep stages from near-infrared video.

#### 🏥 Surgical AI

- **[Intraoperative 2D/3D Image Registration via Differentiable X-ray Rendering](https://openaccess.thecvf.com/content/CVPR2024/html/Gopalakrishnan_Intraoperative_2D3D_Image_Registration_via_Differentiable_X-ray_Rendering_CVPR_2024_paper.html)** — DiffPose combines patient-specific simulation with differentiable rendering to align intraoperative X-rays with preoperative CT without landmark annotations.

---

### CVPR 2023

#### 🔬 Medical Imaging & Segmentation

- **[Ambiguous Medical Image Segmentation Using Diffusion Models](https://openaccess.thecvf.com/content/CVPR2023/html/Rahman_Ambiguous_Medical_Image_Segmentation_Using_Diffusion_Models_CVPR_2023_paper.html)** — Single diffusion model that produces multiple plausible segmentation variants by learning a distribution over annotator group insights, validated on CT, ultrasound, and MRI.
- **[Bidirectional Copy-Paste for Semi-Supervised Medical Image Segmentation](https://openaccess.thecvf.com/content/CVPR2023/html/Bai_Bidirectional_Copy-Paste_for_Semi-Supervised_Medical_Image_Segmentation_CVPR_2023_paper.html)** — Bidirectional copy-paste between labeled and unlabeled volumes in a Mean Teacher framework, achieving SOTA on LA and Pancreas-CT semi-supervised benchmarks. *Bai et al.*
- **[Devil Is in the Queries: Advancing Mask Transformers for Real-World Medical Image Segmentation and Out-of-Distribution Localization](https://openaccess.thecvf.com/content/CVPR2023/html/Yuan_Devil_Is_in_the_Queries_Advancing_Mask_Transformers_for_Real-World_CVPR_2023_paper.html)** — Adapts mask-transformer queries for medical segmentation and out-of-distribution localization.
- **[Directional Connectivity-Based Segmentation of Medical Images](https://openaccess.thecvf.com/content/CVPR2023/html/Yang_Directional_Connectivity-Based_Segmentation_of_Medical_Images_CVPR_2023_paper.html)** — Uses directional connectivity to improve medical image segmentation.
- **[Fair Federated Medical Image Segmentation via Client Contribution Estimation](https://openaccess.thecvf.com/content/CVPR2023/html/Jiang_Fair_Federated_Medical_Image_Segmentation_via_Client_Contribution_Estimation_CVPR_2023_paper.html)** — Estimates clients' contributions to improve fairness in federated medical segmentation.
- **[Label-Free Liver Tumor Segmentation](https://openaccess.thecvf.com/content/CVPR2023/html/Hu_Label-Free_Liver_Tumor_Segmentation_CVPR_2023_paper.html)** — Synthesizes realistic pseudo-tumors in healthy CT scans to train a segmentation model without any real tumor annotations, outperforming fully supervised baselines.
- **[Learning Federated Visual Prompt in Null Space for MRI Reconstruction](https://openaccess.thecvf.com/content/CVPR2023/html/Feng_Learning_Federated_Visual_Prompt_in_Null_Space_for_MRI_Reconstruction_CVPR_2023_paper.html)** — Learns federated visual prompts for MRI reconstruction in a null-space formulation.
- **[MagicNet: Semi-Supervised Multi-Organ Segmentation via Magic-Cube Partition and Recovery](https://openaccess.thecvf.com/content/CVPR2023/html/Chen_MagicNet_Semi-Supervised_Multi-Organ_Segmentation_via_Magic-Cube_Partition_and_Recovery_CVPR_2023_paper.html)** — Partitions and restores volumetric regions for semi-supervised multi-organ segmentation.
- **[MCF: Mutual Correction Framework for Semi-Supervised Medical Image Segmentation](https://openaccess.thecvf.com/content/CVPR2023/html/Wang_MCF_Mutual_Correction_Framework_for_Semi-Supervised_Medical_Image_Segmentation_CVPR_2023_paper.html)** — Two-subnet mutual correction with contrastive difference review and dynamic competitive pseudo-label generation to reduce cognitive bias in semi-supervised segmentation.
- **[Orthogonal Annotation Benefits Barely-Supervised Medical Image Segmentation](https://openaccess.thecvf.com/content/CVPR2023/html/Cai_Orthogonal_Annotation_Benefits_Barely-Supervised_Medical_Image_Segmentation_CVPR_2023_paper.html)** — Uses orthogonal views to improve medical segmentation with very limited annotation.
- **[PEFAT: Boosting Semi-Supervised Medical Image Classification via Pseudo-Loss Estimation and Feature Adversarial Training](https://openaccess.thecvf.com/content/CVPR2023/html/Zeng_PEFAT_Boosting_Semi-Supervised_Medical_Image_Classification_via_Pseudo-Loss_Estimation_and_CVPR_2023_paper.html)** — Estimates pseudo-label losses and uses adversarial features for semi-supervised medical classification.
- **[Pseudo-Label Guided Contrastive Learning for Semi-Supervised Medical Image Segmentation](https://openaccess.thecvf.com/content/CVPR2023/html/Basak_Pseudo-Label_Guided_Contrastive_Learning_for_Semi-Supervised_Medical_Image_Segmentation_CVPR_2023_paper.html)** — Uses pseudo-label-guided contrastive objectives for semi-supervised medical segmentation.
- **[Rethinking Few-Shot Medical Segmentation: A Vector Quantization View](https://openaccess.thecvf.com/content/CVPR2023/html/Huang_Rethinking_Few-Shot_Medical_Segmentation_A_Vector_Quantization_View_CVPR_2023_paper.html)** — Studies few-shot medical segmentation through vector quantization.
- **[SDC-UDA: Volumetric Unsupervised Domain Adaptation Framework for Slice-Direction Continuous Cross-Modality Medical Image Segmentation](https://openaccess.thecvf.com/content/CVPR2023/html/Shin_SDC-UDA_Volumetric_Unsupervised_Domain_Adaptation_Framework_for_Slice-Direction_Continuous_Cross-Modality_CVPR_2023_paper.html)** — Preserves slice-direction continuity during volumetric cross-modality adaptation.

#### 🧫 Computational Pathology & Microscopy

- **[A Soma Segmentation Benchmark in Full Adult Fly Brain](https://openaccess.thecvf.com/content/CVPR2023/html/Liu_A_Soma_Segmentation_Benchmark_in_Full_Adult_Fly_Brain_CVPR_2023_paper.html)** — Segments neuronal somata in fly microscopy data.
- **[DoNet: Deep De-Overlapping Network for Cytology Instance Segmentation](https://openaccess.thecvf.com/content/CVPR2023/html/Jiang_DoNet_Deep_De-Overlapping_Network_for_Cytology_Instance_Segmentation_CVPR_2023_paper.html)** — Decompose-and-reconstruct strategy separates overlapping cell instances in cytology images for accurate instance segmentation.
- **[Histopathology Whole Slide Image Analysis With Heterogeneous Graph Representation Learning](https://openaccess.thecvf.com/content/CVPR2023/html/Chan_Histopathology_Whole_Slide_Image_Analysis_With_Heterogeneous_Graph_Representation_Learning_CVPR_2023_paper.html)** — Represents heterogeneous relationships in whole-slide pathology graphs.
- **[Interventional Bag Multi-Instance Learning on Whole-Slide Pathological Images](https://openaccess.thecvf.com/content/CVPR2023/html/Lin_Interventional_Bag_Multi-Instance_Learning_on_Whole-Slide_Pathological_Images_CVPR_2023_paper.html)** — Causal intervention via do-calculus removes confounding in bag-level MIL for more robust WSI classification.
- **[OCELOT: Overlapped Cell on Tissue Dataset for Histopathology](https://openaccess.thecvf.com/content/CVPR2023/html/Ryu_OCELOT_Overlapped_Cell_on_Tissue_Dataset_for_Histopathology_CVPR_2023_paper.html)** — Provides overlapping cell and tissue annotations for histopathology.
- **[RankMix: Data Augmentation for Weakly Supervised Learning of Classifying Whole Slide Images With Diverse Sizes and Imbalanced Categories](https://openaccess.thecvf.com/content/CVPR2023/html/Chen_RankMix_Data_Augmentation_for_Weakly_Supervised_Learning_of_Classifying_Whole_CVPR_2023_paper.html)** — Augments whole-slide features across image sizes and imbalanced categories.
- **[Task-Specific Fine-Tuning via Variational Information Bottleneck for Weakly-Supervised Pathology Whole Slide Image Classification](https://openaccess.thecvf.com/content/CVPR2023/html/Li_Task-Specific_Fine-Tuning_via_Variational_Information_Bottleneck_for_Weakly-Supervised_Pathology_Whole_CVPR_2023_paper.html)** — VIB-based fine-tuning compresses WSI representations to task-relevant bottlenecks, improving weakly supervised classification with fewer labeled slides.
- **[Topology-Guided Multi-Class Cell Context Generation for Digital Pathology](https://openaccess.thecvf.com/content/CVPR2023/html/Abousamra_Topology-Guided_Multi-Class_Cell_Context_Generation_for_Digital_Pathology_CVPR_2023_paper.html)** — Topology-aware generation model creates realistic multi-class cell spatial layouts for data augmentation in computational pathology.
- **[Visual Language Pretrained Multiple Instance Zero-Shot Transfer for Histopathology Images](https://openaccess.thecvf.com/content/CVPR2023/html/Lu_Visual_Language_Pretrained_Multiple_Instance_Zero-Shot_Transfer_for_Histopathology_Images_CVPR_2023_paper.html)** — MI-Zero reformulates zero-shot transfer under MIL for gigapixel WSIs, achieving 70.2% average accuracy on three cancer subtyping tasks without task-specific labels. *Lu et al., Mahmood Lab*
- **[Weakly Supervised Segmentation With Point Annotations for Histopathology Images via Contrast-Based Variational Model](https://openaccess.thecvf.com/content/CVPR2023/html/Zhang_Weakly_Supervised_Segmentation_With_Point_Annotations_for_Histopathology_Images_via_CVPR_2023_paper.html)** — Segments histopathology images from point annotations through contrast-based variational modeling.

#### 🤖 Foundation Models & Vision-Language

- **[Geometric Visual Similarity Learning in 3D Medical Image Self-Supervised Pre-Training](https://openaccess.thecvf.com/content/CVPR2023/html/He_Geometric_Visual_Similarity_Learning_in_3D_Medical_Image_Self-Supervised_Pre-Training_CVPR_2023_paper.html)** — Geometric similarity as a self-supervised signal for pre-training 3D medical image encoders, improving transfer to organ segmentation tasks.
- **[Hierarchical Discriminative Learning Improves Visual Representations of Biomedical Microscopy](https://openaccess.thecvf.com/content/CVPR2023/html/Jiang_Hierarchical_Discriminative_Learning_Improves_Visual_Representations_of_Biomedical_Microscopy_CVPR_2023_paper.html)** — Hierarchical contrastive learning framework that aligns microscopy image representations at multiple granularities for richer visual pre-training.
- **[Interactive and Explainable Region-Guided Radiology Report Generation](https://openaccess.thecvf.com/content/CVPR2023/html/Tanida_Interactive_and_Explainable_Region-Guided_Radiology_Report_Generation_CVPR_2023_paper.html)** — Generates explainable radiology reports guided by interactively selected image regions.
- **[Learning To Exploit Temporal Structure for Biomedical Vision-Language Processing](https://openaccess.thecvf.com/content/CVPR2023/html/Bannur_Learning_To_Exploit_Temporal_Structure_for_Biomedical_Vision-Language_Processing_CVPR_2023_paper.html)** — BioViL-T: CNN-Transformer hybrid multi-image encoder jointly trained with a text model on longitudinal chest X-ray reports; SOTA on progression classification, phrase grounding, and report generation. *Bannur et al., Microsoft Research*

#### 📋 Clinical NLP, EHR & Healthcare

- **[Benchmarking Self-Supervised Learning on Diverse Pathology Datasets](https://openaccess.thecvf.com/content/CVPR2023/html/Kang_Benchmarking_Self-Supervised_Learning_on_Diverse_Pathology_Datasets_CVPR_2023_paper.html)** — Evaluates self-supervised learning across diverse pathology datasets.
- **[Bi-Directional Feature Fusion Generative Adversarial Network for Ultra-High Resolution Pathological Image Virtual Re-Staining](https://openaccess.thecvf.com/content/CVPR2023/html/Sun_Bi-Directional_Feature_Fusion_Generative_Adversarial_Network_for_Ultra-High_Resolution_Pathological_CVPR_2023_paper.html)** — Uses bidirectional feature fusion for high-resolution virtual pathology restaining.
- **[Causally-Aware Intraoperative Imputation for Overall Survival Time Prediction](https://openaccess.thecvf.com/content/CVPR2023/html/Li_Causally-Aware_Intraoperative_Imputation_for_Overall_Survival_Time_Prediction_CVPR_2023_paper.html)** — Imputes missing intraoperative information with causal structure for survival prediction.
- **[DeGPR: Deep Guided Posterior Regularization for Multi-Class Cell Detection and Counting](https://openaccess.thecvf.com/content/CVPR2023/html/Tyagi_DeGPR_Deep_Guided_Posterior_Regularization_for_Multi-Class_Cell_Detection_and_CVPR_2023_paper.html)** — Regularizes posterior predictions for multiclass cell detection and counting.
- **[Dynamic Graph Enhanced Contrastive Learning for Chest X-Ray Report Generation](https://openaccess.thecvf.com/content/CVPR2023/html/Li_Dynamic_Graph_Enhanced_Contrastive_Learning_for_Chest_X-Ray_Report_Generation_CVPR_2023_paper.html)** — Dynamic knowledge graph with contrastive learning (DCL) retrieves disease-specific nodes to guide chest X-ray report generation; SOTA on IU-Xray and MIMIC-CXR. *Li et al.*
- **[Image Quality-Aware Diagnosis via Meta-Knowledge Co-Embedding](https://openaccess.thecvf.com/content/CVPR2023/html/Che_Image_Quality-Aware_Diagnosis_via_Meta-Knowledge_Co-Embedding_CVPR_2023_paper.html)** — Accounts for image quality in diagnostic modeling through shared knowledge embeddings.
- **[KiUT: Knowledge-Injected U-Transformer for Radiology Report Generation](https://openaccess.thecvf.com/content/CVPR2023/html/Huang_KiUT_Knowledge-Injected_U-Transformer_for_Radiology_Report_Generation_CVPR_2023_paper.html)** — U-connection transformer that distills visual, clinical, and contextual knowledge at multiple scales for accurate radiology report generation.
- **[METransformer: Radiology Report Generation by Transformer With Multiple Learnable Expert Tokens](https://openaccess.thecvf.com/content/CVPR2023/html/Wang_METransformer_Radiology_Report_Generation_by_Transformer_With_Multiple_Learnable_Expert_CVPR_2023_paper.html)** — Multiple learnable expert tokens in both encoder and decoder attend to complementary image regions and are regularized by orthogonal loss for diverse, accurate report generation.
- **[Towards Trustable Skin Cancer Diagnosis via Rewriting Model's Decision](https://openaccess.thecvf.com/content/CVPR2023/html/Yan_Towards_Trustable_Skin_Cancer_Diagnosis_via_Rewriting_Models_Decision_CVPR_2023_paper.html)** — Analyzes and revises model decisions for more trustworthy skin cancer classification.

#### 🧠 Neuroimaging, EEG & Brain AI

- **[High-Resolution Image Reconstruction With Latent Diffusion Models From Human Brain Activity](https://openaccess.thecvf.com/content/CVPR2023/html/Takagi_High-Resolution_Image_Reconstruction_With_Latent_Diffusion_Models_From_Human_Brain_CVPR_2023_paper.html)** — Reconstructs high-resolution images from human brain activity using latent diffusion.
- **[Neuralizer: General Neuroimage Analysis Without Re-Training](https://openaccess.thecvf.com/content/CVPR2023/html/Czolbe_Neuralizer_General_Neuroimage_Analysis_Without_Re-Training_CVPR_2023_paper.html)** — Performs neuroimage analysis across tasks without task-specific retraining.
- **[Seeing Beyond the Brain: Conditional Diffusion Model With Sparse Masked Modeling for Vision Decoding](https://openaccess.thecvf.com/content/CVPR2023/html/Chen_Seeing_Beyond_the_Brain_Conditional_Diffusion_Model_With_Sparse_Masked_CVPR_2023_paper.html)** — Reconstructs visual content from brain activity with diffusion models.

#### 🫀 Physiological Signals & Medical Time Series

- **[Neuron Structure Modeling for Generalizable Remote Physiological Measurement](https://openaccess.thecvf.com/content/CVPR2023/html/Lu_Neuron_Structure_Modeling_for_Generalizable_Remote_Physiological_Measurement_CVPR_2023_paper.html)** — Uses neuronal-structure modeling for generalizable remote physiological measurement.
- **[Non-Contrastive Unsupervised Learning of Physiological Signals From Video](https://openaccess.thecvf.com/content/CVPR2023/html/Speth_Non-Contrastive_Unsupervised_Learning_of_Physiological_Signals_From_Video_CVPR_2023_paper.html)** — Learns physiological video signals without contrastive supervision.

#### 🏥 Surgical AI

- **[Constrained Evolutionary Diffusion Filter for Monocular Endoscope Tracking](https://openaccess.thecvf.com/content/CVPR2023/html/Luo_Constrained_Evolutionary_Diffusion_Filter_for_Monocular_Endoscope_Tracking_CVPR_2023_paper.html)** — Tracks monocular endoscopes with constrained evolutionary filtering.

---

## NeurIPS

### NeurIPS 2025

#### 🔬 Medical Imaging & Segmentation

- **[AOR: Anatomical Ontology-Guided Reasoning for Medical Large Multimodal Model in Chest X-Ray Interpretation](https://proceedings.neurips.cc/paper_files/paper/2025/hash/1bd9b52bef7bdf59c6382eace3510b56-Abstract-Conference.html)** — Uses anatomical ontologies to guide chest X-ray reasoning in medical multimodal models.
- **[CXReasonBench: A Benchmark for Evaluating Structured Diagnostic Reasoning in Chest X-rays](https://proceedings.neurips.cc/paper_files/paper/2025/hash/7ef1f85b1c93a08274ee388a01381729-Abstract-Datasets_and_Benchmarks_Track.html)** — Benchmarks structured diagnostic reasoning from chest X-rays. *[Datasets and Benchmarks]*
- **[D2SA: Dual-Stage Distribution and Slice Adaptation for Efficient Test-Time Adaptation in MRI Reconstruction](https://proceedings.neurips.cc/paper_files/paper/2025/hash/a41a0bb8185ddb8cf37c29ef9c83e5ac-Abstract-Conference.html)** — Adapts both distributions and slices at inference for MRI reconstruction.
- **[DIsoN: Decentralized Isolation Networks for Out-of-Distribution Detection in Medical Imaging](https://proceedings.neurips.cc/paper_files/paper/2025/hash/ee4432ad0aa3ab4c6c3dee47b2d541b5-Abstract-Conference.html)** — Detects out-of-distribution medical images through decentralized isolation networks.
- **[Dual-Res Tandem Mamba-3D: Bilateral Breast Lesion Detection and Classification on Non-contrast Chest CT](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2456a42386e445ba884511aa17ca4a30-Abstract-Conference.html)** — Detects and classifies breast lesions in non-contrast chest CT.
- **[Fast MRI for All: Bridging Access Gaps by Training without Raw Data](https://proceedings.neurips.cc/paper_files/paper/2025/hash/1653aaa4b24f65b009ede40c8761ed1f-Abstract-Conference.html)** — Studies accelerated MRI training when raw measurement data are unavailable.
- **[Improving Deep Learning for Accelerated MRI With Data Filtering](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f9ea03241672bac37ba9390449e96a98-Abstract-Datasets_and_Benchmarks_Track.html)** — Filters training data to improve accelerated MRI reconstruction. *[Datasets and Benchmarks]*
- **[LoMix: Learnable Weighted Multi-Scale Logits Mixing for Medical Image Segmentation](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5f0e54e34ba4c30fbc6f229986dbffb4-Abstract-Conference.html)** — Combines multiscale segmentation predictions through learned logit weights.
- **[Mamba Goes HoME: Hierarchical Soft Mixture-of-Experts for 3D Medical Image Segmentation](https://proceedings.neurips.cc/paper_files/paper/2025/hash/8cdae43c4af3da3f157382f9ebc65c56-Abstract-Conference.html)** — Combines hierarchical expert mixtures and state-space modeling for 3D medical segmentation.
- **[MedSG-Bench: A Benchmark for Medical Image Sequences Grounding](https://proceedings.neurips.cc/paper_files/paper/2025/hash/6c22b0280d0d7d9e0c3126b1e92df1a0-Abstract-Datasets_and_Benchmarks_Track.html)** — Benchmarks grounding of descriptions in medical image sequences. *[Datasets and Benchmarks]*
- **[Neighborhood Self-Dissimilarity Attention for Medical Image Segmentation](https://proceedings.neurips.cc/paper_files/paper/2025/hash/36b80eae70ff629d667f210e13497edf-Abstract-Conference.html)** — Uses neighborhood dissimilarities to guide attention in medical segmentation.
- **[Optical Coherence Tomography Harmonization with Anatomy-Guided Latent Metric Schrödinger Bridges](https://proceedings.neurips.cc/paper_files/paper/2025/hash/08b60b4af0b8163b18553b15f5ce25d2-Abstract-Conference.html)** — Harmonizes optical coherence tomography with anatomically guided latent transport.
- **[Orochi: Versatile Biomedical Image Processor](https://proceedings.neurips.cc/paper_files/paper/2025/hash/14b15e3676b060fb8fcc94eddadd0710-Abstract-Conference.html)** — Provides a general biomedical image-processing framework.
- **[Pancakes: Consistent Multi-Protocol Image Segmentation Across Biomedical Domains](https://proceedings.neurips.cc/paper_files/paper/2025/hash/3cd5473f038dfb5357e3544cc1cb3b98-Abstract-Conference.html)** — Generates multiple plausible segmentation protocols for unseen biomedical domains while maintaining semantic consistency across images.
- **[PanTS: The Pancreatic Tumor Segmentation Dataset](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2dc24f4adc257251b2f3929c67ec1e3a-Abstract-Datasets_and_Benchmarks_Track.html)** — Multi-institutional CT dataset with expert-validated annotations of pancreatic tumors, pancreatic subregions, and surrounding anatomy. *Datasets and Benchmarks Track* *[Datasets and Benchmarks]*
- **[PolyPose: Deformable 2D/3D Registration via Polyrigid Transformations](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5750f91d8fb9d5c02bd8ad2c3b44456b-Abstract-Conference.html)** — Registers deformable 2D and 3D medical images using locally rigid transformations.
- **[SHF: Symmetrical Hierarchical Forest with Pretrained Vision Transformer Encoder for High-Resolution Medical Segmentation](https://proceedings.neurips.cc/paper_files/paper/2025/hash/cc44bf651235b9cd61c4143ae3bbb0de-Abstract-Conference.html)** — Combines hierarchical structures and pretrained visual features for high-resolution medical segmentation.
- **[The Boundaries of Fair AI in Medical Image Prognosis: A Causal Perspective](https://proceedings.neurips.cc/paper_files/paper/2025/hash/c1715562b2227580b6c6db2050d7f6d2-Abstract-Conference.html)** — FairTTE studies demographic disparities and their causal sources in imaging-based time-to-event prediction, including under distribution shifts.
- **[Time-Embedded Algorithm Unrolling for Computational MRI](https://proceedings.neurips.cc/paper_files/paper/2025/hash/86f19768c110b25ac41dc08cd3783d12-Abstract-Conference.html)** — Uses temporal embeddings in algorithm-unrolled MRI reconstruction.
- **[Towards Better Dental AI: A Multimodal Benchmark and Instruction Dataset for Panoramic X-ray Analysis](https://proceedings.neurips.cc/paper_files/paper/2025/hash/3797b3a3c939156757857cf1b9afde3c-Abstract-Datasets_and_Benchmarks_Track.html)** — Benchmarks multimodal reasoning and instruction following for panoramic dental X-rays. *[Datasets and Benchmarks]*
- **[Towards Generalizable Retina Vessel Segmentation with Deformable Graph Priors](https://proceedings.neurips.cc/paper_files/paper/2025/hash/a3a931c0781a4608a2e5e6a12fb1eaa8-Abstract-Conference.html)** — Uses deformable graph priors for retinal vessel segmentation generalization.
- **[Towards Prospective Medical Image Reconstruction via Knowledge-Informed Dynamic Optimal Transport](https://proceedings.neurips.cc/paper_files/paper/2025/hash/3a5b75ce6cbd3aaaa32d6e935ffc4cff-Abstract-Conference.html)** — Uses knowledge-informed dynamic transport for medical image reconstruction.
- **[TractoTransformer: Diffusion MRI Streamline Tractography using CNN and Transformer Networks](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e510ebf9102e17d0ef6c6a0144678da7-Abstract-Conference.html)** — Combines convolutional and transformer features for diffusion MRI tractography.
- **[VQ-Seg: Vector-Quantized Token Perturbation for Semi-Supervised Medical Image Segmentation](https://proceedings.neurips.cc/paper_files/paper/2025/hash/201408406e0c5cf7626c4baeae6eaadd-Abstract-Conference.html)** — Perturbs quantized visual tokens for semi-supervised medical segmentation.
- **[X-Field: A Physically Informed Representation for 3D X-ray Reconstruction](https://proceedings.neurips.cc/paper_files/paper/2025/hash/dd49e00b6a3762d44f623e383ff6d29b-Abstract-Conference.html)** — Uses physically informed representations for 3D X-ray reconstruction.

#### 🧫 Computational Pathology & Microscopy

- **[Cancer Survival Analysis via Zero-shot Tumor Microenvironment Segmentation on Low-resolution Whole Slide Pathology Images](https://proceedings.neurips.cc/paper_files/paper/2025/hash/527d9d8f89aec80d634e366a97f49ba8-Abstract-Conference.html)** — Predicts cancer survival using zero-shot tumor-microenvironment segmentation in whole-slide pathology.
- **[D-VST: Diffusion Transformer for Pathology-Correct Tone-Controllable Cross-Dye Virtual Staining of Whole Slide Images](https://proceedings.neurips.cc/paper_files/paper/2025/hash/048445f5e3321dc9721930b15ba9387b-Abstract-Conference.html)** — Produces pathology-preserving whole-slide virtual stains with controllable tone.
- **[$\epsilon$-Seg: Sparsely Supervised Semantic Segmentation of Microscopy Data](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2bece8a80d534c625aa2503871d752ed-Abstract-Conference.html)** — Segments microscopy images with sparse semantic supervision.
- **[Few-Shot Learning from Gigapixel Images via Hierarchical Vision-Language Alignment and Modeling](https://proceedings.neurips.cc/paper_files/paper/2025/hash/675dc71676eb3bec5326824365a9bac2-Abstract-Conference.html)** — Aligns hierarchical image-language representations for few-shot gigapixel analysis.
- **[From Pixels to Views: Learning Angular-Aware and Physics-Consistent Representations for Light Field Microscopy](https://proceedings.neurips.cc/paper_files/paper/2025/hash/dcad3425f5c8c36b5b3885c091bf1257-Abstract-Conference.html)** — Learns angular-aware and physics-consistent representations for light-field microscopy.
- **[GeneFlow: Translation of Single-cell Gene Expression to Histopathological Images via Rectified Flow](https://proceedings.neurips.cc/paper_files/paper/2025/hash/40ae6c3a8dea3b20ea2352b33f52243f-Abstract-Conference.html)** — Generates histopathological images from single-cell gene-expression information through rectified flow.
- **[Learning Relative Gene Expression Trends from Pathology Images in Spatial Transcriptomics](https://proceedings.neurips.cc/paper_files/paper/2025/hash/7d535a224c8ae54ba75bac0457b6b279-Abstract-Conference.html)** — Predicts relative gene-expression patterns from spatial histopathology images.
- **[MAPLE: Multi-scale Attribute-enhanced Prompt Learning for Few-shot Whole Slide Image Classification](https://proceedings.neurips.cc/paper_files/paper/2025/hash/a94a8800a4b0af45600bab91164849df-Abstract-Conference.html)** — Uses multiscale attribute-guided prompts for few-shot whole-slide classification.
- **[MATCH: Multi-faceted Adaptive Topo-Consistency for Semi-Supervised Histopathology Segmentation](https://proceedings.neurips.cc/paper_files/paper/2025/hash/97e2df4bb8b2f1913657344a693166a2-Abstract-Conference.html)** — Uses multiple topological consistency constraints for semi-supervised pathology segmentation.
- **[Navigating the MIL Trade-Off: Flexible Pooling for Whole Slide Image Classification](https://proceedings.neurips.cc/paper_files/paper/2025/hash/8bacb23a4f6b6f52dd5c81c15b4e4ac5-Abstract-Conference.html)** — Adapts pooling to different whole-slide multiple-instance learning tasks.
- **[PathVQ: Reforming Computational Pathology Foundation Model for Whole Slide Image Analysis via Vector Quantization](https://proceedings.neurips.cc/paper_files/paper/2025/hash/59f278de1619bdb6b53fd04e8e0976e0-Abstract-Conference.html)** — Adapts pathology foundation representations through vector quantization for whole-slide tasks.
- **[Revisiting End-to-End Learning with Slide-level Supervision in Computational Pathology](https://proceedings.neurips.cc/paper_files/paper/2025/hash/eae33167166b44df7c929f70984c0c0b-Abstract-Conference.html)** — Reassesses end-to-end pathology learning from slide-level labels.
- **[scSplit: Bringing Severity Cognizance to Image Decomposition in Fluorescence Microscopy](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5d40003a9594a35cb0fe42e7aa3eb078-Abstract-Conference.html)** — Decomposes fluorescence microscopy images while accounting for signal severity.
- **[Semantic and Visual Crop-Guided Diffusion Models for Heterogeneous Tissue Synthesis in Histopathology](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b6ae90f159bb5d2e48bad834e12bf1d8-Abstract-Conference.html)** — Synthesizes heterogeneous histopathology tissues with semantic and visual crop guidance.
- **[Sequential Attention-based Sampling for Histopathological Analysis](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e45e17a501d2c77511eb29d138b33a01-Abstract-Conference.html)** — Learns sequential attention-based sampling for pathology analysis.
- **[SGCD: Stain-Guided CycleDiffusion for Unsupervised Domain Adaptation of Histopathology Image Classification](https://proceedings.neurips.cc/paper_files/paper/2025/hash/37964391303da7d70d07e83d2b0c3c5e-Abstract-Conference.html)** — Uses stain-guided diffusion to adapt histopathology classifiers without target labels.
- **[Single GPU Task Adaptation of Pathology Foundation Models for Whole Slide Image Analysis](https://proceedings.neurips.cc/paper_files/paper/2025/hash/10a3b1c30b8cceb507b9e8ddcc9a1a6a-Abstract-Conference.html)** — Adapts pathology foundation models to whole-slide tasks on a single GPU.
- **[STARC-9: A Large-scale Dataset for Multi-Class Tissue Classification for CRC Histopathology](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f90cd97544e17dfd76af5c4f1b698a50-Abstract-Datasets_and_Benchmarks_Track.html)** — Provides colorectal histopathology data for multiclass tissue classification. *[Datasets and Benchmarks]*
- **[THUNDER: Tile-level Histopathology image UNDERstanding benchmark](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e3a2bd22ef74970b2fff74a16f806237-Abstract-Datasets_and_Benchmarks_Track.html)** — Benchmarks tile-level understanding of histopathology images. *[Datasets and Benchmarks]*
- **[Unsupervised Trajectory Optimization for 3D Registration in Serial Section Electron Microscopy using Neural ODEs](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b9ecf4d84999a61783c360c3782e801e-Abstract-Conference.html)** — Registers serial-section electron microscopy volumes through trajectory optimization with neural ODEs.

#### 🤖 Foundation Models & Vision-Language

- **[3D-RAD: A Comprehensive 3D Radiology Med-VQA Dataset with Multi-Temporal Analysis and Diverse Diagnostic Tasks](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f8250afec8305ed4a6b27ae405507442-Abstract-Datasets_and_Benchmarks_Track.html)** — Benchmarks CT visual question answering across six tasks, including medical computation and longitudinal diagnosis. *Datasets and Benchmarks Track* *[Datasets and Benchmarks]*
- **[An Investigation of Memorization Risk in Healthcare Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2025/hash/0f4f18102c0dad5156e11e85414ba2d2-Abstract-Conference.html)** — Measures memorization and privacy risks in healthcare foundation models.
- **[Better Tokens for Better 3D: Advancing Vision-Language Modeling in 3D Medical Imaging](https://proceedings.neurips.cc/paper_files/paper/2025/hash/c4861cc81b768dc36a676fceed8f7672-Abstract-Conference.html)** — BTB3D learns compact volumetric tokens for high-resolution CT report generation and text-conditioned CT synthesis.
- **[Chiron-o1: Igniting Multimodal Large Language Models towards Generalizable Medical Reasoning via Mentor-Intern Collaborative Search](https://proceedings.neurips.cc/paper_files/paper/2025/hash/967017dbe801dc95f5a2587c6d6a1ef3-Abstract-Conference.html)** — Uses collaborative mentor-intern search to improve generalizable multimodal medical reasoning.
- **[CPathAgent: An Agent-based Foundation Model for Interpretable High-Resolution Pathology Image Analysis Mimicking Pathologists' Diagnostic Logic](https://proceedings.neurips.cc/paper_files/paper/2025/hash/933b5d002cf251b3e854d586e55ac58c-Abstract-Conference.html)** — Models pathologists' diagnostic workflows with an interpretable high-resolution pathology agent.
- **[CURV: Coherent Uncertainty-Aware Reasoning in Vision-Language Models for X-Ray Report Generation](https://proceedings.neurips.cc/paper_files/paper/2025/hash/86a99b74adac7c77998902371f53850d-Abstract-Conference.html)** — Models uncertainty consistently during vision-language radiology report reasoning.
- **[DrVD-Bench: Do Vision-Language Models Reason Like Human Doctors in Medical Image Diagnosis?](https://proceedings.neurips.cc/paper_files/paper/2025/hash/12750d99d0faa73763108ff2bbeb54fd-Abstract-Datasets_and_Benchmarks_Track.html)** — Evaluates visual evidence comprehension, diagnostic reasoning trajectories, and report generation across five medical imaging modalities. *Datasets and Benchmarks Track* *[Datasets and Benchmarks]*
- **[ExGra-Med: Extended Context Graph Alignment for Medical Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2025/hash/9df0a10002a16365d03792ee5098376d-Abstract-Conference.html)** — Extends contextual graph alignment in medical image-language models.
- **[From Human Attention to Diagnosis: Semantic Patch-Level Integration of Vision-Language Models in Medical Imaging](https://proceedings.neurips.cc/paper_files/paper/2025/hash/be7bc8aa38696723cebe296b6122d7e3-Abstract-Conference.html)** — Combines human attention and patch-level semantic information for medical image diagnosis.
- **[GauSAM: Contour‑Guided 2D Gaussian Fields for Multi‑Scale Medical Image Segmentation with Segment Anything](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e7ed7e6f3a0962844379b3ac9629e9ec-Abstract-Conference.html)** — Uses contour-guided Gaussian fields with SAM for multiscale medical segmentation.
- **[MedicalNarratives: Connecting Medical Vision and Language with Localized Narratives](https://proceedings.neurips.cc/paper_files/paper/2025/hash/c12e460cd8f8ae39f1ed7a9140c62620-Abstract-Datasets_and_Benchmarks_Track.html)** — Links medical images and language through localized narratives. *[Datasets and Benchmarks]*
- **[QoQ-Med: Building Multimodal Clinical Foundation Models with Domain-Aware GRPO Training](https://proceedings.neurips.cc/paper_files/paper/2025/hash/359ffa88712bd688963a0ca641d8330b-Abstract-Conference.html)** — Trains generalist clinical models across medical images, time-series signals, and reports using rewards adjusted for domain rarity and modality difficulty.
- **[RAD: Towards Trustworthy Retrieval-Augmented Multi-modal Clinical Diagnosis](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b28ca52a43881fd87196c71145f30092-Abstract-Conference.html)** — Retrieves disease-centered knowledge and uses clinical guidelines to guide multimodal feature alignment and diagnostic fusion.
- **[RadZero: Similarity-Based Cross-Attention for Explainable Vision-Language Alignment in Chest X-ray with Zero-Shot Multi-Task Capability](https://proceedings.neurips.cc/paper_files/paper/2025/hash/510e5c2fd5ad326f75594563f4ad5e0d-Abstract-Conference.html)** — Aligns chest X-rays and language through interpretable similarity-based attention.
- **[Segment Anything Model Meets Semi-supervised Medical Image Segmentation: A Novel Perspective](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f88306d7c33a024c255ed6aa5e1211fd-Abstract-Conference.html)** — Integrates SAM into semi-supervised medical segmentation.
- **[SMMILE: An expert-driven benchmark for multimodal medical in-context learning](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5e0d42bf1eaafd60c03f141eb7ac761b-Abstract-Datasets_and_Benchmarks_Track.html)** — Expert-curated benchmark testing whether multimodal models can learn medical tasks from demonstrations across specialties and imaging modalities. *Datasets and Benchmarks Track* *[Datasets and Benchmarks]*
- **[Toward a Vision-Language Foundation Model for Medical Data: Multimodal Dataset and Benchmarks for Vietnamese PET/CT Report Generation](https://proceedings.neurips.cc/paper_files/paper/2025/hash/a9f5ebadfbf7b6b10d685c385713b35a-Abstract-Datasets_and_Benchmarks_Track.html)** — Provides multimodal Vietnamese PET/CT data and report-generation benchmarks. *[Datasets and Benchmarks]*

#### 📋 Clinical NLP, EHR & Healthcare

- **[Adaptive Data-Borrowing for Improving Treatment Effect Estimation using External Controls](https://proceedings.neurips.cc/paper_files/paper/2025/hash/0bb9b8b55b0fd61c7788a8a4ddbd3ddd-Abstract-Conference.html)** — Borrows external-control data adaptively to estimate clinical treatment effects.
- **[Adaptive Frontier Exploration on Graphs with Applications to Network-Based Disease Testing](https://proceedings.neurips.cc/paper_files/paper/2025/hash/dc300c4d75b94b211b149ae4bcbbf2d2-Abstract-Conference.html)** — Learns network exploration strategies for disease testing.
- **[Aligning Evaluation with Clinical Priorities: Calibration, Label Shift, and Error Costs](https://proceedings.neurips.cc/paper_files/paper/2025/hash/10c456d2160517581a234dfde15a7505-Abstract-Conference.html)** — Evaluates clinical predictions with calibration, label shift, and asymmetric error costs.
- **[Anatomically inspired digital twins capture hierarchical object representations in visual cortex](https://proceedings.neurips.cc/paper_files/paper/2025/hash/7ae2b0eedc560e3afbffd68445b8a220-Abstract-Conference.html)** — Models hierarchical human visual-cortex representations with anatomically informed digital twins.
- **[Beyond Average Value Function in Precision Medicine: Maximum Probability-Driven Reinforcement Learning for Survival Analysis](https://proceedings.neurips.cc/paper_files/paper/2025/hash/398753ddd2e10ce39d0c620e85fab922-Abstract-Conference.html)** — Optimizes survival-related precision-medicine decisions through reinforcement learning.
- **[CARES: Comprehensive Evaluation of Safety and Adversarial Robustness in Medical LLMs](https://proceedings.neurips.cc/paper_files/paper/2025/hash/1ca47465a87b8e125d9076b2e6ac6c96-Abstract-Datasets_and_Benchmarks_Track.html)** — Evaluates medical language-model safety and adversarial robustness. *[Datasets and Benchmarks]*
- **[Causal Explanation-Guided Learning for Organ Allocation](https://proceedings.neurips.cc/paper_files/paper/2025/hash/fde7a53da2d95f459331e308e684c9a9-Abstract-Conference.html)** — Guides organ-allocation models with causal explanations.
- **[CGBench: Benchmarking Language Model Scientific Reasoning for Clinical Genetics Research](https://proceedings.neurips.cc/paper_files/paper/2025/hash/19138f8392f7863f483e90e1c2819fc9-Abstract-Datasets_and_Benchmarks_Track.html)** — Benchmarks language-model scientific reasoning in clinical genetics. *[Datasets and Benchmarks]*
- **[ClinBench: A Standardized Multi-Domain Framework for Evaluating Large Language Models in Clinical Information Extraction](https://proceedings.neurips.cc/paper_files/paper/2025/hash/621b4af77315234465ef366ea14b5dc5-Abstract-Datasets_and_Benchmarks_Track.html)** — Standardizes evaluation of structured extraction from clinical notes across oncology, atrial fibrillation, and social determinants of health. *Datasets and Benchmarks Track* *[Datasets and Benchmarks]*
- **[ClinicalLab: Aligning Agents for Multi-Departmental Clinical Diagnostics in the Real World](https://proceedings.neurips.cc/paper_files/paper/2025/hash/6a059625a6027aca18302803743abaa2-Abstract-Datasets_and_Benchmarks_Track.html)** — Combines a multi-department diagnostic benchmark, clinical evaluation metrics, and an agent designed around clinical workflows. *Datasets and Benchmarks Track* *[Datasets and Benchmarks]*
- **[Controlling The Spread of Epidemics on Networks with Differential Privacy](https://proceedings.neurips.cc/paper_files/paper/2025/hash/4f347493f34e4a88fecf6783dbaabfb9-Abstract-Conference.html)** — Controls network epidemic spread subject to differential privacy.
- **[DAAC: Discrepancy-Aware Adaptive Contrastive Learning for Medical Time series](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f36a180277bd3d5781dc02245f9d5f52-Abstract-Conference.html)** — Uses discrepancy-aware contrastive learning for medical time series.
- **[Democratizing Clinical Risk Prediction with Cross-Cohort Cross-Modal Knowledge Transfer](https://proceedings.neurips.cc/paper_files/paper/2025/hash/99fda93fb2c8f60fbbf10a7df6cf1c06-Abstract-Conference.html)** — Transfers clinical risk predictors across cohorts and modalities.
- **[DermaCon-IN: A Multiconcept-Annotated Dermatological Image Dataset of Indian Skin Disorders for Clinical AI Research](https://proceedings.neurips.cc/paper_files/paper/2025/hash/a2c548b2ed3141400d86a235eaa6fad0-Abstract-Datasets_and_Benchmarks_Track.html)** — Provides dermatology images of Indian skin conditions with clinical concept annotations. *[Datasets and Benchmarks]*
- **[Detecting Data Deviations in Electronic Health Records](https://proceedings.neurips.cc/paper_files/paper/2025/hash/4b460c81b7bbdee478817bf1b7f0b9ca-Abstract-Conference.html)** — Uses layered knowledge distillation to estimate EHR data fidelity and detect records that deviate from patients' physiological states.
- **[Doctor Approved: Generating Medically Accurate Skin Disease Images through AI-Expert Feedback](https://proceedings.neurips.cc/paper_files/paper/2025/hash/1cda90dcb11055c9d40ce6395b53d146-Abstract-Conference.html)** — Uses expert feedback to improve the medical accuracy of generated skin disease images.
- **[DoseSurv: Predicting Personalized Survival Outcomes under Continuous-Valued Treatments](https://proceedings.neurips.cc/paper_files/paper/2025/hash/221f7e3c1c8b4ee48d45a53589051590-Abstract-Conference.html)** — Predicts personalized survival outcomes under continuously valued treatments.
- **[DQVis Dataset: Natural Language to Biomedical Visualization](https://proceedings.neurips.cc/paper_files/paper/2025/hash/54b50a954e7e46fef6fa33f7dd83e7ec-Abstract-Datasets_and_Benchmarks_Track.html)** — Benchmarks natural-language interfaces for biomedical visualization. *[Datasets and Benchmarks]*
- **[FAPEX: Fractional Amplitude-Phase Expressor for Robust Cross-Subject Seizure Prediction](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b7de1556bc4be01966c6bc56fb2da6e0-Abstract-Conference.html)** — Uses amplitude-phase representations to improve cross-subject seizure prediction.
- **[Fine-grained List-wise Alignment for Generative Medication Recommendation](https://proceedings.neurips.cc/paper_files/paper/2025/hash/44a1f7e0a1fe7867f586b10739a0c26a-Abstract-Conference.html)** — Uses fine-grained listwise alignment for generative medication recommendation.
- **[From Indicators to Insights: Diversity-Optimized for Medical Series-Text Decoding via LLMs](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e8e30fda5ab87ea93360a36288ac0145-Abstract-Conference.html)** — Decodes medical time-series signals into text through language models.
- **[From Pose to Muscle: Multimodal Learning for Piano Hand Muscle Electromyography](https://proceedings.neurips.cc/paper_files/paper/2025/hash/a7d80c990c77ae2570087243ec802314-Abstract-Conference.html)** — Provides multimodal representations of hand electromyography during piano performance.
- **[From Pretraining to Pathology: How Noise Leads to Catastrophic Inheritance in Medical Models](https://proceedings.neurips.cc/paper_files/paper/2025/hash/854ba5f89c3b048265a5e00231ea5477-Abstract-Conference.html)** — Studies how pretraining noise propagates into downstream medical models.
- **[Generating Multi-Table Time Series EHR from Latent Space with Minimal Preprocessing](https://proceedings.neurips.cc/paper_files/paper/2025/hash/26a1c8863b2e2e6bd820849d46f4c25d-Abstract-Conference.html)** — Generates multitable longitudinal EHR data with limited preprocessing.
- **[Improving the Generation and Evaluation of Synthetic Data for Downstream Medical Causal Inference](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2ba023061bca4e2d3cbe9ceaeef37e43-Abstract-Conference.html)** — Studies synthetic-data generation and evaluation for downstream clinical causal inference.
- **[Integrating Drug Substructures and Longitudinal Electronic Health Records for Personalized Drug Recommendation](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5b0c0b2c2efdd736a53688ebfdc3bcdb-Abstract-Conference.html)** — Combines drug substructures and longitudinal patient records for personalized medication recommendation.
- **[Investigating and Mitigating Catastrophic Forgetting in Medical Knowledge Injection through Internal Knowledge Augmentation Learning](https://proceedings.neurips.cc/paper_files/paper/2025/hash/0d2c50691b832d8e8901715998e7c22c-Abstract-Conference.html)** — Uses internal knowledge augmentation to reduce forgetting during medical knowledge injection.
- **[Learning to Zoom with Anatomical Relations for Medical Structure Detection](https://proceedings.neurips.cc/paper_files/paper/2025/hash/ebcf1bff7b2fe6dcc3fbe666faaa50f1-Abstract-Conference.html)** — Learns anatomy-guided zooming policies for medical structure detection.
- **[Magical: Medical Lay Language Generation via Semantic Invariance and Layperson-tailored Adaptation](https://proceedings.neurips.cc/paper_files/paper/2025/hash/ac242082287ec232a1b8080838526789-Abstract-Conference.html)** — Generates patient-facing medical language through semantic preservation and lay adaptation.
- **[MedAgentBoard: Benchmarking Multi-Agent Collaboration with Conventional Methods for Diverse Medical Tasks](https://proceedings.neurips.cc/paper_files/paper/2025/hash/d59aa09699530c00d4b875a883876641-Abstract-Datasets_and_Benchmarks_Track.html)** — Benchmarks medical multi-agent collaboration against conventional approaches. *[Datasets and Benchmarks]*
- **[MedChain: Bridging the Gap Between LLM Agents and Clinical Practice with Interactive Sequence](https://proceedings.neurips.cc/paper_files/paper/2025/hash/6bc02900c74234aa5a0c1a7148ed933f-Abstract-Datasets_and_Benchmarks_Track.html)** — Introduces sequential, interactive clinical cases and a retrieval-augmented agent spanning five stages of clinical workflow. *Datasets and Benchmarks Track* *[Datasets and Benchmarks]*
- **[MedMax: Mixed-Modal Instruction Tuning for Training Biomedical Assistants](https://proceedings.neurips.cc/paper_files/paper/2025/hash/9a6f7d845cf12385524f0f27ab26f57e-Abstract-Datasets_and_Benchmarks_Track.html)** — Trains biomedical assistants with mixed-modality instruction tuning. *[Datasets and Benchmarks]*
- **[MoodAngels: A Retrieval-augmented Multi-agent Framework for Psychiatry Diagnosis](https://proceedings.neurips.cc/paper_files/paper/2025/hash/27bb4753c44e0990865583fa49296465-Abstract-Conference.html)** — Uses retrieval-augmented expert mixtures for mental-health assistance.
- **[MTBBench: A Multimodal Sequential Clinical Decision-Making Benchmark in Oncology](https://proceedings.neurips.cc/paper_files/paper/2025/hash/103ea9d6b26ed1eceb881f5d588879e5-Abstract-Datasets_and_Benchmarks_Track.html)** — Benchmarks sequential multimodal clinical decisions in oncology. *[Datasets and Benchmarks]*
- **[Multimodal Disease Progression Modeling via Spatiotemporal Disentanglement and Multiscale Alignment](https://proceedings.neurips.cc/paper_files/paper/2025/hash/bfe27c959fda8112520479539c69360f-Abstract-Conference.html)** — Disentangles spatial and temporal information for multimodal disease-progression modeling.
- **[Offline Guarded Safe Reinforcement Learning for Medical Treatment Optimization Strategies](https://proceedings.neurips.cc/paper_files/paper/2025/hash/8cf2d1a2fef23281af0f50d1a04dfd7c-Abstract-Conference.html)** — Uses guarded offline reinforcement learning for safer treatment optimization.
- **[PatientSim: A Persona-Driven Simulator for Realistic Doctor-Patient Interactions](https://proceedings.neurips.cc/paper_files/paper/2025/hash/24945e3bdc7b3f4b2e64b9979a16f38e-Abstract-Datasets_and_Benchmarks_Track.html)** — Simulates doctor-patient interactions using patient personas. *[Datasets and Benchmarks]*
- **[Reinforcement Learning for Out-of-Distribution Reasoning in LLMs: An Empirical Study on Diagnosis-Related Group Coding](https://proceedings.neurips.cc/paper_files/paper/2025/hash/3d7cb780442f0d17c844dbe34997fab7-Abstract-Conference.html)** — Studies out-of-distribution medical coding through reinforcement learning on diagnosis-related groups.
- **[Scaling Epidemic Inference on Contact Networks: Theory and Algorithms](https://proceedings.neurips.cc/paper_files/paper/2025/hash/1450de2df1dff2bb997fbb0b9136f2d0-Abstract-Conference.html)** — Scales inference of epidemic dynamics on contact networks.
- **[Self-supervised Learning of Echocardiographic Video Representations via Online Cluster Distillation](https://proceedings.neurips.cc/paper_files/paper/2025/hash/581e1a06fa20f2c079dc5fb2db236335-Abstract-Conference.html)** — Learns echocardiographic video representations through online cluster distillation.
- **[Simulating Viva Voce Examinations to Evaluate Clinical Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2025/hash/ba16ea88cbe2478c10518df1d52811ec-Abstract-Datasets_and_Benchmarks_Track.html)** — Simulates oral examinations to evaluate language-model clinical reasoning. *[Datasets and Benchmarks]*
- **[SplashNet: Split‑and‑Share Encoders for Accurate and Efficient Typing with Surface Electromyography](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f29af347aedbdaa316043aa8457a8fb6-Abstract-Conference.html)** — Uses split-and-shared encoders for surface-EMG text input.
- **[Statistically Valid Post-Deployment Monitoring Should Be Standard for AI-Based Digital Health](https://proceedings.neurips.cc/paper_files/paper/2025/hash/a540928a972fea5b501b64c51f7829ef-Abstract-Position_Paper_Track.html)** — Argues for statistically valid monitoring of deployed digital-health models.
- **[TCM-Ladder: A Benchmark for Multimodal Question Answering on Traditional Chinese Medicine](https://proceedings.neurips.cc/paper_files/paper/2025/hash/cbdd26a4490f5a8dad0d732508714029-Abstract-Datasets_and_Benchmarks_Track.html)** — Benchmarks multimodal question answering about traditional Chinese medicine. *[Datasets and Benchmarks]*
- **[Timely Clinical Diagnosis through Active Test Selection](https://proceedings.neurips.cc/paper_files/paper/2025/hash/7c42e8a9eb471d225a4abec5e79d0153-Abstract-Conference.html)** — Selects diagnostic tests actively to reduce delays in clinical diagnosis.
- **[Towards Doctor-Like Reasoning: Medical RAG Fusing Knowledge with Patient Analogy through Textual Gradients](https://proceedings.neurips.cc/paper_files/paper/2025/hash/dd0151081b1e80e93f1b8aaf0b684c18-Abstract-Conference.html)** — Combines retrieved knowledge and analogous patients for medical reasoning.
- **[Uncover Governing Law of Pathology Propagation Mechanism Through A Mean-Field Game](https://proceedings.neurips.cc/paper_files/paper/2025/hash/88ced2103ce0c9f80c6aab9cabdd849d-Abstract-Conference.html)** — Studies mechanisms of pathological propagation through mean-field games.

#### 🧠 Neuroimaging, EEG & Brain AI

- **[BaRISTA: Brain Scale Informed Spatiotemporal Representation of Human Intracranial Neural Activity](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f42926b257ef16923f08bbf3b59fe214-Abstract-Conference.html)** — Learns spatiotemporal representations of human intracranial neural activity.
- **[Beyond Pairwise Connections: Extracting High-Order Functional Brain Network Structures under Global Constraints](https://proceedings.neurips.cc/paper_files/paper/2025/hash/fa86a9c7b9f341716ccb679d1aeb9afa-Abstract-Conference.html)** — Extracts high-order functional brain network structures under global constraints.
- **[BrainEC-LLM: Brain Effective Connectivity Estimation by Multiscale Mixing LLM](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b273c97f005db33b15b9514f2bd42431-Abstract-Conference.html)** — Estimates effective brain connectivity with multiscale mixing and language models.
- **[Brain Harmony: A Multimodal Foundation Model Unifying Morphology and Function into 1D Tokens](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b0832cc57899cfd2d3fedeb3f330ba80-Abstract-Conference.html)** — Unifies brain morphology and function in a multimodal foundation model.
- **[Brain-Inspired fMRI-to-Text Decoding via Incremental and Wrap-Up Language Modeling](https://proceedings.neurips.cc/paper_files/paper/2025/hash/dca63f2650fe9e88956c1b68440b8ee9-Abstract-Conference.html)** — Uses incremental and contextual language modeling for fMRI-to-text decoding.
- **[BrainMoE: Cognition Joint Embedding via Mixture-of-Expert Towards Robust Brain Foundation Model](https://proceedings.neurips.cc/paper_files/paper/2025/hash/061238f13b8e65ce435c4a691ff5d7f1-Abstract-Conference.html)** — Learns robust brain representations with a mixture of experts.
- **[BrainODE: Neural Shape Dynamics for Age- and Disease-aware Brain Trajectories](https://proceedings.neurips.cc/paper_files/paper/2025/hash/abdc8c031aa6c6917c3b593166e5e340-Abstract-Conference.html)** — Models age- and disease-dependent brain-shape trajectories through neural dynamics.
- **[BrainOmni: A Brain Foundation Model for Unified EEG and MEG Signals](https://proceedings.neurips.cc/paper_files/paper/2025/hash/3aef4a18c2646b9d11d9ab4d9bec72c8-Abstract-Conference.html)** — Pretrains shared representations across EEG and MEG recordings.
- **[Bridging Brains and Concepts: Interpretable Visual Decoding from fMRI with Semantic Bottlenecks](https://proceedings.neurips.cc/paper_files/paper/2025/hash/7da6e0e00702c60607a6ae05c802ef85-Abstract-Conference.html)** — Uses semantic bottlenecks to make fMRI visual decoding interpretable.
- **[Care-PD: A Multi-Site Anonymized Clinical Dataset for Parkinson’s Disease Gait Assessment](https://proceedings.neurips.cc/paper_files/paper/2025/hash/bedc73979a95be7727af0c9a99c675ce-Abstract-Datasets_and_Benchmarks_Track.html)** — Provides multisite anonymized gait recordings for clinical Parkinson's assessment. *[Datasets and Benchmarks]*
- **[CSBrain: A Cross-scale Spatiotemporal Brain Foundation Model for EEG Decoding](https://proceedings.neurips.cc/paper_files/paper/2025/hash/7e199ad8ae40eb19b2980f61f659cb07-Abstract-Conference.html)** — Pretrains EEG representations across spatial and temporal scales.
- **[DCA: Graph-Guided Deep Embedding Clustering for Brain Atlases](https://proceedings.neurips.cc/paper_files/paper/2025/hash/954729c2c57c32cab97c4f868dbb4d3e-Abstract-Conference.html)** — Uses graph-guided deep clustering to construct brain atlases.
- **[EvoBrain: Dynamic Multi-Channel EEG Graph Modeling for Time-Evolving Brain Networks](https://proceedings.neurips.cc/paper_files/paper/2025/hash/d51ce6040fe3dafd260411593f05a1fa-Abstract-Conference.html)** — Models changing multichannel EEG connectivity with dynamic graphs.
- **[Hierarchical Information Aggregation for Incomplete Multimodal Alzheimer's Disease Diagnosis](https://proceedings.neurips.cc/paper_files/paper/2025/hash/4da4dd613cc9e63932d643b9c6e8f86f-Abstract-Conference.html)** — Aggregates information hierarchically for Alzheimer's diagnosis under missing modalities.
- **[$i$MIND: Insightful Multi-subject Invariant Neural Decoding](https://proceedings.neurips.cc/paper_files/paper/2025/hash/daa098aa8e1fc718943ff1ab7b5b30c9-Abstract-Conference.html)** — Learns subject-invariant representations for neural decoding.
- **[Inference of Whole Brain Electrophysiological Networks Through Multimodal Integration of Simultaneous Scalp and Intracranial EEG](https://proceedings.neurips.cc/paper_files/paper/2025/hash/82a6afb1f666daaeec8da4d775452bc7-Abstract-Conference.html)** — Integrates simultaneous scalp and intracranial EEG to infer whole-brain electrophysiological networks.
- **[Is Limited Participant Diversity Impeding EEG-based Machine Learning?](https://proceedings.neurips.cc/paper_files/paper/2025/hash/aa5642fb7d78a1bca9ceba3d8bd564f4-Abstract-Conference.html)** — Examines demographic diversity as a limitation in EEG machine learning.
- **[Joint Modeling of fMRI and EEG Imaging Using Ordinary Differential Equation-Based Hypergraph Neural Networks](https://proceedings.neurips.cc/paper_files/paper/2025/hash/d29921d606226cdcf0fc8325f2fc1b99-Abstract-Conference.html)** — Jointly models fMRI and EEG with differential-equation hypergraphs.
- **[Listening to the Brain: Multi-Band sEEG Auditory Reconstruction via Dynamic Spatio-Temporal Hypergraphs](https://proceedings.neurips.cc/paper_files/paper/2025/hash/bbc6396ae4b4dbf78ce328aa8beafd27-Abstract-Datasets_and_Benchmarks_Track.html)** — Reconstructs auditory content from multiband stereoelectroencephalography using dynamic hypergraphs. *[Datasets and Benchmarks]*
- **[Local-Global Coupling Spiking Graph Transformer for Brain Disorders Diagnosis from Two Perspectives](https://proceedings.neurips.cc/paper_files/paper/2025/hash/4c454d34f3a4c8d6b4ca85a918e5d7ba-Abstract-Conference.html)** — Models brain disorders with local-global spiking graph representations.
- **[Long-term Intracortical Neural activity and Kinematics (LINK): An intracortical neural dataset for chronic brain-machine interfaces, neuroscience, and machine learning](https://proceedings.neurips.cc/paper_files/paper/2025/hash/cb463f73a35802996546ac8e8b1b2743-Abstract-Datasets_and_Benchmarks_Track.html)** — Provides long-term intracortical recordings and kinematics for brain-machine interface research. *[Datasets and Benchmarks]*
- **[LUNA: Efficient and Topology-Agnostic Foundation Model for EEG Signal Analysis](https://proceedings.neurips.cc/paper_files/paper/2025/hash/66969a9e6bd7a26dfeccea7227178ca7-Abstract-Conference.html)** — Builds an efficient EEG foundation model adaptable to recording topology.
- **[MoRE-Brain: Routed Mixture of Experts for Interpretable and Generalizable Cross-Subject fMRI Visual Decoding](https://proceedings.neurips.cc/paper_files/paper/2025/hash/50ea4dbd1cff6bd3daef939eff10c092-Abstract-Conference.html)** — Uses expert mixtures for interpretable cross-subject fMRI visual decoding.
- **[Multi-dataset Joint Pre-training of Emotional EEG Enables Generalizable Affective Computing](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f1b8d443042f376aa3654b6c68de6297-Abstract-Conference.html)** — Pretrains jointly across emotional EEG datasets for generalizable affect recognition.
- **[NEED: Cross-Subject and Cross-Task Generalization for Video and Image Reconstruction from EEG Signals](https://proceedings.neurips.cc/paper_files/paper/2025/hash/fca83589e85cb061631b7ebc5db5d6bd-Abstract-Conference.html)** — Studies cross-subject and cross-task visual reconstruction from EEG.
- **[NeuroH-TGL: Neuro-Heterogeneity Guided Temporal Graph Learning Strategy for Brain Disease Diagnosis](https://proceedings.neurips.cc/paper_files/paper/2025/hash/9d87a0c38431d0ec8d8b8ece95198c04-Abstract-Conference.html)** — Models temporal brain networks with neurobiological heterogeneity for disease diagnosis.
- **[NOVA: A Benchmark for Rare Anomaly Localization and Clinical Reasoning in Brain MRI](https://proceedings.neurips.cc/paper_files/paper/2025/hash/96a9caf416c8951812a666eca742e050-Abstract-Datasets_and_Benchmarks_Track.html)** — Benchmarks rare brain MRI anomaly localization and clinical reasoning. *[Datasets and Benchmarks]*
- **[Orthogonal Contrastive Learning for Multi-Representation fMRI Analysis](https://proceedings.neurips.cc/paper_files/paper/2025/hash/a81a1eabfb6cbece73ddd0e6a1645d67-Abstract-Conference.html)** — Learns multiple complementary fMRI representations through orthogonal contrastive objectives.
- **[Predicting Functional Brain Connectivity with Context-Aware Deep Neural Networks](https://proceedings.neurips.cc/paper_files/paper/2025/hash/7f09298fd090c13c5583549d22ec1158-Abstract-Conference.html)** — Predicts functional brain connectivity with context-aware networks.
- **[REFED: A Subject Real-time Dynamic Labeled EEG-fNIRS Synchronized Recorded Emotion Dataset](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2bf0ed7c35d9d84128e7f7c72ab76402-Abstract-Datasets_and_Benchmarks_Track.html)** — Provides synchronized EEG and fNIRS with dynamic emotion annotations. *[Datasets and Benchmarks]*
- **[REVE: A Foundation Model for EEG - Adapting to Any Setup with Large-Scale Pretraining on 25,000 Subjects](https://proceedings.neurips.cc/paper_files/paper/2025/hash/20a917f77773ac0fa8bea2bdd6606b66-Abstract-Conference.html)** — Pretrains EEG models across large, diverse participant and recording configurations.
- **[Riemannian Flow Matching for Brain Connectivity Matrices via Pullback Geometry](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5616112a0120c15bf7d47a6bccc21bc3-Abstract-Conference.html)** — Models brain connectivity matrices through Riemannian flow matching.
- **[S$^2$M-Former: Spiking Symmetric Mixing Branchformer for Brain Auditory Attention Detection](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b8330f5b70b3c53172417deac6f057b1-Abstract-Conference.html)** — Detects auditory attention from brain signals with a spiking mixing architecture.
- **[SPICED: A Synaptic Homeostasis-Inspired Framework for Unsupervised Continual EEG Decoding](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e09a895d25a6444b6bb4b565465e02f0-Abstract-Conference.html)** — Uses synaptic-homeostasis-inspired learning for continual EEG decoding.
- **[SynBrain: Enhancing Visual-to-fMRI Synthesis via Probabilistic Representation Learning](https://proceedings.neurips.cc/paper_files/paper/2025/hash/2a095b46705d7e6f81fc50270fe770c2-Abstract-Conference.html)** — Synthesizes fMRI from visual inputs with probabilistic representation learning.
- **[THD-BAR: Topology Hierarchical Derived Brain Autoregressive Modeling for EEG Generic Representations](https://proceedings.neurips.cc/paper_files/paper/2025/hash/dcf75ae771b21d642c98ce056e745ae7-Abstract-Conference.html)** — Uses hierarchical brain topology for autoregressive EEG pretraining.
- **[ZEBRA: Towards Zero-Shot Cross-Subject Generalization for Universal Brain Visual Decoding](https://proceedings.neurips.cc/paper_files/paper/2025/hash/01c561df365429f33fcd7a7faa44c985-Abstract-Conference.html)** — Studies zero-shot cross-subject generalization for visual decoding from brain activity.

#### 🫀 Physiological Signals & Medical Time Series

- **[A Multimodal BiMamba Network with Test-Time Adaptation for Emotion Recognition Based on Physiological Signals](https://proceedings.neurips.cc/paper_files/paper/2025/hash/d616a353c711f11c722e3f28d2d9e956-Abstract-Conference.html)** — Combines physiological modalities and test-time adaptation for emotion recognition.
- **[CogPhys: Assessing Cognitive Load via Multimodal Remote and Contact-based Physiological Sensing](https://proceedings.neurips.cc/paper_files/paper/2025/hash/014e80b61aca7a85630e6da5d63427c6-Abstract-Datasets_and_Benchmarks_Track.html)** — Measures cognitive load using remote and contact physiological sensing. *[Datasets and Benchmarks]*
- **[egoEMOTION: Egocentric Vision and Physiological Signals for Emotion and Personality Recognition in Real-world Tasks](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b9784f4c3685bebeacd387c4e680b5b2-Abstract-Datasets_and_Benchmarks_Track.html)** — Combines egocentric vision and physiological signals for emotion and personality analysis. *[Datasets and Benchmarks]*
- **[FEEL: Quantifying Heterogeneity in Physiological Signals for Generalizable Emotion Recognition](https://proceedings.neurips.cc/paper_files/paper/2025/hash/e560a0b22e4432003d0dba63ff8dc457-Abstract-Datasets_and_Benchmarks_Track.html)** — Quantifies physiological heterogeneity for generalizable emotion recognition. *[Datasets and Benchmarks]*
- **[GEM: Empowering MLLM for Grounded ECG Understanding with Time Series and Images](https://proceedings.neurips.cc/paper_files/paper/2025/hash/8798321486948322be2b4d658744ba72-Abstract-Conference.html)** — Unifies ECG waveforms, ECG images, and text while linking diagnostic explanations to measurable waveform evidence.
- **[MIRA: Medical Time Series Foundation Model for Real-World Health Data](https://proceedings.neurips.cc/paper_files/paper/2025/hash/8e12ba543adc673da5b89c9311fcf72c-Abstract-Conference.html)** — Pretrains a continuous-time forecasting model to handle irregular sampling, heterogeneous frequencies, and missing observations in medical time series.
- **[MyoChallenge 2024: A New Benchmark for Physiological Dexterity and Agility in Bionic Humans](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5a8f69523f9511a5706568c552de0ebb-Abstract-Datasets_and_Benchmarks_Track.html)** — Benchmarks physiological dexterity and agility in musculoskeletal simulation. *[Datasets and Benchmarks]*
- **[PhysDrive: A Multimodal Remote Physiological Measurement Dataset for In-vehicle Driver Monitoring](https://proceedings.neurips.cc/paper_files/paper/2025/hash/3446e07569081f0f8a144e68bfa7afdf-Abstract-Datasets_and_Benchmarks_Track.html)** — Provides multimodal in-vehicle physiological measurements for driver monitoring. *[Datasets and Benchmarks]*
- **[PhysioWave: A Multi-Scale Wavelet-Transformer for Physiological Signal Representation](https://proceedings.neurips.cc/paper_files/paper/2025/hash/f7a7bb369e48f10e85fce85b67d8c516-Abstract-Conference.html)** — Combines multiscale wavelets and transformers for physiological-signal representations.
- **[SensorLM: Learning the Language of Wearable Sensors](https://proceedings.neurips.cc/paper_files/paper/2025/hash/42cd98f0e7520d4a63c34891ac1c972f-Abstract-Conference.html)** — Learns joint language and wearable-sensor representations.

#### 🏥 Surgical AI

- **[EgoExOR: An Ego-Exo-Centric Operating Room Dataset for Surgical Activity Understanding](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5e3ffa2c53dce23986ca0f8d1d2bbc7e-Abstract-Datasets_and_Benchmarks_Track.html)** — Provides synchronized ego-exocentric operating-room recordings for surgical activity research. *[Datasets and Benchmarks]*
- **[EndoBench: A Comprehensive Evaluation of Multi-Modal Large Language Models for Endoscopy Analysis](https://proceedings.neurips.cc/paper_files/paper/2025/hash/02ff2906a49d985808e7ba8798b9f9cd-Abstract-Datasets_and_Benchmarks_Track.html)** — Benchmarks multimodal language models on endoscopic analysis. *[Datasets and Benchmarks]*
- **[PolypSense3D: A Multi-Source Benchmark Dataset for Depth-Aware Polyp Size Measurement in Endoscopy](https://proceedings.neurips.cc/paper_files/paper/2025/hash/7447a884f2e1f1284530bcbd03379624-Abstract-Datasets_and_Benchmarks_Track.html)** — Benchmarks depth-aware polyp size estimation across endoscopy sources. *[Datasets and Benchmarks]*
- **[SonoGym: High Performance Simulation for Challenging Surgical Tasks with Robotic Ultrasound](https://proceedings.neurips.cc/paper_files/paper/2025/hash/396b1d7ada6d6980d51c81bc5e4da15b-Abstract-Datasets_and_Benchmarks_Track.html)** — Simulates robotic-ultrasound environments for surgical tasks. *[Datasets and Benchmarks]*
- **[Towards Dynamic 3D Reconstruction of Hand-Instrument Interaction in Ophthalmic Surgery](https://proceedings.neurips.cc/paper_files/paper/2025/hash/4c12e97f2e05304a451e18c9c945036f-Abstract-Conference.html)** — Reconstructs dynamic hand-instrument interactions during ophthalmic surgery.

---

### NeurIPS 2024

#### 🔬 Medical Imaging & Segmentation

- **[Addressing Asynchronicity in Clinical Multimodal Fusion via Individualized Chest X-ray Generation](https://proceedings.neurips.cc/paper_files/paper/2024/hash/3310034c97fab48fdbcba18f90fd5364-Abstract-Conference.html)** — Generates individualized chest X-rays to address asynchronous clinical modalities.
- **[A Textbook Remedy for Domain Shifts: Knowledge Priors for Medical Image Analysis](https://proceedings.neurips.cc/paper_files/paper/2024/hash/a4e683f0ce6b91e7fbdae9d32642d88f-Abstract-Conference.html)** ⭐ *Spotlight* — Knowledge-enhanced Bottlenecks (KnoBo) integrate prior medical knowledge from natural language textbooks to improve robustness against domain shifts without additional labeled data.
- **[Autoregressive Image Diffusion: Generation of Image Sequence and Application in MRI](https://proceedings.neurips.cc/paper_files/paper/2024/hash/e93ac11b7e96337962fa38b0460ede3b-Abstract-Conference.html)** — Generates medical image sequences through autoregressive diffusion.
- **[CAT: Coordinating Anatomical-Textual Prompts for Multi-Organ and Tumor Segmentation](https://proceedings.neurips.cc/paper_files/paper/2024/hash/06a52a54c8ee03cd86771136bc91eb1f-Abstract-Conference.html)** — Coordinates anatomical and textual prompts for multi-organ and tumor segmentation.
- **[Copycats: the many lives of a publicly available medical imaging dataset](https://proceedings.neurips.cc/paper_files/paper/2024/hash/cdbeaeb8a0313940a5752c4ec8838ca6-Abstract-Datasets_and_Benchmarks_Track.html)** — Audits reuse and provenance of publicly available medical imaging datasets. *[Datasets and Benchmarks]*
- **[Deep Learning in Medical Image Registration: Magic or Mirage?](https://proceedings.neurips.cc/paper_files/paper/2024/hash/c3fe2a07ec47b89c50e89706d2e23358-Abstract-Conference.html)** — Large-scale empirical study showing classical optimization often outperforms deep learning registration under standard evaluation, reorienting the field's benchmarking practices.
- **[DiffusionBlend: Learning 3D Image Prior through Position-aware Diffusion Score Blending for 3D Computed Tomography Reconstruction](https://proceedings.neurips.cc/paper_files/paper/2024/hash/a30769d9b62c9b94b72e21e0ca73f338-Abstract-Conference.html)** — Blends position-aware diffusion scores for 3D CT reconstruction.
- **[E2ENet: Dynamic Sparse Feature Fusion for Accurate and Efficient 3D Medical Image Segmentation](https://proceedings.neurips.cc/paper_files/paper/2024/hash/d6be2b51b213f4f5994243ccb494d97e-Abstract-Conference.html)** — Fuses sparse features dynamically for efficient volumetric medical segmentation.
- **[Equivariant spatio-hemispherical networks for diffusion MRI deconvolution](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5d4f5a2de6320641566be8722d5f78dc-Abstract-Conference.html)** — Uses hemispherical equivariance for diffusion MRI deconvolution.
- **[MotionTTT: 2D Test-Time-Training Motion Estimation for 3D Motion Corrected MRI](https://proceedings.neurips.cc/paper_files/paper/2024/hash/47a6e9e2c3019f13ad94a0f259fe4970-Abstract-Conference.html)** — Uses inference-time training to estimate motion for corrected 3D MRI reconstruction.
- **[One-to-Multiple: A Progressive Style Transfer Unsupervised Domain-Adaptive Framework for Kidney Tumor Segmentation](https://proceedings.neurips.cc/paper_files/paper/2024/hash/2bd6c9e37df10754a8f5286fca465a80-Abstract-Conference.html)** — Uses progressive one-to-many style transfer for kidney tumor segmentation adaptation.
- **[Samba: Severity-aware Recurrent Modeling for Cross-domain Medical Image Grading](https://proceedings.neurips.cc/paper_files/paper/2024/hash/8aa0c4d28021c0b273480f9e2aab83a6-Abstract-Conference.html)** — Uses severity-aware recurrence for cross-domain medical image grading.
- **[SegVol: Universal and Interactive Volumetric Medical Image Segmentation](https://proceedings.neurips.cc/paper_files/paper/2024/hash/c7c7cf10082e454b9662a686ce6f1b6f-Abstract-Conference.html)** — 3D foundation segmentation model trained on 90K unlabeled + 6K labeled CT volumes supporting 200+ anatomical categories via semantic and spatial prompts, outperforming prior methods by up to 37%.
- **[Sm: enhanced localization in Multiple Instance Learning for medical imaging classification](https://proceedings.neurips.cc/paper_files/paper/2024/hash/8db9279f593652ee9bb2223b4a2c43fa-Abstract-Conference.html)** — Improves localization from multiple-instance medical classification supervision.
- **[Touchstone Benchmark: Are We on the Right Way for Evaluating AI Algorithms for Medical Segmentation?](https://proceedings.neurips.cc/paper_files/paper/2024/hash/1b8726b572e0dfa72793f9f6590664fd-Abstract-Datasets_and_Benchmarks_Track.html)** — Audits evaluation practices for medical segmentation algorithms. *[Datasets and Benchmarks]*

#### 🧫 Computational Pathology & Microscopy

- **[Arctique: An artificial histopathological dataset unifying realism and controllability for uncertainty quantification](https://proceedings.neurips.cc/paper_files/paper/2024/hash/840ba425392fbfede5cf50c755c608c6-Abstract-Datasets_and_Benchmarks_Track.html)** — Provides controllable artificial histopathology data for uncertainty evaluation. *[Datasets and Benchmarks]*
- **[Are nuclear masks all you need for improved out-of-domain generalisation? A closer look at cancer classification in histopathology](https://proceedings.neurips.cc/paper_files/paper/2024/hash/4cc4cc789849230a4f495a2060b45c87-Abstract-Conference.html)** — Studies how nuclei masks affect cancer-classification generalization across pathology domains.
- **[FAST: A Dual-tier Few-Shot Learning Paradigm for Whole Slide Image Classification](https://proceedings.neurips.cc/paper_files/paper/2024/hash/bdcdf38389d7fcefc73c4c3720217155-Abstract-Conference.html)** — Uses a two-tier few-shot strategy for whole-slide classification.
- **[Free Lunch in Pathology Foundation Model: Task-specific Model Adaptation with Concept-Guided Feature Enhancement](https://proceedings.neurips.cc/paper_files/paper/2024/hash/9251fa7fcc356bbfc16c040f4c030d83-Abstract-Conference.html)** — Training-free adaptation strategy injecting task-specific conceptual guidance into pathology foundation models, boosting downstream performance at zero additional cost.
- **[Leveraging Tumor Heterogeneity: Heterogeneous Graph Representation Learning for Cancer Survival Prediction in Whole Slide Images](https://proceedings.neurips.cc/paper_files/paper/2024/hash/760341adc5632de3f1cf2e8d22215a93-Abstract-Conference.html)** — ProtoSurv: heterogeneous graph model capturing spatial interactions among diverse cell populations in WSIs to improve cancer survival prediction.
- **[Micro-Bench: A Microscopy Benchmark for Vision-Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2024/hash/36b31e1bb8ecd4f4081686448e9eff2d-Abstract-Datasets_and_Benchmarks_Track.html)** — Benchmarks vision-language understanding of microscopy images. *[Datasets and Benchmarks]*
- **[MultiOrg: A Multi-rater Organoid-detection Dataset](https://proceedings.neurips.cc/paper_files/paper/2024/hash/addc6188191d8874f3759926bbf45daa-Abstract-Datasets_and_Benchmarks_Track.html)** — Provides a multi-rater organoid-detection dataset. *[Datasets and Benchmarks]*
- **[Rethinking Transformer for Long Contextual Histopathology Whole Slide Image Analysis](https://proceedings.neurips.cc/paper_files/paper/2024/hash/b7eecb72574b043ad0c69ea296212450-Abstract-Conference.html)** — Redesigns token management and attention to handle gigapixel WSIs with very long context windows, enabling slide-level weakly supervised prediction.
- **[SR-CACO-2: A Dataset for Confocal Fluorescence Microscopy Image Super-Resolution](https://proceedings.neurips.cc/paper_files/paper/2024/hash/6e4248741e35ab5dd7b29178633ddc28-Abstract-Datasets_and_Benchmarks_Track.html)** — Provides confocal fluorescence microscopy images for super-resolution. *[Datasets and Benchmarks]*
- **[STimage-1K4M: A histopathology image-gene expression dataset for spatial transcriptomics](https://proceedings.neurips.cc/paper_files/paper/2024/hash/3ef2b740cb22dcce67c20989cb3d3fce-Abstract-Datasets_and_Benchmarks_Track.html)** — Provides paired histopathology images and spatial gene-expression measurements. *[Datasets and Benchmarks]*
- **[xMIL: Insightful Explanations for Multiple Instance Learning in Histopathology](https://proceedings.neurips.cc/paper_files/paper/2024/hash/0f9e0309d8a947ca44463a9b7e8b6a3f-Abstract-Conference.html)** — Extends MIL with concept-based explanations, producing clinically interpretable predictions for biomarker detection and outcome prediction from WSIs.

#### 🤖 Foundation Models & Vision-Language

- **[BenchX: A Unified Benchmark Framework for Medical Vision-Language Pretraining on Chest X-Rays](https://proceedings.neurips.cc/paper_files/paper/2024/hash/0cb35e10bf7bb73d10c12414edbd63fd-Abstract-Datasets_and_Benchmarks_Track.html)** — Provides a unified evaluation framework for chest X-ray vision-language pretraining. *[Datasets and Benchmarks]*
- **[CARES: A Comprehensive Benchmark of Trustworthiness in Medical Vision Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/hash/fde7f40f8ced5735006810534dc66b33-Abstract-Datasets_and_Benchmarks_Track.html)** — Evaluates trustworthiness of medical VLMs across truthfulness, safety, fairness, robustness, and privacy dimensions. *[Datasets and Benchmarks]*
- **[Curriculum Fine-tuning of Vision Foundation Model for Medical Image Classification Under Label Noise](https://proceedings.neurips.cc/paper_files/paper/2024/hash/2093ed77c549eda95bd6f7212b735b43-Abstract-Conference.html)** — Adapts visual foundation models to medical label noise through curriculum learning.
- **[Enhancing vision-language models for medical imaging: bridging the 3D gap with innovative slice selection](https://proceedings.neurips.cc/paper_files/paper/2024/hash/b53513b83232116ae25f57a174a7c993-Abstract-Datasets_and_Benchmarks_Track.html)** — Vote-MI: unsupervised one-pass 2D slice selection that bridges 2D VLMs and 3D medical volumes (CT/MRI) without retraining the VLM. *[Datasets and Benchmarks]*
- **[FairMedFM: Fairness Benchmarking for Medical Imaging Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2024/hash/c9826b9ea5e1b49b256329934a578d83-Abstract-Datasets_and_Benchmarks_Track.html)** — First systematic fairness benchmark evaluating 20 foundation models across 17 medical imaging datasets spanning multiple modalities and sensitive demographic attributes. *[Datasets and Benchmarks]*
- **[FEDMEKI: A Benchmark for Scaling Medical Foundation Models via Federated Knowledge Injection](https://proceedings.neurips.cc/paper_files/paper/2024/hash/0235cbb8cd6425d0b55daefce388fc0b-Abstract-Datasets_and_Benchmarks_Track.html)** — Benchmarks federated knowledge injection into medical foundation models. *[Datasets and Benchmarks]*
- **[G2D: From Global to Dense Radiography Representation Learning via Vision-Language Pre-training](https://proceedings.neurips.cc/paper_files/paper/2024/hash/1ac14e44228aeadabb3c934822c1212a-Abstract-Conference.html)** — Aligns global and local radiographic representations through vision-language pretraining.
- **[HEALNet: Multimodal Fusion for Heterogeneous Biomedical Data](https://proceedings.neurips.cc/paper_files/paper/2024/hash/765871e77d2ca65126d3d64d31aa6908-Abstract-Conference.html)** — Hybrid Early-fusion Attention Learning Network that preserves modality-specific structure while capturing cross-modal interactions and handling missing modalities gracefully.
- **[MDAgents: An Adaptive Collaboration of LLMs for Medical Decision-Making](https://proceedings.neurips.cc/paper_files/paper/2024/hash/90d1fc07f46e31387978b88e7e057a31-Abstract-Conference.html)** — Multi-agent framework that automatically assigns solo or group LLM collaboration structures based on medical task complexity, improving accuracy across diverse clinical benchmarks.
- **[Towards Open Respiratory Acoustic Foundation Models: Pretraining and Benchmarking](https://proceedings.neurips.cc/paper_files/paper/2024/hash/2f803abdcad9de35b45d5a656dade45c-Abstract-Datasets_and_Benchmarks_Track.html)** — Pretrains and benchmarks open respiratory-acoustic foundation models. *[Datasets and Benchmarks]*
- **[Uni-Med: A Unified Medical Generalist Foundation Model For Multi-Task Learning Via Connector-MoE](https://proceedings.neurips.cc/paper_files/paper/2024/hash/941938d6c3c57b4ef4a518965e238a6d-Abstract-Conference.html)** — Connector Mixture-of-Experts (CMoE) bridges a universal visual encoder and an LLM, enabling one model to handle diverse medical imaging tasks without task-specific tuning.

#### 📋 Clinical NLP, EHR & Healthcare

- **[A Decision-Language Model (DLM) for Dynamic Restless Multi-Armed Bandit Tasks in Public Health](https://proceedings.neurips.cc/paper_files/paper/2024/hash/074f42212be2c8ee651db00f17965ec4-Abstract-Conference.html)** — Combines decision models and language for adaptive public-health intervention allocation.
- **[A teacher-teacher framework for clinical language representation learning](https://proceedings.neurips.cc/paper_files/paper/2024/hash/d1ebc73cd4c88866b97a6851ece739d1-Abstract-Conference.html)** — Uses teacher-teacher learning for clinical language representations.
- **[Automated Multi-Task Learning for Joint Disease Prediction on Electronic Health Records](https://proceedings.neurips.cc/paper_files/paper/2024/hash/e955bd39051d4d080826b2ffcf3a7fe2-Abstract-Conference.html)** — Automatically coordinates multiple EHR-based disease-prediction tasks.
- **[Bidirectional Recurrence for Cardiac Motion Tracking with Gaussian Process Latent Coding](https://proceedings.neurips.cc/paper_files/paper/2024/hash/3d77c6dcc7f143aa2154e7f4d5e22d68-Abstract-Conference.html)** — Tracks cardiac motion using bidirectional recurrence and Gaussian-process latent codes.
- **[Biomedical Visual Instruction Tuning with Clinician Preference Alignment](https://proceedings.neurips.cc/paper_files/paper/2024/hash/aec33ab89b5986605cd7c331396e7e5c-Abstract-Datasets_and_Benchmarks_Track.html)** — Aligns biomedical visual instruction tuning with clinician preferences. *[Datasets and Benchmarks]*
- **[Cross-Care: Assessing the Healthcare Implications of Pre-training Data on Language Model Bias](https://proceedings.neurips.cc/paper_files/paper/2024/hash/2a617efee5815f12b405d40569dea0a5-Abstract-Datasets_and_Benchmarks_Track.html)** — Evaluates how pretraining data affect healthcare bias in language models. *[Datasets and Benchmarks]*
- **[DiReCT: Diagnostic Reasoning for Clinical Notes via Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/hash/892850bf793e03b5c410dfd9425b94c8-Abstract-Datasets_and_Benchmarks_Track.html)** — Uses language models to reason diagnostically over clinical notes. *[Datasets and Benchmarks]*
- **[DMNet: Self-comparison Driven Model for Subject-independent Seizure Detection](https://proceedings.neurips.cc/paper_files/paper/2024/hash/3192aa37a2227627d7f8cbf582c075f3-Abstract-Conference.html)** — Uses self-comparison to improve seizure detection across subjects.
- **[EHRCon: Dataset for Checking Consistency between Unstructured Notes and Structured Tables in Electronic Health Records](https://proceedings.neurips.cc/paper_files/paper/2024/hash/a291dad965af9bc2e39ffeb2ca1c6dc0-Abstract-Datasets_and_Benchmarks_Track.html)** — Checks consistency between clinical notes and structured EHR tables. *[Datasets and Benchmarks]*
- **[EHRNoteQA: An LLM Benchmark for Real-World Clinical Practice Using Discharge Summaries](https://proceedings.neurips.cc/paper_files/paper/2024/hash/e15c4afff22f12c4986c1fcb4e941e03-Abstract-Datasets_and_Benchmarks_Track.html)** — Benchmarks realistic clinical questions using discharge summaries. *[Datasets and Benchmarks]*
- **[emg2pose: A Large and Diverse Benchmark for Surface Electromyographic Hand Pose Estimation](https://proceedings.neurips.cc/paper_files/paper/2024/hash/64f8884f6ba3d9ace5bb647c4f917896-Abstract-Datasets_and_Benchmarks_Track.html)** — Provides a surface-EMG benchmark for hand-pose estimation. *[Datasets and Benchmarks]*
- **[emg2qwerty: A Large Dataset with Baselines for Touch Typing using Surface Electromyography](https://proceedings.neurips.cc/paper_files/paper/2024/hash/a64d53074d011e49af1dfc72c332fe4b-Abstract-Datasets_and_Benchmarks_Track.html)** — Provides surface-EMG recordings and baselines for touch typing. *[Datasets and Benchmarks]*
- **[EMGBench: Benchmarking Out-of-Distribution Generalization and Adaptation for Electromyography](https://proceedings.neurips.cc/paper_files/paper/2024/hash/59fe60482e2e5faf557c37d121994663-Abstract-Datasets_and_Benchmarks_Track.html)** — Benchmarks electromyography adaptation and generalization under distribution shifts. *[Datasets and Benchmarks]*
- **[EpiCare: A Reinforcement Learning Benchmark for Dynamic Treatment Regimes](https://proceedings.neurips.cc/paper_files/paper/2024/hash/eb86863306d17c58d18315b5261a4520-Abstract-Datasets_and_Benchmarks_Track.html)** — Benchmarks reinforcement learning for dynamic treatment regimes. *[Datasets and Benchmarks]*
- **[Eye-gaze Guided Multi-modal Alignment for Medical Representation Learning](https://proceedings.neurips.cc/paper_files/paper/2024/hash/0b9536e186a77feff516893a5f393f7a-Abstract-Conference.html)** — Aligns medical modalities through clinician eye-gaze information.
- **[GMAI-MMBench: A Comprehensive Multimodal Evaluation Benchmark Towards General Medical AI](https://proceedings.neurips.cc/paper_files/paper/2024/hash/ab7e02fd60e47e2a379d567f6b54f04e-Abstract-Datasets_and_Benchmarks_Track.html)** — Provides a broad multimodal benchmark for general medical AI. *[Datasets and Benchmarks]*
- **[HEST-1k: A Dataset For Spatial Transcriptomics and Histology Image Analysis](https://proceedings.neurips.cc/paper_files/paper/2024/hash/60a899cc31f763be0bde781a75e04458-Abstract-Datasets_and_Benchmarks_Track.html)** — Pairs spatial transcriptomics with histology for image-based tissue analysis. *[Datasets and Benchmarks]*
- **[Image-aware Evaluation of Generated Medical Reports](https://proceedings.neurips.cc/paper_files/paper/2024/hash/0fbbc5129cafcee8530223b8565561ac-Abstract-Conference.html)** — Evaluates generated medical reports using the corresponding images.
- **[Instruction Tuning Large Language Models to Understand Electronic Health Records](https://proceedings.neurips.cc/paper_files/paper/2024/hash/62986e0a78780fe5f17b495aeded5bab-Abstract-Datasets_and_Benchmarks_Track.html)** — Tunes language models to understand electronic health records through instructions. *[Datasets and Benchmarks]*
- **[Knowledge-Empowered Dynamic Graph Network for Irregularly Sampled Medical Time Series](https://proceedings.neurips.cc/paper_files/paper/2024/hash/7c04aea54c2a60a632a47bd451cd2849-Abstract-Conference.html)** — Models irregular medical time series through knowledge-guided dynamic graphs.
- **[Learning Low-Rank Feature for Thorax Disease Classification](https://proceedings.neurips.cc/paper_files/paper/2024/hash/d4ab6d24758a0fe33604e1f4224ceea1-Abstract-Conference.html)** — Learns low-rank visual features for thoracic disease classification.
- **[MedCalc-Bench: Evaluating Large Language Models for Medical Calculations](https://proceedings.neurips.cc/paper_files/paper/2024/hash/99e81750f3fdfcaf9613db2dbf4bd623-Abstract-Datasets_and_Benchmarks_Track.html)** — Benchmarks language models on medical calculations. *[Datasets and Benchmarks]*
- **[Medformer: A Multi-Granularity Patching Transformer for Medical Time-Series Classification](https://proceedings.neurips.cc/paper_files/paper/2024/hash/3fe2a777282299ecb4f9e7ebb531f0ab-Abstract-Conference.html)** — Transformer tailored for medical time-series (EEG, ECG) using multi-granularity patches to capture local and global temporal patterns, achieving SOTA on multiple clinical benchmarks.
- **[MediQ: Question-Asking LLMs and a Benchmark for Reliable Interactive Clinical Reasoning](https://proceedings.neurips.cc/paper_files/paper/2024/hash/32b80425554e081204e5988ab1c97e9a-Abstract-Conference.html)** — Evaluates interactive clinical reasoning and question asking.
- **[MedJourney: Benchmark and Evaluation of Large Language Models over Patient Clinical Journey](https://proceedings.neurips.cc/paper_files/paper/2024/hash/9f80af32390984cb709cdeb014d0df41-Abstract-Datasets_and_Benchmarks_Track.html)** — Benchmarks language-model reasoning across longitudinal patient journeys. *[Datasets and Benchmarks]*
- **[Med-Real2Sim: Non-Invasive Medical Digital Twins using Physics-Informed Self-Supervised Learning](https://proceedings.neurips.cc/paper_files/paper/2024/hash/0b081a44ed0b8c0c4aa6bd886a60bea4-Abstract-Conference.html)** — Learns virtual patient-specific cardiac simulators from non-invasive echocardiography, predicting pressure-volume loops and enabling personalized digital twins without invasive procedures.
- **[MedSafetyBench: Evaluating and Improving the Medical Safety of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/hash/3ac952d0264ef7a505393868a70a46b6-Abstract-Datasets_and_Benchmarks_Track.html)** — Evaluates and improves medical safety of language-model responses. *[Datasets and Benchmarks]*
- **[PEACE: A Dataset of Pharmaceutical Care for Cancer Pain Analgesia Evaluation and Medication Decision](https://proceedings.neurips.cc/paper_files/paper/2024/hash/26c05ef0790f2a8ad53700e1ef436643-Abstract-Datasets_and_Benchmarks_Track.html)** — Benchmarks pharmaceutical care, analgesia, and medication decisions for cancer pain. *[Datasets and Benchmarks]*
- **[PediatricsGPT: Large Language Models as Chinese Medical Assistants for Pediatric Applications](https://proceedings.neurips.cc/paper_files/paper/2024/hash/fa5b423e24b442180bcd4e13ae75a27f-Abstract-Conference.html)** — Develops a Chinese medical language assistant for pediatric tasks.
- **[Randomized Sparse Matrix Compression for Large-Scale Constrained Optimization in Cancer Radiotherapy](https://proceedings.neurips.cc/paper_files/paper/2024/hash/dd745a0c4f91fe91866fe6788be9cc28-Abstract-Conference.html)** — Compresses sparse optimization problems for large-scale cancer radiotherapy planning.
- **[RoME: A Robust Mixed-Effects Bandit Algorithm for Optimizing Mobile Health Interventions](https://proceedings.neurips.cc/paper_files/paper/2024/hash/e7b3e34d118d1fc6135b0bcbf3254d58-Abstract-Conference.html)** — Optimizes mobile-health interventions with a robust mixed-effects bandit model.
- **[SM3-Text-to-Query: Synthetic Multi-Model Medical Text-to-Query Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/hash/a182a8e6ebc91728b6e6b6382c9f7b1e-Abstract-Datasets_and_Benchmarks_Track.html)** — Benchmarks conversion of medical language to database queries using synthetic data. *[Datasets and Benchmarks]*
- **[SMART: Towards Pre-trained Missing-Aware Model for Patient Health Status Prediction](https://proceedings.neurips.cc/paper_files/paper/2024/hash/751ef1e7f557a8a88f0837b61bf5070f-Abstract-Conference.html)** — Predicts patient health status with missing-aware pretraining.
- **[Towards Multi-dimensional Explanation Alignment for Medical Classification](https://proceedings.neurips.cc/paper_files/paper/2024/hash/ea370419760b421ce12e3082eb2ae1a8-Abstract-Conference.html)** — Aligns multiple dimensions of explanations in medical classification.
- **[Trajectory Flow Matching with Applications to Clinical Time Series Modelling](https://proceedings.neurips.cc/paper_files/paper/2024/hash/c1e67cde895c3c91edb43569ad0df260-Abstract-Conference.html)** — Uses trajectory flow matching to model clinical time series.
- **[UltraMedical: Building Specialized Generalists in Biomedicine](https://proceedings.neurips.cc/paper_files/paper/2024/hash/2dfc26ce9039f00eee4aba0c54931e46-Abstract-Datasets_and_Benchmarks_Track.html)** — Builds specialized biomedical language-model generalists. *[Datasets and Benchmarks]*
- **[Unscrambling disease progression at scale: fast inference of event permutations with optimal transport](https://proceedings.neurips.cc/paper_files/paper/2024/hash/73c362193e3e23188b2a74de7824cc4c-Abstract-Conference.html)** — Infers disease-progression event orders efficiently through optimal transport.

#### 🧠 Neuroimaging, EEG & Brain AI

- **[A scalable generative model for dynamical system reconstruction from neuroimaging data](https://proceedings.neurips.cc/paper_files/paper/2024/hash/9304fe9848ca4db73c79ac0bac414aef-Abstract-Conference.html)** — Reconstructs neuroimaging dynamics with scalable generative modeling.
- **[BrainBits: How Much of the Brain are Generative Reconstruction Methods Using?](https://proceedings.neurips.cc/paper_files/paper/2024/hash/61c00c07e6d27285e4b952e96cc65666-Abstract-Conference.html)** — Measures the contribution of brain information to generative visual reconstruction.
- **[Brain-JEPA: Brain Dynamics Foundation Model with Gradient Positioning and Spatiotemporal Masking](https://proceedings.neurips.cc/paper_files/paper/2024/hash/9c3828adf1500f5de3c56f6550dfe43c-Abstract-Conference.html)** — Pre-trains a model of brain dynamics using gradient positioning and spatiotemporal masking.
- **[Brain Treebank: Large-scale intracranial recordings from naturalistic language stimuli](https://proceedings.neurips.cc/paper_files/paper/2024/hash/aefa2385b3f33abf1526ae4e2c208cd9-Abstract-Datasets_and_Benchmarks_Track.html)** — Provides large-scale intracranial recordings during naturalistic language stimuli. *[Datasets and Benchmarks]*
- **[EEG2Video: Towards Decoding Dynamic Visual Perception from EEG Signals](https://proceedings.neurips.cc/paper_files/paper/2024/hash/84bad835faaf48f24d990072bb5b80ee-Abstract-Conference.html)** — Decodes dynamic visual information from EEG.
- **[EEGPT: Pretrained Transformer for Universal and Reliable Representation of EEG Signals](https://proceedings.neurips.cc/paper_files/paper/2024/hash/4540d267eeec4e5dbd9dae9448f0b739-Abstract-Conference.html)** — Pretrains transformers for generalizable EEG representations.
- **[Exploring the trade-off between deep-learning and explainable models for brain-machine interfaces](https://proceedings.neurips.cc/paper_files/paper/2024/hash/f1cf02ce09757f57c3b93c0db83181e0-Abstract-Conference.html)** — Examines trade-offs between deep and explainable models for brain-machine interfaces.
- **[Few-shot Algorithms for Consistent Neural Decoding (FALCON) Benchmark](https://proceedings.neurips.cc/paper_files/paper/2024/hash/8c2e6bb15be1894b8fb4e0f9bcad1739-Abstract-Datasets_and_Benchmarks_Track.html)** — Benchmarks few-shot methods for consistent neural decoding. *[Datasets and Benchmarks]*
- **[fMRI predictors based on language models of increasing complexity recover brain left lateralization](https://proceedings.neurips.cc/paper_files/paper/2024/hash/e28e19d00b23fe0265f433fa05a96b06-Abstract-Conference.html)** — Studies how language-model complexity relates to fMRI prediction and brain lateralization.
- **[Geodesic Optimization for Predictive Shift Adaptation on EEG data](https://proceedings.neurips.cc/paper_files/paper/2024/hash/399888844ffc8fa95c2db196f3f1b60b-Abstract-Conference.html)** — Adapts EEG models to predictive distribution shifts through geometric optimization.
- **[Long-range Brain Graph Transformer](https://proceedings.neurips.cc/paper_files/paper/2024/hash/2bd3ffba268a2699c212a233ed2907f1-Abstract-Conference.html)** — Models long-range relationships in brain graphs with a transformer.
- **[Neural decoding from stereotactic EEG: accounting for electrode variability across subjects](https://proceedings.neurips.cc/paper_files/paper/2024/hash/c473b9c8897f50203fa23570687c6b30-Abstract-Conference.html)** — Accounts for electrode variability in cross-subject intracranial EEG decoding.
- **[NeuroBOLT: Resting-state EEG-to-fMRI Synthesis with Multi-dimensional Feature Mapping](https://proceedings.neurips.cc/paper_files/paper/2024/hash/29c294ddc628c94cd2c636383ef106c1-Abstract-Conference.html)** — Synthesizes resting-state fMRI from EEG through multidimensional feature mapping.
- **[NeuroClips: Towards High-fidelity and Smooth fMRI-to-Video Reconstruction](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5c594bf6223b67109441c9e0c97542ed-Abstract-Conference.html)** — Reconstructs temporally smooth videos from fMRI.
- **[Neuro-Vision to Language: Enhancing Brain Recording-based Visual Reconstruction and Language Interaction](https://proceedings.neurips.cc/paper_files/paper/2024/hash/b1c62bdeee97b38c34dcda152c829511-Abstract-Conference.html)** — Combines brain-based visual reconstruction with language interaction.
- **[Physics-Regularized Multi-Modal Image Assimilation for Brain Tumor Localization](https://proceedings.neurips.cc/paper_files/paper/2024/hash/49fb58cfd482a33619d48a5c5910cf3c-Abstract-Conference.html)** — Combines physical regularization and multimodal information for brain tumor localization.
- **[Visual Decoding and Reconstruction via EEG Embeddings with Guided Diffusion](https://proceedings.neurips.cc/paper_files/paper/2024/hash/ba5f1233efa77787ff9ec015877dbd1f-Abstract-Conference.html)** — Uses guided diffusion to reconstruct visual stimuli from EEG embeddings.

#### 🫀 Physiological Signals & Medical Time Series

- **[DreamCatcher: A Wearer-aware Multi-modal Sleep Event Dataset Based on Earables in Non-restrictive Environments](https://proceedings.neurips.cc/paper_files/paper/2024/hash/9ab8bb568825d49ce31aa87b7e2f4ad7-Abstract-Datasets_and_Benchmarks_Track.html)** — Provides an earable-based dataset for sleep-event analysis in unconstrained settings. *[Datasets and Benchmarks]*
- **[EEVR: A Dataset of Paired Physiological Signals and Textual Descriptions for Joint Emotion Representation Learning](https://proceedings.neurips.cc/paper_files/paper/2024/hash/1cba8502063fab9df252a63968691768-Abstract-Datasets_and_Benchmarks_Track.html)** — Pairs physiological measurements and text for emotion-representation learning. *[Datasets and Benchmarks]*
- **[FactorizePhys: Matrix Factorization for Multidimensional Attention in Remote Physiological Sensing](https://proceedings.neurips.cc/paper_files/paper/2024/hash/af1c61e4dd59596f033d826419870602-Abstract-Conference.html)** — Uses matrix factorization for multidimensional attention in remote physiological sensing.
- **[Leveraging an ECG Beat Diffusion Model for Morphological Reconstruction from Indirect Signals](https://proceedings.neurips.cc/paper_files/paper/2024/hash/9988f2c8e07c1f98af7ba9ca31ccae0b-Abstract-Conference.html)** — Uses ECG diffusion priors to reconstruct cardiac morphology from indirect signals.
- **[Robust Sleep Staging over Incomplete Multimodal Physiological Signals via Contrastive Imagination](https://proceedings.neurips.cc/paper_files/paper/2024/hash/cb0f9020c00fc52a9f6c9dbfacc6ac58-Abstract-Conference.html)** — Stages sleep under missing physiological modalities through contrastive imagination.
- **[WildPPG: A Real-World PPG Dataset of Long Continuous Recordings](https://proceedings.neurips.cc/paper_files/paper/2024/hash/0433292a3eb101df8f4d72a63f5410d4-Abstract-Datasets_and_Benchmarks_Track.html)** — Provides long, continuous physiological recordings for real-world PPG research. *[Datasets and Benchmarks]*

#### 🏥 Surgical AI

- **[Multi-view Masked Contrastive Representation Learning for Endoscopic Video Analysis](https://proceedings.neurips.cc/paper_files/paper/2024/hash/55cb562b1f5af71f6707f3ff3c7941e6-Abstract-Conference.html)** — Learns endoscopic video representations with multiview masked contrastive training.

---

### NeurIPS 2023

#### 🔬 Medical Imaging & Segmentation

- **[AbdomenAtlas-8K: Annotating 8,000 CT Volumes for Multi-Organ Segmentation in Three Weeks](https://proceedings.neurips.cc/paper_files/paper/2023/hash/7331077e0449e94a91370c46b4f80f57-Abstract-Datasets_and_Benchmarks.html)** — Provides large-scale abdominal CT annotations for multi-organ segmentation. *[Datasets and Benchmarks]*
- **[A case for reframing automated medical image classification as segmentation](https://proceedings.neurips.cc/paper_files/paper/2023/hash/ad6a3bd12095fdca71c306871bdec400-Abstract-Conference.html)** — Examines the benefits of formulating medical classification as segmentation.
- **[Aligning Synthetic Medical Images with Clinical Knowledge using Human Feedback](https://proceedings.neurips.cc/paper_files/paper/2023/hash/2b1d1e5affe5fdb70372cd90dd8afd49-Abstract-Conference.html)** — RLHF-based alignment of generative medical image models to match clinical expert knowledge. *Sun et al.*
- **[Benchmarking Encoder-Decoder Architectures for Biplanar X-ray to 3D Bone Shape Reconstruction](https://proceedings.neurips.cc/paper_files/paper/2023/hash/412732f172bdd5ad0efde2fafa110700-Abstract-Datasets_and_Benchmarks.html)** — Benchmarks reconstruction of 3D bone geometry from biplanar X-rays. *[Datasets and Benchmarks]*
- **[EHRXQA: A Multi-Modal Question Answering Dataset for Electronic Health Records with Chest X-ray Images](https://proceedings.neurips.cc/paper_files/paper/2023/hash/0c007ebef1d11fd48da6ce4f54687db6-Abstract-Datasets_and_Benchmarks.html)** — Combines EHR tables and chest X-rays in multimodal clinical question answering. *[Datasets and Benchmarks]*
- **[Keypoint-Augmented Self-Supervised Learning for Medical Image Segmentation with Limited Annotation](https://proceedings.neurips.cc/paper_files/paper/2023/hash/bee3d6218d7414f8cadfff0eafd0d7be-Abstract-Conference.html)** — Uses anatomical keypoints in self-supervised medical segmentation with limited labels.
- **[Lung250M-4B: A Combined 3D Dataset for CT- and Point Cloud-Based Intra-Patient Lung Registration](https://proceedings.neurips.cc/paper_files/paper/2023/hash/abf37695a4562ac4c05194d717d47eec-Abstract-Datasets_and_Benchmarks.html)** — Provides CT and point-cloud data for intra-patient lung registration. *[Datasets and Benchmarks]*
- **[LVM-Med: Learning Large-Scale Self-Supervised Vision Models for Medical Imaging via Second-order Graph Matching](https://proceedings.neurips.cc/paper_files/paper/2023/hash/58cc11cda2a2679e8af5c6317aed0af8-Abstract-Conference.html)** — Self-supervised pretraining on ~1.3M medical images across 55 datasets using second-order graph matching for semantic structure alignment, achieving 6–7% gains over prior VLMs on challenging tasks.
- **[Quilt-1M: One Million Image-Text Pairs for Histopathology](https://proceedings.neurips.cc/paper_files/paper/2023/hash/775ec578876fa6812c062644964b9870-Abstract-Datasets_and_Benchmarks.html)** — Large-scale histopathology image-text dataset harvested from YouTube educational videos, enabling VL pre-training. *[Datasets and Benchmarks]*
- **[ResoNet: Noise-Trained Physics-Informed MRI Off-Resonance Correction](https://proceedings.neurips.cc/paper_files/paper/2023/hash/2e0bd92a1d3600d4288df51ac5e6be5f-Abstract-Conference.html)** — Uses physics-informed learning for MRI off-resonance correction.
- **[Rethinking Semi-Supervised Medical Image Segmentation: A Variance-Reduction Perspective](https://proceedings.neurips.cc/paper_files/paper/2023/hash/1f7e6d5c84b0ed286d0e69b7d2c79b47-Abstract-Conference.html)** — Studies variance reduction in semi-supervised medical segmentation.
- **[RVD: A Handheld Device-Based Fundus Video Dataset for Retinal Vessel Segmentation](https://proceedings.neurips.cc/paper_files/paper/2023/hash/3a71ee306d6991f2f87dd414e0bdf851-Abstract-Datasets_and_Benchmarks.html)** — Provides handheld fundus videos for retinal vessel segmentation. *[Datasets and Benchmarks]*
- **[Scale-Space Hypernetworks for Efficient Biomedical Image Analysis](https://proceedings.neurips.cc/paper_files/paper/2023/hash/29f421fbdcc82aeb349d784d3aaccdb3-Abstract-Conference.html)** — Uses scale-space hypernetworks for efficient biomedical image analysis.
- **[Spatio-Angular Convolutions for Super-resolution in Diffusion MRI](https://proceedings.neurips.cc/paper_files/paper/2023/hash/294de0fa7149adcb88aa3119c239c63e-Abstract-Conference.html)** — Uses spatio-angular convolutions for diffusion MRI super-resolution.
- **[Towards Generic Semi-Supervised Framework for Volumetric Medical Image Segmentation](https://proceedings.neurips.cc/paper_files/paper/2023/hash/05dc08730e32441edff52b0fa6caab5f-Abstract-Conference.html)** — Studies a general semi-supervised framework for volumetric medical segmentation.

#### 🧫 Computational Pathology & Microscopy

- **[CHAMMI: A benchmark for channel-adaptive models in microscopy imaging](https://proceedings.neurips.cc/paper_files/paper/2023/hash/3ecca655ac67685fdc2155da0eceda6b-Abstract-Datasets_and_Benchmarks.html)** — Benchmarks channel-adaptive representation learning for microscopy images. *[Datasets and Benchmarks]*
- **[DiffInfinite: Large Mask-Image Synthesis via Parallel Random Patch Diffusion in Histopathology](https://proceedings.neurips.cc/paper_files/paper/2023/hash/f64927f5de00c47899e6e58c731966b6-Abstract-Datasets_and_Benchmarks.html)** — Synthesizes large pathology images and masks through parallel patch diffusion. *[Datasets and Benchmarks]*
- **[The Rise of AI Language Pathologists: Exploring Two-level Prompt Learning for Few-shot Weakly-supervised Whole Slide Image Classification](https://proceedings.neurips.cc/paper_files/paper/2023/hash/d599b81036fd1a3b3949b7d444f31082-Abstract-Conference.html)** — Uses hierarchical prompts for few-shot whole-slide classification with weak supervision.

#### 🤖 Foundation Models & Vision-Language

- **[LLaVA-Med: Training a Large Language-and-Vision Assistant for Biomedicine in One Day](https://proceedings.neurips.cc/paper_files/paper/2023/hash/5abcdf8ecdcacba028c6662789194572-Abstract-Datasets_and_Benchmarks.html)** — Curriculum method using GPT-4-generated self-instruction from PubMed figure-caption pairs to align a general VLM to biomedical VQA in under 15 GPU-hours. *[Datasets and Benchmarks]*
- **[Med-UniC: Unifying Cross-Lingual Medical Vision-Language Pre-Training by Diminishing Bias](https://proceedings.neurips.cc/paper_files/paper/2023/hash/af38fb8e90d586f209235c94119ba193-Abstract-Conference.html)** — Reduces cross-language bias in medical vision-language pretraining.
- **[Multimodal Clinical Benchmark for Emergency Care (MC-BEC): A Comprehensive Benchmark for Evaluating Foundation Models in Emergency Medicine](https://proceedings.neurips.cc/paper_files/paper/2023/hash/8f61049e8fe5b9ed714860b951066f1e-Abstract-Datasets_and_Benchmarks.html)** — Benchmarks multimodal foundation models in emergency care. *[Datasets and Benchmarks]*

#### 📋 Clinical NLP, EHR & Healthcare

- **[An Iterative Self-Learning Framework for Medical Domain Generalization](https://proceedings.neurips.cc/paper_files/paper/2023/hash/ac0035c349f3fe8af6a93fe44697b5bd-Abstract-Conference.html)** — Uses iterative self-learning to improve medical domain generalization.
- **[Benchmarking Large Language Models on CMExam - A comprehensive Chinese Medical Exam Dataset](https://proceedings.neurips.cc/paper_files/paper/2023/hash/a48ad12d588c597f4725a8b84af647b5-Abstract-Datasets_and_Benchmarks.html)** — Provides a Chinese medical-examination benchmark for language models. *[Datasets and Benchmarks]*
- **[Contrast Everything: A Hierarchical Contrastive Framework for Medical Time-Series](https://proceedings.neurips.cc/paper_files/paper/2023/hash/ae7d9c77b5ff9e3b7833a68523b880f2-Abstract-Conference.html)** — Learns medical time-series representations through hierarchical contrastive training.
- **[CSMeD: Bridging the Dataset Gap in Automated Citation Screening for Systematic Literature Reviews](https://proceedings.neurips.cc/paper_files/paper/2023/hash/4962a23916103301b27bde29a27642e8-Abstract-Datasets_and_Benchmarks.html)** — Benchmarks automated citation screening for systematic medical literature reviews. *[Datasets and Benchmarks]*
- **[EHRSHOT: An EHR Benchmark for Few-Shot Evaluation of Foundation Models](https://proceedings.neurips.cc/paper_files/paper/2023/hash/d42db1f74df54cb992b3956eb7f15a6f-Abstract-Datasets_and_Benchmarks.html)** — Releases de-identified EHR data for 6,739 Stanford patients with 35 clinical tasks plus a foundation model pretrained on 2.57M patients, enabling few-shot clinical prediction benchmarking. *[Datasets and Benchmarks]*
- **[INSPECT: A Multimodal Dataset for Patient Outcome Prediction of Pulmonary Embolisms](https://proceedings.neurips.cc/paper_files/paper/2023/hash/39736af1b9d87a1fddad9f84a6bcf64c-Abstract-Datasets_and_Benchmarks.html)** — Provides multimodal pulmonary-embolism data for clinical outcome prediction. *[Datasets and Benchmarks]*
- **[Into the Single Cell Multiverse: an End-to-End Dataset for Procedural Knowledge Extraction in Biomedical Texts](https://proceedings.neurips.cc/paper_files/paper/2023/hash/23e3d86c9a19d0caf2ec997e73dfcfbd-Abstract-Datasets_and_Benchmarks.html)** — Provides a dataset for extracting experimental procedures from biomedical text. *[Datasets and Benchmarks]*
- **[Knowledge-based in silico models and dataset for the comparative evaluation of mammography AI for a range of breast characteristics, lesion conspicuities and doses](https://proceedings.neurips.cc/paper_files/paper/2023/hash/75d0956c9594f47bfb86a07bef58d4b0-Abstract-Datasets_and_Benchmarks.html)** — Provides simulated mammography data for controlled evaluation across breast anatomy and radiation dose. *[Datasets and Benchmarks]*
- **[MedSat: A Public Health Dataset for England Featuring Medical Prescriptions and Satellite Imagery](https://proceedings.neurips.cc/paper_files/paper/2023/hash/f4fdf676c3b21f20f8c391d929188386-Abstract-Datasets_and_Benchmarks.html)** — Combines medical prescriptions and satellite observations for public-health analysis. *[Datasets and Benchmarks]*
- **[RaLEs: a Benchmark for Radiology Language Evaluations](https://proceedings.neurips.cc/paper_files/paper/2023/hash/eb5683d06bdef51ed4dff644908eef4b-Abstract-Datasets_and_Benchmarks.html)** — Benchmarks language evaluation for radiology. *[Datasets and Benchmarks]*
- **[REFINE: A Fine-Grained Medication Recommendation System Using Deep Learning and Personalized Drug Interaction Modeling](https://proceedings.neurips.cc/paper_files/paper/2023/hash/4b7439a4ab0b8e4bcb4e2412c6a10a58-Abstract-Conference.html)** — Models personalized drug interactions for fine-grained medication recommendation.
- **[Spatially Resolved Gene Expression Prediction from Histology Images via Bi-modal Contrastive Learning](https://proceedings.neurips.cc/paper_files/paper/2023/hash/df656d6ed77b565e8dcdfbf568aead0a-Abstract-Conference.html)** — Aligns histology and spatial transcriptomics through bimodal contrastive learning.
- **[Temporal Causal Mediation through a Point Process: Direct and Indirect Effects of Healthcare Interventions](https://proceedings.neurips.cc/paper_files/paper/2023/hash/b7d9b1d4a9464d5d1ece82198e351349-Abstract-Conference.html)** — Models direct and mediated effects of healthcare interventions through temporal point processes.
- **[VTaC: A Benchmark Dataset of Ventricular Tachycardia Alarms from ICU Monitors](https://proceedings.neurips.cc/paper_files/paper/2023/hash/7a53bf4e02022aad32a4019d41b3b476-Abstract-Datasets_and_Benchmarks.html)** — Provides annotated ventricular tachycardia alarms from intensive-care monitors. *[Datasets and Benchmarks]*
- **[WBCAtt: A White Blood Cell Dataset Annotated with Detailed Morphological Attributes](https://proceedings.neurips.cc/paper_files/paper/2023/hash/9f34484e5b8d87f09cc58c292a1c9f5d-Abstract-Datasets_and_Benchmarks.html)** — Provides white-blood-cell images annotated with detailed morphological attributes. *[Datasets and Benchmarks]*

#### 🧠 Neuroimaging, EEG & Brain AI

- **[Alleviating the Semantic Gap for Generalized fMRI-to-Image Reconstruction](https://proceedings.neurips.cc/paper_files/paper/2023/hash/3106c718fe84b91fc301fe2f5b738448-Abstract-Conference.html)** — Aligns brain and image semantics for generalizable fMRI reconstruction.
- **[Brain Dissection: fMRI-trained Networks Reveal Spatial Selectivity in the Processing of Natural Images](https://proceedings.neurips.cc/paper_files/paper/2023/hash/90e06fe49254204248cb12562528b952-Abstract-Conference.html)** — Studies visual spatial selectivity using fMRI-trained networks.
- **[Cinematic Mindscapes: High-quality Video Reconstruction from Brain Activity](https://proceedings.neurips.cc/paper_files/paper/2023/hash/4e5e0daf4b05d8bfc6377f33fd53a8f4-Abstract-Conference.html)** — Reconstructs videos from human brain recordings.
- **[Contrast, Attend and Diffuse to Decode High-Resolution Images from Brain Activities](https://proceedings.neurips.cc/paper_files/paper/2023/hash/28dad4a70f748a2980998d3ed0f1b8d2-Abstract-Conference.html)** — Decodes high-resolution images from brain activity with contrastive learning, attention, and diffusion.
- **[CSLP-AE: A Contrastive Split-Latent Permutation Autoencoder Framework for Zero-Shot Electroencephalography Signal Conversion](https://proceedings.neurips.cc/paper_files/paper/2023/hash/2aab54135bd206ef6d4949ce17528d98-Abstract-Conference.html)** — Converts EEG signals through contrastive disentangled latent representations.
- **[DeWave: Discrete Encoding of EEG Waves for EEG to Text Translation](https://proceedings.neurips.cc/paper_files/paper/2023/hash/1f2fd23309a5b2d2537d063b29ec1b52-Abstract-Conference.html)** — Discretizes EEG recordings for brain-to-text translation.
- **[Explainable Brain Age Prediction using coVariance Neural Networks](https://proceedings.neurips.cc/paper_files/paper/2023/hash/92bb2145c74b7d10fbb61aba315b5010-Abstract-Conference.html)** — Predicts brain age with explainable covariance-based neural networks.
- **[Learning Topology-Agnostic EEG Representations with Geometry-Aware Modeling](https://proceedings.neurips.cc/paper_files/paper/2023/hash/a8c893712cb7858e49631fb03c941f8d-Abstract-Conference.html)** — Learns EEG representations across electrode topologies through geometric modeling.
- **[NeuroGraph: Benchmarks for Graph Machine Learning in Brain Connectomics](https://proceedings.neurips.cc/paper_files/paper/2023/hash/14f656f21d09a4114666f60a45aab1aa-Abstract-Datasets_and_Benchmarks.html)** — Benchmarks graph machine learning on brain connectomics. *[Datasets and Benchmarks]*
- **[Plug-and-Play Stability for Intracortical Brain-Computer Interfaces: A One-Year Demonstration of Seamless Brain-to-Text Communication](https://proceedings.neurips.cc/paper_files/paper/2023/hash/83a14a36de4502bac5b580db36e81858-Abstract-Conference.html)** — Studies long-term stability of intracortical brain-to-text communication.
- **[PPi: Pretraining Brain Signal Model for Patient-independent Seizure Detection](https://proceedings.neurips.cc/paper_files/paper/2023/hash/dbeb7e621d4a554069a6a775da0f7273-Abstract-Conference.html)** — Pretrains brain signals for patient-independent seizure detection.
- **[Reconstructing the Mind's Eye: fMRI-to-Image with Contrastive Learning and Diffusion Priors](https://proceedings.neurips.cc/paper_files/paper/2023/hash/4ddab70bf41ffe5d423840644d3357f4-Abstract-Conference.html)** — Combines contrastive representations and diffusion priors for fMRI image reconstruction.
- **[RH-BrainFS: Regional Heterogeneous Multimodal Brain Networks Fusion Strategy](https://proceedings.neurips.cc/paper_files/paper/2023/hash/b9c353d02e565f0f7cba94c4f3584eaa-Abstract-Conference.html)** — Fuses regional heterogeneous multimodal brain networks.
- **[Scaling laws for language encoding models in fMRI](https://proceedings.neurips.cc/paper_files/paper/2023/hash/4533e4a352440a32558c1c227602c323-Abstract-Conference.html)** — Studies scaling behavior of language-based fMRI encoding models.
- **[SwiFT: Swin 4D fMRI Transformer](https://proceedings.neurips.cc/paper_files/paper/2023/hash/8313b1920ee9c78d846c5798c1ce48be-Abstract-Conference.html)** — Uses four-dimensional shifted-window transformers to represent fMRI.
- **[YouTubePD: A Multimodal Benchmark for Parkinson’s Disease Analysis](https://proceedings.neurips.cc/paper_files/paper/2023/hash/acffd5024f52c3a9ecc8ccb4b75b4e5c-Abstract-Datasets_and_Benchmarks.html)** — Provides a multimodal Parkinson's disease benchmark from public video recordings. *[Datasets and Benchmarks]*

#### 🫀 Physiological Signals & Medical Time Series

- **[BIOT: Biosignal Transformer for Cross-data Learning in the Wild](https://proceedings.neurips.cc/paper_files/paper/2023/hash/f6b30f3e2dd9cb53bbf2024402d02295-Abstract-Conference.html)** — Tokenizes biosignals into a shared representation for cross-dataset learning despite mismatched channels, variable recording lengths, and missing values.
- **[Convolution Monge Mapping Normalization for learning on sleep data](https://proceedings.neurips.cc/paper_files/paper/2023/hash/21718991f6acf19a42376b5c7a8668c5-Abstract-Conference.html)** — Normalizes distributions for learning from sleep data with convolutional Monge mappings.
- **[ECG-QA: A Comprehensive Question Answering Dataset Combined With Electrocardiogram](https://proceedings.neurips.cc/paper_files/paper/2023/hash/d0b67349dd16b83b2cf6167fb4e2be50-Abstract-Datasets_and_Benchmarks.html)** — Provides questions paired with ECG recordings for grounded cardiac question answering. *[Datasets and Benchmarks]*
- **[rPPG-Toolbox: Deep Remote PPG Toolbox](https://proceedings.neurips.cc/paper_files/paper/2023/hash/d7d0d548a6317407e02230f15ce75817-Abstract-Datasets_and_Benchmarks.html)** — Provides open tools and benchmarks for deep remote pulse measurement. *[Datasets and Benchmarks]*

#### 🏥 Surgical AI

- **[Text Promptable Surgical Instrument Segmentation with Vision-Language Models](https://proceedings.neurips.cc/paper_files/paper/2023/hash/5af741d487c5f0b08bfe56e11d1883e4-Abstract-Conference.html)** — Segments surgical instruments from text prompts using vision-language models.

---

## ICML

### ICML 2025

#### 🔬 Medical Imaging & Segmentation

- **[Distribution-aware Fairness Learning in Medical Image Segmentation From A Control-Theoretic Perspective](https://proceedings.mlr.press/v267/oh25c.html)** — Studies distribution-aware fairness in medical segmentation using a control-theoretic formulation.
- **[Efficient Noise Calculation in Deep Learning-based MRI Reconstructions](https://proceedings.mlr.press/v267/dalmaz25a.html)** — Improves efficiency of noise estimation in deep MRI reconstruction.
- **[GraphCL: Graph-based Clustering for Semi-Supervised Medical Image Segmentation](https://proceedings.mlr.press/v267/wang25cq.html)** — Uses graph-based clustering to improve semi-supervised medical segmentation.
- **[LangDAug: Langevin Data Augmentation for Multi-Source Domain Generalization in Medical Image Segmentation](https://proceedings.mlr.press/v267/tiwary25a.html)** — Applies Langevin data augmentation to generalize medical segmentation across source domains.
- **[L-Diffusion: Laplace Diffusion for Efficient Pathology Image Segmentation](https://proceedings.mlr.press/v267/li25ea.html)** — Uses Laplace diffusion for efficient pathology image segmentation.
- **[MedRAX: Medical Reasoning Agent for Chest X-ray](https://proceedings.mlr.press/v267/fallahpour25a.html)** — Coordinates reasoning and tools for chest X-ray analysis.
- **[Staged and Physics-Grounded Learning Framework with Hyperintensity Prior for Pre-Contrast MRI Synthesis](https://proceedings.mlr.press/v267/wang25cc.html)** — Synthesizes pre-contrast MRI using staged learning and physical priors.
- **[The Four Color Theorem for Cell Instance Segmentation](https://proceedings.mlr.press/v267/zhang25do.html)** — Uses graph-coloring structure for cell instance segmentation.

#### 🧫 Computational Pathology & Microscopy

- **[Context Matters: Query-aware Dynamic Long Sequence Modeling of Gigapixel Images](https://proceedings.mlr.press/v267/guo25j.html)** — Uses query-aware long-sequence modeling for gigapixel pathology images.
- **[Distributed Parallel Gradient Stacking(DPGS): Solving Whole Slide Image Stacking Challenge in Multi-Instance Learning](https://proceedings.mlr.press/v267/wu25ae.html)** — Scales whole-slide multiple-instance learning through distributed gradient stacking.
- **[Scalable Generation of Spatial Transcriptomics from Histology Images via Whole-Slide Flow Matching](https://proceedings.mlr.press/v267/huang25t.html)** — Predicts spatial transcriptomic information from histology with whole-slide flow matching.
- **[Towards scientific discovery with dictionary learning: Extracting biological concepts from microscopy foundation models](https://proceedings.mlr.press/v267/donhauser25a.html)** — Extracts interpretable biological concepts from microscopy foundation models.
- **[ViTally Consistent: Scaling Biological Representation Learning for Cell Microscopy](https://proceedings.mlr.press/v267/kenyon-dean25a.html)** — Scales representation learning for cell microscopy with consistent vision transformers.

#### 🤖 Foundation Models & Vision-Language

- **[CLIMB: Data Foundations for Large Scale Multimodal Clinical Foundation Models](https://proceedings.mlr.press/v267/dai25b.html)** — Unifies clinical imaging, text, time series, and graph datasets to study multitask pretraining and multimodal transfer.
- **[HealthGPT: A Medical Large Vision-Language Model for Unifying Comprehension and Generation via Heterogeneous Knowledge Adaptation](https://proceedings.mlr.press/v267/lin25n.html)** — Unifies medical visual comprehension and generation through heterogeneous knowledge adaptation.
- **[MMedPO: Aligning Medical Vision-Language Models with Clinical-Aware Multimodal Preference Optimization](https://proceedings.mlr.press/v267/zhu25v.html)** — Weights preference optimization by clinical relevance using plausible hallucinations and lesion-region perturbations to improve image-grounded responses.
- **[Raptor: Scalable Train-Free Embeddings for 3D Medical Volumes Leveraging Pretrained 2D Foundation Models](https://proceedings.mlr.press/v267/an25a.html)** — Builds volumetric embeddings from frozen 2D image encoders and random projections without additional pretraining.
- **[TinyMIG: Transferring Generalization from Vision Foundation Models to Single-Domain Medical Imaging](https://proceedings.mlr.press/v267/liu25cf.html)** — Transfers foundation-model generalization to medical imaging trained on a single domain.

#### 📋 Clinical NLP, EHR & Healthcare

- **[BoxLM: Unifying Structures and Semantics of Medical Concepts for Diagnosis Prediction in Healthcare](https://proceedings.mlr.press/v267/tan25e.html)** — Fuses ontology and EHR hierarchies with language-model semantics through box embeddings for longitudinal diagnosis prediction.
- **[Breaking the Barrier of Hard Samples: A Data-Centric Approach to Synthetic Data for Medical Tasks](https://proceedings.mlr.press/v267/de-souza25a.html)** — Synthesizes challenging medical training examples through a data-centric generation strategy.
- **[Doubly Protected Estimation for Survival Outcomes Utilizing External Controls for Randomized Clinical Trials](https://proceedings.mlr.press/v267/gao25s.html)** — Uses external controls to estimate survival outcomes in randomized clinical trials.
- **[EARTH: Epidemiology-Aware Neural ODE with Continuous Disease Transmission Graph](https://proceedings.mlr.press/v267/wan25b.html)** — Models continuous disease transmission with an epidemiology-aware neural differential equation.
- **[Evaluating LLMs Across Multi-Cognitive Levels: From Medical Knowledge Mastery to Scenario-Based Problem Solving](https://proceedings.mlr.press/v267/zhou25n.html)** — Evaluates medical language models from factual knowledge through clinical scenario reasoning.
- **[Gradient-based Explanations for Deep Learning Survival Models](https://proceedings.mlr.press/v267/langbein25a.html)** — Explains deep survival predictions with gradient-based feature attribution, including multimodal medical data.
- **[iDPA: Instance Decoupled Prompt Attention for Incremental Medical Object Detection](https://proceedings.mlr.press/v267/yi25b.html)** — Uses instance-decoupled prompt attention for incremental medical object detection.
- **[Learn to Vaccinate: Combining Structure Learning and Effective Vaccination for Epidemic and Outbreak Control](https://proceedings.mlr.press/v267/elahi25a.html)** — Combines structure learning and vaccination decisions for epidemic control.
- **[MedXpertQA: Benchmarking Expert-Level Medical Reasoning and Understanding](https://proceedings.mlr.press/v267/zuo25a.html)** — Benchmarks expert-level medical reasoning and multimodal understanding.
- **[Modalities Contribute Unequally: Enhancing Medical Multi-modal Learning through Adaptive Modality Token Re-balancing](https://proceedings.mlr.press/v267/peng25a.html)** — Rebalances modality tokens to account for unequal contributions in medical multimodal learning.
- **[Multimodal Medical Code Tokenizer](https://proceedings.mlr.press/v267/su25b.html)** — Tokenizes medical codes across modalities for unified clinical representations.
- **[NeuralCohort: Cohort-aware Neural Representation Learning for Healthcare Analytics](https://proceedings.mlr.press/v267/liu25cr.html)** — Learns cohort-aware patient representations for healthcare analysis.
- **[Position: Beyond Assistance – Reimagining LLMs as Ethical and Adaptive Co-Creators in Mental Health Care](https://proceedings.mlr.press/v267/badawi25a.html)** — Examines ethical and adaptive roles for language models in mental-health care.
- **[Position: Medical Large Language Model Benchmarks Should Prioritize Construct Validity](https://proceedings.mlr.press/v267/alaa25a.html)** — Argues for construct-valid evaluation of medical language models.
- **[Position: Retrieval-augmented systems can be dangerous medical communicators](https://proceedings.mlr.press/v267/wong25b.html)** — Analyzes medical communication risks introduced by retrieval-augmented systems.
- **[SAFER: A Calibrated Risk-Aware Multimodal Recommendation Model for Dynamic Treatment Regimes](https://proceedings.mlr.press/v267/shen25l.html)** — Recommends dynamic treatment regimes with calibrated risk-aware multimodal modeling.
- **[Unified Screening for Multiple Diseases](https://proceedings.mlr.press/v267/narter25a.html)** — Studies unified screening models for multiple diseases.
- **[Visual and Domain Knowledge for Professional-level Graph-of-Thought Medical Reasoning](https://proceedings.mlr.press/v267/bao25b.html)** — Combines visual evidence and domain knowledge in graph-of-thought medical reasoning.
- **["Why Is There a Tumor?": Tell Me the Reason, Show Me the Evidence](https://proceedings.mlr.press/v267/ma25k.html)** — Links tumor-related diagnostic reasoning to visible supporting evidence.

#### 🧠 Neuroimaging, EEG & Brain AI

- **[Are Large Brainwave Foundation Models Capable Yet ? Insights from Fine-Tuning](https://proceedings.mlr.press/v267/lee25a.html)** — Evaluates fine-tuning strategies for brainwave foundation models.
- **[Causal Invariance-aware Augmentation for Brain Graph Contrastive Learning](https://proceedings.mlr.press/v267/yu25o.html)** — Learns brain graph representations with causal-invariance-aware augmentation.
- **[Do We Really Need Message Passing in Brain Network Modeling?](https://proceedings.mlr.press/v267/yang25r.html)** — Examines the role of message passing in brain network modeling.
- **[Human-Aligned Image Models Improve Visual Decoding from the Brain](https://proceedings.mlr.press/v267/rajabi25a.html)** — Uses human-aligned image models for visual decoding from brain activity.
- **[MindAligner: Explicit Brain Functional Alignment for Cross-Subject Visual Decoding from Limited fMRI Data](https://proceedings.mlr.press/v267/dai25m.html)** — Aligns brain functions across subjects for visual decoding with limited fMRI data.
- **[MindCustomer: Multi-Context Image Generation Blended with Brain Signal](https://proceedings.mlr.press/v267/yu25n.html)** — Conditions image generation on multiple contexts from brain signals.
- **[MindLLM: A Subject-Agnostic and Versatile Model for fMRI-to-text Decoding](https://proceedings.mlr.press/v267/qiu25e.html)** — Decodes text from fMRI with a subject-agnostic language model.
- **[NeuroTree: Hierarchical Functional Brain Pathway Decoding for Mental Health Disorders](https://proceedings.mlr.press/v267/ding25c.html)** — Decodes hierarchical functional brain pathways for mental-health modeling.
- **[Pre-Training Graph Contrastive Masked Autoencoders are Strong Distillers for EEG](https://proceedings.mlr.press/v267/wei25q.html)** — Distills EEG representations using graph contrastive masked autoencoding.

#### 🫀 Physiological Signals & Medical Time Series

- **[Beyond Sensor Data: Foundation Models of Behavioral Data from Wearables Improve Health Predictions](https://proceedings.mlr.press/v267/erturk25a.html)** — Uses wearable behavioral representations to improve health predictions.
- **[Boosting Masked ECG-Text Auto-Encoders as Discriminative Learners](https://proceedings.mlr.press/v267/pham-hung25a.html)** — Improves discriminative ECG representations through masked ECG-text autoencoding.
- **[EEG-Language Pretraining for Highly Label-Efficient Clinical Phenotyping](https://proceedings.mlr.press/v267/gijsen25a.html)** — Aligns EEG segments with clinical report segments to improve label-efficient phenotyping, zero-shot classification, and cross-modal retrieval.
- **[Efficient Personalized Adaptation for Physiological Signal Foundation Model](https://proceedings.mlr.press/v267/wu25ah.html)** — Personalizes pretrained physiological-signal models with efficient adaptation.
- **[From Token to Rhythm: A Multi-Scale Approach for ECG-Language Pretraining](https://proceedings.mlr.press/v267/wang25du.html)** — MELP aligns ECG signals and reports at token, beat, and rhythm levels for transferable cardiac representations.
- **[H-Tuning: Toward Low-Cost and Efficient ECG-based Cardiovascular Disease Detection with Pre-Trained Models](https://proceedings.mlr.press/v267/zhou25aj.html)** — Adapts pretrained models for efficient ECG-based cardiovascular disease detection.

---

### ICML 2024

#### 🔬 Medical Imaging & Segmentation

- **[Adaptive Sampling of k-Space in Magnetic Resonance for Rapid Pathology Prediction](https://proceedings.mlr.press/v235/yen24a.html)** — Selects k-space measurements adaptively for rapid pathology prediction from MRI.
- **[Contextualized Policy Recovery: Modeling and Interpreting Medical Decisions with Adaptive Imitation Learning](https://proceedings.mlr.press/v235/deuschel24a.html)** — Models and interprets clinical policies with contextualized imitation learning.
- **[Robustness of Deep Learning for Accelerated MRI: Benefits of Diverse Training Data](https://proceedings.mlr.press/v235/lin24h.html)** — Evaluates the effect of training-data diversity on accelerated MRI robustness.
- **[Unsupervised Domain Adaptation for Anatomical Structure Detection in Ultrasound Images](https://proceedings.mlr.press/v235/pu24b.html)** — Adapts anatomical structure detection across ultrasound domains without target labels.

#### 📋 Clinical NLP, EHR & Healthcare

- **[Contrastive Learning for Clinical Outcome Prediction with Partial Data Sources](https://proceedings.mlr.press/v235/xia24e.html)** — CLOPPS learns robust cross-modal clinical representations under missing modalities (labs, notes, imaging) via contrastive alignment, enabling strong single-source inference at test time.
- **[ED-Copilot: Reduce Emergency Department Wait Time with Language Model Diagnostic Assistance](https://proceedings.mlr.press/v235/sun24a.html)** — RL-trained LLM that sequentially recommends patient-specific lab tests in the ED to minimize wait time while maximizing diagnostic accuracy, evaluated on a new MIMIC-ED-Assist benchmark.
- **[Exploiting Negative Samples: A Catalyst for Cohort Discovery in Healthcare Analytics](https://proceedings.mlr.press/v235/zheng24c.html)** — Uses negative examples to improve healthcare cohort discovery.
- **[MH-pFLID: Model Heterogeneous personalized Federated Learning via Injection and Distillation for Medical Data Analysis](https://proceedings.mlr.press/v235/xie24h.html)** — Personalizes heterogeneous federated medical models through knowledge injection and distillation.
- **[Multimodal Prototyping for cancer survival prediction](https://proceedings.mlr.press/v235/song24b.html)** — Uses multimodal prototypes for cancer survival prediction.
- **[Position: Reinforcement Learning in Dynamic Treatment Regimes Needs Critical Reexamination](https://proceedings.mlr.press/v235/luo24f.html)** — Critically examines reinforcement learning methods for dynamic treatment regimes.
- **[ProtoGate: Prototype-based Neural Networks with Global-to-local Feature Selection for Tabular Biomedical Data](https://proceedings.mlr.press/v235/jiang24c.html)** — Selects global and local features in tabular biomedical data using prototype-based networks.
- **[Reservoir Computing for Short High-Dimensional Time Series: an Application to SARS-CoV-2 Hospitalization Forecast](https://proceedings.mlr.press/v235/ferte24a.html)** — Forecasts COVID-related hospitalization from short, high-dimensional time series using reservoir computing.
- **[Safe Exploration in Dose Finding Clinical Trials with Heterogeneous Participants](https://proceedings.mlr.press/v235/chien24a.html)** — Balances safety and exploration in dose-finding trials with heterogeneous participants.
- **[Unlocking the Power of Spatial and Temporal Information in Medical Multimodal Pre-training](https://proceedings.mlr.press/v235/yang24v.html)** — Combines spatial and temporal information in medical multimodal pretraining.
- **[WISER: Weak Supervision and Supervised Representation Learning to Improve Drug Response Prediction in Cancer](https://proceedings.mlr.press/v235/shubham24a.html)** — Transfers weakly supervised drug-response representations toward personalized cancer treatment prediction.

#### 🧠 Neuroimaging, EEG & Brain AI

- **[Coprocessor Actor Critic: A Model-Based Reinforcement Learning Approach For Adaptive Brain Stimulation](https://proceedings.mlr.press/v235/pan24g.html)** — Studies adaptive brain stimulation with model-based actor-critic reinforcement learning.
- **[Learning High-Order Relationships of Brain Regions](https://proceedings.mlr.press/v235/qiu24b.html)** — Learns high-order relationships among brain regions.
- **[MindEye2: Shared-Subject Models Enable fMRI-To-Image With 1 Hour of Data](https://proceedings.mlr.press/v235/scotti24a.html)** — Shares information across subjects to decode images from limited fMRI recordings.
- **[Neurodegenerative Brain Network Classification via Adaptive Diffusion with Temporal Regularization](https://proceedings.mlr.press/v235/cho24f.html)** — Classifies neurodegenerative brain networks using temporally regularized adaptive diffusion.
- **[REST: Efficient and Accelerated EEG Seizure Analysis through Residual State Updates](https://proceedings.mlr.press/v235/afzal24a.html)** — Accelerates EEG seizure analysis with residual state updates.
- **[Unsupervised Representation Learning of Brain Activity via Bridging Voxel Activity and Functional Connectivity](https://proceedings.mlr.press/v235/behrouz24a.html)** — Learns brain representations by linking voxel activity with functional connectivity.
- **[Vector Quantization Pretraining for EEG Time Series with Random Projection and Phase Alignment](https://proceedings.mlr.press/v235/gui24a.html)** — Pretrains EEG representations using vector quantization, random projection, and phase alignment.

#### 🫀 Physiological Signals & Medical Time Series

- **[SleepFM: Multi-modal Representation Learning for Sleep Across Brain Activity, ECG and Respiratory Signals](https://proceedings.mlr.press/v235/thapa24a.html)** — Learns multimodal representations from polysomnography using leave-one-out contrastive learning for sleep staging and sleep-disordered breathing detection.
- **[Zero-Shot ECG Classification with Multimodal Learning and Test-time Clinical Knowledge Enhancement](https://proceedings.mlr.press/v235/liu24bg.html)** — Combines multimodal representations and clinical knowledge at inference for zero-shot ECG classification.

---

### ICML 2023

#### 🔬 Medical Imaging & Segmentation

- **[ACAT: Adversarial Counterfactual Attention for Classification and Detection in Medical Imaging](https://proceedings.mlr.press/v202/fontanella23a.html)** — Uses adversarial counterfactual attention for medical image classification and detection.
- **[Evidential Interactive Learning for Medical Image Captioning](https://proceedings.mlr.press/v202/zheng23g.html)** — Uses evidential interaction to guide medical image captioning.

#### 📋 Clinical NLP, EHR & Healthcare

- **[Accounting For Informative Sampling When Learning to Forecast Treatment Outcomes Over Time](https://proceedings.mlr.press/v202/vanderschueren23a.html)** — Accounts for informative sampling when forecasting longitudinal clinical treatment outcomes.
- **[Adaptive Identification of Populations with Treatment Benefit in Clinical Trials: Machine Learning Challenges and Solutions](https://proceedings.mlr.press/v202/curth23a.html)** — Adaptively identifies patient subpopulations that benefit from treatment in clinical trials.
- **[Causal Modeling of Policy Interventions From Treatment-Outcome Sequences](https://proceedings.mlr.press/v202/hizli23a.html)** — Models interventions on treatment policies, including blood-glucose trajectories.
- **[Improving Medical Predictions by Irregular Multimodal Electronic Health Records Modeling](https://proceedings.mlr.press/v202/zhang23v.html)** — Models irregularly sampled multimodal EHR (numerical time series + clinical notes) with a dedicated alignment mechanism, yielding consistent gains on mortality and readmission prediction.
- **[On Heterogeneous Treatment Effects in Heterogeneous Causal Graphs](https://proceedings.mlr.press/v202/watson23a.html)** — Studies treatment-effect heterogeneity in causal graphs motivated by healthcare comorbidity.
- **[Sequential Multi-Dimensional Self-Supervised Learning for Clinical Time Series](https://proceedings.mlr.press/v202/raghu23a.html)** — Learns clinical time-series representations across multiple dimensions through sequential self-supervision.

#### 🧠 Neuroimaging, EEG & Brain AI

- **[Functional Neural Networks: Shift invariant models for functional data with applications to EEG classification](https://proceedings.mlr.press/v202/heinrichs23a.html)** — Models smooth functional signals with shift-invariant networks, including EEG classification.
- **[Sliced-Wasserstein on Symmetric Positive Definite Matrices for M/EEG Signals](https://proceedings.mlr.press/v202/bonet23a.html)** — Compares covariance distributions of M/EEG signals using a sliced-Wasserstein distance on positive-definite matrices.

---

## ICLR

### ICLR 2025

#### 🔬 Medical Imaging & Segmentation

- **[Large-scale and Fine-grained Vision-language Pre-training for Enhanced CT Image Understanding](https://proceedings.iclr.cc/paper_files/paper/2025/hash/3c3b120aae631df27fcd6f94e26615c0-Abstract-Conference.html)** — Fine-grained anatomy-level VL pre-training on 69,086 patients; achieves 81.3% average AUC across 54 CT disease diagnosis tasks. *[Code](https://github.com/alibaba-damo-academy/fvlm)*
- **[LeFusion: Controllable Pathology Synthesis via Lesion-Focused Diffusion Models](https://proceedings.iclr.cc/paper_files/paper/2025/hash/233d16f17f809981763db2f01b7f9603-Abstract-Conference.html)** ⭐ *Spotlight* — Lesion-focused diffusion model that generates lesion-containing image-segmentation pairs from lesion-free scans; validated on cardiac MRI and lung CT. *[Code](https://github.com/HINTLab/LeFusion)*
- **[Moner: Motion Correction in Undersampled Radial MRI with Unsupervised Neural Representation](https://proceedings.iclr.cc/paper_files/paper/2025/hash/b0131b6ee02a00b03fc3320176fec8f5-Abstract-Conference.html)** — Corrects motion in undersampled radial MRI using unsupervised neural representations.
- **[Scale-Aware Contrastive Reverse Distillation for Unsupervised Medical Anomaly Detection](https://proceedings.iclr.cc/paper_files/paper/2025/hash/9d6d351ba8028a50382f42a065d31bf0-Abstract-Conference.html)** — Detects medical image anomalies with scale-aware contrastive reverse distillation.
- **[Score-based Self-supervised MRI Denoising](https://proceedings.iclr.cc/paper_files/paper/2025/hash/fd7b830c1df85211e0710faff9c0adda-Abstract-Conference.html)** — Denoises MRI through score-based self-supervised learning.
- **[Self-Supervised Diffusion MRI Denoising via Iterative and Stable Refinement](https://proceedings.iclr.cc/paper_files/paper/2025/hash/f4cff71af48c5eb8d023c6431135fc64-Abstract-Conference.html)** — Refines diffusion MRI denoising through iterative self-supervised training.
- **[Time-to-Event Pretraining for 3D Medical Imaging](https://proceedings.iclr.cc/paper_files/paper/2025/hash/d0de8a3baf58878e6f479f91dfdc672e-Abstract-Conference.html)** — Pre-trains 3D CT image encoders using time-to-event supervision from paired longitudinal EHR data; improves outcome prediction by 23.7% AUROC.
- **[Unleashing the Potential of Vision-Language Pre-Training for 3D Zero-Shot Lesion Segmentation via Mask-Attribute Alignment](https://proceedings.iclr.cc/paper_files/paper/2025/hash/6111371a868af8dcfba0f96ad9e25ae3-Abstract-Conference.html)** — Cross-modal knowledge injection to align visual lesion features with textual disease descriptions for zero-shot 3D segmentation. *Jiang et al.*

#### 🧫 Computational Pathology & Microscopy

- **[A Multiscale Frequency Domain Causal Framework for Enhanced Pathological Analysis](https://proceedings.iclr.cc/paper_files/paper/2025/hash/22a94399f08a058383e9ef7516ed103f-Abstract-Conference.html)** — Addresses confounding and multiscale feature integration in whole-slide pathology analysis using frequency-domain causal modeling.
- **[Efficient Neuron Segmentation in Electron Microscopy by Affinity-Guided Queries](https://proceedings.iclr.cc/paper_files/paper/2025/hash/86d70cc74581ba2d110f57526ebf2473-Abstract-Conference.html)** — Segments neurons in electron microscopy volumes.
- **[Interpretable Vision-Language Survival Analysis with Ordinal Inductive Bias for Computational Pathology](https://proceedings.iclr.cc/paper_files/paper/2025/hash/f543648b4332a4d8b9e1b72c6b4e2e26-Abstract-Conference.html)** — Combines vision-language representations and ordinal inductive bias for interpretable pathology survival analysis.

#### 🤖 Foundation Models & Vision-Language

- **[Interpretable Bilingual Multimodal Large Language Model for Diverse Biomedical Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/hash/414fd191b3246a19a55741b938380136-Abstract-Conference.html)** — Develops a bilingual biomedical multimodal language model.
- **[MediConfusion: Can you trust your AI radiologist? Probing the reliability of multimodal medical foundation models](https://proceedings.iclr.cc/paper_files/paper/2025/hash/b37c2e26b75ee02fcabd65a2a0367136-Abstract-Conference.html)** — Benchmark revealing that state-of-the-art medical MLLMs perform below random guessing on clinically confusing image pairs.
- **[MedTrinity-25M: A Large-scale Multimodal Dataset with Multigranular Annotations for Medicine](https://proceedings.iclr.cc/paper_files/paper/2025/hash/11c483499c285f30daf832c17dc752bd-Abstract-Conference.html)** — 25M medical image triplets with multigranular annotations; LLaVA-Tri achieves 81.6% on VQA-RAD and 87.8% on SLAKE.
- **[MMed-RAG: Versatile Multimodal RAG System for Medical Vision Language Models](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a559a5a8aa5ae6682ced009ad97cdb16-Abstract-Conference.html)** — Domain-aware retrieval-augmented generation system that improves factual accuracy of medical VLMs by 43.8% across five datasets.
- **[Prompt as Knowledge Bank: Boost Vision-language model via Structural Representation for zero-shot medical detection](https://proceedings.iclr.cc/paper_files/paper/2025/hash/59a9cc95f046e9125d8816ef971873e7-Abstract-Conference.html)** — Uses structured prompt knowledge for zero-shot medical detection.

#### 📋 Clinical NLP, EHR & Healthcare

- **[BoneMet: An Open Large-Scale Multi-Modal Murine Dataset for Breast Cancer Bone Metastasis Diagnosis and Prognosis](https://proceedings.iclr.cc/paper_files/paper/2025/hash/25dbf5a09fbf2553739a04645d3dfb2c-Abstract-Conference.html)** — Provides longitudinal multimodal imaging data from a murine breast-cancer bone-metastasis model for diagnostic and prognostic research.
- **[Conditional Diffusion with Ordinal Regression: Longitudinal Data Generation for Neurodegenerative Disease Studies](https://proceedings.iclr.cc/paper_files/paper/2025/hash/524ef58c2bd075775861234266e5e020-Abstract-Conference.html)** — Generates longitudinal neurodegenerative disease data using diffusion models and ordinal progression information.
- **[Constructing Confidence Intervals for Average Treatment Effects from Multiple Datasets](https://proceedings.iclr.cc/paper_files/paper/2025/hash/e1194b07221de8783a02087bb899d69f-Abstract-Conference.html)** — Combines multiple patient datasets to estimate treatment effects with confidence intervals.
- **[Context Clues: Evaluating Long Context Models for Clinical Prediction Tasks on EHR Data](https://proceedings.iclr.cc/paper_files/paper/2025/hash/2a246ec4437808525a088abae744c2d3-Abstract-Conference.html)** — Evaluates long-context models on clinical prediction tasks using electronic health records.
- **[Differentially private learners for heterogeneous treatment effects](https://proceedings.iclr.cc/paper_files/paper/2025/hash/6baec7c4ba0a8734ccbd528a8090cb1f-Abstract-Conference.html)** — Studies differentially private estimation of heterogeneous treatment effects from patient records.
- **[Diffusion Generative Modeling for Spatially Resolved Gene Expression Inference from Histology Images](https://proceedings.iclr.cc/paper_files/paper/2025/hash/31cc93d156b4ab1514d71ca5147a6e67-Abstract-Conference.html)** — Infers spatially resolved gene expression from histology images using generative diffusion.
- **[Dynamic Modeling of Patients, Modalities and Tasks via Multi-modal Multi-task Mixture of Experts](https://proceedings.iclr.cc/paper_files/paper/2025/hash/e3b82f4c7ba93a88025cf97dca9edc83-Abstract-Conference.html)** — Models patient, modality, and task relationships with multimodal multitask mixture-of-experts learning.
- **[Efficiently Democratizing Medical LLMs for 50 Languages via a Mixture of Language Family Experts](https://proceedings.iclr.cc/paper_files/paper/2025/hash/1551c01d7a3d0bf21e2518331e9f7074-Abstract-Conference.html)** — MoE routing with language-family-specific experts enables high-quality multilingual medical LLMs under data scarcity. *[Code](https://github.com/FreedomIntelligence/ApolloMoE)*
- **[GANDALF: Generative AttentioN based Data Augmentation and predictive modeLing Framework for personalized cancer treatment](https://proceedings.iclr.cc/paper_files/paper/2025/hash/67159f1c0cab15dd34c76a5dd830a389-Abstract-Conference.html)** — Combines generative data augmentation and predictive modeling for personalized cancer treatment.
- **[KGARevion: An AI Agent for Knowledge-Intensive Biomedical QA](https://proceedings.iclr.cc/paper_files/paper/2025/hash/64c43928ae2d9ccea03d893a5edd9cb2-Abstract-Conference.html)** — Improves medical question answering with a knowledge-graph agent.
- **[Learning Causal Alignment for Reliable Disease Diagnosis](https://proceedings.iclr.cc/paper_files/paper/2025/hash/6ce9d51dded7dac82b3b4d3dbb1d73bc-Abstract-Conference.html)** — Aligns diagnostic models with radiologists through causal decision analysis.
- **[Learning General-purpose Biomedical Volume Representations using Randomized Synthesis](https://proceedings.iclr.cc/paper_files/paper/2025/hash/4f693c15f189efd888b6782a5f4eccb1-Abstract-Conference.html)** — Pre-trains representations for biomedical volumes.
- **[Multimodal Lego: Model Merging and Fine-Tuning Across Topologies and Modalities in Biomedicine](https://proceedings.iclr.cc/paper_files/paper/2025/hash/8064e4ebbcbe594628887b420956d8c3-Abstract-Conference.html)** — Combines modalities for biomedical representation learning.
- **[PathGen-1.6M: 1.6 Million Pathology Image-text Pairs Generation through Multi-agent Collaboration](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ebf8764ecf0688cdd9fe1e5a9c525d0d-Abstract-Conference.html)** — Generates pathology image-text pairs through collaborating agents for multimodal pretraining.
- **[Reasoning-Enhanced Healthcare Predictions with Knowledge Graph Community Retrieval](https://proceedings.iclr.cc/paper_files/paper/2025/hash/cb5a3b4589c1a16f14740396625cbfc8-Abstract-Conference.html)** — KARE integrates multi-source medical KG community retrieval with LLM reasoning; outperforms leading models by up to 15% on MIMIC mortality/readmission prediction. *[Code](https://github.com/pat-jj/KARE)*
- **[Reliable and Diverse Evaluation of LLM Medical Knowledge Mastery](https://proceedings.iclr.cc/paper_files/paper/2025/hash/91a5bb5e5939cb075f5f2464d7b8bbf0-Abstract-Conference.html)** — Evaluates medical knowledge mastery with diverse and reliability-oriented tests.
- **[Small Models are LLM Knowledge Triggers for Medical Tabular Prediction](https://proceedings.iclr.cc/paper_files/paper/2025/hash/5c8236f62e33b5224634069e64cb271a-Abstract-Conference.html)** — Uses smaller predictive models to help language models reason over medical tables.

#### 🧠 Neuroimaging, EEG & Brain AI

- **[Adaptive Shrinkage Estimation for Personalized Deep Kernel Regression in Modeling Brain Trajectories](https://proceedings.iclr.cc/paper_files/paper/2025/hash/31994923f58ae5b2d661b300bd439107-Abstract-Conference.html)** — Personalizes regression of brain trajectories.
- **[Animate Your Thoughts: Reconstruction of Dynamic Natural Vision from Human Brain Activity](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a8b148559549ce33261e79b4400e0d77-Abstract-Conference.html)** — Reconstructs dynamic visual experiences from human brain activity.
- **[Biologically Plausible Brain Graph Transformer](https://proceedings.iclr.cc/paper_files/paper/2025/hash/81f19c0e9f3e06c831630ab6662fd8ea-Abstract-Conference.html)** — Uses a biologically informed graph transformer to model brain networks.
- **[BrainOOD: Out-of-distribution Generalizable Brain Network Analysis](https://proceedings.iclr.cc/paper_files/paper/2025/hash/9379ea6ba7a61a402c7750833848b99f-Abstract-Conference.html)** — Studies out-of-distribution generalization for brain networks.
- **[BrainUICL: An Unsupervised Individual Continual Learning Framework for EEG Applications](https://proceedings.iclr.cc/paper_files/paper/2025/hash/deb06c4a6d757b51166fef8ab6c607ec-Abstract-Conference.html)** — Studies continual adaptation of EEG representations across individuals.
- **[CBraMod: A Criss-Cross Brain Foundation Model for EEG Decoding](https://proceedings.iclr.cc/paper_files/paper/2025/hash/bbbd6d915cb90be21c1254a82d45cedd-Abstract-Conference.html)** — Separately models spatial and temporal EEG dependencies with adaptable positional encoding for transfer across clinical and BCI tasks.
- **[Hierarchical Uncertainty Estimation for Learning-based Registration in Neuroimaging](https://proceedings.iclr.cc/paper_files/paper/2025/hash/1f26227c864ebe79ff56a3dcd713f040-Abstract-Conference.html)** — Quantifies uncertainty across scales in learning-based neuroimaging registration.
- **[MindSimulator: Exploring Brain Concept Localization via Synthetic fMRI](https://proceedings.iclr.cc/paper_files/paper/2025/hash/bf121b033db3bac31c3193e8a0dcbf66-Abstract-Conference.html)** — Uses synthetic fMRI to investigate localization of brain concepts.
- **[NeuroLM: A Universal Multi-task Foundation Model for Bridging the Gap between Language and EEG Signals](https://proceedings.iclr.cc/paper_files/paper/2025/hash/8b4add8b0aa8749d80a34ca5d941c355-Abstract-Conference.html)** — Pretrains a multitask EEG foundation model aligned with language.
- **[SIM: Surface-based fMRI Analysis for Inter-Subject Multimodal Decoding from Movie-Watching Experiments](https://proceedings.iclr.cc/paper_files/paper/2025/hash/2d90ba4e432eeff9b8fa975be173ac26-Abstract-Conference.html)** — Studies surface-based fMRI representations for inter-subject multimodal decoding.
- **[SPDIM: Source-Free Unsupervised Conditional and Label Shift Adaptation in EEG](https://proceedings.iclr.cc/paper_files/paper/2025/hash/fc6cd575b8340be6ee70beaed9ca4015-Abstract-Conference.html)** — Adapts EEG models to conditional and label shifts without accessing source data.
- **[Synthesizing Realistic fMRI: A Physiological Dynamics-Driven Hierarchical Diffusion Model for Efficient fMRI Acquisition](https://proceedings.iclr.cc/paper_files/paper/2025/hash/8deff86036ee6a73cda883dc7d2d6b07-Abstract-Conference.html)** — Synthesizes fMRI with a hierarchical diffusion model informed by physiological dynamics.
- **[The Case for Cleaner Biosignals: High-fidelity Neural Compressor Enables Transfer from Cleaner iEEG to Noisier EEG](https://proceedings.iclr.cc/paper_files/paper/2025/hash/28c9ce39a89c03f0bdd9725907d5abbc-Abstract-Conference.html)** — Transfers information from cleaner intracranial recordings to noisier scalp EEG through neural compression.
- **[Toward Generalizing Visual Brain Decoding to Unseen Subjects](https://proceedings.iclr.cc/paper_files/paper/2025/hash/3f9bbf77fbd858e5b6e39d39fe84ed2e-Abstract-Conference.html)** — Studies visual brain decoding that generalizes to previously unseen subjects.
- **[XAIguiFormer: explainable artificial intelligence guided transformer for brain disorder identification](https://proceedings.iclr.cc/paper_files/paper/2025/hash/35023b871910f21b03c379dc90764f0f-Abstract-Conference.html)** — Explains predictions of brain disorders.

#### 🫀 Physiological Signals & Medical Time Series

- **[ECHOPulse: ECG Controlled Echocardio-gram Video Generation](https://proceedings.iclr.cc/paper_files/paper/2025/hash/3929a7785bd56f57edcff0152ab41289-Abstract-Conference.html)** — Generates echocardiography videos conditioned on ECG signals.
- **[PaPaGei: Open Foundation Models for Optical Physiological Signals](https://proceedings.iclr.cc/paper_files/paper/2025/hash/7871f51d332c8661cc729539d7987b21-Abstract-Conference.html)** — Introduces open pretrained representations for optical physiological signals.
- **[Reading Your Heart: Learning ECG Words and Sentences via Pre-training ECG Language Model](https://proceedings.iclr.cc/paper_files/paper/2025/hash/17aa70697d6cd35835f201c6fb0a2fd5-Abstract-Conference.html)** — Learns ECG representations through language-inspired pretraining at multiple signal granularities.
- **[SleepSMC: Ubiquitous Sleep Staging via Supervised Multimodal Coordination](https://proceedings.iclr.cc/paper_files/paper/2025/hash/3ca317b75ddc9dda494185926ee1c025-Abstract-Conference.html)** — Coordinates multiple sensing modalities for sleep staging.

---

### ICLR 2024

#### 🔬 Medical Imaging & Segmentation

- **[FairTune: Optimizing Parameter Efficient Fine Tuning for Fairness in Medical Image Analysis](https://proceedings.iclr.cc/paper_files/paper/2024/hash/da409884a933ecbc4af03338111bf6aa-Abstract-Conference.html)** — Optimizes parameter-efficient adaptation to improve fairness in medical image analysis.
- **[How Well Do Supervised 3D Models Transfer to Medical Imaging Tasks?](https://proceedings.iclr.cc/paper_files/paper/2024/hash/47360925c45a166c96f652589265dee9-Abstract-Conference.html)** — Evaluates transfer of supervised 3D models to medical imaging tasks.
- **[LLM-CXR: Instruction-Finetuned LLM for CXR Image Understanding and Generation](https://proceedings.iclr.cc/paper_files/paper/2024/hash/7f70331dbe58ad59d83941dfa7d975aa-Abstract-Conference.html)** — Unified LLM capable of chest X-ray image understanding, report generation, and image synthesis from text.
- **[The Effect of Intrinsic Dataset Properties on Generalization: Unraveling Learning Differences Between Natural and Medical Images](https://proceedings.iclr.cc/paper_files/paper/2024/hash/5ef6b140c8b6cc2904854e30c6db78eb-Abstract-Conference.html)** — Analyzes how dataset properties affect generalization on natural and medical images.

#### 🧫 Computational Pathology & Microscopy

- **[CAMIL: Context-Aware Multiple Instance Learning for Cancer Detection and Subtyping in Whole Slide Images](https://proceedings.iclr.cc/paper_files/paper/2024/hash/9bbc8b6038603e6170e35f89e3c3e296-Abstract-Conference.html)** — Models contextual relationships among whole-slide patches for cancer detection and subtyping.
- **[Weakly Supervised Virus Capsid Detection with Image-Level Annotations in Electron Microscopy Images](https://proceedings.iclr.cc/paper_files/paper/2024/hash/982ca2640e64bf7a1908b028ebc8734a-Abstract-Conference.html)** — Detects virus capsids in electron microscopy using image-level annotations.

#### 🤖 Foundation Models & Vision-Language

- **[FairSeg: A Large-Scale Medical Image Segmentation Dataset for Fairness Learning Using Segment Anything Model with Fair Error-Bound Scaling](https://proceedings.iclr.cc/paper_files/paper/2024/hash/bfdd520867b56af18dc9e80a8235b887-Abstract-Conference.html)** — Provides a fairness-oriented medical segmentation dataset and error-bound scaling method.

#### 📋 Clinical NLP, EHR & Healthcare

- **[A Flexible Generative Model for Heterogeneous Tabular EHR with Missing Modality](https://proceedings.iclr.cc/paper_files/paper/2024/hash/59e828197370fad05ee2f975b5da6cd9-Abstract-Conference.html)** — Generates heterogeneous tabular EHR data while accounting for missing modalities.
- **[Bayesian Neural Controlled Differential Equations for Treatment Effect Estimation](https://proceedings.iclr.cc/paper_files/paper/2024/hash/e897b4d0914f213896f3e5c25732b1ed-Abstract-Conference.html)** — Estimates treatment effects over continuous time with Bayesian neural controlled differential equations and uncertainty quantification.
- **[Diagnosing Transformers: Illuminating Feature Spaces for Clinical Decision-Making](https://proceedings.iclr.cc/paper_files/paper/2024/hash/fbf1b3765e081251c804da7f508f3b21-Abstract-Conference.html)** — SUFO framework for interpreting fine-tuned transformer feature spaces in high-stakes clinical settings. *Hsu et al.*
- **[Enhancing Small Medical Learners with Privacy-preserving Contextual Prompting](https://proceedings.iclr.cc/paper_files/paper/2024/hash/79322f3668888f8f7fc99bbd98fbbaed-Abstract-Conference.html)** — Uses privacy-preserving contextual prompts to improve smaller medical models.
- **[GraphCare: Enhancing Healthcare Predictions with Personalized Knowledge Graphs](https://proceedings.iclr.cc/paper_files/paper/2024/hash/484d254ff80e99d543159440a06db0de-Abstract-Conference.html)** — Constructs patient-specific knowledge graphs from open biomedical KGs and applies Bi-Attention Augmented GNN, achieving strong clinical prediction performance with dramatically less labeled data.
- **[MOTOR: A Time-to-Event Foundation Model For Structured Medical Records](https://proceedings.iclr.cc/paper_files/paper/2024/hash/b36554b97da741b1c48c9de05c73993e-Abstract-Conference.html)** ⭐ *Spotlight* — Self-supervised TTE foundation model pre-trained on 55M EHR patient records; improves 19 clinical prediction tasks by 4.6% over SOTA with 95% label efficiency.
- **[Multimodal Patient Representation Learning with Missing Modalities and Labels](https://proceedings.iclr.cc/paper_files/paper/2024/hash/f49d76cf84df83a611883c621c96d2d9-Abstract-Conference.html)** — Robust multimodal patient representation learning under realistic conditions of missing modalities and labels.
- **[Prototypical Information Bottlenecking and Disentangling for Multimodal Cancer Survival Prediction](https://proceedings.iclr.cc/paper_files/paper/2024/hash/9ead108421b202494d01b5060d12aa34-Abstract-Conference.html)** — Disentangles multimodal information for cancer survival prediction through an information bottleneck.
- **[Yet Another ICU Benchmark: A Flexible Multi-Center Framework for Clinical ML](https://proceedings.iclr.cc/paper_files/paper/2024/hash/c26a89073d972f2e6643617b0f3a9e8a-Abstract-Conference.html)** — Provides a configurable multicenter benchmark for clinical prediction in intensive care.

#### 🧠 Neuroimaging, EEG & Brain AI

- **[Brain decoding: toward real-time reconstruction of visual perception](https://proceedings.iclr.cc/paper_files/paper/2024/hash/1fb0a4de9c14f5557eeea886e22569cd-Abstract-Conference.html)** — Studies real-time reconstruction of visual perception from brain recordings.
- **[BrainLM: A foundation model for brain activity recordings](https://proceedings.iclr.cc/paper_files/paper/2024/hash/029ce70401321de3808b3ac39e1ab167-Abstract-Conference.html)** — Transformer foundation model pre-trained on 6,700 hours of fMRI data; predicts clinical variables (age, anxiety, PTSD) and generalizes to unseen cohorts. *Caro et al.*
- **[BrainSCUBA: Fine-Grained Natural Language Captions of Visual Cortex Selectivity](https://proceedings.iclr.cc/paper_files/paper/2024/hash/057779005710fdbca7be97667d16047d-Abstract-Conference.html)** — Generates natural-language descriptions of visual cortex selectivity.
- **[Decoding Natural Images from EEG for Object Recognition](https://proceedings.iclr.cc/paper_files/paper/2024/hash/d0865cbe51d35ec322f9af9db7806fc7-Abstract-Conference.html)** — Decodes natural-image information from EEG for object recognition.
- **[Deep Geodesic Canonical Correlation Analysis for Covariance-Based Neuroimaging Data](https://proceedings.iclr.cc/paper_files/paper/2024/hash/9f4d04276a5277b3c8478d05da701bf6-Abstract-Conference.html)** — Aligns covariance-based multimodal neuroimaging representations using geodesic canonical correlation analysis.
- **[Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI](https://proceedings.iclr.cc/paper_files/paper/2024/hash/47393e8594c82ce8fd83adc672cf9872-Abstract-Conference.html)** — LaBraM uses neural spectrum tokenization and masked code prediction to pretrain EEG representations across heterogeneous datasets.

#### 🫀 Physiological Signals & Medical Time Series

- **[Guiding Masked Representation Learning to Capture Spatio-Temporal Relationship of Electrocardiogram](https://proceedings.iclr.cc/paper_files/paper/2024/hash/412fb8623bf8b6d56fb6285ea295447e-Abstract-Conference.html)** — Uses masked representation learning to capture spatial and temporal ECG relationships.
- **[Large-scale Training of Foundation Models for Wearable Biosignals](https://proceedings.iclr.cc/paper_files/paper/2024/hash/0d99a8c048befb6dd6e17d7684adacac-Abstract-Conference.html)** — Pretrains foundation models on large collections of wearable biosignals.

---

### ICLR 2023

#### 🔬 Medical Imaging & Segmentation

- **[3D UX-Net: A Large Kernel Volumetric ConvNet Modernizing Hierarchical Transformer for Medical Image Segmentation](https://openreview.net/forum?id=wsZsjOSytRA)** — Uses large-kernel volumetric convolutions for medical image segmentation.
- **[AE-FLOW: Autoencoders with Normalizing Flows for Medical Images Anomaly Detection](https://openreview.net/forum?id=9OmCr1q54Z)** — Combines autoencoding and normalizing flows for medical image anomaly detection.
- **[DDM$^2$: Self-Supervised Diffusion MRI Denoising with Generative Diffusion Models](https://openreview.net/forum?id=0vqjc50HfcC)** — Denoises diffusion MRI with self-supervised generative diffusion modeling.
- **[MEDFAIR: Benchmarking Fairness for Medical Imaging](https://openreview.net/forum?id=6ve2CkeQe5S)** — Benchmarks demographic fairness in medical image analysis.

#### 🧫 Computational Pathology & Microscopy

- **[Bayes-MIL: A New Probabilistic Perspective on Attention-based Multiple Instance Learning for Whole Slide Images](https://openreview.net/forum?id=_geIwiOyUhZ)** — Models uncertainty in attention-based whole-slide multiple-instance learning.
- **[Exploring Low-Rank Property in Multiple Instance Learning for Whole Slide Image Classification](https://openreview.net/forum?id=01KmhBsEPFO)** — Exploits low-rank structure for multiple-instance whole-slide classification.

#### 🤖 Foundation Models & Vision-Language

- **[Advancing Radiograph Representation Learning with Masked Record Modeling](https://openreview.net/forum?id=w-x7U26GM7j)** — MRM: unified framework that reconstructs masked image patches and masked report tokens as complementary objectives, yielding strong pre-trained radiograph encoders that transfer efficiently with limited labels.
- **[MEDICAL IMAGE UNDERSTANDING WITH PRETRAINED VISION LANGUAGE MODELS: A COMPREHENSIVE STUDY](https://openreview.net/forum?id=txlWziuCE5W)** — Systematic evaluation of pretrained VLMs across 9 medical imaging datasets and 8 adaptation strategies, establishing best practices for medical VLM transfer learning.

#### 📋 Clinical NLP, EHR & Healthcare

- **[Deep Reinforcement Learning for Cost-Effective Medical Diagnosis](https://openreview.net/forum?id=0WVNuEnqVu)** — Learns cost-sensitive sequences of decisions for medical diagnosis through reinforcement learning.
- **[Learning Domain-Agnostic Representation for Disease Diagnosis](https://openreview.net/forum?id=-HHJZlRpGb)** — Learns representations that transfer across domains for disease diagnosis.
- **[ManyDG: Many-domain Generalization for Healthcare Applications](https://openreview.net/forum?id=lcSfirnflpW)** — Addresses generalization across multiple healthcare domains.

#### 🧠 Neuroimaging, EEG & Brain AI

- **[BrainBERT: Self-supervised representation learning for intracranial recordings](https://openreview.net/forum?id=xmcYx_reUn6)** — Learns self-supervised representations of intracranial neural recordings.

#### 🫀 Physiological Signals & Medical Time Series

- **[BSTT: A Bayesian Spatial-Temporal Transformer for Sleep Staging](https://openreview.net/forum?id=ZxdkjTgK_Dl)** — Uses a Bayesian spatial-temporal transformer for sleep staging.

---

## ICCV / ECCV

### ICCV 2025

#### 🔬 Medical Imaging & Segmentation

- **[AcZeroTS: Active Learning for Zero-shot Tissue Segmentation in Pathology Images](https://openaccess.thecvf.com/content/ICCV2025/html/Tang_AcZeroTS_Active_Learning_for_Zero-shot_Tissue_Segmentation_in_Pathology_Images_ICCV_2025_paper.html)** — Actively learns tissue annotations for zero-shot pathology segmentation.
- **[Adaptive Learning of High-Value Regions for Semi-Supervised Medical Image Segmentation](https://openaccess.thecvf.com/content/ICCV2025/html/Lei_Adaptive_Learning_of_High-Value_Regions_for_Semi-Supervised_Medical_Image_Segmentation_ICCV_2025_paper.html)** — Selects valuable regions for semi-supervised medical segmentation.
- **[Alleviating Textual Reliance in Medical Language-guided Segmentation via Prototype-driven Semantic Approximation](https://openaccess.thecvf.com/content/ICCV2025/html/Ye_Alleviating_Textual_Reliance_in_Medical_Language-guided_Segmentation_via_Prototype-driven_Semantic_ICCV_2025_paper.html)** — Reduces over-reliance on language through prototype-driven semantic grounding in medical segmentation.
- **[Breaking Grid Constraints: Dynamic Graph Reconstruction Network for Multi-organ Segmentation](https://openaccess.thecvf.com/content/ICCV2025/html/Xiao_Breaking_Grid_Constraints_Dynamic_Graph_Reconstruction_Network_for_Multi-organ_Segmentation_ICCV_2025_paper.html)** — Reconstructs dynamic graphs for multi-organ segmentation.
- **[COME: Dual Structure-Semantic Learning with Collaborative MoE for Universal Lesion Detection Across Heterogeneous Ultrasound Datasets](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_COME_Dual_Structure-Semantic_Learning_with_Collaborative_MoE_for_Universal_Lesion_ICCV_2025_paper.html)** — Combines structural and semantic experts for lesion detection across ultrasound datasets.
- **[Coordinate-based Speed of Sound Recovery for Aberration-Corrected Photoacoustic Computed Tomography](https://openaccess.thecvf.com/content/ICCV2025/html/Li_Coordinate-based_Speed_of_Sound_Recovery_for_Aberration-Corrected_Photoacoustic_Computed_Tomography_ICCV_2025_paper.html)** — Recovers spatial sound-speed variation for aberration-corrected photoacoustic CT.
- **[CoSMIC: Continual Self-supervised Learning for Multi-Domain Medical Imaging via Conditional Mutual Information Maximization](https://openaccess.thecvf.com/content/ICCV2025/html/Liu_CoSMIC_Continual_Self-supervised_Learning_for_Multi-Domain_Medical_Imaging_via_Conditional_ICCV_2025_paper.html)** — Uses conditional mutual information to retain representations across medical imaging domains.
- **[Debiased Curriculum Adaptation for Safe Transfer Learning in Chest X-ray Classification](https://openaccess.thecvf.com/content/ICCV2025/html/Liu_Debiased_Curriculum_Adaptation_for_Safe_Transfer_Learning_in_Chest_X-ray_ICCV_2025_paper.html)** — Uses debiased curriculum adaptation for safer chest X-ray transfer learning.
- **[FB-Diff: Fourier Basis-guided Diffusion for Temporal Interpolation of 4D Medical Imaging](https://openaccess.thecvf.com/content/ICCV2025/html/You_FB-Diff_Fourier_Basis-guided_Diffusion_for_Temporal_Interpolation_of_4D_Medical_ICCV_2025_paper.html)** — Uses Fourier-guided diffusion to interpolate four-dimensional medical images.
- **[GDKVM: Echocardiography Video Segmentation via Spatiotemporal Key-Value Memory with Gated Delta Rule](https://openaccess.thecvf.com/content/ICCV2025/html/Wang_GDKVM_Echocardiography_Video_Segmentation_via_Spatiotemporal_Key-Value_Memory_with_Gated_ICCV_2025_paper.html)** — Uses gated spatiotemporal key-value memory for echocardiography video segmentation.
- **[Keep Your Friends Close, and Your Enemies Farther: Distance-aware Voxel-wise Contrastive Learning for Semi-supervised Multi-organ Segmentation](https://openaccess.thecvf.com/content/ICCV2025/html/Zhao_Keep_Your_Friends_Close_and_Your_Enemies_Farther_Distance-aware_Voxel-wise_ICCV_2025_paper.html)** — Uses distance-aware voxel contrastive learning for semi-supervised multi-organ segmentation.
- **[MedSegFactory: Text-Guided Generation of Medical Image-Mask Pairs](https://openaccess.thecvf.com/content/ICCV2025/html/Mao_MedSegFactory_Text-Guided_Generation_of_Medical_Image-Mask_Pairs_ICCV_2025_paper.html)** — Generates medical images and masks jointly from textual descriptions.
- **[MRGen: Segmentation Data Engine For Underrepresented MRI Modalities](https://openaccess.thecvf.com/content/ICCV2025/html/Wu_MRGen_Segmentation_Data_Engine_For_Underrepresented_MRI_Modalities_ICCV_2025_paper.html)** — Generates segmentation training data for underrepresented MRI modalities.
- **[MultiverSeg: Scalable Interactive Segmentation of Biomedical Imaging Datasets with In-Context Guidance](https://openaccess.thecvf.com/content/ICCV2025/html/Wong_MultiverSeg_Scalable_Interactive_Segmentation_of_Biomedical_Imaging_Datasets_with_In-Context_ICCV_2025_paper.html)** — Uses in-context guidance to segment biomedical datasets interactively.
- **[Progressive Test Time Energy Adaptation for Medical Image Segmentation](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_Progressive_Test_Time_Energy_Adaptation_for_Medical_Image_Segmentation_ICCV_2025_paper.html)** — Adapts segmentation models progressively at inference through energy-based objectives.
- **[RA-BUSSeg: Relation-aware Semi-supervised Breast Ultrasound Image Segmentation via Adjacent Propagation and Cross-layer Alignment](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_RA-BUSSeg_Relation-aware_Semi-supervised_Breast_Ultrasound_Image_Segmentation_via_Adjacent_Propagation_ICCV_2025_paper.html)** — Models adjacent regions and cross-layer relationships in semi-supervised breast ultrasound segmentation.
- **[Scaling Tumor Segmentation: Best Lessons from Real and Synthetic Data](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_Scaling_Tumor_Segmentation_Best_Lessons_from_Real_and_Synthetic_Data_ICCV_2025_paper.html)** — Analyzes how real and synthetic data scale tumor segmentation.
- **[Seeing the Trees for the Forest: Rethinking Weakly-Supervised Medical Visual Grounding](https://openaccess.thecvf.com/content/ICCV2025/html/Huy_Seeing_the_Trees_for_the_Forest_Rethinking_Weakly-Supervised_Medical_Visual_ICCV_2025_paper.html)** — Studies weakly supervised grounding of medical image findings.
- **[Semantic versus Identity: A Divide-and-Conquer Approach towards Adjustable Medical Image De-Identification](https://openaccess.thecvf.com/content/ICCV2025/html/Tian_Semantic_versus_Identity_A_Divide-and-Conquer_Approach_towards_Adjustable_Medical_Image_ICCV_2025_paper.html)** — Balances patient identity removal and preservation of medical semantics.
- **[Similarity Memory Prior is All You Need for Medical Image Segmentation](https://openaccess.thecvf.com/content/ICCV2025/html/Tang_Similarity_Memory_Prior_is_All_You_Need_for_Medical_Image_ICCV_2025_paper.html)** — Uses similarity-based memory priors for medical segmentation.
- **[SPA: Efficient User-Preference Alignment against Uncertainty in Medical Image Segmentation](https://openaccess.thecvf.com/content/ICCV2025/html/Zhu_SPA_Efficient_User-Preference_Alignment_against_Uncertainty_in_Medical_Image_Segmentation_ICCV_2025_paper.html)** — Aligns medical segmentations with user preferences under uncertainty.
- **[STDDNet: Harnessing Mamba for Video Polyp Segmentation via Spatial-aligned Temporal Modeling and Discriminative Dynamic Representation Learning](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_STDDNet_Harnessing_Mamba_for_Video_Polyp_Segmentation_via_Spatial-aligned_Temporal_ICCV_2025_paper.html)** — Uses state-space temporal modeling for video polyp segmentation.
- **[Structure-aware Semantic Discrepancy and Consistency for 3D Medical Image Self-supervised Learning](https://openaccess.thecvf.com/content/ICCV2025/html/Pan_Structure-aware_Semantic_Discrepancy_and_Consistency_for_3D_Medical_Image_Self-supervised_ICCV_2025_paper.html)** — Uses structural-semantic discrepancies and consistency for 3D medical self-supervision.
- **[Teaching AI the Anatomy Behind the Scan: Addressing Anatomical Flaws in Medical Image Segmentation with Learnable Prior](https://openaccess.thecvf.com/content/ICCV2025/html/Jeon_Teaching_AI_the_Anatomy_Behind_the_Scan_Addressing_Anatomical_Flaws_ICCV_2025_paper.html)** — Learns anatomical priors to reduce structural errors in medical segmentation.
- **[Test-time Adaptation for Foundation Medical Segmentation Model Without Parametric Updates](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_Test-time_Adaptation_for_Foundation_Medical_Segmentation_Model_Without_Parametric_Updates_ICCV_2025_paper.html)** — Adapts medical foundation segmentation models at inference without parameter updates.
- **[UKBOB: One Billion MRI Labeled Masks for Generalizable 3D Medical Image Segmentation](https://openaccess.thecvf.com/content/ICCV2025/html/Bourigault_UKBOB_One_Billion_MRI_Labeled_Masks_for_Generalizable_3D_Medical_ICCV_2025_paper.html)** — Provides large-scale MRI masks for generalizable 3D segmentation.
- **[UniFuse: A Unified All-in-One Framework for Multi-Modal Medical Image Fusion Under Diverse Degradations and Misalignments](https://openaccess.thecvf.com/content/ICCV2025/html/Su_UniFuse_A_Unified_All-in-One_Framework_for_Multi-Modal_Medical_Image_Fusion_ICCV_2025_paper.html)** — Unifies multimodal medical fusion across varying degradation and misregistration conditions.

#### 🧫 Computational Pathology & Microscopy

- **[ASCENT: Annotation-free Self-supervised Contrastive Embeddings for 3D Neuron Tracking in Fluorescence Microscopy](https://openaccess.thecvf.com/content/ICCV2025/html/Han_ASCENT_Annotation-free_Self-supervised_Contrastive_Embeddings_for_3D_Neuron_Tracking_in_ICCV_2025_paper.html)** — Tracks neurons in microscopy recordings.
- **[Bridging Local Inductive Bias and Long-Range Dependencies with Pixel-Mamba for End-to-end Whole Slide Image Analysis](https://openaccess.thecvf.com/content/ICCV2025/html/Qiu_Bridging_Local_Inductive_Bias_and_Long-Range_Dependencies_with_Pixel-Mamba_for_ICCV_2025_paper.html)** — Combines local image structure and long-range state-space modeling for whole-slide analysis.
- **[COIN: Confidence Score-Guided Distillation for Annotation-Free Cell Segmentation](https://openaccess.thecvf.com/content/ICCV2025/html/Jo_COIN_Confidence_Score-Guided_Distillation_for_Annotation-Free_Cell_Segmentation_ICCV_2025_paper.html)** — Distills confidence-guided predictions for cell segmentation without manual annotations.
- **[Continual Multiple Instance Learning with Enhanced Localization for Histopathological Whole Slide Image Analysis](https://openaccess.thecvf.com/content/ICCV2025/html/Lee_Continual_Multiple_Instance_Learning_with_Enhanced_Localization_for_Histopathological_Whole_ICCV_2025_paper.html)** — Improves localization during continual whole-slide multiple-instance learning.
- **[Cracking Instance Jigsaw Puzzles: An Alternative to Multiple Instance Learning for Whole Slide Image Analysis](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_Cracking_Instance_Jigsaw_Puzzles_An_Alternative_to_Multiple_Instance_Learning_ICCV_2025_paper.html)** — Learns whole-slide representations by reconstructing relationships between image instances.
- **[Flow-MIL: Constructing Highly-expressive Latent Feature Space For Whole Slide Image Classification Using Normalizing Flow](https://openaccess.thecvf.com/content/ICCV2025/html/Ma_Flow-MIL_Constructing_Highly-expressive_Latent_Feature_Space_For_Whole_Slide_Image_ICCV_2025_paper.html)** — Uses normalizing flows to model expressive whole-slide classification features.
- **[GECKO: Gigapixel Vision-Concept Contrastive Pretraining in Histopathology](https://openaccess.thecvf.com/content/ICCV2025/html/Kapse_GECKO_Gigapixel_Vision-Concept_Contrastive_Pretraining_in_Histopathology_ICCV_2025_paper.html)** — Pretrains gigapixel pathology representations against visual concepts.
- **[GMMamba: Group Masking Mamba for Whole Slide Image Classification](https://openaccess.thecvf.com/content/ICCV2025/html/Zheng_GMMamba_Group_Masking_Mamba_for_Whole_Slide_Image_Classification_ICCV_2025_paper.html)** — Uses group masking in state-space whole-slide classification.
- **[Graph Domain Adaptation with Dual-branch Encoder and Two-level Alignment for Whole Slide Image-based Survival Prediction](https://openaccess.thecvf.com/content/ICCV2025/html/Shou_Graph_Domain_Adaptation_with_Dual-branch_Encoder_and_Two-level_Alignment_for_ICCV_2025_paper.html)** — Aligns graph representations across domains for whole-slide survival prediction.
- **[How To Make Your Cell Tracker Say "I dunno!"](https://openaccess.thecvf.com/content/ICCV2025/html/Paul_How_To_Make_Your_Cell_Tracker_Say_I_dunno_ICCV_2025_paper.html)** — Models uncertainty in cell tracking.
- **[Integrating Biological Knowledge for Robust Microscopy Image Profiling on De Novo Cell Lines](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_Integrating_Biological_Knowledge_for_Robust_Microscopy_Image_Profiling_on_De_ICCV_2025_paper.html)** — Learns representations of cell lines from microscopy images.
- **[Inverse 3D Microscopy Rendering for Cell Shape Inference with Active Mesh](https://openaccess.thecvf.com/content/ICCV2025/html/Ichbiah_Inverse_3D_Microscopy_Rendering_for_Cell_Shape_Inference_with_Active_ICCV_2025_paper.html)** — Models cell shape in microscopy images.
- **[Normal and Abnormal Pathology Knowledge-Augmented Vision-Language Model for Anomaly Detection in Pathology Images](https://openaccess.thecvf.com/content/ICCV2025/html/Song_Normal_and_Abnormal_Pathology_Knowledge-Augmented_Vision-Language_Model_for_Anomaly_Detection_ICCV_2025_paper.html)** — Ano-NAViLa incorporates descriptions of normal and abnormal tissue to detect and localize pathology anomalies with image-text explanations.
- **[PathDiff: Histopathology Image Synthesis with Unpaired Text and Mask Conditions](https://openaccess.thecvf.com/content/ICCV2025/html/Bhosale_PathDiff_Histopathology_Image_Synthesis_with_Unpaired_Text_and_Mask_Conditions_ICCV_2025_paper.html)** — Learns from unpaired text and mask datasets to generate histopathology images with controllable semantic and spatial content.
- **[PathFinder: A Multi-Modal Multi-Agent System for Medical Diagnostic Decision-Making Applied to Histopathology](https://openaccess.thecvf.com/content/ICCV2025/html/Ghezloo_PathFinder_A_Multi-Modal_Multi-Agent_System_for_Medical_Diagnostic_Decision-Making_Applied_ICCV_2025_paper.html)** — Coordinates triage, navigation, description, and diagnosis agents to inspect whole-slide images and explain diagnostic evidence.
- **[PS3: A Multimodal Transformer Integrating Pathology Reports with Histology Images and Biological Pathways for Cancer Survival Prediction](https://openaccess.thecvf.com/content/ICCV2025/html/Raza_PS3_A_Multimodal_Transformer_Integrating_Pathology_Reports_with_Histology_Images_ICCV_2025_paper.html)** — Integrates pathology reports, whole-slide histology, and pathway information for multimodal cancer prognosis.
- **[Unsupervised Histopathological Image Semantic Segmentation with Overlapping Patches Consistency Constraint](https://openaccess.thecvf.com/content/ICCV2025/html/Cai_Unsupervised_Histopathological_Image_Semantic_Segmentation_with_Overlapping_Patches_Consistency_Constraint_ICCV_2025_paper.html)** — Uses agreement among overlapping patches for unsupervised pathology segmentation.
- **[WSI-LLaVA: A Multimodal Large Language Model for Whole Slide Image](https://openaccess.thecvf.com/content/ICCV2025/html/Liang_WSI-LLaVA_A_Multimodal_Large_Language_Model_for_Whole_Slide_Image_ICCV_2025_paper.html)** — Builds a multimodal language assistant for whole-slide pathology.

#### 🤖 Foundation Models & Vision-Language

- **[Boosting Vision Semantic Density with Anatomy Normality Modeling for Medical Vision-language Pre-training](https://openaccess.thecvf.com/content/ICCV2025/html/Cao_Boosting_Vision_Semantic_Density_with_Anatomy_Normality_Modeling_for_Medical_ICCV_2025_paper.html)** — Uses anatomical normality to strengthen medical image-language semantic alignment.
- **[Derm1M: A Million-scale Vision-Language Dataset Aligned with Clinical Ontology Knowledge for Dermatology](https://openaccess.thecvf.com/content/ICCV2025/html/Yan_Derm1M_A_Million-scale_Vision-Language_Dataset_Aligned_with_Clinical_Ontology_Knowledge_ICCV_2025_paper.html)** — Provides dermatology image-language data aligned with clinical ontology concepts.
- **[GEMeX: A Large-Scale, Groundable, and Explainable Medical VQA Benchmark for Chest X-ray Diagnosis](https://openaccess.thecvf.com/content/ICCV2025/html/Liu_GEMeX_A_Large-Scale_Groundable_and_Explainable_Medical_VQA_Benchmark_for_ICCV_2025_paper.html)** — Pairs chest X-ray questions and answers with visual and textual explanations across multiple question formats.
- **[Learnable Retrieval Enhanced Visual-Text Alignment and Fusion for Radiology Report Generation](https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_Learnable_Retrieval_Enhanced_Visual-Text_Alignment_and_Fusion_for_Radiology_Report_ICCV_2025_paper.html)** — Learns retrieval and image-text alignment jointly for radiology reports.
- **[MaskSAM: Auto-prompt SAM with Mask Classification for Volumetric Medical Image Segmentation](https://openaccess.thecvf.com/content/ICCV2025/html/Xie_MaskSAM_Auto-prompt_SAM_with_Mask_Classification_for_Volumetric_Medical_Image_ICCV_2025_paper.html)** — Automatically generates SAM prompts for volumetric medical segmentation.
- **[Medical World Model](https://openaccess.thecvf.com/content/ICCV2025/html/Yang_Medical_World_Model_ICCV_2025_paper.html)** — Combines vision-language policies, tumor dynamics generation, and survival analysis to simulate treatment-conditioned disease evolution.
- **[ModalTune: Fine-Tuning Slide-Level Foundation Models with Multi-Modal Information for Multi-task Learning in Digital Pathology](https://openaccess.thecvf.com/content/ICCV2025/html/Ramanathan_ModalTune_Fine-Tuning_Slide-Level_Foundation_Models_with_Multi-Modal_Information_for_Multi-task_ICCV_2025_paper.html)** — Adapts slide-level foundation models using multimodal information across pathology tasks.
- **[One Polyp Identifies All: One-Shot Polyp Segmentation with SAM via Cascaded Priors and Iterative Prompt Evolution](https://openaccess.thecvf.com/content/ICCV2025/html/Mao_One_Polyp_Identifies_All_One-Shot_Polyp_Segmentation_with_SAM_via_ICCV_2025_paper.html)** — Segments polyps from one example using SAM, cascaded priors, and iterative prompts.
- **[ProbMED: A Probabilistic Framework for Medical Multimodal Binding](https://openaccess.thecvf.com/content/ICCV2025/html/Gao_ProbMED_A_Probabilistic_Framework_for_Medical_Multimodal_Binding_ICCV_2025_paper.html)** — Aligns chest X-rays, ECGs, echocardiograms, and text as probability distributions to capture many-to-many relationships across clinical modalities.
- **[SAMora: Enhancing SAM through Hierarchical Self-Supervised Pre-Training for Medical Images](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_SAMora_Enhancing_SAM_through_Hierarchical_Self-Supervised_Pre-Training_for_Medical_Images_ICCV_2025_paper.html)** — Pretrains SAM hierarchically on medical images through self-supervision.
- **[Toward Fair and Accurate Cross-Domain Medical Image Segmentation: A VLM-Driven Active Domain Adaptation Paradigm](https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Toward_Fair_and_Accurate_Cross-Domain_Medical_Image_Segmentation_A_VLM-Driven_ICCV_2025_paper.html)** — Combines active adaptation and vision-language representations for fair cross-domain segmentation.
- **[Uncertainty-Driven Expert Control: Enhancing the Reliability of Medical Vision-Language Models](https://openaccess.thecvf.com/content/ICCV2025/html/Liang_Uncertainty-Driven_Expert_Control_Enhancing_the_Reliability_of_Medical_Vision-Language_Models_ICCV_2025_paper.html)** — Uses uncertainty-guided expert control to improve medical vision-language reliability.
- **[Vision-Language Neural Graph Featurization for Extracting Retinal Lesions](https://openaccess.thecvf.com/content/ICCV2025/html/Hassan_Vision-Language_Neural_Graph_Featurization_for_Extracting_Retinal_Lesions_ICCV_2025_paper.html)** — Extracts retinal lesions through image-language graph features.

#### 📋 Clinical NLP, EHR & Healthcare

- **[An OpenMind for 3D Medical Vision Self-supervised Learning](https://openaccess.thecvf.com/content/ICCV2025/html/Wald_An_OpenMind_for_3D_Medical_Vision_Self-supervised_Learning_ICCV_2025_paper.html)** — Pretrains 3D medical visual representations through self-supervision.
- **[C2MIL: Synchronizing Semantic and Topological Causalities in Multiple Instance Learning for Robust and Interpretable Survival Analysis](https://openaccess.thecvf.com/content/ICCV2025/html/Cen_C2MIL_Synchronizing_Semantic_and_Topological_Causalities_in_Multiple_Instance_Learning_ICCV_2025_paper.html)** — Uses multiple-instance learning for patient survival prediction.
- **[Conditional Visual Autoregressive Modeling for Pathological Image Restoration](https://openaccess.thecvf.com/content/ICCV2025/html/Liu_Conditional_Visual_Autoregressive_Modeling_for_Pathological_Image_Restoration_ICCV_2025_paper.html)** — Restores pathology images through conditional visual autoregressive modeling.
- **[Constructing Ophthalmic MLLM for Positioning-diagnosis Collaboration Through Clinical Cognitive Chain Reasoning](https://openaccess.thecvf.com/content/ICCV2025/html/Liu_Constructing_Ophthalmic_MLLM_for_Positioning-diagnosis_Collaboration_Through_Clinical_Cognitive_Chain_ICCV_2025_paper.html)** — Models clinical cognitive chains for coordinated ophthalmic localization and diagnosis.
- **[Controllable Latent Space Augmentation for Digital Pathology](https://openaccess.thecvf.com/content/ICCV2025/html/Boutaj_Controllable_Latent_Space_Augmentation_for_Digital_Pathology_ICCV_2025_paper.html)** — Augments pathology data through controllable latent representations.
- **[Is Visual in-Context Learning for Compositional Medical Tasks within Reach?](https://openaccess.thecvf.com/content/ICCV2025/html/Reiss_Is_Visual_in-Context_Learning_for_Compositional_Medical_Tasks_within_Reach_ICCV_2025_paper.html)** — Evaluates compositional in-context learning in medical visual tasks.
- **[RadGPT: Constructing 3D Image-Text Tumor Datasets](https://openaccess.thecvf.com/content/ICCV2025/html/Bassi_RadGPT_Constructing_3D_Image-Text_Tumor_Datasets_ICCV_2025_paper.html)** — Constructs paired 3D tumor images and descriptive text.
- **[TeethGenerator: A two-stage framework for paired pre- and post-orthodontic 3D dental data generation](https://openaccess.thecvf.com/content/ICCV2025/html/Lei_TeethGenerator_A_two-stage_framework_for_paired_pre-_and_post-orthodontic_3D_ICCV_2025_paper.html)** — Generates paired dental geometries before and after orthodontic treatment.
- **[Towards a Universal 3D Medical Multi-modality Generalization via Learning Personalized Invariant Representation](https://openaccess.thecvf.com/content/ICCV2025/html/Tan_Towards_a_Universal_3D_Medical_Multi-modality_Generalization_via_Learning_Personalized_ICCV_2025_paper.html)** — Learns personalized invariant representations across 3D medical modalities.
- **[Transformer-based Tooth Alignment Prediction with Occlusion and Collision Constraints](https://openaccess.thecvf.com/content/ICCV2025/html/Dong_Transformer-based_Tooth_Alignment_Prediction_with_Occlusion_and_Collision_Constraints_ICCV_2025_paper.html)** — Predicts orthodontic tooth alignment subject to collision and occlusion constraints.
- **[Vector Contrastive Learning For Pixel-Wise Pretraining In Medical Vision](https://openaccess.thecvf.com/content/ICCV2025/html/He_Vector_Contrastive_Learning_For_Pixel-Wise_Pretraining_In_Medical_Vision_ICCV_2025_paper.html)** — Pretrains medical visual features through pixel-level vector contrastive learning.
- **[ViCTr: Vital Consistency Transfer for Pathology Aware Image Synthesis](https://openaccess.thecvf.com/content/ICCV2025/html/Susladkar_ViCTr_Vital_Consistency_Transfer_for_Pathology_Aware_Image_Synthesis_ICCV_2025_paper.html)** — Transfers consistency of disease-related structures during pathology-aware image synthesis.

#### 🧠 Neuroimaging, EEG & Brain AI

- **[Beyond Brain Decoding: Visual-Semantic Reconstructions to Mental Creation Extension Based on fMRI](https://openaccess.thecvf.com/content/ICCV2025/html/Jing_Beyond_Brain_Decoding_Visual-Semantic_Reconstructions_to_Mental_Creation_Extension_Based_ICCV_2025_paper.html)** — Extends fMRI visual decoding toward semantic reconstruction and mental imagery.
- **[Bridging the Gap between Brain and Machine in Interpreting Visual Semantics: Towards Self-adaptive Brain-to-Text Decoding](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_Bridging_the_Gap_between_Brain_and_Machine_in_Interpreting_Visual_ICCV_2025_paper.html)** — Adapts brain-to-text decoding.
- **[CABLD: Contrast-Agnostic Brain Landmark Detection with Consistency-Based Regularization](https://openaccess.thecvf.com/content/ICCV2025/html/Salari_CABLD_Contrast-Agnostic_Brain_Landmark_Detection_with_Consistency-Based_Regularization_ICCV_2025_paper.html)** — Detects anatomical landmarks in brain images.
- **[EEGMirror: Leveraging EEG Data in the Wild via Montage-Agnostic Self-Supervision for EEG to Video Decoding](https://openaccess.thecvf.com/content/ICCV2025/html/Liu_EEGMirror_Leveraging_EEG_Data_in_the_Wild_via_Montage-Agnostic_Self-Supervision_ICCV_2025_paper.html)** — Uses montage-agnostic EEG self-supervision for video decoding across recording settings.
- **[Learn2Synth: Learning Optimal Data Synthesis Using Hypergradients for Brain Image Segmentation](https://openaccess.thecvf.com/content/ICCV2025/html/Hu_Learn2Synth_Learning_Optimal_Data_Synthesis_Using_Hypergradients_for_Brain_Image_ICCV_2025_paper.html)** — Synthesizes training data for brain segmentation with hypergradient optimization.
- **[M-Net: MRI Brain Tumor Sequential Segmentation Network via Mesh-Cast](https://openaccess.thecvf.com/content/ICCV2025/html/Lu_M-Net_MRI_Brain_Tumor_Sequential_Segmentation_Network_via_Mesh-Cast_ICCV_2025_paper.html)** — Uses sequential mesh-based modeling for MRI brain tumor segmentation.
- **[Neurons: Emulating the Human Visual Cortex Improves Fidelity and Interpretability in fMRI-to-Video Reconstruction](https://openaccess.thecvf.com/content/ICCV2025/html/Wang_Neurons_Emulating_the_Human_Visual_Cortex_Improves_Fidelity_and_Interpretability_ICCV_2025_paper.html)** — Incorporates visual-cortex structure into interpretable fMRI video reconstruction.
- **[Neuroverse3D: Developing In-Context Learning Universal Model for Neuroimaging in 3D](https://openaccess.thecvf.com/content/ICCV2025/html/Hu_Neuroverse3D_Developing_In-Context_Learning_Universal_Model_for_Neuroimaging_in_3D_ICCV_2025_paper.html)** — Builds an in-context 3D model for multiple neuroimaging tasks.
- **[Optimal Transport for Brain-Image Alignment: Unveiling Redundancy and Synergy in Neural Information Processing](https://openaccess.thecvf.com/content/ICCV2025/html/Xiao_Optimal_Transport_for_Brain-Image_Alignment_Unveiling_Redundancy_and_Synergy_in_ICCV_2025_paper.html)** — Aligns images with brain activity representations.

#### 🫀 Physiological Signals & Medical Time Series

- **[egoPPG: Heart Rate Estimation from Eye-Tracking Cameras in Egocentric Systems to Benefit Downstream Vision Tasks](https://openaccess.thecvf.com/content/ICCV2025/html/Braun_egoPPG_Heart_Rate_Estimation_from_Eye-Tracking_Cameras_in_Egocentric_Systems_ICCV_2025_paper.html)** — Measures heart rate through eye-tracking cameras in egocentric systems.
- **[FusionPhys: A Flexible Framework for Fusing Complementary Sensing Modalities in Remote Physiological Measurement](https://openaccess.thecvf.com/content/ICCV2025/html/Ying_FusionPhys_A_Flexible_Framework_for_Fusing_Complementary_Sensing_Modalities_in_ICCV_2025_paper.html)** — Fuses complementary sensing modalities for remote physiological measurements.
- **[RhythmGuassian: Repurposing Generalizable Gaussian Model For Remote Physiological Measurement](https://openaccess.thecvf.com/content/ICCV2025/html/Lu_RhythmGuassian_Repurposing_Generalizable_Gaussian_Model_For_Remote_Physiological_Measurement_ICCV_2025_paper.html)** — Adapts generalizable Gaussian models for remote vital-sign measurement.
- **[Spatial Alignment and Temporal Matching Adapter for Video-Radar Remote Physiological Measurement](https://openaccess.thecvf.com/content/ICCV2025/html/Liang_Spatial_Alignment_and_Temporal_Matching_Adapter_for_Video-Radar_Remote_Physiological_ICCV_2025_paper.html)** — Aligns video and radar information across space and time for physiological measurement.

#### 🏥 Surgical AI

- **[MedVSR: Medical Video Super-Resolution with Cross State-Space Propagation](https://openaccess.thecvf.com/content/ICCV2025/html/Liu_MedVSR_Medical_Video_Super-Resolution_with_Cross_State-Space_Propagation_ICCV_2025_paper.html)** — Uses state-space propagation and reconstruction to improve medical video resolution under noise, camera motion, and abrupt transitions.
- **[MetaScope: Optics-Driven Neural Network for Ultra-Micro Metalens Endoscopy](https://openaccess.thecvf.com/content/ICCV2025/html/Li_MetaScope_Optics-Driven_Neural_Network_for_Ultra-Micro_Metalens_Endoscopy_ICCV_2025_paper.html)** — Combines optical modeling and neural reconstruction for miniature metalens endoscopy.
- **[OphCLIP: Hierarchical Retrieval-Augmented Learning for Ophthalmic Surgical Video-Language Pretraining](https://openaccess.thecvf.com/content/ICCV2025/html/Hu_OphCLIP_Hierarchical_Retrieval-Augmented_Learning_for_Ophthalmic_Surgical_Video-Language_Pretraining_ICCV_2025_paper.html)** — Learns from hierarchical ophthalmic video-text annotations and retrieved silent videos for surgical phase and instrument recognition.

---

### ECCV 2024

#### 🔬 Medical Imaging & Segmentation

- **[A Cephalometric Landmark Regression Method based on Dual-encoder for High-resolution X-ray Image](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/4167_ECCV_2024_paper.php)** — Regresses cephalometric landmarks from high-resolution dental X-rays with dual encoders.
- **[Adaptive Correspondence Scoring for Unsupervised Medical Image Registration](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5502_ECCV_2024_paper.php)** — Scores correspondences adaptively for unsupervised medical registration.
- **[Alternate Diverse Teaching for Semi-supervised Medical Image Segmentation](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/764_ECCV_2024_paper.php)** — Alternates diverse teacher models for semi-supervised medical segmentation.
- **[AnatoMask: Enhancing Medical Image Segmentation with Reconstruction-guided Self-masking](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/7731_ECCV_2024_paper.php)** — Anatomy-aware masked image modeling for self-supervised 3D medical image segmentation; dynamically masks anatomically significant regions via reconstruction loss.
- **[CardiacNet: Learning to Reconstruct Abnormalities for Cardiac Disease Assessment from Echocardiogram Videos](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3391_ECCV_2024_paper.php)** — Learns echocardiographic disease representations by reconstructing cardiac abnormalities.
- **[ChEX: Interactive Localization and Region Description in Chest X-rays](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3114_ECCV_2024_paper.php)** — Localizes and describes chest X-ray regions through interactive queries.
- **[DiffuX2CT: Diffusion Learning to Reconstruct CT Images from Biplanar X-Rays](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6022_ECCV_2024_paper.php)** — Reconstructs CT volumes from biplanar X-rays using diffusion.
- **[Effective Lymph Nodes Detection in CT Scans Using Location Debiased Query Selection and Contrastive Query Representation in Transformer](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5850_ECCV_2024_paper.php)** — Uses location-debiased queries and contrastive representations for lymph-node detection in CT.
- **[Energy-induced Explicit quantification for Multi-modality MRI fusion](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/1183_ECCV_2024_paper.php)** — Quantifies energy information for multimodal MRI fusion.
- **[FairDomain: Achieving Fairness in Cross-Domain Medical Image Segmentation and Classification](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/9771_ECCV_2024_paper.php)** — Studies fairness under domain shifts in medical image classification and segmentation.
- **[GenerateCT: Text-Conditional Generation of 3D Chest CT Volumes](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/10147_ECCV_2024_paper.php)** — Generates 3D chest CT volumes conditioned on text.
- **[Gradient-Aware for Class-Imbalanced Semi-supervised Medical Image Segmentation](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/7246_ECCV_2024_paper.php)** — Uses gradient information to address class imbalance in semi-supervised medical segmentation.
- **[Identity-Consistent Diffusion Network for Grading Knee Osteoarthritis Progression in Radiographic Imaging](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/11241_ECCV_2024_paper.php)** — Models consistent subject identity when predicting knee osteoarthritis progression from radiographs.
- **[I-MedSAM: Implicit Medical Image Segmentation with Segment Anything](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/1503_ECCV_2024_paper.php)** — Extends SAM to medical images via implicit neural representations that model continuous anatomical boundaries, enabling high-resolution segmentation without resolution-dependent retraining.
- **[NePhi: Neural Deformation Fields for Approximately Diffeomorphic Medical Image Registration](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/12148_ECCV_2024_paper.php)** — Memory-efficient neural deformation fields for large-scale 3D medical image registration.
- **[Plug-and-Play Learned Proximal Trajectory for 3D Sparse-View X-Ray Computed Tomography](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5164_ECCV_2024_paper.php)** — Learns proximal reconstruction trajectories for sparse-view 3D CT.
- **[PMT: Progressive Mean Teacher via Exploring Temporal Consistency for Semi-Supervised Medical Image Segmentation](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/8535_ECCV_2024_paper.php)** — Uses a progressive mean-teacher strategy and temporal consistency for semi-supervised medical segmentation.
- **[Radiative Gaussian Splatting for Efficient X-ray Novel View Synthesis](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/111_ECCV_2024_paper.php)** — Models X-ray rendering with Gaussian representations for novel-view synthesis.
- **[Rethinking Deep Unrolled Model for Accelerated MRI Reconstruction](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/9565_ECCV_2024_paper.php)** — Reassesses deep unrolled models for accelerated MRI reconstruction.
- **[ScribblePrompt: Fast and Flexible Interactive Segmentation for Any Biomedical Image](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5664_ECCV_2024_paper.php)** — Interactive segmentation network trained on 65,000+ scribble annotations across 54,000+ images, outperforming SAM and specialist models using scribbles, clicks, or bounding boxes on diverse biomedical images.
- **[The Devil is in the Statistics: Mitigating and Exploiting Statistics Difference for Generalizable Semi-supervised Medical Image Segmentation](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/7047_ECCV_2024_paper.php)** — Studies distributional statistics in generalizable semi-supervised medical segmentation.
- **[Unified Medical Image Pre-training in Language-Guided Common Semantic Space](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/10510_ECCV_2024_paper.php)** — Pretrains medical images in a shared language-guided semantic space.
- **[Unsupervised Multi-modal Medical Image Registration via Invertible Translation](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/4467_ECCV_2024_paper.php)** — Registers medical modalities through invertible cross-modal translation.

#### 🧫 Computational Pathology & Microscopy

- **[Attention-Challenging Multiple Instance Learning for Whole Slide Image Classification](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6954_ECCV_2024_paper.php)** — Challenges attention selection during whole-slide multiple-instance learning.
- **[Co-synthesis of Histopathology Nuclei Image-Label Pairs using a Context-Conditioned Joint Diffusion Model](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/2037_ECCV_2024_paper.php)** — Generates paired nuclei images and labels with context-conditioned diffusion.
- **[denoiSplit: a method for joint microscopy image splitting and unsupervised denoising](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3482_ECCV_2024_paper.php)** — Separates and denoises overlapping microscopy image channels.
- **[DGR-MIL: Exploring Diverse Global Representation in Multiple Instance Learning for Whole Slide Image Classification](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5548_ECCV_2024_paper.php)** — Learns diverse global slide representations for multiple-instance classification.
- **[Knowledge-enhanced Visual-Language Pretraining for Computational Pathology](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6901_ECCV_2024_paper.php)** — Adds pathology knowledge to vision-language pretraining.
- **[Large-Scale Multi-Hypotheses Cell Tracking Using Ultrametric Contours Maps](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/10114_ECCV_2024_paper.php)** — Tracks multiple cell hypotheses using hierarchical contour representations.
- **[Norma: A Noise Robust Memory-Augmented Framework for Whole Slide Image Classification](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6825_ECCV_2024_paper.php)** — Uses noise-robust augmented memory for whole-slide classification.
- **[Pathology-knowledge Enhanced Multi-instance Prompt Learning for Few-shot Whole Slide Image Classification](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/1736_ECCV_2024_paper.php)** — Uses pathology-guided prompts for few-shot whole-slide classification.
- **[Semi-supervised Segmentation of Histopathology Images with Noise-Aware Topological Consistency](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/10058_ECCV_2024_paper.php)** — Uses noise-aware topological consistency for semi-supervised pathology segmentation.
- **[Snuffy: Efficient Whole Slide Image Classifier](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/12535_ECCV_2024_paper.php)** — Provides an efficient whole-slide image classification model.
- **[Solving the inverse problem of microscopy deconvolution with a residual Beylkin-Coifman-Rokhlin neural network](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/9626_ECCV_2024_paper.php)** — Deconvolves microscopy images.
- **[Style-Extracting Diffusion Models for Semi-Supervised Histopathology Segmentation](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/9583_ECCV_2024_paper.php)** — Extracts staining style with diffusion for semi-supervised histopathology segmentation.
- **[Test-Time Stain Adaptation with Diffusion Models for Histopathology Image Classification](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5175_ECCV_2024_paper.php)** — Adapts pathology staining at inference using diffusion models.
- **[Trackastra: Transformer-based cell tracking for live-cell microscopy](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/9819_ECCV_2024_paper.php)** — Uses transformers to link cell detections across live-cell microscopy frames.
- **[WSI-VQA: Interpreting Whole Slide Images by Generative Visual Question Answering](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5355_ECCV_2024_paper.php)** — Answers questions about whole-slide images through generative modeling.

#### 🤖 Foundation Models & Vision-Language

- **[CC-SAM: Enhancing SAM with Cross-feature Attention and Context for Ultrasound Image Segmentation](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6124_ECCV_2024_paper.php)** — Adds cross-feature attention and contextual information to ultrasound SAM adaptation.
- **[Domesticating SAM for Breast Ultrasound Image Segmentation via Spatial-frequency Fusion and Uncertainty Correction](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3309_ECCV_2024_paper.php)** — Combines spatial-frequency information and uncertainty correction for breast ultrasound SAM adaptation.
- **[HERGen: Elevating Radiology Report Generation with Longitudinal Data](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/7209_ECCV_2024_paper.php)** — Uses longitudinal evidence for radiology report generation.
- **[Learning with Counterfactual Explanations for Radiology Report Generation](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5958_ECCV_2024_paper.php)** — Uses counterfactual explanations to guide radiology report generation.
- **[MedRAT: Unpaired Medical Report Generation via Auxiliary Tasks](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/8947_ECCV_2024_paper.php)** — Learns medical report generation from unpaired data through auxiliary tasks.
- **[VP-SAM: Taming Segment Anything Model for Video Polyp Segmentation via Disentanglement and Spatio-temporal Side Network](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3403_ECCV_2024_paper.php)** — Adapts SAM to video polyp segmentation with disentangled spatiotemporal information.

#### 📋 Clinical NLP, EHR & Healthcare

- **[A Diffusion Model for Simulation Ready Coronary Anatomy with Morpho-skeletal Control](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/10081_ECCV_2024_paper.php)** — Generates coronary anatomy with diffusion models.
- **[Bridging the Pathology Domain Gap: Efficiently Adapting CLIP for Pathology Image Analysis with Limited Labeled Data](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/8099_ECCV_2024_paper.php)** — Adapts CLIP to pathology with limited labels.
- **[CliffPhys: Camera-based Respiratory Measurement using Clifford Neural Networks](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/11393_ECCV_2024_paper.php)** — Uses Clifford neural networks for camera-based respiratory measurement.
- **[GTP-4o: Modality-prompted Heterogeneous Graph Learning for Omni-modal Biomedical Representation](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/523_ECCV_2024_paper.php)** — Learns biomedical representations with multimodal supervision.
- **[Improving Medical Multi-modal Contrastive Learning with Expert Annotations](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3080_ECCV_2024_paper.php)** — Uses expert annotations to guide medical multimodal contrastive learning.
- **[Multistain Pretraining for Slide Representation Learning in Pathology](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/4788_ECCV_2024_paper.php)** — Uses multiple staining types to pretrain slide representations.
- **[Oulu Remote-photoplethysmography Physical Domain Attacks Database (ORPDAD)](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/9215_ECCV_2024_paper.php)** — Benchmarks physical-domain attacks against remote pulse measurement.
- **[PathMMU: A Massive Multimodal Expert-Level Benchmark for Understanding and Reasoning in Pathology](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/7899_ECCV_2024_paper.php)** — Evaluates expert-level multimodal understanding and reasoning in pathology.
- **[RadEdit: stress-testing biomedical vision models via diffusion image editing](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/1923_ECCV_2024_paper.php)** — Edits radiology images to stress-test biomedical vision models.
- **[VSViG: Real-time Video-based Seizure Detection via Skeleton-based Spatiotemporal ViG](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/10768_ECCV_2024_paper.php)** — Detects seizures from video using skeleton-based spatial-temporal graphs.

#### 🧠 Neuroimaging, EEG & Brain AI

- **[Brain-ID: Learning Contrast-agnostic Anatomical Representations for Brain Imaging](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/1918_ECCV_2024_paper.php)** — Learns brain anatomical representations robust to imaging contrast changes.
- **[Brain Netflix: Scaling Data to Reconstruct Videos from Brain Signals](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3816_ECCV_2024_paper.php)** — Uses large-scale brain recordings to reconstruct visual videos.
- **[DreamDiffusion: High-Quality EEG-to-Image Generation with Temporal Masked Signal Modeling and CLIP Alignment](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/4605_ECCV_2024_paper.php)** — Generates images from EEG using masked temporal modeling and image-language alignment.
- **[Enhancing Cross-Subject fMRI-to-Video Decoding with Global-Local Functional Alignment](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/11062_ECCV_2024_paper.php)** — Aligns local and global brain functions for cross-subject fMRI video decoding.
- **[MinD-3D: Reconstruct High-quality 3D objects in Human Brain](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6365_ECCV_2024_paper.php)** — Decodes three-dimensional objects from brain activity.
- **[NeuroPictor: Refining fMRI-to-Image Reconstruction via Multi-individual Pretraining and Multi-level Modulation](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6746_ECCV_2024_paper.php)** — Refines fMRI image reconstruction through multisubject pretraining and multilevel modulation.
- **[UMBRAE: Unified Multimodal Brain Decoding](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/1133_ECCV_2024_paper.php)** — Unifies brain decoding across multiple modalities.

#### 🫀 Physiological Signals & Medical Time Series

- **[Bi-TTA: Bidirectional Test-Time Adapter for Remote Physiological Measurement](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/1774_ECCV_2024_paper.php)** — Adapts remote physiological measurements bidirectionally at inference.
- **[Continual Learning for Remote Physiological Measurement: Minimize Forgetting and Simplify Inference](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/5279_ECCV_2024_paper.php)** — Continually learns remote physiological measurements while limiting forgetting.
- **[Implicit Neural Models to Extract Heart Rate from Video](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/10941_ECCV_2024_paper.php)** — Estimates heart rate from video using implicit neural models.

#### 🏥 Surgical AI

- **[A Rotation-invariant Texture ViT for Fine-Grained Recognition of Esophageal Cancer Endoscopic Ultrasound Images](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/4582_ECCV_2024_paper.php)** — Uses rotation-invariant texture representations to recognize esophageal cancer in endoscopic ultrasound.
- **[Leveraging Near-Field Lighting for Monocular Depth Estimation from Endoscopy Videos](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/4784_ECCV_2024_paper.php)** — Uses near-field illumination information for monocular endoscopic depth estimation.
- **[OphNet: A Large-Scale Video Benchmark for Ophthalmic Surgical Workflow Understanding](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/633_ECCV_2024_paper.php)** — Provides a video benchmark for ophthalmic surgical workflow understanding.
- **[Self-Supervised Video Desmoking for Laparoscopic Surgery](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/9123_ECCV_2024_paper.php)** — Removes laparoscopic smoke with self-supervised video learning.
- **[Shape-guided Configuration-aware Learning for Endoscopic-image-based Pose Estimation of Flexible Robotic Instruments](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3268_ECCV_2024_paper.php)** — Uses configuration and shape constraints to estimate flexible instrument pose from endoscopic images.

---

### ICCV 2023

#### 🔬 Medical Imaging & Segmentation

- **[Anatomical Invariance Modeling and Semantic Alignment for Self-supervised Learning in 3D Medical Image Analysis](https://openaccess.thecvf.com/content/ICCV2023/html/Jiang_Anatomical_Invariance_Modeling_and_Semantic_Alignment_for_Self-supervised_Learning_in_ICCV_2023_paper.html)** — Combines anatomical invariance and semantic alignment in volumetric medical pretraining.
- **[BoMD: Bag of Multi-label Descriptors for Noisy Chest X-ray Classification](https://openaccess.thecvf.com/content/ICCV2023/html/Chen_BoMD_Bag_of_Multi-label_Descriptors_for_Noisy_Chest_X-ray_Classification_ICCV_2023_paper.html)** — Uses bags of multilabel descriptors for chest X-ray learning with noisy labels.
- **[CancerUniT: Towards a Single Unified Model for Effective Detection, Segmentation, and Diagnosis of Eight Major Cancers Using a Large Collection of CT Scans](https://openaccess.thecvf.com/content/ICCV2023/html/Chen_CancerUniT_Towards_a_Single_Unified_Model_for_Effective_Detection_Segmentation_ICCV_2023_paper.html)** — Joint detection, segmentation, and diagnosis of 8 cancer types in a single model trained on 1,000+ CT scans.
- **[CauSSL: Causality-inspired Semi-supervised Learning for Medical Image Segmentation](https://openaccess.thecvf.com/content/ICCV2023/html/Miao_CauSSL_Causality-inspired_Semi-supervised_Learning_for_Medical_Image_Segmentation_ICCV_2023_paper.html)** — Uses causal structure to guide semi-supervised medical segmentation.
- **[CLIP-Driven Universal Model for Organ Segmentation and Tumor Detection](https://openaccess.thecvf.com/content/ICCV2023/html/Liu_CLIP-Driven_Universal_Model_for_Organ_Segmentation_and_Tumor_Detection_ICCV_2023_paper.html)** — CLIP text embeddings guide a universal segmentation model to handle 25 organs and 6 tumor types with open-vocabulary extensibility.
- **[Continual Segment: Towards a Single, Unified and Non-forgetting Continual Segmentation Model of 143 Whole-body Organs in CT Scans](https://openaccess.thecvf.com/content/ICCV2023/html/Ji_Continual_Segment_Towards_a_Single_Unified_and_Non-forgetting_Continual_Segmentation_ICCV_2023_paper.html)** — Continually segments whole-body organs from CT while retaining prior anatomical knowledge.
- **[CuNeRF: Cube-Based Neural Radiance Field for Zero-Shot Medical Image Arbitrary-Scale Super Resolution](https://openaccess.thecvf.com/content/ICCV2023/html/Chen_CuNeRF_Cube-Based_Neural_Radiance_Field_for_Zero-Shot_Medical_Image_Arbitrary-Scale_ICCV_2023_paper.html)** — Divides 3D medical volumes into cubes and applies NeRF-based implicit representation for zero-shot arbitrary-scale super-resolution.
- **[Decomposition-Based Variational Network for Multi-Contrast MRI Super-Resolution and Reconstruction](https://openaccess.thecvf.com/content/ICCV2023/html/Lei_Decomposition-Based_Variational_Network_for_Multi-Contrast_MRI_Super-Resolution_and_Reconstruction_ICCV_2023_paper.html)** — Jointly reconstructs and super-resolves multicontrast MRI through variational decomposition.
- **[Learning Cross-Representation Affinity Consistency for Sparsely Supervised Biomedical Instance Segmentation](https://openaccess.thecvf.com/content/ICCV2023/html/Liu_Learning_Cross-Representation_Affinity_Consistency_for_Sparsely_Supervised_Biomedical_Instance_Segmentation_ICCV_2023_paper.html)** — Segments individual instances in biomedical images.
- **[Learning to Distill Global Representation for Sparse-View CT](https://openaccess.thecvf.com/content/ICCV2023/html/Li_Learning_to_Distill_Global_Representation_for_Sparse-View_CT_ICCV_2023_paper.html)** — GloReDi distills global frequency and spatial features from a dense-view teacher to reconstruct high-quality CT from sparse projections.
- **[MRM: Masked Relation Modeling for Medical Image Pre-Training with Genetics](https://openaccess.thecvf.com/content/ICCV2023/html/Yang_MRM_Masked_Relation_Modeling_for_Medical_Image_Pre-Training_with_Genetics_ICCV_2023_paper.html)** — Uses masked relations between imaging and genetic information for medical pretraining.
- **[Neural Deformable Models for 3D Bi-Ventricular Heart Shape Reconstruction and Modeling from 2D Sparse Cardiac Magnetic Resonance Imaging](https://openaccess.thecvf.com/content/ICCV2023/html/Ye_Neural_Deformable_Models_for_3D_Bi-Ventricular_Heart_Shape_Reconstruction_and_ICCV_2023_paper.html)** — Reconstructs biventricular cardiac shape from sparse 2D MRI.
- **[Preserving Tumor Volumes for Unsupervised Medical Image Registration](https://openaccess.thecvf.com/content/ICCV2023/html/Dong_Preserving_Tumor_Volumes_for_Unsupervised_Medical_Image_Registration_ICCV_2023_paper.html)** — Volume-preservation regularization for unsupervised deformable registration to prevent pathological tissue distortion.
- **[Probabilistic Modeling of Inter- and Intra-observer Variability in Medical Image Segmentation](https://openaccess.thecvf.com/content/ICCV2023/html/Schmidt_Probabilistic_Modeling_of_Inter-_and_Intra-observer_Variability_in_Medical_Image_ICCV_2023_paper.html)** — Models both inter-observer and intra-observer variation in medical segmentation.
- **[Rethinking Multi-Contrast MRI Super-Resolution: Rectangle-Window Cross-Attention Transformer and Arbitrary-Scale Upsampling](https://openaccess.thecvf.com/content/ICCV2023/html/Li_Rethinking_Multi-Contrast_MRI_Super-Resolution_Rectangle-Window_Cross-Attention_Transformer_and_Arbitrary-Scale_Upsampling_ICCV_2023_paper.html)** — Uses windowed cross-attention for arbitrary-scale multicontrast MRI super-resolution.
- **[Taxonomy Adaptive Cross-Domain Adaptation in Medical Imaging via Optimization Trajectory Distillation](https://openaccess.thecvf.com/content/ICCV2023/html/Fan_Taxonomy_Adaptive_Cross-Domain_Adaptation_in_Medical_Imaging_via_Optimization_Trajectory_ICCV_2023_paper.html)** — Distills optimization trajectories to adapt medical models across differing label taxonomies.
- **[UniverSeg: Universal Medical Image Segmentation](https://openaccess.thecvf.com/content/ICCV2023/html/Butoi_UniverSeg_Universal_Medical_Image_Segmentation_ICCV_2023_paper.html)** — CrossBlock mechanism that produces accurate segmentation maps for any new anatomy or modality given a small labeled support set, trained on 53 open-access datasets (MegaMedical). *Butoi et al., MIT CSAIL*
- **[XNet: Wavelet-Based Low and High Frequency Fusion Networks for Fully- and Semi-Supervised Semantic Segmentation of Biomedical Images](https://openaccess.thecvf.com/content/ICCV2023/html/Zhou_XNet_Wavelet-Based_Low_and_High_Frequency_Fusion_Networks_for_Fully-_ICCV_2023_paper.html)** — Fuses wavelet frequency information for supervised and semi-supervised biomedical segmentation.

#### 🧫 Computational Pathology & Microscopy

- **[Adaptive Template Transformer for Mitochondria Segmentation in Electron Microscopy Images](https://openaccess.thecvf.com/content/ICCV2023/html/Pan_Adaptive_Template_Transformer_for_Mitochondria_Segmentation_in_Electron_Microscopy_Images_ICCV_2023_paper.html)** — Segments mitochondria in microscopy images.
- **[Affine-Consistent Transformer for Multi-Class Cell Nuclei Detection](https://openaccess.thecvf.com/content/ICCV2023/html/Huang_Affine-Consistent_Transformer_for_Multi-Class_Cell_Nuclei_Detection_ICCV_2023_paper.html)** — Detects nuclei in microscopy images.
- **[Boosting Whole Slide Image Classification from the Perspectives of Distribution, Correlation and Magnification](https://openaccess.thecvf.com/content/ICCV2023/html/Qu_Boosting_Whole_Slide_Image_Classification_from_the_Perspectives_of_Distribution_ICCV_2023_paper.html)** — Models distribution, correlation, and magnification in whole-slide classification.
- **[ConSlide: Asynchronous Hierarchical Interaction Transformer with Breakup-Reorganize Rehearsal for Continual Whole Slide Image Analysis](https://openaccess.thecvf.com/content/ICCV2023/html/Huang_ConSlide_Asynchronous_Hierarchical_Interaction_Transformer_with_Breakup-Reorganize_Rehearsal_for_Continual_ICCV_2023_paper.html)** — Continual learning framework for WSI analysis that handles sequentially arriving cancer datasets without forgetting.
- **[CO-PILOT: Dynamic Top-Down Point Cloud with Conditional Neighborhood Aggregation for Multi-Gigapixel Histopathology Image Representation](https://openaccess.thecvf.com/content/ICCV2023/html/Nakhli_CO-PILOT_Dynamic_Top-Down_Point_Cloud_with_Conditional_Neighborhood_Aggregation_for_ICCV_2023_paper.html)** — Represents gigapixel pathology with adaptive top-down point neighborhoods.
- **[Cross-Modal Translation and Alignment for Survival Analysis](https://openaccess.thecvf.com/content/ICCV2023/html/Zhou_Cross-Modal_Translation_and_Alignment_for_Survival_Analysis_ICCV_2023_paper.html)** — CMTA translates between pathology and genomic modalities bidirectionally and aligns their representations for improved cancer survival prediction.
- **[Improving Representation Learning for Histopathologic Images with Cluster Constraints](https://openaccess.thecvf.com/content/ICCV2023/html/Wu_Improving_Representation_Learning_for_Histopathologic_Images_with_Cluster_Constraints_ICCV_2023_paper.html)** — CluSiam adds cluster-consistency constraints to self-supervised pre-training, improving patch-level histopathology representations.
- **[LNPL-MIL: Learning from Noisy Pseudo Labels for Promoting Multiple Instance Learning in Whole Slide Image](https://openaccess.thecvf.com/content/ICCV2023/html/Shao_LNPL-MIL_Learning_from_Noisy_Pseudo_Labels_for_Promoting_Multiple_Instance_ICCV_2023_paper.html)** — Learns from noisy pseudo-labels in whole-slide multiple-instance classification.
- **[Multimodal Optimal Transport-based Co-Attention Transformer with Global Structure Consistency for Survival Prediction](https://openaccess.thecvf.com/content/ICCV2023/html/Xu_Multimodal_Optimal_Transport-based_Co-Attention_Transformer_with_Global_Structure_Consistency_for_ICCV_2023_paper.html)** — MOTCat: optimal transport aligns pathology patches with genomic features for robust multimodal survival prediction on TCGA datasets.
- **[Multiple Instance Learning Framework with Masked Hard Instance Mining for Whole Slide Image Classification](https://openaccess.thecvf.com/content/ICCV2023/html/Tang_Multiple_Instance_Learning_Framework_with_Masked_Hard_Instance_Mining_for_ICCV_2023_paper.html)** — Mines difficult instances during whole-slide multiple-instance classification.
- **[Unsupervised Learning of Object-Centric Embeddings for Cell Instance Segmentation in Microscopy Images](https://openaccess.thecvf.com/content/ICCV2023/html/Wolf_Unsupervised_Learning_of_Object-Centric_Embeddings_for_Cell_Instance_Segmentation_in_ICCV_2023_paper.html)** — Learns object-centered representations for unsupervised cell instance segmentation.
- **[uSplit: Image Decomposition for Fluorescence Microscopy](https://openaccess.thecvf.com/content/ICCV2023/html/Ashesh_uSplit_Image_Decomposition_for_Fluorescence_Microscopy_ICCV_2023_paper.html)** — Separates overlapping fluorescence microscopy channels.

#### 🤖 Foundation Models & Vision-Language

- **[LIMITR: Leveraging Local Information for Medical Image-Text Representation](https://openaccess.thecvf.com/content/ICCV2023/html/Dawidowicz_LIMITR_Leveraging_Local_Information_for_Medical_Image-Text_Representation_ICCV_2023_paper.html)** — Local-region contrastive alignment between chest X-ray patches and report sentences for improved downstream classification and retrieval.
- **[MedKLIP: Medical Knowledge Enhanced Language-Image Pre-Training for X-ray Diagnosis](https://openaccess.thecvf.com/content/ICCV2023/html/Wu_MedKLIP_Medical_Knowledge_Enhanced_Language-Image_Pre-Training_for_X-ray_Diagnosis_ICCV_2023_paper.html)** — Enriches VL pre-training by replacing raw report text with structured medical entity triplets, achieving strong zero-shot and few-shot performance on 11 X-ray datasets.
- **[PRIOR: Prototype Representation Joint Learning from Medical Images and Reports](https://openaccess.thecvf.com/content/ICCV2023/html/Cheng_PRIOR_Prototype_Representation_Joint_Learning_from_Medical_Images_and_Reports_ICCV_2023_paper.html)** — Prototype-based joint learning aligns local image regions with report sentences for fine-grained medical VL representation.
- **[Towards Unifying Medical Vision-and-Language Pre-Training via Soft Prompts](https://openaccess.thecvf.com/content/ICCV2023/html/Chen_Towards_Unifying_Medical_Vision-and-Language_Pre-Training_via_Soft_Prompts_ICCV_2023_paper.html)** — Soft-prompt-based unified pre-training framework across diverse medical vision-language tasks.
- **[Unify, Align and Refine: Multi-Level Semantic Alignment for Radiology Report Generation](https://openaccess.thecvf.com/content/ICCV2023/html/Li_Unify_Align_and_Refine_Multi-Level_Semantic_Alignment_for_Radiology_Report_ICCV_2023_paper.html)** — Aligns medical visual and textual semantics at multiple levels for report generation.

#### 📋 Clinical NLP, EHR & Healthcare

- **[Harvard Glaucoma Detection and Progression: A Multimodal Multitask Dataset and Generalization-Reinforced Semi-Supervised Learning](https://openaccess.thecvf.com/content/ICCV2023/html/Luo_Harvard_Glaucoma_Detection_and_Progression_A_Multimodal_Multitask_Dataset_and_ICCV_2023_paper.html)** — Provides multimodal data and learning methods for glaucoma detection and progression.

#### 🧠 Neuroimaging, EEG & Brain AI

- **[Dual Meta-Learning with Longitudinally Consistent Regularization for One-Shot Brain Tissue Segmentation Across the Human Lifespan](https://openaccess.thecvf.com/content/ICCV2023/html/Sun_Dual_Meta-Learning_with_Longitudinally_Consistent_Regularization_for_One-Shot_Brain_Tissue_ICCV_2023_paper.html)** — Uses meta-learning and longitudinal consistency for one-shot brain tissue segmentation across age groups.
- **[Enhancing Modality-Agnostic Representations via Meta-Learning for Brain Tumor Segmentation](https://openaccess.thecvf.com/content/ICCV2023/html/Konwer_Enhancing_Modality-Agnostic_Representations_via_Meta-Learning_for_Brain_Tumor_Segmentation_ICCV_2023_paper.html)** — Meta-learns brain tumor representations robust to missing or changing modalities.
- **[Scratch Each Other's Back: Incomplete Multi-Modal Brain Tumor Segmentation via Category Aware Group Self-Support Learning](https://openaccess.thecvf.com/content/ICCV2023/html/Qiu_Scratch_Each_Others_Back_Incomplete_Multi-Modal_Brain_Tumor_Segmentation_via_ICCV_2023_paper.html)** — Uses class-aware self-support learning for incomplete-modality brain tumor segmentation.
- **[SFHarmony: Source Free Domain Adaptation for Distributed Neuroimaging Analysis](https://openaccess.thecvf.com/content/ICCV2023/html/Dinsdale_SFHarmony_Source_Free_Domain_Adaptation_for_Distributed_Neuroimaging_Analysis_ICCV_2023_paper.html)** — Adapts distributed neuroimaging models without source-domain data.

---

## ACL / EMNLP

### ACL 2025

#### 🔬 Medical Imaging & Segmentation

- **[CheXalign: Preference fine-tuning in chest X-ray interpretation models without human feedback](https://aclanthology.org/2025.acl-long.1342/)** — Aligns chest X-ray interpretations through preference tuning without human feedback.

#### 🤖 Foundation Models & Vision-Language

- **[Asclepius: A Spectrum Evaluation Benchmark for Medical Multi-Modal Large Language Models](https://aclanthology.org/2025.acl-long.1178/)** — Evaluates medical multimodal models across specialties and diagnostic capacities with specialist comparisons.
- **[Automated Structured Radiology Report Generation](https://aclanthology.org/2025.acl-long.1301/)** — Generates radiology reports with explicit output structure.
- **[EAGLE: Expert-Guided Self-Enhancement for Preference Alignment in Pathology Large Vision-Language Model](https://aclanthology.org/2025.acl-long.711/)** — Uses expert guidance for preference alignment in pathology vision-language models.
- **[Exploring Compositional Generalization of Multimodal LLMs for Medical Imaging](https://aclanthology.org/2025.acl-long.639/)** — Uses Med-MAT to study generalization to unseen combinations of imaging modality, anatomy, and task.
- **[Focus on What Matters: Enhancing Medical Vision-Language Models with Automatic Attention Alignment Tuning](https://aclanthology.org/2025.acl-long.460/)** — Aligns attention automatically to improve medical vision-language models.
- **[HSCR: Hierarchical Self-Contrastive Rewarding for Aligning Medical Vision Language Models](https://aclanthology.org/2025.acl-long.679/)** — Uses hierarchical self-contrastive rewards to align medical vision-language models.
- **[Improving Medical Large Vision-Language Models with Abnormal-Aware Feedback](https://aclanthology.org/2025.acl-long.636/)** — UMed-LVLM combines abnormality-focused instruction tuning and reward signals to improve localization and image understanding.
- **[Online Iterative Self-Alignment for Radiology Report Generation](https://aclanthology.org/2025.acl-long.1348/)** — Iteratively aligns radiology report generation with self-generated feedback.
- **[RADAR: Enhancing Radiology Report Generation with Supplementary Knowledge Injection](https://aclanthology.org/2025.acl-long.1279/)** — Injects supplementary clinical knowledge into radiology report generation.
- **[The Impact of Auxiliary Patient Data on Automated Chest X-Ray Report Generation and How to Incorporate It](https://aclanthology.org/2025.acl-long.9/)** — CXRMate-ED incorporates clinical history, vital signs, and other emergency-department records into chest X-ray report generation.

#### 📋 Clinical NLP, EHR & Healthcare

- **[Adverse Event Extraction from Discharge Summaries: A New Dataset, Annotation Scheme, and Initial Findings](https://aclanthology.org/2025.acl-long.1386/)** — Provides annotations and baseline models for extracting adverse events from discharge summaries.
- **[AfriMed-QA: A Pan-African, Multi-Specialty, Medical Question-Answering Benchmark Dataset](https://aclanthology.org/2025.acl-long.96/)** — Evaluates medical question answering and demographic bias using questions spanning African countries and medical specialties.
- **[Aligning AI Research with the Needs of Clinical Coding Workflows: Eight Recommendations Based on US Data Analysis and Critical Review](https://aclanthology.org/2025.acl-long.45/)** — Analyzes clinical coding workflows and recommends better alignment of AI research with practice.
- **[A Modular Approach for Clinical SLMs Driven by Synthetic Data with Pre-Instruction Tuning, Model Merging, and Clinical-Tasks Alignment](https://aclanthology.org/2025.acl-long.950/)** — Combines synthetic instruction data, model merging, and clinical-task alignment for smaller clinical language models.
- **[Are LLMs effective psychological assessors? Leveraging adaptive RAG for interpretable mental health screening through psychometric practice](https://aclanthology.org/2025.acl-long.440/)** — Uses adaptive retrieval and psychometric practice for interpretable mental-health screening.
- **[AutoMedEval: Harnessing Language Models for Automatic Medical Capability Evaluation](https://aclanthology.org/2025.acl-long.314/)** — Uses language models to automate evaluation of medical capabilities.
- **[Can Large Language Models Accurately Generate Answer Keys for Health-related Questions?](https://aclanthology.org/2025.acl-short.28/)** — Investigates answer keys and evaluation in health question answering.
- **[Can LLMs Understand Unvoiced Speech? Exploring EMG-to-Text Conversion with LLMs](https://aclanthology.org/2025.acl-short.56/)** — Studies EMG-to-text conversion with language models for unvoiced speech interfaces.
- **[DDxTutor: Clinical Reasoning Tutoring System with Differential Diagnosis-Based Structured Reasoning](https://aclanthology.org/2025.acl-long.1495/)** — Tutors clinical reasoning using structured differential diagnosis.
- **[Follow-up Question Generation For Enhanced Patient-Provider Conversations](https://aclanthology.org/2025.acl-long.1226/)** — Generates follow-up questions to support patient-provider conversations.
- **[HyKGE: A Hypothesis Knowledge Graph Enhanced RAG Framework for Accurate and Reliable Medical LLMs Responses](https://aclanthology.org/2025.acl-long.580/)** — Augments medical question answering with hypothesis-guided knowledge-graph retrieval.
- **[Improving Automatic Evaluation of Large Language Models (LLMs) in Biomedical Relation Extraction via LLMs-as-the-Judge](https://aclanthology.org/2025.acl-long.1238/)** — Evaluates biomedical relation extraction with language-model judges.
- **[Knowledge-Augmented Multimodal Clinical Rationale Generation for Disease Diagnosis with Small Language Models](https://aclanthology.org/2025.acl-long.540/)** — Combines multimodal evidence and knowledge to generate clinical diagnostic rationales with small language models.
- **[Less is More: Explainable and Efficient ICD Code Prediction with Clinical Entities](https://aclanthology.org/2025.acl-long.1489/)** — Uses clinical entities for efficient, explainable ICD code prediction.
- **[LLM as Entity Disambiguator for Biomedical Entity-Linking](https://aclanthology.org/2025.acl-short.25/)** — Disambiguates biomedical entities in text.
- **[LLMs Can Simulate Standardized Patients via Agent Coevolution](https://aclanthology.org/2025.acl-long.846/)** — Uses coevolving agents to simulate standardized patients.
- **[MEDDxAgent: A Unified Modular Agent Framework for Explainable Automatic Differential Diagnosis](https://aclanthology.org/2025.acl-long.677/)** — Provides a modular agent framework for explainable differential diagnosis.
- **[Medical Graph RAG: Evidence-based Medical Large Language Model via Graph Retrieval-Augmented Generation](https://aclanthology.org/2025.acl-long.1381/)** — Retrieves graph-structured evidence for medical language-model reasoning.
- **[NGQA: A Nutritional Graph Question Answering Benchmark for Personalized Health-aware Nutritional Reasoning](https://aclanthology.org/2025.acl-long.296/)** — Benchmarks nutritional question answering.
- **[Pattern Recognition or Medical Knowledge? The Problem with Multiple-Choice Questions in Medicine](https://aclanthology.org/2025.acl-long.266/)** — Examines whether medical multiple-choice evaluation measures knowledge or pattern recognition.
- **[PsyDial: A Large-scale Long-term Conversational Dataset for Mental Health Support](https://aclanthology.org/2025.acl-long.1049/)** — Provides long-term conversational data for mental-health support.
- **[Query-driven Document-level Scientific Evidence Extraction from Biomedical Studies](https://aclanthology.org/2025.acl-long.1359/)** — Extracts scientific evidence from biomedical literature.
- **[ReflecTool: Towards Reflection-Aware Tool-Augmented Clinical Agents](https://aclanthology.org/2025.acl-long.663/)** — Introduces a clinical agent benchmark and uses stored tool experience, reflection, and verification to improve clinical tool use.
- **[SECRET: Semi-supervised Clinical Trial Document Similarity Search](https://aclanthology.org/2025.acl-long.264/)** — Searches similar clinical-trial documents with semi-supervised representations.
- **[Should I Believe in What Medical AI Says? A Chinese Benchmark for Medication Based on Knowledge and Reasoning](https://aclanthology.org/2025.acl-short.91/)** — Benchmarks Chinese medication knowledge and reasoning.
- **[TC–RAG: Turing–Complete RAG’s Case study on Medical LLM Systems](https://aclanthology.org/2025.acl-long.558/)** — Studies memory and control mechanisms in retrieval-augmented medical language-model systems.
- **[Temporal Relation Extraction in Clinical Texts: A Span-based Graph Transformer Approach](https://aclanthology.org/2025.acl-long.1251/)** — Uses span-based graph transformers to extract temporal relationships from clinical text.
- **[Towards Omni-RAG: Comprehensive Retrieval-Augmented Generation for Large Language Models in Medical Applications](https://aclanthology.org/2025.acl-long.742/)** — Introduces MedOmniKB and source planning optimization to retrieve suitable evidence from heterogeneous medical knowledge sources.
- **[Tracking Life’s Ups and Downs: Mining Life Events from Social Media Posts for Mental Health Analysis](https://aclanthology.org/2025.acl-long.345/)** — Identifies life events in social-media histories for mental-health analysis.
- **[uMedSum: A Unified Framework for Clinical Abstractive Summarization](https://aclanthology.org/2025.acl-long.134/)** — Provides a unified framework for clinical abstractive summarization.
- **[VITAL: A New Dataset for Benchmarking Pluralistic Alignment in Healthcare](https://aclanthology.org/2025.acl-long.1119/)** — Benchmarks alignment with diverse values and preferences in healthcare.
- **[What is Stigma Attributed to? A Theory-Grounded, Expert-Annotated Interview Corpus for Demystifying Mental-Health Stigma](https://aclanthology.org/2025.acl-long.272/)** — Studies mental-health stigma using interview data.

#### 🧠 Neuroimaging, EEG & Brain AI

- **[Delta-KNN: Improving Demonstration Selection in In-Context Learning for Alzheimer’s Disease Detection](https://aclanthology.org/2025.acl-long.1253/)** — Selects in-context examples for Alzheimer's disease detection.
- **[Mitigating Confounding in Speech-Based Dementia Detection through Weight Masking](https://aclanthology.org/2025.acl-long.514/)** — Mitigates confounding in speech-based dementia detection through selective weight masking.

---

### EMNLP 2025

#### 🔬 Medical Imaging & Segmentation

- **[CREPE: Rapid Chest X-ray Report Evaluation by Predicting Multi-category Error Counts](https://aclanthology.org/2025.emnlp-main.1102/)** — Evaluates chest X-ray reports by predicting counts of different error categories.

#### 🤖 Foundation Models & Vision-Language

- **[Structuring Radiology Reports: Challenging LLMs with Lightweight Models](https://aclanthology.org/2025.emnlp-main.392/)** — Compares lightweight models with language models for radiology report structuring.
- **[X-FLoRA: Cross-modal Federated Learning with Modality-expert LoRA for Medical VQA](https://aclanthology.org/2025.emnlp-main.422/)** — Uses modality-specific low-rank experts for federated medical VQA.

#### 📋 Clinical NLP, EHR & Healthcare

- **[3DS: Medical Domain Adaptation of LLMs via Decomposed Difficulty-based Data Selection](https://aclanthology.org/2025.emnlp-main.983/)** — Selects medical instruction-tuning examples using model-specific estimates of understanding, response confidence, and correctness.
- **[3MDBench: Medical Multimodal Multi-agent Dialogue Benchmark](https://aclanthology.org/2025.emnlp-main.1353/)** — Simulates multimodal telemedical consultations with patient and assessor agents to evaluate diagnostic accuracy and dialogue quality.
- **[Africa Health Check: Probing Cultural Bias in Medical LLMs](https://aclanthology.org/2025.emnlp-main.1639/)** — Probes cultural bias in medical language-model responses about African healthcare.
- **[A Knowledge-driven Adaptive Collaboration of LLMs for Enhancing Medical Decision-making](https://aclanthology.org/2025.emnlp-main.1699/)** — Coordinates language-model agents using medical knowledge for clinical decisions.
- **[Ask Patients with Patience: Enabling LLMs for Human-Centric Medical Dialogue with Grounded Reasoning](https://aclanthology.org/2025.emnlp-main.142/)** — Combines medical guidelines and Bayesian active learning for adaptive symptom gathering and transparent multi-turn diagnostic dialogue.
- **[Aspect-Oriented Summarization for Psychiatric Short-Term Readmission Prediction](https://aclanthology.org/2025.emnlp-main.1423/)** — Uses aspect-oriented psychiatric summaries to predict short-term readmission.
- **[AutoCT: Automating Interpretable Clinical Trial Prediction with LLM Agents](https://aclanthology.org/2025.emnlp-main.1575/)** — Uses language-model agents for interpretable clinical-trial outcome prediction.
- **[Building Trust in Clinical LLMs: Bias Analysis and Dataset Transparency](https://aclanthology.org/2025.emnlp-main.1174/)** — Studies bias and dataset transparency in clinical language models.
- **[Causal Representation Learning from Multimodal Clinical Records under Non-Random Modality Missingness](https://aclanthology.org/2025.emnlp-main.1465/)** — Learns causal clinical representations when missing modalities are not random.
- **[Causal Tree Extraction from Medical Case Reports: A Novel Task for Experts-like Text Comprehension](https://aclanthology.org/2025.emnlp-main.1313/)** — Extracts causal reasoning trees from medical case reports.
- **[CMedCalc-Bench: A Fine-Grained Benchmark for Chinese Medical Calculations in LLM](https://aclanthology.org/2025.emnlp-main.1302/)** — Benchmarks fine-grained Chinese medical calculations in language models.
- **[DDO: Dual-Decision Optimization for LLM-Based Medical Consultation via Multi-Agent Collaboration](https://aclanthology.org/2025.emnlp-main.1340/)** — Optimizes collaborating agents for medical consultation decisions.
- **[DeepWell-Adol: A Scalable Expert-Based Dialogue Corpus for Adolescent Positive Mental Health and Wellbeing Promotion](https://aclanthology.org/2025.emnlp-main.646/)** — Provides expert-based conversations supporting adolescent mental-health research.
- **[DischargeSim: A Simulation Benchmark for Educational Doctor–Patient Communication at Discharge](https://aclanthology.org/2025.emnlp-main.546/)** — Simulates discharge conversations to evaluate educational doctor-patient communication.
- **[EmoAgent: Assessing and Safeguarding Human-AI Interaction for Mental Health Safety](https://aclanthology.org/2025.emnlp-main.594/)** — Assesses risks to mental-health safety during human-AI interactions.
- **[End-to-End Learnable Psychiatric Scale Guided Risky Post Screening for Depression Detection on Social Media](https://aclanthology.org/2025.emnlp-main.201/)** — Uses psychiatric scales to guide screening for depression-related social-media content.
- **[Enhancing Study-Level Inference from Clinical Trial Papers via Reinforcement Learning-Based Numeric Reasoning](https://aclanthology.org/2025.emnlp-main.1544/)** — Uses reinforcement learning for numerical inference from clinical-trial publications.
- **[From Scores to Steps: Diagnosing and Improving LLM Performance in Evidence-Based Medical Calculations](https://aclanthology.org/2025.emnlp-main.548/)** — Diagnoses stepwise errors in evidence-based medical calculations.
- **[HealthCards: Exploring Text-to-Image Generation as Visual Aids for Healthcare Knowledge Democratizing and Education](https://aclanthology.org/2025.emnlp-main.1401/)** — Evaluates generated visual aids for healthcare education.
- **[Leveraging Knowledge Graph-Enhanced LLMs for Context-Aware Medical Consultation](https://aclanthology.org/2025.emnlp-main.1549/)** — Combines contextual medical consultation with knowledge-graph-enhanced language models.
- **[M3Retrieve: Benchmarking Multimodal Retrieval for Medicine](https://aclanthology.org/2025.emnlp-main.771/)** — Benchmarks multimodal retrieval across medical data sources.
- **[Mapping semantic networks to Dutch word embeddings as a diagnostic tool for cognitive decline](https://aclanthology.org/2025.emnlp-main.1560/)** — Maps semantic networks to word embeddings to study cognitive decline.
- **[Measuring Risk of Bias in Biomedical Reports: The RoBBR Benchmark](https://aclanthology.org/2025.emnlp-main.160/)** — Benchmarks risk-of-bias assessment in clinical trial reports.
- **[MedFact: A Large-scale Chinese Dataset for Evidence-based Medical Fact-checking of LLM Responses](https://aclanthology.org/2025.emnlp-main.1646/)** — Provides Chinese evidence-grounded medical fact-checking data.
- **[MedHallu: A Comprehensive Benchmark for Detecting Medical Hallucinations in Large Language Models](https://aclanthology.org/2025.emnlp-main.143/)** — Benchmarks detection of plausible but incorrect medical answers with controlled hallucination difficulty and uncertainty-aware evaluation.
- **[Med-PRM: Medical Reasoning Models with Stepwise, Guideline-verified Process Rewards](https://aclanthology.org/2025.emnlp-main.837/)** — Uses guideline-verified stepwise process rewards for medical reasoning.
- **[Med-VRAgent: A Framework for Medical Visual Reasoning-Enhanced Agents](https://aclanthology.org/2025.emnlp-main.939/)** — Builds agents with enhanced reasoning over medical visual evidence.
- **[MentalGLM Series: Explainable Large Language Models for Mental Health Analysis on Chinese Social Media](https://aclanthology.org/2025.emnlp-main.686/)** — Develops explainable models for Chinese social-media mental-health analysis.
- **[MultiMed-ST: Large-scale Many-to-many Multilingual Medical Speech Translation](https://aclanthology.org/2025.emnlp-main.599/)** — Provides multilingual medical speech data for many-to-many translation.
- **[Not What the Doctor Ordered: Surveying LLM-based De-identification and Quantifying Clinical Information Loss](https://aclanthology.org/2025.emnlp-main.1637/)** — Measures clinical information lost during language-model de-identification.
- **[Pluralistic Alignment for Healthcare: A Role-Driven Framework](https://aclanthology.org/2025.emnlp-main.1596/)** — Aligns healthcare responses with pluralistic role-dependent preferences.
- **[Process-Supervised Reward Models for Verifying Clinical Note Generation: A Scalable Approach Guided by Domain Expertise](https://aclanthology.org/2025.emnlp-main.967/)** — Uses domain-guided process rewards to verify generated clinical notes.
- **[RareSyn: Health Record Synthesis for Rare Disease Diagnosis](https://aclanthology.org/2025.emnlp-main.620/)** — Synthesizes health records to support rare-disease diagnosis.
- **[ReasonMed: A 370K Multi-Agent Generated Dataset for Advancing Medical Reasoning](https://aclanthology.org/2025.emnlp-main.1344/)** — Provides multi-agent-generated data for medical reasoning research.
- **[ReDepress: A Cognitive Framework for Detecting Depression Relapse from Social Media](https://aclanthology.org/2025.emnlp-main.1758/)** — Uses cognitive structure to study depression relapse in social-media histories.
- **[ReEvalMed: Rethinking Medical Report Evaluation by Aligning Metrics with Real-World Clinical Judgment](https://aclanthology.org/2025.emnlp-main.598/)** — Aligns medical report evaluation with clinical expert judgments.
- **[Section-Level Simplification of Biomedical Abstracts](https://aclanthology.org/2025.emnlp-main.697/)** — Simplifies biomedical abstracts for broader audiences.
- **[Synth-SBDH: A Synthetic Dataset of Social and Behavioral Determinants of Health for Clinical Text](https://aclanthology.org/2025.emnlp-main.1418/)** — Synthesizes clinical text about social and behavioral determinants of health.
- **[The Sound of Syntax: Finetuning and Comprehensive Evaluation of Language Models for Speech Pathology](https://aclanthology.org/2025.emnlp-main.1768/)** — Evaluates language models on speech-pathology tasks.
- **[Towards AI-Assisted Psychotherapy: Emotion-Guided Generative Interventions](https://aclanthology.org/2025.emnlp-main.1664/)** — Uses emotion-guided generation for psychotherapy-support interventions.
- **[TracSum: A New Benchmark for Aspect-Based Summarization with Sentence-Level Traceability in Medical Domain](https://aclanthology.org/2025.emnlp-main.43/)** — Benchmarks medical aspect-based summarization with sentence-level evidence traceability.
- **[Tree-of-Quote Prompting Improves Factuality and Attribution in Multi-Hop and Medical Reasoning](https://aclanthology.org/2025.emnlp-main.285/)** — Uses quoted evidence to improve attribution and factuality in medical reasoning.
- **[Trustworthy Medical Question Answering: An Evaluation-Centric Survey](https://aclanthology.org/2025.emnlp-main.1398/)** — Surveys evaluation methods for trustworthy medical question answering.
- **[Viability of Machine Translation for Healthcare in Low-Resourced Languages](https://aclanthology.org/2025.emnlp-main.535/)** — Evaluates healthcare translation in low-resource languages.

#### 🧠 Neuroimaging, EEG & Brain AI

- **[Aligning Text/Speech Representations from Multimodal Models with MEG Brain Activity During Listening](https://aclanthology.org/2025.emnlp-main.1748/)** — Aligns speech and text representations with human MEG during listening.
- **[Rethinking Cross-Subject Data Splitting for Brain-to-Text Decoding](https://aclanthology.org/2025.emnlp-main.289/)** — Examines data-splitting practices for brain-to-text decoding.

#### 🏥 Surgical AI

- **[MMAG: Multimodal Learning for Mucus Anomaly Grading in Nasal Endoscopy via Semantic Attribute Prompting](https://aclanthology.org/2025.emnlp-main.1066/)** — Grades nasal mucus abnormalities from endoscopy using visual attributes.

---

### ACL 2024

#### 🤖 Foundation Models & Vision-Language

- **[Fine-Grained Image-Text Alignment in Medical Imaging Enables Explainable Cyclic Image-Report Generation](https://aclanthology.org/2024.acl-long.514/)** — Aligns images and reports at fine granularity for explainable bidirectional generation.

#### 📋 Clinical NLP, EHR & Healthcare

- **[ChiMed-GPT: A Chinese Medical Large Language Model with Full Training Regime and Better Alignment to Human Preferences](https://aclanthology.org/2024.acl-long.386/)** — Trains and preference-aligns a Chinese medical language model across a complete training pipeline.
- **[DocLens: Multi-aspect Fine-grained Evaluation for Medical Text Generation](https://aclanthology.org/2024.acl-long.39/)** — Evaluates medical text generation across multiple fine-grained aspects.
- **[FactPICO: Factuality Evaluation for Plain Language Summarization of Medical Evidence](https://aclanthology.org/2024.acl-long.459/)** — Evaluates factual consistency when simplifying medical evidence into plain language.
- **[From Sights to Insights: Towards Summarization of Multimodal Clinical Documents](https://aclanthology.org/2024.acl-long.708/)** — Summarizes clinical documents containing both visual and textual information.
- **[HealMe: Harnessing Cognitive Reframing in Large Language Models for Psychotherapy](https://aclanthology.org/2024.acl-long.93/)** — Uses cognitive reframing in language-model-based psychotherapy support.
- **[RAM-EHR: Retrieval Augmentation Meets Clinical Predictions on Electronic Health Records](https://aclanthology.org/2024.acl-short.68/)** — Augments EHR predictive models with retrieval from similar historical patient visits and summarized external knowledge, improving clinical risk prediction across multiple tasks.
- **[To Generate or to Retrieve? On the Effectiveness of Artificial Contexts for Medical Open-Domain Question Answering](https://aclanthology.org/2024.acl-long.533/)** — Compares generated and retrieved contexts for open-domain medical question answering.
- **[Unity in Diversity: Collaborative Pre-training Across Multimodal Medical Sources](https://aclanthology.org/2024.acl-long.199/)** — Pretrains jointly across heterogeneous medical modalities and data sources.

#### 🧠 Neuroimaging, EEG & Brain AI

- **[Enhancing EEG-to-Text Decoding through Transferable Representations from Pre-trained Contrastive EEG-Text Masked Autoencoder](https://aclanthology.org/2024.acl-long.393/)** — Transfers contrastively pretrained EEG-text representations to language decoding.
- **[SPZ: A Semantic Perturbation-based Data Augmentation Method with Zonal-Mixing for Alzheimer’s Disease Detection](https://aclanthology.org/2024.acl-long.823/)** — Augments Alzheimer's speech-detection data through semantic perturbation and zonal mixing.

---

### EMNLP 2024

#### 🔬 Medical Imaging & Segmentation

- **[Automatic sentence segmentation of clinical record narratives in real-world data](https://aclanthology.org/2024.emnlp-main.1156/)** — Segments sentences in real clinical record narratives.

#### 🤖 Foundation Models & Vision-Language

- **[Divide and Conquer Radiology Report Generation via Observation Level Fine-grained Pretraining and Prompt Tuning](https://aclanthology.org/2024.emnlp-main.433/)** — Uses observation-level pretraining and prompt tuning for radiology reports.
- **[ERVQA: A Dataset to Benchmark the Readiness of Large Vision Language Models in Hospital Environments](https://aclanthology.org/2024.emnlp-main.873/)** — Evaluates medical vision-language readiness for hospital environments.
- **[FEDKIM: Adaptive Federated Knowledge Injection into Medical Foundation Models](https://aclanthology.org/2024.emnlp-main.464/)** — Injects federated knowledge into medical foundation models.
- **[Medical Adaptation of Large Language and Vision-Language Models: Are We Making Progress?](https://aclanthology.org/2024.emnlp-main.677/)** — Reassesses progress in medical adaptation of language and vision-language models.
- **[RaTEScore: A Metric for Radiology Report Generation](https://aclanthology.org/2024.emnlp-main.836/)** — Evaluates generated radiology reports with a radiology-specific metric.
- **[Towards Injecting Medical Visual Knowledge into Multimodal LLMs at Scale](https://aclanthology.org/2024.emnlp-main.418/)** — Adds medical visual knowledge to multimodal language models at scale.

#### 📋 Clinical NLP, EHR & Healthcare

- **[An Unsupervised Approach to Achieve Supervised-Level Explainability in Healthcare Records](https://aclanthology.org/2024.emnlp-main.280/)** — Learns explainable healthcare-record representations without direct explanatory supervision.
- **[Beyond Label Attention: Transparency in Language Models for Automated Medical Coding via Dictionary Learning](https://aclanthology.org/2024.emnlp-main.500/)** — Uses dictionary learning to improve transparency of automated clinical coding.
- **[Bio-RFX: Refining Biomedical Extraction via Advanced Relation Classification and Structural Constraints](https://aclanthology.org/2024.emnlp-main.588/)** — Extracts biomedical relations from text.
- **[BMRetriever: Tuning Large Language Models as Better Biomedical Text Retrievers](https://aclanthology.org/2024.emnlp-main.1241/)** — Learns biomedical text retrieval representations.
- **[Can Large Language Models Enhance Predictions of Disease Progression? Investigating Through Disease Network Link Prediction](https://aclanthology.org/2024.emnlp-main.980/)** — Studies language-model representations for disease-progression network prediction.
- **[CareCorpus+: Expanding and Augmenting Caregiver Strategy Data to Support Pediatric Rehabilitation](https://aclanthology.org/2024.emnlp-main.392/)** — Provides a corpus for pediatric rehabilitation language applications.
- **[CARER - ClinicAl Reasoning-Enhanced Representation for Temporal Health Risk Prediction](https://aclanthology.org/2024.emnlp-main.580/)** — Combines clinical reasoning with representations for temporal health-risk prediction.
- **[CasiMedicos-Arg: A Medical Question Answering Dataset Annotated with Explanatory Argumentative Structures](https://aclanthology.org/2024.emnlp-main.1026/)** — Provides medical questions annotated with explanatory argument structures.
- **[CliMedBench: A Large-Scale Chinese Benchmark for Evaluating Medical Large Language Models in Clinical Scenarios](https://aclanthology.org/2024.emnlp-main.480/)** — Evaluates Chinese medical language models in clinical scenarios.
- **[Deciphering Cognitive Distortions in Patient-Doctor Mental Health Conversations: A Multimodal LLM-Based Detection and Reasoning Framework](https://aclanthology.org/2024.emnlp-main.1256/)** — Detects and explains cognitive distortions in multimodal mental-health conversations.
- **[DKEC: Domain Knowledge Enhanced Multi-Label Classification for Diagnosis Prediction](https://aclanthology.org/2024.emnlp-main.712/)** — Adds domain knowledge to multilabel diagnosis prediction.
- **[EHRAgent: Code Empowers Large Language Models for Few-shot Complex Tabular Reasoning on Electronic Health Records](https://aclanthology.org/2024.emnlp-main.1245/)** — Uses code-capable agents for complex tabular reasoning over EHRs.
- **[Emotion Granularity from Text: An Aggregate-Level Indicator of Mental Health](https://aclanthology.org/2024.emnlp-main.1069/)** — Studies granularity of textual emotion expressions as a mental-health indicator.
- **[Fool Me Once? Contrasting Textual and Visual Explanations in a Clinical Decision-Support Setting](https://aclanthology.org/2024.emnlp-main.1051/)** — Compares the effects of visual and textual explanations in clinical decision support.
- **[Generalizing Clinical De-identification Models by Privacy-safe Data Augmentation using GPT-4](https://aclanthology.org/2024.emnlp-main.1181/)** — Uses privacy-safe synthetic augmentation to improve clinical de-identification generalization.
- **[Generative Models for Automatic Medical Decision Rule Extraction from Text](https://aclanthology.org/2024.emnlp-main.399/)** — Extracts medical decision rules from text with generative models.
- **[Large Language Models Are Poor Clinical Decision-Makers: A Comprehensive Benchmark](https://aclanthology.org/2024.emnlp-main.759/)** — Benchmarks language models as clinical decision makers.
- **[MedAdapter: Efficient Test-Time Adaptation of Large Language Models Towards Medical Reasoning](https://aclanthology.org/2024.emnlp-main.1244/)** — Adapts language models efficiently at inference for medical reasoning.
- **[MedCoT: Medical Chain of Thought via Hierarchical Expert](https://aclanthology.org/2024.emnlp-main.962/)** — Coordinates expert hierarchies to generate medical chains of thought.
- **[MediTOD: An English Dialogue Dataset for Medical History Taking with Comprehensive Annotations](https://aclanthology.org/2024.emnlp-main.936/)** — Provides annotated English dialogues for taking patient medical histories.
- **[MedReadMe: A Systematic Study for Fine-grained Sentence Readability in Medical Domain](https://aclanthology.org/2024.emnlp-main.958/)** — Studies sentence-level readability of medical language.
- **[NeuroTrialNER: An Annotated Corpus for Neurological Diseases and Therapies in Clinical Trial Registries](https://aclanthology.org/2024.emnlp-main.1050/)** — Annotates neurological diseases and therapies in clinical-trial registries.
- **[PATIENT-\psi: Using Large Language Models to Simulate Patients for Training Mental Health Professionals](https://aclanthology.org/2024.emnlp-main.711/)** — Simulates patients to support training of mental-health professionals.
- **[PsyGUARD: An Automated System for Suicide Detection and Risk Assessment in Psychological Counseling](https://aclanthology.org/2024.emnlp-main.264/)** — Detects suicide risk in psychological counseling conversations.
- **[Roleplay-doh: Enabling Domain-Experts to Create LLM-simulated Patients via Eliciting and Adhering to Principles](https://aclanthology.org/2024.emnlp-main.591/)** — Lets clinical experts specify principles for simulated patient behavior.
- **[RULE: Reliable Multimodal RAG for Factuality in Medical Vision Language Models](https://aclanthology.org/2024.emnlp-main.62/)** — Retrieval-augmented framework that enforces factual grounding in medical VLM responses via controllable context selection.
- **[Self-Training Large Language and Vision Assistant for Medical Question Answering](https://aclanthology.org/2024.emnlp-main.1119/)** — Self-trains multimodal assistants for medical question answering.
- **[SPEED++: A Multilingual Event Extraction Framework for Epidemic Prediction and Preparedness](https://aclanthology.org/2024.emnlp-main.720/)** — Extracts multilingual outbreak events for epidemic preparedness.
- **[Still Not Quite There! Evaluating Large Language Models for Comorbid Mental Health Diagnosis](https://aclanthology.org/2024.emnlp-main.931/)** — Evaluates diagnosis of co-occurring mental-health conditions.
- **[SYNFAC-EDIT: Synthetic Imitation Edit Feedback for Factual Alignment in Clinical Summarization](https://aclanthology.org/2024.emnlp-main.1120/)** — Uses synthetic editing feedback to align clinical summaries with facts.
- **[When LLMs Meets Acoustic Landmarks: An Efficient Approach to Integrate Speech into Large Language Models for Depression Detection](https://aclanthology.org/2024.emnlp-main.8/)** — Combines acoustic landmarks and language models for depression detection.

#### 🧠 Neuroimaging, EEG & Brain AI

- **[Adversarial Text Generation using Large Language Models for Dementia Detection](https://aclanthology.org/2024.emnlp-main.1222/)** — Generates adversarial text to study robustness of dementia detection.
- **[Decoding the Echoes of Vision from fMRI: Memory Disentangling for Past Semantic Information](https://aclanthology.org/2024.emnlp-main.122/)** — Disentangles prior semantic information when decoding vision from fMRI.

---

### ACL 2023

#### 🤖 Foundation Models & Vision-Language

- **[Toward Expanding the Scope of Radiology Report Summarization to Multiple Anatomies and Modalities](https://aclanthology.org/2023.acl-short.41/)** — Extends radiology report summarization across anatomical regions and imaging modalities.

#### 📋 Clinical NLP, EHR & Healthcare

- **[A Simple and Flexible Modeling for Mental Disorder Detection by Learning from Clinical Questionnaires](https://aclanthology.org/2023.acl-long.681/)** — Uses clinical questionnaire information for flexible mental-disorder detection.
- **[Automated Metrics for Medical Multi-Document Summarization Disagree with Human Evaluations](https://aclanthology.org/2023.acl-long.549/)** — Compares automated medical multi-document summarization metrics with human judgments.
- **[Can NLI Provide Proper Indirect Supervision for Low-resource Biomedical Relation Extraction?](https://aclanthology.org/2023.acl-long.138/)** — Uses natural language inference for low-resource biomedical relation extraction.
- **[Characterization of Stigmatizing Language in Medical Records](https://aclanthology.org/2023.acl-short.28/)** — Characterizes stigmatizing language in clinical records.
- **[Clinical Note Owns its Hierarchy: Multi-Level Hypergraph Neural Networks for Patient-Level Representation Learning](https://aclanthology.org/2023.acl-long.305/)** — Models note hierarchies with multilevel hypergraphs for patient representation learning.
- **[CoAD: Automatic Diagnosis through Symptom and Disease Collaborative Generation](https://aclanthology.org/2023.acl-long.350/)** — Generates symptoms and diseases jointly for automatic diagnosis.
- **[DARE: Towards Robust Text Explanations in Biomedical and Healthcare Applications](https://aclanthology.org/2023.acl-long.644/)** — Studies robust textual explanations in biomedical and healthcare tasks.
- **[Detecting Contradictory COVID-19 Drug Efficacy Claims from Biomedical Literature](https://aclanthology.org/2023.acl-short.61/)** — Identifies contradictory claims about COVID-19 drug efficacy.
- **[DICE: Data-Efficient Clinical Event Extraction with Generative Models](https://aclanthology.org/2023.acl-long.886/)** — Extracts clinical events through data-efficient generative modeling.
- **[DrBERT: A Robust Pre-trained Model in French for Biomedical and Clinical domains](https://aclanthology.org/2023.acl-long.896/)** — Pretrains robust French representations for biomedical and clinical language.
- **[Efficient Diagnosis Assignment Using Unstructured Clinical Notes](https://aclanthology.org/2023.acl-short.42/)** — Assigns diagnostic codes from unstructured clinical notes.
- **[Human-in-the-loop Evaluation for Early Misinformation Detection: A Case Study of COVID-19 Treatments](https://aclanthology.org/2023.acl-long.881/)** — Evaluates misinformation about COVID-19 treatments.
- **[Injecting knowledge into language generation: a case study in auto-charting after-visit care instructions from medical dialogue](https://aclanthology.org/2023.acl-long.133/)** — Injects knowledge into after-visit instructions generated from medical dialogue.
- **[MDACE: MIMIC Documents Annotated with Code Evidence](https://aclanthology.org/2023.acl-long.416/)** — Provides evidence annotations for clinical coding in MIMIC discharge summaries.
- **[MidMed: Towards Mixed-Type Dialogues for Medical Consultation](https://aclanthology.org/2023.acl-long.453/)** — Models mixed types of medical consultation dialogue.
- **[ORGAN: Observation-Guided Radiology Report Generation via Tree Reasoning](https://aclanthology.org/2023.acl-long.451/)** — Tree-structured reasoning over clinical observations guides a decoder to generate complete, clinically consistent radiology reports with explicit rationales.
- **[Summarizing, Simplifying, and Synthesizing Medical Evidence using GPT-3 (with Varying Success)](https://aclanthology.org/2023.acl-short.119/)** — Evaluates language-model summarization, simplification, and synthesis of medical evidence.
- **[Towards Identifying Fine-Grained Depression Symptoms from Memes](https://aclanthology.org/2023.acl-long.495/)** — Identifies specific depression symptoms expressed through memes.
- **[Understanding Client Reactions in Online Mental Health Counseling](https://aclanthology.org/2023.acl-long.577/)** — Models clients' reactions in online mental-health counseling.

#### 🧠 Neuroimaging, EEG & Brain AI

- **[Towards Domain-Agnostic and Domain-Adaptive Dementia Detection from Spoken Language](https://aclanthology.org/2023.acl-long.668/)** — Studies adaptation and generalization in speech-based dementia detection.

---

### EMNLP 2023

#### 🤖 Foundation Models & Vision-Language

- **[A Self-training Framework for Automated Medical Report Generation](https://aclanthology.org/2023.emnlp-main.1024/)** — Self-trains automated medical report generation models.

#### 📋 Clinical NLP, EHR & Healthcare

- **[A Comprehensive Evaluation of Biomedical Entity Linking Models](https://aclanthology.org/2023.emnlp-main.893/)** — Evaluates biomedical entity linking.
- **[An Integrative Survey on Mental Health Conversational Agents to Bridge Computer Science and Medical Perspectives](https://aclanthology.org/2023.emnlp-main.698/)** — Surveys mental-health conversational agents across computing and clinical research.
- **[Appraising the Potential Uses and Harms of LLMs for Medical Systematic Reviews](https://aclanthology.org/2023.emnlp-main.626/)** — Examines potential uses and harms of language models in medical systematic reviews.
- **[AutoTrial: Prompting Language Models for Clinical Trial Design](https://aclanthology.org/2023.emnlp-main.766/)** — Prompts language models to support clinical-trial design.
- **[BioFEG: Generate Latent Features for Biomedical Entity Linking](https://aclanthology.org/2023.emnlp-main.710/)** — Links biomedical entities with fine-grained representations.
- **[Biomedical Named Entity Recognition via Dictionary-based Synonym Generalization](https://aclanthology.org/2023.emnlp-main.903/)** — Recognizes biomedical named entities in text.
- **[Clinical Contradiction Detection](https://aclanthology.org/2023.emnlp-main.80/)** — Detects contradictions within clinical information.
- **[Controllable Contrastive Generation for Multilingual Biomedical Entity Linking](https://aclanthology.org/2023.emnlp-main.350/)** — Links biomedical entities across languages.
- **[Detection of Multiple Mental Disorders from Social Media with Two-Stream Psychiatric Experts](https://aclanthology.org/2023.emnlp-main.562/)** — Uses specialized psychiatric representations to detect multiple mental disorders from social media.
- **[Dr ChatGPT tell me what I want to hear: How different prompts impact health answer correctness](https://aclanthology.org/2023.emnlp-main.928/)** — Studies prompt-based assessment of health-answer correctness.
- **[Enhancing Biomedical Lay Summarisation with External Knowledge Graphs](https://aclanthology.org/2023.emnlp-main.498/)** — Uses knowledge graphs for lay summaries of biomedical literature.
- **[Exploring the Boundaries of GPT-4 in Radiology](https://aclanthology.org/2023.emnlp-main.891/)** — Evaluates capabilities and limitations of GPT-4 in radiology.
- **[FaMeSumm: Investigating and Improving Faithfulness of Medical Summarization](https://aclanthology.org/2023.emnlp-main.673/)** — Investigates and improves factual faithfulness in medical summarization.
- **[FedTherapist: Mental Health Monitoring with User-Generated Linguistic Expressions on Smartphones via Federated Learning](https://aclanthology.org/2023.emnlp-main.734/)** — Monitors mental-health language signals on smartphones through federated learning.
- **[Fine-grained Medical Vision-Language Representation Learning for Radiology Report Generation](https://aclanthology.org/2023.emnlp-main.989/)** — Learns phenotype-driven image-sentence representations for radiology report generation (PhenotypeCLIP).
- **[Hierarchical Pretraining on Multimodal Electronic Health Records](https://aclanthology.org/2023.emnlp-main.171/)** — Pretrains hierarchical multimodal electronic health record representations.
- **[Improving Biomedical Abstractive Summarisation with Knowledge Aggregation from Citation Papers](https://aclanthology.org/2023.emnlp-main.40/)** — Studies citation support in biomedical summaries.
- **[Language and Mental Health: Measures of Emotion Dynamics from Text as Linguistic Biosocial Markers](https://aclanthology.org/2023.emnlp-main.188/)** — Studies textual emotion dynamics as mental-health indicators.
- **[MedEval: A Multi-Level, Multi-Task, and Multi-Domain Medical Benchmark for Language Model Evaluation](https://aclanthology.org/2023.emnlp-main.540/)** — Benchmarks medical language models across tasks, domains, and evaluation levels.
- **[Multilingual Simplification of Medical Texts](https://aclanthology.org/2023.emnlp-main.1037/)** — Simplifies medical text across languages.
- **[NLI4CT: Multi-Evidence Natural Language Inference for Clinical Trial Reports](https://aclanthology.org/2023.emnlp-main.1041/)** — Benchmarks evidence-based natural language inference over clinical-trial reports.
- **[Physician Detection of Clinical Harm in Machine Translation: Quality Estimation Aids in Reliance and Backtranslation Identifies Critical Errors](https://aclanthology.org/2023.emnlp-main.712/)** — Studies clinician detection of harmful healthcare translation errors.
- **[Revisiting De-Identification of Electronic Medical Records: Evaluation of Within- and Cross-Hospital Generalization](https://aclanthology.org/2023.emnlp-main.224/)** — Evaluates clinical de-identification within and across hospitals.
- **[Semantic Similarity Models for Depression Severity Estimation](https://aclanthology.org/2023.emnlp-main.1000/)** — Uses semantic similarity representations to estimate depression severity.
- **[Task-Adaptive Tokenization: Enhancing Long-Form Text Generation Efficacy in Mental Health and Beyond](https://aclanthology.org/2023.emnlp-main.944/)** — Adapts tokenization for long-form mental-health text generation.
- **[Towards Interpretable Mental Health Analysis with Large Language Models](https://aclanthology.org/2023.emnlp-main.370/)** — Develops interpretable language-model analysis of mental-health text.

#### 🧠 Neuroimaging, EEG & Brain AI

- **[A Digital Language Coherence Marker for Monitoring Dementia](https://aclanthology.org/2023.emnlp-main.994/)** — Uses digital language-coherence measures to monitor dementia.
- **[Granularity Matters: Pathological Graph-driven Cross-modal Alignment for Brain CT Report Generation](https://aclanthology.org/2023.emnlp-main.408/)** — Aligns pathology-related graph information with images for brain CT report generation.
- **[Reformulating NLP tasks to Capture Longitudinal Manifestation of Language Disorders in People with Dementia.](https://aclanthology.org/2023.emnlp-main.986/)** — Models longitudinal language changes associated with dementia.

---

## NAACL

### NAACL 2025

#### 🤖 Foundation Models & Vision-Language

- **[Fact-Aware Multimodal Retrieval Augmentation for Accurate Medical Radiology Report Generation](https://aclanthology.org/2025.naacl-long.28/)** — FactMM-RAG trains a fact-aware retriever from RadGraph-derived report pairs to provide reference reports for radiology generation.
- **[Guiding Medical Vision-Language Models with Diverse Visual Prompts: Framework Design and Comprehensive Exploration of Prompt Variations](https://aclanthology.org/2025.naacl-long.587/)** — Studies diverse visual prompt designs for medical vision-language models.
- **[VividMed: Vision Language Model with Versatile Visual Grounding for Medicine](https://aclanthology.org/2025.naacl-long.89/)** — Supports segmentation masks and bounding boxes alongside VQA and report generation for both 2D and 3D medical images.

#### 📋 Clinical NLP, EHR & Healthcare

- **[Afrispeech-Dialog: A Benchmark Dataset for Spontaneous English Conversations in Healthcare and Beyond](https://aclanthology.org/2025.naacl-long.426/)** — Evaluates African-accented conversational speech recognition and how transcription errors affect medical dialogue summaries.
- **[A Layered Debating Multi-Agent System for Similar Disease Diagnosis](https://aclanthology.org/2025.naacl-short.46/)** — Uses layered multi-agent debate to distinguish similar disease diagnoses.
- **[Automatic Evaluation of Healthcare LLMs Beyond Question-Answering](https://aclanthology.org/2025.naacl-short.10/)** — Evaluates healthcare language models beyond conventional question answering.
- **[Benchmarking Large Language Models on Answering and Explaining Challenging Medical Questions](https://aclanthology.org/2025.naacl-long.182/)** — Introduces JAMA Clinical Challenge and Medbullets to evaluate medical question answering and explanations against expert-written references.
- **[Entangled Relations: Leveraging NLI and Meta-analysis to Enhance Biomedical Relation Extraction](https://aclanthology.org/2025.naacl-long.165/)** — Uses natural language inference and meta-analysis for biomedical relation extraction.
- **[Entity Decomposition with Filtering: A Zero-Shot Clinical Named Entity Recognition Framework](https://aclanthology.org/2025.naacl-long.150/)** — Decomposes entity extraction and filters predictions for zero-shot clinical named-entity recognition.
- **[How Can We Diagnose and Treat Bias in Large Language Models for Clinical Decision-Making?](https://aclanthology.org/2025.naacl-long.114/)** — Evaluates and mitigates bias in language-model clinical decisions.
- **[K-COMP: Retrieval-Augmented Medical Domain Question Answering With Knowledge-Injected Compressor](https://aclanthology.org/2025.naacl-long.351/)** — Compresses retrieved knowledge for medical question answering.
- **[KMI: A Dataset of Korean Motivational Interviewing Dialogues for Psychotherapy](https://aclanthology.org/2025.naacl-long.541/)** — Provides Korean motivational-interviewing conversations for psychotherapy research.
- **[Lived Experience Not Found: LLMs Struggle to Align with Experts on Addressing Adverse Drug Reactions from Psychiatric Medication Use](https://aclanthology.org/2025.naacl-long.553/)** — Evaluates whether language models reflect expert guidance on adverse psychiatric medication reactions.
- **[MeNTi: Bridging Medical Calculator and LLM Agent with Nested Tool Calling](https://aclanthology.org/2025.naacl-long.263/)** — Introduces a medical calculator agent and CalcQA benchmark covering tool selection, nested calculations, slot filling, and unit conversion.
- **[Multimodal Cognitive Reframing Therapy via Multi-hop Psychotherapeutic Reasoning](https://aclanthology.org/2025.naacl-long.250/)** — Models multimodal cognitive-reframing therapy through multihop psychotherapeutic reasoning.
- **[Rationale-Guided Retrieval Augmented Generation for Medical Question Answering](https://aclanthology.org/2025.naacl-long.635/)** — Uses rationales to guide retrieval-augmented medical question answering.
- **[Step-by-Step Fact Verification System for Medical Claims with Explainable Reasoning](https://aclanthology.org/2025.naacl-short.68/)** — Verifies medical claims through stepwise, explainable fact checking.
- **[SylloBio-NLI: Evaluating Large Language Models on Biomedical Syllogistic Reasoning](https://aclanthology.org/2025.naacl-long.371/)** — Evaluates biomedical syllogistic reasoning in language models.

#### 🧠 Neuroimaging, EEG & Brain AI

- **[FLIQA-AD: a Fusion Model with Large Language Model for Better Diagnose and MMSE Prediction of Alzheimer’s Disease](https://aclanthology.org/2025.naacl-short.49/)** — Combines multimodal information and language models for Alzheimer's diagnosis and cognitive-score prediction.

---

### NAACL 2024

#### 📋 Clinical NLP, EHR & Healthcare

- **[A Continued Pretrained LLM Approach for Automatic Medical Note Generation](https://aclanthology.org/2024.naacl-short.47/)** — Continues language-model pretraining for automatic medical-note generation.
- **[ALBA: Adaptive Language-Based Assessments for Mental Health](https://aclanthology.org/2024.naacl-long.136/)** — Uses adaptive language-based assessments to study mental-health evaluation.
- **[A Zero-Shot Monolingual Dual Stage Information Retrieval System for Spanish Biomedical Systematic Literature Reviews](https://aclanthology.org/2024.naacl-long.206/)** — Retrieves Spanish biomedical evidence for systematic literature reviews without task-specific training.
- **[CMB: A Comprehensive Medical Benchmark in Chinese](https://aclanthology.org/2024.naacl-long.343/)** — Provides a comprehensive Chinese-language medical evaluation benchmark.
- **[Depression Detection in Clinical Interviews with LLM-Empowered Structural Element Graph](https://aclanthology.org/2024.naacl-long.452/)** — Models structural elements of clinical interviews for depression detection.
- **[Diverse Perspectives, Divergent Models: Cross-Cultural Evaluation of Depression Detection on Twitter](https://aclanthology.org/2024.naacl-short.58/)** — Tests how depression detectors transfer across cultural and geographical populations.
- **[Event Detection from Social Media for Epidemic Prediction](https://aclanthology.org/2024.naacl-long.322/)** — Uses social-media event detection to support epidemic forecasting.
- **[Generating Mental Health Transcripts with SAPE (Spanish Adaptive Prompt Engineering)](https://aclanthology.org/2024.naacl-long.285/)** — Generates Spanish mental-health transcripts through adaptive prompt engineering.
- **[Improving Factuality in Clinical Abstractive Multi-Document Summarization by Guided Continued Pre-training](https://aclanthology.org/2024.naacl-short.66/)** — Improves factuality of clinical multi-document summaries through guided continued pretraining.
- **[Improving Pre-trained Language Model Sensitivity via Mask Specific losses: A case study on Biomedical NER](https://aclanthology.org/2024.naacl-long.280/)** — Uses mask-specific losses for biomedical named entity recognition.
- **[LLM-based Medical Assistant Personalization with Short- and Long-Term Memory Coordination](https://aclanthology.org/2024.naacl-long.132/)** — Memory coordination mechanism that balances short-term context and long-term patient history in LLM-based medical assistants for personalised clinical dialogue.
- **[Mapping Long-term Causalities in Psychiatric Symptomatology and Life Events from Social Media](https://aclanthology.org/2024.naacl-long.306/)** — Analyzes long-term links between psychiatric symptoms and life events in social-media data.
- **[Multi-stage Retrieve and Re-rank Model for Automatic Medical Coding Recommendation](https://aclanthology.org/2024.naacl-long.273/)** — Combines retrieval and reranking for automatic medical-code recommendation.
- **[On-the-fly Definition Augmentation of LLMs for Biomedical NER](https://aclanthology.org/2024.naacl-long.212/)** — Augments biomedical named entity recognition with on-the-fly definitions.
- **[Pregnant Questions: The Importance of Pragmatic Awareness in Maternal Health Question Answering](https://aclanthology.org/2024.naacl-long.403/)** — Evaluates pragmatic awareness in maternal-health question answering.
- **[Towards Reducing Diagnostic Errors with Interpretable Risk Prediction](https://aclanthology.org/2024.naacl-long.399/)** — Extracts EHR evidence to support interpretable diagnostic risk prediction.

#### 🧠 Neuroimaging, EEG & Brain AI

- **[MapGuide: A Simple yet Effective Method to Reconstruct Continuous Language from Brain Activities](https://aclanthology.org/2024.naacl-long.211/)** — Reconstructs continuous language from brain activity.

---

## AAAI

### AAAI 2025

#### 🔬 Medical Imaging & Segmentation

- **[AFiRe: Anatomy-Driven Self-Supervised Learning for Fine-Grained Representation in Radiographic Images](https://ojs.aaai.org/index.php/AAAI/article/view/34091)** — Learns anatomy-aware radiographic representations through self-supervision.
- **[AIF-SFDA: Autonomous Information Filter Driven Source-Free Domain Adaptation for Medical Image Segmentation](https://ojs.aaai.org/index.php/AAAI/article/view/32498)** — Filters information for source-free adaptation of medical segmentation models.
- **[A Trusted Lesion-assessment Network for Interpretable Diagnosis of Coronary Artery Disease in Coronary CT Angiography](https://ojs.aaai.org/index.php/AAAI/article/view/32642)** — Assesses coronary lesions with interpretable features from CT angiography.
- **[A Unified Degradation-Robust Approach to SSL and UDA for 3D Medical Images](https://ojs.aaai.org/index.php/AAAI/article/view/32466)** — Studies degradation-robust self-supervised learning and unsupervised adaptation for 3D medical images.
- **[A Unified Loss for Handling Inter-Class and Intra-Class Imbalance in Medical Image Segmentation](https://ojs.aaai.org/index.php/AAAI/article/view/32956)** — Addresses both inter-class and within-class imbalance in medical segmentation losses.
- **[Autoregressive Sequence Modeling for 3D Medical Image Representation](https://ojs.aaai.org/index.php/AAAI/article/view/32848)** — Learns 3D medical image representations through autoregressive sequence modeling.
- **[BLS-GAN: A Deep Layer Separation Framework for Eliminating Bone Overlap in Conventional Radiographs](https://ojs.aaai.org/index.php/AAAI/article/view/32826)** — Separates bone layers to reduce overlapping structures in conventional radiographs.
- **[Boosting ViT-based MRI Reconstruction from the Perspectives of Frequency Modulation, Spatial Purification, and Scale Diversification](https://ojs.aaai.org/index.php/AAAI/article/view/32656)** — Combines frequency, spatial, and scale information for transformer-based MRI reconstruction.
- **[Breaking Information Isolation: Accelerating MRI via Inter-sequence Mapping and Progressive Masking](https://ojs.aaai.org/index.php/AAAI/article/view/33147)** — Shares information between MRI sequences through progressive masking and inter-sequence mapping.
- **[BSAFusion: A Bidirectional Stepwise Feature Alignment Network for Unaligned Medical Image Fusion](https://ojs.aaai.org/index.php/AAAI/article/view/32499)** — Aligns features bidirectionally for fusion of unregistered medical modalities.
- **[ConDSeg: A General Medical Image Segmentation Framework via Contrast-Driven Feature Enhancement](https://ojs.aaai.org/index.php/AAAI/article/view/32482)** — Uses contrast-driven feature enhancement for medical segmentation.
- **[Deep Hierarchies and Invariant Disease-Indicative Feature Learning for Computer Aided Diagnosis of Multiple Fundus Diseases](https://ojs.aaai.org/index.php/AAAI/article/view/32566)** — Learns hierarchical and disease-indicative fundus features for ophthalmic diagnosis.
- **[Dual-calibrated Co-training Framework for Personalized Federated Semi-Supervised Medical Image Segmentation](https://ojs.aaai.org/index.php/AAAI/article/view/32671)** — Calibrates co-training for personalized federated semi-supervised medical segmentation.
- **[Efficient Deformable Convolutional Prompt for Continual Test-Time Adaptation in Medical Image Segmentation](https://ojs.aaai.org/index.php/AAAI/article/view/32591)** — Uses deformable convolutional prompts for continual adaptation of medical segmentation at inference.
- **[Every Component Counts: Rethinking the Measure of Success for Medical Semantic Segmentation in Multi-Instance Segmentation Tasks](https://ojs.aaai.org/index.php/AAAI/article/view/32408)** — Proposes CC-Metrics, revealing that standard mean-IoU severely underestimates segmentation failure on small/rare objects in multi-instance medical tasks.
- **[FAMNet: Frequency-aware Matching Network for Cross-domain Few-shot Medical Image Segmentation](https://ojs.aaai.org/index.php/AAAI/article/view/32184)** — Frequency-domain feature matching for few-shot segmentation across CT and MRI domains, mitigating texture/contrast shifts between scanners without expensive domain-specific retraining.
- **[FedVCK: Non-IID Robust and Communication-Efficient Federated Learning via Valuable Condensed Knowledge for Medical Image Analysis](https://ojs.aaai.org/index.php/AAAI/article/view/35497)** — Condenses useful knowledge for communication-efficient federated medical image analysis under non-identical distributions.
- **[GapMatch: Bridging Instance and Model Perturbations for Enhanced Semi-Supervised Medical Image Segmentation](https://ojs.aaai.org/index.php/AAAI/article/view/33919)** — Combines instance and model perturbations in semi-supervised medical segmentation.
- **[Generative Medical Segmentation](https://ojs.aaai.org/index.php/AAAI/article/view/32402)** — Reformulates medical image segmentation as a generative modeling problem, enabling open-vocabulary segmentation of arbitrary anatomical or pathological structures beyond fixed training categories.
- **[Gradient Alignment Improves Test-Time Adaptation for Medical Image Segmentation](https://ojs.aaai.org/index.php/AAAI/article/view/32244)** — Aligns gradients to improve test-time adaptation of medical segmentation.
- **[Label-Efficient Data Augmentation with Video Diffusion Models for Guidewire Segmentation in Cardiac Fluoroscopy](https://ojs.aaai.org/index.php/AAAI/article/view/32675)** — Augments fluoroscopy data with video diffusion for guidewire segmentation.
- **[Leveraging Anatomical Consistency for Multi-Object Detection in Ultrasound Images via Source-free Unsupervised Domain Adaptation](https://ojs.aaai.org/index.php/AAAI/article/view/32700)** — Uses anatomical consistency for source-free adaptation of ultrasound structure detection.
- **[Like an Ophthalmologist: Dynamic Selection Driven Multi-View Learning for Diabetic Retinopathy Grading](https://ojs.aaai.org/index.php/AAAI/article/view/34116)** — Dynamically selects views for diabetic retinopathy grading.
- **[MCAT: Visual Query-Based Localization of Standard Anatomical Clips in Fetal Ultrasound Videos Using Multi-Tier Class-Aware Token Transformer](https://ojs.aaai.org/index.php/AAAI/article/view/35047)** — Localizes standard anatomical clips in fetal ultrasound videos using visual queries. *[AI for Social Impact]*
- **[MonoBox: Tightness-Free Box-Supervised Polyp Segmentation Using Monotonicity Constraint](https://ojs.aaai.org/index.php/AAAI/article/view/32371)** — Segments polyps from bounding-box supervision using monotonicity constraints.
- **[Motion Artifact Removal in Pixel-Frequency Domain via Alternate Masks and Diffusion Model](https://ojs.aaai.org/index.php/AAAI/article/view/32960)** — Uses pixel and frequency information with complementary masks to remove MRI motion artifacts through a pretrained diffusion model.
- **[Multi-view Evidential Learning-based Medical Image Segmentation](https://ojs.aaai.org/index.php/AAAI/article/view/33911)** — Models evidence from multiple views for medical segmentation.
- **[Neighbor Does Matter: Density-Aware Contrastive Learning for Medical Semi-supervised Segmentation](https://ojs.aaai.org/index.php/AAAI/article/view/32776)** — Uses density-aware neighborhood contrastive learning for semi-supervised medical segmentation.
- **[ParseCaps: An Interpretable Parsing Capsule Network for Medical Image Diagnosis](https://ojs.aaai.org/index.php/AAAI/article/view/32321)** — Uses parsing capsule networks for interpretable medical image diagnosis.
- **[Rethinking U-Net: Task-Adaptive Mixture of Skip Connections for Enhanced Medical Image Segmentation](https://ojs.aaai.org/index.php/AAAI/article/view/32627)** — Adapts U-Net skip connections to medical segmentation tasks.
- **[S2S2: Semantic Stacking for Robust Semantic Segmentation in Medical Imaging](https://ojs.aaai.org/index.php/AAAI/article/view/32678)** — Stacks semantic information for robust medical segmentation.
- **[S³-Mamba: Small-Size-Sensitive Mamba for Lesion Segmentation](https://ojs.aaai.org/index.php/AAAI/article/view/32824)** — Improves sensitivity to small lesions through state-space segmentation modeling.
- **[SGTC: Semantic-Guided Triplet Co-training for Sparsely Annotated Semi-Supervised Medical Image Segmentation](https://ojs.aaai.org/index.php/AAAI/article/view/32986)** — Uses semantic guidance in triplet co-training for sparsely labeled medical segmentation.
- **[SIGraph: Saliency Image-Graph Network for Retinal Disease Classification in Fundus Image](https://ojs.aaai.org/index.php/AAAI/article/view/33090)** — Combines saliency images and graph representations for retinal disease classification.
- **[Single Exposure Quantitative Phase Imaging with a Conventional Microscope Using Diffusion Models](https://ojs.aaai.org/index.php/AAAI/article/view/32271)** — Combines chromatic aberrations and zero-mean diffusion to recover quantitative phase from a single microscope exposure, including clinical urine microscopy.
- **[SVRMamba: Slice-to-Volume Reconstruction from Multiple MRI Stacks with Slice Sequence Guided Mamba](https://ojs.aaai.org/index.php/AAAI/article/view/32907)** — Reconstructs MRI volumes from multiple stacks using slice-sequence state-space modeling.
- **[TCAM-Diff: Triplane-Aware Cross-Attention Medical Diffusion Model](https://ojs.aaai.org/index.php/AAAI/article/view/34433)** — Uses triplane-aware cross-attention in medical image diffusion.
- **[Towards a Comprehensive, Efficient and Promptable Anatomic Structure Segmentation Model Using 3D Whole-Body CT Scans](https://ojs.aaai.org/index.php/AAAI/article/view/32335)** — Builds an efficient promptable segmentation model for whole-body CT anatomy.
- **[Towards Realistic Semi-supervised Medical Image Classification](https://ojs.aaai.org/index.php/AAAI/article/view/32526)** — Studies realistic training and evaluation settings for semi-supervised medical image classification.
- **[U-KAN Makes Strong Backbone for Medical Image Segmentation and Generation](https://ojs.aaai.org/index.php/AAAI/article/view/32491)** — Integrates KAN (Kolmogorov-Arnold Network) layers into the U-Net pipeline on tokenized intermediate features, yielding a new backbone that achieves higher accuracy with lower compute on medical segmentation benchmarks.
- **[Unsupervised Self-Prior Embedding Neural Representation for Iterative Sparse-View CT Reconstruction](https://ojs.aaai.org/index.php/AAAI/article/view/32794)** — Uses self-prior implicit representations for iterative sparse-view CT reconstruction.
- **[VOILA: Complexity-Aware Universal Segmentation of CT Images by Voxel Interacting with Language](https://ojs.aaai.org/index.php/AAAI/article/view/32805)** — Combines language and voxel interactions for anatomy-aware CT segmentation.

#### 🧫 Computational Pathology & Microscopy

- **[A Gaussian Filter-Based 3D Registration Method for Series Section Electron Microscopy](https://ojs.aaai.org/index.php/AAAI/article/view/32103)** — Registers serial-section electron microscopy images with Gaussian-filter-based 3D alignment.
- **[Category Prompt Mamba Network for Nuclei Segmentation and Classification](https://ojs.aaai.org/index.php/AAAI/article/view/33116)** — Uses category prompts and state-space modeling for nuclei segmentation and classification.
- **[Dynamic Entity-Masked Graph Diffusion Model for Histopathology Image Representation Learning](https://ojs.aaai.org/index.php/AAAI/article/view/33202)** — Learns histopathology representations with entity-masked graph diffusion.
- **[Efficient Online Training for Zero-Shot Time-Lapse Microscopy Denoising and Super-Resolution](https://ojs.aaai.org/index.php/AAAI/article/view/32354)** — Denoises and super-resolves time-lapse microscopy images without task-specific training.
- **[From Representation Space to Prognostic Insights: Whole Slide Image Generation with Hierarchical Diffusion Model for Survival Prediction](https://ojs.aaai.org/index.php/AAAI/article/view/32788)** — Generates whole-slide representations with hierarchical diffusion for survival prediction.
- **[OODML: Whole Slide Image Classification Meets Online Pseudo-Supervision and Dynamic Mutual Learning](https://ojs.aaai.org/index.php/AAAI/article/view/33154)** — Combines online pseudo-label supervision and mutual learning for whole-slide classification.
- **[Promptable Representation Distribution Learning and Data Augmentation for Gigapixel Histopathology WSI Analysis](https://ojs.aaai.org/index.php/AAAI/article/view/32779)** — Models promptable feature distributions for augmentation and gigapixel pathology analysis.
- **[Queryable Prototype Multiple Instance Learning with Vision-Language Models for Incremental Whole Slide Image Classification](https://ojs.aaai.org/index.php/AAAI/article/view/32325)** — Uses queryable prototypes and vision-language representations for incremental whole-slide classification.
- **[Unpaired Multi-Domain Histopathology Virtual Staining Using Dual Path Prompted Inversion](https://ojs.aaai.org/index.php/AAAI/article/view/32949)** — Transfers histopathology staining across unpaired domains using prompted inversion.

#### 🤖 Foundation Models & Vision-Language

- **[DAMPER: A Dual-Stage Medical Report Generation Framework with Coarse-Grained MeSH Alignment and Fine-Grained Hypergraph Matching](https://ojs.aaai.org/index.php/AAAI/article/view/32393)** — Combines medical terminology alignment and hypergraph matching for radiology report generation.
- **[DuSSS: Dual Semantic Similarity-Supervised Vision-Language Model for Semi-Supervised Medical Image Segmentation](https://ojs.aaai.org/index.php/AAAI/article/view/32674)** — Uses dual semantic-similarity supervision in vision-language medical segmentation.
- **[Fine-grained Adaptive Visual Prompt for Generative Medical Visual Question Answering](https://ojs.aaai.org/index.php/AAAI/article/view/33047)** — Adapts fine-grained visual prompts for generative medical VQA.
- **[HC-LLM: Historical-Constrained Large Language Models for Radiology Report Generation](https://ojs.aaai.org/index.php/AAAI/article/view/32596)** — Uses historical information as constraints for radiology report generation.
- **[Incongruent Multimodal Federated Learning for Medical Vision and Language-based Multi-label Disease Detection](https://ojs.aaai.org/index.php/AAAI/article/view/35054)** — Handles mismatched modalities in federated image-language disease detection. *[AI for Social Impact]*
- **[KPL: Training-Free Medical Knowledge Mining of Vision-Language Models](https://ojs.aaai.org/index.php/AAAI/article/view/34075)** — Mines medical knowledge from vision-language models without training.
- **[LLM-RG4: Flexible and Factual Radiology Report Generation Across Diverse Input Contexts](https://ojs.aaai.org/index.php/AAAI/article/view/32890)** — Generates factual radiology reports from varying combinations of clinical inputs.
- **[Medical MLLM Is Vulnerable: Cross-Modality Jailbreak and Mismatched Attacks on Medical Multimodal Large Language Models](https://ojs.aaai.org/index.php/AAAI/article/view/32396)** — Evaluates jailbreak and mismatched-input vulnerabilities in medical multimodal language models.
- **[Overcoming Heterogeneous Data in Federated Medical Vision-Language Pre-training: A Triple-Embedding Model Selector Approach](https://ojs.aaai.org/index.php/AAAI/article/view/32807)** — Selects embedding models for federated medical vision-language pretraining under data heterogeneity.
- **[Perturbating, Tuning, and Collaborating: Harnessing Vision Foundation Models for Single Domain Generalization on Medical Imaging](https://ojs.aaai.org/index.php/AAAI/article/view/32571)** — Adapts visual foundation models to generalize medical imaging from a single domain.
- **[Radiology Report Generation via Multi-objective Preference Optimization](https://ojs.aaai.org/index.php/AAAI/article/view/32936)** — Optimizes multiple preference objectives for radiology report generation.
- **[Towards a Multimodal Large Language Model with Pixel-Level Insight for Biomedicine](https://ojs.aaai.org/index.php/AAAI/article/view/32394)** — Supports pixel-level biomedical image understanding with a multimodal language model.

#### 📋 Clinical NLP, EHR & Healthcare

- **[Aligning Time-series by Local Trends: Applications in Public Health](https://ojs.aaai.org/index.php/AAAI/article/view/35062)** — Aligns locally similar temporal trends in public-health time series. *[AI for Social Impact]*
- **[Anatomical Knowledge Mining and Matching for Semi-supervised Medical Multi-structure Detection](https://ojs.aaai.org/index.php/AAAI/article/view/32699)** — Mines anatomical relationships for semi-supervised detection of multiple medical structures.
- **[CA-MLIF: Cross-Attention and Multimodal Low-Rank Interaction Fusion Framework for Tumor Prognostic Prediction](https://ojs.aaai.org/index.php/AAAI/article/view/32170)** — Models multimodal interactions for tumor prognosis through cross-attention and low-rank fusion.
- **[CareBot: A Pioneering Full-Process Open-Source Medical Language Model](https://ojs.aaai.org/index.php/AAAI/article/view/34799)** — Introduces an open medical language-model training and adaptation pipeline.
- **[Context in Public Health for Underserved Communities: A Bayesian Approach to Online Restless Bandits](https://ojs.aaai.org/index.php/AAAI/article/view/35039)** — Studies context-aware allocation of public-health interventions to underserved communities. *[AI for Social Impact]*
- **[CUPCase: Clinically Uncommon Patient Cases and Diagnoses Dataset](https://ojs.aaai.org/index.php/AAAI/article/view/35050)** — Provides uncommon clinical cases for diagnostic evaluation. *[AI for Social Impact]*
- **[DearLLM: Enhancing Personalized Healthcare via Large Language Models-Deduced Feature Correlations](https://ojs.aaai.org/index.php/AAAI/article/view/32079)** — Uses language-model-inferred feature relationships for personalized healthcare prediction.
- **[DepMGNN: Matrixial Graph Neural Network for Video-based Automatic Depression Assessment](https://ojs.aaai.org/index.php/AAAI/article/view/32153)** — Uses matrix-valued graph modeling for video-based depression assessment.
- **[Distribution-Free Uncertainty Quantification in Mechanical Ventilation Treatment: A Conformal Deep Q-Learning Framework](https://ojs.aaai.org/index.php/AAAI/article/view/35013)** — Uses conformal risk control for offline reinforcement learning in mechanical ventilation. *[AI for Social Impact]*
- **[Domain Generalized Medical Landmark Detection via Robust Boundary-Aware Pre-Training](https://ojs.aaai.org/index.php/AAAI/article/view/32323)** — Pretrains boundary-aware features for medical landmark detection across domains.
- **[Dr. Tongue: Sign-Oriented Multi-label Detection for Remote Tongue Diagnosis](https://ojs.aaai.org/index.php/AAAI/article/view/32230)** — Detects multiple tongue signs for remote diagnostic support.
- **[Enhancing Healthcare Recommendations: A Privacy-Protective and Interpretable Cross-Domain Framework](https://ojs.aaai.org/index.php/AAAI/article/view/33322)** — Studies interpretable cross-domain healthcare recommendation with privacy protection.
- **[Evaluating Index-based Treatment Allocation in Underresourced Communities](https://ojs.aaai.org/index.php/AAAI/article/view/35001)** — Evaluates index-based resource allocation, including a mobile-health program for pregnant women. *[AI for Social Impact]*
- **[Fair Federated Survival Analysis](https://ojs.aaai.org/index.php/AAAI/article/view/34214)** — Studies demographic fairness and censoring disparities in federated survival analysis.
- **[HHAN: Comprehensive Infectious Disease Source Tracing via Heterogeneous Hypergraph Neural Network](https://ojs.aaai.org/index.php/AAAI/article/view/32006)** — Traces infectious-disease sources with heterogeneous hypergraphs.
- **[HI-DR: Exploiting Health Status-Aware Attention and an EHR Graph+ for Effective Medication Recommendation](https://ojs.aaai.org/index.php/AAAI/article/view/33301)** — Uses patient health status and EHR graphs for medication recommendation.
- **[Hierarchical Divide-and-Conquer for Fine-Grained Alignment in LLM-Based Medical Evaluation](https://ojs.aaai.org/index.php/AAAI/article/view/34803)** — Decomposes medical evaluation into hierarchically aligned subtasks.
- **[How Your Location Relates to Health: Variable Importance and Interpretable Machine Learning for Environmental and Sociodemographic Data](https://ojs.aaai.org/index.php/AAAI/article/view/35044)** — Models relationships between location, environmental context, sociodemographics, and health. *[AI for Social Impact]*
- **[Incomplete Modality Disentangled Representation for Ophthalmic Disease Grading and Diagnosis](https://ojs.aaai.org/index.php/AAAI/article/view/32570)** — Disentangles incomplete multimodal information for ophthalmic diagnosis and disease grading.
- **[Integrating Sequence and Image Modeling in Irregular Medical Time Series Through Self-Supervised Learning](https://ojs.aaai.org/index.php/AAAI/article/view/33737)** — Jointly models sequence and image views of irregular medical time series.
- **[Knowledge-Guided Domain Adaptation Model for Transferring Drug Response Prediction from Cell Lines to Patients](https://ojs.aaai.org/index.php/AAAI/article/view/32032)** — Transfers drug-response models from cell lines to patients using clinical knowledge and domain adaptation.
- **[LLaVA Needs More Knowledge: Retrieval Augmented Natural Language Generation with Knowledge Graph for Explaining Thoracic Pathologies](https://ojs.aaai.org/index.php/AAAI/article/view/32342)** — Retrieves knowledge-graph evidence to explain thoracic pathology findings.
- **[M2OST: Many-to-one Regression for Predicting Spatial Transcriptomics from Digital Pathology Images](https://ojs.aaai.org/index.php/AAAI/article/view/32830)** — Predicts spatial transcriptomic measurements from digital pathology images.
- **[MDD-5k: A New Diagnostic Conversation Dataset for Mental Disorders Synthesized via Neuro-Symbolic LLM Agents](https://ojs.aaai.org/index.php/AAAI/article/view/34763)** — Synthesizes diagnostic conversations about mental disorders with neuro-symbolic language-model agents.
- **[MEATRD: Multimodal Anomalous Tissue Region Detection Enhanced with Spatial Transcriptomics](https://ojs.aaai.org/index.php/AAAI/article/view/33409)** — Detects anomalous tissue regions with spatial transcriptomics information.
- **[Medical Manifestation-Aware De-Identification](https://ojs.aaai.org/index.php/AAAI/article/view/34835)** — Preserves relevant medical manifestations while de-identifying clinical data.
- **[Medical Multimodal Model Stealing Attacks via Adversarial Domain Alignment](https://ojs.aaai.org/index.php/AAAI/article/view/32734)** — Studies medical multimodal model-stealing attacks through adversarial domain alignment.
- **[MEDSAGE: Enhancing Robustness of Medical Dialogue Summarization to ASR Errors with LLM-generated Synthetic Dialogues](https://ojs.aaai.org/index.php/AAAI/article/view/34518)** — Generates synthetic dialogues to improve medical summarization under speech-recognition errors.
- **[Memorize and Rank: Elevating Large Language Models for Clinical Diagnosis Prediction](https://ojs.aaai.org/index.php/AAAI/article/view/34660)** — Uses memorization and ranking to improve clinical diagnosis prediction.
- **[MMPF: Multi-Modal Perception Framework for Abnormal Medical Condition Detection](https://ojs.aaai.org/index.php/AAAI/article/view/33157)** — Combines multiple modalities to detect abnormal medical conditions.
- **[Multi-OphthaLingua: A Multilingual Benchmark for Assessing and Debiasing LLM Ophthalmological QA in LMICs](https://ojs.aaai.org/index.php/AAAI/article/view/35053)** — Evaluates multilingual ophthalmology question answering and demographic bias in low-resource settings. *[AI for Social Impact]*
- **[Parallel-Learning of Invariant and Tempo-variant Attributes of Single-Lead Cardiac Signals: PLITA](https://ojs.aaai.org/index.php/AAAI/article/view/33693)** — Separates invariant and time-varying attributes of single-lead cardiac signals.
- **[PersonalizedUS: Interpretable Breast Cancer Risk Assessment with Local Coverage Uncertainty Quantification](https://ojs.aaai.org/index.php/AAAI/article/view/35017)** — Provides interpretable breast-cancer risk assessment with local coverage uncertainty estimates. *[AI for Social Impact]*
- **[Step-Calibrated Diffusion for Biomedical Optical Image Restoration](https://ojs.aaai.org/index.php/AAAI/article/view/32635)** — Restores biomedical optical images with diffusion models.
- **[Trustworthy and Practical AI for Healthcare: A Guided Deferral System with Large Language Models](https://ojs.aaai.org/index.php/AAAI/article/view/35063)** — Combines language models with guided deferral for healthcare decisions. *[AI for Social Impact]*
- **[VidSole: A Multimodal Dataset for Joint Kinetics Quantification and Disease Detection with Deep Learning](https://ojs.aaai.org/index.php/AAAI/article/view/35033)** — Provides multimodal data for joint kinetics measurement and disease detection. *[AI for Social Impact]*
- **[XTSFormer: Cross-Temporal-Scale Transformer for Irregular-Time Event Prediction in Clinical Applications](https://ojs.aaai.org/index.php/AAAI/article/view/35073)** — Models clinical events with transformers spanning multiple temporal scales. *[AI for Social Impact]*

#### 🧠 Neuroimaging, EEG & Brain AI

- **[Accessible, At-Home Detection of Parkinson’s Disease via Multi-Task Video Analysis](https://ojs.aaai.org/index.php/AAAI/article/view/35031)** — Uses multitask video analysis for accessible at-home Parkinson's disease detection. *[AI for Social Impact]*
- **[A Compact Implicit Neural Representation for Efficient Storage of Massive 4D Functional Magnetic Resonance Imaging](https://ojs.aaai.org/index.php/AAAI/article/view/32520)** — Compresses large four-dimensional fMRI recordings with implicit neural representations.
- **[BrainGuard: Privacy-Preserving Multisubject Image Reconstructions from Brain Activities](https://ojs.aaai.org/index.php/AAAI/article/view/33579)** — Protects privacy in multi-subject brain image reconstruction.
- **[BrainMAP: Learning Multiple Activation Pathways in Brain Networks](https://ojs.aaai.org/index.php/AAAI/article/view/33581)** — Maps activation pathways in brain networks.
- **[Breaking Data Silos in Parkinson’s Disease Diagnosis: An Adaptive Federated Learning Approach for Privacy-Preserving Facial Expression Analysis](https://ojs.aaai.org/index.php/AAAI/article/view/33572)** — Uses adaptive federated facial-expression analysis for privacy-preserving Parkinson's disease assessment.
- **[CLIP-MSM: A Multi-Semantic Mapping Brain Representation for Human High-Level Visual Cortex](https://ojs.aaai.org/index.php/AAAI/article/view/32994)** — Models visual cortex responses with CLIP-based semantic representations.
- **[CognitionCapturer: Decoding Visual Stimuli from Human EEG Signal with Multimodal Information](https://ojs.aaai.org/index.php/AAAI/article/view/33587)** — Decodes visual stimuli from EEG using multimodal information.
- **[DeCorrNet: Enhancing Neural Decoding Performance by Eliminating Correlations in Noise](https://ojs.aaai.org/index.php/AAAI/article/view/33577)** — Removes correlated neural noise to improve decoding for brain-computer interfaces.
- **[DECT: Harnessing LLM-assisted Fine-Grained Linguistic Knowledge and Label-Switched and Label-Preserved Data Generation for Diagnosis of Alzheimer’s Disease](https://ojs.aaai.org/index.php/AAAI/article/view/34671)** — Uses language-assisted data generation for Alzheimer's disease diagnosis.
- **[Long-Term EEG Partitioning for Seizure Onset Detection](https://ojs.aaai.org/index.php/AAAI/article/view/33557)** — Partitions long EEG recordings for seizure-onset detection.
- **[Manhattan Self-Attention Diffusion Residual Networks with Dynamic Bias Rectiﬁcation for BCI-based Few-Shot Learning](https://ojs.aaai.org/index.php/AAAI/article/view/33580)** — Uses diffusion residual networks and adaptive bias correction for few-shot brain-computer interfaces.
- **[MarkovType: A Markov Decision Process Strategy for Non-Invasive Brain-Computer Interfaces Typing Systems](https://ojs.aaai.org/index.php/AAAI/article/view/35064)** — Models non-invasive brain-computer-interface typing as a Markov decision process. *[AI for Social Impact]*
- **[MEPNet: Medical Entity-Balanced Prompting Network for Brain CT Report Generation](https://ojs.aaai.org/index.php/AAAI/article/view/34788)** — Balances medical entities in prompts for brain CT report generation.
- **[MindPainter: Efficient Brain-Conditioned Painting of Natural Images via Cross-Modal Self-Supervised Learning](https://ojs.aaai.org/index.php/AAAI/article/view/33585)** — Generates images conditioned on brain activity.
- **[NeuralFlix: A Simple While Effective Framework for Semantic Decoding of Videos from Non-invasive Brain Recordings](https://ojs.aaai.org/index.php/AAAI/article/view/32762)** — Decodes video semantics from brain activity.
- **[See Through Their Minds: Learning Transferable Brain Decoding Models from Cross-Subject fMRI](https://ojs.aaai.org/index.php/AAAI/article/view/32611)** — Transfers visual decoding across subjects' fMRI recordings.
- **[Semantic-guided Masked Mutual Learning for Multi-modal Brain Tumor Segmentation with Arbitrary Missing Modalities](https://ojs.aaai.org/index.php/AAAI/article/view/32545)** — Uses semantic-guided mutual learning for brain tumor segmentation with missing modalities.
- **[Wills Aligner: Multi-Subject Collaborative Brain Visual Decoding](https://ojs.aaai.org/index.php/AAAI/article/view/33554)** — Aligns neural representations across subjects for brain decoding.

#### 🫀 Physiological Signals & Medical Time Series

- **[AnchorInv: Few-Shot Class-Incremental Learning of Physiological Signals via Feature Space-Guided Inversion](https://ojs.aaai.org/index.php/AAAI/article/view/33563)** — Uses feature-guided inversion for few-shot incremental physiological-signal classification.
- **[Personalized Sleep Staging Leveraging Source-free Unsupervised Domain Adaptation](https://ojs.aaai.org/index.php/AAAI/article/view/33592)** — Personalizes sleep staging through source-free unsupervised adaptation.
- **[PhysDiff: Physiology-based Dynamicity Disentangled Diffusion Model for Remote Physiological Measurement](https://ojs.aaai.org/index.php/AAAI/article/view/32704)** — Disentangles physiological dynamics in diffusion-based remote vital-sign measurement.
- **[RhythmMamba: Fast, Lightweight, and Accurate Remote Physiological Measurement](https://ojs.aaai.org/index.php/AAAI/article/view/33204)** — Uses lightweight state-space modeling for remote physiological measurement.

#### 🏥 Surgical AI

- **[Surgical Workflow Recognition and Blocking Effectiveness Detection in Laparoscopic Liver Resection with Pringle Maneuver](https://ojs.aaai.org/index.php/AAAI/article/view/32332)** — Recognizes surgical workflows and vascular-blocking effectiveness in laparoscopic liver resection.
- **[Unsupervised Photometric-Consistent Depth Estimation from Endoscopic Monocular Video](https://ojs.aaai.org/index.php/AAAI/article/view/32521)** — Estimates endoscopic depth from monocular video using photometric consistency.

---

### AAAI 2024

#### 🔬 Medical Imaging & Segmentation

- **[An Embedding-Unleashing Video Polyp Segmentation Framework via Region Linking and Scale Alignment](https://ojs.aaai.org/index.php/AAAI/article/view/27942)** — Links regions across frames and scales for video polyp segmentation.
- **[A Robust Mutual-Reinforcing Framework for 3D Multi-Modal Medical Image Fusion Based on Visual-Semantic Consistency](https://ojs.aaai.org/index.php/AAAI/article/view/28536)** — Fuses 3D medical modalities using mutually reinforcing visual-semantic consistency.
- **[CariesXrays: Enhancing Caries Detection in Hospital-Scale Panoramic Dental X-rays via Feature Pyramid Contrastive Learning](https://ojs.aaai.org/index.php/AAAI/article/view/30196)** — Uses contrastive feature pyramids for caries detection in panoramic dental X-rays. *[AI for Social Impact]*
- **[Combinatorial CNN-Transformer Learning with Manifold Constraints for Semi-supervised Medical Image Segmentation](https://ojs.aaai.org/index.php/AAAI/article/view/28007)** — Combines convolutional and transformer learning under manifold constraints for semi-supervised segmentation.
- **[Combining Graph Transformers Based Multi-Label Active Learning and Informative Data Augmentation for Chest Xray Classification](https://ojs.aaai.org/index.php/AAAI/article/view/30133)** — Combines active learning and augmentation for multilabel chest X-ray classification.
- **[DTMFormer: Dynamic Token Merging for Boosting Transformer-Based Medical Image Segmentation](https://ojs.aaai.org/index.php/AAAI/article/view/28394)** — Merges tokens dynamically to improve transformer-based medical segmentation.
- **[FedA3I: Annotation Quality-Aware Aggregation for Federated Medical Image Segmentation against Heterogeneous Annotation Noise](https://ojs.aaai.org/index.php/AAAI/article/view/29525)** — Accounts for heterogeneous annotation quality in federated medical segmentation.
- **[HACDR-Net: Heterogeneous-Aware Convolutional Network for Diabetic Retinopathy Multi-Lesion Segmentation](https://ojs.aaai.org/index.php/AAAI/article/view/28453)** — Segments diabetic retinopathy lesions with heterogeneous-aware convolutions.
- **[Learning Generalized Medical Image Segmentation from Decoupled Feature Queries](https://ojs.aaai.org/index.php/AAAI/article/view/27839)** — Uses decoupled feature queries for generalizable medical segmentation.
- **[MedSegDiff-V2: Diffusion-Based Medical Image Segmentation with Transformer](https://ojs.aaai.org/index.php/AAAI/article/view/28418)** — Upgraded diffusion segmentation framework that replaces the UNet denoiser with a Transformer backbone, outperforming prior diffusion-based segmentation models across multiple modalities.
- **[MFTN: Multi-Level Feature Transfer Network Based on MRI-Transformer for MR Image Super-resolution](https://ojs.aaai.org/index.php/AAAI/article/view/28011)** — Transfers multilevel features for MRI super-resolution.
- **[NaMa: Neighbor-Aware Multi-Modal Adaptive Learning for Prostate Tumor Segmentation on Anisotropic MR Images](https://ojs.aaai.org/index.php/AAAI/article/view/28215)** — Uses neighboring slices and multimodal adaptation for prostate segmentation in anisotropic MRI.
- **[NeBLa: Neural Beer-Lambert for 3D Reconstruction of Oral Structures from Panoramic Radiographs](https://ojs.aaai.org/index.php/AAAI/article/view/28241)** — Reconstructs oral anatomy from panoramic radiographs using a neural Beer-Lambert formulation.
- **[Novel Class Discovery in Chest X-rays via Paired Images and Text](https://ojs.aaai.org/index.php/AAAI/article/view/28598)** — Discovers new disease classes from paired chest X-rays and text.
- **[Null Space Matters: Range-Null Decomposition for Consistent Multi-Contrast MRI Reconstruction](https://ojs.aaai.org/index.php/AAAI/article/view/27869)** — Separates range and null-space components for consistent multicontrast MRI reconstruction.
- **[Polyper: Boundary Sensitive Polyp Segmentation](https://ojs.aaai.org/index.php/AAAI/article/view/28274)** — Uses boundary-sensitive modeling for polyp segmentation.
- **[Rolling-Unet: Revitalizing MLP’s Ability to Efficiently Extract Long-Distance Dependencies for Medical Image Segmentation](https://ojs.aaai.org/index.php/AAAI/article/view/28173)** — Models long-range dependencies efficiently within a medical segmentation U-Net.
- **[Sparse Bayesian Deep Learning for Cross Domain Medical Image Reconstruction](https://ojs.aaai.org/index.php/AAAI/article/view/28008)** — Uses sparse Bayesian modeling for cross-domain medical image reconstruction.
- **[SuperJunction: Learning-Based Junction Detection for Retinal Image Registration](https://ojs.aaai.org/index.php/AAAI/article/view/27782)** — Detects vascular junctions for retinal image registration.
- **[Test-Time Adaptation via Style and Structure Guidance for Histological Image Registration](https://ojs.aaai.org/index.php/AAAI/article/view/28601)** — Guides test-time adaptation of histological registration through style and structure.

#### 🧫 Computational Pathology & Microscopy

- **[Boosting Multiple Instance Learning Models for Whole Slide Image Classification: A Model-Agnostic Framework Based on Counterfactual Inference](https://ojs.aaai.org/index.php/AAAI/article/view/28135)** — Uses counterfactual inference to improve whole-slide multiple-instance classifiers.
- **[CaMIL: Causal Multiple Instance Learning for Whole Slide Image Classification](https://ojs.aaai.org/index.php/AAAI/article/view/27873)** — Addresses confounding in whole-slide classification through causal multiple-instance learning.
- **[Cell Graph Transformer for Nuclei Classification](https://ojs.aaai.org/index.php/AAAI/article/view/28179)** — Uses cell graphs for nucleus classification in pathology images.
- **[Electron Microscopy Images as Set of Fragments for Mitochondrial Segmentation](https://ojs.aaai.org/index.php/AAAI/article/view/28191)** — Segments mitochondria in electron microscopy images.
- **[Inertial Algorithm with Dry Fraction and Convolutional Sparse Coding for 3D Localization with Light Field Microscopy](https://ojs.aaai.org/index.php/AAAI/article/view/30072)** — Localizes structures in three dimensions using light-field microscopy.
- **[Memory-Efficient Prompt Tuning for Incremental Histopathology Classification](https://ojs.aaai.org/index.php/AAAI/article/view/28615)** — Tunes prompts efficiently for incremental histopathology classification.
- **[Point Transformer with Federated Learning for Predicting Breast Cancer HER2 Status from Hematoxylin and Eosin-Stained Whole Slide Images](https://ojs.aaai.org/index.php/AAAI/article/view/28082)** — Uses federated point transformers to predict HER2 status from whole-slide histology.
- **[Transformer-Based Video-Structure Multi-Instance Learning for Whole Slide Image Classification](https://ojs.aaai.org/index.php/AAAI/article/view/29338)** — Combines video-structure modeling and multiple-instance learning for whole-slide classification.
- **[UniCell: Universal Cell Nucleus Classification via Prompt Learning](https://ojs.aaai.org/index.php/AAAI/article/view/28009)** — Uses prompting for universal nucleus classification.

#### 🤖 Foundation Models & Vision-Language

- **[Automatic Radiology Reports Generation via Memory Alignment Network](https://ojs.aaai.org/index.php/AAAI/article/view/28279)** — Aligns visual and textual memories for radiology report generation.
- **[PromptMRG: Diagnosis-Driven Prompts for Medical Report Generation](https://ojs.aaai.org/index.php/AAAI/article/view/28038)** — Conditions medical report generation on diagnostic prompts.

#### 📋 Clinical NLP, EHR & Healthcare

- **[AMD: Anatomical Motion Diffusion with Interpretable Motion Decomposition and Fusion](https://ojs.aaai.org/index.php/AAAI/article/view/28042)** — Models anatomical motion through interpretable diffusion-based decomposition and fusion.
- **[BAND: Biomedical Alert News Dataset](https://ojs.aaai.org/index.php/AAAI/article/view/29757)** — Provides a biomedical news dataset for language modeling and evaluation.
- **[Bootstrapping Large Language Models for Radiology Report Generation](https://ojs.aaai.org/index.php/AAAI/article/view/29826)** — Curriculum bootstrapping strategy that uses an LLM to iteratively generate and filter pseudo-labeled reports for self-training, improving radiology report quality with minimal annotated data.
- **[Characterizing Information Seeking Events in Health-Related Social Discourse](https://ojs.aaai.org/index.php/AAAI/article/view/30241)** — Studies health information seeking in social discourse. *[AI for Social Impact]*
- **[CLIPSyntel: CLIP and LLM Synergy for Multimodal Question Summarization in Healthcare](https://ojs.aaai.org/index.php/AAAI/article/view/30206)** — Combines image-language representations and language models to summarize healthcare questions. *[AI for Social Impact]*
- **[Collaborative Synthesis of Patient Records through Multi-Visit Health State Inference](https://ojs.aaai.org/index.php/AAAI/article/view/29871)** — Synthesizes patient records through inference across multiple visits.
- **[Collaborative Tooth Motion Diffusion Model in Digital Orthodontics](https://ojs.aaai.org/index.php/AAAI/article/view/27935)** — Generates coordinated tooth movements for digital orthodontics with diffusion modeling.
- **[ConSequence: Synthesizing Logically Constrained Sequences for Electronic Health Record Generation](https://ojs.aaai.org/index.php/AAAI/article/view/29460)** — Synthesizes EHR event sequences subject to logical constraints.
- **[Constraint Latent Space Matters: An Anti-anomalous Waveform Transformation Solution from Photoplethysmography to Arterial Blood Pressure](https://ojs.aaai.org/index.php/AAAI/article/view/28985)** — Translates photoplethysmography to arterial blood pressure with constrained latent representations.
- **[Deep Reinforcement Learning for Early Diagnosis of Lung Cancer](https://ojs.aaai.org/index.php/AAAI/article/view/30248)** — Uses deep reinforcement learning to support early lung-cancer diagnosis. *[AI for Social Impact]*
- **[Depression Detection via Capsule Networks with Contrastive Learning](https://ojs.aaai.org/index.php/AAAI/article/view/30228)** — Uses contrastive capsule-network representations for depression detection. *[AI for Social Impact]*
- **[DPA-P2PNet: Deformable Proposal-Aware P2PNet for Accurate Point-Based Cell Detection](https://ojs.aaai.org/index.php/AAAI/article/view/28289)** — Detects cells from point annotations using deformable proposal-aware prediction.
- **[DrFuse: Learning Disentangled Representation for Clinical Multi-Modal Fusion with Missing Modality and Modal Inconsistency](https://ojs.aaai.org/index.php/AAAI/article/view/29578)** — Disentangles clinical modalities to handle missing inputs and inconsistent information.
- **[HDformer: A Higher-Dimensional Transformer for Detecting Diabetes Utilizing Long-Range Vascular Signals](https://ojs.aaai.org/index.php/AAAI/article/view/29233)** — Uses long-range vascular information for diabetes detection.
- **[IGAMT: Privacy-Preserving Electronic Health Record Synthesization with Heterogeneity and Irregularity](https://ojs.aaai.org/index.php/AAAI/article/view/29491)** — Synthesizes privacy-preserving EHRs with heterogeneous, irregular observations.
- **[IVP-VAE: Modeling EHR Time Series with Initial Value Problem Solvers](https://ojs.aaai.org/index.php/AAAI/article/view/29534)** — Models EHR time series using variational representations and initial-value-problem solvers.
- **[KG-TREAT: Pre-training for Treatment Effect Estimation by Synergizing Patient Data with Knowledge Graphs](https://ojs.aaai.org/index.php/AAAI/article/view/28727)** — Combines patient information and knowledge graphs in pretraining for treatment-effect estimation.
- **[Large Language Models Are Clinical Reasoners: Reasoning-Aware Diagnosis Framework with Prompt-Generated Rationales](https://ojs.aaai.org/index.php/AAAI/article/view/29802)** — Generates rationales to support language-model clinical reasoning.
- **[MedAlign: A Clinician-Generated Dataset for Instruction Following with Electronic Medical Records](https://ojs.aaai.org/index.php/AAAI/article/view/30205)** — Expert-annotated dataset benchmarking LLM instruction-following in EHR contexts across diverse clinical tasks. *[AI for Social Impact]*
- **[MedBench: A Large-Scale Chinese Benchmark for Evaluating Medical Large Language Models](https://ojs.aaai.org/index.php/AAAI/article/view/29723)** — Provides a large Chinese-language benchmark for medical language models.
- **[MICA: Towards Explainable Skin Lesion Diagnosis via Multi-Level Image-Concept Alignment](https://ojs.aaai.org/index.php/AAAI/article/view/27842)** — Aligns skin images with clinical concepts for explainable lesion diagnosis.
- **[Mining Gaze for Contrastive Learning toward Computer-Assisted Diagnosis](https://ojs.aaai.org/index.php/AAAI/article/view/28586)** — Uses clinician gaze as contrastive supervision for computer-assisted diagnosis.
- **[Outlier Ranking for Large-Scale Public Health Data](https://ojs.aaai.org/index.php/AAAI/article/view/30222)** — Ranks anomalous observations in large public-health datasets. *[AI for Social Impact]*
- **[PathAsst: A Generative Foundation AI Assistant towards Artificial General Intelligence of Pathology](https://ojs.aaai.org/index.php/AAAI/article/view/28308)** — Introduces a generative multimodal assistant for pathology tasks.
- **[VITA: ‘Carefully Chosen and Weighted Less’ Is Better in Medication Recommendation](https://ojs.aaai.org/index.php/AAAI/article/view/28704)** — Selects and weights clinical information for medication recommendation.
- **[Zhongjing: Enhancing the Chinese Medical Capabilities of Large Language Model through Expert Feedback and Real-World Multi-Turn Dialogue](https://ojs.aaai.org/index.php/AAAI/article/view/29907)** — Aligns a Chinese medical language model through expert feedback and clinical dialogue.

#### 🧠 Neuroimaging, EEG & Brain AI

- **[A Local-Ascending-Global Learning Strategy for Brain-Computer Interface](https://ojs.aaai.org/index.php/AAAI/article/view/28867)** — Learns local-to-global representations for brain-computer interfaces.
- **[Beyond Mimicking Under-Represented Emotions: Deep Data Augmentation with Emotional Subspace Constraints for EEG-Based Emotion Recognition](https://ojs.aaai.org/index.php/AAAI/article/view/28891)** — Augments underrepresented emotional patterns in EEG through constrained latent subspaces.
- **[Bridging the Semantic Latent Space between Brain and Machine: Similarity Is All You Need](https://ojs.aaai.org/index.php/AAAI/article/view/29009)** — Aligns fMRI representations with the semantic latent space of vision-language models.
- **[DMMR: Cross-Subject Domain Generalization for EEG-Based Emotion Recognition via Denoising Mixed Mutual Reconstruction](https://ojs.aaai.org/index.php/AAAI/article/view/27819)** — Reconstructs mixed EEG information for cross-subject emotion generalization.
- **[Federated Modality-Specific Encoders and Multimodal Anchors for Personalized Brain Tumor Segmentation](https://ojs.aaai.org/index.php/AAAI/article/view/27909)** — Personalizes brain tumor segmentation with federated modality-specific encoders and shared anchors.
- **[MetaRLEC: Meta-Reinforcement Learning for Discovery of Brain Effective Connectivity](https://ojs.aaai.org/index.php/AAAI/article/view/28892)** — Estimates effective connectivity in brain networks with meta-reinforcement learning.
- **[TMFormer: Token Merging Transformer for Brain Tumor Segmentation with Missing Modalities](https://ojs.aaai.org/index.php/AAAI/article/view/28572)** — Merges tokens for brain tumor segmentation with missing imaging modalities.

#### 🫀 Physiological Signals & Medical Time Series

- **[Fusion-Vital: Video-RF Fusion Transformer for Advanced Remote Physiological Measurement](https://ojs.aaai.org/index.php/AAAI/article/view/27898)** — Fuses video and radio-frequency measurements for remote physiological sensing.
- **[Generalizable Sleep Staging via Multi-Level Domain Alignment](https://ojs.aaai.org/index.php/AAAI/article/view/27779)** — Aligns domains at multiple levels for generalizable sleep staging.
- **[Region-Disentangled Diffusion Model for High-Fidelity PPG-to-ECG Translation](https://ojs.aaai.org/index.php/AAAI/article/view/29422)** — Translates PPG to ECG with region-disentangled diffusion.

#### 🏥 Surgical AI

- **[SurgicalSAM: Efficient Class Promptable Surgical Instrument Segmentation](https://ojs.aaai.org/index.php/AAAI/article/view/28514)** — Adapts SAM with prototype-based class prompts and contrastive learning for surgical instrument segmentation without manually specified points or boxes.

---

### AAAI 2023

#### 🔬 Medical Imaging & Segmentation

- **[ACL-Net: Semi-supervised Polyp Segmentation via Affinity Contrastive Learning](https://ojs.aaai.org/index.php/AAAI/article/view/25382)** — Uses affinity-based contrastive learning for semi-supervised polyp segmentation.
- **[CCQ: Cross-Class Query Network for Partially Labeled Organ Segmentation](https://ojs.aaai.org/index.php/AAAI/article/view/25264)** — Uses cross-class queries for organ segmentation with incomplete labels.
- **[ClassFormer: Exploring Class-Aware Dependency with Transformer for Medical Image Segmentation](https://ojs.aaai.org/index.php/AAAI/article/view/25171)** — Models class-aware dependencies with transformers for medical segmentation.
- **[Leveraging Old Knowledge to Continually Learn New Classes in Medical Images](https://ojs.aaai.org/index.php/AAAI/article/view/26659)** — Continually recognizes new medical image classes while retaining prior knowledge. *[AI for Social Impact]*
- **[MVCINN: Multi-View Diabetic Retinopathy Detection Using a Deep Cross-Interaction Neural Network](https://ojs.aaai.org/index.php/AAAI/article/view/26080)** — Combines multiple retinal views through cross-interaction for diabetic retinopathy detection.
- **[Reconstructing an Epidemic Outbreak Using Steiner Connectivity](https://ojs.aaai.org/index.php/AAAI/article/view/26372)** — Reconstructs epidemic outbreaks using network connectivity constraints.
- **[Reducing Domain Gap in Frequency and Spatial Domain for Cross-Modality Domain Adaptation on Medical Image Segmentation](https://ojs.aaai.org/index.php/AAAI/article/view/25260)** — Aligns frequency and spatial features across modalities for medical segmentation.
- **[Rethinking Data Augmentation for Single-Source Domain Generalization in Medical Image Segmentation](https://ojs.aaai.org/index.php/AAAI/article/view/25332)** — Studies augmentation for single-source generalization in medical segmentation.
- **[Super-efficient Echocardiography Video Segmentation via Proxy- and Kernel-Based Semi-supervised Learning](https://ojs.aaai.org/index.php/AAAI/article/view/25381)** — Uses proxy and kernel-based semi-supervised learning for efficient echocardiography segmentation.
- **[Unsupervised Domain Adaptation for Medical Image Segmentation by Selective Entropy Constraints and Adaptive Semantic Alignment](https://ojs.aaai.org/index.php/AAAI/article/view/25138)** — Combines selective entropy constraints with adaptive semantic alignment for unsupervised medical segmentation domain adaptation.

#### 🧫 Computational Pathology & Microscopy

- **[HVTSurv: Hierarchical Vision Transformer for Patient-Level Survival Prediction from Whole Slide Image](https://ojs.aaai.org/index.php/AAAI/article/view/25315)** — Predicts patient survival from whole-slide images through hierarchical visual attention.
- **[MulGT: Multi-Task Graph-Transformer with Task-Aware Knowledge Injection and Domain Knowledge-Driven Pooling for Whole Slide Image Analysis](https://ojs.aaai.org/index.php/AAAI/article/view/25471)** — Combines task-specific knowledge and graph transformers for whole-slide analysis.
- **[RLogist: Fast Observation Strategy on Whole-Slide Images with Deep Reinforcement Learning](https://ojs.aaai.org/index.php/AAAI/article/view/25467)** — Learns efficient observation strategies for whole-slide analysis with reinforcement learning.
- **[Weakly-Supervised Semantic Segmentation for Histopathology Images Based on Dataset Synthesis and Feature Consistency Constraint](https://ojs.aaai.org/index.php/AAAI/article/view/25136)** — Uses synthetic data and feature consistency for weakly supervised histopathology segmentation.

#### 🤖 Foundation Models & Vision-Language

- **[MMTN: Multi-Modal Memory Transformer Network for Image-Report Consistent Medical Report Generation](https://ojs.aaai.org/index.php/AAAI/article/view/25100)** — Uses multimodal memory to align images and generated medical reports.

#### 📋 Clinical NLP, EHR & Healthcare

- **[A Composite Multi-Attention Framework for Intraoperative Hypotension Early Warning](https://ojs.aaai.org/index.php/AAAI/article/view/26681)** — Combines multiple attention mechanisms for early warning of intraoperative hypotension. *[AI for Social Impact]*
- **[A Fair Incentive Scheme for Community Health Workers](https://ojs.aaai.org/index.php/AAAI/article/view/26653)** — Allocates incentives for community health workers under fairness considerations. *[AI for Social Impact]*
- **[Causal Recurrent Variational Autoencoder for Medical Time Series Generation](https://ojs.aaai.org/index.php/AAAI/article/view/26031)** — Generates medical time series through a causal recurrent variational model.
- **[Cogito Ergo Summ: Abstractive Summarization of Biomedical Papers via Semantic Parsing Graphs and Consistency Rewards](https://ojs.aaai.org/index.php/AAAI/article/view/26503)** — Summarizes biomedical literature.
- **[Context-Aware Safe Medication Recommendations with Molecular Graph and DDI Graph Embedding](https://ojs.aaai.org/index.php/AAAI/article/view/25861)** — Combines contextual, molecular, and drug-interaction information for medication recommendation.
- **[Correct-by-Construction Reinforcement Learning of Cardiac Pacemakers from Duration Calculus Requirements](https://ojs.aaai.org/index.php/AAAI/article/view/26728)** — Uses formal requirements to constrain reinforcement learning of cardiac pacemaker behavior. *[Safe and Robust AI]*
- **[Detecting Anomalous Networks of Opioid Prescribers and Dispensers in Prescription Drug Data](https://ojs.aaai.org/index.php/AAAI/article/view/26692)** — Detects anomalous networks of opioid prescribers and dispensers. *[AI for Social Impact]*
- **[Detecting Sources of Healthcare Associated Infections](https://ojs.aaai.org/index.php/AAAI/article/view/25554)** — Identifies possible sources of healthcare-associated infections.
- **[EINNs: Epidemiologically-Informed Neural Networks](https://ojs.aaai.org/index.php/AAAI/article/view/26690)** — Integrates epidemiological information into neural forecasting models. *[AI for Social Impact]*
- **[Estimating Average Causal Effects from Patient Trajectories](https://ojs.aaai.org/index.php/AAAI/article/view/25921)** — Estimates causal effects using longitudinal patient trajectories.
- **[Estimating Treatment Effects from Irregular Time Series Observations with Hidden Confounders](https://ojs.aaai.org/index.php/AAAI/article/view/25844)** — Estimates treatment effects from irregular observations with hidden confounding.
- **[Forecasting with Sparse but Informative Variables: A Case Study in Predicting Blood Glucose](https://ojs.aaai.org/index.php/AAAI/article/view/26154)** — Forecasts blood glucose using sparse but informative predictors.
- **[GraphPrompt: Graph-Based Prompt Templates for Biomedical Synonym Prediction](https://ojs.aaai.org/index.php/AAAI/article/view/26256)** — Uses graph prompts for biomedical synonym prediction.
- **[Help Me Heal: A Reinforced Polite and Empathetic Mental Health and Legal Counseling Dialogue System for Crime Victims](https://ojs.aaai.org/index.php/AAAI/article/view/26685)** — Uses reinforcement learning to support empathetic counseling for crime victims. *[AI for Social Impact]*
- **[Heterogeneous Graph Learning for Multi-Modal Medical Data Analysis](https://ojs.aaai.org/index.php/AAAI/article/view/25643)** — Models heterogeneous multimodal medical data with graph learning.
- **[Human Mobility Modeling during the COVID-19 Pandemic via Deep Graph Diffusion Infomax](https://ojs.aaai.org/index.php/AAAI/article/view/26678)** — Models human mobility during the COVID-19 pandemic with graph diffusion representations. *[AI for Social Impact]*
- **[Improving Biomedical Entity Linking with Cross-Entity Interaction](https://ojs.aaai.org/index.php/AAAI/article/view/26624)** — Links biomedical entity mentions to structured concepts.
- **[Inferring Patient Zero on Temporal Networks via Graph Neural Networks](https://ojs.aaai.org/index.php/AAAI/article/view/26152)** — Infers epidemic patient-zero candidates from temporal networks.
- **[KerPrint: Local-Global Knowledge Graph Enhanced Diagnosis Prediction for Retrospective and Prospective Interpretations](https://ojs.aaai.org/index.php/AAAI/article/view/25667)** — Combines local and global medical knowledge graphs for diagnostic prediction and interpretation.
- **[Learning Motion-Robust Remote Photoplethysmography through Arbitrary Resolution Videos](https://ojs.aaai.org/index.php/AAAI/article/view/25217)** — Measures remote pulse signals robustly across motion and video resolutions.
- **[Med-EASi: Finely Annotated Dataset and Models for Controllable Simplification of Medical Texts](https://ojs.aaai.org/index.php/AAAI/article/view/26649)** — Provides fine-grained annotations for controlled simplification of medical language. *[AI for Social Impact]*
- **[MTDiag: An Effective Multi-Task Framework for Automatic Diagnosis](https://ojs.aaai.org/index.php/AAAI/article/view/26666)** — Models multiple diagnostic tasks jointly. *[AI for Social Impact]*
- **[“Nothing Abnormal”: Disambiguating Medical Reports via Contrastive Knowledge Infusion](https://ojs.aaai.org/index.php/AAAI/article/view/26665)** — Contrastive knowledge infusion disambiguates the ubiquitous "no abnormality" phrase in radiology reports, improving clinical NLP classification by pulling normal and pathological report representations apart. *[AI for Social Impact]*
- **[Scalable Decision-Focused Learning in Restless Multi-Armed Bandits with Application to Maternal and Child Health](https://ojs.aaai.org/index.php/AAAI/article/view/26431)** — Allocates maternal and child health interventions with restless bandits.
- **[ScatterFormer: Locally-Invariant Scattering Transformer for Patient-Independent Multispectral Detection of Epileptiform Discharges](https://ojs.aaai.org/index.php/AAAI/article/view/25086)** — Detects epileptiform discharges using patient-independent multispectral scattering representations.
- **[SCI: A Spectrum Concentrated Implicit Neural Compression for Biomedical Data](https://ojs.aaai.org/index.php/AAAI/article/view/25602)** — Compresses biomedical data using spectral implicit neural representations.
- **[Seq2Seq Surrogates of Epidemic Models to Facilitate Bayesian Inference](https://ojs.aaai.org/index.php/AAAI/article/view/26658)** — Uses sequence-to-sequence epidemic surrogates to support Bayesian inference. *[AI for Social Impact]*
- **[Toward Robust Diagnosis: A Contour Attention Preserving Adversarial Defense for COVID-19 Detection](https://ojs.aaai.org/index.php/AAAI/article/view/25395)** — Preserves contour attention under adversarial perturbations for COVID-19 diagnosis.

#### 🧠 Neuroimaging, EEG & Brain AI

- **[Electrophysiological Brain Source Imaging via Combinatorial Search with Provable Optimality](https://ojs.aaai.org/index.php/AAAI/article/view/26471)** — Reconstructs brain sources from electrophysiological signals.
- **[Extracting Semantic-Dynamic Features for Long-Term Stable Brain Computer Interface](https://ojs.aaai.org/index.php/AAAI/article/view/25738)** — Extracts stable semantic and dynamic features for long-term brain-computer interfaces.
- **[M3AE: Multimodal Representation Learning for Brain Tumor Segmentation with Missing Modalities](https://ojs.aaai.org/index.php/AAAI/article/view/25253)** — Learns multimodal representations for brain tumor segmentation with missing sequences.
- **[Robust One-Shot Segmentation of Brain Tissues via Image-Aligned Style Transformation](https://ojs.aaai.org/index.php/AAAI/article/view/25276)** — Segments brain tissues in medical images.
- **[Self-Supervised Learning for Anomalous Channel Detection in EEG Graphs: Application to Seizure Analysis](https://ojs.aaai.org/index.php/AAAI/article/view/25952)** — Detects anomalous EEG channels through self-supervised graph learning for seizure analysis.
- **[Towards Voice Reconstruction from EEG during Imagined Speech](https://ojs.aaai.org/index.php/AAAI/article/view/25745)** — Reconstructs voice information from imagined-speech EEG.

---

## KDD

### KDD 2025

#### 🔬 Medical Imaging & Segmentation

- **[Enhancing Bone Mineral Density Estimation from X-ray Images with Cross-Modal Knowledge Distillation](https://doi.org/10.1145/3711896.3737214)** — Estimates bone mineral density from X-rays using cross-modal knowledge distillation. *[Applied Data Science]*
- **[Evidential Prototype Learning for Semi-supervised Medical Image Segmentation](https://doi.org/10.1145/3711896.3736944)** — Uses evidential prototypes for semi-supervised medical segmentation.

#### 🧫 Computational Pathology & Microscopy

- **[Capillary Dataset: A Dataset of Nail-fold Capillaries Captured by Microscopy for Diabetes Detection](https://doi.org/10.1145/3711896.3737425)** — Provides nail-fold capillary microscopy data for diabetes detection research. *[Datasets and Benchmarks]*

#### 🤖 Foundation Models & Vision-Language

- **[FlanS – A Foundation Model for Free-Form Language-based Segmentation in Medical Images](https://doi.org/10.1145/3711896.3736963)** — Supports free-form language prompts for medical image segmentation.

#### 📋 Clinical NLP, EHR & Healthcare

- **[A Deep Subgrouping Framework for Precision Drug Repurposing via Emulating Clinical Trials on Real-world Patient Data](https://doi.org/10.1145/3690624.3709418)** — Uses emulated clinical trials and patient subgrouping to support precision drug repurposing. *[Applied Data Science]*
- **[A Diffusion-Based Method for Learning the Multi-Outcome Distribution of Medical Treatments](https://doi.org/10.1145/3711896.3736819)** — DIME models the joint interventional distribution of dependent, mixed-type treatment outcomes for uncertainty-aware treatment effect estimation.
- **[Advancing Confidence Calibration and Quantification in Medication Recommendation](https://doi.org/10.1145/3690624.3709232)** — Calibrates confidence and uncertainty in medication recommendation.
- **[AntAkso: Claims Management System for Health Insurance in Alipay](https://doi.org/10.1145/3690624.3709398)** — Presents an AI system for health-insurance claims management. *[Applied Data Science]*
- **[Asymmetrical Reciprocity-based Federated Learning for Resolving Disparities in Medical Diagnosis](https://doi.org/10.1145/3690624.3709235)** — Addresses diagnostic disparities through federated learning with asymmetric reciprocity.
- **[Automatic Radiotherapy Treatment Planning with Deep Functional Reinforcement Learning](https://doi.org/10.1145/3690624.3709430)** — Automates radiotherapy treatment planning with deep functional reinforcement learning. *[Applied Data Science]*
- **[CLaDMoP: Learning Transferrable Models from Successful Clinical Trials via LLMs](https://doi.org/10.1145/3711896.3736879)** — Transfers information from successful clinical trials through language-model pretraining and adaptation.
- **[CLEAR: Addressing Representation Contamination in Multimodal Healthcare Analytics](https://doi.org/10.1145/3690624.3709164)** — Addresses contamination between modality representations in healthcare models.
- **[CURE: A dataset for Clinical Understanding & Retrieval Evaluation](https://doi.org/10.1145/3711896.3737435)** — Benchmarks clinical understanding and information retrieval. *[Datasets and Benchmarks]*
- **[Diffmv: A Unified Diffusion Framework for Healthcare Predictions with Random Missing Views and View Laziness](https://doi.org/10.1145/3711896.3736908)** — Makes healthcare predictions despite randomly missing modalities and weakly used views.
- **[Learnable Prompt as Pseudo-Imputation: Rethinking the Necessity of Traditional EHR Data Imputation in Downstream Clinical Prediction](https://doi.org/10.1145/3690624.3709166)** — Uses learnable prompts as pseudo-imputation for EHR-based clinical prediction.
- **[MedDiTPro: A Prompt-Guided Diffusion Transformer for Multimodal Longitudinal Medical Data Synthesis](https://doi.org/10.1145/3711896.3737045)** — Synthesizes multimodal longitudinal medical data with prompt-guided diffusion transformers.
- **[MentalChat16K: A Benchmark Dataset for Conversational Mental Health Assistance](https://doi.org/10.1145/3711896.3737393)** — Provides conversational data for evaluating mental-health assistance. *[Datasets and Benchmarks]*
- **[MOPI-HFRS: A Multi-objective Personalized Health-aware Food Recommendation System with LLM-enhanced Interpretation](https://doi.org/10.1145/3690624.3709382)** — Recommends health-aware personalized food choices with language-model explanations. *[Applied Data Science]*
- **[SatHealth: A Multimodal Public Health Dataset with Satellite-based Environmental Factors](https://doi.org/10.1145/3711896.3737440)** — Links satellite-derived environmental factors with public-health outcomes in a multimodal dataset. *[Datasets and Benchmarks]*
- **[SepsisCalc: Integrating Clinical Calculators into Early Sepsis Prediction via Dynamic Temporal Graph Construction](https://doi.org/10.1145/3690624.3709402)** — Integrates clinical calculators into temporal graphs for early sepsis prediction. *[Applied Data Science]*
- **[Simulated Infectious Diseases Datasets with Controlled Data Bias](https://doi.org/10.1145/3711896.3737401)** — Provides simulated infectious-disease datasets with controlled sources of bias. *[Datasets and Benchmarks]*
- **[TarDiff: Target-Oriented Diffusion Guidance for Synthetic Electronic Health Record Time Series Generation](https://doi.org/10.1145/3711896.3737147)** — Generates synthetic EHR time series with target-oriented diffusion guidance to support downstream prediction under data scarcity and class imbalance.
- **[Test-Time Training with Diversified Local Aggregation Consistency for Mortality Prediction using Clinical Time Series](https://doi.org/10.1145/3711896.3737151)** — Adapts mortality prediction models to individual target patients while addressing temporal imbalance and cross-institution domain shifts.

#### 🧠 Neuroimaging, EEG & Brain AI

- **[Brain Effective Connectivity Estimation via Fourier Spatiotemporal Attention](https://doi.org/10.1145/3690624.3709226)** — Estimates effective brain connectivity with Fourier spatiotemporal attention.
- **[Neurophysiologically Realistic Environment for Comparing Adaptive Deep Brain Stimulation Algorithms in Parkinson’s Disease](https://doi.org/10.1145/3711896.3737397)** — Simulates neurophysiologically grounded environments for comparing adaptive deep-brain stimulation algorithms in Parkinson's disease. *[Datasets and Benchmarks]*

#### 🫀 Physiological Signals & Medical Time Series

- **[Characterizing the Risk of Atrial Fibrillation in Cardiac Patients with Exceptional Electrocardiogram Phenotypes](https://doi.org/10.1145/3711896.3737200)** — Characterizes atrial-fibrillation risk using exceptional ECG phenotypes. *[Applied Data Science]*
- **[ECGrecover: A Deep Learning Approach for Electrocardiogram Signal Completion](https://doi.org/10.1145/3690624.3709405)** — Completes missing ECG signal information with deep learning. *[Applied Data Science]*

---

### KDD 2024

#### 🔬 Medical Imaging & Segmentation

- **[Masked LoGoNet: Fast and Accurate 3D Image Analysis for Medical Domain](https://doi.org/10.1145/3637528.3672069)** — Uses masked global-local modeling for efficient 3D medical image analysis.

#### 📋 Clinical NLP, EHR & Healthcare

- **[Chromosomal Structural Abnormality Diagnosis by Homologous Similarity](https://doi.org/10.1145/3637528.3671642)** — Uses homologous similarity to diagnose structural chromosomal abnormalities in clinical imaging. *[Applied Data Science]*
- **[FlexCare: Leveraging Cross-Task Synergy for Flexible Multimodal Healthcare Prediction](https://doi.org/10.1145/3637528.3671974)** — Transfers information across clinical tasks for flexible multimodal healthcare prediction.
- **[NudgeRank: Digital Algorithmic Nudging for Personalized Health](https://doi.org/10.1145/3637528.3671562)** — Uses algorithmic nudges for personalized health. *[Applied Data Science]*
- **[Personalised Drug Identifier for Cancer Treatment with Transformers using Auxiliary Information](https://doi.org/10.1145/3637528.3671652)** — Uses auxiliary information and transformers for personalized cancer drug identification. *[Applied Data Science]*
- **[ProtoMix: Augmenting Health Status Representation Learning via Prototype-based Mixup](https://doi.org/10.1145/3637528.3671937)** — Augments health-status representations through prototype-based mixup.
- **[RareBench: Can LLMs Serve as Rare Diseases Specialists?](https://doi.org/10.1145/3637528.3671576)** — Evaluates language models on rare-disease diagnostic knowledge. *[Applied Data Science]*
- **[RJUA-MedDQA: A Multimodal Benchmark for Medical Document Question Answering and Clinical Reasoning](https://doi.org/10.1145/3637528.3671644)** — Benchmarks multimodal medical-document question answering and clinical reasoning. *[Applied Data Science]*
- **[SepsisLab: Early Sepsis Prediction with Uncertainty Quantification and Active Sensing](https://doi.org/10.1145/3637528.3671586)** — Combines uncertainty quantification and active sensing for early sepsis prediction. *[Applied Data Science]*
- **[Synthesizing Multimodal Electronic Health Records via Predictive Diffusion Models](https://doi.org/10.1145/3637528.3671836)** — Generates multimodal EHR data with predictive diffusion models.
- **[TACCO: Task-guided Co-clustering of Clinical Concepts and Patient Visits for Disease Subtyping based on EHR Data](https://doi.org/10.1145/3637528.3671594)** — Co-clusters clinical concepts and patient visits for EHR-based disease subtyping. *[Applied Data Science]*
- **[Towards Automatic Evaluation for LLMs’ Clinical Capabilities: Metric, Data, and Algorithm](https://doi.org/10.1145/3637528.3671575)** — Develops data, metrics, and algorithms for evaluating language models' clinical capabilities. *[Applied Data Science]*

#### 🧠 Neuroimaging, EEG & Brain AI

- **[EEG2Rep: Enhancing Self-supervised EEG Representation Through Informative Masked Inputs](https://doi.org/10.1145/3637528.3671600)** — Learns EEG representations through informative masking. *[Applied Data Science]*

#### 🫀 Physiological Signals & Medical Time Series

- **[Brant-X: A Unified Physiological Signal Alignment Framework](https://doi.org/10.1145/3637528.3671953)** — Aligns different physiological signals within a unified representation framework.
- **[Mutual Distillation Extracting Spatial-temporal Knowledge for Lightweight Multi-channel Sleep Stage Classification](https://doi.org/10.1145/3637528.3671981)** — Distills spatial and temporal information for lightweight multichannel sleep staging.

---

### KDD 2023

#### 📋 Clinical NLP, EHR & Healthcare

- **[A Look into Causal Effects under Entangled Treatment in Graphs: Investigating the Impact of Contact on MRSA Infection](https://doi.org/10.1145/3580305.3599763)** — Estimates effects of contact on MRSA infection under entangled graph treatments. *[Applied Data Science]*
- **[Assisting Clinical Decisions for Scarcely Available Treatment via Disentangled Latent Representation](https://doi.org/10.1145/3580305.3599774)** — Uses disentangled representations to support decisions about sparsely observed treatments. *[Applied Data Science]*
- **[Conditional Neural ODE Processes for Individual Disease Progression Forecasting: A Case Study on COVID-19](https://doi.org/10.1145/3580305.3599792)** — Forecasts individual disease progression with conditional neural ODE processes. *[Applied Data Science]*
- **[Deep Offline Reinforcement Learning for Real-World Treatment Optimization Applications](https://doi.org/10.1145/3580305.3599800)** — Applies offline deep reinforcement learning to real-world treatment optimization. *[Applied Data Science]*
- **[Doctor Specific Tag Recommendation for Online Medical Record Management](https://doi.org/10.1145/3580305.3599810)** — Recommends clinician-specific tags for managing medical records. *[Applied Data Science]*
- **[Expert Knowledge-Aware Image Difference Graph Representation Learning for Difference-Aware Medical Visual Question Answering](https://arxiv.org/abs/2307.11986)** — Knowledge graph encoding expert-defined difference relationships between paired medical images for difference-aware VQA on MIMIC-Diff-VQA benchmark. *[Applied Data Science]*
- **[FedPseudo: Privacy-Preserving Pseudo Value-Based Deep Learning Models for Federated Survival Analysis](https://doi.org/10.1145/3580305.3599348)** — Preserves privacy in federated survival analysis with pseudo values.
- **[Granger Causal Chain Discovery for Sepsis-Associated Derangements via Continuous-Time Hawkes Processes](https://doi.org/10.1145/3580305.3599369)** — Models causal chains of sepsis-related derangements with continuous-time Hawkes processes.
- **[MedLink: De-Identified Patient Health Record Linkage](https://doi.org/10.1145/3580305.3599427)** — Links de-identified patient health records across data sources.
- **[Self-supervised Classification of Clinical Multivariate Time Series using Time Series Dynamics](https://doi.org/10.1145/3580305.3599954)** — Uses temporal dynamics for self-supervised classification of clinical multivariate time series. *[Applied Data Science]*
- **[Towards Suicide Prevention from Bipolar Disorder with Temporal Symptom-Aware Multitask Learning](https://doi.org/10.1145/3580305.3599917)** — Models temporal symptoms for multitask suicide-risk analysis in bipolar disorder. *[Applied Data Science]*
- **[TWIN: Personalized Clinical Trial Digital Twin Generation](https://doi.org/10.1145/3580305.3599534)** — Generates personalized digital twins of clinical trials.
- **[Warpformer: A Multi-Scale Modeling Approach for Irregular Clinical Time Series](https://doi.org/10.1145/3580305.3599543)** — Models irregular clinical time series through multiscale temporal warping.
- **[Web-Based Long-Term Spine Treatment Outcome Forecasting](https://doi.org/10.1145/3580305.3599545)** — Forecasts long-term outcomes of spine treatments.

#### 🧠 Neuroimaging, EEG & Brain AI

- **[Interpretable Sparsification of Brain Graphs: Better Practices and Effective Designs for Graph Neural Networks](https://doi.org/10.1145/3580305.3599394)** — Studies interpretable sparsification of brain graphs for graph neural networks.
- **[MBrain: A Multi-Channel Self-Supervised Learning Framework for Brain Signals](https://doi.org/10.1145/3580305.3599426)** — Pretrains multichannel brain-signal representations through self-supervision.
- **[Multimodal Indoor Localisation in Parkinson’s Disease for Detecting Medication Use: Observational Pilot Study in a Free-Living Setting](https://doi.org/10.1145/3580305.3599872)** — Studies multimodal indoor localization for detecting medication use in Parkinson's disease. *[Applied Data Science]*
- **[One-shot Joint Extraction, Registration and Segmentation of Neuroimaging Data](https://doi.org/10.1145/3580305.3599452)** — Jointly extracts, registers, and segments neuroimaging data from a single example.

#### 🫀 Physiological Signals & Medical Time Series

- **[ECGGAN: A Framework for Effective and Interpretable Electrocardiogram Anomaly Detection](https://doi.org/10.1145/3580305.3599812)** — Detects ECG anomalies with an interpretable generative adversarial framework. *[Applied Data Science]*

---

## Proceedings indexing

Use the [proceedings indexer](docs/indexing.md) to enumerate complete conference catalogs, screen titles and available abstracts for medical AI topics, and compare the results with this list. It produces a review queue with matching evidence and a coverage report; candidate papers still require manual verification.

```sh
python -m pip install -r requirements-index.txt
python scripts/index_papers.py
```

See the generated [coverage report](reports/coverage.md) and [candidate queue](reports/candidates.md). The full local index retains unflagged papers so that screening rules can be expanded without repeating the crawl.

Reviewed inclusion and exclusion decisions are stored in the [curation ledger](data/curation.json). After reviewing new candidates, apply approved entries and regenerate the queue:

```sh
python scripts/apply_curation.py --check
python scripts/apply_curation.py
python scripts/index_papers.py --rescreen --offline
```

The applicator validates official titles, conference years, track metadata, and paper-specific links. It preserves the conference → year → topic layout and does not add papers based on screening scores alone. See the [metadata audit](docs/metadata-audit.md) for corrected and archived entries.

---

## Contributing

Contributions are very welcome!

- **Add a paper**: Open a PR with the paper entry in the appropriate conference section, using the format:  
  `**[Title](URL)** — One-sentence description. *Authors*`
- **Fix a broken link**: Open an issue or PR.
- **Suggest a new category**: Open an issue to discuss.
- **Verify metadata**: Check the title, conference, publication year, and summary against the official proceedings; prefer a paper-specific proceedings page or DOI over a general accepted-papers list.
- **Avoid duplicates**: Check for both the full title and model acronym before adding a paper, including papers with an earlier arXiv date.

**Scope**: Papers published at CS/AI conference proceedings (CVPR, NeurIPS, ICLR, ICML, ICCV, ECCV, ACL, EMNLP, NAACL, AAAI, KDD, etc.) in the years 2023–2025 on medical imaging, pathology and biomedical microscopy, clinical NLP and EHR, human neuroimaging and brain-computer interfaces, physiological signals, surgical AI, or healthcare. Datasets, benchmarks, and named special tracks are labeled. Workshops, doctoral/student abstracts, faculty highlights, co-located IAAI papers, and pure biology papers (drug discovery, protein folding, genomics) are outside the current scope.

---

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related rights to this work.
