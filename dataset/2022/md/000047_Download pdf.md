---
paper_id: "000047"
year: 2022
title: "Download pdf"
source_url: "https://zenodo.org/record/7316682/files/000047.pdf"
---

# PERFORMANCE MIDI-TO-SCORE CONVERSION BY NEURAL BEAT TRACKING 

Lele Liu<sup>∗1,2</sup> Qiuqiang Kong<sup>3</sup> Veronica Morfi<sup>1</sup> 1 Centre for Digital Music, Queen Mary University of London, UK 

Emmanouil Benetos<sup>1,2</sup> 

2 The Alan Turing Institute, UK 3 ByteDance Shanghai, China 

lele.liu@qmul.ac.uk 

## ABSTRACT 

Rhythm quantisation is an essential part of converting performance MIDI recordings into musical scores. Previous works on rhythm quantisation are limited to the use of probabilistic or statistical methods. In this paper, we propose a MIDI-to-score quantisation method using a convolutional-recurrent neural network (CRNN) trained on MIDI note sequences to predict whether notes are on beats. Then, we expand the CRNN model to predict the quantised times for all beat and non-beat notes. Furthermore, we enable the model to predict the key signatures, time signatures, and hand parts of all notes. Our proposed performance MIDI-to-score system achieves significantly better performance compared to commercial software evaluated on the MV2H metric. We release the toolbox for converting performance MIDI into MIDI scores at: https://github.com/cheriell/PM2S. 

## 1. INTRODUCTION 

Performance MIDI-to-Score (PM2S) conversion aims to convert a performance MIDI, usually recorded by electronic MIDI keyboards, into musical scores in computerreadable score format such as MIDI, MusicXML [1] and Lilypond [2]. PM2S covers a list of subtasks including rhythm quantisation, note value prediction, key estimation, voice separation, and possibly score typesetting such as beaming and playing techniques annotation. PM2S can be used in various scenarios such as music improvisation [3], complete music transcription [4±7] in combination with multi-pitch detection, music alignment [8], music education, music performance analysis [9], and building music archives. 

Although research on the various subtasks on PM2S dates back to earlier decades [10±13], the first academic paper that fully formulated this task was published in 2016 [14]. The paper works on converting a performance MIDI recording into a LilyPond score. The authors firstly fixed 

* The author conducted this work as an intern at ByteDance. 

> © L. Liu, Q. Kong, V. Morfi, and E. Benetos. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: L. Liu, Q. Kong, V. Morfi, and E. Benetos, ªPerformance MIDI-to-score conversion by neural beat trackingº, in Proc. of the 23rd Int. Society for Music Information Retrieval Conf., Bengaluru, India, 2022. 

spurious overlapping notes according to a defined note overlapping ratio, then applied a probabilistic model using Hidden Markov Models (HMMs) based on a tactus-root combination concept [15] for meter, harmony, and stream estimation. After that, the note onsets and offsets are quantised to beat subdivisions. Note spellings and staves are determined from the predicted harmony and streams. 

Following the use of conventional methods for solving subtasks such as rhythm quantisation, recent years have seen some advances on statistical methods [5,16±19]. Nakamura et al. [16] proposed an improvement for rhythm transcription using a merged-output HMM to solve the problem introduced by multiple voices. A note value prediction method using Markov random fields was proposed in [17]. The two methods were further improved for automatic music transcription by combining multi-pitch detection [5, 19]. Mcleod and Steedman [18] proposed an HMM-based meter detection method for aligning MIDI performances. 

Over the past two years, researchers have published papers using deep learning methods on PM2S. Hiramatsu et al. [20] proposed to use a recurrent neural network for joint estimation of note values and voices from note pitches and onset times, which in combination with multi-pitch detection and rhythm quantisation, outperformed previous methods [14, 19] for automatic music transcription. The Score Transformer [21] provided a solution to generating human-readable scores from quantised MIDI files. 

From previous works, we observe that the problem of PM2S is usually solved through a combination of different methods for subtasks. Moreover, although there are attempts on applying deep learning methods for the task, they do not cover the rhythm quantisation step. 

To address the limitations mentioned above, we propose to use a deep learning method for PM2S. We develop a CRNN model that directly converts a performance MIDI into a MIDI score. We pay special attention to the rhythm quantisation step, and propose to solve the problem by tracking beats on a MIDI note sequence. We then expand the CRNN model to predict a compact output for generating a quantised MIDI score, including quantised onset times and note values, time signatures, key signatures and hand parts. To better capture our method’s ability in modelling expressive performances, we train and evaluate our proposed model on a set of classical piano music datasets [22, 23]. In a comparison with two commercial software 

395 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

products MuseScore [24] and Finale [25], our proposed method achieved significantly better performance based on the MV2H metric [26]. 

## 2. METHODOLOGY 

## 2.1 Problem definition 

Our proposed method aims to predict a MIDI score from a performance MIDI using a deep learning model. Assume a performance MIDI note sequence X where notes are ordered firstly by time and secondly by pitch. Each note in the sequence is represented by a tuple: 



<!-- Start of picture text -->
X = {(pn, on, dn, vn)} N n=1 (1)<br><!-- End of picture text -->

where pn, on, dn, vn are the MIDI pitch number, onset and duration in seconds, and velocity for the n-th note, N is the number of notes. We aim to predict the transcribed MIDI score annotations including 



<!-- Start of picture text -->
Yn = {(mon, nvn, hn)} N n=1 (2)<br><!-- End of picture text -->



<!-- Start of picture text -->
Yt = {(ti, tni, tdi)} T i=1 (3)<br><!-- End of picture text -->



<!-- Start of picture text -->
Note sequence<br>kernel size & channel<br>(9, 1), 512<br>(9, 1), 256<br>(9, in_features), 128<br>Convolutional<br>Batch normalisation<br>Exponential linear unit<br>Dropout (0.15)<br>ConvBlock To next convolutional layer<br>Bi-directional GRU (512)<br>Bi-directional GRU (512)<br>GRUBlock Linear (512)<br>Linear (1)<br>In-note beat probabilities<br><!-- End of picture text -->

Figure 1. Model architecture for in-note beat prediction. 

## 2.3 Neural beat tracking on note sequences 

## 2.3.1 In-note and out-of-note beats 

To match the model input data in note sequence format, we separate beats into two groups: 

- In-note: beats concurrent with at least one note onset; 

- Out-of-note: beats not concurrent with any note onset. 



<!-- Start of picture text -->
Yk = {(ti, ki)} K i=1 (4)<br><!-- End of picture text -->



<!-- Start of picture text -->
Y = (Yn, Yt, Yk) (5)<br><!-- End of picture text -->

where Yn covers the musical onset time mon, note value nvn and hand part hn for all notes; Yt and Yk are the time signature and key signature changes, where ti is the time and tni, tdi and ki are the time signature numerator, time signature denominator, and key signature respectively. T and K are the numbers of time signature changes and key signature changes. A MIDI score can be obtained by combining information from X and Y. 

## 2.2 From beat tracking to rhythm quantisation 

Considering rhythm quantisation as a fine-grained tracking of beats and beat subdivisions, we propose to do rhythm quantisation by combining beat tracking and the prediction of musical note onset times in subdivisions within a beat. We use a deep learning model for both beat tracking and musical onset time prediction. Adding the beat tracking component allows the two components to learn from each other. It also allows us to use training data such as [23] that has beat-level annotations, but do not provide fine-grained alignment in subdivision level. 

We define mon in Eq. (2) as a ratio of: 



<!-- Start of picture text -->
mon = sn/S (6)<br><!-- End of picture text -->

where sn is the musical note onset time in subdivisions within a beat, and S is the number of subdivisions per beat in rhythm quantisation. 

In our proposed approach, we first train a deep learning model to predict in-note beats in a binary classification task, and then use dynamic programming to infer out-ofnote beats from the in-note ones. 

## 2.3.2 In-note beat prediction 

Let the ground truth in-note beat labels for each note in the note sequence be Bn ∈{0, 1}. We define a binary classification model that predicts the in-note beat probabilities for each note given the note sequence X, that is: 



<!-- Start of picture text -->
Pn = P (Bn|X) (7)<br><!-- End of picture text -->

The model is trained to find the minimum binary crossentropy loss defined as: 



<!-- Start of picture text -->
N<br>L = − N 1 � (Bn ∗ log(Pn) + (1 − Bn) ∗ log(1 − Pn))<br>n=1<br><!-- End of picture text -->



<!-- Start of picture text -->
(8)<br><!-- End of picture text -->

In order to acquire the beat and downbeat predictions, we use a CRNN with 3 convolutional layers and 2 bidirectional gated recurrent unit (GRU) layers. Figure 1 shows the model architecture. The predicted in-note beat probabilities are then converted to binary labels by dynamic thresholding. The dynamic threshold depends on the maximum predicted probability in a fixed segment length in seconds. 

## 2.3.3 Out-of-note beat prediction 

We assume there are in total N<sup>i</sup> in-note beats and out-ofnote beats are at subdivisions of their neighbouring in-note beats b<sup>i</sup> n<sup>andbi</sup> n+1<sup>whereb</sup> n<sup>imeansthen-thin-notebeat</sup> 

396 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

## Al <mark>g</mark> orithm 1 Out-of-note beat <mark>p</mark> rediction 

Input: List of in-note beats B<sup>i</sup> 

Output: List of all beats B after adding out-of-note beats 

- 1: n ← 1 

- 2: for K = 0, 1, 2, 3 do 

- 3: Initialise objective function OK ← 0 

- 4: Initialise beat sequence BK ←{b1} 

- 5: end for 

6: for n = 1, 2, . . . , N<sup>i</sup> − 2 do 

7: for Kcur = 0, 1, 2, 3 do 8: Get out-of-note beats for current step by Eq. (9) 

9: if Tempo is beyond tempo range limits then 10: Go to next Kcur 11: end if 12: for Kprev = 0, 1, 2, 3 do 13: Update objective function by Eq. (11) 14: end for 15: Select the minimum objective among all Kprev values 

16: Add out-of-beats for current step to the beat sequence mapped to the selected Kprev 

17: end for 18: for Kcur = 0, 1, 2, 3 do 19: Update OK, BK mapped with Kcur 20: end for 

- 21: end for 

22: Return the beat sequence in BK with the minimum objective function OK 

and n ∈{1, 2, . . . , N<sup>i</sup> }. We insert out-of-note beats b<sup>o</sup> from candidates in: 



<!-- Start of picture text -->
k<br>b o n,K = {b n i + K + 1 ( b n i +1 − b n i )} k K =1 (9)<br><!-- End of picture text -->

where K ∈{0, 1, 2, 3} is the number of out-of-note beats to insert for the current interval. We try to find a way that minimises the tempo change after adding out-of-note beats to the beat sequence. To describe the level of tempo change for a list of beats, we define an objective function as follows: 



<!-- Start of picture text -->
N −2<br>O1 = � � bn+2 − bn+1 (10)<br>n=1 ����log bn+1 − bn � � ���<br><!-- End of picture text -->

where N is the number of beats in the final beat sequence and bn is the n-th beat. However, this function does not take into account adding too many out-of-note beats. We thus add a penalty associated with the number of out-ofnote beats to the objective function, resulting in: 



<!-- Start of picture text -->
O = O1 + λ × N o (11)<br><!-- End of picture text -->

where λ is the penalty coefficient applied to avoid adding too many out-of-note beats which is tuned based on experiments and N<sup>o</sup> is the number of out-of-note beats added. In this way, we obtain an objective function O to be minimised in the out-of-note beat prediction process that encourages both a low level of tempo change and adds fewer out-of-note beats. 



<!-- Start of picture text -->
GRUBlock Linear (200 ) tempo<br>ConvBlock GRUBlock Linear (1) downbeats<br>GRUBlock Linear (1) beats<br>ConvBlock GRUBlock Linear (24) musical onsets<br>Note sequence ConvBlock GRUBlock Linear (96) note values<br>Linear (5) time signature numerators<br>ConvBlock GRUBlock<br>Linear (4) time signature denominators<br>ConvBlock GRUBlock Linear (12) key signatures<br>ConvBlock GRUBlock Linear (1) hand parts<br>concatenate<br>disable back propagation during training<br><!-- End of picture text -->

Figure 2. Model architecture for performance MIDI-toscore conversion. 

We use a dynamic programming algorithm (defined in Algorithm 1) to find the optimal out-of-note beats while minimizing O. 

## 2.4 Performance MIDI-to-Score 

Based on the problem definition in Section 2.1, we make some modifications to the prediction of time signature and key signature changes. In our proposed model, we define Yt and Yk in a way that the time signature and key signature values are mapped with each note by the note onsets. We also add beat bn, downbeat dbn, and tempo temn prediction in note level. Beat probabilities are defined as in Eq. (7); similar definitions are used for downbeats. As a result, we define our model as X → Y<sup>′</sup> where: 



<!-- Start of picture text -->
Y ′ = {(mon, nvn, hn, tnn, tdn, kn, bn, dbn, temn)} N n=1<br>(12)<br><!-- End of picture text -->

We then define a CRNN-based model that maps the input note sequence X with Y<sup>′</sup> . Among the output elements, hand part hn, beats bn and downbeats dbn are defined as binary classification tasks; the others are defined as multiclass classification tasks, where 

- Musical onset mon is defined as in Eq. (6), whose value is quantised by beat subdivisions; 

- Note values nvn are quantised by beat subdivisions; 

- Time signature is defined to be tnn ∈{0, 2, 3, 4, 6} and tdn ∈{0, 2, 4, 8}, 0s indicate other values; 

- Key signature kn is defined to be in {C, Db, D, Eb, E, F, Gb, G, Ab, A, Bb, B}; 

- Tempo is quantised following a minimum inter-beatinterval of 0.01s. 

Our proposed model structure is shown in Figure 2. The Convolutional blocks (ConvBlock) and GRU blocks (GRUBlock) have similar structure to the ones in Figure 1. Links between branches allow the output elements to learn from each other. The model is trained jointly using binary cross-entropy loss for binary classification output elements and negative log-likelihood loss for multi-task classification output elements. 

A MIDI score can then be generated by combining the information given in the performance MIDI and the output 

397 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

|Statistics|Train|Valid|Test|Total|
|---|---|---|---|---|
|Distinct pieces|426|49|29|504|
|Performances|1324|157|29|1510|
|Duration (hour)|108.3|12.7|2.2|123.2|
|Notes(10<sup>3</sup>)|3984.0|517.6|73.2|4574.7|



Table 1. Dataset Statistics. Performances from the MAPS dataset and the CPM database for the same piece are not counted as different performances, since MAPS pieces are originally obtained from the CPM database. 

predictions from our proposed model. 

## 3. EXPERIMENTS 

## 3.1 Data 

## 3.1.1 Datasets 

To better demonstrate the ability of our proposed method on quantising expressive performance, we use a collection of classical piano music pieces from 1) The MAPS dataset [22] and corresponding metrical annotations from the A- MAPS dataset [27]; 2) The Classical Piano-Midi (CPM) database [28]; and 3) The ASAP dataset [23]. 

In order to avoid piece overlaps between train, validation and test splits, we use the distinct music piece labels for all piano performances given in the ACPAS dataset [29]. We use a real recording subset in MAPS (the ENSTDkCl subset) as the test set as in [5, 20]. Other music pieces not included in the test set are randomly split into training and validation based on their distinct music piece labels. In this way, we get a train/validation/test setup with no overlapping music pieces among splits. Table 1 shows the dataset statistics. 

## 3.1.2 Annotation 

Annotations are provided in different formats in the datasets we use. The A-MAPS dataset and the CPM database provide fully annotated MIDI scores with tempo and metrical information. Thus, we extract the annotations we need from the MIDI scores directly. Performances from the ASAP dataset come with two sets of annotations, MIDI scores and annotations in .tsv files. However, the MIDI scores were written by non-professionals and are not a good source of ground truth. Thus, we follow the authors’ suggestion to use the provided annotations in the .tsv files, in which beat, downbeat, time signature and key signature annotations are provided. Due to the fact that the .tsv annotations do not cover precise fine-grained metrical and hand part annotations, we mask the ASAP data on musical onset time, note value, and hand part prediction during training. Moreover, when matching note onset times to beats or non-beats in our proposed model, we set a tolerance of ±50ms to beat matching to comprise short-time variances introduced by human performance. 

## 3.1.3 Data augmentation 

Given the note sequence information defined in Section 2, we consider the following data augmentation methods: 

- Pitch shift: Shift MIDI pitch values up or down for the whole music performance. The shifted pitch is defined as: ps = p0 + pshift where p0 is the original pitch value and pitch shift pshift ∈ {0, ±1, ±2, ..., ±12}. 

- Tempo change: Change the tempo to a ratio of the original tempo. The new tempo temc = rt ∗ tem0 where tem0 is the original tempo and rt ∈ [0.8, 1.2] is the ratio. 

- Note removal: For polyphonic music, there should be little influence to the metrical structure of the music piece when removing some concurrent notes. Thus, for each group of M concurrent notes, we randomly remove 0 to M-1 of them from the MIDI performance. 

- Note introduction: Contrary to note removal, we randomly select 0-100% of notes from the MIDI performance, and add new notes that are concurrent with the selected ones. We keep the velocity and duration the same, so as to preserve the original music structure as much as possible. The new note pitches are ±12 semitones apart from the original note pitches. 

## 3.2 Evaluation metrics 

## 3.2.1 Beat tracking evaluation 

We define a note-level F-measure for evaluating in-note beat tracking, and a beat-level F-measure which follows the benchmark F-measure for beat and downbeat tracking [30] with a time tolerance of ±70ms. In both cases, a true positive means a predicted beat is in the ground truth; a false positive means a predicted beat is not in the ground truth; and a false negative means a ground truth beat is missing in prediction. 

For both F-measures, we report the precision p, recall r and F-score f . Similar definitions are used for downbeats. 

## 3.2.2 Performance MIDI-to-Score evaluation 

We use the MV2H metric [26] to evaluate the system performance on PM2S conversion. The metric covers five sub-metrics including multi-pitch detection (Fp), voice separation (Fvo), metrical alignment (Fme), note value detection (Fva), and harmonic analysis (Fha). The final accuracy F is the average of all the sub-metrics. 

## 3.3 Comparative experiments 

Among the subtasks in PM2S, rhythm quantisation is a crucial and difficult part. It is also highly related to the estimation of time signatures, musical onsets, and note values. In our proposed rhythm quantisation method which combines neural beat tracking and musical onset time estimation, we consider beat tracking as a more important step since it works on drawing the skeleton of the metrical grid. 

Thus, for the first part of our experiments, we investigate different input data configurations and data augmentation methods for the beat tracking part of our proposed method. To get rid of influences from out-of-note beat prediction, we use the note-level F-measure in our comparison. After that, we validate our beat tracking method on 

398 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

beat-level F-measure combining out-of-note beat prediction in comparison with a baseline beat tracking model. 

## 3.3.1 Input data encoding 

Given the input data in note sequences, we consider the following ways of encoding the input elements: 

- Pitches: 

   - ± M: 128-dimensional one-hot vectors in MIDI pitch numbers; 

   - ± C: 12-dimensional one-hot vectors in octave values. 

- Onset times: 

   - ± AR: the raw value in seconds; 

   - ± AO: one-hot vectors quantised by 10ms resolution; 

   - ± SR: onset time shift in seconds compared to the previous note onset (o<sup>shift</sup> i = oi − oi−1 for i > 

   - 0, o<sup>shift</sup> 0 = 0); 

   - ± SO: one-hot onset time-shift quantised by 10ms resolution (with a maximum onset time shift of 4s, larger values are trimmed to 4s). 

- Durations: 

   - ± R: the raw values in seconds; 

   - ± O: one-hot vectors quantised by 10ms resolution (similar to onset shift, large values are trimmed to 4s). 

- Velocities are always normalised to 0-1. 

For all possible input encoding combinations, we train and evaluate the in-note beat prediction part of our proposed model (excluding downbeat). The model learning rate is set to be 0.001. Since different input encodings can cause changes in the model convergence speed, we do not add learning rate decay in this comparison. The model is trained using a batch size of 32 over 4 GPUs with a dropout rate of 0.15. For each combination, we take the best model checkpoint on the validation set during training, and evaluate it over the test set. The performances of the model on all different input data encoding combinations are reported in Table 2. 

From the results, we can see that in terms of pitch encoding, using the MIDI pitches tends to outperform using the chroma groups most of the time. For onsets, onset shift leads to better results than absolute onset across all encoding combinations. Using one-hot encoding for onset is better than using the raw values for most cases. 6 out of 8 encoding combinations result in better model performance with onsets encoded in one-hot format. However, an opposite preference is discovered for duration encoding, where duration in raw values ends up with better results for more cases. 

Among all the 16 input data encoding combinations tested, the one with MIDI pitch, one-hot onset shift, and duration in raw value shows the best model performance. We use this input data encoding combination in our subsequent experiments. 

|Input e|ncoding|s|Note-|level F-|measure|
|---|---|---|---|---|---|
|Pitch|Onset|Duration|p|r|f|
|M|AR|R|86.7|77.7|79.9|
|M|AR|O|89.9|57.2|65.2|
|M|AO|R|82.1|78.3|79.3|
|M|AO|O|83.3|72.2|76.0|
|M|SR|R|89.2|89.4|87.8|
|M|SR|O|88.8|91.9|89.5|
|M|SO|R|91.2|94.3|91.3|
|M|SO|O|91.1|90.3|89.1|
|C|AR|R|86.7|68.7|73.6|
|C|AR|O|80.7|64.4|67.2|
|C|AO|R|82.8|76.2|78.4|
|C|AO|O|82.7|71.9|76.0|
|C|SR|R|90.4|88.0|87.3|
|C|SR|O|90.2|88.9|87.5|
|C|SO|R|89.9|91.3|89.1|
|C|SO|O|88.8|90.6|88.0|



Table 2. Model performance on different input data encoding combinations. 

|Input feature omitted|p|r|f|
|---|---|---|---|
|Pitch|90.4|93.7|90.6|
|Onset|84.6|72.8|76.4|
|Duration|89.5|93.1|90.1|
|Velocity|89.5|93.9|90.6|
|Use all features|91.2|94.3|91.3|
|Augmentation method omitted|p|r|f|
|Pitch shift|92.0|92.0|90.6|
|Tempo change|91.7|89.5|89.7|
|Note removal|91.5|90.9|90.4|
|Extra note|91.2|94.3|91.3|
|Use all methods|92.9|93.7|92.2|
|No data augmentation|89.7|95.2|90.9|



Table 3. Note-level F-measure results on the ablation studies. 

## 3.3.2 Ablation studies 

Using the best input encoding combination observed in the previous comparison, we run an ablation study on the input features and different data augmentation techniques. We use all four input features when exploring different data augmentation methods. 

Table 3 shows the ablation study results. From the table, we see that all four input features are helpful in beat tracking, among which the onset feature is the most beneficial one. This is consistent with the fact that onsets can be the feature to carry most metrical information in music performances. People can usually infer beat times from drum beats without knowing other information such as pitch or duration. Pitch and velocity are less important but still make a difference. That may be because pitch carries some harmony information that helps beat prediction. Velocity can provide useful information as well since beats are more probable to be concurrent with heavy notes. Finally, duration is of certain importance, suggesting it carries more metrical information than pitch and velocity. 

399 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

|Models(output data)|fb|fdb|
|---|---|---|
|Baseline (b, db)|66.9|57.6|
|Proposed (b, db)|85.7|63.3|
|Proposed(d,db,t)|86.2|69.8|



Table 4. Beat-level F-measure results on the baseline and proposed models. b: beat, db: downbeat, t: tempo. 

|Methods|Fp|Fvo|Fme|Fva|Fha|F|
|---|---|---|---|---|---|---|
|Finale|82.2|54.6|9.9|92.2|86.2|65.0|
|MuseScore|10.0|65.0|15.3|95.0|84.5|54.0|
|Proposed|99.8|87.0|61.7|99.9|91.1|87.9|



Table 5. MV2H evaluation on performance MIDI-to-score conversion. 

Results on different data augmentation methods suggest that all four proposed data augmentation methods improve performance, among which tempo change is the most beneficial one. Not performing data augmentation does not result in the lowest note-level F-score. However, its low precision rate indicates a limitation on predicting more false positives, which is discouraged since we will be adding out-of-note beats based on the predicted in-note beats. It is possible that we can add the false negatives back when predicting out-of-note beats, but we cannot remove the false positives. 

## 3.3.3 Proposed model vs. baseline model 

Using the best configurations in previous experiment results, we combine the out-of-note beat prediction step and evaluate our proposed model performance on beat tracking using beat-level F-measure. We compare our method with a baseline model that is similar to a state-of-the-art audio beat tracking model [31]. We retrain the baseline model using a pianoroll input replacing the original audio spectrogram input, where the pianoroll is calculated from the performance MIDI, and let the model predict beat and downbeat probabilities. The probabilities are then passed to a dynamic Bayesian network [32, 33] to get beats and downbeats in seconds. 

Table 4 shows the comparative results between the baseline and our proposed model. Results suggest our proposed model largely outperforms the baseline when jointly trained with beats and downbeats. This is possibly because that the baseline model is a general purpose system designed to operate on richer content than piano music alone, and that our proposed model can better handle tempo changes. By adding tempo to the output data, the performance of our proposed model can be further improved, which suggests a benefit of joint learning. 

## 3.4 System performance evaluation 

Using the best configurations found in the comparative experiments, we train and evaluate our proposed CRNN model defined in Section 2.4 on PM2S conversion. We report the model performance on the MV2H metric described in Section 3.2.2. 

When looking for other methods for comparison, we realise that there are some difficulties in comparing our system with existing academic works. Cogliati et al. [14] evaluated their method in a subjective way by inviting five music theory students to rate the transcribed musical scores. Works such as [5, 19, 34] do provide a combination of methods to achieve PM2S conversion, however, the system performance was reported on audio-to-score transcription. Thus, we compared our proposed method with two commercial software products Finale v27 [25] and MuseScore v3 [24] that can do PM2S conversion. 

Results in Table 5 suggest that our proposed model outperforms MuseScore and Finale across all MV2H submetrics. A significantly better performance can be observed in the metrical alignment sub-metric Fme which is highly related to the rhythm quantisation step. By checking outputs generated from MuseScore, we found that its low performance on Fp is caused by time shifts introduced when quantising notes according to a constant tempo estimated over the whole music piece. Constant tempo estimation also caused its low performance reported on Fme. A similar limitation can be found in output scores from Finale. On the contrary, our proposed method tracked tempo changes during rhythm quantisation and preserved the expressiveness of music performance as much as possible. This not only benefits metrical alignment, but also results in high accuracies on Fp and Fva. Still, the rhythm quantisation performance (Fme) is far from satisfactory. Some typical errors include double/half tempo error and errors introduced by missing/extra beat predictions. 

To provide a better understanding of the performance of our proposed method, we provide some example outputs from our model together with their performance MIDI recordings<sup>1</sup> . 

## 4. CONCLUSION 

We described our proposed method for rhythm quantisation by using a CRNN beat tracking model that predicts whether notes are at a beat position or not. We explored different input data encoding and data augmentation methods on the beat tracking model. We found that note onset time is the most important input feature in beat prediction and it is best to encode it into a one-hot onset-shift vector. Tempo change benefits most among the data augmentation methods explored. We validated our model’s beat tracking ability in comparison with a pianoroll-input baseline model. In the end, we report the performance of our proposed system on PM2S conversion in comparison with MuseScore and Finale. 

Possible next steps include investigating more powerful model architectures such as the Transformer [35], expanding the output data to generate a machine-readable score [21], probing our system’s ability in dealing with more genre and instrumentation [19,36,37], and exploring our method’s potential in automatic music transcription by combining multi-pitch detection [38,39]. 

> 1 Example outputs: https://cheriell.github.io/ research/PM2S 

400 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

## 5. ACKNOWLEDGEMENTS 

L. Liu is a research student at the UKRI Centre for Doctoral Training in Artificial Intelligence and Music, supported jointly by the China Scholarship Council and Queen Mary University of London. The work of L. Liu is supported by The Alan Turing Institute through an Enrichment Scheme. 

We would like to thank Huan Zhang, Changhong Wang and the reviewers for their valuable feedback to improve our work. 

## 6. REFERENCES 

- [1] M. Good, ªMusicXML: An internet-friendly format for sheet music,º XML Conference and Expo, pp. 1±12, 2001. [Online]. Available: http://citeseerx.ist.psu.edu/viewdoc/download? doi=10.1.1.118.5431&rep=rep1&type=pdf 

- [2] H.-W. Nienhuys and J. Nieuwenhuizen, ªLilypond, a System for Automated Music Engraving,º in Proceedings of the XIV Colloquium on Musical Informatics (XIV CIM 2003), 2003, pp. 167±171. 

- [3] S. D. Reeves and T. T. P. Walsh, Creative jazz improvisation. Taylor & Francis, 2022. 

- [4] R. G. C. Carvalho and P. Smaragdis, ªTowards Endto-End Polyphonic Music Transcription: Transforming Music Audio Directly to A Score,º in IEEE Workshop on Applications of Signal Processing to Audio and Acoustics, vol. 2017-Octob, 2017, pp. 151±155. 

- [5] E. Nakamura, E. Benetos, K. Yoshii, and S. Dixon, ªTowards Complete Polyphonic Music Transcription: Integrating Multi-Pitch Detection and Rhythm Quantization,º in ICASSP, IEEE International Conference on Acoustics, Speech and Signal Processing, vol. 2018April. IEEE, 2018, pp. 101±105. 

- [6] L. Liu and E. Benetos, ªFrom Audio to Music Notation,º in Handbook of Artificial Intelligence for Music, E. R. Miranda, Ed. Springer, 2021, pp. 693±714. 

- [7] L. Liu, V. Morfi, and E. Benetos, ªJoint Multi-pitch Detection and Score Transcription for Polyphonic Piano Music,º in ICASSP, IEEE International Conference on Acoustics, Speech and Signal Processing, 2021. 

- [8] J. Huang, E. Benetos, and S. Ewert, ªImproving Lyrics Alignment through Joint Pitch Detection,º in ICASSP, IEEE International Conference on Acoustics, Speech and Signal Processing. Institute of Electrical and Electronics Engineers (IEEE), 2 2022, pp. 451± 455. [Online]. Available: https://arxiv.org/abs/2202. 01646v1 

- [9] B. Li, X. Liu, K. Dinesh, Z. Duan, and G. Sharma, ªCreating a Multitrack Classical Music Performance Dataset for Multimodal Music Analysis: Challenges, 

Insights, and Applications,º IEEE Transactions on Multimedia, vol. 21, no. 2, pp. 522±535, 2019. 

- [10] P. Desain and H. Honing, ªThe Quantization of Musical Time: A Connectionist Approach,º Computer Music Journal, vol. 13, no. 3, pp. 56±66, 1989. 

- [11] D. Temperley and D. Sleator, ªModeling meter and harmony: A preference-rule approach,º Computer Music Journal, vol. 23, no. 1, pp. 10±27, 1999. 

- [12] C. Raphael, ªAutomated Rhythm Transcription,º in ISMIR, 2001, pp. 99±107. 

- [13] H. Takeda, N. Saito, T. Otsuki, M. Nakai, H. Shimodaira, and S. Sagayama, ªHidden Markov model for automatic transcription of MIDI signals,º Proceedings of 2002 IEEE Workshop on Multimedia Signal Processing, MMSP 2002, pp. 428±431, 2002. 

- [14] A. Cogliati, D. Temperley, and Z. Duan, ªTranscribing Human Piano Performance into Music Notation,º in ISMIR, 2016. 

- [15] D. Temperley, ªA unified probabilistic model for polyphonic music analysis,º Journal of New Music Research, vol. 38, no. 1, pp. 3±18, 2009. 

- [16] E. Nakamura, K. Yoshii, and S. Sagayama, ªRhythm Transcription of Polyphonic Piano Music Based on Merged-Output HMM for Multiple Voices,º IEEE/ACM Transactions on Audio Speech and Language Processing, vol. 25, no. 4, pp. 794±806, 2017. 

- [17] E. Nakamura, K. Yoshii, and S. Dixon, ªNote Value Recognition for Piano Transcription Using Markov Random Fields,º IEEE/ACM Transactions on Audio Speech and Language Processing, vol. 25, no. 9, pp. 1542±1554, 2017. 

- [18] A. McLeod and M. Steedman, ªMeter detection and alignment of MIDI performance,º Proceedings of the 19th International Society for Music Information Retrieval Conference, ISMIR 2018, pp. 113±119, 2018. 

- [19] K. Shibata, E. Nakamura, and K. Yoshii, ªNonLocal Musical Statistics as Guides for Audioto-Score Piano Transcription,º arXiv preprint arXiv:2008.12710, 2020. [Online]. Available: http: //arxiv.org/abs/2008.12710 

- [20] Y. Hiramatsu, E. Nakamura, and K. Yoshii, ªJoint Estimation of Note Values and Voices for Audio-to-Score Piano Transcription,º in ISMIR. International Society for Music Information Retrieval Conference, 2021, pp. 278±284. 

- [21] M. Suzuki, ªScore Transformer: Generating Musical Score from Note-level Representation,º in ACM International Conference Proceeding Series, vol. 1, 2021. 

401 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

- [22] V. Emiya, R. Badeau, and B. David, ªMultipitch Estimation of Piano Sounds Using a New Probabilistic Spectral Smoothness Principle,º IEEE Transactions on Audio, Speech and Language Processing, vol. 18, no. 6, pp. 1643±1654, 2010. 

- [23] F. Foscarin, A. Mcleod, P. Rigaux, F. Jacquemard, and M. Sakai, ªASAP: A Dataset of Aligned Scores and Performances for Piano Transcription,º in ISMIR, International Society for Music Information Retrieval Conference, 2020. 

- [24] ªMuseScore.º [Online]. Available: https://musescore. org 

- [25] ªFinale music notation software.º [Online]. Available: https://www.finalemusic.com 

- [26] A. Mcleod and M. Steedman, ªEvaluating Automatic Polyphonic Music Transcription,º in ISMIR, International Society for Music Information Retrieval Conference, 2018, pp. 42±49. [Online]. Available: https://www.github.com/apmcleod/MV2H. 

- [27] A. Ycart and E. Benetos, ªA-MAPS: Augmented MAPS Dataset with Rhythm and Key Annotations,º in ISMIR, International Society for Music Information Retrieval Conference, Late-Breaking Demo, 2018. 

- [28] ªClassical Piano-Midi Database.º [Online]. Available: http://www.piano-midi.de 

   - [35] Y.-H. Chou, I.-C. Chen, C.-J. Chang, J. Ching, and Y.H. Yang, ªMidiBERT-Piano: Large-scale Pre-training for Symbolic Music Understanding,º arXiv preprint arXiv: 2107.05223, 7 2021. [Online]. Available: https://arxiv.org/abs/2107.05223v1 

   - [36] K. Tanaka, T. Nakatsuka, R. Nishikimi, K. Yoshii, and S. Morishima, ªMulti-instrument Music Transcription Based on Deep Spherical Clustering of Spectrograms and Pitchgrams,º in ISMIR, International Society for Music Information Retrieval Conference, 2020, pp. 327±334. 

   - [37] Y. T. Wu, B. Chen, and L. Su, ªMulti-Instrument Automatic Music Transcription with Self-Attention-Based Instance Segmentation,º IEEE/ACM Transactions on Audio Speech and Language Processing, vol. 28, pp. 2796±2809, 2020. 

   - [38] Q. Kong, B. Li, X. Song, Y. Wan, and Y. Wang, ªHigh-resolution Piano Transcription with Pedals by Regressing Onsets and Offsets Times,º arXiv preprint arXiv:2010.01815, pp. 1±10, 2020. [Online]. Available: http://arxiv.org/abs/2010.01815 

   - [39] R. M. Bittner, J. J. Bosch, D. Rubinstein, G. MeseguerBrocal, and S. Ewert, ªA Lightweight InstrumentAgnostic Model for Polyphonic Note Transcription and Multipitch Estimation,º in ICASSP, 2022, pp. 781± 785. 

- [29] L. Liu, V. Morfi, and E. Benetos, ªACPAS: A Dataset of Aligned Classical Piano Audio And scores for Audio-To-Score Transcription,º in ISMIR LateBreaking Demo, 2021, pp. 2±4. 

- [30] M. E. P. Davies, N. Degara, and M. D. Plumbley, ªEvaluation Methods for Musical Audio Beat Tracking Algorithms,º Centre for Digital Music, Queen Mary University of London, Tech. Rep., vol. C4DM-TR-09, no. October, p. 17, 2009. 

- [31] S. Böck and M. E. P. Davies, ªDeconstruct, Analyse, Reconstruct: How To Improve Tempo, Beat, and Downbeat Estimation,º in ISMIR, International Society for Music Information Retrieval Conference, 2020. 

- [32] S. Böck, F. Krebs, and G. Widmer, ªA multi-model approach to beat tracking considering heterogeneous music styles,º Proceedings of the 15th International Society for Music Information Retrieval Conference, ISMIR 2014, pp. 603±608, 2014. 

- [33] F. Krebs, S. Böck, and G. Widmer, ªAn efficient statespace model for joint tempo and meter tracking,º Proceedings of the 16th International Society for Music Information Retrieval Conference, ISMIR 2015, pp. 72± 78, 2015. 

- [34] A. Mcleod, ªEvaluating Non-Aligned Musical Score Transcriptions with MV2H,º in ISMIR, International Society for Music Information Retrieval Conference, Late-Breaking Demo, 2019. 

402 

