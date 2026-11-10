---
paper_id: "000105"
year: 2022
title: "Download pdf"
source_url: "https://zenodo.org/record/7316804/files/000105.pdf"
---

# CONCEPT-BASED TECHNIQUES FOR ªMUSICOLOGIST-FRIENDLYº EXPLANATIONS IN A DEEP MUSIC CLASSIFIER 

Francesco Foscarin<sup>1∗</sup> 

Katharina Hoedt<sup>1∗</sup> Verena Praher<sup>1∗</sup> 

Arthur Flexer<sup>1</sup> Gerhard Widmer<sup>1,2</sup> 

1 Institute of Computational Perception, Johannes Kepler University Linz, Austria 2 LIT AI Lab, Linz Institute of Technology, Austria 

{firstname}.{lastname}@jku.at 

## ABSTRACT 

Current approaches for explaining deep learning systems applied to musical data provide results in a low-level feature space, e.g., by highlighting potentially relevant timefrequency bins in a spectrogram or time-pitch bins in a piano roll. This can be difficult to understand, particularly for musicologists without technical knowledge. To address this issue, we focus on more human-friendly explanations based on high-level musical concepts. Our research targets trained systems (post-hoc explanations) and explores two approaches: a supervised one, where the user can define a musical concept and test if it is relevant to the system; and an unsupervised one, where musical excerpts containing relevant concepts are automatically selected and given to the user for interpretation. We demonstrate both techniques on an existing symbolic composer classification system, showcase their potential, and highlight their intrinsic limitations. 

## 1. INTRODUCTION 

The mass adoption of deep learning methods in recent years has increased interest in the field of explainability,<sup>1</sup> i.e., the study of techniques that generate a human-understandable explanation of a model’s decision [1]. As deep learning models are usually not intrinsically interpretable, techniques that can be applied to trained models (i.e., post-hoc methods) are of great interest. The resulting explanations cannot only reveal potential issues of the system itself and the data it uses, but can also provide insights into the problem we are targeting, thus helping us to gain knowledge about it [2]. 

Higher-level musical tasks such as chord transcription or composer classification may require explanations that can only be understood by persons with advanced musical 

* Equal contribution. 

1 Considered synonymous to the term interpretability in this paper. 

> © F. Foscarin, K. Hoedt, V. Praher, A. Flexer, and G. Widmer. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: F. Foscarin, K. Hoedt, V. Praher, A. Flexer, and G. Widmer, ªConcept-Based Techniques for ªMusicologist-friendlyº Explanations in a Deep Music Classifierº, in Proc. of the 23rd Int. Society for Music Information Retrieval Conf., Bengaluru, India, 2022. 

expertise. However, the explanation techniques for musical systems that have been proposed in recent years [3±7] are feature-based, i.e., the explanation is given in terms of the input features the system considers. Typical input features for musical systems, e.g., spectrograms or piano roll representations, are high-dimensional, and, since the importance of a single time frequency / pitch bin does not convey much meaningful interpretation, feature-based explanations can be hard to understand.<sup>2</sup> Musicologists are therefore often unable to analyse the results of trained systems, let alone contribute to the development of new learning models. This motivates research on techniques that provide explanations that are as similar as possible to those that a human music domain expert would naturally use. 

Concept-based explanations offer an interesting direction. They were first explored by Kim et al. [12] and later developed in several works (e.g., by Chen et al. [13]) for image systems, which also use high-dimensional input features. Instead of producing feature-level descriptors, the explanation is based on human-understandable concepts. For example, [12] tests whether the concept of ªstripesº would increase the probability that an image classifier labels an image as ªzebraº. Music can also be described with musical concepts; terms such as ªdiatonic sequenceº, ªalberti bassº, ªdifficult-to-play musicº, ªorchestral musicº, ªrubatoº, ªshuffle drum beatº, ªfunky bass lineº, etc. are used to describe pieces or specific elements in a piece. 

In this paper, we explore two concept-based techniques to explain deep learning systems that deal with musical data: one supervised and one unsupervised. The first (see Section 4) is based on Testing with Concept Activation Vectors (TCAV) [12]: the user defines a concept by providing examples and interrogates the system to find out if the concept is relevant or not for its decision. This can be applied to any kind of neural network and, even more generally, to any system that has a hidden layer for which we can compute directional derivatives. The second technique, described in Section 5, is an adaptation of [14] and works in an unsupervised fashion, where the most relevant concepts are automatically produced and given to the user for interpretation. Each concept is presented in the form of a set of musical excerpts. This approach requires networks whose hidden layers contain only non-negative values and 

2 Moreover, their truthfulness has recently been debated [8±11]. 

876 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

have a spatial correlation with the input data, two conditions that are satisfied by most Convolutional Neural Networks (CNNs). 

Our contributions are: the first application of conceptbased post-hoc approaches to musical data, in particular, we target the composer classification system of Kim et al. [15] that uses piano roll representations of piano MIDI files as input; the definition and creation of musical concept datasets; a dedicated visualisation of unsupervised concepts for symbolic music data; and, finally, the exploration of the Non-negative Tucker Decomposition (NTD) for the factorisation of hidden layers. Our code and data are available on Github.<sup>3</sup> 

## 2. RELATED WORK 

Recent work in the field of Music Information Retrieval (MIR) that focus on explainability for deep models consists mainly of feature-based post hoc methods (e.g., [3±5,7]). Chowdhury et al. introduce pre-defined ªmid-level featuresº that could be considered concepts as intermediate targets in a two-level prediction model [16]. Related to this, approaches that consider instrinsic as opposed to post-hoc methods gain increasing attention in the audio domain as well (e.g., [17±19]). However, no prior studies have examined post-hoc concept-based explainability techniques on systems that work with musical data. To provide a technical context for our work, we focus on related approaches that work on audio or image data. 

A recent approach [20] applies concept-based techniques to multimodal data (video, audio, and text) to explain an emotion classifier for video sequences of human conversations. For the audio signal, they only test the concept of ªvoice pitchº, i.e., the averaged fundamental frequency of the speaker’s voice. In another related study, Parekh et al. [21] learn a codebook of sounds (e.g., alarm sound) from input audio through Non-negative Matrix Factorisation (NMF), which is then used to obtain hidden network layer representations that indicate time activations of these pre-learnt components. This has some similarities with our unsupervised approach, as we also make use of nonnegative factorisation techniques to disentangle concepts. However, while [21] performs the factorisation on the input and propagates the results to a hidden layer, we factorise the hidden layer activations and project the results back to the input data. The approach of [21] is promising if we assume that the underlying reason for a system decision can be extracted directly from the input with unsupervised separation approaches. However, since this might not always be the case, we factorise the layer activations to exploit the non-linear feature extraction a network does internally to obtain more meaningful explanations. 

Our work uses techniques and results originally proposed for the image domain. The work of Kim et al. [12] provides the basis for the supervised explanation, although the creation of concept data sets is more challenging for music. We base the unsupervised explanation on the work 

> 3 https://github.com/CPJKU/composer_concept 

of Zhang et al. [14], but propose a dedicated visualisation of piece excerpts and test different solutions for the tensor factorisation step by employing the NTD. 

## 3. EXPERIMENTAL SETUP 

This section details the type of data and the system that we use to demonstrate our explainability techniques. 

Data: We use MIDI representations of piano performances from the MAESTRO v2.0.0 dataset [22]. As proposed by Kim et al. [15], we pre-select data by composers with at least 16 pieces and remove files with more than one composer (e.g., Schubert/Liszt, ªDer Mueller und der Bachº), so that pieces of 13 different composers remain (see Table 1). We randomly split the resulting 667 pieces in a training (462 pieces) and validation (205 pieces) set. For each piece, we sample 90 excerpts of 20 seconds randomly across time and different performances of the same piece (if available). 

Composer Classifier: In this work, we investigate the composer classification system proposed by Kim et al. [15]. For more recent systems, the code was not available [23] or we were unable to reproduce their results [24]. During preprocessing, we transform MIDI excerpts into piano roll representations with a 50 ms time step, i.e., a matrix 88 × 400, which is used as input to a ResNet-50 [25]. Kim et al. [15] use an additional channel with onset information, which we omit because it does not improve the performance of our system. As proposed by [15], we train the network with Stochastic Gradient Descent with momentum (factor 0.9), L2 weight regularisation (factor 0.0001), and crossentropy loss function. The initial learning rate is set to 0.01, and scheduled with cosine annealing [26]. Our attempt to retrain the system results in a F1 score of 0.93 compared to 0.83 in the original work [15]. The accuracy of our system is 0.93. The difference in performance could be attributed to a problem during preprocessing in the original code, which reduced the resolution of the piano roll. 

## 4. SUPERVISED CONCEPT-BASED EXPLANATIONS 

In this section, we use TCAV [12] to build a supervised concept-based explainer. We manually define musical concepts and interrogate a music classifier to find out how much a concept influences the results of the classifier. 

## 4.1 Musical Concepts 

Musical concepts describe the characteristics of a certain group of notes and are identified by musicologists with a specific name or with a small sentence (e.g., ªstaccatoº, ªrubatoº, ªmelody with jumpsº, etc.). To define a musical concept in a way that can be used within our system, we construct concept datasets, i.e., sets of pieces that have one specific musical concept in common. In this paper, we build three different concept datasets, each consisting of 30 musical excerpts of ~25 seconds. Ideally, the bigger and more diverse the concept datasets is, the lower is the probability that it will also represent other unwanted concepts. 

877 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

The first dataset describes the ªalberti bassº: an accompaniment pattern first used during the classical period, where notes of chords are horizontally distributed in the left hand part [27]. For this dataset a semi-professional pianist composed ~25 second excerpts that contain this pattern, while trying to vary as much as possible other musical elements (e.g., key, tempo, content of the right hand). 

The second concept is ªdifficult-to-play musicº. A dataset of difficult musical excerpts was collected using the ranking produced by the musical score publisher G. Henle.<sup>4</sup> Excerpts were sampled from difficult pieces available in the MAESTRO dataset among different composers to avoid introducing biases toward some of them. 

The third concept is ªcontrapuntal textureº, which denotes piano pieces composed of multiple monophonic voices that behave as separate instruments. This style is mostly present in pieces by some Baroque composers (e.g., Bach, Telemann, Händel, Buxtehude). For this dataset, we sampled Bach fugue performances, ensuring that they were not used during training the targeted composer classifier. 

In addition to these three concept datasets, in this paper we use a collection of 10 different random datasets, which are built by randomly sampling 20 second excerpts from the MAESTRO dataset. 

## 4.2 CAVs and Conceptual Sensitivity 

A Concept Activation Vector (CAV) [12] vl<sup>krepresentsa</sup> concept k in the output space of a neural network layer l. To compute it, we need the corresponding concept dataset (containing e.g., pieces with alberti bass) and a random dataset [12]. For a specific network layer l, we compute the layer activations (i.e., the output of the layer) for every piano roll x in the concept dataset, as well as the random dataset (see Figure 1). These activations can be seen as points in a (H × W × C)-dimensional space, where H, W, C are the horizontal, vertical, and channel size in the layer activations tensor. We train a binary linear classifier (e.g., Support Vector Machine (SVM) or logistic regression) that separates the layer activations of the concept pieces from those of the random pieces. The vector of coefficients of this binary classifier, i.e., the vector orthogonal to the classification boundary, is the CAV vl<sup>k[12].</sup> 

To measure whether a concept k is relevant for a piece being classified as a certain composer o, we use the conceptual sensitivity Sk,o,l of the system [12], i.e., the directional derivative of the prediction in the direction of the CAV, 



<!-- Start of picture text -->
Sk,o,l = ∇gl,o(fl(x)) · vl k. (1)<br><!-- End of picture text -->

Here, gl,o transforms the activation vector fl(x) to the logit for the output class o, that is, it represents the remaining computations after a layer l up to the output of the system. Intuitively, S is a scalar that measures how much the output logits change if we perturb the layer activations in the direction of the CAV. Positive values mean that a concept k encourages the classification of x as class o. 

> 4 https://www.henle.de/us/about-us/ levels-of-difficulty-piano/ 



<!-- Start of picture text -->
Output gl(fi(x))<br>NN<br>layer l<br>H<br>Layer activations<br>fi(x)<br>layer 1<br>_<br>_<br>二<br>Pianoroll x<br><!-- End of picture text -->

Figure 1. Layer l activations for one piece excerpt. H, W and C are the horizontal, vertical, and channel size. The function encoded by the neural network is represented in two parts: fl from the NN input to the layer output, and gl from the layer output to the NN output. 

The conceptual sensitivity is a local explanation, i.e., it explains how a system behaves for a specific input. We produce a global explanation, the TCAV score, that no longer depends on a specific input, by taking multiple pieces that belong to one class and computing the ratio of pieces for which S is positive [12]. 

## 4.3 Experiments and Results 

To investigate TCAV, we first compute a CAV for every one of our proposed concepts ªalberti bassº, ªdifficult-to-play musicº, and ªcontrapuntal textureº.<sup>5</sup> As a linear classifier that separates the activations of the concept samples from those of the random samples, we use a linear SVM. This approach requires inputs of the same dimension, so we crop or pad all concepts to 20 seconds length (also used during training). Cropping is done by selecting the middle 20 seconds of a MIDI performance; padding adds silence until the appropriate length is reached. 

In the next step, we examine the conceptual sensitivities of all the validation data and compute the TCAV score for all pieces by the same composer, i.e., the relative amount of positive conceptual sensitivities over the pieces. We again need to ensure inputs have the same length as our concepts, so we split every piece into non-overlapping 20 second segments and use all of these for subsequent computations. Although we can compute the TCAV score for any layer of the composer classifier, for brevity we show results of the penultimate layer subsequently, expecting this layer to encode the highest level features, similar to the image domain [28]. To compute TCAV scores, we perform ten runs with ten random datasets [12], and run a two-sided t-test and a Bonferroni correction for all concepts and composers 

> 5 Using https://captum.ai/api/concept.html 

878 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
alberti bass + + + + - - + - - -<br>diff.-to-play music - - - + + + +<br>contrapuntal texture + + - - - -<br>Bach Scarlatti Haydn Mozart Beethoven Schubert Chopin Schumann Liszt Brahms Debussy Scriabin Rachmn.<br><!-- End of picture text -->

Table 1. Summary of TCAV scores for three concepts and the penultimate layer of a composer classifier. ª+º indicate a positive influence of a concept on the classification of a composer, ª-º negative influence. Empty cells show results that fail significance testing, i.e., the concept does not consistently en-/decourage the classification of a certain composer. 

to validate our experiments. We use a significance threshold of α = 0.05/13 (correcting for 13 hypothesis tests). 

In our experiments, the SVM differentiating between concepts and random data has an accuracy greater than 0.9 for all concepts (in most cases, even 1). This means that the activations of the penultimate layer for the concept and the random samples are linearly separable, i.e., the CAV we produce represents the concept it is targeting. The TCAV score results are summarised in Table 1. All cells with ª+º or ª-º show results that pass our statistical significance test, and the remaining (empty) cells show results that fail. The symbol ª+º means that a particular concept appears important for the classification of the corresponding composer (i.e., average TCAV score > 0.5); ª-º that a concept discourages the classification of an input as a certain composer (i.e., average TCAV score < 0.5). 

Table 1 shows both results that we would expect (e.g., alberti bass being relevant for Mozart, contrapuntal texture for Bach), and a few results which seem counter-intuitive (e.g., the model relying on alberti bass for Bach or Brahms ± although one can find examples of such structures also in their works). It is possible that our model mixes the proposed concepts with other confounding ones, e.g., all pieces in the Alberti Bass dataset have also a quite simple harmonic structure. In general, there is no proof that the model understands our proposed concepts similarly to how a human listener would, yet we can make some interesting observations. Remarkably, even an extremely abstract concept such as ªdifficult-to-play musicº might be grasped by our model: Liszt, Scriabin, Rachmaninoff are clear candidates for this attribute. The same applies to the ªcontrapuntal texture". Cases with negative impact (ª-º) should probably be interpreted with care: the fact that the classifier did not consider these concepts relevant for the classification does not necessarily mean that they are not present in the pieces. This could apply in particular to the subtle concept of contrapuntal texture. Also interesting is the case of Scarlatti, who is very much an outsider in classical music, style-wise (ªa freakish if not downright incorrect composerº [29]) and could not be associated with any of our concepts. 

## 5. UNSUPERVISED CONCEPT-BASED EXPLANATIONS 

The supervised approach requires the user to pre-define concepts. This is very time-consuming, and the user could have to try a potentially infinite number of concepts if the network works differently than expected. In this section, we discuss an unsupervised approach instead: we build an explainer that identifies the relevant concepts and presents pieces where this concept is maximally activated (and some where the concept is not present). The musical expertise of the user is then used to translate these example pieces into a musical concept (with or without a name). 

For the unsupervised approach described below, we introduce two limitations on the target neural network: we assume it to be convolutional and to use a non-negative activation function [30] (e.g., ReLU). 

## 5.1 Tensor Factorisation for CAV Extraction 

Consider a set of layer activations X = {fl(x1), · · · , fl(xN )} generated from multiple pieces x1, . . . , xN . Layer activations that are close together (in terms of Euclidean distance) correspond to perceptually similar inputs [31] and therefore might describe similar concepts within the inputs. We could cluster similar activations and consider the pieces that generate these activations as examples of the same concept [32]. 

This works best if only one concept is present in a piece excerpt. However, we expect an excerpt to contain a number of different musical concepts, e.g., an alberti bass and a legato melody, both following a certain chord progression. Since these concepts can be shared across the same notes, we need a way to disentangle their effects on the layer activations. Due to the restriction on the type of activations (only non-negative) that we introduced in this section, we can use the NTD for this objective (see Section 5.3). 

## 5.2 Channel CAVs 

Given layer activations fl(x), let us consider their channelmode tubes [33], i.e., the vectors obtained by fixing an index h and w for the horizontal and vertical dimension (see lefthand side of Figure 2). In the case of CNNs, we can consider each of these vectors as a different representation of the same piece with a different receptive field [34]. As proposed in [14], we can analyse channel-mode tubes ∈ R<sup>C</sup> instead of full layer activations ∈ R<sup>H×W ×C</sup> . This increases the 

879 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
fi(xp)<br>fi(x1) C-CAVs<br>matrix E<br>Tensor Decompos i ton<br>H<br><!-- End of picture text -->

Figure 2. Left: Channel-mode tubes that result from fixing indices of activations in the W and H dimension of the activation space. Right: C-CAVs extraction from the layer activations of multiple pieces. Each channel tube is decomposed as a weighted sum of C<sup>′</sup> C-CAVs. 

amount of data and reduces the dimension of each data point by a factor of H × W , therefore, we expect that the tensor decomposition that we will run on these data will achieve better results. Since every channel-mode tube represents a piece, we can compute CAVs in this restricted channel space R<sup>C</sup> , and refer to them as Channel-CAVs (or C-CAVs). We can again compute the conceptual sensitivities for such C-CAVs, as explained in Section 4.2. 

We compute C-CAVs by starting from a dataset of pieces (segmented in 20-second excerpts) of the composers we want to explain (any number of composers can be considered). We input each excerpt into the trained system and produce activations for a certain layer l (see Figure 1). The set of all activations can be seen as a tensor X ∈ R<sup>N×H×W ×C</sup> , where N is the number of piece excerpts and H, W and C are the frequency, time, and channel size of the layer activation tensor. We then apply a NTD to X to obtain a set of C-CAVs. 

Moving to a channel-based formulation also permits us to highlight in which part of a piece a certain concept is present: since layer activations have a spatial correlation with input data [35] we can project the position h, w of each C-CAV onto the input piano roll. This creates a concept presence heatmap showing the presence of a C-CAV [14] on a piano roll, which can be visualised to improve the user’s understanding of the concept. Averaging the values in this heatmap gives a number that expresses how much a concept is activated in a certain excerpt and allows a ranking of the pieces according to their average concept presence. 

## 5.3 Non-negative Tucker Decomposition 

The NTD is a technique to decompose a tensor (e.g., X ) into a so-called non-negative core tensor T , and multiple factor matrices A ∈ R<sup>N×N ′</sup> , B ∈ R<sup>H×H′</sup> , D ∈ R<sup>W ×W ′</sup> and E ∈ R<sup>C×C′</sup> (one for every dimension) [33], such that 



<!-- Start of picture text -->
N ′ H ′ W ′ C ′<br>X ≈ tnhwcan ◦ bh ◦ dw ◦ ec (2)<br>∑∑∑∑ n=1 h=1 w=1 c=1<br><!-- End of picture text -->

Here, the core tensor T is in R<sup>N ′×H′×W ′×C′</sup> , and one 

of its scalar elements is denoted by tnhwc. The symbol ª◦º denotes the vector outer product of the column vectors of the (four) factor matrices an, bh, dw, ec. The number of columns of the factor matrices (i.e., the NTD ranks), N<sup>′</sup> , H<sup>′</sup> , W<sup>′</sup> and C<sup>′</sup> are hyper-parameters that can be chosen by the user; if we set them to N<sup>′</sup> = N , H<sup>′</sup> = H, etc., an exact reproduction of the original tensor X is possible [33]. However, we mostly want to set them at lower values (i.e., N<sup>′</sup> << N , H<sup>′</sup> << H, etc.) to decrease the size of the matrices. 

Equation 2 tells us that every channel-mode tube in X can be reconstructed as a weighted sum of the columns of matrix E. As previously mentioned, each channel-mode tube represents a piece (in activation space), and each piece contains a sum of multiple concepts as C-CAVs. Then the C-CAVs we are looking for are disentangled as columns in E (see Figure 2), and their number is specified by rank C’. 

The NTD also allows us to reconstruct an approximation of the original tensor (i.e., the original layer activations), and compute the output of the composer classifier by feeding it back into the network. We can then compute the ratio of the predictions that remain unchanged after the NTD step (i.e., the fidelity) [14] to evaluate its impact on the composer classifier. For more details on NTD, we refer to [33]; in this paper, we use the implementation provided in [36], with the Hierarchical non-negative Alternating Least Squares algorithm to update the factor matrices and the Fast Iterative Shrinkage-Thresholding Algorithm to update the core. 

## 5.4 Experiments and Results 

We compute the unsupervised explanations for the penultimate layer of our composer classification system and test multiple NTD ranks. As in [14], we present each concept to the user through the five piece excerpts with the highest average concept presence. The presentation of piece excerpts is more challenging for musical data than for images. Although symbolic performances can be visualised with piano rolls, some musical elements (e.g., harmonic elements) may be hard to understand in this format. We opt for a mixed audio-image visualisation where each excerpt is represented both with a piano roll (with a colour scale for velocity information) and with a listenable MIDI file. We create interactive piano roll visualisations (using Plotly [37]) in which the user can zoom in and out to explore different resolution levels. The concept presence heatmap is displayed as a semi-transparent mask over the piano roll. A heatmap with a fixed threshold, as proposed in [14], is hard to interpret for our data, so the user is presented with a slider that adapts the heatmap threshold (see Figure 3). We also provide ªcontrastive examplesº for each concept, i.e., the 5 excerpts where the average concept presence is minimal. Although our explainer could find relevant concepts starting from a dataset that includes any number of composers, we focus on the results with only two composers. According to psychological studies [2], explanations are easier to understand when they involve only a small amount of information and when they target contrast cases [1], i.e., understanding why a composer is selected instead of another is easier than 

880 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
average concept presence: 17.59<br>average concept presence: 17.32<br>average concept presence: 16.49<br>20% 40%<br><!-- End of picture text -->

Figure 3. Visualisation of one concept (out of 4 produced by 4d NTD) through the masked piano rolls of the three dataset excerpts with the highest average concept presence. The concept heatmap threshold is set to 60%. This concept has positive conceptual sensitivity for Chopin and negative for Bach, therefore it is useful to distinguish between the two composers. 

understanding why a composer is selected in general. For this reason, we also focus on C-CAVs with opposing conceptual sensitivities, i.e., negative for one class and positive for the other. We experimented with three different nonnegative factorisation approaches: NTD applied to the 4d matrix (as explained in Section 5.3), NTD on a 3d matrix with concatenated horizontal and vertical dimensions, and NMF on a 2d matrix (as proposed by [14]) with concatenated horizontal, vertical, and piece dimension. 

We found that the target classifier, when only two composers are considered, can be approximated with maximum fidelity by using only 3 to 5 C-CAVs, depending on the composers considered. For a fixed number of C-CAVs, we found no clear advantage for one of the three factorisation techniques with respect to the fidelity score. NTD allows for a much higher compression of X , up to 15 times smaller, preserving the same fidelity; but it is also much slower to compute. From a manual analysis, we see that our unsupervised explainer finds, for each opposing concept, examples of typical composing styles that are useful for discriminating between two composers. 

Figure 3 shows an example of what our model considers a typical Chopin-style pattern that is not present in Bach’s music. In musical terms, it might be named ªfast upward or downward movements (in the upper register) in parallel or broken thirds/sixths/octaves". Since our approach is based on non-negative factorisation techniques, some of their typical problems are also present in our results. For example, our system could produce one C-CAV that comprises what musical experts would typically interpret as two different concepts, or vice versa, produce two C-CAVs, both referring to the same concept. The former might have happened with the four small, seemingly unrelated blobs in the lower registers in the last two piano rolls of Figure 3. Furthermore, it is difficult to assign musically meaningful concept names to some C-CAVs, especially those with low average concept presence. 

## 6. CONCLUSION AND FUTURE WORK 

In this paper, we explored a supervised and an unsupervised approach with the aim of producing explanations of deep musical classifiers interpretable by musicologists. In the supervised approach, we define high-level musical concepts (e.g., alberti bass) by building concept datasets and interrogate a classifier to find the relevance of a concept for the classifier decisions. This approach is useful when the user wants to test a specific concept. However, the process of creating a concept dataset can be time-consuming, requires high-level music expertise, and it could be necessary to try many different concepts before finding a relevant one. A solution to these problems is the unsupervised approach, which selects the relevant concepts by itself. Each concept is presented as a set of piece excerpts where the concept is maximally present. The user can listen to those excerpts and visualise them in a piano roll representation with a heatmap highlighting the concept position. 

Future work on the supervised explainer will integrate recent promising results on model non-linearity and stricter hypothesis testing [38]. The unsupervised part will benefit from a formal user-based evaluation by musicologists to see which number of C-CAVs produce the most interpretable musical concepts and if there is agreement on their naming. Sparsity constraints applied to the core tensor and matrices in the NTD may attenuate the non-negative factorisation problems. While both supervised and unsupervised approaches work on piece excerpts of fixed length, an extension to variable length pieces could enable the study of concepts that span a longer time frame (e.g., piece structure). Moreover, our two approaches could be applied to explain audio classifiers, although this would complicate the visualisation of the concept heatmap for the unsupervised explainer, and could make the creation of concept datasets more challenging. Finally, dedicated user interfaces enabling to define concepts and visualise results would be helpful for musicologists. 

881 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

## 7. ACKNOWLEDGEMENTS 

This work was supported by the European Research Council (ERC) under the EU’s Horizon 2020 research & innovation programme, grant agreement No. 101019375 (Whither Music?), the Austrian Science Fund (FWF, project No. P31988), and the Federal State of Upper Austria (LIT AI Lab). 

## 8. REFERENCES 

- [1] T. Miller, ªExplanation in Artificial Intelligence: Insights from the Social Sciences,º Artificial Intelligence, vol. 267, pp. 1±38, 2019. 

- [2] C. Molnar, Interpretable Machine Learning, 2nd ed., 2022. [Online]. Available: https://christophm.github.io/ interpretable-ml-book 

- [3] S. Mishra, B. L. Sturm, and S. Dixon, ªLocal Interpretable Model-agnostic Explanations for Music Content Analysis,º in Proceedings of the 18th International Society for Music Information Retrieval Conference, ISMIR, 2017, pp. 537±543. 

- [4] S. Mishra, E. Benetos, B. L. Sturm, and S. Dixon, ªReliable Local Explanations for Machine Listening,º in Proceedings of the 2020 International Joint Conference on Neural Networks, IJCNN. IEEE, 2020, pp. 1±8. 

- [5] V. Haunschmid, E. Manilow, and G. Widmer, ªaudioLIME: Listenable Explanations Using Source Separation,º in Proceedings of the 13th International Workshop on Machine Learning and Music, MML, 2020, pp. 20±24. 

- [6] ÐÐ, ªTowards Musically Meaningful Explanations Using Source Separation,º CoRR, vol. abs/2009.02051, 2020. 

- [7] A. B. Melchiorre, V. Haunschmid, M. Schedl, and G. Widmer, ªLEMONS: Listenable Explanations for Music recOmmeNder Systems,º in Advances in Information Retrieval: Proceedings of the 43rd European Conference on IR Research, ECIR, vol. 12657. Springer, 2021, pp. 531±536. 

- [8] A. Ghorbani, A. Abid, and J. Y. Zou, ªInterpretation of Neural Networks Is Fragile,º in Proceedings of the 33rd AAAI Conference on Artificial Intelligence, AAAI, 2019, pp. 3681±3688. 

- [9] P. Kindermans, S. Hooker, J. Adebayo, M. Alber, K. T. Schütt, S. Dähne, D. Erhan, and B. Kim, ªThe (Un)reliability of Saliency Methods,º in Explainable AI: Interpreting, Explaining and Visualizing Deep Learning, ser. Lecture Notes in Computer Science. Springer, 2019, vol. 11700, pp. 267±280. 

- [10] J. Adebayo, J. Gilmer, M. Muelly, I. J. Goodfellow, M. Hardt, and B. Kim, ªSanity Checks for Saliency 

   - Maps,º in Advances in Neural Information Processing Systems 31: Proceedings of the 32nd Annual Conference on Neural Information Processing Systems, NeurIPS, 2018, pp. 9525±9536. 

- [11] V. Praher, K. Prinz, A. Flexer, and G. Widmer, ªOn the Veracity of Local, Model-agnostic Explanations in Audio Classification: Targeted Investigations with Adversarial Examples,º in Proceedings of the 22nd International Society for Music Information Retrieval Conference, ISMIR, 2021, pp. 531±538. 

- [12] B. Kim, M. Wattenberg, J. Gilmer, C. J. Cai, J. Wexler, F. B. Viégas, and R. Sayres, ªInterpretability Beyond Feature Attribution: Quantitative Testing with Concept Activation Vectors (TCAV),º in Proceedings of the 35th International Conference on Machine Learning, ICML. PMLR, 2018, pp. 2673±2682. 

- [13] Z. Chen, Y. Bei, and C. Rudin, ªConcept Whitening for Interpretable Image Recognition,º Nature Machine Intelligence, vol. 2, no. 12, pp. 772±782, 2020. 

- [14] R. Zhang, P. Madumal, T. Miller, K. A. Ehinger, and B. I. P. Rubinstein, ªInvertible Concept-based Explanations for CNN Models with Non-negative Concept Activation Vectors,º in Proceedings of the 35th AAAI Conference on Artificial Intelligence, AAAI, 2021, pp. 11 682±11 690. 

- [15] S. Kim, H. Lee, S. Park, J. Lee, and K. Choi, ªDeep Composer Classification Using Symbolic Representation,º ISMIR Late Breaking and Demo Papers, 2020. 

- [16] S. Chowdhury, A. Vall, V. Haunschmid, and G. Widmer, ªTowards Explainable Music Emotion Recognition: The Route via Mid-level Features,º in Proceedings of the 20th International Society for Music Information Retrieval Conference, ISMIR, 2019, pp. 237±243. 

- [17] P. Zinemanas, M. Rocamora, M. Miron, F. Font, and X. Serra, ªAn Interpretable Deep Learning Model for Automatic Sound Classification,º Electronics, vol. 10, no. 7, p. 850, 2021. 

- [18] P. Zinemanas, M. Rocamora, E. Fonseca, F. Font, and X. Serra, ªToward Interpretable Polyphonic Sound Event Detection with Attention Maps Based on Local Prototypes,º in Proceedings of the 6th Workshop on Detection and Classification of Acoustic Scenes and Events, DCASE, 2021, pp. 50±54. 

- [19] Z. Ren, T. T. Nguyen, and W. Nejdl, ªPrototype Learning for Interpretable Respiratory Sound Analysis,º in Proceedings of the 2022 IEEE International Conference on Acoustics, Speech and Signal Processing, ICASSP. IEEE, 2022, pp. 9087±9091. 

- [20] A. R. Asokan, N. Kumar, A. V. Ragam, and S. S. Sharath, ªInterpretability for Multimodal Emotion Recognition using Concept Activation Vectors,º CoRR, vol. abs/2202.01072, 2022. 

882 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

- [21] J. Parekh, S. Parekh, P. Mozharovskyi, F. d’Alché-Buc, and G. Richard, ªListen to Interpret: Post-hoc Interpretability for Audio Networks with NMF,º CoRR, vol. abs/2202.11479, 2022. 

- [22] C. Hawthorne, A. Stasyuk, A. Roberts, I. Simon, C. A. Huang, S. Dieleman, E. Elsen, J. H. Engel, and D. Eck, ªEnabling Factorized Piano Music Modeling and Generation with the MAESTRO Dataset,º in Proceedings of the 7th International Conference on Learning Representations, ICLR, 2019. 

- [23] Q. Kong, K. Choi, and Y. Wang, ªLarge-Scale MIDI-based Composer Classification,º CoRR, vol. abs/2010.14805, 2020. 

- [24] D. Yang and T. Tsai, ªComposer Classification With Cross-Modal Transfer Learning and MusicallyInformed Augmentation,º in Proceedings of the 22nd International Society for Music Information Retrieval Conference, ISMIR, 2021, pp. 802±809. 

- [25] K. He, X. Zhang, S. Ren, and J. Sun, ªDeep Residual Learning for Image Recognition,º in Proceedings of the 2016 IEEE Conference on Computer Vision and Pattern Recognition, CVPR. IEEE Computer Society, 2016, pp. 770±778. 

   - [33] T. G. Kolda and B. W. Bader, ªTensor Decompositions and Applications,º SIAM Review, vol. 51, no. 3, pp. 455±500, 2009. 

   - [34] W. Luo, Y. Li, R. Urtasun, and R. S. Zemel, ªUnderstanding the Effective Receptive Field in Deep Convolutional Neural Networks,º in Advances in Neural Information Processing Systems 29: Proceedings of the 30th Annual Conference on Neural Information Processing Systems, NIPS, 2016, pp. 4898±4906. 

   - [35] J. Dai, K. He, and J. Sun, ªConvolutional Feature Masking for Joint Object and Stuff Segmentation,º in Proceedings of the 2015 IEEE Conference on Computer Vision and Pattern Recognition, CVPR. IEEE Computer Society, 2015, pp. 3992±4000. 

   - [36] J. Kossaifi, Y. Panagakis, A. Anandkumar, and M. Pantic, ªTensorLy: Tensor Learning in Python,º Journal of Machine Learning Research, vol. 20, pp. 26:1±26:6, 2019. 

   - [37] P. T. Inc. (2015) Collaborative Data Science. Montreal, QC. [Online]. Available: https://plot.ly 

   - [38] J. Pfau, A. T. Young, J. Wei, M. L. Wei, and M. J. Keiser, ªRobust Semantic Interpretability: Revisiting Concept Activation Vectors,º CoRR, vol. abs/2104.02768, 2021. 

- [26] I. Loshchilov and F. Hutter, ªSGDR: Stochastic Gradient Descent with Warm Restarts,º in Proceedings of the 5th International Conference on Learning Representations, ICLR, 2017. 

- [27] C. Rosen, The Classical Style: Haydn, Mozart, Beethoven. WW Norton & Company, 1997, no. 653. 

- [28] B. Zhou, A. Khosla, À. Lapedriza, A. Oliva, and A. Torralba, ªObject Detectors Emerge in Deep Scene CNNs,º in Proceedings of the 3rd International Conference on Learning Representations, ICLR, 2015. 

- [29] R. Kirkpatrick, Domenico Scarlatti: Revised Edition. Princeton University Press, 1983, vol. 200. 

- [30] C. Nwankpa, W. Ijomah, A. Gachagan, and S. Marshall, ªActivation Functions: Comparison of trends in Practice and Research for Deep Learning,º CoRR, vol. abs/1811.03378, 2018. 

- [31] R. Zhang, P. Isola, A. A. Efros, E. Shechtman, and O. Wang, ªThe Unreasonable Effectiveness of Deep Features as a Perceptual Metric,º in Proceedings of the 2018 IEEE/CVF Conference on Computer Vision and Pattern Recognition, CVPR. Computer Vision Foundation / IEEE Computer Society, 2018, pp. 586± 595. 

- [32] A. Ghorbani, J. Wexler, J. Y. Zou, and B. Kim, ªTowards Automatic Concept-based Explanations,º in Advances in Neural Information Processing Systems 32: Proceedings of the 33rd Annual Conference on Neural Information Processing Systems, NeurIPS, 2019, pp. 9273±9282. 

883 

