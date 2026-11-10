---
paper_id: "000067"
year: 2021
title: "Is there a “language of music-video clips” ? A qualitative and quantitative study 539-546"
source_url: "https://archives.ismir.net/ismir2021/paper/000067.pdf"
---

# **IS THERE A "LANGUAGE OF MUSIC-VIDEO CLIPS" ? A QUALITATIVE AND QUANTITATIVE STUDY** 

**Laure Prétet** LTCI, Télécom Paris Bridge.audio, Paris, France 

**Gaël Richard Geoffroy Peeters** LTCI, Télécom Paris LTCI, Télécom Paris IP Paris, France IP Paris, France 

## **ABSTRACT** 

Recommending automatically a video given a music or a music given a video has become an important asset for the audiovisual industry - with user-generated or professional content. While both music and video have specific temporal organizations, most current works do not consider those and only focus on globally recommending a media. As a first step toward the improvement of these recommendation systems, we study in this paper the relationship between music and video temporal organization. We do this for the case of official music videos, with a quantitative and a qualitative approach. Our assumption is that the movement in the music are correlated to the ones in the video. To validate this, we first interview a set of internationally recognized music video experts. We then perform a largescale analysis of official music-video clips (which we manually annotated into video genres) using MIR description tools (downbeats and functional segments estimation) and Computer Vision tools (shot detection). Our study confirms that a "language of music-video clips" exists; i.e. editors favor the co-occurrence of music and video events using strategies such as anticipation. It also highlights that the amount of co-occurrence depends on the music and video genres. 

## **1. INTRODUCTION** 

Each day, an ever-growing quantity of videos is created by professionals (for advertisement, movies, series, etc) and individuals (for Instagram, TikTok, YouTube, etc). Finding an appropriate soundtrack to emphasize the video content is therefore a common exercise, which can be timeconsuming if done manually. This explains the success of commercial systems such as MatchTune or of research papers such as “Look, Listen and Learn” [1]. While such systems are very good at recommending music based on the video content, the temporal synchronization between both modalities is rarely taken into account. In order to develop synchronization-aware recommendation systems, some domain knowledge is required on how the synchronization is performed in real videos that feature music. In 

> © Laure Prétet, Gaël Richard, Geoffroy Peeters. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). **Attribution:** Laure Prétet, Gaël Richard, Geoffroy Peeters, “Is there a "language of music-video clips" ? A qualitative and quantitative study”, in _Proc. of the 22nd Int. Society for Music Information Retrieval Conf.,_ Online, 2021. 

this work, we attempt at bridging this knowledge gap by performing a fine-grained cross-modal analysis of the synchronization between audio and video content. We hypothesize that better understanding professionally produced music videos helps designing better models for musicvideo synchronization. This has applications in automatic music-video recommendation [2–6] and generation [7–9]. 

Temporal structure (at the beat, bar or functional segment level) is one of the dominant characteristics of music. For this reason, its automatic estimation has received a lot of attention in the Music Information Retrieval (MIR) community [10]. Temporal structure in video (cuts, scenes, chapters) has similarly received a lot of attention in the Computer Vision community (for example with the goal of creating video summary [11]). Our fine-grained analysis will be using these structural elements. 

Our cross-modal analysis could be performed on any type of video that features a musical soundtrack (eg commercials, movies). We focus here on the special case of of Official Music Videos (OMV). We call OMV an audiovisual document where the audio part consists in a music track, and which aims at promoting said track and its performing artists. As a result, the music track is generally the only source of audio in OMVs. This makes OMVs good prototypes for a study on music-video synchronisation. We do not consider user-generated videos, because we assume that analyzing professionally produced OMVs is more likely to provide reusable insights. 

In the specific case of OMVs, the editing team will often arrange the video rushes based on the structure of the music track [12]. In some cases, the music track can also be adapted from the studio version for narrative purposes. Therefore, music and video structure are de facto associated. However, the level of synchronicity is not always the same, depending on the considered OMV. This is not only due to artistic choices but also depends on the music genre and video genre, as we will see in our study. 

**Proposal and paper organization.** In this paper, we study the relationship between music and video temporal organization using a qualitative and a quantitative approach. The _qualitative_ study is based on a set of interviews with three renowned specialists of official music videos. We interview them in order to find out if and how they consider the relationship between music and video structure in their work. The _quantitative_ analysis is based on a detailed analysis of music and video structural events in OMV using MIR and Computer Vision 

539 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

tools. The OMVs correspond to a subset of the Harmonix dataset [13]. We study specifically the relationship between the duration of music and video segments and between the positions of their respective boundaries. We highlight the dependency of those according to the OMV music and video genre (for which we annotated the data). 

The paper is organized as follows. Section 2 discusses the related literature. Section 3 describes the qualitative study and summarizes the interviews of three music video experts: Jack Bartman (composer), Alexandre Courtès (director) and Maxime Pozzi (editor). Section 4 describes the quantitative study: the dataset creation (4.2), the analysis of the music and video segment duration (4.3.1) and of the music and video segment position (4.3.2). Section 5 concludes and discusses the perspectives of this work. 

## **2. RELATED WORK** 

## **2.1 Music-Video Synchronization: A Short Review** 

Music supervision is an industry that aims specifically at synchronizing music to video. Music supervision experts are dedicated to proposing the best soundtrack to all types of videos, ranging from commercials to movies and series. As of today, this recommendation and synchronization work still features a large amount of manual work. Inskip et. al. [14] interviewed music supervision experts and described their workflow. The authors mention that "the clearest briefs appear to be moving images", suggesting that other types of data (emotion, textual description, reference soundtracks) are not necessary to perform the task. 

At the same period, Gillet et al. [15] proposed a system that can automate part of the music supervision task. Their system relies on the synchronization of music structure (onsets and functional segments) and video structure (motion intensity and cuts) to perform music-video recommendation, without external data. Yang [16] and Mulhem [17] proposed similar approaches. 

More recently, Alexander Schindler gathered a dataset of OMVs (the Music Video Dataset) and performed an in-depth analysis of this specific media [18]. In [19], Schindler and Rauber explain how shot boundary detection is an ill-defined task in music videos, as shot transitions are used in a complex and artistic way. By analyzing the clips, they observe that the music videos present characteristic editing styles (number of shots per second, types of transition) for certain music genres or moods. But they do not quantify this correlation. In [12], the same authors analyze the correlation between visual contents (objects present in the scene) and music genre. For example, cowboy hats are almost systematic in country music videos. 

In our study, we propose a joint approach. We analyze the correlation between the music/video _structure_ and music/video _genres_ . 

analyze the video structure. More specifically, we estimate the downbeat positions, functional segments and shot boundaries from the OMV of our dataset. In the following, we describe the tools we have used for our analysis. 

Downbeat tracking is a popular MIR task [20]. As a result, several ready-to-use libraries are available to estimate downbeat positions from audio files [21, 22]. The state-of-the-art algorithm of Böck et al. [23] consists in two steps. First, a RNNDownBeatProcessor, which relies on multiple Recurrent Neural Networks (LSTMs), estimates jointly beat and downbeat activation functions. The output of the neural networks represents the probability of each frame of being a beat or downbeat position. These activation functions are then fed as observations to a DBNDownBeatTrackingProcessor, which relies on a Dynamic Bayesian network (DBN). The DBN outputs the beat positions of highest likelihood, along with their position inside the bar. 

At a larger timescale, the automatic detection of boundaries between functional segments (choruses, verses and bridges) has also received a lot of attention from the MIR community. The Ordinal Linear Discriminant Analysis (OLDA) algorithm by McFee et al. [24] relies on supervised learning to perform this task. This method adapts the linear discriminant analysis projection by only attempting to separate adjacent segments. Then, the obtained features are clustered with a temporal constraint: only similar successive segments are merged together. 

Similar to music, videos can be divided into segments of various duration, from shots to scenes to chapters and longer sequences. In this study, we focus on a segmentation into shots. The TransNet system [25], by Souˇcek et al., is a Convolutional Neural Network which employs dilated 3D convolutions and which is trained in a supervised way on a shot boundary detection task. 

## **3. QUALITATIVE ANALYSIS: INTERVIEWS** 

## **3.1 Methodology** 

In order to gather intuition on the synchronization of music and video, we conducted a series of semi-structured face-to-face interviews. We selected three music video experts from different professions: composition, direction and editing. Following Inskip et. al. [14], we selected the respondents using a snowball sampling technique. 

Interviews were performed using the Zoom video conferencing software, lasting up to one and a half hours. The interviews were transcribed manually by the researcher, and transcripts were sent back to the respondents for validation. Areas of discussion included the participant’s dayto-day workflow and technical tools, their interactions with the other professions of the industry, and their opinion on example music videos prepared by the researcher. 

## **3.2 Interviews Summary** 

## **2.2 Audiovisual Structure Estimation Tools** 

Our quantitative study (Section 4) relies both on MIR to analyze the music structure and on Computer Vision to 

## _3.2.1 Jack Bartman, Composer_ 

As a composer (for commercials such as Nike, Apple or UbiSoft), Bartman has to adopt both a global and a pre- 

540 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

cise local approach: the content of the music has to match the visual atmosphere, and its temporal structure must be aligned both globally at clip level and locally at frame level. In some cases, the editing follows the structure of the music. But in other cases, typically for advertisement, it is the opposite, and the composer has to adapt the music to an existing movie. Most of the time, when music has to be edited on an existing movie, the slicing operation is privileged. 

_"Slicing can happen at unconventional moments, like the first or last beat of a bar! I simply add a sound effect to make it work."_ 

Time stretching and accelerations can be employed too, but are far less usual. Bartman stresses that synchronizing cuts to audio events is especially important around emotional climaxes of the video. Finally, for some projects, an exact synchronization is not the golden rule: 

_"This year, I worked on a short movie about psychological aspects of the Covid-19 lockdown. After getting used to an imperfectly synchronized mockup soundtrack, the director did not want to use the final version, as the mockup would better suit the intended "madness" atmosphere"._ 

## _3.2.2 Alexandre Courtès, Director_ 

As a director (such as for U2, Phoenix, Cassius, Franz Ferdinand or Jamiroquai), Courtès generally has a lot of freedom when it comes to the temporal organization of a music video. Directors often come up with their own concept and they have little constraint about the content of the video. At large temporal scale, their mission is to emphasize the music climaxes by the appropriate video content. 

_"The music video will often show a performance, so it is similar to a musical comedy: it has to feature costumes, chapters, sets, acts."_ 

Directors are not responsible for placing the cuts, but they can introduce diversity in the video transitions (explosions, large objects passing in front of the camera; see [19] for a more exhaustive list). 

_"Cuts have to follow the music’s rhythm, even though they might not always co-occur with beats."_ 

## _3.2.3 Maxime Pozzi, Editor_ 

As an editor (such as for Rihanna, Taylor Swift, Foals or Woodkid), Pozzi has to combine both a local, frame-level approach to the design of a global emotional trajectory. 

_"Editors and musicians have a similar job, we all want the same thing: rhythm, narration, climaxes."_ 

For chorus and verses, the editing will follow the rhythm and typically accelerate near climaxes. During bridges, it will often be slower and poetic. This can be illustrated for example by Katy Perry’s _Firework_ music video (Figure 1). In this clip, we can see some functional segments where cuts happen very frequently (several times in each bar) and segments where they happen less frequently, for example on the downbeats only. 

Editing can be used as an element of narration. For example, in Adele’s _Rolling in the deep_ music video, starting at timestamp 02:20, the cuts are systematically placed just before the downbeat (see Figure 2). 



<!-- Start of picture text -->
1<br>0<br>Few Frequent<br>cuts cuts<br>1<br>0<br>1<br>0<br>time  ( s )<br>0 233<br>Cut likelihood<br>Downbeats<br>Funct. segments<br><!-- End of picture text -->

**Figure 1** : Audiovisual structure of Katy Perry, _Firework_ , full clip. Horizontal axis: time. Cuts: TransNet estimates. Downbeats: Madmom estimates. Music functional segments: OLDA estimates. 



<!-- Start of picture text -->
1 Δa Δa Δa Δa<br>0<br>1<br>0 time  ( s )<br>140 150<br>Cut likelihood<br>Downbeats<br><!-- End of picture text -->

**Figure 2** : Audiovisual structure of Adele, _Rolling in the deep_ , timestamps 02:20 to 02:30. Horizontal axis: time. Cuts: TransNet estimates. Downbeats: Madmom estimates. ∆ _a_ : anticipation of cuts with respect to downbeat. 

_"Off-beat cuts are used to create dynamics: to surprise the viewer, and illustrate the music’s emotional climax. It makes the video direction appear more "indie" as well, this can be required by the performing artists."_ 

## **3.3 Summary** 

These three interviews provide us with a series of intuitions and hypotheses about the way audio and video are synchronized in music videos. First, musical structure such as chorus and verses are taken into account when directing a music video. Second, audio events such as rhythm, beat and downbeat are taken into account when editing a music video. Finally, according to the desired atmosphere, the audio and video structural events can be more or less perfectly synchronized. 

## **4. QUANTITATIVE ANALYSIS** 

## **4.1 Methodology** 

In the following, we conduct a set of quantitative experiments on how the Structural Events (SE) of the music and of the video are synchronized in time. We do so using Official Music Videos (OMVs). We therefore first collect a dataset of OMVs, along with music and video genre annotations (Section 4.2). For each of them we use MIR tools to estimate music SE (downbeats and functional segments) and Computer Vision tools to estimate video SE (shot boundaries). In our first experiment, we study the 

541 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 



<!-- Start of picture text -->
Harmonix (1000 items - {music-genre, bpm, meter} annotations)<br>548 Official Music Video Video-genre annotation<br>{performance, concept/abstract; narrative, dance, other}<br>Computer Vision (TransNet)<br>video<br>video shot - duration- position  ∆ e 6 4 ="5 T fV O gY z WGn M L 8 ="> A C0 H icj V LSs N V wZ I iq L uC ly 2 Y h/QpKk 0 p4tadG93qyn/ x B 0T nz j 3 Nw Z0 fskGv a Km2bXgu p V 1 bX 0 u s5dC L Ao M / x gq p Nn dY 1Q+0TcVjF7 R 6Je u W B N E 3 Oq 7dti 2 D9Wo H l N D nUa6HI5 O e L b 8 93t0F/2 C FCHwu OGEBkJ6at hS GS J E3I hUj Fs74dmtVi1qW5 y VHo Dcqr Y I 9 u C FH s b0 N +M /r E c nS J3 m BT7 5kRHdW n L J U x EV9 0 t UD w pZ 0 Ts5 lQ9i7O 1 b C h9 gl X D+ 8 L Y w j Z2 6 T73k c JCihR9nu8BH 5V U 67F S c e TX w b y s0nzkY2 = l e64 ="Y Ss7 rwhGEXgxTAW 1 ="> A Cy3icj V HLSs N V w ZI iqLu C Gzd/YBtQknb a WL v 0 AXbjR f / iD 4o 3p m OnH v b 32q cm EYry l XV v f yG5ukQ R r vB YP yNb A 9V7 J hxYXd/t u I4li K p7rRH v B W vM BOS K i+W35/bp1QfcEF2 g jIYA 4 E Y Q 8WO D 0 N mAtf i LI k TipH C I r ZP3y 7t Ggn 0 5deyRJ BFipqt4 r DL9fc I f zvJNS BW oEsX76 p8 r+YtA0e q h U j q 3OS L H i ry5/Q R Cj nt M + 68BV u yp e Lv S sa Plz n LO g Wib B/j pkr F s 0 zMU c Y o S Km qOd 3 jAae1u 5 i 2c a 3 p d1 8 Aj l s=</ t shotshot ∆ Gn ML8Ii T O 4z wc ="> AC 0 H j V Ss N FD 2 r1pf Z d u / Ql p K k0z Y T W Iy E Us 4tad G 9 3 q nx B8A f L7 v a0 K Z m2 bXgup W V1 s5 d C L Ao M / x qhyiNn Y 6JeuWBaH v G R/ 4 r NE 3 Oq 7dti 2D 9oz 8 1hPX n 9 3t 08 F L/2 COl r w Y HuGE Bk J 6a hS egxAb1I Uj d m t V i1 qW 5 y Al 2 6 JHo D crY I 9 u C w E Ug / a37K M F s /c s3U f 7 X J rhaONA 9 m BT5 kRHdW n L x EV 0 SgFtDwp Z i7 O 1 p D d 6kU r Jhb s TC9 gl X + 8 zqnQmfey0PLYwjZ23 R9j n u8 Y BH 5VS K 6U 7Fc e TX w b y s0zk2 = </la t shot time<br>MIR (OLDA, Madmom) + Harmonix annotations (bpm, meter)<br>music<br>funct. segments<br>bar  - position l e 64=" L SVClmz g 7IX xqJ ="> A C z nicjVHLSs NF yCq 5 IU Q d 0 V3LisYB9 S n a i1 h 9wqx8fo v 4B + r e Xm K e c2 f u vX bk VwYxtG W1 t /LbO z UeJr HD qk7o h X j 1 o h i Zvm 2 x+ r 4F z G 6 0 M W c g V u13 Us Q T C moFDe + 3 j i74 / 9SphxU6OE g K w Bucn i Z MGI a2F X F SGERO6Bvj 3bN lA1 o 6 Ds kTi 4 m LE / V x ne b y i R Xo E / u68 r c jq nDRL o r i b65/ U j n rs6 4 8XNU ue 2p+Kt S l b Zs /h zn P Ki Vux8eS L rnCc q 4QA V 1fE73ONB2hDb a s 4tv Sb j 8ByYg = segment ∆ 3j D E7 luvU s qmOQ="> A C z ic VHN S GB/o 5d g Ty b It ZRPXG kyT sN o p V S 8eviW+g4 / jm 5MfzOxu2 c J a 3q em Z2 b n5 hc W lT t6 S R K0N LgkX I wA9F fEM 1 X E l ZO J H4 b qx 6Ld 9 3 Q P/c roh t 5 nI 7Ty sFMaY k V t pks0 8WZ 2 v L w / 3 zU R 7 Qn i OAh C ITB JP a Im5J K kTe0n fLs 1 O Mz a u c j NVQ6 l tb p fq 7 W VaP I ULYv / y j Z T 9 elF M 5 R N 341sG2d6 k0z r B nKNzt o0Mb 3s+Wm / GU V L9 OS 7p Aea IH wC2y x h+6zC o OcY QZ d4 w e r J p 1bt9 S a yLDXsAN l bar<br>- - position beat duration ∆ l e64="Thw 7O LIp D Fi3 j e 64 ="J/ Bx q0uW7ThQ kd ="> A C z3 ic jV H N SsGB / ="> AC ynicj V H N Ss G yVbB H3g p 68 G j2 o ItZRPX kb BU 0 m K o N4 XjxaMH+Q C 8ev T i V W+ y g 4 o / j t mI U 0Js vIH fQDxRc fzOx + u 2 4 c I l y n L J a3qemZb 5 k mZ1v n a Z TW3t n6 S R K0N 2 L gkX G 5t b24W d 3 UYx N h SfwA6y r E M 1 YCt5zA9Fw L / d vXlZOJ H4w hU e a 4W cSPbY01 7 C rz 9 3 Q P/cr oh qt 5 E H n4I7O TJ 2 R NfDdvu t Ygq i m 10 aY r Q E 7T k K pV y Zt s08W2 v G Zg mIlW3t 7 vp 8 +VYP C 3zUZ R 7 Q tniO Ah 8CIT B EIe7 AQ0 dOG C T1 8aAOE nIqR g L 2CF9Bzrp6xP c O Mz a ku c5 j NVQ JqO CRPQDp W K6m 3 sk iX T0 1 y ZodlzwmXp vf q7 W 0 6wR s Q I3 xP 7lmyv/5O9C q Z T /9 elF M 5 R N b I 7 J 021a n u 0 fXSl K i In T +z qk r P N z1 pUn r 3 Ls7 V /0J S vT q W m /G U tVzL 9 O+NS7 pd s/r z OR A o l 8j 0n NLFbKm I y3UKm x fL W I7 z GHT h + 6 CoO cr PE1RwgS qsp H v 4wC O er J p 1b dYt 9e vg3 t mH4=</la t barbar ∆ B b 6 Y J9RCPHS I="> A0i cjVF L wNWZ/y a nUvTXh4 K G R2T W Y dP /ZnXSiL 6u D l 5v4A K +N C b8 M f Y g 0P D hZ H Rs fGJ yan p m eL 3 E4 k W l7 8 u1 C F S+ 2 T O Rp DIK t 9 VFLo B Pw7lkfS 4qz vy5 8 xQ6ru Y csGbA1 dU xmM1 2i U Wo/ Pd 7H Bf s 4 R AQ G IhFC E X k 9 O 3 o x Ug h Sc 2 C 5 9j ml 7M zXV a t w e rL T D JI P q 2w X 93Tr I F b h Ni /f Hl64 U j1E P k n q K DaO78zJy S S Hs GW f / n 3 j U v +m y 5qb 8p 1 M u T 7 0LC d o w2 W s U z 3D G9hE i 7J P cY 8H Fpb 1 r lZ V / S a 2B O 6+QT4gjv< t beat<br>- duration ∆ e 6 4=" Jzb d5 n 1hBY9RCP H ="> A C 0Hi cjVFP L y an U0v TX h4 Ki qG R 6uX D l5L v4A iK+ N /Cb8Y2SMZn f 7b +Y 348 a T J m eLs3E4aZY k nW l 7R8u y1 2I 0 T wQ P X F 3u6br7ORp D w7lkfS 4 I qz vy5 8 DGbA 1 Y dU h K/ Xqx m d P m1Hx Bf s4RA Q G I h FC MXA c9 4 h J C 0tQ F L j O3oxUgS 2 2 l 7M h zX Vm a t w e rL T5 DxJ I tq l nJmzv 2X3T K b e w 9rIF h H 3 lf26F4 U j1EwPknq K rn9S t F CTx G hPHsWf/ 3 y 5 q b 8pW 1 3M u GT 7 0L m W 2 U q4 3 P cY 8H Fpb 1 rlZV/Sa2B3D O gZjv</la t beat<br><!-- End of picture text -->

**Figure 3** : Schematic view of the different audiovisual structural events considered: shots (∆ _shot, lshot_ ), functional music segments ( _lsegment_ ), bars/downbeats (∆ _bar, lbar_ ) and beats (∆ _beat, lbeat_ ). Illustration music video: Psy, _Gangnam Style_ . 

correlation between the duration of the shots and the various musical SEs (beat and bar duration). In our second experiment, we study the temporal co-occurrence of the shot boundaries and the various musical SEs (bar and functional segment boundaries). We analyze the results of those for each music genre and each video genre. 

## **4.2 Dataset** 

For our quantitative study, we consider a subset of the Harmonix dataset [13]. Harmonix was initially released for automatic estimation of beat, downbeat and functional music segments. It features popular (mostly hits) Western music tracks for which there is a high probability of having an associated music video. From the list of 1,000 YouTube video links provided, 899 were successfully retrieved, of which 40% contained only still images and 2.4% were duplicates. As a contribution of this work we provide the list and URLs of the remaining 548 OMVs as well as the genre annotations described below<sup>1</sup> . 

## _4.2.1 Annotations into Structural Events_ 

We consider here two types of Structural Events (SE): those based on the music content -audio-, and those based on video content -image frames over time (see Figure 3). 

**Music SE.** We consider three types of music SEs. At the smallest temporal scale we consider the beats and downbeats; at the largest temporal scale we consider the functional music segment boundaries (between the verses, bridges, choruses). Harmonix features a set of manual annotations<sup>2</sup> . However, these annotations correspond to studio versions of the tracks which can, in some cases, 

> 1 Our list is accessible at: https://gitlab.com/creaminal/publications/ismir2021-language-of-clips/-/blob/master/video_genres.csv. 

> 2 into functional segments, downbeat and beat. 

be largely different from the version used in the OMV. For this reason, we only used the annotations into bpm and meter of the Harmonix dataset to get the beat duration ∆ _beat_ = _bpm_ <u>60</u><sup>andbarduration∆</sup><sup>_bar_=4 or 3∆</sup><sup>_beat_</sup> (which is computed as a multiple of the bar duration using the time signature). For the downbeat positions, we used the algorithm of Böck et al. [23], implemented in the Madmom library [21]. In the following, we denote by _lbar_ the list of downbeat positions for a given track. For the functional music segments, we used the implementation of OLDA from the MSAF library [26]. In the following, we denote by _lsegment_ the list of boundary positions between the segments for a given track. For our dataset, the average duration of functional music segments is 19.73 s. and the average bar duration is 2.30 s. 

**Video SE.** We consider only the least ambiguous video SE, the shot boundaries (or cuts). To detect boundaries between shots, we use the TransNet system [25] and the associated library, available on GitHub<sup>3</sup> . The TransNet output is a continuous function of time _fshot_ ( _t_ ) _∈_ [0 _,_ 1] representing the likelihood of a boundary at time _t_ . _fshot_ has a sampling rate of 25 Hz. 

Also, for each OMV, we compute the histogram of its shot duration. We do so by first estimating the list of shot boundary positions _lshot_ by thresholding _fshot_ ( _t_ ) with _τ_ = 0 _._ 5. The resulting segments have an average duration ∆ _shot_ of 4.76s. We then compute the histogram of these durations. We denote by ∆<sup>max</sup> _shot_<sup>thepositionofthemaxi-</sup> mum of this histogram (in seconds). 

We sum up the various SE in Table 1. 

**Table 1** : Notation associated to each SE considered. 

|**Music**|||
|---|---|---|
|genre<br>funct. segments positions<br>bar duration<br>bar/downbeat positions<br>beat duration|_lsegment_<br>∆_bar_<br>_lbar_<br>∆_beat_|Harmonix annotations<br>OLDA/MSAF<br>Harmonix annotations<br>Madmom<br>Harmonix annotations|
|**Video**|||
|genre<br>shot boundary probability<br>shot boundary positions<br>most common shot duration|_fshot_(_t_)<br>_lshot_<br>∆<sup>max</sup><br>_shot_|Manual annotations<br>TransNet|



## _4.2.2 Annotations into genre_ 

We consider both the genre associated to the music and the one associated to the video. 

**Music genre.** While still controversial in its exact definition [27], music genre is a convenient way to describe musical content. For this reason, it has been and it is still a widely studied topic<sup>4</sup> . For our experiments, we use the music genre annotations provided by the Harmonix dataset metadata. 

**Video genre.** Video genre classification is a much less studied topic. Existing studies focus on a much smaller sets of video genres [32–34]. Only Gillet et al. [2] and 

> 3 https://github.com/soCzech/TransNet 

> 4 It has dedicated challenges [28], and large datasets featuring hundreds of categories [29–31]. 

542 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

Schindler [18] studied the case of OMVs and there is no consensus on their taxonomy of video genres. There is also no annotated dataset for this task. 

We merge [2] and [18] to obtain a set of 5 video categories and and a corresponding single-label dataset. Maxime Pozzi, a professional music video editor, validated our taxonomy during our preliminary interview (see part 3.2.3). One author then manually annotated all 548 video clips of Harmonix into the five following video genres: 

- Performance videos (P): The artist or band are presented performing the song. 74 videos; example: Iron Maiden, _Powerslave_ . 

- Concept/Abstract videos (C): The video illustrates the music metaphorically via a series of abstract shots related to semantics or atmosphere of the song. 227 videos; example: Lady Gaga, _Poker Face_ . 

- Narrative videos (N): The music video has a strong narrative content, with identifiable characters and an explicit chronology. 160 videos; example: Taylor Swift, _Teardrops on My Guitar_ . 

- Dance videos (D): Artists present a rehearsed dance choreography in sync with the music. 62 videos; examples: Sean Paul, _Get Busy_ . 

- Other (O): Other types of music videos, including lyrics videos, animated music videos, etc. 25 videos; example: Train, _Hey, Soul Sister_ . 

## **4.3 Experiments** 

We hypothesize that the music structural events play an important role for the placement of cuts during the video editing. We check this assumption by measuring: 

- if their segment duration are correlated in Section 4.3.1; 

- if their position co-occur in Section 4.3.2. 

According to Gillet [2], the performance of alignmentbased music-video recommendation systems are strongly correlated to the video genre. We therefore differentiate our results by music and video genre. 

## _4.3.1 Comparison between events duration_ 

Our first experiment aims at evaluating to which extent the musical and video events have similar durations. 

To measure this, we compare ∆<sup>max</sup> _shot_<sup>(themostcom-</sup> mon shot duration) with the beat duration ∆ _beat_ and bar duration ∆ _bar_ obtained from the Harmonix annotations. When ∆<sup>max</sup> _shot_<sup>is close to ∆</sup><sup>_bar_, this indicates that a system-</sup> atic change of shots occurs with the same speed as the bar changes. This however does not mean that the changes occur simultaneously (we study this in Section 4.3.2). 

This is for example the case of "Heartless" by Kanye West (see Figure 4 [top]) where the large peak at ∆<sup>max</sup> _shot_<sup>=2.72 s can be explained by the tempo at 88 bpm; or</sup> "Firework" by Katy Perry (see Figure 4 [bottom]) where the large peak at ∆<sup>max</sup> _shot_<sup>=1.93scanbeexplainedbythe</sup> tempo at 124 bpm. 

In our dataset, a synchronization at the bar level (0 _._ 5∆ _bar <_ ∆<sup>max</sup> _shot_<sup>_<_1</sup><sup>_._5∆</sup><sup>_bar_)occursforonefifthof</sup> the clips (95 music videos). Synchronization may also occur at other levels: at the beat level ∆ _beat_ , or the pattern 



<!-- Start of picture text -->
(2.6-2.8) ≈  4 88 bpm60<br>Nb ts<br>11<br>Shot duration (s)<br>(1.8-2.0) ≈  4 60<br>124 bpm<br>20<br>15<br>Nb ots10<br>I<br>16 18<br>Shot duration (s)<br><!-- End of picture text -->

**Figure 4** : [top] Histogram of shot duration in the music video of _Heartless_ by Kanye West. The tempo is 88 bpm. [bottom] Histogram of shot duration in the music video of _Firework_ by Katy Perry. The tempo is 124 bpm. 

level ∆ _pattern_ (usually an even multiple of the bar duration). In our dataset, a synchronization at the beat level (0 _._ 5∆ _beat <_ ∆<sup>max</sup> _shot_<sup>_<_1</sup><sup>_._5∆</sup><sup>_beat_)occursfortwothirdsof</sup> the clips (329 music videos). However, synchronization at pattern level ∆ _pattern_ = 4∆ _bar_ almost never occurs (2 music videos). 

In Table 2, we indicate for each music genre and video genre, the number of tracks for which the ∆<sup>max</sup> _shot_<sup>corre-</sup> spond to ∆ _bar_ or ∆ _beat_ . We only focus here on the most represented genres, i.e. which appear at least 10 times. We observe a strong correspondence between ∆<sup>max</sup> _shot_<sup>and</sup> ∆ _bar_ for the music genres Country, Dance/Electro and Rock (one fourth of the tracks). We observe a strong correspondence between ∆<sup>max</sup> _shot_<sup>and∆</sup><sup>_beat_forthemusic</sup> genres Alternative and Reggaeton (three quarters of the tracks). This may imply, for example, that music video professionals favor more dynamic editing styles (using shorter shots on average) for Reggaton than for Country music. We observe a strong correspondence between ∆<sup>max</sup> _shot_<sup>and ∆</sup><sup>_bar_for the video genre Performance</sup> (one fourth of the tracks). On the contrary, we observe a low correspondence between ∆<sup>max</sup> _shot_<sup>and∆</sup><sup>_beat_forthe</sup> video genre Other (one third of the tracks). It is likely that music videos in the Other category favor experimental editing styles, with shots of more diverse duration. 

As we see, there is a strong relationship between the video events and musical events duration. This however does not mean that the changes occur simultaneously. We study this in the next section. 

## _4.3.2 Comparison between events position_ 

Our second experiment aims at evaluating to what extent the musical events _lseg_ , _lbar_ and video events _fshot_ ( _t_ ) happen simultaneously. To measure this, we compute for each audio boundary _i_ ( _ti ∈ lseg_ or _ti ∈ lbar_ ) a score _Si ∈_ [0 _,_ 1]. 

543 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

**Table 2** : Agreement of musical structure (bar ∆ _bar_ and beat ∆ _beat_ level) and dominant shot duration ∆<sup>max</sup> _shot_<sup>ac-</sup> cording to the **music genre** [top table] and according to the **video genre** [bottom table]. Highest values are highlighted in bold, lowest values in italic. 

||∆<sup>max</sup><br>_shot _<sup>_≃_</sup>|<sup>∆</sup><sup>_bar_</sup>|∆<sup>max</sup><br>_shot _<sup>_≃_</sup>|<sup>∆</sup><sup>_beat_</sup>|
|---|---|---|---|---|
|Music Genre|# tracks|%|# tracks|%|
|Alternative|2|8.3|19|**79.2**|
|Country|10|**29.4**|16|47.1|
|Dance/Electro|12|**24.5**|28|57.1|
|Hip-Hop|12|12.6|69|72.6|
|Pop|40|14.8|158|_58.3_|
|R&B|1|_5.3_|13|68.4|
|Reggaeton|1|8.3|9|**75.0**|
|Rock|4|**23.5**|10|_58.8_|
||∆<sup>max</sup><br>_shot _<sup>_≃_</sup>|<sup>∆</sup><sup>_bar_</sup>|∆<sup>max</sup><br>_shot _<sup>_≃_</sup>|<sup>∆</sup><sup>_beat_</sup>|
|Video Genre|# tracks|%|# tracks|%|
|Concept|33|14.5|148|**65.2**|
|Dance|11|17.7|40|**64.5**|
|Narration|28|17.5|93|58.1|
|Performance|19|**25.7**|41|55.4|
|Other|4|_16.0_|8|_32.0_|



_Si_ is defined as the integral over time of the shot boundary likelihood _fshot_ ( _t_ ) tampered by a non-normalized Gaussian window _w_ ( _t_ ). _w_ ( _t_ ) is centered on _ti_ , with _σ_ = 2 (such that the effective duration of the window is approximately 0.5s at a frame rate of 25Hz) and with _w_ (0) = 1. 



<!-- Start of picture text -->
Si = w ( t − ti ) fshot ( t ) dt, ∀ti ∈{lseg, lbar}<br>� t<br><!-- End of picture text -->

A large value of _Si_ indicates that the _ti_ position (the music structural event) corresponds to a large probability of shot boundary. We then average _Si_ for all audio boundaries _i_ to get _S_ . _S_ might be considered as a measure of precision, since it provides information on _how many audio boundaries are explained by a video boundary_ . It should be noted that the number of video boundaries is larger than the number of audio boundaries (as seen in Figures 1 and 2). _S_ is also close to the measure proposed by [35] to evaluate the performances of beat-tracking algorithms. A large value of _S_ indicates that the shot boundaries are located at the same positions as the music structural events _lseg_ or _lbar_ . We compute _S_ separately using the _ti_ from _lseg_ or from _lbar_ . To check if the amount of music-video event synchronization depends on the music and video genre, we average _S_ over all tracks of a given genre (music or video). 

**Co-occurrence of music/video events by music genre.** Table 3 [top part] shows the co-occurrence scores _S_ aggregated over music genres. We observe variations of the values of _S_ according to the music genre. For Pop, _S_ ( _lseg_ ) is large (0.36) indicating that many shot transitions occur at the functional segment boundaries positions. For R&B and Reggaeton, _S_ ( _lbar_ ) is large (0.31 and 0.28) indicating that many shot transitions occur at the downbeat positions. We also observe that the value of _S_ ( _lseg_ ) and _S_ ( _lbar_ ) vary according to the music genre with very small values for Dance/Electronic, Hip-Hop and Rock. This comes as a surprise especially for Dance/Electronic, because in the previous experiment, we observed a strong correspondence between the duration of shots and bars for this music genre. This shows that even though bars and 

**Table 3** : Shot transition intensity _S_ around music boundaries (either functional segments boundaries _lseg_ or bar boundaries _lbar_ ) according to **music genre** [top table] and according to the **video genre** [bottom table]. Mean values and confidence intervals at 95% are displayed. Highest values are highlighted in bold, lowest values in italic. 

|Music Genre|_S_(_lseg_)|_S_(_lbar_)|# tracks|
|---|---|---|---|
|Alternative|0.22_±_0.08|0.23_±_0.02|24|
|Country|0.20_±_0.06|0.21_±_0.02|34|
|Dance/Electro|_0.18 ± 0.05_|0.21_±_0.02|49|
|Hip-Hop|0.19_±_0.03|0.25_±_0.01|95|
|Pop|**0.36**_±_**0.02**|0.21_±_0.01|271|
|R&B|**0.29**_±_**0.10**|**0.31**_±_**0.03**|19|
|Reggaeton|0.24_±_0.11|**0.28**_±_**0.04**|12|
|Rock|_0.18 ± 0.07_|_0.19 ± 0.03_|17|
|Video Genre|_S_(_lseg_)|_S_(_lbar_)|# tracks|
|Concept|0.20_±_0.02|**0.23**_±_**0.01**|227|
|Dance|**0.18**_±_**0.04**|**0.24**_±_**0.01**|62|
|Narration|**0.18**_±_**0.03**|**0.23**_±_**0.01**|160|
|Performance|_0.15 ± 0.04_|0.16_±_0.01|74|
|Other|_0.11 ± 0.06_|_0.11 ± 0.02_|25|



shots have similar duration, their boundaries might not always co-occur. 

**Co-occurrence of music/video events by video genre.** Table 3 [bottom part] shows the co-occurrence scores _S_ aggregated over video genres. We observe variations of the values of _S_ according to the video genre. We see that the Dance video genre has a large value of _S_ ( _lbar_ ) (0.24), which is not surprising given that video labeled as Dance actually show people dancing on the beat. We also observe large values of _S_ ( _lbar_ ) for the Concept and Narration video genres with consistent synchronization on the downbeats. For the Performance video genre (the band is playing in front of the camera), we don’t observe such a large correspondence ( _S_ ( _lbar_ ) = 0 _._ 16). For the Other video genre, the low values ( _S_ ( _lbar_ ) = _S_ ( _lseg_ ) = 0 _._ 11) are not surprising, given that some videos are very experimental and may feature complex video transitions, which may be difficult to detect by the TransNet. 

## **5. CONCLUSION** 

According to the professionals and to our experiments, official music videos are edited by taking into account the music structure. Although some experts mentioned that synchronization was often a matter of taste and intuition, we were able to bring out some trends. We showed that the co-occurrence of music and video structural events would vary according to the music and video genres. These elements can be reused to design or improve automatic musicvideo recommendation systems. For example, if the task is to recommend an illustration video for a Pop or R&B track, the system is expected to favor candidates that allow high synchronization of the structural events. 

However, we have the intuition that other factors may impact the editing style of OMV. In future work, we plan to investigate the role of other metadata, such as release date, artist popularity or harmonic complexity. Although we focused on OMV for this study, we believe that a similar analysis can be conducted on other types of musical videos, e.g. movies or commercials. 

544 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

## **6. REFERENCES** 

- [1] R. Arandjelovic and A. Zisserman, “Look, Listen and Learn,” in _Proceedings of IEEE ICASSP (International Conference on Computer Vision)_ , Venice, Italy, 2017. 

- [2] O. Gillet, S. Essid, and G. Richard, “On the correlation of automatic audio and visual segmentations of music videos,” _IEEE Transactions on Circuits and Systems for Video Technology_ , vol. 17, no. 3, pp. 347–355, 2007. 

- [3] J.-C. Wang, Y.-H. Yang, I.-H. Jhuo, Y.-Y. Lin, and H.-M. Wang, “The acousticvisual emotion guassians model for automatic generation of music video,” in _Proceedings of ACM Multimedia_ , Nara, Japan, 2012. 

- [4] F.-F. Kuo, M.-K. Shan, and S.-Y. Lee, “Background Music Recommendation for Video Based on Multimodal Latent Semantic Analysis,” in _Proceedings of ICME (International Conference on Multimedia and Expo)_ , San Jose, CA, USA, 2013. 

- [5] J. C. Lin, W. L. Wei, and H. M. Wang, “EMVmatchmaker: Emotional temporal course modeling and matching for automatic music video generation,” in _Proceedings of ACM Multimedia_ , Brisbane, Australia, 2015, pp. 899–902. 

- [6] J. C. Lin, W. L. Wei, J. Yang, H. M. Wang, and H. Y. M. Liao, “Automatic music video generation based on simultaneous soundtrack recommendation and video editing,” in _Proceedings of MMM (International Conference on Multimedia Modeling)_ , Reykjavik, Iceland, 2017. 

- [7] X.-S. Hua, L. Lu, and H.-J. Zhang, “Automatic music video generation based on temporal pattern analysis,” in _Proc. of ACM Multimedia_ , New York City, NY, USA, 2004. 

- [8] J. Wang, E. Chng, and C. Xu, “Fully and SemiAutomatic Music Sports Video Composition,” in _Proceedings of ICME (International Conference on Multimedia and Expo)_ , Toronto, ON, Canada, 2006. 

- [9] J. Wang, E. Chng, C. Xu, Hanqinq Lu, and Q. Tian, “Generation of Personalized Music Sports Video Using Multimodal Cues,” _IEEE Transactions on Multimedia_ , vol. 9, no. 3, 2007. 

- [10] J. S. Downie, “Music Information Retrieval Evaluation eXchange.” [Online]. Available: http://www.music-ir. org/mirex/wiki/MIREX_HOME 

- [11] A. Aner and J. R. Kender, “Video Summaries through Mosaic-Based Shot and Scene Clustering,” in _Proceedings of ECCV (European Conference on Computer Vision)_ , Copenhagen, Denmark, 2002, pp. –. 

- [12] A. Schindler and A. Rauber, “Harnessing musicrelated visual stereotypes for music information retrieval,” _ACM Transactions on Intelligent Systems and Technology_ , vol. 8, no. 2, pp. 1–21, 2016. 

- [13] O. Nieto, M. Mccallum, M. E. P. Davies, A. Robertson, A. Stark, and E. Egozy, “The Harmonix Set: Beats, Downbeats, and Functional Segment Annotations of Western Popular Music,” in _Proceedings of ISMIR (International Conference on Music Information Retrieval)_ , Delft, The Netherlands, 2019. [Online]. Available: https://archives.ismir.net/ismir2019/paper/000068.pdf 

- [14] C. Inskip, A. Macfarlane, and P. Rafferty, “Music, Movies and Meaning: Communication in Filmmakers’ Search for Pre-existing Music, and the Implications for Music Information Retrieval,” in _Proceedings of ISMIR (International Conference on Music Information Retrieval)_ , Philadelphia, PA, USA, 2008. [Online]. Available: https://archives.ismir.net/ ismir2008/paper/000117.pdf 

- [15] O. Gillet, “Transcription des signaux percussifs. Application à l’analyse de scènes musicales audiovisuelles,” Ph.D. dissertation, Ecole Nationale Superieure des Telecommunications, 2007. [Online]. Available: https://pastel.archives-ouvertes.fr/pastel-00002805 

- [16] Ruiduo Yang and M. Brown, “Music database query with video by synesthesia observation,” in _Proceedings of ICME (International Conference on Multimedia and Expo)_ . Taipei, Taiwan: IEEE, 2004, pp. –. 

- [17] P. Mulhem, M. S. Kankanhalli, J. Yi, and H. Hassan, “Pivot vector space approach for audio-video mixing,” _IEEE Multimedia_ , vol. 10, no. 2, pp. 28–40, 4 2003. 

- [18] A. Schindler, “Multi-Modal Music Information Retrieval: Augmenting Audio-Analysis with Visual Computing for Improved Music Video Analysis,” Ph.D. dissertation, Technische Universität Wien, 2019. [Online]. Available: https://arxiv.org/abs/2002.00251 

- [19] A. Schindler and A. Rauber, “On the Unsolved Problem of Shot Boundary Detection for Music Videos,” in _Proceedings of MMM (International Conference on Multimedia Modeling)_ , vol. 11295 LNCS. Thessaloniki, Greece: Springer Verlag, 2019. [Online]. Available: https://link.springer.com/chapter/ 10.1007%2F978-3-030-05710-7_43 

- [20] B. Jia, J. Lv, and D. Liu, “Deep learning-based automatic downbeat tracking: a brief review,” _Multimedia Systems_ , vol. 25, no. 6, 12 2019. 

- [21] S. Böck, F. Korzeniowski, J. Schlüter, F. Krebs, and G. Widmer, “Madmom: A new Python audio and music signal processing library,” in _Proceedings of ACM Multimedia_ , New York City, NY, USA, 2016, pp. 1174–1178. 

- [22] D. Bogdanov, X. Serra, N. Wack, E. Gómez, S. Gulati, P. Herrera, O. Mayor, G. Roma, J. Salamon, and J. Zapata, “ESSENTIA: an Open-Source Libraryfor Sound and Music Analysis,” in _Proceedings of ACM Multimedia_ . New York, NY, USA: ACM Press, 2013. 

545 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

- [23] S. Böck, F. Krebs, and G. Widmer, “Joint Beat and Downbeat Tracking with Recurrent Neural Networks.” in _Proceedings of ISMIR (International Society for Music Information Retrieval Conference)_ , New York City, NY, USA, 2016. [Online]. Available: https://archives.ismir.net/ismir2016/paper/000186.pdf 

- [24] B. McFee and D. P. Ellis, “Learning to segment songs with ordinal linear discriminant analysis,” in _Proceedings of IEEE ICASSP (International Conference on Acoustics, Speech and Signal Processing)_ , Florence, Italy, 2014, pp. 5197–5201. 

- [25] T. Souˇcek, J. Moravec, and J. Lokoˇc, “TransNet: A deep network for fast detection of common shot transitions,” _arXiv preprint arXiv:1906.03363_ , 2019. [Online]. Available: https://arxiv.org/abs/1906.03363 

- [26] O. Nieto and J. P. Bello, “Systematic Exploration Of Computational Music Structure Research.” in _Proceedings of ISMIR (International Conference on Music Information Retrieval)_ , New York City, NY, USA, 2016. [Online]. Available: https://archives.ismir. net/ismir2016/paper/000043.pdf 

   - [33] J. Varghese and K. N. Ramachandran Nair, “A Novel Video Genre Classification Algorithm by Keyframe Relevance,” in _Information and Communication Technology for Intelligent Systems. Smart Innovation, Systems and Technologies_ . Singapore: Springer, 2019, vol. 106. [Online]. Available: https://link.springer. com/chapter/10.1007%2F978-981-13-1742-2_68 

   - [34] K. Choro´s, “Video Genre Classification Based on Length Analysis of Temporally Aggregated Video Shots,” in _Computational Collective Intelligence. Lecture Notes in Computer Science_ . Springer, Cham, 2018, vol. 11056. [Online]. Available: https://link.springer.com/chapter/10.1007% 2F978-3-319-98446-9_48 

   - [35] A. T. Cemgil, B. Kappen, P. Desain, and H. Honing, “On tempo tracking: Tempogram representation and Kalman filtering,” _Journal of New Music Research_ , vol. 29, no. 4, pp. 259–273, 2000. [Online]. Available: https://www.mcg.uva.nl/papers/mmm-26.pdf 

- [27] R. Hennequin, J. Royo-Letelier, and M. R. Moussallam Deezer, “Audio Based Disambiguation of Music Genre Tags,” in _Proceedings of ISMIR (International Conference on Music Information Retrieval)_ , 2018. [Online]. Available: https://archives.ismir.net/ismir2018/paper/000163.pdf 

- [28] M. Defferrard, S. P. Mohanty, S. F. Carroll, and M. Salathé, “Learning to Recognize Musical Genre from Audio,” in _Companion of WWW (The Web Conference)_ , New York City, NY, USA, 2018, pp. –. 

- [29] T. Bertin-Mahieux, D. P. Ellis, B. Whitman, and P. Lamere, “The Million Song Dataset,” in _Proceedings of ISMIR (International Conference on Music Information Retrieval)_ , Miami, FL, USA, 2011. [Online]. Available: https://ismir2011.ismir.net/papers/OS6-1.pdf 

- [30] J. F. Gemmeke, D. P. W. Ellis, D. Freedman, A. Jansen, W. Lawrence, R. Channing Moore, M. Plakal, and M. Ritter, “Audio Set: An Ontology and HumanLabeled Dataset for Audio Events,” in _Proceedings of IEEE ICASSP (International Conference on Acoustics, Speech and Signal Processing)_ , New Orleans, LA, USA, 2017. 

- [31] M. Defferrard, K. Benzi, P. Vandergheynst, and X. Bresson, “FMA: A Dataset for Music Analysis,” in _Proceedings of ISMIR (International Society for Music Information Retrieval Conference)_ , Suzhou, China, 2017. [Online]. Available: https://archives.ismir.net/ ismir2017/paper/000075.pdf 

- [32] J. You, G. Liu, and A. Perkis, “A semantic framework for video genre classification and event analysis,” _Signal Processing: Image Communication_ , vol. 25, no. 4, 2010. 

546 

