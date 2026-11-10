---
paper_id: "000095"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706601/files/000095.pdf"
---

# JOINT OBJECT DETECTION AND SOUND SOURCE SEPARATION 

|Sunyoo Kim<sup>1</sup>|Yunjeong Choi<sup>1</sup>|Doyeon Lee<sup>1</sup>|Seoyoung Lee<sup>2</sup>|
|---|---|---|---|
|Eunyi Lyou<sup>1</sup>|Seungju Kim<sup>3</sup>|Junhyug Noh<sup>4∗</sup>|Joonseok Lee<sup>1∗</sup>|



1 Seoul National University, Seoul, Korea 2 University of Texas at Austin, Texas, USA 3 Sookmyung Women’s University, Seoul, Korea 4 Ewha Womans University, Seoul, Korea `meoignis@snu.ac.kr, junhyug@ewha.ac.kr, joonseok@snu.ac.kr` 

## ABSTRACT 

We propose See2Hear (S2H), a framework that jointly learns audio-visual representations for object detection and sound source separation from videos. Existing methods do not fully exploit the synergy between the detection and separation tasks, often relying on disjointly pre-trained visual encoders. Our S2H integrates both tasks in an endto-end trainable unified structure using transformer-based architectures. A naive combination of these approaches, however, results in suboptimal performance. We propose a dynamic filtering mechanism that selects relevant object queries from the object detector to resolve this issue. We conduct extensive experiments to verify that our approach achieves the state-of-the-art performance in audio source separation on MUSIC and MUSIC-21, while maintaining competitive object detection performance. Ablation studies confirm that the joint training of detection and separation is mutually beneficial for both tasks. 

## 1. INTRODUCTION 

Human perception is inherently multimodal, taking input signals from five senses and comprehensively understanding the given situation from their fusion. [1–3] Often, integrating multiple cues helps us to coherently understand our surroundings. Music is not an exception; for instance, seeing and recognizing a particular instrument simultaneously allows us to associate it with the sound it produces. More broadly, visual cues can be often useful to recognize co-occurring sound, and at the same time, auditory signals can also help to visually perceive an object. 

In literature, researchers have explored a wide range of audio-visual learning, including self-supervised crossmodal alignment [4, 5], audio-visual representation learning [6, 7], and sound source localization [8, 9]. These efforts collectively demonstrate that visual and auditory in- 

∗Corresponding authors 

© S. Kim, Y. Choi, D. Lee, S. Lee, E. Lyou, S. Kim, J. Noh, and J. Lee. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: S. Kim, Y. Choi, D. Lee, S. Lee, E. Lyou, S. Kim, J. Noh, and J. Lee, “Joint Object Detection and Sound Source Separation”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

formation, when processed jointly, can provide more robust perception than considering each modality alone. 

Among these research on audio-visual correspondence, our focus is on audio-visual sound source separation [10– 15], which aims to isolate individual sound sources from a complex mixture by exploiting the visual signal as an anchor. For instance, if multiple instruments are played together, seeing a violin or a trumpet often helps a model discern which frequency belongs to each instrument. 

Despite this clear connection between visual identification of a source and its auditory presence in the mixture, most prior approaches treat relevant visual tasks (e.g., object detection) and sound separation independently, or sequentially. Typically, one first uses a pre-trained detector to localize instruments, then feeds the bounding boxes or region features into a separate network for separation [11,14,15]. 

However, such two-step or disjoint pipelines do not take advantage of potentially useful cues from the other modalities; e.g., the visual signals for sound separation and vice versa. Considering that accurate object localization would provide guidance for better sound isolation and improved sound separation can also reinforce better visual representations by focusing on the most relevant object regions, disjointly tackling these two problems would be suboptimal. 

In this paper, we propose See2Hear (S2H), which jointly learns to detect objects and separate their corresponding audio signals, trained end-to-end. To achieve this, we adopt a Transformer-based architecture, wellsuited to seamlessly handle multimodal inputs with minimal modality-specific encoding overhead. Particularly, a multimodal Transformer enables direct attention across the audio and visual tokens, representing parts of the spectrogram and the image, respectively. We train both detection and separation in a single model, allowing gradients from both tasks to update the shared representation space. 

However, a naive assemble of visual and audio Transformers with cross-attention is not scalable. More specifically, we discover that it is crucial to control the number of reorganized objects. Without a proper measure, far more bounding boxes are detected than actual during training, making the weight updates less accurate and computationally infeasible. To resolve this issue, we incorporate a dynamic filtering mechanism that discards low-confidence or overlapping detections, thus avoiding confusion from spurious regions. As a result, our model effectively “sees” 

813 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

objects and “hears” their corresponding sounds in a fully integrated manner. 

Our experiments verify that this unified architecture effectively exploits synergy between the two tasks, surpassing the performance of methods that rely on external or pre-extracted detections [11,14,15]. 

Our main contributions are summarized as follows:<sup>1</sup> 

- We propose a novel unified framework that jointly learns object detection and audio-visual sound source separation end-to-end, allowing cross-task synergy. 

- We introduce a dynamic filtering of object queries, ensuring that only relevant objects guide the separation. 

- Our method achieves the state-of-the-art sound separation performance on MUSIC [10] and MUSIC-21 [16], while maintaining reasonable detection performance. Through comprehensive analysis, we highlight the benefit of jointly training the two tasks. 

## 2. RELATED WORK 

## 2.1 Audio Source Separation 

Audio source separation aims to isolate distinct sound sources from mixed signals. Classical approaches include Independent Component Analysis (ICA) [17–19]. ICAbased methods laid the foundation for blind source separation (BSS) under the assumption of statistical independence, while Non-negative Matrix Factorization (NMF) [20,21] introduced parts-based representations particularly suited for music. 

Deep learning revolutionized the field with approaches like Deep Clustering [22] and Deep Attractor Networks [23], which learn discriminative embeddings for source separation. U-Net architectures [24, 25] became standard for music separation through skip connections that refine signals in the time-frequency domain. 

Recent transformer-based methods have pushed stateof-the-art performance, with the Audio Spectrogram Transformer (AST) [26] demonstrating that attention mechanisms can effectively model both short and longrange dependencies. We adopt AST as our audio encoder backbone, extending it to audio-visual separation. 

## 2.2 Audio-Visual Sound Separation 

Audio-visual approaches leverage visual information to guide sound separation, significantly outperforming audioonly methods. The mix-and-separate paradigm introduced by Sound-of-Pixels [10] creates synthetic mixtures for selfsupervised learning. This approach was adapted by subsequent methods [5,10–15,27], including Co-Separation [11] that discovers audio-visual associations, and recursive separation methods [12]. 

Recent advances include Cyclic co-learning (CCoL) [13] that iteratively refines separation and localization, and AME [14] and TriBERT [28], which incorporate additional cues like motion and human pose. iQuery [15] uses 

> 1 Code available at `https://github.com/snuviplab/S2H` . 

visually-named audio queries in a cross-attention-based transformer to separate sources. Rahman and Sigal [29] proposed a weakly-supervised approach that learns audiovisual co-segmentation from videos labeled only with object labels. 

However, existing methods rely on pre-extracted visual features or pre-trained object detectors, creating a disconnect between visual analysis and audio separation. This two-stage approach introduces error propagation and prevents joint optimization of both tasks. Even recent diffusion-based methods like DAVIS [30] operate on preprocessed visual inputs rather than learning representations jointly with audio separation. 

## 2.3 Object Detection for Audio-Visual Tasks 

Object detection has evolved from region-based CNNs like R-CNN [31] and Faster R-CNN [32] to transformerbased approaches. DETR [33] revolutionized detection by treating it as a direct set prediction problem, eliminating hand-crafted components like anchor generation and non-maximum suppression. This end-to-end differentiability makes DETR particularly suitable for integration with other modalities. In audio-visual research, object detection primarily serves as preprocessing. Methods like Co-Separation [11] and iQuery [15] use pre-trained detectors to identify visual regions before separation. While recent work explores tighter integration between detection and audio processing in specific domains [34–36], most approaches still treat detection as a separate module. The potential of jointly training detection with audio-visual tasks remains largely unexplored, particularly for learning cross-modal associations directly rather than relying on pre-trained visual features. 

## 2.4 Joint Learning in Audio-Visual Tasks 

Traditional sequential pipelines suffer from error propagation and miss cross-modal interactions that could enhance both modalities. Recent speech domain advances demonstrate clear benefits: TDFNet [37] achieves 10% improvement through joint speaker feature learning, while IIANet [38] and DGFNet [39] show that integrating modalities throughout networks substantially outperforms late fusion. However, the music domain lags behind. While speech systems embrace joint learning, music source separation remains dominated by two-stage approaches – Music Gesture [40] and recent work [15] still use pre-extracted visual features. This gap is significant given music’s visual richness: instrument movements and spatial arrangements offer valuable cues better exploited through joint learning. The absence of end-to-end joint training in music separation represents a major opportunity that our S2H framework addresses through unified optimization of object detection and sound separation. 

## 3. PROBLEM FORMULATION 

We consider the object detection and sound source separation tasks simultaneously. Given a video V containing 

814 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
Audio Branch Spectrogram Decoder<br>Mixed audio Spectrogram<br>Mixed audio of spectrumSmiz reshape DecoderAudio embeddingSout<br>multiple objectsSmix STFT Da H × W × D<br>AudioEncoder Separated<br>masks<br>featureAudio Object featuresOutput NO × D H × W × N0M<br>A<br>NA × D<br>Audiovisual<br>frame Selected Decoder av<br>features<br>sampling VisualEncoderViualDecoder Dynamic filter F NO × DVf Cross attentionk4Audio-visual xL<br>Video with multiple objects<br>that make sound Self attention<br>V FN Lod True masks<br>Object query M<br>Visual Branch embeddingsQ × D pseudo-label Audio-visual Fusion<br><!-- End of picture text -->

Figure 1: Overview of our See2Hear (S2H) framework. Taking a video and its audio as input, unimodal branches (Sec. 4.1) first encode visual and audial features, respectively. Then, the Audio-visual fusion module (Sec. 4.2) produces multimodal-aware representations of the video, directly utilized to predict the spectrogram corresponding to each detected object in the video. The model is trained with two task-specific losses, one for the object detection (Lod) and another for the sound source separation (Lss). 

K objects that produce sound, the expected output of this task is a set of triples {(bi, si, ci) : i = 1, ..., K}, where bi ∈ [0, 1]<sup>4</sup> is the bounding box, si is the separated sound, and ci ∈C is the class label for each object i within the video. The sound s can be represented in multiple ways, including (mel-)spectrogram or the raw wave, and C is a set of pre-defined classes, e.g., musical instruments. 

We emphasize that our goal is to train a single model that performs both object detection and sound source separation tasks end-to-end, assuming that solving these two tasks would require common cues and provide useful information to each other. 

## 4. PROPOSED APPROACH 

In this section, we detail our proposed framework, namely See2Hear (S2H), which integrates object detection and audio-visual sound separation in a unified end-to-end transformer-based architecture. Fig. 1 overviews our proposed framework for joint training of object detection and sound separation, composed of unimodal encoders (the visual object detection branch and the audio branch; Sec. 4.1) and multimodal decoders (audio-visual feature fusion module and the final spectrogram decoder; Sec. 4.2). 

## 4.1 Modality-specific Encoders 

forward network (FFN), their bounding boxes (bq) and class labels (cq) are predicted for q ∈{1, ..., Q}. 

However, among these Q query embeddings, we observe that many represent the background or duplicate objects multiple times. To avoid confusing the audio-visual decoder with irrelevant objects, we filter out irrelevant query embeddings in several ways; e.g., we exclude bounding boxes that overlap by more than θ in the intersection over union (IoU), or apply Non-Maximum Suppression (NMS) to keep only one with the highest confidence (confidence thresholding). We also keep only one bounding box with the highest confidence for each object class in a frame, if multiple boxes share the same predicted label. This dynamic filtering helps the model focus on key objects, avoiding spurious bounding boxes that could degrade separation. We denote by NO the number of remaining object query embeddings across all frames. They are concatenated to form Vf ∈ R<sup>NO×D</sup> , and passed to the audio-visual decoder, described in Sec 4.2. 

Audio Branch. We encode the input audio signal, composed of sounds from multiple sources, using a transformer-based architecture (e.g., AST [26]) from its log-mel spectrogram. Similarly to the visual branch, we obtain a sequence of audio token embeddings A ∈ R<sup>NA×D</sup> , where NA denotes the number of query embeddings across the entire spectrogram, and it is passed to the audio-visual decoder in Sec 4.2. 

Visual Branch. Given an input video V, F frames are uniformly sampled. Then, an object detector encodes the visual signals. Adopting a transformer-based architecture (e.g., DETR [33]), the visual encoder and decoder in Fig. 1 produce intermediate visual representations called query embeddings for Q detected objects. Through a feed- 

## 4.2 Audio-Visual Fusion and Decoders 

We now elaborate the core module of our S2H framework – the audio-visual decoder – which fuses the extracted visual object and audio features, followed by the spectrogram decoding process. 

815 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

Audio-Visual Fusion. After detecting objects in the visual branch and extracting audio tokens from the audio branch, we fuse them via a transformer audio-visual decoder. As shown in Fig. 1, the audio-visual decoder Dav takes the final filtered set of visual query embeddings, Vf ∈ R<sup>NO×D</sup> , as the decoder queries, and the audio tokens, A ∈ R<sup>NA×D</sup> , as the keys and values. Composed of multiple (L) transformer decoder layers, which perform self-attention over Vf to capture interactions among the object queries, followed by cross-attention with the audio tokens A, it produces the updated object features O ∈ R<sup>NO×D</sup> , where NO is the total number of object query embeddings across all frames. These features are aware of the audial signals as well as visual ones. 

Spectrogram Decoder. Finally, we produce a fullresolution sound mask corresponding to each detected object using a light-weight upsampling audio decoder Da illustrated in Fig. 1. It takes as input the encoded audio features A ∈ R<sup>NA×D</sup> , reshaped back to a 2D feature map, and yields a spectrogram embedding Sout ∈ R<sup>H×W ×D</sup> , matching the size of the input spectrogram. We then fuse the object embedding Oo ∈ R<sup>D</sup> for a particular object o with Sout to obtain its mask: 



<!-- Start of picture text -->
Mˆ o = σ(Oo ⊗ Sout), (1)<br><!-- End of picture text -->

where ⊗ denotes a dot product at each spatial location, and σ is the sigmoid function. 

At inference, this predicted mask M<sup>ˆ</sup> o is multiplied with the input spectrogram (with multiple sound sources) to separate out the sound corresponding to the particular object o. 

## 4.3 Model Training 

We optimize two main losses end-to-end: object detection loss and sound separation loss. This end-to-end training encourages synergy: bounding box refinement benefits from audio constraints, and audio separation benefits from robust visual grounding. 

Object Detection Loss. We apply the set prediction loss [33], which involves bipartite matching between the Q predicted queries and ground-truth bounding boxes. Denoting pˆq and<sup>ˆ</sup> bq be the predicted class probability and bounding box for the query q, and c<sup>∗</sup> q<sup>and b∗</sup> q<sup>be the matched</sup> ground truth label and box, the loss is defined as 



<!-- Start of picture text -->
Q<br>Lod = ��− log ˆpq(c ∗ q ) + 1 {c ∗ q̸ =∅} λL1∥ˆbq − b q ∗∥1<br>q=1<br>+ 1{c∗q̸ =∅} λgiou �1 − GIoU( ˆ bq, b ∗ q ) � � , (2)<br><!-- End of picture text -->

where λL1 and λgiou control the relative weighting of L1 and GIoU losses for the bounding box regression. 

Sound Separation Loss. For each video, we minimize the L1 distance between the predicted and ground truth spectrogram corresponding to each object in it: 



<!-- Start of picture text -->
Lss = � ∥M ˆ o − Mo∥1, (3)<br>o<br><!-- End of picture text -->

where Mo is the true audio spectrogram produced by the object o within in the video, and M<sup>ˆ</sup> o is its prediction. As the training set does not provide the true per-source sound spectrogram, pseudo-ground truth can be adopted for this loss. (See Sec. 5.1 for our experimental settings.) 

Overall Objective. The overall objective is given by 



<!-- Start of picture text -->
L = Lss + λ Lod (4)<br><!-- End of picture text -->

where λ is a hyperparameter. The sound source separation loss Lss backpropagate all the way through the shared visual and audio transformers, enabling synergy between detection and separation. Although Lod only flows within the visual branch, the bounding box predictions it refines lead to more precise object queries for cross-attention, thereby indirectly improving the audio representation learned via Lss. This synergy fosters better separation and detection. 

## 5. EXPERIMENTS 

## 5.1 Experimental Settings 

Datasets. We evaluate our model on MUSIC [10] and MUSIC-21 [16]. MUSIC contains 685 solo and duet videos with 11 musical instrument categories, of which 637 are currently available. MUSIC-21 extends it to 1,365 solo videos with 21 instruments, and 1,040 videos are currently available. 

We follow the standard protocol [10] of setting aside the first video of each class for validation and the second one for test, leaving the rest to form the training set. 

Evaluation Protocol. Since no publicly available dataset provides ground truth labels for sound source separation, we follow the widely-used mix-and-separate paradigm [5, 10–15, 27] for training. Specifically, we randomly sample M videos {(V<sup>(m)</sup> , s<sup>(m)</sup> )}<sup>M</sup> m=1<sup>fromthetrainingdataand</sup> mix their audio by smix =<sup>�M</sup> m=1<sup>s(m).Wedenoteits</sup> spectrogram by Smix. We take the normalized mask of each video m as its ground-truth mask: 



<!-- Start of picture text -->
S (m)<br>M (m) = (5)<br>� m ′ S(m′)  ,<br><!-- End of picture text -->

where S<sup>(m)</sup> is the spectrogram of s<sup>(m)</sup> and the division is performed element-wise. 

Since the MUSIC and MUSIC-21 datasets do not provide bounding-box annotations for object detection, we obtain pseudo-ground truth boxes in each frame using a well-established open-vocabulary detector, following prior works [15]. Specifically, we adopt Detic [41], which is capable of detecting arbitrary categories when provided with a text prompt. To generate the training samples, we perform inference on each frame with a relevant instrument prompt (e.g., “guitar”, “violin”, “flute”, “saxophone”, and so on) and take the predicted bounding boxes with confidence score ≥ 0.7. If there are more than one bounding boxes with IoU ≥ 0.7, we take the maximal one only. These box predictions then serve as pseudo-labels to train our visual branch. 

816 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

Data Preprocessing. We sample F = 3 frames per video with a stride of 1 and a video sampling rate of 1 fps, and resize each frame to a maximum side length of 256 pixels while preserving aspect ratio. For the audio input, we sample 6 seconds of the input audio at 11 kHz, centered at the middle of each sampled frame. We apply Short-Time Fourier Transform (STFT) with a window size of 1,022 and hop length of 256, resulting in a 512 × 256 complex spectrogram, which is then resampled on a log-frequency scale to 256 × 256. The phase information is preserved for reconstruction. 

Backbone Models. For the visual branch, we use DETR [33] as a set-based object detector to predict bounding boxes and class probabilities. It has a ResNet backbone [31] that extracts feature maps, which are then flattened and passed to a transformer encoder. The hyperparameter Q is usually set as the maximally expected number of objects in a frame, and we use Q = 12 for MUSIC and Q = 22 for MUSIC-21, reserving one query as the background class. 

For the audio branch, we adopt AST [26], a transformer-based audio classifier, given a log-mel spectrogram of size F ×T . While AST was originally designed for classification, we use it to obtain a sequence of patch embeddings A ∈ R<sup>NA×D</sup> , dropping the classification token. 

Baselines. We compare our S2H with the state-of-the-art sound separation models, iQuery [15], Sound-of-Pixels (SoP) [10], and CoSep [11]. Since the number of available videos varies depending on the access time, we re-train all baselines on the same set of currently available videos to ensure a fair comparison. 

Evaluation Metrics. The sound separation task is evaluated using Source-to-Distortion Ratio (SDR), Source-toInterference Ratio (SIR), and Source-to-Artifacts Ratio (SAR). For object detection, we measure the mean Average Precision (mAP) and mean Intersection over Union (mIoU). 

Implementation Details. We use 6 encoder and decoder layers for the visual encoder, respectively. For the audio encoder, we use the first 6 layers of a pre-trained AST model. We grid-search λ by cross-validation and set it to 0.1. We set the bounding box overlap threshold θ = 0.7. 

We train for 100 epochs using the AdamW optimizer with a batch size of 48, decaying the learning rate at epoch 80 by a factor of 0.1. The learning rates are set to 1 × 10<sup>−5</sup> for the visual backbone, 2 × 10<sup>−5</sup> for the DETR encoder and decoder, 5 × 10<sup>−5</sup> for the AST audio encoder, and 1 × 10<sup>−4</sup> for the audio-visual decoder and the audio decoder. We mix 2 soundtracks per mini-batch, leading to up to 4 distinct instruments in the mixture. 

## 5.2 Comparison with Competing Methods 

Tab. 1 shows the results on MUSIC (left) and MUSIC21 (right). Our S2H outperforms existing baselines in sound separation, achieving higher SDR, SIR, and SAR. The improvement in SDR is particularly substantial (gains 

|Method|SDR|MUSIC<br>SIR|SAR|SDR|MUSIC-2<br>SIR|1<br>SAR|
|---|---|---|---|---|---|---|
|Sound-of-Pixels|5.63|6.85|9.80|5.77|9.95|10.33|
|CoSep|5.72|8.00|8.13|6.17|8.73|10.18|
|iQuery|8.04|11.63|11.92|7.51|11.16|11.64|
|S2H (Ours)|9.03|12.85|13.99|9.20|12.54|14.79|



Table 1: Sound separation performance of competing models. On MUSIC [10] and MUSIC-21 [16], S2H achieves state-of-the-art separation metrics. 

of about +2dB over iQuery [15] on MUSIC). We attribute this to the explicit synergy between object detection and sound separation in our architecture. 

Fig. 2 further illustrates this improvement with qualitative examples. In a duet video with flute and violin, S2H accurately localizes both instruments and reconstructs their individual spectrograms with minimal interference. 

## 5.3 Ablation Studies 

We perform ablations on MUSIC to isolate key design choices in S2H. Tab. 2 summarizes the results. 

- (1) Effect of Bounding Box Filtering. We compare the performance of our full model to the one without the dynamic bounding box filtering described in Sec. 4.1. The performance significantly drops, e.g., from 9.03 to 8.19 for sound source separation (in SDR) and from 0.67 to 0.54 for object detection (in mAP). Without filtering, many low-confidence or heavily duplicate bounding boxes are passed to the audio-visual decoder, confusing the model during the fusion step, as they contain object queries that do not correspond to any true sounding object. Interestingly, the mIoU remains fairly high (0.85) even without the bounding box filtering, suggesting that some boxes are spatially correct, yet the sheer number of boxes for the same object degrades both detection precision and separation quality. 

- (2) Effect of Cross-modal Fusion. Our proposed S2H introduces cross-modal fusion, aiming to create synergy between the object detection and sound separation tasks. In order to see the effect of this design, we compare with a simpler U-Net-based decoder structure, which has been widely used in audio source separation, instead of our transformer-based cross-attention. With this design, the visual branch simply yields a latent feature (instead of bounding-box queries), then concatenated with audio features. We observe a drastic performance drop in sound source separation metrics (e.g., 9.03 → 2.34 in SDR). This highlights the benefit of our transformer-based cross-attention, which allows explicit object-aware fusion between the boundingbox queries and the spectrogram embeddings. 

- (3) Effect of Cross-attention. Instead of completely replacing the audio-visual fusion with a U-Net, we further experiment with our audio-visual fusion only with self-attention to see the effect of cross-modal attention. 

817 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
(a) Detection Results (b) Ground Truth (c) Ours (d) SoP (e) iQuery<br>Video #1<br>Video #2<br>Video #1<br>Video #2<br><!-- End of picture text -->

Figure 2: Qualitative examples of object detection and sound source separation. (a) Predicted bounding boxes in a sampled video frame. (b) Ground-truth spectrogram of the source audio. (c)–(e) The separated spectrogram by our and baseline methods. 

As each modality is independently processed, the performance drops sharply (9.03 → 5.22 in SDR), reaffirming the benefits of cross-modal interaction. Similarly, the detection metrics (mAP and mIoU) also degrade, since the visual branch no longer receives indirect supervision signals from the separation loss. 

- (4) Effect of Joint Training. We remove the detection loss by setting λ = 0 in Eq. (4), effectively discarding the detection supervision. Although the visual branch still encodes the visual features, it has no further incentive to localize objects or refine bounding-box predictions tailored to sound source separation. In this scenario, the detection performance drops to 0, showing that the bounding boxes degenerate immediately. The sound separation quality is also reduced (SDR 9.03 → 7.67), indicating that accurate object localization significantly helps the sound separation task. This underscores the synergy between detection and separation. 

## 6. CONCLUSION 

We present See2Hear (S2H), a novel framework that jointly learns object detection and sound source separation. By leveraging transformer-based modules both for the visual and audio branches, and by integrating them through a shared audio-visual decoder, S2H captures richer crossmodal dependencies than previous disjoint or sequential 

|Configuration|Soun<br>SDR|d Separ<br>SIR|ation<br>SAR|Dete<br>mAP|ction<br>mIoU|
|---|---|---|---|---|---|
|Full S2H|9.03|12.85|13.99|0.67|0.80|
|(1) No b-box filtering|8.19|11.17|14.80|0.54|0.85|
|(2) U-Net-like decoder|2.34|8.33|5.94|0.25|0.84|
|(3) No cross-attention|5.22|8.67|12.54|0.32|0.82|
|(4) NoLod loss|7.67|11.05|13.49|0.00|0.00|



Table 2: Ablation studies on MUSIC. Each component significantly contributes to the performance of S2H, for both sound source separation and object detection. 

methods. Our dynamic filtering mechanism ensures that only relevant detections guide separation. Extensive experiments on MUSIC and MUSIC-21 demonstrate that S2H achieves the state-of-the-art sound separation performance, while also maintaining competitive detection accuracy. Our ablation studies confirm that object detection and sound separation indeed mutually benefit each other when trained end-to-end. 

In spite of the promising results, S2H still has some limitations. Mainly due to the lack of labeled data for sound source separation, S2H has been verified mostly on single instrument scenes. With a larger scaled data, it could be extended to multi-instrument scenes with more complex polyphony. Also, as its application is not confined to musical audio, it could be applied to other multimodal tasks (e.g., speech-driven detection or action recognition). 

818 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

Acknowledgments. This work was supported by Youlchon Foundation, NRF (RS-2021-NR05515, RS-202400336576, RS-2023-0022663) and IITP grants (RS2022-II220264, RS-2024-00353131, RS-2022-00155966) funded by the government of Korea. 

## 7. REFERENCES 

- [1] C. Opoku-Baah, A. M. Schoenhaut, S. G. Vassall, D. A. Tovar, R. Ramachandran, and M. T. Wallace, “Visual influences on auditory behavioral, neural, and perceptual processes: a review,” Journal of the Association for Research in Otolaryngology, vol. 22, no. 4, pp. 365–386, 2021. 

- [2] A. Tonelli, L. F. Cuturi, and M. Gori, “The influence of auditory information on visual size adaptation,” Frontiers in Neuroscience, vol. 11, p. 594, 2017. 

- [3] Q. Huang, A. Jansen, J. Lee, R. Ganti, J. Y. Li, and D. P. Ellis, “MuLan: A joint embedding of music audio and natural language,” in Proceedings of the 23rd International Society for Music Information Retrieval Conference (ISMIR), 2022. 

- [4] R. Arandjelovi´c and A. Zisserman, “Look, listen and learn,” in Proceedings of the IEEE International Conference on Computer Vision (ICCV), 2017. 

- [5] A. Owens and A. A. Efros, “Audio-visual scene analysis with self-supervised multisensory features,” in Proceedings of the European Conference on Computer Vision (ECCV), 2018. 

- [6] Y. Aytar, C. Vondrick, and A. Torralba, “SoundNet: Learning sound representations from unlabeled video,” in Advances in Neural Information Processing Systems (NeurIPS), 2016. 

- [7] T. Afouras, A. Owens, J. S. Chung, and A. Zisserman, “Self-supervised learning of audio-visual objects from video,” in Proceedings of the European Conference on Computer Vision (ECCV), 2020. 

- [8] A. Senocak, T.-H. Oh, J. Kim, M.-H. Yang, and I. S. Kweon, “Learning to localize sound source in visual scenes,” in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2018. 

- [9] K. Qian, Y. Zhang, S. Chang, D. Cox, and M. Hasegawa-Johnson, “Unsupervised speech decomposition via triple information bottleneck,” in Proceedings of the 37th International Conference on Machine Learning (ICML), 2020. 

- [10] H. Zhao, C. Gan, A. Rouditchenko, C. Vondrick, J. McDermott, and A. Torralba, “The sound of pixels,” in Proceedings of the European Conference on Computer Vision (ECCV), 2018. 

- [11] R. Gao and K. Grauman, “Co-separating sounds of visual objects,” in Proceedings of the IEEE International Conference on Computer Vision (ICCV), 2019. 

- [12] X. Xu, B. Dai, and D. Lin, “Recursive visual sound separation using minus-plus net,” in Proceedings of the IEEE International Conference on Computer Vision (ICCV), 2019. 

- [13] Y. Tian, D. Hu, and C. Xu, “Cyclic co-learning of sounding object visual grounding and sound separation,” in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2021. 

- [14] L. Zhu and E. Rahtu, “Visually guided sound source separation and localization using self-supervised motion representations,” in Proceedings of the IEEE Winter Conference on Applications of Computer Vision (WACV), 2022. 

- [15] J. Chen, R. Li, Z. Hou, G. Zhang, L. Peng, and C.-W. Ngo, “iQuery: Instruments as queries for audio-visual sound separation,” in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2023. 

- [16] H. Zhao, C. Gan, W.-C. Ma, and A. Torralba, “The sound of motions,” in Proceedings of the IEEE International Conference on Computer Vision (ICCV), 2019. 

- [17] J.-F. Cardoso, “Blind signal separation: Statistical principles,” Proceedings of the IEEE, vol. 86, no. 10, pp. 2009–2025, 1998. 

- [18] A. J. Bell and T. J. Sejnowski, “An informationmaximization approach to blind separation and blind deconvolution,” Neural Computation, vol. 7, no. 6, pp. 1129–1159, 1995. 

- [19] A. Hyvärinen and E. Oja, “Independent component analysis: Algorithms and applications,” Neural Networks, vol. 13, no. 4-5, pp. 411–430, 2000. 

- [20] D. D. Lee and H. S. Seung, “Learning the parts of objects by non-negative matrix factorization,” Nature, vol. 401, no. 6755, pp. 788–791, 1999. 

- [21] P. Smaragdis and J. C. Brown, “Non-negative matrix factorization for polyphonic music transcription,” in IEEE Workshop on Applications of Signal Processing to Audio and Acoustics, 2003. 

- [22] J. R. Hershey, Z. Chen, J. Le Roux, and S. Watanabe, “Deep clustering: Discriminative embeddings for segmentation and separation,” in Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2016. 

- [23] Z. Chen, Y. Luo, and N. Mesgarani, “Deep attractor network for single-microphone speaker separation,” in Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2017. 

819 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [24] A. Jansson, E. J. Humphrey, N. Montecchio, R. Bittner, A. Kumar, and T. Weyde, “Singing voice separation with deep u-net convolutional networks,” in Proceedings of the 18th International Society for Music Information Retrieval Conference (ISMIR), 2017. 

- [25] D. Stoller, S. Ewert, and S. Dixon, “Wave-u-net: A multi-scale neural network for end-to-end audio source separation,” in Proceedings of the 19th International Society for Music Information Retrieval Conference (ISMIR), 2018. 

- [26] Y. Gong, Y.-A. Chung, and J. Glass, “AST: Audio spectrogram transformer,” in Proceedings of the Interspeech Conference, 2021. 

- [27] A. Ephrat, I. Mosseri, O. Lang, T. Dekel, K. Wilson, A. Hassidim, W. T. Freeman, and M. Rubinstein, “Looking to listen at the cocktail party: A speakerindependent audio-visual model for speech separation,” ACM Transactions on Graphics (TOG), vol. 37, no. 4, pp. 112:1–112:11, 2018. 

- [28] T. Rahman, M. Yang, and L. Sigal, “TriBERT: Humancentric audio-visual representation learning,” in Advances in Neural Information Processing Systems (NeurIPS), 2021. 

- [29] T. Rahman and L. Sigal, “Weakly-supervised audiovisual sound source detection and separation,” in IEEE International Conference on Multimedia and Expo (ICME), 2021. 

- [30] C. Huang, S. Liang, Y. Tian, A. Kumar, and C. Xu, “DAVIS: High-quality audio-visual separation with generative diffusion models,” arXiv preprint arXiv:2308.00122, 2023. 

   - [35] S. Mo and Y. Tian, “Audio-visual grouping network for sound localization from mixtures,” in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2023. 

   - [36] H. Chen, W. Xie, A. Vedaldi, and A. Zisserman, “Localizing visual sounds the hard way,” in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2021. 

   - [37] S. Pegg, K. Li, and X. Hu, “TDFnet: An efficient audio-visual speech separation model with top-down fusion,” in International Conference on Information Science and Technology, 2023. 

   - [38] K. Li, X. Hu, S. Pegg, R. Zhang, F. Zhou, X. Wu, and X. Liu, “IIAnet: An intra- and inter-modality attention network for audio-visual speech separation,” in Proceedings of the 41st International Conference on Machine Learning (ICML), 2024. 

   - [39] Y. Yu and S. Sun, “DGFnet: End-to-end audio-visual source separation based on dynamic gating fusion,” in Proceedings of the International Conference on Multimedia Retrieval (ICMR), 2025. 

   - [40] C. Gan, D. Huang, H. Zhao, J. B. Tenenbaum, and A. Torralba, “Music gesture for visual sound separation,” in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2020. 

   - [41] X. Zhou, R. Girdhar, A. Joulin, P. Krähenbühl, and I. Misra, “Detecting twenty-thousand classes using image-level supervision,” in Proceedings of the European Conference on Computer Vision (ECCV), 2022. 

- [31] R. Girshick, J. Donahue, T. Darrell, and J. Malik, “Rich feature hierarchies for accurate object detection and semantic segmentation,” in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2014. 

- [32] S. Ren, K. He, R. Girshick, and J. Sun, “Faster R- CNN: Towards real-time object detection with region proposal networks,” in Advances in Neural Information Processing Systems (NeurIPS), 2015. 

- [33] N. Carion, F. Massa, G. Synnaeve, N. Usunier, A. Kirillov, and S. Zagoruyko, “End-to-end object detection with transformers,” in Proceedings of the European Conference on Computer Vision (ECCV), 2020. 

- [34] F. R. Valverde, J. V. Hurtado, and A. Valada, “There is more than meets the eye: Self-supervised multi-object detection and tracking with sound by distilling multimodal knowledge,” in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2021. 

820 

