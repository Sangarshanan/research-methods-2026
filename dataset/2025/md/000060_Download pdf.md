---
paper_id: "000060"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706500/files/000060.pdf"
---

# VIDEO-GUIDED TEXT-TO-MUSIC GENERATION USING PUBLIC DOMAIN MOVIE COLLECTIONS 

Haven Kim<sup>1</sup> 

Zachary Novack<sup>1</sup> Weihan Xu<sup>2</sup> Julian McAuley<sup>1</sup> Hao-Wen Dong<sup>3</sup> 

1 University of California San Diego 

2 Duke University 

3 University of Michigan 

## ABSTRACT 

Despite recent advancements in music generation systems, their application in film production remains limited, as they struggle to capture the nuances of real-world filmmaking, where filmmakers consider multiple factors—such as visual content, dialogue, and emotional tone—when selecting or composing music for a scene. This limitation primarily stems from the absence of comprehensive datasets that integrate these elements. To address this gap, we introduce Open Screen Soundtrack Library (OSSL), a dataset consisting of movie clips from public domain films, totaling approximately 36.5 hours, paired with high-quality soundtracks and human-annotated mood information. To demonstrate the effectiveness of our dataset in improving the performance of pre-trained models on film music generation tasks, we introduce a new video adapter that enhances an autoregressive transformer-based text-to-music model by adding video-based conditioning. Our experimental results demonstrate that our proposed approach effectively enhances MusicGen-Medium in terms of both objective measures of distributional and paired fidelity, and subjective compatibility in mood and genre. To facilitate reproducibility and foster future work, we publicly release the dataset, code, and demo<sup>1</sup> . 

## 1. INTRODUCTION 

Music plays a crucial role in films, shaping its artistic quality and influencing its commercial success [1]. A wellcomposed soundtrack enhances the emotional depth of a scene, guiding audience perception and engagement [2–5]. Despite recent advancements in music generation systems, significant challenges remain in adapting these technologies for film production, as these systems are not designed to 

> 1 Dataset: `https://havenpersona.github.io/ossl-v1` Code: `https://github.com/havenpersona/ossl-v1` Demo: `https://havenpersona.github.io/demo/ismir2025` 

© Haven Kim, Zachary Novack, Weihan Xu, Julian McAuley, and Hao-Wen Dong. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: Haven Kim, Zachary Novack, Weihan Xu, Julian McAuley, and Hao-Wen Dong, “Video-Guided Text-to-Music Generation Using Public Domain Movie Collections”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

align with the real-world practices of film music composition, where multiple elements—such as visual content, dialogue, and emotional tone—are considered altogether [6]. 

A major obstacle is the lack of comprehensive datasets containing movie clips paired with their corresponding soundtracks. While some existing film datasets are derived from commercial movies, many are no longer available for download [7–9], and some provide only video embeddings rather than raw movie clips [10], making it challenging to distinguish segments containing music from those that do not. The remaining datasets do not include isolated soundtrack stems [11–14]. While we acknowledge the possibility of constructing a dataset using source-separated music, as done in previous approaches [15], we find the quality of source-separated music to be suboptimal, as it occasionally includes incorrect audio such as voice or sound effects, making it unsuitable for our use case. 

Another missing element that plays a pivotal role in making film music is mood information, as dialogues and scenes alone are often insufficient to fully convey emotions, which explains why scripts typically include not only dialogues but also separate mood descriptions. However, we find that this aspect remains largely unaddressed in existing resources, with no publicly available film datasets annotated with mood information. 

To bridge this gap, we introduce the Open Screen Soundtrack Library (OSSL), a dataset comprising approximately 36.5 hours of movie clips from public domain films, each paired with their corresponding soundtracks and mood annotations. The dataset is created by automatically identifying timestamps of musical segments within the films, mapping these segments to the soundtracks, and then verifying the mappings manually. To demonstrate the effectiveness of this dataset for enhancing music generation for movie clips, we incorporate a video adapter into a text-to-music generation model (MusicGen) [16] and finetune it on our dataset. We evaluate our models on both public domain films and commercial films, which we call OSSL Evaluation Set - Public and Commercial (OES-Pub and OES-Com), respectively, in order to ensure that our approach can handle various kinds of data. Our objective and subjective evaluations demonstrate that we successfully extend a text-to-music generation model, MusicGen-Medium, to handle both textual and video inputs for enhanced film music generation. 

518 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

For reproducibility and accessibility, we publicly release our main dataset, OSSL, as well as the evaluation sets, OES-Pub and OES-Com. 

## 2. RELATED WORK 

Audio-Domain Music Generation. Contemporary music generation architectures in the audio domain predominantly follow two distinct paradigms. The first employs neural codecs to transform digital audio signals into discrete tokens, enabling transformer-based models [17] to generate music by learning token distributions from prompts such as text [16, 18, 19] or video [20–22]. The second paradigm leverages diffusion-based frameworks, where diffusion models are trained to generate audio signals, conditioned on prompts such as textual descriptions [23–29] or video frames [30, 31]. Our models are built upon MusicGen [16], a text-to-music generation framework based on the former approach. 

Multimodal Music Generation. Most existing audiodomain music generation models support purely unimodal conditions, such as text [18, 29], or have limited multimodal support for text along with audio [16, 18, 32] or abstract musical signals [33–35]. In constrast, work on conditioning on visual signals is more limited. One example is a transformer-based model conditioned on text, speech, images, and videos, which generates discrete music tokens that are later converted into raw waveforms from embeddings obtained from pre-trained speech, image, and video encoders [36]. An alternative approach involves converting visual inputs into detailed textual descriptions, and feeding them into a model. This enables the use of diverse modalities, including text, videos, and images as inputs [37]. Another recent study trained a video-to-music generation model on a diverse set of video features, while integrating textual conditioning to enable high-level control through textual embeddings derived from a pre-trained text encoder [21]. On the other hand, our approach focuses on integrating a video adapter into a pre-trained text-to-music generation model in order to build a music generation model conditioned on multimodal inputs. 

Video-Conditioned Music Generation. One of the earliest contributions to video-to-music generation utilized human pose features extracted by pre-trained models, in order to generate plausible music for video clips containing individuals playing musical instruments [38]. In contrast, another early study employed self-defined handcrafted features to capture relevant video attributes [39]. More recently, the field has shifted toward leveraging embeddings derived from pre-trained video encoders [20–22,40], both in the audio and symbolic domain. This approach has been integrated into our models, enabling them to perform crossattention on embeddings derived from a pre-trained video encoder designed to capture both spatial and temporal video information [41]. 

Adapter Mechanisms. Adapter mechanisms, which integrate compact and trainable modules into pre-trained models, were originally introduced to enhance transfer learning 

|Dataset|Audio|MIDI|Self-<br>Hosted|Mood|Video<br>Content|Length<br>(Hours)|
|---|---|---|---|---|---|---|
|HIMV-200K [48]|✓|✗|✗|✗|Music Video,<br>User-Generated Video|-|
|URMP [49]|✓|✓|✗|✗|Music Performance|33.5|
|TikTok [50]|✓<br>|✗|✗<br>|✗|Dance Video|1.5|
|AIST++ [51]|✓|✗|✓|✗|3D Dance Motion|5.2|
|SymMV [52]|✓|✓|✗|✗|Music Video|76.5|
|MuVi-Sync [53]|✓|✓|✗|✗|Music Video|-|
|BGM909 [54]|✓|✓|✗|✗|Music Video|-|
|NES-VMDB [55]|✗|✓|✗|✗|Gameplay Video|474.0|
|OSSL (Ours)|✓|✗|✓|✓|Films|36.5|



Table 1: Comparison of video-music datasets available as of June 2025. The proposed OSSL dataset is the first self-hosted video-music dataset (i.e., without requiring separate download procedures via YouTube URLs or sharing requests) which includes mood annotations. 

efficiency in natural language processing (NLP) [42]. This approach is commonly employed to adapt pre-trained backbone models for various tasks [43,44]. 

Our work is particularly inspired by methods that modify pre-trained models to accommodate external conditions with new modalities. Notably, prior research has demonstrated the effectiveness of lightweight adapters in incorporating image prompts into text-to-image diffusion models [45, 46]. Building on this idea, subsequent work has extended the approach by using adapters to integrate audio prompts into diffusion-based text-to-music generation models [47]. On the other hand, our approach attempts to integrate video prompts into autoregressive transformerrbased text-to-music generation models. 

## 3. DATASET CONSTRUCTION 

## 3.1 Open Screen Soundtrack Library (OSSL) 

We introduce the Open Screen Soundtrack Library (OSSL), a collection of movie clips with their corresponding soundtracks and associated metadata, including mood annotations. We provide an overview of the comparison of video-music datasets in Table 1 and an illustration of our dataset construction methodology in Figure 1. 

Data Collection. We compile a list of public domain films along with metadata (e.g., title, release date, and genres) and obtain complete versions from YouTube. To achieve the highest music quality by obtaining soundtrack stems without unnecessary noise, we download soundtracks, instead of source-separated music, for each film from YouTube, guided by IMDB<sup>2</sup> metadata. The frame rate and resolution for each video are 25fps and 960x720, respectively, and the sampling rate for each soundtrack is 44.1kHz. 

Musical Segment Identification. To identify the timestamps of segments with soundtracks within the films, we employ a pre-trained source separation model [56] trained to decompose movie audio into three components: music, effect, and dialogue. After source separation, we apply a silence detection algorithm to music parts using `pyAudioAnalysis` [57], with a frame length and step size of 20ms and a threshold scaling factor of 0.2. We define a 

> 2 An online database on films. `https://www.imdb.com` 

519 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
DATA COLLECTION SOURCE SEPARATION SILENCE DETECTION<br>MOVIE MUSIC<br>EFFECT<br>DIALOGUE<br>十  CLIP 1 CLIP 2 CLIPn<br>SOUNDTRACKS<br>MAIN TITLE<br>2:40 EVENT DETECTION<br>CLIP1<br>1:06 CHROMA<br>Lovers Quarrel1:12 CALCULATIONDISTANCE m<br>Eddie's Bar<br>2:23<br>p=0.4 p=0.01 p=0.39<br>CLIPn<br><!-- End of picture text -->

Figure 1: Illustration of our methodology for constructing the OSSL dataset. We collect publicly available movies and their soundtracks. We separate movie audio into music and other elements, and extract music using a silence detection algorithm. An event detection algorithm ensures the extracted audio is truly music. We then calculate chroma distance to match clips with their corresponding soundtracks, assigning the closest match. Human inspection verifies these mappings. 



<!-- Start of picture text -->
80<br>70<br>60<br>50<br>Count40<br>30<br>20<br>10<br>0 _<br>1910 1920 1930 1940 1950 1970 080 1990 2000 2010<br><!-- End of picture text -->

Figure 2: Distribution of release years for the OSSL dataset 

segment as a clip if it is longer than 10 seconds and contains no silence longer than 1 second. 

Following this, we verify the presence of musical content using an event detection algorithm [58], as the extracted soundtrack may contain non-musical elements owing to the limitations of current source separation models. Specifically, we apply the event detection algorithm to each clip and retain only those where the average probability of containing a musical event exceeds 0.3. (This threshold value is determined empirically by testing different values across multiple samples.) 

Movie Clips-Soundtracks Mapping. Because a movie typically contains multiple soundtracks, it was essential to determine which soundtrack each movie clip corresponds to. The most effective method we found is using chroma similarity<sup>3</sup> . Specifically, we compare the chroma features of source-separated soundtracks from movie clips with those of each soundtrack in the film, assigning clips to the soundtrack with the minimum chroma distance. 

Manual Quality Inspection. The resulting movie clips are manually assessed by human evaluators, and any clips with incorrect mappings (i.e., when a clip is paired to a 

> 3 We attempted a fingerprinting approach (https://github.com/worldveil/dejavu) to test mapping 20 clips from the movie “D.O.A” against 24 soundtracks. However, this method produced inaccurate mappings in most instances, achieving only one correct identification out of 20 samples—a failure rate of 95%. Our chroma similarity approach, on the other hand, accurately mapped 17 clips to their corresponding soundtracks, yielding a success rate of 85%. 

|Attributes|OSSL|OES-Pub|OES-Com|
|---|---|---|---|
|Number of samples|736|100|100|
|Number of unique films|299|76|37|
|Average clip duration|178.47 sec|30 sec|30 sec|
|Total duration|36.49 hours|0.83 hours|0.83 hours|



Table 2: Statistical overview of OSSL, OES-Pub, and OESCom 

wrong soundtrack) are excluded from our dataset. 

Mood Annotation. The final stage of our dataset construction involves annotating mood information for each movie clip. We classify mood into four categories based on a previously suggested taxonomy—Russell’s 4Q, where the four classes are one of the HVHA (high valence, high arousal), HVLA (high valence, low arousal, LVHA (low valence, high arousal), and LVLA (low valence, low arousal) [59,60]. 

We employ two human annotators. We first provide them with a brief explanation of the concepts of valence and arousal in the context of music and then ask them to independently annotate the movie clips using the four mood categories. In the majority of cases (89.9% of samples), both annotators assign the same label to a movie clip. When agreement occurs, we retain the assigned annotation. If they disagree, they discuss their choices until they reach a consensus. As a result, we obtain 276 movie clips classified as happy, 30 as sad, 315 as nervous, and 115 as peaceful. 

## 3.2 OSSL Evaluation Set (OES) 

We evaluate our models on two distinct datasets: OSSL Evaluation Set-Public (OES-Pub), comprising of movie clips from public domain films that are not included in OSSL, and OSSL Evaluation Set-Commercial (OES-Com), consisting of commercial films. The evaluation on OES-Pub serves to confirm that our models have effectively learned to generalize from this data distribution. On the other hand, the evaluation on OES-Com shows whether these models can generalize to contemporary commercial films. Notably, OES-Com incorporates a large proportion (89%) of clips 

520 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
Music Token<br>Multi-Head AttentionVideo Adapted ProbabilitiesSoftmax<br>Linear<br>CROSS CROSS Add & Norm<br>ATTENTION ATTENTION<br>Feed<br>a Forward<br>Linear Add & Norm<br>Transformation Video-Adapted<br>Multi-Head<br>Attention<br>ViViT MusicGen Add & NormMasked<br>Encoder Encoder Multi-Head<br>Attention<br>A film soundtrack for a<br> happy scene. An orchestral:<br>pei g g ns<br>and cellos. Music Token<br>Video Clip Text (Converted from Encodec)<br>TRAINABLEFROZEN<br><!-- End of picture text -->

Figure 3: Extending MusicGen: We introduce a video adapter, which applies cross-attention to linearly transformed video embeddings, scaled by α, and integrates it into the original cross-attention mechanism. A fire icon denotes trainable components, while a snowflake icon indicates frozen components. 

from films released within the past year. Finally, we annotate each movie clip with mood information in the same way as we did for constructing OSSL ( `[MOOD]` ). 

Finally, we present detailed statistical information for OSSL, OES-Pub, and OES-Com in Table 2. 

## 4. MODEL ARCHITECTURE 

In this section, we present our methodology for integrating a video adapter into an existing text-to-music generation model, MusicGen [16], along with its illustration in Figure 3. 

MusicGen [16] is an autoregressive transformer [17]based model that generates discrete tokens which are subsequently converted into audio signals by a neural codec [61] from textual prompts. Each attention head in the original model’s cross attention modules is initially defined as: 



<!-- Start of picture text -->
headi = Attention(xWi (q) , z t Wi (k) , z t Wi (v) ) (1)<br><!-- End of picture text -->

In this formulation, x represents the decoder’s current hidden states, z<sup>t</sup> means the text encoder’s output, and i is the index of an attention head. 

To implement our video adapter, we leverage a pretrained video encoder. Specifically, we choose the ViViT<sup>4</sup> [41] , a transformer-based video understanding model pretrained on a large-scale dataset [62], which provides a strong foundation for our task of film video understanding. We first obtain the video embeddings (zv ∈ R<sup>n</sup> ) using it. Subsequently, we apply an affine linear transformation X ∈ R<sup>m×n</sup> to adjust the dimension of video embeddings from the model’s original dimension n to the dimension that is compatible with our text embeddings m ( ˜zv = X ∗ zv). 

We modify the cross-attention layer, which originally processes single modalities, to incorporate video embeddings, thereby enabling the model to attend to multimodal 

> 4 `google/vivit-b-16x2-kinetics400` 

contexts. Specifically, we augment the original crossattention mechanism with a video-conditioned component, where each attention head computes its output by leveraging both text and video modalities. 



<!-- Start of picture text -->
headi = Attention(xWi (q) , ztWi (k) , ztWi (v) )<br>(2)<br>+α × Attention(xW ˜ i(q), z˜vW˜ i(k), z˜vW˜ i(v))<br><!-- End of picture text -->

where x represents the decoder’s current hidden states, z˜v represents the video embeddings with adjusted dimensions, and α is a trainable parameter. 

During training, only the newly introduced parameters W˜ i(q), W˜ i(k), W˜ i(v), α, and X are optimized after random initialization, while all other components of the model remain frozen. 

## 5. EXPERIMENTAL SETTING 

## 5.1 Comparison Models 

We fine-tune MusicGen-Small and MusicGen-Medium with video adapters,<sup>5</sup> as described in the previous section. Here, S-MULTI and M-MULTI denote these models, where “S” and “M” stand for “Small” and “Medium,” respectively. 

As baselines, we use the original MusicGen-Small and MusicGen-Medium models, which generate results solely based on text prompts. We denote these models as S-BASE and M-BASE, respectively. 

To assess the effectiveness of video adapters, we also compare them against models fine-tuned on our dataset using only textual prompts (i.e., without video adapters). These models are denoted as S-TEXT and M-TEXT. Unlike S-MULTI and M-MULTI, where existing parameters are frozen and new parameters are trained, S-TEXT and M- TEXT do not incorporate new parameters. Instead, we apply Low-Rank Adaptation [63] when fine-tuning these models. 

## 5.2 Dataset Preprocessing 

Since the default maximum length of MusicGen is 30 seconds, we train our models to generate only the first 30 seconds of music for the first 30 seconds of each video clip. This is because we detected the start time of each segment, so it prevents generating from the middle of a track. Because MusicGen produces raw audio at a sampling rate of 32,000 Hz, all soundtracks are resampled to this rate before training. Additionally, we normalize all soundtracks so that their maximum amplitude is always one. 

## 5.3 Text Prompts Design 

Prompts have been suggested to be a significant factor influencing the outcomes of generative models [64–66]. In our experiments, text prompts serve not only as primary information for fine-tuning text-based models (S-TEXT and M-TEXT) but also as a basis for inference in baseline models (S-BASE and M-BASE). To ensure a fair comparison, therefore, we carefully design them to fully leverage the capabilities of text-to-music generation models,. 

> 5 Due to computational constraints, we did not conduct experiments on MusicGen-Large. 

521 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

We experiment with three types of textual information: (1) mood annotations from our dataset, (2) movie genre labels (e.g., thriller, romance), and (3) LLM-generated music descriptions obtained using an open-source music captioning model [67]. We observe that while both mood annotations and LLM-generated music captions subjectively improve generation quality, adding genre information often has a negative impact. For instance, when using the prompt, “A film soundtrack for a peaceful scene in a thriller movie,” our baseline models, S-BASE and M-BASE, overemphasizes the keyword “thriller,” producing music unsuitable for peaceful scenes. As a result, our final structured template includes only mood information and LLM-generated music captions: “A film soundtrack for a `[MOOD]` scene. `[CAPTION]` .” Here, `[MOOD]` is a natural language description of our Russell’s Q4-based mood annotation, which is one of happy (high valence, high arousal), sad (low valence, low arousal), nervous (low valence, high arousal), or peaceful (high valence, low arousal). To generate music captions ( `[CAPTION]` ), we extract the first 30 seconds of each soundtrack in our dataset, divide it into three 10-second segments, and generate a caption for each using a music captioning model [67], as we recognize that film music evolves over time. We then use a commercial LLM, specifically Claude 3.5 Sonnet, to summarize these captions with the prompt: “Summarize the description of each song in one sentence from 0 to 30 seconds.” Consequently, the resulting captions concisely describe how the music changes over time, providing a brief musical summary (e.g., ‘The piece transitions from cembalo to marimba, concluding with a Tibetan singing bowl and animal sounds’). 

When designing text prompts for OES-Pub and OES-Com, we use source-separated music to generate `[CAPTION]` , unlike OSSL, which features original soundtrack stems. This results in the music captioning model frequently describing the audio as having poor recording quality. To mitigate this, we explicitly instruct Claude 3.5 Sonnet to exclude any mention of audio quality when summarizing the captions for OES-Pub and OES-Com. 

## 5.4 Training Details 

Our models are trained using the AdamW optimizer [68] (β1 = 0.9, β2 = 0.999) with a weight decay of 1 × 10<sup>−2</sup> . The initial learning rate is set to 1 × 10<sup>−4</sup> and scheduled using a cosine annealing strategy [69] with a linear warm-up phase. The OSSL dataset is split into training and validation sets in a 9:1 ratio. To prevent overfitting, we stop training a model when the model does not improve for three epochs during the validation stage. Due to computational constraints, the batch size is set to 1. Training is conducted on a single NVIDIA A6000 GPU. 

## 5.5 Objective Evaluation Metrics 

Distributional Fidelity. As common in most audiodomain TTM research [70, 71], we assess the quality of our outputs at the distributional level by comparing generations from our model against a high-quality reference set, here comprised of 5K commercial soundtracks. To do so, 

we first extract embedding from our generated audio for each method and the reference set using CLAP [72]. With these embeddings, we then compute Frechet Audio Distance (FAD) [73] and Precision [74] for this purpose. FAD compares distributional distance by fitting a high dimensional Gaussian to each dataset and measuring the Frechét distance between them, while Precision uses a k-NN estimate of the reference set’s distribution and measures how many generated samples lie in the estimated manifold. 

Paired Fidelity. As our evaluation sets, OES-Pub and OES-Com, also contain paired video-music data in the form of source-separated musical tracks from each movie clip, we are also able to directly assess how well our models recreate the reference music on a paired sample-by-sample basis. Specifically, here we measure the CLAP Audio Similarity and Kullback-Leibler (KL) Divergence between the generated music and the reference music for this purpose. The CLAP Audio Similarity is calculated as a cosine similarity between the CLAP embeddings of the generated and reference samples for each video clip. The KL divergence is calculated using the estimated distributions the generated and reference samples with the PaSST audio classifier [75]. 

Sample Diversity. To evaluate the diversity of the generated samples, we employ Recall [74], following prior work in music generation [70,71]. Using the same embedding model (CLAP) and reference/generated datasets from Distributional Fidelity, we use a k-NN estimate of each generated distribution and calculate the fraction of real samples that lie in the generated manifold. 

## 5.6 Subjective Survey 

To subjectively evaluate our models, we first select 10 representative samples from our evaluation set, OES-Com. Specifically, the OES-Com is divided into 10 clusters using k-means clustering, based on the CLAP embeddings of source-separated music, and we select the sample closest to the centroid of each cluster. Using these 10 samples, we design a survey in the form of a website and distribute it within our social network, recruiting 15 participants. 

The survey procedure is structured as follows: Each participant is randomly assigned 2 out of the 10 samples. First, participants are required to watch the original version of the first movie clip. This step serves two purposes: to familiarize them with the atmosphere of the clip and to standardize the experience for participants regardless of prior exposure to the movie. After viewing the original clip, participants rate the inference results of each model (S-BASE, S-TEXT, S-MULTI, M-BASE, M-TEXT, and M-MULTI) for the corresponding clip, with the presentation order of the models randomized by the website. Subsequently, participants repeat the process for the second assigned movie clip, watching its original version and rating the inference results of each model, with the randomized order. 

The evaluation assesses each model across three dimensions—genre, mood, and audio quality—using a 10-point Likert scale. For genre, participants rate how cinematic the AI-generated music sounds (1: not cinematic at all, 10: very cinematic). For mood, participants evaluate the compatibil- 

522 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

||OSSL|Video<br>|||||Object|ive||||||Subjective||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||Fine-|Adapter<br>Inte-|Di|stributio|nal Fideli|ty||Paired Fi|delity||Div|ersity|H|uman Ratings||
||tuned|grated|FA|D↓|Precis|ion↑|Simil|arity↑|KL|↓|Rec|all↑|Mood↑|Genre↑|Quality↑|
||||pub|com|pub|com|pub|com|pub|com|pub|com|avg±CI|avg±CI|avg±CI|
|S-BASE|✗|✗|64.91|77.99|22.00|14.00|41.55|34.77|1.20|1.93|4.78|6.20|4.53±0.91|5.27±1.04|5.67±0.99|
|S-TEXT|✓|✗|61.98|75.75|20.00|14.00|42.44|34.81|1.13|1.97|9.90|19.00|5.77±1.73|6.00±1.11|6.20±0.76|
|S-MULTI|✓|✓|64.39|75.59|16.00|14.00|43.36|36.09|1.15|1.98|7.50|3.30|4.93±0.99|5.87±1.00|6.10±0.91|
|M-BASE|✗|✗|60.91|76.79|21.00|12.00|43.61|34.39|1.06|1.88|8.04|8.46|5.13±0.94|5.60±1.12|6.20±0.84|
|M-TEXT|✓|✗|61.15|77.79|24.00|17.00|45.31|33.72|1.04|1.90|7.28|13.78|5.20±0.99|6.03±0.98|6.00±1.02|
|M-MULTI|✓|✓|59.51|73.26|25.00|21.00|45.31|36.25|1.00|1.81|9.96|8.72|6.20±1.05|6.70±1.06|7.07±0.93|



Table 3: Evaluation results. Objective metrics include FAD, Precision, CLAP Audio Similarity (Similarity), KL Divergence, and Recall. Subjective metrics include human ratings for mood, genre, and audio quality. pub and com indicate results on OES-Pub and OES-Com, respectively; avg ± CI refers to average values and 95% confidence intervals. 

ity of the music with the emotional tone of the movie clip (1: not compatible at all, 10: very compatible). For audio quality, participants provide a subjective assessment of the audio quality (1: very poor quality, 10: very high quality). 

In the following section, we present the average rating values and 95% confidence intervals for each model, based on each of the three criteria. 

## 6. RESULTS AND ANALYSIS 

We present our comprehensive evaluation results in Table 3. Distributional Fidelity Our evaluation on OES-Com reveals that fine-tuning on OSSL enhances distributional fidelity. Specifically, S-TEXT and S-MULTI achieve lower FAD scores compared to S-BASE while M-TEXT and M- MULTI exhibit higher Precision scores relative to M-BASE, indicating closer alignment with the target distribution. In contrast, the results on OES-Pub show no significant improvement in distributional fidelity. Although M-TEXT and M-MULTI demonstrate increased Precision scores compared to M-BASE, S-TEXT and S-MULTI actually experience a decrease in Precision when evaluated on OES-Pub. This discrepancy is expected, as distributional fidelity is calculated using reference embeddings from commercial movie soundtracks. Encouragingly, the ability to improve performance on commercial soundtracks by training on public domain data suggests effective feature transfer across domains. Particularly, M-MULTI achieved the lowest FAD scores and highest Precision scroes on both evaluation sets, demonstrating its outstanding performance in distributional fidelity. 

Paired Fidelity Fine-tuning on OSSL consistently increases the CLAP audio similarity between reference and generated music across both OES-Pub and OES-Com datasets. Additionally, training reduces KL divergence when evaluated on OES-Pub, indicating improved alignment in classifier predictions. However, this improvement is less pronounced on OES-Com, suggesting some limitations in generalizing to commercial soundtracks. Notably, M-MULTI stands out by achieving significantly lower KL scores on both datasets, highlighting its superior performance in paired fidelity. 

Sample Diversity Training on OSSL generally results in a slight increase in sample diversity relative to the base models, as indicated by Recall scores when evaluated on OES- 

Pub, with the exception of M-TEXT, which shows a minor decrease. We observe the significantly higher Recall scores for S-TEXT and M-TEXT on OES-Com, despite the use of commercial soundtracks as reference tracks. This finding counters initial concerns about overfitting to patterns unique to public domain data, demonstrating that fine-tuning can enhance diversity even on out-of-domain references. However, S-MULTI exhibits a notable drop in diversity, likely due to the added complexity of learning from both text and video inputs. In contrast, the larger M-MULTI model avoids this issue and even shows slight increases in Recall scores on both datasets relative to the baseline, suggesting that greater model capacity helps mitigate the challenges of multimodal training. 

Human Ratings Human ratings for mood, genre, and quality exhibit wide 95% confidence intervals, reflecting considerable variability in subjective assessments. Despite this, models fine-tuned on OSSL generally receive higher average ratings for mood and genre fidelity compared to their baseline counterparts, indicating better alignment with human expectations in these dimensions. However, training has minimal impact on perceptual quality. We observe an interesting trend video adapters: integrating them into smaller models (S-MULTI) slightly lowers average ratings across all metrics, whereas in medium-sized models (MMULTI), they enhance performance in mood, genre, and quality. This indicates that the benefits of video integration may be contingent on sufficient model capacity. 

## 7. CONCLUSION AND FUTURE WORK 

In this paper, we introduced the Open Screen Soundtrack Library (OSSL), a dataset comprising movie clips, corresponding soundtracks, and mood annotations. To show the effectiveness of our dataset, we adapted a text-to-music generation model with video conditions and fine-tuned it on our dataset. We conducted evaluations both on public domain and commercial films, and the results show the effectiveness of our dataset and architecture, when applied to medium-sized models. However, due to the limited number of participants, the subjective evaluation requires further validation. Despite this, we believe that the OSSL will advance film music research within ethical boundaries and our experiments on the proposed methods show insightful observations for integrating video modalities into existing text-to-music generation models. 

523 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 8. ETHICS STATEMENT 

Our research adheres to ethical principles by ensuring that the construction of Open Screen Soundtrack Library (OSSL) and training methodologies are based solely on copyright-free materials. By publicly releasing our dataset, we aim to promote ethical research practices and encourage the broader community to utilize copyright-free data for model training, fostering transparency and responsible AI development. 

For evaluation, we used commercial movie clips strictly for scientific purposes, with no intent to infringe upon the rights of content producers. We believe our use falls within ethical and fair-use guidelines. However, to respect copyright laws, we will not release video clips of the OES-Com, and instead provide YouTube URLs for video clips for reproducibility. 

## 9. REFERENCES 

- [1] B. Millet, J. Chattah, and S. Ahn, “Soundtrack design: The impact of music on visual attention and affective responses,” Applied ergonomics, vol. 93, p. 103301, 2021. 

- [2] H. T. P. Thao, D. Herremans, and G. Roig, “Multimodal deep models for predicting affective responses evoked by movies.” in ICCV Workshops, 2019, pp. 1618–1627. 

- [3] M. Won, J. Salamon, N. J. Bryan, G. J. Mysore, and X. Serra, “Emotion embedding spaces for matching music to stories,” arXiv preprint arXiv:2111.13468, 2021. 

- [4] H. T. P. Thao, B. Balamurali, G. Roig, and D. Herremans, “Attendaffectnet–emotion prediction of movie viewers using multimodal fusion with self-attention,” Sensors, vol. 21, no. 24, p. 8356, 2021. 

- [5] P. Chua, D. Makris, D. Herremans, G. Roig, and K. Agres, “Predicting emotion from music videos: exploring the relative contribution of visual and auditory information to affective responses,” arXiv preprint arXiv:2202.10453, 2022. 

- [6] K. Xu, “Analysis of the roles of film soundtracks in films,” in 2022 International Conference on Comprehensive Art and Cultural Communication (CACC 2022). Atlantis Press, 2022, pp. 351–355. 

- [7] M. Marszalek, I. Laptev, and C. Schmid, “Actions in context,” in 2009 IEEE Conference on Computer Vision and Pattern Recognition. IEEE, 2009, pp. 2929–2936. 

- [8] M. Tapaswi, Y. Zhu, R. Stiefelhagen, A. Torralba, R. Urtasun, and S. Fidler, “Movieqa: Understanding stories in movies through question-answering,” in Proceedings of the IEEE conference on computer vision and pattern recognition, 2016, pp. 4631–4640. 

- [9] Q. Huang, Y. Xiong, A. Rao, J. Wang, and D. Lin, “Movienet: A holistic dataset for movie understanding,” in Computer Vision–ECCV 2020: 16th European 

Conference, Glasgow, UK, August 23–28, 2020, Proceedings, Part IV 16. Springer, 2020, pp. 709–727. 

- [10] M. Soldan, A. Pardo, J. L. Alcázar, F. Caba, C. Zhao, S. Giancola, and B. Ghanem, “Mad: A scalable dataset for language grounding in videos from movie audio descriptions,” in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2022, pp. 5026–5035. 

- [11] A. Rohrbach, M. Rohrbach, N. Tandon, and B. Schiele, “A dataset for movie description,” in Proceedings of the IEEE conference on computer vision and pattern recognition, 2015, pp. 3202–3212. 

- [12] P. Vicol, M. Tapaswi, L. Castrejon, and S. Fidler, “Moviegraphs: Towards understanding human-centric situations from videos,” in Proceedings of the IEEE conference on computer vision and pattern recognition, 2018, pp. 8581–8590. 

- [13] K. Curtis, G. Awad, S. Rajput, and I. Soboroff, “Hlvu: A new challenge to test deep understanding of movies the way humans do,” in Proceedings of the 2020 International Conference on Multimedia Retrieval, 2020, pp. 355–361. 

- [14] M. Bain, A. Nagrani, A. Brown, and A. Zisserman, “Condensed movies: Story based retrieval with contextual embeddings,” in Proceedings of the Asian Conference on Computer Vision, 2020. 

- [15] W. Xu, P. P. Liang, H. Kim, J. McAuley, T. BergKirkpatrick, and H.-W. Dong, “Teasergen: Generating teasers for long documentaries,” 2024. [Online]. Available: https://arxiv.org/abs/2410.05586 

- [16] J. Copet, F. Kreuk, I. Gat, T. Remez, D. Kant, G. Synnaeve, Y. Adi, and A. Défossez, “Simple and controllable music generation,” Advances in Neural Information Processing Systems, vol. 36, 2024. 

- [17] A. Vaswani, “Attention is all you need,” Advances in Neural Information Processing Systems, 2017. 

- [18] A. Agostinelli, T. I. Denk, Z. Borsos, J. Engel, M. Verzetti, A. Caillon, Q. Huang, A. Jansen, A. Roberts, M. Tagliasacchi et al., “Musiclm: Generating music from text,” arXiv preprint arXiv:2301.11325, 2023. 

- [19] Y.-H. Lan, W.-Y. Hsiao, H.-C. Cheng, and Y.-H. Yang, “Musicongen: Rhythm and chord control for transformer-based text-to-music generation,” arXiv preprint arXiv:2407.15060, 2024. 

- [20] Z. Tian, Z. Liu, R. Yuan, J. Pan, Q. Liu, X. Tan, Q. Chen, W. Xue, and Y. Guo, “Vidmuse: A simple video-tomusic generation framework with long-short-term modeling,” arXiv preprint arXiv:2406.04321, 2024. 

524 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [21] K. Su, J. Y. Li, Q. Huang, D. Kuzmin, J. Lee, C. Donahue, F. Sha, A. Jansen, Y. Wang, M. Verzetti et al., “V2meow: Meowing to the visual beat via video-tomusic generation,” in Proceedings of the AAAI Conference on Artificial Intelligence, vol. 38, no. 5, 2024, pp. 4952–4960. 

- [22] H. Zuo, W. You, J. Wu, S. Ren, P. Chen, M. Zhou, Y. Lu, and L. Sun, “Gvmgen: A general video-to-music generation model with hierarchical attentions,” arXiv preprint arXiv:2501.09972, 2025. 

- [23] S. Forsgren and H. Martiros, “Riffusion-stable diffusion for real-time music generation,” URL https://riffusion. com, 2022. 

- [24] Q. Huang, D. S. Park, T. Wang, T. I. Denk, A. Ly, N. Chen, Z. Zhang, Z. Zhang, J. Yu, C. Frank et al., “Noise2music: Text-conditioned music generation with diffusion models,” arXiv preprint arXiv:2302.03917, 2023. 

- [25] F. Schneider, O. Kamal, Z. Jin, and B. Schölkopf, “Mo\ˆ usai: Text-to-music generation with long-context latent diffusion,” arXiv preprint arXiv:2301.11757, 2023. 

- [26] M. W. Lam, Q. Tian, T. Li, Z. Yin, S. Feng, M. Tu, Y. Ji, R. Xia, M. Ma, X. Song et al., “Efficient neural music generation,” Advances in Neural Information Processing Systems, vol. 36, pp. 17 450–17 463, 2023. 

- [27] J. Melechovsky, Z. Guo, D. Ghosal, N. Majumder, D. Herremans, and S. Poria, “Mustango: Toward controllable text-to-music generation,” arXiv preprint arXiv:2311.08355, 2023. 

- [28] T. Karchkhadze, M. R. Izadi, K. Chen, G. Assayag, and S. Dubnov, “Multi-track musicldm: Towards versatile music generation with latent diffusion model,” arXiv preprint arXiv:2409.02845, 2024. 

- [29] Z. Evans, J. D. Parker, C. Carr, Z. Zukowski, J. Taylor, and J. Pons, “Stable audio open,” arXiv preprint arXiv:2407.14358, 2024. 

- [30] Y.-B. Lin, Y. Tian, L. Yang, G. Bertasius, and H. Wang, “Vmas: Video-to-music generation via semantic alignment in web music videos,” arXiv preprint arXiv:2409.07450, 2024. 

- [31] R. Li, S. Zheng, X. Cheng, Z. Zhang, S. Ji, and Z. Zhao, “Muvi: Video-to-music generation with semantic alignment and rhythmic synchronization,” arXiv preprint arXiv:2410.12957, 2024. 

- [32] O. Tal, A. Ziv, I. Gat, F. Kreuk, and Y. Adi, “Joint audio and symbolic conditioning for temporally controlled text-to-music generation,” arXiv preprint arXiv:2406.10970, 2024. 

- [33] S.-L. Wu, C. Donahue, S. Watanabe, and N. J. Bryan, “Music controlnet: Multiple time-varying controls for music generation,” 2023. 

- [34] Z. Novack, J. McAuley, T. Berg-Kirkpatrick, and N. J. Bryan, “DITTO: Diffusion inference-time t- optimization for music generation,” in International Conference on Machine Learning (ICML), 2024. 

- [35] ——, “DITTO-2: Distilled diffusion inference-time t-optimization for music generation,” in International Society of Music Information Retrieval (ISMIR), 2024. 

- [36] S. Liu, A. S. Hussain, Q. Wu, C. Sun, and Y. Shan, “Mumu-llama: Multi-modal music understanding and generation via large language models,” arXiv preprint arXiv:2412.06660, 2024. 

- [37] B. Wang, L. Zhuo, Z. Wang, C. Bao, W. Chengjing, X. Nie, J. Dai, J. Han, Y. Liao, and S. Liu, “Multimodal music generation with explicit bridges and retrieval augmentation,” arXiv preprint arXiv:2412.09428, 2024. 

- [38] C. Gan, D. Huang, P. Chen, J. B. Tenenbaum, and A. Torralba, “Foley music: Learning to generate music from videos,” in Computer Vision–ECCV 2020: 16th European Conference, Glasgow, UK, August 23–28, 2020, Proceedings, Part XI 16. Springer, 2020, pp. 758–775. 

- [39] S. Di, Z. Jiang, S. Liu, Z. Wang, L. Zhu, Z. He, H. Liu, and S. Yan, “Video background music generation with controllable music transformer,” in Proceedings of the 29th ACM International Conference on Multimedia, 2021, pp. 2037–2045. 

- [40] L. Zhuo, Z. Wang, B. Wang, Y. Liao, C. Bao, S. Peng, S. Han, A. Zhang, F. Fang, and S. Liu, “Video background music generation: Dataset, method and evaluation,” in Proceedings of the IEEE/CVF International Conference on Computer Vision, 2023, pp. 15 637– 15 647. 

- [41] A. Arnab, M. Dehghani, G. Heigold, C. Sun, M. Luˇci´c, and C. Schmid, “Vivit: A video vision transformer,” in Proceedings of the IEEE/CVF international conference on computer vision, 2021, pp. 6836–6846. 

- [42] N. Houlsby, A. Giurgiu, S. Jastrzebski, B. Morrone, Q. De Laroussilhe, A. Gesmundo, M. Attariyan, and S. Gelly, “Parameter-efficient transfer learning for nlp,” in International conference on machine learning. PMLR, 2019, pp. 2790–2799. 

- [43] J. Pfeiffer, A. Kamath, A. Rücklé, K. Cho, and I. Gurevych, “Adapterfusion: Non-destructive task composition for transfer learning,” arXiv preprint arXiv:2005.00247, 2020. 

- [44] J. Pfeiffer, A. Rücklé, C. Poth, A. Kamath, I. Vuli´c, S. Ruder, K. Cho, and I. Gurevych, “Adapterhub: A framework for adapting transformers,” arXiv preprint arXiv:2007.07779, 2020. 

- [45] H. Ye, J. Zhang, S. Liu, X. Han, and W. Yang, “Ip-adapter: Text compatible image prompt adapter for text-to-image diffusion models,” arXiv preprint arXiv:2308.06721, 2023. 

525 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [46] C. Mou, X. Wang, L. Xie, Y. Wu, J. Zhang, Z. Qi, and Y. Shan, “T2i-adapter: Learning adapters to dig out more controllable ability for text-to-image diffusion models,” in Proceedings of the AAAI Conference on Artificial Intelligence, vol. 38, no. 5, 2024, pp. 4296– 4304. 

- [47] F.-D. Tsai, S.-L. Wu, H. Kim, B.-Y. Chen, H.-C. Cheng, and Y.-H. Yang, “Audio prompt adapter: Unleashing music editing abilities for textto-music with lightweight finetuning,” arXiv preprint arXiv:2407.16564, 2024. 

- [48] S. Hong, W. Im, and H. S. Yang, “Contentbased video-music retrieval using soft intra-modal structure constraint,” 2017. [Online]. Available: https: //arxiv.org/abs/1704.06761 

- [49] B. Li, X. Liu, K. Dinesh, Z. Duan, and G. Sharma, “Creating a multitrack classical music performance dataset for multimodal music analysis: Challenges, insights, and applications,” IEEE Transactions on Multimedia, vol. 21, no. 2, p. 522–535, Feb. 2019. [Online]. Available: http://dx.doi.org/10.1109/TMM. 2018.2856090 

- [50] Y. Zhu, K. Olszewski, Y. Wu, P. Achlioptas, M. Chai, Y. Yan, and S. Tulyakov, “Quantized gan for complex music generation from dance videos,” 2022. [Online]. Available: https://arxiv.org/abs/2204.00604 

- [51] R. Li, S. Yang, D. A. Ross, and A. Kanazawa, “Ai choreographer: Music conditioned 3d dance generation with aist++,” 2021. [Online]. Available: https://arxiv.org/abs/2101.08779 

- [52] L. Zhuo, Z. Wang, B. Wang, Y. Liao, C. Bao, S. Peng, S. Han, A. Zhang, F. Fang, and S. Liu, “Video background music generation: Dataset, method and evaluation,” in Proceedings of the IEEE/CVF International Conference on Computer Vision, 2023, pp. 15 637– 15 647. 

- [53] J. Kang, S. Poria, and D. Herremans, “Video2music: Suitable music generation from videos using an affective multimodal transformer model,” Expert Systems with Applications, vol. 249, p. 123640, Sep. 2024. [Online]. Available: http://dx.doi.org/10.1016/j. eswa.2024.123640 

- [54] S. Li, Y. Qin, M. Zheng, X. Jin, and Y. Liu, “Diffbgm: A diffusion model for video background music generation,” 2024. 

- [55] I. Cardoso, R. O. Moraes, and L. N. Ferreira, “The nes video-music database: A dataset of symbolic video game music paired with gameplay videos,” in Proceedings of the 19th International Conference on the Foundations of Digital Games, ser. FDG 2024. ACM, May 2024, p. 1–6. [Online]. Available: http://dx.doi.org/10.1145/3649921.3650011 

- [56] R. Solovyev, A. Stempkovskiy, and T. Habruseva, “Benchmarks and leaderboards for sound demixing tasks,” 2023. 

- [57] T. Giannakopoulos, “pyaudioanalysis: An open-source python library for audio signal analysis,” PloS one, vol. 10, no. 12, p. e0144610, 2015. 

- [58] Q. Kong, Y. Cao, T. Iqbal, Y. Wang, W. Wang, and M. D. Plumbley, “Panns: Large-scale pretrained audio neural networks for audio pattern recognition,” IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 28, pp. 2880–2894, 2020. 

- [59] J. A. Russell, “A circumplex model of affect.” Journal of personality and social psychology, vol. 39, no. 6, p. 1161, 1980. 

- [60] H.-T. Hung, J. Ching, S. Doh, N. Kim, J. Nam, and Y.-H. Yang, “Emopia: A multi-modal pop piano dataset for emotion recognition and emotion-based music generation,” arXiv preprint arXiv:2108.01374, 2021. 

- [61] A. Défossez, J. Copet, G. Synnaeve, and Y. Adi, “High fidelity neural audio compression,” arXiv preprint arXiv:2210.13438, 2022. 

- [62] W. Kay, J. Carreira, K. Simonyan, B. Zhang, C. Hillier, S. Vijayanarasimhan, F. Viola, T. Green, T. Back, P. Natsev, M. Suleyman, and A. Zisserman, “The kinetics human action video dataset,” 2017. [Online]. Available: https://arxiv.org/abs/1705.06950 

- [63] E. J. Hu, Y. Shen, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang, L. Wang, and W. Chen, “Lora: Low-rank adaptation of large language models,” arXiv preprint arXiv:2106.09685, 2021. 

- [64] T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P. Dhariwal, A. Neelakantan, P. Shyam, G. Sastry, A. Askell et al., “Language models are few-shot learners,” Advances in neural information processing systems, vol. 33, pp. 1877–1901, 2020. 

- [65] V. Liu and L. B. Chilton, “Design guidelines for prompt engineering text-to-image generative models,” in Proceedings of the 2022 CHI conference on human factors in computing systems, 2022, pp. 1–23. 

- [66] J. White, Q. Fu, S. Hays, M. Sandborn, C. Olea, H. Gilbert, A. Elnashar, J. Spencer-Smith, and D. C. Schmidt, “A prompt pattern catalog to enhance prompt engineering with chatgpt,” arXiv preprint arXiv:2302.11382, 2023. 

- [67] S. Doh, K. Choi, J. Lee, and J. Nam, “Lp-musiccaps: Llm-based pseudo music captioning,” arXiv preprint arXiv:2307.16372, 2023. 

- [68] F. H. Ilya Loshchilov, “Decoupled weight decay regularization,” arXiv preprint arXiv:1711.05101, 2017. 

526 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [69] I. Loshchilov and F. Hutter, “Sgdr: Stochastic gradient descent with warm restarts,” arXiv preprint arXiv:1608.03983, 2016. 

- [70] Z. Novack, G. Zhu, J. Casebeer, J. McAuley, T. BergKirkpatrick, and N. J. Bryan, “Presto! distilling steps and layers for accelerating music generation.” in International Conference on Learning Representations (ICLR), 2025. 

- [71] J. Nistal, M. Pasini, C. Aouameur, M. Grachten, and S. Lattner, “Diff-a-riff: Musical accompaniment cocreation via latent diffusion models,” arXiv preprint arXiv:2406.08384, 2024. 

- [72] Y. Wu, K. Chen, T. Zhang, Y. Hui, T. Berg-Kirkpatrick, and S. Dubnov, “Large-scale contrastive language-audio pretraining with feature fusion and keyword-to-caption augmentation,” in ICASSP 2023-2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2023, pp. 1–5. 

- [73] K. Kilgour, M. Zuluaga, D. Roblek, and M. Sharifi, “Fr\’echet audio distance: A metric for evaluating music enhancement algorithms,” arXiv preprint arXiv:1812.08466, 2018. 

- [74] M. F. Naeem, S. J. Oh, Y. Uh, Y. Choi, and J. Yoo, “Reliable fidelity and diversity metrics for generative models,” 2020. 

- [75] K. Koutini, J. Schlüter, H. Eghbal-Zadeh, and G. Widmer, “Efficient training of audio transformers with patchout,” arXiv preprint arXiv:2110.05069, 2021. 

527 

