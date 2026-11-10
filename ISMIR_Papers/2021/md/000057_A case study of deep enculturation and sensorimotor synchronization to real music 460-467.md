---
paper_id: "000057"
year: 2021
title: "A case study of deep enculturation and sensorimotor synchronization to real music 460-467"
source_url: "https://archives.ismir.net/ismir2021/paper/000057.pdf"
---

# **A CASE STUDY OF DEEP ENCULTURATION AND SENSORIMOTOR SYNCHRONIZATION TO REAL MUSIC** 

**Olof Misgeld**<sup>1</sup><sup>_,_2</sup> **Torbjörn Gulz**<sup>1</sup><sup>_,_2</sup> **Andre Holzapfel**<sup>2</sup> **J¯ura Miniotait˙e**<sup>2</sup> 

1 KMH Royal College of Music, Sweden 

2 KTH Royal Institute of Technology, Sweden 

misgeld@kth.se, gulz@kth.se 

## **ABSTRACT** 

Synchronization of movement to music is a behavioural capacity that separates humans from most other species. Whereas such movements have been studied using a wide range of methods, only few studies have investigated synchronisation to real music stimuli in a cross-culturally comparative setting. The present study employs beat tracking evaluation metrics and accent histograms to analyze the differences in the ways participants from two cultural groups synchronize their tapping with either familiar or unfamiliar music stimuli. Instead of choosing two apparently remote cultural groups, we selected two groups of musicians that share cultural backgrounds, but that differ regarding the music style they specialize in. The employed method to record tapping responses in audio format facilitates a fine-grained analysis of metrical accents that emerge from the responses. The identified differences between groups are related to the metrical structures inherent to the two musical styles, such as non-isochronicity of the beat, and differences between the groups document the influence of the deep enculturation of participants to their style of expertise. Besides these findings, our study sheds light on a conceptual weakness of a common beat tracking evaluation metric, when applied to human tapping instead of machine generated beat estimations. 

## **1. INTRODUCTION** 

Feeling the beat is universal to music experience and production, and rhythmical patterns are determinant for musical genres across the globe. _Enculturation_ concerns the influence of the surrounding cultural environment on the development of individuals’ perception, cognition and behavior. _Sensorimotor synchronization_ (SMS) regulates how humans synchronize their behavior to time ordered stimuli in various sensory modalities [1]. The enculturation in musical contexts has been explored in auditory SMS studies on the perception and reproduction of rhythms in 

© O. Misgeld, T. Gulz, A. Holzapfel and J. Miniotait˙e . Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). **Attribution:** O. Misgeld, T. Gulz, A. Holzapfel and J. Miniotait˙e , “A case study of deep enculturation and sensorimotor synchronization to real music”, in _Proc. of the 22nd Int. Society for Music Information Retrieval Conf.,_ Online, 2021. 

different cultural contexts [2]. However, most SMS studies have used generated stimuli, and only a small number of studies – including cross-cultural studies – have had humans tapping along with real music [3]. In general, research on enculturation challenges the dominance of Western music in music perception and cognition research [4,5]. 

Previous studies in rhythm perception have been based on subjects with highly different cultural and ethnic backgrounds [2–9]. The present study compares musicians within a similar cultural group: music students at the same higher music education institution, with specialization in either one of the two genres. Hence, the present study adds to previous research on the role of deep enculturation in rhythm perception by examining sensorimotor synchronization of musicians in two different musical genres. 

We ask whether deep enculturation as practitioners leads to higher agreement in sensorimotor synchronization to music stimuli among the group of musicians practicing the particular style. Furthermore, we explore how emerging differences between groups of musicians are tied to genre-specific musical parameters. To this end, we record subjects from two groups of musicians tapping the beat to music examples from two genres. Our analysis employs a combination of computational measures and qualitative analysis in order to shed light on genre-specific interpretations of musical meter. We apply beat tracking evaluation metrics in order to estimate the degree of agreement between the tapping responses in the two groups of musicians. In addition to the computational agreement estimate, recording the tapping in audio format enables us to capture both the time instances of responses and their dynamic emphasis. Based on this information, we explore the relation between tapping responses and metrical structure based on histograms of the recorded tapping responses. 

The genres included in this study are jazz music and Scandinavian traditional folk music, both known for their intricate rhythmical structures. The choice of these two genres was further motivated by the fact that they are both taught at the Royal College of Music in Stockholm. This results in an environment to recruit participants who share a common cultural background, but differ mainly in terms of the musical style in which they have particular expertise. 

In Scandinavian folk music, some triple meter dance music forms include styles with non-isochronous, asymmetric beat patterns [10, 11]. Although these patterns are 

460 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

well-documented in contemporary Nordic folk music and dance practice, behavioral responses to this music have not yet been approached in the context of SMS studies. In jazz, on the one hand, a large part of the repertoire consists of music with a definite relation to the beat, which is controlled by quarter notes played in the bass and the ride cymbal [12]. On the other hand, in some jazz music the main beat is not connected to a specific instrument. Identifying the beat and subdivisions can therefore be challenging for a listener. Based on these genre characteristics we expect varying agreements between the the two groups of musicians in three aspects: the dynamic emphasis of the beats in a measure, concerning non-isochronous asymmetric beat patterns in Scandinavian folk music, and on the main metrical level in jazz music. 

The remainder of the paper is structured as follows: in Section 2 we refer to relevant research on sensorimotor synchronization, enculturation, mutual agreement metrics, and rhythm and meter perception within the two genres. Section 3 describes the experimental setup and methods for data collection and analysis, including the process of correcting the mutual agreement metrics for a detected tempo bias caused by human tapping motor noise. In Section 4 we present the results of our analysis, which are further discussed in Section 5. 

## **2. BACKGROUND-RELATED WORK** 

## **2.1 Sensorimotor synchronization and tapping studies** 

One of the most common experimental setups to explore SMS is by means of tapping studies, where the main goal is to examine subjects’ ability to coordinate hand or finger movement to rhythm-stimuli. These stimuli usually consist of relatively simple rhythms synthesized using click sounds, and subjects are instructed to synchronize with the stimuli as accurately as possible. As summarized by [1,13], synchronisation is characterized by a negative asynchrony with a variability of the standard deviation of the asynchronies (SD _asy_ ) depending on the intervals in stimuli and tapping responses. 

In discourse about music the concepts of time and timing are used in many ways, frequently with a judgemental connotation. One way to quantitatively examine timing is to perform tapping experiments, and there has been relatively much research performed that indicates higher tapping accuracy for professional musicians than for nonmusicians. For instance, magnetic resonance experiments showed how professional pianists had a faster and different learning process in complicated tapping attempts [14]. For pianists, however, tapping can be regarded as similar to everyday practice at the instrument. It has been shown by [15] that being in their proper environment with their instruments helps musicians to perform with a significantly lower synchronization error when playing the drum set than in previous tapping experiments. 

Whereas the vast majority of tapping studies has been conducted with simple rhythmic stimuli, tapping data obtained when using musical stimuli can provide addi- 

tional information. Palmer and Krumhansl describe how more experienced listeners/practitioners use subdivisions to identify meter and beats with more confidence [16]. London et al. [17] move a step further and question the traditional Western way of identifying beats based on melodic and rhythmic accents and argue that the rhythmic organization in certain music styles can be based on contrametricity: a significant portion of note onsets tend to be non-congruent with the metrical framework. Here, they base their arguments on research on drum ensembles in Mali [18] and Turkish modal art music [19]. Hence, tapping studies with real music stimuli may provide valuable information when the informants are musicians with indepth knowledge of music structure. 

## **2.2 Enculturation and meter perception** 

Cross-cultural studies have provided evidence for the effects of enculturation on various aspects of music perception and cognition, and several studies have compared the perception of rhythmical and metrical categories between distant cultural groups [4, 5]. Experimental studies [3,6, 7, 20] indicate that, for rhythm perception, familiarity is a more important factor than complexity based on integer ratios. The perception of rhythm is known to be primed from the metrical context [21], and practitioners of non-Western musical cultures have been shown to accurately represent the complex asynchronous rhythmic patterns common in their respective genre [2]. Studies have explored rhythm perception and enculturation at early ages [22], and [9] have reported effects from passive, shortterm exposure on children’s perception of non-isochronous meter. Drawing on these findings, recent works have presented a probabilistic model simulating enculturation in meter perception, with predictive coding inferred from previous rhythmic exposure [23]. 

## **2.3 Scandinavian traditional folk music** 

Polska, springlek, pols and springar are Swedish and Norwegian triple meter music and dance forms that in regional sub-forms include asymmetric beat [10, 11]. In addition to the asymmetry on the beat level, sub-beat rhythm patterns are often non-isochronous and un-even [24], so that asymmetric beat lengths cannot be attributed from simply adding equal shorter pulse units [25, 26]. Rather, it has been suggested that beat asymmetry should be understood as uneven subdivisions of an isochronous _common slow pulse_ at measure level, and in relation to the periodicity of dance movements [25]. Furthermore, variations in asymmetric beat lengths occur within performances, corresponding with distinct melodic rhythm gestalt patterns [27]. The close connection with dance is reflected in how musicians dynamically articulate beat cycles [27]. As a consequence, understanding the metrical structure requires some familiarity with these specific musical forms. As this music is often performed solo, on violin or fiddle, with plenty of ornamentation and complex bowing patterns, researchers [28] have pointed to the challenge of finding sound events that precisely correspond to the experienced 

461 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

musical beat. The Norwegian folk musician and researcher Groven reported tapping on a morse transmitter for measuring uneven beat ratios in springar/polska music already in the 1930-ties [29], more recent studies have applied tapping [30], sound graph analysis [11, 24, 30], and motion capture [31, 32] for analyzing asymmetric beat patterns in Scandinavian folk music. However, at this point we are not aware of tapping studies comparing musicians from different genres encountering these music forms. 

## **2.4 Jazz music** 

Jazz music developed rapidly during the 20th century and now consists of many different sub-genres from early jazz, such as Dixieland and swing, to modern jazz such as modal jazz and free jazz [33]. Common to the different specializations is that they all contain several complex parts in terms of melody, harmony, and rhythms. The rhythmic complexity becomes particularly evident in the more modern jazz, where nontraditional meters and intricate percussive subdivisions are used [12]. The complexity includes different overlay techniques like the placement of 2- or 4- cycle patterns over 3/4 meter and 3/4 or 3/2 patterns over 4/4 meter. The musicians have to agree on where the – sometimes hard to discern – beat is while playing. Additional difficulty for an inexperienced listener to perceive the beat may emerge when the beat is not directly marked by any instrument. Studies in cognitive neuroscience explored the pre-attentive brain response to various musical parameter changes and reported high measures for jazz musicians compared to classical and rock/pop musicians [34]. Other studies suggest listening, but above all, performing music in specific genres generates a clearer meter perception [7]. Many jazz tunes are also performed in a high tempo (up to 400 BPM), which also challenges the musician’s technique and the listener’s beat perception. 

## **2.5 Mutual agreement** 

Most of the evaluation in SMS experiments is based on statistical analysis of the asynchronies between participant responses and stimulus onsets (see Section 1 in [1] for an overview). Such an analysis would require the compilation of a reference beat for the music stimuli, which is a problematic procedure since not all beats coincide with note onsets. In the absence of a reference annotation, previous work [35] has suggested to employ beat tracking evaluation metrics to estimate the mutual agreement between beat estimates obtained from beat tracking algorithms. This approach has been used to analyze the agreement between human beat tapping sequences in the context of exploring music collections [36]. Among various employed metrics, information gain [37] was found to produce reliable estimates for such mutual agreement. 

## **3. METHOD** 

## **3.1 Apparatus** 

Music stimuli were presented through studio-monitoring headphones (Beyerdynamic DT 700 PRO headset). The 

experimental setup applied first by [38] was used to record participant tapping. It consists of a sensor made from soft material, with a microphone attached to the surface of the sensor. A Focusrite 6i6 USB sound card was used to simultaneously record the microphone output and a split of the headphone signal in two channels of a stereo wav file. 

## **3.2 Stimuli** 

20 stimuli of jazz and 20 stimuli of Scandinavian folk music were chosen by the first and second author, who are performers and teachers within each of these genres, and affiliated to the same higher music education institution as the participants<sup>1</sup> . In addition, two practice stimuli were selected for each style. Each excerpt is about 42 seconds long. The measure onsets were manually annotated by the two first authors for later analysis. The tempi – based on these annotations – were between 109 to 155 beats per minute (BPM) (M=135, SD=12) for folk music and 55 and 294 BPM (M=183, SD=66) for jazz, respectively. Whereas the tempo means are similar, the Scandinavian folk examples, all related to dance, have a much smaller range of tempi. The Jazz stimuli in this study are mainly recorded between 1960-2000, originating in American post-bebop or a Nordic jazz tradition. The ensembles are mostly piano trios or quartets with one horn player. 

## **3.3 Participants** 

The participants for the experiment were advanced students of either jazz or folk music programs at the Royal College of Music in Stockholm. In total 8 jazz musicians and 9 folk musicians participated in the study. Participants were between 20 and 29 years old (mean = 23.5 years), 6 male and 11 female. 

Before participating in the experiment, each participant filled out a questionnaire with questions about their education, their experience with different musical genres, and their dancing experience. All participants lived in Stockholm and spoke Swedish. Many participants had a background in playing other genres beyond the focus of their study program. However, no jazz musicians stated that they play folk music, and only one folk musician stated that they have experience playing jazz music. The participants had had regular practice on a musical instrument or singing between 4 and 18 years (mean = 10.6 years). All folk musicians answered that they danced on occasion and had dancing as part of their study curriculum. On the other hand, only three jazz musicians danced occasionally whereas the other five jazz musicians responded that they never dance. 

## **3.4 Procedure** 

The experiment started with the participant signing a consent form and then receiving verbal instructions on using the equipment. They were then instructed to tap the beat to the music excerpts they were going to listen to, and they 

> 1 Music stimuli, tapping data and complementary results histograms are provided here: https://bit.ly/3uJ7EC7. 

462 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

were asked to emphasize the beat that they considered the first in each measure. Before presenting the musical stimuli, an isochronous clicking track with IOI of 0.5s was played, and the participant was asked to tap in synchrony to the sound. This served the purpose to adjust playback volume, and to check the amplitude of the sensor output. After that, music stimuli were presented in two blocks, one for each music genre. Each block started with the two practice stimuli, followed by the 20 stimuli in randomized order. Further, the order of the blocks was divided so that half of the participants from each group started with the jazz stimuli, and the other half started with the folk music stimuli. The whole experiment took about 50 minutes, including a concluding discussion in which participants had the opportunity to ask questions about the project. 

## **3.5 Data analysis** 

The recorded responses were analyzed using a simple thresholding as proposed by [38], resulting in a list of time instances for tap locations for each response. We conducted three types of quantitative analyses using the responses and the obtained tap annotations: 

**1) Mutual agreement:** Information Gain (IG) (see Section 2.5) was calculated between all tapping annotations of each group for a particular stimulus. The IG takes on values between 0 and 5.3, with low numbers indicating low agreement. Preliminary experiments indicated low IG values for human tapping responses as compared to values reported for accurate beat trackers, with a decrease of IG values for increasing tempi. To investigate this trend, the authors recorded their own tapping responses to isochronous clicks at four IOI rates between 60 and 180 bpm. From these sequences, a similar linear decrease was observed for IG with increasing tempo, as displayed in Figure 1. The slope (-0.0048) and intercept (3.232) of this trend were determined using linear regression. Using the information of the annotated tempi of the stimuli, the IG values for comparisons between the participants’ responses were corrected using these regression values. It is worth pointing out that such a problem of a beat tracking metric has not been observed so far, and it is caused by the overall standard deviation of human tapping [1], a phenomenon absent from beat tracking algorithms. 

**2) Inter-tap intervals (ITI):** Using the tap annotations, histograms of ITI were calculated for each group and stimulus. These were then analyzed in relation to the annotated tempo to investigate if certain metrical levels tend to be preferred depending on group and musical style. 

**3) Accent histograms:** Whereas the previous two analyses use the tap annotations as input, the histogram analysis uses the recorded responses in which emphases of the first beat of a bar are reflected. Each response is differentiated over time and half-wave rectified to avoid eventual cancellation of positive and negative values. Each response is then normalized to have a maximum magnitude of one to compensate for varying tapping intensities between participants. All recordings have been annotated with the bar positions, and using this information the normalized re- 



<!-- Start of picture text -->
3,50<br>Gain<br>3,00<br>Information<br>2,50<br>eo<br>2,00 75 100 125 150 175<br>BPM<br><!-- End of picture text -->

**Figure 1** . Linear decrease in Information Gain computed from the authors’ tapping to isochronous clicks at four different IOI rates. 

sponses are divided into bar length segments. To create histograms of equal length independent from tempo, each such bar length segment is divided into 60 equal-duration bins, and the values of the normalized response between the bin boundaries are added. For a whole song, these bar-length histograms are added for each individual participant, and the mean histogram across all participants of a group for each song is computed. These histograms will be analyzed regarding the relation between the strongest, and the second strongest peak, which will provide an estimate for the average emphasis of a downbeat position. Furthermore, the positions of the peaks will facilitate an analysis of the perceived position of the downbeat, and the degree of non-isochronous tapping (especially for Scandinavian folk music). 

The two first authors individually annotated all files with aspects that make these files potentially difficult to tap to. These annotations will provide further background for the contextualization of the above-listed three quantitative analysis methods. 

## **4. RESULTS** 

Our analysis resulted in tempo corrected information gain scores, ITI histograms and accent histograms for each group and music stimulus. The mean tempo corrected information gain scores for each stimulus within each group of musicians were analyzed using n-way ANOVA tests to determine if the averages in the dataset differed with respect to the type of musician and genre. The music genre of the stimuli had an impact on the agreement of the musicians as a whole (F(Genre) = 34.62, p _<_ 0.001), with an interaction effect between genres and groups of musicians (F(Musician*Genre) = 7,62, p = 0.007). The average score for each combination of musician and music genre in Figure 2 reveals that jazz musicians agreed more on how to tap the beat to jazz music than how to tap the beat to folk music. At the same time, there was no significant difference between the genres for the folk musicians. The ANOVA indicated no difference between the overall performance 

463 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 



<!-- Start of picture text -->
Genre<br>2,50 Jazz music<br>Folk music<br>2,00<br>1,50<br>Information Gain1,00<br>0,50<br>0,00<br>Jazz Folk<br>Musician<br>Figure 2 . Mean tempo corrected information gain between<br>groups of jazz (N=8) and folk (N=9) musicians tapping to<br>jazz (N=20) and Scandinavian folk (N=20) music stimuli.<br>95% confidence intervals in brackets.<br>0.2 JZ8, Jazz musicians JZ8, Jazz musicians<br>150<br>0.1 100<br>50<br>Tap emphasis<br>Emp i rcal Probab i lty 00 500 1000 1500 0 20Bins 40 60<br>ITI in ms<br>0.2 JZ8, Folk Musicians 200 JZ8, Folk Musicians<br>0.1 100<br>Tap emphasis<br>Emp i rcal Probab i lty 0 500ITI in ms1000 1500 00 20Bins 40 60<br>0.4 JZ6, Jazz Musicians 300 JZ6, Jazz musicians<br>200<br>0.2<br>100<br>Tap emphasis<br>Emp i rcal Probab i lty 0 200 400 600 800 1000 0 20Bins 40 60<br>ITI in ms<br>0.2 JZ6, Folk Musicians 200 JZ6, Folk musicians<br>0.1 100<br>Tap emphasis<br>Emp i rcal Probab i lty 0 200 400ITI in ms600 800 1000 0 20Bins 40 60<br><!-- End of picture text -->

**Figure 2** . Mean tempo corrected information gain between groups of jazz (N=8) and folk (N=9) musicians tapping to jazz (N=20) and Scandinavian folk (N=20) music stimuli. 95% confidence intervals in brackets. 

**Figure 3** . Tapping to jazz. ITI (left) and accent (right) histograms for the two groups of musicians with two examples of stimuli in slow (JZ8, 55 BPM) and fast (JZ6, 206 BPM) tempo. The dashed vertical lines in the accent histograms show isochronous beat positions. 

of the two groups of musicians (F(Musician) = 0.64, p = 0.426). 

The ITI and accent histograms facilitate a more detailed and complementary analysis of differences between the groups of musicians’ tapping behavior in the different examples. These differences relate to the preferred metrical level in jazz, to tapping with non-isochronous beat in folk music, and to the accentuation of metrical periodicity in folk music. 

The ITI histograms displayed in Figure 3 exemplify jazz stimuli where the two groups tapped at different metrical levels. All jazz music stimuli were in duple meters, with four beats per measure, and with an annotated tempo between 55 and 294 BPM. In all jazz stimuli with tempi _>_ 200 BPM, a portion of the folk musicians’ tapping was at half the tempo compared to the majority of jazz musicians’. The accent histograms for some of these show 



<!-- Start of picture text -->
0.15 SF12, Jazz musicians 150 SF12, Jazz musicians<br>0.1 100<br>0.05 50<br>Tap de dis<br>200 400 600 800 1000 1200 40 60<br>Emp i rcal Probab i lty ITI in ms 20Bins<br>0.15 SF12, Folk musicians 300 SF12, Folk musicians<br>0.1 200<br>0.05 100<br>Tap emphasis<br>Emp i rcal Probab i lty 00 200 400ITI in ms600800 1000 1200 20Bins 40 60<br>0.2 SF20, Jazz musicians 150 SF20, Jazz musicians<br>100<br>0.1<br>50<br>Tap emphasis<br>200 400 600800 1000 1200 40 60<br>Emp i rcal Probab i lty ITI in ms 20Bins<br>SF20, Folk musicians 300 SF20, Folk musicians<br>0.2<br>200<br>0.1 100<br>Tap emphasis<br>200 400 6008001000 1200 20 40 60<br>Emp i rcal Probab i lty ITI in ms Bins<br><!-- End of picture text -->

**Figure 4** . Tapping to Scandinavian folk music. ITI (left) and accent (right) histograms for the two groups of musicians with two examples of stimuli with asymmetric beat: _polska_ with short-long-medium (SF12, 146 BPM), and long-medium-short (SF20, 130 BPM) beat patterns. The dashed vertical lines in the accent histograms show isochronous beat positions. 

peaks on beat 2 and 4 for folk musicians, indicating that the half-tempo tapping was partly phase-shifted so that folk musicians tapped only on beat two and four of the four beats tapped by jazz musicians (JZ6 in Figure 3). In the two slowest jazz examples, with annotated tempi of 55 and 60 BPM, the group of folk musicians partly tapped at the triple tempo. In contrast, the group of jazz musicians stayed at the annotated tempo level or in one song partly tapped in double tempo, as exemplified by JZ8 in Figure 3. 

Figure 4 illustrates two folk music stimuli where folk musicians tapped along with the asymmetric beat. The ITI histogram for folk musicians tapping to stimuli SF12 displays a peak around 300ms corresponding to a shorter beat, and the related accent histogram displays a shortlong-medium pattern, including some variability in the tapping of the second beat. This variability could be explained by the polska-beat itself - varying between more or less acute asymmetry. However, listening to the recorded tapping responses for these tunes revealed that, among folk musicians, some were tapping an isochronous beat and others an asymmetric beat. For the second stimuli (SF20) depicted in Figure 4, the histograms illustrate that folk musicians tap consistent with a long-medium-short asymmetric beat pattern. For jazz musicians tapping to folk music stimuli with an asymmetric beat, no consistent non-isochronous tapping was found from these histograms. Instead, it appears that jazz musicians were tapping isochronously but with a low agreement between the musicians. 

For most folk music stimuli, with folk musicians tapping, the triple meter was distinguishable in the accent his- 

464 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

tograms, with a stronger signal on the first beat. The second beat then appeared weaker, and the third beat was a little bit stronger than the second, as exemplified with stimuli SF12 in Figure 4. No consistent metrical accentuation was found for jazz musicians tapping to folk, and for tapping to jazz, the first beat of four was accentuated only with a few of the stimuli. 

Additionally, some observations were made during the experiments. All of the participants in the experiment marked metrical structures in addition to the tapping on the cushion. For instance, participants nodded their heads, tapped with their other hand on a surface next to them, or snapped their fingers. Most of the folk musicians were surprised when they were asked to tap the beat with their hands and to tap all the beats in the measure. One folk musician said, “It is more important to keep the beat with the feet, at least for us. We are used to stomping the beat on one and three”. Almost all of the folk musicians were tapping with their feet in addition to tapping fingers on the cushion. When hearing examples from the genre that the participants were not used to, all participants at first reacted to signal that they experienced discomfort. They either made a facial expression signaling surprise, or they laughed, signaling that they found the task difficult. Most of the participants stated afterward that they were not used to listening to the genre that they were less familiar with. 

Two of the jazz musicians pointed out that it was harder to distinguish a clear beat pattern with folk music, since many folk music examples had only one instrument playing, while the jazz music examples had multiple instruments playing. 

## **5. DISCUSSION** 

Cross-cultural studies shed light on universals and specifics in music cognition and perception [5]. This study adds to previous findings on the role of enculturation in the context of music meter perception by comparing advanced musicians trained in different genres but with otherwise similar cultural backgrounds. Our analysis of differences between groups combined computational measurements with analysis by genre-experts. A mutual agreement estimate (see Section 2.5) indicated significantly higher agreement among jazz musicians when tapping to jazz music than when tapping to Scandinavian folk music. Further analysis of tapping patterns and the dynamic emphasis of beats, using ITI and accent histograms, provided more insights into group-specific interpretations of meter and beat. For jazz musicians tapping to jazz, we found a more consistent alignment to the extreme tempi, compared to folk musicians who were more likely to tap at half-tempo (for faster tempi) or sub-divide (for slower tempi). For example, marking the triple-subdivision - the “swing” - at a slow tempo (see Figure 3) is mainly encountered among folk musicians. Furthermore, part of the non-jazz experts’ tapping was phase-shifted, marking only beat 2 and 4. 

The folk music examples were all ternary meter, including non-isochronous, asymmetric styles of polska. In addition to this metric particularity, these tunes were performed 

solo on bowed instruments with only occasional accompaniment of foot-tapping. These properties pose challenges for inexperienced listeners: the lack of clear transients at beat positions, more limited spectral spread of information, and, in general, that dance movements and foot-tapping are complementary to how rhythms relate to meter in these styles [10, 32] (audible foot-tapping on beat 1 and 3 was detected by the authors only in four of the 20 stimuli). Consequently, folk musicians tapped along with asymmetric beat patterns while jazz musicians, expecting beats to be isochronous, failed in finding consistent beat patterns, which resulted in a low agreement between the jazz musicians. Furthermore, the dynamic emphasis of beats in folk musicians’ tapping to folk music were consistent with descriptions of metric beat articulations [27]. 

We found a dependency between the mutual agreement metric and tempo in our material. We conducted an additional experiment, tapping to generated clicks at different IOIs, which confirmed this dependency and provided a correction factor for our results. Hence, the standard deviation of human tapping (SD _asy_ ) introduces a bias in the computational metric, which so far had been employed for automatic beat tracking evaluation mainly. Further studies should investigate the robustness of beat tracking metrics in presence of motor noise typical for human production. 

Our study used a selection of commercial and archive music recordings, which included genre-specific differences in conventions, settings and instruments. For instance, all jazz examples featured ensemble playing while folk music examples were all played solo on violin or hardingfela. Although studies could benefit from more neutrally designed stimuli, these differences reflect standard practice in these genres and thus reflect real-world situations that these musicians are likely to face. 

## **6. CONCLUSION** 

This study employed mutual agreement metrics, ITI and accent histograms to analyse the sensorimotor synchronization of two groups of musicians when tapping to music from familiar and unfamiliar genres. We found groupand genre-specific behaviours for tapping with the main metrical level, tapping with asymmetric beat and the accentuation of beat cycles. The musicians shared the same cultural background but were specialist in either jazz or Scandinavian folk music, and our findings show a coherence with genre-specific meter conventions as a result of deep genre expertise. In addition, we identified a tempo bias in the mutual agreement metric caused by human motor noise, which motivates future studies of the validity of beat tracking metrics when applied to human tapping. 

## **7. ACKNOWLEDGMENTS** 

Andre Holzapfel was supported by the Swedish Research Council (2019-03694) and the Marianne and Marcus Wallenberg Foundation (MMW 2020.0102). 

465 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

## **8. REFERENCES** 

- [1] B. H. Repp and Y. H. Su, “Sensorimotor synchronization: A review of recent research (2006-2012),” _Psychonomic Bulletin and Review_ , vol. 20, no. 3, pp. 403– 452, 2013. 

- [2] R. Polak, N. Jacoby, T. Fischinger, D. Goldberg, A. Holzapfel, and J. London, “Rhythmic prototypes across cultures: A comparative study of tapping synchronization,” _Music Perception: An Interdisciplinary Journal_ , vol. 36, no. 1, pp. 1–23, 2018. 

- [3] C. Drake and J. B. El Heni, “Synchronizing with Music: Intercultural Differences,” _Annals of the New York Academy of Sciences_ , vol. 999, no. 1, pp. 429–437, nov 2003. 

- [4] C. J. Stevens, “Music Perception and Cognition: A Review of Recent Cross-Cultural Research,” _Topics in Cognitive Science_ , vol. 4, no. 4, pp. 653–667, oct 2012. 

- [5] S. J. Morrison and S. M. Demorest, “Cultural constraints on music perception and cognition,” in _Progress in Brain Research_ , J. Chiao, Ed. Elsevier, 2009, vol. 178, no. C, pp. 67–77. 

- [6] C. M. Yates, T. Justus, N. B. Atalay, N. Mert, and S. E. Trehub, “Effects of musical training and culture on meter perception,” _Psychology of Music_ , vol. 45, no. 2, pp. 231–245, 2017. 

- [7] B. Kalender, S. E. Trehub, and E. G. Schellenberg, “Cross-cultural differences in meter perception,” _Psychological Research_ , vol. 77, no. 2, pp. 196–203, 2013. 

- [8] N. Jacoby and J. H. McDermott, “Integer Ratio Priors on Musical Rhythm Revealed Cross-culturally by Iterated Reproduction,” _Current Biology_ , vol. 27, no. 3, pp. 359–370, 2017. 

- [9] E. E. Hannon, C. M. Vanden Bosch der Nederlanden, and P. Tichko, “Effects of perceptual experience on children’s and adults’ perception of unfamiliar rhythms,” _Annals of the New York Academy of Sciences_ , vol. 1252, no. 1, pp. 92–99, 2012. 

- [10] J.-P. Blom, “The Dancing Fiddle, On the Expression of Rhythm in Hardingfele Slåtter,” in _Norwegian folk music Series 1 Slåttar for the harding fiddle Vol. 7 Springar in 3/4 time_ , ser. Norsk folkemusikksamling. Oslo: Universitetsforlaget, 1981, vol. Serie 1 B., p. 289. 

- [11] S. Ahlbäck, “Metrisk analys - en metod att beskriva skillnaden mellan låttyper,” _Norsk folkemusikklags skrifter_ , no. 4, 1989. 

- [12] J. Pressing, “Black Atlantic Rhythm: Its Computational and Transcultural Foundations,” _Music Perception_ , vol. 19, no. 3, pp. 285–310, 2002. 

- [13] B. H. Repp, “Sensorimotor synchronization: A review of the tapping literature,” _Psychonomic Bulletin & Review_ , vol. 12, no. 6, pp. 969–992, 2005. 

- [14] M. Hund-Georgiadis and D. Yves Von Cramon, “Motor-learning-related changes in piano players and non-musicians revealed by functional magneticresonance signals,” _Experimental Brain Research_ , vol. 125, no. 4, pp. 417–425, 1999. 

- [15] S. Fujii, M. Hirashima, K. Kudo, T. Ohtsuki, Y. Nakamura, and S. Oda, “Synchronization error of drum kit playing with a metronome at different tempi by professional drummers,” _Music Perception: An Interdisciplinary Journal_ , vol. 28, no. 5, pp. 491–503, 2011. 

- [16] C. Palmer and C. L. Krumhansl, “Mental Representations for Musical Meter,” _Journal of experimental psychology. Human perception and performance_ , vol. 16, no. 4, pp. 728–741, 1990. 

- [17] J. London, R. Polak, and N. Jacoby, “Rhythm histograms and musical meter: A corpus study of Malian percussion music,” _Psychonomic Bulletin and Review_ , vol. 24, no. 2, pp. 474–480, 2017. 

- [18] R. Polak, “Rhythmic Feel as Meter: Non-Isochronous Beat Subdivision in Jembe Music from Mali,” _Music Theory Online_ , vol. 16, no. 4, pp. 1–26, 2010. 

- [19] A. Holzapfel, “Relation Between Surface Rhythm and Rhythmic Modes in Turkish Makam Music,” _Journal of New Music Research_ , vol. 44, no. 1, pp. 25–38, 2015. 

- [20] E. E. Hannon, G. Soley, and S. Ullal, “Familiarity overrides complexity in rhythm perception: A crosscultural comparison of American and Turkish listeners,” _Journal of Experimental Psychology: Human Perception and Performance_ , vol. 38, no. 3, pp. 543–548, 2012. 

- [21] P. Desain and H. Honing, “The formation of rhythmic categories and metric priming,” _Perception_ , vol. 32, no. 3, pp. 341–365, 2003. 

- [22] E. E. Hannon, G. Soley, and R. S. Levine, “Constraints on infants’ musical rhythm perception: effects of interval ratio complexity and enculturation,” _Developmental Science_ , vol. 14, no. 4, pp. 865–872, 2011. 

- [23] B. van der Weij, M. T. Pearce, and H. Honing, “A probabilistic model of meter perception: Simulating enculturation,” _Frontiers in Psychology_ , vol. 8, no. MAY, pp. 1–18, 2017. 

- [24] I. Bengtsson, “On notation of time, signature and rhythm in Swedish polskas,” _Studia instrumentorum musicae popularis III._ , pp. 22–31, 1974. 

- [25] T. Kvifte, “Categories and timing: On the perception of meter,” _Ethnomusicology_ , vol. 51, no. 1, pp. 64–84, 2007. 

466 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

- [26] M. Nilsson, “The swedish polska,” _Stockholm: Svenskt visarkiv/Musikverket_ , 2017. 

- [27] S. Ahlbäck, “About Asymmetrical Beat in the Polska,” in _The Polish Dance in Scandinavia and Poland_ , M. Ramsten, Ed. Stockholm: Svenskt visarkiv, 2003, p. 165–80. 

- [28] M. Johansson, “Rhythm into style: studying asymmetrical grooves in Norwegian folk music,” Ph.D. dissertation, University of Oslo, 2009. 

- [29] E. Groven, “Musikkstudiar-ikkje utgjevne før. 1. Rytmestudiar,” _Heiderskrift til Eivind Groven._ , pp. 93– 102, 1971. 

- [30] T. Kvifte, “Fenomenet ’asymetrisk’ takt i norsk og svensk folkemusikk.” _Studia Musicologica Norvegica_ , no. 25, pp. 387–430, 1999. 

- [31] M. R. Haugen, “Investigating Periodic Body Motions as a Tacit Reference Structure in Norwegian Telespringar Performance,” _Empirical Musicology Review_ , vol. 11, no. 3-4, p. 295, 2017. 

- [32] O. Misgeld and A. Holzapfel, “Towards the study of embodied meter in Swedish folk dance,” in _Folk Music Analysis workshop_ , no. Mid, 2018, p. 6. 

- [33] P. F. Berliner, _Thinking in jazz: The Infinite Art of Improvisation_ . The University of Chicago Press, 1994. 

- [34] P. Vuust, E. Brattico, M. Seppänen, R. Näätänen, and M. Tervaniemi, “Practiced musical style shapes auditory skills,” _Annals of the New York Academy of Sciences_ , vol. 1252, no. 1, pp. 139–146, 2012. 

- [35] A. Holzapfel, M. E. Davies, J. R. Zapata, J. L. Oliveira, and F. Gouyon, “Selective sampling for beat tracking evaluation,” _IEEE Transactions on Audio, Speech and Language Processing_ , vol. 20, no. 9, pp. 2539–2548, 2012. 

- [36] O. Cornelis, J. Six, A. Holzapfel, and M. Leman, “Evaluation and recommendation of pulse and tempo annotation in ethnic music,” _Journal for New Music Research_ , vol. 42, no. 2, pp. 131–149, 2013. 

- [37] M. E. P. Davies, N. Degara, and M. D. Plumbley, “Evaluation methods for musical audio beat tracking algorithms,” Queen Mary University of London, Centre for Digital Music, Tech. Rep. C4DM-TR-09-06, 2009. [Online]. Available: http://www.elec.qmul.ac.uk/people/markp/2009/ DaviesDegaraPlumbley09-evaluation-tr.pdf 

- [38] N. Jacoby and J. H. McDermott, “Integer ratio priors on musical rhythm revealed cross-culturally by iterated reproduction,” _Current Biology_ , vol. 27, no. 3, pp. 359– 370, 2017. 

467 

