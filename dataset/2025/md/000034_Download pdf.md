---
paper_id: "000034"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706395/files/000034.pdf"
---

# WHAT SONG NOW? PERSONALIZED RHYTHM GUITAR LEARNING IN WESTERN POPULAR MUSIC 

Zakaria Hassein-Bey<sup>1</sup> Yohann Abbou<sup>2</sup> Alexandre D’Hooge<sup>1</sup> Mathieu Giraud<sup>1</sup> Gilles Guillemain<sup>2</sup> Aurélien Jeanneau<sup>1</sup> 1 Univ. Lille, CNRS, Centrale Lille, UMR 9189 CRIStAL, F-59000 Lille, France 2 Guitar Social Club, F-59000 Lille, France 

## ABSTRACT 

The guitar is one of the most popular musical instruments, and numerous pedagogical tools have been developed to support learners. They rely on vast collections of songs, sheet music, and tablatures, making it challenging for guitarists to navigate and identify pieces that are both pedagogically relevant and aligned with their musical interests. 

We introduce a simple multi-criteria rule-based model to assess both the difficulty of learning a piece and the skill level of a guitarist, taking into account musical and technical criteria. The model provides personalized suggestions that help learners progress efficiently, considering parts within songs, but also multiple versions of the same part, accounting for simplified adaptations or different playing styles, and finally exercises used to progressively learn each part version. 

We implement and evaluate this approach in the context of rhythm guitar in popular music, using a dataset designed for the proprietary application Guitar Social Club. Expert evaluation of 77 recommendations for eight user profiles of varying levels indicate that in 82% of cases, the model provides relevant suggestions. While the full dataset remains proprietary, we release under open licenses the code along with a sub-corpus containing annotated difficulties for 319 versions of 110 parts from 40 songs. 

## 1. INTRODUCTION 

Guitar pedagogy has evolved alongside the technologies available to the general public [1]. Video-sharing platforms have enabled the formation of digital and real-life learning communities [2]. Although the actual pedagogical value of “serious games” is sometimes debated [3, 4], games such as Guitar Hero, RockBand, or Rocksmith have contributed to popularizing the guitar among the general public. Such games can involve controllers, real guitars, and/or augmented reality [5,6]. 

The vast number of tools and resources available to musicians makes selecting suitable pedagogical material complex. Solutions have been proposed to compile learning resources related to popular songs [7] or to search for pieces based on the chords users wish to practice [8]. Song recommendation can be optimized to maximize the number of playable songs after learning a new chord [9]. One of the major challenges in these applications is suggesting pieces to users that match their skill level, which includes challenges in both estimating the song difficulty and the user level. 

Models with multiple criteria for difficulty estimation have been proposed for piano music [10]. Recent work also proposed evaluating the difficulty of a piece by estimating a fingering or directly analyzing an image of the score [11, 12]. For the guitar, Vasquez et al. interviewed guitar teachers to develop criteria for estimating the difficulty of a piece with seven 4-scale criteria, along with a machine learning method to automate human ratings [13]. 

Contributions. Pedagogical assistance is crucial in learning music. However, to our knowledge, no approach currently provides an optimized learning path that balances difficulty and interest for guitarists of all levels. Our goal is to suggest songs tailored to learners’ current level and past experience, ensuring both accessibility and progress. 

Focusing on accompaniment or rhythm guitar [14], we identify what makes the difficulty for a guitarist, based on multiple criteria, and considering songs, parts, and versions (Section 2). We present a dataset of 1344 versions of 534 song parts (Section 3), and propose a model to suggest versions, parts, and songs personalized to someone’s skills (Section 4). This model is integrated into the proprietary application Guitar Social Club (GSC), which is currently in development, aimed to create an environment centered around guitar playing and learning. We implement and test this model (Section 5), and conclude with a discussion on personalized pedagogy (Section 6). 

> © Z. Hassein-Bey, Y. Abbou, A. D’Hooge, M. Giraud, G. Guillemain, and A. Jeanneau. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: Z. HasseinBey, Y. Abbou, A. D’Hooge, M. Giraud, G. Guillemain, and A. Jeanneau, “What Song Now? Personalized Rhythm Guitar Learning in Western Popular Music”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

## 2. WHAT MAKES LEARNING NEW SONGS DIFFICULT? 

## 2.1 Difficulty Criteria and Exercises 

The skill level of a learner cannot be defined with a single value. A guitarist may, for instance, know many chords, 

296 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

|ℓC|Chord complexity|||Chord examples|
|---|---|---|---|---|
|0-2|Basic open chords,    i|simple voicings, few fingers with close|i   positi|i   ons<br>Em, E, Am, A7sus4|
|3-4|Open chords, light|inversions, more open positions||C, D7, Gsus4, Fadd9|
|5-6|Common barre cho|rds, moderate stretches||F, Dmin7, G9, Bbadd6|
|7-8|More barre positio|ns, less intuitive grips||EM9, F#m, C#m/G#, Eb|
|9-10|Advanced voicings|,large stretches,full fretboard usage||Fm7,Abm,C#/G,Esus4/B|
|ℓP|Rhythmic Patte|rns|ℓT|Tempo / Impact Complexity|
|0-2|Mostly half and|quarter notes|0-2|Slow (60-200 PIPM)|
|3-4|Mostly eights, so|me sixteenths|3-4|Medium (200-400 PIPM)|
|5-6|Sixteenths with r|egular patterns|5-6|Faster (400-600 PIPM)|
|7-8|Sixteenths, irreg|ular patterns, claves, polyrhythms|7-8|High-speed (600-800 PIPM)|
|9-10|Elaboratedpolyr|hythms,odd-time signatures|9-10|Extreme(>800 PIPM)|
|ℓG|Typical time|Global Difficulty|||
|0-2|T0|Absolute beginner: basic open chords,|simpl|e strumming, slow tempo|
|3-4|T0 + 6 months|Beginner: basic open chords, simple st|rummi|ng, slow tempo|
|5-6|T0 + 3 years|Intermediate: barre chords, basic rhyth|m vari|ations, moderate tempo|
|7-8|T0 + 5 years|Confirmed: complex chord transitions,|intric|ate rhythms, faster playability|
|9-10|T0 + 8 years|Advanced: mastery of multiple styles,   i<br>Expert: near-professional level, full ar|impro  i<br>tistic c|visation, technical proficiency<br>ontrol,advanced improvisation|



Table 1. Criteria for assessing song/part/version difficulty in rhythm guitar playing, as discussed in Section 2. (a) Chords. (b) Rhythmic Patterns. There are further correcting factors for binary/ternary meters, upbeats... Note that this corpus mostly contain pop songs without elaborated polyrhythms. (c) Peak Impacts Per Minute (PIPM). Note that very or extremely slow PIPM can be also hard to play (not displayed here). (d) Global difficulty. Learning times vary considerably among students, and some never progress beyond the Beginner or Intermediate levels. The durations mentioned typically apply to students who practice their instrument several times a week. 

including complex ones, but struggle with smooth transitions. Conversely, another guitarist may only know basic chords but switch between them effortlessly, even in complex rhythms. The authors of [13] identify several difficulty criteria: the intrinsic complexity of a chord based on its fingering, the rarity of a chord, how the chord is strummed, and within a chord sequence, the repetitiveness and speed of chord transitions. 

The criteria proposed in this paper (Table 1) are also based on the expertise of a guitar teacher (YA, second author). While many criteria are similar, some differences arose, especially when it comes to the relative importance of each aspect. It’s worth noting that our work is focused about assisting guitar learning while [13] aimed at predicting the playability of guitar songs in a more general fashion, which might explain variations in the criteria. 

Chord complexity (ℓC) can be estimated using several indicators: the number of fingers required, the fret span, the use of open or muted strings, and the overall hand positioning. However, the true challenge often lies not in playing a single chord, but in transitioning between chords and hand positions. A key pedagogical principle emphasized by the guitar teacher is that of a leading finger. An open C major chord typically uses the ring finger as an anchor, while D/F# often requires the index finger or even the thumb. Alternating between chords with different leading fingers – such as in “C to D/F#” or even in the very common “G to C” – demands more effort and precision from the learner. In contrast, transitions like “Em to Asus2” are relatively easy, as they involve minimal finger movement and maintain a consistent hand shape (Figure 1). 

Considering tempo (ℓT ), the amount of Beats Per Minute (BPM, considering quarter notes as beats) alone is 



<!-- Start of picture text -->
C G Em<br>X O O O O O O O O<br>3 2 1 2 1 3 4 2 3<br>D/F# C Asus2<br>X X X O O X O O O<br>1 2 4 3 3 2 1 2 3<br><!-- End of picture text -->

Figure 1. Guitar chord diagrams with possible fingerings (1: index finger) and transitions. C to D/F# requires a complete finger repositioning. G to C involves moving the index and middle fingers together. Em to Asus2 is easier, requiring only a shift of the hand toward higher strings. 

not sufficient to characterize tempo complexity. For instance, a song at 70 BPM where the guitarist primarily plays sixteenth notes can present a similar level of rhythmic challenge as a song at 140 BPM with mostly eighth notes. In both cases, the effective playing rate is comparable, even if the perceived speed is different for the player and the listener. To better capture this aspect and to characterize the rythmic density of a piece, we introduce the Peak Impacts Per Minute (PIPM) – that is, the maximum beatrate (per minute) of the most frequently occuring rhythmic figure. Both previous examples would be at 280 PIPM, even if they would feature parts with lower PIPM. 

Rhythmic patterns (ℓP ) also play a significant role in determining difficulty – particularly their regularity and rarity. Surprisingly, rhythmic patterns played almost no role in [13] for difficulty estimation. 

297 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

|||1. Knoc|ki|ngon|Heaven’s Doo|r(|Bob Dy|lan,1|973)||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Version a<br>ℓC ℓP|ℓT ℓG|Version<br>ℓC|<br>ℓ|b<br>P ℓT|Ve<br> ℓG|rsi<br>ℓC|on c<br> ℓP ℓ|T ℓG|Version d (<br>ℓC ℓ<br>|SR)<br>P ℓT ℓG|Versio<br><br>ℓ<br>|n e (OR)<br>C ℓP ℓT ℓG|
|Intro/Chorus<br>1.a o/ 120 1<br>0|0<br>0<br>1.b<br>|�/ 90<br>1|1|1|0<br>1.c<br>�/ 120|1|1<br>1|1|1.d<br>�<br>�/ 72 1<br><br>|2<br>2<br>1|1.e<br>�<br>�/ 72 <br>|1<br>2<br>2<br>1|
|Verse<br>2.a o/ 120 3<br>0|0<br>1<br>2.b<br>�|/ 120 3|1|1|2<br>2.c<br>�/ 120|3|1<br>1|2|2.d<br>�<br>�/ 72 3<br><br>|2<br>2<br>2|2.e<br>�<br>�/ 72 <br>|3<br>2<br>2<br>3|
|Full Song<br>0.a o/ 72<br>3<br>0|0<br>1<br>0.b<br>|�/ 72<br>3|1|1|2<br>0.c<br>�/ 72|3|1<br>1|2|0.d<br>�<br>�/ 72 3<br>|2<br>2<br>2|0.e<br>�<br>�/ 72|3<br>2<br>2<br>3|
|||65|.|Losin|gmyReligion|(R.|E.M.,1|991)|||||
||Ve<br>|rsion c<br>ℓC<br>ℓP<br>ℓ|T|ℓG|Versi<br>|on<br>ℓC|d (SR)<br>ℓP<br>|ℓT<br>ℓ|Vers<br>G<br>|ion e (OR<br>ℓC<br>ℓP|)<br>ℓT<br>ℓG||
|Intro/Chorus|1.c<br>�/ 120|4<br>1<br>|1|3|1.d<br>�<br>�/ 90<br>|4|2|3<br>3|1.e<br>�<br>�/ 125<br>|4<br>2|4<br>4||
|Verse|2.c<br>�/ 120|2<br>1<br>|1|2|2.d<br>�<br>�/ 90<br>|2|2|3<br>2|2.e<br>�<br>�/ 125<br>|4<br>2|4<br>3||
|Bridge|4.c<br>�/ 120|4<br>1<br>|1|2|4.d<br>�<br>�/ 90<br>|4|2|1<br>2|4.e<br>�<br>�/ 125<br>|4<br>2|1<br>2||
|Full Song|0c<br>/ 125|4<br>1<br>|1|3|0d<br>�<br>/ 125|4|2|3<br>|0e<br>�<br>/ 125|4<br>2|4<br>4||
||.<br>�|5|5|. Fade|.<br>� <br>To Black(Me|tal|lica,19|84)|.<br>�||||
||||||Versio<br>|n e<br>ℓC|(OR)<br><br>ℓP|ℓT|ℓG||||
|||Intro||1.e|�<br>�/ 58<br>|2|3|3|4||||
|||Bridge 0||2.e|�<br>�/ 90|9|3|3|7||||
|||Verse||3.e|�/ 120<br>|3|3|3|4||||
|||Chorus||4.e|�<br>�/ 58|3|3|6|5||||
|||Bridge 1||5.e|�<br>�/ 58|3|3|7|6||||
|||Bridge 2||6.e|�<br>�/ 58|3|3|7|5||||
|||Outro||7.e|Clave / 58|4|4|5|5||||
|||Full Son|g|0.e|OR / 58|9|4|7|8||||



Table 2. Ratings for selected versions and parts from three songs. Versions (a), (b), and (c) are introductory arrangements, using mainly whole, half, and quarter-note rhythmic patterns, respectively. Version (d) is close to the original song but features a Simplified Rhythm (SR), reducing the complexity of the most challenging patterns. Version (e) presents the Original Rhythm (OR), closely reproducing the version performed by the original band. �/120 indicates that the version has a fastest note value of a quarter note and played with a tempo of 120 BPM. Knocking on Heaven’s Door can be played by beginners, including by absolute beginners for its version (a), where chords change on each whole note (ℓG = 1). In Losing my religion, in easy versions, Intro and Chorus are more challenging than the Verse, especially concerning chords (ℓC). Fade to Black, with its 7 parts, is destinated to advanced players. The “Bridge 0”, featuring diminished chords with two different voicings, is particularly difficult (ℓC = 9). As this song features very characteristic voicings and elaborate transitions, the decision was to have only the version (e) in the corpus. 

Difficulty also arises from the interaction between the left and right hands, particularly when the number of strings plucked or strummed varies significantly between chords. This combinatorial complexity further contributes to the challenge of chord transitions. A model of rhythmic guitar difficulty should consider not only the complexity of individual chord positions or rhythmic patterns, but also the difficulty of transitions between them, especially at a given tempo. Altogether, each song difficulty is rated as a whole (ℓG) as perceived by the guitar teacher. 

Moreover, when working with a teacher, students are often given specific exercises to target challenging aspects of a song – most commonly particular chord or pattern changes that need to be practiced at varying speeds. In this way, different songs may share common exercises. As a result, the difficulty of learning a new song also depends on the number and complexity of new exercises it introduces, beyond those the student has already mastered. 

## 2.2 Songs, Parts, and Versions 

Even with multiple criteria, treating the difficulty of a song as fixed is unrealistic, since it varies throughout the piece. R.E.M.’s Losing my Religion, for example, has a Bridge that is more technical and challenging than the Verse because of the fast-paced chord changes (Table 2). Indeed, the Verse is mostly composed of the simple sequence of 

chords (Am, Em) which is a perfect for a very first piece of a guitar beginner. The Bridge however contains the chords G, F, Dm, and Am, and thus transitions between them. The F chord is particularly complex for beginners because it has to be played with a barre. 

But what does it really mean to “play Losing My Religion”? Some advanced players may aim to master the full tablature as performed by the band, while for many guitarists, simply strumming the Verse chords – enough to sing along – is already a meaningful goal. This has real pedagogical value. A beginner who cannot yet play the Verse as recorded may still feel accomplished learning a simplified version, guided by their teacher in choosing an adaptation suited to their level. Thus, a song and even each part of a song could have multiple versions, each with an estimated difficulty level that reflects different approaches to playing it (Table 2). Simplification can focus on reducing the number or complexity of chords – for example, by removing barre chords – as well as simplifying strumming patterns or other musical features. 

We thus consider songs, parts, versions, and exercises linked to them. The segmentation of a song into parts, such as Intro, Verse, Chorus, Bridge, or Outro, is both musical and technical. Since parts are often homogeneous from a guitaristic perspective, it is possible to model their own difficulty and pedagogical interest for a given person. 

298 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
35 0<br>25 0 a a a 25 0 a<br>b 40 0 b 30 0 b b<br>20 0 cd 30 0 cd 25 0 cd 20 0 cd<br>15 0 e e 20 0 e 15 0 e<br>20 0 15 0<br>10 0 10 0<br>10 0<br>5 0 10 0 5 0 5 0<br>0 0 0 0<br>0 2 4 6 8 10 0 2 4 6 8 10 0 2 4 6 8 10 0 2 4 6 8 10<br>Chords Rhythmic Patterns Tempo/impact Global<br>Versions Versions Versions Versions<br><!-- End of picture text -->

Figure 2. Distribution of the difficulty of the 1344 versions among the four criteria. Version range from (a), easiest, to (e), most difficult, as described on Table 2. 

## 3. CORPUS 

The corpus developped for Guitar Social Club contains 194 songs from the popular acoustic guitar repertoire. The guitar teacher selected pieces frequently requested by students of various ages, genders, and musical preferences. The songs are categorized into six genres: Rock (32%), Pop (29%), Funk/Soul/R&B (10%), World Music (9%), and Other/Radio (20%). Expanding the corpus and better representing underrepresented styles is a future goal. 

The songs contain between 1 and 7 parts, with most having 2 or 3, totaling 534 parts. The parts have in average 2.5 versions, totaling 1344 versions. Finally, the application includes 3248 video exercises. Most of these exercises focus on practicing chord transitions at varying speeds. Each exercise was manually linked to specific versions/parts/songs of the dataset. The application further contains pseudo-songs with instructional videos on generic topics. 

## 4. A MODEL FOR PERSONALIZED SUGGESTION 

We consider a finite corpus of songs S = {s1, s2, ..., sS}, parts P = {p1, p2, ..., pP }, versions V = {v1, v2, ..., vV }, and exercices E = {e1, e2, ..., eE}, Each version v is linked to one part π(v) ∈P, and each part p is linked to one song σ(p) ∈S. Each version v is also linked to a set of exercices ε(v) ⊂E. A guitarist g already knows a subset Vg ⊂V of these versions. We assume that it means that they already master the exercises Eg = ∪v∈Vg ε(v). 

Which version of which part of which piece, and thus which exercises, should they work on to progress? To provide a personalized pedagogical suggestion, our approach is to consider multiple criteria to model the difficulty of a version/part (Section 4.1) and to estimate the guitarist’s skill levels (4.2). This allows us to model the pedagogical value of a version/part for each learner (4.3). 

## 4.1 Modeling Version/Part/Song Difficulty 

Each song/part/version v was analyzed and assessed according to K difficulty criteria {ℓ1, ℓ2, . . . , ℓK}. Each criterion represents a value ℓk(v) ∈ [0, 10], where 0 indicates a version that a beginner can play and 10 is for an experienced guitarist. The K = 4 evaluated criteria described 

in Section 2 are thus Chords (ℓC), Rhythmic Patterns (ℓP ), Tempo/Impact (ℓT ), and Global (ℓG) (Table 1). 

Criterion ℓG was assessed by the guitar teacher, and other criteria combine human expert evaluation (following Table 1) with proprietary procedures. Table 2 shows these ratings for three songs of increasing difficulty, and Figure 2 the distribution of ratings in the corpus. 

For rhythm-related criteria, moderate and slow values predominate. The distribution of the difficulty criteria is mostly centered around intermediate ratings. This observation suggests that the corpus is well distributed across levels and could likely benefit guitarists of all levels. 

## 4.2 Estimating a Learner’s Skill Level 

How can we describe the skill level of a guitarist g across the considered criteria? For each criterion ℓk, we retrieve Vg<sup>k[N]</sup> ⊂Vg, the list of the N most difficult known versions according to that criterion. The skill level ℓk(g) of the guitarist is then the average difficulty of these N versions: 



<!-- Start of picture text -->
ℓk(g) = N 1 � ℓk(v)<br>v∈Vg k[N ]<br><!-- End of picture text -->

For example, with N = 4, a guitarist g who knows perfectly Knocking on Heaven’s Door (all parts, version (e)) but only the easiest version (c) of Losing my Religion would have skill levels ℓC(g) = 3.75, ℓP (g) = 1.75, ℓT (g) = 1.75, and ℓG(g) = 3.00. In the actual model, the levels of each guitarist are estimated by selecting N = 15 part versions among the ones they practiced, which amounts to 6 songs on average. 

## 4.3 Personalized Version Suggestions 

The learner’s skill level is compared to the difficulty of a specific version of a song part, considering a challenge value τ ∈ [1, 2, 3, 4] that will be discussed below. A challenge fit Fg(v, τ ) is computed for a guitarist g wishing to learn a version v under the challenge τ : 



<!-- Start of picture text -->
K •<br>Fg(v, τ ) = � αk |Ck(g, v, τ )|<br>k=1<br><!-- End of picture text -->

The challenge fit is a weighted sum of the absolute value of K<sup>•</sup> fits Ck(g, v, τ ), each weighted by a coefficient αk. These fits take into account the K difficulty criteria defined previously (see Section 4.3.1), but also other criteria (4.3.2, 4.3.3), and equal zero when the fit is perfect. 

299 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
0 0<br>1 0 1 0<br>2 0 2 0<br>3 0 1 3 0 1<br>2 2<br>4 0 3 4 0 3<br>4 4<br>5 0 5 0<br>1 0 1 2 3 4 5 6 1 0 1 2 3 4 5 6<br>Tempo/impact difficulty Global difficulty<br>Rank Rank<br><!-- End of picture text -->

Figure 3. Distribution of the recommendations, on each of the four challenges according to ℓT and ℓG, for the profile G4 (with levels ℓT = 2.89 and ℓG = 3.33). 

## 4.3.1 Challenge Fit for a Difficulty Criterion 

The fit is modeled using an exponential function with parameters βk (scaling coefficient) and γk,τ (bias to control target difficulty under challenge τ ): 



<!-- Start of picture text -->
Ck(g, v, τ ) = e βk[ℓk(v)−ℓk(g)−γk,τ ] − 1<br><!-- End of picture text -->

When γk,τ = 0, then the value Ck(g, v, τ ) equals 0 when ℓk(v) = ℓk(g), meaning the version v exactly matches the guitarist’s level. When γk,τ is strictly positive (resp. negative), we want that the guitarist target a higher (resp. lower) difficulty than their current level. 

The model eventually proposes four challenges (Table 3). Challenge 2 suggests parts/versions at the guitarist’s level (γk,2 ≈ 0), Challenge 1 suggests easier parts/versions (γk,1 negative), and Challenges 3 and 4 suggest progressively harder parts/versions (γk,τ positive). 

## 4.3.2 Challenge Fit for the New Exercices 

We call nεg(v) = |e ∈ ε(v)\Eg| the number of exercices in ε(v) not currently known by g. Let γE,τ be the number of new exercices to be targeted, then the fit is: 



<!-- Start of picture text -->
CE(g, v, τ ) = e βE [nεg(v)−γE,τ ] − 1<br><!-- End of picture text -->

This value could be adapted to account for the difficulty of each exercise, provided such data is available. 

## 4.3.3 Additional Challenge Fits 

Other criteria k can be implemented. For example, the proprietary application includes discrete fits to align with user preferences or recommendations from another system, favor complete songs within a given style, or focus on parts with specific pedagogical interest: 



<!-- Start of picture text -->
when the criterion is met<br>Ck(g, v, τ ) =<br>1 otherwise<br>� 0<br><!-- End of picture text -->

## 4.4 Song/Part Coherency and Full Songs 

For each guitarist g and challenge value τ , fits are computed against all versions v (Figure 3). The model selects versions v that offer the best fits, minimizing Fg(v, τ ). Additionally, we ensure that a given song and part appear in only one challenge value to avoid redundancy. 

Full songs (bottom lines on Table 2) can also be suggested, in different versions. They are evaluated based on 

|k|challenge valueτ|αk|βk|1|γk,<br>2|τ<br>3|4|
|---|---|---|---|---|---|---|---|
|C|Chords|0.5|1|−0.5|0|1|3|
|P|Rhythmic Patterns|0.5|1.5|−0.5|0|1|3|
|T|<br>Tempo/Impact .|0.5|1.5|−0.5|0|1|3|
|G|<br>Global|0.8|0.3|−0.5|0.5|1|3|
|E|Exercises Number|2|0.8|2|3|5|7|



Table 3. Coefficients for each criterion. The γ values were set increasing on the 4 challenges. Challenge 2 is meant to be almost the estimated level of the guitarist. 

the difficulty of their most challenging parts – occasionally adjusted to account for additional complexity. Full songs are given a bonus in the ranking process, encouraging learners to engage with complete pieces. 

## 4.5 Optimizing Weights 

The coefficients γk,τ were chosen to target different challenges and to control the number of new exercises introduced (Table 3). The coefficients αk and βk were refined during the evaluation process (see Section 5.2). The small amount of data available, combined with the intention to maintain a very simple and interpretable model, led us to favor manual tuning over automated optimization techniques, even if it might introduce bias and overfitting. 

## 5. IMPLEMENTATION AND EVALUATION 

## 5.1 Implementation, Code and Data Availability 

Commercial application. The Guitar Social Club application, currently under development, provides guitarists with a comprehensive environment centered around guitar playing, with more than 3200 instructional videos. Users indicate their preferred styles, the songs they already know, and the songs they wish to learn. The model described here, with additional proprietary criteria, suggest song/part versions, categorized into four different challenge levels. Guitarists then select the piece they want to work on and progress through a series of exercises supported by videos of increasing difficulty. Videos may be shared across multiple parts (e.g., teaching a specific chord or chord transition) or tailored to a particular part (e.g., for a unique rhythmic pattern). The application also tracks which exercises the user has completed, and this data could be used to enhance personalization. 

Open-source and open-data components. Developed in Python, the code for the model described here along with its evaluation is released under the LGPLv3+ license in a git repository available from `algomus.fr/code` . Although the complete dataset is proprietary, we release a subset of this data under an open license, covering difficulty metadata for 40 songs, 110 parts, and 319 versions, as well as 148 oracle evaluations related to these songs/parts/versions (see below). This public dataset is available with the code as well as on the long-term recherche.data.gouv.fr archive at `https://doi.org/ 10.57745/1KXHMJ` . 

300 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
0.3 0.2 0.2 0.3 0.2 0.2 0.2<br>0.3 0.2 0.2 0.2 0.4 0.2 0.6 0.3 0.3 0.5 0.3 0.8 0.3 0.2<br>0.2 0.2 0.6 0.3 0.5 0.3 0.6 0.5 0.3 0.6 0.20.2 0.5 0.5 0.30.2 0.7 0.2 0.3 0.5 0.40.2<br>0.5 0.2 0.2 0.2 0.2 0.2 0.2 0.2<br>G1 G2 G3 G4 G5 G6 G7 G8 G1 G2 G3 G4 G5 G6 G7 G8<br>a) b)<br>0.5 0.5 0.7 0.2 0.5 0.3 0.20.2 0.2 0.2 0.4 0.6 0.2 0.3<br>0.3 0.6 0.3 0.2 0.2 1.0 0.8 0.8 1.0 1.0 0.6 0.5 0.6 0.4 0.8 0.3 0.5<br>0.2 0.7 0.5 0.6 0.2 0.2 0.2 0.2 0.2 0.3 0.2 0.3<br>G1 G2 G3 G4 G5 G6 G7 G8 G1 G2 G3 G4 G5 G6 G7 G8<br>G1 G2 G3 G4 G5 G6 G7 G8 c) d)<br>- -3 -2 -1 0 1 2 3 +<br><!-- End of picture text -->

Figure 4. Distribution on deviations between the predicted challenge and the expert annotation on 77 recommendations from eight test profiles. (Left). Full model. In average, 49% of the model suggestions perfectly match the challenge value from the expert (0), and 82% deviate with at most 1 challenge value (+1 or −1). (Right). Ablation models, ignoring a) chords, b) PIPM and Rhythmic Patterns, c) global difficulty, and d) number of exercices. 

## 5.2 Evaluation 

## 6. DISCUSSION AND CONCLUSION 

We created eight test profiles G1 − G8, representing different guitarist skill levels spanning from absolute beginners (G1) to advanced (G8). For each such guitarist g, the model suggests up to 12 song/part versions r that minimize Fg(r, τ ) (3 per challenge), with thus, for each suggestion r, a suggested challenge φ(r, g) ∈ [1, 2, 3, 4]. The guitar teacher evaluates the relevance of these suggestions, providing for each suggestion r for a guitarist g an oracle value ψ(r, g) ∈ [−∞, 1, 2, 3, 4, +∞]. The integers represent the expected challenge of the song/part version, A value −∞ means the suggestion is too simple for g and should never have been proposed, while +∞ indicates that it is far too difficult. During the optimization of the coefficients (see Section 4.5), the expert guitar teacher actually labeled up to 720 suggestions (including 77 evaluations on the final suggestions). This information may be used for future model optimization and validation. For example, on the guitarist profile G4, the (full) song 1. Knocking on Heaven’s Door (see Table 2) is annotated in the oracle as ψ(1.c, G4) = 1, ψ(1.d, G4) = 2, and ψ(1.e, G4) = 3. 

The Figure 4 shows the distribution of ∆(r) = φ(r) − ψ(r) on the 77 evaluations for various models. With the coefficients shown on Table 3, 82% of the suggestions are considered pertinent by the teacher, that is with |∆| ≤ 1. Ablation models, in which certain criteria are omitted, still achieve solid results, with average relevant prediction rates ranging from 60% to 100%. This highlights both the robustness of the full model and the significance of individual criteria, particularly the assessed overall difficulty. 

The observed errors mostly concern songs that are either too simple or too complex, even within challenge levels 1 and 4, respectively. Future work will focus on studying these edge cases in greater detail to improve the model’s accuracy and relevance. 

Tools supporting pedagogy and offering suggestions can help prevent learner demotivation during self-study phases [4]. They can also assist educators in recommending suitable pieces with less preparatory work [12], promoting independent and personalized learning [15]. Suggestions should occasionally encourage learners to step outside their comfort zone, as teachers often advise. 

Building on [13], we introduced criteria to assess rhythm guitar difficulty in Western popular music and a model to evaluate guitarist skill levels. To mirror real learning, we divided songs into parts with multiple versions linked to exercises. This model is implemented in the Guitar Social Club application, and we openly release a part of this dataset. Evaluation against expert oracle data shows that 82% of the suggestions are relevant, validating this rule-based suggestion approach as a first proof-of-concept. 

The deterministic rule-based system and its manual optimization may have produce overfitting, but the extremely simplicity of the model (only 10 coefficients α and β) reduced this risk. In any case, using an automated system to suggest new songs to learn has limitations and is akin to biases. Determining which songs a learner knows presents difficulties – users might claim to know a song while lacking the proficiency assumed by the model. A guitar teacher could detect such discrepancies. 

Investigating how learner autonomy is balanced with pedagogical guidance, and how personalization extends beyond self-declared mastery, could enhance such methods. Future work could explore non-intrusive ways to verify learner proficiency, such as analyzing timing accuracy, note or chord correctness at specific instants, or comparing performance patterns against expert models. It should include some randomisation or better counter-measures to limit biases [16] and better evaluation with actual user data. Finally, the framework presented here could also be applied to other instruments or even to fields beyond music where skills and learning content need to be matched. 

301 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 7. ACKNOWLEDGMENTS 

The authors thank the Algomus team for their valuable feedback and the anonymous reviewers, whose contributions helped improve this paper. This project is supported by La Plaine Images, Hauts-de-France Innovation Développement, Bpifrance, the French Tech initiative, and the ANR TABASCO project (ANR-22-CE38-0001). 

## 8. ETHICS STATEMENT 

While the eight test profiles were created by the expert guitar teacher with certain students in mind, no personal data was used in this study. The study does not involve any user feedback or direct user involvement. Future research could include such aspects, which would require prior ethical consideration and approval from the relevant ethics committee. 

## 9. REFERENCES 

- [1] R. C. Rodriguez and V. Marone, “Guitar learning, pedagogy, and technology: A historical outline,” Social Sciences and Education Research Review, vol. 8, no. 2, pp. 9–27, 2021. 

- [2] A.-M. Burns, S. Bel, and C. Traube, “Learning to play the guitar at the age of interactive and collaborative Web technologies,” in Sound and Music Computing Conference (SMC 2017), 2017. 

- [3] D. Arsenault, “Guitar Hero:" Not like playing guitar at all"?” Loading..., vol. 2, no. 2, 2008. 

- [4] M. Margoudi, M. Oliveira, and G. Waddell, “GameBased Learning of Musical Instruments: A Review and Recommendations,” in European Conference on Games Based Learning (ECGBL 2016), 2016. 

- [5] R. Rodriguez and V. Marone, “Learning beyond the game: A multimodal analysis of Rocksmith users interactions,” Acta Ludologica, vol. 3, no. 2, pp. 36–53, 2020. 

   - [9] S. Ariga, M. Goto, and K. Yatani, “Strummer: An interactive guitar chord practice system,” in IEEE International Conference on Multimedia and Expo (ICME 2017), 2017, pp. 1057–1062. 

   - [10] V. Sébastien, H. Ralambondrainy, O. Sébastien, and N. Conruyt, “Score Analyzer: automatically determining scores difficulty level for instrumental e-Learning,” in International Society for Music Information Retrieval Conference (ISMIR 2012), 2012, p. 571. 

   - [11] P. Ramoneda, N. C. Tamer, V. Eremenko, X. Serra, and M. Miron, “Score difficulty analysis for piano performance education based on fingering,” in IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP 2022), 2022. 

   - [12] P. Ramoneda, J. J. Valero-Mas, D. Jeong, and X. Serra, “Predicting performance difficulty from piano sheet music images,” in International Society for Music Information Retrieval Conference (ISMIR 2023), Sep. 2023. 

   - [13] M. A. V. Vásquez, M. Baelemans, J. Driedger, W. Zuidema, and J. A. Burgoyne, “Quantifying the ease of playing song chords on the guitar,” in International Society for Music Information Retrieval Conference (ISMIR 2023), 2023. 

   - [14] D. Régnier, N. Martin, and L. Bigo, “Identification of rhythm guitar sections in symbolic tablatures,” in International Society for Music Information Retrieval Conference (ISMIR 2021), 2021. 

   - [15] T. Vaizman and G. Harpaz, “Retuning music teaching: Online music tutorials preferences as predictors of amateur musicians music self-efficacy in informal music learning,” Research Studies in Music Education, vol. 45, no. 2, pp. 397–414, 2023. 

   - [16] A. Ferraro, X. Serra, and C. Bauer, “Break the loop: Gender imbalance in music recommenders,” in Conference on Human Information Interaction and Retrieval (CHIIR 21), 2021, pp. 249–254. 

- [6] J. Martin-Gutierrez, M. S. Del Rio Guerra, V. LopezChao, R. H. Soto Gastelum, and J. F. Valenzuela Bojórquez, “Augmented reality to facilitate learning of the acoustic guitar,” Applied Sciences, vol. 10, no. 7, p. 2425, 2020. 

- [7] M. Barthet, A. Anglade, G. Fazekas, S. Kolozali, and R. Macrae, “Music recommendation for music learning: Hottabs, a multimedia guitar tutor,” in Workshop on Music Recommendation and Discovery (WOMRAD 2011), 2011, pp. 7–13. 

- [8] A. Xambó, J. Pauwels, G. Roma, M. Barthet, and G. Fazekas, “Jam with Jamendo: Querying a large music collection by chords from a learner’s perspective,” in Audio Mostly on Sound in Immersion and Emotion (AM 2018), 2018, pp. 1–7. 

302 

