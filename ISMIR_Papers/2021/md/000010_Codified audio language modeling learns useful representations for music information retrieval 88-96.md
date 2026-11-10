---
paper_id: "000010"
year: 2021
title: "Codified audio language modeling learns useful representations for music information retrieval 88-96"
source_url: "https://archives.ismir.net/ismir2021/paper/000010.pdf"
---

# **CODIFIED AUDIO LANGUAGE MODELING LEARNS USEFUL REPRESENTATIONS FOR MUSIC INFORMATION RETRIEVAL** 

**Rodrigo Castellon**<sup>*****</sup> 

## **Chris Donahue**<sup>*****</sup> **Percy Liang** 

Stanford University 

{rjcaste, cdonahue, pliang}@cs.stanford.edu 

### **ABSTRACT** 

We demonstrate that language models pre-trained on codified (discretely-encoded) music audio learn representations that are useful for downstream MIR tasks. Specifically, we explore representations from Jukebox [1]: a music generation system containing a language model trained on codified audio from 1M songs. To determine if Jukebox’s representations contain useful information for MIR, we use them as input features to train shallow models on several MIR tasks. Relative to representations from conventional MIR models which are pre-trained on tagging, we find that using representations from Jukebox as input features yields 30% stronger performance on average across four MIR tasks: tagging, genre classification, key detection, and emotion recognition. For key detection, we observe that representations from Jukebox are considerably stronger than those from models pre-trained on tagging, suggesting that pre-training via codified audio language modeling may address blind spots in conventional approaches. We interpret the strength of Jukebox’s representations as evidence that modeling audio instead of tags provides richer representations for MIR. 

### **1. INTRODUCTION** 

It is conventional in MIR<sup>1</sup> to _pre-train_ models on large labeled datasets for one or more tasks (commonly tagging), and reuse the learned representations for different _downstream_ tasks [2–10]. Such _transfer learning_ approaches decrease the amount of labeled data needed to perform well on downstream tasks, which is particularly useful in MIR where labeled data for many important tasks is scarce [11, 12]. Historically-speaking, improvement on downstream tasks is enabled by finding ever-larger sources of labels for pre-training—in chronological order: tags [3], metadata [5, 7, 9, 10], and recently, co-listening data [9]. However, it stands to reason that modeling music _audio_ 

> * Equal contribution. 

> 1 MIR has a broad definition, but in this paper “MIR” refers specifically to making discriminative predictions on music audio. 

> © Rodrigo Castellon, Chris Donahue, Percy Liang. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). **Attribution:** Rodrigo Castellon, Chris Donahue, Percy Liang, “Codified audio language modeling learns useful representations for music information retrieval”, in _Proc. of the 22nd Int. Society for Music Information Retrieval Conf.,_ Online, 2021. 

(as opposed to labels) could yield richer representations. Recently, contrastive learning [13] has been proposed as a pre-training strategy to learn representations from audio for MIR [14], but this approach has yet to exceed the performance of label-based pre-training on downstream tasks. 

Outside of the discriminative MIR landscape, a recent system called Jukebox [1] demonstrated promising performance for generating music audio. To achieve this result, Jukebox leverages recent architectural developments from natural language processing (NLP) by _codifying_ audio—encoding high-rate continuous audio waveforms into lower-rate discrete sequences which can be fed in directly to NLP models. Specifically, Jukebox trains a Transformer [15, 16] _language model_ , an autoregressive generative model, on codified audio from 1M songs. Purely for convenience, we refer to Jukebox’s training procedure as _codified audio language modeling_ (CALM). 

While Jukebox already demonstrates that CALM is useful for music _generation_ , in this work we demonstrate that CALM is also useful as a pre-training procedure for _discriminative_ MIR tasks. To this end, we repurpose Jukebox for MIR by first using it to extract audio feature representations, and then training shallow models ( _probes_ [18,19]) on downstream tasks using these features as input (Figure 1). Relative to representations from models pre-trained with tagging, we find that representations from Jukebox are 30% more effective on average when used to train probes on four downstream MIR tasks: tagging, genre classification, key detection, and emotion recognition. We also observe that representations from Jukebox are much more useful for key detection than those from models pre-trained on tagging, which suggests that CALM pre-training may be particularly beneficial for tasks which have little to do with tagging. This simple setup of training shallow models on representations from Jukebox is even competitive with purpose-built state-of-the-art methods on several tasks. 

To facilitate reproducibility [11], we release all of our code for this project, alongside images for Docker containers which provide full provenance for our experiments.<sup>2</sup> We note that, while CALM pre-training at the scale of Jukebox requires substantial computational resources, our post hoc experiments with Jukebox only require a single commodity GPU with 12 GB memory. 

> 2 Code: https://github.com/p-lambda/jukemir Containers: https://hub.docker.com/orgs/jukemir All experiments reproducible on the CodaLab platform: https://worksheets.codalab.org/worksheets/ 0x7c5afa6f88bd4ff29fec75035332a583 

88 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 



<!-- Start of picture text -->
6 7<br>…<br>8 9 7 2 0 0 6 5 0 6 5 2 5 2 0 6<br><!-- End of picture text -->

**Figure 1** . Conventional MIR pre-training ( **left** ) trains convolutional neural networks on audio spectrograms using manually-annotated labels from tagging datasets. In contrast, CALM MIR pre-training ( **middle** ) involves training a language model on codified audio, which has been previously explored for music generation [17,1]—here, we propose to use it for discriminative MIR tasks. To determine if CALM pre-training is effective for MIR, we probe for information about particular MIR tasks ( **right** ) in resultant representations. Specifically, we extract features from the learned language model for the audio in small, task-specific labeled datasets, and use these features to train shallow probing models on each task. 

### **2. CALM PRE-TRAINING** 

CALM was first proposed by van den Oord et al. and used for unconditional speech generation [20]. As input, CALM takes a collection of raw audio waveforms (and optionally, conditioning metadata), and learns a distribution _p_ (audio _|_ metadata). To this end, CALM adopts a threestage approach: (1) _codify_ a high-rate continuous audio signal into lower-rate discrete codes, (2) train a _language model_ on the resulting codified audio and optional metadata, i.e., learn _p_ (codified audio _|_ metadata), and (3) decode sequences generated by the language model to raw audio.<sup>3</sup> The original paper [20] also proposed a strategy for codifying audio called the vector-quantized variational auto-encoder (VQ-VAE), and the language model was a WaveNet [21]. Within music, CALM was first used by Dieleman et al. for unconditional piano music generation [17], and subsequently, Dhariwal et al. used CALM to build a music generation system called Jukebox [1] with conditioning on genre, artist, and optionally, lyrics. 

Despite promising results on music audio generation, CALM has not yet been explored as a pre-training strategy for discriminative MIR. We suspect that effective music audio generation necessitates intermediate representations that would also contain useful information for MIR. This hypothesis is further motivated by an abundance of previous work in NLP suggesting that generative and selfsupervised pre-training can yield powerful representations for discriminative tasks [22–25]. 

To explore this potential, we repurpose Jukebox for MIR. While Jukebox was designed only for generation, its internal language model was trained on codified audio from a corpus of 1 _._ 2M songs from many genres and 

> 3 This third stage is not necessary for transfer learning. 

artists, making its representations potentially suitable for a multitude of downstream MIR tasks. Jukebox consists of two components—the first is a small (2M parameters) VQVAE model [20] that learns to codify high-rate (44 _._ 1 kHz), continuous audio waveforms into lower-rate ( _∼_ 345 Hz), discrete code sequences with a vocabulary size of 2048 (11 bits). The second component is a large (5B parameters) language model that learns to generate codified audio using a Transformer decoder—an architecture originally designed for modeling natural language [15,16]. By training on codified audio (as in [17, 1]) instead of raw audio (as in [21, 16]), language models are (empirically) able to learn longer-term structure in music, while simultaneously using less memory to model the same amount of audio. 

Like conventional MIR models which pre-train on tagging and/or metadata, Jukebox also makes use of genre and artist labels during training, providing them as conditioning information to allow for increased user control for generation. Hence, while CALM in general is an unsupervised strategy that does not require labels, transfer learning from Jukebox specifically should _not_ be considered an unsupervised approach (especially for downstream tasks like genre detection). However, by modeling the _audio_ itself instead of modeling the _labels_ (as in conventional MIR pretraining), we hypothesize that Jukebox learns richer representations for MIR tasks than conventional strategies. 

### **3. EXTRACTING SUITABLE REPRESENTATIONS FROM JUKEBOX** 

Here we describe how we extract audio representations from Jukebox which are suitable as input features for training shallow models. While several pre-trained Jukebox models exist with different sizes and conditioning in- 

89 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 



<!-- Start of picture text -->
1.0<br>0.8<br>0.6<br>Tagging (Magnatagatune)<br>0.4 Genre classification (GTZAN)<br>Emotion recognition (Emomusic)<br>0.2 Key detection (Giantsteps)<br>Average<br>0.0<br>0 10 20 30 40 50 60 70<br>Layer<br>Validation Performance<br><!-- End of picture text -->

**Figure 2** . Normalized validation performance of linear models trained on representations from specific layers of Jukebox across four downstream MIR tasks. On average, the strongest representations for these tasks come from the middle of Jukebox. 

formation, here we use the 5B-parameter model without lyrics conditioning (named “5b”), which is a sparse transformer [15, 16] containing 72 layers. Each layer yields 4800-dimensional activations for each element in the codified audio sequence, i.e., approximately 345 times per second. To extract representations from this model for a particular audio waveform, we (1) resample the waveform to 44 _._ 1kHz, (2) normalize it, (3) codify it using the Jukebox VQ-VAE model, and (4) input the codified audio into the language model, interpreting its layer-wise activations as representations. Jukebox was trained on _∼_ 24-second audio clips (codified audio sequences of length 8192)—we feed in this same amount of audio at a time when extracting representations. In addition to the genre and artist conditioning fields mentioned previously, Jukebox expects two additional fields: total song length and clip offset—to ensure that representations only depend on the input audio, we simply pass in “unknown” for artist and genre, one minute for song length, and zero seconds for clip offset.<sup>4</sup> 

The Jukebox language model yields an unwieldy amount of data—for every 24-second audio clip, it emits 24 _×_ 345 _×_ 72 _×_ 4800 numbers, i.e., over 10GB if stored naively as 32-bit floating point. We reduce the amount of data by mean pooling across time, a common strategy in MIR transfer learning [4, 8], which aggregates more than 10GB of activations to around 1MB (72 _×_ 4800). 

### **3.1 Layer selection** 

While pooling across time dramatically reduced the dimensionality of Jukebox’s outputs, training shallow classifiers on 72 _×_ 4800 features is still computationally expensive. To further reduce the dimensionality, we use only one of the layers from Jukebox—the middle layer (36)—yielding a total of 4800 features per 24 second audio clip. Unlike conventional pre-training, where the strongest representations for transfer learning typically lie at the end of the network [26], the strongest representations from pre-trained 

> 4 We observed in initial experiments that passing in ground-truth conditioning information had little effect on downstream performance. Hence, we elected to pass in placeholder metadata to maintain the typical type signature for audio feature extraction (audio as the only input). 

|Task|Size|Metrics|#Out|
|---|---|---|---|
|Tagging [31]|25860|AUC/AP|50|
|Genre classification [32]|930|Accuracy|10|
|Key detection [33]|1763|Score|24|
|Emotion recognition [34]|744|A/V_R_<sup>2</sup>|2|



**Table 1** . Basic information about the four tasks we consider in this work, including the size of each task-specific dataset in terms of number of labeled examples, relevant metrics for each task, and the number of model outputs required for each dataset. 

language models tend to lie towards the middle [27–30]. To confirm this observation in our context, we trained linear models using representations from different layers of Jukebox on our downstream MIR tasks—average performance indeed peaked at the middle layers (Figure 2). 

In addition to using the middle layer, we experimented with two other layer selection strategies: (1) sub-sampling layers across the network, and (2) selecting relevant layers in a task-specific fashion.<sup>5</sup> We found that the simplest strategy of using only the middle layer was equally effective and more computationally practical<sup>6</sup> than the other two layer selection strategies. 

### **4. DOWNSTREAM TASK DESCRIPTIONS** 

We select four downstream MIR tasks to constitute a benchmark for comparing different audio feature representations: (1) tagging, (2) genre classification, (3) key detection, and (4) emotion recognition. A summary of the datasets used for each task appears in Table 1. These tasks were selected to cover a wide range of dataset sizes (744 examples for emotion recognition vs. 26k examples for tagging) and subjectivity (emotion recognition is more subjective vs. key detection is more objective). Additionally, each task has a public dataset with standard evaluation metrics. We describe each of these tasks below. 

### **4.1 Tagging** 

Tagging involves determining which tags from a fixed set of tags apply to a particular song. Categories of tags include genre (e.g., jazz), instrumentation (e.g., violin), emotions (e.g., happy), and characteristics (e.g., fast). There are two large datasets for tagging, which both contain human-annotated tags for 30-second clips: MagnaTagATune [31] (MTT) which contains around 26k clips, and a tagged subset of 240k clips from the Million Song Dataset [35] (MSD). While both datasets contain a large vocabulary of tags, typical usage involves limiting the vocabulary to the 50 most common tags in each. 

Because it is the largest non-proprietary MIR dataset, MSD is commonly used for pre-training models for transfer learning. To mitigate an unfair advantage of methods 

> 5 This procedure selected layers that were the most jointly informative in a greedy fashion, measured by task performance with a linear probe. 

> 6 While the entirety of Jukebox does _not_ fit on a single commodity GPU with 12GB memory, the first 36 layers _do_ fit. 

90 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

which pre-train on MSD, we use MTT instead of MSD to benchmark representations on tagging performance. While both datasets are superficially similar (choosing from 50 tags for 30-second clips), their label distributions are quite different: MSD is skewed towards genre tags, while MTT is skewed towards instrumentation tags. 

We use the standard (12:1:3) train, validation, and test split for MTT [3]. Additionally, we report both common metrics (both are macro-averaged over tags): area under the receiver operating characteristic curve (MTTAUC), and average precision (MTTAP).<sup>7</sup> Note that inconsistencies in handling unlabeled examples for past work on MTT have been observed [36]—some work discards examples without top-50 tags during training, evaluation, both, or neither. In this work, we do not discard any examples. 

### **4.2 Genre classification** 

Genre classification involves assigning the most appropriate genre from a fixed list for a given song. For this task, we report accuracy on the GTZAN dataset [37], which contains 30-second clips from 10 distinct genres. We adopt the “fault-filtered” split from [32] which addresses some of the reported issues with this dataset [38]. We note that this task has a high degree of overlap with tagging, as tagging datasets typically have a number of genres within their tag vocabulary. In fact, seven of ten genres in GTZAN are present in the tag list of MSD. 

### **4.3 Key detection** 

Key detection involves predicting both the scale and tonic pitch class for the underlying key of a song. We investigate the Giantsteps-MTG and Giantsteps datasets [33] which include songs in major and minor scales for all pitch classes, i.e., a 24-way classification task. As in past work [39], we use the former for training and the latter for testing. Because no standard validation split exists for Giantsteps-MTG, we follow [32] and create an artiststratified 4:1 split for training and validation, which we include in our codebase for reproducibility. The music in this dataset is all electronic dance music, and the clips are two minutes in length. We report the typical weighted score metric for Giantsteps (GS): an accuracy measure which gives partial credit for reasonable mistakes such as predicting the relative minor key for the major ground truth [40]. 

### **4.4 Emotion recognition** 

Emotion recognition involves predicting human emotional response to a song. Data is collected by asking humans to report their emotional response on a two dimensional valence-arousal plane [41], where valence indicates positive versus negative emotional response, and arousal indicates emotional intensity. We use the Emomusic dataset [34], which contains 744 clips of 45 seconds in length. We investigate the static version of this task 

> 7 Most past work refers to the quantity of average precision as area under the precision-recall curve. 

|Representation|Pre-training strategy|Dimensions|
|---|---|---|
|CHROMA|N/A|72|
|MFCC|N/A|120|
|CHOI[4]|MSD Tagging [3]|160|
|MUSICNN [8]|MSD Tagging [3]|4194|
|CLMR [14]|Contrastive [13]|512|
|JUKEBOX[1]|CALM [20]|4800|



**Table 2** . Basic statistics about the six representations we examine in this work. 

where original time-varying annotations are averaged together to constitute a clip-level annotation. Because this dataset does not have a standard split, it is difficult to directly compare with past work. To simplify comparison going forward, we created an artist-stratified split of Emomusic, which is released in our codebase. We take the highest reported numbers from past work to characterize “state-of-the-art” performance, though we note that these numbers are not directly comparable to our own due to differing splits. We report the coefficient of determination between the model predictions and human annotations for arousal (EmoA) and valence (EmoV). 

### **5. PROBING EXPERIMENTS** 

Here we describe our protocol for probing for information about MIR tasks in representations from Jukebox and other pre-trained models, i.e., measuring performance of shallow models trained on these tasks using different representations as input features. We borrow the term “probing” from analogous investigations in NLP [19,42,43], however such methodology is common in MIR [2–5,7–10]. 

### **5.1 Descriptions of representations** 

In addition to probing representations from Jukebox (an exemplar of CALM pre-training), we probe four additional representations which are emblematic of three other MIR pre-training strategies (Table 2). Before pre-training, handcrafted features were commonplace in MIR—as archetypal examples, we probe constant-Q chromagrams (CHROMA) and Mel-frequency cepstral coefficients (MFCC), extracted with librosa [49] using the default settings. As in [4], we concatenate the mean and standard deviation across time of both the features and their first- and secondorder discrete differences. We also probe two examples of the current conventional paradigm which pre-trains on tagging using MSD: a convolutional model proposed by Choi et al. [4] (CHOI), and a more modern convolutional model from [8] (MUSICNN). Finally, we compare to a recent MIR pre-training strategy called _contrastive learning of musical representations_ [14] (CLMR), though we note that CLMR was trained on far less audio (a few thousand songs) than the other pre-trained models. 

All of these strategies operate at different frame rates, i.e., they produce a different number of representation vectors for a fixed amount of input audio. To handle 

91 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

||Ta|gs|Genre|Key|Emo|tion||
|---|---|---|---|---|---|---|---|
|Approach|MTTAUC|MTTAP|GTZAN|GS|EmoA|EmoV|Average|
|(No pre-training) Probing CHROMA|77_._6|18_._5|32_._8|56_._5|29_._3|5_._9|38_._7|
|(No pre-training) Probing MFCC|85_._8|30_._2|44_._8|14_._6|47_._9|26_._5|38_._7|
|(Tagging) Probing CHOI[4]|89_._7|36_._4|75_._9|13_._1|67_._3|43_._4|51_._9|
|(Tagging) Probing MUSICNN [8]|90_._6|38_._3|79_._0|12_._8|70_._3|46_._6|53_._7|
|(Contrastive) Probing CLMR [14]|89_._4|36_._1|68_._6|14_._9|67_._8|45_._8|50_._8|
|(CALM) Probing JUKEBOX[1]|**91**_._**5**|**41**_._**4**|**79**_._**7**|**66**_._**7**|**72**_._**1**|**61**_._**7**|**69**_._**9**|
|State-of-the-art [9,8,6,44–46]|**92**_._**0**|38_._4|**82**_._**1**|**79**_._**6**|70_._4*|55_._6*|**72**_._**5***|
|Pre-trained [9,14,6,45,45,47]|**92**_._**0**|35_._9|**82**_._**1**|75_._8|67_._1*|55_._6*|70_._8*|
|From scratch [8,8,48,44,44,39]|90_._7|38_._4|65_._8|74_._3|70_._4*|50_._0*|66_._2*|



**Table 3** . Comparing performance of probes on representations from a model pre-trained with CALM to other pretrained MIR models (top section) to reported state-of-the-art performance (bottom section) across four tasks: (1) tagging (MTTAUC/MTTAP), (2) genre classification (GTZAN), (3) key detection (GS), and (4) emotion recognition (EmoA/EmoV). For all six metrics, the max score is 100 and higher is better—see Section 4 for a full description of tasks/metrics. For each metric, the best probing-based approach and the best approach overall are **bolded** . We also report an average score across all four tasks; tasks with multiple evaluation metrics are averaged beforehand. On all metrics, probing JUKEBOX is more effective than probing representations from other pre-trained models. Probing JUKEBOX is competitive with task-specific state-of-the-art approaches for all tasks/metrics except key detection (GS). Note that the ordering of citations in the bottom section corresponds to respective column ordering. * indicates that past work on Emomusic evaluates on different subsets of the dataset than our work and hence numbers are not directly comparable—see Section 4.4 for details. 

this, we follow common practice of mean pooling representations across time [4, 8]. While CHROMA, MFCC, and CLMR produce a single canonical representation per frame, we note that the other three produce multiple representations per frame, i.e., the activations of individual network layers. For CHOI, we concatenate all layer activations together, which was shown to have strong performance on all downstream tasks in [4]. For MUSICNN, we concatenate together the mean and max pool of threesecond windows (before mean pooling across these windows), i.e., the default configuration for that approach. For JUKEBOX, we use the middle layer activations as motivated in Section 3.1. By using a single layer, we mitigate the potential of a superficial dimensionality advantage for JUKEBOX, as this induces a dimensionality similar to that of MUSICNN (4800 and 4194 respectively; see Table 2). 

Unlike other representations which operate on short audio windows, CHOI and JUKEBOX were trained on long windows (29 seconds and 24 seconds respectively). Accordingly, for the three datasets with short clips (tagging, genre classification, and emotion recognition all have clips between 30 and 45 seconds in length), we adopt the policy from [4] and simply truncate the clips to the first window when computing representations for CHOI and JUKEBOX. Because clips from the key detection dataset are longer (two minutes), we split the clips into 30-second windows for all methods and train probes on these shorter windows. At test time, we ensemble window-level predictions into clip-level predictions before computing the score. 

### **5.2 Probing protocol** 

To probe representations for relevant information about downstream MIR tasks, we train shallow supervised mod- 

els (linear models and one-layer MLPs) on each task using these representations as input features. As some representations may require different hyperparameter configurations for successful training, we run a grid search over the following hyperparameters (216 total configurations) for each representation and task (24 total grid searches), using early stopping based on task-specific metrics computed on the validation set of each task: 

- Feature standardization: {off, on} 

- Model: {Linear, one-layer MLP with 512 hidden units} 

- Batch size: {64, 256} 

- Learning rate: {1e-5, 1e-4, 1e-3} 

- Dropout probability: {0 _._ 25, 0 _._ 5, 0 _._ 75} 

- L2 regularization: {0, 1e-4, 1e-3} 

While we use this same hyperparameter grid for all tasks, the learning objective varies by task (cross-entropy for genre classification and key detection, independent binary cross-entropy per tag for tagging, and mean squared error for emotion recognition) as does the number of probe outputs (Table 1). Some tasks have multiple metrics—we early stop on MTTAUC for tagging as it is a more common metric than MTTAP, and on the average of EmoA and EmoV for emotion recognition. We take the model with the best early stopping performance from each grid search and compute its performance on the task-specific test set. 

### **6. RESULTS AND DISCUSSION** 

In Table 3, we report performance of all representations on all tasks and metrics, as well as average performance across all tasks. Results are indicative that CALM is a promising paradigm for MIR pre-training. Specifically, we observe that probing the representations from JUKEBOX 

92 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

(learned through CALM pre-training) achieves an average of 69 _._ 9, which is 30% higher relative to the average of the best representation pre-trained with tagging (MUSICNN achieves an average of 53 _._ 7). Performance of JUKEBOX on all individual metrics is also higher than that of any other representation. Representations from all pre-trained models outperform hand-crafted features (CHROMA and MFCC) on average. Note that these results are holistic comparisons across different model architectures, model sizes, and amounts of pre-training data (e.g., CLMR was trained on far less data than JUKEBOX), and hence not sufficient evidence to claim that CALM is the “best” music pre-training strategy in general. 

We also observe that JUKEBOX contains substantially more information relevant for key detection than other representations. While CHROMA (spectrogram projected onto musical pitch classes) contains information relevant to key detection by design, all other representations besides JUKEBOX yield performance on par with that of a majority classifier (outputting “F minor” for every example scores 15 _._ 0)—hence, these representations contain almost no information about this task. For models pre-trained with tagging (CHOI and MUSICNN), intuition suggests that this is because none of the tags in MSD relate to key signature. For CLMR, we speculate that the use of transposition as a data augmentation strategy removes information about key signature. While tagging and CLMR were not designed with the intention of supporting transfer to key detection, we argue that it is generally desirable to have a unified music representation which performs well on many downstream MIR tasks. Hence, we interpret the comparatively stronger performance of JUKEBOX on key detection as evidence that CALM pre-training addresses blind spots present in other MIR pre-training paradigms. 

In the bottom section of Table 3, we also report state-ofthe-art performance for purpose-built methods on all tasks, which is further broken down by models which use any form of pre-training (including pre-training on additional task-specific data as in [47]) vs. ones that are trained from scratch. Surprisingly, we observe that probing JUKEBOX is competitive with state-of-the-art for all tasks except for key detection, and achieves an average only 4% lower relative to that of state-of-the-art. On tagging, probing JUKEBOX achieves similar MTTAUC to a strategy which pre-trains on a proprietary dataset of 10M songs using supervision [9]. We interpret the strong performance of this simple probing setup as evidence that CALM pre-training is a promising path towards models that are useful for many MIR tasks. 

We believe that CALM pre-training is promising for MIR not just because of the strong performance of an existing model (Jukebox), but also because there are numerous avenues which may yield further improvements. Firstly, CALM could be scaled up to pre-train even larger models on more data (Jukebox was trained on 1M songs, while Spotify has an estimated 70M songs in its catalog). In [50], it is observed that increasing model and dataset size yields predictable improvements to cross-entropy for language modeling in NLP, an insight which may also 

hold for CALM pre-training for MIR. Secondly, we anticipate that fine-tuning a model pre-trained with CALM would outperform our probing setup. Finally, taking a cue from related findings in NLP, we speculate that CALM pretraining with a bidirectional model and masked language modeling (as in BERT [23]) would outperform the generative setup of Jukebox (that of GPT [51]). 

### **7. RELATED WORK** 

Transfer learning has been an active area of study in MIR for over a decade [52,53,2,54]. The predominant strategy for MIR pre-training using large tagging datasets was first proposed by van den Oord et al. 2014 [3]. This work pretrained deep neural networks on MSD and demonstrated promising performance on other tagging and genre classification tasks. Choi et al. 2017 [4] pre-trained a convolutional neural network on MSD and also explored a more diverse array of downstream tasks—we use their pre-trained model as a baseline. More recent improvements use the same approach with different architectures [6,8]. 

Other strategies for MIR transfer learning have been proposed. Some work pre-trains on music metadata (e.g., artist, album) instead of tags [5, 7]. In contrast to the manual annotations required for tagging-based pretraining, metadata is much cheaper to obtain, but performance of pre-training on metadata is comparable to that of pre-training on tagging. Kim et al. 2020 [10] improve over Choi et al. 2017 [4] using a multi-task approach. Huang et al. [9] demonstrate that metadata can be combined with proprietary co-listening data for pre-training on 10M songs to achieve state-of-the-art performance on MTT—probing representations from CALM pre-training on 1M songs achieves comparable performance (Table 3). Finally, contrastive learning [13] has been proposed for MIR pre-training [55,56,14]—we compare to [14]. 

While CALM has not previously been explored for MIR transfer learning, it has been explored for other purposes. van den Oord et al. 2017 [20] first proposed CALM and used it for unconditional speech generation. Variations of CALM have been explored for speech recognition [57,58] and urban sound classification [59]. CALM has also been explored for music generation [17, 1]. Language models have been used extensively for symbolic music [60–62], including work on pre-training [63,64]. 

### **8. CONCLUSION** 

In this work we demonstrated that CALM is a promising pre-training strategy for MIR. Compared to conventional approaches, CALM learns richer representations by modeling audio instead of labels. Moreover, CALM allows MIR researchers to repurpose NLP methodology— historically, repurposing methodology from another field (computer vision) has provided considerable leverage for MIR. Finally, CALM suggests a direction for MIR research where enormous models pre-trained on large music catalogs break new ground on MIR tasks, analogous to ongoing paradigm shifts in other areas of machine learning. 

93 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

**9. ACKNOWLEDGEMENTS** [13] T. Chen, S. Kornblith, M. Norouzi, and G. Hinton, “A simple framework for contrastive learning of visual 

like to thank Nelson Liu, Mina Lee, John Herepresentations,” in _ICML_ , 2020. 

We would like to thank Nelson Liu, Mina Lee, John Hewitt, Janne Spijkervet, Minz Won, Jordi Pons, Ethan Chi, Michael Xie, Ananya Kumar, and Glen Husman for helpful conversations about this work. We also thank all reviewers for their helpful feedback. 

- [14] J. Spijkervet and J. A. Burgoyne, “Contrastive learning of musical representations,” _arXiv:2103.09410_ , 2021. 

- [15] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. Kaiser, and I. Polosukhin, “Attention is all you need,” _arXiv:1706.03762_ , 2017. 

### **10. REFERENCES** 

- [1] P. Dhariwal, H. Jun, C. Payne, J. W. Kim, A. Radford, and I. Sutskever, “Jukebox: A generative model for music,” _arXiv:2005.00341_ , 2020. 

   - [16] R. Child, S. Gray, A. Radford, and I. Sutskever, “Generating long sequences with sparse transformers,” _arXiv:1904.10509_ , 2019. 

- [2] P. Hamel, M. Davies, K. Yoshii, and M. Goto, “Transfer learning in MIR: Sharing learned latent representations for music audio classification and similarity,” in _ISMIR_ , 2013. 

   - [17] S. Dieleman, A. van den Oord, and K. Simonyan, “The challenge of realistic music generation: modelling raw audio at scale,” in _NIPS_ , 2018. 

- [3] A. van den Oord, S. Dieleman, and B. Schrauwen, “Transfer learning by supervised pre-training for audio-based music classification,” in _ISMIR_ , 2014. 

   - [18] G. Alain and Y. Bengio, “Understanding intermediate layers using linear classifier probes,” _arXiv:1610.01644_ , 2016. 

- [4] K. Choi, G. Fazekas, M. Sandler, and K. Cho, “Transfer learning for music classification and regression tasks,” in _ISMIR_ , 2017. 

   - [19] D. Hupkes, S. Veldhoen, and W. Zuidema, “Visualisation and ‘diagnostic classifiers’ reveal how recurrent and recursive neural networks process hierarchical structure,” _Journal of Artificial Intelligence Research_ , 2018. 

- [5] J. Park, J. Lee, J. Park, J.-W. Ha, and J. Nam, “Representation learning of music using artist labels,” _arXiv:1710.06648_ , 2017. 

   - [20] A. van den Oord, O. Vinyals, and K. Kavukcuoglu, “Neural discrete representation learning,” _arXiv:1711.00937_ , 2017. 

- [6] J. Lee, J. Park, K. L. Kim, and J. Nam, “SampleCNN: End-to-end deep convolutional neural networks using very small filters for music classification,” _Applied Sciences_ , 2018. 

   - [21] A. van den Oord, S. Dieleman, H. Zen, K. Simonyan, O. Vinyals, A. Graves, N. Kalchbrenner, A. Senior, and K. Kavukcuoglu, “WaveNet: A generative model for raw audio,” _arXiv:1609.03499_ , 2016. 

- [7] J. Lee, J. Park, and J. Nam, “Representation learning of music using artist, album, and track information,” _arXiv:1906.11783_ , 2019. 

- [8] J. Pons and X. Serra, “musicnn: Pre-trained convolutional neural networks for music audio tagging,” _ISMIR Late-breaking Demos_ , 2019. 

   - [22] M. E. Peters, M. Neumann, M. Iyyer, M. Gardner, C. Clark, K. Lee, and L. Zettlemoyer, “Deep contextualized word representations,” in _North American Chapter of the Association for Computational Linguistics: Human Language Technologies_ , 2018. 

- [9] Q. Huang, A. Jansen, L. Zhang, D. P. Ellis, R. A. Saurous, and J. Anderson, “Large-scale weaklysupervised content embeddings for music recommendation and tagging,” in _ICASSP_ , 2020. 

   - [23] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, “BERT: Pre-training of deep bidirectional transformers for language understanding,” in _North American Chapter of the Association for Computational Linguistics: Human Language Technologies_ , 2018. 

- [10] J. Kim, J. Urbano, C. C. Liem, and A. Hanjalic, “One deep music representation to rule them all? A comparative analysis of different representation learning strategies,” _Neural Computing and Applications_ , 2020. 

   - [24] A. Radford, J. Wu, R. Child, D. Luan, D. Amodei, and I. Sutskever, “Language models are unsupervised multitask learners,” _OpenAI Blog_ , 2019. 

- [11] B. McFee, J. W. Kim, M. Cartwright, J. Salamon, R. M. Bittner, and J. P. Bello, “Open-source practices for music signal processing research: Recommendations for transparent, sustainable, and reproducible audio research,” _IEEE Signal Processing Magazine_ , 2018. 

   - [25] X. Liu, Y. Zheng, Z. Du, M. Ding, Y. Qian, Z. Yang, and J. Tang, “GPT understands, too,” _arXiv:2103.10385_ , 2021. 

- [12] W. Chen, J. Keast, J. Moody, C. Moriarty, F. Villalobos, V. Winter, X. Zhang, X. Lyu, E. Freeman, J. Wang _et al._ , “Data usage in MIR: history & future recommendations,” in _ISMIR_ , 2019. 

- [26] M. D. Zeiler and R. Fergus, “Visualizing and understanding convolutional networks,” in _European Conference on Computer Vision_ , 2014. 

94 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

- [27] N. F. Liu, M. Gardner, Y. Belinkov, M. E. Peters, and N. A. Smith, “Linguistic knowledge and transferability of contextual representations,” _arXiv:1903.08855_ , 2019. 

- [28] M. Chen, A. Radford, R. Child, J. Wu, H. Jun, D. Luan, and I. Sutskever, “Generative pretraining from pixels,” in _ICML_ , 2020. 

- [29] E. A. Chi, J. Hewitt, and C. D. Manning, “Finding universal grammatical relations in multilingual bert,” in _Association for Computational Linguistics_ , 2020. 

- [30] A. Rogers, O. Kovaleva, and A. Rumshisky, “A primer in BERTology: What we know about how BERT works,” _Transactions of the Association for Computational Linguistics_ , 2020. 

- [31] E. Law, K. West, M. I. Mandel, M. Bay, and J. S. Downie, “Evaluation of algorithms using games: The case of music tagging.” in _ISMIR_ , 2009. 

- [32] C. Kereliuk, B. L. Sturm, and J. Larsen, “Deep learning and music adversaries,” _IEEE Transactions on Multimedia_ , 2015. 

- [33] P. Knees, Á. Faraldo Pérez, H. Boyer, R. Vogl, S. Böck, F. Hörschläger, M. Le Goff _et al._ , “Two data sets for tempo estimation and key detection in electronic dance music annotated from user corrections,” in _ISMIR_ , 2015. 

- [34] M. Soleymani, M. N. Caro, E. M. Schmidt, C.-Y. Sha, and Y.-H. Yang, “1000 songs for emotional analysis of music,” in _ACM International Workshop on Crowdsourcing for Multimedia_ , 2013. 

- [35] T. Bertin-Mahieux, D. P. Ellis, B. Whitman, and P. Lamere, “The Million Song Dataset,” in _ISMIR_ , 2011. 

- [36] M. Won, A. Ferraro, D. Bogdanov, and X. Serra, “Evaluation of CNN-based automatic music tagging models,” _arXiv:2006.00751_ , 2020. 

- [37] G. Tzanetakis and P. Cook, “Musical genre classification of audio signals,” _IEEE Transactions on Speech and Audio Processing_ , 2002. 

- [38] B. L. Sturm, “The GTZAN dataset: its contents, its faults, their effects on evaluation, and its future use,” _arXiv:1306.1461_ , 2013. 

- [39] F. Korzeniowski and G. Widmer, “End-to-end musical key estimation using a convolutional neural network,” in _European Signal Processing Conference_ , 2017. 

- [40] C. Raffel, B. McFee, E. J. Humphrey, J. Salamon, O. Nieto, D. Liang, and D. P. Ellis, “mir_eval: A transparent implementation of common mir metrics,” in _ISMIR_ , 2014. 

- [41] A. Huq, J. P. Bello, and R. Rowe, “Automated music emotion recognition: A systematic evaluation,” _Journal of New Music Research_ , 2010. 

- [42] A. Conneau, G. Kruszewski, G. Lample, L. Barrault, and M. Baroni, “What you can cram into a single vector: Probing sentence embeddings for linguistic properties,” _arXiv:1805.01070_ , 2018. 

- [43] J. Hewitt and C. D. Manning, “A structural probe for finding syntax in word representations,” in _North American Chapter of the Association for Computational Linguistics: Human Language Technologies_ , 2019. 

- [44] F. Weninger, F. Eyben, and B. Schuller, “On-line continuous-time music mood regression with deep recurrent neural networks,” in _ICASSP_ , 2014. 

- [45] E. Koh and S. Dubnov, “Comparison and analysis of deep audio embeddings for music emotion recognition,” _arXiv:2104.06517_ , 2021. 

- [46] Pioneer, “rekordbox v3.2.2,” 2015. [Online]. Available: http://www.cp.jku.at/datasets/giantsteps/ 

- [47] J. Jiang, G. G. Xia, and D. B. Carlton, “MIREX 2019 submission: Crowd annotation for audio key estimation,” _MIREX_ , 2019. 

- [48] F. Medhat, D. Chesmore, and J. Robinson, “Masked conditional neural networks for audio classification,” in _International Conference on Artificial Neural Networks_ , 2017. 

- [49] B. McFee, C. Raffel, D. Liang, D. P. Ellis, M. McVicar, E. Battenberg, and O. Nieto, “librosa: Audio and music signal analysis in python,” in _Python in Science Conference_ , 2015. 

- [50] J. Kaplan, S. McCandlish, T. Henighan, T. B. Brown, B. Chess, R. Child, S. Gray, A. Radford, J. Wu, and D. Amodei, “Scaling laws for neural language models,” _arXiv:2001.08361_ , 2020. 

- [51] A. Radford, K. Narasimhan, T. Salimans, and I. Sutskever, “Improving language understanding by generative pre-training,” _OpenAI Blog_ , 2018. 

- [52] P. Hamel and D. Eck, “Learning features from music audio with deep belief networks,” in _ISMIR_ , 2010. 

- [53] J. Weston, S. Bengio, and P. Hamel, “Multi-tasking with joint semantic spaces for large-scale music annotation and retrieval,” _Journal of New Music Research_ , 2011. 

- [54] K. Seyerlehner, M. Schedl, R. Sonnleitner, D. Hauger, and B. Ionescu, “From improved auto-taggers to improved music similarity measures,” in _International Workshop on Adaptive Multimedia Retrieval_ , 2012. 

- [55] X. Favory, K. Drossos, T. Virtanen, and X. Serra, “Learning contextual tag embeddings for cross-modal alignment of audio and tags,” _arXiv:2010.14171_ , 2020. 

95 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

- [56] A. Ferraro, X. Favory, K. Drossos, Y. Kim, and D. Bogdanov, “Enriched music representations with multiple cross-modal contrastive learning,” _IEEE Signal Processing Letters_ , 2021. 

- [57] A. Baevski, M. Auli, and A. Mohamed, “Effectiveness of self-supervised pre-training for speech recognition,” _arXiv:1911.03912_ , 2019. 

- [58] A. Baevski, H. Zhou, A. Mohamed, and M. Auli, “wav2vec 2.0: A framework for self-supervised learning of speech representations,” _arXiv:2006.11477_ , 2020. 

- [59] P. Verma and J. Smith, “A framework for contrastive and generative learning of audio representations,” _arXiv:2010.11459_ , 2020. 

- [60] D. Eck and J. Schmidhuber, “Finding temporal structure in music: Blues improvisation with LSTM recurrent networks,” in _IEEE Workshop on Neural Networks for Signal Processing_ , 2002. 

- [61] I. Simon and S. Oore, “Performance RNN: Generating music with expressive timing and dynamics,” 2017. [Online]. Available: https://magenta.tensorflow.org/ performance-rnn 

- [62] C.-Z. A. Huang, A. Vaswani, J. Uszkoreit, N. Shazeer, I. Simon, C. Hawthorne, A. M. Dai, M. D. Hoffman, M. Dinculescu, and D. Eck, “Music transformer,” in _ICLR_ , 2019. 

- [63] C. Donahue, H. H. Mao, Y. E. Li, G. W. Cottrell, and J. McAuley, “LakhNES: Improving multi-instrumental music generation with cross-domain pre-training,” in _ISMIR_ , 2019. 

- [64] H.-T. Hung, C.-Y. Wang, Y.-H. Yang, and H.-M. Wang, “Improving automatic jazz melody generation by transfer learning techniques,” in _Asia-Pacific Signal and Information Processing Association Annual Summit and Conference_ , 2019. 

96 

