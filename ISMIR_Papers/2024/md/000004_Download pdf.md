---
paper_id: "000004"
year: 2024
title: "Download pdf"
source_url: "https://zenodo.org/record/14877286/files/000004.pdf"
---

# HARMONIC AND TRANSPOSITION CONSTRAINTS ARISING FROM THE USE OF THE ROLAND TR-808 BASS DRUM Emmanuel Deruty Sony Computer Science Laboratories, Paris, France; Aalborg University, Denmark `emmanuel.deruty@sony.com` 

|ABSTRACT|
|---|



|The study investigates hip-hop music producer Scott|
|---|
|Storch’s approach to tonality, where the song’s key is trans-<br>posed to fit the Roland TR-808 bass drum instead of tun-<br>ing the drums to the song’s key. This process, involving the<br>adjustment of all tracks except the bass drum, suggests sig-<br>nificant production motives. The primary constraint stems<br>from the limited usable pitch range of the TR-808 bass|
|drum if its characteristic sound is to be preserved. The<br>research examines drum tuning practices, the role of the|
|Roland TR-808 in music, and the sub-bass qualities of its|
|bass drum. Analysis of TR-808 samples reveals their char-<br>acteristics and their integration into modern genres like<br>trap and hip-hop. The study also considers the impact of|
|loudspeaker frequency response and human ear sensitiv-|
|ity on bass drum perception. The findings suggest that<br>Storch’s method prioritizes the spectral properties of the|
|bass drum over traditional pitch values to enhance the bass<br>response. The need to maintain the unique sound of the<br>TR-808 bass drum underscores the importance of spectral<br>formants and register in contemporary popular music pro-<br>duction.|



## 1. INTRODUCTION 

In popular music, a common practice is to tune the drums to the song’s key [1]. However, in a 2007 interview [2], R&B producer Scott Storch suggests that during the production of music involving a Roland TR-808 drum machine, it may be beneficial to do the opposite and transpose the song’s key to fit the 808 bass drum [3]. The process involves transposing all the tracks but the bass drum. Storch’s motive for undertaking such a potentially timeconsuming set of operations is to conserve the characteristic sound of the 808 bass drum. 

The present study investigates aspects of the music production process that may explain Storch’s position. In Section 2, we shortly address the issue of drum tuning in popular music. In Section 3, we provide an overview of the importance and usage of the Roland TR-808 in popular music production, focusing on its bass drum voice. 

|© E. Deruty. Licensed under a Creative Commons Attribu-|
|---|
|tion 4.0 International License (CC BY 4.0). Attribution:<br>E. Deruty,|
|“Harmonic and Transposition Constraints Arising from the Use of the|
|Roland TR-808 Bass Drum”, in Proc. of the 25th Int. Society for Music|
|Information Retrieval Conf., San Francisco, United States, 2024.|



|In Section 4.1, we analyze the content of TR-808 bass|
|---|
|drum samples. In Section 4.2, we relate spectral features<br>of TR-808 bass drum samples to a diachronic analysis of|
|the power spectrum in popular music. In Section 5, we can|
|understand Storch’s position by involving the frequency re-|
|sponse of loudspeakers and the sensitivity of the human|
|ear. Finally, in Section 6, we discuss how the practice sug-|
|gested by Storch may be a particular case of how properties|
|of the spectrum might be considered more important than|
|pitch values.|



## 2. DRUMS AND TUNING 

|The musical signal has been divided into two categories:|
|---|
|“percussion has a short temporal duration and is rich in|
|noise, while harmonic elements have a long temporal du-|
|ration with most of the signal energy concentrated in pitch|
|spikes” [4]. “The harmonic and percussive components of|
|music signals have much different structures in the power|
|spectrogram domain, the former is horizontal, while the|
|latter is vertical” [5]. These observations are the basis for|
|source separation methods distinguishing “drums” from|
|“pitched instruments” [6,7].|



|Yet, drums can contain|pitched content [8]. In drum|
|---|---|
|sounds, relations between|eigenfrequencies are not nec-|
|essarily harmonic [9]. “Th<br>usually not structured like|e tonal elements in drums are<br> partials in a harmonic series.|
|Instead, their frequency re|lationship can range from in-|
|harmonic to chaotic” [10].|From a music producer’s per-|
|spective, “drums make sev<br>ously” [11].|eral different notes simultane-|



|Recent source separation methods don’t involve prior|
|---|
|hypotheses. They’re based on models trained on actual|
|data. Listening to the audio output stemming from such|
|technology indicates that drum stems extracted from pop-<br>ular music do contain pitch. Demonstrations of Stein-|
|berg’s SpectraLayers [12], Native Instruments’ iZotope|
|RX 8 [12], iZotope RX 9 [13], and StemRoller [14], pro-<br>vide relevant examples.|



|If drums contain pitched content, they can be tuned. In<br>popular music, the “[i]ntricate tuning of acoustic drums<br>can have a significant impact on the quality and contex-|
|---|
|tuality of the instrument” [1]. There is no consensus on|
|how to tune drums: “[t]alk to ten different drummers and|
|you’ll get ten different ways to tune drums [...] there’s ac-|
|tually no wrong or right way to tune a drum, or right or|
|wrong pitches to tune it to” [15].|



|78|
|---|



Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

Scott Storch is an American record producer and songwriter. Storch has been referred to as a “producer that changed the R&B game” [16], a “superproducer” [17], i.e. a wave of artists “who have established a new degree of visibility for the rap producer, earning star billings virtually equal in prominence to the artists that they produce” [18]. For Scott Storch, drum tuning is an integral part of the music production process: 

“I know there’s a lot of producers [who will] put an 808 in the song, and there will be chords and stuff clashing with it, and [...] if [...] your ears are really in tune with that stuff, you realize it’s just like [“not so convincing” kind of gesture]... Sometimes, it actually does something cool to the track, but [...] I like to [...] get into that and tune the kick to match [...] the bass line or whatever the chords are doing [...], I just try different stuff... then... [even when there is] not an incredible amount of tune that carries over regular kicks, like short kicks, and I find myself sometimes at least even trying to tune [...] a regular [...] kick drum sound, and get it close to where most of the chords are in the song...” [2, 0:30] 

In the above, Storch mentions the Roland TR-808 bass drum and testifies to tuning bass drums to match the music’s key. 3. THE ROLAND TR-808 

The Roland TR-808 Rhythm Composer is an analog drum machine manufactured between 1980 and 1983 [19]. It is “one of the most influential and unique drum machines of its time” [20]. “To this day, the 808 remains a benchmark against which all other analog drum machines are measured” [21]. It can be found in many music genres. The TR-808’s distinctive presets are classic sounds in hiphop, techno, electro, R&B, and house music [22]. The 808 “play[ed] a central role in the development of acid house” [21]. Pop music star Phil Collins used it throughout his entire career [23, 1:21:28]. It is “a fixture in hip-hop culture, not only as a tool for producers but as a defining sound of the genre” [19]. According to Scott Storch, in modern trap music, producers “live in an 808 world” [24]. One reason for the success of the 808 resides in the fact that “it sounded like nothing else [...] and this is what made it so distinctive” [25]. Perhaps as a result, the 808 has been seen not only as a drum machine but as an “instrument in its own right” [23, 0:06:51]. 

One notable voice of the 808 is its “long and velvet deep, almost subsonic” bass drum [25], which can be made into a “multi-second-long decaying pseudo-sinusoid with a characteristic sighing pitch” [21]. According to producer Pharrell Williams, the 808 bass drum “filled a massive void in the sound spectrum that wasn’t there [...] once the 808 started to occupy that space, it became like something that you missed if you didn’t have it” [23, 1:20:52]. 

Over time, the 808 bass drum became used as both kick drum and bass. According to producer Remi Kabaka Jr., “the kick drum would play the bass at the same time [...] there was drums and there was bass, but now the two were sort of fused, so the fill was not just complex and rhythmical, but it was also tonal” [23, 1:11:11]. Musician and writer Alex Lavoie notes that “[i]n most contemporary music genres, especially in trap and hip-hop, the 808 often carries the bassline, providing both the lowend foundation and outlining the harmonic progression of the song” [26]. Musician and producer Charles Burchell writes that the TR-808 “brings a sound closer to a traditional bass line while retaining the power of a drum [...] In many cases, producers will not use a kick drum sample. Instead, they program drum patterns with a tuned 808 as the kick drum” [27]. 

As a tonal instrument, the 808 bass drum can be tuned: as Lavoie states, “[a]n 808 kick, particularly when it has a long decay, effectively functions as a bass instrument. That’s why tuning your 808s is so crucial” [26]. Lavoie warns that “[i]f the pitch of your 808 kick doesn’t match the key of your song, it can create a dissonant effect” [26]. 4. THE 808 BASS DRUM 4.1 Signal analysis of 808 bass drum samples 

Figure 1 shows the waveform corresponding to the “TR808 BD Bass Drum Long 01” preset. All samples considered in this paper originate from the TR-808 Trisample library [28]. The waveform confirms that the sample is tonal. The tonal aspect derives from the TR-808 generation technique, during which an oscillator produces a sawtooth wave that is filtered to make it close to a sine wave [29]. 



Figure 1. “TR808 BD Bass Drum Long 01” sample, waveform. 

Figure 2 shows the STFT for the same sample. Harmonics are present near the start of the sample and then fade out. The sample’s pitch value is briefly higher near the beginning, then decreases to a stable value. A study of the 37 “long” samples from the Trisample library shows that the median range for the initial frequency sweep is close to one half-tone. 

The Tristar library features “driven” samples (a reference to the slang term “drive” for “overdrive”, i.e. “distortion”). Figure 3 shows the STFT for one “driven” sample. The threshold conditioning the display of the partials as red lines is the same as in Figure 2, which indicates that the distortion boosts the level of the overtones. 

79 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 



<!-- Start of picture text -->
Time (s) 2.2<br><!-- End of picture text -->

Figure 2. “TR808 BD Bass Drum Long 01” sample, STFT. The horizontal lines follow the fundamental and harmonics. The blue line stops when the energy of the corresponding bin is lower than 0.7 times the peak energy of all bins. The red lines stop when the energy of the corresponding bin is lower than 0.5 times the peak energy of all bins. 



<!-- Start of picture text -->
0.6 Time (s)<br><!-- End of picture text -->

Figure 3. “TR808 BD Bass Drum Driven 01” sample, STFT. 

Figure 4 shows the STFT for an extract from the 2017 song “Mask Off”, by the American rapper Future. The track has been described as an example of heavy 808 use [19]. The initial frequency sweep on each bass drum occurrence is similar to the samples shown in Figures 2 and 3. The vertical distribution of high energy values at the beginning of each bass drum occurrence suggests that the 808 is superimposed with a noisier kick drum. The 808 samples are tuned to the song’s tonality (D minor). The pitch values (D1 and B♭0) are very low: they stand one minor second and one perfect fourth above the piano’s lowest note. The corresponding frequency range (ca. 40Hz) recalls the “almost subsonic” aspect of the 808 bass drum samples [25]. 



<!-- Start of picture text -->
Beat number<br><!-- End of picture text -->

Figure 4. Future, “Mask Off”, 8 beats from 0’25 to 0’30, STFT. The vertical lines denote the kick drum’s onsets. The horizontal lines follow the TR’s fundamental and harmonics. The corresponding pitch values are shown at the top. 

## 4.2 Sub-bass frequencies and the 808 bass drum 

Producers recognize three distinct regions of sub-bass: the “boom” (ca. 30Hz), the “thump” (ca. 50Hz) and the 

“punch” (ca. 80Hz) [30, pp. 88–118] [31, p. 282]. Figure 5 confirms that 50Hz (the “thump”) is the “frequency range occupied by the Roland TR-808 analog kick” [31]. 

Before the advent of digital audio, low frequencies were attenuated to protect amplifiers and speakers from the adverse effects of mechanical noise and harmonic distortion [31, p. 282] [32,33]. Musical information in this frequency range only became possible by using digital audio as a medium. Figure 6 shows the evolution of the power spectrum in popular music. The measures were derived from a dataset containing 30435 tracks released between 1961 and 2022. The choice of the tracks stems from the “Best Ever Albums” website, a review aggregator that proposes the best-rated albums for each year of production [34]. For each year, we select the best-rated albums. The overall spectral profile is consistent with Pestana’s results [35]. The increase of energy in the lower band, also testified by Hove et al. [36], is concomitant to the advent of digital audio. 



<!-- Start of picture text -->
49.48Hz Short<br>Medium<br>Long<br>50.12Hz 51.05Hz Driven<br>Distribution<br>46 47 48 49 50 51 52 53 54<br>Frequency (Hz)<br><!-- End of picture text -->

Figure 5. Distribution of fundamental frequencies of TR-808 bass drum samples. The fundamental frequencies are evaluated on 0.2-second windows. The contribution of each window is weighted according to the energy at the fundamental frequency. In the non-“driven” presets, the maximum of the distribution corresponds to f0 = 49.48 Hz. The f0 values for the “driven” presets are higher. “Short” presets involve a secondary local maximum (f0 = 51.05 Hz) corresponding to the samples’ earliest windows. 



<!-- Start of picture text -->
Power spectrum (white=more energy, black=less energy)<br>4277<br>1963 1968 1973 1978 1983 1988 1993 1998 2003 2008 2013 2018<br>Year<br>Power spectrum (each band has the same mean)<br>8041<br>4277<br>Center frequency2275<br>1963 1968 1973 1978 1983 1988Year1993 1998 2003 2008 2013 2018<br><!-- End of picture text -->

Figure 6. Evolution of the power spectrum in popular music. Top, raw energy values. Bottom, values for each frequency band are normalized to the same mean. 

The analysis results shown in Figure 2 indicate that after the initial 0.4s-long attack, “long” 808 samples are based on a single low-frequency sine wave. The sine wave’s frequency is ca. 50 Hz according to Figure 5. The results shown in Figures 3 and 4 suggest that this very low frequency remains an essential component of the 808 bass 

80 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

drum with added harmonics. Confronting these observations with the power spectrum evolution in popular music (Figure 6), it follows that the sound of the 808 bass drum wasn’t fully reproduced before the end of the ’90s, even though the machine itself was sold between 1980 and 1983. 

mentioned by Storch. Storch states that the loudspeakers may not reproduce the bass correctly in such a situation. 

Professional mixing engineers mainly use near-field monitors [39, p. 3]. With such monitors, they can produce “masters which ‘travel’ well to their use by the record buyers” [40]. The use of near-field monitors extends to producers. Nigel Godrich testifies that during the production of Radiohead’s “OK Computer”, he always used nearfield monitors, but never the studios’ main monitors, which “don’t relate to anything” and are “fairly useless” [41]. In the many videos documenting his work, Storch can be seen using near-field monitors. 

After 2009, “the characteristic 808-kick drums [...] started entering mainstream music in general”, and trap music, a “tradition of rap that developed during the 1990s”, an “808 world” according to Scott Storch (see Section 3), “began to reach strong presence on the mainstream Billboard music charts” [37]. So strong is the presence of trap in the charts that this formerly underground genre has been qualified as “pop”, in the sense that “[p]eople’s ears have adjusted” to it [38]. 

Newell et al. [40] provide the frequency response for 36 near-field monitoring loudspeakers. Figure 7 graphs the median frequency response for these loudspeakers against the median f0 for the 808 bass drum samples (49.5Hz / G1) and the TR bass drum median frequency transposed down one perfect fourth (37Hz / D1). The downward transposition results in a gain loss of 6.3 dB. Following Storch’s suggestion and transposing up the song key instead of transposing down the 808 sample would avoid the 6.3dB loss. In Storch’s terms, transposing the song up may “let speakers do what they need to do with the bass”. 

The extended bandwidth provided by the emergence of digital audio made possible the faithful restitution of the entire spectrum of the 808 bass drum, which favored the birth and rise of a music genre that became mainstream and influenced popular music in general. 5. TUNING THE SONG’S KEY TO THE TR-808 BASS DRUM 



<!-- Start of picture text -->
10<br>Response (dB)<br>-5 semitones Median f0<br>- B8 TR-808<br>20 25 32 50 63 80 100 126 159 200<br>Frequency (Hz)<br><!-- End of picture text -->

In Section 2, Scott Storch describes how he tries to tune the bass drum (808 in particular) to the music’s key. Later in the same interview, Storch suggests that instead of tuning the 808 bass drum sample to the song’s tonality, one can do the opposite and adjust the song’s key to the 808 bass drum sample: 

“[S]ometimes, producers will program a song in a certain key, and they’ll try to program an Figure 7. near field loudspeaker responses as a function 808 under it, and it’s like the key of the song is of frequency. The center horizontal line in each box reprealmost too low to really let speakers do what sents the median, and the two surrounding horizontal lines represent the 25<sup>th</sup> and 75<sup>th</sup> percentiles. The blue line shows they need to do with the bass so, I recommend [...] modulating the song up, transposing it the smoothed median response. The red vertical line represents the median f0 for the 808 bass drum as shown in Secup a couple of keys, and you’ll be surprised how much more level you can get out of the tion 4.2, Figure 5. The gray rectangle denotes a -5 semitone transposition of the median f0. The textual represensong. [Because] anything really below [. . . ] a low E [...], it’s like the speakers are gonna tation displays the difference in the response that occurs. not, let you turn it up, you don’t feel the bass Loudspeakers are not the only frequency-dependent response.” [2, 1:37] 

Loudspeakers are not the only frequency-dependent transducers involved in the listening process. The human ear is also sensitive to frequency. In particular, as the frequencies get closer to the lower limit of human hearing, a sine wave with the same sound pressure level but a lower frequency will be perceived as less loud. The phenomenon is accounted for by equal loudness contours, representing the sound pressure levels at different frequencies that are perceived as equally loud [42]. Figure 8 graphs the ISO226-2003 [43] equal loudness contours against the median 808 bass drum f0, and the same frequency transposed down one perfect fourth. If we choose a loudness of 60 phon, a +5.5dB gain would be required so that the transposed f0 remains at the same loudness. Therefore, considering the human ear as one of the transducers in the signal path, the gain it applies to the signal when transposing down the original median f0 is ca. -5.5dB. As a result, 

Storch describes a situation in which a producer previously set the key for a song, tunes an 808 bass drum to make it fit the key, and, as a result, the 808 bass drum does not sound “right”. 5.1 Transposition of the TR-808 bass drum: effect on the lowest partial 

Let us consider an example where the song’s key is D, as in the extract from Figure 4. We focus on the fundamental, the only lasting component in samples from the “long” type (Figure 2). As seen in Figure 5, the f0 of an 808 bass drum is ca. 49.5Hz, corresponding to a G1. The producer, therefore, transposes the 808 bass drum one perfect fourth down (5 semitones) to a D1 – one tone below the “low E” 

81 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

the overall gain loss following the downward transposition originating from both the loudspeakers and the ear can be estimated to be ca. 11.8 dB. 



<!-- Start of picture text -->
100<br>120 80<br>(dB SPL)100 6040<br>20<br>80<br>60<br>-5 semitone Median f0<br>→ +5.5 dB TR-808<br>25 32 40 50 63 80 100 126 159 200<br>Frequency (Hz)<br><!-- End of picture text -->

Figure 8. Equal-loudness contours according to [43]. The numbers superimposed on each contour indicate the loudness value corresponding to the contour (in phon). The red vertical line represents the median f0 for the 808 bass drum as shown in Section 4.2, Figure 5. The gray rectangle indicates a -5 semitone transposition of the median f0 (one perfect fourth down). The textual representation displays the gain that would be required so that the transposed f0 remains at the same 60-phon loudness. 

If different 808 bass drum notes result in different gains, then a sequence of different 808 bass drum notes will result in gain changes within the sequence. Quoting Storch, “for 808s [. . . ] I try to stay in the comfort zone of the speaker, so I don’t [...] have the volumes jumping out for different notes” [44]. In other words, 808 bass drum parts’ pitch should remain largely static to achieve a stable gain. In turn, largely static bass pitch values may result in a limited variety of chords. The phenomenon illustrates how loudness stability may take precedence over harmonic complexity. 

## 5.2 Transposition of the TR-808 bass drum: involvement of the harmonics 

The 808 bass drum samples corresponding to Figures 3 and 4 involve lasting harmonics. Figure 9 shows the combined response deriving from both the near field loudspeakers and the ear’s sensitivity at 60 phon. The lower the frequency, the greater the influence of transposition on the overall gain. The gain loss diminishes with each harmonic. It is almost zero for the fifth harmonic. 

We generate a 49.5Hz five-partial harmonic complex tone. The amplitudes of the partials are the same as in the “TR808 BD Bass Drum Driven 01” sample when the frequency values reach a static regime (see Figure 3). The overall power change following a 5-semitone downward transposition is -4.5dB. It is much less than the -11.8 dB gain brought by the downward transposition of the lone fundamental. The result suggests that the issues mentioned by Scott Storch (gain conservation and gain stability) mainly concern the fundamental or, at least, the lowest harmonics. In other words, Storch is specifically concerned with the audibility and stability of the 808 bass drum’s bottom partials. 

The phenomenon known as the "missing fundamental" [45] suggests that even if a negative gain is applied to lower 



<!-- Start of picture text -->
20<br>Overa l  notional gain (dB)-80 -11.5 dBf0 -> -5.4 dB 12 ->-3.4 dB -3.2 dB -1.0 dBf4 -><br>20 29 42 09 87 126 183 265 383 553 800 1157<br>Frequency (Hz)<br><!-- End of picture text -->

Figure 9. The black line shows the combined response deriving from both the near field loudspeakers and the ear’s sensitivity at 60 phon (Figures 7 and 8). The red vertical lines represent the median values for the 808 bass drum’s fundamental and harmonics. The textual representations display the difference in the response that occurs from a -5 semitone transposition. 

harmonics, the perceived pitch remains unchanged due to the auditory system’s temporal pitch processing. Only timbre is affected. In the case of the sub-bass register, i.e. frequencies lower than 100Hz according to Fink [31, p. 281], another perceptual aspect may be mentioned. In relation to findings by Takahashi et al. [46], Fink et al. [30, pp. 88-118] suggest that one aspect of the perceptual effects of bass stems from small body surface displacements. According to the author, each sub-bass range can be associated with a body region in which the corresponding frequencies are imaginatively felt. The “boom” (ca. 30Hz) is “the semi-audible vibration in the gut felt during the deepest drops in dancehall and dubstep”. The “thump” (ca. 50Hz) is felt in the stomach, and the “punch” (ca. 80Hz) in the chest. Even when listeners use headphones, bass frequencies may be associated with a “tactile sensation” [47]. Fink [31] and Hove et al. [47]’s views suggest that low frequencies may play a role beyond pitch and timbre, in this case, a haptic role. 

A downward transposition and the resulting negative gain applied to these frequencies may affect both the resulting timbre and bodily sensation. As a result, they may be prejudicial to at least some music genres, independently from the presence of upper harmonics. 

## 6. PITCH AND REGISTER 

Scott Storch’s advice according to which a song’s key may be adjusted to the 808 bass drum sample is based on the following premise: the transposition of the elements of the music that are not the 808 bass drum is less problematic than the transposition of the 808 bass drum. The change in pitch values doesn’t affect the musical intervals, but the shift in register affects the perceived spectral profile. The change in perceived spectral profile is more important in the case of the TR-808 bass drum due to its low-frequency content. 

Following Frisius [48, p. 81], “a [music] theory [that] posits a principle of neutral transposition, according to which groups of pitches essentially do not change their character if one transposes them”, doesn’t take into account the transposition of the sounds themselves. Frisius 

82 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

remarks that such a theory may not be suited to music from the 20<sup>th</sup> century. He mentions the composer Luigi Russolo, who found it difficult to “transpos[e] sonic gestures into other registers without losing their identity”. According to Frisius, this difficulty is “felt above all when pitch is not clearly definable”. One way to understand the phenomenon is that transposed melodies are only the “same as” each other because they are constructed using a set of pitches whose chromas repeat at the octave. The listener encodes them in terms of pitch sequences. If two sounds are “transpositions” of each other but are not perceived in terms of pitch, then they are just different sounds. 

Pitch intervals may be robust to transposition, but the register will change, and so will timbre. The phenomenon has been described in orchestration treatises [49–51]. According to Hector Berlioz, as far as the violin is concerned, C major may be “grave, mais sourd et terne” (rich in low frequencies, but dull and muted), and F# minor “tragique, sonore, incisif ” (tragic, resonant, incisive) [49]. More recently, Reymore et al. [52] have studied the relation between pitch height and timbre in acoustic instruments. 

Personal interviews with music producers from the production company Hyper-Music ( `https://www. hyper-music.com/` ) suggest that in recent popular music, the simultaneous consideration for pitch values and register when considering transposition is paramount. According to one of Hyper-Music producers, Storch prioritizing the register of an instrument over particular pitch values is a “basic rule” of modern music production. Pitch is subservient to spectral formants. Priority is given to the absolute position of the formants in the spectrum. If pitch has to be changed so that the formants of the sound carrying the pitch reach the desired positions, it will be changed. Another producer from the same company claims to be always cautious with transposition, as it may affect timbre. In accordance with Frisius’ point of view, if the pitch content of the part is not too strong, the same producer may simply forego transposition, even if the pitched content of the sample conflicts with other tonal elements. 

In productions involving a TR-808 bass drum, HyperMusic’s producers often set the tonality to D or Eb to take full advantage of the bass drum’s character. Such tonalities neighbor that of the example shown in Figure 4. 

## 7. CONCLUSION 

According to Section 2, some authors have previously divided the musical signal into two categories: percussion (rich in noise, short duration), and harmonic elements (long duration, most of the energy concentrated in spikes in the spectrum) [4, 5, 7]. However, other authors have studied the existence of pitch in percussion [8–10]. In music production, drum tuning has been seen as essential [1] but sometimes difficult [8]. Scott Storch, a renowned music producer, has emphasized the importance of fine-tuning drums to match the music’s key despite the inherent challenges in doing so. 

In Section 3, we showed that the Roland TR-808 Rhythm Composer has been deemed an influential analog 

drum machine [19–21], primarily known for its distinctive and deep bass drum sound [25]. Producers and musicians from various music genres have testified to its efficiency in providing low-end foundation. They use the 808 bass drum not only as a kick drum but also as a tonal instrument that plays basslines, thus emphasizing the importance of its tuning. 

Signal analyses of 808 bass drum samples reported in Section 4 show that its fundamental frequency can be found ca. 50Hz and may or may not have lasting harmonics. The measured evolution of the power spectrum in popular music suggests that digital audio technology enabled the faithful reproduction of the 808 bass drum’s extended bandwidth, which played a crucial role in the rise of trap music’s popularity and its subsequent influence on mainstream music [37]. 

In Section 5, we discussed tuning the song’s key to the 808 bass drum. Producers often try to tune the bass drum to match the song’s key. However, Scott Storch suggests an alternative approach: adjusting the song’s key to fit the 808 bass drum sample. Storch explains that some songs might have a key that is too low for the bass to be correctly reproduced by speakers. Instead, he recommends transposing the music up to achieve a more balanced and powerful bass response. If, for instance, the bass drum is transposed down one perfect fourth to match the song’s key, its fundamental frequency loses ca. 11.8 dB in overall gain, considering the response of near field loudspeakers of the type that producers customarily use [39,40] and the human ear’s sensitivity to frequency [43]. The loss may affect the instrument’s timbre and invalidate the specific bodily sensations the sub-bass range may evoke [30, 31, 47]. The analysis also suggests that the gain loss primarily affects the fundamental frequency and lower harmonics. The discussion emphasizes the importance of controlling the level of bass in music production. It suggests that adjusting the song’s key to the 808 bass drum can indeed be a helpful technique to achieve this goal. 

In Section 6, we briefly discussed the relationship between pitch and register in music and how transposition may affect these elements. While classical Western music theory emphasizes the robustness of pitch intervals to transposition, other perspectives [48,52] suggest that transposition has significant consequences on timbre. Orchestration treatises have long associated specific timbral characteristics with different keys, highlighting the importance of considering both pitch and register [49–51]. Recent interviews with popular music producers suggest the approach is significant in modern music production. 

An intriguing research direction may stem from the assessment of one of the interviewees, according to which spectral formants have precedence over pitch values in modern popular music. Storch’s handling of the 808 bass drum is an example of this principle. If such a claim proves to have merit, it may have consequences on music analysis and user interaction in generative systems applied to popular music. 

83 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

## 8. ACKNOWLEDGMENTS 

Many thanks to Yann Macé and Luc Leroy from the music production company Hyper Music for their insights into Scott Storch’s work and the subsequent discussions. Special thanks to David Meredith (Aalborg University) for his valuable comments. 

## 9. REFERENCES 

- [1] R. Toulson, C. C. Crigny, P. Robinson, and P. Richardson, “The perception and importance of drum tuning in live performance and music production,” The Journal on the Art of Record Production, vol. 4, 2009. 

- [2] B. Zisook, “Remix Hotel Atlanta announces keynote speaker Scott Storch,” https://djbooth.net/features/remix-hotel-atlantaannounces-keynote-speaker-scott-storch-0830072, 2007, accessed: 2023-11-09. 

- [3] Penton Media, “Scott storch on kick drums,” https://youtu.be/R5PUcMAFZOI, 2007, accessed: 2023-11-09. 

- [4] H. Rump, S. Miyabe, E. Tsunoo, N. Ono, and S. Sagayama, “Autoregressive MFCC models for genre classification improved by harmonic-percussion separation.” in ISMIR, 2010, pp. 87–92. 

- [5] N. Ono, K. Miyamoto, H. Kameoka, and S. Sagayama, “A real-time equalizer of harmonic and percussive components in music signals.” in ISMIR, 2008, pp. 139–144. 

- [6] D. Fitzgerald, “Harmonic/percussive separation using median filtering,” in 13th International Conference on Digital Audio Effects (DAFX10), Graz, Austria, 2010. 

- [7] J. Yoo, M. Kim, K. Kang, and S. Choi, “Nonnegative matrix partial co-factorization for drum source separation,” in 2010 IEEE International Conference on Acoustics, Speech and Signal Processing. IEEE, 2010, pp. 1942–1945. 

- [8] P. G. Richardson, “Acoustic analysis and tuning of cylindrical membranophones,” Ph.D. dissertation, Anglia Ruskin University, 2010. 

- [9] P. R. Antunes, “Is it possible to tune a drum?” Journal of Computational Physics, vol. 338, pp. 91–106, 2017. 

- [10] C.-W. Wu, C. Dittmar, C. Southall, R. Vogl, G. Widmer, J. Hockman, M. Müller, and A. Lerch, “A review of automatic drum transcription,” IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 26, no. 9, pp. 1457–1483, 2018. 

- [11] J. Roberts, “About drums,” https://circularscience.com /about-drums/, accessed: 2023-11-09. 

- [12] Attack Magazine, “Four of the best stem separation tools,” https://youtu.be/9oNHoE4wHc8&t=870 and t=1181, 2022, accessed: 2023-11-09. 

- [13] S. Loose, “iZotope RX 9 - fixing drums in the master??” https://youtu.be/LCH23ZiTXCA&t=177, 2022, accessed: 2023-11-09. 

- [14] Verysickbeats, “This Might be the CLEANEST Stem Remover from Songs | StemRoller,” https://youtu.be/G76oQ3uL90&t=364, 2023, accessed: 2023-11-09. 

- [15] Drum Magazine, “How to tune drums in four steps,” https://drummagazine.com/how-to-tune-drumsin-four-steps/, accessed: 2023-11-09. 

- [16] M. Singleton, “20 producers that the R&B game,” https://www.yardbarker.com/entertainment/articles/ 20_producers_that__the_r_b_game/s1__37845173, Oct. 2022, accessed: 2023-11-09. 

- [17] D. Chapman, “‘That ill, tight sound’: telepresence and biopolitics in post-Timbaland rap production,” Journal of the Society for American Music, vol. 2, no. 2, pp. 155–175, 2008. 

- [18] R. Levine and B. Werde, “Superproducers,” https://www.wired.com/2003/10/producers/, Oct. 2003, accessed: 2023-11-09. 

- [19] Z. Hasnain, “How the Roland TR-808 revolutionized music,” The Verge, Apr. 2017. 

- [20] O. Meyers, “Roland TR-808 Rhythm Composer,” McGill University, Tech. Rep., 2003. 

- [21] K. J. Werner, J. S. Abel, and J. O. Smith III, “A physically-informed, circuit-bendable, digital model of the Roland TR-808 bass drum circuit.” in DAFx, 2014, pp. 159–166. 

- [22] G. Dayal, “Roland TR-808,” Grove Music Online, Jan. 2014. [Online]. Available: https://doi.org/10.1093/ gmo/9781561592630.article.A2257229 

- [23] A. Dunn, “808,” https://youtu.be/KClqn0oN1lY, 2015, accessed: 2023-11-09. 

- [24] S. Storch, “Masterclass: becoming a hitmaker with Scott Storch. Chapter 8, ‘Defining a bass line’,” https://www.aulart.com/masterclass/scott-storchbecoming-a-hitmaker/, 2022, accessed: 2023-11-09. 

- [25] C. Carter, “Roland TR808 Rhythm Composer (Retro),” Sound on Sound, May 1997. 

- [26] A. Lavoie, “What is an 808? 7 ways to make huge 808 kicks,” https://blog.landr.com/what-is-an808/, Sep. 2020, accessed: 2023-11-09. 

- [27] C. Burchell, “Production hacks: Creating 808 basslines,” https://articles.roland.com/productionhacks-creating-808-basslines/, Nov. 2022, accessed: 2023-11-09. 

- [28] Trisamples, “TR-808,” https://trisamples.com/rolandtr808-free-download/, 2020, accessed: 2023-11-09. 

84 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

- [29] G. Reid, “Practical bass drum synthesis,” Sound on Sound, Feb. 2002. 

- [30] R. Fink, M. Latour, and Z. Wallmark, The relentless pursuit of tone: Timbre in popular music. Oxford University Press, 2018. 

- [31] R. Fink, “The boom in the box: Bass and sub-bass in desktop production,” The Bloomsbury Handbook of Music Production, 2020. 

- [32] O. Read, The Recording and Reproduction of Sound. A Complete Reference Manual for the Professional and the Amateur, 2nd edition. Howard W. Sams Co., 1952. 

- [33] A. Millard, America on record: a history of recorded sound. Cambridge University Press, 2005. 

- [34] Best Ever Albums, “Best ever albums,” https://www.besteveralbums.com/, 2023, accessed: 2023-11-09. 

- [35] P. D. Pestana, Z. Ma, J. D. Reiss, A. Barbosa, and D. A. Black, “Spectral characteristics of popular commercial recordings 1950-2010,” in Audio Engineering Society Convention 135. Audio Engineering Society, 2013. 

- [36] M. J. Hove, P. Vuust, and J. Stupacher, “Increased levels of bass in popular music recordings 1955–2016 and their relation to loudness,” The Journal of the Acoustical Society of America, vol. 145, no. 4, pp. 2247–2253, 2019. 

- [37] J. Kaluža, “Reality of trap: Trap music and its emancipatory potential.” IAFOR Journal of Media, Communication & Film, vol. 5, no. 1, 2018. 

- [38] C. Lee, “2 Chainz explains why ‘pretty girls like trap music’,” https://www.rollingstone.com/music/musicfeatures/2-chainz-explains-why-pretty-girls-like-trapmusic-talks-his-bucket-list-and-benihana-193850, 2017, accessed: 2023-11-09. 

   - [44] S. Storch, “Masterclass: becoming a hitmaker with Scott Storch. Chapter 6, ‘Selecting drum sounds’,” https://www.aulart.com/masterclass/scott-storchbecoming-a-hitmaker/, 2022, accessed: 2023-11-09. 

   - [45] J. C. R. Licklider, “A duplex theory of pitch perception,” The Journal of the Acoustical Society of America, vol. 23, no. 1, Supplement, pp. 147–147, 1951. 

   - [46] Y. Takahashi, K. Kanada, and Y. Yonekawa, “The relationship between vibratory sensation and body surface vibration induced by low-frequency noise,” Journal of low frequency noise, vibration and active control, vol. 21, no. 2, pp. 87–100, 2002. 

   - [47] M. J. Hove, S. A. Martinez, and J. Stupacher, “Feel the bass: Music presented to tactile and auditory modalities increases aesthetic appreciation and body movement.” Journal of Experimental Psychology: General, vol. 149, no. 6, p. 1137, 2020. 

   - [48] R. Frisius, “In search of lost harmony,” Contemporary music: theoretical and philosophical perspectives, pp. 77–87, 2010. 

   - [49] H. Berlioz, Grand traité d’instrumentation et d’orchestration modernes, dédié à sa majesté Frédéric Guillaume IV roi de Prusse. Schonenberger, 1844. 

   - [50] F. A. Gevaert, Nouveau traité d’instrumentation. Lemoine & fils, 1885. 

   - [51] C. Koechlin, Traité de l’orchestration en 4 volumes. Eschig, 1954. 

   - [52] L. Reymore, J. Noble, C. Saitis, C. Traube, and Z. Wallmark, “Timbre semantic associations vary both between and within instruments: An empirical study incorporating register and pitch height,” Music Perception: An Interdisciplinary Journal, vol. 40, no. 3, pp. 253–274, 2023. 

- [39] M. Senior, Mixing secrets for the small studio. Taylor & Francis, 2011. 

- [40] P. R. Newell, K. R. Holland, and J. P. Newell, “The Yamaha NS10M: twenty years a reference monitor. Why?” Proceedings of the Institute of Acoustics, vol. 23, no. 8, pp. 29–40, 2001. 

- [41] A. Robinson, “Radio days,” The Mix, Aug. 1997. 

- [42] H. Fletcher and W. A. Munson, “Loudness, its definition, measurement and calculation,” Bell System Technical Journal, vol. 12, no. 4, pp. 377–430, 1933. 

- [43] ISO, “Normal equal-loudness level contours-ISO 226: 2003,” 2003. [Online]. Available: https: //www.iso.org/standard/34222.html 

85 

