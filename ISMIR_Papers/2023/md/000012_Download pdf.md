---
paper_id: "000012"
year: 2023
title: "Download pdf"
source_url: "https://zenodo.org/record/10265237/files/000012.pdf"
---

# TAPTAMDRUM: A DATASET FOR DUALIZED DRUM PATTERNS 

Behzad Haki Bła˙zej Kotowski Cheuk Lun Isaac Lee Sergi Jordà 

Music Technology Group, Universitat Pompeu Fabra, Barcelona, Spain 

```
behzad.haki@upf.edu,blazej.kotowski@upf.edu,clilee@connect.ust.hk,sergi.jorda@upf.edu
```

## ABSTRACT 

Drummers spend extensive time practicing rudiments to develop technique, speed, coordination, and phrasing. These rudiments are often practiced on "silent" practice pads using only the hands. Additionally, many percussive instruments across cultures are played exclusively with the hands. Building on these concepts and inspired by Einstein’s probably apocryphal quote, "Make everything as simple as possible, but not simpler," we hypothesize that a dual-voice reduction could serve as a natural and meaningful compressed representation of multivoiced drum patterns. This representation would retain more information than its corresponding monotonic representation while maintaining relative simplicity for tasks such as rhythm analysis and generation. To validate this potential representation, we investigate whether experienced drummers can consistently represent and reproduce the rhythmic essence of a given drum pattern using only their two hands. We present TapTamDrum: a novel dataset of repeated dualizations from four experienced drummers, along with preliminary analysis and tools for further exploration of the data. 

## 1. INTRODUCTION 

## 1.1 Motivation 

Music is a fundamental aspect of human culture, and rhythm is a central element of musical expression. Many different cultures have developed complex and sophisticated rhythmic traditions that are deeply rooted in their history, language, and social structures [1]. Representing music, and more specifically rhythm, in a symbolic form is crucial for a wide range of purposes, including communication, and preservation of musical traditions. Moreover, symbolic representations of music are essential for enabling the efficient processing and manipulation of musical data by computers, enabling new possibilities for music analysis and creation. However, representing complex rhythmic patterns in a notation system that accurately captures their essence and feeling can be a challenging task, 

> © F. Author, S. Author, and T. Author. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: F. Author, S. Author, and T. Author, “TapTamDrum: A Dataset for Dualized Drum Patterns”, in Proc. of the 24th Int. Society for Music Information Retrieval Conf., Milan, Italy, 2023. 

particularly when the rhythms are highly complex or involve multiple layers of interlocking patterns. 

Some attempts on representing percussion in a domain specific-way have been made, initially focusing on a single stream of onsets [2]. In [3], Toussaint offers a holistic analysis of rhythmic patterns, with an approach largely centred around monotonic representations. Representing a rhythmic pattern in a monotonic stream of offsets has indeed proven to be successful for some tasks like transforming a sequence of taps to a fully-orchestrated percussive pattern in GrooVAE [4]. However, while a rhythmic pattern reduced to a monotonic stream of its onsets retains part of its horizontal structure related to temporality, it also loses its vertical quality, which is related to the interplay between different voices [3]. As a result, a monotonic pattern transformation fails to capture the complete essence of a multi-voice rhythm, as noticed by Lartillot and Bruford [5]. Inspired by Einstein’s probably apocryphal quote, "Make everything as simple as possible, but not simpler," in this work we hypothesise that a dual-voice reduction could serve as a more natural and meaningful compressed representation of multi-voiced drum patterns than its monotonic equivalent, and that this representation could preserve some quality related to the interaction or tension between instruments, while maintaining relative simplicity for tasks such as rhythm analysis and generation. 

The rationale behind this approach can also be related to the role of the human motor system in rhythm perception. The importance of the motor system in rhythm creation and perception is rooted in the fact that many musical rhythms are based on movements that involve two limbs. It was previously documented that the synchronisation of movement to a musical pulse happens automatically, whether of the hand movements [6,7], walking [8], or dancing [9]. A number of studies prove that motor areas of the brain play a significant role in beat perception and synchronisation. As Patel and Iversen argue in [10], the ability to coordinate two limbs in a synchronised and precise manner is essential for playing musical instruments and dancing to music. This is exemplified by the tradition of drumming, which typically involves striking a drum with two hands. The renowned drummer Jaki Liebezeit, even simplified his drum kit to only require two hands to play, and developed a rhythmic notation system called E-T that employs only two symbols to represent any rhythm, accommodating any musical situation [11]. Thus, the use of two limbs in music and rhythm is not only a fundamental aspect of motor 

114 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

coordination, but also a practical consideration in the representation and communication of musical rhythms. 

A bell pattern is a two-voiced pattern frequently used in West African music, which is usually used as a key pattern to suggest a temporal organisation for different instruments and musicians [12]. This pattern is used from the Sub-Sahara, to West Africa, to the central lands of Congo and the Nyusa lands in Southeast Africa [13]. Agawu [14] claims that the notoriously complex rhythms in West African music can be represented with a bell pattern, which could usually be played with two-voiced percussion instruments. This African tradition migrated to the new world during the colonial period. Rooted in the Caribbeans, the Clave cross-rhythm also splits the beat into two voices, one regular beat and another irregular [15]. 

Additionally, subjective rhythmization is a widely recognized phenomenon in auditory perception [16], which occurs when individuals are exposed to monotonous auditory stimuli such as the ticking of a clock. Rather than hearing a simple "tick-tick-tick" pattern, our brains transform the sound into a more complex rhythmic sequence, such as "tick-tock-tick-tock," comprising two distinct parts. This naturally occurring cognitive process enhances the subjective perception of rhythm and makes the stimulus more engaging and dynamic to the listener. The concept of rhythm streams, which is linked to the theory of auditory streaming, is examined by Witek et al. [17]. Their research reveals that the addition of a single instrumental component to a monotonic rhythmic pattern can greatly influence its perceived rhythm, whereas the addition of another component to a two-instrument pattern has a discernible impact only in certain instrumentation contexts. Finally, Lartillot and Bruford [5] argue that any rhythm can be reduced to an oscillation between two states: high and low. Their rule-based system transforms multi-voice patterns into a monotonic stream of timed events representing the toggles between the states and their accentuations. 

All the aforementioned evidences provide support for the initial hypothesis that simplified, dual-voice representations of multi-voice rhythmic patterns may be adequate in communicating both the vertical and horizontal characteristics of rhythm. 

## 1.2 Rhythm Pattern Dualization 

To formalize this idea, we introduce the novel concept of dualization of rhythm patterns. The task of rhythm dualization could be defined as the transformation of any multivoice rhythmic pattern to another pattern composed of a maximum of two voices, while preserving the coherence and the perceptual essence of the original rhythm as much as possible. Dualization involves simplifying and highlighting the most essential features of complex rhythmic patterns. This dualized representation can be viewed as a form of abstraction, in which the most essential features of a rhythm are distilled and represented in a way that is easier to process, grasp, and perform. 

Dualization could also enhance the creative and expressive potential of contemporary musicians, by provid- 

ing them with a tool for exploring and adapting traditional rhythmic patterns in new and innovative ways. Moreover, the study of dualization can shed light on the cognitive and neural mechanisms involved in rhythm perception and performance, as well as the cultural and historical factors that shape rhythmic traditions. By introducing this novel concept, we hope to stimulate further research and innovation in the field of rhythm notation, and to advance our understanding of the cognitive, cultural, and creative processes involved in rhythmic expression. 

In the next section, we present the dualization experiments we have conducted with the participation of four highly skilled professional drummers to validate our hypothesis. We introduce the dataset that emerged from these experiments, which serves as a valuable resource for our analysis. In Section 3, we delve into a detailed analysis of this dataset, shedding light on key findings and insights. Subsequently, in Section 4, we highlight potential applications and promising avenues for future research. 

## 2. METHODOLOGY 

While monotonic representations of multi-voiced rhythms can be obtained by simply flattening any rhythmic pattern, the process of dualizing a multi-voiced rhythm appears to be less straightforward. To further support our hypothesis that dualized patterns can serve as a natural and more meaningful compressed representation of multivoiced drum patterns compared to their monotonic counterparts, we aimed to investigate whether there is a level of consensus or consistency in how multi-voiced patterns can be dualized. To this end, we recruited 4 professional drummers and conducted various dualization exercises, exploring different approaches and gathering insights into the process of dualization. 

## 2.1 Preparation of Rhythmic Material 

To ensure a diverse range of rhythms for dualization, we utilized Magenta’s Groove MIDI Dataset [4]. This dataset comprises of 13.6 hours of live recordings performed on a Roland TD-11 electronic drum kit, each labeled with beat type (i.e. "beat" or "fill"), time signature, and style. The recordings are not quantized (neither in time nor velocity) and vary in duration and styles. For our work, we focused on the "beat" subset of the dataset resulting in 503 original recordings. In this subset, only twelve performances were not in 4/4 meter, and subsequently, we dismissed them. Table 1 summarizes the distributions of styles within the final selected samples. 

||Rock|Funk|Latin|Jazz|Hip-hop|Other|
|---|---|---|---|---|---|---|
|Count|124|42|41|34|25|79|
|Percentage|36%|12%|12%|10%|7%|23%|



Table 1. Style distributions within the 345 2-bar samples selected from GMD 

The original GMD recordings vary from several seconds to a few minutes. As a result, for each session we 

115 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

selected a single 2-bar segment with the highest total cosine similarity with every other 2-bar segments within the session (similarity was calculated between fully quantized patterns). This approach ensured that we had a diverse and representative set of 2-bar rhythms from different sessions and styles for our dualization experiments. These representative segments were further processed to exclude patterns that contained only 2 or less voices (which would have made the dualization task trivial). This left us with a final set of 345 individual meaningful and non-trivial 2-bar loops, suitable for our dualization experiments. 

## 2.2 Data Collection Sessions 

We hired 4 drummers with expertise in Western drumming tradition, two of them with conservatory experience, as shown in Table 2. Each drummer participated in several individual sessions of approximately one hour each. The experiments consisted of playing 2-bar multi-voice drum loops to the participants and asking them to concurrently perform dualized versions using only drum sticks on a Roland HandSonic HPD-15 MIDI drum pad. Participants were instructed to only hit the left region of the drum pad with the left hand and vice-versa. 



<!-- Start of picture text -->
P1 P2 P3 P4<br>A g e 41 20 24 22<br>Ex p erience  ( Years ) 25 11 10 9<br>Dominant Hand Left Left Ri g ht Ri g ht<br><!-- End of picture text -->

Table 2. Demographics of the participants 

For each of the data collection sessions, an Ableton Live<sup>1</sup> project was prepared in advance, containing the drum patterns to be dualized at their original tempo, without any velocity or timing quantization. As shown in Figure 1, the sessions were set up such that the participant would listen to a looping 2-bar pattern and after 1 or 2 repetitions would start to concurrently play their dualized interpretations of the pattern. The participants were allowed to continue their dualizations for as many repetitions as desired until they were confident in the accuracy of the dualization. All the drum patterns in all of the sessions were synthesized using a single sound source.<sup>2</sup> No auditory feedback of dualizations were provided to the participants except for the acoustic sound of the drum pad. 



<!-- Start of picture text -->
Listen Listen & Attempt Unlimited Listens & Attempts<br>2-Bar Drum Pattern<br>at Original Tempo<br>Attempt 1 Attempt 2<br>..<br>Final Dualization …... Attempt N<br><!-- End of picture text -->

Figure 1. Set up of the dataset collection sessions 

## 2.3 Post Session Questionnaire and Interviews 

After the first recording session, each participant was given a questionnaire and an open interview was also conducted. 

> 1 `www.ableton.com` 

> 2 Neutral preset of Addictive Drums 2’s Fairfax sound pack 

The questionnaire comprised of three sections: (1) general information about the participant, (2) assessment of the intuitiveness of the task and confidence in their performance, and (3) exploration of how various rhythmic factors and metrics (e.g., number of instruments, tempo, genre, density, syncopation, mostly extracted from [18, 19]) could potentially influence the dualization process. Parts 2 and 3 of the questionnaire utilized a 7-point Likert scale ranging from 0 to 6. Results from these two parts are summarized in Table 3. 

||P1|P2|P3|P4|Avg.|
|---|---|---|---|---|---|
|General Impressions<br>||||||
|Intuitiveness|4|5|6|5|5|
|Confidence|6|3|4|4|4.25|
|Influence of Rhythmic Features*||||||
|No. of Instruments|0|6|5|5|4|
|Beat Division|0|4|3|5|3|
|Tempo|0|4|3|2|2.25|
|Style|6|3|5|6|5|
|Familiaritywith Style|6|6|6|5|5.75|
|Syncopation-ness|6|5|5|1|4.25|
|Dynamics|6|4|3|4|4.25|
|Note Density|6|4|5|4|4.75|
|LMH Distribution|6|3|2|5|4|
|LMH Syncopation-ness|6|2|4|1|3.25|
|LMH Dynamics|6|4|3|4|4.25|
|LMH Density|3|4|4|6|4.25|



Table 3. Summary of the questionnaires. 

* refers to the perceived importance that different rhythmic features have on the dualizations. LMH refers to the Low, Mid and High frequency regions. Descriptors taken from [18,19]. 

Additionally, after the questionnaire, open interviews were conducted with each participant. In the following sections, we provide a summary with some of the more relevant an recurrent topics discussed. 

## 2.3.1 Meaningfulness, Replicability and Universality 

All four participants unanimously agreed that the concept of dualization is valid and meaningful. Despite one of them admitting to not having thought much about it before, they all found the concept intuitive and useful after the session. Despite that the patterns in the introductory sessions were randomly repeated without notifying the participants, they were able to notice the duplication of the same 2-bar tracks in the session, and they strongly believed that even though their corresponding dualized patterns might not be identical, they would likely share a high similarity. While the results were not entirely conclusive (as discussed in the next section), all participants also expressed confidence in having similar mindsets as their peers while dualizing the same rhythm. Participant 1 justified this idea by referencing the development of the Western percussive tradition from the snare drum, stating that fundamentally, drummers listen to key elements represented by the snare. 

## 2.3.2 The Effects of Style and Repetition 

One participant stated that genre greatly influences which voices to focus on; for example, in the case of rock, the snare and the bass drum would more often be followed, 

116 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

whereas in jazz-influenced styles, the hi-hat and the ride cymbal could probably be included in the reduction, as they emphasise lay back and swing. However, not all participants agreed on interpreting dualization solely as the replication of the two most prominent voices. Some believed that they needed to first digest and understand each rhythm, before extracting its essential form for dualization. Two participants also mentioned that listening to the same pattern repeatedly in the experiment promoted a "dualization refinement", listening more deeply to each iteration and thus refining the extraction of the pattern’s rhythmic essence. 

## 2.3.3 Problems with the Recording Sessions 

Participants reported some issues during the recording sessions, such as using always the same VSTI for all patterns, independently of their musical style. Also, the use of Roland HPD-15, which has a single surface with multiple pads, seems to encourage some drummer habits such as paradiddles, and some participants would have preferred a separated two-pad device. Some tracks were inadequately selected for a 4/4 based recording as Participant 1 interpreted them as a 6/8 time signature, even though GrooveMIDI labelled them as in 4/4. For some swing and shuffled rhythms sometimes the last semiquaver was cut. Participants were also aware of the style bias and of the abundance of Western influenced styles specifically rooted from a snare drum tradition. 

## 3. DATASET AND ANALYSIS 

In this section, we will start with providing an overview of the dataset. Subsequently, we will provide a preliminary analysis of the collected dualizations. The objective of this analysis is to establish whether there is any validity to the hypothesis that professional drummers are able to dualize drum patterns with some level of consistency, so as to establish whether further research on this topic is warranted. 

During the dataset collection sessions, we had a limited time span during which all four participants were available. For the initial session, we had access to all four participants. This session was set up in a manner that would allow us to investigate two main questions: (1) whether a single drummer dualizes a given pattern consistently at different times (Intra Participant consistency) and (2) how consistently different drummers dualize the same drum pattern (Inter Participant consistency). As such, we selected 24 drum patterns to be presented randomly three times to each of the four drummers without notifying them about the repetitions (Subset A1). During the first stage of the data collection sessions, Participant 1 was able to participate longer, as a result, 48 more drum patterns were dualized by him in the same manner (Subset A2). 

During the A2 sessions, Participant 1 notified us that he was aware that we were testing a single drum pattern multiple times. Following this comment, he told us that, if needed, he can dualize the drum patterns in two different ways, in his own terms, in a “simple” and a “complex” manner. Inspired by this comment, we confirmed with the 

other participants about this view of dualization. Subsequently, we modified the remaining sessions so as to explore whether there is any consistencies among the “simple” and “complex” dualizations. We were able to partially conduct these sessions with Participants 1 and 2 (Subset B1), while the remaining sessions were only conducted with Participant 1. Table 4 summarizes the collected data. 

The final dataset consists of 1116 dualizations obtained from the participants. These dualizations were obtained from the set of 345 unique drum patterns. Moreover, each of the drum patterns were used in a single dualization test, that is, for example, a drum pattern used in Subset A1 was not reused in the A2, B1 and B2 subsets. The decision to not reuse the drum patterns in different subsets was made to maximize the number of drum patterns for which at least one set of dualizations were available in the final dataset. 

In Section 3.1, we will use the collected dataset to provide a preliminary analysis on whether there are any intra/inter participant consistencies between the dualizations obtained at random from all four participants (Subset A1) - see Figure 2. Lastly, in Section 3.2, we will compare simple dualizations with their complex counterparts from both intra- and inter-participant perspectives. The analysis presented in this section has been done on a binary representation of the dualizations, fully quantized to a 16th note grid. Moreover, it should be noted that, as confirmed with the participants, a given dualization can be reproduced using an inverse hand combination. As such, to compare the rhythmic similarity between the dualizations, a handagnostic measure should be employed (e.g. L `0` R `0` LL and R0L0RR patterns should be treated as identical - L and R refer to Left and Right hand hits at a 16th note time step and 0 refers to silence). 



<!-- Start of picture text -->
Drum Pattern 3 ...<br>Drum Pattern 2<br>Drum Pattern 1<br>Participant N<br>Intra Pairs<br>000 Inter Pairs<br><!-- End of picture text -->

Figure 2. Inter-/Intra- pairs. For each drum pattern, intrapairs are selected from each of the participants. Inter-pairs are selected by pairing a participant’s repetition with all other repetitions corresponding to the same test. 

To this end, we focused our analysis on the flattened versions of the dualizations, that is, the left and right hand patterns were superimposed onto a single sequence (e.g. 101011). While this approach does not explore the function of each of the dualized streams, we believe that it is valid as a preliminary investigation, because if the flattened patterns show no rhythmic consistency, further analysis on the function of each hand may not be warranted. In other words, the validity of our hypothesis is contingent upon the presence of rhythmic consistency in the dualized patterns, and further analysis may be needed to determine the functional aspects of each hand in the dualizations. 

117 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

|Sub|se|t|Tested Drum Patterns|Rep|etitions|Per T|est|Total Dualizations|
|---|---|---|---|---|---|---|---|---|
|||||P1|P2|P3|P4||
|Three Repetitions (A)||Multi-Participant(A1)|24|3|3|3|3|288(24×3×4)|
|||Single Participant(A2)|48|3|-|-|-|144(48×3×1)|
|Simple vs Complex (B)||Multi-Participant(B1)|69|2|2|-|-|276(69×2×2)|
|||Single Participant(B2)|204|2|-|-|-|408(204×2×1)|
|To|tal||345|762|210|72|72|1116|



Table 4. Summary of the collected dataset 

## 3.1 Three Repetitions (A1 Session, Participants 1-4) 

In Subset A1, we presented 24 drum patterns<sup>3</sup> to each of the four participants three times in a random order, resulting in a total of 288 obtained dualizations. We first examine the consistency of each participant’s dualizations over the three repetitions (intra-participant analysis), and then we investigate the consistency of each of dualizations with their counterparts<sup>4</sup> from other participants (interparticipant analysis). To establish the similarity between two given patterns, we used the Jaccard similarity measure, defined as the ratio of the overlap of two sequences divided by the union. Moreover, to establish the perceptual similarity of the dualizations, we used Edit Distance [20, 21], defined as the minimum number of operations (insertions, deletions, or substitutions) required to transform one sequence into another. Figures 3 and 4 summarize the results of inter/intra-participant analysis using a pair-wise comparison. In both cases, in order to establish a baseline comparison, we also calculate the Edit and Jaccard values for the same number of pairs randomly selected (each random pair comes from dualizations obtained from two randomly selected participants and are ensured not to be associated with the same drum pattern). 



<!-- Start of picture text -->
Edit Distance Jaccard Similarity<br>30 1.0<br>0.8<br>20<br>0.5<br>10 0.2<br>0.0<br>P1 P2 P3 P4 Rand. P1 P2 P3 P4 Rand.<br><!-- End of picture text -->

Figure 3. Intra-Participant Analysis of Subset A1 

The results of the intra-participant distributions (Figure 3) show that the Edit distances are smaller for any of the four participants’ repetitions compared to the distance between randomly paired dualizations. Similarly, the Jaccard similarities are also higher than the random pairs. 

Unlike the intra-participant distributions, the edit distances for inter-participant dualizations have some overlap with the random pairs. This overlap is also observed in the Jaccard similarity values. However, despite this overlap, the inter-participant distributions still show a trend towards higher similarity values compared to the random pairs. The lower consistency between inter-participant dualizations, compared to the intra-participant dualizations may be an indicator that experienced drummers have a consistent du- 

> 3 latin: 4, hiphop: 3 , jazz: 3, rock: 3, funk: 2, soul: 2, afrobeat: 1, afrocuban: 1, dance: 1, neworleans: 1, pop: 1, punk: 1, reggae: 1 4 dualizations obtained from the same drum pattern tested 



<!-- Start of picture text -->
30 Edit Distance 1.0 Jaccard Similarity<br>0.8<br>20<br>0.5<br>10 0.2<br>0.0<br>P1/P2 P1/P3 P1/P4 P2/P3 P2/P4 P3/P4 Rand. P1/P2 P1/P3 P1/P4 P2/P3 P2/P4 P3/P4 Rand.<br><!-- End of picture text -->

Figure 4. Inter-Participant Analysis of Subset A1 

alized interpretation of rhythms, however, these interpretations vary to some extent compared to other drummers. While this is a possibility, we believe more comprehensive analysis is required prior to making this conclusion as there are a number of limitations to the approach taken in this paper. 

The current state of our analysis imposes several restrictions and simplifications that limit the depth of our study of the dataset. Firstly, it is constrained to the flattened versions of the dualizations. Secondly, it dismisses (quantizes) the velocity and micro-timing information, which are important factors in drumming that can affect nuances and groove. Experienced drummers often utilize velocity and micro-timing to add expressiveness to their playing, potentially leading to differences in the perceived rhythm. Therefore, a comprehensive investigation of the dualizations should incorporate these dimensions for a more nuanced understanding. 

## 3.2 Simple/Complex (B Sessions, Participant 1) 

As mentioned previously, Participant 1 pointed in the open interview that a dualization can be done in different manners: simple and complex. For further exploring this idea, in a second phase of the dataset collection sessions, two participants were asked to first dualize a drum pattern in a simple manner, and also immediately after, re-dualize the same pattern in a more complex manner. These sessions were partially conducted with Participants 1 and 2 (session B1), and more tests were done using Participant 1 (session B2). For the sake of brevity, we focus the analysis of this subset on Participant 1 (a total of 273 paired simple and complex dualizations). 

Figure 5 shows that a major distinction between the simple and complex dualizations of Participant 1 is that the simple versions are considerably less active than their complex counterparts. One interesting observation is that the activity level of the dualizations obtained from Participant 1 during the first session (A1) (in which this simple/complex distinction had not been introduced) are more on par with the complex dualizations. This observation 

118 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 



<!-- Start of picture text -->
1.0 Step Densities<br>0.8<br>0.6<br>0.4<br>0.2<br>0.0<br>P1 P1 P1 P2 P4<br>Simple Complex (A1) (A1) (A1) (A1)<br>(B) (B)<br><!-- End of picture text -->

Figure 5. Step Densities. Left two distributions correspond to the 273 simple and complex dualizations obtained from P1 in sessions B1 and B2; remaining four correspond to 72 dualizations per each participant in A1 

along with the step density distributions for Participants 2-4 raises a question that perhaps, unless restricted, the drummers default to more active dualizations. This tendency may be explainable from two perspectives: (1) in most styles, the hands are generally highly active as they are responsible for playing the majority of the drum kit, and (2) the dualizations may be by default more biased towards the rudiments that many drummers strenuously practice using their hands. 

To further analyze the simple and complex dualizations, we calculated the edit distance and Jaccard distance between each pair of dualizations (see Figure 6). Similar to section 3.1, to establish a baseline comparison, we used an equal number of uncorrelated simple and complex pairs from Participant 1 dualizations. The results here show that, while lower in general, the distribution of the edit distances between the simple and complex pairs are partially overlapping. Moreover, this distribution is higher than the intra repetition distribution in Subset A1. These trends are also evident in the Jaccard similarity distributions. These differences relative to the intra distances in subset A1 are fully expected knowing that the dualizations are intentionally varied in this experiment. 



<!-- Start of picture text -->
30 Edit Distance 1.0 Jaccard Similarity<br>0.8<br>20 004<br>10 0.2<br>0.0<br>P1 (A1) P1 Simple Rand. P1 Sim. Rand. P1 Sim.<br>P1 Complex Rand P1 Comp. (A1) P1 ComplexP1 Simple Rand. P1 Compl.<br><!-- End of picture text -->

Figure 6. Distributions of distances/similarities between all of the Participants simple dualizations and their corresponding complex dualizations 

## 4. APPLICATIONS AND FUTURE WORK 

The majority of our work has been focused on data collection and curation, as well as preparing tools to allow the community to easily explore and study the data. All the collected data have been carefully processed and organized for both A and B subsets. Moreover, we have prepared an accompanying website that enables researchers to listen to all paired repetitions while also visualizing the piano rolls. Lastly, we have also developed an open-source API that allows for easy access to the data, visualization, synthesis, 

and analysis using both pre-implemented and third-party tools of interest. All these resources are publicly available at `https://taptamdrum.github.io` .<sup>5</sup> 

We envision that the dataset can be used in a variety of studies. Rhythm reduction studies could use it to examine the simplification of multi-voiced patterns into dualvoiced ones. The dataset can also be used to develop computational models for drum pattern reduction. These models would be highly valuable as they allow for easier study of polyphonic drum patterns. Moreover, knowing that the dualizations of a single participant for a given drum pattern are highly correlated (i.e. they are perceptual interpretations of the same pattern), researchers can validate whether the features extracted from the dualizations are also highly correlated. This would provide a way to evaluate the effectiveness of rhythm feature extraction algorithms and potentially improve them. Similarly, to establish the perceptual relevance of rhythmic distance/similarity measures, researchers can use the simple/complex subset of the dataset to ensure that the proposed measures result in reasonable distances that correlate with the perceptual re-interpretations of a given pattern. 

Lastly, the dataset can also be used for drum generation tasks. For instance, a generative model could be developed so as convert a dual sequence into a full drum pattern (similar to single voice rhythm into multi-voice drum generators [4, 22]). Such generative models can be used in many creative ways as during the inference stage, each of the left/right streams fed into the drum generator can be extracted from separate instruments/sources. Moreover, the random repetitions and the simple/complex repetitions can be used in developing deep metric learning models that rely on paired training samples. 

## 5. CONCLUSIONS 

In this work, we presented TapTamDrum, a novel dataset consisting of 1116 dualizations of drum patterns performed by four experienced drummers, covering 345 unique drum patterns selected from Magenta’s GrooveMIDI dataset. The analysis conducted in section 3.1 provides valuable insights into the dataset. Firstly, it shows that there are intraparticipant consistencies in the dualizations. That said, the inter-participant analysis are less definitive and require further detailed investigation. Moreover, the simple/complex comparisons (section 3.2) show that the complex dualizations are significantly more active than the simple ones while adhering to some level of rhythmic consistency with their simple counterparts. The analysis conducted in this work was preliminary and limited and has not explored the full potential of the dataset. The main focus of this work was to collect, curate, organize the dataset and also provide resources for prompt exploration of the data. To this end, we have prepared an accompanying website and an open-source API. Finally, this dataset can be used in a variety of rhythm related studies ranging from perception to generation. 

> 5 `https://github.com/taptamdrum/dataset` 

119 

## Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

## 6. ACKNOWLEDGMENTS 

This research was partly funded by the Ministry of Science and Innovation of the Spanish Government. Agencia Estatal de Investigación (AEI). (Reference: PID2019111403GB-I00). 

## 7. REFERENCES 

- [1] J. Powell, “What is temporal art? a persistent question revisited,” Contemporary Aesthetics, vol. 13, 2015. 

- [2] W. T. Berry, Structural functions in music. Courier Corporation, 1987. 

- [3] G. T. Toussaint, The geometry of musical rhythm: What makes a "Good" rhythm good? CRC Press, 2016. 

- [4] J. Gillick, A. Roberts, J. Engel, D. Eck, and D. Bamman, “Learning to groove with inverse sequence transformations,” in Proc. of the 36th International Conference on Machine Learning, California, USA, May 2019, pp. 2269–2279. 

- [5] O. Lartillot and F. Bruford, “Bistate reduction and comparison of drum patterns,” in Proc. of the 21st International Society for Music Information Retrieval Conference. Montreal, Canada: ISMIR, Oct. 2020, pp. 318–324. 

- [6] B. H. Repp and A. Penel, “Auditory dominance in temporal processing: New evidence from synchronization with simultaneous visual and auditory sequences.” Journal of Experimental Psychology: Human Perception and Performance, vol. 28, no. 5, pp. 1085–1099, 2002. 

- [7] P. J. Treffner and M. Turvey, “Handedness and the asymmetric dynamics of bimanual rhythmic coordination.” Journal of Experimental Psychology: Human Perception and Performance, vol. 21, no. 2, p. 318, 1995. 

- [8] L.-A. Leow, C. Rinchon, and J. Grahn, “Familiarity with music increases walking speed in rhythmic auditory cuing,” Annals of the New York Academy of Sciences, vol. 1337, no. 1, pp. 53–61, 2015. 

   - [12] E. D. Novotney, “The 3:2 relationship as the foundation of timelines in West African musics,” Ph.D. dissertation, University of Illinois at Urbana-Champaign, 1998. 

   - [13] G. Kubik, Africa and the Blues. University Press of Mississippi, 1999. 

   - [14] K. Agawu, The African Imagination in Music. Oxford University Press, 04 2016. 

   - [15] D. Peñalosa and P. Greenwood, The Clave Matrix: Afro-Cuban Rhythm : Its Principles and African Origins, ser. Unlocking clave. Bembe Books, 2012. 

   - [16] R. Bååth, “Subjective Rhythmization: A Replication and an Assessment of Two Theoretical Explanations,” Music Perception, vol. 33, no. 2, pp. 244–254, 12 2015. 

   - [17] M. A. G. Witek, E. F. Clarke, M. L. Kringelbach, and P. Vuust, “Effects of Polyphonic Context, Instrumentation, and Metrical Location on Syncopation in Music,” Music Perception, vol. 32, no. 2, pp. 201–217, 12 2014. 

   - [18] D. Gómez-Marín, “Similarity and style in electronic dance music drum rhythms,” Ph.D. dissertation, Pompeu Fabra University, Spain, 2018. 

   - [19] D. Gómez-Marín, S. Jordà, and P. Herrera, “Drum rhythm spaces: From polyphonic similarity to generative maps,” Journal of New Music Research, vol. 49, no. 5, pp. 438–456, 2020. 

   - [20] O. Post and G. Toussaint, “The edit distance as a measure of perceived rhythmic similarity,” Empirical Musicology Review, vol. 6, no. 3, pp. 164–179, 2011. 

   - [21] M. Moritz, M. Heard, H.-W. Kim, and Y. S. Lee, “Invariance of edit-distance to tempo in rhythm similarity,” Psychology of Music, vol. 49, no. 6, pp. 1671– 1685, 2021. 

   - [22] B. Haki, M. Nieto, T. Pelinski, and S. Jordà, “Real-Time Drum Accompaniment Using Transformer Architecture,” in Proceedings of the 3rd Conference on AI Music Creativity. AIMC, Sep. 2022. [Online]. Available: 10.5281/zenodo.7088343 

- [9] M. Leman, D. Moelants, M. Varewyck, F. Styns, L. van Noorden, and J.-P. Martens, “Activating and relaxing music entrains the speed of beat synchronized walking,” PLoS ONE, vol. 8, no. 7, p. e67932, Jul. 2013. 

- [10] A. D. Patel and J. R. Iversen, “The evolutionary neuroscience of musical beat perception: the action simulation for auditory prediction (ASAP) hypothesis,” Frontiers in Systems Neuroscience, vol. 8, May 2014. 

- [11] J. Podmore, Jaki Liebezeit: The Life, Theory And Practice Of A Master Drummer. Unbound, 2020. 

120 

