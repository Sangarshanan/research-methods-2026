---
paper_id: "000117"
year: 2024
title: "Download pdf"
source_url: "https://zenodo.org/record/14877511/files/000117.pdf"
---

# LYRICALLY SPEAKING: EXPLORING THE LINK BETWEEN LYRICAL EMOTIONS, THEMES AND DEPRESSION RISK 

Pavani Chowdary<sup>1</sup> 

Bhavyajeet Singh<sup>1</sup> 

Rajat Agarwal<sup>1</sup> 

Vinoo Alluri<sup>1</sup> 

1 Music Cognition Group, International Institute of Information Technology, Hyderabad, India 

```
{boddu.pavani,bhavyajeet.singh,rajat.agarwal}@research.iiit.ac.in,vinoo.alluri@iiit.ac.in
```

## ABSTRACT 

Lyrics play a crucial role in affecting and reinforcing emotional states by providing meaning and emotional connotations that interact with the acoustic properties of the music. Specific lyrical themes and emotions may intensify existing negative states in listeners and may lead to undesirable outcomes, especially in listeners with mood disorders such as depression. Hence, it is important for such individuals to be mindful of their listening strategies. In this study, we examine online music consumption of individuals at risk of depression in light of lyrical themes and emotions. Lyrics obtained from the listening histories of 541 Last.fm users, divided into At-Risk and No-Risk based on their mental well-being scores, were analyzed using natural language processing techniques. Statistical analyses of the results revealed that individuals at risk for depression prefer songs with lyrics associated with low valence and low arousal. Additionally, lyrics associated with themes of denial, selfreference and blame were preferred. This study opens up the possibility of an approach to assessing depression risk from the digital footprint of individuals and potentially developing personalized recommendation systems. 

Keywords: depression, lyrics, lastfm, emotions, themes 

## 1. INTRODUCTION 

Depression is one of the leading causes of disability in young adults globally, according to the World Health Organization [1]. It has the potential to hinder and curb development in personal and social avenues of life, making it a debilitating condition. This underscores the imperative to identify and address it in the early stages. 

Music plays an important role in regulating mood and emotions [2]. Musical preferences and music listening habits are known to invoke and reinforce moods and emotions and satisfy psychological needs [3, 4]. Emotionally vulnerable young adults were found to have more intense 

> © P. Chowdary, B. Singh, R. Agarwal and V. Alluri. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: P. Chowdary, B. Singh, R. Agarwal and V. Alluri, “Lyrically Speaking: Exploring the Link Between Lyrical Emotions, Themes and Depression Risk”, in Proc. of the 25th Int. Society for Music Information Retrieval Conf., San Francisco, United States, 2024. 

relationships with music [5]. An increased emotional reliance on music was also observed in such individuals [6]. However, certain music engagement behaviors and strategies are associated with indicators of poor mental health and do not always lead to the alleviation of existing depressive symptoms [7]. Individuals who are depressed or at risk of depression are often unconscious of using music as a tool to improve emotional states [8], which might lead to adverse outcomes. This highlights the importance of addressing and studying music listening behaviors of individuals prone to depression risk for developing intervention methods to come up with listening strategies that may lead to positive outcomes. 

Online music streaming platforms such as Spotify<sup>1</sup> , Last.fm<sup>2</sup> , and Apple Music<sup>3</sup> offer their users a large variety of songs across genres and make it possible to study the musical digital footprints of their users. Last.fm allows the extraction of the listening histories of its users and the corresponding metadata, which prompted several studies that utilized Last.fm to study naturally occurring user listening behaviors in light of depression risk [9, 10, 11]. However, the relationship between lyrics, specifically the semantics and emotional connotations of lyrics, and depression has received little to no attention in the literature, while lyrics were found to play a crucial role in affecting emotional states [12]. Lyrics were also found to be essential for depicting sadness in music [13]. This study seeks to address this gap by examining the relationship between lyrical emotions and themes extracted from user listening histories and depression risk. 

## 2. BACKGROUND AND RELATED WORK 

We highlight previous studies that used online music listening histories from Last.fm and preferences to identify different trends and characteristics in music listening behaviors of individuals at risk of depression. Surana et al. [9] was the first such study, which used user-annotated tags from Last.fm, to identify emotion- and genre-tag preferences of individuals at risk of depression. The results of this study revealed that At-Risk individuals consume music that is tagged with emotions representing sadness, such as sad, depressed, dead, low and miserable, and belonging to 

> 1 www.spotify.com 

> 2 www.last.fm 

> 3 music.apple.com 

1046 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 



<!-- Start of picture text -->
User K10 scores<br>Mean QPS<br>Emotion-based<br>Mental Well-Being Emotion Quadrant Analysis<br>Survey Extraction<br>User<br>Lyrics<br>Categorizaton<br>Last.fm Users<br>Music Listening Theme-based<br>History Mean Frequency Scores Analysis<br>Theme Extraction<br>Data Collection Lyrics Processing Statistical Analysis<br><!-- End of picture text -->

Figure 1: Methodology 

genres such as neo-psychedelic, dream-pop and indiepop. In a later study, Surana et al. [10] studied emotions in relation to acoustic features of music as dynamic measures across the span of six months by dividing the listening history into sessions based on periods of inactivity to observe any dynamic patterns in music listening behaviors of AtRisk individuals. This study found that individuals at risk of depression rely more heavily on music and tend to listen to the same songs repeatedly. It was also found that they tend to listen to sad music for longer periods. 

Shriram et al. [11] were the first to study lyrics in this context in terms of lyrical repetitiveness and compressibility. The results revealed that At-Risk individuals prefer music with lower lyrical simplicity (lower compressibility) and greater information content, especially for music that is characterized as sad. 

However, no study to date has explored the link between lyrical emotions and themes extracted from online listening histories and depression risk, to the best of our knowledge. This link is crucial to investigate because lyrics reinforce negative states and, in dire situations, lead to maladaptive outcomes. The only study that has looked into lyrical themes associated with maladaptive listening strategies, which is known to be a proxy for depression risk [14], was done by Singh et al. [15]. They explored the link between lyrical themes extracted using DICTION<sup>4</sup> and unhealthy music engagement strategies characterized by the Unhealthy-Healthy music scale (HUMS) [14], which indirectly indicates depression risk. This study revealed that individuals who engage in unhealthy and maladaptive listening strategies listen to music with lyrical themes representing self-reference and blame. However, this has been done in the context of online discourse surrounding depression on Reddit. This raises the question of whether similar behavior can be observed in the lyrical content derived from the listening histories of individuals at risk on music 

streaming platforms. In this study, we investigated the relationship between individuals’ online listening histories and their risk of depression in the context of lyrical emotions and themes. 

Based on previous research in the field [9, 10, 11, 15], we hypothesize the following: 

- Building on prior research demonstrating a preference for sad music among At-Risk individuals [9,10], we hypothesize that these individuals exhibit a greater preference for music with lyrics associated with low valence and low arousal. 

- In line with the established link between lyrical themes and unhealthy music engagement behaviors shown by Singh et al. [15], we hypothesize that AtRisk individuals consume music that is higher in terms of themes such as self-reference, and blame. 

## 3. METHODOLOGY 

Figure 1 summarizes the procedure used in our study, which is described as follows. 

## 3.1 Dataset 

We used the dataset from Surana et al. [9,10] for our analysis. The dataset consists of the six-month music listening history of 541 Last.fm users (Mean Age = 25.4, SD = 7.3), of which 444 were male, 82 were female, and 15 identified as other. This data was acquired by means of a survey that was posted on Reddit<sup>5</sup> and Facebook<sup>6</sup> Last.fm pages. Informed consent was taken from the participants and participation was completely voluntary. They were informed that the study posed no risks and that their confidentiality would be maintained. The analysis was performed at a group level, ensuring no individuals could be identified. 

> 5 www.reddit.com 

> 6 www.facebook.com 

4 www.dictionsoftware.com 

1047 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

## 3.1.1 Measure of Depression Risk 

To assess mental well-being, Kessler’s Psychological Distress Scale (K10) questionnaire [16] is utilized, which measures psychological distress with a focus on symptoms of anxiety and depression. Following the approach of Surana et al. [9], participants scoring 29 or higher on the K10 questionnaire were classified as being in the “AtRisk” group for depression, while those scoring below 20 constitute the “No-Risk” group. Out of the total users, 193 individuals were in the No-Risk group, and 142 were in the At-Risk group. 

## 3.1.2 Listening History and Lyrics 

Lyrics for the tracks in the listening histories are extracted from Genius.com and MetroLyrics.com. Lyrics for approximately 76% of the entire repository of songs were obtained. Songs with no lyrics comprised around 4% of the dataset. 

## 3.2 Lyrics Processing 

## 3.2.1 Lyrics-Emotion Mapping 

based on song lyrics. The model is trained on the MoodyLyrics [20] and MER [21] datasets, which consist of songs uniformly distributed across the four quadrants of the Russell’s Valence-Arousal circumplex model. The model was used to return a single quadrant label for each song by mapping the song’s lyrical content to the 2D Valence-Arousal space, which was used to categorize the tracks into one of the four quadrants. 

To quantify user preferences for quadrant categories, we computed a quadrant prevalence (QPS) score for each quadrant, which is determined by the proportion of tracks from each user’s listening history, within the respective quadrants, as shown in Equation 1. The top 100 most frequently listened songs were identified and assigned weights based on listening frequency. The QPS for each user and quadrant was then calculated as the average weighted frequency of songs belonging to that specific quadrant in their listening history. 



<!-- Start of picture text -->
∑ si∈L ( uj ) w(si) · I(q(si) = qk)<br>QP S(uj, qk) = (1)<br>∑ si∈L(uj ) w(si)<br><!-- End of picture text -->

## where, 



<!-- Start of picture text -->
1<br>Arousal<br>2nd Quadrant (Q2) 1st Quadrant (Q1)<br>Anger Happiness<br>Valence<br>3rd Quadrant (Q3) 4th Quadrant (Q4)<br>Sadness Tenderness<br>0<br><!-- End of picture text -->

Figure 2: Two-dimensional Valence-Arousal space 

Lyrics were projected onto the Russell’s Complex Model of Affect [17], which is used to organize emotions along two orthogonal dimensions: Valence, which represents pleasantness and Arousal, which represents energy. As can be seen in Figure 2, The first quadrant represents high valence and high arousal (happiness), the second quadrant represents low valence and high arousal (anger), the third quadrant represents low valence and low arousal (sadness), and the fourth quadrant represents high valence and low arousal (tenderness). We employed a model proposed in Agarwal et al. [18] to map each song’s lyrical content to a quadrant in the VA space. The architecture of the model is a deep neural network architecture that employs XLNet [19], an advanced bidirectional transformer, to perform multitask learning for emotional classification 

QP S(uj, qk) : QPS of quadrant qk for user uj 

si : a song in the top 100 songs of the user’s listening history L(uj) 

w(si) : the weight (listening frequency) of song si. q(si) : quadrant assigned to song si 

I(.) : indicator function that equals 1 if the condition inside is true (song si belongs to quadrant qk) and 0 otherwise. 

## 3.2.2 Lyrics-Semantic Themes Mapping 

Following a similar approach to Singh et al. [15], we used DICTION to analyze the lyrics and identify underlying semantic themes. DICTION operates through the use of dictionaries that contain lists of words associated with specific linguistic, emotional and cognitive contexts. There are 5 themes and 35 sub-themes in total. We chose the themes Self-reference, Blame, Optimism, Hardship, Satisfaction, Inspiration, Exclusion and Denial. The frequency scores corresponding to all the themes and sub-themes for each song were obtained, based on the occurrence of the words from the lyrics in the dictionary lists. Similar to the quadrant prevalence scores, mean frequency scores (MFS) were computed for all the themes per user, as shown in Equation 2. 



<!-- Start of picture text -->
∑ si∈L ( uj ) w(si) · Tk(si)<br>M F S(uj, tk) = (2)<br>∑ si∈L(uj ) w(si)<br><!-- End of picture text -->

where, 

M F S(uj, tk) : MFS of theme tk for user uj 

si : a song in the top 100 songs of listening history L(uj) w(si) : the weight (listening frequency) of song si. Tk(si) : the frequency score assigned to song si for theme tk. 

1048 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

## 3.3 Statistical Testing 

We divided the users into At-Risk and No-Risk groups based on their K10 scores, as mentioned before. For each quadrant, we performed a two-tailed Mann-Whitney U (MWU) test on the quadrant prevalence score between the At-Risk and No-Risk groups. Similarly, a MWU test was performed for the mean frequency score between At-Risk and No-Risk groups, for each theme selected. 

## 4. STATISTICAL TESTING AND RESULTS 

## 4.1 Lyrical Emotion-Based Results 

A statistically significant difference (p < 0.05) was observed for the QPS corresponding to Q3, which is representative of low valence and low arousal values (U-statistic = 15727.5, p = 0.02), with a higher median for the At-Risk group, as can be seen in 3. We observed no significant differences between the distributions of the At-Risk and No-Risk groups for the other quadrants. The same trend was observed when the top 250 songs were considered. 



<!-- Start of picture text -->
80 p = 0.285 p = 0.020 p = 0.663GroupAL-RiskNo-Risk<br>p = 0.758<br>60<br>oz<br>Q1 Q2 Q3 Q4<br>Quadrant<br><!-- End of picture text -->

Figure 3: Violin plots of mean QPS per quadrant for AtRisk and No-Risk groups 

## 4.2 Lyrical Theme-based Results 

We found significant differences (p<0.05) between AtRisk and No-Risk groups in the case of denial, selfreference and blame. As can be inferred from Table 1, The median for the At-Risk group is higher in the cases of the themes denial, self-reference and blame. 

||Theme|U-statistic|p-value|
|---|---|---|---|
||Denial|15950.0|0.010|
|At-Risk >|Self-reference|15968.0|0.009|
|No-Risk|Blame|15691.5|0.023|



Table 1: MWU Test results for the Mean Frequency Scores between the At-Risk and No-Risk groups; Here At-Risk > No-Risk refers to the themes where the median is greater in the case of the At-Risk group 

## 5. DISCUSSION 

This study is the first of its kind to explore the association between risk for depression and the emotional and the- 

matic connotations of the lyrical content of the music individuals engage with online, as opposed to studies in lab settings or self-reported data. Our results are in concordance with our initial hypotheses, in addition to revealing novel findings. 

The At-Risk group exhibited a higher median score for Q3 (low valence, low arousal) than the No-Risk group. This finding suggests a greater prevalence of sadnessrelated lyrical content in the music listened to by the AtRisk group. The stronger association of the At-Risk group with sadness aligns with the results of past research studies on the topic. These results suggest that At-Risk individuals tend to consume music with lyrics that reflect their negative emotional states. 

As hypothesized, the themes self-reference and blame were more prevalent in the At-Risk group. Additionally, the themes denial was also shown to be preferred by AtRisk individuals. Since the themes of blame and selfreference in lyrics were found to be associated with unhealthy listening strategies [15], listening to music associated with these themes would not be beneficial to individuals at risk of depression, and in some cases may lead to negative outcomes. This highlights the importance of mindful consumption strategies for music for people at risk of depression. 

In conclusion, our results show that certain music engagement strategies are maladaptive in nature and should be avoided to prevent the worsening of mood, building on top of previous studies in the area. These results can potentially aid in developing intervention strategies based on lyrical content that should be avoided for better outcomes from music listening. 

## 5.1 Limitations 

A limitation of this study is the exclusive focus on lyrical emotions and themes. The interaction of these with the acoustic properties of music and lyrical complexity, as well as in the context of depression risk, could be explored, which could possibly yield a better understanding. The interaction between lyrical themes and emotional connotations is also something that is yet to be studied. Another limitation is that this study exclusively focuses on music with English lyrics. We have also used a predetermined set of themes offered by DICTION, which may not be enough to capture several lyrical themes. An approach to solve this would be to use Large Language Models (LLMs) to generate themes from a repository of songs and then using them for the scoring. 

## 5.2 Future Work 

The results from this paper can be used in building music recommendation systems for depressed individuals that tailor the recommendations, keeping in mind the emotions and themes that are associated with mood worsening and maladaptive behaviors to maximize the positive outcomes through music listening. These results could be combined with other measures associated with such behaviors. This work also opens up the possibility of early depression risk 

1049 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

prediction from online music listening behaviors, in terms of lyrics, by cementing lyrical emotions and themes as indicators for depression risk. These measures, in addition to acoustic features [10] and other indicators such as lyrical complexity and social tags [11,9], could potentially be used to develop a multi-modal depression risk prediction system. 

## 6. REFERENCES 

- [1] W. Depression, “Other common mental disorders: global health estimates,” Geneva: World Health Organization, vol. 24, 2017. 

- [2] A. C. North, D. J. Hargreaves, and J. J. Hargreaves, “Uses of music in everyday life,” Music perception, vol. 22, no. 1, pp. 41–77, 2004. 

- [3] M. Baltazar and S. Saarikallio, “Toward a better understanding and conceptualization of affect self-regulation through music: A critical, integrative literature review,” Psychology of Music, vol. 44, no. 6, pp. 1500–1521, 2016. 

- [4] T. Schäfer, “The goals and effects of music listening and their relationship to the strength of music preference,” PloS one, vol. 11, no. 3, p. e0151634, 2016. 

- [5] D. J. Hargreaves, A. C. North, and M. Tarrant, “135Musical Preference and Taste in Childhood and Adolescence,” in The Child as Musician: A handbook of musical development. Oxford University Press, 06 2006. 

- [6] K. S. McFerran, S. Garrido, and S. Saarikallio, “A critical interpretive synthesis of the literature linking music and adolescent mental health,” Youth & Society, vol. 48, no. 4, pp. 521–538, 2016. 

- [7] J. Stewart, S. Garrido, C. Hense, and K. McFerran, “Music use for mood regulation: Self-awareness and conscious listening choices in young people with tendencies to depression,” Frontiers in Psychology, vol. 10, 2019. 

- [8] K. Mcferran and S. Saarikallio, “Depending on music to feel better: Being conscious of responsibility when appropriating the power of music,” The Arts in Psychotherapy, vol. 41, 01 2013. 

- [9] A. Surana, Y. Goyal, M. Shrivastava, S. Saarikallio, and V. Alluri, “Tag2risk: Harnessing social music tags for characterizing depression risk,” arXiv preprint arXiv:2007.13159, 2020. 

   - [12] A. M. Demetriou, A. Jansson, A. Kumar, and R. M. Bittner, “Vocals in music matter: the relevance of vocals in the minds of listeners,” in International Society for Music Information Retrieval Conference, 2018. [Online]. Available: https://api.semanticscholar. org/CorpusID:53875501 

   - [13] E. Brattico, V. Alluri, B. Bogert, T. Jacobsen, N. Vartiainen, S. Nieminen, and M. Tervaniemi, “A functional mri study of happy and sad emotions in music with and without lyrics,” Frontiers in Psychology, vol. 2, 2011. 

   - [14] S. Saarikallio, C. Gold, and K. Mcferran, “Development and validation of the healthy-unhealthy music scale,” Child and Adolescent Mental Health, vol. 20, 05 2015. 

   - [15] B. Singh, K. Vaswani, S. Paruchuri, S. Saarikallio, P. Kumaraguru, and V. Alluri, ““help! i need some music!”: Analysing music discourse depression on reddit,” PLoS ONE, 2023. 

   - [16] R. Kessler, G. Andrews, L. Colpe, H. EE, D. Mroczek, S.-L. Normand, E. Walters, and A. Zaslavsky, “Short screening scales to monitor population prevlances and trends in non-specific psychological distress,” Psychological medicine, vol. 32, pp. 959–76, 09 2002. 

   - [17] J. Russell, “A circumplex model of affect,” Journal of Personality and Social Psychology, vol. 39, pp. 1161– 1178, 12 1980. 

   - [18] Y. Agrawal, R. G. R. Shanker, and V. Alluri, Transformer-Based Approach Towards Music Emotion Recognition from Lyrics. Springer International Publishing, 2021, p. 167–175. [Online]. Available: http://dx.doi.org/10.1007/978-3-030-72240-1_12 

   - [19] Z. Yang, Z. Dai, Y. Yang, J. Carbonell, R. Salakhutdinov, and Q. V. Le, “Xlnet: Generalized autoregressive pretraining for language understanding,” 2020. 

   - [20] E. Çano and M. Morisio, “Moodylyrics: A sentiment annotated lyrics dataset,” in Proceedings of the 2017 international conference on intelligent systems, metaheuristics & swarm intelligence, 2017, pp. 118–124. 

   - [21] R. Malheiro, R. Panda, P. Gomes, and R. P. Paiva, “Emotionally-relevant features for classification and regression of music lyrics,” IEEE Transactions on Affective Computing, vol. 9, pp. 240–254, 2018. [Online]. Available: https://api.semanticscholar.org/ CorpusID:21791683 

- [10] A. Surana, Y. Goyal, and V. Alluri, “Static and dynamic measures of active music listening as indicators of depression risk,” Oct. 2020. 

- [11] J. Shriram, S. Paruchuri, and V. Alluri, “How much do lyrics matter? analysing lyrical simplicity preferences for individuals at risk of depression,” Aug. 2021. 

1050 

