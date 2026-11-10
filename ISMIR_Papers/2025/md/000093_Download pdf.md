---
paper_id: "000093"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706596/files/000093.pdf"
---

# IDENTIFICATION AND CLUSTERING OF UNSEEN RAGAS IN INDIAN ART MUSIC 

Parampreet Singh<sup>†</sup> , Adwik Gupta, Aakarsh Mishra, Vipul Arora Indian Institute of technology, Kanpur 

```
{params21,adwikg22,aakarsh21,vipular}@iitk.ac.in
```

## ABSTRACT 

Raga classification in Indian Art Music is an open-set problem where unseen classes may appear during testing. However, traditional approaches often treat it as a closed set problem, rejecting the possibility of encountering unseen classes. In this work, we try to tackle this problem by first employing an Uncertainty-based Out-Of-Distribution (OOD) detection, given a set containing known and unknown classes. Next, for the audio samples identified as OOD, we employ Novel Class Discovery (NCD) approach to cluster them into distinct unseen Raga classes. We achieve this by harnessing information from labelled data and further applying contrastive learning on unlabelled data. With thorough analysis, we demonstrate the influence of different components of the loss function on clustering performance and examine how varying openness affects the NCD task in hand. 

## 1. INTRODUCTION 

Ragas form the core melodic framework of Indian Art Music (IAM), each characterized by a distinct set of notes and improvisational rules that evoke specific emotions or moods [1]. Identifying Ragas in audio recordings has various applications, including music recommendation systems, cultural preservation, and music education [1]. While traditional methods would rely on handcrafted features and expert knowledge, recent advancements in deep learning have enabled automated Raga identification [2–6], where the shortage of labeled datasets remains a significant challenge. Labeling Raga audios in MIR is costly and labor-intensive, requiring domain expertise, while variations in style and recording conditions further complicate annotation. The problem of Raga identification is inherently an open-set problem, since the number of Ragas is not fixed, and new, unseen classes can emerge during testing, making classification more challenging. However, existing approaches have largely treated it as a closed-set problem [2, 3, 5, 6], limiting their ability to handle novel Raga classes during testing. 

> © P. Singh, A. Gupta, A. Mishra and V. Arora. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: P. Singh, A. Gupta, A. Mishra and V. Arora, “Identification and Clustering of Unseen Ragas in Indian Art Music”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

This work tackles the challenge of unknown Raga classes through the following approach. First, we perform Out-of-Distribution (OOD) detection by using uncertainty estimates from a model trained only on seen classes, identifying unseen Ragas without prior exposure to them. Next, we frame this as a Novel Class Discovery (NCD) problem, where the OOD Raga samples are assumed to belong to distinct, previously unseen classes and are clustered in a self-supervised manner. For NCD, we would generally have target classes <= training classes. So, we define openness of the NCD problem in a similar manner to openset [7] problems as: 



<!-- Start of picture text -->
2 ×  | trainin g  classes |<br>ONCD = 1 − � 2 × |training classes| + |test classes| (1)<br><!-- End of picture text -->

For our task, we define two disjoint subsets of Raga classes: a closed-set training set Ctrain consisting of 12 known Raga classes belonging to PIM [6] dataset (sourced from Prasar Bharati<sup>1</sup> audios), and a held-out target set Ctest comprising novel Raga classes that are entirely unseen during training, belonging to both Saraga (Hindustani) [8] and PIM [6] datasets. We analyze our approach on varying levels of openness on both the datasets. 

By utilizing this framework, we can effectively tap into the vast amount of freely available, unlabeled Raga recordings from online platforms like YouTube, significantly reducing dependence on manually labeled data. Our approach not only addresses the challenge posed by limited labeled datasets but also enhances the ability of MIR systems to recognize a broader range of Ragas, providing a scalable and adaptive solution for music classification. The codes, metadata, and other resources can be accessed at the dedicated Github Repository. 

## 2. RELATED WORKS 

## 2.1 OOD Detection 

Uncertainty estimation is a well-established field in machine learning that focuses on evaluating the confidence of model predictions for given test examples. Various approaches utilize uncertainty for identifying OOD samples. The work [9] proposes using maximum softmax probabilities as uncertainty indicators. Deep ensembles [10] com- 

> 1 Prasar Bharati is India’s public broadcasting agency, comprising Doordarshan Television Network and All India Radio. It maintains an extensive archive of Indian classical music recordings. 

797 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

bine multiple models to achieve robust uncertainty estimates. Bayesian Neural Networks offer principled uncertainty quantification through posterior distribution approximation. Other methods include techniques which train an auxiliary model to predict confidence scores [11–13]. Monte Carlo dropout (MC-dropout) [14] applies dropout during inference to simulate Bayesian sampling. In our work, we utilize uncertainty scores from MC-dropout for OOD detection, leveraging our pre-trained model without requiring additional training. 

## 2.2 Novel Class Discovery (NCD) 

Novel Class Discovery focuses on clustering unknown classes in unlabeled data while utilizing knowledge from labeled data of known classes [15–19]. Unlike semisupervised learning [20, 21], which assumes shared label spaces, or zero-shot learning [22, 23], which requires human-defined semantic attributes, NCD enables discovery of novel categories without such dependencies. This makes it particularly valuable for music applications, where new classes continuously emerge. 

In the image domain, NCD approaches have explored various contrastive learning techniques. Han et al. [18] introduces a graph-based approach for transferring knowledge from labeled to unlabeled data. Ranking statistics [16] have been introduced to construct negative samples for contrastive loss, while Neighborhood Contrastive Learning (NCL) [17] replaces ranking statistics with cosine similarity and proposes methods for generating hard negatives. 

## 2.3 Self-supervised Learning in Music Classification 

Several works in music classification have explored selfsupervised learning techniques. Differentiable ranking [24] techniques on spectrogram patches improve instrument classification and pitch estimation, though this approach is computationally intensive. [25] utilizes selfsupervised contrastive learning for singing voice analysis by applying audio-specific transformations such as timestretching and pitch-shifting to distinguish vocal timbre and expression. Another study, [26], integrates the Swin Transformer into a contrastive learning framework for music genre classification, demonstrating strong performance with limited labeled data. Additionally, [27] explores the reordering of shuffled spectrogram segments to improve learned audio representations for tasks such as instrument classification and pitch estimation. 

In our work, for NCD, we build on Neighborhood Contrastive Learning (NCL) [17] with tailored modifications in positive/negative pair generation and better transformations for consistency loss for our task. We train a supervised model to learn meaningful representations, and then use these representations to train another model in a selfsupervised manner to discover and categorize novel Raga classes in the unlabeled dataset. 



<!-- Start of picture text -->
softmax Classificationonuut<br>Audio ExtractorFeature S1U S OOD ID<br>f(.) 00D<br>Chromagram Clnsern<br>(.l pou)<br><!-- End of picture text -->

Figure 1. Block diagram illustrating the overall system workflow: audio input is first converted to a chromagram and processed by a feature extractor. Extracted features are then used for classification, out-of-distribution (OOD) detection, and subsequent clustering of OOD samples, enabling both in-distribution classification and unsupervised grouping of OOD data. 

## 3. METHOD 

The overall flow of the whole process is shown in Figure 1. We construct a labeled subset S<sup>l</sup> containing N number of 30-second audio clips x<sup>l</sup> i<sup>,sourcedfromthePIM</sup> dataset [6], each belonging to one of the c<sup>t</sup> predefined Raga classes. We pre-process to remove speech segments, discard audio clips shorter than 30 seconds, and subsequently extract tonic-normalized chromagram features [6], which forms the input to train the Raga classifier f (·). Formally, the labeled subset S<sup>l</sup> is defined as: S<sup>l</sup> = (x<sup>l</sup> i<sup>, ct</sup> i<sup>)</sup> Ni=1<sup>,</sup> where c<sup>t</sup> i<sup>∈Clcorresponds to its ground-truth Raga label.</sup> Similarly, we define an unlabeled subset of M samples S<sup>u</sup> = {x<sup>u</sup> i<sup>}M</sup> i=1<sup>,wherethe correspondingclasslabelsare</sup> assumed to be absent. The set of unseen classes C<sup>u</sup> is varied in size based on the openness of the problem. 

## 3.1 Supervised pre-training 

For classification, we split S<sup>l</sup> into training, validation, and test subsets, and train a CNN-LSTM model f (·) in a fully supervised manner using categorical cross-entropy loss. Once trained, this CNN-LSTM model serves as a feature extractor by removing the final softmax layer. The resulting feature extractor, denoted as ffeat(·), generates embeddings yi for both S<sup>l</sup> and S<sup>u</sup> , which are later used for OOD detection and NCD. 

## 3.2 OOD Detection 

Monte Carlo (MC) Dropout [14] is a technique for estimating epistemic uncertainty in deep learning models. Given a pre-trained CNN-LSTM classifier f (·), we enable dropout at inference time to approximate a Bayesian neural network. The predictive uncertainty is estimated by performing T stochastic forward passes, yielding a set of softmax outputs. By doing this, we assume that the network’s parameters Wt vary under different dropout masks. The variance of these predictions quantifies uncertainty values. Higher variance indicates greater uncertainty, suggesting a higher likelihood of the sample belonging to an OOD class. 

798 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 3.3 Novel Class Discovery 

## 3.3.1 BCE Loss 

For an input audio clip x<sup>u</sup> i ∈ S<sup>u</sup> , let yi<sup>u</sup> = ffeat(xi<sup>u)</sup> be the embeddings using the pre-trained feature extractor ffeat(·). The cosine similarity ε between a pair of feature embeddings (yi<sup>u, y</sup> j<sup>u) is given by:</sup> i<sup>)⊤y</sup> <mark>j</mark><sup>u</sup> ε(yi<sup>u, y</sup> j<sup>u) =(yu</sup> (2) ∥yi<sup>u∥∥y</sup> j<sup>u∥</sup> 

Now, using this, we assign a pairwise pseudo-label ti,j as: 



<!-- Start of picture text -->
ti,j =  1 �ε(yi u, y j u) ≥ δ �, (3)<br><!-- End of picture text -->

where δ is a similarity threshold that determines whether the two samples belong to the same latent class. Furthermore, if two audio samples x<sup>u</sup> i<sup>and xu</sup> j<sup>are formed by split-</sup> ting from the same audio file, they are assigned ti,j = 1 as they definitely belong to the same class. 

These pairwise pseudo-labels are used to train a selfattention encoder model g(·), which incorporates a multihead self-attention mechanism utilizing scaled dot-product attention, along with layer normalization and feedforward sub-layers. The network consists of multiple such stacked layers, with the input being the embedding yi<sup>uand its out-</sup> put denoted as zi<sup>u=g(y</sup> i<sup>u).ForBCElossbetweenthe</sup> given pair of inputs, we define normalized dot product between the output embeddings, given by pi,j: 



<!-- Start of picture text -->
(zi u)⊤z j u<br>pi,j = (4)<br>∥zi u∥· ∥z j u∥<br><!-- End of picture text -->

Al <mark>g</mark> orithm 1 al <mark>g</mark> :Novel Ra <mark>g</mark> a Clusterin <mark>g</mark> 

Require: OOD dataset S<sup>u</sup> , feature extractor ffeat(·) Require: Encoder model g(·), learning rates β, γ, temperature parameter τ 

- 1: Extract chromagram features from all x<sup>u</sup> i<sup>∈Su</sup> 2: Use ffeat(·) to compute embeddings yi<sup>u</sup> 3: for each pair (yi<sup>u, y</sup> j<sup>u) ∈Sudo</sup> 4: Compute cosine similarity ε(yi<sup>u, y</sup> j<sup>u)</sup> 

- 5: Assign pseudo-label ti,j based on threshold δ 

- 6: Compute pi,j using Eq: 4 

- 7: Compute BCE Loss ℓbce 

- 8: end for 

- 9: for each sample x<sup>u</sup> i<sup>do</sup> 

- 10: Apply time and volume shifts on x<sup>u</sup> i<sup>to getxˆu</sup> i 11: Compute transformed embeddings yˆi<sup>u= f(ˆxu</sup> i<sup>)</sup> 12: Compute Consistency Loss ℓmse 

- 13: end for 

- 14: for each sample x<sup>u</sup> i<sup>do</sup> 

- 15: Select H hardest negative samples ξm and positive samples ϕ 

- 16: Define contrastive loss ℓcl using positive and negative pairs 

- 17: end for 

- 18: Compute total loss: ℓ = ℓbce + βℓcl + γℓmse 

19: for epoch = 1 to E do 

- 20: Train g(·) using total loss ℓ 

21: end for 

22: Output: Trained model g(·) 

The similarities are ranked in ascending order, and the H least similar embeddings are selected as hard negatives: 

The BCE loss function is defined as: 



<!-- Start of picture text -->
ξh = argtoph(ζi u), ∀i. (8)<br><!-- End of picture text -->



<!-- Start of picture text -->
ℓbce = ti,j log(pi,j) + (1 − ti,j) log(1 − pi,j). (5)<br><!-- End of picture text -->

## 3.3.2 Consistency Loss 

To enforce consistency under transformations, we introduce a loss ensuring that an audio sample xi and its transformed versions x˜i yield similar outputs. We generate alternate views by time shifting, where for a given audio clip, we create two transformed versions by slightly shifting its start and end times (by 2 seconds) within the original audio, and by volume modification (increase and decrease). We then extract embeddings from the transformed audio x˜i, obtaining z˜i = g(f (˜xi)), and apply MSE loss as: 



<!-- Start of picture text -->
C l C u<br>ℓmse = C 1l � �zi l − z˜ i l �2 + C1 u � �zj u − z˜ j u �2 . (6)<br>i=1 j=1<br><!-- End of picture text -->

## 3.3.3 Contrastive Learning 

To define contrastive loss, we construct positive and negative pairs for our dataset. For negative pairs, each yi<sup>uis</sup> compared with all embeddings yn ∈ S<sup>u</sup> ∪ S<sup>l</sup> , using cosine similarity ε(yi<sup>u, yn).We then create a list ζ</sup> i<sup>u.</sup> 



<!-- Start of picture text -->
ζi u = list(ε(y i u, yn)), ∀{yi u ∈ Su}. (7)<br><!-- End of picture text -->

For positive pairs, similar to BCE loss, all the audio samples x<sup>u</sup> i<sup>andxu</sup> j<sup>originatingfromsameaudiofileare</sup> considered to belong to the same class and hence treated as positive pairs. Their corresponding embeddings zˆi<sup>uare</sup> stored in the set ϕ which is defined as: 



<!-- Start of picture text -->
ϕ = {zˆi u | z i u shares the same source audio file}<br><!-- End of picture text -->

We now define the contrastive loss ℓcl [17] as: 



<!-- Start of picture text -->
ℓcl = − k 1 zˆ�i u∈β log e ε(z i u,zˆ i u)/τ e+ ε( � z i u, z¯ zˆ ∈i u ξ ) m /τeε(z i u,z¯ m u )/τ  ,<br>(9)<br><!-- End of picture text -->

where τ is a temperature parameter that controls the concentration of similarity scores. This loss function optimizes embeddings by bringing each sample closer to its positive counterpart zˆi<sup>uwhilepushingitawayfromhard</sup> negatives z¯m<sup>u.Finally, get a unified objective function ℓby</sup> combining eq: 5,6,9: 



<!-- Start of picture text -->
ℓ = ℓbce + βℓcl + γℓmse. (10)<br><!-- End of picture text -->

Here, β and γ are the scaling hyperparameters, as the magnitude of these losses varies significantly. Proper tuning 

799 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

of these hyperparameters is critical for achieving optimal performance. This combined loss is used to train the selfattention encoder g(·), which learns to differentiate unseen raga classes in a self-supervised manner. This whole training process is explained in Algorithm 1. 

## 3.4 Clustering Techniques 

Given the embeddings zi from the encoder model g(·), we experiment with three different approaches for grouping the embeddings to assign predicted labels: (i) Computing a cosine similarity matrix across embedding pairs (zi, zj), and given a threshold th, grouping those with similarity ε > th into the same cluster. (ii) Applying K-means clustering to group the embeddings into K clusters. 

(iii) Reducing the dimensionality of embeddings using UMAP for visualization, followed by K-means clustering on the transformed representations. 

## 3.5 Evaluation Metrics 

We assess the quality of the clusters so formed using both label-independent and label-dependent evaluation metrics. (i) Silhouette Score(SS) [28] is a label-independent metric, which evaluates how well a data point is situated within its designated cluster in relation to other clusters, without considering the ground truth for those clusters. The score falls between -1 and 1. For well-separated clusters, SS comes out to be 1, and it is -1 for poorly formed clusters. (ii) Adjusted Rand Index (ARI) [29] is a label-dependent metric, which compares the similarity between predicted clusters and actual ground truth clusters, with an adjustment for random assignments. The score ranges from 0 to 1, where 1 represents perfect alignment with the ground truth. 

(iii) Mutual Information (MI) [30] measures the amount of information shared between the true clusters (c<sup>t</sup> ) and predicted clusters (c<sup>p</sup> ). It captures how much knowing the predicted cluster assignment reduces uncertainty about the true cluster assignment. The range of MI is not bounded, with higher values indicating that the predicting clustering is more aligned with the actual class structure. 

(iv) Clustering Accuracy (ACC) evaluates how well the predicted clusters align with the true labels. For each ground truth cluster c<sup>t</sup> , we identify the predicted cluster c<sup>p</sup> that has the highest overlap with c<sup>t</sup> . The subset of embeddings that belong to both c<sup>t</sup> and c<sup>p</sup> is represented as: 



<!-- Start of picture text -->
c pt = {zi | zi ∈ c p and zi ∈ c t }.<br><!-- End of picture text -->

Then, ACC for a given true cluster c<sup>t</sup> is then computed as: 



<!-- Start of picture text -->
ACC(c t ) = | cpt |<br>|c t | × 100.<br><!-- End of picture text -->

Misclassified points are those that do not belong to any matched cluster. Furthermore, if a predicted cluster c<sup>p</sup> is mapped to multiple true clusters c<sup>t</sup> , the clustering is considered invalid, and accuracy, along with other performance metrics, is not calculated. 

## 4. EXPERIMENTAL RESULTS 

The labeled dataset S<sup>l</sup> consists of 141 audio files sourced from PIM [6] dataset, segmented into 5,734 audio samples, with a total duration of approximately 47.78 hours. A CNN-LSTM model f (·) is trained in a supervised manner on this dataset for multi-class classification across 12 Raga classes, achieving an F1-score of 0.89 through crossvalidation. This trained model serves as a feature extractor for downstream tasks, where representations for OOD detection and NCD are obtained by extracting features from different depths of the network. We construct another set S<sup>u</sup> for which the Raga labels are discarded, treating it as unlabeled data. We conduct a range of OOD and NCD experiments using both the PIM [6] and Saraga [8] (Hindustani) datasets at different stages, as summarized in Table 1. 

|Experiment|Dataset|Description|
|---|---|---|
|OOD detec-<br>tion|PIM/<br>Saraga|Carry out OOD Detection<br>for both datasets separately<br>usingf(·); results in Table 2|
|Feature abla-<br>tion|PIM|Compare<br>Chromagram<br>vs<br>Melody [31] vs MERT [32]<br>features; results in Table 3|
|Loss compo-<br>nent ablation|PIM|Testℓbce/ℓcl/ℓmse contribu-<br>tions; results in Table 5|
|Clustering<br>comparison|PIM/<br>Saraga|Evaluate Cosine-sim vs K-<br>Means vs UMAP+K-means;<br>results in Table 4|
|Openness<br>study|PIM|Analyze<br>performance<br>at<br>openness = 0.09 & 0.18;<br>results in Table 6|



Table 1. Summary of all experimental setups, datasets, and their corresponding result locations in the paper. 

|Metric/Dataset|Saraga|PIM|
|---|---|---|
|OOD Accuracy|85.6%|80.87%|



Table 2. Comparison of OOD detection Accuracy for Saraga and PIM datasets 

## 4.1 OOD 

For OOD detection, we select test files from five unseen classes in the PIM and Saraga datasets, prioritizing those with higher representation. From PIM, we use 41 audio files, resulting in 2,435 audio clips (20.29 hours), belonging to 5 Raga classes: Bageshri, Bhopali, Jog-Kauns, Mishra-Khamaj, and Puriya-Kalyan. From Saraga, 14 audio files, yielding 1,136 audio clips (9.46 hours) belonging to 5 Raga classes: Bhopali, Bhimpalasi, Marwa, Shree, Todi. An equal number of files from S<sup>l</sup> (only from PIM dataset) is included for comparison. The f (·) model is trained with MC-dropout, with T=50 forward passes for each xi, and a variance-based threshold is applied to classify samples as OOD or in-distribution. Results, presented 

800 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

in Table 2, demonstrate OOD detection performance. The model performs better on Saraga for OOD detection, the reason being since the f (·) model is trained on the PIM dataset, the OOD recordings from PIM may share acoustic similarities with the training data, making OOD detection more challenging. In contrast, the Saraga dataset, recorded in different acoustic environments, serves as a more distinct and thus easier target for OOD detection. 

## 4.2 Feature Ablation 

For S<sup>l</sup> , we extract embeddings using the pre-trained MERT model [32], melody-based embeddings from [31], and the feature extractor ffeat(·), which extracts embeddings from the penultimate layer of CNN-LSTM classifier f (·). These embeddings are then clustered using cosine similarity, as described in Section 3.4. 

The clustering outcomes for S<sup>l</sup> are summarized in Table 3. The results indicate that embeddings from both MERT and melody-based models yield subpar performance, even when evaluated with label-independent metrics. In contrast, ffeat(·) provides significantly better clustering results. So, we adopt ffeat(·) as the feature extractor for the remainder of our study. 

|Metric|MERT|Melody|ffeat(·)|
|---|---|---|---|
|SS|0.13|-0.01|0.54|
|ARI|0.00|0.08|0.83|
|MI|0.02|0.22|1.99|
|ACC|11.15|25.04|90.05|



Table 3. Comparison of MERT, Melody extraction tool (Mel), and ffeat(·) for clustering using k-means on S<sup>l</sup> 

## 4.3 NCD 

## 4.3.1 Comparison with baseline 

For the baseline, clustering is performed directly on the embeddings yi using the three clustering methods described in Section 3.4. In our proposed approach, we train the encoder model g(·) using the combined loss ℓ (eq: 10) on both the PIM and Saraga datasets. The resulting clustering performance for both baseline and proposed methods is presented in Table4. As expected, the baseline results for S<sup>u</sup> are significantly worse than those for the labeled dataset. This outcome is anticipated since the feature extractor ffeat(·) is not trained on S<sup>u</sup> , and S<sup>u</sup> and S<sup>l</sup> contain disjoint Raga classes. Consequently, clustering performance is poor for both label-dependent and labelindependent clustering metrics under the baseline. 

Fig. 2 shows the confusion matrix for classification of 5 unknown Raga classes: Bhopali, Bageshri, Jog-Kouns, Mishra-Khamaj, and Puriya-Kalyan out of PIM dataset. We compute f1-scores based on the confusion matrix, and observe that the model performs well for Bageshri (F1: 0.85) and Bhopali (F1: 0.92), which are more distinct and straightforward Ragas. However, it struggles with MishraKhamaj (F1: 0.51), Jog-Kouns (F1: 0.69), and Puriya- 

Kalyan (F1: 0.60). These Ragas, being Mishra (mixed) Ragas, inherently share musical similarities with more than one Ragas in their structure itself, making them more challenging to distinguish and often leading to confusion for the model. This highlights the intrinsic complexity of Mishra Ragas and emphasizes the need for more refined approaches to accurately classify such Ragas. 



<!-- Start of picture text -->
6 00<br>422 3 42 88 0<br>5 00<br>7 625 10 27 23<br>4 00<br>2 0 335 28 154<br>3 00<br>3 7 9 150 44 2 00<br>1 00<br>7 25 50 78 282<br>0<br>Bg Bp JK MK PK<br>Predicted Classes<br>Bg<br>Bp<br>JK<br>True Classes<br>MK<br>PK<br><!-- End of picture text -->

Figure 2. Confusion matrix for S<sup>u</sup> showing classification performance on the PIM dataset for five Ragas: Bhopali (Bp), Bageshri (Bg), Jog-Kouns (JK), MishraKhamaj (MK), and Puriya-Kalyan (PK). 

For the Saraga dataset, trained on Raga Bhopali, Bhimpilasi, Marwa, Todi, and Shree in their set S<sup>u</sup> , the confusion matrix (not shown) reveals significant overlap between Raag Shree and Marwa. This can be attributed to their structural similarities as they both belong to the Marwa thaat<sup>2</sup> , share common notes with one exception, omit Pancham<sup>3</sup> note in Ascent (Aaroh), and are sung at the same time of the day. We also find that the audio recordings for these 2 Ragas feature the same singers in the dataset, and also from the same concert, leading to shared tonal and acoustic characteristics, which may have caused them to cluster closely and, hence, poorer clustering performance compared to the PIM dataset. Another thing is that in Saraga dataset, the representation of each Raga class is limited to max 3 audio files, wherever in PIM, we have at least 7 audio files for each of the unlabeled classes. 

## 4.3.2 Loss component Ablation 

To understand the individual contributions of different components in our final loss function ℓ, we train the encoder model g(·) separately using each component—Binary Cross-Entropy (BCE) loss (ℓbce), Contrastive loss (ℓcl), their sum (ℓcl+bce), and the full combined loss ℓ (Eq. 10). For this comparison, we apply K- means clustering on the resulting embeddings using only the PIM dataset. The clustering performance for each setup is summarized in Table5. 

> 2 A thaat is a parent scale in Hindustani Music, that defines the set of notes used in ragas. If two ragas belong to the same thaat, they are likely to share similar notes, making them more acoustically similar. 

> 3 The fifth note in the scale; when omitted in the Aaroh of ragas from the same Thaat, it further reduces their melodic distinctiveness. 

801 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

|Dataset|ClusteringM|ethods|SS|ARI|MI|ACC(%)|
|---|---|---|---|---|---|---|
||Cosine Similarity|Baseline<br>Proposed|0.22<br>0.75|0.50<br>0.58|0.87<br>1.17|58.96<br>72.10|
|PIM|KM|Baseline|0.36|0.48|0.79|70.75|
||-eans|Proposed|0.85|0.64|0.94|79.34|
||UMAP|Baseline|0.63|0.53|0.83|71.48|
|||Proposed|0.79|0.60|0.85|72.99|
||Ci Siilit|Baseline|0.15|0.30|0.65|53.61|
||osne mary|Proposed|0.71|0.43|0.86|78.37|
|Saraa|K-Means|Baseline|0.40|0.41|0.79|75.44|
|g||Proposed|0.82|0.44|0.82|81.04|
||UMAP|Baseline|0.60|0.44|0.81|73.85|
|||Proposed|0.66|0.47|0.85|78.88|



Table 4. Performance comparison of clustering methods on PIM and Saraga Datasets 

|Metric|ℓcl|ℓbce|ℓcl+bce|ℓ|Metric|ONCD = 0.09|ONCD = 0.18|
|---|---|---|---|---|---|---|---|
|SS|0.39|0.59|0.62|0.85|SS|0.85|0.50|
|ARI|0.52|0.55|0.59|0.64|ARI|0.64|0.44|
|MI|0.76|0.84|0.87|0.94|MI|0.94|0.83|
|ACC(%)|70.16|75.43|76.04|79.34|ACC(%)|79.34|55.68|



Table 5. Comparison of clustering metrics for training g(·) using ℓcl, ℓbce, ℓcl+bce, and l, after clustering zi<sup>uusing K-</sup> means clustering 

Table 6. Clustering Comparison for Different Levels of Openness Eq: 1 (ONCD ) 

We observe that ℓcl forms poor clusters, as evident from the plot (not shown), where we see all the samples separated like they are plotted along the boundary of a circle. It has been explained by [33] also that contrastive Learning (CL) pushes dissimilar samples apart without preserving semantic structure, sometimes grouping unrelated samples while separating similar ones, which is evident here also. BCE performs better by focusing on confidently similar pairs and ignoring uncertain ones. ℓcl+bce combines the strengths of both, further improving clustering. Adding MSE enhances semantic consistency, making ℓ the most effective, outperforming all three across all metrics. 

## 4.3.3 Openness Study 

We analyze the impact of openness on clustering performance. As defined in Section 1, openness is determined by the number of labeled classes |C<sup>l</sup> | and the number of unseen classes |C<sup>u</sup> |. In our case, |C<sup>l</sup> | is fixed to 12, but we now experiment with values 5 and 12 for |C<sup>u</sup> |, resulting in openness values of 0.09 and 0.18, respectively for PIM dataset. A higher openness value corresponds to a more challenging problem, as is observed in Table 6. We observe a significant drop in performance, particularly in ACC, suggesting that some classes are being clustered poorly or even randomly, despite a relatively good SS score. This may be due to reduced representation for certain classes as the number of samples per class decreases. Increasing the sample size could potentially improve clustering performance. 

Our results show that the proposed method achieves clustering quality comparable to supervised approaches, 

which is valuable for MIR tasks like Raga Identification where labeled data is limited. It enables scalable use of unlabeled recordings, expanding Raga datasets without heavy reliance on manual labeling. 

## 5. CONCLUSION AND FUTURE SCOPE 

In this study, we propose a novel approach for identifying and clustering unseen Raga classes in Indian Art Music. We first use Uncertainty Estimation for Out-ofDistribution (OOD) detection on both the Saraga and PIM datasets, effectively distinguishing unknown Ragas from known ones. Then, we apply a contrastive learning-based Novel Class Discovery (NCD) method in a self-supervised setting to cluster the OOD Ragas into distinct clusters. Our approach demonstrates strong cross-dataset generalization, as features extracted from PIM were successfully used to train and cluster for Saraga. Additionally, we analyze the impact of varying openness values, showing that higher openness yields poorer clustering performance, highlighting the need for further improvements. 

Future work can focus on better handling of Mishra Ragas to reduce confusion with parent Ragas. Expanding Raga Identification datasets, exploring multimodal or hierarchical learning could enhance adaptability and may help mitigate performance drops at higher openness. Framing the task as a General Class Discovery (GCD) task, where the model learns from both labeled and unlabeled sets simultaneously, could be a good future direction. 

802 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 6. ACKNOWLEDGEMENTS 

This work was supported by Prasar Bharati, India’s public broadcasting agency. 

- [13] S. Kumar, P. Singh, and V. Arora, “Confidenceenhanced models for indian art music analysis,” in 2025 IEEE International Conference on Acoustics, Speech, and Signal Processing Workshops (ICASSPW), 2025. 

## 7. REFERENCES 

- [1] X. Serra, “The computational study of a musical culture through its digital traces,” Acta Musicologica, vol. 89, no. 1, p. 24–44, Jun. 2017. 

- [2] S. Chowdhuri, “Phononet: multi-stage deep neural networks for raga identification in hindustani classical music,” in ICMR, 2019. 

- [3] S. Paschalidou and I. Miliaresi, “Multimodal Deep Learning Architecture for Hindustani Raga Classification,” Sensors & Transducers, vol. 261, no. 2, pp. 77– 86, Feb. 2024. 

- [4] A. A. Bidkar, R. S. Deshpande, and Y. H. Dandawate, “A north indian raga recognition using ensemble classifier,” IJEET, vol. 12, no. 6, pp. 251–258, 2021. 

- [5] S. T. Madhusudhan and G. V. Chowdhary, “Deepsrgm - sequence classification and ranking in indian classical music via deep learning,” ArXiv, vol. abs/2402.10168, 2024. [Online]. Available: https: //api.semanticscholar.org/CorpusID:208334841 

- [6] P. Singh and V. Arora, “Explainable deep learning analysis for raga identification in indian art music,” 2024. [Online]. Available: https://arxiv.org/abs/2406. 02443 

- [7] W. J. Scheirer, A. de Rezende Rocha, A. Sapkota, and T. E. Boult, “Toward open set recognition,” IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 35, no. 7, pp. 1757–1772, 2013. 

- [8] A. Srinivasamurthy, S. Gulati, R. Caro Repetto, and X. Serra, “Saraga: Open datasets for research on indian art music,” Empirical Musicology Review, vol. 16, no. 1, p. 85–98, Dec. 2021. 

- [9] D. Hendrycks and K. Gimpel, “A baseline for detecting misclassified and out-of-distribution examples in neural networks,” arXiv preprint arXiv:1610.02136, 2016. 

- [10] B. Lakshminarayanan, A. Pritzel, and C. Blundell, “Simple and scalable predictive uncertainty estimation using deep ensembles,” Advances in neural information processing systems, vol. 30, 2017. 

- [11] C. Corbière, N. Thome, A. Bar-Hen, M. Cord, and P. Pérez, “Addressing failure prediction by learning model confidence,” Advances in Neural Information Processing Systems, vol. 32, 2019. 

- [12] C. Corbiere, N. Thome, A. Saporta, T.-H. Vu, M. Cord, and P. Perez, “Confidence estimation via auxiliary models,” IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 44, no. 10, pp. 6043–6055, 2021. 

- [14] Y. Gal and Z. Ghahramani, “Dropout as a bayesian approximation: Representing model uncertainty in deep learning,” in international conference on machine learning. PMLR, 2016, pp. 1050–1059. 

- [15] Y. J. Lee and K. Grauman, “Object-graphs for contextaware category discovery,” in 2010 IEEE Computer Society Conference on Computer Vision and Pattern Recognition, 2010, pp. 1–8. 

- [16] K. Han, S.-A. Rebuffi, S. Ehrhardt, A. Vedaldi, and A. Zisserman, “Automatically discovering and learning new visual categories with ranking statistics,” in International Conference on Learning Representations, 2020. 

- [17] Z. Zhong, E. Fini, S. Roy, Z. Luo, E. Ricci, and N. Sebe, “Neighborhood contrastive learning for novel class discovery,” in 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2021, pp. 10 862–10 870. 

- [18] K. Han, A. Vedaldi, and A. Zisserman, “Learning to discover novel visual categories via deep transfer clustering,” 2019 IEEE/CVF International Conference on Computer Vision (ICCV), pp. 8400–8408, 2019. [Online]. Available: https://api.semanticscholar.org/ CorpusID:201646290 

- [19] Y.-C. Hsu, Z. Lv, J. Schlosser, P. Odom, and Z. Kira, “Multi-class classification without multi-class labels,” in International Conference on Learning Representations, 2019. [Online]. Available: https: //openreview.net/forum?id=SJzR2iRcK7 

- [20] X. Yang, Z. Song, I. King, and Z. Xu, “A survey on deep semi-supervised learning,” IEEE Transactions on Knowledge and Data Engineering, vol. 35, no. 9, pp. 8934–8954, 2023. 

- [21] Y. Yang, N. Jiang, Y. Xu, and D.-C. Zhan, “Robust semi-supervised learning by wisely leveraging openset data,” IEEE Transactions on Pattern Analysis and Machine Intelligence, pp. 1–15, 2024. 

- [22] Y. Xian, B. Schiele, and Z. Akata, “Zero-shot learning — the good, the bad and the ugly,” in 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2017, pp. 3077–3086. 

- [23] Y. Xian, C. H. Lampert, B. Schiele, and Z. Akata, “Zero-shot learning—a comprehensive evaluation of the good, the bad and the ugly,” IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 41, no. 9, pp. 2251–2265, 2019. 

803 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [24] A. N. Carr, Q. Berthet, M. Blondel, O. Teboul, and N. Zeghidour, “Self-supervised learning of audio representations from permutations with differentiable ranking,” IEEE Signal Processing Letters, vol. 28, pp. 708–712, 2021. 

- [25] H. Yakura, K. Watanabe, and M. Goto, “Selfsupervised contrastive learning for singing voices,” IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 30, pp. 1614–1623, 2022. 

- [26] H. Zhao, C. Zhang, B. Zhu, Z. Ma, and K. Zhang, “S3t: Self-supervised pre-training with swin transformer for music classification,” in ICASSP 2022 - 2022 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2022, pp. 606–610. 

- [27] E. Fonseca, D. Ortego, K. McGuinness, N. E. O’Connor, and X. Serra, “Unsupervised contrastive learning of sound event representations,” in ICASSP 2021 - 2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2021, pp. 371–375. 

- [28] P. J. Rousseeuw, “Silhouettes: A graphical aid to the interpretation and validation of cluster analysis,” Journal of Computational and Applied Mathematics, vol. 20, pp. 53–65, 1987. 

- [29] N. X. Vinh, J. Epps, and J. Bailey, “Information theoretic measures for clusterings comparison: Variants, properties, normalization and correction for chance,” Journal of Machine Learning Research, vol. 11, no. 95, pp. 2837–2854, 2010. [Online]. Available: http://jmlr.org/papers/v11/vinh10a.html 

- [30] A. Strehl and J. Ghosh, “Cluster ensembles - a knowledge reuse framework for combining multiple partitions,” Journal of Machine Learning Research, vol. 3, pp. 583–617, 01 2002. 

- [31] K. R. Saxena and V. Arora, “Interactive singing melody extraction based on active adaptation,” IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 32, pp. 2729–2738, 2024. 

- [32] Y. LI, R. Yuan, G. Zhang, Y. Ma, X. Chen, H. Yin, C. Xiao, C. Lin, A. Ragni, E. Benetos, N. Gyenge, R. Dannenberg, R. Liu, W. Chen, G. Xia, Y. Shi, W. Huang, Z. Wang, Y. Guo, and J. Fu, “MERT: Acoustic music understanding model with large-scale self-supervised training,” in The Twelfth International Conference on Learning Representations, 2024. 

- [33] F. Wang and H. Liu, “Understanding the behaviour of contrastive loss,” in Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, 2021, pp. 2495–2504. 

804 

