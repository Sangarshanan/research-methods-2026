---
paper_id: "000076"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706552/files/000076.pdf"
---

# GOAT: A LARGE DATASET OF PAIRED GUITAR AUDIO RECORDINGS AND TABLATURES 

Jackson Loth<sup>1</sup> , Pedro Sarmento<sup>1,2</sup> , Saurjya Sarkar<sup>1</sup> , Zixun Guo<sup>1</sup> , Mathieu Barthet<sup>1,3</sup> , and Mark Sandler<sup>1</sup> 

1Centre for Digital Music, Queen Mary University of London 

2Music.AI 

3Aix-Marseille Univ CNRS PRISM 

```
{j.j.loth,p.p.sarmento,saurjya.sarkar,zixun.guo,m.barthet,mark.sandler}@qmul.ac.uk
```

## ABSTRACT 

In recent years, the guitar has received increased attention from the music information retrieval (MIR) community driven by the challenges posed by its diverse playing techniques and sonic characteristics. Mainly fueled by deep learning approaches, progress has been limited by the scarcity and limited annotations of datasets. To address this, we present the Guitar On Audio and Tablatures (GOAT) dataset, comprising 5.9 hours of unique high-quality direct input audio recordings of electric guitars from a variety of different guitars and players. We also present an effective data augmentation strategy using guitar amplifiers which delivers near-unlimited tonal variety, of which we provide a starting 29.5 hours of audio. Each recording is annotated using guitar tablatures, a guitar-specific symbolic format supporting string and fret numbers, as well as numerous playing techniques. For this we utilise both the Guitar Pro format, a software for tablature playback and editing, and a text-like token encoding. Furthermore, we present competitive results using GOAT for MIDI transcription and preliminary results for a novel approach to automatic guitar tablature transcription. We hope that GOAT opens up the possibilities to train novel models on a wide variety of guitar-related MIR tasks, from synthesis to transcription to playing technique detection. 

## 1. INTRODUCTION 

The guitar is one of the most popular instruments in modern western music. It is no surprise that guitar-centered research has received a lot of attention, particularly in the wake of advances in deep learning. Tasks such as automatic guitar transcription (AGT) [1] [2] [3] [4], tablature generation [5] [6], guitar amplifier modeling [7] [8] [9], and more have seen great progress. Despite this interest in guitars, there remains limited data availability for guitar 

© J. Loth, P. Sarmento, S. Sarkar, Z. Guo, M. Barthet, and M. Sandler. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: J. Loth, P. Sarmento, S. Sarkar, Z. Guo, M. Barthet, and M. Sandler, “GOAT: A Large Dataset of Paired Guitar Audio Recordings and Tablatures”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

audio, particularly in the case of annotated audio recordings. 

Musical Instrument Digital Interface (MIDI) is a well known standard of representing music, and is a common choice when annotating the guitar [10] [4]. MIDI easily encodes essential parameters of musical notes such as pitch, note onset, duration and velocity. However, it does not give any indication of string or fret number, nor does it have any standardized way of representing the numerous expressive components of guitar playing [11]. It is based on a descriptive type of notation, in which there is a relationship between symbols and pitch. Tablatures, however, are a prescriptive type of notation commonly used for guitar, in which there is a relation between symbols and actions, i.e. how to play said symbols [12]. While there are some guitar-focused datasets in the literature that offer tablature-like annotations [13] [14] [15] [16], they are typically limited to fret and string values, ignoring expressive techniques (e.g. bends, palm mutes, legatos). 

As a motivation behind the creation of GOAT, the Guitar On Audio and Tablatures dataset, we seek to surpass the limitations of MIDI and instead prioritize building a dataset of guitar recordings annotated using guitar tablatures, a popular musical format among guitarists. For this we rely on Guitar Pro, a commercial software for tablature edition and playback widely spread amongst the guitar community. This dataset consists of 5.9 hours of unique real audio recordings of guitars, fully annotated for fret/string numbers and expressive playing techniques. We also include the entire dataset rendered through a wide variety of different digital guitar amplifiers in various configurations and cabinet impulse responses, for a total of 29.5 hours of fully annotated audio. The annotations are provided in Guitar Pro format, as well as DadaGP [12] tokens, a compressed text-like representation of the information in the tablatures. In an attempt to make a bridge with prior literature, we also include MIDI versions of the content. 

This paper’s contributions include (1) an overview of the GOAT dataset and the data collection methodology; (2) a data augmentation strategy for obtaining a large amount of timbral variation; (3) an evaluation of results when using the GOAT dataset for the task of AGT, complemented with (4) preliminary results on a novel audio-to-text-based approach for AGT; finally, some (5) suggestions for prospec- 

655 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

tive applications using the GOAT dataset. We first cover some relevant background concerning guitar tablatures and similiar previously released music datasets. In Section 3, we extensively describe the methodology used to compile the GOAT dataset. We then describe, in Section 4, the details of the GOAT dataset, the features it encompasses and the ones it lacks. Within Section 5 we present results from a use case for GOAT in the context of AGT, following both a traditional MIDI-based approach for comparison with previous results, and a novel procedure using the text-like token representations of GOAT to fine-tune a Whisper [17] model. Finally, Section 6 proposes additional applications for the dataset. 

## 2. BACKGROUND 

## 2.1 Guitar Tablatures 

Guitar tablatures (see Figure 1), also called tabs, are symbolic representations of guitar music. 



<!-- Start of picture text -->
full full<br>PM<br>14 12 14 14 12-15 14 12<br>14~12-10<br>0<br><!-- End of picture text -->

Figure 1. Example of two measures of a guitar tablature, from the Guitar Pro editing software, exemplifying different guitar playing techniques (i.e. bends, palm mutes, legatos and slides). 

In contrast to MIDI, which simply represents a note pitch over time, tabs represent both the fret and string number of a guitar. Tablatures can also support expressive playing techniques such as bends, hammer-ons, pull-offs, strum directions and more. It is a very intuitive, visual representation of guitar music and is popular among guitarists for learning specific songs and performances. Guitar tabs have seen an increase in attention from researchers in the past few years in areas such as guitar tablature generation [12] [5] [6] [18] [19], automatic guitar transcription [1] [3], tablature prediction from MIDI [20] and acoustic guitar synthesis from tablatures [21]. 

As previously discussed, representing tablatures is difficult as there is no standardised representation like MIDI. Some works use a JSON-like representation to encode information [13] [22]. DadaGP [12] also introduced an easy to parse text-based encoding which uses a simple vocabulary to describe strings, fret, and many guitar-specific expressive techniques. 

## 2.2 Guitar-Focused Datasets 

To facilitate guitar focused research, a number of datasets has been compiled for various purposes, focusing mainly on the task of AGT, as observable in Table 1. Datasets such as GuitarSet [13], EGDB [10], GAPS [4] (which focuses 

|Dataset|Length(m)|MIDI|Tab|
|---|---|---|---|
|GAPS [4]|843|✓|✗|
|GOAT [Ours]|354|✓|✓|
|IDMT [22]|340|✗|✓|
|Guitar-TECHS [16]|312|✓|✓|
|GuitarSet [13]|180|✗|✓|
|FrançoisLeduc [2]|240|✓|✗|
|EGDB [10]|118|✓|✗|



Table 1. Guitar-focused datasets in the literature. We report real audio content duration (in minutes), and existence of annotations in MIDI and Tablature format. We consider tablature format to be any kind of annotation containing string and fret information. 

exclusively on classical guitar recordings), IDMT-SMTGuitar [22] FrançoisLeduc [2] and Guitar-TECHS [16] contain real guitar recordings with annotations of notes, typically in MIDI or tablature-like form. IDMT-SMTAudio-Effects [23] focuses on guitar recordings with various audio effects. SynthTab [14] contains an extremely large collection of audio renditions of guitar tracks synthesised using a virtual instrument. While still sounding somewhat realistic, we do not include SynthTab in Table 1 due to the synthetic nature of the audio. 

## 3. METHODOLOGY 

In order to have as much flexibility as possible with the dataset, it was decided early on that the dataset would have the following qualities: (1) direct input (DI) recordings to allow for post-processing towards tone variety; (2) 44.1 kHz sampling rate to account for high-quality audio; (3) annotations in the form of guitar tablatures to capture as much detail about the playing as possible. 

## 3.1 Data Collection 

The data was produced by both the main authors and two third party content creators. These creators delivered digital audio workstation (DAW) projects containing a preexisting cover of a popular song and corresponding tablatures, from which the audio and tab pairs were extracted. This allowed us to quickly obtain a large amount of data. Each song was manually checked and aligned against the tablature to ensure that every note was correct between audio and tablature. If multiple guitar parts were present in a tab, they were split off into separate files. In addition to this, we recorded over an hour of additional audio to complement the dataset. This was done by collecting community-created tablatures<sup>1</sup> and recording the parts in each song exactly as described in the tablature. 

## 3.2 Data Processing 

In order to protect the work made by the third party creators, all song and artist names were removed from the file 

> 1 https://www.songsterr.com/ 

656 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
1789 208 1078 757 664 416 250 578 202 386 417 432 571 261 261 174 145 220 20 65 5 31 20<br>4000<br>3500<br>B 3100 456 1031 1728 882 1530 786 1267 754 1155 982 956 779 709 472 508 109 305 83 73 50 9 3<br>3000<br>G 3452 499 2507 759 2309 1698 1542 1939 1630 2414 1484 915 1326 369 654 153 156 141 75 79 11 1<br>2500<br>StngD 4488 263 2922 1070 1562 1915 1964 2603 1220 2191 950 1631 611 668 523 97 53 67 11 28 2 7 2000O c u r ences<br>1500<br>A 3888 304 2546 2027 17582421 15592435 905 1521 544 937 278 117 244 62 38 20<br>1000<br>3646 1033 1162 1727 799 1294 417 825 528 657 184 207 236 66 26 70 11 8 8 -500<br>0<br>2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24<br>Fret Number<br><!-- End of picture text -->

Figure 2. Note distribution over the fretboard (i.e. string and fret positions) of the content in the GOAT dataset. 

names and tablatures. The tablatures were all converted to the DadaGP [12] text encoding format due to its popularity in tablature-related tasks. MIDI was also generated from the tablatures using the Guitar Pro MIDI export function. While the MIDI annotations do not encode the expressive techniques included in the tabs, they allow the dataset to be used along with other datasets and models which were built for MIDI annotations, leveraging contributions from the literature. Despite the actual notes played in the audio files having small timing imperfections, the notes in the tablature annotations are all quantized to a grid. The alignment procedure from [4] was used to fine-align the MIDI notes to the performances. Both the fine-aligned and quantized MIDI are provided in the dataset. The tabs were also rendered using the Guitar Pro Realistic Sound Engine (RSE)<sup>2</sup> . virtual instrument to create additional synthetic data. 

## 3.3 Amplifier Rendering 

The audio in GOAT is recorded from the raw output of an electric guitar pickup, also called direct input or DI. This is not a sound commonly heard in music, as the electric guitar sound most listeners are accustomed to comes from a DI run through a guitar amplifier and guitar speaker cabinet connected in series. We collected DIs in order to maximize the potential of data augmentation via reamping. Reamping is a process in which a DI is run through an amplifier and sometimes a full effects chain to transform it into a desired final sound. This is common in music production when an engineer wants to capture a performance but not commit to a final guitar tone. 

While it would be theoretically possible to reamp GOAT using a variety of real amplifiers and cabinets, this process is time consuming and expensive. Instead, we can use high quality digital amplifier models and impulse responses (IRs) of a guitar cabinet speaker to model the amplifier and speaker cabinet respectively. This approach was used by [10] and showed improvement in transcription with the increased tone variety, though the amplifier models used were of low quality and limited to just five total 

digital amplifiers. We extend this idea by using a higher quality modern amplifier modeling software, as well as significantly increasing the variety in amplifiers and cabinets used. Through this method, we are able to transform the audio in GOAT much closer to the sound of real world data, as well as significantly increase the timbral variety. 

For the amplifier, we used the Neural Amp Modeler<sup>3</sup> (NAM), a high quality digital amplifier plugin. The NAM allows users to capture a ‘profile’ of a guitar amplifier, essentially a snapshot of the amplifier’s sound. A large community<sup>4</sup> has grown out of users sharing their profiles online. Using publicly available NAM profiles, we curated a dataset of roughly 7,000 profiles from over 1,000 different amplifiers. A profile was chosen at random to render each audio item in the dataset. IRs were used from the NeuralDSP Archetype Nolly<sup>5</sup> plugin. This plugin has cabinet IRs from several different microphones, with parameters to control the microphone height and distance from the speaker. The microphone and its parameters were chosen at random for each audio item in the dataset. A send to a room reverb was also enabled at random (with a 25% chance of being enabled) and the send level was randomised between −10dB and 0dB. A python package called Pedalboard [24] was used to render the audio. This process was repeated 5 times over, resulting in 29.5 hours of fully annotated audio. This process can, however, be extended by choosing different post-processing approaches. The reamping code<sup>6</sup> is made publicly available. 

## 4. DATASET 

## 4.1 Statistical Overview 

The finalised dataset contains 5.17 hours of DI recordings in standard tuning<sup>7</sup> and 25.85 hours of amplifier recording, as well as an additional 43.85 minutes in non-standard tuning. This is broken into 153 (standard tuning) and 19 (non-standard tuning) individual dataset items. 

For each data point in the GOAT dataset we provide the following: (1) the DI audio file (in .wav format) and (2) 

> 3 https://www.neuralampmodeler.com/ 

> 4 https://tonehunt.org/ 

> 5 https://neuraldsp.com/plugins/archetype-nolly 

> 2 https://www.guitar-pro.com/blog/p/14545-signature-soundsexplained-guitar-pro-7 

> 6 https://github.com/JackJamesLoth/GOAT-Dataset 

> 7 Standard tuning uses the open string pitches E, A, D, G, B, e. 

657 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
(c) Note Durations<br>(a) Tempo (in BPM, for each song) 8000 (b) Time Signatures (for each measure) (960 ticks per quarter note) 7000 (d) Guitar Playing Techniques<br>18 7000 30000 6000<br>1416 6000 25000 5000<br>12 5000 20000 4000<br>10 4000<br>8 3000 15000 3000<br>6 10000 2000<br>2000<br>4 1000 5000 1000<br>0<br>50 100 150 4/4 6/8 6/4 3/4 5/4other 2880others legato palm mute slide bend<br><!-- End of picture text -->

Figure 3. Statistical information about the GOAT dataset. Histograms of tempo (in BPM) per song (a), time signatures per measure (b), most common note durations, in which a value of 960 ticks corresponds to a quarter note (c), and most frequent guitar playing techniques (d). 

the DI audio rendered through 5 different amplifiers and 5 different cabinets (in .wav format); (3) the corresponding Guitar Pro tablature (in .gp and .gp5 format, the latter to allow for conversion into the DadaGP format), the (4) corresponding DadaGP text encoding of the Guitar Pro annotation (in .txt format), and (5) a rendered version into audio using the RSE virtual instrument in Guitar Pro (in .wav format); finally, (6) the corresponding MIDI and fine-aligned MIDI annotations (in .mid format). A .csv file containing metadata and file paths is also provided. 

|Guitar|Standard(m)|Other(m)|
|---|---|---|
|Stratocaster|208.82|26.15|
|Les Paul|6.08|7.36|
|Jazzmaster|15.62|10.34|
|Strandberg|79.83|-|



Table 2. Breakdown of content of audio (in minutes) by type of guitar, using standard or alternative tunings (e.g. drop-D tunings, half-step or whole-step down-tunings). 

mostly “power chords”, common in the rock/metal sonorities, comprised of the root, and the fifth and octave above. 

Figure 3 shows histogram breakdowns of the musical content in the dataset. In (a) we observe a distribution of the tempos, in bpm, for each song in the GOAT dataset. In terms of time signatures, in (b) we see a prevalence of 4/4 time signatures in most of the measures of the songs in the dataset. The statistics presented in (c) and (d) leverage the token format of the DadaGP annotations. Inspecting the GOAT dataset via this text-like format, we can produce an histogram of the most common note durations (see (c), in which a quarter note corresponds to 960 ticks, 480 ticks correspond to an eighth note, 240 ticks to a sixteenth note, 320 to an eighth note triplet, 720 ticks to a dotted eighth note, and so on), and the most commonly used guitar playing techniques (d). Regarding the latter, we have highlighted the four most prevalent expressive techniques, but the dataset contains instances of others (e.g. tapping, vibrato), although with a much smaller representation. 

## 4.2 Distribution 

Table 2 reports the content (in terms of minutes) of audio, divided by type of guitar used in the recordings. Overall, it contains 172 distinct audio files, each with all the annotations and metadata described previously. 

In Figure 2 we observe a compilation of the note distribution for all the songs in GOAT, from a total of 109,869 total played notes, containing information about the frets and strings used for each. 

|Chord Type|Number of Instances|
|---|---|
|w/ 3 notes|7,174|
|w/ 4 notes|4,260|
|w/ 5 notes|1,065|
|w/ 6 notes|1,039|



Table 3. Breakdown of number of chords in the GOAT dataset in terms of number of notes. 

Statistics on the chords present in GOAT are shown in Table 3. From a total of 13,538 chords in the dataset, there is a prevalence of chords played using only 3 notes. This includes triads (major, minor, diminished, augmented), but 

We distribute the GOAT dataset on the Zenodo<sup>8</sup> platform. The dataset is made available by request to better control its use for research purposes only. 

## 4.3 What Is Missing? 

As of this version, there is no information regarding key signature as metadata in GOAT. Finally, akin to what the authors referred to in [12], Guitar Pro (up until its version 5) does not include note velocity information as in MIDI. However, Guitar Pro does represent loudness between notes and musical phrases by using traditional dynamic instructions (e.g. forte, piano). Thus, dynamics are excluded from both the Guitar Pro and MIDI renditions of the GOAT dataset, and they are exclusively contained in the realistic DI recordings. In terms of metadata, it would be interesting to provide a distribution of the type of chords in terms of harmonic quality (e.g. major, minor, seventh) as well as diagrams or fingerings, but that information is currently absent from what GOAT provides. 

> 8 https://zenodo.org/records/15690894 

658 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 5. EXPERIMENTS USING GOAT 

In order to showcase the applicability of GOAT, we selected automatic music transcription as a use case. We evaluate GOAT on two tasks, transcription into MIDI format, (here referred to as MIDI transcription), focusing only on capturing note’s pitch, duration and velocity information, and a newly proposed task of automatic guitar tablature transcription (AGTT) via DadaGP token prediction. 

## 5.1 MIDI Transcription 

While GOAT is not expressly a MIDI-focused dataset, MIDI transcription is still the most common baseline used in automatic guitar transcription (AGT) and is the method researchers will be most familiar with. Despite the previously discussed shortcomings of MIDI, it is still beneficial to evaluate GOAT using the task of MIDI transcription in order to better understand how the dataset compares to other similar datasets. 

Following [4] [2], we finetune a high-resolution transcription model [25] pretrained using extensively augmented data [26]. Rather than training from scratch, we finetune a pretrained model, as [2, 4] have demonstrated that finetuning yields superior performance. We use the same training setup as [4] where each training data is segmented into 10-second chunks with a hop size of 1 second. During training, we apply data augmentation by randomly shifting the pitch up to ±2 semitones. 

We train three separate models using GOAT for our experiments. The models were trained on an NVIDIA A5000 GPU until convergence. The first uses only the raw DI recordings (DI). The next uses the dataset reamped once using our methodolgy discussed in Section 3.3 (AMP). Finally, we train a model using the dataset reamped twice (AMP-XL). While this does not mean that the model would see more variety in MIDI annotation during training, it does mean that the model will see more timbral variety during training. These models are then evaluated on the test split of GOAT (both DI and AMP) and GuitarSet [13] (which contains only acoustic guitar). We choose to evaluate our model on GuitarSet to assess its zero-shot learning capabilities. This is done in order to test the following hypotheses: H1 - data augmentation in the form of guitar amplifier reamping improves the generalizability of a transcription model on real data; H2 - reamping the dataset multiple times to give additional timbral variety further improves the generalizability of a transcription model on real data. The MIDI transcription results are found in Table 4. 

## 5.1.1 Discussion 

All three models in general achieve fairly competitive results on the test datasets [2]. The AMP model is able to obtain comparable results to the DI model on the DI and GuitarSet test split, while significantly outperforming the DI model on the AMP test split, the latter being the closest to a real world transcription scenario concerning electric guitar. This is strong evidence for H 1, suggesting that the amplifier data augmentation allows the model to generalize to different amplifier timbres without sacrificing quality in 

|Data|Test Split|P|R|F|
|---|---|---|---|---|
||DI|0.847|0.798|0.820|
|DI|AMP|0.771|0.677|0.714|
||GuitarSet|0.879|0.849|0.860|
||DI|0.853|0.836|0.843|
|AMP|AMP|0.824|0.781|0.800|
||GuitarSet|0.882|0.815|0.843|
||DI|0.831|0.809|0.818|
|AMP-XL|AMP|0.821|0.796|0.806|
||GuitarSet|0.872|0.808|0.835|



Table 4. MIDI transcription results. Metrics used are notelevel precision (P ), recall (R) and F1 score (F ). 

the case of DI or acoustic guitar. This improvement also surpasses the gains observed between models trained with DI and amplifier data in [10], further validating the effectiveness of our data augmentation strategy. Notably, our model trained solely on DI data achieves comparable transcription performance on GuitarSet’s test set [2], further validating GOAT’s effectiveness in training AGT systems. 

Interestingly, the AMP-XL model performs worse than both the DI and AMP models on the DI and GuitarSet test splits, while performing slightly better than AMP on the AMP test split. This seems to suggest that the additional timbre variety is only helping generalisation among amplifier timbres, while hurting generalisation among the unseen DI and acoustic guitar timbres. However, we posit that this still shows some evidence for H 2 given that the AMP test split is the closest to a real world electric guitar transcription use case. 

## 5.2 Tablature Transcription with Whisper 

Given our choice of Guitar Pro as the annotation format in GOAT, an obvious choice of task to evaluate the dataset is AGTT. While this task has seen some previous work [1] [3], it is still conducted in a manner similar to MIDI transcription by predicting string and fret activations at small time scales. We formulate the problem differently and propose a new task by instead using the DadaGP annotations as plain text and treating the problem as an audio-to-text problem. This approach means that we are not predicting exact note timings, but rather the more general sheet music-like interpretation of the input audio. 

For this task, we fine-tune Whisper [17], a large foundation model trained for automatic speech recognition. The audio in GOAT was split into 15 second chunks, as Whisper has a maximum audio input length of 30 seconds. Whisper also has a maximum sequence length of 448, so any chunks whose annotations exceeded 448 tokens were excluded. This meant we were only able to use roughly 4.65 hours of GOAT. A custom tokenizer was also created so that the model could correctly interpret and predict DadaGP tokens. The vocabulary used in DadaGP was simplified, removing tokens relating to artist and genre and 

659 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

|Data|Loss|Accuracy|WER|
|---|---|---|---|
|DI|1.787|0.682|0.515|
|AMP|2.065|0.681|0.547|
|AMP-XL|2.285|0.692|0.518|



Table 5. Evaluation results on the test split of GOAT from the best runs of the fine-tuned Whipser model. 

simplifying note tokens by removing timbre information. 

In our experiments, we again train three different models using the same data setup as in Section 5.1. The models were trained on an NVIDIA A100 GPU until convergence. We use token accuracy and word error rate (WER) to evaluate the performance. Preliminary results from the best performing epochs are presented in Table 5. 

## 6.1 Automatic Guitar Transcription 

Containing both MIDI and tablature annotations of the source audio, GOAT lends itself to AGT very well. Section 5 details preliminary results for MIDI-based transcription and a newly proposed task of DadaGP token prediction for tablature transcription. We leave improvement on these baselines as future work. 

## 6.2 Realistic Guitar Synthesis 

GOAT provides numerous examples of different notes and playing techniques, with annotations for all of them. The data can be used to help train or fine-tune popular models such as RAVE [27] and DDSP [28]. It is also suitable for MIDI synthesis models such as [29] or even novel tasks such as synthesis from guitar tablatures. 

## 5.2.1 Discussion 

The transcription results ultimately did not work well, though they do show some promise. DadaGP is a highly structured text encoding, and the biggest initial hurdle is learning this structure. For example, in a DadaGP encoding, notes are specified through one or more `note` tokens, followed by a `wait` token. Given the abundance of `wait` tokens in DadaGP encodings, it is possible for the model to simply learn to output only these tokens to optimise the loss function. While example outputs of the fine-tuned models to show this behavior in parts of the prediction, the first half of the token predictions still tend to be semistructured DadaGP encodings. Common note groups (e.g simple chords) are predicted. However, these ultimately did not correlate with the notes in the ground-truth encodings. While the accuracy appears to be somwhat high, this is likely misleading due to the prelevance of `wait` tokens in both the dataset and model outputs. 

It seems likely that more fine-tuning and data is needed to get a workable transcription model. Training using the AMP-XL data resulted in a small improvement to the accuracy and WER, suggesting that additional data could be beneficial. A pretraining step using synthetic data, such as SynthTab [14] for example, could be a feasible way to collect enough data to get the model to properly learn the DadaGP structure. This could then be followed by a further fine-tuning step on GOAT to expose the model to a wide range of timbres and real guitar playing. However, we leave these improvements for future work. We include these limited results in order to show the potential of this approach and showcase the benefit of a dataset like GOAT, which is unique in being the only non-synthetic dataset of paired guitar audio and tablatures. 

## 6. PROSPECTIVE USE CASES 

We envision GOAT as a general purpose dataset that can be useful for a number of different tasks. While we propse these tasks as the starting point of work with this dataset, we hope that the dataset finds uses in other unique and interesting tasks as well. 

## 6.3 Automatic Guitar Playing Technique Identification 

Automatic guitar playing technique identification is another task that we believe can benefit from the availability of GOAT. For example, the authors in [30], propose ways of modelling bends in guitar tablatures. Moreover, while datasets exist for this type of work [31], GOAT has significantly more audio and contains both playing technique and note annotations. We hypothesise that this could potentially be combined with AGTT, further improving the capabilities of guitar transcription models. 

## 6.4 Effect/Distortion Removal 

The clean DI audio and amplifier pairs provide numerous examples for effect/distortion removal techniques [32] [33]. The data augmentation techniques can also be extended to other common effects (e.g phaser, chorus). 

## 7. CONCLUSION 

We present GOAT, a vast dataset containing pairs of real guitar audio and guitar tablature annotations. This dataset is unique among guitar-focused datasets in that it uses digital representations of tablatures as the annotation for real audio, an annotation format which is well suited to capture guitar-specific metadata. A data augmentation strategy which offers a large amount of tonal variety is presented. We validate the use of the dataset and the augmentation strategy through a standard literature-based MIDI transcription experiment. The results show competitive performance as well as considerable improvement to generalisation when using data augmentation. We also show preliminary steps towards AGTT via DadaGP tokens, a task uniquely suited to GOAT. Finally, we propose prospective interesting applications and paths of research utilising GOAT including transcription, synthesis, playing technique identification and effect removal tasks. We hope that this dataset helps researchers further improve guitarfocused MIR research. 

660 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 8. ETHICAL STATEMENT 

We declare that, in the creation of the GOAT dataset, careful consideration was undertaken by the authors to ensure that the process follows the ethical guidelines supported by the ISMIR community. In this regard, we inform that (1) the content creators were made aware of the prospective applications and use cases for the data they provided, that (2) they agreed to such applications, and that (3) they were duly compensated for the data. However, due to the fact that the GOAT dataset contains covers (i.e. subjective renditions, performances and annotations/transcriptions) of popular songs, both in recorded audio and tablature formats, and because we do not exclusively own the copyrights for some of its content, we intend to make the dataset available for research purposes only, upon request. 

## 9. ACKNOWLEDGEMENTS 

This work is supported by the EPSRC UKRI Centre for Doctoral Training in Artificial Intelligence and Music (Grant no. EP/S022694/1) as well as UKRI Innovate UK (Project no. 10102804). 

## 10. REFERENCES 

- [1] A. Wiggins and Y. E. Kim, “Guitar Tablature Estimation with a Convolutional Neural Network,” in Proceedings of the International Society for Music Information Retrieval Conference (ISMIR), 2019, pp. 284– 291. 

- [2] X. Riley, D. Edwards, and S. Dixon, “High Resolution Guitar Transcription via Domain Ddaptation,” in International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2024, pp. 1051–1055. 

- [3] F. Cwitkowitz, T. Hirvonen, and A. Klapuri, “FretNet: Continuous-valued pitch contour streaming for polyphonic guitar tablature transcription,” in IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2023, pp. 1–5. 

- [4] J. Riley, Z. Guo, D. Edwards, S. Dixon et al., “GAPS: A Large and Diverse Classical Guitar Dataset and Benchmark Transcription Model,” in 25th International Society for Music Information Retrieval (ISMIR) Conference, 2024. 

- [5] J. Loth, P. Sarmento, C. Carr, Z. Zukowski, and M. Barthet, “ProgGP: From GuitarPro Tablature Neural Generation To Progressive Metal Production,” in 16th International Symposium on Computer Music Multidisciplinary Research, Tokyo, Japan, 2023. 

- [6] “ShredGP: Guitarist Style-Conditioned Tablature Generation,” in 16th International Symposium on Computer Music Multidisciplinary Research, 2023. 

- [7] A. Wright, E.-P. Damskägg, L. Juvela, and V. Välimäki, “Real-Time Guitar Amplifier Emulation with Deep Learning,” Applied Sciences, vol. 10, 

no. 3, p. 766, Jan. 2020. [Online]. Available: https://www.mdpi.com/2076-3417/10/3/766 

- [8] A. Wright, V. Välimäki, and L. Juvela, “Adversarial guitar amplifier modelling with unpaired data,” in ICASSP 2023-2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2023, pp. 1–5. 

- [9] Y.-H. Chen, Y.-T. Yeh, Y.-C. Cheng, J.-T. Wu, Y.-H. Ho, J.-S. R. Jang, and Y.-H. Yang, “Towards Zero-Shot Amplifier Modeling: One-to-many Amplifier Modeling via Tone Embedding Control,” Proceedings of the International Society for Music Information Retrieval Conference (ISMIR), 2024. 

- [10] Y.-H. Chen, W.-Y. Hsiao, T.-K. Hsieh, J.-S. R. Jang, and Y.-H. Yang, “Towards Automatic Transcription of Polyphonic Electric Guitar Music: A New Dataset and a Multi-loss Transformer Model,” in IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2022, pp. 786–790. 

- [11] J. Loth, P. Sarmento, S. Sarkar, and M. Barthet, “Analysis of MIDI as Input Representations for Guitar Synthesis,” in DMRN+19: Digital Music Research Network One-day Workshop, 2024. 

- [12] P. Sarmento, A. Kumar, C. Carr, Z. Zukowski, M. Barthet, and Y.-H. Yang, “DadaGP: a Dataset of Tokenized GuitarPro Songs for Sequence Models,” in Proceedings of the International Society for Music Information Retrieval Conference (ISMIR), 2021, pp. 610–618. 

- [13] Q. Xi, R. M. Bittner, J. Pauwels, X. Ye, and J. P. Bello, “GuitarSet: A Dataset for Guitar Transcription,” Proceedings of the International Society for Music Information Retrieval Conference (ISMIR), 2018. 

- [14] Y. Zang, Y. Zhong, F. Cwitkowitz, and Z. Duan, “SynthTab: Leveraging Synthesized Data for Guitar Tablature Transcription,” in IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2024, pp. 1286–1290. 

- [15] H. Pedroza, W. Abreu, R. M. Corey, and I. R. Roman, “Leveraging Real Electric Guitar Tones and Effects to Improve Robustness in Guitar Tablature Transcription Modeling,” in DAFx, 2024. 

- [16] ——, “Guitar-TECHS: An Electric Guitar Dataset Covering Techniques, Musical Excerpts, Chords and Scales Using a Diverse Array of Hardware,” IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2025. 

- [17] A. Radford, J. W. Kim, T. Xu, G. Brockman, C. McLeavey, and I. Sutskever, “Robust Speech Recognition via Large-Scale Weak Supervision,” in International Conference on Machine Learning. Proceedings of Machine Learning Research, 2023, pp. 28 492–28 518. 

661 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [18] P. Sarmento, A. Kumar, Y.-H. Chen, C. Carr, Z. Zukowski, and M. Barthet, “GTR-CTRL: Instrument and Genre Conditioning for Guitar-Focused Music Generation with Transformers,” in Proc. of the EvoMUSART Conf. Springer, 2023, pp. 260–275. 

- [19] P. Sarmento, “Guitar Tablature Generation with Deep Learning,” Ph.D. dissertation, Queen Mary University of London, August 2024. 

- [20] D. Edwards, X. Riley, P. Sarmento, and S. Dixon, “MIDI-to-Tab: Guitar Tablature Inference via Masked Language Modeling,” in Proceedings of the International Society for Music Information Retrieval Conference (ISMIR), 2024. 

- [21] H. Kim, S. Choi, and J. Nam, “Expressive Acoustic Guitar Sound Synthesis with an Instrument-Specific Input Representation and Diffusion Outpainting,” in IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2024, pp. 7620– 7624. 

   - [30] A. D’Hooge, L. Bigo, and K. Déguernel, “Modeling bends in popular music guitar tablatures,” in 24th International Society for Music Information Retrieval Conference. Milan, Italy: International Society for Music Information Retrieval, Nov 2023. 

   - [31] Y.-P. Chen, L. Su, Y.-H. Yang et al., “Electric Guitar Playing Technique Detection in Real-World Recording Based on F0 Sequence Pattern Recognition,” in Proceedings of the International Society for Music Information Retrieval (ISMIR), 2015, pp. 708–714. 

   - [32] M. Rice, C. J. Steinmetz, G. Fazekas, and J. D. Reiss, “General Purpose Audio Effect Removal,” in IEEE Workshop on Applications of Signal Processing to Audio and Acoustics (WASPAA). IEEE, 2023, pp. 1–5. 

   - [33] J. Imort, G. Fabbro, M. A. Martinez Ramirez, S. Uhlich, Y. Koyama, and Y. Mitsufuji, “Distortion Audio Effects: Learning How to Recover the Clean Signal,” in Proceedings of the International Society for Music Information Retrieval (ISMIR), 2022. 

- [22] C. Kehling, J. Abeßer, C. Dittmar, and G. Schuller, “Automatic tablature transcription of electric guitar recordings by estimation of score-and instrumentrelated parameters.” in DAFx, 2014, pp. 219–226. 

- [23] M. Stein, J. Abeßer, C. Dittmar, and G. Schuller, “Automatic Detection of Audio Effects in Guitar and Bass Recordings,” in Audio Engineering Society Convention 128. Audio Engineering Society, 2010. 

- [24] P. Sobot, “Pedalboard,” Jul. 2021. [Online]. Available: https://doi.org/10.5281/zenodo.7817838 

- [25] Q. Kong, B. Li, X. Song, Y. Wan, and Y. Wang, “HighResolution Piano Transcription with Pedals by Regressing Onset and Offset Times,” IEEE ACM Transactions on Audio, Speech and Language Processing, vol. 29, pp. 3707–3717, 2021. 

- [26] D. Edwards, S. Dixon, E. Benetos, A. Maezawa, and Y. Kusaka, “A Data-Driven Analysis of Robust Automatic Piano Transcription,” IEEE Signal Process. Lett., vol. 31, pp. 681–685, 2024. 

- [27] A. Caillon and P. Esling, “RAVE: A variational autoencoder for fast and high-quality neural audio synthesis.” [Online]. Available: http://arxiv.org/abs/ 2111.05011 

- [28] J. Engel, L. H. Hantrakul, C. Gu, and A. Roberts, “DDSP: Differentiable Digital Signal Processing,” in International Conference on Learning Representations (ICLR), 2020. 

- [29] B. Maman, J. Zeitler, M. Müller, and A. H. Bermano, “Performance conditioning for diffusion-based multiinstrument music synthesis,” in ICASSP 2024-2024 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2024, pp. 5045–5049. 

662 

