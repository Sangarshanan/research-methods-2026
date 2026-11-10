---
paper_id: "000075"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706547/files/000075.pdf"
---

# IDOLSONGSJP CORPUS: A MULTI-SINGER SONG CORPUS IN THE STYLE OF JAPANESE IDOL GROUPS 

Hitoshi Suda<sup>1</sup> Junya Koguchi<sup>2</sup> Shunsuke Yoshida<sup>3</sup> Tomohiko Nakamura<sup>1</sup> Satoru Fukayama<sup>1</sup> Jun Ogata<sup>1</sup> 1 National Institute of Advanced Industrial Science and Technology (AIST), Tokyo, Japan 2 Meiji University, Tokyo, Japan 3 The University of Tokyo, Tokyo, Japan 

```
suda.h@aist.go.jp,korguchi@gmail.com
```

## ABSTRACT 

Japanese idol groups, comprising performers known as “idols,” are an indispensable part of Japanese pop culture. They frequently appear in live concerts and television programs, entertaining audiences with their singing and dancing. Similar to other J-pop songs, idol group music covers a wide range of styles, with various types of chord progressions and instrumental arrangements. These tracks often feature numerous instruments and employ complex mastering techniques, resulting in high signal loudness. Additionally, most songs include a song division (utawari) structure, in which members alternate between singing solos and performing together. Hence, these songs are wellsuited for benchmarking various music information processing techniques such as singer diarization, music source separation, and automatic chord estimation under challenging conditions. Focusing on these characteristics, we constructed a song corpus titled IdolSongsJp by commissioning professional composers to create 15 tracks in the style of Japanese idol groups. This corpus includes not only mastered audio tracks but also stems for music source separation, dry vocal tracks, and chord annotations. This paper provides a detailed description of the corpus, demonstrates its diversity through comparisons with real-world idol group songs, and presents its application in evaluating several music information processing techniques. 

## 1. INTRODUCTION 

Processing music audio signals is one of the major directions in the music information retrieval (MIR) field [1, 2]. The techniques include beat tracking [3, 4], fundamental frequency estimation [5, 6], automatic musical chord estimation [7–9], music source separation (MSS) [10,11], and automatic lyrics transcription (ALT) [12,13]. 

Training and evaluating MSS techniques in a supervised manner requires a corpus consisting of ground-truth stems, 

> © H. Suda, J. Koguchi, S. Yoshida, T. Nakamura, S. Fukayama, and J. Ogata. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: H. Suda, J. Koguchi, S. Yoshida, T. Nakamura, S. Fukayama, and J. Ogata, “IdolSongsJp Corpus: A Multi-Singer Song Corpus in the Style of Japanese Idol Groups”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

i.e., isolated acoustic signals categorized by instrument type. Such corpora include MUSDB18 [14, 15] and MoisesDB [16], which have been widely used for training and evaluating source separation methods [17]. On the other hand, some studies have shown that these corpora tend to exhibit lower loudness levels compared to commercially available tracks and have evaluated realistic performance on extended corpora by amplifying existing tracks to match commercial loudness levels [18]. However, some of the tracks in these corpora still feature fewer instruments and simpler mastering effects compared to contemporary commercial tracks, which makes practical performance evaluation challenging. A more realistic assessment of MSS for contemporary songs requires constructing a music corpus that closely emulates the characteristics of these tracks. 

In the field of music information processing, various techniques for multi-singer songs have also been explored, such as the separation of overlapping vocal signals [19]. Several corpora have been constructed for the study of such techniques, such as the jaCappella corpus and MedleyVox [20, 21]. In songs where singer combinations change between sections, key challenges include identifying which parts are sung by which singers and at what time. In Japanese idol groups, such structures are referred to as song division (utawari in Japanese), which is intentionally designed to enhance both the appeal of the song and the individuality of each idol [22–24]. Such information is vital not only for music appreciation but also for applications such as music video production and live concert arrangements. Similarly, for K-pop dance groups, line distribution videos that visualize song division structures have been widely shared on platforms such as TikTok and YouTube. The automatic recognition of these structures from music signals is known as singer diarization [25]. Several studies have proposed specialized methods tailored for J-pop songs and have also constructed a dedicated corpus [23,24]. In summary, these studies suggest that focusing on multi-singer songs will further advance the field of music information processing. 

Another important aspect of music information processing is active music listening, which involves interactive interfaces that enable listeners to better understand and appreciate music with the help of music understanding techniques [26]. Studies on active music listening interfaces require preparing target songs and evaluating them through 

647 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

user interactions with the proposed interfaces. While using commercial tracks for these evaluations is desirable, obtaining permission from individual copyright holders (e.g., record companies) is often challenging. Similarly, some research-oriented song corpora, such as the RWC Music Database [27], also require permission for public distribution, and conducting online evaluation experiments poses copyright concerns. Thus, to advance research in this area, it is essential to construct a music corpus whose license explicitly permits research use and public sharing. 

This study aims to construct a high-loudness corpus of multi-singer songs that can be distributed online and accessible to both researchers and ordinary listeners. To address this challenge, we focus on Japanese idol group songs, which are well-suited for music information processing applications owing to their complex instrumental and vocal arrangements, commercial-level loudness, and diverse musical styles. In addition, these idol group songs are indispensable elements of Japanese pop culture. For instance, at the 2024 Japan Record Awards<sup>1</sup> , FRUITS ZIPPER’s “NEW KAWAII” received the Best Piece Award, and Cho Tokimeki♥Sendenbu’s “Saijokyu ni Kawaii no!” received the Best Lyrics Award. Given their cultural and technical importance, we commissioned professional creators to compose 15 songs in the style of Japanese idol groups and constructed a corpus titled IdolSongsJp. These tracks are mastered to a loudness level comparable to commercial songs and feature realistic song division (utawari) structures and diverse chord progressions. Furthermore, the corpus includes not only mastered tracks but also stems designed for source separation, dry solo vocal tracks for each singer, and musical chord annotations, enabling a wide range of evaluations in music information processing. To advance studies on music listening applications, we made this corpus publicly distributable for non-commercial use. This paper presents the aim and detailed description of the corpus and demonstrates the diversity of the songs by comparing them with real-world idol group songs. This paper also shows the application of the corpus by evaluating several fundamental MIR techniques. 

## 2. IDOLSONGSJP CORPUS: A MULTI-SINGER CORPUS IN THE JAPANESE IDOL GROUP STYLE 

We constructed a novel corpus titled IdolSongsJp, comprising 15 multi-singer songs in the style of Japanese idol groups. This corpus features 10 female and 8 male singers, all of whom are professionals or semiprofessionals, and each of the 15 songs features a unique combination of singers. All creators are professionals with experience providing songs to real idol groups. Each individual contributed to no more than three songs to ensure a diverse range of creative styles across the corpus. Each song was designed to exhibit distinctive characteristics that reflect the diverse styles observed in Japanese idol group songs. Table 1 presents the list of songs along with their keywords and core concepts. This 

> 1 `https://www.tbs.co.jp/recordaward/` 

corpus is available at `https://huggingface.co/ datasets/imprt/idol-songs-jp` . 

The songs exhibit several characteristics typical of Japanese idol songs, as described below: 

- Song division (utawari) structures. In this structure, the vocal arrangements vary across different sections of each song. Different singers take turns line by line, with some sections sung solo and others performed by multiple singers simultaneously. In addition, the songs feature countermelodies, harmonies, and choral sections (e.g., “oohs” and “ahhs”), which are characteristic of J- pop songs. 

- Various music styles. This corpus comprises a diverse range of music styles, including pop songs as well as genres such as UK Garage (M05), ballads (F05 and M06), rock (M03), and dance music (F08). 

- Various lyrical themes. While love songs (e.g., F02, F04, M04, M06) are common in idol songs, some songs feature alternative themes, such as selfintroduction (F01) and topics related to idol groups (F06). 

- High loudness. The mastering process targeted a loudness of −7 LUFS, similar to that of commercial idol group songs. Since some creators release lowloudness versions for online platforms, such as Spotify and YouTube, this corpus also includes tracks mastered to a target loudness of −9 LUFS. 

- Reflection of Japanese idol culture. At idol group concerts, audiences frequently cheer and shout in response to the performances. Specifically, tracks F01, F07, and M01 incorporate cheers, shouts, and chants (referred to as calls and mixes in Japanese [28]) into their recordings. 

This corpus comprises several types of data that are suitable for evaluating various music information processing techniques. Figure 1 shows the data types organized according to the song production process. All audio signals were sampled at 48 kHz and encoded in 32-bit floatingpoint format to make dithering unnecessary. The following list shows the included data: 

- Stems. These stems were created by linearly mixing instrumental signals according to their respective categories and applying bus effects. The category definitions were derived from MoisesDB [16]. 

- Stems for MSS. This corpus employs four categories: drums, bass, vocals, and other. These signals were created by linearly mixing the corresponding stems and applying mastering effects. 

- Dry vocal tracks. The corpus contains 414 individual dry vocal tracks, including lead melodies, countermelodies, harmonies, choruses, and chants. Each singer recorded the whole song, and final vocals in the mastered tracks were trimmed based on the designated song division structures. The tracks were 

648 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

|ID|Title|Tempo|No. of singers|No. of stems|Keywords and core concepts|
|---|---|---|---|---|---|
|F01|Introjuice|186 bpm|7|15|Self-introduction; audience interaction (callsandmixes)|
|F02|Aoharu Syndrome|190 bpm|6|11|Rapidly unfolding lyrical narrative|
|F03|Awake|175 bpm|5|12|Frequent key changes (11 times)|
|F04|Awanai Kagi|123 bpm|8|13|Dance music with acoustic piano and guitar; questioning lyrics|
|F05|Kaerimichi|90 bpm|6|14|Heartbreak ballad; metaphorical lyrics; no multi-singer sections|
|F06|Ima, Sekai wa Kagayaiteru|132 bpm|4|12|Topics related to idol groups; metaphorical lyrics|
|F07|Illuminyati|160 bpm|7|11|Coined word; wordplay; audience interaction (chants)|
|F08|tic-tac-toe|120 bpm|9|10|Vocal doubling; vocoder effects; rap; code-switching with English|
|M01|Liberty wing|135 bpm|8|15|Introduction of other members; audience interaction (calls)|
|M02|trick star|134 bpm|7|17|Augmented chords; high stem count|
|M03|Answer|185 bpm|6|12|Rock; ateji (alternate kanji pronunciations)|
|M04|Uraomote Docchi?|157 bpm|7|10|Release cut piano; Vocaloid style|
|M05|Deep breath|130 bpm|5|8|UK Garage; rap; code-switching with English; vocal chops|
|M06|Soredemo, Sukidayo|78 bpm|4|11|Heartbreak ballad; ad-libbed vocals and piano|
|M07|“Suki” no Aizu|138 bpm|6|12|Three members singing an octave lower; long spoken lines|



Table 1. Songs in the IdolSongsJp corpus. The prefix of each song ID (F or M) indicates the gender of the singers. 



<!-- Start of picture text -->
[Instruments] [Stems] [Master�bus�(w/o�limiter)] [Mastered]<br>Kick Track�effects<br>Pro-L�2 Mastered<br>Snare Track�effects Bus�effects drums +0dB –9LUFS<br>Hi-hat Track�effects perc_atonal no_limit<br>Master�effects<br>(–9LUFS)<br>Pro-L�2 Mastered<br>E.Gt.�(Left) Track�effects<br>Bus�effects egt +2dB –7LUFS<br>E.Gt.�(Right) Track�effects<br>fx<br>piano<br>Singer�1�Lead Track�effects [Stems�for�music�source�separation]<br>Bus�effects vocal_lead<br>Singer�2�Lead Track�effects Master�effects drums Pro-L�2 drums<br>Master�effects other Pro-L�2 other<br>Singer�1�Harmon y Track�effects Master�effects vocals Pro-L�2 vocals<br>Bus�effects vocal_bg<br>Singer�2�Harmon y Track�effects Master�effects bass Pro-L�2 bass<br>…<br><!-- End of picture text -->

Figure 1. Overview of the production process for songs in the IdolSongsJp corpus. Data types included in the corpus are highlighted in red. 

processed using specialized software (e.g., Melodyne<sup>2</sup> ) to adjust pitch and timing. These processed tracks can be utilized to train and evaluate singing voice synthesis techniques. 

- Master bus signals without limiters. These signals were produced by linearly mixing the stems and applying mastering effects except the final limiter. 

- Mastered tracks at −7 LUFS and −9 LUFS. For maximization and limiting, we used the Modern preset of FabFilter Pro-L 2<sup>3</sup> . The loudness of the tracks mastered to a target of −7 LUFS ranges between −7.1 LUFS and −7.0 LUFS, based on the ITU-R BS.1770-3 standard [29]. The tracks have been designed and mastered based on the −7 LUFS version. 

- Off-vocal tracks and minus-one vocal tracks. These signals were generated using the same process as for the mastered tracks, except that the vocal signals were excluded. Minus-one vocal tracks include backing harmonies and choruses. The corpus includes these versions in the same three mastering 

> 2 `https://www.celemony.com/en/melodyne/` 

> `what-is-melodyne` 

> 3 `https://www.fabfilter.com/products/ pro-l-2-limiter-plug-in` 

types as described above. 

- Solo versions. Each of the 95 solo version tracks was mastered by mixing instrumental signals with the corresponding solo vocal signal, meaning that each track features the vocal performance of only one specific singer. Therefore, the corpus can also be utilized as a solo song corpus. Each track is available in the same three mastering types as described above. 

- Key and chord annotations in Harte’s shorthand notation [30] with time information. These annotations are based on the consensus of at least two hired expert annotators. 

The authors retain all copyrights to the corpus. This corpus is available free of charge for non-commercial research and entertainment purposes. No prior consent is required for such uses. Any commercial use of the corpus requires prior permission from the authors. Users may rearrange, parody, and apply machine learning techniques to the corpus, provided that the creators’ moral rights are upheld. To protect the rights associated with software instruments and commercial sample libraries, sampling the instrumental tracks to create unrelated content or to train machine learning models is prohibited. 

649 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



Figure 2. Visualization of music embeddings extracted from real-world idol group songs and songs from our corpus. Each gray dot represents a real-world idol group song, while red and blue dots indicate songs from our corpus featuring female and male vocals, respectively. 

## 3. COMPARISON WITH REAL-WORLD IDOL GROUP SONGS 

The IdolSongsJp corpus is designed to capture the diverse styles of idol group music. This section demonstrates the style diversity of the songs in our corpus by comparing their music embeddings to those derived from real-world idol group songs. 

We processed 4,483 publicly available preview tracks performed by 234 female idol groups, which we obtained from a music subscription service. To mitigate the effects of vocal characteristics and variations in the number of singers, we extracted the accompaniment signals using the fine-tuned model of Hybrid Transformer Demucs (HT Demucs) [11, 17]. We then extracted 512-dimensional embeddings from these signals using a contrastive language–audio pretraining (CLAP) model [31]. Subsequently, we reduced the dimensionality of these embeddings to two using uniform manifold approximation and projection (UMAP) [32]. We also extracted embeddings from the songs in our corpus and reduced their dimensionality using the same UMAP parameters as previously described. The CLAP model was `music_audioset_epoch_15_esc_90.14`<sup>4</sup> , which is designed for music signals. In this comparison, all real-world songs were performed by female groups, as these songs are generally more accessible and wellorganized online than those by male groups. Nonetheless, this section treats all songs in the IdolSongsJp corpus uniformly since vocal characteristics were mitigated. 

Figure 2 shows the results. The embedding space reveals a continuous distribution of songs without forming distinct clusters. The figure shows that the songs in our 

corpus are broadly distributed across the embedding space, indicating a wide variety of styles. Tracks located near the periphery of the embedding space exhibit unique styles, while those near the center tend to have more common idol group characteristics. This suggests that the corpus includes both distinctive songs (e.g., F05, F06, F08) and more typical ones (e.g., F01, M04). Moreover, the absence of data points in certain regions of the embedding space, such as the upper right region, suggests directions for further expansion of the corpus. 

## 4. APPLICATION 1: MUSIC SOURCE SEPARATION 

As mentioned in Section 2, the IdolSongsJp corpus includes stem signals, which help the evaluation of MSS techniques. In this section, we evaluate the performance of the fine-tuned model of HT Demucs [11, 17], which separates music signals into four stems: bass, drums, vocals, and other. We evaluated the performance using three types of input signals, all of which are provided in the corpus: 

1. Linear summation of stems without mastering effects. The stems are summed linearly without any additional mastering processing. 

2. Mastered tracks at −9 LUFS. For these tracks, the same mastering effects as those used in producing the mastered tracks were applied to the groundtruth stems. 

3. Mastered tracks at −7 LUFS. The only difference from condition 2 is the gain parameter applied to the final limiter. 

Since mastering effects include not only maximizers and limiters but also equalizers, stereo imaging plug-ins, and other processing plug-ins, the final mixed signals differ considerably from the raw stems. To address this discrepancy, we applied the same mastering effects to the individual stems in conditions 2 and 3 so that the acoustic conditions of the reference stems approximately matched those of the mastered tracks. Note that since most mastering effects are nonlinear, simply summing the processed stems does not reproduce the final mastered tracks. These effects were applied to each stem solely to approximate the overall acoustic conditions, such as loudness and stereo balances. In this evaluation, signal-to-distortion ratio (SDR) was used as the evaluation metric. 

Figure 3 shows the separation results. For condition 1 (linear summation of stems), the separation performance was comparable to that observed with MUSDB18HQ [15], demonstrating the effectiveness of the HT Demucs model. In contrast, when processing the mastered signals, the separation performance deteriorated, particularly for drums and vocals, and was lower than previously reported for existing high-loudness music corpora [18]. One possible explanation is that certain mastering effects are designed to smooth, glue, and saturate the tracks and induce interactions between stems, thereby complicating MSS. Notably, the mastered signals for track 

4 `https://huggingface.co/lukewys/laion_clap` 

650 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



Figure 3. Signal-to-distortion ratios (SDR) for separated signals from the IdolSongsJp corpus, obtained using the fine-tuned model of HT Demucs [11, 17]. Dots indicate outliers that lie more than 1.5 times the interquartile range away from the quartiles. 

M05, “Deep breath,” exhibited the lowest separation performance across all stems. Because this song is based on UK Garage, its sound design, especially the bass, differs considerably from the typical one found in pop and rock music. These findings suggest that enhancing the diversity of genres and effects in the training tracks may be necessary to further improve the performance of MSS techniques. Furthermore, the results indicate potential limitations in the current categorization of instruments, suggesting that target source separation techniques [33] will be required for more effective applications. 

## 5. APPLICATION 2: AUTOMATIC CHORD ESTIMATION 

As mentioned in Section 2, the IdolSongsJp corpus contains musical chord annotations provided by expert annotators. Figure 4 shows the occurrence rates of chord qualities, excluding chord roots, inversions, tensions, and non-chorded sections. The proportion of major and minor chords is 50%, which is significantly lower than the 65% observed in the McGill Billboard corpus [34], a reference corpus used in the Music Information Retrieval Evaluation eXchange (MIREX) competition. In contrast, the corpus includes a large number of tetrads and pentads (e.g., seventh and ninth chords), as well as diminished (dim) and augmented (aug) chords. Therefore, effective chord estimation for this corpus requires a model with a large chord vocabulary capable of covering these diverse chord types. 

We applied and evaluated two open-source chord estimation methods on the IdolSongsJp corpus. The first method is based on multitask classification of chord attributes (e.g., root, quality, bass, and seventh) using bi-directional long short-term memory (Bi-LSTM) net- 



Figure 4. Distribution of chord qualities in the IdolSongsJp corpus, represented using Harte’s shorthand notation [30]. Chord roots, inversions, tension notes, and nonchorded segments are excluded. The 7sus4 chord, which is not defined in this notation or in the open-source evaluation package `mir_eval` , is composed of (1, 4, 5, ♭7). 

works<sup>5</sup> [35]. The second is an end-to-end method based on bi-directional Transformers<sup>6</sup> [36]. Both methods can handle recognition tasks involving a large chord vocabulary. Figure 5 shows the chord estimation results. For root note estimation and major/minor chord estimation, both methods achieved accuracies exceeding 80%, demonstrating their effectiveness on this corpus. However, the recognition accuracy for tetrads was below 60% for both methods, indicating limitations in handling larger chord vocabulary. In the figure, the MIREX4 column represents the recognition accuracy for chords consisting of four or more notes, where at least four component notes must be correctly identified. In this case, the accuracy was below 30% for both methods, indicating a large room for improvement in recognizing chords with complex structures. In summary, chord estimation involving an extended chord vocabulary, such as tetrads and beyond, remains challenging for current methods. 

## 6. APPLICATION 3: AUTOMATIC LYRICS TRANSCRIPTION 

As described in Sections 2 and 3, the songs in the IdolSongsJp corpus cover a wide range of musical styles with a variety of genres, tempos, and lyrical themes. Therefore, the corpus serves as a benchmark dataset for various natural language processing tasks involving lyrics in diverse 

> 5 `https://github.com/music-x-lab/ ISMIR2019-Large-Vocabulary-Chord-Recognition` 6 `https://github.com/jayg996/BTC-ISMIR19` 

651 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



Figure 5. Chord estimation accuracies using two opensource methods [35, 36]. Evaluation metrics are based on the Music Information Retrieval Evaluation eXchange (MIREX) competition and the implementation in the opensource package `mir_eval` . The MIREX4 column indicates the recognition accuracy for chords consisting of four or more notes, where at least four component notes must be correctly identified. Dots indicate outliers that lie more than 1.5 times the interquartile range away from the quartiles. 

musical contexts. For example, this section evaluates the performance of automatic lyrics transcription (ALT) using existing automatic speech recognition (ASR) techniques. 

We utilized two ASR methods to perform ALT. The first method uses Whisper with its large model [37]. The language tag for Japanese was provided as input to its Transformer decoder. The second method is based on a Conformer model [38] that accepts Hidden-Unit BERT (HuBERT) [39] features. For the HuBERT model, we used `kushinada-hubert-large`<sup>7</sup> [40]. The Conformer model was trained on LaboroTVSpeech, a large-scale Japanese speech corpus derived from television broadcasts [41]. Both methods were designed for general ASR and were not specifically tailored for ALT. In this evaluation, we used three types of input signals: (1) mastered tracks at −7 LUFS, (2) vocal signals separated from the mastered tracks using the fine-tuned model of HT Demucs, and (3) raw lead vocal stems without any mastering effects. 

Table 2 presents the character error rates (CERs) for the transcription results. The performance of the Whisper model remained consistent across all three input conditions. This consistency, as reported also in previous studies [42], demonstrates the robustness of Whisper against accompaniment signals and degradation caused by MSS. In contrast, the results indicate that the Conformer model with HuBERT features was more negatively affected by 

||S [%]|D[%]|I [%]|CER [%]|
|---|---|---|---|---|
|Whisper [37]|||||
|Mastered tracks|10.3|8.7|21.8|40.7|
|+Demucs|8.1|15.7|20.0|43.8|
|Lead vocals|7.9|14.1|17.7|39.7|
|HuBERT+Conform|er [38–4|0]|||
|Mastered tracks|13.4|59.8|2.5|75.6|
|+Demucs|16.3|26.1|5.1|47.5|
|Lead vocals|15.1|21.5|5.2|41.8|



Table 2. Character error rates (CERs) for automatic lyrics transcription. Columns S, D, and I represent substitution, deletion, and insertion error rates, respectively. The CER column shows the total character error rate, the sum of these three error types. Rows labeled Mastered tracks correspond to tracks mastered at −7 LUFS; +Demucs indicates separated vocal signals obtained from these mastered tracks using HT Demucs; and Lead vocals indicates the raw lead vocal stems without mastering effects. 

accompaniment signals, despite having been trained on data that included music TV programs. The two systems demonstrated different error tendencies: the Whisper model tended to produce insertion errors, while the Conformer model frequently generated deletion errors, with insertion errors occurring rarely. Moreover, the Whisper model often produced hallucinated outputs, such as “thank you for your watching.” Conversely, the Conformer model tended to skip over fast segments and failed to recognize English phrases accurately, which contributed to its frequent deletion errors. 

## 7. CONCLUSION 

We constructed the IdolSongsJp corpus, a novel multisinger song corpus in the style of Japanese idol groups. The corpus includes not only mastered tracks but also stems for evaluating MSS techniques, dry vocal tracks, solo versions for all song–singer pairs, and chord annotations provided by expert annotators. The songs cover a wide range of musical styles observed in Japanese idol groups, encompassing diverse genres, tempos, song division patterns, and lyrical themes. Therefore, the corpus serves as a realistic resource not only for general tasks, such as MSS and automatic chord estimation, but also for song-specific applications, such as audience interaction enhancement and piano arrangement generation. 

The IdolSongsJp corpus explicitly focuses on song division (utawari) structures, making it well-suited for multisinger tasks such as singer diarization and multi-pitch detection. Future directions include applying this corpus to the development and evaluation of such tasks specific to multi-singer songs. Furthermore, extending this approach to popular music genres from other regions, such as Korean and Chinese pop, may further broaden the applicability of music information processing techniques, particularly those for multi-singer songs. 

7 `https://huggingface.co/imprt/ kushinada-hubert-large` 

652 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 8. ACKNOWLEDGMENTS 

This research was partially supported by the AIST policybased budget project “R&D on Generative AI Foundation Models for the Physical Domain.” The authors would like to acknowledge Mr. Takizawa (AIST) for his support in the speech recognition evaluation. 

## 9. ETHICS STATEMENT 

This corpus includes instrument stems and dry vocal tracks, which may be used for music generation and related applications. Instrument stems may be utilized to create new musical content through music generation techniques or sampling, potentially infringing on the rights of these sources. Vocal signals may also enable synthetic speech that is unethical or impersonates others. To address these concerns, such uses are explicitly prohibited under the license provided at the distribution repository. 

## 10. REFERENCES 

- [1] M. Müller, D. P. W. Ellis, A. Klapuri, and G. Richard, “Signal processing for music analysis,” IEEE journal of selected topics in signal processing, vol. 5, no. 6, pp. 1088–1110, 2011. 

- [2] H. Purwins, B. Li, T. Virtanen, J. Schluter, S.-Y. Chang, and T. Sainath, “Deep learning for audio signal processing,” IEEE journal of selected topics in signal processing, vol. 13, no. 2, pp. 206–219, 2019. 

- [3] M. Goto, “An audio-based real-time beat tracking system for music with or without drum-sounds,” Journal of new music research, vol. 30, no. 2, pp. 159–171, 2001. 

- [4] L. Jean, “Efficient tempo and beat tracking in audio recordings,” Journal of the Audio Engineering Society. Audio Engineering Society, vol. 51, pp. 226–233, 2003. 

- [5] M. Goto, “A robust predominant-F0 estimation method for real-time detection of melody and bass lines in CD recordings,” in Proc. 2000 IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP), vol. 2, 2000, pp. 757–760. 

- [6] J. Salamon, E. Gomez, D. P. W. Ellis, and G. Richard, “Melody extraction from polyphonic music signals: Approaches, applications, and challenges,” IEEE Signal Processing Magazine, vol. 31, no. 2, pp. 118–134, 2014. 

- [7] H.-T. Cheng, Y.-H. Yang, Y.-C. Lin, I.-B. Liao, and H. H. Chen, “Automatic chord recognition for music classification and retrieval,” in Proc. 2008 IEEE International Conference on Multimedia and Expo, 2008, pp. 1505–1508. 

- [8] N. Boulanger-Lewandowski, Y. Bengio, and P. Vincent, “Audio chord recognition with recurrent neural 

networks,” in Proc. 14th International Society for Music Information Retrieval Conference (ISMIR 2013), 2013. 

- [9] F. Korzeniowski and G. Widmer, “A fully convolutional deep auditory model for musical chord recognition,” in Proc. 2016 IEEE 26th International Workshop on Machine Learning for Signal Processing (MLSP), 2016, pp. 1–6. 

- [10] T. Virtanen, “Monaural sound source separation by nonnegative matrix factorization with temporal continuity and sparseness criteria,” IEEE Transactions on Audio, Speech, and Language Processing, vol. 15, no. 3, pp. 1066–1074, 2007. 

- [11] A. Défossez, “Hybrid spectrogram and waveform source separation,” in Proc. ISMIR 2021 Music Demixing Workshop, 2021, pp. 1–11. 

- [12] A. Mesaros and T. Virtanen, “Automatic recognition of lyrics in singing,” EURASIP Journal on Audio, Speech, and Music Processing, vol. 2010, no. 1, pp. 1–11, 2010. 

- [13] X. Gao, C. Gupta, and H. Li, “Automatic lyrics transcription of polyphonic music with lyrics-chord multitask learning,” IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 30, pp. 2280– 2294, 2022. 

- [14] Z. Raf **i** , A. Liutkus, F.-R. Stöter, S. I. Mimilakis, and R. Bittner, “The MUSDB18 corpus for music separation,” 2017. [Online]. Available: https://doi.org/ 10.5281/zenodo.1117372 

- [15] ——, “MUSDB18-HQ - an uncompressed version of MUSDB18,” 2019. [Online]. Available: https: //doi.org/10.5281/zenodo.3338373 

- [16] I. Pereira, F. Araújo, F. Korzeniowski, and R. Vogl, “MoisesDB: A dataset for source separation beyond 4- stems,” in Proc. 24th International Conference on Music Information Retrieval Conference (ISMIR 2023), 2023, pp. 619–626. 

- [17] S. Rouard, F. Massa, and A. Défossez, “Hybrid transformers for music source separation,” in Proc. 2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2023, pp. 1–5. 

- [18] C.-B. Jeon and K. Lee, “Towards robust music source separation on loud commercial music,” in Proc. 23rd International Society for Music Information Retrieval Conference (ISMIR 2022), 2022. 

- [19] D. Petermann, P. Chandna, H. Cuesta, J. Bonada, and E. Gomez, “Deep learning based source separation applied to choir ensembles,” in Proc. 21st International Society for Music Information Retrieval Conference (ISMIR 2020), 2020. 

653 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [20] T. Nakamura, S. Takamichi, N. Tanji, S. Fukayama, and H. Saruwatari, “jaCappella Corpus: A Japanese a cappella vocal ensemble corpus,” in Proc. 2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2023, pp. 1–5. 

- [21] C.-B. Jeon, H. Moon, K. Choi, B. S. Chon, and K. Lee, “MedleyVox: An evaluation dataset for multiple singing voices separation,” in Proc. 2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2023, pp. 1–5. 

- [22] Y. Okada, Ed., Living with Idols (in Japanese). Pot Publishing, 2013. 

- [23] H. Suda, D. Saito, S. Fukayama, T. Nakano, and M. Goto, “Singer diarization for polyphonic music with unison singing,” IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 30, pp. 1531–1545, 2022. 

- [24] H. Suda, S. Yoshida, T. Nakamura, S. Fukayama, and J. Ogata, “FruitsMusic: A real-world corpus of Japanese idol-group songs,” in Proc. 25th International Society for Music Information Retrieval Conference (ISMIR 2024), 2024. 

- [25] M. Thlithi, C. Barras, J. Pinquier, and T. Pellegrini, “Singer diarization: Application to ethnomusicological recordings,” in Proc. 5th International Workshop on Folk Music Analysis (FMA 2015), 2015, pp. 124– 125. 

- [26] M. Goto, “Active music listening interfaces based on signal processing,” in Proc. 2007 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), vol. 4, 2007, pp. IV–1441–IV–1444. 

- [27] M. Goto, H. Hashiguchi, T. Nishimura, and R. Oka, “RWC music database: Popular, classical and jazz music databases,” in Proc. 3rd International Conference on Music Information Retrieval Conference (ISMIR 2002), 2002. 

- [28] W. Xie, “Japanese “idols” in trans-cultural reception: the case of AKB48,” in The Art of Reception, J. Bracker and A.-K. Hubrich, Eds., 2021, pp. 371–399. 

- [29] Radiocommunication Sector of International Telecommunication Union (ITU-R), “Recommendation ITU-R BS.1770-3: Algorithms to measure audio programme loudness and true-peak audio level,” 2012. 

- [30] C. Harte, M. B. Sandler, S. A. Abdallah, and E. Gómez, “Symbolic representation of musical chords: A proposed syntax for text annotations,” in Proc. 6th International Conference on Music Information Retrieval (ISMIR 2005), 2005, pp. 66–71. 

- [31] Y. Wu, K. Chen, T. Zhang, Y. Hui, M. Nezhurina, T. Berg-Kirkpatrick, and S. Dubnov, “Large-scale contrastive language-audio pretraining with feature fusion and keyword-to-caption augmentation,” arXiv [cs.SD], 2022. 

- [32] L. McInnes, J. Healy, N. Saul, and L. Großberger, “UMAP: Uniform manifold approximation and projection,” Journal of open source software, vol. 3, no. 29, p. 861, 2018. 

- [33] X. Liu, H. Liu, Q. Kong, X. Mei, J. Zhao, Q. Huang, M. D. Plumbley, and W. Wang, “Separate what you describe: Language-queried audio source separation,” in Proc. Interspeech 2022, 2022, pp. 1801–1805. 

- [34] J. A. Burgoyne, J. Wild, and I. Fujinaga, “An expert ground truth set for audio chord recognition and music analysis,” in Proc. 12th International Society for Music Information Retrieval Conference (ISMIR 2011), 2011. 

- [35] J. Jiang, K. Chen, W. Li, and G. Xia, “Largevocabulary chord transcription via chord structure decomposition,” in Proc. 20th International Society for Music Information Retrieval Conference (ISMIR 2019), 2019. 

- [36] J. Park, K. Choi, S. Jeon, D. Kim, and J. Park, “A bi-directional Transformer for musical chord recognition,” in Proc. 20th International Society for Music Information Retrieval Conference (ISMIR 2019), 2019. 

- [37] A. Radford, J. W. Kim, T. Xu, G. Brockman, C. McLeavey, and I. Sutskever, “Robust speech recognition via large-scale weak supervision,” in Proc. 40th International Conference on Machine Learning (ICML’23), 2022, pp. 28 492–28 518. 

- [38] A. Gulati, J. Qin, C.-C. Chiu, N. Parmar, Y. Zhang, J. Yu, W. Han, S. Wang, Z. Zhang, Y. Wu, and R. Pang, “Conformer: Convolution-augmented transformer for speech recognition,” in Proc. Interspeech 2020, 2020, pp. 5036–5040. 

- [39] W.-N. Hsu, B. Bolte, Y.-H. H. Tsai, K. Lakhotia, R. Salakhutdinov, and A. Mohamed, “HuBERT: Selfsupervised speech representation learning by masked prediction of hidden units,” IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 29, pp. 3451–3460, 2021. 

- [40] D. Takizawa, T. Nakamura, H. Suda, and S. Fukayama, “Automatic speech recognition of Japanese dialects using large-scale self-supervised learning models (in Japanese),” in Proc. 2025 Spring Meeting of the Acoustical Society of Japan, 2025. 

- [41] S. Ando and H. Fujihara, “Construction of a large-scale Japanese ASR corpus on TV recordings,” in Proc. 2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2021, pp. 6948– 6952. 

- [42] O. Cífka, H. Schreiber, L. Miner, and F.-R. Stöter, “Lyrics transcription for humans: A readabilityaware benchmark,” in Proc. 25th International Society for Music Information Retrieval Conference (ISMIR 2024), 2024. 

654 

