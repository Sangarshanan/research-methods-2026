---
paper_id: "000017"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706353/files/000017.pdf"
---

# A MULTIDIMENSIONAL APPROACH TO OPERA ANALYSIS: HARMONY, TEMPO, AND DRAMATIC INTERACTION IN WAGNER’S SIEGFRIED 

Pascal Schmolenzky<sup>1</sup> Stephanie Klauk<sup>1</sup> Rainer Kleinertz<sup>3</sup> Meinard Müller<sup>4</sup> 

Stephanie Klauk<sup>1</sup> Christof Weiß<sup>2</sup> 

1 Institut für Musikwissenschaft, Saarland University, Germany 

2 Center for Artificial Intelligence and Data Science, University of Würzburg, Germany 

3 Hochschule für Musik Saar, Germany 

4 International Audio Laboratories Erlangen, Germany 

```
pascal.schmolenzky@uni-saarland.de,s.klauk@mx.uni-saarland.de,
```

```
christof.weiss@uni-wuerzburg.de
```

## ABSTRACT 

Richard Wagner’s four-opera cycle Der Ring des Nibelungen presents unique challenges for music analysis due to its large scale, structural complexity, and intricate relationship between music and drama. While harmony plays a central role, additional factors such as tempo, instrumentation, and leitmotifs significantly contribute to formal organization. This study combines computational and musicological approaches to analyzethe third (final) act of Siegfried, the third evening in the Ring cycle. By integrating symbolic score data, manual annotations, audio-based harmonic analysis, and libretto information, we jointly visualize harmonic progressions, tempo variations, and dramatic interactions to reveal large-scale structural developments in Wagner’s music. Our interdisciplinary analysis highlights the role of tonal stability and instability, tempo contrasts as well as character interactions in shaping form. More broadly, this study demonstrates how computational methods can complement traditional musicological analysis, offering a structured framework for studying complex operatic works. Our visualizations contribute to a deeper understanding of Wagner’s music and pave the way for further research integrating computational tools into opera analysis. 

## 1. INTRODUCTION 

The analysis of Wagner’s dramas presents unique challenges due to their large-scale structural complexity, and intricate relationship between music and drama. In 1924, the conductor and musicologist Alfred Lorenz was the first to attempt a systematic exploration of what he called Wagner’s ‘secret of form’ [1]. He focused on harmony in or- 

> © P. Schmolenzky, S. Klauk, C. Weiß, R. Kleinertz, and M. Müller. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: P. Schmolenzky, S. Klauk, C. Weiß, R. Kleinertz, and M. Müller, “A Multidimensional Approach to Opera Analysis: Harmony, Tempo, and Dramatic Interaction in Wagner’s Siegfried”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

der to segment Wagner’s musical texture into discrete formal units. From the 1960s onwards, Lorenz’ analyses met with strong criticism [2–4]. A central objection was that his method imposed rigid, preexisting formal types onto Wagner’s music. Critics argued that his segmentation into formally and tonally closed periods forced Wagner’s organically evolving structures into inflexible and artificial framework [5]. Further musicological analysis strategies have been extended to other musical and extra-musical elements of Wagner’s operas (cf. most recently [6]) but are at the same time limited to isolated case studies. 

Recently, computational studies have shown to be beneficial in producing a large-scale overview to Wagner’s operas [7, 8]. Although these computational approaches rely on a statistical and therefore more neutral basis, they have not yet addressed the highly relevant interplay between multiple musical parameters. In addition to harmony, elements such as tempo, timing and agogics, instrumentation, dynamics, etc. have been defined as crucial for shaping dramatic structure in Wagner (e.g. [9]). 

The present study addresses this by employing computational visualization techniques for a multidimensional approach. As our central contribution, we integrate computational audio analysis and symbolic score data, libretto information, as well as manual annotations of recorded performances. By systematically mapping different parameters—tempo, harmony, and speaker roles— to the musical timeline (measures), we aim to reveal largescale patterns of an operatic work and its performances. As an example, we analyze the third act of Wagner’s Siegfried, the third opera of the tetralogy, visualize the musical progressions throughout the scenes of this act, and discuss the musicological implications of our visualizations. From a more conceptual perspective, implementing such computational tools provides an empirical strategy for evaluating traditional musicological readings as well as for offering new perspectives on Wagner’s dramatic works. 

142 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



Figure 1. Siegfried, Act III, Scene 1. Visualization of tempo curves from 16 different recordings between 1952 and 2011. Individual performances are shown in semi-transparent colored lines, while the bold red line represents the smoothed median tempo across all performances. 

## 2. FORM AND STRUCTURE IN WAGNER’S SIEGFRIED 

This paper focuses on aspects of form and structure in the sense of musical shape [10]. We leave aside the so-called semantic listening of leitmotifs, which is subject of numerous recent publications about form and function [11, 12], modes of perception [13] or automated detection [14]. Drawing on Wagner’s concept of the “poetic-musical period,” Lorenz provided the first large-scale formal analysis of Wagner’s opera cycle Der Ring des Nibelungen [1], including Siegfried. In doing this, he partitioned the entire tetralogy into a series of 146 periods, each defined by a local key (“principal tonality”) and its dramatic and musical content. Lorenz described these periods as overarching structural units that framed Wagner’s compositions, identifying the highest number of such periods in Siegfried, of which Act III contains 15 out of 45. Contrary to Lorenz, Patrick McCreless refuses the model of such smaller periods for the third act, and identifies a large-scale fivemovement symphonic form instead [3]. He discusses the compositional shift between act II and III, which corresponds to an interval of 12 years, in terms of harmonic density. 

Further analytical studies on Siegfried focused on particular case studies. Among others, Anthony Newcomb [9] analyzes the opening of Siegfried’s Act III, arguing that large-scale formal coherence is not primarily achieved through overall tonal structure characterised by specific local keys but rather through a projection of the dramatic process onto the music. This process—i.e. the portrayal of characters, their changing emotional states, and their conflicts—shapes the broader formal design of a larger section and can be observed through the progression of various parameters. Newcomb specifically emphasizes the role of tonal stability (clear cadential progressions) and instability (e.g. increased chromaticism, ambiguous tonal centers etc.), as well as tempo, timing, and pitch. Carol Berger [15] is largely interested in traditional Italian opera forms and, censequently, only gives an overview of Scene III of the third act. Even more focused is Jürgen Schläder’s study of the final Siegfried-Brünnhilde duet [16], whereas Hermann Danuser’s [17] and Katharina Hottmann’s [18] more 

philological analyses of Scene II and III, respectively, reflect Siegfried’s conception as a heroic figure. 

Expanding beyond these traditional musicological approaches, computational studies have applied audio-based analysis techniques to Wagner’s Walküre, providing new insights into its large-scale structure and musical organization [7, 8]. Using the Wagner Ring Dataset (WRD) [19], we apply this computational approach to Wagner’s Siegfried. Additionally, we provide integrated visualizations that not only capture the harmonic progression over entire scenes, but also highlight information about tempo and singers. This provides a structured, multi-dimensional view of Wagner’s evolving musical form and shows largescale developments, helping to evaluate and complement traditional analytical perspectives. 

## 3. COMPUTATIONAL ANALYSES AND ANNOTATIONS 

In our analysis of harmony and tempo, we combine the computational analysis of musical properties from audio recordings with the visualization of manual annotations contained in the WRD [19]. 

The harmonic analysis is based on Bernard Haitink’s 1988 recording of Siegfried. Firstly, we extract pitchclass activities over time by employing a deep learningbased chroma extraction method [20], which provides robust pitch-class representations under complex performance conditions. To account for the coarse temporal scale of local keys and scales, we smooth these pitch-class representations using a moving average filter with a window size of 64 measures and a hop size of one measure. Based on these features, we compute a probability distribution across the 12 diatonic scales by applying a patternmatching technique that compares the extracted pitch-class activity with binary templates of each scale [20, 21]. The resulting values are visualized as vertically stacked bands, where the “0” band corresponds to the diatonic scales without accidentals, i. e., the pitch content of the C major or the A minor scale (absolute diatonic scale measurement). The remaining bands are arranged with respect to the circle of fifths (e.g. −1 corresponds to F major or D minor, +1 corresponds to G major or E minor etc.). 

143 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
250<br>200<br>150<br>(bpm)<br>100<br>Absolute diatonic scale Tempo<br>654321012345 50<br>50 100 150 200 250 300 350 400 0<br>Time (measures)<br>Figure 2. Siegfried, Act III, Scene 1. Probability values for diatonic scales are represented in grayscale, with black indicat-<br>ing high probability. These are overlaid with a smoothed median tempo curve in red (in bpm). Transparent, colored areas<br>indicate the singer activity of characters Wotan (light blue) and Erda (light green), respectively.<br><!-- End of picture text -->

To obtain tempo curves, we estimate the local tempo from the measure annotations and corresponding time signature annotations indicating beats per measure from [22]. From these, we derive a tempo curve for each performance (version), indicating the average tempo per measure. For enhanced readability, we suppress local fluctuations by using a moving average filter of length 11 measures. To reduce the influence of individual performances but rather capturing the typical effects occurring in most performances, we calculate a median tempo curve across all 16 performances (see Figure 1). To relate these measurements with the dramatic structure, we further highlight changes in vocal activity. To this end we apply the singer (role) annotations as provided in the WRD [22] and overlay them in the plots as transparent colored areas. 

To provide a practical way of engaging with the visualized data, we make the visualizations accessible with an interactive interface that allows intuitive navigation and control. This tool enables users to independently toggle all currently available parameters, including tempo curves from all 16 individual performances, their mean and median values, as well as harmonic progressions. Additionally, further annotations such as speaker roles, key and time signatures, and tempo markings can be displayed or hidden as needed. Users can define specific excerpts and customize the combination of parameters and annotations according to their analytical focus. A zoom functionality further enhances usability by allowing users to closely examine individual passages or gain a broader overview of entire scenes. The configuration of all these aspects can be individually. 

## 4. VISUALIZATIONS OF SIEGFRIED, ACT III 

We now want to demonstrate the potential of this multimodal approach and discuss its musicological implications. To this end, the following visualizations and analyses focus on the three scenes from the third act of Siegfried. Each is structured as a dialogue and centers around a dramatic conflict between two characters. (For consistency, the character “Der Wanderer” is referred to as “Wotan” throughout the text. Due to its extent, we divide Scene 3 into two separate visualizations.) 

## 4.1 Scene 1 – Wotan and Erda (Figure 2) 

The first scene of Act III in Siegfried is characterized by the encounter between Wotan (light blue areas) and Erda (light green areas), which unfolds as a dramatic confrontation. The scene begins with an instrumental prelude (uncolored) in G minor (−2 region). Wotan’s entrance at measure 74 coincides with a return to this tonic key, reinforcing his authoritative presence. His initial statements maintain a steady tempo of approximately 95 beats per minute (bpm), while his harmonic language remains relatively stable around E♭ major (−3 region). A significant shift occurs with Erda awakening in measure 121. Her entrance is characterized by a sudden tempo decrease to around 60 bpm, paired with increased harmonic instability, as indicated by significant tonal changes in the visualization. These elements musically distinguish Erda’s initial state from Wotan’s dominance, which is also mirrored in tempo: Erda gradually aligns with Wotan’s faster pace as the argument intensifies. By measure 291, she abandons her earlier slow tempo, gradually approaching Wotan’s tempo. The culmination of their confrontation occurs at measure 351, where Wagner introduces a long fermata (“langes Schweigen”). This moment of silence marks the dramatic turning point before Wotan’s concluding monologue, in which he reasserts his dominance, returning to E♭ major (−3 region). 

The tonal language of both characters also undergoes a development. Erda has two harmonically rather stable moments, first around measure 200 and again from measure 230, both of which evoke reminiscences of other characters: first the Norns in E major, then Brünnhilde in E♭ major (cf. [9]). The tonality of Wotan’s passages, on the other hand, becomes increasingly unstable throughout the scene. During the final phase of the confrontation (mm. 280–351), the music of both characters is harmonically instable. This reflects the dramatic escalation of their conflict. 

For the whole scene without the instrumental prelude, Newcomb suggests an ABA form (A: mm. 74–189, B: mm. 190–356, A: mm. 357–439). In our visualization (fig. 2) this is clearly reflected in the black zones around the −3 scale framing the outer A sections. The B section stands out most clearly, beginning with a harmonic shift from E♭ 

144 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
250<br>200<br>150<br>(bpm)<br>100<br>Absolute diatonic scale po<br>654321012345 50<br>0<br>450 500 550 600 650 700 750 800<br>Time (measures)<br>Figure 3. Siegfried, Act III, Scene 2. Visualization of diatonic scale probabilities and tempo curve (as in Fig. 1). Transpar-<br>ent, colored areas indicate the singer activity of characters Wotan (light blue) and Siegfried (light yellow).<br><!-- End of picture text -->

major to E major (+4), corresponding to the most intense phase of the dramatic conflict and its escalation. This is reflected in both tempo and harmonic instability. 

## 4.2 Scene 2 – Wotan and Siegfried (Figure 3) 

Scene 2 can be divided into three main sections that reflect the dramatic and musical development of the encounter between Wotan (light blue areas) and Siegfried (light yellow areas). The first section (mm. 468–619) consists of a mutual interrogation, where both characters engage in a question–answer exchange. First, Wotan questions Siegfried (mm. 483–551), ending with a mocking laugh (m. 551), followed by Siegfried questioning Wotan (mm. 551–619), which concludes similarly with laughter in measure 619 [17]. The second section (mm. 619–658) forms a transitional episode in which tensions arise and Wotan tries to persuade Siegfried not to awaken Brünnhilde. Finally, the third section (mm. 659–741) marks the open escalation of the conflict, culminating in Siegfried’s destruction of Wotan’s spear. These sections are clearly articulated through changes in tempo and harmonic progression, providing a structural and expressive framework for the scene. 

The interrogation section is defined harmonically by a shift to the −4 and −3 scales. At first Siegfried appears alone, advancing through a more harmonically stable region centered on B major (+5 scale) and G major (+1). This initial passage also features the highest tempo of the scene, reaching approximately 125 bpm. The transition towards the interrogation is marked by Wotan’s question, “Wohin, Knabe, heißt dich dein Weg?” (mm. 483ff.), which initiates a modulation towards the −2 and subsequently the −4 scale. The tempo, however, only begins to decline with Wotan’s second question concerning Brünnhilde and never returns to its earlier peak. From this point on, Wotan consistently adopts a slower pace compared to Siegfried, with these tempo differences becoming increasingly pronounced throughout the exchange. While Siegfried maintains a relatively steady tempo around 120 bpm—reflecting his determination and forward momentum—Wotan’s responses progressively decelerate. 

This tempo design continues in the middle section (mm. 619–658), where Wotan reaches his lowest point of approximately 75 bpm, while Siegfried remains at around 

120 bpm. Harmonically, the section begins with stability on the 0 scale, but as Wotan makes his emotional appeal to Siegfried not to awaken Brünnhilde, a modulation unfolds through F major toward B♭ major (−1 and −2 scale). 

The third section (mm. 659–741) begins with a renewed escalation, introduced by an upbeat that quickly restores Siegfried’s characteristic tempo of around 120 bpm. He then makes an explicit threat, demanding that Wotan clear his path. From measure 667 onwards, Wotan responds with a notably more combative stance, reflected in a significantly increased tempo of about 100 bpm. This energetic exchange continues until Wotan reaches a peak of 120 bpm at measure 684, where he mentions the loss of his power. The conflict culminates in a climactic confrontation as Siegfried shatters Wotan’s spear at measure 740—a moment that aligns with a tempo peak of approximately 120 bpm, reached through a continuous acceleration beginning at measure 704. The harmonic structure in this final section remains unstable throughout. Following this climax, a pronounced ritardando in measure 742 sharply reduces the tempo to about 60 bpm, leading to Wotan’s final admission of defeat (mm. 747ff.). 

## 4.3 Scene 3 – Siegfried and Brünnhilde (Figure 4) 

Scene 3 unfolds in two major parts: Siegfried’s solo section (up to m. 1066), and the dialogue with Brünnhilde (light purple areas) from measure 1067 onwards, which may be understood as a sort of operatic duet [16]. 

This division is clearly reflected in the harmonic structure. During Siegfried’s section, the harmony remains relatively stable on the +4 and +3 scales (E major and A major). Starting around measure 935—marked by an abrupt increase in tempo—the music enters a longer modulatoring passage that gradually leads into the second part. The beginning of the duet is firmly grounded in C major, indicated by a shift to the 0 scale in the visualization, reinforcing a structural break between the two halves of the scene. The second part (from m. 1067) can be divided into three subsections. The two outer sections are duet-like (mm. 1067ff. and from m. 1719), both characterized by a strong emphasis on C major (0 scale) [15] and a relatively stable tempo. In the first passage, the tempo gradually increases, while in the second passage it reaches the scene’s (and act’s) peak 

145 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
250<br>200<br>150<br>(qm)<br>100<br>Absolute diatonic scale mpo<br>654321012345 50<br>0<br>850 900 950 1000 1050 1100 1150 1200<br>Time (measures)<br>250<br>200<br>150<br>(bpm)<br>100<br>Absolute diatonic scale Tempo<br>654321012345 50<br>0<br>1300 1400 1500 1600 1700<br>Time (measures)<br><!-- End of picture text -->

Figure 4. Siegfried, Act III, Scene 3 Combined visualization of the final scene. Singer activities (roles) are indicated by transparent colors: Siegfried (light yellow), Brünnhilde (light purple), and overlapping segments where both characters sing simultaneously (light brown). 

at approximately 175 bpm. In both cases, the characters move largely synchronously, with no pronounced tempo contrast between them. Both duets correspond in terms of affect and structure: the first reflects Brünnhilde’s passionate yet restrained turn towards Siegfried, while the second is a moment of their ultimate affirmation [16]. Between these two passages lies a transitional section, which can be interpreted as a process of overcoming fear. Accordingly, the dramatic turning points of the scene are shaped by fearrelated affects: first, Siegfried’s fear of sexual intimacy (mm. 930ff.) and his uncertainty or lack of understanding (mm. 1151–1278); then Brünnhilde’s experience of sexual fear (mm. 1279–1369), followed by her fear of losing her former identity and knowledge (mm. 1361–1478) [18]. 

We now turn to one particular passage of this transitional section, where Brünnhilde’s fear becomes more prominent. It takes the form of an intense dialogue (mm. 1277–1475), in which she gradually realizes that she is no longer part of the divine world of the Valkyries. This transformation unfolds through three distinct losses, triggered by the gaze on her horse, Grane, in mm. 1285ff. 

The first phase of this transformation is marked by Brünnhilde’s realization of her lost attributes—shield (mm. 1308ff.), helmet (mm. 1312ff.), and breastplate (mm. 1324ff.)—as symbols of her former power. This causes her a profound shock which leads to a strong physical rejection of Siegfried (m. 1357) and a desperate reminder of Valhalla (mm. 1365ff.) and culminates in the admission of her changed identity (“Brünnhilde bin ich nicht 

mehr”) in measures 1384ff. (see e.g. [23, 24]). The progression of tempo and harmony reflects this emotional distress. The tempo curve oscillates between acceleration and deceleration, each corresponding to the character’s emotional state. Brünnhilde’s entries coincide with tempo reductions, while Siegfried, embodying decisiveness, consistently initiates his responses at a significantly faster pace. Despite these more locally fluctuations, the overall tempo trajectory gradually increases. 

Siegfried’s subsequent response intensifies the tempo once more, before Brünnhilde articulates further losses: the fading of her wisdom and foresight (mm. 1405ff.) and the loss of her sight (mm. 1421ff.). At this emotional peak, Brünnhilde’s fear and agitation reach their highest intensity. In contrast to the earlier pattern, Siegfried’s replies are increasingly slow, while Brünnhilde’s tempo remains elevated at around 130 bpm. Harmonically, this peak is marked by significant instability (mm. 1410ff.) before a more stable passage emerges on the −5 scale toward the end. 

## 5. DISCUSSION 

The visualizations illustrate how the parameters of tempo and harmony correlate with the unfolding drama, providing an external structural coherence to Wagner’s music. For example, the initial contrast between Wotan’s stable tempo and harmonic centering and Erda’s slow and harmonically unstable or shifting responses in Scene 1 

146 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

clearly reflects their dramatic interaction. Similarly, in Scene 2, Siegfried’s consistently higher tempo highlights his determination and forward momentum. Moreover, the tempo evolution, particularly evident in Erda’s initially delayed responses becoming progressively quicker throughout Scene 1, highlights the dramatic interplay. This does not imply that the development of these parameters or their character-specific manifestation directly indicates concrete emotions or mental states; rather, it reflects dramatic tension and relaxation. For instance, Wotan’s slower tempo in Scene 2 does not necessarily signal uncertainty compared to Scene 1; instead, it suggests a calmer, more measured demeanor, akin to a wise grandfather facing his exuberant grandson. 

Nevertheless, a clear pattern emerges in the first two scenes. Initially, distinct tempo differences are established to differentiate the characters. With increasing escalation of conflict, these tempos converge, above all through the acceleration of the slower character towards the faster one. Scene 3, however, presents a more nuanced scenario, particularly during the dialogue in the middle part (mm. 1277–1475). It centers around the psychological process Brünnhilde undergoes due to her loss of identity rather than fundamental antagonism. Consequently, the tempo-difference pattern followed by convergence is initially present, yet both characters simultaneously experience gradual tempo increases while maintaining their different positions. Additionally, in Siegfried’s final responses (mm. 1390ff. and 1412ff.), he slightly reduces the tempo, reacting empathetically rather than further escalating the conflict. 

A similar correlation can be observed regarding harmony. The differentiation between stable and unstable harmonic regions effectively aligns with the progression of drama. Less functionally stable harmony, often accompanies heightened dramatic tension or the emotional states of the characters (e.g., Wotan’s rapid sixteenth-note figurations at the beginning and towards the end of Scene 1). However, this harmonic correlation appears less distinctly pronounced than the tempo progressions. 

Moreover, harmonic progression—in particular, shifts between distinct tonal regions—can serve as an effective indicator of large-scale formal segmentation. In Scene 2, for example, the question-and-answer section, dramaturgically framed by Siegfried’s laughter, is clearly situated within the −4 and −3 regions, setting it apart from both the preceding and the following sections. Similarly, Siegfried’s solo passage at the beginning of Scene 3 remains harmonically stable within the +3 and +4 regions. The following modulatory phase leads directly to a dramatic turning point: Brünnhilde’s awakening. We can find additional examples of such segmentation in the two consecutive monologues in Scene 3 from both Brünnhilde (mm. 1472–1560) and Siegfried (mm. 1560–1613), which are clearly distinguished from their surroundings in both tempo and harmony. 

## 6. CONCLUSIONS AND FUTURE WORK 

The analyses presented in this study support Newcomb’s reading that musical form in Wagner’s works is best understood as a dynamic musical process shaped by dramatic development [9]. We have shown that his interpretation of formal coherence—derived from the interaction of musical parameters—can be extended to the other two scenes in Act III. As the visualizations reveal, this perspective also enables the identification of different strategies in the progression of parameters (tempo, tonality, singers) and their correlation with the dramatic content. While Scene 2 exhibits a structure similar to Scene 1 with contrasting tempi converging toward a climax, its formal and dramaturgical setup is more complex. Scene 3 increases this complexity even further, portraying a psychological transformation rather than a clearly external conflict. These differences illustrate that tempo and harmonic progression play an important role not only on a local level, in the musical articulation of individual protagonists, but also on a larger scale, reflecting broader dramatic developments across entire scenes or acts—again confirming Newcomb’s hypothesis [9]. As the act unfolds, these layers become increasingly overlapped, revealing compound strategies of dramatic intensification. This contributes to an overall increase in structural density across the act, echoing McCreless’s observation of a similar increase of harmonic density from Acts I and II to Act III [3]. This may also explain why Lorenz’s model of periodization fits in some cases, but not in others [1]. 

While our visual analyses occasionally align with traditional analytical findings, particularly regarding major turning points, these conventional approaches offer limited guidance for comprehensive structural understanding. Their focus often remains on localized formal types or philologically oriented readings [17,18,23], or they refer to the libretto [16]. In contrast, the multidimensional method presented here allows for large-scale analyses of extended operatic works, offering a replicable framework that may be applied to the entire Ring cycle and other compositions. 

In future work, automated methods could support the expansion of this approach to include additional parameters such as dynamics, pitch, instrumentation [25] and annotations such as leitmotifs [14]. Furthermore, while the present study focuses on parameters that are largely independent of specific performances, the tempo parameter, in particular, is strongly shaped by individual decisions of the conductor. Detailed performance analyses could therefore offer valuable information, both by comparing different interpretations and by examining where performers diverge from the tempo indications in the score [26]. Additional annotations, e. g. tempo markings, could be integrated into the visualizations to highlight such interpretive deviations more clearly. 

## 7. ACKNOWLEDGMENTS 

This work was supported by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) un- 

147 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

der Grant No. 252013209 (DFG MU 2686/7-2, DFG KL 864/4-2). The International Audio Laboratories Erlangen are a joint institution of the Friedrich-AlexanderUniversität Erlangen-Nürnberg (FAU) and Fraunhofer Institute for Integrated Circuits IIS. 

We especially thank Moritz Schumacher for his work in developing the interactive interface presented in this paper. 

## 8. REFERENCES 

- [1] A. Lorenz, Der musikalische Aufbau des Bühnenfestspieles “Der Ring des Nibelungen”, ser. Das Geheimnis der Form bei Richard Wagner. Max Hesses, 1924, vol. 1. 

- [2] C. Dahlhaus, “Formprinzipien in Wagners ‘Ring des Nibelungen’,” in Beiträge zur Geschichte der Oper, H. Becker, Ed. Regensburg, Germany: Bosse, 1969, pp. 95–129. 

- [3] P. McCreless, Wagners’s Siegfried: It’s Drama, History and Music. UMI Research Press, 1982. 

- [4] S. McClathie, Analyzing Wagner’s Operas: Alfred Lorenz and German Nationalist Ideology. Univ. of Rochester Press, 1998. 

- [5] A. Newcomb, “Those images that yet fresh images beget,” The Journal of Musicology, vol. 2, no. 3, pp. 227–245, 1983. 

- [6] D. Trippett, Ed., Wagner in Context. Cambridge Univ. Press, 2024. 

- [7] C. Weiß, R. Kleinertz, and M. Müller, “Möglichkeiten der computergestützten Erkennung und Visualisierung harmonischer Strukturen–eine Fallstudie zu Richard Wagners ‘Die Walküre’,” Bericht zur Jahrestagung der Gesellschaft für Musikforschung (GfM), Mainz, Germany, 2016. 

- [8] C. Weiß, F. Zalkow, M. Müller, S. Klauk, and R. Kleinertz, “Versionsübergreifende Visualisierung harmonischer Verläufe: Eine Fallstudie zu Wagners Ring-Zyklus,” in Proceedings of the Jahrestagung der Gesellschaft für Informatik (GI), Chemnitz, Germany, 2017, pp. 205–217. 

- [9] A. Newcomb, “The birth of music out of the spirit of drama: An essay in Wagnerian formal analysis,” 19thCentury Music, vol. 5, no. 1, pp. 38–66, 1981. 

- [10] J. P. E. Harper-Scott, “Form and structure,” in The Cambridge Companion to Wagner’s Ring Cycle, M. Berry and N. Vazsonyi, Eds. Cambridge, England: Cambridge Univ. Press, 2020, pp. 102–123. 

- [11] T. S. Grey, Ed., Wagner’s Musical Prose: Texts and Contexts. Cambridge Univ. Press, 1995. 

- [12] M. Bribitzer-Stull, Understanding the Leitmotif: From Wagner to Hollywood Film Music. Cambridge Univ. Press, 2015. 

- [13] D. Baker and D. Müllensief, “Perception of leitmotives in Richard Wagner’s ‘Ring des Nibelungen’,” in Proceedings of the 14th Int. Conference for Music Cognition and Perception, San Francisco, CA, USA, 2016, p. 207. 

- [14] M. Krause, F. Zalkow, J. Zalkow, C. Weiß, and M. Müller, “Classifying leitmotifs in recordings of operas by Richard Wagner,” in Proceedings of the International Society for Music Information Retrieval Conference (ISMIR), 2020, pp. 473–480. 

- [15] K. Berger, Beyond Reason: Wagner Contra Nietzsche. Univ. of California Press, 2017. 

- [16] J. Schläder, Das Opernduett: ein Szenentypus des 19. Jahrhunderts und seine Vorgeschichte, ser. Studien zur Geschichte und Theorie der dramatischen Künste. Max Niemeyer, 1995, vol. 6. 

- [17] H. Danuser, “Des Wanderers Siegfried. Kein Idyll,” in Wagners Siegfried und die (post-)heroische Moderne, T. Janz, Ed. Würzburg, Germany: Königshausen & Neumann, 2011, pp. 271–290. 

- [18] K. Hottmann, “Fürchten oder Nicht-Fürchten? Zur Dramaturgie der Schluss-Szene des ‘Siegfried’,” in Wagners Siegfried und die (post-)heroische Moderne, T. Janz, Ed. Würzburg, Germany: Königshausen & Neumann, 2011, pp. 291–324. 

- [19] C. Weiß, V. Arifi-Müller, M. Krause, F. Zalkow, S. Klauk, R. Kleinertz, and M. Müller, “Wagner ring dataset: A complex opera scenario for music processing and computational musicology,” Transactions of the International Society for Music Information Retrieval (TISMIR), vol. 6, no. 1, pp. 135–149, 2023. 

- [20] C. Weiß and M. Müller, “From music scores to audio recordings: Deep pitch-class representations for measuring tonal structures,” ACM Journal on Computing and Cultural Heritage (JOCCH), vol. 17, no. 3, pp. 45:1–19, 2024. 

- [21] ——, “Computergestützte Visualisierung von Tonalitätsverläufen in Musikaufnahmen. Möglichkeiten für die Korpusanalyse,” in Instrumentalmusik neben Haydn und Mozart. Analyse, Aufführungspraxis und Edition, S. Klauk, Ed. Würzburg, Germany: Königshausen & Neumann, 2009, pp. 107–130. 

- [22] C. Weiß, V. Arifi-Müller, M. Krause, F. Zalkow, S. Klauk, R. Kleinertz, and M. Müller, “Wagner Ring Dataset: A complex opera scenario for music processing and computational musicology,” Transaction of the International Society for Music Information Retrieval (TISMIR), vol. 6, no. 1, pp. 135–149, 2023. [Online]. Available: https: //transactions.ismir.net/articles/10.5334/tismir.161 

- [23] W. Breig, “Anmerkungen zu Brünnhildes Musik,” in Musik. Frau. Sprache. Interdisziplinäre Frauen- und 

148 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

Genderforschung an der Hochschule für Musik und Theater Hannover, K. Beyer and A. Kreutziger-Herr, Eds. Herbolzheim, Germany: Centaurus, 2003, pp. 173–187. 

- [24] S. Henze-Döhring, “Liebe – Tragik – Zur musikdramatischen Konzeption der Brünnhilden-Gestalt,” in “Das Weib der Zukunft”: Frauengestalten und Frauenstimmen bei Richard Wagner, S. Vill, Ed. Stuttgart and Weimar, Germany: Metzler, 2000, pp. 124–152. 

- [25] M. Krause and M. Müller, “Hierarchical classification for instrument activity detection in orchestral music recordings,” IEEE/ACM Transactions on Audio, Speech, and Language Processing (TASLP), vol. 31, pp. 2567–2578, 2023. 

- [26] M. Allis, “Richter’s Wagner: a new source for tempi in Das Rheingold,” Cambridge Opera Journal, vol. 20, no. 2, pp. 117–148, 2008. 

149 

