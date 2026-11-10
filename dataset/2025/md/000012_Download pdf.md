---
paper_id: "000012"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706343/files/000012.pdf"
---

# PREDICTING FLUTIST ONSET TIMING IN DUET PERFORMANCE: A MULTIMODAL ANALYSIS OF GESTURE AND BREATH CUES 

Jaeran Choi Taegyun Kwon Juhan Nam Graduate School of Culture Technology, KAIST, South Korea 

```
{jaeran.choi,ilcobo2,juhan.nam}@kaist.ac.kr
```

## ABSTRACT 

- 1 ABSTRACT 37 38 

- 2 In ensemble performances, musicians use gesture and 39 3 breath cues to synchronize their initial notes at the begin40 4 ning of a piece, but the precise relationship between these 41 5 cues and onset timing remains under-explored. This study 42 6 investigates how flutists’ gesture and breath cues encode 43 7 the timing information for the initial note onset. This re44 8 search consists of four components: (1) Collection of a cue 45 9 dataset containing synchronized video and audio record46 

- 10 ings of flute-piano duets, (2) Identification of cue candidate 47 11 points through facial movement curves and breath onset48 12 offset analysis, (3) Verification of predicted onset accuracy 49 13 using linear regression on these cues compared to human 50 14 onset asynchronies and (4) Introduction and exploration of 51 15 a ‘trigger’ concept, defined as immediate, clearly perceiv52 16 able gestures (such as stopping or raising the head) indi53 17 cating the precise moment of onset. Our findings suggest 54 18 a dual-cue system: preparatory cues broadly predict onset 55 19 timing, while precise triggers refine the exact onset. We 56 20 compared the time difference between the predicted and 57 21 piano onsets with the flute–piano asynchronies and veri58 22 fied the concepts of cue and trigger through expert inter59 23 views. This research contributes to a deeper understanding 60 24 of the complex phenomena of musical cues during perfor61 25 mance through multimodal analysis. This paper provides 62 26 an open-access cue dataset, which can be found on the ac63 27 companying website.<sup>1</sup> 64 

65 

1. INTRODUCTION 66 67 is inherently multimodal, combining 68 

28 

- 29 Music performance is inherently multimodal, combining 30 sound and motion. Although these elements primarily con31 vey musical expression to audiences [1], they also play a 32 critical role in ensemble synchronization among perform33 ers [2]. Performers often employ specific gestures and 34 breathing sounds as musical cues to synchronize their note 35 onsets, particularly at the beginning or during critical mo36 ments in a performance. The convention of cueing approx- 

69 

70 71 

72 

73 

74 

75 

1 https://github.com/jaeranchoi/flutist_cue_dataset 76 

77 

78 

> © J. Choi, T. Kwon and J. Nam.. Licensed under a Creative 79 Commons Attribution 4.0 International License (CC BY 4.0). Attribution: J. Choi, T. Kwon and J. Nam., “Predicting Flutist Onset Timing in 80 Duet Performance: A Multimodal Analysis of Gesture and Breath Cues”, 81 in Proc. of the 26th Int. Society for Music Information Retrieval Conf., 82 Daejeon, South Korea, 2025. 83 

imately one beat before the musical onset has been extensively documented in previous studies [3–5]. Head nodding gestures, in particular, are commonly used as intuitive musical cues, and previous studies have utilized such gestures to define cue timings, even extending their application to interactions with robotic musicians [5–7]. Therefore, understanding musical cues not only deepens synchronization knowledge but is also crucial for designing interactive performance systems. 

Previous studies have examined the role of gestures and breathing in performer synchronization. Bishop et al. showed that performers use visual and auditory cues to synchronize after silence or rests [8]. Additionally, gestures at the beginning of a piece were found to correlate with tempo, particularly through falling acceleration curves that typically reach their midpoint approximately one beat before the onset [9]. However, this midpoint timing was often not precisely one beat ahead, and exact onset prediction based on these curves was not explored. Vera et al. demonstrated increased onset asynchrony when performers restarted together after rests without visual contact, and identified relationships between breath onsetoffset timings and rest durations, yet did not clarify how gestures or breathing specifically encode onset timing [10]. Although these studies highlight the significance of gestures and breath cues in synchronization, they have not thoroughly investigated how combined visual and auditory cues precisely predict intended onset timing, especially at the beginning of a piece. 

One reason for the limited quantitative analyses in previous studies is the difficulty of accurately tracking gestures. Bishop et al. utilized Kinect sensors and accelerometers to measure motion curves [9], while Timmers et al. employed infrared markers to measure bow velocity in a string quartet setting [11]. In contrast, our approach uses sensorless image processing techniques, applying optical flow methods [12] to quantitatively track facial gesture movements. 

This paper investigates how a flutist’s intended onset timing is encoded through gesture and breath cues, comprising four main components: (1) Collection of synchronized video and audio data from flute-piano duet performances involving 20 flutists (Total 1,320 trials), (2) Extraction and annotation of gesture cue features using face movement curves analyzed by optical flow, alongside manual annotation of breath onset and offset timings, (3) Verification of predictive accuracy for cue-based onset pre- 

100 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
Cue Dataset Cue Feature Extraction & Detection Onset Prediction Evaluation<br>Video Gesture Cue<br>Facial Area Motion Curve Max & Min Peak Detection<br>Detection Extraction Quantitative<br>(Mediapipe) (Optical Flow) Max & Min Peak Annotation Evaluation<br>Linear<br>Regression<br>Breath Cue &<br>Audio Breath Cue Onset & OffsetAnnotation Onset<br>Prediction<br>Qualitative<br>Evaluation<br>Flute & Piano Onset<br>MWM Flute & Piano Onset<br>Annotation<br><!-- End of picture text -->

Figure 1: The overall framework for the musical cue detection and onset timing prediction 

84 dictions by comparing linear regression–derived timings to 129 85 observed human onset asynchronies and (4) Exploration of 130 86 a trigger concept, which involves three types of immediate, 131 87 clearly perceivable movements: quickly raising the head, 132 88 stopping head movement after the cue or slowly raising the 133 89 head. The first type just before fully raising the head, the 134 90 second triggers onset immediately after stopping, and the 135 91 third provides a less clear signal. These trigger movements 136 92 allow performers to precisely detect the onset moment for 137 93 accurate synchronization. 138 94 Our analysis demonstrates clear relationships between 139 95 the lengths of gesture and breath cues and onset timings. 140 96 Gesture cues showed a linear relationship between po141 97 sition, velocity and acceleration peaks in vertical facial 142 98 movements and subsequent onset timing. Similarly, breath 143 99 cues exhibited a correlation between breath duration and 144 100 the timing interval to the note onset, with variations ob145 101 served across different tempos. We further verified our hy146 102 potheses through expert interviews. Additionally, we con147 103 ducted a case study to address related phenomena, includ148 104 ing adaptation effects—reduced discrepancies through re149 105 peated rehearsal—and instances of cue execution failures, 150 106 where significant differences between cue-based predicted 107 onset and actual onset were observed. Based on these 151 152 108 observations, we conclude that musicians utilize two pri153 109 mary synchronization strategies: rough timing indication 154 110 through gesture and breath cues, and precise, immediate 111 signals through triggers. Furthermore, exact synchroniza155 112 tion is refined through repetitive rehearsals. 156 157 158 

## 2. RELATED WORKS 

113 

159 

## 2.1 Musical Cue for Synchronization 

114 

115 Musical cues, essential for performer communication, 160 116 include visual gestures and non-musical elements like 161 117 breathing. They are particularly valuable for precise coor162 118 dination, such as in pieces with abrupt tempo changes [13], 163 119 or synchronization after rests and tempo variations [8]. 164 120 The beginning of a musical piece is challenging for coordi165 121 nation due to the absence of preceding audio cues. Bishop 166 122 et al. examined visual cues at piece initiation, finding that 167 123 the peak of the acceleration curve in nodding gestures indi168 124 cated beat positions, while gesture duration and periodicity 169 125 conveyed tempo information [9]. However, they did not in126 vestigate the predictive capability of gesture cues for onset 170 127 timing prediction. 171 

- 128 Most studies on synchronization between gestures and 

172 

musical rhythm have emphasized velocity peaks rather than spatial positions as primary features. Su [14] demonstrated this using minimal laboratory setups with bouncing point-light and auditory stimuli. Similar findings emerged from string quartet studies linking bow speed to tempo cues [11], and conductor studies emphasizing baton velocity and acceleration [15]. Vera et al. further highlighted breath cues’ significance in synchronization, particularly when visual contact is limited [10]. These studies underline the role of gesture and breath cues in synchronization, suggesting velocity, acceleration, and cue length influence timing. However, few studies have simultaneously examined those cues in wind instruments to assess their impact on timing. Our study extends this by quantitatively examining correlations between gestures, breath cues, and onset timings through multimodal analysis of flute-piano duets. 

## 2.2 Gesture Analysis of Performance 

Motion tracking methods utilizing sensors or optical flowbased video tracking [16] are common for gesture analysis. Previous studies by Bishop et al. and Timmers et al. used attachable sensors or markers to measure movement and acceleration [9, 11], whereas Bochen et al. applied audio-visual analysis with optical flow to examine vibrato patterns from string players’ hand movements [17, 18]. Maezawa et al. proposed MuEns, a multimodal scorefollowing system employing optical flow to track gestures for automated piano accompaniment. However, in that particular work, the authors utilized arbitrarily defined gesture cues instead of systematically analyzing how performers naturally encode onset timings [5]. 

## 3. DATASET 

## 3.1 Musical Cue Dataset 

We created a multimodal cue dataset containing video and audio recordings of flute-piano duet performances to analyze musical cues from gestures and breathing sounds. Following previous studies [9,14], we identified peaks in position, velocity, and acceleration curves as potential gesture cue points. Breath cue points were defined by the breath onset and offset timings. We termed the interval between paired cue points as ‘cue length’ and the duration from cue initiation to flute onset as ‘cue-onset length’. 

## 3.1.1 Participants 

A total of 20 professional flutists and 3 pianists participated in the experiment, all holding bachelor’s or master’s 

101 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
Breath Breath Flute Piano 2nd<br>Start Onst st st set Measure<br>ANLU<br>Flute<br>Piano<br><!-- End of picture text -->

Figure 2: Breath Cue and Onset Annotation Breath cue is defined by the breath onset and offset annotated on the mel spectrogram. Six markers are annotated per trial. Detailed information can be found in Section 3.2 

- 173 degrees in performance. Each flutist-pianist pair had not 174 previously performed together. 

## 175 3.1.2 Placement and Equipment 

- 210 

- 176 The setup mimicked a concert stage, with flutists posi211 177 tioned facing away from the pianists. The pianists could 212 178 observe the flutists, while the flutists were instructed to 213 179 give cues without turning or looking at the pianists. A 214 180 camera recorded flutists at 60 fps<sup>2</sup> , and microphones sep215 181 arately captured audio from each instrument at 44.1 kHz. 216 182 A neutral-colored screen behind flutists minimized back217 183 ground interference for accurate facial movement tracking. 218 

- 184 3.1.3 Musical Piece 

- 219 

- 185 This dataset comprises simultaneously starting flute–piano 186 duets. Part 1 included a C major scale and Pachelbel’s 220 187 Canon performed at slow (50 BPM), medium (100 BPM) 221 188 and fast (150 BPM) tempos, each repeated twice as warm222 189 up exercises (12 trials). Part 2 consisted of 18 classical 223 190 pieces simplified for piano and arranged for simultaneous 224 191 starts. Each piece was assigned a specific tempo (50, 100, 225 192 or 150 BPM), and the entire set of 18 pieces was repeated 226 193 three times, resulting in 54 trials. Each duet performed a 227 194 total of 66 trials, resulting in 1,320 trials overall. Sheet 228 195 music and sample audio were provided in advance. 229 

196 3.1.4 Procedure 

230 

197 The recording procedure for each piece included: (1) An 231 198 experimenter’s clap signaling start, followed by a measure 232 199 of clicks matching the given tempo; (2) The flutist giving a 233 200 cue after clicks ended; (3) The duet beginning in response 234 201 to the cue. 235 

236 

## 3.1.5 Post-session Interview 

202 

- 237 

- 203 The interviews collected the insights of the participants 238 

- 204 on cue strategies. Participants reported providing cues ap239 

- 205 proximately one beat (or half or two beats, depending on 240 

- 206 the piece) ahead, using body movements or breath. Some 241 

- 207 participants mentioned that in typical performance situa242 

- 208 tions, they adjust their cue timing based on the accompa209 nying instrument and ensemble context. 



<!-- Start of picture text -->
Max PeakMin Peak Flute Onset<br>-240<br>PoS-200<br>-280<br>Vel<br>0.5<br>Acc 0.0<br>-0.5<br>-1.0<br>25.5 26.0 26.5 27.0 27.5<br>Seconds<br><!-- End of picture text -->

Figure 3: Gesture Cue Example Gesture cue is defined with the maximum(red) and minimum(black) peaks. The interval between these peaks, called ‘cue length’ (x, red line), and the duration between the maximum peak to the flute onset, called ‘cue-onset length’ (y, blue line). 

## 3.2 Annotation and Preprocessing 

Video and audio data synchronization was achieved through an experimenter’s clap at the start. Using the spectrogram viewer in Adobe Audition, we manually annotated six markers per trial on the mel spectrogram (Figure 2): the experimenter’s clap (Start), breath sound onset and offset (Breath Onset, Breath Offset), initial note onsets of flute and piano (Flute Onset, Piano Onset), and the flute’s second measure onset (2nd Measure). 

## 4. METHODS 

## 4.1 Gesture Cue Detection 

## 4.1.1 Motion Detection 

To detect gesture cues from flutists, we used MediaPipe’s face landmark detection<sup>3</sup> [19] to reliably identify face regions, even when partially obscured by the flute. Subsequently, optical flow methods [17,18] were applied to track facial motion. A pilot study indicated optimal face landmark detection accuracy when the face occupied at least 50% of the video frame height; videos were accordingly resized. 

## 4.1.2 Motion Feature Extraction 

We analyzed facial gestures by extracting position, velocity, and acceleration magnitude curves from averaged y- axis optical flow values. Due to quantized pixel positions causing discrete velocity curves, we applied zero-phase filtering<sup>4</sup> to smooth the curve while preserving peak positions. 

## 4.1.3 Motion Peak Picking 

Figure 3 illustrates a typical gesture cue pattern. Within a one-measure window preceding the flute onset (‘cue window’), we identified maximum and minimum peaks on position, velocity, and acceleration curves using the findpeaks<sup>5</sup> algorithm. This approach automatically detected 

- 3 available at: https://developers.google.com/mediapipe 

> 4 scipy.signal.filtfilt 

> 2 Some videos were recorded at 30 fps due to camera overheating 

> 5 scipy.signal.find_peaks 

102 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
Gesture Cue, Position Gesture Cue, Velocity Gesture Cue, Acceleration Breath Cue<br>y=1.53x y=2.28x y=3.05x y=1.78x<br>r=0.62 r=0.64 r=0.72 r=0.78<br>Cue-Onset Length (s)<br>yso=1.56x r=0.40 yso=2.32x r=0.50 yso=3.09x r=0.65 yso=1.83x r=0.60<br>y100=1.56x r=0.23 y1∞0=2.33x r=0.26 y1∞0=3.12x r=0.73 y100=1.77x r=0.68<br>y150=1.43x r=0.37 y150=2.13x r=0.36 y150=2.89x r=0.63 y150=1.68x r=0.77<br>Cue Length (s) Cue Length (s) Cue Length (s)0.6 0.8 Cue Length (s)0.6<br><!-- End of picture text -->

Figure 4: Relationship between Cue Length and Cue-Onset Length for Gesture Position, Velocity, Acceleration, and Breath Cue Black line: overall regression; blue, green, pink: 50, 100, 150 BPM, respectively. Slopes (y = ax) and correlation (r) are shown for each curve. 

243 848 peaks, with 394 manually annotated. Trials without 285 244 clear peak patterns or failed tracking were excluded, re286 245 sulting in 1,242 usable trials out of 1,320. Gesture curves 287 246 from cases where peak tracking failed are also available on 288 247 the accompanying webpage. 289 290 

248 4.2 Breath Cue Detection 

249 To detect breath cues, we annotated breath onset and offset 250 within the same one-measure ‘cue window’ preceding flute 291 251 onset, based on mel spectrograms (Figure 2). Analyses 252 were conducted exclusively on the 1,242 trials that were 292 253 verified to contain valid gesture cues. 293 294 254 4.3 Onset Timing Prediction 295 255 We examined four cues: gesture position, velocity, accel296 256 eration, and breath. To explore the relationship between 297 257 these cues and onset timing, we applied a simple linear 298 258 regression model. Each cue length was set as the inde299 259 pendent variable x, while the cue-onset length (the inter300 260 val from cue start positions—maximum peak or breath on301 261 set—to the actual onset) was the dependent variable y. The 302 262 regression model, without bias, is defined by y=ax, as il303 263 lustrated in Figure 3. The slope a derived from the re304 264 gression indicates the ratio between cue length and onset 305 265 timing, enabling onset prediction. Additionally, we ana306 266 lyzed the trials separately by tempo to assess differences 307 267 in cue-onset relationships, examining both the regression 308 268 slope and Pearson correlation. A high correlation would 309 269 confirm the cue’s validity for predicting onset timing. 310 

311 270 5. RESULTS AND DISCUSSION 312 271 5.1 Patterns in Gesture Curves 313 314 272 The position curve did not consistently show the same 315 273 shape in all trials, but in most cases it remained static ini316 274 tially and then displayed a clear downward-up-down mo317 275 tion pattern that served as a signal (Figure 3). Even when 318 276 the position curve deviated from the typical pattern, an 319 277 up-down motion immediately preceding onset was consis278 tently present (1242 out of 1320 trials, see Section 4.1.3). 320 279 These movements were often periodic and sinusoidal, re321 280 sulting in velocity and acceleration curves that mirrored 322 281 the position curve, but phase-shifted by approximately a 323 282 quarter cycle. Further investigation could examine how 324 283 variations in curve characteristics, such as the degree of si325 284 nusoidal shape and periodicity consistency, influence per326 

formers’ interpretation of cues and their subsequent synchronization accuracy. Moreover, analyzing deviations from typical sinusoidal patterns might uncover additional insights into performer-specific gesture strategies. Due to challenges in quantifying these curve characteristics precisely, this topic remains open for future research. 

## 5.2 Results of the Linear Regression 

Figure 4 illustrates the relationships between cue length and cue-onset length for gesture and breath cues across all participants. Both types of cues showed linear relationships with cue-onset durations. For breath cues, eight outliers were identified due to ambiguous annotations; these were excluded from subsequent regression analyses. Linear regression indicated slopes of 1.53 (gesture position), 2.28 (gesture velocity), 3.05 (gesture acceleration), and 1.78 (breath cue). Interestingly, none of the cues yielded a slope close to 2, suggesting that counting the cue length and subsequent duration as equal units (similar to counting two beats) is not consistently applicable. The velocity and breath cues had slopes closest to 2, but the interval from the velocity cue to onset was slightly longer (1.28 times cue length), while for the breath cue it was slightly shorter (0.78 times cue length). Gesture acceleration showed a strong correlation (0.72) with cue-onset durations, but breath cues exhibited an even stronger correlation (0.78), highlighting their superior reliability for predicting onsets. The higher correlation with velocity and acceleration compared to position aligns with previous studies, suggesting performers primarily perceive velocity or acceleration peaks as cue indicators rather than positional points. However, acceleration peaks closely align with previous position peaks, indicating a potential two-peak encoding pattern in position curves. Precisely quantifying this relationship is challenging and thus remains a topic for future research. 

Additionally, slopes generally decreased slightly with increased tempo, indicating flute onsets occurred sooner than expected based on proportionally shortened cue lengths. Furthermore, correlation coefficients for gesture cues decreased at higher tempos, whereas breath cues exhibited higher correlations at faster tempos, reinforcing the effectiveness of breath cues for synchronization. 

103 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
Flutist Onset (Ground Truth) Predicted Onset (Gesture Pos) Predicted Onset (Gesture Vel) Predicted Onset (Gesture Acc) Predicted Onset (Breath)<br>300 Mean: 17ms Mean: 24ms Mean: 27ms Mean: 47ms Mean: 17ms<br>Abs Mean; 79m Abs Mean: 121ms Abs Mean: 144 Abs Men: 168ms Abs Mean: 109ms<br>200 STD: 168ms STD: 200ms STD: 220ms STD: 247ms STD: 209ms<br>Count<br>100<br>-0.5 0.0 0.5 -0.5 0.0 0.5 -0.5 0.0 0.5 -0.5 0.0 0.5 -0.5 0.0 0.5<br>Piano Flute Piano Predicted Onset Piano Predicted Onset Piano Predicted Onset Piano Predicted Onset<br>Eany Early Early Early Eany Eany Early Early Early Early<br>Asynchrony (s)<br>Figure 5: Histogram of Note Onset Asynchrony Onset time differences between the pianist’s onset and 1. Flutist onset<br>(Ground truth) 2-4. Predicted onset from gesture position, velocity, acceleration cue 5. Predicted onset from breath cue.<br>ID Group Gesture Onset Breath Onset Async Abs STD Asynchrony by Session Repetitions<br>Clarity Timing Clarity Timing Async  Absolute Mean<br>late 4.5 3.3 3.9 3.4 71 71 39 0.10<br>A good 4.0 3.6 4.8 3.0 54 54 31 0.09<br>fast 3.8 2.4 4.4 2.6 -54 125 66<br>late 4.4 3.1 3.9 3.1 71 71 39 0.08<br>B good 3.1 3.4 3.3 3.4 54 54 31<br>fast 3.9 3.9 4.5 3.9 -54 125 66 0.07<br>Mean asynchrony (sec) S1 (12 pieces) T1 (18 pieces)SessionT2 (18 pieces) T3 (18 pieces)<br><!-- End of picture text -->

Table 1: Result of the Expert Evaluation Expert ratings of cue clarity and execution timing (1 = late, 3 = on-time, 5 = early) on a 5-point scale, with asynchrony metrics (ms) indicating average group asynchrony. 

Figure 6: Human onset asynchrony across session repetition. 

As described in Section 3.1.3, we observed asynchrony changes through an initial warm-up session of 12 trials (S1) and three repeated sets of 18 pieces (T1–T3), illustrated in Figure 6. Asynchrony notably decreased from the initial warm-up session (S1) through the second repetition session (T2) but stabilized thereafter. We interpret this as indicating adaptation effects, where performers quickly improved synchronization by familiarizing themselves with each other’s cues. However, ongoing piece variation and unresolved consensus about triggers (Section 5.4) likely prevented further reduction in asynchrony beyond a certain threshold. 

indicating average group asynchrony. 363 364 327 5.3 Note Onset Asynchrony 365 328 5.3.1 Asynchrony Comparision 366 329 Figure 5 shows histograms of time differences between 367 330 the pianist’s onset and five conditions: actual flutist onset 368 331 (gray) and four predicted onsets from the linear regression 369 332 model (Section 5.2). This error represents the discrepancy 370 333 expected if the flutist perfectly followed our linear model 371 334 and executed the cues precisely. A notable feature in the 372 335 pianist-flutist asynchrony histogram is the minimal occur373 336 rence of trials just before zero milliseconds. This sug374 337 gests a tendency for the leader (flutist) to start slightly ear375 338 lier than the follower (pianist), aligning with observations 339 confirmed by expert interviews (Section 5.5.2). Addition376 340 ally, we consider auditory reaction (performers starting in 377 341 response to hearing the partner’s onset) unlikely in most 378 342 cases, as the observed asynchronies are typically smaller 379 343 than the average auditory reaction time (150 ms) [20]. 380 344 The ‘Pianist-Flutist asynchrony’ had the narrowest 381 345 spread (Absolute(Abs) mean = 79ms, Standard Deviation 382 346 (STD) = 168ms), consistent with previous research re383 347 porting the first onset asynchronies slightly above 80ms 384 348 [9]. Gesture-based predictions showed absolute mean er385 349 rors between 121–168ms, with acceleration predictions ex386 350 hibiting higher variability (STD = 247ms). Breath pre387 351 dictions were more consistent (Abs mean = 109 ms, STD 388 352 = 209 ms). Although the acceleration cue demonstrated 389 353 the highest Pearson correlation, its greater variability and 390 354 longer cue length contributed to larger errors. These find391 355 ings suggest that while cue-based linear predictions are 392 356 slightly less precise than human synchronization, breath 393 357 cues provide more reliable predictions than gesture-based 394 358 cues. The precision of predictions compared with actual 395 359 flutist onsets exhibited similar patterns. 396 397 360 5.3.2 Reduction of Asynchrony Through Repetition 398 361 We also investigated whether synchronization accuracy 399 362 improves as pianists and flutists adapt to each other’s cues. 400 

## 5.4 Triggers 

Despite the considerable accuracy of linear predictions (Section 5.2), questions remained regarding precise cue recognition, particularly for velocity and acceleration peaks. Given potential perception errors in identifying cue points, we investigated additional factors musicians might use to ensure precise synchronization. We observed characteristic gesture patterns immediately following cue movements near onset timings. After the downwardupward-downward cue motion, flutists typically executed one of three distinct trigger patterns (Figure 7): (A) initiating onset just before raising the head again, typically aligned with the previous upward cue movement, (B) briefly pausing with the head lowered and starting immediately afterward, or (C) ambiguously initiating onset while slowly raising the head. Patterns (A) and (B) provided clear, immediate signals suitable as precise triggers. Pattern (C), however, represented ambiguous or absent triggers. Without prior agreement, these ambiguous gestures could cause confusion—for example, a flutist intending pattern (A) might be misinterpreted by the pianist as pattern (B), resulting in significant timing discrepancies. Such cases were indeed observed, and the validity of these trigger patterns was further confirmed through expert interviews (Section 5.5). Thus, we propose that musicians initially encode approximate timing through cues and then 

104 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

Trigger ACue Onset Trigger BCue Onset Trigger CCue Onset 444 Pos 445 446 Vel 447 448 Acc 449 450 Seconds Figure 7: Examples of three trigger types (A, B, C) 451 Green dashed lines indicate breath onset and offset, the 452 blue line marks flute onset, and the red line piano onset. 453 The red shaded area represents the cue interval. 454 455 401 achieve precise synchronization through clearly defined 456 402 trigger gestures. 457 458 403 5.5 Expert Evaluation and Interview 459 404 After the main analysis, we conducted a two-hour inter460 405 view with two expert flutists, each with over 20 years of 461 406 ensemble and teaching experience. The session involved 462 407 two main tasks: evaluating trials categorized as fast, good, 463 408 or late based on onset predictions from velocity cues, and 464 409 assessing our trigger hypothesis. Due to time constraints, 465 410 only velocity cues were used, as they offered the most in466 411 terpretable and perceptually reliable basis for cue classifi467 412 cation. 468 413 5.5.1 Evaluation of Linear Model Predictions 469 

## 5.5.1 Evaluation of Linear Model Predictions 

413 

470 414 Experts reviewed 8 trials from each group (fast, good, late) 471 415 to evaluate the clarity of the cues (accuracy) and whether 472 416 the actual onset timing matched the timing implied by the 473 417 cue (execution timing). The experts evaluated 24 randomly 474 418 ordered trials without being informed of the group labels. 475 419 After agreeing with the assumption that head-nodding ges476 420 tures and breathing serve as cues, experts rated cue accu477 421 racy on a scale from 1 (no recognizable cue) to 5 (clearly 478 422 recognizable cue) and execution timing from 1 (very late) 479 423 to 5 (very early), with 3 representing precise timing. Re480 424 sults are summarized in Table 1. 

425 Surprisingly, the experts differed notably in their eval481 426 uations of breath cue execution timing, which also did not 482 427 align clearly with actual pianist-flutist asynchrony. Expert 483 428 A rated the ‘good’ group’s gesture cues as slightly late but 484 429 breath cues as most accurate. Expert B rated the groups in 485 430 descending order (late-good-fast) of perceived lateness but 486 431 still considered the ‘late’ group relatively early (average 487 432 3.1). Actual asynchrony partly aligned with our predic488 433 tions; the ‘good’ group exhibited the smallest asynchrony, 489 434 consistent with the cue hypothesis. However, unexpected 490 435 discrepancies emerged, such as the ‘fast’ group showed 491 436 later flute onsets than the piano. These inconsistencies 492 437 likely reflect individual variations in interpreting and ex493 438 ecuting cues. 494 495 

## 5.5.2 In-depth Interview 

439 

496 

440 After the video evaluation, we conducted detailed discus497 441 sions about the linear prediction model and the trigger 498 442 concept. Experts acknowledged the general practice of 499 443 cueing approximately one beat ahead, noting that specific 500 

movements were intuitively executed rather than explicitly planned. Both emphasized tempo-related influences on gesture and breath cues, highlighting gesture periodicity as crucial for clear cue delivery. 

Regarding triggers, experts initially did not consciously recognize different trigger types but agreed with the proposed classifications after reviewing examples. Both agreed type (A) was optimal, while type (B) was considered challenging due to the flute’s physical constraints. Opinions on type (C) diverged: Expert A considered it inherently prone to higher errors, whereas Expert B believed it could be viable when accompanied by precise breath cues and rehearsal. Experts noted that triggers may vary depending on musical context (phrasing, emphasis). They also observed potential triggers, including the flute’s endpoint position, lip shape, and finger movements. Finally, both proposed that in flute-piano duets, slight delays in piano onset might cognitively benefit synchronization, potentially explaining the scarcity of trials where piano onset preceded flute onset, as observed in Figure 5. 

## 5.6 Limitation 

Although this study contributes to understanding cuebased synchronization, several limitations remain. First, our trigger analysis was not fully quantitative; future research should develop precise methods for defining triggers from gesture curves and consider additional signals such as lip shape, finger movements, and horizontal flute actions. Second, The decision-making process for selecting triggers was not investigated. Exploring how musicians choose and agree on triggers could further clarify synchronization strategies. Additionally, individual variability in cue and trigger preferences was not quantitatively examined; future research could explore personalized synchronization strategies. Lastly, our findings apply specifically to flute-piano duets and piece initiation. Generalizing these methods to other instrument combinations and ongoing musical contexts remains necessary. 

## 6. CONCLUSION 

This study investigated how gesture and breath cues used by flutists in flute-piano duets encode note onset timing at the initiation of musical pieces. To quantitatively analyze cues, we collected a cue dataset, identifying cue points via motion tracking and breath sounds. Our multimodal analysis revealed linear relationships between cue lengths and onset timings, confirming that gesture and breath cues reliably predict onset timing. In addition, we introduced the concept of triggers, defined as immediate gestures that indicate precise onset moments, which we validated through expert interviews. Future research could further develop the analysis of triggers to achieve a more systematic understanding. Additionally, developing regression models that jointly use gesture and breath cues, or exploring sophisticated predictive models, would be valuable. It could further extend our cue analysis methods to other instruments, ensemble configurations, and within-performance synchronization, providing deeper insights into the complexity of ensemble coordination. 

105 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 7. ETHICS STATEMENT 

- [9] ——, “Beating time: How ensemble musicians’ cueing gestures communicate beat position and tempo,” Psychology of Music, vol. 46, no. 1, pp. 84–106, 2018. 

549 

501 

550 502 This study was approved by the Institutional Review Board 551 503 (IRB), and all participants consented to video recording 504 and data sharing. Each flutist’s session lasted 1.5 hours, 552 505 pianists had 30-minute breaks between sessions, with up 553 506 to four sessions per day. Participants received appropri554 507 ate compensation. To protect privacy, the video data will 555 508 remain confidential. 

- [10] B. Vera, E. Chew, and P. G. Healey, “A study of ensemble synchronisation under restricted line of sight.” in International Society for Music Information Retrieval Conference (ISMIR), 2013, pp. 293–298. 

- [11] R. Timmers, S. Endo, A. Bradbury, and A. M. Wing, “Synchronization and leadership in string quartet performance: a case study of auditory and visual cues,” Frontiers in Psychology, vol. 5, p. 645, 2014. 

556 

557 509 8. ACKNOWLEDGMENTS 558 559 510 This work has been supported by the National Research 511 Foundation of Korea (NRF) grant funded by the Korea 560 512 government (MSIT) under Grant RS-2023-NR077289 and 561 513 Grant RS-2024-00358448. 562 563 564 

- [12] B. Li, X. Liu, K. Dinesh, Z. Duan, and G. Sharma, “Creating a multitrack classical music performance dataset for multimodal music analysis: Challenges, insights, and applications,” IEEE Transactions on Multimedia, vol. 21, no. 2, pp. 522–535, 2018. 

## 9. REFERENCES 

514 

- [13] S. Kawase, “Gazing behavior and coordination during piano duo performance,” Attention, Perception, & Psychophysics, vol. 76, pp. 527–540, 2014. 

565 566 567 

- 515 [1] C.-J. Tsay, “Sight over sound in the judgment of music 516 performance,” Proceedings of the National Academy of 517 Sciences, vol. 110, no. 36, pp. 14 580–14 585, 2013. 

   - [14] Y.-H. Su, “Audiovisual beat induction in complex auditory rhythms: Point-light figure movement as an effective visual beat,” Acta Psychologica, vol. 151, pp. 40–50, 2014. 

- 568 

- 518 [2] L. Bishop, C. Cancino-Chacón, and W. Goebl, “Mov569 

- 519 ing to communicate, moving to interact: Patterns of 570 

- 520 body motion in musical duo performance,” Music Per571 

- 521 ception: An Interdisciplinary Journal, vol. 37, no. 1, 522 pp. 1–25, 2019. 572 573 

- 523 [3] F. K. Hukporti, Your Guide to Basic Conducting. Ac574 524 cra: Noyam Publishers, 2023. 575 

- 525 [4] R. Page-Shipp, D. Joseph, and C. van Niekerk, “Con576 526 ductorless singing group: a particular kind of self577 527 managed team?” Team Performance Management: An 578 

- 528 International Journal, vol. 24, no. 5/6, pp. 331–346, 579 

- 529 2018. 

      - [15] G. Luck and J. A. Sloboda, “Spatio-temporal cues for visually mediated synchronization,” Music Perception, vol. 26, no. 5, pp. 465–473, 2009. 

   - 575 [16] B. K. Horn and B. G. Schunck, “Determining optical 576 flow,” Artificial intelligence, vol. 17, no. 1-3, pp. 185– 577 203, 1981. 578 [17] B. Li, K. Dinesh, Z. Duan, and G. Sharma, “See 579 and listen: Score-informed association of sound tracks 580 to players in chamber music performance videos,” 581 in 2017 IEEE International Conference on Acoustics, 582 Speech and Signal Processing (ICASSP), 2017, pp. 583 2906–2910. 

- 530 [5] A. Maezawa and K. Yamamoto, “MuEns: A multi531 modal human-machine music ensemble for live concert 532 performance,” in Proceedings of the 2017 CHI Confer533 ence on Human Factors in Computing Systems, 2017, 534 pp. 4290–4301. 

      - [18] B. Li, C. Xu, and Z. Duan, “Audiovisual source association for string ensembles through multi-modal vibrato analysis,” Proc. Sound and Music Computing (SMC), pp. 159–166, 2017. 

   - 584 585 586 

- 535 [6] X. Gao, A. Rogel, R. Sankaranarayanan, B. Dowling, 536 and G. Weinberg, “Music, body, and machine: gesture537 based synchronization in human-robot musical interac538 tion,” Frontiers in Robotics and AI, vol. 11, 2024. 

587 

   - 588 [19] V. Bazarevsky, I. Grishchenko, K. Raveendran, T. Zhu, 589 F. Zhang, and M. Grundmann, “Blazepose: On590 device real-time body pose tracking,” arXiv preprint 591 arXiv:2006.10204, 2020., 2020. 

- 539 [7] A. Lim, T. Mizumoto, L.-K. Cahier, T. Otsuka, T. Taka591 arXiv:2006.10204, 2020., 2020. 

- 540 hashi, K. Komatani, T. Ogata, and H. G. Okuno, 541 “Robot musical accompaniment: integrating audio and 592 [20] R. J. Kosinski, “A literature review on reaction time,” 542 visual cues for real-time synchronization with a human 593 Clemson University, vol. 10, no. 1, pp. 337–344, 2008. 543 flutist,” in 2010 IEEE/RSJ International Conference on 544 Intelligent Robots and Systems, 2010, pp. 1964–1969. 

- 545 [8] L. Bishop and W. Goebl, “When they listen and when 546 they watch: Pianists’ use of nonverbal audio and vi547 sual cues during duet performance,” Musicae Scien548 tiae, vol. 19, no. 1, pp. 84–110, 2015. 

106 

