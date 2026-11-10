---
paper_id: "000025"
year: 2022
title: "Download pdf"
source_url: "https://zenodo.org/record/7316634/files/000025.pdf"
---

# DISTORTION AUDIO EFFECTS: LEARNING HOW TO RECOVER THE CLEAN SIGNAL 

Johannes Imort<sup>♮</sup> Giorgio Fabbro<sup>♯</sup> Marco A. Martínez-Ramírez<sup>♭</sup> Stefan Uhlich<sup>♯</sup> Yuichiro Koyama<sup>♭</sup> Yuki Mitsufuji<sup>♭</sup> 

♮RWTH Aachen University, Germany ♯Sony Europe B.V., Stuttgart, Germany 

♭Sony Group Corporation, Tokyo, Japan 

johannes.imort@rwth-aachen.de, giorgio.fabbro@sony.com 

## ABSTRACT 

Given the recent advances in music source separation and automatic mixing, removing audio effects in music tracks is a meaningful step toward developing an automated remixing system. This paper focuses on removing distortion audio effects applied to guitar tracks in music production. We explore whether effect removal can be solved by neural networks designed for source separation and audio effect modeling. 

Our approach proves particularly effective for effects that mix the processed and clean signals. The models achieve better quality and significantly faster inference compared to state-of-the-art solutions based on sparse optimization. We demonstrate that the models are suitable not only for declipping but also for other types of distortion effects. By discussing the results, we stress the usefulness of multiple evaluation metrics to assess different aspects of reconstruction in distortion effect removal. 

## 1. INTRODUCTION 

With the emergence of musical recordings, audio effects have become indispensable in the music production process. They are used by musicians as a creative tool to alter the sound of their instruments, and by sound engineers to craft a balanced mix from multiple recording tracks [1]. 

For the task of mixing and automatic remixing [2], the dry (i.e., unprocessed) source tracks are required. Given the recent advances in automatic mixing [3, 4] and music source separation (MSS) [5], a system could facilitate the adjustment of a stereo mixture to the taste and preferences of the user similar to [6]. However, when separating sources with a system trained on music stems (e.g., MUSDB18 [7]) the mixing process is not considered, and, hence, the output of such a system contains the wet (i.e., processed) signal. As nonlinear distortion is one of the most commonly used effects for electric instruments, this 

> © J. Imort, G. Fabbro, M. A. Martínez-Ramírez, S. Uhlich, Y. Koyama, and Y. Mitsufuji. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: J. Imort, G. Fabbro, M. A. Martínez-Ramírez, S. Uhlich, Y. Koyama, and Y. Mitsufuji, ªDistortion Audio Effects: Learning How to Recover the Clean Signalº, in Proc. of the 23rd Int. Society for Music Information Retrieval Conf., Bengaluru, India, 2022. 

work focuses on musical distortion effects that are used for aesthetic means (e.g., guitar overdrive/distortion pedals) and applied in the process of mixing (e.g., tape saturation). These distortion effects result in added harmonics, intermodulation distortion, and a compressed sound [8]. 

This paper investigates different deep neural network (DNN) approaches regarding their applicability to the audio effect removal problem. Our contributions can be summarized as follows: 

- We show that recovering the clean signal from clipped or overdriven guitar signals can be efficiently solved with neural networks designed for source separation. The models achieve high quality and fast inference in contrast to solutions based on sparse optimization. 

- We found that the superior performance of the models evaluated on the de-overdrive task can be traced back to superimposing the overdriven signal with the clean signal. We show that the architectures are suitable not only for declipping but also for other types of distortion effects. 

- By discussing the results, we highlight that the metrics under evaluation prove beneficial in measuring different aspects of the reconstruction and can be advised for further investigations. 

This work is organized as follows: Sec. 2 gives a formal introduction to audio effect removal and introduces the types of distortions that were used throughout this study. Sec. 3 briefly discusses previous work on iterative and DNN-based declipping approaches. The methods under evaluation are outlined in Sec. 4. Sec. 5 describes the data that were used for training, reports details about the experimental setup, and presents the chosen objective evaluation metrics. In Sec. 6, we evaluate the results of the comparative study of four different neural network architectures on the task of distortion removal in guitar signals for the SoX overdrive implementation. Then, we compare the same architectures on the declipping task to one state-of-the-art declipping algorithm using guitar signals as well as generic music signals. Lastly, Sec. 7 gives a conclusion and presents an outlook for future work. Audio examples are available online at joimort.github.io/distortionremoval/ . 

218 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
x λsox(x10) λtanh(x10) λhc(x10)<br>1.0<br>0.5<br>0.0<br>−0.5<br>−1.0<br>0 1 2 3 4 5 6 7<br>Time / ms<br>Amplitude<br><!-- End of picture text -->

Figure 1. Example of different distortion types applied to a guitar signal. The input signal x(k) is amplified before being modified by a wave-shaper function. 

## 2. PROBLEM FORMULATION 

We introduce audio effect removal as the task of recovering the original discrete audio signal x ∈ R<sup>n</sup> from the processed discrete signal y ∈ R<sup>n</sup> , which is obtained by applying the possibly nonlinear and time-varying function f to the signal x: 



<!-- Start of picture text -->
y = g(x) = αf (x) + (1 − α)x, (1)<br><!-- End of picture text -->

with α ∈ [0, 1] denoting the weight of the wet signal, and g the summation function of the dry and wet signal. The goal is to find an estimation of the original signal ˆx by estimating the inverse function ˆx = gˆ<sup>−1</sup> (y). 

Generally, distortion effects clip the input signal and can be divided into systems that apply hard-clipping or soft-clipping. As this work focuses on both types of distortion, we introduce the following generic formulation of <mark>γ</mark> a wave-shaper that maps the amplified signal xγ = 1 <mark>0</mark> 20 <mark>x</mark> to a fixed range: 



<!-- Start of picture text -->
f (x) = λ(xγ) with λ : R → [−θc, θc]. (2)<br><!-- End of picture text -->

Here, γ denotes the gain in decibels, λ the arbitrary waveshaper function, and θc the fixed clipping threshold. For the case of hard-clipping, λ is defined as: 



<!-- Start of picture text -->
xγ,k, if |xγ,k| ≤ θc<br>λhc(xγ,k) = (3)<br>�θcsgn(xγ,k) otherwise,<br><!-- End of picture text -->

with sgn denoting the sign function, and xγ,k the k-th time sample of the amplified signal. Fig. 1 highlights the difference between different distortion types. Hard-clipping cuts off the amplitude when it exceeds a defined threshold (as typical for saturation in digital signal processing). Soft-clipping (e.g., λtanh(xγ,k) = tanh(xγ,k)) gradually applies a smooth transition before reaching a fully saturated state (as typical for saturation in analog amplifiers). 

Modeling the characteristics of distortion pedals in reality is more complex: [9] provides an overview on different methods and discusses DNN-based approaches. In order to simplify the problem for our investigation, we focus on wave-shaping. The overdrive algorithm of the audio editing software SoX [10] serves as an example of softclipping (λsox) but, in contrast to (2), it is dependent on 

previous samples. Furthermore, it blends the wet signal with the dry one (α < 1). 

## 3. RELATED WORK 

To the best of our knowledge, there has been no previous research on distortion audio effect removal. Therefore, this section outlines the most relevant iterative and DNN-based declipping approaches since declipping is a special case of distortion audio effect removal. 

## 3.1 Iterative Declipping Methods 

Previous research on approaches to declipping has focused mainly on unsupervised algorithms that recover the signal under the assumption of a generic regularization such as signal sparsity [11]. Usually, these approaches target the hard-clipping case only (see (3)). While early approaches were based on auto-regressive models, (e.g., [12]) recent state-of-the-art methods evolved by combining ideas from inverse problems and sparse regularization [13]. 

Recently, [11] and [13] discussed popular declipping algorithms. One of the current state-of-the-art methods is A- SPADE, which will serve as a baseline for this study. The algorithm is briefly introduced in Sec. 4. 

## 3.2 DNN-Based Declipping 

In contrast to iterative algorithms, to date, there are only few contributions comprising supervised DNNs. 

Kashani et al. [14] introduced a declipping method based on the U-Net architecture [15]. It operates on magnitude spectrograms while the waveform of the output is obtained by reusing the phase information from the distorted input signal. The system is trained and evaluated on pairs of hard-clipped and clean speech samples. 

Mack and Habets [16] proposed an architecture comprising a BLSTM-based deep filtering method that works on complex spectrograms and hence also considers phase information. Similar to [14], they train the system on speech data only. Unlike any other approach, they not only investigate the system on the hard-clipping case but also on the soft-clipping case. Tanaka et al. recently proposed APPLADE [17], a declipping method that takes advantage of the sparse optimization techniques described above together with deep learning. Accordingly, they embed a DNN in the iterative algorithm to enhance the thresholding operation. They report a slightly higher performance than previous algorithms, better robustness to mismatches between training and test data, and faster inference. 

## 4. METHODS 

This section describes four neural network architectures that we selected from the literature and evaluated on the distortion removal task. We approach the distortion effect removal problem from the perspective of filtering the added harmonics and intermodulation distortion, similar to [16]. Therefore, we include one model from the domain 

219 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

of audio effect modeling and three architectures originally proposed for music source separation.<sup>1</sup> For the latter models, instead of multiple output channels for different sources, we use only one output channel and consider them as general audio-to-audio transformation architectures. 

CRAFx was proposed as a system for modeling timevarying audio effects with a neural network [9, 18]. The end-to-end model operates on the signal in the time domain and is divided into an adaptive front-end (encoder), a bi-directional long-short-term-memory (BLSTM)-based structure that applies the modeled effect in the latent space, and a synthesis back-end (decoder). In contrast to the other DNN-based models presented in this section, this architecture employs architectural priors (e.g., learnable nonlinear activations) in the context of audio effects. 

Open-Unmix (UMX) was introduced as a reference implementation for music source separation [19]. The architecture is based on the BLSTM model from [20] and uses magnitude spectrograms as input features. The essential element of Open-Unmix is its three-layer BLSTM network that enables to learn both long- and short-time dependencies [21]. 

An element-wise multiplication of the input spectrograms with the estimated masks yields the final output. Commonly, spectrogram-based source separation models are compared with the oracle performance of an ideal ratio mask (IRM) that is defined as the ratio between the reference and the test spectrogram [22] in decibels. For reconstruction, the phase of the input signal is used. The model was adapted for a sampling rate of fs = 16 kHz. We include this model in our evaluation as a standard frequency domain MSS model that relates to the BLSTM-based declipping model from [16] (cf. Sec. 3.2). 

Wave-U-Net was proposed as one of the first end-toend approaches for music source separation based on time domain signals [23]. Hence, it incorporates not only the magnitude but also the phase of music signals. It adapts the U-Net architecture [15] to one-dimensional audio signals. We decreased the models’ number of learnable parameters from 17M to approximately 1M by reducing the number of layers from 12 to 8 resulting in a reduced receptive field, as we experienced overfitting for our datasets. Since the model was successfully employed not only for source separation but automatic mixing as well [3], we assume a general suitability for audio-to-audio transformation tasks. Moreover, the model is highly related to the U-Net-based declipping model from [14] (cf. Sec. 3.2). 

Demucs was initially designed to be an end-to-end model for music source separation in the time domain [24]. While it builds on the Wave-U-Net model, it introduces several improvements to the architecture. The model comprises a convolutional encoder, a BLSTM structure, and a convolutional decoder. As for Wave-U-Net, we decreased the number of trainable parameters from 66M to 1M by reducing the number of blocks from 12 to 6 resulting in a 

> 1 Two of the methods under evaluation, Demucs and Wave-U-Net, do not explicitly filter the signals in the audio domain, rather they perform a nonlinear mapping. Nevertheless, they were both successfully employed for MSS, which is a filtering problem. 

reduced receptive field. 

A-SPADE was introduced as a sparsity-based declipping algorithm that outperforms previous similar approaches [25]. For each time frame of the clipped signal y, it approximates a solution of the following problem: 



<!-- Start of picture text -->
minx,z ||z||0 s.t. x ∈ Γ(y) and ||F(x) − z||2 ≤ ϵ, (4)<br><!-- End of picture text -->

where z denotes the unknown discrete Fourier coefficients of each time frame and F the Fourier transform operator. Γ is defined as the feasible space of solutions (i.e., clipping consistency constraint). We included the algorithm in the evaluation of the declipping task as a baseline that delivers state-of-the-art performance [11,13]. 

## 5. EXPERIMENTS 

Our experiments focus on the following three scenarios: a) We conducted experiments on guitar recordings that were processed using the overdrive algorithm of the audio editing software SoX [10] (CEG-OD). b) We performed the same experiments as in the previous scenario while processing the same clean guitar recordings with hard-clipping (CEG-HC). c) We tested the systems on an extensive dataset comprising various hard-clipped sounds (SignalTrain-HC) to evaluate their performance against a popular declipping algorithm when the models are trained given an increase in the amount and variety of data. 

## 5.1 Data 

The models were trained on two different datasets to assess the distortion audio effect removal capabilities. The audio signals from a dataset that contains a single instrument class (e.g., electric guitar) exhibit consistent signal statistics. In order to restrict the statistics that need to be modeled in a first step, we chose to concentrate on dry guitar samples as target data. 

Since a large-scale, polyphonic dataset from clean electric guitar sounds is, to the best of our knowledge, not available<sup>2</sup> , we used an internal dataset, which we refer to as CEG (Clean Electric Guitar) dataset. The monaural data were gathered from various sources, mainly commercial audio loop packages and recordings of solo guitar, and has a duration of 1.68 h. All signals were re-sampled to a common sampling rate of 16 kHz in order to speed up convergence during training. To create the input dataset CEG-OD, the overdrive algorithm of SoX was applied to the data using five uniformly sampled gain levels in the range of γ ∈ [20, 50]dB. Likewise, the input dataset for the hard-clipping task, CEG-HC, was created using hardclipping (see (3)) with gain levels from the same distribution. Both datasets have a total length of 8.4 h. 

Although CEG represents a good source of data for our experiments due to its specificity of timbre, it remains a 

> 2 A publicly available guitar dataset for the recognition of audio effects exists (IDMT-SMT-Audio-Effects [26]). However, the dataset contains primarily homogeneous monophonic sounds and therefore, we choose to use the CEG dataset instead. 

220 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

limited resource in terms of size and variety. Before attempting to train a system to handle recordings in real environments (e.g., a commercial song), we need to investigate how the current models at our disposal handle the availability of more and diverse training data. For this purpose, we also performed experiments on the SignalTrain dataset, which consists of more than 24 h of music and randomly-generated test signals [27]. By applying hardclipping to these clean data using a uniformly-sampled input SDR value in the range SDRinp ∈ [1, 20]dB, we created SignalTrain-HC. During evaluation, we applied each input SDR in the set SDRinp ∈{1, 3, 5, 7, 10, 15, 20}dB to each sample in the test set. 

Each dataset was split into non-overlapping subsets for training (80%), validation (10%) and testing (10%). We evaluated the models on the test split. 

## 5.2 Experimental Setup 

During the supervised training procedure, Adam [28] was used as optimizer with initial learning rates according to the model’s original implementations. The learning rate was reduced by a factor of 10 after 150 epochs of no decrease in the validation loss. All models were optimized using the source-to-distortion ratio (SDR) between their full output sequences ˆx and the respective target sequences x in each batch B of N elements (not to be confused with the definition in the BSS_eval toolkit [29]): 



<!-- Start of picture text -->
LB(x, ˆx) = N 1 � 10 log10 �||xi|| 2 /||xi − xˆi|| 2� . (5)<br>i∈B<br><!-- End of picture text -->

We stopped all trainings after 1000 epochs. All models processed audio sequences that are randomly extracted from each clip in the dataset; the length of the extracted sequences is equal to 2 s (2.3 s for CRAFx due to its architecture). We used a batch size of 16 for all experiments. 



<!-- Start of picture text -->
Distorted<br>Demucs<br>Wave-U-Net<br>CRAFx<br>UMX<br>IRM<br>0 10 20 30 40 −4 −3 −2 −1 0<br>SI-SDR [dB] → PEAQ [ODG] →<br>Distorted<br>Demucs<br>Wave-U-Net<br>CRAFx<br>UMX<br>IRM<br>0.5 0.6 0.7 0.8 0.9 1.0 0 5 10 15 20<br>Rnonlin → ← FAD<br><!-- End of picture text -->

Figure 2. Box plot of scores for the CEG-OD dataset. The boxes show the first and third quartile of the data while the median is indicated with a line in the box. Higher scores indicate superior performance except for FAD. The results suggest that U-Net-based models performing convolutions in the time domain are the most promising approach to solving the task of overdrive removal. 

The R-nonlin metric [36], in contrast, was developed specifically for detecting nonlinear distortions and, like PEAQ, considers the human auditory system. Rnonlin is defined between 0 (high distortion) and 1 (no distortion). 

The Fréchet audio distance (FAD) was recently proposed as a reference-free evaluation metric for music enhancement algorithms. It has shown to correlate more with human perception than the SDR [37]. In order to obtain the FAD, the embedding statistics of both the whole clean and distorted test set are generated using a VGGish model [38]. The FAD is calculated based on the Fréchet distance between two multivariate Gaussians computed from both the test and the reference embeddings. [39]. 

## 6. RESULTS 

## 5.3 Objective Metrics 

In speech enhancement and source separation, the ubiquitous measure to estimate the quality of a system is the SDR. However, applying (2) to a signal does not retain its energy. Therefore, we follow the approach of [30]: the scale-invariant SDR (SI-SDR) is obtained by rescaling the target signal s such that the residual s − sˆ is orthogonal to s by using the optimal scaling factor ˆs<sup>T</sup> s/||s||<sup>2</sup> . 

An evaluation exclusively based on the objective similarity of the signals does not necessarily imply a correlation with human perception [31,32]. Accordingly, we observed that the SI-SDR scores occasionally disagreed with our qualitative evaluation. Therefore, we also considered three metrics based on human perception. 

The perceptual evaluation of audio quality (PEAQ) [33] is a widely used perceptual metric [11, 13, 34, 35] that measures the amount of degradation between two audio signals. The output of PEAQ is an Overall Difference Grade (ODG), which can reach values between 0 (imperceptible impairment) and −4 (very annoying impairment). Even though PEAQ is used in declipping and audio restoration studies [11,13,34], it was developed for audio codecs. 

In this section, we provide the results of the experiments introduced in the previous section. 

## 6.1 De-Overdrive (CEG-OD) 

Fig. 2 shows the results of the models that remove overdrive from guitar tracks. 

Firstly, in SI-SDR, both Demucs and Wave-U-Net perform exceptionally well and even outperform the idealratio-mask by more than 24 dB. While CRAFx yields considerably worse performance, it also surpasses the IRM oracle. UMX is the least performing of all the models in our comparison. It should be noted that for UMX, a model that operates on magnitude spectrograms, the IRM represents its upper limit in performance. 

Similar results are obtained with PEAQ, Rnonlin and FAD: while Demucs and Wave-U-Net yield the best scores and surpass the IRM, the ones for CRAFx and UMX are considerably worse. It seems that directly processing the signals in the time domain using a U-Net-based architecture represents the most promising approach for the removal of the overdrive effect. 

221 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
Distorted<br>Demucs<br>Wave-U-Net<br>CRAFx<br>UMX<br>A-SPADE<br>IRM<br>−5 0 5 10 15 20 −4 −3 −2 −1<br>SI-SDR [dB] → PEAQ [ODG] →<br>Distorted<br>Demucs<br>Wave-U-Net<br>CRAFx<br>UMX<br>A-SPADE<br>IRM<br>0.5 0.6 0.7 0.8 0.9 1.0 0 5 10 15 20 25<br>Rnonlin → ← FAD<br><!-- End of picture text -->

Figure 3. Box plot of scores for the CEG-HC dataset. It is difficult to clearly determine the best model, although Demucs represents a good compromise for all the metrics. 

## 6.2 Declipping (CEG-HC) 

Fig. 3 shows the results on the task of declipping on guitar recordings. Generally, we experienced a drop in the scores: now the models have been trained on declipping, which is an ill-posed problem, as missing parts of the signal need to be reconstructed. Additionally, we report scores for our declipping baseline, A-SPADE. 

Despite the general performance drop, Demucs surpasses the results of A-SPADE in terms of SI-SDR by almost 1 dB. While UMX and Wave-U-Net yield similar performances, CRAFx is the method with lowest scores. 

Regarding PEAQ, no method surpasses the IRM and the A-SPADE algorithm. As before, Demucs and Wave-U-Net have similar performance: while PEAQ slightly favors the latter, SI-SDR favors the former. In contrast to the previous results, CRAFx has no significant advantage over UMX. 

While Demucs achieves the best score for Rnonlin among the neural models, it does not surpass A-SPADE since the difference in their score is marginal. Interestingly, UMX achieves better results than CRAFx and WaveU-Net. As the Rnonlin metric was explicitly designed to detect nonlinear distortions, we conclude that UMX’ outputs contain fewer nonlinear distortions than the outputs of CRAFx and Wave-U-Net. 

Surprisingly, when computing the FAD, UMX outperforms all other methods, including A-SPADE. This might be accounted to the fact that the FAD is based on the mel spectrum, whereas UMX optimizes the magnitude spectrogram. While Demucs and CRAFx outperform A-SPADE in FAD as well, the score for Wave-U-Net is slightly worse. The FAD for the IRM is relatively small because the difference between the reference and test embeddings from the VGGish model can be traced back to the masking operation and quantization. Demucs seems to constitute a good compromise regarding performance since it yields first- or second-best results for all metrics. 

## 6.3 Declipping (SignalTrain-HC) 

Fig. 4 shows the results for declipping SignalTrain-HC. Due to the lower gains that are used to prepare the data 



<!-- Start of picture text -->
Distorted<br>Demucs<br>Wave-U-Net<br>UMX<br>A-SPADE<br>IRM<br>0 10 20 30 40 −4 −3 −2 −1 0<br>SI-SDR [dB] → PEAQ [ODG] →<br>Distorted<br>Demucs<br>Wave-U-Net<br>UMX<br>A-SPADE<br>IRM<br>0.6 0.8 1.0 0 1 2 3 4<br>Rnonlin → ← FAD<br><!-- End of picture text -->

Figure 4. Box plot of scores for the SignalTrain-HC dataset. Demucs can be regarded as the best model regarding the median score across all metrics. 

(see Sec. 5.1), the overall performance seems to be superior but cannot be directly compared to the previous results. Because of its considerably worse performance in the previous task, CRAFx was left out of the evaluation. 

Demucs surpasses all other models in SI-SDR, including IRM and A-SPADE. Moreover, Wave-U-Net and UMX both surpass A-SPADE but not the IRM. PEAQ gives a similar ranking of the methods: only UMX cannot reach the A-SPADE baseline. None of the neural methods surpasses the IRM. In terms of Rnonlin, the same ranking is obtained, with Demucs surpassing, Wave-U-Net reaching, and UMX just missing A-SPADE. The FAD highlights that UMX and Demucs deliver comparable performance, outperforming the baseline, but not surpassing the IRM. 

When only looking at SI-SDR or PEAQ, we notice the superiority of the time domain models. Future research should investigate whether the waveform in the time domain is the best input representation for the task, compared to, e.g., the real and imaginary part of a spectrogram [40] or both the waveform and the spectrogram [41]. Ultimately, Demucs can be considered the best model in our experiments for the task of declipping on SignalTrain. 

## 6.4 Discussion 

Qualitative Evaluation Although the abundance of evaluation metrics in the literature has the potential to analyze the results in very detailed ways, it does not always aid the judgement of which method is best given the individual context. Often, different applications have different requirements concerning the sound quality and can afford some types of distortions or artifacts to be left in the signal. Therefore, we report some qualitative considerations that need to be taken into account concerning our results, with the aim of finding some descriptive patterns among them. Fig. 5 shows spectrograms of a hard-clipped guitar signal and the outputs of all models under evaluation. 

We found that the characteristics of the artifacts that each model produces are consistent, independent from the task it is applied to. Nevertheless, for the time domainbased models, the artifacts are less prominent in the deoverdrive task. Here, Demucs often produces outputs that 

222 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
0.5<br>y x<br>0.0<br>−0.5<br>0.00 0.05 0.10 0.15 0.20<br>Time / s<br>Input Demucs Wave-U-Net CRAFx<br>5<br>0<br>Target IRM UMX A-SPADE<br>5<br>0<br>0.1 0.2 0.1 0.2 0.1 0.2 0.1 0.2<br>Time / s Time / s Time / s Time / s<br>Amplitude<br>/kHzFreq.<br>/kHzFreq.<br><!-- End of picture text -->

Figure 5. Spectrograms of a clipped guitar signal (γ = 45 dB), its target signal, and the output of each method. The respective time domain input and target signal are shown at the top. While all methods significantly reduce the harmonics, it can be observed that IRM and UMX smear the transients. A-SPADE relies on the strongest bins in the clipped spectrum, which leads to tonal artifacts. 

are virtually indistinguishable from the original signal. Generally, Demucs is the model that most often produces high quality results. Especially for inputs with a low amount of distortion, it can reconstruct the original sound without any perceptual artifact. Wave-U-Net behaves similarly, although it often cannot reach the same quality. 

UMX generally removes the distortion characteristics very well at the cost of strong phasing artifacts: Despite the absence of input distortions, the spectral features of the output are not necessarily consistent with the ones of the target. This is most likely due to UMX re-using the phase of the distorted input to reconstruct the signal in the time domain and the frame-wise processing. Moreover, Fig. 5 highlights that the transients are smeared by re-using the phase of the degraded signal. 

CRAFx does not suffer from phasing artifacts, but occasionally leaves part of the distortion features in the output. In some cases, the model fails to reconstruct the onset of some notes, penalizing the listening experience. 

Finally, A-SPADE is the model that exhibits the strongest and most frequent artifacts, especially for strongly clipped signals. Although it considers phase information by working in the complex frequency domain, it leads to non-optimal solutions. Nevertheless, distortion features (like those left by Demucs) or transient smearing (left by UMX) do not occur. 

Influence of the Dry Signal We have observed a substantial difference in performance between models that need to remove overdrive (CEG-OD dataset) and models that need to remove hard-clipping (CEG-HC dataset). The superior performance of the models trained and tested on CEG-OD can be mainly traced back to the presence of the non-distorted signal in the overdrive output and not to the soft-clipping character of the specific overdrive implemen- 

tation. We verified this hypothesis by training Wave-UNet on hard-clipped data superimposed with the clean signal (even when the amplitude of the clean signal is considerably low). We obtained results similar to those in the de-overdrive task (median results without superposition: SI-SDR = 7.2 dB, with superposition: SI-SDR = 34.4 dB). While the performance drop is present for all metrics, it is less pronounced for UMX which seems not to utilize the additional information in the signal. 

Inference Speed The benefits of Demucs in the context of declipping go beyond the quality of its outputs: using a neural approach also has advantages regarding inference speed. Inference with A-SPADE is comparably slow (real-time factor on CPU ×RT ∈ [4.2, 27.3] depending on SDRinp [13]), being an iterative approach that requires a computation of the Fourier transform and its inverse at each iteration. Demucs (×RT = 0.072), WaveU-Net (×RT = 0.113) and UMX (×RT = 0.026) instead, allow for fast inference on the CPU and even surpass realtime constraints independently on SDRinp without sacrificing the quality of the results. 

Evaluation Metrics The results highlight how our evaluation metrics focus on different aspects of the reconstructions: While SI-SDR measures differences between two audio signals in the time domain, PEAQ focuses on the perceptual quality without differentiating between degradation related to nonlinear distortions and artifacts/quality. In contrast, Rnonlin specifically highlights nonlinear distortions that have not been removed. Finally, FAD focuses primarily on the degradation that is observable in the mel spectrum. Hence, each metric proves beneficial in measuring specific aspects in the analysis of audio effect removal systems and can be advised for further investigations. 

## 7. CONCLUSION 

We showed that recovering the clean signal from clipped or overdriven audio signals can efficiently solved with neural networks designed for source separation. We found that Demucs achieves high quality according to the chosen evaluation metrics, especially when the distortion algorithm to be removed blends the distorted sound with the original one. This outcome highlights the potential of the proposed approach for other audio effects that mix dry and wet signals (e.g., parallel compression, reverberation, delay, modulation effects). 

Moreover, we showed that Demucs, Wave-U-Net, and UMX outperform one state-of-the-art declipping method on our test data. This outcome is promising, considering that the dataset to train such a system is potentially much larger than the size of the dataset we used. By discussing the results, we stressed the usefulness of multiple evaluation metrics suitable to assess distortion removal systems. 

Future work should include gathering more clean electric guitar data and generating a dataset using high-quality distortion emulations, which is required to improve generalization on real-world data. Furthermore, the knowledge from sparsity-based declipping algorithms could yield a valuable prior for declipping through DNNs. 

223 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

## 8. REFERENCES 

- [1] U. Zölzer, DAFX: digital audio effects, 2nd ed. Chichester, West Sussex, England: Wiley, 2011. 

- [2] R. Stables, B. De Man, and J. D. Reiss, ªTen years of automatic mixing,º in Proceedings of the 3rd Workshop on Intelligent Music Production, Salford, UK, 15 September 2017, 2017. 

- [3] M. A. Martínez-Ramírez, D. Stoller, and D. Moffat, ªA Deep Learning Approach to Intelligent Drum Mixing With the Wave-U-Net,º Journal of the Audio Engineering Society, vol. 69, no. 3, pp. 142±151, Mar. 2021. 

- [4] C. J. Steinmetz, J. Pons, S. Pascual, and J. Serra, ªAutomatic Multitrack Mixing With A Differentiable Mixing Console Of Neural Audio Effects,º in ICASSP 2021 - 2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). Toronto, ON, Canada: IEEE, Jun. 2021, pp. 71±75. 

- [5] Y. Mitsufuji, G. Fabbro, S. Uhlich, F.-R. Stöter, A. Défossez, M. Kim, W. Choi, C.-Y. Yu, and K.-W. Cheuk, ªMusic Demixing Challenge 2021,º Frontiers in Signal Processing, vol. 1, Jan. 2022. 

- [6] W. Choi, M. Kim, M. A. Martínez-Ramírez, J. Chung, and S. Jung, ªAMSS-Net: Audio Manipulation on User-Specified Sources with Textual Queries,º in Proceedings of the 29th ACM International Conference on Multimedia, Apr. 2021, pp. 1775±1783. 

- [7] Z. Raf **i** , A. Liutkus, F.-R. Stöter, S. I. Mimilakis, and R. Bittner, ªThe MUSDB18 corpus for music separation,º Dec. 2017. 

- [8] T. Wilmering, D. Moffat, A. Milo, and M. B. Sandler, ªA History of Audio Effects,º Applied Sciences, vol. 10, no. 3, p. 791, Jan. 2020. 

- [9] M. A. Martínez-Ramírez, E. Benetos, and J. Reiss, ªDeep Learning for Black-Box Modeling of Audio Effects,º Applied Sciences, vol. 10, p. 638, Jan. 2020. 

- [10] C. Bagwell, et al., ªSound eXchange (SoX),º Feb. 2015. 

- [11] P. Záviška, P. Rajmic, A. Ozerov, and L. Rencker, ªA Survey and an Extensive Evaluation of Popular Audio Declipping Methods,º IEEE Journal of Selected Topics in Signal Processing, vol. 15, no. 1, pp. 5±24, Jan. 2021. 

- [12] A. Janssen, R. Veldhuis, and L. Vries, ªAdaptive interpolation of discrete-time signals that can be modeled as autoregressive processes,º IEEE Transactions on Acoustics, Speech, and Signal Processing, vol. 34, no. 2, pp. 317±330, Apr. 1986. 

- [13] C. Gaultier, S. KitiÂc, R. Gribonval, and N. Bertin, ªSparsity-Based Audio Declipping Methods: Selected Overview, New Algorithms, and Large-Scale Evaluation,º IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 29, pp. 1174±1187, 2021. 

- [14] H. B. Kashani, M. M. Goodarzi, A. Jodeiri, and S. G. Firooz, ªImage to Image Translation based on Convolutional Neural Network Approach for Speech Declipping,º 4th Conference on Technology In Electrical and Computer Engineering (ETECH 2019), 2019. 

- [15] O. Ronneberger, P. Fischer, and T. Brox, ªU-Net: Convolutional Networks for Biomedical Image Segmentation,º in Medical Image Computing and ComputerAssisted Intervention ± MICCAI 2015, N. Navab, J. Hornegger, W. M. Wells, and A. F. Frangi, Eds. Cham: Springer International Publishing, 2015, pp. 234±241. 

- [16] W. Mack and E. A. P. Habets, ªDeclipping Speech Using Deep Filtering,º in 2019 IEEE Workshop on Applications of Signal Processing to Audio and Acoustics (WASPAA), Oct. 2019, pp. 200±204. 

- [17] T. Tanaka, K. Yatabe, M. Yasuda, and Y. Oikawa, ªAPPLADE: Adjustable Plug-and-Play Audio Declipper Combining DNN with Sparse Optimization,º in ICASSP 2022 - 2022 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). Singapore, Singapore: IEEE, May 2022, pp. 1011± 1015. 

- [18] M. A. Martínez-Ramírez, E. Benetos, and J. D. Reiss, ªA general-purpose deep learning approach to model time-varying audio effects,º in 22nd International Conference on Digital Audio Effects (DAFx-19), Jun. 2019. 

- [19] F.-R. Stöter, S. Uhlich, A. Liutkus, and Y. Mitsufuji, ªOpen-Unmix - A Reference Implementation for Music Source Separation,º Journal of Open Source Software, vol. 4, no. 41, p. 1667, Sep. 2019. 

- [20] S. Uhlich, M. Porcu, F. Giron, M. Enenkl, T. Kemp, N. Takahashi, and Y. Mitsufuji, ªImproving music source separation based on deep neural networks through data augmentation and network blending,º in 2017 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). New Orleans, LA: IEEE, Mar. 2017, pp. 261±265. 

- [21] S. Hochreiter and J. Schmidhuber, ªLong Short-Term Memory,º Neural Computation, vol. 9, no. 8, pp. 1735± 1780, Nov. 1997. 

- [22] A. Narayanan and D. Wang, ªIdeal ratio mask estimation using deep neural networks for robust speech recognition,º in 2013 IEEE International Conference on Acoustics, Speech and Signal Processing, 2013, pp. 7092±7096. 

- [23] D. Stoller, S. Ewert, and S. Dixon, ªWave-U-Net: A Multi-Scale Neural Network for End-to-End Audio Source Separation,º in Proceedings of the 19th ISMIR Conference, Paris, France, September 23-27, 2018, Paris, Jun. 2018. 

224 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

- [24] A. Défossez, N. Usunier, L. Bottou, and F. Bach, ªMusic Source Separation in the Waveform Domain,º arXiv:1911.13254 [cs, eess, stat], Apr. 2021. 

- [25] S. KitiÂc, N. Bertin, and R. Gribonval, ªSparsity and Cosparsity for Audio Declipping: A Flexible Non-convex Approach,º in Latent Variable Analysis and Signal Separation, E. Vincent, A. Yeredor, Z. Koldovský, and P. Tichavský, Eds. Cham: Springer International Publishing, 2015, pp. 243±250. 

- [26] M. Stein, J. Abeûer, C. Dittmar, and G. Schuller, ªAutomatic Detection of Audio Effects in Guitar and Bass Recordings,º in AES 128th Convention, London, UK, May 2010. 

- [27] S. H. Hawley, B. Colburn, and S. I. Mimilakis, ªSignalTrain: Profiling Audio Compressors with Deep Neural Networks,º in AES 147th Convention, May 2019. 

- [28] D. P. Kingma and J. Ba, ªAdam: A Method for Stochastic Optimization,º in 3rd International Conference on Learning Representations, {ICLR} 2015, San Diego, CA, USA, May 7-9, 2015, Conference Track Proceedings, 2015. 

- [29] E. Vincent, R. Gribonval, and C. Fevotte, ªPerformance measurement in blind audio source separation,º IEEE Transactions on Audio, Speech and Language Processing, vol. 14, no. 4, pp. 1462±1469, Jul. 2006. 

- [30] J. L. Roux, S. Wisdom, H. Erdogan, and J. R. Hershey, ªSDR ± Half-baked or Well Done?º in ICASSP 2019 - 2019 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). Brighton, United Kingdom: IEEE, May 2019, pp. 626±630. 

   - [35] J. You, U. Reiter, M. M. Hannuksela, M. Gabbouj, and A. Perkis, ªPerceptual-based quality assessment for audio±visual services: A survey,º Signal Processing: Image Communication, vol. 25, no. 7, pp. 482±501, Aug. 2010. 

   - [36] C.-T. Tan, B. C. J. Moore, N. Zacharov, and V.-V. Mattila, ªPredicting the Perceived Quality of Nonlinearly Distorted Music and Speech Signals,º Journal of the Audio Engineering Society, vol. 52, no. 7/8, pp. 699± 711, Jul. 2004. 

   - [37] K. Kilgour, M. Zuluaga, D. Roblek, and M. Sharifi, ªFréchet Audio Distance: A Reference-Free Metric for Evaluating Music Enhancement Algorithms,º in Interspeech 2019. ISCA, Sep. 2019, pp. 2350±2354. 

   - [38] S. Hershey, S. Chaudhuri, D. P. W. Ellis, J. F. Gemmeke, A. Jansen, R. C. Moore, M. Plakal, D. Platt, R. A. Saurous, B. Seybold, M. Slaney, R. J. Weiss, and K. Wilson, ªCNN Architectures for Large-Scale Audio Classification,º International Conference on Acoustics, Speech and Signal Processing (ICASSP), Jan. 2017. 

   - [39] D. Dowson and B. Landau, ªThe Fréchet distance between multivariate normal distributions,º Journal of multivariate analysis, vol. 12, no. 3, pp. 450±455, 1982. 

   - [40] W. Choi, M. Kim, J. Chung, D. Lee, and S. Jung, ªInvestigating U-Nets with various Intermediate Blocks for Spectrogram-based Singing Voice Separation,º in Proceedings of the 21th International Society for Music Information Retrieval Conference, Oct. 2020. 

   - [41] A. Défossez, ªHybrid Spectrogram and Waveform Source Separation,º in Proceedings of the ISMIR 2021 Workshop on Music Source Separation, Nov. 2021. 

- [31] E. Cano, D. FitzGerald, and K. Brandenburg, ªEvaluation of quality of sound source separation algorithms: Human perception vs quantitative metrics,º in 2016 24th European Signal Processing Conference (EUSIPCO). Budapest, Hungary: IEEE, Aug. 2016, pp. 1758±1762. 

- [32] V. Emiya, E. Vincent, N. Harlander, and V. Hohmann, ªSubjective and Objective Quality Assessment of Audio Source Separation,º IEEE Transactions on Audio, Speech, and Language Processing, vol. 19, no. 7, pp. 2046±2057, Sep. 2011. 

- [33] T. Thiede, W. C. Treurniet, R. Bitto, C. Schmidmer, T. Sporer, J. G. Beerends, and C. Colomes, ªPEAQ - The ITU Standard for Objective Measurement of Perceived Audio Quality,º Journal of the Audio Engineering Society, vol. 48, no. 1/2, pp. 3 EP ± 29, Feb. 2000. 

- [34] S. Lattner and J. Nistal, ªStochastic Restoration of Heavily Compressed Musical Audio Using Generative Adversarial Networks,º Electronics, vol. 10, no. 11, p. 1349, Jun. 2021. 

225 

