---
paper_id: "000031"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706389/files/000031.pdf"
---

# TOWARDS ROBUST MUSIC TRANSCRIPTION BY MEASURING CROSS-VERSION CONSISTENCY IN WESTERN CLASSICAL MUSIC 

Yannik Venohr 

Yiwei Ding Christof Weiß 

Center for Artificial Intelligence and Data Science, University of Würzburg 

```
{yannik.venohr,yiwei.ding,christof.weiss}@uni-wuerzburg.de
```

## ABSTRACT 

Automatic Music Transcription (AMT) is a central task within MIR, enabling various subsequent applications. Despite advancements thanks to deep learning, improving AMT remains challenging due to the scarcity of large, high-quality annotated datasets. Recognizing pitches in multi-instrument settings beyond solo piano is particularly difficult, as models struggle to generalize across domains due to dataset biases and overfitting. AMT research appears to have hit a glass ceiling, where further progress is difficult to achieve and to measure. To address this, we propose cross-version consistency (CVC)—an annotationfree evaluation framework that measures a model’s transcription consistency across different recordings of the same musical work. We formalize this concept and systematically analyze its relationship with standard evaluation metrics on the AMT subtask of multi-pitch estimation. Our results show that CVC is closely tied to standard evaluation metrics and enables model assessment using only unlabeled multi-version datasets, making it particularly valuable in domains where annotated data is scarce but multiversion recordings are easy to obtain, such as orchestral music. Beyond this, we argue that CVC is, by design, a desirable property for transcription models and our results indicate that it can provide insights into a model’s robustness, i. e., its ability to generalize to out-of-domain data. 

## 1. INTRODUCTION 

Automatic Music Transcription (AMT) aims to convert music recordings into some form of music notation, making it a powerful tool for various applications [1]. In musicology, AMT can help to analyze large collections of recorded music, including improvised performances or orally transmitted pieces, revealing patterns that might otherwise remain inaccessible [2,3]. AMT also supports music education by providing automatic transcriptions to help with learning and practice. Ultimately, an AMT system aims towards generating a human-readable score. How- 

> Cf © Yannik Venohr, Yiwei Ding and Christof Weiß. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: Yannik Venohr, Yiwei Ding and Christof Weiß, “Towards Robust Music Transcription by Measuring Cross-Version Consistency in Western Classical Music”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 



<!-- Start of picture text -->
fθ<br>Version 1: SC06<br>Work: SWD - Gute Nacht X1<br>62<br>DTW Warping Path Similar?<br>9 Version 2: AL98<br>P2<br><!-- End of picture text -->

Figure 1: Cross-version consistency. We compare predictions Y<sup>ˆ</sup> 1, Y<sup>ˆ</sup> 2 from a model fθ across two different recordings X1, X2 of the same work at musically corresponding positions. 

ever, this goal is commonly addressed through intermediate steps with increasing levels of abstraction. These steps include frame-level, note-level, stream-level, and notationlevel transcription as defined in [1]. 

While transcription models have shown good results in piano-only scenarios [4, 5, 6], recognizing pitches in a multi-instrument scenario beyond solo piano remains a significant challenge [1]. Recently, using large-scale Transformer architectures, some significant progress has been made for stream-level transcription [7,8]. However, when tested on unseen datasets, these models show a drastic drop in efficacy [8]. Similarly, for frame-level transcription, Weiß and Peeters [9] found that variations between architectures are often smaller than variations across training runs and even become irrelevant in cross-dataset evaluations. This highlights the long-standing problem that deep learning models tend to overfit to inherent dataset biases rather than generalizing effectively [10]. For AMT models to be practically useful for musicology, they must be robust and able to generalize to out-of-domain data. 

A major challenge is the scarcity of large, unbiased, and high-quality annotated datasets. Inspired by advances in other modalities like text and images, a natural next step is to find ways to leverage unlabeled data. Early efforts in this direction include self-supervised learning approaches, such as learning from equivariance under pitch transposi- 

271 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

tion [11]. However, even with improved models, the challenge of measuring progress with a limited amount of reliable test data remains unresolved. 

Inspired by previous work [12, 13, 14], we propose to address this challenge by exploiting multi-version datasets of Western classical music. These datasets contain several versions (recorded performances) of the same musical work—possibly by different musicians, on different instruments, and in different recording conditions—all closely following the same score. Thus, we obtain different audio signals that carry the same musical content. This provides an opportunity to evaluate transcription models beyond standard evaluation metrics. As our main contribution, we formalize and systematically test the notion of Cross-Version Consistency (CVC). We consider a model to have a high CVC, if it makes similar predictions at musically corresponding positions, regardless of performer or recording conditions (Figure 1). As this measure does not depend on annotations, it enables us to evaluate models even in domains, where annotated data is scarce or unavailable. Moreover, as it implicitly captures when and which transcription errors occur rather than just how many, it may serve as a useful additional figure of merit for evaluating transcription models. While this paper aims to providing insights for the broader field of AMT, the experiments in this paper focus on the subtask of frame-level transcription, also known as Multi-Pitch Estimation (MPE). Our main contributions are (1) proposing and formalizing CVC, (2) designing experiments to systematically examine its relationship with standard evaluation metrics and (3) showing that CVC is closely tied to both transcription capabilities and a model’s ability to generalize to different domains. 

The remainder of the paper is organized as follow: Section 2 reviews related work. Section 3 formalizes CVC. Section 4 presents our experimental setup. Section 5 presents results and discusses our findings. Section 6 concludes the paper. 

## 2. RELATED WORK 

AMT has been an active research area for nearly five decades [1]. Given the extensive body of work in this field, we refer to [1] for a comprehensive overview. Most stateof-the-art AMT approaches rely on deep learning with supervised training [4, 5, 6, 15, 16, 9, 7, 8], where models are trained on datasets of music recordings with aligned pitch annotations. Even though these approaches have been successful in certain domains, two key challenges remain: (1) compared to traditional signal processing techniques, deep learning models often struggle to generalize across different domains [1] and, (2) in many domains such as choir or orchestral music, annotated datasets are scarce, limiting the effectiveness of supervised learning. 

Exploiting multi-version datasets, for both training and evaluation, has emerged as a strategy to address these challenges. Weiß et al. [12, 9] leveraged multi-version datasets for evaluation, studying generalization across versions and analyzing the impact of different splitting strategies. Krause et al. [13, 17] explored training strategies 

using multi-version data. One approach employs contrastive learning, treating temporally close audio segments across versions as positive pairs and distant segments as negative pairs [17]. However, their findings suggest that the resulting representations capture instrument texture rather than pitch classes and harmonies. Another approach minimizes the distance between time–frequency representations of different versions of the same work [13], demonstrating promising MPE results. Liu and Weiß [14] used multi-version datasets for domain adaptation within a teacher–student learning paradigm. They use a notion of CVC to filter training labels by comparing teacher annotations across versions and retaining only matching annotations for student training. In contrast to [14], where CVC is considered as a filter on binary outputs, we define it as a measure on the probabilities. Moreover, we consider a larger picture, formalize and systematically explore CVC. 

## 3. CROSS-VERSION CONSISTENCY 

In this paper, we focus on MPE, aiming to train a neural network fθ to estimate pitch probabilities from audio. Specifically, a model produces a sequence of pitch probability vectors Y<sup>ˆ</sup> = (ˆy(0), . . . , ˆy(T )), where each vector yˆ(t) ∈ [0, 1]<sup>72</sup> represents the probability of pitches being active at time frame t. We consider a model to have a high CVC, if it makes similar predictions at musically corresponding positions, regardless of differences in performer and recording conditions. 

## 3.1 Alignment via Dynamic Time Warping 

As a peculiarity of Western classical music, different versions of a work exactly follow the same score regarding pitch and note information, but are quite free in regards to global and local tempo (including fluctuations such as agogics, ritardando, or rubato). To identify musically corresponding positions despite these tempo variations, we rely on Dynamic Time Warping (DTW) [18], a well-established method for aligning time-series data. DTW yields a warping path between two sequences with lengths N and M denoted as P = (p(1), . . . , p(L)) with 



<!-- Start of picture text -->
p(l) = (nl, ml) ∈ [1 : N ] × [1 : M ].<br><!-- End of picture text -->

This warping path establishes correspondences between time frames of the two sequences, enabling us to align musical positions despite tempo variations (see Figure 1 in blue). Notably, although DTW is computed using audio feature sequences, it can also be applied to align predictions, since we use the same feature rate for both. 

## 3.2 Cross-Version Consistency 

Given two audio signals X1 and X2 and their respective pitch predictions Y<sup>ˆ</sup> 1 = fθ(X1) ∈ R<sup>N×72</sup> and Y<sup>ˆ</sup> 2 = fθ(X2) ∈ R<sup>M×72</sup> , we compute the similarity between aligned frames along the warping path. For the l-th element p(l) in the warping path P , we define the frame-level 

272 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

similarity using a suitable similarity measure (e.g., cosine similarity) as 

|Ref.|Name|Intr.|hh:mm|W ×V|
|---|---|---|---|---|
|[19]|`SWD`|Piano, Singing|10:49|24×9|
|[20]|`BPSD`|Piano|41:08|32<sup>a </sup>×11<br>|
|t.b.p.|`BSQD`|Strings|62:12|70<sup>b </sup>×9|
|[21]|`RWC-C`|Mixed|5:21|35×1|
|[22]|`TRIOS`|Mixed|0:03|5×1|





<!-- Start of picture text -->
s(l) = cossim( Y ˆ 1(nl), Y ˆ 2(ml)) ∈ [0, 1].<br><!-- End of picture text -->

Since some versions may be performed in different keys, we transpose Y<sup>ˆ</sup> accordingly before computing the similarity. For a given model fθ and two recordings X1 and X2 of the same musical work, we define CVC as the average frame-level similarity across the aligned frames: 

Table 1: Datasets used in this paper. W : Number of unique works. V : Number of unique versions.<sup>a</sup> The first movements of the 32 sonatas.<sup>b</sup> 16 full string quartets. 

|L|Ref.|Architecture|Parameters|
|---|---|---|---|
|CVC(fθ, X1, X2) = <sup>1</sup><br>L<br><br>�<br><br>s(l).|[16]<br>[15]|`Basic Pitch`<br>`Deep Salience`|13,320<br>406,453|
|l=1|[9]|`ResNet-S`|393,535|
|i|[9]|`ResNet-M`|1,512,783|
|n set of recordings D, we define CVC to be|[9]|`ResNet-L`|4,555,683|



For a given set of recordings D, we define CVC to be computed for all pairwise combinations of different versions of each work and averaged over works. By design, this measure assesses a model’s robustness against variations in performer and recording conditions. We argue that being consistent across differing conditions is particularly desirable for applications like corpus analysis. Moreover, as it implicitly captures when and which transcription errors occur rather than just how many, it offers a complementary perspective to standard evaluation metrics. While, by definition, a model making constant but incorrect predictions (e.g., predicting the same pitch for every frame) will yield a high CVC score, we note that this does not invalidate the metric since we consider CVC as an additional figure of merit rather than a standalone quality indicator. 

Table 2: Model architectures used in this paper. Each model is based closely on the referenced work, though minor differences may exist due to reimplementation (e.g., slight variations in parameter counts). 

exclusively for testing. To ensure they represent outof-domain data, we exclude pieces with instrumentations matching our three multi-version datasets, leaving 35 of the 50 pieces in `RWC` . Table 1 provides an overview. 

## 4.2 Models 

In this paper, we focus on demonstrating the potential of CVC as a measure for evaluating MPE models. Rather than proposing complex network architectures or conducting extensive hyperparameter tuning, we aim to assess a range of commonly used architectures. We implement five fully convolutional deep learning models that are closely inspired by prior work, making minimal adjustments to fit our training framework. The smallest model is based on the note activation component of the Notes and Multipitch (NMP)<sup>2</sup> model [16] adjusted to work with fewer harmonics, which we will refer to as `Basic Pitch` . Another model builds upon the `Deep Salience` network [15], with an additional layer to quantize outputs into semitone bins. Lastly, we use three different sizes of a deep convolutional network with additional residual connections ( `ResNet` ), as described in [9]. In Table 2, we show model sizes ranging from 13 thousand to 4,5 million parameters. 

## 4. EXPERIMENTAL SETUP 

To study our proposed consistency measure, we conduct a series of experiments on the relationship of CVC on multiversion datasets and common evaluation metrics on labeled test sets. 

## 4.1 Datasets and Splits 

In the center of all our experiments are three structured multi-version datasets: Schubert Winterreise Dataset ( `SWD` ) [19], Beethoven Piano Sonata Dataset ( `BPSD` ) [20], and Beethoven String Quartet Dataset ( `BSQD` ) [to be published soon<sup>1</sup> ]. Since these datasets are used for training and for evaluation, we split them into subsets. To avoid overfitting to specific recording conditions (“version effect”, [9]) or melodic/harmonic patterns in a work (“cover song effect”, [9]), we ensure that models are neither trained on the same versions nor works they are tested on and always use a strict “neither split”. (see Fig. 4 in [12]). 

## 4.3 Implementation Details 

All models are trained from scratch using the Adam optimizer for 50 epochs, with binary cross-entropy as the loss function. We set the learning rate to 0.0005. The input to all models is a Harmonic Constant-Q Transform (HCQT) [15] with five harmonics and one subharmonic spanning six octaves (C1–C7) with three bins per semitone, resulting in 216 pitch bins. We use a sample rate of 22.05 kHz and an HCQT hop size of 512 samples, yielding a frame rate of approximately 43 Hz. We process sequences of 64 

For our studies on generalization, we use two further high-quality datasets as unseen test sets: the classical subset of the Real World Computing Music Database ( `RWC` ) [21] and `TRIOS` [22]. These datasets, which include orchestral, horn, flute, cembalo, and organ pieces, are used 

> 1 A multi-version dataset comprising 6-7 Versions of L. v. Beethovens complete string quartets with annotations derived from symbolic ABC Corpus [3]. 

> 2 Please note that in [16], “note” refers to quantized pitch on a semitone axis, in contrast to sub-semitone pitch contours. 

273 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

frames (roughly 1.5 seconds of audio) in mini-batches of 128 samples. To mitigate and analyze the impact of randomness [9], we repeat training three times using different seeds. For each training run, we save and evaluate checkpoints after every five epochs. DTW is computed using the SyncToolbox [23] implementation of memory-restricted multi-scale DTW (MrMsDTW) [24] using chroma and onset features at a frame rate of approximately 43 Hz. For further details refer to the source code<sup>3</sup> . 

## 5. RESULTS 

Our experiments for testing and understanding CVC are driven by two Research Questions (RQ). 

RQ 1: Can CVC serve as a proxy for model efficacy within one domain? For example, does a model that obtains higher CVC on `SWD` also show higher efficacy on `SWD` . To study this, we test whether CVC correlates with standard evaluation metrics on the three multi-version datasets. 

RQ 2: Beyond this, does CVC provide insight into model robustness—the ability to generalize to out-ofdomain-data? Here we are particularly interested in cases, where our consistency measure might be complementary to common evaluation metrics. To test this, we investigate whether CVC on the multi-version datasets correlates with standard evaluation metrics on the two unseen out-ofdomain datasets. 

To test for correlation, we report Spearman’s rank correlation coefficient (ρ). For visualization purposes, we overlay a linear regression line on the plots. 

## 5.1 Proxy for Efficacy Within One Domain 

To address the first research question and determine whether CVC can serve as a proxy for efficacy within a domain, we train multiple models fθ, systematically varying either their architecture or training data, and compare their CVC scores with their Average Precision (AP) scores. 

Amount of Training Data: In the first experiment, we vary the amount of training data. We use a mixed train set ( `SWD+BPSD+BSQD` ) as a pool and train the `ResNet-M` architecture on increasing fractions of this pool, ranging from 10% to 20% up to the full dataset. Figure 2 shows one plot for each of the three multi-version test sets. To simulate models of different quality, we evaluate multiple checkpoints for each run. Each marker represents a checkpoint of a model, with the color indicating the amount of training data the model has seen. The x-axis reports CVC, while the y-axis reports the AP—both computed on the respective test set. 

As expected, increasing the amount of training data generally leads to higher AP scores. However, due to the inherent randomness of deep learning, small increases in data size do not always result in higher AP. More importantly, looking at the figures and the high correlation coefficients, we can observe a clear correlation between CVC and AP on all three test sets. This suggests its potential as 

> 3 https://github.com/yannik-venohr/ismir25-cvc-for-mpe 



<!-- Start of picture text -->
(a) Test set: SWD<br>90<br>Spearman's ρ: 0.97<br>85<br>80<br>Precision75<br>70<br>Average 165<br>60<br>55<br>(b) Test set: BPSD<br>90 Spearman's ρ : 0.77<br>85<br>80<br>75<br>70<br>65<br>Average Precision<br>60<br>55<br>(c) Test set: BSQD<br>90 Spearman's ρ : 0.93<br>85<br>80<br>70 88<br>65<br>Average Precision<br>60<br>55<br>0.70 0.75 0.80 0.85<br>Cross-Version Consistency<br>Fraction of data used for training (%)<br>10 ● 30 50 70 90<br>20 40 60 80 100<br><!-- End of picture text -->

Figure 2: Varying the amount of training data. CVC vs. AP—both computed on the respective test set—for `ResNet-M` trained on increasing fractions of `SWD+BPSD+BSQD` . 

a proxy for model efficacy within one domain. The correlation is slightly weaker for BPSD, possibly due to its smaller AP range (≈ 15% vs. ≈ 30% in other datasets) where effects of randomness become more relevant. 

Domain of Training Data: In this next experiment, we explore models trained on different datasets. For this we train `ResNet-M` on all possible combinations of the three multi-version datasets. Compared to the previous experiment, this can be seen as a more drastic variation, as we not only vary the amount, but also the instrumentation a model has seen during training. As with the previous experiment, we compute CVC and AP on the test sets of the three multi-version datasets. Results are shown in Figure 3. First of all, we see strong differences between the three test sets. When testing within the domain of `SWD` (Figure 3a), we see a strong correlation (ρ = .92) between CVC 

274 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
(a) Test set: SWD<br>90<br>Spearman's ρ : 0.92<br>80<br>70<br>60<br>Average Precision<br>50<br>(b) Test set: BPSD<br>06<br>Spearman's ρ : 0.38<br>80<br>70<br>60<br>Average Precision<br>50<br>(c) Test set: BSQD<br>90<br>Spearman's ρ : 0.75<br>80<br>70<br>60 x<br>Average Precision<br>50<br>0.75 0.80 0.85 090<br>Cross-Version Consistency<br>Training data<br>SWD SWD+BPSD BPSD+BSQD<br>X BPSD SWD+BSQD SWD+BPSD+BSQD<br>BSQD<br><!-- End of picture text -->

Figure 3: Varying the training domain. CVC vs. AP— both computed on the respective test set—for `ResNet-M` trained on combinations of `SWD, BPSD` and `BSQD` . 

and AP. When testing in the string quartet domain ( `BSQD` , Figure 3c), we observe a first case where models have a lower AP but a higher CVC, with `SWD` in dark blue and `BPSD` in yellow, while still maintaining a strong correlation overall (ρ = .75). In contrast to this is the domain of `BPSD` (Figure 3b), where we only observe a weak correlation (ρ ≈ .38). In the center of the plot, there seems to be a correlation on a smaller scale between the models that have seen examples of `BPSD` during training. However, the models trained on `SWD` , `BSQD` , and `SWD+BSQD` all show low AP, but still comparable CVC. The models trained on `BSQD` show a particularly low AP, while having a CVC comparable to all other models. Upon examining predictions of these models more closely, we observed that they consistently miss pitches in the higher registers. While this obviously makes this a not very useful model, one could argue that making mistakes regardless of performer and recording conditions is a desired property for corpus stud- 



<!-- Start of picture text -->
Spearman's ρ : 0.61<br>82<br>80<br>78<br>76<br>Architecture<br>Basic Pitch<br>74 Deep Salience<br>Average Prec i son (Combined) ResNet-S<br>72 ResNet-M<br>ResNet-L<br>0.79 0.80 0.81 0.82 0.83 0.84 0.85 0.86<br>Cross-Version Consistency (Combined)<br><!-- End of picture text -->

Figure 4: Varying model architecture. CVC vs. AP—both computed on all three multi-version datasets—for different architectures trained on `SWD+BPSD+BSQD` . 

ies. Let us take a closer look at another example. The models trained on `BPSD` (yellow) have a higher AP, but a lower CVC than the models trained `SWD+BSQD` (light blue). We expect a higher AP, since it has been trained in the domain where it is tested, but CVC does not seem to reflect this. We will further discuss this example in Section 5.2. 

Model Architecture: In this experiment, we compare different model architectures while keeping the training data constant ( `SWD+BPSD+BSQD` ). Figure 4 shows the results, where colors indicate the trained architecture. Since the trends were similar across the three multi-version datasets, we combined the results of the three test domains by averaging them. Each dataset is weighted equally, regardless of its size. As expected, models with higher capacity tend to achieve higher AP. More importantly, we see that even in this experiment, we find a correlation between CVC and AP (ρ = .61), even though it is slightly weaker. Notably, compared to the previous experiment, the range of AP is relatively small (≈ 10%). Interestingly, differences in CVC do not always translate to differences in AP. For example, when comparing `Deep Salience` (yellow) and `ResNet-M` (grey)—two models of similar size—we observe that although `ResNet-M` , which incorporates residual connections, achieves higher CVC, both models attain similar AP. We discuss this observation further in Section 5.2. 

To summarize, most experiments show a correlation between CVC and AP. However, some individual examples suggest that CVC may capture aspects of a model that are not fully reflected in AP scores within the domain of the multi-version sets. Notably, we observed instances where a model with higher CVC did not necessarily achieve higher AP—and the other way around. 

## 5.2 Proxy for Robustness 

While the previous experiments examined the relationship between CVC and model efficacy within the same domain, we now turn our focus to robustness. To address this second research question and assess whether CVC serves as a 

275 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
80 Spearman's ρ : 0.70<br>78<br>76<br>+<br>74<br>t=<br>72<br>70<br>Aver+ roeon os)68<br>66<br>0.76 0.77 0.78 0.79 0.80 0.81 0.82 0.83<br>Cross-Version Consistency(BPSD)<br>Training data<br>SWD SWD+BPSD BPSD+BSQD<br>BPSD SWD+BSQD SWD+BPSD+BSQD<br>BSQD<br><!-- End of picture text -->

Figure 5: CVC as proxy for model robustness. CVC on `BPSD` vs. AP on `RWC+TRIOS` . As in Figure 3 we compare `ResNet-M` trained on the different training data. 

proxy for a model’s ability to generalize to out-of-domain data, we analyze its correlation with AP on the two unseen out-of-domain datasets: `RWC` and `TRIOS` . For this we will take a closer look at the two instances, where correlation was not observed in the previous experiments. 

Domain of Training Data: Let us recall the experiment on varying the domain of training data from the previous section. When evaluating in the domain of `BPSD` (Figure 3b), changes in AP did not necessarily correspond to CVC. We now extend this analysis by comparing CVC on `BPSD` to AP on `RWC+TRIOS` . The results of this are shown in Figure 5. Note that, while the meaning of the y-axis changed, the x-axis is exactly the same as in the experiment from the previous section. As opposed to the previous section, we can now see a strong correlation (ρ = .7) between CVC on `BPSD` and AP on `RWC+TRIOS` . Looking closer at our previous example, we see that the lower CVC of the models trained on `BPSD` (yellow) is now reflected in a lower AP on out-of domain data. Whereas the higher CVC of the models trained on `SWD+BSQD` (light blue) is reflected in a higher AP. This indicates that by measuring CVC, we are able to identify models that overfit to dataset biases of `BPSD` . 

Model Architecture: We now conduct an experiment similar to the architecture comparison from the previous section (Figure 4). However, now we compare CVC on the combined three multi-version datasets to AP on `RWC+TRIOS` (Figure 6). The overall trends remain similar, but one difference emerges. Taking a closer look at the two models with differences in CVC but similar AP ( `Deep Salience` and `ResNet-M` ), we now observe that `Deep Salience` performs slightly worse on the out-of-domain test set compared to `ResNet-M` . This also reflects in a slightly higher correlation coefficient. Even though the effect is small, this supports two insights: (1) models with residual connections may generalize better, aligning with 



<!-- Start of picture text -->
80 Spearman's ρ : 0.71<br>78<br>76<br>Architecture<br>Basic Pitch<br>74 Deep Salience<br>ResNet-S<br>Average Prec i son (RWC+TRIOS) ResNet-M<br>ResNet-L<br>72<br>0.79 0.80 0.81 0.82 0.83 0.84 0.85 0.86<br>Cross-Version Consistency (Combined)<br><!-- End of picture text -->

Figure 6: CVC as proxy for model robustness. CVC on the three multi-version datasets vs. AP on `RWC+TRIOS` . As in Figure 4 we compare different architectures, all trained on `SWD+BPSD+BSQD` . 

prior findings [12] and (2) CVC might be able to capture this generalization ability. 

To summarize, the previous section identified instances where CVC captures model aspects not fully reflected in AP scores within multi-version datasets. For those cases, we investigated whether CVC on the multi-version datasets might correlates with standard evaluation metrics on outof-domain datasets. Our results suggest that CVC does indeed seem to provide insights into model robustness. This would indicate that CVC is not just a useful evaluation metric within the domain of the multi-version dataset, but also a valuable additional figure of merit for assessing a model’s ability to generalize to out-of-domain data. 

## 6. CONCLUSION 

In this paper, we presented CVC as an annotation-free strategy for evaluating AMT models, which assesses whether a model makes consistent predictions when facing different versions of the same musical piece. We argued that CVC is, by design, a desirable property of transcription models used for corpus analysis. We showed that, in most cases, it may serve as a proxy of model efficacy within a domain. In cases where it does not, we could observe that CVC can provides insights into a model’s ability to generalize to out-of-domain data, making it a powerful additional figure of merit. 

In this work, we established CVC for evaluation. However, we believe that our findings lay the groundwork for a larger goal: leveraging multi-version data to improve model training. The results give confidence to the idea of cross-version based contrastive learning [17] for MPE. Inspired by the usage in [11], in future work we would like to explore using the CVC as a distance measure for contrastive learning with a Siamese Network architecture [25]. Since this study focused on frame-level transcription (MPE), our future work will explore note-level transcription, integrating onset detection [4, 16] and Transformer architectures for further improvements. 

276 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 7. ACKNOWLEDGEMENTS: 

This work was funded by the German Research Foundation (Deutsche Forschungsgemeinschaft, DFG) within the Emmy Noether Junior Research Group on Computational Analysis of Music Audio Recordings: A Cross-Version Approach (DFG WE 6611/3-1, Grant No. 531250483). 

## 8. REFERENCES 

- [1] E. Benetos, S. Dixon, Z. Duan, and S. Ewert, “Automatic music transcription: An overview,” IEEE Signal Processing Magazine, vol. 36, no. 1, pp. 20–30, 2019. 

- [2] X. Serra, “The computational study of a musical culture through its digital traces,” Acta Musicologica, vol. 89, no. 1, p. 24–44, 2017. 

- [3] M. Neuwirth, D. Harasim, F. C. Moss, and M. Rohrmeier, “The annotated Beethoven corpus (ABC): A dataset of harmonic analyses of all Beethoven string quartets,” Frontiers Digit. Humanit., vol. 5, p. 16, 2018. 

- [4] C. Hawthorne, E. Elsen, J. Song, A. Roberts, I. Simon, C. Raffel, J. H. Engel, S. Oore, and D. Eck, “Onsets and frames: Dual-objective piano transcription,” in Proceedings of the International Society for Music Information Retrieval Conference, (ISMIR), Paris, France, 2018, pp. 50–57. 

- [5] C. Hawthorne, I. Simon, R. Swavely, E. Manilow, and J. H. Engel, “Sequence-to-sequence piano transcription with transformers,” in Proceedings of the International Society for Music Information Retrieval Conference (ISMIR), Online, 2021, pp. 246–253. 

- [6] Q. Kong, B. Li, X. Song, Y. Wan, and Y. Wang, “Highresolution piano transcription with pedals by regressing onset and offset times,” IEEE ACM Trans. Audio Speech Lang. Process., vol. 29, pp. 3707–3717, 2021. 

- [7] J. Gardner, I. Simon, E. Manilow, C. Hawthorne, and J. H. Engel, “MT3: multi-task multitrack music transcription,” in The Tenth International Conference on Learning Representations, (ICLR), 2022. 

- [8] S. Chang, E. Benetos, H. Kirchhoff, and S. Dixon, “YourMT3+: multi-instrument music transcription with enhanced transformer architectures and crossdataset STEM augmentation,” in 34th IEEE International Workshop on Machine Learning for Signal Processing, (MLSP). IEEE, 2024, pp. 1–6. 

- [9] C. Weiß and G. Peeters, “Comparing deep models and evaluation strategies for multi-pitch estimation in music recordings,” IEEE ACM Trans. Audio Speech Lang. Process., vol. 30, pp. 2814–2827, 2022. 

- [10] R. Geirhos, J. Jacobsen, C. Michaelis, R. S. Zemel, W. Brendel, M. Bethge, and F. A. Wichmann, “Shortcut learning in deep neural networks,” Nat. Mach. Intell., vol. 2, no. 11, pp. 665–673, 2020. 

- [11] A. Riou, S. Lattner, G. Hadjeres, and G. Peeters, “PESTO: pitch estimation with self-supervised transposition-equivariant objective,” in Proceedings of the 24th International Society for Music Information Retrieval Conference, (ISMIR), 2023, pp. 535–544. 

- [12] C. Weiß, H. Schreiber, and M. Müller, “Local key estimation in music recordings: A case study across songs, versions, and annotators,” IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 28, pp. 2919–2932, 2020. 

- [13] M. Krause, S. Strahl, and M. Müller, “Weakly supervised multi-pitch estimation using cross-version alignment,” in Proceedings of the 24th International Society for Music Information Retrieval Conference, (ISMIR), 2023, pp. 289–296. 

- [14] L. Liu and C. Weiss, “Utilizing cross-version consistency for domain adaptation: A case study on music audio,” in The Second Tiny Papers Track at (ICLR), 2024. 

- [15] R. M. Bittner, B. McFee, J. Salamon, P. Li, and J. P. Bello, “Deep salience representations for F0 tracking in polyphonic music,” in Proceedings of the International Society for Music Information Retrieval Conference (ISMIR), Suzhou, China, 2017, pp. 63–70. 

- [16] R. M. Bittner, J. J. Bosch, D. Rubinstein, G. MeseguerBrocal, and S. Ewert, “A lightweight instrumentagnostic model for polyphonic note transcription and multipitch estimation,” in IEEE International Conference on Acoustics, Speech and Signal Processing, (ICASSP). IEEE, 2022, pp. 781–785. 

- [17] M. Krause, C. Weiß, and M. Müller, “A cross-version approach to audio representation learning for orchestral music,” in Proceedings of the 24th International Society for Music Information Retrieval Conference, ISMIR, A. Sarti, F. Antonacci, M. Sandler, P. Bestagini, S. Dixon, B. Liang, G. Richard, and J. Pauwels, Eds., 2023, pp. 832–839. 

- [18] M. Müller, Fundamentals of Music Processing - Using Python and Jupyter Notebooks, Second Edition. Springer, 2021. 

- [19] C. Weiß, F. Zalkow, V. Arifi-Müller, M. Müller, H. V. Koops, A. Volk, and H. G. Grohganz, “Schubert winterreise dataset: A multimodal scenario for music analysis,” ACM Journal on Computing and Cultural Heritage, vol. 14, no. 2, pp. 25:1–25:18, 2021. 

- [20] J. Zeitler, C. Weiß, V. Arifi-Müller, and M. Müller, “BPSD: A coherent multi-version dataset for analyzing the first movements of beethoven’s piano sonatas,” Trans. Int. Soc. Music. Inf. Retr., vol. 7, no. 1, pp. 195– 212, 2024. 

- [21] M. Goto, H. Hashiguchi, T. Nishimura, and R. Oka, “RWC music database: Music genre database and 

277 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

musical instrument sound database,” in Proceedings of the International Society for Music Information Retrieval Conference (ISMIR), Baltimore, Maryland, USA, 2003, pp. 229–230. 

- [22] J. Fritsch and M. D. Plumbley, “Score informed audio source separation using constrained nonnegative matrix factorization and score synthesis,” in Proceedings of the IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP), 2013, pp. 888–891. 

- [23] M. Müller, Y. Özer, M. Krause, T. Prätzlich, and J. Driedger, “Sync Toolbox: A Python package for efficient, robust, and accurate music synchronization,” Journal of Open Source Software (JOSS), vol. 6, no. 64, pp. 3434:1–4, 2021. 

- [24] T. Prätzlich, J. Driedger, and M. Müller, “Memoryrestricted multiscale dynamic time warping,” in IEEE International Conference on Acoustics, Speech and Signal Processing, (ICASSP). IEEE, 2016, pp. 569– 573. 

- [25] J. Bromley, I. Guyon, Y. LeCun, E. Säckinger, and R. Shah, “Signature verification using a siamese time delay neural network,” in Advances in Neural Information Processing Systems 6, [7th NIPS Conference]. Morgan Kaufmann, 1993, pp. 737–744. 

278 

