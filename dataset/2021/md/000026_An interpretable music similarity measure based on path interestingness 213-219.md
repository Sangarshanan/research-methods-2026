---
paper_id: "000026"
year: 2021
title: "An interpretable music similarity measure based on path interestingness 213-219"
source_url: "https://archives.ismir.net/ismir2021/paper/000026.pdf"
---

# **AN INTERPRETABLE MUSIC SIMILARITY MEASURE BASED ON PATH INTERESTINGNESS** 

## **Giovanni Gabbolini** 

Insight Centre for Data Analytics School of Computer Science & IT University College Cork, Ireland 

giovanni.gabbolini@insight-centre.org 

## **Derek Bridge** 

Insight Centre for Data Analytics School of Computer Science & IT University College Cork, Ireland d.bridge@cs.ucc.ie 

### **ABSTRACT** 

We introduce a novel and interpretable path-based music similarity measure. Our similarity measure assumes that items, such as songs and artists, and information about those items are represented in a knowledge graph. We find paths in the graph between a seed and a target item; we score those paths based on their interestingness; and we aggregate those scores to determine the similarity between the seed and the target. A distinguishing feature of our similarity measure is its interpretability. In particular, we can translate the most interesting paths into natural language, so that the causes of the similarity judgements can be readily understood by humans. We compare the accuracy of our similarity measure with other competitive path-based similarity baselines in two experimental settings and with four datasets. The results highlight the validity of our approach to music similarity, and demonstrate that path interestingness scores can be the basis of an accurate and interpretable similarity measure. 

### **1. INTRODUCTION** 

The concept of similarity is central to music information retrieval, as it underpins important applications like recommender systems and visualisation in user interfaces [1]. In recent years, there has been a surge in the use of knowledge graphs to solve various information retrieval tasks. For example, knowledge graphs have been applied to recommender systems [2] and question answering [3]. In this work, we use knowledge graphs to gauge music similarity. We introduce a novel path-based similarity measure. We represent items, such as songs and their artists, and information about those items in a knowledge graph; we find paths in the graph between a seed and a target item; we score those paths; and we aggregate the scores to determine the similarity between the seed and the target. 

We propose to score paths based on interestingness. Interestingness is introduced in [4] as a way of distinguishing 

> © G. Gabbolini and D. Bridge. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). **Attribution:** G. Gabbolini and D. Bridge, “An interpretable music similarity measure based on path interestingness”, in _Proc. of the 22nd Int. Society for Music Information Retrieval Conf.,_ Online, 2021. 

|Path(in natural language)|Int.|
|---|---|
|George Jones was married to TammyWynette.|0.60|
|Tammy Wynette was the parent of the<br>artist Georgette Jones and George Jones<br>was also theparent of the same artist.|0.56|
|Tammy Wynette wrote “Our Private Life”<br>and George Jones also wrote the same song.|0.45|
|Tammy Wynette has made country music,<br>and so did George Jones.|0.34|
|Tammy Wynette was based in United States and<br>George Jones was based in the same country.|0.31|
|Tammy Wynette was a solo artist,<br>and George Jones was a solo artist.|0.29|



**Table 1** . An example of the working of our proposed similarity measure. In this example, it is given the artists Tammy Wynette and George Jones as seed and target items. 

more interesting from less interesting paths in a knowledge graph. In [4], the authors use what they call _segues_ to connect a song to the next song, e.g. in a playlist. Segues are translations into natural language of interesting paths in a knowledge graph. We also employ the path-to-text module from [4], useful to translate paths to natural language. In this paper, we are extending [4] by showing that these paths and their interestingness scores can be the basis of an accurate and interpretable similarity measure. 

For example, given the artists Tammy Wynette and George Jones as seed and target, our algorithm finds six paths between the two items, then it assigns an interestingness score to the paths, and it aggregates the scores to determine the similarity. It can convert the paths to natural language for display to a user. We report in Table 1 its natural language translations of the paths (Path column) and the interestingness scores (Int. column). 

A distinguishing feature of our similarity measure is its interpretability. Miller defines interpretability as the degree to which a human can understand the cause of a decision [5]. According to this definition, our similarity measure is interpretable. Users can understand the causes of a similarity score by looking at natural language translations of the paths used to compute it, ranked by their interestingness. For example, a user can understand why our al- 

213 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

gorithm thinks that Tammy Wynette and George Jones are similar, when presented with the ranked list of explanations in Table 1. Notice how the interestingness score intuitively reflects the interestingness of the paths. For example, two artists being married has higher score than two artists both being solo singers. 

Music similarity measures are usually not interpretable, e.g. see [6]. This may be related to a system-centric research protocol, which is common in the field, and consists of laboratory experiments conducted without end-user involvement, e.g. the evaluation of algorithms on digital databases [7]. This protocol is pragmatic but it may have contributed to widening the “semantic gap” in music similarity measures, which sets a bound on user satisfaction [1]. The term “semantic gap” refers to the discrepancy between high-level perception of similarity by humans and the lowlevel numerical data used by algorithms [8]. For example, a user might perceive two songs as similar because of their lyrics, while an algorithm might be limited to using abstract statistical descriptors operating on the audio signals. One way of alleviating the semantic gap is the introduction of mid-level features. Mid-level features either combine low-level features or extend them to ones that incorporate additional, higher-level knowledge [1]. Another way of reducing the gap is the adoption of interpretable similarity measures. An interpretable similarity measure can narrow the gap between the low perceptual level of an algorithm, which makes a decision about similarity, and the high perceptual level of a human, by providing an explanation for the human to understand the decision. 

The remainder of the paper is organised as follows: in Section 2, we frame our similarity measure in the literature of the subject; in Section 3, we formalise our similarity measure; and, in Section 4, we validate our similarity measure in four experimental conditions. The source code supporting this study is freely available.<sup>1</sup> 

### **2. RELATED WORK** 

The concept of similarity is central to Music Information Retrieval. Over the years, researchers have proposed many ways of measuring music similarity, which can be categorised based on the data they use. We might, for example, categorise them into two: content-based approaches that use the audio signal; and context-based approaches that use information about artists and the pieces of music themselves, e.g. their lyrics, listening logs, and so on [9]. We refer the reader to the book by Knees & Schedl [6] for an extensive review of content-based and context-based approaches. The similarity measure that we propose in this paper is context-based. 

Some of the context-based approaches make use of knowledge graphs. These approaches represent entities from the music domain and information about those entities as nodes in a graph, and they use graph structure to gauge similarity. (We define knowledge graphs more formally in Section 3.1.) 

Many knowledge graph-based approaches to the measurement of similarity are path-based. They use the existence of paths between the seed and the target entities to determine similarity. Path-based algorithms usually score paths based on some criteria, and then aggregate path scores to determine similarity. For example, in [10] Leal et al. describe Shakti. Shakti scores each path by summing hand-crafted node weights and edge weights, and then dividing by the cube of the path length. Shakti only considers paths whose length falls below a fixed threshold. In [11], Strobin & Niewiadomski extend Shakti by setting node and edge weights using a genetic algorithm. This extension evolves different sets of weights indexed by path length, and considers paths of any length. They adjust node weights by considering centrality, i.e. the number of in-going and out-going edges of a node. 

Passant proposes another path-based algorithm, called LDSD [12]. LDSD considers only paths of length up to two. It assigns low scores to paths whose type is common in the context of the seed and target entities. Piao & Breslin extend LDSD in [13]. They propose four variants of LDSD, which correct the path scoring mechanism with global information, such as the frequency of path types in the whole knowledge graph. In a comparative study, Piao et al. show that LDSD largely outperforms Shakti in accuracy [14]. 

The similarity measure that we propose in this paper is also path-based. It is different from the works in the literature as we employ a novel scoring mechanism for paths, based on their interestingness. 

As well as path-based approaches to the measurement of similarity, there are also embedding-based approaches. These work by representing the knowledge graph in a dense, low-dimensional feature space, which tries to preserve as much of the graph’s structural information as possible. There are several ways to learn knowledge-graph embeddings. We refer the reader to [15] for a survey. Once the embeddings are learned, the similarity between entities can be computed on their vector representations using, for example, cosine similarity. 

Path-based and embedding-based approaches to the measurement of similarity differ in their interpretability. In [16], Du et al. provide a characterization of approaches based on their potential for interpretability. They introduce the concept of _intrinsic interpretability_ , which is achieved by constructing self-explanatory models. Pathbased approaches typically exhibit intrinsic interpretability, since the paths used to gauge similarity can be considered to be self-explanatory. Embedding-based approaches do not exhibit intrinsic interpretability, since the embeddings used to gauge similarity cannot be considered to be self-explanatory. As a consequence, path-based approaches are interpretable after the translation of the paths to natural language, while embedding-based approaches can become interpretable only after the introduction of a post-hoc model, built to generate explanations [16]. 

Path-based approaches are not the only category of similarity measures to feature intrinsic intepretability. For ex- 

1 https://github.com/GiovanniGabbolini/ipsim 

214 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 



<!-- Start of picture text -->
r 1<br>e 1 e 2 r 3 e 3<br>r 2<br><!-- End of picture text -->

**Figure 1** . A simple knowledge graph. 

ample, if items are described by sets of tags, then Jaccard similarity over tags also exhibits intrinsic intepretability. The similarity can be explained by showing the tags shared between the seed and the target. Even so, we find a scarcity of interpretable similarity measures in the literature; the book [6] contains very few, for example. 

We mention that Passant’s LDSD is also interpretable, since Passant implements a mechanism to translate paths to natural language [12] . 

### **3. METHOD** 

As we have already indicated, our approach to the measurement of similarity of entities in knowledge graphs is path-based. It builds on work described in [4], where the authors introduce interestingness as a way of distinguishing more interesting from less interesting paths in a knowledge graph. 

In the following, we first introduce some preliminary concepts, then we review [4]’s definition of interestingness, and finally we introduce our similarity measure. 

### **3.1 Preliminaries** 

Both our work and [4] make use of a knowledge graph _G_ as an abstract representation for items and information about those items. In the experiments that we report later in this paper, items are artists; in [4], items are songs. But the approach is domain-independent: items can be any entities of interest. 

The function _paths_ ( _i1 , i2_ ) finds the paths in _G_ from the item _i_ 1 _∈ I_ to the item _i_ 2 _∈ I_ , without visiting any other item in _I_ and without cycles. In other words, if items are songs, for example, then the function finds paths between pairs of songs, where the paths are not allowed to contain any intermediate songs. 

### **3.2 Interestingness** 

In [4], the interestingness of a path in a knowledge graph is defined as a weighted combination of three heuristics: 

- **Rarity** Let _T_ be the set of all path types in _G_ ; and let _f_ ( _t_ ) be the number of paths in _G_ that are of type _t_ . The _rarity_ of a path _p_ is defined as: 



<!-- Start of picture text -->
rarity ( p ) = 1  − f ( type ( p ))<br>max t∈T f ( t )<br><!-- End of picture text -->

- **Unpopularity** Let _edgeset_ ( _e_ ) be the set of in-going and out-going edges to and from an entity _e ∈ E_ in _G_ . The centrality of an entity _e_ is: 



<!-- Start of picture text -->
 |edgeset ( e ) | <br>centrality ( e ) = min<br>1 , mediane ′ ∈E |edgeset ( e′ ) |  ,<br>given type ( e ′ ) =  type ( e )<br><!-- End of picture text -->

The _unpopularity_ of a path _p_ is defined as: 



<!-- Start of picture text -->
unpopularity ( p ) = 1  − e∈ min p∩E ( centrality ( e ))<br><!-- End of picture text -->

- **Shortness** If we define _length_ ( _p_ ) as the number of edges in path _p_ , then the _shortness_ of a path is given by: 



<!-- Start of picture text -->
1<br>shortness ( p ) =<br>length ( p )<br><!-- End of picture text -->

The _interestingness_ of a path _p_ in _G_ is given by: 

- A **knowledge graph** is a set of triples _G_ = _{_ ( _e, r, e_<sup>_′_</sup> ) _| e, e_<sup>_′_</sup> _∈ E, r ∈ R}_ , where _E_ and _R_ denote, respectively, the sets of entities (nodes) and relationships (edges). For example, the knowledge graph of Figure 1 contains three triples, _{_ ( _e_ 1 _, r_ 1 _, e_ 2) _,_ ( _e_ 1 _, r_ 2 _, e_ 2) _,_ ( _e_ 2 _, r_ 3 _, e_ 3) _}_ . A special subset of entities _I ⊆ E_ , are the items. Every entity has a _type_ and a _value_ . For example, if an entity represents an artist, then its type is “artist” and its value is the URI of that artist. Every edge (relationship) has a _type_ also. For example, an edge that connects two artists who have collaborated will have “collaborated with” as its type. 

- A **path** _p_ in _G_ is an ordered list of entities and edges in _G_ , _p_ = [ _e_ 1 _, r_ 1 _, ..., rn−_ 1 _, en_ ] where each triple in _p_ must be in _G_ . For example, with reference to the knowledge graph of Figure 1: [ _e_ 1 _, r_ 1 _, e_ 2 _, r_ 3 _, e_ 3] is a path; [ _e_ 1 _, r_ 1 _, e_ 2 _, r_ 1 _, e_ 3] is not a path, as the triple ( _e_ 2 _, r_ 1 _, e_ 3) is not in the knowledge graph. The _type_ of _p_ is the ordered concatenation of the entity and edge types in _p_ . 



<!-- Start of picture text -->
interestingness ( p ) =  w 1 rarity ( p )+<br><!-- End of picture text -->



<!-- Start of picture text -->
w 2 unpopularity ( p )+<br>w 3 shortness ( p )<br><!-- End of picture text -->

Its values range from zero to one. _w_ 1 _, w_ 2 _, w_ 3 are parameters to be tuned, subject to _w_ 1 + _w_ 2 + _w_ 3 = 1 _._ 

In [4], the authors run a user trial where participants are asked to evaluate segues. They find that _interestingness_ positively correlates with human perceptions of quality: _interestingness_ is high for segues perceived as highquality, and vice versa. This lends credence to the idea of using their definition of interestingness in the similarity measure that we are proposing in this paper. 

### **3.3 Similarity** 

We define the similarity between two items _i_ 1 _∈ I_ and _i_ 2 _∈ I_ as an aggregate of the interestingness of the paths between them: 



<!-- Start of picture text -->
sim ( i 1 , i 2) = � interestingness ( p )  I ( p, n )<br>p∈paths ( i 1 ,i 2)<br><!-- End of picture text -->

215 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

where _I_ is an indicator function: _I_ ( _p, n_ ) = 1 if _length_ ( _p_ ) _≤ n_ , and 0 otherwise. _n_ is a parameter whose value determines whether the aggregation restricts attention to shorter paths or whether it considers all paths ( _n_ = _∞_ ). It is not clear _a priori_ whether it is beneficial to put a limit on path length and, if so, what limit to use. For example, [12] use only paths of length up to three, while [11] uses all paths. In our case, we leave the choice open by introducing the parameter _n_ to be tuned. The interestingness weights _w_ 1, _w_ 2, _w_ 3 are also parameters to be tuned. 

In the following, we refer to our similarity measure as IPSIM ( **I** nteresting **P** ath **Sim** ilarity). IPSIM is domainindependent. In the rest of this paper, we focus on the music domain, and in particular the case where items are music artists. The reason we focus on artist similarity is that it is a common choice in the literature and there is an amount of data to use in offline experiments. 

sures of music similarity. Every method has its own advantages and disadvantages. In this paper, we assess music similarity measures using two common experimental settings. The first uses a similar-artists ground-truth, and the second uses user-artist interaction histories. 

### _4.2.1 Using a ground-truth_ 

This evaluation procedure replicates the one in [17]. The procedure uses datasets that are composed of tuples of the form _(seed artist, similar-artists ground-truth)_ . In other words, for each seed artist, it gives a list of artists that have been independently judged to be similar to the seed, these artists being regarded as the ground-truth. We employ two datasets: 

- **_MIREX_ :** This dataset comprises 188 seed artists. The ground truth is based on similarity judgements expressed by experts during the MIREX Audio Music Similarity and Retrieval Task. 

### **4. EXPERIMENTS** 

We provide an evaluation for IPSIM in the case of music artists. In this evaluation, we are particularly interested in evaluating the accuracy that IPSIM is able to achieve. 

### **4.1 Knowledge graph** 

We represent an artist with their MusicBrainz URI.<sup>2</sup> This representation can be easily changed with only minor modifications to the rest of our implementation, e.g. if artists were instead represented by their Spotify URIs. 

Our implementation uses a knowledge graph with 30 distinct node types and 205 distinct edge types. It is built with data that we harvest from two resources: 

- **MusicBrainz** We use MusicBrainz as the main source of factual data. We exploit the MusicBrainz APIs.<sup>3</sup> They allow us to navigate the MusicBrainz database, and offer entity-linking functionalities. We mine different sorts of factual data, ranging from the birth places of the artists to the genres that they play. 

- **Wikidata** We use Wikidata as an additional source of factual data.<sup>4</sup> There exists a mapping from MusicBrainz URIs to Wikidata URIs, making it easy to use both resources. From Wikidata, we mine biographical data about artists that is not available in MusicBrainz, e.g. the awards that an artist has won. 

We provide a complete description of entities and relationships that build up the knowledge graph that we use in this paper in the additional materials.<sup>5</sup> 

### **4.2 Experiment design** 

As highlighted by Knees & Schedl [1], there is no agreement upon the best method to evaluate the quality of mea- 

> 2 https://musicbrainz.org/ 

> 3 https://python-musicbrainzngs.readthedocs.io/ en/v0.7.1/ 

> 4 https://wikidata.org/ 

> 5 https://doi.org/10.5281/zenodo.5121460 

- **_LastFM-g_ :** This dataset comprises 2336 seed artists. The ground truth is based on similarity judgements gathered from the Last.fm APIs.<sup>6</sup> 

See [17] for additional details on these datasets. 

To evaluate a similarity measure on a given dataset, we do the following. For every seed artist, we use the similarity measure to score the other artists and then to rank them by decreasing similarity with the seed. Then, we compare this ranking _@N_ with the ground-truth from the dataset, according to the standard accuracy metrics _nDCG_ and _Precision_ , or _Pr_ for short. 

### _4.2.2 Using interaction histories_ 

This protocol uses a dataset that records how users have interacted with artists. We denote with _U_ , _I_ the sets of users and artists resp. and with _|U |_ , _|I|_ their cardinalities. Lower case letters _u_ , _i_ refer to _u ∈ U_ , _i ∈ I_ . In this case, the dataset is organised as a matrix _R ∈_ R<sup>_|U|×|I|_</sup> . Each cell _rui >_ 0 of _R_ accounts for a user-artist interaction. If a user _u_ is not known to have interacted with an artist _i_ , then _rui_ is zero. 

We employ two datasets of this kind: 

- **_LastFM-h_ :** In this Last.fm dataset (which is different from the one described earlier), _rui_ is the listening count by user _u_ of artist _i_ [18].<sup>7</sup> We filter out users who have listened to fewer than five artists, and artists listened to by fewer than five users. We end up with 1877 users and 2828 artists. We convert listening counts to ratings on a 1–5 scale following the procedure given in [19]. For every user, we hold-out at random 40% of her interactions, and we keep the other interactions as training data. We further split the held-out interactions into two equal-sized parts, to form validation and test data. Finally, we remove the interactions where _rui <_ 4 from the validation and test data so that they only contain artists that the users like. 

> 6 last.fm 

- 7 https://grouplens.org/datasets/hetrec-2011/ 

216 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

- **_Facebook_ :** This dataset, from the Second Linked Open Data-enabled Recommender Systems Challenge, contains items liked by users in three domains: movies, books and music.<sup>8</sup> We focus on music artists, by keeping only items of types: _music_artist_ and _music_band_ . We filter out artists liked by fewer than five users, and those whose MusicBrainz URI cannot be resolved. We end up with 52069 users and 4435 artists. In this case, _rui_ = 1 if the user _u_ likes the artist _i_ . For every user, we hold-out 40% of her interactions at random, and we keep the others as training data. We further split the held-out interactions into two equal-sized parts, to form validation and test data. 

For these two datasets, the evaluation procedure uses the similarity measure as a core component within a recommender system. The design of the recommender system is inspired by [13], chosen because of its heavy reliance on similarity, which is what we are trying to evaluate. We define the user profile of a user _u_ as the artists she has rated (in the training set): 



<!-- Start of picture text -->
P ( u ) =  {j|ruj̸ = 0 }.<br><!-- End of picture text -->

Let _NN_ ( _k, i, P_ ( _u_ )) be the set of _k_ most similar items in _P_ ( _u_ ) to an artist _i_ . The predicted relevance score for a user _u_ and an artist _i_ , indicated as _<u>rui</u>_ <u>, is computed as:</u> 



<!-- Start of picture text -->
0 if  i ∈ P ( u )<br>rui =<br>�� j∈NN ( k,i,P  ( u )) ruj sim ( i, j ) if  i̸ ∈ P ( u )<br><!-- End of picture text -->

For every user, we compute the relevance score _<u>rui</u>_ for every artist _i ∈ I_ , and rank the artists by decreasing score. Then, we compare this ranking _@N_ and the held-out test data (or validation data, as appropriate), according to the standard accuracy metrics _nDCG_ and _Precision_ , or _Pr_ for short. We take higher recommendation accuracy to be an indication of a higher quality similarity measure. 

### **4.3 Baseline similarity measures** 

We include in our experiments three baselines. The first is a random algorithm (RND), useful to set a lower bound on the performance. It rates the similarity between two items to be a random number between zero and one. The other two (COUNT and LDSD) are path-based algorithms. By comparing our path-based approach to other path-based similarities, we reduce the number of confounders, so we can investigate whether our idea of using interestingness as a scoring mechanism for paths is a good one. In fact, the path-based similarity measures that we use in this experiment all use the same knowledge graph and the same paths, and differ only in the way the paths are scored and how the scores are aggregated. COUNT is a simple path-based algorithm that works by counting the number of paths between items. It is equivalent to substituting 1 for the argument to the sum in the definition of _sim_ given earlier. LDSD is an accurate path-based algorithm that proposes a carefullydesigned weighting heuristic for paths [12]. 

> 8 https://lists.w3.org/Archives/Public/ public-vocabs/2015Feb/0046.html 

||_w_1|_w_2|_w_3|_n_|_k_|
|---|---|---|---|---|---|
|_MIREX_|0.3|0.1|0.6|2|NA|
|_LastFM-g_|0.0|0.1|0.9|2|NA|
|_LastFM-h_|0.0|0.0|1.0|2|40|
|_Facebook_|0.9|0.0|0.1|_∞_|_∞_|



**Table 2** . Optimal parameters found for IPSIM. 

### **4.4 Parameter tuning** 

IPSIM has some parameters, as indicated in Section 3.3. Additionally, the experiment using listening histories introduces another parameter, i.e. the number of neighbours _k_ used by the recommender system, as described in Section 4.2.2. We set the parameters with a grid-search, optimizing _nDCG@10_ on the validation data. For the experiment using a ground-truth, we tune the parameters of IPSIM. For the experiment using listening histories, we tune the parameters of IPSIM and we tune _k_ for each of RND, COUNT, LDSD and IPSIM. We report the optimal parameters found for IPSIM in Table 2. The optimal values of the parameter _k_ for RND, COUNT and LDSD are, respectively, 5, 10 & 40 in _LastFM-h_ and 1, 1 & 7 in _Facebook_ . 

The optimal parameter configurations change from dataset to dataset. This might be due to the different nature of the datasets. _MIREX_ features human judgements of artist similarity; the algorithmic judgments to be found in _LastFM-g_ might not completely agree with these. Schedl et al. [7] suggest that human perception of similarity is influenced by user factors, such as user context (e.g. mood) and user properties (e.g. musical training). User factors might have directly influenced the people who annotated _MIREX_ , but not the algorithm used to construct _LastFMg_ . The remaining two datasets, _LastFM-h_ and _Facebook_ , gather another kind of data, i.e. interaction histories, but they are gathered in different ways. In _LastFM-h_ , unless the user intervenes, the next recommended song is played automatically, whereas, in _Facebook_ , users are interacting with artist fan pages in what is usually a more deliberate, conscious and considered way. 

In three of the four datasets, at least one of the three interestingness heuristics of IPSIM receives a weight of zero. We may find an explanation for this in the median number of paths between artists: 19 in _MIREX_ , 13 in _LastFM-g_ , and seven in both _LastFM-h_ and _Facebook_ . _MIREX_ is the only dataset where all three weights are non-zero, and is also the dataset with the highest median number of paths between artists. In general, the use of a more complex model (with non-zero weights for each component) might be beneficial only when the dataset refers to artists in the knowledge graphs for whom there exists a rich variety of paths, e.g. when considering popular artists. 

### **4.5 Results** 

We conduct the experiments described in Section 4.2. We compare IPSIM against the baselines described in Section 4.3 (RND, COUNT, LDSD). We set the parameters of the similarity measures and the recommender as described in 

217 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 



<!-- Start of picture text -->
(a) MIREX (b) LastFM-g (c) LastFM-h (d) Facebook<br>0.150 IPSIM<br>0.125 0.025 LDSD<br>0.125 0.030 COUNT<br>0.100 0.020 RND<br>0.100<br>Pr@N0.075 0.075 0.020 0.015<br>0.050 0.010<br>0.050 0.010<br>0.025 0.005<br>0.025<br>0.000 0.000 0.000<br>0 20 40 60 80 100 0 20 40 60 80 100 20 40 60 80 100 20 40 60 80 100<br>N N N N<br><!-- End of picture text -->

**Figure 2** . Accuracy of similarity measures on the _MIREX_ , _LastFM-g_ , _LastFM-h_ and _Facebook_ datasets, as measured by _Precision_ at cutoffs from one to 100. 

||_nDCG@5_|_nDCG@10_|_Pr@5_|_Pr@10_|
|---|---|---|---|---|
|RND|0.023|0.022|0.026|0.023|
|COUNT|0.065|0.057|0.062|0.052|
|LDSD|0.102|0.094|0.096|0.088|
|IPSIM|**0.136**<sup>_∗∗∗_</sup>|**0.114**<sup>_∗_</sup>|**0.130**<sup>_∗∗∗_</sup>|**0.101**<sup>_∗_</sup>|



**Table 3** . Accuracy of similarity measures on the _MIREX_ dataset, as measured by _nDCG_ and _Precision_ at cutoffs five and ten.<sup>_∗_</sup> : _p_ <0.05;<sup>_∗∗_</sup> : _p_ <0.01;<sup>_∗∗∗_</sup> : _p_ <0.001. 

||_nDCG@5_|_nDCG@10_|_Pr@5_|_Pr@10_|
|---|---|---|---|---|
|RND|0.002|0.002|0.002|0.002|
|COUNT|0.037|0.030|0.033|0.025|
|LDSD|0.103|0.086|0.095|0.075|
|IPSIM|**0.111**<sup>_∗∗_</sup>|**0.094**<sup>_∗∗∗_</sup>|**0.103**<sup>_∗∗_</sup>|**0.083**<sup>_∗∗∗_</sup>|



**Table 4** . Accuracy of similarity measures on the _LastFMg_ dataset, as measured by _nDCG_ and _Precision_ at cutoffs five and ten.<sup>_∗_</sup> : _p_ <0.05;<sup>_∗∗_</sup> : _p_ <0.01;<sup>_∗∗∗_</sup> : _p_ <0.001. 

||_nDCG@5_|_nDCG@10_|_Pr@5_|_Pr@10_|
|---|---|---|---|---|
|RND|0.001|0.000|0.001|0.000|
|COUNT|0.015|0.012|0.014|0.010|
|LDSD|**0.025**<sup>_∗∗∗_</sup>|**0.020**<sup>_∗∗_</sup>|**0.022**<sup>_∗∗∗_</sup>|0.016|
|IPSIM|0.016|0.017|0.017|**0.017**|



**Table 5** . Accuracy of similarity measures on the _LastFMh_ dataset, as measured by _nDCG_ and _Precision_ at cutoffs five and ten.<sup>_∗_</sup> : _p_ <0.05;<sup>_∗∗_</sup> : _p_ <0.01;<sup>_∗∗∗_</sup> : _p_ <0.001. 

||_nDCG@5_|_nDCG@10_|_Pr@5_|_Pr@10_|
|---|---|---|---|---|
|RND|0.001|0.001|0.001|0.001|
|COUNT|0.017|0.014|0.016|0.012|
|LDSD|0.021|0.018|0.019|0.017|
|IPSIM|**0.024**<sup>_∗∗∗_</sup>|**0.021**<sup>_∗∗∗_</sup>|**0.023**<sup>_∗∗∗_</sup>|**0.020**<sup>_∗∗∗_</sup>|



**Table 6** . Accuracy of similarity measures on the _Facebook_ dataset, as measured by _nDCG_ and _Precision_ at cutoffs five and ten.<sup>_∗_</sup> : _p_ <0.05;<sup>_∗∗_</sup> : _p_ <0.01;<sup>_∗∗∗_</sup> : _p_ <0.001. 

Section 4.4 using the validation data. We report the results on the test data. We verify the significance of differences between IPSIM and LDSD with Wilcoxon signedrank test. 

Tables 3 & 4 report on the experiment that uses a ground-truth. IPSIM outperforms all the baselines in both the _MIREX_ and _LastFM-g_ datasets. We notice that IPSIM scores accuracy at least double that of COUNT in both datasets. The increase in performance with respect to LDSD is statistically significant in both datasets. 

Tables 5 & 6 report on the experiment that uses listening histories. IPSIM is always more accurate than COUNT. IPSIM always outperforms LDSD in _Facebook_ but outperforms LDSD in only one case in _LastFM-g_ , and the difference in this case is not statistically significant. 

We investigate more deeply how accuracy varies with the cutoff in Figure 2. For the four datasets, the figure shows the _Precision_ of the similarity measures as a function of the cutoff. The figure confirms that IPSIM has higher precision than LDSD on _LastFM-h_ for cutoffs greater than ten, but the precision of IPSIM drops for cutoffs _<_ 10. We also notice that, on _MIREX_ , _LastFM-g_ and _Facebook_ , IPSIM outperforms LDSD for every cutoff ranging from one to 100. 

The results provide evidence that interestingness can be the basis of an accurate similarity measure. 

### **5. CONCLUSIONS AND FUTURE WORK** 

The results of the experiments highlight the validity of our approach to music similarity (at least in the case of music artists), and demonstrate that the interestingness scores of [4] can be the basis of an accurate and interpretable similarity measure. Future work might include a comparison of the performance of our similarity measure against an even wider range of music similarity measures. We are also interested in using the proposed similarity measure in a related-item recommender system, that can meaningfully guide users in their exploration of the items by means of the interpretability of the similarity measure. 

218 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

### **6. ACKNOWLEDGMENTS** 

This publication has emanated from research conducted with the financial support of Science Foundation Ireland under Grant number 12/RC/2289-P2 which is co-funded under the European Regional Development Fund. For the purpose of Open Access, the authors have applied a CC BY public copyright licence to any Author Accepted Manuscript version arising from this submission. 

### **7. REFERENCES** 

- [1] P. Knees and M. Schedl, “Introduction to music similarity and retrieval,” in _Music Similarity and Retrieval: An Introduction to Audio- and Web-based Strategies_ . Berlin, Heidelberg: Springer Berlin Heidelberg, 2016, pp. 1–30. [Online]. Available: https://doi.org/10.1007/978-3-662-49722-7_1 

- [2] Q. Guo, F. Zhuang, C. Qin, H. Zhu, X. Xie, H. Xiong, and Q. He, “A survey on knowledge graph-based recommender systems,” _IEEE Transactions on Knowledge and Data Engineering_ , pp. 1–1, 2020. 

- [3] A. Bordes, S. Chopra, and J. Weston, “Question answering with subgraph embeddings,” in _Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP)_ . Doha, Qatar: Association for Computational Linguistics, Oct. 2014, pp. 615–620. [Online]. Available: https: //www.aclweb.org/anthology/D14-1067 

- [4] G. Gabbolini and D. Bridge, “Generating interesting song-to-song segues with dave,” in _Proceedings of the 29th ACM Conference on User Modeling, Adaptation and Personalization_ , ser. UMAP ’21. New York, NY, USA: Association for Computing Machinery, 2021, p. 98–107. [Online]. Available: https://doi.org/10.1145/3450613.3456819 

- [5] T. Miller, “Explanation in artificial intelligence: Insights from the social sciences,” _Artificial Intelligence_ , vol. 267, pp. 1–38, 2019. [Online]. Available: https://www.sciencedirect.com/science/article/ pii/S0004370218305988 

- [6] P. Knees and M. Schedl, in _Music Similarity and Retrieval: An Introduction to Audio- and Webbased Strategies_ . Berlin, Heidelberg: Springer Berlin Heidelberg, 2016. [Online]. Available: https: //doi.org/10.1007/978-3-662-49722-7 

- [7] M. Schedl, A. Flexer, and J. Urbano, “The neglected user in music information retrieval research,” _Journal of Intelligent Information Systems_ , vol. 41, no. 3, pp. 523–539, 2013. [Online]. Available: https: //doi.org/10.1007/s10844-013-0247-6 

- [8] D. Ponceleón and M. Slaney, “Multimedia information retrieval,” in _Modern Information Retrieval: The Concepts and Technology Behind Search_ . AddisonWesley Professional, 2011, pp. 589–590. 

- [9] P. Knees and M. Schedl, “A survey of music similarity and recommendation from music context data,” _ACM Trans. Multimedia Comput. Commun. Appl._ , vol. 10, no. 1, Dec. 2013. [Online]. Available: https://doi.org/10.1145/2542205.2542206 

- [10] J. Leal, V. Rodrigues, and R. Queirós, “Computing semantic relatedness using DBPedia,” _Symposium on Languages, Applications and Technologies, 1st_ , no. January, pp. 133–147, 2012. 

- [11] Ł. Strobin and A. Niewiadomski, “Evaluating semantic similarity with a new method of path analysis in RDF using genetic algorithms,” _Journal of Applied Computer Science_ , vol. 21, no. 2, pp. 137–152, 2013. 

- [12] A. Passant, “Measuring semantic distance on linking data and using it for resources recommendations,” _AAAI Spring Symposium - Technical Report_ , vol. SS10-07, pp. 93–98, 2010. 

- [13] G. Piao and J. G. Breslin, “Measuring semantic distance for linked open data-enabled recommender systems,” in _Proceedings of the 31st Annual ACM Symposium on Applied Computing_ , ser. SAC ’16. New York, NY, USA: Association for Computing Machinery, 2016, p. 315–320. [Online]. Available: https://doi.org/10.1145/2851613.2851839 

- [14] G. Piao, S. S. Ara, and J. G. Breslin, “Computing the semantic similarity of resources in dbpedia for recommendation purposes,” _Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)_ , vol. 9544, pp. 185–200, 2016. 

- [15] Y. Dai, S. Wang, N. N. Xiong, and W. Guo, “A survey on knowledge graph embedding: Approaches, applications and benchmarks,” _Electronics_ , vol. 9, no. 5, 2020. [Online]. Available: https://www.mdpi. com/2079-9292/9/5/750 

- [16] M. Du, N. Liu, and X. Hu, “Techniques for interpretable machine learning,” _Commun. ACM_ , vol. 63, no. 1, p. 68–77, Dec. 2019. [Online]. Available: https://doi.org/10.1145/3359786 

- [17] S. Oramas, M. Sordo, L. Espinosa-Anke, and X. Serra, “A semantic-based approach for artist similarity,” in _16th International Society for Music Information Retrieval Conference_ , Málaga, Spain, 26/10/2015 2015, pp. 100–106. [Online]. Available: http://hdl.handle.net/10230/26278 

- [18] I. Cantador, P. Brusilovsky, and T. Kuflik, “2nd workshop on information heterogeneity and fusion in recommender systems (hetrec 2011),” in _Proceedings of the 5th ACM conference on Recommender systems_ , ser. RecSys 2011. New York, NY, USA: ACM, 2011. 

- [19] Ò. Celma, “Music recommendation and discovery in the long tail,” Ph.D. dissertation, Universitat Pompeu Fabra, Barcelona, 2008. 

219 

