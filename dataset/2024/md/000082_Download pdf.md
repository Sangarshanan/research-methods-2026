---
paper_id: "000082"
year: 2024
title: "Download pdf"
source_url: "https://zenodo.org/record/14877441/files/000082.pdf"
---

# COMPUTATIONAL ANALYSIS OF YAREDAWI YEZEMA SILT IN ETHIOPIAN ORTHODOX TEWAHEDO CHURCH CHANTS 

Mequanent Argaw Muluneh<sup>1,2</sup> Yan-Tsung Peng<sup>2</sup> Li Su<sup>1</sup> 1 Institute of Information Science, Academia Sinica, Taipei, Taiwan 

2 Department of Computer Science, National Chengchi University, Taipei, Taiwan 

```
mequanenta@gmail.com,ytpeng@cs.nccu.edu.tw,lisu@iis.sinica.edu.tw
```

## ABSTRACT 

Despite its musicological, cultural, and religious significance, the Ethiopian Orthodox Tewahedo Church (EOTC) chant is relatively underrepresented in music research. Historical records, including manuscripts, research papers, and oral traditions, confirm Saint Yared’s establishment of three canonical EOTC chanting modes during the 6th century. This paper attempts to investigate the EOTC chants using music information retrieval (MIR) techniques. Among the research questions regarding the analysis and understanding of EOTC chants, Yaredawi YeZema Silt, namely the mode of chanting adhering to Saint Yared’s standards, is of primary importance. Therefore, we consider the task of Yaredawi YeZema Silt classification in EOTC chants by introducing a new dataset and showcasing a series of classification experiments for this task. Results show that using the distribution of stabilized pitch contours as the feature representation on a simple neural-network-based classifier becomes an effective solution. The musicological implications and insights of such results are further discussed through a comparative study with the previous ethnomusicology literature on EOTC chants. By making this dataset publicly accessible, our aim is to promote future exploration and analysis of EOTC chants and highlight potential directions for further research, thereby fostering a deeper understanding and preservation of this unique spiritual and cultural heritage. 

## 1. INTRODUCTION 

The Ethiopian Orthodox Tewahedo Church (EOTC) chants hold immense cultural and religious significance in Ethiopia, yet they are largely overlooked [1].<sup>1</sup> The EOTC chant is believed to have originated with Saint Yared (505– 571), who composed the three EOTC chanting modes 

> 1 The Eritrean Orthodox Tewahedo Church, which separated from the EOTC administration system a few decades ago, also utilizes these chants. We acknowledge its important role in preserving this sacred form of church music. 

(YeZema Siltoch in Amharic language),<sup>2</sup> namely Ge’ez,<sup>3</sup> Ezil and Araray. Saint Yared’s pioneering musical compositions, liturgical chants, and associated dance movements had a significant impact on Ethiopian sacred music tradition [2]. The Debterawoch (also called Merigetawoch), who are the expert musicians and heirs of Saint Yared, play a crucial role in the transmission and performance of the sacred music [1]. Ethiopian sacred music has been preserved through oral and written traditions, with written documents supporting and reinforcing the ongoing oral traditions [3]. The significance of the EOTC chants in Ethiopian culture and worldwide is evident through the two major spiritual mass celebrations that have been recognized by UNESCO as intangible cultural heritages: the Commemoration Feast of the Finding of the True Holy Cross of Christ (in 2013) and the Ethiopian Epiphany (in 2019).<sup>4</sup> These two celebrations, primarily accompanied by the EOTC chants, are among the five intangible cultural heritages from Ethiopia registered by UNESCO. 

Despite its long history and development, the research of EOTC chants was quite rare. Among them, a renowned ethnomusicological work from Western academia was by Shelemay et al. [3, 4], based on the analysis of a series of EOTC chants collected in Addis Ababa, 1975. They discussed the oral and written tradition of EOTC chants, the EOTC chant music notation system, and further the definition of the three chanting modes, specifically the pitch sets used in each of the modes. It should be noted that in this work, all the recordings were transcribed and analyzed by ear. As stated in the paper, the analysis, for a limited number of recordings, was sometimes challenging when transcribing the non-Western music scales. With no indigenous classification of their pitch materials [3], YeZema Siltoch remains a primary research topic in the music theory of EOTC chants. 

This paper is a study on YeZema Siltoch of the EOTC chants from computational perspectives. Our contributions in this paper are three-fold. First, we propose a new dataset for YeZema Silt classification and analysis. Second, we 

© M. A. Muluneh, Y. T. Peng, and L. Su. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: M. A. Muluneh, Y. T. Peng, and L. Su, “Computational Analysis of Yaredawi YeZema Silt in Ethiopian Orthodox Tewahedo Church Chants”, in Proc. of the 25th Int. Society for Music Information Retrieval Conf., San Francisco, United States, 2024. 

> 2 Siltoch is the plural form of silt. For simplicity, the Amharic phrase YeZema Silt and the English phrase chanting mode will be used interchangeably throughout this paper. 

> 3 The term Ge’ez holds various connotations depending on context; here, it denotes one of the three chanting styles. Conversely, it also refers to the language and may have other applications. 

> 4 `https://ich.unesco.org/en/state/ethiopia-ET? info=elements-on-the-lists` 

729 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

benchmark the YeZema Silt classification on the dataset using neural network classifiers with a number of features, primarily the pitch contour features which have been verified useful in analyzing various kinds of music [5–11]. Third, we perform a comparative study with [3,4] to echo, and to revise their statements as well: while the pitch sets used in Ezil and Araray was regarded as the same [3], our numerical results indicate notable difference in between them. In the rest of this paper, we will have a background introduction of EOTC chants in Section 2. The proposed dataset, benchmarks and the comparative study will be in Sections 3, 4, and 5, respectively. Conclusion and future works will be given in Section 6. 

## 2. BACKGROUND OF EOTC CHANTS 

## 2.1 Features and Performance Traditions 

The spiritual schools of the EOTC have several departments, locally known as Guba’e bet. These departments include Nibab-bet (reading practice), Zema-bet (introductory to advanced level offices chanting), Qidase-bet (or Kidase-bet, liturgical chants), Qine-bet<sup>5</sup> (or Kine-bet, poetry), Aquaquam-bet (or Akuakuam-bet, advanced chanting with accompaniments), and YeMetsahift Tirguame-bet (exegesis of scriptures). The knowledge and skills acquired from each Guba’e bet are crucial for understanding the chants. Each Guba’e bet, which focused on chanting, has two or more slightly different vocal and performance styles [12]. For example, Zema-bet has Bethlehem, Achabir, Qoma, and Tegulet, and Qidase-bet has Selelkula and Debre Abay. These nominations are based on the names of places where the center of excellence, that approves a senior student to be a teacher, is located. Such Guba’e bet, for example, Bethlehem has a slightly different vocal style, ornamentation, and notation complexity compared to Qoma, and it also has its own swaying and religious dancing tradition with its own drumbeat. 

The EOTC chants incorporate monophonic, antiphonal, and choral ritual performances. Our dataset is derived from Qidase-bet, which primarily focuses on monophonic and antiphonal ritual performance components without accompaniments. In contrast, Aquaquam-bet emphasizes religious dance and movements, primarily choral with some monophonic and antiphonal components. It is accompanied by prayer staffs known as mequamia, drums, and sistrums [12, 13]. The content of the chants - the text, whether poetic or unpoetic, is directly or indirectly based on the Holy Bible. The lyrics primarily employ Ge’ez ( ), an ancient Semitic language with a distinct script known as Fidäl. These chants play an essential role in the religious practices of nearly 43.5% of the country’s population, or over 32 million Orthodox Tewahedo Christians, according to the 2007 national census [14].<sup>6</sup> 

The social groups involved in the chants include priests, deacons, and laypeople who attend the service hours. Tra- 

> 5 -ne’ is pronounced as in ‘Nelson’ 

> 6 The Ethiopian and Eritrean faithful worldwide served by the chants is additional to the data reported in [14]. 

ditionally, the chants were transmitted orally, with singers memorizing a repertoire of phrases and melodies to perform during liturgical celebrations. Several decades ago, chant manuscripts were handwritten on parchment, which refers to processed goat or sheep skins. Even today, some scholars adhere to this practice to uphold the church’s cultural traditions. However, in recent decades, transmission has been supported by printed manuscripts for training along with oral traditions for actual performance. 

Despite its rich heritage, the tradition of EOTC chants faces significant challenges. Many training centers are closing down due to absence of government support, insufficient community support for students [12], and the dominance of modern education since the 20th century. Despite the contributions of printing and recording advancements, the computational contribution to the Ge’ez language and the chants remains underdeveloped. Except for a few works on MIR [13] and music generation [15], computational research on the EOTC chants is not as developed as it is for some other secular music. These issues highlight the need for more research on the EOTC chants. Our research aims to contribute to MIR-related tasks on the EOTC chants, addressing this gap. 

## 2.2 YeZema Siltoch - Chanting Modes 

The EOTC chants encompass three primary YeZema Siltoch (modes): Ge’ez, Ezil, and Araray. They are typically employed sequentially or intermixed, sometimes aligning with the church calendar’s seasons. Notably, during fasting periods, the Ge’ez and Araray modes predominate, while the Ezil mode mostly reserved for holidays. These modes serve as conduits for conveying distinct emotions and seasonal themes within the EOTC chants [1]. 

- Ge’ez: Characterized by a foundational, low tone, Ge’ez chanting evokes a sense of despondency and solemnity. Rendered in a relaxed, subdued manner devoid of rhythmic constraints, it encapsulates feelings of despair, disappointment, and sorrow [1]. In [3], the Ge’ez mode is interpreted as a chain of third (a-c<sup>′</sup> -e<sup>′</sup> ) with “chromatic auxiliary notes around the outer fifth” (♯g/ ♭b around a, and ♯d<sup>′</sup> / f<sup>′</sup> around e<sup>′</sup> ). 

- Ezil: Positioned within a mid-range vocal register, the Ezil (or Izil) mode assumes a secondary role, characterized by its unassuming, moderate cadence. Emotionally neutral in essence, it is seldom utilized during fasting periods, maintaining a comfortable, ordinary vocal expression. Shelemay et al. [3] stated that “Ezil uses the same pitch set as in Araray,” but this pitch set is rendered as either c-d-e-g-a or c-df-g-a, implying that the third note lies in between e and f and causes ambiguity for Western ears. 

- Araray: Distinguished by its high-pitched rendition, embellished with ornamental flourishes and a brisk tempo, the Araray mode exudes vitality and jubilation. It serves as a vehicle for conveying animated expressions, elation, and manifestations of compassion, happiness and fulfillment. 

730 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 



<!-- Start of picture text -->
ē<br>so-neh xna wǎen. à<br> 0 :<br>C . Na<br>3：<br>P05 201-0205 00<br>ATD<br>:<br><!-- End of picture text -->

Figure 1. Interlinear letter-based notations with interspersed neumes. From the first underlined two words, the letters enclosed in red rectangles are used as short-form representations of the melody to be used over the other underlined words, sung with the same melody. 

The EOTC chants rely on a sophisticated system of interlinear notations, encompassing neumatic signs interspersed between letter-based representations [1, 3]. This notation system serves as the cornerstone of melodic expression in chanting. Although some notations are common across different chanting modes, they produce distinct melodies depending on the mode, making it challenging to identify a specific mode solely based on notation. Figure 1 provides an example of the notation system used in the EOTC chants. 

## 3. DATASET 

The dataset was manually collected from the Eat the Book website,<sup>7</sup> a hub of numerous audio books for most of the teachings in the EOTC school departments, with full and partial coverage. From the available audio books, we selected the Se’atat Zema (Horologium chant), which is part of Qidase-bet department. All the audios selected for our dataset were recorded by a single scholar at a sampling rate of 44,100 Hz and in stereo channel. 

Our first step in the audio arrangement process involved narrowing the gap between the longest and shortest duration among the audios. Long audios, such as those over 13 minutes, were segmented into shorter audios of less than three minutes (180 seconds) in a way that preserves meaningful segments. This segmentation process also applied to audios that contained multiple chanting modes. For example, if an audio had 160 seconds of Araray mode followed 

> 7 `https://eathebook.org/` , We acknowledge the website’s administrators for their invaluable contribution. 

|||Duration Distribution||
|---|---|---|---|
|40||||
|Freuenc (number o**f**iles)<sup>35 30 25 20 15 10</sup>||||
|qy  <br>5||||
|0 2|0<br>40|60<br>80<br>100 120 140 <br>Duration (seconds)|160 180|
|gure 2.|Distrib<br>Shele|ution of audio recording len<br>mayand Jeffery [4]<br>T|gth (in secs<br>his work|
|Modes|#|Length<br>#|Length|
|Araray|8|11m36s<br>118|192m36s|
|Ezil|6|9m56s<br>176|291m29s|
|Ge’ez|10|21m12s<br>75|118m6s|
|Total|24|42m44s<br>369|602m11s|



Figure 2. Distribution of audio recording length (in secs). 

Table 1. Data distribution among the chanting modes. 

by 22 seconds of Ezil mode content, it would be segmented into two separate audios of 160 seconds and 22 seconds. Recordings that were less than three minutes but still had multiple modes were also segmented based on the respective duration of the included chanting modes. 

On the other hand, short audios, like a 19-second audio, were merged with neighboring context audios when applicable to our assumptions. If no neighboring audio with the same mode was found, it would be counted as a separate audio. As we arranged all audios to be in a single mode, we have a corresponding mode label for each audio. Another audio cleaning process was removing non-chant segments as the recordings included short explanatory statements about the corresponding chants. We manually removed them to ensure that the full audio content will be for chanting. In this process we also have shortened the duration of significant silent regions, resulted in only two silent regions above two seconds, particularly 2.25 and 2.14 seconds. After such cleaning procedures, the overall duration distribution of our dataset, ranging from 20.142 seconds to 177.476 seconds, is shown in Figure 2. As our immediate future work, we are working on expanding our dataset by including annotation of word-level lyrics to audio alignment as well as other features, which are not uncovered in this paper to keep the focus. We will do more research regarding other possible additional features. 

Table 1 presents the comparison between the previously used dataset (i.e., the recordings collected by Shelemay et al. in [4]) and our dataset. While the previous dataset, with a total of 24 instances, is less than one hour, our dataset accounts for more than 10 hours, with a total of 369 instances. The chanting mode annotations of the dataset are available on `https://github.com/mequanent/ ChantingModeClassification.git` . 

731 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

## 4. YAREDAWI YEZEMA SILT CLASSIFICATION 

As a preliminary study, we only consider using timeaveraged audio features (i.e., the features ignoring the information lying in the temporal dimension) for Yaredawi YeZema Silt classification. Focusing on such features also supports our subsequent discussion on the pitch distributions of different chanting modes (see Section 5). 

## 4.1 Feature Representations and Classifiers 

Following previous works on the analysis of various kinds of music [5–11], we consider pitch distribution, the distribution of the frame-level pitch values, for the classification task. Our pipeline of feature extraction mostly resembles [10,16], by having the stages of pitch contour extraction, stable region extraction, and pitch drift calibration. First, the pitch detection algorithm pYIN [17] is utilized for pitch contour extraction. It sets the time resolution to 128 samples (5.8 ms) while the frequency resolution to 10 cents. After having the pitch contour, the pitch distribution is obtained by having a histogram over the frame-level pitch values with a frequency resolution of also 10 cents. To analyze the time-averaged aspects of the chanting modes, extracting the stable regions of the pitch contour while discarding the sliding, ornamental or other unstable components might be helpful. We therefore reimplement two stable region extraction methods, namely the morphetic method and the masking method, both proposed in [5]. There is also observable pitch drift during the performance. With an investigation of the data, we found that the pitch drifting along the whole recording is relatively small (around 1 semitone upward for the whole recording), so the pitch calibration process can be done straightforwardly with a linear regression. More specifically, the regression is performed on the pitch values 1 semitones around the global maximum of the pitch histogram. With the regression line with slope s, the pitch contour f [t] indexed by time t is calibrated to fcalibrated[t] by having fcalibrated[t] := f [t] − st. 

The pitch distribution features are therefore based on the six types of pitch contours: three stabilization modes (no stabilization, stabilization with morphetic method, and stabilization with masking method) times two calibration modes (with and without calibration). Besides, several audio features are also compared: time-average melspectrogram, mel frequency cepstral coefficient (MFCC), and chromagram. The melspectrogram and MFCC are extracted using the `torchaudio` package [18], while the chromagram is extracted with the `librosa` package [19]. The time-average features of them are obtained simply by taking average over the time axis. 

For the classifiers, we utilize the M5 (0.5M) model architecture proposed in [20]. The model is a fully convolutional network containing only 1-D convolution layers, max pooling layers and a global average pooling layer. Such a design has small number of training parameters and can capture the invariance in data [21]. While this network was taken for raw waveform, we adapt it to operate in the frequency domain regarding it as an operator invariant to 

pitch shifting. To customize the model to our extracted features, we changed the receptive fields in the first convolutional layer from 80 to 3 when running on the non-rawaudio features in our experiments. For all the experiments, we adopt the categorical cross entropy loss function, Adam optimizer, learning rate of 0.001, batch size of 32, and 50 epochs, due to model convergence. 

## 4.2 Experiment Settings 

To observe how the characteristics of YeZema Silt vary across different recordings, we consider both the withindataset and cross-dataset experiments. For the withindataset experiment, we perform 5-fold cross validation (CV) on the proposed dataset and report the average classification accuracy. For the cross-dataset case, the model is trained on the proposed dataset and then tested on the recordings performed by a chanter from a different chanting department, specifically Zema-bet, in different time and location [4]. The recordings we used from [4], described in Table 1, have a sampling rate of 44100 Hz with stereo channel with 0.33 and 4.05 seconds of shortest and longest audio recordings, respectively. Lastly, to examine the reasonable identifiable audio duration among the chanting modes and how the duration affects the performance, we consider four input durations, namely 5 seconds, 10 seconds, 20 seconds and full length. 

## 4.3 Results 

Table 2 lists the classification accuracy of all the experiment settings. First, the results of full length audio show that all the pitch distribution greatly outperform other audio features by a gap of over 25 percentage points. Also, the pitch distribution is more robust than the other audio features in the cross-dataset scenario, with a performance drop by 7 to 23 percentage points. However, comparing the six pitch distributions, it is not clear which calibration or stabilization mode is better. The best accuracy over all in the CV scenario is the calibrated but non-stabilized pitch distribution, but the trend does not apply to the crossdataset case. Besides, we observe that 1) pitch contour stabilization does help on the accuracy for most of the cases, 2) using stabilization tends to reduce the performance gap between within-dataset and cross-dataset scenarios, and 3) the masking method can reduce this gap better than the morphetic method does, though the morphetic method typically has better classification accuracy. Lastly, there is a clear trend that a longer input audio leads to a better performance. This implies that YeZema Silt is a long-term, song-level music concept, while it can also be signified to some extend upon a 10- to 20-sec duration, which is around the duration of a set of music notation. 

Table 3 shows two example confusion matrices for both the within-dataset and cross-dataset cases. For the withindataset case, the accuracy of each class basically follows the amount of data (Ezil > Araray > Ge’ez, see Table 1). The trend is different for the cross-dataset case: all classification errors occur between Ezil and Araray, a result being in line with the experience of analysis [3]. 

732 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

|Feat|ure representat|ion|With|in-datase|t(5-fold|CV)||Cross-|dataset||
|---|---|---|---|---|---|---|---|---|---|---|
||Calibration|Stabilization|full|20 sec|10 sec|5 sec|full|20 sec|10 sec|5 sec|
|||No|96.20|91.51|87.93|81.60|87.50|82.98|72.96|74.76|
||No|Morphetic|95.13|87.23|83.47|73.35|83.33|84.40|76.67|70.97|
|Pitch contour||Masking|94.85|83.85|76.85|64.32|87.50|74.47|68.52|55.41|
|||No|98.11|89.92|88.02|80.78|75.00|80.85|77.04|69.64|
||Yes|Morphetic|95.66|87.71|80.39|70.58|79.17|73.05|70.00|69.07|
|||Masking|92.94|84.05|76.32|63.22|83.33|78.01|79.63|62.43|
|Time-a|verage chrom|agram|68.01|66.63|62.28|55.93|62.50|50.43|42.68|45.33|
|Time-ave|rage mel-spec|trogram|64.20|59.20|55.16|54.61|37.50|48.72|50.41|47.91|
|Tim|e-average MF|CC|68.52|66.62|66.16|65.42|37.50|35.90|36.18|39.17|



Table 2. Results (classification accuracy, in %) of Yaredawi YeZema Silt classification. 

||5-f|old CV|||Cros|s-datase|t|
|---|---|---|---|---|---|---|---|
||G|E|A||G|E|A|
|G|92.0|2.67|5.33|G|100.0|0.0|0.0|
|E|1.14|97.73|1.14|E|0.0|83.33|16.67|
|A|2.54|2.54|94.92|A|0.0|25.0|75.0|



Table 3. Confusion matrices over the Ge’ez (G), Ezil (E) and Araray (A) classes. The reported classifier is trained on calibrated pitch contour with masking stabilization. 

## 5. ANALYSIS OF YAREDAWI YEZEMA SILT 

The goal of our analysis of YeZema Silt is using computational tools to individually identify the pitches utilized in the three chanting modes. Any attempt to this relies on some music theoretical assumptions. The classification results presented in Section 4.3 supports two assumptions that facilitate the analysis: first, YeZema Silt is a song-level property that can be satisfactorily described with time-average pitch distributions; second, YeZema Silt can be identified by a classifier invariant to pitch-shifting (i.e. convolution). On the other hand, the classification results also expose a few technical limitations. While the raw pitch distribution (i.e., without pitch contour stabilization) yields the best classification accuracy, it is highly noisy and therefore less applicable for our analysis purpose. In fact, we found in our study that the raw and the morphetic pitch distribution are relatively deficient in the below-mentioned analysis process. Therefore, instead of advocating a specific setting in terms of classification accuracy, we decided to use the calibrated pitch contour with masking stabilization method on the full length audio for subsequent analysis, although its performance is not the most favorable. It is worth noting that in this case, the performance gap between within-dataset CV and cross-dataset is relatively small among all settings. 

Our approach, which partly resembles [10], contains three steps: 1) shift the pitch distributions of each recording such that each of them are best correlated (i.e., best aligned); 2) compute the average of the aligned pitch distribution for all the recording of the same chanting mode; 3) employ the Gaussian Mixture Model (GMM) to estimate the representative pitch set from the distribution. 

Specifically, the pitch distributions of two recordings pi 

and pj are aligned through pitch-shifting pj by ξij such that their cross-correlation Rij := Rij[ξ] is maximized: 



<!-- Start of picture text -->
ξij = −ξji := arg max Rij[ξ] . (1)<br>ξ<br><!-- End of picture text -->

The recording which has the highest average correlation with all the other recordings is considered as an anchor: the pitch distributions of all the other recordings are pitchshifted to this anchor according to their optimal ξ and are then averaged for GMM fitting. The mean (µ), variance (σ<sup>2</sup> ) and weight (w) of each GMM component then represents the pitch center, pitch variance and pitch weight. The GMM fitting process is initialized by user-specified mean values to enhance convergence [10]. To facilitate the discussion, only the components having variance smaller than 100 cents are considered as representative pitches. 

The top row of Fig. 3 illustrates the aligned pitch distributions for the three chanting modes and the two datasets. We observe that the recordings in the same chanting modes typically have similar pitch distributions over the two datasets. Such a consistent trend is also observed from the average pitch distributions (middle row of Fig. 3), which shows that only one pitch (the third peak from the left) from the two dataset in Araray is somehow different. 

The bottom row of Fig. 3 shows the GMM-estimated pitch distributions for all the recordings from both datasets. By selecting the pitches summing up to maximal weights within one octave, we obtain three representative pitches for Ge’ez (denoted as g1, g2 and g3, from low to high), five for Ezil (denoted as e1, e2, e3, e4 and e5) and also five for Araray (denoted as a1, a2, a3, a4 and a5).<sup>8</sup> Other representative pitches outside this octave are also notated: the pitch being one octave below g3 is denoted as G3, while the pitch one octave above g1 is denoted as g˙1. The same naming rules also apply for Ezil and Araray. 

Table 4 shows the GMM-estimated parameters for the three modes. First, the pitches used in the Ge’ez mode are more flexible than other two modes, as can be observed by their variances than the pitches in other two modes. Among them, only g2 has the variance less than 10 cents. 

> 8 Here, the subscript number does not imply the hierarchical order of the musical scale (e.g., g1 does not mean “the tonic of the Ge’ez mode”). The hierarchy of these pitches is another research question and will be considered as future work. 

733 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

|Ge'ez|lz3|Araray|Mode|Note name|µ|σ<sup>2</sup>|w|∆µ|
|---|---|---|---|---|---|---|---|---|
|An|||Ge’ez|G3<br>g1<br>g2<br>g3<br>˙g1|361<br>847<br>1171<br>1571<br>2047|11<br>21<br>7<br>14<br>18|0.034<br>0.211<br>0.171<br>0.419<br>0.112|486<br>324<br>400<br>476|
|||||E4|189|6|0.022|258|
|||||E5|447|14|0.023||
|||||e1|670|6|0.106|223<br>270|
|||||e2|940|7|0.151|234|
||||Ezil|e3|1174|7|0.123|232|
|||||e4|1406|3|0.416||
|||||e5|1674|15|0.068|268<br>204|
|||||˙e1|1878|5|0.059||
|||||˙e2|2139|5|0.013|261|
|||||A5<br>a1|173<br>520|3<br>6|0.008<br>0.318|347<br>172|
|||||a2|692|8|0.173|218|
|G3 g1 g2 g3 g1 E4 Ese<br>Relati|1 e2e3e4 ese1 è2 A<br>ve pitch (log frequen|5 a1a2a3 a4a5 à1<br>cy)|Araray|a3<br>a4<br>a5<br>˙a1|910<br>1207<br>1381<br>1716|10<br>5<br>4<br>5|0.176<br>0.134<br>0.027<br>0.084|297<br>174<br>335|



Figure 3. Illustration of pitch distributions for the three YeZema Siltoch. Top: the aligned pitch distributions of all the recordings. A row in the 2-D illustration represents the pitch distribution of one recording. Darker color represents larger values. Red background represents pitch distributions of the recordings in [4]. Middle: the average pitch distribution of the proposed dataset (green) and [4] (red). Bottom: GMM-estimated pitch distributions for all the recordings from both datasets. The pitch value of each note name under the bottom row is listed in Table 4. 

g3 and g2 form a major third (∆µ = 400 cents) while g1 and g2 form approximately a minor third g2 (∆µ = 324 cents). The pitches of g1 and g3 can vary by more or less semitones. Besides, we also observe that the octaves of g1 and g3 (i.e., G3 and g˙1) also have large variances. This implies that such variance (flexibility of pitch) depend on the pitch name rather than the register. These findings are basically in line with the statements (a scale ♯g-a-♭b-c<sup>′</sup> -♯d<sup>′</sup> - e<sup>′</sup> -f<sup>′</sup> while g-c<sup>′</sup> -e<sup>′</sup> are the stem pitches) made in [4]. 

Both the Ezil and Araray modes have five representative pitches within one octave. However, the five representative pitches of them are different. For Ezil, all the intervals lie between 200 cents (major second) and 300 cents (minor third), while for Araray, the intervals distribute from 172 cents (less than a major second) to 347 cents (in between a minor third and a major third). In other words, there is a consistent trend that the intervals in Ezil are more equally distributed than Araray. There are also some flexible usage of pitch, for example, e5 (E5) in Ezil. These suggest that the pitch sets found in [4] needs revision: from our observation, each of the pitch sets used in the three EOTC chanting modes is distinctive. Besides, a mode is characterized by not only its pitch centers, but also its pitch variances. 

Table 4. GMM-estimated mean (µ, in cents), variance (σ<sup>2</sup> , in cents), weight (w) of the representative note pitches in the Ge’ez, Ezil, and Araray modes. Reference pitch (0 cent) is 82.4 Hz. The intervals (difference between two neighboring pitches, ∆µ) are listed in the last column. 

## 6. CONCLUSION 

In this paper, we presented a research on a relatively underexplored music genre, the Ethiopian Orthodox Tewahedo Church (EOTC) chant, from three computational perspectives. First, through a rigorous data cleaning and annotation process, we presented a new and high-quality EOTC chant dataset, which can be extended for various music information retrieval (MIR) and music generation tasks. Second, we conducted a chanting mode (YeZema Silt) recognition task using our dataset and achieved promising results. Additionally, this paper is, to our knowledge, the first to computationally analyze the pitch sets of the EOTC chanting modes, specifically YeZema Siltoch, with new musicological insights. In the future, we plan to keep enriching the annotations of the datasets, by incorporating more details like lyrics, chanting options, reading tones and other potential features. Analyzing YeZema Siltoch using the features in the temporal dimension and the new data annotations are also our ongoing projects. 

The EOTC chants encompass a wide range of styles and forms. In this paper, we specifically concentrated on the Se’atat Zema (Horologium chant), which falls under the Qidase-bet department. Our objective is to encourage responsible research on EOTC chants, as computational research in this area can lead to technological advancements that enhance the learning process and increase accessibility. Diversifying the data and MIR of EOTC chants for the protection and promotion of this spiritual-cultural heritage is also our future work in the long term. 

734 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

## 7. ETHICS STATEMENT 

The chants we are working on belongs to the Ethiopian Orthodox Tewahedo Church (EOTC). The oral traditions and beliefs that mainly preserve these chants for more than 1500 years should be credited properly. This work aims to contribute on promoting the chants and finding solutions for their easy understanding. There is no intention to modify the chants in any form. 

No explicit permission request is done to the Eathebook.org administrators as recordings are open to the public education and we are using for educational purpose. We value their great effort in making the chants publicly available. 

## 8. REFERENCES 

- [1] A. Kebede, “The sacred chant of Ethiopian monotheistic churches: Music in black Jewish and Christian communities,” in The Black Perspective in Music, J. Southern, Ed. Brandeis University: JSTOR, 1980, pp. 20– 34. 

- [2] K. Shelemay, “The musician and transmission of religious tradition: The multiple roles of the Ethiopian Debtera,” Journal of Religion in Africa, pp. 242-260, vol. 22, 1992. 

- [3] K. K. Shelemay, P. Jeffery, and I. Monson, “Oral and written transmission in Ethiopian Christian chant,” Early Music History, vol. 12, pp. 55–117, 1993. 

- [4] K. K. Shelemay and P. Jeffery, Ethiopian Christian Liturgical Chant: An Anthology, Part 1 to Part 3. AR Editions, Inc., 1993, vol. 1. 

- [5] S. Rosenzweig, F. Scherbaum, and M. Müller, “Detecting stable regions in frequency trajectories for tonal analysis of traditional Georgian vocal music,” in International Society for Music Information Retrieval Conference (ISMIR), Delft, The Netherlands, 2019, pp. 352–359. 

- [6] D. Han, R. C. Repetto, and D. Jeong, “Finding tori: Self-supervised learning for analyzing korean folk song,” in International Society of Music Information Retrieval Conference (ISMIR), Milan, Italy, 2023, p. 440–447. 

- [7] B. Nikzat and R. Caro Repetto, “KDC: an open corpus for computational research of dastg¯ahi music,” in International Society of Music Information Retrieval Conference (ISMIR), Bengaluru, India, 2022, pp. 321–328. 

- [8] S. Nadkarni, S. Roychowdhury, P. Rao, and M. Clayton, “Exploring the correspondence of melodic contour with gesture in raga alap singing,” in International Society of Music Information Retrieval Conference (ISMIR), Milan, Italy, 2023, pp. 21–28. 

- [9] R. Caro Repetto and X. Serra, “Creating a corpus of jingju (beijing opera) music and possibilities for 

melodic analysis,” in International Society of Music Information Retrieval Conference (ISMIR), Taipei, Taiwan, 2014, pp. 313–318. 

- [10] F. Scherbaum, N. Mzhavanadze, S. Rosenzweig, and M. Müller, “Tuning systems of traditional georgian singing determined from a new corpus of field recordings,” Musicologist, vol. 6, no. 2, pp. 142–168, 2022. 

- [11] A. Vidwans, P. Verma, and P. Rao, “Classifying cultural music using melodic features,” in 2020 International Conference on Signal Processing and Communications (SPCOM), 2020, pp. 1–5. 

- [12] M. Tsegaye, “Traditional education of the ethiopian orthodox church and its potential for tourism development (1975-present),” Master’s Thesis, Addia Ababa University, Addis Ababa, Ethiopia, 2011. [Online]. Available: http://etd.aau.edu.et/handle/123456789/248 

- [13] B. T. Dagnew, “Ethiopian Orthodox Tewahido Church Aquaquam Zema classification model using deep learning,” Master’s Thesis, Bahir Dar University, Bahir Dar, Ethiopia, 2023. 

- [14] “Ethiopian Statistical Agency: Population and Housing Census. (2007). 2007 Census Results. retrieved from https://www.statsethiopia.gov.et/wpcontent/uploads/2019/06/population-and-housingcensus-2007-national_statistical.pdf,” Online, accessed: April 11, 2024. 

- [15] G. Zemedu and Y. Assabie, “Concatenative hymn synthesis from Yared notations,” in Advances in Natural Language Processing, A. Przepiórkowski and M. Ogrodniczuk, Eds. Cham: Springer International Publishing, 2014, pp. 400–411. 

- [16] S. Rosenzweig, F. Scherbaum, and M. Müller, “Computer-assisted analysis of field recordings: A case study of Georgian funeral songs,” ACM Journal on Computing and Cultural Heritage, vol. 16, no. 1, dec 2022. [Online]. Available: https://doi.org/10.1145/ 3551645 

- [17] M. Mauch and S. Dixon, “Pyin: A fundamental frequency estimator using probabilistic threshold distributions,” in 2014 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2014, pp. 659–663. 

- [18] J. Hwang, M. Hira, C. Chen, X. Zhang, Z. Ni, G. Sun, P. Ma, R. Huang, V. Pratap, Y. Zhang, A. Kumar, C.Y. Yu, C. Zhu, C. Liu, J. Kahn, M. Ravanelli, P. Sun, S. Watanabe, Y. Shi, Y. Tao, R. Scheibler, S. Cornell, S. Kim, and S. Petridis, “Torchaudio 2.1: Advancing speech recognition, self-supervised learning, and audio processing components for pytorch,” 2023. 

- [19] B. McFee, C. Raffel, D. Liang, D. P. Ellis, M. McVicar, E. Battenberg, and O. Nieto, “librosa: Audio and music signal analysis in python,” in In Proceedings of the 

735 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

14th python in science conference, vol. 8, 2015, pp. 18–25. 

- [20] W. Dai, C. Dai, S. Qu, J. Li, and S. Das, “Very deep convolutional neural networks for raw waveforms,” in IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2017, pp. 421–425. 

- [21] J. Thickstun, Z. Harchaoui, D. P. Foster, and S. M. Kakade, “Invariances and data augmentation for supervised music transcription,” in IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2018, pp. 2241–2245. 

736 

