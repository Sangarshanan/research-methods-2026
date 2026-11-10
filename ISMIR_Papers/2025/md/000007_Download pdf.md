---
paper_id: "000007"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706333/files/000007.pdf"
---

# RADIF CORPUS: A SYMBOLIC DATASET FOR NON-METRIC IRANIAN CLASSICAL MUSIC 

Maziar Kanani Sean O’Leary University of Galway TU Dublin 

## James McDermott University of Galway 

```
sean.oleary@tudublin.iejames.mcdermott@universityofgalway.ie
```

```
m.kanani1@universityofgalway.ie
```

### ABSTRACT 

### 1.1 Foundations of Iranian Classical Music 

Non-metric music forms the core of the repertoire in Iranian classical music. Dastg¯ahi music serves as the underlying theoretical system for both Iranian art music and certain folk traditions. At the heart of Iranian classical music lies the radif, a foundational repertoire that organizes melodic material central to performance and pedagogy. 

In this study, we introduce the first digital corpus representing the complete non-metrical radif repertoire, covering all 13 existing components of this repertoire. We provide MIDI files (about 281 minutes in total) and data spreadsheets describing notes, note durations, intervals, and hierarchical structures for 228 pieces of music. We faithfully represent the tonality including quarter-tones, and the non-metric aspect. Furthermore, we provide supporting basic statistics, and measures of complexity and similarity over the corpus. 

Our corpus provides a platform for computational studies of Iranian classical music. Researchers might employ it in studying melodic patterns, investigating improvisational styles, or for other tasks in music information retrieval, music theory, and computational (ethno)musicology. 

### 1. INTRODUCTION 

While ethnic music traditions from around the world have recently gained more attention in computational research, many still lack the necessary datasets to support such studies. Iran, with its rich diversity of ethnic and folk musical traditions, offers great potential for computational analysis that reflects its regional musical identity. 

In this work, we take a step toward addressing this gap by introducing a dataset specifically focused on Iranian non-metric classical music, aiming to support and inspire future studies in this area. We begin by introducing Iranian classical music and its core repertoire, the radif. After reviewing previously published datasets, we present our own dataset in detail. Finally, we provide a statistical and visual overview of the dataset, which can serve as a useful reference for researchers and practitioners. 

> © M. Kanani, S. O’Leary, and J. McDermott. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: M. Kanani, S. O’Leary, and J. McDermott, “Radif Corpus: A Symbolic Dataset for Non-metric Iranian Classical Music”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

Iranian classical music comes from a larger style of music called dastg¯ahi music. This term describes the theoretical framework underlying Iranian classical music and certain styles of Iranian folk music, such as bakhti¯ari. The core repertoire of Iranian classical music is radif (literally "order"), a structured collection of melodies transmitted across generations and foundational to performance and pedagogy. 

Radif is a collection of melodies organized into a specific sequence, typically divided into 12 subcategories (traditionally 13). Out of these, seven are primary subcategories known as dastg¯ah, and five (respectively six) are secondary, referred to as ¯av¯az, which can also be considered as smaller dastg¯ah and serve as subcategories for the primary seven. Each of these subcategories is known for its distinctive characteristics. They are typically recognized based on their main mode (Introduced in the first g¯usheh), the functional roles of their tones within that mode, and the specific sequence of g¯ushehs within them. 

The dastg¯ahs are: shur, seg¯ah, nav¯a, hom¯ay¯un, chah¯arg¯ah, m¯ah¯ur, and r¯astpanjg¯ah. 

The ¯av¯azes are: bay¯at-e-kord, bay¯at-e-tork (also referred to as bay¯at-e-zand), dasht¯ı, ab¯u’at¯a, afsh¯ar¯ı, and bay¯at-e-esfah¯an. 

Among the six ¯av¯azes, bay¯at-e-esfah¯an is a subcategory of the hom¯ay¯un, while the remaining are subcategories of the shur. In many accounts, radif is considered to have 5 ¯av¯azes, as bay¯at-e-kord is often omitted. The reason is that most experts dispute the requirement of recognizing it as a independent ¯av¯az. In this study, we have included bay¯at-e-kord to ensure a complete representation. 

Each of these subcategories comprises pieces called g¯ushehs. These g¯ushehs can range from being as brief as a single sentence to as extensive as a full composition, with performances lasting several minutes. 

G¯ushehs can be divided into three types: modal, melodic, and rhythmic. Modal g¯ushehs are played to introduce a mode as a small framework for improvisation. Melodic g¯ushehs introduce a specific melody and its variations, where that specific melody remains fixed in different performance versions. Rhythmic g¯ushehs represent a specific rhythm and its variations. The same g¯usheh names may appear in different dastg¯ahs or ¯av¯azes. Kereshmeh is a rhythmic g¯usheh that appears multiple times in the radif, sharing the same rhythmic pattern in each case. Another 

60 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

example is haz¯ın, a melody that is performed in different modes; it is classified as a melodic g¯usheh. Qaracheh is an example of a modal g¯usheh that appears in more than one dastg¯ah. 

The term ¯av¯az has three meanings: 1) broadly, it refers to singing; 2) more generally, it refers to Iranian nonmetric music; and 3) more specifically, it signifies the segments of radif that are smaller than a dastg¯ah. This study focuses on the third definition, though the other two meanings are clarified where relevant. 

Non-metric music refers to musical organization that lacks regular meter while potentially maintaining other temporal structures [1]. The distinction between nonmetric music and free-rhythm music centers on the preservation of proportional durational relationships. [2] defines free rhythm as “the rhythm of music without perceived periodic organization,” encompassing music where temporal organization serves non-rhythmic goals such as text transmission or melodic exposition. We consider that nonmetric music maintains relative proportional relationships between note durations despite lacking metrical organization, while free-rhythm music may abandon proportional consistency entirely. 

Tsuge discusses the concept of non-metric music and emphasizes its greater importance in Iranian music compared to other traditions [3]. He explains that the rhythmic structure of ¯av¯az (second definition) music is mainly based on the poetic rhythm system, where a repeating pattern of different number and size of syllables shapes its rhythm. This structure is closely connected to the nature of the Persian (Farsi) language and its classical poetry system which plays a significant role in how the melody is formed and perceived. Kanani and Azadehfar [4] described the key ¯av¯az (second definition) patterns commonly found in nonmetric traditional Iranian vocal music. 

The exact origins of the radif system in Iranian music are not clearly defined. Some sources, like Bruno Nettl, believe it originated in the 17th century, while others suggest the 18th century as the starting point [5–7]. What is clear, however, is that radif developed from the late Safavid era (1670s-1730s) through to the mid-Q¯aj¯ar period (1850s). The lack of precise dating can be linked to the oral tradition of this music and the absence of recording technology at the time. 

It is believed that radif was created to support the teaching of musical modes and to enhance skills in improvisation and modulation within Iranian art music [8]. The same radif can be interpreted differently by different musicians, and once a student becomes a master, they are able to develop their own version of the radif. Over time, many prominent music masters have created their own interpretations, leading to different versions of radif. These musicians developed their radif based on their personal understanding, experience, and expression of Iranian modes, either for their own performances or to teach younger learners. Traditionally, radif was passed down orally from master to student, preserving its legacy and technical details through generations. 

The version of radif curated by musician and educator M¯ırz¯a ’Abdoll¯ah has become the most widely used choice in private lessons, university music education and conservatories over the past century. Initially, it was mainly associated with the t¯ar and set¯ar instruments, but today, it has been adapted and performed on many key Iranian instruments, including kamancheh, sant¯ur, ney, q¯an¯un, o¯ud, and qeychak. 

### 1.2 Exploring Datasets 

In recent years, the creation and sharing of digital music corpora has gained significant attention among researchers in areas such as music information retrieval, computational musicology, and natural language processing. Various studies have demonstrated that well-curated datasets can facilitate analysis of both symbolic and audio musical features, thereby promoting new insights into musical traditions [9,10], styles, and technologies. 

Many music information retrieval (MIR) corpora are primarily audio-based, with annotations for pitch, timing, structural information, etc., e.g. [11, 12], while others are symbolic / score-based. Of the latter, some are based on automated reading of paper scores [13]. Ours differs in that we have manually written the digital score. 

Considering other musical traditions in the geographical region, there is no symbolic corpus available for Arabic Maq¯am music, whereas a symbolic corpus does exist for Turkish Makams, known as SymbTr [14]. 

There are some audio datasets related to these musical traditions, such as the Dunya corpus, which includes Turkish Makam [15], Carnatic, Hindustani [16], Beijing Opera [17], and Arab-Andalusian music [18]. The Dunya corpus is part of a larger project called CompMusic [19]. 

To the best of our knowledge, there was no symbolic corpus available for Iranian music before our previous work, in which we introduced the Shour Corpus [20]. This corpus includes one section of the radif (shur) and was used in our study on discovering patterns and producing meaningful variations through grammatical representation (compression) in this musical style. 

KUG Dastg¯ahi [21] and [22] are two audio datasets for Iranian music. Nava [23] is an audio dataset designed for Iranian instrument recognition, while Ar-MGC is a dataset for Arabic music genre classification [24]. 

### 1.3 Our Contribution 

At the time of writing this paper, to the best of our knowledge, there is no symbolic dataset covering the entire radif. This led us to create the Radif Corpus, which includes all non-metric pieces from M¯ırz¯a ’Abdoll¯ah’s radif. Out of the several transcriptions of M¯ırz¯a ’Abdoll¯ah’s radif, we have selected the edition titled “Radif Analysis - based on the notation of M¯ırz¯a ’Abdoll¯ah’s radif with annotated visual description” by Dariush Talai [25]. This edition consists of a recorded performance, together with a score derived from the performance, notated with hierarchical structure. Although radif also includes some metric pieces, which are usually performed at the end of each dastg¯ah/¯av¯az, our 

61 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

corpus excludes them as we are focusing on non-metric music. Figure 1 presents an example of a transcription from the book. 



<!-- Start of picture text -->
Panjeh she'ri<br>OU hi<br><!-- End of picture text -->

Figure 1. Transcription sample from Dariush Talai’s “Radif Analysis," illustrating the second g¯usheh structure in the shur dastg¯ah. The three white boxes indicate the main structural divisions, while the last white box contains a further sub-division marked in gray. 

In [19], Serra identified five critical criteria for corpora in the CompMusic project: Purpose, Coverage, Completeness, Quality, and Reusability. These are criteria that we also considered in our work. Our purpose has already been stated; Coverage and Completeness are achieved by including an entire radif collection. Regarding Quality, we believe the transcription is accurate, as it has been doublechecked by one of the authors who is an expert in this musical style. Reusability is addressed by providing open data in a documented format. 

This corpus is a resource for MIR, computational musicology, and ethnomusicology, enabling applications such as melodic pattern recognition, automatic transcription, and mode classification. It enables symbolic music generation and AI-assisted improvisation. The dataset also facilitates cross-cultural music studies, allowing for comparative analysis with Turkish Makams and Arabic Maqams, as well as phrase-level examinations of melodic progression. Additionally, its structured format aids computational analysis of non-metric rhythm and hierarchical structure understanding, making it a foundational dataset for exploring Iranian classical music in both traditional and computational domains. 

### 2. RADIF CORPUS DESCRIPTION 

Our corpus includes all these dastg¯ahs/¯av¯azes, featuring 228 non-metric g¯ushehs. The MIDI files contain a total of 43,441 notes, with a total playback duration of approximately 16,825 seconds (about 281 minutes). 

The dataset represents each musical piece as a sequence of notes, where for each note we store microtonal pitch, duration, pitch (quarter tones), interval, MIDI pitch number and MIDI bend. Data formats are csv files and MIDI files, which have been manually transcribed from the book. 

Additionally, we provide MusicXML files converted from the CSV data. These XML files preserve the microtonal pitch information using fractional `<alter>` values following MusicXML 4.0 standards. For non-metric rhythm representation, we use flexible time signatures that accommodate the total duration of each piece. However, we note that some current music notation software implementations show limitations in both microtonal playback and non-metric representation. We observed that quartertones are not played back correctly, and the software tends to generate complex time signatures (e.g., 342/8) as a workaround for representing non-metric music, which, while functional, may not provide an aesthetically ideal notation display. The MusicXML conversion script is included in the repository for researchers who wish to experiment with different notation software or contribute to improving microtonal MusicXML rendering capabilities. These files don’t represent hierarchical structures. 

The dataset includes several figures that are explored further in the continuation of this paper. Our digital version exactly mimics the paper source, while to simplify the dataset and avoid additional complexity, grace notes or ornaments are not included in the dataset. 

The accurate representation of Iranian classical music involves dealing with two main issues: non-metric rhythm and micro-tonal pitch. In the following subsections, we describe our methods to address these challenges. 

Tonality. Notes are symbolized by C, D, E, F, G, A, B, with accidental signs including flat (<sup>Z</sup> ), Koron (k), Sori (s), and sharp (<sup>\</sup> ). Here, “Koron” and “Sori” indicate micro-tonal adjustments specific to Iranian music - quarter tones lower and higher, respectively. 

Chromatic Scale. Although these intervals suggest a 24-quarter-tone chromatic scale per octave, which can be seen in some contemporary compositions, Iranian instruments traditionally employ only 18 specific notes: C, D<sup>Z</sup> , Dk, D, E<sup>Z</sup> , Ek, E, F, Fs, F<sup>\</sup> , Gk, G, A<sup>Z</sup> , Ak, A, B<sup>Z</sup> , Bk, B, with corresponding quarter-tone intervals: 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1, 1. 

MIDI. Pitch bend is a commonly used method for representing microtones in MIDI files in microtonal music styles. To encode Koron, we assign it a MIDI note number one semitone lower than the natural note and a pitch bend, i.e. increase of 2048 (a quarter tone); for Sori, the MIDI note number is the same as the natural, with a pitch bend increase of 2048. 

Octaves. We consider the lowest note in the first g¯usheh 

62 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

of each dastg¯ah/¯av¯az as the start note of the main octave. For example in the first g¯usheh of our corpus the lowest note is F3 so the main octave is from F3 to F4. The music in the main octave is represented only by its symbols and accidental signs (if any are present). For notes in octaves other than the main one, we use ‘+’ or ‘-’ followed by a number to indicate the number of octaves above or below the main octave. For example, an Ak from one octave higher than the main octave would be written as Ak+1. 

Intervals. The Intervals column represents the pitch difference between consecutive notes, with "1" indicating a quarter-tone step. 

Durations. The term non-metric does not mean the same as free rhythm. In this musical style, notes are related to each other through proportional duration differences, with some being longer or shorter than others. These relationships create the rhythmic structure, which is mostly fixed and not altered by the performer. While the exact durations are not strictly defined, they can be categorized into four main types: very short, short, long, and very long. These can be said to correspond to sixteenth, eighth, quarter, and half notes [25] and are numerically represented as 1, 2, 4, and 8 in the corpus, where 1 rhythmic unit is equivalent to 1 sixteenth note. 

Greater Hierarchical Structures. We also documented the hierarchical structure of each piece, as provided in the original printed source (see Figure 1). In our notation, brackets represent hierarchical relationships, forming a tree structure. An open-bracket “[” in the datasheet marks the beginning of a tree node, with following notes representing the contents of a section or subsection until the matching close-bracket “]”. Each tune is enclosed within brackets, representing the root node. Additional pairs of brackets define child nodes, which can themselves contain further subsections, forming a nested hierarchy. 

For example, in Figure 1, the abstract hierarchical structure can be represented as `[ [ ] [ ] [ [ ] ] ]` . The outer brackets enclose the entire tune. The second pair of brackets defines the first section, covering the first three lines in Figure 1. The third pair corresponds to the section spanning lines three to six. The next open bracket is followed by another open bracket, indicating the presence of a subsection, which corresponds to lines eight and nine. The subsection is highlighted in the last line. 

### 3. STATISTICAL AND VISUAL OVERVIEW 

In the dataset, for each g¯usheh, we provide both a pitch histogram and an interval histogram. Figure 2 provides an example of the interval histogram for a g¯usheh. 

Each dastg¯ah or ¯av¯az comes with a spreadsheet giving information about its g¯ushehs, like the number of notes and total duration. Table 1 presents the number of g¯ushehs in each dastg¯ah or ¯av¯az, along with the number of notes, duration in both units and seconds, and pitch range. 

M¯ah¯ur has the highest number of g¯ushehs with 34, followed by chah¯arg¯ah with 31 and shur with 29. It also contains the largest number of notes, with 6104 in m¯ah¯ur, 5788 in chah¯arg¯ah, and 4830 in shur. These three also 



<!-- Start of picture text -->
07 - Gabri<br>5 0<br>4 0<br>3 0<br>2 0<br>1 0<br>0<br>Interval<br>Frequency<br>4 3 2 1 0 1 2 3 4 5 6 7 8 9 0 1 1 1 2 1 3 1 1 4<br><!-- End of picture text -->

Figure 2. Interval histogram of Gabri, a g¯usheh in ab¯u’at¯a 

have the longest durations, with values of 12480, 11606, and 9839 rhythmic units, respectively. 

Afsh¯ar¯ı has the fewest g¯ushehs with 4, followed by bay¯at-e-esfah¯an with 5, and dasht¯ı and bay¯at-e-kord with 6 each. The shortest dastg¯ah/¯av¯az in terms of duration is dasht¯ı, with 1308 notes and a duration of 2685 units, followed by bay¯at-e-kord with 1360 notes and a duration of 2432 units. afsh¯ar¯ı is the third shortest, with 1520 notes and a duration of 2681 units. 

Regarding individual g¯ushehs, kereshmeh in seg¯ah is the shortest g¯usheh in the corpus, while bay¯at-e r¯aje’ va for¯ud in bay¯at-e-esfah¯an is the longest. 

|dastg¯ah/¯av¯az|g¯usheh<br>Count|Number<br>of<br>Notes|Total<br>Duration<br>(unit)|MIDI Perfor-<br>mance Dura-<br>tion(second)|Pitch Range|
|---|---|---|---|---|---|
|Shur|29|4830|9839|1966|[F,A<sup>Z</sup>+2]|
|Bay¯at-e-kord|6|1360|2432|486|[G-1,A<sup>Z</sup>+1]|
|Dasht¯ı|6|1308|2685|536|[F-2,G+1]|
|Bay¯at-e-tork|16|2544|4986|996|[F-1,G+1]|
|Abuata|7|2194|3959|791|[F,A<sup>Z</sup>+1]|
|Afsh¯ar¯ı|4|1520|2681|536|[F-1,A<sup>Z</sup>+1]|
|Seg¯ah|20|3283|6559|1310|[F,F+2]|
|Nav¯a|19|3252|5975|1194|[D-1,C+1]|
|Hom¯ay¯un|27|5323|9780|1954|[D,F+2]|
|Bay¯at-e-esfah¯an|5|1669|3264|652|[D-1,F<sup>\</sup>+1]|
|Chah¯arg¯ah|31|5788|11606|2319|[C-1,G+2]|
|M¯ah¯ur|34|6104|12480|2493|[C-1,G+2]|
|R¯astpanjg¯ah|24|4266|7958|1590|[D-1,C+2]|



Table 1. Summary of g¯usheh information for each dastg¯ah and ¯av¯az, including the number of g¯ushehs, total notes, duration in units and seconds and pitch range. 

### 3.1 Melodic Progression 

One of the main objectives when a musician performs a complete concatenated dastg¯ah is to follow seyr, or melodic movement [26]. In traditional Iranian music, seyr refers to the progression of melodies within a piece, shaping the overall pitch direction of the music through its introduction, development, climax, and resolution. 

Seyr underlines the importance of transitional notes and melodic phrases in establishing the identity and modal character of the piece. These elements play a crucial role in guiding the melodic flow from one section to another, ensuring a coherent and expressive musical journey. 

Each dastg¯ah/¯av¯az folder includes a pitch contour plot to show its seyr. The pitch contour plot illustrates how the melody and pitch evolve across different g¯ushehs. 

63 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
1 .0<br>0 0 0 0 0.028 0 0 0.045 0 0.022 0 0.008 0.007 0 0 0<br>0 0 0 0.006 0.073 0 0 0.269 0 0.174 0.299 0.041 0.034 0 0 0<br>0 0 0.020 0.045 0.123 0.071 0.096 0.179 0 0.239 0.325 0.187 0.123 0 0 0 0 .8<br>0.009 0.028 0.088 0.158 0.162 0.205 0.231 0.194 0.223 0.261 0.156 0.220 0.199 0.056 0.014 0.038<br>0.255 0.280 0.291 0.313 0.263 0.429 0.365 0.119 0.436 0.152 0.091 0.195 0.260 0.249 0.078 0.101 0 .6<br>0.340 0.449 0.355 0.310 0.251 0.232 0.250 0.149 0.277 0.130 0.065 0.220 0.267 0.365 0.310 0.275<br>0.264 0.187 0.207 0.110 0.078 0.054 0.058 0.045 0.064 0.022 0.039 0.106 0.103 0.203 0.381 0.283<br>0.075 0.028 0.032 0.003 0.011 0 0 0 0 0 0.026 0.024 0.007 0.081 0.181 0.199 0 .4<br>0.057 0.028 0.008 0.003 0.011 0.009 0 0 0 0 0 0 0 0.030 0 0.104<br>0 0 0 0 0 0 0 0 0 0 0 0 0 0.010 0 0 0 .2<br>0 0 0 0 0 0 0 0 0 0 0 0 0 0.005 0 0<br>0 0 0 0.052 0 0 0 0 0 0 0 0 0 0 0.036 0<br>0 .0<br>Gusheh<br>G+1<br>F+1<br>Eb<br>D<br>C<br>Bb<br>Ak<br>G<br>Microtonal Pitch F<br>Ek-1 Normalized Frequency<br>D-1<br>F-1<br>01 - Daramad-e Avva l h 02 - Doga 03 - Daramad-e Dovvo m 04 - Daramad-e Sevvo m 05 - Haji Hasan i 06 - Basteh-Nega r 07 - Zangule h 08 - Khosravan i 09 - Naghme h 10 - Feyl i 11 - Shekaste h 12 - Mehraban i 13 - Jameh-dara n 14 - Mehdi Zarab i 15 - Ruh ol- arva h 16 - Qata r<br><!-- End of picture text -->

Figure 3. Heat map of pitch occurrences across 16 g¯ushehs in bay¯at-e-tork ¯av¯az, shown along the time axis, illustrating tonal functionality in each g¯usheh and shifts in the most repeated tone throughout the melodic progression. 

### 3.2 Analyzing the Functionality of Pitches 

One of the other key differences between Iranian classical music and Western music lies in how the central pitch is treated. In Western music, the tonic (or root note) is the main pitch around which a key is built, providing a sense of stability and resolution. In contrast, Iranian music uses the concept of sh¯ahed, a pitch that is emphasized or serves as a focal point within an ¯av¯az or dastg¯ah, but does not necessarily act as the final resting note. The sh¯ahed can shift or be re-emphasized within a dastg¯ah/¯av¯az performance. Additionally, Persian music distinguishes between the sh¯ahed (point of focus), Ist (stops or longer rests through phrases of melody) and Khatemeh (cadential notes), while in Western theory, the tonic usually plays all three roles. Due to these differences, the sh¯ahed and tonic may occasionally coincide, but they represent distinct concepts. Understanding this distinction is essential for analyzing the structure and phrasing of Iranian classical music. We don’t annotate any of these concepts in the dataset as there is some ambiguity in them and they are not provided in the source. 

Fig. 3 shows the frequency of occurrence of each pitch in each tune. This plot can be adapted for studying pitch functionality in each g¯usheh. It also shows how the most repeated pitch has shifted. This heat map can be found in the dataset for each dastg¯ah/¯av¯az. 

### 3.3 Complexity Analysis 

McCormack et al. [27] argue that complexity is fundamental to human creativity and observe that most art occupies a middle ground—neither too simple nor too complex. Our previous works [20, 28, 29] and ongoing research attempt to compare musical complexity across different pieces. We calculated the normalized Pathway Assembly Index (PAI) [30] to assess the complexity of each g¯usheh. The PAI represents the number of steps needed to reconstruct a melody through the binary concatenation of pitches and previous concatenations (e.g., `{a, b, c, d, r} -> ca -> ab -> ra -> cad -> abra -> cadabra -> abracadabra` [30] gives PAI=7). The normalized PAI is the PAI divided by the tune length. 



<!-- Start of picture text -->
0.5 0<br>0.4 8<br>0.4 5<br>0.4 3<br>0.4 0<br>0.3 8 Normalized PAI (Interval)<br>0.3 5 Normalized PAI (Pitch)<br>0.3 3<br>Normalized PAI<br>d Darama Jameh-dara n Bayat-e Raje va Foru d Naghme h Suz-o goda z<br><!-- End of picture text -->

Figure 4. Normalised complexity across bay¯at-e-esfah¯an 

Figure 4 displays the normalized PAI for ¯av¯az bay¯at-eesfah¯an, where we calculate PAI over the tune represented as pitches, and then separately over the tune represented as intervals. Across the dataset, the average PAI is 0.47. Specifically, shur (pitch) shows the highest complexity at 0.51, while afsh¯ar¯ı (pitch) records the lowest at 0.36. Higher complexity means less repetitive patterns. We didn’t observe any consistent trend in complexity within dastg¯ah/¯av¯az. 

### 3.4 Similarity Analysis 

An interesting aspect is the comparison of similarities within each dastg¯ah/¯av¯az and across the entire dataset. We analyzed similarity using normalized Damerau-Levenshtein distance, a method commonly used for melody similarity comparison [31, 32]. Specifically, pitch sequences were compared within each dastg¯ah/¯av¯az, and interval sequences were used for comparisons across the entire dataset. This approach helps to limit the effects of musical transposition and identifies similar motifs’ movements that appear in different sections of the radif. 

Figure 5 presents a similarity matrix for the 228 g¯ushehs in the dataset, with corresponding matrices for each individual dastg¯ah/¯av¯az available in the corpus.<sup>1</sup> 

We added horizontal and vertical lines to visually sep- 

> 1 High-resolution version of the similarity matrix: `https:// limewire.com/d/IXH5G#ZUZyGVbiqi` 

64 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
Shou r<br>Bayat-e-kor d<br>Dasht i<br>Bayat-e-Tor k<br>Abuat a<br>Afshar i<br>Sega h<br>Nav a<br>Homayou n<br>Bayat-e Esfaha n<br>Chaharga h<br>Mahou r<br>Rast Panjga h<br>Shou r Bayat-e-kor d Dasht i k Bayat-e-Tor Abuat a Afshar ih Sega Nav a Homayou n Bayat-e Esfaha n Chaharga h Mahou r Rast Panjga h<br><!-- End of picture text -->

Figure 5. Similarity matrix across the corpus. Light colours indicate high similarity. 

arate each dastg¯ah/¯av¯az. This figure highlights notable musical resemblances: the short diagonal lines e.g. near bottom-centre indicate strong similarities among some g¯ushehs in chah¯arg¯ah and seg¯ah, as well as among some in hom¯ay¯un and r¯astpanjg¯ah. 

The large square block in the top-left corner suggests that all dastg¯ahs/¯av¯azes within that region (from sh¯ur to nav¯a) share significant similarities. Furthermore, the figure effectively illustrates the self-similarity within most dastg¯ah/¯av¯az. All except hom¯ay¯un form distinct blocks along the diagonal line that represent these internal similarities. The block in the bottom-right confirms the similarity between m¯ah¯ur and r¯astpanjg¯ah. 

A prominent point along this diagonal corresponds to several g¯ushehs with strong mutual resemblance. In hom¯ay¯un, several g¯ushehs are named after nor¯uz (nor¯uz ‘arab’, nor¯uz sab¯a, and nor¯uz kh¯ar¯a), and parts of these are highly similar. These findings could pave the way for further studies based on these musical similarities matrices in future research. 

allowing for reuse and adaptation with proper credit. Researchers are encouraged to cite this paper when using the dataset in academic or creative work. 

### 5. CONCLUSION 

In this paper, we have introduced the Radif Corpus, a comprehensive symbolic dataset for Iranian classical music that covers all 13 dastg¯ah/¯av¯az of this tradition, specifically the non-metric pieces from M¯ırz¯a ’Abdoll¯ah’s radif. This dataset addresses the non-metric core of Iranian art music by documenting microtonal pitch, melodic progressions, and hierarchical structures across 228 pieces. By offering detailed annotations in both MIDI and CSV formats, the Radif Corpus provides a valuable platform for research in music information retrieval, music theory, and computational (ethno)musicology. We hope it will inspire future explorations of Iranian classical music and serve as a foundational resource for advancing analytical and creative studies in this domain. 

### 4. AVAILABILITY AND ACCESS 

The Radif Corpus is openly available on Zenodo under the DOI: 10.5281/zenodo.15742125. It includes the musical data in CSV MIDI, and MusicXML formats. In addition, it contains supporting figures, pitch and interval histograms, pitch contour plots, and similarity matrices for eachdastg¯ah and ¯av¯az. 

### 6. ACKNOWLEDGMENTS 

This work was conducted with the financial support of the Research Ireland Centre for Research Training in Digitally-Enhanced Reality (d-real) under Grant No. 18/CRT/6224. For the purpose of Open Access, the author has applied a CC-BY public copyright license to any Author Accepted Manuscript version arising from this submission. 

All materials are released under a CC-BY 4.0 license, 

65 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

### 7. ETHICS STATEMENT 

Our work uses publicly available music corpora and does not involve human participants directly. The music collection is part of the Iranian classical music tradition, which is not itself owned or copyrighted by any individual composer. The edition we have used is used by permission of the author. 

This musical tradition is culturally important, and we have tried to be respectful and careful in how we talk about it and use it. 

The authors declare no conflicts of interest. 

### 8. REFERENCES 

- [1] F. Lerdahl and R. Jackendoff, A Generative Theory of Tonal Music. Cambridge, Mass.: MIT Press, 1983. 

- [2] M. R. L. Clayton, “Free rhythm: Ethnomusicology and the study of music without metre,” British Journal of Ethnomusicology, vol. 5, no. 1, pp. 323–334, 1996. [Online]. Available: https://oro.open.ac.uk/17650/1/ FreeRhythm.pdf 

- [3] G. Tsuge, “Rhythmic aspects of the âvâz in Persian music,” Ethnomusicology, pp. 205–227, 1970. 

- [4] M. Kanani and M. R. Azadehfar, “Study of tahrir patterns in Iranian classical Radif music based on Mohammadreza Shajarian’s performance,” 2020. 

- [5] B. Nettl, “Music of the Middle East,” Excursions in world music, pp. 54–87, 2012. 

- [6] L. Miller, “The Radif of Persian music, studies of structure and cultural context in the classical music of Iran,” 1993. 

- [7] D. Talaei, A New Approach to the Theory of Persian Music. Tehran, Iran: Mahoor, 1993. 

- [8] H. Farhat, The Dastg¯ah Concept in Persian Music. Cambridge University Press, 2004. 

- [9] C. Papaioannou, I. Valiantzas, T. Giannakopoulos, M. Kaliakatsos-Papakostas, and A. Potamianos, “A dataset for Greek traditional and folk music: Lyra,” arXiv preprint arXiv:2211.11479, 2022. 

- [10] R. De Valk, R. Ahmed, and T. Crawford, “JosquIntab: A dataset for content-based computational analysis of music in lute tablature.” in ISMIR, 2019, pp. 431–438. 

- [11] D. Foster, S. Dixon et al., “Filosax: A dataset of annotated jazz saxophone recordings,” 2021. 

- [12] P. Beauguitte, B. Duggan, and J. D. Kelleher, “A corpus of annotated Irish traditional dance music recordings: Design and benchmark evaluations,” 2016. 

- [13] P. Polykarpidis, D. Kalofonos, D. Balageorgos, and C. Anagnostopoulou, “Three related corpora in middle Byzantine music notation and a preliminary comparative analysis.” in ISMIR, 2022, pp. 306–313. 

- [14] M. K. Karaosmano˘glu, “A Turkish makam music symbolic database for music information retrieval: SymbTr,” in Proceedings of 13th International Society for Music Information Retrieval Conference; 2012 October 8-12; Porto, Portugal. Porto: ISMIR, 2012. p. 223–228. International Society for Music Information Retrieval (ISMIR), 2012. 

- [15] B. Uyar, H. S. Atli, S. ¸Sentürk, B. Bozkurt, and X. Serra, “A corpus for computational research of Turkish Makam music,” in Proceedings of the 1st International Workshop on Digital Libraries for Musicology, 2014, pp. 1–7. 

- [16] A. Srinivasamurthy, G. K. Koduri, S. Gulati, V. Ishwar, and X. Serra, “Corpora for music information research in Indian art music,” Proceedings of the ICMC/SMC Conference, pp. 1029–1036, 2014. 

- [17] R. C. Repetto and X. Serra, “Creating a corpus of Jingju (Beijing opera) music and possibilities for melodic analysis.” in ISMIR, 2014, pp. 313–318. 

- [18] M. Sordo, A. Chaachoo, and X. Serra, “Creating corpora for computational research in Arab-Andalusian music,” in Proceedings of the 1st International Workshop on Digital Libraries for Musicology, 2014, pp. 1–3. 

- [19] X. Serra, “Creating research corpora for the computational study of music: The case of the CompMusic project,” in Audio engineering society conference: 53rd international conference: Semantic audio. Audio Engineering Society, 2014. 

- [20] M. Kanani, “Grammatical structure and grammatical variations in non-metric Iranian classical music,” AIMC 2024 (09/09-11/09), 2024. 

- [21] B. Nikzat and R. Caro Repetto, “Kdc: An open corpus for computational research of Dastg¯ahi music,” in Proceedings of the 23rd International Society for Music Information Retrieval Conference, 2022. 

- [22] P. Heydarian and J. D. Reiss, “A database for Persian music,” in Proc. of the Digital Music Research Network Summer Conference (DMRN 2005), 2005. 

- [23] B. Baba Ali, A. Gorgan Mohammadi, and A. Faraji Dizaji, “Nava: A Persian traditional music database for the dastg¯ah and instrument recognition tasks,” Advanced Signal Processing, vol. 3, no. 2, pp. 125–134, 2019. 

- [24] L. Almazaydeh, S. Atiewi, A. Al Tawil, and K. Elleithy, “Arabic music genre classification using deep convolutional neural networks (cnns).” Computers, Materials & Continua, vol. 72, no. 3, 2022. 

- [25] D. Talai, Radif Analysis Based on the Notation of Mirza Abdollah’s Radif With Annotated Visual Description. Tehran, Iran: Ney, 2015. 

66 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [26] M. Chalesh and H. Asa’di, ““seyir” in Persian classical music (case study: Darâmad-e avâz-e bayâteesfahân),” Journal of Fine Arts: Performing Arts & Music, vol. 22, no. 2, pp. 81–91, 2017. 

- [27] J. McCormack, C. Cruz Gambardella, and A. Lomas, “The enigma of complexity,” in Artificial Intelligence in Music, Sound, Art and Design: 10th International Conference, EvoMUSART 2021, Held as Part of EvoStar 2021, Virtual Event, April 7–9, 2021, Proceedings 10. Springer, 2021, pp. 203–217. 

- [28] M. Kanani, S. O’Leary, and J. McDermott, “Graphbased mutations for music generation,” in Proceedings of the Companion Conference on Genetic and Evolutionary Computation, 2023, pp. 1916–1919. 

- [29] M. Kanani, S. O’Leary, and J. McDermott, “Parsing musical structure to enable meaningful variations,” in 

AIMC 2023 (forthcoming): The International Conference on AI and Musical Creativity, Sussex, UK, 30th August–1st September, 2023. 

- [30] S. M. Marshall, D. Moore, A. R. Murray, S. I. Walker, and L. Cronin, “Quantifying the pathways to life using assembly spaces,” arXiv preprint arXiv:1907.04649, 2019. 

- [31] G. Gillen and J. McDermott, “FONN: Folk N- gram aNalysis,” 2021. [Online]. Available: https: //doi.org/10.5281/zenodo.5768216 

- [32] “D3.2 analysis of music repositories to identify musical patterns (v1.0),” Polifonia Project, Tech. Rep., 2022. [Online]. Available: https://polifonia-project.eu/wp-content/uploads/ 2022/07/Polifonia_D3.2_V1.0.pdf 

67 

