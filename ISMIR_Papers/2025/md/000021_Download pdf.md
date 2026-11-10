---
paper_id: "000021"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706363/files/000021.pdf"
---

# ALIGNING TEXT-TO-MUSIC EVALUATION WITH HUMAN PREFERENCES 

Yichen Huang<sup>1</sup> Zachary Novack<sup>2</sup> Koichi Saito<sup>3</sup> Jiatong Shi<sup>1</sup> Shinji Watanabe<sup>1</sup> Yuki Mitsufuji<sup>3</sup> John Thickstun<sup>4</sup> Chris Donahue<sup>1</sup> 

1Carnegie Mellon University 2University of California – San Diego 

3Sony AI 4Cornell University 

```
william_h21@outlook.com,chrisdonahue@cmu.edu
```

## ABSTRACT 

Despite significant recent advances in generative acoustic text-to-music (TTM) modeling, robust evaluation of these models lags behind, relying in particular on the popular Fréchet Audio Distance (FAD). In this work, we rigorously study the design space of reference-based divergence metrics for evaluating TTM models through (1) designing four synthetic meta-evaluations to measure sensitivity to particular musical desiderata, and (2) collecting and evaluating on MusicPrefs, an open-source dataset of pairwise human preferences for TTM systems. We find that not only is the standard FAD setup inconsistent on both synthetic and human preference data, but that nearly all existing metrics fail to effectively capture desiderata, and are only weakly correlated with human perception. We propose a new metric, the MAUVE Audio Divergence (MAD), computed on representations from a self-supervised audio embedding model. We find that this metric effectively captures diverse musical desiderata (average rank correlation 0.84 for MAD vs. 0.49 for FAD) and also correlates more strongly with MusicPrefs (0.62 vs. 0.14). 

## 1. INTRODUCTION 

Recent advances in text-to-music (TTM) modeling have produced models capable of generating coherent, highfidelity, open-ended music audio [1–6]. While the perceived quality of TTM systems has clearly improved, our evaluation methods have not kept pace with this progress. Systematic human evaluation data for generated music is limited, unlike modalities like text [7] and speech [8]. Automatic evaluations of music commonly rely on the Fréchet Audio Distance (FAD) [9]. However, FAD was originally developed for evaluating music enhancement algorithms, and has been shown to correlate poorly with human preferences on open-ended music generation [10]. 

> © Y. Huang, Z. Novack, K. Saito, J. Shi, S. Watanabe, Y. Mitsufuji, J. Thickstun, C. Donahue. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: Y. Huang, Z. Novack, K. Saito, J. Shi, S. Watanabe, Y. Mitsufuji, J. Thickstun, C. Donahue, “Aligning Text-to-music Evaluation with Human Preferences”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

In this work, we perform a systematic study of the design space of automatic evaluation metrics for open-ended Western pop music generation. We identify three components of an automatic evaluation metric: (1) a reference set of representative music that we aim to model, (2) a representation that captures salient features of music audio, and (3) a divergence metric that quantifies differences between representations of the reference set and those of the generated music. This design space includes FAD, which uses VGGish features [11] and the Fréchet distance as a divergence, as well as more recent proposals that pair Fréchet distance with richer audio representations [12,13] such as those from CLAP [14], or replace Fréchet distance with kernelized divergence metrics such as MMD [15]. 

To more rigorously explore this design space, we conduct a meta-evaluation of metrics by studying their sensitivity to “common sense” desiderata—properties that we posit as desirable for any TTM system tailored for pop music generation. We codify each desideratum as a synthetic data generation process: we produce degraded music audio with controlled and increasing amounts of degradation, inducing an interpretable ordering. We then meta-evaluate a metric by measuring the rank correlation (Kendall’s τ ) between its ordering of the degraded music to the “ground truth”. We propose four degradation processes, reflecting sensitivity of metrics to four desiderata: fidelity, musicality, context length, and diversity. From these findings we propose a new metric, the MAUVE Audio Divergence (MAD), which performs well in our meta-evaluation compared to FAD (τ = 0.84 vs. 0.49 respectively, see our supplementary material for comprehensive results).<sup>1</sup> 

Ultimately our goal is to identify metrics that not only align with common sense desiderata, but also with real human preferences. To measure this, we collect and release MusicPrefs, an open-source dataset of pairwise human preferences for TTM generation (concurrent with [16,17]). We find that MAD correlates more strongly human preferences (τ = 0.62) according to MusicPrefs, compared to traditional evaluation metrics including FAD (τ = 0.14). We can think of the meta-evaluation as training data for metric selection, and MusicPrefs as test data—from this perspective, the results of human evaluation show that MAD is not overfit to the synthetic meta-evaluation tasks. 

1 `https://bit.ly/mad-metric-supplement` 

174 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
Human Eval (MusicPrefs) TTM Models Automatic Eval (MAD)<br>Reference Reference Divergence Calculation<br>Model #1 Distribution Embeddings Old: FAD, MMD<br>A<br>Embedding …<br>Model #2 Model<br>Proposed: MAUVE<br>B Old: VGGish<br>Proposed: MERT …<br>Model #N<br>Generated Generated<br>Distribution Embeddings<br>Winrates: [Model #2: 30%, Model #1: 40%, ...] Divergences: [Model #3: 0.6, Model #2: 0.4, ...]<br>Measure Correlation<br>…<br><!-- End of picture text -->

Figure 1: Overview of our proposed automatic evaluation metric (MAD) and open dataset of human preferences for TTM (MusicPrefs). Given a collection of open TTM models, we present a thorough analysis of different reference-based divergence metrics and embedding backbones. Then, by collecting MusicPrefs, an open source dataset of pairwise TTM human preference data, we measure how well the induced rankings of different metrics correlate with human preferences. 

Our overall contributions are summarized as follows: 

- We perform a systematic study of evaluation metrics for TTM, based on a broad set of audio degradation models and validated by human preferences. 

- We introduce MusicPrefs, a new open source dataset of human preference data TTM outputs. 

- We propose the MAUVE Audio Divergence (MAD) metric for TTM evaluation, based on the MAUVE metric for open-ended text generation [18]. According to MusicPrefs, MAD correlates more strongly with human preferences than previous metrics. 

Figure 1 provides an overview of MAD and MusicPrefs. Code and data are made available.<sup>2</sup> 

## 2. PRELIMINARIES AND METHODS 

We study reference-based evaluation metrics [19] that compare a collection of generated outputs to a reference set of representative data from the distribution we aspire to model. A reference-based metric quantifies the divergence between the probability distribution of a distribution q (ordinarily a generative model) and a reference distribution p using a representative sample x1,...,Np ∼ p, i.e., a reference set of Np human music performances. To identify salient discrepancies between q and p, we define an evaluation metric on features of examples extracted using an embedding model. Given Nq generated outputs y1,...,Nq ∼ q, and features f : audio → R<sup>d</sup> from an embedding model, a reference-based evaluation metric M : q → [0, ∞) is a divergence D(f (y1), . . . , f (yNq )||f (x1), . . . , f (xNp )) between features of audio generated by q and features of reference audio from p. 

> 2 Sound examples from our synthetic study and MusicPrefs can be found at `https://bit.ly/mad-metric` . An implementation of MAD is available at `https://github.com/i-need-sleep/ mad` . MusicPrefs is available at `https://huggingface.co/ datasets/i-need-sleep/musicprefs` . 

The design space of reference-based evaluation metrics can therefore be characterized by (1) the reference distribution p and corresponding reference set, (2) the embedding model and features f used to process the audio samples, and (3) the divergence D used to calculate distributional discrepancies in feature space R<sup>d</sup> . For example, FAD uses VGGish as the embedder, activations of the final (pre-classification) layer as features, Fréchet distance as a divergence, and doesn’t prescribe a particular reference set. 

## 2.1 Choosing a Reference Set 

Gui et al. [12] report that the choice of reference set can heavily influence the performance of automatic metrics. Moreover, the commonly used MusicCaps [3] dataset includes a notable amount of low-quality entries that can make FAD scores correlate poorly with human ratings. In our experiments, we primarily use FMA-Pop [12], a curated subset of FMA [20] emphasizing songs with high play counts under the “pop” label. We focus on pop because this is the primary genre modeled by state-of-the-art music generation systems. FMA-Pop contains 4,230 songs of 30 seconds in length each. To compare this openly available reference set to more restrictive choices, we also experiment with an internal dataset of high-quality licensed music audio containing 7,846 songs, from which we extract 30-second clips at random. 

## 2.2 Extracting Features from Embedding Models 

We study the performance of a variety of audio models as embedding models. In addition to VGGish [11], originally used for FAD, and the higher-performing audio understanding models explored in Gui et al. [12] (CLAP [14] and MERT [21]), we experiment with strong music generation models (MusicGen [4] and Jukebox [1]). We study these self-supervised models as embedding models because they may more accurately capture salient audio features overlooked by distantly-supervised music models [22]. 

Given an embedding model, we consider several strategies to extract features. A natural candidate for features 

175 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

is model’s internal activations. For a deep model with many layers, we must decide which layer’s activations to use as features. For audio models, which process temporal data, we must decide how to aggregate these features across time. We study four strategies for temporal aggregation of features: (1) Max-pool: take the maximum of each feature across time; (2) Average-pool, the mean of each feature across time; (3) Last: features at the last time index; (4) First: features at the first time index (only considered for the bi-directional MERT model). For more details about our search space of embedding backbones, layers, and pooling methods, see Table 3 in the supplement. 

## 2.3 Calculating Divergences 

We study a variety of divergences for parameterizing an evaluation metric. The key distinctions between these metrics involve how they estimate the reference and generated distributions within the chosen embedding space. FAD [9] uses the assumption that these distributions are Gaussian and calculate the Frechét distance between them. MMD [23] (equivalently referred to as KD or KAD [15]) constructs a kernel density estimator of these distributions. The Precision/Recall/Density/Coverage (or PRDC) metrics [19] use k-NN estimators: Precision/Density/Coverage use k-NN to estimate the support of the reference distribution p and measure whether the generated samples are supported by p; Recall conversely uses k- NN to estimate the support of the generative distribution q and measure whether the reference set is supported by q. MAUVE [24] uses k-means to form discrete histogram estimates of p and q, and approximates the divergence curve C(p, q) = {(exp(−cKL(q|rλ)), exp(−cKL(p|rλ)))} for rλ = λp + (1 − λ)q, λ ∈ (0, 1). MAUVE is defined as the area under the approximated divergence curve. 

As MAUVE is a score bounded on [0, 1] where higher is better, for consistency with other divergence metrics such as FAD we redefine it as − ln(MAUVE) ranging from [0, inf) where lower is better. Among the metrics we study, MAUVE and Recall are the only metrics that explicitly estimate the generated distribution q in the embedding feature space (as MMD only does this implicitly in the corresponding RKHS) with more expressivity than fitting a single Gaussian like FAD. 

## 3. SYNTHETIC DATA META-EVALUATION 

To explore the design space of reference-based music metrics, we first construct a set of four meta-evaluations designed to specifically disentangle different desiderata in TTM systems. A high quality evaluation metric intuitively should be sensitive to human interpretable degradations of our target data. Formally, if we have some ordered set of model distributions {q1, q2, . . . , qK} in decreasing order of human perceptual quality (q1 best, qK worst), then a good divergence metric M should induce the following behavior: M (qi) < M (qj), ∀i < j. Thus, our synthetic meta-evaluation seeks to assess how well a given metric follows this behavior across different sets of distributions {qi} that codify particular desiderata. 

Past works look at the sensitivity of metrics to degradations in audio fidelity by distorting with noise [9,12]. In addition to measuring sensitivity to fidelity, here we explore three additional desiderata for musicality, context, and diversity. For each desideratum, we propose a pattern that interpretably degrades music along that axis alone. In this way, we capture whether a given metric actually captures specific forms of musical degradation, which allows us to measure sensitivity of each metric to changes in distortion strength as well as embedding backbone. Our goal is not to comprehensively capture all possible distortions a TTM model could exhibit, but instead to capture a few common sense ones to enable more objective comparison of metrics. 

For each desideratum, we generate K = 11 sets of increasingly degraded audio, where each set contains 5,000 clips of 30 seconds in length. For each metric M , we measure the rank correlation (Kendall’s τ ) between the ordering induced by the metric and the ground truth ordering 1, . . . , K. We measure rank correlations for two reasons: (1) direct correlation metrics like Pearson’s assume linearity (which cannot be assumed for any given divergence), and (2) modern TTM divergence metrics exist primarily for researchers to compare the relative performance of generative systems (i.e., “horse-racing"); the absolute differences between models for a given divergence are generally poorly understood and not particularly meaningful. We outline each desiderata in the following subsection—see our supplement for additional details on each task. 

## 3.1 Codifying desiderata via synthetic degradations 

Fidelity. Fidelity is the simplest form of degradation and has been somewhat studied previously on Frechét-based metrics [9, 12]. Here, we start with the FMA-Pop dataset, and gradually distort the audio fidelity of each sample. Specifically, we add isotropic Gaussian noise to each audio file, with increasing standard deviation denoting greater distortion (the noise added to qi has a standard deviation of 0.2 ·<sup><mark>i</mark></sup> 10<sup>−</sup><sup><mark>1)</mark>.Notably, this is the only category of degrada-</sup> tion that is considered in previous work. 

Musicality. Absent from previous acoustic music evaluations is any way to measure the “musicality" of a TTM model’s outputs. While this is inherently difficult to measure directly, we codify (Western) musicality using the notion that perceived musicality is correlated with features of the symbolic representation of music. Specifically, we posit that introducing random pertubations both rhythmically (i.e. slight changes in note timing) and harmonically (i.e. pitch changes) can contribute to degradation of musicality. We perturb subsets of notes by [−6, 6] semitones in pitch and [−0.2, 0.2] seconds in onset and offset. We use a subset of the Lakh MIDI dataset [25] while perturbing the note timings and pitches with increasing probability of perturbation from 0 to 0.5 in steps of 0.05. From these perturbed MIDI sequences, we then render them into 44.1 kHz audio using Fluidsynth [26]. In this way, we can directly measure how evaluation metrics treat changes to the musical structure independently of audio fidelity distortions. 

Context. While our definitions of fidelity and musi- 

176 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
Fidelit y Musicalit y Context Diversit y<br>1. 0 FAD<br>0. 8 Recall<br>MAUVE<br>0. 6<br>0. 4<br>0. 2<br>0. 0<br>0.000 0.025 0.050 0.075 0.100 0.125 0.150 0.175 0.200 0.0 0.1 0.2 0.3 0.4 0.5 1 2 3 4 5 10 0 10 1 10 2 10 3<br>White noise std. Note perturbation prob. Max. context len. (seconds) Num. unique prompts<br>Adjusted score<br><!-- End of picture text -->

Figure 2: Aggregated results for synthetic meta-evaluation. Metric scores are normalized to [0, 1] and averaged across all embedding models. Shaded areas show standard deviations. While FAD shows large inconsistencies on Musicality and minor inconsistencies on others, Recall and MAUVE have robust performance on all desiderata. 

cality effectively capture local structure, they do not fully address how music fundamentally requires long-term coherence. Text-to-music (TTM) systems often introduce unique perceptual artifacts related to temporal inconsistency. To assess whether evaluation metrics detect these temporal coherence issues, we sample from MusicGenSmall [4] while controlling for context length by generating in k-step blocks where k ∈{1, 2, 3, . . . , 10, 15} seconds. For each block, the model only accesses the previous block as context. This allows us to directly manipulate temporal consistency, as shorter-context generations typically lack coherent structure and contain jarring transitions that violate musical expectations. 

Diversity. While the preceding tasks all measure different senses of perceptual quality, diversity is equally important for TTM systems and their evaluation metrics [19]. Thus, here we treat the artificial reduction of diversity as the distortion factor. We use a cleaned subset of text prompts from MusicCaps [3] (detailed in Section 4) and prompt MusicGen-Small to generate 5000 segments using a decreasing prompt set size (lower diversity), specifically: {2.5K, 2K, 1K, 500, 200, 100, 50, 25, 10, 5, 1}. At the extreme, all 5k generations are based on the same prompt. In this way, we can assess how different evaluation metrics react to different levels of diversity. 

## 3.2 Results 

Here we compare a number of different evaluation metrics and embedding backbones (see Section 2). For each task and metric, we search over combinations of layers and pooling methods for each embedding backbone with FMAPop as the reference set. In order to assess the performance of each embedding backbone-divergence combination, we report the Kendall-Tau coefficient τ between the automatic scores and ground truth rankings (i.e. whether a given metric captures the decrease in quality as the distortion level increases for each task), which is bounded in [-1, 1]. 

With this framework, we investigated four high-level empirical questions: (1) How robust are different divergence metrics to changes in embedding backbones? (2) How much does embedding backbone impact metric performance? (3) How robust are such divergence metrics to changes in reference distribution? (4) How efficient are such metrics with respect to the generation set size? 

Metric Robustness Across Embeddings. In Table 1 (top), we show the average Kendall τ across the four synthetic sets aggregated across embedding models, each un- 

der their best (layer, aggregation) setups. Notably, MAUVE and Recall show the best overall performance, surpassing all other metrics across embedding backbones. In particular, FAD and all other metrics struggle heavily on the musicality task, showing a distinct lack of the ability to evaluate generated music that has consistent audio quality but semantic degradations, and perform poorly on the Context and Diversity tasks. This suggests that our musicality, context, and diversity sets can be a useful tool in meta-evaluating sensitivity to more nuanced differences in music. Interestingly, Recall and Coverage, while designed as diversity measures, can also distinguish quality differences in musicality, fidelity, and context length. Precision and Density exhibits relative poorer performance in all four aspects despite being designed as fidelity measures. This indicates that Precision and Density may have a low performance ceiling for evaluating music. 

Figure 2 shows the scores by each metric against the groundtruth level of distortion directly for FAD and our top performing metrics MAUVE and Recall. In particular, we find that MAUVE not only captures the gradual perturbation under each task well, but does so with considerably lower variance across embedding backbones than Recall and FAD do. Additionally, though most metrics are capable of distinguishing differences between varying intensities of Gaussian noises, corroborating previous works [9, 12], MAUVE scores more closely follow an exponential pattern, which is arguably more similar to human perception of additive Gaussian distortion. 

Divergence Quality by Embedding Backbone. With MAUVE and Recall established as the more robust metrics, we now shift our attention to how different embedding models perform when applied with these metrics. Results are shown in Table 1 (bottom). We observe that the self-supervised models MERT, Jukebox, MusicGen embeddings perform reasonably well when paired with either MAUVE or Recall. VGGish performs notably poorly in evaluating Musicality, with practically random performance as the distortion level increases, since its classification training does not allow it to capture the more nuanced and long-term factors in music quality. CLAP similarly falls behind on Musicality and Context, presumably because of the limited expressiveness allowed by its text-audio training data. 

Robustness Across Reference Sets. Since all the divergence metrics studied are reference-based metrics, the choice of reference dataset can be highly important, as the 

177 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

||Fidelity|Musicality|Context|Diversity|Average|Avg. (Internal)|
|---|---|---|---|---|---|---|
|Recall|1.00±0.00|0.80±0.24|0.70±0.21|0.87±0.06|0.84±0.11|0.82±0.16|
|MAUVE|1.00±0.00|0.73±0.30|0.81±0.16|0.59±0.13|0.78±0.07|0.86±0.07|
|FAD|0.91±0.22|0.44±0.57|0.92±0.13|0.61±0.20|0.72±0.14|0.71±0.20|
|Coverage|1.00±0.00|0.49±0.40|0.64±0.30|0.70±0.14|0.71±0.07|0.71±0.11|
|MMD|1.00±0.00|0.35±0.61|0.78±0.31|0.60±0.25|0.68±0.26|0.75±0.25|
|Density|0.95±0.12|0.01±0.73|−0.12±0.80|0.31±0.29|0.29±0.17|0.55±0.35|
|Precision|0.88±0.23|0.12±0.43|−0.23±0.67|0.39±0.28|0.29±0.26|0.49±0.25|
|MusicGen-M|1.00±0.00|0.98±0.03|0.85±0.00|0.76±0.22|0.90±0.06|0.92±0.11|
|MusicGen-S|1.00±0.00|0.93±0.05|0.76±0.23|0.70±0.24|0.85±0.02|0.93±0.14|
|MERT|1.00±0.00|0.75±0.21|0.89±0.05|0.76±0.22|0.85±0.02|0.91±0.22|
|Jukebox|1.00±0.00|0.89±0.05|0.82±0.00|0.62±0.29|0.83±0.08|0.83±0.25|
|VGGish|1.00±0.00|0.53±0.51|0.78±0.21|0.87±0.06|0.79±0.09|0.74±0.33|
|CLAP|1.00±0.00|0.51±0.13|0.42±0.10|0.67±0.15|0.65±0.02|0.69±0.18|



Table 1: Average Kendall τ rank correlation (higher is better) and standard deviation between different evaluation setups and our synthetic meta-evaluation set. Top: Aggregated correlation across embedding models, each under their best (layer, aggregation) setup. Bottom: Aggregated correlation across the more robust MAUVE and Recall metrics. All metrics are calculated against FMA-Pop except for the last column, which is uses our internal set of high-quality licensed music. 

lower-quality but commonly used MusicCaps (where some excerpts are captioned as “low-quality") results in metric scores less correlated with human preference as opposed to FMA-Pop and MusCC (a small subset of musdb18 [27]) [12]. In order to verify that the present results are robust across reference sets, we recreate our experiments using an internal set of high-quality music of similar size. 

Results are shown in the rightmost column in Table 1. FMA-Pop performs comparably to our set of internal music as a reference set, with the internal music leading to an overall slightly better performance. The trends we observe with FMA-Pop still holds: MAUVE and Recall are consistently higher-performing, and embedding from selfsupervised models consistently lead to better performance. This presents an important point for open research in the TTM space: while high-quality reference sets may seem optimal, FMA-Pop proves to be reasonably comparable as a reference distribution to perform generative evaluation. 

Efficiency. The compute time for reference-based TTM evaluation is dominated by the time it takes to generate and embed each audio sample, as opposed to the time required to measure divergence (despite previous concerns). Accordingly, sample efficiency is the strongest determining factor for overall computational efficiency (as opposed to asymptotic behavior of the metric [15,23]). To examine how robust each metric is with respect to sample size, we measure rank correlation on our synthetic metaevaluation data for FAD with VGGish and CLAP embeddings, MMD with MERT embeddings, and MAUVE with MERT embeddings across exponentially decreasing the generated sample sizes of {5000, 2500, 1250, 625}. We find that FAD and MAUVE are comparably robust to reduction in the sample size (similar correlation at N = 5000 and N = 625 samples), while MAUVE shows stronger overall correlations at all sample sizes. See Figure 5 in the supplementary material for more details. 

## 3.3 MAD: MAUVE Audio Divergence (MAD) 

These insights from our synthetic meta-evaluation motivate a new TTM evaluation metric: MAUVE Audio Di- 

vergence (MAD). Specifically, MAD utilizes MERT to extract embeddings, which are then used to calculate MAUVE in its embedding space. Out of the stronger performing metrics MAUVE and Recall, we choose MAUVE as we observe lower variance in scores across embedding backbones, suggesting robust tolerance to changes in backbones. Among self-supervised models which perform well across Mauve and Recall (MusicGen and MERT), we choose MERT to avoid the counterintuitive scenario of evaluating generative models with other generative models. MAD is able to capture a wide range of musical perturbations, far surpassing the current standard usage of FAD and discriminative backbones. While we recommend that practitioners use a reference set that best codifies the goals of their TTM system, we offer FMA-Pop as a default, given that it correlates well with MAD scores on our internal reference set. In our synthetic meta-evaluation, MAD (0.84 average τ ) significantly outperforms the standard FAD with VGGish embeddings (0.49 average τ ). Both MERT and MAUVE notably contributes to the improved performance: Ablating MERT (MAUVE + VGGish) results in an average τ of 0.73 while ablating MAUVE (FAD + MERT) leads to an average τ of 0.72. 

## 4. MEASURING HUMAN PREFERENCE ALIGNMENT 

Collecting MusicPrefs. We collected a large dataset of human preferences on music generated by state-ofthe-art open weights TTM models. Our approach involved two key steps: (1) generating music samples from 7 representative models (Stable Audio Open [5], MusicGen small/medium/large [4], AudioLDM2 [28], MusicLDM [29], and Riffusion v1 [2]) using 2,617 instrumental-only text prompts derived from MusicCaps, and (2) collecting pairwise human preferences via Amazon Mechanical Turk. For each prompt, we generated 10 outputs per model using distinct random seeds, resulting in 183k total audio clips. We then collected preferences on 2,520 output pairs (120 preferences per unique model pair), asking annotators to independently judge fidelity 

178 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

||||Hu|man|||Au|tomatic (|Diverge|nce)|Control|
|---|---|---|---|---|---|---|---|---|---|---|---|
|System|Over|all↑|Fidel|ity↑|Music|ality↑|FAD↓|FAD-C|LAP↓|MAD↓|CLAP↑|
|MusicGen-L|24.24|(1)|22.96|(1)|25.42|(1)|5.649 (4)|3.904|(2)|2.744 (2)|0.356 (3)|
|MusicGen-M|17.28|(2)|17.35|(2)|17.08|(2)|5.802 (5)|3.940|(5)|3.504 (3)|0.337 (5)|
|MusicGen-S|14.11|(3)|14.67|(3)|13.43|(4)|6.032 (6)|3.987|(6)|3.928 (4)|0.314 (6)|
|MusicLDM|12.17|(4)|10.45|(6)|14.02|(3)|5.538 (1)|3.916|(4)|4.713 (5)|0.411 (1)|
|SAO|11.41|(5)|13.95|(4)|9.19|(6)|5.547 (2)|3.883|(1)|1.970 (1)|0.356 (4)|
|AudioLDM2|10.83|(6)|9.87|(7)|11.74|(5)|5.632 (3)|3.913|(3)|5.321 (6)|0.378 (2)|
|Riffusion v1|9.97|(7)|10.75|(5)|9.12|(7)|7.994 (7)|4.179|(7)|5.477 (7)|0.185 (7)|
|τ (pval.)|1.00 (|0.00)|0.71 (|0.03)|0.81 (|0.01)|0.14 (0.77)|0.14|(0.77)|0.62 (0.07)|0.10 (0.76)|



Table 2: Comparison of human preferences from MusicPrefs to automatic metrics for music generation models, including MAD (proposed). Human preferences are Bradley-Terry scores. We solicit musicality and fidelity preferences separately, referring to their union as “Overall”. We report standard automatic metrics: FAD using VGGish [9] and CLAP [12] embeddings, our proposed MAD which measures MAUVE [18] on MERT [21] embeddings, and CLAP score [14] which measures an orthogonal axis of adherence to text control (we do not expect it to correlate). For each metric, we induce a ranking and compute the Kendall τ rank correlation relative to overall human preferences. We find that MAD yields stronger correlation (τ = 0.62, p = 0.07) with human preferences relative to existing metrics. 

and musicality without showing them the original prompts. Annotators could declare ties, which we discarded from analysis (25% for fidelity, 19% for musicality). 

Measuring Alignment. We assess how well our analyzed metrics align with human preferences. In particular, we focus on how the ordering induced by a given divergence metric matches the human rankings from MusicPrefs. We focus on this ranking behavior as the ability to consistently determine the relative performance of models (i.e., “horse-racing") is integral to modern TTM research in assessing commensurate gains from paper to paper. We compare MAD to the baseline FAD (with both VGGish and CLAP backbones), as well as the induced ranking from the reference-free CLAP-Score metric [14,30], which measures control adherence to the underlying text conditions and should be independent of human ranking. 

Table 2 shows the overall induced rankings by each metric sorted according to the overall human ranking and Kendall’s τ coefficients relative to the overall rankings. Human rankings are calculated through their BradleyTerry scores, which are linearly equivalent to Elo score and thus more accurately estimate the overall strength of each model than assessing raw win rate [7,31,32]. MAD shows a stronger correlation with human rankings than other metrics, nearly exactly matching the human preferences with the exception of a strong preference towards Stable Audio Open. Note that we do not expect CLAP score to correlate with MusicPrefs as annotators were not shown prompts— we include it to provide evidence that MusicPrefs measures desiderata orthogonal to control as intended. 

## 5. RELATED WORK 

Generative music systems, and in particular audio-domain systems, have seen a renaissance in recent years driven by the wider methodological explosion in generative models, owing core advances to insights from language models [1,4] and diffusion models [2,5,28,29]. Despite similarities with the text and image domains, the space of work on generative evaluation is much less developed for TTM. 

While Kilgour et al. [9] and Gui et al. [12] have attempted to assess the quality of evaluation metrics in TTM systems (leading to the adoption of better FAD backbones [33–35]), these only considered Frechét Distance as a metric, and only considered fidelity distortions in their analyses. While some TTM works have included additional metrics outside FAD and CLAP score [5,6, 29,36,37], such works purely rely on the assumption that insights from the image modality [19,23] would transfer to TTM, with no empirical verification. Vinay and Lerch [10] and Chung et al. [15] are similar, with the former focusing on benchmarking metrics for older audio synthesis models (with no strong correlation found with human perception), and the latter exploring the MMD metric used in earlier TTM works [6,36,38] for foley generation. Concurrently, two recent works have collected human ratings and preference data on synthetic music clips from TTM systems [16, 17]. Liu et al. [16] collect Mean Opinion Scores for each system based on overall music impression and text alignment—here we collect pairwise preferences. Grötschla et al. [17] also collect pairwise preferences for TTM, though they do not explore alignment with automatic metrics. 

## 6. CONCLUSION 

We propose MAD: a new evaluation metric for automatic evaluation of TTM models. MAD is derived from a systematic meta-evaluation that analyzes sensitivity of evaluation hyperparameters to various music generation desiderata. In terms of robustness, we find that MAUVE outperforms previously studied divergences like Fréchet Distance, and self-supervised embedding models like MERT outperform discriminative ones. We collect and release MusicPrefs, an open dataset of pairwise human TTM preferences, and use it to demonstrate that MAD strongly correlates with human preferences. While we do not recommend replacing human evaluations with MAD, automatic evaluations can provide a powerful signal for competition and hill-climbing on model performance. We hope MAD can provide such a signal for music generation research. 

179 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 7. ACKNOWLEDGEMENTS 

This work was supported by funding from Sony AI. 

## 8. REFERENCES 

- [1] P. Dhariwal, H. Jun, C. Payne, J. W. Kim, A. Radford, and I. Sutskever, “Jukebox: A generative model for music,” arXiv preprint arXiv:2005.00341, 2020. 

- [2] S. Forsgren and H. Martiros, “Riffusion - Stable diffusion for real-time music generation,” 2022. [Online]. Available: https://riffusion.com/about 

- [3] A. Agostinelli, T. I. Denk, Z. Borsos, J. Engel, M. Verzetti, A. Caillon, Q. Huang, A. Jansen, A. Roberts, M. Tagliasacchi, M. Sharifi, N. Zeghidour, and C. Frank, “Musiclm: Generating music from text,” 2023. [Online]. Available: https://arxiv.org/abs/2301. 11325 

- [4] J. Copet, F. Kreuk, I. Gat, T. Remez, D. Kant, G. Synnaeve, Y. Adi, and A. Defossez, “Simple and controllable music generation,” in Advances in Neural Information Processing Systems, A. Oh, T. Naumann, A. Globerson, K. Saenko, M. Hardt, and S. Levine, Eds., vol. 36. Curran Associates, Inc., 2023, pp. 47 704–47 720. 

- [5] Z. Evans, J. D. Parker, C. Carr, Z. Zukowski, J. Taylor, and J. Pons, “Stable audio open,” 2024. [Online]. Available: https://arxiv.org/abs/2407.14358 

- [6] Z. Novack, G. Zhu, J. Casebeer, J. McAuley, T. BergKirkpatrick, and N. J. Bryan, “Presto! distilling steps and layers for accelerating music generation.” in International Conference on Learning Representations (ICLR), 2025. 

- [7] W.-L. Chiang, L. Zheng, Y. Sheng, A. N. Angelopoulos, T. Li, D. Li, B. Zhu, H. Zhang, M. I. Jordan, J. E. Gonzalez, and I. Stoica, “Chatbot arena: An open platform for evaluating llms by human preference,” in ICML, 2024. [Online]. Available: https://openreview.net/forum?id=3MW8GKNyzI 

- [8] W.-C. Huang, S.-W. Fu, E. Cooper, R. Zezario, T. Toda, H.-M. Wang, J. Yamagishi, and Y. Tsao, “The voicemos challenge 2024: Beyond speech quality prediction,” 2024 IEEE Spoken Language Technology Workshop, 12 2024. [Online]. Available: https://arxiv.org/abs/2409.07001 

- [9] K. Kilgour, M. Zuluaga, D. Roblek, and M. Sharifi, “Fréchet audio distance: A reference-free metric for evaluating music enhancement algorithms,” in Interspeech, 2019. [Online]. Available: https://api. semanticscholar.org/CorpusID:202725406 

- [10] A. Vinay and A. Lerch, “Evaluating generative audio systems and their metrics,” in Proceedings of the 23nd International Society for Music Information Retrieval Conference (ISMIR 2022), 2022. 

- [11] S. Hershey, S. Chaudhuri, D. P. W. Ellis, J. F. Gemmeke, A. Jansen, R. C. Moore, M. Plakal, D. Platt, R. A. Saurous, B. Seybold, M. Slaney, R. J. Weiss, and K. Wilson, “Cnn architectures for large-scale audio classification,” in 2017 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2017, pp. 131–135. 

- [12] A. Gui, H. Gamper, S. Braun, and D. Emmanouilidou, “Adapting frechet audio distance for generative music evaluation,” in Proc. IEEE ICASSP 2024, 2024. [Online]. Available: https://arxiv.org/abs/2311.01616 

- [13] J. Retkowski, J. Stepniak, and M. Modrzejewski, “Frechet music distance: A metric for generative symbolic music evaluation,” 2025. [Online]. Available: https://arxiv.org/abs/2412.07948 

- [14] Y. Wu, K. Chen, T. Zhang, Y. Hui, T. Berg-Kirkpatrick, and S. Dubnov, “Large-scale contrastive languageaudio pretraining with feature fusion and keywordto-caption augmentation,” in IEEE International Conference on Acoustics, Speech and Signal Processing, ICASSP, 2023. 

- [15] Y. Chung, P. Eu, J. Lee, K. Choi, J. Nam, and B. S. Chon, “Kad: No more fad! an effective and efficient evaluation metric for audio generation,” arXiv preprint arXiv:2502.15602, 2025. 

- [16] C. Liu, H. Wang, J. Zhao, S. Zhao, H. Bu, X. Xu, J. Zhou, H. Sun, and Y. Qin, “Musiceval: A generative music dataset with expert ratings for automatic text-tomusic evaluation,” in ICASSP 2025 - 2025 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2025, pp. 1–5. 

- [17] F. Grötschla, A. Solak, L. A. Lanzendörfer, and R. Wattenhofer, “Benchmarking music generation models and metrics via human preference studies,” in ICASSP 2025 - 2025 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2025, pp. 1–5. 

- [18] K. Pillutla, S. Swayamdipta, R. Zellers, J. Thickstun, S. Welleck, Y. Choi, and Z. Harchaoui, “MAUVE: Measuring the gap between neural text and human text using divergence frontiers,” in Advances in Neural Information Processing Systems, A. Beygelzimer, Y. Dauphin, P. Liang, and J. W. Vaughan, Eds., 2021. [Online]. Available: https://openreview.net/forum?id= Tqx7nJp7PR 

- [19] M. F. Naeem, S. J. Oh, Y. Uh, Y. Choi, and J. Yoo, “Reliable fidelity and diversity metrics for generative models,” in International Conference on Machine Learning. PMLR, 2020, pp. 7176–7185. 

- [20] M. Defferrard, K. Benzi, P. Vandergheynst, and X. Bresson, “FMA: A dataset for music analysis,” in 18th International Society for Music Information Retrieval Conference (ISMIR), 2017. [Online]. Available: https://arxiv.org/abs/1612.01840 

180 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [21] Y. Li, R. Yuan, G. Zhang, Y. Ma, X. Chen, H. Yin, C. Lin, A. Ragni, E. Benetos, N. Gyenge, R. Dannenberg, R. Liu, W. Chen, G. Xia, Y. Shi, W. Huang, Y. Guo, and J. Fu, “Mert: Acoustic music understanding model with large-scale self-supervised training,” 2023. 

- [22] R. Castellon, C. Donahue, and P. Liang, “Codified audio language modeling learns useful representations for music information retrieval,” arXiv preprint arXiv:2107.05677, 2021. 

- [23] S. Jayasumana, S. Ramalingam, A. Veit, D. Glasner, A. Chakrabarti, and S. Kumar, “Rethinking fid: Towards a better evaluation metric for image generation,” in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2024, pp. 9307– 9315. 

- [24] K. Pillutla, L. Liu, J. Thickstun, S. Welleck, S. Swayamdipta, R. Zellers, S. Oh, Y. Choi, and Z. Harchaoui, “Mauve scores for generative models: theory and practice,” J. Mach. Learn. Res., vol. 24, no. 1, Mar. 2024. 

- [25] C. Raffel, “Learning-based methods for comparing sequences, with applications to audio-to-midi alignment and matching,” 2016. [Online]. Available: https://api.semanticscholar.org/CorpusID:63439223 

- [26] FluidSynth, “Fluidsynth: Software real-time synthesizer based on the soundfont 2 specification,” https: //www.fluidsynth.org, 2024, accessed: 2024-11-20. 

- [27] Z. Raf **i** , A. Liutkus, F.-R. Stöter, S. I. Mimilakis, and R. Bittner, “The MUSDB18 corpus for music separation,” Dec. 2017. [Online]. Available: https: //doi.org/10.5281/zenodo.1117372 

- [28] H. Liu, Y. Yuan, X. Liu, X. Mei, Q. Kong, Q. Tian, Y. Wang, W. Wang, Y. Wang, and M. D. Plumbley, “Audioldm 2: Learning holistic audio generation with self-supervised pretraining,” IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 32, pp. 2871–2883, 2024. 

[Online]. Available: https://api.semanticscholar.org/ CorpusID:125209808 

   - [32] H. White, “Maximum likelihood estimation of misspecified models,” Econometrica, vol. 50, no. 1, pp. 1–25, 1982. [Online]. Available: http://www.jstor.org/stable/1912526 

   - [33] Z. Novack, J. McAuley, T. Berg-Kirkpatrick, and N. J. Bryan, “DITTO: Diffusion inference-time t- optimization for music generation,” in International Conference on Machine Learning (ICML), 2024. 

   - [34] ——, “DITTO-2: Distilled diffusion inference-time t- optimization for music generation,” in International Society of Music Information Retrieval (ISMIR), 2024. 

   - [35] R. Ciranni, E. Postolache, G. Mariani, M. Mancusi, L. Cosmo, and E. Rodolà, “Cocola: Coherenceoriented contrastive learning of musical audio representations,” ArXiv, vol. abs/2404.16969, 2024. [Online]. Available: https://api.semanticscholar.org/ CorpusID:269430865 

   - [36] J. Nistal, M. Pasini, C. Aouameur, M. Grachten, and S. Lattner, “Diff-a-riff: Musical accompaniment cocreation via latent diffusion models,” arXiv preprint arXiv:2406.08384, 2024. 

   - [37] K. Saito, D. Kim, T. Shibuya, C.-H. Lai, Z. Zhong, Y. Takida, and Y. Mitsufuji, “SoundCTM: Unifying score-based and consistency models for full-band text-to-sound generation,” in The Thirteenth International Conference on Learning Representations, 2025. [Online]. Available: https://openreview.net/forum?id=KrK6zXbjfO 

   - [38] J. Nistal, M. Pasini, and S. Lattner, “Improving musical accompaniment co-creation via diffusion transformers,” arXiv preprint arXiv:2410.23005, 2024. 

- [29] K. Chen, Y. Wu, H. Liu, M. Nezhurina, T. BergKirkpatrick, and S. Dubnov, “Musicldm: Enhancing novelty in text-to-music generation using beatsynchronous mixup strategies,” in ICASSP 2024 - 2024 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2024, pp. 1206– 1210. 

- [30] R. Huang, J. Huang, D. Yang, Y. Ren, L. Liu, M. Li, Z. Ye, J. Liu, X. Yin, and Z. Zhao, “Make-an-audio: Text-to-audio generation with prompt-enhanced diffusion models,” arXiv preprint arXiv:2301.12661, 2023. 

- [31] R. A. Bradley and M. E. Terry, “Rank analysis of incomplete block designs: I. the method of paired comparisons,” Biometrika, vol. 39, p. 324, 1952. 

181 

