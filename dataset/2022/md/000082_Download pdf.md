---
paper_id: "000082"
year: 2022
title: "Download pdf"
source_url: "https://zenodo.org/record/7316754/files/000082.pdf"
---

# **A DIFFUSION-INSPIRED TRAINING STRATEGY FOR SINGING VOICE EXTRACTION IN THE WAVEFORM DOMAIN** 

**Genís Plaja-Roglans Marius Miron Xavier Serra** 

Music Technology Group, Universitat Pompeu Fabra, Barcelona, Spain 

{genis.plaja, marius.miron, xavier.serra}@upf.edu 

## **ABSTRACT** 

Notable progress in music source separation has been achieved using multi-branch networks that operate on both temporal and spectral domains. However, such networks tend to be complex and heavy-weighted. In this work, we tackle the task of singing voice extraction from polyphonic music signals in an end-to-end manner using an approach inspired by the training and sampling process of denoising diffusion models. We perform unconditional signal modelling to gradually convert an input mixture signal to the corresponding singing voice or accompaniment. We use fewer parameters than the state-of-the-art models while operating on the waveform domain, bypassing the phase estimation problem. More concisely, we train a non-causal WaveNet using a diffusion-inspired strategy while improving the said network for singing voice extraction and obtaining performance comparable to the end-to-end stateof-the-art on MUSDB18. We further report results on a non-MUSDB-overlapping version of MedleyDB and the multi-track audio of Saraga Carnatic showing good generalization, and run perceptual tests of our approach. Code, models, and audio examples are made available.<sup>1</sup> 

## **1. INTRODUCTION** 

Singing voice extraction, which involves separating the vocal source from music recording mixtures, has received a lot of attention from the Audio Signal Processing (ASP) and Music Information Retrieval (MIR) communities in the recent years. The problem can be modelled in the waveform domain [1–4], the frequency domain [5–7], or a combination of both [8–10]. In general, spectrogrambased approaches have been more popular despite having to deal with the problem of the complex phase, usually leading to artifacts or unnaturalness of the separated sources. Within the Music Demixing Challenge (MDX) framed in ISMIR 2021 [11], diverse submissions achieved state-of-the-art source separation performance, in the majority of cases being multi-branch networks combining 

> 1 github.com/genisplaja/diffusion-vocal-sep 

> © G. Plaja-Roglans, M. Miron, and X. Serra. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). **Attribution:** G. Plaja-Roglans, M. Miron, and X. Serra, “A diffusion-inspired training strategy for singing voice extraction in the waveform domain”, in _Proc. of the 23rd Int. Society for Music Information Retrieval Conf.,_ Bengaluru, India, 2022. 

features from both time and frequency domains [8–10], proposing therefore solutions to account for the problem with the phase. Nonetheless, these models tend to be heavy-weighted and include engineered strategies to improve the predicted outputs. 

While the problem of source separation has been shown to be challenging on the waveform domain, promising results have been reported [2,3,12], opening the door for the development of models that bypass the problem with the complex phase. However, as the performance improves, the model size and complexity accordingly grow. 

In this work we propose a training and sampling strategy inspired on the recently emerged denoising diffusion models [13] to perform end-to-end singing voice extraction. Denoising diffusion models are a novel class of generative models theoretically grounded in the nonequilibrium statistical physics that can gradually convert one distribution into another using a Markov chain [14], while learning to perform the reverse process. More concisely, numerous works use diffusion models to convert a signal from a particular data distribution to a simple one (e.g. isotropic Gaussian noise) by gradually adding samples of the said simple distribution. Subsequently, the model is trained to reverse the perturbation process and generate data samples of the original distribution using the easily tractable noise as input [15–17]. Diffusion models have recently emerged as a versatile and high-performance method for data generation, outperforming classical generative approaches for the task of image generation [13]. In the fields of ASP and MIR, diffusion models have also shown promising performance for speech synthesis [16,18], speech restoration and enhancement [13, 15, 19–21], audio super-resolution [22], singing voice synthesis [23], and symbolic music generation [24]. Despite that, the literature does not include many attempts to use diffusion models for source separation, being [25], to the best of our knowledge, the only attempt. 

Despite the use of deterministic signals as diffusion perturbation in place of Gaussian noise has shown promising results in reverting different arbitrary types of image noise and performing image morphing [26], to the best of our knowledge, no exploration of this idea in the audio domain has been reported to date. In this work, we build on top of DiffWave, a versatile diffusion model for speech synthesis [16] that is based on a non-causal WaveNet architecture that has been previously used for music source separation [12]. We introduce an end-to-end approach to model 

685 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

the task of singing voice extraction as a diffusion-alike process, by converting between two audio data distributions that share similar content, in this case the singing voice and the corresponding mixture. We propose to use a deterministic diffusion perturbation, a music mixture, to gradually transform its corresponding isolated singing voice into the mixture while learning to conduct the reverse process at inference. Given the formulation of the diffusion process, we train a model that learns to estimate the perturbation at different ratios. Subsequently, we leverage from the parametrization of the reverse process of diffusion models to chain these estimations and sample, given an input mixture, improved vocal source separation in terms of artifacts and interferences compared to the vanilla trained network. 

## **2. METHOD** 

## **2.1 Diffusion process** 

We assume that the waveform-domain signal corresponding to the mixture _m_ is the sum of the singing voice _v_ and the accompaniment _a_ , such as: _m_ = _v_ + _a_ . Our goal is to estimate _v_ given _m_ . In the following sections we formalize our method by relating it with the diffusion theory in the literature. In Figure 1 we display the two main steps of our method: the diffusion and the reverse process. 

**Diffusion.** The diffusion process assumes perturbing the training data with different scales of noise iteratively following a Markov chain [13]: 



<!-- Start of picture text -->
T<br>q ( x 1 , ..., xT |x 0) = q ( xt|xt− 1) (1)<br>t =1<br><!-- End of picture text -->

The input signal _x_ 0 is gradually perturbed by incrementally adding a particular signal in small _T_ diffusion steps. This process results into a latent variable _xT_ of same distribution of the perturbation. The standard diffusion schema, introduced in [13] and subsequently used in most of the diffusion research, perturbs _x_ 0 with random Gaussian noise, therefore _xT_ is an isotropic Gaussian noise distribution. In our case, the input signal _x_ 0 is initialized with the isolated singing voice _v_ , and perturbed by incrementally adding the mixture _m_ . This results in _xT_ being a mixture-alike signal, containing both voice and accompaniment. Therefore, _q_ ( _xt|xt−_ 1) in Eq. 1 is an operation to add a small amount of perturbation _m_ to the given signal _xt−_ 1, moving to the next diffusion step _xt_ . We use _m_ as perturbation to account for the formal diffusion design in [13], in which the latent variable _xT_ is expected to belong to the same data distribution as the perturbing noise. The level of perturbation at each diffusion step is controlled by _βt_ , which is a small positive coefficient within a fixed noise schedule denoted _β_ . That said, using the parametrization proposed in [13], we can compute any given diffusion step using: 



<!-- Start of picture text -->
q ( xt|x 0) = √ α ¯ tx 0 + √ 1  − α ¯ tm (2)<br><!-- End of picture text -->

where _αt_ = 1 _− βt_ and _α_ ¯ _t_ = ⅡI _ts_ =1<sup>_αs_.Note also that the</sup> most common inference input of a singing voice extraction model – which in our case is _xT_ – is a mixture. Given 



<!-- Start of picture text -->
价 -DIFFUSION<br>x1 XT-1<br>价<br>x� u≈ ⊥x<br>-REVERSE-<br><!-- End of picture text -->

**Figure 1** . Overview of our diffusion-inspired training approach for the case of singing voice extraction. 

Eq. 2, the perturbation is a mixture _m_ to ensure _xT ≈ m_ , otherwise the said condition may not be given. 

Modelling musical signals using a mixture of Gaussian functions has been previously explored in [27]. Note also that architectures similar to DiffWave have been already used to model mixture, accompaniment, and vocal signals [12,28] (for further detail see Section 2.2). 

**Reverse process.** The reverse process aims at iteratively reverting the perturbation added by the diffusion: 



<!-- Start of picture text -->
T<br>pθ ( x 0 , ..., xT − 1 |m ) = Ⅱ pθ ( xt− 1 |xt ) (3)<br>t =1<br><!-- End of picture text -->

We propose to parameterize the variable _pθ_ ( _xt−_ 1 _|xt_ ) as <u>1</u> _−αt_ <u>1</u> _xt −_ _~~√~~_ 1 _−α_ ¯ _t_<sup>_ϵ_(</sup><sup>_xt, t_)</sup> _~~√~~_ _<u>αt</u>_<sup>, being</sup><sup>_ϵ_(</sup><sup>_xt, t_) the perturbation</sup> estimated by the model at a given diffusion step _t_ . This parametrization is leveraged from the diffusion sampling process in [13]. However, we remove the deviation parameter from the original parametrization, which in our deterministic noise case yields worse predictions. This process can be seen as an iterative refinement of the latent variable _xT_ to convert it to _x_ 0, in our case to iteratively transform an input mixture to its corresponding singing voice source. **Training.** The training objective of the original diffusion process is to maximize the log likelihood of: _pθ_ ( _x_ 0) = _pθ_ ( _x_ 0 _, ..., xT −_ 1 _|xT_ ) _platent_ ( _xT_ ) _dx_ 1: _T_ [13], considering stochastic noise as perturbation. Since in this context it is not possible to calculate the said integral, in the literature this problem is approached by maximizing its variational lower bound (ELBO) [13]. The reader is referred to [16], for a detailed development of this maximization. In our case, relying on the ELBO is not required given the deterministic perturbation. Therefore, by using pairs of ( _xt, x_ 0) [13], and referring to Eq. 2, we are able to effectively optimize the model with parameters _θ_ using the following objective [13]: 



<!-- Start of picture text -->
L ( θ ) = ϵ − ϵθ ( √ α ¯ tx 0 + √ 1  − α ¯ tm, t )) 2 (4)<br><!-- End of picture text -->

where _ϵ_ is the target or true perturbation, whereas _ϵθ_ is the perturbation the model estimates based on _α, t_ ¯ , the mixture _m_ and the input _x_ 0. In the case of extracting the singing voice, we use the accompaniment _a_ instead of mixture _m_ as the target corresponding to _ϵ_ . Therefore, we do not include the voice into the target of the training process, thus we alleviate the loss of vocal quality that may occur after several reverse steps. 

686 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

**Noise schedule.** Choosing the noise schedule _β_ has been found to be crucial for the performance of diffusion models [13]<sup>2</sup> and in fact, efforts have been done to learn said variable instead of defining it manually [29]. In our scenario, we require a schedule _β_ that accounts for the proposed diffusion-inspired approach, in which _x_ 0 is expected to be predominant in the completely perturbed signal _xT_ . Moreover, our perturbation _m_ is the mixture corresponding to _x_ 0, thus _x_ 0 is contained in the perturbation, which may lead to an abnormally over-loud source in the completely diffused _xT_ . Ultimately, the inference input is a mixture, therefore we propose to use a schedule that produces a latent variable _xT_ as close as possible to an actual mixture. 

Our noise schedule is defined by _β_ 0 = 1<sup>_−_4</sup> , _βT_ = 0 _._ 2, and _T_ = 20, being 20 a reliable option for audio as found in [16]. This noise schedule produces _q_ ( _xT |x_ 0) _≈ m_ , and we denote it _β_ 20. Note that the closer _βT_ to 1, we should expect a more aggressive transformation, leading to less interference at the expense of losing quality of the estimated source. Recent diffusion-based works in the audio domain successfully model their task using 4–8 steps [21]. To study the effect of the number of diffusion steps and explore the feasibility of modelling the task with less computational expense, we experiment with a new schedule _β_ 8, which is defined by _β_ 0 = 1<sup>_−_4</sup> , _βT_ = 0 _._ 5, and _T_ = 8. 

**Accompaniment estimation.** To perform accompaniment estimation we initialize _x_ 0 to be the musical accompaniment _a_ , while the singing voice _v_ is the target _ϵ_ for training in Eq. 4, and we adjust _β_ . Since usually the accompaniment is a mixture of multiple sources, and the singing voice – now the perturbation – is normally predominant, we may increase the number of diffusion steps to 100 in the schedule and experiment with a more granular reverse process. The other parameters remain unchanged. 

## **2.2 Network details** 

We propose to use the unconditional vanilla DiffWave to learn the reverse process [16]. Although recent works in music separation propose various improvements with regards to the architectures used, in this work we focus on exploring a novel diffusion-inspired process for source separation. At the same time, we aim at improving a smaller model that has been previously applied for source separation using our diffusion-inspired training and sampling method, while leaving the improvements on the network, or using a different architecture, as future work. Nonetheless, we consider the versatility and light weight of the entire method an advantage. Note that within the scope of this paper, we perform monaural source separation. 

**Architecture.** The DiffWave architecture is based on a modified WaveNet [30] extended with bidirectional dilated convolution modules (Bi-DilConv), aiming at removing the autoregressive generation constraint so that the model is non-causal and the reverse process is done in _T_ steps. The said Bi-DilConv modules have been pre- 

> 2 Despite being aware that our perturbation is a deterministic signal instead of stochastic noise, we still use the term noise schedule in this work for easier understanding in relation with cited works. 

viously applied for the problem of music source separation [12, 28]. The used non-causal WaveNet consists of a stack of _L_ residual layers, which are equally grouped into _N_ blocks. Therefore, each block includes<sup>_L_</sup> _/N_ layers with skip-connections as the original WaveNet. A Bi-DilConv module with kernel-size 3 is included in each layer. The size of the dilation, initialized at 1, is doubled at each layer of a block: [1 _,_ 2 _,_ 4 _,_ 8 _, ...,_ 2<sup>_L_</sup> _/N −_ 1]. Before going through the stacked blocks, the input is projected using a 1D convolutional layer of _C_ channels of features. Similarly to the original WaveNet, the output is obtained by summing the skip connections of all the residual blocks. For our experiments we configure the WaveNet architecture with _L_ = 30, _N_ = 10, and _C_ = 64, which in [16] is found to effectively work while preserving the light weight of the architecture. 

**Diffusion step embedding.** Since the training process is based on optimizing Eq. 4 given a pair ( _xt, x_ 0), we need to input the diffusion step _t_ to the model. We use a 128dimension encoding vector for each _t_ [16], defined as [31]: 



<!-- Start of picture text -->
0 ∗F ( S− 1) ∗f<br>tembed = sin 10 S− 1 t , ..., sin 10 S− 1 t ,<br>� � � � �<br>0 ∗F ( S− 1) ∗F (5)<br>cos 10 S− 1 t , ..., cos 10 S− 1 t<br>� � � ��<br><!-- End of picture text -->

where _F_ is the embedding factor and _S_ is half the embedding size. Note that _F_ and _S_ are pre-defined and fixed hyperparameters, which in our experimentation are set to _F_ = 4 and _S_ = 64. Next, the embedded diffusion step is passed through three dense layers, the first two having size _S ∗_ 2, while the latter maps the latent embedding into the _C_ channels the input is projected to, therefore we can add the embedding to the input of each residual layer. 

**Conditioning.** Using a vocoder paradigm, diffusionbased approaches for audio modelling usually use conditioning to guide the signal generation, providing clues to obtain a particular desired output. Audio-related diffusion works in the literature propose to guide the signal generation using, for instance, mel-spectrogram [16, 32] or linguistic features [33]. We do not condition our network for three reasons: **(1)** Conditioning our vocal extraction model, for instance on the mel-spectrogram of the target vocal signal, would probably improve the output quality, however the task of source separation assumes that data of this kind is not available at inference, **(2)** Our latent variable _xT_ is not an isotropic Gaussian but a known mixture recording containing the target signal, therefore it serves as a conditioner to guide the transformation towards the isolated singing voice, **(3)** We reduce the model size. 

## **2.3 Post-processing** 

To account for a possible over-increase of the signal amplitude during the reverse process, the output of said process is clamped to the amplitude levels of the input mixture. 

During the iterative signal transformation at inference we may generate audio content and artifacts not contained in the original vocal signal. Although not perceptually significant, these artifacts are heavily penalized by objective evaluation metrics [34]. Moreover, the iterative nature of the algorithm may accumulate several of the said artifacts 

687 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

in the final prediction. As an optional step, we use the multichannel Wiener filter to improve our separation, a well-known process used in numerous source separation works [35]. We use the Python version in norbert [36]. 

Since our model operates in an end-to-end manner, we use the following procedure to apply the Wiener filtering. Let _v_ ˆ be an estimated vocal source and _a_ ˆ the corresponding estimated musical accompaniment. The inputs of the Wiener process are the Short-Time Fourier Transform (STFT) of the input mixture _m_ , and the magnitude STFT of both ˆ _v_ and ˆ _a_ estimates. The outputs of the Wiener process are the filtered complex spectrograms for _v_ ˆ and _a_ ˆ. We take the magnitude of said spectrograms and combine it with the corresponding phases _ϕ_ (ˆ _v_ ) and _ϕ_ (ˆ _a_ ) that our proposed model estimates. In that sense, we do not use the Wiener filtering to estimate the phase as typically done for spectrogram-based approaches that cannot estimate such complex target, but refine our estimation using the Expectation-Maximization algorithm [37] to make sure that the predicted signal is contained in the input mixture. 

## **3. RELATION WITH PREVIOUS WORK** 

The literature on waveform-based singing voice extraction is mainly based on encoder/decoder architectures, with the non-causal adaptation of WaveNet [12,30] as the only exception. Wave-U-Net [3] is an autoencoder inspired by its spectrogram-based counterpart U-Net [7], while ConvTasNet [2, 4] estimates prediction masks in the mid-point of the network. The leading model is Demucs, now available in two versions v1 [1] and v2 [2], which is also a convolutional autoencoder with a bidirectional LSTM in the bottleneck. There is a growing tendency on the size of the above-mentioned models, while all use similar, standard training procedures. In contrast, we focus on the training strategy and propose a diffusion-inspired approach for a light-weight model. Building on top of DiffWave, we train a non-causal WaveNet very similar to the one used for music source separation [30], differing only on the number of residual layers, the output projection (since WaveNet in [30] estimates multiple targets while in DiffWave the target is only the added perturbation by the diffusion process), and the additional diffusion step embedding. 

Our work has common aspects with [39], in which a novel training strategy is built on top of Demucs (v2) by modelling and learning the dependencies between target sources, and adding an iterative refinement at the output using a Gibbs sampling process. Contrastingly, we use a diffusion-inspired algorithm to train a smaller baseline model for source separation, not to directly estimate the target sources but to gradually transform a mixture signal into its corresponding singing voice. 

The literature of diffusion-related approaches for music source separation is scarce. In [25], an improved reverse process based on Langevin dynamics is proposed and applied to several autoregressive models, including WaveNet, which shows competitive performance on separating the vocals from a piano accompaniment. However no experiments on MUSDB18 [40] are reported. 

## **4. EXPERIMENTS** 

## **4.1 Experimental setup** 

We include the following models in our experiments: **(1)** Singing voice extraction model with different noise schedules: _β_ 20 and _β_ 8 and _β_ 1, **(2)** Singing voice extraction model with _β_ 20 and Wiener filtering, using the accompaniment obtained by subtracting the estimated vocals _v_ ˆ from the input mixture _m_ , **(3)** Accompaniment extraction model with _β_ 100, **(4)** Combination of singing voice extraction model with _β_ 20 and accompaniment extraction model with _β_ 100 using Wiener filtering. For the experiments we use ADAM optimizer with learning rate of 2<sup>_−_4</sup> and batch size of 8. The models are first trained for 200k steps and next, we keep training while evaluating the performance using BSS Eval [41] repeatedly when _≈_ 500 training steps are completed, storing the model that performs the best on the validation set, until 500k steps. 

We use the MUSDB18 dataset [40] for training. The accompaniment is computed as the linear sum of the _bass_ , _drums_ , and _other_ sources as represented in the dataset. To train the models we first split the tracks in MUSDB18 in chunks of 4 seconds to optimize the training process and obtain more variate data batches along the training steps. We do not disregard the unvoiced samples, aiming at improving the estimation on vocal silences [28]. 

For a comparison with the state-of-the-art, our models are evaluated on the test set of MUSDB18, using the standardized metrics for source separation (Signal-toDistortion Ratio or SDR, Signal-to-Interference Ratio or SIR, and Signal-to-Artifact Ratio or SAR) [42]. We use the BSS Eval implementation and the evaluation setup from the SiSEC challenge [41], using window and hop sizes of 1 second, and subsequently computing the median over all the 1-second estimations of each song. We finally report the median over the entire MUSDB18 testing tracks. We compare our approach with the waveform-based state-ofthe-art: WaveNet, Wave-U-Net, ConvTas-Net and Demucs v1 and v2. We report the metrics that the best versions of these methods obtain on the testing set of MUSDB18 [41]. For WaveNet we consider the best performing configuration in [28], and for ConvTas-Net the music source separation version proposed in [2]. 

Being aware of the possible biases that might occur if training and evaluating on data from the same distribution, even if the splits are properly differentiated, we consider two additional testing sets: (1) A non-MUSDBoverlapping version of MedleyDB [43], in which we remove the 46 overlapping tracks between MedleyDB and MUSDB18 [44] disregarding also the tracks from shared artists between the two even if the track is not present in both, and (2) A manually-cleaned subset of the multi-track audio of the Saraga Carnatic dataset [45] (ground-truth accompaniment is not available). The track list of both datasets is made available in the accompanying repository. 

The objective metrics in [41] are not always correlated with the scores from perceptual evaluations of music source separation [46]. However, perceptual tests are 

688 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

||||**Sin**|**ging Vo**|**ice**|**Acc**|**ompani**|**ment**|
|---|---|---|---|---|---|---|---|---|
|**Model**|**Params**|**Diff. steps**|**SDR**|**SIR**|**SAR**|**SDR**|**SIR**|**SAR**|
|WaveNet [12] (w/ add. loss [38])|_≈_3.3M|-|4.49|13.52|6.17|11.39|16.37|13.49|
|Wave-U-Net [3]|_≈_10.2M|-|4.97|13.98|4.41|11.11|15.30|11.44|
|ConvTas-Net [2]|_≈_8.75M|-|6.43|-|-|-|-|-|
|Demucs (v1) [1]|-|-|5.44|-|-|-|-|-|
|Demucs (v2) [2]|_≈_450M|-|6.84|-|-|-|-|-|
|Ours (vocal)|_≈_750K|1|4.81|9.21|8.09|-|-|-|
|Ours (vocal)|_≈_750K|8|5.63|10.55|8.86|-|-|-|
|Ours (vocal)|_≈_750K|20|5.59|10.78|8.89|-|-|-|
|Ours (vocal) + Wiener|_≈_750K|20|5.66|11.60|8.49|-|-|-|
|Ours (accomp)|_≈_750K|100|-|-|-|11.12|13.11|16.44|
|Ours (vocal & accomp) + Wiener|_≈_750K + 750K|20 + 100|6.07|12.77|8.61|11.72|14.44|16.81|



**Table 1** . Performance comparison between our model and the waveform-based state-of-the-art. Metrics in dB. 

time-consuming and expensive to conduct. We run a perceptual evaluation of the vocal separation for four models: Wavenet (again the best model in [28]), Wave-U-Net (the best model in [3] for monaural separation), Demucs (the v2 model for stereo mixture and 4 sources), and our best model (combining both vocal and accompaniment extraction models using Wiener). We reiterate the experiment in [28] with the same 5 songs (10 second excerpts) and including now our model and Demucs v2.<sup>3</sup> 

In this perceptual experiment we follow a double-blind multi-stimulus experimental design with a hidden reference. Similarly to [28], participants are asked to assess the global quality of vocal separation taking into account the suppression of other sources and the lack of distortion, rating the stimuli on scale from 1 to 5, with 1 being _very intrusive interferences from other sources and degraded audio_ , and 5 being _unnoticeable interferences from other sources and not degraded audio_ . In contrast to [28], the order of the songs is randomized, so that the final rating does not depend on a predefined ordering. In addition, we include the ground-truth vocal stem as a hidden reference along the other stimuli corresponding to the vocal separation of the four models being tested. This hidden reference is used as a control stimuli to filter-out participants that have not performed the training stage, have not understood the task, or do not have sufficient expertise. The participants are asked to calibrate the volume using a tone burst. Then, they perform a training stage where detailed instructions and three audio examples from the same song are presented: the reference mixture, the ground-truth vocal stem and a poor quality separation using a model not included in our test. We use the webMUSHRA framework [47] to implement the experimental design in an online test. 

## **4.2 Objective evaluation** 

In Table 1 we compare the performance of our approach with the waveform-domain state-of-the-art models. No metrics on accompaniment separation and SIR/SAR for vocals are reported for Demucs and ConvTas-Net since 

these target to _vocals, bass, drums and other_ . We observe that our vocal extraction model outperforms WaveNet (note that DiffWave is based on WaveNet), Wave-U-Net, and Demucs v1 in terms of SDR, the latter by a slight difference. Our model provides notable improvement on SAR, which is translated into an output with less artifacts. When combining our vocal and accompaniment extraction models through Wiener filter we obtain closer performance to ConvTas-Net, while Demucs v2 is still leading on SDR _≈_ 0 _._ 8 _dB_ above. While iteratively transforming an input mixture, for instance, to the corresponding singing voice, incorrectly estimated accompaniment that is not recognised in the subsequent reverse steps may accumulate in the final prediction. Although the said interferences might not be audible at naked ear, these are penalized by the metrics. The Wiener filtering provides notable improvement on that issue, as especially noted in the SIR and also in the perceptual evaluation in Section 4.3, albeit the source quality is slightly compromised. Finally, note that we use fewer parameters, enhancing the portability and reproducibility of our approach. 

The _β_ 1 singing extraction model, which directly estimates the perturbation by transforming the input mixture in a single run, scores similar than the baseline WaveNet, however we observe a notable decrease of SIR, while SAR improves. This may be given the transformation nature of our approach, which removes the perturbation from the target source instead of directly estimating the source. The _β_ 8 model scores similar than _β_ 20, however the SIR decreases while SAR is maintained. While adding more steps provides improved interference removal, no notable negative effect is observed in the quality of the estimated source. Nonetheless, if the computational expense is prioritized, the _β_ 8 model may be used for an optimized inference since the measured performance drop in our experiments is not dramatic. In fact, both models predict faster than real-time on a TITAN Xp GPU. For accompaniment separation, using _β_ 100 provides better predictions. However, as observed for vocals, we may be also capable of modelling this task using less steps, with no significant performance drop. 

3 jordipons.me/apps/end-to-end-music-source-separation 

689 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

|||**M**|**USDB1**|**8**|**M**|**edleyD**|**B**|**Saraga Carnatic**|
|---|---|---|---|---|---|---|---|---|
|**Model for singing voice**|**Model weight**|**SDR**|**SIR**|**SAR**|**SDR**|**SIR**|**SAR**|**SDR**|
|Ours (vocal, _β_20, no Wiener)|_≈_26MB|5.59|10.78|8.89|4.86|8.87|9.06|4.11|
|Wave-U-Net [3]|_≈_117MB|4.97|13.98|4.41|1.61|7.47|4.50|2.13|
|Demucs (v2) [2]|_≈_1GB|6.84|-|-|6.01|-|-|6.12|



**Table 2** . Performance comparison of our baseline model and state-of-the-art on additional test datasets. Metrics in dB. 

In Table 2 we evaluate our baseline _β_ 20 singing voice extraction model (with no post-processing) on the two additional testing datasets presented in Section 4.1. We perform the same evaluation procedure for Wave-U-Net and Demucs v2, comparing how the three models generalize to the testing datasets, using the performance on MUSDB18 – which is also the training dataset for the three – as reference. Our model and Demucs v2 show good generalization to MedleyDB, both getting a similar and small performance drop. Contrastingly, the Wave-U-Net performance is negatively affected in terms of both SDR and SIR. A similar scenario is observed in the Carnatic Music experiment. While Wave-U-Net generalization is again compromised, our model and Demucs v2 are decently able to maintain the performance, the latter being less affected by the change of domain. Similarly to what observed in the MUSDB18 experiment, Demucs v2 predictions include less artifacts, especially in the high-frequency range, being reflected in the metrics as such. Audio examples of this experiment are available in the accompanying repository. 

We analyse the behaviour of the _β_ 20 singing voice model along the steps in the reverse process. We observe that the SIR (interf.) notably increases along the steps, at a compromise of a much less steeply SAR (artifacts) decrease. Namely, as we iteratively transform the signal from mixture to singing voice, we remove the accompaniment while trying to maintain the quality of the singing voice, relying on the model trained with our diffusion-inspired strategy to estimate the perturbation at each step while alleviating the additional interferences incorrectly generated during the reverse process. We note that given the parametrization of the reverse process, stronger transformation is performed in the first steps (1 to 5 for _β_ 20), while the rest of the steps refine the final estimation. For that reason, fair or good performance – relatively to the overall track difficulty – on the first step normally leads to enhanced final output, while bad initial performance may even be further degraded through the reverse process. 

## **4.3 Perceptual evaluation** 

In total 40 people participated in our experiment, 4 of them being excluded because they scored the ground-truth stimuli lower than a separation stimuli. We compute Mean Opinion Score (MOS) by averaging the ratings for all songs and all participants. The results in terms of MOS are presented in Figure 2. Note that Ground-truth is not reaching 5, meaning that the test includes difficult cases with distorted vocals or large unvoiced segments. We observe that the 95% Confidence Interval for our model is very sim- 



<!-- Start of picture text -->
5 Cl (95%) 4.74<br>[1.57, 1.82]<br>[2.22, 2.50]<br>4 [2.55, 2.86]<br>[2.55, 2.88]<br>[4.67, 4.84] 2.71 2.72<br>2.35 T<br>1.71<br>Evaluation(1-Bad/5-Exc el nt)<br>WaveNet Wave-U-Net Demucs(v2) Ours Ground-truth<br><!-- End of picture text -->

**Figure 2** . Perceptual evaluation report for the waveformbased state-of-the-art models and ours 

ilar to Demucs and notably higher than both Wave-U-Net and especially WaveNet, a very similar architecture to the instance we have trained using our diffusion-inspired strategy. Such test suggests that the predictions made by our approach may include artifacts or interferences that affect negatively the standardized metrics but are not perceivable at naked ear. This test may be extended in future to separately study the perceivable distortion and interference. 

## **5. CONCLUSIONS** 

In this paper we leverage from the denoising diffusion algorithm to propose a training and sampling strategy for singing voice extraction. The model trained using our approach learns to gradually transform a mixture into its corresponding vocal source or accompaniment, achieving comparable performance to the waveform-based state-ofthe-art on MUSDB18. In addition, we evaluate how our approach generalizes to other testing sets, showing decent generalization to these out-of-domain data. We also run a perceptual test in which our approach scores similar than Demucs v2 and outperforms the others. Our approach operates on an architecture similar to WaveNet and obtains better objective and perceptual evaluation. This work has a broad future outlook. For the next steps, we look at separating other sources and supporting stereo. We also look at extending the approach, for instance, by using a different or improved network to learn the reverse process, focusing on U-Nets which are the leading architecture music source separation. We may also consider conditioning, the key element of diffusion-based approaches in the literature. Finally, our diffusion-inspired reverse parametrization may be further improved to better refine the predictions. 

690 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

## **6. ACKNOWLEDGEMENTS** 

This work was carried out under the projects Musical AI - PID2019-111403GB-I00/AEI/10.13039/501100011033 and NextCore - RTC2019-007248-7 funded by the Spanish Ministerio de Ciencia, Innovación y Universidades (MCIU) and the Agencia Estatal de Investigación (AEI). We would like to thank the 40 participants that took the perceptual test for this work. 

## **7. REFERENCES** 

- [1] A. Défossez, N. Usunier, L. Bottou, and F. Bach, “Demucs: Deep Extractor for Music Sources with extra unlabeled data remixed,” 2019. [Online]. Available: http://arxiv.org/abs/1909.01174 

- [2] A. Défossez, N. Usunier, L. Bottou, and F. Bach, “Music Source Separation in the Waveform Domain,” 2019. [Online]. Available: http://arxiv.org/abs/1911. 13254 

- [3] D. Stoller, S. Ewert, and S. Dixon, “Wave-U-Net: A multi-scale neural network for end-to-end audio source separation,” _In Proc. of the 19th Int. Society for Music Information Retrieval Conf. (ISMIR),_ Paris, France, pp. 334–340, 2018. 

- [4] Y. Luo and N. Mesgarani, “Conv-TasNet: Surpassing Ideal Time-Frequency Magnitude Masking for Speech Separation,” _IEEE/ACM Transactions on Audio Speech and Language Processing_ , vol. 27, no. 8, pp. 1256– 1266, 2019. 

- [5] N. Takahashi and Y. Mitsufuji, “D3Net: Densely connected multidilated DenseNet for music source separation,” 2020. [Online]. Available: http://arxiv. org/abs/2010.01733 

- [6] T. Li, J. Chen, H. Hou, and M. Li, “Sams-Net: A Sliced Attention-based Neural Network for Music Source Separation,” _In Proc. on the 12th Int. Symposium on Chinese Spoken Language Processing (ISCSLP)_ , 2021. 

- [7] A. Jansson, E. Humphrey, N. Montecchio, R. Bittner, A. Kumar, and T. Weyde, “Singing voice separation with deep U-Net convolutional networks,” _In Proc. of the 18th Int. Society for Music Information Retrieval Conf. (ISMIR),_ Suzhou, China, pp. 745–751, 2017. 

- [8] A. Défossez, “Hybrid spectrogram and waveform source separation,” 2021. [Online]. Available: http: //arxiv.org/abs/2111.03600 

- [9] M. Kim, W. Choi, J. Chung, D. Lee, and S. Jung, “KUIELab-MDX-Net: A Two-Stream Neural Network for Music Demixing,” 2021. [Online]. Available: http://arxiv.org/abs/2111.12203 

- [10] C.-Y. Yu and K.-W. Cheuk, “Danna-Sep: Unite to separate them all,” 2021. [Online]. Available: http://arxiv.org/abs/2112.03752 

- [11] Y. Mitsufuji, G. Fabbro, S. Uhlich, F.-R. Stöter, A. Défossez, M. Kim, W. Choi, C.-Y. Yu, and K.-W. Cheuk, “Music Demixing Challenge 2021,” _Frontiers in Signal Processing_ , no. January, 2022. 

- [12] D. Rethage, J. Pons, and X. Serra, “A wavenet for speech denoising,” _In Proc. of the IEEE Int. Conf. on Acoustics, Speech and Signal Processing (ICASSP),_ Paris, France, vol. 2018-April, pp. 5069–5073, 2018. 

- [13] J. Ho, A. Jain, and P. Abbeel, “Denoising diffusion probabilistic models,” _In Proc. of the 33th Advances in Neural Information Processing Systems (NeurIPS),_ Online, pp. 6840–6851, 2020. 

- [14] C. Jarzynski, “Equilibrium free-energy differences from nonequilibrium measurements: A masterequation approach,” _Physical Review_ , 1997. 

- [15] J. Zhang, S. Jayasuriya, and V. Berisha, “Restoring degraded speech via a modified diffusion model,” _In Proc. of the Annual Conf. of the Int. Speech Communication Association (INTERSPEECH),_ Online, vol. 4, pp. 2753–2757, 2021. 

- [16] Z. Kong, W. Ping, J. Huang, K. Zhao, and B. Catanzaro, “DiffWave: A Versatile Diffusion Model for Audio Synthesis,” _In Proc. of the 9th Int. Conf. on Learning Representations (ICLR),_ Vienna, Austria, 2021. 

- [17] J. Sohl-Dickstein, E. A. Weiss, N. Maheswaranathan, and S. Ganguli, “Deep unsupervised learning using nonequilibrium thermodynamics,” _In Proc. of the 32nd Int. Conf. on Machine Learning (ICML),_ Lille, France, vol. 3, pp. 2246–2255, 2015. 

- [18] N. Chen, Y. Zhang, H. Zen, R. J. Weiss, M. Norouzi, and W. Chan, “WaveGrad: Estimating Gradients for Waveform Generation,” _In Proc. of the 9th Int. Conf. on Learning Representations (ICLR),_ Vienna, Austria, 2021. 

- [19] Y.-J. Lu, Z.-Q. Wang, S. Watanabe, A. Richard, C. Yu, and Y. Tsao, “Conditional Diffusion Probabilistic Model for Speech Enhancement,” _In Proc. of the IEEE Int. Conf. on Acoustics, Speech and Signal Processing (ICASSP),_ Singapore, 2022. 

- [20] Y. J. Lu, Y. Tsao, and S. Watanabe, “A Study on Speech Enhancement Based on Diffusion Probabilistic Model,” _In Proc. of the Asia-Pacific Signal and Information Processing Association Annual Summit and Conf. (APSIPA ASC),_ Online, pp. 659–666, 2021. 

- [21] J. Serrà, S. Pascual, J. Pons, R. O. Araz, and D. Scaini, “Universal speech enhancement with score-based diffusion,” 6 2022. [Online]. Available: http://arxiv.org/abs/2206.03065 

- [22] J. Lee and S. Han, “NU-wave: A diffusion probabilistic model for neural audio upsampling,” _In Proc. of the Annual Conf. of the Int. Speech Communication Association (INTERSPEECH),_ Brno, Czech Republic, vol. 4, no. 3, pp. 2698–2702, 2021. 

691 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

- [23] J. Liu, C. Li, Y. Ren, F. Chen, and Z. Zhao, “DiffSinger: Singing Voice Synthesis via Shallow Diffusion Mechanism,” _In Proc. of the 36th Conf. on Artificial Intelligence (AAAI),_ Online, 2022. 

- [24] G. Mittal, J. Engel, C. Hawthorne, and I. Simon, “Symbolic Music Generation with Diffusion Models,” _In Proc. of the 22th Int. Society for Music Information Retrieval Conf. (ISMIR),_ Online, pp. 468–475, 2021. 

- [25] V. Jayaram and J. Thickstun, “Parallel and Flexible Sampling from Autoregressive Models via Langevin Dynamics,” _In Proc. of the Int. Conf. on Learning Representations (ICLR),_ Online, 2021. 

- [26] A. Bansal, E. Borgnia, H.-M. Chu, J. S. Li, H. Kazemi, F. Huang, M. Goldblum, J. Geiping, and T. Goldstein, “Cold diffusion: Inverting arbitrary image transforms without noise,” 8 2022. [Online]. Available: http://arxiv.org/abs/2208.09392 

- [27] J. L. Durrieu, G. Richard, B. David, and C. Févotte, “Source/filter model for unsupervised main melody extraction from polyphonic audio signals,” _IEEE Transactions on Audio, Speech, and Language Processing_ , vol. 18, no. 3, 2010. 

- [28] F. Lluís, J. Pons, and X. Serra, “End-to-end music source separation: Is it possible in the waveform domain?” _In Proc. of the Annual Conf. of the Int. Speech Communication Association (INTERSPEECH),_ Graz, Austria, vol. 2019-September, pp. 4619–4623, 2019. 

- [29] D. P. Kingma, T. Salimans, B. Poole, and J. Ho, “Variational Diffusion Models,” _In Proc. of the 35th Conf. on Neural Information Processing Systems (NeurIPS 2021),_ Online, pp. 21 696–21 707, 2021. 

- [30] A. van den Oord, S. Dieleman, H. Zen, K. Simonyan, O. Vinyals, A. Graves, N. Kalchbrenner, A. Senior, and K. Kavukcuoglu, “WaveNet: A Generative Model for Raw Audio,” 2016. [Online]. Available: http://arxiv.org/abs/1609.03499 

- [31] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polosukhin, “Attention is all you need,” _Advances in Neural Information Processing Systems (NeurIPS),_ Long Beach, USA, vol. 2017-December, pp. 5999–6009, 2017. 

- [32] W. Ping, K. Peng, A. Gibiansky, S. O. Arik, A. Kannan, S. Narang, J. Raiman, and J. Miller, “Deep Voice 3: Scaling text-to-speech with convolutional sequence learning,” _In Proc. of the Int. Conf. on Learning Representations (ICLR),_ Vancouver, Canada, 2018. 

- [33] S. O. Arik, G. Diamos, A. Gibiansky, J. Miller, K. Peng, W. Ping, J. Raiman, and Y. Zhou, “Deep Voice 2: Multi-speaker neural text-to-speech,” _In Proc. of the Conf. on Neural Information Processing Systems (NeurIPS),_ Long Beach, USA, 2017. 

- [34] P. Chandna, M. Blaauw, J. Bonada, and E. Gomez, “A Vocoder Based Method for Singing Voice Extraction,” _In Proc. of the IEEE Int. Conf. on Acoustics, Speech and Signal Processing (ICASSP),_ Brighton and Hove, UK, vol. 2019-May, pp. 990–994, 2019. 

- [35] A. Nugraha, A. Liutkus, and E. Vincent, “Multichannel audio source separation with deep neural networks,” _IEEE/ACM Transactions on Audio, Speech, and Language Processing_ , vol. 24, no. 9, pp. 1652–1664, 2016. 

- [36] A. Liutkus and F. R. Stöter, “sigsep/norbert,” 2019. [Online]. Available: https://doi.org/10.5281/zenodo. 3269749 

- [37] N. Duong, E. Vincent, and R. Gribonval, “Underdetermined reverberant audio source separation using a full-rank spatial covariance model,” _IEEE Transactions on Audio, Speech, and Language Processing_ , vol. 18, no. 7, pp. 1830–1840, 2010. 

- [38] P. Huang, M. Kim, M. Hasegawa-Johnson, and P. Smaragdis, “Singing-voice separation from monaural recordings using deep recurrent neural networks,” _In Proc. of the 15th Int. Society for Music Information Retrieval Conf. (ISMIR),_ Taipei, Taiwan, pp. 477–482, 2014. 

- [39] E. Manilow, C. Hawthorne, C.-Z. Huang, B. Pardo, and J. Engel, “Improving Source Separation by Explicitly Modeling Dependencies Between Sources,” _In Proc. of the IEEE Int. Conf. on Acoustics, Speech and Signal Processing (ICASSP),_ Singapore, 2022. 

- [40] Z. Raf **i** , A. Liutkus, F.-R. Stöter, S. I. Mimilakis, and R. Bittner, “MUSDB18 - a corpus for music separation,” Dec. 2017. [Online]. Available: https: //doi.org/10.5281/zenodo.1117372 

- [41] F. R. Stöter, A. Liutkus, and N. Ito, “The 2018 Signal Separation Evaluation Campaign,” _Lecture Notes in Computer Science_ , vol. 10891, pp. 293–305, 2018. 

- [42] E. Vincent, R. Gribonval, and C. Févotte, “Performance measurement in blind audio source separation,” _IEEE Transactions on Audio, Speech, and Language Processing_ , vol. 4, no. 14, pp. 1462–1469, 2006. 

- [43] R. Bittner, J. Salamon, M. Tierney, M. Mauch, C. Cannam, and J. Bello, “MedleyDB: A multitrack dataset for annotation-intensive MIR research,” _In Proc. of the 15th Int. Society for Music Information Retrieval Conf. (ISMIR),_ Taipei, Taiwan, pp. 155–160, 2014. 

- [44] “SigSep MUSDB Website,” https://sigsep.github.io/ datasets/musdb.html, accessed: 01-05-2022. 

- [45] A. Srinivasamurthy, S. Gulati, R. C. Repetto, and X. Serra, “Saraga: Open Datasets for Research on Indian Art Music,” _Empirical Musicology Review_ , 2020. 

692 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

- [46] E. Cano, D. Fitzgerald, and K. Brandenburg, “Evaluation of quality of sound source separation algorithms: Human perception vs quantitative metrics,” _In Proc. of the 24th European Signal Processing Conf. (EUSIPCO),_ Budapest, Hungary, pp. 1758–1762, 2016. 

- [47] M. Schoeffler, S. Bartoschek, F.-R. Stöter, M. Roess, S. Westphal, B. Edler, and J. Herre, “webmushra—a comprehensive framework for web-based listening tests,” _Journal of Open Research Software_ , vol. 6, no. 1, 2018. 

693 

