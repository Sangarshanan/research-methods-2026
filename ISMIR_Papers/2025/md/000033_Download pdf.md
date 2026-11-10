---
paper_id: "000033"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706393/files/000033.pdf"
---

# LiLAC: A LIGHTWEIGHT LATENT CONTROLNET FOR MUSICAL AUDIO GENERATION 

Tom Baker<sup>1,2∗</sup> 

1University Of Manchester 

```
tom.baker@manchester.ac.uk
```

Javier Nistal<sup>2</sup> 2Sony CSL - Paris 

```
javier.nistal@sony.com
```

## ABSTRACT 

Text-to-audio diffusion models produce high-quality and diverse music but often lack the fine-grained, time-varying controls essential for music production. ControlNet enables attaching external controls to a pre-trained generative model by cloning and fine-tuning its encoder on new conditionings. However, this approach incurs a large memory footprint and restricts users to a fixed set of controls. We propose a lightweight, modular architecture that considerably reduces parameter count while matching ControlNet in audio quality and condition adherence. Our method offers greater flexibility and significantly lower memory usage, enabling more efficient training and deployment of independent controls. We conduct extensive objective and subjective evaluations and provide numerous audio examples on the accompanying website.<sup>1</sup> 

## 1. INTRODUCTION 

With the rise of generative models, new challenges have emerged in the field of human-computer interaction, especially in how users interact with these systems [1]. This issue is particularly significant in domains of artistic expression, such as music creation, where users need interfaces that allow for both high-level control over abstract concepts and precise manipulation of low-level details. Achieving this balance between creative freedom and technical control is critical for musicians and composers when working with generative systems. 

Generative models for music have explored various control mechanisms to bridge the gap between user intention and machine output [2–6]. However, there is no clear consensus on which control modalities or signals are most effective. Currently, one of the most common methods for interacting with generative music systems is through text input [2–4], which leverages shared embedding spaces for text and audio information [7]. While this approach has facilitated significant advancements, it lacks the fine-grained control required for detailed music production. 

> 1 `https://lightlatentcontrol.github.io` ∗Research undertaken while an intern at Sony CSL - Paris 

> © T. Baker and J. Nistal. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: T. Baker and J. Nistal, “LiLAC: A Lightweight Latent ControlNet for Musical Audio Generation”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

In response to these limitations, some studies have experimented with conditioning generative models on timevarying signals, such as pitch or dynamics [5, 8]. These provide more specificity but are still constrained by a key issue: control signals are typically required during the training process of the generative model. Once the model has learned to respond to these inputs, the control mechanisms become fixed and inflexible. 

Modular approaches like ControlNet [9] enable flexible, post-hoc control of image generative models and have recently been adapted to music generation [10,11]. While effective, these techniques come with important limitations: memory-intensive clones of the network for each new control [9], or rigid multi-control schemes [12]. 

In this work, we adapt ControlNet’s framework to musical audio generation, introducing a modular architecture that replaces cloned encoder blocks with lightweight convolutional layers. While similar parameter-efficient approaches exist in computer vision [13], our method is the first to demonstrate this for music, enabling flexible training of multiple independent control models (e.g., chroma, chords) without retraining the backbone. By decoupling controls into task-specific modules, users can deploy only the necessary conditions during inference, often with lower memory overhead than a single traditional ControlNet branch. Crucially, our evaluations—spanning objective metrics (FAD, APA) and subjective listening tests—show that this streamlined design achieves performance comparable to ControlNet in audio quality and condition adherence, establishing a practical balance between flexibility and fidelity for music generation workflows. 

## 2. RELATED WORK 

Controls for music generation models encompass diverse input modalities. Text prompting is widely used [2–4,14– 17], and recent joint text-audio embeddings allow zeroshot control without paired data [7, 18, 19], enabling edits like “make this piece of music more happy” [20, 21]. However, text can be ambiguous and less suited for precise control in music production. Finer-grained controls, such as melody [5], rhythm and dynamics [8], or timbral features [22, 23], offer more precision. Multimodal inputs like images or video also expand creative possibilities [24]. Audio-based conditioning is particularly effective for tasks like accompaniment generation and style transfer [25–31], with models like Diff-A-Riff [6, 32] and 

287 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

SingSong [33] leveraging input audio to guide generation. Control integration strategies vary—from trainingtime conditioning to inference-time guidance [34] or latent optimization [35,36]. Inspired by ControlNet, recent methods introduce auxiliary networks for control [10,11], while others, like Sketch2Sound [37], explore lightweight alternatives. Despite this progress, optimal strategies remain unclear. ControlNet-style designs offer modularity but are often resource-intensive or inflexible. To address this, we propose a new lightweight and modular architecture that retains ControlNet’s strengths with improved efficiency. 

## 3. BACKGROUND 

This work builds on ControlNet [9] (see Sec. 3.2), a framework for introducing post-hoc controllability into pretrained generative models. While our architecture is generalisable to any generative model, we utilise Diff-a-Riff [6] (see Sec. 3.1) as the backbone model throughout this paper. In the following sections, we provide an overview of these two architectures, laying the groundwork for the proposed methodology. 

## 3.1 Diff-A-Riff 

Diff-a-Riff [6] is a Latent Diffusion Model (LDM) designed to generate high-quality individual musical stems that align with a user-provided musical audio sample, denoted Context. The model employs a Consistency Autoencoder (CAE) [38] to compress raw audio into compact latent representations and utilises an Elucidated Diffusion Model (EDM) [39] framework. The CAEs latent audio codec reduces 48 kHz audio to a 64-dimensional encoding at ∼12 Hz. Generation can be controlled via audio references, text prompts, or interpolations of both, facilitated by a shared CLAP embedding space [7, 19]. For further details, refer to the original paper [6]. 

## 3.2 ControlNet 

ControlNet [9] introduces a method to augment large pretrained text-to-image diffusion models with new controls. It achieves this by freezing the parameters of the original model, or backbone, and introducing a so-called adaptor branch—a trainable copy of the backbone’s encoding layers. This branch processes both original inputs and new conditional signals, feeding activations back through zero-initialised convolutions while reusing only the original training objective. 

The decoupled architecture allows for conditioning with limited specialised data, enabling diverse controls (edges, depth maps, segmentation, poses) without compromising the pretrained backbone’s capabilities. 

ControlNet has been successfully adapted to musical audio, providing time-frequency controls like pitch or loudness [10, 11]. Below, we provide a brief overview of the details relevant to this paper. 

## 3.2.1 Architecture 

The architecture is displayed in Fig. 1. For layer l, we utilise both a frozen encoder block Fl(xl−1,e) and its cloned adaptor block counterpart Gl(x `ˆ` l−1,e). Here, xl−1 and x `ˆ` l−1, represent the outputs from the previous frozen and control layers, respectively, while e denotes the backbone’s original conditional embeddings. Using zero convolutions Zs, the skip connection sl is computed as: 



<!-- Start of picture text -->
sl = Fl(xl−1,e) + Zs(Gl(x ˆ l−1,e)) (1)<br><!-- End of picture text -->

The input to the adaptor branch x `ˆ` 0 is derived from the noised input tensor x0 and the new conditional c through the input zero convolution: x `ˆ` 0 = x0 + Zin(c). 

ControlNet [9] demonstrates that using cloned encoders from the backbone model is critical for effective control signal integration, as randomly initialised convolutions compromise condition adherence, particularly when text conditioning is misaligned. Additionally, zero convolutions—used to introduce the control signal via skip connections—gradually introduce the signal during training, improving stability and output quality. 

## 4. LILAC 

In this section, we introduce LiLAC and detail how its architecture, conditioning mechanisms, and training methodologies diverge from ControlNet. 

## 4.1 Proposed Architecture 

In Fig. 1, we depict the basic block of LiLAC’s architecture. Instead of cloning the backbone’s encoder, LiLAC performs a second pass through each of the frozen encoder blocks, wrapping these by smaller convolutional layers. Specifically, we introduce three layers per block: a head layer before the frozen block, a tail layer after the frozen block, and a residual connection to preserve condition information as it passes through the frozen block. 

Formally, we replace the cloned encoder block Gl(x,e `ˆ` ) in (1) with 



<!-- Start of picture text -->
Gl(x,e ˆ ) ≈It (Fl(Ih(x ˆ ),e)) + Zr(x ˆ ),<br>� � � ��� ���<br>tail head residual<br><!-- End of picture text -->

where I represents the identity convolutions used as the head and tail layers (see Sec. 4.1.1), and Zr denotes the zero convolution used as the residual connection. 

While other multi-control methodologies have proposed reintroducing the condition into each block [10], we found empirically that this approach does not improve condition adherence and adds redundant parameters. 

## 4.1.1 Identity Convolutions 

As discussed in Sec. 3.2.1, ensuring the adaptor branch leverages the backbone model’s knowledge while gradually introducing the conditional signal during training is crucial. We achieve this by initialising the adaptor pathway 

288 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
❆ ❆<br><!-- End of picture text -->

Figure 1. ControlNet [9] (left) and LiLAC (right) adaptor blocks (l = `1` ). The noisy input signal is denoted as x0, and conditional signal as c. The frozen encoder block is denoted F1, and its cloned copy G1. Identity I and zero Z convolutions, along with the skip connection pathway s1 are also illustrated. 

to mirror the backbone encoder through identity convolutions I, in the head and tail layers, and zero convolutions, Z, in the residual layers. 

We initialise any n-dimensional Identity convolution kernel biases to 0 and the weights WI[k1,...kn,,i,j] as: 



<!-- Start of picture text -->
1 k1,...kn = K 2 − 1 , and i = j<br>WI[k1,...kn,i,j] =<br>0 otherwise<br>⎧⎪⎪⎨⎪⎪⎩<br><!-- End of picture text -->

Where k1,...kn index spatial positions in the kernel, and i,j index input and output channels. K is the kernel size and must be odd; in our case, all convolution kernels are size 1 to maintain a lightweight network. 

## 4.2 Conditioning Signals 

As outlined in Section 4.1, the condition c is introduced to the adaptor branch by adding it to the noised input x0. However this requires dimensional alignment between both tensors. For n-dimensional input data with C channels, the noised input is represented as x0 ∈ R<sup>C×k1×...×kn</sup> . Conditions are provided as feature maps in the form c ∈ R<sup>N×k1×...×kn</sup> , where N is the number of condition channels. To align the condition with the input tensor, the initial zero convolution Zin also maps the condition’s channels from N to C before they are combined. 

## 5. EXPERIMENTAL SETUP 

## 5.1 Data 

In this work, we use the same dataset from Diff-A-Riff [6], comprising 12,000 multi-track recordings, randomly split into 1 million 10-second segments. During training, the model receives one track as the target and a random combination of the remaining tracks as musical Context. 

## 5.1.1 Conditions 

In addition to the original training data, we pre-extract the required conditioning control signals from each audio track 

as specified below. For evaluation purposes, we select two distinct signals to address different use cases: chroma pitch class conditioning and chord conditioning. 

Chroma. A chromagram is extracted from the target single track using the librosa library [40]. The 12 chroma bins are placed along the channel dimension, and the time scale is downsampled to match the frame rate of the latent audio codec used by the backbone model (∼ 11.7 Hz) [38]. 

Chord. We extract chord symbols for each frame from mixed multi-track audio using Deep12MIR [41] and convert them into a 12-dimensional chroma-like format. Each chord is encoded as a vector where pitch classes in the chord are assigned 1, the root note 2, and remaining entries 0. This format supports all chord symbols, with harmonically related chords receiving similar embeddings, and facilitates the use of arbitrary chord shapes absent in the training data. 

## 5.2 Training details 

We follow the backbone’s training methodology [6]. Conditions Context, e, and c are all independently dropped out with a 50% probability during the training of the adaptor branch [9], encouraging the model to use the new condition, c as a replacement for missing information and enabling Classifier Free Guidance (CFG) [42] at inference. All models are trained for 2 days on a single NVIDIA RTX 3090 GPU with a batch size of 128. We use AdamW [43] optimizer with a base learning rate of `10`<sup>−4</sup> and a cosine annealing learning rate scheduler with linear warmup [44]. 

## 5.3 Objective Evaluation 

In the following section, we present two objective evaluation strategies: one comparing our methodology against baseline models, and the other analysing condition conflicts and their impact on condition adherence. 

## 5.3.1 Metrics 

We employ a subset of the metrics used in the backbone paper [6]: Fréchet Audio Distance (FAD) [45] for audio quality and diversity; Audio Prompt Adherence (APA) [46] and CLAP Score (CS) for context and text adherence, respectively. For evaluating adherence to the LiLAC-provided chromagram conditioning we calculate the chroma Mean Squared Error (cMSE) between input and output chromagrams. All metrics are computed by averaging across five sets of 500 samples. Distribution-based metrics such as FAD and APA are measured using the CLAP embedding space [7,19] against a background dataset of 5,000 real audio samples. 

## 5.3.2 Baselines 

We compare LiLAC against four baseline configurations: the backbone model in three conditioning setups—totally unconditioned (Diff-a-Riff*), with CLAP (Diff-a-Riff ), and with both CLAP and context (Diff-a-Riff + Context)—as well as the original ControlNet architecture applied to the backbone. 

289 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 5.3.3 Comparison and Ablation 

With the aim of keeping the architecture as light as possible, we conduct an ablation study for each of the three LiLAC adaptor layers described in Section 4.1-Head (H), Tail (T), and Residual (R). We evaluate their performance relative to the parameter overhead (see Tab. 1). Additionally, we test a model variant denoted LiLAC* that avoids a second pass through the backbone model by directly inserting the new adaptor layers as part of the backbone’s forward pass, similar in idea to previous work [37] (Although notably we don’t further fine-tune our backbone model). 

For the objective evaluations, we deliberately employ raw chromagram conditioning due to its high information density, enabling us to establish a more accurate upper bound on the model’s conditional adherence performance. Since each audio signal produces only a single chromagram, this allows for precise and unambiguous objective comparisons using the cMSE. In contrast, chord symbols can have multiple valid interpretations for a single stem, and as there is no unambiguous single way to evaluate adherence across a variety of instrument classes, we reserve these for the subjective test (see Sec. 5.4). 

## 5.3.4 Conflictive Conditioning 

Next, we evaluate how LiLAC and ControlNet-style models respond to conflicting CLAP and chroma conditionings (e.g., a solo violin CLAP embedding with a polyphonic chroma condition). Certain conditions, especially those extracted directly from audio, can be "overspecified"—containing redundant information. For example, chromagrams may include also traces of timbre and pitch range due to lower chroma bin resolution at lower frequencies. We measure the change in CLAP Score across different conditioning setups to quantify how these added control conditions may override or "leak" into the backbone model’s original CLAP conditioning. 

We compare three setups: 1) CLAP embeddings and control signals are aligned (i.e., extracted from the same source audio signal); 2) CLAP embeddings and control signals are misaligned (sourced from different audio examples); and 3) the model receives only the control signal, with CLAP conditioning omitted, labelled none. Using these setups, we evaluate the following variables: 

Impact of Architecture: We compare all proposed LiLAC configurations as well as ControlNet to assess which architecture is more susceptible to CLAP leakage—where over-specified control signals (e.g., chroma) can dominate or obscure CLAP’s condition. By contrasting performance in aligned vs. misaligned configurations, we quantify how strongly each model prioritises information from the new control signals over pre-existing CLAP embeddings. 

Impact of Control Signal Specificity: We evaluate three control signal types: (1) Chroma, an over-specified signal containing pitch, timing, and timbral information; (2) Thresholded Chroma, a variant where amplitudes ≥ `0` . `9` are clipped to 1 and all others to 0, reducing fine timbral details to minimise leakage; and (3) Chords, a well- 

specified signal conveying only harmonic structure. By analysing the difference in CLAP Score across these conditions, we quantify whether reducing surplus information in the conditional signal leads to more faithful adherence to the CLAP embedding. 

## 5.4 Subjective Evaluation 

To subjectively evaluate LiLAC’s effectiveness in conditioning the diffusion model, we conduct two listening tests loosely following MUSHRA guidelines [47] (i.e., using the true accompaniment as hidden reference in our case). In both tests, participants rate sets of audio samples on a 100-point scale (0: poor, 100: excellent) based on two criteria: audio quality and subjective adherence, respectively, for each questionnaire.<sup>2</sup> Each test comprises 10 questions, with each presenting 5 unlabeled, randomly ordered samples corresponding to LiLAC<sup>H</sup> , LiLAC<sup>HTR</sup> , ControlNet, the ground-truth reference track and a negative anchor. Further details about each test are given below. 

## 5.4.1 Subjective Audio Quality (SAQ): 

The SAQ test evaluates whether the control models audibly degrade the output quality. Participants are asked to rank each set of examples based on perceived audio quality and the presence of artifacts. For each question round, we start from a reference track, randomly sampled from the validation set, and extract the chromas and CLAP embeddings. Using these as conditioning, we generate an example with each of the three evaluated models. To create the negative anchor, we apply heavy compression (16 kbps MP3) to the ground truth track. The ground truth audio is used as a positive anchor. Shared chroma and CLAP conditioning in this test ensures that all examples are comparable, as they should ideally exhibit the same pitch distribution and timbre. This approach encourages participants to focus solely on evaluating audio quality. 

## 5.4.2 Subjective Condition Adherence (SCA): 

The SCA test evaluates the models’ ability to adhere to chord conditioning, chosen for its flexibility in generating varied outputs (e.g., chords, bass lines, melodies). Participants rank how well the generated output aligns harmonically with the chord conditioning extracted from the multitrack recording. For each round, we begin with a multitrack recording and isolate one instrument track as the reference. Before generation, we evaluate the remaining multitrack; if it does not contain at least one polyphonic voice throughout the test sample, then the sample lacks sufficient harmonic content to reliably discern chords and is excluded from the listening test We extract chord symbols<sup>˙</sup> from the full multitrack and CLAP embeddings from the reference track, then generate an example for each tested model. The negative anchor is generated using the CLAPconditioned Diff-A-Riff backbone, i.e., without chord or context conditioning. To facilitate comparison, the generated output is panned to the left, while the remaining multitrack is panned to the right. 

> 2 `https://linktr.ee/lilactests` 

290 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 6. RESULTS 

In what follows, we present and discuss the results of the evaluations outlined in Sec. 5. 

|Model|APA ↑|FAD ↓|cMSE ↓|
|---|---|---|---|
|Diff-a-Riff* (432M)|0.63|0.812|0.206|
|+Context|1.00|0.508|0.148|
|+ ControlNet (165M)|1.00|0.507|0.052|
|H (32M)|1.00|0.506|0.057|
|+ LiLAC<br>HT (48M)|1.00|0.507|0.056|
|<br>HR (47M)|1.00|0.509|0.056|
|HTR (64M)|1.00|0.507|0.055|
|+ LiLAC* (47M)|1.00|0.508|0.070|



Table 1. Objective metrics: Audio Prompt Adherence (APA) and Fréchet Audio Distance (FAD) for audio quality; chroma Mean Squared Error (cMSE) for chroma adherence. All models include CLAP conditioning except for Diff-A-Riff<sup>∗</sup> . Additionally, all new control models are conditioned on chroma. 

## 6.1 Objective Experiments 

Table 1 shows objective comparison between LiLAC and baseline models (see Sec.5.3.3). The APA metric—a distribution-based score bounded in range [ `0` , `1` ] [46]—shows that all models conditioned on CLAP embeddings and chroma outperform the context-free Diff-ARiff baseline (Diff-A-Riff<sup>∗</sup> ) and match the performance of the context-conditioned variant (+ Context). This indicates that chromagram-based conditioning is consistently effective at guiding alignment with the multitrack, regardless of architectural variations. Analogously, FAD scores remain comparable across all setups, suggesting that adding conditioning does not degrade audio quality. In particular, the near-identical FAD scores between Diff-A-Riff + Context baseline, ControlNet and LiLAC models indicate that posthoc conditioning doesn’t compromise fidelity (low FAD, high APA) and may enhance controllability (high APA). While these results provide a statistical perspective on the overall distribution of generated outputs and their alignment with musical context based on chroma alone, they do not directly reveal how faithfully models respond to specific chroma inputs. A pairwise metric is required to evaluate adherence on a per-example basis. For this purpose, we report cMSE. Here, ControlNet achieves the best absolute adherence to the chroma input, though all LiLAC configurations deliver competitive results while maintaining a considerably smaller parameter count (i.e., 165M in ControlNet versus 32M in LiLAC<sup>H</sup> )<sup>3</sup> . Among them, the HTR variant shows stronger performance, with cMSE close to ControlNet. Interestingly, LiLAC*, a lightweight 

> 3 As the size of the adaptor blocks scales with the encoder’s channel dimensions, the exact parameter reduction depends on the specific backbone architecture. For Diff-A-Riff [6], our lightest configuration (LiLAC<sup>H</sup> ) uses only 19% of ControlNet’s parameters. This efficiency scales with larger architectures: for Stable Audio Open [48], the parameter usage drops to 10.2%, while for image models such as SD V2 [49], it reduces dramatically to 2.6%. 

architecture inspired by prior work [37], exhibits limitations in controlling fine melodic nuances, thus, we exclude it from further evaluations. 

|Model|Aligned|Misaligned|None|
|---|---|---|---|
|Diff-a-Riff|0.65 (0.17)|0.65 (0.21)|0.17 (0.21)|
|+ LiLAC<sup>H</sup>|0.67 (0.06)|0.55(0.06)|0.57(0.06)|
|+ LiLAC<sup>HT</sup>|0.67 (0.06)|0.54 (0.06)|0.58 (0.05)|
|+ LiLAC<sup>HR</sup>|0.67 (0.06)|0.54 (0.06)|0.58 (0.06)|
|+ LiLAC<sup>HTR</sup>|0.67 (0.05)|0.53 (0.06)|0.58 (0.05)|
|+ ControlNet|0.67 (0.05)|0.52 (0.06)|0.60 (0.05)|



Table 2. CS↑<sup>a</sup> (cMSE↓) for models trained with chroma conditioning and Diff-A-Riff baseline. Each column corresponds with a different setting: aligned pairs of chromagram and CLAP embedding, misaligned pairs, or without CLAP embedding (see Sec. 5.3.4). aCS↓ in the None case 

We next investigate how the new chroma adaptors interact with the backbone’s CLAP default conditioning (see Sec.5.3.4). Table 2 reports CLAP similarity scores (CS) and chroma reconstruction error (cMSE) across various model configurations. The results indicate a degree of information overlap between CLAP embeddings and chroma conditions. When both are present—but convey conflicting information—CLAP similarity scores noticeably decline, suggesting that chroma conditioning can partially overwrite or interfere with the original CLAP guidance. However, this drop is moderate, and the model still reconstructs a faithful chromagram, as reflected in the low cMSE even in the misaligned setting. This implies that the model makes reasonable sense of the conflicting conditionals—following the CLAP guidance as much as possible while still producing generations that faithfully adhere to the chroma conditioning. 

Interestingly, in the CLAP-unconditioned setting, cMSE remains low while CS stays high. This supports our hypothesis of information redundancy between chromagrams and CLAP embeddings. It suggests that the model can still infer high-level cues—such as timbre—from chromagrams alone, allowing it to produce content that aligns with what CLAP, even in its absence. That said, the model’s ability to maintain reasonable CLAP similarity without explicit CLAP input does not necessarily mean it reconstructs the original instrument associated with the chromagram. More likely, it infers a plausible instrument class—such as strings or pads—that fits the given pitch range and harmonic content. This suggests that the model interprets chroma conditioning sensibly: when CLAP is available, it may refine or overwrite the inferred instrument identity; when absent, it defaults to generating something timbrally coherent that aligns with the chroma structure. 

Among all setups, the LiLAC architecture demonstrates the least susceptibility to CLAP interference, with its lightweight variant performing best under both conflicting and CLAP-ablated conditions. This robustness is likely due to its simplified structure, which limits the extent to which the model encodes auxiliary information alongside the CLAP embedding. 

291 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

|Condition|Aligned|Misaligned|None|
|---|---|---|---|
|Diff-a-Riff|0.65 (0.17)|0.65 (0.21)|0.17 (0.21)|
|+ Chord|0.65 (0.14)|0.64(0.20)|0.36(0.18)|
|+ Thresh|0.65 (0.08)|0.62 (0.17)|0.45 (0.10)|
|+ Chroma|0.67<br>(0.06)|0.55 (0.06)|0.57 (0.06)|



Table 3. CS↑<sup>a</sup> (cMSE↓) for LiLAC<sup>H</sup> trained on chord, thresholded chroma, and chroma with the Diff-a-Riff baseline (see Sec. 5.3.4). aCS↓ in the None case 

To reduce redundancy with CLAP, we evaluate LiLAC<sup>H</sup> —our lightest and best-performing variant—using compressed melodic inputs: thresholded chromagrams (thresh) and chords. Table 3 compares performance across CLAP-aligned, misaligned, and unconditioned (None) settings (see Sec. 5.3.4). 

Intuitively, less specific conditioning signals should exhibit lower overlap with CLAP embeddings. This is confirmed by the results: thresholding the chromagram significantly reduces the conflict between the two modalities. Among the tested conditions, chords show the least interference, with almost no drop in CLAP similarity in the misaligned case. Notably, even without CLAP conditioning, the chord model achieves a CLAP score of 0.36—up from 0.17 in the unconditioned baseline—suggesting that a substantial amount of global musical information (e.g., tempo, tonality) is implicitly captured by the chord input alone. 

However, this robustness may come at the cost of reduced influence from the conditioning. We observe that weaker conditions, like chords, are more easily overridden by CLAP. For instance, the cMSE rises sharply from 0.08 to 0.17 when CLAP is misaligned, despite the sparsity of the chord-based input. This indicates that even minimal shifts in CLAP can significantly distort the resulting chroma, especially when the conditioning is less constraining. To confirm this, we re-evaluated the cMSE under the aligned setting for chords and observed a consistent value around 0.14. This validates that the observed jump in cMSE under misalignment reflects a genuine interference effect, rather than noise or sampling variance. 

Overall, these findings highlight that our proposed conditioning mechanisms—especially when simplified—can effectively cooperate with CLAP guidance. When signals are aligned, they yield coherent generations that satisfy both timbral and harmonic constraints. When conflicting, the model tends to prioritise chroma while still leveraging CLAP to guide plausible generation. Even in the absence of CLAP, the model retains the ability to infer global cues such as tempo, tonality, and timbre from abstract melodic inputs, demonstrating the versatility and robustness of the conditioning approach. 

## 6.2 Subjective Experiments 

Table 4 presents results from our Subjective Audio Quality (SAQ) and Subjective Condition Adherence (SCA) evaluations (see Sec. 5.4). Across both tests, we collected a total of 1,250 ratings from 25 participants (11 for 

|Model|SAQ ↑|SCA ↑|
|---|---|---|
|Reference|61.5±4.7|82.3±4.3|
|ControlNet<br>|56.4±4.2|66.5±5.1|
|LiLAC<sup>H</sup>|60.6±4.6|65.9±4.8|
|LiLAC<sup>HTR</sup>|58.7±4.2|68.6±4.9|
|Anchor|26.4±4.9|12.5±2.5|



Table 4. Listener ratings with 95% confidence intervals for SAQ and SCA across evaluated models (see Sec. 5.4). 

SCA and 14 for SAQ). In the SAQ test, all three models were rated comparably in terms of audio quality. The two LiLAC variants—especially the lightweight configuration—slightly outperformed ControlNet based on both mean score and average rank. However, these differences did not reach statistical significance, either among the three models or relative to the original stem, as indicated by the Friedman test (p > `0` . `10` ). This aligns with expectations: given that the backbone is frozen, it is unlikely that control mechanisms alone would improve audio quality. Nevertheless, the slightly better performance of LiLAC models may reflect a better preservation of pre-trained features, due to their smaller and more focused adapter layers. 

The SCA results show similar outcomes. All models significantly outperform unconditional generation (p < `0` . `0001` ), and again show remarkable similarity to one another (p > `0` . `8` ). Regarding conditional adherence to the original stem, there is a more noticeable gap to the reference, however LiLAC<sup>HTR</sup> comes closer than other models, showing only marginally significant differences (p = `0` . `09` ). Overall, these findings are consistent with our expectations: while audio quality remains stable across control methods, condition adherence benefits more clearly from architectural improvements like LiLAC<sup>HTR</sup> . 

## 7. CONCLUSION 

In this paper, we introduced a lightweight and flexible control methodology for text-to-audio diffusion models, inspired by ControlNet but with a significantly reduced parameter count. Our approach supports multiple configurations to accommodate control signals of varying complexity, while maintaining— and in some cases improving upon—the audio quality and condition adherence of the original method, as demonstrated in both objective and subjective evaluations. We believe this modular and efficient framework paves the way for more expressive and musically useful control modalities in audio generation. 

As future work, we plan to explore the modularity and composability of multiple LiLAC controllers operating over a shared backbone, as well as investigate whether our method generalises to non-convolutional architectures such as DiT<sup>4</sup> . 

> 4 Subsequent to our initial submission, we have successfully applied this architecture to the DiT-based Diff-a-Riff 2 [32] and seen similar results, suggesting that our methodology generalises well beyond convolutional architectures. For this, we adapted the ControlNet methodology pioneered in [50] and again substituted the cloned transformer blocks for the pre-existing frozen blocks wrapped by our adaptor layers . 

292 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 8. ETHICS STATEMENT 

Sony Computer Science Laboratories is committed to exploring the positive applications of AI in music creation. We collaborate with artists to develop innovative technologies that enhance creativity. We uphold strong ethical standards and actively engage with the music community and industry to align our practices with societal values. Our team is mindful of the extensive work that songwriters and recording artists dedicate to their craft. Our technology must respect, protect, and honour this commitment. 

LiLAC presents a lighter, more flexible control paradigm that enables musicians to exercise fine-grained control over generative model outputs, ensuring complete artistic agency. We hope the presentation of this model will encourage commercial text-to-audio model providers to incorporate similar additional controls into their workflows, thereby empowering users with greater creative autonomy. 

Both LiLAC and its backbone model, Diff-A-Riff, have been trained exclusively on datasets that were legally acquired for internal research and development purposes. Consequently, neither the training data nor the models can be made publicly available. We remain committed to full legal compliance and proactively address all ethical considerations in our work. 

## 9. REFERENCES 

- [1] J. Schneider, “Explainable Generative AI (GenXAI): A Survey, Conceptualization, and Research Agenda,” Artificial Intelligence Review, vol. 57, 2024. 

- [2] A. Agostinelli, T. I. Denk, Z. Borsos, J. Engel, M. Verzetti, A. Caillon, Q. Huang, A. Jansen, A. Roberts, M. Tagliasacchi, M. Sharifi, N. Zeghidour, and C. Frank, “MusicLM: Generating Music From Text,” 2023. 

- [3] H. Liu, Z. Chen, Y. Yuan, X. Mei, X. Liu, D. Mandic, W. Wang, and M. D. Plumbley, “AudioLDM: Textto-Audio Generation with Latent Diffusion Models,” in International Conference on Machine Learning (ICML), Hawaii, United States, 2023. 

- [4] Z. Evans, C. J. Carr, J. Taylor, S. H. Hawley, and J. Pons, “Fast Timing-Conditioned Latent Audio Diffusion,” in International Conference on Machine Learning (ICML), Vienna, Austria, 2024. 

- [5] J. Copet, F. Kreuk, I. Gat, T. Remez, D. Kant, G. Synnaeve, Y. Adi, and A. Défossez, “Simple and Controllable Music Generation,” in 37th Conference on Neural Information Processing Systems (NeurIPS), New Orleans, United States, 2023. 

- [6] J. Nistal, M. Pasini, C. Aouameur, M. Grachten, and S. Lattner, “Diff-A-Riff: Musical Accompaniment Cocreation via Latent Diffusion Models,” in Proc. of the 25th Int. Society for Music Information Retrieval Conf. (ISMIR), San Francisco, United States, 2024. 

- [7] B. Elizalde, S. Deshmukh, M. A. Ismail, and H. Wang, “CLAP: Learning Audio Concepts From Natural Language Supervision,” in IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), Rhodes Island, Greece, 2023. 

- [8] Y.-K. Wu, C.-Y. Chiu, and Y.-H. Yang, “JukeDrummer: Conditional Beat-aware Audio-domain Drum Accompaniment Generation via Transformer VQ-VAE,” in Proc. of the 23rd Int. Society for Music Information Retrieval Conf. (ISMIR), Bengaluru, India, 2022. 

- [9] L. Zhang, A. Rao, and M. Agrawala, “Adding Conditional Control to Text-to-Image Diffusion Models,” in IEEE International Conference on Computer Vision (ICCV), Paris, France, 2023. 

- [10] S.-L. Wu, C. Donahue, S. Watanabe, and N. J. Bryan, “Music ControlNet: Multiple Time-varying Controls for Music Generation,” IEEE/ACM Transactions on Audio, Speech, and Language Processing, (TASLP), vol. 32, Nov. 2023. 

- [11] S. Hou, S. Liu, R. Yuan, W. Xue, Y. Shan, M. Zhao, and C. Zhang, “Editing Music with Melody and Text: Using ControlNet for Diffusion Transformer,” in International Conference on Acoustics, Speech, and Signal Processing (ICASSP), Hyderabad, India, 2025. 

- [12] S. Zhao, D. Chen, Y.-C. Chen, J. Bao, S. Hao, L. Yuan, and K.-Y. K. Wong, “Uni-ControlNet: All-in-One Control to Text-to-Image Diffusion Models,” in 37th Conference on Neural Information Processing Systems (NeurIPS), New Orleans, United States, 2023. 

- [13] D. Zavadski, J.-F. Feiden, and C. Rother, “ControlNetXS: Designing an Efficient and Effective Architecture for Controlling Text-to-Image Diffusion Models,” 2023. 

- [14] F. Schneider, O. Kamal, Z. Jin, and B. Schölkopf, “Moûsai: Text-to-Music Generation with LongContext Latent Diffusion,” 2023. 

- [15] Q. Huang, D. S. Park, T. Wang, T. I. Denk, A. Ly, N. Chen, Z. Zhang, Z. Zhang, J. Yu, C. Frank, J. Engel, Q. V. Le, W. Chan, Z. Chen, and W. Han, “Noise2Music: Text-conditioned Music Generation with Diffusion Models,” 2023. 

- [16] P. Li, B. Chen, Y. Yao, Y. Wang, A. Wang, and A. Wang, “JEN-1: Text-Guided Universal Music Generation with Omnidirectional Diffusion Models,” in IEEE Conference on Artificial Intelligence (CAI), Singapore, Singapore, 2024. 

- [17] H. Liu, Y. Yuan, X. Liu, X. Mei, Q. Kong, Q. Tian, Y. Wang, W. Wang, Y. Wang, and M. D. Plumbley, “AudioLDM 2: Learning Holistic Audio Generation with Self-supervised Pretraining,” IEEE/ACM Transactions on Audio, Speech and Language Processing, vol. 32, May 2024. 

293 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [18] Q. Huang, A. Jansen, J. Lee, R. Ganti, J. Y. Li, and D. P. W. Ellis, “MuLan: A Joint Embedding of Music Audio and Natural Language,” in Proc. of the 23rd Int. Society for Music Information Retrieval Conf. (ISMIR), Bengaluru, India, 2022. 

- [19] Y. Wu, K. Chen, T. Zhang, Y. Hui, M. Nezhurina, T. Berg-Kirkpatrick, and S. Dubnov, “Large-scale Contrastive Language-Audio Pretraining with Feature Fusion and Keyword-to-Caption Augmentation,” in IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), Rhodes Island, Greece, 2023. 

- [20] Y. Zhang, Y. Ikemiya, G. Xia, N. Murata, M. A. Martínez-Ramírez, W.-H. Liao, Y. Mitsufuji, and S. Dixon, “MusicMagus: Zero-Shot Text-to-Music Editing via Diffusion Models,” in The 33rd International Joint Conference on Artificial Intelligence (IJCAI), Jeju, Korea, 2024. 

- [21] H. Manor and T. Michaeli, “Zero-Shot Unsupervised and Text-Based Audio Editing Using DDPM Inversion,” in International Conference on Machine Learning (ICML), Vienna, Austria, 2024. 

- [22] J. Nistal, S. Lattner, and G. Richard, “DrumGAN: Synthesis of Drum Sounds With Timbral Feature Conditioning Using Generative Adversarial Networks,” in Proc. of the 21st Int. Society for Music Information Retrieval Conf. (ISMIR), Montréal, Canada, 2020. 

- [23] J. Nistal, C. Aouameur, I. Velarde, and S. Lattner, “DrumGAN VST: A Plugin for Drum Sound Analysis/Synthesis With Autoencoding Generative Adversarial Networks,” in International Conference on Machine Learning (ICML), Baltimore, United States, 2022. 

- [24] R. Huang, J. Huang, D. Yang, Y. Ren, L. Liu, M. Li, Z. Ye, J. Liu, X. Yin, and Z. Zhao, “Make-An-Audio: Text-To-Audio Generation with Prompt-Enhanced Diffusion Models,” in International Conference on Machine Learning (ICML), Hawaii, United States, 2023. 

- [25] S. Lattner and M. Grachten, “High-Level Control of Drum Track Generation Using Learned Patterns of Rhythmic Interaction,” in Workshop on Applications of Signal Processing to Audio and Acoustics (WASPAA), New Paltz, United States, 2019. 

- [26] M. Grachten, S. Lattner, and E. Deruty, “BassNet: A Variational Gated Autoencoder for Conditional Generation of Bass Guitar Tracks with Learned Interactive Control,” Applied Sciences, vol. 10, 2020. 

- [27] J. D. Parker, J. Spijkervet, K. Kosta, F. Yesiler, B. Kuznetsov, J.-C. Wang, M. Avent, J. Chen, and D. Le, “StemGen: A music generation model that listens,” in International Conference on Acoustics, Speech and Signal Processing (ICASSP), Seoul, Korea, 2024. 

- [28] M. Pasini, M. Grachten, and S. Lattner, “Bass Accompaniment Generation via Latent Diffusion,” in International Conference on Acoustics, Speech, and Signal Processing (ICASSP), Seoul, Korea, 2024. 

- [29] G. Mariani, I. Tallini, E. Postolache, M. Mancusi, L. Cosmo, and E. Rodolà, “Multi-Source Diffusion Models for Simultaneous Music Generation and Separation,” in International Conference on Learning Representations (ICLR), Vienna, Austria, 2024. 

- [30] G. Bindi and P. Esling, “Unsupervised Composable Representations for Audio,” in Proc. of the 25th Int. Society for Music Information Retrieval Conf. (ISMIR), San Francisco, United States, 2024. 

- [31] T. Karchkhadze, M. R. Izadi, and S. Dubnov, “Simultaneous Music Separation and Generation Using MultiTrack Latent Diffusion Models,” 2024. 

- [32] J. Nistal, M. Pasini, and S. Lattner, “Improving Musical Accompaniment Co-creation via Diffusion Transformers,” in 38th Conference on Neural Information Processing Systems (NeurIPS), Vancouver, Canada, 2024. 

- [33] C. Donahue, A. Caillon, A. Roberts, E. Manilow, P. Esling, A. Agostinelli, M. Verzetti, I. Simon, O. Pietquin, N. Zeghidour, and J. Engel, “SingSong: Generating musical accompaniments from singing,” 2023. 

- [34] M. Levy, B. D. Giorgi, F. Weers, A. Katharopoulos, and T. Nickson, “Controllable Music Production with Diffusion Models and Guidance Gradients,” in 37th Conference on Neural Information Processing Systems (NeurIPS), New Orleans, United States, 2023. 

- [35] Z. Novack, J. McAuley, T. Berg-Kirkpatrick, and N. J. Bryan, “DITTO: Diffusion Inference-Time T- Optimization for Music Generation,” in International Conference on Machine Learning (ICML), Vienna, Austria, 2024. 

- [36] Z. Novack, J. McAuley, T. Berg-Kirkpatrick, and N. Bryan, “DITTO-2: Distilled Diffusion InferenceTime T-Optimization for Music Generation,” in Proc. of the 25th Int. Society for Music Information Retrieval Conf. (ISMIR), San Francisco, United States, 2024. 

- [37] H. F. García, O. Nieto, J. Salamon, B. Pardo, and P. Seetharaman, “Sketch2Sound: Controllable Audio Generation via Time-Varying Signals and Sonic Imitations,” 2024. 

- [38] M. Pasini, S. Lattner, and G. Fazekas, “Music2Latent: Consistency Autoencoders for Latent Audio Compression,” in Proc. of the 25th Int. Society for Music Information Retrieval Conf. (ISMIR), San Francisco, United States, 2024. 

- [39] T. Karras, M. Aittala, T. Aila, and S. Laine, “Elucidating the Design Space of Diffusion-Based Generative Models,” in 36th Conference on Neural Information 

294 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

Processing Systems (NeurIPS), New Orleans, United States, 2022. 

- [40] B. McFee, C. Raffel, D. Liang, D. Ellis, M. McVicar, E. Battenberg, and O. Nieto, “Librosa: Audio and Music Signal Analysis in Python,” in Proc. of the 14th Python in Science Conf. (SCIPY), Austin, Texas, 2015. 

- [41] T. Akama, N. Polouliakh, and H. Kishi, “Deep12: Music Analysis AI,” 2023. 

- [42] J. Ho and T. Salimans, “Classifier-Free Diffusion Guidance,” in NeurIPS Workshop on Deep Generative Models and Downstream Applications, Online, 2021. 

- [43] I. Loshchilov and F. Hutter, “Decoupled Weight Decay Regularization,” in 7th International Conference on Learning Representations (ICLR), New Orleans, United States, 2019. 

- [44] ——, “SGDR: Stochastic Gradient Descent with Warm Restarts,” in 5th International Conference on Learning Representations (ICLR), Toulon, France, 2017. 

- [45] K. Kilgour, M. Zuluaga, D. Roblek, and M. Sharifi, “Fréchet Audio Distance: A Metric for Evaluating Music Enhancement Algorithms,” in Interspeech, Graz, Austria, 2019. 

- [46] M. Grachten, “Measuring Audio Prompt Adherence with Distribution-based Embedding Distances,” 2024. 

- [47] ITU-R BS.1534-3, “Methods for the subjective assessment of small impairments in audio systems,” 2015. 

- [48] Z. Evans, J. D. Parker, C. J. Carr, Z. Zukowski, J. Taylor, and J. Pons, “Stable Audio Open,” 2024. 

- [49] R. Rombach, A. Blattmann, D. Lorenz, P. Esser, and B. Ommer, “High-Resolution Image Synthesis with Latent Diffusion Models,” in Computer Vision and Pattern Recognition (CVPR), New Orleans, United States, 2022. 

- [50] J. Chen, Y. Wu, S. Luo, E. Xie, S. Paul, P. Luo, H. Zhao, and Z. Li, “PIXART-δ: Fast and Controllable Image Generation with Latent Consistency Models,” 2024. 

295 

