---
paper_id: "000002"
year: 2022
title: "Download pdf"
source_url: "https://zenodo.org/record/7342730/files/000002.pdf"
---

# TOWARD POSTPROCESSING-FREE NEURAL NETWORKS FOR JOINT BEAT AND DOWNBEAT ESTIMATION 

Tsung-Ping Chen Li Su Institute of Information Science, Academia Sinica, Taiwan 

{tearfulcanon, lisu}@iis.sinica.edu.tw 

## ABSTRACT 

Recent deep learning-based models for estimating beats and downbeats are mainly composed of three successive stagesÐfeature extraction, sequence modeling, and post processing. While such a framework is prevalent in the scenario of sequence labeling tasks and yields promising results in beat and downbeat estimations, it also indicates a shortage of the employed neural networks, given that the post-processing usually provides a notable performance gain over the previous stage. Moreover, the assumption often made for the post-processing is not suitable for many musical pieces. In this work, we attempt to improve the performance of joint beat and downbeat estimation without incorporating the post-processing stage. By inspecting a state-of-the-art approach, we propose reformulations regarding the network architecture and the loss function. We evaluate our model on various music data and show that the proposed methods are capable of improving the baseline approach without the aid of a post-processing stage. 

## 1. INTRODUCTION 

Beat and downbeat trackings have been of long-standing interests in the communities of signal processing and music information retrieval (MIR) [1–5]. The two tasks inherently possess the class imbalance issue [6], i.e., the highly imbalanced numbers of beat (downbeat) and non-beat (non-downbeat) frames in music data, and hence remain challenging in many cases even nowadays. To tackle the beat and downbeat tracking problems, early signal processing approaches have developed a three-stage framework which consists of feature extraction, sequence modeling, and post-processing [7–9]. Over the past few years, great progresses on the two tasks have been made through the combination of the three-stage pipeline and deep learning models such as recurrent neural networks (RNNs) [10–12], convolutional-recurrent neural networks (CRNNs) [13], and Transformer-based networks [14]. Among the thriving research, a convolutional approach achieves the state-ofthe-art performance on joint estimation of tempo, beat, and 

> © Tsung-Ping Chen and Li Su. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: Tsung-Ping Chen and Li Su, ªToward postprocessing-free neural networks for joint beat and downbeat estimationº, in Proc. of the 23rd Int. Society for Music Information Retrieval Conf., Bengaluru, India, 2022. 

downbeat [15], in which convolutional neural networks (CNNs) and temporal convolutional networks (TCNs) [16] are placed in charge of the feature extraction and of the sequence modeling, respectively, while dynamic Bayesian networks (DBNs) [17] are used for the post-processing. 

In spite of the promising results obtained by this approach, the employed networks raise three concerns. First, the CNNs for feature extraction convolve an input spectrogram with small kernels at the very beginning, and a max-pooling layer is followed immediately. Therefore, the spectro-temporal patterns might not be well-captured [18]. Second, the dilated convolutions [19] of the TCNs involve a small kernel size and an exponentially increasing dilation rate. Despite the large receptive fields obtained at higher layers, this design leads to extremely sparse samplings which join distantly-separated frames, and consequently the contextual information could be irrelevant [20]. Lastly, the assumptions made for the DBNs that the meter is unchanged or the rhythmic patterns are known [11, 21] are not always applicable to various music genres, even to popular music. For example, the Hainsworth dataset [22], which is often employed for evaluation, includes several clips of pop or rock songs with changing meter. Moreover, the DBNs involve intricate design and assumptions for representing the state and the transition throughout a piece of music, and hence introduce non-trivial works in addition to the training of the preceding neural networks. 

In this paper, we cope with the joint beat and downbeat estimation task by addressing the aforementioned issues. To get rid of the post-processing DBNs while maintaining the performance, we consider to improve the network architecture and the loss function. Precisely, we propose to use scaled depthwise separable convolutions [23–25] to aggregate rich contextual information at multiple time scales. To address the class imbalance issue, the focal loss [26] and the Dice loss [27] are employed in place of the commonly used cross entropy loss. Besides, we make our model aware of the periodic structure of beat or downbeat sequences by including a label embedding network [28] during training. We evaluate the proposed architecture on various music data, including both audio and MIDI files, and demonstrate a state-of-the-art performance on the Ballroom dataset. The main contribution of this work is that we thoroughly address the architectural issues for beat and downbeat estimations. Most of the problems are shared by sequence models in general, and therefore the proposed methods could be applied to many other MIR-related tasks. 

27 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

## 2. OVERVIEW OF THE STATE-OF-THE-ART 

The model of [15] without the DBNs is taken as our baseline upon which we build our new model to address the architectural issues mentioned beforehand. In the following, we briefly introduce the baseline model using the threestage framework, and present the new model thereafter. We skip the post-processing stage for we aim to expel the DBNs from the system in this work. An overview of the baseline model is illustrated at the top of Figure 1. 

## 2.1 Feature extraction 

Given an audio signal represented as a log-magnitude spectrogram of size T ×J, where T denotes the number of time steps and J the number of frequency bins, the CNNs of the baseline model extract high-level features using three groups of 2-D convolution and max-pooling layers. The three convolutional layers (with a kernel size of 3 × 3, 1 × 12, and 3 × 3, respectively)<sup>1</sup> capture harmonic content at different frequency scales, while the max-pooling operations (with a kernel size of 1 × 3 ) reduce the frequency dimension in three steps. In other words, the CNNs gradually transcribe the harmonic information into high-level features, and output a sequence of size T × D with D indicating the dimension of high-level features. 

## 2.2 Sequence modeling 

The high-level feature sequence from the previous stage is then passed to the TCNs for learning temporal structure. As depicted at the top of Figure 1, each TCN layer performs two 1-D dilated convolutions in parallel with a kernel of size 5 and an exponentially increasing dilation rate 2<sup>l</sup> (resp. 2<sup>l+1</sup> ), where l is the layer number. The outputs of the two dilated convolutions are concatenated and reprojected to keep the feature dimensionality constant. As a result, the TCNs efficiently enlarge the receptive field within a few layers with the amount of learnable parameters increasing linearly to the number of layers. Given that the TCNs has 11 layers, the two convolutions at the last layer will expand the kernels across over 4000 (resp. 8000) time frames with each element of the two kernels being spaced 1024 (resp. 2048) frames apart. Therefore, the temporal context modelled by the TCN is more than 80 seconds (assume a frame rate of 100 fps). Afterwards, the output of the TCNs is processed by the DBNs to obtain a sequence of beat or downbeat estimates. 

## 2.3 Potential issues 

In the community of computer vision, it has been shown that stacking small convolutional kernels followed by pooling layers is effectual for extracting high-level features of an image [29–31]. Such a architecture is often adopted by audio-based, or more specifically spectrogram-based research [32–34]. Considering the nature of images, it is reasonable to aggregate information hierarchically from spatial associations. However, it is questionable that a spectro- 



<!-- Start of picture text -->
Feature Extraction Sequence Modeling<br>x11<br>5x1 dilated conv<br>3x3 conv 1x12 conv 3x3 conv 5x1 dilated conv<br>1x3 mp 1x3 mp 1x3 mp<br>5x41 conv 15x1 conv 301x1 separable conv<br>5x61 conv 21x1 conv 401x1 separable conv<br>gmp<br><!-- End of picture text -->

Figure 1: Architecture reformulation with respect to convolution (conv) and max pooling (mp) layers . Top: model of [15] without DBNs. Bottom: proposed architecture. The feature dimension is not shown in the figure. 

gram could be well-represented with the same architecture. The characteristic spectral information of a musical piece does not necessarily reside in the adjacent frequency bins within a small kernel. Moreover, it is also suspicious that the compressed frequency dimension after pooling operations is as meaningful as a downsampled image. 

On the other hand, it has been observed that dilated convolutions result in the so-called gridding artifacts [35,36], due to that adjacent elements in the output are calculated from completely different sets of elements in the input. Additionally, small convolutional kernels with high dilation rates relate input elements which are highly sparsely distributed and hence might lack of correlations. In the scenario of beat or downbeat estimation, stacked 1-D dilated convolutions could be preferable for they are able to encode periodic structure of the beat (downbeat) through equidistant elements of dilated kernels. However, it is not guaranteed that an inquired musical piece has a steady tempo as well as a constant rhythm. Hence, a network equipped with dilated convolutions for modeling temporal information may have limitations on expressive music. 

## 3. APPROACH 

## 3.1 Task formulation 

We treat the joint beat and downbeat estimation task as a sequence labeling problem [37, 38]. Given an input spectrogram X ∈ R<sup>T ×J</sup> , the task involves the assignment of a categorical label ∈{downbeat, xbeat, neither}<sup>2</sup> to each time step t ∈ T. We employ a model architecture which mainly consists of a feature extraction network (fex), a sequence modeling network (fseq), and an estima- 

> 1 A kernel size M × N specifies a convolution window across M time frames and N frequency bins. 

2 The label xbeat refers to a beat which is not a downbeat. 

28 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
Feature Sequence Estimation<br>Extraction Modeling<br>Cx_<br>SR FL DL<br>Encoder<br>Label Embedding<br>RL<br><!-- End of picture text -->

we use depthwise separable convolutions [23] (hereafter separable convolutions) instead. Separable convolution, denoted as fsc(·, d, w), factorizes a standard convolution into a depthwise convolution and a pointwise convolution. This factorization allows a network to expand the receptive field using a large kernel size without drastically increasing the number of parameters. Similarly to the TCNs, we use two separable convolutions with kernel sizes of wseq,1 and wseq,2, as shown in Figure 1. Each sequence modeling layer, denoted as fseq(·), is thus formulated as below: 



<!-- Start of picture text -->
fseq(·) = fsc(·, D, wseq,1) + fsc(·, D, wseq,2). (3)<br><!-- End of picture text -->

Figure 2: Proposed architecture. Dashed borders indicate data sequences, and solid ones denote neural networks. The losses includes focal loss (FL), Dice loss (DL), reconstruction loss (RL), and structural regularization (SR). 

tion network (fest) for the task: 



<!-- Start of picture text -->
P = fest(H),<br>H = fseq(Z), (1)<br>Z = fex(X),<br><!-- End of picture text -->

where Z, H ∈ R<sup>T ×D</sup> are higher-level feature sequences, and P ∈ R<sup>T ×3</sup> is a sequence of model estimates indicating the probabilities of the three categorical labels across all time steps. The overall model architecture is schematically shown in Figure 2. 

## 3.2 Reformulation of feature extraction 

We propose to use kernels of larger sizes for the 2-D convolution layers and remove the intermediate pooling layers in fex. As shown at the bottom of Figure 1, the feature extraction network consist of two layers, denoted as fex<sup>(1)andf (2)</sup> ex<sup>.Thefirstlayercapturesharmonicinforma-</sup> tion distributed across the frequency bins of an input spectrogram, while the second layer aggregates the harmonic information along the temporal dimension. Within each layer l, we employ two parallel convolutions with kernel sizes of wex,<sup>(l)</sup> 1<sup>andw</sup> ex,<sup>(l)</sup> 2<sup>.Fortheseconvolutionopera-</sup> tions, we keep the frequency dimension of the input spectrogram uncompressed, and thus the output shape will be T × J × D. Finally, we employ a global max pooling layer (GMP) [39] to reduce the frequency dimension (J) of the output, yielding the feature sequence Z ∈ R<sup>T ×D</sup> . Let fc(·, d, w) denote a standard convolution parameterized by the number of filters d and the kernel size w. The feature extraction network can be formulated as follows: 



<!-- Start of picture text -->
Z = fex(X) = GMPj∈J (f (2) ex (f (1) ex (X))),<br>(2)<br>fex (l)(·) = [fc(·, D, w ex, (l) 1 ), fc(·, D, w ex, (l) 2 )]W ex (l),<br><!-- End of picture text -->

where Wex<sup>(l)∈R2D×Dis a learnable parameter matrix at</sup> the l-th layer, and [·, ·] indicates a concatenation operation. 

## 3.3 Reformulation of sequence modeling 

To maintain a large receptive field while get rid of the sparse sampling issue introduced by dilated convolutions, 

Considering that rhythmic patterns are tempodependent, that is, the inter-beat or the inter-downbeat interval will vary according to the current tempo, it is crucial for a network to learn tempo-invariant, or scaleinvariant patterns [40]. To achieve scale invariance, we simply introduce a set of dilation rates, or scale factors s = {rs}<sup>S</sup> s=1<sup>toeachseparableconvolution.Thescaled</sup> separable convolution, accordingly, will operate S times on the same input with the kernel being expanded by the given set of dilation rates: 



<!-- Start of picture text -->
fssc (·, d, w) = (fsc(·, d, w, r1), . . . , fsc(·, d, w, rS)), (4)<br><!-- End of picture text -->

where (·, . . . , ·) denotes a stacking operation. Therefore, the scaled separable convolution is capable of capturing rhythmic patterns at different tempi simultaneously. Note that the dilation employed here differs from that of the original TCNs in two aspects. First, we employ the dilation for modeling tempo variance rather than for expanding the receptive field. Second, the parameters of a scaled separable convolution are shared among the S operations. 

By introducing the scale factors, we add a new dimension to the output of the scaled separable convolution, whose shape thus becomes T × D × S. We summarize the scale information by applying a gating mechanism, termed scale summarization (SS), which is similar to the Squeeze-and-Excitation operation of the SENet [41]. Let U ∈ R<sup>T ×D×S</sup> denote the output of a scaled separable convolution. We use global average pooling (GAP) along both the time and the feature dimensions to calculate scalewise statistics z ∈ R<sup>S</sup> . Subsequently, a gating function g ∈ R<sup>S</sup> is generated by using a projection layer with learnable parameters W ∈ R<sup>S×S</sup> and a softmax activation. Lastly, we apply the gate function to U for obtaining the summarized output U<sup>′</sup> ∈ R<sup>T ×D</sup> : 



<!-- Start of picture text -->
S<br>U ′ = SS(U) = Ug,<br>∑ s=1 (5)<br>g = softmax(Wz), z = GAP<br>s∈S t∈T,d∈D (U).<br><!-- End of picture text -->



<!-- Start of picture text -->
In conclusion, the L-layer sequence modeling network<br>can be formally expressed as follows:<br>H (l) = fseq (l) (H(l−1)),<br>fseq (l) (·) = SS(f s sc(·, D, wseq,1) + f s sc(·, D, wseq,2)), (6)<br><!-- End of picture text -->

with boundaries H<sup>(0)</sup> = Z and H<sup>(L)</sup> = H. 

29 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

## 3.4 Estimation 

We employ a convolutional layer with a kernel size of west followed by a softmax activation function to estimate the probabilities of being downbeat (db), xbeat (xb), and neither (n) at each time step: 



<!-- Start of picture text -->
[Pdb, Pxb, Pn] = P = fest(H)<br>(7)<br>= softmax(fc(H, d = 3, west)),<br>d<br><!-- End of picture text -->

where Pdb, Pxb, Pn ∈ R<sup>T</sup> indicate the estimated probabilities of the three categorical labels across T time steps. During inference, we generate a downbeat sequence (Idb) and a beat sequence (Ib) from Pdb and Pxb by finding the local maximums (LM): 



<!-- Start of picture text -->
Idb = LM(Pdb),<br>(8)<br>Ib = LM(Pb) = LM(Pdb + Pxb).<br><!-- End of picture text -->

## 3.5 Loss function 

Cross entropy is often used as the loss function in the beat and the downbeat estimation tasks. Since the cross entropy loss treats all samples equally, the network optimization will be dominated by vast amount of easy samples, i.e., time frames not belonging to the beat and the downbeat. Similar cases can be found in computer vision-related tasks such as object detection, where exists an extreme foreground-background disproportion. The focal loss (FL) [26] is therefore proposed to weigh more on hard or easily mis-classified samples by introducing a modulating term to the cross entropy loss: 



<!-- Start of picture text -->
N<br>FL = − 1 mi × yi × log(pi), (9)<br>-∑ N i=1<br><!-- End of picture text -->

where pi is the estimated probability of sample i being classified as the ground truth yi, and mi = (1 − pi)<sup>γi</sup> is the modulating term with γi being a controllable factor. It is noteworthy that the FL, as same as the cross entropy, is calculated on individual samples and hence unable to reflect spatial or temporal relations between samples. On the other hand, the Dice loss (DL) [27], which has been applied to semantic segmentation of images, measures the overlap between the estimations of N samples and the ground truths, and thus can delineate the regions of interest, e.g., beat positions in a given musical sequence: 



<!-- Start of picture text -->
N<br>DL = 1 − N2 ∑ i = 1 p i × N y i . (10)<br>∑ i=1 p i 2 + ∑ i=1 y i 2<br><!-- End of picture text -->

We propose to use a hybrid of the FL and the DL in place of the cross entropy loss, for they address the class imbalance issue from two complementary aspects: the FL accentuates individual hard samples whereas the DL underlines collective similarity of the minority samples. In practice, we compute the FL on P while the DL on both Pdb and Pb. By combining the two losses, we urge our network to focus on the minority classes, i.e., beats and downbeats, both at the frame level and at the sequence level. 



<!-- Start of picture text -->
KD<br>Kdb<br>D&o<br><!-- End of picture text -->

Figure 3: Representations of beat (top) and downbeat (bottom) for label embedding (assume a meter of 4/4). The horizontal axes are the time dimensions while the vertical axes indicate the phase classes. Kb and Kdb are the numbers of classes for beat and downbeat, respectively. 

## 3.6 Label embedding 

Another concern in regard to the loss function is that the periodic structure of a beat or downbeat sequence is not considered. A recent work deals with the periodicity by estimating beat phase instead of beat presence at each frame [42]. Accordingly, the beat estimation task is reformulated as a sequence labeling problem in which the beat phase is represented as a discrete sawtooth wave with period equal to the interbeat interval. This reformulation, however, enlarges the estimation space as the beat phase is categorized into K classes with K being the phase resolution. 

Alternatively, we leverage the label embedding approach [28] for learning the periodic structure. As illustrated in Figure 3, a sequence of ground-truth annotations is represented as a discrete triangular wave ∆{db,b} ∈ R<sup>T ×K{db,b}</sup> whose troughs locate at the beat or downbeat frames. We then employ a vanilla autoencoder to encode the represented annotations in an unsupervised manner. The encoder (fenc) and the decoder (fdec) used are both a simple 1-D convolution layer with a kernel size of we, i.e., fenc(·) = fdec(·) = fc(·, D, we). The label embedding network is formulated as follows: 



<!-- Start of picture text -->
[Vdb ′ , V b ′ ] = fdec(E),<br>E = fenc([Vdb, Vb]), (11)<br>Vdb = ∆dbWdb, Vb = ∆bWb,<br><!-- End of picture text -->

where W{db,b} ∈ R<sup>K{db,b}×D</sup> are learnable phase embedding matrices, V{db,b} ∈ R<sup>T ×D</sup> are sequences of embeddings, E ∈ R<sup>T ×D</sup> is a sequence of joint embeddings, and V{<sup>′</sup> db,b}<sup>∈RT ×DarethereconstructionsofV{db,b}.We</sup> compute the reconstruction loss (RL) as follows: 



<!-- Start of picture text -->
RL = FL(∆db, ∆ ′ db ) + FL(∆b, ∆′ b ),<br>∆ ′ db = softmax (Vdb ′ W db ⊤ ),<br>k∈K (12)<br>∆ ′ b = softmax (Vb ′ W b ⊤).<br>k∈K<br><!-- End of picture text -->

As illustrated in Figure 2, the joint embedding E is taken as a structural regularization (SR) of H (the output of the sequence modeling network) by minimizing the mean squared error (MSE): 



<!-- Start of picture text -->
SR = MSE(E, H). (13)<br><!-- End of picture text -->

Hence, the total loss L = FL + DL + RL + SR. We train the whole networks in an end-to-end fashion. As the 

30 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

contextual information of the annotations is encoded in E, adding this topology-aware regularization term (SR) to the loss computation enables the network to explicitly learn the structural characteristics [43]. The source code of the proposed model is available online.<sup>3</sup> 

## 4. EVALUATION 

## 4.1 Data preparation 

Four datasets are employed in the evaluation, including the Ballroom [44], the Hainsworth [22], the GTZAN [45], and the ASAP [46]. Each audio file (with a sampling rate of 44,100 Hz) in the datasets is transformed into a logmagnitude spectrogram with a total of 81 frequency bins from 30 Hz to 17,000 Hz, by using the Python package librosa [47]. Specifically, the short-time Fourier transform (STFT) with a window size of 92.9 ms (4,096 samples) and a hop size of 23.2 ms (1,024 samples) is applied, and the output spectrogram is mapped onto the Mel scale. The per-bin first-order difference is calculated for each spectrogram as an additional feature (only the positive differences are retained) [16]. In consequence, each audio file is represented as X ∈ R<sup>T ×81×2</sup> with T being the time steps of the corresponding spectrogram. Besides, the MIDI data of the ASAP are also used for evaluation. Following [48], we represent each MIDI file by four features: the pitch profile ∈ R<sup>T ×88</sup> (i.e., pianoroll), the onset profile ∈ R<sup>T ×88</sup> , the spectral flux ∈ R<sup>T</sup> , and the inter-onset interval ∈ R<sup>T</sup> . We modify our feature extraction network accordingly for the MIDI representation, and keep the other parts of the architecture unchanged. Specifically, the pitch profile and the onset profile are concatenated together and fed into the feature extraction network. The output of the feature extraction network is then concatenated with the other two features and taken as the input of the succeeding layer. 

On the other hand, the beat and downbeat annotations are represented as binary sequences, Yb, Ydb ∈{0, 1}<sup>T</sup> , where a time step t ∈ T has a value of 1 if it belongs to the beat or the downbeat, and 0 otherwise. To treat joint beat and downbeat estimation as a sequence labeling problem, we further generate Y ∈{0, 1}<sup>T ×3</sup> based on Ydb and Yb, which is a sequence of one-hot vectors indicating the categorical label of each time step. The Y is used to compute the FL (with P) while the Yb and the Ydb are for the DL (with Pb and Pdb, respectively), as depicted in Figure 2. 

## 4.2 Experiment 

We evaluate the proposed architecture on the four datasets and report the beat and the downbeat estimation performances using the standard F1 measure with a tolerance window of ±70 ms. The hyperparameters of the architecture are set as in Table 1. The model of [15] without DBNs (i.e., the top one in Figure 1) is employed as our baseline model. The numbers of learnable parameters are around 110K and 63K for the proposed model and the baseline, 

> 3 https://github.com/Tsung-Ping/ Joint-beat-and-downbeat-estimation 

|Input||
|---|---|
|Number of frequency bins|J = 81for Audio<br>J = 88for MIDI|
|Feature extraction||
|Kernel size|w<sup>(1)</sup><br>ex,1 <sup>= 5 × 41</sup><br>|
|Kernel size|w<sup>(1)</sup><br>ex,2 <sup>= 5 × 61</sup><br>|
|Kernel size|w<sup>(2)</sup><br>ex,1 <sup>= 15 × 1</sup><br>|
|Kernel size|w<sup>(2)</sup><br>ex,2 <sup>= 21 × 1</sup>|
|Feature dimension|D = 20|
|Sequence modeling||
|Kernel size|wseq,1 = 301|
|Kernel size|wseq,2 = 401|
|Scale factor|s={1,2,3,4}|
|Number of scales|S = 4|
|Number of layers|L= 4|
|Estimation||
|Kernel size|west = 7|
|Label embedding||
|Number of beat phase classes|Kb = 150|
|Number of downbeat phase classes<br>Kernel size|Kdb = 500<br>we = 7|



Table 1: Hyperparameters of the proposed architecture. 

respectively. Evidently, we can employ separable convolutions to enlarge the receptive field without a catastrophic increase of model capacity. To investigate the effectiveness of the proposed methods, we further perform an ablation study by removing one of the reformulations: feature extraction (abl_ex), sequence modeling (abl_seq), loss function (abl_loss), and label embedding (abl_lab). 

In line with [15], the Ballroom and the Hainsworth are both split for 8-fold cross-validations.<sup>4</sup> Note that the two datasets are used separately rather than merged as a single cross-validation set. The GTZAN is divided into 10 parts according to the built-in genre labels, with which a 10-fold cross-validation is performed to inspect the performance variance with respect to genre.<sup>5</sup> For the ASAP, we first create a subset by selecting audio recordings which have a paired MIDI file (519 pairs in total). Afterwards, a test set is built from the subset with musical pieces by the four composers: Glinka, Mozart, Schubert, and Rachmaninoff; the remaining data of the subset are used for training. The paired MIDI files are used as the audio counterparts to examine the impact of input modality on the performance. 

All the training data are augmented in two ways: 1) by shifting the pitch of an audio signal before the STFT is applied, and 2) by changing the hop size of the STFT window.<sup>6</sup> For the ASAP, we only apply the pitch augmentation as its total duration is significantly longer than the other three datasets. By the pitch augmentation, we can easily increase the data amount without extra annotation 

> 4 The details of the data splitting can be found at https:// github.com/superbock/ISMIR2020. 

> 5 jazz.00003, jazz.00009, jazz.00010, jazz.00014, jazz.00018, jazz.00020 are excluded for they have no downbeat annotations; reggae.00086 is damaged and also excluded. 

> 6 We use pitch shifts ∈ {-5 ∼ +6} (semitones) and hop sizes ∈{18.9, 20.3, 21.8, 23.2, 26.1, 29.0, 31.9} (ms) for the data augmentation. 

31 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

|Task|Model|Ballroom|Hainsworth|||||GTZA|N|||||AS|AP|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||blues|classical|country|disco|hiphop|jazz|metal|pop|reggae|rock|Audio|MIDI|
|Beat|baseline|96.60|84.18|83.20|51.62|96.65|97.76|94.61|68.40|82.46|93.84|92.76|89.90|71.43|72.45|
||proposed|96.81|86.28|86.63|63.23|94.82|97.63|95.58|79.80|86.48|94.81|93.05|93.01|71.40|75.70|
|Donbeat|baseline|92.06|66.18|59.25|14.70|79.70|82.71|72.86|33.47|64.64|84.67|51.06|76.49|49.46|57.34|
|w|proposed|94.21|69.11|60.98|30.17|83.91|86.28|79.10|50.66|67.21|83.86|56.87|76.55|63.92|67.43|



Table 2: Evaluation results in terms of F1 score (%). For the Ballroom and the Hainsworth, the scores are the averaged performances over a 8-fold cross-validation. For the GTZAN, the score on each genre is obtained in a 10-fold crossvalidation manner. For the ASAP, the performances on the audio data and on the MIDI data are separately shown. 

|Task|Model|Ballroom|Hainsworth|
|---|---|---|---|
||abl_ex|96.08 (-0.73)|85.49 (-0.79)|
|Bt|abl_seq|96.98 (+0.17)|85.96 (-0.32)|
|ea|abl_loss|95.27 (-1.54)|86.52 (+0.24)|
||abl_lab|96.54 (-0.27)|86.83 (+0.55)|
||abl_ex|92.16 (-2.05)|62.27 (-6.84)|
|Donbeat|abl_seq|94.16 (-0.05)|69.73 (+0.62)|
|w|abl_loss|91.99 (-2.22)|66.79 (-2.32)|
||abl_lab|93.61 (-0.60)|69.58 (+0.47)|



Table 3: Ablation study on the Ballroom and the Hainsworth. Performance in terms of F1 score (%) and relative improvement against the proposed model (in parentheses) are provided. 

cost; moreover, the model can explicitly learn rhythmic features independent of absolute pitch. By the hop-size augmentation, we can obtain more training data of different tempi with a slight adjustment of the annotations. 

## 4.3 Result 

The evaluation results are summarized in Table 2, showing the performance on each dataset in terms of beat estimation and downbeat estimation. When evaluated on the Ballroom and the Hainsworth, the proposed model outperforms the baseline in both beat and downbeat estimations. Moreover, it is surprising that the evaluation results on the Ballroom are even better than [15] (beat: 96.20; downbeat: 91.6) and [14] (beat: 96.20; downbeat: 93.7) considering that we didn’t use a combination of datasets for training and DBNs for post-processing; in addition, our model is smaller in capacity than the best model of [14] which has around 4.7M learnable parameters. On the other hand, the results on the Hainsworth indicate that more efforts should be put in dealing with music data of diverse styles. For instance, the choruses collected in the Hainsworth are extremely flexible in tempo at the beginning and particularly at the end of each phrase, and therefore a phrase segmentation technique might be incorporated in the tasks. 

For the GTZAN, the proposed model demonstrates its superiority over the baseline in almost all the cases. The average beat estimation performances are 85.12% and 88.50% for the baseline and the proposed model, respectively, while the average downbeat estimation performances are 61.96% and 67.56%. According to the evaluation results, the rhythmic characteristics of classical and jazz are quite distinct from the other genres. Nev- 

ertheless, our model still surpasses the baseline by around 15.5 and 17.2 percentage points in estimating the downbeats of classical and jazz, respectively. These improvements are notable and indicate the capability of our model in both tasks, especially in downbeat estimation. 

For the audio data of the ASAP, the proposed model performs comparably to the baseline on the beat estimation while remarkably outperforms the baseline on the downbeat estimation. For the MIDI data of the ASAP, our model achieves greater results both on estimating the beats and the downbeats. It is worth noting that in all cases, the estimation result is better on the MIDI data than on the audio counterpart. Given that automatic music transcription (AMT) [49–51] is an active research topic in the field of MIR, it could be promising to incorporate AMT techniques into the beat and the downbeat estimations. 

Finally, as shown in Table 3, the ablation study indicates that our reformulations of the feature extraction and the loss function have notable positive effect especially on estimating downbeats, while the improvements by the other components are inconsistent over the tasks and datasets. We also observed that for the Hainsworth, the model without the label embedding (abl_lab) performs slightly better. This might result from the limited expressiveness of H due to the regularization on it. A more extensive study is required to justify the proposed reformulations. 

## 5. CONCLUSION 

We have addressed the joint beat and downbeat estimation task based on a state-of-the-art approach. By inspecting the potential issues in this approach, we proposed several reformulations to further the performance of deep neural networks. We experimentally showed that the proposed architecture is capable of outperforming the state-of-theart approach without the aid of a post-processing network. In the scenario of deep learning-based beat and downbeat estimations, as well as in many sequence labeling frameworks, it is common to involve a post-processing stage in addition to the deep neural networks since the outputs by the networks are usually coarse when a simple thresholding method is applied. While involving a post-processing stage often leads to an improvement over the preceding deep learning models, it hinders the formulation of endto-end training and indicates a necessity to reconsider the employed neural networks. Hopefully, we are able to build a model tailored to the task of interest with a deeper look at the network architecture from the perspective of data. 

32 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

## 6. REFERENCES 

- [1] M. Goto and Y. Muraoka, ªA beat tracking system for acoustic signals of music,º in Proceedings of the 2nd ACM International Conference on Multimedia, 1994, pp. 365–372. 

- [2] S. Dixon, ªAutomatic extraction of tempo and beat from expressive performances,º Journal of New Music Research, vol. 30, no. 1, pp. 39–58, 2001. 

- [3] L. M. Smith, ªBeat critic: Beat tracking octave error identification by metrical profile analysis,º in Proceedings of the 11th International Society for Music Information Retrieval Conference (ISMIR), 2010, pp. 99– 104. 

- [4] H. Grohganz, M. Clausen, and M. Müller, ªEstimating musical time information from performed MIDI files,º in Proceedings of the 15th International Society for Music Information Retrieval Conference (ISMIR), 2014, pp. 35–40. 

- [5] S. Durand, J. P. Bello, B. David, and G. Richard, ªFeature adapted convolutional neural networks for downbeat tracking,º in Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2016, pp. 296–300. 

- [6] R. Anand, K. G. Mehrotra, C. K. Mohan, and S. Ranka, ªAn improved algorithm for neural network classification of imbalanced training sets,º IEEE Transactions on Neural Networks, vol. 4, no. 6, pp. 962–969, 1993. 

- [7] M. Goto and Y. Muraoka, ªAn audio-based real-time beat tracking system and its applications,º in Proceedings of the International Computer Music Conference (ICMC), 1998. 

- [8] M. E. P. Davies and M. D. Plumbley, ªA spectral difference approach to downbeat extraction in musical audio,º in Proceedings of the 14th European Signal Processing Conference (EUSIPCO), 2006, pp. 1–4. 

- [9] D. P. Ellis, ªBeat tracking by dynamic programming,º Journal of New Music Research, vol. 36, no. 1, pp. 51– 60, 2007. 

- [10] F. Krebs, S. Böck, M. Dorfer, and G. Widmer, ªDownbeat tracking using beat synchronous features with recurrent neural networks,º in Proceedings of the 17th International Society for Music Information Retrieval Conference (ISMIR), 2016, pp. 129–135. 

- [11] S. Böck, F. Krebs, and G. Widmer, ªJoint beat and downbeat tracking with recurrent neural networks,º in Proceedings of the 17th International Society for Music Information Retrieval Conference (ISMIR), 2016, pp. 255–261. 

- [12] C. Chiu, A. W. Su, and Y. Yang, ªDrum-aware ensemble architecture for improved joint musical beat and downbeat tracking,º IEEE Signal Processing Letters, vol. 28, pp. 1100–1104, 2021. 

- [13] M. Fuentes, B. McFee, H. C. Crayencour, S. Essid, and J. P. Bello, ªA music structure informed downbeat tracking system using skip-chain conditional random fields and deep learning,º in Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2019, pp. 481–485. 

- [14] Y.-N. Hung, J.-C. Wang, X. Song, W.-T. Lu, and M. Won, ªModeling beat and downbeat estimations with a time-frequency Transformer,º in Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2022, pp. 401–405. 

- [15] S. Böck and M. E. P. Davies, ªDeconstruct, analyse, reconstruct: How to improve tempo, beat, and downbeat estimation,º in Proceedings of the 21th International Society for Music Information Retrieval Conference (ISMIR), 2020, pp. 574–582. 

- [16] M. E. P. Davies and S. Böck, ªTemporal convolutional networks for musical audio beat tracking,º in Proceedings of the 27th European Signal Processing Conference (EUSIPCO), 2019, pp. 1–5. 

- [17] F. Krebs, S. Böck, and G. Widmer, ªAn efficient statespace model for joint tempo and meter tracking,º in Proceedings of the 16th International Society for Music Information Retrieval Conference (ISMIR), 2015, pp. 72–78. 

- [18] J. Pons, O. Slizovskaia, R. Gong, E. Gómez, and X. Serra, ªTimbre analysis of music audio signals with convolutional neural networks,º in Proceedings of the 25th European Signal Processing Conference (EUSIPCO), 2017, pp. 2744–2748. 

- [19] F. Yu and V. Koltun, ªMulti-scale context aggregation by dilated convolutions,º in Proceedings of the 4th International Conference on Learning Representations (ICLR), 2016. 

- [20] P. Wang, P. Chen, Y. Yuan, D. Liu, Z. Huang, X. Hou, and G. W. Cottrell, ªUnderstanding convolution for semantic segmentation,º in Proceedings of the IEEE Winter Conference on Applications of Computer Vision (WACV), 2018, pp. 1451–1460. 

- [21] F. Krebs, S. Böck, and G. Widmer, ªRhythmic pattern modeling for beat and downbeat tracking in musical audio,º in Proceedings of the 14th International Society for Music Information Retrieval Conference (ISMIR), 2013, pp. 227–232. 

- [22] S. Hainsworth and M. D. Macleod, ªParticle filtering applied to musical tempo tracking,º EURASIP Journal on Applied Signal Processing, vol. 15, pp. 2385–2395, 2004. 

- [23] L. Sifre, ªRigid-motion scattering for image classification,º Ph.D. thesis, École Polytechnique, 2014. 

33 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

- [24] F. Chollet, ªXception: Deep learning with depthwise separable convolutions,º in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2017, pp. 1800–1807. 

- [25] A. G. Howard, M. Zhu, B. Chen, D. Kalenichenko, W. Wang, T. Weyand, M. Andreetto, and H. Adam, ªMobileNets: Efficient convolutional neural networks for mobile vision applications,º ArXiv e-prints, 2017. [Online]. Available: http://arxiv.org/abs/1704.04861 

- [26] T. Lin, P. Goyal, R. B. Girshick, K. He, and P. Dollár, ªFocal loss for dense object detection,º in Proceedings of the IEEE International Conference on Computer Vision (ICCV), 2017, pp. 2999–3007. 

- [27] F. Milletari, N. Navab, and S. Ahmadi, ªV-Net: Fully convolutional neural networks for volumetric medical image segmentation,º in Proceedings of the 4th International Conference on 3D Vision (3DV), 2016, pp. 565–571. 

- [28] Z. Akata, F. Perronnin, Z. Harchaoui, and C. Schmid, ªLabel-embedding for image classification,º IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 38, no. 7, pp. 1425–1438, 2016. 

- [29] K. Simonyan and A. Zisserman, ªVery deep convolutional networks for large-scale image recognition,º in Proceedings of the 3rd International Conference on Learning Representations (ICLR), 2015. 

- [30] K. He, X. Zhang, S. Ren, and J. Sun, ªDeep residual learning for image recognition,º in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2016, pp. 770–778. 

- [31] G. Huang, Z. Liu, L. van der Maaten, and K. Q. Weinberger, ªDensely connected convolutional networks,º in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2017, pp. 2261–2269. 

- [32] F. Korzeniowski and G. Widmer, ªA fully convolutional deep auditory model for musical chord recognition,º in Proceedings of the 26th IEEE International Workshop on Machine Learning for Signal Processing (MLSP), 2016, pp. 1–6. 

- [33] K. Choi, G. Fazekas, and M. B. Sandler, ªAutomatic tagging using deep convolutional neural networks,º in Proceedings of the 17th International Society for Music Information Retrieval Conference (ISMIR), 2016, pp. 805–811. 

- [34] S. Böck, M. E. P. Davies, and P. Knees, ªMulti-task learning of tempo and beat: Learning one to improve the other,º in Proceedings of the 20th International Society for Music Information Retrieval Conference (ISMIR), 2019, pp. 486–493. 

- [35] F. Yu, V. Koltun, and T. A. Funkhouser, ªDilated residual networks,º in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2017, pp. 636–644. 

- [36] R. Hamaguchi, A. Fujita, K. Nemoto, T. Imaizumi, and S. Hikosaka, ªEffective use of dilated convolutions for segmenting small object instances in remote sensing imagery,º in Proceedings of the IEEE Winter Conference on Applications of Computer Vision (WACV), 2018, pp. 1442–1450. 

- [37] X. Ma and E. H. Hovy, ªEnd-to-end sequence labeling via bi-directional LSTM-CNNs-CRF,º in Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (ACL), 2016. 

- [38] A. Akbik, D. Blythe, and R. Vollgraf, ªContextual string embeddings for sequence labeling,º in Proceedings of the 27th International Conference on Computational Linguistics (COLING), 2018, pp. 1638–1649. 

- [39] M. Oquab, L. Bottou, I. Laptev, and J. Sivic, ªIs object localization for free? - weakly-supervised learning with convolutional neural networks,º in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2015, pp. 685–694. 

- [40] B. D. Giorgi, M. Mauch, and M. Levy, ªDownbeat tracking with tempo invariant convolutional neural networks,º in Proceedings of the 21th International Society for Music Information Retrieval Conference (ISMIR), 2020, pp. 216–222. 

- [41] J. Hu, L. Shen, and G. Sun, ªSqueeze-and-excitation networks,º in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2018, pp. 7132–7141. 

- [42] T. Oyama, R. Ishizuka, and K. Yoshii, ªPhase-aware joint beat and downbeat estimation based on periodicity of metrical structure,º in Proceedings of the 22nd International Society for Music Information Retrieval Conference (ISMIR), 2021, pp. 493–499. 

- [43] A. Mosinska, P. Márquez-Neila, M. Kozinski, and P. Fua, ªBeyond the pixel-wise loss for topology-aware delineation,º in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2018, pp. 3136–3145. 

- [44] F. Gouyon, A. Klapuri, S. Dixon, M. Alonso, G. Tzanetakis, C. Uhle, and P. Cano, ªAn experimental comparison of audio tempo induction algorithms,º IEEE Transactions on Audio, Speech, and Language Processing (TASLP), vol. 14, no. 5, pp. 1832–1844, 2006. 

- [45] G. Tzanetakis and P. R. Cook, ªMusical genre classification of audio signals,º IEEE Transactions on Speech and Audio Processing, vol. 10, no. 5, pp. 293–302, 2002. 

34 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

- [46] F. Foscarin, A. McLeod, P. Rigaux, F. Jacquemard, and M. Sakai, ªASAP: a dataset of aligned scores and performances for piano transcription,º in Proceedings of the 21th International Society for Music Information Retrieval Conference (ISMIR), 2020, pp. 534–541. 

- [47] B. McFee, C. Raffel, D. Liang, D. P. Ellis, M. McVicar, E. Battenberg, and O. Nieto, ªlibrosa: Audio and music signal analysis in Python,º in Proceedings of the 14th python in science conference (SCIPY), vol. 8, 2015. 

- [48] Y. Chuang and L. Su, ªBeat and downbeat tracking of symbolic music data using deep recurrent neural networks,º in Asia-Pacific Signal and Information Processing Association Annual Summit and Conference (APSIPA), 2020, pp. 346–352. 

- [49] A. Ycart, A. McLeod, E. Benetos, and K. Yoshii, ªBlending acoustic and language model predictions for automatic music transcription,º in Proceedings of the 20th International Society for Music Information Retrieval Conference (ISMIR), 2019, pp. 454–461. 

- [50] Y. Wu, B. Chen, and L. Su, ªMulti-instrument automatic music transcription with self-attention-based instance segmentation,º IEEE ACM Transactions on Audio, Speech, and Language Processing (TASLP), vol. 28, pp. 2796–2809, 2020. 

- [51] C. Hawthorne, I. Simon, R. Swavely, E. Manilow, and J. H. Engel, ªSequence-to-sequence piano transcription with transformers,º in Proceedings of the 22nd International Society for Music Information Retrieval Conference (ISMIR), 2021, pp. 246–253. 

35 

