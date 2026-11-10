---
paper_id: "000087"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706579/files/000087.pdf"
---

# MODELING THE DIFFICULTY OF SAXOPHONE MUSIC 

Šimon Libˇrický, Jan Hajiˇc jr. 

Institute of Formal and Applied Linguistics, Charles University `librickysimon@gmail.com, hajicj@ufal.mff.cuni.cz` 

### ABSTRACT 

In learning music, difficulty is an important factor in choice of repertoire, choice of tempo, and structure of practice. These choices are typically done with the guidance of a teacher; however, not all learners have access to one. While piano and strings have had some attention devoted to automated difficulty estimation, wind instruments have so far been under-served. In this paper, we propose a method for estimating the difficulty of pieces for winds and implement it for the tenor saxophone. We take the cost-oftraversal approach, modelling the part as a sequence of transitions – note pairs. We estimate transition costs from newly collected recordings of trill speeds, comparing representations of saxophone fingerings at various levels of expert input. We then compute and visualise the cost of the optimal path through the part, at a given tempo. While we present this model for the tenor saxophone, the same pipeline can be applied to other woodwinds, and our experiments show that with appropriate feature design, only a small proportion of possible trills is needed to estimate the costs well. Thus, we present a practical way of diversifying the capabilities of MIR in music education to the wind family of instruments. 

### 1. INTRODUCTION AND SYSTEM OVERVIEW 

One essential element of studying music is choosing appropriate repertoire. Out of the factors that make a piece appropriate for a learner, its difficulty is among the most important: too much of a challenge, or not enough of one, can seriously damage the learning process [1, 2]. A major factor governing the difficulty of executing an instrumental part is also its target tempo, which must be determined. In addition to estimating the difficulty of entire pieces, an overview of which parts of a piece are difficult (and hence will likely require the most practice) might be useful for any learner. While teachers are of course proficient in assigning appropriate repertoire, tempo, and practice plans, not every learner has access to a qualified teacher. Hence, there is cause to try and model the difficulty of a piece and its parts automatically. 

> © Š. Libˇrický, and J. Hajiˇc jr.. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: Š. Libˇrický, and J. Hajiˇc jr., “Modeling the Difficulty of Saxophone Music”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

Just as there are under-served students, there are underserved instruments. The topic of difficulty estimation, together with fingering estimation, has been explored on the piano [3, 4] and to some extent also on string instruments [5,6]; not, however, for wind instruments. 

In this paper, we propose a model of difficulty for the tenor saxophone. We take the “optimum path” paradigm [6], where control of musical instruments is fundamentally structured into “play states” or “play actions” meant to sound the desired tone at the desired time. Playing a part can then be modelled as traversing a path through the corresponding play states in time, and difficulty of a part is the cost of this traversal. 

In order for this model to generalise to unseen parts, we can factorize the cost of a path to the aggregated costs of sub-sequences for which we have cost estimates, similarly to how n-gram language models truncate history. These sub-sequences can be as short as individual notes (unigrams); however, playing one note with no context is nearly meaningless. Together with [6] we settle on transitions between two fingerings as the units for which cost is defined.<sup>1</sup> We retain at least some meaningful musical context, while keeping the state space manageable (approx. 750 possible fingering pairs on the tenor saxophone). Traversal through a woodwind part is then the traversal through a finite-state automaton with tones as nodes and transition costs on the edges, which is easily tractable. 

Two things thus must be done: defining the play states for the saxophone, and estimating transition costs. For the saxophone, a play state that produces a desired tone is a combination of fingering, breath, muscle voicing, and articulation. Breath, however, is hard to observe and formalise, and in any case is not entirely independent from fingering, though some characterisation of breath parameters from woodwind audio has been done [7, 8]. Articulation and muscle voicing for saxophones have been studied [9, 10], but not to a level that they can be easily modelled computationally. Hence, we focus on encoding play states via fingering. 

The final missing piece of the puzzle is then to estimate the costs of transitions. This is, however, non-trivial for the saxophone. For instance, the major second from (written) C to D on a tenor saxophone varies wildly in breath support, voicing requirements, and motor movements in the three octaves where this interval appears. Thus, in or- 

> 1 There is only a small number of scenarios on a saxophone where a performer would alter fingerings based on anything other than the preceding and following fingerings. 

747 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

der to estimate the transition costs, a combination of expert knowledge and real-world data is necessary. Direct datadriven difficulty estimation [11] trains a model on extrinsic annotations of difficulty, instead of intrinsic properties of the notes that make up the performance, requiring more data with difficulty ratings. Instead, we proposed for creating fingering and difficulty prediction models that rely on data that are easier to acquire, using trill speed as a proxy for fingering transition difficulty, taking inspiration from [12], who evaluated theoretical fingering designs for digital instruments. 

Besides designing and implementing the application of the optimum path difficulty model for the saxophone using trill speeds, which is general enough to apply to any wind instrument without having to adjust important assumptions (such as single-voice parts<sup>2</sup> ), we also contribute a dataset of tenor saxophone trills and extracted trill speeds for all its playable transitions, we show that expert knowledge in representation design for the inherently limited data leads to more accurate transition cost estimation as well as for minimising the data acquisition costs for more instrument models, and we provide the implementation of the difficulty model itself as well as the pipeline for data collection and trill speed extraction.<sup>3</sup> 

### 2. RELATED WORK 

Existing music difficulty estimation methods rely on using musician-made annotations for optimal fingerings [3], or setting (or learning) of weights based on expert observations [6]. For woodwinds and brass instruments, however, where large leaps can be accomplished with minimal motor movement in the fingers and arms, the rules-based approach of [6] make creating expert rules that determine optimal fingerings difficult. 

Data-driven difficulty estimation methods for the piano are available, based on symbolic representations [13–15], sheet music images [16], or recently audio [17]; rearrangement by difficulty has also been done [18]. For the violin, optimal fingering estimations exist: the original optimal path approach [6], though focus has been more on player skill level rather than part difficulty, both for fingering estimation [19] and in context of visual perception of violinists [20]. In [21], symbolic score difficulty was estimated for violin, piano, and guitar. 

For the woodwind instrument family, however, focus has been more on their acoustical properties [7, 22]. Saxophone acoustics have been modeled [23] and reed parameters have been estimated from audio [8]. The kinetics of fingerings and note transitions were studied for the flute [24]. In [25], recorder audio is classified by typical mistake, but not difficulty. Sight-reading skills have been described for the clarinet (and violin) already in 1953 [26], and for the flute they have been empirically characterised [27], together with the difference in breath control between beginners and experts [28]. 

> 2 Multiphonics would rarely apply to likely users of such a system. 3 See Section 12 for link to implementation. 

## Session 0 

Trill #1 - cluster 0 B With octave key be be Bb With octave key (Bis key) 

Figure 1. An example of a prompt presented to performers. In this case, the performer is meant to trill between Bb4 and B4 (written pitch). 



<!-- Start of picture text -->
Visualisation of trill speed variance of repeated transitions<br>Player 1<br>Player 2<br>Player 3<br>6 Player 5Player 4<br>5<br>C<br>Tri l  sp e d in tri l s/s<br>2<br>Trans. 1 Trans. 2 Trans. 3 Trans. 4 Trans. 5 Trans. 6<br>Individual repeated transitions<br><!-- End of picture text -->

Figure 2. Visualisation of the per-player/session differences in trill speed for transitions that were recorded in every session (“anchor” transitions). 

### 3. DATA COLLECTION 

The process of collecting data consists of recording tenor saxophone (henceforth just saxophone) players trilling. The musicians are instructed to trill (1) as fast as possible, (2) as cleanly as possible,<sup>4</sup> and (3) as legato as possible.<sup>5</sup> 

The data was recorded in sessions of approx. 65 trills, taking an hour to record (including a short break). For each session, a set of music notation prompts – see Figure 1 – was typeset for the players to play from, communicating which notes were to be trilled between and which fingerings were to be used for each, along with emphasising the idea of speed. 

To avoid player fatigue in a recording session, a very simplified prior estimate of difficulty was done using only the size of the jump and primitive information about how many fingers move, to mix likely easy and difficult trills. 

Each session was subsequently manually split into recordings of individual trills. From the fingerings chosen, there are 741 possible fingering pairs.<sup>6</sup> In total, 817 trills were recorded, with 5 

> 4 Additional clarification was given to performers to play in such a way to minimise over/underblowing that would result in hearing notes in the harmonic series of the fundamental note being played. 

> 5 On a saxophone, this would mean that the tongue is not used to separate the two notes. For larger jumps such as an octave, or when needing to play a low note that is easier to produce when tongued, this instruction was de-emphasised. 

> 6 Some of these were recorded but not used in future sections, as they were trills between alternate fingerings of the same note. The trill extraction methodology in Section 4 cannot work with this for now. 

748 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
Cluster 1<br>Cluster 2<br>Trill 4 Trill 6<br><!-- End of picture text -->

Figure 3. Example of how clusters and trills are detected visualised on a CREPE [29] salience plot. Dashed yellow line loosely represents the cluster boundary. 

different, similarly advanced conservatory-level performers participating for a total of 13 sessions.<sup>7</sup> 

6 “anchor” transitions were recorded in every session to explore the nature of trill speed variations across performers and sessions. The speeds for these transitions is shown in Figure 2. Note that Player 5 is among the fastest in 3, and among the slowest in the other 3. 

### 4. TRILL SPEED EXTRACTION WORKFLOW 

After recording all necessary trills, an automatic trill speed extraction step is run to extract the highest trill speed from the raw audio for each fingering transition. 

We use CREPE [29] to predict f0 from the raw audio. To determine what notes participate in the trill, we perform k-means clustering on the f0 values with k = 2. The MIDI values are then derived from the median value of each cluster using `librosa` [30], at A=440 Hz. 

The trill speed for each segment was then determined by the number of complete trills completed within that segment (see Figure 3). A complete trill is defined as starting on note 1, transitioning to note 2, and returning to note 1. In practice, performers vary speed over each trill. To find the fastest stable trill speed, we take the first half, middle two quarters, and second half of each trill (each segment is about 1.5–3 seconds long – sufficient to count as a sustained trill), and take the highest average trill speed from these three segments. 

On more technically difficult transitions at speed, under and overblowing of the note happens. To correct for possible misclusterings, where such mistakes are detected as their own cluster,<sup>8</sup> if one cluster was less than 20% the size of the other, we discarded it and re-ran k-means with k = 2 again. 

To check for possible errors in trill speed extraction, the detected notes are matched against the expected interval from the recording session. If the notes detected by the trill speed extraction algorithm do not match the expected 

> 7 Alternate fingerings for F#, Bb with/without octave key, and Front F/F# were used. These were settled on following discussion with the participating saxophonists as to which alternate fingerings they used regularly. 

> 8 Especially on sub-fifth transitions, where an octave distance from the true notes might “tempt” k-means to put both target notes in one cluster. 



<!-- Start of picture text -->
Example: Eb with octave key<br>Left Hand Right Hand<br>1010110000000_1100110000<br>Let/Right hand plit<br>18<br><!-- End of picture text -->

Figure 4. A diagram explaining the encoding format as it relates to a fingering chart. 1 (octave key) – 13 are left hand keys, 14–23 are right hand keys. 

notes, we checked the trill recording manually to make sure the extracted trill speed does match the recorded trill. 

### 5. TRANSITION FEATURES 

To estimate costs for unrecorded transitions,<sup>9</sup> a representation of transitions is needed. Each transition is a pair of play states; we represent play states as fingerings. The saxophone has a finite number of keys (23, see Figure 4) that can be pressed, so we can straightforwardly represent a transition as two binary fingering vectors.<sup>10</sup> However, while this representation does in principle contain all information about a transition, more recorded data points may be needed to learn how the keys interact – which combinations are difficult and which are easy. Because we want to minimise the amount of recording necessary to reach a given cost estimation accuracy, we design two more representations: one that focuses on the player’s fingers rather than the instrument’s keys, and expert features that incorporate factors of difficulty from saxophone pedagogy. In total, three representations are used for transitions (shown in Figure 5): 

- “Raw” (abbr. R) features – raw encodings are simply concatenated. 

- “Finger” (abbr. F) features – each finger gets a 1 or 0 based on whether it has to move during the transition, along with a penalty if any finger has to move from one pressed key to a different pressed key (presence of a same-finger transition). 

- “Expert” features – further divided into “HandBased” (E-HB) and “Finger-Based” (E-FB). 

> 9 Which occur if we subsampled as per Section 7. 

> 10 For instruments where a large amount of adjustments can be made via the embouchure or other non-finger motor movements that are known for each pitch, these would also be incorporated. 

749 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

### 5.1 Finger features 

Each combination of covered keys has a sufficiently unique map to which fingers are active, so the “Finger” features can be derived automatically from the “Raw” features. 

The only complication is dealing with palm keys (played by the side of the hand or fingers). Two methods of mapping keys to fingers were used for the Finger feature set: a ’palm-as-a-finger’ (PAF) approach, where palm keys are treated as being played by a ’sixth finger’ on each hand representing the palm, and a ’palm-key-to-finger-mapping’ (P2FM) approach, where each palm key is mapped onto the finger that plays it using its side. For example, the High D key (key 13 in Figure 4) is played by the side of the index finger. 



Figure 5. Encoding a transition (E with octave key to high D) with Raw, Expert feature sets are in the version that includes MIDI and with expert weights enabled. 

### 5.2 Expert features 

The “Expert” features, selected in consultation with the recording saxophonists, contain: 

- MIDI values of both fingerings (written pitch). 

- Number of fingers that have to move from a pressed key to a different pressed position (so called samefinger transitions). These are big indicators of difficulty, as they are impossible to play legato and are generally cumbersome.<sup>11</sup> 

- Presence of any palm key transition on the left and right hand respectively. 

- Whether or not the octave key has to change state. 

- Presence of a fingering that is below a low C#. These notes require additional embouchure and air support. 

To this shared base, the Hand-Based Expert feature set (E-HB) adds the number of fingers that have to change on the left and right hand respectively. A transition requiring the left pointer, middle and ring finger to change states would receive a value of 3 for this feature (for the left hand). The Finger-Based Expert features (E-FB) instead add a feature for every finger, with value 1 if it has to move and 0 otherwise.<sup>12</sup> We experimented also with omitting the MIDI values when training a model (labelled “NoM”). In addition, Expert Weights (EW) were chosen to help indicate how severely a given feature is likely to impact the trill speed for a given transition. These weights were manually adjusted until k-means clustering with k = n/5<sup>13</sup> resulted in clusters of approximately the same difficulty as judged by the expert. We experimented with disabling these as well (labelled “NoEW”). 

### 6. TRANSITION DIFFICULTY ESTIMATION 

To estimate the difficulty of transitions (intervals) that are not recorded, we train regression models. This step can significantly lower the cost of parameterising the entire difficulty model, because it can decrease the number of recording sessions needed. There are thus two goals: 

> 11 The Bis key is ignored for this, as it is a special case of an intended same finger transition. 

(1) to obtain a model that is as accurate in predicting transition trill speeds as possible, with (2) as few of the recorded transitions as possible used as training data. 

Experiments were conducted to compare the proposed feature sets and two model classes: a linear regression model (LM), and a multi-layer perceptron (MLP), both using `sklearn` [31]. The MLP had a hidden layer size of 50, and used the `lbfgs` solver. Both of these models additionally clamped any prediction below 0.5 trills/s to 0.5.<sup>14</sup> 

A stratified k-fold with shuffle was used to divide the data into folds of 150 test trills, with stratification classes dictated by binning transitions by their trill speed (bins 0– 1.5, 1.5–3, 3–4.5, 4.5+). 

We report mean squared error (MSE), and also weighted mean squared error (wMSE) weighted by the relative frequency of intervals in the Weimar Jazz Database (WJD) [32], to measure how the model performs with respect to what one in fact encounters in repertoire rather than with respect to what the instrument can play (although we are more interested in the latter). 

Besides mean squared error, we also evaluate using mean absolute percentage error (MAPE). For the use case of difficulty estimation, a predicted and actual trill speed of 1 and 2 is a much larger issue than a similar absolute difference of 5 and 6. Additionally, the easier a transition is (and thus possessing a higher recorded trill speed), the more variance there may be between performers and even between recordings of similar transitions by the same performer, as, at the higher ends of the speed scale, fatigue and other factors play a much larger role; such a phenomenon can be seen in Figure 2. 

Results of trill speed estimation experiments are in Table 1. As evidenced by the mean squared error (MSE) values found during the experiment, the LM stops improving at ±0.97 MSE and 0.39 MAPE. The MLP performed much better, getting down to ±0.4 MSE and just under 0.2 MAPE using the Expert feature sets. The Finger-based feature set performed better than the Raw feature set in MSE but not in MAPE, suggesting that the improvement in MSE comes in faster trills – which is congruent with these fea- 

> 12 This part is almost identical to the finger-based features. 

> 13 Chosen as an amount of transitions comparable intuitively. 

14 0.5 is still lower than any actual recorded trill speed. 

750 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

|Feature set|LM(MSE)|LM(wMSE)|LM(MAPE)|MLP(MSE)|MLP(wMSE)|MLP(MAPE)|
|---|---|---|---|---|---|---|
|R|1.06|1.95|0.39|0.65|1.41|0.25|
|F(PAF)|0.97|2.02|0.39|0.52|0.96|0.25|
|F(P2FM)|0.98|2.10|0.39|0.53|1.06|0.25|
|E-HB|0.94|1.93|0.39|0.42|0.56|0.22|
|E-HB(NoM)|0.94|1.91|0.39|0.34|0.53|0.20|
|E-HB(NoEW)|0.94|1.94|0.39|0.36|0.79|0.18|
|E-HB(NoM&EW)|0.94|1.91|0.39|0.35|0.67|0.19|
|E-FB|0.94|1.92|0.38|0.63|1.16|0.26|
|E-FB(NoM)|0.94|1.90|0.39|0.47|0.90|0.22|
|E-FB(NoEW)|0.94|1.93|0.38|0.45|1.23|0.19|
|E-FB(NoM&EW)|0.94|1.90|0.39|0.33|0.75|0.18|



Table 1. Table showing the average MSE, average WJD-weighted MSE (wMSE), and average MAPE over all folds for a given model and feature extraction method (Best per column in bold; runner-ups in bold italics). Note that MAPE of e.g. 0.2 corresponds to the estimate being 20% off on average. 



<!-- Start of picture text -->
True vs Predicted trill speed for MLP with E-HB (No EW) feature set<br>True (recorded) trill speed<br>Predicted trill speed<br>7<br>Tri l  sp e ds in tri l s/s<br>25 50 75 100 125 150 175<br>Individual transitions from fold 0 test data sorted by true trill speed<br><!-- End of picture text -->

Figure 6. Differences between true and predicted trill speeds for the MLP model using the E-HB(NoEW) feature set. Transitions are sorted in ascending order by their true trill speed. 

tures more closely related to motor limitations. 

Errors in wMSE are larger than equally weighted MSE; easier (faster) transitions are more common, so the more heavily weighed errors are on transitions with more noise. 

The main takeaway, however, is that expert-designed features clearly perform best, probably as a function of the small maximum available dataset size. At the same time, however, the relationships between individual features are non-trivial in any representation, as the MLP clearly performs better than the linear model. We estimate a MAPE lower bound from the “anchor” transitions (Figure 2), with the median speed of each transition as its the ‘true’ value. The average anchor MAPE was 0.10 (max. 0.14, min. 0.06). The best model is thus only 8% worse than the attainable maximum. 

### 7. SAMPLING METHODS 

Not all recorded transitions are equally informative, so a good sampling strategy might reduce the number of 

recordings necessary to achieve a target prediction error. 

For the following tests, the Expert Hand-Based (No Expert Weights) features were used.<sup>15</sup> For each sampling method, the stratified k-fold cross-validation from Figure 6, was used. For every fold, the training set was then downsampled to the target n using the given sampling method. On this downsampled training set the MLP from Figure 6 was trained, and evaluated on the test set. For each n, 3 independent, differently seeded samples were tested, with the graphed value being the mean of the MAPEs of each sampling attempt. We compared three sampling methods: 

Uniform sampling of recorded transitions. 

Cluster-based. For every data point, its Hand-based Expert features (with Expert weights<sup>16</sup> and MIDI enabled) were extracted. Then, a k-means clustering was run, with k = n, so that we would get one cluster per sample point we want to get, and from each cluster a random data point was uniformly selected into the training sample. 

Empirical. We extracted note bigram probabilities from the Weimar Jazz Database [32] (WJD), with Laplace smoothing at α = 0.1, and sampled the transitions according to these probabilities. For notes with multiple fingerings, possible transitions were sampled uniformly. We expect this sampling to perform worse – but it roughly speaks to the data efficiency of just recording players play repertoire and extracting transition costs from that. 

As seen in Figure 7, cluster-based sampling performs best, with uniform sampling coming in a close second. Cluster-based sampling is slightly better at lower n’s, as it likely creates a more informative set of training data. However, the differences are in practice minimal. Empirical sampling performs much worse; frequently occurring transitions are not more informative. 

While the uniform and cluster sampling never diverge too much, the shallow slope somewhat means that around the region of MAPE 0.25, the difference between these two 

> 15 Chosen as it is in the slightly better performant expert feature set in the form that achieved the best MAPE. 

> 16 The expert weights were specifically designed in theory for this clustering, not for the model. 

751 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



Figure 7. Graph showing MAPE as training sample size increases across sampling methods. The coloured lines are the mean MAPEs over all folds at a given sample size. 0.25 mean MAPE is shown as a possible target MAPE choice at which to compare sampling strategies. 

sampling methods is about one recording session worth of recordings – 2 for clusters vs. 3 for uniform. Again, expert features show their usefulness. 

### 8. APPLICATION EXAMPLE 

Estimating the difficulty of a saxophone part is finally done by finding the optimal path through a finite-state automaton between our first and last set of states. The edge weights are the maximum attainable trill speeds estimated by the MLP model with E-HB(NoEW) features. We do not use the measured trill speeds directly because we want our system to also be usable for other instruments for which the estimation methodology described above allowed proceeding without recording all the transitions. 

Given that note values are known from the part, we can account for a given target tempo. The “fastest” (maximal) path through the part in terms of fingerings is found with Viterbi decoding over the estimated trill speeds (yielding optimal fingerings). Then, for every fingering bigram in the part, the transition difficulty is the proportion of the required “half trill” speed at the target tempo to the estimated maximum trill speed for that bigram. 

The outcome of one such model pass is visualised in Figure 8.<sup>17</sup> The brightness of each notehead is given by the average of its incoming and outgoing transition difficulties. This excerpt shows the non-trivial difficulty structure of the saxophone. The low notes are harder than midrange especially due to complex pinky finger movement at the end of the phrase. At the same time it is sensitive to a major factor of technical difficulty – speed, with the triplets standing out. We created a Musescore 3.6 plugin implementing this visualisation (see Section 12). 

> 17 Two full `*.mxl` examples are available in the Github repository (see Section 12). 



Figure 8. Example difficulty visualisation tool output. The redder a note is, the more difficult the segment around is deemed to be. Tempo for this visualisation was set to 160 BPM, which is not particularly fast for jazz [33]. 

### 9. DISCUSSION & CONCLUSION 

We have proposed a method for estimating the difficulty of woodwind parts based on the “optimal path” paradigm [6] and implemented it for the tenor saxophone, providing data, methods for transition weight estimation, and showing how expert knowledge can help minimise the cost of creating such models for other instruments. It is an example of participatory, practice-based research. 

However, there are also significant limitations. Most importantly, we would prefer to empirically evaluate the overall estimation, but we lack digitally encoded saxophone parts with authoritative ground truth difficulty. The ideal source would be piece grading from a musical examination board such as the ABRSM (Associated Board of the Royal Schools of Music), but digital encodings of the ABRSM-graded pieces are not available and copyright issues would prevent sharing an evaluation corpus, so difficulty evaluation data must be gathered.<sup>18</sup> 

Trill speed does not directly capture the intricacies of voicing, articulation, and breath support, which are all major contributors to woodwind difficulty. To maintain discrete play states, knowledge of these mechanics could be encoded in additional expert features. Also, trill speeds can be asymmetrical. On the saxophone, going up an octave quickly is much easier than down an octave; this is not modeled. 

This methodology still requires initial access to a technically proficient instrumentalist (and domain expert) to do the recordings and design the expert features and instrument encodings. Especially when using cluster-based sampling, many of the recorded transitions may be large, technical leaps that may be difficult for beginners to play. As can be seen in Figure 2, even for the same transition, the variance of the recorded trill speed can be high. Some normalisation procedure is needed. However, as seen in Figure 2, a performer may be the fastest for one transition, but slowest in another, so a single coefficient per player is unlikely to be effective. However, the opportunity here is to at the same time arrive at a normalisation function that can easily personalise the transition costs to a specific player based solely on recording a few anchor transitions. Despite these limitations, we believe this work can serve at least as a first step towards including the woodwind family more into MIR for music pedagogy, and we look forward to how others might take inspiration and devote some more attention to these instruments. 

> 18 This also speaks to the under-representation of woodwinds in MIR; although an audio-to-score system for the saxophone has been tried [34]. 

752 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

### 10. ACKNOWLEDGMENT STATEMENT 

This work is supported by project “Human-centred AI for a Sustainable and Adaptive Society” (reg. no.: CZ.02.01.01/00/23_025/0008691), co-funded by the European Union. Computing infrastructure was provided by the LINDAT/CLARIAH-CZ Research Infrastructure (https://lindat.cz), supported by the Ministry of Education, Youth and Sports of the Czech Republic (Project No. LM2023062). 

### 11. ETHICS STATEMENT 

All players signed an informed consent form. All data is pseudonymised. Video recordings of sessions, taken as a backup source for checking against unexpected errors in extraction, were deleted as soon as the trill and trill speed extraction steps were finished and checked. No generative AI tools were used in producing this text; code generation was used for hints in visualisations that are used as figures. 

### 12. DATA AND CODE ACCESSIBILITY 

The raw audio data in the form of recorded trills is here: `http://hdl.handle.net/11234/1-5942` . This also includes the output of the trill speed extraction pipeline, as rerunning the pipeline for all the data is time-consuming. All code and other implementation details can be found at `www.github.com/ Vobludalib/SaxophoneDifficultyModel/ tree/ISMIR2025` . The Musescore 3.6 plugin implementing this model can be found at `www.github.com/ Vobludalib/SaxophoneDifficultyModel/ tree/main/plugin` . 

### 13. REFERENCES 

- [1] M. A. Guadagnoli and T. D. Lee, “Challenge point: a framework for conceptualizing the effects of various practice conditions in motor learning,” Journal of motor behavior, vol. 36, no. 2, pp. 212–224, 2004. 

- [2] J. Bugos and W. Lee, “Perceptions of challenge: the role of catastrophe theory in piano learning,” Music Education Research, vol. 17, no. 3, p. 312–326, May 2014. [Online]. Available: http: //dx.doi.org/10.1080/14613808.2014.899334 

- [3] E. Nakamura, Y. Saito, and K. Yoshii, “Statistical learning and estimation of piano fingering,” Information Sciences, vol. 517, pp. 68–85, 2020. [Online]. Available: https://www.sciencedirect.com/ science/article/pii/S0020025519311879 

- [4] N. Srivatsan and T. Berg-Kirkpatrick, “Checklist models for improved output fluency in piano fingering prediction,” in Proceedings of the 23rd International Society for Music Information Retrieval Conference, ISMIR 2022, Bengaluru, India, December 4-8, 2022, P. Rao, H. A. Murthy, A. Srinivasamurthy, R. M. Bittner, R. C. Repetto, M. Goto, X. Serra, and 

M. Miron, Eds., 2022, pp. 525–531. [Online]. Available: https://archives.ismir.net/ismir2022/paper/ 000063.pdf 

- [5] D. Radicioni, L. Anselma, and V. Lombardo, “A segmentation-based prototype to compute string instruments fingering,” in Proceedings of the Conference on Interdisciplinary Musicology, vol. 17, 05 2004, pp. 15– 18. 

- [6] S. I. Sayegh, “Fingering for string instruments with the optimum path paradigm,” Computer Music Journal, vol. 13, no. 3, pp. 76–84, 1989. [Online]. Available: http://www.jstor.org/stable/3680014 

- [7] J. Kuroda and G. Koutaki, “Sensing control parameters of flute from microphone sound based on machine learning from robotic performer,” Sensors, vol. 22, no. 5, p. 2074, 2022. 

- [8] A. Muñoz Arancón, B. Gazengel, J.-P. Dalmont, and E. Conan, “Estimation of saxophone reed parameters during playing,” The Journal of the Acoustical Society of America, vol. 139, no. 5, pp. 2754–2765, 2016. 

- [9] M. Weikert and J. Schlömicher-Thier, “Laryngeal movements in saxophone playing: Video-endoscopic investigations with saxophone players: A pilot study,” Journal of Voice, vol. 13, no. 2, pp. 265–273, Jun 1999. [Online]. Available: https: //doi.org/10.1016/S0892-1997(99)80031-9 

- [10] G. P. Scavone, A. Lefebvre, and A. R. da Silva, “Measurement of vocal-tract influence during saxophone performance,” The Journal of the Acoustical Society of America, vol. 123, no. 4, pp. 2391–2400, 2008. 

- [11] P. Ramoneda, N. C. Tamer, V. Eremenko, X. Serra, and M. Miron, “Score difficulty analysis for piano performance education based on fingering,” in ICASSP 2022 - 2022 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2022, pp. 201–205. 

- [12] T. West, “Pitch Fingering Systems and the Search for Perfection,” in 22nd International Conference on New Interfaces for Musical Expression, NIME 2022, online, June 28 - July 1, 2022. nime.org, jun 16 2022. 

- [13] V. Sébastien, H. Ralambondrainy, O. Sébastien, and N. Conruyt, “Score analyzer: Automatically determining scores difficulty level for instrumental e-learning,” in 13th International Society for Music Information Retrieval Conference (ISMIR 2012), 2012, pp. 571–576. 

- [14] S.-C. Chiu and M.-S. Chen, “A study on difficulty level recognition of piano sheet music,” in 2012 IEEE International Symposium on Multimedia, 2012, pp. 17–23. 

- [15] Y. Ghatas, M. Fayek, and M. Hadhoud, “A hybrid deep learning approach for musical difficulty estimation of piano symbolic music,” Alexandria Engineering Journal, vol. 61, no. 12, pp. 10 183–10 196, 2022. 

753 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [16] P. Ramoneda, J. J. Valero-Mas, D. Jeong, and X. Serra, “Predicting performance difficulty from piano sheet music images,” in Proceedings of the 24th International Society for Music Information Retrieval Conference, ISMIR 2023, Milan, Italy, November 5-9, 2023, 2023, pp. 708–715. 

- [17] P. Ramoneda, M. Lee, D. Jeong, J. J. Valero-Mas, and X. Serra, “Can audio reveal music performance difficulty? insights from the piano syllabus dataset,” IEEE Transactions on Audio, Speech and Language Processing, pp. 1129–1141, 2025. 

- [18] M. Suzuki, “Piano score rearrangement into multiple difficulty levels via notation-to-notation approach,” EURASIP Journal on Audio, Speech, and Music Processing, vol. 2023, no. 1, p. 52, 2023. 

- [19] W. Nagata, S. Sako, and T. Kitamura, “Violin fingering estimation according to skill level based on hidden markov model,” in Music Technology meets Philosophy - From Digital Echos to Virtual Ethos: Joint Proceedings of the 40th International Computer Music Conference, ICMC 2014, and the 11th Sound and Music Computing Conference, SMC 2014, Athens, Greece, September 14-20, 2014. Michigan Publishing, 2014. [Online]. Available: https://hdl.handle.net/2027/spo.bbp2372.2014.189 

- [20] V. D’Amato, E. Volta, L. Oneto, G. Volpe, A. Camurri, and D. Anguita, “Understanding violin players’ skill level based on motion capture: a data-driven perspective,” Cognitive Computation, vol. 12, pp. 1356–1369, 2020. 

- [21] D. S. Deconto, E. L. F. Valenga, and C. N. Silla, “Automatic music score difficulty classification,” in 2023 30th International Conference on Systems, Signals and Image Processing (IWSSIP), 2023, pp. 1–5. 

- [22] J. Wolfe, J. Smith, J. Tann, and N. H. Fletcher, “Acoustic impedance spectra of classical and modern flutes,” Journal of sound and vibration, vol. 243, no. 1, pp. 127–144, 2001. 

- [23] T. Smyth and M. Rouhipour, “Saxophone modelling and system identification,” in Proceedings of Meetings on Acoustics. ASA, 2013. [Online]. Available: http://dx.doi.org/10.1121/1.4799622 

- [24] A. Almeida, R. Chow, J. Smith, and J. Wolfe, “The kinetics and acoustics of fingering and note transitions on the flute,” the Journal of the Acoustical Society of America, vol. 126, no. 3, pp. 1521–1529, 2009. 

- [25] Y. Han and K. Lee, “Hierarchical approach to detect common mistakes of beginner flute players.” in ISMIR, 2014, pp. 77–82. 

- [26] A. G. Thomson, An analysis of difficulties in sight reading music for violin and clarinet. University of Cincinnati, 1953. 

- [27] W. B. Thompson, “Music sight-reading skill in flute players,” The Journal of general psychology, vol. 114, no. 4, pp. 345–352, 1987. 

- [28] P. de la Cuadra, B. Fabre, N. Montgermont, and C. Chafe, “Analysis of flute control parameters: A comparison between a novice and an experienced flautist,” Acta Acustica united with Acustica, vol. 94, no. 5, pp. 740–749, 2008. 

- [29] J. W. Kim, J. Salamon, P. Li, and J. P. Bello, “Crepe: A convolutional representation for pitch estimation,” in 2018 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2018, pp. 161–165. 

- [30] B. McFee, M. McVicar, D. Faronbi, I. Roman, M. Gover, S. Balke, S. Seyfarth, A. Malek, C. Raffel, V. Lostanlen, B. van Niekirk, D. Lee, F. Cwitkowitz, F. Zalkow, O. Nieto, D. Ellis, J. Mason, K. Lee, B. Steers, E. Halvachs, C. Thomé, F. Robert-Stöter, R. Bittner, Z. Wei, A. Weiss, E. Battenberg, K. Choi, R. Yamamoto, C. Carr, A. Metsai, S. Sullivan, P. Friesch, A. Krishnakumar, S. Hidaka, S. Kowalik, F. Keller, D. Mazur, A. Chabot-Leclerc, C. Hawthorne, C. Ramaprasad, M. Keum, J. Gomez, W. Monroe, V. A. Morozov, K. Eliasi, nullmightybofo, P. Biberstein, N. D. Sergin, R. Hennequin, R. Naktinis, beantowel, T. Kim, J. P. Åsen, J. Lim, A. Malins, D. Hereñú, S. van der Struijk, L. Nickel, J. Wu, Z. Wang, T. Gates, M. Vollrath, A. Sarroff, Xiao-Ming, A. Porter, S. Kranzler, Voodoohop, M. D. Gangi, H. Jinoz, C. Guerrero, A. Mazhar, toddrme2178, Z. Baratz, A. Kostin, X. Zhuang, C. T. Lo, P. Campr, E. Semeniuc, M. Biswal, S. Moura, P. Brossier, H. Lee, and W. Pimenta, “librosa/librosa: 0.10.2.post1,” May 2024. [Online]. Available: https: //doi.org/10.5281/zenodo.11192913 

- [31] F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel, P. Prettenhofer, R. Weiss, V. Dubourg et al., “Scikit-learn: Machine learning in python,” Journal of machine learning research, vol. 12, no. Oct, pp. 2825–2830, 2011. 

- [32] M. Pfleiderer, K. Frieler, J. Abeßer, W.-G. Zaddach, and B. Burkhart, Eds., Inside the Jazzomat - New Perspectives for Jazz Research. Schott Campus, 2017. 

- [33] G. L. Collier and J. L. Collier, “An exploration of the use of tempo in jazz,” Music Perception, vol. 11, no. 3, p. 219–242, 1994. [Online]. Available: http://dx.doi.org/10.2307/40285621 

- [34] J. C. Martínez-Sevilla, M. Alfaro-Contreras, J. J. Valero-Mas, and J. Calvo-Zaragoza, “Insights into endto-end audio-to-score transcription with real recordings: A case study with saxophone works,” in INTERSPEECH 2023, ser. interspeech_2023. ISCA, Aug. 2023, p. 2793–2797. 

754 

