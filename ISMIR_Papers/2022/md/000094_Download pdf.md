---
paper_id: "000094"
year: 2022
title: "Download pdf"
source_url: "https://zenodo.org/record/7316780/files/000094.pdf"
---

# SAMPLEMATCH: DRUM SAMPLE RETRIEVAL BY MUSICAL CONTEXT 

## Stefan Lattner 

Sony Computer Science Laboratories (CSL), Paris, France stefan.lattner@sony.com 

### ABSTRACT 

Modern digital music production typically involves combining numerous acoustic elements to compile a piece of music. Important types of such elements are drum samples, which determine the characteristics of the percussive components of the piece. Artists must use their aesthetic judgement to assess whether a given drum sample fits the current musical context. However, selecting drum samples from a potentially large library is tedious and may interrupt the creative flow. In this work, we explore the automatic drum sample retrieval based on aesthetic principles learned from data. As a result, artists can rank the samples in their library by fit to some musical context at different stages of the production process (i.e., by fit to incomplete song mixtures). To this end, we use contrastive learning to maximize the score of drum samples originating from the same song as the mixture. We conduct a listening test to determine whether the human ratings match the automatic scoring function. We also perform objective quantitative analyses to evaluate the efficacy of our approach. 

### 1. INTRODUCTION 

Machine-learning (ML) powered tools are increasingly finding their way into modern music production [1]. Commercial tools already use machine learning for different applications, like mixing/mastering<sup>1</sup> or data visualization.<sup>2</sup> In public perception, ML and artificial intelligence (AI) is often associated with content generation. Indeed, also in music production, generative AI models are about to transition from research labs to the studio, in the form of tools that integrate seamlessly into the artist’s workflow, like Magenta Studio<sup>3</sup> and others [2–6]. 

Besides content generation, another frequent task in modern music production is content retrieval, where commercial solutions (based on expert systems) also already exist.<sup>4</sup> In manual content retrieval (i.e., content selection), artists select “loops” (short, typically bar-aligned audio files 

1 https://www.izotope.com/ 2 https://algonaut.audio/ 

3 https://magenta.tensorflow.org/studio/ 4 https://jamahook.com/ 

⃝c Stefan Lattner. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: Stefan Lattner, “SampleMatch: Drum Sample Retrieval by Musical Context”, in Proc. of the 23rd Int. Society for Music Information Retrieval Conf., Bengaluru, India, 2022. 

of any content) or “samples” (usually shorter, single notes or drum hits) that fit the current musical context. Content selection is a creative act in its own right, but it is challenging to browse through potentially large loop or sample libraries while – crucially – keeping the current context in mind. 

To support the selection process, we envision a retrieval system that learns aesthetic principles of matching drum samples to musical context from data. As a result, it is able to sort a drum sample library according to a score it assigns to each sample. This lets users start their search with the most promising options first and may help turn a cumbersome curation process into a more artistic activity. 

We use the cosine similarity in a learned latent space as a scoring function. Two encoders are trained with a contrastive loss to maximize the score between mixtures and drum samples originating from the same song. The encoders are trained with an electronic and acoustic data set of songs whose tracks are available separately. We perform a user study to evaluate if human listeners agree with our proposed scoring function. To that end, we test if participants prefer samples that obtain a high rating by the scoring function over randomly selected samples. Furthermore, we perform an ablation study to evaluate the different components of our method. In addition, we want to understand better how the learned space is organized. In particular, we want to gain some insights into the relationship of drum samples that fit well in the same context. For that, we perform a correlation analysis between audio features of samples that are close in the learned latent space. 

The paper is organized as follows. Related works are discussed in Section 2, and Section 3 describes the used method. The used data and data preprocessing are described in Section 4. Section 5 explaines how the model training is performed. In Section 6, we introduce the performed experiments, including the objective evaluation, a user study and correlation analysis. We present and discuss the results in Section 7 and conclude in Section 8. 

### 2. RELATED WORK 

Self-supervised learning has been a hot topic in recent years, with well-known works in the visual domain, like MoCo [7] and SimCLR [8] that adopt contrastive learning approaches, and BYOL [9], or VICReg [10] that aim to eliminate negative samples. Examples for contrastive approaches in the speech domain are Wav2Vec [11], Wav2Vec 2.0 [12], as well as SpeechSimCLR [13]. Inspired by these works, self-supervised learning in non-speech (i.e., musical and 

781 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

environmental) audio was also introduced with contrastive approaches [14,15], Audio2Vec [16] and Wav2Vec for nonspeech audio using a conformer architecture [17]. An example for self-supervised learning for audio based on the BYOL method is [18]. Other audio-related contributions based on contrastive learning are multimodal contrastive learning (for audio and video) [19], as well as multi-format contrastive learning (between raw audio and spectrogram representations) [20]. We adopt ideas from self-supervised learning methods mentioned above, using a dictionary lookup approach like in MoCo [7], we adopt the variance- and co-variance regularization of VICReg [10], and we use decoupled contrastive learning, as proposed in [21]. 

Other works on drum sample retrieval involve the contrastive learning-based retrieval of single drum samples by their mixed versions [22] and retrieval by vocalization [23, 24]. Other academic works that tackle the task of matching artistic content based on aesthetic principles are the Neural Loop Combiner [25], and a stem mashup creation approach [26] (both based on contrastive learning). Other methods for computational mashup creation are based on optimization [27] or expert systems [28]. 

### 3. METHOD 

### 3.1 Scoring Function 

The goal of our proposed method is to estimate how well a given drum sample fits a specific musical context. This task can be modeled by contrastive learning as a dictionary look-up task, as described in [7]. A musical context qi ∈ R<sup>m</sup> acts as a query, and drum samples kj ∈ R<sup>m</sup> as keys. We define a scoring function s(qi, kj) that outputs a high score if the sample fits the query. To that end, we use two encoders gq and gk to produce a query encoding ui = gq(qi), ui ∈ R<sup>d</sup> and a sample encoding vj = gk(kj), vj ∈ R<sup>d</sup> . Finally, we define the scoring function as the cosine similarity sim(·, ·) between the resulting encodings s(qi, kj) = sim(ui, vj). We train the encoders using a contrastive loss called NT-Xent in [8]: 



<!-- Start of picture text -->
ex p ( sim ( ui ,  v j)/ τ )<br>X (Z) = − log (1)<br>� l̸=j exp (sim(ui, vl)/τ ) ,<br><!-- End of picture text -->

where {ui, vj} is a positive pair, Z ∈ R<sup>n×d</sup> are all representations of a training batch, τ is the temperature parameter, and we adopt the decoupled contrastive learning variant, that has shown to work better for smaller batch sizes, by removing the positive pair from the denominator (i.e., l̸ = j) [21]. 

### 3.2 Regularizations 

Furthermore, we combine the contrastive loss with the variance and covariance regularization used in VICReg [10]. The variance regularization term is defined as a hinge function that penalizes variances of latent features along the batch dimension that are smaller than 1 as 



<!-- Start of picture text -->
d<br>V(Z) = d 1 � max (0, 1 − S(z:,j, ǫ)), (2)<br>j=1<br><!-- End of picture text -->

where Python slicing notation is used, and S is the regularized standard deviation 



<!-- Start of picture text -->
S(x, ǫ) = � Var(x) + ǫ. (3)<br><!-- End of picture text -->

The covariance regularization penalizes non-zero offdiagonal entries in the covariance matrix of each batch, leading to a decorrelation of the latent dimensions: 



<!-- Start of picture text -->
C(Z) = d 1 � [C(Z)] 2 i,j , (4)<br>i̸=j<br><!-- End of picture text -->

where C is the covariance matrix 



<!-- Start of picture text -->
1 d n<br>C(Z) = d−1 � (z:,i − z¯i)(z:,i − z¯i) T , z¯i = n 1 � zj,i.<br>i=1 j=1<br>(5)<br><!-- End of picture text -->

Even though the cosine distance renders the norms of the network outputs irrelevant, they can still grow due to optimization dynamics. To keep the norms in a moderate range, we also add a norm regularization in form of a hinge function as 



<!-- Start of picture text -->
n<br>N (Z) = − n 1 � min (0, c −||zi||), (6)<br>i=1<br><!-- End of picture text -->

where we fix c = 4 in our experiments (because most norms are smaller than 4 at initialization). Putting all the above terms together (and weighting the regularization terms with factors γ, δ and η), yields the final loss 



<!-- Start of picture text -->
L(Z) = X (Z) + γV(Z) + δC(Z) + ηN (Z). (7)<br><!-- End of picture text -->

### 4. DATA 

We used a dataset of electronic music and pop/rock songs of 44.1 kHz sample rate for training and evaluation. The electronic music portion consists of 4830 so-called “remix packs”, with durations ranging from several seconds to several minutes. Each remix pack consists of multiple audio tracks that contain the individual (mutually aligned) instruments (such as synth, bass, guitar, pad, strings, choir, brass, keyboard, vocals, and different percussion instruments). 

The Pop/Rock dataset is a proprietary dataset of 885 well-known rock/pop songs of the past decades, including artists such as Lady Gaga, Coldplay, Stevie Wonder, Lenny Kravitz, Metallica, AC/DC, and Red Hot Chili Peppers. The stems (guitar, vocals, bass guitar, keyboard, misc, and different percussion instruments) are available as individual audio tracks for each song. 

From every percussion track in the dataset, we extract so-called “one-shots”, single hits with the respective percussion instrument. To that end, we picked those samples where the subsequent onset is of maximal distance (to retain most of the percussion’s potential reverb). From the pop/rock songs, we extract 5 one-shots per percussion track, while from the electronic songs, we extract 1 oneshot per percussion track (as most of the time they are all identical). Altogether, this results in 63042 one-shot drum samples. 

782 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

We categorize the extracted drum samples into 6 categories which are {kick, snare, hi-hat, ride, crash, toms}. The assignment is based on the filenames of the stems the samples originate from, using keyword dictionaries of typical drum-type expressions (like “hat” for hi-hat or “BD” for kick drum). We split the dataset in train / eval / test set with proportions 0.85/0.05/0.1 (on a track level, meaning that samples of one track do not spread over different sets). All reported results are computed on the test set. 

### 5. TRAINING 

As an encoder, we use the EfficientNet-B4 [29], where we start training from weights that have been pre-trained on the ImageNet dataset. Even though ImageNet is far from the audio spectrum domain, it turned out that using ImageNet weights is crucial in our experiments (see Section 7.1, and it has also been shown in a previous study that cross-domain pre-training can be beneficial [30]). 

The 1000 output units are reduced to 256 with a single linear layer. The EfficientNet expects a 2D input, which we provide by converting the audio signals into mel-scaled spectrograms with an STFT window length of 2048, a hop length of 512, and 128 resulting mel bins, considering the whole frequency range (fmax = 22050). Also, we logscale the values of the resulting mel spectrograms. We input the resulting spectrograms in each of the three RGB input channels of the EfficientNet (after normalization to the ImageNet color statistics). 

A positive pair consists of an audio query and a corresponding drum sample. Given a drum sample, we select the stems of the corresponding song and remove the stem from which the drum sample was extracted. Then, we randomly choose at least 2, at most all of the remaining stems (the number of stems is uniformly sampled) and mix them on the fly during training (note that the mel spectrogram transformation is part of the model architecture using the nnAudio library).<sup>5</sup> All audio inputs are of length 4 seconds. If a drum sample is shorter than that, it is zeropadded. To obtain a query, we are cutting a 4-second-long snippet from a random position of the mixture. 

The encoders are trained by the ADAM optimizer, with a batch size of 190, a learning rate of 3e-4, and a weight decay factor of 3e-5. The temperature parameter τ of the NT-Xent loss is set to 0.2. The factors for the variance and covariance regularization terms γ and δ are set to 1, and the norm regularization factor η is set to 10. 

We use some data augmentation on both the queries and the drum samples. First, Gaussian noise is added (up to −12 dB). Furthermore, we perform time-stretch with a ratio between 0.9 and 1.15 of the original tempo. Another augmentation is reducing the gain down to a minimum attenuation of −6 dB, and we perform a time shift of up to 800ms to the right and 200ms to the left (to make the models invariant to the exact onset position of one-shot audios). All these augmentations occur with a probability of 50% for each instance. 

### 6. EXPERIMENTS 

In this section, we introduce the conducted experiments to validate our method including objective metrics (Section 6.1), the user study (Section 6.2), and we describe the method of the correlation analysis (Section 6.3). 

### 6.1 Objective Evaluation 

As the actual goal of the study is to sort the candidate samples given an audio query qi, the primary evaluation metric is the ranki of the ground-truth samples for a given query (i.e., the samples that originate from the same song as the query). For that, we sort all drum samples in descending order according to the cosine similarity to a given encoded query and determine how early in the list a ground-truth sample is located. We also divide the ranki by N list entries to obtain normalized ranks ∈ (0, 1]. As we can extract several queries (4-second-long random excerpts) for each song in the test set, and as there are several drum samples assigned to each song, we perform this test for every song in the test set 50 times (resulting in |Q| = 27k evaluations) and average the resulting ranks. The explanation above results in the Mean Normalized Rank summarized as 



<!-- Start of picture text -->
|Q|<br>1 ranki<br>Rmn = |Q| �i=1 N . (8)<br><!-- End of picture text -->

In addition, we also report the Median Normalized Rank Rmd, as this is an indicator of how well the model performs most of the time, ignoring possible outliers. 

Besides also reporting the contrastive loss X (see Equation 1), we also evaluate how well the model has learned to cluster electronic and acoustic queries (i.e., mixtures) and keys (i.e., drum samples). To that end, we perform a binary (acoustic/electronic) k-nn classification (with k = 50) on the encodings separately for both the queries and the keys. From this classification task, we report the likelihood (Lq and Lk, respectively) of the data under the predictions. 

In order to better understand the influence of different design choices, we perform ablation studies and report the metrics for each model and training variants. The different ablation scenarios are described in the following. 

- 2Enc denotes our proposed setup with 2 separate encoders instead of a shared encoder for both, queries and samples. 

- PTrain denotes a variant that starts training from an EfficientNet that was pre-trained on ImageNet, instead of from randomly initialized weights. 

- In Aug, data augmentation is used. 

- VCReg, is using the variance and co-variance regularization terms (see Equations 2 and 4). 

- In SMix, we randomly mix different numbers n of random stems to form a query (where n > 1). If SMix is not used, we always mix all stems of a song. 

5 https://github.com/KinWaiCheuk/nnAudio 

783 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

- For QSInv, in addition to sampling positive pairs from queries and corresponding samples, we also include as positive pairs two queries and two samples originating from the same song. 

### 6.2 User Study 

To evaluate the quality of the scoring function, we perform a user study in which we ask 10 experts (with musical education or concerned with music production) to rate the quality of selected drum samples given a musical context. More precisely, we test their preference between drum samples that scored well according to our system and samples that are randomly picked from the dataset. The possible choices are to select one of the two proposed mixtures, or “equal” (if there is no preference for one of the choices), or “skip” (if the samples to be rated are not of the expected class or any other problem occurred). Every participant obtains 12 single comparisons (presenting each of the 6 percussion types twice) and provides 12 ratings accordingly. After that, they can decide if they want to enter a further session (to provide 12 further ratings). Participants are asked not to perform more than 4 sessions to obtain a balanced result. 

The procedure to obtain one comparison presented to a participant for rating is as follows. We pick a percussion type (e.g., snare) and a song from the test set that contains such a type as a single stem. We remove the stem containing that type, mix the remaining stems and pick ten 4-second-long excerpts from randomly sampled positions of the resulting mixture. All these excerpts are then fed through the query encoder, and the mean is taken from the resulting encodings. The resulting mean vector acts as the query encoding for the current song. Using this query, the cosine similarities to the latent representations of all 63k drum samples in the data set (obtained as described in Section 6) are computed, and the ten samples with the highest similarities are selected. Furthermore, ten drum samples of the corresponding percussion type are randomly picked from the data set. The thereby obtained samples are used to generate 20 new versions of the current song (a version for each sample). 

To create a new version of a song, we perform an onset detection on the previously removed stem (containing the percussion type in question), position the selected samples in the estimated positions, and mix the resulting stem with the remaining stems (omitting the original stem of the percussion type in question). That way, we replace the original drum track with a track containing the drum sample to be evaluated. For a single user rating, we then contrast the mixtures of a randomly picked and a highly rated percussion sample and have participants indicate their preference between the two. 

### 6.3 Correlation Analysis 

In order to gain some insights into the latent space learned by the encoders, we perform a correlation analysis between audio features of neighboring data points. For that, different perceptual and spectral features are computed for 



<!-- Start of picture text -->
0. 6<br>0. 4<br>0. 2<br>acoustic<br>0. 0 electronic<br>0. 2<br>0. 4<br>0. 6<br>0.6 0.4 0.2 0.0 0.2 0.4 0.6 0.8<br><!-- End of picture text -->

Figure 1: Principal Component Analysis (PCA) of drum sample encodings. Red dots indicate samples originating from electronic music and blue dots indicate samples originating from acoustic music. 

the drum samples in the data set using the Audio Commons timbre models<sup>6</sup> for perceptual features (e.g., boominess, brightness, depth, hardness, roughness, warmth) and librosa<sup>7</sup> for spectral features (e.g., spectral centroid or spectral contrast). We also add an indicator if the respective drum sample originates from an electronic or acoustic song. In the former case, the “electronic” feature value is set to 1, in the latter case to 0. 

The drum samples are mapped into the sample encoder’s latent space, and k-means clustering is performed using k = 24. In each cluster, the mean of each audio feature is used as a specific observation of that audio feature variable. Then, the Pearson correlation coefficient is computed between all such variables (separately for every percussion type). As a result, we can derive statements like “whenever the loudness of a kick drum is high, the boominess of the snare tends to be low”. Note that for computing the audio features, we normalize every sample to 0.5 seconds (i.e., cut or pad) so that the audio feature computation is not influenced by the length of the audio file (as some features are computed by averaging several spectrogram frames). To obtain the latent encodings used to compute the clusters, we use the regular 4-second-long samples. 

### 7. RESULTS AND DISCUSSION 

### 7.1 Objective Evaluation 

In Table 1, we report the contrastive loss, the Mean and Median Normalized Rank, and the query and sample electronic/acoustic classification likelihood for different archi- 

> 6 https://github.com/AudioCommons/ ac-audio-extractor 

> 7 https://librosa.org/ 

784 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

|||Queri|es: full m|ixtures|||Querie|s: sparse|mixtures||
|---|---|---|---|---|---|---|---|---|---|---|
|Variant|X|Rmn|Rmd|Lq|Lk|X|Rmn|Rmd|Lq|Lk|
|2Enc+PTrain+Aug+VCReg+SMix|3.614|0.105|0.032|0.9940|0.9767|3.761|0.124|0.043|0.9905|0.9763|
|2Enc+PTrain+Aug+VCReg+SMix+QSInv|3.718|0.120|0.037|0.9900|0.9782|3.818|0.136|0.047|0.9862|0.9768|
|2Enc+PTrain+Aug+VCReg|4.001|0.124|0.061|0.9825|0.9732|4.389|0.183|0.100|0.9635|0.9724|
|2Enc+PTrain+VCReg+SMix|3.742|0.128|0.037|0.9945|0.9895|3.780|0.137|0.042|0.9901|0.9898|
|2Enc+PTrain+Aug+SMix|3.575|0.116|0.032|0.9946|0.9774|3.812|0.135|0.043|0.9893|0.9790|
|2Enc+Aug+VCReg+SMix|5.235|0.458|0.432|0.7268|0.7629|5.237|0.470|0.451|0.7188|0.7480|
|2Enc+Aug+VCReg+SMix+QSInv|4.174|0.164|0.079|0.9826|0.9566|4.387|0.181|0.091|0.9768|0.9585|
|PTrain+Aug+VCReg+SMix|3.853|0.121|0.047|0.9812|0.9809|4.000|0.137|0.058|0.9768|0.9819|
|2Enc+PTrain|3.883|0.140|0.053|0.9925|0.9795|4.399|0.205|0.089|0.9821|0.9803|



Table 1: Ablation study for different architectures and training scenarios tested on queries from full mixtures and queries from sparse mixtures (a sparse mixture is based on a random number n of stems, where n > 1). X denotes the contrastive loss and Rmn and Rmd is the mean and median normalized rank, respectively, of ground truth samples. Lq is the likelihood of the binary k-nn (electronic/acoustic) classification task for query, and Lk for key encodings in the latent space. 

tectures and training scenarios (as described in Section 6.1). For each run, we train for 600 epochs and pick the saved checkpoint of the epoch with the best performance (regarding the Mean Normalized Rank Rmn) on the evaluation set for evaluating the test set. We report the results when evaluating the models with queries that are drawn from mixtures where all stems of a song are used (denoted as “full mixtures”) and mixtures with a random number n of stems (denoted as “sparse mixtures”, where n > 1). The latter scenario is crucial in music production, where sample selection may occur at an intermediate state of the project, when several instruments are still missing. 

The results show that our proposed architecture and training procedure (first row in Table 1) performs best in the mean and median rank metrics (Rmn and Rmn) for both query scenarios (note that the random guessing baseline is 0.5). It is somewhat surprising to us that QSInv (i.e., imposing additional invariance for queries/samples originating from the same song) does not improve but rather worsens the result (cf. row 2 of the table). Apparently, the relaxation of the space caused by not using this regularization helps to perform the main objective. 

We can see for SMix that it is vital to mix different (numbers of) stems on the fly during training (cf. third row in Table 1 where this has not been done). SMix does not only help for the “sparse mixtures” scenario at test time (right part of the table) but also in the “full mixtures” scenario (left part of the table). 

Using a pre-trained EfficientNet (PTrain) makes a considerable difference in the overall performance and training dynamics. In fact, when not using pre-trained weights, it is necessary to add QSInv in our experiments. Otherwise, the encoders do not learn at all (see row 6 in Table 1). 

The last row of Table 1 presents the results of a scenario where all training optimizations (augmentation, variance, co-variance regularization, and sparse mixing) are turned off. It can be seen that the performance deteriorates substantially, particularly in the “sparse mixtures” test scenario. 

Finally, the results of the classification likelihood (mostly around 99%) show that the models have implicitly learned to separate electronic and acoustic content (cf. Figure 1, showing a PCA of the drum sample encodings). Interest- 



<!-- Start of picture text -->
7 0 type<br>Mean<br>6 0 Kick<br>Snare<br>HiHat<br>5 0 Ride<br>Crash<br>4 0 Toms<br>3 0<br>2 0<br>1 0<br>0<br>best random equal<br>rating<br>percent<br><!-- End of picture text -->

Figure 2: Preference ratings of participants in the user study, separated by percussion type (the blue bar “Mean” shows the mean of all ratings). “best” are mixtures with samples that scored highest by our method, and “random” denotes mixtures with random samples from the data set. An “equal” rating means no particular preference. 

ingly, this separation works consistently better if no data augmentation is used (see row 4 in Table 1). Electronic samples are generally “cleaner” than those extracted from acoustic music. Augmentation (e.g., adding noise) may remove some of these characteristics, making it harder to discriminate between the two classes. 

### 7.2 User Study 

Figure 2 shows the results of the listening test (based on 300 ratings in total, omitting skipped ratings). On average (“Mean”), the samples that are ranked “best” by our method were preferred approximately twice as often as random samples (61.57% to 32.64%). It is also interesting that for most percussion types, the human preference for “best” is similar to or better than average (with Snare and Ride being the most salient), while human ratings disagree with our system’s choices, particularly often for HiHat and Toms. A hypothesis why HiHats perform worse is that we merged both open and closed hi-hat in one group. When replacing the original hi-hats with the selected ones, there 

785 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
Snare vs. Crash<br>boomines s 0 .6-0.60.7-0.4-0.1-0.6-0.6 0.3 0.3 -0.7-0.6-0.2 0.5-0.7-0.6 0 .8<br>brightnes s -0 .50.6-0.60.7 -0.1 0.5 0.7-0.4-0.50.6 0.5 0.1 -0.30.6 0.6<br>dept h 0 .6-0.60.7-0.5-0.1-0.6-0.7 0.4 0.4 -0.7-0.6-0.2 0.5-0.7-0.7 0 .6<br>hardnes s -0 .40.5-0.50.6 -0.10.4 0.5-0.4-0.40.6 0.5 0.1-0.2 0.6 0.4<br>loudnes s -0 .4 0.4 -0.4 0.2 0.4 0.5 0.5-0.10.1 0.6 0.5 0.2 -0.50.6 0.6 0 .4<br>roughnes s -0 .4 0.4 -0.30.6 0.1 0.4 0.4-0.3-0.10.4 0.4 0.0-0.10.4 0.3<br>sharpnes s -0 .50.6-0.50.7 -0.10.5 0.6-0.4-0.40.6 0.5 0.0-0.2 0.5 0.5 0 .2<br>warmt h 0 .6-0.60.7-0.6 0.0 -0.6-0.7 0.4 0.4 -0.7-0.6-0.20.4 -0.7-0.7<br>log_attack_tim e -0 .3 0.3-0.20.2 0.5 0.4 0.3-0.00.4 0.2 0.2-0.1-0.20.2 0.3 0 .0<br>spectral_centroi d 0 .5-0.50.6 -0.2-0.2-0.5-0.5 0.2 0.3 -0.6-0.5-0.2 0.6-0.6-0.6<br>0.2<br>spectral_bandwidt h 0 .6-0.60.6-0.3-0.1-0.5-0.6 0.3 0.4 -0.7-0.6-0.1 0.5-0.6-0.7<br>spectral_contras t 0 .5 -0.60.5-0.6 0.1 -0.5-0.6 0.4 0.4 -0.6-0.5 0.1 0.3 -0.6-0.7 0.4<br>spectral_flatnes s -0 .60.6-0.70.5 -0.0 0.6 0.7-0.4-0.50.7 0.6 0.1 -0.50.7 0.7<br>spectral_rollof f 0 .5-0.50.6 -0.2-0.1-0.5-0.6 0.3 0.3 -0.6-0.5-0.2 0.6-0.6-0.7 0.6<br>electroni c -0 .60.7-0.70.5 0.1 0.6 0.7-0.4-0.30.7 0.6 0.0 -0.50.7 0.9<br>Crash<br>boominessbrightnessdepthhardnessloudnessroughnesssharpnesslog_attack_timewarmthspectral_centroidspectral_bandwidthspectral_contrastspectral_flatnessspectral_rolloffelectronic<br>Snare<br><!-- End of picture text -->

Figure 3: Correlations between perceptual and spectral features (and electronic / acoustic indicator) of Snare and Crash drum samples that are close in the latent space (i.e., scored to fit well in the same musical context). 

while the spectral features tend to be negatively correlated (from “log attack time” to “spectral rolloff”). Possibly, as snare and crash have similar perceptual characteristics, they should not get into each other’s way regarding their frequency ranges. Whenever the snare occupies the higher frequencies, the crash occupies the lower frequencies and vice versa (according to the “spectral centroid” entry of −0.6 in the diagonal). 

Finally, the correlations with the “electronic” indicator are also informative. It shows that a snare (and partly a crash) in electronic music tends to be more intense than in acoustic music, with more brightness, loudness, and sharpness. At the same time (looking at the spectral centroid), in electronic music, a snare tends to occupy rather lower frequencies than in acoustic music, while the opposite is true for crash (where the spectral centroid is positively correlated with electronic snares - having a correlation coefficient of 0.7). The high correlation of “electronic” (0.9) in the diagonal shows that electronic snares and crashes tend to be in the same clusters of the latent space. 

### 8. CONCLUSION AND FUTURE WORK 

is an equal chance that an open hi-hat is used for a rhythm that is meant to be instantiated with a closed hi-hat and vice versa. This is particularly problematic in electronic music, where closed hi-hats are often used with minimal temporal intervals. The reason why Toms do not work well is probably due to less available training data (many tracks do not have tom stems). Examples of how the user study was presented can be found on the accompaniment website.<sup>8</sup> 

### 7.3 Correlation Analysis 

Figure 3 shows the correlation coefficients between audio features of snare and crash drum samples over clusters in the latent space (as described in Section 6.3, note that the entirety of the percussion-type combinations is shown on the accompaniment website).<sup>8</sup> 

To our knowledge, there is no theory about the aesthetic rules of drum sample selection. Therefore, this analysis is particularly informative. It is interesting to see that strong correlations exist at all between the audio features of snare and crash found in the same clusters of the latent space (as is true for most other percussion-type combinations). Consequently, the characteristics that make drum samples fit in the same musical contexts can (also) be explained by such lower-level features. Using such correlation coefficients makes it possible to understand how the learned space is organized. More importantly, it is also possible to derive rules and make the method explainable. For example, it is possible to extract statements like “if the snare of a song sounds warm, the crash should not sound bright” (because “warmth” of the snare and “brightness” of the crash are negatively correlated with a coefficient of −0.6). 

When looking at the diagonal of the correlation matrix in Figure 3, we see that the perceptual features tend to be positively correlated (from “boominess” to “warmth”), 

We introduced a method that automatically scores the fit of drum samples to a given musical context. As the method is thought to be used in a music production context, the audio queries used for training are based on “sparse mixtures”, which allows scoring samples at different stages of the music production process. Results show that this form of data augmentation generally improves performance, also when queries are computed from complete mixtures at test time. Critically, the automatic system should agree with human judgment. Therefore, we performed a user study that tests this agreement. It could be shown that the drum samples that are highly rated by our system are also preferred by human experts approximately twice as often as randomly selected samples. 

As the architecture and training procedure combine different ideas, we performed an ablation study, where it became clear that starting with a pre-trained model is crucial for a good final performance and that additional choices (like using variance and co-variance regularization, data augmentation, and on-the-fly sparse mixing) improve the results considerably. It was also shown that audio features of drum samples whose encodings are close in the latent space are highly correlated, and we demonstrated that the observed correlations can also be interpreted to derive rules. 

Our proposed method is not limited to drum samples but can potentially be used to retrieve different kinds of musical material based on learned aesthetic principles. Also, in the future, we want to scale up the system by using bigger data sets and a more generic pre-processing strategy. Currently, single drum samples are extracted before training to obtain a controlled experiment setup and application scenario. Developing a system that uses stems directly would apply better to audio sources of any type and would therefore greatly increase the applicability of our method in music production. 

8 https://sites.google.com/view/samplematch 

786 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

### 9. ACKNOWLEDGEMENTS 

I want to thank the reviewers for their extraordinarily thorough suggestions to improve this work and my colleagues at Sony CSL that assisted me with technical expertise and emotional support. 

### 10. REFERENCES 

- [1] E. Deruty, M. Grachten, S. Lattner, J. Nistal, and C. Aouameur, “On the development and practice of AI technology for contemporary popular music production,” Trans. Int. Soc. Music. Inf. Retr., vol. 5, no. 1, p. 35, 2022. [Online]. Available: https://doi.org/10.5334/tismir.100 

- [2] J. Nistal, C. Aouameur, I. Velarde, and S. Lattner, “Drumgan VST: A plugin for drum sound analysis/synthesis with autoencoding generative adversarial networks,” in Proceedings of the 39th International Conference on Machine Learning, Baltimore, Maryland, USA, 2022. [Online]. Available: https://arxiv.org/pdf/2206.14723.pdf 

- [3] J. H. Engel, L. Hantrakul, C. Gu, and A. Roberts, “DDSP: Differentiable digital signal processing,” in 8th International Conference on Learning Representations, ICLR, Addis Ababa, Ethiopia, April 26-30, 2020. [Online]. Available: https://openreview.net/forum?id=B1x1ma4tDr 

- [4] T. Bazin, G. Hadjeres, P. Esling, and M. Malt, “Spectrogram inpainting for interactive generation of instrument sounds,” in Joint Conference on AI Music Creativity, 2020. [Online]. Available: https://arxiv.org/abs/2104.07519 

- [5] S. Lattner and M. Grachten, “High-level control of drum track generation using learned patterns of rhythmic interaction,” in IEEE Workshop on Applications of Signal Processing to Audio and Acoustics, WASPAA, New Paltz, NY, USA, October 20-23, 2019, pp. 35–39. [Online]. Available: https: //doi.org/10.1109/WASPAA.2019.8937261 

- [6] G. Hadjeres and L. Crestel, “The piano inpainting application,” CoRR, vol. abs/2107.05944, 2021. [Online]. Available: https://arxiv.org/abs/2107.05944 

- [7] K. He, H. Fan, Y. Wu, S. Xie, and R. B. Girshick, “Momentum contrast for unsupervised visual representation learning,” in IEEE/CVF Conference on Computer Vision and Pattern Recognition, CVPR, Seattle, WA, USA, June 13-19, 2020, pp. 9726– 9735. [Online]. Available: https://doi.org/10.1109/ CVPR42600.2020.00975 

- [8] T. Chen, S. Kornblith, M. Norouzi, and G. E. Hinton, “A simple framework for contrastive learning of visual representations,” in Proceedings of the 37th International Conference on Machine Learning, ICML, 13-18 July, 2020, pp. 1597–1607. [Online]. 

Available: http://proceedings.mlr.press/v119/chen20j. html 

- [9] J. Grill, F. Strub, F. Altch´e, C. Tallec, P. H. Richemond, E. Buchatskaya, C. Doersch, B. A.<sup>´</sup> Pires, Z. Guo, M. G. Azar, B. Piot, K. Kavukcuoglu, R. Munos, and M. Valko, “Bootstrap your own latent - A new approach to self-supervised learning,” in Annual Conference on Neural Information Processing Systems, NeurIPS, December 6-12, 2020. [Online]. Available: https://proceedings.neurips.cc/paper/2020/hash/ f3ada80d5c4ee70142b17b8192b2958e-Abstract.html 

- [10] A. Bardes, J. Ponce, and Y. LeCun, “VICReg: Variance-invariance-covariance regularization for selfsupervised learning,” CoRR, vol. abs/2105.04906, 2021. [Online]. Available: https://arxiv.org/abs/2105. 04906 

- [11] S. Schneider, A. Baevski, R. Collobert, and M. Auli, “wav2vec: Unsupervised pre-training for speech recognition,” in Interspeech, 20th Annual Conference of the International Speech Communication Association, Graz, Austria, 15-19 September, 2019, pp. 3465–3469. [Online]. Available: https://doi.org/10.21437/Interspeech.2019-1873 

- [12] A. Baevski, Y. Zhou, A. Mohamed, and M. Auli, “wav2vec 2.0: A framework for self-supervised learning of speech representations,” in Annual Conference on Neural Information Processing Systems, NeurIPS, December 6-12, 2020. [Online]. Available: https://proceedings.neurips.cc/paper/2020/hash/ 92d1e1eb1cd6f9fba3227870bb6d7f07-Abstract.html 

- [13] D. Jiang, W. Li, M. Cao, W. Zou, and X. Li, “Speech SimCLR: Combining contrastive and reconstruction objective for self-supervised speech representation learning,” in Interspeech, 22nd Annual Conference of the International Speech Communication Association, Brno, Czechia, 30 August - 3 September, 2021, pp. 1544–1548. [Online]. Available: https://doi.org/10. 21437/Interspeech.2021-391 

- [14] A. Saeed, D. Grangier, and N. Zeghidour, “Contrastive learning of general-purpose audio representations,” in IEEE International Conference on Acoustics, Speech and Signal Processing, ICASSP, Toronto, ON, Canada, June 6-11, 2021, pp. 3875–3879. [Online]. Available: https://doi.org/10.1109/ICASSP39728.2021.9413528 

- [15] J. Spijkervet and J. A. Burgoyne, “Contrastive learning of musical representations,” in Proceedings of the 22nd International Society for Music Information Retrieval Conference, ISMIR, Online, November 7- 12, 2021, pp. 673–681. [Online]. Available: https: //archives.ismir.net/ismir2021/paper/000084.pdf 

- [16] M. Tagliasacchi, B. Gfeller, F. de Chaumont Quitry, and D. Roblek, “Pre-training audio representations with self-supervision,” IEEE Signal Process. Lett., 

787 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

vol. 27, pp. 600–604, 2020. [Online]. Available: https://doi.org/10.1109/LSP.2020.2985586 

- [17] S. Srivastava, Y. Wang, A. Tjandra, A. Kumar, C. Liu, K. Singh, and Y. Saraf, “Conformer-based self-supervised learning for non-speech audio tasks,” CoRR, vol. abs/2110.07313, 2021. [Online]. Available: https://arxiv.org/abs/2110.07313 

- [18] D. Niizumi, D. Takeuchi, Y. Ohishi, N. Harada, and K. Kashino, “BYOL for audio: Self-supervised learning for general-purpose audio representation,” in International Joint Conference on Neural Networks, IJCNN, Shenzhen, China, July 18-22, 2021, pp. 1–8. [Online]. Available: https://doi.org/10.1109/ IJCNN52387.2021.9534474 

- [19] L. Wang, P. Luc, A. Recasens, J. Alayrac, and A. van den Oord, “Multimodal self-supervised learning of general audio representations,” CoRR, vol. abs/2104.12807, 2021. [Online]. Available: https://arxiv.org/abs/2104.12807 

- [20] L. Wang and A. van den Oord, “Multi-format contrastive learning of audio representations,” CoRR, vol. abs/2103.06508, 2021. [Online]. Available: https: //arxiv.org/abs/2103.06508 

- [21] C. Yeh, C. Hong, Y. Hsu, T. Liu, Y. Chen, and Y. LeCun, “Decoupled contrastive learning,” CoRR, vol. abs/2110.06848, 2021. [Online]. Available: https://arxiv.org/abs/2110.06848 

- [22] W. Kim and J. Nam, “Drum sample retrieval from mixed audio via a joint embedding space of mixed and single audio samples,” in Audio Engineering Society Convention 149. Audio Engineering Society, 2020. 

      - tracks to generate music mashups,” in Thirty-Fifth AAAI Conference on Artificial Intelligence, February 2-9, 2021, pp. 187–195. [Online]. Available: https: //ojs.aaai.org/index.php/AAAI/article/view/16092 

   - [27] G. Bernardo and G. Bernardes, “Leveraging compatibility and diversity in computational music mashup creation,” in AM ’21: Audio Mostly, Virtual Event / Trento, Italy, September 1-3, 2021, pp. 248–255. [Online]. Available: https://doi.org/10.1145/3478384.3478424 

   - [28] M. E. P. Davies, P. Hamel, K. Yoshii, and M. Goto, “AutoMashUpper: Automatic creation of multi-song music mashups,” IEEE ACM Trans. Audio Speech Lang. Process., vol. 22, no. 12, pp. 1726–1737, 2014. [Online]. Available: https://doi.org/10.1109/TASLP. 2014.2347135 

   - [29] M. Tan and Q. V. Le, “EfficientNet: Rethinking model scaling for convolutional neural networks,” in Proceedings of the 36th International Conference on Machine Learning, ICML, Long Beach, California, USA, 9- 15 June, 2019, pp. 6105–6114. [Online]. Available: http://proceedings.mlr.press/v97/tan19a.html 

   - [30] A. Guzhov, F. Raue, J. Hees, and A. Dengel, “ESResNet: Environmental sound classification based on visual domain models,” in 25th International Conference on Pattern Recognition, ICPR, Virtual Event / Milan, Italy, January 10-15, 2020, pp. 4933–4940. [Online]. Available: https://doi.org/10. 1109/ICPR48806.2021.9413035 

- [23] A. Delgado, C. Saitis, E. Benetos, and M. B. Sandler, “Deep conditional representation learning for drum sample retrieval by vocalisation,” CoRR, vol. abs/2204.04651, 2022. [Online]. Available: https: //doi.org/10.48550/arXiv.2204.04651 

- [24] A. Mehrabi, K. Choi, S. Dixon, and M. B. Sandler, “Similarity measures for vocal-based drum sample retrieval using deep convolutional auto-encoders,” in IEEE International Conference on Acoustics, Speech and Signal Processing, ICASSP, Calgary, AB, Canada, April 15-20, 2018, pp. 356–360. [Online]. Available: https://doi.org/10.1109/ICASSP.2018.8461566 

- [25] B. Chen, J. B. L. Smith, and Y. Yang, “Neural loop combiner: Neural network models for assessing the compatibility of loops,” in Proceedings of the 21th International Society for Music Information Retrieval Conference, ISMIR, Montreal, Canada, October 11-16, 2020, pp. 424–431. [Online]. Available: http://archives.ismir.net/ismir2020/paper/000225.pdf 

- [26] J. Huang, J. Wang, J. B. L. Smith, X. Song, and Y. Wang, “Modeling the compatibility of stem 

788 

