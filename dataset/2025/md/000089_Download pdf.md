---
paper_id: "000089"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706588/files/000089.pdf"
---

# FRETBOARDFLOW: A DUAL-MODEL APPROACH TO OPTIMIZE CHORD VOICINGS ON THE GUITAR FRETBOARD 

Marcel A. Vélez Vásquez<sup>1</sup> Mariëlle Baelemans<sup>1</sup> Jonathan Driedger<sup>2</sup> John Ashley Burgoyne<sup>1</sup> 1 ILLC, University of Amsterdam, the Netherlands 2 Chordify, Groningen, the Netherlands 

```
m.a.velezvasquez@uva.nl
```

## ABSTRACT 

Smoothly transitioning between chords on the guitar can be a major challenge for beginners, especially when they rely on just a few common chord diagrams. Yet many chords can be played in multiple ways (i.e., voicings), which can facilitate more comfortable hand movements on the fretboard. To address this, we present the FretboardFlow dataset, featuring 97 songs recorded with a hexaphonic pickup to capture multiple chord voicings as performed by expert guitarists. Our dataset builds upon the GuitarSet pipeline, incorporating a Python translation of Prätzlich et al’s KAMIR algorithm for interference reduction, for automated hexaphonic transcriptions, thereby capturing harmonic structure and performance-driven voicing choices that implicitly reflect muscle memory and ergonomic habits, providing a rich resource for analyzing real-world chord transitions. 

To predict the most convenient voicing within progressions, we propose a dual-model approach integrating both chord and voicing history, and loss functions well-suited to the flexible nature of voicings. Our research expands on prior chord prediction work by incorporating expertrecorded voicing variations of the same progressions and introducing a novel machine learning approach to fretboard navigation. We publicly release this dataset as a living resource to support data-driven exploration of context-aware guitar instructions. 

## 1. INTRODUCTION 

Online guitar-tablature and learning platforms like Ultimate Guitar [1] and Chordify provide millions of users access to extensive rhythm guitar song libraries. These websites often display multiple ways to play a given chord symbol, known as chord voicings (e.g., Ultimate Guitar suggests 27 ways to voice a G major chord). Yet they rarely guide learners in choosing between candidate voicings [2], nor do they adapt subsequent chord voicings to reflect prior playing decisions. As a result, novice players often default to a single, commonly taught chord voicing – even though 

> © M.A. Vélez Vásquez, M.C.E. Baelemans, J. Driedger, and J.A. Burgoyne. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: M.A. Vélez Vásquez, M.C.E. Baelemans, J. Driedger, and J.A. Burgoyne, “FretboardFlow: A DualModel Approach to Optimize Chord Voicings on the Guitar Fretboard”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

voicings significantly affect tonal character, physical comfort, and voice leading [2–4]. For instance, a player might struggle with frequent shifts between open and barre chords, when consistently using barre voicing could yield smoother transitions across an entire progression. Without contextual guidance, such inefficient choices can hinder playability [5] and may go unnoticed by beginners [6]. 

Selecting appropriate voicings can be challenging and time-consuming at any skill level. Beginners, in particular, often face awkward transitions due to initial fingerings choices [7–9]. As players gain experience, they develop an intuition for convenient voicings for a given progression [2]. Automatic systems that can recommend context-sensitive voicings could help build this intuition. However, current computational approaches and datasets do not yet fully address these nuanced decisions. 

From a computational perspective, prior work [10] suggests that incorporating a longer history of previously played voicings can lead to smoother transitions. However, this insight remains underexplored in current voicing prediction systems and educational tools. Meanwhile, existing community-based datasets such as DadaGP [11] offer large-scale chord transcriptions but do not explicitly capture multiple voicings of the same progression. As a result, they overlook the nuanced transitions that are essential for modeling naturalistic guitar performance. This gap highlights the need for a dedicated resource that systematically captures varied, context-sensitive voicings. 

In this paper, we introduce FretboardFlow, a curated dataset of expert-played rhythm guitar performances featuring up to five voicing variations for 35 songs, totaling 97 hexaphonic pickup recordings. We build on the Billboard Playability dataset and McGill Billboard dataset [12,13] by employing a hexaphonic pickup to record individual strings, ensuring we can distinguish closely related chords that otherwise sound similar. We further propose a dual-model voicing prediction approach that combines information from both chord-symbol sequences and the history of previously played voicings, encouraging smoother transitions. Finally, we introduce a proper scoring rule, which encourages the model to capture the probabilistic nature of voicing choices rather than enforcing a single “correct” voicing. 

## 2. RELATED WORK 

Prior work has mainly focused on understanding and developing voicings for musical instruments, particularly the 

763 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

piano [14–16]. Notably, Nakamura et al. employed datadriven techniques to advance piano transcription and performance analysis, leveraging the PIG Dataset, which includes fingering annotations from multiple pianists [15]. Their results show the value of multi-performer datasets for modeling how different musicians approach chord structures. Similarly, Srivatsan and Berg-Kirkpatrick introduced a checklist-based reinforcement learning model for piano fingering prediction utilizing a representation based on relative note positions [17]. Their approach significantly enhanced the fluency and playability of predicted fingerings, and their reevaluation of standard metrics highlighted the complexity of modeling comfortable performance. 

While these piano-focused methods showcase the effectiveness of data-driven approaches, research on the guitar’s unique challenges remains limited. Existing work has examined guitar fingering capture and tracking, often using computer vision or specialized sensors [6,18,19]. However, these efforts typically focus on real-time detection rather than documenting alternative voicings. Although largescale tablature datasets such as the DadaGP dataset [11] and those used in MIREX transcription tasks [20–22] provide extensive chord data, they seldom focus on modeling multiple valid ways to fret the same chord or progression. 

Recent work by Vélez Vásquez et al. [12] has made significant strides in formalizing the concept of playability for rhythm guitar. Through interviews with teachers and players, they developed a rubric encompassing seven criteria related to playability, three of which directly concern chord voicings. Their findings emphasize the need for deeper analysis of how alternative fingerings and fretboard positions affect overall ease of performance. This focus aligns with a long-standing pedagogical traditions that emphasize intentional finger placement as fundamental both to technical fluency and musical expressivity [23,24]. Fingering – defined as the specific assignment of fingers to frets and strings – has been shown to influence both the physical execution and perceived difficulty of a musical passage significantly [6,19,25]. A critical factor in this regard is the amount of hand movement required between chords [7], which can often be minimized when players have access to a broader vocabulary of chord voicings. In this context, a tool capable of suggesting suitable and potentially novel voicings tailored to the current progression could greatly improve both playability and learning outcomes. 

While recent work has laid the groundwork for datadriven chord voicing prediction (most recently by d’Hooge et al. [10], who show that incorporating the previous chord diagram improves voicing prediction), the field still lacks balanced, high-quality datasets specifically designed for voicing prediction, as well as models that effectively take longer chord history into account. To address these gaps, we introduce a performance-based dataset that captures expert voicing decisions, including multiple variations of the same chord in real musical contexts. Alongside this, we explore a dual-model prediction framework that integrates both chord symbols and prior voicing history, enabling more contextaware modeling of voicing transitions. 

## 3. FRETBOARDFLOW DATASET 

Predicting chord voicings beyond the most common positions around the lower frets of the guitar neck requires a dataset that captures multiple feasible voicings for the same chord progression. As illustrated in Figure 1B, the community-based DadaGP dataset features high fretboard activity in the lower positions, reflecting a bias toward open chords (where strings are played without being fretted on the neck). While such shapes are commonly used by novice guitarists, they may lead to suboptimal transitions – for example, requiring frequent shifts between open and barre chords when staying in barre shapes might offer more convenient movement. Moreover, while individual chords can be played in many ways, not all voicings fit together in the context of a progression. Capturing only a single voicing per progression risks leading models to memorize a one-to-one mapping between a progression and a voicing, rather than considering any appropriate alternatives. To complement existing resources like DadaGP, we introduce FretboardFlow, a curated dataset of expert performances that captures natural voicing choices across the fretboard (see Figure 1A). By including multiple voicings for the same progression, FretboardFlow enables the development of models that can learn context-aware fretboard usage. 

Our FretboardFlow dataset builds on the Billboard Playability Dataset [12], a curated subset of the broader McGill Billboard Dataset [13] comprising 200 songs from the Billboard Hot 100. The Playability dataset provides detailed chord transcriptions and annotations across seven difficulty criteria – three of which relate directly to voicing – but uses a fixed chord voicing for each chord when predicting playability. This simplification limits the exact modeling of the progressions, since the dataset’s experts might have used different voicings during playability annotations. In designing FretboardFlow, we expanded this dataset by recording multiple expert-performed voicings for the same chord progressions, with an emphasis on natural movement on the fretboard. Our selection of songs draws from the Billboard Playability set specifically for its diversity in and annotations of chord difficulty levels; as a result, the dataset includes a range of chord types and playing techniques. While prior work [10] used datasets such as DadaGP [11], which provides large-scale community-contributed GuitarPro files, they emphasize open-position voicings (see Figure 1B), and are not specifically designed for chord voicing prediction. In contrast, FretboardFlow aims to provide richer data for learning natural voicings across the fretboard. 

To construct the FretboardFlow dataset, we recorded multiple performances by expert guitarists, resulting in a subset of 35 songs selected from the Billboard Playability dataset (see Section 3.1). Each song was recorded in one to five different voicing variations, yielding a total of 97 performances that reflect alternatives one might viably play. 

Capturing transitions between chords in specific voicings presents inherent challenges. While the fingering of a chord voicing plays a critical role in playability [24], recording precise finger placement would require complex motion capture or computer vision setups. Instead, we focus on cap- 

764 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
A:<br>B:<br><!-- End of picture text -->

Figure 1. Fretboard heatmaps illustrating fret usage across two datasets. (A) Heatmap of fret usage across all hexaphonic recordings in the FretboardFlow dataset. (B) Heatmap of fret usage in d’Hooge et al.’s chord diagram subset [10] of the DadaGP dataset [11]. The x-axis represents fret positions, starting with the open string. The y-axis corresponds to the six guitar strings, with the bottom row representing the low E string and the top row the high e string. Fret usage in (A) is more evenly distributed up to the 12th fret, suggesting expressive coverage of the fretboard. In contrast, (B) shows usage concentrated around the first three frets, with some activity near frets 5 and 7. 

turing which frets are pressed on each string, disregarding which finger is used, to strike a balance between precision and practicality. Using a guitar equipped with a hexaphonic pickup, we are able to determine the string and fret for each note in a chord, enabling accurate reconstruction of fretboard positions even in cases where audio alone might be ambiguous. 

FretboardFlow captures how voicings may vary both across songs, and within the same chord symbol progressions. More information about variation in song version count per contributor is available in the supplementary material. We release this dataset as a living resource, with plans to expand it over time, to support further research in voicing prediction, playability modeling, and personalized music instruction. 

## 3.1 Song selection 

We asked the participants to aim for at least three different voicings per song, instructing them to perform the pieces as is, without use of a capo. However, understanding the challenges some pieces pose, guitarists were permitted to simplify their performances by omitting inversions or added intervals, provided they informed us for accurate annotation. In practice, it only occurred for one song that one participant did not feel comfortable playing the inversion/added interval for more than one take. 

To ensure a diverse range of difficulties within our dataset and prevent multiple participants from accidentally choosing the same song, we assigned each participant three very easy, five easy, ten difficult, and three very difficult pieces, based on their Billboard Playability scores for Chord Fingering Difficulty. These assignments were based on the Chord Fingering Difficulty (CFD) criteria from the Bill- 

board playabilty dataset. Unlike other categories, ’very difficult’ pieces were strategically distributed among multiple participants. This exception was made because these pieces, due to their complexity, offer valuable insights into advanced playing techniques and only two of the participants opted to practice these. 

## 3.2 Participant instructions 

Participants were provided with a web-based interface to practice songs and familiarize themselves ahead of the recording session. They selected songs from a list annotated with difficulty ratings from the Billboard Playability dataset [12], allowing them to choose material appropriate to their skill and interest. 

Once familiarized with the songs, recordings were made using the same web-interface and the hardware setup described in Section 3.3. Participants were encouraged to focus on producing feasible and musically coherent voicings, rather than flawless takes. While the contributors had the option to practice at slower tempos, only one performance was recorded in half-time. 

Four expert guitarists contributed. Expert A was instrumental in creating 56 recordings, averaging 3.2 variations per song, including two versions of the most difficult song, Stevie Wonder’s “Do I Do”, without using simplified or half-speed versions. Expert B contributed 8 recordings, averaging 2.7 voicings per song, including 3 simplified versions and no half-speed recordings. Expert C contributed 19 recordings, averaging 2.1 voicings per song, with no simplifications but one half-speed recording. Expert D contributed 14 recordings, averaging 2.5 voicings per song, also without employing simplifications or half-speed. 

765 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 3.3 Recording setup 

Our recording setup, audio-cleanup and pitch estimation were inspired by the GuitarSet pipeline [26]. We used a custom-built hexaphonic pickup to record each individual guitar string. The pickup, built by Ubertar, uses six individual magnets – one per string – to capture separate audio channels. This pickup had to be soldered to a 7-pin cable and connected to a custom-made breakout box (also from Ubertar), allowing us to route each string’s signal independently. An additional standard output cable was used to transfer the regular mono output of the guitar itself. 

To capture the 7 audio streams, we used a Focusrite Scarlett 18i20 (3rd Gen), where each stream was recorded as separate tracks. For the guitar, we used a high-end Breedlove Concerto steel-string acoustic guitar for all recordings, attaching the hexaphonic pickup in the soundhole using the acoustic adapter from Ubertar. 

Although each string was recorded using individual magnets, the magnets were sensitive enough that audio bleed occurred between adjacent strings. To address this, we implemented a Python reimplementation of the KAMIR algorithm [27], originally developed in MATLAB, which we used to reduce interference. After isolating each signal we applied pYin [28] for pitch extraction. 

Post-processing and correction of the extracted pitch data were carried out using a combination of automated and manual methods. Focusing on chord voicings over precise onsets, we diverged from the GuitarSet pipeline. Rather than using Tony [29], we used Ableton Live 12, to enable multi-track MIDI editing and alignment. Pitch data was quantized to four evenly spaced positions per bar, and only unique phrases within each song were corrected (including uniqueness of voicings). 

Further details, including software tools, annotation choices, difficult cases, and model examples are available on Github.<sup>1</sup> 

## 4. FRETBOARDFLOW ANALYSIS AND COMPARISON TO DADAGP 

A primary focus of our dataset is its emphasis on multiple feasible chord voicings, rather than a single valid shape. While each voicing in the dataset has been performed, the absence of a particular voicing in our dataset does not imply it is unfeasible. In our recordings, 7.24% of the chords contain inversions, and 6.50% include added intervals – slightly higher than the 4.90% and 2.35%, respectively, found in DadaGP [11], suggesting a greater distribution of less common chord forms. 

We further analyzed fretboard usage through heatmaps (Figures 1A and 1B). FretboardFlow displays a more uniform spread of fret usage, extending well beyond the seventh fret, while DadaGP shows a strong bias toward open strings and second/third frets, indicating a narrower range of chord positions. 

An n-gram analysis (unigram through tetragram) further emphasizes the variety of voicing options in FretboardFlow. 

> 1 https://github.com/Marcel-Velez/FretboardFlow 

Even at the trigram and tetragram levels, chord progressions frequently appear in multiple voicings, whereas the DadaGP shows heavier reliance on a single voicing per progression. As shown in Figure 2, FretboardFlow consistently contains a higher proportion of progressions with multiple unique voicing variants compared to DadaGP across all n-gram levels. We define distinct n-gram variants as any chord sequence in which at least one voicing differs; thus, two progressions with the same chord labels but only one altered voicing still count as separate variants. This highlights how FretboardFlow complements existing datasets by providing not only multiple chord shapes for individual chords but also meaningful variation within chord sequences – a core goal of our dataset. 

## 5. DUAL-MODEL APPROACH 

The challenge of predicting the optimal chord voicing relies on combining the information of two distinct data types. On one hand, our model must interpret past voicing fret positions, capturing the temporal relation between chord transitions, while simultaneously processing the history of chord symbols and the upcoming chord. First, it encodes the voicing history, a sequence of fretboard matrices that capture fret positions over time, allowing it to model natural transitions. Second, it processes the chord-symbols, represented as many-hot encoded vectors (e.g., root, quality, bass), capturing the harmonic context. Our solution is a novel approach, illustrated in Figure 3. It consists of two subnetworks, each processing one of the data streams, whose outputs are combined with a single linear layer. 

The upper chord-symbol subnetwork processes the chord-symbol sequence up to time step t. We encode each chord symbol into a structured representation that captures the root note, chord quality, and bass note. Following the approach in [12, 30], we use an LSTM or DeepGRU to model these chord-symbol transitions. By using an LSTM (or alternatively, a DeepGRU with attention), the network can effectively learn from arbitrary length context, ensuring musical correctness for the prediction. 

In parallel, the lower voicing-history subnetwork deals with the fretboard positions used in previous time steps (up to t − 1). This sequential encoding captures the physical transitions between chords. For this subnetwork we again use an LSTM or DeepGRU to model these transitions. The aim is to encourage convenient voicings. 

After both subnetworks process their respective inputs, we concatenate their latent representations and feed the result through a single linear layer, outputting a distribution over possible frets for time step t. 

## 5.1 Implementation 

We slightly alter the LSTM-based framework used by [12, 30], which demonstrated promising results for both piano and guitar playability prediction. Specifically, we adopt a bidirectional LSTM variant to reflect that guitarists often know the full chord progression beforehand and can choose voicings that best fit the entire sequence. By considering 

766 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
Uni-gram Bi-gram Tri-gram Tetra-gram<br>0. 8 Dataset<br>FretboardFlow<br>0. 6 DadaGP<br>0. 4<br>0. 2<br>0. 0<br>Number of Unique Voicing Variants Number of Unique Voicing Variants Number of Unique Voicing Variants Number of Unique Voicing Variants<br>1 2 3 4 5 6 7 8 9 10111213 1 2 3 4 5 6 7 1 2 3 4 1 2 3<br>Proportion (Ratio)<br><!-- End of picture text -->

Figure 2. Histograms comparing the number of unique chord variants and chord progressions of lengths 2, 3, and 4 in the larger community-based DadaGP dataset [11] and our curated FretboardFlow dataset. Each subplot displays the distribution of unique variants (x-axis: number of variants; the y-axis: ratio). DadaGP shows a strong bias toward a single variant, while FretboardFlow consistently demonstrates higher ratios for progressions with multiple variations. 



<!-- Start of picture text -->
������<br>������<br>�������<br>EC��� �C��H �C��H<br>2����,2���� �<br>� � K<br>@�����9<br>������<<br>�������<br>������ ������ ������<br>�����������* �����������* �����������*<br>������ ������� ������ �������<br><!-- End of picture text -->

Figure 3. Overview of the dual-subnetwork architecture for chord voicing prediction. One subnetwork encodes the chord-symbol sequence, while the other processes voicing history as fretboard matrices. The outputs are concatenated and passed to a linear layer to predict the next voicing. 

information from both preceding and subsequent chords, the model more closely approximates the way guitarists choose transitions along a progression. Additionally, we explore the implementation of a DeepGRU-like architecture for both subnetworks [31]. This model shares similarities with the LSTM but incorporates an attention module, allowing the model to attend to distinct parts of the input sequence. 

To handle chord symbols effectively, we encode each symbol into a structured vector representation in a similar fashion as Koops et al. and McFee et al. [32,33]. Specifically, our representation consists of three pitch class vectors spanning the 12 semitones of the Western musical octave: the root note encoding, a one-hot vector indicating which pitch class serves as the chord root; the quality and added intervals, a many-hot vector denoting the valid pitch classes for a given quality and additions; and the bass note encoding, a similarly encoded one-hot vector indicating the bass note (to account for inversions). These are then concatenated to serve as input to the chord-symbol subnetwork. 

To encode each chord voicing, we use a binary matrix representation of the fretboard. Each string’s state is represented by a one-hot vector of size nfrets + 2, where we reserve one index for open strings and another for muted strings. In our recordings, the guitar has 21 frets, leading to a 6 × 23 matrix per chord. This layout captures the physical placement of the voicing, enabling our sequence model to 

learn transitions from one chord shape to the next. 

We train the networks both with cross-entropy loss and mean-squared-error loss, which are equivalent to the logarithmic and Brier scoring rules for probabilistic forecast comparison, in the sense of Gneiting and Raftery [34]. Specifically, these loss functions are proper scoring rules, which are convex and guarantee that minimal loss would be achieved only when the network accurately reflects the probabilities of an expert choosing different possible fingerings in each context (as opposed to fixed ground truth). 

## 6. EXPERIMENTS AND RESULTS 

We trained and tested on two datasets: FretboardFlow (the new dataset presented in this work) and DadaGP [11] filtered to contain only chord diagram data (as in [10]). We also tested a data augmentation approach in line with previous studies [10,35]. We transposed each chord symbol and its voicing up or down by semitone steps until the transposition would either introduce an open string or exceed the 15th fret. This helps mitigate chord-key biases and multiplies the size of each dataset by a factor of 7+. 

In addition to our own dual models, we also trained and tested d’Hooge et al.’s MLP model and baseline model [10] as reference points, using the same vocabulary as our dualmodel vocabulary. We ran all combinations of model (BiLSTM dual model, DeepGRU dual model, MLP [10], or baseline [10]), dataset (FretboardFlow, augmented FretboardFlow, DadaGP, or augmented DadaGP), loss function (cross-entropy or MSE), and three different history lengths for the dual models (1, 3, or 7). We used five-fold crossvalidation, with one fold (20%) reserved for validation and another fold (20%) for testing in each run. Early stopping happened if the validation loss did not improve by at least 0.001 within two epochs. 

The most prominent results of our experiments appear in Table 1, and a complete list is provided in the supplemental material. We consider test loss to be the best evaluation metric for this task, because of the scoring-rule properties mentioned above: only proper scoring rules can fully take into account the natural variation in experts’ voicing preferences. We also include the evaluation suite of d’Hooge et al. [10], however, to facilitate comparison across the literature. This suite includes the following metrics, which together capture both musical accuracy and physical playa- 

767 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

|Model|Dataset|History<br>length|Loss<br>type|Loss↓|F1↑|F1P ↑|F1SF ↑|Ease of<br>transition↑|Unplayability↓|
|---|---|---|---|---|---|---|---|---|---|
|Bi-LSTM|FretboardFlow+|3|Cross|2.80±0.01|0.13±0.00|0.72±0.01|0.56±0.01|0.06±0.00|0.47±0.01|
|DeepGRU|FretboardFlow+|3|Cross|1.20±0.19|0.21±0.00|0.75±0.05|0.25±0.00|0.06±0.01|0.53±0.04|
|DeepGRU|FretboardFlow+|1|Cross|1.04±0.04|0.20±0.00|0.80±0.01|0.24±0.00|0.08±0.00|0.46±0.02|
|DeepGRU|FretboardFlow|1|Cross|1.51±0.09|0.19±0.01|0.73±0.04|0.27±0.00|0.11±0.01|0.27±0.04|
|MLP|FretboardFlow+|1|Cross|2.62±0.00|0.71±0.00|0.82±0.00|0.71±0.00|0.07±0.00|0.50±0.01|
|Baseline|FretboardFlow+|0|Cross|2.91±0.00|0.41±0.00|0.74±0.01|0.41±0.00|0.04±0.00|0.62±0.03|
|Bi-LSTM|DadaGP+|3|Cross|2.50±0.01|0.14±0.00|0.93±0.00|0.84±0.01|0.06±0.00|0.55±0.01|
|DeepGRU|DadaGP+|3|Cross|0.49±0.00|0.27±0.00|0.93±0.00|0.30±0.00|0.06±0.00|0.53±0.00|
|DeepGRU|DadaGP|3|Cross|0.77±0.08|0.30±0.01|0.87±0.02|0.36±0.02|0.20±0.01|0.09±0.02|
|MLP|DadaGP+|1|Cross|2.58±0.00|0.75±0.00|0.86±0.00|0.75±0.00|0.06±0.00|0.62±0.00|
|Baseline|DadaGP+|0|Cross|2.76±0.00|0.57±0.00|0.79±0.00|0.57±0.00|0.02±0.00|0.86±0.01|
|DeepGRU|DadaGP+|3|MSE|0.01±0.00*|0.22±0.00|0.92±0.00|0.25±0.01|0.06±0.00|0.53±0.00|
|MLP|DadaGP+|1|MSE|0.03±0.00*|0.73±0.00|0.85±0.00|0.73±0.00|0.06±0.00|0.62±0.00|
|Baseline|DadaGP+|0|MSE|0.03±0.00*|0.52±0.00|0.77±0.00|0.52±0.00|0.01±0.00|0.89±0.02|



Table 1. Best configurations of our models compared to prior work and baseline on FretboardFlow and DadaGP. Test loss is our primary metric, while additional metrics (F1P, F1SF, unplayability, transition ease) ensure comparability with previous literature. Full results are in the supplementary material. Note: Test losses are not directly comparable across loss types. 

bility: naïve F1 measures exact voicing matches between predicted and reference chord; pitch-class F1 considers whether the chord’s set of pitches (ignoring octaves) aligns with the target chord symbol; string-fret F1 evaluates correctness on a per-string basis, capturing partial matches if only some string-fret assignments differ; unplayability indicates unplayable voicings, based on the anatomical score from [36]; and ease of transition, rating how comfortable it is to move from one chord to the next based on the chord change metric proposed by [37]. 

## 6.1 Performance on FretboardFlow 

Rows 1–6 of Table 1 present key results on original and augmented FretboardFlow (+). For FretboardFlow+, we compare the best LSTM (history 3) with DeepGRUs of history 1 and 3. The DeepGRU (history 1) on FretboardFlow is included to assess the effect of augmentation. MLP and Baseline serve as references. 

All DeepGRU variants achieve substantially lower test loss than the bi-LSTM, MLP, and baseline, highlighting their effectiveness in modeling chord-voicings. While the LSTM outperforms the baseline, it underperforms the MLP, which performs best on F1P, indicating better pitch class prediction. GRUs improve on the baseline in F1P on FretboardFlow+, but not on string-fret F1. The LSTM slightly surpasses the baseline on string-fret F1 but still underperforms the MLP. GRUs, especially with history 1, offer better ease-of-transition and lower unplayability than MLP and Baseline. Only MLP performs strongly on naïve F1, showing its advantage in replicating exact chord shapes 

## 6.2 Performance on DadaGP 

Rows 7–11 of Table 1 show top LSTM and GRU models on DadaGP+, along with GRU on original DadaGP and MLP/Baseline for reference. History 3 performed best for both LSTM and GRU. GRU achieves much lower test loss than LSTM, indicating better overall predictions, while LSTM yields higher F1SF. LSTM also outperforms MLP and Baseline on most metrics (except naïve F1), suggest- 

ing stronger, but not exact, voicing replication. On nonaugmented DadaGP, GRU has slightly higher test loss but improved ease-of-transition and lower unplayability, indicating that augmentation improves voicing diversity but may reduce ergonomic feasibility 

The final rows compare MSE-trained GRU, MLP, and Baseline. Though loss values are not directly comparable, the MSE GRU achieves the lowest test loss and highest F1P, outperforming MLP and Baseline by ≥0.07. It also shows lower unplayability and competitive ease-oftransition. When compared to cross-entropy, the MSEbased GRU maintains similar pitch-class F1 but performs worse on naïve F1 and F1SF, suggesting that while MSE captures pitch correctness equally well, it sacrifices precision in exact voicing and string-fret alignment. 

## 7. CONCLUSION AND FUTURE WORK 

To predict comfortable chord voicings within progressions on the guitar, we proposed a dual-model architecture with two parallel subnetworks, either Bi-LSTMs or DeepGRUs, that integrate both chord and voicing history. Leveraging a loss function well-suited to the flexible nature of guitar voicings, our approach improves over prior work by utilizing longer-term context and better modeling voicing variation. 

We also introduced FretboardFlow, a new dataset of expert-recorded chord progressions featuring natural voicing variation. While the DadaGP dataset yields lower absolute test losses (mostly likely due to DadaGP’s larger scale and less variation in voicing), our models – particularly those using DeepGRU – achieve significantly lower loss on than prior models on both datasets, more effectively capturing the subtleties of voicing variations. 

Finally, our codebase includes a re-implementation of the KAMIR algorithm [27] for more general use. 

As a publicly released, living dataset, FretboardFlow supports data-driven research into fretboard navigation. Future work will explore integrating ergonomic constraints directly into the objective function, expanding the dataset, and refining long-context modeling. 

768 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 8. ACKNOWLEDGMENT 

We thank Jeanine, Pepijn, Julian, and Anders for their time practicing and recording multiple voicing versions of the songs. This research was supported by the Dutch Research Council (NWO) as part of the project InDeep (NWA.1292.19.399). 

- [9] N. d. S. Cunha, A. Subramanian, and D. Herremans, “Generating guitar solos by integer programming,” Journal of the Operational Research Society, vol. 69, no. 6, pp. 971–985, 2018. 

- [10] A. d’Hooge, L. Bigo, K. Déguernel, and N. Martin, “Guitar chord diagram suggestion for western popular music,” in Sound and Music Computing Conference, 2024. 

## 9. ETHICS STATEMENT 

This study was approved by the Ethics committee of the Faculty of Humanities at the University of Amsterdam (Reference: FGW-2325_2024). Participants were recruited through informal outreach within the our personal and professional networks. All participants provided informed consent, and received appropriate compensation in accordance with the ethics committee guidelines of <mark>C2</mark> .50 per 15 minutes. A data management plan was filed and is available upon request to ensure that the collected data is handled responsibly and in compliance with institutional guidelines. 

## 10. REFERENCES 

- [1] Ultimate Guitar, “UG Community @ ultimateguitar.com,” https://www.ultimate-guitar.com/forum/, accessed: 2025-02-05. 

- [2] J. De Souza, “Fretboard transformations,” Journal of Music Theory, vol. 62, no. 1, pp. 1–39, 2018. 

- [3] T. Koozin, “Guitar voicing in pop-rock music: A performance-based analytical approach,” Music Theory Online, vol. 17, no. 3, 2011. 

- [4] D. Huron, “Tone and voice: A derivation of the rules of voice-leading from perceptual principles,” Music Perception, vol. 19, no. 1, pp. 1–64, 2001. 

- [5] M. C. E. Baelemans, M. A. Vélez Vásquez, and J. A. Burgoyne, “Defining playability in musical performance: Cognitive factors and implications for automated song difficulty estimation,” in Proceedings of SysMus23, 2023, pp. 77–79. 

- [6] G. Hori and S. Sagayama, “Minimax Viterbi algorithm for HMM-based guitar fingering decision,” in Proceedings of the 17th International Society for Music Information Retrieval Conference, 2016, pp. 448–453. 

- [7] S. Ariga, S. Fukayama, and M. Goto, “Song2guitar: A difficulty-aware arrangement system for generating guitar solo covers from polyphonic audio of popular music.” in Proceedings of the 18th International Society for Music Information Retrieval Conference, 2017, pp. 568–574. 

- [8] S. Ariga, M. Goto, and K. Yatani, “Strummer: An interactive guitar chord practice system,” in Proceedings of the IEEE International Conference on Multimedia and Expo, 2017, pp. 1057–1062. 

- [11] P. Sarmento, A. Kumar, C. J. Carr, Z. Zukowski, M. Barthet, and Y.-H. Yang, “DadaGP: A dataset of tokenized GuitarPro songs for sequence models,” in Proceedings of the 22nd International Society for Music Information Retrieval Conference, 2021. 

- [12] M. A. V. Vásquez, M. Baelemans, J. Driedger, W. H. Zuidema, and J. A. Burgoyne, “Quantifying the ease of playing song chords on the guitar,” in Proceedings of the 24th International Society for Music Information Retrieval Conference, 2023, pp. 725–732. 

- [13] J. A. Burgoyne, J. Wild, and I. Fujinaga, “An expert ground truth set for audio chord recognition and music analysis,” in Proceedings of the 12th International Society for Music Information Retrieval Conference, vol. 11, 2011, pp. 633–638. 

- [14] E. Nakamura and K. Yoshii, “Statistical piano reduction controlling performance difficulty,” APSIPA Transactions on Signal and Information Processing, vol. 7, no. e13, 2018. 

- [15] E. Nakamura, Y. Saito, and K. Yoshii, “Statistical learning and estimation of piano fingering,” Information Sciences, vol. 517, pp. 68–85, 2020. 

- [16] P. Ramoneda, D. Jeong, V. Eremenko, N. C. Tamer, M. Miron, and X. Serra, “Combining piano performance dimensions for score difficulty classification,” Expert Systems with Applications, vol. 238B, no. 121776, 2024. 

- [17] N. Srivatsan and T. Berg-Kirkpatrick, “Checklist models for improved output fluency in piano fingering prediction,” in Proceedings of the 23rd International Society for Music Information Retrieval Conference, 2022, pp. 525–531. 

- [18] W. H. Elashmawi, J. Emad, A. Serag, K. Khaled, A. Yehia, K. Mohamed, H. Sobeah, and A. Ali, “A novel approach for improving guitarists’ performance using motion capture and note frequency recognition,” Applied Sciences, vol. 13, no. 10, p. 6302, 2023. 

- [19] G. Hori, “Three-level model for fingering decision of string instruments,” in Proceedings of the 15th International Symposium on Computer Music Multidisciplinary Research, 2021, pp. 93–98. 

- [20] M. McVicar, R. Santos-Rodríguez, Y. Ni, and T. De Bie, “Automatic chord estimation from audio: A review of the state of the art,” IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 22, no. 2, pp. 556–575, 2014. 

769 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [21] R. M. Bittner, J. J. Bosch, D. Rubinstein, G. MeseguerBrocal, and S. Ewert, “A lightweight instrumentagnostic model for polyphonic note transcription and multipitch estimation,” in Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing, 2022, pp. 781–785. 

- [22] E. J. Humphrey and J. P. Bello, “From music audio to chord tablature: Teaching deep convolutional networks to play guitar,” in Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing, 2014, pp. 6974–6978. 

- [23] R. J. Sherrod, A guide to the fingering of music for the guitar. The University of Arizona, 1981. 

- [24] C. Czerny, Letters to a young lady, on the art of playing the pianoforte. R. Cocks, 1842, (translated by J. A. Hamilton). 

- [25] G. Hori, H. Kameoka, and S. Sagayama, “Input-output HMM applied to automatic arrangement for guitars,” Information and Media Technologies, vol. 8, no. 2, pp. 477–484, 2013. 

- [26] Q. Xi, R. M. Bittner, J. Pauwels, X. Ye, and J. P. Bello, “Guitarset: A dataset for guitar transcription,” in Proceedings of the 19th International Society for Music Information Retrieval Conference, 2018, pp. 453–460. 

      - Computing and Applications, vol. 32, no. 4, pp. 929– 939, 2020. 

   - [33] B. McFee and J. P. Bello, “Structured training for largevocabulary chord recognition.” in Proceedings of the 18th International Society for Music Information Retrieval Conference, 2017, pp. 188–194. 

   - [34] T. Gneiting and A. E. Raftery, “Strictly proper scoring rules, prediction, and estimation,” Journal of the American Statistical Association, vol. 102, no. 477, p. 359–378, 2007. 

   - [35] M. McVicar, S. Fukayama, and M. Goto, “AutoGuitarTab: Computer-aided composition of rhythm and lead guitar parts in the tablature space,” IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 23, no. 7, pp. 1105–1117, 2015. 

   - [36] K. A. Wortman and N. Smith, “CombinoChord: A guitar chord generator app,” in Proceedings of the 11th Annual IEEE Computing and Communication Workshop and Conference, 2021, pp. 0785–0789. 

   - [37] K. Yazawa, K. Itoyama, and H. G. Okuno, “Automatic transcription of guitar tablature from audio signals in accordance with player’s proficiency,” in Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing, 2014, pp. 3122–3126. 

- [27] T. Prätzlich, R. M. Bittner, A. Liutkus, and M. Müller, “Kernel additive modeling for interference reduction in multi-channel music recordings,” in Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing, 2015, pp. 584–588. 

- [28] M. Mauch and S. Dixon, “pYIN: A fundamental frequency estimator using probabilistic threshold distributions,” in Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing, 2014, pp. 659–663. 

- [29] M. Mauch, C. Cannam, R. Bittner, G. Fazekas, J. Salamon, J. Dai, J. Bello, and S. Dixon, “Computer-aided melody note transcription using the tony software: Accuracy and efficiency,” in Proceedings of the First International Conference on Technologies for Music Notation and Representation, 2015. 

- [30] P. Ramoneda, N. C. Tamer, V. Eremenko, X. Serra, and M. Miron, “Score difficulty analysis for piano performance education based on fingering,” in Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing, 2022, pp. 201–205. 

- [31] M. Maghoumi and J. J. LaViola, “DeepGRU: Deep gesture recognition utility,” in Advances in Visual Computing: 14th International Symposium on Visual Computing. Berlin: Springer, 2019, pp. 16–31. 

- [32] H. V. Koops, W. B. de Haas, J. Bransen, and A. Volk, “Automatic chord label personalization through deep learning of shared harmonic interval profiles,” Neural 

770 

