---
paper_id: "000036"
year: 2022
title: "Download pdf"
source_url: "https://zenodo.org/record/7316656/files/000036.pdf"
---

THREE RELATED CORPORA IN MIDDLE BYZANTINE MUSIC NOTATION AND A PRELIMINARY COMPARATIVE ANALYSIS 

Polykarpos Polykarpidis<sup>1</sup> Dionysios Kalofonos<sup>2</sup> Dimitrios Balageorgos<sup>1</sup> Christina Anagnostopoulou<sup>1</sup> 1 Department of Music Studies, National and Kapodistrian University of Athens, Greece 2 Independent researcher, Manchester, UK 

polpol@music.uoa.gr, peitemou@gmail.com, dbalageorgos@music.uoa.gr, chrisa@music.uoa.gr 

# ABSTRACT 

The Middle Byzantine notation (MBn) is used to capture the plainchant melodies of eastern Orthodox Christian music from the middle of the 12th century until 1814. In the context of this research, we study the evolution of a subgenre of Byzantine music known as Heirmologic. We present three Heirmologic corpora spanning the periods before, during and after the 16th century. We discuss the challenges we faced during the digitisation process, and the steps we took to overcome them. For the analysis of the three corpora, we apply the three methods, namely notational texture, melodic arch similarity, and JensenShannon distances of Markovian models, the second of which is novel and inspired by the idea of melodic arches [1, 2]. Through these methods, we aim at highlighting the differences of the corpora in order to obtain an outline of the evolution of the subgenre. We observe that the post16th century Heirmologic pieces are more similar to the 16th century ones, while there is a greater difference with the pre-16th century pieces. This indicates that the 16th century constitutes a turning point in the melodic features of the Heirmologic subgenre. 

# 1. INTRODUCTION 

Byzantine music has a known history of 2000 years and it constitutes a part of the human world heritage [3]. Roughly, the first millennium is characterised as prenotational period, while the second as notational period [4]. It was mainly developed in the Eastern Byzantine Empire and up to this day has been influencing the cultures of the Southeast and Eastern Europe, and parts of the Caucasus regions. It has also influenced, among others, the Western and the Slavic music [5,6]. 

The Middle Byzantine notation (MBn) is used to capture the plainchant melodies of Byzantine music from the middle of the 12th century until 1814 [7]. At the moment 

> © P. Polykarpidis, D. Kalofonos, D. Balageorgos, and C. Anagnostopoulou. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: P. Polykarpidis, D. Kalofonos, D. Balageorgos, and C. Anagnostopoulou, ªThree related corpora in Middle Byzantine music notation and a preliminary comparative analysisº, in Proc. of the 23rd Int. Society for Music Information Retrieval Conf., Bengaluru, India, 2022. 

of writing, the cataloged manuscripts of Byzantine music are numbered approximately 10,000, most of them written in MBn [8]. The absence of MBn corpora prevents the computational process of this music genre and makes impossible any cross-cultural research, what is described in [9,10]. Previous attempts have been made to transcribe Byzantine music into staff notation, but they were rejected due to loss of the information that is rooted in the symbols’ orthography [7]. 

We present three related corpora of MBn scores which are part of the Knowledge Representation presented in [11]. The corpora are available to MBn researchers as well as to the wider musicological community [12]. These corpora are used in a study to outline the evolution of the Heirmologic subgenre of Byzantine music that took place in the 16th century. For this reason, we present a preliminary comparative analysis of the corpora. 

This paper is organised as follows. Section 2 introduces the Heirmologic subgenre that the pieces of the corpora belong to, the manuscripts that the corpora consist of, and the reason why we study them. It closes with the discussion on the challenges in the digitisation and how we dealt with them. Section 3 presents the methods we applied for the musicological analysis of the corpora. Section 4 presents the results of the analysis. This paper closes with section 5 which discusses our results. 

# 2. THE THREE CORPORA 

Byzantine music consists of three subgenres: Heirmologic, Sticheraric, and Papadic. The subgenre of a Byzantine music piece depends on the poetic form of its lyrics<sup>1</sup> . Generally, Byzantine music compositions of a hymn are influenced by (a) the subgenre that the hymn belongs and (b) the preceding compositions of the same hymn (different melodies using the same lyrics). Regarding point (b), Manuel Chrysaphes (15th century) in his treatise [14, pp. 44±47], states that new compositions of Hymns follow the music of the preceding compositions of these Hymns. Since music can be expressed as a series of viewpoints, 

> 1 Specifically, the Heirmologic music pieces (called Heirmoi) use lyrics that belong to the poetic form of Kanon [7, 13]. At a high level, a Kanon consists of a number of stanzas, some of which work as model melodies. These stanzas are called Heirmoi (singular: Heirmos). The remaining stanzas of Kanon follow the melodies of the Heirmoi [7]. The book that contains the Heirmoi is called Heirmologion. 

306 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

we explore this observation and we model the similarity of the corpora through the distances of their respective viewpoints. 

In the context of this research, we study the evolution of the Heirmologic subgenre. Using the Knowledge Representation (see section 2.5), we focus our attention on the Heirmologions of 16th century, and specifically the Karykis Heirmologion. This selection is not random. According to the existing historical research, in the 16th century a great change happened to the melodies of the Heirmologion [13,15,16]. In order to study the Karykis’ Heirmologion and to evaluate its contribution to the tradition, we select the Heirmologions of pre-Karykis, Karykis and post-Karykis. 

# 2.1 A representative sample of Heirmologion of pre-Karykis era 

In our research we evaluate the contribution of Karykes’ Heirmologion in the context of tradition. As a representative example of the previous tradition, the Heirmologion of manuscript 1101 from the Iveron (mount Athos) library was chosen. This Heirmologion was written somewhere between 1535-1540 by the monk Pachomius Rousanos [17]. 

There are several reasons for choosing Rousanos’ Heirmologion as a representative of the pre-Karykis era: (a) the Rousanos’ Heirmologion follows the prevailing tradition of the subgenre, (b) it is dated close to Karykis’ era, (c) Rousanos was a well-known lettered monk, who had a good knowledge of both notation and theory, so his manuscripts are considered reliable sources. 

# 2.2 A representative sample of Karykis’ Heirmologion 

So far, no autograph of Karykis’ Heirmologion has been identified. From various copies of the Karykis’ Heirmologion, the Iveron 1167 was chosen for these analyses. This manuscript dates to the early 17th century. 

# 2.3 A representative sample of Heirmologion of post-Karykis era 

As a representative example of the post-Karykis tradition, we take the Balasis’ Heirmologion of Sinai 1433 (Jerusalem). This Heirmologion was written in 1690 by Kosma the Macedonian [18]. In the period between the Balasis’ and Karykis’ Heirmologions, appeared also some other Heirmologion anthologies. However, based on the number of copies, Balasis’ Heirmologion was especially popular among the post-Karykis’ Heirmologions. Therefore, the next main tradition of the Heirmologion subgenre is considered to be that of Balasis. Regarding the choice of the copy, Kosmas the Macedonian was a peer of Balasis in music studies and his manuscripts are considered to be a reliable source [19]. 

# 2.4 Corpora 

Having defined the previous and the next tradition of the Karykis’ Heirmologion, it becomes possible to create three 

corpora that represent these traditions. Specifically, 128 Heirmoi were received from each Heirmologion. The sample is evenly distributed in terms of Echoi (modes): 16 Heirmoi per Echos. The same Heirmoi were taken from each corpus, i.e., the same text (lyrics) composed by different composers. This sample is approximately 25% of the number of Heirmoi contained in each Heirmologion. 

# 2.5 Knowledge Representation 

The Knowledge Representation we use is a tree structure capturing the viewpoints [20, 21] of the music piece. In our case, these viewpoints are the syllable, interval, pitch, and voiced sign. The syllable is the viewpoint that captures in a sequential form the syllables of the lyrics. The interval and pitch viewpoints capture the information that provides us with the Metrophonia<sup>2</sup> of the piece (i.e., basic melodic line without duration information). The voiced sign viewpoint captures the aspect of the notation that provides us with the Metrophonia. Naturally the tree captures the relations of the viewpoints and their sequence in the music piece. Exploiting the structure of the tree, the researcher can then perform a computational analysis of the properties of the music piece. Moreover, the researcher can post-process the tree to highlight specific properties of the music piece by reorganising the connections of the viewpoints. For more information see [11]. 

# 2.6 Digitisation challenges 

During the process of digitisation of the music pieces, we were faced with a number of challenges. Firstly, notational errors in the manuscripts due to the scribe is a common issue. Such errors are identified through the Metrophonia of the notation and are corrected by comparing these excerpts containing the error with similar excerpts from other manuscripts. For the pre-Karykis Heirmologion (manuscript Iveron 1101), the following manuscripts were used for the corrections: Grottaferrata EgII [22], Sinai 1256 [23] and Iveron 1185 [24]; for Karykis Heirmologion (manuscript Iveron 1167) manuscripts Iveron 1154, Iveron 1155 and Iveron 1231 were used [24]; and for post-Karykis Heirmologion (manuscript Sinai 1433) manuscripts NLG 946, NLG 936 and NLG 967 were used [25]. All the imposed corrections are documented within the corpus (GitHub link). 

Secondly, the signs of MBn are grouped into two main categories: Voiced signs and Voiceless signs. One of the uses of the latter is to group the former. Many times it does not seem clear which Voiced signs the Voiceless signs are grouping (e.g., Figure 1). This ambiguity particularly concerns the Heirmologions of Karykis’ era and onwards. This problem does not have a unique solution and individual rules may apply. A general principle that we followed in our corpora was that Voiceless signs group all the Voiced signs in a syllable. Also, sometimes we juxtaposed the am- 

2 Although the interpretation of this notation remains an open question, the basic melodic line as evidenced by the signs (called Metrophonia) is unquestionable. 

307 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



Figure 1. The top excerpt is from the Heirmologion of the manuscript Iveron 1167 f 4r, while the bottom is the same excerpt from the Heimrologion of the manuscript Iveron 1155 f 4r. As can be seen, the same Voiceless sign (red with a green border) spans several Voiced signs (black) in the two manuscripts. 

biguous excerpts from corresponding manuscripts to locate a kind of pattern. 

Thirdly, at a higher level, the MBn can be understood as a sequence of signs that indicate intervals. The pitches of these intervals are determined by a series of specific signs which are always placed at the beginning of the pieces. This group of signs is called Martyriai. Choosing a pitch as representative of each Martyria is not always straightforward [26]. The choices made in the specific music pieces are such as to facilitate the comparison of the three corpora. 

Fourthly, our Knowledge Representation gives us the ability to capture the melodic phrases of each piece. The choice of end points of music phrases is not objective. In order to be consistent with our choices across the corpora, we have created a set of general rules and separation preferences. 

Rule 1.1: Phrases are separated in the last syllable of a word. Rule 1.2: Phrases are separated in the last syllable of an Enclisis group (linguistic term). Rule 2.1: The last syllable of the phrase usually contains at least one of the following signs<sup>3</sup> : Diple Apostrophos, Diple, Apoderma, Kratema (rarer), Klasma (rarer). Rule 2.2: The penultimate syllable of the phrase can have the Koufisma sign. Rule 2.3 (intuitive): The last syllable of the phrase may have one of the following compound signs: Omalon, Piasma, and Vareia. Rule 3: There should be a colon and/or a comma in the lyrics of the music text. Rule 4 (tendency): Small phrases rather than large ones are preferred. Rule 5: The Martyriai appearing mid-text usually separate phrases. 

# 3. METHODS OF COMPARISON 

In order to draw an outline of the evolution of the Heirmologic subgenre of Byzantine music, we use three methods to capture the differences of some aspects of the corpora: Notational texture (method 1), similarity of the melodic arches (method 2), and distances of Markovian models of the attributes (method 3). 

> 3 These are the names of the signs of MBn that etymologically come from Greek words [7]. 

# 3.1 Method 1: notational texture. 

In plainchant music (e.g., Byzantine, Gregorian, Mozarabic etc.) a characteristic of the style of a piece is its average number of notes, time beats, or signs per syllable [27±33]. Based on this characteristic, we can cluster the music pieces into three categories: syllabic, neumatic, and melismatic. In order to eliminate any ambiguities in these categories, we define two types of texture: Notational and Durational texture. Notational texture of a corpus is defined as the average number of pitches or of signs on a syllable, while Durational texture of a corpus is defined as the average number of durations per syllable. When the average number of the measured quantity (pitch, duration, signs etc.) of a corpus is between 1 and 2, then the texture of the corpus is characterized syllabic, when it is between 2 and 4 then the texture of the corpus is characterized neumatic, and when it is 4 or more then the texture of the corpus is characterized melismatic. Hence, a music corpus in terms of pitch can belong to syllabic style, while in terms of duration can belong to neumatic style. The interpretation of the MBn in terms of the duration of the syllables remains an open question. Consecutively, as the music pieces considered in this research are written in MBn, our measurements cover the notational texture. 

All the pieces of our corpora belong to Heirmologic subgenre. This means that the general notational texture of these three corpora is syllabic. Nevertheless, through this measurement we can obtain a more subtle distinction of the notational texture of the syllables as examined by Troelsgard [30]. Specifically, we measure the number of pitches per syllable, notational_texture =<sup><mark>|</mark>voiced</sup><sup><mark>_</mark>units</sup><sup><mark>|</mark></sup> <mark>.</mark> |syllables| 

# 3.2 Method 2: similarity of the melodic arches 

As we discussed in section 2, tradition plays an influential role in the composition of a hymn. In this research, we are interested in (a) identifying the areas where the new compositions follow the tradition, (b) the areas where the new compositions diverge from the tradition, and (c) quantify the divergence of the new and prior compositions. 

Plotting the melodic lines of the different compositions of the same poetic verses lined up by syllable, we observe that the compositions usually present similar melodic shapes in corresponding areas (Figure 2). Based on this observation and inspired by the idea of melodic arches [1,2], we create a novel method that, given two melodies of the same number of syllables, returns a percentage of similarity of their melodic arches. The design of this algorithm is driven by (a) the fact that the compositions in Byzantine Music are rooted on the syllables of the lyrics, (b) the duration of the pitches is unknown, and (c) the need for the derivation of a comparison metric instead of a metric for the identification of a dominant melodic arches [1]. 

The algorithm consists of three phases, (a) the plotting of the pitches (Algorithm 1), (b) the extraction of the arches (Algorithm 2), and (c) the comparison of the arches of the melodic lines (Algorithm 3). 

Given two music pieces, the algorithm extracts the pitches, and plots them on a two dimensional grid (Algo- 

308 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



Figure 2. The melodic line of the first 30 syllables of Heirmos ‘Theio kalyptheis’ by the two compositions (Iveron 1101 and Iveron 1167). The x-axis represents the syllables, where at x=0, the value of y is the Martyria, i.e., the initial pitch (see [11]). The y-axis represents the steps (pitches). 

rithm 1). The two pieces are aligned by syllables, and are of equal length. As a result, the pitches give us a view of the shape of the melodic lines, and highlights the similarities and differences of the compositions (Figure 2). 

In the next phase the algorithm extracts the arches that are formed by the pitches (Algorithm 2), i.e. shape of the melody. Using these arches, we translate the two melodies into sequences of two types of arches: convex and concave. 

In the final phase, the algorithm compares the compositions through their arches (Algorithm 3). When two areas are translated into the same arch type, they are considered to be similar. When two areas are translated into different arch types, they are considered to be dissimilar. When the areas cannot be translated into arches, they are classified as dissimilar due to different shapes. 

When the arch of one melodic line corresponds to more than one arches of the other, the former is compared with the second degree polynomial regression of the latter. The second degree polynomial will give us a curve that is either convex or concave. Through the comparison of the two melodic lines, we obtain (a) the degree of similarity, (b) the degree of dissimilarity due to difference arches, and (c) the degree of dissimilarity due to difference shapes (Figure 3). 

# 3.3 Method 3: distances of Markovian models of the attributes 

As a third method, we capture the viewpoints as sequences (n-grams). We apply Markovian models on the n-grams to examine the divergence of the corpora. The melodic features of the notation are those that refer directly to the basic melodic line of the chant: pitch, interval, voiced unit. The information carried by the first two attributes is identical to that of the western staff. Voiced units are those that encapsulate the music information of the main melodic line as it is imprinted on the other two features (pitch, interval). In essence, the voiced unit attribute concerns the sign itself as it is imprinted in the score, while the pitch and the interval concern the aspects of the melody that the voiced units indirectly indicate (signified and signifier). 

From the pitch and interval we also extract three others features which are redundancies of the melodic line: general syllabic pitch, general syllabic interval, and melodic 

Al <mark>g</mark> orithm 1 Pitch <mark>p</mark> lottin <mark>g</mark> al <mark>g</mark> orithm. 

- 1: Let syllables be the sequence of syllables of a music piece. 

- 2: Let pitches be the sequence of pitches of a music piece. 

- 3: Let f<sup>assoc</sup> : syllablek → pitchesk where pitchesk is the sequence of pitches associated with syllablek and pitchesnk is the nth pitch of pitchesk. 

- 4: Let f<sup>pos</sup> : syllable<sup>n</sup> i=1<sup>→Z+bethemappingofthe</sup> position of a syllable i in the sequence of the music piece to positive integers, this mapping defines the values of the x-axis. 

- 5: ∀n ∈ [ 1, |pitchesk| ] where pitchesk = f<sup>assoc</sup> (syllablek), we plot the points, P = { (x, y) : x = f<sup>pos</sup> (syllablek−1) + n/|pitchesk|, y = pitchesnk }. Point (x0, y0) is reserved for the initial pitch given by a special sign known as Martyria. 

- 6: Create an abstraction by removing the embellishments, in the context of syllable, from the melodic line, defined as P<sup>−</sup> = {(x, y) : (x, y) ∈ P, x ∈ Z<sup>+</sup> }, i.e. for every syllable keep the last pitch. 

- 7: For each pair of points in P<sup>−</sup> , we identify the melodic contour (i.e., step up or down). Zero intervals inherit the melodic contour of the previous pair, hence they do not change the melodic contour. 

contour of syllable. For the general syllabic pitch, instead of extracting every pitch from every sign of the syllable, we extract only the last pitch of the syllable. For the general syllabic interval, instead of extracting every interval from every sign of the syllable, we extract the sum of all intervals of the syllable. For the melodic contour of the syllable, we extract the values (−, +, 0), which describe the contour of the general syllabic interval. 

Using our Knowledge Representation [11], the corpora is translated into sequences of values based on the logic of viewpoints [20, 21]. For the aforementioned viewpoints, we train Markov models of different order, and we measure the distance of the models using the Jensen-Shannon distance (i.e., the square root of the Jensen-Shannon divergence) [34,35]. To tackle the zero-probability problem we use Laplace smoothing [36]. 

Markov models express the probability of an n-gram appearing in the corpus. However, Markov models do not capture the position of the n-gram in the corpus and since we are restricted to low order Markov models due to overfitting, two different corpora can theoretically result in the same probability distribution. As we are using this method to find the relation of two corpora, we apply it both on the detailed dataset that reflects the music surface and on a simplified dataset that has a single value associated with each syllable. Since the corpora contain the same lyrics and in the simplified dataset every syllable has one value (one pitch, one interval, or one contour), the n-grams span the same regions for both melody and lyrics. 

Furthermore, since the divergence is derived from the 

309 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

# Al <mark>g</mark> orithm 2 Arch extraction al <mark>g</mark> orithm. 

- 1: Let α = (start, peak, end, shape) be an arch, where start, peak, end ∈ P<sup>−</sup> and shape ∈{CONV EX, CONCAV E}. 

- 2: Let point x be the starting point, then start<sup>α</sup> = x. 

- 3: Find xi such that all pairs in the range [x, xi] have the same contour or zero intervals, then peak<sup>α</sup> = xi. 

- 4: Find xj such that all pairs in the range [xi, xj] have the same contour or zero intervals, then end<sup>α</sup> = xj. 

- 5: Set shape<sup>α</sup> = CONCAV E when start<sup>α</sup> < peak<sup>α</sup> , otherwise shape<sup>α</sup> = CONV EX. {Since zero intervals do not change the contour, the arch will include zero intervals.} 

Markov tables, and since we are using it for comparison, we make sure that the Markov tables of the corpora under comparison consist of a common set of n-grams, spanning the union of the set of symbols found in the corpora under comparison. As such, the divergence reflects the distance of the probability distributions over a single set of n-grams. 

We study n-grams between the orders of 2 and 4, and favour higher orders until the point where all lines show decrease due to over-fitting. As we are interested in the comparison of the corpora, higher orders with the same probability indicate areas of similarity between the corpora. However, with higher order Markov, we tend towards the scenario where an n-gram appears once in one corpus and not the other, the Markov table is dominated by noise due to smoothing, and Jensen-Shannon distance reflects the noise rather than the relation of the data. 

Finally, the absolute values of the Jensen-Shannon distance are not meaningful without a reference. As we are studying the distances of corpora, we need a reference in order to quantify the magnitude of their distance. For this reason, we make use of a case study corpus consisting of 16 Heirmoi in first echos which have the property that the 8 pre-Karykis<sup>4</sup> and 8 Karykis<sup>5</sup> Heirmoi belong to the pre-Karykis’ music style. Generally, Karykis changes the compositional style in first echos, but for some reason, he keeps the previous style (pre-Karykis) for only these 8 Heirmoi. This is confirmed by the similar cadential pitches and pitch profiles, the highest melodic arch similarity (similar arches 84.4%, dissimilar arches 12.9% and dissimilar shapes 2.7%), and low Jensen-shannon distance (gray line in Figures 4 & 5). For these reasons, we consider the distance of these case study corpora as a threshold for similarity. 

# 4. RESULTS 

Table 1 presents the notational textures (i.e. the number of voiced units per syllable) of the three corpora. The three corpora show a syllabic notational texture. We observe that Karykis tends even closer to compose Heirmos with absolute syllabic notational texture (i.e., near to 1). 

> 4 Manuscript Iveron 1101, folios 7v-9r 

> 5 Manuscript Iveron 1167, folios 138r-141v 

# Al <mark>g</mark> orithm 3 Arch com <mark>p</mark> arison al <mark>g</mark> orithm. 

- 1: Let A and A<sup>′</sup> be the sequences of arches of the two melodic lines under comparison. ̸ = ∅<sup≯</sup> 

- 2: while A̸ = ∅ and A<sup>′̸</sup> = ∅ do 

- 3: Let α1 be the first arch in A, and α1<sup>′be the first arch</sup> in A<sup>′</sup> . 



<!-- Start of picture text -->
4: Let L = ∅, R = ∅.<br>5: if start α1 < start α 1 ′ then<br>6: L = {α1}.<br>7: R = {αn ′ ∈ A′ : endα n ′ ≤ end α1 }.<br>8: else if start α1 > start α 1 ′ then<br>9: L = {α1 ′ }.<br>10: R = {αn ∈ A : end αn ≤ end α 1 ′ }.<br>11: else<br>12: L = {α ∈ A : end α ≤ max<br>α ′′ ∈{α1,α ′ 1 }endα′′ }.<br>13:<br>14: R = {α ′ ∈ A ′ : end a′ ≤ max<br>α ′′ ∈{α1,α ′ 1 }endα′′ }.<br>15: end if<br>16: Let area L = �n i=0 endαi − startαi where α ∈ L.<br>Equally we define area R .<br≯<br><!-- End of picture text -->

- 17: if area<sup>L̸</sup> = area<sup>R</sup> then 

- 18: Expand smallest area by adding padding, i.e. zero intervals. 

- 19: end if 

- 20: Let quad(area<sup>L</sup> ) and quad(area<sup>R</sup> ) be the two quadratic regressions using the points of the arches and the padding included in these areas. The two areas are considered similar if the curves have the same shape, i.e., both curves being convex or concave. 

- 21: Remove from A and A<sup>′</sup> the arches in L and R. 22: end while 



<!-- Start of picture text -->
cor p ora p re-kar y kis kar y kis balasis<br>notational texture 1.22 1.13 1.23<br><!-- End of picture text -->

Table 1. The notational texture of the corpora. 

Figure 3 shows the results of the similarity of the melodic arches. The melodic arches of the Karykis-Balasis corpora show the greatest similarity (78.99%). In the second place we have the pre-Karykis ± Karykis pair with similarity (68.18%), and in the last place the pre-Karykis ± Balasis pair with similarity (62.34%). The exact opposite is true for dissimilarity and the percentage of dissimilar shapes. Our results follow the observation of Stathis [13, pp. 26], quoting ªthe seventeenth-century Heirmologia contain kallopismoi [literally, to make beautiful or embellishments, but not to be confused with improvisations] of the Heirmologia of Theophanes Karykes and Iohasaph the New Koukouzelesº, i.e. the 17th onwards Heirmologions are not considered original compositions as they use as a basis the 16th century Heirmologions. 

Figures 4 & 5 present the Jensen-Shannon distances of the corpora on the studied viewpoints. We observe that Karykis-Balasis show the smallest difference, while preKarykis ± Karykis and pre-Karykis ± Balasis show similar 

310 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
Similarity of melodic arches<br>78.99<br>80 00 pre- Karykis ± Karykis<br>68.18 00 Karykis ± Balasis<br>62.34 pre-Karykis ± Balasis<br>60<br>40<br>28.11<br>22.84<br>20<br>14.43<br>9.01 9.56<br>6.58<br>0<br>similar dissimilar arches dissimilar shapes<br><!-- End of picture text -->

Figure 3. The bar charts of the melodic arches’ similarity. 

||pitch||interval||voiced unit|
|---|---|---|---|---|---|
|0.24<br>0.22<br>0.20<br>0.18<br>0.16||0.24<br>0.22<br>0.20<br>0.18<br>0.16||0.26<br>0.24<br>0.22<br>0.20<br>0.18<br>0.16<br>0.14<br>0.12||
|2-gr|ams 3-grams 4-grams 5-gra|ms<br>2-gra|ms 3-grams 4-grams 5-gra|ms<br>2-gr|ams<br>3-grams<br>4-grams|



Figure 4. The Jensen-Shannon distances (abbr. JSd) of the Markov models. The reference line shows the JSd of the case study corpora (pre-Karykis and Karykis) where Karykis chooses exceptionally to keep the pre-Karykis tradition. The Blue line shows the JSd of the pre-Karykis ± Karykis, the orange shows the JSd of the Karykis - Balasis, and the green line shows the JSd of the pre-Karykis ± Balasis. The orders of n-grams are kept low in order to reduce the negative effect of higher order n-grams [38]. 

distances which are greater than of Karykis ± Balasis. The close relation of Karykis ± Balasis is confirmed by the near placement of the orange and gray lines of the case study corpus (section 3.3). The low rate of dissimilarity of the Karykis ± Balasis Markov models is consistent with the observation of Makris [37] that the modality of Karykis ± Balasis remains the same in contrast to the modality of the pre-Karykis era. 

# 5. DISCUSSION 

The notational texture (i.e. the number of voiced units per syllable) of the corpora outlines a change that occurred in the Heirmologic style. As shown in Table 1, the notational texture of Karykis presents a drop (1.22 → 1.13) which leads us to a more syllabic texture. At the same time, however, Balasis shows an increase of notational texture, which reaches the same value as pre-Karykis (1.13 → 1.23). If we consider that there is no important difference in the 



<!-- Start of picture text -->
general syllabic pitch general syllabic interval syllabic contour<br>0.26 0.24<br>0.24 0.24 0.23<br>0.22 0.22<br>0.22 0.21<br>0.20<br>0.20 0.20<br>0.18 0.19<br>0.18<br>0.18<br>2-grams 3-grams 4-grams 2-grams 3-grams 4-grams 4-grams 5-grams 6-grams 7-grams<br><!-- End of picture text -->

Figure 5. As of Figure 4, the Jensen-Shannon distances of redundant viewpoints. 

interpretation-performance of the notation of the three corpora, then we can conclude that the values of the notation texture also correspond to values of durational texture. From these changes to the values of the notational texture, we can observe that Karykis simplifies the pre-Karykis melos and Balasis makes it sophisticated again by increasing the textures (notational and durational). 

According to the bar chart of similarity of the melodic arches, the Karykis and Balasis pair present the greatest similarity than the other two. This presupposes that Karykis changes the tradition of the Heirmologion and Balasis largely follows Karykis. Also, we observe that all pairs present a melodic similarity that is more than 60%. This can be justified by the fact that the compared pieces are different compositions of the same lyrics (different melodies of the same Heirmoi). It seems that there are some constraints between the text and the melody, especially in the accented syllables. For example, we can guess that the composers want the accented syllables to be in local maxima. So, the peak areas influence the melodic contour of the melodic lines. This presupposes that Karykis changes the tradition and Balasis largely follows Karykis. Specifically, Karykis ± Balasis have less distances than pre-Karykis ± Karykis and pre-Karykis ± Balasis ones. 

These results can be viewed within the context of the Theses concept in Byzantine music. Theses are formulae that work as building blocks in Byzantine music pieces. Since the Markov models capture the melodies as frequencies of small patterns, we can infer that similar models of two corpora indicate that the two corpora use similar Theses. 

# 6. CONCLUSIONS 

This paper presented three related corpora belonging to the Heirmologic subgenre of the Byzantine music. The corpora are digitised using the Knowledge Representation of [11] which captures the MBn. Through this effort we envisage the creation of a large database of MBn scores. Through the computational analysis we observed that Karykis changes the style of the subgenre while the succeeding tradition of the subgenre (Balasis) follows the Karykis style. Even though the analysis presented addresses a specific research question, it offers us insights which will become the inspiration for further research in the domain of Computational Byzantine Musicology. 

311 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

# 7. ACKNOWLEDGMENTS 

We would like to thank Fabian Moss for his insights in the digitisation of the corpora. 

# 8. REFERENCES 

- [1] D. Huron, ªThe Melodic Arch in Western Folksongs,º Computing in Musicology, vol. 10, Mar. 1996. 

- [2] N. Cook, A guide to musical analysis, reprint ed. Oxford: Oxford Univ. Press, 2009. 

- [3] ªConvention for the Safeguarding of the Intangible Cultural Heritage Intergovernmental Committee for the Safeguarding of the Intangible Cultural Heritage Fourteenth Session Bogotá,º Dec. 2019. 

- [4] G. Stathis, Ta protographa tes exegeseos eis ten nean methodou semiographias: ta prolegomena. Athens, Greece: Institute of Byzantine Musicology, 2016, vol. 1. 

- [5] M. VelimiroviÂc, Byzantine elements in early Slavic chant: The Hirmologion. Munksgaard, 1960. 

- [6] E. Wellesz, Eastern Elements in Western Chant: Studies in the Early History of Ecclesiastical Music. Byzantine Institute, 1947, google-Books-ID: uXzQvwEACAAJ. 

- [7] C. Troelsgård, Byzantine neumes: a new introduction to the Middle Byzantine musical notation, ser. Monumenta musicae Byzantinae. Subsidia. Copenhagen : Lancaster: Museum Tusculanum Press ; Gazelle [distributor], 2011, no. 9, oCLC: ocn750956349. 

- [8] M. Alexandru, Palaiographia Byzantines Mousikes [Paleography of Byzantine Music], Apr. 2017. [Online]. Available: https://repository.kallipos.gr/handle/ 11419/6487 

- [9] P. Savage, ªAn overview of cross-cultural music corpus studies,º in Oxford Handbook of Music Corpus Studies. New York: Oxford University Press. [Online]. Available: https: //www.researchgate.net/publication/326143358_An_ overview_of_cross-cultural_music_corpus_studies 

- [10] X. Serra, ªCreating research corpora for the computational study of music: the case of the compmusic project,º in Audio engineering society conference: 53rd international conference: Semantic audio. Audio Engineering Society, 2014. 

- [11] P. Polykarpidis, C. Anagnostopoulou, and D. Kalofonos, ªTowards the digitisation of Middle Byzantine notation: a formal model and Knowledge Representation,º in Music Encoding Conference 2022, Halifax, Canada, To be published. 

- [12] ÐÐ, ªMBnHeirmologicCorpora,º Jul. 2022, publisher: OSF. [Online]. Available: https://osf.io/f97a5/ ?view_only=131fae4a07a04792986a12c43327709a 

- [13] G. Stathis, Introduction to Kalophony, the Byzantine Ars Nova: The Anagrammatismoi and MathÅemata of Byzantine Chant. Peter Lang, 2014, google-BooksID: gAvwoQEACAAJ. 

- [14] D. Conomos, The treatise of Manuel Chrysaphes, the Lampadarios: On the theory of the art of Chanting and on certain erroneous views that some hold about it, ser. Corpus Scriptorum de re Musica. Wien: Österreichische Akademie der Wissenschaften, 1985, no. II. 

- [15] E. Makris, ªAdjustments of modality in the Postbyzantine Heirmologion,º in Tradition and Innovation in Late- and Postbyzantine Liturgical Chant. Acta of the Congress Held at Hernen Castle, the Netherlands, in April 2005. Hernen Castle, Netherlands: Peeters, 2008, pp. 37±63. 

- [16] N. Bouka, ªE paradose ton Eirmologikon Byzantinon melodion tou Bareos echou apo ton 10o aiona eos ton 16o aiona,º PhD, Ionian University, Corfu, Greece, 2004. 

- [17] A. Chaldaeakes, Ermeneia syntomos eis tin kath’ emas mousikin Pachomiou monachou, ser. Mnimeia Ellenorthodoxis Mousikes. Athens, Greece: Athos, 2015, vol. 5, no. 1. 

- [18] D. Balageorgos and F. Kritikou, Ta cheirographa tes Byzantines Mousikes: Sina. Athens, Greece: Institute of Byzantine Musicology, 2021, vol. 2. 

- [19] G. Zesimos, ªKosmas Iberites kai Makedon: Domestikos tes mones ton Iberon,º PhD, National and Kapodistrian University of Athens, Athens, Greece, 2007. 

- [20] D. Conklin and C. Anagnostopoulou, ªRepresentation and discovery of multiple viewpoint patterns,º in Proceedings of the International Computer Music Conference (ICMC 2001), Havana, Cuba, 2001, pp. 479±485. 

- [21] D. Conklin and I. Witten, ªMultiple viewpoint systems for music prediction,º Journal of New Music Research, vol. 24, no. 1, pp. 51± 73, Mar. 1995, publisher: Routledge_eprint: https://doi.org/10.1080/09298219508570672. [Online]. Available: https://doi.org/10.1080/ 09298219508570672 

- [22] L. Tardo, Hirmologium Cryptense, ser. principale (Facsimilés). Rome, Italy: Monumenta Musicae Byzantinae, 1951, vol. 3, no. 1. 

- [23] D. Balageorgos and F. Kritikou, Ta cheirographa tes Byzantines Mousikes: Sina. Athens, Greece: Institute of Byzantine Musicology, 2008, vol. 1. 

- [24] G. Stathis, Ta cheirographa tes Byzantines Mousikes: Agion Oros. Athens, Greece: Institute of Byzantine Musicology, 2015, vol. 4, no. 1. 

312 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

- [25] D. Touliatos-Miles, A Descriptive Catalogue of the Musical Manuscript Collection of the National Library of Greece: Byzantine Chant and Other Music Repertory Recovered. London: Routledge, Oct. 2017. 

- [26] J. Raasted, Intonation Formulas and Modal Signatures in Byzantine Musical Manuscripts. Copenhagen: E. Munksgaard, 1966. 

      - April 2005. Hernen Castle, Netherlands: Peeters, 2008, pp. 37±63. 

   - [38] J. Sakellariou, F. Tria, V. Loreto, and F. Pachet, ªMaximum entropy models capture melodic styles,º Scientific Reports, vol. 7, no. 1, Aug. 2017. [Online]. Available: https://www.nature.com/articles/ s41598-017-08028-4 

- [27] ªSyllabic style,º 2001. [Online]. Available: https: //doi.org/10.1093/gmo/9781561592630.article.27236 

- [28] ªNeumatic style,º 2001. [Online]. Available: https: //doi.org/10.1093/gmo/9781561592630.article.19788 

- [29] ªMelismatic style,º 2001. [Online]. Available: https: //doi.org/10.1093/gmo/9781561592630.article.18333 

- [30] C. Troelsgård, ªStylistic variation in the old Sticherarion,º in Theoria and Praxis of the Psaltic Art. Athens, Greece: Institute of Byzantine Musicology, 2006, pp. 225±232. 

- [31] G. S. Papadopoulos and P. Polykarpidis, ªElements in the development of how the Great Doxologies were sung from the 18th to the 19th century,º Journal of the International Society for Orthodox Music, vol. 4, no. 2, pp. 293±322, Nov. 2020, number: 2. [Online]. Available: https://journal.fi/jisocm/article/view/95235 

- [32] P. Polykarpidis and G. S. Papadopoulos, ªMelismatic elements in heirmologic chants from the 16th to the 19th century.º Thessaloniki, Greece: IMS Study Group, 2022. [Online]. Available: https://www.academia.edu/52588244/Melismatic_ elements_in_heirmologic_chants_from_the_16th_to_ the_19th_century 

- [33] D. Spanoudakis, ªOctaechia and Melismaticity in Byzantine Music. Collations and Musicological Reductive ± Statistical Analysis,º IMS Regional Association for the Study of Music of the Balkans, pp. 181±199, 2021. [Online]. Available: https://ejournals.lib.auth.gr/smb/article/view/7939 

- [34] F. C. Moss, ªTransitions of Tonality: A Model-Based Corpus Study,º PhD, École Polytechnique Fédérale de Lausanne, Lausanne, Switzerland, 2019. [Online]. Available: https://infoscience.epfl.ch/record/273178 

- Ð 

- [35] ªscipy.spatial.distance.jensenshannon SciPy v1.7.1 Manual.º [Online]. Available: https://docs.scipy.org/doc/scipy/reference/generated/ scipy.spatial.distance.jensenshannon.html 

- [36] C. D. Manning, P. Raghavan, and H. Schütze, Introduction to Information Retrieval. Cambridge, UK: Cambridge University Press, 2008. 

- [37] E. Makris, ªAdjustments of modality in the Postbyzantine Heirmologion,º in Tradition and Innovation in Late- and Postbyzantine Liturgical Chant. Acta of the Congress Held at Hernen Castle, the Netherlands, in 

313 

