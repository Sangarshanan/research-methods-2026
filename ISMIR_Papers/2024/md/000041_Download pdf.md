---
paper_id: "000041"
year: 2024
title: "Download pdf"
source_url: "https://zenodo.org/record/14877355/files/000041.pdf"
---

# **INNER METRIC ANALYSIS AS A MEASURE OF RHYTHMIC SYNCOPATION** 

## **Brian Bemman** 

Durham University 

brian.m.bemman@durham.ac.uk 

**Justin Christensen** University of Sheffield 

j.christensen@sheffield.ac.uk 

### **ABSTRACT** 

Inner Metric Analysis (IMA) is a method for symbolic music analysis that identifies strong and weak metrical positions according to coinciding periodicities within note onsets. These periodicities are visualized with bar graphs known as _metric weight_ and _spectral weight profiles_ . Analyzing these profiles for the presence of syncopation has thus far required manual inspection. In this paper, we propose a simple measure using chi-squared distance for quantifying the level of syncopation found in IMA weight profiles by considering each as a distribution to be compared against (1) a uniform distribution ‘nominal’ weight profile, and (2) a non-uniform distribution based on beat strength. We apply this measure to the task of predicting perceptual ratings of syncopation using the Song (2014) dataset of 111 single-bar rhythmic patterns and compare its performance to seven existing models of syncopation/complexity. Our results indicate that the proposed measure based on (1) achieves a moderately high Spearman rank correlation (rs = 0.80) to all ratings and is the only single measure that reportedly works across all categories. For so-called polyrhythms in 4/4, the measure based on (2) surpasses all other models and further outperforms five models for monorhythms in 6/8 and three models for monorhythms in 4/4. 

### **1. INTRODUCTION** 

Much research has gone into understanding the perception of temporal patterns [1–3] and many more recent studies within this scope have focused on the perceived levels of syncopation and complexity in these patterns [4–11]. Subsequently, a number of different computational methods have been proposed for modeling these, including models that are based on a metric hierarchy using tree-based structures [7,12–14] and those that are not [15–19]. Many of these models have been tested on various perceptual tasks, such as syn- 

> © B. Bemman, and J. Christensen. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). **Attribution:** B. Bemman, and J. Christensen, “Inner Metric Analysis as a Measure of Rhythmic Syncopation”, in _Proc. of the 25th Int. Society for Music Information Retrieval Conf.,_ San Francisco, United States, 2024. 

copation prediction, and their respective performances have been compared [6,9,20–23]. However, none of the comparisons carried out to date have considered Inner Metric Analysis [24]. 

Inner Metric Analysis (IMA) is a method of symbolic music analysis for identifying strong and weak metrical positions in a piece based on coinciding periodicities found in its note onsets [24]. Over the years, IMA has been applied to the tasks of automatic meter detection [25] and dance music classification [26], but it has largely been used in more traditional music analysis contexts [24,27]. An important feature of IMA is its ability to provide a representation of the _inner_ metric structure of a piece rather than a representation tied to its _outer_ metric structure–––the meter as indicated by the time signature in a score. This feature allows IMA to identify, for example, instances where the notated music conflicts with the implied or perceived meter. For this reason, it has been used to aid in the identification of syncopation [24], which has typically been defined as a temporary displacement of the regular metrical accent [28]. However, until now the use of IMA to identify syncopation in a musical passage has required manual analysis by a music theorist or other domain expert. 

In this paper, we propose using chi-squared distance as a first step towards computing a quantifiable measure of syncopation from weight profiles produced by IMA. We apply this method to the task of predicting perceptual ratings of syncopation in the Song (2014) [22] dataset containing 111 one-bar rhythmic patterns in two different meters and rhythm types (i.e., monorhythms in 4/4, monorhyhms in 6/8, and so-called polyrhythms in 4/4). In section 2, we explain how IMA produces a metrical analysis of a musical passage and detail the rhythmic patterns in the Song (2014) dataset. In section 3, we introduce our proposed measure based on chi-squared distance for comparing the weight profiles produced by IMA to a uniform distribution or ‘nominal’ weight profile as well as to a non-uniform distribution based on beat strength [29]. We evaluate this measure in section 4 by testing it on the aforementioned dataset and compare its performance to the reported performances of seven existing models of syncopation/complexity. We summarize our findings in section 5 and suggest possible directions for future work. 

389 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 



<!-- Start of picture text -->
On ★ ★ ★ ★ ★ ★<br>A 0 2● 3 4 5 9 7 HI<br><!-- End of picture text -->

**Figure 1** . Opening bars of the “Twinkle, Twinkle Little Star” melody and single local meter (A) with its pulses (black circles) generated by Inner Metric Analysis (IMA). Note that stars denote onsets (On). 

### **2. RELATED WORK** 

### **2.1 Inner Metric Analysis (IMA)** 

IMA computes, from the note onsets of a piece, an exhaustive listing of _local meters_ —each of which must be a sub-sequence of onsets or _pulses_ that are (1) at least 3 in number, (2) separated by a fixed inter-onset interval, called the _period_ , (3) not able to be extended further (forwards or backwards in time) within the sequence of all onsets of the piece, and (4) not contained within the pulses belonging to any other local meter. Figure 1 shows the opening two bars of “Twinkle, Twinkle Little Star” with its single local meter. Note that the single local meter (A) contains at least 3—in this case, 7, evenly-spaced pulses (black circles), each aligned with a corresponding onset in the music above. The numbers at the bottom indicate the positions within an underlying “grid” called _time points_ , equivalent to _tatums_ , upon which the onsets are fitted. Because all adjacent onsets have an equal, constant spacing, represented in the score as quarter-note durations, no time point exists between them. In such passages, there will be only a single local meter as any other possible set of pulses would necessarily be contained within this local meter. For more complex rhythms, this will not be the case. 

Following the enumeration of all local meters in a piece, IMA computes a _metric weight_ for each onset based on the number of pulses in local meters that coincide with this onset and the lengths of those local meters to which these pulses belong. Formally, let _On_ be the set of all onset time points in a piece and m be a local meter that contains an onset, o, and where km denotes the length of m minus 1. M (l) denotes the set of all local meters of length at least l, where in straight-forward implementations of IMA, l is 2 (equal to the minimum number of pulses, 3, minus 1). The metric weight of o is defined as the sum of the values, km, of the local meters, m, that contain o. The metric weight of an onset o ∈ On is thus given by 



<!-- Start of picture text -->
Wl,p(o) = ∑ (km) p , (1)<br>{m∈M (l):o∈m}<br><!-- End of picture text -->

where p is a weighting parameter typically set to p = 2 that is used to control the relative influence of the length of local meters on the metric weight [24]. For example, the metric weight assigned to each of the 7 onsets of the melody shown in Figure 1, using the 



<!-- Start of picture text -->
10<br><!-- End of picture text -->

**Figure 2** . Opening bars of a syncopated variation of the “Twinkle, Twinkle Little Star” melody with all ten (A–J) local meters and their extensions (red triangles) generated by Inner Metric Analysis (IMA). 

typical weighting parameter of p = 2, would be (7 − 1)<sup>2</sup> = 36, as each onset has only a single pulse (i.e., no coinciding pulses) belonging to one local meter of length 7 − 1 = 6. 

In addition to the metric weight, IMA also computes a _spectral weight_ that considers the _extension_ of each local meter to certain time points on the grid that align with either onsets or silence (i.e., rests) in a piece. Formally, an extension, ext(m), of a local meter, m, is defined as the set of time points, {s+id, ∀i}, where s denotes the time point of the first onset in m, d is the period, and i is an integer time point in the underlying grid. Figure 2 shows a syncopated variation of the melody shown in Figure 1 with all ten of its local meters (A–J) and extensions (red triangles). Note that, in contrast to Figure 1, there are multiple local meters (ten) where no one local meter is contained within the pulses belonging to any other local meter. Take, for example, local meter (E), which shares two of its pulses (time points 1 and 7) with local meter (D), but contains a third (time point 4) that is not shared with (D). The purpose of extensions in IMA is to allow for pulses to contribute to parts of passages where they are not even present. The case for projecting pulses further in time in this way through extensions, for example, is made stronger when one considers the possibility for some latent or persisting pulse in the listener’s perception. The spectral weight is computed in a similar manner to the metric weight (shown in Equation 1), except that it assigns a weight to each time point (rather than only to each onset) based on the pulses and now extensions which coincide with this time point. For a time point, t, the spectral weight is given by 



<!-- Start of picture text -->
SWl,p(t) = ∑ (km) p . (2)<br>{m∈M (l):t∈ext(m)}<br><!-- End of picture text -->

Whereas the metric weight of, for example, the first onset (at time point 0) shown in Figure 2, would consider only local meter (H) due to it having the only coinciding pulse, the spectral weight would consider the additional contributions of local meters (A, B, C, G), due to their coinciding extensions. 

390 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 



<!-- Start of picture text -->
Metric Weight Profile<br>60<br>40<br>20<br>0<br>0 2 4 6 8 10 12 14<br>Time point<br>(a)<br>Spectral Weight Profile<br>60<br>40<br>20<br>0<br>0 2 4 6 8 10 12 14<br>Time point<br>(b)<br>Weight<br>Weight<br><!-- End of picture text -->

**Figure 3** . The metric and spectral weight profiles of the opening two bars of the syncopated “Twinkle, Twinkle Little Star” melody from Figure 2 with metric weights shown in (a) and spectral weights shown in (b), as computed by Inner Metric Analysis (IMA). 

Whether an analysis of a piece by IMA uses metric weights or spectral weights, it is typical for the weights to be plotted in the form of a bar graph called a _profile_ . With a trained eye, musical features of a piece such as a possible meter (whether notated or not) and syncopation often emerge through visual inspection of the profile. Figure 3 shows the _metric weight profile_ and _spectral weight profile_ for the opening two bars of the syncopated “Twinkle, Twinkle Little Star” melody shown in Figure 2. Given that the actual meter of the syncopated melody in Figure 2 is known, we can see in its corresponding weight profiles, shown in Figure 3, that all lower weights at time points 0, 2, 4, 6, 8, 10, 12, 14 appear at on-beat locations while all higher weights at time points 1, 3, 5, 7, 9, 11, 13, 15 appear at offbeat locations, suggesting a strong possibility for the presence of syncopation. 

### **2.2 The Song (2014) Syncopation Dataset** 

Datasets containing rhythmic (or temporal) patterns for studying human perception remain relatively few in number and small in size [1–4,7,30,31]. A number of these early datasets were originally constructed as a means for evaluating perceptual complexity and have since been co-opted for the study of syncopation [5, 

6]. Even fewer datasets exist for the explicit study of syncopation [7, 22, 32, 33], however, the Song (2014) [22] dataset is arguably one of the largest. 

The Song (2014) [22] dataset contains 111 singlebar rhythmic patterns (and their mean listener perceptual ratings from 0 to 4) in two possible meters, 4/4 and 6/8, and of two different rhythm types, mono and poly.<sup>1</sup> There are 27 monorhythm patterns in 4/4 (15 on quarter-note grid; 12 on eighth-note grid), 36 monorhythm patterns in 6/8 (eighth-note grid), and 48 so-called polyrhythm patterns in 4/4 (quarter-note triplet grid)—each of which were preceded for listeners by an audible two-bar metronome in their respective meter. Patterns in each category range from having a single onset (e.g., ⟨0, 0, 0, 1⟩ monorhythm in 4/4 with an onset on the fourth beat) up to a number of onsets equal to the number of time points in the underlying grid (e.g., ⟨1, 1, 1, 1, 1, 1⟩ monorhythm in 6/8 of all eighth notes). 

### **3. PROPOSED MEASURE OF SYNCOPATION USING IMA** 

The central premise motivating our proposed measure is the consideration of weight profiles produced by IMA as distributions through which comparisons with other distributions using chi-squared distance [34] can provide insight into the underlying rhythmic structure that is relevant to predicting syncopation. We consider two possible distributions that we will compare against the weight profiles produced by IMA for a given rhythmic pattern: (1) a uniform distribution based on what we call a ‘nominal’ weight profile that operates conservatively and in the spirit of IMA without knowledge of the underlying meter, and (2) a nonuniform distribution based on beat strength [29] that operates with explicit knowledge of the underlying meter and is nearly analogous to a nominal weight profile but for metrical (hierarchy) structure. A nominal weight profile is the uniform distribution of weights that results from an IMA analysis of any sequence consisting entirely of equally-spaced onsets irrespective of the hierarchical metrical level at which these are expressed. For example, a pattern in 4/4 consisting of all quarter notes, half-notes, or eighth notes will each result in a nominal weight profile. Our motivation for considering nominal weight profiles is based on a simplifying assumption that a less syncopated rhythmic pattern or passage of music will have more equal weighting across its weight profile than a more syncopated pattern or passage. This was observed, for example, in Figures 1 and 2, with the less syncopated melody containing a single local meter resulting in a metric weight profile containing at each onset a constant weight and its syncopated version containing multiple local meters resulting in weight pro- 

> 1 The complete Song (2014) [22] dataset and perceptual ratings can be found in the following repository: https://code. soundsoftware.ac.uk/projects/syncopation-dataset. 

391 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

files (shown in Figure 3) containing a variable weight that fluctuates over time. Our motivation in (2) for considering non-uniform distributions based on beat strength comes from the fact that clearly not all rhythmic patterns consist of all equally-spaced onsets, and, much like previous models of syncopation, such as Weighted Note-to-Beat Distance (WNBD) [17] or the Longuet-Higgins and Lee (LHL) model [12], providing additional information beyond what is explicitly available in the onsets (e.g., beat locations or rests), can provide relevant (or indeed necessary) information for modelling or predicting syncopation. 

The proposed measure adopts two different constructions for handling normalization across patterns and distributions, both of which we will use in our evaluation. The first of these constructions considers a given metric or spectral weight profile produced by IMA as a normalized distribution, P<sup>′</sup> , scaled to unit length and a second, un-normalized uniform distribution, Q, representing a nominal weight profile having some constant value, Qi for all i. The measurenormalized (weighted) chi-squared distance,<sup>χ</sup> D1, between two distributions P<sup>′</sup> and Q of length n (time points) is given by 



<!-- Start of picture text -->
n−1 ( P i ′ − Q i ) 2<br>IMAM,S χ D1 = n 1 ∑i=0 ( (Pi ′ + Qi) ) a , (3)<br><!-- End of picture text -->

where a is a weighting parameter (discussed in section 4) and n <mark>1</mark><sup>servestonormalizethedistanceby</sup> measure length. By calculating the distance of an observed weight profile from a nominal weight profile, we obtain a measure of the overall aperiodicity or irregularity of the rhythmic content (relative to the constant, Qi, in the uniform distribution), where the higher the overall value, the greater the amount of perceived syncopation there is predicted to be. In principle, while the constant Qi could be any rational value, for the purposes of this paper, we will utilize a constant value between [0, 1] corresponding to the maximum upper and minimum lower ranges of the P<sup>′</sup> distribution. In addition to the a weighting parameter, an optimal constant value for Qi will be learned in section 4. 

Whereas the Q uniform distribution in Equation 3 was left un-normalized to allow for various constant values to be learned, which would otherwise disappear with normalization, other distributions, such as our non-uniform distribution based on beat strength, will require normalization for fair comparisons with P<sup>′</sup> . Thus, an alternative weighted construction,<sup>χ</sup> D2, of Equation 3 appears below for the same normalized distribution, P<sup>′</sup> , and another normalized distribution, S<sup>′</sup> , also of length n and scaled to unit length: 



<!-- Start of picture text -->
n−1 ( P i ′ − S i ′ ) 2<br>IMAM,S χ D2 = ∑ , (4)<br>i=0 ( (Pi ′ + S i ′) ) a<br><!-- End of picture text -->

where a is the same weighting parameter as in 

the earlier construction. Note that because both distributions have been scaled to unit length, normalizing by measure length, n, as was done in Equation 3, is no longer necessary. In our use of Equation 4, we consider four different distributions for S<sup>′</sup> , corresponding to the beat strengths produced by music21 [29] (using the beatStrength method) for each of the four different types of meter/rhythm types found in the Song (2014) [22] dataset. The following four (un-normalized) beat strength distributions are those used with this construction: (1) 4/4 meter with quarter-note grid ⟨1.0, 0.25, 0.5, 0.25⟩, (2) 4/4 meter with eighth-note grid ⟨1.0, 0.125, 0.25, 0.125, 0.5, 0.125, 0.25, 0.125⟩, (3) 6/8 meter with eighth-note grid ⟨1.0, 0.25, 0.25, 0.5, 0.25, 0.25⟩, and (4) 4/4 meter with quarter-note triplet grid ⟨1.0, 0.0625, 0.0625, 0.25, 0.0625, 0.0625, 0.5, 0.0625, 0.0625, 0.25, 0.0625, 0.0625⟩. 

### **4. EVALUATION** 

We have evaluated our IMA-based measure on the Song (2014) [22] dataset of 111 one-bar rhythmic patterns and their perceptual ratings of syncopation for three reasons: (1) there is a relatively large number of stimuli in comparison to other available datasets, (2) the stimuli were constructed specifically for the purpose of studying syncopation and not, for example, complexity or groove, and (3) there has been significant work already done on evaluating other computational models of syncopation with this dataset. The reader is referred to [22] for an in-depth discussion of the performances of existing models using this dataset. 

### **4.1 Procedure** 

We have adopted an optimization approach using leave-one-out cross-validation in which we performed a grid search over the pair of parameters, Qi, and a from Equation 3 for 100<sup>2</sup> value-pairs within the range [0, 1] in increments of 0.01. For each distinct weighting parameter pair, we carried out the procedure below for all rhythmic patterns in the training set: 

1. Repeat the time-span note sequence of the given Song (2014) [22] one-bar rhythmic pattern twelve times. As IMA requires at least three pulses to form a local meter, it is generally less effective with short rhythmic patterns having few onsets. For this reason, it has been suggested in [26] to repeat short patterns in this way when using IMA. 

2. Convert this extended time-span note sequence from (1) to an ordered set of note onset indices suitable for analysis by IMA e.g., ⟨0, 1, 0, 1⟩ to ⟨1, 3⟩ (using 0-based indexing). 

3. Compute IMA metric and spectral weight profiles for this extended twelve-bar rhythmic pat- 

392 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

tern from (2) using an IMA weighting parameter p = 2 and minimum local meter length, l = 2. 

4. ‘Fold’ the metric and spectral weight profiles in (3) into single bars and sum those weights at each time point having equivalent within-bar locations. Then scale each weight profile to unit length such that they each sum to 1. 

5. Compute a measure of syncopation from each normalized single-bar metric and spectral weight profile from (4) using Equation 3 and the given weighting parameter pair, Qi and a. 

Following the procedure above for all training rhythmic patterns and a given weighting parameter pair, the respective sets of syncopation scores computed for each of the metric and spectral weight profiles are min-max normalized. The Spearman rank correlation coefficient, rs, is then computed for each of these sets of syncopation scores and the min-max normalized mean perceptual ratings, in the same way that was done for each of the computational models evaluated in [22, pp. 92–94] so that fair comparisons could be made. The procedure for using Equation 4 and the non-uniform distributions based on beat strength is identical to the steps outlined above, except the grid search was performed across all 100 values between [0, 1] for a only, and the set of beat strengths chosen for any given pattern was that matching in number of time points, n. The weight parameter (Equation 4) or weight parameter pair (Equation 3) that produced the highest mean rank correlation achieved across all k-folds was retained and the final results below are reported using the best parameters across the entire dataset. All syncopation-dependent procedures were implemented in Julia (v. 1.10.0) and all statistical calculations were made with R (v. 4.3.2). 

### **4.2 Results and Discussion** 

We compare the performance of the proposed measure to the reported performances of seven models of syncopation/complexity previously evaluated in [22] and [21, 23] on the same dataset. These models are Longuet-Higgins and Lee (LHL) [12], Off-Beatness (TOB) [16], Metric Complexity (TMC) [14], Weighted Note-to-Beat Distance (WNBD) [17], Cognitive Complexity (PRS) [13], Off-beat model (KTH) [15], and Sioros et al. (SG) [7]. Table 1 shows the results of our IMA-based measure of syncopation for both the metric and spectral weight profiles using the two proposed distributions across the dataset in comparison to these other models. 

In Table 1, the best weighting parameters found for Equation 3 (<sup>χ</sup> D1) were a = 1.0 for both metric and spectral weight and Qi = 0.74 for metric weight and Qi = 0.83 for spectral weight. The best weighting parameters for Equation 4 (<sup>χ</sup> D2) were a = 0.82 

> 3 There may be disagreement as to whether polyrhythms in the Song (2014) [22] dataset are what they claim and whether some existing models are in fact incapable of analyzing these 

|||Rhythm <br>|Type & <br>|Meter<br>||
|---|---|---|---|---|---|
||Model/Measure|Mono <sup>4</sup>4|Mono <sup>6</sup>8|Poly <sup>4</sup>4|Total|
|1.|IMAM<sup>χ</sup>D1|0.53*|0.67*|0.46*|0.80*|
|2.|IMAS<sup>χ</sup>D1|0.51*|0.67*|0.39*|0.79*|
|3.|IMAM<sup>χ</sup>D2|0.86*|0.74*|0.73*|0.66*|
|4.|IMAS<sup>χ</sup>D2|0.83*|0.74*|0.70*|0.61*|
|5.|LHL|0.86*|0.68*|-||
|6.|TMC|0.92*|0.67*|-||
|7.|PRS|0.95*|0.76*|-||
|8.|SG|0.88*|0.73*|-||
|9.|TOB|0.36|0.17|NA||
|10.|WNBD|0.52*|0.47*|0.41*||
|11.|KTH|0.79*|-|−0.23||



**Table 1** . Spearman correlation rank coefficients (rs) of 9 different models/measures of syncopation for 111 mono- and poly-rhythmic patterns in two meters and their perceptual ratings. For the proposed measures based on IMA (1–4), IMAM and IMAS denote use of metric and spectral weight, respectively. Note that results for models 5–11 are the values reported in [22, pp. 92–94]. An asterisk denotes where p < 0.01, a hyphen indicates where a given measure is reported as being incapable of providing a result<sup>3</sup> , and empty cells mark no reported results. 

for metric weight and a = 0.35 for spectral weight. It is clear from these results that while Equation 3 worked best across the entirety of the dataset (e.g., IMAM<sup>χ</sup> D1: rs = 0.80∗; p < 0.01—an improvement over no a weighting parameter and Qi set to an arbitrary 0.5, rs = 0.73∗; p < 0.01), it resulted in relatively poor performance within the individual categories. Perhaps not surprisingly, however, providing additional information about the underlying meter, in the form of beat strengths as done in Equation 4, significantly improved the performance in these individual categories but to the detriment of overall performance (e.g., IMAM<sup>χ</sup> D2: rs = 0.66∗; p < 0.01— same as without a). In all cases except monorhythms in 6/8, metric weight performed better than spectral weight. In particular, IMAM<sup>χ</sup> D2, outperformed all three of the existing models (TOB, WNBD, KTH) reportedly capable of providing a result for the so-called polyrhythms in 4/4 (rs = 0.73∗; p < 0.01); five of the existing models (LHL, TMC, SG, TOB, WNBD) capable of providing a result for monorhythms in 6/8 (rs = 0.74∗; p < 0.01); and only three (TOB, WNBD, KTH) of all seven models for monorhythms in 4/4 (rs = 0.86∗; p < 0.01; tying with LHL). It should be noted that in [22, p. 139] a so-called weightedmultiple combined (WMC) model using optimized versions of the best combinations of these previous models was able to achieve a rank correlation across the entire dataset of rs = 0.89 ∗ (p < 0.01). While the proposed IMA measure falls short in this regard 

without reinterpreting their meter (e.g., 4/4 to 12/8). The reader is referred to [22] for detail on these possible concerns. 

393 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 



<!-- Start of picture text -->
1.00<br>0.75<br>AAA Rhythm Type<br>4/4 Mono<br>0.50 6/8 Mono<br>4/4 Poly<br>0.25<br>Normalized Syncopation Pred i ctons<br>0.00<br>0.00 0.25 0.50 0.75 1.00<br>Normalized Mean Human Ratings<br>(a)<br>1.00<br>0.75<br>Rhythm Type<br>4/4 Mono<br>0.50<br>6/8 Mono<br>4/4 Poly<br>0.25<br>Normalized Syncopation Pred i ctons<br>0.00<br>0.00 0.25 0.50 0.75 1.00<br>Normalized Mean Human Ratings<br>(b)<br><!-- End of picture text -->

**Figure 4** . Normalized syncopation predictions produced by IMAM<sup>χ</sup> D1 (rs = 0.80∗; p < 0.01) in (a) and IMAM<sup>χ</sup> D2 (rs = 0.66∗; p < 0.01) in (b) against the normalized human ratings for the 111 rhythmic patterns in the Song (2014) [22] dataset. Note that regression lines are plotted with shaded areas indicating a 95% confidence interval. 

(rs = 0.80∗; p < 0.01), it remains noteworthy that its performance is close to approaching the performance of a significantly more complex method consisting of many different models. For completeness, Figure 4 shows regression plots of the predicted syncopation scores across the entire dataset for both IMAM<sup>χ</sup> D1 and IMAM<sup>χ</sup> D2 against the human ratings. 

The reason for the difference in performances for both constructions across the dataset versus within the individual categories is not immediately clear, however, the use of rank correlation combined with the distributed locations and smaller sizes of the respective sets of rhythm and meter type examples within the dataset is likely a contributing factor. Despite the better overall performance of Equation 3 over Equation 4, one problem with our first construction using this dataset concerns the density of pattern onsets, which has been shown to interact with their perceived displacement from a metrical hierar- 

chy in regards to syncopation [33]. Many of the patterns are highly sparse, and Equation 3 is unable to differentiate, for example, between two distinct patterns each having a single onset, such as ⟨1, 0, 0, 0⟩ and ⟨0, 1, 0, 0⟩, or the same number of equally-spaced onsets shifted in time, such as ⟨1, 0, 1, 0⟩ and ⟨0, 1, 0, 1⟩. This would help to explain its relatively low performance in the individual categories. Equation 4, on the other hand, does not encounter these same difficulties, and its improved performance in the individual categories suggests an informative structural correspondence between the metrical strengths as identified by IMA weight profiles and the beat strengths they were compared against. In an actual piece of music, however, one might expect to find relatively less sparse and more complex examples, so more ecologically valid comparisons may provide deeper insights into whether syncopated patterns have generally less equal weighting in their profiles as unsyncopated patterns, as is assumed by Equation 3. Finally, while the choice of chi-squared distance is motivated by the desire to obtain the best possible results across the entirety of the dataset using the simplest method, multiple other distance measures were tested (e.g., Euclidean and Minkowski) with the relatively more complex JensenShannon divergence [35] performing marginally better across the dataset (rs = 0.81∗; p < 0.01) but marginally worse within the individual categories. 

### **5. CONCLUSION** 

In this paper, we proposed a first step towards using Inner Metric Analysis (IMA) to provide a quantifiable measure of syncopation based on chi-squared distance and comparisons to two different types of distributions. We evaluated our method using a dataset of rhythmic patterns constructed specifically for the task of studying syncopation and compared its performance to the performances of seven existing computational models. Our results indicate that the proposed measure based on comparisons with a uniform distribution achieves a moderately high Spearman rank correlation (rs = 0.80) to all perceptual ratings and is the only single measure that reportedly works across all meters and rhythm types (mono, poly, 4/4 and 6/8). For so-called polyrhythms in 4/4, the measure based on comparisons with a distribution of beat strengths surpasses all other models and further outperforms five models for monorhythms in 6/8 and three models for monorhythms in 4/4. Finally, considering the entirety of a rhythmic sequence as done here rather than summing isolated instances of syncopation as in, for example, the LHL [12] model, appears to have higher validity [36]. In future work, it would be useful to consider other datasets, particularly ones which contain more ecologically valid examples, as well as with other distributions, possibly coming from statistical corpora studies or perceptual profiles, that could be automatically selected for in comparisons. 

394 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

### **6. ACKNOWLEDGMENTS** 

We would like to thank Tuomas Eerola, Mark Gotham, and the anonymous reviewers for their helpful suggestions during the later stages of this paper as well as David Meredith for useful feedback provided during its early stages. 

### **7. REFERENCES** 

- [1] P. J. Essens and D. J. Povel, “Metrical and nonmetrical representations of temporal patterns,” _Perception & Psychophysics_ , vol. 37, no. 1, pp. 1–7, 1985. 

- [2] D.-J. Povel and P. J. Essens, “Perception of temporal patterns,” _Music Perception: An Interdisciplinary Journal_ , vol. 2, no. 4, pp. 411–440, 1985. 

- [3] P. J. Essens, “Structuring temporal sequences: Comparison of models and factors of complexity,” _Perception & Psychophysics_ , vol. 57, no. 2, pp. 519–532, 1995. 

- [4] I. Shmulevich and D. J. Povel, “Measures of temporal pattern complexity,” _Journal of New Music Research_ , vol. 29, no. 1, pp. 61–69, 2000. 

- [5] L. M. Smith and H. Honing, “Evaluating and extending computational models of rhythmic syncopation in music,” in _Proceedings of the International Computer Music Conference_ , 2006, pp. 688– 691. 

- [6] F. Gómez, E. Thul, and G. T. Toussaint, “An experimental comparison of formal measures of rhythmic syncopation,” in _Proceedings of the International Computer Music Conference_ , 2007, pp. 101–104. 

- [7] G. Sioros, M. Miron, M. Davies, F. Gouyon, and G. Madison, “Syncopation creates the sensation of groove in synthesized music examples,” _Frontiers in Psychology_ , vol. 5, p. 1036, 2014. 

- [8] P. Vuust, M. J. Dietz, M. Witek, and M. Kringelbach, “Now you hear it: a predictive coding model for understanding rhythmic incongruity,” _Annals of the New York Academy of Sciences_ , vol. 1423, pp. 19–29, 2018. 

- [9] F. Hoesl and O. Senn, “Modelling perceived syncopation in popular music drum patterns: A preliminary study,” _Music & Science_ , vol. 1, p. 2059204318791464, 2018. 

- [10] D. Temperley, “Modeling common-practice rhythm,” _Music Perception: An Interdisciplinary Journal_ , vol. 27, no. 5, pp. 355–376, 2010. 

- [11] M. Witek, E. F. Clarke, M. L. Kringelbach, and P. Vuust, “Effects of polyphonic context, instrumentation and metric location on syncopation in 

music,” _Music Perception: An Interdisciplinary Journal_ , vol. 32, pp. 201–217, 2014. 

- [12] H. Longuet-Higgins and C. Lee, “The rhythmic interpretation of monophonic music,” _Music Perception: An Interdisciplinary Journal_ , vol. 4, no. 1, pp. 424–441, 1984. 

- [13] J. Pressing, “Cognitive complexity and the structure of musical patterns,” in _Proceedings of the 4th Conference of the Australian Cognitive Science Society_ , 2002. 

- [14] G. T. Toussaint, “A mathematical analysis of african, brazilian, and cuban clave rhythms,” in _Proceedings of BRIDGES: Mathematical Connections in Art, Music and Science_ , 2002, pp. 157–168. 

- [15] M. Keith, _From Polychords to Pólya: Adventures in Music Combinatiorics_ . Princeton: Vinculum Press, 1991. 

- [16] G. T. Toussaint, “Mathematical features for recognizing preference in sub-saharan african traditional rhythm timelines,” in _3rd International Conference on Advances in Pattern Recognition_ , 2005, pp. 18–27. 

- [17] F. Gómez, A. Melvin, D. Rappaport, and G. T. Toussaint, “Mathematical measures of syncopation,” in _Renaissance Banff: Mathematics, Music, Art, Culture_ , 2005, pp. 73–84. 

- [18] M. E. P. D. George Sioros and C. Guedes, “A generative model for the characterization of musical rhythms,” _Journal of New Music Research_ , vol. 47, no. 2, pp. 114–128, 2018. 

- [19] M. Rohrmeier, “Towards a formalization of musical rhythm,” _Proceedings of the 21st International Society for Music Information Retrieval_ , pp. 621– 629, 2020. 

- [20] E. Thul and G. T. Toussaint, “Rhythm complexity measures: A comparison of mathematical models of human perception and performance,” in _Proceedings of the 9th International Society for Music Information Retrieval Conference (ISMIR)_ , 2008, pp. 663–668. 

- [21] C. Song, A. J. R. Simpson, C. A. Harte, M. T. Pearce, and M. B. Sandler, “Syncopation and the score,” _PLoS ONE_ , vol. 8, no. 9, pp. 1–7, 2013. 

- [22] C. Song, “Syncopation: Unifying music theory and perception,” PH.D. diss., Queen Mary, University of London, 2014. 

- [23] C. Song, M. T. Pearce, and C. A. Harte, “Synpy: A python toolkit for syncopation modelling,” in _Proceedings of the 12th International Conference on Sound and Music Computing (SMC15)_ , 2015, pp. 295–300. 

395 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

- [24] A. Volk, “The study of syncopation using Inner Metric Analysis: Linking theoretical and experimental analysis of metre in music,” _Journal of New Music Research_ , vol. 37, no. 4, pp. 259–273, 2008. 

- [25] W. B. De Haas and A. Volk, “Meter detection in symbolic music using inner metric analysis,” in _Proceedings of the 17th International Society for Music Information Retrieval Conference_ , 2016, pp. 441–447. 

- [26] E. Chew, A. Volk, and C. Y. Lee, “Dance music classification using inner metric analysis,” in _The Next Wave in Computing, Optimization, and Decision Technologies_ , B. Golden, S. Raghavan, and E. Wasil, Eds. Boston, MA: Springer US, 2005, pp. 355–370. 

- [27] A. Volk, “Applying inner metric analysis to 20th century compositions,” in _Proceedings of the 1st Conference of the Society for Mathematics and Computation in Music, MCM 2007, Berlin, Germany, May 18–20, 2007_ , 2007, pp. 204–210. 

- [28] A. Latham, _The Oxford companion to music_ . Oxford University Press, 2011. 

- [29] Michael Scott Asato Cuthbert, “Music 21: A toolkit for computer-aided musicology.” [Online]. Available: https://web.mit.edu/music21/ 

- [30] W. T. Fitch and A. J. Rosenfeld, “Perception and production of syncopated rhythms,” _Music Perception: An Interdisciplinary Journal_ , vol. 25, no. 1, pp. 43–58, 2007. 

- [31] P. E. Keller and E. Schubert, “Cognitive and affective judgements of syncopated musical themes,” _Advances in Cognitive Psychology_ , vol. 7, pp. 142– 156, 2011. 

- [32] G. Sioros, A. Holzapfel, and C. Guedes, “On measuring syncopation to drive an interactive music system,” in _Proceedings of the 13th International Society for Music Information Retrieval Conference (ISMIR)_ , 2012, pp. 283–288. 

- [33] N. R. Fram and J. Berger, “Syncopation as probabilistic expectation: Conceptual, computational, and experimental evidence,” _Cognitive Science_ , vol. 47, no. 12, p. e13390, 2023. 

- [34] W. G. Cochran, “The χ2 test of goodness of fit,” _The Annals of mathematical statistics_ , pp. 315– 345, 1952. 

- [35] J. Lin, “Divergence measures based on the shannon entropy,” _IEEE Transactions on Information theory_ , vol. 37, no. 1, pp. 145–151, 1991. 

- [36] G. Sioros, G. Madison, D. Cocharro, A. Danielsen, and F. Gouyon, “Syncopation and Groove in Polyphonic Music: Patterns Matter,” _Music Perception_ , vol. 39, no. 5, pp. 503–531, 06 2022. 

396 

