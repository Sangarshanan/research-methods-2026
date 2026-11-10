---
paper_id: "000018"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706355/files/000018.pdf"
---

# EXPLORING THE FEASIBILITY OF LLMS FOR AUTOMATED MUSIC EMOTION ANNOTATION 

Meng Yang<sup>1</sup> Jon McCormack<sup>1</sup> Maria Teresa Llano<sup>2</sup> Wanchao Su<sup>1</sup> 1 SensiLab, Monash University, Melbourne, Australia 

2 University of Sussex, Brighton, United Kingdom 

```
{Meng.Yang,Jon.McCormack,Wanchao.Su}@monash.edu,Teresa.Llano@sussex.ac.uk
```

## ABSTRACT 

Current approaches to music emotion annotation remain heavily reliant on manual labelling, a process that imposes significant resource and labour burdens, severely limiting the scale of available annotated data. This study examines the feasibility and reliability of employing a large language model (GPT-4o) for music emotion annotation. In this study, we annotated GiantMIDI-Piano, a classical MIDI piano music dataset, in a four-quadrant valence-arousal framework using GPT-4o, and compared against annotations provided by three human experts. We conducted extensive evaluations to assess the performance and reliability of GPT-generated music emotion annotations, including standard accuracy, weighted accuracy that accounts for inter-expert agreement, inter-annotator agreement metrics, and distributional similarity of the generated labels. 

While GPT’s annotation performance fell short of human experts in overall accuracy and exhibited less nuance in categorizing specific emotional states, inter-rater reliability metrics indicate that GPT’s variability remains within the range of natural disagreement among experts. These findings underscore both the limitations and potential of GPT-based annotation: despite its current shortcomings relative to human performance, its cost-effectiveness and efficiency render it a promising scalable alternative for music emotion annotation. 

## 1. INTRODUCTION 

Music is widely recognized as a medium for conveying complex human emotions and experiences, making emotion-related research a focal point in the Music Information Retrieval (MIR) community [1]. Most empirical advances in emotion-related MIR start with a prerequisite step: securing a sufficiently large, reliable set of emotion labels. Existing datasets like DEAM [2], Emotify [3], VGMIDI [4] and EMOPIA [5], were all created through intensive manual annotation campaigns. While indispensable, human labelling is slow and costly, so most 

> © M. Yang, J. McCormack, T. Llano, and W. Su. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: M. Yang, J. McCormack, T. Llano, and W. Su, “Exploring the Feasibility of LLMs for Automated Music Emotion Annotation”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

of these datasets plateau at a few thousand items. These scale limits, in turn, the downstream research: modern deep architectures demand far more data than the community can currently afford to label by hand. Recent advances in large language models (LLMs) have transformed text understanding, making it possible to infer music’s perceived emotion from extrinsic textual sources—metadata, lyrics, and contextual descriptions. Some of what shapes listeners’ perceived emotion is encoded outside the sound itself: composer biographies, genre conventions, and the historical context of composition [6]. Although LLMs cannot “hear” melody, harmony, or timbre, they can parse these documents and extract the affective stance they imply. In vocal music, lyrics already serve as an effective textual proxy and have underpinned successful MER studies [7–10]. Instrumental works, however, lack built-in semantic cues; for them, metadata becomes the primary linguistic window into a composer’s expressive intent. This has been demonstrated in previous research, which has shown correlations between perceived emotion as well as historical and cultural context [11], motivating our use of metadatadriven LLM inference to annotate perceived emotion at scale for instrumental music. 

In this study, we explore a novel annotation methodology that employs a large language model (GPT-4o) as an automated annotator for the perceived emotion of music. Our approach uses the title and composer of a music piece as search keywords to retrieve relevant web results, providing the LLM with extracted textual content as context, enabling it to infer an appropriate emotion label based on the available information. We apply our method to annotate GiantMIDI-Piano [12], a classical piano dataset with 10,855 MIDI music pieces, using a four-quadrant valencearousal framework. To evaluate this GPT-based annotation method, we randomly selected 100 samples from each of four emotion categories, totalling 400 samples, and obtained annotations for each sample from three human experts. We then compared the GPT-generated labels against the expert annotations using a comprehensive evaluation framework that includes binary and weighted accuracy metrics, inter-annotator reliability measures (Cohen’s Kappa and Fleiss’ Kappa), and distributional similarity analyses via Jensen–Shannon divergence. 

Our findings show that although GPT-4o does not yet match human experts in overall accuracy or nuanced emotional categorization, its inter-rater variability falls within 

150 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

the range of natural disagreement among experts. These results highlight both the challenges and potential of LLMbased annotation: while further refinements are needed before it can fully replace manual annotation, the method’s cost-effectiveness and efficiency make it a promising approach for large-scale music emotion annotation. 

The main contributions of this paper are as follows: (1) We propose a cost-effective approach to music emotion annotation by leveraging GPT’s text-based inference capability, reducing the reliance on time-consuming and costly manual labelling, (2) We develop a comprehensive evaluation framework incorporating accuracy metrics, interannotator agreement measures, and distributional analyses to assess and compare the performance of GPT-generated and expert annotations. 

## 2. RELATED WORK 

## 2.1 Music Emotion Annotation 

Early Music Information Retrieval (MIR) research on emotion, such as Music Emotion Recognition (MER), has relied heavily on manually annotated datasets. For example, CAL500 [13] contains 502 songs and each song is annotated with multiple human-provided emotion labels, and the DEAM dataset [2] includes 1,802 music excerpts with continuous and static arousal-valence annotations. While these corpora have proven invaluable for developing and evaluating models and tasks, manual emotion annotation requires multiple human listeners per track, making it both costly and labour-intensive [14–16]. As a result, most datasets are small in scale, typically comprising only hundreds or thousands of songs, and are often limited to specific genres [2–5, 13], constraining the performance on data-intense models. Models trained on such limited datasets struggle to generalize, and the lack of large-scale, standardized datasets complicates benchmarking across different studies. 

Various alternative approaches have been proposed to address these challenges. Gamified annotation techniques such as MoodSwings [17], and crowd-sourced tagging platforms like Last.fm and AllMusic, can expedite label collection, but they often introduce new problems such as data sparsity, biased sampling, or unclear taxonomy and a lack of label quality assurance [14]. The need for scalable, cost-effective, and consistent annotation methods has led researchers to explore advanced AI solutions – including LLMs – to assist or automate the labelling process. 

## 2.2 LLM-Based Annotation 

Recently, LLMs have revolutionized text-based annotation and classification tasks [18]. Unlike task-specific classifiers, LLMs are pre-trained on massive text corpora and can perform labelling through natural language prompts without task-specific retraining. Studies have shown that these models can match or even occasionally surpass the accuracy and consistency of crowd-sourced or expert annotations, primarily by applying labelling criteria more uniformly and reducing the impact of subjective interpretation [19, 20]. Moreover, once deployed, LLMs annotate data 

rapidly and at relatively low cost, rendering them highly suitable for large-scale applications [21]. 

Textual sources have long served as the source of emotional evidence for music–emotion studies. Early work inferred emotion directly from lyrics [7–10, 22], while more recent efforts have mined user-generated discourse—YouTube comments, tweets, Reddit threads—to annotate pieces along the valence–arousal plane, achieving moderate reliability with transformer models [23]. These strategies, however, presuppose plentiful public discussion or vocal content and therefore miss much of the instrumental and lesser-known classical repertoire. Prior research shows that metadata—composer background, genre, stylistic school, and historical context—also correlates with music emotion [11], which offers a broadly applicable foundation for automatic emotion annotation. Our study builds on this insight: we employ LLMs to annotate perceived emotion labels directly from contextual metadata, thereby expanding annotated resources for the non-lyrics music. 

## 3. METHODOLOGY 

## 3.1 Data Preparation 

We employed the GiantMIDI-piano dataset [12], a classical piano MIDI collection comprising 10,855 files from 2,786 composers. For each piece, we collected contextual information by web-crawling a curated list of music information sources<sup>1</sup> . We extracted metadata, such as genre, style, composer biography, historical and cultural context, and the composer’s creative intent, which were then incorporated into the prompt provided to the GPT-4o for annotating the perceived emotion of the music. 

## 3.2 GPT-based Annotation 

The collected text metadata was used to automate emotion annotation of the music in our dataset. Emotion labels were assigned according to Russell’s valence–arousal model [24], following the quadrant-based scheme used in EMOPIA [5] to categorized into four discrete quadrants: High Valence–High Arousal (HVHA), High Valence–Low Arousal (HVLA), Low Valence–High Arousal (LVHA), and Low Valence–Low Arousal (LVLA). GPT-4o was supplied with contextual information via a structured prompt that explicitly instructed it to infer the perceived emotional content of each piece solely from the provided text, thereby minimizing hallucination. If the model determined that the available information was insufficient for a reliable annotation, it was instructed to return the label “not enough information.” The prompt is presented in Figure 1. To ensure that GPT-4o selected the most reliable label based on the context and did not introduce random fluctuations, we set the model’s temperature to 0. Following the annotation process, a total of 9,803 musical pieces were assigned valid emotion labels. 

> 1 e.g., `en.wikipedia.org` , `imslp.org` , `naxos.com` , `allmusic.com` , `classical-music.com` , `gramophone. co.uk` 

151 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
You are a music expert tasked with annotating<br>the emotion conveyed by a musical piece.<br>Based on the context provided below, select<br>one valence-arousal label that best describes<br>the music's emotional state. Choose only from<br>the following options:<br>HVHA: High Valence, High Arousal<br>HVLA: High Valence, Low Arousal<br>LVHA: Low Valence, High Arousal<br>LVLA: Low Valence, Low Arousal<br>If the context does not clearly indicate a<br>specific emotion, make reasonable inferences<br>using as much information as possible about<br>the genre, style, historical context etc.<br>Only if no useful clues are available, answer<br>“not enough information”.<br>{context}<br><!-- End of picture text -->

Figure 1. The Prompt for Music Emotion Annotation. 

## 3.3 Human Evaluation 

To assess the feasibility and quality of GPT-generated annotations, we engaged three annotators with over five years of formal music training and similar cultural backgrounds. Before annotation, they calibrated their understanding of the valence–arousal framework to ensure a consistent labelling standard. We randomly sampled 100 tracks from each of the four emotion quadrants (400 total), ensuring a balanced distribution across quadrants. To reduce potential stylistic bias, the samples were selected to cover a diverse range of composers and musical styles within the classical piano repertoire. Each annotator independently labelled the perceived emotion based on listening experience. The annotations were then aggregated by majority voting to establish a human-derived gold standard. Samples for which at least two out of three annotators agreed were designated as high-confidence samples, while those lacking consensus were classified as low-confidence samples. Our human annotation results yielded 386 high-confidence samples and 14 low-confidence samples. 

## 3.4 Evaluation Framework 

We assessed the performance and reliability of the GPTgenerated labels using a comprehensive evaluation framework that incorporates multiple metrics: 

## 3.4.1 Accuracy 

Binary Accuracy is defined as the proportion of highconfidence samples for which the GPT-generated label exactly matches the gold standard obtained via majority voting among human experts. 

Given the subjectivity in music emotion annotation, a strict binary accuracy metric—where a sample is considered “correct” only if the GPT-generated label exactly matches the gold standard (i.e., the majority vote from experts)—may not capture the nuances of expert disagreement. To more precisely reflect the gradations in expert agreement, we propose a Weighted Accuracy that incorporates partial consensus among experts. Specifically, let si be the score assigned to sample i based on how closely GPT’s prediction aligns with expert consensus: 

- Full Consensus (3/3): All three experts agree on the same label. In this case if GPT’s label matches the gold standard, si = 1; Otherwise si = 0. 

- Partial Consensus (2/3): Two experts agree on a majority label Lm, and one expert has a minority label Ln. In this case if GPT’s label equals Lm, si = 1; if GPT’s label equals Ln, si = 0.5; Otherwise si = 0<sup>2</sup> . 

- Complete Disagreement (3 distinct labels): All three experts disagree, each offering a unique label. If GPT’s label matches any one of the three experts labels, si = 1/3. Otherwise si = 0. 

Finally, the Weighted Accuracy is computed as the average score across all N samples: 



<!-- Start of picture text -->
n<br>WeightedAccuracy = N 1 � si<br>i=1<br><!-- End of picture text -->

## 3.4.2 Inter-Annotator Consistency 

Cohen’s Kappa is used to measure pairwise agreement between two sets of annotations while accounting for chance agreement. For a pair of raters, it is given by: 



<!-- Start of picture text -->
κ = P 1 0  −  − P P e e ,<br><!-- End of picture text -->

where P0 is the observed agreement and Pe is the expected agreement by chance. We computed Cohen’s Kappa for GPT versus the gold standard, as well as for each pair of human annotators. 

Fleiss’ Kappa extends the kappa statistic to multiple raters. Given a rating matrix R where each row represents a sample and each column j represents the number of ratings for category j, the per-item agreement is: 



<!-- Start of picture text -->
k<br>1<br>Pi = � nij(nij − 1)<br>ni(ni − 1)<br>j=1<br><!-- End of picture text -->



<!-- Start of picture text -->
k<br>with ni N= � nij. The overall observed argreement is<br>P¯ = N 1 � Pji=1, and the chance agreement is Pe = �k p 2 j ,<br>i=1 j=1<br><!-- End of picture text -->

where pi is the proportion of ratings in category j across all samples. Fleiss’ Kappa is then: 



<!-- Start of picture text -->
P¯ − Pe<br>κF = 1 − Pe ,<br><!-- End of picture text -->

We computed Fleiss’ Kappa for both the human-only annotations and for the combined GPT and human annotations. 

## 3.4.3 Distributional Similarity 

JS divergence is used to measure the similarity between two probability distributions. For each sample, let P = (p1, ..., pk) be the aggregated expert distribution (derived from the relative frequencies of the three expert labels) and Q = (q1, ..., qk) be the one-hot representation of the GPT prediction. The JS divergence is defined as: 

> 2 Note that each sample contributes at most one credit—so the weighted accuracy remains within [0, 1], and GPT incurs no penalty when its annotation aligns with the majority. 

152 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

|Annotator|Accuracy|Weighted Accuracy|
|---|---|---|
|GPT-4o|0.710|0.788|
|Human1|0.833|-|
|Human2|0.812|-|
|Human3|0.869|-|



Table 1. Accuracy Comparison of GPT-4o and Human Annotations with respect to the Gold Standard. 

|Model|Accuracy|
|---|---|
|GPT-3.5|0.430|
|GPT-4o|0.710|
|GPT-4.5|0.705|



Table 2. Accuracy Comparison among GPT models. 



<!-- Start of picture text -->
JS(P ∥ Q) = 2 1 K L(P ∥ M ) + 2 1 K L(Q ∥ M )<br><!-- End of picture text -->

where M = 2 <mark>1</mark><sup><mark>(</mark>P+ Q)andtheKullback–Leiblerdiver-</sup> gence KL(P ∥ Q) is given by: 



<!-- Start of picture text -->
k<br>KL(P ∥ Q) = � pj log pj<br>qj<br>j=1<br><!-- End of picture text -->

A lower JS divergence indicates greater similarity between the GPT-generated and aggregated expert distributions. 

## 4. EXPERIMENTAL RESULTS AND DISCUSSION 

## 4.1 Pre-Test: Stability and Reproducibility of GPT-4o’s Annotation 

Before conducting the main evaluation, we performed a pre-test to verify the stability and reproducibility of GPT4o’s annotations under a deterministic setting (temperature = 0). This configuration ensures that the model consistently selects the most probable output, eliminating randomness and enabling precise evaluation. To test this, GPT-4o was prompted to annotate the same 400 samples across three independent runs. Results showed that 385 samples received identical labels in all runs, and the remaining 15 had two out of three consistent labels. This high level of consistency confirms that temperature = 0 yields stable, repeatable outputs, allowing us to attribute performance differences to the model’s underlying reasoning rather than stochastic variation. 

## 4.2 Accuracy 

## 4.2.1 Overall Annotation Performance 

Table 1 demonstrates the accuracy of GPT-4o’s annotations against a human-derived gold standard, evaluated using both binary and weighted accuracy metrics. Binary accuracy, the proportion of high-confidence samples in which GPT-4o’s label exactly matched the gold standard, was approximately 71%. In contrast, weighted accuracy, which accounts for varying degrees of expert consensus by awarding partial credit in cases of partial agreement, increased to around 78%. Although human annotators achieved higher binary accuracy (ranging from approximately 81% to 87% across individual raters), the performance of GPT-4o is still acceptable considering the inherent subjectivity of music emotion annotation and the advantages in cost and efficiency. 

## 4.2.2 Comparison of GPT Model Performance 

We evaluated multiple GPT models from OpenAI for music emotion annotation. As results shown in table 2, the newly released GPT-4.5 achieves 70.5% accuracy, matching GPT-4o’s 71%, offering no notable improvement. In contrast, GPT-3.5 reaches only 43%, underscoring significant advancements in the GPT-4 family’s ability to accurately interpret and annotate musical emotion. 

## 4.2.3 Context Ablation Study 

To further validate the effectiveness of providing musical context, we conducted an ablation experiment in which GPT-4o was prompted to label the same 400 samples without any additional context information. In this “title-only” condition, GPT-4o had access to nothing more than the music title and composer name, and it achieved a binary accuracy of only 57%. In contrast, when the model was furnished with the context we collected from online sources describing the work’s genre, stylistic background, historical and cultural factors, and composer biography, its accuracy rose significantly to 71%. This gap underscores the importance of contextual information for disambiguating subtle emotional cues – information that purely nominal references (e.g., a piece’s title) cannot reliably convey. Therefore, the contextual metadata can be seen as a crucial signal enabling GPT-4o to better align its annotations with expert judgments. 

## 4.2.4 Consensus-Based Subgroup Analysis 

In addition to overall accuracy metrics, we analyzed performance within two expert-consensus subgroups. As shown in table 3, in the full-consensus group (211 samples in which all experts agreed), GPT-4o correctly annotated 180 samples (85.3%) and erred on 31 samples. In the partial-consensus group (175 samples with a 2/3 expert agreement), GPT-4o matched the majority opinion in 94 samples (53.7%), with no instances of aligning with the minority opinion and 21 samples classified entirely incorrectly. By comparison, human annotators in the partialconsensus subgroup achieved correctness ranging from 114 to 121 out of 175 samples (65.1% to 69.1%). These findings indicate that GPT-4o performs robustly when expert consensus is strong, and in cases of ambiguity, it captures a substantial portion of expert agreement. 

## 4.3 Inter-Annotator Reliability Analysis 

Inter-annotator reliability was assessed using both Cohen’s Kappa and Fleiss’ Kappa. Table 4 and table 5 present both pairwise Cohen’s Kappa and Fleiss’ Kappa values. The Cohen’s Kappa between GPT-4o and the gold standard (obtained via majority voting) was 0.613, indicating moderate agreement. Among the human experts, the pairwise Cohen’s Kappa values were 0.547, 0.568, and 0.569, with an average of 0.561. In addition, the pairwise Cohen’s Kappa values between GPT-4o and individual human annotators were 0.467, 0.593, and 0.607, yielding an average of 0.556. Although GPT-4o’s agreement with individual experts is slightly lower than the agreement observed 

153 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
Grou p N GPT-4o Human1 Human2 Human3<br>Full-Consensus 211 180 (85.3%) 211 211 211<br>Partial Consensus 175 94  ( 53.7% ) 114  ( 65.1% ) 115  ( 65.7% ) 121  ( 69.1% )<br>Table 3. Accuracy of GPT-4o and Human Annotators in Full and Partial Consensus Groups.<br>Annotator GPT-4o Human1 Human2 Human3 Normalized Confusion Matrix (Gold vs GPT) Normalized Confusion Matrix (Gold vs Human1)<br>0.8<br>Human1GPT-4o 0.467N.A. 0.467N.A. 0.5930.547 0.6070.568 HVHA 0.73 0.07 0.16 0.05 0.7 HWHA 0.88 0.08 0.05 0.00 0.70.8<br>Human2 0.593 0.547 N.A 0.569 HVLA 0.12 0.61 0.13 0.13 HVLA 0.12 0.78 0.05 0.04 0.6<br>Human3 0.607 0.568 0.569 N.A. 0.5<br>0.4<br>Table 4.. Pairwise Cohen’s Kappa between GPT-4o and (golxl (pertU/HA 0.08 0.09 0.70 0.13 0.2 UVHA 0.09 0.01 0.84 0.06 0.20.3<br>human experts. I/LA 0.00 0.12 0.04 0.84 0.1 IVLA 0.00 0.03 0.09 0.88 0.1<br>HVHA Prediction UHA IVLA 0.0 HVHA Prediction S/HA U/LA<br>Normalized Confusion Matrix (Gold vs Human2) Normalized Confusion Matrix (Gold vs Human3)<br>HVHA 0.83 0.05 0.12 0.00 0.8 HVHA 0.85 0.08 0.07 0.00 0.8<br>0.7 0.7<br>H/LA 0.06 0.06 0.04 0.04 HMLA 0.07 0.88 0.01 0.04 0.6<br>0.5 0.5<br>Table 5.. Summary of inter-annotator reliability metrics in I/HA 0.06 0.02 0.89 0.03 0.30.4 LVHA 0.04 0.06 0.84 0.06 0.30.4<br>both average Cohen’s Kappa and Fleiss’ Kappa values. Gold (Expert Consensus) 0.2 0.2<br>IVLA 0.00 0.16 0.05 0.79 0.1 LVLA 0.00 0.07 0.07 0.87 0.1<br>among human annotators, the differences are relatively mi- 0.0 0.0<br>nor. At the group level, Fleiss’ Kappa was 0.561 for the HVHA HVLAPrediction UNA HVLAPection DIHA DVLA<br><!-- End of picture text -->

Table 4.. Pairwise Cohen’s Kappa between GPT-4o and human experts. 

||Average|Average|Fleiss|Fleiss|
|---|---|---|---|---|
|GPT-4o|GPT-4o|Human|Kappa|Kappa|
|v.s. Gold|v.s.|v.s.|among|GPT-4o v.s.|
||Human|Human|Human|Human|
|0.613|0.556|0.561|0.561|0.558|



Table 5.. Summary of inter-annotator reliability metrics in both average Cohen’s Kappa and Fleiss’ Kappa values. 

among human annotators, the differences are relatively minor. At the group level, Fleiss’ Kappa was 0.561 for the human experts and 0.558 when GPT-4o was included, indicating that GPT-4o’s overall variability is comparable to that of the human raters. 

Figure 2. Normalized confusion matrix (by gold standard) comparing GPT-4o-generated emotion labels with expert consensus. 

To compare the agreement levels of GPT-4o against each individual expert, we performed bootstrap-based hypothesis testing on the pairwise Cohen’s Kappa statistics. As shown in table 6, although the average Cohen kappa of GPT-4o versus gold (0.614) is close to the mean human kappa (0.593), bootstrap difference analysis reveals that GPT-4o’s agreement with the gold standard is significantly lower than each expert, as evidenced by the 95% confidence intervals for the differences (e.g.,[-0.267,0.135] when comparing to Human3) all lying below zero. This outcome indicates that, on an individual basis, experts agree with the gold standard more consistently than GPT4o does. However, these pairwise discrepancies should be interpreted in the context of normal inter-rater variance: they highlight that GPT-4o tends to deviate from the gold standard more often than any single human annotator, rather than reflecting the overall group-level consistency. Indeed, a subsequent Fleiss’ Kappa analysis reveals that incorporating GPT-4o into the set of raters does not significantly alter collective agreement—its mean difference from the human-only group is 0.003 with a 95% confidence interval of [-0.019,0.025], indicating no significant impact. Consequently, while GPT-4o’s labeling differs more often from the gold standard than any single human expert, its variability at the group level remains within the range of human disagreement. 

predictions to the aggregated expert distribution, the average squared JS divergence was lower at 0.175. These results suggest some divergence between GPT-4o’s predictions and individual expert labels, but the overall similarity to the combined expert consensus is moderate, indicating GPT-4o captures much of the collective expert opinion despite minor discrepancies with individual judgments. 

## 4.4 Error Analysis by Category 

Error analysis based on the normalized confusion matrices (Figure 2) reveals misclassification patterns for GPT4o relative to the gold standard. In the high valence–high arousal (HVHA) category, for instance, GPT-4o correctly annotated 73% of samples but misclassified about 16.0% as low valence–high arousal (LVHA). A similar trend is observed in the low valence-low arousal (LVLA) category, where GPT-4o’s performance is relatively robust and even slightly exceeds that of Human2; however, GPT-4o tends to misclassify some LVLA samples as HVLA. These suggest that while GPT-4o is relatively adept at capturing the arousal dimension, it struggles to distinguish between positive and negative valence. Notably, This pattern of valence confusion is also present in Human2’s annotations, suggesting that even expert annotators may find it challenging to precisely distinguish the valence of some samples in this category. Additionally, GPT-4o exhibits suboptimal performance in the high valence–low arousal (HVLA) category, indicating a limited capacity to capture emotional nuances. Collectively, these findings highlight that while GPT-4o performs reasonably well in cases with clear emotional cues, its ability to discern fine-grained differences in emotion—particularly those involving the valence dimension—remains limited. 

## 4.3.1 Jensen–Shannon Divergence Analysis 

Table 7 shows the squared JS divergence for interpretability, where lower values indicate greater similarity between distributions. On an individual basis, the average squared JS divergence between GPT-4o and each expert was 0.266 (GPT-4o vs. Human1), 0.205 (GPT-4o vs. Human2), and 0.194 (GPT-4o vs. Human3). When comparing GPT-4o’s 

154 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

|Comparison|Main Difference|95% CI|
|---|---|---|
|GPT-4o vs. Gold minusHuman1 vs. Gold|-0.174|[-0.250, -0.096]|
|GPT-4o vs. Gold minus Human2 vs. Gold|-0.176|[-0.241, -0.113]|
|GPT-4o vs. Gold minus Human3 vs. Gold|-0.200|[-0.267,-0.135]|
|Fleiss’ kappa,Human Experts minus GPT-4o & Human Experts|0.003|[-0.019,0.025]|



Table 6. Bootstrap Differences in Pairwise and Group-Level Kappa. 

|Comparison|Main Difference|
|---|---|
|GPT-4o v.s. Human1|0.266|
|GPT-4o v.s. Human2|0.205|
|GPT-4o v.s. Human3|0.194|
|GPT-4o v.s. Aggregated Experts|0.175|



Table 7. Average Squared Jensen–Shannon Divergence between GPT-4o and Expert Annotation Distributions 

## 5. DISCUSSION AND FUTURE WORK 

Our results indicate that while GPT-4o’s overall performance in music emotion annotation falls short of human expert-level accuracy, its variability remains within the range of natural disagreement among experts. Notably, GPT-4o tends to conflate emotional categories that differ primarily along the valence dimension, suggesting that valence is more challenging to infer from textual metadata than arousal, a difficulty also reflected in human annotations. This highlights a key limitation of our context-based method, in which GPT-4o annotations rely exclusively on pre-crawled textual metadata, therefore the accuracy and granularity of the annotations are limited by the quality and comprehensiveness of available textual information. Additionally, metadata-based inference rests on the majority cultural consensus encoded in text. While effective in most cases, this premise can mislabel “outlier” works whose affective intent departs from stylistic norms. 

A critical issue arising from our findings relates to the subjectivity of music emotion annotation tasks. Music emotion can be approached from two perspectives: perceived emotions (the emotions a listener believes the music is intended to convey) and induced emotions (the emotions the listener personally experiences while listening) [25]. Our methodology explicitly targets perceived emotions via textual contexts—cultural cues and genre conventions that shape listeners’ expectations before a note is heard—as a scalable proxy for annotation, reflecting a socially shared interpretation of what the music expresses rather than the idiosyncratic emotions it might induce. Even so, disagreement among human annotators reminds us that perceived emotion is not wholly objective, underscoring the inherent complexity in music emotion annotation. 

Furthermore, relying on synthetic labels produced by large language models such as GPT-4o raises important ethical questions. Automated annotation undoubtedly offers scale and cost efficiency, yet risks eroding the nuanced interpretive judgments human experts provide. Replacing human annotation entirely could introduce systematic biases and oversimplifications—concerns that are especially salient in a domain as subjective as music–emotion research. We therefore advocate for a hybrid annotation framework to combine AI-generated initial annotations with human expert oversight for ambiguous cases. For in- 

stance, GPT-4o can serve as a first-pass annotator: highconfidence predictions—those backed by clear contextual cues—can be accepted directly after sampling validation, while low-margin or “not-enough-information” cases are routed to human annotators. This division of labour harnesses the scalability of LLMs while preserving essential human insight, and concurrently addressing broader ethical concerns about the responsible use of synthetic data. 

Future work should focus on several key areas to address current limitations. First, refining prompt engineering by incorporating richer contextual details—such as comprehensive composer biographies, historical and cultural narratives, and program notes—may improve GPT4o’s ability to capture emotional nuances, particularly along the valence dimension. Second, enabling real-time online context retrieval would allow the model access to more dynamic and detailed metadata, potentially improving its discriminative capabilities. Third, adopting the aforementioned hybrid human–AI annotation framework would balance efficiency and quality while also partially addressing the ethical concerns about AI-driven data annotation. Finally, exploring multi-modal approaches that integrate audio features with contextual metadata could provide a more holistic and accurate assessment of musical emotions, further bridging the gap between automated and expert-level annotations. Such models may also extend coverage to brand-new or undocumented works by enabling direct emotion inference from raw audio, complementing our current metadata-dependent pipeline. 

Overall, although GPT-4o’s current performance does not entirely substitute for human expertise, its efficiency and scalability present a valuable opportunity to complement human annotations in large-scale Music Emotion research. Future work should refine prompting, enable online access, combine human–AI annotation, and integrate multimodal inputs to improve quality while addressing ethical and subjective challenges. 

## 6. CONCLUSION 

In this study, we presented a novel approach for automatic music emotion annotation using GPT-4o, leveraging contextual metadata extracted via web-crawling to label non-lyrical classical music. Our comprehensive evaluation, incorporating accuracy metrics, inter-annotator reliability measures, distributional similarity, and error analysis demonstrated that while GPT-4o does not yet match human expert accuracy, its outputs are stable and its variability falls within the range of natural human disagreement. Overall, our findings highlight the potential of LLM annotation as a scalable and cost-effective tool for large-scale music emotion annotation. 

155 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 7. REFERENCES 

- [1] Y.-H. Yang and H. H. Chen, “Machine recognition of music emotion: A review,” ACM Transactions on Intelligent Systems and Technology, vol. 3, no. 3, May 2012. 

- [2] A. Aljanaki, y.-h. Yang, and M. Soleymani, “Developing a benchmark for emotional analysis of music,” PLOS ONE, vol. 12, p. e0173392, 03 2017. 

- [3] A. Aljanaki, F. Wiering, and R. C. Veltkamp, “Studying emotion induced by music through a crowdsourcing game,” Information Processing & Management, vol. 52, no. 1, p. 115–128, Jan. 2016. 

- [4] L. N. Ferreira and J. Whitehead, “Learning to generate music with sentiment,” in Proceedings of the Conference of the International Society for Music Information Retrieval, Delft, Netherlands, 2019, pp. 384–390. 

- [5] H.-T. Hung, J. Ching, S. Doh, N. Kim, J. Nam, and Y.H. Yang, “Emopia: A multi-modal pop piano dataset for emotion recognition and emotion-based music generation,” in International Society for Music Information Retrieval Conference, 2021. 

- [6] M. Barthet, G. Fazekas, and M. Sandler, “Music emotion recognition: From content- to context-based models,” in From Sounds to Music and Emotions, M. Aramaki, M. Barthet, R. Kronland-Martinet, and S. Ystad, Eds. Berlin, Heidelberg: Springer Berlin Heidelberg, 2013, pp. 228–252. 

- [7] R. Delbouys, R. Hennequin, F. Piccoli, J. RoyoLetelier, and M. Moussallam, “Music mood detection based on audio and lyrics with deep neural net,” ArXiv, vol. abs/1809.07276, 2018. 

- [8] F. H. Rachman, R. Sarno, and C. Fatichah, “Music emotion detection using weighted of audio and lyric features,” in 2020 6th Information Technology International Seminar (ITIS), 2020, pp. 229–233. 

- [9] X. Hu, K. Choi, and J. S. Downie, “A framework for evaluating multimodal music mood classification,” Journal of the Association for Information Science and Technology, vol. 68, 2017. [Online]. Available: https://api.semanticscholar.org/CorpusID:45480061 

- [10] Y. Agrawal, R. G. R. Shanker, and V. Alluri, “Transformer-based approach towards music emotion recognition from lyrics,” in Advances in Information Retrieval: 43rd European Conference on IR Research, ECIR 2021, Virtual Event, March 28 – April 1, 2021, Proceedings, Part II, Berlin, Heidelberg, 2021, p. 167–175. 

- [11] X. Hu and J. S. Downie, “Exploring mood metadata: Relationships with genre, artist and usage metadata,” in International Society for Music Information Retrieval Conference, 2007. [Online]. Available: https://api. semanticscholar.org/CorpusID:16794525 

- [12] Q. Kong, B. Li, J. Chen, and Y. Wang, “Giantmidipiano: A large-scale midi dataset for classical piano music,” Transactions of the International Society for Music Information Retrieval, May 2022. 

- [13] D. Turnbull, L. Barrington, D. Torres, and G. Lanckriet, “Towards musical query-by-semantic-description using the cal500 data set,” in Proceedings of the 30th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, ser. SIGIR ’07. New York, NY, USA: Association for Computing Machinery, 2007, p. 439–446. 

- [14] P. L. Louro, H. Redinho, R. Santos, R. Malheiro, R. Panda, and R. P. Paiva, “Merge – a bimodal dataset for static music emotion recognition,” 2025. [Online]. Available: https://arxiv.org/abs/2407.06060 

- [15] Y. E. Kim, E. M. Schmidt, R. Migneco, B. G. Morton, P. Richardson, J. J. Scott, J. A. Speck, and D. Turnbull, “Music emotion recognition: A state of the art review,” in International Society for Music Information Retrieval Conference, 2010. 

- [16] P. Donnelly and A. Beery, “Evaluating large-language models for dimensional music emotion prediction from social media discourse,” in Proceedings of the 5th International Conference on Natural Language and Speech Processing (ICNLSP 2022). Trento, Italy: Association for Computational Linguistics, Dec. 2022, pp. 242–250. 

- [17] Y. E. Kim, E. M. Schmidt, and L. Emelle, “Moodswings: A collaborative game for music mood label collection,” in International Society for Music Information Retrieval Conference, 2008. [Online]. Available: https://api.semanticscholar.org/CorpusID: 14382686 

- [18] Z. Tan, D. Li, S. Wang, A. Beigi, B. Jiang, A. Bhattacharjee, M. Karami, J. Li, L. Cheng, and H. Liu, “Large language models for data annotation and synthesis: A survey,” in Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing. Miami, Florida, USA: Association for Computational Linguistics, Nov. 2024, pp. 930–957. 

- [19] F. Gilardi, M. Alizadeh, and M. Kubli, “Chatgpt outperforms crowd workers for text-annotation tasks,” Proceedings of the National Academy of Sciences of the United States of America, vol. 120, 2023. 

- [20] Z. He, C.-Y. Huang, C.-K. C. Ding, S. Rohatgi, and T.-H. K. Huang, “If in a crowdsourced data annotation pipeline, a gpt-4,” in Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems, ser. CHI ’24. New York, NY, USA: Association for Computing Machinery, 2024. 

- [21] S. Wang, Y. Liu, Y. Xu, C. Zhu, and M. Zeng, “Want to reduce labeling cost? GPT-3 can help,” in Findings of the Association for Computational Linguistics: 

156 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

EMNLP 2021. Punta Cana, Dominican Republic: Association for Computational Linguistics, Nov. 2021, pp. 4195–4205. 

- [22] D. Edmonds and J. Sedoc, “Multi-emotion classification for song lyrics,” in Proceedings of the Eleventh Workshop on Computational Approaches to Subjectivity, Sentiment and Social Media Analysis. Online: Association for Computational Linguistics, Apr. 2021, pp. 221–235. 

- [23] P. Donnelly and A. Beery, “Evaluating large-language models for dimensional music emotion prediction from social media discourse,” in Proceedings of the 5th International Conference on Natural Language and Speech Processing (ICNLSP 2022), M. Abbas and A. A. Freihat, Eds. Trento, Italy: Association for Computational Linguistics, dec 2022, pp. 242– 250. [Online]. Available: https://aclanthology.org/ 2022.icnlsp-1.28/ 

- [24] J. Russell, “A circumplex model of affect,” Journal of personality and social psychology, vol. 39, no. 6, pp. 1161–1178, 1980. 

- [25] A. Gabrielsson, “Emotion perceived and emotion felt: Same or different?” Musicae Scientiae, vol. 5, no. 1_suppl, pp. 123–147, 2001. 

157 

