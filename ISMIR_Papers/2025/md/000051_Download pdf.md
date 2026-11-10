---
paper_id: "000051"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706481/files/000051.pdf"
---

# IMPROVING BERT FOR SYMBOLIC MUSIC UNDERSTANDING USING TOKEN DENOISING AND PIANOROLL PREDICTION 

## Jun-You Wang Institute of Information Science Academia Sinica 

## Li Su 

Institute of Information Science Academia Sinica 

### ABSTRACT 

We propose a pre-trained BERT-like model for symbolic music understanding that achieves competitive performance across a wide range of downstream tasks. To achieve this target, we design two novel pre-training objectives, namely token correction and pianoroll prediction. First, we sample a portion of note tokens and corrupt them with a limited amount of noise, and then train the model to denoise the corrupted tokens; second, we also train the model to predict bar-level and local pianoroll-derived representations from the corrupted note tokens. We argue that these objectives guide the model to better learn specific musical knowledge such as pitch intervals. For evaluation, we propose a benchmark that incorporates 12 downstream tasks ranging from chord estimation to symbolic genre classification. Results confirm the effectiveness of the proposed pre-training objectives on downstream tasks. 

### 1. INTRODUCTION 

In recent years, music information retrieval (MIR) research in the symbolic music domain has undergone a paradigm shift from the development of task-specific models to the adoption of the pre-training/fine-tuning paradigm, where a model is first pre-trained on a large-scale dataset with selfsupervised learning (SSL) objectives and then fine-tuned on specific downstream tasks [1–7]. One of the advantages is that this paradigm is adaptable to downstream tasks with only minimum task-specific designs. Inspired by the advance of natural language processing (NLP) [8–10], pretrained symbolic music understanding models like MidiBERT [1] and MusicBERT [5] typically adopt a similar architecture and pre-training objective as BERT, i.e., masked language modeling (MLM) in text sequences [11]. Discussions for improvement have been therefore focused on the masking strategy during pre-training [3, 4], leading to improved performance in downstream tasks. 

However, currently there are several issues that have to be overcome. First, there is a limitation of using only MLM in symbolic music modeling due to the fundamental 

> © J.-Y. Wang and L. Su. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: J.-Y. Wang and L. Su, “Improving BERT for symbolic music understanding using token denoising and pianoroll prediction”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

differences between music and text. Unlike words, symbolic music events are usually the notes of a specific music scale performed at specific time intervals. The MLM objective does not implicitly encode such music knowledge, but treats all note tokens as individuals, regardless of their possible tonal or metrical implications. Modifications regarding pre-training objectives should be made to help the model learn such aspects of symbolic music better. Second, there is a lack of a comprehensive evaluation for pretrained models for symbolic music. Previous works are only evaluated for five or fewer downstream tasks quantitatively [1–6], which could be improved to reveal more advantages and disadvantages of a pre-trained model. 

To address these issues, we make two main contributions in this work. First, we propose two novel selfsupervised learning objectives for pre-training. The first one, namely the token denoising objective, is a modified version of the MLM objective. Instead of randomly replacing note tokens with a pre-defined `[MASK]` token, we randomly corrupt the attributes of note tokens by adding small random noises and train the model to reconstruct the original tokens. Such a token de-noising objective implicitly encodes the actual distance information of note attribute values. The second one, namely the pianoroll prediction objective, has the model infer pitch and chroma distribution from the corrupted input note sequence, which resembles the prediction of pianoroll representation. This helps the model implicitly learn the idea of pianoroll, which encompasses important features such as the temporal information and the interval between notes, which are crucial in downstream tasks such as melody extraction [12–14], roman numeral analysis [7,15,16], etc. As a result, the pretrained model acquires domain knowledge on symbolic music and performs better on downstream tasks. 

Second, to verify the effectiveness of pre-trained models, we conduct a comprehensive evaluation by adapting the models to a total of 12 downstream classification tasks, which far exceeds the scale of evaluation in previous works [1–6]. To achieve this goal, we propose a unified protocol for fine-tuning, and recast various symbolic music understanding tasks with publicly available datasets into this framework. By fine-tuning a pre-trained model on such a wide range of downstream tasks, we do not only demonstrate the effectiveness of the proposed methods, but also pave the way for the evaluation of future work. As a preliminary step toward formalizing the evaluation of pretrained models in symbolic music, we invite the research 

442 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

community to include more diverse downstream tasks and further refine the protocol to facilitate the future development of different forms of symbolic pre-trained models. 

### 2. RELATED WORK 

Symbolic music data is an abstract representation of music [17], which represents a musical piece with a sequence of notes. Each note contains at least three attributes: onset timing, note duration, and note pitch. Additional attributes such as tempo, time signature, staff information, etc., may also present. Symbolic music understanding aims to infer high-level information from it, such as melody [12, 14], motifs [18], repeated patterns [19, 20], functional harmony [15, 21], texture [22], genre [23], structural boundary [24], and emotion [25,26]. 

As symbolic music understanding tasks highly involve the domain knowledge of music, annotating ground-truths for these tasks typically have to be done by experts, sometimes assisted with computational tools [27]. As a result, available data for symbolic music understanding tasks are usually scarce. To address this issue, previous work has proposed to generate training data automatically [28] and obtaining annotation from the Internet [29]. Recently, there have been attempts to directly utilize large language models (LLMs) for symbolic music understanding tasks [30, 31], which removes the demand of a largescale dataset; however, the results are unsatisfactory. In tasks related to music reasoning such as key estimation and harmony analysis, the best LLM only achieves an accuracy slightly better than random guess, possibly due to the domain gap between text and symbolic music [30]. 

Another research direction is to adapt a pre-trained model in the symbolic music domain to downstream tasks. In the past few years, the surge of pre-trained models that can be easily adapted to various downstream tasks has led to a paradigm change in multiple domains [32, 33], such as text [8, 9, 11], image [34], speech [35–37], and music in the audio domain [33, 38–40]. In symbolic music domain, there are also efforts to build pre-trained models for symbolic music understanding [1, 3–5] and symbolic music generation [2,6,41]. Due to the similarity between text and symbolic music [17], previous pre-trained models on symbolic music understanding mostly employs similar architectures and pre-training objectives as in NLP. For example, [1, 3–5] are all based on BERT [11]. In this work, we propose novel objectives that take into account the distinct characteristics of symbolic music for pre-training. 

### 3. PROPOSED METHOD 

Figure 1 gives an overview of the proposed method. The input symbolic music representation is a music piece X composed of N notes, i.e., X := {xn}<sup>N</sup> n=1<sup>,and</sup> xn := (on, pn, dn) represents the n-th note with its onset, pitch, and duration in X, and a list of downbeat timings DB composed of M downbeat timings, i.e., DB := {dbm}<sup>M</sup> m=1<sup>.ForMIDIdata(includingperfor-</sup> mance MIDI), an unreliable yet doable way to obtain the 

raw DB information is to retrieve the tick information (e.g., the number of ticks per beat and downbeat) in MIDI. The proposed pre-trained model F (·) generates a contextualized representation at the note level. During pre-training, we add a prediction head G on top of F and train G(F (·)) with unlabeled data through self-supervised learning objectives. Then, during fine-tuning, we remove G and add another prediction head H(·) on top of F , and train both F and H in a downstream classification task. We aim to improve F so that H(F (·)) could achieve better overall performance in a wide range of downstream tasks. 

### 3.1 Tokenization and segmentation 

Following MidiBERT [1], we adopt a modified version of the Compound Word (CP) representation [42] for tokenization. Each note xn is represented by a CP token with four attributes, (bn, posn, pitn, durn). bn ∈ [0, 1] is a binary flag that denotes whether a note is at the start of a bar; posn ∈ [0, 15] denotes the onset position of a note within a bar rounded to an integer number of 1/4 crotchet beats; pitn ∈ [22, 107] denotes note pitch; durn ∈ [1, 64] denotes note duration rounded to an integer number of 1/8 crotchet beats. In practice, we follow MidiBERT by assuming that the duration of a bar is four crotchet beats (i.e., 4/4 or 2/2 time signature). For bars that have a different duration (which can be inferred from DB), we rescale them to four crotchet beats. As for segmentation, following [5], we adopt a maximum sequence length of 1024 tokens. 

### 3.2 Backbone model 

In previous work, BERTBASE [11], a bidirectional encoder with 12 Transformer layers [43], has been widely used as the backbone model [1, 3–6]. In this work, we choose ModernBERT [44] as our backbone model. ModernBERT is an enhanced version of BERT that incorporates various techniques to improve training efficiency and performance, such as flash attention [45], local attention, rotary positional encoding mechanisms [46], etc. Although the official ModernBERT model contains 22 layers, we reduce them to 12 for a fair comparison with MidiBERT. We refer to our proposed ModernBERT-based model as M2BERT, which stands for Modern-MidiBERT. 

### 3.3 Pre-training objectives 

In both BERT and MidiBERT [1, 11], the MLM objective is applied for pre-training. They first randomly choose a fraction of input tokens (15% of tokens in practice). For the chosen tokens, 80% of them are replaced with a special `[MASK]` token, 10% of them are replaced with a randomly sampled token, and the remaining 10% tokens are kept intact. Then, the model is trained to recover the original tokens from such masked inputs. However, the MLM objective does not fully account for domain-specific knowledge in music. For example, the fact that “the pitch difference between E4 and C4 is necessarily a major third” cannot be inferred simply by successfully predicting a masked token. As a result, the model lacks a mechanism to ensure that the 

443 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
Pre-training Pianoroll Chroma Pianoroll Chroma<br>Pianoroll<br>CP tokens Convert to<br>prediction<br>pianoroll loss<br>Noisy CP tokens Denoised CP tokens<br>b=ruepos1=0/16pit65dur=32b_2=Falsepos2=4/16pit_2=68dur=32<br>Token<br>Random ModernBERT F() Prediction denoising<br>corruption head G() loss<br>b1=Truepos1=0/16 pit1=65 dur/=32b2=FalsepoSs2=6/16Pi=270dur=732 b₁=Truepos1=0/16pit1=65du/=32 poS2=4/16 pit2=65 dur/=832<br>个<br>Fine-tuning CPtokens<br>Prediction Cross-<br>ModernBERT F() entropy<br>head H() loss<br>b=ruepos1=0/16pit1=65durt=32b2=Falsepos2=4/16pit_2=68du/=232<br>Ground-truth<br><!-- End of picture text -->

Figure 1. An overview of the proposed method. 

learned embeddings of these two pitches reflect the general relationship shared by all major third intervals. 

To address this issue, we propose two pre-training objectives. The first is to train the model to correct corrupted tokens rather than masked tokens, and employ a corruption strategy that is aware of the proximity of notes (named as the token denoising objective). The second is to have the model predict not only tokens but also pianorolllike features, which can capture geometrical information of notes that is well encoded in a pianoroll representation but cannot be trivially inferred from a token sequence alone (named as the pianoroll prediction objective). The two pretraining objectives are described below. 

### 3.3.1 Token denoising 

Similar to MLM, we also randomly sample notes and corrupt them. But instead of replacing notes with the `[MASK]` token, we corrupt notes by randomly perturbing the value of the tokens. For an input token (bn, posn, pitn, durn), we obtain a corrupted token (<sup>˜</sup> bn, pos˜ n, pit<sup>˜</sup> n, dur<sup>˜</sup> n) it by: 



<!-- Start of picture text -->
˜bn = rand(0, 2), (1)<br><!-- End of picture text -->



<!-- Start of picture text -->
pos˜ n = rand(clip(posn − rpos), clip(posn + rpos)), (2)<br><!-- End of picture text -->



<!-- Start of picture text -->
pit˜ n = rand(clip(pitn − rpit), clip(pitn + rpit)), (3)<br><!-- End of picture text -->



<!-- Start of picture text -->
dur˜ n = rand(clip(durn − rdur), clip(durn + rdur)), (4)<br><!-- End of picture text -->

where the rand(x, y) function randomly samples an integer from the interval [x, y); the clip(z) function clips z such that z lies in a valid range of token number (e.g., [0, 15] for posn); the hyperparameters rpos, rpit, and rdur determine the range of corruption. Setting rpos, rpit, rdur := ∞ results in the case of random sampling from all possible tokens. The proposed model is trained to recover the original note tokens (i.e., denoise) from the corrupted ones with the crossentropy loss, similar to the MLM objective in BERT. 

The reasons behind this corruption strategy are twofold. First, as noted in previous NLP work, using the `[MASK]` token introduces a discrepancy of distribution between pre-training data and fine-tuning data, making the pre-training process allocate model dimensions to exclusively represent the `[MASK]` tokens [47]. The same work 

also shows that randomly replacing `[MASK]` to other tokens is a suboptimal strategy [47]. Our proposed objective (i.e., randomly corrupting tokens but within a limited range) represents a compromise strategy to reduce such discrepancy, and is easy to operate on symbolic music data. Second, limiting the range of corruption encourages the model to better learn the proximally relative distance between note tokens, which usually carries musical meanings. For example, suppose rpit is set to 12 semitones, making the model observe a note corrupted to C6. The model is then guided to infer that the correct pitch must be located between C5 and C7 rather than other pitch values far away from C6. This mechanism is desirable, as it guides the model to learn the knowledge related to the pitch interval. 

### 3.3.2 Pianoroll prediction 

Another set of the proposed pre-training objective is to make the model predict pianoroll and chroma representations. Two prediction mechanisms are imposed: 

- The bar-level prediction mechanism has each xn predict the pianoroll (denoted as PRn) and chromagram (denoted as CMn) of the bar in which the onset of xn is located. 

- The local prediction mechanism has each xn predict the pianoroll and chromagram at the onset position of xn, i.e., PRn[posn] and CMn[posn]. 

The two mechanisms represent different types of guidance for the model’s prediction capability: bar-level prediction ensures that all notes within the same bar predict the same representation, while local prediction allows each note to individually predict the representation corresponding to its specific timing. In practice, we divide one bar into 16 tatums (1/4 crotchet beats per tatum). Given that pitch tokens range from 22 to 107, the dimensions of PRn and CMn are (16, 86) and (16, 12), respectively. We employ the L2 loss with the weight for each loss term being equal. Specifically, for each xn, we have: 



<!-- Start of picture text -->
Ln = L2(PRn, PR ˆ n) + L2(CMn, CM ˆ n)<br>+ L2(PRn[posn], PR ˆ n[posn])<br>+ L2(CMn[posn], CM ˆ n[posn]) , (5)<br><!-- End of picture text -->

444 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

where PR<sup>ˆ</sup> n and CMˆ n denote the predicted pianoroll and chromagram from xn respectively. The total loss is therefore the sum of the token reconstruction loss and the pianoroll prediction loss over all notes. 

### 3.4 Prediction heads 

Two types of prediction heads H are utilized to perform the downstream tasks in the fine-tuning stage. The first type is for note-level prediction tasks, where H is simply a linear layer with Softmax activation. Another type is for sequence-level prediction tasks, where H contains an attention-based weighting average layer, a linear layer and Softmax activation. The attention-based weighting average layer uses two linear layers and a Softmax activation to determine the weight for each note, and then computes the weighting average of all notes’ embedding to form the sequence-level embedding. All these settings are derived from MidiBERT’s protocol [1], where the only differences are that we remove the dropout layer and reduce the number of linear layers for classification to one, which simplifies H and better aligns with BERT’s fine-tuning protocol [11]. In this work, three downstream tasks (SGC, PS, and ER, see Section 4 for details) are trained at sequence level, while all other downstream tasks are trained at note level. The G used for pre-training is also constructed with a linear layer with Softmax activation. 

During fine-tuning, the backbone model F and the prediction head H are jointly optimized. For each downstream task, we fine-tune the model with a training set, and select the best model checkpoint based on the model performance on a validation set following the designated evaluation metric of that task. 

### 4. THE SMC BENCHMARK 

We conduct an evaluation on 12 different downstream tasks for symbolic music classification. We refer to the combination of all these tasks and datasets as the SMC benchmark, which stands for Symbolic Music Classification benchmark. The benchmark is available at `https: //zenodo.org/records/15681035` . 

Similar to [1, 3, 4, 11], we focus on classification tasks, a common problem formulation of symbolic music understanding. Additionally, we aim to integrate these downstream tasks to achieve the following three objectives. 1) Reproducibility. We only select tasks with publicly available datasets that can be freely downloaded without requiring a data access application; 2) Diversity. We include a wide range of datasets while ensuring that each dataset is used for at most two downstream tasks.<sup>1</sup> 3) Comparability. We prefer to select tasks that have been discussed in previous work and have publicly reported state-of-the-art results for comparison. 

The 12 tasks are listed as follows: 

> 1 For example, the dataset compiled by AugmentedNet [15] is used for functional harmony analysis, which is decomposed into five subtasks. We only include two of them (chord root and local key) as downstream tasks. 

Symbolic genre classification (SGC). This task classifies the music genre of symbolic music (in MIDI format). We adopt the CD2 part of the Tagtraum genre annotations [23] for this task. To construct a balanced dataset, we select the five most frequent genres in the dataset<sup>2</sup> and sample 1,150 songs for each. Then, we divide the dataset into training/validation/test set with 500/150/500 songs for each class. We adopt the accuracy metric for this task. 

Piano performer style classification (PS). This task classifies the piano performer of a symbolic music from eight candidate pianists. It was introduced in MidiBERT along with the Pianist8 dataset [1]. Instead of following the official train/test split, considering the modest scale of the dataset, we divide it into five folds and perform crossvalidation. We adopt the accuracy metric for this task. 

Emotion recognition (ER). This task classifies the emotion of symbolic music into four quadrants of the valence-arousal space. Following [1], we use the EMOPIA dataset [25] and adopt the accuracy metric. We divide the dataset into five folds and perform cross-validation. 

Beat note prediction (BP). This task identifies beat notes from a performance MIDI note sequence, where each note contains only onset, offset, and pitch information, with onset and offset measured in seconds rather than quantized beat numbers. BP is a subtask of the Performance MIDI-to-Score conversion (PM2S) task [48]. To perform this task, we utilize the PM2S dataset compiled by Liu et al. [48], follow their train/valid/test split, and adopt the F1-score for evaluation. Since the input is not quantized in time, the pseudo-tokens of onset time and duration are obtained by the following pre-processing steps: 1) determine the global tempo T by assuming the length of one beat as the median value of all notes’ duration; 2) if T ∈/ [40, 200], then T is multiplied or divided by 2 to make it lie in the range; 3) quantize the note sequence to 16th notes by assuming a 4/4 time signature and constant tempo regardless of the actual performance content.<sup>3</sup> 

Downbeat note prediction (DbP). Similar to BP, this task aims to identify downbeat notes. We again use the PM2S dataset with the same train/valid/test split as Liu et al. [48] and use the F1-score metric. 

Chord root estimation (CR). This task involves predicting the tatum-wise chord roots for symbolic music and serves as a crucial subtask in functional harmony analysis [7,15,16,21]. We use the combined dataset compiled by AugmentedNet for this task and follow its train/valid/test split [15]. Following [7, 15, 16], we also adopt the Chord Symbol Recall (CSR) metric, but at the 1/4 crotchet beat level (instead of 1/8), since both MidiBERT and the proposed M2BERT have a time resolution of 1/4 crotchet beats. This should only lead to a negligible difference, as chord changes rarely occur at 1/8 crotchet beats. 

Local key estimation (LK) estimates the local key for symbolic music and is also a crucial subtask of functional harmony analysis. We utilize the same dataset, experiment setting and evaluation metric as in the case of CR. 

> 2 The five genres are Country, Electronic, Pop, RnB, and Rock. 

> 3 This does not imply that the actual time signature must be 4/4, but is simply a method to construct input tokens for the proposed model. 

445 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

Symbolic melody extraction (ME) classifies each note into three classes: vocal melody, instrumental melody, or accompaniment, which was also used for evaluation in MidiBERT [1]. We use the POP909 dataset [49] for this task and follow the same train/valid/test split as in MidiBERT. Note-level accuracy is adopted for evaluation. 

Symbolic velocity estimation (VE). Also introduced in MidiBERT, the objective of this task is to estimate the velocity of notes in terms six classes: pp, p, mp, mf, f, and ff. We use the same setting and evaluation metric as in ME. 

Orchestral texture classification (OTC) labels the textural layer of each track in symphony music in terms of melody, rhythm, and harmony [22, 50]. We utilize the dataset proposed by Le et al. in [50], which contains texture annotation of 24 symphony movements composed by Beethoven, Haydn, and Mozart. 18 of them are accompanied with digital score and have been used for the evaluation recently in [51]. We therefore follow the settings in [51], including the 7-class formulation for the multilabel scenario (exclude the “no label” class), the same train/test split, and bar-level accuracy for evaluation. Motif note identification (MNID). Similar to ME, MNID classifies whether or not a note in a music belongs to a motif of that music. This task plays a critical role in music analysis by highlighting important notes that contribute to the motifs of a musical piece [18]. We adopt the BPS-motif dataset for this task [18], and employ the note-level F1-score for evaluation. As a first attempt to this task, we divide this dataset into five folds and conduct cross-validation on it. 

Violin fingering prediction (VF) predicts the fingering that a performer uses to perform a symbolic violin piece. This task could also be considered as a generation task, as the fingering choices are up to the performer themself. However, we still consider this task as an aspect of music understanding since it corresponds to the notion of playability, a physical constraint over notes. We use the TNUA dataset [52] for this task and use the same train/valid/test split as [53]. Following [53], we treat violin fingering as a 240-class classification task (the combination of four string choices, five finger choices, and 12 hand position choices) and use note-level accuracy for evaluation. 

### 5. EXPERIMENT SETUP 

We utilize the StableAdamW optimizer [54] and randomly corrupt 30% of the note tokens for pre-training. The corruption hyperparameters rpos, rpit, and rdur are set to 4, 12, and 12, respectively. All other pre-training hyperparameters remain the same as MidiBERT, namely: learning rate of 2 × 10<sup>−5</sup> , weight decay of 0.01, batch size of 12, 85%/15% partition of the training and validation set, and choose the best model checkpoint that maximizes the token reconstruction accuracy on the validation set. 

For the pre-training dataset, we employ two settings. The first one, referred to as the “Reduced” dataset, follows MidiBERT [1] by combining POP909 [49], Pop1K7 [42], EMOPIA [25], Pianist8 [1], and ASAP [27], while excluding all non-4/4 time signature music from the training 

data.<sup>4</sup> This leads to a dataset containing 4.89M notes. For this setting, we train the model for 150 epochs, which takes around 18 hours on an NVIDIA RTX 6000 Ada GPU.<sup>5</sup> The second setting, referred to as the “Full” dataset, contains the Reduced dataset plus the lmd_matched set of the Lakh MIDI dataset [55], totaling 350.32M notes. Because of the limitation of our computational resources, we only train the model for 25 epochs when using the Full dataset, regardless of the decreasing validation loss. In the experiments, we employ the Reduced setting in all the ablation studies for a fair comparison with MidiBERT, while only employing the second setting for our best configuration. 

Our comparative study incorporates two models (i.e., MidiBERT and M2BERT), two datasets (i.e., Reduced and Full), and three training objectives: 1) the original MLM objective; 2) the proposed corrupted note reconstruction objective (denoted as RC(rpos,rpit,rdur), parametrized by the corruption ranges (rpos, rpit, rdur) labeled in the subscripts); 3) the pianoroll prediction objective (denoted as Pianoroll). It should be noted that RC∞ denotes note corruption by random sampling on all possible tokens. The source code of the proposed model and additional ablation study results are available at `https://github.com/ york135/M2BERT` . 

### 6. RESULTS 

Table 1 presents the experiment results over all the settings on the 12 downstream tasks. For reference, we show the state-of-the-art (SOTA) performance of the tasks in the last row, if available. First, we observe that all the settings of the proposed M2BERT model outperforms MidiBERT for almost all the downstream tasks; this demonstrates the advantages of the ModernBERT architecture. Second, random sampling (i.e. RC∞) does outperform MLM, possibly due to the removal of the `[MASK]` token. However, the proposed RC4,12,12 further outperforms RC∞; this shows the effectiveness of limiting the range of random corruption. Finally, incorporating the Full dataset for training further improves overall performance. 

Further delving into the results on each downstream task, we found that the individual proposed objectives do not consistently benefit all downstream tasks. Comparing MLM and RC4,12,12+Pianoroll (under M2BERT), we found that the improvements of RC4,12,12+Pianoroll mainly lies in DbP, CR, ME, OTC, and ER. Remarkably, the ME accuracy is improved from 0.975 to 0.982, which represents a relative error reduction of 28%. However, in other tasks, the improvements are marginal or even zero. We suspect that the proposed objectives tend to represent the musical domain knowledge related more on pitches, intervals, and chords, and therefore benefit more on these 

> 4 We use this setting to have a fair comparison with MidiBERT. However, as discussed in Section 3.1, the proposed model can still process non-4/4 music pieces by rescaling the bars, which are frequently seen in tasks that involve classical music, such as CR, LK, and MNID. 

> 5 The original MidiBERT trains the model for 500 epochs, but we found that for the proposed M2BERT, the validation loss usually reaches the lowest point between 100 and 150 epochs. Therefore, we terminate the training at the end of 150 epochs. 

446 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

|Model|Objectives|Dataset|SGC<br>Acc.|BP<br>F1|DbP<br>F1|CR<br>CSR|LK<br> CSR|ME<br>Acc.|VE<br> Acc.|OTC<br>Acc.|PS<br>Acc.|ER<br>Acc.|VF<br>Acc.|MNID<br>F1|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|MidiBERT|MLM|Reduced|.397|.843|.706|.795|.761|.964|.518|.694|.708|.638|.551|.700|
|M2BERT|MLM|Reduced|.403|.867|.749|.825|.796|.975|.524|.695|.740|.641|.509|.708|
|M2BERT|RC∞|Reduced|.397|.864|.768|.838|.780|.978|.536|.703|.740|.666|.538|.712|
|M2BERT|RC4,12,12|Reduced|.404|.867|.779|.838|.791|.983|.534|.707|.740|.658|.511|.719|
|M2BERT|RC4,12,12+Pianoroll|Reduced|.405|.867|.768|.847|.804|.982|.532|.725|.742|.667|.536|.718|
|M2BERT|RC4,12,12+Pianoroll|Full|.433|.886|.839|.855|.811|.986|.534|.720|.746|.671|.539|.745|
|SOTA|NA|NA|-|.945|.757|.849|.829|.974∗|.536|.695|.736†|.719†|.489|-|



Table 1. Evaluation results on the proposed SMC benchmark. If possible, we also show the state-of-the-art (SOTA) performance on the tasks reported by previous work. ∗ in the SOTA row means that it is reported under a simpler (2-class instead of 3-class) problem definition [56]; † denotes that the results are reported with a different dataset partition [4]. Results that achieve or surpass the SOTA are shown in italic, and the best results among pre-trained models are shown in bold. The SOTAs are obtained from [4,7,16,51,53,56]. For BP and DbP, we reproduce the evaluation of [48] and achieve a significantly better results than what they report (0.862 and 0.698, respectively), so we show the reproduction results. 

|Model|Objectives|Length|SGC<br>BP|DbP|CR|LK|ME|VE|OTC|PS|ER|VF|MNID|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|M2BERT|RC4,12,12+Pianoroll|512|.403<br>.870 <br>|.765|.808|.779|.976 <br>|.533<br>|.693<br>|.733|.647<br>|.493<br>|.725|
|M2BERT<br>M2BERT|RC4,12,12+Pianoroll<br>RC4,12,12+Pianoroll|1024<br>2048|.405<br>.867 <br>.397<br>.887|.768<br> .773|.847 <br>.862|.804<br> .805|.982 <br>.985|.532<br> .538|.725<br>.710|.742<br>.746|.667<br>.653|.536<br>.527|.718<br>.719|



Table 2. The ablation study results on the choice of maximum sequence lengths (the “Length” column). 

tasks (note that DbP is also benefited, possibly because it is somewhat related to chord changes). On the other hand, for BP, pitch and pitch interval are less important (as discussed in [48]) and are therefore not benefited. 

Another interesting finding lies in the result of VF, the only task in which MidiBERT outperforms the proposed M2BERT. While this suggests that M2BERT is not universally better than MidiBERT, we should also take into account that 1) the fine-tuning dataset for VF is smaller than those for other tasks; 2) VF is different from the other tasks in the sense that VF focuses more on the performer’s empirical preferences rather than music theory. These factors, rather than the model itself, might be responsible for this trend. Nevertheless, we can still observe that the proposed note correction and pianoroll prediction objectives do improve the performance of VF for M2BERT. 

Furthermore, our best model, M2BERT with the RC4,12,12+Pianoroll objectives, pre-trained with the full dataset, outperforms the SOTAs in DbP, CR, LK, ME, OTC, PS, and VF (six of the ten tasks that have a comparable SOTA). Considering that 1) we do not employ multitask learning or data augmentation, both are frequently used in SOTA works [7, 16, 48]; 2) we do not adopt taskspecific model design or hyperparameter search; and 3) we also do not adopt task-specific input representation; these results are promising, showing the effectiveness of using a pre-trained model for symbolic music classification. 

Finally, we conduct an ablation study on the choice of different maximum sequence lengths for the proposed M2BERT model. The results are shown in Table 2. We observe that for most of the downstream tasks, using a longer token length leads to better performance. Specifically, the two tasks which are benefited most by using a long token length are CR, which is improved by 5.4 percentage points, and LK, which is improved by 2.6 percent- 

age points, when increasing the sequence length from 512 to 2048, at the cost of the quadratic time complexity introduced by the Transformer architecture. Considering such a trade-off, we eventually choose the sequence length of 1024 in all other experiments (see Table 1). 

### 7. CONCLUSION 

With a systematic evaluation on a benchmark incorporating 12 downstream tasks, we have demonstrated the effectiveness of using token denoising and pianoroll prediction to enhance the pre-training of a BERT-like model for symbolic music understanding. This result underscores the important insight that symbolic music pre-training should focus on optimizing meaningful musical information, and, on the other hand, reveals the limitations of applying traditional NLP methods that optimize token sequences to symbolic music data. We also show the effectiveness of using an advanced model architecture and increasing the scale of data for pre-training. Additionally, considering that our symbolic pre-trained model was only trained on at most 350M notes—whereas text pre-trained models can leverage trillions of text tokens [9,57]—there is significant potential for scaling up our approach given more data [58]. It is also important to clarify that, to focus the discussions on model pre-training strategies, our current benchmark consists solely of classification tasks that allow for direct linear probing. Therefore, to further advance symbolic music foundation models in music understanding, our future directions include developing methods to optimize other types of musical information (e.g., rhythm), addressing more integrative symbolic music understanding tasks such as the entire functional harmony recognition task and the performance MIDI-to-score conversion task, and identifying pathways for further scaling up our model. 

447 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

### 8. ETHICS STATEMENT 

In this work, all the datasets used in model training and evaluation are publicly available and can be downloaded without submitting any data access application form. While this strict policy improves the reproducibility, it also makes the evaluation biased toward high-resource tasks and music genres that have a larger amount of publicly available data. For example, for classical music, we mainly focus on western classical music instead of classical music from other regions. Future efforts could be made to mitigate this issue by adding more diverse datasets and downstream tasks to the evaluation benchmark. 

### 9. ACKNOWLEDGMENTS 

This work is supported in part by National Science and Technology Council under Grant NSTC 113-2221-E-001013, the Academia Sinica Grand Challenge (GCS) Program under Grant AS–GCS–112–M07, and the Postdoctoral Scholar Program of Academia Sinica under Grant AS-PD-1141-M15-2. 

### 10. REFERENCES 

- [1] Y. Chou, I. Chen, C. Chang, J. Ching, and Y. Yang, “MidiBERT-Piano: Large-scale pre-training for symbolic music understanding,” CoRR, vol. abs/2107.05223, 2021. 

- [2] X. Liang et al., “PianoBART: Symbolic piano music generation and understanding with large-scale pretraining,” in IEEE International Conference on Multimedia and Expo, ICME, 2024, pp. 1–6. 

- [3] Z. Zhao, “Adversarial-midibert: Symbolic music understanding model based on unbias pre-training and mask fine-tuning,” CoRR, vol. abs/2407.08306, 2024. 

- [4] Z. Shen, L. Yang, Z. Yang, and H. Lin, “More than simply masking: Exploring pre-training strategies for symbolic music understanding,” in Proceedings of the 2023 ACM International Conference on Multimedia Retrieval, 2023, p. 540–544. 

- [5] M. Zeng, X. Tan, R. Wang, Z. Ju, T. Qin, and T. Liu, “MusicBERT: Symbolic music understanding with large-scale pre-training,” in Findings of the Association for Computational Linguistics: ACL/IJCNLP, 2021, pp. 791–800. 

- [6] Z. Wang and G. Xia, “MuseBERT: Pre-training music representation for music understanding and controllable generation,” in Proceedings of the 22nd International Society for Music Information Retrieval Conference, ISMIR 2021, 2021, pp. 722–729. 

- [7] M. Sailor, “RNBert: Fine-tuning a masked language model for roman numeral analysis,” in Proceedings of the 25th International Society for Music Information Retrieval Conference, ISMIR, 2024, pp. 814–821. 

- [8] OpenAI, “GPT-4 technical report,” CoRR, vol. abs/2303.08774, 2023. 

- [9] H. Touvron et al., “Llama: Open and efficient foundation language models,” CoRR, vol. abs/2302.13971, 2023. 

- [10] E. Beeching et al., “Open LLM leaderboard,” https://huggingface.co/spaces/HuggingFaceH4/open_ llm_leaderboard, 2023. 

- [11] J. Devlin, M. Chang, K. Lee, and K. Toutanova, “BERT: pre-training of deep bidirectional transformers for language understanding,” in Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, NAACL-HLT, 2019, pp. 4171–4186. 

- [12] A. L. Uitdenbogerd and J. Zobel, “Melodic matching techniques for large music databases,” in Proceedings of the 7th ACM International Conference on Multimedia, 1999, pp. 57–66. 

- [13] F. Simonetta, C. E. C. Chacón, S. Ntalampiras, and G. Widmer, “A convolutional approach to melody line identification in symbolic scores,” in Proceedings of the 20th International Society for Music Information Retrieval Conference (ISMIR), 2019, pp. 924–931. 

- [14] K. Kosta, W. T. Lu, G. Medeot, and P. Chanquion, “A deep learning method for melody extraction from a polyphonic symbolic music representation,” in Proceedings of the 23rd International Society for Music Information Retrieval Conference (ISMIR), 2022, pp. 757–763. 

- [15] N. N. López, M. Gotham, and I. Fujinaga, “AugmentedNet: A roman numeral analysis network with synthetic training examples and additional tonal tasks,” in Proceedings of the 22nd International Society for Music Information Retrieval Conference, ISMIR, 2021, pp. 404–411. 

- [16] E. Karystinaios and G. Widmer, “Roman numeral analysis with graph neural networks: Onset-wise predictions from note-wise features,” in Proceedings of the 24th International Society for Music Information Retrieval Conference, ISMIR, 2023, pp. 597–604. 

- [17] D. Le, L. Bigo, M. Keller, and D. Herremans, “Natural language processing methods for symbolic music generation and information retrieval: a survey,” CoRR, vol. abs/2402.17467, 2024. 

- [18] Y. Hsiao, T. Hung, T. Chen, and L. Su, “Bps-motif: A dataset for repeated pattern discovery of polyphonic symbolic music,” in Proceedings of the 24th International Society for Music Information Retrieval Conference (ISMIR), 2023, pp. 281–288. 

448 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [19] T. Collins, “2013:Discovery of Repeated Themes & Sections,” https://www.music-ir.org/mirex/wiki/2013: Discovery_of_Repeated_Themes_%26_Sections, 2013. 

- [20] D. Meredith, K. Lemström, and G. A. Wiggins, “Algorithms for discovering repeated patterns in multidimensional representations of polyphonic music,” Journal of New Music Research, vol. 31, no. 4, pp. 321–345, 2002. 

- [21] T.-P. Chen and L. Su, “Functional harmony recognition of symbolic music data with multi-task recurrent neural networks,” in Proceedings of the 19th International Society for Music Information Retrieval Conference (ISMIR), 2018, pp. 90–97. 

- [22] Z.-S. Lin et al., “S3: A symbolic music dataset for computational music analysis of symphonies,” in Extended Abstracts for the Late-Breaking Demo Session of the 25th International Society for Music Information Retrieval Conference (ISMIR), 2024. 

- [23] H. Schreiber, “Improving genre annotations for the million song dataset,” in Proceedings of the 16th International Society for Music Information Retrieval Conference, ISMIR, 2015, pp. 241–247. 

- [24] C. Hernandez-Olivan, S. R. Llamas, and J. R. Beltrán, “Symbolic music structure analysis with graph representations and changepoint detection methods,” CoRR, vol. abs/2303.13881, 2023. 

- [25] H. Hung, J. Ching, S. Doh, N. Kim, J. Nam, and Y. Yang, “EMOPIA: A multi-modal pop piano dataset for emotion recognition and emotion-based music generation,” in Proceedings of the 22nd International Society for Music Information Retrieval Conference, ISMIR, 2021, pp. 318–325. 

- [26] J. Zhao and K. Yoshii, “Multimodal multifaceted music emotion recognition based on self-attentive fusion of psychology-inspired symbolic and acoustic features,” in Asia Pacific Signal and Information Processing Association Annual Summit and Conference, APSIPA ASC, 2023, pp. 1641–1645. 

- [27] F. Foscarin, A. McLeod, P. Rigaux, F. Jacquemard, and M. Sakai, “ASAP: a dataset of aligned scores and performances for piano transcription,” in Proceedings of the 21th International Society for Music Information Retrieval Conference, ISMIR, 2020, pp. 534–541. 

- [28] H. Zhang, J. Tang, S. R. Rafee, S. Dixon, G. Fazekas, and G. A. Wiggins, “ATEPP: A dataset of automatically transcribed expressive piano performance,” in Proceedings of the 23rd International Society for Music Information Retrieval Conference, ISMIR, 2022, pp. 446–453. 

- [29] A. Ycart and E. Benetos, “A-MAPS: Augmented MAPS dataset with rhythm and key annotations,” in 

   - 19th International Society for Music Information Retrieval Conference, ISMIR Late Breaking and Demo Papers, 2018. 

- [30] Z. Zhou et al., “Can LLMs "reason" in music? an evaluation of llms’ capability of music understanding and generation,” in Proceedings of the 25th International Society for Music Information Retrieval Conference (ISMIR), 2024. 

- [31] R. Yuan et al., “ChatMusician: Understanding and generating music intrinsically with LLM,” in Findings of the Association for Computational Linguistics, ACL, 2024, pp. 6252–6271. 

- [32] R. Bommasani et al., “On the opportunities and risks of foundation models,” CoRR, vol. abs/2108.07258, 2021. 

- [33] M. Won, Y. Hung, and D. Le, “A foundation model for music informatics,” in IEEE International Conference on Acoustics, Speech and Signal Processing, ICASSP, 2024, pp. 1226–1230. 

- [34] A. Radford et al., “Learning transferable visual models from natural language supervision,” in Proceedings of the 38th International Conference on Machine Learning, ICML, vol. 139, 2021, pp. 8748–8763. 

- [35] S. Yang et al., “SUPERB: speech processing universal performance benchmark,” in Interspeech 2021, 22nd Annual Conference of the International Speech Communication Association, 2021, pp. 1194–1198. 

- [36] S. Chen et al., “WavLM: Large-scale self-supervised pre-training for full stack speech processing,” IEEE Journal of Selected Topics in Signal Processing, vol. 16, no. 6, pp. 1505–1518, 2022. 

- [37] C. Huang et al., “Dynamic-SUPERB Phase-2: A collaboratively expanding benchmark for measuring the capabilities of spoken language models with 180 tasks,” in The Thirteenth International Conference on Learning Representations, ICLR 2025, 2025. 

- [38] Y. Li et al., “MERT: acoustic music understanding model with large-scale self-supervised training,” in The Twelfth International Conference on Learning Representations, ICLR 2024, 2024. 

- [39] W. Liao et al., “Music foundation model as generic booster for music downstream tasks,” CoRR, vol. abs/2411.01135, 2024. 

- [40] R. Castellon, C. Donahue, and P. Liang, “Codified audio language modeling learns useful representations for music information retrieval,” in Proceedings of the 22nd International Society for Music Information Retrieval Conference, ISMIR, 2021, pp. 88–96. 

- [41] S. Wu, Y. Wang, X. Li, F. Yu, and M. Sun, “MelodyT5: A unified score-to-score transformer for symbolic music processing,” in Proceedings of the 25th International Society for Music Information Retrieval Conference, ISMIR, 2024, pp. 642–650. 

449 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [42] W. Hsiao, J. Liu, Y. Yeh, and Y. Yang, “Compound word transformer: Learning to compose full-song music over dynamic directed hypergraphs,” in ThirtyFifth AAAI Conference on Artificial Intelligence, AAAI, 2021, pp. 178–186. 

- [43] A. Vaswani et al., “Attention is all you need,” in Advances in Neural Information Processing Systems 30: Annual Conference on Neural Information Processing Systems, 2017, pp. 5998–6008. 

- [44] B. Warner et al., “Smarter, better, faster, longer: A modern bidirectional encoder for fast, memory efficient, and long context finetuning and inference,” CoRR, vol. abs/2412.13663, 2024. 

- [45] T. Dao, D. Y. Fu, S. Ermon, A. Rudra, and C. Ré, “FlashAttention: fast and memory-efficient exact attention with IO-awareness,” in Advances in Neural Information Processing Systems 35: Annual Conference on Neural Information Processing Systems 2022, NeurIPS, 2022. 

- [46] J. Su, M. H. M. Ahmed, Y. Lu, S. Pan, W. Bo, and Y. Liu, “Roformer: Enhanced transformer with rotary position embedding,” Neurocomputing, vol. 568, p. 127063, 2024. 

   - [53] W. Lin, Y. F. Wang, and L. Su, “Enhancing violin fingering generation through audio-symbolic fusion,” in IEEE International Conference on Acoustics, Speech and Signal Processing, ICASSP, 2024, pp. 811–815. 

   - [54] M. Wortsman, T. Dettmers, L. Zettlemoyer, A. Morcos, A. Farhadi, and L. Schmidt, “Stable and lowprecision training for large-scale vision-language models,” in Advances in Neural Information Processing Systems 36: Annual Conference on Neural Information Processing Systems 2023, NeurIPS, 2023. 

   - [55] C. Raffel, “Learning-based methods for comparing sequences, with applications to audio-to-midi alignment and matching,” Ph.D. dissertation, Columbia University, USA, 2016. 

   - [56] J. Zhao, D. Taniar, K. Adhinugraha, V. M. Baskaran, and K. Wong, “Multi-mmlg: a novel framework of extracting multiple main melodies from MIDI files,” Neural Comput. Appl., vol. 35, no. 30, pp. 22 687–22 704, 2023. 

   - [57] A. Dubey et al., “The Llama 3 herd of models,” CoRR, vol. abs/2407.21783, 2024. 

   - [58] J. Hestness et al., “Deep learning scaling is predictable, empirically,” CoRR, vol. abs/1712.00409, 2017. 

- [47] Y. Meng et al., “Representation deficiency in masked language modeling,” in The Twelfth International Conference on Learning Representations, ICLR, 2024. 

- [48] L. Liu, Q. Kong, V. Morfi, and E. Benetos, “Performance midi-to-score conversion by neural beat tracking,” in Proceedings of the 23rd International Society for Music Information Retrieval Conference, ISMIR, 2022, pp. 395–402. 

- [49] Z. Wang et al., “POP909: A pop-song dataset for music arrangement generation,” in Proceedings of the 21th International Society for Music Information Retrieval Conference, ISMIR 2020, 2020, pp. 38–45. 

- [50] D. Le, M. Giraud, F. Levé, and F. Maccarini, “A corpus describing orchestral texture in first movements of classical and early-romantic symphonies,” in DLfM ’22: 9th International Conference on Digital Libraries for Musicology, 2022, pp. 27–35. 

- [51] Y.-H. Chu and L. Su, “Orchestral texture classification with convolution,” in Extended Abstracts for the LateBreaking Demo Session of the 24th International Society for Music Information Retrieval Conference (ISMIR), 2023. 

- [52] Y.-H. Jen, T.-P. Chen, S.-W. Sun, and L. Su, “Positioning left-hand movement in violin performance: A system and user study of fingering pattern generation,” in Proceedings of the 26th International Conference on Intelligent User Interfaces, 2021, p. 208–212. 

450 

