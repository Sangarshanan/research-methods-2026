---
paper_id: "000038"
year: 2022
title: "Download pdf"
source_url: "https://zenodo.org/record/7316660/files/000038.pdf"
---

# KDC: AN OPEN CORPUS FOR COMPUTATIONAL RESEARCH OF DASTG AHI<sup>¯</sup> MUSIC 

Babak Nikzat 

Kunstuniversität Graz 

b.nikzat@kug.ac.at 

## Rafael Caro Repetto Kunstuniversität Graz 

rafael.caro-repetto@kug.ac.at 

### ABSTRACT 

Iranian dastgÅahi music is considered as the classical repertory of contemporary Iran. In the 19th century, the melodic modes that developed during its long history were grouped in categories, each of them known as dastgÅah. The dastgÅahi system presents unique features, that have been object of musicological study since its inception. However, computational methods for its research are still scarce, due in good part to the lack of open, well curated corpora. The aim of the KUG DastgÅahi Corpus (KDC) is to contribute to the development of computational corpus driven research for this tradition. KDC is created following the FAIR principles, and in close collaboration with performers and scholars, who contribute to it with annotations and qualitative evaluations. Besides presenting the first version of KDC, in this paper we explore the possibilities that Iranian dastgÅahi music offers to computational research. In order to test the performance of state-of-the-art technologies applied to this music tradition, we present preliminary results for several analytical tasks, and discuss their opportunities and limitations learnt in the process. 

### 1. INTRODUCTION 

The potential of computational methods for supporting musicological research tasks is increasingly being recognized and adopted by musicologists. Due to the high degree of specialization required both from the technical and musicological sides of this kind of research, collaboration between specialists from both disciplines is one of the most fruitful approaches for computational musicology. Developed at the Institute for Ethnomusicology of the Kunstuniversität Graz (KUG), the KUG DastgÅahi Corpus (KDC) aims to offer a growing collection of well curated and annotated data of Iranian dastgÅahi music around which engineers, musicologists and researchers from other disciplines interested in this music tradition can collaborate. In this first section we describe the main features of the dastgÅahi musical system and offer an overview of the state-of-theart of its computational research. Then, we introduce and describe in detail the first version of KDC. In section 3 we 

© B. Nikzat, and R. Caro Repetto. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: B. Nikzat, and R. Caro Repetto, ªKDC: An Open Corpus for Computational Research of DastgÅahi Musicº, in Proc. of the 23rd Int. Society for Music Information Retrieval Conf., Bengaluru, India, 2022. 

discuss the potential of Iranian dastgÅahi music for computational research. In the following sections, preliminary analyses carried out to test such potential are presented and discussed. The paper closes with our plan for expanding KDC and future work. 

### 1.1 Iranian dastg¯ahi music 

Iranian dastgÅahi music is modal. The basic modal entities in this tradition are known as gušes and they are defined by a model melody built on a specific intervallic structure, a series of characteristic melodic patterns, and a modal centre known as šÅahed [1]. Related gušes are grouped in specific collections, and in a specific order. These collections are known either as dastgÅah or ÅavÅaz, each of them with its own specific name. A dastgÅah is larger than an ÅavÅaz in terms of number of gušes, and an ÅavÅaz is considered to be a subcategory of a specific dastgÅah. Nowadays, the canonical repertoire consists of 7 dastgÅahs and 5 ÅavÅazes (see Table 1). For simplicity, in this paper we are using dastgÅah to refer to both of them collectively. The gušes in a particular dastgÅah are organized in a fixed order, and even though the performance of a dastgÅah does not required all its gušes to be performed, the order has to be maintained. The first guše in all dastgÅahs is called darÅamad, and it has a very significant meaning since it introduces the dastgÅah. Most performances start and end with darÅamad. 

Along the history of Iranian dastgÅahi music, great masters (ostÅads) of this tradition defined their own canonical repertory of the 7 dastgÅahs and 5 ÅavÅazes, fixing the number of gušes in each of them, their particular order, their specific melodic contour and their rhythmic rendition. These canonical repertoires are known as radif s, always associated with their corresponding ostÅad. These fixed radif s are nowadays only used for learning the tradition. Contemporary musicians perform their own interpretation of the repertory, but through the rules they experientially extracted from the radif they learnt. As a more encompassing concept, different performance schools are recognized, each of them with idiosyncratic performance styles. The most extended ones today are Tabriz, Tehran and Isfahan. 

Iranian dastgÅahi music uses a microtonal tuning system, resulting in specific intervallic structures defined for each guše. Three basic interval categories are considered, namely tone, semitone and an intermediate one between the previous two, whose specific width is not fixed but flexible [1], depending on guše or even performer, and that is the result of altering one natural tone less than a semitone 

321 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

up (sori) or down (koron). These intervallic structures form specific scales, in which particular tones receive predominant roles, such as šÅahed and ist, which are fundamental for defining the modal features of a guše. 

Specific techniques for vocal and instrumental performance, including an extensive repertory of ornamentation, is another essential aspect of this music, showing a great diversity depending on school, instrument, and personal style. The most common instrumental ornaments include: ešÅareh, tekiyeh, qalt, dorrÅab, riz, and šalÅal. Tahrir is the most significant singing ornament, which requires a specific technique in which the singer switches between chest and head voice (see Fig. 5). 

Gušes can be performed in free rhythm or using rhythmic cycles. Even though this is fixed per each guše in the radif s, it is decided by each musician in contemporary performance. When a guše is sung in free rhythm, the prosodic rules, known as aruz, of Persian classical poetry, to which most of the sung lyrics in Iranian dastgÅahi music belong, informs the rhythmic rendition of the singing. This results in a characteristic rhythmic style that is also adopted when a guše is perfomed only instrumentally [2, 3]. Aruz not only informs musical rhythm through the sequence of long and short syllables, but also through the qualitative features of the vowels (hejÅa) [4, 5]. For metred performance, musicians can draw on rhythmic cycles known as adwÅar-e iqÅai, the most common ones being kerešme, ˇcÅahÅar-pÅareh, zanguleh and gereyli [4]. Each dowr-e iqÅai is defined by a number of pulses, known as naqareh, and a structure of accents. 

A typical ensemble of Iranian dastgÅahi music is formed by santur (hammered zither), tÅar (long-neck lute), setÅar (long-neck lute), ney (bamboo flute), kamanˇce (spike fiddle), tonbak (goblet drum) and a singer. The music, however, is also commonly performed by a solo singer or instrumentalist. 

DastgÅahi music is an oral tradition and conventionally the students learn it by memorizing a specific radif taught in private lessons by an ostÅad. The learning process is based on observation and imitation. In the contemporary context some teachers use transcriptions in staff notation as teaching material. However the notation functions just as memory aid, since many details cannot be represented in the staff notation system. 

### 1.2 Computational analysis of Iranian dastg¯ahi music 

Considering the magnitude of Iranian dastgÅahi music, in terms of history, wide performance realm, complex theorization and extensive musicological research, this music tradition has received comparatively little attention from computational approaches. Pioneering work has been carried out by the researcher and santur performer Peyman Heydarian. Since his master thesis [6], Heydarian is working on the computational analysis of this instrument, especially its acoustic features [7±9], as well as on dastgÅahi music performed in this instrument, with a special focus on dastgÅah classification [10±12]. In fact, this second task, automatic dastgÅah identification and classifica- 

tion, has been the most common one by other researchers who approached this tradition from computational methods [13±16]. 

Computationally aided musicological research on dastgÅahi music is still very rare. Shafiei used score to audio alignment for the analysis of tahrir [17], while Sanati analysed intervals from ney recordings [18]. There has also been some work on dastgÅahi music generation using deep neural networks [19]. 

We argue that one of the reasons that explains that the computational analysis of dastgÅahi music is not yet been fully established in an unified trend, instead of occasional isolated works, is the lack of a comprehensive, publicly accessible datasets upon which continuous research can be built. All the publications referenced in the previous paragraphs gathered their own research datasets, but none of them offer any indication about possibilities for accessing them. Only Heydarian has been able to sustain a decades long research on this tradition based on his own dataset [20], but it is not public, and it only includes recordings of santur. Hence, the goal of KDC precisely is to contribute to the establishment of a coherent line of computational research on Iranian dastgÅahi music by providing an open, well curated corpus of high quality recordings, upon which this research can be built. 

### 2. DESCRIPTION OF KDC 

KDC is conceived as an ever growing corpus, so in this paper we present its first version. Although far from its ideal size in terms of coverage, it already offers a coherent and comprehensive representation of the dastgÅahi system. Currently, KCD contains 213 solo recordings by four professional musicians, 65 of which consist of complete guše performances and hence form the core of the corpus. 

In order to analyse the corpus, we draw on the five criteria defined by Serra [21]: 

Purpose: As described in section 1, KDC is created for the analysis of Iranian dastgÅahi music using corpus driven computational methods. Due to the lack of a notational system originally devised for this music tradition, and the difficulties of staff notation for capturing key elements of this music, especially regarding tuning, intonation and ornamentation, KDC primarily aims at gathering audio recordings. However, the inclusion of other data types, such as scores, lyrics, videos, images, etc., that might contribute to the general purpose of the corpus, is not excluded. A key point in the creation of KDC is the close collaboration with musicians. They do not only contribute with recordings and annotations, but also with their knowledge, evaluation, and research ideas. Musicians are thus considered as active collaborators of KDC. 

Coverage: According with KDC’s purpose, we focus on voice and melodic instruments. In this first version of the corpus, being one of our goals to test state-of-theart technologies for the analysis of this music tradition, we have focused on solo performances, and consciously excluded ensemble performances, that would present a greater challenge for computational analysis. In order to 

322 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

|||Perf|ormance|ŠÅahed|Ist|Pitch Set|R|adif|
|---|---|---|---|---|---|---|---|---|
||ˇCÅahÅargÅah|7|9:02|5|3|2|5|5:21|
||HomÅayun|5|7:35|5|4|2|3|3:50|
|Åah|MÅahur|6|8:37|5|2|2|3|2:03|
|stg|NavÅa|6|9:19|5|4|2|3|4:01|
|Da|RÅast-PanjgÅah|4|5:56|4|3|2|2|2:15|
||SegÅah|5|8:57|5|2|2|3|2:12|
||Šur|7|9:55|5|2|2|3|2:12|
||AbuatÅa|5|6:47|5|3|1|2|2:01|
|z|AfšÅari|5|9:36|5|4|1|2|1:56|
|vÅa|BayÅat-e Tork|5|8:03|5|3|1|2|1:47|
|ÅA|<br>Dašti|5|6:53|5|4|1|2|2:10|
||EsfahÅan|5|9:21|5|3|2|2|2:40|
||Total|65|100:01|59|38|20|31|31:40|



Table 1. Number of recordings in KDC according to dastgÅah and ÅavÅaz. For performance and radif recordings, the duration is also given. 

|Inst.|Musician|Rec.|Dur.|
|---|---|---|---|
|voice|F. Sahebghalam, R. Zalpour|24|37:50|
|ney|R. Zalpour, M. Khodadadi|37|45:54|
|setÅar|M. Shaari|35|47:57|
|Total||96|131:41|



Table 2. Number of performance and radif recordings in KDC according to instrument. 

build a first dataset that provides a coherent and comprehensive representation of the dastgÅah system, this first version of KDC contains the first guše of all 7 dastgÅahs and 5 ÅavÅazes, known as darÅamad, which holds great significance (see section 1.1). Four professional musicians (see Table 2) have contributed to KDC with original recordings of complete performances<sup>1</sup> of these 12 darÅamads. Hence, the corpus currently contains five full renditions of the 12 darÅamads, namely, two vocal ones, one female and one male (with the exception of the darÅamad of dastgÅah rÅast-panjgÅah, whose female vocal rendition could not be recorded), two by ney, and one by setÅar. According to their own decision, the musicians occasionally recorded more than one version of a particular darÅamad, and all of them are included in the corpus. This results in 65 performance recordings, which is the core of KDC (see Table 1). 

Completeness: KDC includes a csv file with metadata and annotations for all recordings, including the corresponding dastgÅah, guše, artist, instrument, recording type, and duration. Considering the methodological purpose of the corpus, the musicians who collaborate with KDC were asked to record the šÅahed of the performed darÅamad as a single, stable pitch. The 59 resulting recordings are included in KDC, and they were used to compute the frequency of the šÅahed,<sup>2</sup> which is added as an annotation 

> 1 Given its improvisational nature, there is no standard rendition of a particular guše. By complete performance we mean a rendition that completely conveys the performed guše. 

> 2 The pitch of the šÅahed was computed with the pYin: Notes plugin [22] of Sonic Visualiser 

in the metadata file. The musicians who collaborate with KDC show a great interest in the project and actively propose contributions to it, according to their understanding of which data could benefit the purpose of KDC. As a consequence, some musicians recorded the ist of the performed darÅamad in a separate file as a single, stable pitch, resulting in 38 recordings, the corresponding pitch set, resulting in 20 recordings, and one or more related performances according to radif (see Table 1). Since pattern analysis is a key task for the study of Iranian dastgÅahs, two of the collaborator musicians manually annotated the characteristic patterns that identify the performed guše using the software Praat [23]. Each of them annotated two full renditions of the 12 darÅamads, so that only the setÅar recordings are still not annotated in terms for patterns. 

Quality: all the recordings in KDC are provided in the lossless compression format flac. The recordings by M. Shaari and F. Sahebghalam were recorded in a professional recording studio at KUG, those by M. Khodadadi were recorded by the first author using a Zoom H4 recorder, and those by R. Zalpour by himself using his cell phone. The musicians, all having previous recording experience, evaluated the quality of their own recordings both in terms of sound and performance quality and agreed to include them in KDC as good representatives of their art. To validate the pitch frequencies of šÅahed, mp3 files were generated, and R. Zalpour assessed their correctness. 

Reusability: All the collaborator musicians contributed their recordings to KDC for them to be published under the Creative Commons Attribution-NonCommercialNoDerivatives 4.0 International License (CC BY-NC-ND 4.0).<sup>3</sup> In order to ensure the reusability of KDC, we follow the FAIR principles.<sup>4</sup> To ensure that all recordings are findable and reusable, they are made available through the KUG’s Phaidra repository.<sup>5</sup> Regarding accessibility, the 

> 3 https://creativecommons.org/licenses/ by-nc-nd/4.0/legalcode 

> 4 https://www.go-fair.org/fair-principles/ 

> 5 The following Phaidra collection is created for KDC: https:// phaidra.kug.ac.at/view/o:127195 

323 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

metadata of all recordings are also stored in MusicBrainz<sup>6</sup> in its original Farsi and with English aliases, and linked to their corresponding Phaidra objects. A specific protocol for interoperable structuring of Iranian dastgÅahi music is still being developed, and is expected to be evolving along with the expansion of the corpus. 

### 3. RESEARCH POTENTIAL OF KDC 

The hypothesis that motivated the KDC project is the conviction that musicological study of Iranian dastgÅahi music can deeply benefit from computational methods. Conversely, we argue that the characteristics of this music raise interesting research tasks for music information retrieval. In this section we point out some of the most relevant of these tasks. Since KDC was created with the purpose of researching the modal aspect of this music, tasks related to this domain are described in more detail. 

### 3.1 Melody and mode 

The study of melody in Iranian dastgÅahi music is one of the most essential tasks, especially for the purpose of KDC, therefore pitch track extraction is essential. According to our preliminary analyses, state-of-the-art algorithms perform satisfactorily for monophonic recordings as those by voice or ney. However, further research is still needed to obtain equally satisfactory results for instruments with high resonance as the setÅar (see section 4). A relevant research task based on these pitch tracks is the corpus driven analysis of vibrato and tahrir (see Fig. 5). Their automatic identification and measurement would contribute to their deeper understanding, but also to better define school styles, or idiomatic performance for specific instruments. 

Tasks conducing to the characterization of gušes are also of key importance. A particularly relevant one is automatic pattern analysis. A main challenge for this task from the computational point of view is evaluation. In order to contribute to that, KDC includes manual annotations by expert musicians. Analyses of each guše’s tonal hierarchy are also essential, especially those contributing to the understanding of concepts like Åsahed or ist (see section 1.1). 

Given the classification system of gušes, dastgÅahs and ÅavÅazes, this music tradition is well suited for automatic recognition and classification tasks, which in fact are the ones most commonly explored to date (see section 1.2). 

Finally, even though Iranian dastgÅahi music is not easily represented on staff notation, a tradition of transcriptions using this notation system exists. This music then can be also taken as a challenging case for automatic transcription, for which existing scores (currently only in print) can be used for evaluation. 

### 3.2 Other musical aspects 

Iranian dastgÅahi music offers interesting tasks for rhythm research. In metred performance, automatic dowr-e iqÅai 

> 6 The following MusicBrainz collection is created for KDC: https://musicbrainz.org/collection/ 6ee214c7-f116-4691-b46d-36033c8b17b0 

detection becomes a significant challenge, given the heterophonic nature of ensemble performance and the timbral and stylistic characteristic of solo performance. Expressive microtiming deviations from isochrony is a meaningful analysis for characterising performance style. Unmetred performance of dastgÅahi music offers a great opportunity for multimodal analysis combining audio and lyrics analysis (this would require incorporating text data to KDC). Natural Language Processing methods can be applied to model the prosodic features of aruz, that can later be mapped to music performance. 

Timbre is a very diverse and expressive feature of Iranian dastgÅahi music performance. Combined with nuances in dynamics, singers use vowel shades to introduce variability in sustained notes. Equally, ney performers use a wide range of timbres from bright, clean ones to raspy, breathy ones. Automatic analysis of the timbral categories can inform about stylistic preferences and if a relationship exists with specific gušes. The use of dynamics is another important element in Iranian dastgÅahi music expressivity, and its computational analysis can shed light about its systematic or stylistic use. 

### 4. PRELIMINARY ANALYSES 

In order to test the potential of KDC as described in the previous section, we carried out a series of preliminary analyses. The current size of KDC does not allow to obtain general conclusions about Iranian dastgÅahi music. Our aim is to explore the possibilities for computational methods, and therefore to suggest further lines of research for future stages of KDC. 

Since our main interest is the melodic dimension of dastgÅahi music, our analysis started with pitch track extraction. To that aim, we applied the CREPE algorithm [24] to all monophonic recordings of KDC, that is, those by voice and ney. After visual and aural examination, we concluded that state-of-the-art algorithms, both for monophonic and polyphonic signals,<sup>7</sup> do not produce results usable for further analysis on the recordings of setÅar, an instrument with high, and sought after, resonance and common use of chords. Consequently, the recordings by setÅar were excluded for these analyses. In order to ensure reproducibility, the data, metadata and annotations used for these analyses are shared as a dataset.<sup>8</sup> The code and resulting plots are also shared in a public repository.<sup>9</sup> 

### 4.1 Š¯ahed 

In order to study šÅahed, we compute pitch histograms from the previously extracted pitch tracks using the algorithm developed in [27]. The histograms are computed in cents aligned to the šÅahed that KDC has annotated for each individual recording. We also compute pitch histograms for the aggregated pitch tracks of all recordings of the same 

> 7 Pitch extraction was attempted on the setÅar recordings using the algorithms CREPE [24], pYin [22] and Melodia [25], the last two in their Sonic Visualiser [26] plug-in version. 

> 8 https://phaidra.kug.ac.at/o:127202 

> 9 https://github.com/Rafael-Caro/KDC-v1.0 

324 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
0.012<br>Zalpour (ney)<br>0.010 Zalpour (voice)<br>Khodadadi (ney)<br>count 0.008<br>0.006<br>normalized0.004<br>0.002<br>0.000<br>0 200 400 600 800 1000 1200<br>cents from šāhed<br><!-- End of picture text -->

Figure 1. Folded pitch histograms of three recordings of darÅamad abuatÅa 



<!-- Start of picture text -->
0.012<br>Abuatā (Khodadadi)<br>0.010 Māhur (Zalpour)<br>count 0.008<br>0.006<br>normalized0.004<br>8:---<br>0.002<br>0.000<br>-600 -400 -200 0 200 400<br>cents from šāhed<br><!-- End of picture text -->

Figure 2. Pitch histograms of two ney recordings. The vertical line indicates the šÅahed 

dastgÅah. Besides, histograms folded to one octave are also computed for individual recordings and for dastgÅahs. 

One of the most discussed issues in Iranian classical music is the concept of šÅahed. Different definitions for this concept can be found in the existing literature. According to Farhat, ª[i]n most of the Persian modes one tone assumes a conspicuously prominent role. It may or may not be the finalisº [1]. Nooshin argues that šÅahed is ª[t]he most prominent pitch, functioning as the tonal center of the modeº [28], while Talai defines it as ª[t]he most frequently repeated pitchº [29]. We argue that corpus driven analyses can help to examine which of the definitions for šÅahed, namely, ªprominentº tone, ªtonal centerº or ªmost frequently repeatedº tone better represents our results. 

Fig. 1 shows the folded pitch histograms of three different performances of the same guše, darÅamad abuatÅa. It can be seen how the šÅahed is the most frequent tone in M. Khodadadi’s performance, but that is not the case in the two ones by R. Zalpour, both vocal and ney. This preliminary result, together with other examples not mentioned here, suggests a more nuanced understanding of šÅahed, that would escape a unique, universally applicable definition. 

|Mus. (inst.)|Mean|SD|Lowest|Highest|
|---|---|---|---|---|
|Saheb. (voice)|4.19|10.28|-10.11|28.10|
|Zalp. (voice)|6.92|7.26|-5.02|16.46|
|Zalp. (ney)|-3.19|16.87|-35.43|23.99|
|Khod. (ney)|13.95|13.70|-7.69|37.07|



Table 3. Mean and SD of the differences in cents between the šÅahed’s pitch in their isolated recordings and in performance per musician and instrument. The difference between the lowest and highest performance of the šÅahed compared with the isolated recording is also given in cents. 

### 4.2 Intonation 

One interesting issue is the musicians’ abstract notion of the šÅahed’s pitch and its actual intonation in performance. Since all the collaborator musicians recorded the šÅahed of their performances as an extra, isolated file according to their aforementioned abstract notion, we can compare its pitch in both contexts. Fig. 2 shows how M. Khodadadi performs the šÅahed 37.07 cents higher than the isolated version he recorded himself, whilst R. Zalpour performs it 35.43 cents lower. We computed the difference between isolated šÅahed and its performed version (obtained from the value of the closest peak in the histogram) for all recordings (excluding setÅar), and calculated the mean and SD for each musician and instrument, as it can be seen in Table 3. The results show a great variability in the divergence between conceptualized and performed šÅahed, frequently reaching easily audible deviations. 

These observations points to an interesting line of future research regarding the perception of intervallic structures by musicians. The specific width of the intervals of a particular guše, an essential element for the conceptualization of Iranian dastgÅahi music, is part of the implicit knowledge of each individual musician, enacted mainly during performance. Their intellectual formulation, as the examples here analysed suggest, might no correspond with this implicit knowledge. 

### 4.3 Pitch alteration 

In some gušes specific degrees can be rendered by two neighbouring pitches. For example, in the case of darÅamad afšÅari, the degree above the šÅahed can be performed at 119 cents above it, which is considered the main tone for this degree, or at 204 cents over the šÅahed, which is considered an altered version of the same degree, as it can be seen in Fig. 3 (cent values computed according to [1]). These altered pitches are known as not-e mote˙gayer [1,30]. The use of this pitch alteration can be observed in pitch histograms as flat peaks, as it can be seen in Fig. 4 around 200 cents. These results point to another interesting line of research, for the computational detection of not-e mote˙gayer that can contribute to the better characterization of gušes. 

### 4.4 Vibrato and tahrir 

In order to analyse vibrato, we ran the Vibrato algorithm available in the Essentia library [31] on all recordings, and 

325 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
204 M<br>119<br>cents from šāhed<br>0 MW<br>94 95 96 139 140 141<br>time (seconds)<br>Figure 3.. Two excerpts of the the pitch track of the of the<br>vocal recording of darÅamad afšÅari by F. Sahebghalam. The darÅamad afšÅari by F. Sahebghalam. The by F. Sahebghalam. The<br>horizontal red line indicates the šÅahed, the gray line at 119 šÅahed, the gray line at 119, the gray line at 119<br>cents indicates the main pitch, whose corresponding not-e<br>mote˙gayer is indicated by the gray line at 204 cents.<br>boxes mark the performance of these two notes.<br>0.008<br>count0.006<br>0.004<br>normalized<br>0.002<br>0.000<br>-800 -600 -400-200 200 400<br>cents from šāhed<br><!-- End of picture text -->

Figure 3.. Two excerpts of the the pitch track of the of the vocal recording of darÅamad afšÅari by F. Sahebghalam. The darÅamad afšÅari by F. Sahebghalam. The by F. Sahebghalam. The horizontal red line indicates the šÅahed, the gray line at 119 šÅahed, the gray line at 119, the gray line at 119 cents indicates the main pitch, whose corresponding not-e mote˙gayer is indicated by the gray line at 204 cents. The boxes mark the performance of these two notes. 

Figure 4. Pitch histogram of the vocal recording of darÅamad afšÅari by F. Sahebghalam. The vertical line indicates the šÅahed 



<!-- Start of picture text -->
pitch track<br>0 MMM mwm<br>cents<br>-500<br>vibrato frequency<br>200<br>H100<br>vibrato extent<br>cents 5<br>128 129 130 131 132 133 134 135 136 137<br>time (seconds)<br><!-- End of picture text -->

Figure 5. Excerpt of the recording of darÅamad abuatÅa by F. Sahebghalam. Upper plot shows pitch track (horizontal line indicates šÅahed), middle plot detected vibrato frequency, and lower plot detected vibrato extent. Highlighted section shows tahrir. 

the results were plotted against the pitch track (see Fig. 5 for an example). These results, stored as csv files, together with the plots for all recordings are available in the code repository. Through visual evaluation of the results we argue that further research is required in order to improve automatic detection of vibrato for this tradition. 

DastgÅahi music is an idiomatic tradition. Vocal and instrumental performances are characterized by specific techniques and sound qualities, being vibrato a relevant one. Its extent, frequency and occurrence are idiomatically specified by instrument, school or personal style. Automatic vibrato detection and measurement can contribute to characterizing idiomatic styles. Another important vocal technique is tahrir, which consists in wide cyclic pitch alteration of a particular tone in terms of pitch and timber. The pitch fluctuation is not realized as glissandi but jumps, and this might explain why it is not detected by the used algorithm, as shown in Fig. 5. Analysing the difference between these two techniques would help to understand the idiomatic practices in Iranian dastgÅahi music. 

### 5. CONCLUSIONS AND FUTURE WORK 

With KDC we set a very ambitious goal: to create an open, well curated, ever growing corpus of Iranian dastgÅahi music data, metadata and expert annotations which can contribute to the development of a coherent line of computational research for this music tradition. This is a task that requires collaborative efforts from musicologists, musicians and computer engineers. KDC is still in its infancy, but its first version presented in this paper is complete enough to test state-of-the-art methodologies, obtain preliminary results, and consequently propose new directions for future research. 

The expansion of KDC is and is going to be a constant future task. As any other aspect of our lives in the past two years, the COVID-19 pandemic has hindered the development of KDC with the suspension of international travels (economic sanctions against Iran prevent working with musicians living in the country from outside). Besides the addition of recordings that cover new gušes, instruments and schools, increasing the number of expert annotations is one of our short term goals. In a first stage, we aim at having the 5 renditions of the whole set of 12 daramÅads annotated at least by three different musicians, so that we can start studying this phenomenon from the perception of the performers. 

Regarding computational analysis, a short term goal is to seek collaborations to perform automatic pattern analysis. This is a fundamental element for the characterization of gušes, and most of our collaborator musicians have highlighted the importance of this task and their interest in it. The annotations currently existing in KDC are aimed to this goal. Other tasks that are of our interest, and for which collaboration with computer engineers is also necessary, is the improvement of pitch track extraction for instruments with great resonance as setÅar. Finally, collaboration will also be sought for the development of methods for automatic tahrir detection and analysis. 

326 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

### 6. ACKNOWLEDGEMENTS 

The authors would like to express their sincerest gratitude and acknowledgement to their collaborator musicians Masoud Shaari, Farahnaz Sahebghalam, Reza Zalpour and Mohammad Khodadadi, not only for contributing their recordings and ideas to KDC, but also for their enthusiastic support to the project. We would also like to thank Dr. Negar Bouban and Reza Zalpour for their very valuable manual annotations of melodic patterns. Finally, we thank Kunstuniversität Graz for the financial support that makes KDC possible. 

### 7. REFERENCES 

- [1] H. Farhat, The DastgÅah Concept in Persian Music. Cambridge and New York: Cambridge University Press, 1990. 

- [2] T. Tsuge, ªRhythmic aspects of the Âvâz in persian music,º Ethnomusicology, vol. 14, no. 2, pp. 205±227, 1970. 

- [3] F. Amoozegar-Fassie, ªThe poetics of persian music: The intimate correlation between prosody and persian classical music,º Ph.D. dissertation, Faculty of Graduate Studies, University of British Columbia, UK, 2008. 

- [4] M. Azadehfar, Rhythmic structure in Iranian music. Tehran: Tehran University Press, 2017. 

- [5] N. Bouban, ªBarresi-ye AvÅai-ye<sup>Å</sup> ritm dar pÅayehÅa-ye vÅajegan-e š’er va nasr-e fÅarsi-ye rasmi [the phonetic study of rhythm in units of poems and writings in standard farsi],º Majaleh-ye pajuheš-hÅa-ye zabÅanšenasi, vol. 1, no. 1, pp. 101±122, 2010. 

- [6] P. Heydarian, ªMusic note recognition for santoor,º Master’s thesis, Tarbiat Modarres University, Iran, 2000. 

- [7] P. Heydarian and J. D. Reiss, ªThe persian music and the santur instrument,º in Proc. of the 6th Int. Society for Music Information Retrieval Conf., London, UK, 2005, pp. 524±527. 

- [8] P. Heydarian and L. Jones, ªMeasurement and calculation of the parameters of santur,º in Proc. of the Annual Conf. of the Canadian Acoustical Association (CAA), Vancouver, Columbia, 2008. 

- [9] ÐÐ, ªTonic and scale recognition in persian audio musical signals,º in 12th Int. Conf. on Signal Processing (ICSP), Hangzhou, China, 2014. 

- [10] P. Heydarian, L. Jones, and A. Seago, ªAutomatic mode estimation of Persian musical signals,º in 133rd Audio Engineering Society Convention, San Francisco, USA, 2012. 

- [11] P. Heydarian, ªAutomatic recognition of persian musical modes in audio musical signals,º Ph.D. dissertation, Faculty of Art, Architecture and Design, London Metropolitan University, UK, 2016. 

- [12] P. Heydarian and D. Bainbridge, ªDastgàh recognition in Iranian music: Different features and optimized parameters,º in 6th International Conference on Digital Libraries for Musicology (DLfM ’19), November 9, 2019, The Hague, Netherlands., 2019, pp. 53±57. 

- [13] N. Darabi, N. H. Azimi, and H. Nojumi, ªRecognition of dastgah and maqam for persian music with detecting skeletal melodic models,º in Proc. SPS-DARTS 2006The second annual IEEE Benelux/DSP Valley Signal Processing Symposium, Antwerp, Belgium, 2006. 

- [14] S. Abdoli, ªIranian traditional music dastgah classification,º in Proceedings of the 12th International Society for Music Information Retrieval Conference, ISMIR 2011, 2011, pp. 275±280. 

- [15] M. A. Layegh, S. Haghipour, and Y. N. Sarem, ªClassification of the radif of mirza abdollah a canonic repertoire of persian music using svm method,º Gazi University Journal of Science, vol. 1, no. 4, pp. 57±256, 2013. 

- [16] L. Ciamarone, B. Bozkurt, and X. Serra, ªAutomatic Dastgah Recognition Using Markov Models,º in Proceedings of the 14th International Symposium on Computer Music Multidisciplinary Research, 2019, pp. 51± 58. 

- [17] S. Shafiei, ªAnalysis of vocal ornamentation in iranian classical music,º in Proc. of the 16th Sound and Music Computing Conf., Málaga, Spain, 2019, pp. 437±441. 

- [18] F. Sanati, ªAn investigation on the value of intervals in persian music,º Master’s thesis, Department of Music, University of Jyväskylä, Finland, 2020. 

- [19] S. Malekzadeh, M. Samami, S. R. Azar, and M. Rayegan, ªClassical music generation in distinct dastgahs with alimnet ACGAN,º CoRR, vol. abs/1901.04696, 2019. 

- [20] P. Heydarian and J. D. Reiss, ªA database for persian music,º in Proc. of the Digital Music Research Network Summer Conference (DMRN 2005), Glasgow, UK, 2005. 

- [21] X. Serra, ªCreating research corpora for the computational study of music: the case of the compmusic project,º in 53rd AES International Conference on Semantic Audio, New York, USA, 2014, pp. 1±9. 

- [22] M. Mauch and S. Dixon, ªpYIN: A fundamental frequency estimator using probabilistic threshold distributions,º in Proceedings of the IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP 2014), Florence, Italy, 2014, pp. 659±663. 

- [23] P. Boersma and D. Weenink, ªPraat: doing phonetics by computer [computer program],º 1992±2022. [Online]. Available: https://www.praat.org 

327 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

- [24] J. W. Kim, J. Salamon, P. Li, and J. P. Bello, ªCrepe: A convolutional representation for pitch estimation,º in 2018 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), Calgary, Canada, 2018, pp. 161±165. 

- [25] J. Salamon and E. Gómez, ªMelody extraction from polyphonic music signals using pitch contour characteristics,º IEEE Transactions on Audio, Speech and Language Processing, vol. 20, pp. 1759±1770, 2012. 

- [26] C. Cannam, C. Landone, and M. Sandler, ªSonic visualiser: An open source application for viewing, analysing, and annotating music audio files,º in Proceedings of the ACM Multimedia 2010 International Conference, Firenze, Italy, October 2010, pp. 1467± 1468. 

- [27] G. K. Koduri, V. Ishwar, J. Serrà, and X. Serra, ªIntonation analysis of rÅagas in carnatic music,º Journal of New Music Research, vol. 43, pp. 73±94, 2014. 

- [28] L. Nooshin, ªThe song of the nightingale: Processes of improvisation in dastgÅah SegÅah (Iranian classical music),º British Journal of Ethnomusicology, vol. 7, no. 1, pp. 69±116, 1998. 

- [29] D. Talai, ªA New Approach to the Theory of Persian Art Music: The RadÅıf and the Modal System,º in Garland Encyclopedia of World Music Volume 6: The Middle East, V. Danielson, S. Marcus, and D. Reynolds, Eds. New York: Routledge, 2001, pp. 894±903. 

- [30] H. Asadi, ªTheoretical foundation of persian classical music: DastgÅah as a muti-modal cycle,º Mahoor, vol. 6, pp. 43±56, 2004. 

- [31] D. Bogdanov, N. Wack, E. Gómez Gutiérrez, S. Gulati, H. Boyer, O. Mayor, G. Roma Trepat, J. Salamon, J. R. Zapata González, and X. Serra, ªEssentia: An audio analysis library for music information retrieval,º in Proc. of the 14th Int. Society for Music Information Retrieval Conf., Curitiba, Brazil, 2013, pp. 493±498. 

328 

