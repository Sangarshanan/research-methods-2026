---
paper_id: "000063"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706515/files/000063.pdf"
---

# ENHANCING MUSIC RECOMMENDER SYSTEMS WITH MULTIMEDIA CONTENT: A CONTEXT-AWARE APPROACH 

Oleg Lesota<sup>1</sup> Veronica Clavijo<sup>2</sup> Attia Rizwani<sup>2</sup> Markus Schedl<sup>1</sup> Bruce Ferwerda<sup>2</sup> 

1 Institute of Computational Perception, Johannes Kepler University Linz, Linz, Austria 

2 Department of Computer Science and Informatics, Jönköping University, Jönköping, Sweden `oleg.lesota@jku.at, bruce.ferwerda@ju.se` 

## ABSTRACT 

The evolution of the music industry has introduced multimedia elements, such as video, text, and images, into music consumption. However, current Music Recommender Systems (MRSs) remain predominantly audio-focused, requiring explicit user interaction to access additional media. This study explores the integration of multimedia content into MRSs, considering the role of contextual activities and the Uses and Gratifications (U&G) framework in enhancing personalization and engagement. A diary study with 26 participants over one week identified nine key activities, with Household Chores, Workout, and Focusing being the most relevant. These activities revealed novel U&Gs such as “For Preference,” “For Convenience,” “For Discovery,” and “To Get Distracted.” A subsequent user study compared a Basic Music App (audio-only) with a Modified Music App (multimedia-enhanced). Results showed that participants preferred the Modified Music App across five constructs: novelty, ease of use, usefulness, satisfaction, and intention to use. These findings suggest that multimedia-enhanced recommendations can improve user experience by aligning with activity-specific preferences. The study contributes to research on personalized MRSs and offers insights for developing context-aware, multimedia-driven recommendations. 

## 1. INTRODUCTION 

Music, in its simplest form, combines sound, both vocal and instrumental, to create beauty in form or expression [1]. Music permeates our daily lives, accompanying us through our routines and experiences. DeNora [2] emphasizes how music fundamentally influences our moods, shapes our memories, and connects us to the world around. 

The way people consume music has evolved significantly over time. Since the launch of MTV in 1981, which transformed the music industry into a more visual expe- 

© O. Lesota, V. Clavijo, A. Rizwani, M. Schedl and B. Ferwerda. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: O. Lesota, V. Clavijo, A. Rizwani, M. Schedl and B. Ferwerda, “Enhancing Music Recommender Systems with Multimedia Content: A Context-Aware Approach”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

rience [3], music consumption has expanded beyond just listening. Katz [4] highlights how visual elements, such as the Illustrated Song Machine and the rise of stereophony, have enhanced musical experiences. Today, music-related media includes not only audio but also text (e.g., lyrics), video (e.g., official music videos), and images (e.g., album covers) [5,6]. Platforms like Spotify, Amazon Music, and YouTube Music offer users complementary media, including videos and lyrics. However, accessing this media typically requires active interaction, which is not always ideal. 

As the nature of music consumption has shifted, researchers have increasingly sought to understand not only why people listen to music but also how they engage with the broader spectrum of music-related media. The Uses and Gratifications Theory (UGT) has emerged as a prominent framework for exploring these motivations, emphasizing how individuals actively seek media to satisfy specific needs and achieve goals [7]. Lonsdale and North [8] applied UGT to investigate motivations for music listening, including comparisons to other leisure activities and age-related differences. Similarly, Krause and Brown [9] examined music format preferences through the UGT lens, while De la Rosa Herrera & Publiese [10] explored reasons for music consumption among emerging adults. 

Research motivations in this field are diverse, ranging from understanding the role of music in everyday life [8, 11] and examining its impact on human existence [12–17] to exploring its social and psychological functions [18]. Recently, the focus has expanded to include Music Recommender Systems (MRSs), which leverage user preferences to predict and recommend songs [19–22]. The rise of streaming services like Spotify, Apple Music, and YouTube Music has amplified the importance of MRSs in shaping the music consumption experience. 

Despite their widespread use, many MRSs fail to account for contextual factors, such as user activity, which significantly influence music consumption [21–23]. This oversight often results in unsatisfactory recommendations that do not align with the dynamic needs of users. Schedl et al. [22] propose that incorporating contextual aspects could significantly enhance the performance of MRSs, to deliver more relevant and satisfying recommendations. 

Garcia-Gathright et al. [24] found that user satisfaction with MRSs increases when the recommendations align with music taste, meet user needs, and support goal 

547 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

achievement. These latter two functions align closely with UGT, suggesting that effective MRSs should not only recommend music that matches user preferences but also address deeper needs and goals. This alignment highlights the critical role of understanding both user needs and contextual factors in designing next-generation MRSs. 

The intersection of evolving media consumption habits, contextual activities, and the uses and gratifications associated with music-related media presents a unique opportunity to enhance MRSs. By applying the UGT framework, researchers can develop more personalized and contextaware systems. This research aims to explore these dimensions, contributing to the creation of user-centered MRSs that not only align with musical preferences but also address broader media consumption habits and contextual activity needs. Hence, the present study addresses the following research questions: 

RQ1: What are the uses and gratifications for engaging with music-related media (audio, text, video, image) based on the user’s contextual activities? 

RQ2: How does a personalized recommendation of musicrelated media influence user experience when considering diverse uses and gratifications, and contextual activities? 

This study aims to fill the gap in current research by examining the motivations behind engaging with different types of music-related media (e.g., text, video, image) next to solely audio, and understanding how contextual activities influence these choices. Therefore, this study focuses on contextual activities as a critical factor in improving music recommendations. By integrating insights from these areas, this research seeks to provide more accurate and relevant recommendations that enhance user experiences based on real-time activities and media preferences. 

## 2. RELATED WORK 

Research on MRSs has increasingly emphasized the impact of users’ contexts, motivations, and emotional states on music selection. While these systems often rely on data such as play counts, skips, and likes, several studies highlight the influence of situational factors, such as location, activity, or mood, on a user’s immediate listening choices [21, 23, 25–27]. Scholars argue that these contextual cues reflect underlying “gratifications” users seek, an idea originating from UGT. If a system ignores such context, it can misinterpret user behavior and deliver recommendations that lack immediate relevance [22]. 

Although widely used techniques like collaborative and content-based filtering effectively identify patterns in large user populations, they rarely capture the nuances of when and why users listen. For instance, a user’s preference for high-energy music while exercising may get overshadowed if the system only looks at the aggregate listening history and not at the time or location associated with each playback. Studies suggest integrating contextual signals, potentially gathered from user-device interactions or even external sensors, to align recommendations more closely with users’ day-to-day realities [22,24,28]. 

Meanwhile, leading streaming services have begun to expand beyond traditional audio consumption. For instance, Spotify not only streams music but also provides built-in lyrics and official music videos for premium users. Amazon Music leverages its X-Ray feature (adapted from Amazon Video), displaying real-time trivia or text annotations about the current track. YouTube Music allows users to switch between audio and video seamlessly. Despite these added functionalities, platforms generally leave it to listeners to initiate any deeper engagement, such as clicking on the lyrics tab or opting to watch a video. Consequently, the service does not dynamically recommend multimedia formats that might enhance an individual’s specific context or motivation at the moment. 

Researchers studying multiple music-related media formats underscore their potential to satisfy broader user needs. Deldjoo et al. [6] and Afchar et al. [5] show that listeners may watch videos for more immersive experiences, read lyrics for clarity, or browse artwork to appreciate a song’s visual identity. Linking these motivations to UGT’s notion of active media selection could extend the impact of MRSs. By recognizing that a listener might, for instance, prefer soothing instrumentals while studying or an immersive music video when actively browsing content, an MRS could shift from merely suggesting music aligned with their general preference to recommending the combination of formats most relevant in the given context. Incorporating the principles of UGT can help MRSs move beyond simple preference matching, offering more nuanced suggestions that address diverse listening scenarios. 

## 3. METHODS 

To investigate how contextual factors affect music consumption and explore whether contextual, activity-aware recommendations can enhance user experience, this research comprised two complementary studies: a Diary Study and a User Study. The Diary Study examined how individuals’ uses and gratifications (U&G) for musicrelated media align with their day-to-day activities (RQ1). Building on these insights, the User Study evaluated how recommending additional media formats (video, text, or images) based on contextual activities and U&G impacts user experience (RQ2). 

By combining the contextual insights from the Diary Study with an experimental User Study, these methods offer a comprehensive approach to understanding how realtime activities and user motivations can shape recommendations for music-related media<sup>1</sup> . 

## 3.1 Diary Study 

A diary study approach was selected to capture participants’ routines and motivations in situ, thus minimizing recall bias. Each participant completed a diary for seven consecutive days, covering weekdays and weekends. Participants recorded four main items for each music consump- 

> 1 We share the consent forms, participant briefs, administrator scripts and additional analysis in the repository: `https://github.com/ hcai-mms/mrs_context-activity_media` 

548 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

tion episode: (1) date and time, (2) current activity, (3) type of music-related media (audio, video, text, or image), and (4) the reasons for choosing that media. This incidental diary design asked participants to submit entries when they naturally engaged with music-related media, thereby reducing irrelevant or forced data. 

Inclusion criteria specified that participants must consume music-related media daily, use multiple streaming services, and provide written consent for collecting diary entries and demographic details. A short pilot with five participants over three days tested the clarity of instructions and the feasibility of the collection process, leading to minor refinements in question phrasing. 

## 3.1.1 Procedures 

A total of 26 participants (19 female, 7 male) completed the diary study, yielding 185 diary entries. Entry counts per participant ranged from three to fourteen, and three participants extended their participation by two additional days. No participants withdrew or provided unusable data. The diary data served to identify a spectrum of U&G that participants sought in different contexts. Each reported activity was categorized. The final categories were narrowed to four key activities: “Social Gathering,” “Household Chores,” “Workout,” and “Relaxing.” These were grouped into two sets: Group 1 (“Social Gathering,” “Household Chores”) and Group 2 (“Workout,” “Relaxing”) that offer a diverse combination of music-related media recommendations. 

## 3.2 User Study 

Building on the Diary Study results, the User Study investigated whether contextual awareness, paired with additional media recommendations, improves user experience (RQ2). Two music application prototypes were developed: 

- Basic Music App Prototype: A simplified system recommending only audio. 

- Modified Music App Prototype: A system that provides audio plus complementary media (i.e., video, text, or image), guided by the contextual activities and motivations identified in the Diary Study. 

Both prototypes were evaluated through two user experience frameworks: 

- ResQue [29], measuring recommendation accuracy, novelty, ease of use, perceived usefulness, overall satisfaction, and intention to use. 

- UEQ-S (User Experience Questionnaire Short Version) [30], assessing broader usability and user experience attributes. 

To ensure that participants focused on the recommended media formats (rather than song preference), music tracks were selected from Spotify’s trending charts and activity-based playlists. Participants were informed that their task was to assess how each prototype’s recommended content aligned with a given scenario, rather than to evaluate the song recommendations. 

## 3.2.1 Procedures 

A total of 63 participants were recruited, mainly through WhatsApp groups in student accommodations in Jönköping, Sweden, and were offered small incentives (e.g., soda and candy). Each participant underwent two stages: 

1. Basic Music App: Participants chose from the activities in their assigned group (e.g., “Household Chores”), interacted with the prototype (audio only), and then completed both ResQue and UEQ-S questionnaires. 

2. Modified Music App: Participants revisited the same activities, but this time the prototype displayed complementary media (i.e., video, text, or images) selected according to Diary Study insights. They again completed ResQue and UEQ-S. 

Sessions lasted approximately 10 minutes, occasionally extending for further discussion when participants gave notable feedback. Following data collection, four participant entries were removed due to disengaged or repetitive responses, leaving 59 valid data points for analysis. 

## 4. RESULTS 

This section presents findings from two complementary studies. The first part covers the Diary Study, which explores how different day-to-day activities shape participants’ choices of music-related media and the uses and gratifications (U&G) they seek (RQ1). The second part describes the User Study, examining whether contextual, multi-format recommendations improve user experience (RQ2). 

## 4.1 Diary Study Results 

Over a seven-day period, participants recorded episodes of music-related media use, yielding a total of 185 diary entries. We discarded 30 invalid entries for issues such as non-music content or insufficient activity context (e.g., “At a kiosk”). This left 155 valid entries, each describing (1) the activity, (2) the media type(s) used (i.e., only audio or complimentary with video, text, or image), and (3) the motivation behind selecting these media. We categorized the entries using Affinity Diagramming, creating two sets of clusters representing activities and U&G: 

- Activities: Nine distinct themes emerged: Household Chores (25 entries), Workout (25), Focusing (20), Social Gathering (19), Commuting (18), Relaxing (16), Passing the Time (13), Meditating (10), and Driving (9). 

- Uses and Gratifications (U&G): Thirteen categories were identified. The most common included: For Preference (34 entries), As a Background (19), To Pass the Time / Enjoy (13), For Active Interaction (11), and For Discovery (11). Other recurring motivations were For Convenience, To Relax, To Get 

549 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
9:41<br>SORRY<br>Dier yr  rm<br>X 14<br>Activities<br>14 tt<br>14<br>Workout Playlist Housyd Pyist Gathering P<br>Suggested Artists View All Suggested Artists View All Suggested Artists View All<br>Suggested Artists View All<br>+<br>The Weeknd Taylor Swift Alec Benjamin + + The Weeknd Taylor Swift Alec Benjamin<br>+ + The Weeknd Taylor Swift Alec Benjamin<br>The Weeknd Taylor Swift Alec Benjamin<br>Q 回 o 合 Q 回 0o 合 Q 回 0 合 Q 回 0o<br>(a) Only audio (b) Audio + image (c) Audio + lyrics (d) Audio + video<br><!-- End of picture text -->

Figure 1: Interfaces with audio and different music-related media 

Distracted, To Concentrate, To Set the Environment, Playlist Usage, To Match Mood, and To Help Sleep / Fall Asleep. 

## 4.1.1 Statistical Analysis of Media Choice 

To investigate how different activities influenced the choice of media, we transformed the data to indicate presence (1) or absence (0) of audio, video, text, or image in each diary entry. A Multivariate Analysis of Variance (MANOVA) showed a statistically significant effect of activity on these media selections (p < 0.001)<sup>2</sup> . For instance, Driving was associated exclusively with audio in all cases, whereas Passing the Time had a higher proportion of video or text usage, Table 1. 

These results highlight the central role of contextual activity in shaping the media formats users prefer and the gratifications they seek, such as using audio-only content while driving or combining video and text when more engaged or relaxed. 

## 4.2 User Study Results 

The user study (N=63 initially; 59 valid after excluding disengaged responses) examined whether a Modified Music App offering context-based recommendations of musicrelated media improves user experience (RQ2). 

## 4.2.1 User Experience (UEQ-S) Findings 

We measured three dimensions in UEQ-S: pragmatic quality, hedonic quality, and overall user experience. Across all 59 participants, the Modified Music App consistently achieved higher average scores than the Basic Music App, suggesting that providing extra media formats can enrich user engagement. Breaking this down by group: 

> 2 Detailed report can be found in the companion repository 

1. “Social Gathering,” “Household Chores”: Participants reported higher hedonic quality in the Modified App (x¯ = 1.917 vs. x¯ = 1.028), finding it more entertaining and novel—particularly for social contexts or idle chores (x¯ = 2.148 vs. x¯ = 1.509). 

2. “Workout,” “Relaxing”: While participants still favored the Modified App overall, some pointed out that extra media (e.g., lyrics or video) during Workout could be distracting, leading them to wish for better toggling or customization (hedonic: x¯ = 0.836 vs. x¯ = 1.953 and pragmatic: x¯ = 1.609 vs. x¯ = 2.117)). 

Although the Modified App improved overall impression, contextual nuances (e.g., a physically active setting) could affect how much people appreciated the added media. 

## 4.2.2 ResQue Analysis 

We used six constructs from the ResQue framework to evaluate participants’ perceptions regarding: 

1. Accuracy (ACC): How well the app’s recommendations fit users’ expectations. 

2. Novelty (NOV): Whether the app introduced interesting new content. 

3. Perceived Ease of Use (PEU): How simple it was to navigate or interact with the app. 

4. Perceived Usefulness (PU): The extent to which participants felt the recommendations enhanced their experience. 

5. User Satisfaction (US): Overall satisfaction with the system. 

550 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

Table 1: Media formats reported across different activities. 

||Household Chores|Workout|Focusing|Social Gathering|Commuting|Relaxing|Passing the Time|Meditating|Driving|
|---|---|---|---|---|---|---|---|---|---|
|Audio|38.46%|80.77%|70.83%|42.11%|78.95%|52.94%|30.77%|100.00%|100.00%|
|Video|57.69%|15.38%|12.50%|52.63%|15.79%|29.41%|46.15%|0.00%|0.00%|
|Text|0.00%|3.85%|8.33%|5.26%|5.26%|0.00%|15.38%|0.00%|0.00%|
|Image|3.85%|0.00%|8.33%|0.00%|0.00%|17.65%|7.69%|0.00%|0.00%|



Table 2: Paired-Samples T-Test for ResQue Constructs. Negative means indicate preference for the Modified App. 

|Pair|Mean Diff.|SD|t|p (1-sided)|p (2-sided)|
|---|---|---|---|---|---|
|ACC|-0.34|1.060|-2.455|0.009|0.0170|
|NOV|-0.54|0.916|-4.549|<0.001|<0.001|
|PEU|-0.37|0.717|-3.996|<0.001|<0.001|
|PU|-0.51|0.838|-4.660|<0.001|<0.001|
|US|-0.39|0.695|-4.307|<0.001|<0.001|
|IU|-0.49|0.751|-5.025|<0.001|<0.001|



6. Intention to Use (IU): Likelihood of adopting the app in the future. 

Descriptive statistics showed that on average, participants rated the Modified App more favorably on each construct (e.g., higher ACC, higher NOV, etc.). A paired-samples T-test indicated these differences were statistically significant at the 99% level (p < 0.01) for most constructs, with one exception: Accuracy (ACC), which was significant at 95% (p = 0.017). This aligns with the open-ended feedback, where some users felt the added media did not always align with their exact activity or preferences, especially in physically active scenarios (see Table 2). 

related media (audio, text, video, image) depending on their contextual activities (RQ1). The Diary Study led to a list of nine distinct activities among 26 participants. Our analysis showed that audio was consumed most frequently, followed closely by the addition of video, while images were the least used. Statistical testing indicated that activity type significantly influenced media usage patterns, pointing to the importance of contextual factors. 

The Diary Study also produced thirteen different U&G for music-related media consumption. Several of these motivations corresponded to those found in previous music-listening research, including “As a Background” [11, 12], “To Pass the Time / Enjoy” [8, 31], “For Active Interaction” (Lonsdale & North, 2011), “To Relax” [8, 11, 31], and “To Concentrate” [8, 11]. However, additional motivations such as “For Preference,” “For Convenience,” “For Discovery,” and “To Get Distracted” appeared to be more specific to multi-format consumption and are not commonly mentioned in studies of audio-only music listening. This finding suggests that extending beyond audio can elicit new motivations for media usage. 

## 5.2 RQ2: Influence of Personalized, Context-Aware Recommendations 

## 4.2.3 Open-Ended Reflections 

To gain deeper insights, we invited participants to comment on their experiences in free-form responses. Common remarks included: 

- “When I’m with friends, it’s great to have videos. But if I’m alone, I usually just lock the screen.” 

- “For household chores, I don’t need lyrics or images. Audio is enough.” 

- “In the gym, I don’t want to look at text or a video all the time. It can be annoying.” 

- “Relaxing sometimes means turning everything off. But if I’m bored, I’ll watch the video.” 

Several participants indicated a strong desire to toggle or customize the extra media features to fit their immediate situation. While they generally found the Modified App more entertaining or novel, the usefulness of having lyrics, video, or images remained highly context-dependent. 

## 5. DISCUSSION 

## 5.1 RQ1: Uses and Gratifications in Contextual Activities 

This study set out to identify the uses and gratifications (U&G) driving individuals to consume different music- 

The second research question (RQ2) investigated how personalized recommendations of music-related media affect user experience when accounting for diverse U&G and contextual activities. The User Study employed two prototypes: a Basic Music App, which only recommended audio, and a Modified Music App, which incorporated additional formats (i.e., video, text, or images) aligned with the activities identified in the Diary Study. Following established evaluation frameworks, we used the ResQue questionnaire [29] and the short version of the User Experience Questionnaire (UEQ-S; [30]) to gain deeper insights. Results consistently favored the Modified App in terms of both pragmatic (ease of use) and hedonic (enjoyment, novelty) qualities. Nevertheless, participant ratings for Accuracy were statistically significant at a 0.05 confidence level (p = 0.017), not at a 0.01 level, indicating that the perceived alignment between recommended media and user preferences varied slightly. Additionally, perceived ease of use showed the smallest difference between the two prototypes, possibly because both shared the same interface layout, colors, and navigation scheme. 

Open-ended responses illustrated the desire for control over media formats, with participants expressing interest in turning off extra content if it became distracting or did not fit their ongoing activity. These responses reinforce the notion that while additional media can be helpful or 

551 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

entertaining, contextual appropriateness remains vital, and users often want the freedom to choose how much visual or textual content accompanies the audio. 

## 6. CONCLUSION 

This research aimed to enhance MRSs by integrating contextual awareness (e.g., driving, working out, or socializing) and introducing music-related media types beyond audio. The Diary Study revealed the range of day-to-day activities during which media are consumed, along with a set of novel U&G (for instance, “For Preference” and “To Get Distracted”), suggesting that multi-format music services can activate motivations not often observed in audio-only environments. The User Study demonstrated that an MRS prototype aligning with these contextual insights generally fosters higher pragmatic and hedonic quality perceptions. 

Overall, these findings suggest a strong potential for context-aware, multimedia-based recommendations to improve the user experience, provided they remain flexible and allow listeners to control or disable additional media as needed. 

## 7. IMPLICATIONS & LIMITATIONS 

The findings from this study offer guidance for enhancing MRSs by integrating contextual activity awareness [22] and user-centric content selection. Introducing musicrelated media, such as video, text, and images, alongside traditional audio formats appears to deliver a more engaging user experience by addressing varied needs across different activities. This approach could be adapted for other media domains, including podcasts, educational videos, or news, where real-time contextual information shapes user engagement. Music streaming services could gain a competitive edge by incorporating these features, thereby increasing user satisfaction. 

Furthermore, the study broadens the intersection between Uses and Gratifications Theory and Recommender Systems by showcasing how contextual activity and multimedia options affect user preferences. The integration of qualitative insights from diary studies with quantitative measures in a user study highlights the value of hybrid research methods. These methods emphasize the significance of contextual relevance and multimedia flexibility in recommendation algorithms, shifting the focus beyond audio-centric research toward multimedia-enhanced MRSs. The resulting insights support the development of adaptive, activity-aware recommenders that can cater to a wider array of user motivations and behaviors. 

Several limitations should be noted. The sample size and demographic diversity were relatively constrained in both the Diary Study and the User Study. This constraint influenced perceptions of accuracy in the Modified Music App. Specifically, the assumption that users who share similar traits would also share music-related media preferences rested on diary data from only 26 participants, perhaps insufficient for accurately capturing all preference variations. Moreover, the Diary Study sample was skewed 

toward female participants, potentially shaping which activities and gratifications emerged most prominently. Because this phase was explicitly exploratory, we do not claim that these patterns generalize across all listener populations; instead, they highlight promising avenues for follow-up. Recruiting a larger, more demographically balanced cohort, or explicitly testing for gender interactions, will help verify whether these insights hold across diverse groups and ensure equitable applicability of context-aware recommendations. 

In addition, our exclusive focus on contextual activities rather than a broader range of signals (e.g., location, time of day, or device usage) [22] may have omitted other drivers of media-format preferences. Incorporating such passive or lightweight sensing in future work could reveal new motivational factors. Finally, the User Study employed a fixed song set drawn from public playlists rather than personalized content, a decision made for logistical reasons; while our emphasis remained on media-type recommendations, this choice may nevertheless have influenced overall user ratings. 

Finally, time constraints imposed a narrower window for collecting diary entries and recruiting participants for the user study. Longer collection intervals or repeated sessions might capture more nuanced behaviors and yield stronger evidence on whether multimedia-enhanced recommendations maintain their appeal over time. 

## 8. FUTURE RESEARCH 

Further research could investigate the long-term impact of multimedia-enhanced recommendations on user engagement and retention, employing a longitudinal study to determine whether added media elements sustain user satisfaction over extended periods. Examining demographic factors, such as age, gender, or cultural background, would also deepen understanding of how media type preferences vary among different user segments. Finally, investigating different media on a more granular level could help improve recommendation accuracy (for instance one could prefer music videos for browsing along and cover videos for learning a song on an instrument). 

Exploring personalization strategies that consider more granular activity detection, emotional states, time-of-day patterns, or location-based data alongside contextual activities could improve the accuracy and relevance of recommendations. Addressing the constraints noted here, including larger, more diverse samples and prolonged observation periods, would likely yield more generalizable findings. By incorporating these directions, future research can refine the design of context-aware, multimedia-driven MRSs to offer more responsive and gratifying user experiences. 

552 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 9. ETHICAL CONSIDERATIONS 

This student-led study was reviewed and approved at the institutional level by Jönköping University and judged to pose minimal risk under Swedish student-research regulations (no Etikprövningsmyndigheten submission was required). All participants received written information about both the diary-logging and prototype-evaluation phases, and provided informed consent before participation. Data collection and storage procedures ensured anonymity and voluntary withdrawal rights. 

To protect participant welfare and data privacy, we implemented several safeguards throughout both studies. First, informed consent procedures emphasized voluntariness: participants were briefed on their freedom to skip any diary entry or withdraw from the app evaluation without consequences. Second, we anonymized all behavioral and survey data at the point of collection. Hence, no direct identifiers were stored. Third, we conducted a debrief immediately following the app-based evaluation, allowing participants to ask questions and request removal of their data if desired. Although the study involved only non-sensitive information (music-listening behaviors and media-format preferences), these steps ensured transparency and respect for participant autonomy. Finally, in reflecting on future real-world deployments of context-aware recommendations—where adaptive features might leverage signals such as time of day or selfreported activities—we acknowledge the inherent tension between personalization and surveillance. We recommend that any production system include clear opt-in prompts, fine-grained user controls for disabling context-driven features, and a strict policy of data minimization to uphold user agency and privacy. 

## 10. ACKNOWLEDGMENTS 

This research was funded in whole or in part by the Austrian Science Fund (FWF): `https://doi.org/10. 55776/COE12` , `https://doi.org/10.55776/ DFH23` , `https://doi.org/10.55776/P36413` . 

## 11. REFERENCES 

- [1] Epperson and Gordon, “Music | Art Form, Styles, rhythm, History,” 2 2025. [Online]. Available: https://www.britannica.com/art/music 

- [2] T. DeNora, Music in everyday life. Cambridge university press, 2000. 

- [3] T. Doherty, “Mtv and the music video: Promo and product,” Southern Journal of Communication, vol. 52, no. 4, pp. 349–361, 1987. 

- [4] M. Katz, Capturing sound: How technology has changed music. Univ of California Press, 2010. 

- [5] D. Afchar, A. Melchiorre, M. Schedl, R. Hennequin, E. Epure, and M. Moussallam, “Explainability in music recommender systems,” AI Magazine, vol. 43, no. 2, pp. 190–208, 2022. 

- [6] Y. Deldjoo, M. Schedl, P. Cremonesi, G. Pasi et al., “Content-based multimedia recommendation systems: definition and application domains,” in Italian Information Retrieval Workshop, 2018, pp. 1–4. 

- [7] T. Schäfer, P. Sedlmeier, C. Städtler, and D. Huron, “The psychological functions of music listening,” Frontiers in psychology, vol. 4, p. 511, 2013. 

- [8] A. J. Lonsdale and A. C. North, “Why do we listen to music? a uses and gratifications analysis,” British journal of psychology, vol. 102, no. 1, pp. 108–134, 2011. 

- [9] A. E. Krause and S. C. Brown, “A uses and gratifications approach to considering the music formats that people use most often,” Psychology of Music, vol. 49, no. 3, pp. 547–566, 2021. 

- [10] K. De la Rosa Herrera and R. Publiese, “The uses and gratifications of music among emerging adults,” International Journal of Arts & Sciences, vol. 10, no. 1, pp. 351–364, 2017. 

- [11] T. Chamorro-Premuzic and A. Furnham, “Personality and music: Can traits explain how people use music in everyday life?” British journal of psychology, vol. 98, no. 2, pp. 175–185, 2007. 

- [12] D. Boer, R. Fischer, H. G. Tekman, A. Abubakar, J. Njenga, and M. Zenger, “Young people’s topography of musical functions: Personal, social and cultural experiences with music across genders and six societies,” International Journal of Psychology, vol. 47, no. 5, pp. 355–369, 2012. 

- [13] B. Ferwerda and M. Schedl, “Investigating the relationship between diversity in music consumption behavior and cultural dimensions: A cross-country analysis.” in UMAP (Extended Proceedings), 2016. 

- [14] B. Ferwerda, A. Vall, M. Tkalcic, and M. Schedl, “Exploring music diversity needs across countries,” in Proceedings of the 2016 Conference on User Modeling Adaptation and Personalization, 2016, pp. 287–288. 

- [15] T. Hays and V. Minichiello, “The meaning of music in the lives of older people: A qualitative study,” Psychology of music, vol. 33, no. 4, pp. 437–451, 2005. 

- [16] M. Schedl, F. Lemmerich, B. Ferwerda, M. Skowron, and P. Knees, “Indicators of country similarity in terms of music taste, cultural, and socio-economic factors,” in 2017 IEEE International Symposium on Multimedia (ISM). IEEE, 2017, pp. 308–311. 

- [17] M. Skowron, F. Lemmerich, B. Ferwerda, and M. Schedl, “Predicting genre preferences from cultural and socio-economic factors for music retrieval,” in European Conference on Information Retrieval. Springer, 2017, pp. 561–567. 

553 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [18] D. J. Hargreaves and A. C. North, “The functions of music in everyday life: Redefining the social in music psychology,” Psychology of music, vol. 27, no. 1, pp. 71–83, 1999. 

- [19] B. Ferwerda, “Improving the user experience of music recommender systems through personality and cultural information,” Ph.D. dissertation, B. Ferwerda, 2016. 

- [20] B. Ferwerda and M. Schedl, “Enhancing music recommender systems with personality information and emotional states: A proposal.” in Umap workshops, 2014. 

- [21] P. Knees, M. Schedl, B. Ferwerda, and A. Laplante, “User awareness in music recommender systems,” Personalized human-computer interaction, pp. 223–252, 2019. 

- [22] M. Schedl, H. Zamani, C.-W. Chen, Y. Deldjoo, and M. Elahi, “Current challenges and visions in music recommender systems research,” International Journal of Multimedia Information Retrieval, vol. 7, pp. 95–116, 2018. 

- [23] Y. Jin, N. N. Htun, N. Tintarev, and K. Verbert, “Contextplay: Evaluating user control for context-aware music recommendation,” in Proceedings of the 27th ACM conference on user modeling, adaptation and personalization, 2019, pp. 294–302. 

- [24] J. Garcia-Gathright, B. St. Thomas, C. Hosey, Z. Nazari, and F. Diaz, “Understanding and evaluating user satisfaction with music discovery,” in The 41st International ACM SIGIR Conference on Research & Development in Information Retrieval, 2018, pp. 55– 64. 

- [25] Y. Hu and M. Ogihara, “Nextone player: A music recommendation system based on user behavior,” in Proceedings of the 12th International Society for Music Information Retrieval Conference, ISMIR, 2011, pp. 103–108. 

- [26] M. Schedl and A. Flexer, “Putting the user in the center of music information retrieval,” in Proceedings of the 13th International Society for Music Information Retrieval Conference, ISMIR, 2012, pp. 385–390. 

- [27] G. Vigliensoni and I. Fujinaga, “Automatic music recommendation systems: Do demographic, profiling, and contextual features improve their performance?” in Proceedings of the 17th International Society for Music Information Retrieval Conference, ISMIR, 2016, pp. 94–100. 

- [28] B. Ferwerda, “The soundtrack of my life: adjusting emotion of music,” in Proceedings of the 1st workshop collaborating with intelligent machines, Seoul, South Korea, 2015. 

- [29] P. Pu, L. Chen, and R. Hu, “A user-centric evaluation framework for recommender systems,” in Proceedings of the fifth ACM conference on Recommender systems, 2011, pp. 157–164. 

- [30] M. Schrepp, “User experience questionnaire handbook,” All you need to know to apply the UEQ successfully in your project, vol. 10, 2015. 

- [31] A. E. Greasley and A. Lamont, “Exploring engagement with music in everyday life using experience sampling methodology,” Musicae Scientiae, vol. 15, no. 1, pp. 45–71, 2011. 

554 

