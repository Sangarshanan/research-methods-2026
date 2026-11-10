---
paper_id: "000102"
year: 2022
title: "Download pdf"
source_url: "https://zenodo.org/record/7342596/files/000102.pdf"
---

# TRACKING THE EVOLUTION OF A BAND’S LIVE PERFORMANCES OVER DECADES 

Florian Thalmann, Eita Nakamura, Kazuyoshi Yoshii Graduate School of Informatics, Kyoto University, Japan 

thalm007@umn.edu, {eita.nakamura, yoshii}@i.kyoto-u.ac.jp 

## ABSTRACT 

Evolutionary studies have become a dominant thread in the analysis of large audio collections. Such corpora usually consist of musical pieces by various composers or bands and the studies usually focus on identifying general historical trends in harmonic content or music production techniques. In this paper we present a comparable study that examines the music of a single band whose publicly available live recordings span three decades. We first discuss the opportunities and challenges faced when working with single-artist and live-music datasets and introduce solutions for audio feature validation and outlier detection. We then investigate how individual songs vary over time and identify general performance trends using a new approach based on relative feature values, which improves accuracy for features with a large variance. Finally, we validate our findings by juxtaposing them with descriptions posted in online forums by experienced listeners of the band’s large following. 

## 1. INTRODUCTION 

Music information retrieval has proven essential for the analysis of large audio corpora, especially ones for which traditional music analysis methods are limited. Such cases include large audio collections for which there is no appropriate symbolic transcription, such as ones containing non-western music or improvised music [1–5]. 

In recent years numerous studies have characterized the temporal evolution of musical characteristics in such corpora. Serra et al identified a restriction of pitch transitions, homogenization of timbral palette, and growing loudness levels in Western popular music [6]. On a similar corpus, Mauch et al discovered three stylistic revolutions between 1960 and 2010, based on topics identified via latent Dirichlet allocation of harmonic and timbral features [7]. Deruty and Pachet determined the ‘loudness war’ in popular music production to have peaked in 2007 [8]. Weiss et al found harmonic complexity to be gradually increasing in Jazz solos between the 1920s and the 2000s [4]. Weiss et 

> © F. Thalmann, E. Nakamura, and K. Yoshii. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: F. Thalmann, E. Nakamura, and K. Yoshii, “Tracking the Evolution of a Band’s Live Performances over Decades”, in Proc. of the 23rd Int. Society for Music Information Retrieval Conf., Bengaluru, India, 2022. 

al also confirmed common hypotheses concerning the evolution of chord transitions, intervals, and tonal complexity in Western classical music [9]. Parmer and Ahn measured information-theoretic complexity of pitch, loudness, timbre, and rhythm in a popular music dataset and identified trends over decades [10].<sup>1</sup> 

All of these studies look at music at a social or cultural level and use audio corpora that consist of material by various composers or musicians, as well as of different genres, subgenres, instrumentations, etc. In this paper we present an analogous study which however focuses on the music of a single band, the Grateful Dead, who are well-known for their ever-evolving performances. We use a dataset that consists of audio recordings of 2617 performances of 15 songs spanning three decades. Although this may be a sizable dataset for a band, we find that musical characteristics show a large variance over the relatively short timespan. For example, the tempos of the performances in the set range from 50 to 160, which over the whole time span results in a relatively sparse cloud of data points. 

Previous approaches are relatively limited when dealing with such diverse data. They all consider the corpus as a whole and simply plot the evolution of audio features against time. This may work reasonably well for some musical characteristics such as tonal complexity, timbre, or loudness. However, we show how subdividing the corpus into subsets, in our case songs, and considering feature data relative to these subsets before integrating them into a whole can improve accuracy and confidence for the detection of overall trends. We identify such trends in various performance characteristics and juxtapose them with observations by experienced listeners from the band’s large following. In particular, despite working with a relatively small subset of only 15 of the band’s songs, we are able to identify generally perceived trends in tempo, song duration, and dynamic, spectral and harmonic content with promising accuracy. 

## 2. DATASET 

The cultural impact and decades long performance history of the Grateful Dead has led to continued interest in the band’s music by both fans and scholars [14]. The band is especially known for their free and inclusive approach to music, their unwillingness to bow to the conventions of popular music, and their aspiration to provide their fans 

> 1 Similar trend analyses were recently done with non-audio music collections, such as with lyrics [11] or symbolic data [12,13]. 

850 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

with a new experience at every concert. The performances of their songs often vary greatly, even from day to day, and they often engage in long improvisational parts or jams. Almost all of their over 2000 concerts between 1965 and 1995 have been recorded, often multiple times, and most of these recordings are public domain and included in the Live Music Archive’s (LMA) largest subcollection.<sup>2</sup> To musicologists, this catalog may be intimidating for these reasons [15], but this make it all the more interesting for studies using MIR methods. 

We use a dataset introduced by [5]<sup>3</sup> which includes 2617 performed versions of a set of 15 songs from the Grateful Dead collection of the Live Music Archive. According to the authors, the songs were selected based on two criteria: a large number of versions with soundboard recordings across the whole time span, as well as a studio recording as a potential reference. Many of these recordings contain crowd noise, which may affect the quality of features, and many are out of tune due to varying tape speed during recording. The dataset comes with a script that downloads the files from the LMA and automatically resamples them based on tuning ratios determined from chroma vectors. Figure 1 (a) shows a chronological distribution of the files. We observe very low counts for the first two years which may be due to a lower number of available recordings, and 1975 when the band retired for a year. A relative distribution of songs across the years (Figure 1 (b)) shows that the first two years of the dataset only contain one song, which may be problematic for an evolutionary analysis. A more systematic generation of such a dataset may prove useful in the future, but we chose to use it here without modifications. 

## 3. METHOD 

The fact that we have subsets of identical or similar musical pieces or recordings can be leveraged at different points in the process. First, a large number of audio features are extracted for each recording in the corpus, now tuned as described above. We then validate these features relatively for each song, which allows us to detect outliers, i.e. wrongly classified songs, as well as adjust wrongly extracted features such as double-time beats. Our statistical analysis includes two steps. We first analyze the feature distribution and evolution for each song independently, which allows us to characterize the relative evolution of normalized feature values for each song. These relative evolutions are then collated into a global evolution curve for each feature, which we validate using bootstrapping, i.e. by alternately leaving out each song. 

## 3.1 Feature Extraction 

The set of audio features used in our study were inspired by previous work on other corpuses referenced in Section 1 and extracted using madmom<sup>4</sup> (beats, from which we de- 



<!-- Start of picture text -->
box_of_rain estimated_prophet<br>casey_jones eyes_of_the_world<br>china_cat_sunflower franklin's_tower<br>20 0 china_doll scarlet_begonias<br>cosmic_charlie ship_of_fools<br>cumberland_blues sugar_magnolia<br>dancin'_in_the_street truckin'<br>dark_star<br>15 0<br>10 0<br>5 0<br>0<br>1965 1970 1975 1980 1985 1990 1995<br>time<br>(a)<br>1. 0<br>0. 8<br>0. 6<br>0. 4<br>0. 2<br>0. 0<br>1965 1970 1975 1980 1985 1990 1995<br>time<br>(b)<br>version count<br>proportion<br><!-- End of picture text -->

Figure 1: (a) Chronological distribution of the recordings for each song in the dataset. (b) Relative distribution of songs by year, order and colors correspond to (a). 

rived tempo), librosa<sup>5</sup> (chroma and mfcc, summarized to the madmom beats), as well as the essentia freesound extractor<sup>6</sup> (for dynamic and spectral summary features). We used standard settings for all extractors, except for with madmom’s DBNBeatTrackingProcessor where we used a much higher transition lambda of 2000 rather than the suggested maximum of 300 in the documentation. This was to reduce the probability of the processor jumping between tempos within one audio file, which may have been occurring due to the many long versions (median over 10min, sometimes over 30min), as well as the amount of crowd noise. 

We also calculated a few additional features, inspired by other studies. Tonal complexity as defined by Weiss et al as the angular deviation or spread of pitch-classes on a circular chroma vector, permuted to correspond to the circle of fifths [4,9,16]. To measure pitch content agnostic of tonality, we devised an analogous pitch complexity feature based 

> 2 https://archive.org/details/GratefulDead 

> 3 https://github.com/grateful-dead-live/ fifteen-songs-dataset 

> 4 https://madmom.readthedocs.io 

> 5 https://librosa.org 

> 6 https://essentia.upf.edu/freesound_extractor. html 

851 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

on the reverse-sorted normalized summarized chroma vector, which results in a right-skewed distribution, of which we took the mean. From the 36-bin harmonic pitch class profiles (HPCP) extracted by essentia, we derived a tuning complexity feature, which expresses the average deviation from 440Hz in both directions.<sup>7</sup> 

## 3.2 Beat Correction and Outlier Detection 

The extracted features allow us to address two frequently occurring problems. The first problem is that beat tracking is often inconsistent between different versions of a song, due to the large variance in tempo and the high amount of improvisation in the dataset. The second problem is that some song sets may contain incomplete fragments or recordings of other songs, due to mis-annotations in the Live Music Archive, as noted by Page et al [17]. 

Our beat correction method consists of identifying instances of beat features that should rather be doubletime, half-time, or two-thirds-time.<sup>8</sup> We start with the original beat pairings Bb<sup>i=(Ri, bRi)ofrecordingsRi,</sup> i = 1 . . . K, and their corresponding beat sequences bRi , which are simply sequences of time points, as extracted by a feature extractor. For each beat sequence bRk we create three variants, a linearly interpolated double-time version dRk ,<sup>9</sup> a half-time version hRk which only contain every other beat, and a two-thirds-time version tRk which contain every third beat of dRk . We end up with four sets of K beat sequence pairings Bb<sup>i, B</sup> d<sup>i, B</sup> h<sup>i, B</sup> t<sup>i,defined analogously to</sup> Bb<sup>i.For each of these pairings we extract a set of features</sup> f1, . . . fF which all depend on the beat sequence in the pairing. For each feature f with a corresponding distance function δf , we then create four K ∗ K distance matrices Dij<sup>x,f</sup> = δf (Bx<sup>i, B</sup> b<sup>j),one for each x∈{b, d, h, t}.These</sup> matrices express how well the four types of beat pairings match with the original pairings bRi . We normalize these matrices using min-max normalizations and calculate for each pairing Bx<sup>kits average distance from the original pair-</sup> ings over all features 



<!-- Start of picture text -->
∆ k x = µf =f 1 ...f F ,j=1...K(D kj x,f )<br><!-- End of picture text -->

Finally, we choose for each recording R<sup>k</sup> its best pairing Bx<sup>kwith minimum ∆k</sup> x<sup>.</sup> 

The set of features that worked well for the dataset used in this paper are chord sequence distributions, onset distributions, and tempo. We generate a chord sequence distribution from a summarized chord sequence, where for every beat interval we take the chord that occupies the longest duration. From this sequence we gather all subsequences of length L at step size 1 and count the occurrences of each possible pattern. Onset distributions are generated by calculating the position of each onset o relative to its neigh- 

> 7 These measures are also related to the information-theoretic complexity measures used by Serra et al or Parmer and Ahn [6,10]. 

> 8 Two-thirds-time has proven to be useful in situations where we have a ternary meter, such as 6/8, which might be interpreted as either binary or ternary by the beat extractor. 

> 9 Each successive pair of beats is interspersed with an average of the two, and an additional beat is added at the end, at an interval corresponding to last interpolated one. 

boring beats b<, b>, e.g (o − b<)/(b> − b<) and quantizing the resulting relative onsets to a grid of G values by multiplying them by G rounding to the nearest integer. Both kinds of distributions are normalized. Tempo is simply calculated as the average distance between successive beats. For beat correction, we chose the parameters L = 4, G = 64. 

For distance functions δf we used the chi-square dis- <mark>(</mark> xi− <mark>y</mark> i <mark>)</mark><sup>2</sup> tance χ<sup>2</sup> (x, y) =<sup><mark>1</mark></sup> 2 �i xi+yi for distributions, and the analogous<sup><mark>(</mark>x</sup> x<sup>−</sup> +<sup><mark>y</mark></sup> y<sup><mark>)</mark>2</sup> for two single values x, y, such as for tempo. 

Next, we identify outlier recordings using an extension of the feature set above, by adding chord sequence distributions with L = 2 as well as overall beat count, i.e. the length of the beat feature vector. Similar to the beat correction method, we calculate a distance matrix Dij<sup>f= δf(Ri, Rj) for each feature fand normalize it.We</sup> then calculate a normalized distance df,k for each feature, consisting of the difference between the average deviation of R<sup>k</sup> from the overall average deviation µ(D<sup>f</sup> ), normalized by overall standard deviation σ(D<sup>f</sup> ). 



<!-- Start of picture text -->
µj=1...K(Dk f j ) − µ(Df )<br>df,k =<br>σ(D f )<br><!-- End of picture text -->

Finally, we consider recordings as outliers if they deviate by 2.5 standard deviations in at least two features (df,k > 2.5) or by four standard deviations in at least one (df,k > 4). The latter condition particularly ensures that recordings of extreme length, such as incomplete fragments or improperly segmented files that include more than one song, get excluded due to an extreme deviation of overall beat count. 

We obtained the best results by applying beat correction and outlier detection successively and iteratively, i.e. one after another in a loop, until both the beat positions and the set of included recordings are stable. Especially for songs with less regular structure, the process only terminates after several iterations, due to the reference beat sequences bRj changing at each step. Furthermore, with iterative application we can catch cases of quadruple time etc. 

When applying this method to the dataset, a total of 211 outliers were removed (around 8%), including for a case where we identified a set consisting of recordings of two songs with similar titles, possibly due to wrong annotations. Of the beat features of the remaining versions, 99 were identified as half-time, 8 as two-thirds-time, and 21 as double-time. 

## 3.3 Statistical Analysis 

We are now ready to start our diachronic analysis of the feature data, which is structured as follows. For each feature we have one data point per version of every song. Each version is associated with a specific day on which it was played. For feature f we thus have the data points P<sup>f</sup> =<sup>�</sup> P<sup>f,1</sup> . . . P<sup>f,15</sup> where P<sup>f,i</sup> = (p<sup>f,i</sup> ki<sup>)ki=1...Kiis</sup> the sequence of data points for song i with Ki versions. 

Although our dataset consists of material from only one band, we face a relatively high variation in features, due 

852 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
17 0<br>16 0<br>15 0<br>14 0<br>13 0<br>0 50 100 150 200 250 300<br>version<br>tempo<br><!-- End of picture text -->

Figure 2: The chronological sequence of tempo data points of all 322 versions of Sugar Magnolia. 

to the constant experimentation and improvisation of the band. Figure 2 illustrates how much the tempo of the song Sugar Magnolia varies over time, sometimes by as much as 30% from one day to the next. We can identify a global trend in such data by creating a trend line using LOWESS [18],<sup>10</sup> which fits a polynomial regression line at each point, based on a local neighborhood. This neighborhood consists of a fixed proportion of all points, which we set to f = .2 or 20%. LOWESS works particularly well for data that is unevenly distributed along the x axis, which is the case here due to the uneven distribution of songs across time (Figure 1). 

We can calculate such curves for each song individually, as shown in Figure 3. The top-most curve in this figure corresponds to the line shown in Figure 2 and we can identify two tempo peaks, one around 1973 and one around 1983. It is also apparent that the overall tempo range in the collection varies by more than a factor of 3, from around 50 to almost 160. In order to get a sense of how the tempo changes over all songs, we can create a plot for the whole set of songs, LOWESS(P<sup>f</sup> ). However, in order to make sure that the curve is not dominated by the values of a single song, we calculate a confidence interval using bootstrapping, leaving out each song once.<sup>11</sup> For each j = 1 . . . 15 we calculate LOWESS(<sup>�</sup> i̸=j<sup>P f,i), and</sup> determine at each time point the minimum and maximum value among these curves to get the confidence interval. 

With absolute values, this confidence interval turns out to be quite large, leaving us unable to draw conclusions with certainty, as shown by the orange curve in Figure 4. For example, we cannot confidently say that the peak observed in 1984 is higher than the one in 1972, due to the overlapping confidence intervals. However, we can get a much better estimate of how the tempo changes by taking relative feature values, which we can simply calculate by 

> 10 As used by Moss et al in their analysis of the evolution of the distribution of pitch-class content on the line of fifths [13]. 

> 11 An alternative method for this is bootstrap resampling, where we could ensure an equal number of points per song. However, due to limitations found in the dataset (after outlier detection one song only has 22 versions), we chose to use the present method. 



<!-- Start of picture text -->
box_of_rain china_doll dancin'_in_the_street eyes_of_the_world ship_of_fools<br>casey_jones cosmic_charlie dark_star franklin's_tower sugar_magnolia<br>china_cat_sunflower cumberland_blues estimated_prophet scarlet_begonias truckin'<br>16 0<br>14 0<br>12 0<br>10 0<br>8 0<br>6 0<br>1968 1972 1976 1980 1984 1988 1992 1996<br>time<br>relative deviation<br><!-- End of picture text -->

Figure 3: LOWESS plots of tempo for each individual song in the dataset. 



<!-- Start of picture text -->
tempo relative<br>1. 3<br>tempo absolute<br>1. 2<br>1. 1<br>1. 0<br>0. 9<br>0. 8<br>0. 7<br>1968 1972 1976 1980 1984 1988 1992 1996<br>time<br>relative deviation<br><!-- End of picture text -->

Figure 4: Bootstrapped LOWESS curves on the whole dataset for absolute and relative tempo values. 

normalizing the sequences (p<sup>f,i</sup> ki<sup>) as follows:</sup> 



<!-- Start of picture text -->
(p f,i ki )<br>(p f,i ki )′ =<br>µ(P f,i )<br><!-- End of picture text -->

In the case of tempo, each version of every song now has a relative tempo feature, which expresses how its tempo relates to all other performances of the song. The blue curve in Figure 4 is a bootstrapped LOWESS calculated on relative tempo values. We can observe a much narrower confidence interval, now enabling us to confidently claim that in 1984 the tempo was higher than any time in the 70s or 90s. We can also observe that in the beginning of the timeline the curves digress dramatically and with a much larger bootstrapping interval, which is due to the dataset containing few versions of few songs during that time, as observed in Section 2. All subsequent plots are of relative features and calculated as just described. 

## 4. RESULTS 

There has been very little musicological work on the Grateful Dead [19, 20], perhaps due to the intimidating size of 

853 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
tempo<br>1. 3 duration<br>1. 2<br>1. 1<br>1. 0<br>0. 9<br>0. 8<br>0. 7<br>1968 1972 1976 1980 1984 1988 1992 1996<br>time<br>relative deviation<br><!-- End of picture text -->

Figure 5: Bootstrapped LOWESS curves for tempo and song duration across all songs. 

the band’s catalog as well as the intentionally fleeting nature of the performances, as hypothesized by Tift [15]. However, when it comes to in-depth knowledge of the band’s music, the best source are undoubtedly the band’s fans themselves, the Deadheads. Many of them have spent decades listening to the music and debating it online, and some of them are so knowledgeable that they have an acute sense of how the music changes every single year throughout the band’s history. In order to find such general yet detailed descriptions of the evolution of the band’s music we searched the Grateful Dead subreddits,<sup>12</sup> the largest forums of their kind with a total of 174k members at the time of writing. We manually read through all pages with discussions on the differences between the band’s phases and collected all general descriptions that include the musical characteristics we study, including tempo, timbre, song lengths, etc, with references to specific years. The pages were found using combinations of the search keywords description, year, decade, 60s, 70s, 80s, 90s, progress, tempo, jam. Some of the most detailed year by year descriptions found are by Wolfman92097, WesternEstatesHOA, MrCompletely, and an anonymous deleted user [21–24], and some people, such as maximinus-thrax have listened to, rated, and briefly described every of the band’s more than 2300 shows [25, 26]. There are also many pages discussing the evolution of individual songs, such as [27]. We will now discuss our results while referring to relevant statements from the community where we can observe a consensus. 

Figure 5 juxtaposes different temporal aspects of the music. We can identify an overall increase in tempo in the 1980s of more than 10%, and a subsequent decrease in the middle of the decade. In terms of duration, the differences are even more dramatic, a sharp increase in the early 70s, followed by a gradual decrease by more than 20% until the late 80s, when duration starts increasing again. Note that the early curve segments in all plots, until about 1969, can be considered biased for the reasons stated in Sec- 

> 12 https://www.reddit.com/r/gratefuldead/, https: //www.reddit.com/r/grateful_dead/ 

tion 3.3. These observations coincide well with a notion in the community that, compared to the 70s, the early 80s are perceived as more energetic, faster paced, and containing fewer and less extensive jams. Wolfman92097 notes that in 1980 “the tempo [starts] to speed up a little”, in 1984 “musically the tempo has really sped up”, and in 1985 “the band slows the tempo a little.” [22] It is striking that this increase and decrease directly corresponds to the tempo curve in Figure 5. Although a bit more abstractly, leedye similarly highlights that exact time period: “79-84 stands out to me as the disco/cocaine era ... post 84 just seems to be a little more of the slow churned vanilla as opposed to that sweet mint chocolate chip.” [28] The same perception is true for individual songs. Discussing a recording of the song Eyes of the World, melwarren says “my 4 year old asked why EOTW was going so fast” and whenthattrainrollsby replies “They played it too fast for my taste in the 80’s.” [29] On a different page the forum members observe how the song went back to a refreshingly new slow tempo in 1990 [27]. These observations can also be verified in Figure 3. 

In terms of song duration, braney86 notes that the “late 70s was full of monster extended jams, and Jerry was absolutely on fire”, while MrCompletely says that “82 through 85 is a long uneven slide down ... 87 is the comeback, shows are very different, most are tightly executed, very light on jams ... 88 starting to stretch back out a little.” [23] Wolfman92097 also observes that in late 1986 “the setlists get much longer and way more experimental than they had been all year” and that in 1988 “jazz and extreme psychedelia gets added in.” [22] Many deadheads’ favorite years are 73/74, “the peak of their spacey, jazzy, psychedelic extended jams” according to devlinontheweb [30]. These observations again directly correspond to the plot in Figure 5. Song duration peaks in 1973, decreases throughout the late 70s and the early 80s with a turnaround point around 87/88, as perceived by MrCompletely. 

Figure 6 shows plots for dynamics features. We can observe a long peak in overall loudness of the soundboard recordings, spanning the entire 1980s. With increasing loudness we see a decrease in dynamic range, which may hint at an increased use of compression in the live mix. However, when comparing with Figure 5, we can also see a striking correlation between loudness and tempo, as well as between dynamic complexity and duration. Dynamic complexity may be another indicator of the amount of improvisation in the recordings, similar to song duration. The latter two, however, seem to be somewhat independent nonetheless. We can particularly observe a bulge in dynamic complexity in the late 70s which does not occur in the duration curve, and in the 90s duration increases while dynamic complexity decreases. On the other hand increased loudness may be a direct consequence of higher tempo and energy. EvilLinux admits that “If I am alone in the car, I usually will choose the 80’s. There is just more energy, more off the rails.” [31] An anonymous deleted user also says that “the Dead did play some incredible 

854 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
1. 4<br>loudness<br>dynamic complexity<br>1. 3<br>1. 2<br>1. 1<br>1. 0<br>0. 9<br>0. 8<br>1968 1972 1976 1980 1984 1988 1992 1996<br>time<br>relative deviation<br><!-- End of picture text -->

Figure 6: Bootstrapped LOWESS curves for dynamic essentia features (loudness_ebu128.short_term.median and dynamic_complexity) across all songs. 



<!-- Start of picture text -->
spectral complexity<br>spectral entropy<br>dissonance<br>1.1 5<br>1.1 0<br>1.0 5<br>1.0 0<br>0.9 5<br>1968 1972 1976 1980 1984 1988 1992 1996<br>time<br>relative deviation<br><!-- End of picture text -->

Figure 7: Bootstrapped LOWESS curves for spectral essentia features (spectral_complexity.median, spectral_entropy.median and dissonance.median). 

shows in the early to mid-80s. They had a "fatter" sound, especially Jerry” [24]. 

A similar observation can be made for spectral features (Figure 7). Complexity and entropy increase for the entire duration of the 1980s, while dissonance has a shorter peak in the late 80s. Many listeners agree that the 80s have an entirely different sound, to a large part characterized by the keyboarder Brent Mydland who played with the band from 1979 to 1990 and who used a greater variety of keyboards and many synthesizers. According to BeaverMartin, Brent “really adds a whole different texture to the vocals and keys,” [28] and WesternEstatesHOA says that “In 1983 the band truly takes off. The physical change of Brent’s new keyboard is enough to change the band’s sound alone. It has deep watery effects and adds so much depth to some of the more simple tunes.” [22] Wolfman92097: “83 Garcia [guitar] is a little more distorted and Brent is using more fake keyboard sounds Phil [bass] is loud.” [21] 

As for tonal content, Figure 8 shows a selection of features calculated as described in Section 3.1. Tonal, pitch, 



<!-- Start of picture text -->
1.0 8<br>pitch complexity<br>tuning complexity<br>1.0 6 tonal complexity<br>1.0 4<br>1.0 2<br>1.0 0<br>0.9 8<br>0.9 6<br>0.9 4<br>0.9 2<br>1968 1972 1976 1980 1984 1988 1992 1996<br>time<br>relative deviation<br><!-- End of picture text -->

Figure 8: Bootstrapped LOWESS curves for pitch, tuning and tonal complexity features. 

and tuning complexities run roughly in parallel and the period of 1980-84 is again demarcated, with a clear dip in all three features. This may again be due to the more streamlined faster performances and the lower degree of improvisation during this period. The late 1980s show parallels with the late 1970s, which may be related to the band starting to improvise more again. However, pitch and tuning complexities also seem highly correlated with dissonance (Figure 7) which may be related to timbre and the typical rich distorted and synthesizer-heavy 1980s Grateful Dead sound. 

## 5. CONCLUSION 

We have shown how evolutionary methods can not only be used for the study of general cultural trends in music, but also to investigate how the performances of a band change over time. We have also seen how we can improve the prediction accuracy of musical trends by considering the feature values relative to subsets of the data. It may be possible to apply a similar method in other situations, such as when studying the simultaneous evolution of the music of different composers, considering the music of each of them relative to their own work. We have also discovered limitations with the dataset used and suggest, in future work, to design a larger more systematic one in order to confirm our preliminary discoveries in this paper. Finally, while we have shown the potential reliability of the accounts of experienced listeners in the community, a more systematic collection and processing of online forum data may lead to more detailed results in the future. 

## 6. ACKNOWLEDGMENTS 

This work is supported in part by JST PRESTO No. JPMJPR20CB and JSPS KAKENHI Nos. 19H04137, 20K21813, 21K02846, 21K12187, 22H03661. 

## 7. REFERENCES 

- [1] Y. Liu, Q. Xiang, Y. Wang, and L. Cai, “Cultural style based music classification of audio signals,” in 2009 

855 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

IEEE International Conference on Acoustics, Speech and Signal Processing. IEEE, 2009, pp. 57–60. 

- [2] D. Moelants, O. Cornelis, and M. Leman, “Exploring african tone scales,” in 10th International Society for Music Information Retrieval Conference (ISMIR2009). International Society for music Information Retrieval, 2009, pp. 489–494. 

- [3] M. Panteli, E. Benetos, and S. Dixon, “A computational study on outliers in world music,” Plos one, vol. 12, no. 12, p. e0189399, 2017. 

- [4] C. Weiß, S. Balke, J. Abeßer, and M. Müller, “Computational corpus analysis: A case study on jazz solos.” in ISMIR, 2018, pp. 416–423. 

- [5] F. Thalmann, K. Yoshii, T. Wilmering, G. A. Wiggins, and M. B. Sandler, “A method for analysis of shared structure in large music collections using techniques from genetic sequencing and graph theory,” in Proceedings of the 21st International Society for Music Information Retrieval Conference, 2020. 

- [6] J. Serrà, Á. Corral, M. Boguñá, M. Haro, and J. L. Arcos, “Measuring the evolution of contemporary western popular music,” Scientific reports, vol. 2, no. 1, pp. 1–6, 2012. 

- [7] M. Mauch, R. M. MacCallum, M. Levy, and A. M. Leroi, “The evolution of popular music: Usa 1960– 2010,” Royal Society open science, vol. 2, no. 5, p. 150081, 2015. 

- [8] E. Deruty and F. Pachet, “The mir perspective on the evolution of dynamics in mainstream music,” in Proceedings of the 16th ISMIR Conference, vol. 723, 2015. 

- [9] C. Weiß, M. Mauch, S. Dixon, and M. Müller, “Investigating style evolution of western classical music: A computational approach,” Musicae Scientiae, vol. 23, no. 4, pp. 486–507, 2019. 

- [10] T. Parmer and Y.-Y. Ahn, “Evolution of the informational complexity of contemporary western music,” arXiv preprint arXiv:1907.04292, 2019. 

- [11] K. Choi and J. Stephen Downie, “A trend analysis on concreteness of popular song lyrics,” in 6th International Conference on Digital Libraries for Musicology, 2019, pp. 43–52. 

- [12] E. Nakamura and K. Kaneko, “Statistical evolutionary laws in music styles,” Scientific reports, vol. 9, no. 1, pp. 1–11, 2019. 

- [13] F. C. Moss, M. Neuwirth, and M. Rohrmeier, “The line of fifths and the co-evolution of tonal pitch-classes,” Journal of Mathematics and Music, pp. 1–25, 2022. 

- [14] M. Benson, Why the Grateful Dead Matter. University Press of New England, 2016. 

- [15] M. C. Tift, “Grateful dead musicking,” in All Graceful Instruments: The Contexts of the Grateful Dead Phenomenon. Cambridge Scholars Publishing, 2021. 

- [16] C. Weiß and M. Müller, “Quantifying and visualizing tonal complexity,” in Proceedings of the Conference on Interdisciplinary Musicology (CIM), 2014, pp. 184– 187. 

- [17] K. R. Page, S. Bechhofer, G. Fazekas, D. M. Weigl, and T. Wilmering, “Realising a layered digital library: exploration and analysis of the live music archive through linked data,” in 2017 ACM/IEEE Joint Conference on Digital Libraries (JCDL). IEEE, 2017, pp. 1–10. 

- [18] W. S. Cleveland and S. J. Devlin, “Locally weighted regression: an approach to regression analysis by local fitting,” Journal of the American statistical association, vol. 83, no. 403, pp. 596–610, 1988. 

- [19] D. Malvinni, Grateful Dead and the Art of Rock Improvisation. Scarecrow Press, 2013. 

- [20] O. Longcroft-Wheaton, “The stylistic development of the grateful dead: 1965-1973.” Ph.D. dissertation, University of Surrey, 2020. 

- [21] “Can you tell when a song was performed just by hearing it?” https://www.reddit.com/r/gratefuldead/ comments/80ifqt/can_you_tell_when_a_song_was_ performed_just_by/, accessed 2022-08-30. 

- [22] “Describing each year of the 80’s,” https: //www.reddit.com/r/gratefuldead/comments/7x5zs9/ describing_each_year_of_the_80s/, accessed 2022-0830. 

- [23] “1980’s Era Dead,” https://www.reddit.com/r/ gratefuldead/comments/1vf47n/1980s_era_dead/, accessed 2022-08-30. 

- [24] “Intro to listening to the Dead!” https: //www.reddit.com/r/gratefuldead/comments/3crjek/ intro_to_listening_to_the_dead/, accessed 2022-0830. 

- [25] “Listened to all the shows. Listened to the best again. Here’s the top 50 or so,” https: //www.reddit.com/r/gratefuldead/comments/sny6dx/ listened_to_all_the_shows_listened_to_the_best/, accessed 2022-08-30. 

- [26] “Grateful Dead Reviews,” https:// raw.githubusercontent.com/maximinus/ grateful-dead-reviews/master/dead_reviews.txt, accessed 2022-08-30. 

- [27] “When did Eyes get slowed down?” https: //www.reddit.com/r/gratefuldead/comments/vax00p/ when_did_eyes_get_slowed_down/, accessed 202208-30. 

856 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

- [28] “Fans of the 80s-90s - what do you like so much about this era?” https://www.reddit.com/r/gratefuldead/ comments/sdufh5/fans_of_the_80s90s_what_do_you_ like_so_much_about/, accessed 2022-08-30. 

- [29] “What are the fastest versions of Dead songs?” https: //www.reddit.com/r/grateful_dead/comments/57btul/ what_are_the_fastest_versions_of_dead_songs/, accessed 2022-08-30. 

- [30] “Best decade and year?” https://www.reddit.com/ r/gratefuldead/comments/pdey6g/best_decade_and_ year/, accessed 2022-08-30. 

- [31] “Can we just cut the shit and agree that the best Dead is from the 70s? Who’s with me?” https: //www.reddit.com/r/gratefuldead/comments/rblwiy/ can_we_just_cut_the_shit_and_agree_that_the_best/, accessed 2022-08-30. 

857 

