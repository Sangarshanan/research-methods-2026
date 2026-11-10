---
paper_id: "000083"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706569/files/000083.pdf"
---

# ASSESSING THE ALIGNMENT OF AUDIO REPRESENTATIONS WITH TIMBRE SIMILARITY RATINGS 

Haokun Tian<sup>1</sup> 

Stefan Lattner<sup>2</sup> Charalampos Saitis<sup>1</sup> 

1 Queen Mary University of London, UK 

2 Sony Computer Science Laboratories, Paris, France 

```
haokun.tian@qmul.ac.uk
```

## ABSTRACT 

Psychoacoustical so-called “timbre spaces” map perceptual similarity ratings of instrument sounds onto lowdimensional embeddings via multidimensional scaling, but suffer from scalability issues and are incapable of generalization. Recent results from audio (music and speech) quality assessment as well as image similarity have shown that deep learning is able to produce embeddings that align well with human perception while being largely free from these constraints. Although the existing human-rated timbre similarity data is not large enough to train deep neural networks (2,614 pairwise ratings on 334 audio samples), it can serve as test-only data for audio models. In this paper, we introduce metrics to assess the alignment of diverse audio representations with human judgments of timbre similarity by comparing both the absolute values and the rankings of embedding distances to human similarity ratings. Our evaluation involves three signalprocessing-based representations, twelve representations extracted from pre-trained models, and three representations extracted from a novel sound matching model. Among them, the style embeddings inspired by image style transfer, extracted from the CLAP model and the sound matching model, remarkably outperform the others, showing their potential in modeling timbre similarity. 



<!-- Start of picture text -->
→ Barthet2010<br>→ Patil2012_A3<br>Zacharakis2014_greek←<br>identical most dissimilar<br><!-- End of picture text -->

Figure 1. Human similarity ratings of three timbre space datasets [1–3]. Each block matrix represents pairwise comparisons between audio stimuli. Entry (i, j) indicates the perceived similarity between audio i and audio j. Darker colors indicate lower similarity. The lower triangular part is made partially transparent due to symmetry. 

## 1. INTRODUCTION 

How do humans distinguish between different musical timbres? This question has driven research in the field of psychoacoustics for decades [4]. Researchers typically recruit a group of people, play different sounds to them in a controlled acoustic environment, and ask them to rate the differences in the sounds by assigning a score. These sounds are normalized in pitch, loudness, and duration so that participants can focus on timbre. After collecting all human ratings, researchers use a technique called multidimensional scaling (MDS) to map the sounds onto a low-dimensional space called timbre space, where distances between the resulting embeddings reflect human ratings. This space is 

> © H. Tian, S. Lattner, and C. Saitis. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: H. Tian, S. Lattner, and C. Saitis, “Assessing the Alignment of Audio Representations with Timbre Similarity Ratings”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

then analyzed to find whether certain acoustic features can explain how timbres are ordered along different dimensions. 

However, these studies have always been limited in scale—that is, they only involved a small number of sound stimuli. If the number of sounds were to increase, the required human ratings would grow quadratically, since ratings are given in pairs. The largest study to date is [5], which includes 42 sound stimuli. Additionally, pitch, loudness, and duration must be fixed to eliminate confounding effects, meaning that a timbre space with variable pitch or loudness can never be constructed. Furthermore, to place new audio samples into a timbre space, new human ratings must always be collected, indicating that the timbre space as a model does not have the ability to generalize without additional efforts. 

To overcome these limitations, we envision a neural network-based model that can serve as a perceptual metric for timbre—that is, it can embed any audio input into a space where distances between embeddings reflect how different humans perceive them. Such a metric would have numerous applications. First, to train a model to generate 

710 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

instrument sounds [6, 7], one could match the timbre by directly computing the loss using this metric rather than relying on spectrogram distances. In music production, it could enable efficient retrieval of samples with similar or contrasting timbres without the need for laborious listening. Additionally, it can encode audio signals into meaningful timbre tokens for generative modeling. Finally, it could provide a control space for musical expression, as has already been demonstrated [8]. 

In this work, we take the first step by evaluating a range of models’ representations, including signal-processingbased low-level representations and those produced by pretrained audio models, on the past 21 small datasets collected by psychoacoustical timbre space studies. Our goal is to determine which model currently performs best in terms of matching human ratings of timbre similarity. We also include a newly trained sound matching model that predicts synthesis parameters from audio, and we evaluate audio representations extracted from it. In particular, we have found that style embeddings, originally proposed for image style transfer, are promising as a future direction for modeling timbre similarity. We clarify that the term “alignment” in this paper does not refer to any temporal synchronizations, and our assessment does not indicate the extent to which models produce disentangled timbre representations—an ability required for some of the applications mentioned in the previous paragraph. 

## 2. RELATED WORK 

Several works have aimed to train models that produce a perceptual timbre space. Esling et al. [9] trained a variational autoencoder to reconstruct audio samples of different timbres, using perceptual ratings from timbre space studies to regularize the space. Lostanlen et al. [10] collected timbre similarity judgments on 78 sounds using free sorting [11]. By aggregating responses from different participants, the sounds were assigned to 19 clusters according to their perceptual similarity. They, along with a subsequent study [12], developed metric learning models to capture this structure. Thoret et al. [13] and Pascal et al. [14] attempted to learn distance metrics directly from timbre space data but did not learn a single metric that generalizes across all datasets. The most similar work to ours is by Vahidi et al. [15], which evaluated the alignment of three representations with timbre similarity ratings. Additionally, the accompanied codebase [16] provides more implementations of alignment scores, but no results have been reported. Our work is a direct continuation, providing a holistic evaluation of various models and implementations with extended functionalities. 

In broader domains, perceptual metrics have been developed to handle various levels of perturbations. They are either trained from scratch or fine-tuned using human perceptual judgments. For audio, Manocha et al. proposed DPAM [17] and CDPAM [18], which address low-level audio perturbations such as noise addition, reverb, and compression. In the image domain, Zhang et al. [19] modeled low-level perturbations including traditional distortions such as noise addition and blur, as well as CNN-based dis- 

tortions. Fu et al. [20] explored mid-level perturbations related to pose, color, and shape. Muttenthaler et al. [21] investigated high-level perturbations involving different object-level concepts (e.g., “grass” versus “sand”). The smallest dataset used is NIGHTS [20] with 20K human judgments, while the largest is THINGS [22], which contains 4.7M human judgments. In particular, [19] demonstrated that deep learning representations, regardless of the training data, model, or task used, exhibit a promising ability to capture perceptual image similarity. Therefore, although current timbre space datasets provide only 2.6K pairwise judgments and are insufficient for training, they are worth being used for model evaluation. 

## 3. DATA AND EXPERIMENTS 

## 3.1 Data 

We use data curated by Thoret et al. [13] and Vahidi et. al [15],<sup>1</sup> comprising a total of 21 datasets from 11 published psychoacoustic studies [1–3,23–25,27,28,31,33,34]. We present summary information for each dataset in Table 1. Each dataset contains a set of audio samples along with pairwise timbre similarity ratings. The sounds span a wide range: acoustic recordings of musical instrument notes, digitally edited acoustic samples designed to create simpler or cross-instrument spectra, and tones from synthesizers and electromechanical instruments. Each similarity rating is an absolute value calculated by averaging across multiple human listeners. We compile all ratings from the 21 datasets into a large, sparse block-diagonal matrix, where the upper triangular part of each block represents the ratings for unique audio pairs in the corresponding dataset. Figure 1 illustrates three of these blocks, with symmetric pairwise ratings visualized by color. In total, the matrix includes 334 audio samples and 2,614 similarity ratings. 

## 3.2 Metrics 

Our goal is to investigate whether an audio model can perceive timbre similarity in a way that aligns with human perception. To this end, we compute pairwise distances between audio representations produced by the model to estimate similarity ratings, which we then compare with real human ratings to obtain alignment scores. Conceptually, the pairwise distances of audio representations form a predicted similarity matrix, which we compare against the ground truth similarity matrix, consisting of human ratings. 

To conduct this evaluation, we first obtain equally shaped representations for audio of different lengths, in preparation for the distance computation. Second, we employ a distance function to quantify their similarity. Third, we require metrics to measure the alignment between the predicted and true similarity matrices. Below, we present our approach to these three steps, resulting in two methods for handling variable length (see next section for cases with only one viable option), two methods for computing distances, and five ways of computing alignment scores. This gives a 

> 1 https://github.com/ben-hayes/timbre-dissimilarity-metrics 

711 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

|Study|Dataset|N of<br>sounds|Pitch|Length<br>(s)|Loudness<br>(dB LUFS)|Type of sounds|N of<br>raters<sup>∗</sup>|
|---|---|---|---|---|---|---|---|
|Grey (1977) [23]|–|16|E♭4|0.27±0.03|-14.61±1.57|Synthesized from acoustic|22|
|Grey & Gordon (1978) [24]|–|16|E♭4|0.27±0.03|-14.87±1.76|Same as above, spectral envelopes traded|22|
|Iverson & Krumhansl (1993) [25]|Whole|16|C4|3.19±0.69|-16.62±3.99|Acoustic [26]|10|
||Onset<br>|16<br>|C4|0.11±0.01|-23.24±9.10<br>|Same as above, only∼80ms attack<br>|9|
||Remainder|16|C4|3.10±0.70|-16.71±4.13|Same as above,∼80ms attack removed|9|
|McAdams et al. (1995) [27]|–|18|E♭4|0.69±0.19|-18.36±4.05|FM simulated and hybrids|22|
|Lakatos (2000) [28]|Combined|20|E♭4<br>|1.50<br>|-24.08±2.98<br>|Acoustic [26]|34|
||Harmonic|17|E♭4|1.50|-25.03±2.36|Same as above, only harmonic sounds|34|
||Percussive|18|E♭4|1.49±0.05|-23.97±3.83|Same as above, only percussive sounds|34|
|Barthet et al. (2010) [1]|–|15|E♭4|1.56±0.04|-23.77±1.13|Physical modeling, clarinet only|16|
|Patil et al. (2012) [2]|A3|11|A3|0.25|-19.03±0.85|Acoustic [29]|6|
||D4<br>|11|D4<br>|0.25|-19.17±0.81|Same as above|20|
||G♯4|11|G♯4|0.25|-18.97±0.81|Same as above|6|
|Zacharakis et al. (2015) [3]|Greek raters|24|A1–4|1.30|-29.36±3.84|Acoustic [30] and synthesizers|33|
||English raters|24|A1–4|1.30|-29.36±3.84|Same as above|20|
|Siedenburg et al. (2016) [31]|Exp 2A Set 1|14|E♭4|0.50|-23.56±3.15|Acoustic [32]|24|
||Exp 2A Set 2|14|E♭4|0.50|-23.77±1.90|Chimeric (spectral envelopes traded)|24|
||Exp 2A Set 3|14|E♭4|0.50|-23.21±2.37|Acoustic and chimeric|24|
||Exp 2B|14|E♭4|0.50|-23.21±2.37|Same as above|24|
|Saitis & Siedenburg (2020) [33]|GEdissim|14|E♭4|0.50|-23.56±3.15|Same as Exp 2A Set 1 in [31,32]|40|
|Vahidi et al. (2020) [34]|–|15|A4|1.00|-9.73±3.09|Subtractive synthesis|35|
|∗Raters are typically musicians or with some|sort of musical backgr|ound. Some|studies use|d a mixture of musi|cians and non-musicia|ns.||



Table 1. Summary of the 21 timbre similarity datasets. We computed integrated loudness for each sample using `pyloudnorm` [35] with a block size of 0.08 seconds—slightly shorter than the shortest sample. While some dynamic variations can be observed, loudness is typically reported to have been normalized by expert listeners. 

total of 10 or 20 scores for each representation (one model can produce multiple representations). Additionally, we have developed this process into an easy-to-use Python package, as described in Section 3.2.4. 

we will also not compute the time-averaged version. We describe in Section 3.4 specifically how the dynamic-length approach is applied for each model. 

## 3.2.2 Distance Functions 

## 3.2.1 Handling Variable Audio Length 

To produce representations for audio, models typically use an analysis window with a fixed length, which slides over time with a hop length to produce time-varying representations. As shown in Table 1, some timbre space datasets have fixed audio lengths, while others do not. This creates the need to compute identically shaped representations for audio of different lengths, as models employing sliding windows inherently produce representations with a time dimension proportional to the input length. To address this, we provide two approaches. The first is to squash the time dimension by computing the average over it. The second, which we call dynamic-length, matches input lengths by padding zeros to the right—or truncating in very few cases—to arrive at the same length. Below are a few scenarios. If the model has a long enough analysis window that covers all input lengths of the timbre space data, all audio samples are padded to this length. For this case, we will not compute the time-averaged version, as the representation has only one frame along the time dimension. And if the model operates with a rather short analysis window, the solution is to always dynamically pad the shorter audio within a pair to match the length of the longer one, ensuring the shapes of their representations match. We only truncate audio samples in one case, and that is when the model is sensitive to time shifting and does not accept sliding. We pad the shorter audio and truncate the longer audio to match the fixed window length. In this case 

We compute pairwise distances using two functions: the ℓ2 distance and cosine distance (defined as one minus the cosine similarity). These functions are applied to flattened audio representations. 

## 3.2.3 Alignment Scores 

The alignment scores are computed between the predicted similarity matrix and the ground truth similarity matrix, both of which are diagonal block matrices. We note that only the pairs within the diagonal blocks are valid, have similarity ratings, and are used to compute the alignment scores. Pairs outside the diagonal blocks lack human ratings as samples are from different datasets. Before computation, the values in each dataset-level block matrix (from both the predicted and ground truth matrices) are rescaled to the range [0, 1]. 

We compute five alignment scores in total. The first is the mean absolute error (MAE). It computes the absolute error between ratings of each unique audio pair and averages the errors across all pairs. The other four are rank-based scores that evaluate how well the model ranks a list of audio samples based on their timbre similarity to a given sample. This is done by comparing each row of the two similarity matrices (column-wise comparison yields the same results due to symmetry), which contains the similarity ratings between a reference sample (whose index corresponds to the row index) and all other samples from the same dataset, where the relative ordering of these ratings determines the 

712 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

timbre similarity ranking with respect to the reference sample. Sorting the ratings per row yields N rankings—one for each sample (each sample is used once as the reference sample)—where N is the total number of samples. The predicted ranking from the computed matrix is then compared to the true ranking from the ground-truth matrix. The final rank-based alignment scores are obtained by computing a score per row and averaging across all rows. 

We use four rank-based metrics for per-row comparisons: Kendall’s rank correlation coefficient, Normalized Discounted Cumulative Gain (NDCG) that treats timbre similarity (rather than dissimilarity) as relevance, Spearman’s rank correlation coefficient, and triplet agreement with an adjustable margin. For the first three standard metrics, we use implementations from `torchmetrics` [36]. For triplet agreement, we first extract all triplets from the groundtruth row that satisfies the given margin condition—that is, the absolute difference between two dissimilarity ratings must be greater than the margin value. This mimics a just-noticeable difference in human perception, where rating differences smaller than this threshold are considered perceptually equivalent to the reference and are therefore excluded from the evaluation. The margin is set to 0.1 in our evaluation. To illustrate, a triplet consists of three audio samples (i, j, k), where i is the reference sample and the similarity between i and j is compared to the similarity between i and k. We then compute the triplet agreement rate as the ratio of triplets for which both matrix rows agree on the relative ordering of j and k with respect to i, to the total number of extracted triplets. 

## 3.2.4 The Python Package 

Our Python package<sup>2</sup> `timbremetrics` simplifies the evaluation process by requiring only the input of a model capable of converting raw waveforms into audio representations to compute the alignment of that model with timbre similarity perception. This package supports all evaluations described in this section and additionally supports three distance functions: ℓ1, negative dot product, and Poincaré distance, a commonly used hyperbolic distance [37]. It is compatible with audio models interfaced by the Fréchet Audio Distance Toolkit [38].<sup>3</sup> Furthermore, it can be used as a convenient training-time evaluation to inspect whether the model can acquire human-like ability to perceive timbre similarity during the learning process. 

## 3.3 Sound Matching 

We train a sound matching model that inverts the Vital synthesizer<sup>4</sup> by predicting the synthesis parameters from synthesized audio.<sup>5</sup> We are interested in whether, via this task, the model can learn meaningful representations that align with timbre similarity perception. We are motivated by the fact that synthesizer parameters encode all audio content using very little storage, and we expect that by learning 

> 2 https://github.com/tiianhk/timbremetrics 

> 3 https://github.com/microsoft/fadtk 

> 4 https://vital.audio 

> 5 Code available at https://github.com/tiianhk/sm4tp 

this compression, we can obtain compact but expressive intermediate representations. 

## 3.3.1 Data Generation 

We use `Vita` ,<sup>6</sup> , a package that provides Python bindings for the Vital Synthesizer, to generate our dataset. Ten parameters and their ranges are subjectively selected to produce pronounced timbral changes when varied. These parameters include one discrete selection from seven basic waveshapes (e.g., sine wave, triangle wave) in the wavetable, two to distort the waveshape, two from a unison effect, three from the ADSR envelope, and two from an EQ. Of these, two are discrete parameters, and the remaining eight are continuous parameters. We uniformly sample each parameter to generate data. A random pitch is also sampled, but not as a prediction target, as pitch is considered unrelated to timbre. We generate a total of 500k samples, each with a maximum length of two seconds, which takes ∼8 hours on a single CPU core. All continuous parameters are rescaled to the range [0, 1] to be used as regression targets. 

## 3.3.2 Model Architecture 

The model starts with an initial convolutional layer with a large kernel size to capture low-level features, followed by batch normalization, ReLU activation, and max pooling. The core of the model comprises four residual blocks with increasing channel dimensions [39]. Each residual block contains two convolutional layers with batch normalization and ReLU, along with a shortcut connection to preserve gradient flow. After feature extraction, a global average pooling layer reduces spatial dimensions, yielding a fixed-length embedding vector of size 256. This embedding is then fed into the output heads: a regression head that produces 8 continuous values between 0 and 1, and two classification heads for discrete predictions. Our model has ∼5M parameters. 

## 3.3.3 Training 

For the discrete parameters, we compute cross-entropy losses. For the continuous parameters, we compute the ℓ1 losses. Losses are added without weighting. We use an 8/2 train-validation split, a batch size of 32, and the Adam optimizer with a learning rate of 1e-4. The model is trained for 100 epochs, which takes ∼12 hours on an A100 GPU. We observe that the validation loss for each parameter has converged. 

## 3.3.4 Task and Style Embeddings 

We extract and evaluate three representations from the sound matching model. The first representation is the 256dimensional embedding obtained right before the prediction heads, which encodes information necessary for solving the task—in our case, synthesis parameter prediction. We refer to this as the task embedding. The other two are inspired by image style transfer [40,41]. We refer to them as the style embedding. Our motivation for using style embeddings is twofold: first, they are invariant to the spatial location of audio events on spectrograms; and second, they use features 

> 6 https://github.com/DBraun/Vita 

713 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

from different layers of a model, thus capturing multiple levels of abstraction—a property shown to be effective for modeling perceptual timbre similarity [14]. The first style embedding, proposed by Gatys et al. [40], is computed as a Gram matrix of feature activations, where each entry captures the inner product between two channels across the spatial dimensions, resulting in a symmetric matrix that captures correlations between channels. The second style embedding is shown to be effective by Huang and Belongie [41] and is computed as the channel-wise mean and standard deviation of activations over the spatial dimensions. Given a feature map with shape (B, C, H, W ), where B is the batch size, C is the channel number, and H and W are the spatial dimensions, i.e. height and width, the style embedding of Gatys et al. has shape (B, C, C), and the style embedding of Huang and Belongie has shape (B, 2C, ). With our model, we extract both Gatys style embeddings and Huang style embeddings from five intermediate convolutional layers: the initial convolutional layer, and the first convolutional layers in each of the four residual blocks. Feature maps are obtained after batch normalization. We concatenate the embeddings obtained from different layers, resulting in a single Gatys style embedding and a single Huang style embedding per input. Together with the tasking embedding, we abbreviate them as s.m.-task, s.m.-Gatys, and s.m.-Huang. 



<!-- Start of picture text -->
Gatys_cosineGatys_12 Huang_cosineHuang_12 task_cosine .. best score fromtask_12 other models<br>0.70<br>0.65<br>Triplet AGR.<br>0.60<br>0.92<br>0.90<br>NDCG SIM.<br>0.88<br>0.4<br>MAE 0.3<br>0.2<br>5000 10000 25 50 75 100<br>step (first epoch zoomed in) epoch<br><!-- End of picture text -->

Figure 2. Evolution of alignment scores during the training of the sound matching model. The left column shows the detailed changes with the first epoch zoomed in, while the right column shows the overall progress across the total 100 epochs. For MAE, lower scores are better; for other metrics, higher scores are better. The best scores refer to the highest (or lowest, for MAE) values of each metric in Figure 3. 

## 3.4 Other Models and Dynamic Length Adaption 

We evaluate signal-processing-based methods<sup>7</sup> that do not learn from data, including mel-frequency cepstral coefficients (MFCC), multi-scale spectrograms (MSS) [7], and the joint time-frequency scattering transform (JTFS) [43]. We also evaluate pre-trained audio models interfaced through the Fréchet Audio Distance Toolkit [38], which are typically trained on large datasets and used to evaluate generative models, as their representations are considered to correlate well with perceptual music quality. This includes three CLAP models trained with natural language supervision [44,45]; two CDPAM models trained on perceptual ratings of audio quality [18]; and neural audio codecs including two Encodec models [46] and one Descript Audio Codec (DAC) [47], which compress audio into lowerbitrate latent representations. Additionally, we evaluate Music2Latent [48] and a reproduction of the Complex Autoencoder (CAE) [49] that produces representations invariant to transposition and time-shift.<sup>8</sup> 

In Section 3.2.1, we discussed how to produce equally shaped representations for audio of different lengths. Here, we describe how this is specifically achieved for each model. Since the longest sample in our data is 4.39 seconds (see Table 1), we compute just one frame of representation for the following models, with their respective analysis window lengths indicated in parentheses: CLAP (ten seconds for [45] and seven seconds for [44]) and CDPAM (five 

> 7 For audio at 44.1kHz, MFCC is computed with n_mfcc=40, MSS is computed with fft_sizes=(4096, 2048, 1024, 512, 256, 128), and JTFS is computed with J = 12, Q = (8, 2), Jfr = 3, and Qfr = 2 using the `Kymatio` package [42]. 

> 8 Trained with piano music from the MAPS dataset [50]. 

seconds). For these models, audio samples are padded to match the window length. The sound matching model has an analysis window of two seconds (which covers 19 out of 21 datasets) and is trained to capture the ADSR envelope, so the analysis window cannot be shifted. Therefore, we pad or truncate samples to a duration of two seconds. The above six models produce eight unique representations, for which we do not compute the time average since they contain only one time frame. For all other models, representations are computed using both time averaging and dynamic padding, where the shorter sample is padded to match the longer one within an audio pair. 

We also evaluate style embeddings extracted from one CLAP model [44], which differs from the sound matching model not only in training objective but also in architecture—it uses a Transformer backbone. However, style embeddings can be computed in a similar way: the internal representations produced by the Transformer consist of spatial tokens with a feature dimension, analogous to spatial locations and channel dimensions in CNNs. Therefore, we treat the transformer’s feature dimension as equivalent to the channel dimension in CNNs. Following this analogy, we compute Gatys style embeddings by measuring correlations between feature dimensions, and Huang style embeddings by computing statistics (mean and variance) across each feature. We compute style embeddings using the outputs from each Swin Transformer block in the first three layers. Each layer contains multiple blocks, with nine blocks in total. The resulting embeddings are concatenated into a single embedding per input for evaluation. 

714 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
dynamic-length_cosine dynamic-length_I2 time-avg_cosine time-avg_l2<br>Triplet AGR.<br>0.7<br>0.6 ıI II II<br>0.925<br>NDCG SIM.<br>0.900<br>0.875<br>MAE<br>0.3 _ _<br>0.2<br>mfcc s.m.-task mmss dac cae<br>clap-ms1<br>s.m.-Gatys s.m.-Huang music2latent encodec-24k encodec-48k<br>clap-ms-Huang1 clap-ms-Gatys1 clap-laion-music clap-laion-audio cdpam-content cdpam-acoustic<br><!-- End of picture text -->

Figure 3. Evaluation results. Each configuration shown at the top is represented by a unique color. For each alignment score, the best result within each configuration is marked with a star, while a yellow dot behind the star indicates the overall winner. For MAE, lower scores are better; for other metrics, higher scores are better. Representations are ordered by the mean triplet agreement across configurations, in descending order. For text labels on the x-axis, the same background color indicates different representations extracted from the same model. 

## 4. RESULTS AND DISCUSSION 

In Figure 2 and 3, we omit the Kendall and Spearman scores, as they are highly correlated with triplet agreement and produce nearly identical rankings of the evaluated representations. We choose to report triplet agreement instead, as it is a more intuitive metric to interpret than the other two. 

Figure 2 shows training-time alignment scores for our sound matching model on all 21 datasets. We use a threefold validation-test split to ensure a fair comparison with other models shown in Figure 3. For each score, we select the best-performing model based on validation performance using only checkpoints from the first epoch. Final results are reported as averages over the test folds. The style embeddings converge quickly, retaining high alignment with human timbre judgments, whereas the task embedding overfits and loses generalization over time. In Figure 3, the style embeddings from both the sound matching model and the CLAP model show clear improvements over their base representations, demonstrating the effectiveness of style embeddings regardless of training objective or model architecture. In particular, the Huang style embedding extracted from the CLAP model shows the strongest performance. 

MFCC remains competitive and outperforms many trained models. By contrast, CDPAM—trained on lowlevel distortion judgments of speech—does not adapt well to musical timbre. This may be due to differences in data domain, or it may echo findings from DreamSim [20], which suggest that perceptual similarity learned for one type of perturbation does not generalize to others. MSS also underperforms, consistent with prior work [51] showing that spectral distances can be problematic for capturing perceptual similarity of pitch. 

Interestingly, Encodec’s 24k model aligns better with 

human ratings than the 48k model, despite the former being trained on a variety of audio data, whereas the latter is trained exclusively on music. This suggests that increased compression combined with broader training data may encourage the model to discard irrelevant details while preserving perceptually meaningful structure, resulting in a more efficient internal timbre representation. This also highlights the effectiveness of Music2Latent, which aligns better with human ratings, has a high compression rate, and is trained on both music and speech. JTFS performs moderately on rank-based metrics but poorly on MAE. This suggests that its distance scale may be nonlinearly stretched relative to human perception, preserving the order of examples but distorting their absolute differences. 

## 5. CONCLUSION 

In this paper, we introduced a unified evaluation framework to compare model-derived distances with human similarity ratings from 21 classic timbre space datasets, encompassing a wide range of musical instrument sounds. We assessed both hand-crafted features (e.g., MFCC) and deep learning-based representations (e.g., CLAP, CDPAM, neural audio codecs), as well as a newly proposed sound matching model that inverts a wavetable synthesizer. Our results showed that style embeddings extracted from different models outperformed their base representations, and in particular, the Huang style embedding from the CLAP model is markedly superior to the others. To encourage further work, we provide a Python package that implements all our metrics and procedures. We hope this evaluation framework and Python package will encourage advancements in timbre metrics across tasks like generative modeling and instrument retrieval. 

715 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 6. ETHICS STATEMENTS 

This work evaluates models using datasets that primarily feature Western musical instruments, which may reflect a cultural bias toward Western music traditions. We acknowledge this limitation and are enthusiastic about including non-Western musical data in our evaluation framework, as it may both enhance cultural diversity and help reveal biases in the models’ behavior under broader musical contexts. 

## 7. ACKNOWLEDGEMENTS 

We thank Mathieu Lagrange for the valuable discussions. This work is supported by the EPSRC UKRI Centre for Doctoral Training in Artificial Intelligence and Music (grant number EP/S022694/1). This research utilized Queen Mary’s Apocrita HPC facility, supported by QMUL Research-IT. http://doi.org/10.5281/zenodo.438045. 

## 8. REFERENCES 

- [1] M. Barthet, P. Guillemain, R. Kronland-Martinet, and S. Ystad, “From clarinet control to timbre perception,” Acta Acustica united with Acustica, vol. 96, no. 4, pp. 678–689, 2010. 

- [2] K. Patil, D. Pressnitzer, S. Shamma, and M. Elhilali, “Music in our ears: the biological bases of musical timbre perception,” PLoS Computational Biology, vol. 8, no. 11, p. e1002759, 2012. 

- [3] A. Zacharakis, K. Pastiadis, and J. D. Reiss, “An interlanguage unification of musical timbre: Bridging semantic, perceptual, and acoustic dimensions,” Music Perception: An Interdisciplinary Journal, vol. 32, no. 4, pp. 394–412, 2015. 

- [4] S. McAdams, “The perceptual representation of timbre,” Timbre: Acoustics, Perception, and Cognition, pp. 23– 57, 2019. 

- [5] T. M. Elliott, L. S. Hamilton, and F. E. Theunissen, “Acoustic structure of the five perceptual dimensions of timbre in orchestral instrument tones,” The Journal of the Acoustical Society of America, vol. 133, no. 1, pp. 389–404, 2013. 

- [6] J. Engel, C. Resnick, A. Roberts, S. Dieleman, M. Norouzi, D. Eck, and K. Simonyan, “Neural audio synthesis of musical notes with wavenet autoencoders,” in International Conference on Machine Learning. PMLR, 2017, pp. 1068–1077. 

- [7] J. Engel, L. H. Hantrakul, C. Gu, and A. Roberts, “DDSP: Differentiable digital signal processing,” in International Conference on Learning Representations, 2020. [Online]. Available: https://openreview.net/ forum?id=B1x1ma4tDr 

- [8] D. L. Wessel, “Timbre space as a musical control structure,” Computer Music Journal, pp. 45–52, 1979. 

- [9] P. Esling, A. Chemla-Romeu-Santos, and A. Bitton, “Generative timbre spaces with variational audio synthesis,” in Proceedings of the International Conference on Digital Audio Effects (DAFx), 2018, pp. 175–181. 

- [10] V. Lostanlen, C. El-Hajj, M. Rossignol, G. Lafay, J. Andén, and M. Lagrange, “Time–frequency scattering accurately models auditory similarities between instrumental playing techniques,” EURASIP Journal on Audio, Speech, and Music Processing, vol. 2021, no. 1, p. 3, 2021. 

- [11] S. Chollet, D. Valentin, and H. Abdi, “Free sorting task,” Novel Techniques in Sensory Characterization and Consumer Profiling, vol. 207, 2014. 

- [12] C. Vahidi, S. Singh, E. Benetos, H. Phan, D. Stowell, G. Fazekas, and M. Lagrange, “Perceptual musical similarity metric learning with graph neural networks,” in 2023 IEEE Workshop on Applications of Signal Processing to Audio and Acoustics (WASPAA). IEEE, 2023, pp. 1–5. 

- [13] E. Thoret, B. Caramiaux, P. Depalle, and S. Mcadams, “Learning metrics on spectrotemporal modulations reveals the perception of musical instrument timbre,” Nature Human Behaviour, vol. 5, no. 3, pp. 369–377, 2021. 

- [14] B. Pascal and M. Lagrange, “On the robustness of musical timbre perception models: From perceptual to learned approaches,” in 2024 32nd European Signal Processing Conference (EUSIPCO). IEEE, 2024, pp. 41–45. 

- [15] C. Vahidi, B. Hayes, C. Saitis, and G. Fazekas, “Acoustic representations for perceptual timbre similarity,” in Digital Music Research Network One-Day Workshop (DMRN+ 16), 2021. 

- [16] B. Hayes and C. Vahidi, “Timbre dissimilarity metrics,” https://github.com/ben-hayes/ timbre-dissimilarity-metrics, 2021, accessed: 2025-0329. 

- [17] P. Manocha, A. Finkelstein, R. Zhang, N. J. Bryan, G. J. Mysore, and Z. Jin, “A differentiable perceptual audio metric learned from just noticeable differences,” in Interspeech, 2020. 

- [18] P. Manocha, Z. Jin, R. Zhang, and A. Finkelstein, “Cdpam: Contrastive learning for perceptual audio similarity,” in IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2021, pp. 196–200. 

- [19] R. Zhang, P. Isola, A. A. Efros, E. Shechtman, and O. Wang, “The unreasonable effectiveness of deep features as a perceptual metric,” in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, 2018, pp. 586–595. 

716 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [20] S. Fu, N. Tamir, S. Sundaram, L. Chai, R. Zhang, T. Dekel, and P. Isola, “Dreamsim: Learning new dimensions of human visual similarity using synthetic data,” in Advances in Neural Information Processing Systems, vol. 36, 2023, pp. 50 742–50 768. 

- [21] L. Muttenthaler, L. Linhardt, J. Dippel, R. A. Vandermeulen, K. Hermann, A. Lampinen, and S. Kornblith, “Improving neural network representations using human similarity judgments,” Advances in Neural Information Processing Systems, vol. 36, pp. 50 978–51 007, 2023. 

- [22] M. N. Hebart, O. Contier, L. Teichmann, A. H. Rockter, C. Y. Zheng, A. Kidder, A. Corriveau, M. VaziriPashkam, and C. I. Baker, “Things-data, a multimodal collection of large-scale datasets for investigating object representations in human brain and behavior,” Elife, vol. 12, p. e82580, 2023. 

- [23] J. M. Grey, “Multidimensional perceptual scaling of musical timbres,” the Journal of the Acoustical Society of America, vol. 61, no. 5, pp. 1270–1277, 1977. 

- [24] J. M. Grey and J. W. Gordon, “Perceptual effects of spectral modifications on musical timbres,” The Journal of the Acoustical Society of America, vol. 63, no. 5, pp. 1493–1500, 1978. 

- [25] P. Iverson and C. L. Krumhansl, “Isolating the dynamic attributes of musical timbrea,” The Journal of the Acoustical Society of America, vol. 94, no. 5, pp. 2595–2603, 1993. 

- [26] F. Opolko and J. Wapnick, McGill University master samples (3 CDs). Quebec, Canada: McGill University, 1987. 

- [27] S. McAdams, S. Winsberg, S. Donnadieu, G. De Soete, and J. Krimphoff, “Perceptual scaling of synthesized musical timbres: Common dimensions, specificities, and latent subject classes,” Psychological Research, vol. 58, pp. 177–192, 1995. 

- [28] S. Lakatos, “A common perceptual space for harmonic and percussive timbres,” Perception & Psychophysics, vol. 62, no. 7, pp. 1426–1439, 2000. 

- [29] M. Goto, H. Hashiguchi, T. Nishimura, and R. Oka, “RWC music database: Music genre database and musical instrument sound database,” in Proceedings of the 4th International Conference on Music Information Retrieval (ISMIR), 2003. 

- [30] F. Opolko and J. Wapnick, The McGill University master samples collection on DVD (3 DVDs). Quebec, Canada: McGill University, 1987. 

- [31] K. Siedenburg, K. Jones-Mollerup, and S. McAdams, “Acoustic and categorical dissimilarity of musical timbre: Evidence from asymmetries between acoustic and chimeric sounds,” Frontiers in Psychology, vol. 6, p. 1977, 2016. 

- [32] Vienna Symphonic Library, https://www.vsl.co.at/. 

- [33] C. Saitis and K. Siedenburg, “Brightness perception for musical instrument sounds: Relation to timbre dissimilarity and source-cause categories,” The Journal of the Acoustical Society of America, vol. 148, no. 4, pp. 2256–2266, 2020. 

- [34] C. Vahidi, G. Fazekas, C. Saitis, and A. Palladini, “Timbre space representation of a subtractive synthesizer,” in Proceedings of the 2nd International Conference on Timbre, 2020, p. 30–33. 

- [35] C. J. Steinmetz and J. Reiss, “pyloudnorm: A simple yet flexible loudness meter in python,” in Audio Engineering Society Convention 150. Audio Engineering Society, 2021. 

- [36] Nicki Skafte Detlefsen, Jiri Borovec, Justus Schock, Ananya Harsh, Teddy Koker, Luca Di Liello, Daniel Stancl, Changsheng Quan, Maxim Grechkin, and William Falcon, “TorchMetrics - Measuring Reproducibility in PyTorch,” Feb. 2022. [Online]. Available: https://github.com/Lightning-AI/torchmetrics 

- [37] V. Khrulkov, L. Mirvakhabova, E. Ustinova, I. Oseledets, and V. Lempitsky, “Hyperbolic image embeddings,” in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2020, pp. 6418–6428. 

- [38] A. Gui, H. Gamper, S. Braun, and D. Emmanouilidou, “Adapting frechet audio distance for generative music evaluation,” in IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2024, pp. 1331–1335. 

- [39] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image recognition,” in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, 2016, pp. 770–778. 

- [40] L. A. Gatys, A. S. Ecker, and M. Bethge, “Image style transfer using convolutional neural networks,” in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, 2016, pp. 2414–2423. 

- [41] X. Huang and S. Belongie, “Arbitrary style transfer in real-time with adaptive instance normalization,” in Proceedings of the IEEE International Conference on Computer Vision, 2017, pp. 1501–1510. 

- [42] M. Andreux, T. Angles, G. Exarchakis, R. Leonarduzzi, G. Rochette, L. Thiry, J. Zarka, S. Mallat, J. Andén, E. Belilovsky et al., “Kymatio: Scattering transforms in python,” Journal of Machine Learning Research, vol. 21, no. 60, pp. 1–6, 2020. 

- [43] J. Andén, V. Lostanlen, and S. Mallat, “Joint time– frequency scattering,” IEEE Transactions on Signal Processing, vol. 67, no. 14, pp. 3704–3718, 2019. 

717 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [44] B. Elizalde, S. Deshmukh, and H. Wang, “Natural language supervision for general-purpose audio representations,” 2023. [Online]. Available: https: //arxiv.org/abs/2309.05767 

- [45] Y. Wu, K. Chen, T. Zhang, Y. Hui, T. Berg-Kirkpatrick, and S. Dubnov, “Large-scale contrastive language-audio pretraining with feature fusion and keyword-to-caption augmentation,” in IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2023. 

- [46] A. Défossez, J. Copet, G. Synnaeve, and Y. Adi, “High fidelity neural audio compression,” arXiv preprint arXiv:2210.13438, 2022. 

- [47] R. Kumar, P. Seetharaman, A. Luebs, I. Kumar, and K. Kumar, “High-fidelity audio compression with improved rvqgan,” Advances in Neural Information Processing Systems, vol. 36, pp. 27 980–27 993, 2023. 

- [48] M. Pasini, S. Lattner, and G. Fazekas, “Music2latent: Consistency autoencoders for latent audio compression,” Proceedings of the 25th International Conference on Music Information Retrieval (ISMIR), 2024. 

- [49] S. Lattner, M. Dörfler, and A. Arzt, “Learning complex basis functions for invariant representations of audio,” in Proceedings of the 20th International Conference on Music Information Retrieval (ISMIR), 2019. 

- [50] V. Emiya, N. Bertin, B. David, and R. Badeau, “Maps-a piano database for multipitch estimation and automatic transcription of music,” 2010. 

- [51] J. Turian and M. Henry, “I’m sorry for your loss: Spectrally-based audio distances are bad at pitch,” in ”I Can’t Believe It’s Not Better!” NeurIPS 2020 workshop, 2020. [Online]. Available: https://openreview.net/forum?id=Z4UwGkTRTes 

718 

