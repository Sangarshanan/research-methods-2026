---
paper_id: "000070"
year: 2022
title: "Download pdf"
source_url: "https://zenodo.org/record/7316730/files/000070.pdf"
---

# TOWARDS QUANTIFYING THE STRENGTH OF MUSIC SCENES USING LIVE EVENT DATA 

Andrew McGraw University of Richmond 

Michael Zhou Columbia University 

mgz2112@columbia.edu amcgraw@richmond.edu 

Douglas R. Turnbull Ithaca College 

dturnbull@ithaca.edu 

## ABSTRACT 

There are many benefits for a community when there is a vibrant local music scene (e.g., increased mental & physical well-being, increased economic activity) and there are many factors that contribute to an environment in which a live music scene can thrive (e.g., available performance spaces, helpful government policies). In this paper, we explore using an estimate of the live music event rate (LMER) as a rough indicator to measure the strength of a local music scene. We define LMER as the number of music shows per 100,000 people per year and then explore how this indicator is (or is not) correlated with 28 other socioeconomic indicators. To do this, we analyze a set of 308,051 music events from 2019 across 1,139 cities in the United States. Our findings reveal that factors related to transportation (e.g., high walkability), population (high density), economics (high employment rate), age (high proportion of individuals age 20-29), and education (bachelor’s degree or higher) are strongly correlated with having a high number of live music events. Conversely, we did not find statistically significant evidence that other indicators (e.g., racial diversity) are correlated. 

## 1. INTRODUCTION 

Certain American cities such as Los Angeles and New York City are famous for having great music scenes. However, there are hundreds of small, medium, and large cities around the country that support vibrant music scenes. These cities often have well-known venues like the Grand Ole Opry in Nashville, TN, or put on large music festivals such as SXSW in Austin, TX. They can be associated with artists who obtain some level of regional, national, or international fame such as Minneapolis, MN with Prince and Asbury Park, NJ with Bruce Springsteen. They sometimes become historically connected with specific genres as in New Orleans, LA with jazz, Seattle, WA with grunge, and Asheville, NC with bluegrass. 

There have been many studies that detail the ways in which music scenes can benefit their communities by en- 

> © M. Zhou, A. McGraw, and D. Turnbull. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: M. Zhou, A. McGraw, and D. Turnbull, ªTowards Quantifying the Strength of Music Scenes using Live Event Dataº, in Proc. of the 23rd Int. Society for Music Information Retrieval Conf., Bengaluru, India, 2022. 

hancing social bonding, improving emotional well-being [1,2], and increased economic activity [3±15]. Researchers have also studied factors that can help foster an environment in which a local music scene can develop and thrive [4, 5, 8, 9, 11, 12, 16±22]. These factors include having a rich music history, having strong support for music education, and government regulations that are favorable for live performance (see Section 2 for details). 

Investment by government and non-government organizations (e.g., Chambers of Commerce, Arts Councils) are associated with strong music scenes (ªmusic havensº) to both further develop these havens as well as help cities with underdeveloped music scenes (ªmusic desertsº) [11]. Many organizations have produced extensive reports [19] about ªmusic citiesº based on interviews and surveys of cities around the world (e.g., Austin, USA [3], London, UK [23], Victoria, AU [24]). While these reports produce valuable and transferable knowledge, they tend to be narrow in their geographic focus (i.e., one city or region). To complement this body of work, we propose a quantitative approach that uses the live music event rate (LMER) to estimate the relative strength of a local music scene. We argue that this simple statistic is straightforward to calculate, easy to interpret, and useful. 

In this work, we introduce a music event dataset that contains information for 308,051 live music events that took place in 1,139 American cities during 2019. Here we consider an event as a live performance by one or more artists at a venue (e.g., bar, concert hall, festival) on a given date. This dataset was collected for music event recommendation application and combines event information that was collected from BandsInTown<sup>1</sup> and Facebook<sup>2</sup> . While this dataset has a number of limitations (e.g., only music events with a digital footprint, data collected using snowball sampling), it allows us to calculate a rough estimate of LMER for each city to enable comparison. 

In this paper, we explore how our estimated LMER is (or is not) correlated with 28 socioeconomic indicators across 6 different categories: transportation, population, economics, age, education, and race. These indicators are closely related to some of the factors (e.g., transportation convenience, population density) that other researchers have suggested are important factors for fostering healthy music scenes. 

In Section 2, we explore existing research on the ben- 

> 1 https://www.bandsintown.com/ 

> 2 https://www.facebook.com/ 

583 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

|Benefits of Music Communities|Factors that Create a Strong Music Community|
|---|---|
|Job creation [3,4,11,12]|Availability of performance spaces and venues [11]|
|Increased consumer spending [6,8,9]|Financial affordability [11,20]|
|Patronages & sponsorships [5,11,12]|Music tourism [8,9,11]|
|Increased financial investments [3,11]|Music education resources [11,12,22]|
|Lower poverty rates [25]|Music heritage and history [4,11]|
|Strengthening social bonding [11]|Demographics (e.g. student populations) [4,11,12,17]|
|Improved mental/physical health [1,2]|Government support/regulation [5,11,12,16]|
|Lower crime rates [7,13,15]|Transportation convenience [11,20]|
|Better community reputation [3,11]|Population density [19]<br>Population growth [18,21]|



Table 1: Table summarizing the benefits of a music community and factors that stimulate a music community. 

efits of and factors that support a strong music scene. In Section 3, we introduce our dataset of music event information and describe how we estimate LMER. Section 4 explores how LMER is correlated with different socioeconomic indicators some of which have been identified as being important factors in healthy music scenes. We then conclude in Section 5 with a discussion of how LMER can be useful for identifying potential music deserts. 

## 2. RELATED WORK 

In this section, we review both academic and music industry research that focuses on the following two questions: 

1. What are the benefits of having a strong music scene? 

2. What factors help foster a strong music scene? 

A summary of our review is provided in Table 1. 

## 2.1 Benefits of a Strong Music Community 

Vibrant music scenes support local economies [3,4,11,12]. A live music event involves working musicians, booking and ticketing agents, sound and lighting technicians, bartenders, security guards, etc. Consumers spend money [6, 8, 9] on concert tickets, food and beverages, and artist merchandise. If a music community is strong enough, it also attracts tourism, where people from outside the community generate revenue for the local economy [8, 9, 11] through hotel stays and other local attractions (museums, parks, etc.). Live music scenes include many small businesses (music and record stores, recording studios, and private music teachers) and large institutions (music conservatories, theaters, and academic institutions). Finally, a vibrant music scene can generate economic knock-on benefits through patronage, sponsorship, cross-promotion, and cross-pollination relationships with other economic sectors [3,5,11,12]. Such cultural-economic interactions can enhance a location’s reputation and quality of life, attracting new residents and new participants to a scene. 

The social and individual benefits of music are also well-studied. Music strengthens the social fabric of a community by "building bridges between cultures and languages, connecting people within a city, a region and 

across borders," as music "touches human beings" and "engages people" [11]. Vibrant music scenes are a component of the "social infrastructure" of healthy communities [26], spaces in which community members of various backgrounds can engage and interact with one another. They are physical spaces that afford and encourage faceto-face social interaction, the development of dense social networks, and the cultivation of shared values. 

Many of these spaces gather together people across the social divisions of class, race, ethnicity, and faith. They are contexts in which people of different backgrounds can encounter one another in a common and often public space. According to the sociologist Robert Putnam, in the context of large pluralistic societies such as the USA, social activities such as music cultivate ªbridging social capital.º These are contexts in which we connect to people potentially unlike ourselves and through this cultivate a sense of ªcivic virtueº that widens ªour awareness of the many ways in which our fates are linkedº [27]. 

Empirical analyses of large social datasets suggest that engagement in arts events is associated with increased happiness and satisfaction measures [2]. Ethnographic case studies of particular music scenes suggest that participation in vibrant scenes is associated with subjective wellbeing [1, 11]. Industry analyses and censuses associate strong scenes with enhanced civic pride and cultural reputation [3,11]. Our ongoing work will explore possible correlations between live, public music events across America and a wide range of well-being indicators, including political participation and the experience of belonging, trust, and reciprocity. 

## 2.2 Factors that Create a Strong Music Community 

Terrill et al. [11] identifies five essential elements of strong music scenes: a large number of active musicians, a community that supports diverse musical offerings, a variety of spaces for rehearsing, recording, and performance, along with a receptive and engaged audience, and a variety of music-related business. Other helpful factors include multi-level government support [5, 12, 16] (e.g., cultural zones, and accommodating noise ordinances and liquor laws [28]), city infrastructure (transportation, affordable housing), and music education [12,22] from public school 

584 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

music programs, to private lessons, to music conservatories [29]. A vibrant music scene also requires equitable access to funding, the fair enforcement of city ordinances, and the cultivation of shared social spaces [28]. Are the small business loans needed to support music infrastructure equitably available across demographic sectors? Are noise ordinances and venue regulations enforced and policed evenly across neighborhoods? Does the local government sponsor arts festivals and programs available to and welcoming of all citizens? 

Demographics play a key role in establishing and invigorating a music community; for example, young people such as university students are more likely to go out to music events [4, 11, 12]. Denser populations often mean stronger social networking, associated with vibrant music scenes [19]. Lastly, as the population increases, the demand for live music also often increases, which can strengthen a music community [18,21]. 

## 3. MUSIC EVENT DATA 

To obtain a rough estimate of the strength of a city’s music scene, we calculated its live music event rate (LMER). Specifically, we calculate the number of music events per year per 100,000 residents in a given geographic area. 

We compiled the LocalifyMusicEvents-USA-2019 dataset<sup>3</sup> that consists of information for 308,051 music events from 1,139 cities in the United States, each with a population of 10,000 or more residents. The music event information was collected using custom web scrapers in late 2018 and all of 2019. We developed two web scrapers, one for BandsInTown, a comprehensive music event website, and one for Facebook, a popular social network. The BandsInTown scraper relied on snowball sampling [30] to build growing lists of artist and venue pages. Each page was scraped for events every 30 days. New artists and venues were continually added based on similarities between artists, artists playing at different venues, and artists playing events with other artists. By contrast, our Facebook scraper collected music event information by cycling repeatedly over a large list of cities continually. 

To calculate LMER, we first count the total number of music events listed in the city during 2019 by matching the city and state names. We then divided by the city population according to the US Census population estimates for 2019. 

Our dataset also contains 28 city-level socioeconomic indicators obtained from three different websites: Census Reporter<sup>4</sup> , DataUSA<sup>5</sup> , and Census Quickfacts<sup>6</sup> . These indicators are partitioned into six groups (transportation, population, economics, age, education, race) and are summarized in Table 2. 

> 3 Data can be found at https://github.com/JimiLab/Loc alifyMusicEventData. 

> 4 https://censusreporter.org/ 

> 5 https://datausa.io/ 

> 6 https://www.census.gov/quickfacts/ 

## 3.1 Music Havens 

We divide the cities into three subsets grouped by population: small (pop. 10K-100K), medium (pop. 100K-500K), and large (pop. 500K or more). For each subset, the top ten "music havens" (cities with the largest LMER) are shown in Table 3. 

|Size|Principal City|Pop.|LMER|
|---|---|---|---|
|Small|South Burlington, VT|19162|0.036|
||Steamboat Springs, CO|12928|0.020|
||Asheville, NC|92859|0.019|
||Santa Cruz, CA|64605|0.019|
||Key West, FL|24843|0.017|
||Burlington, VT|42545|0.017|
||Ithaca, NY|30569|0.016|
||Fredericksburg, TX|11245|0.016|
||Lahaina, HI|12776|0.014|
||Rutland,VT|15398|0.013|
|Medium|Salt Lake City, UT|200546|0.023|
||Berkeley, CA|121353|0.016|
||New Orleans, LA|390144|0.015|
||Richmond, VA|230436|0.015|
||Cambridge, MA|118925|0.013|
||Boulder, CO|105670|0.010|
||Orlando, FL|287435|0.009|
||Fort Collins, CO|170245|0.009|
||Minneapolis, MN|429605|0.009|
||Charleston,SC|143151|0.008|
|Large|Denver, CO|727211|0.016|
||Washington, DC|705749|0.011|
||Austin, TX|979263|0.011|
||Atlanta, GA|506804|0.010|
||Seattle, WA|753655|0.010|
||Portland, OR|653467|0.009|
||Las Vegas, NV|651297|0.008|
||San Francisco, CA|881549|0.007|
||Philadelphia, PA|1584064|0.005|
||Dallas, TX|1343565|0.005|



Table 3: Top 10 "Music Havens" for Small (pop. 10K-100K), Medium (pop. 100K-500K), and Large Cities (pop. 500K+) ranked by Live Music Evert Rate (LMER) 

In these three lists, we find several popular tourist towns, e.g., Steamboat Springs, CO, Key West, FL, Las Vegas, NV, as well as college towns, e.g., Burlington & South Burlington, VT (U. of Vermont), Ithaca, NY (Cornell U.), Berkeley, CA (U. of California). We also find several cities, like Austin, TX, Asheville, NC, Atlanta, GA, and New Orleans, LA which all frequently appear on lists of top destinations for ªmusic tourismº in the United States.<sup>7</sup> 

Many of the medium and large cities that we identify as music havens also appear on a list of American cities with the most concerts per capita based on data from Seat- 

> 7 https://www.thrillist.com/travel/nation/best-cities-for-live-musicnew-york-memphis-asheville-and-austin 

585 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

|Indicator|Description|Source|
|---|---|---|
||Transportation||
|Mean Travel Time|Mean travel time to work(minutes)|Census Reporter|
|Public Transit|% ofpopulation who tookpublic transit(e.g.,buses)|Census Reporter|
|Bicycle|% ofpopulation who biked|Census Reporter|
|Walkability|% ofpopulation who walked|Census Reporter|
|Public Transit+Bicycle+Walkability|% ofpopulation who tookpublic transit,biked,or walked|Census Reporter|
||Population||
|Population Density|Populationper square mile|Census Reporter|
|10 Year Population Growth|Populationgrowth from 2010(acc. to CensusQuickfacts,as of April 1,2010)to 2019(acc. to ACS 2019).|CensusQuickfacts,Census Reporter|
|Migration Rate Since Previous Year|Geographic mobility- % ofpopulation who moved to citysince lastyear.|Census Reporter|
||Economics||
|Per Capita Income|Average incomeperperson in city ($)|Census Reporter|
|Median Household Income|Median incomeper household in city ($)|Census Reporter|
|PovertyRate|% of city population belowpovertyline|Census Reporter|
|Median PropertyValue|Median value of owner-occupied housingunits($)|Census Reporter|
|Employment Rate|Number ofpeople employed(DataUSA)divided by2019population(Census Reporter)|DataUSA,Census Reporter|
|Median Gross Rent|Mediangross rent($),2015-2019|CensusQuickfacts|
|Median Owner Cost With Mortgage|Median selected monthlyowner costs -with a mortgage($),2015-2019|CensusQuickfacts|
|Median Owner Cost Without Mortgage|Median selected monthlyowner costs -without a mortgage($),2015-2019|CensusQuickfacts|
|Owner-Occupied HousingUnit Rate|Owner-occupied housingunit rate(%),2015-2019|CensusQuickfacts|
||Age||
|Median Age|Median age of city|Census Reporter|
|Percent Under 18|Percentage ofpopulation under age 18|Census Reporter|
|Percent 18-29|Percentage ofpopulation between ages 18 and 29|Census Reporter|
|Percent Under 30|Percentage ofpopulation under age 30|Census Reporter|
|Percent 20-29|Percentage ofpopulation between ages 20 and 29|Census Reporter|
|Percent 10-29|Percentage ofpopulation between ages 10 and 29|Census Reporter|
|Age DiversityIndex|Simpson’s diversityindex for age(0-9,10-19,...,70-79,80+)|Census Reporter|
||Education||
|High School Or Higher|Percentage ofpopulation that are high schoolgrads or higher|Census Reporter|
|Bachelor Or Higher|Percentage ofpopulation with Bachelor’\s degree or higher|Census Reporter|
|Postgrad Degree|Percentage ofpopulation withpost-grad degree|Census Reporter|
||Race||
|Race DiversityIndex|Simpson’s diversityindex for ethnicity (White,Black,Native,Asian,Islander,Other,Two+,Hispanic)|Census Reporter|



Table 2: A list of all 28 city-level socioeconomic indicators used and their corresponding descriptions. 

Geek<sup>8</sup> , a large ticket reselling site [31]. Their top cities include Las Vegas, NV, Nashville, TN, Austin, TX, and Denver, CO. This overlap gives us some confidence in our approach but it should be noted that the SeatGeek reports only examines large events from the top 100 grossing artists in the top 100 market areas (i.e., cities). 

## 3.2 Music Deserts 

There were 87 cities (7.6% of 1,139 cities) for which there were no events in the LocalifyMusicEvents-USA-2019 dataset. The three "music desert" cities with the largest populations were Renton, WA (pop. 101,747), Deltona, FL (pop. 92,752), and Newton, MA (pop. 88,411). When we examine all three using simple Google web searches, it is clear that there are music events taking place in these cities, as they are listed on their corresponding local websites<sup>9</sup> but not found when we scraped event information from our two data sources (BandsInTown, Facebook). This suggests that our dataset is incomplete due to the imperfect nature of our scraping procedure and our limited set of data sources. We will further discuss these limitations in Section 5.1. 

> 8 https://seatgeek.com/ 

> 9 Renton, WA: https://rentondowntown.com/happenings/summerconcert-series/, Deltona, FL: https://www.deltonafl.gov/parksrecreation-department/events/22814, Newton, MA: https://patch.com/massachusetts/newton/newton-porchfest-2019-whatknow 

## 4. CORRELATION WITH SOCIOECONOMIC INDICATORS 

In this section, we explore correlations between LMER and the 28 different socioeconomic indicators using statistical testing. If we assume that LMER is a rough indicator of the strength of a local music scene, we can use it to study how music scenes are related to other aspects of our society. We have grouped the 28 socioeconomic indicators into six categories: Transportation, Population, Economics, Age, and Education & Race. The 28 indicators we sampled, as well as the sources they were collected from, are shown in Table 2. 

We use a Bonferroni correction when determining statistical significance since we are conducting multiple hypothesis statistical tests [32]. Usually, in significance testing, we perform one statistical test, and obtain the correlations r and p-values p; an indicator is deemed significant if p < α, where α is the p-value threshold. The Bonferroni correction, however, deems an indicator significant if p < α/I, where I is the number of statistical tests (i.e., one per indicator). In our experiment, there are I = 28 indicators and we set α to 0.05; thus, a correlation is significant if the p-value is less than α/I = 1.8e-3. 

Table 4 shows the correlation coefficients (or r-values) and the probability of observing the data assuming no correlation (p-value) for each of these indicators grouped in their categories, with the p-values (p) ranked from smallest (most significant) to largest (least significant) for each category. 

586 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

## 4.1 Transportation 

As shown in Table 4, we find that there is a strong positive correlation between LMER and the first four transportation-based indicators (percentage of people who bike, take public transit, walk, or all three together). Good public transportation reduces the overall cost of attending a show [20] and enables more people to drink alcohol (more safely) at night, which is very often associated with live music events. This finding supports the claim by Terrill et al. [11] that supportive urban infrastructure is an important factor for a strong local music scene. We also considered the mean travel time to work, but did not find it to have a statically significant correlation. 

## 4.2 Population 

We observe that population density as well as one-year and ten-year population growth are all positively correlated with LMER. Van der Hoeven and Hitters [19] argue that "density and diversity provide the critical mass of participants that alternative [music] scenes need to thrive." When people are clustered together, it is easier to engage and interact with one another. This idea also relates to population growth; as people with diverse backgrounds immigrate to the city, there is an increase in opportunities for musicians to influence one another in novel ways [18]. 

## 4.3 Economics 

As we discussed in Section 2.2, many researchers have suggested that having a strong local music scene is good for the local economy [6, 8, 9, 11]. This is consistent with our findings that employment rate, housing cost, per capita income, and median property values are all positively correlated with LMER. We found it interesting that the owneroccupied housing rate is negatively correlated which suggests that there are more live music events when there is a higher proportion of renters relative to homeowners. This is consistent with the observation that home affordability has dropped in the United States, making it harder for young people to own their homes [33], and as we observe in the next subsection, having a larger percentage of younger adults is positively correlated with LMER. 

Concerning poverty, Harrison [25] examines how ªmusic projects develop the skills, education levels, incomes, or occupational possibilities of participants living in material poverty, which in turn can enhance their socioeconomic status.º Accordingly, we might expect a lower poverty rate where there was more live music but we did not find a statistically significant correlation between poverty rate and LMER. We assume therefore that the dynamic between poverty and music is too complex to be measured in a simple quantitative analysis. 

## 4.4 Age 

Our results show that cities with a high proportion of young people between the ages of 18 and 29 tend to have a large live music event rate. Conversely, cities with a large population of people under 18 are negatively correlated with 

LMER. This may be because many music venues (i.e., bars) tend to have 18-and-up and 21-and-up policies due to laws related to serving alcohol. These two results, along with the fact that neither median age nor the percentage of the population under 30 is correlated with LMER, suggest that cities with many young adults (college students, young professionals, aspiring young artists) are places where we expect to have many live music events. Conversely, cities with a relatively large percentage of families are less likely to have a high rate of music events. As mentioned in the previous subsection, age is also positively correlated to home ownership, as decreasing home affordability in the United States has caused fewer young people to own a home; this entails a negative correlation between owneroccupied housing rate and LMER, as higher housing ownership rates means fewer young people, an indicator of a lower LMER. 

## 4.5 Education 

Terrill et al. [11] suggests that "cities such as Toronto, Adelaide, Austin, and Berlin point to their large student populations as helpful factors in generating engaged audiences." Our results support this in that we find a positive correlation between LMER and cities with a high proportion of people with undergraduate or graduate degrees. This is also reflected by the fact that many of the top Music Havens in Table 3 are college towns as was discussed in Section 3.1. 

## 4.6 Race 

We did not find a significant correlation between our racial diversity index and the LMER. This might be surprising considering the associations suggested between healthy music scenes and demographic diversity [34]. In that, we only explore one indicator that explicitly relates to race, a more thorough analysis is required to explore the complex relationship between race and the strength of music scenes. 

## 5. DISCUSSION 

In this paper, we explore how using the live music event rate (LMER) is straightforward to estimate, easy to interpret, and correlated with a large and diverse set of socioeconomic indicators. We found a strong positive correlation between LMER and the percentage of people who take public transit, walk, or bike. Education is also strongly correlated with LMER. We also observed that many economic indicators (e.g., employment rate, per capita income, median property value) are also correlated with LMER. Finally, there is a high live music event rate when there is a high proportion of late teens and individuals in their twenties. We did not find a significant correlation between LMER and our race diversity index. This is not to say that no relationship exists, but rather our simplistic analysis did not reveal a statistically significant correlation. 

587 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

|Indicator|r|p|
|---|---|---|
|Transportation|||
|Bicycle|0.39|5.1e-43|
|Public Transit+Bicycle+Walkability|0.34|1.1e-32|
|Public Transit|0.26|1.8e-18|
|Walkability|0.24|7.7e-17|
|Mean Travel Time|0.04|1.5e-01|
|Population|||
|Population Density|0.21|1.5e-12|
|10 Year Population Growth<br>|0.18<br>|9.8e-10<br>|
|Migration Rate Since Previous Year|0.13|1.7e-05|
|Economics|||
|Employment Rate|0.26|4.7e-19|
|Owner-Occupied Housing Unit Rate|-0.21|3.3e-13|
|Median Owner Cost w/ Mortgage<br>|0.19<br>|2.4e-10<br>|
|Median Owner Cost w/o Mortgage|0.17|2.9e-09|
|Median Property Value<br>|0.17<br>|1.8e-08<br>|
|Per Capita Income|0.16|3.7e-08|
|Median Gross Rent|0.15|2.7e-07|
|Median Household Income|0.06|3.1e-02|
|PovertyRate|-0.00|8.2e-01|
|Age|||
|Percent Under 18|-0.24|7.6e-16|
|Percent 20-29|0.17|2.0e-08|
|Percent 18-29|0.14|1.8e-06|
|Age Diversity Index|0.11|1.1e-04|
|Percent 10-29|0.10|4.5e-04|
|Median Age|-0.06|4.1e-02|
|Percent Under 30|0.02|4.1e-01|
|Education|||
|Bachelor Or Higher|0.27|6.6e-20|
|Postgrad Degree|0.24|8.1e-16|
|High School Or Higher|0.12|6.6e-05|
|Race|||
|Race Diversity Index|-0.07|1.9e-02|



Table 4: Table showing the correlation coefficient (r) and p-values (p) for all 28 socioeconomic indicators across all 1,139 cities. Statistically significant indicators are in bold 

font. 

## 5.1 Limitations 

As mentioned in Section 3.2, the music events dataset was not collected for this research, but rather for our Localify.org<sup>10</sup> music events recommendation application. As a result, the scraping was limited in the number of data sources (Facebook & BandsInTown), collected in an adhoc manner (snowball sampling), only covers one year of data (2019), and only looks at one country (United States). It is probable that many active artists, venues, and events were not found using our music event data collection process. 

To increase our coverage and add redundancy, we have since added additional scrapers (e.g., SongKick, Google, Eventbrite) but the music event data we have scraped in 2020 and 2021 is problematic since such a high percentage of scheduled music events were canceled due to COVID19. However, even with a large number of scrapers, our 

> 10 https://localify.org/ 

approach necessarily ignores music events that do not have a digital footprint. This includes many underground (private house parties, DIY shows), music in religious spaces (e.g., churches), and impromptu performances (e.g., busking). Our future work will be to explore how our approach to scraping music event information might be incomplete and/or biased by taking a detailed census of music events in individual cities using more principled ethnographic techniques (e.g., observation, interviews, historical records). 

As described in Section 3, the 28 socioeconomic indicators for each city were collected using three different web sources, rather than one unified source. A more systematic approach is to use one unified source for our data collection, such as ESRI datasets<sup>11</sup> . For certain indicators addressed in Section 2 and Table 1, such as mental/physical health, cultural heritage, and local government regulations on music, we could not find any available quantitative data sources to measure them. 

## 5.2 Future Work 

Both popular culture and academic research tend to focus on "music havens" like Nashville, TN and Seattle, WA. These are cities that are known to have a great local music scene and they reap economic, social, and cultural rewards because of it. We, by contrast, are especially interested in identifying cities with underdeveloped music scenes. We plan to study these ªmusic deserts"’ and explore how various strategies could be used to help them strengthen their local music scenes. For example, Terrill et al. [11] outlines a number of potential strategies which include developing music-friendly government policies, creating musicfocused offices and advisory boards, investing in audience development, and creating music tourism plans. We argue that cities with low local music event rates (LMER) may be good initial candidates for future research involving the study of music deserts. 

## 6. REPRODUCIBILITY 

To make our research both fully reproducible and transparent, our full LocalifyMusicEvents-USA-2019 dataset and the associated data processing code (in the form of Jupyter Notebooks) can be found at https://github.com/J imiLab/LocalifyMusicEventData. 

## 7. ACKNOWLEDGEMENTS 

Doug Turnbull, Tim Clerico, John Hunter, and Emmett Barry all contributed to the Localify.org music event scraper code. This research was supported by NSF grant IIS-1901330/1901168 and NEH grant HAA-280975-21. Finally, we would like to thank the anonymous ISMIR reviewers for their highly constructive feedback. 

## 8. REFERENCES 

- [1] S. Baker, R. Nowak, P. Long, J. Collins, and Z. Cantillon, ªCommunity Well-Being, Post-Industrial Music 

> 11 https://www.esri.com/en-us/arcgis/products/arcgis-open-data 

588 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

   - Cities and the Turn to Popular Music Heritage,º in Music Cities. Springer, 2020, pp. 43±61. 

- [2] D. Wheatley and C. Bickerton, ªSubjective Well-Being and Engagement in Arts, Culture and Sport,º Journal of Cultural Economics, vol. 41, no. 1, pp. 23±45, 2017. 

- [3] T. M. G. (Firm), The Austin Music Census: A DataDriven Assessment of Austin’s Commercial Music Economy. Titan Music Group, LLC, 2015. [Online]. Available: https://books.google.com/books?id=fStOjw EACAAJ 

- [4] A. J. Baker, ªAlgorithms to Assess Music Cities: Case Study Ð Melbourne as a Music Capital,º SAGE Open, vol. 7, no. 1, pp. 1±12, 2017. 

- [5] S. Frith, M. Brennan, M. Cloonan, and E. Webster, ª‘Analysing Live Music in the UK’ Findings One Year into a Three-Year Research Project,º IASPM Journal, vol. 1, no. 1, pp. 1±30, 2010. 

- [6] F. Holt, ªThe Economy of Live Music in the Digital Age,º European Journal of Cultural Studies, vol. 13, no. 2, pp. 243±261, 2010. 

- [7] D. Siegel and F. Bovenkerk, Crime and Music. Springer, 2021. 

- [8] ªEconomic Contribution of the Venue-Based Live Music Industry in Australia,º Australasian Performing Right Association, vol. 20, 2011. 

- [9] S. Hallam, I. Cross, and M. Thaut, Oxford Handbook of Music Psychology. Oxford University Press, 2011. 

- [10] A. J. Ferrer, ªThe Effect of Live Music on Decreasing Anxiety in Patients Undergoing Chemotherapy Treatment,º Journal of Music Therapy, vol. 44, no. 3, pp. 242±255, 2007. 

- [11] A. Terrill, D. Hogarth, A. Clement, P. Assistant, and R. Francis, The Mastering of a Music City: Key Elements, Effective Strategies and Why It’s Worth Pursuing. Music Canada, 2015. 

- [12] E. Webster, M. Brennan, A. Behr, M. Cloonan, and J. Ansell, ªValuing Live Music: The UK Live Music Census 2017 Report,º 2018. 

- [13] A. Williams and A. Lal, ªCorrelations between Crime Rates in US Cities, and the Popularity of Rap and HipHop Music,º 2015. 

- [14] S. Oakes and G. Warnaby, ªConceptualizing the Management and Consumption of Live Music in Urban Space,º Marketing Theory, vol. 11, no. 4, pp. 405±418, 2011. 

- [15] C. Pinkney and S. Robinson-Edwards, ªGangs, Music and the Mediatisation of Crime: Expressions, Violations and Validations,º Safer Communities, 2018. 

- [16] S. Brown and U. Volgsten, Music and Manipulation: On the Social Uses and Social Control of Music. Berghahn Books, 2005. 

- [17] H. Shobe and D. Banis, ªMusic Regions and Mental Maps: Teaching Cultural Geography,º Journal of Geography, vol. 109, no. 2, pp. 87±96, 2010. 

- [18] C. Gibson, ªRural Transformation and Cultural Industries: Popular Music on the New South Wales Far North Coast,º Australian Geographical Studies, vol. 40, no. 3, pp. 337±356, 2002. 

- [19] A. Van der Hoeven and E. Hitters, ªThe Social and Cultural Values of Live Music: Sustaining Urban Live Music Ecologies,º Cities, vol. 90, pp. 263±271, 2019. 

- [20] P. E. Earl, ªSimon’s Travel Theorem and the Demand for Live Music,º Journal of Economic Psychology, vol. 22, no. 3, pp. 335±358, 2001. 

- [21] M. Brennan, ªLive Music History,º The SAGE Handbook of Popular Music, pp. 207±222, 2015. 

- [22] K. Swanwick, Music, Mind and Education. Routledge, 2003. 

- [23] M. Davyd, ªGRASSROOTS MUSIC VENUES (GMVs)±DEFINITION,º 2016. 

- [24] D. A. Economics, ªThe Economic, Social and Cultural Contribution of Venue-based Live Music in Victoria,º Melbourne: Arts Victoria, 2011. 

- [25] K. Harrison, ªMusic, Health, and Socio-Economic Status: A Perspective on Urban Poverty in Canada,º Yearbook for Traditional Music, vol. 45, p. 58±73, 2013. 

- [26] E. Klinenberg, Palaces for the People: How Social Infrastructure Can Help Fight Inequality, Polarization, and the Decline of Civic Life. Crown, 2018. 

- [27] R. D. Putnam, ªBowling Alone: America’s Declining Social Capital,º in Culture and Politics. Springer, 2000, pp. 223±234. 

- [28] A. McGraw, ªMapping Sonic and Affective Geographies in Richmond, Virginia,º Sonic Identity at the Margins, p. 19, 2022. 

- [29] L. K. Richerme, ªEquity via Relations of Equality: Bridging the Classroom-Society Divide,º International Journal of Music Education, vol. 39, no. 4, pp. 492± 503, 2021. 

- [30] L. A. Goodman, ªSnowball Sampling,º The Annals of Mathematical Statistics, pp. 148±170, 1961. 

- [31] ªWhich U.S. Cities Get the Most Concerts?º https: //seatgeek.com/tba/music/which-u-s-cities-get-themost-concerts/. 

- [32] C. Y. Wijaya, ªMultiple Hypothesis Testing Correction for Data Scientist,º Oct 2021. [Online]. Available: https://towardsdatascience.com/multiple-hypothesis-t esting-correction-for-data-scientist-46d3a3d1611d 

589 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

- [33] G. Paz-Pardo, ªThis is Why Owning a Home is More Difficult than Ever for Young People,º Jan 2022. [Online]. Available: https://www.weforum.org/agenda /2022/01/younger-generations-homeownership-housi ng-market-wealth-inequality/ 

- [34] C. Ballico and A. Watson, Music Cities: Evaluating a Global Cultural Policy Concept. Springer, 2020. 

590 

