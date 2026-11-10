---
paper_id: "000096"
year: 2022
title: "Download pdf"
source_url: "https://zenodo.org/record/7343071/files/000096.pdf"
---

# ªMORE THAN WORDSº: LINKING MUSIC PREFERENCES AND MORAL VALUES THROUGH LYRICS 

Vjosa Preniqi<sup>1</sup> Kyriaki Kalimeri<sup>2</sup> Charalampos Saitis<sup>1</sup> 1 Centre for Digital Music, Queen Mary University of London, London UK 

2 ISI Foundation, Turin, Italy 

{v.preniqi, c.saitis}@qmul.ac.uk, kyriaki.kalimeri@isi.it, 

## ABSTRACT 

This study explores the association between music preferences and moral values by applying text analysis techniques to lyrics. Harvesting data from a Facebook-hosted application, we align psychometric scores of 1,386 users to lyrics from the top 5 songs of their preferred music artists as emerged from Facebook Page Likes. We extract a set of lyrical features related to each song’s overarching narrative, moral valence, sentiment, and emotion. A machine learning framework was designed to exploit regression approaches and evaluate the predictive power of lyrical features for inferring moral values. Results suggest that lyrics from top songs of artists people like inform their morality. Virtues of hierarchy and tradition achieve higher prediction scores (.20 ≤ r ≤ .30) than values of empathy and equality (.08 ≤ r ≤ .11), while basic demographic variables only account for a small part in the models’ explainability. This shows the importance of music listening behaviours, as assessed via lyrical preferences, alone in capturing moral values. We discuss the technological and musicological implications and possible future improvements. 

## 1. INTRODUCTION 

The field of music recommender systems has a lot to gain from the fields of music psychology and sociology [1,2], where researchers have found converging evidence that people listen to music that reflects their personality needs [3±7] and helps express their values [8±10]. For example, extroverted people tend to choose more energetic and rhythmic tunes, while listeners holding values of understanding and tolerance prefer more sophisticated and complex music. Indeed, operationalising knowledge of how personality traits relate to listener taste and preferences has already been shown to improve music recommendations [11,12] and to make them more diverse [13]. Yet personality dispositions alone may not suffice to explain, and thus model, our music listening behaviours. 

> © V. Preniqi, K. Kalimeri, and C. Saitis. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: V. Preniqi, K. Kalimeri, and C. Saitis, ªªMore than wordsº: Linking Music Preferences and Moral Values through Lyricsº, in Proc. of the 23rd Int. Society for Music Information Retrieval Conf., Bengaluru, India, 2022. 

Aiming to advance an integrative view of the music listener, which may benefit music recommender system scenarios, we set to explore the less attended relation between moral values and music preferences. If personal values are conceived as intrinsic motivational goals, moral values reflect traits learned under the influence of society, culture, and religion, amongst others, which bond people together into groups. Considering music as an evolved tool of social affiliation and bonding [14,15], it is reasonable to speculate that people may like certain music styles and genres because they provide stimuli that match their morality-related needs. 

We further hypothesise that moral values are expressed more clearly in a verbal rather than non-verbal manner and examine their influence on musical taste through lyrics. When people listen to sung music, their preferences are driven by not only the audio content but also the content of lyrics [16]. Lyrics convey rich, multifaceted messages about societal issues such as love, life and death, but also political or religious concepts, often independently from melodic and other audio information [17]. Lyrical messages can support listeners’ mental health [18]. Nonetheless, little is known about whether lyrical information manifests links between psychological traits and music preferences [19]. To what extent are moral values reflected in the lyrics of one’s favourite songs? Do lyrics predict the moral traits of listeners? 

To tackle these questions, we used data from the LikeYouth.org project, a Facebook-hosted application developed specifically for research purposes as a surveying tool and was mainly deployed in Italy. Upon providing their informed consent, participants completed validated psychometric questionnaires for personality, moral traits and basic human values, basic demographic information such as age and gender, while agreed to share their Page Likes (see [20] for a detailed description of the complete dataset). For the purpose of this study we only analysed moral values scores and Likes on music artist Pages. Combining these with information from the genius.com music database, we obtained the lyrics from the five most popular songs per artist. We performed both sentiment [21] and emotion [22] analysis on the obtained lyrics, assessed their moral narratives employing the MoralStrength lexicon [23], and examined themes and overarching narratives through topic modelling [24]. 

We built a series of regression models that infer moral traits from lyrical content, demographics, and Likes-based 

797 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

features (e.g., artist popularity). Our findings show that peoples’ worldviews and moral values are indeed reflected in their music preferences as modelled through lyrics, in line with recent literature [25,26]. Extracting topic and moral features from lyrics specifically increased model performance over sentiment, emotion, and demographic features. 

We contribute to the growing literature studying the interplay between music and psychology, with findings that clearly link the preferences of people to artists and songs that are in line with their moral values. Personalised recommendations for streaming on-demand music can be greatly enriched by including notions of moral worldviews about their listeners instead of only shallow psychological attributes [1,5,10]. Such knowledge can be directly implemented in psychologically aware music recommender systems, improving music streaming services and contributing to listener wellbeing [27]. On a different key, the relationship between moral worldviews and music preference is crucial to inform communication experts about their choice of the most appropriate music piece to accompany a social campaign. 

## 2. BACKGROUND 

We operationalise morality via the Moral Foundations Theory (MFT) [28], which expresses the psychological basis of moral reasoning in terms of five innate foundations, namely Care/Harm, Fairness/Cheating, Loyalty/Betrayal, Authority/Subversion, and Purity/Degradation. These can further collapse into two superior foundations: Individualising (Care and Fairness), indicative of a more liberal perspective, and Binding (Purity, Authority and Loyalty), indicative of a more conservative outlook. 

Moral foundations are considered to be higher psychological constructs than the more commonly investigated personality traits [29]. They have been associated with attitudes towards complex situations such as politics [30,31], climate change [32], and vaccination [33,34]. 

However, moral values have attracted less attention from music scientists. Using data from an ad-hoc online survey comprising, among other items, MFQ scores and preferences ratings on 13 music genres, Preniqi et al. [25] found that people with higher levels of Binding foundations (e.g., more authoritarian individuals) tend to listen to country and Christian music, the lyrics of which often foster notions of tradition [3]. Those with lower levels of Binding traits tend to prefer music genres such as punk and hip-hop, where lyrics are known to challenge traditional values, and the status quo [8]. Individualising foundations were overall harder to predict (cf. [35]). Furthermore, including demographic information (e.g., age, gender, political views, education) improved MFT predictions marginally, indicating the ability of music preferences alone to explain one’s moral values. 

In the computational social science field, recent work has demonstrated the predictability of MFT traits from a variety of digital data, including gameplay [36], smartphone usage and web browsing [35]. Moral values can also be explained by verbal data, as they can be more clearly communicated through thoughts and opinions [23,34,37]. Several 

|||Census|MFT<br>All data<br>n= 3,920|MFT &≥10<br>Page Likes<br>n= 1,386|
|---|---|---|---|---|
|Gender|M|48%|54%|53%|
||F|52%|46%|47%|
|A|<25|23%|21%|29%|
|ge|≥25|77%|79%|71%|



Table 1. Demographic breakdown of our data according to gender and age. The ªCensusº column reports the national distribution per attribute according to the statistics provided by the official census bureau [45]. 

dictionary-based approaches for predicting moral values expressed in texts such as tweets and other social media posts have been proposed, including the Moral Foundations Dictionary [37, 38] and the MoralStrength lexicon [23]. Here we employ the latter to uncover moral narratives in song lyrics, which we then use to predict the moral traits of listeners. 

The relation between lyrics and music preferences has only recently started to receive attention across music and social psychology disciplines. Some studies have suggested associations between the personality or mental health of songwriters and their lyrics [39,40]. On the listener side, neurotic individuals tend to listen to songs with more complex and less repetitive lyrics that express negative emotions [19,41]. More conscientious individuals tend to prefer lyrics talking about achievements [19] but also about love [42]. Importantly, preferences for lyrics are found to be predictive of personality traits distinctly from audio or melodic preferences [19,42]. 

Concerning moral values, in recent work, they have been found to explain a unique and significant portion of the variance in the lyrical preferences of different metal music sub-genre fans that was not already accounted for by personality traits [26]. For example, preferring lyrics about celebrating metal culture and unity was related to higher levels of the Loyalty foundation and higher levels of extroversion. In U.S. popular music, an increase in lyrics related to self-focus and -promotion since the 1980s has been shown to manifest the increasing individualism of American society [43,44]. 

## 3. DATA COLLECTION 

The LikeYouth Facebook-hosted application was initially launched in March 2016, while the data used here were downloaded in September 2019. It was deployed mainly in Italy, where approximately 64,000 people entered the platform, from whom 3,920 users (90% geolocated in Italian territory) filled out the MFT questionnaire correctly. 

Of those, 47% did not provide their age due to the facultative nature of LikeYouth. Because we wished to include age as a demographic predictor variable, we inferred the missing values from all (e.g., not just music artist related) Page Likes of the 3,920 users. Similar to [46] we created 

798 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

a sparse matrix representation of Page Likes per user and applied sparse singular value decomposition to reduce dimensionality, while binning the age attribute (median = 25) as ªyoungerº (< 25) and ªolderº (≥ 25) allowed to approximate the official census distribution [45]. We then employed an XGBoost classifier, to predict missing age values [35], with an estimated AUROC = 0.79 and standard deviation = 0.018. Acknowledging that age inference might add bias to our models, we only use age as a predictor in isolated experiments (see Table 4). We also run the same experiments keeping only users who provided their age. Predictions were similar for Binding and slightly lower for Individualising. 

To ensure the stability of our regression models, we applied a simple activity threshold. After extensive experimentation we chose to drop users with less than 10 Facebook Page Likes related to music artists (Page category selection), resulting in a reduced final dataset of 1,386 users. Table 1 reports the demographic breakdown of our data sample in terms of gender and age, which follows closely the population distribution of the official Italian census [45]. 

For the final 1,386 users, we retrieved song lyrics corresponding to their music artist Page Likes using genius.com. Querying the Genius API, we initially obtained the 10 most popular songs per artist alongside the respective lyrics. We assume that if a user liked the Page of a specific artist, then that artist’s most famous songs (as per Genius) reflect the music preferences of the user. We carried out predictive tasks using the n = 10, 5, or 3 most popular songs from an artist and found that n = 5 gave the best compromise in terms of predictions, computational resources, and withinmusician variability in lyrical and audio content (see future work discussion) while maintaining an optimal number of musicians and songs for our lyrics data. Finally, we used the spaCy library [47, 48] to identify songs with English lyrics only, resulting in 3,179 artists and 15,895 songs. 

We also considered two additional, more shallow digital trace features that can potentially convey information about user’s music habits, namely the number of Page Likes per user (mean = 35.11, standard deviation = 33.95) and a built-in feature of artist popularity from LikeYouth, based on the number of Page followers. 

We use LikeYouth because, to our best knowledge, it is the only dataset providing MFT scores of individuals alongside a potential proxy of their music preferences (e.g., artist Page Likes). A limitation of this approach is that the data provided by LikeYouth are static and may thus refer to a snapshot of music interests in time. Streaming platforms could offer richer information about habitual music listening [7,42]. Nonetheless, there is substantial evidence that Facebook Page Likes can capture personality needs and personal values [5,20,46]. Another limitation is that LikeYouth user MFT scores and thus our predictive models cannot be made publicly available due to privacy implications [34]. Instead, we have shared the lyrics data and related source code for lyrical feature modeling in a GitHub repository.<sup>1</sup> 

|Type|Method|Features|
|---|---|---|
|Topics|LDA|Death/Fear/Violence,<br>Obscene, Romantic,<br>World/Time/Life|
|Morals|MoralStrength|Care, Fairness, Loyalty,<br>Authority, Purity|
|Sentiment|VADER|Negative, Positive,<br>Neutral, Compound|
|||Anger, Disgust, Fear,|
|Emotions|NRC|Sadness, Anticipation,<br>Surprise, Joy, Trust|



Table 2. Summary of lyrical features used in this study. 

## 4. LYRICS CONTENT ANALYSIS 

We extracted a set of textual features related to each song lyrics’ overarching narrative (topic modelling), moral valence, sentiment, and emotion. Based on the corresponding feature modeling method, we applied different levels of text preprocessing. Sentiment detection required only a general cleanup while keeping punctuation and capitalization within the text. For the other methods, we extracted Part Of Speech (POS) lemmas using the spaCy lemmatizer [47]. On average, each lyrics contained 273 words and 108 lemmas. 

## 4.1 Topic Modelling 

Initially, we aimed to uncover common patterns in the lyrics narratives by applying a topic modelling approach based on Latent Dirichlet Allocation (LDA) [24]. We used LDA due to its simplicity, high accuracy in topic modelling, and good computational efficiency [49]. The input of the LDA model is a term frequency matrix of the corpus created by the song lyrics. To eliminate very common terms that can lead to irrelevant topics, we ignored words with frequency higher than 90%. 

To derive the optimum number of topics k, we optimized the topic coherency (Cv metric [50]) for models with k ∈ [2, 16] using a step size of 2. The number of topics for which coherency was maximised was k = 4. For k > 4, we obtained topics that were either generic or hard to characterise due to the mixture of different words belonging to multiple topics. While for k = 4, the topics obtained were in line with previous literature [51,52]. Table 3 depicts examples of manually selected songs of 5 artists for each topic, ranked by descending weight in the specific topic. 

## 4.2 Moral Valence 

We assess the moral narratives by employing the MoralStrength lexicon [23], which holds the state-of-the-art performance in moral text prediction. This expands the Moral Foundation Dictionary by offering three times more moralannotated lemmas. The lexicon provides, along with each lemma, the moral valence score, a numeric assessment that indicates both the polarity and the intensity of the lemma 

1 https://github.com/vjosapreniqi/ lyrics-content-features 

799 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

|Topic|Artist|Song Title|%|
|---|---|---|---|
||Mike Williams<br>|Give it up<br>|99<br>|
|Romantic|Marc Anthony|I need to know<br>|99|
|(039)|NSYNC|I want you back|99|
|.|Willie Nelson|Always on my mind|98|
||Alexia|Because I miss you|97|
||Tyga|Rack city<br>|98<br>|
|Obscene|Fat Joe|Yellow tape|96|
|(024)|Cardi B|Bartier cardi|95|
|.|Chamillionaire|Ridin’|95|
||21 Savage|Bank account|91|
||Holly Herndon|Morning sun|99|
|World/Time/|Noisecontrollers|The day|97|
|Life|Nathan East|Finally home|96|
|(0.22)|Dave Gahan|Tomorrow|94|
||Gabrielle Aplin|Start of time|90|
||Hatebreed|Destroy everything|99|
|Death/Fear/|Fear Factory|Edgecrusher|97|
|Violence|Eomac|Mandate for murder|95|
|(0.15)|Destruction|Thrash till death|92|
||Sabaton|Attack of dead men|91|



Table 3. LDA topic modelling: overall topic prevalence (in brackets below topic descriptions) and 5 manually selected songs per topic as ranked by descending topic proportion. 

in each of the five moral foundations (MFT traits). Moral valence is expressed on a Likert scale from one to nine, with five considered neutral. When lower than 5, scores reflect notions closer to Harm, Cheating, Betrayal, Subversion, and Degradation, while values higher than 5 indicate Care, Fairness, Loyalty, Authority, and Purity, respectively. 

We obtained a moral valence score for each lemma in a song’s lyrics and each MFT trait, which is then averaged across lemmas for each song. Negation correction was not applied, as moral foundation polarities do not directly translate as opposites (e.g., ªnot careº is not the same as ªharmº). The MoralStrength lexicon has a limited linguistic coverage; as a result, we could not predict moral valence for 16% of the collected lyrics. Instead, we assigned them the value 5, the neutral point of the moral valence Likert scale. This approach pushes the observed mean towards the center of the scale, but captures the variability of the moral values across all the lyrical data. 

## 4.3 Sentiment and Emotion Analysis 

In textual data, emotions, as brief and preconscious phenomena, can be defined via descriptions of appraisal, physiological reaction, expressive display, feeling, or action tendency, while sentiments, as lasting and conscious emotional dispositions, tend to be modelled in terms of text polarity (positive, negative, neutral) [53]. 

We applied the commonly used VADER (Valence Aware Dictionary and sEntiment Reasoner) model [21] on the lyrical text to obtain information about the sentiment of each song. The VADER model is shown to perform well both with long and short text, providing for each song a score for positive, neutral, negative, and compound sentiment 



<!-- Start of picture text -->
Correlations for Individualising<br>lyric_care<br>fear<br>trust<br>anticipation<br>anger<br>joy<br>positive<br>negative<br>gender<br>-0.2 -0.1 0.1 0.2<br>Correlations for Binding<br>artist liked no<br>polularity<br>lyric_authority<br>lyric_care<br>lyric_purity<br>lyric_fairness<br>death/violence<br>world/life<br>Romantic<br>sadness<br>fear<br>disgust<br>anticipation<br>anger<br>trust<br>joy<br>negative<br>positive<br>-0.2 -0.1 0.1 0.2<br>Demographics Lyrics sentiment Lyrics word emotions<br>FB features Lyrics topics Lyrics moral strength<br><!-- End of picture text -->

Figure 1. Spearman’s Rank correlations of MFT super foundations with demographics, artist likes and lyrics features. We report only ones that were significant at p ≤ .01. ªArtist liked noº refers to the number of artist Likes per user. 

(see Table 2). We also estimated the eight basic emotions defined in the Plutchik wheel of emotions [54] employing the NRC Word±Emotion Association Lexicon [22]. This lexicon was shown to be efficient with unlabeled data [55]. Each song lyrics was annotated with the eight emotions (see Table 2) by averaging its word emotion association scores. 

## 5. EXPERIMENTS AND RESULTS 

Initially, we explored the relationship between users’ moral values as emerged from the self-reported questionnaires, basic demographic attributes, and their respective music preferences, as expressed in the linguistic components of the lyrics. Figure 1 depicts the statistically significant correlations (p ≤ .01) obtained for the two superior foundations, namely Individualising and Binding. We observed that people who value more Individualising foundations prefer artists whose songs prevalently talk about anticipation and trust. On the other side, those concerned more about social order and Binding foundations tend to prefer artists who deal with more romantic topics in their songs instead of existential and social issues. Overall, participants with strong Binding foundations display a tendency to dislike songs with negative valence and emotions such as sadness, fear, or disgust. Yet both the Individualising and Binding groups resonate with positive and joyful songs, showing that despite often profound differences in sociopolitical stances, music is a shelter to everyone. 

Next, we proposed a series of experimental designs to 

800 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
Care Fairness<br>Loyalty<br>lyric_care joy popularity<br>anticipation trust sadness<br>joy lyric_care Feature value negative<br>trust gender Death/Fear/Violence<br>-0.4 0.4 -0.4-0.3 -0.2 -0.1 0.0 0.2 0.3 0.4<br>SHAP value (impact on model output) SHAP value (impact on model output) SHAP value (impact on model output)<br>Authority Purity<br>popularity popularity<br>sadness negative<br>negative Feature value positive Feato utlue<br>Death/Fear/Violence Death/Fear/Violence<br>-0.1 -0.2 -0.1 0.1 0.4<br>SHAP value (impact on model output) SHAP value (impact on model output)<br><!-- End of picture text -->

Figure 2. Top 4 individual feature contributions (via SHAP values) for the five basic moral foundations from experiment EX8 (see Table 4). The higher the SHAP value, the more the feature contributes to the prediction model. 

|ID|Features|
|---|---|
|EX1|Sentiment (VADER)|
|EX2|Emotions (NRC)|
|EX3|Sentiment + Emotions|
|EX4|Best of {EX1, EX2, EX3} + Morals|
|EX5|Best of {EX1, EX2, EX3} + Topics|
|EX6|Best of {EX1, EX2, EX3} + Morals + Topics|
|EX7|EX6 + Age + Gender|
|EX8|EX7 + Artist Likes + Artist Popularity|



Table 4. Summary of performed experiments with corresponding features used as predictors. 

infer moral values of the participants from their music preferences and the respective linguistic content. Table 4 summarises the performed experiments. We employed four algorithms, namely Support Vector Regressor, Random Forest, XGBoost, and ElasticNet, to predict moral values using a multivariate regression approach over a 5-fold crossvalidation setting. For each participant, the features were aggregated and normalised. Here, we report only the results from the Random Forest since it slightly outperformed the rest. We used the Pearson’s correlation coefficients between the predicted and actual moral values scores to measure the model’s goodness fit. This metric was commonly used in papers that predicted personality based on users’ music preferences and listening behaviours [5,56]. 

To comprehend the general behaviour of our models and evaluate the importance of each feature, we estimated the SHAP values. SHAP (SHapley Additive exPlanations) is a game theory approach designed to illustrate the features’ contribution to the final output of any machine learning model [57]. 

Following the incremental experimental design reported in Table 4, we trained one model per each moral foundation and presented the best results obtained by each feature in Table 5. In line with recent literature [25] that shows higher prediction accuracy for Binding rather than Individualising foundations, we noticed a similar behaviour also when inferring from linguistic features of song lyrics. 

When adding demographics and artist Facebook information (EX8), the results slightly improved for both super foundations, implying that the more information we have about users’ demographics and music preferences, the more precise our models become. Despite that, the model trained on just emotions, sentiment and moral information (EX4) achieved almost as good results as those who are aware of the demographics and the general artist information (EX7 and EX8). This highlights the importance of music preferences in portraying our goals and decisions whose motivations go far beyond basic demographic knowledge. 

Figure 2 depicts the most important individual (only top 4 due to page restrictions) features for predicting each of the five moral foundations. While Figure 3 illustrates the impact individual (top 8) and grouped features in inferring the two superior foundations when considering all predictor variables (EX8). In line with observed correlations, feature importance representations for regression models show that lyrics linked to objective and subtle emotions (e.g., joy, trust, and anticipation) effectively predict Care and Fairness. Whereas more intense and opposite polarities of sentiment and emotions (e.g., fear, sadness, lyrics positive and negative valence) account for better predictions of Loyalty, Authority and Purity. We noticed that those who value more the Binding foundations appear to be sensitive to the popularity of the song, which reflects their worldview of prioritising group-focus over self-focus. 

## 6. CONCLUSION 

This paper discussed the link between lyrical information and moral values. We presented a wide range of lyrics processing techniques and features for measuring the power of linguistic aspects in predicting complex psychological traits such as moral values. Besides, we explored and compared the impact of user demographics and shallow digital traces in inferring moral foundations against the song lyrics components. 

We noticed that Binders express their views throughout their music preference and lyrical styles. In contrast, Individualising views are more complex to be captured solely by people’s music lyrics preferences. Thus, using the proposed framework, it was easier to infer moral values of Binding 

801 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

||||Moral|Foundations - R|egression Mode|ls|||
|---|---|---|---|---|---|---|---|---|
||EX1|EX2|EX3|EX4|EX5|EX6|EX7|EX8|
|C|.07 [-.05, .19]|.10 [-.02, .21]|.10 [-.02, .22]|.11 [-.01, .22]|.11 [-.01, .22]|.11 [-.01, .22]|.12 [ .01, .24]|.12 [ .01, .23]|
|F|.04 [-.08, .15]|.06 [-.05, .18]|.06 [-.05, .18]|.07 [-.05, .18]|.06 [-.06, .17]|.06 [-.06, .17]|.07 [-.05, .19]|.05 [-.07, .17]|
|L|.11 [-.01, .23]|.16 [ .04, .27]|.18 [ .06, .29]|.20 [ .08, .31]|.19 [ .08, .30]|.20 [ .08, .31]|.20 [ .08, .31]|.21 [ .09, .32]|
|A|.18 [ .06, .29]|.22 [ .10, .32]|.24 [ .12, .34]|.26 [ .15, .37]|.24 [ .13, .35]|.26 [ .15, .36]|.26 [ .15, .37]|.28 [ .16, .38]|
|P|.18 [ .06, .29]|.20 [ .09, .31]|.23 [ .12, .34]|.25 [ .14, .36]|.23 [ .11, .34]|.25 [ .13, .36]|.25 [ .13, .36]|.27 [ .16, .37]|
|I|.08 [-.04, .19]|.09 [-.03, .21]|.10 [-.01, .22]|.09 [-.03, .21]|.10 [-.02, .21]|.09 [-.03, .21]|.10 [-.02, .22]|.11 [-.01, .22]|
|B|.19 [ .07, .30]|.23 [ .11, .34]|.26 [ .15, .37]|.29 [ .17, .39]|.27 [ .15, .37]|.28 [ .17, .39]|.28 [ .17, .39]|.30 [ .19, .41]|



Table 5. Moral foundations regression with Random Forest using different feature combinations (see Table 4): Pearson’s correlation [95% confidence intervals] between predicted and the actual values averaged across 5-fold cross-validation. C: Care; F: Fairness; L: Loyalty; A: Authority; P: Purity; I: Individualising; B: Binding. 



<!-- Start of picture text -->
Individual and grouped features for Individualising<br>High<br>joy Emotions<br>anticipation<br>Sentiment<br>trust<br>gender Demographics<br>lyric_care Feature value Morals<br>positive<br>neutral Topics<br>Artist FB features<br>popularity<br>Low<br>-0.4 -0.3-0.2 -0.1 0.0 0.3 0.4 0.00 0.05 0.10 0.15 0.20 0.25<br>SHAP value (impact on model output) mean(|SHAP valuel) (average impact on model output magnitude)<br>Individual and grouped features for Binding<br>High<br>popularity Emotions<br>negative Sentiment<br>sadness<br>positive Artist FB features<br>Romantic Feature value Topics<br>Death/Fear/Violence Morals<br>lyric_faimness<br>Demographics<br>fear<br>-0.4 0.2 0.3 0.4 0.00 0.05 0.10 0.15 0.20 0.25<br>SHAP value (impact on model output) mean(ISHAP valuel) (average impact on model output magnitude)<br><!-- End of picture text -->

Figure 3. Individual (top 8) and grouped feature contributions (via SHAP values) for the two superior moral foundations from experiment EX8 (see Table 4). The higher the SHAP value, the more the feature contributes to the prediction model. 

(.20 ≤ r ≤ .30) between predicted and target values than Individualising foundations (.08 ≤ r ≤ .11). 

We demonstrated that lyrics features extracted from the naturally emerging music preferences in social media, to some extent, allow for constructing reliable inferences of moral values. Considering the expanded presence of online music streaming services our findings may have direct implications for music recommendation and personalisation algorithms [1,5,58]. Since moral values are a key element of the decision making process in several societal issues [35,59] and highly linked to political leanings [60], our research implications can help future studies to tackle aspects of why and how music is or can be used for mass stimulation and persuasion in social and political campaigns, raising awareness on what our digital music behaviours can reveal. 

In future work, we intend to combine audio and lyrical content analysis together in a multimodal framework to further expand our understanding of music and moral affiliations, especially for Individualising foundations that remain hard to predict. Recent work highlights that preferences for both lyrics and audio features are important in predicting, often distinctly, personality traits [42]. We will also use additional data from LikeYouth to investigate if moral foundations can explain variance in music preferences that cannot be accounted for by personality traits and personal values (cf. [26]). We ultimately aim to integrate our findings into novel psychologically aware music recommender systems, but also beyond the music domain to other media. 

802 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

## 7. ACKNOWLEDGEMENTS 

This work was supported by the QMUL Centre for Doctoral Training in Data-informed Audience-centric Media Engineering (2021±2025) as part of a PhD studentship awarded to VP. KK acknowledges support from the Lagrange Project of the Institute for Scientific Interchange Foundation (ISI Foundation) funded by Fondazione Cassa di Risparmio di Torino (Fondazione CRT). We would like to thank the three anonymous reviewers and the meta-reviewer for their thoughtful comments. 

## 8. REFERENCES 

- [1] L. Porcaro, C. Castillo, and E. Gómez Gutiérrez, ªDiversity by design in music recommender systems,º Transactions of the International Society for Music Information Retrieval. 2021; 4 (1)., 2021. 

- [2] A. Laplante, ªImproving music recommender systems: What can we learn from research on music tastes?º in ISMIR, 2014, pp. 451±456. 

- [3] P. J. Rentfrow and S. D. Gosling, ªThe do re mi’s of everyday life: the structure and personality correlates of music preferences.º Journal of personality and social psychology, vol. 84, no. 6, p. 1236, 2003. 

- [4] D. M. Greenberg, M. Kosinski, D. J. Stillwell, B. L. Monteiro, D. J. Levitin, and P. J. Rentfrow, ªThe song is you: Preferences for musical attribute dimensions reflect personality,º Social Psychological and Personality Science, vol. 7, no. 6, pp. 597±605, 2016. 

- [5] G. Nave, J. Minxha, D. M. Greenberg, M. Kosinski, D. Stillwell, and J. Rentfrow, ªMusical preferences predict personality: evidence from active listening and facebook likes,º Psychological science, vol. 29, no. 7, pp. 1145±1158, 2018. 

- [6] S. P. Devenport and A. C. North, ªPredicting musical taste: Relationships with personality aspects and political orientation,º Psychology of Music, vol. 47, no. 6, pp. 834±847, 2019. 

- [7] I. Anderson, S. Gil, C. Gibson, S. Wolf, W. Shapiro, O. Semerci, and D. M. Greenberg, ªªjust the way you areº: Linking music listening on spotify and personality,º Social Psychological and Personality Science, vol. 12, no. 4, pp. 561±572, 2021. 

- [8] A. Gardikiotis and A. Baltzis, ª‘rock music for myself and justice to the world!’: Musical identity, values, and music preferences,º Psychology of Music, vol. 40, no. 2, pp. 143±163, 2012. 

- [9] V. Swami, F. Malpass, D. Havard, K. Benford, A. Costescu, A. Sofitiki, and D. Taylor, ªMetalheads: The influence of personality and individual differences on preference for heavy metal.º Psychology of Aesthetics, Creativity, and the Arts, vol. 7, no. 4, p. 377, 2013. 

- [10] S. Manolios, A. Hanjalic, and C. C. Liem, ªThe influence of personal values on music taste: Towards value-based music recommendations,º in Proceedings of the 13th ACM Conference on Recommender Systems, 2019, pp. 501±505. 

- [11] R. Hu and P. Pu, ªEnhancing collaborative filtering systems with personality information,º in Proceedings of the fifth ACM conference on Recommender systems, 2011, pp. 197±204. 

- [12] Y. Jin, N. Tintarev, N. N. Htun, and K. Verbert, ªEffects of personal characteristics in control-oriented user interfaces for music recommender systems,º User Modeling and User-Adapted Interaction, vol. 30, no. 2, pp. 199±249, 2020. 

- [13] F. Lu and N. Tintarev, ªA diversity adjusting strategy with personality for music recommendation.º in IntRS@ RecSys, 2018, pp. 7±14. 

- [14] C. Loersch and N. L. Arbuckle, ªUnraveling the mystery of music: Music as an evolved group process.º Journal of Personality and Social Psychology, vol. 105, no. 5, p. 777, 2013. 

- [15] P. E. Savage, P. Loui, B. Tarr, A. Schachner, L. Glowacki, S. Mithen, and W. T. Fitch, ªMusic as a coevolved system for social bonding,º Behavioral and Brain Sciences, vol. 44, 2021. 

- [16] A. M. Demetriou, A. Jansson, A. Kumar, and R. M. Bittner, ªVocals in music matter: the relevance of vocals in the minds of listeners.º in ISMIR, 2018, pp. 514±520. 

- [17] S. O. Ali and Z. F. Peynircio˘glu, ªSongs and emotions: are lyrics and melodies equal partners?º Psychology of music, vol. 34, no. 4, pp. 511±534, 2006. 

- [18] J. H. Lee, A. Bhattacharya, R. Antony, N. K. Santero, and A. Le, ªFinding home: Understanding how music supports listener mental health through a case study of bts,º in ISMIR, 2021, pp. 358±365. 

- [19] L. Qiu, J. Chen, J. Ramsay, and J. Lu, ªPersonality predicts words in favorite songs,º Journal of Research in Personality, vol. 78, pp. 25±35, 2019. 

- [20] A. Urbinati, K. Kalimeri, A. Bonanomi, A. Rosina, C. Cattuto, and D. Paolotti, ªYoung adult unemployment through the lens of social media: Italy as a case study,º in International Conference on Social Informatics. Springer, 2020, pp. 380±396. 

- [21] C. Hutto and E. Gilbert, ªVader: A parsimonious rulebased model for sentiment analysis of social media text,º in Proceedings of the international AAAI conference on web and social media, vol. 8, no. 1, 2014, pp. 216±225. 

- [22] S. M. Mohammad and P. D. Turney, ªCrowdsourcing a word±emotion association lexicon,º Computational intelligence, vol. 29, no. 3, pp. 436±465, 2013. 

803 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

- [23] O. Araque, L. Gatti, and K. Kalimeri, ªMoralstrength: Exploiting a moral lexicon and embedding similarity for moral foundations prediction,º Knowledge-based systems, vol. 191, p. 105184, 2020. 

- [24] D. M. Blei, A. Y. Ng, and M. I. Jordan, ªLatent dirichlet allocation,º Journal of machine Learning research, vol. 3, no. Jan, pp. 993±1022, 2003. 

- [25] V. Preniqi, K. Kalimeri, and C. Saitis, ªModelling moral traits with music listening preferences and demographics,º arXiv preprint arXiv:2107.00349, 2021. 

- [26] K. J. Messick and B. E. Aranda, ªThe role of moral reasoning & personality in explaining lyrical preferences,º PLoS one, vol. 15, no. 1, p. e0228057, 2020. 

- [27] Y. Mejova and K. Kalimeri, ªEffect of values and technology use on exercise: implications for personalized behavior change interventions,º in Proceedings of the 27th ACM Conference on User Modeling, Adaptation and Personalization, 2019, pp. 36±45. 

- [28] J. Graham, J. Haidt, S. Koleva, M. Motyl, R. Iyer, S. P. Wojcik, and P. H. Ditto, ªMoral foundations theory: The pragmatic validity of moral pluralism,º in Advances in experimental social psychology. Elsevier, 2013, vol. 47, pp. 55±130. 

- [29] D. P. McAdams and J. L. Pals, ªA new big five: fundamental principles for an integrative science of personality.º American psychologist, vol. 61, no. 3, p. 204, 2006. 

- [30] A. Miles and S. Vaisey, ªMorality and politics: Comparing alternate theories,º Social Science Research, vol. 53, pp. 252±269, 2015. 

- [31] J. Haidt and J. Graham, ªWhen morality opposes justice: Conservatives have moral intuitions that liberals may not recognize,º Social Justice Research, vol. 20, no. 1, pp. 98±116, 2007. 

- [32] C. Wolsko, H. Ariceaga, and J. Seiden, ªRed, white, and blue enough to be green: Effects of moral framing on climate change attitudes and conservation behaviors,º Journal of Experimental Social Psychology, vol. 65, pp. 7±19, 2016. 

- [33] A. B. Amin, R. A. Bednarczyk, C. E. Ray, K. J. Melchiori, J. Graham, J. R. Huntsinger, and S. B. Omer, ªAssociation of moral values with vaccine hesitancy,º Nature Human Behaviour, vol. 1, no. 12, pp. 873±880, 2017. 

- [34] K. Kalimeri, M. G. Beiró, A. Urbinati, A. Bonanomi, A. Rosina, and C. Cattuto, ªHuman values and attitudes towards vaccination in social media,º in Companion Proceedings of The 2019 World Wide Web Conference, 2019, pp. 248±254. 

- [35] K. Kalimeri, M. G. Beiró, M. Delfino, R. Raleigh, and C. Cattuto, ªPredicting demographics, moral foundations, and human values from digital behaviours,º Comput. Hum. Behav., vol. 92, pp. 428±445, 2019. 

- [36] E. Kim, R. Iyer, J. Graham, Y.-H. Chang, and R. Maheswaran, ªMoral values from simple game play,º in International Conference on Social Computing, Behavioral-Cultural Modeling, and Prediction. Springer, 2013, pp. 56±64. 

- [37] Y. Lin, J. Hoover, G. Portillo-Wightman, C. Park, M. Dehghani, and H. Ji, ªAcquiring background knowledge to improve moral value prediction,º in 2018 ieee/acm international conference on advances in social networks analysis and mining (asonam). IEEE, 2018, pp. 552±559. 

- [38] J. Graham, J. Haidt, and B. A. Nosek, ªLiberals and conservatives rely on different sets of moral foundations.º Journal of personality and social psychology, vol. 96, no. 5, p. 1029, 2009. 

- [39] D. M. Greenberg, S. C. Matz, H. A. Schwartz, and K. R. Fricke, ªThe self-congruity effect of music.º Journal of Personality and Social Psychology, 2020. 

- [40] E. J. Lightman, P. M. McCarthy, D. F. Dufty, and D. S. McNamara, ªUsing computational text analysis tools to compare the lyrics of suicidal and non-suicidal songwriters,º in Proceedings of the Annual Meeting of the Cognitive Science Society, vol. 29, no. 29, 2007. 

- [41] J. Shriram, S. Paruchuri, and V. Alluri, ªHow much do lyrics matter? analysing lyrical simplicity preferences for individuals at risk of depression,º arXiv preprint arXiv:2109.07227, 2021. 

- [42] L. Sust, G. Kudchadker, R. Schoedel, T. Schuwerk, M. Bühner, and C. Stachl, ªPersonality computing with naturalistic music listening data,º 2022. 

- [43] C. N. DeWall, R. S. Pond Jr, W. K. Campbell, and J. M. Twenge, ªTuning in to psychological change: Linguistic markers of psychological traits and emotions over time in popular us song lyrics.º Psychology of Aesthetics, Creativity, and the Arts, vol. 5, no. 3, p. 200, 2011. 

- [44] P. McAuslan and M. Waung, ªBillboard hot 100 songs: Self-promoting over the past 20 years.º Psychology of Popular Media Culture, vol. 7, no. 2, p. 171, 2018. 

- [45] I.Stat, ªItalian statistics,º http://dati.istat.it/, accessed: 2019-09. 

- [46] M. Kosinski, Y. Bachrach, P. Kohli, D. Stillwell, and T. Graepel, ªManifestations of user personality in website choice and behaviour on online social networks,º Machine learning, vol. 95, no. 3, pp. 357±380, 2014. 

- [47] M. Honnibal and I. Montani, ªspaCy 2: Natural language understanding with Bloom embeddings, convolutional neural networks and incremental parsing,º 2017, to appear. 

804 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

- [48] M. Neumann, D. King, I. Beltagy, and W. Ammar, ªScispaCy: Fast and robust models for biomedical natural language processing,º in Proceedings of the 18th BioNLP Workshop and Shared Task. Florence, Italy: Association for Computational Linguistics, Aug. 2019, pp. 319±327. [Online]. Available: https: //aclanthology.org/W19-5034 

- [49] A. Lancichinetti, M. I. Sirer, J. X. Wang, D. Acuna, K. Körding, and L. A. N. Amaral, ªHigh-reproducibility and high-accuracy method for automated topic classification,º Physical Review X, vol. 5, no. 1, p. 011007, 2015. 

- [50] M. Röder, A. Both, and A. Hinneburg, ªExploring the space of topic coherence measures,º in WSDM, 2015, pp. 399±408. 

- [51] S. Sasaki, K. Yoshii, T. Nakano, M. Goto, and S. Morishima, ªLyricsradar: A lyrics retrieval system based on latent topics of lyrics.º in Ismir, 2014, pp. 585±590. 

- [52] L. Misael, C. Forster, E. Fontelles, V. Sampaio, and M. França, ªTemporal analysis and visualisation of music,º in Anais do XVII Encontro Nacional de Inteligência Artificial e Computacional. SBC, 2020, pp. 507± 518. 

- [53] M. Munezero, C. S. Montero, E. Sutinen, and J. Pajunen, ªAre they different? affect, feeling, emotion, sentiment, and opinion detection in text,º IEEE transactions on affective computing, vol. 5, no. 2, pp. 101±111, 2014. 

- [54] R. Plutchik, ªA psychoevolutionary theory of emotions,º 1982. 

- [55] E. Çano and M. Morisio, ªMoodylyrics: A sentiment annotated lyrics dataset,º in Proceedings of the 2017 International Conference on Intelligent Systems, Metaheuristics & Swarm Intelligence, 2017, pp. 118±124. 

- [56] A. Anderson, L. Maystre, I. Anderson, R. Mehrotra, and M. Lalmas, ªAlgorithmic effects on the diversity of consumption on spotify,º in Proceedings of The Web Conference 2020, 2020, pp. 2155±2165. 

- [57] S. M. Lundberg and S.-I. Lee, ªA unified approach to interpreting model predictions,º Advances in neural information processing systems, vol. 30, 2017. 

- [58] J. R. Ogden, D. T. Ogden, and K. Long, ªMusic marketing: A history and landscape,º Journal of Retailing and Consumer Services, vol. 18, no. 2, pp. 120±125, 2011. 

- [59] J. Haidt and C. Joseph, ªIntuitive ethics: How innately prepared intuitions generate culturally variable virtues,º Daedalus, vol. 133, no. 4, pp. 55±66, 2004. 

- [60] G. Lakoff, Moral politics: How liberals and conservatives think. University of Chicago Press, 2010. 

805 

