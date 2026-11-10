---
paper_id: "000028"
year: 2023
title: "Download pdf"
source_url: "https://zenodo.org/record/10265269/files/000028.pdf"
---

# TOWARDS COMPUTATIONAL MUSIC ANALYSIS FOR MUSIC THERAPY 

Anja Volk<sup>1</sup> Tinka Veldhuis<sup>1</sup> Katrien Foubert<sup>2</sup> Jos de Backer<sup>2</sup> 1 Department of Information and Computing Sciences, Utrecht University, the Netherlands 2 Faculty of Medicine, KU Leuven, LUCA School of Arts, Belgium 

```
a.volk@uu.nl,tinkaveldhuis94@gmail.com,{katrien.foubert,jos.debacker}@kuleuven.be
```

## ABSTRACT 

The research field of music therapy has witnessed a rising interest in recent years to develop and employ computational methods to support therapists in their daily practice. While Music Information Retrieval (MIR) research has identified the area of health and well-being as a promising application field for MIR methods to support health professionals, collaborations with experts in this field are as of today sparse. This paper provides an overview of potential applications of computational music analysis as developed in MIR for the field of active music therapy. We elaborate on the music therapy method of improvisation, with a particular focus on introducing therapeutic concepts that relate to musical structures. We identify application scenarios for analysing musical structures in improvisations, introduce existing analysis methods of therapists, and discuss the potential of MIR methods to support these analyses. Upon identifying a current gap between high-level concepts of therapists and low-level features from existing computational methods, the paper concludes further steps towards developing computational approaches to music analysis for music therapy in an interdisciplinary collaboration. 

## 1. INTRODUCTION 

The use of music technology in the context of health and well-being is becoming increasingly important, in line with a growing interest in eHealth in medicine. Music’s affordances such as emotion regulation [1], motor coordination [2], and social interaction [3], enable a broad range of therapeutic applications. They feed into research on developing music technology for various contexts of music therapy (MT) such as for supporting motor and cognitive rehabilitation through musical biofeedback [4] and through music-based applied games [5,6], or through digital musical instruments developed for specific patient groups [7]. For a broad overview on different use cases of music technology for music therapy we refer to [8]. 

One of the main application fields envisioned for music technology in the context of health and well-being is the 

> © A. Volk, T. Veldhuis, K. Foubert and J. de Backer. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: A. Volk, T. Veldhuis, K. Foubert and J. de Backer, “Towards Computational Music Analysis for Music Therapy”, in Proc. of the 24th Int. Society for Music Information Retrieval Conf., Milan, Italy, 2023. 

support of data analysis from therapeutic sessions, including analysis and visualizations of musical structures. The computational analysis of musical structures has been one of the main research topics of music information retrieval (MIR) over the past decades. While MIR has identified the health context as one of its future challenges [9], there exist only few attempts to employ MIR methods for the analysis of musical structures in the context of MT to date [10–15]. The goal of this paper is to provide an introduction and overview on how MIR methods for computational music analysis can be of use for active music therapy (employing music making), specifically for analysing musical improvisations from therapy sessions to support music therapists. 

The contributions of this paper are threefold: First, it provides an overview of the different contexts in which music therapists analyse musical material from improvisations, and of their analytical approaches (Section 2). Second, it identifies and describes different scenarios in MT which can benefit from computational methods on music analysis. (Section 3). Third, it identifies a current gap between high-level concepts of therapists and low-level features of current computational approaches, and concludes collaboration perspectives for MIR and MT researchers on developing computational approaches to musical structure analysis of clinical improvisations (Section 4). 

## 2. OVERVIEW ON MUSIC THERAPY 

## 2.1 What is music therapy? 

The American Music Therapy Association describes music therapy (MT) as "the clinical and evidence-based use of music interventions to accomplish individualized goals within a therapeutic relationship by a credentialed professional who has completed an approved music therapy program" [16]. In a music intervention, therapists create musical experiences in a holistic manner involving the patient’s cognition, emotion, movement and social interaction, to approach issues faced by their patients. Music therapists theorize that musical processes are correlated with psychological processes [17, 18]: a musical change can indicate a change in the patient’s inner state or in the interrelation between the patient and others. For instance, if a patient with ADHD learns to focus during MT, or a patient with Parkinson learns to have more control over their body while playing music, these improvements can be generalizable to other areas in their lives, because of the interdependence of human functioning [17]. For an overview on the 

247 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 



<!-- Start of picture text -->
Forms Receptive Active<br>e.g. Guided<br>Methods Imagery Improvisation Singing/playing Composition<br>and Music existing songs & songwriting<br>Initial Finding Enhancing<br>Application areas clinical Monitoring Moments creative<br>assessment process Of Interest potential<br><!-- End of picture text -->

Figure 1. Main forms and methods of music therapy with application areas for computational music analysis. This paper focuses on the areas depicted by coloured blocks. 

various affordances of music for therapeutic use, and clinical and non-clinical contexts of music intervention see [8]. 

## 2.2 Active music therapy 

MT is divided into active (music making) and receptive (music listening) MT [19], see Figure 1. A common receptive method is called Guided Imagery and Music (GIM) [20], in which the patient listens to music in a relaxed state. The therapist guides the patient in bringing up the imagery that emerges from their inner process in response to the music, to explore their inner conflicts. 

In active MT, creative methods such as improvisation, composition and songwriting are employed, as well as recreative methods such as singing an existing song. Creative methods are used to unravel underlying psychological patterns [21]. For instance, if the patient acts mainly as the follower in the interaction with the therapist during a musical improvisation (i.e. only the therapist initiates changes in the music), this behaviour can help to unravel interaction patterns and corresponding associations in daily life interactions of the patient. 

In improvisation methods, the patient plays or sings music that they are creating themselves, either alone, with the therapist or in a group. This paper focuses on the setting of therapist and patient playing together. During a MT session, the therapist is focused on creating the music together with the patient (and the verbal evaluation of it), using musical interventions, such as changes in one or more musical parameters like timbre, dynamics, or timing, to encourage changes in the playing style of the patient. After the session, the therapist listens to the recording of the session and seeks to answer questions such as: In what way does the patient interact? Where did it feel like we were in a flow together (instead of the patient just playing for themselves) and what type of intervention caused this? In which musical parameters is the patient very rigid and what interventions change that? The therapist then seeks to draw parallels to other aspects of the patient’s life and could ask the patient in the next session if the way they interact and react to the music is the same in other situations in their life. After this verbal reflection, these habits can be further explored when improvising again. In this way, therapist and patient try to slowly break out of typical habits in the process of consecutive MT sessions. 

In composition methods, the patient uses their impro- 

visations to subsequently compose music. This could be done for example by starting with a musical improvisation, then selecting from the improvisations the parts or motifs the patient finds most interesting to use in a composition, then improvising again using these motifs, and so forth, hence employing an iterative approach. This fosters interpersonal trust through a joint process working towards an explicit artistic product [22]. In song writing, the use and analysis of lyrics is important, in composition the focus is on using musical parameters and structure. 

## 2.3 Analysis of music therapy improvisations 

There exist many different approaches to analyse MT sessions. In some of them, therapists analyse only the behaviour of the patient, and not the created music. Approaches that do analyse musical structures are called music-centered approaches, such as the Nordoff-Robbins method [23, 24]) and the so-called psychodynamic approach [25]. This paper focuses on the psychodynamic approach, which suggests that producing music can help accessing the unconscious mind such that the patient’s underlying issues will surface within a musical improvisation. While analysing musical structures can be useful in all MT methods and approaches, e.g. in receptive methods pattern discovery could be helpful to investigate whether specific patterns contribute to what patients prefer to listening to in specific contexts, we will focus in this paper on active, creative MT methods (see Figure 1). 

Bruscia, one of the pioneers for analysis of MT improvisations (MTI), created the so-called Improvisation Assessment Profiles (IAPs) [26], for which the therapist fills out questionnaires based on their observations. The IAP consists of six different profiles (called Autonomy, Integration, Tension, Variability, Salience and Congruence). For example, the Autonomy profile explores the intermusical relationship between patient and therapist, which could show that the patient is a leader or a follower, where the patient does or does not initiate changes in the music when playing together. The therapist can observe this relationship in different musical dimensions, such as in rhythm, melody, or harmony, but also in lyrics [27]. The Tension profile shows how much tension is created through different aspects of the music, relating to questions such as: is the tempo or modality calm, or tense [28]? For a detailed description of Variability, Salience, and Congruence, we refer to [17,28]. 

248 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

Therapists typically do not use all profiles and dimensions, but focus on one profile and fill out the questionnaire for all musical dimension or analyse one musical dimension in all six profiles [10]. They choose the profile and parameters based on the context: for instance, with MT for a child with ADHD, it could be relevant to analyse the presence of hyper-activity and how this changes over time, for which the therapist could use the Tension profile. 

The profiles describe high-level concepts from Bruscia [17] that require fine-grained descriptions on how they might relate to concepts of musical structure for MIR researchers. For instance, when can a tempo be described as tense? According to [10, 29, 30], there exists a variety of other methods for analysing MTI, see e.g. [24, 31–33], which all address various high-level MT concepts (such as autonomy or tension). In general, these analyses are carried out by the therapist after the MT session by listening to the recorded music, using different analytical methods and the implicit musical knowledge of the therapist. There exists no systematic research on how music therapists use the different music analysis methods in their practice, as music analysis methods in MT are a particularly underresearched area according to [34]. 

## 3. APPLICATION AREAS OF COMPUTATIONAL MUSIC ANALYSIS IN MT IMPROVISATIONS 

Computational methods for music analysis can be employed for several areas within the MT domain. In this section, we describe for the creative methods within active MT (namely improvisation, composition and songwriting) the following different application areas: initial clinical assessment; monitoring process; finding of so-called Moments of Interests; and enhancing the creative potential of patients within composition processes. 

## 3.1 Psychological Assessment 

Psychological assessment is the collection and analysis of information of a patient, resulting in hypotheses about the nature and causes of a patient’s personality, condition, resources and potentials. In the context of MTI, the information includes musical data. 

Initial clinical assessment. Hypotheses which are formed in the psychological assessment are used to determine an effective treatment program [10], considering the skills the patient currently has and what kind of therapy would fit them. Data gathered in the psychological assessment during the first therapy session is used to determine if the patients’ symptoms are consistent with the diagnostic criteria for a specific mental disorder [35]. Computational analyses of the improvisations in the first therapy session can support the initial clinical assessment. For instance, computationally analysing musical timing parameters of clinical improvisations can be promising in diagnosing Borderline Personality Disorder [14]. 

Monitoring process. Therapists use the data gathered with psychological assessment in later stages of the therapy for monitoring the process of the patient during treat- 

ment, such as for detecting any form of progress or development of the patient. One existing approach for assessing this process is the so-called microanalysis [30] which focuses on small changes in social, musical, and emotional behaviour and experiences within one MT session. A computational tool could assist in performing the microanalysis on the musical content on aspects such as identifying musical dimensions of the patient’s improvisations that, for instance, contain many repetitions for assessing the degree of rigidity in the playing style; identifying aspects of interventions of the therapist that caused changes in the patient’s playing style on a micro level; determining the dimensions which had the greatest influence on the musical change observed in the improvisation. Gathering these insights over different sessions helps to establish what is typical of a patient’s improvisational style and how it changes over time as a result of the therapeutic interventions. 

Moments Of Interest. Effects of MT are often seen in specific moments within one musical improvisation session. When carrying out psychological assessment, therapists seek to identify these specific moments which can be turning points in the development of a patient. The focus of the therapist’s analysis is to identify the so-called Moments of Interest (MOIs) [21], though there exist many other terms for MOIs, such as meaningful moments [36], pivotal moments [37], and present moments [38]. 

MOIs are chosen by therapists based on what they recognise as an important change [30]. It could be a mistake (e.g. patient accidentally plays an unintentional note), a mis-attunement between therapist and patient (e.g. patient does not listen to the therapist’s playing which leads to unsynchronized notes), a refreshing new harmonic chord, etc. The musical events right after this moment are also of interest, since the therapist notices if the change leads indeed to something new within the improvisation (e.g. if a moment of interaction occurs between patient and therapist where they dissolve the mistake or continue on the new chord). MOIs are not described by one single form of musical change, different musical elements could be of importance in the identification of MOIs for individual diseases and patients. For instance, for patients with psychosis it could be an important change if they stop playing repetitively [39], and for borderline patients it could be an important change if they start alternating between leading and following the therapist in the improvisation [40]. 

## 3.1.1 Case study: playing styles for psychosis patients 

A specifically interesting example for the potential application of computational music structure analysis, is the identification of different playing styles within MTI of patients with psychosis, including the finding of specific MOIs, namely Moments of Synchronicity (MOS). The spectrum of different playing styles as identified in [41] ranges from so-called sensorial play to complete musical form. In between arise Moments of Synchronicity. 

Sensorial play describes a style consisting of repetitive and monotonous, or chaotic and fragmented play, with a lack of phrasing, silences and dynamics. This style is typ- 

249 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

ical for patients with psychosis who are perceptually and emotionally detached from their improvisation and are not really engaging in the music, leading to an absence of interaction between patient and therapist. Typical characteristics of sensorial play are, e.g., random playing (tonal and atonal), and a significant lack of variation. 

Musical form denotes a playing style that is situated on the other end of the range of observed playing styles in patients with psychosis compared to sensorial play. It arises from an inter-subjective phenomenon between patient and therapist, where both engage in a musical interaction. They experience being autonomous and equal, and are able to introduce their own new musical ideas to the improvisation. It is characterized as an improvisation where dynamical differentiation, pulse, phrasing, pauses, repetition, variation, rhythmic and melodic themes, and especially interaction between players can be observed. A clear beginning, ending and development can be identified. 

Moments of Synchronicity (MOS). For patients with psychosis, the goal is to progress from sensorial play to musical form during several therapy sessions. In between, MOS between patient and therapist need to be established. These are short moments where both players have a shared feeling of an autonomous and free playing style, constituting a moment of musical interaction. Often MOS are fuelled by interventions from the therapist. In these moments, attunement/synchronicity in the musical parameters of the patient and therapist can be observed and some variation, dynamics and phrasing emerge. A pulse, combined with accents in the meter, are shared. MOS enrich the therapeutic relationship, creating moments of trust, which enable the patient to take more risks in the music playing, which in turn leads to changes in the patient. MOS are the most basic form of a MOI; after these first interactions, new interactions can emerge (see [41,42] for a detailed descriptions of the playing styles and MOS). 

In sum, MOS denote specific MOIs for patients with psychosis, marking their transition from sensorial play to musical form. Recognizing these different playing styles identified by the extent as to how much musical structures are present in a MTI, delivers an interesting case study for MIR on musical structure analysis and pattern discovery. 

## 3.2 Enhancing the creative potential for composing 

The composition methods for enhancing the creative potential of patients as part of active music therapy (see Figure 1) offer a particularly interesting field of application for automatic pattern discovery. For creating compositions, patients start with improvising music. Afterwards, the patient and therapist listen to the music together and seek to find parts that the patient would like to use for composing their own musical piece. The therapist writes down the motifs they hear in musical notation, which can be time consuming. A pattern discovery tool could be used to identify and highlight all moments where the patient repeated their motifs, and preferably these motifs could be automatically transcribed to musical notation so that in the next phase of the composition these motifs could be used immediately. 

## 4. DEVELOPING MIR METHODS FOR MT 

## 4.1 Existing Computational Approaches in MT 

A number of computational approaches have been developed to support psychological assessment in MTI, which we summarize in this section. According to [10,12], Computer Aided Music Therapy Analysis System (CAMTAS) was the first attempt to organize and analyse audio and video data specifically from MT. Developed during the mid-90s, it was used for uploading recorded data and playing back audio and video files simultaneously. Another annotation tool, the so-called Music Therapy Analysing Partitura (MAP) [29], helps to annotate events in MT based on therapist’s manual transcriptions. The therapist can annotate the auditory material from a session, including the music itself, but also e.g. talking, silence, crying, and laughing, using a visual format with fixed graphical codes, allowing the therapist to view the content of one improvisation or over a whole session. Both CAMTAS and MAP rely on manual work by the therapist without any automatic detection of events from music recordings, hence using these tools is rather time-consuming [10]. 

Computational tools for MTI which analyse the musical content are the Music Therapy Logbook [12] and the Music Therapy Toolbox (MTTB) for MatLab [15,27,43]. The Music Therapy Logbook was developed in collaboration between MIR and MT researchers. It can be used to gather evidence of changes in a patient‘s and therapist‘s use of music over time for psychological assessment. In a proofof-concept study using simulated MTI where one expert would improvise in the role of the patient and the other as the therapist [12], existing MIR techniques e.g. for the detection of tempo changes or the identification of rhythmic patterns, have been employed. It was tested whether computational methods can assist in evaluating whether therapist’s tempo changes are effective in increasing the patient’s tempo flexibility. While it was possible to identify, for instance, call and response type of play between therapist and patient, it was concluded that addressing higherlevel concepts about musical interactions with computational means has yet to be fully explored in the future. 

The MTTB tool takes MIDI files of therapist and patient as input and automatically extracts musical features, which it outputs into graphs depicting both the therapist and patient over time. The musical features in the MTTB are based on the Autonomy profile of the IAP [27] described in section 2.3. For instance, the density graph is calculated by averaging the number of notes played in a given time window. Since theory suggests that increasing musical density is a sign of increased arousal and therefore increased emotional and physiological density [44], density should be clinically relevant [43]. By manually reading and interpreting the two graphs of the therapist and patient, the role-relationship can be determined for the feature. A pilot study [45] investigated how the MTTB could support clinical assessment from improvisations when combined with subjective experiences of the participants, delivering first insights on how this tool might be used in the future 

250 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

for investigating Bruscia’s improvisation techniques, such as imitation and synchronisation through specific musical parameters. The MTTB is still under development. 

For monitoring the process of patients over several therapy sessions with computational methods, the concept of Musical Profiling was introduced in [10], comprising three parts: Typical Performance for establishing a patient’s individual typical playing style, Temporal Evolution for measuring the changes in different features in the improvisations over some time or over different sessions, and Individual Tendencies, measuring relations between features that are specific to that patient. In a case study with 6 participants, they used e.g. averages of the features of duration, note count, tempo, pulse clarity, dynamic centroid, and pitch centroid, to characterize a typical performance. The Musical Profiling concept is intended to contribute to establishing a systematic method of measuring and representing musical processes in improvisations in order to formalize assessment methods. To the best of our knowledge, this concept has not yet been set into practice. 

In sum, there exist promising first steps in developing computational approaches to support the psychological assessment of the therapist when analysing clinical improvisations. They are not yet ready for use in clinical practice. Linking high-level MT concepts (such as moments of interest, tension, salience) to elements of the musical structure that can be extracted with computational features from the music, is as of today not a solved problem (see [11,46] for studies on linking computational features to clinical improvisations). Moreover, from the perspective of their practical use, tools like MATLAB are not easy to use for all music therapists, and while MIDI is useful in the MT research context, most clinical contexts work with audio. 

## 4.2 Musical structure analysis and pattern discovery 

For analysing the musical content of clinical improvisations, MIR methods for musical structure analysis [47–51] as well as pattern discovery [52–64] could be of potential use in the different application fields within MT described in section 3. Techniques to identify coherent segments using concepts such as homogeneity, novelty, repetition, or regularity, developed in music structure analysis [47, 48], might be useful for describing structures emerging in clinical improvisations. Pattern discovery methods could support the identification of different playing styles such as sensorial play or musical form, taking into account the amount and kind of repetition and variation in musical patterns identified. However, these methods have been developed for different scenarios and styles, such as for popular music, jazz, classical music or folk songs. It needs to be explored in how far these techniques need to be adapted for improvisations in the MT context; e.g. in [13] it has been shown that repeated musical patterns identified in MTI were rather different from patterns typically investigated in musicological analyses of compositions and corpora. 

Apart from the difference in the musical material, the analysis process of music therapists differs from musicological investigations of compositions. Typically, the 

therapist has participated in the improvisation and analyses afterwards the recorded musical material, taking into account their own experience during the improvisation, which might already steer the attention to certain elements of the structure. This is different from a musicological analysis of musical material that has been produced by other musicians (or musical novices). 

For adapting MIR methods to the context of MT, the typical high-level concepts addressed by music therapists need to be investigated and deconstructed collaboratively in order to establish how these concepts are manifested in musical features and structures that can be described by computational means. Proof-of-concept studies such as [10, 12] provide a promising start into applying MIR features for analysing MTI. Yet, in order to develop meaningful computational features for the working context of therapists, their implicit knowledge employed in analysing clinical improvisations needs to be made more explicit. One example is given in [34] employing interviews with therapists to determine implicit and explicit knowledge in music analysis of MTI. Working towards the explicating of this implicit knowledge through collaboration would also contribute to establish how much agreement exists between different therapists using the same terminology and analysis methods. This constitutes an important step not only for developing computational methods, but also in developing assessment methods that support the development of evidence-based methods in MT. 

## 4.3 Collaboration perspectives for computational approaches to musical structure in MT improvisations 

In MIR, there exists a strong tradition of collaboration with domain experts on investigating specific musical concepts for enabling computational modeling, such as on Leitmotifs [65–67], on cadences [68–70], on similarity of folk songs belonging to a tune family [71, 72], or on melodic schemata and patterns of a certain musical style [54, 55, 72–74]. The establishment of data sets and annotations of experts regarding these concepts has been a crucial factor for enabling collaboration. We expect this to be a necessary step also for developing computational approaches to music analysis for MTI. In the following we indicate examples for the envisioned collaboration for the applications described in section 3. 

Initial clinical assessment. For developing computational methods for the analysis of improvisations within the initial clinical assessment, data sets and descriptions of typical playing styles for specific patient groups need to be established. For instance, an overview of which profiles and musical dimensions therapists typically select for specific patient groups within their manual assessment using IAPs, could serve as a starting point for explicating therapists’ knowledge on how to describe playing styles using musical features. In the future, once computational methods have been established, they could support therapists to initially scan all profiles with the help of computation, instead of manually selecting a few, ensuring that nothing has been overlooked before concentrating on selected aspects. 

251 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

Monitoring process. Comparing improvisations from different sessions in order to monitor the therapeutic process requires a data-rich approach to musical structure for which computational methods are specifically apt. The concept of Temporal Evolution within Musical Profiling [10] is a first step to monitor process, using low-level musical features such as note count or pitch centroid. For getting closer to the MT practice, the high-level concepts of music analysis in MT need to be connected to appropriate models in MIR, such as identifying recurring patterns and the amount of repetitiveness and variation observed in these patterns, and the comparison of features over time. 

Finding MOIs and identifying playing styles. For an overview on envisioned steps in the collaboration between MIR and MT researchers on identifying MOIs as important changes in the therapeutic process, we refer to the discussion in [8] on the creation of datasets and annotations, and the use of automatic pattern discovery and information theory. For the specific case of MOS as a progress from sensorial play to musical form (see Section 3.1.1), the identification of emerging synchronicity in the musical parameters of patient and therapist requires the modeling of musical structure as emerging from an interaction. For instance, MIR models on rhythm and meter could be adapted for detecting the establishment of a shared pulse in MOS, requiring a data collection with improvisations exhibiting different degrees of stability and variability in temporal structures with annotations on MOS as identified by therapists. For distinguishing different playing styles, such as sensorial play and musical form as described in section 3.1.1, computational methods for identifying musical structure, repetition and variation along different musical dimensions, can be employed. 

Enhancing the creative potential of patients for composing. Automatic pattern discovery has been successfully employed in MIR for the automatic generation of music [75, 76]. For supporting the composition method as part of active MT, pattern discovery could assist in enhancing the creativity of the patient in the iterative process of generating a composition from improvisations. For discovering appropriate motifs in the patient’s improvisations, the methods need to be able to find non-exact matches that might be perceptually meaningful. Appropriate visualization methods for displaying identified matches could support patients in choosing which matches they consider meaningful to work with. Automatic music generation systems such as [77] could be used to explore whether they might support enhancing the patient’s creativity in MT (see the discussions in [78] on AI and musical creativity, and [8] on automatic music generation specifically for MT). 

We conclude the following steps for establishing the collaboration between MIR and MT on developing computational methods for music analysis of improvisations: 

- Investigate music analysis methods of therapists and create data sets with clinical improvisations and music analytic annotations from therapists. Using simulated therapy sessions as in [12,45] letting therapists imitate typical playing styles of patients is a first step, yet its useful- 

ness is limited by providing only stereotypical examples. 

- Establish a catalogue of typical intervention methods of therapists in clinical improvisations as a first step on finding appropriate musical features for developing analytical methods to musical interactions in MTI. 

- Explore computational approaches from MIR for the automatic detection of musical structures in MTI; start with assessing existing MIR features, and determine suitable adaptations for supporting therapists’ analytical concepts. Taking into account the granularity of music information required, determine in which contexts symbolic and/or audio formats are appropriate. 

- Initiate case studies: For exploring the emergence of musical structures in MTI, identifying different playing styles of patients with psychosis as in Section 3.1.1 can provide a particular interesting starting point for collaboration once datasets are established, since these playing styles are well described in the MT literature. 

- Assess how much therapists (dis)agree in their individual intervention and analysis styles. Investigating the agreement between therapists requires the building of dedicated annotation tools and methods to measure agreement between annotators, such as in [79–82]. 

- Assess how the intuitive knowledge of the music therapist on their subjective experience in the improvisation can be combined with and enhanced by the objective analysis of the musical material through computation, to support therapists in their daily work, and to further establish evidence-based treatments in MT. 

- Consider aspects of usability, including considerations from HCI, for developing appropriate tools for the daily practice of therapists; see [8, 42] for some general considerations on developing tools for MT. 

## 5. CONCLUSION 

Clinical improvisation from music therapy provide interesting and novel musical data for developing MIR methods for music structure analysis and pattern discovery, aiming to support therapists in their daily work. Interdisciplinary efforts between MIR and MT researchers need to be invested to close the gap between high-level concepts of music analysis used by therapists, and low-level features of current computational approaches to analyse MTI. Investigating music analysis methods employed by therapists, including the explication of therapists’ implicit musical knowledge and the assessment of the agreement between different therapists, constitutes a crucial step for developing computational tools for MT. Specifically important herein is the establishing of data sets with clinical improvisations for different application areas, such as for initial clinical assessment, including different patient groups and catalogues of typical interventions of therapists. Creating these data sets through interdisciplinary efforts will not only prepare the ground for the appropriate computational modeling of music structures in MTI, but also to a better understanding of music analysis methods in MT, ultimately contributing to ongoing research on establishing evidence-based methods in MT. 

252 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

## 6. REFERENCES 

- [1] K. S. Moore, “A systematic review on the neural effects of music on emotion regulation: Implications for music therapy practice,” Journal of Music Therapy, vol. 50, no. 3, p. 198–242, 2013. 

- [2] S. Dalla Bella, C. E. Benoit, N. Farrugia, M. Schwartze, and S. A. Kotz, “Effects of musically cued gait training in Parkinson’s disease: Beyond a motor benefit,” Annals of the New York Academy of Sciences, vol. 1337, pp. 77–85, 2015. 

- [3] W. L. Magee and C. Bowen, “Using music in leisure to enhance social relationships with patients with complex disabilities,” NeuroRehabilitation, vol. 23, pp. 305–311, 2008. 

- [4] P. Kantan, E. G. Spaich, and S. Dahl, “A Technical Framework for Musical Biofeedback in Stroke Rehabilitation,” IEEE Transactions on Human-Machine Systems, vol. 52, no. 2, pp. 220–231, 2022. 

- [5] V. Bégel, A. Seilles, and S. Dalla Bella, “Rhythm workers: A music-based serious game for training rhythmic skills,” Music & Science, vol. 1, pp. 1–16, 2018. 

- [6] K. Agres and D. Herremans, “Music and motiondetection: A game prototype for rehabilitation and strengthening in the elderly,” in International Conference on Orange Technologies, 2017, pp. 95–98. 

- [7] Z. Vamvakousis and R. Ramirez, “The eyeharp: A gaze-controlled digital musical instrument,” Frontiers in Psychology, vol. 7, 2016. 

- [8] K. R. Agres, R. S. Schaefer, A. Volk, S. van Hooren, A. Holzapfel, S. Dalla Bella, M. Müller, M. de Witte, D. Herremans, R. Ramirez Melendez, M. Neerincx, S. Ruiz, D. Meredith, T. Dimitriadis, and W. L. Magee, “Music, computing, and health: a roadmap for the current and future roles of music technology for health care and well-being,” Music & Science, vol. 4, pp. 1– 32, 2021. 

- [9] X. Serra, M. Magas, E. Benetos, M. Chudy, S. Dixon, A. Flexer, E. Gómez, F. Gouyon, P. Herrera, S. Jordà, O. Paytuvi, G. Peeters, J. Schlüter, H. Vinet, and G. Widmer, Roadmap for music information research. Creative Commons BY-NC-ND 3.0 License, 2013. 

- [10] N. Letul˙e, “Musical Profiling: Towards a ComputerBased Analysis of Clinical Improvisations,” Master’s thesis, Dept. of Music, Univ. of Jyväskylä, Jyväskylä, Finland, 2014. 

- [11] G. Luck, K. Riikkilä, O. Lartillot, J. Erkkilä, P. Toiviainen, A. Mäkelä, K. Pyhäluoto, H. Raine, L. Verkila, and J. Värri, “Exploring relationships between level of mental retardation and features of music therapy improvisations: A computational approach,” Nordic Journal of Music Therapy, vol. 15, no. 1, pp. 30–48, 2006. 

- [12] E. Streeter, M. E. Davies, J. D. Reiss, A. Hunt, R. Caley, and C. Roberts, “Computer aided music therapy evaluation: Testing the Music Therapy Logbook prototype 1 system,” The Arts in Psychotherapy, vol. 39, no. 1, pp. 1–10, Feb. 2012. 

- [13] C. Anagnostopoulou, A. Alexakis, and A. Triantafyllaki, “A Computational Method for the Analysis of Musical Improvisations by Young Children and Psychiatric Patients with No Musical Background,” in Proceedings of the 12th International Conference on Music Perception and Cognition and the 8th Triennial Conference of the European Society for the Cognitive Sciences of Music, E. Cambouropoulos, C. Tsougras, P. Mavromatis, and K. Pastiadis, Eds., Thessaloniki, 2012. 

- [14] K. Foubert, T. Collins, and J. De Backer, “Impaired maintenance of interpersonal synchronization in musical improvisations of patients with borderline personality disorder,” Frontiers in Psychology, vol. 8, Apr. 2017, Art. no. 537. 

- [15] J. Erkkilä, “Music Therapy Toolbox (MTTB) – An Improvisation Analysis Tool for Clinicians and Researchers,” in Microanalysis in Music Therapy: Methods, Techniques and Applications for Clinicians, Researchers, Educators and Students. Jessica Kingsley Publishers, 2021, ch. 10, pp. 134–148. 

- [16] American Music Therapy Association. "Setting the record straight: What music therapy is and is not." Musictherapy.org. Accessed at Aug. 23, 2021. [Online]. Available: https://www.musictherapy.org/ about/musictherapy/ 

- [17] K. E. Bruscia, Defining Music Therapy, 3rd ed. Gilsum, NH, USA: Barcelona Publishers, 2014. 

- [18] H. Smeijsters, Sounding the self: analogy in improvisational music therapy. Gilsum, NH, USA: Barcelona Publishers, 2005. 

- [19] B. L. Wheeler, Music Therapy Handbook. New York, NY, USA: The Guilford Press, 2015. 

- [20] H. L. Bonny. "Music Psychotherapy: Guided Imagery and Music". Voices.no. Accessed at Okt. 22, 2021. [Online]. Available: https: //voices.no/index.php/voices/article/view/1876/1640 

- [21] J. Fachner, “Music, moments and healing processes: Music therapy,” in The Routledge Companion to Music Cognition, R. Ashley and R. Timmers, Eds. Abingdon, UK: Routledge, 2017, ch. 1.8, pp. 89–100. 

- [22] J. De Backer, B. Sebreghts, and K. Foubert, “Composition Plus. A process-compositional approach in music therapy to empower creative potential.” Journal of Urban Culture Research, vol. 25, pp. 161–175, 2022. 

- [23] P. Nordoff and C. Robbins, Creative Music Therapy. New York: John Day, 1977. 

253 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

- [24] K. Aigen, Being in music: Foundations of NordoffRobbins music therapy. Gilsum, NH, USA: Barcelona Publishers, 1996. 

- [25] J. De Backer and J. Sutton, The Music in Music Therapy: Psychodynamic Music Therapy in Europe : Clinical, Theoretical and Research Approaches. Jessica Kingsley Publishers, 2014. 

- [26] K. E. Bruscia, Improvisational models of music therapy. Springfield, IL, USA: Charles C Thomas Publisher, 1987. 

- [27] J. Erkkilä and T. Wosch, “The Music Therapy Toolbox,” in Music Therapy Assessment: Theory, Research, and Application. London, UK: Jessica Kingsley Publishers, 2019, ch. 15, pp. 293–314. 

- [28] Nordic Journal of Music Therapy. "IAP Revisited". Njmt.w.uib.no. Accessed at Apr. 12, 2022. [Online]. Available: https: //njmt.w.uib.no/nordic-journal-of-music-therapy/ forum-online-discussions-1998-2006/iap-revisited/ 

- [29] A. Gilboa, “Nordic Journal of Music Therapy Developments in the MAP: A method for describing and analyzing music therapy sessions,” Nordic Journal of Music Therapy, vol. 21, no. 1, pp. 57–79, 2012. 

- [30] T. Wigram and T. Wosch, Microanalysis in Music Therapy: Methods, Techniques and Applications for Clinicians, Researchers, Educators and Students. London, UK: Jessica Kingsley Publishers, 2007. 

- [31] H. T. Baxter, J. Berghofer, and L. MacEwan, The individualized music therapy assessment profile: IMTAP. London, UK: Jessica Kingsley Publishers, 2007. 

- [32] M. Forinash and D. Gonzalez, “A Phenomenological Perspective of Music Therapy,” Music Therapy, vol. 8, no. 1, pp. 35–46, 1989. 

- [33] M. Langenberg, J. Frommer, and W. Tress, “A Qualitative Research Approach to Analytical Music Therapy,” Music Therapy, vol. 12, no. 1, pp. 59–84, 1993. 

- [34] N. Letul˙e, E. Ala-Ruona, and J. Erkkilä, “Professional freedom: A grounded theory on the use of music analysis in psychodynamic music therapy,” Nordic Journal of Music Therapy, vol. 27, no. 5, pp. 448–466, 2018. 

[35] Washington State University. "Module 3: Clinical Assessment, Diagnosis, and Treatment". opentext.wsu.edu. Accessed at Dec. 18, 2021. [Online]. Available: https://opentext.wsu.edu/abnormal-psych/chapter/ module-3-clinical-assessment-diagnosis-and-treatment/ 

- [36] J. Fachner, “Communicating change-meaningful moments, situated cognition and music therapy: A response to North (2014),” Psychology of Music, vol. 42, no. 6, pp. 791–799, 2014. 

- [37] M. Gavrielidou and H. Odell-Miller, “An investigation of pivotal moments in music therapy in adult mental health,” The Arts in Psychotherapy, vol. 52, pp. 50–62, Feb. 2017. 

- [38] G. Ansdell, J. Davidson, W. L. Magee, J. Meehan, and S. Procter, “From "This F***ing life" to "that’s better" . . . in four minutes: an interdisciplinary study of music therapy’s "present moments" and their potential for affect modulation,” Nordic Journal of Music Therapy, vol. 19, no. 1, pp. 3–28, 2010. 

- [39] J. De Backer and T. Wigram, “Analysis of Notated Music Examples Selected from Improvisations of Psychotic Patients,” in Microanalysis in Music Therapy: Methods, Techniques and Applications for Clinicians, Researchers, Educators and Students, London, UK, ch. 9, pp. 120–133. 

- [40] K. Foubert, B. Sebreghts, J. Sutton, and J. De Backer, “Musical encounters on the borderline. Patterns of mutuality in musical improvisations with Borderline Personality Disorder,” Arts in Psychotherapy, vol. 67, 2020, Art. no. 101599. 

- [41] J. De Backer, “Music and psychosis: A research report detailing the transition from sensorial play to musical form by psychotic patients.” Nordic Journal of Music Therapy, vol. 17, no. 2, pp. 89–104, 2008. 

- [42] T. Veldhuis, “Repeated musical patterns in music therapy analysis,” Small Project Report, Utrecht University, 2022. 

- [43] J. Erkkilä, O. Lartillot, G. Luck, K. Riikkilä, and P. Toiviainen, “Intelligent music systems in music therapy,” Music Therapy Today, vol. 5, no. 5, pp. 1–21, 2004. 

- [44] G. Husain, W. F. Thompson, and E. G. Schellenberg, “Effects of musical tempo and mode on arousal, mood, and spatial abilities,” Music perception, vol. 20, no. 2, pp. 151–171, 2002. 

- [45] A. Kurkjian, K. Skinner, and H. Ahonen, “Using music-adapted technology to explore Bruscia’s clinical techniques introduced in autism research: Pilot study,” Approaches: An Interdisciplinary Journal of Music Therapy, vol. 13, no. 2, pp. 178–204, 2021. 

- [46] G. Luck, P. Toiviainen, J. Erkkilä, O. Lartillot, K. Riikkilä, A. Mäkelä, K. Pyhäluoto, H. Raine, L. Varkila, and J. Värri, “Modelling the relationships between emotional responses to, and musical content of, music therapy improvisations,” Psychology of Music, vol. 36, no. 1, pp. 25–45, 2008. 

- [47] O. Nieto, G. J. Mysore, C.-i. Wang, J. B. Smith, J. Schlüter, T. Grill, and B. McFee, “Audio-based music structure analysis: Current trends, open challenges, and applications,” Transactions of the International Society for Music Information Retrieval, vol. 3, no. 1, 2020. 

254 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

- [48] F. Bimbot, O. Le Blouch, G. Sargent, and E. Vincent, “Decomposition into autonomous and comparable blocks: a structural description of music pieces,” in Proc. of the 11th International Society for Music Information Retrieval Conference, Utrecht, The Netherlands, 2010, pp. 189–194. 

- [49] J. Paulus, M. Müller, and A. Klapuri, “Audiobased music structure analysis,” in Proc. of the 11th International Society for Music Information Retrieval Conference, Utrecht, The Netherlands, 2010, pp. 625–636. 

- [50] J. Pauwels, F. Kaiser, and G. Peeters, “Combining Harmony-Based and Novelty-Based Approaches for Structural Segmentation,” in Proc. of the 14th International Society for Music Information Retrieval Conference, Curitiba, Brazil, 2013, pp. 601–606. 

- [51] G. Shibata, R. Nishikimi, E. Nakamura, and K. Yoshii, “Statistical music structure analysis based on a homogeneity-, repetitiveness-, and regularityaware hierarchical hidden semi-Markov model,” in Proc. of the 20th International Society for Music Information Retrieval Conference, Delft, The Netherlands, 2019, pp. 268–275. 

- [52] E. Cambouropoulos, “Musical parallelism and melodic segmentation:: A computational approach,” Music Perception, vol. 23, no. 3, pp. 249–268, 2006. 

- [53] T. Collins, A. Arzt, S. Flossmann, and G. Widmer, “SIARCT-CFP: Improving Precision and the Discovery of Inexact Musical Patterns in Point-Set Representations,” in Proc. of the 14th International Society for Music Information Retrieval Conference, 2013, pp. 549–554. 

- [54] D. Conklin, “Discovery of distinctive patterns in music,” Intelligent Data Analysis, vol. 14, no. 5, pp. 547– 554, 2010. 

- [55] D. Conklin and C. Anagnostopoulou, “Comparative pattern analysis of Cretan folk songs,” Journal of New Music Research, vol. 40, no. 2, pp. 119–125, 2011. 

- [56] R. B. Dannenberg and N. Hu, “Pattern discovery techniques for music audio,” Journal of New Music Research, vol. 32, no. 2, pp. 153–163, 2003. 

- [57] J. Forth, “Cognitively-motivated geometric methods of pattern discovery and models of similarity in music,” Ph.D. dissertation, Goldsmiths, Univ. of London, London, UK, 2012. 

- [58] B. Janssen, W. Haas, A. Volk, and P. v. Kranenburg, “Finding repeated patterns in music: State of knowledge, challenges, perspectives,” in International Symposium on Computer Music Multidisciplinary Research. Springer, 2013, pp. 277–297. 

- [59] O. Lartillot, “Automated motivic analysis: An exhaustive approach based on closed and cyclic pattern mining in multidimensional parametric spaces,” in Computational Music Analysis, D. Meredith, Ed. Springer, 2016, ch. 11, pp. 273–302. 

- [60] D. Meredith, K. Lemström, and G. A. Wiggins, “Algorithms for discovering repeated patterns in multidimensional representations of polyphonic music,” Journal of New Music Research, vol. 31, no. 4, pp. 321–345, 2002. 

- [61] O. Nieto and M. M. Farbood, “Identifying polyphonic patterns from audio recordings using music segmentation techniques,” in Proc. of the 15th International Society for Music Information Retrieval Conference, 2014, pp. 411–416. 

- [62] M. Pesek, A. Leonardis, and M. Marolt, “SymCHM—An Unsupervised Approach for Pattern Discovery in Symbolic Music with a Compositional Hierarchical Model,” Applied Sciences, vol. 7, no. 11, p. 1135, 2017. 

- [63] I. Y. Ren, H. V. Koops, A. Volk, and W. Swierstra, “In search of the consensus among musical pattern discovery algorithms,” in Proc. of the 18th International Society for Music Information Retrieval Conference, 2017, pp. 671–678. 

- [64] G. Velarde, D. Meredith, and T. Weyde, “A waveletbased approach to pattern discovery in melodies,” in Computational Music Analysis. Springer, 2016, ch. 12, pp. 303–333. 

- [65] M. Krause, M. Müller, and C. Weiß, “Towards Leitmotif Activity Detection in Opera Recordings,” Transactions of the International Society for Music Information Retrieval, vol. 4, no. 1, p. 127–140, 2021. 

- [66] K. R. Page, T. Nurmikko-Fuller, C. Rindfleisch, Weigl, R. D. M., Lewis, L. Dreyfus, and D. De Roure, “A toolkit for live annotation of opera performance: Experiences capturing Wagner’s Ring cycle,” in Proc. of the 16th International Society for Music Information Retrieval Conference, 2015, pp. 211–217. 

- [67] L. Dreyfus and C. Rindfleisch, “Using digital libraries in the research of the reception and interpretation of Richard Wagner’s leitmotifs,” in Proceedings of the International Workshop on Digital Libraries for Musicology, 2014, pp. 1–3. 

- [68] M. Rohrmeier and M. Neuwirth, “Towards a Syntax of the Classical Cadence,” in What Is a Cadence? Theoretical and Analytical Perspectives on Cadences in the Classical Repertoire. Leuven University Press, 2015, pp. 287–338. 

- [69] P. van Kranenburg and F. Karsdorp, “Cadence detection in western traditional stanzaic songs using melodic and textual features,” in Proc. of the 15th International 

255 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

   - Society for Music Information Retrieval Conference, 2014, pp. 391–396. 

- [70] L. Bigo, L. Feisthauer, M. Giraud, and F. Levé, “Relevance of musical features for cadence detection,” in Proc. of the 19th International Society for Music Information Retrieval Conference, 2018, pp. 671–678. 

- [71] A. Volk and P. van Kranenburg, “Melodic similarity among folk songs: An annotation study on similaritybased categorization in music,” Musicae Scientiae, vol. 16, no. 3, pp. 317–339, 2012. 

   - [81] A. Flexer, T. Lallai, and K. Rašl, “On Evaluation of Inter- and Intra-Rater Agreement in Music Recommendation,” Transactions of the International Society for Music Information Retrieval, vol. 4, no. 1, pp. 182– 194, 2021. 

   - [82] H. V. Koops, W. B. de Haas, J. A. Burgoyne, J. Bransen, A. Kent-Muller, and A. Volk, “Annotator subjectivity in harmony annotations of popular music,” Journal of New Music Research, vol. 48, no. 3, pp. 232–252, 2019. 

- [72] P. Boot, A. Volk, and W. B. de Haas, “Evaluating the role of repeated patterns in folk song classification and compression,” Journal of New Music Research, vol. 45, no. 3, pp. 223–238, 2016. 

- [73] R. Caro Repetto, R. Gong, N. Kroher, and X. Serra, “Comparision of the singing style of two Jingju schools,” in Proc. of the 16th International Society for Music Information Retrieval Conference, Malaga, Spain, 2015, pp. 507–513. 

- [74] V. I. S. Gulati, J. Serrà and X. Serra., “Mining Melodic Patterns in Large Audio Collections of Indian Art Music,” in Proc. of the Tenth International Conference on Signal-Image Technology and Internet-Based Systems, 2014, pp. 264–271. 

- [75] D. Herremans and E. Chew, “MorpheuS: generating structured music with constrained patterns and tension,” IEEE Transactions on Affective Computing, vol. 10, no. 4, pp. 510–523, 2019. 

- [76] D. Conklin and G. Maessen, “Generation of melodies for the lost chant of the mozarabic rite,” Applied Sciences, vol. 9, no. 20, 2019. [Online]. Available: https://www.mdpi.com/2076-3417/9/20/4285 

- [77] F. Pachet, “The Continuator: Musical Interaction With Style,” Journal of New Music Research, vol. 32, no. 3, pp. 333–341, 2003. 

- [78] B. L. T. Sturm, A. L. Uitdenbogerd, H. V. Koops, and A. Huang, “Editorial for TISMIR special collection: AI and musical creativity,” Transactions of the International Society for Music Information Retrieval, vol. 5, no. 1, pp. 67–70, 2022. 

- [79] D. Tomaševi´c, S. Wells, I. Y. Ren, A. Volk, and M. Pesek, “Exploring annotations for musical pattern discovery gathered with digital annotation tools,” Journal of Mathematics and Music, vol. 15, no. 2, pp. 194–207, 2021. 

- [80] A. Flexer and T. Grill, “The Problem of Limited Interrater Agreement in Modelling Music Similarity,” Journal of New Music Research, vol. 45, no. 3, pp. 239– 251, 2016. 

256 

