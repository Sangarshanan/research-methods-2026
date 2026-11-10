---
paper_id: "000059"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706498/files/000059.pdf"
---

# REFINING MUSIC SAMPLE IDENTIFICATION WITH A SELF-SUPERVISED GRAPH NEURAL NETWORK 

Aditya Bhattacharjee<sup>1</sup> Ivan Meresman Higgs<sup>1</sup> Mark Sandler<sup>1</sup> Emmanouil Benetos<sup>1</sup> 

1 Queen Mary University of London, UK 

```
{a.bhattacharjee,i.meresman-higgs,mark.sandler,emmanouil.benetos}@qmul.ac.uk
```

## ABSTRACT 

Automatic sample identification (ASID) - the detection and identification of portions of audio recordings that have been reused in new musical works - is an essential but challenging task in the field of audio query-based retrieval. While a related task, audio fingerprinting, has made significant progress in accurately retrieving musical content under “real world” (noisy, reverberant) conditions, ASID systems struggle to identify samples that have undergone musical modifications. Thus, a system robust to common music production transformations such as time-stretching, pitch-shifting, effects processing, and underlying or overlaying music is an important open challenge. In this work, we propose a lightweight and scalable encoding architecture employing a Graph Neural Network within a contrastive learning framework. Our model uses only 9% of the trainable parameters compared to the current state-of-the-art system while achieving comparable performance, reaching a mean average precision (mAP) of 44.2%. 

To enhance retrieval quality, we introduce a two-stage approach consisting of an initial coarse similarity search for candidate selection, followed by a cross-attention classifier that rejects irrelevant matches and refines the ranking of retrieved candidates - an essential capability absent in prior models. In addition, as queries in real-world applications are often short in duration, we benchmark our system for short queries using new fine-grained annotations for the Sample100 dataset, which we publish as part of this work. 

## 1. INTRODUCTION 

Sampling is a musical technique that “incorporates portions of existing sound recordings into a newly collaged composition” [1]. The samples often undergo significant modification during this creative process: they may be pitch-shifted, time-stretched and heavily processed with audio effects (henceforth sampling transformations), and are typically combined with other musical elements, creating “musical interference” which makes identification difficult even for human experts. The relevance of this practice is highlighted 

> © A. Bhattacharjee, I. Meresman Higgs, M. Sandler, and E. Benetos. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: A. Bhattacharjee, I. Meresman Higgs, M. Sandler, and E. Benetos, “Refining music sample identification with a self-supervised graph neural network”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

as, since the mass popularisation of hip hop, disco and electronic dance music, this kind of “transformative appropriation” has become one of the most important techniques for composers and songwriters [2]. 

Automatic sample identification (ASID) is a crucial task in music retrieval: given an audio query - either a small segment or an entire music track - the goal is to retrieve the sample source from a database of music recordings, even if sampling transformations have been applied. The potential to substantially impact domains such as attribution and copyright highlights the relevance of this task for music creators and rights holders, as well as music information retrieval (MIR) researchers. 

This task is particularly challenging as sampling transformations can drastically alter the audio features while maintaining perceptual similarity. A reasonable approach is to take cues from deep learning-based audio fingerprinting research, learning metrics that allow for a similarity-based search and retrieval system. Additionally, augmentations in the training pipeline allow models to learn invariance to sampling transformations employed in music production. Recent audio fingerprinting research has successfully employed Graph Neural Networks (GNNs), achieving stateof-the-art results while using compact architectures that facilitate efficient training, which informs this work. 

Progress in ASID has been hindered by the limited availability of well-annotated datasets that reflect real-world sampling practices. The Sample100 dataset [3] is the only publicly available dataset of annotations specifically addressing the presence of samples in commercially produced songs. In this paper we present a revised version of this dataset, annotated by experts to include more fine-grained temporal annotations of the samples, as well as additional comments, time-stretching estimates and instrumentation information. We use these new annotations to report segmentwise hit-rates and to analyse the performance of our system in relation to the type of sample and augmentations performed during the artistic process. 

Our key contributions are as follows: 

- We propose the adaptation of a lightweight Graph Neural Network as the neural encoder for ASID. 

- We introduce a binary cross-attention classifier to facilitate an accurate ranking and refining of retrieved audio fingerprints. 

- We contribute new fine-grained temporal annotations to the Sample100 dataset, and evaluate our model’s 

511 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

performance on short-query retrieval, demonstrating superior top-N hit-rates compared to the baseline. 

- We present a detailed analysis of retrieval performances on different types of samples and discuss the viability of the proposed framework. 

Our code as well as the newly extended Sample100 dataset have been made available for reproducibility<sup>1</sup> . 

re-mixing source separated stems as proposed in [7]. For evaluation, our retrieval methodology employs a two-stage process: initial candidate selection via approximate nearestneighbour search, followed by fine-grained ranking with the cross-attention classifier. Figure 1 illustrates the complete retrieval pipeline, detailing how reference matches are retrieved and ranked for a given query. 

## 3.1 Input Features 

## 2. RELATED WORKS 

Despite the ASID task being a relevant and challenging one for the MIR community, there have been few attempts to tackle it. Foundational work by Van Balen et al. [3], introduced the Sample100 dataset and proposed the adaptation of a spectral peak-based audio fingerprinting framework to make it robust to pitch-shifting. Gururani et al. [4] proposed a system inspired by music cover identification, using Non-negative Matrix Factorization to create templates of the samples and Dynamic Time Warping to achieve a detection algorithm that could be robust to time-shifting. Both of these works focus primarily on robustness against individual sampling transformations but neither address the broader range typically encountered in real-world scenarios. Other traditional fingerprinting methods that were effective for audio retrieval tasks, such as audfprint [5] and Panako [6] have also been tested on this task [7] and proved insufficient for ASID, struggling with the challenges of combined sampling transformations and interfering “musical noise” (the overlying musical composition). 

More recently, the first deep learning-based approach by Cheston et al. [7] achieved state-of-the-art performance on the Sample100 dataset using a CNN architecture (ResNet50IBN) previously used for cover song identification [8] and exploiting music source separation to create synthetic training data. This approach serves as our baseline and demonstrates both the feasibility and remaining challenges of applying deep learning to ASID. 

Current state-of-the-art audio retrieval systems predominantly use CNNs [8–10] or transformers [11] trained with contrastive learning objectives. While effective, these architectures typically require significant computational resources and large training batches, limiting their practical viability. These limitations can be addressed by more parameter-efficient approaches based on Graph Neural Networks (GNNs), which excel at capturing complex structural patterns in non-Euclidean spaces [12]. GNNs have proven effective for audio tasks where temporal and spectral relationships are important, including audio fingerprinting [13] and audio tagging [14], by effectively modelling local and global interactions between time-frequency regions. 

## 3. METHODOLOGY 

ASID involves two categories of audio recordings: a reference, an original music recording, and a query, a new recording that incorporates (i.e., samples) parts of the reference. For training, we generate query-reference pairs by 

Our system employs log-scaled Mel-spectrograms as input features. Given an audio waveform y ∈ R<sup>t</sup> , sampled at 16 kHz, we first compute its Mel-spectrogram representation X ∈ R<sup>F ×T</sup> . Here, F denotes the number of Mel-frequency bins, and T is the number of temporal frames. 

During training, we randomly sample short audio segments of fixed duration tseg from each recording in the training dataset and use it to generate proxy query-reference pairs (see Section 3.4.1). For retrieval, we use real query and reference audio recordings which are segmented into overlapping segments of length tseg. Section 5 details the configuration of the input features and hyperparameters. 

## 3.2 Encoder Architecture 

Our GNN encoder builds upon the architecture introduced in [13]. Given an input Mel-spectrogram X , we first represent it as a set of three-dimensional time-frequency points, each described by its time index, frequency bin index, and amplitude value. From this initial representation, we produce overlapping patch embeddings by aggregating local neighbourhoods of time-frequency points into latent vectors. Formally, each resulting patch embedding is represented by: 



<!-- Start of picture text -->
f : R 3×p → R d , (1)<br><!-- End of picture text -->

where p denotes the number of neighbouring points aggregated per patch, and d is the dimensionality of the latent embedding. These patch embeddings serve directly as nodes in the subsequent graph structure. 

Next, we construct a k-nearest neighbours (kNN) graph from these node embeddings. Specifically, for each node embedding xi, we identify its k nearest neighbours based on cosine similarity in the latent embedding space. The resulting edges represent latent structural relationships among Mel-spectrogram patches. 

Node embeddings are then iteratively refined via graph convolution (GraphConv) layers. For each node embedding xi, we aggregate information from its neighbours xj, where j ∈N (xi). Formally, the update rule is given by: 



<!-- Start of picture text -->
yi = xi + σ�AGG({xj : j ∈N (xi)})�, (2)<br><!-- End of picture text -->

where yi is the updated embedding, σ denotes a nonlinear activation function, N (xi) is the set of neighbours of node xi, and AGG represents an aggregation operation summarizing relevant information from neighbouring nodes. Through iterative aggregation, each node embedding progressively encodes increasingly rich contextual and structural information. The GNN encoder comprises multiple blocks of GraphConv layers, each followed by feedforward 

1 https://github.com/chymaera96/NeuralSampleID 

512 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
Query A Reference embeddings B<br>Query embeddings P1P2<br>SpectrogramM el Segments P3P4P5<br>GNN GNN<br>encoder encoder<br>Refine Correct match<br> +<br>Segmented refs rank<br>Database<br>Final<br>of reference dn ranked<br>songs NMr N output<br>List of candidates dn<br>f c p<br>Correct match NMq<br>dn<br>N<br>L2 projection layer MHCA Classifier<br>MHCA + mean Context vector<br><!-- End of picture text -->

Figure 1. Illustrated ASID methodology: (A) Given a query, we compute segment-level embeddings (fingerprints), matched to reference embeddings via approximate nearest-neighbour (ANN) search; based on which, candidate songs are retrieved from the reference database through a lookup process (dotted arrows). (B) A multi-head cross-attention (MHCA) classifier refines and ranks candidates using node embedding matrices NMq (query) and NMr (references). 

network (FFN) layers. At the beginning of each block, the kNN graph is dynamically reconstructed to reflect the updated node embeddings. 

The output of the GNN encoder is a set of refined node embeddings, collectively referred to as the node embedding matrix, which serve as input features to the crossattention classifier. Finally, these node embeddings are average-pooled and projected into audio fingerprints. Both latent embeddings are used in the subsequent retrieval refinement stage. 

For a comprehensive discussion of architectural details and design considerations, we refer readers to [13]. 

## 3.3 Cross-Attention Classifier 

To capture the latent relationships between these two sets of node embeddings, we introduce a multi-head crossattention classifier. Given a query and a reference audio segment, we first compute the node embedding matrices q ∈ R<sup>N×dn</sup> and r ∈ R<sup>N×dn</sup> , respectively. Here, N is the number of nodes, and dn is the dimensionality of each node embedding. We compute attention-weighted embeddings as follows: 



<!-- Start of picture text -->
C = MHA(q, r, r) (3)<br><!-- End of picture text -->

where MHA(.) denotes standard multi-head attention [15]. The resulting embedding matrix C ∈ R<sup>N×dn</sup> is an attention-weighted transformation of r, where attention is computed between corresponding node embeddings in q and r. C is then aggregated by mean pooling, producing a single context vector c ∈ R<sup>dn</sup> : 



<!-- Start of picture text -->
N<br>c = N 1 � Cj (4)<br>j=1<br><!-- End of picture text -->

where Cj is context vector of the j-th node embedding. Finally, the context vector c is transformed by a shallow nonlinear classifier into a scalar confidence score s: 



<!-- Start of picture text -->
s = σ(w T c + b) (5)<br><!-- End of picture text -->

where w ∈ R<sup>dn</sup> , b ∈ R are learnable parameters, and σ denotes the sigmoid activation function. The scalar s indicates the confidence that the query and reference segments match. As shown in Figure 1, at retrieval time, this is used as a ranking mechanism as well as a measure for rejecting low-confidence candidates. 

## 3.4 Training Pipeline 

Our proposed approach involves two distinct training stages: a self-supervised contrastive learning stage for embedding training and a subsequent binary classification stage for the downstream cross-attention classifier. Both stages use identical procedures to produce proxy query-reference pairs from the source-separated training data, closely following the methodology established in prior work [7]. 

## 3.4.1 Query-Reference Pair Generation 

Let us denote the stems extracted from the training audio source x as a set S = {s1, s2, ..., sK}, where each stem sk corresponds to a source-separated audio component (e.g., vocals, drums, bass). Given a random timestamp segment ts starting at t and of length ∆t, we first extract corresponding audio segments from each stem as 



<!-- Start of picture text -->
sk(ts) = sk[t, t + ∆t] (6)<br><!-- End of picture text -->

resulting in the set {s1(ts), s2(ts), ..., sK(ts)}. These stem segments are partitioned randomly into two subsets, Sq and Sr, with Sq ∪Sr = S and Sq ∩Sr = ∅. 

A query segment xq is formed as the sum of stems in Sq: 



<!-- Start of picture text -->
xq = � s(ts). (7)<br>s∈Sq<br><!-- End of picture text -->

The reference segment xr is generated by mixing an augmented version of the query segment with the remaining stems: 



<!-- Start of picture text -->
xr = aug2 aug1 (xq) + � s(ts) . (8)<br>� s∈Sr �<br><!-- End of picture text -->

513 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

Here, aug1 and aug2 represent audio effects functions applied sequentially to simulate realistic music production transformations. The effect parameters are sampled from a uniform distribution. Specifically, 

- aug1: time-offset (±250ms) and gain variation (±10dB). 

- aug2: pitch-shifting (±3 semitones) and timestretching (70 - 150%). 

The source-separation system (see Section 4.1) allows the extraction of musically salient sources that can constitute a sample. The pair (xq, xr) constitutes a positive queryreference example; xq is a proxy for a query containing an instance of a sample, and xr represents a reference example which contains the sample that is creatively distorted and is present in a mix along with other musical elements. 

## 3.4.2 Contrastive Learning 

We train the encoder using a self-supervised contrastive learning framework. Given a batch of B pairs {(x<sup>i</sup> q<sup>, x</sup> r<sup>i)}B</sup> i=1<sup>, we obtain their corresponding audio finger-</sup> prints {zq<sup>i, z</sup> r<sup>i}N</sup> i=1<sup>from the encoder.We then employ the</sup> Normalized Temperature-scaled Cross Entropy (NT-Xent) loss [16] to maximize similarity between embeddings from positive pairs, while minimizing cosine similarity to embeddings from all other pairs in the batch. 

## 3.4.3 Downstream Classifier Training 

The cross-attention classifier is trained as a downstream task, with the encoder parameters frozen after the contrastive learning stage. For this stage, we discard the previously used projection network and directly use the node embedding matrix obtained from the encoder. 

Training batches consist of query-reference pairs generated identically to the contrastive learning stage. Let Q = {qi}<sup>B</sup> i=1<sup>cand R = {rj}B</sup> j=1<sup>crepresent query and refer-</sup> ence embedding sets in a batch, respectively, where each embedding qi, rj ∈ R<sup>N×dn</sup> , and Bc is the batch size. Positive examples correspond to pairs of identical indices: 



<!-- Start of picture text -->
P = {(qi, rj) | i = j}, (9)<br><!-- End of picture text -->

while negative examples are selected from pairs with nonidentical indices via hard-negative mining. Specifically, we select negative pairs as the subset of non-positive pairs that maximize audio fingerprint similarity, thus being the most confounding: 



<!-- Start of picture text -->
N = {(qi, rj −) | i̸ = j, r j − = arg r max j ,j̸=i sim(zi, zj)}.<br>(10)<br><!-- End of picture text -->

We maintain a fixed ratio of 1:3 for positive to negative pairs within each training batch. The classifier outputs a scalar prediction p ∈ [0, 1], trained with the binary crossentropy (BCE) loss, where the label for pairs (qi, rj) ∈P is 1 and for for pairs (qi, rj<sup>−)∈Nis0.</sup> 

## 3.5 Retrieval and Evaluation 

Our retrieval system, illustrated in Figure 1, operates in two sequential stages: 

- Approximate nearest-neighbour (ANN) search to do a fast and coarse search of candidate reference audio fingerprints from the database. 

- Cross-attention classifier scoring to refine the candidate set and rank them based on relevance. 

For every overlapping segment (computed as described in Section 3.1) in the query, we probe the reference database for matches based on the similarity of the audio fingerprints; thus yielding a set of candidate matches. 

In the second stage, we utilize the cross-attention classifier to refine these candidate matches. For each candidate segment retrieved, we extract its corresponding node embedding matrix. Given a query recording, represented as a sequence of node embedding matrices, we compute classifier scores p(q, r) for each pair of query q and retrieved candidate r. The final candidate segment-level confidence score is determined by selecting the maximum classifier score over all segments of the query: 



<!-- Start of picture text -->
pclf(q, r) = maxqi∈Q p(qi, r). (11)<br><!-- End of picture text -->

We reject candidate segments with confidence scores pclf(q, r) < 0.5. Subsequently, we aggregate these accepted segment-level scores to obtain a song-level retrieval score. Specifically, for each unique reference recording, we sum the segment-level confidence scores: 



<!-- Start of picture text -->
Psong(q, R) = � Pclf(q, r), (12)<br>r∈R<br><!-- End of picture text -->

where R denotes the set of retrieved segments belonging to the same reference song. The resulting aggregated scores Psong(q, R) provide a robust ranking of candidate songs for each query recording. 

## 4. DATASET 

## 4.1 Training Dataset 

For training, we use the Free Music Archive (FMA) medium dataset [17], which contains 25,000 30-second tracks across 16 genres. We pre-processed this dataset to make it suitable for our stem-mixing contrastive learning approach. We used the current SOTA algorithm “BeatThis” [18] to perform beat tracking and use this as a proxy for musical rhythmic regularity in the FMA tracks, excluding 2,533 tracks with fewer than 32 beats after the first downbeat. This filtering ensured that our training data consisted only of musical content with some level of rhythmic structure. 

To generate the stems that will be used for the synthetic training pairs, we applied source separation using the Hybrid Transformer Demucs model ( `htdemucs` ) [19] to each usable track, separating them into drums, bass, vocals, and “other” stems. 

514 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 4.2 Evaluation Dataset 

For the evaluation of our system, we use the Sample100 dataset [3] . The dataset consists of 75 full-length hiphop recordings (queries) containing samples from 68 fulllength songs (references) across a variety of genres, with R&B/Soul representing the majority [7]. It contains 106 sample relationships and a total of 137 sample occurrences, as some queries use multiple samples and some references appear in multiple queries. To challenge retrieval systems, the dataset includes 320 additional “noise” tracks with a similar genre distribution, which are not sampled in any query. 

Because samples are typically created from a short segment of a song, only a small portion of each candidate track is sampled and present in queries - sample lengths range from just one second to 26 seconds. The samples represent real-world musical “transformative appropriation” [2], including both tonal (riffs), percussive drum break (beats), and 1-note micro-samples. Non-musical samples (e.g. film dialogue) are not included. 

To enable more detailed evaluation, we present an extended version of the Sample100 dataset with fine-grained temporal annotations performed by expert musicians using Sonic Visualiser [20]. Unlike the original dataset, which only provided first occurrence timestamps at 1-second precision, our annotations include precise start and end times for all sample occurrences with ±250ms resolution, transforming the dataset into a segment-wise evaluation resource. This improved temporal granularity allows for more accurate evaluation of ASID systems by testing with short query snippets from anywhere within the sampled material. 

We further enrich the dataset by adding estimates of the time-stretching ratio between the reference and query tracks, as well as instrumentation (stem) annotations for both the original material and the interfering instruments in the query, and expanding the comments about the samples. The time-stretching ratio was calculated from the tempo of both query and reference segments, determined through a combination of automatic beat tracking [18] with manual verification. Stem annotations were performed by listening to the tracks and their source-separated stems to ensure accuracy. Relevant sample class counts are shown in Table 4, including a categorisation into substantial or minimal time-stretching. This new information will enable more nuanced analysis of our model’s performance across different types of sampling practices in section 6.3. 

## 5. EXPERIMENTAL SETUP 

## 5.1 Hyperparameters and Configuration 

Our experimental setup and hyperparameter choices are summarized in Table 1, with certain parameters detailed in the preceding sections. The contrastive learning stage was performed using an NVIDIA A100 GPU, with models trained for a maximum of 180 epochs; we employed early stopping based on validation performance. Training utilized the Adam optimizer coupled with a cosine annealing learning-rate scheduler. For the downstream cross-attention classifier, we trained for a maximum of 5 epochs using 

the Adam optimizer with a fixed learning rate, keeping the encoder parameters frozen to preserve the learned representations from the contrastive learning stage. For the ANN search algorithm, we use IVF-PQ [21], an efficient choice for retrieval tasks in large vector databases. 

|Hyperparameter|Value|
|---|---|
|Sampling rate|16,000 Hz|
|log-power Mel-spectrogram sizeF ×T|64×32|
|Fingerprint {window length, hop}|{4s, 0.5s}|
|Fingerprint dimension|128|
|Node matrix dimension {N,dn}|{32, 512}|
|Temperatureτ|0.05|
|Contrastive batch sizeB|1024|
|Downstream batch sizeBc|32|



Table 1. Experimental Configuration 

## 5.2 Evaluation Metrics 

The ASID task is fundamentally a retrieval problem, where the goal is to rank candidate audio segments based on their relevance to a query. Hence, we adopt mean average precision (mAP) [22] as our primary metric, where the query is computed from a full song containing a sample. The mean average precision (mAP) summarizes retrieval quality by aggregating the precision values at the ranks where relevant items are retrieved, averaged across all queries. 

Additionally, inspired by an established practice in audio fingerprinting literature [10], we report top-N hit rates. Specifically, we measure the proportion of queries for which at least one correct sample is retrieved within the top N ranked results. We do so for different query sizes (5s to 20s). This metric provides an intuitive indication of practical retrieval accuracy and the system’s efficacy for short queries. 

## 5.3 Baseline Framework 

We compare our proposed system against the recent stateof-the-art baseline introduced by Cheston et al. [7]. Their framework employs a ResNet50-IBN architecture and utilizes a multi-task learning approach that jointly optimises a metric learning objective through triplet loss and an auxiliary classification task. This architecture has achieved state-of-the-art retrieval performance in terms of mean average precision (mAP). Due to practical computational constraints, we instead adopt and report results on a ResNet18IBN model, which has a comparable number of parameters to our proposed GNN-based encoder. Apart from the model size, we closely adhere to the training procedures and evaluation methodology outlined in [7]. We also include their reported best performance for reference. 

## 6. RESULTS AND DISCUSSION 

## 6.1 Benchmarking 

We present the performance comparison between our proposed GNN+MHCA architecture and the baseline in Table 2. Our model matches the reported performance of 

515 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

the much larger ResNet50-IBN model, and significantly outperforms the reimplemented baseline. 

|Model|#params|mAP|
|---|---|---|
|ResNet50-IBN(Cheston et al.)|222M|0.441|
|ResNet18-IBN(Baseline)|34M|0.330|
|GNN(Ours)<br>batch size = 1024|20M|0.416|
|GNN +<br>batch size = 256||0.373|
|MHCA<br>batch size = 512|20M|0.411|
|(Ours)<br>batch size = 1024||0.442|



Table 2. Performance of models on Sample100 dataset. 

A key factor influencing our model’s performance is the batch size used during contrastive learning. Increasing the batch size from 256 to 1024 leads to an improvement of 6.9pp in mean average precision (mAP). This improvement occurs because larger batch sizes provide more negative samples per positive pair, enriching the diversity of the contrastive space. Consequently, the model learns embeddings that better discriminate between relevant and irrelevant examples. While larger batch sizes (e.g., 2048) were explored, the associated training time rendered hyperparameter tuning impractical, and thus these results are not reported. 

|Models||Qu|eryLe|ngth||
|---|---|---|---|---|---|
||5 sec|7 sec|10 s|15 sec|20 sec|
|Top|-1 Hit|Rate(%)||||
|ResNet18-IBN(Baseline)|15.8|15.8|16.0|16.5|21.7|
|GNN+MHCA(Ours)<br>Top|15.5<br>-3 Hit|24.6<br>Rate(%)|27.5|26.1|30.7|
|ResNet18-IBN(Baseline)|24.3|24.3|29.2|26.1|32.3|
|GNN+MHCA(Ours)|19.1|32.1|38.3|40.9|50.3|
|Top|-10 Hit|Rate(%)||||
|ResNet18-IBN(Baseline)|27.4|27.4|40.4|45.2|49.1|
|GNN+MHCA(Ours)|19.1|33.8|44.7|51.3|63.2|



performance can be attributed to the combined effect of the two-stage retrieval process, rather than solely to the rejection capability of the classifier. 

## 6.3 Performance by Sample Characteristics 

To understand the performance of the model across sample characteristics, we computed the mAP for different categories of Sample100. As shown in Table 4, there is a modest performance gap between melodic/harmonic riff samples and percussive beat samples (the two 1-note samples were not taken into account). This may be attributed to the nature of beat samples, which consist primarily of drums that are often subject to overdubbing techniques where producers layer additional percussion elements, and that might also be buried deeper in the mix beneath other instrumentation, potentially making them less salient for the GNN to capture. Further analysis by looking at the specific instrumentation in the reference and query, or by applying source separation at detection time, is left for future work. 

|||Type||Time st|retching|
|---|---|---|---|---|---|
||Riff|Beat|1-note|>5%|<5%|
|# samples|71|33|2|44|62|
|mAP|0.471|0.391|-|0.340|0.503|



Table 4. Performance according to sample class. 

A significant performance gap was observed in relation to time stretching, where we classified samples subjected to minimal time stretching (<5%) and those with significant time stretching (>5%). This 16.3pp difference in performance shows that although our model is robust to some degree of time-stretching, large changes in tempo fundamentally alter the temporal relationships between audio features that our model relies on for identification. 

Table 3. Hit rates of our framework and baseline. 

## 7. CONCLUSION AND FUTURE WORK 

Table 3 shows our model’s performance on short queries, a common use case in real-world sample identification scenarios. While the hit rates for shorter queries are comparable to the baseline, our framework exhibits significantly superior performance for longer queries (14.1pp increase in top-1 hit rate for 20-second-long queries). The progressive improvement in hit rates with increasing query length show that our approach effectively aggregates segment-level confidence scores to retrieve the correct reference song. 

## 6.2 Retrieval Refinement via Cross-Attention Classifier 

To examine the impact of the cross-attention classifier as a retrieval refinement step, we conduct an ablation study. Table 2 shows that incorporating the classifier (MHCA) to rank retrieved results improves mAP by 2.6pp, confirming the utility of this refinement stage. Additionally, to evaluate the classifier’s capability to reject irrelevant matches, we construct a balanced validation set comprising 300 positive query-reference pairs and 300 negative pairs drawn from the “noise” data described in Section 4.2. The classifier achieves an AUROC score of 0.776, indicating that it does not perfectly discriminate between genuine and confounding examples. Thus, the observed improvement in retrieval 

This paper presents a lightweight GNN-based approach for automatic sample identification that achieves state-of-theart performance while using only 9% of the parameters compared to previous methods. Our key contributions include adapting a GNN encoder for sample identification, introducing a cross-attention classifier for refining retrieval results, and extending the Sample100 dataset with fine-grained temporal annotations that enable granular evaluation. 

Our results show that the proposed framework achieves a mAP of 44.2%, with strong performance on melodicharmonic samples and samples with low time-stretching. Our framework’s cross-attention stage is useful in the refining of the ranking, and introduces rejection capabilities. 

Future work should explore end-to-end training methods robust to sampling transformations, and explore integrating source separation during inference to improve performance on heavily masked samples. Newly available annotations can be leveraged for analysis of how specific attributes of samples (instrumentation type, interpolation, genre) affect identification accuracy, and we hope the release of our extended Sample100 dataset will aid the development of specialized techniques that address the most challenging cases in ASID. 

516 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 8. ACKNOWLEDGMENTS 

We thank Matthew Alan Walford for his contributions to the new annotations of the Sample100 dataset. This research utilised Queen Mary’s Apocrita HPC facility, supported by QMUL Research-IT (http://doi.org/10.5281/zenodo.438045). This work was supported by UKRI - Innovate UK (Project no. 10102241). A. Bhattacharjee is a research student at the UKRI Centre for Doctoral Training in Artificial Intelligence and Music, supported jointly by UK Research and Innovation [grant number EP/S022694/1] and Queen Mary University of London. 

## 9. REFERENCES 

- [1] K. McLeod, P. DiCola, J. Toomey, and K. Thomson, Creative License: The Law and Culture of Digital Sampling. Durham, NC, USA: Duke University Press, 2011. 

- [2] J. Demers, Steal This Music: How Intellectual Property Law Affects Musical Creativity. Athens, GA, USA: University of Georgia Press, 2006. 

- [3] J. V. Balen, “Automatic recognition of samples in musical audio,” Master’s thesis, Universitat Pompeu Fabra, Barcelona, Spain, 2011. 

- [4] S. Gururani and A. Lerch, “Automatic sample detection in polyphonic music,” in Proc. of the 18th Int. Society for Music Information Retrieval Conf., Suzhou, China, 2017. 

- [5] D. Ellis, “audfprint: Landmark-based audio fingerprinting,” 2014, software. [Online]. Available: https://github.com/dpwe/audfprint 

- [6] J. Six and M. Leman, “Panako - a scalable acoustic fingerprinting system handling time-scale and pitch modification,” in Proc. of the 15th Int. Society for Music Information Retrieval Conf., Taipei, Taiwan, 2014. 

- [7] H. Cheston, J. V. Balen, and S. Durand, “Automatic identification of samples in hip-hop music via multi-loss training and an artificial dataset,” 2025, arXiv preprint arXiv:2502.06364. [Online]. Available: https://arxiv.org/abs/2502.06364 

- [8] X. Du, Z. Yu, B. Zhu, X. Chen, and Z. Ma, “Bytecover: Cover song identification via multi-loss training,” in Proc. IEEE Int. Conf. Acoustics, Speech and Signal Processing, Toronto, ON, Canada, 2021, pp. 551–555. 

- [9] X. Xu, X. Chen, and D. Yang, “Key-invariant convolutional neural network toward efficient cover song identification,” in Proc. IEEE Int. Conf. Multimedia and Expo, San Diego, CA, USA, 2018. 

- [10] S. Chang, D. Lee, J. Park, H. Lim, K. Lee, K. Ko, and Y. Han, “Neural audio fingerprint for high-specific audio retrieval based on contrastive learning,” in Proc. 

IEEE Int. Conf. Acoustics, Speech and Signal Processing, Toronto, ON, Canada, 2021, pp. 3025–3029. 

- [11] A. Singh, K. Demuynck, and V. Arora, “Attention-based audio embeddings for query-by-example,” in Proc. of the 23rd Int. Society for Music Information Retrieval Conf., Bengaluru, India, 2022, pp. 52–58. 

- [12] G. Li, M. Muller, A. Thabet, and B. Ghanem, “Deepgcns: Can gcns go as deep as cnns?” in Proc. IEEE/CVF Int. Conf. Computer Vision, Seoul, Korea, 2019, pp. 9267–9276. 

- [13] A. Bhattacharjee, S. Singh, and E. Benetos, “Grafprint: A gnn-based approach for audio identification,” in Proc. IEEE Int. Conf. Acoustics, Speech and Signal Processing, Hyderabad, India, 2025. 

- [14] S. Singh, C. J. Steinmetz, E. Benetos, H. Phan, and D. Stowell, “Atgnn: Audio tagging graph neural network,” IEEE Signal Processing Letters, 2024. 

- [15] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Łukasz Kaiser, and I. Polosukhin, “Attention is all you need,” Advances in Neural Information Processing Systems, vol. 30, 2017. 

- [16] T. Chen, S. Kornblith, M. Norouzi, and G. Hinton, “A simple framework for contrastive learning of visual representations,” in Proc. Int. Conf. Machine Learning, 2020, pp. 1597–1607. 

- [17] M. Defferrard, K. Benzi, P. Vandergheynst, and X. Bresson, “Fma: A dataset for music analysis,” in Proc. of the 18th Int. Society for Music Information Retrieval Conf., Suzhou, China, 2017. 

- [18] F. Foscarin, J. Schlüter, and G. Widmer, “Beat this! accurate beat tracking without dbn postprocessing,” in Proc. of the 25th Int. Society for Music Information Retrieval Conf., San Francisco, CA, USA, 2024. 

- [19] S. Rouard, F. Massa, and A. Défossez, “Hybrid transformers for music source separation,” in Proc. IEEE Int. Conf. Acoustics, Speech and Signal Processing, Rhodes Island, Greece, 2023. 

- [20] C. Cannam, C. Landone, and M. Sandler, “Sonic visualiser: An open source application for viewing, analysing, and annotating music audio files,” in Proc. ACM Multimedia Int. Conf., Firenze, Italy, 2010, pp. 1467–1468. 

- [21] J. Johnson, M. Douze, and H. Jégou, “Billion-scale similarity search with gpus,” IEEE Transactions on Big Data, vol. 7, no. 3, pp. 535–547, 2019. 

- [22] J. S. Downie, “The music information retrieval evaluation exchange (2005–2007): A window into music information retrieval research,” Acoustical Science and Technology, vol. 29, no. 4, pp. 247–255, 2008. 

517 

