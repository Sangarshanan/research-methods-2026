---
paper_id: "000022"
year: 2022
title: "Download pdf"
source_url: "https://zenodo.org/record/7316628/files/000022.pdf"
---

# JUKEDRUMMER: CONDITIONAL BEAT-AWARE AUDIO-DOMAIN DRUM ACCOMPANIMENT GENERATION VIA TRANSFORMER VQ-VAE 

Yueh-Kao Wu Ching-Yu Chiu Yi-Hsuan Yang Academia Sinica National Cheng Kung University Taiwan AI Labs yk.lego09@gmail.com x2009971@gmail.com yhyang@ailabs.tw 

## ABSTRACT 

This paper proposes a model that generates a drum track in the audio domain to play along to a user-provided drumfree recording. Specifically, using paired data of drumless tracks and the corresponding human-made drum tracks, we train a Transformer model to improvise the drum part of an unseen drumless recording. We combine two approaches to encode the input audio. First, we train a vectorquantized variational autoencoder (VQ-VAE) to represent the input audio with discrete codes, which can then be readily used in a Transformer. Second, using an audiodomain beat tracking model, we compute beat-related features of the input audio and use them as embeddings in the Transformer. Instead of generating the drum track directly as waveforms, we use a separate VQ-VAE to encode the mel-spectrogram of a drum track into another set of discrete codes, and train the Transformer to predict the sequence of drum-related discrete codes. The output codes are then converted to a mel-spectrogram with a decoder, and then to the waveform with a vocoder. We report both objective and subjective evaluations of variants of the proposed model, demonstrating that the model with beat information generates drum accompaniment that is rhythmically and stylistically consistent with the input audio. 

## 1. INTRODUCTION 

Deep generative models for musical audio generation have witnessed great progress in recent years [1±8]. While models for generating symbolic music such as MIDI [9±12] or musical scores [13] focus primarily on the composition of musical content, an audio-domain music generation model deals with sounds and thereby has extra complexities related to timbre and audio quality. For example, while a model for generating symbolic guitar tabs can simply consider a guitar tab as a sequence of notes [11], a model that generates audio recordings of guitar needs to determine not only the underlying sequence of notes but also the way to render (synthesize) the notes into sounds. Due to the complexities involved, research on deep generative models for 

© Y.-K. Wu, C.-Y. Chiu, and Y.-H. Yang. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: Y.-K. Wu, C.-Y. Chiu, and Y.-H. Yang, ªJukeDrummer: Conditional Beat-aware Audio-Domain Drum Accompaniment Generation via Transformer VQ-VAEº, in Proc. of the 23rd Int. Society for Music Information Retrieval Conf., Bengaluru, India, 2022. 

musical audio begins with the simpler task of synthesizing individual musical notes [1±3], dispensing the need to consider the composition of notes. Follow-up research [4±6] extends the capability to generating musical passages of a single instrument. The Jukebox model [7] proposed by OpenAI greatly advances the state-of-the-art by being able to, quoting their sentence, ªgenerate high-fidelity and diverse songs with coherence up to multiple minutes.º Being trained on a massive collection of audio recordings with the corresponding lyrics but not the symbolic transcriptions of music, Jukebox generates multi-instrument music as raw waveforms directly without an explicit model of the underlying sequence of notes. 

This work aims to improve upon Jukebox in two aspects. First, the backbone of Jukebox is a hundred-layer Transformer [14, 15] with billions of parameters that are trained with 1.2 million songs on hundreds of NVIDIA V100 GPUs for weeks at OpenAI, which is hard to reproduce elsewhere. Inspired by a recent Jukebox-like model for singing voice generation called KaraSinger [8], we instead build a light-weight model with only 25 million parameters by working on Mel-spectrograms instead of raw waveforms. Our model is trained with only 457 recordings on a single GeForce GTX 1080 Ti GPU for 2 days. 

Second, and more importantly, instead of a fully autonomous model that makes a song from scratch with various instruments, we aim to build a model that can work cooperatively with human, allowing the human partner to come up with the musical audio of some instruments as input to the model, and generating in return the musical audio of some other instruments to accompany and to complement the user input, completing the song together. Such a model can potentially contribute to human-AI co-creation in songwriting [16] and enable new applications. 

In technical terms, our work enhances the controllability of the model by allowing its generation to be steered on a user-provided audio track. It can be viewed as an interesting sequence-to-sequence problem where the model creates a ªtarget sequenceº of music that is to be played along to the input ªsource sequence.º Besides requirement on audio quality, the coordination between the source and target sequences in terms of musical aspects such as style, rhythm, and harmony is also of central importance. 

We note that, for controllability and the intelligibility of the generated singing, both Jukebox [7] and KaraSinger [8] have a lyrics encoder that allows their generation to be steered on textual lyrics. While being technically similar, 

193 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

our accompaniment generation task (ªaudio-to-audioº) is different from the lyric-conditioned generation task (ªtextto-audioº) in that the latter does not need to deal with the coordination between two audio recordings. 

Specifically, we consider a drum accompaniment generation problem in our implementation, using a ªdrumlessº recording as the input and generating as the output a drum track that involves the use of an entire drum kit. We use this as an example task to investigate the audio-domain accompaniment generation problem out of the following reasons. First, datasets used in musical source separation [17] usually consist of an isolated drum stem along with stems corresponding to other instruments. We can therefore easily merge the other stems to create paired data of drumless tracks and drum tracks as training data of our model. (In musical terms, drumless, or ªMinus Drumsº songs are recordings where the drum part has been taken out, which corresponds nicely to our scenario.) Second, we suppose a drum accompaniment generation model can easily find applications in songwriting [18], as it allows a user (who may not be familiar with drum playing or beat making) to focus on the other non-drum tracks. Third, audio-domain drum accompaniment generation poses interesting challenges as the model needs to determine not only the drum patterns but also the drum sounds that are supposed to be, respectively, rhythmically and stylistically consistent with the input. Moreover, the generated drum track is expected to follow a steady tempo, which is a basic requirement for a human drummer. We call our model the ªJukeDrummer.º 

As depicted in Figure 1, the proposed model architecture contains an ªaudio encoderº (instead of the original text encoder [7, 8]) named the drumless VQ encoder that takes a drum-free audio as input. Besides, we experiment with different ways to capitalize an audio-domain beat and downbeat tracking model proposed recently [19] in a novel beat-aware module that extracts beat-related information from the input audio, so that the language model for generation (i.e., the Transformer) is better informed of the rhythmic properties of the input. The specific model [19] was trained on drumless recordings as well, befitting our task. We extract features from different levels, including lowlevel tracker embeddings, mid-level activation peaks, and high-level beat/downbeat positions, and investigate which one benefits the generation model the most. 

Our contribution is four-fold. First, to our best knowledge, this work represents the first attempt to drum accompaniment generation of a full drum kit given drum-free mixed audio. Second, we develop a light-weight audio-toaudio Jukebox variant that takes an input audio of up to 24 seconds as conditioning and generates accompanying music in the domain of Mel-spectrograms (Section 3). Third, we experiment with different beat-related conditions in the context of audio generation (Section 4). Finally, we report objective and subjective evaluations demonstrating the effectiveness of the proposed model (Sections 6 & 7).<sup>1</sup> . 

> 1 We share our code and checkpoint at: https://github.com/ legoodmanner/jukedrummer. Moreover, we provide audio examples at the following demo page: https://legoodmanner. github.io/jukedrummer-demo/ 



<!-- Start of picture text -->
Drumless<br>Audio<br>Mel Extractor<br>Drumless<br>VQ Encoder<br>Language Model<br>Beat-aware Module<br>Drum<br>VQ Decoder<br>Vocoder<br>JUKEDRUMMER<br>Drum<br>Accompaniment<br><!-- End of picture text -->

Figure 1: Diagram of the proposed JukeDrummer model for the inference stage. The training stage involves learning additional Drum VQ Encoder and Drumless VQ Decoder (see Figure 2) that are not used at inference time. 

## 2. BACKGROUND 

## 2.1 Related Work on Drum Generation 

Conditional drum accompaniment generation has been studied in the literature, but only in the symbolic domain [20, 21], to the best of our knowledge. Dahale et al. [20] used a Transformer encoder to generate an accompanying symbolic drum pattern of 12 bars given a four-track, melodic MIDI passage. Makris et al. [21] adopted instead a sequence-to-sequence architecture with a bi-directional long short-term memory (BLSTM) encoder extracting information from the melodic input and a Transformer decoder generating the drum track for up to 16 bars in MIDI format. While symbolic-domain music generation has its own challenges, it differs greatly from the audio-domain counterpart studied in this paper, for it is not about generating sounds that can be readily listened to by human. 

Related tasks that have been attempted in the literature with deep learning include symbolic-domain generation of a monophonic drum track (i.e., kick drum only) of multiple bars [4], symbolic-domain drum pattern generation [22±25], symbolic-domain drum track generation as part of a multi-track MIDI [26±29], audio-domain one-shot drum hit generation [30±34], audio-domain generation of drum sounds of an entire drum kit of a single bar [35], and audio-domain drum loop generation [36]. Jukebox [7] generates a mixture of sounds that include drums, but not an isolated drum track. By design, Jukebox does not take any input audio as a condition and generate accompaniments. 

## 2.2 The Original Jukebox model 

The main architecture of Jukebox [7] is composed of two components: a multi-scale vector-quantized variational autoencoder (VQ-VAE) [37±41] and an autoregressive Transformer decoder [14,15]. The VQ-VAE is for converting a continuous-valued raw audio waveform into a sequence of so-called discrete VQ codes, while the Transformer establishes a language model (LM) of the VQ codes capable of generating new code sequences. 

194 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
Drum sounds codebook<br>Drum VQ Drum VQ De-<br>Encoder<br>Drum-less sounds codebook<br>Drumless Drumless<br>VQ Encoder VQ Decoder<br><!-- End of picture text -->

Figure 2: We use separate VQ-VAEs for the drumless and drum tracks, both operating on the Mel-spectrograms. 

Specifically, VQ-VAE consists of an encoder and a decoder, referred to as the VQ-VAE encoder E and VQ-VAE decoder D below, respectively. Given an audio waveform x ∈ R<sup>1×N</sup> , where N denotes the number of audio samples (e.g., N = 1,058,400 for a 24-second audio clip sampled at 44.1 kHz), the VQ-VAE encoder would convert x into a sequence of latent vectors {ht ∈ R<sup>D</sup> , t = 1, ..., T }, where the sequence length T is proportional to N , and the VQ-VAE decoder would have to reconstruct x from the ªvector-quantizedº version of the latent vectors, denoting as {h<sup>′</sup> t<sup>∈RD, t = 1, ..., T}, that is obtained by finding the</sup> nearest prototype vector h<sup>′</sup> t<sup>= ezof each htin a codebook</sup> of prototype vectors {ek ∈ R<sup>D</sup> , k = 1, ..., K}, where K is the size of the codebook. Each prototype vector can be regarded as a cluster centroid in the latent space as a result of K-means clustering. The VQVAE encoder/decoder and the codebook are jointed learned by minimizing the reconstruction loss ∥xt −D(h<sup>′</sup> t<sup>)∥</sup> 2<sup>2, and the commitment loss of</sup> the clustering ∥E(xt) − sg(ez)∥2<sup>2, where xtdenotes a slice</sup> of x, sg(.) the stop-gradient operation, and ht = E(xt). 

Once the VQ-VAE is trained, the x can be viewed as a sequence of ªIDsº {zt ∈ Z1:K, t = 1, ..., T }, each corresponding to the index of the element of the codebook that is used to represent each slice of x. The Transformer can then be trained on such sequences of IDs to learn the underlying language, or ªcomposition rules,º of the audio codes. Once trained, the transformer can be used to generate a novel sequence of codes, which can then be converted into an audio waveform by the VQVAE decoder. 

As the waveforms are extremely long, Jukebox actually uses a ªmulti-scaleº VQ-VAE that converts a waveform into three levels of codes, and accordingly three Transformers for building the LM at each level [7]. KaraSinger works on Mel-spectrograms but also uses multi-scale VQVAE [8]. We simplify their architecture by working on Mel-spectrograms with only one level of codes instead of multiple levels, as introduced below. 

## 3. PROPOSED METHODS 

In our task, we are given pairs of audio waveforms, namely a drumless stem x<sup>m</sup> and a drum stem x<sup>d</sup> . Our goal is to train a model that can generate x<sup>d</sup> ∗<sup>given an unseen xm</sup> ∗<sup>from</sup> 



<!-- Start of picture text -->
Drum-lessDrum-less tokens Drum-less Drum tokens<br>Audio Audio<br>Drum-less Token Embedding Drum Token Embedding<br>Position Embedding Position Embedding<br>Beat-aware Module Beat-aware Module<br>In-chunk Attention In-chunk Attention<br>Cross-chunk Attention Cross-chunk Attention xM<br>Previous-chunck Attention Previous-chunck Attention<br>Encoder/Decoder Attention<br>In-chunk Attention<br>In-chunk Attention<br>Cross-chunk Attention<br>Cross-chunk Attention<br>Previous-chunck attention<br>Previous-chunck Attention<br>Encoder/Decoder Attention<br>Keys & Values<br>Predicted Drum Tokens<br><!-- End of picture text -->

Figure 3: Details of our Transformer encoder/decoder. 

the test set. To achieve so, we propose several extensions of the Jukebox model. While we focus on drum accompaniment generation only, the same methodology may apply equally well to other conditional generation tasks. 

Two VQ-VAEs. As illustrated in Figure 2, we build separate VQ-VAEs for x<sup>m</sup> and x<sup>d</sup> using drumless stems and drum stems respectively. Once trained, the drumless VQ-VAE encoder and the drum VQ-VAE encoder would convert x<sup>m</sup> and x<sup>d</sup> into {zt<sup>m∈Z1:Km, t=1, ..., T}and</sup> {zt<sup>d∈Z1:Kd, t=1, ..., T} separately.Assuming that the</sup> drumless tracks are more diverse, we suggest use a larger codebook size for the drumless sounds codebook than the drum sounds codebook, namely K<sup>m</sup> ≥ K<sup>d</sup> . 

Mel VQ-VAE & Vocoder. To reduce computational cost, we build VQ-VAEs that take Mel-spectrograms as the input and target output. Specifically, we use the convolutional blocks of UNAGAN [5] to build a pair of VQVAE encoder and VQ-VAE decoder that has symmetric architectures (one downsampling and the other upsampling). We omit the details of UNAGAN due to space limit. Our Transformer accordingly learns the LM for codes of the Mel-spectrograms. Once a novel sequence of (drum) codes is generated by the Transformer, we use our (drum) VQVAE decoder to convert the codes into a Mel-spectrogram, and then use a neural vocoder [42] to convert the Melspectrogram into the corresponding waveform. While the latent vector ht (and accordingly zt) corresponds to a slice of waveform in the original Jukebox, here the latent vectors h<sup>m</sup> t<sup>and hd</sup> t<sup>(and z</sup> t<sup>m, z</sup> t<sup>d) both correspond to a fixed number</sup> of L frames of the short-time Fourier Transform (STFT) while computing the Mel-spectrograms. 

Seq2seq Transformer. While the Jukebox model uses a Transformer decoder to model the sequences {zt, t = 1, ..., T } corresponding to mixtures of sounds, in our case we need a dedicated Transformer encoder to take the se- 

195 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
Drum-less audio Beat<br>Beat information extractor Beat Conditioner Condition<br>Embeddings<br>Input Audio Feature<br>BLSTM Conditoner FC<br>Resizer<br>(314, T’)<br>Tracker Embedding<br>Low-Level Tracker Embeddings<br>Mid-Level<br>(50,T') Re-Sampling EmbeddingResizer<br>FC (50, T)<br>Mid-Level Activation Peaks<br>ActivationFunction Peak Picking High-Level<br>High-Level Beat Position Embedding<br>(3,T') Resizer<br>HMM<br>(d_model, T)<br><!-- End of picture text -->

Figure 4: Details of the proposed beat-aware module that extracts beat condition embeddings from the drumless audio. 

quence {zt<sup>m, t=1, ..., T}correspondingtoadrumless</sup> audio as the input, and a Transformer decoder to generate the sequence {zt<sup>d, t=1, ..., T}correspondingto</sup> the accompanying drum audio as the output, leading to a sequence-to-sequence (seq2seq) architecture. Following Jukebox, we use the attention mechanism of the Scalable Transformer [15] in our Transformer encoder/decoder. As depicted in Figure 3, to determine its output zi<sup>dateach</sup> i, our Transformer decoder uses factorized ªin-chunk,º ªcross-chunkº and ªprevious-chunkº attention layers to attend to the drum codes it generates previously, namely z<i<sup>d={z</sup> t<sup>d, t=1, ..., i −1}, to maintain the coherence of</sup> its output. A ªchunkº here is a slice of the corresponding sequence. Moreover, the Transformer decoder uses ªencoder/decoder attentionº to attend to the final layer of the Transformer encoder to get contextual information from the drumless code sequence {zt<sup>m, t=1, ..., T}.Tobetter</sup> synchronize the input and output, position embeddings are used. We refer readers to [7,15] for details. 

Beat-Aware Module. Figure 3 also shows that we use a novel ªbeat-aware moduleº (after the position embedding) in both Transformer encoder and decoder. We note that the code zt<sup>mis trained to provide essential information needed</sup> to reconstruct the drumless audio x<sup>m</sup> t<sup>,sotheinformation</sup> carried by zt might be mixed, covering different musical aspects including timbre, style, rhythm, etc. To supply the Transformer with clear rhythm-related information of x<sup>m</sup> , we might need such a dedicated beat-aware module. 

As depicted in Figure 4, the beat-aware module consists two sub-modules, the ªbeat information extractorº and the ªbeat conditioner.º The former extracts beat-related information per frame from x<sup>m</sup> using an existing beat/downbeat tracker [19], while the latter incorporates that beat-related information for each t as a beat condition embedding c<sup>m</sup> t<sup>∈</sup> R<sup>dmodel</sup> that has the same length dmodel as the token embedding of the Transformers, and adds together the beat condition embedding and token embedding per t to serve as the input to the subsequent attention layers. 

Despite that deep learning-based beat/downbeat track- 

ers such as those proposed by Böck et al. [43±45] have achieved excellent performance for mainstream pop, rock or dance music, their performance and behaviors are influenced by the sound source composition (i.e., drum/nondrum sounds) of their training data [19, 46]. Considering that our input music is drumless, which is quite different from the music that existing common beat/downbeat trackers [44, 45] are trained with and trained for, we use in our beat information extractor the ªnon-drum trackerº developed by Chiu et al. [19] exclusively for drumless stems. In Section 4, we describe three ways to extract different levels of beat information feature from the non-drum tracker. 

## 4. BEAT CONDITION EMBEDDING 

As shown on the left of Figure 4, following the common design [44], the beat/downbeat tracker [19] uses BLSTM layers to get 50-dimensional ªtracker embeddingsº from x<sup>m</sup> , and then uses fully-connected (FC) layers to compute 3-dimensional ªactivation functionsº indicating the likelihood of observing a beat, downbeat, or non-beat at each frame. Finally, either a simple peak-picking or a hidden Markov model (HMM)-based algorithm [44] can be used to finalize the beat and downbeat time positions from the activation functions. We accordingly investigate extracting features from different stages of this processing pipeline. 

Low-level (tracker) embeddings. We simply use the high-dimensional tracker embeddings, resampling it temporally, pooling them every L frames, and converting each of them to the desired length dmodel with an FC. 

High-level beat/downbeat positions. From the beat and downbeat time positions estimated by HMM, a frame can be labeled as either a beat, downbeat, or non-beat. We learn three dmodel-dimensional embedding vectors corresponding to each case, and represent every L frames with one of the three vectors according to the frame labels. 

Mid-level activation peaks. As the beat/downbeat positions are sparse over time, we consider a ªdenserº version by simply picking the peak positions of the activation func- 

196 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

tions by scipy.signal.find_peaks [47] and similarly learning embedding vectors that are assigned to the frames according to whether a frame corresponds to a peak or not. Such a peak might represent a musical onset. 

## 5. EXPERIMENT SETUP 

Multi-track datasets for research on musical source separation [17] usually host recordings that each consists of an isolated drum stem along with stems corresponding to other instruments. We can simply take the drum stem as the target drum track, and the summation of the remaining stems as the input drumless track. In our implementation, we used the multi-track recordings from three datasets. MUSDB18 [17] contains 150 recordings, each of which has four stems corresponding to vocal, drums, bass, and ªothers.º It is commonly used in source separation. MedleyDB [48] contains 196 multi-track recordings, each of which includes a drum stem along with many other stems. MixingSecret [49] has 257 multi-track recordings with various instruments, all including drums. We removed the 46 duplicate recordings between MUSDB18 and MedleyDB and the 100 duplicate recordings between MUSDB18 and MixingSerect, leading to 457 recordings to be used in our work. We randomly split the recordings into 80%, 10%, 10% as the training set, validation set (for parameter tuning), and testing set (for objective and subjective evaluation) at the ªrecording-level,º ensuring that a recording does not appear in different splits. 

All the recordings are sampled at 44.1 kHz and the stems are all monaural. Following Jukebox [7], we used 24-second audio clips in our work. We sliced each recording (and accordingly the stems) to 23.8-second audio clips with 50% temporal overlaps (as 2<sup>20</sup> /44100 = 23.8), and discarded the clips that do not contain any drum sounds. We then computed the Mel-spectrograms of each clip with PyTorch v1.7.1 with a Hann window of 1,024 samples for STFT, a hop size of 256 samples and 80 Mel-filter banks. 

To evaluate the performance of the proposed JukeDrummer and validate the effectiveness of model components, we adopted the following variants in our experiments.<sup>2</sup> 

- seq2seq+beat (low): given a drumless clip x<sup>m</sup> , we computed the drumless codes {zt<sup>m} and the low-</sup> level beat/downbeat tracker embeddings {c<sup>m</sup> t<sup>} as the</sup> model input, to predict the drum codes {zt<sup>d}that</sup> eventually lead to the generated drum clip x<sup>d</sup> , using the proposed seq2seq Transformer. 

- seq2seq+beat (mid): using the beat condition embeddings computed from the mid-level activation peaks (see Section 4) for {c<sup>m</sup> t<sup>} instead.</sup> 

- seq2seq+beat (high): using the beat condition embeddings from the high-level beat/downbeat positions as {c<sup>m</sup> t<sup>} instead.</sup> 

> 2 A reviewer suggested that we should have compared our model with other accompaniment generation models that operate in the symbolic domain such as [20] and [21], saying that we can use existing audio samples or drum synthesis models to render their output to audio. However, the problem is that such a symbolic-domain accompaniment generation model also requires its input to be a MIDI file rather than audio. 

- seq2seq w/o beat: to study the usefulness of the beat conditioning, we predicted {zt<sup>d} from {z</sup> t<sup>m},</sup> not using any beat-related conditions at all. 

- decoder+beat (low): to study the usefulness of the drumless codes {zt<sup>m},weusedonlythelow-</sup> level beat condition embeddings {c<sup>m</sup> t<sup>}asinputto</sup> predict {zt<sup>d}, via a Transformer decoder-only archi-</sup> tecture (i.e., not seq2seq Transformer). 

- decoder w/o beat: this is the baseline drummer that ªplays its own,º generating {zt<sup>d}autore-</sup> gressively via a Transformer decoder without taking any information (neither {zt<sup>m}nor{cm</sup> t<sup>})fromthe</sup> drumless clip x<sup>m</sup> it is supposed to play along to. 

While the Mel-spectrogram for a clip in our case has 4,096 frames, the VQ-VAE encoder downsamples it to a sequence of T = 1,024 latent vectors, namely each corresponding to L = 4 frames. For VQ-VAE, we set the codebook size of drumless sounds K<sup>m</sup> = 1,024 and that of drums K<sup>d</sup> = 32 (so K<sup>m</sup> ≫ K<sup>d</sup> ), and the dimension of the latent vectors D = 64. The VQ-VAE encoders/decoders for both drumless and drums all have two layers. For those models employing a seq2seq LM, the Transformer encoder has 9 layers and the Transformer decoder has 20 layers.<sup>3</sup> 

At inference time, we used the drum VQ decoder to convert the drum codes {zt<sup>d} to a Mel-spectrogram, which</sup> is then turned into the waveform of the drum clip x<sup>d</sup> by a HiFi-GAN V1 vocoder [42]. We trained the vocoder from scratch with audio of drum sounds from our dataset for 2.5 days, and then, inspired by [50,51], fine-tuned it on the reconstructed Mel-spectrograms of the Drum VQ decoder. 

## 6. OBJECTIVE EVALUATION 

As audio-domain drum accompaniment generation is new, we propose customized metrics. Specifically, we use the ªdrum trackerº trained exclusively for drum stems by Chiu et al. [19], which follows exactly the same pipeline as the non-drum tracker (cf. Figure 4), to extract rhythmic features at three different levels for the ground-truth and generated drum sounds for the test split. We then compare the rhythmic features of the ground-truth and the generated in such three levels, using the mean square error for the low-level tracker embeddings (TrackEmb-MSE), cross entropy for the mid-level activation functions (ActEntropy), and the F-measure for beat/downbeat estimation (B/DB-F1). The last one, computed by mir_eval [52], uses the beat positions of the ground-truth drums as the reference and those of the generated drums as the estimated beats. These metrics evaluates only the rhythmic consistency between the generated drums and the drumless audio (using its human-made drum track as a proxy), not other aspects such as stylistic consistency and audio quality, which will be evaluated subjectively in Section 7. 

> 3 We used Adam as our optimizer with a learning rate of 0.0003 for both VQ-VAE and Transformer LM. We trained our LM with a batch size of 16, input feature dimension dmodel = 512, two heads for multihead attention, and the chunk size for factorized attention being 16. For those employing a decoder-only architecture, the number of layers of the Transformer decoder reduces to 15 because 5 of the layers corresponding to the ªencoder/decoder attentionº are removed. 

197 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

|Model|Obj|ective metrics||Su<br>|bjective<br>|MOS (<br>|∈[1,5]<br>|)<br>|
|---|---|---|---|---|---|---|---|---|
||TrackEmd-MSE↓|Act-Entropy↓|B/DB-F1↑|R<sup>m/d</sup>|S<sup>m/d</sup>|Q<sup>d</sup>|R<sup>d</sup>|O<sup>d</sup>|
|seq2seq+beat (low)|.068±.023|.928±.189|.340|3.27|3.44|3.39|3.37|3.20|
|seq2seq+beat (mid)|.077±.022|.963±.200|.212|Ð|Ð|Ð|Ð|Ð|
|seq2seq+beat (high)|.080±.024|.938±.160|.132|Ð|Ð|Ð|Ð|Ð|
|seq2seq w/o beat|.081±.022|.968±.233|.110|1.78|2.34|2.95|2.58|2.05|
|decoder+beat (low)|.068±.023|.931±.200|.339|3.05|3.34|3.33|3.07|3.17|
|decoder w/o beat|.087±.025|.987±.240|.114|1.59|1.83|2.56|1.88|1.73|
|Real data(not vocoded)|Ð|Ð|Ð|4.39|3.95|3.85|4.61|4.17|



Table 1: Results of objective and subjective evaluation of variants of the proposed JukeDrummer model. The metrics are (from left to right): beat/downbeat tracking embedding MSE, beat/downbeat activation entropy, beat/downbeat F1, R<sup>m/d</sup> (rhythmic consistency), S<sup>m/d</sup> (stylistic consistency), Q<sup>d</sup> (audio quality), R<sup>d</sup> (rhythmic stability), O<sup>d</sup> (overall). ↓ / ↑: the lower/higher the better; best two results (among the six model variants) per column highlighted in bold. 

Result shown in the middle of Table 1 clearly shows that the models with low-level beat information achieve lower MSE, cross entropy, and higher F1, suggesting the usefulness of the low-level beat information for rhythmic consistency. The mid-level and high-level ones seem less effective (possibly because they are relatively monotonic), so we did not evaluate them further in Section 7. The objective scores also suggest that the Transformer encoder does not contribute much to rhythmic consistency. 

## 7. SUBJECTIVE EVALUATION 

With an online study, we solicited 22 anonymous volunteers to rate the result for 3 out of 15 random drumless tracks (each 23.8 seconds) from the test split. Each time, a volunteer listened to a drumless tracks (x<sup>m</sup> ∗<sup>) first, and then</sup> (in random orders) the mixture (i.e., x<sup>m</sup> ∗<sup>+ xd</sup> ∗<sup>)containing</sup> drum samples generated by four different models, plus the real human-made one (to set a high anchor). The volunteer then rated them in the following aspects on a 5-point Likert scale: rhythmic consistency between the drumless input and generated drums; stylistic consistency concerning the timbre and arrangement of the drumless input and generated drums; audio quality and rhythmic stability (whether the drummer follows a steady tempo) of the generated drum; and overall perceptual impression. 

The mean opinion scores (MOS) in Table 1 show that seq2seq+beat (low) consistently outperforms the others, validating the effectiveness of using both the drumless codes and beat conditions. decoder+beat (low) performs consistently the second best, outperforming the two models without beat information significantly in three aspects according to paired t-test (p-value < 0.05), validating again the importance of the beat-aware module. Complementing Section 6, the MOS result suggests that the beat conditions seem more important than the drumless codes, though the best result is obtained with both. 

Figure 5 further demonstrates that, given the same input, our model can generate multiple accompaniments with diversity in both beat and timbre. Diversity is an interesting aspect that is hard to evaluate, but it is desirable as there is no single golden drum accompaniment for a song. This may also explain why the F1 scores in Table 1 seem low. 



Figure 5: Two sets of three different generated samples by the same model given the same beat condition embedding. 

Verbal feedbacks from the subjects confirm that our best model generates drum accompaniment that is rhythmically and stylistically consistent with the input, especially for band music or music with heavy use of bass. However, the model still has limits. At times the model generates total silence, though it can be avoided by sampling the LM again. The model may struggle to change its tempo going through different sections of a song. Moreover, the generation might be out-of-sync with the input in the beginning few seconds, until the model gets sufficient context. Please visit the demo page for various examples. 

## 8. CONCLUSION 

We have presented JukeDrummer, a novel audio-to-audio extension of OpenAI’s JukeBox model capable of adding the drum part of a drumfree recording in the audio domain. To our knowledge, this represents the first attempt to audiodomain generation conditioned on drumless mixed audio. With objective and subjective evaluations, we validated the effectiveness of the customized VQ-VAE plus the seq2seq Transformer design, and the proposed beat-aware module. Among the beat conditions, we found that the low-level embeddings work the best. Future work can be done to further improve the language model (LM), and to extend our work to other audio-to-audio generation tasks. 

198 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

## 9. ACKNOWLEDGEMENT 

We are grateful to the anonymous reviewers for their valuable comments. This research is funded by grant NSTC 109-2628-E-001-002-MY2 from the National Science and Technology Council of Taiwan. 

## 10. REFERENCES 

- [1] J. Engel, C. Resnick, A. Roberts, S. Dieleman, D. Eck, K. Simonyan, and M. Norouzi, ªNeural audio synthesis of musical notes with WaveNet autoencoders,º in Proc. Int. Conf. Machine Learning, 2017. 

- [2] J. Engel, K. K. Agrawal, S. Chen, I. Gulrajani, C. Donahue, and A. Roberts, ªGANSynth: Adversarial neural audio synthesis,º in Proc. Int. Conf. Learning Representations, 2019. 

- [3] C. Donahue, J. McAuley, and M. Puckette, ªAdversarial audio synthesis,º in Proc. Int. Conf. Learning Representations, 2019. 

- [4] S. Lattner and M. Grachten, ªHigh-level control of drum track generation using learned patterns of rhythmic interaction,º in Proc. IEEE Work. Applications of Signal Processing to Audio and Acoustics, 2019. 

- [5] J.-Y. Liu, Y.-H. Chen, Y.-C. Yeh, and Y.-H. Yang, ªUnconditional audio generation with generative adversarial networks and cycle regularization,º in Proc. INTERSPEECH, 2020. 

- [6] J. Engel, L. Hantrakul, C. Gu, and A. Roberts, ªDDSP: Differentiable digital signal processing,º in Int. Conf. Learning Representations, 2021. 

- [7] P. Dhariwal, H. Jun, C. Payne, J. W. Kim, A. Radford, and I. Sutskever, ªJukebox: A generative model for music,º arXiv preprint arXiv:2005.00341, 2020. 

- [8] C.-F. Liao, J.-Y. Liu, and Y.-H. Yang, ªKaraSinger: Score-free singing voice synthesis with VQ-VAE using Mel-spectrograms,º in Proc. IEEE Int. Conf. Acoust. Speech Signal Process., 2022, pp. 956±960. 

- [9] C. M. Payne, ªMuseNet,º OpenAI Blog, 2019. 

- [10] C. Donahue et al., ªLakhNES: Improving multiinstrumental music generation with cross-domain pretraining,º in Proc. Int. Soc. Music Information Retrieval Conf., 2019. 

- [11] Y.-H. Chen, Y.-H. Huang, W.-Y. Hsiao, and Y.-H. Yang, ªAutomatic composition of guitar tabs by Transformers and groove modeling,º in Proc. Int. Soc. Music Inf. Retr. Conf., 2020. 

- [12] Z. Wang, Y. Zhang, Y. Zhang, J. Jiang, R. Yang, J. Zhao, and G. Xia, ªPianoTree VAE: Structured representation learning for polyphonic music,º in Proc. Int. Soc. Music Inf. Retr. Conf., 2020. 

- [13] M. Suzuki, ªScore Transformer: Transcribing quantized MIDI into comprehensive musical score,º in Proc. Int. Soc. Music Inf. Retr. Conf., Late-breaking demo paper, 2021. 

- [14] A. Vaswani et al., ªAttention is all you need,º in Proc. Advances in Neural Information Processing Systems, 2017, pp. 5998±6008. 

- [15] R. Child, S. Gray, A. Radford, and I. Sutskever, ªGenerating long sequences with sparse Transformers,º arXiv preprint arXiv:1904.10509, 2019. 

- [16] C. A. Huang, H. V. Koops, E. Newton-Rex, M. Dinculescu, and C. J. Cai, ªAI song contest: Human-AI co-creation in songwriting,º in Proc. Int. Soc. Music Inf. Retr. Conf., 2020, p. 708±716. 

- [17] Z. Raf et al., ªThe MUSDB18 corpus for music separation,º 2017. [Online]. Available: https://doi.org/ 10.5281/zenodo.1117372 

- [18] E. Deruty, M. Grachten, S. Lattner, J. Nistal, and C. Aouameur, ªOn the development and practice of AI technology for contemporary popular music production,º Transactions of the International Society for Music Information Retrieval, vol. 5, no. 1, pp. 35±49, 2022. 

- [19] C.-Y. Chiu, W.-Y. Su, and Y.-H. Yang, ªDrum-aware ensemble architecture for improved joint musical beat and downbeat tracking,º IEEE Signal Processing Letters, vol. 28, pp. 1100±1104, 2021. 

- [20] R. Dahale, V. Talwadker, P. Verma, and P. Rao, ªNeural drum accompaniment generation,º in Proc. Int. Soc. Music Inf. Retr. Conf., Late-breaking demo paper, 2021. 

- [21] D. Makris, G. Zixun, M. Kaliakatsos-Papakostas, and D. Herremans, ªConditional drums generation using compound word representations,º in Proc. Artificial Intelligence in Music, Sound, Art and Design, 2022, p. 179±194. 

- [22] J. Gillick, A. Roberts, J. Engel, D. Eck, and D. Bamman, ªLearning to groove with inverse sequence transformations,º in Proc. Int. Conf. Machine Learning, 2019. 

- [23] V. Thio, H.-M. Liu, Y.-C. Yeh, and Y.-H. Yang, ªA minimal template for interactive web-based demonstrations of musical machine learning,º in Proc. Workshop on Intelligent Music Interfaces for Listening and Creation, 2019. 

- [24] G. Alain, M. Chevalier-Boisvert, F. Osterrath, and R. Piche-Taillefer, ªDeepDrummer: Generating drum loops using deep learning and a human in the loop,º arXiv preprint arXiv:2008.04391, 2020. 

199 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

- [25] N. Tokui, ªCan GAN originate new electronic dance music genres? ± Generating novel rhythm patterns using GAN with genre ambiguity loss,º arXiv preprin: 2011.13062, 2020. 

- [26] H.-W. Dong, W.-Y. Hsiao, L.-C. Yang, and Y.-H. Yang, ªMuseGAN: Symbolic-domain music generation and accompaniment with multi-track sequential generative adversarial networks,º in Proc. AAAI Conf. Artificial Intelligence, 2018. 

- [27] I. Simon, A. Roberts, C. Raffel, J. Engel, C. Hawthorne, and D. Eck, ªLearning a latent space of multitrack measures,º arXiv preprint arXiv:1806.00195, 2018. 

- [28] H.-M. Liu and Y.-H. Yang, ªLead sheet generation and arrangement by conditional generative adversarial network,º in Proc. IEEE. Conf. Machine Learning and Applications, 2018, pp. 722±727. 

- [29] Y. Ren, J. He, X. Tan, T. Qin, Z. Zhao, and T.-Y. Liu, ªPopMAG: Pop music accompaniment generation,º in Proc. ACM Multimedia Conf., 2020. 

- [30] J. Nistal, S. Lattner, and G. Richard, ªDrumGAN: Synthesis of drum sounds with timbral feature conditioning using generative adversarial networks,º in Proc. Int. Soc. Music Information Retrieval Conf., 2020. 

- [31] A. Ramires, P. Chandna, X. Favory, E. Gómez, and X. Serra, ªNeural percussive synthesis parameterised by high-level timbral features,º in Proc. IEEE Int. Conf. Acoustics, Speech and Signal Processing, 2020. 

- [32] C. Aouameur, P. Esling, and G. Hadjeres, ªNeural drum machine: An interactive system for realtime synthesis of drum sounds,º arXiv preprint arXiv:1907.02637, 2019. 

- [33] J. Drysdale, M. Tomczak, and J. Hockman, ªAdversarial synthesis of drum sounds,º in Proc. Int. Conf. Digital Audio Effects, 2020. 

- [34] ÐÐ, ªStyle-based drum synthesis with GAN inversion,º in Proc. Int. Soc. Music Inf. Retr. Conf., Latebreaking demo paper, 2021. 

- [35] M. Tomczak, M. Goto, and J. Hockman, ªDrum synthesis and rhythmic transformation with adversarial autoencoders,º in Proc. ACM Int. Conf. Multimedia, 2020, p. 2427±2435. 

- [36] T. Hung, B. Chen, Y. Yeh, and Y. Yang, ªA benchmarking initiative for audio-domain music generation using the Freesound Loop Dataset,º in Proc. Int. Soc. Music Information Retrieval Conf., 2021. 

- [37] A. v. d. Oord, O. Vinyals, and K. Kavukcuoglu, ªNeural discrete representation learning,º in Proc. Advances in Neural Information Processing Systems, 2017. 

- [38] L. Kaiser et al., ªFast decoding in sequence models using discrete latent variables,º in Proc. Int. Conf. Machine Learning, 2018, pp. 2390±2399. 

- [39] A. Razavi et al., ªGenerating diverse high-fidelity images with VQ-VAE-2,º in Proc. Advances in Neural Information Processing Systems, 2019. 

- [40] A. Polyak et al., ªSpeech resynthesis from discrete disentangled self-supervised representations,º in Proc. Interspeech, 2021, pp. 3615±3619. 

- [41] J. Walker, A. Razavi, and A. v. d. Oord, ªPredicting video with VQVAE,º arXiv preprint arXiv:2103.01950, 2021. 

- [42] J. Kong, J. Kim, and J. Bae, ªHiFi-GAN: Generative adversarial networks for efficient and high fidelity speech synthesis,º in Proc. Advances in Neural Information Processing Systems, 2020. 

- [43] S. Böck, F. Korzeniowski, J. Schlüter, F. Krebs, and G. Widmer, ªmadmom: A new Python audio and music signal processing library,º Proc. ACM Multimed. Conf., pp. 1174±1178, 2016. 

- [44] S. Böck et al., ªJoint beat and downbeat tracking with recurrent neural networks,º in Proc. Int. Soc. Music Information Retrieval Conf., 2016. 

- [45] S. Böck and M. E. P. Davies, ªDeconstruct, analyse, reconstruct: How to improve tempo, beat, and downbeat estimation,º in Proc. Int. Soc. Music Inf. Retr. Conf., 2020, p. 574±582. 

- [46] C.-Y. Chiu, J. Ching, W.-Y. Hsiao, Y.-H. Chen, W.Y. Su, and Y.-H. Yang, ªSource separation-based data augmentation for improved joint beat and downbeat tracking,º in Proc. Eur. Signal Process. Conf., 2021. 

- [47] P. Virtanen et al., ªSciPy 1.0: Fundamental algorithms for scientific computing in Python,º Nature Methods, vol. 17, pp. 261±272, 2020. 

- [48] R. Bittner et al., ªMedleyDB: A multitrack dataset for annotation-intensive MIR research,º in Proc. Int. Soc. Music Inf. Retr. Conf., 2014, [Online] http://medleydb.weebly.com/. 

- [49] ªThe ‘Mixing Secrets’ free multitrack download library,º [Online] https://www.cambridge-mt.com/ms/ mtk/. 

- [50] K.-W. Kim, S.-W. Park, J. Lee, and M.-C. Joe, ªASSEM-VC: Realistic voice conversion by assembling modern speech synthesis techniques,º in Proc. IEEE Int. Conf. Acoust. Speech Signal Process., 2022. 

- [51] X. Tan et al., ªNaturalSpeech: End-to-end text to speech synthesis with human-level quality,º arXiv preprint arXiv:2205.04421, 2022. 

- [52] C. Raffel et al., ªmir_eval: A transparent implementation of common MIR metrics,º in Proc. Int. Soc. Music Inf. Retr. Conf., 2014, pp. 367±372. 

200 

