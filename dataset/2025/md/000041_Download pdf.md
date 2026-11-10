---
paper_id: "000041"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706414/files/000041.pdf"
---

# EXPOTION: FACIAL EXPRESSION AND MOTION CONTROL FOR MULTIMODAL MUSIC GENERATION 

Fathinah Izzati<sup>∗</sup> 

Xinyue Li<sup>∗</sup> Gus Xia 

Mohamed bin Zayed University of Artificial Intelligence, United Arab Emirates `{fathinah.izzati, xinyue.li, gus.xia}@mbzuai.ac.ae` 

## ABSTRACT 

We propose EXPOTION (Facial Expression and Motion Control for Multimodal Music Generation), a generative model leveraging multimodal visual controls—specifically, human facial expressions and upper-body motion—as well as text prompts to produce expressive and temporally accurate music. We adopt parameter-efficient fine-tuning (PEFT) on the pretrained text-to-music generation model, enabling fine-grained adaptation to the multimodal controls using a small dataset. To ensure precise synchronization between video and music, we introduce a temporal smoothing strategy to align multiple modalities. Experiments demonstrate that integrating visual features alongside textual descriptions enhances the overall quality of generated music in terms of musicality, creativity, beat-tempo consistency, temporal alignment with the video, and text adherence, surpassing both proposed baselines and existing state-of-the-art video-to-music generation models. Additionally, we introduce a novel dataset consisting of 7 hours of synchronized video recordings capturing expressive facial and upper-body gestures aligned with corresponding music, providing significant potential for future research in multimodal and interactive music generation. Code, demo and dataset are available at `https: //github.com/xinyueli2896/Expotion.git` 

## 1. INTRODUCTION 

Music generation models have become increasingly versatile and interactive, capable of integrating control signals from various modalities, including audio, text, and symbolic representations (such as MIDI or musical scores). These conditions act as control to guide the model toward producing more precise, and targeted outputs aligned with user expectations. Although current text-to-music generation models can produce impressive musical quality, they often lack the fine-grained temporal control mechanisms 

> ∗These authors contributed equally to this work. 

> © F. Izzati, X. Li, and G. Xia. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: F. Izzati, X. Li, and G. Xia, “Expotion: Facial Expression and Motion Control for Multimodal Music Generation”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 



<!-- Start of picture text -->
"A sly, whimsical melody full of sneaky<br>rhythms and playful surprises, like a T5 Encoder<br>musical prank with a grin."<br>Cross Attention<br>Conditional<br>Adapter<br>EmbeddingJoint Music Generation ModelTransformer-based<br>Encoder<br>Expressive Music<br>-MMr<br><!-- End of picture text -->

Figure 1. Overview of Expotion’s multimodal inference pipeline, showing how visual gestures and facial expressions guide expressive music generation. 

and expressivity necessary to flexibly adapt to a wide range of real-world scenarios. 

Inspired by the idea that gestures and facial expressions can act as important guides for music, similar to what conductors do, we further explore visual controls in this study and propose Expotion, a deep music generative model with multimodal controls–facial expression and upper body motion, as well as text prompts. Expotion is designed to synthesize high-quality music that is both expressive (ensuring that the musical content reflects the emotional and expressive cues of the face and gestures) and temporally accurate (so that every change in motion and expression is accurately mirrored in the music) with the input video, as shown in Figure 1. 

While some studies have explored audio–music generation tasks given videos—ranging from audio effects generation (e.g., [1–11]) video music background generation (e.g., [12–15]), and dance music generation (e.g., [16–18] among others), our work focuses on the subtle dynamics of gestures and facial expressions, emphasizing their finegrained temporal synchronization with music generation. This opens up potential applications in real-time, interactive audiovisual systems. 

To achieve our goal, we first introduce a newly curated dataset comprising of 7 hours of carefully synchronized video-music pairs featuring expressive gestures and facial expressions closely matched to the corresponding music. Given the limited amount of data, we employ parameter-efficient fine-tuning (PEFT) on a transformerbased text-to-music generation model [19]—leveraging powerful ability of the model pretrained on a massive 

354 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

music-text data that have been shown to be effective in incorporating additional modalities [9, 10, 20–23]. By finetuning only 4% of the original model’s parameters [20], our method seamlessly integrates multimodal visual inputs (facial expressions and upper-body gestures) using only 130 video–audio pairs for training, thereby minimizing network complexity while ensuring robust multimodal fusion. We also propose an approach called temporal smoothing to ensure precise and efficient temporal alignment between audio and video modalities. 

Our experiments show that Expotion can generate highquality, temporally accurate music that faithfully reflects the expressive nuances inherent in the visual inputs and textual descriptions. Although textual descriptions supply the primary contextual cues—leveraging the model’s strong text-understanding capabilities to guarantee baseline music quality—the addition of visual input further enhances alignment, expressiveness, and consistency. In comprehensive subjective and objective evaluations, Expotion consistently outperforms current state-of-the-art video-to-music generation models [24] and multimodal captioning baselines across multiple metrics, including (1) Quality of Generated Music, (2) Beats and Tempo Consistency, (3) Text-Audio Similarity, and (4) Video–Music Consistency. 

To the best of our knowledge, this work is the first to leverage synchronized expressive gestures and facial expressions for music generation. Our experiments show that incorporating visual features as control signals not only enhances the temporal alignment between the video and generated music but also improves text adherence and overall musical quality—highlighting the complementary strengths of both modalities. We believe that Expotion will empower artists with a more expressive, controllable, and interactive approach to music creation. 

## 2. RELATED WORK 

We review three key paradigms for controllable music generation: visual and motion-based control, textual and symbolic conditioning, and training and adaptation strategies. 

Visual and Motion-Based Control Early interactive systems mapped facial or bodily features directly to sound. Valenti et al.’s Sonify Your Face modulated audio via Bayesian classification of facial motion units [25], and Clay et al. translated whole-body emotional expressions into electronic-music parameters [26]. D2MNet extracted global style and local beat vectors from LMA-derived movement signals to drive an autoregressive generator [27]. DeepTunes [28] and [29] combine CNN-based emotion detection with GPT-2 lyric models, LSTMs, and transformers to jointly predict discrete and valence–arousal emotions and produce synchronized music (and lyrics) that closely reflect the user’s image input. Videoconditioned models such as VidMuse [24], V2Meow [15], and Video2Music [14] align music with motion cues and scene context, while Foley-style systems translate indi- 

vidual events to sound via latent diffusion or transformers [1,2,8]. 

Textual and Symbolic Conditioning Text-to-music models like MusicLM [30] and MusicGen [19] generate high-quality audio from descriptive prompts but lack explicit time-varying control. MusicGen-Melody extends this by conditioning on a reference melody track for pitch contours [19]. CoCoMulla leverages chord charts and drum patterns to control harmony and rhythm [20], and Sketch2Sound introduces continuous vocal–imitation curves (loudness, brightness, pitch) alongside text to modulate audio generation [21]. 

Training and Adaptation Strategies Many video-toaudio and music models are trained from scratch on large paired datasets—such as AudioSet [31] and VGGSound [32]—to learn cross-modal correspondences [1–4, 24]. When data is limited, parameter-efficient fine-tuning (PEFT) is effective: Sketch2Sound fine-tunes a single linear layer per control signal on a frozen diffusion backbone [21], while CoCoMulla and AirGen attach lightweight adapters to MusicGen, tuning under 4% of parameters for chord and rhythm control or music inpainting [20,33]. Expotion adopts a similar PEFT approach with visual multimodal inputs. 

## 3. METHODOLOGY 

Our approach consists of of 1) a joint embedding encoder to integrate temporally aligned video-based controls, and 2) a condition adaptor to fine-tune MusicGen by incorporating the learned joint visual embeddings. We froze the parameters of the vanilla Musicgen during training to preserve its text understanding ability. 

## 3.1 Joint Visual Embeddings 

To effectively incorporate facial expression and upperbody movement features from video, we adopt a joint embedding framework combining these two types of features, as shown in Figure 2. Since videos capturing facial expressions and upper-body gestures typically exhibit less dynamic motion, a relatively low frame rate is sufficient for smooth human perception. To address the discrepancy between this frame rate and the frame rate of MusicGen, we introduce targeted sampling strategies for video feature processing that differ from those applied to audio. We also propose an approach called temporal smoothing to ensure precise and efficient temporal alignment between audio and video modalities, maintaining the expressivity of video, and enhancing the overall multimodal integration. 

## 3.1.1 Facial Expression Embedding 

To extract facial expression features from video, we employed MARLIN, a self-supervised learning framework specifically designed to derive universal facial representations from unannotated video data [34]. For each frame, MARLIN generates features that capture information from both the current frame and its neighboring frames. To temporally align these facial expression features with the au- 

355 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
Concatenation<br>Temporal Smoothing Low-rank<br>Feature<br>Extraction Projection<br>I<br>Visual Feature Embeddings Interpolated Embeddings +<br>Positional Linear<br>Encoding Projection<br>Joint Embeddings Latent Embeddings<br>+<br>_<br><!-- End of picture text -->

Figure 2. Joint embedding of visual features. Facial expression and motion features are first extracted from the given video and temporally smoothed through interpolation, producing refined intermediate representations. These temporally aligned embeddings then undergo dimensionality reduction through the low-rank projection layer. Then, the concatenated embeddings are projected to the same dimension as the MusicGen hidden layers. Finally, the positional encoding is added to the latent embeddings to form the final joint embeddings. 

dio codes produced by Encodec in MusicGen, we utilized a specialized temporal smoothing strategy: first resampling the video from 30 fps to 80 fps and then, since MARLIN processes 16 frames simultaneously, obtaining the facial expression features in a frame rate of 5 fps by setting the stride to 16 frames. To minimize information loss from this downsampling, we applied linear interpolation to the facial expression feature zf ∈ R<sup>T ×768</sup> , where T is the total number of frames and 768 is the hidden dimension. z<sup>(i)</sup> ∈ R<sup>d1</sup> f represents the feature at i-th frame. For a desired (possibly non-integer) time index t, let 



<!-- Start of picture text -->
i = ⌊t⌋, α = t − i,<br><!-- End of picture text -->

so that t lies between the i-th and (i + 1)-th frames. The interpolated feature zˆf<sup>(t)</sup> is computed as 



<!-- Start of picture text -->
zˆft = (1 − α) zfi + α zfi+1 . (1)<br><!-- End of picture text -->

This formula linearly weights the neighboring features, ensuring a smooth transition between frames. 

We further compress the interpolated facial features by projecting them onto a low-dimensional space with dimension d1 using a trainable matrix Wf ∈ R<sup>d1×768</sup> : 



<!-- Start of picture text -->
z ′ fi = W T f zˆf i ∈ Rd1 . (2)<br><!-- End of picture text -->

## 3.1.2 Motion Embedding 

We compare two motion representations: one extracted from the Synchformer visual encoder [35] and another from RAFT optical flow [36]. 

For Synchformer, we standardize videos fps and segment each video into 16-frame clips with a stride of 5, yielding outputs of shape (T, 8, dim), where the 8 dimension captures local temporal context. We flatten the first 

two dimensions, perform temporal interpolation as 



<!-- Start of picture text -->
zˆmt = (1 − α) zmi + α zmi+1 , (3)<br><!-- End of picture text -->

and then project the interpolated features to a lowerdimensional space using a trainable matrix Wm ∈ R<sup>d2×D</sup> (D = original feature dimension), yielding 



<!-- Start of picture text -->
zm ′ i = W T m zˆm i ∈ Rd2 . (4)<br><!-- End of picture text -->

For RAFT, we sample the video at 5 fps to obtain frames {It}<sup>T</sup> t=1<sup>andcomputethedenseopticalflowFt∈</sup> R<sup>H×W ×2</sup> for each consecutive pair (It, It+1) using RAFT [36]. Each flow field is then processed by a Flow Embedding CNN F to yield a compact feature vector: 



<!-- Start of picture text -->
zt flow = F(Ft) ∈ R 256 . (5)<br><!-- End of picture text -->

F is composed of several convolutional layers with kernel size 3 and ReLU activations, followed by an adaptive average pooling operation. We perform temporal interpolation and project the resulting sequence to a lowerdimensional space in the same way as Sychformer. This ensures that both motion representations are aligned in time and compatible with the MusicGen transformer’s input requirements. 

## 3.1.3 Positional Embeddings 

We define a learnable matrix We ∈ R<sup>(d1+d2)×d</sup> to fuse the embeddings mentioned above, together with a learnable positional embedding zpos,i ∈ R<sup>d1+d2</sup> to support sequential modeling. The combined joint symbolic and acoustic embedding is computed as: 



<!-- Start of picture text -->
zi = We T zfi ; zmi ] + zpos,i ∈ R d . (6)<br><!-- End of picture text -->

356 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

Let T denote the total number of frames. Then, the overall sequential joint embedding is given by: 

z = {z1, z2, . . . , zT } ∈ R<sup>T ×d</sup> . (7) 

## 3.2 Condition Adaptor 

Adopting a similar approach to CoCoMulla [20], we extend the idea of a condition adaptor to handle time-varying video inputs, such as facial expressions and motion. In a standard Transformer, each self-attention layer processes T hidden embeddings (one per Encodec frame). In our approach, the final L layers of the MusicGen decoder expand this to 2T embeddings by adding T condition prefix positions, which encode the control information. Specifically, we insert a sequence of learnable input embeddings into the (N − L + 1)th decoder layer to initiate the condition prefix. In this prefix, the hidden states go only through self-attention layers (omitting cross-attention). Let 



<!-- Start of picture text -->
Hl p ∈ RT ×d (N − L + 1 ≤ l ≤ N )<br><!-- End of picture text -->

be the output for the condition prefix, with H0<sup>pas the learn-</sup> able input embeddings. The condition prefix is computed as: 



<!-- Start of picture text -->
Q p l , K l p, V l p = QKV-projector �Hl p + Zl �,<br>Hl p +1 = Self-Attention �Q p l , K l p, V l p �,<br><!-- End of picture text -->

where Zl are the sequential joint embeddings (defined in Eq. (7)). No causal mask is applied here, and the condition prefix does not attend to the Encodec tokens. 

For the remaining part, the hidden states Hl ∈ R<sup>T ×d</sup> (for 1 ≤ l ≤ N ) are processed normally. Their standard attention output Sl is computed as: 



<!-- Start of picture text -->
Ql, Kl, Vl = QKV-projector(Hl),<br>Sl = Self-Attention�Ql, Kl, Vl�.<br><!-- End of picture text -->

To incorporate condition information in the last L layers, we compute cross attention Sl<sup>′betweenQland</sup> {Kl<sup>p, V</sup> l<sup>p} using self-attention, fusing Qlwith Qp</sup> l<sup>:</sup> 



<!-- Start of picture text -->
Sl ′ = Self-Attention �Ql + Q p l , K l p, V l p �.<br><!-- End of picture text -->

A learnable gating factor gl (initialized to zero) combines the outputs: 



<!-- Start of picture text -->
Hl+1 = Cross-Attention�Sl + gl · Sl ′, text �.<br><!-- End of picture text -->

In our implementation, all MusicGen layers (including QKV-projector, Self-Attention, and Cross-Attention) are frozen; only H0<sup>p, Wp, Wa, We, zpos, and glare trainable.</sup> 

## 4. EXPERIMENTS 

listening to 30-second audio clips. Before starting the recording, the volunteers were asked to listen to the music track once, allowing them time to think about the facial expressions and body movements that would align with the music. The audio clips used were licensed instrumental tracks from Epidemic Sound, ensuring no vocals were present. The collection includes a variety of music genres, such as pop, jazz, blues, classical, and epic, among others. We were able to collect 7 hours of paired video-audio data. The paired video-audio data are then chopped into 10 seconds per clip. We set aside 30 minutes of data for test and validation. We also generated captions for each audio clip with audio-captioning model SALMONN [37] to be used as text prompts during training and inference. The prompt given to SALMONN for captioning is ’Please describe the music’. In the data collecting process, volunteers gave informed consent, agreeing that their videos would be used only for research and anonymized to protect their privacy. 

## 4.2 Implementation 

Our base model, MusicGen (text-only), consists of three main parts: a pre-trained EnCodec, a pre-trained T5 encoder, and an acoustic transformer decoder. The decoder has 48 layers, each with causal self-attention and cross-attention to process text prompts. MusicGen uses EnCodec, a Residual Vector Quantization (RVQ) autoencoder [38], to convert audio sampled at 32,000 Hz into discrete codes at 50 Hz, which are then passed to the transformer decoder. 

We trained the proposed model using four A1000 GPUs, employing an initial learning rate of 1e-02 and a batch size of 10 consisting of ten 10-second audio samples, for 40 epochs. Training was stopped after 40 epochs to prevent overfitting. During training, the model’s parameters were updated using a cross-entropy reconstruction loss. In the low-rank projection step, we set d1 in Equation (2) and d2 in Equation (4) to be 12. 

## 4.3 Baselines 

Since our model addresses a novel domain for which no existing opensource models are specifically trained with both video (facial expression and motion) and text controls, we selected vanilla MusicGen (text-conditioned) and two recent video-conditioned music generation models—VidMuse [24] and Video2Music [39]—as our baselines. Video2Music uses an Affective Multimodal Transformer to generate emotionally aligned, expressive symbolic music (chords) from video inputs by leveraging semantic, motion, scene, and emotion features, while VidMuse integrates both local and global visual cues through a Long-Short-Term Visual Module. 

## 4.1 Dataset 

## 4.4 Evaluation 

Due to the lack of sufficient paired video-audio data with clear facial features, we curated our own dataset by collecting the data manually. We recruited volunteers to record their facial expressions and upper body movements while 

Our evaluation consists of two parts: subjective and objective evaluations. Because MusicGen only accepts textual input, we generate fused multimodal captions from the 

357 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

||||Gen|eral Music Q|uality|Rhythm Alig|nment|Text/Video-A|udio Consistency|
|---|---|---|---|---|---|---|---|---|---|
||Motion Feat.|Prompt F|AD-VGG↓|Avg. KL↓A|vg. IS Score↑|Tempo Err. (bpm)↓F|1-score (Beat)|↑Text-Audio↑|Video-Audio↑|
|face|–|Generated|2.52|0.74|1.45|31.53|0.38|0.48|0.55|
|motion|RAFT|Generic|3.56|1.05|1.16|28.07|0.37|0.38|0.65|
|motion|RAFT|Generated|2.25|0.66|1.53|33.71|0.37|0.52|0.59|
|motion|Syncformer|Generic|3.52|1.08|1.20|31.03|0.35|0.37|0.61|
|motion|Syncformer|Generated|1.93|0.65|1.57|32.89|0.36|0.52|0.61|
|face+motion|Syncformer|Generated|2.55|0.67|1.49|32.72|0.37|0.54|0.59|
|MusicGen|–|Generated|2.76|0.79|1.54|35.84|0.33|0.50|0.42|
|Video2Music|–|–|18.97|1.32|1.01|26.13|0.38|0.25|0.59|
|VidMuse|–|–|9.91|1.10|1.33|33.01|0.37|0.36|0.52|



Table 1. Comparison of music quality, rhythm alignment, and text/video-audio consistency metrics across different configurations. 

video–audio pairs to serve as prompts for the text-only MusicGen baseline. This approach ensures a fair comparison by providing equivalent descriptive information across all models. 

## 4.4.1 Objective Evaluation 

In our objective evaluation, we assess the music generated from three perspectives: (1) the inherent quality, (2) rhythm alignment, and (3) text/video-audio consistency. To measure the inherent quality of the music, we employed Frechet Audio Distance(FAD) with VGGish embeddings which measures perceptual similarity to real music [40, 41], Kullback-Leibler (KL) divergence which quantifies distributional alignment with real audio labels [42,43], and Inter-Sample Score (IS Score) which captures the diversity among generated samples [44]. To evaluate the rhythm alignment between generated and ground truth music, we calculated the tempo error, which is defined as how far an estimated BPM(beats-per-minute) deviates from the true (ground-truth) BPM, and beat consistency between the generated and reference music. To evaluate the text/video-audio consistency, we use CLAP [45] and LanguageBind [46] respectively. We employ these models trained with contrastive learning approach to measure model’s ability to generate music that reflects the semantic meaning of the text and video. 

## 4.4.2 Subjective Evaluation 

We gathered participants of varying level of musical background to rate the generated music—across various configurations and the baseline—over five groups of six videos. They were shown the text prompts without being informed which model produced each track. Ratings were based on the following criteria: 

- Musicality: How effectively the audio captures key musical qualities. 

- Text-audio Similarity: The degree of alignment between the generated music and the provided textual prompt. 

- Video-audio Consistency: The extent to which the music corresponds with the video content in terms of tempo and emotional expression. 

- Creativity: The uniqueness and innovativeness of the generated audio. 

## 4.5 Ablation studies 

We conducted ablation studies to evaluate the effects of various experimental setups. Specifically, these studies explored the following model setups: (1) the use of different motion features (RAFT versus Synchformer) and (2) the use of generic prompts of ‘music with catchy melody’ versus detailed prompts generated by the audio-captioning model. 

## 5. RESULTS 

## 5.1 Objective Evaluations 

General Music Quality. The results in Table 1 demonstrate that models incorporating motion information, particularly those using the Syncformer features with generated prompts, consistently outperform others across general music quality metrics, especially the baselines. This configuration performs best overall, with the lowest FAD and KL scores and the highest IS Score, indicating realistic, diverse, and well-aligned music generation. Comparatively, models using the RAFT features perform less consistently, and those using only facial input or generic prompts yield weaker results. Baseline methods like VidMuse and Video2Music show significantly poorer FD and KL scores, highlighting the advantage of multimodal control of our model. 

Rhythm Alignment. Among all the configuration tested, the model trained with RAFT motion features and generic captions achieves the lowest Average Tempo Error (28.07 BPM), indicating better temporal alignment with the audio compared to other proposed methods. Video2Music achieves the lowest tempo error because it transcribes the audio into MIDI and computes rhythmic characteristics in the form of note density and loudness from the audio–a proxies for the music’s rhythms [14]. The baseline model MusicGen shows the poorest performance in all tempo and beat tracking metrics, underscoring its non-expressiveness in controlling generated music. 

Text/Video-Audio Consistency The text-audio similarity scores reveal that multimodal conditioning (face and motion) significantly enhance text-alignment compared to text-only conditioning baseline (MusicGen), although they do not provide explicit textual information. The face+motion model achieves the highest text-music scores 

358 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

(0.54).In contrast, video-audio similarity scores show that models trained with generic (non-descriptive) captions achieve stronger alignment with video (e.g., 0.65 and 0.61), suggesting that text conditioning may not benefit—and may even hinder—video-audio consistency. The poor video-audio alignment of MusicGen outputs and the low text-audio alignment in music generated by Video2Music and VidMuse is justied as these models are not conditioned on the respective modalities. 

## 5.2 Subjective Evaluation 



<!-- Start of picture text -->
Text-audio Similarity<br>Creativity Musicality<br>baseline<br>face<br>face_motion Video-audio Consistency<br>motion<br>motion_generic_prompts<br><!-- End of picture text -->

Figure 3. Subjective Evaluation Results on Four Metrics 

Figure 3 presents a subjective analysis of the quality of music generated by five models—vanilla MusicGen(baseline) and four variants of our models trained with different configurations. A total of 13 participants (6 female, 7 male) aged 18–40 years (Median = 27) took part. Based on self-reported musical training, 20 % of participants have beginner level of experience in music, 20 % intermediate, and 60 % professional. 

Notably, all of our models—except for one—outperform the baseline in creativity and musicality, suggesting that incorporating facial expressions and motion cues enables the system to better capture the expressive qualities of the input video. This expressiveness is reflected in the generated music, which participants perceive as more musical and creative. Our model trained with only motion features and generic prompts, perform poorly in all evaluation metrics, indicating that generic textual prompts are insufficient to guide high-quality music generation. Without meaningful textual context, visual features alone do not provide enough semantic grounding to produce good music. The superior performance of motion features over facial features in both objective and subjective evaluations likely stems from the nature of the dataset: participants found it easier to convey musical cues through movements rather than facial expressions, resulting in richer and more expressive motion data. These findings highlight that visual and textual modalities are complementary: while textual input provides semantic intent, visual features—especially motion—enrich the 

generated music’s expressiveness. Overall, our model, integrating features from both modality is capable for producing music that is coherent, expressive, and creative as perceived by human. 

## 5.3 Ablation Studies 

## 5.3.1 RAFT vs. Synchformer 

The comparison between RAFT and Syncformer as motion feature extractors reveals notable differences in both general music quality and rhythm-related metrics as shown in Table 1. Syncformer outperforms RAFT across FAD, and IS Score, indicating more realistic and slightly more diverse music generation. However, there is no significant difference between the choice of these two motion featrues in terms of tempo error and beat accuracy of the generated music. These finding suggests that Syncformer may capture more expressive and semantically rich motion patterns, whereas RAFT may be better at preserving rhythmic consistency in simpler contexts. 

## 5.3.2 Generic vs. Generated Captions 

Comparing models trained with generated captions to those using generic captions, we observed that although music generated with generic captions yielded lower CLAP scores—likely due to receiving minimal textual information—they achieved better tempo accuracy than those trained with generated prompts (tempo error of 28.07 BPM tempo versus 33.71 BPM when comparing models trained with same configuration except for choice for prompts). This suggests that adding extra textual context may introduce noise or distract from the purely visual motion cues, ultimately reducing temporal accuracy. 

## 6. CONCLUSION 

Expotion demonstrates that visual cues—specifically, body movements and facial expressions—can effectively serve as expressive controls for music generation. By leveraging a pretrained text-to-music model [19] and applying parameter-efficient fine-tuning, our approach achieves notable improvements from the original text-only conditioning MusicGen using only 130 clips (6 hours) of training data in 40 epochs. Integrating these multimodal signals with textual prompts, Expotion produces music that shows strength in musicality, creativity, and temporal accuracy, as evidenced by enhanced beat, tempo, and overall semantic consistency across text, video, and audio. A temporal smoothing strategy further ensures fine-grained alignment between the visual cues and the generated music. Our results outperform state-of-the-art baselines, and subjective studies confirm that the combination of facial and motion features yields superior performance, while objective evaluations highlight that motion features—particularly those extracted via Synchformer—strike an optimal balance between rhythmic consistency and expressive dynamics. Overall, Expotion represents a promising step toward more expressive, controllable, and interactive audiovisual music generation systems. 

359 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 7. REFERENCES 

- [1] H. K. Cheng, M. Ishii, A. Hayakawa, T. Shibuya, A. Schwing, and Y. Mitsufuji, “Taming Multimodal Joint Training for High-Quality Video-to-Audio Synthesis,” CVPR, 2025. 

- [2] S. Luo, C. Yan, C. Hu, and H. Zhao, “Diff-Foley: Synchronized Video-to-Audio Synthesis with Latent Diffusion Models,” in Advances in Neural Information Processing Systems (NeurIPS), 2023. 

- [3] I. Viertola, V. Iashin, and E. Rahtu, “Temporally Aligned Audio for Video with Autoregression,” IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2025. 

- [4] Y. Zhang, Y. Gu, Y. Zeng, Z. Xing, Y. Wang, Z. Wu, and K. Chen, “FoleyCrafter: Bring Silent Videos to Life with Lifelike and Synchronized Sounds,” arXiv preprint arXiv:2407.01494, 2024. 

- [5] Y. Wang, W. Guo, R. Huang, J. Huang, Z. Wang, F. You, R. Li, and Z. Zhao, “Frieren: Efficient Videoto-Audio Generation Network with Rectified Flow Matching,” in Advances in Neural Information Processing Systems (NeurIPS), 2024. 

- [6] M. Sun, W. Wang, Y. Qiao, J. Sun, Z. Qin, L. Guo, X. Zhu, and J. Liu, “MM-LDM: Multi-Modal Latent Diffusion Model for Sounding Video Generation,” in Proceedings of the 32nd ACM International Conference on Multimedia (ACM MM), 2024. 

- [7] S. Yang, Z. Zhong, M. Zhao, S. Takahashi, M. Ishii, T. Shibuya, and Y. Mitsufuji, “Visual Echoes: A Simple Unified Transformer for Audio-Visual Generation,” arXiv preprint arXiv:2405.14598, 2024. 

- [8] J. Lee, J. Im, D. Kim, and J. Nam, “Video-Foley: Two-Stage Video-To-Sound Generation via Temporal Event Condition For Foley Sound,” arXiv preprint arXiv:2408.11915, 2024. 

- [9] X. Liu, K. Su, and E. Shlizerman, “Tell what you hear from what you see: Video to audio generation through text,” arXiv preprint arXiv:2402.05937, 2024. 

- [10] S. Mo, J. Shi, and Y. Tian, “Text-to-audio generation synchronized with videos,” arXiv preprint arXiv:2403.07055, 2024. 

- [11] Y. Du, Z. Chen, J. Salamon, B. Russell, and A. Owens, “Conditional Generation of Audio from Video via Foley Analogies,” in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2023, pp. 2426–2436. 

- [12] R. Li, S. Zheng, X. Cheng, Z. Zhang, S. Ji, and Z. Zhao, “MuVi: Video-to-Music Generation with Semantic Alignment and Rhythmic Synchronization,” arXiv preprint arXiv:2410.12957, 2024. 

- [13] Y.-B. Lin, Y. Tian, L. Yang, G. Bertasius, and H. Wang, “VMAs: Video-to-Music Generation via Semantic Alignment in Web Music Videos,” in Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (WACV), 2025. 

- [14] J. Kang, S. Poria, and D. Herremans, “Video2Music: Suitable Music Generation from Videos using an Affective Multimodal Transformer model,” Expert Systems with Applications, vol. 249, p. 123640, 2024. 

- [15] K. Su, J. Y. Li, Q. Huang, D. Kuzmin, J. Lee, C. Donahue, F. Sha, A. Jansen, Y. Wang, M. Verzetti, and T. I. Denk, “V2Meow: Meowing to the Visual Beat via Video-to-Music Generation,” in Proceedings of the AAAI Conference on Artificial Intelligence (AAAI), 2024, pp. 4952–4960. 

- [16] X. Liang, W. Li, L. Huang, and C. Gao, “DanceComposer: Dance-to-Music Generation Using a Progressive Conditional Music Generator,” IEEE Transactions on Multimedia, 2024. 

- [17] Y. Zhu, Y. Wu, K. Olszewski, J. Ren, S. Tulyakov, and Y. Yan, “Discrete Contrastive Diffusion for CrossModal Music and Image Generation,” in Proceedings of the International Conference on Learning Representations (ICLR), 2023. 

- [18] J. Yu, Y. Wang, X. Chen, X. Sun, and Y. Qiao, “Long-Term Rhythmic Video Soundtracker,” in Proceedings of the 40th International Conference on Machine Learning (ICML), 2023. 

- [19] J. Copet, F. Kreuk, I. Gat, T. Remez, D. Kant, G. Synnaeve, Y. Adi, and A. Défossez, “Simple and controllable music generation,” in Advances in Neural Information Processing Systems (NeurIPS), 2024. 

- [20] L. Lin, G. Xia, J. Jiang, and Y. Zhang, “Contentbased controls for music large language modeling,” in Proceedings of the International Society for Music Information Retrieval Conference (ISMIR), 2024. [Online]. Available: https://arxiv.org/abs/2310.17162 

- [21] H. F. Garcia, O. Nieto, J. Salamon, B. Pardo, and P. Seetharaman, “Sketch2sound: Controllable audio generation via time-varying signals and sonic imitations,” arXiv preprint arXiv:2402.13253, 2024. 

- [22] A. Guzhov, F. Raue, J. Hees, and A. Dengel, “Audioclip: Extending clip to image, text and audio,” in ICASSP 2022 - IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2022, pp. 976–980. 

- [23] C. Raffel, N. Shazeer, A. Roberts, K. Lee, S. Narang, M. Matena, Y. Zhou, W. Li, and P. J. Liu, “Exploring the limits of transfer learning with a unified text-to-text transformer,” Journal of Machine Learning Research, vol. 21, no. 140, pp. 1–67, 2020. 

360 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [24] Z. Tian, Z. Liu, R. Yuan, J. Pan, Q. Liu, X. Tan, Q. Chen, W. Xue, and Y. Guo, “Vidmuse: A simple video-to-music generation framework with long-shortterm modeling,” CVPR, 2025. 

- [25] R. Valenti, A. Jaimes, and N. Sebe, “Sonify Your Face: Facial Expressions for Sound Generation,” in Proceedings of the 2010 ACM Multimedia Workshop on Visual Media Interpretation and Understanding (VMIU), 2010. 

- [26] A. Clay, N. Couture, E. Decarsin, M. DesainteCatherine, P.-H. Vulliard, and J. Larralde, “Movement to emotions to music: using whole body emotional expression as an interaction for electronic music generation,” in Proceedings of the International Conference on New Interfaces for Musical Expression (NIME), 2012. 

- [27] J. Huang, X. Huang, L. Yang, and Z. Tao, “D2MNet for music generation jointly driven by facial expressions and dance movements,” Array, 2024. 

- [28] V. P, P. A, S. G. Vasist, S. Rao, and K. S. Srinivas, “DeepTunes: Music Generation based on Facial Emotions using Deep Learning,” in International Conference on Intelligent Computing and Technology (I2CT), 2022. 

- [29] J. Huang, X. Huang, L. Yang, and Z. Tao, “A Continuous Emotional Music Generation System Based on Facial Expressions,” in Proceedings of the International Conference on Intelligent Data (ICID), 2022. 

- [30] G. Research, “Musiclm: Generating music from text,” 2023, preprint available on arXiv. 

- [31] J. F. Gemmeke, D. P. W. Ellis, D. Freedman, A. Jansen, W. Lawrence, and R. C. Moore, “Audio set: An ontology and human-labeled dataset for audio events,” in 2017 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2017, pp. 776–780. 

- [32] H. Chen, W. Xie, A. Vedaldi, and A. Zisserman, “Vggsound: A large-scale audio-visual dataset,” in Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2020, pp. 721–725. 

- [33] L. Lin, G. Xia, Y. Zhang, and J. Jiang, “Arrange, inpaint, and refine: Steerable long-term music audio generation and editing via content-based controls,” in Proceedings of the 32nd International Joint Conference on Artificial Intelligence (IJCAI). IJCAI, 2024. 

- [34] Z. Cai, S. Ghosh, K. Stefanov, A. Dhall, J. Cai, H. Rezatofighi, R. Haffari, and M. Hayat, “Marlin: Masked autoencoder for facial video representation learning,” in CVPR. CVPR, 2023. 

- [35] X. W. R. E. Iashin, V. and A. Zisserman, “Synchformer: Efficient synchronization from sparse cues,” in ICASSP 2024-2024 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2024. 

- [36] Z. Teed and J. Deng, “Raft: Recurrent all-pairs field transforms for optical flow,” in European Conference on Computer Vision (ECCV). Springer, 2020, pp. 402–419. 

- [37] C. Tang, W. Yu, G. Sun, X. Chen, T. Tan, W. Li, L. Lu, Z. Ma, and C. Zhang, “Salmonn: Towards generic hearing abilities for large language models,” in Proceedings of the International Conference on Learning Representations (ICLR), 2024. 

- [38] A. Défossez, J. Copet, G. Synnaeve, and Y. Adi, “High fidelity neural audio compression,” 2022. [Online]. Available: https://arxiv.org/abs/2210.13438 

- [39] J. Kang, S. Poria, and D. Herremans, “Video2music: Suitable music generation from videos using an affective multimodal transformer model,” Expert Systems with Applications, vol. 249, p. 123640, Sep. 2024. [Online]. Available: http://dx.doi.org/10.1016/j. eswa.2024.123640 

- [40] K. Kilgour, R. Clark, K. Simonyan, and M. Sharifi, “Frechet audio distance: A reference-free metric for evaluating music enhancement algorithms,” in Interspeech, 2019, pp. 2350–2354. 

- [41] S. Hershey, S. Chaudhuri, D. P. W. Ellis, J. F. Gemmeke, A. Jansen, R. Moore, M. Plakal, D. Platt, R. A. Saurous, B. Seybold, M. Slaney, R. J. Weiss, and K. Wilson, “Cnn architectures for large-scale audio classification,” in IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2017, pp. 131–135. 

- [42] Q. Kong, Y. Cao, T. Iqbal, Y. Wang, W. Wang, and M. D. Plumbley, “Panns: Large-scale pretrained audio neural networks for audio pattern recognition,” IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 28, pp. 2880–2894, 2020. 

- [43] K. Koutini, H. Eghbal-zadeh, M. Widrich, J. Brandstetter, A. Thakur, V. Berenz, T. Mörwald, S. Hochreiter, and B. Hammer, “Efficient training of audio transformers with patchout,” in Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2022, pp. 874–878. 

- [44] T. Salimans, I. Goodfellow, W. Zaremba, V. Cheung, A. Radford, and X. Chen, “Improved techniques for training gans,” in Advances in Neural Information Processing Systems (NeurIPS), 2016, pp. 2234–2242. 

- [45] Y. Wu, K. Chen, T. Zhang, Y. Hui, M. Nezhurina, T. Berg-Kirkpatrick, and S. Dubnov, “Large-scale contrastive language-audio pretraining with feature 

361 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

fusion and keyword-to-caption augmentation,” in Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2023. [Online]. Available: https://arxiv.org/abs/2211. 06687 

- [46] B. Zhu, B. Lin, M. Ning, Y. Yan, J. Cui, H. Wang, Y. Pang, W. Jiang, J. Zhang, Z. Li, W. Zhang, Z. Li, W. Liu, and L. Yuan, “Languagebind: Extending video-language pretraining to n-modality by languagebased semantic alignment,” 2024. [Online]. Available: https://arxiv.org/abs/2310.01852 

362 

