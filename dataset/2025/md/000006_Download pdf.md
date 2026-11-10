---
paper_id: "000006"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706331/files/000006.pdf"
---

# CONDITIONAL DIFFUSION AS LATENT CONSTRAINTS FOR CONTROLLABLE SYMBOLIC MUSIC GENERATION 

Matteo Pettenò Alessandro Ilic Mezza Alberto Bernardini 

Dipartimento di Elettronica, Informazione e Bioingegneria 

Politecnico di Milano, Milan, Italy 

```
matteo.petteno@mail.polimi.it, alessandroilic.mezza@polimi.it, alberto.bernardini@polimi.it
```

## ABSTRACT 

Recent advances in latent diffusion models have demonstrated state-of-the-art performance in high-dimensional time-series data synthesis while providing flexible control through conditioning and guidance. However, existing methodologies primarily rely on musical context or natural language as the main modality of interacting with the generative process, which may not be ideal for expert users who seek precise fader-like control over specific musical attributes. In this work, we explore the application of denoising diffusion processes as plug-and-play latent constraints for unconditional symbolic music generation models. We focus on a framework that leverages a library of small conditional diffusion models operating as implicit probabilistic priors on the latents of a frozen unconditional backbone. While previous studies have explored domain-specific use cases, this work, to the best of our knowledge, is the first to demonstrate the versatility of such an approach across a diverse array of musical attributes, such as note density, pitch range, contour, and rhythm complexity. Our experiments show that diffusiondriven constraints outperform traditional attribute regularization and other latent constraints architectures, achieving significantly stronger correlations between target and generated attributes while maintaining high perceptual quality and diversity. 

## 1. INTRODUCTION 

Latent Constraints (LC) [1] refer to a set of techniques for generating conditionally from unconditional generative models. Traditional methods for enforcing user-defined constraints during model training, such as using attributeregularization losses or training on curated subsets, require extensive labeled data, large amounts of computational power, and time-consuming hyperparameter tuning. The cost of retraining becomes increasingly prohibitive as the number of conditioning variables grows, especially when expert users need the flexibility to choose from a range of 

> © M. Pettenò, A. I. Mezza, and A. Bernardini. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: M. Pettenò, A. I. Mezza, and A. Bernardini, “Conditional Diffusion as Latent Constraints for Controllable Symbolic Music Generation”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

different attributes at any given time, as is the case in symbolic music generation and computer-assisted music composition. 

Deep latent-variable models like GANs and VAEs learn to generate diverse outputs by sampling from a structured latent space. By exploiting this property, LC provides a principled framework for endowing pre-trained unsupervised models with post-hoc conditional generation capabilities. This is achieved either explicitly, by optimizing a new model that imposes the desired behavior onto latent representations [1], or implicitly, by training a small personalized model to generate only from regions of the latent space [2]. In this way, at inference time, LC models yield latents that, once decoded, result in outputs with the desired attributes. LC is also closely related to latent translation [3], which introduces neural networks that bridge multimodal representations of different pre-trained generative models, conditioning on the respective domain labels. 

Latent diffusion [4] can be thought of as a class of LC. In Latent Diffusion Models (LDMs), the pre-trained autoencoder is typically understood as a way to compress the data into a lower-dimensional space where reverse diffusion is computationally feasible. By conditioning the denoising process, though, it is possible to steer the decoder to generate outputs with desired characteristics by feeding it inputs that lie in certain regions of the latent space associated with the desired attributes of the output, just like in existing LC methods. 

Diffusion-based symbolic music generation models have been conditioned on various inputs, including text prompts [5, 6], musical context [7], accompaniment [8], chords [9, 10], and rhythmic textures [10]. Recent methods, such as MelodyDiffusion [9] and Polyffusion [10], apply conditional denoising on piano roll representations, treating them as image-like data. As a result, sequence modeling is tightly coupled with control, making it infeasible to seamlessly substitute one conditioning signal for another without retraining the note-generation process. Notably, this also applies to many recent controllable generation methods that are not based on diffusion [11–13]. 

Against this backdrop, diffusion-driven LC offer a particularly compelling approach for achieving modular fader-like control [14, 15] over multiple musical attributes with an otherwise unconditional model, allowing users to manipulate different musical features along continuous axes through a range of attribute-specific LDMs. 

52 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

LDM specifications depend on the base unconditional model; Denoising Diffusion Probabilistic Models (DDPM) [16] and Denoising Diffusion Implicit Models (DDIM) [17] operate on continuous latent spaces, whereas Discrete DDPM [18] operate on tokenized representations. In particular, discrete diffusion models have recently shown promising results for symbolic music generation [19–21]. Prior work also explored latent diffusion for specific domains, such as emotion-controlled symbolic music generation either by learning from emotion-labeled data [22] or by relying on emotion classifier guidance [23]. Post-hoc control over black-box music rules has been tackled in [24] by means of stochastic control guidance, which, inspired by control theory, entails sampling several realizations of the next denoising step and selecting the one most compliant with the rule. 

In this work, by looking at latent diffusion through the lens of LC, we study LDMs as plug-and-play conditioning modules. Thus, we keep the base generative model fixed and develop a library of diffusion-driven LC models (“LCDiff”) trained on a range of non-differentiable and possibly continuous musical attributes, including contour, note density, pitch range, and rhythm complexity. 

We show that, compared to attribute-regularized VAEs [25, 26] and other LC architectures [3], LC-Diff improves fidelity (measured by Fréchet Music Distance [27]) and controllability (measured by the correlation between desired attributes and those of generated samples) across all attributes considered in the present study. 

## 2. DIFFUSION AS LATENT CONSTRAINTS 

Let z ∼ p(z|x) be the latent representation of an input sequence x with N tokens and attribute a ∈ R. Diffusion models employ a Markov chain to progressively corrupt input data with Gaussian noise and learn to reverse the process. Forward (latent) diffusion begins with the representation z0 = z and gradually adds noise following a schedule βt, with t = 1, . . . , T . At each step, Gaussian noise is introduced according to 



<!-- Start of picture text -->
q(zt|zt−1) = N (zt; � 1 − βtzt−1, βtI). (1)<br><!-- End of picture text -->

The LC-Diff reverse diffusion process aims to navigate the latent space of a pre-trained generative model by tracing a trajectory conditional on the target attribute starting from a noise sample zT ∼N (0, I). A denoising function ϵθ is trained to predict the additive noise at each step. ϵθ is thus conditioned on a and a time variable ξt that can be either the diffusion step ξt = t [16] or the continuous noise level ξt =<sup><mark>√</mark></sup> <mark>α¯</mark> t [28], where α¯t =<sup>�t</sup> i=1<sup>(1 −βi).</sup> 

By sampling the conditional distribution of zt at an arbitrary timestep in closed form 



<!-- Start of picture text -->
q(zt|z0) = N (zt; √ α¯tz0, (1 − α¯t)I), (2)<br><!-- End of picture text -->

it is possible to efficiently train ϵθ by optimizing random terms of the following objective [16]: 



<!-- Start of picture text -->
L = Ez0∼p(z|x),ϵ∼N (0,I),t �∥ϵ − ϵθ(zt, ξt, a)∥ 2� , (3)<br><!-- End of picture text -->



<!-- Start of picture text -->
Shift Scale<br>+<br>0/1<br>Linear Linear Linear Linear<br>SiLU SiLU<br>Linear Linear<br>Sinusoidal Encoding Sinusoidal Encoding<br>Noise level Attribute<br>+<br><!-- End of picture text -->

Figure 1: LC-Diff conditioning networks. 



<!-- Start of picture text -->
Residual Dense Block (×3)<br>Stack (×2)<br>+<br>+ ×<br>Linear (256) LayerNorm Linear (2048)<br>SiLU<br>Linear (2048) LayerNorm<br>Shift Scale<br><!-- End of picture text -->

Figure 2: LC-Diff denoiser architecture. 

where ξt is sampled from either U ({1, . . . , T }) [16] or U (<sup><mark>√</mark></sup> <mark>α¯</mark> t−1 <mark>,</mark><sup><mark>√</mark></sup> <mark>α¯</mark> t <mark>)</mark> [28]. 

## 2.1 Sampling 

Different sampling strategies have been explored in the literature. At inference time, DDPMs [16] involve a stochastic Markov process where, at each intermediate step, a small amount of Gaussian noise is added back in to encourage diversity in the generated samples. However, following a stochastic trajectory typically requires a large number of steps, slowing down the sampling process. DDIMs [17] differ from DDPMs by making the process deterministic. With this class of models, forward diffusion is reversed by 



<!-- Start of picture text -->
zt−1 = √ α¯ t−1 f (zt, ξt, a) + g(zt, ξt, a), (4)<br><!-- End of picture text -->

where 



<!-- Start of picture text -->
1 − α¯tϵθ ( zt , ξ t ,  a )<br>f (zt, ξt, a) = zt − √ (5)<br>√α¯ t<br><!-- End of picture text -->

attempts to directly estimate z0 from the current noisy latent zt, while 



<!-- Start of picture text -->
g(zt, ξt, a) = � 1 − α¯t−1ϵθ(zt, ξt, a) (6)<br><!-- End of picture text -->

ensures that the trajectory toward z0 follows the direction pointing to zt. The deterministic nature of DDIM allows to skip intermediate denoising steps and perform only Ts ≪ T iterations of the reverse process, thereby enabling faster inference. 

## 2.2 Conditioning 

We aim to condition ϵθ on continuous musical attributes a ∈ R. Similarly, Chen et al. [28] found it beneficial to 

53 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

|(%)|Contour|Note Density|Pitch Range|Complexity|
|---|---|---|---|---|
|NM|63.36|76.63|46.70|48.67|
|P&L|37.44|10.11|0.41|50.59|
|LC-VAE-A|60.88|97.56|34.69|33.32|
|LC-VAE-SE|52.02|97.33|36.84|52.00|
|LC-Diff|85.60|98.59|80.97|94.93|



Table 1: Pearson Correlation Coefficient (PCC) between target and decoded attributes. 

condition on the noise level instead of the discrete diffusion step, which [7] later adopted for LDM-based symbolic music generation. Thus, we are left with two continuous conditioning signals to be passed onto the diffusion model. 

We inject a and<sup><mark>√</mark></sup> <mark>α¯</mark> t <mark>i</mark> nto ϵθ through dedicated networks (see Figure 1). First, we apply Sinusoidal Encoding (SE) based on Transformer positional embeddings [29] 



<!-- Start of picture text -->
Γ(u) = � sin (ωi(u)) , cos (ωi(u)) �d/i=02 (7)<br><!-- End of picture text -->

where ωi(u) = <mark>s</mark> b<sup>2</sup> <mark>u</mark><sup>i/d[7],withd∈Nthe(even)dimen-</sup> sionality of the embedding, b ∈ R the base frequency, and s ∈ R a frequency scaling hyperparameter. The resulting SE features are passed through a linear layer with SiLU activations. Finally, we employ Feature-wise Linear Modulation (FiLM) [30], where two fully-connected layers yield shifts and scales, respectively, that modulate the activations of the denoiser (see Figure 2). The two conditioning branches run in parallel. This is equivalent to learning a single affine transformation, where scale and shift are the sum of FiLM outputs from the attribute and noise level conditioning networks. 

To enhance controllability over the generated samples, we also apply Classifier-Free Guidance (CFG) [31] to the noise prediction: 



<!-- Start of picture text -->
ϵˆθ(zt, ξt, a) = (1 + w)ϵθ(zt, ξt, a) − wϵθ(zt, ξt), (8)<br><!-- End of picture text -->

where ϵθ(zt, ξt) is the unconditional noise prediction and w ∈ R≥0 is the guidance scale. To make CFG effective, the model must learn to predict noise both with and without attribute conditioning. We achieve this through conditioning dropout (depicted as 0/1 in Figure 1), i.e., setting the outputs of the attribute conditioning network to zero with a certain probability when evaluating (3). 

## 3. EVALUATION 

## 3.1 Dataset 

The models are designed to learn pitch sequence representations from four-bar monophonic melodies. We construct a large-scale dataset comprising melodies extracted from 176,581 MIDI files from the Lakh MIDI Dataset [32].<sup>1</sup> 

First, we assess whether each MIDI file contains time signature changes. If any are found, we segment the file and retain only sections with a 4/4 time signature. Each MIDI event is then quantized to the nearest sixteenth note. 

A melody is defined as a sequence of pitches within the standard 88-key piano range, played by an instrument 

> 1 C. Raffel, 2016, “The Lakh MIDI Dataset v0.1.” [Online]. Available: `https://colinraffel.com/projects/lmd` 

||Contour|Note Density|Pitch Range|Complexity|
|---|---|---|---|---|
|Uncond. VAE||4|1.44||
|NM|35.506|58.436|30.833|47.61|
|P&L|49.698|67.836|40.657|87.80|
|LC-VAE-A|30.197|29.450|30.257|32.435|
|LC-VAE-SE|29.161|30.124|31.274|30.166|
|LC-Diff|19.299|20.559|31.695|17.51|



Table 2: Fréchet Music Distance [27]. 

mapped to a valid MIDI program. A melody is considered complete when a full measure of silence occurs. We extract only melodies spanning at least four bars and comprising at least three distinct pitches. If multiple notes sound simultaneously, we follow the approach proposed in [33] and select only the highest-pitched note to ensure monophonic sequences. Subsequently, four-bar segments are extracted using a stride of one bar. 

For each melody thus extracted, we compute 13 musical attributes, including those outlined in Section 3.2. 

Melodies are encoded as sequences of N = 64 integers in P = {0, . . . , 129}, where each element represents either a MIDI note number (0-127) or one of two special tokens: note off (128) and note hold (129). The dataset is divided into training, validation, and test sets, with training data augmented through transposition by a randomly selected number of semitones within a range of ±1 octave. The final dataset, consisting of 10,126,676 unique melodies, is publicly available.<sup>2</sup> 

## 3.2 Musical Attributes 

As previously done in [25], we focus on four musical attributes: (i) Contour, which quantifies the melodic movement in a sequence, measured by averaging the pitch differences between consecutive notes; (ii) Note Density, defined as the ratio between the number of notes in the melody and the sequence length. It takes values in [0, 1]; (iii) Pitch Range, defined as the difference between the highest and lowest MIDI pitch values in the sequence, normalized by the range of an 88-key piano. It takes values in �0,<sup><mark>127</mark></sup> 88 <mark>�</mark> , where values above one indicate a range exceeding A0–C8; (iv) Rhythm Complexity, evaluated using Toussaint’s metrical complexity measure [34], corrected for the total number of notes in the sequence [26]. By definition, it takes on discrete values. 

## 3.3 Unconditional Generative Model 

As base unconditional model, we implement a β-VAE [35] based on MusicVAE [33]. This model, previously used in LDM-based symbolic music generation [7], also enables direct comparison with existing attribute-regularized VAEs (AR-VAEs) employing the same architecture [25, 26] (see Section 3.5). 

The encoder pψ(z|x) consists of a two-layer bidirectional LSTM network fed with four-bar pitch sequence representations (see Section 3.1), followed by two linear lay- 

> 2 M. Pettenò, Aug. 2024, “4 Bars Monophonic Melodies Dataset (Pitch Sequence),” Zenodo, doi: `https://doi.org/10.5281/zenodo .13369389` 

54 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
20 20 10 10<br>nn nno<br>10 10<br>2<br>(a) NM (b) P&L (c) LC-VAE-A (d) LC-VAE-SE<br><!-- End of picture text -->

Figure 3: Regression plots comparing target and decoded Contour attributes across baseline methods. 



<!-- Start of picture text -->
10<br>2<br><!-- End of picture text -->

Figure 4: Regression plot comparing target and decoded Contour attributes using LC-Diff. 

ers parameterizing the latent posterior. The hierarchical decoder qϕ(x|z) features two unidirectional LSTMs, with the bottom-level network autoregressively estimating the distribution over the sequence values via a softmax nonlinearity [33]. As such, each pitch sequence x ∈ P<sup>N</sup> is first mapped onto a single latent code z ∈ R<sup>M</sup> , M = 256, and since decoding amounts to a next token prediction task, the standard β-VAE objective [35] 



<!-- Start of picture text -->
LVAE = −Epψ(z|x) [log qϕ(x|z)] + βDKL [pψ(z|x) ∥ p(z)] ,<br>(9)<br><!-- End of picture text -->

is implemented using cross-entropy as reconstruction loss. The unconditional model is trained for 40,000 iterations on a single NVIDIA Titan RTX GPU with a batch size of 512. The objective (9) is minimized using Adam, and the learning rate is decreased exponentially from 10<sup>−3</sup> to 10<sup>−5</sup> with a rate of 0.9999. The hyperparameter β is annealed exponentially from 0 to 10<sup>−3</sup> , which encourages the model to prioritize accurate sequence reconstruction during the early part of the training. Similarly to [33], we apply teacher forcing within the bottom-level decoder with a probability following a logistic schedule. 

## 3.4 Conditional Diffusion Model 

With latent codes being vectors in R<sup>M</sup> , we implement a DDIM model with a fully-connected denoiser network.<sup>3</sup> Shown in Figure 2, the denoiser comprises an input layer with 2048 linear units, followed by three dense residual blocks. Each residual block comprises two stacks of LayerNorm, feature-wise modulation (responsible for joint attribute and time conditioning), SiLU, and a linear layer, plus a residual connection that shortcuts the input and output of the block. Finally, the output is linearly projected back onto R<sup>M</sup> . 

> 3 Source code and audio examples are available at `https://mpet teno.github.io/controllable-latent-diffusion/` 

We set the SE dimensionality to d = 128. The attribute and noise level conditioning networks have 512 and 2048 units in the first linear layer and FiLM layers, respectively. 

In the forward process, βt follows a linear schedule from 10<sup>−6</sup> to 10<sup>−2</sup> over T = 1000 steps. Conversely, the number of sampling steps is set to Ts = 100. 

We train the model with an attribute conditioning dropout probability of 20%. We then apply CFG with a guidance scale of w = 3.0 [31]. In our experiments, CFG proved fundamental to achieve attribute regularization. 

The resulting denoiser network has 43.1 million parameters, and converges in just about 20 training epochs, half the iterations required by the unconditional model. 

## 3.5 AR-VAE Baseline Methods 

For comparison, we consider AR-VAEs [25, 26] with the same architecture as the unconditional model described in Section 3.3. AR-VAEs incorporate regularization during training by means of a supervised multi-task learning approach, with the goal of encoding the attribute a in the i-th dimension zi of their latent spaces. This is achieved by including an AR loss term in (9) 



<!-- Start of picture text -->
LAR-VAE = LVAE + γLAR, (10)<br><!-- End of picture text -->

where γ ≥ 0 is a tunable hyperparameter controlling the strength of the regularization. 

Mezza et al. [26] propose the use of 



<!-- Start of picture text -->
L NM AR = MAE(zi, a˜), (11)<br><!-- End of picture text -->

where MAE(·, ·) denotes the mean absolute error, and ˜a is the z-score of a. 

Pati and Lerch [25] introduced a regularization term that enforces a monotonic relationship between a and zi, i.e., 



<!-- Start of picture text -->
L P&L AR = MAE (tanh(δ Dz), sign(Da)) , (12)<br><!-- End of picture text -->

where Dz and Da are pairwise distance matrices between zi and a of all samples in a batch, respectively, and δ > 0 is a tunable hyperparameter. As in [25], we set γ = 1 and δ = 10. The remaining training details are the same as in Section 3.3. For brevity, we will later refer to the former AR method as “NM” and to the latter as “P&L.” 

## 3.6 LC-VAE Baseline Methods 

Similarly to Tian and Engel [3], we implement LC through a conditional VAE (cVAE) trained on the representations of 

55 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
40<br>40 40<br>20 20 20 20<br>10 20 30 40 0 10 20 30 40 10 20 30 40 10 20 30 40<br>(a) NM (b) P&L (c) LC-VAE-A (d) LC-VAE-SE<br><!-- End of picture text -->

Figure 5: Regression plots comparing target and decoded Rhythm Complexity attributes across baseline methods. 



<!-- Start of picture text -->
60<br>40<br>20<br>10 20 30 40<br>a<br><!-- End of picture text -->

Figure 6: Regression plot comparing target and decoded Rhythm Complexity attributes using LC-Diff. 

the base unconditional model (Section 3.3). The cVAE encoder consists of four linear layers with ReLU activations, followed by two Gating Mixing Layers (GML) that parameterize the innermost latent distribution. The decoder mirrors the encoder with four linear layers with ReLU activations, followed by an output GML. Except for using 2048 units in the fully-connected layers and M<sup>′</sup> = 128 latent variables, the cVAE architecture is the same as in [3]. 

Let z ∈ R<sup>M</sup> be the latent representations of the unconditional model, zc ∈ R<sup>M ′</sup> be the latent representations of the cVAE, and a ∈ R the sequence attribute. The authors of [3] considered binary labels and one-hot vectors were thus concatenated with z and zc. Instead, we deal with continuous attributes. We implement two cVAE variants that differ in how a is fed into the networks. In the first variant, later referred to as LC-VAE-A, we feed ˜z = [z<sup>T</sup> , a]<sup>T</sup> to the encoder, and z˜c = [z<sup>T</sup> c<sup>, a]Tto the decoder.In the second</sup> variant, named LC-VAE-SE, we concatenate z and zc, respectively, with the attribute SE, i.e., ˜z = [z<sup>T</sup> , Γ(a)]<sup>T</sup> and z˜c = [z<sup>T</sup> c<sup>, Γ(a)]T .</sup> 

## 4. RESULTS 

## 4.1 Attribute-Controlled Generation 

To evaluate the controllability of the generative models under scrutiny, we sample the target attributes uniformly in the range of zero to the 99th percentile of the attribute distribution of the sequences in the test set.<sup>4</sup> These equallyspaced values, which we refer to as target attributes, are fed to the respective conditioning network of LC-Diff, suitably transformed and plugged into the regularized dimen- 

> 4 Limiting the range to the 99th percentile is meant to exclude those sequences with abnormally high attribute values. We argue that these sequences are spurious, and we attribute their existence to the choice, borrowed from [33], of extracting melodies by naïvely picking the highest note at any given time. 

sion zi of the AR-VAEs, and concatenated to the input vector of the LC-VAE decoder networks. 

Table 1 lists the Pearson Correlation Coefficients (PCC) between the target attributes and those computed from the generated sequences (the higher, the better). LC-Diff consistently outperforms the two AR-VAEs (NM and P&L) and LC-VAEs (both with and without SE) for all attributes considered. Notably, LC-Diff is the only method among those considered in the present study to yield correlation scores higher than 80% across the board. 

As for Contour, LC-Diff achieves a PCC of 85.60%, outperforming the next-best model, NM, by over 22%. The difference is less pronounced for Note Density, where LCDiff (98.56%) improves upon the second-best model by just 1%. Nonetheless, LC-VAE-A and LC-VAE-SE already achieve 97.56% and 97.33%, respectively, suggesting that constraining the generative model is very effective compared to AR methods when it comes to rendering the desired number of notes. LC-Diff also demonstrates significant improvements in Pitch Range and Rhythm Complexity. For Pitch Range, it achieves a PCC of 80.97%, exceeding NM (46.70%) by 34.27%, while NM itself outperforms LC-VAEs by approximately 10%. For Rhythm Complexity, LC-Diff achieves a remarkable 94.93%, surpassing LC-VAE-SE (52%) by 42.93%. 

Concerning AR models, while NM directly encodes the (standardized) distribution onto the ith dimension of the latent space, there is no a priori way to know the monotonic relationship learned using the P&L regularization in (12). This explains the near-zero correlation observed for Pitch Range, and, in general, the overall lower PCC. 

Figures 3 through 6 show the regression plots of Contour and Rhythm Complexity. Figure 3 and Figure 4 illustrate the case of a continuous distribution, while Figure 5 and Figure 6 exemplify a case where the attribute takes on integer values. Across both attributes, LC-Diff is characterized by a lower spread and a clear linear trend. In Figure 3, all baseline models show a tendency to produce excessively high contour values, whereas LC-Diff (Figure 4) appears to mitigate the issue. Likewise, Figure 5 reveals that all models but LC-Diff (Figure 6) tend to fail when the target Complexity values are low. 

## 4.2 Data Fidelity 

To evaluate the quality of the generated sequences, we use the Fréchet Music Distance (FMD) [27], a metric that extends the family of Fréchet Inception Distance [36] and 

56 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
C5 C5 C5<br>C4 C4 C4<br>Note Note Note<br>C3 C3 C3<br>C2 C2 C2<br>C10 1 2 3 4 5 9 1 C10 1 2 3 4 5 9 7 C10 1 2 3 4 5 6 7<br>Time Time Time<br>(a) a = 1.0 → ag = 1.03 (b) a = 3.0 → ag = 2.95 (c) a = 6.0 → ag = 6.19<br><!-- End of picture text -->

Figure 7: Examples of MIDI files generated by controlling the Contour attribute with LC-Diff. 



<!-- Start of picture text -->
C5 C5 C5<br>C4 C4 C4<br>NoteC3 NoteC3 NoteC3<br>C2 C2 C2<br>C1 C1 C1<br>0 1 2 3 5 9 7 0 1 2 3 4 9 0 1 2 3 4 5 9 7<br>Time Time Time<br>(a) a = 0 → ag = 0 (b) a = 15 → ag = 15 (c) a = 33 → ag = 33<br><!-- End of picture text -->

Figure 8: Examples of MIDI files generated by controlling Rhythm Complexity with LC-Diff. Quarter notes are indicated by solid vertical lines; odd pulses (strong) are indicated by dashed lines; even pulses (weak) are indicated by dotted lines. 

Fréchet Audio Distance [37] to the symbolic music domain. FMD was computed between 22,016 melodies from the held-out test set and an equal number of generated sequences. To prevent the FMD from measuring a spurious divergence from the real attribute distribution, we condition the generation on the attributes of the reference sequences, rather than using evenly-spaced control values as in Section 4.1. By conditioning with attributes measured from the test set, indeed, we aim to simultaneously compare the fidelity of generated sequences and how well they conform to the desired attribute distribution. 

Table 2 reports the results obtained using CLaMP 2 MIDI embeddings [38] (the lower, the better). For comparison, we report the FMD between the reference test set and the output of the unconditional VAE (see Section 3.3) obtained by decoding 22,016 samples from N (0, I). 

The results presented in Table 2 demonstrate that the proposed LC-Diff model consistently achieves the lowest FMD values across most attributes, indicating superior performance in generating samples that aligns more closely with the statistical properties of real sequences. Notably, LC-Diff outperforms all baselines in Contour (19.299), Note Density (20.559), and Rhythm Complexity (17.51), significantly improving over both AR-VAEs and LCVAEs. While LC-VAE-A achieves the best Pitch Range score (30.257), LC-Diff remains competitive (31.695). 

Overall, all LC methods outperform the unconditional base model (41.44), showing that introducing post-hoc control leads to more consistent and structured music generation, with better alignment to the desired attributes. 

Finally, Figure 7 and Figure 8 illustrate the potential diversity in the generated samples produced by LC-Diff when conditioned on low, medium, and high values of Contour and Rhythm Complexity, respectively. 

## 5. CONCLUSIONS 

In this paper, we have explored latent diffusion through the lens of Latent Constraints (LC), demonstrating the efficacy of DDIMs as plug-and-play conditioning modules for symbolic music generation. By keeping the base generative model fixed, we trained diffusion-based LC models (LCDiff) capable of controlling a range of non-differentiable and continuous musical attributes, including contour, note density, pitch range, and rhythm complexity. Our empirical evaluations reveal that LC-Diff significantly outperforms attribute-regularized VAEs and cVAE-based LC methods in terms of both fidelity and controllability, with absolute improvements of up to 12.65 in Fréchet Music Distance and 43% in correlation between desired and generated attributes. These results highlight the potential of denoising as a powerful tool for ad hoc fader-like control over multiple musical attributes along continuous axes, effectively transforming a pre-trained unconditional model into a controllable music generation system depending on the user’s needs. Future work will focus on expanding the library of LC-Diff models to include a wider range of musical attributes and exploring the integration of user interfaces for real-time control. Future experiments could also explore attribute-controlled input transformations by applying forward diffusion to encoded representations, rather than drawing noise samples from the standard normal prior. Furthermore, we aim to investigate the potential for LC of other generative techniques, such as flow matching and consistency models. 

## 6. REFERENCES 

[1] J. Engel, M. Hoffman, and A. Roberts, “Latent constraints: Learning to generate conditionally from un- 

57 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

   - conditional generative models,” in International Conference on Learning Representations, 2018. 

- [2] M. Dinculescu, J. Engel, and A. Roberts, “MidiMe: Personalizing a MusicVAE model with user data,” in NeurIPS Workshop on Machine Learning for Creativity and Design, 2019. 

- [3] Y. Tian and J. Engel, “Latent translation: Crossing modalities by bridging generative models,” arXiv preprint arXiv:1902.08261, 2019. 

- [4] R. Rombach, A. Blattmann, D. Lorenz, P. Esser, and B. Ommer, “High-resolution image synthesis with latent diffusion models,” in Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, 2022, pp. 10 684–10 695. 

- [5] S. Wu and M. Sun, “Exploring the efficacy of pretrained checkpoints in text-to-music generation task,” in The AAAI-23 Workshop on Creative AI Across Modalities, 2023. 

- [6] P. Jajoria and J. McDermott, “Text conditioned symbolic drumbeat generation using latent diffusion models,” arXiv preprint arXiv:2408.02711, 2024. 

- [7] G. Mittal, J. Engel, C. Hawthorne, and I. Simon, “Symbolic music generation with diffusion models,” in Proc. of the 22nd International Society for Music Information Retrieval Conference (ISMIR), 2021, pp. 468–475. 

- [8] M. Pasini, M. Grachten, and S. Lattner, “Bass accompaniment generation via latent diffusion,” in ICASSP 2024-2024 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2024, pp. 1166–1170. 

- [9] S. Li and Y. Sung, “MelodyDiffusion: Chordconditioned melody generation using a transformerbased diffusion model,” Mathematics, vol. 11, no. 8, 2023. 

- [10] L. Min, J. Jiang, G. Xia, and J. Zhao, “Polyffusion: A diffusion model for polyphonic score generation with internal and external controls,” in Proc. of the 24th International Society for Music Information Retrieval Conference (ISMIR), 2023, pp. 231–238. 

- [11] L. Kawai, P. Esling, and T. Harada, “Attributes-aware deep music transformation.” in Proc. of the 21st International Society for Music Information Retrieval Conference (ISMIR), 2020, pp. 670–677. 

- [12] S.-L. Wu and Y.-H. Yang, “MuseMorphose: Full-song and fine-grained piano music style transfer with one transformer VAE,” IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 31, pp. 1953– 1967, 2023. 

- [13] M. E. Malandro, “Composer’s Assistant 2: Interactive multi-track MIDI infilling with fine-grained user control,” in Proc. of the 25th International Society for Music Information Retrieval Conference (ISMIR), 2024, pp. 438–445. 

- [14] G. Lample, N. Zeghidour, N. Usunier, A. Bordes, L. Denoyer, and M. Ranzato, “Fader networks: Manipulating images by sliding attributes,” in Advances in Neural Information Processing Systems, 2017, pp. 5963–5972. 

- [15] H. H. Tan and D. Herremans, “Music FaderNets: Controllable music generation based on high-level features via low-level feature modelling,” in Proc. of the 21st International Society for Music Information Retrieval Conference (ISMIR), 2020, pp. 109–116. 

- [16] J. Ho, A. Jain, and P. Abbeel, “Denoising diffusion probabilistic models,” in Proc. of the 34th International Conference on Neural Information Processing Systems, 2020, pp. 1–12. 

- [17] J. Song, C. Meng, and S. Ermon, “Denoising diffusion implicit models,” in International Conference on Learning Representations, 2021. 

- [18] J. Austin, D. D. Johnson, J. Ho, D. Tarlow, and R. van den Berg, “Structured denoising diffusion models in discrete state-spaces,” in Advances in Neural Information Processing Systems, 2021, pp. 1–13. 

- [19] A. Lv, X. Tan, P. Lu, W. Ye, S. Zhang, J. Bian, and R. Yan, “GETMusic: Generating any music tracks with a unified representation and diffusion framework,” arXiv preprint arXiv:2305.10841, 2023. 

- [20] M. Plasser, S. Peter, and G. Widmer, “Discrete diffusion probabilistic models for symbolic music generation,” in Proc. of the Thirty-Second International Joint Conference on Artificial Intelligence, 2023. 

- [21] J. Zhang, G. Fazekas, and C. Saitis, “Composer stylespecific symbolic music generation using vector quantized discrete diffusion models,” in 2024 IEEE 34th International Workshop on Machine Learning for Signal Processing (MLSP), 2024, pp. 1–6. 

- [22] ——, “Fast diffusion GAN model for symbolic music generation controlled by emotions,” arXiv preprint arXiv:2310.14040, 2023. 

- [23] M. Zhang, L. J. Ferris, L. Yue, and M. Xu, “Emotionally guided symbolic music generation using diffusion models: The AGE-DM approach,” in Proc. of the 6th ACM International Conference on Multimedia in Asia, 2024, pp. 1–5. 

- [24] Y. Huang, A. Ghatare, Y. Liu, Z. Hu, Q. Zhang, C. S. Sastry, S. Gururani, S. Oore, and Y. Yue, “Symbolic music generation with non-differentiable rule guided diffusion,” arXiv preprint arXiv:2402.14285, 2024. 

- [25] A. Pati and A. Lerch, “Attribute-based regularization of latent spaces for variational auto-encoders,” Neural Computing and Applications, vol. 33, no. 9, pp. 4429– 4444, 2021. 

58 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [26] A. I. Mezza, M. Zanoni, and A. Sarti, “A latent rhythm complexity model for attribute-controlled drum pattern generation,” EURASIP Journal on Audio, Speech, and Music Processing, vol. 2023, no. 1, 2023. 

- [27] J. Retkowski, J. Ste¸pniak, and M. Modrzejewski, “Frechet music distance: A metric for generative symbolic music evaluation,” arXiv preprint arXiv:2412.07948, 2024. 

- [28] N. Chen, Y. Zhang, H. Zen, R. J. Weiss, M. Norouzi, and W. Chan, “WaveGrad: Estimating gradients for waveform generation,” in International Conference on Learning Representations, 2021. 

- [29] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. u. Kaiser, and I. Polosukhin, “Attention is all you need,” in Advances in Neural Information Processing Systems, vol. 30, 2017. 

- [30] E. Perez, F. Strub, H. de Vries, V. Dumoulin, and A. C. Courville, “FiLM: Visual reasoning with a general conditioning layer,” in Proc. of the Thirty-Second AAAI Conference on Artificial Intelligence, 2018, pp. 3942– 3951. 

- [31] J. Ho and T. Salimans, “Classifier-free diffusion guidance,” in NeurIPS 2021 Workshop on Deep Generative Models and Downstream Applications, 2021. 

- [32] C. Raffel, “Learning-based methods for comparing sequences, with applications to audio-to-midi alignment and matching,” Ph.D. dissertation, Columbia University, 2016. 

- [33] A. Roberts, J. Engel, C. Raffel, C. Hawthorne, and D. Eck, “A hierarchical latent vector model for learning long-term structure in music,” in Proc. of the 35th International Conference on Machine Learning, 2018, pp. 4364–4373. 

- [34] G. Toussaint, “A mathematical analysis of African, Brazilian, and Cuban clave rhythms,” in Bridges: Mathematical Connections in Art, Music, and Science, 2002, pp. 157–168. 

- [35] I. Higgins, L. Matthey, A. Pal, C. P. Burgess, X. Glorot, M. M. Botvinick, S. Mohamed, and A. Lerchner, “beta-VAE: Learning basic visual concepts with a constrained variational framework.” International Conference on Learning Representations, vol. 3, 2017. 

- [36] M. Heusel, H. Ramsauer, T. Unterthiner, B. Nessler, and S. Hochreiter, “GANs trained by a two time-scale update rule converge to a local Nash equilibrium,” in Proc. of the 31st International Conference on Neural Information Processing Systems, 2017, pp. 6629–6640. 

- [37] K. Kilgour, M. Zuluaga, D. Roblek, and M. Sharifi, “Fréchet audio distance: A reference-free metric for evaluating music enhancement algorithms,” in Proc. Interspeech 2019, 2019, pp. 2350–2354. 

- [38] S. Wu, Y. Wang, R. Yuan, Z. Guo, X. Tan, G. Zhang, M. Zhou, J. Chen, X. Mu, Y. Gao, Y. Dong, J. Liu, X. Li, F. Yu, and M. Sun, “CLaMP 2: Multimodal music information retrieval across 101 languages using large language models,” arXiv preprint arXiv:2410.13267, 2025. 

59 

