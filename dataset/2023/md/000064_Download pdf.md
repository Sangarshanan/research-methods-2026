---
paper_id: "000064"
year: 2023
title: "Download pdf"
source_url: "https://zenodo.org/record/10265345/files/000064.pdf"
---

# THE GAMES WE PLAY: EXPLORING THE IMPACT OF ISMIR ON MUSICOLOGY 

## Vanessa Nina Borsan Mathieu Giraud 

Univ. Lille, CNRS, Centrale Lille 

UMR 9189 CRIStAL, F-59000 Lille, France 

```
{vanessa,mathieu}@algomus.fr
```

## Richard Groult 

Univ Rouen Normandie, INSA Rouen Normandie, 

Université Le Havre Normandie, Normandie Univ 

LITIS UR 4108, F-76000 Rouen, France 

```
richard.groult@univ-rouen.fr
```

### ABSTRACT 

Throughout history, a consistent temporal and spatial gap has persisted between the inception of novel knowledge and technology and their subsequent adoption for extensive practical utilization. The article explores the dynamic interaction and exchange of methodologies between musicology and computational music research. It focuses on an analysis of ten years’ worth of papers from the International Society for Music Information Retrieval (ISMIR) from 2012 to 2021. Over 1000 citations of ISMIR papers were reviewed, and out of these, 51 later works published in musicological venues drew from the findings of 28 ISMIR papers. Final results reveal that most contributions from ISMIR rarely make their way to musicology or humanities. Nevertheless, the paper highlights four examples of successful knowledge transfers between the fields and discusses best practices for collaborations while addressing potential causes for such disparities. In the epilogue, we address the interlaced origins of the problem as stemming from the language of new media, institutional restrictions, and the inability to engage in multidisciplinary communication. 

### 1. INTRODUCTION 

In 2005, Cook [1] critically addressed the prospects and difficulties of collaborations between Music Information Retrieval (MIR) and musicology, many of which were revisited by Downie in 2009, further examining their implications and potential advancements [2]. With the emergence of empirical research methods and advancements in technology, music research has encompassed multiple academic fields, leading to a transformation in the structures of these disciplines, including Music Information Retrieval (MIR) and contemporary musicology. Given their multidisciplinary nature, the categorization of either is becoming increasingly arbitrary. However, for the purpose of 

> © VN. Borsan, M. Giraud, and R. Groult. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: VN. Borsan, M. Giraud, and R. Groult, “The Games We Play: Exploring The Impact of ISMIR on Musicology”, in Proc. of the 24th Int. Society for Music Information Retrieval Conf., Milan, Italy, 2023. 

the clarity of further arguments in this paper, we classify “traditional” and humanities-centred music research fields (musicology, music theory, ethnomusicology, etc.) under the umbrella term “musicology.” Conversely, we use the term “MIR” to encompass all fields that engage in naturalsciences-based (typically computational) research related to music, such as acoustics, informatics, physics, mathematics, engineering, and more<sup>1</sup> . 

Despite the significant impact of both fields in broadening our understanding of music, unresolved issues highlighted by Cook continue to hinder their collaboration to this day [1]. In recent years, a growing number of musicologists, along with humanities researchers in general, have shown a preference for working with digital materials rather than physical ones [3], but the application of computation to research can be approached at various levels. There are general-purpose software, such as word processors or spreadsheet editors, and music-oriented software, such as Sibelius, Finale, and Audacity; there are programming music/MIR platforms and libraries, such as Humdrum [4], music21 [5], Librosa [6] and Essentia [7] and then there are methods and algorithms as developed by the MIR community, for example [8–11] and others (see [12] for a detailed review). While computer usage is prevalent among many researchers there are fewer musicologists who adopt or contribute to similar methodologies. However, through new media and computational advancements, music and our relationship to it are changing [13]. Given the expansion of what is deemed significant in the “realm of music,” it raises the question of whether familiarity with computational languages is becoming a prerequisite for its exploration. 

Computational methods assist researchers in handling larger and more varied datasets, but, would musicologists agree that “working with [these] datasets [have] open[ed] up new areas of musicology?” [1] Or, has this shift evoked new areas of research, which are (almost) independent from the musicological domain? The goal of this paper is to ask to what extent the MIR contributions (in the frames of ISMIR) resonate throughout the musicological community. The very results of these particular analyses may also 

> 1 Our labels are arbitrary categories for rough orientation, considering disciplines like music cognition that fit into both/neither category. 

545 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

highlight some of the core issues of miscommunication between the two domains. 

We start by outlining the “ready-made” arguments of collaboratory issues of the fields (Section 1), followed by a methodology introduction for a bibliographical study of ten years of ISMIR papers (2010–2021) and their citations, where we present some empirical results (Sections 2 and 3). As an example of “good collaboratory practice”, we detail four examples, where ISMIR findings were later used by/for a musicological audience through datasets, methodologies, and tool and/or code (Section 4). In conclusion, we discuss the results, examine potential reasons for the outcomes, and draw on theories of play and media studies to support our findings (Section 5). 

### 2. THE WEB OF ARGUMENTS 

Numerous authors have explored the advantages and/or drawbacks of interdisciplinary research in the realm of music. We acknowledge the tensions within musicology without delving into the detailed evolution of historic musicology, ethnomusicology, and systematic (empirical) musicology, as these topics have already been extensively covered( [14]). We focus on the development of (pro and con) arguments, generally raised in the 2000s and 2010s. 

### 2.1 Years 2000–2010: Enticement Versus Restraint 

The critical discussions began with the emergence of more empirically-centred approaches, mostly labelled as systematic musicology. Following the iconic question “Who stole systematic musicology?”, Leman [15] observed, that even systematic musicology had no longer belonged to “itself.” Conversely, transdisciplinary musicology gained traction among engineering departments (MIR, sound processing), as and neuroscientists and psychologists, who developed a growing interest in the study of music. 

Amidst the rapid growth of music-related technology production, papers in the early 2000s addressed contemporary musicology, its redefinition, and future methodologies and goals. For some, technologies were viewed as a natural extension for quantitative, big-data, and empirical music analyses [1], while others thought of music research as an interdisciplinary ground of “somewhat equal” subdisciplines, including musicology and MIR. Addressing the benefits of these collaborations, [16,17], many authors highlighted the benefits of multidisciplinary projects in expanding the boundaries of isolated disciplines for more comprehensive outcomes. In contrast, others warned that in “an era in which interdisciplinarity has become a kind of mantra, verbally subscribed to by nearly everyone, disciplines continue to police their own boundaries [18].” A similar opinion was shared by Parncutt [14], and Leman, who stressed that, even though they like talking about interdisciplinary projects, “it was very rare that researchers went beyond the boundaries of their own disciplines [15].” Additionally, knowledge transfers are anything but fluid 

among computational scientists and musicologists, thus the ideas expand poorly, if at all [19], hence, they must be improved [12]. The scepticism towards unconditionally welcoming the emerging collaboratory changes thus remained. In 2009, [2] reflected on interdisciplinary dynamics during the first 10 years of ISMIR, highlighting its shortcomings, such as the inability to communicate the produced tools to the user (performer, musicologists, ...), favouring low-level over high-level features and audio over other symbolic music representations, and so forth. 

### 2.2 Years 2010–Today: The Quest for Consensus 

The scepticism and critiques were not far-fetched nor properly addressed, as Urberg later noticed that the methodological visions of “fundamentally-renewed” music research, had “not [yet] taken over the majority of musicological scholarship [20].” Nonetheless, he imposed that the methodology of research has already shifted, as there is an ascending trend of new research tools and digitized (music) data representations, a lot of them consciously used by musicologists. So what seems to be the problem? 

Finding balance in methodology, data collection and interpretation. Still in the second decade of the 21st century, when the introduced arguments began to overlap, Inskip et. al. [25] conducted a survey in order to answer this question. The study suggests that “[...] efforts should be made into supporting the development of their digital skills and providing usable, useful and reliable software created with a ‘musicology-centred’ design approach.” Otherwise, the “data richness will lead to information overload [26].” As Dahling expressed in 2012, there are many tools for music collection and analysis, of which many “suffer from various shortcomings, such as specificity to a certain repertoire or approach, lack of robustness and flexibility, flawed user interfaces, or output is difficult to interpret [26].” A similar concern has been expressed by others, such as [27] and [28], or, for textual analysis [29]. All of them advocate not only for a more accessible and flexible computational methods, but also express the need understand what these methods do and how. Alongside epistemological confusion and other (methodological) drawbacks, a similar problem was stressed by Aucouturier and Bigand. Their dialogue-style paper revealed the flaws and prospects for collaborations between MIR and music research (specifically music cognition) [30]. In Drucker’s words, “the humanities are not a mere afterthought, simply studying and critiquing the effects of computational methods. [Their theory] can provide ways of thinking differently [31].” In a different light, the latter was also implied by [32]. 

Cyclical collaboration vs discontinuity. Following Downie’s call for improvements [2], some authors discussed refined measurements that need to be considered regarding data collection and interpretation, for “obtaining or accessing high-quality datasets remains a serious hurdle, especially on a large scale [33].” These hurdles limit the (digital) quality of music research, but not only that. All 

546 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

|Claim/link to musicology|ISMIRpapers|Examples of claim|
|---|---|---|
|None, “musicolog” is only present in<br>one of the references|147 (42.7%)||
|Application of musicological con-<br>cepts, by only explaining citation,<br>or apply musicological concepts, or<br>hinting towards the possibility of<br>musicological application.|81 (23.6%)|[21]<br>“In order to select relevant low-level features, we refer tomusicologypapers such as<br>[...] which suggest that arousal is related to features including rhythm density, note<br>density, key, dynamic, tempo, etc.”<br>[22]<br>“We assume that the music tradition is known, and that the rhythm class (t¯al.a) of the<br>piece is from a set of known(frommusicologicalliterature)t¯al.as.”|
|Some claim of musicological utility.|114 (33.7%)|[23]<br>“[...] retaining the rest of the presented framework, e.g. for an analytical ontology<br>of musicological terms supporting the use of digital score annotations to illustrate<br>points in scholarly musicological arguments.” (see Section 4)<br>[24]<br>“These features can serve as inputs to machine learning algorithms, or they can be<br>analyzed statisticallyto derive musicological insights.” (see Section 4)|



Table 1. Links and/or claims regarding musicology in 342 ISMIR papers from 2012 to 2021 where “musicolog” occurs. 

music cannot be collected and/or represented in the same manner, and it is not feasible to investigate and discuss it within identical methodological frameworks [28,34]. They believe that this perspective should be considered not only by musicologists but should also be of equal importance for the field of MIR. Schüler and Huron argued that mutual theoretical awareness is essential for musicologists and MIR researchers [19,35]. Methodological tools should not be confused with philosophical worldviews [35], and due to the importance of theory and “practice”, there must exist a cyclical collaboration between the disciplines [27]. Humanities scholars express concern about detached interpretation and the prioritization of “facts” and algorithmic success in studies [28, 29]. Thus, the algorithms must be transparent enough for the scholars to actively participate in the building blocks of their framework and methods. “[I]n the long run, the most ’useful’ computational analyses will be the ones which are interactive, confronting a human user with the results of computational analysis and allowing that user to modify or intervene in the procedure to arrive at an acceptable or interesting result [28].” 

From a more critical standpoint, Becker asks whether “our failure [is] due to our own shortcomings in not becoming thoroughly versed in the protocols and expectations of another discipline? Or, was the failure due to too stringent protocols and expectations for publication in a [...] journal?”, concluding that some disciplinary barriers may be unbreachable due to rigid institutional formations [18]. Leman, conversely, sees the “failure” of collaboration in the notion of the absence of “concrete planned goal at long term, except some vague idea of what all these research activities are up to [15].” Although no firm solutions have been introduced, some humanities authors [29, 36, 37] offered partial theoretical frameworks. Our methodology, inspired by the latter (e.g., Moretti’s Distant Reading), will be introduced in the following section. 

### 3.1 Article Selection and Filtration: Which papers claim to have some musicological utility? 

We downloaded all 1055 ISMIR papers<sup>2</sup> from the past 10 years (2012–2021)<sup>3</sup> and converted the .pdf files to .txt files. We retrieved 342 articles which included the root “musicolog”, meaning the article contained words like “musicological,” “musicology”, and “ethnomusicologist”<sup>4</sup> . Next, we reviewed these 342 papers to determine their musicological implications, categorizing them into 3 categories (see Table 1 for examples and details). Subsequently, we focused on the 114 ISMIR papers that claimed some musicological relevance and the citations, if any. 

### 3.2 Citations Analysis: Were the papers later used “in musicology”? 

To study how and if these 114 papers may have had an impact on musicology, we identified 907 citations of them through Google Scholar. The median of all citations per cited paper is 16. The most cited paper was cited 208 times, while 10 were never cited. We retrieved almost all of these citations<sup>5</sup> and sorted the citing papers by these two (slightly ambivalent) categories. 

- ➀ Is any “citator” a musicologist? As “musicologists”, we classified researchers with a Master’s or PhD degree in a “musicological” research field or most of their activity was mostly conducted in a musicological environment (see Introduction). Together, there were 210 citations to 67 unique ISMIR papers that corresponded with this category. 

- ➁ Does the citing paper appear in a musicological journal/conference? Here, we focus on venues instead of in- 

2 `https://www.ismir.net/conferences/` 

### 3. METHODOLOGY AND RESULTS 

In this section, we discuss the filtering process of ISMIR 2012–21 to examine whether and how such papers were used in musicological studies. We also provide statistics and information on data availability. 

> 3 Due to time constraints, we couldn’t thoroughly analyze all ISMIR papers. Instead, we focused on the impact of early 2000s ideas on the MIR and musicology collaboration, exploring new tools, and acknowledging changes due to improved technology and online publication accessibility. 

> 4 We acknowledge potential exclusions of articles using terms like “music research,” “music theory,” or “music history”, and that ISMIR papers may hold musicological significance without explicitly stating so. 

> 5 About 20 were excluded due to inaccessibility of the article or lack of information, among which 6 belong to centred dataset. 

547 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

|Journal/Conference|Citations<br>(Cited ISMIRpapers)|
|---|---|
|Digital Libraries for Musicology (DLfM)<sup>⋆</sup>|31<br>(15)|
|Journal of New Music Research (JNMR)<sup>⋆</sup>|17<br>(15)|
|Acta Musicologica|7<br>(7)|
|Frontiers in Digital Humanities<sup>⋆</sup>|6<br>(5)|
|Empirical Musicology Review (EMR)|6<br>(5)|
|Folk Music Analysis(FMA)|6<br>(5)|
|4: Musicae Scientiae; Zeitschrift der Gesell|schaft für Musikthe-|
|orie; Digital Scholarship in the Humanities|<sup>⋆</sup>; McGill University|
|(Schulich School of Music, Music Technol|ogy<sup>⋆</sup>); Utrecht Uni-|
|versity (MA or PhD Thesis)<sup>⋆</sup>; 3: Music Th|eory Online (MTO);|
|Computational Music Analysis; UC San|Diego<sup>⋆</sup>; 2: Compu-|
|tational Phonogram Archiving: Current Re<br>|search in Systematic<br>|
|Musicology<sup>⋆</sup>; The Musical Quarterly; Journ|al on Computing and|
|Cultural Heritage<sup>⋆</sup>; Digital Humanities Quar<br>pear once)|terly<sup>⋆</sup>; +33 more (ap-<br>70 citations in total|



Table 2. Somewhat musicology-centred journals/conferences/books/institutions, in which ISMIR papers were cited 143 times. The venues marked with (<sup>⋆</sup> ) have both, musicology/MIR goals. 

dividuals, because researchers with musicological backgrounds can have a strong root in MIR as well, while musicological journals mainly target and publish works of primarily musicologically-motivated research activity. We defined “musicological venues” by their primary motivation and targeted audience (Table 2), some of them also have (secondary) MIR motivations (<sup>⋆</sup> in Table 2). ISMIR was fully excluded, with the intention to show to which extent these contributions manage to “leave” the ISMIR community. Together, there were 143 citations in rather musicologically relevant publications to 55 ISMIR papers. 

From here, we focus on the 143 citations, as the rest either focused on the MIR audience only (was published in technical, science, MIR conference) or did not imply the musicological utility. 

### 3.3 Filtered Citations Analysis: What is the type of citation/utility? 

We sorted the 143 citations (or 114 unique citing articles) of previously mentioned 55 ISMIR papers, focusing on if and how the first use the latter. 

- ✘ Only referencing the ISMIR paper. 92 citations only reference 43 ISMIR papers. The authors referenced the article, because it was relevant to the topic, however, their contribution was not actually used. 

The other 51 citations cited and somewhat used 28 ISMIR contributions<sup>6</sup> , split into the following types: 

- ✓ Dataset (10 citations to 5 ISMIR papers): The author(s) of citation (partially) used the dataset, presented in cited ISMIR paper. 

> 6 Certain ISMIR papers were referenced and utilized in various contexts, and/or classified under multiple utility categories. 



<!-- Start of picture text -->
15 10 5 5 10 15 20 25<br>2012<br>2013<br>2014<br>2015<br>(a) (b) (c) 2016 (f) (e) (d)<br>2017<br>2018<br>2019<br>2020<br>2021<br>ISMIR papers ISMIR year citing papers<br><!-- End of picture text -->

Figure 1. Distribution of the papers reported in this study among the years. Left. (a) 114 ISMIR papers with “musicolog” root and claiming to have some musicological utility; (b) from which 43 ISMIR papers cited in musicological venues; (c) from which 28 ISMIR papers actually used at least once. Right. (d) 143 citations in 51 citing papers (of the 43 ISMIR papers) from musicological venues; (e) from which 87 citations (74 unique citing papers) with at least one musicologist as an author; (f) from which 35 (or 31 unique citing papers) with actual usage (of the 28 ISMIR papers). Even for citations, the considered year is the year of the original ISMIR paper. 

- ✓ Methodology (22 citations to 17 ISMIR papers): The author(s) of citation (partially) used the methodology, presented in cited ISMIR paper. 

- ✓ Code/Tool (19 citations to 13 ISMIR papers): The author(s) of citation (partially) used the code and/or tool, presented in cited ISMIR paper. 

### 3.4 Statistics on these Papers and Citations 

About 10% of ISMIR articles mention “musicolog” every year. As expected, most recent papers are not cited (Figure 1). Despite the limited 10-year time span, papers that received at least one citation showed an average gap of three years between publication and the first citation. If we consider the 81 “older papers” published between 2012 and 2018, about the third of them have been actually used at least once in another study. 

The list of musicological venues is also revealing (Table 2): The conference that most frequently included ISMIR’s contribution was DLfM, a community that started as a satellite event of ISMIR and that “provides a forum for musicians, musicologists, librarians, and technologists to share findings and expertise<sup>7</sup> .” It is followed by JNMR, which “publishes systematic, scientific and technological research on music, musical processes and musical behaviours, including popular, cultural and canon music”<sup>8</sup> . The majority of the 143 citations (see Figure 1) appear in journals/conferences with a clearly stated inclination to MIR and/or digital humanities ((<sup>⋆</sup> ) in Table 2) and include several MIR scientists. 

> 7 `https://dlfm.web.ox.ac.uk` 8 `https://www.tandfonline.com/journals/nnmr20` 

548 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

Among 51 citations that used ISMIR papers, 16 papers were (partial) self-citations, meaning there was at least one common author. However, in 12 cases, new team members were involved (often from outside the initial institution), and in 4 cases, a new musicologist was present. 

### 3.5 Data Availability 

The annotated data on the 114 papers, which claim to have some musicological utility, and the one of 143 citing papers of the 28 papers are available on a git repository through open licences (Open Database License, Database Contents License) at `algomus.fr/data` . 

### 4. FOUR EXAMPLES OF KNOWLEDGE AND IDEA TRANSFERS 

51 citations in musicological venues were thus used one of the 28 ISMIR papers through its dataset, methodology, code and/or tool. We focused on four of these stories: In the qualitative observation, we picked examples that describe the type of utility of ISMIR contribution. 

Despite some self-citations, promising collaborations were observed within research teams integrating interdisciplinary dynamics between musicology and MIR. These teams included both computer/MIR scientists and “conventionally” trained musicologists. 

Tool: VIS Framework. In an ISMIR 2014 paper, researchers from the Distributed Digital Music Archives & Libraries Lab at McGill University introduced the VIS Framework, a Python library for music analysis together with a case study on counterpoint patterns in symbolic music scores [38]. The library was further used and cited by the same group in “musicological” venues, such as a study on encoding and translation issues published in DLfM [39]. Two PhD theses from the Schulich School of Music (McGill University) also used the framework. First proposed a computer-assisted approach to the study of interval-succession treaties [40], while second studied the tonality practice of seventeenth-century Italian composers in trio-sonatas [41] and used VIS to extract features. The VIS GUI was found to be essential in making the analysis task easier for non-computational scientists. 

Dataset: The Story of Jingju. The Music Technology Group (UPF, Barcelona, Spain) includes the ethnomusicologist, Repetto. His ISMIR 2017 paper with Serra introduced JMSC, of collection of scores or Jingju (also called “Beijing Opera”) [42]. Two citing DLfM 2017 papers<sup>9</sup> analyzed the melodic syllabic contours in JMSC [43, 44], each paper including another member of the MTG joining the two authors of the ISMIR paper. 

Multidisciplinary environments have been created by MIR and music teams globally, fostering collaboration 

> 9 DLfM was a satellite event of ISMIR at that time, meaning the papers and their citations appeared (and were likely prepared) simultaneously. 

with external groups, attracting more scientists, and expanding opportunities for obtaining PhD positions from both sides. The following story exemplifies how a multidisciplinary group can attract new collaborations. 

Methodology/Tool: The Lohengrin TimeMachine. An ISMIR 2017 paper by Weigl and Page, from the University of Oxford, presented an update on the MELD framework [23], used to encode information of and about music (e.g., digital representations of notation, audio, contextual information) inside MEI. MELD has been cited by 25 other papers. One of the “MELD applications”, the Lohengrin TimeMachine was presented at DLfM in 2021 [45] by Lewis and Page, as well as Dreyfus, an American musicologist who was previously not involved with the MIR community. In his late career, he was appointed at the University of Oxford – but in the music department. The application explored a few extracts of Wagner’s Lohengrin through scores, motives, orchestration, structure, texts, audio/video, musicological analysis, etc. It offers interesting representations to a wider audience of both musical knowledges but also on the very methodology of the musicological research. This citation is also a good example of the time it may take to cross domains (here, 4 years). 

Tool: Mindfulness and Music Performance Study . In ISMIR 2017, researchers from IRCAM presented the PiPo plugin, designed for data stream processing in various domains including interactive audio processing and MIR. This API-based tool facilitates the extraction of low-level descriptors from audio and motion data streams [46]. A 2021 citing paper in Psychology of Music, from a completely independent group, in Israel, examined whether short-term mindfulness meditation activity would improve music performance (vocal skills) regarding pitch intonation, dynamics transmission, and vocal resonation [47]. They use the PiPo tool in the processing phase, using PiPo modules for the automatic segmentation of markers by onset (time-tagged frames) for low-level descriptor extraction (pitch, dynamics, timbre ...). Focusing on music psychology, this application doesn’t qualify as a musicological study. However, it showcases how MIR methods can be applied to humanities-based music research. Interestingly, out of the 114 ISMIR papers examined, this is the only one reused in a “musicological” context independently of the original authors. 

### 5. DISCUSSION AND CONCLUSION 

While ISMIR is not exclusively focused on musicology, certain researchers who publish at ISMIR assert their impact on the field. Our examination of the last five years as well as a ten-year period of ISMIR reveals that the majority of these contributions seldom make their way into musicological or humanities scholarship. Out of the 28 ISMIR papers, which have been cited and used, the majority of them are partly self-cited, and/or are “re-used” within the same group, lab etc. Somehow, we did not find a single example 

549 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

of independent musicological application of ISMIR 20122021 contributions in a traditional musicological journal. 

We are aware that our study has some biases. To broadly observe how MIR and other music research interact, we should explore the utility dynamics both ways (ISMIR to musicology, and musicology to ISMIR), as well as analyze roots other than “musicolog” in multiple venues (both MIR and music) and thoroughly explore the organizers, institutions, and authors. There are also time<sup>10</sup> and space<sup>11</sup> variables, which could have had an impact on the results. Research and collaboration cannot always be measured solely by points or numbers. Non-citable research and pedagogical activities at universities are valuable components that may not be easily quantifiable. In some cases, tools or datasets may be used for inspiration without being cited in the final report. Similarly, ISMIR-presented tools may be employed without direct citation, with references made to non-ISMIR contributions or other sources. 

Various technologies have undoubtedly made their way to musicologists, inspiring the creation of a quasi-common ground with IT and other domains. However, further efforts are necessary to establish a consistent circulation of knowledge. While some are managing this challenge (see Section 4), most still struggle. 

This struggle could be understood through theories of the game (or play) by Huizinga [48] then Caillois [49]. They discuss how the games we play are not only those of “leisure” (sports, video games, ...) but also “law and order, commerce and profit, craft and art, [...] and science. All are rooted in the primaeval soil of play [48].” Caillois considers day-to-day games people play in the light of competitive examinations and economic competition [49], and his six rules very much resemble the scientific atmosphere. Like play, it is 1. not obligatory to participate in science, which 2. must be conducted (or “played”) in an environment, pre-defined in time and space. 3. The strategy (research development) is left to the individual ideas 4. and is generally locked in an infinite loop of “unproductivity” (meaning, it is largely being developed and executed and re-executed within itself). Both (games and science) follow conventional rules and take place in 6. “make-believe” world, which is accompanied by a special awareness of a second reality. For example, this may as well be the daily shift from one’s research to mundane events. Games (or science) can only be played when all parties are in agreement with the particular rules. 

Several of these may be incompatible between the MIR and musicology, one of them being, as mentioned in [50], the language of new media (similar idea in [13]). As later elaborated by [51] and [52], this language has, “in the process of epochal technological change” never been immediate, but instead adopted “through a process of transition [52].” Since the majority of new technologies (or 

> 10 The contributions we examine may be applied in the future. 

> 11 Some venues cannot be observed through Google Scholar, and some contributions may not have cited the source when applying their tools or databases in their research. 

languages) for music analysis “skipped” the transitional era, and are, for an average musicologist, incomprehensible or non-intuitive (algorithmic codes), the computational products “do not manage to address them [musicologists] in an intelligible way.” There seems to be a “clear disconnect between how MIR tasks are designed to evaluate systems, and how end users are supposed to use those systems [...] [making them] difficult and costly to implement [12]”. Consequently, the results, produced by such processes also become unusable, as the “involvement in the wheel of algorithms is indispensable for musicological research [13, 52].” It is this kind of disruption alone, that can disable the multidisciplinary game. 

Reflecting on our discussion in Section 2, Huron, imposed the obligation for both parties (MIR and musicology) to familiarize themselves with each other’s methodologies [35]. Additionally, [30] highlights the importance of knowing which parts of whose methodology are to be used for a fruitful collaboration. Leman suggests solving the gap by inducing multi-modality, introducing contextbased approaches into empiricism [15]; and a more reserved Parncutt, explains that the wall is set by the feeling of superiority on both sides [14], and so on. Still, the rules of the playground must first reach consensus (starting with the transition towards a common “language”). And this is where these “common grounds” come to light. ISMIR in itself is a multidisciplinary environment, however, most of the participants (deriving from natural rather than humanities or social sciences), already play by similar rules (or speak the same language). Consequently, the multidisciplinary activity within MIR remains rather limited and, despite numerous surveys [12] has yet been unable to properly address all of the (reasons for) constraints mentioned by [2] about 14 years ago. As seen in 3.4, the most cited papers in musicological venues are derived from DLfM and JNMR. This is not a coincidence, as these are “institutions”, whose “rules” derive from a compromise between both disciplines, as well as the majority of yearly contributions, manage to speak the language of both. It hence makes sense, that one of the mentioned papers addressing these matters [30] is structured as a dialogue, as it is exactly that, finding a practical working consent among (the two) sciences, that can endorse a fertile collaboration. Merely adapting to each other’s rules seems like trying to simultaneously play football and handball, where similar “material” surely cannot and will not bring a consensus between the two games. The successful examples (Section 4) and mentioned discussions, should be considered to help us advance our fundamental goals on institutional grounds and go beyond both MIR and musicology. In the process of transductive ergomimesis, “new digital media drastically reposition the people” [13] and repeatedly evoke new (motor) skills and techniques, professions, and multidisciplinary actions (see also [53]). The change is hence indispensable for the two fields, “but we’ve got to put in place the [institutional] conditions to make it actually happen” [1]. It seems that it is, in the end, this game (digital) musicologists may want actually want to play. 

550 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

Acknowledgements. We thank Ken Déguernel, Louis Couturier, the Algomus team, and the anonymous reviewers for their thought-provoking remarks. 

### 6. REFERENCES 

- [1] N. Cook, “Towards the compleat musicologist,” in International Conference on Music Information Retrieval (ISMIR 2005), 2005. 

- [2] J. S. Downie, D. Byrd, and T. Crawford, “Ten years of ismir: Reflections on challenges and opportunities.” in ISMIR, 2009, pp. 13–18. 

- [3] T. C. Duguid, M. Feustle, F. Giannetti, and E. Grumbach, “Music scholarship online (MuSO): a research environment for a more democratic digital musicology,” Digital Humanities Quarterly, vol. 13, no. 1, 2019. 

- [4] D. Huron, “Music information processing using the Humdrum toolkit: Concepts, examples, and lessons,” Computer Music Journal, vol. 26, no. 2, pp. 11–26, 2002. 

   - [12] M. Schedl, E. Gómez, J. Urbano et al., “Music information retrieval: Recent developments and applications,” Foundations and Trends® in Information Retrieval, vol. 8, no. 2-3, pp. 127–261, 2014. 

   - [13] T. Magnusson, Sonic writing: technologies of material, symbolic, and signal inscriptions. Bloomsbury Publishing USA, 2019. 

   - [14] R. Parncutt, “Systematic musicology and the history and future of Western musical scholarship,” Journal of interdisciplinary music studies, vol. 1, no. 1, pp. 1–32, 2007. 

   - [15] M. Leman, “Systematic musicology at the crossroads of modern music research.” in Systematic and comparative musicology: Concepts, methods, findings, P. Lang, Ed., 2008, pp. 89–115. 

   - [16] K. Neubarth, M. Bergeron, and D. Conklin, “Associations between musicology and music information retrieval.” in International Society for Music Information Retrieval Conference (ISMIR 2011), 2011, pp. 429– 434. 

- [5] M. S. Cuthbert and C. Ariza, “music21: A toolkit for computer-aided musicology and symbolic music data,” International Society for Music Information Retrieval Conference (ISMIR 2010), pp. 637–642, 2010. 

- [6] B. McFee, C. Raffel, D. Liang, D. P. Ellis, M. McVicar, E. Battenberg, and O. Nieto, “librosa: Audio and music signal analysis in Python,” in Python in Science Conference (SCIPY 2015), vol. 8, 2015, pp. 18–25. 

- [7] D. Bogdanov, N. Wack, E. Gómez Gutiérrez, S. Gulati, H. Boyer, O. Mayor, G. Roma Trepat, J. Salamon, J. R. Zapata González, X. Serra et al., “Essentia: An audio analysis library for music information retrieval,” in International Society for Music Information Retrieval Conference (ISMIR 2013), 2013, pp. 493–498,. 

- [8] O. Lartillot, “Automated motivic analysis: An exhaustive approach based on closed and cyclic pattern mining in multidimensional parametric spaces,” in Computational Music Analysis. Springer, 2016, pp. 273–302. 

- [9] M. Mongeau and D. Sankoff, “Comparison of musical sequences,” Computers and the Humanities, vol. 24, no. 3, pp. 161–175, 1990. 

- [10] E. Cambouropoulos, “The local boundary detection model (LBDM) and its application in the study of expressive timing,” in International Computer Music Conference (ICMC 2001), 2001, pp. 7–22. 

- [11] C. Finkensiep, K. Déguernel, M. Neuwirth, and M. Rohrmeier, “Voice-leading schema recognition using rhythm and pitch features,” in International Society for Music Information Retrieval Conference (ISMIR 2020), 2020, pp. 520–526. 

- [17] A. Volk, F. Wiering, and P. Kranenburg, “Unfolding the potential of computational musicology,” in International Conference on Informatics and Semiotics in Organisations (ICISO 2011), 2011, pp. 137–144. 

- [18] J. Becker, “Crossing boundaries: An introductory essay,” Empirical Musicology Review, vol. 4, no. 2, pp. 45–48, 2009. 

- [19] N. Schüler, “Reflections on the history of computerassisted music analysis 1: Predecessors and the beginnings,” Musicological Annual, vol. 41, no. 1, pp. 31– 43, 2005. 

- [20] M. Urberg, “Pasts and futures of digital humanities in musicology: Moving towards a “bigger tent”,” Music Reference Services Quarterly, vol. 20, no. 3-4, pp. 134–150, 2017. 

- [21] H. H. Tan and D. Herremans, “Music fadernets: Controllable music generation based on high-level features via low-level feature modelling,” in International Society for Music Information Retrieval Conference (ISMIR 2020), 2020. 

- [22] A. Srinivasamurthy, A. Holzapfel, and X. Serra, “Informed automatic meter analysis of music recordings,” in International Society for Music Information Retrieval Conference (ISMIR 2017), 2017, pp. 679–685. 

- [23] D. Weigl and K. Page, “A framework for distributed semantic annotation of musical score:" take it to the bridge!",” in International Society for Music Information Retrieval Conference (ISMIR 2017), 2017, pp. 221–228. 

551 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

- [24] C. McKay, J. Cumming, and I. Fujinaga, “jSymbolic 2.2: Extracting features from symbolic music for use in musicological and MIR research.” in International Society for Music Information Retrieval Conference (ISMIR 2018), 2018, pp. 348–354. 

- [25] C. Inskip and F. Wiering, “In their own words: Using text analysis to identify musicologists’ attitudes towards technology,” in International Society for Music Information Retrieval Conference (ISMIR 2015), 2015, pp. 455–461. 

- [26] E. Dahlig-Turek, S. Klotz, R. Parncutt, and F. Wiering, Musicology (Re-) Mapped: Discussion Paper. European Science Foundation, 2012. 

- [27] P. Van Kranenburg, J. Garbers, A. Volk, F. Wiering, L. P. Grijp, and R. C. Veltkamp, “Collaboration perspectives for folk song research and music information retrieval: The indispensable role of computational musicology,” Journal of Interdisciplinary Music Studies, vol. 4, no. 1, pp. 17–43, 2010. 

- [28] A. Marsden, “Music analysis by computer: Ontology and epistemology,” in Computational Music Analysis, 2016, pp. 3–28. 

- [29] J. E. Dobson, Critical digital humanities: the search for a methodology. University of Illinois Press, 2019. 

- [30] J.-J. Aucouturier and E. Bigand, “Mel Cepstrum & Ann Ova: The difficult dialog between MIR and music cognition.” in International Society for Music Information Retrieval Conference (ISMIR 2012), 2012, pp. 397–402. 

- [31] J. Drucker, “Humanistic theory and digital scholarship,” Debates in the digital humanities, vol. 150, pp. 85–95, 2012. 

- [32] F. Morreale, “Where does the buck stop? ethical and political issues with AI in music creation,” Transactions of the International Society for Music Information Retrieval, vol. 4, no. 1, pp. 105–113, 2021. 

- [33] L. Pugin, “The challenge of data in digital musicology,” Frontiers in Digital Humanities, vol. 2, p. 4, 2015. 

   - [38] C. Antila and J. Cumming, “The VIS framework: Analyzing counterpoint in large datasets.” in International Society for Music Information Retrieval Conference (ISMIR 2014), 2014, pp. 71–76. 

   - [39] N. Nápoles, G. Vigliensoni, and I. Fujinaga, “Encoding matters,” in Digital Libraries for Musicology (DLfM 2018), 2018, pp. 69–73. 

   - [40] A. Morgan, “Renaissance interval-succession theory: Treatises and analysis,” Ph.D. dissertation, Schulich School of Music, McGill University, 2017. 

   - [41] S. Howes, “Tonality and transposition in the seventeenth-century trio sonata,” Ph.D. dissertation, Schulich School of Music , McGill University, 2021. 

   - [42] R. C. Repetto and X. Serra, “A collection of music scores for corpus based jingju singing research.” in International Society for Music Information Retrieval Conference (ISMIR 2017), 2017, pp. 46–52. 

   - [43] R. Gong, R. C. Repetto, and X. Serra, “Creating an a cappella singing audio dataset for automatic Jingju singing evaluation research,” in Digital Libraries for Musicology (DLfM 2017), 2017, pp. 37–40. 

   - [44] R. C. Repetto, S. Zhang, and X. Serra, “Quantitative analysis of the relationship between linguistic tones and melody in Jingju using music scores,” in Digital Libraries for Musicology (DLfM 2017), 2017, pp. 41– 44. 

   - [45] D. Lewis, K. Page, and L. Dreyfus, “Narratives and exploration in a musicology app: Supporting scholarly argument with the Lohengrin TimeMachine,” in Digital Libraries for Musicology (DLfM 2021), 2021, pp. 50–58. 

   - [46] N. Schnell, D. Schwarz, J. Larralde, and R. Borghesi, “Pipo, a plugin interface for afferent data stream processing modules,” in International Society for Music Information Retrieval Conference (ISMIR 2017), 2017. 

   - [47] E. Ornoy and S. Cohen, “The effect of mindfulness meditation on the vocal proficiencies of music education students,” Psychology of Music, vol. 50, no. 5, 2021. 

   - [48] J. Huizinga, Homo ludens. Routledge, 1949. 

- [34] S. Münnich, “FAIR for whom? Commentary on Hofmann et al. (2021),” Empirical Musicology Review, vol. 16, no. 1, pp. 151–153, 2021. 

- [35] D. Huron, “The new empiricism: Systematic musicology in a postmodern age,” The 1999 Ernest Bloch Lectures, pp. 1–32, 1999. 

- [36] S. Ahlbäck, “Melody beyond notes: A study of melody cognition,” Ph.D. dissertation, Göteborgs Universitet, 2004. 

- [37] F. Moretti, Distant reading. Verso Books, 2013. 

- [49] R. Caillois, Man, Play, and Games. University of Illinois Press, 2001. 

- [50] L. Manovich, The language of new media. MIT press: Cambridge, USA, 2002. 

- [51] P. Krašovec, Tujost kapitala. Sophia, 2021. 

- [52] V. N. Borsan and L. Stefanija, “Introduction,” Musicological Annual, vol. 58/2, pp. 10–14, 2022. 

- [53] F. A. Kittler, Gramophone, film, typewriter. Stanford University Press, 1999. 

552 

