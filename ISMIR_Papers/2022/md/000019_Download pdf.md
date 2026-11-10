---
paper_id: "000019"
year: 2022
title: "Download pdf"
source_url: "https://zenodo.org/record/7316622/files/000019.pdf"
---

# BEAT TRANSFORMER: DEMIXED BEAT AND DOWNBEAT TRACKING WITH DILATED SELF-ATTENTION 

Jingwei Zhao<sup>2,4</sup> Gus Xia<sup>3,5</sup> Ye Wang<sup>1,2,4</sup> 1 School of Computing, NUS 2 Institute of Data Science, NUS 3 Music X Lab, NYU Shanghai 4 Integrative Sciences and Engineering Programme, NUS Graduate School 5 MBZUAI 

jzhao@u.nus.edu, gxia@nyu.edu, wangye@comp.nus.edu.sg 

## ABSTRACT 

We propose Beat Transformer, a novel Transformer encoder architecture for joint beat and downbeat tracking. Different from previous models that track beats solely based on the spectrogram of an audio mixture, our model deals with demixed spectrograms with multiple instrument channels. This is inspired by the fact that humans perceive metrical structures from richer musical contexts, such as chord progression and instrumentation. To this end, we develop a Transformer model with both time-wise attention and instrument-wise attention to capture deep-buried metrical cues. Moreover, our model adopts a novel dilated self-attention mechanism, which achieves powerful hierarchical modelling with only linear complexity. Experiments demonstrate a significant improvement in demixed beat tracking over the non-demixed version. Also, Beat Transformer achieves up to 4% point improvement in downbeat tracking accuracy over the TCN architectures. We further discover an interpretable attention pattern that mirrors our understanding of hierarchical metrical structures. 

## 1. INTRODUCTION 

Music audio beat and downbeat tracking, which aims to infer the very basic metrical structure of music, is a long-standing central topic in music information retrieval (MIR). A good beat estimation benefits various downstream MIR tasks, including transcription and structure analysis [1±5]. Moreover, beat tracking can be applied to human-computer interaction [6,7], music therapy [8], and more scenes, as beats echo with human perceptual and motor sensitivity to musical rhythms. 

We see significant progress in beat tracking with the development of deep neural networks. Current mainstream methods utilize temporal convolutional networks (TCNs) to extract frame-wise beat activations from an input spectrogram [9]. We further see successful efforts in boosting beat tracking performance, including phase-informed postprocessing with dynamic Bayesian networks (DBNs) [10], 

> © J. Zhao, G. Xia, and Y. Wang. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: J. Zhao, G. Xia, and Y. Wang, ªBeat Transformer: Demixed Beat and Downbeat Tracking with Dilated Self-Attentionº, in Proc. of the 23rd Int. Society for Music Information Retrieval Conf., Bengaluru, India, 2022. 

multi-task learning for joint beat, downbeat and tempo estimation [11±13], and explicit beat phase modelling [14]. 

Recently, Transformer has demonstrated highly competitive performances over a range of MIR tasks [15±21]. In this paper, we propose Beat Transformer, a novel Transformer encoder architecture for joint beat and downbeat tracking. To better accommodate Transformer to our purpose, we introduce two extra inductive biases. Firstly, our model is constructed with short-windowed dilated selfattention. An exponentially increasing dilation rate enables our model to discern beats from non-beats in a hierarchical manner. With a fixed window size, our model maintains a linear complexity to the input sequence length. 

Another inductive bias is demixed beat tracking. This strategy is inspired by the fact that human beat tracking is always accompanied by and enhanced by a deep understanding of the musical contexts. For example, the coordination of instruments enforces the progression of chords and bass notes, thus implying metrical accents, and such cues can be easily identified by human listeners. To capture this relation, we use Spleeter [22] to demix an input music piece into multiple instrument channels, and our model performs both time-wise and instrument-wise attention in alternate Transformer layers to excavate metrical cues. 

We evaluate Beat Transformer on a wide range of beat- and downbeat-annotated datasets. Besides competing with state-of-the-art works, we present a thorough ablation study to illustrate the effectiveness of dilated self-attention and demixing. Moreover, our model learns highly interpretable representations. We demonstrate that our model can be interpreted as a learner over finite-state Markov chains, and we observe beat phase transition through visualization of the transition (attention) matrix. 

In brief, the contributions of our paper are as follows: 

- We propose Beat Transformer<sup>1</sup> , a novel Transformer encoder architecture for joint beat and downbeat tracking in music audio. 

- We devise dilated self-attention, which demonstrates powerful sequential modelling with linear complexity, potentially adaptable to more general MIR tasks. 

- We make use of music demixing to complement and enhance beat tracking, shedding light on future MIR research towards universal music understanding. 

- 1 Available at https://github.com/zhaojw1998/Beat-Transformer. 

169 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

## 2. RELATED WORKS 

We review two topics related to our work: beat tracking, and Transformer. For beat tracking, we focus on its development with deep neural networks. For Transformer, we address its application in MIR. For more general review of both topics, we refer readers to [23] and [24], respectively. 

## 2.1 Music Audio Beat Tracking 

Beat tracking has been formulated as a two-stage sequential learning task. The first stage aims to determine the likelihood of beat presence, or beat activation, at each frame of an input spectrogram. The initial deep learning approach for this purpose was based on long short-term memory networks (LSTM) [25, 26]. To better pick up the beat sequence from raw model output, at the second stage, a dynamic Baysian network (DBN) is introduced to infer tempo and beat phase transition from beat activation [10]. 

The current mainstream methods substitute the LSTM with a TCN architecture [9, 12±15]. Specifically, the convolutional kernels have a dilation rate exponential to the depth of layer. This hierarchical structure facilitates the network to model various scales, functionally similar to pooling, but maintains the same input and output size [27]. Besides architecture, another breakthrough of beat tracking is the formulation of multi-task learning [11±15]. Specifically, beat, downbeat, and tempo are strongly correlated metrical features. Sharing model weights among all three sub-tasks helps each to reach better convergence. 

A recent trend of beat tracking is to deal with demixed music sources. Chiu et. al. leverages demixed drum and non-drum streams to enhance model adaptability to different drum source conditions [28, 29]. In fact, humans can track beats while switching their attention among different instrument parts. Hence the coordination of instrumental sources can be explored for useful metrical information. 

In our work, we inherit the fashion of multi-task learning and the use of DBN, while proposing a novel Transformer encoder architecture to replace TCN. We formalize dilated self-attention [30, 31] for efficient modeling of long metrical structures. Moreover, we seek to enhance beat tracking by introducing instrumental attention among drum, piano, bass, vocal, and other demixed sources. 

## 2.2 Transformer in MIR 

Transformer has established itself de facto state-of-theart in natural language and symbolic music domain. Recently, it has also demonstrated outstanding performance over audio-based MIR tasks, including music transcription [17±19], music tagging [20, 21], and other analysis [16]. For these tasks, a Transformer model is trained over short spectrogram clips typically of 2-5 seconds as a compromise to the quadratic complexity computing self-attention. 

Transformer is first applied to beat tracking by Hung et. al. [15] using SpecTNT blocks [16]. For each SpecTNT block, a spectral Transformer encoder first aggregates spectral information at each time step, and then a temporal encoder exchanges information in time and pays attention 

to beat and downbeat positions. Such a time-frequency design makes an effective use of spectral features and achieves the state-of-the-art performance. 

Our work is also a Transformer-based architecture that strives to enhance beat tracking with richer musical contexts. Instead of aggregating spectral features as in [15], we resort to demixed instrumental attention as a more explicit inductive bias to exploring spectral information. Our design of dilated self-attention is also a crucial step to accommodate Transformer to beat tracking. With only linear complexity, our model handles full-length songs at a time. 

## 3. METHOD 

The core of our method is a Transformer encoder based on 1) dilated self-attention (DSA), and 2) demixed instrumental attention, to extract a framewise beat activation from input spectrograms. In this section, we first formalize DSA in Section 3.1. We then present our design of demixed beat tracking in Section 3.2. We further interpret our method with Markov chain properties in Section 3.3. 

## 3.1 Dilated Self-Attention (DSA) 

## 3.1.1 Background of Self-Attention (SA) 

We first recall that, for vanilla Transformer layers, selfattention (SA) is computed via the scaled dot product: 



<!-- Start of picture text -->
Attention(Q, K, V ) = softmax ( Q K ⊤ ) V, (1)<br>√ df<br><!-- End of picture text -->

where Q1:T , K1:T , V1:T ∈ R<sup>T ×df</sup> are query, key, and value sequences, each linearly mapped from input x1:T . T is the sequence length, and df is the feature dimension. 

The partial attention from position i to j is explicitly: 



<!-- Start of picture text -->
j<br>eij = QiK ⊤ , (2)<br>√ df<br><!-- End of picture text -->

where 1 ≤ i, j ≤ T . Such computation leads to quadratic complexity O(T<sup>2</sup> ) in terms of both time and space. 

## 3.1.2 Dilated Self-Attention (DSA) 

An illustration of DSA is shown in Figure 1. DSA is computed over a short window of size lwin = m + n + 1, where m and n are the length of non-causal and causal components of the window (in Figure 1, m = n = 2). Each Transformer layer has a dilation rate r ⩾ 1, and r increases exponentially as the layer goes deeper. 

Formally, given Q, K, and V ∈ R<sup>T ×df</sup> , DSA first computes Q-K attention by: 



<!-- Start of picture text -->
i + rk<br>eik = Qi √ K d ⊤ f , (3)<br><!-- End of picture text -->

where 1 ≤ i ≤ T and −m ≤ k ≤ n. Specifically, i + rk refers to the positions in K1:T that are attainable by Qi under the dilated window of rate r. When i + rk exceeds the sequence range [1, T ], we fill eik with −inf. 

170 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
Layer 3  𝐾𝐾𝑗𝑗<br>Dilation 22 2<br>Layer 2<br>Dilation 22 1<br>𝑄𝑄𝑖𝑖<br>Layer 1<br>Dilation 22 0<br>(a) Layer-wise view of dilated self-attention (Adapted from TCN structures [9,27]) (b) Attention matrix view at layer 2<br>Figure 1:: Illustration of dilated self-attention (with a non-causal short window of size 5) over a three-layer Transformer.<br>Part (a) shows the hierarchical connectivity across layers, which shares the same pattern as TCN in [9]. Part (b) shows the<br>attention matrix at layer 2, with colours indicating relative position. The white colour indicates unattainable positions.<br>Instrumental<br>0 1 2 3 4 5 6 7 8 9 ⋯⋯ Transformer<br>Padded 𝐾𝐾/𝑉𝑉𝐾𝐾/𝑉𝑉/𝑉𝑉𝑉𝑉<br>0 1 2 3 4 5 6 7 8 9 Layer with SA<br>Demixed<br>0 1 2 3 4 5 6 7 8 9 rolling and  Transformer<br>concatenation𝐾𝐾/𝑉𝑉𝐾𝐾/𝑉𝑉/𝑉𝑉𝑉𝑉<br>2 3 4 5 6 7 8 9 0 1 Block  other<br>4 5 6 7 8 9 0 1 2 3 Temporal Transformer Layer  drumbass<br>with DSA piano<br>vocal<br>0 1 2 3 4 5 6 7 8 9<br>𝑇𝑇<br>𝑄 1:𝑇𝑇𝑄𝑄<br><!-- End of picture text -->



<!-- Start of picture text -->
Layer 3<br>Dilation 22 2<br>Layer 2<br>Dilation 22 1<br>Layer 1<br>Dilation 22 0<br><!-- End of picture text -->

Figure 1:: Illustration of dilated self-attention (with a non-causal short window of size 5) over a three-layer Transformer. Part (a) shows the hierarchical connectivity across layers, which shares the same pattern as TCN in [9]. Part (b) shows the attention matrix at layer 2, with colours indicating relative position. The white colour indicates unattainable positions. 



<!-- Start of picture text -->
0 1 2 3 4 5 6 7 8 9<br>Padded 𝐾𝐾/𝑉𝑉𝐾𝐾/𝑉𝑉/𝑉𝑉𝑉𝑉<br>0 1 2 3 4 5 6 7 8 9<br>0 1 2 3 4 5 6 7 8 9 rolling and<br>concatenation𝐾𝐾/𝑉𝑉𝐾𝐾/𝑉𝑉/𝑉𝑉𝑉𝑉<br>2 3 4 5 6 7 8 9 0 1<br>4 5 6 7 8 9 0 1 2 3<br>0 1 2 3 4 5 6 7 8 9<br>𝑄 1:𝑇𝑇𝑄𝑄<br><!-- End of picture text -->

Figure 3: Demixed Transformer block. Two Transformer layers are stacked ªorthogonallyº, each handling time-wise dilated self-attention and instrument-wise self-attention. 

Figure 2: Illustration of efficient DSA implementation, with dilation rate r = 2 and window size lwin = 5. 

Then, the Q-K attention eik is normalized via softmax: 



<!-- Start of picture text -->
ex p( eik )<br>pik = (4)<br>�n k=−m exp(eik)<br><!-- End of picture text -->

The output of DSA is a sequence z1:T , where zi is the weighted average of V under the same dilated window: 



<!-- Start of picture text -->
n<br>zi = � pik(Vi+rk) (5)<br>k=−m<br><!-- End of picture text -->

We apply DSA with exponentially increasing dilation rates and relative positional embedding (RPE) [32] to a stack of Transformer layers. Each layer consists of two sub-layers: DSA, and a position-wise feed-forward layer. We place residual connections across each sub-layer and perform layer normalization [33] before each sub-layer. 

## 3.1.3 Memory Efficient Implementation of DSA 

A straightforward implementation of DSA is to mask SA. Concretely, a square mask takes the same form as in Figure 1b, where all uncolored positions are filled with −inf, rendering a rather sparse attention matrix. This way, however, still requires quadratic complexity, because eij is explicitly computed for all masked positions. 

Our implementation takes a ªrollingº strategy to eliminate redundant computation. As in Figure 2, lwin copies of K1:T sequences are padded and rolled along the time axis, and then concatenated on a new axis. In this way, each Qi sees Kj directly and only at j = i + rk for −m ≤ k ≤ n, which is exactly the coverage of the dilated window. 

Formally, given K1:T ∈ R<sup>T ×df</sup> , dilation rate r, and window size lwin, the rolling strategy takes three steps: 

1. Pad K1:T with <mark>⌊</mark><sup><mark>lwin</mark></sup> 2<sup><mark>⌋</mark>× r steps on both sides;</sup> 

2. Make lwin copies of padded K. Starting from 0, each copy is cyclically rolled r more steps; 

3. Concatenate each copy along a new axis and retrieve the first T steps. The output has shape T × lwin × df . 

The same procedure applies to V1:T as well. In this way, computing DSA is essentially as simple as Equation (1). Here, instead of Q, K, V ∈ R<sup>T ×df</sup> , we have Q ∈ R<sup>T ×1×df</sup> and K, V ∈ R<sup>T ×lwin×df</sup> , with T treated as a batch dimension. The computation complexity is O(T × lwin), while lwin is fixed and small enough to be left uncounted. 

## 3.2 Demixed Beat Tracking 

## 3.2.1 Demixed Transformer Block 

We use Spleeter 5-stems model [22] to demix an input piece into spectrograms with |C| instrument channels, where C = {vocal, piano, drum, bass, other}. As shown in Figure 3, we stack two Transformer layers to perform time-wise and instrument-wise attention in turn. Let the input at layer l be x<sup>l</sup> 1:T,1:|C|<sup>∈RT ×|C|×df, a temporal</sup> Transformer layer (TTL) first takes x<sup>l</sup> 1:T,c<sup>for 1 ≤c ≤|C|:</sup> 



<!-- Start of picture text -->
x l 1: +1 T,c = TTL(x 1: l T,c ) (6)<br><!-- End of picture text -->

Then, an instrumental Transformer layer (ITL), on the orthogonal direction, takes x<sup>l</sup> t,<sup>+1</sup> 1:|C|<sup>for 1 ≤t ≤T:</sup> 



<!-- Start of picture text -->
x l t, +2 1:|C| = ITL(xl t, +1 1:|C| ) (7)<br><!-- End of picture text -->

A TTL followed by ITL forms a demixed Transformer block. TTL consists of DSA as described in Section 3.1.2. 

171 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
Pre-Processing𝐹𝐹= 128 Transformer Layers Demixed Transformer Block Post-Processing<br>31 5 SA (instrumental)<br>32 64 256 Beat<br>𝑇𝑇 𝑇𝑇 𝑇𝑇 𝑇𝑇 Downbeat<br>Feed-Forward<br>vocal<br>pianodrum<br>bass<br>Demixingother Convolution & Pooling ×3 ×3 ×3 Temporal  Tempo<br>Pooling<br>DBN<br>(temporal)DSA  Feed-Forward (temporal)DSA  Feed-Forward (temporal)DSA  Feed-Forward<br>Linear & Sigmoid<br><!-- End of picture text -->

Figure 4: Beat Transformer architecture. For conciseness, layer normalization and dropout layers are not shown. 

For ITL, we use vanilla SA because there is only 5 instrument channels. As instruments are not sequentially ordered, we do not add any positional encoding to ITL. 

Through demixed Transformer blocks, our model can capture the rhythmic evolution of each instrument, as well as the harmonic coordination among all instruments. 

## 3.2.2 Partial Demix Augmentation 

Spleeter may produce empty channels when a certain instrument does not present. To avoid potential effects of such a situations, we develop a partial demix strategy for data augmentation. Partial demix creates new stems by summing up existing instrument channels of a default 5- stem demixed input sample. For example, an augmented data sample may have three channels corresponding to C<sup>′</sup> = {vocal&piano, drum, bass&other}. 

In our case, we randomly sum up 2, 3, or 4 instrument channels of a 5-stem input with a probability 30%, 10%, and 10% during training. In this way, our model is encouraged to pay attention to instrument-agnostic musical contents and thus is less affected by empty channels where no valid music content is present. As our augmentation strategy also adds to the demix diversity and the data quantity, we believe it brings general benefits to training as well. 

## 3.3 Markov Chain Interpretation 

In Equation (4), we formulate the attention matrix of DSA as P = [pij]1≤i,j≤T , where pij ≥ 0 if and only if j = i + rk for −m ≤ k ≤ n. Here, r is the dilation rate, and m, n are components of the attention window. Moreover, P satisfies<sup>�T</sup> j=1<sup>pij=1foralli.Therefore,Pcanbe</sup> regarded as the transition matrix of a finite-state Markov chain, where each state is a position of the input sequence. 

For a stack of temporal Transformer layers (TTL), where DSA is employed, layer l essentially learns a unique one-step transition P<sup>l</sup> , by which our model can attend to local neighbours covered by the attention window. Through L layers, our model makes an L-step transition, during which it attends to global positions hierarchically. The overall L-step transition matrix P<sup>(L)</sup> satisfies: 



<!-- Start of picture text -->
L<br>P (L) = � P l (8)<br>l=1<br><!-- End of picture text -->

Note that P<sup>l</sup> itself is a rather sparse matrix (due to short attention window), while P<sup>(L)</sup> is densely connected. Its 

components [p<sup>(</sup> ij<sup>L)]1≤i,j≤Trepresent the hierarchical atten-</sup> tion weights across the whole L layers, which can tell us much richer attention patterns (more in Section 4.4). 

## 3.4 Complete Architecture 

A complete view of Beat Transformer is presented in Figure 4. The inputs are log-scaled spectrograms demixed by Spleeter, with F = 128 mel-bins and |C| = 5 instrument channels. Subject to Spleeter, our frame rate is 43.07 fps and the frequency range is up to 11 kHz. We then use three 2D convolutional layers, shared by each demixed channel, as a front-end feature extractor. The convolutional design is the same as in [13] except that we employ more filters to reach feature dimension dmodel = 256. 

Beat Transformer comprises 9 temporal Transformer layers (TTL) with DSA. Each TTL has 8 attention heads with window size lwin = 5, four of which have skewed window ranges, where m = 0, 1, 3, 4, respectively, and n = 4 − m. The dilation rate grows exponentially from 2<sup>0</sup> to 2<sup>8</sup> , stretching to a receptive field of 47.51 seconds. Among the 9 TTLs, the middle three are expanded to demixed Transformer blocks by interleaving ITLs. We found it sufficient to perform instrumental attention only in the middle layers, which has a proper scale of 1-5 seconds. Each Transformer layer has 8 heads (df = 32) followed by a feed-forward layer with hidden dimension dff = 1024. 

We sum up the instrument channels of the output of the last Transformer layer and obtain a frame-wise beat representation of shape T × dmodel. Following multi-task learning practice [11±14], we use a linear layer to map the representation to beat and downbeat activations respectively, and add a regularization branch predicting global tempo via ªskip connectionsº [12]. We apply DBN in Madmom package [34] as the post-processor to pick up the beat and downbeat sequence from raw activations. For DBN parameters, we set observation_lambda = 6, transition_lambda = 100, and threshold = 0.2. 

## 4. EXPERIMENTS 

## 4.1 Datasets 

We utilize a total of 7 datasets for model training and evaluation: Ballroom [35, 36], Hainsworth [37], RWC Popular [38], Harmonix [39], Carnetic [40], SMC [41], 

172 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

|||Bea|t Accuracy||Down|beat Accura|cy|
|---|---|---|---|---|---|---|---|
|Dataset|Model|F-Measure|CMLt|AMLt|F-Measure|CMLt|AMLt|
||TCN+Demix|0.960|0.942|0.960|0.925|0.924|0.956|
||Ours w/o Demix|0.968|0.946|0.965|0.930|0.925|0.963|
||Ours w/o Aug.|0.967|0.949|0.967|0.928|0.931|0.958|
|Ballroom|<br>Ours|0.968|0.954|0.966|0.941|0.944|0.969|
||Böcket al.[13]|0.962|0.947|0.961|0.916|0.913|0.960|
||Hunget al.[15]|0.962|0.939|0.967|0.937|0.927|0.968|
||TCN+Demix|0.887|0.827|0.918|0.739|0.708|0.861|
||Ours w/o Demix|0.902|0.844|0.934|0.721|0.688|0.843|
||Ours w/o Aug.|0.892|0.831|0.908|0.742|0.703|0.837|
|Hainsworth|Ours|0.902|0.842|0.918|0.748|0.712|0.841|
||Böcket al.[13]|0.904|0.851|0.937|0.722|0.696|0.872|
||Hunget al.[15]|0.877|0.862|0.915|0.748|0.738|0.870|
||TCN+Demix|0.954|0.903|0.956|0.901|0.866|0.923|
||Ours w/o Demix|0.954|0.902|0.958|0.887|0.846|0.916|
||Ours w/o Aug.|0.952|0.901|0.950|0.897|0.863|0.919|
|Harmonix|<br>Ours<br>|0.954|0.905|0.957|0.898|0.863|0.919|
||Böcket al.[13]<sup>∗</sup>|0.933|0.841|0.938|0.804|0.747|0.873|
||Hunget al.[15]|0.953|0.939|0.959|0.908|0.872|0.928|
||TCN+Demix|0.596|0.455|0.625||||
||Ours w/o Demix|0.589|0.448|0.621||||
||Ours w/o Aug.|0.595|0.450|0.626||||
|SMC|<br>Ours|0.596|0.456|0.635||||
||Böcket al.[13]|0.552|0.465|0.643||||
||Hunget al.[15]|0.605|0.514|0.663||||
||TCN+Demix|0.873|0.780|0.907|0.700|0.646|0.842|
||Ours w/o Demix|0.876|0.787|0.914|0.686|0.633|0.834|
||Ours w/o Aug.|0.881|0.797|0.921|0.703|0.653|0.845|
|GTZAN|<br>Ours|0.885|0.800|0.922|0.714|0.665|0.844|
||Böcket al.[13]<br>|0.885<br>|0.813|0.931|0.672<br>|0.640<br>|0.832<br>|
||Hunget al.[15]|0.887|0.812|0.920|0.756|0.715|0.881|



Table 1: Testing results of beat and downbeat tracking under 8-fold cross-validation. GTZAN is unseen from training and held out for test only. Böck et. al. [13] on Harmonix is reproduced by [15], as indicated by the<sup>∗</sup> symbol. We use <mark>underscore</mark> to denote best results comparing with our ablation models and use boldface to compare with state-of-the-art models. 

and GTZAN [42, 43]. We acquire Harmonix in melspectrogram and invert each piece to audio using GriffinLim Algorithm [44, 45] with Librosa package [46]. Following convention, we leave GTZAN for testing only and use the other datasets in 8-fold cross validation [11±13]. 

## 4.2 Training 

Our model is supervised in a multi-task learning fashion, where beat, downbeat, and tempo are predicted jointly [13]. Beat and downbeat annotations are each represented as a 1D binary sequence that indicates beat (1) and nonbeat (0) states at each input frame. Following [13], we widen beat and downbeat states to ±2 neighbours of annotated frames with weights 0.5 and 0.25. Following [12], we derive tempo target from beat annotation for the tempo prediction branch. We found the use of tempo branch generally beneficial to beat tracking, as it may serve as a regularization term that helps reaching better convergence. 

For training, we combine the binary cross entropy loss over beat, downbeat, and tempo by weighing them equally. We use a batch size of 1 to train on whole sequences with different lengths. For excessively long songs, we split them 

into 3-minute (8k-frame) clips. We apply RAdam [47] plus Lookahead [48] optimizer with an initial learning rate of 1e−3, which is reduced by a factor of 5 whenever the validation loss gets stuck for 2 epochs before being capped at a minimum value of 1e−7. We use dropout [49] with rate 0.5 for the tempo branch and 0.1 for other parts of the network. We apply partial demix augmentation described in Section 3.2.2 as the only means of data augmentation. Our model has 9.29M trainable parameters and is trained with an RTX-A5000-24GB GPU. Each training fold generally takes 20 epochs (in 11 hours) to fully converge. 

## 4.3 Evaluation 

## 4.3.1 Baseline Methods 

We first compare three ablation models to validate our module design. The first ablation model is Ours trained without partial demix augmentation (Ours w/o Aug.). The second model removes all ITL layers and tracks beat with a single channel of non-demixed mixture (Ours w/o Demix). The last model replaces each TTL layer with a TCN layer [13] of the same dilation rate (TCN+Demix). We imple- 

173 

Proceedings of the 23rd ISMIR Conference, Ben𝑏𝑘𝑏 𝑘𝑏galuru, India, December 4-8𝑑𝑘𝑑𝑘𝑑𝑏galuru, India, December 4-8𝑑𝑘𝑑𝑘𝑑𝑑𝑘𝑑𝑘𝑑𝑘𝑑𝑘𝑑𝑑𝑘𝑑𝑘𝑑𝑑 <u>, 2022</u> 



<!-- Start of picture text -->
𝑏𝑘𝑏𝑘𝑏𝑏 𝑘𝑏galuru, India, December 4-8𝑑𝑘𝑑𝑘𝑑𝑏galuru, India, December 4-8𝑑𝑘𝑑𝑘𝑑𝑑𝑘𝑑𝑘𝑑𝑘𝑑𝑘𝑑𝑑𝑘𝑑𝑘𝑑𝑑<br>𝐾𝐾𝑗𝑗 𝐾𝐾𝑗𝑗 𝐾𝐾𝑗𝑗 𝐾𝐾𝑗𝑗<br>𝑄𝑄𝑖𝑖 𝑄𝑄𝑖𝑖 𝑄𝑄𝑖𝑖 𝑄𝑄𝑖𝑖<br>𝑑 𝑘𝑘−1𝑑<br>𝑏 𝑘𝑘−1𝑏 𝑏 𝑘𝑘−1𝑏<br>𝑏 𝑘𝑘𝑏 𝑏 𝑘𝑘𝑏 𝑑 𝑘𝑘𝑑<br>𝑏 𝑘𝑘+1𝑏 𝑏 𝑘𝑘+1𝑏<br>𝑑 𝑘𝑘+1𝑑<br>𝑏 𝑘𝑘−1𝑏 𝑏 𝑘𝑘𝑏 𝑏 𝑘𝑘+1𝑏 𝑏 𝑘𝑘−1𝑏 𝑏 𝑘𝑘𝑏 𝑏 𝑘𝑘+1𝑏 𝑑 𝑘𝑘−1𝑑 𝑑 𝑘𝑘𝑑 𝑑 𝑘𝑘+1𝑑<br>(a) P (1) lower scale (b) P (3) beat scale (c) P (5) downbeat scale (d) P (9) higher scale<br><!-- End of picture text -->

Figure 5: Visualization of temporal attention matrix based on the product rule in Equation (8) for L-step transition on a Markov chain. L = 1, 3, 5, and 9 from part (a) to (d), which model different hierarchies of the metrical structure. 

ment TCN layers following [23] while setting the input and output shape to be the same as our model. The resulting model yields a comparable amount of 10.25M parameters and is trained without augmentation. 

In addition, we compare our model with two recent works that have achieved state-of-the-art performance. Specifically, Böck et al. [13] is based on TCN architectures and Hung et al. [15] is based on SpecTNT. 

## 4.3.2 Results and Discussion 

In Table 1, we first observe Ours w/o Aug. yields generally better performance than TCN+Demix, especially on the unseen GTZAN dataset. As both models share a comparable amount of parameters, this result demonstrates the capability of Transformer (DSA) versus TCN (dilated convolution), which also corroborates with previous findings on Transformer’s comparability to convolution on general tasks [50±52]. Considering that Transformer is notoriously data-inefficient to train, it is remarkable that our model is well-trained with limited data without augmentation. We owe this merit to DSA, which not only prevents redundant computation but also makes musical sense in terms of the hierarchical structure of music metrical modelling. 

Comparing Ours w/o Demix to Ours w/o Aug., while both models are highly competitive in beat tracking, the latter demonstrates more superiority in downbeat tracking. Downbeat tracking is generally more difficult than beat tracking because it is involved with deeper musical knowledge, such as chord and bass progression, behind the apparent spectrogram energy. In our model, the instrumental attention captures the instrumental coordination as hints to the harmonic cues that are orthogonal to the temporal axis, and thus acquires better metrical modelling. 

Comparing Ours w/o Aug. to Ours, we observe a consistent improvement across datasets brought by partial demix augmentation, which indicates the general usefulness of this augmentation strategy to model training. 

Compared to state-of-the-art models, our improvement in downbeat accuracy is more significant than that in beat accuracy. On the test-only GTZAN dataset, we obtain 4% point gain in F-measure over Böck et al. [13] in downbeat tracking. Compared to Hung et al. [15], which is also based on Transformer, our model can be more flexibly trained (owing to the efficient DSA mechanism) on a 24GB GPU in contrast to four 32GB GPUs reported in [15]. 

## 4.4 Attention Matrix Visualization 

We visualize the attention matrix that our model learns by interpreting it as a multi-step Markov transition matrix as defined in Equation (8). Specifically, the L-step matrix is the product of L one-step matrices through L layers. Here we only consider TTLs with dilated self-attention, as ITLs work on an orthogonal axis. Figure 5 shows the attention matrix P<sup>(L)</sup> for L = 1, 3, 5, and 9 of the drum channel, inferred from the piece hiphop.00090 chosen from GTZAN. 

Figure 5a shows a one-step transition. Each position Qi can only attend to its neighbours covered by the attention window. Still, we observe that beat positions (denoted by bk) are likely to get more attention. In Figure 5b where we step to the beat scale, most attention spots are aligned with beats. Moreover, we observe that the attention at bk is typically prolonged after Qi leaves bk, and is formed before Qi reaches bk for every k. This means that our model learns to transition its attention from the offbeat phase following the last beat to the upbeat phase preceding the next beat. Figure 5c further stretches the view to the downbeat scale, and we can see similar patterns aligned with downbeat positions (denoted by dk). Finally, in Figure 5d, the attention reaches further positions and displays a structural pattern. 

The above visualization demonstrates the inner logic that our model exploits for beat and downbeat tracking. We see that our model gathers information from both local and global scales with an organized hierarchy. 

## 5. CONCLUSION 

In conclusion, we contribute a novel Transformer architecture for audio beat and downbeat tracking. The main novelty lies first in our design of dilated self-attention, which brings down the computation complexity of Transformer from quadratic to linear level. In addition, we successfully enhance beat and downbeat tracking by utilizing off-theshelf progress in music demixing. Our model not only captures deeper harmonic cues for better metrical inference but also discerns beat and downbeat in a visualizable hierarchical manner. Our model is efficient, interpretable, and potentially generalizable with highly competitive sequential modelling power. We hope our model encourages future MIR research toward universal music understanding. 

174 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

## 6. REFERENCES 

- [1] A. Holzapfel and E. Benetos, ªThe sousta corpus: Beat-informed automatic transcription of traditional dance tunes,º in Proceedings of the 17th International Society for Music Information Retrieval Conference, ISMIR, 2016, pp. 531±537. 

- [2] G. Shibata, R. Nishikimi, and K. Yoshii, ªMusic structure analysis based on an LSTM-HSMM hybrid model,º in Proceedings of the 21th International Society for Music Information Retrieval Conference, ISMIR, 2020, pp. 23±29. 

- [3] R. Nishikimi, E. Nakamura, M. Goto, K. Itoyama, and K. Yoshii, ªBayesian singing transcription based on a hierarchical generative model of keys, musical notes, and F0 trajectories,º IEEE ACM Transactions on Audio, Speech, and Language Processing, vol. 28, pp. 1678±1691, 2020. 

- [4] R. Ishizuka, R. Nishikimi, and K. Yoshii, ªGlobal structure-aware drum transcription based on selfattention mechanisms,º Signals, vol. 2, no. 3, pp. 508± 526, 2021. 

- [5] C. Donahue and P. Liang, ªSheet sage: Lead sheets from music audio,º 2021, Late Breaking Demo in the 22nd International Society for Music Information Retrieval Conference, ISMIR. [Online]. Available: https://archives.ismir.net/ismir2021/ latebreaking/000049.pdf 

- [6] T. Bi, P. Fankhauser, D. Bellicoso, and M. Hutter, ªReal-time dance generation to music for a legged robot,º in 2018 IEEE/RSJ International Conference on Intelligent Robots and Systems, IROS. IEEE, 2018, pp. 1038±1044. 

- [7] K. Yamamoto, ªHuman-in-the-loop adaptation for interactive musical beat tracking,º in Proceedings of the 22nd International Society for Music Information Retrieval Conference, ISMIR, 2021, pp. 794±801. 

- [8] Z. Cai, R. J. Ellis, Z. Duan, H. Lu, and Y. Wang, ªBasic evaluation of auditory temporal stability (beats): A novel rationale and implementation,º in Proceedings of the 14th International Society for Music Information Retrieval Conference, ISMIR, 2013, pp. 541±546. 

- [9] E. P. MatthewDavies and S. Böck, ªTemporal convolutional networks for musical audio beat tracking,º in 27th European Signal Processing Conference, EUSIPCO. IEEE, 2019, pp. 1±5. 

- [10] F. Krebs, S. Böck, and G. Widmer, ªAn efficient statespace model for joint tempo and meter tracking,º in Proceedings of the 16th International Society for Music Information Retrieval Conference, ISMIR, 2015, pp. 72±78. 

- [11] S. Böck, F. Krebs, and G. Widmer, ªJoint beat and downbeat tracking with recurrent neural networks,º in 

   - Proceedings of the 17th International Society for Music Information Retrieval Conference, ISMIR, 2016, pp. 255±261. 

- [12] S. Böck, M. E. P. Davies, and P. Knees, ªMulti-task learning of tempo and beat: Learning one to improve the other,º in Proceedings of the 20th International Society for Music Information Retrieval Conference, ISMIR, 2019, pp. 486±493. 

- [13] S. Böck and M. E. P. Davies, ªDeconstruct, analyse, reconstruct: How to improve tempo, beat, and downbeat estimation,º in Proceedings of the 21th International Society for Music Information Retrieval Conference, ISMIR, 2020, pp. 574±582. 

- [14] T. Oyama, R. Ishizuka, and K. Yoshii, ªPhase-aware joint beat and downbeat estimation based on periodicity of metrical structure,º in Proceedings of the 22nd International Society for Music Information Retrieval Conference, ISMIR, 2021, pp. 493±499. 

- [15] Y. Hung, J. Wang, X. Song, W. T. Lu, and M. Won, ªModeling beats and downbeats with a time-frequency transformer,º in IEEE International Conference on Acoustics, Speech and Signal Processing, ICASSP. IEEE, 2022, pp. 401±405. 

- [16] W.-T. Lu, J.-C. Wang, M. Won, K. Choi, and X. Song, ªSpecTNT: A time-frequency transformer for music audio,º in Proceedings of the 22nd International Society for Music Information Retrieval Conference, ISMIR, 2021, pp. 396±403. 

- [17] C. Hawthorne, I. Simon, R. Swavely, E. Manilow, and J. Engel, ªSequence-to-sequence piano transcription with transformers,º in Proceedings of the 22nd International Society for Music Information Retrieval Conference, ISMIR, 2021, pp. 246±253. 

- [18] L. Ou, Z. Guo, E. Benetos, J. Han, and Y. Wang, ªExploring transformer’s potential on automatic piano transcription,º in IEEE International Conference on Acoustics, Speech and Signal Processing, ICASSP. IEEE, 2022, pp. 776±780. 

- [19] J. Gardner, I. Simon, E. Manilow, C. Hawthorne, and J. H. Engel, ªMT3: multi-task multitrack music transcription,º in The Tenth International Conference on Learning Representations, ICLR. OpenReview.net, 2022. 

- [20] M. Won, S. Chun, and X. Serra, ªToward interpretable music tagging with self-attention,º arXiv preprint arXiv:1906.04972, 2019. 

- [21] M. Won, K. Choi, and X. Serra, ªSemi-supervised music tagging transformer,º in Proceedings of the 22nd International Society for Music Information Retrieval Conference, ISMIR, 2021, pp. 769±776. 

175 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

- [22] R. Hennequin, A. Khlif, F. Voituret, and M. Moussallam, ªSpleeter: a fast and efficient music source separation tool with pre-trained models,º Journal of Open Source Software, vol. 5, no. 50, p. 2154, 2020, deezer Research. [Online]. Available: https://doi.org/10.21105/joss.02154 

- [23] M. E. Davies, S. Böck, and M. Fuentes, Tempo, Beat and Downbeat Estimation, 2021. [Online]. Available: https://tempobeatdownbeat.github.io/tutorial/ intro.html 

- [24] T. Lin, Y. Wang, X. Liu, and X. Qiu, ªA survey of transformers,º arXiv preprint arXiv:2106.04554, 2021. 

- [25] S. Böck and M. Schedl, ªEnhanced beat tracking with context-aware neural networks,º in Proceedings of the 14th International Conference on Digital Audio Effects, DAFx, 2011, pp. 135±139. 

- [26] S. Böck, F. Krebs, and G. Widmer, ªA multi-model approach to beat tracking considering heterogeneous music styles,º in Proceedings of the 15th International Society for Music Information Retrieval Conference, ISMIR, 2014, pp. 603±608. 

- [27] A. van den Oord, S. Dieleman, H. Zen, K. Simonyan, O. Vinyals, A. Graves, N. Kalchbrenner, A. W. Senior, and K. Kavukcuoglu, ªWavenet: A generative model for raw audio,º in The 9th ISCA Speech Synthesis Workshop. ISCA, 2016, p. 125. 

- [28] C. Chiu, J. Ching, W. Hsiao, Y. Chen, A. W. Su, and Y. Yang, ªSource separation-based data augmentation for improved joint beat and downbeat tracking,º in 29th European Signal Processing Conference, EUSIPCO. IEEE, 2021, pp. 391±395. 

- [29] C. Chiu, A. W. Su, and Y. Yang, ªDrum-aware ensemble architecture for improved joint musical beat and downbeat tracking,º IEEE Signal Processing Letters, vol. 28, pp. 1100±1104, 2021. 

- [30] R. Dai, S. Das, L. Minciullo, L. Garattoni, G. Francesca, and F. Brémond, ªPDAN: pyramid dilated attention network for action detection,º in IEEE Winter Conference on Applications of Computer Vision, WACV. IEEE, 2021, pp. 2969±2978. 

- [31] N. Moritz, T. Hori, and J. L. Roux, ªCapturing multiresolution context by dilated self-attention,º in IEEE International Conference on Acoustics, Speech and Signal Processing, ICASSP. IEEE, 2021, pp. 5869± 5873. 

- [32] P. Shaw, J. Uszkoreit, and A. Vaswani, ªSelf-attention with relative position representations,º in Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, NAACL-HLT, Volume 2. Association for Computational Linguistics, 2018, pp. 464±468. 

- [33] J. L. Ba, J. R. Kiros, and G. E. Hinton, ªLayer normalization,º arXiv preprint arXiv:1607.06450, 2016. 

- [34] S. Böck, F. Korzeniowski, J. Schlüter, F. Krebs, and G. Widmer, ªmadmom: A new python audio and music signal processing library,º in Proceedings of the 2016 ACM Conference on Multimedia Conference, MM. ACM, 2016, pp. 1174±1178. 

- [35] F. Gouyon, A. Klapuri, S. Dixon, M. Alonso, G. Tzanetakis, C. Uhle, and P. Cano, ªAn experimental comparison of audio tempo induction algorithms,º IEEE Transactions on Audio, Speech, and Language Processing, vol. 14, no. 5, pp. 1832±1844, 2006. 

- [36] F. Krebs, S. Böck, and G. Widmer, ªRhythmic pattern modeling for beat and downbeat tracking in musical audio,º in Proceedings of the 14th International Society for Music Information Retrieval Conference, ISMIR, 2013, pp. 227±232. 

- [37] S. W. Hainsworth and M. D. Macleod, ªParticle filtering applied to musical tempo tracking,º EURASIP Journal on Advances in Signal Processing, vol. 2004, no. 15, pp. 1±11, 2004. 

- [38] M. Goto, H. Hashiguchi, T. Nishimura, and R. Oka, ªRWC music database: Popular, classical and jazz music databases,º in ISMIR 2002, 3rd International Conference on Music Information Retrieval, 2002. 

- [39] O. Nieto, M. McCallum, M. E. P. Davies, A. Robertson, A. M. Stark, and E. Egozy, ªThe harmonix set: Beats, downbeats, and functional segment annotations of western popular music,º in Proceedings of the 20th International Society for Music Information Retrieval Conference, ISMIR, 2019, pp. 565±572. 

- [40] A. Srinivasamurthy and X. Serra, ªA supervised approach to hierarchical metrical cycle tracking from audio music recordings,º in IEEE International Conference on Acoustics, Speech and Signal Processing, ICASSP. IEEE, 2014, pp. 5217±5221. 

- [41] A. Holzapfel, M. E. P. Davies, J. R. Zapata, J. L. Oliveira, and F. Gouyon, ªSelective sampling for beat tracking evaluation,º IEEE Transactions on Speech and Audio Processing, vol. 20, no. 9, pp. 2539±2548, 2012. 

- [42] G. Tzanetakis and P. R. Cook, ªMusical genre classification of audio signals,º IEEE Transactions on Speech and Audio Processing, vol. 10, no. 5, pp. 293±302, 2002. 

- [43] U. Marchand and G. Peeters, ªSwing ratio estimation,º in Proceedings of the 18th International Conference on Digital Audio Effects, DAFx, 2015. 

- [44] D. Griffin and J. Lim, ªSignal estimation from modified short-time fourier transform,º IEEE Transactions on acoustics, speech, and signal processing, vol. 32, no. 2, pp. 236±243, 1984. 

176 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

- [45] N. Perraudin, P. Balázs, and P. L. Sùndergaard, ªA fast griffin-lim algorithm,º in IEEE Workshop on Applications of Signal Processing to Audio and Acoustics, WASPAA. IEEE, 2013, pp. 1±4. 

- [46] B. McFee, C. Raffel, D. Liang, D. P. Ellis, M. McVicar, E. Battenberg, and O. Nieto, ªlibrosa: Audio and music signal analysis in python,º in Proceedings of the 14th python in science conference, vol. 8. Citeseer, 2015, pp. 18±25. 

- [47] L. Liu, H. Jiang, P. He, W. Chen, X. Liu, J. Gao, and J. Han, ªOn the variance of the adaptive learning rate and beyond,º in 8th International Conference on Learning Representations, ICLR. OpenReview.net, 2020. 

- [48] M. R. Zhang, J. Lucas, J. Ba, and G. E. Hinton, ªLookahead optimizer: k steps forward, 1 step back,º in Advances in Neural Information Processing Systems 32: Annual Conference on Neural Information Processing Systems, NeurIPS, 2019, pp. 9593±9604. 

- [49] N. Srivastava, G. E. Hinton, A. Krizhevsky, I. Sutskever, and R. Salakhutdinov, ªDropout: a simple way to prevent neural networks from overfitting,º Journal of Machine Learning Research, vol. 15, no. 1, pp. 1929±1958, 2014. 

- [50] A. Dosovitskiy, L. Beyer, A. Kolesnikov, D. Weissenborn, X. Zhai, T. Unterthiner, M. Dehghani, M. Minderer, G. Heigold, S. Gelly, J. Uszkoreit, and N. Houlsby, ªAn image is worth 16x16 words: Transformers for image recognition at scale,º in 9th International Conference on Learning Representations, ICLR, 2021. 

- [51] H. Touvron, M. Cord, M. Douze, F. Massa, A. Sablayrolles, and H. Jégou, ªTraining data-efficient image transformers & distillation through attention,º in Proceedings of the 38th International Conference on Machine Learning, ICML, ser. Proceedings of Machine Learning Research, vol. 139. PMLR, 2021, pp. 10 347±10 357. 

- [52] Z. Liu, Y. Lin, Y. Cao, H. Hu, Y. Wei, Z. Zhang, S. Lin, and B. Guo, ªSwin transformer: Hierarchical vision transformer using shifted windows,º in 2021 IEEE/CVF International Conference on Computer Vision, ICCV. IEEE, 2021, pp. 9992±10 002. 

177 

