---
paper_id: "000048"
year: 2022
title: "Download pdf"
source_url: "https://zenodo.org/record/7342755/files/000048.pdf"
---

# **SYMBOLIC MUSIC LOOP GENERATION WITH NEURAL DISCRETE REPRESENTATIONS** 

**Sangjun Han**<sup>1</sup> **, Hyeongrae Ihm**<sup>1</sup> **, Moontae Lee**<sup>1,2</sup> **, Woohyung Lim**<sup>1</sup> 1 LG AI Research, 2 University of Illinois at Chicago 

```
{sj.han, hrim, moontae.lee, w.lim}@lgresearch.ai
```

## **ABSTRACT** 

Since most of music has repetitive structures from motifs to phrases, repeating musical ideas can be a basic operation for music composition. The basic block that we focus on is conceptualized as loops which are essential ingredients of music. Furthermore, meaningful note patterns can be formed in a finite space, so it is sufficient to represent them with combinations of discrete symbols as done in other domains. In this work, we propose symbolic music loop generation via learning discrete representations. We first extract loops from MIDI datasets using a loop detector and then learn an autoregressive model trained by discrete latent codes of the extracted loops. We show that our model outperforms well-known music generative models in terms of both fidelity and diversity, evaluating on random space. Our code and supplementary materials are available at https://github.com/sjhan91/Loop_VQVAE_Official. 

## **1. INTRODUCTION** 

With the advance of generative models, many studies are trying to model sequential data such as language and speech. Music can also benefit from their previous works since it consists of a sequence of multiple notes to represent the composer’s intention. Through the advancement, individuals can imitate the musical inspiration of artists without musical expertise. 

Several works related to music generation have focused on generating long sequences by utilizing the expressive power of Transformer [1-4]. It is a promising approach because the Transformer with hierarchical layers can learn various types of repetitive structures on its self-attentions. However, it still has limitations, derived from the error accumulation and rhythmic irregularity, to achieve the ultimate goal which is to compose full-length music [1, 2]. To tackle that problem, we explicitly utilize recurrence properties in music, generating short and fixed-length music phrases that can be used as basic patterns of music. 

Repeating musical ideas is a basic operation for music composition. This operation conceptualizes the loop, an essential ingredient for creating remixes or mash-ups [5]. With the concept, we can simplify the generation task into generating one distinctive pattern which consists only of a 

> © S. Han, H. Ihm, M. Lee, and W. Lim. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). **Attribution:** S. Han, H. Ihm, M. Lee, and W. Lim, “Symbolic Music Loop Generation with Neural Discrete Representations”, in _Proc. of the 23_<sup>_rd_</sup> _Int. Society for Music Information Retrieval Conf._ , Bengaluru, India, 

few bars. For loop extraction, previous works have attempted to detect autocorrelated peaks (it relies on an assumption that it is sufficient to detect the starting point of phrases) [5, 6], but we apply the knowledge of overall loop structures, obtained from a public audio dataset, to the MIDI domain. 

Another intuition is that the musical ideas can be formed in combinations of finite symbols. It is known that learning discrete latent codes is sufficient to represent the continuous world since many modalities consist of sequences of symbols [7]. For example, objects in vision, words in language, and phonemes in speech may be candidates of symbols. Also, compressing raw data into discrete semantic units makes an autoregressive model easy to train by capturing long-range data dependency [8]. If we regard consecutive notes as symbols, it is natural to adopt discrete representation as the basis of our autoregressive generator. This process can emphasize pattern to pattern structures sacrificing the minimal loss of note details. 

In contrast to using Inception Score (IS) and Fréchet Inception Distance (FID) for computer vision [9, 10], no consensus has been made for evaluating generated music. This is because the absence of pre-trained feature extractors prohibits the comparison of true and generated samples on feature space. Recently, Naeem has shown that random embedding can also be effective when the target distribution is far from pre-trained model statistics [11]. Using the random initialized networks, we evaluate our generative models on sample fidelity and diversity as firstly suggested in [12]. 

In this work, we propose symbolic music loop generation via learning discrete representations. It involves two main processes; 1) _loop extraction_ from MIDI datasets using a loop detector and 2) _loop generation_ from an autoregressive model trained by discrete latent codes of the extracted loops. The outputs of the generative model are loops consisting of 8 bars, which can be repeated seamlessly. Since we aim to generate polyphony and multitrack sequences, the bass and drum are chosen for our experiments, which are fundamental components of melody and rhythm. Additionally, we adopt an evaluation protocol from [11] to measure two-dimensional score which stands for fidelity and diversity. Our contributions are summarized as follows; 

- We propose the framework of symbolic music loop generation, which involves loop extraction, loop generation, and its evaluations. 

403 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

- For loop extraction, we design a structure-aware loop detector trained by external audio sources to extract loops of 8 bars from MIDI. 

- For loop generation, we verify that an autoregressive model combined with discrete representations can generate plausible loop phrases which can be repeated. 

- With randomly initialized networks for embedding, we evaluate sample quality in terms of fidelity and diversity. 

## **2.3 Discrete Representations** 

As opposed to VAE [23] with continuous prior, Oord has proved that a finite set of latent codes is sufficient to reconstruct while it prevents posterior collapse [7]. Powerful autoregressive priors with the latent codes have shown promising performance not only in image generation [8] but also text2image [24], and video generation [25]. Loop generation can also benefit from discrete data compression by expressing long-range structural patterns. 

## **2. RELATED WORK** 

We introduce several works related to the history of loop extraction and music generation, the effectiveness of discrete representations, and the development of evaluating generative models. 

## **2.1 Loop Extraction** 

For symbolic music generation, some researchers have prepared their dataset by sliding a window with a stride of 1 bar [13, 14]. Although they have achieved good generative performance, this process does not consider relative positions within music, generating ambiguous phrases. 

Some works have imposed structural constraints on music generation models [15, 16], or directly detect novel segments which are repetitive in time series [17, 18]. In the audio domain, there have been attempts to extract loops explicitly by capturing repeated phrases [5, 6]. They extract harmonic features such as chroma vectors or mel-frequency cepstrum and catch autocorrelation peaks to determine the starting point of loops. They also require a heuristic process to decide which features should be more weighted. In contrast, our loop detector works on a datadriven approach, so it does not require a manual process such as feature extraction and weighting strategies. 

A recent work for drum loop generation has informed the availability of a human-created loop dataset from Looperman (https://www.looperman.com/) [19]. Although it consists of audio sources with various instruments and genres, we suggest a promising approach to combine them with Lakh MIDI Dataset (LMD) [20]. Concretely, we extract domain-invariant loop structures from Looperman and train a loop detector using them to extract loops from LMD. 

## **2.2 Symbolic Music Generation** 

To make MIDI available in machine learning, two representation methods are prevalent; event-based representation and time-grid based representation [21]. Although the former can represent high time-resolution with a few event vectors, we choose the latter one to benefit from fixedlength and repetitive structures for music. There have been several works to deal with polyphony multitrack representation [1, 13, 22]. Especially for time-grid based representation, MuseGAN [22] has stacked five instruments each of which consists of 4 bars and 84 pitches. We follow their method while restricting to two instruments, the bass and drum. 

## **2.4 Evaluation of Generative Models** 

Proper evaluation metrics for generative models are important to reduce human evaluation labor. Previous works of music generation have inspected model metrics ( _e.g.,_ log-likelihood) or musical metrics on data space to evaluate how much true and generated samples are similar [3, 22, 26]. Comparison on data space, however, is vulnerable to pixel by pixel phase difference, ignoring data semantics. Without available pre-trained networks, it has been reported that random embeddings are more robust for evaluation rather than using models trained by other data domains [11]. In this respect, we take randomly initialized networks as our feature extractor and evaluate our music samples on feature space. 

The commonly used metrics in computer vision are IS and FID which compute a one-dimensional score. To distinguish fidelity and diversity from the score, Sajjadi has suggested precision and recall evaluating overlapped ratio between true and generated distribution [12]. After that, some works have proposed different ways of constructing data distribution using k-nearest neighbors (KNN) [11, 27]. We adopt KNN based evaluation protocol since it is not affected by its initialization and is robust to outliers. 

## **3. PROPOSED METHOD** 

Our work starts with collecting MIDI loops using a structure-aware loop detector. Since we design the detector to take not the music itself but bar-to-bar structures, we can train it with a loop-labeled dataset from audio domain. After obtaining the MIDI loop set, we design a loop generator in two-stage; compressing data into discrete space and building an autoregressive model with them. Lastly, generated samples are evaluated on qualitative and quantitative metrics. 

## **3.1 Data Preparation** 

## _3.1.1 Looperman Dataset_ 

Looperman Dataset from the audio domain is collected and transformed for training our loop detector. We collect 1,000 loops of 8 bars from Looperman, a website allowing to upload and download free music loops. Formally, we cess of data transformation for the loop detector will be denote one loop that is 1-D audio as described in section 3.2.1. 𝑥𝑥𝑊 **𝑊** 𝑊𝑊 ∈ ℛ. The pro- 

404 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
Loop WAV (XWAV) MIDI(XMIDI)<br>Mel-spectogram<br>One-class<br>Loop Detector<br>Training Inference<br>CWAV CMIDI CwAV CM1DI<br>Correlation Matrix<br>are used to train the one-class loop detector and we extract Figure 1.  The process of loop extraction. (a)  (a) (b) 𝑥𝑥𝑊 𝑊 𝑊𝑊  and<br>𝑥𝑥𝑀 𝑀 𝑀 𝑀  are transformed to each correlation matrix. (b) 𝐶𝐶𝑊 𝑊 𝑊𝑊<br>to the detector.<br>loops from Lakh MIDI Dataset by forward passing 𝐶𝐶𝑀 𝑀 𝑀<br><!-- End of picture text -->

## _3.1.2 Lakh MIDI Dataset_ 

Lakh MIDI Dataset is a collection of MIDI files with various genres and tracks, so it is appropriate to conduct symbolic music experiments [20]. In this experiment, each note is quantized on the 16th note unit with binary representation so that 16 notes are placed in a bar. To verify the feasibility of multitrack polyphony generation, we extract two instruments; bass guitar (program=32~39) and drum (is_drum=True) which play crucial roles of melodic and rhythmic patterns in music. The bass pitches are clipped from C1 to B4 (48 pitches). If several pitches for the bass are played at the same time, we make only the lowest pitch alive for natural play. For the drum set, nine components (kick, snare, closed hi-hat, open hi-hat, low tom, mid tom, high tom, crash, and ride) are regarded as a standard set and the rest of the components are incorporated into the closest one or discarded. Formally, our pianoroll representation can be described as follows; 𝑥𝑥𝑀 **𝑀** 𝑀 **𝑀** ∈ {0, 1}<sup>(𝑇𝑇×𝐵𝐵)×𝑃𝑃</sup> where 𝑇𝑇 is the number of time steps in a bar (𝑇𝑇= 16), 𝐵𝐵 is the number of bars (by sliding a window with a stride of 1 bar, removing non-𝐵𝐵= 8), and 𝑃𝑃 is the number of pitches (4/4 signature music. Using pretty_midi [28] and pypiano-𝑃𝑃= 57). We collect 5,687,274 phrases of 8 bars roll [29] in Python library, MIDI processing is conducted. 

## **3.2 Loop Extraction** 

_3.2.1 Data Transformation for the Loop Detector_ indicating bar-to-bar correlation (Figure 1 (a)). For the We transform each the 𝑥𝑥𝑊 **𝑊** 𝑊𝑊 and 𝑥𝑥𝑀 **𝑀** 𝑀 **𝑀** to 𝐵𝐵× 𝐵𝐵 matrix 𝑥𝑥𝑊 **𝑊** 𝑊𝑊, we extract 𝐵𝐵 mel-spectrograms each corresponding to 𝐵𝐵 bars and compute a correlation matrix (𝐶𝐶𝑊 **𝑊** 𝑊𝑊). For the 𝑥𝑥𝑀 **𝑀** 𝑀 **𝑀** , we compute normalized Hamming distance among scribed in Appendix B.3. bars and renormalize it to express correlation (𝐶𝐶𝑀 **𝑀** 𝑀 **𝑀** ). Only the upper triangle part of 𝐶𝐶 is used. More details are de- 



<!-- Start of picture text -->
Random Set 4 00 0<br>Random Set 3 000<br>Random Set 2 -∞<br>Groups<br>Random Set 1 0<br>Loop Set 0m 8 00 o<br>0.0 0.5 1.0 1.5 2.0 2.5 3.0 3.5<br>Loop Score<br><!-- End of picture text -->

**Figure 2.** The evaluation of our loop detector. Green lines in the boxes indicate median values and red triangles for mean values. 

## _3.2.2 Loop Extraction through the Loop Detector_ 

Our loop detector is to classify loop and non-loop phrases, given only loop-labeled datasets. It is related to the problem of anomaly detection trained in an unsupervised way to construct normal data distribution. At inference time, outliers from the distribution are regarded as anomalous samples. Similarly, we treat 𝐶𝐶𝑊 **𝑊** 𝑊𝑊 as normal samples One-Class Deep SVDD [30] as our loop detector, of which (training set) and measure the likelihood of 𝐶𝐶𝑀 **𝑀** 𝑀 **𝑀** (test set) the training objective is on 𝐶𝐶𝑊 **𝑊** 𝑊𝑊 distribution. Among several ways, we choose 1 ∑ (1) 𝑛𝑛 𝑚 **𝑚** 𝑚𝑚 𝑛𝑛 𝑖𝑖=1 ||𝑓𝑓𝑤𝑤(𝑥𝑥𝑖𝑖) −𝑐𝑐||<sup>2</sup> + 𝜆 **𝜆** (𝑊𝑊) where 𝑓𝑓𝑤𝑤 is a neural network taking input 𝑥𝑥 with learnaThe objective can be thought as mapping all data samples ble parameters 𝑊𝑊, 𝑚𝑚 is the number of training samples, 𝑐𝑐 is a center vector, and 𝜆𝜆(𝑊𝑊) is a controllable regularizer. −1 and center close to center 𝑐𝑐, contracting a hypersphere. Initially, 𝑓𝑓𝑤𝑤 is trained to reconstruct 𝑥𝑥 with a decoder 𝑓𝑓𝑤𝑤 with bias-off and LeakyReLU(0.1) to prevent hy-𝑐𝑐 is set to mean vectors acquired from 𝑓𝑓𝑤𝑤 initial pass of persphere collapse as referred in [30]. During training, the training data. 𝑓𝑓𝑤𝑤 consists of 3 fully-connected layers AdamW optimizer [31] is applied with cosine annealing from 1e-3 to 5e-6 for 1,000 epochs. At inference time, the (2) loop score of 𝐶𝐶𝑀 **𝑀** 𝑀 **𝑀** can be obtained as 𝑙 **𝑙** 𝑙𝑙𝑝𝑝 𝑠𝑠𝑐𝑐𝑙𝑙𝑠 **𝑠** = ||𝑓𝑓𝑤𝑤∗(𝑥𝑥) −𝑐𝑐||<sup>2</sup> cess of loop extraction is illustrated on Figure 1 (b)). Samwhere ples with lower loop scores are considered close to the loop. 𝑤𝑤<sup>∗</sup> stands for optimized parameters of 𝑓𝑓 (the proTo evaluate the loop detector, we manually pick 100 groups randomly picked (Figure 2). Although the randomized groups can contain subsets of loops, we can ver-loop samples from 𝑥𝑥𝑀 **𝑀** 𝑀 **𝑀** and compare them with 4 ify that the loop set group indicates the lowest loop score (0.153 (±0.282)). Also, paired _t_ -test between the loop group and each other group shows the statistically signifiwhether loop or not, we set a conservative threshold as cant difference with positive one sigma of the loop score distribution (trans-𝑝𝑝< 0.001. When determining to be used at loop generation stage. formed by 𝑙 **𝑙** 𝑙𝑙 to fit close to Gaussian distribution) from the training set. Consequently, we collect 751,935 𝑥𝑥𝑀 **𝑀** 𝑀 **𝑀** 

405 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
Conv1d<br>Decoder<br>ResBlock<br>4 x2<br>Upsample Quantized Z<br>Dictionary<br>ResBlock e2e3e4 … eκ<br>x2<br>Z<br>ConvBlock<br>Encoder<br>Conv1d<br>ž1 ž2 ž3<br>LSTM x4 Autoregressivè Model<br>z1 Z2 Z3<br><!-- End of picture text -->

**Figure 3.** The process of loop generation. The upper denotes VQ-VAE and the bottom for LSTM based autoregressive model. 

## **3.3 Loop Generation** 

## _3.3.1 Data Compression using VQ-VAE_ 

VQ-VAE [7] maps a data sequence into discrete latent space and reconstructs it to the original data space. With an encoder 𝑞𝑞𝜙𝜙and a decoder 𝑝𝑝𝜃𝜃, the objective becomes 𝑚 **𝑚** 𝑥𝑥 𝔼𝔼[𝑙 **𝑙** 𝑙𝑙𝑝𝑝𝜃𝜃(𝑥𝑥|𝑧𝑧)] −𝛽𝛽||𝑞𝑞𝜙𝜙(𝑧𝑧|𝑥𝑥) −𝑠𝑠𝑙𝑙[𝑠𝑠]|| (3) where 𝑠𝑠𝑙𝑙 denotes a stop gradients operator for the dictionary embedding 𝑠𝑠. During forward pass, latent 𝑧𝑧 from the encoder 𝑞𝑞𝜙𝜙(𝑧𝑧|𝑥𝑥) is quantized to nearest embedding 𝑠𝑠. The ary is updated in the sense of centroids of K-means clus-second term above is responsible for the latent 𝑧𝑧 not to ditering. verge far from 𝑠𝑠. For every batch, the embedding dictionOur VQ-VAE (Figure 3) encodes x = {𝑥𝑥1, 𝑥𝑥2 ,∙∙∙, 𝑥𝑥𝑇𝑇×𝐵𝐵}, 𝑥𝑥denotes latent dimensions (𝑖𝑖 ∈ℝ<sup>𝑃𝑃</sup> into z = {𝑧𝑧1, 𝑧𝑧2 ,∙∙∙, 𝑧𝑧𝑆𝑆}= 16, 𝑧𝑧𝑖𝑖 ∈ℝ). Starting from ran-<sup>𝑀𝑀</sup> where S denotes the number of time steps (domly initialized dictionary𝑆𝑆= 32) in latent space and 𝐷𝐷 ped to the nearest embed= {𝑠𝑠1, 𝑠𝑠2 ,∙∙∙, 𝑠𝑠𝐾𝐾} , 𝑠𝑠𝑖𝑖 ∈ℝ<sup>𝑀𝑀</sup> beddings are passed to the V(𝐾𝐾= 512), the latent 𝑧𝑧𝑖𝑖 is AE decoder to reconstruct ding their original data. For the 𝑠𝑠𝑘𝑘 where 𝑘𝑘= 𝑚𝑚𝑠𝑠𝑙𝑙𝑚 **𝑚** 𝑚𝑚𝑗𝑗 𝑖𝑖onstruction objective, our<sup>−𝑠𝑠</sup> 𝑗𝑗<sup>. After that, the em-</sup> data representation is regarded as multi-label for each time time step), so cross-entropy loss with softmax is not suitastep (multiple 1s can exist on pitch ble. Our objective for the reconstruction is described as 𝑃𝑃 dimension at one 

|Model|Reconstruction Error|
|---|---|
|CNN-VAE|4.412e-3|
|VQ-VAE|6.643e-3|



**Table 1.** The reconstruction errors. This is computed as the average of hamming distance between input and target samples of the validation set. 

𝑛1 ∑ ∑ (4) 𝑛𝑛 𝑛𝑛 𝑖𝑖=1 𝑗𝑗=1 𝑚 **𝑚** 𝑚𝑚 − 𝐿𝐿 (𝜎𝜎(𝑙𝑙𝑖𝑖𝑗𝑗), 𝑦𝑦𝑖𝑖𝑗𝑗) where 𝐿𝐿 denotes binary cross-entropy, 𝜎𝜎 is sigmoid funcotherwise 0. tion, 𝑙𝑙 is outputs of the VQ-VAE with 𝑚𝑚 notes, and 𝑦𝑦 for ground truth. WhenThe details of our VQ-VAE architectures (Figure 3) are 𝜎𝜎(𝑙𝑙𝑖𝑖𝑗𝑗) ≥0.5, it predicts label as 1, described in Appendix B.4. Empirically, we have verified sion, severely deteriorates the reconstruction task of the that a high compression ratio, especially along 𝑆𝑆 dimenboth the compression ratio and reconstruction quality. AdamW optimizer and cosine annealing from 1e-3 to 5e-6 VQ-VAE. The value of 𝑆𝑆 has been determined to consider is applied to the model training. As did in [32], random with one of batch samples. After training, we forward pass restarting is applied to less referenced 𝑠𝑠𝑖𝑖, replacing them _3.3.2 Generation through an Autoregressive Model_ the training set to obtain quantized embeddings 𝑧𝑧. 

_3.3.2 Generation through an Autoregressive Model_ We design an autoregressive model ∏ over the quantized embeddings to generate unseen sam-𝑆𝑆 𝑖𝑖=0 𝑝𝑝𝜃𝜃(𝑧𝑧𝑖𝑖 |𝑧𝑧<𝑖𝑖) LSTM with an embedding layer. For each time step, softples. The quantized indices 𝑘𝑘 are used as inputs of 4-layers max output predicts next step index 𝑘𝑘 (validation accuracy sampling unseen data in full sampling mode, temperatures 76.651% in teacher forcing mode). 𝑧𝑧0 is sampled from in softmax enable us to control sample diversity (tempera-multinomial distribution 𝑝𝑝(𝑧𝑧0) of the training set. When ture=0.7). We compare several sampling methods such as temperature sampling, top-k sampling [33], and nucleus sampling [34]. The generated indices are decoded by the VQ-VAE’s decoder. 

## **4. QUANTITATIVE EVALUATION** 

For quantitative evaluation of generated samples, we address three concepts; 1) _model metric_ related to evaluating the capacity of generative models, 2) _musical style_ related to measuring how much our intended properties of the loop are involved in generated samples, and 3) _similarity metrics_ related to how much generated samples are involved in the training set on feature space (or vice versa). 

## **4.1 Model Metric** 

**Reconstruction Error:** For VAE, the reconstruction error is part of the objective function that indicates how well the 

406 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

|Model|LS|UP|ND|P|R|D|C|
|---|---|---|---|---|---|---|---|
|TrainingSet|6.806e-3|5.769|14.383|-|-|-|-|
|CNN-VAE|3.496e-1|5.614|12.648|0.642±0.033|0.625±0.021|0.617±0.076|0.746±0.024|
|Music Transformer|7.200e-1|4.127|11.290|0.546±0.077|0.359±0.113|0.687±0.174|0.408±0.064|
|MuseGAN|2.307e-1|**5.790**|14.011|0.641±0.013|**0.689**±**0.012**|0.673±0.045|0.842±0.013|
|VQ-VAE+LSTM<br>(temperature sampling)|2.275e-1|5.079|14.289|0.768±0.013|0.655±0.022|1.263±0.047|0.949±0.002|
|VQ-VAE+LSTM<br>(top-k sampling=30)|**1.978e-1**|5.044|14.320|0.779±0.015|0.636±0.015|1.328±0.072|**0.952**±**0.004**|
|VQ-VAE+LSTM<br>(top-p sampling=0.08)|2.037e-1|5.042|**14.341**|**0.783**±**0.017**|0.638±0.029|**1.337**±**0.075**|0.950±0.005|



**Table 2.** The result table indicates all metrics explained at section 4.2 and 4.3. We compute P, R, D, and C from 10 different networks, so we denote mean values with standard deviations. Best values are marked in bold font. 

|Model|F1score<br>(P & R)|F1score<br>(D & C)|
|---|---|---|
|CNN-VAE|0.633|0.675|
|Music Transformer|0.433|0.512|
|MuseGAN|0.664|0.748|
|VQ-VAE+LSTM<br>(temperature sampling)|**0.707**|1.084|
|VQ-VAE+LSTM<br>(top-k sampling=30)|0.700|1.109|
|VQ-VAE+LSTM<br>(top-p sampling=0.08)|0.703|**1.111**|



**Table 3.** F1 score from Table 2 results. 

model decodes its latent features to the original data. However, perfect satisfaction with the objective does not guarantee to generate high-quality samples (empirically, we have verified that original VAE has produced many noisy samples even after achieving the minimal reconstruction error when forcing Kullback-Leibler divergence term to 0). 

## **4.2 Musical Style** 

The investigation of used harmonics and rhythm patterns indicates the musical style of our generated samples. **Loop Score (LS):** Using the trained loop detector, we can evaluate how much generated samples are close to the loop. **Unique Pitch (UP):** It computes the average number of used pitches per bar [22]. It reflects harmonic components on data space. It is desirable for generated samples to follow UP values of the training set. 

**Note Density (ND):** It computes the average number of notes played per bar considering all instruments [26]. It reflects rhythmic components on data space. It is desirable for generated samples to follow ND values of the training set. 

latent space while indicating the sample fidelity and diversity. 

**Precision & Recall (P & R):** The fidelity of generative models can be evaluated on precision which measures how much generated distributions are involved in true distributions. Likewise, the diversity can be realized by recall which measures how much true distributions are involved in generated distributions [12]. 

Kynkäänniemi have proposed improved P & R that count the presence of samples on the overlapped data manifold constructed by KNN [27]. In the case of precision, the data manifold is constructed from multiple spheres whose center is determined by true samples and whose radius is the distance between the true samples and their k- th nearest neighbors. All operations in the P & R should be conducted on latent space, so we use simple CNN networks initialized randomly for embedding [11]. For both P metrics from 10 different networks. To avoid extensive & R, we fix computation of the KNN, we use 10,000 samples for each 𝑘𝑘 of the KNN to 5 and get the average of the network. 

**Density and Coverage (D & C):** P & R are vulnerable to outliers overestimating data manifold. To remedy this, [11] have counted the average number of overlapped samples on a sphere. The concept and process of D & C are similar with P & R, except that the density can be greater than 1. 

## **5. EXPERIMENTS** 

We evaluate our model by comparing it to 1) _training set_ , 2) _CNN-VAE_ similar structure with our VQ-VAE, 3) _Music Transformer_ [3], and 4) _MuseGAN_ [22]. All models have generated loop samples as many as the training set. Additionally, we apply several sampling methods for the VQ-VAE+LSTM and compare them. The experiment details of the baselines are explained in Appendix A. 

## **5.1 Quantitative Evaluation Results** 

## **4.3 Similarity Metrics** 

Evaluating generated music samples on data space considers only musical features that humans can perceive. Here, we measure similarity of true and generated samples on 

## _5.1.1 Model Metric Results_ 

Due to the finite latent codes, our VQ-VAE is a little worse than the CNN-VAE for the reconstruction task (Table 1). 

407 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
MuseGAN 0.96 22<br>0.675 3 14.4<br>— VQ-VAE+LSTM 0.94<br>0.650<br>45 1 0.92 14.3<br>0.625<br>0.90<br>Recall 0.600 3 Density 14.2 54<br>0.575 0.88<br>0.550 Coverage Note  14.1 3<br>0.86<br>0.525<br>0.84 14.0<br>0.500 0.65 0.70 0.75 0.80 0.85 0.90 0.8 1.0 1.2 1.4 1.6 1.8 2.0 5.1 5.2 5.3 5.4 5.5 5.6 5.7 5.8<br>Precision Density Unique Pitch<br><!-- End of picture text -->

**Figure 4.** Rejection sampling results for the MuseGAN and VQ-VAE+LSTM. Each numbering markers indicates the various rejection rates (getting stricter from 1 to 5). The rates correspond to {no apply, 1, 0.1, 0.01, 0.001}. 



<!-- Start of picture text -->
Training Set<br>VQ-VAE+LSTM ▲<br>Groups<br>MuseGAN<br>1.0 1.5 2.0 2.5 3.0 3.5 4.0 4.5 5.0<br>Ratings<br><!-- End of picture text -->

**Figure 5.** Human listening test. Green lines in the boxes indicate median values and red triangles for mean values. As referred in [7], we have observed that 𝛽𝛽 in the VQ- _5.1.2 Musical Metric Results_ VAE objectives did not affect much to the task (𝛽𝛽= 0.25). 

Our proposed model achieves the highest performance in terms of LS and ND (Table 2). The reason for poor performance in UP may be related to the VQ-VAE’s reconstruction performance. Nevertheless, they can generate highly structural and rhythmic samples in a holistic view. Note that the Music Transformer fails to preserve the loop properties in its generated samples. 

## _5.1.3 Similarity Metric Results_ 

Except for the recall, our model achieves much better scores in terms of precision, density and coverage (Table 2). In MuseGAN, the recall may be overestimated by generated outliers. Depending on sampling methods and their parameters for full sampling mode, we can observe that there is a trade-off between fidelity and diversity. Even with the random embeddings, the all metrics show consistent performance (low standard deviations). A comprehensive evaluation (F1 score) can be found in Table 3. 

## **5.2 Rejection Sampling** 

It is promising that the loop detector can be used to control the trade-off between fidelity and diversity of generative models. This concept, rejection sampling, is to reject generated samples which do not meet our conditions. (loop scores in this context) [8]. If setting the rejection rate strictly, we can obtain music samples which are closer to the loop. For the experiments, we choose high-scored models that are MuseGAN and VQ-VAE+LSTM with top- 

k sampling. Figure 4 shows the P & R, D & C, and UP & ND results for various rejection rates. In P & R, the two models show similar trends while applying more strict rejection rates, but opposite trends for other metrics. Contrary to our assumption, both D & C of MuseGAN increase as we apply the stricter loop detector. It rather disproves that MuseGAN produces many outliers, so the loop detector may help to increase sample diversity close to the true distribution. In terms of ND, both models indicate minimal effect with the rejection sampling. However, they show contradiction about the aspect of UP changes. 

## **5.3 Human Listening Test** 

We conduct a listening test for 20 people. We select the training set as a baseline and compare loop samples from two generative models (MuseGAN and VQ-VAE+LSTM with top-k sampling). Participants are asked to listen 10 samples for each group (total 30 samples) and evaluate how much the sample sounds like the loop music (which can be repeated seamlessly) on a Likert scale. 

As Figure 5, the training set group achieves the highest ratings with an average rating of 3.885 (±1.045). For the generative models, VQ-VAE+LSTM achieves the highest average rating 3.585 (±1.141). It seems that the participants have felt them closer to the real music since loops from discrete representations are repetitive and structural (MuseGAN 3.060 (±1.172)). Additionally, we carry out Kruskal-Wallis H test which is non-parametric one-way ANOVA. The test shows a statistically significant difference among the test groups with **6. CONCLUSION** 𝐻𝐻= 49.811, 𝑝𝑝< 0.001. 

We leverage recurring nature of music by adopting the concept of the loop. To fulfill our objective, we address two processes; _loop extraction_ and _loop generation_ . First, we design a loop detector trained by a loop audio dataset to prepare loops from MIDI. Second, we adopt the twostage generative approach, compressing data into discrete representations and designing an autoregressive model. Even without pre-trained feature extractors, we can evaluate our generative models on measuring fidelity and diversity. It is observed that our model outperforms well-known generative model for loop generation. 

408 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

## **7. REFERENCES** 

- [1] Yi Ren, Jinzheng He, Xu Tan, Tao Qin, Zhou Zhao, and Tie-Yan Liu, "PopMAG: Pop Music Accompaniment Generation,” in _Proc. of the 28th ACM International Conference on Multimedia_ , 2020, pp. 1198– 1206. 

- [2] Yu-Siang Huang and Yi-Hsuan Yang, "Pop Music Transformer: Beat-based Modeling and Generation of Expressive Pop Piano Compositions," in _Proc. of the 28th ACM International Conference on Multimedia_ , 2020, pp. 1180–1188. 

- [3] Cheng-Zhi Anna Huang, Ashish Vaswani, Jakob Uszkoreit, Noam Shazeer, Ian Simon, Curtis Hawthorne, Andrew M. Dai, Matthew D. Hoffman, Monica Dinculescu, and Douglas Eck, “Music Transformer,” _arXiv preprint arXiv:1809.04281_ , 2018. 

- [4] Christine Payne, “MuseNet,” _OpenAI_ , openai.com/blog/musenet, 2019. 

- [5] Bee Suan Ong, and Sebastian Streich, “Music Loop Extraction from Digital Audio Signals,” in _Proc. of the 2008 IEEE International Conference on Multimedia and Expo_ , IEEE, 2008, pp. 681–684. 

- [6] Zhengshan Shi, and Gautham J. Mysore, “LoopMaker: Automatic Creation of Music Loops from Pre-recorded Music,” in _Proc. of the 2018 CHI Conference on Human Factors in Computing Systems_ , 2018, pp. 1–6. 

- [7] Aaron Van Den Oord, Oriol Vinyals, and Koray Kavukcuoglu, “Neural Discrete Representation Learning,” in _Advances in Neural Information Processing Systems_ , 2017, pp. 6306–6315. 

- [8] Ali Razavi, Aaron Van den Oord, and Oriol Vinyals, “Generating Diverse High-Fidelity Images with VQVAE-2,” in _Advances in Neural Information Processing Systems_ , 2019, pp. 7989–7999. 

- [9] Tim Salimans, Ian Goodfellow, Wojciech Zaremba, Vicki Cheung, Alec Radford, and Xi Chen, "Improved Techniques for Training GANs," in _Advances in Neural Information Processing Systems_ , 2016, pp. 2234–2242. 

- [10] Martin Heusel, Hubert Ramsauer, Thomas Unterthiner, Bernhard Nessler, and Sepp Hochreiter, "GANs Trained by a Two Time-Scale Update Rule Converge to a Local Nash Equilibrium," in _Advances in Neural Information Processing Systems_ , 2017, pp. 6626–6637. 

- [11] Muhammad Ferjad Naeem, Seong Joon Oh, Youngjung Uh, Yunjey Choi, and Jaejun Yoo, “Reliable Fidelity and Diversity Metrics for Generative Models,” in _Proc. of the 37th International Conference on Machine Learning_ , PMLR, 2020, pp. 7176–7185. 

- [12] Mehdi S. M. Sajjadi, Olivier Bachem, Mario Lucic, Olivier Bousquet, and Sylvain Gelly, “Assessing 

Generative Models via Precision and Recall,” in _Advances in Neural Information Processing Systems_ , 2018, pp. 5228–5237. 

- [13] Adam Roberts, Jesse Engel, Colin Raffel, Curtis Hawthorne, and Douglas Eck, “A Hierarchical Latent Vector Model for Learning Long-Term Structure in Music,” in _Proc. of the 35th International Conference on Machine Learning_ , PMLR, 2018, pp. 4364– 4373. 

- [14] Gautam Mittal, Jesse Engel, Curtis Hawthorne, and Ian Simon, “Symbolic Music Generation with Diffusion Models," _Proc. of the 22nd International Society for Music Information Retrieval Conference_ , 2021, pp. 468–475. 

- [15] François Pachet, Alexandre Papadopoulos, and Pierre Roy, "Sampling Variations of Sequences for Structured Music Generation," in _Proc. of the 18th International Society for Music Information Retrieval Conference_ , 2017, pp. 167–173. 

- [16] Rewon Child, Scott Gray, Alec Radford, and Ilya Sutskever, "Generating Long Sequences with Sparse Transformers," _arXiv preprint arXiv:1904.10509_ , 2019. 

- [17] Jonathan Foote, “Automatic Audio Segmentation using a Measure of Audio Novelty," in _Proc. of the IEEE International Conference on Multimedia and Expo_ , IEEE, 2000, pp. 452–455. 

- [18] Joan Serra, Meinard Müller, Peter Grosche, and Josep Lluis Arcos, "Unsupervised Detection of Music Boundaries by Time Series Structure Features,” in _Proc. of the AAAI Conference on Artificial Intelligence_ , 2012, pp. 1613–1619. 

- [19] Tun-Min Hung, Bo-Yu Chen, Yen-Tung Yeh, and Yi-Hsuan Yang, “A Benchmarking Initiative for Audio-Domain Music Generation Using the Freesound Loop Dataset,” in _Proc. of the 22nd International Society for Music Information Retrieval Conference_ , 2021, pp 310–317. 

- [20] Colin Raffel, “Learning-based Methods for Comparing Sequences, with Applications to Audio-to-MIDI Alignment and Matching,” Ph.D. dissertation, Columbia University, 2016. 

- [21] Shulei Ji, Jing Luo, and Xinyu Yang, “A Comprehensive Survey on Deep Music Generation: Multi-level Representations, Algorithms, Evaluations, and Future Directions,” _arXiv preprint arXiv:2011.06801_ , 2020. 

- [22] Hao-Wen Dong, Wen-Yi Hsiao, Li-Chia Yang, and Yi-Hsuan Yang, “MuseGAN: Multi-track Sequential Generative Adversarial Networks for Symbolic Music Generation and Accompaniment,” in _Proc. of the AAAI Conference on Artificial Intelligence_ , 2018, pp. 34–41. 

409 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

- [23] Diederik P. Kingma, and Max Welling, “Auto-Encoding Variational Bayes,” _arXiv preprint arXiv:1312.6114_ , 2013. 

- [24] Aditya Ramesh, Mikhail Pavlov, Gabriel Goh, Scott Gray, Chelsea Voss, Alec Radford, Mark Chen, and Ilya Sutskever, "Zero-Shot Text-to-Image Generation," in _Proc. of the 38th International Conference on Machine Learning_ , PMLR, 2021, pp. 8821–8831. 

- [25] Jacob Walker, Ali Razavi, and Aäron van den Oord, "Predicting Video with VQVAE," _arXiv preprint arXiv:2103.01950_ , 2021. 

- [26] Kristy Choi, Curtis Hawthorne, Ian Simon, Monica Dinculescu, and Jesse Engel, “Encoding Musical Style with Transformer Autoencoders,” in _Proc. Of the 37th International Conference on Machine Learning_ , PMLR, 2020, pp. 1899–1908. 

- [27] Tuomas Kynkäänniemi, Tero Karras, Samuli Laine, Jaakko Lehtinen, and Timo Aila, “Improved Precision and Recall Metric for Assessing Generative Models,” in _Advances in Neural Information Processing Systems_ , 2019, pp. 3927–3936. 

- [28] Colin Raffel and Daniel PW Ellis, “Intuitive Analysis, Creation and Manipulation of MIDI Data with pretty_midi,” in _Proc. of the 15th International Society for Music Information Retrieval Conference Late Breaking and Demo Papers_ , 2014. 

- [29] Hao-Wen Dong, Wen-Yi Hsiao, and Yi-Hsuan Yang, “Pypianoroll: Open Source Python Package for Handling Multitrack Pianoroll,” in _Proc. of the 19th International Society for Music Information Retrieval Conference Late Breaking and Demo Papers_ , 2018. 

- [30] Lukas Ruff, Robert A. Vandermeulen, Nico Goernitz, Lucas Deecke, Shoaib A. Siddiqui, Alexander Binder, Emmanuel Müller, and Marius Kloft, “Deep One-Class Classification,” in _Proc. of the 35th International Conference on Machine Learning_ , PMLR, 2018, pp. 4393–4402. 

- [31] Ilya Loshchilov and Frank Hutter, “Decoupled Weight Decay Regularization,” _arXiv preprint arXiv:1711.05101_ , 2017. 

- [32] Prafulla Dhariwal, Heewoo Jun, Christine Payne, Jong Wook Kim, Alec Radford, and Ilya Sutskever, “Jukebox: A Generative Model for Music _,_ ” _arXiv preprint arXiv:2005.00341_ , 2020. 

- [33] Angela Fan, Mike Lewis, and Yann Dauphin, “Hierarchical Neural Story Generation,” _arXiv preprint arXiv:1805.04833_ , 2018. 

- [34] Ari Holtzman, Jan Buys, Li Du, Maxwell Forbes, and Yejin Choi, “The Curious Case of Neural Text Degeneration,” _arXiv preprint arXiv:1904.09751_ , 2019. 

410 

