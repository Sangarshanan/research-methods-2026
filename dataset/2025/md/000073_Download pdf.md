---
paper_id: "000073"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706543/files/000073.pdf"
---

# PLAYABILITY PREDICTION IN DIGITAL GUITAR LEARNING USING INTERPRETABLE STUDENT AND SONG REPRESENTATIONS 

Manuel Müllerschön 

Anssi Klapuri Marcelo Rodríguez 

Christian Cardin 

Yousician Oy, Helsinki, Finland 

```
anssi.klapuri@yousician.com
```

## ABSTRACT 

Digital music learning applications have become a popular option for self-guided learning of musical instruments. Personalization of the learning curriculum in such applications hinges on two essential components: The learning unit (song arrangement) and the learner (student). While previous research has focused extensively on quantifying and characterizing the musical content, learner representation remains largely unexplored. In this paper, we introduce interpretable representations for these components, in the context of digital guitar learning. 

We propose a methodology to embed song arrangements and individual guitar students into a shared, interpretable skill vector space. To achieve that, we employ an automated profiling technique for guitar tablatures, generating granular vocabulary and difficulty descriptors. We validate the effectiveness of these representations by predicting the proportion of onsets played correctly by students, using a large-scale dataset from an online guitar learning platform. 

Our results demonstrate that models leveraging the combined representation of students and song arrangements outperform informed baselines and show better predictive accuracy when compared to models using either representation individually. These findings underscore the value of joint learner-song arrangement representations for digital music learning. 

## 1. INTRODUCTION 

In 1984, Benjamin Bloom published the landmark paper The 2 Sigma Problem - The Search for Methods of Group Instruction as Effective as One-to-One Tutoring [1]. In his research, Bloom validated quantitatively what many teachers subconsciously knew to be true: individualized learning supervision can drastically improve the learning experience. The effect was significant; students in his research 

> © M. Müllerschön, A. Klapuri, M. Rodríguez and Christian Cardin. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: M. Müllerschön, A. Klapuri, M. Rodríguez and Christian Cardin, “Playability Prediction in Digital Guitar Learning using Interpretable Student and Song Representations”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

cohort performed two standard deviations better than those taught in a conventional classroom setting. 

Forty years later, self-guided learning on digital learning platforms enjoys tremendous popularity [2]. While these education providers offer many advantages (flexibility, ubiquitousness, price), they still largely miss out on the educational boon of personalized learning. 

Remedying that and building meaningful personalization hinges on understanding: Who is the student, and what is their experience? And, what are the characteristics of the learning units on the platform? In the case of guitar students, that would entail the need to characterize both the learning units and the skill level of the students. Previous research has focused on the former [3–6]. Comparatively less work has gone into the latter, likely due to the unavailability of sizeable longitudinal datasets. Our work is motivated by this research gap. 

The context of this paper is Yousician, a digital guitar learning platform that provides several arrangements of each song at varying levels of difficulty. We propose a methodology to match song arrangements to the skill level of the student, aiming to improve learning outcomes [7,8]. Our approach consists of three main elements: 

1. We employ an automated profiling technique for song arrangements, annotating each note or chord with educationally relevant tags and numerical difficulty estimates. 

2. When the student plays a song arrangement on the platform, we assess the correctness of their playing at each point, in real time. This allows us to translate the tags and difficulty estimates into evidence of skill. The information is accumulated into a data structure that we call the student experience profile. 

3. We have a large record of students who attempted to play song arrangements on the learning platform. The data includes the student experience profile at the time of play. With it, we train a model that can predict the success rate of a certain student in playing a certain song arrangement for the first time. We call this task personalized playability prediction. 

Our interest lies in transparent, interpretable representations of student skill and arrangement difficulty. Having that enables students of the learning platform to understand 

631 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

what skill they are learning, and the aspects that make a song arrangement difficult. 

## 2. RELATED WORK 

In MIR there has been significant attention paid to the educational characterization and difficulty estimation of song arrangements for piano [3, 6, 9], and guitar [4, 5]. Velez Vazquez et al. introduce the concept of playability prediction for guitar, predicting expert-assigned difficulties for chord arrangements, though not personalizing it for the individual student [4]. With regards to the student, there is an established field of study for performance assessment, with analysis mostly tied to a single performance [10–12]. Research in educational psychology has studied the problem of knowledge tracing, which seeks to model a student’s state of understanding [13,14]. The work has historically centered around domains such as mathematics and language. Recent work has adapted knowledge tracing for music learning [15]. Beyond knowledge tracing, educational psychology provides us with relevant insights into designing self-guided learning environments [16]. In addition, we draw inspiration for designing digital learning platforms from music learning research, such as dynamics of instrument practice at home [7] and institutional music learning [8]. 

If we go beyond the domain of music education, there is a broad body of research on educational recommender systems – their design, application, and evaluation [17–20]. While many educational recommender systems address institutional learning settings with scarce data, some address the personalization of digital learning platforms. Smith et al. developed a co-creative AI for the music and code learning platform EarSketch, providing personalized feedback and recommendations for learners [21]. Notably, the language learning app Duolingo developed an educational recommender system that models both the student and the learning unit, which improved learning outcomes [22]. 

## 3. PROFILING TABLATURES WITH TIMED TAGS AND DIFFICULTY ESTIMATES 

In our digital learning platform, songs are arranged at different difficulty levels and oriented towards different styles (e.g., melodic playing, accompaniment). The arrangement’s notation can be assumed to specify, at least, the notes to be played, their musical timing, and the string, fret, and finger to articulate them. 

Figure 1 depicts our profiling system in action. The profiler proceeds by scanning the input tablature, note by note. Tag descriptors are categorical, aiming to provide a vocabulary of learning outcomes. Difficulty descriptors are vectors, aiming to quantify psychomotor difficulty. All descriptors are time-stamped, making a tablature profile a tabular, time-series hybrid. In the following, we elaborate, in turn, on each aspect. 

Tags: Each tag is defined in collaboration with our team of educators. Tagging automation needs to scale to both 



<!-- Start of picture text -->
16ths<br>FSharpDiatonicNotes<br>Tags ThickStrings<br>[Genre / ArtistSong Categorical Slides LowThumbPos<br>Arrangment DownPickingPickingPos<br>[Notation Unit<br>[Posture Discomfort]<br>Q=82<br>[Verse1] G#m A DifficultiesVector Relocation Speed<br>7<br>TAB<br><!-- End of picture text -->

Figure 1: Profiling example for 'Under The Bridge' by RHCP. 

new tag definitions, as well as tag definition changes. We sided with a rule-based system, as it provided a clean way to address definition changes. The resulting tag set matches the wording used to introduce music concepts and playing techniques in instructional videos, making for instances of both nominal data (e.g. 'cowboy chords' ) and ordinal data (e.g. 'small jump', 'big jump' ). The complete tag set has 650 unique tags. In this paper, we experiment with three tag subsets: (a) instrumental technique, with 37 tags (e.g. 'slide', 'thick strings', 'partial barre' ), (b) rhythm, with 20 tags (e.g. '16ths', 'off-beat', 'shuffles' ), and (c) chord shapes, with 256 tags (e.g. 'xx0232', which is an open D chord voicing, in standard tuning). The latter subset contains the most common open and movable guitar chord shapes in our catalogue. 

||Psychomotor difficultyestimates|
|---|---|
|Fretting|hand<br>Posture discomfort, fretting force,|
|(6)|hand relocation speed, finger real-<br>location speed, wrist repositioning<br>speed,finger repositioningspeed|
|Plucking|hand<br>Hand relocation speed, pick reposi-|
|(4)|tioning speed, string muting coordi-<br>nation,meter-pickingalignment|



Table 1: Numerical difficulty estimates used in this paper. 

Difficulties: We aim to automatically describe five factors that may complicate music performance: fretting discomfort (e.g., when pressing strings), hand posture discomfort (e.g., when holding a chord), movement inefficiency (e.g., when transitioning from one point on the fretboard to another), positioning inefficiency (e.g., when rearranging fingers so that they are placed on top of the strings that need to be pressed), and coordination inefficiency (e.g., when a picking pattern does not align with metric subdivisions). 

To that end, we implement models that, given an input tablature, can predict articulation symbols. We make one of such models to predict (fretting-hand) fingering, based on [23], and another to predict plucking direction (down or up), based on [24]. Both frame articulation prediction as a search problem, where good fingers/plucking choices are those that minimize cumulative biomechanical cost. To solve the search problem efficiently, dynamic pro- 

632 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

gramming is used. Our references are instances of proofof-principle work. In both cases, we curated validation databases, so as to extend their processing capacity (e.g., have [23] support polyphonic input), and finetune their biomechanical interpretability. Table 1 specifies the full vector. Describing the inner workings of each model is beyond the scope of this paper. Refer to [25] for details. 

## 4. REPRESENTING STUDENT SKILL AND ARRANGEMENT DIFFICULTY 

Personalization requires modelling the interrelationship between students and learning units. In Section 3, we showed how to represent the content of song arrangements, with note-level granularity. We also have access to evaluated performances, with matching granularity. This section describes how, from that data, we make a joint representational space for students and arrangements. 

## 4.1 Student Experience Profile (SXP) 

The student is represented in a data structure that we call the student experience profile (SXP). The core component of an SXP is an experience vector, in which evidence of skill is accumulated. We describe the experience vector in section 4.1.1, and describe how we extend its raw capacity in section 4.1.2. 

## 4.1.1 Student Experience Vector 

Any time a student chooses to play an arrangement, the application records the evaluation of each note/chord performed. Given that the platform offers different play modalities, such as practice and looping, we refer to plays as student-arrangement interactions, to preserve generality. Both evaluated performance and tags/difficulties are time-stamped, with high precision, so we can accurately align the two. 

For this paper, we test a 433-dimensional experience vector. Each element corresponds to either a tag or a difficulty. Tags account for 256 + 37 + 20 dimensions, corresponding to chords, instrumental technique, and rhythm. Difficulties account for 120 dimensions. Difficulties are continuous variables, which we quantise to an integer scale of ten steps. We reserve 100 dimensions to host them, and reserve 10 + 10 dimensions to host their cumulative totals. 

Experience Accumulation: When the student plays correctly, the vector values are incremented at the positions corresponding to the tags and difficulties (that temporarily align with the note/chord played). Henceforth, we refer to an evaluated note/chord instance as onset, so as to see success/mistake as an event in time, which may have to do with more than just the note/chord instance that was played at that point. For music units that in fact span one onset, for instance, a chord strum, we accumulate experience based on the evaluation of that single onset. For music units that span more than a single onset, such as rhythms, we use a sliding window of eight onsets, and accumulate 



<!-- Start of picture text -->
80000<br>60000<br>40000<br>20000<br>Raw repositioning speed difficulty over corpus<br><!-- End of picture text -->

Figure 2: Plucking hand, 'pick repositioning speed' difficulty distribution over the entire arrangement corpus. Computed quantile borders are depicted as vertical dotted lines. 

experience only if the share of correctly performed onsets exceeds 75%. This design choice was made to be conservative about experience accumulation. For difficulties, we follow a slightly different logic. For each onset position in the arrangement, we have access to the difficulty vector d, specified in Table 1. If an onset is played correctly and has a difficulty di > 0 for dimension i, then the experience vector dimension that corresponds to di is incremented. 

The above process allows us to project each performance of a student onto the experience vector space, where each dimension can be expressed in words that students can intuitively understand, and relate to a skill necessary for guitar playing. 

Difficulty Quantisation: Each difficulty dimension has different ranges and different distributions. We quantise their range to 1-10, using quantile normalisation. Quantile normalisation is done for each difficulty separately, using the entirety of our catalogue. Figure 2 shows an example. 



<!-- Start of picture text -->
Maximum Total Collected<br>Experience Experience<br>No Decay Half-life Half-life Half-life<br>1year 1 month 1 week<br><!-- End of picture text -->

Figure 3: Visualization of the student experience profile with different temporal decay factors. 

## 4.1.2 Views and Temporality of Experience 

Using the experience accumulation procedure described above, we derive a pair of experience vectors: the collected experience vc, and the maximum possible experience vm (had the student played the arrangement perfectly). Doing so opens the possibility to model not only first-order effects, such as experience gain, but also second-order ones, such as the consistency with which skill is demonstrated (via elementwise divison vc(s) ⊘ vm(s), for instance). 

Recency plays an important role in skill development [26], so we introduce a temporal dimension to the SXP, illustrated in Figure 3. Instead of just one pair of experience vectors that represent the entire learning journey of the student on the platform, we use four different vector 

633 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

pairs that represent different time intervals. When a student plays an arrangement on the platform, each of the four vector pairs is updated. We introduce decay rates to the experience components. ("forgetting factors.") Each day, the four cumulative experience components are multiplied by the decay rates 0.998, 0.9775, and 0.91, approximating half-life times of the experience of one year, one month, and one week, respectively. For our experiments, we also keep a no-decay component. 

The resulting SXP can be seen as 4 · 2 · 433 tensor. It makes for a thorough representation of cumulative experience, while retaining all the benefits of a fixed-size representation: It can be accessed, updated, and stored in an efficient and scalable way. 

## 4.2 Arrangement Characterisation (AC) 

In order to characterize arrangements, we project them onto the same 433-dimensional skill vector space that we use for the student experience representation. To do that, we take the vector that would result from a perfect and complete playthrough of the arrangement, accumulating skill in the same manner as done for the SXPs. That results in an interpretable pairing: SXP values represent experience gained, AC values represent experience needed. We normalize AC values by the number of onsets in the arrangement. That makes them scale-invariant, which has tested better (than length) in difficulty prediction [4,25]. 

## 5. PREDICTING STUDENT PERFORMANCE 

Systems in sections 3 and 4 are created to serve multiple personalisation tasks. In this paper, we test their efficacy on the task of recommending song arrangements. We know from music learning research that skill-difficulty mismatches have a negative impact on student learning outcomes, especially in self-guided learning environments [7, 8]. If we can meet students at their level, both enjoyment and learning outcomes can be assumed to improve. This experimental task can hence (a) help us validate the utility of the SXP and AC representations, and (b) move towards more meaningful personalization in the platform. 

## 5.1 Success Ratio as Prediction Target 

Quantifying the outcome of student-arrangement interactions is non-trivial. An established criticism in the space of educational recommender systems is that traditional accuracy metrics are overvalued, and little attention is paid to whether the target variable actually correlates with learning outcome [20]. 

With that in mind, we settled on using the success ratio of student-arrangement interaction. The success ratio is computed by dividing the number of successfully played onsets by the total number of played onsets. Our reasons for this choice are twofold. First, success ratios are used to model learning outcomes in knowledge tracing theory [27]. Second, we know that the success ratio correlates with student sentiments. Analyzing a large-scale set of studentarrangement interactions, including explicit student feed- 



<!-- Start of picture text -->
300000<br>250000<br>200000<br>150000<br>Frequency100000<br>50000<br>0 0.0 0.2 0.4 0.6 0.8 1.0<br>Student-arrangement interaction success ratio<br><!-- End of picture text -->

Figure 4: Distribution of the success ratio over the data set of student-arrangement interactions. 

back, we found that the success ratio strongly correlates with the sentiment of the student. The interactions that were rated relaxing or boring had a mean success ratio of 86%. Interactions that students rated inspiring or fun had an average of 80% while the interactions rated stressful or discouraging had a mean success ratio of 61% This suggests that if we are able to reliably predict the success ratio of a given interaction, we can suggest arrangements in the 70-80% range, which is more likely to motivate students. 

## 5.2 Personalized Playability Prediction Data Set 

We call the above-described task personalized playability prediction, adding the student representation to previous efforts [4]. We constructed a large-scale labeled dataset from historical data, containing the SXP, AC, observed success ratio, and relevant interaction metadata. Recognizing that the SXP continuously evolves over a student’s learning journey, the dataset creation required reconstructing SXP snapshots at the time of playing, in order to produce complete and accurate observations analogous to those available at inference time. Figure 4 shows the distribution of the success ratio in our dataset. 

To limit the amount of noise in the training set, we use three sampling constraints. First, we choose only to consider prima vista interactions, to isolate the data from practice effects. Second, we require that the included interactions exceed a certain minimum duration (20 onsets), to avoid introducing noise through students quitting the arrangement due to technical issues or disliking the song. Third, we maximize the diversity of ways in which students access arrangements (lessons, search, rankings), to avoid collinearities. 

The resulting data set spans 2,316,880 interactions from November 2022 to June 2024, including more than 200,000 guitar students. Due to the extensive nature of the SXP snapshots and ACs, the dataset exceeds 30 gigabytes. 

## 6. EXPERIMENTS AND RESULTS 

## 6.1 Ablation Using an XGB Regressor 

We made several explicit design decisions while conceiving the SXP and AC. Although informed by domain knowledge, we are aware that these might not result in optimal data structures for personalized playability prediction, specifically. So we first conducted an ablation study to understand the relevance of our input and parametrizations 

634 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

|Id|Ablation study|Input dim|RMSE|MAE|R<sup>2</sup>|
|---|---|---|---|---|---|
|1|Predict-the-mean baseline|–|0.2329±0.0007|0.1906±0.0006|0.0000±0.0000|
|2|Chord tags|1024|0.1880±0.0011|0.1431±0.0009|0.3486±0.0073|
|3|Instrument tech. and rhythmic tags|172|0.1532±0.0004|0.1109±0.0004|0.5677±0.0031|
|4|Difficulty histograms|480|0.1489±0.0009|0.1053±0.0007|0.5915±0.0048|
|5|Full vector|1732|0.1484±0.0008|0.1066±0.0006|0.5939±0.0045|
|6|Instr.+rhythmic tags & difficulties|708|0.1474±0.0007|0.1037±0.0005|0.5996±0.0045|
|7|Arrangement representation only|120|0.1983±0.0008|0.1535±0.0007|0.2752±0.0039|
|8|Student representation only|360|0.2091±0.0007|0.1640±0.0006|0.1940±0.0064|



Table 2: Ablation study on feature subset combinations, using XGB regression. 

|Id|Regressor|Dime|nsionality|RMSE|MAE|R<sup>2</sup>|
|---|---|---|---|---|---|---|
|||Input|Encoded||||
|1|EncoderNN [SXP]|6928|256|0.2175±0.0011|0.1722±0.0009|0.1308±0.0044|
|2|EncoderNN [SXP+AC]|6928|256 + 120|0.1643±0.0015|0.1211±0.0012|0.5040±0.0062|
|3|ShallowNN [SXP+AC]|480|–|0.1701±0.0020|0.1275±0.0058|0.4663±0.0133|
|4|TunedXGB[SXP+AC]|480|–|0.1474±0.0007|0.1037±0.0005|0.5996±0.0045|



Table 3: Regressor candidates for personalized playability prediction task 

for this task. We used a gradient-boosting (XGB) regression model. Its tree-based modeling approach tends to be less vulnerable to dataset imbalances and input normalization, both issues that we know exist in our dataset. Also, the XGB regressor is an established industry standard for solving real-world regression tasks. For comparison, we tested a multivariate linear regression model. It converged towards predicting the dataset mean, so we instead directly use predicting the mean as a baseline. 

Preliminary experiments revealed that omitting the intermediate decaying factors has no meaningful impact on XGB performance. Hence, for our ablation experiment, we input an SXP with (a) non-decaying experience (only vc), and (b) fastest-decaying experience (vc and vm), as well as the AC. The full input dimensionality is 4 · 433 = 1732. 

In our ablation study, we ran a cross-validation experiment on feature subsets. For each variant, we selected the corresponding slices of the experience vectors from both the SXP and AC. To account for the dimensionality change, we tuned the XGB regressor parameters before each experiment. Table 2 shows the results. 

We can see that using any slice of the skill vectors renders an improvement upon predicting the mean (2-4), and that the difficulty histograms seem to contribute the strongest to the model’s accuracy. Adding all of the vector slices together (5) does not improve the accuracy significantly. Instead, dropping the large set of chord tags (6) renders the best result – however, not significantly better than using only the histograms. Importantly, combining the information of the SXP and AC renders drastically better results than using either of the two on their own (model 4 vs. models 7–8). 

## 6.2 Autoencoder and Encoder-Based Regressors 

The ablation results led us to question the degree of redundancy in our representations. To assess that, we trained an autoencoder on the SXPs. We iterated on latent spaces 

of different sizes to understand how much compression we can apply to the student representation. The autoencoder was trained in a self-supervised manner. We trained on a separate set of unlabeled SXPs, so as to preserve the labeled dataset for training regression models that use the representations learned by the autoencoder. 

For these experiments, we augmented the four accumulative memory components introduced in Section 4.1.2 with four sequential memory components, which represent the experience of the student within their last four active days. The resulting experience profile is a tensor of size 8 · 2 · 433 = 6928. 

We ran training iterations on five different autoencoder architectures, each tasked with reconstructing the original 6928 dimensional SXP from a latent space representation of 1048, 524, 256, 128, and 64 dimensions. The accuracy of the decoder remained high for the first 3 models. Only when constraining the latent space to 128 dimensions we experience a significant drop in accuracy. 

Given that compressing SXP to 256 dimensions (5% of its original size) retains useful information, we set out to test whether the SXP embeddings can serve as the trunk for a neural network regressor. This could provide an alternative to feature selection, as we could rely entirely on compression to condense SXPs for playability prediction. 

We first built a predictor that uses only the SXP. We take the encoder component of the autoencoder and add a shallow neural network to the latent space layer. Then, we conduct end-to-end training on the labeled dataset. Results are shown in Table 3 (1). Next, we implemented an adaptation of this model where, in addition to the 256dimensional embedding, we plugged scale-normalized arrangement characterization into the model and trained it on the labeled dataset (2). Then, as a benchmark, we applied a shallow feed-forward neural network to the difficulty histogram features identified in the ablation study (3). Lastly, we indicate the performance of the XGB regression model 

635 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

on the same set of features. 

We can see that the embedding carries significant explanatory power. Combining the SXP embedding with the arrangement representation leads to an accuracy that lies clearly above the baseline, and beats out the featureengineered benchmark. We can also see that the XGB regression model outperforms all. 

## 6.3 Model Evaluation and Error Analysis 

Experiments in sections 6.1 and 6.2 show that the XGB regressor, variant 7 in Table 2, performs best. This model uses a combination of instrumental technique tags, rhythmic tags, and difficulty histograms. We prefer this model not only because of its predictive performance, but also because of its lightweight architecture, low computational cost, and relatively small input dimensionality. 

To further validate the model’s suitability and performance, we conducted a detailed error analysis. First, we examined the distribution of the model’s predictions. Results indicate that the predictions closely mirrored the actual distribution of the target variable, without undesirable convergence toward the mean. 



<!-- Start of picture text -->
0.16<br>0.14<br>0.12<br>0.10<br>MAE of prediction<br>0.08 0 8 10 11 12 13 14 15<br>Mastery level<br><!-- End of picture text -->

Figure 5: Mean absolute error of predictions for mastery level of the student. The mastery level contains the highest successfully played song level of the students. 

Next, we analyzed the distribution of prediction errors across student mastery levels. The mastery level contains the highest successfully played song level of the students, where human educators assign song levels that range between 0 and 15. Results are shown in Figure 5. The analysis revealed that errors were generally evenly distributed, and slightly elevated at skill level 0 (absolute beginners) and level 15 (expert players). This pattern is understandable since, for beginners (level 0), there is only a limited amount of student history available, making accurate predictions challenging. Similarly, level 15 represents highly skilled students tackling difficult arrangements. As the data set only contains prima vista interactions, predicting the outcome of such complex interactions is notoriously difficult. 

Additionally, we investigated prediction errors across student-arrangement interactions, stratified by the true success ratio. Results are shown in Figure 6. Errors are notably higher in the lower range (0.0–0.3), which aligns with expected gameplay dynamics: When a student cannot play a song, the interaction ends automatically, shifting the prediction task from assessing performance to estimating how long they play before failing. The prediction target hence becomes highly volatile, explaining the error increase. 



<!-- Start of picture text -->
1.0<br>0.8<br>0.6<br>0.4<br>0.2<br>Abs. prediction e r or<br>0.0<br>< 0.1 < 0.2 < 0.3 < 0.4< 0.5< 0.6 < 0.7 < 0.8 < 0.9 > 0.9<br>True success ratio of student-arrangement interaction<br><!-- End of picture text -->

Figure 6: Predictive performance of the XGBRegression model, stratified by true success ratios 

## 7. CONCLUSION 

In this paper, we explored personalisation in digital guitar learning. We introduced a fully automated methodology for representing both student experience and arrangement difficulty, and showed that combining these representations enables accurate prediction of prima vista performance. Our analysis highlighted the significant contribution of difficulty histograms to prediction accuracy. We also found that student representations could be compressed to just 5% of their original dimensionality with minimal accuracy loss, facilitating efficient inference. 

Future work will extend beyond this initial use case, exploring the potential of these representations across different personalization scenarios. All looking to enhance selfguided music learning. 

## 8. ACKNOWLEDGEMENTS 

We thank the anonymous reviewers for the many insightful comments and suggestions. 

## 9. REFERENCES 

- [1] B. S. Bloom, “The 2 sigma problem: The search for methods of group instruction as effective as one-to-one tutoring,” Educational Researcher, vol. 13, pp. 16 – 4, 1984. 

- [2] R. C. Rodriguez and V. Marone, “Guitar learning, pedagogy, and technology: A historical outline,” Social Sciences and Education Research Review, vol. 8, no. 2, Dec. 2021. 

- [3] P. Ramoneda, V. E. Eremenko, A. D’Hooge, E. ParadaCabaleiro, and X. Serra, “Towards explainable and interpretable musical difficulty estimation: A parameterefficient approach,” in ISMIR, 2024, pp. 520–528. 

- [4] M. A. V. Vásquez, M. Baelemans, J. Driedger, W. Zuidema, and J. A. Burgoyne, “Quantifying the ease of playing song chords on the guitar,” in ISMIR, 2023, pp. 725–732. 

- [5] S. Ariga, S. Fukayama, and M. Goto, “Song2guitar: A difficulty-aware arrangement system for generating 

636 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

guitar solo covers from polyphonic audio of popular music.” in ISMIR, 2017, pp. 568–574. 

- [6] V. Sébastien, H. Ralambondrainy, O. Sébastien, and N. Conruyt, “Score analyzer: Automatically determining scores difficulty level for instrumental e-learning,” in ISMIR, 2012, pp. 571–576. 

- [7] S. Fukuda, Y. Fukuda, M. Hosoda, A. Motomura, E. Sasao, M. Matsubara, and M. Niitsuma, “Field Study on Children’s Home Piano Practice: Developing a Comprehensive System for Enhanced StudentTeacher Engagement,” in ISMIR, 2024, pp. 381–388. 

- [8] A. Kavcic Pucihar, K. Habe, B. Rotar Pance, and M. Laure, “The key reasons for dropout in slovenian music schools – a qualitative study,” Frontiers in Psychology, vol. 15, 05 2024. 

- [9] P. Ramoneda, N. C. Tamer, V. Eremenko, X. Serra, and M. Miron, “Score difficulty analysis for piano performance education based on fingering,” International Conference on Acoustics, Speech and Signal Processing, pp. 201–205, 2022. 

- [10] Y. Ju, C. Y. Wu, B. C. Lorenzo, J. Yang, J. Deng, F. Fan, and S. Lui, “End-to-End Automatic Singing Skill Evaluation Using Cross-Attention and Data Augmentation for Solo Singing and Singing With Accompaniment,” in ISMIR, 2024. 

- [11] A. Lerch, C. Arthur, K. A. Pati, and S. Gururani, “Music Performance Analysis: A Survey,” ISMIR, 2019. 

- [12] Y. Jiang, “Expert and novice evaluations of piano performances: Criteria for computer-aided feedback,” in ISMIR, 2023, pp. 367–374. 

- [13] A. T. Corbett and J. R. Anderson, “Knowledge tracing: Modeling the acquisition of procedural knowledge,” User Modeling and User-Adapted Interaction, vol. 4, no. 4, pp. 253–278, 12 1994. 

- [14] C.-K. Yeung and H. Kong, “Deep-IRT: Make Deep Learning Based Knowledge Tracing Explainable Using Item Response Theory,” EDM 2019 - Proceedings of the 12th International Conference on Educational Data Mining, pp. 683–686, 4 2019. 

   - [18] M. Murtaza, Y. Ahmed, J. A. Shamsi, F. Sherwani, and M. Usman, “AI-Based Personalized E-Learning Systems: Issues, Challenges, and Solutions,” IEEE Access, vol. 10, pp. 81 323–81 342, 2022. 

   - [19] S. S. Khanal, P. W. Prasad, A. Alsadoon, and A. Maag, “A systematic review: machine learning based recommendation systems for e-learning,” Education and Information Technologies, vol. 25, no. 4, pp. 2635–2664, 7 2020. 

   - [20] M. Erdt, A. Fernández, and C. Rensing, “Evaluating Recommender Systems for Technology Enhanced Learning: A Quantitative Survey,” IEEE Transactions on Learning Technologies, vol. 8, no. 4, pp. 326–344, 10 2015. 

   - [21] J. Smith, E. Truesdell, J. Freeman, B. Magerko, K. Boyer, and T. Mcklin, “Modeling music and code knowledge to support a co- creative ai agent for education,” in ISMIR, 2020, pp. 134–141. 

   - [22] K. Bicknell, C. Brust, and B. Settles, “How Duolingo’s AI Learns what you Need to Learn: The languagelearning app tries to emulate a great human tutor,” IEEE spectrum, vol. 60, no. 3, pp. 28–33, 3 2023. 

   - [23] G. Hori and S. Sagayama, “Minimax viterbi algorithm for hmm-based guitar fingering decision.” in ISMIR, 2016, pp. 448–453. 

   - [24] E. T. de Lima and G. L. Ramalho, “On rhythmic pattern extraction in bossa nova music.” in ISMIR, 2008, pp. 641–646. 

   - [25] M. Rodríguez and A. Klapuri, “Educational profiling of guitar tablature: Tools to foster self-guided learning,” in Submitted to CMMR, 2025. 

   - [26] T. Savion-Lemieux and V. B. Penhune, “The effects of practice and delay on motor skill learning and retention,” Experimental Brain Research, vol. 161, pp. 423– 431, 2005. 

   - [27] S. Shen, Q. Liu, Z. Huang, Y. Zheng, M. Yin, M. Wang, and E. Chen, “A survey of knowledge tracing: Models, variants, and applications,” IEEE Transactions on Learning Technologies, 2024. 

- [15] Y. Zhang, Y. Zhang, W. Xu, Z. Wang, and J. Sun, “SingPAD: A Knowledge Tracing Dataset Based on Music Performance Assessment,” pp. 332–340, 2024. 

- [16] W. Varela, P. C. Abrami, and R. Upitis, “Selfregulation and music learning: A systematic review,” Psychology of Music, vol. 44, no. 1, pp. 55–74, 2016. 

- [17] F. L. da Silva, B. K. Slodkowski, K. K. A. da Silva, and S. C. Cazella, “A systematic literature review on educational recommender systems for teaching and learning: research trends, limitations and opportunities,” Education and Information Technologies, vol. 28, no. 3, pp. 3289–3328, 3 2023. 

637 

