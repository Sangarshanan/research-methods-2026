---
paper_id: "000057"
year: 2023
title: "Download pdf"
source_url: "https://zenodo.org/record/10265331/files/000057.pdf"
---

# HOW CONTROL AND TRANSPARENCY FOR USERS COULD IMPROVE ARTIST FAIRNESS IN MUSIC RECOMMENDER SYSTEMS 

## Karlijn Dinnissen 

Utrecht University, The Netherlands `k.dinnissen@uu.nl` 

## Christine Bauer 

Paris Lodron University Salzburg, Austria `christine.bauer@plus.ac.at` 

### ABSTRACT 

As streaming services have become a main channel for music consumption, they significantly impact various stakeholders: users, artists who provide music, and other professionals working in the music industry. Therefore, it is essential to consider all stakeholders’ goals and values when developing and evaluating the music recommender systems integrated into these services. One vital goal is treating artists fairly, thereby giving them a fair chance to have their music recommended and listened to, and subsequently building a fan base. Such artist fairness is often assumed to have a trade-off with user goals such as satisfaction. Using insights from two studies, this work shows the opposite: some goals from different stakeholders are complementary. Our first study, in which we interview music artists, demonstrates that they often see increased transparency and control for users as a means to also improve artist fairness. We expand with a second study asking other music industry professionals about these topics using a questionnaire. Its results indicate that transparency towards users is highly valued and should be increased. 

### 1. INTRODUCTION 

Music is most consumed on streaming services nowadays [1]. These services often have music recommender systems (MRS) integrated to provide personalized recommendations to users. Unfortunately, those systems might disadvantage some artists due to biases in the data, the system, and society. This could lead to unfairness for artists, e.g., through reduced visibility and opportunities [2–5]. 

To mitigate such issues, it is essential to understand and involve the stakeholders affected by MRS, and assess whether we are solving the right problems [6]. However, researchers have rarely directly reached out to these stakeholders inquiring how exactly they are affected, and what they value and desire in these systems. Limited work has been done on the user side, e.g., interviewing users about fairness in recommender systems (RS) in general [7], diversity in MRS [8], and the impact of MRS on listeners [9]. 

> © K. Dinnissen and C. Bauer. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: K. Dinnissen and C. Bauer, “How Control and Transparency for Users Could Improve Artist Fairness in Music Recommender Systems”, in Proc. of the 24th Int. Society for Music Information Retrieval Conf., Milan, Italy, 2023. 

Work considering the artists’ view is equally scarce. Exceptions are two interview-based studies on artists’ perspective on fairness in MRS [10], and on playlists in music streaming services [11]. Moreover, to date, no research consults other music industry professionals. Such indirect stakeholders are often ignored when designing and evaluating systems such as MRS, even though these systems affect them as well [12]. In the case of MRS, some professionals come into direct contact with streaming services and embedded MRS, e.g., when working in a publishing or concert booking role. More indirectly, the success of a professional in an artist’s team depends on that of the artist, which in part depends on streaming services. 

This work focuses on two topics that are not described in existing artist-focused work: (i) transparency for users and (ii) giving more control to users. These topics emerged unprompted in interviews with artists (Study 1), which aimed to understand what artists consider to be fair in music streaming services and embedded MRS, and which role artists envision for music streaming platforms with regard to fairness, diversity, and transparency. While the general results of this study are described in Dinnissen & Bauer [13], in the work at hand, we zoom in on transparency and control for users because artists frequently mentioned these concepts as a means to increase artist fairness. This suggests that—contrary to what is often suggested [14–16]—there is not necessarily a trade-off between user and artist goals; they could even be complementary. Inspired by these insights, we subsequently query industry professionals through a questionnaire (Study 2). 

We address the following research questions (RQs): 

- RQ1: How do (i) artists and (ii) other music industry professionals view the current level of transparency and control for users on music streaming services? 

- RQ2: Which role do artists see for user transparency and control in improving artist fairness? 

- RQ3: What are artists’ user interface (UI) suggestions to improve transparency and control? 

This work offers insight into several perspectives on transparency and control of MRS for users. Artists think both should be increased and give concrete UI suggestions to achieve this. Industry professionals agree that transparency for users should be increased but offer a more nuanced view on control. We emphasize two key points: (i) user and artist goals should not always be viewed as 

482 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

trade-offs, as some can be complementary, and (ii) directly involving a diverse set of stakeholders is essential in music information retrieval (MIR) research and development, to integrate their values and needs adequately. 

### 2. RELATED WORK 

### 2.1 Fairness in Music Recommender Systems 

Fairness in MRS is increasingly receiving attention in the RS and MIR research communities [17, 18], as music streaming services and their integrated MRS significantly influence the music landscape [19]. One challenge here is that fairness is a human judgment value with many definitions and factors at play that do not directly translate into RS evaluation metrics [3]. Hence, research generally focuses on specific, often demographics-based fairness dimension(s) [5], such as nationality (e.g., [20]) and gender (e.g., [4, 21]). Here, a system is generally considered fair on a dimension if it upholds group fairness, a concept in which several groups of people are defined (e.g., based on their nationality), and the system should not give anyone a lesser experience based on their belonging to one group. 

Fairness research in the music domain covers users (i.e., consumers), artists (i.e., item providers), or both simultaneously (for an overview, see [2]). Frequently mentioned issues for artists are popularity bias, a phenomenon where already popular items are recommended more often than others (e.g., [22,23]), and the item cold-start problem, denoting difficulty in accurately recommending new items due to lack of previous interactions (e.g., [24]). These issues particularly affect new or less well-known music acts. For users, goals such as satisfaction are often considered rather than their fairness desires. Still, users indicate that in RS in general, provider fairness is important to them [7]. 

Other stakeholders to consider are platforms offering MRS [25,26], music labels [27], and other music industry professionals who come into contact with or are impacted by music streaming services (e.g., concert bookers, artist managers, event producers). To the best of our knowledge, no work directly addresses the latter stakeholder group’s view on how their values should be integrated into MRS. 

### 2.2 Transparency for Users 

Like fairness, RS transparency is increasingly valued by users and item providers alike [10,28], with its societal relevance resulting in EU-wide legislation [29]. Transparency is often offered through interpretable or explainable RS, which can educate users on inner RS workings [7,30]. To properly gauge RS fairness, transparency is considered a prerequisite. In Sonboli et al. [7], users indicate desiring insight into the fairness goals of organizations that offer RS. Ferwerda et al. [31] show that MRS users were more satisfied if they perceived a playlist as fair (here, focusing on artist popularity), even if they could not identify which playlist was more fair according to objective measures. 

Insight into the inner workings of MRS, and therein considered fairness dimensions, could be offered on multiple levels and with different amounts of detail [30,32]. On 

the broadest level, music streaming services could share relevant business rules. On an abstract RS model level, global explanations can show overall tendencies on different dimensions (including fairness) [33]. Local model explanations are also possible, e.g., on the level of specific songs, artists, or playlists [33–35]. Different user personalities and cognition needs should be considered here [36], ideally allowing users to choose the type of explanations [7]. When promoting lesser-known artists, persuasive explanations might increase how users rate their recommendations [16]. However, users indicate they do not want to be (unintentionally) manipulated through explanations, even in a fairness context [7]. Finally, visualizations might also bring model logic to light [32], though textual explanations might be more effective in the MRS domain [34]. Yet, such transparency-enhancing functionality has rarely been implemented into user-facing parts of music streaming services, especially on the model level. 

### 2.3 Giving Users Control 

User control is considered an essential quality of an effective RS, as it positively affects user trust and satisfaction [28]. While transparency can provide insight into fairness, control gives users the agency to change their recommendations based on their values and goals, which could include fairness. Users indicate they want to choose whether they want more personalized recommendations that might be less fair for item providers, or less personalized in favor of fairness [7]. In the music domain specifically, research on user control often aims at exploration, discovery, or diversification tasks (e.g., [8, 32, 37–41]), with no works to date focusing on fairness. Still, if users’ listening behavior becomes more diverse (i.e., they start engaging with a broader range of music items), this could also contribute to artist fairness if that range includes less popular or historically underrepresented artists [15,42]. 

Like transparency, user control can be implemented on different system levels in a MRS. Literature differentiates between low-level control on recommendation data level (playlist, play and like buttons, rating), middle-level control on user profile level (e.g., with tags or sliders), and high-level control on algorithm parameter level [32]. When enabling such functionality, the extent to which a user can take control should be personalized to keep cognitive load and complexity at an acceptable level [32,37]. 

Even though research demonstrates how users can be given control and how this contributes to recommendation acceptance and user satisfaction, in practice, users typically have little control in widely used MRS. Essentially, RS providers are in the main position to control the system, and with it, the items recommended [43,44]. In the music industry, some item suppliers (e.g., major labels) may be in a strong position to shift the control to their side [43]. 

### 3. METHODS 

We employed two studies: Study 1 with artists and Study 2 with other music industry professionals. Here, we describe 

483 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

|Code|Age|Gender|Audience<br>reach|Genre|
|---|---|---|---|---|
|P1|26–35|Male|Local|Hip-Hop|
|P2|26–35|Male|National|Rock/Pop|
|P3|26–35|Male|Local|Rock/Punk/Metal|
|P4a,b|26–35|Male|Local (a)|Hardcore/Rock/Blues|
||||National,<br>Local (b)|(a), Indie/Metal (b)|
|P5|26–35|Male|Internat.|Dance|
|P6|18–25|Non-binary|Local|Pop|
|P7a,b|46–55|Female (a),<br>Male (b)|National|Alt. Pop|
|P8a,b|56–65|Female|N/A|Folk/World|
|P9|18–25|Non-binary|Local|Rock/Pop/Folk|
|P10|26–35|Male|Local|Neoclassical|
|P11|36–45|Female|Local|80’s Alt. Synthpop|
|P12|18–25|Female|Local|Metal|
|P13|26–35|Female|(Inter)nat.|Indie-pop Alt.|
|P14|36–45|Male|National|Many|



Table 1. Study 1 self-reported participant information. 

both studies’ methods and outline our analysis approach. 

### 3.1 Study 1: Interviews with Artists 

We conducted 14 interviews with currently active music artists in the Netherlands from January to March 2022. We reached out to new participants until we reached a high level of thematic saturation [45]. For music groups, we offered the opportunity to join the interview with two members. This resulted in 3 interviews with two members and 11 interviews with individual artists (Table 1). 

The research setup was based on the one used by [10], starting with a metadata questionnaire and a short presentation about MRS. Then, we conducted a semi-structured interview (52 minutes on average). Questions, outlined in detail in Dinnissen & Bauer [13], covered a broad range of topics: transparency for artists, artist control over recommendations, reaching an audience, popularity bias, diversity, gender balance, influencing users’ behavior, localization, repertoire size, royalty distribution, and impact of the COVID-19 pandemic. By using open questions, we encouraged an open conversation rather than a predefined one, leaving space for artists to add insights. 

We recorded, transcribed, and pseudonymized the audio of the interviews. We used a Qualitative Content Analysis [46] for which we based the annotation scheme on the codes used in [10] (deductive) and then adapted the codes based on the interview content (inductive). Three annotators coded the transcripts, with two inter-annotator sessions indicating a high level of inter-annotator agreement. In the work at hand, we focus on the interview parts related to transparency and control for users. Therefore, we analyze results under respective codes ‘Transparency’ (top-level)—‘Towards user’, and ‘Control’ (top-level)— ‘For users’. As mentioned in Section 1, neither topic was explicitly addressed in the questions. Both organically came up when discussing experiences and fairness. 

### 3.2 Study 2: Questionnaires 

To reach a considerable sample of music industry professionals, we used questionnaires as our data collection ap- 

proach in Study 2.<sup>1</sup> We collected 35 responses, all filled in on tablets, from attendees at Eurosonic Noorderslag, a major European conference for music industry professionals held in January 2023.<sup>2</sup> 12 participants identified as women, 22 as men, and 1 participant refrained from stating their gender. Participants were from 7 European countries. When asked about their current professional role(s), participants indicated education (10), technology (7), event production (6), bookings (5), research/science (4), marketing/PR (4), artist (3), legal/policy (3), artist representation (2), and other (7). 11 participants indicated more than one role, and ‘artist’ was not the sole role for any participant. 

In the questionnaire, we address the wide variety of topics from Study 1, this time from several points of view (i.e., artist, MRS user, and participants’ own as an industry professional). For this work, again, we focus on the questions that relate to transparency and control for users (see Table 2). We used a 5-point Likert-scale answering format and also offered the options to indicate ‘Don’t know / prefer not to answer’, skip a question if desired, and add comments. For the topics at hand, no comments were added. As one participant skipped all four questions on these topics, we present results for 34 participants. 

### 4. RESULTS AND DISCUSSION 

We outline the results of our studies going from our research questions. Insights from both Study 1 and Study 2 are used to answer RQ1, whereas RQ2 and RQ3 zoom in further on the results of Study 1. 

### 4.1 RQ1: Transparency & Control for Users 

For RQ1, we present insights from artists and other music industry professionals about current transparency and control for users within music streaming services. 

Transparency—Artist view. All participants indicated using music streaming services both as a consumer and artist, distinguishing clearly between those two roles in their answers. In some cases, their views as an artist were similar to those from a user perspective. On transparency, they remarked that MRS deployed in streaming services are opaque to both artists and users. Here, we focus on the latter, which came up in several interviews despite no question being dedicated to this point of view. Opaqueness of MRS towards users was often stated as a fact: “As a user [...] you really have no idea what is recommended to you. You are kind of cool with all of it because they do a pretty good job, those algorithms.” (P6) 

Artists called for more transparency on especially fairness objectives and diversity in recommendations. Some also noted that if users lack insight into MRS, they have no way of knowing whether and how their taste is being influenced: “It would be proper for a platform to show how it works, and that you as a listener would also... know? [...] As I think it influences [...] our listening behavior—which is not necessarily our taste—a lot.” (P13) 

> 1 Study 2 materials can be accessed at [47]. 

> 2 `https://esns.nl/en/` 

484 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

Transparency—Music industry professional view. From Study 2, we show results for 34 industry professionals for the two questions dedicated to user transparency (Table 2, Q1+2). Responses on whether personalized MRS are transparent to users were spread (SD = 1.37), with 32% of participants somewhat agreeing, but also 26% of participants strongly disagreeing. Participants tend toward a negative view (Mean = 2.79) on current transparency towards users, displaying similar tendencies as artists. 

A stronger consensus can be found on whether personalized MRS should be made more transparent. Here, no participants opted for (slightly) disagree; only one participant chose the neutral option, and the other participants either somewhat agreed (56%) or strongly agreed (41%). This shows a clear, almost unanimous call for more transparency of MRS, mirroring this call from artists in Study 1. 

Discussion. From these results, we deduce that both stakeholder groups highly value transparency for users in MRS, think it is currently lacking, and desire improvement. All in all, artists mainly focus on system-level information (versus, e.g., song-level), which could be shared through global explanations [34]. As in Sonboli et al. [7], artists mention an educational component, noting users do not know how MRS work, which objectives are incorporated, and how MRS influence their listening behavior. 

Control—Artist view. In Study 1, the topic of control for users frequently surfaced when artists discussed their own experiences as streaming service users: being unhappy with their recommendations, and having no options to modify them: “Truly every week [certain act] is added to my Release Radar, every week I dislike it, I disliked [their profile], and it still appears every week. How?” (P2) 

“You start [on YouTube] with a very small band, and eventually you always end up, let’s say, at... Metallica, at Rock Im Park, you know. So I never find that useful.” (P3) 

Increased user control was not only mentioned as a solution to such problems, but also as a means to generally improve MRS by allowing users to provide more information on their preferences: “I know plenty of people who really enjoy listening to the same music all the time and especially don’t want to hear anything new. [...] If they’d solely be presented with a lot of different styles, they’d probably think: ‘that’s it, I’ll go somewhere else, this is too much for me’. So it would be very cool if you could indicate [yourself], from zero to ten, ‘I am very experimental’.” (P4a) 

Nevertheless, some artists viewed actively searching for specific music on streaming services as effectively also ‘taking control’: “If I want to listen to super obscure HipHop or something, then there are [play]lists for that. You do need to know those exist [...], but they contain all kinds of new things I didn’t know about before.” (P1) 

P2 did note that not all users know how to find such lists or want to put in such effort: “I feel like people very often simply listen to what they are told. [...] 30 years ago, radio dictated what people could listen to in the car, so people just listened to that, and now Spotify is doing it.” (P2) 

Control—Music industry professional view. Resulting from Study 2, we show responses from 34 participants 

in Table 2 (Q3+4). Contrary to artists, industry professionals were less unanimously negative about the current extent to which users can control their recommendations in MRS. Regarding users’ influence on general recommendations, participants were divided on the topic, with 38% indicating being somewhat or strongly dissatisfied, and 41% indicating they were somewhat or strongly satisfied. 

On the extent to which users can influence their personal playlists, participants responded slightly more positively (Mean = 3.38), with 29% indicating they were somewhat or strongly dissatisfied, and 56% indicating they were somewhat or strongly satisfied. Overall, dissatisfaction with current user control seems less pronounced in this stakeholder group than for artists. 

Discussion. Artists expressed dissatisfaction with current control over recommendations, as well as the lack of agency for users to change them. Some works (e.g., [44]) suggest that streaming services’ business interests are a possible reason for limited control. Still, the added value artists see for increased control aligns with frequently discussed user goals, such as exploration [37,39,41] and discovery [32]. The industry professionals’ view was more nuanced, with about half of the participants being satisfied with the extent to which users can currently control MRS. 

### 4.2 RQ2: Role of Transparency & Control in Improving Artist Fairness 

For RQ2, we focus on why artist fairness could be improved by increasing transparency and control for users, according to our participants. As this emphasis was initiated by participants from Study 1 but out of scope for Study 2, we focus on insights from Study 1. 

Artists mainly mentioned transparency towards users in the context of algorithmically generated and ‘curated’ (i.e., created by an editor) playlists. These could be created with specific fairness goals in mind, which should be clearly communicated to the user. Such playlists could counter biases in MRS by presenting the user with more diverse music, e.g., highlighting music from (historically) underrepresented artists. P7b mentioned this could also be a way to highlight older repertoire, and P9 noted: “An older album can, of course, still be new to someone.” (P9) 

However, P8a+b and P13 remarked that solely offering playlists with a designated fairness goal would not bring any lasting shift in user behavior: “If you put all [women] in one list, then it is a list again. Then it effectively becomes some kind of subgenre, while gender actually transcends genre, and... it should not be an issue at all anyway.” (P13) 

A second suggestion was giving insight into all current playlists regarding certain ratios such as artist gender or ethnicity. With such insights, users could be made more aware of current inequalities, and make more informed and fairer decisions based on their own values: “I think it is important for creators that users know what they are choosing. [...] Such transparency is missing completely. So I think it would be better if [streaming services] were transparent, like: all [play]lists contain this many women, this many men, this many black people, this many white peo- 

485 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

|No.|Question|Min|Max|Median|Mean|SD|
|---|---|---|---|---|---|---|
|Q1|For users of streaming services, I feel like it is clear for which reason(s) specific music is rec-<br>ommended to them.|1|5|3|2.79|1.37|
|Q2|For users of streaming services, I feel like it is important to make it more clear for which<br>reason(s) specific music is recommended to them.|3|5|4|4.38|0.54|
|Q3|For users of streaming services, I am happy with the extent to which they can influence which<br>music is in their general recommendations.|1|5|3|3|1.26|
|Q4|For users of streaming services, I am happy with the extent to which they can influence which<br>music is in their personalized playlists.|1|5|4|3.38|1.19|



Table 2. Questionnaire responses (1 = ‘Strongly disagree’, 5 = ‘Strongly agree’). 

ple, this many... and they would do this for all lists. End of story. And all of them would do it.” (P8a) 

Other than more transparency, giving users more control over their recommendations was also suggested as a way to address unfairness issues. When discussing popularity bias and cold start problems, several participants suggested letting users manually adapt their playlists or general recommendations. Users could then, e.g., indicate they want to receive more songs that they have not listened to before: “Ideally, I would like to see not one band name I already know. As a small artist, I would appreciate that a lot as well, as it would make chances a little higher you’d maybe be recommended for once.” (P3) 

Alternatively, users could indicate their preferred level of adventurousness: “Maybe it would be nice to make a specific setting for [more music outside of usual taste], ‘I feel adventurous’ or something like that.” (P6) 

As a final insight, we note that most artists desired stronger measures, such as actively making playlists more diverse or balanced. P8a remarked that if users are given the choice, only those who already wish to contribute to a balanced and diverse music landscape would use such functionality: “[Recommending more diverse music] should just be a standard, [...] because else, it just won’t happen. Because that’s not the way people are. We are herd animals! We do what we know! And we also do what we know if we say: ‘I want to discover something new’. [...] It is a choice you think suits you. [...] So if you offer it as a choice, you will keep fishing in the same pond.” (P8a) 

P13 also suggests offering more balanced playlists to start with: “[I would prefer] a playlist which contains a certain number—that it is more balanced.” (P13) 

P5 remarked this could be achieved while taking user type (e.g., inclination towards diverse music) into account, and adapting recommendations based on that: “So it might start with... 30, 33%, and if it is a hit, the percentage becomes higher, and if [the more diverse songs are] skipped, it becomes lower... something like that.” (P5) 

Discussion. Artists identified a connection between transparency for users and artist fairness. They indicated that users need insight into how MRS work to make informed decisions matching their fairness needs, which literature suggests could benefit artist fairness [7, 31]. Even though persuasive explanations might increase users’ satisfaction with lesser-known artist recommendations [16], we note that such persuasion is not necessarily appreciated [7]. Artists especially emphasized insight into platform fair- 

ness goals (confirming results for RS in general [7]), and fairness metrics within playlists. To some extent, playlist channels intended to address fairness are currently offered: e.g., Spotify’s EQUAL [48] and Deezer’s Women’s Impact [49] initiatives both aim to combat gender disparity, while other curated playlists are dedicated to a certain niche, e.g., Tidal’s Diversity & Tradition: New Black Americana [50]. However, while dedicating playlists to an underrepresented group addresses the overall fairness issue, each standalone playlist is not necessarily a fair one, as it features only one group. Lastly, we note that collecting data on, or giving users insights into, sensitive attributes such as gender and ethnicity, is a debated topic [51]. 

Concerning giving users more control, artists noted it would help increase fairness on certain aspects if desired. This corresponds to previous findings [7], where users expressed their wish to adapt personalized RS on diversity aspects. Control over diversity in MRS could also contribute to artist fairness if less popular or (historically) underrepresented artists are recommended as a result [15,42]. Still, some artists believed that increased control alone would not make a significant impact, as they expected that only users whose listening behavior is already diverse would increase their playlists’ diversity. 

### 4.3 RQ3: UI Suggestions 

For RQ3, we cover concrete ideas for implementing transparency- and control-enhancing UI functionalities, as brought up in Study 1. These came up when discussing (desired) artist fairness improvements, and integrating those in a manner that users would perceive positively. Ideas focused on influencing either MRS in general, or specific streaming service pages (e.g., playlists). 

Artists mentioned some approaches to increase transparency and agency for users simultaneously. Those could be implemented on: (1) a user profile page, where users can modify their general recommendations, and (2) specific playlists so that users could modify recommendations within each playlist. For example, P6 and P11 mentioned sliders to adapt, e.g., how many new artists versus established artists should be recommended, or whether songs should be new to the user: “Perhaps just a percentage, a slider, saying how many recommended songs you’d know already, and how many you wouldn’t know, which you could adjust according to which mood you’re in.” (P6) 

P7a+b and P11 suggested adding tags or filters so that 

486 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

users could indicate what they want to be recommended, e.g., only songs from a specific genre or region: “As if you are logging in from France, for example.” (P7b) 

Lastly, P10 mentioned addressing users through a prompt suggesting to increase the listener-artist connection. This could be achieved by proposing that the user visits the profile of artists they often listen to but have not yet looked up. Prompts could also suggest trying something more adventurous: “Let’s say someone is listening to the same things constantly, after one week you could also say: ‘hey, [user], is it time for something else?’ [...] And then you could indicate: ‘nah, I don’t really feel like it, go back to what I was listening to, let’s just play The Beatles and The Rolling Stones again’... Or you like it.” (P10) 

Discussion. Our results offer a first insight into transparency- and control-increasing design for MRS, from the artist’s perspective. As a whole, artists focused on control in their answers rather than on transparencyincreasing design or explanations. They mainly focused on mid-level controls on user profiles, playlists, or through prompts, rather than low- and high-level controls [32]. These responses correspond to previous research (e.g., sliders [32,37–39] and tags [32]) but had not yet been noted in an artist fairness context. From the user perspective, such controls could help influence MRS to better fit the current user goals and mindset (i.e., focused, open, or exploratory) [52]. In Sonboli et al. [7], users emphasize the importance of design practices to promote fair treatment. From the streaming services’ side, new functionality by YouTube Music might address the need for more control by allowing users to customize radio channels, e.g., by indicating what percentage of songs should be new to the user [53]. Deezer has also introduced a ‘Country Selector’ allowing users to switch the ‘home country’ on which their music and shows recommendations are based [54]. Regarding transparency, Spotify recently introduced an AIgenerated ‘DJ’ feature offering personalized playlists with item-based explanations [55]. Further new functionalities and redesign should be extensively researched and tested to minimize user change aversion [56], and to verify whether they correspond with other stakeholder values. 

### 5. CONCLUSION 

### 5.1 Insights for the MIR Community and Beyond 

Our work contributes insights into artists’ and music industry professionals’ perspectives on MRS transparency towards users. Our results suggest neither stakeholder is positive about the current transparency, despite its importance in MIR systems [18]. “Transparency can serve to empower artists and listeners to challenge AI systems” [18]. In the literature, there is a strong agreement that transparency is fundamental for MIR [5, 17, 18] and MRS specifically [10, 36], which is supported by our findings. Our results also show that the transparency towards users is considered insufficient and requires improvement. 

Regarding control, artists indicate clearly that they desire increased user control over MRS, deeming the current 

level insufficient. They argue that the combination of transparency toward users and giving them control will, in turn, help increase fairness for artists, which is a novel and complementary view going beyond existing work. By contrast, music industry professionals are interestingly divided on this matter, for which the cause is yet to be explored. 

On a broader level, we learn that there is not necessarily a trade-off between user, item provider, and industry goals (as extensively discussed in multi-stakeholder systems research): indeed, there is some overlap. In our work’s context, users, artists, and other music industry professionals essentially want the same (i.e., more transparency and control for users) for similar reasons (i.e., better artist fairness and more recommendation diversity), though our study does not deliver insights concerning industry professionals’ reasoning. Hence, it is imperative that MIR involves different stakeholders to understand better what the various actors need and value, and integrates those needs and values in MRS. While trade-offs will keep existing, we need to delve into, and focus on, overlaps and joint goals. 

Our work also contributes UI suggestions addressing control and transparency. We note that making only userfacing design changes is insufficient; they should be supported by MIR measures (e.g., data enhancement for retrieval and filtering, fair ranking). We emphasize the significance of combining algorithms and UI research alike. 

Concluding, in MIR research, we need to support artists better. Taking a multi-stakeholder approach will accelerate this because some goals and needs are complementary. Essentially, supporting users (in transparency and control) can help artists (in terms of fairness). 

### 5.2 Limitations and Future Work 

One constraint of this work is that we aim for exploration with our sample and therefore do not offer an exhaustive, generalizable overview. In future work, both studies could be extended with participants from different cultural, musical, and professional backgrounds to paint a more generalizable overall picture. The perspectives of streaming service providers and other additional stakeholders could also be further addressed. Additionally, as we did not explicitly address transparency and control for users in Study 1, we might have missed views from participants where those topics did not come up. Still, this ensures that responses were spontaneous and unprompted. Lastly, Study 2 mostly contained closed questions that did not allow in-depth analysis, though participants had the possibility to add remarks in the optional free text fields. 

A promising future direction is to implement the suggested UI functionalities in a music streaming service, and compare user behavior to that in a system without such functionalities. It would be especially worthwhile to conduct user studies evaluating those functionalities with various stakeholder groups and measure differences in perceived transparency, control, and fairness of such a system. Such a study should cover what RS should deliver if a user indicates not wanting fair recommendations, and how to personalize any fairness-aimed explanations to user needs. 

487 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

### 6. ACKNOWLEDGEMENTS 

We thank all participating artists and music industry professionals for sharing their invaluable insights. We also express our gratitude to all who supported us in recruiting participants, and especially to Marloes Vredenborg and Isabella Saccardi, both of whom helped conduct Study 2. 

### 7. REFERENCES 

- [1] IFPI, “Global music report 2023: State of the industry,” London, UK, 2023. [Online]. Available: https: //www.ifpi.org/wp-content/uploads/2023/03/Global_ Music_Report_2023_State_of_the_Industry.pdf 

- [2] K. Dinnissen and C. Bauer, “Fairness in music recommender systems: a stakeholder-centered mini review,” Frontiers in Big Data, vol. 5, 2022. [Online]. Available: https://doi.org/10.3389/fdata.2022.913608 

- [3] M. D. Ekstrand, A. Das, R. Burke, and F. Diaz, “Fairness in information access systems,” Foundations and Trends<sup>®</sup> in Information Retrieval, vol. 16, no. 1–2, 2022. [Online]. Available: https://doi.org/10. 1561/1500000079 

- [4] A. Ferraro, X. Serra, and C. Bauer, “Break the loop: Gender imbalance in music recommenders,” in Proceedings of the 2021 Conference on Human Information Interaction and Retrieval, ser. CHIIR ’21. New York, NY, USA: ACM, 2021, pp. 249–254. 

- [5] C. Bauer, “Allowing for equal opportunities for artists in music recommendation,” in Proceedings of the 1st Workshop on Designing Human-Centric Music Information Research Systems, ser. wsHCMIR ’19, Delft, The Netherlands, 2019, pp. 16–18. [Online]. Available: http://arxiv.org/abs/1911.05395 

- [6] ——, “Report on the ISMIR 2020 special session: How do we help artists?” ACM SIGIR Forum, vol. 54, no. 2, 2020. [Online]. Available: https: //doi.org/10.1145/3483382.3483398 

- [7] N. Sonboli, J. J. Smith, F. Cabral Berenfus, R. Burke, and C. Fiesler, “Fairness and transparency in recommendation: The users’ perspective,” in Proceedings of the 29th ACM Conference on User Modeling, Adaptation and Personalization, ser. UMAP ’21. New York, NY, USA: ACM, 2021, pp. 274–279. [Online]. Available: https://doi.org/10.1145/3450613.3456835 

- [8] K. Robinson, D. Brown, and M. Schedl, “User insights on diversity in music recommendation lists,” in Proceedings of the 21st International Society for Music Information Retrieval Conference, ser. ISMIR ’20. ISMIR, Oct. 2020, pp. 446–453. [Online]. Available: https://doi.org/10.5281/zenodo.4245464 

- [9] J. H. Lee, L. Pritchard, and C. Hubbles, “Can we listen to it together? Factors influencing reception of music recommendations and post-recommendation 

behavior,” in Proceedings of the 20th International Society for Music Information Retrieval Conference, ser. ISMIR ’19. ISMIR, Nov. 2019, pp. 663–669. [Online]. Available: https://doi.org/10.5281/zenodo. 3527896 

- [10] A. Ferraro, X. Serra, and C. Bauer, “What is fair? Exploring the artists’ perspective on the fairness of music streaming platforms,” in HumanComputer Interaction – INTERACT 2021: 18th IFIP TC 13 International Conference, ser. INTERACT ’21, vol. 12933. Cham, Germany: Springer, 2021, pp. 562–584. [Online]. Available: https: /doi.org/10.1007/978-3-030-85616-8_33 

- [11] I. Siles, A. Ross Arguedas, M. Sancho, and R. Solís-Quesada, “Playing spotify’s game: artists’ approaches to playlisting in latin america,” Journal of Cultural Economy, 2022. [Online]. Available: https://doi.org/10.1080/17530350.2022.2058061 

- [12] B. Friedman, P. H. Kahn, A. Borning, and A. Huldtgren, Value Sensitive Design and Information Systems. Dordrecht: Springer Netherlands, 2013, pp. 55–95. [Online]. Available: https://doi.org/10.1007/978-94-007-7844-3_4 

- [13] K. Dinnissen and C. Bauer, “Amplifying artists’ voices: Item provider perspectives on influence and fairness of music streaming platforms,” in Proceedings of the 31st ACM Conference on User Modeling, Adaptation and Personalization, ser. UMAP ’23. New York, NY, USA: ACM, 2023, pp. 238–249. [Online]. Available: https://doi.org/10.1145/3565472.3592960 

- [14] E. Bugliarello, R. Mehrotra, J. Kirk, and M. Lalmas, “Mostra: A flexible balancing framework to tradeoff user, artist and platform objectives for music sequencing,” in Proceedings of the ACM Web Conference 2022, ser. WWW ’22. New York, NY, USA: ACM, 2022, p. 2936–2945. [Online]. Available: https://doi.org/10.1145/3485447.3512014 

- [15] R. Mehrotra, J. McInerney, H. Bouchard, M. Lalmas, and F. Diaz, “Towards a fair marketplace: Counterfactual evaluation of the trade-off between relevance, fairness & satisfaction in recommendation systems,” in Proceedings of the 27th ACM International Conference on Information and Knowledge Management, ser. CIKM ’18. New York, NY, USA: ACM, 2018, pp. 2243–2251. [Online]. Available: https://doi.org/10.1145/3269206.3272027 

- [16] S. M. Mousavifar and J. Vassileva, “Investigating the efficacy of persuasive strategies on promoting fair recommendations,” in Persuasive Technology, ser. PERSUASIVE ’22. Cham, Germany: Springer International Publishing, 2022, pp. 120–133. [Online]. Available: https://doi.org/10.1007/978-3-030-98438-0_10 

- [17] A. Holzapfel, B. Sturm, and M. Coeckelbergh, “Ethical dimensions of music information retrieval 

488 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

   - technology,” Transactions of the International Society for Music Information Retrieval, vol. 1, no. 1, pp. 44–55, Sep 2018. [Online]. Available: https: //doi.org/10.5334/tismir.13 

- [18] B. L. T. Sturm, M. Iglesias, O. Ben-Tal, M. Miron, and E. Gómez, “Artificial intelligence and music: Open questions of copyright law and engineering praxis,” Arts, vol. 8, no. 3, 2019. [Online]. Available: https://www.mdpi.com/2076-0752/8/3/115 

- [19] P. Tschmuck, The Economics of Music, 2nd ed. Newcastle upon Tyne, UK: Agenda Publishing, 2021. [Online]. Available: https://doi.org/10.2307/j. ctv1wgvb9x 

- [20] C. Bauer and M. Schedl, “On the importance of considering country-specific aspects on the onlinemarket: an example of music recommendation considering country-specific mainstream,” in 51st Hawaii International Conference on System Sciences, ser. HICSS ’18, 2018, pp. 3647–3656. [Online]. Available: https://doi.org/10.24251/HICSS.2018.461 

- [21] A. Epps-Darling, R. Takeo Bouyer, and H. Cramer, “Artist gender representation in music streaming,” in Proceedings of the 21st International Society for Music Information Retrieval Conference, ser. ISMIR ’20. ISMIR, Oct. 2020, pp. 248–254. [Online]. Available: https://doi.org/10.5281/zenodo.4245416 

- [22] K. Lee and K. Lee, “My head is your tail: Applying link analysis on long-tailed music listening behavior for music recommendation,” in Proceedings of the Fifth ACM Conference on Recommender Systems, ser. RecSys ’11. New York, NY, USA: ACM, 2011, pp. 213–220. [Online]. Available: https://doi.org/10.1145/2043932.2043971 

- [23] D. Kowald, M. Schedl, and E. Lex, “The unfairness of popularity bias in music recommendation: A reproducibility study,” in Advances in Information Retrieval, ser. ECIR ’20. Cham, Germany: Springer International Publishing, 2020, pp. 35–42. [Online]. Available: https://doi.org/10.1007/978-3-030-45442-5_5 

- [24] M. Saveski and A. Mantrach, “Item cold-start recommendations: Learning local collective embeddings,” in Proceedings of the 8th ACM Conference on Recommender Systems, ser. RecSys ’14. New York, NY, USA: ACM, 2014, pp. 89–96. [Online]. Available: https://doi.org/10.1145/2645710.2645751 

- [25] H. Abdollahpouri and S. Essinger, “Multiple stakeholders in music recommender systems,” in 1st International Workshop on Value-Aware and Multistakeholder Recommendation at RecSys 2017, ser. VAMS ’17, August 2017, pp. 1–3. [Online]. Available: http://arxiv.org/abs/1708.00120 

- [26] C. Bauer and E. Zangerle, “Leveraging multimethod evaluation for multi-stakeholder settings,” in 

Proceedings of the 1st Workshop on the Impact of Recommender Systems, ser. ImpactRS ’19, vol. 2462, 2019. [Online]. Available: http://ceur-ws.org/ Vol-2462/short3.pdf 

- [27] P. Knees, A. Ferraro, and M. Hübler, “Bias and feedback loops in music recommendation: Studies on record label impact,” in Proceedings of the 2nd Workshop on Multi-Objective Recommender Systems, colocated with 16th ACM Conference on Recommender Systems (RecSys 2022), ser. CEUR Workshop Proceedings, vol. 3268. CEUR-WS.org, 2022. [Online]. Available: https://ceur-ws.org/Vol-3268/paper6.pdf 

- [28] P. Pu, L. Chen, and R. Hu, “A user-centric evaluation framework for recommender systems,” in Proceedings of the Fifth ACM Conference on Recommender Systems, ser. RecSys ’11. New York, NY, USA: ACM, 2011, p. 157–164. [Online]. Available: https://doi.org/10.1145/2043932.2043962 

- [29] European Union, “Regulation (eu) 2022/2065 of the european parliament and of the council of 19 october 2022 on a single market for digital services and amending directive 2000/31/ec (Digital Services Act),” 2022. [Online]. Available: https: //eur-lex.europa.eu/eli/reg/2022/2065/oj 

- [30] N. Tintarev and J. Masthoff, “Beyond explaining single item recommendations,” in Recommender Systems Handbook, F. Ricci, L. Rokach, and B. Shapira, Eds. New York, NY: Springer US, 2022, pp. 711–756. [Online]. Available: https: //doi.org/10.1007/978-1-0716-2197-4_19 

- [31] B. Ferwerda, E. Ingesson, M. Berndl, and M. Schedl, “I don’t care how popular you are! investigating popularity bias in music recommendations from a user’s perspective,” in Proceedings of the 2023 Conference on Human Information Interaction and Retrieval, ser. CHIIR ’23. New York, NY, USA: ACM, 2023, pp. 357–361. [Online]. Available: https://doi.org/10.1145/3576840.3578287 

- [32] Y. Jin, N. Tintarev, N. N. Htun, and K. Verbert, “Effects of personal characteristics in control-oriented user interfaces for music recommender systems,” User Modeling and User-Adapted Interaction, vol. 30, pp. 199–249, 2020. [Online]. Available: https: //doi.org/10.1007/s11257-019-09247-2 

- [33] T. Kulesza, S. Stumpf, M. Burnett, S. Yang, I. Kwan, and W.-K. Wong, “Too much, too little, or just right? ways explanations impact end users’ mental models,” in 2013 IEEE Symposium on Visual Languages and Human Centric Computing, ser. VL/HCC ’13, 2013, pp. 3–10. [Online]. Available: https://doi.org/10.1109/VLHCC.2013.6645235 

- [34] P. Kouki, J. Schaffer, J. Pujara, J. O’Donovan, and L. Getoor, “Personalized explanations for hybrid recommender systems,” in Proceedings of the 

489 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

24th International Conference on Intelligent User Interfaces, ser. IUI ’19. New York, NY, USA: ACM, 2019, pp. 379–390. [Online]. Available: https://doi.org/10.1145/3301275.3302306 

- [35] G. Zhao, H. Fu, R. Song, T. Sakai, Z. Chen, X. Xie, and X. Qian, “Personalized reason generation for explainable song recommendation,” ACM Transactions on Intelligent Systems and Technology, vol. 10, no. 4, jul 2019. [Online]. Available: https://doi.org/10.1145/3337967 

- [36] M. Millecamp, N. N. Htun, C. Conati, and K. Verbert, “To explain or not to explain: The effects of personal characteristics when explaining music recommendations,” in Proceedings of the 24th International Conference on Intelligent User Interfaces, ser. IUI ’19. New York, NY, USA: ACM, 2019, pp. 397–407. [Online]. Available: https://doi.org/10.1145/3301275.3302313 

- [37] I. Andjelkovic, D. Parra, and J. O’Donovan, “Moodplay: Interactive mood-based music discovery and recommendation,” in Proceedings of the 2016 Conference on User Modeling Adaptation and Personalization, ser. UMAP ’16. New York, NY, USA: ACM, 2016, pp. 275–279. [Online]. Available: https://doi.org/10.1145/2930238.2930280 

- [38] M. Millecamp, N. N. Htun, Y. Jin, and K. Verbert, “Controlling Spotify recommendations: Effects of personal characteristics on music recommender user interfaces,” in Proceedings of the 26th Conference on User Modeling, Adaptation and Personalization, ser. UMAP ’18. New York, NY, USA: ACM, 2018, pp. 101–109. [Online]. Available: https: //doi.org/10.1145/3209219.3209223 

- [39] Y. Liang and M. C. Willemsen, “Exploring the longitudinal effects of nudging on users’ music genre exploration behavior and listening preferences,” in Proceedings of the 16th ACM Conference on Recommender Systems, ser. RecSys ’22. New York, NY, USA: ACM, 2022, pp. 3–13. [Online]. Available: https://doi.org/10.1145/3523227.3546772 

- [40] F. Sanna Passino, L. Maystre, D. Moor, A. Anderson, and M. Lalmas, “Where to next? a dynamic model of user preferences,” in Proceedings of the Web Conference 2021, ser. WWW ’21. New York, NY, USA: ACM, 2021, pp. 3210–3220. [Online]. Available: https://doi.org/10.1145/3442381.3450028 

- [41] S. Petridis, N. Daskalova, S. Mennicken, S. F. Way, P. Lamere, and J. Thom, “Tastepaths: Enabling deeper exploration and understanding of personal preferences in recommender systems,” in 27th International Conference on Intelligent User Interfaces, ser. IUI ’22. New York, NY, USA: ACM, 2022, p. 120–133. [Online]. Available: https://doi.org/10.1145/3490099. 3511156 

- [42] A. Anderson, L. Maystre, I. Anderson, R. Mehrotra, and M. Lalmas, “Algorithmic effects on the diversity of consumption on Spotify,” in Proceedings of The Web Conference 2020, ser. WWW ’20. New York, NY, USA: ACM, 2020, pp. 2155–2165. [Online]. Available: https://doi.org/10.1145/3366423.3380281 

- [43] C. Bauer and E. Zangerle, “Information imbalance and responsibility in recommender systems,” in 2nd Workshop on Green (Responsible, Ethical and Social) IT and IS—the Corporate Perspective (GRES-IT/IS), ser. GRES-IT/IS ’18. Vienna, Austria: Department für Informationsverarbeitung und Prozessmanagement, WU Vienna University of Economics and Business, March 2018. [Online]. Available: https://epub.wu.ac.at/7681/ 

- [44] J. W. Morris and D. Powers, “Control, curation and musical experience in streaming music services,” Creative Industries Journal, vol. 8, no. 2, pp. 106–122, 2015. [Online]. Available: https://doi.org/10.1080/ 17510694.2015.1090222 

- [45] G. Guest, A. Bunce, and L. Johnson, “How many interviews are enough?: An experiment with data saturation and variability,” Field Methods, vol. 18, no. 1, pp. 59–82, 2006. [Online]. Available: https://doi.org/10.1177/1525822X05279903 

- [46] P. Mayring, Qualitative content analysis, 2nd ed. Sage, 2004, vol. 1, pp. 159–176. 

- [47] K. Dinnissen and C. Bauer, “Questionnaire: Music Industry Professionals’ View on Music Streaming Services and Recommender Systems,” Jul. 2023. [Online]. Available: https://doi.org/10.5281/zenodo. 8121152 

- [48] “Spotify EQUAL,” 2023, accessed: 2023-07-07. [Online]. Available: https://open.spotify.com/genre/ equal-page 

- [49] “Women’s Impact,” 2023, accessed: 2023-07-07. [Online]. Available: https://www.deezer.com/en/channels/ womensvoices 

- [50] “Diversity & Tradition: New Black Americana,” 2023, accessed: 2023-07-07. [Online]. Available: https://tidal.com/browse/playlist/ d80fa7b2-a08b-4b49-9de7-65326d5dfe51 

- [51] M. Bogen, A. Rieke, and S. Ahmed, “Awareness in practice: Tensions in access to sensitive attribute data for antidiscrimination,” in Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency, ser. FAT* ’20. New York, NY, USA: ACM, 2020, pp. 492–500. [Online]. Available: https://doi.org/10.1145/3351095.3372877 

- [52] C. Hosey, L. Vujovi´c, B. St. Thomas, J. GarciaGathright, and J. Thom, “Just give me what i want: How people use and evaluate music search,” in Proceedings of the 2019 CHI Conference on Human 

490 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

Factors in Computing Systems, ser. CHI ’19. New York, NY, USA: ACM, 2019, p. 1–12. [Online]. Available: https://doi.org/10.1145/3290605.3300529 

- [53] M. Clark, “YouTube Music will let you make your own custom radio stations,” Feb. 2023, accessed: 2023-07-07. [Online]. Available: https://www.theverge.com/2023/2/21/23609228/ youtube-music-radio-builder-custom-stations 

- [54] “Never Miss Home Again With Deezer’s Country Selector,” Sep. 2020, accessed: 2023-07-07. [Online]. Available: https://www.deezer-blog.com/press/ deezer-country-selector/ 

- [55] “Spotify Debuts a New AI DJ, Right in Your Pocket,” Feb. 2023, accessed: 2023-07-07. [Online]. Available: https://newsroom.spotify.com/2023-02-22/ spotify-debuts-a-new-ai-dj-right-in-your-pocket/ 

- [56] I. Pettersson, C. Fredriksson, R. Dadgar, J. Richardson, L. Shields, and D. McKenzie, “Minimizing change aversion through mixed methods research: A case study of redesigning spotify’s your library,” in Extended Abstracts of the 2023 CHI Conference on Human Factors in Computing Systems, ser. CHI EA ’23. New York, NY, USA: ACM, 2023. [Online]. Available: https://doi.org/10.1145/3544549.3573875 

491 

