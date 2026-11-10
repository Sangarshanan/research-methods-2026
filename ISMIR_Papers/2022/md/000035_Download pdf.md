---
paper_id: "000035"
year: 2022
title: "Download pdf"
source_url: "https://zenodo.org/record/7316654/files/000035.pdf"
---

# NETWORK ANALYSES FOR CROSS-CULTURAL MUSIC POPULARITY 

Kongmeng Liew<sup>1</sup> Vipul Mishra<sup>1</sup> Yangyang Zhou<sup>1</sup> Elena V. Epure<sup>2</sup> Romain Hennequin<sup>2</sup> Shoko Wakamiya<sup>1</sup> Eiji Aramaki<sup>1</sup> 1 Graduate School of Science and Technology, Nara Institute of Science and Technology, Japan 2 Deezer Research, Paris, France 

{liew.kongmeng, vipul-mi, zhou.yangyang.zr4, wakamiya, aramaki}@is.naist.jp {eepure, rhennequin}@deezer.com 

## ABSTRACT 

Anglo-American popular culture has been said to be intricately connected to global popular culture, both shaping and being shaped by popular trends worldwide, yet few research has examined this issue empirically. Our research quantitatively maps the extent of these cultural influences in popular music consumption, by using network analyses to explore cross-cultural popularity in music from 30 countries corresponding to 6 cultural regions (N = 4863 unique songs over six timepoints from 2019-2021). Using Top100 charts from these countries, we constructed a network based on the co-occurrence of songs in charts, and used eigencentrality as an indicator of cross-cultural song popularity. We then compared the country-of-origin of the artists, arousal music features, and socioeconomic indicators. Songs from artists with Anglo-American backgrounds tended to have higher eigencentrality overall, and mixed effects regressions showed that eigencentrality was negatively associated with danceability, and positively associated with spectral energy, and the migrant population of the country (of the charts). Next, using community detection, we observed 11 separate ’communities’ in the network. Most communities appeared to be limited by region/culture, but Anglo-American music seemed disproportionally able to transcend cultural boundaries far beyond their geographical borders. We also discuss implications pertaining to cultural hegemony, and the effectiveness of our method in estimating cross-cultural popularity. 

## 1. INTRODUCTION 

How do songs become international hits? To some extent, research suggests that one answer is simply being based in America, and singing in English [1]. Numerous studies have documented the prevalence of Anglo-American artists on the charts of ’foreign’ countries throughout the 1960s to the 2000s [2, 3]. Yet, at the same time, the 

> © K. Liew, V. Mishra, Y. Zhou, E. V. Epure, R. Hennequin, S. Wakamiya, and E. Aramaki. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: K. Liew, V. Mishra, Y. Zhou, E. V. Epure, R. Hennequin, S. Wakamiya, and E. Aramaki, ªNetwork Analyses for Cross-Cultural Music Popularityº, in Proc. of the 23rd Int. Society for Music Information Retrieval Conf., Bengaluru, India, 2022. 

1980s saw a nationalistic increase in the consumption of domestic, and localized artists alongside widely dominant Anglo-American music [1,4]. However, these papers rely on country-determined charts as indicators of musicpopularity, which raises problems of irregularity. For example, the metrics/methods used to determine rankings on national top charts may differ between countries. Moreover, charts may also be defined through radio plays (e.g., Billboard), which biases the consumption pattern towards the distributor of the music, rather than bottom-up listening preferences. The advent of music streaming services in recent years provides a possible solution to both these issues: within a platform, charts are calculated through consistent metrics. Secondly, users choose the songs they want to listen to. While music recommendation systems do provide suggestions on songs for the user, these are still largely based on the users’ preferences and listening history [5], and users still retain agency in choosing whether or not to listen to a recommended song. This is a shift away from the music-purchase model [6], allowing for greater flexibility and choice. Accordingly, streaming charts offer increased granularity, whereas music-purchase models only monitor sales. In this regard, country charts from music streaming services may be more representative of bottom-up music consumption. 

In assessing the global top charts provided by streaming services, we are unable to decompose the cultural contribution of individual countries in determining overall global popularity, as such information is typically not made public. We thus needed a method to combine music from various country-charts to composite a marker of global popularity. To this end, we constructed a network from Top 100 charts from 30 countries (over 6 cultural regions), and relied on the co-occurence of songs within and across charts to determine its cross-cultural popularity through centrality. Constructing a network would also allow us to quantify the cultural diversity and clusters present across these 30 charts through community detection algorithms. More information on how networks are used in this paper is available in Section 2 (Methods). 

Accordingly, our research aims to use network analyses to model the cultural ’Communities’ present across these charts, and in doing so, assess the dynamics of cultural influences in music consumption around the world. We identified 11 Communities, most bounded by shared cultures, 

298 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

with the exception of the largely Anglo-American Community, which was prevalent across charts from all cultural regions. 

## 1.1 Network analyses 

Network analyses model the complex relational structures present in a data, and have been used in a diverse range of applications, from web search engines [7], to modeling language evolution [8], and are used widely in the social sciences [9, 10]. They examine relationships between nodes in a network: nodes refer to any entity that is treated as fundamental in the analysis. For example, in a study on social networks, individuals are often treated as nodes. The relationships between nodes are represented by edges. edges may be weighted, to reflect the strength of a connection between two nodes. For example, two individuals (nodes) that frequently interact with each other, may have a higher weight for that relationship (edge), than between two strangers. Accordingly, some nodes may be more strongly connected with other nodes in a network. These nodes exert a greater influence on the network, and are more ‘central’: centrality refers to the relative importance of a node to all other nodes within the network [11]. 

In this paper, we rely strongly on the notion of eigencentrality, which additionally accounts for the corresponding centrality of linked nodes in determining the centrality of a given node [12]. For our analysis, we define nodes to be unique songs, and the edge weights as the frequency by which they co-occur on any country’s Top 100 charts. Songs with high eigancentrality scores are more influential within the network, which means that they carry a greater presence across the various country-based Top 100 charts used in this analysis, which could be in turn indicative of greater cross-cultural popularity. 

## 1.2 Contextualizing factors 

For interpretation, we also compared the eigencentrality of songs on countries’ charts with socioeconomic indicators, as well as song-level information on the country-of-origin or residence of its artist, and features of rhythmic and intensity arousal. 

## 1.2.1 Artists’ Country-of-residence and origin 

While constructing a network of music charts would allow us to visualize and compare the influence of individual songs, we still needed to compare this information to the cultural background of these songs. As such, we obtained the country-of-residence (where possible) or country-oforigin of all artists that were represented on the charts. We then grouped these countries according to their cultural region to facilitate cultural comparison. 

## 1.2.2 Gross Domestic Product (GDP), income inequality, and migration 

Going beyond the network, we wanted to examine if economic development, social inequality, and migration could offer explanations for cross-cultural popularity. Past research has identified links between music preferences, and 

socialeconomic status (SES; [13]), such as social class [14]. At a country-level, Woolhouse and Bansal [15] found a direct relationship between economic development and music consumption patterns. Accordingly, we examined economic development through GDP per capita, and income inequality (Gini coefficient). Finally, we also examined migration statistics, as music has strong functions for identity formation in immigrants (see [16, 17]), who may bring with them differing music consumption patterns into the country they relocate to. Moreover, societies with high openness may be more accepting of immigrants and more open towards foreign cultures [18], and consequently, may be more receptive towards music from beyond their cultural region. 

## 1.2.3 Arousal features in music 

Rhythmic (danceability) and intensity (energy) arousal features of songs in national charts has been shown to reflect that country’s affordances for high-arousal negative emotional experiences in daily life [19]. Energy, in particular, has been shown to reflect the use of cathartic emotional downregulation of anger experiences [20]. Given that past research has found links between music popularity and arousal features (e.g., [21, 22], we also examined eigencentrality in the context of musical arousal. 

## 1.3 Related work: Network analyses in music research 

Networks have long been used to analyze and visualize relationship structures in music. In predicting artist popularity, Matsumoto et al. [23] constructed a context-aware network combining Spotify-based audio features with biographic metadata and ’related artist’ lists. South et al. [24] examined a dataset of musical collaborations on Spotify, and used eigencentrality to estimate the influence of artists on that dataset. Zinoviev [25] similarly examined the mobility of individual musicians amongst music groups in the Russian music industry. Finally, Ortega [21] examined music covers to estimate the influence of the original artist. While these projects largely used network analyses to estimate the popularity or influence of an artist or song, our research is unique in using chart co-ocurrence to derive cross-cultural popularity, through accounting for the relative popularity of songs from different regions around the world. 

## 2. METHODS 

## 2.1 Data Acquisition 

Our analysis utilized consumption charts of Top 100 songs (by monthly play count on Deezer) from 30 countries (see Table 1: Chart Country) for March 2019, September 2019, March 2020, September 2020, March 2021, and September 2021, for a total Nsongs = 16998 (unique Nsongs = 4863 from Nartists = 1001). 

For each song, we obtained the titles, artists, and ISRC codes from the Deezer Application Program Interface 

299 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

|Cultural Region|Chart Country|Country-of-Origin|
|---|---|---|
|African-Islamic|*UAE,<br>Saudi<br>Arabia,<br>Turkey,<br>South Africa|*Bahrain, *Morocco, Lebanon, *UAE, Saudi Arabia, Egypt,<br>*Syria, South Africa, Iraq, Nigeria, Turkey, Algeria, Uzbek-<br>istan, Iran, Azerbaijan, *Kazakhstan, *Kuwait, Tunisia, Jor-<br>dan, Palenstine, *Comoros, *Yemen, *Congo|
|Catholic-Europe|Croatia, Hungary, Poland, Austria,<br>Belgium, Spain, France, Italy|France, Italy, Belgium, Spain, Austria, Croatia, Slovenia,<br>Hungary, Poland, *Greece, Portugal|
|Confucian (Asia)|Not Applicable|South Korea, Japan|
|English-Speaking|Australia,<br>Canada,<br>*Ireland,|United Kingdom, United States, Canada, Australia, *New|
|(Anglo-American)|United Kingdom, United States|Zealand, *Ireland|
|Latin America|Argentina, Brazil, Chile, Colom-<br>bia, Guatemala, Mexico|Colombia, Philippines, *Puerto Rico, Argentina, Uruguay,<br>Chile, *Panama, Venezuela, *Dominican Republic, Peru, *Ja-<br>maica, Brazil, Mexico, Guatemala|
|Orthodox-Europe|Russia, Ukraine|*Lithuania, *Kosovo, Bosnia and Herzegovina, Ukraine, Ro-<br>mania, Serbia, Bosnia, Belarus, Bulgaria, Russia, Armenia|
|Protestant-Europe|Switzerland, Germany, Denmark,<br>Finland, Netherlands|Netherlands, Sweden, Norway, Germany, Switzerland, Den-<br>mark, Iceland, Finland, Estonia|
|West-South Asia|Not Applicable|Israel,Vietnam,Malaysia|



Table 1. List of countries where charts were sampled from (Chart Country) and where sampled artists either resided in or originated from (Country-of-Origin). These were grouped according to Inglehart & Welzel’s Cultural Map of the World (Cultural Region), following their macro-level orientation on Traditionalism and Secularity. Countries with ’*’ were not included in the original Cultural Map, but were categorized following the categories of their geographical neighbours. 

(API)<sup>1</sup> , and obtained artists’ country of residence/origin from the MusicBrainz API<sup>2</sup> . Through this method, we managed to obtain the country or residence for artists from 2942 songs, and manually searched for the country of residence or origin (if country of residence was unavailable) for the artists of the remaining 1921 songs, through a combination of databases from Google, Wikipedia, LastFM, and Popnable. For analyses, we labelled this variable as Country-of-Origin. We also obtained danceability, based on detrended fluctuation analysis [26], and spectral energy scores for each song through the Essentia [27] library. 

Country-level indicators of economic development were obtained through Gross Domestic Product (GDP) per capita, percentage of migrants, and income inequality (Gini) from the World Bank Databank<sup>3</sup> . We also categorized countries according to their respective Inglehart-Welzel cultural regions<sup>4</sup> : African-Islamic, Catholic-Europe, Confucian, English-Speaking, LatinAmerica, Orthodox-Europe, Protestant-Europe, and WestSouth Asia. If the country was not officially categorized in this system, we approximated the category based on the categorization of its geographical neighbours. Country categorizations are in Table 1, and data is available on our online repository<sup>5</sup> . 

## 2.2 Data Handling and Analysis 

To construct the networks, we created undirected edge lists for each timepoint, consisting of nodes (song), weight: the number of times any two songs (or nodes) appeared on the same country’s charts (denoted by W ). In other words, for any given timepoint, we define a network G, where G = (V, E). V refers to the set of unique songs in all 

> 1 https://developers.deezer.com/api 

> 2 https://musicbrainz.org 3 https://databank.worldbank.org/source/ world-development-indicators 4 https://www.worldvaluessurvey.org/ 5 https://osf.io/uyh6d/ 

charts, and E refers to the set of edges. W is the weighted adjacency matrix of the graph and is defined as follows for any pair of songs (i, j): 



<!-- Start of picture text -->
Wij = � Cooccur(Ck, i, j) (1)<br>Ck∈C<br><!-- End of picture text -->

where C = {C1, C2, . . . , CK} is the set of all considered charts and Ck is a particular chart (for a particular country and month), i.e. the set of 100 songs that were most listened in this country during this month. Cooccur is an indicator function which takes the value 1 if and only if song i and song j co-occur in Ck, and 0 otherwise. To assess the centrality of a node, we examined the eigencentrality (x) of a node i, which is written in Equation 2 as: 



<!-- Start of picture text -->
xi = Λ 1 � Wijxj (2)<br>j∈V<br><!-- End of picture text -->

Here, Λ refers to the largest eigenvalue of the matrix W . Centrality of a node (song) xi takes into account the sum of centralities of its neighbors, which was a reason why we used this measure (as opposed to degree centrality, which relies only on the number of connections). Eigencentrality parameters (e.g., number of iterations) relied on igraph defaults obtained from arpack [28]. 

For community detection, we used the modularity metric, which identifies nodes with statistically higher numbers of connections (edges) than random chance levels, and partitioning the interconnected nodes according to the boundaries of these ‘above random’ interconnections [29]. We used Clauset et al’s fastgreedy function (’cluster_fast_greedy’ [30]) that repeatedly combines lowerlevel communities to maximize modularity, for a bottomup determination of the number and structure of communities. These analyses were conducted through the igraph package [31] in R [32]. 

For statistical analyses, we fitted separate χ<sup>2</sup> tests and ordinary least squares (OLS) or linear mixed effects (LME) 

300 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



Figure 1. Network visualization using the Kamada-Kawai force-directed algorithm. Songs are represented by nodes, and node size corresponds to eigencentrality. Communities are displayed through colors. A version with node labels (titles and artists) is available on our online repository. 

regression models [33] predicting node (song) eigencentrality from Community (OLS), cultural region (LME), economic development (LME), and danceability/spectral energy features (LME). For LME models, random intercepts were included for country-of-consumption (countries’ charts), and random slopes were included for danceability and spectral energy by country where applicable. Degrees of freedom were estimated using Satterthwaite approximation. All categorical variables were deviation coded to examine the relative effect of a specific cultural region against the mean of all regions. 

## 3. RESULTS 

## 3.1 Descriptive statistics of detected Communities 

A total of 11 Communities (C1-11) were detected from the network. Of which, Communities 10 (C10) and 11 (C11) had substantial amounts (5807 and 2056 songs respectively), but the other Communities ranged between sizes of 179 (C5) to 832 (C8). Due to space concerns we report only the results on cultural regions in this paper, but contingency tables and lists describing the countryof-consumption of the charts and country-of-origin of the artists’ are available on our online repository<sup>6</sup> . Figure 1 displays a visualization of the network using a KamadaKawai layout [34]. 

We then tested the Communities’ association with country-of-consumption (that the Top 100 chart was from) and country-of-origin of the artist. These were grouped according to their cultural region, described in Table 1. We observed a significant association between Communities and songs’ culture-of-consumption, χ<sup>2</sup> (50, 10681) = 15433, p < .001, and between Communities and artists’ culture-of-origin, χ<sup>2</sup> (35, 10459) = 16253, p < .001. Figures 2 and 3 visualize the cultural make-up by culture-of- 



<!-- Start of picture text -->
400 0 Cultural Region<br>African−Islamic<br>Catholic−Europe<br>English−Speaking<br>Latin−America<br>200 0 Orthodox<br>Protestant−Europe<br>0<br>1 2 3 4 5 6 7 8 9 10 11<br>Communities<br>Figure 2.. Visualizing culture-of-consumption: the distri-<br>bution of charts that make up each Community, catego-<br>by cultural region. Community 10 (C10) for exam-<br>ple, comprises 5807 songs that are in charts from all 6 cul-<br>tural regions sampled in this study.<br>Cultural Region<br>400 0 African−Islamic<br>Catholic−Europe<br>Confucian<br>English−Speaking<br>Latin−America<br>200 0 Orthodox<br>Protestant−Europe<br>West−South−Asia<br>0<br>1 2 3 4 5 6 7 8 9 10 11<br>Communities<br>count<br>count<br><!-- End of picture text -->

Figure 2.. Visualizing culture-of-consumption: the distribution of charts that make up each Community, categorized by cultural region. Community 10 (C10) for example, comprises 5807 songs that are in charts from all 6 cultural regions sampled in this study. 

Figure 3. Visualizing culture-of-origin: the distribution of artists’ countries for each Community, categorized by cultural region. Community 10 (C10) for example, comprises 5807 songs, of which 4707 are from the English-Speaking (Anglo-American) cultural region. 

consumption and culture-of-origin. For the most part, with the exception of C10, we find the relative consistency between culture-of-consumption and culture-of-origin, suggesting that the artists residing or originating from a specified cultural Community were largely listened to (popular) within the same cultural Community. For example, C1 comprised charts from the Netherlands, and a majority (87.6%) artists were of Dutch origin. Other Communities represented a linguistic cultural sphere over several countries: in C8, French-origin artists comprised 88.7% of the Community, which was largely split amongst Belgian (36.4%), French (39.3%), and Swiss (27.8%) Top100 charts. However, for C10, we observed that AngloAmerican artists’ formed the majority (70.1%), but consumption was spread out over all cultural regions and all 30 countries. 

6 https://osf.io/uyh6d/ 

301 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
0. 4<br>0. 3 Cultural Region<br>African−Islamic<br>Catholic−Europe<br>English−Speaking<br>0. 2<br>Latin−America<br>Protestant−Europe<br>0. 1<br>0. 0<br>1 2 3 4 5 6 7 8 9 10 11<br>Communities<br>Mean Eigencentrality<br><!-- End of picture text -->

Figure 4. Mean eigencentrality of songs in each Community. Colors denote the most common culture-of-origin for artists in that Community. 

## 3.2 Cross-cultural popularity (eigencentrality) 

An OLS model (R<sup>2</sup> = 0.36, F (10, 11033) = 614, p < .001) with eigencentrality as the outcome variable, Communities as the predictor, and C1 as the reference level, found that, C2 (β = −0.19, t = −4.15, p < .001), C3 (β = −0.20, t = −4.01, p < .001), C4 (β = −0.25, t = −6.10, p < .001), C5 (β = −0.16, t = −2.87, p = .004), C6 (β = −0.18, t = −3.69, p < .001), and C7 (β = −0.19, t = −4.15, p < .001) showed significantly lower eigencentrality (than the average across Communities), and C10 (β = 1.17, t = 72.08, p < .001), and C11 (β = 0.14, t = 6.92, p < .001) showed significantly higher eigencentrality. These suggest that C2-7 had songs with cross-cultural popularity significantly lower than the Grand mean, and C10 and C11 had songs with crosscultural popularity significantly above the Grand mean. These results are visualized in Fig 4. 

Next, we examined the eigencentrality of songs by the culture-of-origin of the artist. As one artist could have several songs across various countries’ charts, we used a LME model, with random intercepts for country-ofconsumption (Model Rmarginal<sup>2=0.42, R</sup> conditional<sup>2=</sup> 0.44). As countries’ economic situation may have also influenced their consumption preferences, GDP per capita was added as a control variable. We observed a significant effect of culture-of-origin (F (7, 6166.9) = 778.73, p < .001), but not GDP per capita (F (1, 27.9) = 0.90, p = .350). With African-Islamic culture as a reference level, we found that songs originating from artists in CatholicEurope (b = −0.11, t = −9.31, p < .001), Latin America (b = −0.11, t = −8.43, p < .001), and Orthodox Europe (b = −0.06, t = −3.73, p < .001) cultures had eigencentrality significantly below the Grand mean, songs originating from artists in Confucian Asia (b = 0.12, t = 4.49, p < .001) and English-Speaking (Anglo-American) cultures (b = 0.34, t = 34.93, p < .001) had eigencentrality significantly above the Grand mean. This suggests that songs from Confucian Asian and Anglo-American artists appeared to be more popular cross-culturally. 

## 3.3 Additional analyses 

We fitted two LME models exploring possible factors behind cross-culturally song popularity. These include socioeconomic reasons, such as GDP, income inequality, and immigration, and musical reasons, where we focus on danceability and energy as measures of rhythmic and intensity arousal inherent in the song. For the socioeconomic model (Model Rmarginal<sup>2=0.05, R</sup> conditional<sup>2=0.10),</sup> only immigration, measured using 2015 migrant percentages within a country’s population, significantly predicted the eigencentrality of the songs on its charts (b = 0.01, t = 3.83, F (1, 20.1) = 14.67, p = .001). However, we noted the possibility that Anglo-American cultures, that typically have higher migrant percentages, also have artists with songs that have higher cross-cultural popularity. As such, we repeated the analysis with the exclusion of these countries (USA, UK, Australia, Canada). While still significant, migrant percentages predicted eigencentrality to a smaller extent (Model Rmarginal<sup>2=0.03, R</sup> conditional<sup>2=</sup> 0.07; b = 0.007, t = 2.21, F (1, 16.9) = 4.90, p = .041, suggesting that countries with larger migrant populations also consume songs that are more cross-culturally popular. 

While both are used as measures of arousal, danceability (rhythmic arousal) and spectral energy (intensity arousal) are only weakly correlated on a song-level (r = 0.043, p, .001). The LME model (Model Rmarginal<sup>2=</sup> 0.02, Rconditional<sup>2=0.12)showedasignificanteffectof</sup> danceability (F (1, 30.4) = 12.4, p = .001) and spectral energy (F (1, 26.9) = 16.3, p < .001). Eigencentrality was negatively predicted by danceability (b = −0.121, t = −3.52, p = .001), but positively predicted by spectral energy (b = 2.68, t = 4.04, p < .001). In sum, after controlling for country-specific effects, the cross-cultural popularity of a song was negatively associated with its danceability but positively associated with energy. 

## 4. DISCUSSION 

Our network appears to model the cultural spread of music consumption amongst the 30 countries studied. The 11 Communities detected largely reflect cultural consumption, which to some extent, seems to quantify linguistic boundaries as a common denominator across cultures. C8 for example, comprises French music, and is consumed in countries where French is widely spoken: Belgium, France, and Switzerland. Similarly, C9 comprises German artists, and is most consumed in Austria, Germany, and Switzerland. However, C10 appears unique in that that is largely comprised of songs by Anglo-American artists, yet is common in charts from countries where English is not primarily spoken. This appears to go beyond the nation or language-based consumption patterns of the other Communities. Given the high eigencentrality scores associated with songs from these cultures, our results may thus be indicative of a disproportional popularity of English-medium songs in global music consumption. 

This interpretation would be consistent with Bello and Garcia’s [4] research on nationalism and cultural diver- 

302 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

gence in local charts in recent years. Our results show that many charts retain a large amount of songs by local or regional artists, and despite past research suggesting that American cultural hegemony in popular music might have decreased in recent years (see [1]), still contain strong Anglo-American music presences. 

In contextualizing cross-cultural popularity in the socioeconomic conditions of a country, we found that migrant population, and not economic development (GDP) or income inequality (Gini coefficient), significantly predicted a country’s consumption of cross-cultural popular songs. As many such artists are of Anglo-American origins, and Anglo-American countries typically have large migrant populations, we repeated this analysis after systematically excluding these countries. Despite a smaller observed effect, our findings remained consistent, in suggesting that migrant population is associated with wider consumption of cross-culturally popular songs. We speculate that a larger migrant population could indicate a more diverse population [35, 36]. If so, consumption patterns may be less subject to nationalistic tendencies, and the drive for local music in recent years may not have had as strong an effect in these Communities. One possibility could be that this creates a larger space and demand for music that is popular elsewhere, but caution that these interpretations are speculations, and more research is needed to uncover the antecedents of cross-cultural popularity. 

We also examined cross-cultural popularity by analyzing song arousal. Following research by [22, 37] that found popular music comprised high intensity and strong rhythms, we show that intensity arousal appears to be more cross-culturally popular, but rhythmic arousal appeared inversely related to popularity. This suggests a conceptual differentiation between both arousal domains, and more research is needed to identify the distinct functions and qualities of both. 

Regarding the high eigencentrality of artists from Confucian Asian cultures, we note however that this could be a result of sampling bias. Given that we did not examine charts from Confucian Asian cultures, the presence of artists with this cultural background would mean that they had to have a level of global visibility to appear in the charts we sampled. In our data, these mainly consisted of South Korean artists, like BTS and Blackpink. Nevertheless, that these artists had songs with larger-thanaverage eigencentrality, despite our sample not having any East Asian charts (where they would have had a natural advantage), is a testament to the success of the South Korean Hallyu movement. Yet, research has also suggested that this may be due to the hybridization of Korean popular music with American influences and trends [38]. 

One limitation of our research is in the narrow sample of countries included in the analysis. For validity, we chose only to focus on countries where Deezer occupies a sizeable market share, inevitably under-representing users in Asia. Secondly, some songs may be region-locked, in that users from Country A may not necessarily be able to listen to a song from Country B. However, we think that this 

affects only a minority of songs, and most songs appear to be accessible from different geographical regions; region specificity may not be a strong-enough limiter in preventing German artists (for example) from being played in the United States. 

Next, we did not conceptually distinguish popularity from influence. Cross-cultural popularity (i.e., the consumption of foreign music) may not necessarily suggest cross-cultural influence (i.e., the pervasiveness of foreign aesthetics and values in local culture), and some of our arguments are built on the assumption that popularity reflects a certain amount of influence. A thorough distinction on mechanisms are beyond the scope of the current paper, but is an area that we feel is in need of more research. Finally, we had difficulties in differentiating country-oforigin from country-of-residence for the artists sampled. These issues were often technical, in that the databases we relied on did not necessarily specify these differences. Consequently, some issues on validity remain: an artists originating from Puerto Rico but residing in New York may be coded inconsistently. Nevertheless, we think our data is sufficient in supporting the broad claims on crosscultural popularity made in this paper, but we defer to ethnomusicologists working in localized geographical areas for greater depth on the role of specific cultural influences within local societies. 

## 5. CONCLUSION 

Given that our aim was to empirically quantify the dynamics of cultural influence in music charts, we think that the findings demonstrate a limited usefulness of our method of using song co-occurence on countries’ charts for network construction, to empirically examining the extent of a culture’s influence. While we focused solely on music consumption and popularity, which at best can be considered just one aspect of influence, we nevertheless found convergence in our findings on Anglo-American musical influence, with evidence from sociological and anthropological literature: Anglo-American dominance remains unmatched in its prevalence around the world. Moving forward, we propose that our method of network construction can also be used to examine the dynamics of regional influences from within the other Communities. For example, C11 comprises songs mostly on Latin American charts, but shows that artists tend to be from Puerto Rico or Colombia, and these artists from these countries may thus have a stronger regional influence within this Community. Thus, even within these regional cultural spheres, artists may be concentrated within industries centered on a small number of countries, and this may be of interest to researchers. All supplementary materials are available on our online OSF repository<sup>7</sup> , and we hope that this can be a resource for the music science community in researching the dynamics of cultural products and cross-cultural influence. 

7 https://osf.io/uyh6d/ 

303 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

## 6. REFERENCES 

- [1] P. Achterberg, J. Heilbron, D. Houtman, and S. Aupers, ªA cultural globalization of popular music? american, dutch, french, and german popular music charts (1965 to 2006),º American Behavioral Scientist, vol. 55, no. 5, pp. 589±608, 2011. [Online]. Available: https://doi.org/10.1177/0002764211398081 

- [2] H. Bekhuis, M. Lubbers, and W. Ultee, ªA MacroSociological Study into the Changes in the Popularity of Domestic, European, and American Pop Music in Western Countries,º European Sociological Review, vol. 30, no. 2, pp. 180±193, 10 2013. [Online]. Available: https://doi.org/10.1093/esr/jct028 

- [3] M. Verboord and A. Brandellero, ªThe globalization of popular music, 1960-2010: A multilevel analysis of music flows,º Communication Research, vol. 45, 01 2016. 

- [4] P. Bello and D. Garcia, ªCultural divergence in popular music: the increasing diversity of music consumption on spotify across countries,º Humanities and Social Sciences Communications, vol. 8, pp. 1±8, 2021. 

- [5] M. Schedl, ªDeep learning in music recommendation systems,º Frontiers in Applied Mathematics and Statistics, vol. 5, 2019. [Online]. Available: https:// www.frontiersin.org/article/10.3389/fams.2019.00044 

- [6] T. Wagner, M. Rose, C. Baccarella, and K.-I. Voigt, ªStreaming killed the download star! how the business model of streaming services revolutionizes music distribution,º Journal of Organizational Advancement, Strategic and Institutional Studies, vol. 8, pp. 29±39, 03 2015. 

- [7] P. Chen, H. Xie, S. Maslov, and S. Redner, ªFinding scientific gems with google’s PageRank algorithm,º Journal of Informetrics, vol. 1, no. 1, pp. 8±15, jan 2007. [Online]. Available: https: //doi.org/10.1016%2Fj.joi.2006.06.001 

- [8] J. C. Jackson, J. Watts, T. R. Henry, J.-M. List, R. Forkel, P. J. Mucha, S. J. Greenhill, R. D. Gray, and K. A. Lindquist, ªEmotion semantics show both cultural variation and universal structure,º Science (New York, N.Y.), vol. 366, no. 6472, p. 1517Ð1522, December 2019. [Online]. Available: https://doi.org/10.1126/science.aaw8160 

- [9] N. Hummon and P. Doreian, ªComputational methods for social network analysis,º Social Networks, vol. 12, pp. 273±288, 12 1990. 

- [10] S. P. Borgatti, A. Mehra, D. J. Brass, and G. Labianca, ªNetwork analysis in the social sciences,º Science, vol. 323, no. 5916, pp. 892±895, 2009. [Online]. Available: https://www.science.org/doi/abs/10.1126/ science.1165821 

- [11] D. Hevey, ªNetwork analysis: a brief overview and tutorial,º Health Psychology and Behavioral Medicine, vol. 6, no. 1, pp. 301±328, 2018, pMID: 34040834. [Online]. Available: https://doi.org/10. 1080/21642850.2018.1521283 

- [12] M. E. J. Newman, Mathematics of Networks. London: Palgrave Macmillan UK, 2016, pp. 1±8. [Online]. Available: https://doi.org/10.1057/ 978-1-349-95121-5_2565-1 

- [13] M. Liu, X. Hu, and M. Schedl, ªThe relation of culture, socio-economics, and friendship to music preferences: A large-scale, cross-country study,º PLOS ONE, vol. 13, no. 12, pp. 1±29, 12 2018. [Online]. Available: https://doi.org/10.1371/journal.pone.0208186 

- [14] K. van Eijck, ªSocial Differentiation in Musical Taste Patterns*,º Social Forces, vol. 79, no. 3, pp. 1163±1185, 03 2001. [Online]. Available: https: //doi.org/10.1353/sof.2001.0017 

- [15] M. H. Woolhouse and J. Bansal, ªWork, rest and (press) play: Music consumption as an indicator of human economic development,º Journal of Interdisciplinary Music Studies, vol. 7, pp. 45±71, 2013. 

- [16] E. Fock, ªWith the background in the foreground - music among young danes with immigrant backgrounds,º YOUNG, vol. 7, no. 2, pp. 62±77, 1999. [Online]. Available: https: //doi.org/10.1177/110330889900700205 

- [17] J. Louie, ªMedia in the lives of immigrant youth,º New directions for youth development, vol. 2003, pp. 111± 30, 02 2003. 

- [18] P. Dinesen, R. Klemmensen, and A. Nùrgaard, ªAttitudes toward immigration: The role of personal predispositions,º Political Psychology, vol. 37, 06 2014. 

- [19] K. Liew, A. H. Q. Koh, N. R. Fram, C. M. Brown, C. dela Cruz, L. L. Neng, R. Hennequin, A. E. Krause, and Y. Uchida, ªGroovin’ to the cultural beat: Preferences for danceable music represent cultural affordances for high-arousal negative emotions,º Dec 2020. [Online]. Available: psyarxiv.com/eqd8t 

- [20] K. Liew, H. Domae, A. H. Q. Koh, and Y. Uchida, ªEnergetic music is used for anger downregulation: A cross-cultural comparison,º In review. 

- [21] J. L. Ortega, ªCover versions as an impact indicator in popular music: A quantitative network analysis,º PLOS ONE, vol. 16, no. 4, pp. 1±18, 04 2021. [Online]. Available: https://doi.org/10.1371/journal. pone.0250212 

- [22] H.-M. Wang and S.-C. Huang, ªMusical rhythms affect heart rate variability: Algorithm and models,º Advances in Electrical Engineering, vol. 2014, 09 2014. 

304 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

- [23] Y. Matsumoto, R. Harakawa, T. Ogawa, and M. Haseyama, ªContext-aware network analysis of music streaming services for popularity estimation of artists,º IEEE Access, vol. 8, pp. 48 673±48 685, 2020. 

- [24] T. South, M. Roughan, and L. Mitchell, ªPopularity and centrality in Spotify networks: critical transitions in eigenvector centrality,º Journal of Complex Networks, vol. 8, no. 6, 03 2021, cnaa050. [Online]. Available: https://doi.org/10.1093/comnet/cnaa050 

- [25] D. Zinoviev, ªNetworks of music groups as success predictors,º CoRR, vol. abs/1709.08995, 2017. [Online]. Available: http://arxiv.org/abs/1709.08995 

- [26] P. Herrera and S. Streich, ªDetrended fluctuation analysis of music signals: Danceability estimation and further semantic characterization,º in Audio Engineering Society Convention 118, May 2005. [Online]. Available: http://www.aes.org/e-lib/browse. cfm?elib=13125 

   - [35] P. Collier, Exodus: How migration is changing our world. Oxford University Press, 2013. 

   - [36] V. Bove and L. Elia, ªMigration, diversity, and economic growth,º World Development, vol. 89, pp. 227±239, 2017. [Online]. Available: https://www.sciencedirect.com/science/article/ pii/S0305750X16304466 

   - [37] R. T. Dean, F. Bailes, and E. Schubert, ªAcoustic intensity causes perceived changes in arousal levels in music: An experimental investigation,º PLOS ONE, vol. 6, no. 4, pp. 1±8, 04 2011. [Online]. Available: https://doi.org/10.1371/journal.pone.0018591 

   - [38] G. Kim, ªKorean wave| between hybridity and hegemony in k-pop’s global popularity: A case of Ègirls’ generation’sämerican debut,º International Journal of Communication, vol. 11, no. 0, 2017. [Online]. Available: https://ijoc.org/index.php/ijoc/ article/view/6306 

- [27] D. Bogdanov, N. Wack, E. Gómez, S. Gulati, P. Herrera, O. Mayor, G. Roma, J. Salamon, J. Zapata, and X. Serra, ªEssentia: An open-source library for sound and music analysis,º in Proceedings of the 21st ACM International Conference on Multimedia, ser. MM ’13. New York, NY, USA: Association for Computing Machinery, 2013, p. 855±858. [Online]. Available: https://doi.org/10.1145/2502081.2502229 

- [28] 1. Introduction to ARPACK, pp. 1±7. [Online]. Available: https://epubs.siam.org/doi/abs/10.1137/1. 9780898719628.ch1 

- [29] M. E. J. Newman, ªModularity and community structure in networks,º Proceedings of the National Academy of Sciences, vol. 103, no. 23, pp. 8577±8582, 2006. [Online]. Available: https://www.pnas.org/doi/ abs/10.1073/pnas.0601602103 

- [30] A. Clauset, M. E. J. Newman, and C. Moore, ªFinding community structure in very large networks,º Phys. Rev. E, vol. 70, p. 066111, Dec 2004. [Online]. Available: https://link.aps.org/doi/10.1103/PhysRevE. 70.066111 

- [31] G. Csardi and T. Nepusz, ªThe igraph software package for complex network research,º InterJournal, vol. Complex Systems, p. 1695, 2006. [Online]. Available: https://igraph.org 

- [32] R Core Team, R: A Language and Environment for Statistical Computing, R Foundation for Statistical Computing, Vienna, Austria, 2020. [Online]. Available: https://www.R-project.org/ 

- [33] D. Bates, M. Mächler, B. Bolker, and S. Walker, ªFitting linear mixed-effects models using lme4,º Journal of Statistical Software, vol. 67, no. 1, pp. 1±48, 2015. 

- [34] T. Kamada, S. Kawai et al., ªAn algorithm for drawing general undirected graphs,º Information processing letters, vol. 31, no. 1, pp. 7±15, 1989. 

305 

