---
paper_id: "000098"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706609/files/000098.pdf"
---

# PERCEPTUAL ERRORS IN MUSIC SOURCE SEPARATION: LOOKING BEYOND SDR AVERAGES 

Saurjya Sarkar<sup>1</sup> Victoria Moomjian<sup>1</sup> Basil Woods<sup>2</sup> Emmanouil Benetos<sup>1</sup> Mark Sandler<sup>1</sup> 1 Queen Mary University of London, 2AudioStrip Ltd. 

```
saurjya.sarkar@qmul.ac.uk,moomjianv@gmail.com
```

## ABSTRACT 

Music source separation extracts individual instrument/performer stems from mixed musical recordings. Performance is typically evaluated using metrics like source-to-distortion ratio (SDR), with higher values indicating better separation. However, relying on global SDR averages across test datasets provides limited insight into model performance. While improved average SDR suggests superior performance, it reveals little about specific strengths and weaknesses. Additionally, averaged metrics fail to account for SDR variance, which depends heavily on the musical characteristics of the test set. These limitations make cross-task/stem comparisons potentially misleading. To address these issues, we conducted a listening study evaluating source separation models across three tasks: 6- stem separation, Lead vs. Backing Vocal Separation, and Duet Separation. Participants assessed diverse examples, particularly those with poor objective or subjective performance. We categorised failure cases into three error types and found that while SDR generally correlates with perceptual ratings, significant deviations occur. Some errors substantially impact human perception but aren’t well captured by SDR, while in other cases, listeners perceive better quality than SDR suggests. Our findings reveal nuances missed in current evaluation paradigms and highlight the need to include error categorisation and performance distribution alongside averaged metrics. 

arate additional instruments from musical mixtures have not performed on par with the well-established drums, bass and vocal stem (4-stem separation) task [2, 3]. While the complexity and lack of consistent data for these other separation tasks are a significant factor, the averaged metrics used to compare different models for a given task and test dataset might be misleading when comparing models across different tasks and datasets. Even within a given separation task, comparing models based on average metrics provides limited insights. 

In this work, we attempt to evaluate how users perceive music source separation results across three music separation tasks: 6-stem separation, Lead vs. Backing Vocal Separation and chamber duet separation. We ask the users to rate 2 aspects of the task, the difficulty of the separation task and the quality of the separated output. We then compare these ratings across tasks and failure categories, in order to gain insights into how well these objective metrics like SDR correlate to the users perceptual ratings and identify if and when the objective metrics deviate from the perceptual ratings. We present the participants with different types of poorly separated examples with a wide range of output SDR scores in our study. The contributions of this study include a framework for categorising performance issues in music source separation, identify distinct types of failures that the models suffer from, the interdependence of musical contexts and separation objectives that cause these error types and insights into the varying impact these error types under different musical contexts on listeners. 

## 1. INTRODUCTION 

Deep learning based audio source separation models are trained to separate individual sound sources or sound classes from a mixture of audio sources. The complexity of the task is determined by both the constituents of the mixture, and the definition of the separation target in the context of that mixture. In the popular Music Source Separation task which was introduced in SiSEC18 [1], the input mixture is a mixed and mastered song consisting of a diverse range of instruments, however the target classes are vocals, drums and bass only. Models trained to sep- 

> © S. Sarkar, V. Moomjian, B. Woods, E.Benetos and M. Sandler. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: S. Sarkar, V. Moomjian, B. Woods, E.Benetos and M. Sandler, “Perceptual Errors in Music Source Separation: looking beyond SDR averages”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

## 2. BACKGROUND 

Source separation has flourished with deep learning across speech, music, and general audio domains, benefiting from standardised task descriptions and evaluation metrics established in the pre-deep-learning era through the SiSEC 2008 [4] public evaluation campaign. This campaign sought a comprehensive evaluation and understanding of source separation systems, including music source separation. While the definition of "stems" (subsets of distinct audio sources) was initially example-specific and dependent on individual production processes, SiSEC 2015 introduced the 4-stem (Vocals, Drums, Bass and Others) formalism which is still followed in the recent MDX21 [5] and SDX23 [6] challenges. These public evaluation campaigns use the objective metric SDR (source-to-distortion ratio) defined by Equation 1, where sˆseparated is the esti- 

839 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

mated signal and starget is the reference signal. 



<!-- Start of picture text -->
∥ star g et ∥ 2<br>SDR = log10 (1)<br>∥sˆseparated − starget ∥ 2<br><!-- End of picture text -->

Since SDR is calculated on a frame-by-frame basis, the SDRsong is calculated as the average across the 4-stems for a song. Then models are evaluated by averaging SDRsong across all songs in a given test dataset [5]. It is well known that averaged metrics give limited insights into model performance under diverse conditions and may correlate poorly to human perception [7, 8]. The SDX23 challenge conducted listening tests on their submissions to validate the objective rankings, however they did not find a clear correlation between the objective scores and perceptual ratings, with similar observations also reported in [9,10]. 

Other works have attempted to explore the task of music source separation outside the 4-stem decomposition paradigm. Datasets and models have been presented for tasks such as 6-stem separation [2, 3], chamber ensemble separation [11], vocal harmony separation [12–14] and piano accompaniment separation [15]. While these methods also report SDR, it is difficult to compare the performance or generalisability of these tasks as they lack the level of task formalism, data availability and diversity as 4-stem music separation. 

Recent works in music separation have explored the influence of musical characteristics of input mixtures on the efficacy of these source separation models. Sarkar et al. [13] report the influence of harmonic overlap amongst sources to have a negative impact separation performance. Subsequently, Sarkar et. al. [16], Ozer et al. [17] and Jeon et al. [14] have observed that pitch overlaps/unisons significantly affect the quality of separation. Jeon et al. additionaly report a 10 dB drop in quality achieved by idealratio-masking (IRM) when comparing duets and unisons. Watcharasupat et al. [2] report that models perform poorly when extending beyond the 4-stem definition into guitars and piano, and are particularly insensitive to timbral differences, which makes the separation of mixtures with similar timbres particularly challenging. They also highlight the unreliability of separation performance for organ, synth stems and backing vocals with highly variable results. Our work explores these themes further by conducting a listening study designed to evaluate the performance of source separation models in these challenging musical contexts. 

## 3. EVALUATION DATA 

We used separation results from 5 different models in our listening study, which were trained for one of three tasks: 6-stem separation, Lead/Backing Vocals separation and duet separation. We use audio stems from the URMP Dataset [18] for chamber ensemble duets, Bach Chorales and Barbershop Quartet Dataset (BCBQ) [19] for choral duets, and a private multi-track dataset of pop song covers which were downmixed to generate our 6-stem and Lead/Backing Vocals separation examples. The private 

dataset was used instead of MoisesDB [3] as the data categorisation mentioned in Section 5 was based on a pilot study conducted on the private licensed dataset. 

## 3.1 6-Stem Separation 

We use two HT-Demucs [20] models trained on different datasets for generating 6-stem separation examples. The models are trained to be able to extract the vocals, bass, drums, keys, guitars and "others" stems from pop songs. We were able to generate 2 different results for each 6-stem separation example, one using the pre-trained experimental model made available by the original authors and one using a model we trained using a private dataset (38.88 hours). 

For our private dataset, we use a similar stem definition as [3]. For piano/keys we include all keyed instruments including synths, organs and electric pianos. Our guitar stem includes both electric and acoustic guitar stems. The specific stem definitions used for the pre-trained model from [20] are unknown, however it was observed that the pre-trained model only separated Electric and Acoustic Pianos into the keys stem, while separating synths into the "Other". While we didn’t explicitly include a 4-stem model in our analysis, the vocal, bass and drums stems from our 6-stem model cover the 4-stem scenario implicitly. 

## 3.2 Lead/Backing Vocal (LV/BV) Separation 

We trained HT-Demucs with three target channels—Lead Vocals (LV), Backing Vocals (BV), and Others (accompaniment). This is similar to the Main vs. Rest separation task presented by Jeon et al. [14], however our task also involves the separation of the accompaniment stem, which is included in the input mixtures. These stems were generated by us using private multitrack data (10.75 hours). The definitions of LV and BV stems were determined on a case by case basis, since no objective definition of Lead and Backing Vocals exists. Any singer that sings at least one verse in isolation is categorised as the "lead vocals" stem, such that duets would include both singers classified as the Lead Vocals. Harmonies, non-lyrical singing were classified as the "backing vocals" stem. 

Even though our model was trained using the above stem definition for lead and backing vocals, it was observed that during inference, the model consistently separated the loudest monophonic singer as the lead vocals and any additional vocal layers as backing. Thus, if at any point the song contains only one singer (including nonlyrical singing), the model separated the solo singing voice as "Lead Vocals". On the other hand, in cases of all forms of harmonised singing, including duets, the model separated the loudest singer as "Lead Vocals" and the remaining singers as "Backing Vocals". This is discussed further in Section 5. 

## 3.3 Duet Separation 

For duet separation, we use a Dual-path Transformer Network (DPTNet) [21] with permutation invariant training 

840 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
10 0<br>Instrument and Error Type<br>MOS-SDR: y = 1.92x + 41.67<br>Ordinary Group<br>Confidence (Standard Dev)<br>Vocals - Unison<br>8 0<br>Choral-MonoT - Unison<br>Lead Vox - Unison<br>Guitar - Sdeg<br>Vocals - Sdeg<br>Other - Sdeg<br>6 0 Keys - Sdeg<br>Bass - Sdeg<br>Lead Vox - Sdeg<br>Guitar - Bleed<br>Vocals - Bleed<br>4 0 Keys - Bleed<br>Ensemble-MonoT - Bleed<br>Choral-MonoT - Bleed<br>Other - Misclass<br>Drums - Misclass<br>Backing Vox - Misclass<br>2 0 Ensemble-MonoT - X-Swap<br>Ensemble-PolyT - X-Swap<br>Choral-PolyT - X-Swap<br>Choral-MonoT - X-Swap<br>Lead Vox - X-Swap<br>0 Guitar - Noise<br>10 5 0 5 10 15 20 Ensemble-MonoT - Noise<br>Output SDR (dB) Backing Vox - Noise<br>Quality MOS<br><!-- End of picture text -->

Figure 1. Scatter plot of all test examples used in the listening study categorised by separation target and error type. The black line represents the linear fit between output SDR and Quality MOS across all test examples. The shaded region represents the standard deviation in Quality MOS observed for examples in a 3dB SDR wide sliding window. 

(PIT) [22] on EnsembleSet [11] to separate 2 source mixtures of monophonic sources. This model was chosen as duet separation tasks have been typically approached using PIT and waveform [23] based methods in other works [13, 14]. Two versions of the DPTNet model were finetuned separately with limited amounts of target domain choral data from the BCBQ dataset and chamber ensemble data from the URMP dataset respectively, as described in [16]. The examples generated by these models include mixtures of identical instruments and the same gendered singers (classified as Monotimbral Ensembles and Monotimbral Choirs) and mixtures of distinct instrument families and different gendered singing duets (classified as Polytimbral Ensembles and Choirs). 

## 4. LISTENING STUDY 

To evaluate how these different separation models perform under different task configurations, an online listening study was conducted where participants were invited to listen to a series of separation examples. They were presented with the input mixture, the target stem label and the separated outputs, including hidden reference, hidden low anchors, and separated results from one or more models. Assessors switch between these stimuli to directly compare the reference and the test signals. Participants rate each audio mixture and instrument stem on a continuous scale for perceived separation difficulty and quality, ranging from 0 to 100. The participants were presented with a calibration stage and 3 practice examples to familiarise themselves 

with the task and testing framework. Each question in the listening test had two parts: Difficulty and Quality. 

Difficulty: This part presents listeners with an input mixture and asks them to listen for a specified source (e.g. guitar) and were instructed as "Based on the mixture audio, do you think it is very difficult to separate this guitar from the other instruments? Or is it simple and easy to differentiate? You can also think about how you expect the guitar to sound on its own and how easy the guitar is to mentally focus on". They were then asked to rate how difficult they perceived the separation of that source to be. The source under evaluation varied in each question and was rated with the guidelines "Very easy" (0 to 20), "Easy" (20 to 40), "Neither easy nor difficult" (40 to 60), "Difficult" (60 to 80), and "Very difficult" (80 to 100). 

Quality: In this part, listeners were given the separated result for the given stem label, as in the Difficulty section, to evaluate the model’s separation performance. They assessed the quality based on how the estimated signal aligned with their expectations, cleanliness, and minimal bleed from other instruments. This was rated with the guidelines of "Bad" (0 to 20), "Poor" (20 to 40), "Fair" (40 to 60), "Good" (60 to 80), and "Excellent" (80 to 100). 

## 4.1 Participants and Pre-screening 

56 assessors took part in this test, and were musicians, researchers and/or audio engineers with musical and critical listening experience. The test was structured in a fashion where after the initial practice and calibration stage, 

841 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

the order of the remaining test examples was randomised. This enabled us to use the results from participants who were unable to complete rating all the examples, as long as they have encountered 1 each of our hidden anchor types. 24 participants completed the entire test, while 32 participants partially completed the test. Of these 32 participants who partially completed the test, 6 of them had to be discarded from our analysis as they did not encounter enough of our hidden anchors. 3 participants had to be removed because they didn’t rate the hidden reference and low anchors within the top 80-100 or bottom 0-20 range. An average of 30.4 responses per question were considered in this study, with each question receiving at least 27 responses and up to 37 responses. 

## 4.2 Excerpts 

The test included 47 different input mixtures: 18 6-stem, 20 duet (10 chamber and 10 choral), and 11 LV/BV examples of length ranging from 3 to 9 seconds. Along with estimated outputs, 12 hidden references were included: 3 6-stem, 4 duet, and 5 LV/BV. Participants rated the quality of 104 estimated outputs: 50 were 6-stem, 40 were Duet, and 11 were LV/BV. The discrepancy between the number of mixtures and estimated outputs is because some examples consisted of multiple outputs for different stems, while in some cases, LV/BV and 6-stem separation share the same input mixtures. 

Of the 6-stem mixtures, the estimated outputs under evaluation were 5 bass, 4 drums, 19 guitar, 5 others, 3 keys/piano, and 11 vocals with 3 additional hidden references of 1 guitar, 1 vocals, and 1 keys, respectively. Each of the 20 duet mixtures presented both estimated sources in different questions, along with 3 chamber ensemble anchors and 1 choral anchor. There were 8 lead vocal and 4 backing vocal sources evaluated which included 1 lead vocal anchor. 

## 5. DATA CATEGORISATION 

The estimated outputs presented in the listening study were chosen from diverse scenarios, including a subset of cherry-picked scenarios where the output SDR and the perceived quality of separation were poor or in disagreement, based on pilot studies. 30 estimated outputs were sampled from our test set as "Ordinary" where no explicit separation failure type was observed, while 64 examples were cherrypicked to exhibit one of the following error types: Bleed, Misclassification (Misclass), Noise, Spectral Degradation (Sdeg), Unison and Crossover-Swaps (X-Swap) which can be broadly categorised into three classes of errors. 

## 5.1 Channel Swaps 

We define channel swaps as cases where the separated output contains the output from a non-target stem and does not overlap with the target stem. This occurs during target stem silence or when target and non-target stems are swapped due to source confusion. These errors manifest 

as source misclassification (Misclass) or pitch/loudness crossover swaps (X-Swaps). 

Misclass occurs when models successfully separate a source but place it in a different channel/stem than the ground truth expects. This was notable in "others" and "backing vocals" residual stems, where content that should be "drums" or "lead vocals" was misclassified. In the example of the drum vs. other misclassification, an electronic drum based pitched percussion was classified as "drums" in our ground truth, while the models predicted those notes as "other". In an example of misclassification between lead and backing vocals, the example contained non-lyrical female singing in the backing vocals, and the lead vocals included a male lyrical singing with audio effects. The LV/BV model was able to effectively separate the two singers from background music, however the female singer was classified as lead singer as it was louder and male as backing. 

X-Swaps are similar to scenarios of misclassification, but instead here we observe the misclassification happen for a part of the audio segment, thus the separated source in the output switches in the audio segment. This occurred primarily in LV/BV and Duet separation. LV/BV models consistently separated the loudest singer as lead vocals with all others as backing. In duet separation, when the pitch trajectories of two sources crossed, models often switched source-channel alignment at the crossover point. These swaps in monotimbral (MonoT) source mixtures are less noticeable, while in polytimbral (PolyT) mixtures, they are more apparent. 

## 5.2 Bleed 

We define Bleed as scenarios where the separated output contains the output from a non-target stem in addition to the target stem. This occurs due to timbral ambiguity or spectral/pitch overlap of sources. For the case of pitch overlaps, we identify these scenarios as cases of Unison, where the target and a non-target source are playing notes in unison. In our experiments we observed that all our models fail to separate sources when they are in unison. In case of duets and lead vs. backing vocal separation, this typically results in a chorus-like effect. The case for unisons in 6-stem separation are often difficult to identify as the note durations and dynamics are very different across source types, and it is observed that in case of unisons, the less louder instrument is typically absent in the output stem and is instead present in the louder non-target stem. 

## 5.3 Artefacts 

The final error category is for scenarios where there are significant separation artefacts present in the separated stem which may affect perceptual performance. Separation artefacts may be additive or subtractive, which are identified as Noise or Spectral Degradation (SDeg) in these examples. While no pattern was observed to cause the separated output to contain additive noise, spectral degradation was typically a byproduct of misclassification or unison. Cases 

842 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
7 0<br>8 0<br>2 .5<br>1 5<br>6 0 0 .0 7 0<br>1 0<br>2.5 6 0<br>5 0<br>5.0 5 0<br>5<br>4 0 7.5 4 0<br>0<br>10.0<br>3 0<br>3 0<br>12.5<br>2 0 5<br>15.0<br>2 0<br>Vocals Bass Drums Guitar Keys OtherLead VoxBacking Vox ChoralEnsemble Vocals Bass Drums Guitar Keys OtherLead VoxBacking Vox ChoralEnsemble<br>Average Difficulty MOS Mean Input SNR (dB) Average Quality MOS Mean Output SDR (dB)<br><!-- End of picture text -->

Figure 2. Comparison of average input SNR and mean difficulty score (Difficulty MOS) across separation tasks. 

Figure 3. Comparison of average output SDR and mean quality score (Quality MOS) by across separation tasks. 

of spectral degradation were identified where the fullness of the separated stem was not observed to be satisfactory. 

## 6. SURVEY ANALYSIS 

In this section, we analyse the responses collected from our listening study as described in Section 4 on the basis of the classifications of our data points as described in Secion 5. The responses received across all valid participants in the survey are then averaged to generate a Mean Difficulty Score (Difficulty MOS) and Mean Quality Score (Quality MOS). These scores were compared with input SNR (loudness of target vs. mixture) and output SDR for each separation example which were calculated using BSS-Eval. 

## 6.1 Difficulty MOS 

In Figure 2, we compare input SNR of a target stem in a given mixture with the Difficulty MOS to explore how users perceive the difficulty of a given source separation task. It was expected that input SNR would have a strong negative correlation with Difficulty MOS, however no clear correlation was observed. When comparing the Difficulty MOS across different separation tasks, we observe that all examples outside the typical 4-stem music separation tasks were consistently rated to be of high difficulty. While the distribution of input SNRs across examples of Backing Vox, Choral and Ensemble Separation are very similar to Vocals and Bass separation examples, the former are consistently rated as highly difficult while the latter are rated to be of low difficulty. This suggests that users perceive separation of harmonically correlated sources highly challenging for a separation model. 

the linear regression model were 1.18, 0.39 and 0.72 respectively, which support our observation that SDR had the most influence on the Quality MOS. An Analysis of Variance (ANOVA) was performed to evaluate the effects of bleed types, mixture types, source types, SDR values on quality ratings. The statistics in ANOVA that indicate significant effects of the factors on quality ratings include the F-statistic and p-value, where a high F-value and a p- value less than 0.05 indicate a statistically significant effect. The results reveal that the SDR value factor rejects the null hypothesis with an F-value of 68.31 and a p-value of 2.83 × 10<sup>−16</sup> , suggesting that the output SDR significantly affects quality ratings. Spearman’s rank correlation further supports this, with a ρ coefficient of 0.66. Given ρ ranges from -1 to 1, this result indicates strong positive correlation between output SDR and quality MOS. 

In Figure 3, we compare output SDR of the test examples with the Quality MOS across different stem types. While a large amount of variance is observed between the classes and within each of the classes for both SDR and Quality MOS, comparing the averages reveal a strong correlation between SDR and Quality MOS except for the "Other" stem. Note that these averages are calculated across multiple models and multiple tasks, and the examples were cherry picked, so the variation in performance observed across stems may not be representative for the separation models used. It is also noteworthy that for some stems, namely Drums, Guitars, Backing Vox and Choral show a slight positive offset of 2-8% in their Quality MOS averages compared to stems like Vocals, Bass, Lead Vox. On the other hand Keys and Ensemble examples show a negative offset of 2-6% in their Quality MOS averages. 

## 6.2 Quality MOS 

Although SIR and SAR were also calculated, no clear correlation between these metrics and subjective scores was observed. We trained a linear regression model to use SIR, SAR and SDR as input features to predict the Difficulty MOS. The coefficients learnt for SDR, SIR and SAR in 

## 6.3 Error Analysis 

Figure 1 displays the Quality MOS score distribution across all listening study examples, annotated by instrument and error type. It includes "ordinary" examples in black, which were the examples verified not to fit our error categories from Section 5. The figure also shows a lin- 

843 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
8 0<br>Sdeg: y = 1.73x + 41.62<br>Bleed: y = 0.95x + 33.52<br>7 0 Misclass:  X-Swap: y = 0.50x + 47.23y  = 0.33x + 55.75<br>Noise: y = 0.32x + 19.14<br>Unison: y = 2.57x + 45.81<br>6 0<br>5 0<br>4 0<br>Groups<br>3 0 Sdeg<br>Bleed<br>2 0 Misclass<br>X-Swap<br>1 0 Noise<br>Unison<br>10 5 0 5 10 15<br>Output SDR (dB)<br>Quality MOS<br><!-- End of picture text -->

Figure 4. Scatter plot with linear fits between Quality MOS and output SDR categorised by error type. 

ear fit between output SDR and Quality MOS, which is calculated across all examples in the listening test and a confidence interval calculated using the standard deviation within a 3dB wide sliding window. Above 7 dB output SDR, strong agreement exists between Quality MOS and output SDR, while significant discrepancies appear for examples below 6 dB output SDR. 

In Figure 4 the relationship between quality MOS and output SDR is analysed for each error group. It is observed that Sdeg, Bleed and Unison exhibit positive correlation between quality MOS and output SDR. However, Quality MOS in cases of Misclass, Noise and X-Swap seem to not be represented well by SDR. It is also observed that Unison and Misclass are consistently rated higher as compared to Bleed and Noise. Examples of noise consistently results in the worst Quality MOS ratings, however these examples do not show any distinctive influence on SAR or SDR when compared to other error types. 

Figure 5 examines the average Quality MOS deviation from the linear fit between Quality MOS and output SDR across instrument types. We find that Bleed, Noise and Sdeg consistently show a negative bias for Quality MOS across all instruments. Conversely, the Misclass shows a consistent positive bias, which implies that users rated examples of Misclass with a higher Quality rating than the output SDR would suggest. Interestingly, examples of X- Swap show an instrument dependent impact on Quality rating deviation where MonoT swaps showed a positive shift in Quality MOS whereas swaps in PolyT mixtures and Lead Vocals show a negative shift in Quality MOS. These shifts were more profound in Ensemble duets, and less so in Choral duets. The lower average impact on choral duets may be due to the fact that users may also be more sensitive to individual vocal identities/timbres rather than their gender, which would’ve influenced the shift in the averages when considered as MonoT and PolyT based on gender. 

## 7. CONCLUSION 

In this study we explore the relationship between subjective ratings for difficulty and quality of music source separation tasks and their respective objective metrics input SNR and output SDR. We show that user perception of sep- 



<!-- Start of picture text -->
3 0<br>Instrument<br>Choral-MonoT Vocals Bass<br>Ensemble-MonoT Backing Vox Lead Vox<br>Guitar Drums Choral-PolyT<br>2 0 Keys Other Ensemble-PolyT<br>1 0<br>0<br>1 0<br>2 0<br>Error Type<br>Bleed Misclass Noise Sdeg Unison X-Swap<br>Quality MOS Deviation<br><!-- End of picture text -->

Figure 5. Average deviation from Quality MOS-SDR linear fit categorised by separation target and error type. 

aration difficulty is highly dependent on the musical context and separation target, and does not strongly correlate with input SNR. Our observations show that SDR on average is a representative objective metric for music source separation, but subjective metrics consistently agree with SDR only above 7 dB. On the other hand, our study highlights the large variance and potential disagreement between subjective Quality ratings and SDR for values less than 7 dB. Our classification of various error types shows that mismatch between task definition and separation capabilities based on target ambiguity lead to disagreement between perceptual ratings and objective metrics like SDR, which result in much higher quality MOS than expected for low SDR examples from tasks beyond 4-stem separation. We also highlight the failure of objective metrics to capture Noise as an error type, especially in examples with SDRs between 0-6 dB, which result in very low Quality ratings, resulting in very high variance in this range. 

Our results highlight the challenges faced in music source separation tasks which explore beyond the typical 4 stem Vocals, Drums, Bass and Others tasks. Timbral ambiguity in stems like keys and guitars significantly affect separation performance. On the other hand, for the task of Lead Vocal Separation, subjective definitions of Lead Vocals are not consistent, and models are instead shown to be capable of separating the loudest monophonic source within a vocal stem. Meanwhile, for PIT-based ensemble separation, we observe that models often do not preserve source consistency across a separation frame and may suffer from channel swaps, which significantly affect SDR performance but do not always negatively influence perceptual ratings. We also show that models cannot separate unisons effectively across all 3 tasks, however these failures are accurately captured by SDR, and the resulting influence on perceptual ratings are in agreement with SDR. Our findings highlight the need for future source separation evaluations to report performance distribution and categorised failures alongside averaged metrics. This would improve our ability to compare models across tasks and may also shed light on how they work. 

844 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 8. ACKNOWLEDGMENTS 

This work was supported by UKRI - Innovate UK (Project no. 10102241). The duet separation models were trained using the Baskerville Tier 2 HPC service (https://www.baskerville.ac.uk/), funded by the EPSRC and UKRI through the World Class Labs scheme (EP/T022221/1) and the Digital Research Infrastructure programme (EP/W032244/1) and is operated by Advanced Research Computing at the University of Birmingham. The 6-stem and LV/BV models were trained on GPUs provided and funded by Audiostrip LTD. 

## 9. ETHICS STATEMENT 

This user study obtained the necessary ethical approval (QMERC20.565.DSEECS24.049) from the Queen Mary Ethics of Research Committee. The private dataset used was purchased and licensed by AudioStrip Ltd., and they owned the appropriate rights for use as required by this study. 

- [8] D. Ward, H. Wierstorf, R. D. Mason, E. M. Grais, and M. D. Plumbley, “Bss eval or peass? predicting the perception of singing-voice separation,” in 2018 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2018, pp. 596–600. 

- [9] M. Torcoli, T. Kastner, and J. Herre, “Objective measures of perceptual audio quality reviewed: An evaluation of their application domain dependence,” IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 29, pp. 1530–1541, 2021. 

- [10] E. Rumbold, G. Tzanetakis, and B. Pardo, “Correlations between objective and subjective evaluations of music source separation,” 21st Sound and Music Computing Conference, SMC 2024, 2024. 

- [11] S. Sarkar, E. Benetos, and M. Sandler, “Ensembleset: a new high quality synthesised dataset for chamber ensemble separation,” in Proc. of the 23rd International Society for Music Information Retrieval Conference (ISMIR), 2022, pp. 625–632. 

## 10. REFERENCES 

- [1] F.-R. Stöter, A. Liutkus, and N. Ito, “The 2018 signal separation evaluation campaign,” in International Conference on Latent Variable Analysis and Signal Separation. Springer, 2018, pp. 293–305. 

- [2] K. N. Watcharasupat and A. Lerch, “A stem-agnostic single-decoder system for music source separation beyond four stems,” in Proceedings of the 25th International Society for Music Information Retrieval (ISMIR), San Francisco, CA, USA, nov 2024. 

- [3] I. G. Pereira, F. Araujo, F. Korzeniowski, and R. Vogl, “Moisesdb: A dataset for source separation beyond 4 stems,” in Ismir 2023 Hybrid Conference, 2023. 

- [4] E. Vincent, S. Araki, and P. Bofill, “The 2008 signal separation evaluation campaign: A community-based approach to large-scale evaluation,” in International Conference on Independent Component Analysis and Signal Separation. Springer, 2009, pp. 734–741. 

- [5] Y. Mitsufuji, G. Fabbro, S. Uhlich, F.-R. Stöter, A. Défossez, M. Kim, W. Choi, C.-Y. Yu, and K.-W. Cheuk, “Music demixing challenge 2021,” Frontiers in Signal Processing, vol. 1, p. 808395, 2022. 

- [6] G. Fabbro, S. Uhlich, C.-H. Lai, W. Choi, M. MartínezRamírez, W. Liao, I. Gadelha, G. Ramos, E. Hsu, H. Rodrigues et al., “The sound demixing challenge 2023–music demixing track,” Transactions of the International Society for Music Information Retrieval, vol. 7, no. 1, 2024. 

- [7] E. Cano, D. FitzGerald, and K. Brandenburg, “Evaluation of quality of sound source separation algorithms: Human perception vs quantitative metrics,” in 2016 24th European Signal Processing Conference (EUSIPCO). IEEE, 2016, pp. 1758–1762. 

- [12] T. Nakamura, S. Takamichi, N. Tanji, S. Fukayama, and H. Saruwatari, “jacappella corpus: A japanese a cappella vocal ensemble corpus,” in ICASSP 20232023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2023, pp. 1–5. 

- [13] S. Sarkar, E. Benetos, and M. Sandler, “Vocal harmony separation using time-domain neural networks,” in Proc. Interspeech 2021, 2021, pp. 3515–3519. 

- [14] C.-B. Jeon, H. Moon, K. Choi, B. S. Chon, and K. Lee, “Medleyvox: An evaluation dataset for multiple singing voices separation,” in ICASSP 2023-2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2023, pp. 1–5. 

- [15] Y. Özer, S. Schwär, V. Arifi-Müller, J. Lawrence, E. Sen, and M. Müller, “Piano concerto dataset (pcd): A multitrack dataset of piano concertos,” Transactions of the International Society for Music Information Retrieval, vol. 6, no. 1, 2023. 

- [16] S. Sarkar, L. Thorpe, E. Benetos, and M. Sandler, “Leveraging synthetic data for improving chamber ensemble separation,” in 2023 IEEE Workshop on Applications of Signal Processing to Audio and Acoustics (WASPAA), 2023, pp. 1–5. 

- [17] Y. Özer and M. Müller, “Source separation of piano concertos using musically motivated augmentation techniques,” IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 32, pp. 1214– 1225, 2024. 

- [18] B. Li, X. Liu, K. Dinesh, Z. Duan, and G. Sharma, “Creating a multitrack classical music performance 

845 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

dataset for multimodal music analysis: Challenges, insights, and applications,” IEEE Transactions on Multimedia, vol. 21, no. 2, pp. 522–535, 2018. 

- [19] R. Schramm, E. Benetos et al., “Automatic transcription of a cappella recordings from multiple singers.” Audio Engineering Society, 2017. 

- [20] S. Rouard, F. Massa, and A. Défossez, “Hybrid transformers for music source separation,” in ICASSP 23, 2023. 

- [21] J. Chen, Q. Mao, and D. Liu, “Dual-Path Transformer Network: Direct Context-Aware Modeling for Endto-End Monaural Speech Separation,” in Proc. Interspeech 2020, 2020, pp. 2642–2646. 

- [22] D. Yu, M. Kolbæk, Z.-H. Tan, and J. Jensen, “Permutation invariant training of deep models for speakerindependent multi-talker speech separation,” in 2017 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2017, pp. 241–245. 

- [23] Y. Luo and N. Mesgarani, “Tasnet: time-domain audio separation network for real-time, single-channel speech separation,” in 2018 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2018, pp. 696–700. 

846 

