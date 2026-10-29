# Medical AI: problem-discovery reading guide

Studies of where existing algorithms, training practices, or evaluation assumptions fail in medical AI, sometimes followed by a corrective method. Here, **science** means methodological discovery, rather than discovery of a biological mechanism. A new architecture or an improved benchmark score alone does not meet this definition.

This selected guide contains **21 papers**. 15 have checks of selected full-text sections; the remainder are abstract-level recommendations. These are reading notes, not independent replications or a complete census.

Science, methods, and benchmarks can overlap. Contribution tags are editorial judgments. A benchmark is included when it supports a specific diagnosis of an existing practice; position papers and method-heavy hybrids are separated below. Evidence and limitations are recorded for each entry. Publication years and tracks follow official proceedings.

[Back to the awesome list](../../README.md) · [Machine-readable review ledger](../../data/science_review.json) · [Candidate queue](candidates.csv) · [Retrieval provenance](retrieval-summary.json)

## How to use this guide

Read the question and finding first, then check the evidence and scope before generalizing. ‘Selected full-text sections’ means the cited passages were inspected, not that every experiment or supplement was audited. ‘Abstract checked’ requires deeper reading before relying on detailed mechanisms. Main-list membership is noted separately from inclusion in this guide.

## Data, representation, and transfer assumptions

### ICLR 2024 — The Effect of Intrinsic Dataset Properties on Generalization: Unraveling Learning Differences Between Natural and Medical Images

[Official paper](https://proceedings.iclr.cc/paper_files/paper/2024/hash/5ef6b140c8b6cc2904854e30c6db78eb-Abstract-Conference.html) · main · science, theory + experiments · in main list.

**Question:** Why can natural-image and medical-image generalization behave differently?

**Finding:** Intrinsic dimension and label sharpness help explain the different learning behavior of the tested natural and medical image datasets.

**Evidence / intervention:** Theory and comparisons across six models and eleven datasets examine dataset properties rather than introducing an architecture alone.

**Scope:** A partial explanation for these datasets, not a theorem covering all medical modalities or all transfer failures.

**Review:** abstract checked; Official abstract.

### ICML 2024 — Robustness of Deep Learning for Accelerated MRI: Benefits of Diverse Training Data

[Official paper](https://proceedings.mlr.press/v235/lin24h.html) · main · science, data-design study · in main list.

**Question:** Does specializing MRI reconstruction training to one acquisition distribution improve robustness?

**Finding:** Diverse training distributions improve effective robustness to tested shifts; joint training can match specialized models on their own distributions.

**Evidence / intervention:** Comparisons include U-net, ViT, and VarNet; joint-data experiments include a smaller joint-set control, and OOD comparisons condition on in-distribution performance.

**Scope:** Accelerated MRI reconstruction, measured mainly by reconstruction quality. This does not establish diagnostic safety or that every data mixture helps.

**Review:** selected full-text sections; Sections 3–4, PDF pp. 5–7 (joint-set control and effective-robustness analysis). [Reviewed PDF](https://raw.githubusercontent.com/mlresearch/v235/main/assets/lin24h/lin24h.pdf).

### ICML 2025 — Do We Really Need Message Passing in Brain Network Modeling?

[Official paper](https://proceedings.mlr.press/v267/yang25r.html) · main · science, method · in main list.

**Question:** Is standard message passing well matched to correlation-based brain graphs?

**Finding:** When topology and node features reuse the constructed connectivity information, the tested GNN and Transformer operators may add little; a simple classifier is a strong diagnostic baseline.

**Evidence / intervention:** Graph-construction analysis and ABIDE/ADNI comparisons motivate a quadratic alternative, BQN; the paper also analyzes its community-detection behavior.

**Scope:** The finding depends on the Pearson-correlation construction and chosen node features. It does not show all message passing is unnecessary for brain data.

**Review:** selected full-text sections; Sections 4.1–4.3 and 5.1, PDF pp. 4–5. [Reviewed PDF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/yang25r/yang25r.pdf).

### NeurIPS 2025 — From Pretraining to Pathology: How Noise Leads to Catastrophic Inheritance in Medical Models

[Official paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/854ba5f89c3b048265a5e00231ea5477-Abstract-Conference.html) · main · science, controlled perturbation + method · in main list.

**Question:** Can pretraining noise leave harmful effects after medical fine-tuning?

**Finding:** Controlled pretraining corruption produces downstream medical OOD degradation; higher-order feature statistics provide an empirical account of the inherited effect.

**Evidence / intervention:** Varying label corruption during pretraining, downstream medical comparisons, and regularization interventions test the proposed explanation.

**Scope:** The tested corruption regimes and datasets bound the claim. The feature-statistic account is not a universal causal proof about all noisy pretraining.

**Review:** selected full-text sections; Introduction and Sections 2.1–2.3, including the controlled corruption setup. [Reviewed PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/854ba5f89c3b048265a5e00231ea5477-Paper-Conference.pdf).

### NeurIPS 2025 — Is Limited Participant Diversity Impeding EEG-based Machine Learning?

[Official paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/aa5642fb7d78a1bca9ceba3d8bd564f4-Abstract-Conference.html) · main · science, data-scaling study · in main list.

**Question:** Can more EEG segments from the same people substitute for more participants?

**Finding:** Participant diversity limits scaling on some tasks, but the trade-off differs across datasets: additional segments can compensate substantially in the tested sleep-staging setting.

**Evidence / intervention:** Participant/segment budget comparisons across tasks and models, followed by augmentation and self-supervised-learning investigations.

**Scope:** Results differ between TUAB/CAUEEG and PhysioNet. Do not simplify this to “more segments never help” or a universal EEG scaling law.

**Review:** selected full-text sections; Sections 3.4–3.5 and 4.1–4.3 (especially the task-dependent segment trade-off). [Reviewed PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/aa5642fb7d78a1bca9ceba3d8bd564f4-Paper-Conference.pdf).

### ICML 2023 — Accounting For Informative Sampling When Learning to Forecast Treatment Outcomes Over Time

[Official paper](https://proceedings.mlr.press/v202/vanderschueren23a.html) · main · science, theory + method · in main list.

**Question:** What changes when patient observation frequency depends on clinical history?

**Finding:** Informative observation timing induces a mismatch between the observed training objective and the desired outcome-forecasting objective.

**Evidence / intervention:** A formal sampling model yields inverse-intensity weighting; a continuous-time forecasting method illustrates the correction.

**Scope:** Identification relies on sampling-at-random and causal assumptions, including treatment unconfoundedness. This is not clinical validation of counterfactual treatment effects.

**Review:** selected full-text sections; Sections 2–3 (sampling and identification assumptions) and 4.1 (weighting). [Reviewed PDF](https://proceedings.mlr.press/v202/vanderschueren23a/vanderschueren23a.pdf).

### ICLR 2025 — Context Clues: Evaluating Long Context Models for Clinical Prediction Tasks on EHR Data

[Official paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/2a246ec4437808525a088abae744c2d3-Abstract-Conference.html) · main · science, evaluation + model study · in main list.

**Question:** Which properties of clinical event sequences challenge long-context models?

**Finding:** Repetition, irregular event timing, and later timeline complexity expose differences from natural-language sequence modeling; tested longer-context models are more resilient on downstream tasks.

**Evidence / intervention:** EHR-OMOP sequence analysis and EHRSHOT performance stratification examine these factors alongside context-length comparisons.

**Scope:** Stratified associations do not by themselves prove causation. Findings concern the tested event-based EHR models and tasks, not every clinical text model.

**Review:** selected full-text sections; Sections 4.2–4.4 (repetition, irregular timing, and timeline position). [Reviewed PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/2a246ec4437808525a088abae744c2d3-Paper-Conference.pdf).

## Evaluation validity, shortcuts, and clinical utility

### NeurIPS 2024 — BrainBits: How Much of the Brain are Generative Reconstruction Methods Using?

[Official paper](https://proceedings.neurips.cc/paper_files/paper/2024/hash/61c00c07e6d27285e4b952e96cc65666-Abstract-Conference.html) · main · science, diagnostic benchmark · in main list.

**Question:** Does realistic brain-to-image reconstruction mean the model recovered more neural information?

**Finding:** Visual quality can reflect generative priors rather than information supplied by the brain measurements.

**Evidence / intervention:** Information bottlenecks probe how much neural input reconstruction systems actually use.

**Scope:** This diagnoses the tested generative reconstruction systems; it does not show neural input is irrelevant to every brain-decoding approach.

**Review:** abstract checked; Official abstract.

### EMNLP 2025 — Rethinking Cross-Subject Data Splitting for Brain-to-Text Decoding

[Official paper](https://aclanthology.org/2025.emnlp-main.289/) · main · science, evaluation protocol · in main list.

**Question:** Can a cross-subject split still leak information in brain-to-text evaluation?

**Finding:** Subject separation alone need not prevent leakage through other shared structure in the evaluated datasets.

**Evidence / intervention:** The paper analyzes splitting practices and re-evaluates decoding under revised criteria.

**Scope:** The scope is the analyzed datasets and split designs; do not infer every brain-to-text result leaks.

**Review:** abstract checked; Official abstract.

### AAAI 2025 — Every Component Counts: Rethinking the Measure of Success for Medical Semantic Segmentation in Multi-Instance Segmentation Tasks

[Official paper](https://ojs.aaai.org/index.php/AAAI/article/view/32408) · AAAI Technical Track on Computer Vision III · science, measurement · in main list.

**Question:** Do aggregate segmentation metrics reflect success on every lesion instance?

**Finding:** Large components can dominate aggregate scores and obscure failures on smaller components in multi-instance medical segmentation.

**Evidence / intervention:** Component-level analysis motivates an evaluation protocol that gives individual instances explicit attention.

**Scope:** The concern is multi-instance objectives and component weighting, not evidence that overlap metrics are useless for every segmentation task.

**Review:** abstract checked; Official abstract.

### ACL 2025 — Pattern Recognition or Medical Knowledge? The Problem with Multiple-Choice Questions in Medicine

[Official paper](https://aclanthology.org/2025.acl-long.266/) · long · science, benchmark + ablations · in main list.

**Question:** How much medical MCQ performance can come from answer-format patterns?

**Finding:** Models can answer questions about fictional medical content surprisingly well; choice and answer-length cues can support performance without the presumed medical knowledge.

**Evidence / intervention:** Synthetic-organ textbooks and bilingual MCQs, plus answer-only, reasoning, and length ablations, probe alternative explanations.

**Scope:** This is a controlled synthetic-MCQ stress test. It does not establish that models lack medical knowledge; some ablations use a narrower set of models.

**Review:** selected full-text sections; Section 3.3 and associated answer-choice/length analyses. [Reviewed PDF](https://aclanthology.org/2025.acl-long.266.pdf).

### ICLR 2025 — MediConfusion: Can you trust your AI radiologist? Probing the reliability of multimodal medical foundation models

[Official paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/b37c2e26b75ee02fcabd65a2a0367136-Abstract-Conference.html) · main · science, stress benchmark · in main list.

**Question:** Can medical multimodal models distinguish images requiring opposite answers to the same question?

**Finding:** Deliberately selected confusing image pairs expose failures hidden by easier conventional medical VQA evaluations.

**Evidence / intervention:** ROCO pairs are selected using high BiomedCLIP similarity and lower DINOv2 similarity; 352 questions are evaluated with individual and paired-set accuracy.

**Scope:** This is adversarially curated, not a prevalence estimate for routine clinical images. Paired-set accuracy and individual accuracy have different random baselines.

**Review:** selected full-text sections; Sections 2.1–2.3 (pair selection and individual versus set metrics). [Reviewed PDF](https://proceedings.iclr.cc/paper_files/paper/2025/file/b37c2e26b75ee02fcabd65a2a0367136-Paper-Conference.pdf).

### EMNLP 2025 — ReEvalMed: Rethinking Medical Report Evaluation by Aligning Metrics with Real-World Clinical Judgment

[Official paper](https://aclanthology.org/2025.emnlp-main.598/) · main · science, measurement benchmark · in main list.

**Question:** Do report metrics distinguish clinically meaningful changes from harmless rewrites?

**Finding:** Controlled rewrites expose mismatches between clinical significance and the behavior of established report-evaluation metrics.

**Evidence / intervention:** Expert-validated report pairs test discrimination and robustness to clinically significant versus insignificant changes.

**Scope:** Constructed report perturbations and the evaluated clinical-report setting limit generalization; no metric is established as valid for all clinical language.

**Review:** selected full-text sections; Sections 4.2.1–4.2.2 (400 expert-validated original/rewritten report pairs). [Reviewed PDF](https://aclanthology.org/2025.emnlp-main.598.pdf).

### ACL 2023 — Automated Metrics for Medical Multi-Document Summarization Disagree with Human Evaluations

[Official paper](https://aclanthology.org/2023.acl-long.549/) · long · science, measurement · in main list.

**Question:** Do automatic medical summarization metrics rank systems as humans do?

**Finding:** The evaluated automatic metrics can disagree with human judgments; some system rankings are negatively correlated.

**Evidence / intervention:** Comparing automatic scores against human evaluation tests whether common optimization targets measure the intended summarization quality.

**Scope:** Medical multi-document summarization and the assessed metrics/systems bound the result. Do not claim every automatic metric is universally anticorrelated with humans.

**Review:** abstract checked; Official abstract.

### EMNLP 2025 — Not What the Doctor Ordered: Surveying LLM-based De-identification and Quantifying Clinical Information Loss

[Official paper](https://aclanthology.org/2025.emnlp-main.1637/) · main · science, survey + measurement · in main list.

**Question:** Do strong de-identification scores guarantee preservation of clinical information?

**Finding:** High token-level scores can coexist with over-redaction and clinically relevant changes; standard scores and simple retention proxies miss important errors.

**Evidence / intervention:** Survey, multiple de-identification pipelines, manual clinical-change annotations, and a clinical-information-retention evaluation method.

**Scope:** Manual change rates use selected false-positive cases, not all notes. Results depend on AHS/MIMIC-III, annotation schemas, and the evaluated pipelines.

**Review:** selected full-text sections; Sections 5–7, especially Tables 2–3 and Section 7.2. [Reviewed PDF](https://aclanthology.org/2025.emnlp-main.1637.pdf).

### ACL 2025 — Spurious Correlations and Beyond: Understanding and Mitigating Shortcut Learning in SDOH Extraction with Large Language Models

[Official paper](https://aclanthology.org/2025.acl-short.86/) · short · science, narrow case study + intervention · indexed; not yet in main list.

**Question:** Can unrelated substance mentions trigger unsupported drug-use extraction?

**Finding:** Alcohol and smoking mentions are associated with false drug-status predictions; trigger-removal experiments support a shortcut explanation in this setting.

**Evidence / intervention:** Drug-status extraction tests vary triggers, prompting, fine-tuning, and demographic strata; evidence-focused prompts are explored as mitigation.

**Scope:** ACL short paper; a focused MIMIC-SHAC case study. The suggested origin in pretraining is a hypothesis, not an established mechanism.

**Review:** selected full-text sections; Evaluation framework and Sections 4–6, including trigger removal and gender-stratified results. [Reviewed PDF](https://aclanthology.org/2025.acl-short.86.pdf).

### NeurIPS 2025 — The Boundaries of Fair AI in Medical Image Prognosis: A Causal Perspective

[Official paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/c1715562b2227580b6c6db2050d7f6d2-Abstract-Conference.html) · main · science, benchmark + causal analysis · in main list.

**Question:** Do existing fairness methods transfer reliably to image-based prognosis?

**Finding:** Time-to-event models exhibit group performance gaps; the benchmark finds limits to existing mitigation strategies and examines their sensitivity to distribution shift.

**Evidence / intervention:** FairTTE covers multiple imaging modalities, prognosis outcomes, sensitive attributes, and fairness measures; model-selection and group-gap analyses make the audit explicit.

**Scope:** Fairness depends on the metric, dataset, and outcome. This is not a universal impossibility theorem for fair prognosis; shift mechanisms need separate scrutiny.

**Review:** selected full-text sections; Abstract and experimental setup/results in PDF p. 7; detailed shift claims remain abstract-level. [Reviewed PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/c1715562b2227580b6c6db2050d7f6d2-Paper-Conference.pdf).

## Problem discovery with a substantial method contribution

### CVPR 2025 — Revisiting MAE Pre-training for 3D Medical Image Segmentation

[Official paper](https://openaccess.thecvf.com/content/CVPR2025/html/Wald_Revisiting_MAE_Pre-training_for_3D_Medical_Image_Segmentation_CVPR_2025_paper.html) · main · science/method hybrid, systematic comparison · in main list.

**Question:** Why have MAE pretraining results been inconsistent for 3D medical segmentation?

**Finding:** Data, architecture, and evaluation choices matter; a carefully configured pipeline changes conclusions about the value of MAE pretraining.

**Evidence / intervention:** The study combines systematic evaluation with an optimized pretraining and segmentation recipe.

**Scope:** Substantial method contribution, with a brain-MRI focus. Treat as a hybrid, not pure evidence that MAE universally fails or succeeds in medical imaging.

**Review:** abstract checked; Official abstract.

### NeurIPS 2025 — Revisiting End-to-End Learning with Slide-level Supervision in Computational Pathology

[Official paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/eae33167166b44df7c929f70984c0c0b-Abstract-Conference.html) · main · science/method hybrid, optimization analysis · in main list.

**Question:** Why can sparse-attention MIL impair end-to-end pathology encoder adaptation?

**Finding:** Sparse attention can over-focus on redundant patches or miss discriminative instances during joint optimization, despite working well with strong frozen features.

**Evidence / intervention:** The paper analyzes this training risk and introduces ABMILX with local/global attention and an end-to-end sampling pipeline.

**Scope:** Problem analysis is intertwined with a substantial architecture/training proposal; the finding is not a rejection of all MIL or sparse attention.

**Review:** selected full-text sections; Introduction, Section 3.1 and Section 3.2 (optimization risks and ABMILX). [Reviewed PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/eae33167166b44df7c929f70984c0c0b-Paper-Conference.pdf).

## Position papers with supporting empirical studies

### ICML 2024 — Position: Reinforcement Learning in Dynamic Treatment Regimes Needs Critical Reexamination

[Official paper](https://proceedings.mlr.press/v235/luo24f.html) · position paper (combined proceedings volume) · position, empirical evaluation audit · in main list.

**Question:** How stable are offline RL conclusions for dynamic treatment regimes?

**Finding:** Algorithm rankings change with reward, MDP, and off-policy evaluation choices; naive policies can score well under some estimators.

**Evidence / intervention:** The authors report over 17,000 evaluations on a sepsis dataset and argue for more reliable evaluation practice.

**Scope:** This is a position paper with empirical support. Favorable estimated returns do not show random treatment is clinically better.

**Review:** selected full-text sections; Abstract and main-results discussion of naive baselines and evaluation sensitivity. [Reviewed PDF](https://raw.githubusercontent.com/mlresearch/v235/main/assets/luo24f/luo24f.pdf).

### ICML 2025 — Position: Medical Large Language Model Benchmarks Should Prioritize Construct Validity

[Official paper](https://proceedings.mlr.press/v267/alaa25a.html) · position paper (combined proceedings volume) · position, construct-validity audit · in main list.

**Question:** Does a medical benchmark score measure the clinical capability it claims to measure?

**Finding:** Proof-of-concept studies find gaps between common medical benchmark performance and the intended clinical constructs.

**Evidence / intervention:** Construct-validity analysis includes matching MedQA items to clinical encounters and testing criterion validity.

**Scope:** A position paper with selected empirical demonstrations, not comprehensive validation of every medical benchmark. Clinical proxy tasks and scoring choices matter.

**Review:** selected full-text sections; Introduction and Section 4.1 (criterion validity of MedQA). [Reviewed PDF](https://raw.githubusercontent.com/mlresearch/v267/main/assets/alaa25a/alaa25a.pdf).

## Reproduce and extend

Render these reviewed notes without downloading the proceedings:

```sh
python scripts/find_science_papers.py --render-only
```

After rebuilding the local proceedings index using the indexing instructions in the main README, rerun candidate retrieval:

```sh
python scripts/find_science_papers.py
```

Retrieval uses title/abstract cues plus the existing medical-scope rules and curated identities. Each output retains conference, publication year, and track. Reviewed ledger entries are retained even if they score poorly. Scores only prioritize reading; an unreviewed candidate is **not** an accepted science classification. False positives, missing abstracts, and papers without the cue vocabulary remain possible. This search does not establish exhaustive recall.

To extend the guide, read the official source and add the question, finding, evidence location, and limits to `data/science_review.json`. Record whether only the abstract or selected full-text passages were inspected. PDF hashes identify the reviewed version; raw PDFs and extracted text stay in the ignored cache. The ledger's main-list membership is a snapshot of its review date.

This purposive selection cannot estimate the fraction of science versus engineering papers, changes in that fraction by year, or acceptance probabilities. Those require a systematically labeled denominator; acceptance analysis also needs rejected submissions.

Reviewed: 2026-10-29. Generated by `scripts/find_science_papers.py`; edit the ledger rather than this file.
