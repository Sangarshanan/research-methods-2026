---
paper_id: "000015"
year: 2023
title: "Download pdf"
source_url: "https://zenodo.org/record/10265243/files/000015.pdf"
---

# SIMILARITY EVALUATION OF VIOLIN DIRECTIVITY PATTERNS FOR MUSICAL INSTRUMENT RETRIEVAL 

Fabio Antonacci Augusto Sarti 

Mirco Pezzoli Raffaele Malvermi Fabio Antonacci Augusto Sarti Dipartimento di Elettronica, Informazione e Bioingegneria - Politecnico di Milano, Milan, Italy 

```
mirco.pezzoli@polimi.it,raffaele.malvermi@polimi.it
```

## ABSTRACT 

The directivity of a musical instrument is a function that describes the spatial characteristics of its sound radiation. The majority of the available literature focuses on measuring directivity patterns, with analysis mainly limited to visual inspections. Recently, some similarity metrics for directivity patterns have been introduced, yet their application has not being fully addressed. In this work, we introduce the problem of musical instrument retrieval based on the directivity pattern features. We aim to exploit the available similarity metrics for directivity patterns in order to determine distances between instruments. We apply the methodology to a data set of violin directivities, including historical and modern high-quality instruments. Results show that the methodology facilitates the comparison of musical instruments and the navigation of databases of directivity patterns. 

## 1. INTRODUCTION 

The analysis of the directional sound radiation characteristics of musical instruments is a rather old topic in the literature with first works by Olson [1] and Meyer [2–4] dating back to the seventies. In the past few decades, numerous studies were proposed mainly focusing on accurate measurements of the directivity patterns [5–8] or on qualitative comparisons of the instrument characteristics [9–11]. 

Recently, the interest in spatial audio technologies [12] for virtual and augmented reality increased the attention towards the modeling and analysis of directivity patterns. In particular, the modeling of directional sound sources showed to provide improved sound field reconstruction for the navigation of sound scenes [13,14]. Therefore, different solutions have been proposed to include the directivity of acoustic sources in simulation frameworks such as boundary and finite element methods [15], numerical simulation [16] and geometrical acoustics [17]. As a matter of fact, the directivity of sound sources impacts on the accuracy of room acoustics simulation [17] and it was shown to be relevant for auralization [18]. 

> © M. Pezzoli, R. Malvermi, F. Antonacci and A. Sarti. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: M. Pezzoli, R. Malvermi, F. Antonacci and A. Sarti, “Similarity evaluation of violin directivity patterns for musical instrument retrieval ”, in Proc. of the 24th Int. Society for Music Information Retrieval Conf., Milan, Italy, 2023. 

In [19], the authors demonstrated that users are able to perceive differences between omnidirectional and directional sound sources, however the evaluation is limited to a single-tone dependent directivity pattern. In the work [20], it was shown that fluctuations occurring in the directivity patterns due to the movements of the musician influence the perception of listeners both in anechoic and reverberant conditions. More recently, in [21], the difference between frequency-dependent directivities and an average directivity pattern has been investigated proving the importance of modelling specific frequency-dependent directivities by means of listening tests. 

Several studies [22–26] focus on the analysis of voice directivity patterns. In particular, [23,25] analyze the patterns associated to held or isolated vowels and consonants from speech and singing voice [24]. Interestingly, the results on mouth and vocal tract configurations [26] showed their impact on the directivity pattern shape. 

As far as the musical instruments are concerned, most of the works put the emphasis on accurate measurement procedures. Typically, the directional sound pressure is acquired in anechoic environments and under controlled conditions [6, 7]. Alternatively, near-field acoustic holography [27,28] has been employed for the evaluation of the directional sound radiation using scanning microphone arrays [29]. More recently, a flexible procedure for measuring the directivity pattern of sound sources that works in low-reverberant environments was introduced in [8]. 

In [9], the directivity patterns of forty one orchestral instruments have been acquired and analyzed. The instruments were played by musicians, rather than mechanically excited, showing that the presence of the player body has the effect of smoothing the patterns. Nevertheless, although [9] draws an interesting analysis of the patterns, the evaluation is mainly limited to graphical inspection without a systematic comparison of the directivity patterns. 

As a matter of fact, the quantitative and objective comparison of directivity patterns is still an open challenge. In the literature, some simple metrics have been proposed [30–33]. Although effective, the interpretation of the results and the quantification of the differences might not be easily interpreted. In general, most of the proposed metrics rely on the correlation between the directivity patterns, either in the spherical harmonics domain [30] or in the spatial domain [32]. In [30], the authors employed the normalized cross correlation (NCC) over the spherical harmonics coefficients of the directivity patterns. The anal- 

138 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

ysis assessed similarities of partials at a given frequency generated by different played pitches. In [34], a rotationinvariant version of the NCC has been proposed to compare the directivity patterns of the data sets in [9,35], which have been made available through [36]. The devised metric has been used to find similarities across the partials of one instrument or between different instruments and a visualization of the corpus through MultiDimensional Scaling (MDS) [37] has been provided. 

More recently, in [38], a novel set of metrics has been introduced, which includes the Jaccard similarity index (JSI) and the centers of mass distance (CMD) in addition to NCC. Both JSI and CMD are derived from the analysis of the so-called principal radiation regions, namely angular regions of the directivity pattern which exhibit the highest sound energy radiation. In [38], the metrics are used for the characterization of directivity patterns of prestigious historical violins enabling the quantitative comparison of the instruments. Nonetheless, the analysis is limited to a small set of 10 instruments and the conclusions drawn by the analysis of each metric, although relevant, are not readily combined. 

In this work, we aim to exploit available similarity metrics for directivity patterns in a comprehensive and systematic fashion. Considering the problem of musical instrument retrieval based on the directivity pattern features [34,39], we introduce novel distances, namely the Jaccard similarity distance (JSD) based on JSI, and the directivity index distance (DID) derived from the so-called directivity index (DI), which are combined with the CMD in a cumulative Directivity Pattern Distance (DPD). The proposed distances are blind with respect to the source type, because they work directly on the directivity values. Therefore, ideally they can be applied on any kind of sound sources, including musical instruments of different families. The joint adoption of multiple distances allows us to take into account different aspects of the directivity patterns without limiting the comparison to a single metric. Moreover, the introduced DPD provides a single-valued solution that represents the distance between the directivity patterns combining the information provided by each considered metric. 

Although the proposed distances can be applied on different musical instruments, we tested them on a data set of violin directivities. As a matter of fact, violins represent an interesting case study due to the highly variability of directivity patterns among the instruments [40,41]. The corpus contains a total of 18 instruments equally divided between 10 historical and 8 modern high-quality violins. To the best of our knowledge, this is the largest data set of violin directivity patterns evaluated in the current literature. The analysis allowed us to observe interesting similarities among the instruments, identifying relevant information in the data set. In particular, modern instruments are relatively distant from the historical ones. Moreover, thanks to the adoption of DPD, we could identify clusters of historical instruments made by one violin maker and two modern “twin” violin. Similarly to [34], we exploit the MDS tech- 



<!-- Start of picture text -->
180° f0°<br>D ( ϕ ,  θ ,  ω )<br>30 ∘<br>60 ∘<br>θ 90 ∘ × [dB] -90° 90° 90°<br>120 ∘<br>150 ∘<br>−180 ∘ 90 ∘ 0 ∘ −90 ∘ 180 ∘<br>ϕ 180*<br><!-- End of picture text -->

Figure 1. Example of directivity pattern D(φ, θ, ω) of a Genelec 8030A at 1.4 kHz, taken from [43]. The principal radiation region P is delimited by a solid black line, while the center of mass r is marked by a black cross. The reference system is reported from top and frontal views. 

nique for the visualization of the data set, which allows us to graphically assess the distances between the instruments observing the clusters of similar violins within. The obtained results pave the way to the retrieval of musical instruments according to their directional sound radiation and open novel perspectives for the exploitation of directivity pattern databases. 

## 2. SIMILARITY METRICS FOR DIRECTIVITY PATTERNS 

Let us define the directivity pattern of an acoustic source as the square-integrable function D(·) ∈ L<sup>2</sup> (S<sup>2</sup> ) describing the energy of the directional sound radiation. The directivity pattern is thus defined over a unit sphere comprising all the possible directions of emission. It follows that the directivity pattern can be conveniently expressed through the widely adopted spherical harmonics expansion [5,8,13] as 



<!-- Start of picture text -->
N n<br>D(φ, θ, ω) = Cn m(ω)Y n m(φ, θ), (1)<br>∑∑ n=0 m=−n<br><!-- End of picture text -->

where φ ∈ [0, 2π] and θ ∈ [0, π] are the azimuth and inclination angles, respectively, Cn<sup>m(ω)arethespherical</sup> harmonics coefficients associated with the source directivity pattern and Yn<sup>m(φ, θ)isthesphericalharmonicofde-</sup> gree n and order m [42]. It is worth noting that the directivity pattern (1) depends on the temporal frequency ω. Moreover, in (1), we assumed the directivity pattern to be band-limited being N the maximum expansion order. In Fig. 1, an example of a loudspeaker directivity pattern is reported. 

## 2.1 Data model 

## 2.1.1 Binary directivity pattern 

In [38], the principal radiation region of a directivity pattern is defined as the set of adjacent directions P that correspond to the maximum acoustic energy emission. In particular, given a threshold value τ , the principal radiation region is defined as 



<!-- Start of picture text -->
P(ω) = (φ ¯ p, θ ¯ p) : DdB(φ ¯ p, θ ¯ p, ω) ≥ τ J , (2)<br> τ = −3 dB and −3 dB and3 dB and and<br>D (φ,  θ ,  ω )<br>DdB(φ, θ, ω) = 10 log10 (3)<br>max(D(φ, θ, ω))<br><!-- End of picture text -->

where τ = −3 dB and −3 dB and3 dB and and 

represents the normalized directivity pattern in decibel scale with max the function extracting its maximum value. 

139 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

In Fig. 1, the principal radiation region P is delimited by a solid black line. 

The thresholding procedure in (2) allows one to define the binary directivity pattern indicating the principal radiation region as 



<!-- Start of picture text -->
(φ, θ) ∈P(ω)<br>D¯ (φ, θ, ω) = . (4)<br>0 otherwise<br>� 1<br><!-- End of picture text -->

overlap. In order to interpret the JSI in terms of a distance, we introduce the JSD metric as 



<!-- Start of picture text -->
JSDk,j(ω) = 1 − JSIk,j(ω), (8)<br><!-- End of picture text -->

so that the JSD decreases up to 0 when two principal radiation regions are matched and the maximum value of JSD is 1, indicating two completely disjoint regions. 

## 2.2.2 Center of Mass Distance (CMD) 

The adoption of the binary patterns is preferable rather than considering only the direction of the maximum, i.e. a single point, in the directivity pattern. As a matter of fact, the binary pattern indicates the regions of high energy emission, i.e. principal radiation, which can have arbitrary shape and extension accordingly to the overall directional characteristics of the directivity pattern. 

## 2.1.2 Centers of mass 

Although the binary pattern (4) provides a comprehensive representation of the principal radiation regions, it is convenient to further identify a “preferred” direction of emission for each region. Therefore, we define the center of mass for a principal radiation region P as [38] 



<!-- Start of picture text -->
r(ω) = M 1 � mprp, (5)<br>p∈P(ω)<br><!-- End of picture text -->

where rp = �sin θ<sup>¯</sup> p cos φ<sup>¯</sup> p, sin θ<sup>¯</sup> p sin φ<sup>¯</sup> p, cos θ<sup>¯</sup> p�T are the points belonging to the set defined in (2). In practice, the directions of P are weighted using the corresponding energy value in the normalized pattern, namely 



<!-- Start of picture text -->
mp = D (φ ¯ p,  ¯θ p,  ω ) with M = � mp. (6)<br>max(D(·, ω)) ,<br>p∈P(ω)<br><!-- End of picture text -->

The center of mass of the directivity pattern is marked in Fig. 1 by a black cross. 

## 2.2 Distance Metrics 

In order to compare the directivity patterns of acoustic sources within a data set, we rely on a set of metrics recently proposed in [38]. Differently from customarily directivity pattern comparisons, where a single metric is considered, the employment of multiple metrics allows us to take into account different characteristics that are captured by each metric. 

## 2.2.1 Jaccard Similarity Distance (JSD) 

According to [38], we define the Jaccard similarity index (JSI) between two binary directivity patterns as 



<!-- Start of picture text -->
JSIk,j(ω) = |  ¯Dk ( ω )  ∩ D¯ j( ω )| (7)<br>|D ¯ k(ω) ∪ D ¯ j(ω)| ,<br><!-- End of picture text -->

where ∩ is the intersection operator and ∪ is the union between the binary patterns of the kth and jth sources. From the definition in (7), it follows that JSIk,j(ω) = 1 when two binary patterns match exactly, while JSIk,j(ω) = 0 when the corresponding principal radiation regions do not 

The CMD is defined in order to compute the distance between two centers of mass as [38] 



<!-- Start of picture text -->
CMDk,j(ω) = arctan , (9)<br>� | rrkk ( (ωω ) ) × · r rj j ( ( ωω) )| �<br><!-- End of picture text -->

where × and · denote the vectorial cross and dot products, respectively. As in [33], when multiple centers of mass are present inside the directivity patterns, the vectors r (5) are selected in order to retain the lowest CMDk,j(ω) values. 

## 2.2.3 Directivity Index Distance (DID) 

The directivity index (DI) is a well-known feature that describes the directionality of a sound source [33]. In particular, the DI measures how much energy is concentrated around the principal directions of a directivity pattern. In this work, we consider the DI of the normalized directivity patterns defined as 



<!-- Start of picture text -->
1<br>DIk(ω) = , (10)<br>� 02π � 0π D�k(φ, θ, ω)dφdθ<br><!-- End of picture text -->

where D<sup>�</sup> k is the normalized directivity pattern of the kth source in linear scale. The DI in (10) is computed with respect to the maximum value of the directivity pattern, which in case of normalized patterns is equal to 1. It follows that high DI values occur for directivity patterns with large principal radiation regions, and vice versa. 

In order to compare two directivity patterns in terms of their DI values, we define the DID as 



<!-- Start of picture text -->
DIDk,j(ω) = � (DIj(ω) − DIk(ω)) 2 , (11)<br><!-- End of picture text -->

where DIk and DIj are the DI (10) of the kth and jth sources, respectively. 

## 2.2.4 Directivity Pattern Distance (DPD) 

In order to conveniently compare two sound sources in terms of their directivity features, we introduce an overall metric that combines the previously defined JSD, CMD and DID into a scalar value. Hence, we define the so-called directivity pattern distance DPD metric as 



<!-- Start of picture text -->
CMDk ,j DIDk ,j<br>DPDk,j = JSDk,j +<br>max(CMDk,j) + max(DIDk,j) , (12)<br><!-- End of picture text -->

where JSDk,j, CMDk,j, DIDk,j denote the mean of the three distance metrics over the frequenc <mark>y</mark> axis. It must be noted that the values of CMDk,j and DIDk,j in (12) are normalized with respect to the maximum value encountered in the data set under analysis, such that all the components of the sum vary within the same dynamic range, i.e. between 0 and 1, and thus have the same relative importance in the definition of DPD. 

140 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

## 3. EVALUATION 

## 3.1 Data set of violin directivity patterns 

The proposed methodology is applied to a data set of violin directivities. The data set includes the frequencydependent directivity patterns of eighteen violins, including ten historical violins made between the 16th and 17th centuries and eight modern violins made during the last two centuries. For all the instruments, the owners provided consent for the usage of the results in an anonymous fashion. For this reason, and for the ease of reading, we will denote all the historical violins with labels H1–H10, while we will refer to the modern ones as M1–M8. 

Concerning the collection of modern violins, it is noteworthy that the instruments labeled with M1–M6 are fine violins selected among the candidates of the “Antonio Stradivari International Triennial Competitions of Stringed instrument making”. The competition, held in the city of Cremona since 1976, embraces both Cremonese and international competitors. Moreover, violins M7 and M8 were made by a Cremonese luthier and are known as “twin violins”. The twin violins were built by employing the very same block of tonewood and following the same geometrical model. As a matter of fact, previous research already showed the high similarity in all the spatial characteristics of their sound. 

The patterns were collected experimentally through the measurement procedure described in [8] and were evaluated at varying frequency within the range [200, 5000] Hz using a 4th-order spherical harmonics expansion in (1). The instruments are played by one professional violinist who is free to move and play comfortably, while the source position and orientation are estimated by the system enabling the measurement of the directivity as described in [8]. The data processing pipeline and the computation of the metrics is developed using the MATLAB software. 

## 3.2 Analysis of the metrics 

To assess the significance of the proposed distance metrics, we first com <mark>p</mark> are the frequency-averaged values of JSD, CMD and DID computed over the set of violin directivity patterns to those obtained for the same data with a commonly used similarity metric, namely NCC. The NCC metric provides a measure of the element-wise similarity between two patterns. In order to properly compare the previously defined distances with the baseline, the NCC between the patterns of the k-th and l-th violins is formalized in terms of a distance as 



<!-- Start of picture text -->
S D�k (φ,  θ ,  ωs )  �Dl (φ,  θ ,  ωs )<br>NCCk,l = 1 − S 1 � s=1 ∥D � k(φ, θ, ωs)∥∥D � l(φ, θ, ωs)∥ , (13)<br><!-- End of picture text -->

where ωs is the s-th frequency at which the directivity patterns are evaluated, with s = 1, . . . , S and S the total number of frequency bins in the data set. In this way, NCCk,l is close to zero when two patterns are similar and reaches a value equal to 2 when they are inversely correlated. Fig. 2 shows a comparison between all the metrics under study. For any possible pair of metrics, a 2D scatter plot is 



<!-- Start of picture text -->
(a) (b) (c)<br>(d) (e) (f)<br><!-- End of picture text -->

Figure 2. Com <mark>p</mark> arison between proposed distance metrics <mark>(</mark> JSD, CMD, DID) and Normalized Cross Correlation (NCC). For each combination of metrics, a 2D scatter plot of the corresponding frequency-averaged values is shown. Z-score normalization is applied to ensure the same dynamic range along the axes [44]. Linear regression is performed to analyze the correlation between the metrics. The regressed line and the R<sup>2</sup> value, measuring the degree of correlation, are highlighted in red. 

reported. The coordinates of the markers in the plot correspond to the two distances for all the possible pairs of violins in the data set. Z-score normalization is applied to the resulting values to ensure the same dynamic range along the axes [44]. The scatter <mark>p</mark> lots in the first row show the comparison between NCC (13) and each of the proposed metrics, while the scatter <mark>p</mark> lots in the second row present the comparison between JSD, CMD and DID only. By inspecting the resulting distributions of points, it is possible to highlight correlations between the metrics. 

On the one hand, it can be noticed that some pairs of metrics exhibit a point distribution that concentrates along a line. A linear trend, in fact, can be observed in Fig. 2a and 2b, showing the (NCC, JSD) and (NCC, CMD) point distributions, respectively. Although less emphasized, a similar trend can be noticed in Fi <mark>g</mark> . 2d and 2e, reporting the distribution of (JSD, CMD) and (JSD, DID), respectively. 

The presence of linearity in these point distributions can be interpreted as due to correlation, i.e. shared information, between the metrics under analysis. This can be particularly true for NCC and JSD, which both measure the degree of pattern matching by definition. More interestingly, however, correlation can be observed between CMD and NCC. We can thus conclude that two violins with similar principal directions of radiation tend to exhibit hi <mark>g</mark> hl <mark>y</mark> matching directivity patterns. Furthermore, JSD and CMD can be used instead of NCC to provide two similarity measures by looking at the pattern shape and at the principal direction of radiation separatel <mark>y</mark> without losing information. Indeed, Fig. 2d shows that JSD and CMD are less correlated than when considering NCC. 

On the other hand, Fig. 2c and Fig. 2e do not exhibit a linear distribution. We can inter <mark>p</mark> ret this evidence as the absence of correlation between DID, NCC and CMD. As a matter of fact, DID measures the difference in the directivity index of two patterns, which is related to the energy distribution, and thus extracts an energy-related informa- 

141 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 





<!-- Start of picture text -->
(a) (b) (c)<br><!-- End of picture text -->

Figure 3. Evaluation of violin similarity based on JSD (a), CMD (b) and DID (c). The elements inside the matrices are obtained by averaging the frequency-dependent distance values. Pairs of similar violins are denoted with dark blue colors, while dissimilar violins are highlighted in yellow. Hierarchical clustering algorithms are employed to sort the elements inside the resulting matrices. The resulting dendrograms are reported above each distance matrix. 

tion that is not captured by the other metrics. 

A quantitative measure of the correlation between the metrics under analysis can be evaluated by performing linear regression on each point distribution. The regressed lines are denoted in red inside each 2D scatter plot. The regression accuracy is assessed in terms of the coefficient of determination R<sup>2</sup> , which is related to the Pearson correlation coefficient in the case of simple linear regression. The resulting R<sup>2</sup> values are reported as an inset inside each plot. According to [45], the values range between 0 and 1, and moderate and strong correlation occurs for values greater than 0.3 and 0.6, respectively. 

It can be noticed that the pair (NCC, JSD) shows moderate to strong correlation, with R<sup>2</sup> = 0.57. Moderate correlations can be observed for (NCC, CMD), (JSD, CMD) and (JSD, DID), with R<sup>2</sup> = 0.42, R<sup>2</sup> = 0.33 and R<sup>2</sup> = 0.38, respectivel <mark>y</mark> . Finall <mark>y</mark> , no correlation occurs for (NCC, DID) and (CMD, DID), with R<sup>2</sup> = 0.09 and R<sup>2</sup> = 0.03, respectively. 

3.3 Violins clustering based on similarity metrics 

In order to group musical instruments that exhibit a sound emission with similar spatial characteristics, the proposed distance metrics can be used together with classical clustering methods. In this case, hierarchical clustering methods are employed, based on the generation of dendrograms [46]. In particular, the proposed similarity metrics are used for the iterative definition of the dendrogram. It is worth to underline, that the adopted clustering algorithm does not require any training data and it is applied directly on the computed similarities. Fig. 3 shows the distance matrices assessing the pairwise similarity between all the violins in the data set under study. The matrix elements in Fi <mark>g</mark> . 3a, 3b and 3c are obtained using the frequency-averaged JSD, 

CMD and DID values, respectively. Pairs of similar violins are highlighted with dark blue colors, while dissimilar violins are colored in yellow. The elements of each distance matrix are sorted according to the leaf order of a dendrogram tree. The Ward’s method [47] is used to generate the tree branches, such that similar violins concentrate inside the matrix. 

By inspecting the resulting distance matrices, it is noteworthy that the order of the elements in the matrix varies depending on the specific distance considered. However, expected groups of violins can be highlighted. In Fig. 3a, the subsets of historical and modern violins are clearly distinguished, bein <mark>g p</mark> laced at the top-left and bottom-right corners of the JSD matrix, respectively. In particular, the twin violins (M7-M8) exhibit the minimum JSD value in the matrix and the remaining modern violins (M1-M6) cluster together. The same behavior occurs also in Fig. 3b and 3c, although at different locations inside the matrices. 

Regarding the historical violins, H1 appears to be very different with respect to the rest of the data set. In <mark>p</mark> articular, high values are encountered for JSD and DID, which are related to the pattern shape and energy, respectively. Conversely, the same violin is more similar to other historical violins concerning the principal directions of radiation. 

Fig. 4 shows the results of violin clustering based on the proposed overall metric DPD. On the left, the dendrogram computed with the Ward’s method is shown, while on the right the resulting distance matrix is reported, with the elements sorted following the dendrogram hierarchy. Pairs of violins characterized by DPD values close to either zero or the maximum are colored in green or white, repsectively. 

Typically, clusters can be extracted from the hierarchy of the dendrogram tree by applying a thresholding with re- 

142 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 



Figure 4. Violin clustering based on the proposed DPD metric. Small distance values correspond to pairs of similar violins and are highlighted in green, while pairs of dissimilar violins exhibit high distance values and are highlighted in white. The elements inside the matrix are sorted according to the dendrogram tree, shown on the left. Clustering is performed by thresholding the dendrogram tree. The threshold is denoted with a cyan line, while the resulting clusters are colored in red. 

spect to the tree height. We decide to subdivide the dendrogram at a height equal to 1.9, i.e. the mean value between the height of the lowest branch in the tree and the height of its root, denoted with a vertical dashed cyan line. As a result, seven clusters are identified inside the data set: (i) three consisting of a single violin (i.e. H1, H10 and H3), (ii) one cluster made of five historical violins (i.e. H4-H6H7-H8-H9), (iii) one cluster made of two historical violins and the twin violins (i.e. H2-H5-M7-M8), (iv) one cluster with four modern violins (i.e. M3-M4-M5-M6) and (v) one cluster with two modern violins (i.e. M1-M2). 

The obtained clusters are coherent with the similarities extracted from the single proposed metrics. In particular, the distinction between historical and modern violins and the high similarity between the twin violins (M7-M8) are emphasized by the DPD. Moreover, hierarchical clustering based on DPD is able to recognize a cluster with five historical violins i.e. H4-H9-H6-H8-H7. Remarkably, the instruments belonging to this cluster have been made by the same luthier. 

## 3.3.1 Visualization of the data collection through MDS 

Given the similarity analysis of the violin directivity patterns based on the proposed DPD metric, the employment of MultiDimensional Scaling methods (MDS) allows one to easily visualize and navigate the collection of data [37]. In practice, MDS methods enable the mapping of the violins into a multidimensional space so that the similarities between the musical instruments in the data set are preserved. 

Fig. 5 shows a 3D representation of the data set based on MDS. In this case, the coordinate system results from the use of Nonclassical MDS with the distance matrix shown in Fig. 4 as input. Each marker in the scatter plot corresponds to a violin, and the same marker color is used to denote violins belonging to the same cluster. 

## 4. CONCLUSION 

In this paper, we tackle the problem of directivity patterns comparison by introducing a novel distance metric denoted 



Figure 5. 3D representation of the violin data set based on Multidimensional Scaling. Nonclassical MDS is applied on the resulting DPD matrix to map the violins into a three-dimensional space. Each marker in the scatter plot corresponds to a violin. The same marker color is used for violins belonging to the same cluster. 

as DPD, which is based on a combination of different similarity metrics and features of the patterns. This approach allows one to compactly compare the similarity of directivity patterns exploiting the different information provided by JSD, CMD and DID. The considered metrics are compared within each other and with respect to the well-known NCC, highlighting that they provide mutually uncorrelated information. 

We analyzed a data set of directivity patterns of 18 violins divided between 10 historical and 8 modern instruments. Through the use of DPD, we were able to identify clusters of similar instruments among which a set of historical instruments made by the same maker and two “twin” violins. Finally, the MDS technique enabled the visualization of the violin data collection starting from the computed distances. 

We foresee the application of the proposed approach for the retrieval of musical instruments based on directivity pattern characteristics. This opens new perspectives for the navigation of data sets of directivity patterns which can be used to provide a more realistic acoustic presence of musical instruments within spatial audio applications. 

143 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

   5. REFERENCES 

- [1] H. F. Olson, Music, physics and engineering. Courier Corporation, 1967, vol. 1769. 

- [2] J. Meyer, “Directivity of the bowed stringed instruments and its effect on orchestral sound in concert halls,” The Journal of the Acoustical Society of America, vol. 51, no. 6B, pp. 1994–2009, 1972. 

- [3] ——, Acoustics and the performance of music: Manual for acousticians, audio engineers, musicians, architects and musical instrument makers. Springer Science & Business Media, 2009. 

- [4] ——, “The influence of the directivity of musical instruments on the efficiency of reflecting or absorbing areas in proximity to the orchestra,” Acta Acustica united with Acustica, vol. 36, no. 3, pp. 147–161, 1976. 

- [5] G. Weinreich and E. B. Arnold, “Method for measuring acoustic radiation fields,” The Journal of the Acoustical Society of America, vol. 68, no. 2, pp. 404–411, 1980. 

- [6] J. Pätynen, V. Pulkki, and T. Lokki, “Anechoic recording system for symphony orchestra,” Acta Acustica united with Acustica, vol. 94, no. 6, pp. 856–865, 2008. 

- [7] J. Curtin, “Measuring violin sound radiation using an impact hammer,” J. Violin Soc. Am. VSA Papers, XXII, no. 1, pp. 186–209, 2009. 

- [8] A. Canclini, F. Antonacci, S. Tubaro, and A. Sarti, “A methodology for the robust estimation of the radiation pattern of acoustic sources,” IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 28, pp. 211–224, 2020. 

- [9] N. R. Shabtai, G. Behler, M. Vorländer, and S. Weinzierl, “Generation and analysis of an acoustic radiation pattern database for forty-one musical instruments,” The Journal of the Acoustical Society of America, vol. 141, no. 2, pp. 1246–1256, 2017. 

- [10] F. Otondo and J. H. Rindel, “The influence of the directivity of musical instruments in a room,” Acta acustica united with Acustica, vol. 90, no. 6, pp. 1178–1184, 2004. 

- [11] J. Pätynen and T. Lokki, “Directivities of symphony orchestra instruments,” Acta Acustica united with Acustica, vol. 96, no. 1, pp. 138–167, 2010. 

- [12] J. G. Tylka and E. Y. Choueiri, “Fundamentals of a parametric method for virtual navigation within an array of ambisonics microphones,” Journal of the Audio Engineering Society, vol. 68, no. 3, pp. 120–137, 2020. 

- [13] M. Pezzoli, F. Borra, F. Antonacci, A. Sarti, and S. Tubaro, “Reconstruction of the virtual microphone signal based on the distributed ray space transform,” in 26th European Signal Processing Conference (EUSIPCO). IEEE, 2018, pp. 1537–1541. 

- [14] M. Pezzoli, F. Borra, F. Antonacci, S. Tubaro, and A. Sarti, “A parametric approach to virtual miking for sources of arbitrary directivity,” IEEE Trans. on audio, speech, and language Process., vol. 28, pp. 2333– 2348, 2020. 

- [15] R. Mehra, L. Antani, S. Kim, and D. Manocha, “Source and listener directivity for interactive wavebased sound propagation,” IEEE transactions on visualization and computer graphics, vol. 20, no. 4, pp. 495–503, 2014. 

- [16] J. Ahrens and S. Bilbao, “Computation of spherical harmonic representations of source directivity based on the finite-distance signature,” IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 29, pp. 83–92, 2021. [Online]. Available: https://ieeexplore.ieee.org/document/9257177/ 

- [17] J. Klein and M. Vorländer, “Simulative investigation of required spatial source resolution in directional room impulse response measurements,” in EAA Spatial Audio Signal Processing Symposium, 2019, pp. 37–42. 

- [18] B. N. Postma, H. Demontis, and B. F. Katz, “Subjective evaluation of dynamic voice directivity for auralizations,” Acta Acustica united with Acustica, vol. 103, no. 2, pp. 181–184, 2017. 

- [19] L. M. Wang and M. C. Vigeant, “Evaluations of output from room acoustic computer modeling and auralization due to different sound source directionalities,” Applied Acoustics, vol. 69, no. 12, pp. 1281–1293, 2008. 

- [20] D. Ackermann, C. Böhm, F. Brinkmann, and S. Weinzierl, “The acoustical effect of musicians’ movements during musical performances,” Acta Acustica united with Acustica, vol. 105, no. 2, pp. 356–367, 2019. 

- [21] A. Corcuera Marruffo and V. Chatziioannou, “A pilot study on tone-dependent directivity patterns of musical instruments,” in Audio Engineering Society Conference: AES 2022 International Audio for Virtual and Augmented Reality Conference. Audio Engineering Society, 2022. 

- [22] C. Noufi, D. Markovic, and P. Dodds, “Reconstructing the dynamic directivity of unconstrained speech,” arXiv preprint arXiv:2209.04473, 2022. 

- [23] B. F. Katz, F. Prezat, and C. d’Alessandro, “Human voice phoneme directivity pattern measurements,” in 4th Joint Meeting of the Acoustical Society of America and the Acoustical Society of Japan, 2006, p. 3359. 

- [24] B. Katz and C. d’Alessandro, “Directivity measurements of the singing voice,” in International Congress on Acoustics (ICA 2007), 2007, p. 6p. 

- [25] P. Kocon and B. B. Monson, “Horizontal directivity patterns differ between vowels extracted from running speech,” The Journal of the Acoustical Society of America, vol. 144, no. 1, pp. EL7–EL12, 2018. 

144 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

- [26] S. Bellows and T. Leishman, “High-resolution analysis of the directivity factor and directivity index functions of human speech,” in Audio Engineering Society Convention 146. Audio Engineering Society, 2019. 

- [27] J. D. Maynard, E. G. Williams, and Y. Lee, “Nearfield acoustic holography: I. theory of generalized holography and the development of NAH,” The Journal of the Acoustical Society of America, vol. 78, no. 4, pp. 1395–1413, 1985. 

- [28] M. Olivieri, M. Pezzoli, F. Antonacci, and A. Sarti, “A physics-informed neural network approach for nearfield acoustic holography,” Sensors, vol. 21, no. 23, 2021. [Online]. Available: https://www.mdpi. com/1424-8220/21/23/7834 

- [29] D. Fernandez Comesana, T. Takeuchi, S. Morales Cervera, and K. R. Holland, “Measuring musical instruments directivity patterns with scanning techniques,” in 25th International Congress on Sound and Vibration, ICSV 2019, 2019. 

- [30] F. Hohl and F. Zotter, “Similarity of musical instrument radiation-patterns in pitch and partial,” Fortschritte der Akustik, DAGA, Berlin, 2010. 

- [31] P. Guillon, R. Nicol, and L. Simon, “Head-related transfer functions reconstruction from sparse measurements considering a priori knowledge from database analysis: A pattern recognition approach,” in Audio Engineering Society Convention 125. Audio Engineering Society, 2008. 

- [32] S. Moreau, J. Daniel, and S. Bertet, “3d sound field recording with higher order ambisonics–objective measurements and validation of a 4th order spherical microphone,” in 120th Convention of the AES, 2006, pp. 20–23. 

- [33] C. Molloy, “Calculation of the directivity index for various types of radiators,” The Journal of the Acoustical Society of America, vol. 20, no. 4, pp. 387–405, 1948. 

- [34] T. Carpentier and A. Einbond, “Spherical correlation as a similarity measure for 3d radiation patterns of musical instruments,” in 16ème Congrès Français d’Acoustique. HAL Open Science, 2022. 

   - [38] M. Pezzoli, A. Canclini, F. Antonacci, and A. Sarti, “A comparative analysis of the directional sound radiation of historical violins,” The Journal of the Acoustical Society of America, vol. 152, no. 1, pp. 354–367, 2022. 

   - [39] M. Olivieri, R. Malvermi, M. Pezzoli, M. Zanoni, S. Gonzalez, F. Antonacci, and A. Sarti, “Audio information retrieval and musical acoustics,” IEEE Instrum. Meas. Mag., vol. 24, no. 7, pp. 10–20, 2021. 

   - [40] G. Weinreich, “Directional tone color,” The Journal of the Acoustical Society of America, vol. 101, no. 4, pp. 2338–2346, 1997. 

   - [41] J. Woodhouse, “The acoustics of the violin: a review,” Reports on Progress in Physics, vol. 77, no. 11, p. 115901, 2014. 

   - [42] A. Schmitz, T. Karolski, and L. Kobbelt, “Using spherical harmonics for modeling antenna patterns,” in 2012 IEEE Radio and Wireless Symposium. IEEE, 2012, pp. 155–158. 

   - [43] J. G. Tylka, R. Sridhar, and E. Choueiri, “A database of loudspeaker polar radiation measurements,” in Audio Engineering Society Convention 139. Audio Engineering Society, 2015. 

   - [44] A. Jain, K. Nandakumar, and A. Ross, “Score normalization in multimodal biometric system,” Pattern Recognition, vol. 38, pp. 2270–2285, 12 2005. 

   - [45] J. Cohen, Statistical power analysis for the behavioral sciences. Routledge, 2013. 

   - [46] G. Gruvaeus and H. Wainer, “Two additions to hierarchical cluster analysis,” British Journal of Mathematical and Statistical Psychology, vol. 25, no. 2, pp. 200– 206, 1972. 

   - [47] S. Sharma, N. Batra et al., “Comparative study of single linkage, complete linkage, and ward method of agglomerative clustering,” in 2019 International Conference on Machine Learning, Big Data, Cloud and Parallel Computing (COMITCon). IEEE, 2019, pp. 568– 573. 

- [35] S. Weinzierl, M. Vorländer, G. Behler, F. Brinkmann, H. von Coler, E. Detzner, J. Krämer, A. Lindau, M. Pollow, F. Schulz et al., “A database of anechoic microphone array measurements of musical instruments,” 2017. 

- [36] J. Ahrens, “Database of spherical harmonic representations of sound source directivities,” https://doi.org/10. 5281/zenodo.3707708, Mar 2020. 

- [37] N. Saeed, H. Nam, M. I. U. Haq, and D. B. Muhammad Saqib, “A survey on multidimensional scaling,” ACM Computing Surveys (CSUR), vol. 51, no. 3, pp. 1–25, 2018. 

145 

