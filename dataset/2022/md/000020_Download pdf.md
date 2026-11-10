---
paper_id: "000020"
year: 2022
title: "Download pdf"
source_url: "https://zenodo.org/record/7342916/files/000020.pdf"
---

# SKETCHING THE EXPRESSION: FLEXIBLE RENDERING OF EXPRESSIVE PIANO PERFORMANCE WITH SELF-SUPERVISED LEARNING 

Seungyeon Rhyu<sup>1</sup> Sarah Kim<sup>2</sup> Kyogu Lee<sup>1,3</sup> 

1 Music and Audio Research Group (MARG), Seoul National University, South Korea 

2 Krust Universe, South Korea 

3 Graduate School of AI, AI Institute, Seoul National University, South Korea 

rsy1026@snu.ac.kr, estelle.kim@krustuniverse.com, kglee@snu.ac.kr 

## ABSTRACT 

We propose a system for rendering a symbolic piano performance with flexible musical expression. It is necessary to actively control musical expression for creating a new music performance that conveys various emotions or nuances. However, previous approaches were limited to following the composer’s guidelines of musical expression or dealing with only a part of the musical attributes. We aim to disentangle the entire musical expression and structural attribute of piano performance using a conditional VAE framework. It stochastically generates expressive parameters from latent representations and given note structures. In addition, we employ self-supervised approaches that force the latent variables to represent target attributes. Finally, we leverage a two-step encoder and decoder that learn hierarchical dependency to enhance the naturalness of the output. Experimental results show that our system can stably generate performance parameters relevant to the given musical scores, learn disentangled representations, and control musical attributes independently of each other. 

## 1. INTRODUCTION 

Computational modeling of expressive music performance focuses on mimicking human behaviors that convey the music [1, 2]. For piano performance, one common task is to render an expressive performance from a quantized musical score. It aims to reproduce the loudness and timing of musical notes that fits to the given score. Most of the conventional studies have used musical scores of Western piano music that includes sufficient amount of guidelines for musical expressions [3±6]. Recent studies using deep learning methods have successfully rendered plausible piano performances that are comparable to those of professional pianists from the given Classical scores [7±9]. 

More recently, it has increased attention to controlling 

> © S. Rhyu, S. Kim, and K. Lee. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: S. Rhyu, S. Kim, and K. Lee, ªSketching the Expression: Flexible Rendering of Expressive Piano Performance with Self-Supervised Learningº, in Proc. of the 23rd Int. Society for Music Information Retrieval Conf., Bengaluru, India, 2022. 

music performance by manipulating one or more disentangled representations from a generative model. These representations are sensitive to the variation of certain factors while invariant to other factors [10]. Maezawa et al. aimed to control a performer’s interpretation through a conditional variational recurrent neural network (CVRNN) [11]. They intended to disentangle a time-variant representation of the personal interpretation. In the acoustic domain, Tan et al. proposed a generative model based on a Gaussian mixture variational autoencoder (GM-VAE) that separately controlled dynamics and articulations of the notes [12]. Their novelty lied in learning multiple representations of high-level attributes from the low-level spectrogram. 

However, these studies have constrained musical creativity. Maezawa et al. controlled musical expression only through quantized features from the musical scores. Tan et al. did not consider controlling tempo or timing with a latent representation. These methods may have restricted any potential for rendering piano performances with flexible musical expression. Musical creativity can be expanded not only by composers but also by performers who can elastically choose various strategies to highlight multiple nuances or emotions [13±15]. Moreover, the music generation field can be also broadened if static music created by automatic composition systems can be easily colored with realistic and elastic expression [16]. 

Therefore, we attempt a new approach that renders piano performances with flexible musical expressions. We disregard a typical assumption from previous studies that a performer must follow a composer’s intent [4,17±19]. According to the literature, performers learn to identify or imitate "expressive models", or explicit planning, of existing piano performances [20]. We focus on this attribute, defining it as a higher-level sketch of the expressive attributes (i.e. dynamics, articulation, and tempo [21]) that the performer draws based on a personal interpretation of the musical piece [4, 11, 20]. We also assume that the remaining attribute represents common performing strategies that are connected to certain musical patterns, while these strategies slightly differ across performers [22,23]. We call this attribute as a structural attribute that belongs to given note structures of a musical piece. 

In this study, we propose a generative model that can 

178 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

flexibly control the entire musical expression, or the explicit planning, of symbolic piano performance<sup>1</sup> . Our system is based on a conditional variational autoencoder (CVAE) that is modified for sequential data [11, 24]. The system generates multiple parameters of piano performance from a note structure of a musical passage, using disentangled representations for the explicit planning and structural attribute. 

We employ a self-supervised learning framework to force the latent representations to learn our target attributes [24±26]. In addition, we facilitate independent control of the three expressive attributes±dynamics, articulation, and tempo±by utilizing an existing method that aligns the latent code with a target attribute [27,28]. Finally, we design a novel mechanism that intuitively models a polyphonic structure of piano performance. In particular, we insert intermediate steps for chordwise encoding and decoding of the piano performance to our encoder-decoder architecture, where a chord denotes a group of simultaneous notes. 

Our approach has several contributions as follows: 1) Our system aims to control musical expression while maintaining any characteristics induced by a given musical structure; 2) We use self-supervised learning where new supervisory signals are involved in regularizing the latent representations effectively; 3) Our system aims to control multiple expressive attributes independently of each other; 4) Lastly, we leverage an intermediate step that projects a notewise representation into the chordwise in the middle of our system to intuitively model the polyphonic structure of piano performance. 

## 2. PROPOSED METHODS 

We aim to build a generative model that factorizes expressive piano performance as the explicit planning and structural attribute. The model is based on a conditional variational autoencoder (CVAE) that reproduces performance parameters based on a given musical structure. 

## 2.1 Data Representation 

We extract features that represent a human performance and the corresponding musical score, following the conventional studies [11,19,29]. 

Performance Features. We extract three features that represent the expressive attributes of each performed note, respectively: MIDIVelocity is a MIDI velocity value that ranges from 24 to 104. IOIRatio represents an instantaneous variation in tempo. We compute an inter-onsetinterval (IOI) between the onset of a note and the mean onset of the previous chord for both a performed note and the corresponding score note. Then, a ratio of performed IOI to score IOI is calculated, clipped between 0.125 and 8, and converted into a logarithmic scale [4]. Articulation represents how much a note is shortened or lengthened compared to the instantaneous tempo. It is a ratio of a performed duration to an IOI value between the onset of 

a note and mean onset of the next chord [19]. It is clipped between 0.25 and 4 and converted into a logarithmic scale. 

Score Features. The features for a musical score represent eight categorical attributes for how the notes are composed: Pitch is a MIDI index number that ranges from 21 to 108. RelDuration and RelIOI are 11-class attributes of a quantized duration and IOI between a note onset and a previous chord, respectively. They range from 1 to 11, and each class represents a multiple of a 16th note’s length with respect to a given tempo [30, 31]. IsTopVoice is a binary attribute of whether the note is the uppermost voice. It is heuristically computed regarding pitches and durations of surrounding notes. PositionInChord and NumInChord are 11-class attributes of a positional index of a note within its chord and the total number of notes in that chord, respectively, that range from 1 to 11. An index 1 for PositionInChord denotes the most bottom position. Staff is a binary attribute of the staff of a note, either of the G clef or F clef. IsDownbeat is a binary attribute of whether a note is at a downbeat or not. 

## 2.2 Modeling Musical Hierarchy 

Inspired by previous studies [4, 8, 9, 32], we build a twostep encoder and decoder: An encoder models both notewise and chordwise dependencies of the inputs, and a decoder reconstructs the notewise dependency from the chordwise representation and the notewise condition. We denote a chord as a group of notes that are hit simultaneously, regardless of the staff, so that they sound together at an instant time [33]. Thus, learning the chordwise dependency is analogous to direct modeling of the temporal progression of the piano performance. Let M ∈ R<sup>C×N</sup> be a matrix that aligns serialized notes to their polyphonic structure, where C and N are the number of chords and the number of notes, respectively. Within the encoder, the notewise representation is sequentially average-pooled by M with dynamic kernel sizes where each size represents the number of notes in each chord. We denote this operation as N2C. In this way, we can directly model chord-level dependency of the note-level expressive parameters [32]. In contrast, the decoder extends the chordwise representation from the encoder back to the notewise using the transposed alignment matrix M<sup>T</sup> , of which process we denote as C2N. Along this, the notewise embedding of the score features replenishes the notewise information for the output. Consequently, notes in the same chord share any information of their corresponding chord, while maintaining their differences by the conditional score features: 



<!-- Start of picture text -->
M · e<br>N2C(e) = , C2N(e) = M T · e (1)<br>� Nn=1 Mn,1:C<br><!-- End of picture text -->

where e denotes a notewise or chordwise representation. 

## 2.3 Overall Network Architecture 

Our proposed network is generally based on the conditional VAE framework [34, 35]. Concretely, we use the sequential VAE that is modified for generation of sequential data [11,24,36]. Let x = {xn}<sup>N</sup> n=1<sup>be a sequence of the</sup> 

1 https://github.com/rsy1026/sketching_piano_ expression 

179 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
𝑥 ො𝑥<br>N2C N2C<br>𝑦<br>𝐿fac 𝑧 (pln) 𝐷 (pln) 𝐿pln<br>෠𝑘<br>𝐿reg 𝑧 (str) 𝐷 (str) 𝐿str<br>At Training Only<br>BiRNN (pln)𝑧<br>N2C C2N<br>Notewise Encoder Chordwise Encoder Chordwise Generator Notewise Encoder<br>RNN (str)𝑧<br>Notewise Encoder<br><!-- End of picture text -->

Figure 1: Overall architecture of the proposed system. The orange box includes the auxiliary tasks only for training. 

performance features, and y = {yn}<sup>N</sup> n=1<sup>be a sequence of</sup> the conditional score features. Our network has two chordwise latent variables z<sup>(pln)</sup> = {zc<sup>(pln)</sup> }<sup>C</sup> c=1<sup>∈RC×d(pln)and</sup> z<sup>(str)</sup> = {zc<sup>(str)</sup> }<sup>C</sup> c=1<sup>∈RC×d(str)that represent explicit plan-</sup> ning and structural attribute, where d<sup>(pln)</sup> and d<sup>(str)</sup> are the sizes of z<sup>(pln)</sup> and z<sup>(str)</sup> , respectively. Our network generates notewise performance parameters x from these latent variables and given score features y. The overall architecture of our proposed system is illustrated in Figure 1. 

Generation. A probabilistic generator parameterized by θ produces the note-level performance parameters x from the two latent variables z<sup>(pln)</sup> and z<sup>(str)</sup> with the given condition y. We note that the latent variables are in chordlevel. This decreases a computational cost and also enables intuitive modeling of polyphonic piano performance where each time step represents a stack of notes and the simultaneous notes share common characteristics [8]: 



<!-- Start of picture text -->
pθ(x, y, z (pln) , z (str) ) =pθ(x|z (pln) , z (str) , y)<br>C (2)<br>pθ(z (pln) ) � pθ(zc (str) |z<c (str), y ≤ (chd c ))<br>c=1<br><!-- End of picture text -->

where y<sup>(chd)</sup> = N2C(ey) is the chordwise embedding, and ey is the notewise embedding for y. We assume that the prior of zc<sup>(pln)</sup> is a standard normal distribution. In contrast, zc<sup>(str)</sup> is sampled from a sequential prior [24, 36, 37], conditioned on both previous latent variables and chordwise score features: zc<sup>(str)</sup> ∼N (µ<sup>(prior)</sup> , diag(σ<sup>(prior)2</sup> ), where [µ<sup>(prior)</sup> , σ<sup>(prior)</sup> ] = f<sup>(prior)</sup> (z<c<sup>(str), y</sup> ≤<sup>(chd</sup> c<sup>)),andf (prior)isa</sup> unidirectional recurrent neural network. The latent representations and y<sup>(chd)</sup> pass through the decoder as shown in Figure 1. During training, the model predicts the intermediate chordwise output that is computed as N2C(x). This is to enhance reconstruction power of our system, propagating accurate information of chord-level attributes to the final decoder. The intermediate activation is then extended to the notewise through the C2N operation. The note-level parameters are generated autoregressively based on this activation and the notewise score feature. We use teacher forcing during training [38]. 

Inference. A probabilistic encoder parameterized by ϕ approximates the posterior distibutions of the latent representations z<sup>(pln)</sup> and z<sup>(str)</sup> from the performance input x 

and conditional score input y: 



<!-- Start of picture text -->
qφ(z (pln) , z (str) |x, y) =qφ(z (pln) |x (chd) )<br>C (3)<br>� qφ(zc (str) |x≤ (chd c ), y ≤ (chd c ))<br>c=1<br><!-- End of picture text -->

where x<sup>(chd)</sup> = N2C(ex) is the chordwise embedding, and ex is the notewise embedding for x. The posterior distributions of zc<sup>(pln)</sup> and zc<sup>(str)</sup> are approximated by distribution parameters encoded by f<sup>(pln)</sup> (x<sup>(chd)</sup> ) and f<sup>(str)</sup> (x<sup>(chd)</sup> , y<sup>(chd)</sup> ), where f<sup>(pln)</sup> and f<sup>(str)</sup> are bidirectional and unidirectional recurrent neural networks, respectively. We note that z<sup>(pln)</sup> is independent of the score features y. This allows a flexible transfer of the explicit planning among other musical pieces. On the other hand, z<sup>(str)</sup> is constrained by y since the structural attributes are dependent on the note structure. 

Training. We train the models pθ and qφ by approximating marginal distributions of the performance features x conditioned on the score features y. This requires to maximize negative evidence lower bound (ELBO) that includes regularization force by Kullback±Leibler divergence [34]: 



<!-- Start of picture text -->
LVAE = Eqφ(z(pln),z(str)|x,y) �log pθ(x|z (pln) , z (str) , y)�<br>+ Eqφ(z(pln),z(str)|x,y) �log pθ(k|z (pln) , z (str) , y)�<br>− KL(qφ(z (pln) |x)∥pθ(z (pln) ))<br>C<br>−<br>� KL(qφ(zc (str) |x ( ≤ chd c ), y ≤ (chd c ))∥pθ(z c (str) |z<c (str), y ≤ (chd c )))<br>c=1<br>(4)<br><!-- End of picture text -->

where k = N2C(x) is the chordwise performance features. 

## 2.4 Regularizing the Latent Variables 

We enhance disentanglement of the latent representations z<sup>(pln)</sup> and z<sup>(str)</sup> using four regularization tasks [24]. 

Prediction Tasks. We extract new supervisory signals for additional prediction tasks from the input data [24]. We define a signal of explicit planning I<sup>(pln)</sup> as a set of smoothed contours of the expressive parameters. It is extracted as a polynomial function predicted from the chordwise performance parameters k. We also derive a signal of structural attribute as I<sup>(str)</sup> = sign(k − I<sup>(pln)</sup> ) which represents normalized directions of the performance parameters. We train two discriminators D<sup>(pln)</sup> and D<sup>(str)</sup> that directly receive z<sup>(pln)</sup> and z<sup>(str)</sup> , respectively. D<sup>(pln)</sup> is composed of A sub-discriminators where each discriminator Da<sup>(pln)</sup> predicts a signal Ia<sup>(pln)</sup> for each expressive attribute a from za<sup>(pln)</sup> ∈ R<sup>C×(d(pln)/A)</sup> , where za<sup>(pln)</sup> is a constituent part of z<sup>(pln)</sup> , and A is the number of expressive attributes. This setting is for a clear disentanglement among the expressive attributes. On the other hand, D<sup>(str)</sup> predicts the signal I<sup>(str)</sup> at once for all expressive attributes that belong to the same musical structure. All discriminators are jointly trained with the generative model, and the costs Lpln and Lstr are minimized 

180 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

<mark>1</mark> as Lpln = A �a<sup>MSE(D</sup> a<sup>(pln)</sup> (za<sup>(pln)</sup> ), Ia<sup>(pln)</sup> ) and Lstr = MSE(D<sup>(str)</sup> (z<sup>(str)</sup> ), I<sup>(str)</sup> ), respectively. Factorizing Latent Variables. We further constrain a generator to guarantee that z<sup>(pln)</sup> delivers correct information regardless of z<sup>(str)</sup> [39]. During training, we sample a new output x˜ using z<sup>(pln)</sup> ∼ qφ(z<sup>(pln)</sup> |x) and z˜<sup>(str)</sup> ∼ pθ(z<sup>(str)</sup> ). Then, we re-infer z˜<sup>(pln)</sup> ∼ qφ(˜z<sup>(pln)</sup> |x˜) to estimate the superversory signal I<sup>(pln)</sup> . This prediction loss is backpropagated only through the generator: 



<!-- Start of picture text -->
Lfac = A 1 � MSE(Da (pln) (˜za (pln) ), Ia (pln) ) (5)<br>a<br><!-- End of picture text -->

Aligning Latent Variables with Factors. Finally, we enable the "sliding-fader" control of the expressive attributes [28]. To this end, we employ the regularization loss proposed by Pati et al. [27] that aligns specific dimensions of z<sup>(pln)</sup> with the target expressive attributes. This method assumes that a latent representation can be disentangled through its monotonic relationship with a target attribute. Let di and dj be a target dimension d of ith and jth latent representations, respectively, where d ∈ za<sup>(pln)</sup> , i, j ∈ [1, M ], and M is the size of a mini-batch. A distance matrix Dd is computed between di and dj within a mini-batch, where Dd = di −dj. A similar distance matrix Da is computed for the two target attribute values ai and aj. We minimize a MSE between Dd and Da as follows: 



<!-- Start of picture text -->
Lreg = MSE(tanh(Dd), sign(Da)) (6)<br><!-- End of picture text -->

## 2.5 Overall Objective 

The overall objective of our proposed network aims to generate realistic performance features with properly disentangled representations for the intended factors: 

L = LVAE + λplnLpln + λstrLstr + λfacLfac + λregLreg (7) 

where λpln, λstr, λfac, and λreg are hyperparameters for balancing the importance of the loss terms. 

## 3. EXPERIMENTAL SETUPS 

## 3.1 Dataset and Implementation 

We use Yamaha e-Competition Dataset [8] and Vienna 4x22 Piano Corpus [40]. From these datasets, we collect 356 performances of 34 pieces by Frédéric Chopin, which have been representative research subjects for analyzing the Western musical expression [6, 22, 41, 42]. We use 30 pieces (108,738 batches) for training and the rest for testing. To verify the generality of model performances, we also collect the external dataset from ASAP dataset [43]. We use 116 performances for 23 pieces by 10 composers who represent various eras of Western music. For subjective evaluation, we collect 42 songs of non-Classical songs from online source<sup>2</sup> which are less constrained to written expression than most Classical excerpts. 

We basically follow Jeong et al. [8] to compute the input features from the aligned pairs of performance and score data. We set MIDI velocities and Beat Per Minute (BPM) of all notes in the score data to be 64 and 120, respectively. We also remove any grace notes for simplicity and manually correct any errors. The performance features are further normalized into a range from -1 to 1 for training. We use an ADAM optimizer [44] with an initial learning rate of 1e-5, which is reduced by 5% every epoch during backpropagation. We empirically set λpln, λstr, λfac, and λreg to be 1000, 100, 1, 10, respectively. We set a degree of the polynomial function computing I<sup>(pln)</sup> as 4 through an ablation study described in the supplementary material. 

## 3.2 Comparative Methods 

To the best of our knowledge, there is no existing method that does not intentionally follow the written guidelines in the musical score. Therefore, we use variants of our proposed network as comparing methods that differ in model architecture: Notewise denotes the proposed model without the hierarchical learning. CVAE denotes a variant of Notewise where z<sup>(pln)</sup> is substituted with the supervisory signal I<sup>(pln)</sup> . We also conduct an ablation study that investigates necessity of the four loss terms. 

## 4. EVALUATION 

We evaluate the proposed network in terms of both objective and subjective criteria. 

## 4.1 Generation Quality 

We compute Pearson’s correlation coefficients between the reconstructed or generated samples and human piano performances [6, 9, 11, 19]. We first measure the reconstruction quality of the test samples ("Rrecon"). Then, we evaluate the samples generated from z˜<sup>(str)</sup> ∼ pθ(z<sup>(str)</sup> ) and either of : 1) z<sup>(pln)</sup> ∼ qφ(z<sup>(pln)</sup> |x) ("Rx|pln") and 2) z0<sup>(pln)</sup> ∼ qφ(z0<sup>(pln)</sup> |x0) ("Rx|pln0 "), where x0 is a zero matrix. 

The results are shown in Table 1. Notewise shows the best scores in both datasets, and our method outperforms CVAE in Rrecon. It indicates that our proposed architecture where a latent representation is used instead of a direct condition is generally good at reconstructing the human data. When using the randomly sampled z˜<sup>(str)</sup> , our method and the model without Lreg show stable scores compared to other baseline models. The model without Lreg also shows the highest scores in Rx|pln for both datasets. It indicates that Lreg may contribute the least to generation power among other loss terms. CVAE and the model only with L<sup>(pln)</sup> also show high scores in Rx|pln0 . This may be due to the posterior collapse that makes the decoder depends mostly on the score condition [45], which is demonstrated in the supplementary material. 

## 4.2 Disentangling Latent Representations 

We verify whether the latent representations are welldisentangled by appropriate information [24]. To this 

2 http://www.ambrosepianotabs.com/page/library 

181 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
80 80<br>60 60<br>MIDIVel. MIDIVel.<br>1.0<br>Articul.0.5<br>20 20 20 20 25 25<br>Onset Index (Chordwise) Onset Index (Chordwise) Onset Index (Chordwise)<br>GT Reconstructed Sampled GT Reconstructed Sampled GT Reconstructed Sampled<br>Sketch Controlled 1 Controlled 2 Sketch Controlled 1 Controlled 2 Sketch Controlled 1 Controlled 2<br>(a) (b) (c)<br><!-- End of picture text -->

Figure 2: Qualitative samples for the proposed system. Light-blue, blue and gray lines denote the reconstructed results, sampled results from the inferred z<sup>(pln)</sup> , and their ground truths, respectively; black and orange lines denote the controlled results that are generated from different random z˜<sup>(str)</sup> ; and green lines denote the "sketch" values, or α, that are inserted to z<sup>(pln)</sup> . The samples demonstrate three excerpts that are: (a) Haydn’s Keyboard Sonata, Hob. XVI:39, 3rd movement, mm. 53-56; (b) Schubert’s Impromptu, Op. 90, No. 4, mm. 149-152; and (c) Balakirev’s Islamey, Op. 18, mm. 29-32. 



<!-- Start of picture text -->
60<br>MIDIVel. MIDIVel. 5 50<br>Onset Index (Chordwise) Onset Index (Chordwise) Onset Index (Chordwise)<br>Raw Value Estimated EP Raw Value Estimated EP Raw Value Estimated EP<br>(a) (b) (c)<br><!-- End of picture text -->

Figure 3: Qualitative results for estimating the explicit planning from raw piano performances. Pink and gray lines denote the estimated contours and raw performance parameters, respectively. The results in (a), (b), and (c) are from the same excerpts for (a), (b), and (c) in Figure 2, respectively. 

|Dataset||Internal|||Externa|l|
|---|---|---|---|---|---|---|
|Metric|Rrecon|Rx|pln|Rx|pln0|Rrecon|Rx|pln|Rx|pln0|
|Notewise|0.870|0.392|0.203|0.875|0.479|0.177|
|CVAE|0.730|0.338|0.223|0.741|0.399|0.216|
|Lpln|0.627|0.357|0.229|0.687|0.414|0.220|
|Lpln+Lstr|0.770|0.325|0.181|0.837|0.398|0.195|
|w/oLfac|0.774|0.289|0.176|0.838|0.354|0.173|
|w/oLreg|0.737|0.437|0.224|0.793|0.502|0.216|
|Ours|0.737|0.427|0.231|0.789|0.498|0.203|



|Dataset|Inte|rnal|Exte|rnal|
|---|---|---|---|---|
|Metric|MSEp|MSEs|MSEp|MSEs|
|Notewise|0.003|0.006|0.022|0.028|
|CVAE|0.034|0.045|0.085|0.092|
|Lpln|0.028|0.036|0.074|0.077|
|Lpln+Lstr|0.012|0.015|0.022|0.027|
|w/oLfac|0.018|0.023|0.021|0.025|
|w/oLreg|0.002|0.004|0.014|0.022|
|Ours|0.001|0.002|0.012|0.020|



Table 2: Evaluation results for the disentanglement of the latent representations. 

|Dataset||Internal|||External||
|---|---|---|---|---|---|---|
|Metric|C|R|L|C|R|L|
|Notewise|0.782|0.916|0.632|0.775|0.914|0.656|
|CVAE|0.798|0.812|0.620|0.773|0.802|0.649|
|Lpln|0.693|0.852|0.323|0.694|0.834|0.324|
|Lpln+Lstr|0.633|0.882|0.253|0.639|0.865|0.277|
|w/oLfac|0.831|0.846|0.789|0.832|0.831|0.847|
|w/oLreg|0.804|0.955|0.653|0.808|0.946|0.657|
|Ours|0.942|0.953|0.976|0.944|0.945|0.977|



Table 3: Evaluation results for the controllability of the expressive attributes. C, R, and L denotes consistency, restrictiveness, and linearity, respectively. Each score is the average score for the expressive attributes. 

Table 1: Evaluation results for the generation quality. The higher score is the better. 

end, each model infers the latent representations z<sup>(pln)</sup> and z<sup>(str)</sup> from the test sets. Each model also randomly samples z˜<sup>(str)</sup> and infers z0<sup>(pln)</sup> ∼ qφ(z<sup>(pln)</sup> |x0). We use z0<sup>(pln)</sup> to measure the structural attribute, since z0<sup>(pln)</sup> represents a flat expression where the structural attribute can be solely exposed. Each model generates new outputs as x<sup>(pln)</sup> ∼ pθ(x<sup>(pln)</sup> |z<sup>(pln)</sup> , ˜z<sup>(str)</sup> , y) and x<sup>(str)</sup> ∼ pθ(x<sup>(str)</sup> |z0<sup>(pln)</sup> , z<sup>(str)</sup> , y). Then, we compute a new signal I˜<sup>(pln)</sup> from x<sup>(pln)</sup> using the polynomial regression. The MSE values are calculated as MSEp = MSE(I<sup>˜(pln)</sup> , I<sup>(pln)</sup> ) and MSEs = MSE(x<sup>(str)</sup> , k − I<sup>(pln)</sup> ). 

Table 2 shows that our method achieves the best scores in all metrics for both datasets. This confirms that our proposed system can learn the latent representations that reflect the intended attributes. Notewise and the model without Lreg also show the robust scores compared to other baseline models. It indicates that using the notewise modeling alone is still relevant for achieving appropriate representations. It also implies that Lreg may not contribute to the disentanglement as much as other loss terms. 

## 4.3 Controllability of Expressive Attributes 

We sample a new input x¯ where entries of each feature are constant across time. Then, each model infers 

182 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

|Metric|Winnin|gRate(Human-likeness)|
|---|---|---|
|Group|T|UT<br>Overall|
|Notewise|0.317(±0.223)|0.541(±0.316) 0.493(±0.309)|
|CVAE|0.467(±0.356)|0.477(±0.342) 0.475(±0.338)|
|Ours|0.417(±0.256)|0.555(±0.256) 0.525(±0.258)|



Table 4: Evaluation results for the winning rate in terms of human-likeness. T, UT, and Overall denote musically trained, untrained, and all groups, respectively. 

z¯<sup>(pln)</sup> ∼ qφ(¯z<sup>(pln)</sup> |x¯). We control each attribute by varying dimension values of ¯z<sup>(pln)</sup> following Tan et al. [28] and examine the new samples generated from z¯<sup>(pln)</sup> . We leverage the existing metrics to measure the controllability of each model [28]: Consistency ("C") measures consistency across samples in terms of their controlled attributes; restrictiveness ("R") measures how much the uncontrolled attributes maintain their flatness over time; and linearity ("L") measures how much the controlled attributes are correlated with the corresponding latent dimensions. We average over the three expressive attributes±dynamics, articulation, and tempo±into one score for each metric. 

Table 3 demonstrates that our system shows the best scores in consistency and linearity in both internal and external datasets. This indicates that our proposed method can robustly control the latent representation z<sup>(pln)</sup> in intended way. The model without Lreg outperforms our method in restrictiveness. It indicates that the uncontrolled attributes by this model are the least interfered by the controlled attribute. However, its scores on consistency and linearity are lower than ours. It confirms that Lreg promotes linear control of the target attributes. 

## 4.4 Subjective Evaluation 

We conduct a listening test to compare the proposed model architecture to Notewise and CVAE. We qualitatively evaluate the base quality of the samples that have flat expressions, so that quality judgments are independent of any preference of arbitrary explicit planning. We generate each sample using z0<sup>(pln)</sup> . A listening test is composed of 30 trials where each participant chooses a more "human-like" sample out of the generated sample and its plain MIDI [9]. Both samples have the same length which is a maximum of 15 seconds, rendered with TiMidity++<sup>3</sup> without any pedal effect. Human-likeness denotes how similar the sample is to an actual piano performance that commonly appears in popular music. A total of 28 participants are involved, and 6 participants are professionally trained in music. 

The results are demonstrated in Table 4. We measure a winning rate, a rate of winning over the plain MIDI, and a top-ranking rate, a rate of being the highest rank among the three models in terms of winning rate. These metrics are further explained in the supplementary material. The results show that musically trained ("T") and untrained ("UT") groups show the different tendency of each other: in the trained group, CVAE shows the best winning rate, and our method gets the best top-ranking rate; in the 



<!-- Start of picture text -->
0.6 0.583<br>0.417 0.3640.386 0.411<br>Rate 0.4 0.250 0.3040.286<br>0.2<br>Top-ranking 0.0<br>UT Overall<br>Ours Notewise CVAE<br><!-- End of picture text -->

Figure 4: Evaluation results for the top-ranking rate. T, UT, and Overall denote musically trained, untrained, and all groups, respectively. 

untrained group, our method shows the highest winning rate, whereas Notewise is top-ranked most frequently. We note that our system reveals smaller variances than those of CVAE and Notewise of the musically trained and untrained groups in the winning rate, respectively. Moreover, our system receives the highest overall scores for both metrics. It indicates that our system can be stably perceived more human-like than the plain MIDI compared to other baseline models. 

## 4.5 Qualitative Examples 

Our system can render new piano performances from the scratch given a musical score. It can directly generate expressive parameters from the randomly sampled z˜<sup>(pln)</sup> ∼ pθ(z<sup>(pln)</sup> ) and z˜<sup>(str)</sup> ∼ pθ(z<sup>(str)</sup> ). We note that z˜<sup>(pln)</sup> does not have temporal dependency: each z˜c<sup>(pln)</sup> is sampled independently of z˜c<sup>(pln</sup> −1<sup>).Hence,weneedtoinsertspecific</sup> values {α<sup>(c)</sup> }<sup>C</sup> c=1<sup>,whichwecallas"smoothsketches",</sup> into the target dimensions of z<sup>(pln)</sup> if any temporal dependency of explicit planning is necessary. Figure 2 shows that the controlled parameters are greatly correlated with α, while their local characteristics follow those of the ground truth. In addition, the black and orange lines together demonstrate granular variety in the parameters induced by different z˜<sup>(str)</sup> for the same musical structure. Moreover, Figure 3 shows that our system can estimate explicit planning from arbitrary human performances, indicating that our system can derive relevant information on explicit planning from the unseen data. 

## 5. CONCLUSION 

We propose a system that can render expressive piano performance with flexible control of musical expression. We attempt to achieve representations for the explicit planning and structural attribute through self-supervised learning objectives. We also leverage the two-step modeling of two hierarchical units for an intuitive generation. Experimental results confirm that our system shows stable generation quality, disentangles the target representations, and controls all expressive attributes independently of each other. Future work can be improving our system using a larger dataset for various genres and composers. We can also further compare our system with recent piano-rendering models [8] to investigate any connections between a performer’s explicit planning and a composer’s intent. 

3 https://sourceforge.net/projects/timidity/ 

183 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

## 6. ACKNOWLEDGMENTS 

We deeply appreciate Dasaem Jeong, Taegyun Kwon, and Juhan Nam for giving technical support to initiate this research. We also especially appreciate Hyeong-Seok Choi for providing critical feedback on the model architecture and evaluation. We greatly appreciate You Jin Choi and all of my colleagues who gave great help with respect to the listening test. 

## 7. REFERENCES 

- [1] G. Widmer and W. Goebl, ªComputational models of expressive music performance: The state of the art,º Journal of New Music Research, vol. 33, no. 3, pp. 203±216, 2004. 

- [2] C. E. Cancino-Chacón, M. Grachten, W. Goebl, and G. Widmer, ªComputational models of expressive music performance: A comprehensive and critical review,º Frontiers in Digital Humanities, vol. 5, no. 25, pp. 1±23, 2018. 

- [3] G. Widmer, S. Flossmann, and M. Grachten, ªYQX plays Chopin,º AI Magazine, vol. 30, no. 3, pp. 35±48, 2009. 

- [4] T. H. Kim, S. Fukayama, T. Nishimoto, and S. Sagayama, ªStatistical approach to automatic expressive rendition of polyphonic piano music,º in Guide to Computing for Expressive Music Performance. Springer, 2013, pp. 145±179. 

- [5] C. E. Cancino-Chacón and M. Grachten, ªAn evaluation of score descriptors combined with non-linear models of expressive dynamics in music,º in Proceedings of the International Conference on Discovery Science, 2015. 

- [6] C. E. Cancino-Chacón, T. Gadermaier, G. Widmer, and M. Grachten, ªAn evaluation of linear and non-linear models of expressive dynamics in classical piano and symphonic music,º Machine Learning, vol. 106, no. 6, pp. 887±909, 2017. 

- [7] A. Maezawa, ªDeep piano performance rendering with conditional VAE,º in Late-Breaking Demo, the 19th International Society for Music Information Retrieval Conference, 2018. 

- [8] D. Jeong, T. Kwon, Y. Kim, K. Lee, and J. Nam, ªVirtuosoNet: A hierarchical RNN-based system for modeling expressive piano performance,º in Proceedings of the 20th International Society for Music Information Retrieval, 2019. 

- [9] D. Jeong, T. Kwon, Y. Kim, and J. Nam, ªGraph neural network for music score data and modeling expressive piano performance,º in Proceedings of the 36th International Conference on Machine Learning, 2019. 

- [10] Y. Bengio, A. Courville, and P. Vincent, ªRepresentation learning: A review and new perspectives,º IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 35, no. 8, 2013. 

- [11] A. Maezawa, K. Yamamoto, and T. Fujishima, ªRendering music performance with interpretation variations using conditional variational RNN,º in Proceedings of the 20th International Society for Music Information Retrieval Conference, 2019. 

- [12] H. H. Tan, Y.-J. Luo, and D. Herremans, ªGenerative modeling for controllable audio synthesis of expressive piano performance,º in Proceedings of the 37th International Conference on Machine Learning, 2020. 

- [13] R. Bresin and A. Friberg, ªEmotional coloring of computer-controlled music performances,º Computer Music Journal, vol. 24, no. 4, 2000. 

- [14] S. R. Livingstone, R. Muhlberger, A. R. Brown, and W. F. Thompson, ªChanging musical emotion: A computational rule system for modifying score and performance,º Computer Music Journal, vol. 34, no. 1, 2010. 

- [15] M. Bernays and C. Traube, ªInvestigating pianists’ individuality in the performance of five timbral nuances through patterns of articulation, touch, dynamics, and pedaling,º Frontiers in Psychology, vol. 5, no. 157, pp. 1±19, 2014. 

- [16] S. Oore, I. Simon, S. Dieleman, D. Eck, and K. Simonyan, ªThis time with feeling: Learning expressive musical performance,º Neural Computing and Applications, vol. 32, pp. 955±967, 2020. 

- [17] A. Bhatara, A. K. Tirovolas, L. M. Duan, B. Levy, and D. J. Levitin, ªPerception of emotional expression in musical performance,º Journal of Experimental Psychology: Human Perception and Performance, vol. 37, no. 3, pp. 921±934, 2011. 

- [18] A. Friberg, R. Bresin, and J. Sundberg, ªOverview of the KTH rule system for musical performance,º Advances in Cognitive Psychology, vol. 2, no. 2-3, pp. 145±161, 2006. 

- [19] S. Flossmann, M. Grachten, and G. Widmer, ªExpressive performance rendering with probabilistic models,º in Guide to Computing for Expressive Music Performance. Springer, 2013, pp. 75±98. 

- [20] R. H. Woody, ªThe relationship between explicit planning and expressive performance of dynamic variations in an aural modeling task,º Journal of Research in Music Education, vol. 47, no. 4, pp. 331±342, 1999. 

- [21] A. Lerch, C. Arthur, A. Pati, and S. Gururani, ªMusic performance analysis: A survey,º in Proceedings of the 20st International Society for Music Information Retrieval Conference, 2019. 

184 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

- [22] B. H. Repp, ªA microcosm of musical expression: II. quantitative analysis of pianists’ dynamics in the initial measures of Chopin’s Etude in E major,º The Journal of the Acoustical Society of America, vol. 105, no. 3, pp. 1972±1988, 1999. 

- [23] H. Honing, ªFrom time to time: The representation of timing and tempo,º Computer Music Journal, vol. 25, no. 3, 2001. 

- [24] Y. Zhu, M. R. Min, A. Kadav, and H. P. Graf, ªS3VAE: Self-supervised sequential VAE for representation disentanglement and data generation,º in Proceedings of Computer Vision and Pattern Recognition, 2020. 

- [25] F. Locatello, S. Bauer, M. Lucic, G. Rätsch, S. Gelly, B. Schölkopf, and O. Bachem, ªChallenging common assumptions in the unsupervised learning of disentangled representations,º in Proceedings of the 36th International Conference on Machine Learning, 2019. 

- [26] D. Hendrycks, M. Mazeika, S. Kadavath, and D. Song, ªUsing self-supervised learning can improve model robustness and uncertainty,º in Proceedings of the 33rd Conference on Neural Information Processing Systems, 2019. 

- [27] A. Pati and A. Lerch, ªAttribute-based regularization of latent spaces for variational auto-encoders,º in Neural Computing and Applications, 2020. 

- [28] H. H. Tan and D. Herremans, ªMusic FaderNets: Controllable music generation based on high-level features via low-level feature modeling,º in Proceedings of the 21st International Society for Music Information Retrieval Conference, 2020. 

- [29] D. Jeong, T. Kwon, Y. Kim, and J. Nam, ªScore and performance features for rendering expressive music performances,º in Proceedings of the Music Encoding Conference, 2019. 

- [30] A. Roberts, J. Engel, and D. Eck, ªHierarchical variational autoencoders for music,º in Proceedings of the 31st Conference on Neural Information Processing Systems, 2017. 

- [31] H.-W. Dong, W.-Y. Hsiao, L.-C. Yang, and Y.-H. Yang, ªMuseGAN: Multi-track sequential generative adversarial networks for symbolic music generation and accompaniment,º in Proceedings of the 32nd AAAI Conference on Artificial Intelligence, 2018. 

- [32] S.-L. Wu and Y.-H. Yang, ªMuseMorphose: Full-song and fine-grained music style transfer with just one Transformer VAE,º arXiv preprint arXiv:2105.04090, 2021. 

   - [34] D. P. Kingma and M. Welling, ªAuto-encoding variational bayes,º arXiv preprint arXiv:1312.6114, 2013. 

   - [35] K. Sohn, X. Yan, and H. Lee, ªLearning structured output representation using deep conditional generative models,º in Proceedings of the 28th International Conference on Neural Information Processing Systems, 2015. 

   - [36] Y. Li and S. Mandt, ªDisentangled sequential autoencoder,º in Proceedings of the 35th International Conference on Machine Learning, 2018. 

   - [37] J. Chung, K. Kastner, L. Dinh, K. Goel, A. C. Courville, and Y. Bengio, ªA recurrent latent variable model for sequential data,º in Proceedings of the 28th International Conference on Neural Information Processing Systems, 2015. 

   - [38] R. J. Williams and D. Zipser, ªA learning algorithm for continually running fully recurrent neural networks,º Neural Computation, vol. 1, no. 2, 1989. 

   - [39] Z. Hu, Z. Yang, X. Liang, R. Salakhutdinov, and E. P. Xing, ªToward controlled generation of text,º in Proceedings of the 34th International Conference on Machine Learning, 2017. 

   - [40] W. Goebl, ªMelody lead in piano performance: Expressive device or artifact?º The Journal of the Acoustical Society of America, vol. 110, no. 1, 2001. 

   - [41] M. Grachten and G. Widmer, ªLinear basis models for prediction and analysis of musical expression,º Journal of New Music Research, vol. 41, no. 4, pp. 311±322, 2012. 

   - [42] Z. Shi, ªComputational analysis and modeling of expressive timing in Chopin Mazurkas,º in Proceedings of the 22nd International Society for Music Information Retrieval Conference, 2021. 

   - [43] F. Foscarin, A. McLeod, P. Rigaux, F. Jacquemard, and M. Sakai, ªASAP: A dataset of aligned scores and performances for piano transcription,º in Proceedings of the 21st International Society for Music Information Retrieval Conference, 2020. 

   - [44] D. P. Kingma and J. Ba, ªAdam: A method for stochastic optimization,º arXiv preprint arXiv:1412.6980, 2014. 

   - [45] I. Higgins, L. Matthey, A. Pal, C. Burgess, X. Glorot, M. Botvinick, S. Mohamed, and A. Lerchner, ªβ-VAE: Learning basic visual concepts with a constrained variational framework,º in Proceedings of the 5th International Conference on Learning Representations, 2017. 

- [33] Z. Wang, Y. Zhang, Y. Zhang, J. Jiang, R. Yang, J. Z. (Jake), and G. Xia, ªPianotree VAE: Structured representation learning for polyphonic music,º in Proceedings of the 37th International Conference on Machine Learning, 2020. 

185 

