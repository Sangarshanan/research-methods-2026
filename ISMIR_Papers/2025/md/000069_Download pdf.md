---
paper_id: "000069"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706527/files/000069.pdf"
---

# INVESTIGATING AN OVERFITTING AND DEGENERATION PHENOMENON IN SELF-SUPERVISED MULTI-PITCH ESTIMATION 

Frank Cwitkowitz Zhiyao Duan 

Audio Information Research Lab, University of Rochester 

```
fcwitkow@ur.rochester.edu,zhiyao.duan@rochester.edu
```

## ABSTRACT 

Multi-Pitch Estimation (MPE) continues to be a sought after capability of Music Information Retrieval (MIR) systems, and is critical for many applications and downstream tasks involving pitch, including music transcription. However, existing methods are largely based on supervised learning, and there are significant challenges in collecting annotated data for the task. Recently, self-supervised techniques exploiting intrinsic properties of pitch and harmonic signals have shown promise for both monophonic and polyphonic pitch estimation, but these still remain inferior to supervised methods. In this work, we extend the classic supervised MPE paradigm by incorporating several self-supervised objectives based on pitch-invariant and pitch-equivariant properties. This joint training results in a substantial improvement under closed training conditions, which naturally suggests that applying the same objectives to a broader collection of data will yield further improvements. However, in doing so we uncover a phenomenon whereby our model simultaneously overfits to the supervised data while degenerating on data used for self-supervision only. We demonstrate and investigate this and offer our insights on the underlying problem. 

## 1. INTRODUCTION 

Pitch is a perceptual attribute of sound events that produce waves or harmonics that oscillate at integer multiples of a fundamental frequency (F0) [1]. Pitch is a foundational aspect of music, and it is often useful to represent musical content in terms of relationships between pitch (i.e., melody and harmony). In Music Information Retrieval (MIR) research, the task of detecting pitch activity and estimating the corresponding F0s within a polyphonic signal is known as Multi-Pitch Estimation (MPE) [2]. This is an important task with exciting applications in machine listening, human-computer interaction, and music databasing. Pitch estimation is also necessary for more high-level MIR tasks such as Automatic Music Transcription (AMT), where MPE is often performed in conjunction with the es- 

> © F. Cwitkowitz and Z. Duan. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: F. Cwitkowitz and Z. Duan, “Investigating an Overfitting and Degeneration Phenomenon in Self-Supervised Multi-Pitch Estimation”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

timation of note events. Currently, state-of-the-art MPE methods are heavily based on supervised machine learning techniques and require large amounts of rich and diverse training data with pitch annotations [3]. However, there are significant challenges with procuring multi-pitch annotations, especially for audio recordings comprising multiinstrument mixtures, difficult-to-annotate polyphonic instruments (e.g., guitar), or less common instruments. For this reason, such methods are unable to scale beyond the available datasets, which are generally homogeneous (e.g., solo piano) or limited in size (i.e., less than 10 hours). 

Several strategies have been proposed to mitigate such issues, including semi-supervision on data with weakly aligned annotations [4] or pre-training on mixtures of large-scale monophonic data [5]. However, these methods still fall within the supervised learning paradigm and as such are subject to the size and quality of the data and annotations. In parallel, there has also been work to build music foundation models that learn more general representations of music which can be transferred to downstream tasks [6, 7]. However, these representations still struggle to capture the level of granularity needed for low-level tasks like MPE. An alternative approach is to define taskspecific self-supervised objectives that encourage a model to respect properties of pitch, such as equivariance to pitch shifting and invariance to timbral transformations [8, 9]. These techniques have demonstrated remarkable success in learning to estimate pitch from unlabeled data and have also been generalized to polyphonic data [10]. 

In this work, we expand upon, refine, and integrate the techniques proposed in [10] into a supervised MPE framework resembling that of recent methods employing a convolutional neural network (CNN) [11–14] trained to estimate a multi-pitch salience-gram for an input spectrogram. We show these self-supervised objectives can significantly improve the performance of the supervised framework under a joint training paradigm. However, when attempting to apply the same objectives to additional data with no corresponding supervision, we observe a surprising phenomenon: self-supervision on the additional data does not improve performance but actually steers our model toward degeneration, i.e. blank pitch salience estimates, on such data. The model still exhibits the correct behavior on the validation set of the annotated dataset as well as evaluation data following a similar distribution. We demonstrate this issue and conduct several follow-up experiments in an attempt to identify and explain the underlying problem. 

596 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 2. FRAMEWORK 

In this section, we describe our feature extraction module, model architecture, and training objectives. Our methodology can be viewed as the integration of self-supervised techniques for MPE [10] into a supervised framework. 

## 2.1 Model & Features 

We adopt a modified version of the fully convolutional 2D autoencoder used in the Timbre-Trap framework [14]. This model comprises four encoder and decoder blocks with dilated convolutions, residual connections, and strided or transposed convolutions for resampling features across frequency. Although Timbre-Trap was proposed as a unified framework to perform transcription and reconstruction, we adopt only the base model and discard the latent feature used to switch between modes. We also insert layer normalization after the initial convolutional layer of both the encoder and decoder, after the strided and transposed convolution in each encoder and decoder block, and after the latent space convolution. Finally, we double the number of filters in each convolutional layer. 

We also replace the complex Constant-Q Transform (CQT) module used in the Timbre-Trap framework with calculation of Harmonic CQT<sup>1</sup> (HCQT) spectrograms [11] XH ∈ [0, 1]<sup>6×K×N</sup> with K = 440 frequency bins starting from fmin = 27.5 Hz and 5 bin per semitone resolution. Input audio is resampled to 22, 050 Hz, and N is the number frames using a hop size of 256 samples. We maintain the original set of harmonics H = {0.5, 1, 2, 3, 4, 5}. The main advantage of the HCQT is its capacity to index harmonic energy across the channel dimension. This structure is perfectly suited for convolutional layers and establishes a strong inductive bias for pitch estimation. One consequence of our model, denoted by F(·), is the resulting shared dimensionality between XH and predictions Y<sup>ˆ</sup> = F (XH), which ideally represent multi-pitch salience-grams. This makes it convenient to formulate the self-supervised techniques proposed in Sec. 2.3. Note that this configuration of model and features is very similar to what was used in the SS-MPE framework [10]. 

## 2.2 Supervised Training 

Given the ground-truth pitch activations Y ∈ [0, 1]<sup>K×N</sup> corresponding to XH, a supervised loss can be defined as 



<!-- Start of picture text -->
N −1 K−1<br>Lspv = N 1 � � B�Yˆ [k, n], �Y [k, n]� , (1)<br>n=0 k=0<br><!-- End of picture text -->

where B(·, ·) represents binary cross-entropy (BCE) loss and Y<sup>�</sup> represents the target multi-pitch salience-gram for XH. Following [11], we blur each frame of Y using a Gaussian kernel with σ = <mark>1</mark> 5<sup>semitones(1bin)toobtain</sup> Y� . Minimization of Lspv represents the classic training objective for supervised MPE and is used as the primary training signal within our framework. 

> 1 As in [10], a variable Q-factor [15] is employed for improved computational efficiency and increased time resolution at lower frequencies. 

## 2.3 Self-Supervised Techniques 

## 2.3.1 Invariance & Equivariance Objectives 

We further define two classes of self-supervised objectives, adapted from [10], based on pitch-invariant and pitchequivariant properties. Under our framework, these objectives are meant to encourage the model to implicitly encode various properties of pitch. A pitch-invariant transformation tiv(·) performs some manipulation of XH that ideally should not affect the predicted multi-pitch saliencegram Y<sup>ˆ</sup> . These transformations can be used to formulate invariance-based losses of the form 



<!-- Start of picture text -->
N −1 K−1<br>Liv = N 1 � � B�F (tiv(XH))[k, n], Y ˆ  [k, n]� . (2)<br>n=0 k=0<br><!-- End of picture text -->

While the relative strength of energy at harmonic frequencies is primarily what influences timbre, pitch is determined by an actual or implied F0. As such, we simulate pitch-invariant timbral transformations tiv−t by applying random parabolic equalization curves u[k] = 1 − 2α(k − β)<sup>2</sup> [16], where β ∈ [0, K − 1] and α ∈ [0, (K− <mark>1</mark> 1)<sup>2</sup><sup><mark>]</mark></sup> are sampled uniformly, to each frame and channel of XH, to define a timbre-invariance loss Liv−t. Similarly, there is no discernible pitch associated with non-harmonic sounds, which nonetheless make up an important aspect of music (i.e., percussion). As such, we create musicallyrelevant pitch-invariant transformations tiv−p by randomly sampling and superimposing percussive audio from the Expanded Groove MIDI Dataset (E-GMD) [17] (at the waveform-level) with volume v ∈ [0, 1], sampled uniformly, to define a percussion-invariance loss Liv−p. 

Conversely, a pitch-equivariant transformation tev(·) performs some manipulation of XH that ideally should correspond to a parallel manipulation of the predicted multi-pitch salience-gram Y<sup>ˆ</sup> . These transformations can be used to formulate equivariance-based losses of the form 



<!-- Start of picture text -->
N −1 K−1<br>Lev = N 1 � � B�F (tev(XH))[k, n], tev�Yˆ [k, n]�� .<br>n=0 k=0<br>(3)<br><!-- End of picture text -->

The HCQT spectrograms fed into our model and the corresponding expected multi-pitch salience-grams have an equivariant relationship for various geometric transformations. These include vertical translations, which correspond to a pitch shift of<sup><mark>∆</mark></sup> 5<sup><mark>k</mark></sup> semitones, horizontal trans- <mark>4∆n</mark> lations, which correspond to a time delay of N seconds, and horizontal stretching, which corresponds to a speed-up by a factor of γ. We perform random pitchequivariant transformations tev−g with uniformly sampled ∆k ∈ [−boct, boct] bins, ∆n ∈ [ <mark>−</mark><sup><mark>N</mark></sup> 4<sup><mark>,N</mark></sup> 4<sup><mark>]</mark>frames, and γ∈</sup> [0.5, 2]<sup>2</sup> to define a geometric-equivariance loss Lev−g. 

While all of these invariance and equivariance properties can be learned implicitly to some degree through a supervised objective or fully convolutional inductive bias, an explicit training signal can lead to less overfitting. Moreover, these techniques can broaden the training data and introduce previously unseen elements such as percussion. 

> 2 Sampled uniformly from [0.5, 1] and [1, 2] in equal proportion. 

597 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 2.3.2 Energy-Based Stimulus 

Objectives based on the losses from Sec. 2.3.1 can be vulnerable to trivial solutions, e.g. uniformly inactive or active multi-pitch salience-grams. One way to protect against such degeneration is to inject some sort of energy-based stimulus. The ground-truth and its derivative Y<sup>�</sup> are one form of stimulus that can prevent collapse, but of course they are not always available. In lieu of ground-truth, a loss leveraging energy-based targets can be formulated as 



<!-- Start of picture text -->
N −1 K−1<br>Leg = N 1 � � B�Yˆ [k, n], X�[k, n]� , (4)<br>n=0 k=0<br><!-- End of picture text -->

where X<sup>�(lin)</sup> =<sup>�5</sup> h=1 h <mark>1</mark><sup>4</sup><sup><mark>X</mark></sup> h<sup>(lin)</sup> represents a weighted average of XH across harmonic channels, computed in linear-scale and converted to decibel-scale. Note that (4) is a simplification of the harmonic and support loss used originally in [14]. While this loss will protect against trivial solutions, the target X<sup>�</sup> [k, n] by nature is quite coarse and contains many false alarms (see [14]). A simple improvement is to induce sparsity through another loss: 



<!-- Start of picture text -->
N −1 K−1<br>Lspr = N 1 � � ���Yˆ [k, n]��� . (5)<br>n=0 k=0<br><!-- End of picture text -->

In practice, Leg and Lspr, if computed at all, are coupled and computed only for predictions without ground-truth. 

## 3. EXPERIMENTS 

In this section, we detail our experimental setup and our initial investigation into the joint training paradigm. 

## 3.1 Training & Evaluation Details 

We train and validate the model in each experiment on URMP [18] following the splits proposed in [3]. Training is conducted on batches of 4 second excerpts using AdamW optimizer [19] with batch size 8 and learning rate 0.0005 for the encoder and 0.00025 for the decoder. Only one excerpt per track is sampled over the course of each epoch. In experiments with self-supervision on additional data, the batch size is expanded to accommodate extra samples without reducing the amount of supervision. The supervised objective (1) is computed and averaged across supervised samples, whereas the self-supervised objectives (2-5) are computed and averaged across all samples within each batch. Since (1-4) are formulated using BCE, they all operate on roughly the same numerical scale. Learning rate warmup is applied over the first 100 epochs of training, and gradient clipping with an L2-norm of 1.0 is applied to improve training stability. The final model for each experiment is chosen as the checkpoint with the maximum F1-score on the validation set across 2500 epochs. 

We evaluate on several MPE and AMT datasets, including Bach10 [20], Su [21], TRIOS [22], the ten-track test set of MusicNet [23], and GuitarSet [24]. We utilize the community-standard `mir_eval` package [25] to compute precision (P ), recall (R), and f1-score (F1 ). Multi-pitch 

estimates are generated by performing local peak-picking on the output multi-pitch salience-grams and thresholding at 0.5. The final results are computed by averaging across all tracks within an individual dataset. 

## 3.2 Baselines 

We compare results for our experiments to several supervised CNN-based approaches to MPE. Deep-Salience [11] feeds an HCQT spectrogram with harmonics H and 5 bins per semitone into several convolutional layers to produce a multi-pitch salience-gram. It is functionally similar to our framework under a supervised-only setting. The model was trained on a private subset of multitrack mixtures (including percussion) from MedleyDB [26]. BasicPitch [12] is similar to Deep Salience, performing MPE at 3 bins per semitone, but employs a more shallow network and further estimates pitch and onset activations at 1 bin per semitone to generate note predictions. The input to the model is an approximation of the HCQT.<sup>3</sup> Data augmentation techniques including additive noise, equalization, and reverb simulation are also utilized. The model was trained on portions of several medium-to-large-sized datasets, including GuitarSet [24]. PUnet:XL [13] is a method drawing inspiration from the idea of pre-stacking AMT models with a U-Net [27]. It processes fixed-length windows of a 6-octave HCQT with harmonics H and 3 bins per semitone, and makes predictions at 1 bin per semitone. The model is trained on MusicNet [23] and incorporates an auxiliary task of degree-of-polyphony estimation at the latent layer and data augmentation techniques including transposition (similar to our geometric-equivariance objective), tuning manipulation, additive noise, and equalization following [16]. Timbre-Trap [14] is a 2D autoencoder designed to perform MPE and audio synthesis jointly based on a simple conditioning mechanism at the latent space. The backbone architecture is nearly identical to that of our framework, barring the modifications noted in Sec. 2.1. However, in the original framework the model received both the real and imaginary part (as separate channels) of an invertible complex CQT [28] as input. Timbre-Trap was trained on URMP [18] following the same splits used in this work. We follow the same post-processing steps described in Sec. 3.1 to evaluate the baseline models,<sup>4</sup> and provide the results at the top of Table 1. 

## 3.3 Joint Training Paradigm 

We first conduct an initial set of experiments evaluating the invariance- and equivariance-based self-supervised objectives under closed training conditions on URMP [18]. In particular, we experiment with the supervised objective in isolation, the supervised objective with each invarianceand equivariance-based objective independently, and all of these objectives together: Ltotal = Lspv + Liv−t + Liv−p + Lev−g. The results are given at the bottom of Table 1. The first thing to note is that overall our framework 

> 3 Note that Basic-Pitch utilizes 7 harmonics and a sub-harmonic. 

> 4 Adopting the original hyperparameters, we threshold Deep-Salience and Basic-Pitch at 0.3, and PUnet:XL (without peak-picking) at 0.4. 

598 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

Table 1. Comparison of precision (P ), recall (R), and f1-score (F1 ) (in percentage points) over several MPE and AMT datasets for baseline methods<sup>*</sup> and ex <mark>p</mark> eriments conducted usin <mark>g</mark> the <mark>p</mark> ro <mark>p</mark> osed framework with self-su <mark>p</mark> ervised ob <mark>j</mark> ectives. 

|||Bach10|||Su|||TRIOS|||MusicNe|t||GuitarSe|t|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Method|P|R|F1|P|R|F1|P|R|F1|P|R|F1|P|R|F1|
|Deep-Salience [11]|86.0|61.0|71.3|74.1|47.9|57.1|92.3|39.4|54.2|63.0|48.1|53.3|77.7|70.6|72.2|
|Basic-Pitch [12]|90.2|75.7|82.2|54.2|44.1|47.5|88.2|44.2|57.9|50.6|42.1|45.7|80.9|75.9|77.7|
|PUnet:XL [13]|88.2|77.6|82.5|76.2|69.8|71.8|89.6|51.3|64.8|77.6|67.6|72.0|74.7|55.2|62.4|
|Timbre-Trap [14]|81.2|84.2|82.6|52.1|53.0|51.4|69.4|49.7|56.8|44.1|57.3|48.7|48.6|75.6|58.0|
|Lspv|88.8|83.1|85.8|61.0|47.7|52.1|82.7|48.0|59.4|53.8|54.7|53.6|70.2|72.9|69.8|
|Lspv +Liv−t|88.5|81.7|84.9|62.5|47.1|52.3|84.4|46.4|58.8|54.9|54.3|53.9|75.4|70.1|70.6|
|Lspv +Liv−p|88.0|84.1|85.9|57.3|52.5|53.4|81.0|50.1|60.6|50.4|58.9|53.8|70.9|78.0|73.2|
|Lspv +Lev−g|91.5|88.6|90.0|64.9|62.9|62.9|90.7|57.9|69.8|58.0|62.9|59.8|79.7|80.4|79.3|
|Ltotal (`Ref.`)|92.1|88.0|90.0|65.0|65.0|64.1|91.0|58.4|70.2|55.8|65.1|59.6|80.5|82.3|80.9|



> * Grayed values indicate a portion of the test data was used for training. 

under the supervised-only setting achieves results comparable to or better than each of the baselines for several datasets. This is especially true with respect to TimbreTrap [14], which is arguably the most comparable due to its similar architecture and identical training data. However, PUnet:XL [13] appears to offer a significant advantage for AMT datasets (i.e., Su, TRIOS, and MusicNet) since it was trained on such data to predict pitch directly at the notelevel. Next, we can observe that each self-supervised objective has the potential to improve performance on one or more datasets. The timbre-invariance objective is least effective and has a mixed effect across datasets, which is somewhat contrary to what has been observed under the fully self-supervised context [10]. It is possible that the property of timbre-invariance is already strongly indicated by the supervised objective. The percussion-invariance objective is moderately beneficial, even for some datasets without percussion. Out of all the evaluation datasets, there is only one track in TRIOS [22] that has percussion. However, even non-percussive audio can have percussive elements, i.e. originating from playing notes on certain instruments. The geometric-equivariance objective is most effective and yields a significant improvement across all datasets. This is likely due to the model capturing harmonic relationships explicitly and efficiently by leveraging the shift-invariance exhibited by the HCQT representation. Combining the supervised objective with all invarianceand equivariance-based objectives produces the best performance, suggesting that each contributes distinctly to robustness. Given that our framework was trained with such a small of amount of audio (i.e., 1-2 hours), these results are quite remarkable, especially when considering performance on data unseen during training (i.e., GuitarSet). 

## 3.4 Self-Supervision on Additional Data 

Given the success with integrating self-supervised objectives into our supervised framework, it is reasonable to question whether the same objectives could be applied to more general music datasets lacking multi-pitch annotations. Indeed, training a model to maintain pitch-invariant and pitch-equivariant properties over a broader collection 

of data could be one potential way to circumvent issues with low data availability for MPE. In this vein, we conduct additional experiments under the joint training paradigm where additional data is included in each batch for selfsupervision only. Specifically, we repeat the experiment combining all objectives (denoted `Ref.` ), but with an additional 16 samples per batch which only influence the invariance- and equivariance-based losses. The datasets we use for additional samples represent different music domains, i.e., simple synthetic monophonic data (NSynth [29]), recordings of classical music mixtures (MusicNet [23]), and high-quality production-level audio (FMA [30]). We extract samples from the training splits of NSynth and MusicNet, and the large (30-second clip) variant of FMA. 

Surprisingly, these experiments all exhibit undesirable behavior: performance for the URMP [18] remains stable and consistent with experiments from Sec. 3.3, but performance for the other datasets collapses. The performance at validation checkpoints over the course of training is presented in Fig. 1. Upon closer inspection, we found that the model predictions degenerate to a trivial solution (blank predictions) for all datasets except for URMP. As such, we repeated each experiment with the energy-based objectives (+EG) from Sec. 2.3.2 on the data used for selfsupervision. Although this does prevent collapse, it ultimately still leads to degraded performance. Finally, we experiment with initializing the model with the weights from the best validation checkpoint of `Ref.` and fine-tuning with<sup><mark>1</mark></sup> 5<sup>the learning rate (-FT). However, the two-stage fine-</sup> tuning paradigm still exhibits the same behavior. 

## 4. DISCUSSION 

In this section, we investigate the phenomenon uncovered in Sec. 3.4 further and conduct several follow-up experiments in an effort to identify the underlying problem. 

## 4.1 Overfitting & Degeneration 

In order to illustrate and characterize the problem of degeneration, Fig. 2 shows predictions for a single sample from `Ref.` along with predictions for the same sample at 25%, 50%, and 75% of the full duration of fine-tuning on 

599 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
URMP Bach10 Su<br>1. 0 1. 0 1. 0<br>0. 8 0. 8 0. 8<br>0. 6 0. 6 0. 6<br>0. 4 0. 4 0. 4<br>0. 2 0. 2 0. 2<br>0. 0 0. 0 0. 0<br>0 2000 4000 6000 8000 10000 0 2000 4000 6000 8000 10000 0 2000 4000 6000 8000 10000<br># Batches # Batches # Batches<br>TRIOS MusicNet GuitarSet<br>1. 0 1. 0 1. 0<br>0. 8 0. 8 0. 8<br>0. 6 0. 6 0. 6<br>0. 4 0. 4 0. 4<br>0. 2 0. 2 0. 2<br>0. 0 0. 0 0. 0<br>0 2000 4000 6000 8000 10000 0 2000 4000 6000 8000 10000 0 2000 4000 6000 8000 10000<br># Batches # Batches # Batches<br>Ref. +NS-16 +NS-16+EG +MN-16 +MN-16+EG +MN-16-FT +FMA-16 +FMA-16+EG +FMA-16-FT<br>-ScoreF1 -ScoreF1 -ScoreF1<br>-ScoreF1 -ScoreF1 -ScoreF1<br><!-- End of picture text -->

Figure 1. Performance over the course of training for experiments leveraging an additional 16 samples per batch from NSynth [29], MusicNet [23], and FMA [30] for self-supervision. EG - Energy-based objectives. FT - Fine-tuning scheme. 



<!-- Start of picture text -->
Ground-Truth Ref. +FMA-16-FT@2500 +FMA-16-FT@5000 +FMA-16-FT@7500<br><!-- End of picture text -->

Figure 2. Ground-truth, baseline, and intermediate predictions at 25%, 50%, and 75% of the duration of the experiment with additional self-supervision on FMA [30] under fine-tuning scheme for track `01-AchGottundHerr` of Bach10 [20]. 

FMA. It can clearly be seen that the strength of predictions (i.e., recall) decreases over time, indicating that there is a trend towards a trivial solution. This also suggests that for the regular experiments without fine-tuning, the model is always struggling to move past the trivial solution. 

Next, to examine whether the role of self-supervised learning was too extreme, we repeat the MusicNet [23] experiments with an exponentially decreasing amount of samples for self-supervision only (i.e., with 8, 4, and 2 additional samples). The performance of these experiments at validation checkpoints is plotted in Fig. 3. Interestingly, there is a noticeable relationship between the amount of samples for self-supervision only and the severity of degeneration. Moreover, the degeneration on MusicNet [23] itself is quite prominent and also exhibits this relationship. 

## 4.2 Training Distributions 

In order to see whether there is an issue regarding mismatch between the distribution of the data used for supervision and that of the data used for self-supervision only, we further extract 10 samples from the URMP [18] training set spanning multiple degrees of polyphony. We denote this split as URMP-T2 and the remainder as URMPT1. We then re-run the reference experiment using only URMP-T1 for training, and then again with additional selfsupervised learning and no corresponding supervision on 

URMP-T2. For completeness, we further run this experiment applying the energy-based objectives to URMP-T2. The performance for these experiments is plotted in Fig. 4. 

Relative to `Ref.` , performance barely decreases when only URMP-T1 is used for training, which is quite interesting by itself. More importantly, when conducting additional self-supervision on the 10 samples of URMPT2, which follow a very similar distribution to URMP-T1, there is still a moderate decrease in performance. The only difference between these two experiments is that each of the self-supervised losses are averaged over the samples from both URMP-T1 and URMP-T2 for each batch instead of only URMP-T1. It is worth noting that the collapse here happens to be less extreme than when training with selfsupervision on other datasets with more samples (see Fig. 3). Furthermore, the degradation on URMP and Bach10 is actually more extreme than what we observed when training on NSynth (+NS-16), but we note that this could also be explained by less supervision on URMP. Another interesting observation is that the energy-based objectives actually further degrade performance, likely due to conflicting with the supervised objective on the same distribution. 

## 4.3 Mitigating Degeneration 

Given all of our observations, it appears the underlying issue is too strong of a pull towards the trivial solution for the 

600 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
URMP Bach10 Su<br>1. 0 1. 0 1. 0<br>0. 8 0. 8 0. 8<br>0. 6 0. 6 0. 6<br>0. 4 0. 4 0. 4<br>0. 2 0. 2 0. 2<br>0. 0 0. 0 0. 0<br>0 2000 4000 6000 8000 10000 0 2000 4000 6000 8000 10000 0 2000 4000 6000 8000 10000<br># Batches # Batches # Batches<br>TRIOS MusicNet GuitarSet<br>1. 0 1. 0 1. 0<br>0. 8 0. 8 0. 8<br>0. 6 0. 6 0. 6<br>0. 4 0. 4 0. 4<br>0. 2 0. 2 0. 2<br>0. 0 0. 0 0. 0<br>0 2000 4000 6000 8000 10000 0 2000 4000 6000 8000 10000 0 2000 4000 6000 8000 10000<br># Batches # Batches # Batches<br>Ref. +MN-16 +MN-8 +MN-4 +MN-2 +MN-16+EG +MN-16-FT<br>-ScoreF1 -ScoreF1 -ScoreF1<br>-ScoreF1 -ScoreF1 -ScoreF1<br><!-- End of picture text -->

Figure 3. Performance over the course of training for experiments varying amount of self-supervision on MusicNet [23]. 



<!-- Start of picture text -->
URMP Bach10 Su<br>1. 0 1. 0 1. 0<br>0. 8 0. 8 0. 8<br>0. 6 0. 6 0. 6<br>0. 4 0. 4 0. 4<br>0. 2 0. 2 0. 2<br>0. 0 0. 0 0. 0<br>0 1000 2000 3000 4000 5000 6000 7000 0 1000 2000 3000 4000 5000 6000 7000 0 1000 2000 3000 4000 5000 6000 7000<br># Batches # Batches # Batches<br>TRIOS MusicNet GuitarSet<br>1. 0 1. 0 1. 0<br>0. 8 0. 8 0. 8<br>0. 6 0. 6 0. 6<br>0. 4 0. 4 0. 4<br>0. 2 0. 2 0. 2<br>0. 0 0. 0 0. 0<br>0 1000 2000 3000 4000 5000 6000 7000 0 1000 2000 3000 4000 5000 6000 7000 0 1000 2000 3000 4000 5000 6000 7000<br># Batches # Batches # Batches<br>Ref. T1 T1/T2 T1/T2+EG<br>-ScoreF1 -ScoreF1 -ScoreF1<br>-ScoreF1 -ScoreF1 -ScoreF1<br><!-- End of picture text -->

Figure 4. Performance over the course of training for experiments which use a reduced portion (T1) of our URMP [18] training set for supervised training with additional self-supervision on the remaining 10 non-overlapping samples (T2). 

non-supervised data, irrespective of its distribution. As it stands, self-supervision without corresponding supervision essentially pushes the model to degenerate on data following a certain distribution. If the distribution of data used for self-supervision is close to that of the supervised data, it will by extension hurt performance on the supervised data. If the distribution of data used for self-supervision is distinct from that of the supervised data, it will have less of an effect on the performance for data outside the distribution. It is unclear whether these interactions would persist if larger and more diverse data were used for supervision. 

Degeneration also seems to be unique to MPE, since self-supervised methods for monophonic pitch estimation [8,9] rely on the inductive bias of monophony and formulate their objectives using categorical cross-entropy. A solution for the polyphonic setting may require some sort of objective that enforces the existence of content in the predictions, to protect against the trivial solution. The energybased objectives are one such protection, but they evidently remove too much flexibility and lead to worse predictions. 

Despite these current challenges, we still believe that selfsupervised learning holds promise for advancing MPE. 

## 5. CONCLUSION 

We have demonstrated that self-supervised objectives can substantially improve upon the standard supervised training paradigm for MPE. However, in attempting to extend self-supervised learning beyond the distribution of data that is already grounded with supervised learning, we encounter issues whereby our model simultaneously overfits to the distribution of the supervised training data while degenerating on the distribution of the self-supervised training data. Self-supervised objectives utilizing energy-based targets can protect against degeneration, but these are too inflexible. Fine-tuning cannot circumvent the problem either. Moreover, we show that degeneration persists even when the supervised and self-supervised training data are taken from the same distribution. We conclude with several remarks and ideas toward overcoming highlighted issues. 

601 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 6. ACKNOWLEDGMENTS 

This work is supported by National Science Foundation (NSF) grant No. 2222129 and synergistic activities funded by NSF grant DGE-1922591. 

## 7. REFERENCES 

- [1] M. Müller, Fundamentals of Music Processing: Audio, Analysis, Algorithms, Applications. Springer, 2015. 

- [2] E. Benetos, S. Dixon, Z. Duan, and S. Ewert, “Automatic music transcription: An overview,” IEEE Signal Processing Magazine, vol. 36, no. 1, pp. 20–30, 2019. 

- [3] J. Gardner, I. Simon, E. Manilow, C. Hawthorne, and J. Engel, “MT3: Multi-task multitrack music transcription,” in Proceedings of ICLR, 2021. 

- [4] B. Maman and A. H. Bermano, “Unaligned supervision for automatic music transcription in the wild,” in Proceedings of ICML, 2022. 

- [5] I. Simon, J. Gardner, C. Hawthorne, E. Manilow, and J. Engel, “Scaling polyphonic transcription with mixtures of monophonic transcriptions,” in Proceedings of ISMIR, 2022. 

- [6] Y. Li, R. Yuan, G. Zhang, Y. Ma, X. Chen, H. Yin, C. Lin, A. Ragni, E. Benetos, N. Gyenge et al., “MERT: Acoustic music understanding model with large-scale self-supervised training,” in Proceedings of ICLR, 2024. 

- [7] W. Liao, Y. Takida, Y. Ikemiya, Z. Zhong, C.-H. Lai, G. Fabbro, K. Shimada, K. Toyama, K. Cheuk, M. A. Martínez-Ramírez et al., “Music foundation model as generic booster for music downstream tasks,” arXiv preprint arXiv:2411.01135, 2024. 

- [8] B. Gfeller, C. Frank, D. Roblek, M. Sharifi, M. Tagliasacchi, and M. Velimirovi´c, “SPICE: Selfsupervised pitch estimation,” IEEE/ACM Transactions on Audio, Speech, and Language Processing (TASLP), vol. 28, pp. 1118–1128, 2020. 

- [9] A. Riou, S. Lattner, G. Hadjeres, and G. Peeters, “PESTO: Pitch estimation with self-supervised transposition-equivariant objective,” in Proceedings of ISMIR, 2023. 

- [10] F. Cwitkowitz and Z. Duan, “Toward fully selfsupervised multi-pitch estimation,” arXiv preprint arXiv:2402.15569, 2024. 

- [11] R. M. Bittner, B. McFee, J. Salamon, P. Li, and J. P. Bello, “Deep salience representations for F0 estimation in polyphonic music,” in Proceedings of ISMIR, 2017. 

- [12] R. M. Bittner, J. J. Bosch, D. Rubinstein, G. MeseguerBrocal, and S. Ewert, “A lightweight instrumentagnostic model for polyphonic note transcription and multipitch estimation,” in Proceedings of ICASSP, 2022. 

- [13] C. Weiß and G. Peeters, “Comparing deep models and evaluation strategies for multi-pitch estimation in music recordings,” IEEE/ACM Transactions on Audio, Speech, and Language Processing (TASLP), vol. 30, pp. 2814–2827, 2022. 

- [14] F. Cwitkowitz, K. W. Cheuk, W. Choi, M. A. MartínezRamírez, K. Toyama, W.-H. Liao, and Y. Mitsufuji, “Timbre-Trap: A low-resource framework for instrument-agnostic music transcription,” in Proceedings of ICASSP, 2024. 

- [15] C. Schörkhuber, A. Klapuri, N. Holighaus, and M. Dörfler, “A matlab toolbox for efficient perfect reconstruction time-frequency transforms with logfrequency resolution,” in Proceedings of AES, 2014. 

- [16] J. Abeßer and M. Müller, “Jazz bass transcription using a U-net architecture,” Electronics, vol. 10, no. 6, p. 670, 2021. 

- [17] L. Callender, C. Hawthorne, and J. Engel, “Improving perceptual quality of drum transcription with the expanded groove MIDI dataset,” arXiv preprint arXiv:2004.00188, 2020. 

- [18] B. Li, X. Liu, K. Dinesh, Z. Duan, and G. Sharma, “Creating a multitrack classical music performance dataset for multimodal music analysis: Challenges, insights, and applications,” IEEE Transactions on Multimedia, vol. 21, pp. 522–535, 2018. 

- [19] I. Loshchilov and F. Hutter, “Decoupled weight decay regularization,” in Proceedings of ICLR, 2019. 

- [20] Z. Duan, B. Pardo, and C. Zhang, “Multiple fundamental frequency estimation by modeling spectral peaks and non-peak regions,” IEEE Transactions on Audio, Speech, and Language Processing (TASLP), vol. 18, no. 8, pp. 2121–2133, 2010. 

- [21] L. Su and Y.-H. Yang, “Escaping from the abyss of manual annotation: New methodology of building polyphonic datasets for automatic music transcription,” in Proceedings of CMMR, 2015. 

- [22] J. Fritsch, “High quality musical audio source separation,” Master’s thesis, UPMC / IRCAM / Telécom ParisTech, 2012. 

- [23] J. Thickstun, Z. Harchaoui, and S. Kakade, “Learning features of music from scratch,” in Proceedings of ICLR, 2017. 

- [24] Q. Xi, R. M. Bittner, J. Pauwels, X. Ye, and J. P. Bello, “GuitarSet: A dataset for guitar transcription,” in Proceedings of ISMIR, 2018. 

- [25] C. Raffel, B. McFee, E. J. Humphrey, J. Salamon, O. Nieto, D. Liang, and D. P. Ellis, “mir_eval: A transparent implementation of common MIR metrics,” in Proceedings of ISMIR, 2014. 

602 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [26] R. M. Bittner, J. Salamon, M. Tierney, M. Mauch, C. Cannam, and J. P. Bello, “MedleyDB: A multitrack dataset for annotation-intensive MIR research.” in Proceedings of ISMIR, 2014. 

- [27] F. Pedersoli, G. Tzanetakis, and K. M. Yi, “Improving music transcription by pre-stacking a U-Net,” in Proceedings of ICASSP, 2020. 

- [28] N. Holighaus, M. Dörfler, G. A. Velasco, and T. Grill, “A framework for invertible, real-time constant-Q transforms,” IEEE Transactions on Audio, Speech, and 

Language Processing (TASLP), vol. 21, pp. 775–785, 2012. 

- [29] J. Engel, C. Resnick, A. Roberts, S. Dieleman, M. Norouzi, D. Eck, and K. Simonyan, “Neural audio synthesis of musical notes with wavenet autoencoders,” in Proceedings of ICML, 2017. 

- [30] M. Defferrard, K. Benzi, P. Vandergheynst, and X. Bresson, “FMA: A dataset for music analysis,” in Proceedings of ISMIR, 2017. 

603 

