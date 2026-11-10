---
paper_id: "000058"
year: 2022
title: "Download pdf"
source_url: "https://zenodo.org/record/7316706/files/000058.pdf"
---

# MELODY TRANSCRIPTION VIA GENERATIVE PRE-TRAINING 

Chris Donahue Stanford University 

John Thickstun Percy Liang Stanford University Stanford University 

## ABSTRACT 

Despite the central role that melody plays in music perception, it remains an open challenge in MIR to reliably detect the notes of the melody present in an arbitrary music recording. A key challenge in melody transcription is building methods which can handle broad audio containing any number of instrument ensembles and musical stylesÐ existing strategies work well for some melody instruments or styles but not all. To confront this challenge, we leverage representations from Jukebox [1], a generative model of broad music audio, thereby improving performance on melody transcription by 20% relative to conventional spectrogram features. Another obstacle in melody transcription is a lack of training dataÐwe derive a new dataset containing 50 hours of melody transcriptions from crowdsourced annotations of broad music. The combination of generative pre-training and a new dataset for this task results in 77% stronger performance on melody transcription relative to the strongest available baseline.<sup>1</sup> By pairing our new melody transcription approach with solutions for beat detection, key estimation, and chord recognition, we build Sheet Sage, a system capable of transcribing humanreadable lead sheets directly from music audio. 

## 1. INTRODUCTION 

In the Western music canon, melody is a defining characteristic of musical composition, and can even constitute the very identity of a piece of music within the collective consciousness. Because of the significance of melody to our music perception, the ability to automatically transcribe the melody notes present in an arbitrary recording could enable numerous applications in interaction [2], education [3], informatics [4], retrieval [5], source separation [6], and generation [7]. Despite the potential benefits, reliable melody transcription remains an open challenge. A closely-related problem that has received considerable attention from the MIR community is melody extraction [8±11], where the goal is to estimate the time-varying, continuous F0 trajectory of the melody in an audio mixture. In contrast, the goal of melody transcription is to out- 

> 1 Examples: https://chrisdonahue.com/sheetsage Code: https://github.com/chrisdonahue/sheetsage 

> © C. Donahue, J. Thickstun, and P. Liang. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: C. Donahue, J. Thickstun, and P. Liang, ªMelody transcription via generative pre-trainingº, in Proc. of the 23rd Int. Society for Music Information Retrieval Conf., Bengaluru, India, 2022. 



<!-- Start of picture text -->
G4 Renders to :<br>F4 MIDI<br>E4 Score<br>E4 F4 G4<br>Transformer<br>One input / output per sixteenth note<br>+ + + + + +<br>Jukebox<br>Outputs are uniformly spaced in time<br><!-- End of picture text -->

Figure 1. Our melody transcription approach involves (1) extracting audio representations from Jukebox [1], a generative model of music, (2) averaging these representations across time to their nearest sixteenth note (dashed outlineÐuses madmom [12, 13] for beat detection), and (3) training a Transformer [14] to detect note onsets (or absence thereof) per sixteenth note. Outputs can be rendered to MIDI (by mapping beats back to time) or a score. 

put the notes of the melody, where a note is defined by an onset time, a pitch, and an offset time. While F0 trajectories are useful for several downstream tasks (e.g., query by humming) and more inclusive of music which does not use equal-tempered pitches, unlike notes, trajectories cannot be readily converted into formats like MIDI or scores which are more convenient for musicians. 

The relative lack of progress on melody transcription is perhaps counterintuitive when compared to the considerable progress on seemingly more difficult tasks like piano transcription [15, 16]. This circumstance stems from two primary factors. First, unlike in piano transcription, melody transcription involves operating on broad audio mixtures from arbitrary instrument ensembles and musical styles. Second, there is a deficit of training data for melody transcription, which particularly impedes the deep learning approaches central to recent improvements on other transcription tasks. Moreover, collecting data for melody tran- 

485 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

scription is difficult compared to collecting data for tasks like piano transcription, where a Disklavier can be used to create aligned training data in real time. 

To overcome the challenge of transcribing broad audio, in this work we leverage representations from Jukebox [1], a large-scale generative model of music audio pre-trained on 1M songs. In [17], Castellon et al. demonstrate that representations from Jukebox are useful for improving performance on a wide variety of MIR tasks. Here we show that, when used as input features to a Transformer model [14], representations from Jukebox yield 27% stronger performance on melody transcription (as measured by note-wise F1) relative to handcrafted spectrogram features conventionally used for transcription. To our knowledge, this is the first evidence that representations learned via generative modeling are useful for time-varying MIR tasks like transcription, as opposed to the song-level tasks (e.g. tagging, genre detection) examined in [17]. 

To address the data deficit for melody transcription, we release a new dataset containing 50 hours of melody annotations for broad audio which we derive from HookTheory.<sup>2</sup> The user-specified alignments between the audio and melody annotations in HookTheory are crudeÐ we refine these alignments using beat detection. To overcome remaining alignment jitter, we resample features to be uniformly spaced in beats (rather than time) and pass these beat-wise resampled features as input to melody transcription models. This procedure has a secondary benefit of enabling simple conversion from raw model outputs to human-readable scores (Figure 1). 

By training Transformer models on this new dataset using representations from Jukebox as input, we are able to improve overall performance on melody transcription by 70% relative to the strongest available baseline. A summary of our primary contributions follows: 

- We show that representations from generative models can improve melody transcription (Section 6). 

- We collect, align, and release a new dataset with 50 hours of melody and chord annotations (Section 4). 

- We propose a method for training transcription models on data with imprecise alignment (Section 5.3). 

- As a bonus application of our melody transcription approach, we build a system which can transcribe music audio into lead sheets (Section 7). 

## 2. RELATED WORK 

Melody transcription is closely related to but distinct from the task of melody extraction, originally referred to as predominant fundamental frequency (F0) estimation [8, 9]. Melody extraction has received significant interest from the MIR community over the last two decades (see [10,11] for comprehensive reviews), and is the subject of an annual MIREX competition [18]. Melody extraction may be 

a component of a melody transcription pipeline in combination with a strategy to segment F0 into notes [19±21]Ð we directly compare to such a pipeline in Section 6.2. 

Compared to melody extraction, melody transcription has received considerably less attention. Earlier efforts use sophisticated DSP-based pipelines [22± 25]Ðunfortunately none of these methods provide code, though [24] provides example transcriptions which we use to facilitate direct comparison. A more recent effort uses ground truth chord labels as extra information to improve melody transcription [26]Ðin contrast, our method does not require extra information. Another line of work seeks to transcribe solo vocal performances into notes [27±30]. As singing voice often carries the melody in popular music, we directly compare to a baseline which firsts isolates the vocals (using Spleeter [31]) and then transcribes them. 

Polyphonic music transcription is another related task which involves transcribing all of the notes present in a recording (not just the melody). This task has its own MIREX contest (Multiple Fundamental F0 Estimation) alongside a growing collection of supervised training data resources [7,32±34]. The similarity of the polyphonic and melody transcription problems motivates us to experiment with representations learned by a polyphonic systemÐ specifically, MT3 [35]Ðfor melody transcription. 

## 3. TASK DEFINITION 

In this work, melody transcription refers to the task of converting a music recording into a monophonic (nonoverlapping) sequence of notes which constitute its dominant melody.<sup>3</sup> More precisely, given a music waveform a of length T seconds, our task is to uncover the sequence of N notes y = [y1, . . . , yN ] that represent the melody of a. For many MIR tasks, including transcription, it can be convenient to work with features of audio X = Featurize(a), rather than waveforms. Hence, a melody transcription algorithm is a procedure that maps featurized audio to notes, i.e. y = Transcribe(X). 

Canonically, a musical note consists of an onset time, a musical pitch, and an offset time. However, in this work we disregard offsets and define a note to be a pair yi = (ti, ni) consisting of an onset time ti ∈ [0, T ) and discrete musical pitch ni ∈ V = {A0, . . . , C8}. We ignore offsets for two reasons. First, accurate offsets have been found to be considerably less important for human perception of transcription quality compared to accurate onsets [36]. Second, in our dataset, a heuristically-determined offset is identical to the user-annotated offset for 89% of notes.<sup>4</sup> 

Formally, a musical audio recording of length T seconds sampled at rate fs is a vector a ∈ R<sup>T fs</sup> . A featurization of audio X ∈ R<sup>T fk×d</sup> is a matrix of d-dimensional features of audio, sampled uniformly at some rate fk ≪ fs (for example, X could be a spectrogram). Intuitively, the function Featurize : R<sup>T fs</sup> → R<sup>T fk×d</sup> defined by 

> 3 Melody is difficult to precisely defineÐhere we adopt an implicit definition based on a dataset of crowdsourced melody annotations. 

> 4 The specific heuristic that we use sets the offset of one note equal to the onset of the next, i.e., it assumes the melody is legato. 

2 https://www.hooktheory.com/theorytab 

486 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

a �→ X maps raw audio to a feature representation more conducive to learning. A melody of length N is a sequence of notes y = [y1, . . . , yN ] ∈ Y<sup>N</sup> consisting of onset-pitch pairs yi = (ti, ni) ∈ Y = R<sup>+</sup> × V where ti < tj if i < j. Given a featurization X, the melody transcription task is to construct a transcription algorithm Transcribe : R<sup>T fk×d</sup> → Y<sup>N</sup> such that X �→ y. 

## 3.1 Evaluation 

To evaluate a melody transcription method Transcribe, we adopt a standard metric commonly used for evaluation in polyphonic music transcription tasks, namely, ªonsetonly note-wise F-measureº [36]. This metric scores an estimated transcript Transcribe(X) by first matching its note onsets to those in the reference y with 50ms of tolerance (default in [37]), and then computes a standard F1 score where an estimated note is treated as correct if it is the same pitch as its matched reference note. This ªnote-wiseº metric represents a departure from the ªframebasedº metrics typically used to evaluate melody extraction algorithmsÐYcart et al. demonstrate in [36] that this particular note-wise metric correlates more strongly with human perception of transcription quality than any other common metric, including frame-based ones. 

We make a slight modification to this note-wise metric specific to the melody transcription setting: an estimate Transcribe(X) may receive full credit if it is off by a fixed octave shift but otherwise identical to the reference. In downstream settings, melody transcriptions are likely to be used in an octave-invariant fashion, e.g., they may be shifted to read more comfortably in treble clef, or performed by singers with different vocal ranges. Hence, we modify the evaluation criteria by simply taking the highest score over octave shifted versions of the estimate: 

max σ∈Z<sup>F1(OctaveShift(Transcribe(X), σ), y).</sup> 

audio content covers a wide range of genresÐthere is a skew towards pop and rock but many other genres are represented including EDM, jazz, and even classical. We create an artist-stratified 8:1:1 split of the dataset for training, validation, and testing. The dataset also includes chord annotations which may facilitate chord recognition research. 

While HookTheory data has been used previously for MIR tasks like harmonization [41, 42], chord recognition [43], and representation learning [44], making use of this platform for MIR is currently cumbersome. One obstacle is that the annotations are created via a ªfunctionalº interface, i.e., one which uses scale degrees and roman numerals relative to a key signature instead of absolute notes and chord names. In contrast, most MIR research favors absolute labels. Hence, we convert annotations from this functional format to a simple (JSON-based) absolute format. One caveat is that the HookTheory annotation interface uses a relative octave system, so there is no way to reliably map annotations to a ground truth octave. Thus, melodies in our dataset also contain only relative octave information, consistent with the octave-invariant evaluation proposed in Section 3.1. 

## 5. METHODS 

Similar to state-of-the-art methodology used for polyphonic transcription [45], our approach to melody transcription involves training Transformer models [14] to predict notes from audio features. However, to address the unique challenges of melody transcription, our approach differs in two distinct ways. First, because melody transcription involves operating on broad audio, we leverage representations from pre-trained models as drop-in replacements for the handcrafted spectrogram features used as inputs to other transcription systems. Secondly, because alignments in our dataset are approximate, we propose a new strategy for training transcription models under such conditions. 

Henceforth, we refer to this octave-invariant metric as F1. 

## 5.1 Pre-trained representations 

## 4. DATASET OVERVIEW 

A major obstacle to progress on melody transcription is the lack of a large volume of data for training. To the best of our knowledge, there are only two datasets available with annotations suitable for melody transcription: the RWC Music Database [38±40] (RWC-MDB), and a dataset labeled by Laaksonen [26]. The former is larger but the annotations are inconsistentÐRyynänen and Klapuri note that only 8.7 hours (130 songs) are usable for melody transcription [24], while the latter only contains 1.5 hours. 

We derive a suitably large dataset for melody transcription using crowdsourced annotations from HookTheory.<sup>5</sup> HookTheory is a platform where users can easily create and share musical analyses of particular recordings hosted on YouTube, with Wikipedia-style editing. The dataset contains annotations for 22k segments of 13k unique recordings totaling 50 hours of labeled audio. The 

> 5 HookTheory annotations are published under a CC BY-NC-SA 3.0 license, which our dataset inherits. 

We explore representations from two different pre-trained models for use as input features to transcription models. In [17], Castellon et al. demonstrate that representations from Jukebox [1]Ða generative model of music audio pre-trained on 1M songsÐconstitute effective features for many MIR tasks, though notably they do not experiment on transcription. We adopt their approach to extract features from Jukebox (fk ≈ 345 Hz, d = 4800), though we use a deeper layer (53) than their default (36) which improved transcription performance in our initial experiments. 

We also explore features from MT3 [35], an encoderdecoder transcription model pre-trained on a multitude of different transcription tasks (though not melody transcription). For this model, we use the encoder’s outputs as features (fk = 125 Hz, d = 512). The two models have different trade-offs with respect to our setting: Jukebox was pre-trained on audio similar to that found in our dataset but in a generative fashion, whereas MT3 is pre-trained on transcription but for different audio domains. 

487 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
User-specified alignment<br>Refined alignment<br><!-- End of picture text -->

Figure 2. We refine the crude user-specified alignments from HookTheory by using beat and downbeat tracking. The first segment beat is mapped to the detected downbeat nearest to the user-specified starting timestamp, and remaining beats are mapped to subsequent detected beats. 

## 5.2 Refined Alignments 

The alignments between audio and HookTheory annotations are crudeÐusers provide only an approximate starting and ending timestamp of their annotated segment within the audio. Because transcription methodology generally depends on precise alignments, we make an effort to refine the user-specified ones. To this end, we make use of the beat and downbeat detection algorithm from madmom [12, 13]. Specifically, our approach aligns the first beat of the segment to the detected downbeat which is nearest to the user-specified starting timestamp. Then, we align the remaining beats to the subsequent detected beats (see Figure 2 for an example). This provides a beat-level alignment for the entire segment, which we linearly interpolate to fractional subdivisions of the beat. Formally, we construct an alignment function Align : [0, B) → [0, T ) that assigns each of B beats in the metrical structure to a time t ∈ [0, T ) in the audio. In an informal listening test, this produced an improved alignment for 95 of 100 segments, where the primary failure mode in the remaining 5 segments occurred when madmom detected the wrong beat as the downbeat. We use these refined alignments for training and evaluation and release them alongside the dataset. 

## 5.3 Beat-wise resampling 

Here we outline our approach for training transcription models in the presence of imprecise alignments. Existing transcription methods were largely designed for domains where perfect alignments are readily available, e.g., piano transcription data captured by a Disklavier. Despite our best efforts, the refined HookTheory alignments are still imprecise when compared to alignments in the datasets used to develop existing methods. Consequently, in initial experiments, we found that naively adopting existing methods (specifically, [16, 45]) resulted in poor performance on our dataset and task. Additionally, initial experiments on training models with an alignment-free approach [46] also resulted in poor performance. 

Accordingly, to sidestep small alignment deviations, we perform a beat-wise resampling of audio features X ∈ R<sup>T fk×d</sup> to yield features that are uniformly 

spaced in subdivisions of the beat (using AlignÐsee Section 5.2) rather than in time. For an audio recording with B beats, we sample features X<sup>˜</sup> ∈ R<sup>4B×d</sup> at sixteenth-note intervals. The value X<sup>˜</sup> i is constructed by averaging all feature vectors in X that are nearest to the i’th sixteenth note into a single vector which acts as a proxy feature. For example, if a recording has a tempo of 120 BPM, a sixteenth note represents 125 ms of time, which would entail averaging across 43 feature vectors from Jukebox (fk ≈ 345 Hz). The intuition is that, while our alignments may not be precise enough to identify which of those 43 frames contains an onset, we can be reasonably confident that it occurs somewhere within them, and thus the relevant frame will be incorporated into the proxy. A similar approach was previously explored for song structure analysis in [47]. 

## 5.4 Modeling 

Together with the beat-wise resampling X<sup>˜</sup> ∈ R<sup>4B×d</sup> , we convert the sparse task labels y ∈ (R<sup>+</sup> × V)<sup>N</sup> into a dense sequence y˜ ∈{{∅} ∪ V}<sup>4B</sup> , which indicates whether or not an onset occurs at each sixteenth note.<sup>6</sup> Formally, 



<!-- Start of picture text -->
nj if Align ( 4 i )  = tj for some note yj,<br>y˜i =<br>∅ otherwise.<br><!-- End of picture text -->

We formulate melody transcription as an aligned sequenceto-sequence modeling problem and attempt to predict the sequence y˜ given X<sup>˜</sup> . Specifically, we train models of the form fθ : R<sup>4B×d</sup> → R<sup>4B×(|V|+1)</sup> , which parameterize probability distributions pθ(˜yi|X<sup>˜</sup> ) = SoftMax(fθ( X<sup>˜</sup> )i) over elements of the sequence y˜. One unique aspect of our dataset is that absolute octave information is absent (see Section 4). Hence, we construct an octave-tolerant cross-entropy loss by identifying the octave shift amount that minimizes the standard cross-entropy loss (denoted CE) when applied to the labels: 



<!-- Start of picture text -->
4B−1<br>min CE(pθ(˜yi|X ˜ ), OctaveShift(˜yi, σ)).<br>σ∈Z<br>∑ i=0<br><!-- End of picture text -->

We require a thresholding scheme to convert the dense sequence of soft probability estimates pθ(˜yi|X<sup>˜</sup> ) into a sparse sequence of notes required by our task (see Section 3). Given a threshold τ ∈ R (in practice, tuned on validation data), we define a sorted onset list 



<!-- Start of picture text -->
I = Sort({i ∈{0, . . . , 4B − 1} : pθ(˜yi = ∅|X ˜ ) < τ }).<br><!-- End of picture text -->

This should be interpreted as a list of N metrical positions where an onset likely occurs. The timings of these onsets are given by the alignment, and we will predict the notevalue with the highest probability. The sparse melody transcription is thus defined for j = 1, . . . , N by 



<!-- Start of picture text -->
Transcribe( X ˜ )j = (tj, nj), where<br>I j<br>tj = Align ,<br>4<br>(-)<br>nj = arg max pθ(˜yIj = v|X ˜ ).<br>v∈V<br><!-- End of picture text -->

> 6 This requires quantizing labels to the nearest sixteenth note. In practice, less than 1% of notes in our dataset are affected by this quantization. 

488 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

|Features|d|F1|
|---|---|---|
|Mel|229|0.514|
|MT3|512|0.550|
|Jukebox|4800|0.615|
|Mel, MT3|741|0.548|
|Mel, Jukebox|5029|0.617|
|MT3, Jukebox|5312|0.622|
|Mel, MT3, Jukebox|5541|0.623|



Table 1. HookTheory test set performance for Transformers trained with different features (top) and combinations (bottom). Features are complementaryÐcombining all three yields highest performanceÐbut marginally so compared to Jukebox alone. 

## 6. EXPERIMENTS 

Here we describe our experimental protocol for training melody transcription models on the HookTheory dataset. The purpose of these experiments is two-fold. First, we compare representations from different pre-trained models to handcrafted spectrogram features to determine if pretraining is helpful for the task of melody transcription (Section 6.1). Second, we compare our trained models holistically to other melody transcription baselines (Section 6.2). 

All transcription models are encoder-only Transformers with the default hyperparameters from [14], except that we reduce the number of layers from 6 to 4 to allow models to be trained on GPUs with 12GB of memory. During training, we select random slices from the annotated segments of up to 96 beats or 24 seconds in length (whichever is shorter). We train using our proposed loss function from Section 5.4 and perform early stopping based on max F1 score across thresholds τ on the validation set, using the best validation τ for testing. All models converge within 15k steps or about a day on a single K40 GPU. 

## 6.1 Comparing input features 

We compare representations from Jukebox [1] and MT3 [35] (see Section 5.1) to handcrafted spectrogram features, which are commonly used by existing transcription methods. Specifically, we compare to log-amplitude Mel spectrograms using the formulation from [16] (fk ≈ 31, d = 229). Because features may contain complementary information, we also experiment with all combinations of these three features. Note that our beat-wise resampling strategy allows for trivial combination of these features (by concatenation) despite their differing rates. In Table 1, we report F1 (as described in Section 3.1) on the HookTheory test set for all input features. 

Overall, using representations from Jukebox as input features results in stronger melody transcription performance than using either representations from MT3 or conventional handcrafted features. Representations from both MT3 and Jukebox outperform conventional handcrafted features, implying that both pre-training strategies are helpful for melody transcription. Note that these two pre-training approaches are compared holisticallyÐthese 

|Approach|F1(All)|F1(Vocal)|
|---|---|---|
|MT3 Zero-shot [35]|0.133|0.085|
|Melodia [48] + Segmentation|0.201|0.268|
|Spleeter [31] + Tony [28]|0.341|0.462|
|DSP + HMM [24]|0.420|0.381|
|Mel + Transformer|0.631|0.621|
|MT3 + Transformer|0.701|0.659|
|Jukebox + Transformer|0.744|0.786|



Table 2. Performance of different approaches on a subset of RWC-MDB [38±40]. The bottom three approaches were trained on the HookTheory dataset. For fair comparison to vocal transcription baselines, we also separately report performance on the vocal portions of this dataset. 

models differ on several axes (number of parameters, pretraining data semantics, pre-training task), and thus it is impossible to disentangle the individual contributions of these different factors without retraining the models. 

Qualitatively speaking, there is a noticeable difference in performance across the three different input features which correlates with quantitative performance (see footnote 1 for sound examples). Using representations from Jukebox tends to result in fewer wrong notes than the other features, and substantially reduces the number of egregiously wrong notes (e.g., notes outside of the key signature). Representations from Jukebox also appear to aid in the detection of more nuanced rhythmic patterns. Moreover, using handcrafted features will often result in several repeated onsets during a longer sustained melody noteÐ in contrast, using representations from Jukebox appears to mitigate this failure mode. 

Different features also appear to complement one another to a degree. The strongest performance overall is obtained by combining all three features, though the improvement over Jukebox alone is marginal. The practical downsides of combining all features outweigh the marginal benefitsÐrunning both pre-trained models effectively doubles the overall runtime, and the models have incompatible software dependencies. Hence, in the remainder of this paper we focus on models trained on individual features. 

## 6.2 Comparison to melody transcription baselines 

We compare overall performance of our proposed melody transcription approach to several baselines. We evaluate all methods on a small subset of 10 songs from RWC-MDB [38±40], another dataset which includes melody transcription labels. We chose this specific subset in an effort to compare to early DSP-based work on melody transcriptionÐnone of the early approaches [22± 25] shared code, however [24] shared melody transcriptions for this 10-song subset. 

In addition to [24], we also compare to a baseline which applies a note segmentation heuristic [19] to a melody extraction algorithm [48]. We additionally compare to MT3 in a zero-shot fashionÐthis model was not trained on melody transcription but was trained on some tasks which incorporate vocal transcription. Finally, because the vo- 

489 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
Jukebox Melody transcriber<br>(Dhariwal et al. 20) (This work)<br>Key estimator<br>(Krumhansl 90)<br>Beat detector Chord recognizer<br>Any song (Böck et al. 16) (This work) Lead sheet<br><!-- End of picture text -->

Figure 3. Inference procedure for Sheet Sage, our proposed system which transcribes any Western music audio into lead sheets (scores which depict melody as notes and harmony as chord names). The green, blue, and yellow boxes respectively take audio, features, and symbolic music data as input. Green boxes are modules that we built as part of this workÐboth are Transformers [14] trained on their respective tasks using audio features from Jukebox [1] and data from HookTheory [49]. 

cals often carry the melody in popular music, we compare to a baseline of running the Tony [28] monophonic transcription software on source-separated vocals isolated with Spleeter [31]. Because this approach will only work for vocals, we also separately report performance on a subset of our evaluation set where the vocals represent the melody. Scores for all methods and baselines appear in Table 2. 

Overall, our approach to training Transformers with features from Jukebox significantly outperforms the strongest baseline in both the vocals-only and unrestricted settings (p < 0.01 using a two-sided t-test for paired samples). Qualitatively speaking, the stronger baselines produce transcriptions where a reasonable proportion of the notes are the correct pitches, but they have poor rhythmic consistency with respect to the ground truth. In contrast, our best model produces the correct pitches more often and with a higher degree of rhythmic consistency. 

signature. We estimate the former using the KrumhanslSchmuckler algorithm [51, 52], which takes the symbolic melody and chord information as input. For the latter, we use madmom [12,13]. Finally, we engrave a lead sheet using Lilypond [53]. See Figure 3 for a full schematic. 

Subjectively speaking, Sheet Sage often produces highquality lead sheets, especially for the chorus and verse segments of pop music which have more prominent melodies. Performance is fairly robust across styles and instruments, even those which are less represented in the training dataÐ one user reported particularly strong success on Bollywood music. However, the system occasionally struggles, especially with quieter vocals, layered harmonies, unusual time signatures, or poor intonation. Sheet Sage is also limited to fixed time and key signatures due to limitations of its downbeat detection and key estimation modules. 

## 8. CONCLUSION 

## 7. SHEET SAGE 

As a bonus demo, here we describe Sheet Sage, a system we built to automatically convert music audio into lead sheets (see footnote on first page for examples), powered by our Jukebox-based melody transcription model. In Western music, a piece can often be characterized by its melody and harmony. When engraved as a lead sheetÐa musical score containing the melody as notes on a staff and the harmony as chord namesÐmelody and harmony can be readily interpreted by musicians, enabling recognizable performances of existing pieces. Hence, for some music, a lead sheet represents the essence of its underlying composition. Existing services like Chordify [50] can already detect a subset of the information needed to produce lead sheets (specifically, chords, beats, and keys) for broad music audio. However, despite past research efforts [24, 25], no user-facing service yet exists which can convert broad music audio into lead sheets, presumably due to the poor performance of existing melody transcription systems. 

To build Sheet Sage, we also train a Jukebox-based chord recognition model on the HookTheory data, using the same methodology that we propose for melody transcription (we simply replace the target vocabulary of onset pitches with one containing chord labels). Passing audio through our Jukebox-based melody transcription and chord recognition models results in a score like format containing raw note names and chord labels per sixteenth note. Engraving this information as a lead sheet requires additional information: the key signature and the time 

We present a new method and dataset which together improve melody transcription on broad music audio. Our method benefits from the rich representations learned by generative models pre-trained on broad audio. This suggests that further improvement in melody transcription may be possible without additional data, i.e., by scaling up or otherwise improving the pre-training procedure. By open sourcing our models and dataset, we hope to spark renewed interest for melody transcription in the MIR community, which may in turn reduce the gap between human perception and machine recognition of a fundamental aspect of music. 

## 9. ETHICAL CONSIDERATIONS 

Our definition of melody transcription incorporates equal temperament, a Western-centric tuning system. This could lead to disparate treatment of non equal-tempered music, e.g., if a streaming service were to use melody transcriptions for recommendation. We therefore advocate for the deployment of transcription only in contexts where users are self-selecting music to listen or play along to. Transcription may also be used to create training data for generationÐas with any work on generation, there are risks of plagiarism and labor displacement. We recommend that any work on generation involve careful auditing and mitigation of plagiarism. Due to the incomplete nature of a melody, we argue that melody generation tools are more likely to be incorporated into co-creation workflows (see [54]) rather than used to displace musicians. 

490 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

## 10. ACKNOWLEDGEMENTS 

Thanks to Annie Hui-Hsin Hsieh, John Hewitt, Maggie Henderson, Megha Srivastava, Nelson Liu, Pang Wei Koh, Rodrigo Castellon, Sam Ainsworth, and Zachary C. Lipton for helpful discussions, support, and advice. We thank all reviewers for their helpful comments. 

- [12] S. Böck, F. Krebs, and G. Widmer, ªJoint beat and downbeat tracking with recurrent neural networks,º in ISMIR, 2016. 

- [13] S. Böck, F. Korzeniowski, J. Schlüter, F. Krebs, and G. Widmer, ªmadmom: A new python audio and music signal processing library,º in International Conference on Multimedia, 2016. 

## 11. REFERENCES 

- [1] P. Dhariwal, H. Jun, C. Payne, J. W. Kim, A. Radford, and I. Sutskever, ªJukebox: A generative model for music,º arXiv:2005.00341, 2020. 

- [2] M. Ryynänen, T. Virtanen, J. Paulus, and A. Klapuri, ªAccompaniment separation and karaoke application based on automatic melody transcription,º in IEEE International Conference on Multimedia and Expo, 2008. 

- [3] K. Droe, ªMusic preference and music education: A review of literature,º Applications of Research in Music Education, 2006. 

- [4] D. Bainbridge, C. G. Nevill-Manning, I. H. Witten, L. A. Smith, and R. J. McNab, ªTowards a digital library of popular music,º in ACM Conference on Digital Libraries, 1999. 

- [5] A. Ghias, J. Logan, D. Chamberlin, and B. C. Smith, ªQuery by humming: Musical information retrieval in an audio database,º in ACM International Conference on Multimedia, 1995. 

- [6] S. Ewert, B. Pardo, M. Muller, and M. D. Plumbley, ªScore-informed source separation for musical audio recordings: An overview,º IEEE Signal Processing Magazine, 2014. 

- [7] C. Hawthorne, A. Stasyuk, A. Roberts, I. Simon, C.Z. A. Huang, S. Dieleman, E. Elsen, J. Engel, and D. Eck, ªEnabling factorized piano music modeling and generation with the MAESTRO dataset,º in ICLR, 2019. 

- [8] M. Goto and S. Hayamizu, ªA real-time music scene description system: Detecting melody and bass lines in audio signals,º in International Joint Conference on Artificial Intelligence Workshop on Computational Auditory Scene Analysis, 1999. 

- [9] M. Goto, ªA real-time music-scene-description system: Predominant-F0 estimation for detecting melody and bass lines in real-world audio signals,º Speech Communication, 2004. 

- [10] J. Salamon, E. Gómez, D. P. Ellis, and G. Richard, ªMelody extraction from polyphonic music signals: Approaches, applications, and challenges,º IEEE Signal Processing Magazine, 2014. 

- [11] K. S. Rao, P. P. Das et al., ªMelody extraction from polyphonic music by deep learning approaches: A review,º arXiv:2202.01078, 2022. 

- [14] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, è. Kaiser, and I. Polosukhin, ªAttention is all you need,º in NeurIPS, 2017. 

- [15] S. Sigtia, E. Benetos, and S. Dixon, ªAn end-to-end neural network for polyphonic piano music transcription,º IEEE Transactions on Audio, Speech, and Language Processing, 2016. 

- [16] C. Hawthorne, E. Elsen, J. Song, A. Roberts, I. Simon, C. Raffel, J. Engel, S. Oore, and D. Eck, ªOnsets and frames: Dual-objective piano transcription,º in ISMIR, 2018. 

- [17] R. Castellon, C. Donahue, and P. Liang, ªCodified audio language modeling learns useful representations for music information retrieval,º in ISMIR, 2021. 

- [18] J. S. Downie, X. Hu, J. H. Lee, K. Choi, S. J. Cunningham, and Y. Hao, ªTen years of MIREX: reflections, challenges and opportunities,º in ISMIR, 2014. 

- [19] J. Salamon, ªaudio_to_midi_melodia,º https: //github.com/justinsalamon/audio_to_midi_melodia, 2015. 

- [20] R. Nishikimi, E. Nakamura, K. Itoyama, and K. Yoshii, ªMusical note estimation for F0 trajectories of singing voices based on a Bayesian semi-beat-synchronous HMM,º in ISMIR, 2016. 

- [21] R. Nishikimi, E. Nakamura, M. Goto, K. Itoyama, and K. Yoshii, ªScale-and rhythm-aware musical note estimation for vocal F0 trajectories based on a semi-tatumsynchronous hierarchical hidden semi-markov model,º in ISMIR, 2017. 

- [22] R. P. Paiva, T. Mendes, and A. Cardoso, ªAn auditory model based approach for melody detection in polyphonic musical recordings,º in International Symposium on Computer Music Modeling and Retrieval, 2004. 

- [23] R. P. Paiva, T. Mendes, and A. Cardoso, ªOn the detection of melody notes in polyphonic audio,º in ISMIR, 2005. 

- [24] M. P. Ryynänen and A. P. Klapuri, ªAutomatic transcription of melody, bass line, and chords in polyphonic music,º Computer Music Journal, 2008. 

- [25] J. Weil, T. Sikora, J.-L. Durrieu, and G. Richard, ªAutomatic generation of lead sheets from polyphonic music signals,º in ISMIR, 2009. 

491 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

- [26] A. Laaksonen, ªAutomatic melody transcription based on chord transcription,º in ISMIR, 2014. 

- [27] E. Molina, L. J. Tardón, A. M. Barbancho, and I. Barbancho, ªSiPTH: Singing transcription based on hysteresis defined on the pitch-time curve,º IEEE Transactions on Audio, Speech, and Language Processing, 2014. 

- [28] M. Mauch, C. Cannam, R. Bittner, G. Fazekas, J. Salamon, J. Dai, J. Bello, and S. Dixon, ªComputer-aided melody note transcription using the Tony software: Accuracy and efficiency,º in International Conference on Technologies for Music Notation and Representation, 2015. 

- [29] R. Nishikimi, E. Nakamura, M. Goto, K. Itoyama, and K. Yoshii, ªBayesian singing transcription based on a hierarchical generative model of keys, musical notes, and F0 trajectories,º IEEE Transactions on Audio, Speech, and Language Processing, 2020. 

- [30] R. Nishikimi, E. Nakamura, M. Goto, and K. Yoshii, ªAudio-to-score singing transcription based on a CRNN-HSMM hybrid model,º APSIPA Transactions on Signal and Information Processing, 2021. 

- [31] R. Hennequin, A. Khlif, F. Voituret, and M. Moussallam, ªSpleeter: a fast and efficient music source separation tool with pre-trained models,º Journal of Open Source Software, 2020. 

- [32] E. Benetos, S. Dixon, D. Giannoulis, H. Kirchhoff, and A. Klapuri, ªAutomatic music transcription: challenges and future directions,º Journal of Intelligent Information Systems, 2013. 

- [33] J. Thickstun, Z. Harchaoui, and S. Kakade, ªLearning features of music from scratch,º in ICLR, 2017. 

- [34] E. Manilow, G. Wichern, P. Seetharaman, and J. Le Roux, ªCutting music source separation some Slakh: A dataset to study the impact of training data quality and quantity,º in IEEE Workshop on Applications of Signal Processing to Audio and Acoustics, 2019. 

- [35] J. Gardner, I. Simon, E. Manilow, C. Hawthorne, and J. Engel, ªMT3: Multi-task multitrack music transcription,º in ICLR, 2022. 

- [36] A. Ycart, L. Liu, E. Benetos, and M. Pearce, ªInvestigating the perceptual validity of evaluation metrics for automatic piano music transcription,º TISMIR, 2020. 

- [37] C. Raffel, B. McFee, E. Humphrey, J. Salamon, O. Nieto, D. Liang, and D. Ellis, ªmir_eval: A transparent implementation of common MIR metrics,º in ISMIR, 2014. 

- [38] M. Goto, H. Hashiguchi, T. Nishimura, and R. Oka, ªRWC Music Database: Popular, classical and jazz music databases,º in ISMIR, 2002. 

- [39] M. Goto, H. Hashiguchi, T. Nishimura, and R. Oka, ªRWC Music Database: Music genre database and musical instrument sound database,º in ISMIR, 2003. 

- [40] M. Goto, ªDevelopment of the RWC Music Database,º in International Congress on Acoustics, 2004. 

- [41] Y.-W. Chen, H.-S. Lee, Y.-H. Chen, and H.-M. Wang, ªSurpriseNet: Melody harmonization conditioning on user-controlled surprise contours,º in ISMIR, 2021. 

- [42] Y.-C. Yeh, W.-Y. Hsiao, S. Fukayama, T. Kitahara, B. Genchel, H.-M. Liu, H.-W. Dong, Y. Chen, T. Leong, and Y.-H. Yang, ªAutomatic melody harmonization with triad chords: A comparative study,º Journal of New Music Research, 2021. 

- [43] J. Jiang, G. G. Xia, and D. B. Carlton, ªMIREX 2019 submission: Crowd annotation for audio key estimation,º MIREX, 2019. 

- [44] J. Jiang, G. G. Xia, D. B. Carlton, C. N. Anderson, and R. H. Miyakawa, ªTransformerVAE: A hierarchical model for structure-aware and interpretable music representation learning,º in ICASSP, 2020. 

- [45] C. Hawthorne, I. Simon, R. Swavely, E. Manilow, and J. Engel, ªSequence-to-sequence piano transcription with transformers,º in ISMIR, 2021. 

- [46] A. Graves, S. Fernández, F. Gomez, and J. Schmidhuber, ªConnectionist temporal classification: labelling unsegmented sequence data with recurrent neural networks,º in ICML, 2006. 

- [47] B. McFee and D. Ellis, ªAnalyzing song structure with spectral clustering,º in ISMIR, 2014. 

- [48] J. Salamon and E. Gómez, ªMelody extraction from polyphonic music signals using pitch contour characteristics,º IEEE Transactions on Audio, Speech, and Language Processing, 2012. 

- [49] C. Anderson, D. Carlton, R. Miyakawa, and D. Schwachhofer, ªHooktheory TheoryTab DB,º https: //www.hooktheory.com/theorytab. 

- [50] B. de Haas, J. P. Magalhaes, D. Ten Heggeler, G. Bekenkamp, and T. Ruizendaal, ªChordify: Chord transcription for the masses,º in ISMIR Late-Breaking Demos, 2014. 

- [51] C. L. Krumhansl, Cognitive foundations of musical pitch. Oxford University Press, 1990. 

- [52] D. Temperley, ªWhat’s key for key? The KrumhanslSchmuckler key-finding algorithm reconsidered,º Music Perception, 1999. 

- [53] H.-W. Nienhuys and J. Nieuwenhuizen, ªLilyPond, a system for automated music engraving,º in Colloquium on Musical Informatics, 2003. 

- [54] C.-Z. A. Huang, H. V. Koops, E. Newton-Rex, M. Dinculescu, and C. J. Cai, ªAI Song Contest: Human-AI co-creation in songwriting,º in ISMIR, 2020. 

492 

