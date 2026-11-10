---
paper_id: "000094"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706598/files/000094.pdf"
---

# MAIA: AN INPAINTING-BASED APPROACH FOR MUSIC ADVERSARIAL ATTACKS 

Yuxuan Liu, Peihong Zhang, Rui Sang, Zhixin Li, Shengchen Li Xi’an Jiaotong-Liverpool University {yuxuan.liu2204, peihong.zhang20, rui.sang22, zhixin.li22}@student.xjtlu.edu.cn shengchen.li@xjtlu.edu.cn 

## ABSTRACT 

Music adversarial attacks have garnered significant interest in the field of Music Information Retrieval (MIR). In this paper, we present Music Adversarial Inpainting Attack (MAIA), a novel adversarial attack framework that supports both white-box and black-box attack scenarios. MAIA begins with an importance analysis to identify critical audio segments, which are then targeted for modification. Utilizing generative inpainting models, these segments are reconstructed with guidance from the output of the attacked model, ensuring subtle and effective adversarial perturbations. We evaluate MAIA on multiple MIR tasks, demonstrating high attack success rates in both white-box and black-box settings while maintaining minimal perceptual distortion. Additionally, subjective listening tests confirm the high audio fidelity of the adversarial samples. Our findings highlight vulnerabilities in current MIR systems and emphasize the need for more robust and secure models. 

## 1. INTRODUCTION 

Music Information Retrieval (MIR) has evolved into a multifaceted research domain, underpinning various applications such as applications that range from genre classification [1] and instrument recognition [2] to cover song identification [3–5] and recommendation systems [6, 7]. As MIR algorithms become increasingly prevalent in both commercial products and academic research, their reliability and robustness have come under scrutiny [8, 9]. Although adversarial vulnerabilities have been extensively studied in speech recognition [10, 11] and image classification [12, 13], the music domain remains comparatively underexplored. 

Adversarial attacks in the Music Information Retrieval (MIR) context can be broadly categorized into noise-based and semantic-based approaches. Noise-based attacks, such 

Yuxuan Liu and Peihong Zhang contributed equally to this work. 

> © Y. Liu, P. Zhang, R. Sang, Z. Li, and S. Li. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: Y. Liu, P. Zhang, R. Sang, Z. Li, and S. Li, “MAIA: An Inpainting-Based Approach for Music Adversarial Attacks”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

as the Carlini–Wagner (C&W) attacks [12] introduces subtle audio distortions to mislead the model into incorrect outputs. Prinz et al. [8] extended this line of work by introducing end-to-end white-box adversarial attacks that operate directly on raw waveforms, demonstrating their effectiveness in degrading instrument classification accuracy and manipulating music recommendation systems while maintaining imperceptible perturbations. Saadatpanah et al. [9] highlighted the vulnerability of copyright detection systems to adversarial attacks, showing that small perturbations can evade robust fingerprinting systems like YouTube’s Content ID and AudioTag, raising concerns about the security of these widely used industrial tools. Additionally, Chen et al. [11] proposed the Devil’s Whisper method, focusing on leveraging psychoacoustic principles to create highly stealthy adversarial audio examples. 

Noise-based adversarial attacks rely on adding imperceptible perturbations to audio but often lack interpretability and fail to leverage the structure and semantics of music [14], limiting their use in scenarios requiring semantic alignment or context-sensitive manipulation. Duan et al. [15] introduced a perception-aware attack framework that reverse-engineers human perception using regression analysis, optimizing perturbations to minimize perceived deviations while maintaining attack effectiveness. This innovative integration of human perception provides a unique perspective, although its dependence on subjective evaluations could limit generalizability. Similarly, Yu et al. [16] developed SMACK, a method that perturbs prosodic features like pitch and rhythm to create semantically meaningful adversarial audio while preserving naturalness. Despite its effectiveness, the computational complexity of prosody optimization remains a challenge. Luo et al. [17] proposed a frequency-driven approach that confines perturbations to high-frequency components, ensuring imperceptibility and semantic coherence. However, its focus on high-frequency regions may limit applicability in scenarios where lowfrequency components are critical. 

Despite these advancements, existing approaches still face challenges in balancing attack effectiveness, musical coherence, and practical feasibility across different MIR tasks. In this paper, we propose a novel music adversarial inpainting attack (MAIA) framework that addresses these gaps. Our approach identifies crucial music segments through importance analysis and selectively reconstructs them via a generative inpainting model, ensuring subtle yet 

805 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

highly targeted adversarial perturbations. Unlike purely noise-based methods, MAIA’s local edits retain musical coherence while influencing classification in a white-box or black-box setting. Through comprehensive evaluations of MIR tasks such as music genre classification and cover song identification, we demonstrate that MAIA achieves state-of-the-art attack success with minimal perceptual artifacts. 

The contributions of this work are threefold: 

1. We propose a novel adversarial attack framework, MAIA, based on importance-driven inpainting. This framework reconstructs critical audio segments with adversarial perturbations, ensuring musical coherence while effectively misleading target models. 

2. We design a black-box importance analysis method that identifies influential music segments through a coarse-to-fine query-based approach, enabling effective adversarial attacks without requiring gradient access. 

3. We perform extensive objective and subjective evaluations to comprehensively benchmark MAIA attack success rate and perceptual quality across MIR tasks. 

## 2. MUSIC ADVERSARIAL INPAINTING ATTACK FRAMEWORK 

## 2.1 Importance Analysis 

A key objective of adversarial attacks in Music Information Retrieval (MIR) is to introduce minimal yet effective perturbations that are hard for both detection algorithms and human listeners to notice. In practical terms, modifying only the most influential time-frequency regions can reduce the extent of injected noise, thereby decreasing perceptual artifacts. Accordingly, we focus on segments that contribute most significantly to the prediction of the model, ensuring a high attack success rate while minimizing any audible changes [18]. 

proposed in the image domain, Grad-CAM can be adapted for our music adversarial attack tasks by: 

- Converting the raw waveform to a suitable timefrequency representation (e.g., Mel-spectrogram). 

- Selecting an appropriate convolutional layer—often the final or penultimate convolutional layer—where feature maps retain meaningful spatial (or timefrequency) structure. In our experiments, for an attacked MIR model M , we select the layer model.layers[-1].blocks[-1].norm1 as the target for analysis. The output of this layer represents the complete, stabilized feature representation from the model’s final block just before the classification head [23]. 

Grad-CAM Computation. Let ˆyc denote the model’s predicted score (logit) for class c. We denote by F<sup>l</sup> the feature map activations at layer l, with Fk<sup>lindicating the kth chan-</sup> nel. We compute Grad-CAM as follows: 

1. Gradient Extraction: Obtain the gradient of yˆc with respect to Fk<sup>l:</sup> 



<!-- Start of picture text -->
∂ y ˆc<br>αk c = Z 1 �x,y ∂Fk l (x, y) , (1)<br><!-- End of picture text -->

where (x, y) indexes the spatial/time-frequency positions and Z is a normalization factor (e.g., number of spatial locations). 

2. Weighted Aggregation: Multiply each feature map Fk<sup>lby its corresponding weight α</sup> k<sup>c, then sum over k</sup> to obtain the raw map: 



<!-- Start of picture text -->
Mc(x, y) = ReLU αk c F l k (x, y) . (2)<br>�� �<br>k<br><!-- End of picture text -->

3. Spatial Masking: Apply a ReLU to keep only positive contributions, generating Mc as the final GradCAM heatmap. Higher intensities in Mc(x, y) indicate greater relevance for predicting class c. 

## 2.1.1 White-Box Importance: Grad-CAM 

When full access to the target model parameters and architecture is available, we adopt a class activation map (CAM) [19]-based strategy to locate time-frequency regions that most heavily influence the classifier’s decision. Traditional CAM methods [19] often require replacing fully-connected layers with global pooling layers [20], thereby constraining the model architecture. However, Grad-CAM [21] generalizes CAM and does not require modifications to the classifier, making it more flexible for existing convolutional neural networks. 

Intuition and Setup. Unlike purely saliency-based approaches [22], which are typically optimized to reflect human visual attention, Grad-CAM specifically captures classifier-relevant regions by propagating class-specific gradient signals back through the network [21]. Originally 

4. Mapping to Time-Frequency Regions: Once Mc is computed, we map it back to the original spectrogram coordinates. We then normalize the heatmap to lie in [0, 1] or select the top p% of time-frequency bins to isolate the most critical regions. We marked these high-intensity areas as the candidate adversarial zone, which we will subsequently modify in our inpainting-based adversarial attack framework. 

## 2.1.2 Black-Box Importance: Coarse-to-Fine Analysis 

In scenarios where internal parameters of the target model M remain unknown, we cannot rely on gradient information to locate critical segments. Instead, we propose a coarse-to-fine black-box procedure that systematically queries the model to identify the most influential portions of the audio. Let x be the full music track, and let M (x) 

806 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

denote the model’s prediction (e.g., classification probability or logit score). We assume access to a loss function L�M (x), y�, where y is the true original label. Initial Partition. We first segment x into N coarse chunks, 



<!-- Start of picture text -->
S (0) = {C1 (0), C 2 (0), . . . , C N (0)}, (3)<br><!-- End of picture text -->

where each Ci<sup>(0)</sup> is a non-overlapping time interval (e.g., 0.5 second). For each chunk Ci<sup>(0)</sup> , we create a modified input �x−Ci(0) using a Zero-Masking procedure. To prevent spectral artifacts arising from abrupt signal changes at the chunk boundaries, we apply a Tukey window to the target segment. The window’s shape parameter was set to 0.1 to create a short, smooth taper at the segment’s edges, ensuring a continuous waveform after masking. This ensures a continuous waveform after masking. We then compute the importance score: 



<!-- Start of picture text -->
I�Ci (0) � = L � M (x�−Ci(0) ), y � − L � M (x), y � . (4)<br>duration � Ci (0) �<br><!-- End of picture text -->

as our candidate adversarial zones, concentrating future perturbations on these critical regions. 

Overall, our black-box importance analysis balances effectiveness and practicality, allowing us to identify precisely which audio segments have the greatest impact on the output of attacked model without requiring knowledge of its internal parameters or gradients. 

## 3. ADVERSARIAL INPAINTING 

After identifying the most influential segments for the target attacked model M , we proceed to adversarially inpaint the top-ranked segments. Our goal is to reconstruct these critical regions in such a way that the resulting track both degrades the prediction confidence of M and remains perceptually coherent to the human ear. In this section, we first introduce the concept of music inpainting, followed by details of two state-of-the-art inpainting models—GACELA [24]—which we leverage for adversarial inpainting. 

## 3.1 GACELA 

A higher value of I�Ci<sup>(0)</sup> � indicates that removing Ci<sup>(0)</sup> leads to a larger drop in model confidence for y, suggesting that Ci<sup>(0)</sup> is more critical to the classification. Ranking and Refinement. Next, we rank the chunks in S<sup>(0)</sup> by their importance measure I�Ci<sup>(0)</sup> � in descending order. Let Cmax<sup>(0)be the chunk with the highest score.We</sup> then refine this chunk by subdividing it into M finer subchunks: 



<!-- Start of picture text -->
Smax (1) = �Cmax (1) ,1 , C max (1) ,2 , . . . , C max (1) ,M �. (5)<br><!-- End of picture text -->

For each sub-chunk C<sup>(1)</sup> max,j<sup>,wecomputeanupdatedim-</sup> portance measure: 



<!-- Start of picture text -->
I�Cmax (1) ,j� = L � M (x�−Cmax(1) ,j ), y � − L � M (x), y � ,<br>duration � Cmax (1) ,j �<br>(6)<br><!-- End of picture text -->

where �x−Cmax(1) ,j<sup>is the audio track with only that sub-chunk</sup> silenced. We then replace Cmax<sup>(0)inoursegmentationwithitssub-</sup> chunks C<sup>(1)</sup> max,j<sup>, thus creating a refined set of segments:</sup> 



<!-- Start of picture text -->
S (1) = �S (0) \{Cmax (0) } � ∪ �Cmax (1) ,1 , . . . , C max (1) ,M �. (7)<br><!-- End of picture text -->

We can iterate this procedure by again choosing the segment with the largest updated importance and subdividing further, denoted S<sup>(2)</sup> , S<sup>(3)</sup> , and so on, until a desired level of granularity is reached or a query budget is exhausted. Final Selection. Upon completing T refinement rounds, we obtain a final set of segments 



<!-- Start of picture text -->
S (T ) = {C1 (T ) , C2 (T ) , . . . , CK (T )}, (8)<br><!-- End of picture text -->

where each Ci<sup>(T )</sup> has a corresponding importance measure I�Ci<sup>(T )</sup> �. We then select the top r segments, 



<!-- Start of picture text -->
�C1 (T ) , . . . , Cr (T ) � = Top�I�Ci (T ) �, r�, (9)<br><!-- End of picture text -->

GACELA (Generative Adversarial Context Encoder for Long Audio Inpainting) [24] is a conditional generative adversarial network (cGAN) designed specifically for reconstructing long gaps in audio signals, such as music. The architecture comprises a generator and five discriminators operating at multiple time and frequency scales. The generator, conditioned on the log-magnitude mel spectrogram of the surrounding audio context, employs convolutional encoder-decoder layers and integrates latent variables to model the multimodal nature of audio inpainting. The discriminators evaluate the plausibility of the generated gaps by considering the context and spectral coherence. 

## 3.2 Adversarial Inpainting with Model Guidance 

After identifying critical segments (Section 2.1), we employ a music inpainting model (e.g., GACELA) to reconstruct these areas while embedding adversarial perturbations guided by the target model M . We propose two variants of this adversarial inpainting strategy, tailored respectively for white-box and black-box settings. 

## 3.2.1 White-Box Scenario: Loss Design and Parameter Tuning 

In the white-box setting, we have access to the parameters and gradients of the target model M , allowing for adversarial optimization in conjunction with the inpainting model Gθ. Let x<sup>(</sup> inp<sup>k)denote the inpainted audio at iteration</sup> k, focusing only on the masked region m which we got from importance analysis. The objective function for adversarial inpainting is defined as: 



<!-- Start of picture text -->
L = λrec Lrec�x ( inp k), x �+λatt Lattack�M (x ( inp k)), y �, (10)<br><!-- End of picture text -->

where reconstruction Loss Lrec ensures that the inpainted audio maintains perceptual and contextual coherence with the original audio in the masked region. Specif- 

807 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

Al <mark>g</mark> orithm 1 White-Box Adversarial In <mark>p</mark> aintin <mark>g</mark> 

Require: Original audio x, mask m, Inpainting model Gθ, Classifier M (white-box), Iterations N , step size α, Weights λrec, λatt. 

- 1: Initialization: 

- 2: xinp ← x ⊙ (1 − m) + Gθ(x ⊙ (1 − m)) ⊙ m 

- 3: for k = 1 to N do 

- 4: Compute Loss: 5: L = λrec d(xinp, x) + λatt ℓ�M (xinp), y� 

- 6: Gradient Update on Mask: 7: g ←∇xinp L; xinp ← xinp − α sign(g ⊙ m) 8: Re-Inpaint: 9: xinp ← x ⊙ (1 − m) + Gθ( xinp ⊙ m , x ⊙ (1 − m)) ⊙ m 

- 10: end for 

- 11: return xinp 

ically, Lrec leverages the loss functions inherent to the inpainting model Gθ. Adversarial Loss Lattack introduces adversarial perturbations to deceive the classifier M . For untargeted attacks, we aim to reduce the confidence of the correct label y: 



<!-- Start of picture text -->
Lattack = ℓ�M (x ( inp k)), y �, (11)<br><!-- End of picture text -->

where ℓ(·) can be a cross-entropy loss. The objective drives the model prediction away from the correct label y, making the attack untargeted. 

The hyperparameters λrec and λatt control the trade-off between preserving audio quality and achieving high attack success rates. We perform a grid search over λrec ∈ {0.5, 1.0, 2.0} and λatt ∈{0.5, 1.0, 2.0}. The optimal values are determined based on attack success rate and perceptual metrics. 

The optimization is an iterative process. Each step consists of three main operations: a forward pass, a gradientbased update, and a re-inpainting stage. 

Forward Pass. First, we compute the reconstruction loss Lrec with the inpainting model and the attack loss Lattack with the target classifier M . 

Gradient Update. Next, the masked region of x<sup>(</sup> inp<sup>k)is</sup> updated by taking a step to minimize the total loss L. This adversarial update is performed using the sign of the gradient: 



<!-- Start of picture text -->
x ( inp k+1) ← x ( inp k) − α sign �∇xinp L ⊙ m�, (12)<br><!-- End of picture text -->

where α is the step size, and the element-wise product with the mask m confines the update to the target region. 

Re-Inpaint. Finally, to ensure the adversarial perturbation remains locally consistent and artifact-free, we reapply the inpainting generator Gθ to the modified region. This step effectively projects the perturbed content back towards a realistic data manifold: 



<!-- Start of picture text -->
xinp (k+1) ← x⊙(1−m)+Gθ�xinp (k+1) ⊙m, x⊙(1−m)�⊙m.<br>(13)<br><!-- End of picture text -->

This iterative process continues until either the maximum iteration count N is reached or the attack success 

rate satisfies a predefined threshold. The detailed process is shown in Algorithm 1. 

## 3.2.2 Black-Box Scenario: Importance-Guided Adversarial Inpainting 

In black-box settings, where the internal parameters and gradients of the target classifier M are inaccessible, we adopt a query-based adversarial inpainting approach guided by the importance analysis (Section 2.1). This method iteratively inpaints critical music segments from highest to lowest importance until the attack succeeds. The detailed process is as follows: 

1) Importance-Guided Segment Processing Based on the importance scores obtained from prior analysis, we sort the music segments in descending order of their significance to the target attacked model prediction. We then process each segment sequentially, prioritizing those with the highest impact. 

2) Adversarial Inpainting for Each Segment For each selected segment, we perform the following steps: 

1. Initialization Utilize the pretrained music inpainting model Gθ to perform standard inpainting on the masked important region m, generating the initial inpainted audio: 

x<sup>(0)</sup> inp<sup>= x⊙(1−m)+Gθ(x⊙(1−m))⊙m.(14)</sup> 

2. Iterative Query-Based Optimization Initialize a latent variable z<sup>(0)</sup> associated with the inpainting model. We employ the Covariance Matrix Adaptation Evolution Strategy (CMA-ES) [25] for gradientfree optimization to refine z and enhance attack efficacy: 



<!-- Start of picture text -->
z (k+1) = CMA-ES(z (k) , F(M, x ( inp k))), (15)<br><!-- End of picture text -->

where F(M, xinp) represents the classification feedback obtained by querying M with the current inpainted audio xinp<sup>(k).CMA-ESoptimizeszbyiter-</sup> atively sampling candidate latent codes, evaluating their performance based on the feedback, and updating the distribution parameters to favor more effective perturbations. 

3. Candidate Generation and Evaluation For each iteration, generate a set of candidate latent variables {z�} by sampling from the current CMA-ES distribution. Use the inpainting model to produce corresponding audio samples {x�inp}: 



<!-- Start of picture text -->
x�inp = Gθ(z, x�  ⊙ (1 − m)). (16)<br><!-- End of picture text -->

Query the target classifier M with each x�inp to obtain classification feedback (e.g., predicted label or confidence score). Evaluate the attack success based on whether M (x�inp)̸ = y. 

808 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

Table 1. Overall Attack Results on CoverHunter (CSI/SHS100K) and IDS-NMR (MGC/GTZAN) using GACELA. Higher ASR is better (untargeted), lower mAP/Accuracy is worse for the model. FAD and LSD measure perceptual distortion (lower is better). Listening Test is scored on a 5-point scale (higher is better). 

|Attack|C|SI (Cove|rHunter /|SHS100|K)||MGC (I|DS-NMR|/ GTZA|N)|
|---|---|---|---|---|---|---|---|---|---|---|
||ASR↑|mAP↓|FAD↓|LSD↓|MOS↑|ASR↑|Acc↓|FAD↓|LSD↓|MOS↑|
|White-Box Attacks|||||||||||
|PGD|82.1%|0.619|12.64|2.10|3.1|84.6%|0.551|15.32|2.20|3.2|
|C&W|88.5%|0.560|12.11|1.94|3.4|89.1%|0.512|14.90|2.21|3.3|
|MAIA-White Box|92.8%|0.488|11.25|1.58|4.0|93.5%|0.466|13.85|1.94|3.8|
|Black-Box Attacks|||||||||||
|NES|70.2%|0.682|13.93|2.27|2.8|65.7%|0.704|16.26|2.15|2.5|
|ZOO|74.9%|0.639|13.51|2.12|3.0|72.4%|0.654|15.90|2.05|3.0|
|MAIA-Black Box|80.1%|0.594|12.56|1.90|3.6|77.9%|0.601|14.68|1.85|3.3|



4. Selection and Evolution Based on the classification feedback, select the most promising candidates that maximize the adversarial loss Lattack and then updates the latent variable distribution parameters to guide future perturbations towards more effective adversarial examples. 

5. Re-Inpainting for Continuity After updating z, reapply the inpainting model to ensure the modified audio remains musically coherent: 

   - x<sup>(</sup> inp<sup>k+1)</sup> = x⊙(1−m)+Gθ(z<sup>(k+1)</sup> , x⊙(1−m))⊙m. (17) 

6. Termination Continue the iterative process until the classifier M is fooled (i.e., M (xinp<sup>(k))̸ = y) or a max-</sup> imum number of iterations is reached. 

## 4. EXPERIMENTS 

In this section, we evaluate our proposed Music Adversarial Inpainting Attack (MAIA) across two representative MIR tasks: Cover Song Identification (CSI) and Music Genre Classification (MGC). Our experiments assess both the white-box and black-box variants of MAIA, comparing them against common baselines by evaluating their performance using both subjective and objective metrics. 

## 4.1 Target Model and Datasets 

## 4.1.1 Cover Song Identification (CSI) 

We adopt the pre-trained CoverHunter model as our target for cover song identification, following the procedure in [26]. Experiments are conducted on the SHS100K dataset [27] test set. 

## 4.1.2 Music Genre Classification (MGC) 

We use the IDS-NMR network [1] on the GTZAN dataset [28] for genre classification. 

## 4.2 Evaluation Metrics 

We report four main classes of metrics: 

Attack Success Rate (ASR): The fraction of test samples successfully misclassified by the target model in an untargeted setting. 

System Performance Degradation: For CSI, we report the post-attack mAP of CoverHunter; for MGC, we report the post-attack accuracy of IDS-NMR. 

FAD (Fréchet Audio Distance based on MERT): We further incorporate pre-trained MERT-V0 [29] as a feature extractor to compute the Fréchet Audio Distance (FAD) [30] on adversarially perturbed tracks. By comparing the extracted feature distributions of original and attacked audio, we gain an additional objective measure of perceptual distance. 

LSD (Log-Spectral Distance) [31]: Evaluates the frame-wise spectral difference between original and perturbed signals. 

Perceptual Similarity (Subjective): A listening test with 100 participants to judge how easily adversarial perturbations can be detected. Each participant is asked to rate on a 5-point scale: 1 (highly noticeable) to 5 (no perceivable difference). 

## 4.3 Attack Baselines 

We compare MAIA against typical white-box and blackbox adversarial methods tailored to audio: 

PGD (Projected Gradient Descent) [32] [White-Box] C&W (Carlini & Wagner) [12] [White-Box] NES (Natural Evolution Strategies) [33] [Black-Box] ZOO (Zero Order Optimization Attack) [34] [BlackBox] 

## 4.4 Implementation Details 

In all experiments, we employed GACELA as the inpainting model to ensure consistent re-generation of targeted music segments; we set the maximum iteration to 10 for white-box methods and capped the query budget at 1000 for black-box methods. We tuned λrec and λatt by grid 

809 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

search, choosing values that balanced attack success rate (ASR) and perceptual fidelity. Table 1 presents the combined results for both CSI (CoverHunter on SHS100K) and MGC (IDS-NMR on GTZAN) under white-box and blackbox attacks. 

## 4.5 Results 

Table 1 demonstrates that our proposed MAIA-White Box consistently outperforms standard white-box attack baselines (PGD and C&W) across both MIR tasks. Specifically, MAIA-WB achieves the highest Attack Success Rate (93.5% for CSI and 94.5% for MGC), significantly reducing the mean Average Precision (mAP) from 0.845 to 0.488 in CoverHunter and classification accuracy from 0.828 to 0.466 in IDS-NMR. Additionally, MAIA-WB maintains superior perceptual quality with lower Fréchet Audio Distance (FAD) and Log-Spectral Distance (LSD) scores, and higher Listening Test ratings (4.0), indicating that the adversarial perturbations remain largely imperceptible to human listeners. In the black-box scenario, MAIABlack Box similarly outperforms NES and ZOO, achieving ASRs of 80.1% for CSI and 77.9% for MGC, with corresponding reductions in mAP and accuracy to 0.594 and 0.601, respectively. MAIA-BB also exhibits lower FAD and LSD scores compared to black-box baselines, and higher Listening Test ratings (3.6), suggesting that our importance-guided adversarial inpainting approach effectively balances attack potency with audio fidelity. Overall, MAIA variants consistently deliver higher attack success rates and greater performance degradation while preserving perceptual quality better than existing attack methods. 

## 5. CONCLUSIONS 

We have presented MAIA, a Music Adversarial Inpainting Attack framework that employs importance-driven segment selection and inpainting-based perturbations in both white-box and black-box settings. By focusing on the most influential regions, MAIA achieves higher attack success rates against CoverHunter (for cover song identification) and IDS-NMR (for genre classification), while preserving audio fidelity as measured by objective (FAD, LSD) and subjective (listening scores) metrics. We believe that our findings highlight both the potential severity and the subtlety of adversarial threats in MIR. By demonstrating a novel inpainting-based approach, we emphasize the need for comprehensive, perception-aware defenses to ensure robust and trustworthy music-related services. 

## 6. ACKNOWLEDGEMENTS 

This work was supported by the Jiangsu Science and Technology Programme (Major Special Programme, Grant No. BG2024027), the Suzhou Science and Technology Development Planning Programme (Gusu Innovation and Entrepreneurship Leading Talents Program, Grant No. ZXL2022472), and the XJTLU Research Development Fund (Grant No. RDF-22-02-046). 

## 7. REFERENCES 

- [1] Y.-N. Hung, C.-H. H. Yang, P.-Y. Chen, and A. Lerch, “Low-resource music genre classification with crossmodal neural model reprogramming,” in ICASSP 20232023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2023, pp. 1–5. 

- [2] A. Solanki and S. Pandey, “Music instrument recognition using deep convolutional neural networks,” International Journal of Information Technology, vol. 14, no. 3, pp. 1659–1668, 2022. 

- [3] X. Du, Z. Yu, B. Zhu, X. Chen, and Z. Ma, “Bytecover: Cover song identification via multi-loss training,” in ICASSP 2021-2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2021, pp. 551–555. 

- [4] X. Du, K. Chen, Z. Wang, B. Zhu, and Z. Ma, “Bytecover2: Towards dimensionality reduction of latent embedding for efficient cover song identification,” in ICASSP 2022-2022 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2022, pp. 616–620. 

- [5] X. Du, Z. Wang, X. Liang, H. Liang, B. Zhu, and Z. Ma, “Bytecover3: Accurate cover song identification on short queries,” in ICASSP 2023-2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2023, pp. 1–5. 

- [6] V. Moscato, A. Picariello, and G. Sperli, “An emotional recommender system for music,” IEEE Intelligent Systems, vol. 36, no. 5, pp. 57–68, 2020. 

- [7] D. Afchar, A. Melchiorre, M. Schedl, R. Hennequin, E. Epure, and M. Moussallam, “Explainability in music recommender systems,” AI Magazine, vol. 43, no. 2, pp. 190–208, 2022. 

- [8] K. Prinz, A. Flexer, and G. Widmer, “On end-to-end white-box adversarial attacks in music information retrieval.” Transactions of the International Society for Music Information Retrieval, vol. 4, no. 1, pp. 93–105, 2021. 

- [9] P. Saadatpanah, A. Shafahi, and T. Goldstein, “Adversarial attacks on copyright detection systems,” in International Conference on Machine Learning. PMLR, 2020, pp. 8307–8315. 

- [10] S. Wang, Z. Zhang, G. Zhu, X. Zhang, Y. Zhou, and J. Huang, “Query-efficient adversarial attack with low perturbation against end-to-end speech recognition systems,” IEEE Transactions on Information Forensics and Security, vol. 18, pp. 351–364, 2022. 

- [11] Y. Chen, X. Yuan, J. Zhang, Y. Zhao, S. Zhang, K. Chen, and X. Wang, “Devil’s whisper: A general approach for physical adversarial attacks against commercial black-box speech recognition devices,” in 29th 

810 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

   - USENIX Security Symposium (USENIX Security 20), 2020, pp. 2667–2684. 

- [12] N. Carlini and D. Wagner, “Towards evaluating the robustness of neural networks,” in 2017 IEEE Symposium on Security and Privacy (SP). IEEE, 2017, pp. 39–57. 

- [13] F. Croce and M. Hein, “Mind the box: l_1-apgd for sparse adversarial attacks on image classifiers,” in International Conference on Machine Learning. PMLR, 2021, pp. 2201–2211. 

- [14] C. Kereliuk, B. L. Sturm, and J. Larsen, “Deep learning and music adversaries,” IEEE Transactions on Multimedia, vol. 17, no. 11, pp. 2059–2071, 2015. 

- [15] R. Duan, Z. Qu, S. Zhao, L. Ding, Y. Liu, and Z. Lu, “Perception-aware attack: Creating adversarial music via reverse-engineering human perception,” in Proceedings of the 2022 ACM SIGSAC conference on computer and communications security, 2022, pp. 905– 919. 

- [16] Z. Rakamari´c and M. Emmi, “SMACK: Decoupling source language details from verifier implementations,” in Computer Aided Verification: 26th International Conference, CAV 2014, Held as Part of the Vienna Summer of Logic, VSL 2014, Vienna, Austria, July 18-22, 2014. Proceedings 26. Springer, 2014, pp. 106–113. 

- [17] C. Luo, Q. Lin, W. Xie, B. Wu, J. Xie, and L. Shen, “Frequency-driven imperceptible adversarial attack on semantic similarity,” in 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR). IEEE Computer Society, 2022, pp. 15 294–15 303. 

- [18] S. Ali, T. Abuhmed, S. El-Sappagh, K. Muhammad, J. M. Alonso-Moral, R. Confalonieri, R. Guidotti, J. Del Ser, N. Díaz-Rodríguez, and F. Herrera, “Explainable artificial intelligence (xai): What we know and what is left to attain trustworthy artificial intelligence,” Information Fusion, vol. 99, p. 101805, 2023. 

- [19] B. Zhou, A. Khosla, A. Lapedriza, A. Oliva, and A. Torralba, “Learning deep features for discriminative localization,” in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, 2016, pp. 2921–2929. 

- [20] M. Lin, “Network in network,” arXiv preprint arXiv:1312.4400, 2013. 

- [21] R. R. Selvaraju, M. Cogswell, A. Das, R. Vedantam, D. Parikh, and D. Batra, “Grad-cam: Visual explanations from deep networks via gradient-based localization,” in Proceedings of the IEEE International Conference on Computer Vision (ICCV), 2017, pp. 618–626. 

- [22] M. Oquab, L. Bottou, I. Laptev, and J. Sivic, “Is object localization for free?-weakly-supervised learning with convolutional neural networks,” in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2015, pp. 685–694. 

- [23] J. Gildenblat and contributors, “Pytorch library for cam methods,” https://github.com/jacobgil/ pytorch-grad-cam, 2021. 

- [24] A. Marafioti, P. Majdak, N. Holighaus, and N. Perraudin, “GACELA: A generative adversarial context encoder for long audio inpainting of music,” IEEE Journal of Selected Topics in Signal Processing, vol. 15, no. 1, pp. 120–131, 2020. 

- [25] K. Varelas, A. Auger, D. Brockhoff, N. Hansen, O. A. ElHara, Y. Semet, R. Kassab, and F. Barbaresco, “A comparative study of large-scale variants of cma-es,” in Parallel Problem Solving from Nature–PPSN XV: 15th International Conference, Coimbra, Portugal, September 8–12, 2018, Proceedings, Part I 15. Springer, 2018, pp. 3–15. 

- [26] F. Liu, D. Tuo, Y. Xu, and X. Han, “Coverhunter: Cover song identification with refined attention and alignments,” in 2023 IEEE International Conference on Multimedia and Expo (ICME). IEEE, 2023, pp. 1080–1085. 

- [27] X. Xu, X. Chen, and D. Yang, “Key-invariant convolutional neural network toward efficient cover song identification,” in 2018 IEEE International Conference on Multimedia and Expo (ICME). IEEE, 2018, pp. 1–6. 

- [28] B. L. Sturm, “The GTZAN Dataset: Its contents, its faults, their effects on evaluation, and its future use,” arXiv preprint arXiv:1306.1461, 2013. 

- [29] Y. Li, R. Yuan, G. Zhang, Y. Ma, X. Chen, H. Yin, C. Xiao, C. Lin, A. Ragni, E. Benetos, N. Gyenge, R. Dannenberg, R. Liu, W. Chen, G. Xia, Y. Shi, W. Huang, Z. Wang, Y. Guo, and J. Fu, “MERT: Acoustic music understanding model with large-scale self-supervised training,” in International Conference on Learning Representations (ICLR), 2024. 

- [30] K. Kilgour, M. Zuluaga, D. Roblek, and M. Sharifi, “Fréchet Audio Distance: A reference-free metric for evaluating music enhancement algorithms,” in Proceedings of Interspeech, 2019. 

- [31] A. Gray and J. Markel, “Distance measures for speech processing,” IEEE Transactions on Acoustics, Speech, and Signal Processing, vol. 24, no. 5, pp. 380–391, 1976. 

- [32] Y. Deng and L. J. Karam, “Universal adversarial attack via enhanced projected gradient descent,” in 2020 IEEE International Conference on Image Processing (ICIP). IEEE, 2020, pp. 1241–1245. 

- [33] D. Wierstra, T. Schaul, T. Glasmachers, Y. Sun, J. Peters, and J. Schmidhuber, “Natural evolution strategies,” The Journal of Machine Learning Research, vol. 15, no. 1, pp. 949–980, 2014. 

811 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [34] P.-Y. Chen, H. Zhang, Y. Sharma, J. Yi, and C.-J. Hsieh, “Zoo: Zeroth order optimization based blackbox attacks to deep neural networks without training substitute models,” in Proceedings of the 10th ACM workshop on artificial intelligence and security, 2017, pp. 15–26. 

812 

