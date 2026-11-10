---
paper_id: "000008"
year: 2021
title: "Visualizing Intertextual Form with Arc Diagrams: Contour and Schema-based Methods 74-80"
source_url: "https://archives.ismir.net/ismir2021/paper/000008.pdf"
---

# **VISUALIZING INTERTEXTUAL FORM WITH ARC DIAGRAMS: CONTOUR AND SCHEMA-BASED METHODS** 

**Aaron Carter-Enyi** Morehouse College 

aaron.carterenyi@morehouse.edu 

**Nathaniel Condit-Schultz** 

## **Gilad Rabinovitch** 

Florida State University Georgia Institute of Technology 

grabinovitch@fsu.edu 

natcs@gatech.edu 

### **ABSTRACT** 

The visualizations in Wattenberg’s _Shape of Song_ (2001) were based on pitch-string matching, but there are many other equivalence classes and similarity relations proposed by music research. This paper applies recent algorithms by Carter-Enyi (2016) and Carter-Enyi and Rabinovitch (2021) with the intention of making arc diagrams more effective for research and teaching. We first draw on Barber’s intertextual analysis of Yorùbá _Oríkì_ , in which tone language texts are circulated through various performances (Barber 1984). Intertextuality is exemplified through a 2018 composition by Nigerian composer Ayò Olúranti, then extended to Dizzy Gillespie’s solo in his recording of “Blue Moon” (ca. 1952). Example visualizations are produced through an open-source implementation, ATAVizM, which brings together contour theory (Quinn 1997), schema theory (Gjerdingen 2007), and edit distance (Orpen and Huron 1992). Applications to the music of Bach and Mozart demonstrate that an Africancentered analytical methodology has utility for music research at large. Computational music research can benefit from analytical approaches that draw upon humanistic theory and are applicable to a variety of musics. 

### **1. INTRODUCTION** 

A promising visualization method for musical form and melodic relationships is the arc diagram, proposed by Wattenberg [1].<sup>1</sup> An arc diagram is a type of network diagram in which the nodes are aligned along a single axis. In the case of a single piece of music (intraopus), the axis represents time and the arcs connect matches between segments of the piece. In the case of multiple works (interopus), pieces might be arranged alphabetically or chronologically as nodes along the axes, and content matches may still be represented through a network of arcs. Applied to music, this visualization technique emphasizes melodic connections that permeate music instead of stressing sectional di- 

> 1 Wattenberg developed an art exhibit and web app, called the _Shape of Song_ [2], which is now defunct. 

> © Aaron Carter-Enyi, Gilad Rabinovitch, Nathaniel ConditSchultz. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). **Attribution:** Aaron Carter-Enyi, Gilad Rabinovitch, Nathaniel Condit-Schultz, “Visualizing Intertextual Form with Arc Diagrams: Contour and Schema-based Methods”, in _Proc. of the 22nd Int. Society for Music Information Retrieval Conf.,_ Online, 2021. 

visions. Understanding form as intertextual (both intraopus and interopus) fits with Africana musics and the zeitgeist of the information age; of being globally connected through the Internet. An intertextual approach is antithetical to western notions of musical works as individual artistic utterances. 

In Wattenberg’s _Shape of Song_ , “Each arc connects two matching passages... [containing] the same sequence of pitches” [1]. This is a simplistic view of melodic associations. Arc diagrams have since been applied to audio and symbolic data to highlight a much greater variety of musical features [3, 4]. We present new visualizations produced using ATAVizM<sup>2</sup> , which brings together contour theory [5,6], schema theory [7], and edit distance [8]. Because these methods reveal patterns within and between works, we consider them intertextual approaches to music analysis. In Yorùbá _Oríkì_ , tone language texts, such as _owé_ (proverbs), are circulated through various performances [9]. Intextuality is exemplified by Nigerian composer Ayò Olúranti’s "O. mo.lúàbí" (2018) and Dizzy Gillespie’s solo on “Blue Moon” (ca. 1952). Arc diagrams visualize the output of recent pattern discovery algorithms by CarterEnyi [10] and with Rabinovitch [11]. The first algorithm was developed specifically for understanding the mapping of speech tone to song in African cultures. Applications of the same implementation to the music of Bach and Mozart demonstrate the extensibility of African-centered methodologies, which may contribute novel approaches to music research at large. 

### **2. UNDERSTANDING FORM AS INTERTEXTUAL** 

Barber argues against seeing a "work of literature as an isolated artifact," considering the alternative of deconstruction as practiced by Derrida [9]. Taking Yorùbá praisesinging ( _Oríkì_ ) as an example, Barber points out that the concept of "wholeness is simply inappropriate" for oral literature which is "constituted and reconstituted only through the participation of many people," including a "chain of performers" and audiences. Each performance is neither entirely unique nor entirely the same, they are related intertextually. When you deconstruct an _Oríkì_ performance to short praise names, proverbs and riddles it is composed of, there is really no difference between interopus and intraopus analysis. 

> 2 Desktop and web versions of the app and source code are available: atavizm.org; radar.auctr.edu/atavizm; github.com/carterenyi/atavizm 

74 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

The concept of intertextuality is not new to music scholarship. _Oríkì_ itself has often been considered both a form of literature and a form of music. If Barber’s description of _Oríkì_ reminds you of the characteristics of jazz or hip hop, we agree. Thinking "interopus" about music challenges notions of authorship, copyright, and intellectual property. Notions that did not exist in many precolonial societies and still struggle to hold sway in many creative economies. Patterns may be found across works and throughout an individual work, repeated with variation. This is exemplified by Yorùbá proverbs Olúranti selected as the basis for "O. mo.lúàbí" (2018). Echoed by Gillespie’s improvisational gestures in his recording of "Blue Moon," which both quotes and hints at Lorenz/Hart’s melody. Gjerdingen’s schema theory [7] suggests that music making in 18th-century Europe relied on a shared stock of skeletal patterns, which explains the rapid creation of compositions and improvisations. Our application to "artworks" by Bach and Mozart will show how the Prinner schema emerges as a skeletal structure in two pieces with highly contrasting surface textures. 

### **3. OPERATIONALIZING INTERTEXTUALITY** 

Musical themes, motives, and formulas are often transposed or modified and remain recognizable. Such relationships are relevant for both inter- and intraopus analysis. For example, a fugue subject is initially stated in the tonic key in a monophonic texture. The answer is a response in a polyphonic texture in a related key (usually dominant). Sometimes the answer is an exact transposition (real answer), and sometimes the answer is transposed and modified (tonal answer). Wattenberg offers the possibility of matching melodic intervals rather than pitch strings, which would match some subjects and answers, but not a subject and tonal answer, in which the subject is both transposed and modified. There are generic contrapuntal skeletons throughout 18th-century European music (schemata) that are embellished in various ways on the musical surface [7]. 

How do we formally relate the Yorùbá texts in poetry and in song? The “licks” of bebop musicians? A subject and tonal answer? Or schemata in 18th-century European music? Velardo et al. name four bases for Symbolic Melodic Similarity (SMS) systems: cognition, music theory, mathematics, and hybrid approaches (2017). The authors mention pitch-class set theory (with a basis in music theory and mathematics), but not contour theory (with a foundation in cognition, music theory, and mathematics, e.g., Quinn [6]), or schema theory (Gjerdingen [7]). This paper focuses on a contour-based method [12] and a schema-based method [11] to operationalize intertextuality on and (slightly) underneath the musical surface, respectively. Of the four pieces analyzed, only the Mozart analysis bears resemblance to a conventional form analysis (e.g., ABA for an entire work). Arc diagrams offer the possibility of new perspectives on form that are difficult to communicate without a network. Musical form in this context is an emergent property of intertextual relations. 

### **4. A CONTOUR-BASED METHOD** 

Carter-Enyi’s contour-level algorithm was developed based on an extensive analysis of Ìgbò and Yorùbá speech, chant and music as well as a perceptual study with 1409 participants [12]. Contour levels are a modified contour theory based on a new understanding of tone-level languages and how tone levels are mapped to music. The following analyses demonstrate the method’s effectiveness as a basis for analyzing and visualizing musical forms. 

### **4.1 "O. mo.lúàbí" by Ayò Olúranti (2018)** 

As a composer, Olúranti carefully sets Yorùbá texts based on their implied pitch and rhythmic contour [13]. "O. mo.lúàbí" is based on a set of Yorùbá _owé_ (proverbs and adages) about good character. The Yorùbá language has three tone-levels: low (à), mid (a, no accent), and high (á). Less is known about the extent to which rhythm is a contrastive element of speech, but it is clear that lexical tone distinguishes many words (47 % of two-syllable words [12]). The following are the six main proverbs incorporated into the work in order of their appearance. For each, the tone sequence is indicated with L for low tone, M for mid tone, and H for high tone. 

1. Ìwà l’èsìn<sup>3</sup> (LL LL). Translation: Character is religion (meaning religion devoid of good character is worthless) 

2. Ìwà l’o.ba àwúre (LL MM LHM). Translation: Supplication is important, good character even more. 

3. Ìwà l’òrìs.à, bí a bá ti hùú sí ni fií gbè’ni sí (LL LLL, H M H M LH H M MH LMH). Translation: Character is god (or salient). One’s behavior determines one’s attitude. 

4. Ká wí be.é, ká bá a be.é, iyì ènìyàn nìye.n (H H H, H H M H, ML LLL LM). Translation: A man is honorable when his word is his bond. 

5. O. mo.lúàbí (MMHLH). Translation: A child born of good character 

6. Tí a ó bàá <u>jé</u> O. s.áká ká kúkú <u>jé</u> O. s.áká. Bí a ó bàá <u>jé</u> Òs.oko ká kúkú <u>jé</u> Òs.oko. Os.áká-Òs.oko ko ye.ni (H M LH H MHH H HH H MHH. H M H LH H LMM H HH H LMM. MHH-LMM M MM). Translation: Be certain without doubt. Be uncertain without doubt. Being neither here nor there is undesirable. 

Because Yorùbá is a tone language, the proverbs have implied contours which Olúranti adapts as themes and motives. Some longer proverbs are broken up or abbreviated (particularly 6). Instances of each tone-level sequence (strings and substrings in the symbolic data) are indicated as nodes between color-coded arcs in Figure 1. Because of the similarity in melodic shape but flexibility in pitch height and melodic intervals, the setting of tone language texts has an affinity to contour theory. However, contour theory, as formalized by Morris [5], could not be applied to this music because it first requires manual segmentation (making it incompatible with pattern discovery) and is intended for segments without any repeating pitches (such 

> 3 Subdot indicates an open vowel or an "esh" instead of s. Underlining is substituted for a subdot where diacritics must be combined. 

75 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 



**Figure 1** . Contour-based intraopus arc diagram of Olúranti’s "O. mo.lúàbí" (2018) 



<!-- Start of picture text -->
wa l'O - ba wu<br>1 0<br>2<br>9g.<br>aL<br><!-- End of picture text -->

**Figure 2** . Contour equivalence class for three tone-level Yorùbá proverb and one of Olúranti’s settings. 

as a 12-tone row). While Olúranti’s piece may be considered post-tonal and through-composed, repeated pitches are used, often to represent the repetition of linguistic tones.<sup>4</sup> Carter-Enyi’s addition of “windowing” to create contour levels<sup>5</sup> is based on the concept of tone levels in African languages [12] and is ideal for finding intertextual proverbs in Olúranti’s polyphonic composition (see Figure 2. Insertions (epenthesis) and deletions (elision) are common in language, so for language-based music allowing for edits to patterns is necessary. Contour level equivalence, as an effective associative method, may be enhanced through similarity metrics such as edit distance [8] when appropriate. 

> 4 Schmuckler has applied concepts of contour theory computationally [14]. However, his method deviates from most music theory and has not been implemented as an open-source toolbox or application. 

> 5 Quinn’s binary (0,1) annotation of pairwise comparisons was another necessary improvement over Morris [6] 

The intertextuality of Olúranti’s piece is revealed in two ways by the diagram. First, the color-coding groups pattern instances by their link to a preexisting proverb (interopus). Second, the networks of equivalence and similarity are linked within the piece by arcs. Some proverbs occur in a limited range of the piece (notably "Kawibe..." and "Osaka..."), so are sectional within the piece, but still intertextually linked to Oríkì performance at large. Several proverbs come together in the final section, a textually and musically cohesive conclusion. 

### **4.2 "Blue Moon" by Dizzy Gillespie (ca. 1952)** 

The notion of intertextuality is nothing new in jazz scholarship, signifying jazz’s spirit of both continuity and innovation. Carter-Enyi’s algorithm is apt for pattern discovery in jazz improvisation. Unlike Olúranti’s "O. mo.lúàbí," where higher precision in contour matching is desirable, in this case, we applied a more inclusive match by reducing the “window size” and reducing “redundant” contour slices [10]. The degree of flexibility or rigidity in finding melodic relationships depends on the task at hand. In the context of jazz improvisation, more inclusive settings resonate with insider knowledge of listeners to jazz, who may recognize many extrapolations. Figure 4 includes parentheses around repeated notes to indicate that they were ignored in the analysis. To make the contour equivalence class more inclusive, only one degree of adjacency for contour comparison was used (see Figure 5). Additionally, a reduction technique was used where identical columns of the matrix are collapsed to a single column, indicated by multiple notes being mapped to a single contour node in Figure 5. 

76 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 



Similar to Olúranti’s "O. mo.lúàbí," Dizzy Gillespie’s recording of "Blue Moon" is based on a preexisting "text," the Lorenz and Hart song. As in _Oríkì_ and in Olúranti’s work, intertextuality is a core part of jazz, which in bebop has an objective quotation or recitation of a complete text (the "head") and a subjective interpolation of the text in the solo. Because the insider knowledge of listeners in the jazz tradition includes recognizing licks that seem to quote the head in the solo, we set the algorithm to be highly inclusive. 

### **4.3 "Fugue in C Minor" by J. S. Bach (BWV 847)** 

**Figure 3** . Contour-based inter/intraopus arc diagram of Gillespie’s "Blue Moon" (ca. 1952) 



**Figure 4** . Theme from "Blue Moon" (Rodgers/Hart 1934) 

Figure 5’s class identifies a wide variety of similar shapes as equivalent strings. A contour motive from the opening melody of “Blue Moon” reappears through Gillespie’s solo.<sup>6</sup> The most inclusive settings for Carter-Enyi’s algorithm [10] are used to relate contours that are expanded or contracted. While it may be debatable whether some of the instances returned by the algorithm are indeed quotations of the theme, one might indeed question the gesture in Figure 5. However, in mm. 41-44, the quotation of the theme is apparent because of a sequence of descending thirds over iterations of the contour. This sequence is visible in the arc diagram (Figure 3 where there is a cluster of instances about two-thirds away through the piece. Although the contours in mm. 41-44 are in expanded form compared to the “head,” these iterations are tied to the theme because of the use of sequence and the salience of similar scale degrees. 

- 6 The transcription analyzed is here is by Jacques Gilbert, many more 

- are available on his website [15] 



<!-- Start of picture text -->
1 0 0<br>0 0 0<br><!-- End of picture text -->

**Figure 5** . Improvisational gesture reduced to a simple contour equivalence class 

The following applications demonstrate the effectiveness of an African-centered computational approach for discovering meaningful patterns in European classical music. In Figure 6, all statements of the fugue subject of BWV 847 are connected through blue arcs, representing a network between the introduction of the subject and all subsequent statements. The subject has cardinality 20 and, through eight iterations,<sup>7</sup> accounts for over 20 % of the pitch content of the piece (160 out of 750 notes). CarterEnyi presents a method for calculating a single equivalence class that incorporates all subject entries and no other segments using his contour level approach [12]. Specifically, a 4-degree window of adjacency is sufficient to recognize all subject statements without any false positives (see Figure 7). 

### **5. A SCHEMA-BASED METHOD** 

Gjerdingen’s schema theory posits shared skeletal contrapuntal patterns in European music of the 18th century. A limited number of skeletal prototypes in composition and improvisation resonates with existing theories of counterpoint and keyboard playing (figured and unfigured bass traditions). Schemata may be more abstract than the contours of Yorùbá proverbs, yet schema theory also suggests that 18th-century European music is also an intertextual tradition rather than a collection of distinct "masterworks." Therefore, schemata are important tools for interopus algorithmic analysis. The following analysis relates pieces by Bach and Mozart that are contrasting on the surface, yet draw extensively on Gjerdingen’s Prinner schema: a soprano skeleton of 6-5-4-3 above a bass skeleton of 4-3-2-1 or 4-3-2-5-1, typically harmonized with IV-I6-vii6-I or a similar harmonic progression. 

We have operationalized schemata as scale-degree skeletons that may be matched in various reductions of the same piece [11]. The method awards points in a score matrix for different syntagmatic (relational) features of notes. In Figure 8, the first row awards points to notes on a strong beat (beat 1 or 3). The second row awards points to notes within a step of notes in the previous window (delineated by bold lines) that already have points in the first row ("precontiguity"). The third row awards points similarly to the second row but for contiguity with high-ranking notes in 

> 7 There is agreement among music analysts (including Bruhn and Schenker) where subject statements are in this fugue. 

77 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 



**Figure 6** . Contour- and Schema-based intraopus arc diagram for Bach’s "Fugue in C minor" (BWV 847) 



<!-- Start of picture text -->
0<br>0<br><!-- End of picture text -->

**Figure 7** . Contour Equivalence Class in BWV 847 

the next window ("post-contiguity"). Finally, the points are totalled and the highest ranking note in each window is selected, producing the reduction, in this case 6-5-4-3, similar to Gjerdingen’s Prinner schema. 

### **5.1 Convergence of Contour and Schema** 

In BWV 847, the subject’s surface contour and the underlying schema converge with a nearly identical interpretation of the piece, except the contour class has an anacrusis and the schema starts with a strong beat. Figure 6 includes the contour network in blue and the schema network in red. Either the contour-level algorithm [12] or schema-based method [11], when applied to BWV 847, identifies all appearances of the subject as equivalent in all three voices of the fugue, whereas pitch strings, interval strings, or other implementations of contour theory would not identify them fully. Either algorithm enables pattern discovery without any specific information about the genre (e.g., the main theme is at the beginning) to find the most prevalent pattern and visualize it. Depending on whether one wishes to demonstrate interopus connections, intraopus connections, or both, one may prefer the contour or schema-based approach. The contour in Figure 7 is very specific to BWV 847. The reduction in Figure 8 relates the subject to portions of many other pieces, including the primary theme in K545 (Figure 9. 



<!-- Start of picture text -->
Note Ab4 C5 B4 C5 D4 G4 C5 B4 C5 D4 F4 44 Ab4 G4 F4 Eb4<br>Onset 0 0 0 0 1 0 0 0 0 0 0 0 1<br>Pre-Cont. 0 0 0 0 0 0 0 0 1 0 0 0 0 1<br>Post-Cont. 0 0 0 0 0 0 0 ?<br>Total 2<br>6 5 4 3<br>Figure 8 . Schema Equivalence Class in BWV 847<br>Note G5 C6 G5 F5 G5 F5 E5 F5 E5<br>Onset 0 0 0 0 0<br>Pre-Cont. 0 0 0 1 0 0<br>Post-Cont. 0 0 1 0 ?<br>Total 2 2 2 0<br>6 5 4 3<br><!-- End of picture text -->

**Figure 9** . Schema Equivalence Class in K545 (mm. 3-4) 

### **5.2 Divergence of Contour and Schema** 

In contrast, the contours and schemata suggest very different formal understandings of Mozart’s "Sonata in C Major" (K545). The arcs above the piano roll in Figure 10 represent a contour-based network. Thinking in terms of melodic shape highlights the conventional sonata form, emphasized by the return of the primary theme at the beginning of the recapitulation (terminus of the red arc). The development is identified by a distinct motive (in yellow) which forms the core [16]. The schema-based network is quite different, shown as downward consecutive arcs. Initial arcs connect the first appearance of musical material to all other instances. However, consecutive arcs do not place any emphasis on the first instance. Consecutive arcs are appropriate for a schema pattern, which is highly intertextual, but not thematic in the traditional sense. Schemata are more minimalistic or generative because much more material can be accounted for by a single equivalence class. 

### **6. CONCLUSION** 

We are trying to decenter music research from two angles: exploring intertextuality, debunking notions of art as created by individuals [9]; and, applying African-centered approaches to analysis (based on [12]. An interopus diagram (Figure 11) summarizes the connections between the works discussed, with contour matches in blue and schema similarity in red. Yorùbá Oríkì is not western diatonic music, so schema theory is not applicable. However, the schema approximation of scale-degree skeletons may be relevant to postcolonial music of Africa, such as "O. mo.lúàbí." Vice-versa, one may not expect contour levels (based on tone levels) to apply to European classical music because there is an emphasis on idiosyncratic 

78 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 



<!-- Start of picture text -->
iiint<br><!-- End of picture text -->

**Figure 10** . Contour (above) and Schema-based (below) intraopus arc diagram for Mozart’s "Sonata in C Major" (K545) 

themes. However, part of the take-away of schema theory is that European musicians in the 18th century relied on a small number of skeletal formulas, so contour motives are likely interopus as well, which questions the notion of distinct "masterpieces." It is only in the relationship between Rodgers/Hart’s "Blue Moon" and Gillespie’s improvisation on it that we (appropriately for jazz) see a match of both contour and schema.<sup>8</sup> Contour and schema, although copresent, are very independent. Gillespie tests the bounds of the tonal paradigm of the song, making the theme an improvisational gesture that is independent from the harmonic progression, while the rhythm section maintains it with some liberty. Similarly, Mozart used the Prinner schema with his main theme and independently of it. This contrasts with the total interdependence of contour and schemata in Bach’s subject. In improvisation, we expect contrapuntal and harmonic patterns to be stretched by a soloist’s wanderings. However, preservation of both contours and scale-degree skeletal schemata suggests intentionality. Bach delineates the subject entrances from the liminal space of the episodes except for a few motivic fragments of the subject. Simlarly, Dizzy Gillespie explores the motive of the "Blue Moon" theme, but only once echoes the full sequence. 

Beyond pure research, ATAVizM has applications in education and teaching music theory as an application for visualizing musical forms designed to be integrated into the undergraduate theory curriculum. Since 2017, the software has been used to teach Fugue, Sonata, and Post-Tonal music in music major courses and Indian Classical, African 

> 8 Although this was not visualized with an arc, the thematic sequence with the model repeated at an interval of a descending diatonic third is replicated at one point by Gillespie in the solo. Both the instance in the theme and the solo form a similar scale-degree skeleton. 



<!-- Start of picture text -->
Oríkì/Owé<br>“Qmlúàbí”<br>“Blue Moon"<br>UU<br>Gillespie's Solo<br>Bach BWV 847<br>Mozart K545<br><!-- End of picture text -->

**Figure 11** . Interopus arc diagram 

Choral, and popular music in general education courses in several US institutions. For teaching contexts, the feature of the user being able to select which strings are thematic is essential. Students make selections based on their analysis of a piece to produce visualizations for analytical papers. The open-source software presented here includes (1) pattern-matching algorithms based on heuristics from music theory (contour and schema) that may be applied to pitch (and duration in the case of contour), (2) theme identification by user input or selection, and (3) color-coding of arcs and a legend. Combining computationally efficient methods for contour and schema pattern recognition with ample features for user direction has brought us closer to reaching the full potential of Wattenberg’s vision for seeing the _Shape of Song_ . 

79 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

### **7. REFERENCES** 

- [1] M. Wattenberg, “Arc diagrams: Visualizing structure in strings,” in _IEEE Symposium on Information Visualization, 2002. INFOVIS 2002._ IEEE, 2002, pp. 110– 116. 

   - [16] W. E. Caplin, _Classical form: A theory of formal functions for the instrumental music of Haydn, Mozart, and Beethoven_ . New York: Oxford University Press, 1998. 

- [2] ——, “The shape of song,” Available at http://www. bewitched.com/song.html (2021/05/01). 

- [3] H.-H. Wu and J. P. Bello, “Audio-based music visualization for music structure analysis,” in _Proceedings of Sound and Music Computing Conference (SMC)_ , 2010, pp. 1–6. 

- [4] D. F. Silva, C.-C. M. Yeh, G. E. Batista, E. J. Keogh _et al._ , “Simple: Assessing music similarity using subsequences joins.” in _ISMIR_ , 2016, pp. 23–29. 

- [5] R. Morris, “Composition with pitch-classes,” _Yale University_ , 1987. 

- [6] I. Quinn, “Fuzzy extensions to the theory of contour,” _Music Theory Spectrum_ , vol. 19, no. 2, pp. 232–263, 1997. 

- [7] R. Gjerdingen, _Music in the galant style_ . New York: Oxford University Press, 2007. 

- [8] K. Orpen and D. Huron, “Measurement of similarity in music: A quantitative approach for non-parametric representations,” _Computers in Music Research_ , vol. 4, 1992. 

- [9] K. Barber, “Yorùbá ’oríkì’ and deconstructive criticism,” _Research in African literatures_ , vol. 15, no. 4, pp. 497–518, 1984. 

- [10] A. Carter-Ényì, “Contour recursion and autosegmentation,” _Music Theory Online_ , vol. 22, no. 1, 2016. 

- [11] A. Carter-Enyi and G. Rabinovitch, “Onset and contiguity: Melodic feature reduction and pattern discovery,” _Music Theory Online_ , vol. 27, no. 4, 2021. 

- [12] A. Carter-Enyi, “Contour levels: an abstraction of pitch space based on african tone systems,” Ph.D. dissertation, The Ohio State University, 2016. 

- [13] S. Oluranti, “Polyrhythm as an integral feature of african pianism: Analysis of piano works by akin euba, gyorgy ligeti & joshua uzoigwe and àjùlo kìnìún (original composition),” Ph.D. dissertation, University of Pittsburgh, 2012. 

- [14] M. A. Schmuckler, “Melodic contour similarity using folk melodies,” _Music Perception_ , vol. 28, no. 2, pp. 169–194, 2010. 

- [15] J. Gilbert, “Jazz trumpet transcriptions from the trumpet kings of the swing era,” Available at http://pubcs.free.fr/jg/jazz_trumpet_transcriptions_ jacques_gilbert_english.html (2021/05/01). 

80 

