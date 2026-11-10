---
paper_id: "000078"
year: 2021
title: "A Differentiable Cost Measure for Intonation Processing in Polyphonic Music 626-633"
source_url: "https://archives.ismir.net/ismir2021/paper/000078.pdf"
---

# **A DIFFERENTIABLE COST MEASURE FOR INTONATION PROCESSING IN POLYPHONIC MUSIC** 

## **Simon Schwär** 

## **Sebastian Rosenzweig Meinard Müller** 

## International Audio Laboratories Erlangen, Germany 

simon.schwaer@fau.de, {sebastian.rosenzweig, meinard.mueller}@audiolabs-erlangen.de 

### **ABSTRACT** 

Intonation is the process of choosing an appropriate pitch for a given note in a musical performance. Particularly in polyphonic singing, where all musicians can continuously adapt their pitch, this leads to complex interactions. To achieve an overall balanced sound, the musicians dynamically adjust their intonation considering musical, perceptual, and acoustical aspects. When adapting the intonation in a recorded performance, a sound engineer may have to individually fine-tune the pitches of all voices to account for these aspects in a similar way. In this paper, we formulate intonation adaptation as a cost minimization problem. As our main contribution, we introduce a differentiable cost measure by adapting and combining existing principles for measuring intonation. In particular, our measure consists of two terms, representing a tonal aspect (the proximity to a tonal grid) and a harmonic aspect (the perceptual dissonance between salient frequencies). We show that, combining these two aspects, our measure can be used to flexibly account for different artistic intents while allowing for robust and joint processing of multiple voices in real-time. In an experiment, we demonstrate the potential of our approach for the task of intonation adaptation of amateur choral music using recordings from a publicly available multitrack dataset. 



<!-- Start of picture text -->
00 b<br>□ 回 00 (a)<br>B bB<br>7000<br>6500<br>(b)<br>6000<br>pitch (cents)<br>5500<br>C (c)<br>(d)<br>pitch shift (cents)<br>musical time (bars)<br><!-- End of picture text -->

**Figure 1** : Joint adaptation of the voices in an example cadence. **(a)** Sheet music. **(b)** Fundamental frequencies of the original synthesized voices measured with pYIN [1] (orange: soprano, red: alto, green: tenor, blue: bass). **(c)** Overall intonation cost _C_ between all voices with _w_ = 0 _._ 33. **(d)** Pitch shift curve for all voices obtained from joint gradient descent on _C_ with _w_ = 0 _._ 33 and _µ_ = 350. 

### **1. INTRODUCTION** 

The widely-used 12-tone equal temperament (12-TET) tuning system divides the octave in twelve equal semitones of the ratio 2<sup>1</sup><sup>_/_12</sup> _≈_ 1 _._ 0595. This allows instruments with fixed pitch to play in any key at the cost of most intervals being slightly out of tune in comparison to the natural overtone spectrum of harmonic sounds. Just Intonation (JI) scales, on the other hand, are constructed from intervals with small integer ratios to a root note. As a result, the harmonic overtones of two tones in a JI scale are more congruent than those in 12-TET. However, the absolute pitches in the JI scale change for different root notes, so that the grid must be adapted to different keys and musical contexts. 

_⃝_ c S. Schwär, S. Rosenzweig, and M. Müller. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). **Attribution:** S. Schwär, S. Rosenzweig, and M. Müller, “A Differentiable Cost Measure for Intonation Processing in Polyphonic Music”, in _Proc. of the 22nd Int. Society for Music Information Retrieval Conf.,_ Online, 2021. 

Many instruments can produce any pitch in between the 12-TET or JI grid or have considerable variance in tuning. This allows performers to dynamically change the sounding scale or chord, both intentionally and accidentally. This flexible intonation is particularly relevant in a cappella choral singing. While 12-TET if often used as an approximation for the distribution of chosen pitches by singers [2,3], their intonation is influenced by a multitude of aspects. For example, choir singers tend to aim for JI in harmonies [4], whereas other influences may prevail in melodic or solistic phrases [5]. At the same time, singers continuously have to account for the intonation of their fellow musicians [6,7], while pitch changes also occur during the sounding tone [8]. Depending on the singers’ ability to control their voices, this complex setting often results in defects like poor local intonation or intonation drift [9,10]. 

Different aspects of intonation are illustrated in the synthesized example cadence shown in Figure 1: The pitches 

626 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

(where “pitch” is used as a technical term synonymously with fundamental frequency here and in the following) in chord I correspond to a JI scale with root F, while chord II is tuned to 12-TET. Continuous deviations are illustrated in chords III and IV, where the soprano in III and all voices in IV are detuned randomly between _−_ 25 and +25 cents around the 12-TET grid. Even with these large pitch fluctuations, the chords can still be clearly recognized<sup>1</sup> . 

When post-processing multitrack recordings, pitchshifting the individual audio signals may mitigate some unintended intonation deviations in a performance. However, this requires a known target pitch, and similarly to intonation in a live performance, the desired target can be influenced by many aspects. Instead of quantizing to a fixed set of pitches like 12-TET or manually tweaking individual notes, we formulate intonation adaptation as a cost minimization problem. A good cost measure for this task should have a local minimum at the target pitch for each individual note. 

As our main contribution, we propose a differentiable cost measure, where the local minima can be adjusted according to artistic intent. In particular, we employ two existing models to account for different aspects of intonation: The first model represents a _tonal_ aspect, that most music is composed from a set of discrete pitches approximated by equal divisions of the octave [11]. The second model considers a _harmonic_ aspect and uses perceptual dissonance to capture the tendency for JI in multi-part harmonies [12]. 

We show that our cost-based approach has several advantageous properties over existing methods for intonation processing: 

- A variable weight between the terms allows for flexibly setting the local minimum anywhere between 12-TET and JI. 

- In contrast to purely dissonance-based adaptation, our cost measure has a local minimum also for musically unstable voices of a chord. 

- Using gradient descent, intonation can be adapted in real-time, dynamically reacting to changing inputs. 

For example, the overall cost shown in Figure 1c is high when voices deviate strongly from the desired pitches. At the same time, musically dissonant chords like the diminished seventh chord in III have a higher inherent perceptual dissonance. Therefore, an adaptation should not aim to achieve zero cost, but to find the nearest local minimum. 

Figure 1d shows the pitch shift curves for the voices in our example that locally minimize the cost measure. The curves were obtained using joint gradient descent, where all voices are processed at the same time and influence each other. The resulting “optimal” pitches after applying the shift lie in between 12-TET and JI, as can be seen e. g. in the major third of chord I. Its initial pitch in the present example is _−_ 14 cents w.r.t. 12-TET and it is pitched up by 10 cents to minimize the cost with the given parameters. Furthermore, the algorithm finds meaningful solutions in 

> 1 Audio examples are available online: https://www.audiolabs-erlangen.de/resources/MIR/ 2021-ISMIR-IntonationCostMeasure. 

the more complex situations occuring in chords III and IV. 

The remainder of this article is structured as follows. In Section 2, we review existing approaches to intonation adaptation and adaptive tuning, in Section 3 we introduce the cost measure, and in Section 4, we demonstrate the applicability to local intonation adaptation in a multitrack choral music recording with amateur singers. 

### **2. RELATED WORK** 

A common intonation adaptation strategy implemented in many commercial products like _Melodyne_ [13] or _AutoTune_ [14] is to measure the fundamental frequency (F0) in a monophonic recording and to pitch-shift the signal such that the F0 approaches a fixed target value. The target can be chosen manually by the user or determined automatically from a predefined grid or score. 

Several approaches have been proposed to dynamically choose a target pitch based on musical assumptions. Rulebased algorithms like _Groven.Max_ [15] or _Hermode Tuning_ [16] choose pitches for all voices of a synthesizer by analyzing the musical structure of a chord. Aiming for JI, they implement fixed rules to compromise in chords where just intervals between all pairs of notes are not possible. This problem can also be addressed by solving a quadratic program [17]. This way, the deviation from JI is distributed evenly across the pitches and all intervals are as close as possible to a small integer ratio. Additional constraints can enable temporal continuity. 

Deep learning is used in [18] to infer “good” intonation from curated training examples of monophonic vocal recordings over a backing track. The model then outputs a pitch shift curve that can match the intonation in an input recording with the characteristics of the training examples. 

Sethares [19] relates the chosen scale to the timbre of the sound. Summing the perceptual dissonance [20] of all individual salient frequency pairs between two sounds, he obtains a _dissonance landscape_ , in which local minima exist for small integer ratio intervals if the timbre is harmonic. This principle is also used for adaptive tuning using gradient descent [12], which achieves a tuning similar to JI without requiring explicit musical analysis of the chords. In [21], the idea was further enhanced to be stable in more complex settings by adding a proximity constraint. This limits the deviation from 12-TET to a few cents and requires the input to be in the same range. 

### **3. INTONATION COST MEASURE** 

Our cost measure is based on the assumption that proper intonation in a polyphonic context is a balance between the proximity to pitches in an equal temperament tuning system most suitable for the composition and the minimization of perceptual dissonance. Mathematically, this can be expressed as the sum of a _tonal_ cost _C_ t, indicating the distance to the pitches in an equal temperament tuning system, and a _harmonic_ cost _C_ h, measuring the perceptual dissonance in the overall sound: 



<!-- Start of picture text -->
C :=  w · C t + (1  − w )  · C h . (1)<br><!-- End of picture text -->

627 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 



<!-- Start of picture text -->
(a)<br>to f3<br>(b)<br>f0 f3f4<br>w = 0.1<br>w= 0.4<br>C<br>w= 0.7 (c)<br>-200 -100 0 100 200<br>shift x (cents)<br><!-- End of picture text -->

**Figure 2** : Conceptual overview of our cost measure. **(a)** _C_ t is higher when salient frequencies are far from the equal temperament grid. **(b)** _C_ h is higher when salient frequencies of a tone (blue) are similar but not equal to salient frequencies of a concurrent reference tone (red). **(c)** Shifting the tone shown in blue by _x_ cents changes the overall cost _C_ . A higher relative weight _w_ of _C_ t to _C_ h results in local minima closer to the 12-TET grid. 

A lower cost _C_ corresponds to a “better” choice for the pitch, where the parameter _w ∈_ [0 _,_ 1] controls the relative weight between the two aspects. 

Figure 2 exemplifies the behavior of _C_ for two hypothetical tones with five harmonic partials each (depicted in blue and red). The graphs in Figure 2c show the change in _C_ when the tone represented in blue is pitch-shifted by _−_ 200 to +200 cents. As the two tones form a major third, a shift by +14 cents would result in a just interval. With a larger _w_ , the relative weight of _C_ t increases, corresponding to a preference for equal temperament, whereas with decreasing _w_ , the local minima move closer to JI intervals. 

In the upcoming section, we develop differentiable expressions for _C_ t and _C_ h and illustrate their properties by continuing our example from Figure 1. In Section 3.4, we then show how the cost measure can be used to adapt the intonation using gradient descent. 

### **3.1 Prerequisites** 

For a given audio signal, we assume a stationary sound in each analysis time frame _n_ and represent it by a set 



<!-- Start of picture text -->
P [ n ] :=  { ( fm, am )  | m ∈{ 1 , ..., M }}, (2)<br><!-- End of picture text -->

consisting of _M_ salient frequencies _fm_ in Hz with amplitude _am_ . The cost measure is defined for a signal w.r.t. to a reference (or “background”) signal represented by a set _P_ ref [ _n_ ]. In the following, we omit the frame index for _P_ and _P_ ref where the time-dependency is not relevant. 

To obtain this representation from audio signals, we use a short-time Fourier transform (STFT) with a frame and 

hop size of 0 _._ 1 sec and detect peaks in the magnitude spectrum of each time frame that constitute the salient frequencies. Avoiding the misinterpretation of transient peaks in the spectrum, we filter the STFT representation to remove percussive components of the signal [22]. Then, we identify up to 16 peaks in the remaining spectrum of each time frame by selecting the local maxima above a threshold. To increase frequency resolution, we interpolate the exact peak frequency and amplitude by fitting a parabola to the magnitudes of neighboring bands [23]. For an inactive voice or a purely percussive signal frame, we set _P_ = _∅_ . 

Note that, for harmonic sounds in a monophonic signal, all salient frequencies in _P_ are close to integer multiples of the lowest frequency _f_ 0. This assumption does not hold for inharmonic sounds and polyphonic recordings. 

For the example in Figure 1, we synthesize the signals using a sawtooth waveform with 16 harmonic partials and amplitudes _ai_ = 1 _/_ ( _iπ_ ) using a reference frequency of 440 Hz for A4. 

### **3.2 Tonal Cost** 

Equal divisions of the octave are a good approximation for the distribution of pitches in many music theories [11]. Furthermore, measuring the distance to an equal temperament grid is an often used strategy to assess the intonation in a performance [3,24]. 

We define the tonal distance _d_<sup>_K_</sup> t<sup>(</sup><sup>_f_1</sup><sup>_, f_2)betweentwo</sup> positive frequencies _f_ 1 and _f_ 2 in Hz on a K-TET grid as 



<!-- Start of picture text -->
d K t ( f 1 , f 2) := 1 , (3)<br>2 1  − cos 2 πK  log2( f 1 /f 2 )) )<br><!-- End of picture text -->

where the distance is small if the interval between _f_ 1 and _f_ 2 is close to a K-TET interval (i. e., _f_ 1 _/f_ 2 _≈_ 2<sup>_k/K_</sup> with _k ∈_ Z). By measuring the tonal distance of each frequency in _P_ to a given reference frequency _f_ ref , we define the tonal cost _C_ t as 



<!-- Start of picture text -->
∑ ( f,a ) ∈P a · d t K ( f, f ref )<br>C t := , (4)<br>∑ ( f,a ) ∈P a<br><!-- End of picture text -->

where frequencies with higher amplitude contribute more to _C_ t. The highest cost _C_ t = 1 is reached, when all salient frequencies lie exactly in the middle between two frequencies on the equal temperament grid defined by _K_ and _f_ ref . The parameters _K_ and _f_ ref can either be estimated from _P_ ref or fixed to known values. Note that, with fixed parameters, _C_ t does not depend on _P_ ref . Furthermore, Figure 2a shows that for integer-multiple frequencies in _P_ , not all frequencies can align with the grid, so that _C_ t is never 0 for such signals. However, the local minimum is reached when the loudest partials are close to the grid. 

For the example, let _P_ include the salient frequencies of the soprano voice while all other voices are contained in _P_ ref . By setting _K_ = 12 and _f_ ref = 440 Hz, we obtain the cost heatmap shown in Figure 3. By pitch-shifting the soprano signal by _−_ 200 to 200 cents and evaluating the cost for each time frame, it shows for which shifts the salient frequencies in the signal fit best on the 12-TET grid. Tracking the nearest local minimum starting at a shift of 0 

628 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 



<!-- Start of picture text -->
200<br>100<br>cost<br>-100<br>pitch shift (cents)<br>-200<br>2<br>musical time (bars)<br><!-- End of picture text -->

**Figure 3** : Tonal cost heatmap for the soprano voice in the example from Figure 1, pitch-shifted by _−_ 200 to +200 cents. White line indicates local minimum closest to 0. 

cents, the white line corresponds to the pitch shift required to minimize the cost. 

### **3.3 Harmonic Cost** 

The perceptual dissonance between concurrent sounds can be expressed in terms of the _pure-tone_ dissonance between all combinations of salient frequencies present in each sound [19]. While the perceived dissonance between two pure tones was first determined experimentally [20], we quantify the dissonance between two positive frequencies _f_ 1 and _f_ 2 using the parametrized model from [11] (omitting a global scaling factor): 



<!-- Start of picture text -->
d h( f 1 , f 2) := exp − ln 2 |  log2( f 1 /f 2) | ) ) , (5)<br>w c<br><!-- End of picture text -->

with _w_ c := 6 _._ 7 _·_ min( _f_ 1 _, f_ 2)<sup>_−_0</sup><sup>_._68</sup> as the frequencydependent parameter that controls the interval of maximal dissonance and the decay of the dissonance curve. To ensure differentiability, we define _d_ h( _f_ 1 _, f_ 2) := 0 for _f_ 1 = _f_ 2.<sup>2</sup> As illustrated in Figure 5, _d_ h( _f_ 1 _, f_ 2) approaches 0 from both sides when _f_ 1 is close to _f_ 2. _d_ h( _f_ 1 _, f_ 2) = 1 is maximal when the logarithmic distance between the two frequencies is _|_ log2( _f_ 1 _/f_ 2) _|_ = _w_ c. 

The sum of _d_ h( _f_ 1 _, f_ 2) between all pairs of salient frequencies in _P_ and _P_ ref weighted by the amplitude constitutes the harmonic cost: 



<!-- Start of picture text -->
∑ ∑ min( a, a r)  · d h( f, f r)<br>( f,a ) ∈P ( f r ,a r) ∈P ref<br>C h := (6)<br>a<br>∑<br>( f,a ) ∈P<br><!-- End of picture text -->

The normalization does not restrict _C_ h to [0 _,_ 1], because the total number of salient frequency pairings is _|P|·|P_ ref _|_ , but when comparing harmonic signals, only a small fraction of pairings have _d_ h( _f_ 1 _, f_ 2) _≫_ 0. By normalizing by the sum of amplitudes in _P_ , we achieve a comparable range for _C_ t and _C_ h, where _C_ h vanishes when the amplitudes in _P_ ref are very small (i. e. no reference signal is present for which a harmonic relation can be evaluated). 

The concept of the harmonic cost is illustrated in Figure 2b, where only the pairings between sets (blue and red) contribute to the cost. With the frequency-dependent _w_ c, 

> 2 Proof of differentiability can be found on the accompanying website. 



<!-- Start of picture text -->
200<br>100<br>cost<br>-100<br>pitch shift (cents)<br>-200<br>musical time (bars)<br><!-- End of picture text -->

**Figure 4** : Harmonic cost heatmap for the soprano voice in the example from Figure 1, pitch-shifted by _−_ 200 to +200 cents. White line indicates local minimum closest to 0. 



<!-- Start of picture text -->
1.0<br>0.5<br>dissonance<br>0.0 {|1og2(f1/f2)| = wc<br>110 220 330 440<br>frequency f{2 (Hz)<br><!-- End of picture text -->

**Figure 5** : Pure-tone dissonance _d_ h( _f_ 1 _, f_ 2) from [11] with _f_ 1 = 220 Hz and _f_ 2 between 110 and 440 Hz. 

the dissonance curve becomes more narrow towards higher frequencies. Applied to the soprano in our example analogous to Figure 3, this results in the heatmap in Figure 4. 

### **3.4 Joint Intonation Adaptation** 

In a musical performance, the cost _C_ may vary between time frames _n_ and we denote the cost in each frame by _C_ [ _n_ ]. The goal of intonation adaptation is to obtain a pitch shift function _p_ : Z _→_ R, where a pitch shift of _p_ [ _n_ ] cents applied to the considered signal minimizes _C_ [ _n_ ]. 

When multiple voices can be adapted simultaneously in a polyphonic multitrack setting, the cost for each individual voice depends on the salient frequencies in the other voices. We denote the cost for each voice _v_ with respect to all other voices by _Cv_ [ _n_ ] and the current pitch shift for the signal of _v_ by _pv_ [ _n_ ]. Then the optimal shift can be found by solving 



<!-- Start of picture text -->
min Cv [ n ] . (7)<br>pv [ n ]<br><!-- End of picture text -->

As described in [12], gradient descent is an effective method to find the local minimum. Pitch-shifting with _pv_ [ _n_ ] affects the salient frequencies in _P_ [ _n_ ] equally on a logarithmic scale while the frequencies in _P_ ref [ _n_ ] stay constant. Thus, the shift _p_ in cents can be moved out of the logarithm in the tonal distance _d_<sup>_K_</sup> t<sup>(</sup><sup>_f_1</sup><sup>_, f_2)andthedisso-</sup> nance _d_ h( _f_ 1 _, f_ 2), for which we introduce auxiliary functions _δ_ t<sup>_K_(</sup><sup>_f_1</sup><sup>_, f_2</sup><sup>_, p_) and</sup><sup>_δ_h(</sup><sup>_f_1</sup><sup>_, f_2</sup><sup>_, p_):</sup> 



<!-- Start of picture text -->
δ t K ( f 1 , f 2 , p ) := 1 2 1  − cos 2 πK (log2( f 1 /f 2) +  p/ 1200) ))<br>δ h( f 1 , f 2 , p ) := exp − ln 2 |  log2( f 1 /f w 2) c  + p/ 1200 | ) )<br>(8)<br><!-- End of picture text -->

In the following, we omit the arguments of the distance and dissonance functions for brevity. Analogous to (5), 

629 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 



<!-- Start of picture text -->
(a)<br>(b)<br>pitch shift (cents)20 20 20 20<br>0 (c)<br>-20<br>2<br>musical time (bars)<br><!-- End of picture text -->

**Figure 6** : Adaptation curves _pv_ [ _n_ ] resulting from joint gradient descent with all four voices (orange: soprano, red: alto, green: tenor, blue: bass, _µ_ = 350). **(a)** _w_ = 1 _._ 0 **(b)** _w_ = 0 _._ 0 **(c)** _w_ = 0 _._ 33 

we define _δ_ h := 0 for log2( _f_ 1 _/f_ 2) = _−p/_ 1200 to retain differentiability. Furthermore, we assume for _δ_ h that _w_ c stays constant for small shifts _p_ , so that its frequencydependency does not play a role in a single gradient descent step. Replacing _d_<sup>_K_</sup> t<sup>with</sup><sup>_δ_</sup> t<sup>_K_</sup> and _d_ h with _δ_ h in (4) and (6) allows calculating the derivative of _Cv_ [ _n_ ] directly with respect to _p_ , so that the update rule becomes 



<!-- Start of picture text -->
pv, new[ n ] =  pv [ n ]  − µ dCv [ n ] , (9)<br>dp<br><!-- End of picture text -->

where _µ_ is a step size parameter and the derivative of _Cv_ [ _n_ ] (with the unit “cost change per cent shifted”) is a weighted <u>t</u> sum of<sup>_dδ_</sup> _dp_<sup>_K_and</sup><sup>_<u>dδ</u>_</sup> _dp_<sup><u>h</u>:</sup> 



<!-- Start of picture text -->
dδdp t K = 1200 πK sin 2 πK (log2( f 1 /f 2) +  p/ 1200) (10)<br><!-- End of picture text -->



<!-- Start of picture text -->
dδ h ln( |  log2( f 1 /f w 2 c )+ p/ 1200 | )<br>dp =  − 600(log2( f 1 /f 2) +  p/ 1200)<br>(11)<br>exp( − ln 2 ( |  log2( f 1 /f 2) + p/ 1200 | )) .<br>w c<br><!-- End of picture text -->

with<sup>_<u>dδ</u>_</sup> _dp_<sup><u>h</u>=0 for log2(</sup><sup>_<u>f</u>_</sup> _f_<sup><u>1</u></sup> 2<sup>)=</sup><sup>_−_</sup> 1200 _<u>p</u>_<sup>.By setting</sup><sup>_pv_[</sup><sup>_n_] to</sup> an initial value (e. g. 0) and repeatedly evaluating (9), we can now iteratively find the local minimum of _Cv_ [ _n_ ] for each time frame. However, for short frame sizes, correlation between salient frequencies in successive time frames can be expected. Therefore, instead of finding the closest local minimum for each frame independently, we can use the pitch shift from the previous frame as the initial value for _pv_ [ _n_ ]. Furthermore, to retain natural short-term pitch variations in the signal (e. g. vibrato), we require a certain temporal smoothness of _pv_ [ _n_ ]. This can be achieved by updating _pv_ [ _n_ ] with only a single gradient descent step in each time frame, which yields 



<!-- Start of picture text -->
pv [ n ] =  pv [ n − 1]  − µ dCv [ n ] (12)<br>dp<br><!-- End of picture text -->

for _n >_ 0 and _pv_ [0] = 0. Together with the frame size, the step size _µ_ controls the rate at which pitch changes in 

the signals influence _pv_ [ _n_ ]. This can be observed in Figure 6, which shows the resulting _pv_ [ _n_ ] from joint gradient descent with (12) for a varying weight _w_ between _C_ t and _C_ h in the example cadence. For example, the pitch shift for the soprano voice visibly approaches a minimum in the first few frames of chords I and II. Moreover, it can be seen that the harmonic cost alone (Figure 6b) is not robust in musically dissonant chords like chord III, whereas with _w_ = 0 _._ 33 (Figure 6c), the obtained pitch shift tends towards JI without ending up in a local minimum far away from equal temperament (cf. tenor in chords III and IV). 

### **4. APPLICATION: INTONATION ADAPTATION IN CHORAL MUSIC** 

In the previous section, we introduced a method to obtain pitch shift curves by minimizing a cost measure that quantifies two aspects of intonation: the distance of a pitch to an equal temperament grid and the perceptual dissonance with regard to a harmonic reference. As a tool, this allows sound engineers to flexibly adapt the intonation in audio recordings between equal temperament and JI using the two parameters _w_ and _µ_ . With _w_ , the relative weight between both aspects can be adjusted depending on artistic intent and musical context. _µ_ controls the temporal behavior of the adaptation, where a larger _µ_ corresponds to a stronger reaction to short-term pitch fluctuations. 

A subjective evaluation of preferred intonation in different musical contexts and the resulting suitable choices for the parameters of our cost measure is beyond the scope of this paper. Many additional aspects, including timbre, acoustics, and performative choices (vibrato, portamento, etc.) [25], as well as listener taste and experience [26], influence intonation perception. Instead, we demonstrate the utility of the cost-based adaptation tool with an example from amateur performances of a cappella choral music. In this application with particularly volatile intonation, we show that the approach is robust on real-world signals and can blindly achieve results that are comparable to scoreinformed intonation adaptation. 

For this, we apply the presented method to recordings from the _Dagstuhl ChoirSet_ (DCS) [27]. The intonation adaptation of individual voices in a vocal recording requires separate signals for each voice and the dataset contains headset microphone signals for each singer. In this section, we consider the last four bars (45 to 48) from a performance of the motet _Locus Iste_ (WAB 23, 1869) by Anton Bruckner (Quartet B, Take 3 in the dataset). The four-part a cappella composition is performed by a quartet of soprano (S), alto (A), tenor (T) and bass (B). 

First, we obtain the salient frequencies for each voice from the four individual headset microphone signals, using the method described in Section 3.1. For the STFT, we keep the hop size of 0 _._ 1 sec (2205 samples in the DCS audio signals) and use a window size of 4096 samples for an improved frequency resolution. Due to varying levels and timbre of the singing voice and background noise, the number of salient frequencies in _P_ [ _n_ ] fluctuates. On average, _|P_ [ _n_ ] _|_ is 6.6 (S: 5.6, A: 6.8, T: 4.4, B: 9.6) in 

630 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

the voiced frames (i. e., where _|P_ [ _n_ ] _| >_ 0). To assess the robustness of the detected salient frequencies against crosstalk and noise, we calculate the average deviation of each frequency from being an integer multiple of the lowest frequency in this frame (corresponding to the “harmonicity” of the signal). In the excerpt, the detected frequencies deviate from the harmonic overtones by a factor of 1.01 on average (S: 1.007, A: 1.012, T: 1.006, B: 1.016). 

We now compute a pitch shift _p_<sup>CB</sup> _v_<sup>[</sup><sup>_n_]foreachvoice</sup> with the cost-based (CB) method as described in Section 3.4, using a single gradient descent step for each frame (see (12)). For the present example, we set _w_ = 0 _._ 2 and _µ_ = 350 and used fixed parameters _K_ = 12 and _f_ ref = 440 Hz for the tonal cost. The pitch shifts _p_<sup>CB</sup> _v_<sup>[</sup><sup>_n_]</sup> are applied to each signal with a time-variant pitch shift algorithm based on resampling and time-scale modification [28]. In a cappella performances, one often observes (downward) intonation drifts [10], causing _p_<sup>CB</sup> _v_<sup>[</sup><sup>_n_] to drift</sup> in the opposite direction to counteract this effect. For instance, the mean pitch shift across all voices in bar 48 of our example is 21 cents. Note that, to counteract a global drift of all voices in a similar direction, even _|p_<sup>CB</sup> _v_<sup>[</sup><sup>_n_]</sup><sup>_|>_</sup> 50 cents may be intended. In this case, additional regularization can be added in the cost minimization to avoid individual voices ending up in local minima that do not reflect the relative intonation in the performance. 

For the comparison of our method with a scoreinformed baseline (BL) approach, we estimate the F0 trajectories for each voice with pYIN [1] and assign the measurements to individual notes from the aligned score annotation provided in DCS. Then, for each time frame of 0 _._ 1 sec duration, we choose a pitch shift _p_<sup>BL</sup> _v_<sup>[</sup><sup>_n_] that shifts</sup> the median F0 in the current frame onto the 12-TET pitch of the corresponding note in the score. To counteract larger fluctuations that result from the relatively small frame size for this method, we additionally smooth _p_<sup>BL</sup> _v_<sup>[</sup><sup>_n_]usinga</sup> moving average with a window size of 3 frames. The shift is applied to the signals in the same way as _p_<sup>CB</sup> _v_<sup>[</sup><sup>_n_].</sup> 

The pitch shift curves for the excerpt, calculated with the blind CB approach (colored) and the score-informed BL (black), are plotted for all voices in Figure 7a, c, e, and g. Furthermore, subfigures b, d, f, and h show the F0 trajectories of the original (black) and adapted (CB: colored, BL: grey) signals. The difference between the two pitch shift curves is small in most frames, particularly when compared to the magnitude of overall pitch fluctuations in the singing voices. Larger differences between the curves can be observed at the onset of some notes. This can be attributed to the strong influence of short-term fluctuations in the measured F0 trajectories on the BL approach. 

In addition, the harmonic cost term _C_ h has a recognizable effect on the local minimum where JI intervals differ from 12-TET. This can be prominently observed in the soprano voice in bar 48 (c.f. the zoomed detail in Figure 7), where the sung note E is the major third of the final C major chord of the piece and therefore has a JI pitch 14 cents lower than 12-TET. This shows that our real-time capable method for cost-based intonation adaptation is able 



<!-- Start of picture text -->
(a)<br>12-TET baseline<br>pitch shift (cents) 5 25 25 cost-based<br>-50<br>6500<br>(b)<br>6200<br>pitch (cents)<br>(c)<br>-25 baseline<br>cost-based<br>pitch shift (cents) -50 50 25<br>6200<br>(d)<br>5900<br>pitch (cents)<br>50 25 0<br>(e)<br>(cents)-25 baseline<br>pitch shift -50 cost-based<br>5700<br>(f)<br>5400<br>pitch (cents)<br>50 25 0<br>(g)<br>(cents)-25 baseline<br>pitch shift -50 cost-based<br>4800<br>4500 (h)<br>4200<br>pitch (cents)<br>45 46 musical time (bars)47 48<br><!-- End of picture text -->

**Figure 7** : Joint adaptation of bars 45-48 of A. Bruckner “Locus Iste” (DCS, Quartet B, Take 3). The F0 trajectory plots (b,d,f,h) show the F0 of the original signal (black), the baseline (BL, grey) and the cost-based (CB, colored, _w_ = 0 _._ 2, _µ_ = 350) pitch-shifted signals. **(a, b)** Soprano **(c, d)** Alto **(e, f)** Tenor **(g, h)** Bass 

to approach JI tuning in vocal recordings without explicit knowledge about scales and keys. 

### **5. CONCLUSION** 

In this paper, we introduced a differentiable cost measure for intonation processing in polyphonic music recordings, which accounts for a tonal and a harmonic aspect in a userspecified proportion. Our method can be used as a flexible tool for intonation adaptation in multitrack choral music recordings. In future work, we will investigate the perceptual implications of our intonation adaptation in real-world signals. Furthermore, we want to apply this principle to more intonation processing tasks such as adaptive tuning of synthesizers and explore ways to incorporate additional aspects of intonation in the cost measure. 

631 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

**Acknowledgements:** This project is supported by the German Research Foundation (DFG MU 2686/12-1, MU 2686/13-1). The International Audio Laboratories Erlangen are a joint institution of the Friedrich-AlexanderUniversität Erlangen-Nürnberg (FAU) and Fraunhofer Institute for Integrated Circuits IIS. 

### **6. REFERENCES** 

- [1] M. Mauch and S. Dixon, “pYIN: A fundamental frequency estimator using probabilistic threshold distributions,” in _IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)_ , Florence, Italy, 2014, pp. 659–663. 

- [2] M. Mauch, K. Frieler, and S. Dixon, “Intonation in unaccompanied singing: Accuracy, drift, and a model of reference pitch memory,” _Journal of the Acoustical Society of America_ , vol. 136, no. 1, pp. 401–411, 2014. 

- [3] C. Weiß, S. J. Schlecht, S. Rosenzweig, and M. Müller, “Towards measuring intonation quality of choir recordings: A case study on Bruckner’s Locus Iste,” in _Proceedings of the International Society for Music Information Retrieval Conference (ISMIR)_ , Delft, The Netherlands, 2019, pp. 276–283. 

- [4] J. Devaney, M. I. Mandel, and I. Fujinaga, “A study of intonation in three-part singing using the automatic music performance analysis and comparison toolkit (AMPACT),” in _Proceedings of the International Society for Music Information Retrieval Conference (ISMIR)_ , Porto, Portugal, 2012, pp. 511–516. 

- [5] F. Havrøy, “‘You Cannot Just Say: “I am Singing the Right Note”’. Discussing intonation issues with Neue Vocalsolisten Stuttgart,” _Music & Practice_ , vol. 1, 2013. 

- [6] A. Grell, J. Sundberg, S. Ternström, M. Ptok, and E. Altenmüller, “Rapid pitch correction in choir singers,” _The Journal of the Acoustical Society of America_ , vol. 126, no. 1, pp. 407–413, 2009. 

- [7] J. Dai and S. Dixon, “Singing together: Pitch accuracy and interaction in unaccompanied unison and duet singing,” _The Journal of the Acoustical Society of America_ , vol. 145, no. 2, pp. 663–675, 2019. 

- [8] ——, “Intonation trajectories within tones in unaccompanied soprano, alto, tenor, bass quartet singing,” _The Journal of the Acoustical Society of America_ , vol. 146, no. 2, pp. 1005–1014, 2019. 

- [9] P.-G. Alldahl, _Choral Intonation_ . Gehrmans Musikförlag, 1990. 

- [10] D. M. Howard, “Intonation drift in a capella soprano, alto, tenor, bass quartet singing with key modulation,” _Journal of Voice_ , vol. 21, no. 3, pp. 300–315, 2007. 

- [11] J. Berezovsky, “The structure of musical harmony as an ordered phase of sound: A statistical mechanics approach to music theory,” _Science Advances_ , vol. 5, p. eaav8490, May 2019. 

- [12] W. Sethares, “Adaptive tunings for musical scales,” _The Journal of the Acoustical Society of America_ , vol. 96, 1994. 

- [13] Celemony, “Melodyne,” https://www.celemony.com/ en/melodyne/, accessed: 2021-05-07. 

- [14] Antares, “Auto-Tune,” https://www.antarestech.com/, accessed: 2021-05-07. 

- [15] D. Code, “Groven.Max: An adaptive tuning system for MIDI pianos,” _Computer Music Journal_ , vol. 26, pp. 50–61, 2002. 

- [16] W. Mohrlock, “Hermode Tuning,” http: //www.hermode.com/index_en.html, accessed: 2021-05-07. 

- [17] K. Stange, C. Wick, and H. Hinrichsen, “Playing music in just intonation: A dynamically adaptive tuning scheme,” _Computer Music Journal_ , vol. 42, no. 3, pp. 47–62, 2018. 

- [18] S. Wager, G. Tzanetakis, C. Wang, and M. Kim, “Deep autotuner: A pitch correcting network for singing performances,” in _Proceedings of the IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP)_ . Barcelona, Spain: IEEE, 2020, pp. 246–250. 

- [19] W. A. Sethares, “Local consonance and the relationship between timbre and scale,” _Journal of the Acoustical Society of America_ , vol. 94, no. 3, pp. 1218–1228, 1993. 

- [20] R. Plomp and W. J. M. Levelt, “Tonal consonance and critical bandwidth,” _Journal of the Acoustical Society of America_ , vol. 38, no. 4, pp. 548–560, 1965. 

- [21] J. Villegas and M. Cohen, “Roughness minimization through automatic intonation adjustments,” _Journal of New Music Research_ , vol. 39, pp. 75 – 92, 2010. 

- [22] D. FitzGerald, “Harmonic/percussive separation using median filtering,” in _Proceedings of the International Conference on Digital Audio Effects (DAFx)_ , Graz, Austria, September 2010, pp. 246–253. 

- [23] J. O. Smith and X. Serra, “PARSHL: An analysis/synthesis program for non-harmonic sounds based on a sinusoidal representation,” in _Proceedings of the International Computer Music Conference (ICMC)_ . Computer Music Association, 1987. 

- [24] T. Nakano, M. Goto, and Y. Hiraga, “An automatic singing skill evaluation method for unknown melodies using pitch interval accuracy and vibrato features,” in _Proceedings of the Annual Conference of the International Speech Communication Association (INTERSPEECH)_ , Pittsburgh, PA, USA, 2006, pp. 1706–1709. 

632 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

- [25] J. M. Geringer, R. B. MacLeod, C. K. Madsen, and J. Napoles, “Perception of melodic intonation in performances with and without vibrato,” _Psychology of Music_ , vol. 43, no. 5, pp. 675–685, 2015. 

- [26] F. Loosen, “The effect of musical experience on the conception of accurate tuning,” _Music Perception_ , vol. 12, no. 3, pp. 291–306, 1995. 

- [27] S. Rosenzweig, H. Cuesta, C. Weiß, F. Scherbaum, E. Gómez, and M. Müller, “Dagstuhl ChoirSet: A multitrack dataset for MIR research on choral singing,” _Transactions of the International Society for Music Information Retrieval (TISMIR)_ , vol. 3, no. 1, pp. 98– 110, 2020. 

- [28] S. Rosenzweig, S. Schwär, J. Driedger, and M. Müller, “Adaptive pitch-shifting with applications to intonation adjustment in a cappella recordings,” to appear in Proceedings of the International Conference on Digital Audio Effects (DAFx), Vienna, Austria, 2021. 

633 

