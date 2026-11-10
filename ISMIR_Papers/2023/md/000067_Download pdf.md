---
paper_id: "000067"
year: 2023
title: "Download pdf"
source_url: "https://zenodo.org/record/10340442/files/000067.pdf"
---

# TOWARDS BUILDING A PHYLOGENY OF GREGORIAN CHANT MELODIES 

Jan Hajiˇc jr.<sup>1</sup> Gustavo A. Ballen<sup>2</sup> Klára Hedvika Mühlová<sup>3</sup> 

Hana Vlhová-Wörner<sup>1</sup> 

1 Masaryk Institute and Archive, Czech Academy of Sciences, Czechia 

2 School of Biological and Behavioural Sciences, Queen Mary University of London, UK 

3 Faculty of Arts, Masaryk University, Czechia 

```
hajic@mua.cas.cz
```

## ABSTRACT 

The historical development of medieval plainchant melodies is an intriguing musicological topic that invites computational approaches to study it at scale. Plainchant melodies can be represented as strings from a limited alphabet, hence making it technically possible to apply bioinformatic tools that are used to study the relationships of biological sequences. We show that using phylogenetic trees to study relationships of plainchant sources is not merely possible, but that it can indeed produce meaningful results. We develop a simple plainchant substitution model for Multiple Sequence Alignment, adapt a Bayesian phylogenetic tree building method, and demonstrate the promise of this approach by validating the resultant phylogenetic tree built from a set of Divine Office sources for the Christmas Vespers against musicological knowledge. 

## 1. INTRODUCTION 

Gregorian chant is the universal sacred liturgical monody of the Roman Catholic church, which exerts strong control over this musical tradition. There is an authoritative edition of chant: if singers from multiple countries and continents sing together, each from their print of liturgical books, they should encounter no conflicts in performance. However, this was not always so. During the five hundred years of notated Gregorian chant manuscript culture, between Guidonian staff notation and the introduction of the post-Tridentine printed liturgical books, rarely was a chant melody written exactly the same in two sources.<sup>1</sup> Despite its stated role as a unifying element of the Roman Catholic church, Gregorian chant was a diverse tradition. 

The diversity of Gregorian chant, both in terms of repertoire and melody, has been a staple of musicological study 

> 1 See cf. a sample of melodies of an antiphon: `https://cantusindex.org/id/004237` 

> © J. Hajiˇc jr., G. A. Ballen, K. H. Mühlová, and H. VlhováWörner. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: J. Hajiˇc jr., G. A. Ballen, K. H. Mühlová, and H. Vlhová-Wörner, “Towards Building a Phylogeny of Gregorian Chant Melodies”, in Proc. of the 24th Int. Society for Music Information Retrieval Conf., Milan, Italy, 2023. 

of plainchant [1, 2]. Already the relative importances of chronology, geography, and cursus<sup>2</sup> are, aside from select topics such as the Cistercian reform, not well understood. Recent chant scholarship thrives on the large-scale digitization effort centered around the Cantus Index network of databases [3], and there are ongoing efforts to apply digital methods to the problem of chant transmission such as the DACT project.<sup>3</sup> 

In this pilot study, we present a novel pipeline to model the relationships between chant sources using tools from bioinformatics: we adapt multiple sequence alignment and phylogenetic tree inference for chant melodies. We qualitatively evaluate the method on a dataset of sources for Christmas Eve vespers.<sup>4</sup> 

## 2. RELATED WORK 

The study of melodic dialects of chant has a long tradition, most prominently in the distinction proposed between “West Frankish” and “East Frankish” chant [4], as has the theory of chant melody in general (i.a. the centonization hypothesis [5, 6] and its criticism [7], [8, pp. 74-75]), but has not yet been performed with computational models at the scales that these enable. The fact that the diversity within chant melodies is a subject worthy of study is further reinforced by the debate on early chant as an orally transmitted tradition [9, 10], justifying an ethnomusicological perspective [11], although the extent of orality of the tradition has since been contested [12]. The formulaic structure of great responsories has been studied in detail [13], even in the pre-computer era [14]. 

Work on larger-scale computational analysis of chant melodies has recently been done in the area of melody segmentation [15], measurement of the melodic arch hypothesis [16] and of the relationship between antiphons and differentiae across modes [16]. Importantly, these works also provide the Cantus Corpus v0.2 database, which presents the contents of the Cantus Database in a manner ready 

> 2 The ecclesiastical environment of a mansucript, such as a monastery of a specific order, a city church, a cathedral. 

> 3 `https://dact-chant.ca/` 

> 4 Data is available at `github.com/Genome-of-Melody/ christmas/releases/tag/ISMIR2023` , tree inference code at `github.com/Genome-of-Melody/mrbayes_volpiano` . 

571 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

for further processing.<sup>5</sup> Cantus Index<sup>6</sup> also provides the Cantus Analysis tool,<sup>7</sup> which is however built solely for analyzing repertoire, not melodies. 

In MIR, the potential for applying bioinformatic tools as string processing models has been previously noted in the context of music similarity search. Tune family identification using Multiple Sequence Alignment (MSA) has been tried [17,18], and MSAs and and BLAST search has been used for melody classification and fast melody retrieval [19], with mixed results. 

More closely related to this work in terms of scientific goals, the field of cultural evolution has also been mapping patterns of musical diversity [20], with roots in the Cantometrics project [21]. Most notably, the evolution of folk melodies in English/US and Japanese traditions has been found to exhibit similar properties, using MSAs [22], and phylogeny of electronic music has been mapped using dynamic community detection rather than phylogenetic trees [23], citing limitations of the tree model in light of horizontal cultural transmission. Cultural and biological evolution was correlated in a study comparing populations in terms of genetics and their folk music [24]. 

Few works in MIR go beyond leveraging MSA as a tool for melodic similarity applications, and in one instance also on chant [25]. From the cultural evolution field have used some phylogenetic models to study music, but so far, not on chant. 

## 3. METHOD 

We model the relationships among melodies from a set of chant sources as a phylogenetic tree. The leaves of the chant sources, which carry (artificially ordered) melodies of the selected Cantus IDs in an analogy to how living species carry genes. Each instance of a chant with a certain Cantus ID in each source is a homologous sequence; the collection of melodies from one Cantus ID across sources is here termed a locus. The pipeline consists of the following steps: 

1. Concatenate cleaned melodies per source (in an arbitrary but fixed order of Cantus IDs) 

2. Compute a (partitioned) multiple sequence alignment (MSA) of the concatenated melodies 

3. Infer a phylogenetic tree over the MSA 

An overview of the pipeline is shown in Fig. 1. 

In the Cantus network of databases, chant melodies are transcribed as strings using Volpiano [26]. Volpiano is both a standard for encoding chant melodies in a plain text format,<sup>8</sup> and a font that renders these strings.<sup>9</sup> The encoding uses several non-tone characters, such as hyphens to indicate boundaries between neumes, syllables, and words, or barline characters to indicate sections. For our experiments, we have removed non-note characters (retaining 

> 5 `https://github.com/bacor/cantuscorpus` 

> 6 `https://cantusindex.org/` 

> 7 `https://cantusindex.org/analyse` 

> 8 `https://cantus.uwaterloo.ca/sites/default/ files/documents/2.\%20Volpiano\%20Protocols.pdf` 

> 9 `http://www.fawe.de/volpiano/` 

syllable and word separators did not have an appreciable effect on alignment, and would thus unnecessarily complicate the state space). 

Any string distance metric can then be used to model between two melodies, and between any two sources (by aggregating the distances between melodies). However, we specifically chose Bayesian phylogenetic trees as the model because (1) their inference procedure can distinguish between similarities that are substantial and those that are the product of chance, (2) the resulting trees, while perhaps not ideal as a model of transmission itself, are optimal results in terms of a clearly defined probabilistic model, and thus have a probabilistic interpretation that directly allows testing hypotheses about the dataset, rather than post-inference normalization of arbitrary similarity scores, (3) the software tools are readily available.<sup>10</sup> 

## 3.1 MSA and Score Matrix 

Multiple sequence alignment (MSA) was carried out with MAFFT v7.505 [27]. Mafft is used for the alignment of melodies because it is a state-of-the-art MSA tool that allows aligning arbitrary text using custom score matrices, thus allowing to process data which are not standard biological sequences such as DNA and aminoacids. (It has already been used in MIR, precisely for these advantages [28].) with our custom score matrix described below. We used a maximum of 1000 iterations and global pairing. 

By default, Mafft aligns arbitrary text by checking whether a given symbol is equal or not to other entries in the alignment. This is not a good model for melodies, as substitutions are not equally likely. The default choice for melodic distance, Mongeau-Sankoff distance [29] addresses the unequal costs of substituting different steps of the scale, but it and others are designed for tonal music, which chant predates by several hundred years. We have not in fact found sufficient music-theoretical understanding of chant melodies (and mode) to design a similar scoring function. Therefore, we resort to a basic physical reality: the cost of a substitution is the number of steps between the two notes, thus crudely mimicking how physically different the position in the melody might feel for a singer familiar with the alternative (see Fig. 2). The application of B flats were assigned a low cost because they were commonly applied without modifying considerably the melody. Liquescences were treated as regular notes of the same pitch. We stress that this is by no means a definitive chant scoring matrix, but rather a starting point to search for one. 

## 3.2 Bayesian Inference of Phylogenetic Trees 

A phylogenetic tree (hereafter: tree) is a graph representing the evolutionary relationships between the objects of study. These trees have long been used in evolutionary biology as a means to depict evolutionary relationships 

10 This article is not meant to inspire the impression that a large amount of technical work was performed: rather, we find it notable that already with a limited amount of technical work, this method already seems to obtain plausible results. 

572 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 



<!-- Start of picture text -->
Dataset MSA result Summary tree<br>Souces alignmentCompute(MAFFT) Sources mrbayes_volpianoInfer tree<br>VV Model settings:<br>Mkv+l+G<br>Concatenated melodies<br>ordered by cantuslD<br>Each source is a leaf.<br>Branch length ~ P(mutation)<br>Substitution model<br>for Volpiano<br>Figure 1. Outline of the pipeline for inference of phylogenetic trees of sources from melodies.<br>by the fast-growing number of possible trees for a<br>set of s terminals B(s)(s)s)) = 2 n ( − 2ss 2 −(n3−(n3−n3−3−− ) !2)2) , this problem<br>13<br><!-- End of picture text -->

by the fast-growing number of possible trees for a given set of s terminals B(s)(s)s)) = 2<sup>n</sup> <mark>(</mark><sup>−</sup> 2ss<sup>2</sup> −(n3−(n3−n3−3−− <mark>)</mark> !2)2)<sup><mark>,</mark>thisproblemcan-</sup> not be solved by visiting all possible topologies in order to calculate the normalising constant in the Bayes’ equation, which also, cannot be analytically solved even for a single topology. Therefore, MCMC sampling is used to construct the posterior densities for all the parameters of the model. The output of MCMC consists of inferred parameter values (mostly branch lengths), sampled trees, and the summary tree.The summary tree summarizes the posterior density of topologies in using a majority-rule consensus: it includes all bi-partitions which are at least in 50% of the sampled topologies. Node posterior probabilities are calculated from the relative frequency of bipartitions in the posterior tree density. Inferred trees are in principle unrooted.<sup>12</sup> 



<!-- Start of picture text -->
①<br>18<br>18 19<br><!-- End of picture text -->

Figure 2. Instances of scores from a reference pitch D. Arrows represent the final pitch and numbers under note bodies represent the score in the matrix. For MAFFT, scores are positive: the furthest distance between pitches is from G3 to D6, which has a score of 1, and the unison has the largest score, which is 19. 

among species, and we are here using it to represent the evolution of sources containing melodies in a similar way. 

Trees are composed of s leaf nodes of degree 1, called tips or terminals, and up to s − 1 internal nodes of degree 3 which represent ancestors. Trees may have a root node: an internal node of degree 2. If a tree is unrooted, there are up to s−2 internal nodes. Edges are called branches, and they have lengths that represent some amount of evolutionary change – usually (as in our case) the expected number of changes per site. 

Unfortunately, all existing software for Bayesian phylogenetics restricts the input data to some sort of biological data, be it DNA, aminoacid, or morphological data; therefore, we had to adapt an existing tool to process Volpiano-encoded chants. We chose to modify MrBayes v3.2.7a [34]. We call our fork `mrbayes_volpiano` , in order to make clear that it is intended for use only with data in volpiano format.<sup>13</sup> `mrbayes_volpiano` accepts Volpiano-encoded chant melodies as input and analyse them using a Markov model of evolution for an arbitrary number of the discrete character states [35]. It uses all the tools from MrBayes available for standard coding, which is the one applied to melody sequence data and can carry out inference of both single-partition or concatenated settings composed of multiple partitions. It processes alignments in nexus format and can be run both in interactive and scripting mode. 

Bayesian inference has been applied to phylogenetic tree estimation since the 1990s [30] and consists of calculating the posterior probability of the tree parameters (topology and branch lengths) for a given tree τ [31]: 



<!-- Start of picture text -->
f ( X | τi , Q)f ( τi )f (Q)<br>f (τi, Q|X) = (1)<br>∑ Bj=1(s) f (X|τj, Q)f (τj)f (Q)<br><!-- End of picture text -->

In this model, f (X|τi) is called the phylogenetic likelihood function, which gives the likelihood of observing the alignment data given the model of evolution parameters Q and a particular tree τi [32, 33]. Both f (τi) and f (Q) are priors for the topology and model of evolution. The topology prior is usually set to be uninformative (uniform over all possible trees). The prior f (Q) is derived from the Mkv+G model, which is the state of the art for morphology-based phylogeny.<sup>11</sup> As can be anticipated 

## 4. CHRISTMAS VESPERS DATASET 

In order to test the ability of our pipeline to resolve substantial relationships between chant sources, we apply it on a dataset of Christmas divine office, specifically Vespers for Vigilia Nativitatis Domini. The dataset was originally collected in order to study relationships between 

> 12 They can be rooted for visualisation e.g. using FigTree ( `https: //github.com/rambaut/figtree` ). 

> 13 The source code is available at `https://github.com/ gaballench/mrbayes_volpiano` 

> 11 As opposed to phylogenies built from sequences of nucleotides (DNA/RNA) or amino-acids (proteins), morphology-based phylogeny models mostly model transition probabilities from one to a different character as equally likely. 

573 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

late medieval Bohemian sources with the data including transcribed melodies available in the Hymnologica database,<sup>14</sup> and we combined this data with all further melodies available for Vig. Nat. Domini vespers from the Cantus Index interface, in order to cover a broader European context. 

The combined dataset contained 14 sources, and a total of 78 chants falling under 6 distinct Cantus IDs. Because the repertoire in office sources is not entirely consistent across sources and our system aligns melodies directly, we had to select a subset of chants contained in as many sources as possible, and then reduce the set of sources to those that contained as many of these chants as possible. The resulting dataset contained 14 sources, each of which had fully transcribed melodies for the following Cantus IDs: 001737, 002000, 003511, 004195, 007040a, and 605019.<sup>15</sup> 

Some sources contained multiple instances of chants of one Cantus ID: In that case, we retained the version with the most complete version of the melody (as repeated instances of the same chant are sometimes only written as incipits in the sources), and if multiple full melodies were available, we selected the melody that was directly in the Vig. Nat. Dom. section (see Tab. 1). 

Why use such a limited dataset, when the entirety of the Cantus Database is available? We originally intended to use the CantusCorpus dataset [15] of Office melodies. However, the authors of the Cantus Database preferred transcribing entire sources, so while there are more than 13000 fully transcribed antiphons in CantusCorpus v0.2 , the vast majority comes from less than 20 sources. This is further compounded by the surprising diversity of office repertoire. Thus, in the entirety of CantusCorpus, it is only possible to find 10 different sources that have transcribed melodies for 5 antiphons. Hence, we decided to use the Christmas dataset, with its advantage of having been collected specifically in order to make the comparison between different sources possible.<sup>16</sup> 

## 4.1 Sources and Evaluation 

Our methodology differs from machine learning experiments in when data is used. The phylogenetic tree model is selected and parametrized a priori, and only then we use a dataset to validate the model: is the tree inferred on the dataset plausible according to musicological expectations? Given that chant transmission provides few hard predictions, these expectations are not expressed in terms of target values. The evaluation of a tree’s plausibility is qualitative. 

Since we base the claim of valid results on comparing the inferred tree against known relationships between the sources, we must give an overview of the 14 sources in terms of their placement along the three major dimensions of chant culture: place, time, and liturgical context. This 

section essentially describes our “evaluation data”. 

A-Wn 1799**. A 13th century Cistercian antiphoner from the Rein monastery in Austria. 

A-VOR Cod. 259/I. A 14th century antiphoner of the collegiate chapter church of Vyšehrad, Prague. In the early 15th century, it was moved to Vorau because of Hussite wars. In 1490-1500, it was adapted for Salzburg liturgy.<sup>17</sup> 

CDN-Hsmu M2149.L4. Cistercian antiphoner from the Abbey of Salzinnes, Namur, in the Diocese of Liège, central Belgium, completed in 1554-1555.<sup>18</sup> 

CH-E 611. A 14th-century antiphoner from the Benedictine monastery of Einsiedeln, central Switzerland. 

CZ-HKm II A 4. An antiphoner from the 1470s, belonging to the municipal Church of the Holy Spirit in Hradec Králové, eastern Czechia.<sup>19</sup> 

CZ-PLm 504 C 004. A late antiphonary from the St. Bartholomew municipal church in Pilsen, western Czechia, from 1616.<sup>20</sup> 

CZ-Pu XVII E 1. A mixed Latin and Czech antiphonary from the early 16th century, of Czech (but further unspecified) provenance.<sup>21</sup> 

CZ-Pn XV A 10. Late 15th century notated breviary from the cathedral cursus in Prague, Czechia.<sup>22</sup> 

CZ-Pu I D 20. An antiphonary from the Augustinian monastery in Tˇreboˇn, southern Czechia, created in the 2nd half of the 14th century.<sup>23</sup> 

D-KA Aug. LX. A complex 12th-century antiphoner, of which the musical notation was almost completely rewritten in the 13th or 14th centuries. From the Zwiefalten Benedictine monastery in southwestern Germany, moved to the abbey of Reichenau in the 15th century.<sup>24</sup> 

D-KNd 1161. A late 12th- and early 13th-century Cistercian antiphoner, possibly written for use by the female abbey of Saint Mechtern in Cologne, western Germany, renamed Saint Apern in 1477.<sup>25</sup> 

F-Pn lat. 12044. An early 12th-century antiphoner from the Benedictine abbey of St.-Maur-de-Fossés, close to Paris, France.<sup>26</sup> 

F-Pn lat. 15181. An early 14th-century notated breviary belonging to the Notre Dame cathedral in Paris, France.<sup>27</sup> 

NL-Uu 406. A 12th-century antiphonary from St. Mary’s church in Utrecht, Netherlands. Later 13th-15thcentury changes. Complex source that has multiple versions of some melodies.<sup>28</sup> 

What results should one expect from a phylogeny of these chant sources? The three major dimensions of “ex- 

- 17 `https://manuscripta.at/hs_detail.php?ID=6267` 

> 18 `https://cantus.uwaterloo.ca/source/123723` 

19 `http://hun-chant.eu/source/1481?page=1` 

> 20 `https://rukopisy.zcm.cz/view.php?ID=504C004` 

21 `https://www.manuscriptorium.com/apps/index.` 

> `php?direct=record&pid=AIPDIG-NKCR__XVII_E_1___ _32Y2B65-cs#search` 

> 22 `http://hymnologica.cz/source/47` 

> 23 `http://hymnologica.cz/source/10721` 

> 24 `https://cantus.uwaterloo.ca/source/123612` 

> 14 `http://hymnologica.cz/jistebnice` 

> 15 All available via `https://cantusindex.org/id/(...)` . 

> 16 This quest for data also highlights the major limitation of our pipeline so far: we need comparable melodies from each source. 

- 25 `https://cantus.uwaterloo.ca/source/601861` 

- 26 `https://cantus.uwaterloo.ca/source/123628` 

- 27 `https://cantus.uwaterloo.ca/source/123631` 

28 `https://cantus.uwaterloo.ca/source/123641` 

574 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

|Source|Provenance|Date|Cursus|605019|001737|002000|003511|004195|007040a|
|---|---|---|---|---|---|---|---|---|---|
|A-Wn 1799**|Rein|1200s|Cistercian|1|NA|1|1|1|1|
|A-VOR Cod. 259/I|Prague|1360|Secular|1|2|1|1|1|1|
|CDN-Hsmu M2149.L4|Salzinnes|1554|Cistercian|1|NA|1|1|1|1|
|CH-E 611|Einsiedeln|1300s|Benedictine|1|3|1|1|1|1|
|CZ-HKm II A 4|Hr. Král.|1400s|Secular|1|1|1|1|1|1|
|CZ-PLm 504 C 004|Plsen|1616|Secular|1|1|1|1|1|1|
|CZ-Pu XVII E 1|Bohemia|1516|Unknown|1|NA|1|1|NA|1|
|CZ-Pn XV A 10|Prague|1300s|Secular|1|1|1|1|1|1|
|CZ-Pu I D 20|Passau|1300s|Augustinian|1|1|1|1|1|1|
|D-KA Aug. LX|Zwiefalten|1100s|Benedictine|1|1|1|1|1|1|
|D-KNd 1161|Köln|1200s|Cistercian|1|NA|1|1|1|1|
|F-Pn lat. 12044|Paris|1100s|Benedictine|1|1|1|1|2|1|
|F-Pn lat. 15181|Paris|1300s|Secular|1|NA|1|1|2|1|
|NL-Uu 406|Utrecht|1150|Secular|1|2|1|3|2|1|



Table 1. Sources of the Christmas Vespers dataset with their provenance, approximate date, cursus, and presence of the chant in each source (1 or more instances per source). NA represents chants not present in a given source. 

ternal” similarity between chant sources, in terms of how similar the segments of culture represented in these sources are expected to be, are geography, chronology, and cursus – space, time, and the liturgical context within which the books were used. It is not entirely clear in chant scholarship how strongly each of these factors should influence chant melodies (the exception where cursus is clearly expected to dominate other factors is that of the Cistercian order, which mandated that all monasteries must have identical liturgical books [36, p. 99]), but these organizing principles should be observed in the resulting tree. 

## 5. EXPERIMENTS AND RESULTS 

For all our experiments, we set up Bayesian inference using an Mkv model of evolution with options +I+G. Metropolis-Hastings MCMC sampling was carried out with four independent runs, each with four chains (one cold and three hot), with 10.000.000 generations, sampling each 1000 generations. Parameter and tree summaries were generated combining the four trace files after a burn-in of 50 % was applied to each. Parameter convergence was assessed by examining the potential scale reduction factor (PSRF) [37] which should approach 1.0 as runs converge, and the average standard deviation of split frequencies (ASDPF) [38] which should be below 0.01 for topological convergence. Other parameters had effective sample size (ESS) values above 600. We do not root the summary trees, because there is no clear outgroup in our dataset. 

## 5.1 Single-locus tree inference 

We first computed a tree for sets of melodies under each of the six Cantus IDs separately. In this setting, we examine whether the model can resolve the structure of diversity of individual melodies. 

For each cantus ID, we aligned the sets of melodies to obtain a nexus matrix that is then used as input for tree inference. This resulted in six different summary trees, one for each chant. We found varying but overall low degrees of resolution in topology. Some chants had nearly no variation and consequently the majority-rule consensus tree is almost a complete polytomy<sup>29</sup> (003511, 004195). Other 

chants had several internal nodes resolved, therefore representing some degree of information contained in a single melodic line which shows changes across sources However, at the scale of individual melodies, there was insufficient signal for the model to find meaningful differences. 

## 5.2 Multi-locus tree inference 

A concatenated experiment, in which the set of 14 sources was chosen to represent the terminals, was then conducted. We prepared individual alignments for each of the loci so that the boundaries for the same locus (Cantus ID) in the resulting nexus matrix were in fixed positions. Here, a tree was resolved (Fig. 3) that exhibits several properties that we believe make it a plausible model of how chant melodies in these sources are related. 

First, cursus. All the Cistercian manuscripts (“white monks”) are grouped tighlty together, with the lowest probability of differences – regardless of geographical area and century of origin. This is not entirely the case for the Benedictine manuscripts: the tree does keep together a S. German and a N. Swiss source, but the French Benedictine source is grouped with a French cathedral source. The probability of changes (expressed as branch length) is also much greater between the two closely related Benedictine manuscripts. Finally, there is an interesting case of the Augustinian CZ-Pu I D 20 manuscript and A- VOR Cod. 259/1. The latter is not from an Augustinian monastery, but belonged to a community of canon regulars – a type of clerical community from which the Augustinian order was organized in 1244. They are not particularly close – they do not have an extra internal node like e.g. the French manuscripts – but they are not separated by one, either, and they lie in between the rest of the Czech group and the rest of the tree. 

Second, geography. If one briefly disregards the Cistercian branch, the topology of the rest of the manuscripts does roughly correspond to their geographical distribution, from the French group in the west to the Czech group in the east. Note also that while there is some resolution in the group of Czech secular manuscripts, it is barely there: the internal nodes occur at most in six out of ten MCMC samples. 

Finally, chronology seems to exert a relatively weak influence, but the dataset is not well suited to study the development of chant melodies in time, as most of the Czech 

> 29 Star graph: a tree with only one internal node. 

575 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 



<!-- Start of picture text -->
NL-Uu<br>13(25)<br>F-Pn lat. 12044F-Pn lat. 15181 1550<br>CDN-Hsmu M2149.L4<br>11(25)<br>0.94 D-KNd 1161<br>0.79 0.83<br>1200<br>0.98<br>0.98<br>0.74 CH-E 611<br>CZ-PLm 504 C 004<br>1616 0.56 13(50)<br>0.52<br>CZ-Pn XV A 10 0.61<br>D-KA Aug. LX<br>14(75)<br>1000-1400<br>CZ-Pu XVII E<br>A-VOR Cod. 259/I<br>CZ-HKm II A 4<br>15(25)<br>0.01 CZ-PuI D 20<br>1470 14(75) 1370<br><!-- End of picture text -->

Figure 3. Main experimental result: summary of the posterior tree density as an unrooted majority-rule consensus tree for the concatenated dataset where each chant is a partition. All bipartitions present in at least 50% of the posterior trees are shown as internal nodes, with their nodal posterior probability. Terminals – tree leaves – are sources. Length of edges corresponds to probability of mutation; scale bar (bottom left) for 1 % expected mutation rate. Flags indicate geographical provenance, icons indicate cursus (black monks – Benedictines, white monks – Cistercians, heart – Augustinian, church building – secular cursus). Century (or half-century) indicated directly; some sources (D-KA Aug. LX, NL-Uu 406) have complex histories – see sec. 4.1. 

sources are later than most other sources, so it is not clear how to distinguish geographical and chronological factors, and there is only one non-Cistercian clearly pre-1300 old source (F-Pn lat. 12044) that was not modified in the later centuries (which is the case both with D-KA Aug. LX and NL-Uu 406). 

## 6. CONCLUSIONS AND FUTURE WORK 

The proposed chant phylogeny pipeline produced a musicologically plausible model of the melodic diversity within the Christmas chant dataset. We do not claim that the resulting tree in Fig. 3 is the only or best possible way to model the relationships between the sources from our Christmas Vigil dataset; however, while further work should primarily focus on assembling a larger dataset and designing a more robust validation procedure, we believe that based on the current result, the proposed method can meaningfully enrich digital chant scholarship. 

A major limitation is that the model requires homologous melodies (indicated by a shared Cantus ID). For the study of melodies to bypass this limitation, “morphological” features derived from melodies would be needed, so that we can process sources that do not share as many (transcribed) melodies. This is especially important for Office sources, where repertoire is strongly differentiated. 

Provided one is not interested in the of melodic diver- 

sity but only in repertoire structures of chant culture, one can build trees from binary features representing the presence/absence of Cantus IDs at given liturgical positions, using the same Bayesian model but with an alphabet of two rather than 19 characters. 

Another limitation is that the current method does not model chronology: it is not yet a model of chant melody evolution through time. This complicates interpreting the tree: one potentially attractive idea is that the internal nodes correspond to likely manuscript copying events, but without a more explicit chronology, this remains speculative. Chronology can be incorporated by using Bayesian divergence time estimation (BDTE), an extension of topology inference that produces branch lengths in absolute time rather than the expected number of substitutions per site by using time priors for either nodes or terminals. Furthermore, BDTE could infer a posterior distribution for nodes without observed time values, and thus we could estimate e.g. the times of origin of different layers of a more complex source (such as D-KA Aug. LX or NL-Uu 406) by using time priors rather than precise time values. 

Many methodological choices merit further exploration (such as the alignment scoring matrix, choice of tree model, or different ways of combining individual chants). However, based on the already plausible results of this pilot study, we are confident that chant phylogeny is a viable and exciting opportunity for digital chant scholarship. 

576 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

## 7. ACKNOWLEDGMENTS 

This publication was made possible through the support of a grant from the John Templeton Foundation (project Genome of Melody). The opinions expressed in this publication are those of the author(s) and do not necessarily reflect the views of the John Templeton Foundation. Jan Hajiˇc and Hana Vlhová-Wörner further acknowledge support from the Czech Science Foundation project no. 1928306X Old Myths, New Facts. 

## 8. REFERENCES 

- [1] D. Hiley, Western Plainchant: A Handbook, ser. Clarendon Paperbacks Series. Clarendon Press, 1995. 

- [2] W. Apel, Gregorian chant. London: Burns & Oates, 1958, vol. 601. 

- [3] D. Lacoste, “The Cantus Database and Cantus Index Network,” in The Oxford Handbook of Music and Corpus Studies. Oxford University Press, 2022. [Online]. Available: https://doi.org/10.1093/oxfordhb/ 9780190945442.013.18 

- [4] P. Wagner, “Germanisches und romanisches im frühmittelalterlichen kirchengesang,” in Bericht über den I. Musikwissenschaftlichen Kongreß der deutschen Musikgesellschaft in Leipzig 1925, Leipzig, Germany, 1925, pp. 21–34. 

- [5] ——, Einführung in die gregorianischen Melodien: t. Gregorianische Formenlehre; eine choralische Stilkunde. Breitkopf & Härtel, 1921, vol. 3. 

- [6] P. Ferretti, Estetica gregoriana: ossia, Trattato delle forme musicali del canto gregoriano, ser. Estetica gregoriana: ossia, Trattato delle forme musicali del canto gregoriano. Pontificio istituto di musica sacra, 1934, no. sv. 1. [Online]. Available: https://books.google.cz/books?id=vOWCnQEACAAJ 

- [7] L. Treitler, “Centonate" chant:" übles flickwerk" or" e pluribus unus?” Journal of the American Musicological Society, vol. 28, no. 1, pp. 1–23, 1975. 

- [8] D. Hiley, Western plainchant: a handbook. Oxford, United Kingdom: Clarendon Press, 1993. 

- [9] H. Hucke, “Toward a new historical view of gregorian chant,” Journal of the American Musicological Society, vol. 33, no. 3, pp. 437–467, 1980. 

- [10] L. Treitler, “The early history of music writing in the west,” Journal of the American Musicological Society, vol. 35, no. 2, pp. 237–279, 1982. [Online]. Available: http://www.jstor.org/stable/831146 

- [11] P. Jeffery, Re-Envisioning Past Musical Cultures: Ethnomusicology in the Study of Gregorian Chant, ser. Chicago Studies in Ethnomusicology. University of Chicago Press, 1992. [Online]. Available: https: //books.google.cz/books?id=2pfB84aGUnMC 

- [12] D. G. Hughes, “Evidence for the traditional view of the transmission of gregorian chant,” Journal of the American Musicological Society, vol. 40, no. 3, pp. 377–404, 1987. 

- [13] K. Helsen, “The use of melodic formulas in responsories: constancy and variability in the manuscript tradition,” Plainsong & Medieval Music, vol. 18, no. 1, pp. 61–76, 2009. 

- [14] W. H. Frere, Antiphonale Sarisburiense: a reproduction in facsimile of a manuscript of the 13th century, with a dissertation and analytical index. Gregg Press Limited, 1901. 

- [15] B. Cornelissen, W. H. Zuidema, J. A. Burgoyne et al., “Mode classification and natural units in plainchant.” in Proceedings of the 21st Int. Society for Music Information Retrieval Conf., Montreal, Canada, 2020, pp. 869–875. 

- [16] B. Cornelissen, W. Zuidema, and J. A. Burgoyne, “Studying large plainchant corpora using chant21,” in 7th International Conference on Digital Libraries for Musicology, 2020, pp. 40–44. 

- [17] P. E. Savage and Q. D. Atkinson, “Automatic tune family identification by musical sequence alignment,” in Proceedings of the 16th ISMIR Conference, vol. 163, 2015. 

- [18] D. Bountouridis, D. G. Brown, F. Wiering, and R. C. Veltkamp, “Melodic similarity and applications using biologically-inspired techniques,” Applied Sciences, vol. 7, no. 12, 2017. [Online]. Available: https: //www.mdpi.com/2076-3417/7/12/1242 

- [19] D. Bountouridis, D. Brown, H. V. Koops, F. Wiering, and R. C. Veltkamp, “Melody retrieval and classification using biologically-inspired techniques,” in Computational Intelligence in Music, Sound, Art and Design, J. Correia, V. Ciesielski, and A. Liapis, Eds. Cham: Springer International Publishing, 2017, pp. 49–64. 

- [20] P. E. Savage, “Cultural evolution of music,” Palgrave Communications, vol. 5, no. 1, pp. 1–12, 2019. 

- [21] A. Lomax, “Factors of musical style,” in Theory & practice: Essays presented to gene weltfish. Mouton The Hague, 1980, pp. 29–58. 

- [22] P. E. Savage, S. Passmore, G. Chiba, T. E. Currie, H. Suzuki, and Q. D. Atkinson, “Sequence alignment of folk song melodies reveals crosscultural regularities of musical evolution,” Current Biology, vol. 32, no. 6, pp. 1395–1402.e8, 2022. [Online]. Available: https://www.sciencedirect.com/ science/article/pii/S0960982222000926 

- [23] M. Youngblood, K. Baraghith, and P. E. Savage, “Phylogenetic reconstruction of the cultural evolution 

577 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

of electronic music via dynamic community detection (1975–1999),” Evolution and Human Behavior, vol. 42, no. 6, pp. 573–582, 2021. 

- [24] H. Pamjav, Z. Juhász, A. Zalán, E. Németh, and B. Damdin, “A comparative phylogenetic study of genetics and folk music,” Molecular Genetics and Genomics, vol. 287, no. 4, pp. 337–349, Mar. 2012. [Online]. Available: https://doi.org/10.1007/ s00438-012-0683-y 

   - [37] A. Gelman and D. B. Rubin, “Inference from iterative simulation using multiple sequences,” Statistical Science, vol. 7, no. 4, pp. 457–472, 1992. [Online]. Available: http://www.jstor.org/stable/2246093 

   - [38] F. Ronquist, P. van der Mark, and J. P. Huelsenbeck, Bayesian phylogenetic analysis using MRBAYES, 2nd ed. Cambridge University Press, 2009, p. 210–266. 

- [25] K. Szabová, Analytical tools for Gregorian chant. Bachelor thesis. Univerzita Karlova, Matematickofyzikální fakulta, 2021. 

- [26] K. Helsen and D. Lacoste, “A report on the encoding of melodic incipits in the cantus database with the music font ‘volpiano’,” Plainsong amp; Medieval Music, vol. 20, no. 1, p. 51–65, 2011. 

- [27] K. Katoh and D. M. Standley, “MAFFT Multiple Sequence Alignment Software Version 7: Improvements in Performance and Usability,” Molecular Biology and Evolution, vol. 30, no. 4, pp. 772–780, 01 2013. 

- [28] D. Bountouridis et al., “Music information retrieval using biologically inspired techniques,” Ph.D. dissertation, Utrecht University, 2018. 

- [29] M. Mongeau and D. Sankoff, “Comparison of musical sequences,” Computers and the Humanities, vol. 24, pp. 161–175, 1990. 

- [30] Z. Yang and B. Rannala, “Bayesian phylogenetic inference using DNA sequences: a Markov Chain Monte Carlo Method.” Molecular Biology and Evolution, vol. 14, no. 7, pp. 717–724, 07 1997. 

- [31] J. P. Huelsenbeck and F. Ronquist, “MRBAYES: Bayesian inference of phylogenetic trees ,” Bioinformatics, vol. 17, no. 8, pp. 754–755, 08 2001. 

- [32] J. Felsenstein, “Maximum-likelihood estimation of evolutionary trees from continuous characters.” American Journal of Human Genetics, vol. 25, no. 5, pp. 471–492, Sep. 1973. 

- [33] ——, “Evolutionary trees from gene frequencies and quantitative characters: Finding maximum likelihood estimates,” Evolution, vol. 35, no. 6, pp. 1229–1242, 1981. 

- [34] F. Ronquist and J. P. Huelsenbeck, “MrBayes 3: Bayesian phylogenetic inference under mixed models,” Bioinformatics, vol. 19, no. 12, pp. 1572–1574, 08 2003. 

- [35] P. O. Lewis, “A likelihood approach to estimating phylogeny from discrete morphological character data,” Systematic biology, vol. 50, no. 6, pp. 913–925, 2001. 

- [36] J. Glasenapp, To Pray without Ceasing: A Diachronic History of Cistercian Chant in the Beaupré Antiphoner (Baltimore, Walters Art Museum, W. 759– 762). Columbia University, 2020. 

578 

