---
paper_id: "000080"
year: 2021
title: "Tracing Affordance and Item Adoption on Music Streaming Platforms 642-649"
source_url: "https://archives.ismir.net/ismir2021/paper/000080.pdf"
---

# **TRACING AFFORDANCE AND ITEM ADOPTION ON MUSIC STREAMING PLATFORMS** 

**Dougal Shakespeare**<sup>1</sup> **Camille Roth**<sup>1</sup><sup>_,_2</sup> 

1 Computational Social Science Team, Centre March Bloch, Berlin 

2 CNRS, France 

dougal.shakespeare@cmb.hu-berlin.de, roth@cmb.hu-berlin.de 

## **ABSTRACT** 

Popular music streaming platforms offer users a diverse network of content exploration through a triad of affordances: _organic_ , _algorithmic_ and _editorial_ access modes. Whilst offering great potential for discovery, such platform developments also pose the modern user with daily adoption decisions on two fronts: platform affordance adoption and the adoption of recommendations therein. Following a carefully constrained set of Deezer users over a 2-year observation period, our work explores factors driving user behaviour in the broad sense, by differentiating users on the basis of their temporal daily usage, adoption of the main platform affordances and the ways in which they react to them, especially in terms of recommendation adoption. Diverging from a perspective common in studies on the effects of recommendation, we assume and confirm that users exhibit very diverse behaviours in using and adopting the platform affordances. The resulting complex and quite heterogeneous picture demonstrates that there is no blanket answer for adoption practices of both recommendation features and recommendations. 

## **1. INTRODUCTION** 

The contemporary music streaming platform is a far cry from the digital repository which it once was. Increased diversification at a platform level has resulted in a range of affordances that is, modes of content access projected by the platform to the user, which allow one to explore a platform’s ever expanding musical catalogs through novel paths. No longer is it necessary for the avid music listener to spend hours on end trawling through digital repositories to find their ‘niche’, thus performing a direct, interestdriven exploration of the whole catalog that is typically denoted as _organic_ ( _O_ ) use. Rather, they are free to draw upon further affordances commonly encapsulated within state-of-the-art platforms which provide some level of assistance or guidance: either purely based on _algorithmic_ 

> © Dougal Shakespeare, Camille Roth. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). **Attribution:** Dougal Shakespeare, Camille Roth, “Tracing Affordance and Item Adoption on Music Streaming Platforms”, in _Proc. of the 22nd Int. Society for Music Information Retrieval Conf.,_ Online, 2021. 

( _A_ ) devices or on some level of _editorial_ ( _E_ ) curation. While at one level, it is true that affordance diversification yields increased potentials for exploration, this also comes at the price of greater emphasis being placed on user platform proficiency – questions of what affordance to employ and what items therein to adopt quickly become frequent decisions the modern user must deal with. 

In our work we trace the aforementioned user tendencies through the notion of adoption on two fronts: _affordance adoption_ (among the triad _O, A, E_ ) and _item adoptions_ therein (i.e., item transfers across affordances). Through a comprehensive quantitative analysis of user listening practices on the popular music streaming platform, Deezer, our work sheds light on the varied and often heterogeneous nature of adoption and behavioural differences amongst users. The contribution of this work both sits within and helps to re-frame the growing body of literature which appraises the interconnected effects of human behaviour and algorithmic influence via an organic comparison. 

## **2. LITERATURE REVIEW** 

## **2.1 Appraising Algorithmic Influence via an Organic Comparison** 

Whilst historically the primary role of a music Recommender System (mRS) on streaming platforms was to facilitate the efficient personalised exploration of a platform’s often vast musical catalog thereby minimising the risk of _choice overload_ [1], a substantial body of multi-disciplinary literature [2–5] points towards the conclusion that user exploration may still in practice, remain confined to a minute fraction of homogeneous musical content – a phenomenon famously denoted as the _‘filter bubble’_ [6]. Similarly in recent years a growing body of simulation based RS literature has also shed light on the tendency for feedback loops to emerge as a product of algorithmic recommendation and (simulated) human consumption [7–10]. Nonetheless, while the tendency for such practices to emerge is clearly outlined in literature, a less trivial second order question still remains ambiguous: 

_To what degree is user platform behaviour primarily a product of algorithmic influence or rather, an autonomous organic process imposed by the user themselves?_ 

642 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

work seeks to fill. 

In light of such questions, a novel branch of the state of the art has sought to measure algorithmic influence by drawing parallels to a user’s organic platform behaviour. Roth conceptualises this debate through what he coins the _‘ROM-COM dichotomy’_ [11] – the tendency for filtering algorithms to either Read Our Minds (ROM) acting as cognitive aids to facilitate organic exploration or rather, Change Our Minds (COM) algorithmically distorting a prior organic preference. Literature appraising algorithmic influence through an organic reference has been applied to a range of multi-disciplinary contexts. Bakshy et al. [12] study the role of Facebook’s NewsFeed algorithm in exposing users to cross-partisan content through an organic reference. Their work finds filtering algorithms to have minimal effect in reducing cross-partisan information in comparison to the organic selection processes suggesting a user’s diversity limitation may be principally due to human pre- and post-selection. In the music domain, Epps-Darling et al. [13] study the role of Spotify’s algorithmic influence on gender representation through an organic reference point. Their findings show user’s organic preference towards male artists to be marginally higher than that recommended by Spotify’s mRS, again suggesting the human organic bias to be stronger than that generated algorithmically. Anderson et al. [14] also analyse diversity with respect to organic vs programmed (algorithmic/editorial) listening events on Spotify. Through the generation of a usage-based embedding space, they find algorithmically-driven exploration to be less diverse than organic, providing evidence for a COM effect. 

Furthermore, recent literature on music streaming uses paints a picture of divergent practices dependent upon the user’s degree of organic-algorithmic usage and actualised with respect to context and user mindsets [15, 16]. Thus, we commence our work with the prior hypothesis that user platform behaviour is largely varied - there is no _average user_ for which a blanket answer to algorithmic influence may be applied. 

## **2.2 Item Adoption in Recommender Systems** 

Whilst item adoption in terms of consumption confined to a given affordance has been covered extensively and critically both in terms of user studies [17, 18] and user modelling [19–21], literature concerning item adoption in relation to the dynamic transfer of items across affordances remains to date, sparse. Nonetheless, the adoption of music streaming platforms independent of their affordances has notably been studied in the field of Cultural Studies. In the works of Datta et al. [22], streaming adoption is shown to lead to substantial increases in both the quantity and diversity of music consumed by a user. Similarly, Rushan et al. [23] also study factors of the platform interface which in itself, determine a consumer’s decision to adopt music streaming platforms as a result of increased platform familiarisation. Still, adoption with respect to transitions across platform affordances remains a literature void which this 

## **2.3 Temporal Dimensions of mRS Usage** 

Time of day information has been evidenced to be an important signal in disentangling platform behaviour [24] and has thus in recent years, become a commonly utilised signal in context dependent RS literature [25–27] to increase personalisation and accuracy of recommendations. What is more, user studies have also revealed that both the time of day and week can play a substantial role in mediating user platform experience and downstream projected user behaviour [28, 29]. Utilising such rich temporal signals encapsulated within listening logs, our work seeks to explore the degree to which adoption on both fronts may differ across temporal daily usages. 

## **3. METHODOLOGY** 

## **3.1 Listening Events Data Set** 

We work with about 2 years of listening histories from about 13K Deezer users who registered in the month of September 2017. We constrain our field of observation to users who remained active over the entire observation period. Formally, we impose a maximum inter-event time threshold of 10 days thus ensuring that users rely on the platform for a regular source of music. This eventually yields 2701 users which forms the ultimate user base for our analysis. We discard listening events <30s as these are deemed as so-called _‘skips’_ . We further merge unique song identifiers which share identical audio embeddings in a pre-build latent space supplied by Deezer (see [30] for use case / generation details). This prevents double couting of identical songs which may have been mis-labeled as distinct. For each listening event we characterise the affordance used to retrieve content of which on Deezer there exists a triad: _organic_ ( _O_ ), _algorithmic_ ( _A_ ) and _editorial_ ( _E_ ). Our research commences from a strict ternary classification of affordance taxonomies drawing influence from the existing body of literature of which this work closely relates [13, 14, 31]. We classify _A_ affordances as those that refer to the platform’s plethora of Recommender System (RS) architectures (e.g., the popular Flow playlist on Deezer) whilst _E_ affordances correspond to curated playlists (such as recommended playlists variously called “10s electronic”, “Rock & Chill”, etc.) of which the majority are mostly human constructed. All remaining modes of access are classified as _O_ including for instance, the search bar, user-constructed playlists and more broadly, modes of content access which do not utilise any degree of recommendation. 

## **3.2 Defining User Classes** 

**Affordance Adoption.** We capture user adoption of platform affordances through the proportion of content accessed via each of the platform’s three main affordances after aggregating listening histories. The listening history of a given user is represented by the temporally-ordered list 

643 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 



<!-- Start of picture text -->
E<br>10<br>0.8 0.2<br>0.6 0.4<br>0.6<br>0.2 0.8<br>1<br>0.8 0.6<br>A<br><!-- End of picture text -->

**Figure 1** . Ternary plot of affordance adoption classes _o_ + (blue), _o_ (grey), _œ_ (green), _a_ (purple), disks represent centroid positions. Crosses represent corrected centroid positions after taking into account the pre-adoption origin of plays (see Sec. 5). 

of listening events over our observation period, formally defined as: 



<!-- Start of picture text -->
P = ( si, ti, fi ) i≤n<br><!-- End of picture text -->

where _si_ is the song ID, _ti_ the timestamp, and _fi ∈ {A, E, O}_ the affordance used for the _i_ -th listening event. We accordingly denote the sublist of _P_ restricted to a = given affordance _F_ as _PF_ ( _si, ti, fi_ ) _i≤n ∧ fi_ = _F_ Considering the proportion of plays accessed _organically, algorithmically_ and _editorially_ respectively, the affordance profile of a given user is defined by the triplet ( _|PO|/|P |, |PA|/|P |, |PE|/|P |_ ) which sums to 1 and can be represented as a barycentric coordinate in ternary space (see Figure 1). Performing a k-means clustering ( _k_ = 4) across affordance profiles yields 4 distinct classes of users which we label as follows: very organic ‘ _o_ +’ (1786 / 65.98%), organic ‘ _o_ ’ (429 / 15.85%), algorithmic ‘ _a_ ’ (224 / 8.27%), organic/editorial ‘ _œ_ ’ (268 / 9.90%). We note that we rather deal with bins, areas or classes than with well-separated clusters per se. Thus, from herein we refer to affordance adoption clusters as classes. Already, a highly varied picture of affordance adoption on the platform emerges along with a shared preliminary benchmark: for all classes, users on average display some degree of _O_ adoption whilst the same cannot be said for _A_ and _E_ . Indeed, at first sight it appears Deezer users do not typically adopt affordances on all fronts but rather, use the platform predominately as an organic catalog much the way one would search through a traditional song library, albeit a much larger one here. However, as we shall later detail, a user’s tendency to consume mostly _O_ content may be misleading: if a significant proportion of a user’s _O_ catalog is a product of _A_ or _E_ adoption the very definition of what it means to adopt _O_ affordances is brought into question. 

**Exploration Behaviour.** Beyond sheer user activity over the entire observation period denoted by play counts _|P |_ , 



<!-- Start of picture text -->
一·A<br>PF(h)<br>PF(h)<br>0.2<br>PF(h) 0.0<br>-0.2<br><!-- End of picture text -->

**Figure 2** . Normalised platform affordance time-of-day activity. Aggregate levels are shown (top) followed by z- normalised activity (middle) and residual de-trended activity levels (bottom). 

we consider a notion of _redundancy_ [29] quantified as a measure of how much a given user saturates their listening catalog (i.e., plays the same songs repeatedly), formally defined as _R_ = 1 _−|S|/|P |_ where _S_ = _{s|_ ( _s, t, f_ ) _∈ P }_ is the set of unique songs in _P_ . 

We additionally characterise the diversity of a user’s exploration using a pre-built 32-dimensional latent space _E_ constructed from low-level audio features via metric learning [30]. The audio embeddings were primarily used by Deezer for the task of artist disambiguation (i.e., where artists had the same name but were stylistically unique). Thus, the construction of _E_ maximises distance for acoustically dissimilar artists while acoustically similar artists remain close in this space. For each user, we compute their average pairwise _cosine distances_ between audio embeddings _Es_ for each _s ∈ S_ and ultimately, report average values. 

**Temporal Time of Day Analysis.** Platform usage can also be seen to vary significantly over the elapsed day at both a aggregate platform and user-centric level. Considering the former first, we compute and plot aggregate activity levels across all affordances at each hour of the day (Fig. 2, top row). Activity is found to largely consist of _O_ followed by _A_ and _E_ at much lower magnitudes, consistent with what has been previously detailed. Without loss of generality, we denote _P_ as the platform-level history for all users (i.e., the whole dataset). To analyse temporal trends independent of magnitude, we consider hourly play counts for each affordance: 



<!-- Start of picture text -->
PF  ( h ) = ( si, ti, fi ) i≤n ∧ ( ti ’s hour= h )  ∧ ( fi = F  )<br><!-- End of picture text -->

to which we subsequently apply a z-normalisation relative to daily play count averages defined as: 



<!-- Start of picture text -->
�<br>PF  ( h ) = PF  ( h )  −PF  ( h ) h<br>σPF  ( h )<br><!-- End of picture text -->

These normalised activity levels (Fig. 2, second row) reveal three peaks of gradually increasing magnitude, respectively in the early morning, morning, and afternoon 

644 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 



<!-- Start of picture text -->
1600  daily user avee eser all-rounder night owl<br>1400<br>1200<br>Pτ(h) 1000<br>800<br>600<br>400<br>200<br>1.00<br>0.75<br>0.50<br>Pτ(h) 0.250.00<br>-0.25<br>-0.50<br>�0.75<br>-1.00<br><!-- End of picture text -->

**Figure 3** . Normalised time-of-day activity levels for each time-of-day class. Aggregate levels are shown (top) followed by residual de-trended activity levels (bottom). 

(16-17:00), from which a gradual decay in activity is experienced. To capture temporal adoption variations of affordances with respect to one another, we finally apply socalled _‘detrending’_ as per [32] by comparing the above z-normalisations _P_<sup>�</sup> _F_ ( _h_ ) relative to other affordances, formally defined as: 



<!-- Start of picture text -->
�<br>P � F  ( h ) = P � F  ( h )  − ( h ) F<br><!-- End of picture text -->

Affordance adoption at a platform level clearly varies across hours of the day (Fig. 2, bottom row). In both the early morning and between the afternoon hours and evening we observe a tendency to favour _O_ respective to _A_ and _E_ affordance life cycles in the same time blocks (i.e. independent of magnitude). Otherwise, either _A_ or _E_ seem to be favoured (again, in relative trend) and essentially appear to exhibit bi-modal relative adoption peaks across the day, albeit at different moments (rather in the morning for _A_ and in the early morning and early afternoon for _E_ ). 

We complement the temporal platform-level analysis by examining daily patterns at the user level, as users will commonly have varied activity levels on music streaming platforms [33] which may be missed by a standalone platform level analysis. To this end, we consider user-level hourly activity aggregated over all affordances _P_ ( _h_ ) = ( _si, ti, fi_ ) _i≤n ∧_ ( _ti_ ’s hour= _h_ ) . As in [29], we subsequently cluster users using k-means ( _k_ = 4 again) applied on _P_ ( _h_ ) as a 24-dimensional unit vector. We observe 4 distinct user-centric behavioural dynamics which we label as follows: the _average user_ (726 / 26.82%), the _night owl_ (928 / 34.28%), the _all rounder_ (245 / 09.05%) and the _daily user_ (808 / 29.85%). We represent the variations of _P_ ( _h_ ) on Fig. 3 by applying the same type of normalization as used above for platform-level quantities _P_ ( _h_ ), except that we consider temporal clusters _T_ instead of affordances _F_ i.e., _PT_ ( _h_ ) in place of _PF_ ( _h_ ). 

## **3.3 Item Adoption** 

In this work we focus exclusively on item adoptions which are imposed directly by the user themselves and thus, we 

only characterise the tendency for users to adopt _A_ or _E_ songs into their _O_ catalog. To capture this behaviour, we introduce the novel measure of _adoption α_ . At a high level, an item can be said to be adopted the first time it has been played organically by a user given that the song was first recommended through some affordance _F_ and not played organically as a prior. Since we are interested in item adoption and thus unique songs, we now focus on song sets rather than lists of plays i.e., _S_ . We outline two possible mutually exclusive song sets, denoted _φ_ and _ρ_ , to differentiate songs which could have been adopted yet were not, from those which were actually adopted: 

**– Adoption feasible,** _φ_ , denoting the set of songs which were played through _F_ but not via _O_ and thus, had the potential to be adopted yet were not: 



<!-- Start of picture text -->
φF = s ∈ S ∃ ( s, t, F )  ∈ P,  ∄( s, t ′ , O )  ∈ P<br><!-- End of picture text -->

**– Adoption realised,** _ρ_ , denoting the set of songs which were played via _F_ as a prior and were consumed through _O_ at least once subsequently: 



<!-- Start of picture text -->
ρF = s ∈ S ∃ ( s, t, F )  ∈ P, t < ( s,t min ′ ,O ) ∈P t′<br><!-- End of picture text -->

Furthermore, if a user is exposed to more recommendations before ultimately making the decision to adopt, this may indicate a weaker influence of the platform’s affordance or that the act of adoption is less likely to be a direct product of it (for instance the user might have heard the song from an external source such as the radio). To capture this intuition, we introduce _rF_ ( _s_ ), the number of recommendations of song _s_ which appeared through _F_ before organic adoption: 



<!-- Start of picture text -->
rF  ( s ) = Ji ( s, t, F )  ∈ P t < ( s,t min ′ ,O ) ∈P t Ji ′<br><!-- End of picture text -->

to which we apply a polynomial scaling function which decays to give more weight to lower numbers of recommendations - a similar practice to how listening counts are often scaled logarithmically in mRS literature [34,35]. 

We assess the relative impact of item adoption at two levels of abstraction. Foremostly, with respect to the number of items which both could have been and were adopted by the user through _F_ i.e., _|φF |_ + _|ρF |_ . Formally let this be defined by: 



<!-- Start of picture text -->
∑ s∈ρ rF  ( s ) −λ<br>αF =<br>|φF |  +  |ρF |<br><!-- End of picture text -->

where _λ ∈_ (0 _,_ 1] is a hyperparameter which affects the degree of polynomial decay with respect to algorithmic impact. In our experiments we set the value of _λ_ = 0 _._ 5. We note our choice of _λ_ is cautious and should in future work be more refined with statistical and qualitative user studies exploring the role of repeated affordance recommendation prior to adoption. 

Secondly, we normalise adoption with respect to the number of unique items consumed via _O_ , thereby capturing the relative impact of algorithmic adoption in a user’s 

645 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

||||o+|||||o|||
|---|---|---|---|---|---|---|---|---|---|---|
||_All_<br>_rounder_|_Average_<br>_user_|_Night_<br>_owl_|_Daily_<br>_user_|_All_|_All_<br>_rounder_|_Average_<br>_user_|_Night_<br>_owl_|_Daily_<br>_user_|_All_|
|_|P|_|***26.62K**|15.59K|*20.87K|15.94K|18.58K|**26.09K**|15.63K|19.68K|16.88K|18.01K|
|_R_|***0.90**|0.85|0.86|*0.83|0.85|***0.82**|0.77|0.77|0.77|0.77|
|_αA_|**0.28**|0.25|0.28|0.25|0.25|**0.15**|0.14|0.15|0.14|0.14|
|_αE_|0.26|**0.27**|0.24|*0.21|0.25|0.18|**0.19**|0.16|0.15|0.17|
|_α_<sup>_′_</sup><br>_A_|0.01|0.02|**0.02**|0.02|0.01|0.06|**0.06**|0.06|0.05|0.06|
|_α_<sup>_′_</sup><br>_E_|0.02|**0.02**|0.02|0.02|0.02|**0.03**|0.02|0.02|0.03|0.02|
|_E_ dist.|0.28|0.29|0.29|**0.29**|0.28|0.28|0.29|**0.30**|0.29|0.29|
||||a|||||œ|||
|_|P|_|**41.20K**|15.06K|16.18K|19.75K|19.01K|**23.80K**|15.40K|19.68K|23.09K|20.14K|
|_R_|***0.85**|0.77|_0.74_|0.77|0.77|0.77|0.74|**0.77**|0.76|0.76|
|_αA_|**0.10**|0.09|0.09|0.09|0.09|0.17|0.16|**0.20**|0.15|0.17|
|_αE_|0.20|0.14|0.15|0.13|0.14|0.14|0.14|**0.16**|0.13|0.14|
|_α_<sup>_′_</sup><br>_A_|0.08|**0.08**|0.08|0.08|0.08|**0.03**|0.02|0.02|0.02|0.02|
|_α_<sup>_′_</sup><br>_E_|0.03|**0.03**|0.02|0.03|0.03|0.05|0.05|**0.05**|0.05|0.05|
|_E_ dist.|0.29|0.30|0.29|**0.30**|0.30|0.28|0.29|0.28|**0.29**|0.29|



**Table 1** . Experimental results across two static affordance and temporal _time of day_ user classes. Values in bold represent the top value, while marked with * are results where the difference is statistically significant (two tailed t-test, _α_ = 0 _._ 05 _/n_ after Bonferroni correction). 

## overall organic listening catalog. Formally, 



<!-- Start of picture text -->
αF ′ =  ρF /|{s ∈ S | ∃ ( s, t, O )  ∈ P }|<br><!-- End of picture text -->

We note that this value is bounded by the number of organic streams in a user’s listening history but nonetheless, we deem this to be a useful measure to capture the influence of item adoption in bringing into question the very meaning of what is deemed organic. 

## **4. RESULTS** 

**Temporal Affordance Adoption Variations.** We first examine the distribution of affordance classes across timeof-day classes. As shown in Figure 4 we observe two fundamental preliminary findings: (1) daily users are more heavily composed of both _a_ and _œ_ users respective to other time-of-day classes; (2) _o_ + users are more proportionally likely to reside within the all rounder and, to a lesser extent, night owl class. Framed differently, users who adopt almost solely _O_ are more likely to favour platform activity in the evening hours of the day whilst users who more heavily _A/E_ -adopt are more likely to favour activity in the day time hours. Once again, our findings reiterate what was observed from our temporal platform evaluation – the use of recommendation affordances corresponds to different categories of temporal use as well as, we contend, different types of users. 

**Characterising platform behaviour.** To further disentangle the respective use cases we now characterise behavioural dynamics for each time-of-day and affordance class. Focusing first on affordances, we attain results that go against the grain of a diversity-constraining narrative (see Table 1). Users who _A_ -adopt more frequently are found to have more diverse exploration in _E_ whilst maintaining relatively low redundancy levels as measured by _R_ . 



<!-- Start of picture text -->
All rounder 0.74 0.49 0.7 1.2 1.4<br>1.2<br>1.0 0.95 1.1 0.99<br>1.0<br>Average user<br>1.4 1.3 1.1 0.88<br>Time-of-day u cla s es<br>-0.8<br>Daily user<br>0.72 0.88 0.95 1.1 -0.6<br>Night owl<br>a. 0e +0<br>Affordance u classes<br><!-- End of picture text -->

**Figure 4** . Affordance vs. time-of-day distributions. Values are normalised such that above or below 1 indicate respectively similar, over- or under- representation of affordance classes respective to those found globally. 

It appears the consumption of _A_ content in fact diversifies a user’s _P_ at both a behavioural and deeper content-based level whilst on the contrary, _o_ + users are found to saturate their listening catalog reflected in the high _R_ levels attained. 

Regarding item adoption within affordance classes we observe both _a_ and _œ_ users to have low levels of _αA_ and _αE_ respectively. This can be interpreted as a passivity to recommendations - such users are more likely to use _A_ and _E_ affordances regularly but on a so-called _auto-pilot_ akin to radio consumption. Nonetheless, when _a_ and _œ_ users do take the decision to adopt this makes a substantial impact to their _O_ catalog and thus, the dispersion of users in the _A, E, O_ ternary space as we shall later detail. Drawing parallels to a more pure organic behaviour through the _o_ +, we observe polar opposite dynamics in 

646 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

comparison to the _a_ and _œ_ users. Whilst _o_ + users _A/E_ - adopt sparsely, their ultimate downstream platform use is less recommendation-skeptic reflected in the much higher levels of item adoption rates for _A_ and _E_ affordances attained ( _αA_ = 0 _._ 25, _αE_ = 0 _._ 25) but with minimal impact to the constitution of their overall _O_ catalog. From the detailed findings it is clear that our preliminary assumption that users display varied behavioural dynamics holds true: users diverge dramatically regarding their affordance adoption, adoption of items therein and perhaps most importantly, subsequent downstream impact experienced to their overall _O_ catalog. 

We next study the effect of temporal preference upon behavioural practices. For a given affordance class and behavioural measure (e.g. _o_ + _, R_ ) we perform two-tailed Welch’s unequal-variance paired t-tests [36] over all 6 pairs of temporal classes which form the affordance class i.e., ( _all rounder_ , _average user_ ), ( _all rounder_ , _daily user_ ), ( _all rounder_ , _night owl_ ), ( _average user_ , _daily user_ ), ( _average user_ , _night owl_ ), ( _daily user_ , _night owl_ ). For a given temporal class, Table 1 marks a value as significant if _p < α/_ 6 (i.e., after adjusting for errors via Bonferroni correction [37]) is attained for all 3 pairwise t-tests performed containing the temporal class under consideration (e.g. ( _all rounder_ , _average user_ ), ( _all rounder_ , _daily user_ ), ( _all rounder_ , _night owl_ )). The results show that users vary significantly with respect to activity and _R_ levels. Central to this finding is the _all rounder_ who displays significantly higher activity levels for _o_ + users but at the price of saturating their listening catalogue reflected in the significantly higher _R_ levels across the majority of affordance classes. Such findings suggest that for a given affordance class, significant deviations across temporal classes only occur for low level behavioural features. There is no clear downstream propagation to a user’s deeper musical preferences, reflected by diverse musical content in an audio embedding space and preference for item adoption – a theory which we shall now test empirically. 

**Disentangling heterogeneous platform behaviour.** To disentangle the influence of time-of-day preference and affordance adoption on user item adoption and reactions to recommendations we next perform a factorial ANOVA, shifting each behavioural attribute to be the dependent variable whose variance we seek to explain. We primarily fit our data to an OLS model _Y_ = _β_ 0 + _β_ 1 _F_ + _β_ 2 _T_ + _β_ 3 _FT_ + _ε_ (where _F_ and _T_ represent affordance and time-of-day labels respectively) before subsequently applying a factorial ANOVA. Due to space constraints, the full ANOVA results table is not included however we now detail the results most relevant to this work. As hypothesised, we observe the only effect size ( _ηp_<sup>2) for which tempo-</sup> ral classes may have both a moderate and significant effect is with regard to a user’s activity _|P |_ . On the contrary, affordance classes offer a moderate-to-high explanatory factor for the variance of the remaining behavioural attributes, foremostly adoption. Perhaps most interestingly, the effect of affordance classes on _αA_ is particularly strong (0 _._ 11) implying that a user’s decision to adopt items into their or- 

ganic catalog may, as previously hypothesised, be principally a product of adopting recommendation affordances. 

For completeness we ultimately examine the effect of sequential time-of-day and affordance adoption influence on the notion of what is meant by an organic stream. Contrary to our preliminary belief that organic access acted as a benchmark for Deezer platform exploration, we observe users to actually be more algorithmic and editorial than first thought, albeit indirectly. Considering a stream to belong to the affordance in which it was adopted as opposed to organic we recompute centroids for each affordance class. In cases where a stream was both adopted via _A_ and _E_ we deem that the item was adopted via the affordance which had the most streams prior to adoption. As shown in Fig. 1, we observe all affordance adoption classes centroids to experience a marked shift towards _A_ and _E_ poles – even more so for users who are already closer to these poles i.e., particularly for _a_ and _œ_ users. 

## **5. CONCLUDING REMARKS** 

In a time where the modern music streaming platform encapsulates a myriad of modes of accessing content, users may and do personalise their platform use in highly varied ways. By acknowledging, assuming and confirming the diversity of user platform behaviour, our work traces the interconnected yet surprisingly sequential factors which drive affordance and item adoption. Our results paint a highly complex picture of user platform behaviour whereby time-of-day preference mediates low-level platform behaviour (activity levels) while affordance adoption preference mediates the ultimate higher-level decision to adopt content into one’s _O_ catalog, a factor which is indeed more reflective of musical taste. 

Coming full circle, the heterogeneity of item adoption and its subsequent impact brings into question the nature of what constitutes an _O_ stream - after taking into consideration the role of adoption, users are indeed found to be markedly less organic than was initially thought. This, in turn, may redefine what affordance adoption really is and perhaps most importantly, challenge the emerging literature which seeks to appraise _A_ influence via an _O_ comparison. Our work hints at the non-binary nature of _O_ which should be carefully considered and analysed. Although beyond the scope of this work, we suggest a fruitful future direction could be to explore non-human item adoptions (i.e., item transfers from _O → A|E_ ). We also advice for future work to explore the role of temporal preference upon adoption practices at varied degrees of abstraction be it weekly, monthly or longitudinal. On the whole, this work aims to hint at a direction that currently remains relatively unexplored in outstanding scholarship concerning the impact of RS on the diversity of user consumption: that user behaviour determines how recommendation affordances are being adopted. In practice, this type of work and approach could be utilised at the platform level to further the development of context-dependent RS, providing musical recommendations which are far more suited to the high variety of user’s driving use cases. 

647 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

## **6. REFERENCES** 

- [1] D. Bollen, B. P. Knijnenburg, M. C. Willemsen, and M. Graus, “Understanding choice overload in recommender systems,” in _Proceedings of the Fourth ACM Conference on Recommender Systems_ , ser. RecSys ’10. New York, NY, USA: Association for Computing Machinery, 2010, p. 63–70. [Online]. Available: https://doi.org/10.1145/1864708.1864724 

- [2] M. Airoldi, “The techno-social reproduction of taste boundaries on digital platforms: The case of music on youtube,” _Poetics_ , p. 101563, 2021. [Online]. Available: https://www.sciencedirect.com/ science/article/pii/S0304422X21000462 

- [3] N. Seaver, “Captivating algorithms: Recommender systems as traps,” _Journal of Material Culture_ , vol. 24, no. 4, pp. 421–436, 2019. 

- [4] T. Bonini and A. Gandini, ““first week is editorial, second week is algorithmic”: Platform gatekeepers and the platformization of music curation,” _Social Media + Society_ , vol. 5, no. 4, pp. 1–11, 2019. 

- [5] T. T. Nguyen, P.-M. Hui, F. M. Harper, L. Terveen, and J. A. Konstan, “Exploring the filter bubble: The effect of using recommender systems on content diversity,” in _Proceedings of the 23rd International Conference on World Wide Web_ , ser. WWW ’14. New York, NY, USA: Association for Computing Machinery, 2014, p. 677–686. [Online]. Available: https://doi.org/10.1145/2566486.2568012 

- [6] E. Pariser, _The Filter Bubble: What the Internet Is Hiding from You_ . The Penguin Press, 2011. 

- [7] A. Ferraro, D. Jannach, and X. Serra, “Exploring longitudinal effects of session-based recommendations,” _Fourteenth ACM Conference on Recommender Systems_ , Sep 2020. [Online]. Available: http://dx.doi.org/10.1145/3383313.3412213 

- [8] A. Ferraro, X. Serra, and C. Bauer, “Break the loop: Gender imbalance in music recommenders,” in _Proceedings of the 2021 Conference on Human Information Interaction and Retrieval_ , ser. CHIIR ’21. New York, NY, USA: Association for Computing Machinery, 2021, p. 249–254. [Online]. Available: https://doi.org/10.1145/3406522.3446033 

- [9] D. Jannach, L. Lerche, I. Kamehkhosh, and M. Jugovac, “What recommenders recommend: an analysis of recommendation biases and possible countermeasures,” _User Modeling and User-Adapted Interaction_ , vol. 25, pp. 427–491, 2015. 

- [10] J. Zhang, G. Adomavicius, A. Gupta, and W. Ketter, “Consumption and performance: Understanding longitudinal dynamics of recommender systems via an agent-based simulation framework,” _Info. Sys. Research_ , vol. 31, no. 1, p. 76–101, Mar. 2020. [Online]. Available: https://doi.org/10.1287/isre.2019.0876 

- [11] C. Roth, “Algorithmic distortion of informational landscapes,” _Intellectica_ , vol. 70, no. 1, pp. 97–118, 2019. 

- [12] E. Bakshy, S. Messing, and L. A. Adamic, “Exposure to ideologically diverse news and opinion on facebook,” _Science_ , vol. 348, no. 6239, pp. 1130–1132, 2015. [Online]. Available: https://science.sciencemag.org/content/348/6239/1130 

- [13] A. C. Epps-Darling, H. Cramer, and R. T. Bouyer, “Artist gender representation in music streaming,” in _Proceedings of the 21st International Society for Music Information Retrieval Conference_ . Montreal, Canada: ISMIR, Oct. 2020, pp. 248–254. [Online]. Available: https://doi.org/10.5281/zenodo.4245416 

- [14] A. Anderson, L. Maystre, I. Anderson, R. Mehrotra, and M. Lalmas, “Algorithmic effects on the diversity of consumption on spotify,” in _Proceedings of The Web Conference 2020_ , ser. WWW ’20. New York, NY, USA: Association for Computing Machinery, 2020, p. 2155–2165. [Online]. Available: https: //doi.org/10.1145/3366423.3380281 

- [15] C. Hosey, L. Vujovi´c, B. St. Thomas, J. GarciaGathright, and J. Thom, _Just Give Me What I Want: How People Use and Evaluate Music Search_ . New York, NY, USA: Association for Computing Machinery, 2019, p. 1–12. [Online]. Available: https://doi.org/10.1145/3290605.3300529 

- [16] N. Karakayali, B. Kostem, and I. Galip, “Recommendation systems as technologies of the self: Algorithmic control and the formation of music taste,” _Theory, Culture & Society_ , vol. 35, no. 2, pp. 3–24, 2018. 

- [17] M. D. Ekstrand, M. Tian, I. M. Azpiazu, J. D. Ekstrand, O. Anuyah, D. McNeill, and M. S. Pera, “All the cool kids, how do they fit in?: Popularity and demographic biases in recommender evaluation and effectiveness,” in _Proceedings of the 1st Conference on Fairness, Accountability and Transparency_ , ser. Proceedings of Machine Learning Research, S. A. Friedler and C. Wilson, Eds., vol. 81. New York, NY, USA: PMLR, 23–24 Feb 2018, pp. 172–186. [Online]. Available: http://proceedings.mlr.press/v81/ekstrand18b.html 

- [18] Y. Jin, N. Tintarev, and K. Verbert, “Effects of individual traits on diversity-aware music recommender user interfaces,” in _Proceedings of the 26th Conference on User Modeling, Adaptation and Personalization_ , ser. UMAP ’18. New York, NY, USA: Association for Computing Machinery, 2018, p. 291–299. [Online]. Available: https://doi.org/10.1145/3209219.3209225 

- [19] M. Pichl and E. Zangerle, “User models for multicontext-aware music recommendation,” _Multimedia Tools and Applications_ , pp. 1–23, 10 2020. 

- [20] G. Aridor, D. Goncalves, and S. Sikdar, “Deconstructing the filter bubble: User decision-making and 

648 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

recommender systems,” in _Fourteenth ACM Conference on Recommender Systems_ , ser. RecSys ’20. New York, NY, USA: Association for Computing Machinery, 2020, p. 82–91. [Online]. Available: https://doi.org/10.1145/3383313.3412246 

- [21] A. B. Melchiorre and M. Schedl, “Personality correlates of music audio preferences for modelling music listeners,” in _Proceedings of the 28th ACM Conference on User Modeling, Adaptation and Personalization_ , ser. UMAP ’20. New York, NY, USA: Association for Computing Machinery, 2020, p. 313–317. [Online]. Available: https://doi.org/10.1145/ 3340631.3394874 

- [22] H. Datta, G. Knox, and B. J. Bronnenberg, “Changing their tune: How consumers’ adoption of online streaming affects music consumption and discovery,” _Marketing Science_ , vol. 37, no. 1, pp. 5–21, 2018. 

- [23] R. I. Rushan, “The way you listen to music: effect of swiping direction and album arts on adoption of music streaming application,” _Behaviour & Information Technology_ , pp. 1–22, 2020. 

- [24] P. Herrera, Z. Resa, and M. Sordo, “Rocking around the clock eight days a week: an exploration of temporal patterns of music listening,” in _1st Workshop On Music Recommendation And Discovery (WOMRAD), ACM RecSys, 2010, Barcelona, Spain_ , Barcelona, 26/09/2010 2010. [Online]. Available: files/publications/womrad2010_submission_16.pdf 

- [25] L. Baltrunas and X. Amatriain, “Towards timedependant recommendation based on implicit feedback,” in _In Workshop on context-aware recommender systems (CARSâ A_<sup>_˘_</sup> _´ Z09_ , 2009. 

- [26] S. Volokhin and E. Agichtein, “Understanding music listening intents during daily activities with implications for contextual music recommendation,” in _Proceedings of the 2018 Conference on Human Information Interaction Retrieval_ , ser. CHIIR ’18. New York, NY, USA: Association for Computing Machinery, 2018, p. 313–316. [Online]. Available: https://doi.org/10.1145/3176349.3176885 

- [27] D. Sánchez-Moreno, Y. Zheng, and M. N. MorenoGarcía, “Incorporating time dynamics and implicit feedback into music recommender systems,” in _2018 IEEE/WIC/ACM International Conference on Web Intelligence (WI)_ , 2018, pp. 580–585. 

- [28] A. Krause, A. North, and L. Hewitt, “The role of location in everyday experiences of music.” _Psychology of Popular Media Culture_ , vol. 5, pp. 232–257, 07 2016. 

   - [30] J. Royo-Letelier, R. Hennequin, V. Tran, and M. Moussallam, “Disambiguating music artists at scale with audio metric learning,” in _Proceedings of the 19th International Society for Music Information Retrieval Conference, ISMIR 2018, Paris, France, September 23-27, 2018_ , E. Gómez, X. Hu, E. Humphrey, and E. Benetos, Eds., 2018, pp. 622–629. 

   - [31] Q. Villermet, J. Poiroux, M. Moussallam, T. Louail, and C. Roth, “Follow the guides: disentangling human and algorithmic curation in online music consumption,” in _Fithteenth ACM Conference on Recommender Systems_ , ser. RecSys ’21. New York, NY, USA: Association for Computing Machinery, 2021. 

   - [32] J. L. Toole, M. Ulm, M. C. González, and D. Bauer, “Inferring land use from mobile phone activity,” in _Proceedings of the ACM SIGKDD International Workshop on Urban Computing_ , ser. UrbComp ’12. New York, NY, USA: Association for Computing Machinery, 2012, p. 1–8. [Online]. Available: https://doi.org/10.1145/2346496.2346498 

   - [33] R. Mehrotra, C. Shah, and B. Carterette, “Investigating listeners’ responses to divergent recommendations,” in _Fourteenth ACM Conference on Recommender Systems_ , ser. RecSys ’20. New York, NY, USA: Association for Computing Machinery, 2020, p. 692–696. [Online]. Available: https://doi.org/10.1145/ 3383313.3418482 

   - [34] S. Dean, S. Rich, and B. Recht, “Recommendations and user agency,” _Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency_ , Jan 2020. [Online]. Available: http://dx.doi.org/10.1145/ 3351095.3372866 

   - [35] G. Jawaheer, M. Szomszor, and P. Kostkova, “Comparison of implicit and explicit feedback from an online music recommendation service,” in _Proceedings of the 1st International Workshop on Information Heterogeneity and Fusion in Recommender Systems_ , ser. HetRec ’10. New York, NY, USA: Association for Computing Machinery, 2010, p. 47–51. [Online]. Available: https://doi.org/10.1145/1869446.1869453 

   - [36] G. Ruxton, “The unequal variance t-test is an underused alternative to student’s t-test and the mannwhitney u test,” _Behavioral Ecology_ , vol. 17, 04 2006. 

   - [37] C. Bonferroni, _Teoria statistica delle classi e calcolo delle probabilità_ , ser. Pubblicazioni del R. Istituto superiore di scienze economiche e commerciali di Firenze. Libreria internazionale Seeber, 1936. [Online]. Available: https://books.google.de/books? id=3CY-HQAACAAJ 

- [29] T. Louail and M. Barthelemy, “Headphones on the wire,” _ArXiv_ , vol. abs/1704.05815, 2017. 

649 

