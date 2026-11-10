---
paper_id: "000023"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706370/files/000023.pdf"
---

# PHYLO-ANALYSIS OF FOLK TRADITIONS: A METHODOLOGY FOR THE HIERARCHICAL MUSICAL SIMILARITY ANALYSIS 

Hilda Romero-Velo<sup>1</sup> 

Gilberto Bernardes<sup>2</sup> Susana Ladra<sup>1</sup> 

José R. Paramá<sup>1</sup> Fernando Silva-Coira<sup>1</sup> 

1 Universidade da Coruña, CITIC, Database Laboratory, Spain 

2 INESC TEC, Faculty of Engineering, University of Porto, Portugal 

> 1 `{h.rvelo, susana.ladra, jose.parama, fernando.silva}@udc.es,` 2 `gba@fe.up.pt` 

## ABSTRACT 

This study introduces and evaluates a new methodology for cross-cultural ethnomusicological analysis of symbolic music. We investigate music similarity in popular traditions rooted in oral transmission by identifying shared patterns at scale across multiple hierarchies. The novelty of our approach lies in expanding musical similarity phyloanalysis-typically adopting alignment metrics that compare entire scores-to structurally aware phrases and macrostructure (i.e., form) alignment. Additionally, we explore patterns derived from multiple representations (chromatic interval, diatonic interval, rhythmic ratios, and a combination of them) to facilitate the exploration of stylistic affinities across musical genres and traditions. Our method is tested on a new dataset of 600 Galician and Irish popular music scores, which includes expert annotations for 21 genres (four shared between the two traditions) and detailed phrase information, all made available as openaccess data. We use the genre separation ratio to examine how alignment strategies capture stylistic structure, providing insights that support musicological exploration across genres and traditions. The resulting phylogenetic trees and distance matrices reveal relationships among traditions, genres, and scores, facilitating the exploration of cross-cultural influences and enabling the identification of shared patterns at multiple hierarchies. 

## 1. INTRODUCTION 

The ethnomusicological studies of popular music rooted in oral transmission across cultures, hereafter referred to as folk music, have increasingly relied on large-scale data analysis to uncover deep structural patterns and evolutionary processes. As musical traditions intersect and evolve over time, researchers face the challenge of transcribing, assembling and processing vast and complex music 

> © H. Romero-Velo, G. Bernardes, S. Ladra, J. R. Paramá and F. Silva-Coira. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: H. Romero-Velo, G. Bernardes, S. Ladra, J. R. Paramá and F. Silva-Coira, “Phylo-Analysis of Folk Traditions: A Methodology for the Hierarchical Musical Similarity Analysis”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

datasets. This need has led to the adoption of computational methods from disciplines like biology, where phylogenetic techniques—originally designed for tracing genetic evolution—are now being used to explore how musical traits are transmitted and transformed across cultures. These methods have been applied to a wide range of musical phenomena, from identifying melodic patterns [1, 2] to studying musical transmission in oral traditions [3]. Additionally, phylogenetic trees have been used to trace the evolution of polyphony from the Baroque to Romantic periods [4] and to analyze plainchant melodies [5]. While some studies focus on rhythmic analysis [6], none have yet examined musical form hierarchically, treating structure and shared patterns across levels as evolving entities. 

Identifying musical patterns and inferring form are key challenges in analysing music from different traditions. Volk et al. [7, 8] argue that experts reliably recognize shared melodic patterns as indicators of folk music families. Building on this idea, we propose a methodology for analysing large score collections based on shared patterns across multiple musical hierarchies. Our approach extends prior work on musical similarity [9–12] by applying alignment metrics from bioinformatics not only to pitch and rhythm but also to structural elements such as phrases and form. This strategy reduces spurious matches between songs that do not fulfill the same structural role. 

To support this hierarchical similarity analysis, we compiled a new dataset of 600 Galician and Irish songs, annotated at the phrase level by experts. These two traditions share deep historical ties through Celtic heritage [13, 14] and 20th-century cultural exchange [15], which introduced the use of the fiddle in traditional Galician music [16]. The rise of Celtic music festivals in the 1970s, such as Ortigueira and Lorient [17,18], further reinforced these connections. Still, to our knowledge, no prior study directly compares the shared genres between Ireland and Galicia. Thus, with this dataset, we explore whether our methodology can reveal shared structural patterns, while also highlighting the distinctive traits of each genre and tradition. 

Notably, our aim is to provide experts with an analytical tool for exploring large datasets of musical scores. To facilitate this endeavour, supplementary figures and diagrams are generated, including inferred genre tree representations. It should be stressed, however, that this is not a methodology for genre identification or classification. 

190 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
Select method to<br>Select encoding compare encoded scores<br>for input scores<br>Similarity Methods<br>Feature Encodings<br>Global<br>DIATONIC<br>CHROMATIC Shared<br>Scores<br>Phrases<br>RHYTHMIC<br>DIATONIC Combined<br>RHYTHMIC<br>CHROMATIC<br>RHYTHMIC Form<br><!-- End of picture text -->

Figure 1. Overview of the proposed methodology. Input scores are encoded according to a selected feature representation and compared pairwise through a similarity method, producing the corresponding distance matrix and phylogenetic tree. 

The paper is structured as follows: Section 2 introduces the annotated dataset; Section 3 details the methodology; Section 4 evaluates the proposed methods; Section 5 discusses a case study; and Section 6 outlines the conclusions. 

## 2. DATASET AND ANNOTATIONS 

We present a new annotated dataset of 600 music scores from Galician and Irish folk traditions, with a balanced distribution of 300 pieces per tradition. It features 21 genres, with 11 and 10 genres per Galician and Irish tradition, respectively. Four genres are shared between the two traditions: march (“marcha” in Galician), mazurka (“mazurca”), polka (“polca”) and waltz (“valse”). The remaining Galician genres are: “alalás”, “foliadas”, “jotas”, “muiñeiras”, “pasacorredoiras”, “pasodobles”, and “rumbas”. The Irish genres also include: “barndance”, “hornpipe”, “jig”, “reel”, “slide”, and “strathspey”. From each genre, 30 songs were selected, except for the Galician “mazurca” and “polca”, with 15 songs each. The dataset was sourced from the Folkoteca Galega<sup>1</sup> and The Session<sup>2</sup> . 

We parsed each score to avoid repetition and Da Capo instructions, thus expanding the musical surface to string sequences of musical events. Music experts annotated each musical piece, indicating phrase endings. In total, the dataset includes 5,844 phrases, of which 3,373 correspond to the Galician tradition and 2,471 to the Irish one. The expanded scores in **kern<sup>3</sup> and MusicXML formats and the phrase annotations are openly published<sup>4</sup> . 

## 3. METHODOLOGY 

This section proposes a methodology for studying the similarity between scores, genres, and traditions. The approach is inspired by bioinformatics, which uses alignment and clustering techniques to analyse the similarity of acid or 

> 1 `https://folkotecagalega.gal/pezas` , March 2025 2 `https://github.com/adactio/TheSession-data` , March 2025 

> 3 `https://www.humdrum.org/rep/kern/` , June 2025 4 `https://github.com/hromerovelo/folkroot` 



<!-- Start of picture text -->
CR: 11/2; 2,1/2; 1; -1,2;<br><!-- End of picture text -->

Figure 2. Sample of feature extraction from a score. 

protein chains. Furthermore, their phylogenetic trees embody the idea of tracing relationships between entities that share common roots, analogous to the study of our genres and cultures via the ‘music DNA’: pitches and rhythms. 

Figure 1 shows the methodology pipeline, highlighting its main modules and dataflow. It outlines the extraction of musical features from symbolic scores, the similarity methods used to compare them, and the construction of phylogenetic trees based on pairwise distances. 

## 3.1 Musical Features 

Considering the oral transmission of folk music, melodic contour, rhythm, and recurring motifs—identified by Volk and van Kranenburg [11] as key perceptual cues—provide a basis for its categorization into tune families. Following the framework proposed by Zhu et al. [19], each piece of music is defined by three features: the diatonic interval (D), the chromatic interval (C), and the rhythmic ratio (R). Using these features, a piece of music can be defined independently of its key and time signature or tempo, as a duration relation is calculated. This approach is particularly advantageous within the folk music context, where numerous pieces are recompiled for different instruments with varying tunes and rhythmic annotations. 

The diatonic interval (D) refers to the direction and number of steps to the next note in the diatonic scale— for example, B to C yields a value of 2 (see Figure 2). The chromatic interval (C) measures the number of semitones between consecutive notes (1 in our previous example). Unison is represented by 1 in the diatonic interval and by 0 in the chromatic interval (no semitone difference). However, unisons are removed during feature extraction, as they do not reflect melodic progression. Negative values indicate descending motion in both features. Together, these representations offer complementary, transpositioninvariant views of pitch, enabling a comparative exploration of melodic content across traditions—diatonic intervals capture stepwise tonal structure, while chromatic intervals provide finer pitch resolution. 

The rhythmic ratio (R) is computed by dividing the duration of two consecutive notes, capturing the relative changes, i.e., whether the duration increases or decreases at each step. For example, in Figure 2, a quarter note is followed by two tied quarter notes; in this step, the following note’s duration is twice that of the previous one. Rests are treated as notes, and their rhythmic ratio is also computed. 

In addition, we consider two other features derived from combining D, C, and R: the diatonic-rhythmic (DR) and the chromatic-rhythmic (CR) features. This approach en- 

191 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
Global Shared Phrases Form Combined F25 S75 Combined F50 S50 Combined F75 S25<br>Genre\Feature D C R DR CR D C R DR CR D C R DR CR D C R DR CR D C R DRCR D C R DRCR<br>Alalás 2.041.992.191.981.981.381.371.441.411.361.751.781.781.761.761.581.581.881.611.691.651.691.981.691.821.771.812.081.801.96<br>Barndance 1.011.011.021.011.011.091.091.121.071.061.231.221.231.221.221.141.141.191.121.121.181.171.221.161.171.211.211.251.201.22<br>Foliadas 1.221.171.241.181.150.860.880.910.900.930.950.950.950.950.930.870.880.900.890.930.890.900.920.910.930.910.920.930.930.93<br>Hornpipe 0.890.900.950.910.921.000.991.020.980.981.071.071.071.071.071.021.011.041.001.001.031.031.051.021.021.051.051.061.051.05<br>Jig 66.00.981.161.051.051.051.041.041.031.021.101.101.121.101.101.071.061.071.061.051.091.071.091.071.071.10 1.091.111.091.09<br>Jotas 0.860.860.940.900.890.850.880.860.860.900.860.860.860.860.850.830.850.810.840.850.830.850.820.850.850.84 0.850.830.850.85<br>March 1.011.021.021.021.021.051.031.061.041.031.111.111.111.111.111.071.061.101.071.061.091.081.111.081.081.101.101.121.101.10<br>Marchas 1.101.101.081.091.090.991.000.950.991.000.950.950.950.950.950.980.990.930.970.990.970.980.940.970.980.960.960.940.960.96<br>Mazurcas 1.011.001.041.031.020.990.980.950.990.980.960.960.960.960.970.980.970.940.980.970.970.970.940.970.960.970.960.950.970.96<br>Mazurka 1.091.061.141.181.161.000.991.021.010.991.081.081.081.081.081.021.011.051.031.011.041.031.061.041.031.061.061.081.061.06<br>Muiñeiras 1.061.051.181.121.101.000.990.981.021.011.031.031.031.031.031.011.000.991.021.02 1.01 1.011.001.021.021.021.021.021.031.03<br>Pasacorredoiras1.041.041.151.091.081.031.021.001.031.021.051.051.061.051.051.041.031.021.041.041.051.041.031.041.051.051.051.051.051.05<br>Pasodobles 1.041.021.061.051.040.930.930.930.930.940.940.940.940.940.930.920.930.910.920.930.930.930.920.920.930.930.930.920.93093<br>Polca 0.950.931.111.010.981.011.001.031.011.001.041.041.041.041.041.011.011.031.011.001.021.021.041.021.011.031.031.051.031.03<br>Polka 1.331.301.231.201.191.271.241.291.241.251.741.741.741.741.741.441.411.581.411.481.561.541.721.531.641.70 1.691.891.691.83<br>Reel 1.021.011.201.061.071.181.141.281.161.141.341.341.351.341.341.261.221.461.231.231.301.271.471.271.301.341.321.451.321.37<br>Rumbas 1.091.081.101.071.060.991.000.991.001.011.001.001.001.001.000.991.000.991.001.010691.00091.001.001.001.006601.001.00<br>Slide 1.291.271.581.371.351.311.291.311.291.281.991.992.001.991.991.541.521.671.501.571.701.701.901.681.811.931.922.201.912.12<br>Strathspey 1.21 1.201.281.231.211.301.271.271.251.231.721.71 1.711.711.71 1.47 1.451.541.411.451.581.561.681.531.601.701.691.841.671.79<br>Valses 0.950.940.960.960.950.870.880.850.880.880.880.890.890.890.900.860.870.840.880.840.860.870.850.870.860.870.880.860.880.87<br>Waltz 0.740.750.680.720.730.800.790.800.800.790.750.750.750.750.750.770.760.750.770.750.760.750.750.760.740.750.750.740.750.74<br>Average 1.09 1.08 1.16 1.11 1.10 1.04 1.04 1.051.041.041.171.171.171.17 1.171.091.081.131.081.091.121.121.171.111.141.161.161.21 1.16 1.19<br><!-- End of picture text -->

Figure 3. GSR metric for each feature using global, shared phrases, form, and combined similarity methods. A traffic light scale highlights best (higher) and worst (lower) results. Higher values indicate genres are better inferred. 



<!-- Start of picture text -->
GSR Sensitivity to Genre Assignment Noise<br>50 Perfect classification GSR: 51.0051.0x higher than random Random trees baseline (mean: 1.000)GSR with increasing noise<br>Random Trees GSR Distribution<br>40 1.010<br>1.005<br>1.000 Mean: 0.9999<br>30 $66'0<br>0.990<br>GSR Value<br>20 Perfect classification GSRis significantly different from random chance<br>Mean GSR from 10,000 random trees<br>10 Convergence at ≥ 40% noise reflects(μ ≈ 1.000, a = 0.0000)<br>the metric's sensitivity to meaningful clustering<br>0<br>0 10 20 30 40 50<br>Noise Level (%)<br><!-- End of picture text -->

Figure 4. GSR drops with noise, nearing random baseline. 

The next two methods identify common phrases between scores prior to computing similarity. One focuses on the number of phrases shared; the other accounts for musical form, i.e., the temporal alignment of shared phrases. The final method combines the preceding two. 

## 3.2.1 Global Similarity 

This is the most direct comparison method. It computes similarity between the entire feature vectors of two pieces by comparing their global alignment, as proposed by Needleman et al. [21] for searching similarities in the amino acid sequences of two proteins. The algorithm assigns a +1 penalty to mismatches and gaps, so lower alignment scores indicate greater similarity. 

## 3.2.2 Shared Phrases Similarity 

ables score representation regardless of key or time signature. To properly combine pitch and rhythm definitions, the character ‘r’ is introduced to indicate melodic rests. This ensures that odd array positions define pitch, while even positions define rhythm. Figure 2 provides an example of a score fragment with the resulting five features. 

## 3.2 Similarity Methods 

For each pair of scores in the dataset, we compute their similarity per musical feature. From now on, let us consider that a musical piece or phrase is represented as a feature vector. We explored four methods to compute similarity, aiming to assess their robustness in grouping the dataset’s genres, assuming that pieces within each genre tend to share pitch and rhythmic patterns. 

The first method consists in performing direct alignment between score pairs. This frequently used method [10, 20] serves as a baseline to check whether hierarchical structural knowledge improves in-genre groupings. 

As the scores have been divided into phrases, the number of phrases they share can be compared. Before this, it is necessary to assess which phrases are considered equal at the feature level under consideration. Given that many differ only in a few notes, we treat it as a clustering problem. 

First, global alignment distances are computed between all phrase pairs. We then adapt the Quality Threshold (QT) Clustering algorithm (Heyer et al. [22]), seeding clusters with phrases at zero distance and constraining cluster cohesion via a maximum diameter rather than a minimum size to prevent grouping dissimilar phrases. That diameter threshold is set to the 10th percentile of the feature’s distance distribution—providing sufficient sensitivity to group similar phrases while avoiding over-fragmentation. A phrase joins the first cluster whose distance to every existing member remains below this threshold; if none qualifies, it forms a singleton cluster. 

Each cluster receives a unique ID. We encode each score as the multiset of its phrase-cluster IDs and compute the resulting frequency vector. The shared-phrases 

192 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
pasacorredoiras(galician)<br>muineiras (galician)<br> Jig (rish)<br> mazurka (irish)<br> march (irish)<br>hornpipe (irish)<br>barndance (rish)<br> reel (rish)<br>strathspey (irish)<br>alalas(galician)<br> mazurcas (galician)<br>marchas (galician)<br> rumbas (galician)<br>polca (galician)<br>waltz (irish)<br>pasodobles (galician)<br>foliadas (galician)<br>jotas (galician)<br><!-- End of picture text -->

Figure 5. Genre tree for rhythmic feature using combined 75% form + 25% shared phrases similarity. Irish and Galician genres highlighted in blue and green, respectively. 

alignment value between two scores is then defined as the Euclidean distance between their frequency vectors — a symmetric, metric measure that naturally arises from the geometry of vector spaces, where similarity corresponds to spatial proximity, and a perspective consistent with established vector-space models in music analysis [23]. 

Example. Let Score A: P1, P2, P1, P3; and Score B: P2, P4, P4, P1. Suppose the phrases are grouped as follows: P1, P2 ∈ C1, P3 ∈ C2, P4 ∈ C3. Then, Score A corresponds to cluster sequence {C1, C1, C1, C2}, and Score B to {C1, C3, C3, C1}. These are encoded as frequency vectors: [3, 1 <mark>,</mark> 0 <mark>]</mark> and <mark>[</mark> 2 <mark>,</mark> 0 <mark>,</mark> 2 <mark>],</mark> res <mark>p</mark> ectivel <mark>y</mark> . The Euclidean distance is (3−2)<sup>2</sup> + (1−0)<sup>2</sup> + (0−2)<sup>2</sup> = <mark>√</mark> 6. 

## 3.2.3 Form Similarity 

Given that each score is defined by the cluster ID of its phrases, it is possible to compute a global alignment based on this definition. This approach allows us to consider phrase order explicitly, capturing structural properties that emerge from the hierarchical organization of the scores. 

Example. Cluster sequences: {C1, C1, C2, C2} vs. {C1, C2, C1, C2}. Both yield a frequency vector of [2, 2] (shared segments distance = 0), but differ in structure, resulting in non-zero form distance. 

## 3.2.4 Combined Similarity 

The combination of shared phrases similarity and form similarity provides a suitable model. The alignment values obtained for each comparison method are first subjected to min-max normalisation, a data preprocessing technique that transforms them to a standard scale. The normalised values are then combined for each score pair using a weighted sum. We examine three combinations of form (F) and shared phrases (S): 0.25 × F + 0.75 × S; 0.5 × F + 0.5 × S; and 0.75 × F + 0.25 × S. 

## 3.3 Phylogenetic Trees 

After calculating a distance matrix between all the scores in the dataset for each combination of features and com- 



<!-- Start of picture text -->
Rhythmic Genre Distance - Combined F75 S25 Similarity<br>barndance<br>hornpipe<br>jig 0.54<br>march<br>mazurka<br>polka 0.23 0.25<br>reel<br>slide 0.22 0.25<br>strathspey<br>waltz<br>alalas<br>foliadas<br>jotas<br>marchas<br>mazurcas<br>muineiras<br>GALICIAN<br>pasacorredoiras<br>pasodobles<br>polca<br>rumbas<br>valses<br>barndance mazurka foliadas jotas polca<br><!-- End of picture text -->

Figure 6. Heatmap of rhythmic distances between genres using 75% form + 25% shared phrases. Cividis scale highlights closer genres in yellow, distant ones in blue. 

parison methods, it is now possible to construct a phylogenetic tree for all such models. The algorithm used for this purpose is Neighbour Joining [24], a bottom-up method that iteratively joins the pair of elements that minimises total branch length. This approach yields unrooted trees and does not assume a constant rate of change, making it well suited to exploratory contexts where no common ancestor is presumed. While the tree figures shown in this paper are rooted for better visual depiction, this does not imply temporal or genealogical derivation—only structural similarity based on the selected comparison features. 

After constructing the phylogenetic trees for all combinations of features and similarity methods, we explore how each model organises the scores in relation to the genre labels provided in the dataset. This is done by computing a distance between each pair of genres, defined as the average tree distance between all scores assigned the respective genres. The resulting genre-level distance matrix is used to generate a phylogenetic tree via the Neighbour Joining algorithm. The matrix is stored in XLSX format, and a heatmap is generated from its min-max normalised version for visual analysis. This representation is not intended as a classification or validation of genre categories, but rather as an analytical tool to contrast models and support musicological interpretation. 

An ethnomusicologist analysing a given feature and comparison method may begin by examining the genre tree and heatmap to observe proximity between genres or internal dispersion within one. Based on this overview, specific genres can be selected for further analysis by computing a tree of scores restricted to them. This enables focused exploration of cross-genre and cross-tradition relationships, potentially revealing otherwise unnoticed connections. 

193 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

### Barndance Marias Prayer 

R: 1 2 1/2 1 2 1/2 1 2 1/2 1 2 1 1/2 1 1 1 1 1 1 1 4 Rumba de Berdoias 

R: 1 21/212 1/212 2 1/41111111116 

Figure 7. Example of two phrases from different traditions. Rhythmic ratio shown in red below each phrase. 

## 4. FEATURE-BASED ANALYSIS OF PHYLOGENETIC TREES 

In order to ascertain which phylogenetic tree from the comparison methods organises the genres more coherently, a metric is required to evaluate whether scores from the same genre tend to cluster together, and whether those from different genres remain further apart. Given the absence of a reference tree for Irish and Galician musical genres, the Inter-Intra Class Distance Ratio metric is adapted from its frequent use in machine learning to check how well a model separates classes. The concept of measuring intraclass cohesion and inter-class separation is fundamental to clustering evaluation metrics [25] and has also been used to assess musical genre separation models [26]. We will refer to this metric as the genre separation ratio (GSR). 

The GSR is calculated for each genre as the ratio of the average between-genre distance to the average withingenre distance. Values greater than one indicate that genres are well separated and that scores from different genres are more distant from each other than from the same genre. Conversely, values lower than one suggest that the distance within a genre exceeds the distance between genres. This last case indicates that the genres are quite similar and that we need sub-genres to distinguish them better. 

## GSR =<sup>avera</sup><sup><mark>g</mark>e intra-</sup><sup><mark>g</mark>enre distance</sup> average inter-genre distance 

Figure 3 presents the GSR results by genre across phylogenetic trees derived from each feature, according to the different similarity comparison methods. On average, form similarity—capturing the phrase-level structure of music—produces higher GSR values, with the 75% form + 25% shared phrases combination yielding the strongest results. The analysis reveals genres that are more clearly differentiated (e.g. “Alalás”, “Polka”, “Slides”, “Strathspey”) and others with greater overlap or lower intra-genre cohesion (e.g. “Waltz”, “Valses”, “Jig”). Overall, the GSR metric provides a nuanced characterization of stylistic differentiation in the Irish and Galician traditions. 

To evaluate the interpretability of the GSR scale, we conducted a sensitivity analysis (see Figure 4). An idealized genre tree produced a GSR of 51.0. Noise was gradually introduced into the genre assignments (up to 50%), leading to a sharp decline in the average GSR, which approached a baseline. This baseline was established using 10,000 trees based on random distance matrices, resulting 



<!-- Start of picture text -->
muineiras<br> pasacorredoiras (galcian)<br>mazurka (rish)<br>• jig (rish)<br>hornpipe (irish)<br>march (rish)<br>barndance (irish)<br> reel (irish)<br>strathspey (irish)<br>alalas (galician)<br>slide<br>(uejei) d<br>waltz (rish)<br>pasodobles (galician)<br>valses (galician)<br> foliadas (galician)<br>Jotas (galiciar)<br>marchas<br><!-- End of picture text -->

Figure 8. Genre tree for chromatic-rhythmic feature using combined 75% form + 25% shared phrases similarity. Irish and Galician genres highlighted in blue and green. 

in a distribution tightly centered at 1.00 (with a maximum outlier of 1.0099). The best-performing methods reached GSR values between 1.17 and 1.21, significantly exceeding values expected under random conditions. These results support the statistical significance of the genre-level patterns inferred by the proposed approach. 

## 5. ETHNOMUSICOLOGICAL CASE STUDY 

To illustrate the potential of our methodology in practical contexts, we focus on the rhythmic and chromaticrhythmic representations, using a combined similarity measure with a 75% form and 25% shared phrase weighting. These configurations yielded the highest average GSR values (see Figure 3), offering clearer inter-genre separation and stronger intra-genre cohesion. The selected features thus provide a particularly meaningful basis for exploring stylistic connections across traditions. This analysis showcases how an ethnomusicologist might leverage such representations to uncover culturally grounded relationships within and between repertoires. The source code, annotated dataset, and results are available at `https: //github.com/hromerovelo/folkroot` (Docker image provided at `https://hub.docker.com/r/ hrvelo/folkroot` ). 

## 5.1 Rhythmic Patterns 

A preliminary examination of the genre tree in Figure 5, based on shared rhythmic patterns and their temporal alignment, shows that both traditions are clearly divided into two main branches. The heatmap in Figure 6 reveals a stronger correlation among Irish genres (e.g., “polka”, “reel”, “slide”, and “strathspey”, which share a strong relationship as dance tunes in duple or quadruple meter— with the exception of “slides”, typically associated with a ternary meter). 

Analysing the diagonal of the heatmap, “polkas”, “reels”, “slides” and “strathspey” are genres with a high degree of similarity between in-genre pieces. These cases appear to support the assumption—as stated in Section 

194 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
Pasodoble de Pol Rumba dos Portelas de Moares<br>CR: 1/2 5 CR: 11/2121/21 21/2121/21 21/2121/21 122-4 2 2 2 -2 -2 -3 1 2 2 -2 -2 -3 2 1 4 0<br>Vals de Arousa<br>CR: 1/4 2 -1 -21 3 4 21 -21 -3 3 4<br><!-- End of picture text -->

Figure 9. Example of a cluster of common phrases from scores of the same tradition but belonging to different genres. Their corresponding chromatic and rhythmic values are shown below each phrase in teal and red colour, respectively. 

3.2—that pieces within a given genre share similar rhythmic and pitch characteristics. In contrast, the Irish “waltz” from the The Session dataset exhibits a maximum intragenre distance (1.0), reflecting complete rhythmic dissimilarity among its own pieces. This initially unexpected outcome prompted closer examination. After discussing this case with Treasa Harkin of the Irish Traditional Music Archive, it was confirmed that the “waltz” label in The Session includes a heterogeneous selection of material: alongside Irish waltzes, it comprises unclassified tunes and Scottish airs, many of which differ stylistically. More broadly, such instances of low within-genre similarity suggest that certain genres may require a richer set of musical descriptors—or even contextual information—to become meaningful points of reference for approaches that explore content-based similarity across repertoires. 

To illustrate the systematic potential of the proposed methodology for cross-cultural studies, consider an ethnomusicologist examining the relationship between two genres from different traditions: the Irish “barndance” and the Galician “rumba”. They could construct a phylogenetic tree of the corresponding scores and observe emerging similarities. Figure 7, for instance, displays two phrases— one from each genre—with a noticeable rhythmic resemblance. Despite the “barndance” typically being performed at a faster tempo (with accents every two beats) and the “rumba” favouring beat-level emphasis, their phrasing results in comparable accentual patterns, reinforcing the perception of high rhythmic similarity. 

## 5.2 Chromatic-Rhythmic Patterns 

The chromatic-rhythmic genre tree (Figure 8) closely resembles the rhythmic one (Figure 5) under the combined similarity metric (75% form, 25% shared phrases), with correlation coefficients of Pearson = 0.9985, Spearman = 0.9982, and Kendall = 0.9687. This reflects structurally equivalent phrases identified via clustering and form-based comparison. In contrast, global similarity between chromatic and rhythmic features yields notably lower correlations (Pearson = 0.8739, Spearman = 0.7833, Kendall = 0.6160), indicating that each feature captures distinct genre-level traits. The approach thereby offers flexibility for exploring stylistic relationships across different representational and comparative levels. 

Focusing on the Galician branch, we studied the relationship between “rumbas”, “pasodobles”, and “valses”— 

genres typically in simple meter. Among these, the score tree reveals a “pasodoble”, a “rumba”, and a “valse” that share similar phrases belonging to the same cluster, as illustrated in Figure 9. While their chromatic-rhythmic descriptions are shown separately for clarity, processing is done jointly, alternating pitch and rhythm values (see Section 3). All three happen to be in C major, though the method is transposition-invariant. This example highlights the method’s robustness in detecting descending thirds by diatonic steps despite differing melodic paths between anchor notes—an alignment not ensured by global similarity. 

## 6. CONCLUSIONS 

This article proposes a novel methodology for analysing large datasets of scores regarding their pitch and rhythmic musical characteristics. The proposed methodology is anchored in the musical hierarchy, thus establishing a novel model that incorporates the musical form (i.e. structure). This approach has yielded improved outcomes compared to baseline per-score global alignment methods. The results demonstrate that incorporating the musical hierarchy through its structural elements and identifying common patterns leads to enhanced analysis of musical relationships. Within the context of folk music, incorporating rhythmic and chromatic-rhythmic features results in a more comprehensive depiction of the dataset. The findings suggest that this framework, considered in its full design, has the potential to serve as a valuable tool for ethnomusicologists conducting cross-cultural studies. Furthermore, it demonstrates how bioinformatics and music can be combined to advance and open up new avenues of research. 

The present paper establishes the foundations for future studies, exploring the use of other phylogenetic algorithms, network-based strategies such as NeighborNet visualisations, and metrics inspired by phylogenetic signal. These directions may help address phenomena like horizontal transmission or stylistic hybridisation, which exceed tree representations. Further work with repertoires from other traditions may clarify which features and hierarchical levels are most informative. In parallel, ongoing collaboration with musicologists aims to evaluate and refine phrase clustering, strengthening the method’s potential as a grounded framework for comparative analysis. 

195 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 7. ACKNOWLEDGMENTS 

We would like to thank Folkoteca Galega and Xulio Xesús León Pérez for providing access to their full archive of Galician traditional music. We also acknowledge the support of PuntoGal to the Folkoteca project, and all the collaborators who have contributed scores to the platform ( `https://folkotecagalega.gal/xente` ). 

Work funded by: CITIC, as a center accredited for excellence within the Galician University System and a member of the CIGUS Network, receives subsidies from the Department of Education, Science, Universities, and Vocational Training of the Xunta de Galicia. Additionally, it is co-financed by the EU through the FEDER Galicia 202127 operational program (Ref. ED431G 2023/01); Xunta de Galicia/FEDER-UE, Spain [grant numbers ED481A 2023/006]; This research has been partially funded by the European Union’s Horizon Europe research and innovation programme under the Marie Sklodowska-Curie grant agreement no 101086338. 

## 8. REFERENCES 

- [1] P. E. Savage and Q. D. Atkinson, “Automatic tune family identification by musical sequence alignment,” in Proceedings of the 16th International Society for Music Information Retrieval Conference (ISMIR), 2015, pp. 162–168, licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). [Online]. Available: http://dx.doi.org/10. 6084/m9.figshare.1468015 

- [2] P. E. Savage, S. Passmore, G. Chiba, T. E. Currie, H. Suzuki, and Q. D. Atkinson, “Sequence alignment of folk song melodies reveals cross-cultural regularities of musical evolution,” Current Biology, vol. 32, no. 6, pp. 1395–1402, 2022. [Online]. Available: https://doi.org/10.1016/j.cub.2022.01.039 

- [3] S. L. Bomin, G. Lecointre, and E. Heyer, “The evolution of musical diversity: The key role of vertical transmission,” PLoS ONE, vol. 11, no. 3, p. e0151570, 2016. [Online]. Available: https: //doi.org/10.1371/journal.pone.0151570 

- [4] G. Rambold, D. Neubacher, and S. Schießl, “Fingerprints, barcode sequences and quasi-phylogenies: Tools for analysing polyphonic music,” PLoS ONE, vol. 18, no. 3, p. e0280478, 2023. [Online]. Available: https://doi.org/10.1371/journal.pone.0280478 

- [5] J. H. Jr., G. A. Ballen, K. H. Mühlová, and H. Vlhová-Wörner, “Towards building a phylogeny of gregorian chant melodies,” in Proceedings of the 24th International Society for Music Information Retrieval Conference (ISMIR), 2023, pp. 571–578. [Online]. Available: https://doi.org/10.5281/zenodo.10265348 

- [6] J. M. Diaz-Banez, G. Farigu, F. Gómez, D. Rappaport, and G. T. Toussaint, “El compás flamenco: A phylogenetic analysis,” in Proceedings of BRIDGES: 

Mathematical Connections in Art, Music, and Science, 2004, pp. 62–70. [Online]. Available: https://archive. bridgesmathart.org/2004/bridges2004-62.pdf 

- [7] P. van Kranenburg, A. Volk, F. Wiering, and R. C. Veltkamp, “Musical models for folk-song melody alignment,” in Proceedings of the International Society for Music Information Retrieval (ISMIR), 2009, pp. 507–512. [Online]. Available: https: //ismir2009.ismir.net/proceedings/PS3-20.pdf 

- [8] A. Volk, E. Chew, E. H. Margulis, and C. Anagnostopoulou, “Music similarity: Concepts, cognition and computation,” Journal of New Music Research, vol. 45, no. 3, pp. 207–209, 2016. [Online]. Available: https://doi.org/10.1080/09298215.2016.1232412 

- [9] N. Carvalho, D. Diogo, and G. Bernardes, “Computational similarity of portuguese folk melodies using hierarchical reduction,” in Proceedings of the 10th International Conference on Digital Libraries for Musicology (DLfM). Milan, Italy: ACM, 2023. [Online]. Available: https://doi.org/10.1145/3625135.3625152 

- [10] B. Janssen, P. van Kranenburg, and A. Volk, “A comparison of symbolic similarity measures for finding occurrences of melodic segments,” in Proceedings of the 16th International Society for Music Information Retrieval Conference (ISMIR), 2015, pp. 622–628. [Online]. Available: https://dspace.library.uu.nl/bitstream/handle/1874/ 321370/Janssen_etal_Proceedings.pdf?sequence=1 

- [11] A. Volk and P. van Kranenburg, “Melodic similarity among folk songs: An annotation study on similaritybased categorization in music,” Musicae Scientiae, vol. 16, no. 3, pp. 317–339, 2012. [Online]. Available: https://www.staff.science.uu.nl/~veltk101/ publications/art/MusicaeScientiae2012.pdf 

- [12] P. van Kranenburg, A. Volk, and F. Wiering, “A comparison between global and local features for computational classification of folk song melodies,” Journal of New Music Research, vol. 42, no. 1, pp. 1–18, 2013. [Online]. Available: https://doi.org/10. 1080/09298215.2012.718790 

- [13] M. Gutiérrez-Steinkamp, “The world of the irish / el mundo irlandés,” TSN: The Spanish Newsletter, no. 9, pp. 77–89, January–June 2020, smithsonian Fellow & Fulbright Specialist (USA). [Online]. Available: https: //dialnet.unirioja.es/descarga/articulo/7855918.pdf 

- [14] E. A. Franch, “Carlos núñez y la música celta,” Revista de Folklore, no. 509, pp. 89–106, 2024. [Online]. Available: https://funjdiaz.net/folklore/07ficha.php? ID=5097&NUM=509 

- [15] X. M. S. Rei, “Language and music in galicia and ireland in the early 20th century,” Oceánide, vol. 13, 2020. [Online]. Available: https://oceanide.es/index. php/012020/article/view/37 

196 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [16] A. F. Vásquez, “The galician fiddle style,” in Crossing Over: Fiddle and Dance Studies from around the North Atlantic 3, I. Russell and A. K. Guigné, Eds. Aberdeen, UK: The Elphinstone Institute, University of Aberdeen, 2010, pp. 199–214. [Online]. Available: https://aura.abdn.ac.uk/bitstream/handle/2164/ 5048/Crossing_Over_2010_Ch._16_V_squez_.pdf 

   - [26] G. Tzanetakis and P. Cook, “Musical genre classification of audio signals,” IEEE Transactions on Speech and Audio Processing, vol. 10, no. 5, pp. 293–302, 2002. [Online]. Available: https: //www.cs.cmu.edu/~gtzan/work/pubs/tsap02gtzan.pdf 

- [17] M. Alberro, “The celticity of galicia and the arrival of the insular celts,” in Proceedings of the Harvard Celtic Colloquium, vol. 24/25, 2009, pp. 1–15. [Online]. Available: https://www.jstor.org/stable/40285178 

- [18] J. C. Calvo-Sotelo, “In the name of ossian: Celtic galicia and the ’brothers from the north’,” Social Identities, vol. 25, no. 6, pp. 828–842, 2019. [Online]. Available: https://doi.org/10.1080/13504630.2018.1564267 

- [19] T. Zhu, R. Fournier-S’niehotta, P. Rigaux, and N. Travers, “A framework for content-based search in large music collections,” Big Data and Cognitive Computing, vol. 6, no. 1, 2022. [Online]. Available: https://www.mdpi.com/2504-2289/6/1/23 

- [20] B. Janssen, P. van Kranenburg, and A. Volk, “Finding occurrences of melodic segments in folk songs employing symbolic similarity measures,” Journal of New Music Research, vol. 46, no. 2, pp. 118–134, 2017. [Online]. Available: https://doi.org/10.1080/ 09298215.2017.1293802 

- [21] S. B. Needleman and C. D. Wunsch, “A general method applicable to the search for similarities in the amino acid sequence of two proteins,” Journal of Molecular Biology, vol. 48, no. 3, pp. 443–453, 1970. [Online]. Available: https: //doi.org/10.1016/0022-2836(70)90057-4 

- [22] L. J. Heyer, S. Kruglyak, and S. Yooseph, “Exploring expression data: identification and analysis of coexpressed genes,” Genome Research, vol. 9, no. 11, pp. 1106–1115, 1999. [Online]. Available: https://genome.cshlp.org/content/9/11/1106 

- [23] D. Meredith, K. Lemström, and G. A. Wiggins, “Algorithms for discovering repeated patterns in multidimensional representations of polyphonic music,” Journal of New Music Research, vol. 31, no. 4, pp. 321–345, 2002. [Online]. Available: https://research.gold.ac.uk/id/eprint/1008/ 

- [24] N. Saitou and M. Nei, “The neighbor-joining method: a new method for reconstructing phylogenetic trees,” Molecular Biology and Evolution, vol. 4, no. 4, pp. 406–425, 1987. [Online]. Available: https: //academic.oup.com/mbe/article/4/4/406/1029664 

- [25] X. Xie and G. Beni, “A validity measure for fuzzy clustering,” IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 13, no. 8, pp. 841–847, 1991. [Online]. Available: https://www.computer.org/ csdl/journal/tp/1991/08/i0841/13rRUynHuk4 

197 

