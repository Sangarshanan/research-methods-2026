---
paper_id: "000019"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706357/files/000019.pdf"
---

# AN EVALUATION STRATEGY FOR LOCAL KEY ESTIMATION: EXPLOITING CROSS-VERSION CONSISTENCY 

Yiwei Ding Yannik Venohr Christof Weiß 

Center for Artificial Intelligence and Data Science (CAIDAS), University of Würzburg 

```
{yiwei.ding,yannik.venohr,christof.weiss}@uni-wuerzburg.de
```

## ABSTRACT 

Local key estimation (LKE) is an important yet challenging task in music information retrieval since it involves a high level of musical abstraction, which entails ambiguity and low inter-annotator agreement. Relying on limited (small) datasets with a single annotation may introduce not only dataset bias but also annotator bias. To address such problems, we propose in this paper a novel, annotation-free evaluation strategy for LKE. To this end, we exploit datasets where multiple versions of the same musical work are available. We investigate the models’ consistency across versions, expecting an effective and robust model to output similar predictions on different versions of the same work. In our experiments, we study the behavior of the proposed cross-version consistency measure using examples of different models and datasets, indicating a strong correlation between cross-version consistency and the models’ effectiveness on in-domain data as well as their generalization to out-of-domain data. Our further studies show that, while being correlated to common evaluation metrics, cross-version consistency is also capturing different aspects of model behavior, thus serving as an additional figure of merit for evaluating LKE models. 

## 1. INTRODUCTION 

Harmony analysis of music audio recordings constitutes an essential part of MIR research. A central task in harmony analysis is local key estimation (LKE), which addresses tonal progressions and modulations on a coarse time scale. Unlike global key estimation, where a single key label is assigned to a piece, local key estimation involves first segmenting the audio and then labeling each segment individually. Although we focus on Western classical music with only 24 major and minor keys, LKE still presents several challenges. First, from a music theory perspective, local key can be inherently ambiguous to build up tension and interesting tonalities [1], and the evolution of compositional styles further complicates the search for universal rules. Second, local key is a perceptual notion— 

> 0 © Y. Ding, Y. Venohr, and C. Weiß. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: Y. Ding, Y. Venohr, and C. Weiß, “An Evaluation Strategy for Local Key Estimation: Exploiting Cross-Version Consistency”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 



<!-- Start of picture text -->
30 31 32 33 34<br>A<br>Key Transitions Over Time<br>B:min<br>B:maj<br>E:min<br>Version 1<br>B:min<br> B:maj ?<br>E:min<br>Version 2 30 31 32 33 34 35<br>Time (Measure)<br><!-- End of picture text -->

Figure 1: Example scenario: A model outputs different predictions for two different versions of the same work. 

the short term tonal center implied by a key label is interconnected with expectancy and listening experience, making it a highly abstract musical concept [2]. Third, as a consequence of this inherent ambiguity and perceptual nature, local key labels are often highly subjective [3], i. e., different music theorists may assign different key labels throughout a piece. As a result, local key annotations by a single annotator cannot be fully trusted—a so-called “ground-truth” annotation might not exist for LKE. 

Due to these challenges, evaluating LKE algorithms remains difficult. Common practices of evaluation are based on accuracy or related metrics computed on the test set [4]. However, the lack of multiple annotations for the test data can lead to an annotator-level overfitting, and the lack of large and diverse datasets can result in a dataset-level overfitting. Since creating large-scale datasets with multiple annotators requires music expertise as well as significant human efforts, this strategy does not scale to a desired dataset size. For this reason, we resort to evaluation strategies that require weak or even no annotations, which can be more scalable and less biased towards test set labels as compared to current evaluation metrics. 

Since we focus on Western classical music, where multiple recorded performances (versions) that exactly follow the same musical score (work) are easily available, we propose in this paper to investigate cross-version consistency (CVC) as another evaluation strategy. Ideally, given the same musical content, an effective and robust model should yield the same predictions for different versions . Obviously, this is sometimes not the case, as exemplified in Figure 1. CVC quantifies how robust the models are against such version differences while the musical content stays the same. These version differences usually involve 

158 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

changes in the recording conditions, performers, interpretations, etc. Moreover, measuring the CVC only requires multi-version datasets with pairwise alignment, which are easier to curate than fully-annotated datasets and are independent of local key annotations, thus avoiding the problem of annotator bias. 

As our main contributions in this paper, we (1) propose a framework to analyze the CVC for local key estimation, (2) carefully investigate the relationship between CVC and the common evaluation metrics, and (3) demonstrate that CVC is measuring related yet different aspects of model behavior, thus serving as an additional figure of merit for LKE evaluation. 

The remainder of this paper is structured as follows: In Section 2, we review related work. Section 3 introduces our CVC measure. Section 4 outlines our experimental setup. In Section 5, we present our results by answering and discussing several research questions. In Section 6, we investigate different variants of the CVC that takes music knowledge into account. Section 7 concludes the paper.<sup>1</sup> 

## 2. RELATED WORK 

In this section, we review some of the related work, including evaluation metrics for global and local key estimation, and other works that exploit multi-version datasets. 

## 2.1 Evaluation metrics for key estimation 

For evaluating key estimation systems, most studies consider standard metrics such as the accuracy (or recall rate) and MIREX scores [4]. Accuracy is usually used for global key estimation [5], where one piece is often assigned to a single key label. In LKE, however, there are often segments with labels of “no key”, which typically occurs due to local key ambiguity. To account for these “no key” labels, recall rate is used instead of accuracy where these frames are ignored, and accuracy is only computed over the remaining frames [3,6]. 

Nonetheless, the recall rate ignores the musical relationship between key labels and treats all the errors as the same. As shown in [3, 6], a large fraction of LKE errors corresponds to musically meaningful key relationships such as fifth errors (e. g., `C:maj` – `G:maj` ), parallel errors ( `C:maj` – `C:min` ), and relative errors ( `C:maj` – `A:min` ). To account for this, the MIREX score has been proposed for evaluation in MIREX campaign [7] to go beyond a binary correct-or-wrong evaluation and give partial scores to these musically meaningful errors [8–10]. Specifically, the MIREX score assigns 0.5 points to fifth errors, 0.3 points to relative errors and 0.2 points parallel errors. 

Both recall rate and MIREX score require human annotations. In harmony analysis tasks that can be intrinsically ambiguous, this can lead to an annotator-level overfitting. These problems of annotator subjectivity have been shown for several harmony analysis tasks such as chord recognition [11–13] or LKE [3], where the inter-rater agreement 

> 1 The code is publicly available at: `https://github.com/ suncerock/cvc-lke-ismir25` 

can be as low as 75% . For these reasons, our strategy aims to evaluate LKE models with annotation-free techniques to obtain additional figures of merit. 

## 2.2 Exploiting multi-version datasets 

There have been works that exploits multi-version datasets in different ways. 

First, the multi-version datasets can be used to improve harmony analysis. Konz and Müller [14] and Ewert et al. [15] identify the passages where the chord labels are consistent across different versions and find that these passages are likely to be correctly-predicted. For resolving inconsistent passages, Konz et al. [16] employ cross-version fusion yieliding stabilized analysis results. Second, multi-version datasets facilitate the detailed analysis of LKE results, providing an extra perspective on models’ generalizability. Weiß et al. [3] study different dataset splits and find that for LKE, generalizing to unseen versions is much easier than generalizing to unseen works. Moreover, they perform a cross-annotator study and raise the concern that many LKE models overfit to certain annotators since models’ recall rate can be higher than the rate of inter-rater agreement. 

Third, multi-version datasets can be leveraged for domain adaption, improving models’ effectiveness in another domain. Liu and Weiß [17] utilize cross-version comparison as a consistency regularizer. Here, a model trained in the source domain (piano music) generates the pseudolabels in the target domain (orchestral music) followed by filtering out labels which are inconsistent across versions. Such techniques are shown to generate improved pseudolabels for target domain training. 

Finally, multi-version datasets can also be used for abstract representation learning. Krause et al. [18] employ a contrastive learning paradigm to learn musical features that are invariant under version shifts such as instrumentation and pitch-class activity. 

Since these prior works either take cross-version consistency as a regularization during training or postprocessing, or focus on analyzing the results on a specific (small) dataset, this paper investigates the consistency itself from a more general perspective. More specifically, we propose to use CVC as an evaluation strategy to measure models’ robustness against version changes and analyze several use cases of this strategy for improving LKE. 

## 3. CONSISTENCY MEASURE 

In this section, we introduce our proposed CVC measures. The overall calculation process is illustrated in Figure 2. We use CVC to measure the consistency of a model’s output across different versions of the same work. 

To this end, we first require a set of audio tracks that represent different versions of the same work, and the model’s predictions on these tracks. For instance, we consider a pair of predictions y1, y2 where y1 ∈ R<sup>N×d</sup> and y2 ∈ R<sup>M×d</sup> with N and M representing the number of 

159 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
Pair-wise Sim.<br>Ver. 1 … v1 v2 v3 v4<br>v1 .4 .6 .5<br>Sim. Avg.<br>v2 .8 .9<br>v3 .7<br>Ver. 3 …<br>v4 Avg.<br>Musical Time Cross-version consistency<br><!-- End of picture text -->

Figure 2: Illustration of the consistency measure. 

time frames of the two recordings and d being the dimension of the prediction. In LKE, we assume to have d = 24 local key classes, and each frame of y1 and y2 captures the probability distribution over the 24 classes. 

Next, since different versions of a work usually differ in (local) tempo and length, we need pairwise alignments between them. We compute this alignment using the `synctoolbox` Python package [19], yielding a warping path for each pair of tracks. We denote the warping path between y1 and y2 as P with elements p[l]=(nl, ml), l ∈ [1 : L], meaning that the nl-th frame in y1 and the ml-th frame in y2 refer to the same position in the musical score. 

Then, given a similarity measure s : R<sup>d</sup> × R<sup>d</sup> → R, we compute the consistency C between version 1 and 2 as: 



<!-- Start of picture text -->
L<br>C(y1, y2) = L 1 � s(y1[nl], y2[ml]) .<br>l=1<br><!-- End of picture text -->

Finally, the cross-version consistency (CVC) of one work is defined as the average consistency between all pairs of versions of this work. We aggregate different works by taking the average as well. 

There are various possible choices for the similarity measure. By default, we use a straightforward measure based on the total variation distance (TVD). Given two probability distributions over the 24 local keys p ∈ R<sup>24</sup> and q ∈ R<sup>24</sup> , the TVD-based similarity is computed as: 



<!-- Start of picture text -->
24<br>s(p, q) = 1 − 1 2 � |pi − qi| .<br>i=1<br><!-- End of picture text -->

Since p and q are probability distributions (i. e., sum up to one), s(p, q) ∈ [0, 1], which naturally gives us a normalized consistency measure. We will discuss the effect of alternative similarity measures in Section 6. 

## 4. EXPERIMENTAL SETUP 

In this section, we describe our experimental setups including datasets, models, and training details. 

## 4.1 Datasets 

For our study, we consider three cross-version datasets: Schubert Winterreise Dataset ( `SWD` ) [20], Beethoven Piano Sonata Dataset ( `BPSD` ) [21], and Beethoven String Quartet 

|Dataset|# Movements|# Versions|Dur. (hh:mm)|
|---|---|---|---|
|`SWD`[20]|24|9|10:50|
|`BPSD`[21]|32 <sup>a</sup><br>|11|41:07|
|`BSQD`[22]|70 <sup>b</sup>|9 <sup>c</sup>|62:12|



Table 1:<sup>a</sup> Only the first movements of the 32 sonatas.<sup>b</sup> 16 full string quartets.<sup>c</sup> 7 of them have all the works and 2 of them have only part of the works. 

|Model|# Params.|
|---|---|
|`cqt_cnn`|293k|
|`hcqt_cnn`|294k|
|`octave_lstm`|46k|
|`octavefull_lstm`|150k|
|`chroma`|32k|
|`chroma_res`|200k|



Table 2: Different models used in our experiments. 

Dataset ( `BSQD` )<sup>2</sup> , all of which come with local key annotations. The number of works (i. e., movements) and versions as well as the total duration of these datasets are listed in Table 1. 

Previous works [3] have investigated the effect of different splits of the datasets where training, validation and test data contain the same works but different versions (version split), the same versions but different works (work split), or neither contain the same works nor the same versions (neither split) . In our experiments, we use the neither split for all datasets since it is the most realistic (and difficult) one. 

## 4.2 Models 

While both signal processing-based methods with handcrafted features and deep learning methods have been applied to LKE, deep learning models typically incorporate less music knowledge and are more data-dependent. Therefore, they often suffer more from the ambiguity and subjectivity of LKE than signal processing methods, so we focus on the deep learning methods in this paper. Building on previous work, we include the following models in our study. The first two, `cqt_cnn` and `hcqt_cnn` are VGG-style convolutional neural networks that take a CQT or a harmonic CQT (HCQT, see [23]) as the input, respectively [3]. Further two models, `octave_lstm` and `octavefull_lstm` rely on musically-inspired octavebased rearrangement in the architecture [24] and add bidirectional LSTM layers to model sequential information [6], where `octavefull_lstm` is equivalent to the original model and `octave_lstm` is a reduced one from the ablation study of [6]. The remaining two, `chroma` and `chroma_res` are convolutional networks that are proposed to learn pitch-class (chroma) representations where `chroma_res` adds more layers with residual connections than `chroma` [25]. We adapt these models for LKE by adding a final linear layer to classify the output into 24 local key classes. Table 2 lists these models along with their number of parameters. 

> 2 This dataset will be published soon and comprises multiple versions of all movements from all Beethoven’s string quartets. Local key annotations are derived from the symbolic ABC dataset [22]. 

160 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 4.3 Training details 

We train all our models from scratch using an Adam optimizer for 100 epochs. We set the learning rate as 0.001. To simulate the variance within one run and to obtain models of varying quality, we pick a checkpoint after every 10 epochs during training. To capture the variance due to random initialization, we repeat each training run 5 times, resulting in 10 (checkpoints) times 5 (runs) data points for each model. As a standard metric to compare with our CVC, we compute the key recall rate (accuracy ignoring frames annotated as “no key”), and compare this with other metrics in Section 6. 

## 5. RESEARCH QUESTIONS AND RESULTS 

In this section, we raise several research questions, present our results and discuss these results regarding our RQs. 

RQ1: Is the cross-version consistency correlated with the effectiveness of the model? As mentioned, we expect an effective and robust model both to have high recall and to be consistent across versions. Therefore, we investigate the correlation between recall and CVC on the same set of test data. If they are correlated, we can use CVC as a proxy for models’ effectiveness and compare models on multi-version datasets without annotations. 

For each model on each dataset, we obtain 50 checkpoints as described in Section 4. From each checkpoint, we compute recall and CVC, and then calculate Spearman’s rank correlation coefficient ρ. To see whether such correlation holds across models, we also compute Spearman’s correlation coefficients over all data points, including different models. For better visualization, we also draw the regression lines.<sup>3</sup> 

The results are shown in Figure 3. The x-axes indicate the cross-version consistency, the y-axes indicate the recall, and different colors indicate different models. 

We can see that on all datasets, within each model, there exist strong correlations between recall and CVC. For example, the model `cqt_cnn` (gold circles) obtains a ρ of 0.73, 0.79, and 0.71 on dataset `SWD` , `BPSD` , and `BSQD` , respectively. From all regressions, we obtain p < 0.05, suggesting that for these models, the CVC is correlated with the recall with statistical significance. 

The overall linear regression across all models (black line) shows statistical significance as well. On the three datasets, the regressions show the ρ value of 0.92, 0.89, and 0.88, all with p < 0.001. This means that the correlation between recall and CVC still holds across models, i.e., models with higher consistency have a higher recall. However, it only suggests a correlation on a coarse scale while on a smaller scale, this must be taken with care for some of the model architectures. For example, on both `BPSD` and `BSQD` , `hcqt_cnn` (green triangles) has a slightly higher CVC but a slightly lower recall than `chroma_res` . This might be due to the fact that these two models are based on 

> 3 We also calculated Pearson’s correlation coefficients, but they are omitted because they are close to the Spearman’s correlation coefficients. 



<!-- Start of picture text -->
(a)<br>cqt_cnn (ρ=0.73)<br>0.85 hcqt_cnn (ρ=0.82)<br>octave_Istm (ρ=0.65)<br>octavefull_Istm (ρ=0.50)<br>0.80 chroma (ρ=0.54)<br>chroma_res (ρ=0.43)<br>0.75 All Models (ρ=0.92)<br>0.70<br>Reca l  (SWD)<br>0.65<br>0.60<br>0.60 0.65 0.70 0.75 0.80 0.85 0.90<br>Cross-Version Consistency (SWD)<br>(b)<br>cqt_cnn (ρ=0.79)<br>0.85 hcqt_cnn (ρ=0.81)<br>octave_Istm (ρ=0.75)<br>octavefull_Istm (ρ=0.69)<br>0.80 chroma (ρ=0.74)<br>chroma_res (ρ=0.80)<br>0.75 All Models (ρ=0.89)<br>0.70<br>Reca l  (BPSD)<br>0.65<br>0.60<br>0.60 0.65 0.70 0.75 0.80 0.85 0.90<br>Cross-Version Consistency (BPSD)<br>(c)<br>cqt_cnn (ρ=0.71)<br>0.85 hcqt_cnn (ρ=0.82)<br>octave_Istm (ρ=0.30)<br>octavefull_Istm (ρ=0.37)<br>0.80 chroma (ρ=0.89)<br>chroma_res (ρ=0.88)<br>All Models (ρ=0.88)<br>0.75<br>0.70<br>Reca l  (BSQD)<br>0.65<br>0.60<br>0.60 0.65 0.70 0.75 0.80 0.85 0.90<br>Cross-Version Consistency (BSQD)<br><!-- End of picture text -->

Figure 3: Correlation between recall and cross-version consistency on (a) `SWD` , (b) `BPSD` , and (c) `BSQD` . 

different architectures and therefore imply different inductive biases. 

In conclusion, we see that in general, CVC is strongly correlated to the recall, so we can use cross-version consistency as a proxy for models’ effectiveness. Beyond that, CVC is also capturing different aspects than recall, so when two models obtain similar CVC, the proxy is not able to surely determine which one is better. The model selection process then needs to consider both the effectiveness and the consistency. 

RQ2: Does the correlation between cross-version consistency and recall hold on out-of-domain test data? In RQ1, we compute CVC and recall on the same source 

161 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
(a) BPSD → BSQD<br>0.80 cqt_cnn (ρ=0.67)<br>hcqt_cnn (ρ=0.43)<br>octave_Istm (ρ=0.58)<br>0.75 octavefull_Istm (ρ=0.72)<br>chroma (ρ=0.77)<br>chroma_res (ρ=0.80)<br>0.70 All Models (ρ=0.92)<br>0.65<br>Reca l  (BSQD)<br>0.60<br>0.55<br>0.60 0.65 0.70 0.75 0.80 0.85 0.90<br>Cross-Version Consistency (BSQD)<br>(b) BSQD → BPSD<br>0.80 cqt_cnn (ρ=0.82)<br>hcqt_cnn (ρ=0.83)<br>octave_Istm (ρ=0.40)<br>octavefull_Istm (ρ=0.60)<br>0.75 chroma (ρ=0.94)<br>chroma_res (ρ=0.93)<br>All Models (ρ=0.94)<br>0.70<br>Reca l  (BPSD)<br>0.65<br>0.60<br>0.60 0.65 0.70 0.75 0.80 0.85 0.90<br>Cross-Version Consistency (BPSD)<br><!-- End of picture text -->

Figure 4: Correlation between recall and CVC on models (a) trained on `BPSD` and tested on `BSQD` (b) trained on `BSQD` and tested on `BPSD` . 

datasets as used for training. However, we often want to compare models’ effectiveness on out-of-domain data, i. e., their out-of-domain generalizability. Therefore, we here investigate the models’ generalization to out-of-domain data in relation to their CVC. If they are correlated, we can then compare different models’ effectiveness on outof-domain multi-version datasets by measuring their CVC. 

To this end, we perform a cross-dataset experiment where we train models on one source dataset and compute both recall and CVC on another dataset as a hold-out test set. Note that we adopt a straightforward definition of outof-domain data: data from a different source dataset. In our cases, this means different instrumentation (string instruments in `BSQD` vs. piano in `BPSD` ) or different composers (Schubert in `SWD` vs. Beethoven in `BPSD` and `BSQD` ). 

Figure 4 shows the results. We have the similar observation that within the same model architecture, the checkpoints that are more consistent on the test set have also higher recall. For example, `cqt_cnn` trained on `BPSD` (Figure 4a) shows a ρ of 0.67 when tested on `BSQD` , and switching training and test dataset gives a ρ of 0.82. This means that higher CVC on out-of-domain data also suggests higher recall on that data. 

Comparing different model architectures, we also see that the overall regressions (across all models) yield ρ = 



<!-- Start of picture text -->
(a) BPSD → BSQD<br>0.80 cqt_cnn (ρ=0.52)<br>hcqt_cnn (ρ=0.10)<br>octave_Istm (ρ=-0.08)<br>0.75 octavefull_Istm (ρ=0.49)<br>chroma (ρ=0.68)<br>chroma_res (ρ=0.29)<br>0.70 All Models (ρ=0.29)<br>0.65<br>Reca l  (BSQD)<br>0.60<br>0.55<br>0.65 0.70 0.75 0.80 0.85 0.90<br>Cross-Version Consistency (BPSD)<br>(b) BSQD → BPSD<br>0.80 cqt_cnn (ρ=0.71)<br>hcqt_cnn (ρ=0.78)<br>octave_Istm (ρ=0.27)<br>octavefull_Istm (ρ=0.41)<br>0.75 chroma (ρ=0.90)<br>chroma_res (ρ=0.63)<br>All Models (ρ=0.63)<br>0.70<br>Reca l  (BPSD)<br>0.65<br>0.60<br>0.65 0.70 0.75 0.80 0.85 0.90<br>Cross-Version Consistency (BSQD)<br><!-- End of picture text -->

Figure 5: Correlation between recall and CVC on models (a) trained on `BPSD` and tested on `BSQD` (b) trained on `BSQD` and tested on `BPSD` . Note that CVC is computed on the unseen test partition of the training dataset. 

0.92 and 0.94, respectively. This indicates that, on a coarse scale, more consistent models are also more effective on these unseen out-of-domain data. From this observation, we conclude that CVC enables us to evaluate a model’s generalizability on an out-of-domain multi-version test set without requiring labels. 

RQ3: Is in-domain cross-version consistency correlated with effectiveness on out-of-domain data? To address RQ2, we computed both CVC and recall on the same test set, which requires the test dataset (target domain) to include multiple versions. However, in practice, we often want to estimate model robustness without such dedicated cross-version datasets. To address this, here in RQ3, we investigate whether CVC in the training (source) domain can be used as a proxy for models’ effectiveness on the target domain, i. e., its capability of domain generalization. To this end, we compute the CVC on the in-domain test data (using a neither split) and the recall rate on out-of-domain test data. 

Figure 5 shows the results. While in some modelspecific and dataset-specific cases, the correlation within one model does not always hold, across different models (black lines), the observations stay similar. These overall 

162 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

regressions show ρ of 0.29 and 0.63, respectively, with all p < 0.001, indicating statistical significance. This means that, on a coarse scale, consistent models in general obtain higher recall than inconsistent ones. This allows us to compare the generalizability of different models: If a model is significantly more consistent on our in-domain cross-version test set, it is very likely to be more robust against domain shifts such as instrumentation changes. 

Given these results, we want to emphasize that models with higher recall on a single in-domain test set are not necessarily more generalizable, which is a typical case of dataset bias. If we compare Figure 3b with Figure 5b, we see that `cqt_cnn` obtains lower recall but slightly higher CVC than `chroma_res` when tested on the in-domain test set `BSQD` but shows higher recall on out-of-domain test set `BPSD` . We conclude that CVC can serve as a complement to the traditional evaluation metrics, indicating the generalizability of the model, even if we neither have labels nor multi-version data in the target domain at hand. 

## 6. TOWARDS INCLUDING MUSIC KNOWLEDGE 

In the previous section, we chose recall as a representative for common evaluation metrics, and used the straightforward TVD-based similarity to compute the cross-version consistency. In this section, we investigate the effect of using other evaluation metrics and consistency measures that take music konwledge into account. 

As mentioned in Section 2, accuracy or recall ignore the musical relationship between different key labels and are therefore not able to account for the different types of errors. In MIREX, researchers have proposed another evaluation metric for key estimation. This MIREX score partially rewards musically meaningful errors including fifth error, parallel error, and relative error (see Section 2.1). 

As an alternative to TVD, we also consider a musically motivated similarity measure. To this end, we arrange a model’s output distribution according to the circle of fifths, placing relative keys next to each other in thirds (e. g., `A:min` between `C:maj` and `F:maj` ). On this geometric key distribution, we compute the Earth Mover’s Distance (EMD), which quantifies the cost of turning one probability distribution into another by moving probability mass the shortest direction along the circle. The circle-offifths arrangement thereby demands for a circular version of the EMD [26]. In [27], a similar measure was applied to compare diatonic scale probabilities, which are closely related to local keys. For example, moving from `C:maj` to `G:maj` costs the same as to `F:maj` and costs less than to `D:maj` , due to the fifth relationship. 

We now want to mutually compare the resulting metrics. To this end, we use the experimental setup of RQ1 in Section 5 and calculate the pairwise Spearman correlation coefficients between recall, MIREX score, TVD-based consistency, and EMD-based consistency. The results are shown in Figure 6, where CVC_TVD and CVC_EMD indicate the consistencies based on TVD and EMD, respectively. We show only the results on `SWD` ; results on other datasets are similar. 



<!-- Start of picture text -->
(a) hcqt_cnn 1.0<br>Recall - 0.91 0.81 0.57<br>-0.8<br>MIREX 0.91 0.76 0.59 0.6<br>CVC_TVD 0.81 0.76 0.76 -0.4<br>-0.2<br>CVC_EMD 0.57 0.59 0.76<br>-0.0<br>Recall MIREX CVC_TVD CVC_EMD<br>(b) octavefull_Istm<br>1.0<br>Recall - 0.99 0.55 0.58<br>0.8<br>MIREX 0.99 0.53 0.56 0.6<br>CVC_TVD 0.55 0.53 0.97 0.4<br>-0.2<br>CVC_EMD 0.58 0.56 0.97<br>-0.0<br>Recall MIREX CVC_TVD CVC_EMD<br>(c) chroma_res 1.0<br>Recall - 0.94 0.47 0.29<br>-0.8<br>MIREX 0.94 0.49 0.39 -0.6<br>CVC_TVD 0.47 0.49 0.79 0.4<br>-0.2<br>CVC_EMD 0.29 0.39 0.79<br>- 0.0<br>Recall MIREX CVC_TVD CVC_EMD<br>Figure 6: Pairwise correlation between recall,<br>MIREX, CVC_TVD and CVC_EMD, computed with<br>(a) hcqt_cnn (b) octavefull_lstm and (c)<br>chroma_res  both trained and tested on  SWD .<br><!-- End of picture text -->

We can see that the correlations between recall and MIREX score are 0.91, 0.99, and 0.94, respectively, indicating a high correlation. Also, CVC_TVD has a rather high correlation with CVC_EMD, with correlation of 0.76, 0.97, and 0.79, respectively. The group of the two standard metrics and the group of the two consistencies still shows correlation, with coefficients of 0.6–0.8 for `hcqt_cnn` and around 0.4–0.5 for `octavefull_lstm` and `chroma_res` . This means that our conclusion from the previous section can be extended to other metrics and consistency measures. In comparison, however, the correlation between these two groups are clearly weaker than the correlation within each groups. This observation suggests that our proposed cross-version consistency is not measuring exactly the same thing as recall rate or MIREX score, but is rather capturing related yet different perspectives, thus serving as a novel figure of merit for LKE evaluation. 

## 7. CONCLUSION 

In this paper, we propose to investigate the cross-version consistency of LKE models as a new strategy for evaluation. We show that CVC is strongly correlated with models’ effectiveness and generalizability to out-of-domain data, while requiring no tedious human annotations but only aligned version pairs. Therefore, we can compare different LKE models with more diverse multi-version datasets without labels, reducing the risk of dataset bias and annotator bias. Note that we do not undermine the importance and necessity of common evaluation metrics, but CVC serves as a good complement, evaluating LKE models from different perspectives. 

163 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 8. ACKNOWLEDGEMENTS 

This work was funded by the German Research Foundation (Deutsche Forschungsgemeinschaft, DFG) within the Emmy Noether Junior Research Group on Computational Analysis of Music Audio Recordings: A Cross-Version Approach (DFG WE 6611/3-1, Grant No. 531250483). 

## 9. REFERENCES 

- [1] M. Roig-Francolí, Harmony in Context. New York: McGraw-Hill, 2011. 

- [2] S. Hallam, I. Cross, and M. Thaut, Oxford handbook of music psychology. Oxford University Press, 2009. 

- [3] C. Weiß, H. Schreiber, and M. Müller, “Local key estimation in music recordings: A case study across songs, versions, and annotators,” IEEE/ACM Transactions on Audio, Speech, and Language Processing (TASLP), vol. 28, pp. 2919–2932, 2020. 

- [4] C. Raffel, B. McFee, E. J. Humphrey, J. Salamon, O. Nieto, D. Liang, D. P. Ellis, and C. C. Raffel, “MIR_EVAL: A transparent implementation of common mir metrics,” in Proceedings of the International Society for Music Information Retrieval Conference (ISMIR), 2014. 

- [5] Y. Kong, V. Lostanlen, G. Meseguer-Brocal, S. Wong, M. Lagrange, and R. Hennequin, “STONE: selfsupervised tonality estimator,” in Proceedings of the International Society for Music Information Retrieval Conference (ISMIR), 2024, pp. 954–961. 

- [6] Y. Ding and C. Weiß, “Towards robust local key estimation with a musically inspired neural network,” in Proceedings of the European Signal Processing Conference (EUSIPCO), 2024, pp. 26–30. 

- [7] J. S. Downie, “The music information retrieval evaluation exchange (2005–2007): A window into music information retrieval research,” Acoustical Science and Technology, vol. 29, no. 4, pp. 247–255, 2008. 

- [8] H. Papadopoulos and G. Peeters, “Local key estimation from an audio signal relying on harmonic and metrical structures,” IEEE Transactions on Audio, Speech, and Language Processing (TASLP), vol. 20, no. 4, pp. 1297–1312, 2011. 

- [9] F. Korzeniowski and G. Widmer, “End-to-end musical key estimation using a convolutional neural network,” in Proceedings of the European Signal Processing Conference (EUSIPCO), 2017, pp. 966–970. 

- [10] ——, “Genre-agnostic key classification with convolutional neural networks,” in Proceedings of the International Society for Music Information Retrieval Conference (ISMIR), 2018, pp. 264–270. 

- [11] A. Laaksonen, “Ambiguity in automatic chord transcription: recognizing major and minor chords,” in Adaptive Multimedia Retrieval: Semantics, Context, and Adaptation (AMR), 2014, pp. 203–213. 

- [12] Y. Ni, M. McVicar, R. Santos-Rodriguez, and T. De Bie, “Understanding effects of subjectivity in measuring chord estimation accuracy,” IEEE Transactions on Audio, Speech, and Language Processing (TASLP), vol. 21, no. 12, pp. 2607–2615, 2013. 

- [13] H. V. Koops, W. B. De Haas, J. A. Burgoyne, J. Bransen, A. Kent-Muller, and A. Volk, “Annotator subjectivity in harmony annotations of popular music,” Journal of New Music Research (JNMR), vol. 48, no. 3, pp. 232–252, 2019. 

- [14] V. Konz and M. Müller, “A cross-version approach for harmonic analysis of music recordings,” in Multimodal Music Processing, ser. Dagstuhl FollowUps. Dagstuhl, Germany: Schloss Dagstuhl–LeibnizZentrum für Informatik, 2012, vol. 3, pp. 53–72. 

- [15] S. Ewert, M. Müller, V. Konz, D. Müllensiefen, and G. A. Wiggins, “Towards cross-version harmonic analysis of music,” IEEE Transactions on Multimedia, vol. 14, no. 3-2, pp. 770–782, 2012. 

- [16] V. Konz, M. Müller, and R. Kleinertz, “A crossversion chord labelling approach for exploring harmonic structures—a case study on Beethoven’s Appassionata,” Journal of New Music Research, vol. 42, no. 1, pp. 61–77, 2013. 

- [17] L. Liu and C. Weiß, “Utilizing cross-version consistency for domain adaptation: A case study on music audio,” in International Conference on Learning Representations (ICLR), Tiny Papers, 2024. 

- [18] M. Krause, C. Weiß, and M. Müller, “A cross-version approach to audio representation learning for orchestral music.” in Proceedings of the International Society for Music Information Retrieval Conference (ISMIR), 2023, pp. 832–839. 

- [19] M. Müller, Y. Özer, M. Krause, T. Prätzlich, and J. Driedger, “Sync toolbox: A python package for efficient, robust, and accurate music synchronization,” Journal of Open Source Software, vol. 6, no. 64, p. 3434, 2021. 

- [20] C. Weiß, F. Zalkow, V. Arifi-Müller, M. Müller, H. V. Koops, A. Volk, and H. G. Grohganz, “Schubert Winterreise dataset: A multimodal scenario for music analysis,” ACM Journal on Computing and Cultural Heritage, vol. 14, no. 2, pp. 25:1–18, 2021. 

- [21] J. Zeitler, C. Weiß, V. Arifi-Müller, and M. Müller, “BPSD: A coherent multi-version dataset for analyzing the first movements of Beethoven’s piano sonatas,” Transactions of the International Society for Music Information Retrieval, vol. 7, no. 1, pp. 195–212, 2024. 

164 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [22] M. Neuwirth, D. Harasim, F. C. Moss, and M. Rohrmeier, “The annotated beethoven corpus (abc): A dataset of harmonic analyses of all beethoven string quartets,” Frontiers in Digital Humanities, vol. 5, p. 16, 2018. 

- [23] R. M. Bittner, B. McFee, J. Salamon, P. Li, and J. P. Bello, “Deep salience representations for F0 tracking in polyphonic music,” in Proceedings of the International Society for Music Information Retrieval Conference (ISMIR), Suzhou, China, 2017, pp. 63–70. 

- [24] A. Elowsson and A. Friberg, “Modeling music modality with a key-class invariant pitch chroma CNN,” in Proceedings of the International Society for Music Information Retrieval Conference (ISMIR), Delft, The Netherlands, 2019, pp. 541–548. 

- [25] C. Weiss, J. Zeitler, T. Zunner, F. Schuberth, and M. Müller, “Learning pitch-class representations from score-audio pairs of classical music,” in Proceedings of the International Society for Music Information Retrieval Conference (ISMIR), 2021, pp. 746–753. 

- [26] J. Rabin, J. Delon, and Y. Gousseau, “Circular Earth Mover’s Distance for the comparison of local features,” in Proceedings of the International Conference on Pattern Recognition (ICPR), Tampa, USA, 2008. 

- [27] C. Weiß and M. Müller, “From music scores to audio recordings: Deep pitch-class representations for measuring tonal structures,” ACM Journal on Computing and Cultural Heritage (JOCCH), vol. 17, no. 3, pp. 45:1–19, 2024. 

165 

