---
paper_id: "000023"
year: 2022
title: "Download pdf"
source_url: "https://zenodo.org/record/7316630/files/000023.pdf"
---

# LEARNING HIERARCHICAL METRICAL STRUCTURE BEYOND MEASURES 

Junyan Jiang<sup>1,2</sup> Daniel Chin<sup>1,2</sup> Yixiao Zhang<sup>1,3</sup> Gus Xia<sup>1,2</sup> 1 Music X Lab, NYU Shanghai 2 MBZUAI 3 Centre for Digital Music, QMUL 

jj2731@nyu.edu, daniel.chin@nyu.edu, yixiao.zhang@qmul.ac.uk, gxia@nyu.edu 

## ABSTRACT 

Music contains hierarchical structures beyond beats and measures. While hierarchical structure annotations are helpful for music information retrieval and computer musicology, such annotations are scarce in current digital music databases. In this paper, we explore a data-driven approach to automatically extract hierarchical metrical structures from scores. We propose a new model with a Temporal Convolutional Network-Conditional Random Field (TCN-CRF) architecture. Given a symbolic music score, our model takes in an arbitrary number of voices in a beatquantized form, and predicts a 4-level hierarchical metrical structure from downbeat-level to section-level. We also annotate a dataset using RWC-POP MIDI files to facilitate training and evaluation. We show by experiments that the proposed method performs better than the rule-based approach under different orchestration settings. We also perform some simple musicological analysis on the model predictions. All demos, datasets and pre-trained models are publicly available on Github<sup>1</sup> . 

## 1. INTRODUCTION 

Music contains rich structures at different levels, and the structure annotations play an important role in music understanding [1,2] and generation [3,4]. Progress has been made in music structure analysis on certain levels, like beat tracking [5±7], downbeat detection [8±11] and part segmentation [12±15]. These levels of structures are often inter-connected with each other, and can be described in a hierarchical way. For example, a part may contain several sections, each containing several measures. Measures can be further decomposed into beats. 

Several views of hierarchical music structures are formally discussed in the Generative Theory of Tonal Music (GTTM) [16], including the grouping structure, the metrical structure, the time-span tree, and the prolongational tree, each focusing on different music properties (i.e., the grouping structure focuses more on melodic grouping 

1 https://github.com/music-x-lab/Hierarchical-Metrical-Structure 

© J. Jiang, D. Chin, Y. Zhang and G. Xia. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: J. Jiang, D. Chin, Y. Zhang and G. Xia, ªLearning Hierarchical Metrical Structure Beyond Measuresº, in Proc. of the 23rd Int. Society for Music Information Retrieval Conf., Bengaluru, India, 2022. 



Figure 1. The hierarchical metrical structure of the beginning of RWC-POP No. 001. Only the main melody is shown. Despite the pick-up bar, these 4 measures are grouped into 2 hypermeasures of length 2, which are further grouped into 1 hypermeasure of length 4. 

while the metrical structure focuses on rhythmic patterns). Among these structures, we choose the metrical structure as the topic for two reasons: (1) For polyphonic music, the metrical structures of different voices are usually compatible, building up a common song-level metrical structure. This property makes data annotation easier and provides opportunities for self-supervision; (2) Some low-level metrical structures (e.g., beats and downbeats) are already annotated in music scores and most MIDI datasets, which can be a helpful source of supervision. In this paper, we will focus our analysis on pop songs, which often contain a well-defined hierarchy of metrical structures [17]. 

Our main goal is to infer the high-level metrical structures given low-level ones like beats and downbeats. The hierarchy of the metrical structure is created by recursively grouping lower metrical units into upper ones (see Figure 1 for an example). We call the grouping of measures (or other larger metrical units) a hypermeasure, and the number of units that form the group as its hypermeter [18,19]. While some properties of beats and measures can be generalized to upper-level metrical structures, there are still many differences to take into account. Similar to the meter, the hypermeter of each layer tends to stay the same to maintain a regular rhythmic pulse, but it is not uncommon to see hypermeter changes in a piece, as shown in Figure 4. Such changes occur more often than low-level meter changes since listeners are less sensitive to longterm rhythmic regularity. Another major difference is that the decision of upper-level metrical structures requires a longer context in the time domain compared to downbeat or beat tracking. 

To resolve these issues, we design a new model that contains a Temporal Convolutional Network (TCN) frontend for metrical level prediction and a Conditional Random Field (CRF) decoder for joint metrical structure decoding. We design the transition of CRF hidden states to allow hypermeter changes with some penalties. To han- 

201 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

dle polyphony, the model takes an arbitrary number of voices/tracks as input, and predicts a confidence score for each track. The final prediction is a weighted average of the results from all tracks. We annotated 70 songs from the RWC-POP dataset and used them for model training and evaluation. We conduct experiments under different orchestration setups with results shown in section 4.4. 

## 2. RELATED WORK 

## 2.1 Downbeat and Meter Tracking 

Downbeat tracking for raw audio is a well-studied task with many promising results. Krebs et al. [8] use particle filters to find the downbeats, yielding a 2-level metrical structure. Durand et al. [9] use an ensemble of convolutional networks to locate downbeats robustly. Fuentes et al. [10] use skip-chain CRF and deep learning to track downbeats, noting that longer-term musical contexts can better inform downbeat tracking. The reader is referred to Gouyon and Dixon’s review [11] for non-symbolic lowlevel metrical analyzers before 2005. 

Notably, locating the beats and downbeats for symbolic music is not a trivial task. Kostek et al. [20] apply neural networks and rough sets to a polyphonic symbolic piece and classify whether each note is accented or not, yielding a 2-level metrical structure (beat and downbeat). Chuang and Su [21] use various RNNs to classify each timestep in a piano roll into non-beat, beat, or downbeat. 

Another related task is time signature detection. Benoit [22] uses symbolic-level auto-correlation to obtain a 4- level metrical structure, and ultimately extracts the meter. More auto-correlative methods [23,24] share a similar logic, since note onsets usually display periodicity in every measure. More recently, inner metric analysis was also used to infer the time signature by Haas et al. [25]. 

## 2.2 Music Segmentation 

The task of music segmentation is to infer musically meaningful section or part boundaries from the music content. Audio-based music segmentation is usually achieved by detecting similarity or repetition of the audio spectral features. McFee and Ellis [13] evaluate inter-time frame similarity and use spectral clustering to obtain a multi-level segmentation of music. Salamon et al. [14] and McCallum [15] replace traditional features with pre-trained deep embeddings to estimate timbre and harmonic similarity. Tralie and McFee [26] fuse multiple similarity metrics for better prediction results. Ullrich et al. [27] train fully supervised CNN on a segment-annotated dataset to detect segment boundaries. See Dannenberg and Goto’s review [28] and the 2010 SOTA report by Paulus et al. [29] to learn more about audio-based music segmentations. 

Segmentation of symbolic music relies more on domain knowledge of music composition. Van der Werf and Hendriks [30] restate GTTM grouping rules in terms of Optimality Theory (OT) and design a Prolog program to find an optimal parse for short monophonic pieces. Dai et al. [31] 

identify phrases as units of melodic repetition by minimizing the Structural Description Length (SDL) for the entire piece, and then extract a 2-layer hierarchy. 

## 2.3 Hierarchical Structure Analysis 

The Generative Theory of Tonal Music (GTTM) [16] discusses several views of the hierarchical music structures, but GTTM does not describe how to realize an analyzer computationally. Various efforts have been made to mechanize GTTM. For example, Jones et al. [32] use a rulebased expert system to obtain a 6-level metrical structure for monophonic pieces, satisfying all GTTM’s wellformedness rules while following Povel’s grid theory [33]. Rosenthal’s Machine Rhythm [34] ventures into the polyphonic domain and uses rule-based methods to extract a 3- level rhythmic annotation for MIDI input. Temperley and Sleator [35] use a preference-rule approach and dynamic programming to obtain the optimal parse. Hamanaka et al. [36] propose the Automatic Time-span Tree Analyzer (ATTA) for structural analysis of 8-bar monophonic scores. Temperley [37] use Bayesian reasoning to jointly analyze metrical, harmonic, and stream structures. Wojcik and Kostek [18] use rule-based methods to retrieve hypermetric rhythm from only the melody. 

Machine learning models are also used for hierarchical structure analysis. Hamanaka et al. propose DeepGTTM [38, 39] which is a fully automatic analyzer that uses a neural network to predict the applicability of GTTM rules for each note, yielding a 5-level metrical structure for 8-bar monophonic scores. 

There are some issues when applying previous works to large polyphonic MIDI databases. Most systems work only for monophonic music or music with limited polyphony. Also, they often work in a short context, usually up to 8 bars. 

## 3. METHODOLOGY 

## 3.1 Problem Setting 

We first formally define the metrical structure prediction task for this paper. Assume we have a music score with T voices (or tracks, in the sense of MIDI files) m1, ..., mT . We also have a list of pre-annotated downbeats d1, ..., dN for the music. The aim is to assign hierarchical metrical labels li ∈{0, 1, ..., L} to each downbeat di where L is the total number of layers we want to build beyond measures. Each label serves as the level of the metrical boundary at di. li = l means di serves as a metrical boundary of all levels for the first l levels beyond measures. Specially, li = 0 means di serves only as a measure boundary but not any metrical boundary beyond measures. 

If we use GTTM’s metrical structure notation, we can use (li+1) dots to represent a metrical boundary level of li. For the example in figure 1, the first 4 measures (excluding the pickup measure) would have labels l1 = 2, l2 = 0, l3 = 1, l4 = 0. 

We can also introduce the following notations. Hypermeasures: A hypermeasure of level l is an interval 

202 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
Metrical level  0 1 2 3 4 0.35 Confidence<br>prediction 𝐡𝑖𝑡 score 𝛼𝑖(𝑡)<br>Quantized track 𝐦𝑡 𝑑𝑖<br>…<br><!-- End of picture text -->

Figure 2. The architecture of the neural network. 

between two downbeats di and dj where li ≥ l, lj ≥ l and lk < l for all k = i + 1...j − 1. In other words, any lk ≥ l serves as a separator of a level-l hypermeasure. Specially, level-0 hypermeasures are just measures. Hypermeters: A hypermeter is the generalization of meters by counting how many level-(l −1) hypermeasures are in a level-l hypermeasure. Since a binary structure is the most commonly used [19,40], we assume a general hypermeter of 2 in all levels, with a few exceptions that cause binary irregularity. 

## 3.2 Temporal Convolutional Network 

Temporal Convolutional Networks (TCNs) have been proven an effective model for beat, downbeat, and tempo tracking [7,41,42]. We believe it is useful for general metrical structure analysis for its unique property we will mention below. We mainly reference [43] for the design of the TCN, but we made it non-causal similar to [7]. Each TCN block contains 8 sequential layers. The first 4 layers are a dilated convolutional layer with kernel size 3 and 256 channels, a batch normalization layer, a Rectified Linear Unit (ReLU) activation layer, and a dropout layer. The next 4 layers repeat this configuration. There is also a residual component that adds a linear transformation of the input to the block output, allowing shortcut connections. 

Our model uses 6 TCN blocks sequentially. Each block multiplies the dilation by 2, starting from 1 at block 1, resulting in an exponentially growing context range for each layer. This allows the model to capture long-term context and more importantly, integrate prior knowledge about binary metrical structure into the network. The model input contains the piano roll and the onset roll of a track quantized into a 16th note level. Under a 4/4 meter, the dilations of the convolutional layers in each block are therefore 1/4 beat, 1/2 beat, 1 beat, 2 beats, 1 measure and 2 measures, respectively. This encourages the convolutional layers to capture more musically meaningful context for binary metrical structures. 

For each track mt in a song, we first feed them into the TCN blocks to get the features for each time step, and then discard the time steps that do not correspond to any downbeat. We use linear layers to project the features into a metrical level prediction h<sup>(</sup> i<sup>t)</sup> and a confidence score αi<sup>(t).</sup> 



<!-- Start of picture text -->
𝑧𝑖<br>(a)<br>𝑙𝑖<br>𝑧𝑖<br>(b)<br>𝑙𝑖<br>𝑧𝑖<br>(c)<br>𝑙𝑖<br>0000 1000 0100 1100 0010 1010 0110 1110 0001 1001 0101 1101 0011<br>····· · ·· · ··· · ·· · ···· · ·· · ···<br>0000 1000 0100 1100 0010 1010 0001 1001 0101 1101 0011<br>····· · ·· · ··· · ···· · ·· · ···<br>0000 1000 0100 1100 0010 1010 0110 1110 0210 1210 0001 1001 0101 1101 0011<br>····· · ·· · ··· · ·· · ·· · ···· · ·· · ···<br><!-- End of picture text -->

Figure 3. Examples of the CRF hidden variables zi (shown as a L-digit number zi<sup>(1)</sup> ...zi<sup>(L)</sup> ) and the corresponding metrical boundary levels li when L = 4. (a) Binary regularity is satisfied. (b) A level-1 hypermeasure is deleted from (a). (c) A level-1 hypermeasure is inserted into (a). Both (b) and (c) are examples of binary irregularity. 

Each prediction h<sup>(</sup> i<sup>t)</sup> is a vector of size (L+1) for the labels 0...L. The final prediction of li is the weighted average of all predictions h<sup>(</sup> i<sup>t)</sup> on the same time step weighted by their confidence scores: 



<!-- Start of picture text -->
a ( i t) := exp αi (t) � � exp αi (t′) (1)<br>t ′<br>pi := � a ( i t)Softmax(h i (t)) (2)<br>t<br><!-- End of picture text -->

## 3.3 Conditional Random Fields 

Conditional Random Fields (CRFs) have been widely used in downbeat tracking [10, 44] to enforce the regularity of the decoded downbeat patterns. Inspired by this, we also use a structured prediction method for decoding. The major differences are that this model needs to predict a hierarchy of L = 4 layers of metrical structures jointly. 

The state space of hierarchical metrical structure can be complex and ambiguous. To make it simple, we restrict our model to accept a hypermeter of 1, 2 or 3 on any level. In the sense of transformational grammar, a level-l hypermeter of 1 can be constructed by deleting some level-(l − 1) hypermeasures from a deep structure with binary regularity, and a hypermeter of 3 can be constructed by inserting some level-(l − 1) hypermeasures (see figure 3 for an example). A hypermeter of 4 or more is not allowed and needs to be decomposed into multiple metrical levels (e.g., 4 = 2 + 2). 

We design the linear CRF with a joint state space zi = (zi<sup>(1)</sup> , ..., zi<sup>(L)</sup> ) where each zi<sup>(l)</sup> ∈{0, 1, 2} corresponds to the current hypermeasure position at level l, i.e., the number of complete level-(l − 1) hypermeasures in this level-l hypermeasure up to the current time step. It can be seen as a generalization of the beat position in [10]. A state zi<sup>(1...l)</sup> = 0 ∧ zi<sup>(l+1)</sup> = 0 denotes a metrical boundary level li = l. Specially, the highest-level metrical boundary li = L is associated and only associated with the state (0, ..., 0), and the lowest-level metrical boundary li = 0 is associated with any zi where zi<sup>(1)</sup> = 0. See figure 3 for some concrete examples. 

203 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

We manually design the transition potential function to encode the belief of binary regularity on each level. We define the transition potential matrix of a single level as 



<!-- Start of picture text -->
A (l) = exp � −1 wdel (l) � 01 exp � −0 wins (l) � (3)<br> 1 0 0 <br><!-- End of picture text -->

where A<sup>(l)</sup> ij<sup>denotesthepotentialoftransitionfromhy-</sup> permeasure position i to position j on level l. wdel<sup>(l)></sup> 0, wins<sup>(l)>0arehyperparametersthatcontrolsthepenalty</sup> of a level-l hypermeasure deletion and insertion respectively. Intuitively, an alternating state sequence like 0, 1, 0, 1 on a single level satisfies binary regularity and will not be penalized. Binary irregularity by inserting (e.g., 0, 1, 2, 0, 1) or deleting (e.g., 0, 0, 1) states are penalized. 

In a hierarchical metrical transition to a level-l metrical boundary, the hypermeasure positions of level 1...(l + 1) are updated, and the ones above level-(l+1) keep the same. Therefore, the joint transition potential is defined as 



<!-- Start of picture text -->
L Azi(−l)1 z i (l) l ≤ li + 1<br>ϕ(zi−1, zi) = � (4)<br>l=1 �I[zi ( − l) 1 = z i (l)] l > li + 1<br><!-- End of picture text -->

where li denotes the corresponding metrical boundary level of zi, and I[b] is the indicator function that returns 1 if b is true and 0 if b is false. 

The emission potential function is designed as ψ(zi, pi) = pili where pili is the li-th entry of pi. We use Viterbi decoding to decode the optimal hidden states z1..d given the observations p1...N : 



<!-- Start of picture text -->
N<br>ˆz = arg maxz ψ(z1, p1) � ϕ(zi−1, zi)ψ(zi, pi) (5)<br>i=2<br><!-- End of picture text -->

## 4. EXPERIMENTS 

## 4.1 Datasets 

The main dataset we use in model training and evaluation is the RWC-POP dataset. It contains 100 songs with aligned MIDI files. The MIDI files have beat and downbeat annotations that are mostly correct<sup>2</sup> . We manually annotated the 4-layer song-level metrical structure for 70 songs. We use 50 songs for training, 10 for validation, and 10 for testing. We acknowledge the ambiguity in data annotation which potentially causes bias by annotator subjectivity [45], so we publicized the annotation data and methods to facilitate discussion and future research. 

All samples are quantized into 16th-note units. The binary piano roll and onset roll are extracted for each track. During training, a random 512-unit (32 measures) segment is chosen from each song, resulting in a 512 × 256 feature matrix (128 MIDI pitches for piano roll and 128 MIDI pitches for onset roll) for each track. To prevent overfitting, we perform label-preserving data augmentation including random pitch shift augmentation of -12 to +12 semitones and a microtiming shift up to an 8th note on the training 

set. The drum track does not use pitch shift augmentation and does not share the same parameter with pitched instruments for the first convolutional layer. 

## 4.2 Model Training 

For model training, we use a mini-batch of 16. We use the Adam optimizer [46] on the cross-entropy classification loss with a learning rate 0.0001 for 100 epochs. In one epoch, we go through each augmented version of each song for 5 times. For each song, we randomly select 2 tracks and try to predict the song-level metrical structure given the weighted average of their predictions. We also apply dropout with a probability 0.5 after each convolutional layer to further suppress overfitting. 

## 4.3 Baseline Models 

While there are some existing rule-based hierarchical metrical structure analyzers [32,39,47] in previous works, they mostly focus on low-level (e.g., beat & downbeat) boundary features like note transitions, durations and local rhythmic patterns. Those features are not effective enough for metrical structures above the measure level. We here build our baseline model using the methodology from [48]. For each metrical level, we calculate the similarity matrix of piano rolls on different granularity and estimate their novelty score as observations. We use a CRF decoder as mentioned above with a different set of hyper-parameters tuned for the baseline model. 

To assess the necessity of introducing metrical irregularity, We also introduce another hypothetical baseline model called the oracle model. The oracle model is not allowed to predict any hypermeter changes (i.e., it always assumes binary regularity) but it always performs the best possible prediction (i.e., maximal F1 score) for each level. This hypothetical model serves as an upper bound for any model that does not allow binary irregularity. 

## 4.4 Results 

Table 1 shows the performance of each model on the test split of RWC-POP songs. To perform a more systematic evaluation, we also created two difficult versions of each test song: (1) no drums: the drum track(s) are removed from the original song and each model is required to predict the same metrical structure without referring to any drum clues; (2) mel. only: all tracks except the melody track are removed. Each model is required to predict the structure by purely referring to the main melody track. 

From the results, we can see that our proposed model performs better than the rule-based counterpart on all metrical levels. Since most test songs have more than 10 MIDI tracks, they provide sufficient metrical hints to both the proposed model and the rule-based model even if the drum track is removed. When we only have the melody track, both the proposed model and the rule-based model’s performances are not satisfactory even on the first level beyond measure. Still, the data-driven approach shows improved performance compared to the rule-based system. 

2 2 out of 70 songs have minor beat/downbeat annotation issues. 

204 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
Rule<br>Proposed ● 00<br>Rule<br>Proposed ●<br>Rule<br>Proposed :<br><!-- End of picture text -->

Figure 4. A case study with song RWC-POP No. 008 from the test split. The song is multi-track but we only show the main melody here. The metrical structure of the song does not satisfy binary regularity because of the 2-bar extensions in the pre-chorus (marked by a dashed blue box), causing hypermeter changes. The prediction of the proposed method aligns well with the reference. The errors in the rule-based prediction are marked in red (better viewed in color). 

|Model|Level 1|Level 2|Level 3|Level 4|
|---|---|---|---|---|
|Proposed|0.9848<br>±0.0215|0.9559<br>±0.0386|0.8880<br>±0.0889|0.6849<br>±0.1900|
|Proposed|0.9338|0.8528|0.7971|0.6646|
|w/o CRF|±0.0390|±0.0937|±0.1276|±0.0844|
|Rule|0.9228|0.8425|0.7485|0.5185|
||±0.0698|±0.1195|±0.1536|±0.2656|
|Oracle|0.9427|0.7782|0.5188|0.4225|
||±0.1120|±0.2076|±0.1751|±0.1234|
|Proposed<br>|0.9868<br>|0.9519<br>|0.8803<br>|0.6611<br>|
|(no drums)|±0.0174|±0.0346|±0.1023|±0.2170|
|Rule|0.9312|0.8107|0.7055|0.4823|
|(no drums)|±0.0660|±0.1568|±0.2008|±0.2239|
|Proposed|0.7413|0.6253|0.5551|0.3808|
|(mel. only)|±0.2139|±0.2448|±0.2536|±0.2399|
|Rule|0.6606|0.4395|0.3142|0.1863|
|(mel. only)|±0.1451|±0.1522|±0.1211|±0.1310|



Table 1. Evaluated F1 scores on the test split of the RWCPOP dataset. 

We observe that the proposed model is better at capturing irregular metrical structures than the rule-based approach. Figure 4 shows a cherry-picked example where binary irregularity can be found. Both the proposed model and the rule-based baseline can detect such irregularity but only the proposed model correctly tells the exact position of the hypermetrical change. 

There is also a tendency for the performance to drop rapidly from lower to higher levels. We believe there are 2 main reasons. First, the higher levels have fewer positive samples, making it hard for the model to learn its semantic characteristics. Second, metrical structures on higher levels are often more ambiguous than lower ones even for human listeners. Sometimes, the highest level (level 4) needs to decide how to group parts together (e.g., verse 

+ pre-chorus or pre-chorus + chorus). Different decisions are sometimes all acceptable. 

## 4.4.1 Out of Distribution Evaluation 

We also want to know whether the proposed model can be applied to MIDI files with very different orchestration setups. Such experiments are hard to perform because of the lack of ground truth annotations. We here perform a small-scale experiment on the POP909 [49] dataset. We select the first 5 songs in the dataset ordered by index and manually annotate the metrical structure<sup>3</sup> . POP909 is a dataset of Chinese pop songs rearranged for piano performance. Each song only has 3 tracks, i.e., a vocal track and two piano tracks, making it harder compared to RWC-POP. The results are shown in table 2. 

From the results, we can see the performance degrades even when all 3 tracks are present. By case inspection, we find that the proposed model has generally satisfactory performance on 3 out of 5 songs on lower layers. However, there is one complex song<sup>4</sup> with multiple metrical and hypermeter changes that make all the approaches fail. Also, due to the lack of rhythmic clues (e.g., drums), a deeper understanding of the syntax and semantics of melody and chords might be required to perform musically meaningful segmentation, which we assume our model can hardly acquire on a small training set of 50 pop songs. 

## 4.5 Confidence Score Analysis 

To perform a statistical analysis of the model behavior and provide a musicological view of the model prediction, we perform model inferences on a large selection of the Lakh MIDI dataset [50]. To ensure enough accuracy of model prediction, we only select a part of the Lakh MIDI dataset 

> 3 We are aware that POP909’s downbeat annotations are sometimes inaccurate and we manually fixed them. 

> 4 POP909 No. 005: I Believe by Van Fan. 

205 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

|Model|Level 1|Level 2|Level 3|Level 4|
|---|---|---|---|---|
|Pd|0.9084|0.8742|0.6470|0.4930|
|ropose|±0.0896|±0.1101|±0.2174|±0.3132|
|Rl|0.6818|0.6625|0.5163|0.3446|
|ue|±0.1855|±0.1550|±0.1195|±0.1856|
|Ol|0.8527|0.7348|0.5883|0.5767|
|race|±0.1735|±0.2763|±0.2493|±0.2474|
|Proposed|0.6742|0.6542|0.5685|0.4797|
|(mel. only)|±0.2962|±0.2737|±0.2403|±0.2053|
|Rule|0.6062|0.3933|0.2642|0.1551|
|(mel. only)|±0.1034|±0.0275|±0.0546|±0.0305|



Table 2. Evaluated F1 scores on the first 5 songs in the POP909 dataset. Mel. only denotes that the melody track is used. Otherwise, all 3 tracks (melody, bridge and piano) are used. 

that has a similar orchestration compared to RWC-POP. We filter the MIDI files according to the following criteria: (1) it contains at least 6 MIDI tracks, including 1 drum track and 1 track whose name contains strings "melody" or "vocal"; (2) if multiple MIDI files’ identified audio sources are the same, at most one MIDI file is kept. A filtered dataset of 3,739 MIDI files is collected. 

We here evaluate the relevance of instruments and the model’s predicted confidence score. Notice that the instrument program number is not a part of the model input, so the only difference comes from the rhythmic properties of their scores. We collect the unnormalized confidence scores α<sup>(t)</sup> for each track mt of different instruments, and calculate their means and standard derivations. Specially, we regard all melody tracks (identified by their names) as a new instrument and ignore its original MIDI program number. Also, we remove all tracks with too many measurelevel rests (more than 1/3 of the whole song) since they trivially result in low confidence scores. 

Table 3 shows the results of confidence score analysis. We can see that drums are the strongest clue for metrical structures. The melody track and many melodic instruments (e.g., guitars) also serve as useful clues. On the other hand, instruments that produce slow accompaniments (e.g., string ensemble and pads) are less preferred. 

## 4.5.1 Drum Track Analysis 

As another experiment of musicological analysis, we perform an experiment on the relation between drum notes and the metrical structure level. For simplicity, we only collect samples that a certain drum event happens exactly on the downbeat, and we collect the corresponding metrical boundary level of that downbeat. The results are shown in Table 4. While the occurrence of many drum events does not significantly change the distribution of the metrical boundary level, the crash cymbal and splash cymbal are certainly useful clues to a high-level metrical boundary. This aligns with people’s perception of them since these cymbals are usually associated with a strong burst of energy, serving as an important rhythmic hint. 

|Track/Instrument|Confidence|
|---|---|
|Melody|1.78±1.22|
|Drum|3.61±2.58|
|Acoustic Grand Piano|0.35±1.69|
|Electric Guitar (jazz)|0.75±1.55|
|Acoustic Bass|0.33±1.66|
|String Ensemble|0.11±1.70|
|Pad (warm)|-0.86±1.78|



Table 3. A selected view of the means and standard derivations of the confidence score for different tracks/instruments. The melody track is identified by its name instead of the MIDI instrument. The drum track is identified by its MIDI channel number (No. 10). 

|Drums (%)|L-0|L-1|L-2|L-3|L-4|
|---|---|---|---|---|---|
|Any|50.00|24.71|12.06|6.21|7.02|
|Bass Drum|48.66|25.10|12.46|6.47|7.30|
|Acoustic Snare|52.27|23.28|11.19|6.27|7.00|
|Closed Hi Hat|51.32|25.14|11.91|5.54|6.11|
|Open Hi Hat|51.90|25.07|11.33|5.38|6.32|
|Crash Cymbal|20.97|19.13|18.58|18.94|22.38|
|Ride Cymbal|51.41|25.03|11.57|5.61|6.39|
|Splash Cymbal|34.80|22.30|16.00|12.90|14.01|



Table 4. A selected view of the frequency of different drum instruments (on a downbeat) associated with different levels of metrical boundaries. L-n means level-n metrical boundary. 

## 5. CONCLUSION AND FUTURE WORK 

In this paper, we propose a data-driven approach for hierarchical metrical structure analysis of symbolic music. Our model adopts a TCN-CRF architecture and accepts an arbitrary number of voices as input. Experiments on MIDI datasets show that our model performs better than rule-based methods under different orchestration settings. 

The model performance is still not satisfactory, especially for high-level metrical structures and music with very different orchestration. We assume the performance would be better if more data were annotated, but there are also other possible directions for data-driven methods. First, self-supervised or semi-supervised methods might be a helpful complement to the lack of labeled datasets. For example, a consistency loss can be used to evaluate the prediction between different voices in the same music piece. Different data augmentation strategies might also be helpful. Second, it might be useful to utilize datasets of related tasks (e.g., section labels) as a source of weak supervision. Related tasks can also be used for multi-task learning. 

Other potential future works include improving the automatic analysis system of other hierarchical structures, e.g., the grouping structures. The application of hierarchical structure analysis in the audio domain is also worth exploring. 

206 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

## 6. REFERENCES 

- [1] N. C. Maddage, C. Xu, M. S. Kankanhalli, and X. Shao, ªContent-based music structure analysis with applications to music semantics understanding,º in Proceedings of the 12th annual ACM international conference on Multimedia, 2004, pp. 112±119. 

- [2] D. P. Ellis and G. E. Poliner, ªIdentifying ‘cover songs’ with chroma features and dynamic programming beat tracking,º in 2007 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), vol. 4, 2007, pp. IV±1429±IV±1432. 

- [3] S. Dieleman, A. van den Oord, and K. Simonyan, ªThe challenge of realistic music generation: modelling raw audio at scale,º Advances in Neural Information Processing Systems, vol. 31, 2018. 

- [4] S. Lattner, M. Grachten, and G. Widmer, ªImposing higher-level structure in polyphonic music generation using convolutional restricted boltzmann machines and constraints,º Journal of Creative Music Systems, vol. 2, pp. 1±31, 2018. 

- [5] D. P. Ellis, ªBeat tracking by dynamic programming,º Journal of New Music Research, vol. 36, no. 1, pp. 51± 60, 2007. 

- [6] S. Dixon, ªEvaluation of the audio beat tracking system beatroot,º Journal of New Music Research, vol. 36, no. 1, pp. 39±50, 2007. 

- [7] E. MatthewDavies and S. Böck, ªTemporal convolutional networks for musical audio beat tracking,º in 2019 27th European Signal Processing Conference (EUSIPCO). IEEE, 2019, pp. 1±5. 

- [8] F. Krebs, A. Holzapfel, A. T. Cemgil, and G. Widmer, ªInferring metrical structure in music using particle filters,º IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 23, no. 5, pp. 817±827, 2015. 

- [9] S. Durand, J. P. Bello, B. David, and G. Richard, ªRobust downbeat tracking using an ensemble of convolutional networks,º IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 25, no. 1, pp. 76±89, 2016. 

- [10] M. Fuentes, B. McFee, H. C. Crayencour, S. Essid, and J. P. Bello, ªA music structure informed downbeat tracking system using skip-chain conditional random fields and deep learning,º in 2019 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2019, pp. 481±485. 

- [11] F. Gouyon and S. Dixon, ªA review of automatic rhythm description systems,º Computer music journal, vol. 29, no. 1, pp. 34±54, 2005. 

- [12] T. Grill and J. Schlüter, ªMusic boundary detection using neural networks on combined features and twolevel annotations.º in Proceedings of the 16th International Society for Music Information Retrieval Conference (ISMIR), 2015, pp. 531±537. 

- [13] B. McFee and D. Ellis, ªAnalyzing song structure with spectral clustering.º in Proceedings of the 15th International Society for Music Information Retrieval Conference (ISMIR). Citeseer, 2014, pp. 405±410. 

- [14] J. Salamon, O. Nieto, and N. J. Bryan, ªDeep embeddings and section fusion improve music segmentation,º in Proceedings of the 22th International Society for Music Information Retrieval Conference (ISMIR), 2021. 

- [15] M. C. McCallum, ªUnsupervised learning of deep features for music segmentation,º in 2019 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2019, pp. 346±350. 

- [16] F. Lerdahl and R. S. Jackendoff, A Generative Theory of Tonal Music, reissue, with a new preface. MIT press, 1996. 

- [17] J. M. Robins, ªPhrase structure, hypermeter, and closure in popular music,º Ph.D. dissertation, The Florida State University, 2017. 

- [18] J. Wojcik and B. Kostek, ªRepresentations of music in ranking rhythmic hypotheses,º in Advances in Music Information Retrieval. Springer, 2010, pp. 39±64. 

- [19] D. Temperley, ªHypermetrical transitions,º Music Theory Spectrum, vol. 30, no. 2, pp. 305±325, 2008. 

- [20] B. Kostek, J. Wojcik, and P. Szczuko, ªSearching for metric structure of musical files,º in International Conference on Rough Sets and Intelligent Systems Paradigms. Springer, 2007, pp. 774±783. 

- [21] Y.-C. Chuang and L. Su, ªBeat and downbeat tracking of symbolic music data using deep recurrent neural networks,º in 2020 Asia-Pacific Signal and Information Processing Association Annual Summit and Conference (APSIPA ASC). IEEE, 2020, pp. 346±352. 

- [22] B. Meudic, ªAutomatic meter extraction from MIDI files,º in Journées d’Informatique Musicale, Marseille, France, Jun. 2002, pp. 1±1. 

- [23] J. C. Brown, ªDetermination of the meter of musical scores by autocorrelation,º The Journal of the Acoustical Society of America, vol. 94, no. 4, pp. 1953±1957, 1993. 

- [24] D. Eck and N. Casagrande, ªFinding meter in music using an autocorrelation phase matrix and shannon entropy.º in Proceedings of the 6th International Conference on Music Information Retrieval (ISMIR), 2005, pp. 504±509. 

207 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

- [25] W. B. De Haas and A. Volk, ªMeter detection in symbolic music using inner metric analysis,º in Proceedings of the 17th International Society for Music Information Retrieval Conference (ISMIR), 2016, p. 441. 

- [26] C. J. Tralie and B. McFee, ªEnhanced hierarchical music structure annotations via feature level similarity fusion,º in 2019 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2019, pp. 201±205. 

- [27] K. Ullrich, J. Schlüter, and T. Grill, ªBoundary detection in music structure analysis using convolutional neural networks.º in Proceedings of the 15th International Society for Music Information Retrieval Conference (ISMIR), 2014, pp. 417±422. 

- [28] R. B. Dannenberg and M. Goto, ªMusic structure analysis from acoustic signals,º in Handbook of signal processing in acoustics. Springer, 2008, pp. 305±331. 

- [29] J. Paulus, M. Müller, and A. Klapuri, ªState of the art report: Audio-based music structure analysis.º in Proceedings of the 11st International Society for Music Information Retrieval Conference (ISMIR). Utrecht, 2010, pp. 625±636. 

- [30] S. Werf and P. Hendriks, ªA constraint-based approach to grouping in language and music,º in Proceedings of the Conference on Interdisciplinary Musicology. Department of Musicology, University of Graz, 2004. 

- [31] S. Dai, H. Zhang, and R. B. Dannenberg, ªAutomatic analysis and influence of hierarchical structure on melody, rhythm and harmony in popular music,º arXiv preprint arXiv:2010.07518, 2020. 

- [32] J. A. Jones, B. O. Miller, and D. L. Scarborough, ªA rule-based expert system for music perception,º Behavior Research Methods, Instruments, & Computers, vol. 20, no. 2, pp. 255±262, 1988. 

- [33] D.-J. Povel, ªA theoretical framework for rhythm perception,º Psychological research, vol. 45, no. 4, pp. 315±337, 1984. 

- [34] D. F. Rosenthal, ªMachine rhythm±computer emulation of human rhythm perception,º Ph.D. dissertation, Massachusetts Institute of Technology, 1992. 

- [35] D. Temperley and D. Sleator, ªModeling meter and harmony: A preference-rule approach,º Computer Music Journal, vol. 23, no. 1, pp. 10±27, 1999. 

- [36] M. Hamanaka, K. Hirata, and S. Tojo, ªImplementing ªa generative theory of tonal music,º Journal of New Music Research, vol. 35, no. 4, pp. 249±277, 2006. 

- [37] D. Temperley, ªA unified probabilistic model for polyphonic music analysis,º Journal of New Music Research, vol. 38, no. 1, pp. 3±18, 2009. 

- [38] M. Hamanaka, K. Hirata, and S. Tojo, ªdeepgttm-i&ii: Local boundary and metrical structure analyzer based on deep learning technique,º in International Symposium on Computer Music Multidisciplinary Research. Springer, 2016, pp. 3±21. 

- [39] ÐÐ, ªdeepgttm-iii: simultaneous learning of grouping and metrical structures,º in the 13th International Symposium on Computer Music Multidisciplinary Research (CMMR2017), 2017, pp. 161±172. 

- [40] M. Rohrmeier, ªTowards a formalization of musical rhythm,º in Proceedings of the 19th International Society for Music Information Retrieval Conference (ISMIR), 2020, pp. 621±629. 

- [41] S. Böck, M. E. Davies, and P. Knees, ªMulti-task learning of tempo and beat: Learning one to improve the other.º in Proceedings of the 20th International Society for Music Information Retrieval Conference (ISMIR), 2019, pp. 486±493. 

- [42] S. Böck and M. E. Davies, ªDeconstruct, analyse, reconstruct: How to improve tempo, beat, and downbeat estimation,º in Proceedings of the 21st International Society for Music Information Retrieval Conference (ISMIR), 2020, pp. 12±16. 

- [43] S. Bai, J. Z. Kolter, and V. Koltun, ªAn empirical evaluation of generic convolutional and recurrent networks for sequence modeling,º arXiv preprint arXiv:1803.01271, 2018. 

- [44] S. Durand and S. Essid, ªDownbeat detection with conditional random fields and deep learned features.º in Proceedings of the 17th International Society for Music Information Retrieval Conference (ISMIR), 2016, pp. 386±392. 

- [45] H. V. Koops, W. B. de Haas, J. Bransen, and A. Volk, ªChord label personalization through deep learning of integrated harmonic interval-based representations,º arXiv preprint arXiv:1706.09552, 2017. 

- [46] D. P. Kingma and J. Ba, ªAdam: A method for stochastic optimization,º arXiv preprint arXiv:1412.6980, 2014. 

- [47] S. Tojo, K. Hirata, and M. Hamanaka, ªComputational reconstruction of cognitive music theory,º New Generation Computing, vol. 31, no. 2, pp. 89±113, 2013. 

- [48] J. Serrà, M. Müller, P. Grosche, and J. L. Arcos, ªUnsupervised detection of music boundaries by time series structure features,º in AAAI, 2012. 

- [49] Z. Wang, K. Chen, J. Jiang, Y. Zhang, M. Xu, S. Dai, and G. Xia, ªPOP909: A pop-song dataset for music arrangement generation,º in Proceedings of the 21st International Society for Music Information Retrieval Conference (ISMIR). Montreal, Canada: ISMIR, Oct. 2020, pp. 38±45. 

208 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

- [50] C. Raffel, ªLearning-based methods for comparing sequences, with applications to audio-to-midi alignment and matching,º Ph.D. dissertation, 2016. 

209 

