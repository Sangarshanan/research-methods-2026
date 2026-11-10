---
paper_id: "000061"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706504/files/000061.pdf"
---

# PIANOVAM: A MULTIMODAL PIANO PERFORMANCE DATASET 

Yonghyun Kim<sup>♭</sup> Junhyung Park<sup>♮</sup> Joonhyung Bae<sup>♯</sup> Kirak Kim<sup>♯</sup> Taegyun Kwon<sup>♯</sup> Alexander Lerch<sup>♭</sup> Juhan Nam<sup>♯</sup> ♭ Music Informatics Group, Georgia Institute of Technology, USA ♮ Department of Mathematical Sciences, KAIST, South Korea ♯ Graduate School of Culture Technology, KAIST, South Korea 

{yonghyun.kim, alexander.lerch}@gatech.edu, {tonyishappy, jh.bae, kirak, ilcobo2, juhan.nam}@kaist.ac.kr 

## ABSTRACT 

The multimodal nature of music performance has driven increasing interest in data beyond the audio domain within the music information retrieval (MIR) community. This paper introduces PianoVAM, a comprehensive piano performance dataset that includes videos, audio, MIDI, hand landmarks, fingering labels, and rich metadata. The dataset was recorded using a Disklavier piano, capturing audio and MIDI from amateur pianists during their daily practice sessions, alongside synchronized top-view videos in realistic and varied performance conditions. Hand landmarks and fingering labels were extracted using a pretrained hand pose estimation model and a semi-automated fingering annotation algorithm. We discuss the challenges encountered during data collection and the alignment process across different modalities. Additionally, we describe our fingering annotation method based on hand landmarks extracted from videos. Finally, we present benchmarking results for both audio-only and audio-visual piano transcription using the PianoVAM dataset and discuss additional potential applications. 

## 1. INTRODUCTION 

Music performance is inherently multimodal, involving not only audio but also motion, posture, and other visual elements as part of the expressive sound creation process [1,2]. In the field of Music Information Retrieval (MIR), there has been growing interest in collecting multimodal performance data to enhance the extraction of musical information by leveraging multiple modalities [3,4]. Such multimodal data —particularly audio-visual data— have been utilized in various MIR tasks across diverse musical genres. Examples include automatic MIDI transcription of solo piano performances [5,6], vibrato analysis of polyphonic string music [7], singing voice separation [8], and melodic motif identification in Indian vocal performances [9]. In these tasks, visual information from performer videos has been 

> © Y. Kim, J. Park, J. Bae, T. Kwon, K. Kim, A. Lerch and J. Nam. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: Y. Kim, J. Park, J. Bae, T. Kwon, K. Kim, A. Lerch and J. Nam, “PianoVAM: A Multimodal Piano Performance Dataset”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 



<!-- Start of picture text -->
Left, float, z=0.83<br>Right, z=1.069<br>File Composer Piece Name Gender Age Skill<br>M. Ravel Gaspard de la Nuit, M. 55, No. 1 Anonymized Male 20-29 Advanced<br><!-- End of picture text -->

Figure 1. The PianoVAM Dataset: Synchronized video, audio, MIDI with fingering, hand landmarks, and metadata. 

shown to improve model robustness by providing additional musical cues. This paper focuses on the multimodal data collection of solo piano performances to improve transcription and explore other potential applications. 

Piano transcription, which converts audio recordings into symbolic representations like MIDI or sheet music, is a well-established MIR task that has made significant progress through large-scale, clean audio-MIDI datasets such as MAESTRO [14] and carefully designed deep learning models [15, 16]. As benchmarking performance on the MAESTRO dataset approaches its ceiling [17], new challenges have emerged in piano transcription. One major challenge is achieving acoustic robustness to ensure reliable transcription from real-world piano performance recordings, which often feature diverse piano timbres, reverberation, or other interfering noise sources. While data augmentation has been a common technique to address this issue [10,18], leveraging visual data from performance videos has recently emerged as an alternative research direction [6,19–21]. Other key challenges include capturing richer performance information beyond a single MIDI track, such as left-right hand separation, piano fingering, and other playing details [12, 13]. Addressing these challenges requires capturing visual-domain data, such as performer motion or keyboard-view videos, and synchronizing them with audio and MIDI data. However, collecting such multimodal data is costly, requiring a dedicated data acquisition system, and time-consuming, as it depends on the availability of prepared piano players. 

This paper introduces PianoVAM, a comprehensive piano performance dataset that includes videos, audio, MIDI, hand landmarks, fingering labels, and rich metadata. An 

528 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

|Dataset|Size (hrs)|Video|Audio|Audio Type|MIDI|Fingering|
|---|---|---|---|---|---|---|
|MAESTROv3 [10]|198.7|✗|44.1–48kHz, Stereo|Real|✓|✗|
|MAPS (MUS subset) [11]|18.6|✗|44.1kHz, Stereo|Synth. & Real|✓|✗|
|OMAPS2 [6]|6.7|1080p/30fps|44.1kHz, Mono|Real|△(.TXT)|✗|
|PianoYT [5]|∼20|Varies|Varies (YouTube)|Varies (YouTube)|△(Pseudo)|✗|
|PianoVAM (Ours)|21.0|1080p/60fps|44.1kHz, Mono|Real|✓|△(Pseudo)|



Table 1. Comparison of piano transcription datasets. 

|Dataset|Total notes|# of pieces|Labeled ratio (%)|Data type|Reliability|Annotation|
|---|---|---|---|---|---|---|
|PIG [12]|100,044|309|100|MIDI & Score (.PDF)|By pianists|Manual|
|ThumbSet [13]|–|2,523|52|MusicXML|By miscellaneous|Manual|
|PianoVAM (Ours)|1,050,966|106|100|Multimodal|∼0.95|Semi-Auto|



Table 2. Comparison of piano fingering datasets. 

overview of PianoVAM is presented in Figure 1. The dataset was collected from amateur pianists during their daily practice sessions on a Disklavier piano, with synchronized topview videos captured in realistic and varied performance conditions. We extracted hand landmarks and generated fingering pseudo-labels using a pretrained hand pose estimation model combined with a semi-automated fingering detection algorithm. We describe the challenges faced during data collection and the alignment of multiple modalities. Furthermore, we detail our fingering annotation method, which utilizes hand landmarks extracted from the videos. Lastly, we present experimental results on both audio-only and audio-visual piano transcription using the PianoVAM dataset for benchmarking, along with a discussion of its potential applications. PianoVAM is available for download from the GitHub page<sup>1</sup> under the CC BY-NC 4.0 license. 

## 2. RELATED WORK 

## 2.1 Audio-Visual Datasets 

The emergence of audio-visual datasets represents a promising frontier in MIR, unlocking new research possibilities by providing visual information that complements audio signals. The URMP dataset [3] offers synchronized audio, video, and MIDI recordings of multi-instrument classical performances, supporting multimodal analysis of ensemble music such as audio-visual source association via vibrato modeling [7]. The Acappella dataset [8] contains solo a cappella videos, enabling audio-visual singing voice separation with fine-grained control over visual and acoustic conditions. Nadkarni et al. present an audio-visual dataset of Hindustani vocal performances annotated with melodic motifs and stable notes, enabling gesture-based music analysis and raga classification through movement-melody correspondence [9]. 

## 2.2 Piano Transcription Datasets 

Table 1 compares existing piano performance datasets with PianoVAM. MAESTRO [10] includes high-quality audio and MIDI data recorded from proficient pianists on Disklavier pianos but lacks top-view videos. While 

1 https://yonghyunk1m.github.io/PianoVAM 

MAPS [11] provides audio and MIDI from actual performances (MUS subset), a significant portion (210 out of 270 recordings) is synthesized. OMAPS2 [6] and PianoYT [5] incorporate video data but offer only limited MIDI annotations: OMAPS2 provides MIDI-like labels, while PianoYT uses pseudo-MIDI annotations transcribed with the Onsets and Frames model [14]. In comparison, PianoVAM offers the most comprehensive multimodal dataset, including real performance audio, synchronized MIDI, top-view videos, and fingering pseudo-labels, although its total duration is limited compared to the larger datasets listed. 

## 2.3 Fingering Datasets 

Table 2 compares existing piano fingering datasets with PianoVAM. PIG [12] incorporates fingering and MIDI information of sections of several pieces played by professional pianists, which also provides different fingerings for the same piece by various pianists. Ramoneda et al. [13] attempted to annotate fingering of the complete piece from partially annotated MusicXML files with the support of ThumbSet dataset, which in turn crowd-sourced fingering information of numerous pieces from MuseScore<sup>2</sup> , an online piano score website, but the source of fingering annotation is not clear. The presented PianoVAM dataset, in contrast, utilizes a fingering detection algorithm applied to top-view video data synced with MIDI and is improved by manual annotation of incomplete fingering labels to improve reliability. 

## 3. DATASET ACQUISITION & PRE-PROCESSING 

## 3.1 Acquisition 

We developed a data acquisition system to streamline the unsupervised recording of video, audio, MIDI, and associated metadata, such as performer and piece details. 

## 3.1.1 Acquisition Workflow 

The acquisition workflow comprises the following steps. First, new users register by providing basic personal details and receive unique QR codes for identification and recording control. A single interface launch initializes the required software: OBS Studio for video and audio, and 

2 https://musescore.com (Last accessed: June 28, 2025) 

529 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
Pitch Distribution Velocit y  Distribution Sustain Pedal Usa g e Distribution<br>1. 0<br>12 0<br>10 0<br>10 0 0. 8<br>8 0<br>8 0 0. 6<br>6 0 6 0<br>0. 4<br>4 0<br>4 0 0. 2<br>2 0<br>2 0 0 0. 0<br>MAESTROv3: Min=21, Median=64, Max=108 MAESTROv3: Min=1, Median=66, Max=126 MAESTROv3: Min=0.00, Median=0.66, Max=0.99<br>PianoVAM: Min=21, Median=65, Max=108 PianoVAM: Min=1, Median=65, Max=126 PianoVAM: Min=0.00, Median=0.91, Max=1.00<br>MIDI Note<br>MIDI Velocity<br>Sustain Pedal Usage Ratio<br><!-- End of picture text -->

Figure 2. Distributional comparison of pitch, velocity, and pedal usage between MAESTROv3 and PianoVAM. 

Logic Pro for audio and MIDI. Before recording, users input performance details and display their profile QR code to a top-view camera to begin capturing. When the performance concludes, presenting a stop QR code ends the recording. 

## 3.1.2 Hardware Setup 

The data acquisition process was managed by a control script on a PC. An overhead-mounted webcam captured the video, while a dedicated microphone and a Disklavier piano provided the audio and MIDI signals, respectively. OBS Studio recorded the audio-video stream, and Logic Pro concurrently recorded the audio-MIDI stream. A common audio signal captured by both systems provided a reference for the global time alignment to correct for recording latency. 

## 3.2 Pre-processing 

## 3.2.1 Alignment 

The time alignment of audio and MIDI data was further refined using the fine alignment technique used for the MAESTRO dataset [10]. Specifically, the recorded audio was down-mixed to mono and resampled to 22.05kHz. The MIDI data was then synthesized into an audio signal at the same sampling rate using FluidSynth with a SoundFont sampled from Disklavier Pro recordings,<sup>3</sup> since we could not access the original Disklavier7 SoundFont. A ConstantQ Transform was applied to both audio signals using a hop length of 64 samples (∼3ms resolution). Finally, we applied Dynamic Time Warping within a Sakoe-Chiba band of ±2.5s to correct any remaining temporal discrepancies, such as small constant offsets or jitter. 

## 3.2.2 Audio Loudness Normalization 

Recordings were collected over a six-month period in a shared studio, with a notable gap between May and August. This interruption may have introduced inconsistencies in loudness due to variations in recording conditions, such as gain settings or microphone placement. To mitigate potential mismatches between loudness and MIDI velocity across the dataset, we applied a loudness normalization procedure. First, the collected MIDI data were synthesized using FluidSynth with a Disklavier-sampled SoundFont<sup>3</sup> . The integrated loudness of each synthesized audio file was 

> 3 https://freepats.zenvoid.org/Piano/YDP-GrandPiano/YDPGrandPiano-SF2-20160804.tar.bz2 (Last accessed: June 28, 2025) 

measured using the pyloudnorm package [22]. We then computed the average loudness across all rendered files and defined −23 LUFS as the desired global average. A uniform gain offset was calculated based on the difference between the measured average and this global reference. This offset was then applied to each rendered file’s loudness to yield a unique target loudness per rendition. Each real PianoVAM audio recording was then scaled to match the target loudness of the corresponding rendition. This process is designed to enhance loudness-velocity consistency while preserving the natural dynamic range of the performances. 

## 4. DATASET STATISTICS 

The dataset contains 106 solo piano recordings from 10 amateur performers, totaling approximately 21 hours. The repertoire is stylistically diverse, spanning works from 38 composers from the Baroque to modern eras (e.g., Bach, Chopin, Kapustin, Joe Hisaishi) and includes several improvisations. Performers’ self-reported skill levels are advanced (70 recordings), intermediate (26), and beginner (10). Although the recording system allowed performers to choose between two performance types —Performance and DailyPractice— all recordings were self-labeled as DailyPractice. This indicates that the dataset primarily captures informal practice sessions where strict score adherence cannot always be expected. 

To investigate differences in expressive characteristics across datasets, we conducted a brief comparative analysis of MIDI-related distributions between MAESTROv3 and PianoVAM. Specifically, we examined three aspects displayed in Figure 2: (i) the distribution of pitch (MIDI note numbers), (ii) the distribution of velocity (MIDI velocity values), and (iii) the distribution of sustain pedal usage on a per-file basis. We computed Cohen’s d for each musical feature to assess the practical significance of inter-dataset differences. Pitch (d = 0.0446) and velocity (d = -0.0379) exhibited negligible differences between datasets. However, pedal usage revealed a large effect size (d = 0.870), indicating a substantially higher use of the sustain pedal in PianoVAM compared to MAESTROv3. We speculate this difference stems from an interplay between a pedaldemanding Romantic/Impressionist repertoire, the generous pedaling tendencies of amateur performers in practice, and a less reverberant studio environment that encourages compensation. 

530 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
Input Preprocess<br>If  depth < threshold<br>Video<br>then  detect floating hand(s)<br>Framewise hand area<br>MIDI<br>detection<br>Keyboard  Hand landmark detection<br>area info (MediaPipe)<br>Framewise finger position<br>evaluation<br>Calculate finger score<br>for each note<br>Output If  a single candidate<br>then  determine fingering<br>MIDI w/ hand &<br>fingering info else  human selection from<br>multiple candidates<br>Labeling<br><!-- End of picture text -->

Figure 3. Flowchart of the fingering detection algorithm. 

## 5. ANNOTATION OF FINGERING LABELS 

To generate fingering annotations, we developed the hybrid algorithm shown in Figure 3. The algorithm first processes performance videos to map hand landmarks to potential finger candidates for each MIDI note. For notes with a single, unambiguous candidate, the fingering is determined automatically, achieving a precision of ∼95% (cf. Table 3). In ambiguous cases with multiple candidates (affecting ∼20% of notes), a custom GUI prompts a human annotator to make the final selection. This approach ensures complete and accurate fingering annotations for the entire dataset. 

## 5.1 Inputs & Outputs 

The inputs are video, MIDI, keyboard corner locations and lens distortion coefficients in the first frame for each video, which can also be set manually by the GUI-based annotation tool. The outputs are fingering information, and a separate MIDI file for each hand. 

## 5.2 Method 

The algorithm suggests candidates fingers that are likely to play each note in the MIDI file. First, hand landmark information is extracted from the input video frame with MediaPipe Hands [23]. A floating hand obfuscating the other hand but not playing any notes should be detected and excluded from the pool of candidates. Thus, we define a metric to measure the z-depth of a hand to detect such floating hands. Assuming that we know the hand skeleton of the player explicitly, we can calculate the z-depth from the xy coordinate information. For each video, we find the model skeleton of each hand, which is a standard for all skeletons that should be unbent, not tilted, and on the keyboard. To measure tilt, the plane defined by three hand key points, namely Wrist (W ), Index Finger Metacarpals (I), 

and Ring Finger Metacarpals (R), is utilized. We assume that the angle ∠IWR of the untilted skeleton (parallel to the plane of the keyboard) should be close to 28<sup>◦</sup> , which is our heuristic estimate for the average human hand in its neutral position. To measure how much the hand is bent, <mark>|</mark> △IW R <mark>|</mark> we calculate the ratio r = |W F1F2F3F4F5|<sup>of |△IWR| and</sup> area of the hexagon |WF1F2F3F4F5| where Fi is the fingertip of the ith finger. Finally, assuming that the hand is playing in the majority of frames, the median △IWR is selected as the default position: 



<!-- Start of picture text -->
I0W0R0 = |∠IW R−28median ◦ | low 10%,r high 50% |△IWR|. (1)<br><!-- End of picture text -->

Let the plane of the projected 2D image be z = z0, and the area of 2D image be 



<!-- Start of picture text -->
A := {(x, y)|x ∈ (−1, 1), y ∈ (−AR, AR)} ⊂ R 2<br>∼= {(x, y, z0)|x ∈ (−1, 1), y ∈ (−AR, AR)} ⊂ PR 3 ,<br><!-- End of picture text -->



<!-- Start of picture text -->
(2)<br><!-- End of picture text -->

where the origin of real projective space PR<sup>3</sup> is the center of the camera lens and AR is the aspect ratio of the video. Since the goal is to calculate the relative depth rather than the real depth, we set z0 = 1 for convenience of calculation. Knowing that the original point is contained in the line {(xt, yt, t)|t ∈ R<sup>+</sup> }, we have three equations likely in general position and three variables to solve t, u, v > 0 from 



<!-- Start of picture text -->
||(xI t, yI t, t), (xW u, yW u, u)||R3 = �� I0W0 �� (3)<br>||(xW u, yW u, u), (xRv, yRv, v)||R3 = �� W0R0 �� (4)<br>||(xRv, yRv, v), (xI t, yI t, t)||R3 = �� R0I0 �� . (5)<br><!-- End of picture text -->

Here, our desired solution can be approximately calculated using Powell’s dog leg algorithm with a close initial guess (ti, ui, vi) = (1, 1, 1). By substituting the solution (t, u, v), we get the 3D coordinates of I, W, R. Finally, d = (t + u + v)/3 becomes the relative z-depth of the mass of the center of the hand skeleton of each frame. If the z-depth is less than the threshold 0.9, or equivalently, if the hand is floating more than 10% of the distance between the camera and the keyboard, we decide that the target hand of the target frame is floating. 

After discarding all floating hands from the detection, possible finger candidates for each note can be chosen. For each note, a fingering score is calculated, indicating the likelihood of each finger pressing the note. The score is based on the number of frames in which the fingertip is in the selected note area. If the fingertip is completely in the area, a value of 1 is assigned; if it is slightly off, a correction weight is applied, reducing the score for this frame. Thus, the final fingering score cannot exceed the total number of frames of each note. From the fingering score of each finger for the nth note, we add the finger as a normal candidate or a strong candidate if the fingering score is greater than 50% or 80% of the theoretical maximum score (note length in frames), respectively. If there exists only one strong candidate, we pick the strong candidate as the only candidate. Note that there might be notes with either no candidate or multiple candidates, in which case the algorithm will leave these notes unlabeled. 

531 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

|Piece (Index)|Prec.<br>(150)|Total<br>No C.|Total<br>Multi C.|
|---|---|---|---|
|Chopin, Op.18 (8)|91.7|12.7|8.0|
|Debussy, L.75 Mvt.3 (17)<sup>∗</sup>|97.1|7.9|2.8|
|Grieg, Op.16 Mvt.2 (18)|99.3|10.6|4.4|
|Yiruma, Kiss the Rain (29)|95.2|5.9|8.7|
|Improvisation (31)|98.6|16.7|3.0|
|Schumann, Op.17 Mvt.1 (34)|82.9|8.0|5.4|
|Kapustin, Op.40 No.6 (42)|98.4|8.4|5.5|
|Scarlatti, K.380 (60)|100.0|3.7|3.5|
|Ravel, M.30 (81)|92.4|35.1|4.4|
|Satie, Gymnopedie No.1 (93)|100.0|4.1|2.4|
|Average of 10 pieces|95.6|13.0<sup>†</sup>|5.1<sup>†</sup>|



Table 3. Precision (Prec.) over first 150 notes, percentage of notes with none or multiple candidates (C.) over all notes for selected 10 pieces (<sup>∗</sup> For finger substitutions, we admit both fingers as correct fingering;<sup>†</sup> Weighted average with the number of total notes of each piece as the weight). 

## 5.2.1 Reliability 

With the support of the dedicated GUI-based fingering annotation tool, we manually labeled the ground truth fingering for the first 150 notes of 10 pieces in PianoVAM to assess the results. As detailed in Table 3, the algorithm achieved an average precision of over 95%, with most prediction errors involving adjacent fingers. The table also reports the percentage of notes with no candidates and multiple candidates. Notably, Ravel’s Jeux d’eau stands out as an outlier with a high ratio of notes without candidates. Excluding this piece, the weighted averages for notes with no and multiple candidates are 9.4% and 5.2%, respectively. 

|Train Dataset|Note|w/ Offset|w/ Vel.|Frame|
|---|---|---|---|---|
|MAESTROv3|93.4|62.3|90.3|78.2|
|PianoVAM|95.8|60.4|93.9|80.0|
|Combined|95.2|73.5|93.0|86.9|



Table 4. Transcription F1 scores on the PianoVAM test split. Bold: highest; Underline: significantly higher than the lowest; Double-line: significantly higher over both others (p < .0167). 

model [14], following its original specifications. The model was trained on each dataset as well as on a combined version. We utilized the model weights corresponding to the checkpoint with the lowest validation loss for inference. 

The results in Table 4 are reported as F1 Scores (%) and calculated over the entire duration of the respective test splits. The terms Note, w/ Offset, and w/ Vel. refer to note evaluation with onset, with onset & offset, and with onset & velocity, respectively (cf. [15]). All four evaluation metrics, including Frame, were computed using the mir_eval package [24]. Following established transcription research conventions, offset timings were adjusted to the pedal-release time if the sustain pedal remained engaged. 

Statistical tests confirm that significant differences across training sets for all metrics (Friedman test, p < .001). Posthoc Wilcoxon tests with Bonferroni correction (α = .0167) showed that both PianoVAM and Combined models significantly outperformed MAESTROv3 in Note and w/ Velocity. For w/ Offset and Frame, only the Combined model yielded significantly higher than both others. While PianoVAM slightly outperformed Combined in Note and w/ Velocity, only the latter difference was statistically significant. 

## 6. BENCHMARK RESULTS 

## 6.3 Audio-Visual Piano Transcription 

To demonstrate its utility, we benchmark the PianoVAM dataset on the task of piano transcription under two settings: audio-only and audio-visual. The audio-visual experiments are specifically designed to assess the visual modality’s contribution to enhancing performance under challenging acoustic conditions. 

## 6.1 Data Split 

To facilitate reproducibility of results, we provide information on data splits designed to meet the following criteria: (i) no composition appears in more than one split, and (ii) the dataset is divided approximately into 80/10/10 percent for the training, validation, and test set, respectively, based on total duration. The resulting train/validation/test splits contain 73, 19, and 14 files, respectively. While these splits are intended to support reproducibility and comparability, we acknowledge that different experimental objectives might require different splits. 

## 6.2 Audio-Only Piano Transcription 

As MAESTRO is widely regarded as a standard dataset in piano transcription research, we deemed it a suitable reference point for evaluating our dataset. Accordingly, we performed a comparative analysis using the Onsets and Frames 

Various approaches have been explored for piano transcription when both audio and video are available. For instance, Wan et al. and Wang et al. proposed methods enhancing the output of an audio-only AMT system by incorporating visual information [19, 20], while Li et al. utilized both modalities jointly to improve onset prediction [6,21]. 

For this benchmark experiment, we focus on examining how visual information can be used to improve transcription performance under suboptimal recording conditions. We implement a simple post-processing pipeline that refines MIDI outputs from an audio-only AMT model by using top-view video, estimated piano keyboard corner coordinates, and hand skeletons detected with MediaPipe Hands [23]. This process enables the elimination of physically implausible notes by referencing visual evidence, thereby improving onset precision. The full implementation and additional details are available on GitHub<sup>1</sup> , and a brief overview follows. 

First, onset events are extracted from the predicted MIDI file. For each onset, the nearest video frame is retrieved, and hand landmarks are predicted [23]. Each video frame’s timestamp is defined as the midpoint of the time interval it covers. If no hand is detected, the corresponding onset is unchanged. When both hands are detected, a perspective transformation is applied using the keyboard cor- 

532 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

|Input|Method<br>|Precision|Recall|F1|
|---|---|---|---|---|
||Vanilla|96.0|43.7|57.2|
|Noisy|+ NoiseAug|96.1|82.8|88.7|
||+ Video|97.2|82.7|89.2|
|Rb|Vanilla|66.8|68.2|64.4|
|evererant|+ Video|68.1|67.8|64.8|



Table 5. Onset prediction performance under different acoustic conditions. Bold: highest in each column; Underline: significantly higher over the preceding method (paired t-test, p < 0.05). 

ner metadata to produce a normalized rectangular image (H : W = 125 : 1024), which maintains the standard height-to-width ratio (1 : 8.147) of an 88-key piano. The same transformation is applied to the predicted hand landmarks. Assuming that the 52 white keys are evenly spaced, the algorithm estimates which white key region each fingertip corresponds to, based on its transformed x-coordinate. To account for possible errors in hand landmark detection, multiple candidate keys are considered for each fingertip, with a tunable threshold determining the candidate range (±2 white keys in our experiment). The final set of valid pitch candidates is obtained by intersecting all fingertip candidate sets. For each onset, if the pitch predicted by the audio-only AMT model falls within this candidate set, the note is retained; otherwise, it is discarded. This process is repeated for all onsets in the transcription. 

Table 5 summarizes onset prediction performance under two challenging acoustic conditions: SNR=0dB Gaussian noise, and added reverberation. To evaluate the model’s robustness under reverberant acoustic conditions, we applied convolutional reverb using a real-world impulse response (IR) recorded in St. George’s Church<sup>4</sup> . The IR was originally sampled at 96kHz and downsampled to 16kHz to match the audio input. All audio samples were convolved with the mono version of this IR using FFT-based convolution. To compensate for the inherent delay in the IR (with its peak located at sample index 653), we removed the first 653 samples from each convolved output to ensure proper temporal alignment. The resulting signals were then peak-normalized to maintain consistent amplitude and avoid distortion. 

Under noisy conditions, the baseline model (Vanilla), trained on clean audio only, exhibited substantial degradation. Introducing noise during training (+ NoiseAug) significantly improves recall and F1 (p < .0001), while precision remains unchanged. For the + NoiseAug condition, the model was trained on a 50/50 mixture of original clean audio and augmented noisy samples. The noisy samples were generated by adding Gaussian noise with signal-to-noise ratios (SNR) randomly sampled from 0 to 24dB (cf. [25]). Adding visual filtering (+ Video) further improves precision (p = .0052) and F1 (p = .0101), however, the gain in recall is not statistically significant. 

> 4 https://webfiles.york.ac.uk/OPENAIR/IRs/st-georges-episcopalchurch/st-georges-episcopal-church.zip; st_georges_far.wav (Last accessed: June 28, 2025) 

In reverberant conditions, visual post-processing significantly improves precision (p = .0005) and marginally improves F1 (p = .0508), with no significant change in recall. Qualitative inspection revealed that reverberant tails were sometimes misclassified as new onsets and the visual modality helped reduce such errors. 

## 7. DISCUSSION 

The dataset was collected using a system designed to facilitate unsupervised recording, allowing performers to play freely without on-site assistance. While this approach streamlines data acquisition, the dataset exhibits biases in performer identity, pedal usage, and composer representation. In addition, since all recordings originate from practice sessions, the dataset is unsuitable for comparative studies with corresponding musical scores. Our fingering detection approach, while promising, faces challenges from visual ambiguities. These arise from both complex pianistic techniques, such as the multi-finger preparations for rapid repetitions in Chopin’s Grande valse brilliante, and visual artifacts like performance-induced motion blur in Ravel’s Jeux d’eau or shadows in the Schumann’s Fantasie in C recording. Furthermore, the algorithm is intentionally focused on conventional playing, thus excluding extended techniques like glissandi or playing with the fist. Our future extensions may include expert performances, expanded modalities (e.g., multi-angle video), and contextually rich data to support more robust and musically meaningful analysis. Moreover, we aim to improve fingering detection precision by leveraging state-of-the-art models for hand pose estimation [26] and 3D reconstruction [27]. 

## 8. CONCLUSION 

We presented PianoVAM, a comprehensive multimodal dataset of amateur piano practice sessions that captures synchronized top-view video, audio, MIDI, hand landmarks, fingering labels, and rich metadata. Recorded using a Yamaha Disklavier in natural, varied practice conditions, PianoVAM addresses key limitations of existing datasets that often lack specific modalities or rely on synthetic or incomplete annotations. To generate fingering labels, we propose a semi-automated method that combines hand landmark detection from video with manual refinement. We also discuss the challenges of multimodal alignment and data collection. To demonstrate the utility of PianoVAM, we report baseline results for both audio-only and audio-visual piano transcription tasks and showcase its potential for advancing a range of MIR applications. Future extensions of the dataset may address current imbalances in musical content and metadata diversity. 

## 9. ETHICS STATEMENT 

This study involved human participants for data collection, which was approved by the Institutional Review Board (IRB) at KAIST (Approval No. KH2023-235). All procedures strictly adhered to established ethical guidelines. 

533 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 10. ACKNOWLEDGMENTS 

We sincerely appreciate the KAIST music and audio computing lab and PIAST (Piano club) members who participated in the dataset acquisition as performers. This research was supported by the National Research Foundation of Korea (NRF) funded by the Korea Government (MSIT) under Grant RS-2023-NR077289 and Grant RS-2024-00358448. 

and generation with the MAESTRO dataset,” in Proceedings of the International Conference on Learning Representations (ICLR), 2019. 

- [11] V. Emiya, N. Bertin, B. David, and R. Badeau, “Maps - a piano database for multipitch estimation and automatic transcription of music,” Research Report, Tech. Rep., 2010. [Online]. Available: https: //hal.inria.fr/inria-00544155 

## 11. REFERENCES 

- [1] V. Bergeron and D. M. Lopes, “Hearing and seeing musical expression,” Philosophy and Phenomenological Research, vol. 78, no. 1, pp. 1–16, 2009. 

- [2] F. Platz and R. Kopiez, “When the eye listens: A metaanalysis of how audio-visual presentation enhances the appreciation of music performance,” Music Perception: An Interdisciplinary Journal, vol. 30, no. 1, pp. 71–83, 2012. 

- [3] B. Li, X. Liu, K. Dinesh, Z. Duan, and G. Sharma, “Creating a multitrack classical music performance dataset for multimodal music analysis: Challenges, insights, and applications,” IEEE Transactions on Multimedia, vol. 21, no. 2, pp. 522–535, 2018. 

- [4] Z. Duan, S. Essid, C. C. S. Liem, G. Richard, and G. Sharma, “Audiovisual analysis of music performances: Overview of an emerging field,” IEEE Signal Processing Magazine, vol. 36, no. 1, pp. 63–73, 2019. 

- [5] A. S. Koepke, O. Wiles, Y. Moses, and A. Zisserman, “Sight to sound: An end-to-end approach for visual piano transcription,” in Proceedings of the IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2020, pp. 1838–1842. 

- [6] Y. Li, X. Wang, R. Wu, W. Xu, and W. Chen, “A crnngcn piano transcription model based on audio and skeleton features,” in IEEE International Conference on Acoustics, Speech, and Signal Processing Workshops (ICASSPW), 2023, pp. 1–5. 

- [7] B. Li, C. Xu, and Z. Duan, “Audiovisual source association for string ensembles through multi-modal vibrato analysis,” in Proceedings of the Sound and Music Computing Conference (SMC), 2017. 

- [8] J. F. Montesinos, V. S. Kadandale, and G. Haro, “A cappella: Audio-visual singing voice separation,” in Proceedings of the 32nd British Machine Vision Conference (BMVC), 2021. 

- [9] S. Nadkarni, P. Rao, and M. Clayton, “Identifying melodic motifs and stable notes from gestural information in indian vocal performances,” Transactions of the International Society for Music Information Retrieval, vol. 7, no. 1, 2024. 

- [10] C. Hawthorne, A. Stasyuk, A. Roberts, I. Simon, C.Z. A. Huang, S. Dieleman, E. Elsen, J. Engel, and D. Eck, “Enabling factorized piano music modeling 

- [12] E. Nakamura, Y. Saito, and K. Yoshii, “Statistical learning and estimation of piano fingering,” Information Sciences, vol. 517, pp. 68–85, 2020. 

- [13] P. Ramoneda, D. Jeong, E. Nakamura, X. Serra, and M. Miron, “Automatic piano fingering from partially annotated scores using autoregressive neural networks,” in Proceedings of the 30th ACM International Conference on Multimedia (ACM MM), 2022, pp. 6502–6510. 

- [14] C. Hawthorne, E. Elsen, J. Song, A. Roberts, I. Simon, C. Raffel, J. Engel, S. Oore, and E. D, “Onsets and frames: Dual-objective piano transcription,” in Proceedings of the 19th International Society for Music Information Retrieval Conference (ISMIR), 2018, pp. 50–57. 

- [15] Q. Kong, B. Li, X. Song, Y. Wan, and Y. Wang, “Highresolution piano transcription with pedals by regressing onset and offset times,” IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 29, pp. 3707–3717, 2021. 

- [16] W. Wei, P. Li, Y. Yu, and W. Li, “Hppnet: Modeling the harmonic structure and pitch invariance in piano transcription,” in Proceedings of the 23rd International Society for Music Information Retrieval Conference (ISMIR), 2022, pp. 709–716. 

- [17] Y. Yan and Z. Duan, “Scoring time intervals using nonhierarchical transformer for automatic piano transcription,” in Proceedings of the 25th International Society for Music Information Retrieval Conference (ISMIR), 2024, pp. 973–980. 

- [18] D. Edwards, S. Dixon, E. Benetos, A. Maezawa, and Y. Kusaka, “A data-driven analysis of robust automatic piano transcription,” IEEE Signal Processing Letters, vol. 31, pp. 681–685, 2024. 

- [19] Y. Wan, X. Wang, R. Zhou, and Y. Yan, “Automatic piano music transcription using audio-visual features,” Chinese Journal of Electronics, vol. 24, no. 3, pp. 597– 603, 2015. 

- [20] X. Wang, W. Xu, J. Liu, W. Yang, and W. Cheng, “An audio-visual fusion piano transcription approach based on strategy,” in Proceedings of the 24th International Conference on Digital Audio Effects (DAFx), 2021, pp. 308–315. 

- [21] Y. Li, X. Wang, R. Wu, W. Xu, and W. Cheng, “A two-stage audio-visual fusion piano transcription model 

534 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

based on the attention mechanism,” IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 32, pp. 3618–3630, 2024. 

- [22] C. J. Steinmetz and J. D. Reiss, “pyloudnorm: A simple yet flexible loudness meter in python,” in 150th AES Convention, 2021. 

- [23] F. Zhang, V. Bazarevsky, A. Vakunov, A. Tkachenka, G. Sung, C.-L. Chang, and M. Grundmann, “Mediapipe hands: On-device real-time hand tracking,” 2020. [Online]. Available: https://arxiv.org/abs/2006.10214 

- [24] C. Raffel, B. McFee, E. J. Humphrey, J. Salamon, O. Nieto, D. Liang, D. P. Ellis, and C. C. Raffel, “Mir_eval: A transparent implementation of common mir metrics.” in Proceedings of the 15th International Society for Music Information Retrieval Conference (ISMIR), 2014, pp. 367–372. 

- [25] Y. Kim and A. Lerch, “Towards robust transcription: Exploring noise injection strategies for training data augmentation,” in Late Breaking Demo of the 25th International Society for Music Information Retrieval Conference (ISMIR), 2024. 

- [26] Y. Xu, J. Zhang, Q. Zhang, and D. Tao, “ViTPose++: Vision Transformer for Generic Body Pose Estimation,” IEEE Transactions on Pattern Analysis & Machine Intelligence, vol. 46, no. 02, pp. 1212–1230, 2024. 

- [27] H. Dong, A. Chharia, W. Gou, F. Vicente Carrasco, and F. D. De la Torre, “Hamba: Single-view 3d hand reconstruction with graph-guided bi-scanning mamba,” Advances in Neural Information Processing Systems, vol. 37, pp. 2127–2160, 2024. 

535 

