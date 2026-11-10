---
paper_id: "000092"
year: 2022
title: "Download pdf"
source_url: "https://zenodo.org/record/7316776/files/000092.pdf"
---

# A REPRODUCIBILITY STUDY ON USER-CENTRIC MIR RESEARCH AND WHY IT IS IMPORTANT 

Peter Knees<sup>1,3</sup> Bruce Ferwerda<sup>2</sup> Andreas Rauber<sup>1</sup> Sebastian Strumbelj<sup>1</sup> Annabel Resch<sup>1</sup> Laurenz Tomandl<sup>1</sup> Valentin Bauer<sup>1</sup> Fung Yee Tang<sup>1</sup> Josip Bobinac<sup>1</sup> Amila Ceranic<sup>1</sup> Riad Dizdar<sup>1</sup> 1 Faculty of Informatics, TU Wien, Austria 2 Department of Computer Science and Informatics, Jönköping University, Sweden 3 School of Music, Georgia Institute of Technology, USA 

peter.knees@tuwien.ac.at 

## ABSTRACT 

Reproducibility of results is a central pillar of scientific work. In music information retrieval research, this is widely acknowledged and practiced by the community by re-implementing algorithms and re-validating machine learning experiments. In this paper, we argue for an increased need to also reproduce the results and findings of user studies, including qualitative work, especially since these often lay the foundations and serve as justification for choices taken in algorithmic design and optimization criteria. As an example, we attempt to reproduce the study by Kim et al. [1] presented in the RecSys (2020) paper ªDo Channels Matter? Illuminating Interpersonal Influence on Music Recommendationsº. By repeating this study on how interpersonal relationships can affect a user’s assessment of music recommendations on a new sample of n = 142 participants, we can largely confirm and support the validity of the original results. At the same time, we extend the analysis and also observe differences with regards to adoption rates between different channels as well as different factors that influences the adoption rate. From this specific reproducibility study, we conclude that potential cultural differences should be accounted for more explicitly in future studies and that systems development should be more explicitly connected to its intended target audience. 

## 1. INTRODUCTION AND CONTEXT 

Ensuring the demonstrable reproducibility of experiments is an essential part of the scientific method to acquire knowledge. Reproducibility in music information retrieval research traditionally has a strong focus on the repeatability of experiments that demonstrate the performance of a 

© P. Knees, B. Ferwerda, A. Rauber, S. Strumbelj, A. Resch, L. Tomandl, V. Bauer, F. Y. Tang, J. Bobinac, A. Ceranic, and R. Dizdar. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: P. Knees, B. Ferwerda, A. Rauber, S. Strumbelj, A. Resch, L. Tomandl, V. Bauer, F. Y. Tang, J. Bobinac, A. Ceranic, and R. Dizdar, ªA Reproducibility Study on Usercentric MIR Research and Why it is Importantº, in Proc. of the 23rd Int. Society for Music Information Retrieval Conf., Bengaluru, India, 2022. 

system. To this end, the formalization and complete documentation of MIR workflows and processes is a top priority (e.g., [2]). This includes proper documentation and provision of access to the data involved, to avoid contributing to the so-called reproducibility crisis found throughout virtually all scientific disciplines. In the MIR community the aspect of data access has been a topic of discussion since the beginning, as dataset sharing is a particularly challenging and sensitive matter, foremost due to copyright issues, cf. [3,4]. Also for evaluation, emphasis is given to applying transparent, open, and sustainable methods, to objectively quantify the performance of systems and consistently compare systems [5]. In short, many efforts of the community are devoted to sharing resources, re-implementing algorithms, and re-validating machine learning experiments to ensure reliable and valid scientific results. 

In order to avoid potentially contributing to the reproducibility crisis on another front, we argue that there is urgent need in MIR research to also reproduce the results and findings of user-centric studies, including qualitative work. The system-centric view in MIR has been repeatedly subject to criticism and raised calls for more user-centric approaches (e.g., [6, 7]) as the objectives of the systems developed are ultimately rooted in users’ needs. In practice this has led to user-centric work taking the essential roles of requirement engineering (e.g. [8±10]) and/or of a system evaluation vehicle, either by generating ground truth, rating the outcomes of systems, or reflecting on their use (e.g., [11±13]). As their outcomes have (or are supposed to have) a fundamental impact and serve as justification for choices taken in algorithmic design and deployed optimization criteria [14, 15], their validity is by no means of lesser importance than that of system-based experiments. Clearly, reproducibility of experiments involving human subjects is hard, as witnessed in the social sciences [16], and has led to the development of the current evaluation strategies as a workaround [17]. Nonetheless, when it comes to the justification of systems objectives, further attention should be paid to the scientific validity of findings by reproducing and corroborating the findings of studies. 

As an example, in this paper, we attempt to reproduce the study by Kim et al. [1], presented in the ACM Rec- 

764 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

Sys 2020 paper ªDo Channels Matter? Illuminating Interpersonal Influence on Music Recommendationsº. We have chosen this particular user study for several reasons. First, the study subject is highly relevant for the development and understanding of music recommender systems, therefore clarifying the reproducibility of the experiments is important for future research. Second, the study is well documented with a clearly laid out methodology. Third, as the original data was collected via a web-based survey, to obtain a new set of responses of comparable quality, we can follow the same strategy, with the main difference that recruited participants have a different cultural, i.e. predominantly European, background. 

In addition to repeating the original study to investigate the differences of music recommendations from music recommender systems (non-interpersonal) and friends and acquaintances (interpersonal), we carry out further analyses to gain insights regarding gender differences. We further make use of the PRIMAD framework for reproducibility of research in e-Science for positioning our work [18]. In the terminology of the PRIMAD framework, in our reproducibility study, we foremost prime the factor of data and consequently investigate the generalization capabilities of the analysis wrt. another sample of users. Through the additional analyses, we also extend the methodology used. 

The remainder of this paper is structured as follows. Section 2 briefly motivates and summarizes the original study by Kim et al. [1]. In Section 3, we describe the methods used to reproduce the study. Section 4 reports on the results and findings of the reproduced study, which are further discussed in relation to the original study in Section 5. In Section 6, we use the PRIMAD model as a tool to systematically categorize the dimensions of reproducibility in this work and suggest its use for future reproducibility studies (not only) of user-centric studies in the MIR research community. Finally, in Section 7 we draw conclusions from this reproducibility study and point out aspects to be considered for future work. 

## 2. ORIGINAL WORK TO BE REPRODUCED 

We aim at reproducing the findings of Kim et al. [1], who have conducted a web survey to investigate the perceptions, evaluations, and differences of music recommendations received through two different channels: interpersonal, i.e., music recommendations received from friends or acquaintances, and non-interpersonal, i.e. music recommendations received from recommendation systems and through updates on artists followed. The rationale behind that study is to gain a deeper understanding of the characteristics of interpersonal music recommendations and how the interpersonal relationship affects the evaluation of the recommendation. 

To this end they recruited 175 Korean-speaking participants (56% female; all above age 18, with 91% of participants between 18 and 32).<sup>1</sup> Furthermore, they collected 

> 1 Despite highlighting that all participants spoke Korean fluently, it is not explicitly stated whether the survey was conducted in Korean or English. 

|Study|Kim<br>et al.[1]|Current<br>study|
|---|---|---|
|Number ofparticipants(n)|175|142|
|Femaleparticipants|56%|45%|
|Age between 18 and 32|91%|86%|
|Use music subscription service|85%|69%|
|Sharingmusic with others|62%|16%|



Table 1. Demographics and characteristics of survey participants in the original study and the reproducibility study. Values for the current study refer to percentages in recorded responses. 

information that 85% of the participants were active users of a music subscription service for more than one year and that 62% of participants were actively sharing music with others more than once per week (see Table 1). 

The study shows an interesting trend, namely that music recommendations obtained from a system are typically considered to be more relevant for a user’s own taste (which is the primary objective of recommender systems), more convenient, and more frequently used and adopted than interpersonal recommendations. On the other hand, aspects of diversity, novelty, and serendipity were evaluated higher when recommendations were obtained through interpersonal channels. More detailed results of the study are also included in this paper for comparison in Section 4. 

From these results, the authors conclude that indeed interpersonal and non-interpersonal channels have different characteristics that should be accounted for when designing music recommendation platforms, particular to take advantage of their individual strengths (e.g., relevance vs. diversity and novelty). They further highlight a limitation of their study and point to a possible next step: ªSince the study was conducted in Korea, Korean cultural background was reflected in the results. Future studies with participants from other cultures (e.g., with different norms, technologies available, etc.) will enable us to explore how cultural differences can influence users’ perceptions and behaviors towards music recommendations from different channels.º In this paper, we aim at gaining such insights by conducting the same study again with a fresh set of participants, with a different background (i.e., predominantly European), as described next. 

## 3. METHODS 

Following the method of Kim et al. [1], we used a web-based survey to investigate interpersonal and noninterpersonal music channels in the context of music playlist creation and consumption. A similar survey was designed with a section regarding interpersonal channels (i.e., from friends or acquaintances) and a section regarding non-interpersonal channels (i.e., from recommendation systems) and sections with the respective questions were presented in a random order to the participants (see Table 2 for the survey questions). The survey was conducted in English with all participants. The questions for each 

765 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

section consisted of the same questions, the only difference is whether they are related to interpersonal or noninterpersonal channels. Upon presenting a section to the participants, they were first asked if they had ever received recommendations through the respective channel. If they had not, they would skip the questions of that section and would move on to the next section. 

The survey questions were divided into two parts: 1) evaluation criteria, and 2) usage behavior. Participants were asked to respond to the four evaluation criteria (i.e., relevance, diversity, novelty, and serendipity) using a 5- point Likert scale. Participants were then asked to respond to the usage behavioral questions of frequency and convenience in a similar 5-point Likert scale fashion. Additionally, participants were asked to estimate the adoption rate of the recommended music to their playlist (i.e., adding the music to their playlist) on a percentage level. As with the original survey, no actual recommendations were presented, as the survey solely focused on past experiences of received recommendations. 

## 4. RESULTS 

We recruited a total of 142 participants for this study in the context of three Master’s course projects at TU Wien via open calls for participation advertised to other students in the course, as well as other peers and acquaintances in their extended networks, cf. [19±21] 

Out of the disclosed and collected information of the total 142 participants, 45% identify as female, 55% as male, with 86% aged between 18 and 32. When it comes to the use of music subscription services, 69% of the participants indicated to use music subscription services for more than a year, and 16% shared music with others more than once a week (a side-by-side comparison with the original study can be found in Table 1). To investigate the reproducibility of Kim et al. [1], similar statistical tests were used. In terms of cultural background, 89% of reporting participants in our study state their origin to be in a European country. In contrast to the original study, where 100% of participants reported their background as Asian (specifically, Korean), in our study, only 7% report their origin to be in an Asian country (see Table 3). 

## 4.1 Evaluation of music recommendation channels 

Initial mean comparison show that diversity, novelty, and serendipity on average score higher for interpersonal music channels, while relevance, convenience, frequency, and adoption rate are higher for the non-interpersonal channels (see Table 4). When conducting significance testing on the four evaluation criteria, paired t-tests confirm that diversity (p < .001) and novelty (p = .002) are rated higher for interpersonal channels and relevance (p < .001) is rated higher for non-interpersonal channels (see Figure 1A). 

An additional principal component analysis (PCA) was conducted to investigate the relationship between the four evaluation criteria. The correlation matrix show that some of the evaluation criteria appeared to be similar than oth- 

ers. The PCA show two components to be extracted from the data with a total accounted variance of 67%: component 1 accounts for 42% and component 2 accounts for 24%. PCA bi-plot (see Figure 2) show that relevance is mainly explained by component 1, and diversity, novelty, and serendipity by component 2. The bi-plot indicate that diversity, novelty, and serendipity are more closely aligned, while relevance is almost orthogonal to these three evaluation criteria. 

## 4.2 Usage behavior of music recommendation channels 

Non-interpersonal channels rated higher for convenience, frequency, and adoption rate (see Table 4). Significance testing by using paired t-tests show that frequency was significantly rated higher (p < .001) for non-interpersonal channels than for interpersonal channels (see Figure 1B). When it comes to the convenience of using a channel, noninterpersonal channels were rated higher (p = .004) as well (see Figure 1C). However, when it comes to the adoption rate, although the non-interpersonal channel scored slightly higher, there was no significant difference (p = ns) between non-interpersonal and interpersonal channels. 

Additionally, a linear regression was conducted to investigate the effect of frequency on adoption rate. Frequency has a significant effect on adoption rate for interpersonal channels (F (1, 110) = 4.416, p = .038) as well as for non-interpersonal channels (F (1, 90) = 4.971, p = .028). Whereas convenience plays an additional role on adoption rate of non-interpersonal channels (F (1, 90) = 4.312, p = .041). 

Furthermore, a univariate regression was conducted to investigate the four evaluation criteria on the adoption rate. For the interpersonal channels, diversity (F (1.68) = = = = 1.574, p .003), novelty (F (1.68) 2.220, p .002) show to have a significant effect on adoption rates, while for the non-interpersonal channels only novelty (F (1.68) = 1.596, p = .06) appeared to be significant. 

## 4.3 Gender differences 

We conducted an additional multivariate test to investigate the role of gender between interpersonal and noninterpersonal channels. Gender differences were found when it comes of frequency of the receiving recommendations through non-interpersonal channels (F (1, 90) = 4.475, p = .035), indicating that males receive more frequent recommendations through non-interpersonal channels than females. However, no significant gender differences (p = ns) were found within interpersonal channels. 

Furthermore, a marginal significant effect was found of gender on novelty within interpersonal channels (F (1, 68) = 3.138, p = .061), indicating that males in particular receive more novel recommendations through interpersonal channels such as friends and acquaintances than females. No significant effects (p = ns) of gender were found within non-interpersonal channels. 

766 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

|Evaluation criteria|Relevance|Is the music recommend through the channel consistent with the context and<br>theme of theplaylist?|
|---|---|---|
||Diversity|Does the music recommended through the channel diversify genre or mood of the<br>playlist?|
||Novelty|Is the music recommended through the channel new or novel?|
||Serendipity|Is the music recommended through the channel unexpected but good in terms of<br>the context and theme of theplaylist?|
||Frequency|How often doyou receive music recommendations through the channel?|
|Usage behavior|Convenience|How convenient is the process of listening to the music recommended through<br>the channel?|
||Adoption rate|What percentage of the recommended music through the channel is added to the<br>playlist?|



Table 2. Survey questions. Same questions were used for both interpersonal and non-interpersonal channels. Adopted from Kim et al. [1]. 



<!-- Start of picture text -->
A) Evaluation Criteria B) Frequency C) Convenience D) Adoption Rate<br>5 Daily Very convenient 100<br>4 At least once per week Convenient 75<br>3 At least once per month Neutral 50<br>2 At least once per year Inconvenient 25<br>1 Hardly ever Very inconvenient<br>Relevance (***) Diversity (***) Novelty (**) Serendipity (ns) Frequency (***) Convenience (**) Adoption rate (ns)<br>InterpersonalNon-interpersonal<br><!-- End of picture text -->

Figure 1. Mean scores with standard deviation error bars (∗ p < 0.01, ∗∗ p < 0.001, ∗∗∗ p < 0.0001). 

|Continent|Percentage|
|---|---|
|Europe|89%|
|Asia|7%|
|Africa/Middle East|3%|
|Oceania|1%|



Table 3. Distribution of participants of the current study according to disclosed origin per continent. 



<!-- Start of picture text -->
Component Plot<br>1.0 1.0<br>0.5 0.5<br>Serendipity<br>0.0 0.0<br>Component2<br>-0.5 -0.5<br>-1.0 -1.0<br>-1.0 -0.5 0.0 0.5 1.0<br>Component 1<br><!-- End of picture text -->

Figure 2. PCA biplot with the two extracted components. 

## 5. DISCUSSION 

In this section, we discuss the results obtained with regards to reproducibility, deviations from the original study, and additional analyses carried out to gain further insights. 

## 5.1 Reproducibility 

For this reproducibility study we followed similar procedures and methods of the original work by Kim et al. [1]. Following the same procedures we recruited 142 participants to fill in questions on their music consumption behaviors through interpersonal and non-interpersonal music channels. 

Looking at the mean values, the overall strength of the mean values suggest that similar trends are found (see Table 4) in the current study as in the original study of Kim et al. [1] between interpersonal channels and noninterpersonal channels. By additionally conducting paired t-tests, we tested whether there are significant differences between the interpersonal and non-interpersonal channels. Also here, we found in general similar results aside of that novelty returned significant, but serendipity and adoption rate became not significant. These results indicate that the sample in this reproducibility study showed less pronounced difference in the areas of serendipity and adoption rate between interpersonal and non-interpersonal channels, but more differences in novelty. 

When looking at the relationship between the four evaluation criteria (i.e., relevance, diversity, novelty, and serendipity), we also found similar results as in the original study. The PCA results show the extraction of two components with a total of 67% of the variance accounted for: component 1 accounting for 43% of the variance and component 2 accounting for 24% of the variance. Our results show that the four evaluation criteria account for a 

767 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

|||Kim et al.[1]|||Current study||
|---|---|---|---|---|---|---|
||Interpersonal<br>(n= 155)|Non-Interpersonal<br>(n= 143)|p|Interpersonal<br>(n= 118)|Non-Interpersonal<br>(n= 100)|p|
|Relevance|3.47(0.86)|4.05(0.70)|<0.0001|3.45(0.88)|3.90(0.88)|<0.0001|
|Diversity|3.92(0.77)|3.59(0.90)|<0.001|3.59(0.95)|3.14(1.2)|<0.001|
|Novelty|4.09(0.71)|3.94(0.82)|ns|3.85(0.88)|3.44(1.0)|<0.01|
|Serendipity|3.65(0.96)|3.23(0.98)|<0.001|3.59(0.85)|3.44(0.94)|ns|
|Convenience|2.64(0.86)|3.05(0.83)|<0.0001|3.41(1.0)|3.78(1.0)|<0.01|
|Frequency|2.03(0.71)|2.65(0.89)|<0.01|2.82(0.89)|3.54(0.83)|<0.001|
|Adoption rate|38.34(22.47)|45.76(22.51)|<0.01|38.57(26.80)|38.68(27.24)|ns|



Table 4. Mean values of each factor with standard deviations and significance levels. Boldfaced values indicate the higher mean values between interpersonal vs. non-interpersonal. 

little less of the variance compared to the original study (75.2% with component 1 accounting for 49% and component 2 accounting for 26.2%). Although the accounted variance of the PCA is lower than of the original study, the extracted components still account for a large part of the variance. 

Further linear regression show similar results as in the original study in which frequency plays a significant role in both interpersonal and non-interpersonal channels when it comes to adoption rates. Additional univariate testing show that adoption rates are influenced by diversity and novelty through interpersonal channels, while the novelty factor only plays a role on adoption rates in noninterpersonal channels. In this respect, our sample differs significantly compared to the Korean sample of the original study in which relevance and novelty factors play a role on adoption rates in interpersonal channels and relevance and diversity influenced adoption rates in non-interpersonal channels. 

## 5.2 Deviations 

Although in general similar results were found in line with the original study, there are obvious differences regarding the effect of certain evaluation criteria on the adoption rate. Where the original study found relevance and novelty to play a role in interpersonal channels and relevance and diversity in non-interpersonal channels on adoption rates, the current study found that it is especially diversity and novelty for interpersonal channels and novelty for non-interpersonal channels on adoption rates. This indicates that for the participants in the current study, they believe that non-system recommendations are able to provide them with more diverse music to listen to. Hence, music that gets recommended through friends or acquaintances consist of better ways to find new music to listen to in order to deepen or broaden people’s music taste. This would suggest that people feel that music recommended through a system or service is more homogeneous (e.g., recommending music from the short tail). The need to include more diversified recommendations (or at least the perception of diversification) in those systems may play an important role on the satisfaction of users [22]. 

The found differences need to have further exploration to find the root-cause of occurring. A possible cause could 

be that cultural differences play a role [23]. The sample in the current study consisted of European participants whereas the original study only had Korean participants. Another difference in the demographics of the sample in the current study is the low amount of participants that is sharing music with others (merely 16% opposed to 62% in the original study), which could contribute to the differences in findings. 

## 5.3 Additional findings 

Aside of testing the reproducibility of the work of Kim et al. [1], we took this opportunity to further investigate other effects within interpersonal and non-interpersonal channels. Our findings show that the usability of noninterpersonal channels plays a significant role on the adoption rate of the music. In this case adding the recommended music to the user’s playlist. Hence, even though improving algorithms is given a lot of attention, the usability still plays a vital role on whether recommendations of systems are being adopted by its users. 

We furthermore found that gender plays a role in some aspects of interpersonal and non-interpersonal channels. In particular, males were found to receive more frequent music recommendations than females. This suggest that males in general might be using music recommendations systems more frequently than females. Additionally we found an effect of gender on receiving novel music recommendations through interpersonal channels. These results suggest that males believe that music recommendations received through friends or acquaintances are more often new or novel than females believe that they receive through interpersonal channels. Hence, it seems that the friends and acquaintances of males share and recommend more often music that is new or novel with each other. 

## 6. ANALYSIS USING THE PRIMAD MODEL 

In order to further analyze and systematically place the conducted reproducibility study, we apply the PRIMAD model [18]. The goal of PRIMAD is to systematically vary (ªprimeº) the factors (P)latform, (R)esearch Objective, (I)mplementation, (M)ethod, (A)ctor, and (D)ata, and to categorize the various types of insights gained via the 

768 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

resulting reproducibility characteristics by analyzing the variations made. 

One of the core principles of the model is the underlying observation that a simple replication of experiments under completely identical conditions does not lead to any real knowledge gains, save from confirming a deterministic behavior of the process. A substantial knowledge gain, however, originates from specific priming and variation of factors. In the concrete case, we are foremost interested in the effect of priming (D)ata, with obvious deviations regarding (A)ctor, i.e. the persons executing the experiments, and (P)latform and (I)mplementation, which can be considered robust due to the well-established and replicable method, and are hence of lesser interest. By extending the analyses, we also vary the (M)ethod to gain further insights with regards to the unchanged overall (R)esearch Objective. 

The repetition of user experiments using a different data sample with a different background provides insights on the generalization capabilities of the analysis. This offers insights on whether the original observations also hold in (slightly) different data settings. Simply using the same data but priming only the parameter settings, on the other hand, uncovers the parameter sensitivity of an analysis. While such a sensitivity evaluation should actually be performed by the initial investigation we frequently observe that studies report on the process of meta-search for the optimal parameter setting, yet sometimes failing to report on the performance variations observed. These, however, are crucial for understanding whether an insight holds as general observation and can thus be deployed, or whether a highly sensitive parameter that causes huge performance variations on minor changes to that parameter basically would limit application to predefined test settings. 

More generally, the question of which factors to prime is difficult to answer. Priming of (D)ata (parameters, raw data) should be a given to derive conclusions that are not based on singular events and configurations. (M)ethod priming is essential for true confirmation of findingsÐ and is finding additional support from the area of explainable AI, where (in principle) interpretable surrogate models are used to understand and explore the behavior of more powerful black-box models. Priming of the (P)latform, at the least, leads to information on the correctness of the (I)mplementation and completeness of the description.<sup>2</sup> In the study investigated, the process was sufficiently documented and even could be reproduced without availability of the original code for the user study or for subsequent data analysis. In general, for user studies, the standards for description of study design, method description, and participants are high and expected to suffice for reproducing the study. Furthermore, as the number of settings and parameters to be documented and taken into account is much smaller than, e.g., in machine learning experiments, this should give further incentive to increasingly reproduce 

> 2 Unfortunately, this aspect seems to see decreasing relevance through the trend of publicly sharing code as extensive testing of code before reuse appears to have lower priority. An investigation of the potentially harmful effects of code sharing on scientific practice are still pending, however. 

user studies and gather even further insights by systematically ªprimingº factors. 

## 7. CONCLUSION 

In this work, we reproduced the study by Kim et al. [1] on differences of music recommendations obtained through non-interpersonal channels, i.e., recommender systems, and recommendations obtained through interpersonal channels, i.e. friends or acquaintances, with newly collected data (sample size n = 142). By re-implementing the analyses as carried out in the original study, we could largely confirm the original results and support their validity. Possibly caused by the differences in music sharing behavior and/or cultural differences (predominantly European vs. Korean study participants), we also found differences in our results mostly with regards to novelty in recommendations and their impact on adoption rate. From this we conclude that the aspect of cultural differences in music consumption should be accounted for more explicitly in future studies, i.e., by repeating and extending existing studies at larger, global scale, or specifically addressing cultures. As MIR systems ultimately are designed for users and user studies (if carried out) are the departing point for the design of these systems, findings of one existing study might not be reliable enough and generalize beyond the group it was conducted with. 

For conducting the various types of reproducibility studies in MIR, using the PRIMAD model seems to be a meaningful framework and we suggest its use in future studies. We should stress, however, that in many reproducibility studies the priming does not happen due to according study design, but to compensate for lack of information available, be it a lack of parameter descriptions, the lack of sharing the data sets involved in training and evaluating systems, failure to make (thoroughly tested) code available or have sufficiently detailed information on architecture and design of, e.g., deep neural network models. Such incomplete information forces the actors in reproducibility studies to make documented assumptions on the according setting, leading most likely to slight variations in the according setting compared to the original study design. 

## 8. ACKNOWLEDGEMENTS 

This research was funded in whole, or in part, by the Austrian Science Fund (FWF) [P33526]. For the purpose of open access, the author has applied a CC BY public copyright license to any Author Accepted Manuscript version arising from this submission. 

## 9. REFERENCES 

- [1] H. J. Kim, S. Y. Park, M. Park, and K. Lee, ªDo channels matter? illuminating interpersonal influence on music recommendations,º in Proceedings of the 14th ACM Conference on Recommender Systems. Virtual Event, Brazil: ACM, Sep. 2020, p. 663±668. 

769 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

- [2] K. R. Page, B. Fields, D. D. Roure, T. Crawford, and J. S. Downie, ªCapturing the workflows of music information retrieval for repeatability and reuse,º Journal of Intelligent Information Systems, vol. 41, no. 3, pp. 435±459, 2013. 

- [3] W. Chen, J. Keast, J. Moody, C. Moriarty, F. Villalobos, V. Winter, X. Zhang, X. Lyu, E. Freeman, J. Wang, S. Cai, and K. Kinnaird, ªData Usage in MIR: History & Future Recommendations,º in Proceedings of the 20th International Society for Music Information Retrieval Conference. Delft, The Netherlands: ISMIR, Nov. 2019, pp. 25±32. 

- [4] R. Bittner, M. Fuentes, D. Rubinstein, A. Jansson, K. Choi, and T. Kell, ªmirdata: Software for Reproducible Usage of Datasets,º in Proceedings of the 20th International Society for Music Information Retrieval Conference. Delft, The Netherlands: ISMIR, Nov. 2019, pp. 99±106. 

- [5] B. McFee, E. J. Humphrey, and J. Urbano, ªA plan for sustainable mir evaluation,º in Proceedings of the 17th International Society for Music Information Retrieval Conference, New York City, United States, Aug. 2016, pp. 285±291. 

- [6] M. Schedl, A. Flexer, and J. Urbano, ªThe neglected user in music information retrieval research,º Journal of Intelligent Information Systems, vol. 41, no. 3, pp. 523±539, 2013. 

- [7] P. Knees, M. Schedl, B. Ferwerda, and A. Laplante, ªUser awareness in music recommender systems,º in Personalized Human-Computer Interaction. De Gruyter Oldenbourg, 2019, pp. 223±252. 

- [8] S. J. Cunningham, N. Reeves, and M. Britland, ªAn ethnographic study of music information seeking: Implications for the design of a music digital library,º in Proceedings of the 3rd ACM/IEEE-CS Joint Conference on Digital Libraries. Houston, Texas: IEEE, May 2003, p. 5±16. 

- [9] J. H. Lee and R. Price, ªUnderstanding Users of Commercial Music Services through Personas: Design Implications,º in Proceedings of the 16th International Society for Music Information Retrieval Conference. Málaga, Spain: ISMIR, Oct. 2015, pp. 476±482. 

- [10] K. Andersen and P. Knees, ªConversations with Expert Users in Music Retrieval and Research Challenges for Creative MIR,º in Proceedings of the 17th International Society for Music Information Retrieval Conference. New York City, United States: ISMIR, Aug. 2016, pp. 122±128. 

- [11] E. L. M. Law, L. von Ahn, R. B. Dannenberg, and M. Crawford, ªTagatune: A game for music and sound annotation,º in Proceedings of the 8th International Conference on Music Information Retrieval. Vienna, Austria: ISMIR, Sep. 2007, pp. 361±364. 

- [12] J. H. Lee, ªCrowdsourcing Music Similarity Judgments using Mechanical Turk,º in Proceedings of the 11th International Society for Music Information Retrieval Conference. Utrecht, Netherlands: ISMIR, Aug. 2010, pp. 183±188. 

- [13] C. Inskip and F. Wiering, ªIn Their Own Words: Using Text Analysis to Identify Musicologists’ Attitudes towards Technology,º in Proceedings of the 16th International Society for Music Information Retrieval Conference. Málaga, Spain: ISMIR, Oct. 2015, pp. 455± 461. 

- [14] J. H. Lee and J. S. Downie, ªSurvey Of Music Information Needs, Uses, And Seeking Behaviours: Preliminary Findings.º in Proceedings of the 5th International Conference on Music Information Retrieval. Barcelona, Spain: ISMIR, Oct. 2004. 

- [15] J. H. Lee and S. J. Cunningham, ªToward an understanding of the history and impact of user studies in music information retrieval,º Journal of Intelligent Information Systems, vol. 41, no. 3, pp. 499±521, 2013. 

- [16] S. Schmidt, ªShall we really do it again? the powerful concept of replication is neglected in the social sciences,º Review of General Psychology, vol. 13, no. 2, pp. 90±100, 2009. 

- [17] J. Urbano, M. Schedl, and X. Serra, ªEvaluation in music information retrieval,º Journal of Intelligent Information Systems, vol. 41, no. 3, pp. 345±369, 2013. 

- [18] A. Rauber, V. Braganholo, J. Dittrich, N. Ferro, J. Freire, N. Fuhr, D. Garijo, C. Goble, K. Järvelin, B. Ludäscher, B. Stein, and R. Stotzka, ªPRIMAD ± information gained by different types of reproducibility,º in Reproducibility of Data-Oriented Experiments in e-Science (Dagstuhl Seminar 16041), J. Freire, N. Fuhr, and A. Rauber, Eds. Dagstuhl, Germany: Schloss Dagstuhl±Leibniz-Zentrum für Informatik, 2016, vol. 6, no. 1, pp. 128±132. 

- [19] A. Resch, S. Strumbelj, and L. Tomandl, ªA Reproducibility Analysis on: Do Channels Matter? Illuminating Interpersonal Influence on Music Recommendations,º Jan. 2021. [Online]. Available: https://doi.org/10.5281/zenodo.4459832 

- [20] V. Bauer, J. Bobinac, and F. Y. Tang, ªReproducibility Study: Do Channels Matter? Illuminating Interpersonal Influence on Music Recommendations,º Jan. 2022. [Online]. Available: https://doi.org/10.5281/zenodo.5920550 

- [21] A. Ceranic, R. Dizdar, and A. Sokoli, ªReproduce experimental results from a paper,º Jan. 2022. [Online]. Available: https://doi.org/10.5281/zenodo.5921006 

- [22] B. Ferwerda, M. P. Graus, A. Vall, M. Tkalcic, and M. Schedl, ªHow item discovery enabled by diversity leads to increased recommendation list attractiveness,º 

770 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

in Proceedings of the Symposium on Applied Computing. Marrakech, Morocco: ACM, Apr. 2017, p. 1693±1696. 

- [23] B. Ferwerda and M. Schedl, ªInvestigating the relationship between diversity in music consumption behavior and cultural dimensions: A cross-country analysis,º in Extended Proceedings of the 24th ACM Conference on User Modeling, Adaptation and Personalisation. Halifax, Canada: CEUR-WS, Jul. 2016. 

771 

