---
paper_id: "000045"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706422/files/000045.pdf"
---

# PIANOBIND: A MULTIMODAL JOINT EMBEDDING MODEL FOR POP-PIANO MUSIC 

## Hayeon Bang Eunjin Choi Seungheon Doh Juhan Nam Graduate School of Culture Technology, KAIST, South Korea 

```
{hayeonbang,jech,seungheondoh,juhan.nam}@kaist.ac.kr
```

### ABSTRACT 

Solo piano music, despite being a single-instrument medium, possesses significant expressive capabilities, conveying rich semantic information across genres, moods, and styles. However, current general-purpose music representation models, predominantly trained on large-scale datasets, often struggle to capture subtle semantic distinctions within homogeneous solo piano music. Furthermore, existing piano-specific representation models are typically unimodal, failing to capture the inherently multimodal nature of piano music, expressed through audio, symbolic, and textual modalities. To address these limitations, we propose PianoBind, a piano-specific multimodal joint embedding model. We systematically investigate strategies for multi-source training and modality utilization within a joint embedding framework optimized for capturing finegrained semantic distinctions in (1) small-scale and (2) homogeneous piano datasets. Our experimental results demonstrate that PianoBind learns multimodal representations that effectively capture subtle nuances of piano music, achieving superior text-to-music retrieval performance on in-domain and out-of-domain piano datasets compared to general-purpose music joint embedding models. Moreover, our design choices offer reusable insights for multimodal representation learning with homogeneous datasets beyond piano music. 

### 1. INTRODUCTION 

The piano stands as a uniquely versatile solo instrument capable of conveying complex polyphonic musical expression through a single instrument. With its expansive tonal range, harmonic possibilities, and expressive capabilities—even allowing orchestral works to be effectively performed on a single keyboard—piano music encompasses diverse genres, styles, and expressive content. Numerous studies in the Music Information Retrieval (MIR) field have targeted tasks focused on piano music, such as piano music generation [1–4] and automatic music transcription [5–8]. However, research on piano-specific represen- 

> © Hayeon Bang, Eunjin Choi, Seungheon Doh, and Juhan Nam. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: Hayeon Bang, Eunjin Choi, Seungheon Doh, and Juhan Nam, “PianoBind: A Multimodal Joint Embedding Model for Pop-piano Music”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 



<!-- Start of picture text -->
Audio Text MIDI<br>Swing, Ballad<br>Bright, Sad, Epic<br>Speedy, Relaxing<br>T<br><!-- End of picture text -->

Figure 1. Illustration of PianoBind: A multimodal piano music representation model integrating audio, MIDI, and text. 

tation models remains limited. Existing approaches are typically constrained to a single modality [9, 10], failing to reflect the inherently multimodal nature of piano music that encompasses audio recordings, symbolic MIDI, and semantic descriptions. 

Recent advances in multimodal joint embedding models have shown promise in bridging the gap between audio and text domains [11–15] and symbolic domains [16–18], yet they often fall short in specialized domains—particularly in solo piano music. Despite their versatility across diverse music categories, general-purpose models typically lack the sensitivity needed to capture subtle semantic nuances within homogeneous solo piano music. This limitation arises primarily from the scarcity of high-quality piano-specific data in general-purpose music-text datasets, which are typically dominated by multi-instrumental or vocal-centric music. 

In this work, we present PianoBind, a multimodal joint embedding model that integrates multiple modalities of solo piano music—audio, symbolic (MIDI), and textual descriptions—within a unified embedding space (illustrated in Figure 1), enabling a more comprehensive representation. Our goal is to capture the fine-grained semantic characteristics of piano music—spanning genre, mood, and style—that are often overlooked by large-scale, general-purpose models. To achieve this, we use the PIAST dataset [19] for training, a pop-piano music (e.g. newage, piano cover, jazz and its sub-genres) dataset that includes audio, MIDI, and textual descriptions. We systematically explore multi-source training strategies tailored to 

391 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

the characteristics of domain-specific datasets. We utilize a comparatively large amount of automatically collected textual data with weaker temporal alignment to audio. This approach compensates for the limited amount of human-annotated data. Furthermore, we propose effective methods for combining multimodal information both during training and at retrieval time, where joint audiosymbolic embeddings can significantly enhance text-tomusic retrieval, particularly in distinguishing highly similar piano pieces. 

Our experiments on both in-domain and out-of-domain piano datasets show that PianoBind outperforms generalpurpose music joint embedding models in capturing the nuances of piano solo music. By focusing on small-scale, homogeneous datasets, our findings also offer valuable guidelines for developing specialized multimodal representation learning approaches in other domains with limited data. As such, this study contributes to the growing body of piano-centric MIR research. It also contributes to broader discussions on efficient and fine-grained multimodal modeling. These contributions are especially relevant when data availability is inherently constrained. We have publicly released code and pretrained weights of PianoBind, with the demo online<sup>1</sup> . 

### 2. RELATED WORKS 

### 2.1 Piano Music Representation Learning 

Piano music has long served as a central subject in MIR, owing to its structural richness and expressive depth. However, despite this sustained attention, existing representation learning approaches for piano music are predominantly unimodal—relying solely on symbolic or audio data—thus failing to reflect the inherently multimodal nature of piano music. 

Early piano music representation in the symbolic music domain primarily focused on disentangling low-level symbolic features, mostly with the goal of enhancing controllability in music generation tasks. Models such as PianoTree VAE [20], Wang et al. [21], and CollageNet [22] exemplify this approach, decomposing music into attributes such as rhythm, harmony, texture, and structure to facilitate usercontrolled music generation. 

More recently, transformer-based models like MidiBERT-Piano [9] and PianoBART [10] have expanded piano music understanding through large-scale pretraining, capturing both low-level features and higherlevel musical attributes. MidiBERT-Piano introduced masked modeling objectives for solo piano MIDI data, demonstrating strong transferability to downstream tasks such as composer classification and expressive attribute prediction. Building upon this foundation, PianoBART extended these capabilities from understanding toward generation tasks, facilitating more sophisticated music creation and symbolic inpainting tasks. Nonetheless, these models remain purely symbolic, lacking integration with acoustic information or natural language semantics. 

> 1 `https://hayeonbang.github.io/PianoBind/` 

Despite the progress in piano music representation learning, multimodal understanding of piano music has been limited, primarily due to the scarcity of datasets that support such approaches. Until recently, few resources existed that combined multiple modalities of piano performance. EMOPIA [23] made an initial step by providing paired audio and MIDI recordings with emotion labels, while PIAST [19] has recently extended this further by adding comprehensive textual annotations describing genre and mood. However, even with these multimodal datasets becoming available, no prior research has proposed an integrated approach that jointly leverages audio, symbolic, and textual modalities for piano music understanding. 

### 2.2 Multimodal Joint Embedding Models 

Multimodal joint embedding models aim to align data from different modalities in a shared embedding space. This alignment creates semantically meaningful representations that capture relationships between modalities, enabling cross-modal retrieval, understanding, and conditioned generation. MuLan [11] pioneered large-scale audio–text training with over 44 million pairs, showing strong retrieval capabilities. MusCALL [12] proposed an audio-text dual encoder architecture, demonstrating improved retrieval performance and downstream performance. CLAP [13] expanded on this by leveraging audio captioning corpora and keyword-to-caption augmentation strategies, and introduced a joint audio-text embedding model. Further refinements include models like TTMR [14] and TTMR++ [15], which address varying query granularities—ranging from single tags to full sentences—and incorporate rich metadata to produce more descriptive and contextual text embeddings. These methods improved retrieval accuracy by modeling both linguistic and musical subtleties. 

In parallel, symbolic-text joint embedding models have been explored through the CLaMP series [16–18], which introduced contrastive learning between symbolic music (e.g., ABC or MIDI) and textual descriptions. While CLaMP pioneered symbolic music retrieval through textABC joint training, CLaMP2 expanded this to multilingual text and MIDI data, and CLaMP3 further incorporated audio and performance signals, marking the first trimodal framework in music representation learning to jointly align audio, symbolic, and textual modalities. 

Despite these advances, most current models are trained on general-purpose, large-scale datasets covering a broad range of musical styles and instrumentation. As a result, they often fall short of capturing the fine-grained semantic differences required for more homogeneous domains like solo piano music. These models tend to underperform in settings where subtle variations in genre, mood, and style must be accurately distinguished. 

To address this gap, our proposed model PianoBind integrates piano-specific audio, symbolic, and textual modalities in a unified embedding space, enabling more precise retrieval within this specialized musical domain. 

392 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
Model Audio<br>Sampler<br>Model<br>PIAST-AT (Fine-tune)<br>PIAST-YT<br>Text Feature T<br>Fusion<br>PIAST-AT<br>Model<br>(Pre-train)<br>Symbolic<br>PIAST-YT<br>Multi-source Training Trimodal Learning Multimodal Item Embedding<br><!-- End of picture text -->

Figure 2. Training strategies of PianoBind: (1) Multi-source training combines small strongly aligned (human-annotated) and large weakly aligned (automatically collected) datasets; (2) Trimodal learning simultaneously aligns audio, symbolic, and textual embeddings; (3) Multimodal item embedding merges multiple modalities into a unified representation. 

### 3. PIANOBIND 

Considering the specific characteristics of piano solo datasets—such as homogeneous data distribution, limited dataset size, and multimodality—we propose a multimodal joint embedding model specialized for solo piano music. In this section, we describe the overall architecture of PianoBind (section 3.1), and the training strategies it explores (section 3.2), comprising: (1) multi-source learning with strongly and weakly aligned pairs, and (2) modality integration across audio, symbolic, and textual features. 

### 3.1 Architecture Overview 

### 3.1.1 Audio Encoder 

Following previous work [12], we adopt a modified ResNet-50 [24] architecture to process mel-spectrogram representations of piano recordings. We extract 128-band mel-spectrograms with a 1024-point FFT, 512-point hop length, and apply log-scaling. As in MusCALL, we apply three stem convolutional layers followed by average pooling, and implement anti-aliased blur pooling. We also follow the downsizing strategy employed in the previous work. 

### 3.1.2 Symbolic Encoder 

We utilize MidiBERT [9] as a symbolic encoder. The model handles bar, position, pitch, and duration information of MIDI by adapting Compound Word (CP) representation [2] into its model. Since MidiBERT does not contain the [CLS] token, we obtained the final MIDI embedding by mean-pooling over the sequence of hidden states from the last Transformer layer, resulting in a dense representation that is then projected to the shared embedding space. 

### 3.1.3 Text Encoder 

Our text processing pipeline employs RoBERTa [25], using its byte-pair encoding (BPE) tokenizer. The tok- 

enized input passes through 12 Transformer layers with 768-dimensional hidden states. Since RoBERTa lacks the standard pooler output found in BERT, we create sentencelevel representations by mean-pooling across the final layer’s hidden states. These textual embeddings are also mapped to our shared space through a linear projection layer. 

### 3.1.4 Joint Embedding with Contrastive Loss 

The representations from our three encoders (audio, MIDI, and text) are aligned through modality-specific linear projections into a 512-dimensional shared embedding space. All embeddings undergo ℓ2-normalization to ensure consistent scaling across modalities. Cross-modal similarities are computed via dot products between these normalized embeddings, providing the foundation for our various training objectives. We use the N-pair Contrastive loss, known as the InfoNCE [26] loss, which maximizes the cosine similarity between positive music-text embedding pairs while minimizing the similarity for negative pairs. For audio-text alignment, the InfoNCE loss is defined as follows: 



<!-- Start of picture text -->
La→t = − 1 N log exp(za,i · zt + , i /τ ) (1)<br>N<br>-∑ i=1 ∑ z∈{zt,i + ,z t,i − } exp(za,i · z/τ )<br><!-- End of picture text -->

where za,i and zt,i refer to audio and text embeddings respectively, in the audio-text training. An analogous loss is computed for MIDI–text pairs by substituting audio embeddings with symbolic ones. τ represents the temperature parameter, and zt,i<sup>−denotes a set of negative text em-</sup> beddings. This aims to align embeddings between relevant music-text pairs while separating irrelevant pairs in the embedding space. The total loss is computed by symmetrically combining losses in both directions (music-totext and text-to-music). The final symmetric loss is defined 

393 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

as: 



<!-- Start of picture text -->
La ↔ t = La→t + Lt→a (2)<br>2<br><!-- End of picture text -->

### 3.2 Training Framework 

### 3.2.1 Multi-source Training 

Considering the small size and specialized annotation required for piano datasets, we explore two strategies to effectively leverage both large-scale, weakly aligned audio–text data and small-scale, expert-annotated data. 

Combined Training We jointly train the model on both sources by mixing them within training batches following prior work [13,15,27,28]. To mitigate data imbalance and noise from weak supervision, we carefully control the sampling ratio between the two sources. This enables the model to learn generalizable language–music alignments while gradually incorporating domain-specific subtleties of solo piano music. 

Pre-training and Fine-tuning Alternatively, we also adopt the two-stage training strategy, pre-training and finetuning, following [29]. The model is first pre-trained on the large-scale, weakly labeled dataset to acquire generalizable music representations. It is then fine-tuned on the smaller, expert-annotated data, with encoder parameters updated. This sequential strategy enables the model to benefit from broad semantic coverage during pre-training, while later adapting to the expressive and stylistic nuances of solo piano music through fine-tuning. 

### 3.2.2 Trimodal Representation Learning 

To fully exploit the multimodal characteristics of piano music, we extend beyond traditional bimodal setups by integrating audio, symbolic (MIDI), and text modalities into a unified retrieval framework. Inspired by the training strategy from AudioCLIP [30], we compute the contrastive loss across modality pairs (audio-text, MIDI-text) and average them to form the final objective. However, considering the nature of our MIDI data as transcribed representations derived directly from corresponding audio recordings, including an audio-MIDI loss would not significantly contribute additional semantic distinction. Consequently, we utilize only the audio-text and MIDI-text contrastive losses, calculating their average as our final training objective: 



<!-- Start of picture text -->
Ltotal = La↔t + Lm↔t (3)<br>2<br><!-- End of picture text -->

Furthermore, we leverage multimodal information not only during the training phase but also at evaluation time. To leverage the complementary strengths of different modalities, we propose multimodal item embeddings that fuse audio and MIDI information. Specifically, audio and MIDI embeddings are integrated through average fusion during the evaluation process. 

### 4. EXPERIMENT 

### 4.1 Dataset 

This study utilizes the PIAST dataset [19], the first musictext dataset explicitly designed for pop-piano music. The dataset consists of audio, MIDI, and textual descriptions, based on a comprehensive piano-specific taxonomy of 31 semantic tags across genre, emotion/mood, and style. The dataset comprises two subsets: PIAST-YT, a large-scale collection of approximately 7,367 tracks (about 900 hours) automatically collected from YouTube, with accompanying textual metadata (titles, descriptions, and tags) refined using a large language model; and PIAST-AT, a smaller, expert-annotated set of 1,986 tracks (about 17 hours in total, 30 seconds per track). For both subsets, MIDI data is generated via automatic piano transcription. The transcribed MIDI files were synchronized to downbeat estimates, and melody and chord information was extracted. 

Since the textual data of PIAST-YT is automatically collected, it exhibits weak alignment with the audio content, introducing considerable noise in the text-audio relationships. To address this challenge, we apply the two multi-source learning strategies described in Section 3, leveraging both the large-scale but weakly aligned PIASTYT data and the smaller, high-quality PIAST-AT annotations. This combined approach enables more robust representation learning despite the inherent data limitations. For experiments, we use a 9:1 train–validation split for PIASTYT, and an 8:1:1 train–validation–test split for PIAST-AT. 

### 4.2 Evaluation 

We evaluate our model using both in-domain and out-ofdomain text-to-music retrieval tasks. For in-domain evaluation, we use the 10% held-out test split from PIASTAT, comprising 199 tracks. For out-of-domain evaluation, we introduce EMOPIA-Caps by manually annotating descriptive tag labels for the EMOPIA test split [23], and transforming them into natural language captions using a large language model. The initial tags were naturally overlapping with the vocabulary used in the PIAST-AT piano-music taxonomy. To address this and better approximate real-world natural user queries, we paraphrased the tags into free-form natural language captions using GPT4o [31]. The generated captions were then reviewed and refined by a human music expert with a major in composition, to ensure their semantic accuracy and musical relevance. This transformation not only better approximates user-style queries, but also enables evaluation of the model’s ability to generalize to diverse textual expressions. Both evaluation datasets use sentence-form textual inputs; however, the in-domain set consists of concatenated tags, whereas the out-of-domain set contains free-form, natural language captions. 

For both evaluation settings, we perform text-to-music retrieval using Recall@K (R@1, R@5, R@10) and Median Rank (MedR), as these metrics reflect the model’s ability to generalize to diverse and unconstrained textual queries. 

394 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

|Training Strategy|In|-domain|(199 trac|ks)|Out|-of-dom|ain(88 tr|acks)|
|---|---|---|---|---|---|---|---|---|
||R@1|R@5|R@10|MedR↓|R@1|R@5|R@10|MedR↓|
|Combined Training|||||||||
|Audio|8.04|25.62|37.18|17|2.56|10.26|35.90|17|
|Symbolic|4.02|17.09|27.13|27|2.56|28.21|43.59|13|
|Trimodal|6.53|24.12|37.68|17|5.13|25.64|46.15|14|
|Pre-training & Fine-|tuning||||||||
|Audio|6.53|28.14|42.71|15|7.69|20.51|46.15|12|
|Symbolic|8.04|26.63|45.23|12|5.13|20.51|35.90|12|
|Trimodal|10.55|35.67|52.76|10|15.38|41.03|51.28|10|



Table 1. Performance comparison on text-based music retrieval tasks, on the in-domain (PIAST-AT) and out-of-domain (EMOPIA-Caps) datasets. 

### 4.3 Implementation Details 

For audio processing, we use 20-second signals with a sampling rate of 16 kHz, consistent with methods established by previous work [12]. To ensure temporal alignment between audio and MIDI, we match each audio segment’s start time (in seconds) with the nearest MIDI bar onset, extracting MIDI tokens from bars that correspond to each audio segment. These sequences are subsequently standardized to exactly 512 tokens through padding or truncation. For text inputs, we employ the RoBERTa tokenizer [25] with a 77-token length limit. To combat overfitting and enhance the diversity of our textual data, we implement a dynamic text dropout strategy building on approaches from several recent works [14–16]. This technique randomly selects and combines available textual elements (such as tags and captions) in varying orders for each training instance. For combined training, we use a 7:3 sampling ratio between PIAST-YT and PIAST-AT. 

All models are trained using the AdamW optimizer with a 5e-5 initial learning rate, 0.2 weight decay, and a consistent batch size of 64 across all experiments. For the contrastive loss, we jointly optimize the temperature parameter τ alongside encoder and projection parameters, following successful approaches demonstrated in recent multimodal works [12, 14]. We select optimal model checkpoints based on median rank performance on our validation dataset. Our implementation is based on PyTorch, using automatic mixed precision and trained on an NVIDIA A6000 GPU. 

### 5. RESULTS 

### 5.1 Comparison of Training Strategies 

### 5.1.1 Multi-source training 

Table 1 shows the performance of different training strategies across both in-domain (PIAST-AT) and out-of-domain (EMOPIA-Caps) test sets. We compare two multi-source learning approaches: combined training and pre-training followed by fine-tuning, each evaluated using two bimodal configurations (audio–text and symbolic–text) and one trimodal (audio–symbolic–text) configuration. 

The results demonstrate that the pre-training and fine- 

tuning approach generally outperforms the combined training across modality configurations and metrics. In the indomain setting, the pre-training and fine-tuning approach with trimodal integration achieves the best performance, reaching a Median Rank of 10, significantly surpassing the corresponding metrics for combined training. Similarly, in the out-of-domain context, it yields superior results with the same Median Rank. While a few isolated metrics—such as R@1 for audio in-domain and R@5 for symbolic out-of-domain—are marginally higher in the combined training setup, these exceptions do not contradict the overall trend. These findings underscore the challenges of small-scale annotated datasets. When dealing with limited high-quality annotations, the combined training approach exposes the model to data imbalance issues, where the larger but noisier dataset can potentially overpower the signal from the smaller expert-annotated data. In contrast, the sequential knowledge transfer approach—initially learning generalizable representations from broader data before adapting to specialized piano-specific contexts—enables the model to better leverage both data sources. 

### 5.1.2 Trimodal Integration 

Our results demonstrate the substantial performance gains achieved through trimodal integration compared to bimodal approaches. Across both multi-source training strategies, the trimodal model consistently outperforms both audio-text and symbolic-text configurations. The improvements are particularly pronounced in the pretraining and fine-tuning approach, where trimodal integration achieves a Median Rank of 10 compared to 12 for symbolic-only and 15 for audio-only. This performance advantage extends to higher R@10, with the trimodal approach achieving 52.76%, significantly outperforming both symbolic and audio. 

These findings strongly support our hypothesis that effective representation of piano music requires integrating multiple modalities. While both audio and symbolic representations capture valuable information—with symbolic representations slightly outperforming audio on indomain retrieval—their combination in a trimodal framework yields representations that more comprehensively capture the semantic nuances of piano music. This sug- 

395 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

|Model|Piano<br>i|Item Modality|In|-domain|(199 tra|cks)|Out|-of-dom|ain(88 t|racks)|
|---|---|---|---|---|---|---|---|---|---|---|
||Sifi||||||||||
||pecic||R@1|R@5|R@10|MedR↓|R@1|R@5|R@10|MedR↓|
|CLAP-Music|✗|Audio|0.00|7.38|9.85|54|5.13|20.51|41.03|15|
|TTMR++|✗|Audio|1.47|6.40|12.31|45|5.13|15.38|28.21|16|
|CLaMP3saas|✗|Audio|1.50|7.53|13.56|49|2.56|20.51|41.03|12|
|CLaMP2|✗|Symbolic|3.02|8.54|14.57|43|5.13|30.77|43.59|14|
|CLaMP3<sup>c2</sup><br>sa|✗|Symbolic|4.02|12.06|22.11|39|12.82|30.77|46.15|12|
|CLaMP3saas|✗|Audio + Symbolic|1.50|7.53|12.06|68|2.56|33.33|46.15|13|
|CLaMP3<sup>c2</sup><br>sa|✗|Audio + Symbolic|2.51|10.55|17.58|47|7.69|28.20|43.58|13|
|PianoBind (Ours)|✓|Audio + Symbolic|10.55|35.67|52.76|10|15.38|41.03|51.28|10|



Table 2. Performance comparisons between PianoBind and previous text-to-music retrieval models, conducted on the indomain (PIAST-AT) and out-of-domain (EMOPIA-Caps) datasets. 

gests that audio and symbolic modalities provide complementary perspectives. 

### 5.2 Comparison with Existing Models 

Table 2 presents a comparative analysis between PianoBind and existing text-to-music retrieval models. We compare against leading audio-based models—CLAPMusic, TTMR++, and CLaMP3saas (optimized for audio)—as well as symbolic-based models, including CLaMP2 and CLaMP3<sup>c</sup> sa<sup>2(optimizedforsymbolic).All</sup> models were trained on a large-scale of general-purpose datasets. The results demonstrate PianoBind’s substantial performance advantage over general-purpose models. For in-domain retrieval, PianoBind achieves the lowest Median Rank of 10, significantly outperforming the bestperforming general-purpose model, CLaMP3<sup>c</sup> sa<sup>2,which</sup> achieved a Median Rank of 39. This performance advantage extends to out-of-domain retrieval as well, where PianoBind maintains its lead with an R@10 of 51.28% and Median Rank of 10, compared to the next best model, CLaMP3<sup>c</sup> sa<sup>2, with 46.15% and 12, respectively.</sup> 

Additionally, we also extended the models from CLaMP3, by implementing multimodal item embeddings through feature fusion—which is not present in the original work. However, even with this approach, CLaMP3 models with feature fusion underperform compared to their bi-modality results. This underperformance likely stems from the specialized nature of CLaMP3 variants, where each model was optimized for a specific modality. 

### 5.3 Comparative Analysis of Model Design Choices 

We conducted additional experiments to validate key model design choices. Specifically, we compared our averaged-loss training strategy in trimodal learning with the saas (symbolic → audio → audio → symbolic) alignment strategy adopted in CLaMP3. As shown in Table 3, our averaged-loss training clearly outperforms both the original CLaMP3saas model and our own reimplementation (Ours_saas) in both in-domain and out-of-domain retrieval. These results demonstrate the advantage of jointly learning audio–text and MIDI–text embeddings, rather than aligning independently trained modalities through a 

|Model|I|D|O|OD|
|---|---|---|---|---|
||R@10|MedR↓|R@10|MedR↓|
|CLaMP3_saas|13.56|49|41.03|12|
|Ours_saas|33.66|18|30.77|19|
|Ours_LossAvg|52.76|10|52.76|10|



Table 3. Comparison between Saas and Averaged Loss in trimodal learning in both in-domain (ID) and out-ofdomain (OOD) evaluations. 

staged alignment process. The consistent performance gains in Median Rank and R@10 further highlight the effectiveness of our unified training objective in capturing fine-grained semantic relationships in piano music. 

### 6. CONCLUSION 

In this paper, we introduced PianoBind, a multimodal joint embedding model designed for pop-piano music, integrating audio, symbolic, and textual modalities. Despite using substantially less training data than general-purpose models, PianoBind achieved strong retrieval performance. Our findings suggest that a sequential multi-source training strategy—pre-training on large-scale noisy data followed by fine-tuning on human-annotated examples—is more effective than training on the two sources simultaneously, particularly in low-resource settings. We also observed that integrating audio and symbolic modalities captures complementary semantic cues, and their joint use leads to more robust embeddings. Moreover, combining audio and symbolic embeddings at inference time improves retrieval performance, provided that the modalities are well-aligned through joint training. 

A limitation of our study is that our evaluation datasets, both in-domain and out-of-domain, are relatively smallscale, potentially restricting the generalizability of our findings. Moreover, our datasets primarily focused on poppiano genres, lacking sufficient representation of classical and other diverse piano genres. Addressing these limitations by constructing larger-scale and more genre-diverse piano-text datasets remains an important direction for future work. This further highlights the need for comprehensive benchmarks to rigorously evaluate multimodal embedding models across varied piano music contexts. 

396 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

### 7. ACKNOWLEDGMENTS 

This work has been supported by the collaboration with NCSOFT, Korea. 

### 8. REFERENCES 

- [1] Y.-S. Huang and Y.-H. Yang, “Pop music transformer: Beat-based modeling and generation of expressive pop piano compositions,” in Proceedings of the 28th ACM international conference on multimedia, 2020, pp. 1180–1188. 

- [2] W.-Y. Hsiao, J.-Y. Liu, Y.-C. Yeh, and Y.-H. Yang, “Compound word transformer: Learning to compose full-song music over dynamic directed hypergraphs,” in Proceedings of the AAAI Conference on Artificial Intelligence, vol. 35, no. 1, 2021, pp. 178–186. 

- [3] S.-L. Wu and Y.-H. Yang, “Compose & embellish: Well-structured piano performance generation via a two-stage approach,” in ICASSP 2023 - 2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2023, pp. 1–5. 

- [4] C.-P. Tan, H. Ai, Y.-H. Chang, S.-H. Guan, and Y.-H. Yang, “Picogen2: Piano cover generation with transfer learning approach and weakly aligned data,” in Proceedings of the 25th International Society for Music Information Retrieval Conference (ISMIR), San Francisco, CA, United States, Nov. 2024. 

- [5] S. Sigtia, E. Benetos, and S. Dixon, “An end-to-end neural network for polyphonic piano music transcription,” IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 24, no. 5, pp. 927–939, 2016. 

- [6] C. Hawthorne, E. Elsen, J. Song, A. Roberts, I. Simon, C. Raffel, J. Engel, S. Oore, and D. Eck, “Onsets and frames: Dual-objective piano transcription,” arXiv preprint arXiv:1710.11153, 2017. 

- [7] Q. Kong, B. Li, X. Song, Y. Wan, and Y. Wang, “Highresolution piano transcription with pedals by regressing onset and offset times,” IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 29, pp. 3707–3717, 2021. 

- [8] T. Kwon, D. Jeong, and J. Nam, “Polyphonic piano transcription using autoregressive multi-state note model,” in International Society for Music Information Retrieval Conference, 2020. [Online]. Available: https://api.semanticscholar.org/CorpusID:222125050 

- [9] Y.-H. Chou, I. Chen, C.-J. Chang, J. Ching, Y.-H. Yang et al., “MidiBERT-Piano: Large-scale pre-training for symbolic music understanding,” arXiv preprint arXiv:2107.05223, 2021. 

- [10] X. Liang, Z. Zhao, W. Zeng, Y. He, F. He, Y. Wang, and C. Gao, “Pianobart: Symbolic piano music generation and understanding with large-scale pre-training,” 

in 2024 IEEE International Conference on Multimedia and Expo (ICME), 2024, pp. 1–6. 

- [11] Q. Huang, A. Jansen, J. Lee, R. Ganti, J. Y. Li, and D. P. Ellis, “Mulan: A joint embedding of music audio and natural language,” arXiv preprint arXiv:2208.12415, 2022. 

- [12] I. Manco, E. Benetos, E. Quinton, and G. Fazekas, “Contrastive audio-language learning for music,” in Proceedings of the 23rd International Society for Music Information Retrieval Conference (ISMIR), 2022. 

- [13] Y. Wu*, K. Chen*, T. Zhang*, Y. Hui*, T. BergKirkpatrick, and S. Dubnov, “Large-scale contrastive language-audio pretraining with feature fusion and keyword-to-caption augmentation,” in IEEE International Conference on Acoustics, Speech and Signal Processing, ICASSP, 2023. 

- [14] S. Doh, M. Won, K. Choi, and J. Nam, “Toward universal text-to-music retrieval,” in ICASSP 2023-2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2023, pp. 1–5. 

- [15] S. Doh, M. Lee, D. Jeong, and J. Nam, “Enriching music descriptions with a finetuned-llm and metadata for text-to-music retrieval,” in ICASSP 2024 - 2024 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2024, pp. 826–830. 

- [16] S. Wu, D. Yu, X. Tan, and M. Sun, “Clamp: Contrastive language-music pre-training for cross-modal symbolic music information retrieval,” arXiv preprint arXiv:2304.11029, 2023. 

- [17] S. Wu, Y. Wang, R. Yuan, Z. Guo, X. Tan, G. Zhang, M. Zhou, J. Chen, X. Mu, Y. Gao et al., “Clamp 2: Multimodal music information retrieval across 101 languages using large language models,” arXiv preprint arXiv:2410.13267, 2024. 

- [18] S. Wu, Z. Guo, R. Yuan, J. Jiang, S. Doh, G. Xia, J. Nam, X. Li, F. Yu, and M. Sun, “Clamp 3: Universal music information retrieval across unaligned modalities and unseen languages,” 2025. [Online]. Available: https://arxiv.org/abs/2502.10362 

- [19] H. Bang, E. Choi, M. Finch, S. Doh, S. Lee, G.-H. Lee, and J. Nam, “PIAST: A multimodal piano dataset with audio, symbolic and text,” in Proceedings of the 3rd Workshop on NLP for Music and Audio (NLP4MusA), Nov. 2024, pp. 5–10. 

- [20] Z. Wang, Y. Zhang, Y. Zhang, J. Jiang, R. Yang, J. Zhao, and G. Xia, “Pianotree vae: Structured representation learning for polyphonic music,” arXiv preprint arXiv:2008.07118, 2020. 

- [21] Z. Wang, D. Wang, Y. Zhang, and G. Xia, “Learning interpretable representation for controllable polyphonic 

397 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

music generation,” Proceedings of the 23rd International Society for Music Information Retrieval Conference (ISMIR), 2020. 

- [22] A. Wuerkaixi, C. Benetatos, Z. Duan, and C. Zhang, “Collagenet: Fusing arbitrary melody and accompaniment into a coherent song,” International Society for Music Information Retrieval, 2022. 

- [23] H.-T. Hung, J. Ching, S. Doh, N. Kim, J. Nam, and Y.H. Yang, “EMOPIA: A multi-modal pop piano dataset for emotion recognition and emotion-based music generation,” in Proceedings of 22th International Conference on Music Information Retrieval (ISMIR), 2021. 

- [24] K. He, Y. Wang, and J. Hopcroft, “A powerful generative model using random weights for the deep image representation,” Advances in Neural Information Processing Systems, vol. 29, 2016. 

- [25] Y. Liu, M. Ott, N. Goyal, J. Du, M. Joshi, D. Chen, O. Levy, M. Lewis, L. Zettlemoyer, and V. Stoyanov, “Roberta: A robustly optimized BERT pretraining approach,” CoRR, vol. abs/1907.11692, 2019. [Online]. Available: http://arxiv.org/abs/1907. 11692 

- [26] A. v. d. Oord, Y. Li, and O. Vinyals, “Representation learning with contrastive predictive coding,” arXiv preprint arXiv:1807.03748, 2018. 

- [27] J. Gardner, I. Simon, E. Manilow, C. Hawthorne, and J. Engel, “Mt3: Multi-task multitrack music transcription,” arXiv preprint arXiv:2111.03017, 2021. 

- [28] Y. Wu, K. Chen, T. Zhang, Y. Hui, T. Berg-Kirkpatrick, and S. Dubnov, “Large-scale contrastive languageaudio pretraining with feature fusion and keyword-tocaption augmentation,” in ICASSP 2023-2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2023, pp. 1–5. 

- [29] S. Doh, K. Choi, J. Lee, and J. Nam, “Lp-musiccaps: Llm-based pseudo music captioning,” in ISMIR, 2023. 

- [30] A. Guzhov, F. Raue, J. Hees, and A. Dengel, “Audioclip: Extending clip to image, text and audio,” in ICASSP 2022-2022 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2022, pp. 976–980. 

- [31] OpenAI, “Chatgpt-4o (gpt-4 omni),” https://openai. com/index/gpt-4o, 2024, accessed: 2025-03-26. 

398 

