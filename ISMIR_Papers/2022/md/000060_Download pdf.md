---
paper_id: "000060"
year: 2022
title: "Download pdf"
source_url: "https://zenodo.org/record/7316710/files/000060.pdf"
---

# **COUNTERPOINT ERROR-DETECTION TOOLS FOR OPTICAL MUSIC RECOGNITION OF RENAISSANCE POLYPHONIC MUSIC** 

**Martha E. Thomae Julie E. Cumming Ichiro Fujinaga** McGill University McGill University McGill University martha.thomaeelias@mail.mcgill.ca julie.cumming@mcgill.ca ichiro.fujinaga@mcgill.ca 

## **ABSTRACT** 

In this paper, we present a music information retrieval (MIR) pipeline to aid musicologists in making editions of mensural music sources. We designed this pipeline by improving existing MIR tools and allowing for their interoperability rather than implementing a new monolithic tool. These MIR tools include technologies such as optical music recognition (OMR), automatic voice alignment for mensural notation, editorial correction software, and computational counterpoint error detection. To ease the editorial correction process necessary to obtain correctly linedup scores, we evaluate whether the use of counterpoint error-detection tools makes the correction process more efficient. While this idea has been discussed before, this paper presents the first attempt at implementing it. The results confirm that marking illegal dissonances in the score following the rules of Renaissance counterpoint makes the process of editorial correction of scribal errors in Renaissance music more efficient by reducing the time taken and improving the accuracy of such corrections. Moreover, it also allowed us to catch OMR errors that had passed through undetected at a previous step of the pipeline. This paper is part of a larger project to preserve and increase access to a set of Guatemalan polyphonic choirbooks through digital images and symbolic scores. 

## **1. INTRODUCTION** 

This paper discusses part of a larger project to preserve and increase access to a set of six Guatemalan Cathedral choirbooks (the _GuatC_ collection).<sup>1</sup> These choirbooks, written in mensural notation, contain mostly sixteenth-century polyphonic music that was copied in the seventeenth and eighteenth centuries [1]. They document a continuous performance tradition of sacred choral music from the Renaissance until the beginning of the nineteenth century and are valuable sources for studying the transmission of music from Europe to Latin America. 

1 _GuatC_ : Guatemala. Guatemala City. Catedral, Archivo Capitular. Other sigla include GCA-Gc. 

© M. E. Thomae, J. E. Cumming, and I. Fujinaga. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). **Attribution:** M. E. Thomae, J. E. Cumming, and I. Fujinaga, “Counterpoint Error-Detection Tools for Optical Music Recognition of Renaissance Polyphonic Music”, in _Proc. of the 23rd Int. Society for Music Information Retrieval Conf.,_ Bengaluru, India, 2022. 

Given the limited access to these manuscript sources, it is of utmost importance to digitize and encode this corpus which otherwise might be lost, damaged, or forgotten. We used a set of digitization and music information retrieval (MIR) technologies to obtain digital images and symbolic files encoding scores with editorial corrections for each of the pieces of the first choirbook of the collection, _GuatC 1_ (see Figure 1). In the process, we tested the following three-step pipeline: (i) digitization, (ii) optical music recognition, and (iii) automatic voice alignment & editorial correction. The digitization step, conducted with a do-it-yourself scanner, was discussed in a previous publication [2]. In this paper, we focus on the encoding part of the pipeline, the last two steps. 

1. **Optical music recognition (OMR) & correction of the results.** We perform OMR on the images to retrieve a symbolic file (a Mensural MEI file) encoding the music of the manuscript. We used the _Music Recognition Encoding and Transcription_ ( _MuRET_ ) OMR framework for this step (see Section 2.2). 

2. **Automatic voice alignment & editorial corrections.** Since we are dealing with mensural notation, OMR is not enough to encode the full rhythmic information of the pieces and obtain a score with the voices properly lined up (see Section 2.1). Two additional steps are needed: (1) _automatic voice alignment_ , which provides the actual duration of each note and returns a preliminary score; and (2) _editorial correction_ , which allows for corrections of scribal errors, some of which can affect the alignment of the voices into a score. We used the _Measuring Polyphony_ ( _MP_ ) _Editor_ for this (see Section 2.3). 

This process generates symbolic scores with editorial corrections in a semi-automatic way through OMR and automatic voice alignment. The user manually corrects the output of each step, correcting the results of the OMR— the recognized symbols and their pitches—in MuRET and correcting the results of the voice alignment in the MP Editor. The latter normally implies the correction of scribal errors in the form of editorial corrections and occasional OMR errors that went undetected in the previous step of the pipeline. We evaluate whether the use of a tool that identifies illegal dissonances in Renaissance counterpoint (see Section 2.4) helps in the correction of this last step of the pipeline. The goal of this MIR pipeline is to aid musicologists in making editions of mensural music sources, 

501 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

with the last step aimed to reduce the challenge of aligning (possibly error-ridden) polyphonic parts by automatically scoring up the voices and by flagging areas of special attention to the human editor—given how time-consuming it can be to find scribal errors. While the idea of using counterpoint rules to detect errors in the original mensural sources has been mentioned before [3], it has not been implemented yet. This paper provides the first attempt at its implementation and evaluation by conducting a small experiment to test our hypothesis. 



<!-- Start of picture text -->
superius altus<br>tenor bassus<br><!-- End of picture text -->

**Figure 1** : Example of a piece in GuatC 1. The voices are written in choirbook layout, where each voice is in a different area of the book opening. 

## **2. BACKGROUND** 

The GuatC collection consists of a set of six manuscript choirbooks written in mensural notation. The first three books have been inventoried [4–6], and the fourth one has been fully transcribed [6]. An overview of the whole collection was presented in [1] and a full inventory is expected [7]. Microfilm images for the first three books were created in the 1980s [8, pp. 3–4]; however, these images are of low quality, with cropped areas and missing folios. 

We decided to test the MIR pipeline presented in Section 1 with the first choirbook (GuatC 1, one of the bestpreserved manuscripts). The GuatC 1 is a book of masses. It contains twelve masses and fifteen short polyphonic pieces. Eight of the masses are from sixteenth-century composers, one mass is by a seventeenth-century composer, another by an eighteenth-century one, and two by composers whose period of activity remains unknown. On the other hand, most of the short polyphonic pieces are anonymous. Modern transcriptions of ten of the masses and four of the short pieces can be found in the _Choral Public Domain Library_ ( _CPDL_ ) wiki, although the provenance of the materials on which the transcriptions were based is shrouded in contradictory accounts.<sup>2</sup> 

> 2 The account found at the _Música Colonial Archive_ page (https://www.cpdl.org/wiki/index.php/Música_Colonial_Archive) cannot be corroborated by the Centro de Investigaciones Regionales de Mesoamérica (CIRMA), the institution that holds the original microfilms, as indicated by the director of CIRMA’s historical archive (Thelma Porres, personal communication, November 2018). 

## **2.1 Mensural Notation and the Voice-Alignment Issue** 

Mensural notation was used for polyphonic music in Europe from the thirteenth to the seventeenth centuries. In triple meter, the duration of the notes in mensural notation depends on the context (i.e., the notes preceding or following), as shown in Figure 2. In Figure 2a, the same note shape has two different durational values, a ternary value, which is called _perfect_ , and a binary value, which is called _imperfect_ . In Figure 2b, another note shape represents two different durations, a regular one and an _altered_ one where the note has twice the duration of its regular value. These three durational values of notes, perfect, imperfect, and altered, are common in fourteenth- to sixteenth-century mensural notation. 



<!-- Start of picture text -->
Tenor<br>uermefait<br>3<br>Mon cuer me fait<br><!-- End of picture text -->

(a) Same note shape with a perfect (P; triple) and imperfect (I; duple) value. 



<!-- Start of picture text -->
Triplum<br>Mon fait<br>Mon cuerme fait<br><!-- End of picture text -->

(b) Same note shape with a regular (one beat) and altered (A; two beats) value. 

**Figure 2** : Example of the different durational values of notes given the context. Both (a) and (b) show an example in mensural notation and its modern transcription below. 

The context-dependent duration of mensural notes, together with the separate-parts layout of most mensural music (e.g., the choirbook layout shown in Figure 1), makes it difficult to know what notes are sounding at the same time in the different voices. We implemented an algorithm to compute the duration of notes based on the context and present the piece lined up in a score [9]. This algorithm is referred to as “automatic voice alignment” or “automatic scoring up” of mensural music. After scoring up the voices, it is still necessary to account for errors (e.g., missing or wrong values for notes and rests) to have a correct score. The scoring up of the piece helps to identify OMR and scribal errors that are obscured by the separate-parts arrangement of the music. 

## **2.2 The Music Recognition Encoding and Transcription OMR Framework (MuRET)** 

There are a few OMR frameworks for early music, including the OMR workflow used by the SIMSSA project through the Rodan workflow manager with the Neon editor [10–13], the OMMR4all framework [14], Aruspix [15], 

502 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

and MuRET [16,17]. MuRET, a framework developed by David Rizo at the University of Alicante as part of the Hispamus Project [18], is the only one with support for handwritten mensural notation.<sup>3</sup> 

As with other OMR tools, MuRET provides information on the pitch and shape of notes as part of its workflow and allows the user to correct the recognized symbols. It also has support for encoding the imperfect / perfect / altered durational values of mensural notes, though these values are not retrieved automatically—as in the case of pitches and note shapes—and instead have to be entered manually in **mens—a Humdrum format for mensural notation [19]—using MuRET’s interface. 

At the end of the OMR process, the user can export the encoded music into MEI (Music Encoding Initiative)—a symbolic file format that has support for encoding mensural notation [20]. It is possible to export two kinds of MEI files in MuRET, _score-based_ and _parts-based_ . The scorebased file has the voices stacked and aligned based on the duration of the notes; however, for the notes to be correctly lined up, the user must have provided the durational values for the notes in **mens (i.e., include imperfections and alterations). The parts-based file provides the music encoded as separate parts (just as in the original sources), encoding only pitch and note-shape information for each note. The information about the notes’ imperfect, perfect, or altered values is calculated by the next tool in the MIR pipeline, the MP Editor, which will return the score-based Mensural MEI file. 

## **2.3 The Measuring Polyphony Editor (MP Editor)** 

The MP Editor is an online editor for mensural notation [21], developed under the Measuring Polyphony Project directed by Karen Desmond.<sup>4</sup> Until recently, this was the only mensural notation editor that performed automatic voice alignment,<sup>5</sup> a functionality that I implemented. The MP Editor takes in a series of notes (i.e., pitches and note shape) and automatically lines up the voices into a score using a re-implementation of the scoring-up script in [9]; additionally, after scoring up the voices, the MP Editor allows the user to perform editorial corrections. In a previous paper, I presented the work done to use MuRET’s parts-based output as MP Editor’s input, which allows for a complete and semi-automatic pipeline of the scoring up of each piece of the GuatC 1 corpus [23]. 

## **2.4 The Dissonance Filter (DF)** 

The goal of this article is to evaluate the efficiency of using counterpoint error markers while making editorial corrections in the last step of the MIR pipeline. On a previous paper, I presented the work done to integrate humlib—Humdrum’s data-parsing library—within the MP 

Editor [23],<sup>6</sup> which allows humlib’s Renaissance dissonance filter to label the dissonant notes.<sup>7</sup> The complete list of dissonance labels available in the filter can be consulted on the Verovio Humdrum Viewer (VHV) page.<sup>8</sup> In the MP Editor, the DF marks the dissonances in the score, and makes a distinction between the legal (e.g., passing tones, lower/upper neighbours, and suspensions) and illegal dissonances, rendering the former in blue and the latter in orange. From the set of dissonance labels presented in the VHV documentation page, the ones considered illegal (and rendered in orange font) are _Z_ / _z_ , _Y_ / _y_ , _L_ / _l_ , and _x_ . For an example of how the DF labels the dissonances in the MP Editor, see Figures 3–5. 

## **3. METHODOLOGY** 

## **3.1 Data Preparation** 

We randomly selected fifteen pieces from the GuatC 1 manuscript, where each piece was either a mass movement or a short polyphonic piece. The fifteen pieces represent around 20% of the total corpus. To ease the editorial work in the MP Editor, we subdivided the long mass movements into smaller units that we called “self-contained units.” Here, we are considering as a “long movement” anything that has more than two openings (i.e., four pages) in the manuscript. We defined the “self-contained unit” as the minimum number of consecutive sections (one or more) that start at a page beginning and end at a page ending. This definition was needed because we had to face the problem of handling sections whose beginning or end do not correspond to the beginning or ending of an image (i.e., a page) since MuRET can only produce an MEI output from a set of one or more selected images. 

We obtained a total of 23 self-contained units and divided these into two datasets: a _DF Dataset_ where the dissonance filter would be activated during the correction process, and a _NDF Dataset_ where no dissonance filter would be used during correction. To guarantee a balanced dataset, we arranged for the DF and NDF datasets to have the same average number of measures, voices, and illegal dissonances. We also made sure that each dataset had close to the same number of CPDL transcriptions to use as a reference, providing another musician’s interpretation of where the mistakes are found and how to fix them. 

Table 1 shows the pieces in the two datasets. The first column contains the name of the self-contained unit (e.g., Missa9.2_Gloria1), which shows the mass number in the inventory table of the GuatC 1 found in [25] (e.g., Missa9 for the 9th mass in GuatC 1), the movement number and name (e.g., Missa9.2_Gloria1 indicates the second movement in the mass, which is always a _Gloria_ ), and the unit number within that movement (the first unit of the Gloria). 

> 3 https://muret.dlsi.ua.es/muret/#/home 

> 4 https://editor.measuringpolyphony.org 

> 5 Imperfections and alterations are entered manually in the editor from the Computerized Mensural Music Editing (CMME) project. The new Mensural Rhythm Interpretation Tool (MeRIT) automatically scores up the piece, but its focus is on introspection and pedagogical use and not on producing an edited score [22]. 

> 6 https://github.com/craigsapp/humlib 

> 7 This filter was developed by Alex Morgan for the Josquin Research Project (https://josquin.stanford.edu). It is based on Peter Schubert’s book on modal counterpoint [24]. 

> 8 https://doc.verovio.humdrum.org/filter/ dissonant/ 

503 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

## **3.2 Experiment Setup and Evaluation Procedure** 

The experiment was conducted by a Bachelor of Music student with a major in voice and a minor in early music. She has knowledge of mensural notation and counterpoint from courses in paleography and Renaissance musicianship, in addition to her participation in early-music vocal ensembles. She corrected each piece following these steps: (1) look at the ends of phrases and sections to see if the voices line up at the cadence in order to determine if there is a note value missing earlier in the piece; and (2) look at the notes preceding that cadence, this would mean looking at all these notes in the NDF Dataset, while focusing on the places with orange labels and the notes preceding them in the DF Dataset. She was also instructed to report the correction time for each piece, annotate any comments about the piece that she considered relevant, and provide the files downloaded from the MP Editor at the end of the correction process. Although most of the corrections at this point in the MIR pipeline should be editorial, we asked the experimenter to still keep an eye out for OMR errors. 

We recorded the correction time per piece, the time invested in the correction of the pieces per dataset (DF and NDF), and the accuracy of those corrections. While the average correction time of the DF and NDF datasets is easy to obtain, analyzing the accuracy of the corrections is more involved. To study the accuracy of the corrections, we used three sets of files: (1) the OMR scored-up files obtained by uploading the OMR Parts-based MEI file into the MP Editor and exporting the score with no corrections; (2) the scores corrected by the experimenter; and (3) the CPDL scores. We compared the OMR scores against the experimenter’s scores to identify the experimenter’s corrections. And we compared the experimenter’s scores against the CPDL scores to identify discrepancies between the two transcriptions.<sup>9</sup> While the CPDL scores cannot be considered ground truth, they record another musician’s ideas about mistakes in the sources, and help in the process of checking the experimenter’s corrections. Whenever we found a discrepancy, we analyzed both versions (the experimenter’s and the CPDL’s) and chose the best solution, always favoring the one that removed “true” illegal dissonance labels and that guaranteed imitation and motivic consistency.<sup>10</sup> Here, we are distinguishing between “true” and “false” illegal dissonances, where **true** illegal dissonances are notes that are correctly labelled as such (i.e., true positives) and, on the other hand, **false** illegal dissonances are actually legal dissonances that are incorrectly classified by the DF (i.e., false positives). We also reuploaded the experimenter’s files into the MP Editor and activated the DF on her files to check if there were any orange labels left to determine whether these were counterpoint errors missed by the experimenter or if they were 

> 9 The OMR and the experimenter’s scores are encoded in MEI, while the CPDL scores are in MusicXML. Therefore, to compare them, we wrote transformation scripts for both formats to convert them into text files that encode the notes in each voice as a sequence of tokens and then compared these text files using a _diff_ tool. 

> 10 Imitation refers to repeated melodic motifs in different voices, typical of sacred polyphony. 

“false” illegal dissonances. We found a few instances of these false illegal dissonances as reported in Section 4.1. 

## **4. RESULTS AND DISCUSSION** 

There are two types of results in this experiment: (1) the average correction time of the NDF and DF datasets, which can be seen in Table 1; and (2) the experimenter score files, which are stored in GitHub.<sup>11</sup> 

||**NDF Da**|**taset**||||
|---|---|---|---|---|---|
|Self-contained|CPDL|Nu|mber|of|Time|
|Units||M|V|IllD|(min)|
|Missa8.4_Sanctus0|yes|29|4|9|8|
|Missa9.2_Gloria1|yes|44|4|46|13|
|Missa9.2_Gloria2|yes|37|4|8|17|
|Missa10.1_Kyrie0|**part**|71|4|4|18|
|Missa10.3_Credo1|yes|67|4|64|16|
|Missa10.5_AgnusI0|yes|23|4|2|7|
|Missa15.3_Credo2|yes|6|4|43|15|
|Missa15.3_Credo3|yes|48|3|0|15|
|Missa16.4_Sanctus2|yes|13|4|17|11|
|Missa17.5_Agnus0|yes|26|4|1|6|
|Piece21_Surrexit0|**no**|17|5|21|10|
||**Average**|**39.2**|**4**|**19.5**|**12.4**|
||**St**|**andard**|**Dev**|**iation**|**4.2**|



||**DF Dat**|**aset**||||
|---|---|---|---|---|---|
|Self-contained|CPDL|Nu|mber|of|Time|
|Units||M|V|IllD|(min)|
|Missa7.4_Sanctus1|**no**|29|4|0|1|
|Missa7.4_Sanctus2|**no**|50|4|52|10|
|Missa9.6_AgnusII0|yes|35|5|14|7|
|Missa10.3_Credo2|yes|40|4|3|2|
|Missa10.3_Credo3|yes|64|4|17|30|
|Missa13.5_Agnus0|yes|30|4|6|6|
|Missa14.1_Kyrie0|yes|56|4|23|7|
|Missa15.1_Kyrie0|yes|44|4|0|1|
|Missa15.3_Credo1|yes|64|4|61|2|
|Missa16.4_Sanctus1|yes|22|4|2|1|
|Missa16.4_Sanctus3|yes|27|3|16|9|
|Piece25_Surrexit0|yes|15|4|13|6|
|**A**|**verage**|**39.7**|**4**|**17.3**|**6.8**|
||**St**|**andard**|**Dev**|**iation**|**8.0**|



**Table 1** : Voice-alignment correction time for each piece in the No Dissonance Filter (NDF) Dataset and the Dissonance Filter (DF) Dataset. The pieces shaded in gray did not require correction. The _M_ stands for measures, _V_ for voices, _IllD_ for illegal dissonances, and the _CPDL_ column indicates if a modern transcription exists on CPDL. 

> 11 https://github.com/martha-thomae/GuatC1/tree/ Experiment/MPeditor_files/Score_files 

504 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

## **4.1 Discussion** 

By analyzing the corrections made to the individual pieces and looking at their correction times, the following points become apparent: 

1. **The use of the DF reduces the correction time.** As shown in Table 1, the use of the DF reduces the correction time from 12 _._ 4 to 6 _._ 8 minutes, almost halving it. However, the standard deviation of the DF Dataset is high compared to the one in the NDF Dataset. This is due to an outlier in the DF Dataset. While the correction time for all pieces in the DF Dataset is in the 1–10 minute range, the Missa10.3_Credo3 correction time is 30 minutes. Details about this mass will be provided later in point 4 below. Removing this outlier from the DF Dataset reduces the average correction time to 4 _._ 7 minutes (and the standard deviation is reduced from 8 _._ 0 to 3 _._ 4). Eliminating the outlier reduces the correction time with the DF to almost a third of the correction time for the NDF. Moreover, for pieces that have around the same amount of information—number of measures, voices, and illegal dissonances—and that did not require any corrections (see grey entries in Table 1), the reduction in time when using the DF is considerable. The pieces in grey with 26 and 29 measures took the experimenter 6 minutes to correct without the DF, and 1 minute with the DF. Similarly, the pieces with 48 and 44 measures took the experimenter 15 minutes without the DF and 1 minute with the DF, despite the fact that the latter (the piece in the DF data) has an extra voice. 

2. **The use of the DF increases accuracy in the correction.** There were numerous cases where the experimenter made a rhythmic change too late.<sup>12</sup> An example is shown in Figure 3. Figure 3a shows the original manuscript reading of Missa15.3_Credo2. Looking at this scored-up version of the piece, the experimenter noticed that the cadence to G at the end of the example was not correct and knew that she had to cut a minim in the alto voice sometime before the cadence. Her correction, halving a semibreve in measure 14, is shown in Figure 3b. This change still resulted in an illegal dissonance, however, shown in Figure 3b by the orange “z” under the _Bb_ in the bass (not shown in the experimenter’s NDF dataset). The rhythmic change should have been made a few measures before (in measure 12), as shown in Figure 3c. While the experimenter’s correction removes all following illegal dissonances (Figure 3b), it still leaves the ones preceding it. The DF would have shown her where to look—just before the first orange label—to change the note value. This change matches the CPDL correction. 

3. **The DF not only aids in identifying scribal errors but also OMR errors that affect the voice alignment.** For pieces where MURET missed a note, or assigned the wrong value of a note or rest in the manuscript, 

> 12 This happened in Missa7.4_Sanctus2, Missa15.3_Credo2, and Missa16.4_Sanctus3. 



<!-- Start of picture text -->
M12 M14<br>(9)<br>142r.jpg_p1s2<br>141vjpg.p1.5<br>142r.jpg.p1.58<br>(a) Original reading.<br>M12 M14 M12 M14<br>xP<br>141vjpg.pl 141vjpg.p1<br>142rjpg.p1,58 142rjpg.p1.38<br>(b) Experimenter’s version. (c) Correct version.<br><!-- End of picture text -->

**Figure 3** : Missa15.3_Credo2 beginning at measure 12. The circled semibreve in measure 14 is the one halved by the experimenter, while the circled semibreve in measure 12 is the one that should have been halved. **Clefs from top to bottom:** G, G, suboctave G, suboctave G. 

the DF helped to identify the missing or incorrect symbol.<sup>13</sup> Although these pieces were part of the NDF Dataset (where the DF was not used during the experiment), applying the DF on the scored-up OMR file could have saved the experimenter some time as the orange labels help in noticing these errors. By finding the first orange label and checking the manuscript around that spot, the experimenter would have realized that a note/rest in the manuscript was missing (or had the wrong value) in the rendered file. 

4. **Style issue – Eighteenth-century works.** The DF was not designed to handle eighteenth-century compositional style. Mass 10 is the only mass in the corpus that we know was composed in the eighteenth century. In many of its self-contained units, one can see the use of seventh chords and ties.<sup>14</sup> In this mass, the DF did not work well, because dissonances that are illegal in Renaissance style are legal in the eighteenth century. The experimenter pointed out a passage in Missa10.3_Credo3, which took her 30 minutes to correct. She invested a lot of time trying to figure out how 

> 13 This happened in Missa9.2_Gloria1, Missa9.2_Gloria2, and Missa10.3_Credo1. 

> 14 Seventh chords are found in Missas10.1_Kyrie0 (measure 4), Missa10.3_Credo1 (measures 11, 12, and 39), Missa10.3_Credo3 (measure 20), and Missa10.5_AgnusI0 (measure 16). While ties are found in Missa10.3_Credo1 and Missa10.3_Credo3. 

505 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

to get rid of the orange labels and finally left the passage as it was. This was the correct decision as this passage combines Baroque and Renaissance styles, with seventh chords (see Figure 4), such as the third inversion seventh chord over the red “D,” shown by the orange “y.” 



<!-- Start of picture text -->
n 79v.jpg,ng s P<br>80r.jpg,<br>g<br>79v.jpg, Z S g<br>gs<br><!-- End of picture text -->

**Figure 4** : Passage where the experimenter invested a lot of time in Missa10.3_Credo3. It is a combination of Renaissance and Baroque style with fake suspensions and seventh chords. **Clefs from top to bottom:** G, suboctave G, suboctave G, F. 

5. **False illegal dissonances.** Rearticulations, minims and semiminims doubling the pitch class of the agent, and extremely short notes like fusas are wrongly labelled as illegal dissonances. This is an issue to correct on the dissonance filter. 

Finally, our methodology of re-uploading the file corrected during the experiment, activating the DF, and looking for illegal dissonances left allowed us to catch an error missed by both the experimenter and the CPDL transcriber. Moreover, our methodology of looking for imitative textures allowed us to easily correct this error (see Figure 5). 

## **5. CONCLUSIONS** 

In this paper, we presented a MIR pipeline designed to obtain corrected symbolic scores for the pieces of a set of Guatemalan choirbooks, and we tested it on the first of these books (GuatC 1). We also presented a way to facilitate correcting the results of the last step of this pipeline, the automatic alignment of the mensural voices recognized by the OMR, conducted in the MP Editor. We used the dissonance filter from the humlib library within the MP Editor to highlight illegal dissonances according to the rules of Renaissance counterpoint. Our findings reveal that using the dissonance filter as a counterpoint error marker for the scoring up of Renaissance music facilitated the spotting of scribal errors and even some OMR errors that went undetected in the previous step of the MIR pipeline. Using the MP Editor and the dissonance filter, the user can see the scored-up OMR file, look for the first illegal dissonance 



<!-- Start of picture text -->
71v.jpg.<br>72r.jpg.<br>N<br>72r.jpg. p 72r.jpg, P<br><!-- End of picture text -->

**Figure 5** : Experimenter and CPDL version of the Christe section of Missa10.1_Kyrie0 with the DF turned on. The alto’s A marked by an orange Z label is an undetected error by the experimenter and the CPDL transcriber. Moving this note down to a G results in imitation of the other voices, marked in green boxes. **Clefs from top to bottom:** G, suboctave G, suboctave G, F. 

(i.e., the first orange label in the MP Editor), and evaluate if there is an OMR or a scribal error at or before this point. The use of the DF reduces the correction time (to almost a third) and increases the accuracy of the correction process for pieces written in Renaissance style. Further improvements in the time and accuracy of the corrections could be obtained by improving the DF (i.e., resolving the issue of false illegal dissonances). The DF proved to be sensitive to changes in style, as shown in the eighteenthcentury mass of the corpus that combines Baroque and Renaissance styles. Future work consists of extending the filter to work on non-Renaissance music. 

In conducting this work, the first author has collaborated with the developers of MuRET, MP Editor, and humlib, improving these tools’ support for mensural notation and allowing for their interoperability. Interested students and scholars can use the presented MIR pipeline to retrieve editorial music scores for other mensural sources semiautomatically. The OMR part of the proposed pipeline can be substituted by any other OMR tool for mensural notation (e.g., Aruspix) as long as its output conforms with the input expected by the MP Editor [23]. Although this experiment was small, it already showed promising results. The following steps would include replicating these findings with more musicologists and exploring other counterpoint errors (e.g., parallel perfect intervals). 

## **6. ACKNOWLEDGEMENTS** 

This work draws on research supported by the Fonds de recherche du Québec – Société et culture (FRQSC, Bourse au doctorat en recherche, 13D - Musique, 2019-B2Z261749) and the Social Sciences and Humanities Research Council of Canada (SSHRC). Special thanks to the developers of the various tools involved in the MIR pipeline, 

506 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

David Rizo (of MuRET), Juliette Regimbal (of the MP Editor), and Craig Sapp (of humlib), as they assisted in the process of allowing for the interoperability of these tools. Thanks to Alexander Morgan, who developed the dissonance filter for the Josquin Research Project; to Geneviève Gates-Panneton, who was the experimenter and provided valuable feedback for this paper; and to Professor Peter Schubert, who served as an expert consultant for questions regarding modal counterpoint. Finally, thanks to Timothy de Reuse and Andres Lou for their help in editing this paper. 

## **7. REFERENCES** 

- [1] O. Morales Abril, “Música local y música foránea en los libros de polifonía de las Catedrales de Guatemala y México,” _Jahrbuch für Renaissancemusik: Troja_ , vol. Vokalpolyphonie zwischen Alter und Neuer Welt: Musikalische Austauschprozesse zwischen Europa und Lateinamerika im 16. und 17. Jahrhundert, no. 14, pp. 95–124, 2015. 

- [2] M. E. Thomae, J. E. Cumming, and I. Fujinaga, “Digitization of choirbooks in guatemala,” in _Proceedings of the 9th International Conference on Digital Libraries for Musicology (DLfM)_ . Prague, Czech Republic: Association for Computing Machinery, 2022, pp. 19–26. [Online]. Available: https://doi.org/10.1145/3543882.3543885 

- [3] Y.-H. Huang, X. Chen, S. Beck, D. Burn, and L. Van Gool, “Automatic handwritten mensural notation interpreter: from manuscript to MIDI performance,” in _Proceedings of the 16th International Society for Music Information Retrieval Conference (ISMIR)_ , Málaga, Spain, 2015, pp. 79–85. 

- [4] D. Pujol, “Polifonía española desconocida conservada en el Archivo Capitular de la Catedral de Guatemala y de la Iglesia parroquial de Santa Eulalia de Jacaltenango,” _Anuario Musical_ , vol. 20, pp. 3–10, 1965. 

- [5] R. Stevenson, _Renaissance and Baroque Musical Sources in the Americas_ . General Secretariat, Organization of American States, 1970. 

- [6] R. J. Snow, _A New-World Collection of Polyphony for Holy Week and the Salve Service: Guatemala City, Cathedral Archive, Music MS 4_ , ser. Monuments of Renaissance Music. Chicago: University of Chicago Press, 1996, no. 9. 

- [7] O. Morales Abril, “Catálogo de los acervos musicales del Archivo Histórico Arquidiocesano de Guatemala,” N.D., unpublished. 

- [8] D. Lehnhoff, _Rafael Antonio Castellanos: vida y obra de un músico guatemalteco_ . Universidad Rafael Landívar, Instituto de Musicología, 1994. [Online]. Available: http://www.url.edu.gt/PortalURL/ Biblioteca/Contenido.aspx?o=6708&s=49 

- [9] M. E. Thomae, J. E. Cumming, and I. Fujinaga, “The mensural scoring-up tool,” in _Proceedings of the 6th International Workshop on Digital Libraries for Musicology (DLfM)_ . The Hague, Netherlands: ACM, pp. 9–19. 

- [10] I. Fujinaga, “Single interface for music score searching and analysis (SIMSSA) project: Optical music recognition workflow for neume notation,” in _Proceedings of the Computers and the Humanities Symposium (JinMonCom)_ . Osaka, Japan: Information Processing Society of Japan, 2019, pp. 281–286. 

- [11] I. Fujinaga and A. Hankinson, “Single interface for music score searching and analysis (SIMSSA),” in _Proceedings of the 1st International Conference on Technologies for Music Notation & Representation (TENOR)_ , Paris, France, 2015, pp. 109–15. 

- [12] G. Burlet, A. Porter, A. Hankinson, and I. Fujinaga, “Neon.js: Neume editor online.” in _Proceedings of the 13th International Society for Music Information Retrieval Conference (ISMIR)_ , Porto, Portugal, 2012, pp. 121–126. 

- [13] J. Regimbal, Z. McLennan, G. Vigliensoni, A. Tran, and I. Fujinaga, “Neon2: A Verovio-based squarenotation editor,” in _Proceedings of the Music Encoding Conference (MEC)_ , Vienna, Austria, 2019. 

- [14] C. Wick and F. Puppe, “OMMR4all – A semiautomatic online editor for Medieval music notations,” in _Proceedings of the 2nd International Workshop on Reading Music Systems (WoRMS)_ , Delft, Netherlands, 2019, pp. 31–34. 

- [15] L. X. Pugin, “Editing Renaissance music: The Aruspix project,” _Beihefte zu editio_ , pp. 64–103, 2009. 

- [16] J. M. Iñesta, D. Rizo, and J. Calvo-Zaragoza, “MuRET as a software for the transcription of historical archives,” in _Proceedings of the 2nd International Workshop on Reading Music Systems (WoRMS)_ , Delft, Netherlands, 2019, pp. 12–15. 

- [17] D. Rizo, J. Calvo-Zaragoza, and J. M. Iñesta, “MuRET: A music recognition, encoding, and transcription tool,” in _Proceedings of the 5th International Conference on Digital Libraries for Musicology (DLfM)_ . Paris, France: ACM, 2018, pp. 52–56. 

- [18] J. M. Iñesta, P. J. P. de León, D. Rizo, J. Oncina, L. Micó, J. R. Rico-Juan, C. Pérez-Sancho, and A. Pertusa, “Hispamus: Handwritten Spanish music heritage preservation by automatic transcription,” in _Proceedings of the 1st International Workshop on Reading Music Systems (WoRMS)_ , Paris, France, 2018, pp. 17–18. 

- [19] D. Rizo, N. P. León, and C. S. Sapp, “White mensural manual encoding: from Humdrum to MEI,” _Cuadernos de Investigación Musical_ , no. 6, pp. 373–393, 2018. 

507 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

- [20] P. Roland, A. Hankinson, and L. Pugin, “Early music and the Music Encoding Initiative,” _Early Music_ , vol. 42, no. 4, pp. 605–11, November 2014. 

- [21] K. Desmond, A. Hankinson, L. Pugin, J. Regimbal, C. S. Sapp, and M. E. Thomae, “Next steps for Measuring Polyphony – A prototype editor for encoding mensural music [poster],” in _Proceedings of the Music Encoding Conference (MEC)_ , E. De Luca and J. Flanders, Eds. Boston, MA: Humanities Commons, 2020, pp. 121–124. 

- [22] A. Plaksin and D. Lewis, “Merit: An interactive annotation tool for mensural rhythms,” in _Proceedings of the 9th International Conference on Digital Libraries for Musicology (DLfM)_ . Prague, Czech Republic: Association for Computing Machinery, 2022, pp. 55–59. [Online]. Available: https://doi.org/ 10.1145/3543882.3543888 

- [23] K. Desmond, L. Pugin, J. Regimbal, D. Rizo, C. S. Sapp, and M. E. Thomae, “Encoding polyphony from Medieval manuscripts notated in mensural notation [panel],” in _Proceedings of the Music Encoding Conference (MEC)_ , S. Munich and D. Rizo, Eds. Alicante, Spain: Humanities Commons, 2021. 

- [24] P. Schubert, _Modal counterpoint, Renaissance style_ . Oxford University Press, USA, 2008. 

- [25] M. E. Thomae, “The Guatemalan choirbooks: Facilitating preservation, performance, and study of the colonial repertoire,” in _Christian Music Traditions in the Americas_ , A. Shenton and J. Smolko, Eds. New York: Rowman & Littlefield, 2021. 

508 

