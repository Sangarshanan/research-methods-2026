---
paper_id: "000034"
year: 2022
title: "Download pdf"
source_url: "https://zenodo.org/record/7316652/files/000034.pdf"
---

# TRACES OF GLOBALIZATION IN ONLINE MUSIC CONSUMPTION PATTERNS AND RESULTS OF RECOMMENDATION ALGORITHMS 

Oleg Lesota<sup>1,2</sup> Emilia Parada-Cabaleiro<sup>1,2</sup> Stefan Brandl<sup>1</sup> Elisabeth Lex<sup>3</sup> Navid Rekabsaz<sup>1,2</sup> Markus Schedl<sup>1,2</sup> 

1Multimedia Mining and Search Group, Institute of Computational Perception, JKU Linz, Austria 2Human-centered AI Group, AI Lab, Linz Institute of Technology (LIT), Austria 

3 Graz University of Technology, Austria 

markus.schedl@jku.at 

## ABSTRACT 

Music streaming platforms allow users to enjoy music from all over the globe. Such opportunity speeds up cultural exchange between different countries, a process often associated with globalization. While such an exchange could lead to more diverse music consumption, empirical evidence on its influence on online music consumption is limited. Besides, the extent to which music recommender systems foster exchange or amplify globalization in music remains an understudied problem. 

In this paper, we present findings from an empirical study to detect traces of globalization in domestic vs. foreign online music consumption. Besides, we investigate if popular recommendation algorithms, specifically ItemKNN and NeuMF, are prone to amplifying globalization processes. Our experiments on Last.fm listening data show nuanced patterns of globalization in music consumption. We observe a strong position of US music in all considered countries. In countries such as Sweden, Great Britain, or Brazil, US music shows various levels of coexistence with domestic music. We find that Finland is least influenced by US music, while greatly consuming and ªexportingº domestic music. With respect to recommendation algorithms, ItemKNN tends to recommend domestic music to users of many countries, while NeuMF contributes to accelerating globalization and shifting balance towards dominance of US music on the market. 

## 1. INTRODUCTION AND RELATED WORK 

Globalization can be defined as an ªexpanding cultural exchange between countries, which may imply an increasing consumption of foreign cultural goods beside the local onesº [1]. Among others, previous research proposes two interpretations of globalization: (i) Cultural Imperialism 

© O. Lesota, E. Parada-Cabaleiro, S. Brandl, E. Lex, N. Rekabsaz, and M. Schedl. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: O. Lesota, E. Parada-Cabaleiro, S. Brandl, E. Lex, N. Rekabsaz, and M. Schedl, ªTraces of Globalization in Online Music Consumption Patterns and Results of Recommendation Algorithmsº, in Proc. of the 23rd Int. Society for Music Information Retrieval Conf., Bengaluru, India, 2022. 

[2], i. e., the growing cultural exchange triggered by globalization is mostly profitable for certain dominant western cultures (in particular American culture) and thereby threatens to overwhelm the others; and (ii) Glocalization [1, 3], i. e., fostering the development of local cultures through the globalization process, by means of adaptation of global cultural forms and strengthening local identity as a counterbalancing mechanism against global influences. These interpretations imply that globalization exposes local cultures to pressure from global trends, and while some of them adapt and confront the threat, others weaken and decline. 

The realizations of these interpretations in various domains have been confirmed by several studies. For instance, Crane [2] shows the dominance of US film industry in most regions of the world, while Chen and Shen [4] display the ability of some cultures to adapt and develop under the pressure of more dominant ones. Approaching globalization, most of the previous works resort to the analysis of various aggregated popular charts representing mainstream consumption trends [1, 5±7]. Specifically, Achterberg [1] show that US music has become increasingly popular in the Netherlands, Germany, and France until the late 1980s’, while starting in the 90s’, more local music has been produced. The revival of domestic music consumption is also evidenced by Bekhuis et al. [6], who show that popularity of domestic artists is positively correlated with a high sentiment of national pride. Similarly, Verboord and Brandellero [7] conduct a multilevel analysis of popcharts’ evolution, showing that the consumption of foreign music has increased in many countries except in the US. 

The mentioned studies conduct the analysis on aggregated pop-music charts, neglecting the nuances of music consumption by the consumers with less mainstream tastes. Including less-mainstream listeners in countryspecific analyses is particularly important, as listeners in different countries display diverse tendencies towards listening to mainstream music [8], which also gets translated into significant differences in the performance of recommendation algorithms [9, 10]. However, to the best of our knowledge, little research has been dedicated to investigate the influence of streaming platforms on globalization processes [5]. Furthermore, the extent to which existing globalization processes might be amplified by music rec- 

291 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

ommender systems has, to the best of our knowledge, not yet been investigated. 

To bridge these gaps, we leverage online music listening data, allowing us to analyze globalization patterns based on actual per-user consumption of music from a wider range of countries. In addition, we study potential impacts music recommender systems may have on globalization. To this end, we strive to answer the following three research questions: 

- RQ1: How prominent is the aspect of US ªcultural imperialismº in the sphere of online music consumption? Is its influence uniform across countries? 

- RQ2: How significant is domestic music consumption in different countries? Are there any signs of ªglocalizationº? 

- RQ3: Do music recommender systems influence users’ inclination towards music coming from certain countries? 

We highlight the importance of RQ3, considering recent research showing that recommender systems can amplify biases from underlying data in their output, as well as inflict additional algorithmic biases. An overview of biases recommender systems are prone to is given in [11,12]. Among them is popularity bias, i. e., the tendency to favor popular items at the expense of niche and less popular items, often leading to dissatisfaction of users [13,14]. We pose RQ3 to investigate possible occurrence of analogous ªglobalization biasº in recommender systems. 

The remainder of the paper is structured as follows. Section 2 describes our methodological approach to the research questions, including data and methods used. We report and analyze our results in Section 3. Section 4 is dedicated to limitations of our study. Finally, we sum up our findings and list potential future directions in Section 5. 

## 2. METHODS AND MATERIALS 

In the following, we detail the methodology we adopt to answer the research questions and describe the dataset our analysis is based upon. We first clarify and formally define the terminology we use in the methodological description: A listening event (or interaction) is a tuple < u, i >, indicating that a user u consumed an item i, which is a music track or a song in our case. Each track i has been created or performed by an artist a.<sup>1</sup> Each artist a originates from a country ca. Each user u is from a country cu. Icu denotes the set of all user±item interactions made by users in country cu. Ica refers to the set of all interactions with items created by artists from country ca. Ica,cu denotes the set of all interactions with items created by artists from country ca, listened to by users from country cu. 

## 2.1 Investigating US Cultural Imperialism 

To answer RQ1, we compute, for all users in a given fixed country cu, their aggregate share of consumed music that 

> 1 Being aware that ªartistº in the context of music can refer to different subjects, we adopt a pragmatic definition here. Owed to the type of usergenerated data we investigate in our study, we consider both composers and performers as artists. 

has been created by artists from each country under consideration. Since we are interested in this share for local and US music (artists), we define the following function 



<!-- Start of picture text -->
ICcu→ca = | Ica , cu |<br>|Icu |<br><!-- End of picture text -->

for which we consider three cases: 



<!-- Start of picture text -->
• Local: ca = cu,<br><!-- End of picture text -->



<!-- Start of picture text -->
• US: ca = US, and<br>• Other: � ICcu→ca , where C is the set of<br>ca∈C\{cu,US}<br>all countries considered (sum over all artist countries<br>that are not the local country nor the US).<br><!-- End of picture text -->

In simple words, this formal framework can answer how much of the music all users in country cu consume was created by artists from the same country (local consumption), was created by artists from the US, and was created by artists from other countries (neither local nor the US); all expressed in relative numbers. 

## 2.2 Investigating Traces of Glocalization 

To answer RQ2, we consider all listening events of songs by artists from the country under investigation, i. e., we fix ca. We then define ICcu←ca , analogously to ICcu→ca above, i. e., for a given country ca, the share of its artists’ listening events that originate from users in each country cu under investigation. 



<!-- Start of picture text -->
ICcu←ca = | Ica , cu |<br>|Ica |<br><!-- End of picture text -->

Here we are mostly interested in this share between local and foreign music consumers, and accordingly consider two cases: 



<!-- Start of picture text -->
• Local: cu = ca, and<br>• Other: � ICcu←ca , where C is the set of<br>cu∈C\{ca}<br><!-- End of picture text -->

all countries considered (sum over all user countries that are not the local country). 

In simple words, this formal framework can answer how much of the music created by artists from ca is consumed by users in the same country (local consumption of local artists), and how much by users in other countries; all expressed in relative numbers. 

## 2.3 Influence of Recommendation Algorithms on Globalization Patterns 

To approach RQ3, we consider two popular recommendation algorithms, a classical ItemKNN [15] and a more recent, deep-learning-based NeuMF [16]. ItemKNN assigns a recommendation score to an item for a given user based on how similar this item is to the items already consumed by the user. Similarity is computed based on the interactions of other users. This algorithm does not learn any special representations for users and items, operating directly on the interaction matrix. On the other hand, NeuMF is a matrix factorization approach. Not only does it learn user and item embeddings, but also a dedicated scoring 

292 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

|Country|Tracks|Users|Artists|Intera<br>Users|ctions<br>Artists|
|---|---|---|---|---|---|
|US|252,370|1,763|15,440|2,057,684|6,607,441|
|GB|99,911|890|5,271|1,095,637|2,767,202|
|DE|42,799|890|3,077|1,012,806|697,866|
|SE|29,108|348|1,970|393,348|672,944|
|CA|24,005|232|1,565|304,817|594,868|
|FR|17,718|281|1,815|337,739|357,730|
|AU|14,770|208|1,306|261,965|343,892|
|FI|14,673|448|1,093|508,934|286,145|
|BR|14,091|1,138|1,022|1,312,909|232,640|
|RU|11,779|1,288|848|1,202,064|155,409|
|JP|11,731|115|1,228|92,459|143,203|
|NO|11,282|224|765|256,921|238,427|
|PL|11,145|1,121|883|1,249,746|186,032|
|NL|10,958|406|1,018|573,307|186,117|
|IT|9,633|252|1,058|237,708|131,769|
|ES|6,115|257|765|297,364|71,862|
|BE|4,204|141|586|166,247|64,765|
|MX|2,881|213|323|295,140|33,887|
|UA|1,849|317|160|348,706|27,339|
|TR|1,478|115|286|113,165|14,868|
|Other|44,736|2,228|4,947|2,521,335|825,595|
|Total|637,236|12,875|45,426|14,640,001|14,640,001|



Table 1: Basic statistics of the dataset. For each country, we report the number of users, tracks, artists, and interactions made by all users in the country as well as interactions made to artists from the country. 

function, thanks to the multi-layer perceptron constituting a part of the model. 

To estimate potential influence of the recommender algorithms on globalization patterns in different countries, we train them on subsamples of the dataset used to answer RQ1 and RQ2, and then analyze the recommendations they produce. To this end, we consider top 10 recommendations provided to each user and then calculate ICcu→ca for cu = ca and ca = US exactly like for RQ1. 

Because the dataset under investigation contains a large number of items (see Table 1), we use its subsamples (containing around 100K items each) to run recommendation experiments, thereby avoiding computational limitations. For the subsamples, we enforce the following standard limitations: every track has to be interacted with at least 5 times and every user is required to have at least 5 interactions. To ensure robustness of the results, we conduct the experiment on three such random subsamples and report average recommendation levels. 

## 2.4 Dataset 

We conduct our experiments on the LFM-2b dataset [17] of listening events created by users of the online music platform Last.fm.<sup>2</sup> Unlike stand-alone streaming services such as Spotify or Deezer, Last.fm is based on the concept of ªscrobblingº, meaning that its users can share on the platform which music they are listening to, regardless of the actual service, device, or application they are using for music consumption. Therefore, Last.fm can be regarded as an aggregator that reflects the entire music consumption history of its users. This is desirable for our analysis since 

we aim at capturing in a more comprehensive way each listener’s (and country’s) music consumption behavior instead of focusing on one particular streaming platform. 

The full LFM-2b dataset contains listening histories of ∼120K users, totaling to ∼2B interactions. Since the dataset’s temporal coverages spans 15 years, from 2005 to 2020, and we intentionally leave out aspects of temporal dynamics from our analysis (see future work), we only consider a subset covering the years 2018-2019. Furthermore, we exclude potentially accidental interactions by removing listening events <u, i> that only occurred once.<sup>3</sup> Since our analysis necessitates country information of both users and artists, we first remove all users for which no such information is available in LFM-2b. We then collect information about artists’ country from Musicbrainz<sup>4</sup> and only retain those artists for whom country data could be retrieved. After these steps we end up with a dataset of ∼14,640K interactions triggered by ∼13K users from 143 countries with ∼637K music tracks produced by ∼45K artists from 155 countries. 

Finally, to reduce the complexity of the analysis and concentrate on reasonably represented countries, we select for the detailed analyses countries with at least 100 users and only countries whose artists created at least a total of 1,000 tracks. These filtering steps result in 20 countries<sup>5</sup> from all over the world (see Table 1 for basic statistics), which we further analyze. Note that the countries beyond these 20 still contribute to the results mentioned as a part of the aggregation over ªotherº countries. 

## 3. RESULTS 

We illustrate our findings with a series of figures. Figure 1 shows how popular is domestic music, music produced by US artists, and music produced by artists from other countries in every of the 20 investigated countries. In case of DE, a little under 40% of listening events generated by German users are allocated to music produced by US artists (orange bar on the left). Under 20% of listening events generated by them is allocated to domestic music, i. e., produced by German artists (blue bar on the right). Figure 2 indicates the degree to which domestic music of different countries is consumed in the country of origin and outside. For example, BR has most of the listening events allocated to its domestic music coming from Brazilians, showing that it is not as popular in other countries. Figure 4 shows the spread of listening interactions with music from every country across other countries. In other words, this matrix shows how uniform the ªexportº of domestic music from every country to other countries is. Every row 

> 3 Since the dataset provides no information about the duration of a listening event, those single user±item interactions are often the result of a recommender engine starting to play a new track to the user, which the user skips after a few seconds. Therefore, we exclude those single interactions to remove this kind of noise. 

> 4 https://musicbrainz.org 

> 5 Throughout the paper, we use ISO codes to abbreviate countries. US: United States, GB: United Kingdom, DE: Germany, SE: Sweden, CA: Canada, FR: France, AU: Australia, FI: Finland, BR: Brazil, RU: Russia, JP: Japan, NO: Norway, PL: Poland, NL: Netherlands, IT: Italy, ES: Spain, BE: Belgium, MX: Mexico, UA: Ukraine, TR: Turkey 

2 https://last.fm 

293 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
US music other domestic music domestic consumption foreign consumption<br>1. 0<br>av g<br>C A<br>A U 0. 8<br>G B<br>B R<br>0. 6<br>I T<br>N O<br>N L 0. 4<br>M X<br>E S 0. 2<br>F R<br>B E<br>S E 0. 0<br>CA AU JP BE NO FR SE GB NL IT US UA ES DE FI MX TR RU PL BRavg<br>J P<br>Artist Country<br>U A<br>D E Figure 2: Consumption distribution of music produced in<br>RP UL different countries, between local (blue) and international<br>T R (gray) audiences.<br>F I<br>U S<br>0.0 0.2 0.4 0.6 0.8 1.0 CA, NL, IT, and UA. Forth, some countries such as GB,<br>Proportion of Interactions<br>Proportion of Interactions<br>User Country<br><!-- End of picture text -->

CA, NL, IT, and UA. Forth, some countries such as GB, BR, and SE show above-average consumption of US music combined with also above-average consumption of domestic music. This is an indication of local musical culture comfortably coexisting and possibly interacting with the incoming US culture. Fifth, other countries such as TR, PL, FI, and RU consume below average of US music, remaining more open for music coming from other countries. In addition, FI also displays significant attention to domestic music. 

Figure 1: Distribution of listening activity over foreign (US and other) and domestic music. Every row corresponds to listeners of one country. Average proportions of interactions with music produced in the US (orange) and domestically (blue) are shown in the first row. 

corresponds to the share, among all listening interactions, of the music produced in a single country. Every cell in the row shows the percentage of listening events coming from listeners of the corresponding country on the x-axis. For example, we can observe that 14.6% of listening interactions with JP music comes from US users (row JP, column US). Figure 3 demonstrates the potential impact two recommendation algorithms, ItemKNN and NeuMF, may have on the consumption balance in different countries. In each of the two subplots, empty bars reflect proportions of music actually consumed by the users (similar to Figure 1): orange bars on the left indicate listening events allocated to US artists, blue bars on the right refer to domestic artists. The filled bars illustrate the same concept applied to items recommended to users of different countries. For example, in Figure 3b, the row corresponding to DE shows that about 50% of items recommended to German users come from US artists, while at the same time only about 40% of their actual listening activity belongs to tracks from US. 

From these observations, we conclude that music produced by US artists maintains strong positions in the considered countries. In particular, it dominates its own domestic market unlike domestic music of other countries. While there are countries combining low consumption of domestic with high consumption of US music, it is hard to call US music globally dominating. Many regions are also comparably influenced by other countries (if combined) and some, like FI or GB, show very strong positions of domestic artists. Thus, we hesitate to call US ªcultural imperialismº absolute and homogeneous across countries. 

We approach RQ2 by defining three indicators related to domestic music in every country: international consumption, i. e., how big is the proportion of interactions with its domestic music coming from other countries (in other words, how widely exported domestic music is, see Figure 2 and 4); domestic popularity, i. e., the proportion of interactions from listeners of the country with domestic music (how popular domestic music is in its home region, see Figure 1); popularity of US music (used to detect hints of cultural dialog between US and considered country, see Figure 1). We analyze these indicators in terms of below/above average across considered countries for every particular country. 

We make the following observations answering RQ1. First, from the listening activity on Last.fm in 2018-2019, we see that 39.6% of all items interacted with were produced by US artists. Second, as Figure 1 shows, over 60% of listening events generated by US users are allocated to domestic music (bottom row, blue bar). This marks domestic superiority of US music, unmatched by any other country. The runner-up, being GB, shows only about 30% of listening events allocated to the domestic market. Third, on average, listeners of considered countries allocate 40% of their consumption to music produced by US artists (top row and vertical red line), with a maximum of about 50% shown by Australia and Canada. For many countries, above-average consumption of US music is combined with below-average consumption of domestic music, e. g., AU, 

Using the indicators described above, we identify four patterns in behavior of domestic music scenes. First, glocalization through adaptation. Countries such as SE and GB score above average on all three indicators: their music is appreciated abroad while also being popular locally, and in addition these countries consume above average US music. We interpret this pattern as comfortable coexistence of global and domestic cultures with the latter likely adapt- 

294 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
rec. US music rec. domestic rec. US music rec. domestic<br>con. US music con. domestic con. US music con. domestic<br>av g av g<br>C A C A<br>A U A U<br>G B G B<br>B R B R<br>I T I T<br>N O N O<br>N L N L<br>M X M X<br>E S E S<br>F R F R<br>B E B E<br>S E S E<br>J P J P<br>U A U A<br>D E D E<br>P L P L<br>R U R U<br>T R T R<br>F I F I<br>U S U S<br>0.0 0.2 0.4 0.6 0.8 1.0 0.0 0.2 0.4 0.6 0.8 1.0<br>Proportion of Interactions Proportion of Interactions<br>(a) Impact of ItemKNN (b) Impact of NeuMF<br>User Country User Country<br><!-- End of picture text -->

Figure 3: Potential impact of recommender algorithms on music consumption balance in different countries. Empty boxes reflect actual consumption (denoted con.) extracted from the data. Filled boxes represent the output the two recommender algorithms produce (denoted rec.). Orange-tinted boxes on the left correspond to consumed / recommended music from US. Blue-tinted on the right - consumed / recommended domestic music. 

ing and contributing to the former. Second, heavier adaptation of global trends. Domestic music is popular in BR as well as US music (both indicators above average). Domestic BR music receives most of its interactions from BR and little international attention. This pattern may imply even heavier adaptation of global influences to domestic circumstances. Third, non-US influenced. Countries such as PL, TR, and RU score below average on all three indicators: their music is predominantly consumed on domestic market while being less popular than US-produced music (which in turns enjoys below average popularity in these countries). We interpret this combination in a way that in these countries domestic music competes with a wide array of incoming music and US music is not necessarily the strongest influence there. Fourth, as the sole representative of this pattern, FI demonstrates high popularity of domestic music, combined with decent international consumption and lower popularity of US music. This pattern may express successful adaptation of less mainstream (beyond US) influences as well as strong distinct national culture. 

We answer RQ3 by analyzing results of the recommendation experiment detailed in Section 2.3. As shown in Figure 3b, NeuMF consistently recommends more USproduced items to listeners of every non-US country than these non-US listeners used to consume. This happens at the expense of the share of recommended domestic items. The character of the change implies that the share of recommended items from other countries is also larger than their actual consumption share (for all countries). We conclude that NeuMF amplifies globalization patterns and in 

particular dominance of an already dominant player, i. e., the US. On the contrary, ItemKNN (see Figure 3a) shows a different and less consistent behavior. Listeners in JP, TR, IT, and FI are recommended a considerably bigger share of domestic tracks than the share of listening events they actually allocate to domestic music. Interestingly, the shares of US music recommended to users in these four countries is lower than the share of US music consumed by them. The average share of recommended US tracks (see top row and red vertical line) is very close to the share of attention US music actually receives. On average, ItemKNN shows less changes than NeuMF. These observations are in line with the results of [14] where ItemKNN shows most calibrated recommendation results in terms of track popularity, especially when compared to methods with a higher number of trainable parameters, such as ALS and Variational Autoencoders. Our experiment shows that music recommendation algorithms can considerably contribute to the process of globalization, and the exact contribution largely depends on the algorithm. Therefore, recommender system designers need to be aware of such potential impacts. 

## 4. LIMITATIONS 

While our analysis captures listeners’ behavior beyond pop charts, it bears a number of limitations. First, the data we base our analysis upon reflects a particular audience: Last.fm users (likely active internet and social media users), and therefore might not be representative of the population at large. Some countries and social groups are underrepresented on Last.fm (e. g., female users). In some 

295 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
U S 1 9.3 8.0 6.1 2.4 2.5 2.1 2.1 2.6 9.0 6.9 0.6 1.7 7.3 3.8 1.6 1.9 1.0 1.9 2.1 0.6<br>G B 1 1.1 10.8 6.0 2.3 1.8 2.3 1.6 2.8 8.0 8.5 0.7 1.7 9.1 4.5 1.9 2.1 1.1 2.1 2.4 0.8<br>D E 6.3 4.5 24.2 2.4 1.3 2.2 1.0 3.3 4.6 10.7 0.4 1.3 8.1 3.2 1.1 2.0 1.1 1.3 2.7 0.8<br>S E 8.4 5.0 7.7 9.5 1.6 2.3 1.2 6.1 5.6 9.4 0.4 2.3 8.4 3.4 1.2 2.3 1.1 1.3 3.2 0.9<br>C A 1 7.4 7.8 6.4 2.7 4.2 2.3 2.1 2.7 8.4 7.3 0.6 1.7 7.3 3.9 1.5 1.8 1.1 2.0 2.1 0.6<br>F R 9.8 5.5 5.9 2.5 1.5 8.7 1.4 3.0 6.0 9.0 0.6 2.0 9.8 3.8 1.6 2.1 2.3 2.4 2.5 1.4<br>A U 1 2.5 7.8 6.8 2.4 2.2 2.1 6.0 2.7 7.9 7.4 0.6 1.7 8.8 4.3 1.2 1.9 1.2 2.0 2.4 0.6<br>F I 5.4 2.7 6.3 1.7 1.4 1.7 0.6 30.5 3.9 10.1 0.4 0.8 6.4 3.1 0.7 1.9 0.8 1.3 3.3 0.7<br>B R 2.7 1.2 1.4 0.3 0.4 0.7 0.3 0.8 79.6 1.4 0.2 0.3 1.4 1.2 0.6 0.5 0.5 0.6 0.3 0.2<br>R U 2.4 1.4 2.0 0.5 0.4 0.5 0.3 1.3 1.9 55.9 0.2 0.6 3.0 0.9 0.3 0.5 0.2 0.6 8.9 0.3<br>J P 1 4.6 6.7 5.4 2.2 2.0 3.1 1.4 4.8 8.1 8.1 7.3 1.3 6.8 2.4 1.0 1.6 1.4 2.8 1.8 0.4<br>N O 8.3 5.1 6.2 3.6 1.6 2.7 1.5 5.3 4.8 8.3 0.5 8.6 8.9 5.0 1.4 2.1 1.3 1.2 2.6 1.0<br>P L 2.9 2.4 2.4 1.1 0.5 1.0 0.4 2.0 1.8 4.0 0.3 0.7 65.7 1.2 0.4 0.8 0.5 0.5 1.3 0.5<br>N L 7.8 5.2 7.8 2.7 1.5 2.2 0.9 4.2 6.8 8.7 0.5 1.8 8.9 13.4 0.8 1.5 1.6 1.5 3.1 1.1<br>I T 7.4 4.9 6.7 2.3 1.3 2.2 1.1 3.8 6.3 8.8 0.5 1.3 8.6 3.6 15.3 2.5 1.3 1.9 2.0 1.1<br>E S 7.0 4.6 4.5 1.5 0.8 1.5 0.7 1.9 5.4 4.9 0.4 0.8 6.0 2.7 1.3 23.3 0.9 10.2 1.2 0.6<br>B E 7.2 4.4 7.2 2.3 1.4 5.2 0.9 2.3 4.9 8.5 0.4 1.7 10.4 9.0 1.5 2.0 8.4 1.3 2.5 1.5<br>M X 7.3 2.4 3.2 1.3 0.9 0.9 0.4 1.0 9.6 4.4 0.1 0.6 2.7 1.7 0.5 3.6 0.2 40.5 0.7 0.2<br>U A 4.6 2.0 3.3 1.3 0.8 1.7 1.2 3.1 2.4 26.1 0.2 0.9 5.5 2.4 0.4 1.3 0.8 0.9 22.1 0.8<br>T R 4.7 2.2 4.1 1.4 0.3 1.1 0.4 1.4 2.1 3.5 0.0 0.6 5.6 2.4 0.3 0.5 0.7 0.9 0.7 54.5<br>av g 8.4 4.7 6.2 2.3 1.4 2.3 1.3 4.3 9.4 10.6 0.7 1.6 9.9 3.8 1.7 2.8 1.4 3.9 3.4 3.4<br>US GB DE SE CA FR AU FI BR RU JP NO PL NL IT ES BE MX UA TR<br>Listener Country<br>Artist Country<br><!-- End of picture text -->

Figure 4: Music export matrix. Every cell shows the proportion of interactions with music from a given artist country allocated to users from a given listener country. For instance, 19.3% of all the music created by US artists is consumed by US listeners, while 14.6% of interactions with the entirety of Japanese music are made by US users. 

countries Last.fm is not very popular and their listeners are likely to use different channels of music consumption. Therefore, our dataset may overrepresent listeners who are open to and interested in global culture, in particular in countries where Last.fm is not popular. Furthermore, the data gathered in the LFM-2b dataset are already affected by recommender systems of different platforms users connect to their Last.fm accounts, which means that our insights about ªactual music preferenceº can be, to a certain degree, distorted. 

## 5. CONCLUSION AND FUTURE WORK 

We addressed three research questions related to patterns of music consumption on online music platforms. Regarding the dominance of US vs. domestic music (RQ1), we found that the former maintains strong positions in all considered countries. However, the US does not display signs of absolute and homogeneous ªcultural imperialismº. While it dominates its domestic market, in other countries, US music shows various levels of coexistence with domestic music. While some countries such as Australia and Canada find their domestic music competing with US music, others, such as Great Britain, Brazil, and Sweden, display high consumption levels of both US and domestic music. Countries like Finland and Germany, on the other hand, are open to music both from other countries and domestically created. 

Looking for traces of glocalization (RQ2), we distin- 

guish several ways domestic music can behave under the pressure of global cultural trends. Music from countries like Great Britain and Sweden shows signs of adaptation of global cultural trends, with their music coexisting with US music and being greatly listened to outside their domestic markets. Music from Brazil appears to be highly influenced by global trends but mostly consumed locally. Countries like Poland and Turkey also display signs of their music being localized and influenced by global trends, however, to a lesser extent influenced by US music than others. Finland combines competitive ªexportº of their music with high local consumption and relatively low consumption of US music, showing signs of a strong and distinctive musical culture. 

Finally, we show that recommender systems may have a considerable impact on globalization patterns (RQ3). We investigate this for a traditional ItemKNN approach and the deep-learning-based NeuMF algorithm. While the former fosters consumption of local music in most of the considered countries, the latter supports internationalization and, in particular, cultural imperialism of the US. 

Directions for future research include temporal analysis of consumption trends over the 15-year-span covered by the LFM-2b dataset, in particular considering possible alterations caused by the global pandemic [18, 19]. Other directions include exploring the link between globalization amplification and popularity bias, and investigating the effectiveness of different mitigation strategies. 

296 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

## 6. ACKNOWLEDGMENTS 

This research was funded in part, by the Austrian Science Fund (FWF) [P33526] and [DFH-23]; as well as by the State of Upper Austria and the Federal Ministry of Education, Science, and Research, through grant LIT-2020-9SEE-113 and LIT-2021-YOU-215. 

## 7. REFERENCES 

- [1] P. Achterberg, J. Heilbron, D. Houtman, and S. Aupers, ªA cultural globalization of popular music? American, Dutch, French, and German popular music charts (1965 to 2006),º American Behavioral Scientist, vol. 55, no. 5, pp. 589±608, 2011. 

- [2] D. Crane, ªCultural globalization and the dominance of the American film industry: Cultural policies, national film industries, and transnational film,º International Journal of Cultural Policy, vol. 20, no. 4, pp. 365±382, 2014. 

- [3] M. Castells, The power of identity. Malden, MA, USA: Blackwell, 1997. 

- [4] X. Chen and S. Shen, ªReview of the impact of cultural imperialism in the context of globalization to the film industry,º in Proc. of the International Conference on Language, Art and Cultural Exchange. Luoyang, China: Atlantis Press, 2021, pp. 205±212. 

- [5] P. Bello and D. Garcia, ªCultural divergence in popular music: the increasing diversity of music consumption on spotify across countries,º Humanities and Social Sciences Communications, vol. 8, no. 1, pp. 1±8, 2021. 

- [6] H. Bekhuis, M. Lubbers, and W. Ultee, ªA macrosociological study into the changes in the popularity of domestic, European, and American pop music in western countries,º European Sociological Review, vol. 30, no. 2, pp. 180±193, 2014. 

- [7] M. Verboord and A. Brandellero, ªThe globalization of popular music, 1960-2010: A multilevel analysis of music flows,º Communication Research, vol. 45, no. 4, pp. 603±627, 2016. 

- [8] C. Bauer and M. Schedl, ªGlobal and country-specific mainstreaminess measures: Definitions, analysis, and usage for improving personalized music recommendation systems,º PLOS ONE, vol. 14, no. 6, pp. 1±36, 2019. 

- [9] G. Vigliensoni and I. Fujinaga, ªAutomatic music recommendation systems: Do demographic, profiling, and contextual features improve their performance?º in Proc. of the International Society for Music Information Retrieval Conference. New York, NY, USA: ISMIR, 2016, pp. 94±100. 

- [10] D. Kowald, P. Müllner, E. Zangerle, C. Bauer, M. Schedl, and E. Lex, ªSupport the underground: Characteristics of beyond-mainstream music listeners,º EPJ Data Science, vol. 10, no. 1, pp. 1±26, 2021. 

- [11] A. Ashokan and C. Haas, ªFairness metrics and bias mitigation strategies for rating predictions,º Information Processing & Management, vol. 58, no. 5, pp. 1± 18, 2021. 

- [12] J. Chen, H. Dong, X. Wang, F. Feng, M. Wang, and X. He, ªBias and debias in recommender system: a survey and future directions (2020),º arXiv preprint arXiv:2010.03240, 2020. 

- [13] H. Abdollahpouri, M. Mansoury, R. Burke, B. Mobasher, and E. C. Malthouse, ªUser-centered evaluation of popularity bias in recommender systems,º in Proc. of the Conference on User Modeling, Adaptation and Personalization. Utrecht, the Netherlands: ACM, 2021, pp. 119±129. 

- [14] O. Lesota, A. Melchiorre, N. Rekabsaz, S. Brandl, D. Kowald, E. Lex, and M. Schedl, ªAnalyzing item popularity bias of music recommender systems: Are different genders equally affected?º in Proc. of the Conference on Recommender Systems. Amsterdam, the Netherlands: ACM, 2021, pp. 601±606. 

- [15] M. Deshpande and G. Karypis, ªItem-based top-N recommendation algorithms,º ACM Transactions on Information Systems - TOIS, vol. 22, pp. 143±177, 2004. 

- [16] X. He, L. Liao, and H. Zhang, ªNeural collaborative filtering,º Proc. of the International Conference on World Wide Web, pp. 173±182, 2017. 

- [17] M. Schedl, S. Brandl, O. Lesota, E. Parada-Cabaleiro, D. Penz, and N. Rekabsaz, ªLfm-2b: A dataset of enriched music listening events for recommender systems research and fairness analysis,º in Proc. of Conference on Human Information Interaction and Retrieval. Regensburg, Germany: ACM SIGIR, 2022, pp. 337±341. 

- [18] N. C. Hansen, J. M. G. Treider, D. Swarbrick, J. S. Bamford, J. Wilson, and J. K. Vuoskoski, ªA crowdsourced database of coronamusic: Documenting online making and sharing of music during the covid-19 pandemic,º Frontiers in Psychology, vol. 12, pp. 1±9, 2021. 

- [19] M. Liu, E. Zangerle, X. Hu, A. Melchiorre, and M. Schedl, ªPandemics, music, and collective sentiment: Evidence from the outbreak of covid-19,º in Proc. of the International Society for Music Information Retrieval Conference. Virtual: ISMIR, 2020, pp. 157±165. 

297 

