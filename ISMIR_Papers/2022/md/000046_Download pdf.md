---
paper_id: "000046"
year: 2022
title: "Download pdf"
source_url: "https://zenodo.org/record/7316680/files/000046.pdf"
---

# ANALYSIS AND DETECTION OF SINGING TECHNIQUES IN REPERTOIRES OF J-POP SOLO SINGERS 

Yuya Yamamoto<sup>1</sup> Juhan Nam<sup>2</sup> Hiroko Terasawa 1 Doctoral Program in Informatics, University of Tsukuba, Japan 

Juhan Nam<sup>2</sup> Hiroko Terasawa<sup>1</sup> 

2 Graduate School of Culture Technology, KAIST, South Korea 

s2130507@s.tsukuba.ac.jp, juhan.nam@kaist.ac.kr, terasawa@slis.tsukuba.ac.jp 

## ABSTRACT 

In this paper, we focus on singing techniques within the scope of music information retrieval research. We investigate how singers use singing techniques using real-world recordings of famous solo singers in Japanese popular music songs (J-POP). First, we built a new dataset of singing techniques. The dataset consists of 168 commercial J-POP songs, and each song is annotated using various singing techniques with timestamps and vocal pitch contours. We also present descriptive statistics of singing techniques on the dataset to clarify what and how often singing techniques appear. We further explored the difficulty of the automatic detection of singing techniques using previously proposed machine learning techniques. In the detection, we also investigate the effectiveness of auxiliary information (i.e., pitch and distribution of label duration), not only providing the baseline. The best result achieves 40.4% at macro-average F-measure on nine-way multi-class detection. We provide the annotation of the dataset and its detail on the appendix website<sup>0</sup> . 

## 1. INTRODUCTION 

A singing voice is one of the most essential elements of music. It provides impactful emotional expressions through melody and lyrics. In particular, in popular music, the role of the singing voice is more important, as the vocal quality and unique style of singers are critical in attracting people. Vocals mainly consist of singer individuality (i.e., vocal fold vibration and vocal tract resonance) and singing expressions (i.e., fine control of pitch, timbre, and loudness). Singing techniques, as the name suggests, are extended techniques in human singing. It characterizes singing voices as a component of expressions in vocal performances. In particular, many professional singers in popular music use singing techniques to make a performance more expressive, each in a different manner. 

> 0 https://yamathcy.github.io/ISMIR2022J-POP/ 

The singing voice is an important subject in the field of music information retrieval (MIR), and there are many prior works that extract quantitative or objective information as in the task of singing transcription [1], lyric identification [2], and singer identification [2]. Computational analysis of singing techniques based on MIR can contribute to the clarification of singing styles and can be applied to music discovery, vocal training, consumergenerated media and so on. Singing techniques have been of keen interest, especially in J-POP, both among singers and music creators; the singing style of J-POP singers has a wide variety, and their singing techniques are diverse. In addition, singing techniques are one of the evaluation criteria in Japanese commercial karaoke systems with scoring systems. Meanwhile, as for music creators, VOCALO songs, whose singer’s voice are created by a singing voice synthesis software such as VOCALOID [3], have been established as a music genre in Japan. Many VOCALOID creators manually manipulate the voice of VOCALOID to make it more expressive, sometimes while referring to how the actual singer produce the singing voice, like how singing techniques are applied. Therefore, J-POP is an attractive research target for singing technique analysis and computational singing technique analysis may bring benefits to real-world applications. 

In this regard, we present a case study of singing technique analysis in J-POP. We first introduce a new dataset, including the annotation of singing techniques for J-POP recordings. We analyze the dataset using descriptive statistics to illustrate the technique distributions and singer styles. Finally, we conduct singing technique detection based on machine learning methods, which can be beneficial to analyze the one side of the singing voice automatically. We demonstrate the detection of various singing techniques (i.e., identifying the singing technique type with its starting time and duration) and report baseline results using existing methods. Finally, we investigate the effect of the identification model with auxiliary information derived from the statistics of the dataset and pitch information. 

## 2. RELATED WORKS 

> © . Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: , ªAnalysis and detection of singing techniques in repertoires of J-POP solo singersº, in Proc. of the 23rd Int. Society for Music Information Retrieval Conf., Bengaluru, India, 2022. 

## 2.1 Singing Technique Analysis 

Analyzing the acoustic patterns of singing expressions has been a long-standing research topic. Research on vibrato 

384 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

dates to the 1930s [4]. Later, computer-based methods allowed a more quantitative analysis of vibrato parameters [5,6]. In addition to vibrato, other singing techniques, such as growling [7], portamento [8], voice registers [9,10], and extreme vocal effects [11] have also been investigated. An analysis of singing techniques was also conducted for J- POP. Migita et al. investigated the vibrato parameters of the imitated singing voices of J-POP vocalists [12]. Yamamoto et al. conducted an exploratory analysis of singing techniques that imitate the singing style of J-POP singers [13]. They found 13 types of singing techniques from 48 tracks and analyzed them with annotations. Because singing techniques in J-POP cover wide repertoires [14], such exploratory analysis is also important for the purpose of singing performance analysis. As our interests are handling and detecting multiple singing techniques rather than specifying a single technique, we annotated the label as in the manner in [13] but on the original real-world tracks of J-POP. Therefore, our new dataset consists of labels for multiple singing techniques. 

## 2.2 Singing Technique Datasets 

There are a handful of datasets that focus on the analysis of singing techniques. The Phonation Mode dataset consisted of four vocal modes (neutral, pressed, breathy, and flow) of sustained sung vowels from four singers [15]. Although the dataset includes a wide range of pitches, they are discrete, and thus lack a melodic context. VocalSet [16] handles the issue by having voices sung in contexts of scales, arpeggios, long tones, and excerpts. In addition, it covers a broader range of singing techniques, such as vibrato, trill, vocal fry, and inhaled singing. Because audio samples in the two datasets were newly recorded, they were collected under controlled conditions. Therefore, their characteristics of singing techniques might be different from those appeared in songs. 

However, several datasets have been annotated for realworld vocal music. The KVT dataset was originally built for vocal-related music-tagging tasks in K-POP music [17]. It contains 70 vocal tags, of which six are related to the singing technique (whisper/quiet, vibrato, shouty, falsetto, speech-like, and non-breathy). The annotation was conducted using crowdsourcing. The MVD dataset was built to analyze screams in heavy metal music, and has four different types of screams (high fry, mid fry, low fry, and layered) [18]. The regions and types of screams in the audio files were manually annotated. Similar to these studies, we are interested in versatile singing techniques in real-world music and thus we chose commercial music to build the dataset. 

## 2.3 Singing/Playing Technique Identification on MIR research 

Studies have been conducted on the automatic identification of singing techniques beyond computational analysis. There are two scenarios for identifying a singing techniques. One is classifying sung vocal audio into singing 

techniques. Several studies have conducted singing technique classification on VocalSet [19] and phonation modes [20, 21]. These works identify singing techniques but do not provide time-related information, such as start time and duration. The other method is to detect the singing technique in time. Miryala et al. [22] identified the singing expressions of raga, classical music in India. They created 35 recordings in eight ragas sung by six singers and showed a classification accuracy of 84.7% using a rulebased classifier. Yang et al. [8] proposed AVA, an interface for analyzing vibrato and portamento based on the filter diagonalization method (FDM) and hidden Markov model (HMM), respectively. They also provided a case study of the analysis of vibrato and portamento in the Beijing opera. Ikemiya et al. [23] provided rule-based parameterization of four singing expressions (vibrato, kobushi, gliss-up, gliss-down), extracted them from recorded vocal tracks to transfer to other vocal tracks, and demonstrated them on two sung excerpts. Kalbag et al. [18] provided scream detection for heavy metal music. They also built the MVD dataset and demonstrated classification, including non-scream singing and non-vocal music. Since singing techniques appear locally on sung vocals, we adapted these temporal detection strategies for identification. 

## 3. DATASET 

In this section, we describe the organization of our new dataset used for the analysis of this study. Due to the limit of the space, more details are described in the appendix site<sup>0</sup> . 

## 3.1 Song Selection 

To cover a wide range of singing techniques, the dataset should include various types of vocalists, considering gender, genre, tempo, and mood. We first listed 42 solo singers (21 males and 21 females), and four famous hit songs were selected from each singer to be as different as possible. Each song was performed as solo performance in Japanese. We collected audio tracks from commercial CD recordings of the J-POP songs. We trimmed the collected audio tracks and annotated only the first consecutive section (i.e., verseA, verse-B and Chorus). Since we prioritized including various songs in our dataset rather than fully annotating multiple verses in a single song, we could collect a diverse set of singing styles. 

When using popular commercial songs for academic research, copyright is always an issue. The works by Kim [17] on K-POP and Kalbag [18] on heavy metal music are good examples of developing datasets using commercial music, which distributes only labels about the performed music but not the audio signals or score information. We followed their solutions and made our dataset that consists of singing technique and pitch (frequency) contour labels. 

385 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
Vibrato Trill Scooping Bend Drop Hiccup Melisma<br>10000<br>H<br>Time (s)<br>Vocal fry Rasp Falsetto Breathy Whisper<br>10000<br>H<br>11<br>0.6 1.2 1.8 2.4 3.6 4.2 4.8 5.4<br>Tongue trill Shout Time (s) Spoken<br>10000<br>0.5 1.5 2.5<br>Time (s)<br><!-- End of picture text -->

Figure 1. Singing techniques included in the dataset. (upper) Pitch techniques with a sketch of pitch contour. Gray is the target vocal note, the red line is the pitch contour and blue dotted lines are boundary of each technique. (middle) Timbral techniques. We also show the non-technique extracted from the same track. (lower) Miscellaneous techniques. 

Homura/LiSA Singing Techniques (Beginning of the song) ScoopingVibrato Vocal fryBendBreathy Sa Yo Na Ra, A Ri Ga To, Ko E No Ka Gi Ri 

Figure 2. An overview of annotation. (middle) an excerpt spectrogram with singing technique (colored area) and vocal melody (orange curve). 

## 3.2 Data Pre-processing 

The dataset contains two types of annotations: vocal melody and singing techniques. We illustrate the annotation result in Figure 2. All annotations were conducted on isolated vocal tracks after vocal separation using Demucs v3 [24], which is a state-of-the-art model for musical source separation. During the annotation process, we confirmed that there was no dropout of vocal regions by comparing the original mixed track. Instead, we observed that the separated vocals tends to retain the back-chorus or sometimes instrumental sounds that are similar to the singer’s voice (e.g., electric guitar, synthesizer). 

## 3.3 Singing Technique Annotation 

We thoroughly surveyed singing techniques based on instructional books [14,25] and other conventional scientific research related to singing techniques [7,13,16,17,26±29] and defined the labels for the major techniques that appear in these references. We manually annotated songs using these labels. 

Although many other singing techniques still exist, we 

> 1 A vocal style between singing and speaking. 

> 2 Although discarded in the analysis, we also annotate ‘unknown’ labels if the region seems to represent a singing technique but is difficult to classify them into any of the techniques above and found 24 unknown 

Table 1. The description of each singing technique ap- <mark>p</mark> eared in the dataset. 

|Technique|description|type|
|---|---|---|
|vibrato|aperiodic oscillation ofpitch.|pitch|
|scooping|an upper continuouspicth change|pitch|
|drop|a lower continuouspicth change|pitch|
|bend|a short tremolo or U/inverted-U<br>shapedpitch change|pitch|
|hiccup|a short hiccuping<br>on attack/release of note|pitch|
|melisma|a musical arrangement<br>in which several notes are<br>applied to one syllable of a lyric.|pitch|
|trill|a continuous pitch change<br>between two notes|pitch|
|falsetto|sungbyfalsetto register.|timbre|
|breathy|sungbybreathysound.|timbre|
|whisper|sunglike whispering.|timbre|
|rasp|sung by a creaky voice<br>with subharmonics.|timbre|
|vocal fry|sung by a creaky voice<br>andpulse registerphonation.|timbre|
|spoken|singing like rapping,sprechgesang <sup>1 </sup>,<br>and some other styles like speaking.|misc.|
|shout|shouting.|misc.|
|tongue trill|a rolling tongue,<br>occurred on[r]consonant.|misc.|



considered the following 15 singing techniques in this study. The pitch contour sketches of these techniques and spectrogram examples are illustrated in Figure 1. 

We note that these label names are not unique in the real-world (e.g., scooping is also called ‘portamento,’ ‘glissando,’ ‘gliss-up,’ ‘shakuri’ (in Japanese)). We made frame-level annotations on the audio tracks collected based 

> techniques in total. In the techniques, there are some sounds akin to coughing and pig squeals, for example. 

386 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
34563185<br>20 用<br>10 10{3 279 268 150 106<br>Counts [#] 102<br>1970 1980 1990 2000 2010 2020 10 26 15 日 日 日<br>Released year Counts(Logc-cle)<br>Figure 3. Distribution of song year of release. Scooing vibrato bend drop breathy hiccup vocal fry falsetto raspd melisma whisper shout spoken nge til<br>Techniques<br>10 1760.0827.9360.7 177.0<br>[#] sgos10 10^2 38.0 11.1 5 1.6<br>60 80 100 120 140 160 180 Total seconds(Log-scale) [s]<br>Song durations [s] vibrato scooping breathy falsetto bend doup rasp hiccup vocal fry melisma whisper spoken shout trill tongue tri l<br>Figure 4.. Distribution of song length in seconds. Techniques<br><!-- End of picture text -->

Figure 4.. Distribution of song length in seconds. 

on the vocabulary. Singing techniques were carefully annotated by an experienced vocalist (i.e., the first author of the paper) with the helps of sound playback and visualizing the spectrograms and pitchgrams. The annotation process is conducted on Sonic Visualizer [30]. 

## 3.4 Melody Annotation 

Since pitch is an essential component of singing technique analysis, we further annotated melodic pitch using Tony [31], followed by manual correction such as removing the unvoiced parts and reverberation tails. 

## 4. DESCRIPTIVE STATISTICS 

## 4.1 Song Statistics 

The distribution of songs selected for the dataset based on the year of release is shown in Figure 3. Songs can be collected from various eras, ranging from 1968 to 2021. The distribution of the songs in the dataset is shown in Figure 4. The overall length was 4h 47m 39s, and the average length of a song track was 1m 43s. The ratio of technique regions per song track was 22.8%. 

Figure 5. Statistics of the labels. upper: counts, lower: total duration. 



<!-- Start of picture text -->
ado 5 0 24 11<br>ai_ootsuka 70 92 14 15 2<br>aiko 64 82 37 31 4<br>aimyon 99 45 30 0 5<br>akira_fuse 132 43 10 6 5 10 2<br>ayauurea 58 73 48 22 18<br>ayaka 69 104 4 12<br>ayumi_hamasakichihiro_onitsukaayaka_hiraharachara 1088010 103743584 184 681 25 083 8 1627100 1010 18<br>judy_and_maryikimono_gakarihikaru_utadacreephypflumpoolgackt 9356 751569 111107927290 315318113 402382 13005 251010914<br>kazumasa_oda 19 49 35 4 0<br>ken_hirai 141 182 £9 14 24 18<br>kenshi_yonezu 69 75 29<br>koji_tamakikumi_koda 9574 39 14 10 8<br>larc_en_ciel 96 124 16<br>Singer ID lisa 150 110<br>masaharu_fukuyamamasayoshi_yamazakimiyuki_nakajima 1738160 55£677 21256 819 12139 0<br>momoe_yamaguchimr_children 8662 6068 10 29<br>naotaro_moriyamanoriyuki_makihara 141 55 90 83 918 25 2 0 182<br>official_hige_dandismsouthern_all_stars 7578 9789 £30 13 2233 40<br>spitz 53 117 31<br>sukima_switch 64 104 14 2 0 2 10 0<br>t_m_revolution 74 43 13 13 0<br>tsuyoshi_nagabuchiyo_hitoto 112 7211 69 60 83 24 41 51 64 0 60 12150 200 120<br>yumiouyayueiokna)yutaka_ozakiyoseobi 154 8159 121112 29 3511 29 13 250 15 1510 0 21 03 00<br>vibrato 6udoons eenq doup hiccup melisma breathy taleto w i sper rasd vocal fry spoken shout<br>Techniques<br><!-- End of picture text -->

## 4.2 Label Statistics 

We present the statistics for the annotated labels as a histogram at the upper side of Figure 5. The most frequent technique is ‘scooping’. It is followed by ‘vibrato’, ‘bend’, and ‘drop’. This indicates that such techniques are relatively common in J-POP. These techniques are also used in Japanese commercial karaoke systems for vocal assessment [32]. ‘scooping’, ‘bend’ and ‘drop’ are portamento, whose frequent use is sometimes considered undesirable in classical singing [25]. It can be said that this frequent use of portamento is a characteristic of J-POP. 

We show the distribution of techniques by each singer in Figure 6 and find that the occurrence frequency of the techniques is different for each singer. We also confirmed that scooping appears more than 29 times for every singer, whereas several singers tend to not use vibrato frequently (e.g., ‘creephyp’, ‘aimyon’, and ‘yoasobi’). 

The lower side of Figure 5 and Figure 7 shows the total duration and distribution of each technique using a boxen- 

Figure 6. Occurrence distribution of singing techniques by singer. The vertical black line divides each category. 

plot, respectively. Figure 7 shows that most of the techniques are relatively short (that is, the range between 0.1s and 1s.), especially for ‘drops’, ‘scooping’, ‘bend’, ‘hiccup’, and ‘vocal fry’. The average length of the singing techniques was 0.4s. 

## 5. SINGING TECHNIQUE DETECTION 

In this section, we describe the detection of the singing techniques. We conducted experiments on a multi-class detection scenario, which handles classification and localization simultaneously. The problem setting is the same as that in sound event detection (SED) [33]. Figure 8 illustrates the proposed method. We investigated the performance of the CRNN model in a singing technique detec- 

> 3 https://seaborn.pydata.org/generated/seaborn.boxenplot.html 

387 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
10<br>s<br>100十十+一+中二十<br>Length(Log-scale)<br>vibrato scooping punq doup hiccup melisma breathy falsetto whisper dsed vocal fry spoken tongue tri l shout<br>Techniques<br><!-- End of picture text -->

Figure 7. Distribution of each technique. Red and blue horizontal lines indicate 1 s and 0.1 s, respectively. 



<!-- Start of picture text -->
Input: Singing voice<br>(10s- 64 dimensional<br>mel spectrogram)<br>128 channel 3x3 Conv., BN, LReLU, 8x1 MP<br>128 channel 3x3 Conv., BN, LReLU, 4x1 MP<br>128 channel 3x3 Conv., BN, LReLU, 2x1 MP<br>32 units BiGRU Model: CRNN<br>32 units FC<br>Sigmoid<br>Threshold (> 0.5)<br>vibrato Output:<br>scoopingvocal fry presence timeline<br>falsetto of singing technique<br>→ Time<br><!-- End of picture text -->

short-time Fourier transform (STFT), we used a Hann window with 2048 samples to compute the discrete Fourier transform (DFT). The hop size was set to 10 ms in every experiment. 

We used a CRNN model, which is widely used as a baseline system for SED. We adapted the settings of the model of Imoto et al. [34], which treated a similar issue (i.e, label sparseness) of ours in SED. The model configuration is shown in Figure 8. The model consists of three convolutional layers, one layer of bidirectional GRU cells, and one fully connected (FC) layers. The input was the aforementioned log-mel-spectrogram, and the output was a multi-hot vector representation of the singing technique for each time frame. All experiments were conducted using a batch size of 16, and the model parameters were optimized using an Adam optimizer with a learning rate of 10<sup>−4</sup> . The model stopped training if the value of the loss function on the validation set did not improve over 10 epochs. 

The model was optimized using the binary crossentropy (BCE) loss. Performance was evaluated using segment-based recall (R), precision (P), macro-F-measure (Macro-F), and micro-F-measure (Micro-F) [35] using sed_eval. The macro-F-measure and micro-F-measure denote the class-wise and instance-wise average of the F- measure, respectively. We set the segment length to 50 ms. 

## 5.2 Model Improvement 

Figure 8. An overview of the singing technique detection. The configuration of the CRNN model is also shown. 

tion task. In addition to running the simple setting, we also investigated how the considerations of the characteristics of the dataset improve the performance (i.e., label sparseness and pitch information). Thus, through the experiment, we attempted to answer for the following three research questions: 1) To what extent can we detect singing techniques using machine learning? 2) Can modification of the loss function treat the problem of label sparseness? 3) Can auxiliary pitch information help improve the detection performance? 

## 5.1 Experimental Conditions 

We performed singer-wise seven-fold cross validation during the experiment. We first split the singers into seven groups. Then, in each run, one group is left out for test set, another one group is for validation set , and the rest are used for training set. Owing to the label imbalances of techniques between singer, we used the 9 most common classes (i.e., ‘bend,’ ‘breathy,’ ‘drop,’ ‘falsetto,’ ‘hiccup,’ ‘rasp,’ ‘scooping,’ ‘vibrato,’ and ‘vocal fry’), which appear on every fold. We divided the singer fold to balance the amount of each technique as much as possible. 

We segmented the vocal tracks, which are separated by Demucs v3 [24] in advance, into 10s audio clips and nonoverlapping parts at a sample rate of 44.1 kHz. Therefore, they were converted into 64-dimensional log-mel spectrograms. For experiments that involve the computation of 

## 5.2.1 Label-frame sparsity 

As mentioned in Section 4.2, most singing techniques have a short duration (i.e., shorter than 1 s). This can cause label imbalance between non-technique frames. To alleviate the problem, we investigated the effect of focal loss [36], which was originally proposed for image object detection. The focal loss can be represented as follows: 



<!-- Start of picture text -->
Lfl(pt) = −α(1 − pt) γ log(pt) (1)<br><!-- End of picture text -->

where α ∈ [0, 1] is a weighting factor for balancing the importance of positive and negative examples, and the term (1 − pt)<sup>γ</sup> is a modulating factor, with γ controlling the rate of dominant examples. We set α = 0.2 and γ = 2 for all conditions in the work that used focal loss. 

## 5.2.2 Pitch information 

We demonstrated that some of the techniques, such as vibrato and scooping, have a pattern of the shape to certain extent. Therefore, it is possible that explicitly feeding the pitch helps in the detection. We further investigated the effect of the auxiliary information. Under this condition, we considered two ways of obtaining pitch in our experiment. One is the ground-truth (GT) pitch annotation mentioned in Subsection 3.4. However, when used in realworld applications, it is difficult to obtain correct pitch annotation. Hence, we also used pitch estimation predicted by CREPE [37] on a separated vocal track. As CREPE can compute pitch confidence, we adopted the pitch value 

> 4 https://tut-arg.github.io/sed_eval/index.html 

388 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

Table 2. The results of sin <mark>g</mark> in <mark>g</mark> techni <mark>q</mark> ue detection. 

||Macro-F|Micro-F|P|R|
|---|---|---|---|---|
|BCE|37.7%|56.6%|40.2%|41.7%|
|Focal|39.6%|57.7%|40.3%|42.6%|
|BCE-GT|39.1%|57.1%|41.4%|42.8%|
|BCE-CREPE|39.1%|57.1%|40.2%|41.7%|
|Focal-GT|40.4%|58.3%|43.1%|42.2%|
|Focal-CREPE|40.3%|57.9%|42.7%|43.3%|



where the confidence value was higher than 0.5, whose overall accuracy was 78.0% evaluated by mir_eval [38]. We converted the pitch contour to a mel-band pitchgram that has the same frequency dimensions as the input melspectrogram, as in the work of singer identification [39]. Therefore, we stacked it on a mel-spectrogram along the channel axis. 

## 5.3 Experimental Results 

## 5.3.1 Baseline 

The first row of Table 2 shows the results of the CRNN model compiled by BCE: 37.7% for Macro-F and 56.6% for Micro-F. The fact that Macro-F is much lower than Micro-F indicates that the model failed to identify minority rather than majority classes. Actually, the class-wise F-measure, as shown in Figure 9, indicates that detection of the minority techniques (e.g., ‘rasp’ and ‘vocal fry’) is more difficult than the majority techniques (e.g., ‘vibrato’ and ‘scooping’). 



<!-- Start of picture text -->
BCEBCE-CREPEBCE-GTFocalFocal-CREPE Focal-GT<br>Cla s -wise F-measure (%)<br>vibrato scooping bend drop hiccup breathy falsetto rasp vocal fry<br>Techniques<br><!-- End of picture text -->

Figure 9. Class-wise F-measure 

dark-red bars in Figure 9). This indicates that the condition is robust to techniques that have a short duration or some relationships with pitch. 

## 5.3.3 Challenges 

The remaining challenges in the task are detected unnatural region lengths and singers’ identity. We confirmed that one of the common mis-detection cases is from the detection of too short or frequently switching regions. It might need to consider post-processing, such as temporal filtering or probabilistic model (e.g, hidden Marcov model, hidden semi-Marcov model, etc.). As for singer identity, it can affect the performance of the timbral techniques. We labeled timbral techniques when the sung voice transformed from the ordinary voice of the singer, and it caused the confusion. For example, the ‘rasp’ from a singer who has clean voice and ordinary voice from a singer who has raspy voice can be confusing. Therefore, there is still an issue of disentangling singers’ identity and singing techniques. 

## 5.3.2 Effect of focal loss and pitch information 

First, we show the results for the effect of focal loss in the middle part of Table 2. The detection performance improved by 1.9% in Macro-F. We further studied the classwise F-measure, as shown in Figure 9, and confirmed that the performance of short techniques, such as ‘bend’ (38.0% → 41.1%), ‘drop’ (35.7% → 39.3%), and ‘hiccup’ (35.1% → 41.2%) are especially improved. This indicates that focal loss can adapt to the sparsity of the label. 

Next, we showed the results of the effect of the auxiliary pitch information in the middle part of Table 2. A remarkable finding is that the F-measure of ‘falsetto’ was particularly improved (51.3% → 56.5%). We also confirmed that the recall value of ‘falsetto’ is raised more (64.7% → 74.1%) rather than the precision value (45.1% → 48.3%). This indicates that pitch information hint at the relationship between the sung pitch value and the occurrence of falsetto (i.e., falsetto can appear only at a higher pitch). We also confirmed that the input of CREPE pitch shows the similar tendency. 

We further investigated the effects of combining these two types of auxiliary information. As shown in the bottom part of Table 2, the combination of GT pitch and focal loss is the best condition in terms of both macro- and micro-F values. We can confirm that both effects of each auxiliary information occur under this condition (red and 

> 5 The other metrics were following; 85.9% for voice recall, 29.9% for voicing false alarms, 94.5% for raw pitch accuracy. 

## 6. CONCLUSION AND FUTURE WORK 

This work presented an analysis and identification of the singing technique in J-POP music as a case study. In addition, we built a new dataset consisting of 168 J-POP songs with annotation of pitch contour and singing techniques. The contributions of this study are summarized as follows: 1) we constructed a dataset with frame-level annotations of singing techniques on 168 famous J-POP vocal songs, 2) conducted a descriptive-statistical analysis of the dataset, 3) proposed a CRNN-based singing technique detection model as a baseline, and confirmed that both auxiliary pitch information and focal loss help the detection performance. 

As we showed the appearance of singing techniques relates to some other factors (e.g., difference of singing technique distribution by singer, pitch information helps the detection of falsetto, etc.), we are planning further investigations of relationships or joint identification between other musical factors (e.g. musical note, lyrics, beat and tempo, etc.) or higher level information (e.g. singer, songs’ emotion, mood, etc.) with making more types of annotation. Although this work focuses only on J-POP, the knowledge can be applicable to other types of singing. Similar study on other style of vocal such as K-POP, western pops or non-popular vocal and comparison between them are other interesting topics for future work. 

389 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

## 7. ACKNOWLEDGEMENTS 

This work was supported by JST SPRING, Grant Number JPMJSP2124. Dr. Maiko Murai (Associate Prof. at the University of Tsukuba) gave advices on copyright law. Yoshihide Ishikawa, Sayori Takayama and Karolina Shi helped the preparation of the metadata. We are grateful to above all. 

## 8. REFERENCES 

- [1] M. Ryynänen, Singing Transcription, A. Klapuri and M. Davy, Eds. Boston, MA: Springer US, 2006. [Online]. Available: https://doi.org/10.1007/ 0-387-32845-9_12 

- [2] E. J. Humphrey, S. Reddy, P. Seetharaman, A. Kumar, R. M. Bittner, A. Demetriou, S. Gulati, A. Jansson, T. Jehan, B. Lehner, A. Kruspe, and L. Yang, ªAn introduction to signal processing for singing-voice analysis: High notes in the effort to automate the understanding of vocals in music,º IEEE Signal Processing Magazine, vol. 36, no. 1, pp. 82±94, 2018. 

- [3] H. Kenmochi and H. Ohshita, ªVocaloid - commercial singing synthesizer based on sample concatenation,º in Interspeech, 2007. 

- [4] C. E. Seashore, ªA musical ornament, the vibrato,º Proc. of Psychology of Music, 1938, pp. 33±52, 1938. 

- [5] E. Prame, ªMeasurements of the vibrato rate of ten singers,º J. Acoust. Soc. Am., vol. 96, no. 4, pp. 1979± 1984, 1994. 

- [6] J. Sundberg, ªThe perception of singing,º in The psychology of music. Elsevier, 1999, pp. 171±214. 

- [7] K.-I. Sakakibara, L. Fuks, H. Imagawa, N. Tayama et al., ªGrowl voice in ethnic and pop styles,º in Proceedings of International Symposium on Musical Acoustics, 2004. 

- [8] L. Yang, S.-K. Rajab, and E. Chew, ªAva: an interactive system for visual and quantitative analyses of vibrato and portamento performance styles,º in In Proceedings of the 17th International Society for Music Information Retrieval Conference (ISMIR), 2016. 

- [9] K. Hirayama and K. Ito, ªDiscriminant analysis of the utterance state while singing,º in Proceedings of IEEE Symposium on Signal Processing and Information Technology (ISSPIT), 2012. 

- [10] Y. Lee, M. Oya, T. Kaburagi, S. Hidaka, and T. Nakagawa, ªDifferences among mixed, chest, and falsetto registers: A multiparametric study,º Journal of Voice (In Press, Corrected Proof), 2021. 

- [11] O. Nieto, ªVoice transformations for extreme vocal effects,º Master thesis, Pompeu Fabra University, 2008. 

- [12] N. Migita, M. Morise, and T. Nishiura, ªA study of vibrato features to control singing voices,º Proceedings of International Congress on Acoustics, pp. 23± 27, 2010. 

- [13] Y. Yamamoto, T. Nakano, M. Goto, H. Terasawa, and Y. Hiraga, ªAnalysis of frequency, acoustic characteristics, and occurrence location of singing techniques using imitated j-pop singing voice,º The Special Interest Group Technical Report of IPSJ (MUS), no. 20, pp. 1±8, 2021, (in Japanese). 

- [14] AKIRA/Utana, The Secret Singing Technique Used by Professional Singers 17 - The karaoke score improved from a 68 to a 92!-. Tsuta-shobou, 2013, (in Japanese). 

- [15] P. Proutskova, C. Rhodes, T. Crawford, and G. Wiggins, ªBreathy, resonant, pressed±automatic detection of phonation mode from audio recordings of singing,º Journal of New Music Research, vol. 42, no. 2, pp. 171±186, 2013. 

- [16] J. Wilkins, P. Seetharaman, A. Wahl, and B. A. Pardo, ªVocalset: A singing voice dataset,º in In Proceedings of the 15th International Society for Music Information Retrieval Conference (ISMIR), 2018, pp. 468±474. 

- [17] K. L. Kim, J. Lee, S. Kum, C. L. Park, and J. Nam, ªSemantic tagging of singing voices in popular music recordings,º IEEE/ACM TASLP, vol. 28, pp. 1656± 1668, 2020. 

- [18] V. Kalbag and A. Lerch, ªScream detection in heavy metal music,º in Proceedings of Sound and Music Computing (SMC), 2022. 

- [19] Y. Yamamoto, J. Nam, H. Terasawa, and Y. Hiraga, ªInvestigating time-frequency representations for audio feature extraction in singing technique classification,º in Proceedings of Asia-Pacific Signal and Information Processing Association Annual Summit and Conference (APSIPA ASC), 2021. 

- [20] J.-L. Rouas and L. Ioannidis, ªAutomatic classification of phonation modes in singing voice: towards singing style characterisation and application to ethnomusicological recordings,º in Interspeech, 2016. 

- [21] D. Stoller, S. Dixon et al., ªAnalysis and classification of phonation modes in singing,º in The 17th International Society for Music Information Retrieval Conference (ISMIR), 2016. 

- [22] S. S. Miryala, K. Bali, R. Bhagwan, and M. Choudhury, ªAutomatically identifying vocal expressions for music transcription.º in In Proceedings of the 14th International Society for Music Information Retrieval Conference (ISMIR), 2013. 

- [23] Y. Ikemiya, K. Yoshii, and K. Itoyama, ªTransferring vocal expressions of a professional singer to unaccompanied singing signals,º in ISMIR-LBD 2014, 2014. 

390 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

- [24] A. Défossez, ªHybrid spectrogram and waveform source separation,º in In Proceedings of the 22nd International Society for Music Information Retrieval Conference (ISMIR), 2021. 

- [25] F. Husler and Y. Rodd-Marling, Singing: The physical nature of the vocal organ: A guide to the unlocking of the singing voice. Random House (UK), 1976. 

- [26] Y. Ikemiya, K. Itoyama, and H. G. Okuno, ªTransferring vocal expression of f0 contour using singing voice synthesizer,º in Proceedings of International Conference on Industrial, Engineering & Other Applications of Applied Intelligent Systems. (IEA/AIE), 2014, pp. 250±259. 

- [27] M. Panteli, R. Bittner, J. P. Bello, and S. Dixon, ªTowards the characterization of singing styles in world music,º in Proceedings of the IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP), 2017, pp. 636±640. 

- [28] M. Nakazato, ªHow to sing ornamented melody in j- pop: Through the analysis of kobushi in ken hirai, keisuke kuwata, chemistry and dreams come true,º Japanese Journal of Music Education Practice, vol. 5, no. 1, pp. 32±39, 2007, (in Japanese). 

   - [36] T.-Y. Lin, P. Goyal, R. Girshick, K. He, and P. Dollár, ªFocal loss for dense object detection,º in Proceedings of the IEEE international conference on computer vision (ICCV), 2017, pp. 2980±2988. 

   - [37] J. W. Kim, J. Salamon, P. Li, and J. P. Bello, ªCrepe: A convolutional representation for pitch estimation,º in Proceedings of the IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP), 2018, pp. 161±165. 

   - [38] C. Raffel, B. McFee, E. J. Humphrey, J. Salamon, O. Nieto, D. Liang, D. P. Ellis, and C. C. Raffel, ªmir_eval: A transparent implementation of common mir metrics,º in In Proceedings of the 15th International Society for Music Information Retrieval Conference (ISMIR), 2014. 

   - [39] T.-H. Hsieh, K.-H. Cheng, Z.-C. Fan, Y.-C. Yang, and Y.-H. Yang, ªAddressing the confounds of accompaniments in singer identification,º in Proceedings of the IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP). IEEE, 2020, pp. 1±5. 

- [29] M. Jones, ªThe rhythm and blues (r&b) protest songs of the civil rights movement: Outlining the natural alignment between the foundational r&b recordings artists and the african-american church during the movement,º Master Theses, Liberty University, 2016. 

- [30] C. Cannam, C. Landone, and M. Sandler, ªSonic visualiser: An open source application for viewing, analysing, and annotating music audio files,º in Proc. ACMMM 2010, 2010, pp. 1467±1468. 

- [31] M. Mauch, C. Cannam, R. Bittner, J. Bello et al., ªComputer-aided melody note transcription using the tony software: Accuracy and eciency,º in Proceedings of the First International Conference on Technologies for Music Notation and Representation (TENOR 2015), 2015. 

- [32] D. C. LTD., ªKaraoke systems,º Japan Patent 2020166142, 2020, (in Japanese). 

- [33] A. Mesaros, T. Heittola, T. Virtanen, and M. D. Plumbley, ªSound event detection: A tutorial,º IEEE Signal Processing Magazine, vol. 38, no. 5, pp. 67±83, 2021. 

- [34] K. Imoto, S. Mishima, Y. Arai, and R. Kondo, ªImpact of sound duration and inactive frames on sound event detection performance,º in Proceedings of the IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP). IEEE, 2021, pp. 860±864. 

- [35] A. Mesaros, T. Heittola, and T. Virtanen, ªMetrics for polyphonic sound event detection,º Applied Sciences, vol. 6, no. 6, p. 162, 2016. 

391 

