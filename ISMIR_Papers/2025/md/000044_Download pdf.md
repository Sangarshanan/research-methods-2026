---
paper_id: "000044"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706420/files/000044.pdf"
---

SLAP: SIAMESE LANGUAGE-AUDIO PRETRAINING WITHOUT NEGATIVE SAMPLES FOR MUSIC UNDERSTANDING 

Julien Guinot<sup>∗,1,2</sup> Alain Riou<sup>∗,3</sup> Elio Quinton<sup>2</sup> György Fazekas<sup>1</sup> 

1 Centre for Digital Music, Queen Mary University of London, U.K. 

2 Music & Audio Machine Learning Lab, Universal Music Group, London, U.K. 

3 LTCI, Télécom-Paris, Institut Polytechnique de Paris, France 

> ∗Equal contribution, correspondence to `j.guinot@qmul.ac.uk` 

# ABSTRACT 

Joint embedding spaces have significantly advanced music understanding and generation by linking text and audio through multimodal contrastive learning. However, these approaches face large memory requirement limitations due to relying on large batch sizes to effectively utilize negative samples. Further, multimodal joint embedding spaces suffer from a modality gap wherein embeddings from different modalities lie in different manifolds of the embedding space. To address these challenges, we propose Siamese Language-Audio Pretraining (SLAP), a novel multimodal pretraining framework that allows learning powerful representations without negative samples. SLAP adapts the Bootstrap Your Own Latent (BYOL) paradigm for multimodal audio-text training, promoting scalability in training multimodal embedding spaces. 

We illustrate the ability of our model to learn meaningful relationships between music and text — specifically, we show that SLAP outperforms CLAP on tasks such as text-music retrieval and zero-shot classification. We also observe competitive downstream performance on several MIR tasks, including with larger or supervised models (genre and instrument classification, auto-tagging). Additionally, our approach has attractive properties, such as a quantifiably reduced modality gap and improved robustness to batch size variations on retrieval performance. Finally, its novel formulation unlocks large-scale training on a single GPU through gradient accumulation. 

# 1. INTRODUCTION 

Joint embedding spaces for text and audio have been foundational in recent developments in music understanding and generation. Such spaces are typically learned via Multimodal Contrastive Learning (MCL), which optimizes a pair of encoders for maximal similarity between positive pairs, while minimizing similarity for negative pairs [1, 2]. 

> © J. Guinot, A. Riou, E. Quinton, and G. Fazekas.. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: J. Guinot, A. Riou, E. Quinton, and G. Fazekas., “SLAP: Siamese Language-Audio Pretraining Without Negative Samples for Music Understanding”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

Though widely successful, some drawbacks have been identified with this method. Recent trends for joint multimodal embedding spaces have emphasized fine-grained understanding between individual text tokens and individual timesteps of music [3, 4] and need for text augmentation strategies to alleviate the lack of large scale datasets [5, 6]. A modality gap emerging from the contrastive approach has been observed, where modalities lie in separate manifolds of the embedding space [7, 8]. This leads to “joint” representations not being truly joint, potentially harming performance. Importantly, contrastive approaches face an inherent scalability issue. Their formulation makes them 1) dependent on batch size for representation quality and 2) more difficult to scale than masked modelling approaches due to the formulation of the contrastive loss [9]. These drawbacks pose issues for foundation models, which by usage should be scalable for adaptation on large-scale datasets. Further, text-music spaces are a many-to-many space. I.e., there is often no one single corresponding appropriate caption for a piece of music, and vice-versa. 

Inspired by recent advances in Self-Supervised Learning for images and general audio [10, 11], we propose SLAP, Siamese Language Audio Pretraining. We adapt Bootstrap Your Own Latent (BYOL) [10] as a jointembedding pretraining approach without negative samples to multimodal text-audio pretraining. We show that SLAP alleviates both the scalability issues and the modality gap inherent to MCL. Our contributions are: 

1. We introduce a scalable, hyperparameter-robust approach to language-audio pretraining which does not require negative pairs to learn strong representations. 

2. We outperform comparable contrastive models on retrieval and downstream probing. 

3. We show that our approach significantly decreases the modality gap between audio and text embeddings compared to contrastive approaches. 

4. Our approach enables larger batch sizes via gradient accumulation, which was previously inaccessible due to the formulation of the contrastive loss. 

To facilitate further research in this direction, we make our code available.<sup>1</sup> 

1 `https://github.com/Pliploop/SLAP` 

382 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

# 2. BACKGROUND 

# 2.1 Multimodal Contrastive Learning 

In contrastive learning, models learn representations by maximizing the similarity between two views of an input while minimizing its similarity with negative samples, typically by optimizing an InfoNCE loss [12]. While these views are typically crafted by randomly applying transforms to the input data points [12, 13], Multimodal Contrastive Learning (MCL) instead relies on paired data from different modalities, such as text-image [1], textvideo [14], audio-image [15], text-music [16,17], and textaudio [2,18]. Contrastive learning spanning more than two modalities has also been investigated [19–21]. 

MCL has been leveraged to great extent in multiple modalities for tasks such as understanding [1], retrieval [16], and generation [22], with many multimodal foundation models emerging from the approach [23, 24]. 

MCL, specifically text-audio and text-music contrastive learning, has also been widely adopted in the field of audio and music. Notably, CLAP [2] and subsequent developments building upon it have demonstrated high audio understanding performance [3, 5, 18, 25]. Learned audio-text representations enable effective text-audio and audio-text retrieval by leveraging similarity metrics between modalities. Beyond catalogue navigation, these capabilities support retrieval-augmented audio captioning [26, 27]. In music-text representation learning, MusCALL [16] and MuLan [17] have both achieved strong performance on downstream tasks such as text-music retrieval, music classification, and zero-shot classification. Finally, joint embedding text-audio spaces have also been leveraged to condition audio and music generative models [28–32]. 

# 2.2 Limitations of contrastive learning 

Despite its widespread success, contrastive learning faces notable limitations, typically related to its reliance on negative samples. First, ensuring a diverse and representative set of negative samples is crucial for stable training, which usually necessitates a large batch size B in practice. However, computing the InfoNCE loss requires storing a B ×B matrix of pairwise similarities on a single GPU, which limits scalability. SigLIP [33] addresses this by replacing the softmax in the criterion with a sigmoid, making distributed training more tractable, though it still demands costly interdevice communication. In addition, contrastive learning implicitly assumes a uniform prior for the data distribution, which is detrimental in long-tailed scenarios [34]. 

MCL, more specifically, also suffers from an issue often referred to as the modality gap, where embeddings from different modalities occupy non-overlapping cone manifolds in the joint latent space [8]. [35] observe a relationship between this gap and the initial model weights and loss temperature, while recent findings suggest this problem could be intrinsic to the loss formulation itself [7]. 

# 2.3 Self-supervised learning without negative samples 

Recent advances in Self-Supervised Learning (SSL) have demonstrated that contrastive learning can be outperformed by alternative approaches that do not rely on negative samples, at least in unimodal settings [10, 36, 37]. 

In particular, BYOL [10] leverages an asymmetric architecture composed of a context encoder and a target encoder. Two augmented views are passed through their respective encoder, and a predictor network maps the context output to match the target’s. Crucially, the target encoder is not trained via gradient descent but updated as an Exponential Moving Average (EMA) of the context encoder, which effectively avoids representation collapse [38]. 

This approach, as well as subsequent works relying on Transformer-based architectures, do not suffer from the conceptual limitations described in Section 2.2, and achieve state-of-the-art performance in image [37, 39, 40] and audio [11, 41–43] representation learning. However, the reliance on EMA requires the context and target encoders to share the same architecture, hindering the direct application of these methods to multimodal scenarios. 

In this work, we draw inspiration from these ideas to propose a novel multimodal SSL framework that eliminates the need for negative samples while addressing the architectural limitations imposed by EMA-based methods. 

# 3. SIAMESE LANGUAGE-AUDIO PRETRAINING 

The training pipeline of SLAP is depicted in Figure 1. Consider an audio encoder EA mapping samples xA of length TA from the audio space to a latent audio representation za so that EA : xA ∈ R<sup>TA</sup> �→ zA ∈ R<sup>d</sup> and a text encoder mapping N tokens to a tex latent space ET : xt ∈ N<sup>N</sup> �→ zt ∈ R<sup>d</sup> . 

Audio and text encoders project inputs into respective modalities’ latent spaces. For each modality, we define a context encoder (E) and an Exponential Moving Average (EMA)-updated target encoder E<sup>¯</sup> with EMA rate τ : 



<!-- Start of picture text -->
E¯ = τ ¯E + (1 − τ )E. (1)<br><!-- End of picture text -->

For each modality, we also incorporate a predictor P, which has been shown to be necessary to prevent trivial solutions and collapse [10, 38]. The predictor of each branch processes the output z of the respective context encoder and aims to predict the output z¯ of the target branch of both modalities. We notate q the output of the predictor: 



<!-- Start of picture text -->
qA = PA(zA), qT = PT (zT ). (2)<br><!-- End of picture text -->

The model is trained by minimizing intermodal losses, defined as the cosine distance between the queries q and targets z¯ from different modalities: 



<!-- Start of picture text -->
q A · ¯zT q T · ¯zA<br>LA→T = 1 − ∥qA∥∥z¯T ∥ , LT →A = 1 − ∥qT ∥∥z¯A∥ , (3)<br><!-- End of picture text -->

where ∥· ∥ denotes the L2 norm. 

Additionally, we introduce intramodal losses between the queries q and targets z¯ within each modality, which 

383 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
Audio<br>Audios<br>agg<br>agg<br>EMA<br>sg( ⋅ )<br>a gg<br>Caption<br>Captions<br>"A blaring metal<br>track with stompy agg<br>kicks and distorted<br>"A blaring metal agg chuggy guitar."<br>track with stompy<br>kicks  and distorted EMA<br>c huggy guitar." EMA sg( ⋅ )<br>agg<br><!-- End of picture text -->

Figure 1. (a) CLAP: The multimodal contrastive loss LCLAP is optimized between batches of audio/text pairs. (b) SLAP: For each audio/text pair, we compute a query q and a target z¯ for each modality, then optimize both the intermodal losses LA→T and LT →A and the intramodal losses LA and LT between the queries and the targets. As indicated by the stopgradient operator sg, the gradient flows only through the context branches, while the target encoders are updated via EMA. 

we find to empirically yield stronger retrieval performance than using intermodal losses alone (see Section 5.6): 



<!-- Start of picture text -->
q A · ¯zA q T · ¯zT<br>LA = 1 − LT = 1 − (4)<br>∥qA∥∥z¯A∥ , ∥qT ∥∥z¯T ∥ .<br><!-- End of picture text -->

The final loss is a combination of intramodal and intermodal losses with a weighing term λ ∈ [0, 1]: 



<!-- Start of picture text -->
L = λ�LA→T + LT →A� + (1 − λ)�LA + LT �. (5)<br><!-- End of picture text -->

This approach does not require any complex machinery to prevent collapse other than an EMA update of encoders from both modalities and the addition of the symmetrybreaking predictor. 

|Task|Dataset|# clips|Clip length|
|---|---|---|---|
|Training|PrivateCaps|260k|full length|
|Rtil|MusicCaps [32]|5.5k|10 seconds|
|ereva|Song Describer [44]|1k|2 minutes|
||GTZAN [45]|1k|30 seconds|
|Probing/ZS|MagnaTagATune [46]|25k|30 seconds|
||OpenMic [47]|20k|10 seconds|



Table 1. Datasets used for training, retrieval, and downstream tasks (probing and zero-shot classification). 

30-second music clips with 50 associated tags. Additionally, we employ the OpenMic dataset [47] for fine-grained instrument tagging, containing annotations for instrument presence over 20,000 snippets. 

# 4.2 Model architecture 

# 4. EXPERIMENTAL SETUP 

# 4.1 Datasets 

The list of datasets used in this work is reported in Table 1. We train SLAP on an internal private dataset of 260,000 pairs of full-length production-quality music tracks and professionally annotated captions (PrivateCaps [16]). Our retrieval testing datasets include two music-caption pair datasets. Specifically, we use MusicCaps [32] and the Song Describer Dataset [44] for text-music retrieval performance evaluation. MusicCaps contains 5,521 music clips, each accompanied by a detailed text description. The Song Describer Dataset includes 2-minute-long permissively licensed music clips with crowd-sourced singlesentence captions. 

For zero-shot classification and downstream probing performance (See Sections 5.2, 5.3), we use the GTZAN dataset [45] for music genre classification, which contains 1,000 audio tracks, each 30 seconds long, spanning 10 genres. We also use the MagnaTagATune (MTAT) dataset [46], an automatic tagging dataset consisting of 25,000 

We use the same architecture as in LAION-CLAP [49], namely HTS-AT [50] for the audio encoder and RoBERTa [51] for the text encoder. This backbone configuration leads to an overall model size of 193M parameters. The predictor architecture is a ReLU-activated multilayer perceptron (MLP) with batch normalization. By default, we employ one 4096-wide hidden layer for the MLP. Both the prediction and projection dimensions are 512, as in CLAP [2]. We leave the study of predictor architecture hyperparameters as well as the influence of encoder architecture to future work. 

# 4.3 Training details 

All models are trained on PrivateCaps using a batch size of 768 across 6 A100 GPUs with PyTorch automatic mixed precision, for 60 epochs. We use linear warmup and cosine decay with a maximum learning rate of 4 × 10<sup>−4</sup> (scaled by batch size) and warmup over 1/10 of total epochs. We use SpecAugment as an audio augmentation [52], which improves performance slightly across tasks. We set EMA 

384 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

|||||A→|T|SongD|escrib|er|T →|A||||A→|T|Musi|cCaps||T →|A||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||R|ecall(|↑)|Norm.|rank (↓)||Recall(|↑)|Norm.|rank (↓)|R|ecall(|↑)|Norm.|rank (↓)||Recall(|↑)|Norm.|rank (↓)|
|Model|Pre.|1|5|10|Med.|Mean|1|5|10|Med.|Mean|1|5|10|Med.|Mean|1|5|10|Med.|Mean|
|SLAP|✗|3.3|13.0|19.7|5.3|12.3|3.7|12.5|19.4|5.4|13.8|1.6|5.3|7.5|4.8|14.5|1.2|4.9|7.9|4.4|13.3|
|CLAP|✗|3.1|9.6|14.9|7.3|14.2|2.7|9.7|15.8|6.7|16.4|0.9|3.4|5.2|8.8|18.2|0.7|3.2|5.2|7.5|17.4|
|SLAP|✓|5.7|18.1|26.6|3.2|8.9|6.0|18.1|26.4|3.6|10.5|3.1|10.1|15.4|1.9|7.7|3.0|9.6|15.4|1.9|7.7|
|CLAP|✓|5.3|14.9|22.2|4.3|9.2|5.7|16.8|24.1|4.3|9.7|2.8|8.3|10.4|3.0|10.0|2.8|8.7|14.0|2.2|7.6|
|MusCAL|L|1.4|7.0|14.4|7.8|14.7|1.9|6.8|12.1|8.8|19.9|1.5|7.1|10.8|9.3|17.3|0.4|1.6|3.0|12.8|21.1|
|LAION-|CLAP<sup>†</sup>|1.9|7.4|11.4|9.4|18.7|1.6|5.3|9.5|9.2|18.2|3.2|10.4|16.0|2.0|6.9|3.7|11.1|17.0|1.6|5.5|



> † Note that LAION-CLAP is trained on a large dataset that includes AudioSet [48], from which the audio samples of MusicCaps were extracted. 

Table 2. Text-Music retrieval results. Bolded results indicate best results between CLAP and SLAP for either models initialized from pretrained checkpoints (✓) or from scratch (✗). All metrics are in percentages. 

update rate τ = 0.95, as we empirically find that lower values (compared to 0.996 in [11]) yield better retrieval performance, and leave full hyper-parameter tuning to future work. We experiment with both randomly initialized and pretrained checkpoints for HTS-AT<sup>2</sup> and RoBERTa<sup>3</sup> , and initialize the HTS-AT backbone from a public checkpoint trained on AudioSet [48] when initializing from pretrained. 

# 5. RESULTS 

# 5.1 Multimodal retrieval 

We perform Audio to Text (A → T ) and Text to Audio (T → A) retrieval across the test datasets described in Section 4.1. We use predictions q as key and query for SLAP models (see Section 5.1.1) and projections z for CLAP models. We report Recall @(1,5,10), as well as Mean and Median Normalized Rank (MNR/MdNR) [53]. We report comparable results from relevant work in literature as well as our reproduced CLAP model. 

We report retrieval results in Table 2. We find that SLAP consistently outperforms both MusCALL [16], which was also trained on PrivateCaps, and our own reproduced CLAP models. Notably, Recall and Normalized Rank are improved across all metrics except for the T → A task on MNR. Initializing from pretrained encoders leads to significantly better performance both for CLAP and SLAP. 

We also compare our results to LAION-CLAP [49], which shares the same architecture. On Song Describer, all our models significantly outperform it, highlighting the importance of high-quality training data for music understanding. On MusicCaps, whose audios are part of their training data, LAION-CLAP performs better; however, our best SLAP model, initialised from pretrained checkpoints, achieves close performances, particularly on A → T . 

|||Song D|escriber|||Musi|cCaps||
|---|---|---|---|---|---|---|---|---|
||A|→T|T|→A|A|→T|T|→A|
|Anchor|R@5|MdNR|R@5|MdNR|R@5|MdNR|R@5|MdNR|
|z|17.8|3.6|17.0|3.8|9.6|2.1|9.4|2.3|
|q|18.1|3.2|18.1|3.6|10.1|1.9|9.6|1.9|



Table 3. Retrieval results using queries q or projection embeddings z as anchors. Best results are in bold. 

> 2 `https://github.com/LAION-AI/CLAP` 

> 3 `https://huggingface.co/FacebookAI/roberta-base` 

# 5.1.1 Prediction vs. projection retrieval 

One variant of our approach is to use predictions instead of projections to perform retrieval. Given the loss formulation, both are possible since both exist in separate embedding spaces and the pretraining objective optimizes for four-way similarity. Here we observe the effect of using q or z as query and key for retrieval. Results are reported in Table 3. We find that using projections instead of predictions leads to a small drop in performance, but both are viable for retrieval tasks, meaning there is no loss of information when compared to CLAP for projections. 

||GTZAN|MT|AT|OpenMic|
|---|---|---|---|---|
|Model|Acc.|AUROC|mAP|mAP|
|SLAP|82.9|92.0|45.8|86.2|
|CLAP|80.9|91.7|45.1|85.8|
|MusCALL|74.5|91.5|44.4|79.7|
|MATPAC|85.9|91.6|41.1|85.4|
|SOTA|87.4[54]|92.7[17]|41.4 [55]|86.7[56]|



Table 4. Probing results on frozen representations for genre classification (GTZAN), automatic tagging (MTAT), and Instrument tagging (OpenMic). Best scores are bolded and second-to-best are <mark>underlined.</mark> 

# 5.2 Downstream probing 

This section verifies the quality of the learned representations of SLAP by performing downstream probing on a range of tasks on representations before the projection head which outputs z. For downstream task evaluation, we freeze the audio encoder and train shallow nonlinear probes (one ReLU-activated 512-wide hidden layer MLPs). Probes are trained with a learning rate of 10<sup>−4</sup> with an early-stopping mechanism on validation loss. 

Our results are reported in Table 4. As above, we compare them to our CLAP baseline and MusCALL. We report the performance of MATPAC [43], the current selfsupervised state-of-the-art on these tasks as well. As a reference, we also indicate state-of-the-art performances for each task. 

We observe that SLAP consistently outperforms CLAP and MusCALL, demonstrating the advantages of our target encoder/predictor strategy over contrastive learning. 

385 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

On MTAT and OpenMic, SLAP surpasses MATPAC, which also employs a target encoder and predictor but is trained on audio alone. This suggests that language supervision is particularly beneficial for tagging tasks but is less useful for genre classification (82.9% vs. 85.9%). 

On tagging tasks, SLAP achieves state-of-the-art results on MTAT (45.8% vs. 41.1%) and bridges the gap with best supervised methods on OpenMic (86.2% vs. 86.7%). 

# 5.3 Zero-shot performance 

Similar to shallow downstream probing, we evaluate the zero-shot performance of SLAP by retrieving the highest similarity prompts to audio using prompts as a class proxy on GTZAN, MTAT, and OpenMic. We report Zero-shot accuracy on GTZAN, as well as ROC-AUC and mAP for automatic tagging on MTAT, and mAR on OpenMic. As previous work has shown the importance of prompt engineering for zero-shot performance [16], we evaluate across four prompts with which we wrap the target class “{}”, “{} music”, “this sounds like {}”, and “A {} track”. We report the best of four scores across datasets for both CLAP, SLAP, and MusCALL [16]. 

We adapt another metric for zero-shot evaluation of multilabel approaches, which we call mean Average Recall (mAR). Previous approaches evaluate multi-tag zero-shot performance by using tag-wise cosine similarity as logits as input for standard metrics such as AUROC and mAP. These metrics are not robust to to cosine similarity distributions centered around 0.5 with low spreads for certain tasks, e.g. instrumentation. mAR computes the mean rank of retrieved ground truth tags for a given audio: 



<!-- Start of picture text -->
K N<br>1<br>mAR = Rn@k. (6)<br>NK<br>-∑ k=1 ∑ n=1<br><!-- End of picture text -->

where K is the number of samples in the dataset, N the number of tags, and Rn@k recall at k for tag n. We evaluate mAR on OpenMic. Results are reported in Table 5 for CLAP, SLAP, and MusCALL [16]. 

We observe that SLAP consistently outperforms or is on par with our CLAP baseline and MusCALL. As for retrieval, a plausible cause is the better overlap between the audio and text spaces of our approach compared to contrastive ones. We measure this overlap in Section 5.4. 

||GTZAN|MTA|T|OpenMIC|
|---|---|---|---|---|
|Model|Acc.|AUROC|mAP|mAR|
|SLAP|58.3|75.0|31.5|70.5|
|CLAP|51.7|75.0|26.0|70.1|
|MusCALL [16]|48.2|73.8|23.0|66.7|



Table 5. Best-of-four zero-shot classification and tagging results for genre and instrument classification, and automatic tagging. Best scores are shown in bold. 

# 5.4 Modality gap 

As discussed in Section 2.2, one notable issue with MCL is the presence of a modality gap [7, 8]. While it is unclear 



<!-- Start of picture text -->
PrivateCaps UMAP reduction - CLAP SongDescriber UMAP reduction - CLAP<br>ZA<br>ZT<br>UMAP 1<br>UMAP 0 UMAP 0<br>PrivateCaps UMAP reduction - SLAP SongDescriber UMAP reduction - SLAP<br>UMAP 1 ZA<br>qT<br>UMAP 0 UMAP 0<br><!-- End of picture text -->

Figure 2. UMAP reduction of the CLAP (top) and SLAP (bottom) embeddings obtained from PrivateCaps (left) and Song Describer (right). 



<!-- Start of picture text -->
Centroid Distance 1. 0 Linear Se p arabilit y<br>CLAP Projections<br>0. 4 日 SLAP Projections SLAP Predictions 0. 9<br>0. 3 0. 8<br>0. 2 0. 7<br>0. 1 0. 6<br>0. 0 0. 5<br>PC SD MC PC SD MC<br>Dataset Dataset<br>) )<br>(A/T (LA/T<br><!-- End of picture text -->

Figure 3. Centroid Distance (left) and Linear separability (right) for SLAP and CLAP on PrivateCaps (PC), Song Describer (SD) and MusicCaps (MC). Lower is better. 

how detrimental the modality gap is to performance for retrieval, it has been shown that “closing the gap” is beneficial at least for generative applications [57]. Intuitively, having disjoint manifolds of audio and text representations allows their usage for cosine-similarity Max Inner Product Search, but is not beneficial for a shared joint understanding of text and audio. Multimodal contrastive models are subject to a modality gap, likely attributable to the formulation of contrastive loss [7]. Not being contrastive, we posit that our method should be less prone to creating such a gap. Figure 2 shows the UMAP reduction of projections zT , zA and qT , qA from PrivateCaps and Song Describer, for both CLAP and SLAP. Although the modality gap is immediately apparent for CLAP, it seems much less pronounced for SLAP. 

As in [7] and [8], we measure this by computing the linear separability LA/T between the respective manifolds of audio and text in the latent space. For both PrivateCaps, MusicCaps and Song Describer, we report in Figure 3 the 

386 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
Model Class pretrained<br>CLAP False<br>SLAP True<br>0.1 0<br>0.0 8<br>0.0 6<br>0.0 4<br>64 128 256 512 768<br>0.1 0<br>0.0 8<br>0.0 6<br>0.0 4<br>64 128 256 512 768<br>Effective Batch Size<br>T<br>Recall@1 A<br>A<br>Recall@1 T<br><!-- End of picture text -->

Figure 4. Scaling batch size for CLAP and SLAP. 

training accuracy of a Logistic Regression classifier trained to distinguish an audio embedding from a text embedding. We also measure the Euclidean distance ∆A/T between the centroids of each modality. 

These observations confirm the modality gap is larger, both in terms of distance and linear separability, for CLAP than for SLAP. More so, it is nearly nonexistent for SLAP on both PC and SD. Although the gap is larger for MC than for PC and SD, this can be attributed to a domain shift between datasets, likely attributable to the noisiness and longer captions of MC. 

# 5.5 Scalability properties 

We compare the scalability of SLAP and CLAP, focusing on batch size. A key limitation of contrastive models like CLAP is that their loss depends on all negatives in a batch, making gradient accumulation ineffective—since the gradient does not scale linearly with batch size. In contrast, SLAP requires no negatives and can theoretically be scaled to vastly large batch sizes, notably due to the lesser memory footprint and the availability of gradient accumulation. We study the effect of batch size on retrieval performance by reporting A → T and T → A R@1 on PrivateCaps for batch sizes from 64 to 768. For CLAP, batch size is scaled directly. For SLAP, we fix a base batch of 128 and accumulate gradients over N = B//128 steps to reach target batch size B. We empirically confirm that gradient accumulation in SLAP is equivalent to true batch scaling. Results are shown in Figure 4. 

# 5.6 Role of Intermodal and Intramodal Loss terms 

One key component of our approach is the multiple loss terms between the different EMA encoders of the training setup. We find that empirically, the absence of these losses 

LA and LT leads to collapse of the model. We show this in Figure 5 by reporting recall@k and linear separability between modalities for different balancing weights λ. 



<!-- Start of picture text -->
MusicCa p s Son g Describer<br>0.15 0 0.2 5 t ask<br>0.12 5 0.2 0 A->TT->A<br>0.10 0 0.1 5 k<br>0.07 5 1<br>0.05 0 0.1 0 5<br>10<br>0.02 5 0.0 5<br>0.00 0 0.0 0<br>0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0<br>1.0 0 1. 0<br>0.9 8<br>0. 9<br>0.9 6<br>0.9 4 0. 8<br>0.9 2<br>0. 7<br>0.9 0<br>0.8 8 0. 6<br>0.8 6<br>0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0<br>Recall@k<br>Modality Gap ()LA/T<br><!-- End of picture text -->

Figure 5. Tuning of intramodality loss balancing weight λ for the SLAP objective, measuring both T → A and A → T retrieval performance and LA/T . 

We find that within a range of λ, SLAP is robust for retrieval. Values of λ outside [0.2, 0.7] lead to almost systematic collapse due to the lack of meaningful constraints between or within modalities. Despite good retrieval robustness, we find that any λ̸ = 0.5 yields a rapidly increasing modality gap. Only a balanced contribution of intra and inter-modality loss terms leads to the significant reduction of the modality gap observed in Section 5.4. 

# 6. CONCLUSION AND FUTURE WORK 

We propose a novel approach to training multimodal joint embedding spaces to align music and text representation: Siamese Language Audio Pretraining (SLAP). SLAP outperforms contrastive models on tasks including text-music retrieval, downstream probing, and zero-shot music understanding. It offers key advantages over contrastive approaches, including negative-free training for better scalability and substantial reduction of the modality gap. Without relying on extensive data augmentation, architectural tuning, or hyperparameter optimization, SLAP matches state-of-the-art performance—demonstrating its potential as a scalable alternative to CLAP-style training. 

CLIP/CLAP being a core component of many textconditioned models, several works have proposed to improve them, e.g., by exploring alternative architectures [2, 58], scaling-up training data [25, 59], promoting semantic or linguistic invariance [59,60] or improving the sensitivity to fine-grained temporal events [3, 5]. Importantly, these improvements typically do not rely on the contrastive loss, and SLAP could probably benefit from them as well. 

Finally, while we demonstrate the effectiveness of our method on music-related tasks, it is generalizable and could be applied to other modalities such as images or general audio. We therefore believe that this approach could lead to many applications beyond the scope of our paper. 

387 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

# 7. ACKNOWLEDGEMENT 

This work is supported by the EPSRC UKRI Centre for Doctoral Training in Artificial Intelligence and Music (EP/S022694/1) and Universal Music Group. 

# 8. REFERENCES 

- [1] A. Radford, J. W. Kim, C. Hallacy et al., “Learning transferable visual models from natural language supervision,” in International conference on machine learning. PMLR, 2021, pp. 8748–8763. 

- [2] B. Elizalde, S. Deshmukh, M. Al Ismail et al., “Clap learning audio concepts from natural language supervision,” in ICASSP 2023-2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2023, pp. 1–5. 

- [3] J. Wu, W. Li, Z. Novack et al., “Collap: Contrastive long-form language-audio pretraining with musical temporal structure augmentation,” in ICASSP 20252025 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2025, pp. 1–5. 

- [4] T. Komatsu, H. Munakata, T. Hasumi et al., “Aligned contrastive learning for text-to-music retrieval,” in ICASSP 2025-2025 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2025, pp. 1–5. 

- [5] Y. Yuan, Z. Chen, X. Liu et al., “T-clap: Temporalenhanced contrastive language-audio pretraining,” in 2024 IEEE 34th International Workshop on Machine Learning for Signal Processing (MLSP). IEEE, 2024, pp. 1–6. 

- [6] I. Manco, J. Salamon, and O. Nieto, “Augment, drop & swap: Improving diversity in llm captions for efficient music-text representation learning,” in Proceedings of the 25th International Society for Music Information Retrieval Conference (ISMIR), 2024. 

- [7] A. Fahim, A. Murphy, and A. Fyshe, “Its Not a Modality Gap: Characterizing and Addressing the Contrastive Gap,” may 2024. [Online]. Available: http://arxiv.org/abs/2405.18570 

- [8] V. W. Liang, Y. Zhang, Y. Kwon et al., “Mind the gap: Understanding the modality gap in multi-modal contrastive representation learning,” Advances in Neural Information Processing Systems, vol. 35, pp. 17 612– 17 625, 2022. 

- [9] H. Pham, Z. Dai, G. Ghiasi et al., “Combined scaling for zero-shot transfer learning,” Neurocomputing, vol. 555, p. 126658, 2023. 

- [10] J.-B. Grill, F. Strub, F. Altché et al., “Bootstrap your own latent-a new approach to self-supervised learning,” Advances in neural information processing systems, vol. 33, pp. 21 271–21 284, 2020. 

- [11] D. Niizumi, D. Takeuchi, Y. Ohishi et al., “Byol for audio: Self-supervised learning for general-purpose audio representation,” in 2021 International Joint Conference on Neural Networks (IJCNN). IEEE, 2021, pp. 1–8. 

- [12] T. Chen, S. Kornblith, M. Norouzi et al., “A simple framework for contrastive learning of visual representations,” in International conference on machine learning. PMLR, 2020, pp. 1597–1607. 

- [13] J. Spijkervet and J. A. Burgoyne, “Contrastive learning of musical representations,” in Proceedings of the 22nd International Society for Music Information Retrieval Conference (ISMIR), 2021. 

- [14] H. Akbari, L. Yuan, R. Qian, W. H. Chuang, S. F. Chang, Y. Cui, and B. Gong, “VATT: Transformers for Multimodal Self-Supervised Learning from Raw Video, Audio and Text,” in Advances in Neural Information Processing Systems, vol. 29. Neural information processing systems foundation, apr 2021, pp. 24 206–24 221. [Online]. Available: https://arxiv. org/abs/2104.11178v3 

- [15] R. Arandjelovic and A. Zisserman, “Look, Listen and Learn,” in Proceedings of the IEEE International Conference on Computer Vision, vol. 2017-Octob. Institute of Electrical and Electronics Engineers Inc., may 2017, pp. 609–617. [Online]. Available: https://arxiv.org/abs/1705.08168v2 

- [16] I. Manco, E. Benetos, E. Quinton et al., “Contrastive audio-language learning for music,” in Proceedings of the 23rd International Society for Music Information Retrieval Conference, ISMIR 2022, Bengaluru, India, December 4-8, 2022, P. Rao, H. A. Murthy, A. Srinivasamurthy, R. M. Bittner, R. C. Repetto, M. Goto, X. Serra, and M. Miron, Eds., 2022, pp. 640–649. 

- [17] Q. Huang, A. Jansen, J. Lee et al., “Mulan: A joint embedding of music audio and natural language,” in Proceedings of the 23rd International Society for Music Information Retrieval Conference, ISMIR 2022, Bengaluru, India, December 4-8, 2022, P. Rao, H. A. Murthy, A. Srinivasamurthy, R. M. Bittner, R. C. Repetto, M. Goto, X. Serra, and M. Miron, Eds., 2022, pp. 559–566. 

- [18] G. Zhu, J. Darefsky, and Z. Duan, “Cacophony: An improved contrastive audio-text model,” IEEE/ACM Transactions on Audio, Speech, and Language Processing, 2024. 

- [19] A. Guzhov, F. Raue, J. Hees et al., “Audioclip: Extending clip to image, text and audio,” in ICASSP 2022-2022 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2022, pp. 976–980. 

- [20] R. Girdhar, A. El-Nouby, Z. Liu et al., “Imagebind: One embedding space to bind them all,” in Proceedings 

388 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

of the IEEE/CVF conference on computer vision and pattern recognition, 2023, pp. 15 180–15 190. 

- [21] G. Cicchetti, E. Grassucci, L. Sigillo, and D. Comminiello, “Gramian Multimodal Representation Learning and Alignment,” dec 2024. [Online]. Available: http://arxiv.org/abs/2412.11959 

- [22] A. Ramesh, P. Dhariwal, A. Nichol et al., “Hierarchical text-conditional image generation with clip latents,” arXiv preprint arXiv:2204.06125, vol. 1, no. 2, p. 3, 2022. 

- [23] J.-B. Alayrac, J. Donahue, P. Luc et al., “Flamingo: a visual language model for few-shot learning,” Advances in neural information processing systems, vol. 35, pp. 23 716–23 736, 2022. 

- [24] Z. Kong, A. Goel, R. Badlani et al., “Audio Flamingo: A Novel Audio Language Model with Few-Shot Learning and Dialogue Abilities,” in Proceedings of Machine Learning Research, vol. 235. ML Research Press, feb 2024, pp. 25 125–25 148. [Online]. Available: https://arxiv.org/abs/2402.01831v3 

- [25] S. Ghosh, S. Kumar, C. K. R. Evuru et al., “Reclap: Improving zero shot audio classification by describing sounds,” in ICASSP 2025-2025 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2025, pp. 1–5. 

- [26] X. Li, W. Chen, Z. Ma et al., “Drcap: Decoding clap latents with retrieval-augmented generation for zero-shot audio captioning,” in ICASSP 2025-2025 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2025, pp. 1–5. 

- [27] S. Ghosh, S. Kumar, C. K. R. Evuru et al., “Recap: Retrieval-augmented audio captioning,” in ICASSP 2024-2024 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2024, pp. 1161–1165. 

- [28] Z. Evans, C. Carr, J. Taylor et al., “Fast timingconditioned latent audio diffusion,” in Proceedings of the 41st International Conference on Machine Learning, 2024, pp. 12 652–12 665. 

- [29] Z. Evans, J. D. Parker, C. Carr et al., “Long-form music generation with latent diffusion,” in Proceedings of the 25th International Society for Music Information Retrieval Conference (ISMIR), 2024. 

- [30] J. Nistal, M. Pasini, C. Aouameur et al., “Diff-a-riff: Musical accompaniment co-creation via latent diffusion models,” in ISMIR, 2024, 2024. 

- [31] H. Liu, Z. Chen, Y. Yuan et al., “AudioLDM: Text-toaudio generation with latent diffusion models,” in Proc. ICML, 2023. 

- [32] A. Agostinelli, T. I. Denk, Z. Borsos et al., “MusicLM: Generating music from text,” arXiv preprint arXiv:2301.11325, 2023. 

- [33] X. Zhai, B. Mustafa, A. Kolesnikov et al., “Sigmoid Loss for Language Image Pre-Training,” in Proceedings of the IEEE International Conference on Computer Vision. Institute of Electrical and Electronics Engineers Inc., mar 2023, pp. 11 941–11 952. [Online]. Available: https://arxiv.org/abs/2303.15343v4 

- [34] M. Assran, R. Balestriero, Q. Duval et al., “The Hidden Uniform Cluster Prior in Self-Supervised Learning,” in 11th International Conference on Learning Representations, ICLR 2023, oct 2023. [Online]. Available: http://arxiv.org/abs/2210.07277 

- [35] P. Y. Shi, M. Welle, M. Björkman et al., “Understanding the Modality Gap in CLIP,” in International Conference on Learning Reprsentations, no. 2023, 2023. 

- [36] X. Chen and K. He, “Exploring simple siamese representation learning,” in Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, 2021, pp. 15 750–15 758. 

- [37] M. Assran, Q. Duval, I. Misra et al., “Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture,” in 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), jun 2023, pp. 15 619–15 629, iSSN: 2575-7075. 

- [38] Y. Tian, X. Chen, and S. Ganguli, “Understanding SelfSupervised Learning Dynamics without Contrastive Pairs,” Proceedings of Machine Learning Research, vol. 139, pp. 10 268–10 278, feb 2021. [Online]. Available: http://arxiv.org/abs/2102.06810 

- [39] M. Oquab, T. Darcet, T. Moutakanni et al., “DINOv2: Learning Robust Visual Features without Supervision,” apr 2023. [Online]. Available: http://arxiv.org/abs/ 2304.07193 

- [40] A. Baevski, W.-N. Hsu, Q. Xu et al., “data2vec: A General Framework for Self-supervised Learning in Speech, Vision and Language,” in Proceedings of Machine Learning Research, Baltimore, MD, USA, 2022. 

- [41] X. Li and X. Li, “ATST: Audio Representation Learning with Teacher-Student Transformer,” in Proceedings of the Annual Conference of the International Speech Communication Association, INTERSPEECH, vol. 2022-Septe. International Speech Communication Association, apr 2022, pp. 4172–4176. [Online]. Available: http://dx.doi.org/10.21437/Interspeech.2022-10126 

- [42] D. Niizumi, D. Takeuchi, Y. Ohishi et al., “Masked Modeling Duo: Learning Representations by Encouraging Both Networks to Model the Input,” in ICASSP 2023 - 2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). Rhodes Island, Greece: IEEE, jun 2023, pp. 1–5. 

- [43] A. Quelennec, P. Chouteau, G. Peeters et al., “Masked latent prediction and classification for self-supervised 

389 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

audio representation learning,” in ICASSP 2025 - 2025 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2025, pp. 1–5. 

- [44] I. Manco, B. Weck, S. Doh et al., “The song describer dataset: a corpus of audio captions for music-andlanguage evaluation,” NeurIPS Machine Learning for Audio Workshop, 2023. 

- [45] G. Tzanetakis and P. Cook, “Musical genre classification of audio signals,” IEEE Transactions on Speech and Audio Processing, vol. 10, no. 5, pp. 293–302, 2002. [Online]. Available: https://doi.org/10.1109/TSA.2002.800560 

- [46] E. Law, K. West, M. I. Mandel et al., “Evaluation of Algorithms Using Games: The Case of Music Tagging,” in Proceedings of the 10th International Society for Music Information Retrieval Conference, ISMIR 2009, Kobe International Conference Center, Kobe, Japan, October 26-30, 2009. International Society for Music Information Retrieval, 2009, pp. 387–392. [Online]. Available: http://ismir2009.ismir. net/proceedings/OS5-5.pdf 

- [47] E. Humphrey, S. Durand, and B. McFee, “Openmic2018: An open data-set for multiple instrument recognition.” in ISMIR, 2018, pp. 438–444. 

- [48] J. F. Gemmeke, D. P. W. Ellis, D. Freedman et al., “Audio set: An ontology and human-labeled dataset for audio events,” in Proc. IEEE ICASSP 2017, New Orleans, LA, 2017. 

- [49] Y. Wu, K. Chen, T. Zhang et al., “Large-scale contrastive language-audio pretraining with feature fusion and keyword-to-caption augmentation,” in Proc. ICASSP. IEEE, 2023, pp. 1–5. 

   - [55] R. Castellon, C. Donahue, and P. Liang, “Codified audio language modeling learns useful representations for music information retrieval,” International Society for Music Information Retrieval (ISMIR), 2021. 

   - [56] S. Chen, Y. Wu, C. Wang et al., “Beats: audio pretraining with acoustic tokenizers,” in Proceedings of the 40th International Conference on Machine Learning, 2023, pp. 5178–5193. 

   - [57] J. Nistal, M. Pasini, and S. Lattner, “Improving musical accompaniment co-creation via diffusion transformers,” in Audio Imagination: NeurIPS 2024 Workshop AI-Driven Speech, Music, and Sound Generation, 2024. 

   - [58] M. Zhao, J. Ono, Z. Zhong et al., “On the Language Encoder of Contrastive Cross-modal Models,” oct 2023. [Online]. Available: http://arxiv.org/abs/2310. 13267 

   - [59] S. Ghosh, Z. Kong, S. Kumar et al., “Audio Flamingo 2: An Audio-Language Model with Long-Audio Understanding and Expert Reasoning Abilities,” mar 2025. [Online]. Available: http: //arxiv.org/abs/2503.03983 

   - [60] X. Dong, J. Bao, Y. Zheng, T. Zhang, D. Chen, H. Yang, M. Zeng, W. Zhang, L. Yuan, D. Chen, F. Wen, and N. Yu, “MaskCLIP: Masked SelfDistillation Advances Contrastive Language-Image Pretraining,” pp. 10 995–11 005, aug 2023. [Online]. Available: https://arxiv.org/abs/2208.12262v1http:// arxiv.org/abs/2208.12262 

- [50] K. Chen, X. Du, B. Zhu et al., “Hts-at: A hierarchical token-semantic audio transformer for sound classification and detection,” in ICASSP 2022-2022 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2022, pp. 646–650. 

- [51] Y. Liu, M. Ott, N. Goyal et al., “Roberta: A robustly optimized bert pretraining approach,” arXiv preprint arXiv:1907.11692, 2019. 

- [52] D. S. Park, W. Chan, Y. Zhang et al., “Specaugment: A simple data augmentation method for automatic speech recognition,” Interspeech 2019, p. 2613, 2019. 

- [53] S. Lattner, “Samplematch: Drum sample retrieval by musical context,” in Proceedings of the 23rd International Society for Music Information Retrieval Conference, {ISMIR} 2022, Bengaluru, India, December 4-8, 2022, 8 2022, pp. 781–788. [Online]. Available: http://arxiv.org/abs/2208.01141https: //archives.ismir.net/ismir2022/paper/000094.pdf 

- [54] K. Koutini, J. Schlüter, H. Eghbal-zadeh et al., “Efficient training of audio transformers with patchout,” Interspeech 2022, 2022. 

390 

