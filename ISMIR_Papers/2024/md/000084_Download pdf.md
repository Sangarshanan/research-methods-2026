---
paper_id: "000084"
year: 2024
title: "Download pdf"
source_url: "https://zenodo.org/record/14877445/files/000084.pdf"
---

# **A CRITICAL SURVEY OF RESEARCH IN MUSIC GENRE RECOGNITION** 

**Owen Green**<sup>1</sup> **Bob L. T. Sturm**<sup>2</sup> **Georgina Born**<sup>3</sup> **Melanie Wald-Fuhrmann**<sup>1</sup> 

1 Department of Music, Max Planck Institute for Empirical Aesthetics, Frankfurt, Germany 

2 Division of Speech, Music and Hearing, KTH, Stockholm, Sweden 

3 Department of Anthropology, Institute for Advanced Studies, UCL, London, UK 

owen.green@ae.mpg.de, bobs@kth.se 

## **ABSTRACT** 

This paper surveys 560 publications about music genre recognition (MGR) published between 2013–2022, complementing the comprehensive survey of [474], which covered the time frame 1995–2012 (467 publications). For each publication we determine its main functions: a review of research, a contribution to evaluation methodology, or an experimental work. For each experimental work we note the data, experimental approach, and figure of merit it applies. We also note the extents to which any publication engages with work critical of MGR as a research problem, as well as genre theory. Our bibliographic analysis shows for MGR research: 1) it typically does not meaningfully engage with any critique of itself; and 2) it typically does not meaningfully engage with work in genre theory. 

## **1. INTRODUCTION** 

Despite much more work [1–560] music genre recognition (MGR) still remains a compelling problem to solve by a machine. This work comes on top of the 467 publications surveyed over a decade ago by Sturm [474]. Of principal concern in that survey is the question: “How does one measure the capacity of a system to recognize and discriminate between abstract characteristics of the human phenomenon of music?” The survey catalogues each of the 467 publications along several dimensions. 1 Sturm determined whether each publication is mainly a review of MGR research, a contribution to evaluation methodology, or a description of experimental work in which an MGR system is built and tested. For each experimental work (438 of 467 publications) Sturm recorded its experimental designs (of which there are 10), datasets (16), and figures of merit (9). 

Now that at least 560 more publications have entered the domain, where does the problem of MGR stand? This paper aims to complement and extend the survey of [474] by 

> 1 The data of that survey can be found here: https: //github.com/boblsturm/Music-Genre-RecognitionSurvey--1995-2012 

> © O. Green, B. Sturm, G. Born, M. Wald-Fuhrmann. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). **Attribution:** O. Green, B. Sturm, G. Born, M. WaldFuhrmann, “A Critical Survey of Research in Music Genre Recognition”, in _Proc. of the 25th Int. Society for Music Information Retrieval Conf.,_ San Francisco, United States, 2024. 

exhaustively surveying research published between 2013– 2022 related to MGR—as well as any earlier publications discovered to have been missed in Sturm’s original work— such that the two surveys give a comprehensive account up to 2022. It also aims to answer several critical questions. Is the experimental design _Classify_ and figure of merit accuracy still the most frequent, despite their noted serious flaws threatening the validity of conclusions drawn from them [470, 471, 561, 562]. Is GTZAN [563] still the most used public dataset, despite its noted faults [400, 467, 471, 564]? How have these faults been considered or even _re_ considered in the past decade? How has all this new research in MGR engaged with work that is critical of MGR as a research problem, i.e., [231, 232, 329, 401, 467, 469– 471, 473, 475–478, 561, 562, 564–574]? How has all this work engaged with genre theory such as [575–598]? 

The next section describes the methodology we use to collect and catalogue publications. Section 3 presents our analyses of this collection along several dimensions. Section 4 gives broad observations and recommendations to guide future work in MGR. The resulting catalogue, bibliography and analysis code are available online.<sup>2</sup> 

## **2. METHODOLOGY** 

We assembled a corpus of 560 publications in the following way. We performed a broad search across _Google Scholar_ for publications appearing from 2013 onwards using search terms like ‘music genre’, ‘recognition OR classification “music genre”’. This gave over 67 pages of results that we manually browsed. We supplemented these results with searches of the ISMIR proceedings, TISMIR and arXiv. We added each relevant publication we found to a dedicated Zotero collection,<sup>3</sup> which is a convenient means to gather, share and organize bibliographic data. 

For each publication in our collection, we read it and manually enter data into a spreadsheet. As done by Sturm [474], we catalogue each publication according to its type, then note the experimental designs, datasets and figures of merit it uses. Additionally, we note whether each publication cites or engages with two kinds of published work: genre-related work from the social sciences and humanities; and work that is critical of MGR. We note what moti- 

> 2 https://www.kth.se/profile/bobs/page/ research-data 

> 3 https://zotero.org 

> <sup>745</sup> 1 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 



<!-- Start of picture text -->
80 79 75<br>70 69 68<br>60 54 59 55 55 55<br>52<br>50 47<br>44 44 42 43<br>40 38 35 39<br>30 28<br>20 19<br>11<br>10 5 4 7<br>1 0 1 2<br>0<br>1995199619971998199920002001200220032004200520062007200820092010201120122013201420152016201720182019202020212022<br>Number of Publications<br><!-- End of picture text -->

**Figure 1** . Annual numbers of publications related to music genre recognition between 1995 and 2022. Dashed vertical line demarcates the end date of publications surveyed in Sturm [474]. The present survey adds ten references before 2013 [115, 149, 155, 181, 194, 202, 209, 354, 423, 426], but 550 other publications surveyed herein are published after 2012. The white plot line shows the number of publications appearing at ISMIR or in the Transactions of ISMIR. 

vations the paper describes for researching MGR. 

To conduct our analyses of the collection, we query entries in our spreadsheet and Zotero library, but also use python and relevant libraries. We export our collection as a BibTex-formatted file, and the spreadsheet as a text file of comma-separated values. In the following subsections we describe in more detail each dimension of our catalogue. (Further details are given in the Supp. Mat.) 

**Publication Type** We assign each publication to at least one of three categories. A _review_ publication is concerned with surveying the domain of MGR, e.g., [474, 599]. An _evaluation_ publication is concerned with evaluation methodology in MGR, such as proposing a dataset, e.g., [113, 600], experimental design, e.g., [571, 601], or taking a critical look at work in the domain, e.g., [471, 566]. Finally, an _experimental_ publication is concerned with engineering and testing MGR systems, e.g., [563, 602]. **Dataset** For experimental publications, we note what data sets are used, whether private data was used, and the modality of data used: musical audio (waveform or extracted features), symbolic data, or other types (e.g., lyrics, WWW, playlists). We also note if a publication works with non-Western musics. 

**Experimental Design** Following the categorisations described by Sturm [474, p. 32], we note the design(s) used in the experiments described by a publication. These ten designs are: _Classify_ , _Features_ , _Generalize_ , _Robust_ , _Scale_ , _Cluster_ , _Retrieve_ , _Rules_ , _Compose_ , _Eyeball_ . (Supp. Mat. S1.5 describes and gives examples of each of these.) 

**Figure of Merit (FoM)** We note the figure(s) of merit used in the evaluation of experiments [474]. The main FoM we look for include _Accuracy_ , _Recall_ , _Precision_ , _Fmeasure_ , _Receiver Operating Characteristic (ROC)_ and the _Confusion Table_ . Where a confusion table has been used we note whether or not there is an accompanying interpretative discussion, and whether specific instances of confusion are discussed. (Supp. Mat. S1.6 defines these.) 

**Referencing** In a direction different from Sturm [474], we record if a publication cites at least one of a collection of 26 publications we deem are _critical_ of MGR, i.e., 

[231, 232, 329, 401, 467, 469–471, 473, 475–478, 561, 562, 564–574]. We also determine whether the citation is accompanied by any discussion or concrete effects on the experimental design in the publication. We also record if a publication refers to work on musical genre from the social sciences and humanities, i.e., [575–591, 593–598], and record if that citation is accompanied by substantive discussion. Supp. Mat. S1.7 discusses both sets of references. 

**Motivation for MGR** Where authors explicitly state a motivating rationale for MGR work, we record which of four non-exclusive categories they appeal to: _industrial need_ , _public good_ , coping with _information overload_ , or are appealing to _precedent_ . There is a degree of unavoidable subjectivity in this designation, and so we opt for parsimony and look only for explicit statements of this kind to avoid unwarranted inference. Supp. Mat. S1.8 provides examples of each of these. 

## **3. ANALYSIS AND RESULTS** 

We now analyze the 560 publications in this survey in relation to the 467 in Sturm [474]. Figure 1 shows the annual number of publications related to MGR since the earliest reference cited in Sturm [474]—Matityaho and Furst [603]. This shows that MGR publications grew to a high point in 2010 after being established in the MIR community a decade earlier as a “flagship problem” of music information retrieval [604]. Thereafter the mean number of publications related to MGR each year is 56.7 (std dev. 13.1). We see that the annual number of publications related to MGR appearing at ISMIR or in its Transactions since 2010 is less than ten in all but two years (2011, 2016). Our survey does not include 28 publications [605–632] because we cannot get access (e.g., behind a paywall), or the language of the paper is not English. 

## **3.1 Publication Types** 

Of the 560 publications we survey in this paper, we find only nine review articles or book chapters discussing MGR 

746 2 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

[98, 193, 247, 323, 325, 339, 467, 474, 493]. Among these, Corrêa and Rodrigues [98] reviews MGR using symbolic data. Kostek [247] is a review of MIR and has a section about MGR; and Tzanetakis [493] is a book chapter reviewing music informatics generally, where music genre appears in one section. Sturm [467] reviews all publications using the GTZAN dataset up to 2012; and Sturm [474] is the survey we extend in this paper. 

We find 19 of our 560 publications that primarily discuss evaluation in MGR research [113, 199, 231, 232, 329, 341, 367, 400, 401, 424, 467, 469–471, 473, 474, 476– 478]. In addition to those already described in Sec. 2, Palmason et al. [341] investigates the agreement of music genre ground truth between different stakeholders. Porter et al. [367] discusses enriching the AcousticBrainz audio feature dataset [633] using metadata collected from a variety of online sources, include genre information. Schreiber [424] extends the Million Song Dataset; and Defferrard et al. [113] introduces the FMA dataset. Finally, Hossain and Al Marouf [199] discusses the creation of a dataset of song lyrics exemplifying different genres of Bengali music. 

Of the 560 publications we survey in this paper, we find 545 that make experimental contributions. Of these, the next three subsections discuss the datasets, experimental designs, and figures of merit used in this subset of publications, comparing and contrasting with the previous survey [474]. We then go further than Sturm [474]. Subsection 3.7 looks at how all 560 publications we survey engage with work critical of MGR. Subsection 3.8 investigates the extent to which they engage with music genre theory. The penultimate subsection 3.5 looks at how MGR is being motivated as a research problem. Subsection 3.6 looks at the kinds of venues at which MGR research is being published. 

## **3.2 Datasets** 

Sturm [474] finds the GTZAN dataset [563] from 2002 is the most used public dataset, appearing in 100 out of 435 publications with an experimental component. We find that GTZAN remains the most frequently used dataset, appearing in 254 of 545 publications that have an experimental component. Some publications use GTZAN for learning bases, which are then used for building MGR systems tested in other datasets, e.g., Jao et al. [213] and Markov and Matsui [295]. Some publications we survey use only a portion of GTZAN. For instance, Agarwal et al. [5] uses only five of ten classes; and Rajesh and Bhalke [390] uses only two. Others add classes to GTZAN, e.g., Iloga et al. [205, 206] adds Cameroonian music, Conceicao et al. [95] adds music from Brazil, Wibowo and Wihayati [519] adds Malaysian Dangdut music, and Shashirekha [440] adds songs sung in an Indian language (Kannada). Moving briefly to the entire collection we survey, we find considerations of music from non-Western traditions to appear in only 61 of the 560 publications; Sturm [474] finds 47 in its survey of 467 publications. 

Some publications analyze GTZAN as a dataset. Flexer [150] analyzes hubs in GTZAN, and tests methods of outlier detection using it. Lu et al. [286, 287] attempt to auto- 

matically find the faults in the dataset identified in Sturm [467]. Rodriguez-Algarra et al. [400] investigates why a particular MGR system performs so well on GTZAN, and finds infrasonic information confounded with labels— more formally explored in Rodriguez-Algarra et al. [401]. Kang and Lin [224] looks at inferring taxonomies of classes in datasets, including GTZAN. Lu et al. [286, 287] use GTZAN as a testbed for anomaly detection. 

The next four most popular datasets we find are ISMIR2004 [634] from 2004 (appearing in 50 publications), FMA [635] from 2016 (36), the Million Song Dataset [600] from 2011 (32), and the Latin Music Dataset [636] from 2008 (23). We find that data that is not publicly available (e.g., in-house data, or undisclosed data) appears in 176 of 545 publications. Of those, we find 146 of them exclusively use non-publicly available data. 

The predominant data modality in our catalogue is acoustic (or features extracted from acoustic data), which appears in 482 of 545 publications with an experimental component. Sturm [474] finds 344 of 435 publications use such a modality. We find symbolic modalities are used in 40 publications, while Sturm [474] finds them used in 81 publications. We find 11 publications use both modalities [2, 23, 187, 189, 209, 270, 359, 360, 362, 507, 556]. Other modalities (e.g., lyrics, WWW, playlists) appear used in 66 of our publications, while Sturm [474] finds these used in 27 publications. 

## **3.3 Experimental design** 

The three most used experimental designs we find in the 545 publications we survey with an experimental component match those found by Sturm [474]. The most used design in both is _Classify_ : we find 514 publications use this, and of those 264 exclusively use this design; Sturm [474] finds this appears in 397 of 435 publications with an experimental component. The second most used design is _Feature_ , which appears in 145 of 545 publications we survey; Sturm [474] finds this appears in 142 of 435 publications. The third most used design is _Generalize_ , which appears in 127 of 545 publications we survey; Sturm [474] finds it appears in 69 of 435 publications. 

The two least-used designs we find are the same as in Sturm [474]: _Rules_ and _Compose_ . Among our 545 papers with an experimental component, we find _Rules_ appears in six publications [63, 70, 97, 209, 246, 402]. For instance, Campobello et al. [63] derive an analytic formulae for GTZAN genres whereby specific feature values extracted from an audio signal are used to compute the relevance of a class. We find the _Compose_ design appears in five [175, 209, 476, 485, 489]. For instance, Sturm [476] inspects the correspondence between randomly generated rhythmic patterns classified with high confidence by a state-of-theart system trained in the BALLROOM dataset [637], and the classes in that dataset. 

## **3.4 Figure of merit** 

We find accuracy is the figure of merit that appears the most: 449 out of 545 publications with an experimental 

747 3 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

component. Sturm [474] finds this appears in 385 of 435 publications. The confusion table is the next most common figure of merit, appearing in 193 publications surveyed here. In those publications with a confusion table, we find no discussion about it in 78 publications—that is, it is merely presented as a table without interpretation. When a confusion table is discussed, musical motivations for confusions are often given. For example, Chathuranga et al. [73] writes, “[In our confusion table] Rock music is mostly misclassified as country and blue. This is due to the facts that rock music and country music have similar roots and rock music came from a combination of country music and rhythm and blues.” Chen and Ramadge [77] writes, “Rock music is easily confused with other genres—perhaps because of its broad nature.” 

Specific instances of confusions are only discussed in nine papers [63, 201, 231, 232, 341, 467, 470, 472, 475]. For instance, Sturm [467] and Campobello et al. [63] show tables of confusions made by classifier for specific excerpts in GTZAN, e.g., Sturm [467] shows GTZAN country excerpt 69 “My Heroes Have Always Been Cowboys” by Willie Nelson is mislabeled “Classical”, and Campobello et al. [63] shows GTZAN filename “country.00069” is mislabeled “Blues”, “Classical” and “Rock”. Sturm et al. [472] do the same but for the Latin Music Dataset. Hsu et al. [201] look at four specific music recordings from a test set they create and inspect how classifications of them differ between systems they test. Finally, Kereliuk et al. [231, 232] and Sturm [470, 475] make use of a set of ten different songs and show how each can be confidently classified in any GTZAN class. 

## **3.5 Justifications of MGR** 

How is MGR as a research problem being justified? We noted two major shades of justification where one was offered. 155 papers were found that explicitly invoke imagined applications for the music industry (106) or end users (49). In 150 of these papers, applications of MGR were presented as useful or necessary in due contemporary information overload. Conversely, 103 papers were noted to make no direct utilitarian appeal for MGR work, but instead to call upon precedent: MGR problems are important because there has been work on MGR. 

In the 150 papers that invoke information overload as a problem that MGR can help solve, a common presumption is that there are problematic quantities of unlabelled musical data that would be more tedious or error-prone to organize by hand than with MGR, e.g [174, 439]. Sometimes, the urgency of dealing with such a problem is emphasised. For example: “a lot of music data has become available recently …in order for users to benefit from them, an efficient music information retrieval technology is necessary.” [294]; “Given the vast number of current collections, automated genre classification is critical for music organization …” [376] 

Publications seldom motivate through learning something about _music_ rather than classifier performance. [301] sets out to understand the temporalities of musical change 

over a 50 year period. [329] argues that MGR classifiers can be repurposed towards greater understanding of genre as musico-social. [189, 505] argue that more interpretable models more useful for musicologists and listeners. [348] investigates the potential of MGR for studying underrepresented traditions. [140] examines the ’tenuous’ relationship between rhythmic similarity and genre. 

## **3.6 Venues for MGR publications** 

Of the 560 publications we review, 350 are conference papers and 156 appear in journals. The most common venue for MGR publications is the ISMIR conference (43 papers). The next most common conferences are _Int. Conf. Acoustics Speech and Signal Processing_ (ICASSP) (12), _Int. Joint Conf. Neural Networks_ (IJCNN) (9), and Interspeech (5). Six publications appear at the music computing conferences ICMC, SMC and DaFx. The most common journals were _IEEE Access_ (7), _Int. Research Journal of Engineering and Technology_ (6), then _IEEE Signal Processing Letters_ , _Int. Journal of Computer Applications_ , _Journal of Intelligent Information Systems_ , _IEEE Trans. on Multimedia_ , _Journal of New Music Research_ , _Trans. of the Int. Society for Music Information Retrieval_ , _Expert Systems with Applications_ , and _Applied Soft Computing_ (4 publications each). 

After stripping edition indicators from conference names, we estimate that papers appeared at 235 unique conferences, of which 195 hosted a single paper in our corpus. Similarly, the 156 journal articles we reviewed appeared across 101 journals, 74 of which hosted a single article from our corpus. 82 publications appear in conferences or journals under the umbrellas of the ACM and IEEE, including ICASSP and WASPAA. In addition to 9 more PhD theses containing work related to MGR [2, 23, 160, 183, 336, 501, 518, 545] we reviewed 14 master’s theses [11, 35, 64, 112, 220, 262, 289, 308, 333, 374, 453, 465]. 

Elsevier publishes the greatest proportion of the journals encountered (11), followed by Springer (9), IEEE (8), MDPI (5), Hindawi (4), IET (3) and ACM (3). 20 publications were on ArXiv or similar pre-print hosting providers with no corresponding official publication. Many publications appear in venues not specifically concerned with music, audio or informatics, but with computing topics more generally or—more general still—with topics like ‘engineering’ or ‘technology’. Some publications appear in venues apparently unrelated to music informatics. For example, [176] appears in the _International Journal of Early Childhood Special Education_ . Others appear in venues whose existence we could not confirm, e.g. [193] was apparently presented at a 2018 ACM Symposium on Neural Gaze Detection of which we can find no online trace. 

## **3.7 Engagement with work critical of MGR** 

We now turn to another aspect not explored in Sturm [474]: How does research in MGR engage with work that is critical of MGR? How many of the 560 publications we survey cite 26 critical publications [231, 232, 329, 401, 467, 469– 

748 4 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

471, 473, 475–478, 561, 562, 564–574]? Do any implement proposed recommendations or alternatives? We find that only 163 of the 560 publications cite at least one of these critical references; and of these, only 77 engage in some way with the critique. Such engagement can be simply applying artist filtering. It can also be motivating the use of a specific experimental design. 

Let us look specifically at criticism around GTZAN [563], the most-used dataset in MGR research. Ten years after its creation, this dataset was carefully analyzed by Sturm [467, 471, 564], resulting in a catalogue of its faults and an index of its contents. Kereliuk et al. [231, 232] created and used the first partitioning of GTZAN that considers its contents.<sup>4</sup> (See Supp. Mat. S2 for an overview of the on-line availability of these materials.) 

Considering the faults of GTZAN have been known since 2012, let us focus on the 250 papers published after 2012 that use GTZAN with a _Classify_ experimental design reporting accuracy as a figure of merit. Of these, we find only 62 acknowledge the existence of faults in GTZAN, and 46 of those essentially ignore or dismiss them. For instance, Sigtia and Dixon [447], Nanni et al. [320], Jeong and Lee [218], Senac et al. [428] and Palmason et al. [340] are five papers that dismiss consideration of the faults by appealing to the popularity of GTZAN as a benchmark dataset: “Although the GTZAN dataset has some shortcomings [564], it has been used as a benchmark for genre classification tasks” [447]. Others claim that their experimental results are not harmed by such problems, e.g., “Despite [its faults], we still used [GTZAN] because these small problems can not seriously damage our results” [205]. We find 15 publications use the fault-filtered partitions of Kereliuk et al. [231, 232]: [66, 81, 144, 145, 218, 236, 267, 271, 302, 305, 329, 349, 364, 540, 554]. Foleiss and Tavares [152] create their own partitioning following Sturm [467], which was then used by Ng et al. [327] and Cai and Zhang [62]. Three other publications [15, 63, 374] acknowledge the faults in GTZAN and perform their own fault-filtering and partitioning. 

The fact that 188 of these 250 publications using GTZAN do not mention its faults could be partly explained by the fact that websites linking to the dataset make no mention of them. At least up to March 20 2022, the original source of GTZAN<sup>5</sup> makes no mention of any faults or of the cataloguing work of Sturm [467, 471, 564]. There currently exist several online copies of GTZAN (or features computed from the dataset), but none of these mention faults; and at this time we find only two online repositories of GTZAN that mention faults (See Supp. Mat. S2). 

Another criticized aspect of MGR research is its use of _Classify_ as an experimental design. Sturm [470, 471, 473, 478, 561, 562] argue that this design is essentially a “horse show”: systems are tasked with tapping their hooves the correct number of times, but no reliable measurement of musical intelligence can be made without controlling for numerous independent variables. While the survey in 

> 4 Both the catalogue of GTZAN and the fault-filtered partition are available here: https://github.com/boblsturm/GTZAN. 

> 5 http://marsyas.info/downloads/datasets.html. 

Sturm [474] finds _Classify_ appears in 91.3% of its surveyed publications, the present survey finds it appears in 94.3%. Furthermore, we find 264 publications _only_ use _Classify_ . While we see at least some work in MGR has cited and engaged with the faults in GTZAN, very few publications in the present survey (outside of those by Sturm and collaborators) meaningfully engage with the criticism of _Classify_ . To the best of our knowledge, there are no publications that dispute the argument of Sturm [470, 471, 473, 478, 561, 562]; and we find only 17 publications citing those six publications and engaging with them in any meaningful way when it comes to experimental design [47, 48, 63, 67, 98, 140, 175, 244, 286, 327, 329, 374, 375, 393, 421, 507, 518], e.g., cautiously interpreting results of classification, or motivating additional experimental designs. 

## **3.8 Engagement with genre theory** 

We now turn to the question: how have the 560 publications in our survey engaged with genre theory from the social sciences and humanities? We find 36 references to such work citing 23 sources [575–598]. Of these 36 publications, 10 go further than just citation [139, 146, 219, 329, 341, 375, 421, 453, 469, 471]. Useful indicators of the ways in which musical genre is a more complex concept than just distributions of acoustic or other features are scattered across these contributions. The following key points emerge from engagements with genre theory in our corpus: 

- **Relational** The interrelationships between genres are crucial to understanding them, yet more complex than can be captured through simple taxonomies [329, 341, 375, 469, 471]. 

- **More-than-sonic** The character of genres is determined not only through sonic traits but that other modalities can be of crucial importance, often as proxies for the social roots of genres [146, 329, 375, 421]. 

- **Social** The relationships between genres and social formations / identities is complex and bidirectional: genres can articulate identities, but genres can also be used as part of demarcating social groupings. The agency in defining and consolidating genre terms is distributed across different social planes, including the institutions of industry, as well as musicians, critics and fans [219, 329, 341, 421]. 

- **Perspectival** Genres and their relationships can be understood quite differently by different groups of people [375, 469, 471]. 

- **Dynamic** No aspect of musical genre stands still. Their salient sonic and other features, interrelationships, connections to social formations are all in constant, unpredictable motion. Crucially this means that the association of particular musical texts and tastes with genres is also subject to change [329, 471]. 

749 5 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

## **4. DISCUSSION** 

Based on a survey of 560 MGR publications from 2013– 2022, we find some continuity with the previous survey by Sturm [474]. GTZAN, _Classify_ and _Accuracy_ remain respectively the most widely used dataset, experiment and figure of merit. Despite an increase in the number of public datasets available to MGR researchers, we also see that the proportion of publications dealing with non-Western musical formations has not changed appreciably. Although the use of alternative modalities of data (e.g., lyrics, WWW, playlists) has roughly doubled, such work remains a minority and treating MGR as an audio-similarity problem still prevails. However, our survey goes further to find that MGR work has by and large not engaged with any critique of its accepted methodologies, critique of the research task itself, or of work in the social sciences and humanities related to genre. 

We note that the engagement that there is has introduced to MGR key facets of the challenges of studying musical genre, which warrant greater consideration—we commend the introductory chapter of [577] as a comprehensive overview. Crucially, each of the factors outlined in Sec. 3.8 not only provide key pointers towards threats to validity for MGR [638] but also indicate that for MIR to contend with genre as a _musical_ topic, a greater diversity of approaches is called for [639]. However, given the quantity of the surveyed publications that appear outside ISMIR or core MIR venues, it is not certain whether MGR remains a “flagship problem” of music information retrieval [604]. 

Has it, rather, become autonomous of MIR, as a convenient downstream task for computer scientists that has the appearances of addressing a domain-specific useful problem? Our reading of the given motivations for MGR research found in this corpus supports the plausibility of this interpretation, given the frequency of appeals to vaguely described industrial and user applications. One way to investigate this further would be through a bibliometric analysis of this corpus, geared towards identifying possible clusters of work through co-citation or collaboration. 6 . A possibility is that MIR specialists have shifted their attention to auto-tagging and away from MGR, which as a ‘superset’ problem of MGR, we do not cover here. However, an interesting area for follow-up research could be to perform a similar survey of auto-tagging research along with a bibliometric comparison, which may shed some light on the movement of research within MIR. 

Nevertheless, we put forward the normative position that _music_ informatics researchers should be oriented to _musical_ questions open to investigating their complexities in collaboration with music scholars. Doing so likely involves shifts in how this research is pursued. Currently, what dominates is exploratory analysis where progress is assessed through benchmarks. [641] provides a framework for assessing the suitability of such ‘outcome reasoning‘ along dimensions of measurement, adaptability, re- 

> 6 Open scholarly databases such as OpenAlex [640] could automate at least some of this, although we note that its coverage of references for the papers in this corpus doesn’t extend to around half of its ISMIR papers. 

silience and compatibility with stakeholder beliefs. These are telling questions, as it’s not clear that for much MGR research who the stakeholders are. If one group of potential stakeholders is other music researchers, rather than the imagined needs of music platforms or their users, then this points to more _explanatory_ work in MGR. However, benchmark-driven predictive modelling need not be abandoned. In [642] the authors point to ways in which benchmark-driven work can be incorporated and redirected towards richer ends and [643] shows how predictive models can be integrated into contemporary approaches to causal inference, suited to theory-driven, explanatory registers of research. 

## **5. CONCLUSION** 

We close with some recommendations. Broadly, MGR suffers from threats to validity [638] that warrant more attention. Some progress could be made through a greater role for theory in MGR, both through authors being more explicit about the theoretical perspective on genre at work in a given study, as well as deeper engagement with theories of musical genre. 

In particular, a close and critical reading of the introductory discussion of [577] in terms of its implications for MIR genre research could be generative for the field. Specifically, it is the sociality, temporality and heterogeneity of genres that are least addressed in the work we have surveyed, and these bring interesting challenges. One fruitful direction to engaging with the social can be found in [644]: by acknowledging that culture is present in every part of the MIR ‘value-chain‘ [645], the authors propose a technical intervention on recommender system design in pursuit of a normative social outcome (‘commonality’) often considered to be outside the scope of engineering concerns. Some of the surveyed work already moves towards dealing with genre as temporal [301], and social-temporal [329]. This suggests a possible intersection with work in music and cultural evolution [646], which could serve as a constructive ‘interface’ between MIR and music studies. 

Finally, to contend with the heterogeneity of genres means dealing not only with their sonic variability, but also variability across the many other dimensions that may define a particular genre for a particular aesthetic coalition. On the first point, we would recommend more genrespecific computational-musicological work like [647–649] to cast light on the relationships between computed features and aesthetic saliences for groups of listeners. More finegrained, genre-specific datasets as in [276] might help here. On the second point, engaging with ‘live’ genres in motion implies the need for work in nonexperimental settings [650] that can cope with diverse, noisy and incomplete data. 

## **6. ACKNOWLEDGMENTS** 

This work was supported by the European Research Council under the European Union’s Horizon 2020 research and innovation programme (Grant agreements No. 864189 and No. 101019164). 

750 6 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

## **7. REFERENCES** 

- [1] M. Abbasi Layegh, S. Haghipour, and Y. Najafi Sarem, “Classification of the Radif of Mirza Abdollah a Canonic Repertoire of Persian Music Using SVM Method,” _Gazi University Journal of Science Part A Engineering and Innovation_ , vol. 1, no. 4, pp. 57–66, 4 2013. 

- [2] J. Abeßer, “Automatic Transcription of Bass Guitar Tracks applied for Music Genre Classification and Sound Synthesis,” Ph.D. dissertation, Technischen Universität Ilmenau, Oct. 23, 2014. 

- [3] Adiyansjah, A. A. S. Gunawan, and D. Suhartono, “Music recommender system based on genre using convolutional recurrent neural networks,” in _The 4th International Conference on Computer Science and Computational Intelligence (ICCSCI 2019) : Enabling Collaboration to Escalate Impact of Research Results for Society_ , vol. 157, Jan. 1, 2019, pp. 99–109. 

- [4] D. Afchar, R. Hennequin, and V. Guigue, “Learning Unsupervised Hierarchies of Audio Concepts,” in _Proceedings of the 23rd International Society for Music Information Retrieval Conference_ , Bengaluru, India: ISMIR, Dec. 4, 2022, pp. 427–436. 

- [5] P. Agarwal, H. Karnick, and B. Raj, “A comparative study of indian and western music forms,” in _Proceedings of the 14th International Society for Music Information Retrieval Conference_ , 2013. 

- [6] N. Agera, S. Chapaneri, and D. Jayaswal, “Exploring textural features for automatic music genre classification,” in _2015 International Conference on Computing Communication Control and Automation_ , Feb. 2015, pp. 822–826. 

- [7] M. Agrawal and A. Nandy. “A novel multimodal music genre classifier using hierarchical attention and convolutional neural network.” arXiv: 2011. 11970 [cs, eess]. (Nov. 24, 2020), [Online]. Available: http://arxiv.org/abs/2011. 11970 (visited on 03/07/2023), preprint. 

- [8] R. L. Aguiar, Y. M. Costa, and C. N. Silla, “Exploring data augmentation to improve music genre classification with ConvNets,” in _2018 International Joint Conference on Neural Networks (IJCNN)_ , Jul. 2018, pp. 1–8. 

- [9] A. N. Ahmad, C. Sekhar, and A. Yashkar, “Music Genre Classification Using Music Information Retrieval and Self Organizing Maps,” in _Proceedings of the Third International Conference on Soft Computing for Problem Solving_ , M. Pant, K. Deep, A. Nagar, and J. C. Bansal, Eds., New Delhi: Springer India, 2014, pp. 625–634. 

- [10] F. Ahmed, P. P. Paul, and M. Gavrilova, “Music genre classification using a gradient-based local texture descriptor,” in _Intelligent Decision Technologies 2016_ , I. Czarnowski, A. M. Caballero, R. J. Howlett, and L. C. Jain, Eds., Cham: Springer International Publishing, 2016, pp. 455–464. 

- [11] R. Ajoodha, “Automatic music genre classification,” M.S. thesis, University of the Witwatersrand, Johannesburg, 2014. 

- [12] R. Ajoodha, R. Klein, and B. Rosman, “Singlelabelled music genre classification using contentbased features,” in _2015 Pattern Recognition Association of South Africa and Robotics and Mechatronics International Conference (PRASARobMech)_ , Nov. 2015, pp. 66–71. 

- [13] H. Akalp, E. Furkan Cigdem, S. Yilmaz, N. Bolucu, and B. Can, “Language representation models for music genre classification using lyrics,” in _2021 International Symposium on Electrical, Electronics and Information Engineering_ , ser. ISEEIE 2021, New York, NY, USA: Association for Computing Machinery, Jul. 20, 2021, pp. 408–414. 

- [14] A.-K. Al-Tamimi, M. Salem, and A. Al-Alami, “On the use of feature selection for music genre classification,” in _2020 Seventh International Conference on Information Technology Trends (ITT)_ , Nov. 2020, pp. 1–6. 

- [15] A. Alexandridis, E. Chondrodima, G. Paivana, M. Stogiannos, E. Zois, and H. Sarimveis, “Music genre classification using radial basis function networks and particle swarm optimization,” in _2014 6th Computer Science and Electronic Engineering Conference (CEEC)_ , Sep. 2014, pp. 35–40. 

- [16] M. A. Ali and Z. A. Siddiqui, “Automatic music genres classification using machine learning,” _International Journal of Advanced Computer Science and Applications_ , vol. 8, no. 8, 2017. 

- [17] S. Allamy and A. L. Koerich, “1D CNN architectures for music genre classification,” in _2021 IEEE Symposium Series on Computational Intelligence (SSCI)_ , Dec. 2021, pp. 01–07. 

- [18] M. A. Al Mamun, I. Kadir, A. S. A. Rabby, and A. Al Azmi, “Bangla music genre classification using neural network,” in _2019 8th International Conference System Modeling and Advancement in Research Trends (SMART)_ , Nov. 2019, pp. 397–403. 

- [19] F. C. F. Almeida, G. Bernardes, and C. Weiss, “Mid-level Harmonic Audio Features for Musical Style Classification,” in _Proceedings of the 23rd International Society for Music Information Retrieval Conference_ , Bengaluru, India: ISMIR, Dec. 4, 2022, pp. 210–217. 

751 7 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

- [20] P. Alonso-Jiménez, D. Bogdanov, J. Pons, and X. Serra, “Tensorflow Audio Models in Essentia,” in _ICASSP 2020 - 2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)_ , May 2020, pp. 266–270. 

- [21] J. Andén and S. Mallat, “Deep Scattering Spectrum,” _IEEE Transactions on Signal Processing_ , vol. 62, no. 16, pp. 4114–4128, Aug. 2014. 

- [22] N. Andreas, P. Maria, R. Ioannou, N. Petkov, and C. N. Schizas, “A machine learning approach for clustering western and non-western folk music using low-level and mid-level,” in _Proceedings 6th International Workshop on Machine Learning and Music_ , 2013, pp. 55–58. 

- [23] A. Anglade, “Logic-based Modelling of Musical Harmony for Automatic Characterisation and Classification,” Ph.D. dissertation, Queen Mary University of London, Apr. 30, 2014. 

- [24] P. G. Antunes, D. M. de Matos, R. Ribeiro, and I. Trancoso. “Automatic fado music classification.” arXiv: 1406.4447 [cs]. (Jun. 17, 2014), [Online]. Available: http://arxiv.org/abs/ 1406.4447 (visited on 03/02/2023), preprint. 

- [25] J. Arenas-Garcia, K. B. Petersen, G. Camps-Valls, and L. K. Hansen, “Kernel Multivariate Analysis Framework for Supervised Subspace Learning: A Tutorial on Linear and Kernel Multivariate Methods,” _IEEE Signal Processing Magazine_ , vol. 30, no. 4, pp. 16–29, Jul. 2013. 

- [26] T. Arjannikov and J. Zhang, “An association-based approach to genre classification in music,” in _Proceedings of the 15th International Society for Music Information Retrieval Conference_ , Taipei, Taiwan, Oct. 27, 2014. 

- [27] T. Arjannikov and J. Z. Zhang, “An empirical study on structured dichotomies in music genre classification,” in _2015 IEEE 14th International Conference on Machine Learning and Applications (ICMLA)_ , Dec. 2015, pp. 493–496. 

- [28] T. Arjannikov and J. Z. Zhang, “Do nested dichotomies help in automatic music genre classification? An empirical study,” in _Proceedings of the International Computer Music Conference (ICMC)_ , 2016. 

- [29] M. G. Armentano, W. A. De Noni, and H. F. Cardoso, “Genre classification of symbolic pieces of music,” _Journal of Intelligent Information Systems_ , vol. 48, no. 3, pp. 579–599, Jun. 1, 2017. 

- [30] K. Aryafar and A. Shokoufandeh, “Multimodal sparsity-eager support vector machines for music classification,” in _2014 13th International Conference on Machine Learning and Applications_ , Dec. 2014, pp. 405–408. 

- [31] M. Astefanoaei and N. Collignon, “Hyperbolic embeddings for music taxonomy,” in _Proceedings of the 1st Workshop on NLP for Music and Audio (NLP4MusA)_ , 2020, pp. 38–42. 

- [32] Y. Atahan, A. Elbir, A. Enes Keskin, O. Kiraz, B. Kirval, and N. Aydin, “Music genre classification using acoustic features and autoencoders,” in _2021 Innovations in Intelligent Systems and Applications Conference (ASYU)_ , Oct. 2021, pp. 1–5. 

- [33] K. M. Athulya and S. Sindhu, “Deep learning based music genre classification using spectrogram,” in _Proceedings of the International Conference on IoT Based Control Networks & Intelligent Systems - ICICNIS 2021_ , Rochester, NY, Jul. 10, 2021. 

- [34] H. Bahuleyan. “Music genre classification using machine learning techniques.” arXiv: 1804. 01149 [cs, eess]. (Apr. 3, 2018), [Online]. Available: http://arxiv.org/abs/1804. 01149 (visited on 03/03/2023), preprint. 

- [35] V. Bajpai, “Evaluation of state of the art for genre classification in large datasets,” M.S. thesis, Sep. 15, 2018. 

- [36] M. Banitalebi-Dehkordi and A. BanitalebiDehkordi, “Music Genre Classification Using Spectral Analysis and Sparse Representation of the Signals,” _Journal of Signal Processing Systems_ , vol. 74, no. 2, pp. 273–280, Feb. 1, 2014. 

- [37] B. K. Baniya, D. Ghimire, and J. Lee, “Evaluation of different audio features for musical genre classification,” in _SiPS 2013 Proceedings_ , Oct. 2013, pp. 260–265. 

- [38] B. K. Baniya, D. Ghimire, and J. Lee, “Music Genre Classification Based on Timbral Texture and Rhythmic Content Features,” in _Proceedings of the 39th Korean Information Processing Society Spring Conference_ , Korea, 2013. 

- [39] B. K. Baniya, J. Lee, and Z.-N. Li, “Audio feature reduction and analysis for automatic music genre classification,” in _2014 IEEE International Conference on Systems, Man, and Cybernetics (SMC)_ , Oct. 2014, pp. 457–462. 

- [40] B. K. Baniya, D. Ghimire, and J. Lee, “A novel approach of automatic music genre classification based on timbrai texture and rhythmic content features,” in _16th International Conference on Advanced Communication Technology (ICACT)_ , Feb. 2014, pp. 96–102. 

- [41] B. K. Baniya, D. Ghimire, and J. Lee, “Automatic music genre classification using timbral texture and rhythmic content features,” in _2015 17th International Conference on Advanced Communication Technology (ICACT)_ , Jul. 2015, pp. 434–443. 

- [42] B. K. Baniya and J. Lee, “Importance of audio feature reduction in automatic music genre classification,” _Multimedia Tools and Applications_ , vol. 75, no. 6, pp. 3013–3026, Mar. 1, 2016. 

752 8 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

- [43] N. Bassiou, C. Kotropoulos, and A. PapazoglouChalikias, “Greek folk music classification into two genres using lyrics and audio via canonical correlation analysis,” in _2015 9th International Symposium on Image and Signal Processing and Analysis (ISPA)_ , Sep. 2015, pp. 238–243. 

- [44] J. F. Bernabeu Briones, C. Pérez-Sancho, P. J. Ponce de León Amador, J. M. Iñesta, and J. CalvoZaragoza, “A multimodal genre recognition prototype,” presented at the III Workshop de Reconocimiento de Formas y Análisis de Imágenes, WSRFAI, Madrid, Spain, Sep. 2013, pp. 13–16. 

- [45] J. K. Bhatia, R. D. Singh, and S. Kumar, “Music genre classification,” in _2021 5th International Conference on Information Systems and Computer Networks (ISCON)_ , Oct. 2021, pp. 1–4. 

- [46] A. Bhowmik and A. E. Chowdhury, “Genre of bangla music: A machine classification learning approach,” _AIUB Journal of Science and Engineering (AJSE)_ , vol. 18, no. 2, pp. 66–72, 2 Aug. 31, 2019. 

- [47] D. Bisharad and R. H. Laskar, “Music genre recognition using residual neural networks,” in _TENCON 2019 - 2019 IEEE Region 10 Conference (TENCON)_ , Oct. 2019, pp. 2063–2068. 

- [48] D. Bisharad and R. H. Laskar, “Music genre recognition using convolutional recurrent neural network architecture,” _Expert Systems_ , vol. 36, no. 4, e12429, 2019. 

- [49] Z. Bodo and E. Szilágyi, “Connecting the last.fm dataset to LyricWiki and MusicBrainz. Lyricsbased experiments in genre classification,” _Acta Universitatis Sapientiae Informatica_ , vol. 10, pp. 158–182, Dec. 20, 2018. 

- [50] D. Bogdanov, A. Porter, P. Herrera Boyer, and X. Serra, “Cross-collection evaluation for music classification tasks,” in _Proceedings of the 17th International Society for Music Information Retrieval Conference;_ , ISMIR, 2016, pp. 379–385. 

- [51] D. Bogdanov, M. Won, P. Tovstogan, A. Porter, and X. Serra, “The MTG-jamendo dataset for automatic music tagging,” in _Proceedings International Conference on Machine Learning_ , ICML, 2019. 

- [52] D. Bogdanov, A. Porter, H. Schreiber, J. Urbano, and S. Oramas, “The AcousticBrainz Genre Dataset: Multi-Source, Multi-Level, Multi-Label, and Large-Scale,” in _Proceedings of the 20th International Society for Music Information Retrieval Conference_ , Delft, The Netherlands: ISMIR, Nov. 4, 2019, pp. 360–367. 

- [53] P. Boonmatham, S. Pongpinigpinyo, and T. Soonklang, “Musical-scale characteristics for traditional Thai music genre classification,” in _2013 International Computer Science and Engineering Conference (ICSEC)_ , Sep. 2013, pp. 227–232. 

- [54] V. Bruni, M. L. Cardinali, and D. Vitulano, “An MDL-Based Wavelet Scattering Features Selection for Signal Classification,” _Axioms_ , vol. 11, no. 8, p. 376, 8 Aug. 2022. 

- [55] G. Brunner, Y. Wang, R. Wattenhofer, and S. Zhao, “Symbolic music genre transfer with CycleGAN,” in _2018 IEEE 30th International Conference on Tools with Artificial Intelligence (ICTAI)_ , Nov. 2018, pp. 786–793. 

- [56] Z. Bu, H. Zhang, and X. Zhu. “GAFX: A General Audio Feature eXtractor.” arXiv: 2207.09145 [cs, eess]. (Jul. 19, 2022), [Online]. Available: http : / / arxiv . org / abs / 2207 . 09145 (visited on 03/24/2023), preprint. 

- [57] A. Buchmüller and C. Gerloff, “Music genre classification using artificial neural networks,” in _Learning Deep: Perspectives on Deep Learning Algorithms and Artificial Intelligence_ , B. Säfken, A. Silbersdorff, and C. Weisser, Eds., Universitätsverlag Göttingen, 2020, pp. 127–144. 

- [58] A. Budhrani, A. Patel, and S. Ribadiya, “Music2vec: Music genre classification and recommendation system,” in _2020 4th International Conference on Electronics, Communication and Aerospace Technology (ICECA)_ , Nov. 2020, pp. 1406–1411. 

- [59] R. d. D. Bulos, G. F. Go, G. O. Ling, T. C. Uy, and L. J. Yap, “Predictive Analysis Using Data Mining Techniques and SQL,” in _Proceedings of the DLSU Research Congres_ , De La Salle University, Manila, Philippines, 2014. 

- [60] H. Cai, T. Pu, Y. Luo, and X. Zhou, “Music genre prediction based on machine learning,” in _2021 IEEE International Conference on Artificial Intelligence and Industrial Design (AIID)_ , May 2021, pp. 198–201. 

- [61] X. C. Cai and H. Z. Zhang. “Fisher discriminative embedding low-rank sparse representation for music genre classification.” (2022), [Online]. Available: https://assets.researchsquare. com/files/rs-1719236/v1_covered. pdf?c=1654629348, preprint. 

- [62] X. Cai and H. Zhang, “Music genre classification based on auditory image, spectral and acoustic features,” _Multimedia Systems_ , vol. 28, no. 3, pp. 779– 791, Jun. 1, 2022. 

- [63] G. Campobello, D. Dell’Aquila, M. Russo, and A. Segreto, “Neuro-genetic programming for multigenre classification of music content,” _Applied Soft Computing_ , vol. 94, p. 106 488, Sep. 1, 2020. 

- [64] F. Capó Clar, “Impact of audio degradation on music classification,” M.S. thesis, Accepted: 2014-0925T10:05:10Z Publisher: Universitat Politècnica de Catalunya, Barcelona, Jul. 10, 2014. 

753 9 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

- [65] R. V. Casaña-Eslava, I. H. Jarman, S. OrtegaMartorell, P. J. G. Lisboa, and J. D. MartínGuerrero, “Music genre profiling based on fisher manifolds and probabilistic quantum clustering,” _Neural Computing and Applications_ , vol. 33, no. 13, pp. 7521–7539, Jul. 1, 2021. 

- [66] R. Castellon, C. Donahue, and P. Liang, “Codified audio language modeling learns useful representations for music information retrieval,” in _Proceedings of the 22nd International Society for Music Information Retrieval Conference_ , Online: ISMIR, Nov. 7, 2021, pp. 88–96. 

- [67] J. R. Castillo and M. J. Flores, “Web-based music genre classification for timeline song visualization and analysis,” _IEEE Access_ , vol. 9, pp. 18 801– 18 816, 2021. 

- [68] H. C. Ceylan, N. Hardalaç, A. C. Kara, and H. Firat, “Automatic music genre classification and its relation with music education,” _World Journal of Education_ , vol. 11, no. 2, pp. 36–45, 2021. 

- [69] W. H. Chak, N. Saito, and D. Weber, “The scattering transform network with generalized morse wavelets and its application to music genre classification,” in _2022 International Conference on Wavelet Analysis and Pattern Recognition (ICWAPR)_ , Sep. 2022, pp. 25–30. 

- [70] Y.-H. Chang and S.-N. Yao, “Artificial Intelligence on the Identification of Beiguan Music,” _Archives of Acoustics_ , vol. 46, no. 3, pp. 471–478, 2021. 

- [71] P.-C. Chang, Y.-S. Chen, and C.-H. Lee, “MSSincResNet: Joint learning of 1D and 2D kernels using multi-scale SincNet and ResNet for music genre classification,” in _Proceedings of the 2021 International Conference on Multimedia Retrieval_ , ser. ICMR ’21, New York, NY, USA: Association for Computing Machinery, Sep. 1, 2021, pp. 29– 36. 

- [72] S. Chapaneri, R. Lopes, and D. Jayaswal, “Evaluation of music features for PUK kernel based genre classification,” in _International Conference on Advanced Computing Technologies and Applications (ICACTA)_ , vol. 45, Jan. 1, 2015, pp. 186–196. 

- [73] D. Chathuranga and L. Jayaratne, “Automatic Music Genre Classification of Audio Signals with Machine Learning Approaches,” _GSTF Journal on Computing (JoC)_ , vol. 3, no. 2, p. 14, Aug. 16, 2013. 

- [74] E. Chaudary, S. Aziz, M. U. Khan, and P. Gretschmann, “Music genre classification using support vector machine and empirical mode decomposition,” in _2021 Mohammad Ali Jinnah University International Conference on Computing (MAJICC)_ , Jul. 2021, pp. 1–5. 

- [75] M. Chaudhury, A. Karami, and M. A. Ghazanfar, “Large-scale music genre analysis and classification using machine learning with apache spark,” _Electronics_ , vol. 11, no. 16, p. 2567, 16 Jan. 2022. 

- [76] O. Chavan, N. Kharade, A. Chaudhari, N. Bhalke, and P. Nimbalkar, “Machine learning and noise reduction techniques for music genre classification,” _International Research Journal of Engineering and Technology_ , vol. 6, no. 12, pp. 225–228, 2019. 

- [77] X. Chen and P. J. Ramadge, “Music genre classification using multiscale scattering and sparse representations,” in _2013 47th Annual Conference on Information Sciences and Systems (CISS)_ , Mar. 2013, pp. 1–6. 

- [78] S.-H. Chen, S.-Y. Ko, and S.-H. Chen, “Automatic music genre classification based on sparse representation and wavelet packet transform with discrete trigonometric transform,” in _2016 Third International Conference on Computing Measurement Control and Sensor Network (CMCSN)_ , May 2016, pp. 134–137. 

- [79] S.-H. Chen, S.-Y. Ko, and S.-H. Chen, “Robust music genre classification based on sparse representation and wavelet packet transform with discrete trigonometric transform.,” _Journal of Network Intelligence_ , vol. 1, no. 2, pp. 67–82, 2016. 

- [80] Y.-T. Chen, C.-H. Chen, S. Wu, and C.-C. Lo, “A two-step approach for classifying music genre on the strength of AHP weighted musical features,” _Mathematics_ , vol. 7, no. 1, p. 19, 1 Jan. 2019. 

- [81] K. Chen, B. Liang, X. Ma, and M. Gu, “Learning Audio Embeddings with User Listening Data for Content-Based Music Recommendation,” in _2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)_ , Jun. 2021, pp. 3015–3019. 

- [82] C. Chen and X. Steven, “Combined transfer and active learning for high accuracy music genre classification method,” in _2021 IEEE 2nd International Conference on Big Data, Artificial Intelligence and Internet of Things Engineering (ICBAIE)_ , Mar. 2021, pp. 53–56. 

- [83] W. Chen and G. Wu, “A multimodal convolutional neural network model for the analysis of music genre on children’s emotions influence intelligence,” _Computational Intelligence and Neuroscience_ , vol. 2022, e5611456, Aug. 29, 2022. 

- [84] Y.-H. Cheng, P.-C. Chang, and C.-N. Kuo, “Convolutional neural networks approach for music genre classification,” in _2020 International Symposium on Computer, Consumer and Control (IS3C)_ , Nov. 2020, pp. 399–403. 

- [85] Y.-H. Cheng, P.-C. Chang, D.-M. Nguyen, and C.-N. Kuo, “Automatic music genre classification based on CRNN.,” _Engineering Letters_ , vol. 29, no. 1, 2020. 

754 10 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

- [86] Y.-H. Cheng, P.-C. Chang, and C.-N. Kuo, “Music genre classification based on visualized spectrogram,” in _2021 International Conference on Technologies and Applications of Artificial Intelligence (TAAI)_ , Nov. 2021, pp. 217–221. 

- [87] G. Chettiar and S. Kalaivani, “Music genre classification techniques,” _International Journal of Engineering Research and Technology_ , vol. 10, no. 11, pp. 158–61, 2021. 

- [88] P. Chiliguano and G. Fazekas, “Hybrid music recommender using content-based and social information,” in _2016 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)_ , Mar. 2016, pp. 2618–2622. 

- [89] K. Choi, G. Fazekas, M. Sandler, and K. Cho, “Transfer learning for music classification and regression tasks,” in _Proceedings of the 18th International Society for Music Information Retrieval Conference_ , ISMIR, Sep. 13, 2017, pp. 141–149. arXiv: 1703.09179 [cs]. 

- [90] K. Choi, G. Fazekas, K. Cho, and M. Sandler, “The effects of noisy labels on deep convolutional neural networks for music tagging,” _IEEE Transactions on Emerging Topics in Computational Intelligence_ , vol. 2, no. 2, pp. 139–149, Apr. 2018. 

- [91] J. Choi, J. Lee, J. Park, and J. Nam, “Zero-shot Learning for Audio-based Music Classification and Tagging,” in _Proceedings of the 20th International Society for Music Information Retrieval Conference_ , ISMIR, 2019, pp. 67–74. arXiv: 1907 . 02670 [cs, eess]. 

- [92] C.-H. Chou and B.-J. Liao, “Music genre classification by analyzing the subband spectrogram,” in _2014 International Conference on Information Science, Electronics and Electrical Engineering_ , vol. 3, Apr. 2014, pp. 1677–1680. 

- [93] C.-H. Chou and J.-H. Shi, “Time-frequency analysis for music genre classification by using wavelet package decompositions,” in _2018 1st IEEE International Conference on Knowledge Innovation and Invention (ICKII)_ , Jul. 2018, pp. 134–137. 

- [94] Ö. Çoban, “Turkish music genre classification using audio and lyrics features,” _Journal of Natural and Applied Sciences_ , vol. 21, no. 2, pp. 322–331, 2 May 6, 2017. 

- [95] J. L. Conceição, R. de Freitas, B. Gadelha, J. G. Kienen, S. Anders, and B. Cavalcante, “Applying supervised learning techniques to brazilian music genre classification,” in _2020 XLVI Latin American Computing Conference (CLEI)_ , Oct. 2020, pp. 102–107. 

- [96] D. Conklin, “Fusion functions for multiple viewpoints,” in _Proceedings of the 6th International Workshop on Machine Learning and Music_ , 2013. 

- [97] A. D. Coronel, “Building an Initial Fitness Function Based on an Identified Melodic Feature Set for Classical and Non-Classical Melody Classification,” in _2013 International Conference on Information Science and Applications (ICISA)_ , Jun. 2013, pp. 1–4. 

- [98] D. C. Corrêa and F. A. Rodrigues, “A survey on symbolic data-based music genre classification,” _Expert Systems with Applications_ , vol. 60, pp. 190– 210, Oct. 30, 2016. 

- [99] Y. Costa, L. Oliveira, A. Koerich, and F. Gouyon, “Music genre recognition based on visual features with dynamic ensemble of classifiers selection,” in _2013 20th International Conference on Systems, Signals and Image Processing (IWSSIP)_ , Jul. 2013, pp. 55–58. 

- [100] Y. Costa, L. Oliveira, A. Koerich, and F. Gouyon, “Music Genre Recognition Using Gabor Filters and LPQ Texture Descriptors,” in _Progress in Pattern Recognition, Image Analysis, Computer Vision, and Applications_ , J. Ruiz-Shulcloper and G. Sanniti di Baja, Eds., ser. Lecture Notes in Computer Science, Berlin, Heidelberg: Springer, 2013, pp. 67–74. 

- [101] Y. M. G. Costa, L. S. Oliveira, and C. N. Silla, “An evaluation of convolutional neural networks for music classification using spectrograms,” _Applied Soft Computing_ , vol. 52, pp. 28–38, Mar. 1, 2017. 

- [102] D. A. Cruz, C. C. Cristancho, and J. E. Camargo, “Automatic Identification of Traditional Colombian Music Genres Based on Audio Content Analysis and Machine Learning Techniques,” in _Progress in Pattern Recognition, Image Analysis, Computer Vision, and Applications_ , I. Nyström, Y. Hernández Heredia, and V. Milián Núñez, Eds., Cham: Springer International Publishing, 2019, pp. 646– 655. 

- [103] J. Dai, W. Liu, C. Ni, L. Dong, and H. Yang, ““Multilingual”deep neural network for music genre classification,” in _Sixteenth Annual Conference of the International Speech Communication Association_ , 2015. 

- [104] J. Dai, W. Liu, H. Zheng, W. Xue, and C. Ni, “Semi-supervised learning of bottleneck feature for music genre classification,” in _Pattern Recognition_ , T. Tan, X. Li, X. Chen, J. Zhou, J. Yang, and H. Cheng, Eds., ser. Communications in Computer and Information Science, Singapore: Springer, 2016, pp. 552–562. 

- [105] J. Dai, S. Liang, W. Xue, C. Ni, and W. Liu, “Long short-term memory recurrent neural network based segment features for music genre classification,” in _2016 10th International Symposium on Chinese Spoken Language Processing (ISCSLP)_ , Oct. 2016, pp. 1–5. 

755 11 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

- [106] J. Dai, W. Xue, and W. Liu, “Multilingual i-vector based statistical modeling for music genre classification.,” in _Interspeech_ , 2017, pp. 459–463. 

- [107] S. Das and A. K. Kolya, “A theoretic approach to music genre recognition from musical features using single-layer feedforward neural network,” in _Emerging Technologies in Data Mining and Information Security_ , A. Abraham, P. Dutta, J. K. Mandal, A. Bhattacharya, and S. Dutta, Eds., ser. Advances in Intelligent Systems and Computing, Singapore: Springer, 2019, pp. 145–155. 

- [108] A. C. M. da Silva, P. R. V. do Carmo, R. M. Marcacini, and D. F. Silva, “Instance selection for music genre classification using heterogeneous networks,” in _Anais Do XVIII Simpósio Brasileiro de Computação Musical_ , SBC, 2021, pp. 8–16. 

- [109] V. H. Da Silva Muniz, J. B. de Oliveira, and S. Filho, “Feature vector design for music genre classification,” in _2021 IEEE Latin American Conference on Computational Intelligence (LA-CCI)_ , Nov. 2021, pp. 1–6. 

- [110] R. de Araújo Lima, R. C. C. de Sousa, H. Lopes, and S. D. J. Barbosa, “Brazilian lyrics-based music genre classification using a BLSTM network,” in _Artificial Intelligence and Soft Computing_ , L. Rutkowski, R. Scherer, M. Korytkowski, W. Pedrycz, R. Tadeusiewicz, and J. M. Zurada, Eds., ser. Lecture Notes in Computer Science, Cham: Springer International Publishing, 2020, pp. 525– 534. 

- [111] S. Deepak and B. Prasad, “Music classification based on genre using LSTM,” in _2020 Second International Conference on Inventive Research in Computing Applications (ICIRCA)_ , Jul. 2020, pp. 985–991. 

- [112] “Structured auto-encoder with application to music genre recognition,” M.S. thesis, Ecole Polytechnique Fédérale de Lausanne, 2015. 

- [113] M. Defferrard, K. Benzi, P. Vandergheynst, and X. Bresson, “FMA: A dataset for music analysis,” in _Proceedings of the 18th International Society for Music Information Retrieval Conference_ , arXiv, Sep. 5, 2017, pp. 316–323. arXiv: 1612.01840 [cs]. 

- [114] M. Defferrard, S. P. Mohanty, S. F. Carroll, and M. Salathé, “Learning to Recognize Musical Genre from Audio: Challenge Overview,” in _Companion Proceedings of the The Web Conference 2018_ , ser. WWW ’18, Republic and Canton of Geneva, CHE: International World Wide Web Conferences Steering Committee, Apr. 23, 2018, pp. 1921– 1922. 

- [115] P. J. P. de León, C. Pérez-Sancho, and J. M. Iñesta, “A shallow description framework for musical style recognition,” in _Structural, Syntactic, and Statistical Pattern Recognition_ , A. Fred, T. M. Caelli, R. P. W. Duin, A. C. Campilho, and D. de Ridder, Eds., ser. Lecture Notes in Computer Science, Berlin, Heidelberg: Springer, 2004, pp. 876– 884. 

- [116] F. A. de Leon and K. Martinez, “Music genre classification using polyphonic timbre models,” in _2014 19th International Conference on Digital Signal Processing_ , Aug. 2014, pp. 415–420. 

- [117] A. A. de Lima, R. M. Nunes, R. P. Ribeiro, and C. N. Silla, “Nordic Music Genre Classification Using Song Lyrics,” in _Natural Language Processing and Information Systems_ , E. Métais, M. Roche, and M. Teisseire, Eds., ser. Lecture Notes in Computer Science, Cham: Springer International Publishing, 2014, pp. 89–100. 

- [118] R. de Lima Aguiar, Y. M. e Gomes da Costa, and L. Nanni, “Music genre recognition using spectrograms with harmonic-percussive sound separation,” in _2016 35th International Conference of the Chilean Computer Science Society (SCCC)_ , Oct. 2016, pp. 1–7. 

- [119] G. Deng and Y. C. Ko, “Active learning music genre classification based on support vector machine,” _Advances in Multimedia_ , vol. 2022, e4705272, Jul. 7, 2022. 

- [120] R. De Prisco, D. Malandrino, G. Zaccagnino, R. Zaccagnino, and R. Zizza, “A bio-inspired approach to infer functional rules and aesthetic goals from music genre styles,” in _Proceedings of the 2017 International Conference on Computer Science and Artificial Intelligence_ , ser. CSAI 2017, New York, NY, USA: Association for Computing Machinery, Dec. 5, 2017, pp. 5–9. 

- [121] E. Dervakos, N. Kotsani, and G. Stamou, “Genre Recognition from Symbolic Music with CNNs,” in _Artificial Intelligence in Music, Sound, Art and Design_ , J. Romero, T. Martins, and N. RodríguezFernández, Eds., ser. Lecture Notes in Computer Science, Cham: Springer International Publishing, 2021, pp. 98–114. 

- [122] J. de Sousa, E. Torres Pereira, and L. Ribeiro Veloso, “A robust music genre classification approach for global and regional music datasets evaluation,” in _2016 IEEE International Conference on Digital Signal Processing (DSP)_ , Oct. 2016, pp. 109–113. 

- [123] P. Devaki, A. Sivanandan, R. S. Kumar, and M. Z. Peer, “Music genre classification and isolation,” in _2021 International Conference on Advancements in Electrical, Electronics, Communication, Computing and Automation (ICAECA)_ , Oct. 2021, pp. 1–6. 

756 12 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

- [124] M. K. Devi, U. Surya, Unnamalai. K, and Tharani. R. K, “Treatment for insomnia using music genre prediction using convolutional recurrent neural network,” in _2022 1st International Conference on Computational Science and Technology (ICCST)_ , Nov. 2022, pp. 919–922. 

- [125] A. Dhall, Y. V. Srinivasa Murthy, and S. G. Koolagudi, “Music genre classification with convolutional neural networks and comparison with F, Q, and mel spectrogram-based images,” in _Advances in Speech and Music Technology_ , A. Biswas, E. Wennekes, T.-P. Hong, and A. Wieczorkowska, Eds., ser. Advances in Intelligent Systems and Computing, Singapore: Springer, 2021, pp. 235–248. 

- [126] J. Dias, V. Pillai, H. Deshmukh, and A. Shah, “Music genre classification & recommendation system using CNN,” in _Proceedings of the 7th International Conference on Innovations and Research in Technology and Engineering (ICIRTE2022_ , Rochester, NY, Apr. 8, 2022. 

- [127] D. Diefenbach, P.-R. Lherisson, F. Muhlenbach, and P. Maret, “Computing the semantic relatedness of music genres using semantic web data,” presented at the Semantics 2016, Sep. 12, 2016. 

- [128] S. Dieleman and B. Schrauwen, “Multiscale approaches to music audio feature learning,” in _Proceedings of the 14th International Society for Music Information Retrieval Conference_ , De Souza Britto Jr., Alceu, Gouyon, Fabien, and Dixon, Simon, Eds., Pontifícia Universidade Católica do Paraná, 2013, pp. 116–121. 

- [129] I.-J. Ding, C.-T. Yen, C.-W. Chang, and H.-Z. Lin, “Optical music recognition of the singer using formant frequency estimation of vocal fold vibration and lip motion with interpolated GMM classifiers,” _Journal of Vibroengineering_ , vol. 16, no. 5, pp. 2572–2581, 5 Aug. 15, 2014. 

- [130] S. Dokania and V. Singh. “Graph representation learning for audio & music genre classification.” arXiv: 1910 . 11117 [cs, stat]. (Oct. 23, 2019), [Online]. Available: http : / / arxiv.org/abs/1910.11117 (visited on 03/03/2023), preprint. 

- [131] A. Dorochowicz, P. Hoffmann, A. Majdańczuk, and B. Kostek, “Classification of Music Genres by Means of Listening Tests and Decision Algorithms,” in _Intelligent Methods and Big Data in Industrial Applications_ , ser. Studies in Big Data, R. Bembenik, Ł. Skonieczny, G. Protaziuk, M. Kryszkiewicz, and H. Rybinski, Eds., Cham: Springer International Publishing, 2019, pp. 291– 305. 

- [132] S. M. Doudpota, S. Guha, and J. Baber, “Mining movies for song sequences with video based music genre identification system,” _Information Processing & Management_ , vol. 49, no. 2, pp. 529–544, Mar. 1, 2013. 

- [133] W. Du, H. Lin, J. Sun, B. Yu, and H. Yang, “A new hierarchical method for music genre classification,” in _2016 9th International Congress on Image and Signal Processing, BioMedical Engineering and Informatics (CISP-BMEI)_ , Oct. 2016, pp. 1033–1037. 

- [134] S. Duggirala and T.-S. Moh, “A novel approach to music genre classification using natural language processing and spark,” in _2020 14th International Conference on Ubiquitous Information Management and Communication (IMCOM)_ , Jan. 2020, pp. 1–8. 

- [135] A. Elbir, H. O. İlhan, G. Serbes, and N. Aydın, “Short time fourier transform based music genre classification,” in _2018 Electric Electronics, Computer Science, Biomedical Engineerings’ Meeting (EBBT)_ , Apr. 2018, pp. 1–4. 

- [136] A. Elbir, H. Bilal Çam, M. Emre Iyican, B. Öztürk, and N. Aydin, “Music genre classification and recommendation by using machine learning techniques,” in _2018 Innovations in Intelligent Systems and Applications Conference (ASYU)_ , Oct. 2018, pp. 1–5. 

- [137] A. Elbir and N. Aydin, “Music genre classification and music recommendation by using deep learning,” _Electronics Letters_ , vol. 56, no. 12, pp. 627– 629, 2020. 

- [138] A. Eppler, A. Männchen, J. Abeßer, C. Weiß, and K. Frieler, “Automatic style classification of jazz recordings with respect to rhythm, tempo, and tonality,” in _Proceedings of the 9th Conference on Interdisciplinary Musicology_ , Dec. 4, 2014. 

- [139] E. V. Epure, A. Khlif, and R. Hennequin, “Leveraging knowledge bases and parallel annotations for music genre translation,” in _Proceedings of the 20th International Society for Music Information Retrieval Conference_ , arXiv, Jul. 27, 2019, pp. 839–846. arXiv: 1907.08698 [cs, eess, stat]. 

- [140] T. M. Esparza, J. P. Bello, and E. J. Humphrey, “From genre classification to rhythm similarity: Computational and musicological insights,” _Journal of New Music Research_ , vol. 44, no. 1, pp. 39– 57, Jan. 2, 2015. 

- [141] S. Evstifeev and I. Shanin, “Music genre classification based on signal processing.,” in _Data Analytics and Management in Data-Intensive Domains_ , 2018, pp. 157–161. 

757 13 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

- [142] P. B. Falola and S. O. Akinola, “Music genre classification using 1D convolution neural network,” _International Journal of Human Computing Studies_ , vol. 3, no. 6, pp. 3–21, 2021. 

- [143] S. Fan and M. Fu, “Music genre recommendation based on MLP & random forest,” in _2022 IEEE 5th International Conference on Information Systems and Computer Aided Education (ICISCAE)_ , Sep. 2022, pp. 331–334. 

- [144] X. Favory, K. Drossos, T. Virtanen, and X. Serra, “COALA: Co-Aligned Autoencoders for Learning Semantically Enriched Audio Representations,” presented at the ICML 2020 Workshop on Self-Supervision in Audio and Speech, arXiv, Jul. 8, 2020. arXiv: 2006.08386 [cs, eess, stat]. 

- [145] X. Favory, K. Drossos, T. Virtanen, and X. Serra, “Learning Contextual Tag Embeddings for Cross-Modal Alignment of Audio and Tags,” in _2021 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)_ , Jun. 2021, pp. 596–600. 

- [146] M. Fell and C. Sporleder, “Lyrics-based Analysis and Classification of Music,” in _Proceedings of COLING 2014_ , Dublin, Ireland, 2014, pp. 620– 631. 

- [147] L. Feng, S. Liu, and J. Yao. “Music genre classification with paralleling recurrent convolutional neural network.” arXiv: 1712 . 08370 [cs, eess]. (Dec. 22, 2017), [Online]. Available: http://arxiv.org/abs/1712.08370 (visited on 03/03/2023), preprint. 

- [148] A. Ferraro and K. Lemström, “On large-scale genre classification in symbolically encoded music by automatic identification of repeating patterns,” in _Proceedings of the 5th International Conference on Digital Libraries for Musicology_ , ser. DLfM ’18, New York, NY, USA: Association for Computing Machinery, Sep. 28, 2018, pp. 34–37. 

- [149] A. Flexer, E. Pampalk, and G. Widmer, “Novelty Detection Based on Spectral Similarity of Songs.,” in _Proceedings of the 6th International Conference on Music Information Retrieval_ , London: ISMIR, 2005, pp. 260–263. 

- [150] A. Flexer, “Hubness-aware outlier detection for music genre recognition,” in _Proceedings of the 19th International Conference on Digital Audio Effects (DAFx-16),_ , Brno, Czech Republic, 2016. 

- [151] J. H. Foleis and T. F. Tavares, “Texture selection for automatic music genre classification,” _Applied Soft Computing_ , vol. 89, p. 106 127, Apr. 1, 2020. 

- [152] J. H. Foleiss and T. F. Tavares. “Random projections of mel-spectrograms as low-level features for automatic music genre classification.” arXiv: 1911 . 04660 [cs, eess]. (Nov. 11, 2019), [Online]. Available: http : / / arxiv . org / abs / 1911 . 04660 (visited on 03/09/2023), preprint. 

- [153] S. O. Folorunso, S. A. Afolabi, and A. B. Owodeyi, “Dissecting the genre of nigerian music with machine learning models,” _Journal of King Saud University - Computer and Information Sciences_ , vol. 34, pp. 6266–6279, 8, Part B Sep. 1, 2022. 

- [154] H. Foroughmand Aarabi and G. Peeters, “Extending Deep Rhythm for Tempo and Genre Estimation Using Complex Convolutions, Multitask Learning and Multi-input Network,” _Journal of Creative Music Systems_ , vol. 1, no. 1, Aug. 30, 2022. 

- [155] A. Foroughmand Arabi, “Enhanced polyphonic music genre classification using high level features,” thesis, Monash University, 2009. 

- [156] E. Fotiadou, N. Bassiou, and C. Kotropoulos, “Greek folk music classification using auditory cortical representations,” in _2016 24th European Signal Processing Conference (EUSIPCO)_ , Aug. 2016, pp. 1133–1137. 

- [157] R. Foucard, S. Essid, G. Richard, and M. Lagrange, “Exploring new features for music classification,” in _2013 14th International Workshop on Image Analysis for Multimedia Interactive Services (WIAMIS)_ , Jul. 2013, pp. 1–4. 

- [158] P. Fulzele, R. Singh, N. Kaushik, and K. Pandey, “A hybrid model for music genre classification using LSTM and SVM,” in _2018 Eleventh International Conference on Contemporary Computing (IC3)_ , Aug. 2018, pp. 1–3. 

- [159] M. N. Furqon, K. Khadijah, S. Suhartono, and R. Kusumaningrum, “Indonesian music genre classification on indonesian regional songs using deep recurrent neural network method,” in _2019 3rd International Conference on Informatics and Computational Sciences (ICICoS)_ , Oct. 2019, pp. 1–5. 

- [160] B. Gao, “Contributions to music semantic analysis and its acceleration techniques,” Ph.D. dissertation, Ecole Centrale de Lyon, Dec. 15, 2014. 

- [161] S. Geng, G. Ren, and M. Ogihara, “Transforming musical signals through a genre classifying convolutional neural network,” in _Proceedings of the First International Workshop on Deep Learning and Music, Joint with IJCNN_ , D. Herremans and C.-H. Chuan, Eds., Anchorage, US: arXiv, Jun. 28, 2017. arXiv: 1706.09553 [cs]. 

- [162] J. George and L. Shamir, “Unsupervised analysis of similarities between musicians and musical genres using spectrograms.,” _Artificial Intelligence Research_ , vol. 4, no. 2, pp. 61–71, 2015. 

758 14 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

- [163] P. Ghaemmaghami and N. Sebe, “Brain and music: Music genre classification using brain signals,” in _2016 24th European Signal Processing Conference (EUSIPCO)_ , Aug. 2016, pp. 708–712. 

- [164] A. Ghildiyal, K. Singh, and S. Sharma, “Music genre classification using machine learning,” in _2020 4th International Conference on Electronics, Communication and Aerospace Technology (ICECA)_ , Nov. 2020, pp. 1368–1372. 

- [165] A. Ghildiyal and S. Sharma, “Music genre classification using data filtering algorithm: An artificial intelligence approach,” in _2021 Third International Conference on Inventive Research in Computing Applications (ICIRCA)_ , Sep. 2021, pp. 922–926. 

- [166] A. Ghosal, R. Chakraborty, B. C. Dhara, and S. K. Saha, “Genre-Based Classification of Song Using Perceptual Features,” in _Intelligent Computing, Networking, and Informatics_ , D. P. Mohapatra and S. Patnaik, Eds., ser. Advances in Intelligent Systems and Computing, New Delhi: Springer India, 2014, pp. 267–276. 

- [167] A. Ghosal, R. Chakraborty, B. C. Dhara, and S. K. Saha, “Perceptual feature-based song genre classification using RANSAC,” _International Journal of Computational Intelligence Studies_ , vol. 4, no. 1, pp. 31–49, Jan. 2015. 

- [168] D. Ghosal and M. Kolekar, “Music genre recognition using deep neural networks and transfer learning,” presented at the Interspeech, Sep. 2, 2018, pp. 2087–2091. 

- [169] D. Ghosal and M. F. Kolekar, “Musical genre and style recognition using deep neural networks and transfer learning,” in _Proceedings, APSIPA Annual Summit and Conference_ , vol. 2018, 2018, pp. 12– 15. 

- [170] S. S. Ghosal and I. Sarkar, “Novel approach to music genre classification using clustering augmented learning method (CALM).,” in _AAAI Spring Symposium: Combining Machine Learning with Knowledge Engineering_ , 2020. 

- [171] P. Ginsel, I. Vatolkin, and G. Rudolph, “Analysis of structural complexity features for music genre recognition,” in _2020 IEEE Congress on Evolutionary Computation (CEC)_ , Jul. 2020, pp. 1–8. 

- [172] A. Girase, A. Advirkar, C. Patil, D. Khadpe, and A. Pokhare, “Lyrics Based Song Genre Classification,” _Journal of Computing Technologies_ , vol. 3, no. 2, pp. 16–19, 2014. 

- [173] I. N. Y. T. Giria, L. A. A. R. Putria, G. A. V. M. Giria, I. G. N. A. C. Putraa, I. M. Widiarthaa, and I. W. Suprianaa, “Music Genre Classification Using Modified K-Nearest Neighbor (MKNN),” _JELIKU (Jurnal Elektronik Ilmu Komputer Udayana)_ , vol. 10, no. 3, p. 5373, 2022. 

- [174] A. Goel, Mohd. Sheezan, S. Masood, and A. Saleem, “Genre classification of songs using neural network,” in _2014 International Conference on Computer and Communication Technology (ICCCT)_ , Sep. 2014, pp. 285–289. 

- [175] I. Goienetxea, J. M. Martínez-Otzeta, B. Sierra, and I. Mendialdua, “Towards the use of similarity distances to music genre classification: A comparative study,” _PLoS ONE_ , vol. 13, no. 2, e0191417, Feb. 14, 2018. 

- [176] C. K. Gomathy and V. Geetha, “Music classification management system,” _International Journal of Early Childhood Special Education (INT-JECSE)_ , vol. 10, no. 5, 2022. 

- [177] W. Gong and Q. Yu, “A deep music recommendation method based on human motion analysis,” _IEEE Access_ , vol. 9, pp. 26 290–26 300, 2021. 

- [178] R. Gupta, J. Yadav, and C. Kapoor, “Music information retrieval and intelligent genre classification,” in _Proceedings of International Conference on Intelligent Computing, Information and Control Systems_ , A. P. Pandian, R. Palanisamy, and K. Ntalianis, Eds., ser. Advances in Intelligent Systems and Computing, Singapore: Springer, 2021, pp. 207–224. 

- [179] R. Gusain, S. Sonker, S. K. Rai, A. Arora, and S. Nagarajan, “Comparison of neural networks and xgboost algorithm for music genre classification,” in _2022 2nd International Conference on Intelligent Technologies (CONIT)_ , Jun. 2022, pp. 1–6. 

- [180] P. Hamel, M. E. P. Davies, K. Yoshii, and M. Goto, “Transfer learning in MIR: Sharing learned latent representations for music audio classification and similarity,” in _Proceedings of the 14th International Society for Music Information Retrieval Conference_ , A. de Souza Britto Jr., F. Gouyon, and S. Dixon, Eds., 2013, pp. 9–14. 

- [181] L. K. Hansen, T. Lehn-Schiøler, K. B. Petersen, J. Arenas-García, J. Larsen, and S. H. Jensen, “Learning and clean-up in a large scale music database,” in _2007 15th European Signal Processing Conference_ , Sep. 2007, pp. 946–950. 

- [182] I. U. Haq, F. Khan, S. Sharif, and A. Shaukat, “Automatic music genres classification as a pattern recognition problem,” in _Sixth International Conference on Machine Vision (ICMV 2013)_ , vol. 9067, SPIE, Dec. 24, 2013, pp. 438–443. 

- [183] M. Haro Berois, “Statistical distribution of common audio features : Encounters in a heavy-tailed universe,” Ph.D. dissertation, Universitat Pompeu Fabra, Nov. 22, 2013. 

- [184] M. Hartmann, P. Saari, P. Toiviainen, and O. Lartillot, “Comparing Timbre-based Features for Musical Genre Classification,” in _Proceedings of the 10th Sound and Music Computing Conference_ , Stockholm, Sweden, 2013. 

759 15 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

- [185] R. Hasan, S. Hossain, F. I. Alam, and M. Barua, “Bangla music genre classification using fast and scalable integrated ensemble boosting framework,” in _2021 3rd International Conference on Sustainable Technologies for Industry 4.0 (STI)_ , Dec. 2021, pp. 1–6. 

- [186] K. M. Hasib, A. Tanzim, J. Shin, K. O. Faruk, J. A. Mahmud, and M. F. Mridha, “BMNet-5: A novel approach of neural network to classify the genre of bengali music based on audio features,” _IEEE Access_ , vol. 10, pp. 108 545–108 563, 2022. 

- [187] Q. He, “A music genre classification method based on deep learning,” _Mathematical Problems in Engineering_ , vol. 2022, e9668018, Mar. 29, 2022. 

- [188] A. Heakl, A. Abdelgawad, and V. Parque, “A study on broadcast networks for music genre classification,” in _2022 International Joint Conference on Neural Networks (IJCNN)_ , Jul. 2022, pp. 1–8. 

- [189] F. Heerde, I. Vatolkin, and G. Rudolph, “Comparing fuzzy rule based approaches for music genre classification,” in _Artificial Intelligence in Music, Sound, Art and Design_ , J. Romero, A. Ekárt, T. Martins, and J. Correia, Eds., ser. Lecture Notes in Computer Science, Cham: Springer International Publishing, 2020, pp. 35–48. 

- [190] R. Hennequin, J. Royo-Letelier, and M. Moussallam, “Audio Based Disambiguation of Music Genre Tags,” in _Proceedings of the 19th International Society for Music Information Retrieval Conference_ , Paris, France: ISMIR, Sep. 23, 2018, pp. 645–652. 

- [191] M. Henry, W. Chandra, and A. Zahra, “Implementation of apriori algorithm for music genre recommendation,” _Jurnal Online Informatika_ , vol. 7, no. 1, pp. 110–115, 2022. 

- [192] J. Heo, H.-s. Shin, J.-h. Kim, C.-y. Lim, and H.-J. Yu. “Convolution channel separation and frequency sub-bands aggregation for music genre classification.” arXiv: 2211 . 01599 [cs, eess]. (Nov. 3, 2022), [Online]. Available: http://arxiv.org/abs/2211.01599 (visited on 03/23/2023), preprint. 

- [193] L. Hoang, “Literature review about music genre classification,” in _Woodstock_ ’ _18: ACM Symposium on Neural Gaze Detection_ , Woodstock, NY: ACM, 2018. 

- [194] J. Hockman, J. Bello, M. Davies, and M. Plumbley, “Automated rhythmic transformation of musical audio,” in _Proceedings - 11th International Conference on Digital Audio Effects, DAFx 2008_ , 2008, pp. 177–180. 

- [195] P. Hoffmann and B. Kostek, “Music data processing and mining in large databases for active media,” in _Active Media Technology_ , D. Ślȩzak, G. Schaefer, S. T. Vuong, and Y.-S. Kim, Eds., ser. Lecture Notes in Computer Science, Cham: Springer International Publishing, 2014, pp. 85– 95. 

- [196] P. Hoffmann and B. Kostek, “Music genre recognition in the rough set-based environment,” in _Pattern Recognition and Machine Intelligence_ , M. Kryszkiewicz, S. Bandyopadhyay, H. Rybinski, and S. K. Pal, Eds., ser. Lecture Notes in Computer Science, Cham: Springer International Publishing, 2015, pp. 377–386. 

- [197] P. Hoffmann and B. Kostek, “Bass enhancement settings in portable devices based on music genre recognition,” _Journal of the Audio Engineering Society_ , vol. 63, no. 12, pp. 980–989, Jan. 6, 2016. 

- [198] W. Hongdan, S. SalmiJamali, C. Zhengping, S. Qiaojuan, and R. Le, “An intelligent music genre analysis using feature extraction and classification using deep learning techniques,” _Computers & Electrical Engineering_ , vol. 100, p. 107 978, May 1, 2022. 

- [199] R. Hossain and A. Al Marouf, “BanglaMusicStylo: A stylometric dataset of bangla music lyrics,” in _2018 International Conference on Bangla Speech and Language Processing (ICBSLP)_ , Sep. 2018, pp. 1–5. 

- [200] K.-C. Hsu, C.-S. Lin, and T.-S. Chi, “Sparse coding based music genre classification using spectrotemporal modulations.,” in _Proceedings of the 17th International Society for Music Information Retrieval Conference_ , ISMIR, 2016, pp. 744–750. 

- [201] W.-H. Hsu, B.-Y. Chen, and Y.-H. Yang. “Deep Learning Based EDM Subgenre Classification using Mel-Spectrogram and Tempogram Features.” arXiv: 2110 . 08862 [cs, eess]. (Oct. 17, 2021), [Online]. Available: http : / / arxiv . org / abs / 2110 . 08862 (visited on 03/24/2023), preprint. 

- [202] X. Hu, J. S. Downie, K. West, and A. F. Ehmann, “Mining music reviews: Promising preliminary results.,” in _Proceedings of the 6th International Conference on Music Information Retrieval_ , London, United Kingdom: ISMIR, Sep. 11, 2005, pp. 536–539. 

- [203] Y.-F. Huang, S.-M. Lin, H.-Y. Wu, and Y.-S. Li, “Music genre classification based on local feature selection using a self-adaptive harmony search algorithm,” _Data & Knowledge Engineering_ , vol. 92, pp. 60–76, Jul. 1, 2014. 

760 16 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

- [204] I. Ikhsan, L. Novamizanti, and I. N. A. Ramatryana, “Automatic musical genre classification of audio using Hidden Markov Model,” in _2014 2nd International Conference on Information and Communication Technology (ICoICT)_ , May 2014, pp. 397– 402. 

- [205] S. Iloga, O. Romain, L. Bendaouia, and M. Tchuente, “Musical genres classification using Markov models,” in _2014 International Conference on Audio, Language and Image Processing_ , Shanghai, China: IEEE, Jul. 2014, pp. 701–705. 

- [206] S. Iloga, O. Romain, and M. Tchuenté, “A sequential pattern mining approach to design taxonomies for hierarchical music genre recognition,” _Pattern Analysis and Applications_ , vol. 21, no. 2, pp. 363– 380, May 1, 2018. 

- [207] D. Imran, H. Wadiwala, M. A. Tahir, and M. Rafi, “Semantic feature extraction using feed-forward neural network for music genre classification.,” _Asian Journal of Engineering, Sciences & Technology_ , vol. 7, no. 2, 2017. 

- [208] M. S. Islam _et al._ , “Machine learning-based music genre classification with pre-processed feature analysis,” _Jurnal Ilmiah Teknik Elektro Komputer dan Informatika_ , vol. 7, no. 3, pp. 491–502, 2021. 

- [209] K. Itoyama, M. Goto, K. Komatani, T. Ogata, and H. G. Okuno, “Query-by-example music retrieval approach based on musical genre shift by changing instrument volume,” in _Proceedings of the 12th Int. Conference on Digital Audio Effects (DAFx-09),_ , Como, Italy, 2009. 

- [210] R. Jain, R. Sharma, P. Nagrath, and R. Jain, “Music genre classification ChatBot,” in _Proceedings of Second International Conference on Computing, Communications, and Cyber-Security_ , P. K. Singh, S. T. Wierzchoń, S. Tanwar, M. Ganzha, and J. J. P. C. Rodrigues, Eds., ser. Lecture Notes in Networks and Systems, Singapore: Springer, 2021, pp. 393–408. 

- [211] M. Jakubec and M. Chmulik, “Automatic music genre recognition for in-car infotainment,” _Transportation Research Procedia_ , TRANSCOM 2019 13th International Scientific Conference on Sustainable, Modern and Safe Transport, vol. 40, pp. 1364–1371, Jan. 1, 2019. 

- [212] D. Jang and S.-J. Jang, “Very short feature vector for music genre classiciation based on distance metric lerning,” in _2014 International Conference on Audio, Language and Image Processing_ , Jul. 2014, pp. 726–729. 

- [213] P.-K. Jao, L. Su, and Y.-H. Yang, “Analyzing the dictionary properties and sparsity constraints for a dictionary-based music genre classification system,” in _2013 Asia-Pacific Signal and Information Processing Association Annual Summit and Conference_ , Oct. 2013, pp. 1–8. 

- [214] P.-K. Jao, C.-C. M. Yeh, and Y.-H. Yang, “Modified lasso screening for audio word-based music classification using large-scale dictionary,” in _2014 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)_ , May 2014, pp. 5207–5211. 

- [215] P.-K. Jao and Y.-H. Yang, “Music annotation and retrieval using unlabeled exemplars: Correlation and sparse codes,” _IEEE Signal Processing Letters_ , vol. 22, no. 10, pp. 1771–1775, Oct. 2015. 

- [216] G. JawaherlalNehru, S. Jothilakshmi, S. Jothishri, S. Bavankumar, B. Rajalingam, and R. Santhoshkumar, “Music genre classification using deep learning techniques,” _Turkish Online Journal of Qualitative Inquiry_ , vol. 12, no. 8, pp. 7293– 7305, 8 Nov. 10, 2021. 

- [217] B. S. Jensen, R. Troelsgaard, J. Larsen, and L. K. Hansen, “Towards a universal representation for audio information retrieval and analysis,” in _2013 IEEE International Conference on Acoustics, Speech and Signal Processing_ , May 2013, pp. 3168–3172. 

- [218] I.-Y. Jeong and K. Lee, “Learning temporal features using a deep neural network and its application to music genre classification.,” in _Proceedings of the 17th International Society for Music Information Retrieval Conference_ , New York City, United States, 2016, pp. 434–440. 

- [219] Z. Jiang and H. N. Huynh, “Unveiling music genre structure through common-interest communities,” _Social Network Analysis and Mining_ , vol. 12, no. 1, p. 35, Feb. 14, 2022. 

- [220] C. Johnson-Roberson and E. Sudderth, “Contentbased genre classification and sample recognition using topic models,” M.S. thesis, Brown University, 2015. 

- [221] A. Kamala and H. Hassani, “Kurdish music genre recognition using a CNN and DNN,” _Engineering Proceedings_ , vol. 31, no. 1, p. 64, 1 2022. 

- [222] K. Kamtue, K. Euchukanonchai, D. Wanvarie, and N. Pratanwanich, “Lukthung Classification Using Neural Networks on Lyrics and Audios,” in _2019 23rd International Computer Science and Engineering Conference (ICSEC)_ , Oct. 2019, pp. 269– 274. 

- [223] E. Kanalici and G. Bilgin, “Music genre classification via sequential wavelet scattering feature learning,” in _Knowledge Science, Engineering and Management_ , C. Douligeris, D. Karagiannis, and D. Apostolou, Eds., ser. Lecture Notes in Computer Science, Cham: Springer International Publishing, 2019, pp. 365–372. 

761 17 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

- [224] K. Kang and F. Lin. “Computing Class Hierarchies from Classifiers.” arXiv: 2112 . 01187 [cs]. (Dec. 2, 2021), [Online]. Available: http : / / arxiv.org/abs/2112.01187 (visited on 03/24/2023), preprint. 

- [225] D. Kania, P. Kania, and T. Łukaszewicz, “Trajectory of fifths in music data mining,” _IEEE Access_ , vol. 9, pp. 8751–8761, 2021. 

- [226] G. Karamanolakis, E. Iosif, A. Zlatintsi, A. Pikrakis, and A. Potamianos, “Audio-based distributional semantic models for music auto-tagging and similarity measurement,” in _Multi-Learn 2017 Workshop at the 25th European Signal Processing Conference_ , Kos Island, Greece, 2017. 

- [227] N. Karunakaran and A. Arya, “A scalable hybrid classifier for music genre classification using machine learning concepts and spark,” in _2018 International Conference on Intelligent Autonomous Systems (ICoIAS)_ , Mar. 2018, pp. 128–135. 

- [228] E. Karystinaios, C. Guichaoua, M. Andreatta, L. Bigo, and I. Bloch, “Music genre descriptor for classification based on tonnetz trajectories,” in _Acte Musical et Environnements Informatiques : Actes Des Journées d_ ’ _Informatique Musicale 2020 (JIM 2020)_ , 2021. 

- [229] C. Kaur and R. Kumar, “Study and analysis of feature based automatic music genre classification using gaussian mixture model,” in _2017 International Conference on Inventive Computing and Informatics (ICICI)_ , Nov. 2017, pp. 465–468. 

- [230] A. J. E. Kell, D. L. K. Yamins, E. N. Shook, S. V. Norman-Haignere, and J. H. McDermott, “A TaskOptimized Neural Network Replicates Human Auditory Behavior, Predicts Brain Responses, and Reveals a Cortical Processing Hierarchy,” _Neuron_ , vol. 98, no. 3, 630–644.e16, May 2, 2018. 

- [231] C. Kereliuk, B. L. Sturm, and J. Larsen, “Deep learning, audio adversaries, and music content analysis,” in _2015 IEEE Workshop on Applications of Signal Processing to Audio and Acoustics_ , 2015. 

- [232] C. Kereliuk, B. L. Sturm, and J. Larsen, “Deep learning and music adversaries,” _IEEE Transactions on Multimedia_ , vol. 17, no. 11, pp. 2059– 2071, Sep. 2015. 

- [233] Y. Khasgiwala and J. Tailor, “Vision transformer for music genre classification using mel-frequency cepstrum coefficient,” in _2021 IEEE 4th International Conference on Computing, Power and Communication Technologies (GUCON)_ , Sep. 2021, pp. 1–5. 

- [234] Y. Kikuchi and N. Aoki, “A study on automatic music genre classification based on the summarization of music data,” in _2020 International Conference on Artificial Intelligence in Information and Communication (ICAIIC)_ , Feb. 2020, pp. 705–708. 

- [235] J. Kim, M. Won, X. Serra, and C. C. S. Liem, “Transfer Learning of Artist Group Factors to Musical Genre Classification,” in _Companion of the The Web Conference 2018 on The Web Conference 2018 - WWW ’18_ , 2018, pp. 1929–1934. arXiv: 1805.02043 [cs, eess, stat]. 

- [236] J. Kim, J. Urbano, C. C. S. Liem, and A. Hanjalic, “One deep music representation to rule them all? A comparative analysis of different representation learning strategies,” _Neural Computing and Applications_ , vol. 32, no. 4, pp. 1067–1093, Feb. 1, 2020. 

- [237] J. Kim and C. C. S. Liem, “The power of deep without going deep? A study of HDPGMM music representation learning,” in _Proceedings of the 23rd International Society for Music Information Retrieval Conference_ , Bengaluru, India: ISMIR, Dec. 4, 2022, pp. 116–124. 

- [238] M. A. Kızrak, K. S. Bayram, and B. Bolat, “Classification of Classic Turkish Music Makams,” in _2014 IEEE International Symposium on Innovations in Intelligent Systems and Applications (INISTA) Proceedings_ , Jun. 2014, pp. 394–397. 

- [239] M. Kleć and D. Koržinek, “Unsupervised feature pre-training of the scattering wavelet transform for musical genre recognition,” in _International Workshop on Innovations in Information and Communication Science and Technology_ , vol. 18, Jan. 1, 2014, pp. 133–139. 

- [240] M. Kleć and D. Korzinek, “Pre-trained deep neural network using sparse autoencoders and scattering wavelet transform for musical genre recognition,” _Computer Science_ , vol. 16, no. 2, pp. 133– 144, 2015. 

- [241] M. Kleć, “Multi-instrumental deep learning for automatic genre recognition,” in _Recent Developments in Intelligent Information and Database Systems_ , Springer, 2016, pp. 53–61. 

- [242] M. Kobayakawa, M. Hoshi, and K. Yuzawa, “Music genre classification of MPEG AAC audio data,” in _2014 IEEE International Symposium on Multimedia_ , Dec. 2014, pp. 347–352. 

- [243] T. Kobayashi, A. Kubota, and Y. Suzuki, “Audio feature extraction based on sub-band signal correlations for music genre classification,” in _2018 IEEE International Symposium on Multimedia (ISM)_ , Dec. 2018, pp. 180–181. 

- [244] A. L. Koerich, “Improving the Reliability of Music Genre Classification using Rejection and Verification.,” in _Proceedings of the 14th International Society for Music Information Retrieval Conference_ , Curitiba, Brazil: ISMIR, Nov. 4, 2013, pp. 511– 516. 

762 18 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

- [245] S. Koparde, V. R. Bhadgaonkar, K. N. Patil, G. N. Basutkar, and D. D. Gayke, “A survey on music genre classification using machine learning,” _International Research Journal of Engineering and Technology_ , vol. 08, no. 03, pp. 640–644, 2021. 

- [246] G. Korvel and B. Kostek, “Discovering rule-based learning systems for the purpose of music analysis,” in _Proceedings of Meetings on Acoustics_ , vol. 39, Acoustical Society of America, Dec. 2, 2019, p. 035 004. 

- [247] B. Kostek, “Music Information Retrieval in Music Repositories,” in _Rough Sets and Intelligent Systems - Professor Zdzisław Pawlak in Memoriam: Volume 1_ , ser. Intelligent Systems Reference Library, A. Skowron and Z. Suraj, Eds., Berlin, Heidelberg: Springer, 2013, pp. 463–489. 

- [248] B. Kostek, P. Hoffmann, A. Kaczmarek, and P. Spaleniak, “Creating a Reliable Music Discovery and Recommendation System,” in _Intelligent Tools for Building a Scientific Information Platform: From Research to Implementation_ , ser. Studies in Computational Intelligence, R. Bembenik, Ł. Skonieczny, H. Rybiński, M. Kryszkiewicz, and M. Niezgódka, Eds., Cham: Springer International Publishing, 2014, pp. 107–130. 

- [249] D. Kostrzewa, R. Brzeski, and M. Kubanski, “The classification of music by the genre using the KNN classifier,” in _Beyond Databases, Architectures and Structures. Facing the Challenges of Data Proliferation and Growing Variety_ , S. Kozielski, D. Mrozek, P. Kasprowski, B. Małysiak-Mrozek, and D. Kostrzewa, Eds., ser. Communications in Computer and Information Science, Cham: Springer International Publishing, 2018, pp. 233–242. 

- [250] D. Kostrzewa, P. Kaminski, and R. Brzeski, “Music genre classification: Looking for the perfect network,” in _Computational Science_ – _ICCS 2021_ , M. Paszynski, D. Kranzlmüller, V. V. Krzhizhanovskaya, J. J. Dongarra, and P. M. A. Sloot, Eds., ser. Lecture Notes in Computer Science, Cham: Springer International Publishing, 2021, pp. 55–67. 

- [251] N. Kothari and P. Kumar, “Literature survey for music genre classification using neural network,” _International Research Journal of Engineering and Technology_ , vol. 9, pp. 691–695, 2022. 

- [252] A. Kotsifakos, E. E. Kotsifakos, P. Papapetrou, and V. Athitsos, “Genre classification of symbolic music with SMBGT,” in _Proceedings of the 6th International Conference on PErvasive Technologies Related to Assistive Environments_ , ser. PETRA ’13, New York, NY, USA: Association for Computing Machinery, May 29, 2013, pp. 1–7. 

- [253] G. Kour and N. Mehan, “Music genre classification using MFCC, SVM and BPNN,” _International Journal of Computer Applications_ , vol. 112, no. 6, pp. 12–14, Feb. 18, 2015. 

- [254] A. Koutras, “Song emotion recognition using music genre information,” in _Speech and Computer_ , A. Karpov, R. Potapova, and I. Mporas, Eds., ser. Lecture Notes in Computer Science, Cham: Springer International Publishing, 2017, pp. 669– 679. 

- [255] D. Kowald, E. Lex, and M. Schedl, “Utilizing human memory processes to model genre preferences for personalized music recommendations,” in _IUI ’20: Proceedings of the 25th International Conference on Intelligent User Interfaces Companion_ , ACM, Mar. 24, 2020, pp. 19–20. arXiv: 2003. 10699 [cs]. 

- [256] P. P. Kuksa. “Efficient multivariate sequence classification.” arXiv: 1409.8211 [cs]. (Sep. 30, 2014), [Online]. Available: http : / / arxiv . org/abs/1409.8211 (visited on 02/19/2024), preprint. 

- [257] D. P. Kumar, B. J. Sowmya, Chetan, and K. G. Srinivasa, “A comparative study of classifiers for music genre classification based on feature extractors,” in _2016 IEEE Distributed Computing, VLSI, Electrical Circuits and Robotics (DISCOVER)_ , Aug. 2016, pp. 190–194. 

- [258] A. Kumar, B. K. S. Siva, G. S. Reddy, and M. R. Rashmi, “Music genre classification,” _International Research Journal of Engineering and Technology_ , vol. 4, no. 4, pp. 3412–3414, 2017. 

- [259] B. Kumaraswamy and P. G. Poonacha, “Deep convolutional neural network for musical genre classification via new self adaptive sea lion optimization,” _Applied Soft Computing_ , vol. 108, p. 107 446, Sep. 1, 2021. 

- [260] B. Kumaraswamy, “Optimized deep learning for genre classification via improved moth flame algorithm,” _Multimedia Tools and Applications_ , vol. 81, no. 12, pp. 17 071–17 093, May 1, 2022. 

- [261] N. Kumari, T. Shukla, K. S. Swati, and K. Balachandra, “Music genre classification for indian music genres,” _International Journal for Research in Applied Science and Engineering Technology_ , vol. 9, no. 8, pp. 1756–1762, 2021. 

- [262] B. Lansdown, “Machine Learning for Music Genre Classification,” M.S. thesis, University of Birmingham, Sep. 1, 2019. 

- [263] D. S. Lau and R. Ajoodha, “Music genre classification: A comparative study between deep learning and traditional machine learning approaches,” in _Proceedings of Sixth International Congress on Information and Communication Technology_ , X.-S. Yang, S. Sherratt, N. Dey, and A. Joshi, Eds., 

763 19 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

ser. Lecture Notes in Networks and Systems, Singapore: Springer, 2022, pp. 239–247. 

- [264] K. Leartpantulak and Y. Kitjaidure, “Music genre classification of audio signals using particle swarm optimization and stacking ensemble,” in _2019 7th International Electrical Engineering Congress (iEECON)_ , Mar. 2019, pp. 1–4. 

- [265] C.-H. Lee, H.-S. Lin, and L.-H. Chen, “Music classification using the bag of words model of modulation spectral features,” in _2015 15th International Symposium on Communications and Information Technologies (ISCIT)_ , Oct. 2015, pp. 121–124. 

- [266] J. Lee, S. Shin, D. Jang, S.-J. Jang, and K. Yoon, “Music recommendation system based on usage history and automatic genre classification,” in _2015 IEEE International Conference on Consumer Electronics (ICCE)_ , Jan. 2015, pp. 134–135. 

- [267] J. Lee and J. Nam, “Multi-level and multi-scale feature aggregation using pretrained convolutional neural networks for music auto-tagging,” _IEEE Signal Processing Letters_ , vol. 24, no. 8, pp. 1208– 1212, Aug. 2017. 

- [268] S. Lee, J. Lee, and K. lee, “Content-based feature exploration for transparent music recommendation using self-attentive genre classification,” in _Proceedings of the Late-Breaking Results Track Part of the Twelfth ACM Conference on Recommender Systems (RecSys_ ’ _18)_ , arXiv, Sep. 3, 2018. arXiv: 1808.10600 [cs, eess]. 

- [269] J. Lee, K. Yoon, D. Jang, S.-J. Jang, S. Shin, and J.-H. Kim, “Music recommendation system based on genre distance and user preference classification.,” _Journal of Theoretical & Applied Information Technology_ , vol. 96, no. 5, 2018. 

- [270] J. Lee, M. Lee, D. Jang, and K. Yoon, “Korean traditional music genre classification using sample and MIDI phrases,” _KSII Transactions on Internet and Information Systems_ , vol. 12, no. 4, pp. 1869– 1886, 2018. 

- [271] J. Lee, J. Park, and J. Nam, “Representation Learning of Music Using Artist, Album, and Track Information,” presented at the Machine Learning for Music Discovery Workshop at ICML 2019, arXiv, Jun. 27, 2019. arXiv: 1906.11783 [cs, eess]. 

- [272] J. Lee, N. J. Bryan, J. Salamon, Z. Jin, and J. Nam, “Metric learning vs classification for disentangled music representation learning,” in _Proceedings of the 21st International Society for Music Information Retrieval Conference_ , Montreal, Canada: ISMIR, Oct. 11, 2020, pp. 439–445. 

- [273] A. Lefaivre and J. Z. Zhang, “Music genre classification: Genre-specific characterization and pairwise evaluation,” in _Proceedings of the Audio Mostly 2018 on Sound in Immersion and Emotion_ , ser. AM’18, New York, NY, USA: Association for Computing Machinery, Sep. 12, 2018, pp. 1–4. 

- [274] M. Leimeister, D. Gaertner, and C. Dittmar, “Rhythmic Classification of Electronic Dance Music,” presented at the Audio Engineering Society Conference: 53rd International Conference: Semantic Audio, Audio Engineering Society, Jan. 27, 2014. 

- [275] M. T. Leleuly and P. H. Gunawan, “Analysis of feature correlation for music genre classification,” in _2020 8th International Conference on Information and Communication Technology (ICoICT)_ , Jun. 2020, pp. 1–4. 

- [276] X. Li, “HouseX: A Fine-grained House Music Dataset and its Potential in the Music Industry,” presented at the Asia Pacific Signal and Information Processing Association Annual Summit and Conference (APSIPA ASC) 2022, Chiang Mai, Thailand: arXiv, Oct. 11, 2022. arXiv: 2207 . 11690 [cs, eess]. 

- [277] Y. Liang, Y. Zhou, T. Wan, and X. Shu, “Deep neural networks with depthwise separable convolution for music genre classification,” in _2019 IEEE 2nd International Conference on Information Communication and Signal Processing (ICICSP)_ , Sep. 2019, pp. 267–270. 

- [278] B. Liang and M. Gu, “Music genre classification using transfer learning,” in _2020 IEEE Conference on Multimedia Information Processing and Retrieval (MIPR)_ , Aug. 2020, pp. 392–393. 

- [279] C. Lin, W. Chen, C. Qiu, Y. Wu, S. Krishnan, and Q. Zou, “LibD3C: Ensemble classifiers with a clustering and dynamic selection strategy,” _Neurocomputing_ , Advances in Pattern Recognition Applications and Methods, vol. 123, pp. 424–435, Jan. 10, 2014. 

- [280] J. Liu, C. Wang, and L. Zha, “A middle-level learning feature interaction method with deep learning for multi-feature music genre classification,” _Electronics_ , vol. 10, no. 18, p. 2206, 18 Jan. 2021. 

- [281] C. Liu, L. Feng, G. Liu, H. Wang, and S. Liu, “Bottom-up broadcast neural network for music genre classification,” _Multimedia Tools and Applications_ , vol. 80, no. 5, pp. 7313–7331, Feb. 1, 2021. 

- [282] X. Liu, S. Song, M. Zhang, and Y. Huang, “MATT. A Multiple-instance Attention Mechanism for Long-tail Music Genre Classification,” in _2022 IEEE International Conference on Systems, Man, and Cybernetics (SMC)_ , Oct. 2022, pp. 782– 787. 

764 20 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

- [283] K. Liu, J. DeMori, and K. Abayomi. “Open set recognition for music genre classification.” arXiv: 2209.07548 [eess, math]. (Sep. 15, 2022), [Online]. Available: http : / / arxiv . org / abs / 2209 . 07548 (visited on 03/03/2023), preprint. 

- [284] Y.-L. Lo, C.-Y. Chiu, and T.-W. Chang, “Discovering Similar Music for Alpha Wave Music,” in _Mobile and Wireless Technologies 2017_ , K. J. Kim and N. Joukov, Eds., ser. Lecture Notes in Electrical Engineering, Singapore: Springer, 2018, pp. 571– 580. 

- [285] M. Long, L. Hu, and F. Jin, “Analysis of main characteristics of music genre based on PCA algorithm,” in _2021 IEEE 2nd International Conference on Big Data, Artificial Intelligence and Internet of Things Engineering (ICBAIE)_ , Mar. 2021, pp. 101–105. 

- [286] Y.-C. Lu, C.-W. Wu, C.-T. Lu, and A. Lerch, “An unsupervised approach to anomaly detection in music datasets,” in _Proceedings of the 39th International ACM SIGIR Conference on Research and Development in Information Retrieval_ , ser. SIGIR ’16, New York, NY, USA: Association for Computing Machinery, Jul. 7, 2016, pp. 749–752. 

- [287] Y.-C. Lu, C.-W. Wu, A. Lerch, and C.-T. Lu, “Automatic outlier detection in music genre datasets.,” in _Proceedings of the 17th International Society for Music Information Retrieval Conference_ , 2016, pp. 101–107. 

- [288] H. Lukashevich, “Confidence Measures in Automatic Music Classification,” in _Data Analysis, Machine Learning and Knowledge Discovery_ , M. Spiliopoulou, L. Schmidt-Thieme, and R. Janning, Eds., ser. Studies in Classification, Data Analysis, and Knowledge Organization, Cham: Springer International Publishing, 2014, pp. 397–405. 

- [289] A. Lykartsis, “Evaluation of accent-based rhythmic descriptors for genre classification of musical signals,” M.S. thesis, Technische Universität Berlin, Berlin, 2014. 

- [290] A. Lykartsis, C.-W. Wu, and A. Lerch, “Beat histogram features from NMF-based novelty functions for music classification.,” in _Proceedings of the 16th International Society for Music Information Retrieval Conference_ , Málaga, Spain: ISMIR, Oct. 2015, pp. 434–440. 

- [291] Z. Ma, “Comparison between machine learning models and neural networks on music genre classification,” in _2022 3rd International Conference on Computer Vision, Image and Deep Learning & International Conference on Computer Engineering and Applications (CVIDL & ICCEA)_ , May 2022, pp. 189–194. 

- [292] V. Macharla and P. Radha Krishna, “Music genre classification using neural networks with data augmentation,” _Journal of Innovation Sciences and Sustainable Technologies_ , vol. 1, no. 1, pp. 21–37, Jan. 12, 2021. 

- [293] P. Mandal, I. Nath, N. Gupta, M. K. Jha, D. G. Ganguly, and S. Pal, “Automatic music genre detection using artificial neural networks,” in _Intelligent Computing in Engineering_ , V. K. Solanki, M. K. Hoang, Z. ( Lu, and P. K. Pattnaik, Eds., ser. Advances in Intelligent Systems and Computing, Singapore: Springer, 2020, pp. 17–24. 

- [294] K. Markov and T. Matsui, “Music genre classification using gaussian process models,” in _2013 IEEE International Workshop on Machine Learning for Signal Processing (MLSP)_ , Sep. 2013, pp. 1–6. 

- [295] K. Markov and T. Matsui, “High level feature extraction for the self-taught learning algorithm,” _EURASIP Journal on Audio Speech and Music Processing_ , vol. 2013, no. 1, p. 6, Apr. 9, 2013. 

- [296] K. Markov and T. Matsui, “Music Genre and Emotion Recognition Using Gaussian Processes,” _IEEE Access_ , vol. 2, pp. 688–697, 2014. 

- [297] G. C. Marques, “Machine Learning Techniques for Music Information Retrieval,” Ph.D. dissertation, Universidade de Lisboa (Portugal), Portugal, 2014, 211 pp. 

- [298] L. Maršík, J. Pokorný, and M. Ilčík, “Improving Music Classification Using Harmonic Complexity,” in _Proceedings of the 14th Conference Information Technologies-Applications and Theory_ , Prague, 2014. 

- [299] J. Martel, T. Nakashika, C. Garcia, and K. Idrissi, “A Combination of Hand-Crafted and Hierarchical High-Level Learnt Feature Extraction for Music Genre Classification,” in _Artificial Neural Networks and Machine Learning_ – _ICANN 2013_ , V. Mladenov, P. Koprinkova-Hristova, G. Palm, A. E. P. Villa, B. Appollini, and N. Kasabov, Eds., ser. Lecture Notes in Computer Science, Berlin, Heidelberg: Springer, 2013, pp. 397–404. 

- [300] M. Matocha and S. K. Zieliński, “Music genre recognition using convolutional neural networks,” _Advances in Computer Science Research_ , vol. 14, pp. 125–142, 2018. 

- [301] M. Mauch, R. M. MacCallum, M. Levy, and A. M. Leroi, “The evolution of popular music: USA 1960–2010,” _Royal Society Open Science_ , vol. 2, no. 5, p. 150 081, May 2015. 

- [302] M. C. Mccallum, F. Korzeniowski, S. Oramas, F. Gouyon, and A. Ehmann, “Supervised and Unsupervised Learning of Audio Representations for Music Understanding,” in _Proceedings of the 23rd International Society for Music Information Retrieval Conference_ , Bengaluru, India: ISMIR, Dec. 4, 2022, pp. 256–263. 

765 21 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

- [303] C. McKay, J. Cumming, and I. Fujinaga, “JSYMBOLIC 2.2: Extracting Features from Symbolic Music for use in Musicological and MIR Research,” in _Proceedings of the 19th International Society for Music Information Retrieval Conference_ , Paris, France: ISMIR, Sep. 23, 2018, pp. 348–354. 

- [304] F. Medhat, D. Chesmore, and J. Robinson, “Music genre classification using masked conditional neural networks,” in _Neural Information Processing_ , D. Liu, S. Xie, Y. Li, D. Zhao, and E.-S. M. El-Alfy, Eds., ser. Lecture Notes in Computer Science, Cham: Springer International Publishing, 2017, pp. 470–481. 

- [305] F. Medhat, D. Chesmore, and J. Robinson, “Masked conditional neural networks for audio classification,” in _Artificial Neural Networks and Machine Learning_ – _ICANN 2017_ , A. Lintas, S. Rovetta, P. F. Verschure, and A. E. Villa, Eds., ser. Lecture Notes in Computer Science, Cham: Springer International Publishing, 2017, pp. 349– 358. 

- [306] F. Medhat, D. Chesmore, and J. Robinson, “Automatic classification of music genre using masked conditional neural networks,” in _2017 IEEE International Conference on Data Mining (ICDM)_ , Nov. 2017, pp. 979–984. 

- [307] J. Mehta, D. Gandhi, G. Thakur, and P. Kanani, “Music genre classification using transfer learning on log-based MEL spectrogram,” in _2021 5th International Conference on Computing Methodologies and Communication (ICCMC)_ , Apr. 2021, pp. 1101–1107. 

- [308] J. Mendes, “Deep learning techniques for music genre classification and building a music recommendation system,” M.S. thesis, Dublin, National College of Ireland, 2020, 22 pp. 

- [309] R. Mignot and G. Peeters, “An Analysis of the Effect of Data Augmentation Methods: Experiments for a Musical Genre Classification Task,” _Transactions of the International Society for Music Information Retrieval_ , vol. 2, no. 1, pp. 97–110, Dec. 18, 2019. 

- [310] J. Mitra and D. Saha. “An Efficient Feature Selection in Classification of Audio Files.” arXiv: 1404 . 1491 [cs]. (Mar. 24, 2014), [Online]. Available: http://arxiv.org/abs/1404. 1491 (visited on 02/19/2024), preprint. 

- [311] K. S. Mounika, S. Deyaradevi, K. Swetha, and V. Vanitha, “Music genre classification using deep learning,” in _2021 International Conference on Advancements in Electrical, Electronics, Communication, Computing and Automation (ICAECA)_ , Oct. 2021, pp. 1–7. 

- [312] S. F. Mughal, S. Aamir, S. A. Sahto, and A. Samad, “Urdu music genre classification using convolution neural networks,” in _2022 International Conference on Emerging Trends in Smart Technologies (ICETST)_ , Sep. 2022, pp. 1–6. 

- [313] G. Mujtaba, S. Kim, E. Park, S. Kim, J. Ryu, and E.-S. Ryu, “Client-driven animated keyframe generation system using music analysis,” in _Proceedings of the Korean Society of Broadcast Engineers Conference_ , The Korean Institute of Broadcast and Media Engineers, 2019, pp. 173–175. 

- [314] S. Muñoz-Romero, J. A. García, and V. GómezVerdejo, “Nonnegative OPLS for Supervised Design of Filter Banks: Application to Image and Audio Feature Extraction,” _IEEE Transactions on Multimedia_ , vol. 20, no. 7, pp. 1751–1766, Jul. 2018. arXiv: 2112.12280 [cs, eess]. 

- [315] B. Murauer and G. Specht, “Detecting music genre using extreme gradient boosting,” in _Companion Proceedings of the The Web Conference 2018_ , ser. WWW ’18, Republic and Canton of Geneva, CHE: International World Wide Web Conferences Steering Committee, Apr. 23, 2018, pp. 1923– 1927. 

- [316] F. Nahar, K. Agres, B. BT, and D. Herremans, “A dataset and classification model for Malay, Hindi, Tamil and Chinese music,” in _Proceedings of the 13th International Workshop on Machine Learning and Music at ECML-PKDD 2020_ , arXiv, Sep. 15, 2020. arXiv: 2009.04459 [cs, eess]. 

- [317] T. Nakai, N. Koide-Majima, and S. Nishimoto, “Encoding and decoding of music-genre representations in the human brain,” in _2018 IEEE International Conference on Systems, Man, and Cybernetics (SMC)_ , Oct. 2018, pp. 584–589. 

- [318] H. Nakamura, H.-H. Huang, and K. Kawagoe, “Detecting Musical Genre Borders for Multi-label Genre Classification,” in _2013 IEEE International Symposium on Multimedia_ , Dec. 2013, pp. 532– 533. 

- [319] L. Nanni, Y. Costa, and S. Brahnam, “Set of texture descriptors for music genre classification,” presented at the 22nd International Conference in Central Europeon Computer Graphics, Visualization and Computer Vision, Václav Skala - UNION Agency, 2014, pp. 145–152. 

- [320] L. Nanni, Y. M. G. Costa, A. Lumini, M. Y. Kim, and S. R. Baek, “Combining visual and acoustic features for music genre classification,” _Expert Systems with Applications_ , vol. 45, pp. 108–117, Mar. 1, 2016. 

- [321] L. Nanni, Y. M. G. Costa, D. R. Lucio, C. N. Silla, and S. Brahnam, “Combining visual and acoustic features for audio classification tasks,” _Pattern Recognition Letters_ , vol. 88, pp. 49–56, Mar. 1, 2017. 

766 22 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

- [322] L. Nanni, Y. M. G. Costa, R. L. Aguiar, C. N. Silla, and S. Brahnam, “Ensemble of deep learning, visual and acoustic features for music genre classification,” _Journal of New Music Research_ , vol. 47, no. 4, pp. 383–397, Aug. 8, 2018. 

- [323] N. Narkhede, S. Mathur, and A. Bhaskar, “Machine learning techniques for music genre classification,” in _Information and Communication Technology for Competitive Strategies (ICTCS 2020)_ , A. Joshi, M. Mahmud, R. G. Ragel, and N. V. Thakur, Eds., ser. Lecture Notes in Networks and Systems, Singapore: Springer, 2022, pp. 155–161. 

- [324] N. Narkhede, S. Mathur, and A. Bhaskar, “Automatic classification of music genre using SVM,” in _Computer Networks and Inventive Communication Technologies_ , S. Smys, R. Bestak, R. Palanisamy, and I. Kotuliak, Eds., ser. Lecture Notes on Data Engineering and Communications Technologies, Singapore: Springer, 2022, pp. 439–449. 

- [325] A. Nasridinov and Y.-H. Park, “A Study on Music Genre Recognition and Classification Techniques,” _International Journal of Multimedia and Ubiquitous Engineering_ , vol. 9, no. 4, pp. 31–42, Apr. 30, 2014. 

- [326] N. Ndou, R. Ajoodha, and A. Jadhav, “Music genre classification: A review of deep-learning and traditional machine-learning approaches,” in _2021 IEEE International IOT, Electronics and Mechatronics Conference (IEMTRONICS)_ , Apr. 2021, pp. 1–6. 

- [327] W. W. Y. Ng, W. Zeng, and T. Wang, “Multi-level local feature coding fusion for music genre recognition,” _IEEE Access_ , vol. 8, pp. 152 713–152 727, 2020. 

- [328] Q. H. Nguyen _et al._ , “Music genre classification using residual attention network,” in _2019 International Conference on System Science and Engineering (ICSSE)_ , Jul. 2019, pp. 115–119. 

- [329] K. Nie, “Inaccurate Prediction or Genre Evolution? Rethinking Genre Classification,” in _Proceedings of the 23rd International Society for Music Information Retrieval Conference_ , Bengaluru, India: ISMIR, Dec. 4, 2022, pp. 329–336. 

- [330] M. R. Nirmal and S. Mohan B S, “Music genre classification using spectrograms,” in _2020 International Conference on Power, Instrumentation, Control and Computing (PICC)_ , Dec. 2020, pp. 1– 5. 

- [331] T. Nkambule and R. Ajoodha, “Classification of music by genre using probabilistic models and deep learning models,” in _Proceedings of Sixth International Congress on Information and Communication Technology_ , X.-S. Yang, S. Sherratt, N. Dey, and A. Joshi, Eds., ser. Lecture Notes in Networks and Systems, Singapore: Springer, 2022, pp. 185– 193. 

- [332] S. Ntalampiras, “Directed acyclic graphs for content based sound, musical genre, and speech emotion classification,” _Journal of New Music Research_ , vol. 43, no. 2, pp. 173–182, Apr. 3, 2014. 

- [333] C. J. O’Brien, “Supervised feature learning via sparse coding for music information rerieval,” M.S. thesis, Georgia Tech, Apr. 24, 2015. 

- [334] S. Oramas, L. Espinosa-Anke, A. Lawlor, X. Serra, and H. Saggion, “Exploring customer reviews for music genre classification and evolutionary studies,” in _Proceedings of the 17th International Society for Music Information Retrieval Conference_ , 2016, pp. 150–156. 

- [335] S. Oramas, O. Nieto, F. Barbieri, and X. Serra, “Multi-label music genre classification from audio, text, and images using deep features,” in _Proceedings of the 18th International Society for Music Information Retrieval Conference_ , Suzhou, China: ISMIR, Jul. 16, 2017, pp. 23–30. arXiv: 1707. 04916 [cs]. 

- [336] S. Oramas, “Knowledge extraction and representation learning for music recommendation and classification,” Ph.D. dissertation, Universitat Pompeu Fabra, Barcelona, Spain, Nov. 14, 2017. 

- [337] S. Oramas, F. Barbieri, O. Nieto, and X. Serra, “Multimodal Deep Learning for Music Genre Classification,” _Transactions of the International Society for Music Information Retrieval_ , vol. 1, no. 1, pp. 4–21, 1 Sep. 4, 2018. 

- [338] R. Ozakar and E. Gedikli, “Music genre classificatio using novel song structure derived features,” in _2020 5th International Conference on Computer Science and Engineering (UBMK)_ , Sep. 2020, pp. 117–120. 

- [339] T. Özseven and B. E. Özseven, “A content analysis of the research approaches in music genre recognition,” in _2022 International Congress on HumanComputer Interaction, Optimization and Robotic Applications (HORA)_ , Jun. 2022, pp. 1–13. 

- [340] H. Pálmason, B. Þ. Jónsson, L. Amsaleg, M. Schedl, and P. Knees, “On competitiveness of nearest-neighbor-based music classification: A methodological critique,” in _Similarity Search and Applications_ , C. Beecks, F. Borutta, P. Kröger, and T. Seidl, Eds., ser. Lecture Notes in Computer Science, Cham: Springer International Publishing, 2017, pp. 275–283. 

- [341] H. Pálmason, B. Þ. Jónsson, M. Schedl, and P. Knees, “Music genre classification revisited: An in-depth examination guided by music experts,” in _Proceedings of the International Symposium on Computer Music Multidisciplinary Research_ , M. Aramaki, M. E. P. Davies, R. Kronland-Martinet, and S. Ystad, Eds., ser. Lecture Notes in Computer Science, Cham: Springer International Publishing, 2018, pp. 49–62. 

767 23 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

- [342] Y. Panagakis and C. Kotropoulos, “Music classification by low-rank semantic mappings,” _EURASIP Journal on Audio, Speech, and Music Processing_ , vol. 2013, no. 1, p. 13, Jun. 24, 2013. 

- [343] Y. Panagakis, C. L. Kotropoulos, and G. R. Arce, “Music genre classification via joint sparse lowrank representation of audio features,” _IEEE/ACM Transactions on Audio Speech and Language Processing_ , vol. 22, no. 12, pp. 1905–1917, Dec. 2014. 

- [344] M. M. Panchwagh and V. D. Katkar, “Music genre classification using data mining algorithm,” in _2016 Conference on Advances in Signal Processing (CASP)_ , Jun. 2016, pp. 49–53. 

- [345] A. Pandey and I. Dutta, “Bundeli Folk-Song Genre Classification with kNN and SVM,” in _Proceedings of the 11th International Conference on Natural Language Processing_ , Goa, India, 2014, pp. 133–138. 

- [346] Y. R. Pandeya, J. You, B. Bhattarai, and J. Lee, “Multi-modal, multi-task and multi-label for music genre classification and emotion regression,” in _2021 International Conference on Information and Communication Technology Convergence (ICTC)_ , Oct. 2021, pp. 1042–1045. 

- [347] S. Panwar, A. Das, M. Roopaei, and P. Rad, “A deep learning approach for mapping music genres,” in _2017 12th System of Systems Engineering Conference (SoSE)_ , Jun. 2017, pp. 1–5. 

- [348] C. Papaioannou, I. Valiantzas, T. Giannakopoulos, M. Kaliakatsos-Papakostas, and A. Potamianos, “A Dataset for Greek Traditional and Folk Music: Lyra,” in _Proceedings of the 23rd International Society for Music Information Retrieval Conference_ , Bengaluru, India: ISMIR, Dec. 4, 2022, pp. 377– 383. 

- [349] J. Park, J. Lee, J. Park, J.-W. Ha, and J. Nam, “Representation learning of music using artist labels,” in _Proceedings of the 19th International Society for Music Information Retrieval Conference_ , ISMIR, 2018, pp. 717–724. 

- [350] S. Park, I. Kim, and K. Ahn, “A stochastic process for music: The example of K-pop music,” _Journal of Physics Conference Series_ , vol. 2287, no. 1, p. 012 010, Jun. 2022. 

- [351] A. R. S. Parmezan, D. F. Silva, and G. E. Batista, “A combination of local approaches for hierarchical music genre classification.,” in _Proceedings of the 21st International Society for Music Information Retrieval Conference_ , Montreal, Canada: ISMIR, 2020, pp. 740–747. 

- [352] N. M. Patil and M. U. Nemade, “Music genre classification using MFCC, K-NN and SVM classifier,” _International Journal of Computer Engineering in Research Trends_ , vol. 4, no. 2, pp. 43–47, 2017. 

- [353] V. Pavan and R. Dhanalakshmi, “Analysis of Audio Data and Prediction of the Genre using Novel Random Forest and Decision Tree,” in _2022 4th International Conference on Inventive Research in Computing Applications (ICIRCA)_ , Sep. 2022, pp. 1773–1777. 

- [354] G. Peeters, “Rhythm classification using spectral rhythm patterns,” in _Proceedings of the 6th International Conference on Music Information Retrieval_ , 2005, pp. 644–647. 

- [355] I. A. Pegoraro Santana _et al._ , “Music4all: A new music database and its applications,” in _2020 International Conference on Systems, Signals and Image Processing (IWSSIP)_ , Jul. 2020, pp. 399–404. 

- [356] R. Peiris and L. Jayaratne, “Supervised learning approach for classification of Sri Lankan music based on music structure similarity,” in _Proceedings of Ninth Annual International Conference on Computer Games, Multimedia and Allied Technology CGAT 2016), Singapore_ , 2016, pp. 84–90. 

- [357] R. Peiris and L. Jayaratne, “Musical genre classification of recorded songs based on music structure similarity,” _European Journal of Computer Science and Information Technology_ , vol. 4, no. 5, pp. 70–88, 2016. 

- [358] N. Pelchat and C. M. Gelowitz, “Neural network music genre classification,” _Canadian Journal of Electrical and Computer Engineering_ , vol. 43, no. 3, pp. 170–173, 2020. 

- [359] R. M. Pereira and C. N. Silla, “Using simplified chords sequences to classify songs genres,” in _2017 IEEE International Conference on Multimedia and Expo (ICME)_ , Jul. 2017, pp. 1446–1451. 

- [360] R. M. Pereira, Y. M. G. Costa, R. L. Aguiar, A. S. Britto, L. E. S. Oliveira, and C. N. Silla, “Representation learning vs. Handcrafted features for music genre classification,” in _2019 International Joint Conference on Neural Networks (IJCNN)_ , Jul. 2019, pp. 1–8. 

- [361] L. V. d. A. S. Pereira and T. F. Tavares, “An interplay between genre and emotion prediction in music: A study in the Emotify dataset,” in _Anais Do Simpósio Brasileiro de Computação Musical (SBCM)_ , SBC, Oct. 24, 2021, pp. 25–29. 

- [362] H. C. Piccoli, C. N. Silla, P. J. P. de Léon, and A. Pertusa, “An evaluation of symbolic feature sets and their combination for music genre classification,” in _2013 IEEE International Conference on Systems, Man, and Cybernetics (SMC)_ , Oct. 2013, pp. 1901–1905. 

- [363] M. H. Pimenta-Zanon, G. M. Bressan, and F. M. Lopes. “Complex Network-Based Approach for Feature Extraction and Classification of Musical Genres.” arXiv: 2110 . 04654 [cs, eess]. (Oct. 9, 2021), [Online]. Available: http : / / 

768 24 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

arxiv.org/abs/2110.04654 (visited on 03/24/2023), preprint. 

- [364] J. Pons and X. Serra, “Randomly Weighted CNNs for (Music) Audio Classification,” in _2019 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)_ , Brighton, United Kingdom: IEEE, May 2019, pp. 336–340. 

- [365] R. Popovici and R. Andonie, “Music genre classification with self-organizing maps and edit distance,” in _2015 International Joint Conference on Neural Networks (IJCNN)_ , Jul. 2015, pp. 1–7. 

- [366] S. Poria, A. Gelbukh, A. Hussain, S. Bandyopadhyay, and N. Howard, “Music Genre Classification: A Semi-supervised Approach,” in _Pattern Recognition_ , J. A. Carrasco-Ochoa, J. F. MartínezTrinidad, J. S. Rodríguez, and G. S. di Baja, Eds., ser. Lecture Notes in Computer Science, Berlin, Heidelberg: Springer, 2013, pp. 254–263. 

- [367] A. Porter, D. Bogdanov, and X. Serra, “Mining metadata from the web for AcousticBrainz,” in _Proceedings of the 3rd International Workshop on Digital Libraries for Musicology_ , ser. DLfM 2016, New York, NY, USA: Association for Computing Machinery, Aug. 12, 2016, pp. 53–56. 

- [368] N. Prabhu, A. Asnodkar, and R. Kenkre, “Music Genre Classification using Improved Artificial Neural Network with Fixed Size Momentum,” _International Journal of Computer Applications_ , vol. 101, no. 14, pp. 25–30, Sep. 18, 2014. 

- [369] N. Prabhu, A. Asnodkar, and R. Kenkre, “Multiclass Suport Class Support Vector Machine for Music Genre Classification,” _International Journal of Computer Applications_ , vol. 107, no. 19, pp. 15– 17, Dec. 18, 2014. 

- [370] N. R. Prabhu, J. Andro-Vasko, D. Bein, and W. Bein, “Music genre classification using data mining and machine learning,” in _Information Technology - New Generations_ , S. Latifi, Ed., ser. Advances in Intelligent Systems and Computing, Cham: Springer International Publishing, 2018, pp. 397–403. 

- [371] R. Prajwal, S. Sharma, P. Naik, and S. Mk, “Music genre classification using machine learning,” _International Research Journal of Modernization in Engineering Technology and Science_ , vol. 3, no. 7, pp. 953–957, 2021. 

- [372] P. R. M. Prasetyaa and G. A. V. M. Giria, “Comparison of use of music content (tempo) and user context (mood) features on classification of music genre,” _JELIKU (Jurnal Elektronik Ilmu Komputer Udayana)_ , vol. 2301, p. 5373, 2019. 

- [373] V. Prashanthi, S. Kanakala, V. Akila, and A. Harshavardhan, “Music genre categorization using machine learning algorithms,” in _2021 International Conference on Computational Intelligence and Computing Applications (ICCICA)_ , Nov. 2021, pp. 1–4. 

- [374] F. Prezja, “Developing and testing sub-band spectral features in music genre and music mood machine learning,” M.S. thesis, University of Jyväskylä, Finland, 2018. 

- [375] M. Prockup, A. F. Ehmann, F. Gouyon, E. M. Schmidt, Ò. Celma, and Y. E. Kim, “Modeling Genre with the Music Genome Project: Comparing Human-Labeled Attributes and Audio Features.,” in _Proceedings of the 16th International Society for Music Information Retrieval Conference_ , Málaga, Spain: ISMIR, Oct. 26, 2015, pp. 31–37. 

- [376] L. K. Puppala, S. S. R. Muvva, S. R. Chinige, and P. Rajendran, “A novel music genre classification using convolutional neural network,” in _2021 6th International Conference on Communication and Electronics Systems (ICCES)_ , Jul. 2021, pp. 1246– 1249. 

- [377] N. Purnama, “Music genre recommendations based on spectrogram analysis using convolutional neural network algorithm with RESNET-50 and VGG-16 architecture,” _JISA(Jurnal Informatika dan Sains)_ , vol. 5, no. 1, pp. 69–74, 1 Jun. 20, 2022. 

- [378] Z. Qi, M. Rahouti, M. A. Jasim, and N. Siasi, “Music genre classification and feature comparison using ML,” in _2022 7th International Conference on Machine Learning Technologies (ICMLT)_ , ser. ICMLT 2022, New York, NY, USA: Association for Computing Machinery, Jun. 10, 2022, pp. 42–50. 

- [379] Z. Qin, W. Liu, and T. Wan, “A Bag-of-Tones Model with MFCC Features for Musical Genre Classification,” in _Advanced Data Mining and Applications_ , H. Motoda, Z. Wu, L. Cao, O. Zaiane, M. Yao, and W. Wang, Eds., ser. Lecture Notes in Computer Science, Berlin, Heidelberg: Springer, 2013, pp. 564–575. 

- [380] C. Qin, H. Yang, W. Liu, S. Ding, and Y. Geng, “Music genre trend prediction based on spatialtemporal music influence and euclidean similarity,” in _2021 36th Youth Academic Annual Conference of Chinese Association of Automation (YAC)_ , May 2021, pp. 406–411. 

- [381] L. Qiu, S. Li, and Y. Sung, “3D-DCDAE: Unsupervised music latent representations learning method based on a deep 3D convolutional denoising autoencoder for music genre classification,” _Mathematics_ , vol. 9, no. 18, p. 2274, 18 Jan. 2021. 

769 25 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

- [382] L. Qiu, S. Li, and Y. Sung, “DBTMPE: Deep bidirectional transformers-based masked predictive encoder approach for music genre classification,” _Mathematics_ , vol. 9, no. 5, p. 530, 5 Jan. 2021. 

- [383] R. J. M. Quinto, R. O. Atienza, and N. M. C. Tiglao, “Jazz music sub-genre classification using deep learning,” in _TENCON 2017 - 2017 IEEE Region 10 Conference_ , Nov. 2017, pp. 3111–3116. 

- [384] S. A. Raczyński and E. Vincent, “Genre-based music language modeling with latent hierarchical pitman-yor process allocation,” _IEEE/ACM Transactions on Audio Speech and Language Processing_ , vol. 22, no. 3, pp. 672–681, Mar. 2014. 

- [385] Q. G. Rafi, M. Noman, S. Z. Prodhan, S. Alam, and D. Nandi, “Comparative analysis of three improved deep learning architectures for music genre classification,” _International Journal of Information Technology and Computer Science_ , vol. 13, no. 2, pp. 1–14, 2021. 

- [386] T. Raissi, A. Tibo, and P. Bientinesi, “Extended pipeline for content-based feature engineering in music genre recognition,” in _2018 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)_ , Apr. 2018, pp. 2661–2665. 

- [387] H. Raj, A. K. Dubey, V. Deep, and Anuranjana, “Music genre classification using machine learning,” in _Advances in Interdisciplinary Engineering_ , N. Kumar, S. Tibor, R. Sindhwani, J. Lee, and P. Srivastava, Eds., ser. Lecture Notes in Mechanical Engineering, Singapore: Springer, 2021, pp. 763– 774. 

- [388] R. Rajan and H. A. Murthy, “Music genre classification by fusion of modified group delay and melodic features,” in _2017 Twenty-third National Conference on Communications (NCC)_ , Mar. 2017, pp. 1–6. 

- [389] A. R. Rajanna, K. Aryafar, A. Shokoufandeh, and R. Ptucha, “Deep neural networks: A case study for music genre classification,” in _2015 IEEE 14th International Conference on Machine Learning and Applications (ICMLA)_ , Dec. 2015, pp. 655–660. 

- [390] B. Rajesh and D. G. Bhalke, “Automatic genre classification of Indian Tamil and western music using fractional MFCC,” _International Journal of Speech Technology_ , vol. 19, no. 3, pp. 551–563, Sep. 1, 2016. 

- [391] A. Ramanathan, P. Srivastava, and R. Jeya, “Machine learning in music genre classification,” _Turkish Online Journal of Qualitative Inquiry_ , vol. 12, no. 3, pp. 2494–2510, 3 Jul. 1, 2021. 

- [392] P. Rameshkumar, M. Monisha, B. Santhi, and T. Vigneshwaran, “Robust feature selection method for music classification,” in _2014 International Conference on Computer Communication and Informatics_ , Jan. 2014, pp. 1–6. 

- [393] J. Ramírez and M. J. Flores, “Machine learning for music genre: Multifaceted review and experimentation with audioset,” _Journal of Intelligent Information Systems_ , vol. 55, no. 3, pp. 469–499, Dec. 1, 2020. 

- [394] F. Raposo, R. Ribeiro, and D. M. de Matos, “On the Application of Generic Summarization Algorithms to Music,” _IEEE Signal Processing Letters_ , vol. 22, no. 1, pp. 26–30, Jan. 2015. 

- [395] F. Raposo, R. Ribeiro, and D. Martins de Matos, “Using Generic Summarization to Improve Music Information Retrieval Tasks,” _IEEE/ACM Transactions on Audio Speech and Language Processing_ , vol. 24, no. 6, pp. 1119–1128, Jun. 2016. 

- [396] M. Raval, P. Dave, and R. Dattani, “Music genre classification using neural networks.,” _International Journal of Advanced Research in Computer Science_ , vol. 12, no. 5, 2021. 

- [397] T. Ren, F. Wang, and H. Wang, “A sequential naive bayes method for music genre classification based on transitional information from pitch and beat,” _Statistics and Its Interface_ , vol. 13, no. 3, pp. 361– 371, 2020. 

- [398] S. S. Renteria Aguilar, L. Llano, and J. CantúOrtiz, “Data-driven techniques for music genre recognition,” in _Computer Science & Information Technology_ , D. C. Wyld and D. Nagamalai, Eds., Academy and Industry Research Collaboration Center (AIRCC), Jul. 11, 2020. 

- [399] F. Rodrigues, F. Pereira, and B. Ribeiro, “Learning from multiple annotators: Distinguishing good from random labelers,” _Pattern Recognition Letters_ , vol. 34, no. 12, pp. 1428–1436, Sep. 1, 2013. 

- [400] F. Rodríguez-Algarra, B. L. Sturm, and H. MaruriAguilar, “Analysing scattering-based music content analysis systems: Where’s the music?” In _Proceedings of the 17th International Society for Music Information Retrieval Conference_ , ISMIR, 2016, pp. 344–350. 

- [401] F. Rodríguez-Algarra, B. L. Sturm, and S. Dixon, “Characterising confounding effects in music classification experiments through interventions,” _Transactions of the International Society for Music Information Retrieval_ , vol. 2, no. 1, pp. 52–66, 2019. 

- [402] L. Rompré, I. Biskri, and J.-G. Meunier, “Using association rules mining for retrieving genre-specific music files,” in _The Thirtieth International Flairs Conference_ , 2017. 

- [403] A. Rosner, M. Michalak, and B. Kostek, “A study on influence of normalization methods on music genre classification results employing kNN algorithms,” _Studia Informatica Pomerania_ , vol. 34, pp. 411–423, 2013. 

770 26 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

- [404] A. Rosner, F. Weninger, B. Schuller, M. Michalak, and B. Kostek, “Influence of low-level features extracted from rhythmic and harmonic sections on music genre classification,” in _Man-Machine Interactions 3_ , D. A. Gruca, T. Czachórski, and S. Kozielski, Eds., ser. Advances in Intelligent Systems and Computing, Cham: Springer International Publishing, 2014, pp. 467–473. 

- [405] A. Rosner, B. Schuller, and B. Kostek, “Classification of music genres based on music separation into harmonic and drum components,” _Archives of Acoustics_ , vol. 39, no. 4, pp. 629–638, 4 Dec. 8, 2014. 

- [406] A. Rosner and B. Kostek, “Musical instrument separation applied to music genre classification,” in _Foundations of Intelligent Systems_ , F. Esposito, O. Pivert, M.-S. Hacid, Z. W. Rás, and S. Ferilli, Eds., ser. Lecture Notes in Computer Science, Cham: Springer International Publishing, 2015, pp. 420– 430. 

- [407] A. Rosner and B. Kostek, “Automatic music genre classification based on musical instrument track separation,” _Journal of Intelligent Information Systems_ , vol. 50, no. 2, pp. 363–384, Apr. 1, 2018. 

- [408] S. Saju, R. Rajan, and A. R. Jayan, “Music genre classification using spatan 6 FPGA and TMS320C6713 DSK,” in _2017 International Conference on Signal Processing and Communication (ICSPC)_ , Jul. 2017, pp. 196–200. 

- [409] A. E. Coca Salazar, “Hierarchical mining with complex networks for music genre classification,” _Digital Signal Processing_ , vol. 127, p. 103 559, Jul. 1, 2022. 

- [410] A. Saravanou, F. Tomasi, R. Mehrotra, and M. Lalmas, “Multi-Task Learning of Graph-based Inductive Representations of Music Content,” in _Proceedings of the 22nd International Society for Music Information Retrieval Conference_ , Online: ISMIR, Nov. 7, 2021, pp. 602–609. 

- [411] R. Sarkar and S. K. Saha, “Music genre classification using EMD and pitch based feature,” in _2015 Eighth International Conference on Advances in Pattern Recognition (ICAPR)_ , Jan. 2015, pp. 1–6. 

- [412] R. Sarkar, N. Biswas, and S. Chakraborty, “Music genre classification using frequency domain features,” in _2018 Fifth International Conference on Emerging Applications of Information Technology (EAIT)_ , Jan. 2018, pp. 1–4. 

- [413] M. Sathyamurthy, X. Dong, and M. P. Kumar, “Geometric deep learning for music genre classification,” in _Proceedings of the 13th International Workshop on Machine Learning and Music_ , 2020, pp. 28–31. 

- [414] C. Savard, E. H. Bugbee, M. R. McGuirl, and K. M. Kinnaird, “SuPP & MaPP: Adaptable structurebased representations for MIR tasks,” in _Proceedings of the 21st International Society for Music Information Retrieval Conference_ , Montreal, Canada: ISMIR, Oct. 11, 2020, pp. 335–342. 

- [415] Y. Sazaki and A. Aramadhan, “Rock Genre Classification using K-Nearest Neighbor,” in _Proceeding of The 1st International Conference on Computer Science and Engineering_ , 2014, pp. 81–83. 

- [416] S. Scardapane, D. Comminiello, M. Scarpiniti, and A. Uncini, “Music classification using extreme learning machines,” in _2013 8th International Symposium on Image and Signal Processing and Analysis (ISPA)_ , Sep. 2013, pp. 377–381. 

- [417] S. Scardapane, R. Fierimonte, D. Wang, M. Panella, and A. Uncini, “Distributed music classification using Random Vector Functional-Link nets,” in _2015 International Joint Conference on Neural Networks (IJCNN)_ , Jul. 2015, pp. 1–8. 

- [418] M. Scarpiniti, S. Scardapane, D. Comminiello, and A. Uncini, “Music genre classification using stacked auto-encoders,” in _Neural Approaches to Dynamics of Signal Exchanges_ , ser. Smart Innovation, Systems and Technologies, A. Esposito, M. Faundez-Zanuy, F. C. Morabito, and E. Pasero, Eds., Singapore: Springer, 2020, pp. 11–19. 

- [419] M. Schedl and C. Bauer, “Online music listening culture of kids and adolescents: Listening analysis and music recommendation tailored to the young,” in _RecSys ’17: Proceedings of the Eleventh ACM Conference on Recommender Systems_ , arXiv, Dec. 24, 2019, pp. 376–377. arXiv: 1912.11564 [cs]. 

- [420] A. Schindler and A. Rauber, “An audio-visual approach to music genre classification through affective color features,” in _Advances in Information Retrieval_ , A. Hanbury, G. Kazai, A. Rauber, and N. Fuhr, Eds., ser. Lecture Notes in Computer Science, Cham: Springer International Publishing, 2015, pp. 61–67. 

- [421] A. Schindler and A. Rauber, “Harnessing musicrelated visual stereotypes for music information retrieval,” _ACM Transactions on Intelligent Systems and Technology_ , vol. 8, no. 2, 20:1–20:21, Oct. 25, 2016. 

- [422] A. Schindler, T. Lidy, and A. Rauber, “Comparing shallow versus deep neural network architectures for automatic music genre classification.,” in _Forum Media Technology_ , 2016, pp. 17–21. 

- [423] D. Schnitzer, A. Flexer, M. Schedl, and G. Widmer, “Local and Global Scaling Reduce Hubs in Space,” _Journal of Machine Learning Research_ , vol. 13, no. 92, pp. 2871–2902, 2012. 

771 27 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

- [424] H. Schreiber, “Improving genre annotations for the million song dataset.,” in _Proceedings of the 16th International Society for Music Information Retrieval Conference_ , Málaga, Spain, 2015, pp. 241– 247. 

- [425] H. Schreiber, “Genre Ontology Learning: Comparing Curated with Crowd-Sourced Ontologies.,” in _Proceedings of the 17th International Society for Music Information Retrieval Conference_ , New York City, United States: ISMIR, Aug. 7, 2016, pp. 400–406. 

- [426] B. Schuller, F. Eyben, and G. Rigoll, “Tango or waltz?: Putting ballroom dance style into tempo detection,” _EURASIP Journal on Audio Speech and Music Processing_ , vol. 2008, no. 1, pp. 1–12, 1 Dec. 2008. 

- [427] A. Sen, “Automatic Music Clustering using Audio Attributes,” _International Journal of Computer Science Engineering_ , vol. 3, no. 6, pp. 307–312, 2014. 

- [428] C. Senac, T. Pellegrini, F. Mouret, and J. Pinquier, “Music feature maps with convolutional neural networks for music genre classification,” in _Proceedings of the 15th International Workshop on Content-Based Multimedia Indexing_ , ser. CBMI ’17, New York, NY, USA: Association for Computing Machinery, Jun. 19, 2017, pp. 1–5. 

- [429] M. Sen Sarma and A. Das, “BMGC: A deep learning approach to classify bengali music genres,” in _Proceedings of the 4th International Conference on Networking, Information Systems & Security_ , ser. NISS2021, New York, NY, USA: Association for Computing Machinery, Nov. 26, 2021, pp. 1–6. 

- [430] J. S. Seo, “A Musical Genre Classification Method Based on the Octave-Band Order Statistics,” _The Journal of the Acoustical Society of Korea_ , vol. 33, no. 1, pp. 81–86, 2014. 

- [431] M. Serwach and B. Stasiak, “GA-based parameterization and feature selection for automatic music genre recognition,” in _2016 17th International Conference Computational Problems of Electrical Engineering (CPEE)_ , Sep. 2016, pp. 1–5. 

- [432] D. R. I. M. Setiadi _et al._ , “Comparison of SVM, KNN, and NB classifier for genre music classification based on metadata,” in _2020 International Seminar on Application for Technology of Information and Communication (iSemantic)_ , Sep. 2020, pp. 12–16. 

- [433] D. R. I. M. Setiadi _et al._ , “Effect of feature selection on the accuracy of music genre classification using SVM classifier,” in _2020 International Seminar on Application for Technology of Information and Communication (iSemantic)_ , Sep. 2020, pp. 7– 11. 

- [434] K. Seyerlehner, M. Schedl, R. Sonnleitner, D. Hauger, and B. Ionescu, “From Improved AutoTaggers to Improved Music Similarity Measures,” in _Adaptive Multimedia Retrieval: Semantics, Context, and Adaptation_ , A. Nürnberger, S. Stober, B. Larsen, and M. Detyniecki, Eds., ser. Lecture Notes in Computer Science, Cham: Springer International Publishing, 2014, pp. 193–202. 

- [435] D. Shah, C. Sachdev, and B. Shah, “Classification of music genre using neural networks with cross-entropy optimization and soft-max output,” _International Journal of Computer Applications_ , vol. 119, no. 12, 2015. 

- [436] M. Shah, N. Pujara, K. Mangaroliya, L. Gohil, T. Vyas, and S. Degadwala, “Music genre classification using deep learning,” in _2022 6th International Conference on Computing Methodologies and Communication (ICCMC)_ , Mar. 2022, pp. 974–978. 

- [437] T. Shaikh and A. Jadhav, “Music genre classification using neural network,” in _ITM Web of Conferences_ , vol. 44, EDP Sciences, 2022, p. 03 016. 

- [438] A. Shakya, B. Gurung, M. S. Thapa, M. Rai, and B. Joshi, “Music classification based on genre and mood,” in _Computational Intelligence, Communications, and Business Analytics_ , J. K. Mandal, P. Dutta, and S. Mukhopadhyay, Eds., ser. Communications in Computer and Information Science, Singapore: Springer, 2017, pp. 168–183. 

- [439] S. Sharma, P. Fulzele, and I. Sreedevi, “Novel hybrid model for music genre classification based on support vector machine,” in _2018 IEEE Symposium on Computer Applications & Industrial Electronics (ISCAIE)_ , Apr. 2018, pp. 395–400. 

- [440] H. L. Shashirekha, “Using MFCC Features for the Classification of Monophonic Music,” in _International Conference on Information and Communication Technologies (ICICT- 2014)_ , 2014, pp. 5–9. 

- [441] M. Sheikh Fathollahi and F. Razzazi, “Music similarity measurement and recommendation system using convolutional neural networks,” _International Journal of Multimedia Information Retrieval_ , vol. 10, no. 1, pp. 43–53, Mar. 1, 2021. 

- [442] L. Shi, C. Li, and L. Tian, “Music genre classification based on chroma features and deep learning,” in _2019 Tenth International Conference on Intelligent Control and Information Processing (ICICIP)_ , Dec. 2019, pp. 81–86. 

- [443] S.-H. Shin, H.-W. Yun, W.-J. Jang, and H. Park, “Extraction of acoustic features based on auditory spike code and its application to music genre classification,” _IET Signal Processing_ , vol. 13, no. 2, pp. 230–234, 2019. 

772 28 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

- [444] S. S. Shinde and D. S. L. Nalbalwar, “Feature Extraction and Wavelet Analysis in Musical Genre Categorization,” _International Journal of Scientific Engineering and Technology Research_ , vol. 3, no. 18, pp. 3759–3763, 2014. 

- [445] A. Sibi, R. Singh, K. Anurag, A. Choudhary, A. Prakash Agrawal, and G. Raj, “Music genre classification using light gradient boosting machine: A pilot study,” in _Machine Intelligence and Data Science Applications_ , V. Skala, T. P. Singh, T. Choudhury, R. Tomar, and Md. Abul Bashar, Eds., ser. Lecture Notes on Data Engineering and Communications Technologies, Singapore: Springer Nature, 2022, pp. 733–748. 

- [446] I. Siddavatam, A. Dalvi, D. Gupta, Z. Farooqui, and M. Chouhan, “Multi genre music classification and conversion system,” _International Journal of Information Engineering and Electronic Business_ , vol. 12, no. 1, p. 30, 2020. 

- [447] S. Sigtia and S. Dixon, “Improved music feature learning with deep neural networks,” in _2014 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)_ , May 2014, pp. 6959– 6963. 

- [448] D. F. Silva, R. G. Rossi, S. O. Rezende, and G. E. D. A. P. A. Batista, “Music classification by transductive learning using bipartite heterogeneous networks,” in _Proceedings of the 15th International Society for Music Information Retrieval Conference_ , H.-M. Wang, Y.-H. Yang, and J. H. Lee, Eds., 2014, pp. 113–118. 

- [449] A. C. M. da Silva, M. A. N. Coelho, and R. F. Neto, “A Music Classification model based on metric learning applied to MP3 audio files,” _Expert Systems with Applications_ , vol. 144, p. 113 071, Apr. 15, 2020. 

- [450] D. F. Silva, A. C. M. da Silva, L. F. Ortolan, and R. M. Marcacini, “On generalist and domainspecific music classification models and their impacts on brazilian music genre recognition,” in _Anais Do XVIII Simpósio Brasileiro de Computação Musical_ , SBC, 2021, pp. 60–67. 

- [451] D. Silva, M. Silva, R. S. Filho, and A. Silva, “On the fusion of multiple audio representations for music genre classification,” in _Anais Do XVIII Simpósio Brasileiro de Computação Musical_ , Porto Alegre, RS, Brasil: SBC, 2021, pp. 37–44. 

- [452] E. F. Simas Filho, E. A. Borges Jr, and A. C. Fernandes Jr, “Genre classification for brazilian music using independent and discriminant features,” _Journal of Communication and Information Systems_ , vol. 33, no. 1, 2018. 

- [453] A. J. Sinclair, “Predicting music genre preferences based on online comments,” M.S. thesis, California Polytechnic State University, San Luis Obispo, California, Jun. 1, 2014. 

- [454] A. Singh and S. Ramanna, “Application of tolerance near sets to audio signal classification,” in _Advances in Feature Selection for Data and Pattern Recognition_ , ser. Intelligent Systems Reference Library, U. Stańczyk, B. Zielosko, and L. C. Jain, Eds., Cham: Springer International Publishing, 2018, pp. 241–266. 

- [455] J. Singh and V. K. Bohat, “Neural network model for recommending music based on music genres,” in _2021 International Conference on Computer Communication and Informatics (ICCCI)_ , Jan. 2021, pp. 1–6. 

- [456] Y. Singh and A. Biswas, “Robustness of musical features on deep learning models for music genre classification,” _Expert Systems with Applications_ , vol. 199, p. 116 879, Aug. 1, 2022. 

- [457] P. Siva Sankalp, T. Baruah, S. Tiwari, and S. Sankar Ganesh, “Intelligent classification of electronic music,” in _2014 IEEE International Symposium on Signal Processing and Information Technology (ISSPIT)_ , Dec. 2014, pp. 000 031–000 035. 

- [458] M. Skowron, F. Lemmerich, B. Ferwerda, and M. Schedl, “Predicting genre preferences from cultural and socio-economic factors for music retrieval,” in _Advances in Information Retrieval_ , J. M. Jose _et al._ , Eds., ser. Lecture Notes in Computer Science, Cham: Springer International Publishing, 2017, pp. 561–567. 

- [459] L. Soboh, I. Elkabani, and Z. Osman, “Arabic cultural style based music classification,” in _2017 International Conference on New Trends in Computing Sciences (ICTCS)_ , Oct. 2017, pp. 6–11. 

- [460] S. I. Sohel, C. Mondol, H. S. Ayon, U. T. Islam, and M. K. Morol, “Music suggestions from determining the atmosphere of images,” in _2021 24th International Conference on Computer and Information Technology (ICCIT)_ , Dec. 2021, pp. 1–7. 

- [461] G. Song, Z. Wang, F. Han, and S. Ding, “Transfer learning for music genre classification,” in _Intelligence Science I_ , Z. Shi, B. Goertzel, and J. Feng, Eds., ser. IFIP Advances in Information and Communication Technology, Cham: Springer International Publishing, 2017, pp. 183–190. 

- [462] A. Soriano, F. Paulovich, L. G. Nonato, and M. C. F. Oliveira, “Visualization of Music Collections Based on Structural Content Similarity,” in _2014 27th SIBGRAPI Conference on Graphics, Patterns and Images_ , Brazil: IEEE, Aug. 2014, pp. 25–32. 

- [463] M. Srinivas, D. Roy, and C. K. Mohan, “Music genre classification using on-line dictionary learning,” in _2014 International Joint Conference on Neural Networks (IJCNN)_ , Jul. 2014, pp. 1937– 1941. 

773 29 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

- [464] S. Sruthi and S. Sridhar, “Music genre predictor based classification of audio files with low level feature of frequency and time domain using support vector machine over K-means clustering algorithm,” in _2022 Sixth International Conference on I-SMAC (IoT in Social, Mobile, Analytics and Cloud) (I-SMAC)_ , Nov. 2022, pp. 268–273. 

- [465] S. Stern, “Analysis of music genre clustering algorithms,” M.S. thesis, The University of Wisconsin - Milwaukee, United States – Wisconsin, 2021, 25 pp. 

- [466] W. Stokowiec, “A comparative study on music genre classification algorithms,” in _Machine Intelligence and Big Data in Industry_ , ser. Studies in Big Data, D. Ryżko, P. Gawrysiak, M. Kryszkiewicz, and H. Rybiński, Eds., Cham: Springer International Publishing, 2016, pp. 123– 132. 

- [467] B. L. Sturm. “The GTZAN dataset: Its contents, its faults, their effects on evaluation, and its future use.” arXiv: 1306.1461. (2013), [Online]. Available: http://arxiv.org/abs/1306. 1461, preprint. 

- [468] B. L. Sturm and F. Gouyon, “Revisiting intergenre similarity,” _IEEE Signal Processing Letters_ , vol. 20, no. 11, pp. 1050–1053, Nov. 2013. 

- [469] B. L. Sturm, “Evaluating music emotion recognition: Lessons from music genre recognition?” In _Proceedings of the 2013 IEEE International Conference on Multimedia and Expo (ICME)_ , 2013, pp. 1–6. 

- [470] B. L. Sturm, “A simple method to determine if a music information retrieval system is a “horse”,” _IEEE Transactions on Multimedia_ , vol. 16, no. 6, pp. 1636–1644, 2014. 

- [471] B. L. Sturm, “The state of the art ten years after a state of the art: Future research in music information retrieval,” _Journal of New Music Research_ , vol. 43, no. 2, pp. 147–172, 2014. 

- [472] B. L. Sturm, C. Kereliuk, and A. Pikrakis, “A closer look at deep learning neural networks with lowlevel spectral periodicity features,” in _Proceedings of the 4th International Workshop on Cognitive Information Processing_ , Copenhagen, Denmark, 2014, pp. 1–6. 

- [473] B. L. Sturm and N. Collins, “The kiki-bouba challenge: Algorithmic composition for content-based MIR research & development,” in _Proceedings of the 15th International Society for Music Information Retrieval Conference_ , 2014, pp. 21–26. 

- [474] B. L. Sturm, “A survey of evaluation in music genre recognition,” in _Adaptive Multimedia Retrieval: Semantics, Context, and Adaptation_ , A. Nürnberger, S. Stober, B. Larsen, and M. Detyniecki, Eds., vol. LNCS 8382, Springer International Publishing, Oct. 2014, pp. 29–66. 

- [475] B. L. Sturm, C. Kereliuk, and J. Larsen, “¿El Caballo Viejo? Latin genre recognition with deep learning and spectral periodicity,” in _Proceedings of the International Conference on Mathematics and Computation in Music_ , 2015, pp. 335–346. 

- [476] B. L. Sturm, “The “Horse”inside: Seeking causes behind the behaviors of music content analysis systems,” _Computers in Entertainment_ , vol. 14, no. 2, 2016. 

- [477] B. L. Sturm, “Faults in the latin music database and with its use,” in _Extended Abstracts for the LateBreaking Demo Session of the 16th International Society for Music Information Retrieval Conference_ , 2015. 

- [478] B. L. Sturm, “Revisiting priorities: Improving MIR evaluation practices,” in _Proceedings of the 17th International Society for Music Information Retrieval Conference_ , New York City, United States: ISMIR, 2016, pp. 488–494. 

- [479] L. Su, C.-C. M. Yeh, J.-Y. Liu, J.-C. Wang, and Y.-H. Yang, “A systematic evaluation of the bag-of-frames representation for music information retrieval,” _IEEE Transactions on Multimedia_ , vol. 16, no. 5, pp. 1188–1200, Aug. 2014. 

- [480] M. Suero, C. P. Gassen, D. Mitic, N. Xiong, and M. Leon, “A deep neural network model for music genre recognition,” in _Advances in Natural Computation, Fuzzy Systems and Knowledge Discovery_ , Y. Liu, L. Wang, L. Zhao, and Z. Yu, Eds., ser. Advances in Intelligent Systems and Computing, Cham: Springer International Publishing, 2020, pp. 377–384. 

- [481] S. Sugianto and S. Suyanto, “Voting-based music genre classification using melspectogram and convolutional neural network,” in _2019 International Seminar on Research of Information Technology and Intelligent Systems (ISRITI)_ , Dec. 2019, pp. 330–333. 

- [482] G. Sun, “Research on architecture for long-tailed genre computer intelligent classification with music information retrieval and deep learning,” _Journal of Physics Conference Series_ , vol. 2033, no. 1, p. 012 008, Sep. 2021. 

- [483] E. N. Tamatjita and A. W. Mahastama, “Comparison of music genre classification using nearest centroid classifier and k-nearest neighbours,” in _2016 International Conference on Information Management and Technology (ICIMTech)_ , Nov. 2016, pp. 118–123. 

- [484] C. P. Tang, K. L. Chui, Y. K. Yu, Z. Zeng, and K. H. Wong, “Music genre classification using a hierarchical long short term memory (LSTM) model,” in _Third International Workshop on Pattern Recognition_ , vol. 10828, SPIE, Jul. 26, 2018, pp. 334–340. 

774 30 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

- [485] H. Tang, Y. Zhang, and Q. Zhang, “The Use of Deep Learning-Based Intelligent Music Signal Identification and Generation Technology in National Music Teaching,” _Frontiers in Psychology_ , vol. 13, p. 762 402, 2022. pmid: 35814087. 

- [486] T. F. Tavares and J. H. Foleiss, “Automatic music genre classification in small and ethnic datasets,” in _International Symposium on Computer Music Multidisciplinary Research_ , M. Aramaki, M. E. P. Davies, R. Kronland-Martinet, and S. Ystad, Eds., ser. Lecture Notes in Computer Science, Cham: Springer International Publishing, 2018, pp. 35– 48. 

- [487] R. Thiruvengatanadhan, “Music genre classification using mfcc and aann,” _International Research Journal of Engineering and Technology_ , vol. 5, no. 10, pp. 1064–1066, 2018. 

- [488] R. Thiruvengatanadhan, “Music genre classification using GMM,” _International Research Journal of Engineering and Technology_ , vol. 5, no. 10, pp. 2395–0056, 2018. 

- [489] N. Tokui. “Can GAN originate new electronic dance music genres? – Generating novel rhythm patterns using GAN with Genre Ambiguity Loss.” arXiv: 2011 . 13062 [cs]. (Nov. 25, 2020), [Online]. Available: http : / / arxiv . org / abs / 2011 . 13062 (visited on 03/24/2023), preprint. 

- [490] T. Toshniwal, P. Tandon, and N. P, “Music genre recognition using short time fourier tranform and CNN,” in _2022 International Conference on Computer Communication and Informatics (ICCCI)_ , Jan. 2022, pp. 1–4. 

- [491] A. Tsaptsinos, “Lyrics-Based Music Genre Classification Using a Hierarchical Attention Network.,” in _Proceedings of the 18th International Society for Music Information Retrieval Conference_ , Suzhou, China: ISMIR, Oct. 23, 2017, pp. 694–701. 

- [492] S. Tsuchida, S. Fukayama, M. Hamasaki, and M. Goto, “AIST Dance Video Database: MultiGenre, Multi-Dancer, and Multi-Camera Database for Dance Information Processing,” in _Proceedings of the 20th International Society for Music Information Retrieval Conference_ , Delft, The Netherlands: ISMIR, Nov. 4, 2019, pp. 501–510. 

- [493] G. Tzanetakis, “Chapter 26 - Music Mining,” in _Academic Press Library in Signal Processing: Volume 1 Signal Processing Theory and Machine Learning_ , ser. Academic Press Library in Signal Processing: Volume 1, P. S. R. Diniz, J. A. K. Suykens, R. Chellappa, and S. Theodoridis, Eds., vol. 1, Elsevier, Jan. 1, 2014, pp. 1453–1492. 

- [494] C. L. R. S. Ueno and D. Furtado Silva, “On combining diverse models for lyrics-based music genre classification,” in _2019 8th Brazilian Conference on Intelligent Systems (BRACIS)_ , Oct. 2019, pp. 138–143. 

- [495] A. S. Ulaganathan and S. Ramanna, “Granular methods in automatic music genre classification: A case study,” _Journal of Intelligent Information Systems_ , vol. 52, no. 1, pp. 85–105, Feb. 1, 2019. 

- [496] J. Urbano, D. Bogdanov, P. Herrera Boyer, E. Gómez Gutiérrez, and X. Serra, “What is the effect of audio quality on the robustness of MFCCs and chroma features?” In _Proceedings of the 15th International Society for Music Information Retrieval Conference_ , International Society for Music Information Retrieval (ISMIR), 2014, pp. 573–578. 

- [497] V. D. Valerio, R. M. Pereira, Y. M. Costa, D. Bertoini, and C. N. Silla Jr, “A resampling approach for imbalanceness on music genre classification using spectrograms,” in _The Thirty-First International Flairs Conference_ , 2018. 

- [498] J. Valverde-Rebaza, A. Soriano, L. Berton, M. C. Ferreira de Oliveira, and A. De Andrade Lopes, “Music Genre Classification Using Traditional and Relational Approaches,” in _2014 Brazilian Conference on Intelligent Systems_ , Oct. 2014, pp. 259– 264. 

- [499] A. van den Oord, S. Dieleman, and B. Schrauwen, “Transfer learning by supervised pre-training for audio-based music classification,” in _Proceedings of the 15th International Society for Music Information Retrieval Conference_ , 2014, pp. 29–34. 

- [500] I. Vatolkin, M. Preuß, and G. Rudolph, “Training set reduction based on 2-gram feature statistics for music genre recognition,” Technische Universität Dortmund, Faculty of Computer Science, Algorithm ⋯, Algorithm Engineering Report TR13-2001, 2013. 

- [501] I. Vatolkin, “Improving supervised music classification by means of multi-objective evolutionary feature selection,” Ph.D. dissertation, TU Dortmund, Jun. 20, 2013. 

- [502] I. Vatolkin, G. Rötter, and C. Weihs, “Music Genre Prediction by Low-Level and High-Level Characteristics,” in _Data Analysis, Machine Learning and Knowledge Discovery_ , ser. Studies in Classification, Data Analysis, and Knowledge Organization, M. Spiliopoulou, L. Schmidt-Thieme, and R. Janning, Eds., Cham: Springer International Publishing, 2014, pp. 427–434. 

- [503] I. Vatolkin and G. Rudolph, “Interpretable music categorisation based on fuzzy rules and highlevel audio features,” in _Data Science, Learning by Latent Structures, and Knowledge Discovery_ , B. Lausen, S. Krolak-Schwerdt, and M. Böhmer, Eds., ser. Studies in Classification, Data Analysis, 

775 31 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

and Knowledge Organization, Berlin, Heidelberg: Springer, 2015, pp. 423–432. 

- [504] I. Vatolkin, G. Rudolph, and C. Weihs, “Evaluation of album effect for feature selection in music genre recognition.,” in _Proceedings of the 16th International Society for Music Information Retrieval Conference_ , Málaga, Spain, 2015, pp. 169– 175. 

- [505] I. Vatolkin, G. Rudolph, and C. Weihs, “Interpretability of Music Classification as a Criterion for Evolutionary Multi-objective Feature Selection,” in _Evolutionary and Biologically Inspired Music, Sound, Art and Design_ , C. Johnson, A. Carballal, and J. Correia, Eds., ser. Lecture Notes in Computer Science, Cham: Springer International Publishing, 2015, pp. 236–248. 

- [506] I. Vatolkin and C. Mckay, “Stability of Symbolic Feature Group Importance in the Context of MultiModal Music Classification,” in _Proceedings of the 23rd International Society for Music Information Retrieval Conference_ , Bengaluru, India: ISMIR, Dec. 4, 2022, pp. 469–476. 

- [507] I. Vatolkin and C. McKay, “Multi-Objective Investigation of Six Feature Source Types for MultiModal Music Classification,” _Transactions of the International Society for Music Information Retrieval_ , vol. 5, no. 1, pp. 1–19, 1 Jan. 24, 2022. 

- [508] T. G. Videira, B. Pennycook, and J. M. Rosa, “Formalizing fado: a contribution to automatic song-making,” _Journal of Creative Music Systems_ , vol. 1, no. 2, 2 Mar. 1, 2017. 

- [509] S. Vishnupriya and K. Meenakshi, “Automatic music genre classification using convolution neural network,” in _2018 International Conference on Computer Communication and Informatics (ICCCI)_ , Jan. 2018, pp. 1–4. 

- [510] L. Wadhwa and P. Mukherjee, “Music genre classification using multi-modal deep learning based fusion,” in _2021 Grace Hopper Celebration India (GHCI)_ , Feb. 2021, pp. 1–5. 

- [511] Z. Wang, J. Xia, and B. Luo, “The Analysis and Comparison of Vital Acoustic Features in ContentBased Classification of Music Genre,” in _2013 International Conference on Information Technology and Applications_ , Nov. 2013, pp. 404–408. 

- [512] Y. Wang, X. Chen, and P. J. Ramadge, “Sparse representation classification via sequential Lasso screening,” in _2013 IEEE Global Conference on Signal and Information Processing_ , Dec. 2013, pp. 1001–1004. 

- [513] J. Wang, C. Wang, J. Wei, and J. Dang, “Chinese opera genre classification based on multi-feature fusion and extreme learning machine,” in _2015 Asia-Pacific Signal and Information Processing Association Annual Summit and Conference (APSIPA)_ , Dec. 2015, pp. 811–814. 

- [514] Z. Wang, S. Muknahallipatna, M. Fan, A. Okray, and C. Lan, “Music Classification using an Improved CRNN with Multi-Directional Spatial Dependencies in Both Time and Frequency Dimensions,” in _2019 International Joint Conference on Neural Networks (IJCNN)_ , Budapest, Hungary: IEEE, Jul. 2019, pp. 1–8. 

- [515] L. Wang, H. Zhu, X. Zhang, S. Li, and W. Li, “Transfer learning for music classification and regression tasks using artist tags,” in _Proceedings of the 7th Conference on Sound and Music Technology (CSMT)_ , H. Li, S. Li, L. Ma, C. Fang, and Y. Zhu, Eds., ser. Lecture Notes in Electrical Engineering, Singapore: Springer, 2020, pp. 81–89. 

- [516] G. Wassi, S. Iloga, O. Romain, and B. Granado, “FPGA-based real-time MFCC extraction for automatic audio indexing on FM broadcast data,” in _2015 Conference on Design and Architectures for Signal and Image Processing (DASIP)_ , Sep. 2015, pp. 1–6. 

- [517] C. Weiss, M. Mauch, and S. Dixon, “Timbreinvariant audio features for style analysis of classical music,” in _11th Sound and Music Computing Conference and 40th International Computer Music Conference (SMC/ICMC2014)_ , Athens, Greece: Zenodo, Sep. 14, 2014. 

- [518] C. Weiß, “Computational methods for tonalitybased style analysis of classical music audio recordings,” Ph.D. dissertation, Technische Universität Ilmenau, Aug. 25, 2017. 

- [519] F. W. Wibowo and Wihayati, “Detection of indonesian dangdut music genre with foreign music genres through features classification using deep learning,” in _2021 International Seminar on Machine Learning, Optimization, and Data Science (ISMODE)_ , Jan. 2022, pp. 313–318. 

- [520] B. Wilkes, I. Vatolkin, and H. Müller, “Statistical and visual analysis of audio, text, and image features for multi-modal music genre recognition,” _Entropy_ , vol. 23, no. 11, p. 1502, 11 Nov. 2021. 

- [521] R. Wongso and D. D. Santika, “Automatic music genre classification using dual tree complex wavelet transform and support vector machine.,” _Journal of Theoretical & Applied Information Technology_ , vol. 63, no. 1, pp. 61–68, 2014. 

- [522] H. Q. Wu and M. Zhang, “Gabor-LBP Features and Combined Classifiers for Music Genre Classification,” _Advanced Materials Research_ , vol. 756–759, pp. 4407–4411, 2013. 

- [523] M.-J. Wu and J.-S. R. Jang, “Combining acoustic and multilevel visual features for music genre classification,” _ACM Transactions on Multimedia Computing Communications and Applications_ , vol. 12, no. 1, 10:1–10:17, Aug. 24, 2015. 

776 32 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

- [524] M. Wu and Y. Wang, “A feature selection algorithm of music genre classification based on ReliefF and SFS,” in _2015 IEEE/ACIS 14th International Conference on Computer and Information Science (ICIS)_ , Jun. 2015, pp. 539–544. 

- [525] W. Wu, F. Han, G. Song, and Z. Wang, “Music genre classification using independent recurrent neural network,” in _2018 Chinese Automation Congress (CAC)_ , Nov. 2018, pp. 192–195. 

- [526] M. Wu and X. Liu, “A double weighted KNN algorithm and its application in the music genre classification,” in _2019 6th International Conference on Dependable Systems and Their Applications (DSA)_ , Jan. 2020, pp. 335–340. 

- [527] B. D. Wundervald and W. M. Zeviani. “Machine learning and chord based feature engineering for genre prediction in popular brazilian music.” arXiv: 1902 . 03283 [cs, eess, stat]. (Feb. 8, 2019), [Online]. Available: http : / / arxiv.org/abs/1902.03283 (visited on 03/09/2023), preprint. 

- [528] B. Wundervald, “Feature Engineering for Genre Characterization in Brazilian Music,” in _Proceedings of the 13th International Workshop on Machine Learning and Music_ , 2020, pp. 60–64. 

- [529] Y. Xiao, Q. Zhang, M. Wu, and D. Kailing, “Application of multilevel local feature coding in music genre recognition,” _Mathematical Problems in Engineering_ , vol. 2022, e3627831, Mar. 22, 2022. 

- [530] Y. Xu and W. Zhou, “A deep music genres classification model based on CNN with squeeze & excitation block,” in _2020 Asia-Pacific Signal and Information Processing Association Annual Summit and Conference (APSIPA ASC)_ , Dec. 2020, pp. 332– 338. 

- [531] Z. Xu, “Construction of intelligent recognition and learning education platform of national music genre under deep learning,” _Frontiers in Psychology_ , vol. 13, p. 843 427, May 26, 2022. pmid: 35693513. 

- [532] K. Xu, M. A. Alif, and G. He, “A novel music genre classification algorithm based on continuous wavelet transform and convolution neural network,” in _Proceedings of the 2021 5th International Conference on Electronic Information Technology and Computer Engineering_ , ser. EITCE 2021, New York, NY, USA: Association for Computing Machinery, Dec. 31, 2022, pp. 1269–1273. 

- [533] Z. Xu _et al._ , “Research on music genre classification based on residual network,” in _Mobile Multimedia Communications_ , Y. Chenggang, W. Honggang, and L. Yun, Eds., ser. Lecture Notes of the Institute for Computer Sciences, Social Informatics and Telecommunications Engineering, Cham: Springer Nature Switzerland, 2022, pp. 209–223. 

- [534] Y.-H. Yang, “Towards real-time music autotagging using sparse features,” in _2013 IEEE International Conference on Multimedia and Expo (ICME)_ , Jul. 2013, pp. 1–6. 

- [535] J. Yang, “Lyric-based music genre classifcation,” M.S. thesis, 2018. 

- [536] H. Yang and W.-Q. Zhang, “Music genre classification using duplicated convolutional layers in neural networks.,” in _Interspeech_ , 2019, pp. 3382– 3386. 

- [537] R. Yang, L. Feng, H. Wang, J. Yao, and S. Luo, “Parallel recurrent convolutional neural networksbased music genre classification method for mobile devices,” _IEEE Access_ , vol. 8, pp. 19 629–19 637, 2020. 

- [538] T. Ye, S. Si, J. Wang, N. Cheng, and J. Xiao, “Uncertainty Calibration for Deep Audio Classifiers,” in _Interspeech_ , Jun. 27, 2022. arXiv: 2206. 13071 [cs, eess]. 

- [539] C.-C. M. Yeh, L. Su, and Y.-H. Yang, “Duallayer bag-of-frames model for music genre classification,” in _2013 IEEE International Conference on Acoustics, Speech and Signal Processing_ , May 2013, pp. 246–250. 

- [540] Y. Yi, K.-Y. Chen, and H.-Y. Gu, “Mixture of CNN experts from multiple acoustic feature domain for music genre classification,” in _2019 AsiaPacific Signal and Information Processing Association Annual Summit and Conference (APSIPA ASC)_ , Nov. 2019, pp. 1250–1255. 

- [541] Y. Yi, X. Zhu, Y. Yue, and W. Wang, “Music genre classification with LSTM based on time and frequency domain features,” in _2021 IEEE 6th International Conference on Computer and Communication Systems (ICCCS)_ , Apr. 2021, pp. 678–682. 

- [542] J. Yoon, H. Lim, and D.-W. Kim, “Music genre classification using feature subset search,” _International Journal of Machine Learning and Computing_ , vol. 6, no. 2, p. 134, 2016. 

- [543] Y. Yu, S. Luo, S. Liu, H. Qiao, Y. Liu, and L. Feng, “Deep attention based music genre classification,” _Neurocomputing_ , vol. 372, pp. 84–91, Jan. 8, 2020. 

- [544] C. Yuan _et al._ , “Exploiting heterogeneous artist and listener preference graph for music genre classification,” in _Proceedings of the 28th ACM International Conference on Multimedia_ , ser. MM ’20, New York, NY, USA: Association for Computing Machinery, Oct. 12, 2020, pp. 3532–3540. 

- [545] M. Zanoni, “Content-based macro-descriptors for music classification and multimedia information retrieval,” Ph.D. dissertation, Politecnico Milano, Milan, Italy, Jan. 1, 2013. 

777 33 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

- [546] C. Zhang, G. Evangelopoulos, S. Voinea, L. Rosasco, and T. Poggio, “A deep representation for invariance and music classification,” in _2014 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)_ , May 2014, pp. 6984– 6988. 

- [547] P. Zhang _et al._ , “A deep neural network for modeling music,” in _Proceedings of the 5th ACM on International Conference on Multimedia Retrieval_ , ser. ICMR ’15, New York, NY, USA: Association for Computing Machinery, Jun. 22, 2015, pp. 379– 386. 

- [548] W. Zhang, W. Lei, X. Xu, and X. Xing, “Improved music genre classification with convolutional neural networks,” in _Interspeech_ , ISCA, Sep. 8, 2016, pp. 3304–3308. 

- [549] X. Zhang, T. Ren, L. Wang, and H. Xu. “Music Influence Modeling Based on Directed Network Model.” arXiv: 2204 . 03588 [stat]. (Apr. 7, 2022), [Online]. Available: http : / / arxiv.org/abs/2204.03588 (visited on 03/24/2023), preprint. 

- [550] Y. Zhang, Z. Zhou, and M. Sun, “Influence of musical elements on the perception of ‘chinese style’ in music,” _Cognitive Computation and Systems_ , vol. 4, no. 2, pp. 147–164, 2022. 

- [551] R. Zhang, X. Zhou, and J. Song, “Music and musician influence, similarity measure, and music genre division based on social network analysis,” in _2nd International Conference on Artificial Intelligence, Automation, and High-Performance Computing (AIAHPC 2022)_ , vol. 12348, SPIE, Nov. 10, 2022, pp. 107–116. 

- [552] W. Zhang, “Music genre classification based on deep learning,” _Mobile Information Systems_ , vol. 2022, e2376888, Aug. 21, 2022. 

- [553] Y. Zhao and J. Guo, “MusiCoder: A universal music-acoustic encoder based on transformer,” in _MultiMedia Modeling_ , J. Lokoč _et al._ , Eds., ser. Lecture Notes in Computer Science, Cham: Springer International Publishing, 2021, pp. 417– 429. 

- [554] H. Zhao, C. Zhang, B. Zhu, Z. Ma, and K. Zhang, “S3T: Self-supervised pre-training with swin transformer for music classification,” in _2022 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)_ , May 2022, pp. 606– 610. 

- [555] E. Zheng, M. Moh, and T.-S. Moh, “Music genre classification: A N-gram based musicological approach,” in _2017 IEEE 7th International Advance Computing Conference (IACC)_ , Jan. 2017, pp. 671–677. 

- [556] Z. Zheng, “The classification of music and art genres under the visual threshold of deep learning,” _Computational Intelligence and Neuroscience_ , vol. 2022, p. 4 439 738, May 18, 2022. pmid: 35634048. 

- [557] H. Zhu, Y. Niu, D. Fu, and H. Wang, “MusicBERT: A self-supervised learning of music representation,” in _Proceedings of the 29th ACM International Conference on Multimedia_ , ser. MM ’21, New York, NY, USA: Association for Computing Machinery, Oct. 17, 2021, pp. 3955–3963. 

- [558] Y. Zhuang, Y. Chen, and J. Zheng, “Music genre classification with transformer classifier,” in _Proceedings of the 2020 4th International Conference on Digital Signal Processing_ , ser. ICDSP 2020, New York, NY, USA: Association for Computing Machinery, Sep. 10, 2020, pp. 155–159. 

- [559] A. Zlatintsi and P. Maragos, “Comparison of different representations based on nonlinear features for music genre classification,” in _2014 22nd European Signal Processing Conference_ , Sep. 2014, pp. 1547–1551. 

- [560] A. Zuhair and H. Hassani. “Comparing the accuracy of deep neural networks (DNN) and convolutional neural network (CNN) in music genre recognition (MGR): Experiments on kurdish music.” arXiv: 2111 . 11063 [cs, eess]. (Nov. 22, 2021), [Online]. Available: http:// arxiv.org/abs/2111.11063 (visited on 03/03/2023), preprint. 

- [561] B. L. Sturm, “Two systems for automatic music genre recognition: What are they really recognizing?” In _Proc. ACM MIRUM Workshop_ , Nov. 2012, pp. 69–74. 

- [562] B. L. Sturm, “Classification accuracy is not enough: On the evaluation of music genre recognition systems,” _J. Intell. Info. Systems_ , vol. 41, no. 3, pp. 371–406, 2013. 

- [563] G. Tzanetakis and P. Cook, “Musical genre classification of audio signals,” _IEEE Trans. Speech Audio Process._ , vol. 10, no. 5, pp. 293–302, Jul. 2002. 

- [564] B. L. Sturm, “An analysis of the GTZAN music genre dataset,” in _Proc. ACM MIRUM Workshop_ , Nara, Japan, Nov. 2012, pp. 7–12. 

- [565] F. R. Algarra and B. L. Sturm, “Re-evaluating the scattering transform,” in _Proc. ISMIR (Late breaking demo)_ , 2015. 

- [566] J. Urbano, M. Schedl, and X. Serra, “Evaluation in music information retrieval,” _Journal of Intelligent Information Systems_ , vol. 41, no. 3, pp. 345–369, 2013. 

- [567] A. Flexer, “Statistical evaluation of music information retrieval experiments,” _J. New Music Research_ , vol. 35, no. 2, pp. 113–120, 2006. 

778 34 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

- [568] A. Flexer, “A closer look on artist filters for musical genre classification,” in _Proc. ISMIR_ , Sep. 2007, pp. 341–344. 

- [569] A. Flexer and D. Schnitzer, “Album and artist effects for audio similarity at the scale of the web,” in _Proc. SMC_ , Jul. 2009, pp. 59–64. 

- [570] A. Flexer, D. Schnitzer, M. Gasser, and T. Pohle, “Combining features reduces hubness in audio similarity,” in _Proc. Int. Symp. Music Info. Retrieval_ , 2010, pp. 171–176. 

- [571] E. Pampalk, A. Flexer, and G. Widmer, “Improvements of audio-based music similarity and genre classification,” in _Proc. Int. Soc. Music Info. Retrieval_ , Sep. 2005, pp. 628–233. 

- [572] G. Peeters, J. Urbano, and G. J. F. Jones, “Notes from the ISMIR 2012 late-breaking session on evaluation in music information retrieval,” in _Proc. ISMIR_ , 2012. 

- [573] M. Schedl, A. Flexer, and J. Urbano, “The neglected user in music information retrieval research,” _J. Intell. Info. Systems_ , vol. 41, no. 3, pp. 523–539, 2013. 

- [574] J. Urbano, B. McFee, J. S. Downie, and M. Schedl, “How significant is statistically significant? the case of audio music similarity and retrieval,” in _Proc. ISMIR_ , 2012, pp. 181–186. 

- [575] G. C. Bowker and S. L. Star, _Sorting Things out: Classification and Its Consequences_ . The MIT Press, 1999. 

- [576] D. Brackett, _Interpreting Popular Music_ , First printing of this edition. Berkeley: University of California Press, Oct. 25, 2000, 280 pp. 

- [577] D. Brackett, _Categorizing Sound: Genre and Twentieth-Century Popular Music_ . University of California Press, Jul. 2016, 376 pp. 

- [578] P. Coulangeon and I. Roharik, “Testing the ”Omnivore/Univore” Hypothesis in a CrossNational Perspective. On the Social Meaning of Ecletism in Musical Tastes,” presented at the The Summer Meeting of the ISA RC28, UCLA, Aug. 19, 2005. 

- [579] P. Coulangeon, “Social Stratification of Musical Tastes : Questioning the Cultural Legitimacy Model,” _Revue française de sociologie_ , vol. 46, no. 5, pp. 123–154, 2005. 

- [580] M. A. Coutinho and F. Miranda, “To describe genres:: Problems and strategies,” in _Genre in a Changing World_ , C. Bazerman, A. Bonini, and D. Figueiredo, Eds., The WAC Clearinghouse, 2009, pp. 35–55. 

- [581] P. DiMaggio, “Classification in art,” _American Sociological Review_ , vol. 52, no. 4, pp. 440–455, 1987. JSTOR: 2095290. 

- [582] E. Drott, “The End(s) of Genre,” _Journal of Music Theory_ , vol. 57, no. 1, pp. 1–45, Apr. 1, 2013. 

- [583] F. Fabbri, “A theory of musical genres: Two applications,” in _Proc. Int. Conf. Popular Music Studies_ , 1980. 

- [584] F. Fabbri, “Browsing musical spaces: Categories and the musical mind,” in _Proc. Int. Association for the Study of Popular Music_ , 1999. 

- [585] S. Frith, _Music For Pleasure: Essays on the Sociology of Pop_ , First Edition. Cambridge: Polity Press, Sep. 22, 1988, 232 pp. 

- [586] J. Frow, _Genre_ . New York, NY, USA: Routledge, 2005. 

- [587] J. C. Lena and R. A. Peterson, “Classification as culture: Types and trajectories of music genres,” _American Sociological Review_ , vol. 73, no. 5, pp. 697–718, 2008. eprint: https://doi.org/ 10.1177/000312240807300501. 

- [588] J. C. Lena, _Banding Together: How Communities Create Genres in Popular Music_ . Princeton University Press, 2012. JSTOR: j.ctt7rrzb. 

- [589] O. Lizardo, “The mutual specification of genres and audiences: Reflective two-mode centralities in person-to-culture data,” _Poetics_ , vol. 68, pp. 52– 71, Jun. 1, 2018. 

- [590] K. McLeod, “Genres, Subgenres, Sub-Subgenres and More: Musical and Social Differentiation Within Electronic/Dance Music Communities,” _Journal of Popular Music Studies_ , vol. 13, no. 1, pp. 59–75, 2001. 

- [591] L. B. Meyer, _Emotion and Meaning in Music_ . Chicago, IL: University of Chicago Press, Feb. 1961, 315 pp. 

- [592] A. F. Moore, “Categorical conventions in music discourse: Style and genre,” _Music & Letters_ , vol. 82, no. 3, pp. 432–442, 2001. 

- [593] K. Negus, _Producing Pop: Culture and Conflict in the Popular Music Industry_ . London: Hodder Education, Jan. 7, 1993, 192 pp. 

- [594] K. Negus, _Popular Music in Theory: An Introduction_ , 1st edition. Cambridge: Polity, Nov. 30, 1996, 255 pp. 

- [595] K. Negus, “From creator to data: The post-record music industry and the digital conglomerates,” _Media, Culture & Society_ , vol. 41, no. 3, pp. 367–384, Apr. 2019. 

- [596] W. G. Roy, ““Race records”and “hillbilly music” : Institutional origins of racial categories in the American commercial recording industry,” _Poetics_ , Music in Society: The Sociological Agenda, vol. 32, no. 3, pp. 265–279, Jun. 1, 2004. 

- [597] W. G. Roy and T. J. Dowd, “What Is Sociological about Music?” _Annual Review of Sociology_ , vol. 36, pp. 183–203, Volume 36, 2010 Aug. 11, 2010. 

779 35 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

- [598] P. Tagg, “Analysing popular music: Theory, method and practice,” _Popular Music_ , vol. 2, pp. 37–67, 1982. JSTOR: 852975. 

- [599] N. Scaringella, G. Zoia, and D. Mlynek, “Automatic genre classification of music content: A survey,” _IEEE Signal Process. Mag._ , vol. 23, no. 2, pp. 133–141, Mar. 2006. 

- [600] T. Bertin-Mahieux, D. P. Ellis, B. Whitman, and P. Lamere, “The million song dataset,” in _Proc. ISMIR_ , 2011, pp. 591–596. 

- [601] F. Rodríguez-Algarra, B. L. Sturm, and S. Dixon, “Characterising confounding effects in music classification experiments through interventions,” _Trans. Int. Soc. Music Information Retrieval_ , vol. 2, no. 1, pp. 52–66, 2019. 

- [602] S. Oramas, F. Barieri, O. Nieto, and X. Serra, “Multimodal deep learning for music genre classification,” _Trans. ISMIR_ , 2018. 

- [603] B. Matityaho and M. Furst, “Neural network based model for classification of music type,” in _Proc. Conv. Electrical and Elect. Eng. in Israel_ , Mar. 1995, pp. 1–5. 

- [604] J.-J. Aucouturier and E. Pampalk, “Introduction – from genres to tags: A little epistemology of music information retrieval research,” _J. New Music Research_ , vol. 37, no. 2, pp. 87–92, 2008. 

- [605] K. Byun and M. Y. Kim, “Musical Genre Classification System based on Multiple-Octave Bands,” _Journal of the Institute of Electronics and Information Engineers_ , vol. 50, no. 12, pp. 238–244, 2013. 

- [606] H. C. Chang and C. K. Yang, “Automatic MIDI Genre Conversion,” _Applied Mechanics and Materials_ , vol. 284–287, pp. 3040–3043, 2013. 

- [607] C.-H. Chuan, “Audio Classification and Retrieval Using Wavelets and Gaussian Mixture Models,” _International Journal of Multimedia Data Engineering and Management (IJMDEM)_ , vol. 4, no. 1, pp. 1–20, Jan. 2013. 

- [608] B. Kostek and A. Kaczmarek, “Music Recommendation Based on Multidimensional Description and Similarity Measures,” _Fundamenta Informaticae_ , vol. 127, no. 1-4, pp. 325–340, Jan. 2013. 

- [609] T. F. B. M. de Matos, “Métodos Estatísticos de Classificação de Géneros Musicais,” M.S. thesis, Lisbon, Jul. 2013. 

- [610] P. Hoffmann and B. Kostek, “Subjective perception of music genres in the field of music information retrieval systems,” in _15th International Symposium on New Trends in Audio and Video_ , 2014. 

- [611] D. Jang, S. Shin, J. Lee, S.-J. Jang, and T.-B. Lim, “Feature reduction based on distance metric learning for musical genre classification,” in _Proceedings of the Korean Society of Broadcast Engineers Conference_ , The Korean Institute of Broadcast and Media Engineers, 2014, pp. 3–4. 

- [612] R. Miki, W. Kameyama, and M. Suganuma, “A Consideration on Music Classification using Background Activity of Brain,” _IEICE Technical Report_ , vol. 114, no. 68, pp. 211–216, May 2014. 

- [613] B. K. Baniya and 이준환, “Label prediction of the unlabeled mood of a music genre using semisupervised learning,” 차세대컨버전스정보서비 스기술논문지, vol. 4, no. 2, pp. 51–64, 2015. 

- [614] P. Hoffmann and B. Kostek, “Music genre classification applied to bass enhancement for mobile technology,” _Elektronika : konstrukcje, technologie, zastosowania_ , vol. 56, no. 4, pp. 14–19, 2015. 

- [615] K. C. Silva Paulo, R. D. Solgon Bassi, A. L. Delorme, R. C. [ Guido, I. N. da Silva, and Anonymous, “Music genre classification based on paraconsistency,” in _2nd International Conference On Advanced Education Technology And Management Science (Aetms 2014)_ , Destech Publications, Inc, Jan. 2015, p. 427. 

- [616] S. U. N. Hui, X. U. Jieping, and L. I. U. Binbin, “Music genre classification based on multiple kernel learning and support vector machine,” _Journal of Computer Applications_ , vol. 35, no. 6, p. 1753, Jun. 2015. 

- [617] S. Kim, D. Kim, and B. Suh, “Music genre classification using multimodal deep learning,” in _Proceedings of HCI Korea_ , ser. HCIK ’16, Seoul, KOR: Hanbit Media, Inc., Jan. 2016, pp. 389–395. 

- [618] Ö. Çoban and G. T. Özyer, “Music genre classification from turkish lyrics,” in _2016 24th Signal Processing and Communication Application Conference (SIU)_ , May 2016, pp. 101–104. 

- [619] R. H. D. Zottesso, Y. M. G. Costa, and D. Bertolini, “Music genre classification using visual features with feature selection,” in _2016 35th International Conference of the Chilean Computer Science Society (SCCC)_ , Oct. 2016, pp. 1–6. 

- [620] W.-J. Jang, H.-W. Yun, S.-H. Shin, H.-J. Cho, W. Jang, and H. Park, “Music genre classification using spikegram and deep neural network,” _Journal of Broadcast Engineering_ , vol. 22, no. 6, pp. 693– 701, 2017. 

- [621] K. Açıcı, T. Aşuroğlu, and H. Oğul, “Information retrieval in metal music sub-genres,” in _2017 25th Signal Processing and Communications Applications Conference (SIU)_ , May 2017, pp. 1–4. 

- [622] Ö. Çoban and I. Karabey, “Music genre classification with word and document vectors,” in _2017 25th Signal Processing and Communications Applications Conference (SIU)_ , May 2017, pp. 1–4. 

- [623] A. Karatana and O. Yildiz, “Music genre classification with machine learning techniques,” in _2017 25th Signal Processing and Communications Applications Conference (SIU)_ , May 2017, pp. 1–4. 

780 36 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

- [624] A. Azcarraga and F. K. Flores, “A study on selforganizing maps and K-means clustering on a music genre dataset,” in _Theory and Practice of Computation_ , World Scientific, Oct. 2017, pp. 219–234. 

- [625] V. S. González, “The impact of temporal features in music genre recognition,” M.S. thesis, TU Dublin, Jan. 2019. 

- [626] Y. Hao, “Music genre classification and transfer based on MusicXML with high-level features and chord vectors,” M.S. thesis, ResearchSpace@Auckland, 2019. 

- [627] C. Dabas, A. Agarwal, N. Gupta, V. Jain, and S. Pathak, “Machine learning evaluation for music genre classification of audio signals,” _International Journal of Grid and High Performance Computing (IJGHPC)_ , vol. 12, no. 3, pp. 57–67, 2020. 

- [628] M. Anand, V. Vijayalakshmi, and S. Vimal, “Music genre classification with deep learning,” _Solid State Technology_ , vol. 63, no. 6, pp. 14 730–14 734, Dec. 2020. 

- [629] A. Shreyash, S. P. Dhanure, P. P. Rathod, C. Ashay, and G. Pritesh, “Identification of music genre using convolutional neural network,” _NEW ARCH-INTERNATIONAL JOURNAL OF CONTEMPORARY ARCHITECTURE_ , vol. 8, no. 2, pp. 2103–2109, Oct. 2021. 

- [630] A. K. Mishra, D. K. Singh, and A. Khare, “Music genre detection using deep learning models,” _i-Manager’s Journal on Information Technology_ , vol. 11, no. 2, p. 10, 2022. 

- [631] J. Singh, “An efficient deep neural network model for music classification,” _International Journal of Web Science_ , vol. 3, no. 3, pp. 236–248, Jan. 2022. 

- [632] D. V. Subbaiah, N. N. Jyothi, K. Lokesh, K. S. Anusha, and K. Saikumar, “Instinctive music genre detection and categorization of audio data using machine learning,” _Harbin Gongye Daxue Xuebao/Journal of Harbin Institute of Technology_ , vol. 54, no. 4, pp. 354–356, 2022. 

- [633] A. Porter, D. Bogdanov, R. Kaye, R. Tsukanov, and X. Serra, “Acousticbrainz: A community platform for gathering music information obtained from audio,” in _Proc. ISMIR_ , 2015, pp. 786–792. 

- [634] P. Cano _et al._ , “Ismir 2004 audio description contest,” Barcelona: Universitat Pompeu Fabra, Music technology Group, Tech. Rep. MTG-TR-2006-02, 2006. 

- [635] K. Benzi, M. Defferrard, P. Vandergheynst, and X. Bresson, “FMA: A dataset for music analysis,” _arXiv_ , vol. 1612.01840, 2016. 

- [636] C. N. Silla, A. L. Koerich, and C. A. A. Kaestner, “The Latin music database,” in _Proc. ISMIR_ , 2008, pp. 451–456. 

- [637] S. Dixon, F. Gouyon, and G. Widmer, “Towards characterisation of music via rhythmic patterns,” in _Proc. ISMIR_ , 2004, pp. 509–517. 

- [638] B. L. T. Sturm and A. Flexer, “A review of validity and its relationship to music information research,” in _Proc. Int. Symp. Music Info. Retrieval_ , 2023. 

- [639] R. Huang, A. Holzapfel, B. L. T. Sturm, and A.-K. Kaila, “Beyond diverse datasets: Responsible mir, interdisciplinarity, and the fractured worlds of music,” _Trans. Int. Soc. Music Information Retrieval_ , vol. 6, no. 1, pp. 43–59, 2023. 

- [640] J. Priem, H. Piwowar, and R. Orr, _Openalex: A fully-open index of scholarly works, authors, venues, institutions, and concepts_ , 2022. arXiv: 2205.01833 [cs.DL]. 

- [641] J. Rodu and M. Baiocchi, “When black box algorithms are (not) appropriate,” _Observational Studies_ , vol. 9, no. 2, pp. 79–101, 2023. 

- [642] D. Raji, E. Denton, E. M. Bender, A. Hanna, and A. Paullada, “AI and the Everything in the Whole Wide World Benchmark,” _Proceedings of the Neural Information Processing Systems Track on Datasets and Benchmarks_ , vol. 1, Dec. 6, 2021. 

- [643] R. McElreath, _Statistical Rethinking: A Bayesian Course with Examples in R and Stan_ . CRC press, 2020. 

- [644] A. Ferraro, G. Ferreira, F. Diaz, and G. Born, “Measuring Commonality in Recommendation of Cultural Content: Recommender Systems to Enhance Cultural Citizenship,” in _Proceedings of the 16th ACM Conference on Recommender Systems_ , ser. RecSys ’22, New York, NY, USA: Association for Computing Machinery, Sep. 13, 2022, pp. 567– 572. 

- [645] A. Holzapfel, B. L. Sturm, and M. Coeckelbergh, “Ethical dimensions of music information retrieval technology,” _Trans. Int. Soc. Music Information Retrieval_ , vol. 1, no. 1, pp. 44–55, 2018. 

- [646] M. Youngblood, K. Baraghith, and P. E. Savage, “Phylogenetic reconstruction of the cultural evolution of electronic music via dynamic community detection (1975–1999),” _Evolution and Human Behavior_ , vol. 42, no. 6, pp. 573–582, Nov. 1, 2021. 

- [647] J. A. Hockman, “An Ethnographic and Technological Study of Breakbeats in Hardcore, Jungle and Drum & Bass,” Ph.D. dissertation, McGill University (Canada), Canada – Quebec, CA, 2013, 544 pp. 

- [648] A. Srinivasamurthy, A. Holzapfel, K. K. Ganguli, and X. Serra, “Aspects of Tempo and Rhythmic Elaboration in Hindustani Music: A Corpus Study,” _Frontiers in Digital Humanities_ , vol. 4, Oct. 31, 2017. 

- [649] K. Frieler, “A feature history of jazz improvisation.,” in _Jazz @ 100_ , ser. Darmstadt Studies in Jazz Research, W. Knauer, Ed., vol. 15, Hofheim: Wolke Verlag, 2018, pp. 67–90. 

781 37 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

- [650] W. R. Shadish, T. D. Cook, and D. T. Campbell, _Experimental and Quasi-experimental Designs for Generalised Causal Inference_ . Houghton Mifflin Company, 2001. 

782 

38 

