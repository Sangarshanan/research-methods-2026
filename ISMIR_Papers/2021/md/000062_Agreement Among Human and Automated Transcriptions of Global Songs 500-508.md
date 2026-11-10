---
paper_id: "000062"
year: 2021
title: "Agreement Among Human and Automated Transcriptions of Global Songs 500-508"
source_url: "https://archives.ismir.net/ismir2021/paper/000062.pdf"
---

# **AGREEMENT AMONG HUMAN AND AUTOMATED TRANSCRIPTIONS OF GLOBAL SONGS** 

**Yuto Ozaki**<sup>**1**</sup> **, John McBride**<sup>**2**</sup> **, Emmanouil Benetos**<sup>**3**</sup> **, Peter Q. Pfordresher**<sup>**4**</sup> **, Joren Six**<sup>**5**</sup> **, Adam T. Tierney**<sup>**6**</sup> **, Polina Proutskova**<sup>**3**</sup> **, Emi Sakai**<sup>**7**</sup> **, Haruka Kondo**<sup>**1**</sup> **, Haruno Fukatsu**<sup>**1**</sup> **,** 

**Shinya Fujii**<sup>**1**</sup> **, Patrick E. Savage**<sup>**1***</sup> 

1Keio University, Fujisawa, Japan 

2Center for Soft and Living Matter, Institute for Basic Science, South Korea 

3Queen Mary University of London, UK 

4University at Buffalo, NY, USA 

5Ghent University, Belgium 

6Birkbeck, University of London, UK 

7No affiliation 

```
*psavage@sfc.keio.ac.jp
```

## **ABSTRACT** 

Cross-cultural musical analysis requires standardized symbolic representation of sounds such as score notation. However, transcription into notation is usually conducted manually by ear, which is time-consuming and subjective. Our aim is to evaluate the reliability of existing methods for transcribing songs from diverse societies. We had 3 experts independently transcribe a sample of 32 excerpts of traditional monophonic songs from around the world (half a cappella, half with instrumental accompaniment). 16 songs also had pre-existing transcriptions created by 3 different experts. We compared these human transcriptions against one another and against 10 automatic music transcription algorithms. We found that human transcriptions can be sufficiently reliable (~90% agreement, κ ~.7), but current automated methods are not (<60% agreement, κ <.4). No automated method clearly outperformed others, in contrast to our predictions. These results suggest that improving automated methods for cross-cultural music transcription is critical for diversifying MIR. 

## **1. INTRODUCTION** 

Cross-cultural analysis is essential to explore diversity and universality of music [1-2]. Such analyses require symbolic representations of sounds such as score notation. However, transcription into notation is usually conducted by ear, which is time-consuming and subjective [3-4]. 

Automated methods of music transcription and melody extraction might potentially solve these problems [5-7]. However, automated extraction of fundamental frequency (F0) alone is not sufficient. Instead, a continuous fundamental frequency must be segmented into discrete notes 

© Yuto Ozaki, John McBride, Emmanouil Benetos, Peter Q. Pfordresher, Joren Six, Adam T. Tierney, Polina Proutskova, Emi Sakai, Haruka Kondo, Haruno Fukatsu, Shinya Fujii, Patrick E. Savage. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). **Attribution:** Yuto Ozaki, John McBride, Emmanouil Benetos, Peter Q. Pfordresher, Joren Six, Adam T. Tierney, Polina Proutskova, Emi Sakai, Haruka Kondo, Haruno Fukatsu, Shinya Fujii, Patrick E. Savage. “Agreement among human and automated transcriptions of global songs”, in _Proc. of the 22_<sup>_nd_</sup> _Int. Society for Music Information Retrieval Conf._ , Online, 2021. 

with the categorical pitches and rhythms that are distinctive features of almost all the world’s music [8]. This challenge is particularly important for variable pitch instruments such as the voice (the most universal instrument [89]). However, to our knowledge, agreement among human and automated transcription has not been objectively quantified using cross-cultural samples or multiple human transcribers. 

The main objective of this paper is to evaluate the degree of agreement among human and automated transcriptions for a global song sample. We demonstrate that the degree of agreement between human transcriptions is substantially higher than the agreement between humans and machines. Our evaluation also reveals that no single algorithm outperforms the others, and there are no clear differences between signal-processing-based methods and datadriven methods. 

## **2. RELATED WORK** 

## **2.1 Subjectivity of manual transcription** 

Manual transcription is central to musicological research, but to our knowledge, agreement among different human transcriptions of the same songs has never been objectively measured. Even qualitative evaluation is rare. A notable exception was a 1963 symposium on transcription where four leading ethnomusicologists independently transcribed a single recording (“A Hukwe* song with musical bow”), resulting in “four rather different transcriptions” [1, 4]. In contrast, List compared transcriptions of three songs (“Rumanian carol”, “Yiddish lullaby”, “Thai lullaby”) by between 2-9 transcribers and concluded that “transcriptions made by ear in notated form are sufficiently accurate, sufficiently reliable to provide a valid basis for analysis” [3]. More recently, Mehr et al. [9] combined transcriptions by 3 experts of 118 diverse traditional songs into a single set of “consensus” transcriptions, and had 10 experts rate their accuracy on a subjective scale from 1 (“Terrible”) to 8 (“Perfect”), finding a median rating of 6 (“Very accurate”). Yet none of these studies provided an objective measurement of the degree of agreement between individual transcribers. 

500 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 



<!-- Start of picture text -->
Solo singing with instruments Global Jukebox<br>Accompaniment Source<br>Solo singing without instruments Natural History of Song<br><!-- End of picture text -->

**Figure 1.** Map of the 32 songs transcribed and analyzed. 

## **2.2 Reliability of automated transcription** 

Automatic transcription reliability has been evaluated extensively for piano music and some other genres of Western music, but rarely for non-Western music. Ycart et al. [10] evaluated the performance of four automated transcription systems against perceptual ratings from 186 participants over 153 examples of piano music taken from the MAPS dataset of MIDI-aligned piano recordings [11]. They found an average Fleiss’ Kappa coefficient of 0.59, or “borderline between moderate and substantial agreement” on participant ratings. Holzapfel and Benetos asked 16 musicologists from 3 European universities to transcribe 8 excerpts of sousta, a traditional Greek in-strumental dance genre, either from scratch or starting from an automatic transcription, finding “no quantitative advantage of using [automatic music transcription]” [12]. Although computer-assisted transcription studies exist [13], recent reviews by musicologists argued that computational tools for musical analysis are either useful for only low-level analysis or not widely adopted within mainstream musicology [14-15]. Overall, there is a clear need for objective measurements of agreement among automated and human transcriptions for a cross-cultural sample of songs. 

## **3. METHODS AND DATASET** 

## **3.1 Audio data** 

To examine the degree of agreement among human and automated transcriptions of diverse songs, we collected a sample of 14-second excerpts from 32 traditional songs evenly distributed across 8 geographic regions (Fig. 1). 16 songs were sampled from the publicly available 14-second excerpts of the Natural History of Song (NHS) Discography dataset [9] and manually extracted 14-second excerpts of the Global Jukebox audio files [16], respectively. We choose these datasets since they cover traditional songs from a global sample of societies. Sampling is randomly conducted using the following criteria: 

- l Songs are sampled equally from each of the eight regions previously used by NHS for their sampling 

(i.e. 4 songs per region from North America, Oceania, etc.). 

- l To assess capabilities of extracting vocal melodies from instrumental accompaniment, songs are sampled to consist of half solo singing without instruments and half solo singing with instruments. 

One exception is that the NHS dataset contains no audio recordings of solo singing with instruments in the Middle East region, so two solo singing excerpts without instrument examples were chosen from this region instead. We deliberately let sampled audio recordings contain various degrees of noise, reflecting the real-world challenges of analyzing traditional recordings. We did not include songs with polyphonic singing since polyphonic transcription is substantially more challenging for both humans and automated methods [5], and is beyond the scope of this study. 

## **3.2 Automated methods** 

We selected 10 automatic music transcription/vocal melody extraction/pitch detection methods. We first choose methods listed in [10] as a baseline. However, that study focused on the systems designed for piano music, so we add methods designed for extracting pitch from human vocals. Considering the difference in the approach of the pitch estimation, our selection consists of automated methods from non-data-driven models and data-driven models. If the model employs a machine learning method (such as artificial neural networks) to learn model parameters from data in a training step, we call it data-driven, otherwise non-data-driven. Table 1 summarizes the selected automated methods. Regarding pYIN [17], we used the TONY [18] software to obtain its F0 estimation. Recently, several symbolic-level automatic transcription methods have been developed [19-21]. However, some models were evaluated with only MIDI synthesized sounds and were not specifically designed for singing voice, so we did not select those methods. 

## **3.3 Transcription process** 

501 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

Twelve-tone equal temperament (12-TET) with A4 = 440 Hz is used to transcribe audio into staff notation by humans. Equal temperament is also applied to automated methods to standardize their outputs. As explained in the introduction, it is essential to obtain symbolic representations of pitch contours to analyze acoustic stimuli as melody. However, 12-TET is not completely appropriate since the pitch quantized into 12-TET does not always correspond to the actual scales/modes and perceptual tonal models even for Western singing, let alone non-Western [30-31]. 

|**Method**|**Target sound**|**Unit**|**Category**|
|---|---|---|---|
|pYIN [17]|Monophonic vocal|Frame|Non data-|
|TONY [18]|Monophonic vocal|Note|driven: pa-<br>rameters|
|Melodia [22]|Vocal melody|Frame|specified<br> <br>|
|STF [23]|Multiple 12-tone ET|Frame|manually<br>|
|CREPE [24]|Monophonic vocal|Frame||
|SPICE [25]|Monophonic vocal|Frame|Data-<br>driven: pa-<br>|
|SS-nPNN [26]|Vocal melody|Frame|rameters<br>otimized<br>|
|AD-NNMF [27]|Multiple piano sound|Note|p<br>by training|
|OAF [28]|Multiple piano sound|Note|with da-<br>tasets.|
|madmom [29]|Multiple piano sound|Note||



**Table 1.** Summary of the selected automated methods. Unit indicates if the F0 estimation is frame-level or notelevel [5] that the latter predicts onset and offset timing. 

While binning continuous F0 into a simplified discrete set of 12 100-cent intervals loses information about microtonal nuance, 100 cents (1 semitone) is both the most commonly used system and roughly corresponds to general levels of variability in singing intonation (imprecision and inaccuracy) [31-32], making it a reasonable choice to use to evaluate accuracy. It's also what was used by Mehr et al. [9] when creating the dataset we use, enabling us to compare our results with theirs. In summary, we decide to take advantage of the convenience and comparability of 12TET, while acknowledging that it does not capture all musical nuances. 

This study focuses on the evaluation of agreement among melodies, and we discard temporal/rhythmic information so we only extract pitch from transcriptions to create a sequence of notes. However, regarding the notes representing unison melodic intervals (i.e. repeated notes), we create two transcription patterns. This is because not all selected automated methods can perform note segmentation. The change in pitch class can be used to segment two notes in the case of the other intervals, but the determining 

boundary between the notes of the same pitch class would require a note segmentation algorithm. Firstly, the raw note sequences are created as a note sequence which includes the unison interval. Based on this version, we also create a note sequence which discards repeated notes and treats the notes of the unison interval as a tied single note (i.e. “CCFGGC” becomes “CFGC”). We call this version “non-unison”. This treatment enables us to evaluate how much the pitch estimation itself, which is a baseline function of automatic transcription, determines performance. In addition, 12-TET has enharmonic equivalent pitch classes, so we only use flat notes for the same sounding sharp and flat notes. 

## _3.3.1 Transcription by humans_ 

We asked three Japanese experts with professional training in Western classical music to independently transcribe the 32 recordings. One of them has professional experience of transcribing non-Western music using Western staff notation. None of them had seen the transcriptions contained in the NHS dataset. They were instructed to use MuseScore3 [33] as a tool to create transcriptions. Following Mehr et al. [9]<sup>1</sup> , we also created a consensus version of our 3 new human transcriptions. Importantly, however, while Mehr et al. only analyzed and published their consensus transcription, we include the three independent transcriptions as well as their combined consensus version to allow us to measure agreement between individual human transcribers. Our three coauthors who undertook transcription were blinded from our hypothesis testing and were asked to create transcriptions prior to discussions about coauthorship. 

## _3.3.2 Transcription by automated methods_ 

In order to standardize the output of each method, we apply post-processing steps including manual work, such as the quantization of frequency, smoothing of pitch contour, or the selection of melody contour by the Viterbi algorithm with manually specifying frequency range of melody for the case of multi-pitch estimation methods (cf. supplementary materials for details). Note that songs used in the evaluation contain solo singing with instrumental accompaniment but chosen methods are not designed to estimate the F0 of those styles of singing except for Melodia and SSnPNN. Therefore the automated methods other than Melodia and SS-nPNN may include the pitch estimation of instrumental sounds, which is excluded from human transcriptions. 

## **3.4 Sequence alignment and evaluation metrics** 

We use the Needleman-Wunsch algorithm [34] to align note sequences (cf. supplementary materials for further details). Agreement between two string sequences can be quantified in various ways. We mainly use Fleiss' Kappa inter-rater reliability coefficient (κ), which measures how much the observed agreement exceeds chance [35]. However, κ does not provide other relevant information such as how many notes actually differ among note sequences or whether differences are due to disagreement about note 

> 1 Mehr et al.’s full consensus transcriptions are published at 

<u>https://osf.io/jh7t5/</u> 

502 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 



<!-- Start of picture text -->
b-1) Human transcription (x3 transcribers + Consensus + NHS) c) Note sequences (4.5* human, 10 automated)<br>Human A<br>-gEEddAAdEdBd--edB 1) Human A<br>Human B -gEEddAAdDdBdd-DdB 2) Human B<br>a) Spectrogram of audio recording Human C gEEddAAdEdbd--EdB 3) Human C<br>Consensus -gEEddAAdEdBd--edB 4) Consensus of A-C<br>NHS -gEEddAAdEdbd--edB 4.5*) NHS consensus [9]<br>0.2 b-2) Machine transcription: F0 contour - Post-processing (x10 methods)<br>0.15 Time (s) -FeEd-abdeCbd--edB 1) TONY<br>TONY<br>6田 E-eEd-a-deCbd--edB 8) CREPE<br>---Ed---dedbdddDdB 9) SS-nPNN<br>0.15 -FeEd-abdeCbD--ddB 10) Melodia<br><!-- End of picture text -->

**Figure 2.** Overview of the agreement evaluation using an example 8-second excerpt from NAIV-075 (Healing song, Kwakwaka'wakw people, 00:06-00:14 from <u>https://osf.io/y29wp). Red indicates disagreement with our new consensus</u> transcription (#4, made by combining the three individual transcriptions #1-3).  For visibility, only the automated transcription produced by TONY is shown, and octave information is omitted from the note sequences. The degree of human-human and human-machine agreement is calculated based on the note sequences (c). For example, #4.5 (NHS consensus) is 95% identical to our consensus #4 (14 out of 15 notes each), while TONY is only 48% identical (7 identical notes out of average note length of 14.5), corresponding to Fleiss’ Kappa values of .94 and .34, respectively. *NB: NHS consensus transcriptions were not available for the 16 songs from the Global Jukebox sample. 

pitch (i.e., substitution) or note segmentation (i.e., insertion/deletion). We also report such quantities by using percent identity (PID) [36-37] (cf. Fig. 2 for an example and for Supplementary Material for detailed explanation and additional analyses using Levenshtein distances). Although our approach did not utilize the real time information of note events, we confirmed it can still make meaningful alignment of notes as in the previous study [37] from the pilot experiment. Meanwhile, we also admit there is the technical difficulty of the extraction of note event timing (i.e. segmentation of sounds). Importantly, our work differs from the related studies evaluating the agreement between human and automated methods' melody annotation [38-39] in aiming symbolic-level note comparison rather than frame-level F0 comparison. In addition, previous studies only reported individual metrics (e.g. either distance-like metrics or inter-rater reliability, but not both), while our study explored agreement of symbolic-level melody using multiple metrics. 

We pre-registered<sup>2</sup> the following two primary hypotheses and 10 corresponding predictions based on pilot analysis of 4 songs not included in our main analyses: 

**H1: Human transcriptions are sufficiently reliable.** This predicts a Fleiss’ Kappa coefficient significantly greater than 0 when comparing our consensus transcription against the consensus transcriptions of Mehr et al. [9]. Note sequences including unison intervals are used. 

## **H2: TONY is the most reliable method of automated** 

**singing transcription.** We predicted this because unlike other methods TONY was designed to perform note segmentation for human vocal melody, better matching human standards for transcription. This predicts that Fleiss’ Kappa comparing TONY with our consensus note sequences will be significantly greater than for the other 9 algorithms when evaluated against the note sequences including unison intervals. 

## **3.5 Transposition** 

We applied transposition in the note sequence alignment process to exclude the effect of disagreement by the discrepancy of the key when calculating κ, PID and Levenshtein distance. The transposition interval was searched from -2 semitones to +2 semitones. For humanhuman transcription comparison, the transposition was performed to maximize PID. Regarding the human-machine transcription comparison, the transposition interval was searched to maximize the average PID of all 10 human-machine pairs for each song and each human transcriber. 

## **4. HYPOTHESES** 

## **5. RESULTS** 

## **5.1 Q1. To what degree do humans’ transcriptions agree?** 

The left-hand side of Figure 3 shows inter-rater reliability and percent identity results comparing human transcribers. As predicted, there was significant agreement between our new consensus transcriptions and the pre-existing NHS consensus transcriptions (median κ = .74, p < .001; median PID = 88%). When we compare the results using individual transcriptions rather than consensus transcriptions, we see that agreement is slightly lower but still relatively high (lowest median κ of .64 and PID 83% for Transcribers A & B).  The left-most two boxes show that individual vs. consensus yields higher agreement than individual vs. individual combinations (e.g. A-Cons, A-B, A-C) for all 

2 <u>https://osf.io/bjemd</u> 

503 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 



<!-- Start of picture text -->
Human vs. Human Human vs. Automated methods<br>Pairwise Our consensusvs. Natural History of SongVS. Natural History of SongOur consensus vs. vs. Our consensus<br>0.5* 0.46 0.50 0.54 0.52 0.56 0.62 0.61 0.73*A 0.99^<br>1.0-<br>Flei s ' Kappa0.5-<br>-0.5-<br>-1.0-<br>A-B A-C B-C A-ConsB-ConsC-Cons A-NHSB-NHSC-NHS Cons-NHS TONYSS-nPNNmadmomOAF MelodiapYIN CREPE STF SPICEAD-NNMF<br>Pairwise Our consensusvS. Natural History of SongVS. Natural History of SongOur consensus vs. vs. Our consensus<br>100-<br>75-<br>50- 而<br>Percent iden t iy 25<br>.<br>0-<br>A-B A-C B-C A-ConsB-ConsC-Cons A-NHSB-NHSC-NHS Cons-NHS TONYSS-nPNNmadmomOAF Melodia pYIN CREPE STF SPICEAD-NNMF<br>Accompaniment Solo singing with instrumentsSolo singing without instruments<br><!-- End of picture text -->

**Figure 3.** Agreement among human-human and human-machine transcribed note sequences. “A”, “B”, and “C” represent the three individual transcribers. The dashed line at κ = 0 and 8.3% identity indicates chance levels of agreement. The numbers appearing above the violin plots indicate effect sizes for our 10 pre-registered predictions, and * and ^ indicate significant p-value and posterior probability, respectively (cf. text for details). Black circles indicate medians, and bars represent 95% confidence intervals of the median [40]. Results using alternative transcription methods, and full p-value and posterior probabilities are available in the supplementary material (figure S3-S7 and table S2-S3). 

transcribers. This means that consensus is indeed reflecting the elements of those three transcribers' transcriptions rather than the particular pairs. These results suggest that transcription of pitch contour could be reliable even for non-Western music. 

We also analyze some low agreement results. There are 25 pairwise κ values lower than 0.4, all of which involved 7 songs (NAIV-033, NAIV-100, NAIV-117, T5431R27, T5482R03, NAIV-015 and NAIV-048). In particular, NAIV-033 (Maya healing song) is a near-monotone chant, and so the degree of agreement by chance is so large that it negates the proportion of agreement. As the unison interval dominates, the note sequences of this song are highly homogeneous (PID > 0.9 for all 6 pairs). Other than this song, the remaining disagreement is mainly caused by disagreement of the pitch rather than segmentation. (cf. supplementary material table S1). In other words, transcribers generally captured the same note events, but the assigned pitch sometimes differs by 1-2 semitones. 

Incidentally, we observed that using raw note sequences yielded the median of κ very close to zero (κ = -0.019) due to cases where the tonal center differed by a semitone (and sometimes a whole tone, cf. supplementary material figure S1-S2 for a sample figure and the results). Therefore, our evaluation actually focused on whether relative pitch, or the shape of the pitch contour, matches between transcribers. 

## **5.2 Q2. Which automated method agrees best with transcription of non-Western music by humans?** 

The right-hand side of Figure 3 shows κ and PID obtained by comparing the machine note sequences and our consensus version's note sequences. Contrary to our prediction, there is no evidence for the superiority of TONY except when compared with AD-NNMF and SPICE. The figure also indicates generally low reliability of automated transcription methods (median κ values are all below 0.4). In particular, SPICE and AD-NNMF both had median κ below 0, suggesting they performed worse than chance. Especially, AD-NNMF failed to pick up notes correctly in many cases and indeed, sometimes the length of note sequence of AD-NNMF is zero (cf. supplementary material figure S8-S9). In such cases, the proportion of agreement between human note sequences also becomes around zero, but chance agreement probability is still positive by its definition, resulting in many negative Kappa values. 

In addition, SPICE and CREPE had difficulty estimating F0 of the particular tracks of monophonic singing, which is apparent from the drop in the plot of note sequence length (cf. supplementary material figure S8-S9). As predicted, κ of automated methods designed for monophonic vocal melody (i.e. TONY, pYIN, CREPE and SPICE) show a relatively large difference dependent on instrumental accompaniment compared to the other methods, 

504 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

but STF also suffered from instrumental sounds. (cf. Figure 3 and supplementary material figure S10). 

See supplementary material for additional analysis details including results of measuring agreement with Levenshtein distances (which were generally similar to results found using PID). 

## **6. DISCUSSION AND FUTURE WORK** 

Overall, we observed that the degree of agreement of transcriptions of diverse traditional songs among human transcribers was relatively high (~90% agreement, κ ~0.7; Fig. 3), while the degree of agreement between human and automated methods was relatively low (< 60% agreement, κ <.4; Fig. 3). Automated methods where less than 60% of estimated notes agree with human judgments are unlikely to produce satisfactory results for the kinds of tasks we hope to use them for, such as cross-cultural comparison of scale and interval systems [41-42]. Landis and Koch [43] suggested that κ of .61-.8 be considered "substantial" agreement .21-0.4 as "fair" agreement, but some have suggested that less than .4 is unacceptably low [44]. Our qualitative examination of the transcriptions (e.g., Fig. 2) supports the interpretation that human transcriptions of diverse traditional songs can be sufficiently reliable, but current state-of-the-art automated methods are not. However, high agreement does not necessarily equate to high quality. The quality of transcription may depend on its goal [4546], so future research should expand on our results to evaluate transcriptions for specific applications (e.g., tonal analysis [41-42]). 

Different combinations of human transcribers and songs had varying levels of agreement, but overall the agreement among three female Japanese experts and the consensus transcription by three white American male experts was surprisingly high, with more differences appearing between individuals than between the two groups. Of course, by definition the experts had been trained in Western music and transcription methods - future studies should explore perceptual variability among listeners with varying degrees of training in different musical systems [47]. 

Disagreement among humans appeared to primarily involve assignment of pitch to different pitch classes. In contrast, disagreement in automated methods appeared to primarily reflect segmentation, rather than F0 estimation. Future studies might be able to clarify this point by collecting both F0 annotations and score transcriptions by humans. This might also allow us to compare our results with more conventional metrics used in research on pitch estimation algorithms such as frame-wise and note-wise F0 agreement and the use of true positive and false positive scores [10] (though we emphasize that our work brings into question the idea that a single 'ground-truth' annotation might even exist that all can agree on for diverse songs). [48] developed a method for evaluating the degree of agreement of F0-estimates among multiple automated methods, and such a method would be especially advantageous to assess the overall reliability of automated methods against global songs once F0 annotation is collected. 

We were surprised that all automated methods performed so poorly even for the relatively simple task of transcribing only pitch sequences for monophonic songs. 

Some might argue it is unfair to evaluate MIR methods designed primarily for F0 transcription of Western instrumental music using symbolic notation transcriptions of (mostly) non-Western songs. Our feelings are somewhat opposite - it is unfair and unethical to limit MIR to a narrow slice of the world’s music [49]. Since our goal was to evaluate the ability of existing MIR algorithms to transcribe global songs using symbolic notation, we believe it is fair and necessary to evaluate state of the art algorithms even though - in fact especially because - they were not designed for this application. Our results thus confirm the strong need for automatic music transcription and other MIR tasks to expand algorithms and datasets beyond the traditional focus on Western classical and popular music to be suitable for more diverse musical styles [49]. Moving from a reliance on convenient but restricted datasets (e.g., the MAPS dataset of MIDI-aligned piano recordings commonly used to evaluate automatic transcription [11]) to cross-cultural datasets like the one presented here and elsewhere [9, 16, 50] will be essential for diversifying MIR. 

The formalization of a general algorithm that agrees with human pitch recognition and note segmentation is an ongoing challenge related to a central issue in MIR: the “correctness” of the algorithm depends on the degree of perceptual variability in the human ground-truth data [51]. Thus, accounting for diversity and subjectivity in human transcriptions is equally critical to advance research on the automatic analysis of music. For example, while we found relatively high agreement among expert transcribers using Western 12-TET notation, we do not know whether the singers whose songs we transcribed would agree with our transcriptions, or whether transcription using a different notation system (e.g., Middle Eastern 24-note microtonal notation, ‘Are’Are 7-note equiheptatonic notation [52], Killick’s “global notation” [53], etc.) would give better or worse results. We see our current results using 12-TET - with all its known problems and cultural baggage [1-5, 4546] - as a baseline against which future studies can test whether other methods of cross-cultural transcription may be able to improve. 

Furthermore, here we solely focused on pitch, but a more comprehensive description of music necessitates other dimensions such as rhythm, timbre, and social context [54]. Other cross-cultural systems of music analysis such as Cantometrics [54-55] and CantoCore [56] have been designed to capture such features. Somewhat counterintuitively, our current results show substantially higher agreement using Western staff notation to analyze a global song sample (κ ~0.7) than was found using these crosscultural song classification systems (κ ~0.3-0.5 [8, 16, 56]). This suggests a need for MIR to better account for diversity in human ground-truth representations of all dimensions of music, not only pitch [57]. 

Musical diversity is a crucial challenge and opportunity for MIR. Quantifying diversity in human “ground-truth” cross-cultural data is an important first step for diversifying MIR. Our study demonstrates that there is still substantial room for improvement for automated methods of music transcription, and provides quantitative estimates of diversity among human transcriptions to help guide development of future MIR methods. 

505 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

## **7. AUTHOR CONTRIBUTIONS** 

Conceptualization: P.E.S, J.M, P.Q.P., J.S., A.T.T., S.F., E.B., Y.O., P.P.; Transcription: E.S., H.K., H.F.; Methodology / Analysis / Investigation / Visualization: Y.O., P.E.S., E.B., J.M.; Project administration / Supervision / Funding acquisition: P.E.S.; Writing – original draft: Y.O., P.E.S.; Writing – review & editing: J.M., E.B., P.Q.P., J.S., A.T.T., P.P., S.F. 

## **8. ACKNOWLEDGEMENTS** 

We thank Olga Velichkina and members of the Keio SFC CompMusic and NeuroMusic labs for feedback on earlier versions of this manuscript. This work was supported by Grant-in-Aid no. 19KK0064 from the Japan Society for the Promotion of Science and by startup grants from Keio University (Keio Global Research Institute, Keio Research Institute at SFC, and Keio Gijuku Academic Development Fund) to P.E.S. 

## **9. DATA/CODE AVAILABILITY** 

Audio files, transcriptions (individual and consensus), aligned note sequences, and analysis scripts are available at <u>https://github.com/comp-music-lab/agreement-humanautomated</u> (codes, transcriptions, sequence data), <u>https://doi.org/10.5281/zenodo.4941863 (audio). The PDF</u> of the supplementary material is also available at the above GitHub link. 

## **10. REFERENCES** 

- [1] B. Nettl, _The Study of Ethnomusicology: ThirtyThree Discussions, 3rd ed._ , Champaign, IL, USA: University of Illinois Press, 2015. 

- [2] P. E. Savage, and S. Brown, “Toward a new comparative musicology,” _Analytical Approaches to World Music_ , vol. 2, no. 2, pp. 148–197, 2013. 

- [3] G. List, “The reliability of transcription,” _Ethnomusicology_ , vol. 18, no. 3, pp. 353–377, 1974. 

- [4] N. M. England, R. Garfias, M. Kolinski, G. List, W. Rhodes, and C. Seeger, “Symposium on transcription and analysis: A Hukwe* song with musical bow,” _Ethnomusicology_ , vol. 8, no. 3, pp. 223–233, 1964. 

- [5] E. Benetos, S. Dixon, Z. Duan, and S. Ewert, “Automatic music transcription: An overview,” _IEEE Signal Processing Magazine_ , vol. 36, no. 1, pp. 20–30, 2019. 

- [6] M. Müller, E. Gómez, and Y. Yang, Eds., "Computational methods for melody and voice processing in music recordings (Dagstuhl seminar 19052)," _Dagstuhl Reports_ , vol. 9, no. 1, pp. 125–177, 2019. 

- [7] Z. Rafii, A. Liutkus, F. Stöter, S. I. Mimilakis, D. FitzGerald, and B. Pardo, "An overview of lead and accompaniment separation in music," _IEEE/ACM Transactions on Audio, Speech, and Language Processing_ , vol. 26, no. 8, pp. 1307-1335, 2018, doi: 10.1109/TASLP.2018.2825440. 

- [8] P. E. Savage, S. Brown, E. Sakai, and T. E. Currie, “Statistical universals reveal the structures and functions of human music,” _Proc. National Academy of Sciences USA_ , vol. 112, no. 29, pp. 8987–8992, 2015. 

- [9] S. A. Mehr et al., "Universality and diversity in human song," _Science_ , vol. 366, eaax0868, 2019, doi: 10.1126/science.aax0868. 

- [10] A. Ycart, L. Liu, E. Benetos, and M. T. Pearce, "Investigating the perceptual validity of evaluation metrics for automatic piano music transcription," _Transactions of the International Society for Music Information Retrieval_ , vol. 3, no. 1, pp. 68–81, 2020, doi: 10.5334/tismir.57. 

- [11] V. Emiya, R. Badeau, and B. David, "Multipitch estimation of piano sounds using a new probabilistic spectral smoothness principle," _IEEE Transactions on Audio, Speech, and Language Processing_ , vol. 18, no. 6, pp. 1643–1654, 2010. 

- [12] A. Holzapfel, and E. Benetos, "Automatic music transcription and ethnomusicology: A user study," in _Proc. 20th International Society for Music Information Retrieval Conference_ , Delft, The Netherlands, 2019, pp. 678-684. 

- [13] E. Gómez, and J. Bonada, "Towards computer-assisted flamenco transcription: An experimental comparison of automatic transcription algorithms as applied to a cappella singing," _Computer Music Journal_ , vol. 37, no. 2, pp. 73–90, 2013. 

- [14] S. Cottrell, "Big music data, musicology, and the study of recorded music: Three case studies," _The Musical Quarterly_ , vol. 101, no. 2-3, pp. 216-243, doi: 10.1093/musqtl/gdy013. 

- [15] L. Tilley, "Analytical ethnomusicology: How we got out of analysis and how to get back in," in _Springer Handbook of Systematic Musicology_ , R. Bader, Eds. Berlin, Germany: Springer, 2018, pp. 953–977. 

- [16] A. L. C. Wood _et al._ , “The Global Jukebox: A public database of performing arts and culture,” _PsyArXiv Preprint._ doi: org/10.31234/osf.io/4z97j. 

- [17] M. Mauch, and S. Dixon, "PYIN: A fundamental frequency estimator using probabilistic threshold distributions," in _Proc. IEEE International Conference on Acoustics, Speech and Signal Processing_ , Florence, Italy, 2014, pp. 659–663 

- [18] M. Mauch et al., “Computer-aided melody note transcription using the tony software: Accuracy and efficiency,” in _Proc. 1st International Conference on Technologies for Music Notation and Representation_ , Paris, France, 2015. 

- [19] R. Nishikimi, E. Nakamura, M. Goto, and K. Yoshii, "Audio-to-score singing transcription based on a CRNN-HSMM hybrid model," _APSIPA Transactions on Signal and Information Processing_ , vol. 10, no. e7, pp. 1-13, 2021, doi: 10.1017/ATSIP.2021.4. 

506 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

- [20] R. Gunter, C. Carvalho, and P. Smaragdis, "Towards end-to-end polyphonic music transcription: Transforming music audio directly to a score," in _IEEE Workshop on Applications of Signal Processing to Audio and Acoustics_ , New York, USA, 2017, pp. 151-155, doi: 10.1109/WASPAA.2017.8170013. 

- [21] M. A. Román, A. Pertusa, and J. Calvo-Zaragoza, "A holistic approach to polyphonic music transcription with neural networks," in _Proc. 20th International Society for Music Information Retrieval Conference_ , Delft, The Netherlands, 2019, pp. 731-737. 

- [22] J. Salamon, and E. Gomez, "Melody extraction from polyphonic music signals using pitch contour characteristics," _IEEE Transactions on Audio, Speech, and Language Processing_ , vol. 20, no. 6, pp. 1759-1770, 2012, doi: 10.1109/TASL.2012.2188515. 

- [23] L. Su, and Y. Yang, "Combining spectral and temporal representations for multipitch estimation of polyphonic music," _IEEE/ACM Transactions on Audio, Speech, and Language Processing_ , vol. 23, no. 10, pp. 1600-1612, 2015, doi: 10.1109/TASLP.2015.2442411. 

- [24] J. W. Kim, J. Salamon, P. Li, and J. P. Bello, "Crepe: A convolutional representation for pitch estimation," in _Proc. 2018 IEEE International Conference on Acoustics, Speech and Signal Processing_ , Calgary, AB, Canada, 2018, pp. 161-165, doi: 10.1109/ICASSP.2018.8461329. 

- [25] B. Gfeller, C. Frank, D. Roblek, M. Sharifi, M. Tagliasacchi, and M. Velimirović, "SPICE: Self-supervised pitch estimation," _IEEE/ACM Transactions on Audio, Speech, and Language_ , vol. 28, pp. 11181128, 2020, doi: 10.1109/TASLP.2020.2982285. 

- [26] W.-T. Lu, and L. Su, “Vocal melody extraction with semantic segmentation and audio-symbolic domain transfer learning,” in _Proc. 19th International Society for Music Information Retrieval Conference_ , Paris, France, 2018, pp. 521–528. 

- [27] T. Cheng, M. Mauch, E. Benetos, and S. Dixon, "An attack/decay model for piano transcription," in _Proc. 17th International Society for Music Information Retrieval Conference_ , New York, NY, USA, 2016, pp. 584–590. 

- [28] C. Hawthorne et al., "Onsets and Frames: Dual-objective piano transcription," in _Proc. 19th International Society for Music Information Retrieval Conference_ , Paris, France, 2018, pp. 50-57. 

- [29] S. Bock, F. Korzeniowski, J. Schluter, F. Krebs, and G. Widmer, “Madmom: A new Python audio and music signal processing library,” in _Proc. 24th ACM International Conference on Multimedia_ , Amsterdam, Netherlands, 2016. 

- [30] R. Ambrazevičius: "The perception and transcription of the scale reconsidered: Several Lithuanian cases," _The World of Music_ , vol. 47, no. 2, pp. 31-53, 2005. 

- [31] P. Q. Pfordresher, S. Brown, K. M. Meier, M. Belyk, and M. Liotti, "Imprecise singing is widespread," _The Journal of the Acoustical Society of America_ , vol. 128, no. 4, pp. 2182-2190, 2010. 

- [32] P. Larrouy-Maestri, Y. Lévêque, D. Schön, A. Giovanni, and D. Morsomme, "The evaluation of singing voice accuracy: A comparison between subjective and objective methods," _Journal of Voice_ , vol, 27, no. 2, pp. 259.e1-259.25, 2013, doi: 10.1016/j.jvoice.2012.11.003. 

- [33] MuseScore: https://musescore.org/ja (accessed Feb. 25, 2021). 

- [34] S. B. Needleman, and C. D. Wunsch, “A general method applicable to the search for similarities in the amino acid sequence of two proteins,” _Journal of Molecular Biology_ , vol. 48, no. 3, pp. 443–453, 1970. 

- [35] K. L. Gwet, _Handbook of Inter-Rater Reliability. The Definitive Guide to Measuring the Extent of Agreement Among Raters, 4th edition_ . Gaithersburg, MD, USA: Advanced Analytics, LLC., 2015. 

- [36] A. C. W. May, "Percent sequence identity: The need to be explicit," _Structure_ , vol. 12, no. 5, pp. 737–738, 2004, doi: 10.1016/j.str.2004.04.001. 

- [37] P. E. Savage, and Q. D. Atkinson: "Automatic tune family identification by musical sequence alignment," in _Proc. 16th International Society for Music Information Retrieval Conference_ , Málaga, Spain, 2015, pp. 162-168. 

- [38] J. J. Bosch, and E. Gómez, “Melody extraction in symphonic classical music: a comparative study of mutual agreement between humans and algorithms,” in _Proc. 9th Conference on Interdisciplinary Musicology_ , Berlin, Germany, 2014. 

- [39] S. Balke, J. Abeßer, J. Driedger, C. Dittmar, and M. Müller, “Towards evaluating multiple predominant melody annotations in Jazz recordings,” in _Proc. 17th International Society for Music Information Retrieval Conference_ , New York City, NY, USA, 2016, pp. 246–252. 

- [40] M. J. Campbell, and M, J. Gardner, "Calculating confidence intervals for some non-parametric analyses," _British Medical Journal_ , vol. 296, no. 6634, pp. 1454-1456, doi: 10.1136/bmj.296.6634.1454. 

- [41] J. M. McBride and T. Tlusty, “Cross-cultural data suggests musical scales evolved to maximise imperfect fifths,” _arXiv Preprint_ , 2020. arXiv:1906.06171. 

- [42] J. Kuroyanagi _et al._ , “Automatic comparison of human music, speech, and bird song suggests uniqueness of human scales,” in _Proc. 9th International Workshop on Folk Music Analysis (FMA2019)_ , Birmingham, UK, 2019, pp. 35–40. 

- [43] J. R. Landis, and G. G. Koch, “The measurement of observer agreement for categorical data,” _Biometrics_ , vol. 33, no. 1, pp. 159–174, 1977. 

507 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

- [44] J. Sim, and C. C. Wright, “The kappa statistic in reliability studies: Use, interpretation, and sample size requirements,” _Physical Therapy_ , vol. 85, no. 3, pp. 257–268, 2005. 

- [45] C. Seeger, “Prescriptive and descriptive music-writing,” _Music. Q._ , vol. 44, no. 2, pp. 184–195, 1958. 

- [46] M. Hood, _The Ethnomusicologist_ . New York: McGraw-Hill, 1971. 

- [47] N. Jacoby et al., “Universality and cross-cultural variation in mental representations of music revealed by global comparison of rhythm priors,” _PsyArXiv Preprint, 2021._ doi: 10.31234/osf.io/b879v _._ 

- [48] S. Rosenzweig, F. Scherbaum, and M. Müller, "Reliability assessment of singing voice F0-estimates using multiple algorithms," in _Proc. 2021 IEEE International Conference on Acoustics, Speech and Signal Processing_ , Ontario, Canada, 2021, pp. 261-265. 

- [49] G. Born, “Diversifying MIR: Knowledge and realworld challenges, and new interdisciplinary futures,” _Trans. Int. Soc. Music Inf. Retr._ , vol. 3, no. 1, pp. 193–204, 2020. 

- [50] P. E. Savage, “An overview of cross-cultural music corpus studies,” in _Oxford Handbook of Music and Corpus Studies_ , D. Shanahan, A. Burgoyne, and I. Quinn, Eds. Oxford University Press, in press. doi: 10.31235/osf.io/nxtbg. 

- [51] A. Flexer, and T. Grill, "The problem of limited interrater agreement in modelling music similarity," _Journal of New Music Research_ , vol. 45, no. 3, pp. 239251, 2016, doi: 10.1080/09298215.2016.1200631. 

- [52] H. Zemp, and V. Malkus, “Aspects of ’Are ’Are musical theory,” _Ethnomusicology_ , vol. 23, no. 1, pp. 5– 48, 1979. 

- [53] A. Killick, “Global notation as a tool for cross-cultural and comparative music analysis,” _Analytical Approaches to World Music_ , vol. 8, no. 2, pp. 235– 279, 2021. 

- [54] P. E. Savage, “Alan Lomax’s Cantometrics Project: A comprehensive review,” _Music & Science_ , vol. 1, pp. 1–19, 2018. 

- [55] A. Lomax, and V. Grauer, “The Cantometric coding book,” in _Folk Song Style and Culture_ , A. Lomax, Ed. Washington, DC, USA: American Association for the Advancement of Science, 1968, pp. 34–74. 

- [56] P. E. Savage, E. Merritt, T. Rzeszutek, and S. Brown, “CantoCore: A new cross-cultural song classification scheme,” _Analytical Approaches to World Music_ , vol. 2, no. 1, pp. 87–137, 2012. 

- [57] H. Daikoku, S. Ding, U. S. Sanne, E. Benetos, A. L. Wood, S. Fujii, and P. E. Savage: “Human and automated judgements of musical similarity in a global sample,” _PsyArXiv Preprint_ , 2020 _,_ doi: https://doi.org/10.31234/osf.io/76fmq. 

508 

