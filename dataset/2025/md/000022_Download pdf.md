---
paper_id: "000022"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706367/files/000022.pdf"
---

# INVESTIGATING MUSIC TRACK LIKING 

# IN THE HALO OF ALBUM COVERS 

Oleg Lesota<sup>1,2∗</sup> 

Anna Hausberger<sup>1,2∗</sup> Ivanna Pshenychna<sup>11</sup> Olha Yehorova<sup>1</sup> Markus Schedl<sup>1,2</sup> 

Oleksandr Shvydanenko<sup>1</sup> 

1 Institute of Computational Perception, Johannes Kepler University Linz, Austria 

2 Linz Institute of Technology, Austria 

> ∗ Equal contribution 

```
markus.schedl@jku.at
```

## ABSTRACT 

Research on music retrieval and recommendation often neglects the fact that a user’s response to a music track depends on contextual factors, such as the composition of the results list, the design of the user interface or the additional media displayed. However, a body of psychological research suggests that human perception and decision making can be strongly influenced by contextual factors. In particular, an initial positive aesthetic impression of a product may influence a buyer’s perception of its features unrelated to appearance, such as utility or reliability, which is a manifestation of a cognitive bias called the halo effect. The work at hand investigates whether an album cover shown to the listener during playback can create a halo effect, influencing the listener’s liking of the track. We approach this question by means of a two-stage user study. In the first stage, participants individually rated a series of album covers and music snippets. In the second stage, they were presented with music tracks and album covers (from those they indicated as unfamiliar to them at the first stage) arranged in pairs, such that their least liked tracks were shown with their most liked album covers and vice versa. The results show that displaying an appealing album cover while playing a music track may result in a higher rating of the track and vice versa. We also observe an indication of halo effect created by the perceived degree of matching between the music tracks and the album cover shown. 

## 1. INTRODUCTION AND RELATED WORK 

The halo effect is a cognitive bias that occurs when an individual’s perception of a specific attribute (positive or negative) influences their opinion on other unrelated attributes [1, 2]. A positive halo effect occurs when a favorable impression of one attribute leads to a positive bias toward other attributes, whereas a negative halo effect, or 

> © O. Lesota, A. Hausberger, I. Pshenychna, O. Shvydanenko, O. Yehorova and M. Schedl. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: O. Lesota, A. Hausberger, I. Pshenychna, O. Shvydanenko, O. Yehorova and M. Schedl, “Investigating Music Track Liking in the Halo of Album Covers”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

“horn effect”, arises when a negative perception of one aspect leads to an overall unfavorable impression [2]. 

Various forms of the halo effect have been studied, with the aesthetic halo effect emerging as one of the most prominent [3]. This effect describes how an initial impression of aesthetics influences opinions on aestheticsunrelated attributes of a product or a person. The aesthetic halo effect has been investigated in several contexts, including webpage usability, product usability, and perceptions of individuals. Kwak et al. [3] find that visual aesthetics of a website, in their study, a charity website, can create an aesthetic halo, shaping the initial perception of the site’s reputation and influencing the evaluation of other website attributes, such as information content quality and usability. In their user study, Minge and Thüring [4] show evidence for two halo effects in user experience with digital audio players. Initially, perceived usability was influenced by visual aesthetics (hedonic halo), but after task completion, perceived visual attractiveness was influenced by system usability (pragmatic halo). In the study of Gulati et al. [5] AI-based beauty filters were shown to increase perceived attractiveness for almost all individuals, regardless of gender, age, and ethnicity. The study confirmed the attractiveness halo effect for traits like intelligence and trustworthiness. 

The halo effect has also been investigated in various entertainment domains. In their research Sahoo et al. [6] show that the halo effect influences movie ratings on Yahoo! Movies, where user ratings of different aspects (e.g., acting, story) are correlated with the overall rating. Their proposed recommendation algorithm, incorporating these dependencies, shows improvements in recommendation accuracy. In the domain of music performance evaluations, it has been shown that positive first impression can impact performance ratings [7, 8]. Furthermore, research has examined the influence of visual appeal on music evaluation, showing that artist attractiveness can positively affect listeners’ ratings of their songs and curiosity about their music. Adrian and Ioana [9] explore how an artist’s visual identity—such as branding, appearance, and promotional materials—influences audience perception of their music, showing that strong branding enhances memorability, engagement, and perceived quality. However, if an artist focuses too much on branding at the expense of authenticity, 

182 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

audiences may become skeptical, which could hurt their long-term success. Schaap et al. [10] explored to what extent evaluations of music are affected by non-musical characteristics of artists, specifically their gender and perceived attractiveness. Their survey experiment reveals a strong halo effect, where more attractive DJs receive higher ratings for their music, with this bias being slightly stronger for male artists. 

Beyond the artist’s image, music album artwork has become a crucial element of music marketing. Album cover designs create expectations, shape first impressions, and even influence the volume of music streaming and sales. A number of studies show that the design of an album cover is connected to the way the audience perceives the related music. Le [11] shows that visual metaphors employed in album cover art impact the listener’s perception of the genre of the song. According to Venkatesan et al. [12] album cover art design choices, such as color schemes and typography, affect the emotional response and expectations of music. Joye and Fennis [13] found that cardinal line orientations in album artwork enhance market performance and listener engagement. 

In the domains of music retrieval and recommendation, cover art has been leveraged, e.g. for music classification [14,15], music exploration [16] or content-based recommendation [17], while receiving limited attention in the context of cognitive biases, and the halo effect in particular [18]. Meanwhile, users of audio and video streaming platforms are often exposed to album cover art while listening to music. This could potentially create a halo effect and influence their perception, in particular liking, of music. Showing that users’ preference is dependent on presence or absence and quality of shown album art would mean that the evaluation procedures employed in music retrieval and recommendation would need to be adjusted to reflect such context. This paper investigates the influence of album cover perception on the liking of a song and examines the potential presence of a halo and horn effects in listeners’ evaluation of music tracks. In this study we tackle the following two research questions: 

• RQ1: To what extent can an album cover, shown during audio playback, influence the listener’s liking of the music track played? 

• RQ2: If present, does the influence of an album cover on music track liking follow the patterns of the halo and/or horn effects? 

## 2. METHODS AND MATERIALS 

We approach answering the research questions by conducting a two-stage user study. In the study we compare user liking of unfamiliar music tracks in situations when (1) the playback is accompanied by an album cover art, and (2) no additional media is shown. To probe both halo and horn effects, for each user, we pair the more appreciated music tracks with least appealing album covers and vice versa. In the first stage of the study, the participants rate a fixed set of music tracks and album covers. In the second stage we 

pair the tracks with the album covers as described above and then the participants rate the music tracks again (with the respective album cover present on screen). At all stages we focus on tracks and album covers the users consider unfamiliar. In the following we describe the procedure in detail<sup>1</sup> . 

## 2.1 Music tracks and album covers 

At the first stage of the study, every participant rated the same sets of 40 album covers and 40 music track snippets. Below we detail the selection process for the items. 

We source the music track snippets from the publicly available Music4All dataset [19], containing 30-second audio snippets, metadata, tags, and other information for 109,269 tracks. We leverage its extension, the Music4All–Onion dataset [20] to assess track and genre popularity based on the number of unique users interacted with each track. In order to ensure diversity in music tracks, we sample them from 5 most popular high-level genres in the dataset. We associate each track with its primary genre, according to Music4All, and aggregate subgenres to high-level genres using AcousticBrainz Genre Dataset [21]. This resulted in selecting the tracks form the following genres: "Rock", "Pop", "Electronic", "Folk, World and Country" and "Funk and Soul". From each genre we select 8 least popular tracks according to Music4All–Onion interaction data in order to increase likelihood of participants being unfamiliar with the tracks. Length of each track was shortened from 30 to 15 seconds in the interest of keeping the study at a reasonable length. 

We source a set of 38,746 album covers for the tracks of Music4All dataset and manually filter out ones containing text such as artist name, song title, or other direct identification information. The filtering procedure resulted in 356 album covers, from which 40 were sampled randomly. 

We limit the sets to the same number of 40 items each in order to (1) be able to create pairs of the rated items, (2) avoid excessive fatigue of the participants. According to Revilla et al. [22] the optimal user study length is 15 minutes with up to 20 min still being acceptable. In our study participants are required to listen to each track for at least 5 seconds before submitting their evaluation. This, combined with the results of a pilot study of 24 participants resulted in an estimate, that the first stage of the study is possible to complete in 16 minutes (motivated participants were allowed to take longer, e.g. if they wished to listen to the full snippets). 

## 2.2 Study stage 1: initial liking of music tracks 

The first stage is divided into two sections. The participants rated at first 40 album covers and in the second section 40 music track snippets of a duration of 15 seconds on a Likert-7 scale interpreting 1 as "I do not like it at all." and 7 as "I like it very much.". The covers and song snippets were randomly shuffled for each participant. Additionally, 

> 1 The resulting item selection, additional statistics and materials can be found in the repository `https://github.com/CPJKU/ music-track-liking-in-album-art-halo` . 

183 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

participants were asked whether they recognized the song ("Do you know this song?") and whether they were familiar with the album cover or an artist featured on it ("Do you know this album cover and/or an artist on it?"), with response options of "Yes" or "No". For the rating of the song snippets, the rating controls become active only after listening to at least 5 seconds of the song. The participants were only able to proceed with the survey after answering both questions for each album cover or music snippet. A previous study [23] supports this approach, confirming that excerpts as short as 5 seconds are already sufficiently representative in terms of preference and familiarity ratings of the song as a whole. 

## 2.3 Study stage 2: track liking in the halo of album art 

Participants who completed the first stage of the study were invited to take part in the second no earlier than 36 hours after completion of the first stage. This time span was chosen based on Ebbinghaus’s research [24], which suggests that most newly acquired information is forgotten within the first 24 hours if not reinforced. For each participant, album covers and songs they recognized were individually removed, creating a personalized list of unfamiliar items. Then these lists were sorted by their rated liking. The lists with ranks of album covers were sorted in descending order (from 7 to 1), and the lists with songs’ ranks were sorted in ascending order (from 1 to 7). The highest rated album covers were then matched with the lowest rated song snippets. If multiple items had the same rating, they were shuffled before matching. In cases in which the lists were of unequal length, items were removed from the middle of the list to keeping the highest- and lowest-rated items. 

In the second stage, participants were presented with pairs consisting of an album cover and a song snippet, created as described above. The pairs were shown in random order to the participants. They were, again, asked whether they recognized either item ("Do you know this album cover and/or this song?") to assess whether the time gap provided was sufficient for forgetting what they previously seen and listened to. In addition, the participants had to rate the song again ("How would you rate this song?"). 

As the album covers were assigned to music tracks based on the participants’ individual evaluation, we include a question to control whether perceived matching of the album cover to the track affected the liking of the track. The participants rated the matching between every track-cover pair presented to them on a Likert-7 scale ("In your opinion, how well does the album cover match the song?"), interpreting 1 as "Does not match at all." and 7 as "Matches very well". The same procedural rules applied as in the first stage: participants had to listen to each snippet for at least 5 seconds before responding, all questions had to be answered before proceeding to the next page of the study. 

## 2.4 Answering the research questions 

We answer RQ1 by investigating the changes in track ranking, according to user liking, associated with showing al- 

bum covers during music playback. For each user we conduct individual analysis only on tracks they marked as unfamiliar during the second stage of the study. We also focus on the users who ended up with at least 10 unfamiliar tracks in the second stage. On the participant level, we compute Kendall rank correlation coefficient (Kendall’s τ ) between track rankings achieved with and without the album cover shown. Kendall’s τ varies in the interval between -1 and 1, with the latter corresponding to the two rankings being identical and, thus, the album cover having no effect on user liking of the tracks. 

To investigate the changes among the initially most and least liked tracks more closely, we compute the agreement score between stage 1 and stage 2 rankings for each user, while focusing on the highest and lowest ranked k items. The agreement score gT op<sup>kbetween top kitems in the two</sup> ranked lists is computed as the the number of items present among the first k positions in both ranked lists (T1<sup>kand</sup> T2<sup>k), divided by the length of the lists, k (Equation 1).The</sup> agreement score for the bottom k items is computed analogously. 



<!-- Start of picture text -->
1 ∩ T k 2 |<br>gT op k = | T k , (1)<br>k<br><!-- End of picture text -->

To ensure that items with the same rating (and therefore tied for the same rank) are fairly considered in the top and bottom k lists, the calculation is repeated 100 times, every time shuffling the tracks with the same rank around. The final agreement score is computed as the average over the 100 runs. To control for the potential influence of shuffling on item position, we compute the standard deviation of each item’s position in the 100 random shuffled lists for each user and stage. This reflects how much an item’s position fluctuates as a result of shuffling. 

We answer RQ2 by investigating Spearman’s rank correlation between the change in the track rating (∆ss) and the appeal of the album cover shown at the second stage (a<sup>1</sup> s<sup>).Inaddition,weinvestigatethecorrelationbetween</sup> the change in the track rating and the perceived matching between the album cover and the associated track (ms). We compute ∆ss = s<sup>2</sup> s<sup>−s1</sup> s<sup>, where s2</sup> s<sup>is the standardized</sup> user liking of the track at the stage 2 of the study (when an album cover was shown along with the playback) and s<sup>1</sup> s<sup>is</sup> the same at the first stage (no album cover shown). Before the correlation analysis we standardize all ratings (liking of songs and album covers, matching of album covers to songs) using Z-score standardization for each participant and each stage of the study individually. 

## 3. RESULTS 

## 3.1 Participants 

A group of 100 participants, living in the United States, active users of music streaming platforms, were recruited through the Prolific<sup>2</sup> platform. The study was conducted in accordance with Prolific guidelines. The participants were made aware of the procedure before the start of the study. 

2 `https://www.prolific.com` 

184 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

Every participant gave an informed consent and was made aware of their ability to withdraw their participation at any moment. The data was collected and stored anonymously. In total 70 participants successfully completed both stages of the study. The mean age of the participants was 40.7 (SD = 13.8) at the time of the study; 43 indicated to be of the sex female and 27 male. The three most used music streaming platforms reported by the participants were: Spotify (n = 42), YouTube Music (n = 30), and Apple Music (n = 16). On average, participants use 1.60.9 different music streaming platforms. 

During the first stage of the study, on average, the participants rated the song snippets 3.5 (SD = 1.8) and the album covers 3.9 (SD = 1.7). The participants indicated familiarity with 3.3 (SD = 6.2) album covers and 4.5 (SD = 7.1) song snippets. After individually filtering the familiar items out and creating individual sets of pairs cover-track, the participants were presented with 34.9 (SD = 7.8) pairs for repeated evaluation of the corresponding music track snippets. 

In the second stage of the study, the participants indicated that on average they were familiar with either the album cover or the track in 3.3 (SD = 6.7) item pairs shown to them. In this stage, participants, again, rated the song snippets on average 3.5 (SD = 1.7) and the matching of the album cover to the song 3.5 (SD = 1.9). After excluding all pairs with familiar items, 31.6 (SD = 11.0) data points (pairs) per participant were available for analysis. 

On average, the participants listened for 13.9 (SD = 2.5) seconds of the song snippets in the first part and for 14.1 (SD = 2.3) seconds in the second part. 

## 3.2 RQ1: Influence of shown album cover 

We investigate the influence of the shown album cover on the listener’s liking of the music track played, by computing individual per-participant Kendall’s τ between the two music track rankings. One – based on their evaluation in the first stage of the study, with no album cover shown. Another – based on the evaluation in the second stage, where along with the previously most liked tracks least appealing album covers were shown and vice versa. We focus on participants who marked at least 10 songs as unfamiliar during the second stage of the study, resulting in 65 participants with 33.8 (SD = 7.8) tracks per participant. 

The distribution of Kendall’s τ over participants is shown in Figure 2 (mean τ = 0.39, SD = 0.25, MIN = −0.32, MAX = 0.74). We observe that, on average, the lists are only moderately correlated. This suggests that, while songs rated higher in stage 1 still tended to be rated higher in stage 2, showing album covers notably affected track ranking. For 44 participants we observe significant (with the p-value threshold 0.05) positive correlation, showing that their liking was more consistent in the presence of album covers. For the remaining 21 participants no significant correlation was detected, highlighting the impact of album covers on their liking. 

Fig. 1 shows the kernel density estimate (KDE) plot of the standard deviation over the positions of each item 

throughout the shuffling process paired with the standardized score given by each user in phase 1 and phase 2. The figure shows the highest density mass at a standard deviation of 2, indicating that the position varies by 2 for most items by shuffling the items of the same score group. 



<!-- Start of picture text -->
3<br>2<br>1<br>0<br>1<br>2<br>3<br>0 2 4 6 8 10<br>SD over position of each item over<br>100 shuffles per user<br>Stand. item score<br><!-- End of picture text -->

Figure 1. KDE plot of standard deviation over position of items in ordered list by rank over 100 random shuffles of item ratings in phase 1 and phase 2. 

Table 1 reports average ranking agreement scores (and the corresponding standard deviations) between the two track rankings: over all participants and separately for participants showing presence/absence of significant Kendall rank correlation. We note that, on average, the two ranked lists share no more than 1 common item in top and bottom 3 (scores of 0.18, 0.26), and less than 5 in top and bottom 10 (scores of 0.44), for participants showing no significant correlation between the two lists (✗). In case of participants showing more consistent rankings (✓), on average their two ranked lists share more than 1 item in top and bottom 3 (0.36, 0.39) and about 6 items in top and bottom 10 (0.58, 0.60). 

Key findings: (a) For 21 out of 65 participants no significant correlation between track rankings with and without an album cover shown detected. This indicates a notable change in track liking, introduced by showing album covers during playback. (b) For the rest, the ranking lists are better aligned. However, notable changes in the tops and bottoms of the lists can be observed, indicating a shift in the overall music track liking, introduced by showing album covers during playback. 



<!-- Start of picture text -->
8<br>6<br>4<br>2<br>0<br>0.2 0.0 0.2 0.4 0.6<br>Kendall's Tau<br>Count<br><!-- End of picture text -->

Figure 2. Distribution of Kendall’s τ over the participants. 

185 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

Table 1. Average ranking agreement in top and bottom k over all participants, between two ranked track lists in stages 1 and 2. 

|Significant||Top||
|---|---|---|---|
|Kendall’s correlation|3|5|10|
|✓/✗|0.310.27|0.370.23|0.530.18|
|✓|0.360.28|0.430.22|0.580.15|
|✗|0.180.23|0.230.20|0.440.21|
|||Bottom||
||3|5|10|
|✓/✗|0.350.27|0.410.23|0.550.16|
|✓|0.390.27|0.450.22|0.600.13|
|✗|0.260.24|0.320.21|0.440.18|



## 3.3 RQ2: Evidence of halo and horn effects 

Answering RQ2, we compute Spearman’s rank correlation between the change in the standardized ratings participants assigned to the tracks in the two stages and the standardized preference score they assigned to the album covers shown with the tracks in stage 2. For this we consider participants who indicated at least 2 pairs as unfamiliar during the second stage of the study, which results in 68 participants and 2,213 data points in total. For the interpretation of the results it is important to remember that the most appealing album covers were shown with the least preferred tracks and vice versa. 

In Figure 3, upper, every point corresponds to a music track, accompanied by an album cover art, shown to a participant in the second stage of the study. The x-axis shows the standardized rating given to the album cover by the participant in the first stage. Higher values show higher appeal of the cover. The y-axis shows the difference in the standardized score, given by the user to the music track between the two stages. Positive values mean that in the second stage, with the album art shown, the track was rated higher than without the album art. Figure 3, lower, follows the same structure, except the x-axis shows the participant’s perception of matching between the album cover and the music track. Higher values correspond to higher perceived matching. 

In Figure 3, upper, we observe that showing higher rated album covers coincides with positive difference in standardized song ratings. This indicates that the songs accompanied by more appealing album covers see a higher increase in the liking score in stage 2. We interpret this finding as an indication of the halo effect. We further note, that showing less appealing album covers is followed by a decline in music track liking in stage 2, indicating the horn effect. Inspecting Figure 3, lower, we note slight positive correlation between the difference in song ratings and the perceived matching of the album cover to the song played. This indicates that the perceived degree of matching between the album cover and the music track can potentially create its own halo (horn) effect. 

Table 2 reports the Spearman’s Rank Correlation between the standardized ratings of the study. In the follow- 



<!-- Start of picture text -->
6<br>4<br>2<br>0<br>2<br>4<br>6<br>2 0 2 4<br>Album cover rating<br>6<br>4<br>2<br>0<br>2<br>4<br>6<br>2 0 2 4<br>Album cover to song matching rating<br>Difference in song ratings<br>Difference in song ratings<br><!-- End of picture text -->

Figure 3. The difference in the standardized song ratings (stage 2 - stage 1) related to the standardized album cover ratings and to the standardized perceived album cover to song matching ratings of the second stage. 

ing we interpret significant correlations at p < 0.01, marked with *. The album ratings of stage 1 (a<sup>1</sup> s<sup>)arenegatively</sup> correlated with the song ratings of stage 1 (s<sup>1</sup> s<sup>),reflecting</sup> our methodology of combining least appealing album covers with most initially liked tracks and vice versa. We observe a positive correlation between the album liking ratings in stage 1 (a<sup>1</sup> s<sup>) and the difference in standardized rat-</sup> ings of the songs (∆ss), which is an additional evidence of the halo and horn effects. The negative correlation between the song ratings of stage 1 (s<sup>1</sup> s<sup>) and the difference in</sup> song ratings in stage 2 (∆ss) indicates the same due to our choice of methodology. The matching rating of the album cover to song snippet (ms) shows a slight positive correlation with the difference in song ratings (∆ss), indicating that the halo (horn) effect is potentially created not only by the appeal of the album cover, but by the overall perceived harmony between the album cover and the music track. 

Key findings: (a) Presence of the halo and horn effects evidenced by significant positive correlation between the album cover appeal and the difference in the track liking. (b) Potential halo (horn) effect created by different degrees of perceived mismatch between the music track and the album cover. 

186 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

Table 2. Spearman’s Rank Correlation between ratings of the first stage of the album cover (a<sup>1</sup> s<sup>),songsnippet</sup> (s<sup>1</sup> s<sup>),differenceinstandardizedsongratings(∆ss),and</sup> standardized matching score between album and song (ms). Significant values are marked with * (p < 0.01). 

||a<sup>1</sup><br>s|s<sup>1</sup><br>s|∆ss|ms|
|---|---|---|---|---|
|a<sup>1</sup><br>s|1.0<sup>∗</sup>|−0.9<sup>∗</sup>|0.4<sup>∗</sup>|−0.0|
|s<sup>1</sup><br>s||1.0<sup>∗</sup>|−0.5<sup>∗</sup>|0.0|
|∆ss|||1.0<sup>∗</sup>|0.2<sup>∗</sup>|
|ms||||1.0<sup>∗</sup>|



## 4. DISCUSSION 

In this study, we investigate the impact of the halo (horn) effect created by contextual media (album covers) on the listener’s liking of the music played. Our findings suggest that such context can notably influence the listeners’ evaluation of music tracks, shaping their subjective experiences. 

One key implication of our results is the importance of contextual framing in music presentation. Album artwork, as shown in this study and, potentially, other context, such as artist reputation, or genre labeling, can substantially affect listeners’ preferences and perceived quality of music. This could be leveraged in domains of music retrieval, recommendation (to increase users’ exposure to new unknown artists through more appealing presentation, to develop more precise context-aware evaluation approaches), and music education (to improve students’ engagement). 

We observe evidence of halo and horn effects in our study. The positive correlation between album cover appeal and the difference in track liking scores indicates that subjectively more appealing covers coincide with higher track evaluations and vice versa. This implies that artists choosing presentation unappealing to their target audience may cause it to undervalue their music. 

Our results hint on the role of perceived album-tosong matching. The positive correlation between the perceived match and rating differences suggests that participants might have adjusted their scores based on how well the album cover fits the track. This introduces an additional contextual factor shaping listeners’ liking of a music track. 

## 5. LIMITATIONS & FUTURE WORK 

In the following we discuss the limitations of the work at hand and outline directions for further research. 

Our results show the influence of the perceived album to track matching on the participants’ evaluation of the music snippet. Further research is needed to validate the presence of the effect. A methodology oriented on creating album-track pairs of various degrees of matching would be required, e.g. taking into account the genre of both the music track and the music actually associated with the album cover. Additionally, in our study, the questions about track liking and album-track matching were placed on the same page, which could cause participants to associate the two. A more distributed study design would help isolate 

this confounding factor. 

The study at hand was conducted with a limited sample of US residents actively using music streaming platforms. Participants in other demographic groups are likely to show different patterns in liking music tracks and its relation to the album art shown. Firstly, people of different cultural backgrounds may have different beauty standards and different ways to process audiovisual information. Secondly, users of streaming platforms may display different levels of response to visual stimuli, such as album art and user interface, compared to people who prefer to listen to music offline. Lastly, the attention listeners pay to album covers may vary with factors beyond demographics, such as personality, music preference or music genre. Therefore, the results of the study at hand cannot be generalized far beyond the investigated user group. Additional research on larger more representative samples is needed to determine more robust patterns. 

Studies show that the halo effect weakens after prolonged interaction with the item in the halo [5,9]. Future work could investigate whether the results change if the participants listen to strictly 5 or 30 seconds of each track, and whether their initial halo-shaped impression lasts beyond the first listening session. 

Finally, it has been shown that the halo effect can manifest to a different extent, depending on the context of the participant, such as mood [25]. Having additional control signal for such context factors would allow to obtain additional insights into halo and horn effects and propose ways of leveraging them in music retrieval and recommendation. 

## 6. CONCLUSION 

The work at hand investigates the halo and the horn effects created by album covers shown to a listener during music playback. In our user study participants were listening to unfamiliar music snippets accompanied by unfamiliar album covers. Based on their individual taste, less appealing album covers were shown while music snippets more aligned with their preference were played (and vice versa). Our results show that introducing album covers to the listening process notably changed individual music track ranking, based on every participant’s liking. We observe a significant correlation between the album cover appeal and improvement in ranking of associated music tracks. We also note that, beyond the appeal of the album cover itself, the perceived matching or mismatching between the cover and the music track can create a halo or horn effect. Our results suggest that evaluation procedures applied to music recommendation and retrieval systems should take into account contextual factors, such as media (album covers) shown in the results lists, as they may influence user liking and, thus, user satisfaction. 

187 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 7. ACKNOWLEDGMENTS 

This research was funded in whole or in part by the Austrian Science Fund (FWF): `https://doi.org/10. 55776/COE12` , `https://doi.org/10.55776/ DFH23` , `https://doi.org/10.55776/P36413` . 

## 8. REFERENCES 

- [1] J. L. Nicolau, J. P. Mellinas, and E. Martín-Fuentes, “The halo effect: A longitudinal approach,” Annals of Tourism Research, vol. 83, p. 102938, 2020. 

- [2] N. Noor, S. Beram, F. K. C. Yuet, K. Gengatharan, and M. S. M. Rasidi, “Bias, halo effect and horn effect: A systematic literature,” International Journal of Academic Research in Business & Social Sciences, vol. 13, no. 3, pp. 1116–1140, 2023. 

- [3] D.-H. Kwak, K. R. Ramamurthy, and D. L. Nazareth, “Beautiful is good and good is reputable: Multipleattribute charity website evaluation and initial perceptions of reputation under the halo effect,” Journal of the Association for Information Systems, vol. 20, no. 11, p. 3, 2019. 

- [4] M. Minge and M. Thüring, “Hedonic and pragmatic halo effects at early stages of user experience,” International Journal of Human-Computer Studies, vol. 109, pp. 13–25, 2018. 

- [5] A. Gulati, M. Martínez-Garcia, D. Fernández, M. A. Lozano, B. Lepri, and N. Oliver, “What is beautiful is still good: the attractiveness halo effect in the era of beauty filters,” Royal Society open science, vol. 11, no. 11, p. 240882, 2024. 

- [6] N. Sahoo, R. Krishnan, G. Duncan, and J. Callan, “Research note—the halo effect in multicomponent ratings and its implications for recommender systems: The case of yahoo! movies,” Information Systems Research, vol. 23, no. 1, pp. 231–246, 2012. 

- [7] G. E. McPherson and E. Schubert, “Measuring performance enhancement in music,” Musical excellence: Strategies and techniques to enhance performance, vol. 4, pp. 61–82, 2004. 

- [8] N. Zoanetti and H. Champion, “Mitigating the halo effect: Managing the wow factor in music performance assessments,” Journal of Research in Music Performance, 2016. 

- [9] C. Adrian and I. Ioana, “The role of visual identity in music perception: a talk with specialists on song likability, perceived quality and emotional reactions,” Kome, vol. 11, no. 1, pp. 110–128, 2023. 

- [10] J. Schaap, M. Berghman, and T. Calkins, “Attractive people make better music? how gender and perceived attractiveness affect the evaluation of electronic dance music artists,” Empirical Studies of the Arts, vol. 41, no. 1, pp. 284–303, 2023. 

- [11] V. T. Le, “Visual metaphors on album covers: An analysis into graphic design’s effectiveness at conveying music genres,” 2020. 

- [12] T. Venkatesan, Q. J. Wang, and C. Spence, “Does the typeface on album cover influence expectations and perception of music?” Psychology of Aesthetics, Creativity, and the Arts, vol. 16, no. 3, p. 487, 2022. 

- [13] Y. Joye and B. M. Fennis, “Set that record straight! cardinal line orientations in music album artwork boost market performance and music consumption,” Psychology & Marketing, vol. 41, no. 4, pp. 916–937, 2024. 

- [14] S. Oramas, F. Barbieri, O. Nieto, and X. Serra, “Multimodal deep learning for music genre classification,” Trans. Int. Soc. Music. Inf. Retr., vol. 1, no. 1, pp. 4– 21, 2018. 

- [15] I. Vatolkin and C. McKay, “Multi-objective investigation of six feature source types for multi-modal music classification,” Trans. Int. Soc. Music. Inf. Retr., vol. 5, no. 1, pp. 1–19, 2022. 

- [16] A. Lehtiniemi and J. Holm, “Easy access to recommendation playlists: selecting music by exploring preview clips in album cover space,” in Proceedings of the 10th International Conference on Mobile and Ubiquitous Multimedia, MUM, 2011, pp. 94–99. 

- [17] Y. Deldjoo, M. Schedl, and P. Knees, “Content-driven music recommendation: Evolution, state of the art, and challenges,” Comput. Sci. Rev., vol. 51, p. 100618, 2024. 

- [18] M. Schedl, O. Lesota, and S. Masoudian, “The importance of cognitive biases in the recommendation ecosystem: Evidence of feature-positive effect, ikea effect, and cultural homophily,” in Proceedings of the 11th Joint Workshop on Interfaces and Human Decision Making for Recommender Systems co-located with 18th ACM Conference on Recommender Systems (RecSys 2024), Hybrid Event, Bari, Italy, October 18, 2024, ser. CEUR Workshop Proceedings, vol. 3815. CEUR-WS.org, 2024, pp. 113–123. 

- [19] I. A. P. Santana, F. Pinhelli, J. Donini, L. G. Catharin, R. B. Mangolin, Y. M. e Gomes da Costa, V. D. Feltrim, and M. A. Domingues, “Music4all: A new music database and its applications,” in 2020 International Conference on Systems, Signals and Image Processing, IWSSIP, 2020, pp. 399–404. 

- [20] M. Moscati, E. Parada-Cabaleiro, Y. Deldjoo, E. Zangerle, and M. Schedl, “Music4all-onion–a large-scale multi-faceted content-centric music recommendation dataset,” in Proceedings of the 31st ACM International Conference on Information & Knowledge Management, 2022, pp. 4339–4343. 

188 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [21] D. Bogdanov, A. Porter, H. Schreiber, J. Urbano, and S. Oramas, “The acousticbrainz genre dataset: Multisource, multi-level, multi-label, and large-scale,” in Proceedings of the 20th International Society for Music Information Retrieval Conference, ISMIR 2019, Delft, The Netherlands, November 4-8, 2019, 2019, pp. 360–367. 

- [22] M. Revilla and J. K. Höhne, “How long do respondents think online surveys should be? new evidence from two online panels in germany,” International Journal of Market Research, vol. 62, no. 5, pp. 538–545, 2020. 

- [23] S. J. Philibotte, S. Spivack, N. H. Spilka, I. Passman, 

and P. Wallisch, “The whole is not different from its parts: music excerpts are representative of songs,” Music Perception: An Interdisciplinary Journal, vol. 40, no. 3, pp. 220–236, 2023. 

- [24] H. Ebbinghaus, “[image] memory: A contribution to experimental psychology,” Annals of neurosciences, vol. 20, no. 4, p. 155, 2013. 

- [25] J. P. Forgas, “She just doesn’t look like a philosopher. . . ? affective influences on the halo effect in impression formation,” European Journal of Social Psychology, vol. 41, no. 7, pp. 812–817, 2011. 

189 

