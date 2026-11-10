---
paper_id: "000051"
year: 2022
title: "Download pdf"
source_url: "https://zenodo.org/record/7316692/files/000051.pdf"
---

# LEARNING UNSUPERVISED HIERARCHIES OF AUDIO CONCEPTS 

Darius Afchar<sup>1,2</sup> Romain Hennequin<sup>1</sup> Vincent Guigue<sup>2</sup> 1Deezer Research, France 2MLIA, ISIR - Sorbonne Université - CNRS, France research@deezer.com 

## ABSTRACT 

Music signals are difficult to interpret from their lowlevel features, perhaps even more than images: e.g. highlighting part of a spectrogram or an image is often insufficient to convey high-level ideas that are genuinely relevant to humans. In computer vision, concept learning was therein proposed to adjust explanations to the right abstraction level (e.g. detect clinical concepts from radiographs). These methods have yet to be used for MIR. 

In this paper, we adapt concept learning to the realm of music, with its particularities. For instance, music concepts are typically non-independent and of mixed nature (e.g. genre, instruments, mood), unlike previous work that assumed disentangled concepts. We propose a method to learn numerous music concepts from audio and then automatically hierarchise them to expose their mutual relationships. We conduct experiments on datasets of playlists from a music streaming service, serving as a few annotated examples for diverse concepts. Evaluations show that the mined hierarchies are aligned with both ground-truth hierarchies of concepts ± when available ± and with proxy sources of concept similarity in the general case. 

## 1. INTRODUCTION 

Music signals are challenging to interpret [1]. For instance, inspecting a spectrogram by parts ± e.g. think of attention maps [2] ± does not convey much meaning with respect to the high-level descriptions that are useful to humans ± e.g. the mood of a song. Fortunately, a solution was proposed in a field that shares similar problems: computer vision. As pixels of images are too low-level to be understandable, concept learning was introduced to rationalise the abstractions steps involved in a feed-forward model (e.g. detection of colours, shapes, patterns, ...), which in turn can be used to describe the content of an image directly, and to align models with human reasonings better. Indeed, this field has had successful applications in explainability (XAI) ± dissecting a model’s predictions into humangrounded concepts [3±5], interactive learning [6] or knowledge transfer between tasks [7]. However, these methods have yet to be used for Music Information Retrieval (MIR). 

Music has particularities that are not captured by the current formulation of concept learning. For instance, let us consider genres as common musical concepts we would like to detect from spectrograms. Genres are typically blended as they influence or result from other genres (e.g. Punk Rock). By contrast, most literature on concept learning has considered sets of few identified and disentangled concepts, which does not apply to genres. Moreover, one trend in MIR is to incorporate multiple types of descriptors into a shared space (e.g. mood, genre, instruments [8, 9]), thus requiring handling even more entanglements. 

We thus propose to study a novel problem for concept learning that is relevant for music: learning hierarchies of concepts. Indeed, a hierarchy enables navigating thousands of non-independent concepts without cognitive overload by uncovering their mutual relationships with a structure, thus rationalising which concepts share the same class or are derived from one another. In addition, the use of taxonomy ± i.e. hierarchy ± is common in musicology and feels like a natural representation in this context [10,11]. 

The problem we study is interesting for music representation learning because research is often limited by data labelling, which is labour-intensive and can be ambiguous or tied to a specific dataset. Meanwhile, concepts can be learned with few shots, which open the doors to new sources of music descriptors. In particular, we propose to leverage a dataset of playlists from a music streaming service as a folksonomy of concepts. Playlists are often built with a specific concept; there exists one for any genre, instrument, mood, and many more niche ideas. Yet, there is no overall ground-truth organisation of playlists, making their use cumbersome. That is why we propose to solve this task by first adapting a method from concept learning research to learn music concepts from playlists in a fewshot manner and then, building on top of this method, automatically derive a hierarchy from the learned concepts. 

The paper proceeds as follows: we provide background on concept and hierarchy learning (section 2); we adapt the literature of concept-based explanations to the realm of MIR (3); we present a novel way to organise the detected concepts into a hierarchy in an unsupervised manner (4); finally, we experiment and discuss our attempt to provide a new audio concepts hierarchy with mixed types (5). 

> © D. Afchar, R. Hennequin, and V. Guigue. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: D. Afchar, R. Hennequin, and V. Guigue, ªLearning Unsupervised Hierarchies of Audio Conceptsº, in Proc. of the 23rd Int. Society for Music Information Retrieval Conf., Bengaluru, India, 2022. 

## 2. PRELIMINARIES AND RELATED WORK 

We first present the literature on concept learning and hierarchy mining, then frame our problem through XAI to uncover common pitfalls to avoid when interpreting data. 

427 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
(a) Concept learning from music playlists (b) Vector similarity computation (c) Graph hierarchy extraction<br>Playlist<br>track 1 [v1, ..., vK]<br>track 2<br>...<br>Reggae<br>Funk Rock<br>Latin Influenced<br>Jazz Rock Funk<br>Jazz Funk<br>Acid Jazz Latin<br>Fusion<br>learned concept vector: v Kiddie Pop Calypso<br>Latin Dance Style<br><!-- End of picture text -->

Figure 1. Overview of our method (a) CAVs learning (section 3.1); (b) t-SNE projection of concepts Vgenre learned on a small dataset with 219 music genres; (c) resulting extracted hierarchy H(S(Vgenre)). Nodes colours denote ground-truth clusters. Experiments on a bigger concept dataset are conducted in section 5. 

## 2.1 Concept learning 

Concept learning has witnessed growing interest in recent years [4]. The introduction of concepts stems from the inadequacy of usual explanation spaces with human mental models of problems: tabular features, pixels, and words in sentences are sometimes too low-level to build relevant explanations or to interact with. This idea is far from novel from a purely technical standpoint: a stream of papers aim to learn a set of sub-attributes in a fully supervised manner (e.g. facial features [12], or animal attributes [13]), that are then combined to predict some end-task labels, typically through a linear regression to track the importance of each attribute. This idea has been revamped recently for concept bottleneck learning [14] and prototypical part learning [15]. In the same vein, disentanglement techniques [16] have sought to realign latent representations to interpretable attributes. All those works rely on the assumption that a somewhat complete set of useful concepts exists, well-defined and rather disentangled, and that a corresponding labelled dataset is readily available to train on. 

This is rarely the case in practice. Kim et al. introduced CAVs for images [3] and demonstrated that concepts could be learned reliably from few annotated examples ± technical details are provided in section 3.1. Going beyond the previously few datasets annotated for concepts, this work has led to new and diverse applications: skin lesion interpretations [17], emotion recognition [18], interactivity [6,19], automatic concept learning [20], batch normalisation [21], sufficiency of explanations with shapley values [22, 23], causal inference [24]. To our knowledge, there exists no application in the music domain. 

## 2.2 Unsupervised Hierarchy Mining 

Using knowledge graphs and taxonomies is frequent leverage in MIR [25]. Unsupervised learning of hierarchy is, 

however, less so. Part of it lies in the difficulty of adequately defining the meaning of the hierarchical relations, learning the hierarchy in a tractable way, and evaluating the found hierarchy without ground-truth. 

Fortunately, there is active literature coming from natural language processing (NLP) research. Many work proposed variants of topic modelling [26] to enable sampling hierarchised structures [27, 28]. However, these methods get computationally intractable as the number of nodes, topics, and hierarchical levels grows. Many successes thus came from scalable greedy methods such as hierarchical clustering [29, 30], rule-mining [31, 32] and graph-based analyses [33, 34]. Outside of NLP, hierarchies have been learned based on the latent manifold geometry [35], predefined structure [36], and for images [37,38]. 

To our knowledge, these techniques have never been combined with concept learning, as we propose. 

## 2.3 Explainability 

Our end goal is to interpret music signals, which is linked to explainability (XAI). Before jumping into our method to learn a hierarchy of concepts, we need to acknowledge that many works have debated the sanity of explanation methods [39±43] and the fact that these methods largely disagree with one another [44]. XAI has vast boundaries, which has also percolated to its music sub-field for which there exists many explanation paradigms and evaluations [45]. Explanations for MIR are thus also prone to exhibiting pathologies that hamper knowledge mining: e.g. shortcut learning [46], lack of clear definitions [39, 47], flawed evaluations [48], out-of-distribution artifacts [49, 50] or misalignment with human reasonings [51±54]. 

Uncovering these failure cases sharpens our understanding of how models make decisions, and shows that we have to go beyond evasive considerations on explain- 

428 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

ability to make them relevant [41] since trustworthy AI is not achieved automatically with XAI [55]. One taxonomic distinction we would like to underline is whether methods aim to explain models or data [56]. Our method is intended to belong to the latter category for which the purpose is not to explain how models work (e.g. troubleshooting learned filters) but rather to use them as proxies to gain new insights about reality (e.g. causal inference [57]). 

With all these aspects in mind and based on previous literature, we formalise our three explanation goals: 

1. Attribution. Identify musical concepts associated with a given track’s audio signal. 

2. Transferability. Detected concepts should be applicable to various settings and tasks. 

3. Generality. The hierarchy should be independent of the signals and make sense for various settings. 

Our first goal is linked to the traditional explanation literature supporting transparency [45,47] and is common in concept-learning. We have defined our second and third goals to stress that the finality of our work is to be as universal as possible. 

## 3. LEARNING MUSIC CONCEPTS 

In this section, we first adopt the few-shot supervision setting of concept learning to learn the music concept⃗vC of each playlist, viewed as a set C of audio signals examples. 

## 3.1 Background on CAVs 

We review some essential notions from the concept learning framework we use to learn playlist concepts [3]. 

We denote⃗f<sup>[ℓ]</sup> the output of the l-th layer of a trained neural network f taking as input some samples x ∼ X. A "concept activation vector"⃗vC is defined for a set of positive examples C as the normal to a separating hyperplane between {⃗f<sup>[ℓ]</sup> (x) | x ∈ C} versus negative examples ± usually {⃗f<sup>[ℓ]</sup> (x) | x̸ ∈ C}, we provide an illustration in Figure 1(a). In practice, the hyperplane is learned through a logistic regression on a subset of C, while holding out the remaining samples for validation and testing<sup>1</sup> . As additional insights, this setting is "sound" for fewshot learning because it uses a pretrained model f with prior knowledge on the domain ± relating to transfer learning [58] ± and learns a linear mapping on its space, hence reducing the risk of over-parametrisation and justifying why more complex mappings are not considered. 

## 3.2 Sets of examples C 

The work of Kim et al. [3] lends itself naturally to learning concepts from playlists. Indeed, playlists can be seen as small sets of positive music examples built around a particular musical idea. As it will be further detailed in our experiments, we can use data from music streaming services where playlists are abundant. We will denote C = {Ci}<sup>K</sup> i 

the set of K sets of music tracks that will enable to learn a CAV set V = {⃗vi}<sup>K</sup> i<sup>discriminating Cin the⃗f[ℓ]space.</sup> It must be noted that playlists are more than a set of tracks, we usually have access to textual data with a title and a description that help rationalise the learnt concepts. 

## 3.3 Backbone model⃗f<sup>[ℓ]</sup> 

As often in few-shot learning, CAVs learning makes use of a pretrained model f ± referred to as backbone ± to embed samples into a latent space with a higher level of abstraction. In this paper, our working hypothesis is that music concepts can be described solely through audio signals. We wanted to fully explore the potential of audio signals, which is a known challenging setting in MIR and recommendation [59], and leave its combination with other sources of features for future work. In addition, having audio inputs enables using our model with any music track from any dataset, hence supporting goal 2, while relying on features such as collaborative filtering or other usage data would have tied our model to a given dataset. 

After having experimented with several models, as the recent self-supervised model CLMR [60], we have chosen to use MusiCNN [61] as the backbone since it had demonstrated consistent performances across various musical tasks, which we deemed on par with our goal 2 and 3. MusiCNN was trained on the Million Song Dataset [62]. 

## 3.4 Preliminary results 

We provide some experimental observations to fix ideas and prepare the next section. If we train CAVs as in the original paper [3] ± further detailed in section 5.2, we obtain a set of vectors V that allows to detect a set of K concepts given any music input spectrogram. An example result of learned concepts is given in Figure 1(b) for one of the studied datasets. Unsurprisingly, we find that many associated concepts end up having close vector weights<sup>2</sup> . If we were to use our concept detectors directly, we would have many concepts activated simultaneously, which could make predictions hard to read when K is very big. On the positive side, note that vector proximity could be used as a means to quantify concept similarities. With this idea, we go a step further and next present our method to build a hierarchy to help rationalise concept dependencies. 

## 4. HIERARCHISING MUSIC CONCEPTS 

Having learned numerous non-independent concepts V = {⃗vi}<sup>K</sup> i<sup>, we next elaborate on how to organise them with a</sup> structure to make them usable (goals 2, 3). 

Many classes of structures are possible, and it would be a mistake to select one with purely theoretical considerations since cognitive and social sciences [63, 64] have underlined that explanatory preferences are shaped by diverse factors that cannot be reduced to a set of so-called golden explanation principles. Therefore, from an empirical standpoint, taxonomies seem to be frequent with music 

> 2 In the figure, proximity is defined as the cosine similarity. 

> 1 By definition,⃗vC is the learned parameter of a logistic regression. 

429 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

concepts (e.g. genres [8], instruments [25]). We thus argue that this class of graph is rather natural for humans and chose to consider it only. 

## 4.1 Similarity graph computation 

Before mining a hierarchy, it is necessary to determine how concepts ± now acting as graph nodes ± relate to one another. Essentially, we are trying to define a similarity measure between concepts. 

When sampling uniformly from a music dataset, concept activations are rare signals overshadowed by uninformative negative detection. The straightforward solution of estimating the empirical covariance of concept activations is thus not a well-behaved measure of similarity. Fortunately, there is another reliable, interpretable (and faster) way to do it. We propose to consider the positive examples of each concept playlist ± embedded in⃗f<sup>[ℓ]</sup> , and to check on what side of other concept hyperplanes their centroid lies. Formally, given V = {⃗vi}1<sup>K,wecomputethematri-</sup> ces of concept similarities S and adjacency A (i.e. A is a binarised matrix representing graph edges): 



<!-- Start of picture text -->
Si,j(V) = Ex∼Ci �σ(⟨⃗vj,⃗f [ℓ] (x)⟩)� (1)<br><!-- End of picture text -->



<!-- Start of picture text -->
Ai,j(V) = Si,j(V) ≥ 1 (2)<br>� 2 �<br><!-- End of picture text -->

where σ denotes the logistic sigmoid function and Ci a random variable sampling spectrogram excerpts from tracks of the playlist Ci. Bias is integrated in⃗vj for simplicity. The threshold at<sup><mark>1</mark></sup> 2<sup>forAtranslateshavingeachplaylist</sup> centroid on the positive side of the concept hyperplanes. Because V is learned through logistic regressions that return well-calibrated probabilities, S and A return similarities with well-defined interpretations. 

## 4.2 Hierarchy extraction 

Having defined similarities between concepts, we next simplify S and A to a hierarchy that highlights what concepts are similar to many others and what others represent unique and niche ideas. 

For our problem and its scale, we propose to adapt the greedy hierarchy construction of Heymann et GarciaMolina [33] that makes use of the notion of betweenness graph centrality [65]. In this method, given an unweighted graph of similarities, a tree is greedily grown by picking each node in decreasing order of centrality in the similarity graph and linking it to the most similar and already-added node in the tree. We denote by H(S(V)) the result of this algorithm on the similarity graph given by the adjacency matrix A(V) and using S(V) as similarity. 

Though this algorithm was originally applied to word tags, we argue that the inductive bias of the targeted hierarchy is applicable to our problem. In particular, the use of centrality is justified by the existence of noisy links in the similarity graph, said links are assumed to be more frequent higher up in the hierarchy (general-general assumption). For us, this means that general concepts ± e.g. Pop and Rock ± should be more likely to be similar than niche 

concepts ± Bedroom Pop and Goth Rock. This sounds reasonable for music content since we expect niche concepts to relate to a specific musical idea, style, or instrument. 



<!-- Start of picture text -->
soul for lovers<br>feeling sad sad pop<br>frozen 2 (french, ge...perinteinen joulu<br>love ballads romantic christmas<br>piano ballads<br>drama korean soul piano<br>mahogany: coversdia chuvoso<br>calming christian<br>pentecostal 2022 | ...chants et musiques c...hebraico/hebrew<br>he voice australia ...<br>indie chill<br>stockfish records<br>cozy christmas<br>didier jeunesse berc...looming flor...sad covers<br><!-- End of picture text -->



Figure 2. Obtained hierarchy on the Deezer dataset. An interactive plot of this figure, as well as many others, is available at research.deezer.com/concept_hierarchy/. 

## 5. EXPERIMENTS 

We first detail our experimental setups, then validate that concepts can be reliably learned from audio, and finally show that our proposed structuring method leads to consistent hierarchies for MIR applications. 

## 5.1 Datasets 

The set of playlists CD we use was exported through the API of the streaming platform Deezer<sup>3</sup> . We have filtered 3635 playlists of mixed types to be used as concepts: all 1498 editorial playlists available ± considered thoughtfully curated but biased by popularity, and 2137 public user playlists with the lower artist popularity ± to improve diversity. Playlists have a mean length of 75 tracks and a minimum of 40. This dataset includes the playlist ids, titles, descriptions, and public 30s audio preview for each track. There are 245074 unique tracks from 116497 unique artists: playlists overlap is thus very limited. 

In order to compare our computed hierarchy to existing taxonomies, we make use of the APM Music dataset [66]. This is a more traditionally tagged dataset, but its relevance for our task is to include a ground-truth two-level hierarchy of the music genres (219) and moods (165) tag types. We aggregate sets of positively tagged examples as Cgenre for each genre tags and respectively Cmood for moods. 

## 5.2 Validating concept learning 

We first present experimental evidence related to learning sets of concepts (section 3), to validate goal 1. 

## 5.2.1 Experimental setup 

Concept examples are split in a 70% (train) / 10% (validation) / 20% (test) fashion. According to the requirements of our backbone [61], we convert audio inputs to 

3 https://developers.deezer.com/api 

430 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

|Source|Audio(↓)|CF(↓)|BERT(↑)|W2V1 (↑)|W2V2(↑)|
|---|---|---|---|---|---|
|H(S(VD))|2.449±0.022|0.845±0.013|0.345±0.007|0.286±0.009|0.542±0.007|
|H(SCF)|2.413±0.021|0.345±0.007|0.416±0.008|0.336±0.010|0.601±0.008|
|H(SBERT)|2.858±0.028|0.868±0.013|0.726±0.005|0.505±0.011|0.652±0.008|
|H(SW2V-1)|2.952±0.028|0.932±0.012|0.523±0.008|0.804±0.005|0.721±0.007|
|H(SW2V-2)|2.843±0.026|0.847±0.012|0.531±0.008|0.596±0.009|0.836±0.004|
|Random|3.388±0.027|1.104±0.006|0.239±0.004|0.142±0.006|0.452±0.006|



Table 1. Evaluation of the full hierarchy on audio, user-logs and title semantic similarities with 95% confidence. Audio and CF source are endowed with an Euclidean distance, the last three semantic sources use cosine similarities. 

mel-spectrograms with log-magnitudes. Representations are extracted from the penultimate layer of the backbone, denoted as f<sup>[ℓ]</sup> ± which gave us the best performances for concept learning overall. Our complete training code, with further details and exact parameters, is provided for reproducibility at github.com/deezer/concept_ hierarchy. 

## 5.2.2 Learning metrics evaluation 

On the Deezer dataset CD, the mean balanced accuracy of learning concepts is 83.8% ± 0.3, with a 95% confidence interval. In detail, we display a histogram of test balanced accuracies in Figure 3, showing that a majority of playlist concepts can be learned reliably from audio. 

As a rationalisation of failure cases, the hypothesis we made in section 3.4 to detect concepts from audio may not always hold. For instance, it fails when playlist concepts rely on factors extraneous to audio (e.g. playlist of a movie soundtrack) or when the backbone space is not expressive enough to discriminate concepts. This actually happens in these experiments with concepts similar in all respects but for their singing languages: e.g. the model makes no difference between Japanese and British jazz. We filter concepts vi below a given test accuracy threshold to account for this effect. Fixed at 70%, 192 concepts are filtered out, leading to K = 3443 remaining concepts. This threshold was set empirically by checking that those left-out concepts were indeed unclear from audio (e.g. OST, new releases, charts). We denote the resulting concept set VD. 

The two smaller APM datasets lead to similar results with a 78.3% ± 0.8 for genres, denoted Vgenre, and a 71.3% ± 0.6 accuracy for mood tags, denoted Vmood. 

As a wrap-up of this section, goal 1 of detecting concepts from audio seems satisfied in our experiments. 



<!-- Start of picture text -->
400<br>300<br>200<br>100<br>0<br>0.5 0.6 0.7 0.8 0.9 1.0<br>Test balanced accuracy<br>random cut-off 84.61%<br>Number of CAVs<br><!-- End of picture text -->

Figure 3. Concept learning performances. The middle line indicates the cut-off at 70% accuracy, the right line is the mean accuracy of the remaining CAVs. 

## 5.3 Hierarchy Mining 

We conduct a three-fold evaluation of our proposed hierarchy extraction method (section 4) in order to evaluate goal 3: structure; ground-truth comparison; alignment with other sources of concept similarities. 

## 5.3.1 Structure priors 

We first provide evidence supporting our choice to extract a hierarchical tree graph over other choices of structures. Though we do not have access to a ground-truth graph of the relations between concepts in CD, we have some priors on what a satisfying result should be like. For instance, we know that musical concepts are often blended (e.g. genres). It is thus safe to assume that a good graph of concepts should be connected. Extending this property, isolated nodes should strongly be discouraged. As another prior assumption on our target graph, we know that we can usually find several similar playlists to a given one, but that very strongly connected nodes should be infrequent, sparsity should thus also be valued. 

With these two priors in mind, we inspect various graph baselines that could straightforwardly be obtained from VD without our hierarchy extraction step: the similarity graph A(VD) from equation (2); a similarity graph obtained from S(VD) with an adjusted threshold to match the sparsity of H(S(VD)) (Sparse A); a top-1 most similar neighbours graph of each node; reference random graphs. Their respective sparsity and connectivity is shown in Table 2. It appears that baseline graphs become disconnected as soon as sparsity drops. We also underline that random baselines provide better-behaved graphs than their counterparts, indicating that similarity links are not evenly distributed among nodes, thus pointing to the existence of communities in the graph that justifies the use of betweenness [67]. Using a hierarchy extraction algorithm helps maintain a low sparsity while connecting every node in the graph. 

|Graph|#Edges(↓)|#CC(↓)|#IN(↓)|
|---|---|---|---|
|H (proposed)<br>|3442(0.03%)|1|0|
|A(VD)|1309163 (11%)|1|0|
|SparseA|3443|2766|2735|
|Top-1|3443|134|0|
|Random SparseA|3443|516|430|
|Random Top-1|3443|7|0|



Table 2. Structure evaluation. We count the number of edges in each graph, of connected components (CC), and of isolated nodes (IN). Lower is better. 

431 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

This study does not prevent using sparse and connected graphs other than hierarchies. We believe that other relevant structures may exist. Nonetheless, as additional benefits of using hierarchies, we note that tree-like graphs are always planar, which eases their visualisation and navigability by having only one most-relevant parent per node. 

## 5.3.2 Ground-truth evaluation 

To validate our generated concept hierarchy, we compare H(S(Vmood)) and H(S(Vgenre)) to the expert tag hierarchy provided with the APM dataset ± which is unavailable for VD. As those hierarchies are two-levelled ± i.e. clustering of tags, we evaluate the accuracy of the mined edges at linking neighbours from the same cluster and compute a silhouette score [68]. Judging from the results given in Table 3, the generation is promising but far from perfect. 

The estimated hierarchy of genres is illustrated in Figure 1(c) to help interpret the results. As a typical failure case, the orange cluster ("Electronica") ends up in two separate branches, which can happen because of the greedy construction of our hierarchy. In other cases, however, the ground-truth may be questioned: "Latin influence", "Latin", "Ethnic Dance" and "Calypso" form a link in our hierarchy, but belong to four different clusters in the ground-truth ± due to non-musical taxonomic considerations ± despite being musically similar. It is not easy to quantify the performance upper-bound we have between our musical concept detection and the practical expert taxonomies we compare to. Nevertheless, seeing that our generated hierarchies roughly align with ground-truth structures is a good sanity check. 



<!-- Start of picture text -->
Ta g s Accurac y ( % ) Silhouette<br>Hmood 45.1 -0.09 ± 0.05<br>H g enre 49.1 -0.17 ± 0.04<br><!-- End of picture text -->

Table 3. Evaluation of our unsupervised hierarchy against ground-truth clustering of moods and genres tags. 

## 5.3.3 Alignment to various sources 

Coming back to the difficult setting of VD, we finally evaluate our hierarchy of concepts with mixed types, illustrated in Figure 2. As we do not have a ground-truth in this general case, we evaluate whether the edges of our hierarchy ± built from S(V) ± make sense on other sources of similarity. Specifically, since our data is collected from a streaming service, collaborative filtering embeddings [69] based on listening logs are available to estimate playlist similarities (SCF). Playlists similar in concepts could indeed be expected to be co-listened by users, though popularity biases are also at play. We also leverage playlist titles and expect neighbours to be rather close semantically. To that end, we use a large language model [70] that can embed any text prompt (SBERT), and two music-specialised word embedders for which we average representations of in-vocabulary words of each concept names: SW2V-1 [9] and SW2V-2 [71]. For reference, we generate hierarchies from each domainspecific source, include a random hierarchy, and a Audio 

measure based on CAVs weights, following our observations made in section 3.4. 

We compute the average similarity on each hierarchy’s edges given those several sources of similarities. Results are provided in Table 1. By construction, each hierarchy maximises performance on the source it was built on. We rather inspect how one source of knowledge transfers to other sources. Collaborative filtering being the canonical way of estimating similarities in the streaming industry our dataset is extracted from and in general [45], we underline that our hierarchy ± solely based on audio ± closely matches its transfer performances, which is a good result<sup>4</sup> . We have thus shown that our hierarchy transfers to other sources of knowledge (goal 3). 

## 5.4 Qualitative discussion 

We retrieve many associations that make sense for humans in H(S(VD)): blues and jazz; rock and pop; motivation, dancing, running, and party are close to one another ± which aligns with previous work [72]. More interestingly, we observe that "LSD Trip" is the parent of "Surf", "Summer of love", and "Stoner Rock", effectively associating an activity to a sport, an historic phenomenon, and a music genre. Yet, we also find some association that make sense for the model but not for humans: e.g. "Rock Christmas" is also a child of "LSD Trip". This phenomenon is hard to avoid with fully unsupervised methods [53,73]. We can find many more interesting associations, but we have to beware of confirmation biases, as often in XAI [51, 52, 74]. We provide online visualisations of the results<sup>5</sup> . 

As observable limitations, VD is biased by the streaming platform usage towards French, English, and Brazilian content, which could be addressed in future work with importance sampling. Then, some concept titles are misleading, e.g. playlists "City sounds: <city>" are confounded by the taste of their curator, resulting in city concepts being close to the 60’s genre, despite this not being obvious solely judging from the title. Finally, as already mentioned, the backbone fails to discriminate linguistic information: e.g. "Queer Pop" and "[Current] Pop" differ by their lyric theme but are neighbours in the hierarchy. 

## 6. CONCLUSION 

Spectrograms are hard to interpret. We propose to extend concept learning to learn hierarchies of music concepts from playlists, with greater flexibility than usual music taggers. Our results should be viewed as complementary to expert music ontologies, as a means to witness how music is organically described by users and editors, and thus to capture new or evolving salient aspects of music. 

This topic is novel and further steps are necessary in order to overcome cultural biases of our data, and to discover causal relations for our structure. Future work include leveraging the found hierarchy for dynamic music recommendation ± e.g. exploring and switching branches. 

> 4 Why not use CF embeddings then? As a reminder, they are tied to the dataset, and thus fail goal 2. They are only used for comparison. 

> 5 research.deezer.com/concept_hierarchy/ 

432 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

## 7. REFERENCES 

- [1] A. Liberman, F. S. Cooper, D. P. Shankweiler, and M. Studdert-Kennedy, ªWhy are speech spectrograms hard to read?º American Annals of the Deaf, pp. 127± 133, 1968. 

- [2] M. Won, S. Chun, and X. Serra, ªVisualizing and understanding self-attention based music tagging,º Machine Learning for Music Discovery Workshop, ICML, 2019. 

- [3] B. Kim, M. Wattenberg, J. Gilmer, C. Cai, J. Wexler, F. Viegas, and R. sayres, ªInterpretability beyond feature attribution: Quantitative testing with concept activation vectors (TCAV),º in International Conference on Machine Learning (ICML). PMLR, 2018, pp. 2668±2677. 

- [4] C.-K. Yeh, B. Kim, and P. Ravikumar, ªHumancentered concept explanations for neural networks,º in Neuro-Symbolic Artificial Intelligence: The State of the Art, vol. 342, 2022, pp. 337±352. 

- [5] A. Ghandeharioun, B. Kim, C.-L. Li, B. Jou, B. Eoff, and R. W. Picard, ªDissect: Disentangled simultaneous explanations via concept traversals,º International Conference on Learning Representations (ICLR), 2022. 

- [6] C. J. Cai, E. Reif, N. Hegde, J. Hipp, B. Kim, D. Smilkov, M. Wattenberg, F. Viegas, G. S. Corrado, M. C. Stumpe et al., ªHuman-centered tools for coping with imperfect algorithms during medical decisionmaking,º in CHI conference on human factors in computing systems, 2019, pp. 1±14. 

- [7] P. Arendsen, D. Marcos, and D. Tuia, ªConcept discovery for the interpretation of landscape scenicness,º Machine Learning and Knowledge Extraction, vol. 2, no. 4, pp. 397±413, 2020. 

- [8] R. Hennequin, J. Royo-Letelier, and M. Moussallam, ªAudio based disambiguation of music genre tags,º International Society of Music Information Retrieval Conference (ISMIR), 2018. 

- [9] S. Doh, J. Lee, T. H. Park, and J. Nam, ªMusical word embedding: Bridging the gap between listening contexts and music,º ICML Workshop: Machine Learning for Music Discovery, 2020. 

- [10] E. M. Von Hornbostel and C. Sachs, ªClassification of musical instruments: Translated from the original german by anthony baines and klaus p. wachsmann,º The Galpin Society Journal, pp. 3±29, 1961. 

- [11] M. AntoviÂc, ªFrom expectation to concepts: Toward multilevel grounding in musical semantics,º Cognitive Semiotics, vol. 9, no. 2, pp. 105±138, 2016. 

- [12] N. Kumar, A. C. Berg, P. N. Belhumeur, and S. K. Nayar, ªAttribute and simile classifiers for face verification,º in 12th International Conference on Computer Vision (ICCV). IEEE, 2009, pp. 365±372. 

- [13] C. H. Lampert, H. Nickisch, and S. Harmeling, ªLearning to detect unseen object classes by between-class attribute transfer,º in Conference on Computer Vision and Pattern Recognition (CVPR). IEEE, 2009, pp. 951±958. 

- [14] P. W. Koh, T. Nguyen, Y. S. Tang, S. Mussmann, E. Pierson, B. Kim, and P. Liang, ªConcept bottleneck models,º in International Conference on Machine Learning (ICML). PMLR, 2020, pp. 5338±5348. 

- [15] C. Chen, O. Li, D. Tao, A. Barnett, C. Rudin, and J. K. Su, ªThis looks like that: deep learning for interpretable image recognition,º Advances in Neural Information Processing Systems (NeurIPS), vol. 32, 2019. 

- [16] B. Zhou, Y. Sun, D. Bau, and A. Torralba, ªInterpretable basis decomposition for visual explanation,º in European Conference on Computer Vision (ECCV), 2018, pp. 119±134. 

- [17] A. Lucieri, M. N. Bajwa, S. A. Braun, M. I. Malik, A. Dengel, and S. Ahmed, ªOn interpretability of deep learning based skin lesion classifiers using concept activation vectors,º in International Joint Conference on Neural Networks (IJCNN). IEEE, 2020, pp. 1±10. 

- [18] A. R. Asokan, N. Kumar, A. V. Ragam, and S. S. Sharath, ªInterpretability for multimodal emotion recognition using concept activation vectors,º arXiv preprint arXiv:2202.01072, 2022. 

- [19] C. Göpfert, Y. Chow, C.-w. Hsu, I. Vendrov, T. Lu, D. Ramachandran, and C. Boutilier, ªDiscovering personalized semantics for soft attributes in recommender systems using concept activation vectors,º The Web Conference (WWW), 2022. 

- [20] A. Ghorbani, J. Wexler, J. Y. Zou, and B. Kim, ªTowards automatic concept-based explanations,º Advances in Neural Information Processing Systems (NeurIPS), vol. 32, 2019. 

- [21] Z. Chen, Y. Bei, and C. Rudin, ªConcept whitening for interpretable image recognition,º Nature Machine Intelligence, vol. 2, no. 12, pp. 772±782, 2020. 

- [22] E. Strumbelj and I. Kononenko, ªAn efficient explanation of individual classifications using game theory,º The Journal of Machine Learning Research, vol. 11, pp. 1±18, 2010. 

- [23] C.-K. Yeh, B. Kim, S. Arik, C.-L. Li, T. Pfister, and P. Ravikumar, ªOn completeness-aware conceptbased explanations in deep neural networks,º Advances in Neural Information Processing Systems (NeurIPS), vol. 33, pp. 20 554±20 565, 2020. 

433 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

- [24] Y. Goyal, A. Feder, U. Shalit, and B. Kim, ªExplaining classifiers with causal concept effect (cace),º arXiv preprint arXiv:1907.07165, 2019. 

- [25] H. F. Garcia, A. Aguilar, E. Manilow, and B. Pardo, ªLeveraging hierarchical structures for few-shot musical instrument recognition,º International Society of Music Information Retrieval Conference (ISMIR), 2021. 

- [26] D. M. Blei, A. Y. Ng, and M. I. Jordan, ªLatent dirichlet allocation,º Journal of machine Learning research, vol. 3, no. Jan, pp. 993±1022, 2003. 

- [27] T. Griffiths, M. Jordan, J. Tenenbaum, and D. Blei, ªHierarchical topic models and the nested chinese restaurant process,º Advances in Neural Information Processing Systems (NIPS), vol. 16, 2003. 

- [28] V.-A. Nguyen, J. L. Ying, P. Resnik, and J. Chang, ªLearning a concept hierarchy from multi-labeled documents,º Advances in Neural Information Processing Systems (NIPS), vol. 27, 2014. 

- [29] G. N. Lance and W. T. Williams, ªA general theory of classificatory sorting strategies: 1. hierarchical systems,º The computer journal, vol. 9, no. 4, pp. 373± 380, 1967. 

- [30] X. Liu, Y. Song, S. Liu, and H. Wang, ªAutomatic taxonomy construction from keywords,º in SIGKDD international conference on Knowledge discovery and data mining, 2012, pp. 1433±1441. 

- [31] J. Völker and M. Niepert, ªStatistical schema induction,º in Extended Semantic Web Conference. Springer, 2011, pp. 124±138. 

- [32] V. Anoop, S. Asharaf, and P. Deepak, ªUnsupervised concept hierarchy learning: a topic modeling guided approach,º Procedia computer science, vol. 89, pp. 386±394, 2016. 

- [33] P. Heymann and H. Garcia-Molina, ªCollaborative creation of communal hierarchical taxonomies in social tagging systems,º Stanford, Tech. Rep., 2006. 

- [34] D. Benz, A. Hotho, and G. Stumme, ªSemantics made by you and me: Self-emerging ontologies can capture the diversity of shared knowledge,º in Web Science Conference (WebSci09), 2010. 

- [35] A. Ross and F. Doshi-Velez, ªBenchmarks, algorithms, and metrics for hierarchical disentanglement,º in International Conference on Machine Learning (ICML). PMLR, 2021, pp. 9084±9094. 

- [36] R. Jenatton, J. Mairal, G. Obozinski, and F. R. Bach, ªProximal methods for sparse hierarchical dictionary learning,º in International Conference on Machine Learning (ICML), 2010. 

- [37] E. Bart, I. Porteous, P. Perona, and M. Welling, ªUnsupervised learning of visual taxonomies,º in Conference on Computer Vision and Pattern Recognition (CVPR). IEEE, 2008, pp. 1±8. 

- [38] P. Hase, C. Chen, O. Li, and C. Rudin, ªInterpretable image recognition with hierarchical prototypes,º in AAAI Conference on Human Computation and Crowdsourcing, vol. 7, 2019, pp. 32±40. 

- [39] F. Doshi-Velez and B. Kim, ªTowards a rigorous science of interpretable machine learning,º arXiv preprint arXiv:1702.08608, 2017. 

- [40] J. Adebayo, J. Gilmer, M. Muelly, I. Goodfellow, M. Hardt, and B. Kim, ªSanity checks for saliency maps,º Advances in neural information processing systems (NeurIPS), 2018. 

- [41] Z. C. Lipton, ªThe mythos of model interpretability: In machine learning, the concept of interpretability is both important and slippery.º Queue, vol. 16, no. 3, pp. 31±57, 2018. 

- [42] D. Janzing, L. Minorics, and P. Blöbaum, ªFeature relevance quantification in explainable ai: A causal problem,º in International Conference on artificial intelligence and statistics. PMLR, 2020, pp. 2907±2916. 

- [43] A. Mahinpei, J. Clark, I. Lage, F. Doshi-Velez, and P. Weiwei, ªPromises and pitfalls of black-box concept learning models,º ICML Workshop on Theoretic Foundation, Criticism, and Application Trend of Explainable AI, 2021. 

- [44] S. Krishna, T. Han, A. Gu, J. Pombra, S. Jabbari, S. Wu, and H. Lakkaraju, ªThe disagreement problem in explainable machine learning: A practitioner’s perspective,º arXiv preprint arXiv:2202.01602, 2022. 

- [45] D. Afchar, A. B Melchiorre, M. Schedl, R. Hennequin, E. V. Epure, and M. Moussallam, ªExplainability in music recommender systems,º in AI Magazine, 2022. 

- [46] R. Geirhos, J.-H. Jacobsen, C. Michaelis, R. Zemel, W. Brendel, M. Bethge, and F. A. Wichmann, ªShortcut learning in deep neural networks,º Nature Machine Intelligence, vol. 2, no. 11, pp. 665±673, 2020. 

- [47] A. B. Arrieta, N. Díaz-Rodríguez, J. Del Ser, A. Bennetot, S. Tabik, A. Barbado, S. García, S. Gil-López, D. Molina, R. Benjamins et al., ªExplainable artificial intelligence (xai): Concepts, taxonomies, opportunities and challenges toward responsible ai,º Information Fusion, vol. 58, pp. 82±115, 2020. 

- [48] D. Afchar, V. Guigue, and R. Hennequin, ªTowards rigorous interpretations: a formalisation of feature attribution,º in International Conference on Machine Learning (ICML). PMLR, 2021, pp. 76±86. 

434 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

- [49] P. Hase, H. Xie, and M. Bansal, ªThe out-ofdistribution problem in explainability and search methods for feature importance explanations,º Advances in Neural Information Processing Systems (NeurIPS), vol. 34, 2021. 

- [50] D. Slack, S. Hilgard, E. Jia, S. Singh, and H. Lakkaraju, ªFooling lime and shap: Adversarial attacks on post hoc explanation methods,º in AAAI/ACM Conference on AI, Ethics, and Society, 2020, pp. 180±186. 

- [51] H. Kaur, H. Nori, S. Jenkins, R. Caruana, H. Wallach, and J. Wortman Vaughan, ªInterpreting interpretability: understanding data scientists’ use of interpretability tools for machine learning,º in CHI conference on human factors in computing systems, 2020, pp. 1±14. 

- [52] J. Dinu, J. Bigham, and J. Z. Kolter, ªChallenging common interpretability assumptions in feature attribution explanations,º NeurIPS Workshop: ML Retrospectives, Surveys & Meta-Analyses (ML-RSA), 2020. 

- [53] F. Locatello, S. Bauer, M. Lucic, G. Raetsch, S. Gelly, B. Schölkopf, and O. Bachem, ªChallenging common assumptions in the unsupervised learning of disentangled representations,º in International Conference on Machine Learning (ICML). PMLR, 2019, pp. 4114± 4124. 

- [54] L. Sixt, M. Schuessler, O.-I. Popescu, P. Weiû, and T. Landgraf, ªDo users benefit from interpretable vision? a user study, baseline, and dataset,º in International Conference on Learning Representations (ICLR), 2022. 

- [55] C. Rudin, C. Chen, Z. Chen, H. Huang, L. Semenova, and C. Zhong, ªInterpretable machine learning: Fundamental principles and 10 grand challenges,º Statistics Surveys, 2021. 

- [56] H. Chen, J. D. Janizek, S. Lundberg, and S.-I. Lee, ªTrue to the model or true to the data?º ICML Workshop on Human Interpretability in Machine Learning, 2020. 

- [57] J. Pearl, ªCausal inference in statistics: An overview,º Statistics Surveys, vol. 3, pp. 96 ± 146, 2009. 

- [58] S. Bozinovski and A. Fulgosi, ªThe influence of pattern similarity and transfer of learning upon training of a base perceptron b2.(original in croatian: Utjecaj slicnosti likova i transfera ucenja na obucavanje baznog perceptrona b2),º in Proc. Symp. Informatica, 1976, pp. 3±121. 

- [59] O. Celma, P. Herrera, and X. Serra, ªBridging the music semantic gap,º International Semantic Web Conference, 2006. 

- [60] J. Spijkervet and J. A. Burgoyne, ªContrastive learning of musical representations,º International Society of Music Information Retrieval Conference (ISMIR), 2021. 

- [61] J. Pons and X. Serra, ªmusicnn: Pre-trained convolutional neural networks for music audio tagging,º Late breaking/demo session of the International Society for Music Information Retrieval Conference (LBDISMIR), 2019. 

- [62] T. Bertin-Mahieux, D. P. Ellis, B. Whitman, and P. Lamere, ªThe million song dataset,º in International Conference on Music Information Retrieval (ISMIR), 2011. 

- [63] T. Lombrozo, ªExplanatory preferences shape learning and inference,º Trends in Cognitive Sciences, vol. 20, no. 10, pp. 748±759, 2016. 

- [64] T. Miller, ªExplanation in artificial intelligence: Insights from the social sciences,º Artificial intelligence, vol. 267, pp. 1±38, 2019. 

- [65] S. P. Borgatti and M. G. Everett, ªA graph-theoretic perspective on centrality,º Social networks, vol. 28, no. 4, pp. 466±484, 2006. 

- [66] B. Gao, E. Dellandréa, and L. Chen, ªMusic sparse decomposition onto a midi dictionary of musical words and its application to music mood classification,º in International Workshop on Content-Based Multimedia Indexing (CBMI). IEEE, 2012, pp. 1±6. 

- [67] M. Girvan and M. E. Newman, ªCommunity structure in social and biological networks,º Proceedings of the national academy of sciences, vol. 99, no. 12, pp. 7821±7826, 2002. 

- [68] P. J. Rousseeuw, ªSilhouettes: a graphical aid to the interpretation and validation of cluster analysis,º Journal of computational and applied mathematics, vol. 20, pp. 53±65, 1987. 

- [69] Y. Hu, Y. Koren, and C. Volinsky, ªCollaborative filtering for implicit feedback datasets,º in International Conference on Data Mining. IEEE, 2008, pp. 263± 272. 

- [70] N. Reimers and I. Gurevych, ªSentence-bert: Sentence embeddings using siamese bert-networks,º in Conference on Empirical Methods in Natural Language Processing. ACL, 2019. 

- [71] M. Won, S. Oramas, O. Nieto, F. Gouyon, and X. Serra, ªMultimodal metric learning for tag-based music retrieval,º in International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2021, pp. 591±595. 

- [72] K. M. Ibrahim, J. Royo-Letelier, E. V. Epure, G. Peeters, and G. Richard, ªAudio-based auto-tagging with contextual tags for music,º in International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2020, pp. 16±20. 

435 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

- [73] F. Dalvi, A. R. Khan, F. Alam, N. Durrani, J. Xu, and H. Sajjad, ªDiscovering latent concepts learned in bert,º in International Conference on Learning Representations (ICLR), 2022. 

- [74] R. S. Nickerson, ªConfirmation bias: A ubiquitous phenomenon in many guises,º Review of General Psychology, vol. 2, no. 2, pp. 175±220, 1998. 

436 

