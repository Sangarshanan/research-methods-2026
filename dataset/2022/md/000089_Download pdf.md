---
paper_id: "000089"
year: 2022
title: "Download pdf"
source_url: "https://zenodo.org/record/7316770/files/000089.pdf"
---

# EMOTION-DRIVEN HARMONISATION AND TEMPO ARRANGEMENT OF MELODIES USING TRANSFER LEARNING 

Takuya Takahashi Mathieu Barthet Centre for Digital Music, Queen Mary University of London 

takahashi@uec.ac.jp, m.barthet@qmul.ac.uk 

## ABSTRACT 

We propose and assess deep learning models for harmonic and tempo arrangement generation given melodies and emotional constraints. A dataset of 4000 symbolic scores and emotion labels was gathered by expanding the HTPD3 dataset with mood tags from last.fm and allmusic.com. We explore how bi-directional LSTM and Transformer encoder architectures can learn relationships between symbolic melodies, chord progressions, tempo, and expressed emotions, with and without a transfer learning strategy leveraging symbolic music data without emotion labels. Three emotion annotation summarisation methods based on the Arousal/Valence (AV) representation are compared: Emotion Average, Emotion Surface, and Emotion Category. 20 participants (average age: 30.2, 7 females and 13 males from Japan) rated how well generated accompaniments matched melodies (musical coherence) as well as perceived emotions for 75 arrangements corresponding to combinations of models and emotion summarisation methods. Musical coherence and match between target and perceived emotions were highest when melodies were encoded using a BLSTM model with transfer learning. The proposed method generates emotion-driven harmonic/tempo arrangements in a fast way, a keen advantage compared to state of the art. Applications of this work include AI-based composition assistant and live interactive music systems for entertainment such as video games. 

## 1. INTRODUCTION 

With the burgeoning of video games, user-generated video content, and tv/film productions released on streaming services, the demand of music for media seems to be growing. Although musicians have known for long how to produce music for such media, interactive music production systems can innovate the way producers create dynamic scores responding to contextual and user factors determined prior to or during the media experience. Deep generative models for music composition have made steady improvements but how to control them to support creative 

> © T. Takahashi, and M. Barthet. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: T. Takahashi, and M. Barthet, ªEmotion-driven harmonisation and tempo arrangement of melodies using transfer learningº, in Proc. of the 23rd Int. Society for Music Information Retrieval Conf., Bengaluru, India, 2022. 

agency remains a challenge [1]. In this work, we investigate deep learning techniques to generate musical arrangements controlled by emotional features. Music composition and arrangement are art crafts which involve specialized knowledge and experience. Prior work used artificial intelligence to either fully automate the music composition [2] and arrangement process [3] or develop assistive tools helping producers to compose new material through human-machine interaction [4]. Our work falls into the second category and focuses on generating harmonisation and tempo arrangements for composed melodies given emotional constraints. Deep learning (DL) was recently used to learn relationships between musical attributes (e.g. notes, chords) and associated emotions [5]. As discussed in [6], music emotions can be considered as being communicated by music (perceived emotions), and as being induced or evoked in listeners (felt emotions) [7]. Depending on the nature of the emotional annotations used during training (e.g. Tan et al. [8]), DL models can be aimed at producing music matching perceived or felt emotions. Music emotion recognition (MER) is one of the most challenging music information retrieval challenge, and new developments aim towards personalized and context-sensitive applications [9]. The proposed system generates harmonic and tempo arrangements for input melodies encoded in the symbolic domain so as to express specific emotions controlling the generation. Harmony and tempo were chosen for the inference stage as they have been shown to affect emotional expression: changes in chord progressions influence the emotions expressed by music [10]; tempo can greatly affect music emotions (especially in terms of arousal) [11]. A challenge in stirring DL generative models using emotion controls is the difficulty in finding training datasets containing both a large number of music examples and emotion labels [12]. We produced the HTPD3 Emotion Dataset (HED) released with this paper by collecting crowd-sourced emotion labels for the 4,000 tracks from the HTPD3 dataset [3]. Given the fairly small size of the dataset, we test the effectiveness of transfer learning for emotion-driven music generation using a network pre-trained only considering musical attributes. 

Applications include the design of assistant tools helping composers/producers to create different arrangements given input melodies and emotional intentions. This may be of help to musicians who do not have advanced musical knowledge and to find inspiration in musical ideas generated by the machine. Another use case is interactive 

741 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

music systems which adapts to the user context, defined in [9] as the dynamic aspects from the listener that fluctuate frequently (e.g. physiological signals). If training was conducted using felt emotion labels, the method could be used for generative music produced on the fly driven by a user’s felt emotions as predicted from e.g. biosignals. This could support affective gaming for example to produce responsive background music adapting itself to the emotional states of the game player, see e.g. [13]. 

## 2. RELATED WORK 

A review of affective algorithmic composition dealing with automatic composition of music based on specific emotions can be found in Sulun et al. [5]. Guo et al. [14] proposed a variational autoencoder (VAE) for music generation controlled by tonal tension predicted from low-level symbolic music features. Tan et al. [8] introduced Music FaderNets enabling to stir music generation based on arousal - an emotional dimension related to excitation - using Gaussian Mixture VAEs (GM-VAEs). Makris et al. [12] proposed a method for assigning valence - an emotional dimension linked to pleasantness - to chords based on prior relationships between mood tags and chord qualities. This enabled the generation of lead sheet data (melody and chord) conditioned by valence, phrasing and time signature using a sequence-to-sequence model. Results from subjective evaluations with 42 participants showed consistency between targeted and perceived valence. However, a limitation is that only valence was considered but not arousal. Sulun et al. [5] recently proposed a promising approach for the generation of multiinstrument symbolic music driven by musical emotion using a Music Transformer architecture. The models can be conditioned by continuous-valued valence and arousal labels and yield results representative of current state of the art on a large scale dataset of 34791 songs. However, possible limitations towards generalisation come from the use of machine-predicted valence labels retrieved from Spotify and the modeling of arousal using MIDI note density. 

## 3. DL ARCHITECTURE FOR AUTOMATIC ARRANGEMENT CONDITIONED BY EMOTIONS 

The proposed DL architecture is divided into a melody context encoder and an arrangement decoder (Figure 1). The melody context encoder aims to capture information from the input melody taken as a sequence. Based on the encoded melodic context embedding and emotional information, the arrangement decoder predicts chords, harmonic functions, and tempo. 

## 3.1 Melody Context Encoder 

The melody context encoder is shown in the top part of Figure 1 and takes a representation of melodies as input and outputs a 128-dimensional embedding (similar to [15]) at every time unit. To reduce the dimensionality of the input, the melody is converted to a pitch class profile (PCP), as in [15]. A PCP is a 12-dimensional vector, in which each 



<!-- Start of picture text -->
PCP PCP PCP PCP<br>Melody Context Encoder (BLSTM or Transformer Encode<br>Emotion Emotion Emotion Emotion<br>FC FC FC FC<br>LSTM LSTM LSTM LSTM<br>AAangement/Decoder<br>FC FC<br>FC FC FC<br>Tiads Crajor F major G major C majpor<br>Functions Tonic Subdominant Dominant Tonic<br>BPM 120 120 120 120<br><!-- End of picture text -->

Figure 1. Architecture of the proposed model. The top represents the melodic context encoding, the bottom represents the arrangement generation (LSTM: long short-term memory network; FC: fully connected layers). 

element of the vector contains the duration of each pitch class event. We compared the two following models for the melody context encoders (see Section 5): 

## Bi-directional LSTM (BLSTM) 

Inspired by the melody harmonizer proposed in [15], the same BLSTM model was used in this study with the aim of encoding the context of the melody. 

## Transformer encoder 

The Transformer [16] is a network originally proposed for machine translation. Its self-attention mechanism supports more complex contexts and more efficient computations than BLSTM. 

## 3.2 Arrangement Decoder 

As shown at the bottom of Figure 1, the arrangement decoder is constructed using LSTM units only with forward propagation. This is to reduce the amount of computation required, and also to be able to make inferences based only on historical information for near real-time applications. The LSTM unit of each melodic time unit receives as input the hidden state of the past unit, the embedding of the melody context, PCP of the melody, and emotion conditions represented numerically. Finally, for every time units, the arrangement decoder outputs the chord labels and chord functions as a classification problem and the tempo as a regression problem. The output layer of each component consists of a fully connected layer. The loss function is expressed as: 

L = CCE(c, c<sup>∗</sup> ) + 1.5CCE(f, f<sup>∗</sup> ) + 0.001MSE(t, t<sup>∗</sup> ) 



<!-- Start of picture text -->
(1)<br><!-- End of picture text -->

742 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

where c, f and t are chord labels, chord functions, and tempo, respectively. c<sup>∗</sup> , f<sup>∗</sup> and t<sup>∗</sup> are the related groundtruth attributes. CCE represents the categorical cross-entropy and MSE represents the mean-squared error. The weight of each error was heuristically determined by observing the reduction in loss during training. 

## 3.3 Training Strategies 

When a sufficient amount of emotion-labelled musical data is available for training, the model can be commonly trained with a backpropagation algorithm. However, when the amount of emotion-labeled data is not sufficient, transfer learning strategy enabling to include data without emotion labels can be effective. In such case, encoders are pre-trained using music examples without emotion labels, then the pre-trained encoders (weights are fixed) and randomly initialized decoders are concatenated and retrained only for the subset of tracks with emotion labels. However, groundtruth data may not provide the best examples since there are several possible arrangements following music theory and perception considerations [3]. As in [3], training was stopped to a fixed number of epochs (500) without using validation, when the loss was significantly reduced (learning rate = 1e-3) and subjectively consistent arrangements were generated with the test data. Results on the effectiveness of the transfer learning strategy are reported in Section 5.4. 

## 4. MUSIC EMOTION QUANTIFICATION 

In order to input emotional conditions to the networks, perceived or felt emotions associated to music have to be represented numerically. We investigated three ways to map emotions into Russell’s arousal-valence (AV) space [17]. 

to a same listener, or different emotions to different listeners. Therefore, similar to [21], two-dimensional Gaussian mixture models (GMMs) can be used to represent perceived/felt emotions associated to multiple mood tags associated to songs in the AV space. The average and standard deviation corresponding to the mood tags associated to a song are obtained from the experimental results in [19]. Based on the average and standard deviation, random sampling is performed and 10000 samples are generated for each tag. Like for EAR, the emotional features were normalized in the range 0-1. Clustering is performed using two-dimensional GMMs based on the randomly sampled points. Two Gaussian components were assumed sufficient to represent the emotional feature surface in the AV plane as in [21]. Finally, the average and standard deviation of each Gaussian component were used as the network input representation. We refer to this emotional representation as the emotion surface representation (ESR) in the remainder. 

## 4.3 Emotion Category Representation 

EAR and ESR are both continuous. However, music emotions may not be best represented by a dimensional model [22]. Studies on music emotion recognition, such as [23], used discrete representations of emotions through categorical variables. We also tested emotional representations with discrete categories. We distinguish four quadrants in the AV space; Q1: high arousal & high valence [joyful], Q2: low arousal & high valence [relaxing], Q3: low arousal & low valence [sad], Q4: high arousal & low valence [angry]). The AV space quadrant with the highest AV annotations determines the emotional category of the music. We refer to this emotional representation as emotion category representation (ECR) in the remainder. 

## 5. EXPERIMENTAL EVALUATION 

## 4.1 Emotion Average Representation 

In the Deezer Mood Detection Detaset [18], the emotional tags from last.fm<sup>1</sup> were mapped to arousal and valence values using [19]’s results. In [19], statistics on participant ratings for emotion words are reported for valence, arousal and dominance on a nine-point scale. In most cases, multiple emotion tags can be associated to music content. To address this, one of the methods used e.g. in [18,20], consists in summarising multiple emotions tags using the geometrical mean of the tag projections in the emotion space (e.g. AV space). We used such method yielding twodimensional emotional features from a set of mood tags for songs. These were normalized in the range 0-1 for network input. We refer to this emotional representation as emotion average representation (EAR) in the remainder. 

## 4.2 Emotion Surface Representation 

The EAR expresses emotions locally in the AV space. However, as investigated e.g. by [20], there is a possibility that a same song suggests/induces multiple emotions 

In this section, the proposed emotion-driven automatic music arrangement systems are evaluated for differences in network architectures and the effect of transfer learning. 

## 5.1 Dataset and training 

Network training requires a dataset in which melody, chords, tempo and emotions (perceived or felt) are simultaneously available. As in [3], we rely on the HTPD3 dataset which provides symbolic melodies, chords, and tempo. Time units were set to two beats (half bars in the 4/4 time signature). The chord played for the longest time over two beats was selected as the chord in that time unit. Notes that spanned a segmentation were split. However, tracks in HTPD3 are not labelled with emotion features. We retrieved crowd-sourced mood tags from last.fm<sup>1</sup> and allmusic.com<sup>2</sup> for the song and artists contained in HTPD3. Tags from last.fm<sup>1</sup> and allmusic.com<sup>2</sup> have previously been used in music emotion studies, see e.g. [18]. As some of the last.fm tags are not related to emotions, we filtered these out using the criteria proposed in [24]. This 

> 2 https://www.allmusic.com/ 

1 https://www.last.fm/ 

743 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

method allowed us to tag approximately 4000 tracks available in HTPD3. We refer to this expanded dataset as the HTPD3 Emotion Dataset (HED) available at the link below<sup>3</sup> . There is some uncertainty on whether crowdsourced mood tags relate to perceived or felt emotions. We assume here that these tags relate to perceived emotions, however this can limit the performance of the model in the experiments. Another caveat is that the mood tags relate to audio versions of songs, whereas our model deals with symbolic music. Hence, as in [5], they are considered as ªweak labels" for symbolic music. The dataset was divided into 90% training data and 10% test data. As suggested in [25], the use of commercial songs to train AI models for research may be considered fair use. 

## 5.2 Evaluation conditions and music stimuli 

We conducted a listening experiment to assess the performance of the proposed model. The study received ethics approval from our institution. Four models (BLSTM without [BL] and with [BT] transfer learning, Transformer without [TR] and with [TT] transfer learning) and the groundtruth (G) were used to create five stimuli for each melody. As we do not investigate the role of key root in this study, the chosen input melodies were converted to either C major or C minor (both training and testing data). Since it is not possible to test all possible EAR and ESR in a continuous way, 15 emotion input presets were prepared for the evaluation. Four types of emotion are represented by EAR, another four by ECR, and seven emotion distributions using the ESR. These input emotions were determined heuristically in order to be able to express as various emotions as possible. The specific configurations are shown on the study website<sup>4</sup> . The chord progressions and tempo generated by the models were converted to MIDI along with the input melody. Audio was rendered from MIDI files using FluidSynth [26] using a SoundFont called SGM-V2.01. As the research [27] has suggested that humans can distinguish the timbre of brass instruments and guitars clearly, the melody part was played by a saxophone and the harmony part by a classical guitar. 

## 5.3 Procedure and Participants 

Participants were given instructions on how to complete the study on a dedicated website<sup>5</sup> which can be used to listen to examples of generated accompaniments. The website displayed participants melodies (sampled randomly from the test set) which were represented in the piano roll style. For each of the 15 cases (corresponding to emotional presets not explicitly revealed to participants), participants had to press the ªExecute" button to obtain five (four models BT, TR, BT, TT, and groundtruth, G) musical arrangements to rate using three questions: 

- Q1 The melody and accompaniment were musically coherent. (Likert item: 0 [Disagree] - 6 [Agree]). Par- 

> 3 http://coconuts-palm-lab.com/EH/HED.zip 

> 4 http://coconuts-palm-lab.com/EmotionPresets/ 

> 5 http://coconuts-palm-lab.com/EH/ 

0:00/0:34 Q1. The melody and accompaniment were musically coherent. Q1.メロディーと伴奏は、音楽的に一貫していますか？（マッチしていますか？） Q2. How exciting (arousal) do you perceive the music to be? Q2. どれほどのこの曲を聞いて興（寛醒）を感じましたか？ 0.758 

Q3.この曲は、ボシティブですか？それともネガディブですか？ 0.237 骨骨骨骨骨骨骨骨 

Figure 2. The evaluation interface (five panels had to be completed for each melody; four models plus groundtruth). 

ticipants were instructed that musical coherence here represents a measure of how well the musical accompaniment matches the melody. 

- Q2 How exciting (arousal) do you perceive the music to be? (Continuous value from 0.0 to 1.0) 

- Q3 How negative or positive (valence) do you perceive the music to be? (Continuous value from 0.0 to 1.0) 

For Q2 and Q3, the self-assessment manikin [28] was used to support associations between numerical rating values and corresponding emotions, together with a representation of the rating in the AV space. Figure 2 provides a screenshot of the emotion rating interface. Participants rated 75 songs in total (15 emotion presets x 5 models) each lasting between approximately 15 to 30 seconds. As participants had to rate new arrangements, we assumed that familiarity with the melody, if any, did not affect the ratings (this would have to be assessed in future work). The whole experiment took about 45 minutes to complete. 

Participants could not identify the models nor the groundtruth. Different melodies were randomly chosen from the test dataset and used for each emotional preset as, in a pilot testing phase, some participants expressed that listening to the same tune over and over made it difficult to evaluate after a while. For a given emotion preset, the five stimuli (BT, TR, BT, TT, and G) were generated for a same melody, to enable fair comparison between models. 

The experiment was completed by 20 participants (7 females, 13 males). All participants were Japanese residents, 19 were Japanese and one was German. Their age ranged between 19 to 59 years (M=30.15, SD=14.05), where M and SD refer to mean and standard deviation, respectively. Six of them had at least one year of formal training in music theory. Eight had more than five years of formal training in their instrument (including voice). 

## 5.4 Results 

In statistical analyses, a Type I error of 0.05 was used except when mentioned otherwise. 

## 5.4.1 Perceived musical coherence 

Figure 3(a) illustrates the mean and standard error for each model, computed on the perceived musical coher- 

744 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
Perceived Musical Coherence<br>BL TR EAR ECR ESR<br>(a) By models (include groundtruth) (b) By input emotional representations<br><!-- End of picture text -->

Figure 3. Results of a subjective evaluation experiment, with statistics on the musical coherence across comparisons. The means and standard errors are given. 

ence considering all emotion presets. An analysis of variance (ANOVA) shows that the perceived music coherence yielded by the models presented significant differences (df=299, F = 66.750, p<.0001). Tukey’s honestly significant difference (HSD) test shows that there is a significant difference between all pairs, except between the BLSTM melody context encoder without transfer learning and the Transformer melody context encoder with transfer learning. The BLSTM model with transfer learning achieves a significantly higher musical coherence compared to the other models. However, compared to the groundtruth, the arrangements generated by the machine learning models were found to be significantly less coherent. 

Figure 3(b) displays the mean and standard error of the musical coherence for each emotional expression. ANOVA results showed a significant difference (df=319, F = 3.661, p = 0.025) and Tukey’s HSD test showed that there was a significant difference only between EAR and ECR. This suggests that the type of emotional representation impacts perceived musical coherence. In particular, it is suggested that EAR may reduce the coherence of the generated music more than the other representations. 

## 5.4.2 Errors between perceived and target emotions 

By observing the error between target and rated emotions, it is possible to assess how well each model expresses the target emotions. The errors for the EAR were obtained using Euclidean distance. The ECR error was defined using the shortest distance between the emotion AV rating and the emotion category AV quadrant. The ESR error was defined by the negative log-likelihood that the rating belongs to the two Gaussians of the GMM component. It should be noted that each absolute emotion error is thus calculated on a different scale. 

We also analyzed the relative emotion error, which indicates the degree of reflection of emotion, based on the ratio between the absolute error of the groundtruth and the absolute error of the arrangement generated by the model. If the absolute error for the music generated by the models is smaller than the absolute error for groundtruth, it suggests that the model may have been properly trained. Fur- 

thermore, the relative emotion error also makes it easier to compare different emotional representations. The relative error er is calculated as follows: 



<!-- Start of picture text -->
am<br>er = (2)<br>ag + ϵ<br><!-- End of picture text -->

where am is the absolute emotion error for a model and ag is the absolute emotion error for the groundtruth. ϵ is a small regularising term, avoiding cases where the denominator tends to zero. 

The upper part of Figure 4 illustrates the mean and standard error of the absolute emotion error (am) for each model and emotional representation. The bottom part of Figure 4 shows relative emotion error (er) boxplots. The medians and quartiles are more appropriate to interpret the results than the averages (green triangles) which are strongly influenced by outliers. The blue dotted line is a threshold representing the absolute emotion error yielded by the groundtruth. If the relative emotion error is smaller than the threshold, it suggests that the model has been able to generate arrangements that are closer to the target emotion than the original groundtruth arrangement. 

The hypothesis that all means are equal in the absolute error of the EAR is rejected based on the ANOVA (df=79, F=4.388, p=0.004). The results of Tukey’s HSD test showed that there was a significant difference in absolute error between the BLSTM with transfer learning and the Transformer without transfer learning (p = 0.003). Moreover, based on the relative emotion errors of the EAR, it was found that the median and quartiles are smaller for BLSTM with transfer learning compared to without transfer learning. In particular, up to the third quartile, the errors were below the threshold, indicating that 75% of the arrangements generated by the model with the transferlearned BLSTM are closer to the target emotion than the original one. The results show that the BLSTM with transfer learning can reduce the emotion error significantly more than the Transformer one. 

ANOVA results suggest that the mean of the absolute error for ECR is not significantly different (df=79, F=1.757, p=0.155). Unlike for EAR, transfer learning does not seem to have had any particular impact for ECR. 

According to ANOVA results, the mean of the absolute error for ESR is not significantly different (df=139, F=2.539, p=0.0557). The results of Tukey’s HSD test also showed that there were only significant differences between the BLSTM with transfer learning and the Transformer without transfer learning (p = 0.042). When observing the relative error of the ESR, the smallest median, quartiles and mean were obtained with the BLSTM with transfer learning. Thus, when ESR was used, the emotional error was the smallest when BLSTM with transfer learning was used as for the EAR. 

In addition, Figure 5 summarises the tempo of the generated arrangements for all the test data. The plotted points represent the actual tempo and the box plot shows the statistics. In all models, the tempo varied significantly when using ESR. This shows that ESR is the emotional representation that generates the most diverse tempi. The 

745 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
Absolute Errors Statistics by inputting EAR Absolute Errors Statistics by inputting ECR Absolute Errors Statistics by inputting ESR<br>0.30 0.20<br>10<br>0.25<br>0.15<br>0.20 0.8<br>0.15 0.10 0.6<br>Absolute E r or0.10 Absolute E r or Absolute E r or0.4<br>0.05<br>0.05 0.2<br>0.00 BL TR BT π 0.00 BL TR BT μ 0.0 BL TR BT<br>Relative Errors Statistics by inputting EAR 5 Relative Errors Statistics by inputting ECR 175 Relative Errors Statistics by inputting ESR<br>25<br>150<br>20 125<br>15 3 1.00<br>Relative E r or10 Relative E r or Relative E r or0.75<br>0.5 0.50<br>0.25<br>0.0<br>BL TR BT π BL TR BT μ BL TR BT π<br><!-- End of picture text -->

Figure 4. Results of the subjective evaluation experiment, with statistics on the absolute emotion error and relative emotion error across models. 



<!-- Start of picture text -->
BL tempi TR tempi<br>120.0117.5 100 H T<br>115.0 80<br>BPM110.0 112.5 BPM 60<br>105.0107.5 20<br>102.5<br>EAR ECR ESR EAR ECR ESR<br>BT tempi TT tempi<br>115 壬 100 一<br>110 中 95<br>105<br>BPM 100 BPM<br>95<br>90 75<br>85<br>EAR ECR ESR EAR ECR ESR<br><!-- End of picture text -->

Figure 5. Statistics of the tempi generated for each model from the all melodies of the test data. Each point represents a generated tempo. 

use of Gaussian variance, as in ESR, may support more complex emotional expressions. 

## 5.5 Discussion 

The highest perceived musical coherence and the lowest absolute and relative emotion errors were obtained when BLSTM with transfer learning was used for the melody context encoder. The results also show that transfer learning, a semi-supervised learning strategy, seems to be effective at generating emotional arrangements. A comparison of the relative errors of the BLSTM with transfer learning showed that the third quartile was not below the threshold only for the ECR, indicating that both EAR and ESR are superior representations for the emotion conditioning. 

The generated arrangement could be computed quickly even with Intel(R) Core(TM) i7-9700K CPU (less than approximately 2.5 seconds per 16 bars of melody for any compared models). This could be useful for real-time music generation scenarios. Due to the simplicity of the model, the arrangement may be generated more quickly than state-of-the-art techniques such as that in [12] (ap- 

proximately 50 seconds per 16 bars of melody for a lead sheet on the same CPU). However, the method in [12] generates the entire leadsheet, so the computation time cannot be directly compared to the ones reported here. 

Several limitations should be highlighted. Observing the perceived musical coherence, there was no model in this experiment that could match the groundtruth. The reasons may be overfitting and a lack of data in the dataset. In most cases, the performance of the model was improved by transfer learning, so it is expected that more data and appropriate validation will help to build better models. Emotion errors remain relatively large and it is difficult to prove that the model consistently expresses the desired emotions. As it is unclear whether emotion labels in the training dataset represents perceived or felt emotions, this may contribute to inference errors. More knowledge about the listener’s state and context would be needed to gauge more comprehensively emotion perception [9]. Results cannot be generalised since participants were from one provenance (Japan) and the sample size was small (20). More participants of different nationalities would be required to assess the generalisability of the proposed models. 

## 6. CONCLUSION 

We devised techniques for automatic harmonic and tempo arrangement of melodies controlled by emotional features, suitable for near real time applications. A network architecture to generate music expressing target emotions by predicting chord progressions and tempo for an input melody was proposed. In addition, three methods to quantify musical emotions were compared. To evaluate the results, we conducted an online listening experiment. For the melodic context encoder, the BLSTM model with transfer learning produced the most coherent arrangement and the one that best reflected the targeted emotions. The proposed method finds applications in assisting tools to create new music arrangements based on emotional directions and affective video games. 

746 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

## 7. REFERENCES 

- [1] Z. Wang, D. Wang, Y. Zhang, and G. Xia, ªLearning Interpretable Representation for Controllable Polyphonic Music Generation,º in Proc. of the 21st Int. Society for Music Information Retrieval Conference, Montréal, Canada, 2020. [Online]. Available: https://github.com/ 

- [2] P. Dhariwal, H. Jun, C. Payne, J. W. Kim, A. Radford, and I. Sutskever, ªJukebox: A generative model for music,º arXiv Preprint arXiv:2005.00341, 2020. 

- [3] Y.-C. Yeh, W.-Y. Hsiao, S. Fukayama, T. Kitahara, B. Genchel, H.-M. Liu, H.-W. Dong, Y. Chen, T. Leong, and Y.-H. Yang, ªAutomatic melody harmonization with triad chords: A comparative study,º Journal of New Music Research, vol. 50, no. 1, pp. 37±51, 2021. 

- [4] G. Hadjeres, F. Pachet, and F. Nielsen, ªDeepbach: A steerable model for bach chorales generation,º in International Conference on Machine Learning. Proceedings of Machine Learning Research (PMLR), 2017, pp. 1362±1371. 

- [5] S. Sulun, M. E. Davies, and P. Viana, ªSymbolic music generation conditioned on continuous-valued emotions,º IEEE Access, 2022. 

- [6] C. L. Krumhansl, ªAn exploratory study of musical emotions and psychophysiology.º Canadian Journal of Experimental Psychology/Revue, vol. 51, no. 4, p. 336, 1997. 

- [7] S. Swaminathan and E. G. Schellenberg, ªCurrent emotion research in music psychology,º Emotion Review, vol. 7, no. 2, pp. 189±197, 2015. 

- [8] H. H. Tan and D. Herremans, ªMusic fadernets: Controllable music generation based on high-level features via low-level feature modelling,º arXiv Preprint arXiv:2007.15474, 2020. 

- [9] J. S. Gómez-Cañón, E. Cano, T. Eerola, P. Herrera, X. Hu, Y.-H. Yang, and E. Gómez, ªMusic emotion recognition: Toward new, robust standards in personalized and context-sensitive applications,º IEEE Signal Processing Magazine, vol. 38, no. 6, pp. 106±114, 2021. 

- [10] A. J. Blood, R. J. Zatorre, P. Bermudez, and A. C. Evans, ªEmotional responses to pleasant and unpleasant music correlate with activity in paralimbic brain regions,º Nature Neuroscience, vol. 2, no. 4, pp. 382± 387, 1999. 

- [11] E. Coutinho and A. Cangelosi, ªMusical emotions: Predicting second-by-second subjective feelings of emotion from low-level psychoacoustic features and physiological measurements.º Emotion, vol. 11, no. 4, p. 921, 2011. 

- [12] D. Makris, K. R. Agres, and D. Herremans, ªGenerating lead sheets with affect: A novel conditional seq2seq framework,º in 2021 International Joint Conference on Neural Networks (IJCNN). IEEE, 2021, pp. 1±8. 

- [13] Y. Frachi, T. Takahashi, F. Wang, and M. Barthet, ªDesign of emotion-driven game interaction using biosignals,º in Proc. HCII, 2022. 

- [14] R. Guo, I. Simpson, T. Magnusson, C. Kiefer, and D. Herremans, ªA variational autoencoder for music generation controlled by tonal tension,º arXiv Preprint arXiv:2010.06230, 2020. 

- [15] H. Lim, S. Rhyu, and K. Lee, ªChord generation from symbolic melody using blstm networks,º arXiv Preprint arXiv:1712.01011, 2017. 

- [16] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, è. Kaiser, and I. Polosukhin, ªAttention is all you need,º in Advances in Neural Information Processing Systems, 2017, pp. 5998±6008. 

- [17] J. A. Russell, ªA circumplex model of affect.º Journal of Personality and Social Psychology, vol. 39, no. 6, p. 1161, 1980. 

- [18] R. Delbouys, R. Hennequin, F. Piccoli, J. RoyoLetelier, and M. Moussallam, ªMusic mood detection based on audio and lyrics with deep neural net,º arXiv Preprint arXiv:1809.07276, 2018. 

- [19] A. B. Warriner, V. Kuperman, and M. Brysbaert, ªNorms of valence, arousal, and dominance for 13,915 english lemmas,º Behavior Research Methods, vol. 45, no. 4, pp. 1191±1207, 2013. 

- [20] M. Barthet, D. Marston, C. Baume, G. Fazekas, and M. Sandler, ªDesign and evaluation of semantic mood models for music recommendation,º in Proc. International Society for Music Information Retrieval Conference, 2013. 

- [21] Y. E. Kim, E. M. Schmidt, R. Migneco, B. G. Morton, P. Richardson, J. Scott, J. A. Speck, and D. Turnbull, ªMusic emotion recognition: A state of the art review,º in International Society for Music Information Retrieval (ISMIR) 2010, vol. 86, 2010, pp. 937±952. 

- [22] M. Barthet, G. Fazekas, and M. Sandler, ªMusic emotion recognition: From content-to context-based models,º in International Symposium on Computer Music Modeling and Retrieval. Springer, 2012, pp. 228±252. 

- [23] C. Laurier, O. Lartillot, T. Eerola, and P. Toiviainen, ªExploring relationships between audio features and emotion in music,º in ESCOM 2009: 7th Triennial Conference of European Society for The Cognitive Sciences of Music, 2009. 

747 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

- [24] M. Buffa, E. Cabrio, M. Fell, F. Gandon, A. Giboin, R. Hennequin, F. Michel, J. Pauwels, G. Pellerin, M. Tikat et al., ªThe wasabi dataset: Cultural, lyrics and audio analysis metadata about 2 million popular commercially released songs,º in European Semantic Web Conference. Springer, 2021, pp. 515±531. 

- [25] OpenAI, ªUspto comment regarding request for comments on intellectual property protection for artificial intelligence innovation,º 2019, available: https://www.uspto.gov/sites/default/files/documents/ OpenAI_RFC-84-FR-58141.pdf. 

- [26] J. Newmarch, ªFluidsynth,º in Linux Sound Programming. Springer, 2017, pp. 351±353. 

- [27] S. McAdams, ªMusical timbre perception,º The Psychology of Music, pp. 35±67, 2013. 

- [28] M. M. Bradley and P. J. Lang, ªMeasuring emotion: The self-assessment manikin and the semantic differential,º Journal of Behaviour Therapy and Experimental Psychiatry, vol. 25, no. 1, pp. 49±59, 1994. 

748 

