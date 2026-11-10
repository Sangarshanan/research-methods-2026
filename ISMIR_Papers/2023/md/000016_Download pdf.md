---
paper_id: "000016"
year: 2023
title: "Download pdf"
source_url: "https://zenodo.org/record/10265245/files/000016.pdf"
---

# **POLYRHYTHMIC MODELLING OF NON-ISOCHRONOUS AND MICROTIMING PATTERNS** 

**George Sioros University of Plymouth georgios.sioros@plymouth.ac.uk** 

## **ABSTRACT** 

Computational models and analyses of musical rhythms are predominantly based on the subdivision of durations down to a common isochronous pulse, which plays a fundamental structural role in the organization of their durational patterns. Meter, the most widespread example of such a temporal scheme, consists of several hierarchically organized pulses. Deviations from isochrony found in musical patterns are considered to form an expressive, micro level of organization that is distinct from the structural macro-organization of the basic pulse. However, polyrhythmic structures, such as those found in music from West Africa or the African diaspora, challenge both the hierarchical subdivision of durations and the structural isochrony of the above models. Here we present a model that integrates the macro- and micro-organization of rhythms by generating non-isochronous grids from isochronous pulses within a polyrhythmic structure. Observed micro-timing patterns may then be generated from structural non-isochronous grids, rather than being understood as expressive deviations from isochrony. We examine the basic mathematical properties of the model and show that meter can be generated as a special case. Finally, we demonstrate the model in the analysis of micro-timing patterns observed in Brazilian samba performances. 

## **1. INTRODUCTION** 

Isochrony has been a fundamental element of computational and cognitive models of musical rhythm, which are often inspired by the organization of rhythms found in Western classical music theory [1]. The advantages of isochrony as a structural foundation for the organization of music are numerous, from the potential to explain our ability to synchronize to music [2–5], to defining higher level qualities such as tempo [1, 6]. However, while periodicity is common in music, strict isochrony is almost never observed [7] and many studies document with empirical data the systematic durational patterns from music around the world, which do not fit into an isochronous structure, including the Viennese waltz [8], Brazilian Samba [9–11], Mali Jembe music [12] and the Norwegian Telespringar [13]. 

> © G. Sioros. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). **Attribution:** G. Sioros, “Polyrhythmic modelling of non-isochronous and microtiming patterns” in _Proc. of the 24_<sup>_td_</sup> _Int. Society for Music Information Retrieval Conf._ , Milan, Italy, 2023. 

Generally, such patterns are understood on the basis of an underlying structural basic isochronous pulse and expressive deviations from it [14]. Although an isochronous pulse may not be directly observed and measured in the music signal, a steady beat may be inferred by the listener, most evidently when we bob our head or tap our feet to the music. Numerous beat tracking algorithms exist in the music information retrieval literature [15] and even cognitive models have been formalized that attempt to imitate this behavior [16, 17]. In most music-theoretical and cognitive models of rhythm, the beats of the basic isochronous pulse are grouped together, say every two or three, resulting in slower pulses that coincide with all faster ones, forming a hierarchical structure often referred to as meter [1, 18]. 

Typically, deviations from isochrony are modeled by processing repeating rhythmic patterns to derive statistical properties, such as the mean deviation from an isochronous pulse at each location of the repetition cycle (see for example [10]). Such statistical models only describe the processed recordings and cannot be generalized. They do, however, provide evidence that deviations from isochrony may be more than a mere expressive element of the performance, and are rather structural components of music [12]. 

Polyrhythmic music challenges the principle of hierarchical organization of rhythms. Polyrhythms are organized on the basis of multiple isochronous pulses of different periods that do not coincide [19–21]. Polyrhythmic elements are found in music around the world, with most representative examples coming from West Africa and the African diaspora [22, 23].  Even in groove-oriented music, where a strong sense of pulse is felt, short patterns that suggest an alternative pulse are common [24]  and evidence indicate that they are central to experiencing groove [25]. Perhaps unsurprisingly, certain polyrhythmic music traditions also exhibit large and systematic deviations from isochrony [26]. It has been proposed that the deviations from isochrony and the polyrhythmic character of music from the African diaspora are related, one enhancing the other [9, p. 234, 23]. 

This paper presents a music-theoretical model that constructs non-isochronous grids from different isochronous pulses within a polyrhythmic context. Essentially, it attributes systematic non-isochronous patterns to underlying polyrhythmic structures that may be considered fundamental to the organization of the rhythmic patterns. In section 2, we present relevant music-theoretical concepts. Section 3, introduces a mathematical formalization of our model along with its key properties. In section 4, we employ the model to analyze Brazilian samba performance data taken from existing literature. 

146 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

## **2. BACKGROUND** 

## **2.1 Structural isochrony** 

In music theory, meter is formalized as a hierarchical structure that groups pulses periodically [18].  In typical mainstream Western music, the events are aligned across the voices in such a way that the salient moments coincide to form a metrical hierarchy (Figure 1). The different levels of the hierarchy correspond to various regularities found in the rhythm. While each level takes the form of a steady pulse, the various levels are stacked so that slower pulses coincide with all faster ones. Consequently, the periodicities in the articulated patterns in the music should also align in a similar fashion, although each voice may not necessarily articulate a specific metrical level. The periodic grouping of the beats has been formalized as a prime factorization problem [27–29]. Generative models of meter that can be implemented in computer algorithms have been developed as a set of transformations [30] and an abstract context-free grammar [31] 

As a cognitive mechanism, meter is understood as oscillations that represent the attentional energy of the listener [3, 4, 32] or a predictive schema [33] that expresses our expectations about the timing of musical events [34]. The limitations of our cognition impose temporal limits to the pulses of the metrical hierarchy [1, p. 29, 35]. At the lower limit, the shortest pulse has a period of ~100ms, and at the upper limit, the longest pulse has a period of ~1.5s. The highest metrical salience is observed for pulses with a moderate period of ~700ms [6]. Tempo is then defined as the frequency of the most salient isochronous pulse of the metrical hierarchy. 

The durations of the sound events are classified by the listener into discrete categories [2, p. 382, 36–39] that are influenced by the sensation of a pulse or meter evoked in them, so that a certain duration may be interpreted as a dif- 

ferent category when listened in a different metrical framework [40]. A rhythmic pattern is essentially coded as a series of nominal durations that are a multiple of the basic isochronous pulse of the metrical hierarchy. 

Despite the fundamental role that isochrony plays in the construction of meter, non-isochronous grouping of beats create non-isochronous metrical levels and meters (NI meters) [1, Ch. 7] (see Figure 2 for an example). Such groupings are based on the principle of maximal evenness [1, 41, 42] which is also the basis for the Euclidean rhythms that are encountered in many traditional rhythms [43, 44]. Such non-isochronous patterns are constructed by distributing a number of onsets _k_ as evenly as possible over a number of beats _n_ of an isochronous pulse. A Euclidean rhythm can then be denoted as _E_ ( _k_ , _n_ ) [43]. 

## **2.2 Micro-timing** 

While the metrical hierarchy determines durational categories for musical events, continuously variable timing determines an expressive level of organization of rhythms [14]. Systematic deviations from the nominal durations are typically measured in ms or as a percentage of the nominal beat duration to allow for an easier comparison between music segments with different tempi (Figure 3). The phenomenology of micro-timing has been discussed within the context of various music genres (see [9, 12, 45, 46] for some examples). Micro-timing modeling typically relies on statistical analysis of the timing of musical events over the duration of a performance to identify systematic, nonisochronous patterns [10, 47]. 



**Figure 3** : Onsets (o) may not exactly align with the isochronous pulse and have expressive (micro) timing deviations denoted with arrows (®). 

## **2.3 Polyrhythms** 



**Figure 1** : The metrical structure (bottom) emerging from The first two bars of “Conquest of Paradise” of composer Vangelis (top). Events are marked with (o). The three pulse levels of the metrical hierarchy ( | )  have periodicities of simple integer ratios 1:3:4 and are aligned with no phase differences. 



**Figure 2** : Example of a Non-Isochronous meter. The middle metrical level is non-isochronous and can be constructed as the Euclidean rhythm _E_ (4,9). 

Polyrhythms have been described in music theory as a form of metric dissonance [19, 20]. While consonant pulses align to give rise to the hierarchical structure of meter, dissonant pulses intertwine. Typically, polyrhythms consist of pulses with distinct beat durations that are not simple integer multiples of one another. The ratio between the beat durations of the two pulses determines the length of the repetition cycle of the entire polyrhythm. The number of beats of each pulse within a cycle of the polyrhythm !!and !" are related to the beat durations of the two pulses "#!and "#": 



<!-- Start of picture text -->
"#! $ !" (1)<br>"#" !!<br><!-- End of picture text -->



**Figure 4** : The 2|3 polyrhythm. A basic isochronous pulse subdivides both the 2-beat and the 3-beat pulses. 

147 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

Polyrhythms can then be represented as !!%!".  Figure 4 depicts a polyrhythm in which 2 beats of one pulse have the same duration as 3 beats of a second pulse. The pulses that constitute a polyrhythmic structure may have a common faster subdivision with a beat duration longer than the perceptual threshold of 100ms, resulting in a type of grouping dissonance or polymeter [21]. 

## **2.4 Polyrhythms as flexible spaces** 

In principle, onsets are assumed to belong to one of the pulses of a polyrhythm, even if they are not perfectly aligned. However, it has been proposed that in music from the African diaspora, the intervals between the pulses of a 16|12 polyrhythm define a flexible space [23]. Events occurring between a beat from the 12-beat pulse and a beat from the 16-beat pulse may have a ‘mixed’ character, belonging at the same time to both pulses. Here, we extend this concept of ‘mixed’ character events to create nonisochronous grids that combine the character of both pulses of a polyrhythm. In this way, we formalize (micro) timing deviations from isochrony as a structural element of musical rhythms rooted in polyrhythms. 

## **3. NON-ISOCHRONOUS GRIDS** 

## **3.1 Definition and construction** 

Non-isochronous pulses are constructed from two isochronous pulses of different periods. We will refer to the constructed non-isochronous pulses as grids (NI grids) to better distinguish them from isochronous pulses. The NI grid is formed by gradually changing the positions of the beats of one isochronous pulse towards a proximate beat of the other pulse. We call the first pulse the ‘formative’ pulse and the later pulse the ‘target’ pulse of the NI grid (Figure 5). The new beat positions for the NI grid are determined by: 



<!-- Start of picture text -->
&# $ '# ( )# * +#$ , '#- (2)<br><!-- End of picture text -->

where _i_ is the beat index of the formative pulse, '# is the formative’s beat time, #$ is the target’s proximate beat time and )# is the ‘shift’ as a fraction of the distance between the two beats taking values in the range [0, 1]. 

In principle, each beat may be shifted independently to form an NI pattern with multiple durations. Here, we examine the case of a uniform shift, where all formative beats are shifted by the same parameter _S_ towards the nearest beat of the target pulse. Then, as _S_ goes from 0 to 1, the formative pulse is being ‘morphed’ into the target pulse. While the relative shift _S_ is uniform, the individual beat 



<!-- Start of picture text -->
Target<br>NI grid<br>Formative<br>i+1<br>Time<br><!-- End of picture text -->

**Figure 5:** Construction of a non-isochronous grid by uniformly shifting the beats of a formative pulse towards the nearest beat positions of a target pulse. 

displacements in time units (e.g. ms) will still have different values as the distance between the beats of the two pulses is not the same for all beats. Furthermore, _S_ can also exhibit dynamic variations. In this sense, it should be understood as analogous to tempo, which can serve as a uniform parameter within a given time span and can also exhibit variations over the duration of a piece. 



<!-- Start of picture text -->
NI grids constructed by a uniform shift consist of only<br>two beat classes, which we refer to as Short and Long for<br>simplicity. If "' is the period of the formative pulse and<br>"# the period of the target pulse, then the two beat classes’<br>durations are:<br>"& $ ./ , )0 * "' ( ) * "# * 1 (3)<br>where,  k  can take one of two values:<br>(4)<br>1%&'() $  2 "' "#3 $ 45 1*'+, $ 6 "' "# 7  $ 4 ( /<br><!-- End of picture text -->

where 8 9 and : ; denote the floor and ceiling functions. The durations of the Short and Long beats are limited within a NI grid. For ) $ <, both the Short and Long beats have a duration equal to the period of the formative pulse "', which is the upper limit for the Short beats and the lower limit for the Long beats. Conversely, for ) $ /, the Short beats reach their shortest duration and the Long beats their longest duration which are=>?@ABAC=DEF@>GFAH=IJ=@KA= LECM@>I?= IJ= @KA= GAC>IL= IJ= @KA= @MCBA@= GEFHA="#. When "' N "#, i.e. !- O !. , then 1%&'() $ < and  1*'+, $ / and therefore the Short beats can reach a duration of 0. 

By construction, the total number of beats of an NI grid is the same as the number of beats of the formative pulse. The number of Long beats of an NI grid can be calculated as the remainder of the division between the number of beats of the formative and target pulses: !*'+, $ !.=P=!(5) 

## **3.2 Maximal evenness in NI grids** 

One of the key properties of the NI grids is that the Short and Long beats are evenly distributed; a direct consequence of the underlying polyrhythmic pulses being isochronous and the shift _S_ being uniform. Different alignments of the pulses result in different rotations of the Short-Long beat pattern. 

So far, we have examined shifts of the formative beats towards the nearest target beats. The above equations and the even distribution of the Short-Long beat classes also apply to shifts towards the next or previous target beat. Arbitrary combinations of the shifts, e.g. some towards the nearest beat and others towards the next beat, may also result in an even distribution of the two beat classes. However, this is guaranteed only when all formative beats follow the same rule. In Figure 6, the example of a 6 beat formative pulse and an 8 beat target pulse is shown. It follows from Eqn (5) that the number of Long beats in the resulting NI grid is 2, and the remaining 4 are Short. The different alignments of the formative and target pulses in Figure 6 produce the same Short-Long beat pattern but in different rotations. 

Given a polyrhythm=!-%!.=and its total duration, Eqns (3 - 5) can be used to calculate the durations and number of Long and Short beats in the corresponding NI grid as a 

148 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 



<!-- Start of picture text -->
一<br>Target<br>i Iid S L S S L S A<br>Formative<br>Target<br>iIid L S S L S S B<br>Formative<br>Target<br>Nri Iid L S S L S S<br>Formative<br><!-- End of picture text -->

**Figure 6** : Three different alignments of a formative pulse with 6 beats and a target pulse of 8 beats produce the same pattern of evenly distributed Short-Long (L/S) beats, but in a different rotation. In A and B, all formative beats are shifted towards the nearest target beats. In C, the formative beats are all shifted forward, i.e. always towards the next target beat. 

function of the shift _S_ . The NI grid can then be produced directly by the Euclidean algorithm as a maximally even distribution of the two beat classes [1, 41, 43]. 

NI grids can be represented as polyrhythms with the additional parameter _S_ : &Q.!-%!.5 )0. However, in contrast to polyrhythms, the order that the two pulses appear in the NI grid definition is important. The formative and target pulses are not equivalent as can easily be seen from Eqn (5), where the  modulo operation is not commutative, and the fact that the number of beats of an NI grid is equal to the number of beats of the formative pulse, but not of the target pulse. 

As a consequence of the even distribution of the Long and Short beats, every Euclidean pattern can be constructed as a NI grid (see Figure 7 for an example taken from [43]). In fact, it follows directly from the construction of Euclidean patterns that Euclidean patterns are equivalent to NI grids with a shift _S_ = 1: 



<!-- Start of picture text -->
R.S5 T0 $ &Q.S=%=T5 /0 (6)<br><!-- End of picture text -->



<!-- Start of picture text -->
Target<br> Ind L S L S L<br>Formative<br><!-- End of picture text -->

**Figure 7:** The Cuban cinquillo pattern is the Euclidean rhythm R.U5V0 and the NI grid &Q.U=%=V5 /0. 

Since the levels of a metrical hierarchy are evenly distributed, they can be constructed from NI grids. For NI meters, the process is similar to the construction of Euclidean patterns. However, typically, meters include isochronous pulses at all levels of their hierarchy and, therefore, these meters can be constructed from degenerate NI grids for which the Short and Long beats have the same duration. 

## **4. APPLICATION TO SAMBA PERFORMANCES** 

Music events may be assigned to the beats of an NI grid. Similar to beat tracking, analyzing an observed durational 

pattern requires aligning event onsets with beats. As not all beats in an NI grid are necessarily articulated, there may be more than one NI grid that fits the rhythmic pattern. Information about the polyrhythmic structures that may be expected for the music at hand can help reduce the search space and find meaningful solutions. Here, we demonstrate the potential of the model in musical rhythm analysis by constructing NI grids that fit the durational patterns found in Brazilian samba. 

Various rhythmic patterns of samba recordings have been reported in the literature [9–11, 13]. They are considered a characteristic feature of the performances and an integral part of the style, although the degree of deviation from isochrony as well as the specific non-isochronous patterns measured vary between studies. In [10], the same Samba rhythm was recorded at three different tempi. From the recordings, mean durations of the four events that make up the basic repetitive pattern were calculated. The results, which are summarized in Table 1, show that all three tempi follow the same general Medium-Short-Medium-Long durational pattern. The relative durations however are different at each tempo, with the fast and preferred tempi showing the most similarity and the slow tempo being more distinct and closer to isochrony with a characteristic lengthened last event. Additionally, the two Medium events (1 and 3) were reported to be significantly different between them, indicative of Medium-Short and Medium-Long duration [10]. 

Here we hypothesize that the observed non-isochronous patterns of  Table 1 are the result of an underlying polyrhythmic structure and we attempt to reproduce them as: 1) NI grids with a 4-beat formative pulse and 3-beat target pulse (section 4.1), and 2) NI grids with a 5-beat formative pulse and a binary target pulse (section 4.2). In section 4.3, we use the NI grids to propose potential explanations for the differences in the observed durations between the three tempi. 

## **4.1 The 4-beat formative pulse hypothesis** 

Our first hypothesis is that the basic Samba pattern (Table 1) emerges from an underlying 4|3 polyrhythm. From Eqn (5), it follows that the corresponding NI grid consists of 3 

|Temo - BPM||Event n|umber||
|---|---|---|---|---|
|p|1|2|3|4|
||Measur|ed in ms|||
|Fast - 133|121<br>±7.1|69<br>±6.0|112<br>±5.1|153<br>±8.6|
|Preferred - 100|157<br>±8.7|110<br>±8.4|142<br>±5.8|196<br>±9.0|
|Slow - 69|212<br>±9.7|198<br>±12.4|206<br>±6.6|256<br>±9.5|
|Measured|in percent|of the tot|al duratio|n|
|Fast-133|27|15|25|34|
|Preferred-100|26|18|24|33|
|Slow-69|24|23|24|29|



**Table 1** : Mean durations and standard deviations of the four events of the basic Samba pattern from [8, Tbl. 3]. 

149 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 



<!-- Start of picture text -->
2 3 2 4<br>Fast T Fast T<br>NI(4|3, 0.39) NI NI(5|2, 0.18)NI<br>F F<br>Preferred T<br>Preferred T<br>NI(5|2, 0.16) NI<br>NI(4|3, 0.27)NI<br>F<br>F<br>Slow T<br>Slow T<br>NI(5|4, 0.71)NI<br>NI(4|3, 0.09)NI<br>F<br>F<br>Alternative NIgrids<br>Preferred T<br>Figure 8 : Potential NI grids with a 4-beat formative pulse<br>for the Samba patterns of Table 1. A hypothetical align- NI(10|4, 0.55) NI<br>ment between the target (T) and formative (F) pulses is  F<br>shown. The NI grids are specified on the left. The four<br>events from Table 1 and the corresponding mean durations  Slow<br>are indicated by grey circles and the integer numbers at the<br>NI(10|4, 0.71) NI<br>top.<br>F<br><!-- End of picture text -->

|Tempo||Event|number||
|---|---|---|---|---|
|NIgrid|1|2|3|4|
|Fast|128.7|69|128.7|128.7|
|_NI_(4|3, 0.39)|(**7.7**)|(0.0)|(**16.7**)|(**24.33**)|
|Preferred|165.0|110.0|165.0|165.0|
|_NI_(4|3, 0.27)|(8.0)|(0.0)|(**23.0**)|(**31.0**)|
|Slow|224.7|198.0|224.7|224.7|
|_NI_(4|3, 0.09)|(**12.7**)|(0.0)|(**18.7**)|(**31.3**)|



**Figure 9** : Potential NI grids with a 5-beat formative pulse (specified on the left) for the patterns in Table 1 (indicated here with grey circles) for the three different tempi. Two alternative NI grids are shown for the preferred and slow tempo duration patterns. 

beat and a binary pulse. Since only 4 of the 5 beats of the NI grid coincide with events, the two beat classes may produce three distinct event durations and in this way reproduce more accurately the event durations in the pattern (Figure 9, top). As in the previous hypothesis, the Short beat is aligned with event 2. The longer fourth event in this hypothesis spans two beats. 

**Table 2** : Theoretical durations in ms for the four samba events based on the NI grids of Figure 8. In parenthesis, the differences between the predicted durations and the observed mean durations for the respective events are shown for comparison with the standard deviations reported in Table 1. Difference greater than the respective standard deviations are shown in bold. 

In the fast and preferred tempi, the length of event 4 is roughly double of the 2<sup>nd</sup> event and therefore we hypothesize that it spans two Short beats. Consequently, NI grid consists of 3 Short beats and 2 Long beats and therefore it is derived from a 5|2 polyrhythm. In the slow tempo, the difference between the duration of event 4 and the rest of the events is smaller. Our hypothesis is that this longer event spans two beats but not of equal durations. Since the first 3 events have similar durations, we hypothesize that a NI grid based on a 5|4 polyrhythm can reproduce this pattern, with the 3 Long beats aligned to the first 3 events. Finally, as previously, _S_ is chosen to minimize the difference between the theoretical and observed mean durations. The results are summarized in Table 3. 

Long beats and a single Short beat. Since the NI grid has the same number of beats as the number of events in the Samba pattern, all four beats coincide with an event (Figure 8) and the shortest event duration (event 2) is aligned to the Short beat of the NI grid. Then, _S_ is chosen so that it minimizes the difference between the theoretical beat durations and the mean event durations for the three different tempi. The results are summarized in Table 2. 

The three different Samba patterns correspond to three different shifts _S_ , so that events 1 and 2 of the Samba pattern are well aligned to the NI grid at all three tempi. However, since the NI grids consist of only two beat classes, events 1, 3 and 4 are matched to beats with the same duration and therefore this model cannot capture the characteristic longer 4<sup>th</sup> event and the difference in the durations of the two Medium events (1 and 3). 

The 5-beat formative pulse hypothesis reproduces more accurately the observed Samba pattern. The differences between the theoretical and observed durations are below the respective standard deviations, except for event 2 and 3 at the preferred tempo. This is indicative of the inability of the 5|2 model to capture the subtle difference between the two Medium events. 

## **4.2 The 5-beat formative pulse hypothesis** 

Introducing a subdivision to the Formative and Target pulses can address the above shortcoming of the model. A 

Our second hypothesis is that the observed Medium-ShortMedium-Long pattern stems from the superposition of  5- 

150 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

|Tempo||Event n|umber||
|---|---|---|---|---|
|NIgrid|1|2|3|4|
|Fast|115.7|74.5|115.7|149.0|
|_NI_(5|2, 0.18)|(5.3)|(5.5)|(3.7)|(3.9)|
|Preferred|150.8|101.2|150.8|202.3|
|_NI_(5|2, 0.16)|(6.2)|(**8.8**)|(**8.8**)|(6.3)|
|Slow|205.3|205.3|205.3|256.0|
|_NI_(5|4, 0.71)|(6.7)|(7.3)|(0.7)|(0.0)|
||<br>Alternativ|<br>e NI grids|<br>||
|Preferred|164.9|110.3|137.6|192.2|
|_NI_(10|4, 0.55)|(7.9)|(0.3)|(4.4)|(3.8)|
|Slow|205.3|205.3|205.3|256.0|
|_NI_(10|4, 0.71)|(6.7)|(7.3)|(0.7)|(0.0)|



**Table 3** : Theoretical durations in ms for the four samba events based on the NI grids of Figure 9. In parenthesis, the differences between the theoretical durations and the observed mean durations for the respective events are shown. Differences greater than the respective standard deviations are shown in bold. 

10|4 NI grid can reproduce the differences between the durations of event 1 and 3 (Figure 9 and Table 3,  alternative NI grids). The period of the 10-beat Formative pulse at the this tempo is 61ms, which is below the perceptual threshold mentioned in section 2.1 for metrical subdivisions. Nevertheless, it may still be a plausible hypothesis considering the shortest event duration in the pattern at hand is 69ms. A similar hypothesis for the fast tempo would result in a period of 46ms for the Formative pulse, which was considered too fast within this context and was ommited. At the slow tempo, the alignment of the 10-beat Formative pulse is identical to the 5-beat one and thus offers no advantage. 

## **4.3 Tempo dependence** 

The above hypotheses provide alternative explanations to those given in [10] for the tempo dependence of the basic samba pattern. 

In the 4-beat formative hypothesis, we reproduce the patterns by gradually changing the shift _S_ , from an almost purely binary pattern at slow tempo to a mixed character pattern at faster tempi. As the tempo becomes faster, the 4- beat pulse approaches the lower threshold for a metrical subdivision and events are pulled from their formative positions (period of 114ms) towards the ternary subdivision (period of 151ms), which is still significantly above the threshold. 

In the 5-beat formative hypothesis, the tempo dependence is explained by the introduction of a subdivision in the target pulse at the slow tempo and change to the polyrhythmic structure from 5|2 to 5|4. At the preferred tempo, the small value of _S_ indicates that events are mainly attracted to the faster 5-beat pulse (period of 121ms) and to a lesser extend to the slower binary subdivision (period of 303ms). As the tempo increases, S moves towards the binary pulse, possibly due to the 5-beat pulse crossing the 100ms threshold (91ms period). At the slow tempo, the binary pulse is subdivided, resulting in pulses with moderate 

periods (174ms for the 5-beat pulse and 218ms for the 4- beat pulse) and a more mixed character pattern. 

## **5. CONCLUSION** 

In this paper, we formalize a novel model for non-isochronous and micro-timing rhythmic patterns that departs from theoretical and cognitive models that emphasize the hierarchical grouping of isochronous pulses prevalent in Western classical music theories. Instead, our model is rooted in non-hierarchical polyrhythmic relationships, such as those found in African polyphony. By incorporating polyrhythmic structures consisting of two pulses, our approach integrates both the structural/macro level and the expressive/micro level of musical rhythms, which are traditionally treated as separate. The resulting construct of nonisochronous (NI) grids unifies these levels within a novel framework. Non-isochronous groupings such as the Euclidean rhythms are then a special case of the model. While, NI grids can model systematic timing deviations from isochrony, not all deviations from isochrony can be accounted for by NI grids, and expressive timing may introduce micro-timing deviations to NI grids. 

Our model is a music-theoretical one and is not intended to represent cognitive processes directly. However, some of its predictions may be relevant to music cognition. For example, it has previously been argued that only two beat classes, Long and Short, are perceptually relevant and that Medium duration events must be understood as expressive variants of these two beat classes [48]. A subsequent study showed that this is indeed the case in Mali Drum Ensemble music [49]. Our model makes similar predictions about the existence of only two beat classes, albeit for different reasons and with different implications for the observed patterns. To assess the perceptual relevance of these predictions, further analysis of musical performances and behavioral experiments are needed. 

The potential of non-isochronous grids in music analysis was demonstrated in the example of Brazilian Samba. We developed two concrete hypotheses for the basic Samba pattern reported in the literature [10], which model the most salient features of the measured event durations and offer alternative explanations and interpretations for their tempo dependence. Polyrhythmic interpretations of the non-isochronous patterns observed in Samba performances have been hypothesized before, for example in [9]. However, such hypotheses are typically explored in a phenomenological and abstract, conceptual form. Our model provides the basis for a formalized method of determining the details of the polyrhythmic and micro-timing character of the observed durational patterns. 

A future study will further test our preliminary hypotheses and compare them with other accounts of samba patterns. For example, we will investigate the possibility that some of the variation in measured durations may be due to a dynamic shift _S_ that changes from one repetition of the pattern to the next. In addition, we will explore the development and evaluation of automated methods for discovering NI grids that can account for the durational patterns observed in music from various genres and music traditions. 

151 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

## **6. REFERENCES** 

- [1] J. London, _Hearing in Time: Psychological Aspects of Musical Meter_ . New York: Oxford University Press, 2012. doi: 10.1093/acprof:oso/9780199744374.001.0001. 

- [2] H. Honing, ‘Structure and Interpretation of Rhythm in Music’, in _The Psychology of Music_ , D. Deutsch, Ed., 3rd ed.Academic Press, Elsevier, 2012, pp. 367–404. 

- [3] E. W. Large and M. R. Jones, ‘The dynamics of attending: How people track time-varying events.’, _Psychological Review_ , vol. 106, no. 1, pp. 119–159, 1999, doi: 10.1037//0033-295X.106.1.119. 

- [4] M. R. Jones, ‘Musical time’, in _The oxford handbook of music psychology_ , S. Hallam, I. Cross, and M. Thaut, Eds., New York: Oxford University Press, 2008, pp. 81–92. doi: 10.1093/oxfordhb/9780199298457.013.0008. 

- [5] E. W. Large _et al._ , ‘Dynamic models for musical rhythm perception and coordination’, _Front. Comput. Neurosci._ , vol. 17, p. 1151895, May 2023, doi: 10.3389/fncom.2023.1151895. 

- [6] R. Parncutt, ‘A perceptual model of pulse salience and metrical accent in musical rhythms’, _Music Perception_ , vol. 11, no. 4, pp. 409–464, 1994. 

- [7] N. Jacoby and J. H. McDermott, ‘Integer Ratio Priors on Musical Rhythm Revealed Cross-culturally by Iterated Reproduction’, _Current Biology_ , vol. 27, no. 3, pp. 359–370, 2017, doi: 10.1016/j.cub.2016.12.031. 

- [8] A. Gabrielsson, ‘Interplay between Analysis and Synthesis in Studies of Music Performance and Music Experience’, _Music Perception_ , vol. 3, no. 1, pp. 59–86, Oct. 1985, doi: 10.2307/40285322. 

- [9] L. Naveda, F. Gouyon, C. Guedes, and M. Leman, ‘Microtiming Patterns and Interactions with Musical Properties in Samba Music’, _Journal of New Music Research_ , vol. 40, no. 3, pp. 225–238, Sep. 2011, doi: 10.1080/09298215.2011.603833. 

- [10] M. R. Haugen and A. Danielsen, ‘Effect of tempo on relative note durations in a performed samba groove’, _Journal of New Music Research_ , vol. 49, no. 4, pp. 349–361, Aug. 2020, doi: 10.1080/09298215.2020.1767655. 

- [11] G. Guillot, ‘Multi-level Anisochrony in Afro-Brazilian music’, _GMTH Proceedings_ , pp. 406–421, 2022, doi: 10.31751/p.200. 

- [12] R. Polak, ‘Rhythmic Feel as Meter : Non-Isochronous Beat Subdivision in Jembe Music from Mali’, _Music Theory Online_ , vol. 16, no. 4, pp. 1–26, 2010. 

- [13] M. R. Haugen, ‘Investigating Musical Meter as Shape: Two Case Studies of Brazilian Samba and Norwegian Telespringar’, in _Proceedings of the 25th Anniversary Conference of the European Society for the Cognitive Sciences of Music_ , E. Van Dyck, Ed., Ghent, Belgium, 2017, pp. 67–74. 

- [14] E. F. Clarke, ‘Levels of structure in the organization of musical time’, _Contemporary Music Review_ , vol. 2, no. 1, pp. 211–238, Jan. 1987, doi: 10.1080/07494468708567059. 

- [15] M. E. P. Davies and S. Bock, ‘Evaluating the Evaluation Measures for Beat Tracking’, presented at the International Society for Music Information Retrieval Conference, 2014. 

- [16] M. J. Velasco and E. W. Large, ‘Pulse Detection in Syncopated Rhythms Using Neural Oscillators’, in _Proceedings of the 12th International Society for Music Information Retrieval Conference_ , A. Klapuri and C. Leider, Eds., Miami, Florida, USA: University of Miami, 2011. 

- [17] E. W. Large, J. A. Herrera, and M. J. Velasco, ‘Neural Networks for Beat Perception in Musical Rhythm’, _Front. Syst. Neurosci._ , vol. 9, no. November, Nov. 2015, doi: 10.3389/fnsys.2015.00159. 

- [18] F. Lerdahl and R. Jackendoff, _A Generative Theory of Tonal Music_ . Cambridge, Massachusetts: The MIT Press, 1983. 

- [19] M. Yeston, _The Stratification of Musical Rhythm_ . New Haven, CT: Yale University Press, 1976. 

- [20] H. Krebs, _Metrical dissonance in the music of Robert Shumann_ . New York, Oxford: Oxford University Press, 1999. 

- [21] V. K. Agawu, _Representing African music: postcolonial notes, queries, positions_ . New York: Routledge, 2003. 

- [22] S. Arom, _African polyphony and polyrhythm_ . Cambridge University Press, 1991. doi: 10.1017/CBO9780511518317. 

- [23] C. D. Stover, ‘A theory of flexible rhythmic spaces for diasporic African music’, PhD, University of Washington, 2009. doi: /10.7560/LAMR37202. 

- [24] A. Danielsen, _Presence and Pleasure: The Funk Grooves of James Brown and Parliament_ . Middletown, CT: Wesleyan University Press, 2006. 

- [25] G. Sioros, G. Madison, D. Cocharro, A. Danielsen, and F. Gouyon, ‘Syncopation and Groove in Polyphonic Music: Patterns Matter’, _Music Perception_ , vol. 39, no. 5, pp. 503–531, Jun. 2022, doi: 10.1525/mp.2022.39.5.503. 

- [26] R. Polak, J. London, and N. Jacoby, ‘Both isochronous and non-isochronous metrical subdivision afford precise and stable ensemble entrainment: A corpus study of malian jembe drumming’, _Frontiers in Neuroscience_ , vol. 10, no. JUN, pp. 1–11, 2016, doi: 10.3389/fnins.2016.00285. 

- [27] G. Sioros and C. Guedes, ‘Syncopation as Transformation’, in _Sound, Music and Motion_ , M. Aramaki, O. Derrien, R. Kronland-Martinet, and S. Ystad, Eds., in Lecture Notes in Computer Science, vol. 8905. Springer International Publishing, 2014, pp. 635–658. doi: 10.1007/978-3-319-12976-1. 

- [28] C. Barlow and H. Lohner, ‘Two essays on theory’, _Computer Music Journal_ , vol. 11, no. 1, pp. 44–60, 1987. 

- [29] C. Barlow, ‘Corrections for Clarence Barlow’ s Article: Two Essays on Theory’, _Computer Music Journal_ , vol. 11, no. 4, p. 10, 1987. 

- [30] G. Sioros, M. E. P. Davies, and C. Guedes, ‘A generative model for the characterization of musical rhythms’, _Journal of New Music Research_ , vol. 47, no. 2, pp. 114–128, Mar. 2018, doi: 10.1080/09298215.2017.1409769. 

152 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

- [31] M. Rohrmeier, ‘Towards a formalization of musical rhythm’, in _Proceedings of the 21st International Society for Music Information Retrieval Conference_ , Montréal, Canada, 2020, pp. 621–629. 

- [32] E. W. Large, ‘Neurodynamics of Music’, in _Music Perception_ , 2010, pp. 201–231. doi: 10.1007/978-14419-6114-3. 

- [33] S. Koelsch, P. Vuust, and K. Friston, ‘Predictive Processes and the Peculiar Case of Music’, _Trends in Cognitive Sciences_ , vol. 23, no. 1, pp. 63–77, 2019, doi: 10.1016/j.tics.2018.10.006. 

- [34] D. Huron, _Sweet anticipation: music and the psychology of expectation_ . Cambridge, Massachusetts / London, England: The MIT Press, 2006. 

- [35] B. H. Repp, ‘Rate Limits of Sensorimotor Synchronization’, _Advances in Cognitive Psychology_ , vol. 2, no. 2, pp. 163–181, Jan. 2006, doi: 10.2478/v10053008-0053-9. 

      - _Music Perception_ , vol. 28, no. 5, pp. 449–460, Jun. 2011, doi: 10.1525/mp.2011.28.5.449. 

   - [47] K. Hellmer and G. Madison, ‘Quantifying Microtiming Patterning and Variability in Drum Kit Recordings: A Method and Some Data’, _Music Perception: An Interdisciplinary Journal_ , vol. 33, no. 2, pp. 147–162, Dec. 2015, doi: 10.1525/mp.2015.33.2.147. 

   - [48] J. London, ‘Commentary’, _Music Theory Online_ , vol. 16, no. 2, 2010. 

   - [49] H. Neuhoff, R. Polak, and T. Fischinger, ‘Perception and Evaluation of Timing Patterns in Drum Ensemble Music from Mali’, _Music Perception_ , vol. 34, no. 4, pp. 438–451, Apr. 2017, doi: 10.1525/mp.2017.34.4.438. 

- [36] E. F. Clarke, ‘Categorical Rhythm Perception: an Ecological Perspective’, in _Action and Perception in Rhythm and Music_ , A. Gabrielsson, Ed., Stockholm: Royal Swedish Academy of Music, 1987, pp. 19– 33. 

- [37] P. Desain and H. Honing, ‘The Quantization of Musical Time: A Connectionist Approach’, _Computer Music Journal_ , vol. 13, no. 3, p. 56, Jan. 1989, doi: 10.2307/3680012. 

- [38] P. Desain and H. Honing, ‘The formation of rhythmic categories and metric priming’, _Perception_ , vol. 32, no. 3, pp. 341–365, 2003, doi: 10.1068/p3370. 

- [39] M. L. A. Jongsma, P. Desain, and H. Honing, ‘Rhythmic context influences the auditory evoked potentials of musicians and nonmusicians’, _Biological Psychology_ , vol. 66, no. 2, pp. 129–152, Apr. 2004, doi: 10.1016/j.biopsycho.2003.10.002. 

- [40] E. W. Large, ‘Rhythm Categorization in Context’, in _Large, Edward W. ‘Rhythm categorization in context.’ Proceedings of the International Conference on Music Perception and Cognition_ , Keele, UK, 2000. 

- [41] J. Clough and J. Douthett, ‘Maximally Even Sets’, _Journal of Music Theory_ , vol. 35, no. 1/2, pp. 93– 173, 1991, doi: 10.2307/843811. 

- [42] R. Cohn, ‘A Platonic Model of Funky Rhythms’, _Journal of the Society for Music Theory_ , vol. 22, no. 2, 2016, doi: 10.30535/mto.22.2.1. 

- [43] G. T. Toussaint, ‘The Euclidean algorithm generates traditional musical rhythms’, in _Proceedings of BRIDGES: Mathematical Connections in Art, Music and Science_ , Banff, Alberta,, Canada, 2005, pp. 47– 56. 

- [44] G. T. Toussaint, _The Geometry of Musical Rhythm: What Makes a ‘Good’ Rhythm Good?_ Chapman and Hall/CRC, 2013. 

- [45] A. Danielsen, ‘The Sound of Crossover: Microrhythm and Sonic Pleasure in Michael Jackson’s “Don’t Stop 'Til You Get Enough”’, _Popular Music and Society_ , vol. 35, no. 2, pp. 151–168, 2012, doi: 10.1080/03007766.2011.616298. 

- [46] D. Moelants, ‘The Performance of Notes Inégales: The Influence of Tempo, Musical Structure, and Individual Performance Style on Expressive Timing’, 

153 

