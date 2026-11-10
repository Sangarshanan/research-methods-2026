---
paper_id: "000012"
year: 2022
title: "Download pdf"
source_url: "https://zenodo.org/record/7316608/files/000012.pdf"
---

# DETECTING SYMMETRIES OF ALL CARDINALITIES WITH APPLICATION TO MUSICAL 12-TONE ROWS 

Anil Venkatesh Viren Sachdev 

Department of Mathematics and Computer Science, Adelphi University 

avenkatesh@adelphi.edu 

## ABSTRACT 

Popularized by Arnold Schoenberg in the mid-20th century, the method of twelve-tone composition produces musical compositions based on one or more orderings of the equal-tempered chromatic scale. The work of twelve-tone composers is famously challenging to traditional Western tonal and structural sensibilities; even so, group theoretic approaches have determined that 10% of certain composers’ works contain a highly unusual classical symmetry of music. We extend this result by revealing many symmetries that were previously undetected in the works of Schoenberg, Webern, and Berg. Our approach is computational rather than group theoretic, scanning each composition for symmetries of many different cardinalities. Thus, we capture partial symmetries that would be overlooked by more formal means. Moreover, our methods are applicable beyond the narrow scope of twelve-tone composition. We achieve our results by first extending the group-theoretic notion of symmetry to encompass shorter motives that may be repeated and reprised in a given composition, and then comparing the incidence of these symmetries between the work of composers and the space of all possible 12-tone rows. We present four candidate hierarchies of symmetry and show that in each model, between 75% and 95% of actual compositions contained high levels of internal symmetry. 

## 1. INTRODUCTION 

The Viennese composers Arnold Schoenberg, Anton Webern, and Alban Berg produced a combination of 86 twelve-tone compositions in the early-to-mid 20th century [1±3]. Each of these compositions is constructed from some permutation of the twelve pitch classes of the equaltempered chromatic scale, which then guides the order of notes in the melody and harmonies. Figure 1 shows musical notation for one such permutation of the pitch classes that was selected by Schoenberg. Each such permutation is called a tone row, and we will take the Viennese tone rows to mean those that underlie the compositions of Schoen- 

> © A. Venkatesh and V. Sachdev. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: A. Venkatesh and V. Sachdev, ªDetecting Symmetries of All Cardinalities With Application to Musical 12-Tone Rowsº, in Proc. of the 23rd Int. Society for Music Information Retrieval Conf., Bengaluru, India, 2022. 



<!-- Start of picture text -->
   <br>       <br><br><!-- End of picture text -->

Figure 1. Musical notation for the row from Schoenberg’s Serenade, opus 24, movement 5. Note that each pitch class is used once. 

berg, Webern, and Berg, the principal members of the Second Viennese School. Using Hauer’s arrangement of the pitch classes at the hour marks of an analog clock diagram [4], each tone row can be visualized as a directed graph that visits each vertex once, and the set of these directed graphs is in bijection with the set of tone rows [5,6]. 

The strict rules of twelve-tone composition and its inherent relation to permutations have inspired formal mathematical study, both combinatorial and group theoretic. Recent work by von Hippel and Huron applied a keyfinding algorithm to subsets of all lengths within certain tone rows in order to quantify their degree of ªtonalnessº [7]. This combinatorial approach construes the tone row as the union of many shorter overlapping subsets whose individual properties imply properties of the tone row as a whole. By contrast, Hunter and von Hippel treated tone rows more like indivisible algebraic objects in their grouptheoretic study, showing that the action of the dihedral group (rotations and reflections) on clock diagrams, together with the operation of reversing the diagram’s arrows, encompass the classical music-theoretic symmetries of translation, inversion, and retrograde [8]. 

The composers of the Second Viennese School considered tone rows to be equivalent under these symmetries so it makes sense to study equivalence classes of tone rows instead of the rows themselves. The resulting row classes of Schoenberg and Webern can therefore be visualized as unlabeled, undirected clock diagrams (start and end points need not be distinguished due to equivalence under retrograde). Berg also considered a fourth symmetry, cyclic shift, so his row classes are larger: they are equivalent to unlabeled, undirected clock diagrams whose endpoints connect [3]. Figure 2 shows clock diagrams of the twentyone row classes used by Webern, with the four diagrams that possess dihedral symmetry set apart from the others. These four diagrams correspond to row classes that are isomorphic to their retrograde. The fact that Berg considered an extra symmetry has the practical effect of making his row classes larger, and hence the set of row classes smaller, 

109 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



Figure 2. Clock diagrams of the twenty-one tone rows used by Webern, with the four symmetric diagrams on the left. 

than those of Schoenberg and Webern. In this work, we follow convention by studying the two alternatives in parallel as the methods of study are otherwise unaffected by the use of an extra symmetry. 

Hunter and von Hippel posed and resolved the following question: are there more symmetric Viennese tone rows than would be expected by chance alone? By the numbers, symmetric rows comprise just 5% of Schoenberg’s works, 19% of Webern’s, and 9% of Berg’s. However, symmetric rows are exceedingly rare among all row classes: just 0.13% of row classes possess dihedrally symmetric clock diagrams (the figure is 1.16% when Berg’s cyclic shift symmetry is included). Hunter and von Hippel made this idea rigorous by using a hypergeometric test to conclude that these composers showed a statistically significant preference for symmetry, whether intentionally or not [8]. 

Results of this kind can be concretely informative to music scholars as well as mathematicians. Most directly, Hunter and von Hippel offered analytical evidence that the three composers preferred symmetric row classes, a fact that had already been believed widely among music scholars [2, 3]. However, their results also contradicted certain beliefs, for example that Webern preferred non-palindromic symmetry [2]. They found that nonpalindromic symmetry is simply much more common than palindromic symmetry, more than accounting for its higher incidence in Webern’s corpus. In short, the enumeration of row classes and their symmetries is a truly interdisciplinary undertaking with promise to inform music scholars in ways that are relevant to their practice. 

The main question left open by Hunter and von Hippel relates to the fact that just 10% of the Viennese tone rows are symmetric. While this figure is already surprisingly high compared to the incidence of symmetry among all row classes, it still leaves the fact that the Viennese twelve-tone composers evidently had some priorities beyond symmetry alone. Indeed, music scholars have posited many other properties of tone rows that may have attracted the composers’ interest: ªcombinatorial,º ªall-interval,º ªtonally colored,º and particularly ªderivedº rows have all been subject to study [9, 10]. Derived rows are those that consist of a sequence of 12/d notes repeated d times under the various transformations available to the composer [10]. 

The Gotham and Yust Serial Analyzer project [11] has yielded a catalog of rows in the repertoire classified by these traditional properties as well as more novel harmonic properties deduced from the discrete Fourier transform approach of Krumhansl [12]. The set of all possible derived rows has also been enumerated algebraically. Fripertinger and Lackner generalized the work of Hunter and von Hippel by constructing a group action and classified all tone rows according to the traditional properties in the Database of Tone Rows and Tropes [10]. To our knowledge, this database has yet to be studied in the sense of Hunter and von Hippel to determine whether the Viennese tone rows contain statistically significant quantities of derived rows, for example. 

The combinatorial study of tone rows has led to the enumeration of rows with various traditionally studied properties as well as measurements of ªtonalnessº and other harmonic properties. Meanwhile on the group-theoretic side, Fripertinger and Lackner’s group action has helped enumerate the derived rows, a much richer set than the fully symmetric rows of Hunter and von Hippel. Missing from the literature is a combinatorial attack on the definition of symmetry in tone rows: just as Yust [13] extended von Hippel and Huron’s study of tonal fit to pairs of tonal, atonal, and mixed dimensions, this paper uses combinatorial means to generalize the concept of derived row, capturing nuances that are impractical to detect with group theory. For example, if we permute just the last two notes of a derived row, the resulting tone row will most likely not possess any group theoretic symmetries. The rigidity of group-theoretic symmetries causes this type of partial symmetry to be overlooked. In this work, we introduce a combinatorial alternative to the group-theoretic definitions of symmetry, scanning each tone row for partial symmetries of all cardinalities. Our approach results in a complete catalog of recurring motives within each tone row, from which we argue that the vast majority of the Viennese tone rows contain unusually high levels of symmetry. Moreover, we believe the flexibility of our approach grants it applications beyond the narrow scope of twelve-tone composition. 

## 2. DETECTING INTERNAL SYMMETRY 

For the purpose of this work, a motive within a tone row is any consecutive sequence of notes that recurs at least once within the same row (transposed and possibly inverted or in retrograde). For example, the row (0, 1, 10, 5, 2, 3, 6, 7, 8, 11, 4, 9) contains the motive (0, 1, 10, 5) which repeats transposed under retrograde inverse as (10, 5, 2, 3), as shown in the top line of Figure 3. This particular row also contains the motive (3, 6, 7, 8) and its transposed retrograde inverse (6, 7, 8, 11). Motives can be as short as two notes or as long as twelve; whereas motives of length 2 occur whenever the same musical interval (or its inverse) is reused in a tone row, motives of length 12 are only found in the rare palindromic rows. The highest incidence of motives can be found in the chromatic scale and the circle of fifths, each of which consists of a single length-2 segment whose corresponding musical interval is 

110 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



Figure 3. Clock diagrams of the tone row (0, 1, 10, 5, 2, 3, 6, 7, 8, 11, 4, 9) showing the nine sequences of length 4. The two recurring motives are indicated with doubled lines. 

repeated eleven times to form the row. In the opposite case, the all-interval rows consist of every different musical interval and consequently possess very few motives. Figure 4 shows clock diagrams for the circle of fifths (containing the maximum number of motives of all lengths) and an allinterval row that contains no motives above length 2 at all. 

Our approach has two stages: first, we enumerate the motives of all lengths for every row class; then, we advance four plausible models for assigning an overall symmetry rating to any set of motives, with attention to the musictheoretic and mathematical literature to ensure consistency of our results with existing knowledge. We begin the first stage by treating each tone row as a collection of length-d sequences of notes, with d ranging from 2 to 12. Figure 3 shows a particular tone row’s nine sequences of length 4, of which two pairs are found to be separate recurring motives. In general, the set of length-d motives of a tone row can be quantified by a partition of 12 − d + 1 (the total number of length-d sequences) based on which sequences appear multiple times. Figure 3 shows that the depicted tone row corresponds to the partition 9 = 2 + 2 + 1 + 1 + 1 + 1 + 1 since there are two motives that each appear twice, plus five other length-4 sequences that do not form motives. As d varies from 2 to 12, the corresponding sets of motives fully encode the symmetrical properties of a tone row at every cardinality. Therefore, the symmetrical properties of any tone row can be represented by a list of partitions of the integers from 1 to 11, corresponding to values of d ranging from 12 down to 2. We refer to such a list of partitions as the full symmetry data of a row class. 

Generalizing symmetry in this way encodes a tremendous amount of information. Hunter and von Hippel identify three types of rows (eight, when cyclic shift is included) [8]. Friptertinger and Lackner extend this to a few thousand by introducing tropes [10]. But a naïve up- 



Figure 4. Clock diagrams of the maximally symmetric circle of fifths and a minimally symmetric all-interval row. 



Figure 5. Clock diagrams of the tone row (0, 1, 8, 11, 10, 3, 2, 7, 4, 6, 9, 5) showing that it achieves symmetry scores of 3, 4, and 2 for the lengths of 2, 3, and 4, respectively. 

per bound on the number of distinct full symmetry data is the product of the first eleven partition numbers, about 5.379 × 10<sup>10</sup> or five thousand times the number of row classes! There are many principled ways to simplify the full symmetry data while maintaining consistency with the literature. One promising approach (not explored in this paper) would map each partition to its length, summarizing the symmetry data of a tone row with an integer 11tuple. Under this scheme, rows whose 11-tuple values are small exhibit more repetitive motives (hence, greater symmetry) than those whose 11-tuple values are large. In an extreme example, the chromatic scale and the circle of fifths achieve scores of all 1’s in this scheme. In this paper, we choose to map the full symmetry data to a differently defined 11-tuple: the maximum values of the partitions. The reason for using the maximum value instead of the length is subjective as both schemes capture essential information about the partition. Figure 5 depicts a tone row whose most-repeated motives of length 2, 3, and 4 have multiplicities of 3, 4, and 2, respectively. This particular tone row has no motives of length 5 or greater, meaning that its symmetries are quantified by the tuple (3, 4, 2, 1, 1, 1, 1, 1, 1, 1, 1). We refer to this tuple as the symmetry score of the row class. 

## 3. ANALYSIS 

In Section 2 we established a map from the set of row classes to an 11-dimensional lattice with the property that greater values correspond to higher multiplicity of motives. The two clock diagrams in Figure 4 illustrate this property: 

111 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

whereas the circle of fifths maps to a symmetry score of (11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1), the depicted all-interval row maps to a symmetry score of (2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) which is in fact the lowest possible multiplicity of motives among all row classes. The next step is to assess whether the Viennese tone rows contain unusually high levels of symmetry, but this depends on how we compare symmetry scores to each other. Instead of presenting just one possible interpretation of ªhigh symmetry,º we give four reasonable candidates that span a wide range of interpretations of symmetry while still respecting musical intuition and the mathematical literature on the topic. In each model, we conduct hypergeometric tests to gauge whether the incidence of high symmetry in the composers’ corpora was significantly greater than would be predicted by chance alone. While these tests are exploratory in nature, the models in Sections 3.1 and 3.2 admit a conservative Bonferroni correction to adjust for the issue of multiple testing [14]. 

## 3.1 Reverse-Lexicographic Model 

The most direct extension of Hunter and von Hippel’s results is to introduce a sensible total order on the set of symmetry scores, then split the scores into ªlowº and ªhighº bins in music-theoretically sound ways and apply a hypergeometric test. A natural candidate for the total order is reverse-lexicographic order (RLEX), prioritizing longer motives over shorter ones. This choice has the advantage of seamlessly reproducing known results in its base case; moreover, it yields a natural definition of low and high symmetry: for each length d, the valid splits are the locations in the total order at which the d-symmetry score increments. For example, we can split the set of tone rows according to whether any length-4 motive is present; in the set of all row classes, 23.62% have a length-4 motive, yet fully 50% of Schoenberg’s tone rows exhibit this symmetry. The associated hypergeometric test gives a p-value of p < 0.0002, so the prevalence of motives of length at least 4 in Schoenberg’s work is unlikely to have arisen by chance alone. This model has 38 splits (40 for Berg) and the adjusted p-values are computed by multiplying by these numbers. Table 1 shows a selection of significant results for the three composers. Notably, more than 90% of Webern’s corpus exhibits a statistically significant level of symmetry in the RLEX sense and both Schoenberg and Webern’s corpora exhibit significant levels of symmetry under the multiple testing correction. Berg’s use of a fourth symmetry and the correspondingly smaller space of row classes makes it more difficult to obtain significant results for his corpus, as already noted by Hunter and von Hippel. However, even in this case a few notable results are seen, although only on an exploratory basis. 

## 3.2 Lattice Rank Model 

The RLEX model faithfully reproduces known results, yet strongly penalizes row classes that contain many short motives but few long ones. The Lattice Rank model delivers on the opposite extreme by using a grading according to 



Figure 6. Directed acyclic graph representation for the partially ordered set of symmetry scores relevant to Schoenberg and Webern. 

the sum of the symmetry score, thereby equally weighting motives of all lengths. Here, the natural divisions of ªhighº and ªlowº symmetry are determined by the rank function with 54 distinct levels (109 for Berg). For example, two-thirds of Webern’s tone rows have lattice rank of 6 or greater (that is, 6 more multiplicity of motives than the lowest symmetry score), while only 11.17% of the set of all row classes has this property. The quantity of tone rows in Webern’s corpus with at least this lattice rank almost certainly did not arise by chance alone (p = 2.5 × 10<sup>−9</sup> ). Table 2 shows that the Lattice Rank model obtains remarkably similar results to the RLEX model in spite of being agnostic to motive length. Again, Schoenberg and Webern’s corpora exhibit statistically significant levels of symmetry even under the multiple testing correction, while Berg’s corpus only does so on an exploratory basis. 

The fact that the RLEX and Lattice Rank models yield similar results in spite of applying diametrically opposed weighting schemes to motives of different lengths suggests that the Viennese tone rows simply contain a lot of internal symmetries no matter how you count them. Still, these models impose value judgments on the relative importance of each internal symmetry, possibly affecting the outcome of the analysis. To validate our findings, we offer a non-parametric alternative that makes no assumptions at all about the relative importance of the different motives. Instead, this alternative is based on the single intuitive assumption that the symmetry scores form a partially ordered set: a row class whose symmetry score is no greater in any component than the symmetry score of a different row class cannot be said to exhibit greater symmetry overall. Abstracting from the lattice structure in this way results in the diagrams in Figures 6 and 7, where each vertex is a symmetry score and the directed edges (all running left-toright) run from lesser to greater in the partial order. 

112 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

|Schoenberg|All|p-value|Webern|All|p-value|Berg|All|p-value|
|---|---|---|---|---|---|---|---|---|
|76.19%**|45.50%|5.11×10<sup>−5</sup>|90.48%***|39.15%|1.51×10<sup>−6</sup>||||
|50.00%**|23.62%|1.88×10<sup>−4</sup>|57.14%*|23.68%|1.01×10<sup>−3</sup>|47.83%|28.84%|0.042|
|38.10%***|11.11%|5.47×10<sup>−6</sup>|42.86%**|11.16%|2.23×10<sup>−4</sup>||||
|11.90%|2.29%|2.67×10<sup>−3</sup>|28.57%***|2.29%|5.89×10<sup>−6</sup>|8.70%|1.04%|0.024|
|4.76%|0.13%|1.50×10<sup>−3</sup>|19.05%***|0.13%|1.93×10<sup>−8</sup>||||



Table 1. Selected RLEX results for each composer, comparing their corpora to the set of all row classes with respect to various ªhighº and ªlowº symmetry bins. Asterisks indicate significance level under conservative Bonferroni correction. * : p < .05, ** : p < .01, *** : p < 0.001. 

|Schoenberg|All|p-value|Webern|All|p-value|Berg|All|p-value|
|---|---|---|---|---|---|---|---|---|
|83.33%|66.07%|0.011|95.24%|66.07%|1.96×10<sup>−3</sup>||||
|47.62%**|20.87%|9.98×10<sup>−5</sup>|71.43%***|20.87%|9.13×10<sup>−7</sup>|56.52%|35.04%|0.029|
|33.33%**|11.17%|1.17×10<sup>−4</sup>|66.67%***|11.17%|2.54×10<sup>−9</sup>||||
|9.52%*|0.90%|5.48×10<sup>−4</sup>|38.10%***|0.90%|7.48×10<sup>−12</sup>|17.39%|4.50%|0.018|
|7.14%***|0.11%|1.47×10<sup>−5</sup>|19.05%***|0.04%|1.38×10<sup>−10</sup>||||



Table 2. Selected Lattice Rank results for each composer, comparing their corpora to the set of all row classes with respect to various ªhighº and ªlowº symmetry bins. Asterisks indicate significance level under conservative Bonferroni correction. * : p < .05, ** : p < .01, *** : p < 0.001. 

## 3.3 Partial Order Rating Models 

In order to set up a hypergeometric test on the poset of symmetry scores, we still need to choose some linear extension of the poset to a total order. The RLEX and Lattice Rank models accomplish this by appealing to music intuitions on the relative importance of different kinds of motives. However, the fact that our poset has a unique least and greatest element gives us a non-parametric alternative. Given any symmetry score v, we count the number of row classes with strictly lesser scores (ascendants) and strictly greater scores (descendants) in the poset. If v has relatively few descendants compared to ascendants, then few row classes have strictly greater symmetry than v and we may say that v possesses a relatively high level of symmetry. To make this idea precise, let Av be the number of row classes assigned to strictly lesser scores than v, and Dv be the number of row classes assigned to strictly greater scores than v. Lastly, let M be the total number of row classes. The formula 



<!-- Start of picture text -->
1<br>2 ( 1 + (Av − Dv)/M ))<br><!-- End of picture text -->

ranges from 0 to 1 as v ranges from the least to greatest elements of the poset. We define the Solo Poset Rating of v by renormalizing this formula to range from 0 to infinity, like so: 



<!-- Start of picture text -->
PRs(v) = − log � 1 − 2 1 ( 1 + (Av − Dv)/M )) �<br>= − log � 12 ( 1 − (Av − Dv)/M ) � . (1)<br><!-- End of picture text -->

In Figure 7, the symmetry score marked by the black vertex would receive a relatively high Solo Poset Rating because it has many ascendants but relatively few descendants. This imbalance is further amplified by the fact that 

scores near the minimum symmetry score are generally assigned to many more row classes than scores near the maximum symmetry score. 

For example, two of Berg’s tone rows have a symmetry score of (6, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1), whose Solo Poset Rating is 0.695. An additional ten of Berg’s tone rows achieve a greater Solo Poset Rating than this, so 12/23 or 52.17% of Berg’s tone rows exhibit a Solo Poset Rating of 0.695 or greater. Meanwhile, just 29.42% of all tone rows achieve a Solo Poset Rating of at least 0.695. If Berg had selected row classes at random, the probability that twelve or more of his corpus would have a Solo Poset Rating of at least 0.695 is just 0.018. 

Figure 7 shows that for any given symmetry score, there are many other scores in the poset that are incomparable. We define the Cohort Poset Rating of a particular score as the average of the Solo Poset Ratings of all scores that are incomparable with the chosen score. Both variants of the Poset Rating quantify how close a given score is to the highest possible symmetry score, compared to its closeness to the lowest possible symmetry score. The two ratings yield nearly identical results when analyzing the corpora of Schoenberg and Webern (Tables 3 and 4). Due to Berg’s smaller space of row classes, the only noteworthy finding for his corpus under the Poset Rating models is the one given in the previous paragraph (the Solo and Cohort models coincide in this case). 

## 4. DISCUSSION 

Our work takes a flexible approach to detecting patterns within tone rows, uncovering partial symmetries that cannot be detected by group theory. The trade-off is that we also find many internal structures that have no name in music theory. Whether this is a true disadvantage depends on 

113 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



Figure 7. Directed acyclic graph representation of the symmetry scores relevant to Berg with highlighted ascendants and descendants of the black vertex, and incomparable scores greyed out. 

|Schoenberg|All Solo(Cohort)|p-value|
|---|---|---|
|83.33%|65.87%|0.010|
|52.38%|26.23%|2.73×10<sup>−4</sup>|
|33.33%|12.85% (11.65%)|5.13×10<sup>−4</sup>|
|9.52%|0.74% (0.60%)|2.73×10<sup>−4</sup>|
|4.76%|0.74% (0.13%)|9.08×10<sup>−3</sup>|



Table 3. Selected Poset Rating results for Schoenberg, comparing his corpus to the set of all row classes with respect to various ªhighº and ªlowº symmetry bins. When the Solo and Cohort ratings do not coincide, the larger of the two p-values is displayed for brevity. 

|Webern|All Solo(Cohort)|p-value|
|---|---|---|
|95.24%|45.35%|1.62×10<sup>−6</sup>|
|66.67%|12.85% (16.03%)|2.78×10<sup>−7</sup>|
|52.38%|2.85%|2.67×10<sup>−12</sup>|
|33.33%|1.03% (1.06%)|1.51×10<sup>−9</sup>|
|19.05%|0.12% (0.25%)|2.39×10<sup>−7</sup>|



Table 4. Selected Poset Rating results for Webern, comparing his corpus to the set of all row classes with respect to various ªhighº and ªlowº symmetry bins. When the Solo and Cohort ratings do not coincide, the larger of the two p-values is displayed for brevity. 

the validity of our basic premise: that the presence of a recurring motive is noteworthy in itself. We believe that this premise is supported by the preexisting scholarly interest in derived rows, those tone rows that are fully generated by a shorter repeating motive [10]. Since small adjustments to a derived row result in similar rows that yet lack any official symmetry, it seems natural to extend the concept of derived row to any tone row that is at least partially generated by a motive. 

In bringing new methods to this topic, we have made particular effort to situate our work in the literature and reproduce known results where possible. Indeed, all our models agree with the existing knowledge that roughly 5% of Schoenberg’s corpus and 19% of Webern’s corpus have significant incidence of symmetry at the highest level. The RLEX model in particular achieves exact replication of known results. Where it was necessary for us to make a value judgment on the relative importance of different motives, we have followed the literature (in the case of RLEX) and also explored the diametrically opposed value judgment (in the case of Lattice Rank) in order to provide maximum contrast. In each case, we performed a multiple testing correction and still found significant levels of symmetry in much of the tone rows of Schoenberg and Webern. We also developed two non-parametric models to further validate our findings. Moreover, our approach to defining symmetry by the presence of shorter motives is analogous to von Hippel and Huron’s measurement of the ªtonalnessº a row by the tonal properties of its subsets [7]. 

As for whether the Viennese twelve-tone composers favored symmetry in their work, our models support this across the board. We find that all three composers made extensive use of symmetry in their work, decidedly beyond what can be explained by chance alone. We found that 76%±83% of Schoenberg’s corpus and 90%±95% of Webern’s corpus contained significant levels of symmetry (up from 5% and 19%, respectively.) Even in the case of Berg, whose much smaller space of row classes limits the power of the hypergeometric test, we can extend the previously determined figure of 9% to the range of 48%±57% of his corpus although only on an exploratory basis. 

Our combinatorial approach has one other advantage over the group-theoretic approaches in the literature. By forgetting the permutation group structure and studying motives on a purely combinatorial level, we no longer restrict ourselves to studying tone rows. Indeed, our methods apply just as well to any data series together with a relevant group of symmetries, with the one concession that there is no clear analog for the hypergeometric test. Still, the n-tuple symmetry score can serve as a feature for classification of melody and rhythm that encodes information of many different cardinalities, evoking concepts from persistent homology and wavelet analysis. While we assert no formal connection between these fields and our work, we take inspiration from the concept of studying an object at many different scales and hope that our success in the enumeration of tone row motives may find broader application in music information retrieval. 

114 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

## 5. REFERENCES 

- [1] E. Haimo, ªThe evolution of the twelve-tone method,º in The Arnold Schoenberg Companion (W. B. Bailey, ed.), pp. 101±128, Westport, CT: Greenwood Press, 1998 

- [2] K. Bailey, The Twelve-Note Music of Anton Webern: Old Forms in a New Language. Cambridge: Cambridge University Press, 1991. 

- [3] D. Headlam, The Music of Alban Berg. New Haven, CT: Yale University Press, 1996. 

- [4] J. M. Hauer, Zwölftontechnik : die Lehre von den Tropen. Wien: Universal Edition, 1925. 

- [5] E. Amiot, ªMathématiques et analyse musicale: une fécondation réciproque,º in Analyse Musicale, vol. 28, pp. 37±41, 1992. 

- [6] E. Krenek, ªMusik und Mathematik,º in Über neue Musik, pp. 71±89, Vienna, Verlag der Ringbuchhandlung, 1937 

- [7] P. T. von Hippel and D. Huron, ªTonal and ‘Anti-Tonal’ Cognitive Structure in Viennese Twelve-Tone Rows,º in Empirical Musicology Review, vol. 15, No. 1-2, 2020. 

- [8] D. J. Hunter and P. T. von Hippel, ªHow Rare is Symmetry in Musical 12-Tone Rows?,º in The American Mathematical Monthly, vol. 110, No. 2, pp. 124±132, February 2003. 

- [9] M. Babbitt, ªSome aspects of twelve-tone composition,º in The Score and I.M.A. Magazine, vol. 12, pp. 53±61, 1955. 

- [10] H. Fripertinger and P. Lackner, ªTone rows and tropes,º in Journal of Mathematics and Music, vol. 9, No. 2, pp. 111±172, 2015. 

- [11] M. Gotham and J. Yust, ªSerial Analysis: A Digital Library of Rows in the Repertoire and their Properties, with Applications for Teaching and Research,º in DLfM ’21: 8th International Conference on Digital Libraries for Musicology, New York, NY: Association for Computing Machinery, 2021. 

- [12] C. Krumhansl, Cognition foundations of musical pitch, New York, NY: Oxford University Press, 1990. 

- [13] J. Yust, ªDimensions of Atonality: A Response and Extension of von Hippel and Huron (2020),º in Empirical Musicology Review, vol. 15, No. 1-2, pp. 119 - 119, 2020. 

- [14] M. Jafari and N. Ansari-Pour, ªWhy, When, and How to Adjust Your P Values?,º in Cell J., vol. 20, No. 4, 2019. 

115 

