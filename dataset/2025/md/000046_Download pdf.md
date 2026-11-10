---
paper_id: "000046"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706424/files/000046.pdf"
---

# ENHANCING NEURAL AUDIO FINGERPRINT ROBUSTNESS TO AUDIO DEGRADATION FOR MUSIC IDENTIFICATION 

R. Oguz Araz<sup>1</sup> Guillem Cortès-Sebastià<sup>2</sup> Emilio Molina<sup>2</sup> Joan Serrà<sup>3</sup> Xavier Serra<sup>1</sup> Yuki Mitsufuji<sup>3,4</sup> Dmitry Bogdanov<sup>1</sup> 

1 Music Technology Group, Universitat Pompeu Fabra, Barcelona, Spain 

2 BMAT Licensing S.L., Barcelona, Spain 

3 Sony AI 4 Sony Group Corporation `recepoguz.araz@upf.edu` 

## ABSTRACT 

Audio fingerprinting (AFP) allows the identification of unknown audio content by extracting compact representations, termed audio fingerprints, that are designed to remain robust against common audio degradations. Neural AFP methods often employ metric learning, where representation quality is influenced by the nature of the supervision and the utilized loss function. However, recent work unrealistically simulates real-life audio degradation during training, resulting in sub-optimal supervision. Additionally, although several modern metric learning approaches have been proposed, current neural AFP methods continue to rely on the NT-Xent loss without exploring the recent advances or classical alternatives. In this work, we propose a series of best practices to enhance the self-supervision by leveraging musical signal properties and realistic room acoustics. We then present the first systematic evaluation of various metric learning approaches in the context of AFP, demonstrating that a self-supervised adaptation of the triplet loss yields superior performance. Our results also reveal that training with multiple positive samples per anchor has critically different effects across loss functions. Our approach is built upon these insights and achieves state-of-the-art performance on both a large, synthetically degraded dataset and a real-world dataset recorded using microphones in diverse music venues. 

## 1. INTRODUCTION 

Audio fingerprinting (AFP) methods are used for identifying unknown audio content [1–3]. Identification is achieved by extracting distinctive representations, known as fingerprints, from audio segments, which are matched against a database of reference audio. Possible AFP applications include music identification (MI) [4], duplicate detection [5], and broadcast monitoring [6]. This paper 

© R. O. Araz, G. Cortès-Sebastià, E. Molina, J. Serrà, X. Serra, Y. Mitsufuji, and D. Bogdanov. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: R. O. Araz, G. Cortès-Sebastià, E. Molina, J. Serrà, X. Serra, Y. Mitsufuji, and D. Bogdanov, “ Enhancing Neural Audio Fingerprint Robustness to Audio Degradation for Music Identification ”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

focuses on MI, where scalability is crucial due to large databases, requiring compact fingerprints for efficient retrieval. MI can be performed at both the track-level and segment-level, the latter involving time-aligned matching between query audio and reference tracks. 

In MI, query audio can significantly differ from its reference track due to various factors. Intentional transformations, such as pitch shifting and time stretching, can alter a track, and since MI often relies on microphone recordings of playback sounds, the query audio may be degraded due to signal transduction and environmental factors during sound propagation. For accurate identification, fingerprints should be robust enough to be recognized despite such alterations. One existing approach, NowPlaying [7], learns to create robust fingerprints from real recordings of aligned clean-degraded music pairs. However, such datasets are costly to gather and, hence, most methods rely on selfsupervision from synthetic audio degradations. [8–11]. 

The quality of the representations obtained by selfsupervised learning (SSL) is influenced by various factors, including the nature of the self-supervision signal and the calculation of the loss function. Yet, current neural AFP approaches unrealistically simulate real-life audio degradation during training, providing sub-optimal supervision. Moreover, although recent work in neural AFP generally assumes that the NT-Xent [12] loss outperforms other classical losses on MI, a systematic comparison between these objectives is missing. Besides, several modern contrastive self-supervised losses that build on the NT-Xent loss have shown promise in related audio tasks [13,14], but have not been evaluated in the context of AFP. In addition, some of these loss functions allow the construction of training batches with multiple differently degraded versions of the same clean audio, a strategy that could improve identification but remains unexplored within the scope of AFP. 

Our work builds upon NAFP [9], a neural AFP approach that generates real-valued fingerprints, with open-source code and pre-trained weights. We uncover several suboptimal design choices of NAFP regarding its SSL strategy and treatment of room acoustics. To address these issues, we propose a series of best practices that significantly enhance identification performance. Moreover, we reveal critical implementation problems in NAFP’s evaluation method that skew performance metrics. We revise 

399 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

these problems and conduct evaluations on both synthetically degraded queries and a real-world dataset recorded with microphones across diverse music venues. Next, we assess the effectiveness of different loss functions for AFP, demonstrating that the triplet loss, contrary to common belief, delivers the best performance. We then explore the benefits and drawbacks of increasing the number of positive samples per anchor in a batch, providing practical training guidelines. Building on these improvements, we obtain a state-of-the-art approach, outperforming the publicly available baselines. We share our pre-trained model weights, open-source code, and data.<sup>1</sup> 

## 2. RELATED WORK 

## 2.1 Metric learning 

Metric learning aims to create representations in which semantically similar elements are closer to each other than semantically dissimilar ones. The triplet loss [15] is a supervised metric learning function that is proven effective in various retrieval tasks. It uses class labels to form triplets of anchor, positive, and negative samples. 

Recent work leverages self-supervised metric learning, with NT-Xent being a particularly successful loss function [12]. More recent work then builds upon NT-Xent: DCL [16] decouples positive pair’s similarities from the negative pairs’; A&U [17] proposes two qualities that good representations should obtain, and theoretically proves that using NT-Xent with an infinite-size batch optimizes them; KCL [18] re-formulates A&U to require a smaller batch. 

NT-Xent and its extensions are only defined for a single positive sample per anchor. SupCon [19] (supervised) and MultiPosCon [20] (self-supervised) both extend NTXent to multiple positives per anchor, reporting benefits in image-related tasks. Notably, MultiPosCon and NT-Xent are equivalent when each anchor has only one positive. Hence, for simplicity, we treat them synonymously. 

The quality of learned representations is influenced by how the batches are constructed, particularly by the number of anchor samples and the number of positives per anchor [15]. However, these aspects remain unexplored in AFP. To address this gap, we perform controlled experiments. Throughout this paper, let NA denote the number of anchors in a batch and NPPA the number of positives per anchor. The number of total samples in a batch is then NB = NA (1 + NPPA). 

## 2.2 Neural AFP 

Neural AFP approaches can be broadly classified into two categories based on the generated fingerprints: binary and real-valued. In this work, we focus on the latter. Relevant approaches include NowPlaying [7], which employs the triplet loss to train a convolutional neural network (CNN), and also CULAF [8], NAFP [9], and ABFP [10], all of which use the NT-Xent loss to train CNNs. Additionally, GraFP [11] trains a graph CNN with the NT-Xent loss. 

> 1 `https://github.com/raraz15/neural-music-fp` 

|Model|FS [Hz]|TL [s]|TH[s]|Available|
|---|---|---|---|---|
|NowPlaying [7]|n/a|n/a|1.000|✗|
|CULAF [8]|16 k|2.50|2.125|✗|
|NAFP [9]|8 k|1.00|0.500|✓|
|ABFP [10]|16 k|0.96|0.096|✗|
|GraFP [11]|16 k|1.00|0.100|✓|
|NMFP (proposed)|8 k|1.00|0.500|✓|



Table 1. Real-valued neural AFP models. Columns indicate the sampling rate (FS), segment duration (TL), hop duration (TH), and publicly available code and weights. 

Table 1 compares these approaches in terms of two aspects that determine an AFP system’s use case: audio sampling rate and fingerprint generation rate (measured by the hop duration). We do not consider high sampling rates necessary for MI, as query audio is often transmitted over bandwidth-limited channels. Moreover, since humans can typically identify music even under low-pass filtering, a robust system should be capable of doing the same. Likewise, the hop sizes around 100 ms used by GraFP and ABFP substantially increase the time, storage, and computational costs of fingerprint extraction and retrieval, reducing overall scalability. This becomes evident by looking at their reported test databases containing 30-second audio chunks instead of full tracks, selected from the Free Music Archive (FMA) [21]. They contain about 97 k ( `fma_large` ) and 25 k ( `fma_medium` ) chunks, corresponding to 28.3 M and 7.3 M fingerprints, respectively. By contrast, NAFP’s test database (and ours, as discussed in Section 3.4) contains over 93 k full-length tracks ( `fma_full` ), totaling 53.6 M fingerprints. Using a 100 ms hop duration would result in 268 M fingerprints, requiring much longer time for both extraction and retrieval. 

## 3. METHODOLOGY 

In this section, we outline NAFP’s methodology and, where applicable, describe our modifications. 

## 3.1 Audio degradations 

NAFP authors focus on achieving robustness against three types of audio degradation: additive background noise, room reverberation, and microphone response. We follow their degradation chain, but curate more extensive sets for each type. NAFP uses background noise recordings featuring a mix of random noises and two specific acoustic scenes: subway and pub environments. However, we found this selection to lack sufficient diversity, and instead adopted the TUT Acoustic Scenes 2016 dataset [22], which includes 15 distinct acoustic scenes representing various potential MI use cases. The training and test sets consist of 585 and 195 minutes of recordings, respectively. 

For room impulse responses (IRs), we use OpenAIR [23] and AIR [24] datasets, similar to NAFP, but with adjustments considering room acoustics. From OpenAIR, we use all 143 mono and stereo recordings from 28 diverse environments, such as halls and churches, chosen for their 

400 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

long-duration IRs. From AIR, we use the IRs recorded without a dummy head. For the binaural recordings, we include both channels separately, as they capture different reflection patterns, resulting in 60 IR measurements from 6 rooms. Unlike NAFP, we also utilize the MIT-Survey [25] dataset, contributing 270 IRs from various public spaces. 

For microphone IRs, we exclusively use the dataset provided by Franco et al. [26]. It contains measurements of 25 microphones encompassing 38 unique microphone-polar pattern combinations. The IRs were measured at distances of 0.5 m, 1.25 m, and 5 m and at multiple incident angles, from which we chose integer multiples of 60<sup>◦</sup> . 

We partition the recordings for each degradation into train and test sets. For background noise, we use the partitions proposed in Mesaros et al. [22]. For IRs, we ensure that the measurements of the same room or microphone are contained in either the training or test set. This consideration does not hold in the publicly available IR partitions of NAFP, which can be verified by comparing the filenames. 

## 3.2 Training 

NAFP authors experiment with two variations based on the training optimizer: Adam [27] and LAMB [28]. The authors reported that LAMB requires a much larger batch size to achieve high performance, making training on consumer-grade GPUs impractical. As a result, we adopt the Adam variation as our baseline, whose pre-trained weights are unavailable. Therefore, we train NAFP-Adam ourselves using the official implementation and the provided audio degradation datasets.<sup>2</sup> In all our experiments, we use the same training music as NAFP: 10 k audio chunks of 30 s duration, sourced from `fma_medium` . 

NAFP has an audio context of one second, and fingerprints are extracted with a 500 ms hop duration at inference. At training, a ± 200 ms random offset is applied between positive and anchor samples to enhance robustness to potential misalignment between query and reference fingerprints. We increase this offset to ± 250 ms, corresponding to 50% of the hop duration, which we find more intuitive. As for input features, we follow the same magnitude mel-spectrogram extraction parameters as NAFP but apply a slightly different formulation during the power conversions step. Finally, we scale the features to [−1, 1], using the global dynamic range of 80 dB. 

We train all models for 100 epochs with the same architecture, optimizer, learning rate scheduler, SpecAugment [29] implementation, and NT-Xent parameter τ as in NAFP-Adam. However, we train our models using automatic mixed precision. The configuration NA = 768, NPPA = 1 requires approximately 15 hours to complete on a single NVIDIA RTX 4090 GPU and 20 CPU cores. 

## 3.3 Retrieval 

NAFP performs a two-stage retrieval using Faiss [30], a library for efficient large-scale similarity search. First, for 

> 2 `https://github.com/mimbres/neural-audio-fp/` 

each fingerprint in the query sequence, the top 20 approximately most similar segments are retrieved. Then, a candidate sequence is constructed for each unique segment, considering its position in the query sequence, and the average similarity score is calculated between the query and candidate sequences. The original Faiss index type and hyper-parameters are kept unchanged in our work. 

## 3.4 Evaluation 

NAFP measures identification performance using the Top1 hit rate metric, which we also employ. However, whereas NAFP evaluates only segment-level identification (focusing on exact and near matches within one hop duration), we evaluate both track- and segment-level identification. 

We discovered that, in NAFP’s evaluation, some query tracks were represented up to 11 times, while others were not represented at all, skewing the results. To address this, we use 30-second audio chunks as queries and select 6 equally spaced indices within the chunk. Starting from each index, we query fingerprint sequences of lengths 1, 3, 9, and 19, corresponding to 1, 2, 5, and 10 seconds of audio, respectively. This method efficiently utilizes the chunks and ensures that each track contributes uniformly to the metric. Additionally, NAFP’s fingerprint storage implementation simply concatenates fingerprints from all query chunks, disregarding track boundaries. As a result, 12.7% of the query sequences contain fingerprints from two tracks. In our implementation, we ensure that each query sequence is contained within a single track. 

Various approaches, including NAFP, perform evaluations on synthetically degraded queries [1,2,31–33], while only a few consider real microphone recordings [7,34]. We evaluate our models on both types of data. 

Syntheticly degraded queries — We build our synthetic evaluation on NAFP’s publicly available test set, which is a subset of `fma_full` . However, it is known that FMA contains duplicates, so we perform duplicate removal. Their test database contains 93,358 full-length tracks. We noted that 1,205 unique tracks were not included, which we included in our test database, resulting in 95,163 total tracks, distinct from the training tracks. 

For the query set, NAFP uses audio chunks of 30second duration from 500 tracks, which is insufficient for a comprehensive evaluation. A larger set increases statistical power, offers better insight into robustness across various degradations, and reduces potential biases. Therefore, we additionally incorporate 9,500 random tracks from our test database, bringing the total to 10,000 query tracks. We then degrade each track from start to end by sequentially applying additive background noise (using a random SNR sampled uniformly from [0,10] dB), followed by convolution with room and microphone IRs (interleaved with random gain, using full IR durations). From the resulting audio, we randomly sample 30-second chunks to be used as queries. We make this dataset publicly available. 

It is worth emphasizing that our evaluation setup uses significantly more queries than those used in NAFP, GraFP, and ABFP, and our database is substantially larger than 

401 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

those used in GraFP and ABFP. Therefore, our evaluation provides a more comprehensive and realistic assessment of scalability than prior work. We argue that scalability claims should be evaluated under similar conditions. 

Real-world data — We conduct a real-world evaluation in collaboration with BMAT Licensing S.L. using a dataset of microphone recordings captured using smartphones and digital recorders in various settings, including bars, nightclubs, and concert halls. The ground truth was established by a fingerprinting system against a large database, with results verified by human annotators. All reference tracks have at least one match, totaling 3,692 query-reference pairs. Although the dataset is not large enough to test scalability, it serves well for testing robustness in real environments. 

## 4. NEURAL MUSIC FINGERPRINTING 

We propose a new approach for training neural AFP models that focuses on musical signal properties and real-life audio degradation. First, to establish a baseline, we benchmark the NAFP-Adam model on track-level identification. Next, we incrementally apply a series of best practices to this baseline to facilitate the learning process, validating the contribution of each. Finally, we explore a range of metric learning approaches to further enhance performance. We refer to our method as NMFP (Neural Music Fingerprinting) to highlight its focus on MI. 

## 4.1 Best practices for MI 

In this section, we improve the self-supervision during training by more closely simulating real-life audio degradation, eliminating faulty learning signals, and providing the model with additional cues. Altogether, our practices improve identification performance by 8.3% and 20.9% on the synthetic and real-world datasets, respectively (Table 2). Notably, our practices add negligible training overhead while substantially raising performance, making them our recommended best practices for training. 

Appropriate audio degradation datasets — Selfsupervision comes from the objective of embedding the clean audio and its synthetically degraded version close to each other. By exposing the model to degradations that closely resemble those encountered in real-world scenarios, we encourage structuring the learned representations accordingly. Therefore, the choice of degradation data is critical; it should reflect realistic use cases. Training with our degradation datasets as opposed to those of NAFP increases performance on both datasets (Table 2, rows 1–2). 

Eliminating false negatives — The objective of the NTXent loss is to increase the similarity between an anchor and its positive, while decreasing the similarity with all its negatives in the batch. However, in NAFP, a batch can contain multiple anchor samples from the same track with an 18% probability (64 segments chosen from 590,000 segments across 10,000 tracks with 59 segments each). Belonging to the same track, these samples share various musical properties. Yet, the loss function treats them as neg- 

ative pairs, resulting in a faulty learning signal. In our implementation, we eliminate false negatives by ensuring that each batch contains one anchor sample per track. This increases fingerprint distinctiveness (Table 2, rows 2–3). 

Full IRs — During training, NAFP truncates all IRs to 75 ms. For a room IR, this duration only includes the early reflections [35]. We aim for more realistic degradation so that our models can learn to generate robust fingerprints against real-life reverberation. Therefore, we use the full duration of IRs, which can go up to several seconds for large rooms [25]. However, in practice, we truncate IRs to the model’s context length, as the longer part will not contribute to the current segment. The resulting model exhibits improved robustness (Table 2, rows 3–4). 

Past reverberation degradation — Query fingerprints extracted from microphone recordings contain reverberation, including the tails of past sound events. Previous audio degradation methods often overlook this aspect, convolving an audio segment with a room IR as if the sound starts abruptly, without acoustic history. Misrepresenting reverberation can result in learning unrealistic representations, especially in such fine-grained applications. Hence, we convolve audio segments starting from their past context and discard the past after convolution, yielding a segment that contains the reverberation of current and past events. Matching the model’s context, we use a one-second past context duration. This increases robustness considerably (Table 2, rows 4–5). 

Lower frequencies — The 300 Hz lower frequency cutoff applied in NAFP’s feature extraction discards valuable information that can provide additional musical cues. In music venues such as concert halls and festival areas, at long distances from the speakers, the bass frequencies will form the majority of the sounds surviving the background noise from the crowd. Since most microphones, including smartphone microphones, can capture lower frequencies, extending the frequency range can provide benefits across different recording devices. We tested multiple values and selected a 160 Hz bound. The resulting model achieves further improved performance (Table 2, rows 5–6). 

## 4.2 Exploring metric learning 

Having improved the self-supervision, we now explore different metric learning methods to further enhance the identification performance. This exploration includes comparing several loss functions, investigating the effect of training with different numbers of anchors and positives per anchor, and tuning loss function hyper-parameters. 

Loss function comparison — Most neural AFP models rely on NT-Xent without comparison with other losses under consistent settings. Here, we systematically compare multiple losses, searching for additional benefits. Specifically, we consider the triplet, NT-Xent, DCL, KCL, and A&U losses. For DCL, we use the same τ parameter as NT-Xent. For A&U and KCL, we take the default parameters in the respective publications. For the triplet loss, we employ hard positive and semi-hard negative mining, 

402 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

||||||||||Top-1 hit|rate (%|)|||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Row|Approach|FN|TIR|Past|FLC||Synthe|tic data|||Real-w|orld data||
|||||||1 s|2 s|5 s|10 s|1 s|2 s|5 s|10 s|
|1|Baseline|✗|75 ms|✗|300 Hz|72.2|82.8|89.7|92.3|33.6|49.9|65.4|71.7|
|2||✗|75 ms|✗|300 Hz|74.4|83.8|89.9|92.1|39.4|56.2|70.5|76.1|
|3||✓|75 ms|✗|300 Hz|76.7|85.8|91.6|93.6|45.5|64.8|77.3|81.9|
|4|Ours|✓|1 s|✗|300 Hz|77.9|86.7|92.0|93.8|49.3|66.7|78.5|82.6|
|5||✓|1 s|✓|300 Hz|80.1|87.9|92.5|94.2|50.6|68.1|79.2|83.0|
|6||✓|1 s|✓|160 Hz|80.5|88.0|92.6|94.2|54.5|70.7|81.0|84.3|



Table 2. Improvements over NAFP in track-level identification using our test set. ‘FN’ indicates if the false negatives issue in the batches is corrected, TIR denotes the impulse response truncation duration, ‘Past’ indicates whether the acoustic history is applied during reverberation, and FLC specifies the lower cut-off frequency during feature extraction. 

|||Top-1 h|it rate (%)|||||Top-1 h|it rate (%|)|
|---|---|---|---|---|---|---|---|---|---|---|
|Loss|Synthe|tic data|Real-w|orld data|Loss|τ, α|Synthe|tic data|Real-w|orld data|
||1 s|2 s|1 s|2 s|||1 s|2 s|1 s|2 s|
|NT-Xent|84.1|90.1|58.7|72.3||0.01|83.2|89.8|61.2|74.3|
|DCL|83.0|89.6|54.5|68.7|NT-Xent|0.02|83.8|90.0|61.8|74.6|
|A&U|76.4|86.2|48.0|66.3|(τ)|0.05|84.1|90.1|58.7|72.3|
|KCL|38.8|60.6|18.2|41.1||0.07|81.8|88.8|53.8|69.2|
|Triplet|86.4|91.6|63.4|75.1|Tilt|0.3|85.9|91.2|63.8|74.9|
|<br>|||||rpe<br>|0.5|86.6|91.7|63.9|75.0|
|le 3.<br>Loss|function c|ompariso|n on track|-level identi-|(α)|0.7|86.7|91.6|63.3|74.7|



Table 3. Loss function comparison on track-level identification using NA = 768 and NPPA = 1. 

Table 5. Hyper-parameter tuning results on track-level identification for NT-Xent (NA = 768, NPPA = 1) and triplet (NA = 512, NPPA = 2) losses. 

|||||Top-1 hi|t rate (|%)|
|---|---|---|---|---|---|---|
|Loss|NA|NPPA|Synth|etic data|Real-w|orld data|
||||1 s|2 s|1 s|2 s|
||64|1|80.5|88.0|54.5|70.7|
||512|1|84.1|90.2|58.2|71.8|
|NT-Xent|768|1|84.1|90.1|58.7|72.3|
||512|2|76.9|85.5|46.0|63.4|
||384|3|74.6|83.7|44.2|62.0|
||64|1|82.8|89.4|57.4|72.1|
||512|1|86.1|91.4|62.5|74.7|
|Triplet|768|1|86.4|91.6|63.4|75.1|
||512|2|86.6|91.7|63.9|75.0|
||384|3|86.1|91.2|63.0|74.6|



Increasing the number of anchors — For the NT-Xent loss in Table 4, increasing NA from 64 to 512 yields a 3.6% improvement on synthetic data, whereas further increasing to 768 causes a saturation. On real-world data, however, increasing NA from 64 to 768 consistently improves performance. For the triplet loss, training with larger NA progressively increases performance on both datasets. 

Number of anchors vs positives per anchor — On the one hand, exposing the model to a diverse set of tracks within a batch is beneficial for learning discriminative representations. On the other hand, presenting multiple degraded versions of the same audio segment can help the model learn invariance to real-world distortions. However, due to the GPU memory constraint, increasing the number of positives per anchor reduces the number of anchors that can fit in a batch, creating a trade-off between diversity and invariance. To create multiple positives for an anchor, we randomly shift the anchor independently and use a different combination of degradations. 

Table 4. Effect of NA and NPPA for NT-Xent and triplet losses. 

computing the loss function using the squared Euclidean distance with a margin of α = 0.5. In this experiment, for a fair comparison, we use NA = 768 for all losses and use one positive per anchor for the triplet loss (NPPA = 1), since the remaining losses are only defined for this setting. 

In Table 4, when the number of total samples in a batch is set to 1536, switching from NPPA = 1 to NPPA = 2 or NPPA = 3 significantly degrades NT-Xent’s performance on both datasets. Moreover, when NA = 512, using NPPA = 2 performs significantly worse than NPPA = 1 on both datasets. These two observations show that, for NTXent, using more than one positive per anchor is detrimental, which is not caused by the reduced number of anchors. Indeed, training with NA = 64 and NPPA = 1 (roughly ten 

Table 3 reports the results, where the triplet loss outperforms all other loss functions. Compared to its closest competitor, NT-Xent, it scores 2.3% and 4.7% higher on the synthetic and real-world data, respectively. Notably, the NT-Xent loss outperforms its extensions: DCL, A&U, and KCL. While we find the decoupling idea of DCL intuitive, our results do not show an improvement. Based on these results, we retain only the triplet and NT-Xent losses for the remainder of our experiments. 

403 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

|||||Top-1 hi|t rate (%)||||
|---|---|---|---|---|---|---|---|---|
|Model||Synthe|tic data|||Real-wo|rld data||
||1 s|2 s|5 s|10 s|1 s|2 s|5 s|10 s|
|NAFP-Adam|72.2|82.8|89.7|92.3|33.6|49.9|65.4|71.7|
|NAFP-LAMB [9]|73.8|83.9|90.4|92.7|42.0|58.6|71.4|76.3|
|GraFP-500 ms|17.0|34.8|52.1|63.6|20.0|42.5|62.0|69.4|
|GraFP-100 ms [11]|19.7|53.6|72.3|80.0|46.6|60.8|74.8|82.5|
|NMFP (proposed)|86.6|91.7|94.5|95.6|63.9|75.0|82.0|84.6|



Table 6. Final comparison on track-level identification. 

times smaller batch size) performs significantly better on both datasets. Therefore, we conclude that NPPA = 1 is the best setting for NT-Xent. For the triplet loss, Table 4 shows that training with NPPA = 2 yields the best performance and, unlike NT-Xent, increasing NPPA does not deteriorate the performance significantly. Notably, training with NPPA = 3 and NPPA = 1 performs comparably, even though the musical variety in a batch is half the amount. Hyper-parameter tuning — In Table 4, we have seen that the triplet loss outperforms NT-Xent in all NPPA-NA combinations. To gain insight into the effect of hyperparameters, we experiment with different τ (NT-Xent) and α (triplet) values. The results are given in Table 5, where the triplet loss again outperforms NT-Xent by a significant amount on both datasets. Notably, NT-Xent’s performance is improved on real-world data by using a smaller τ parameter. Based on these results, we choose the triplet loss with NA = 512, NPPA = 2, and α = 0.5 for our NMFP model. 

|Mdl|Mth|To|p-1 hit|rate (|%)|
|---|---|---|---|---|---|
|oe|ac|1 s|2 s|5 s|10 s|
|NAFP-Adam|exact<br>near|50.5<br>61.2|64.8<br>74.2|74.1<br>83.4|78.2<br>87.7|
|NAFPLAMB 9|exact|55.1|66.4|74.4|77.9|
|- []|near|62.7|74.6|83.3|87.4|
|NMFP d|exact|63.8|74.8|82.0|85.0|
|(propose)|near|75.6|83.5|89.2|92.0|



Table 7. Segment-level identification results on the synthetic dataset. 

outperforms its baseline, NAFP-Adam, by 13.3% in exact matches and 14.4% in near matches. NMFP also outperforms NAFP-LAMB by 8.7% in exact matches and 12.9% in near matches. Together, the results in Table 6 and Table 7 demonstrate that our model, NMFP, sets the state-ofthe-art on both track- and segment-level MI. 

## 5. RESULTS 

## 6. CONCLUSION 

Here, we compare NMFP with NAFP-Adam (baseline method) and the only state-of-the-art models with publicly available weights: NAFP-LAMB [9] and GraFP [11]. NMFP and NAFP models are trained at 8 kHz sampling rate, while GraFP was trained at 16 kHz, hence requiring upsampling. Additionally, GraFP uses a 100 ms hop, whereas our models operate with 500 ms. We consider GraFP with each hop duration. 

Table 6 shows that NMFP substantially outperforms both NAFP and GraFP on track-level identification. In particular, NMFP improves its baseline (NAFP-Adam) by 14.4% on synthetic data and 30.3% on real-world data, and it surpasses the official NAFP-LAMB by 12.8% and 21.9%, respectively. Against GraFP, NMFP scores 69.6% higher on synthetic data and 43.9% on real-world data when using a 500 ms hop. With a 100 ms hop, it still outperforms GraFP by 66.9% on synthetic data and 17.3% on real-world data. This drastic difference could be due to the applied upsampling, which can not create the higher frequencies that GraFP likely depends on. 

In Table 7, we compare NMFP against NAFP on segment-level identification on the synthetic data. We exclude GraFP from this comparison, as its authors do not consider segment-level identification, and due to their peak picking methods’ interaction with silent segments. NMFP 

We present a comprehensive framework for enhancing the robustness of neural AFP models against real-world audio degradation. By correcting evaluation flaws in prior work, we establish a more reliable benchmark for future AFP research. Our evaluations, conducted on both a synthetic dataset and a real-world dataset recorded in diverse music venues, show that NMFP significantly outperforms existing neural AFP models with publicly available weights. Specifically, on track-level identification, it outperforms the official NAFP model by 12.9% on synthetic data and by 21.9% on real-world data. 

Our success stems from two key areas. First, we show that paying careful attention to musical signal properties and room acoustics enhances performance considerably. Second, by revisiting metric learning, we uncovered several key findings that further improve performance. We discovered that the triplet loss, despite common assumptions, outperforms modern alternatives such as NT-Xent. We also found that triplet loss does not suffer from the performance saturation seen with NT-Xent at large batch sizes. Finally, we characterized a critical trade-off between the number of anchors and positives per anchor in training batches. Together, these insights form a set of validated, high-impact principles for neural AFP development. 

404 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 7. ACKNOWLEDGMENTS 

This work was supported by the pre-doctoral program AGAUR-FI ajuts (2024 FI-3 00065) Joan Oró, funded by the Secretaria d’Universitats i Recerca of the Departament de Recerca i Universitats of the Generalitat de Catalunya; and by the Cátedras ENIA program “IA y Música: Cátedra en Inteligencia Artificial y Música” (TSI-100929-2023-1), funded by the Secretaría de Estado de Digitalización e Inteligencia Artificial and the European Union – Next Generation EU. 

This work was also part of the project TROBA – Technologies for the recognition of musical works in the era of dynamic generation of audio content (ACE014/20/000051), within the call Nuclis d’R+D 2024, with the support of ACCIÓ (Agency for Business Competitiveness, Government of Catalonia). 

## 8. REFERENCES 

- [1] J. Haitsma, T. Kalker, and J. Oostveen, “Robust audio hashing for content identification,” in Int. Workshop on Content-Based Multimedia Indexing (CBMI), 2001. 

- [2] J. Haitsma and T. Kalker, “A highly robust audio fingerprinting system,” in Proc. of the 3rd Int. Conf. on Music Information Retrieval (ISMIR), 2002. 

- [3] P. Cano, E. Batle, T. Kalker, and J. Haitsma, “A review of algorithms for audio fingerprinting,” in IEEE Workshop on Multimedia Signal Processing (MMSP), 2002. 

- [4] A. Wang, “The Shazam music recognition service,” Communications of the ACM, vol. 49, no. 8, pp. 44– 48, 2006. 

- [5] C. Burges, J. Platt, and S. Jana, “Distortion discriminant analysis for audio fingerprinting,” IEEE Transactions on Speech and Audio Processing, vol. 11, no. 3, pp. 165–174, 2003. 

- [6] G. Cortès, A. Ciurana, E. Molina, M. Miron, O. Meyers, J. Six, and X. Serra, “BAF: An audio fingerprinting dataset for broadcast monitoring,” in Proc. of the 23rd Int. Soc. for Music Information Retrieval Conf. (ISMIR), 2022. 

- [7] B. A. y. Arcas, B. Gfeller, R. Guo, K. Kilgour, S. Kumar, J. Lyon, J. Odell, M. Ritter, D. Roblek, M. Sharifi, and M. Velimirovi´c, “Now Playing: Continuous low-power music recognition,” 2017, arXiv:1711.10958 [cs, eess]. [Online]. Available: http://arxiv.org/abs/1711.10958 

- [8] Z. Yu, X. Du, B. Zhu, and Z. Ma, “Contrastive unsupervised learning for audio fingerprinting,” 2020, arXiv:2010.13540 [cs, eess]. [Online]. Available: http://arxiv.org/abs/2010.13540 

- [9] S. Chang, D. Lee, J. Park, H. Lim, K. Lee, K. Ko, and Y. Han, “Neural audio fingerprint for high-specific audio retrieval based on contrastive learning,” in IEEE 

Int. Conf. on Acoustics, Speech and Signal Processing (ICASSP), 2021. 

- [10] A. Singh, K. Demuynck, and V. Arora, “Attentionbased audio embeddings for query-by-example,” in Proc. of the 23rd Int. Society for Music Information Retrieval Conf. (ISMIR), 2022. 

- [11] A. Bhattacharjee, S. Singh, and E. Benetos, “GraFPrint: A GNN-based approach for audio identification,” in IEEE Int. Conf. on Acoustics, Speech and Signal Processing (ICASSP), 2025. 

- [12] T. Chen, S. Kornblith, M. Norouzi, and G. Hinton, “A simple framework for contrastive learning of visual representations,” in Proc. of the 37th Int. Conf. on Machine Learning (ICML), 2020. 

- [13] J. Serrà, R. O. Araz, D. Bogdanov, and Y. Mitsufuji, “Supervised contrastive learning from weakly-labeled audio segments for musical version matching,” in Proc. of the 42nd Int. Conf. on Machine Learning (ICML), 2025. 

- [14] J. Guinot, E. Quinton, and G. Fazekas, “Semisupervised contrastive learning of musical representations,” in Proc. of the 25th Int. Soc. for Music Information Retrieval Conf. (ISMIR), 2024. 

- [15] F. Schroff, D. Kalenichenko, and J. Philbin, “Facenet: A unified embedding for face recognition and clustering,” in IEEE Conf. on Computer Vision and Pattern Recognition (CVPR), 2015, pp. 815–823. 

- [16] C.-H. Yeh, C.-Y. Hong, Y.-C. Hsu, T.-L. Liu, Y. Chen, and Y. LeCun, “Decoupled contrastive learning,” in Computer Vision – ECCV, 2022. 

- [17] T. Wang and P. Isola, “Understanding contrastive representation learning through alignment and uniformity on the hypersphere,” in Proc. of the 37th Int. Conf. on Machine Learning (ICML), 2020. 

- [18] P. Koromilas, G. Bouritsas, T. Giannakopoulos, M. A. Nicolaou, and Y. Panagakis, “Bridging mini-batch and asymptotic analysis in contrastive learning: From InfoNCE to kernel-based losses,” in Proc. of the 41st Int. Conf. on Machine Learning (ICML), 2024. 

- [19] P. Khosla, P. Teterwak, C. Wang, A. Sarna, Y. Tian, P. Isola, A. Maschinot, C. Liu, and D. Krishnan, “Supervised contrastive learning,” in Proc. of the 34th Int. Conf. on Neural Information Processing Systems (NeurIPS), 2020. 

- [20] Y. Tian, L. Fan, P. Isola, H. Chang, and D. Krishnan, “StableRep: Synthetic images from text-to-image models make strong visual representation learners,” in Proc. of the 37th Int. Conf. on Neural Information Processing Systems (NeurIPS), 2023. 

405 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [21] M. Defferrard, K. Benzi, P. Vandergheynst, and X. Bresson, “FMA: A dataset for music analysis,” in Proc. of the 18th Int. Soc. for Music Information Retrieval Conf. (ISMIR), 2017. 

- [22] A. Mesaros, T. Heittola, and T. Virtanen, “TUT database for acoustic scene classification and sound event detection,” in 24th European Signal Processing Conf. (EUSIPCO), 2016. 

- [23] D. T. Murphy and S. Shelley, “OpenAIR: An Interactive Auralization Web Resource and Database,” in Audio Engineering Society Convention 129, 2010. 

arXiv:2305.09559 [cs, eess]. [Online]. Available: http://arxiv.org/abs/2305.09559 

   - [34] M. Ramona and G. Peeters, “AudioPrint: An efficient audio fingerprint system based on a novel cost-less synchronization scheme,” in IEEE Int. Conf. on Acoustics, Speech and Signal Processing (ICASSP), 2013. 

   - [35] L. L. Beranek, “Concert hall acoustics—1992,” The Journal of the Acoustical Society of America, vol. 92, no. 1, pp. 1–39, 1992. 

- [24] M. Jeub, M. Schäfer, and P. Vary, “A binaural room impulse response database for the evaluation of dereverberation algorithms,” in Proc. of Int. Conf. on Digital Signal Processing (DSP), 2009. 

- [25] J. Traer and J. H. McDermott, “Statistics of natural reverberation enable perceptual separation of sound and space,” Proc. of the National Academy of Sciences, vol. 113, no. 48, pp. E7856–E7865, 2016. 

- [26] J. Franco, B. Bˇacilˇa, T. Brookes, and E. De Sena, “A multi-angle, multi-distance dataset of microphone impulse responses,” Journal of the Audio Engineering Society, 2022. 

- [27] D. Kingma and J. Ba, “Adam: A method for stochastic optimization,” in Proc. of the 3rd Int. Conf. for Learning Representations (ICLR), 2015. 

- [28] Y. You, J. Li, S. Reddi, J. Hseu, S. Kumar, S. Bhojanapalli, X. Song, J. Demmel, K. Keutzer, and C.-J. Hsieh, “Large batch optimization for deep learning: Training BERT in 76 minutes,” in Proc. of the 8th Int. Conf. on Learning Representations (ICLR), 2020. 

- [29] D. S. Park, W. Chan, Y. Zhang, C.-C. Chiu, B. Zoph, E. D. Cubuk, and Q. V. Le, “SpecAugment: A simple data augmentation method for automatic speech recognition,” in 20th Annual Conf. of the Int. Speech Communication Association (INTERSPEECH), 2019. 

- [30] J. Johnson, M. Douze, and H. Jégou, “Billion-scale similarity search with GPUs,” IEEE Transactions on Big Data, vol. 7, no. 3, pp. 535–547, 2019. 

- [31] R. Sonnleitner and G. Widmer, “Robust quad-based audio fingerprinting,” IEEE/ACM Trans. on Audio, Speech, and Language Processing, vol. 24, no. 3, pp. 409–421, 2016. 

- [32] A. Báez-Suárez, N. Shah, J. A. Nolazco-Flores, S.H. S. Huang, O. Gnawali, and W. Shi, “SAMAF: Sequence-to-sequence autoencoder model for audio fingerprinting,” ACM Trans. Multimedia Comput. Commun. Appl., vol. 16, no. 2, pp. 1–23, 2020. 

- [33] A. Agarwaal, P. Kanaujia, S. S. Roy, and S. Ghose, “Robust and lightweight audio fingerprint for automatic content recognition,” 2023, 

406 

