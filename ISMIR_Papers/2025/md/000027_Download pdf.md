---
paper_id: "000027"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706381/files/000027.pdf"
---

# A SURVEY ON VISION-TO-MUSIC GENERATION: METHODS, DATASETS, EVALUATION, AND CHALLENGES 

Zhaokai Wang<sup>1</sup> , Chenxi Bao<sup>2</sup> , Le Zhuo<sup>3</sup> , Jingrui Han<sup>4</sup> Yang Yue<sup>5</sup> , Yihong Tang<sup>6</sup> , Victor Shea-Jay Huang<sup>3</sup> , Yue Liao<sup>7</sup> 1Shanghai Jiao Tong University 2Music Tech Lab, DynamiX 3The Chinese University of Hong Kong 4Beijing Film Academy 5Tsinghua University 6McGill University 7National University of Singapore `wangzhaokai@sjtu.edu.cn {cloudingcxb17,zhuole1025,liaoyue.ai}@gmail.com` 

## ABSTRACT 

Vision-to-music generation, including video-to-music and image-to-music tasks, is a significant branch of multimodal artificial intelligence demonstrating vast applications like film scoring and short video creation. However, research in vision-to-music is still in its preliminary stage due to its complex internal structure and the difficulty of modeling dynamic relationships with video. To the best of our knowledge, existing surveys focus on general music generation without comprehensive discussion on visionto-music. In this paper, we systematically review the research progress in the field of vision-to-music generation. We first analyze the technical characteristics and core challenges for three input types: general videos, human movement videos, and images, as well as two output types of symbolic music and audio music. We then summarize the existing methodologies from the architecture perspective. A detailed review of common datasets and evaluation metrics is provided. Finally, we discuss current challenges and future directions. We hope our survey can inspire further innovation in vision-to-music generation and the broader field of multimodal generation in academic research and industrial applications. 

## 1. INTRODUCTION 

Recent advances in multimodal artificial intelligence have witnessed substantial progress in generating and understanding content for modalities like text, images, video, and speech [1–7]. Music generation, as an important part of this multimodal ecosystem, has also seen remarkable development. Among the various music generation tasks (e.g. unconditional music generation [8, 9] and textto-music generation [10, 11]), vision-to-music, including video-to-music and image-to-music generation, has garnered particular interest due to its practical applications in film scoring, short video platforms, and music accompa- 

> © Authors. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: Authors, “A Survey on Vision-to-Music Generation: Methods, Datasets, Evaluation, and Challenges”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

niment. For general users, automatically generated background music can alleviate copyright concerns and reduce the time spent searching for suitable music. For professional composers, AI-assisted music composition can streamline the iterative process of matching a score to visual content, expediting the communication cycle with directors and producers. 

Despite this demand, the development of vision-tomusic remains relatively preliminary. For academic research, the inherent challenges ranging from aligning rich visual cues with musical structure to handling the multifaceted nature of music generation contribute to the task’s high complexity, making it more difficult than the common text-to-music task [10–12]. Although a growing number of works have emerged in recent years [13–18], they are still far from meeting the diverse requirements of real-world scenarios. For industrial integration, while other AI-generated content (AIGC) fields, such as text-toimage [19–21] and text-to-video [22,23], have experienced rapid adoption in both professional and consumer contexts, vision-to-music systems have yet to see broad industrial deployment, with only pilot products like Tianpuyue AI<sup>1</sup> . The unique demands of film scoring, which often require precise emotional and temporal synchronization with visual storytelling, heighten the difficulty of achieving robust and artistically consistent results through AI methods. 

To the best of our knowledge, although existing works provide reviews on general music generation [24–28], there lack surveys focusing on the vision-to-music generation task. Given the above gaps, we aim to provide a comprehensive survey on vision-to-music generation. We provide a timeline of representative works in Fig. 1, and an overview of vision-to-music generation in Fig. 2. 

The subsequent sections of this paper are organized as follows: Sec. 2 introduces the fundamentals of visionto-music generation, analyzing the technical characteristics and core challenges of three major scenarios: general videos, human movement videos, and images. Sec. 3 reviews current vision-to-music methods, comparing innovations and limitations in vision encoding, vision-music projection, and music generation module design. Sec. 4 discusses recent vision-to-music datasets. Sec. 5 introduces 

> 1 https://www.tianpuyue.cn/video2music 

223 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
CMT MeLFusion VEH<br>Foley Music V2Meow Diff-BGM MuVi FilmComposer<br>Dance2music MuMu-LLaMA VidMuse SONIQUE AudioX<br>RhythmicNet Video2Music Mozart’s Touch VidMusician GVMGen<br>V-MusProd EIMG VMAS MTM XMusic<br>2020-2022 2023.12 2024.9 2024.12 2025.3<br><!-- End of picture text -->

Figure 1: Timeline of representative works in vision-to-music generation. 

evaluation metrics, categorized their purposes (music-only and vision-music correspondence) and approaches (objective and subjective). Sec. 6 discusses the current research status and existing challenges. Through this work, we aspire to inspire further innovation in vision-to-music generation and the broader field of multimodal learning communities, driving progress in both academic research and industrial applications of vision-to-music generation. 

## 2. FUNDAMENTALS 

In the broad multimodal research community, music is often treated as a subset of audio [8, 22, 29–33]. However, unlike general audio which may include background noise, speech, or sound effects, music embodies intricate internal structures and richness of information, including harmony, counterpoint, and instrumentation. These complexities make it essential to consider music as an independent modality, which sets the stage for exploring visionto-music generation. 

When delving into this specific area, we first need to recognize the unique relationship between visual input and musical output. We analyze the characteristics of three input types in vision-to-music generation: general videos, human movement videos, and images, and two output types: symbolic music and audio music. This categorization helps us better understand the current state and challenges of the field. 

## 2.1 Input Types 

General Videos. This includes a wide range of video contents, such as natural landscapes, films, sports, animations, etc. Techniques in this category typically focus on extracting features like motion, color, or visual semantics to create music that aligns with the visual narrative. 

Images. Approaches in this domain focus on transforming static images into music. Since images lack temporal semantics and rhythm, these methods usually only need to focus on the overall style, and there is no strict requirement for the duration of the generated music. The application scenarios for image-to-music are not as extensive as video-to-music, but they include functionalities like creat- 

ing musical memories for photo albums. This type of pair data is easy to collect, but its inherent correlation may not be very strong. 

Human Movement Videos. These videos typically include dance, sports, instrument performances, and other human movements. For instrument performance videos, where humans play music instruments but the audio is removed, the music is determined by the input video to some extent, and the generation process is similar to reconstructing music from the silent videos. For dance, sports, and other human movements, they emphasize rhythmic alignment (especially local rhythm) more than general videos, while semantic constraints are generally weaker, requiring only overall style matching. Therefore, extracted 2D/3D keypoints representing human motion are often directly used as inputs instead of raw videos. 

In the remaining sections, we will mainly focus on general videos and images, while paying relatively less attention to human movement videos. This is because they focus on rhythmic relations and the semantic association with music is relatively weak, where 2D body keypoints are directly used as video features. Their application scenarios are also relatively limited [13]. 

## 2.2 Output Types 

Symbolic Music. Symbolic music is represented as discrete elements like notes, chords, or sequences of musical symbols [25]. Most early vision-to-music methods are symbolic [13, 15, 34, 35]. Symbolic music can incorporate music theory, such as chords, and generate longer pieces with good controllability. However, the limited data availability restricts its scalability to large models, and the expressive and emotional depth is constrained by soundfonts. Audio Music. Such methods aim to generate music in its audio form [14, 16–18, 36–39], often employing generative models such as transformers [40], VAEs, GANs [41], or diffusion models [42] to synthesize realistic sound from the visual input. Audio music benefits from large-scale datasets for training, enabling end-to-end generation with rich expressiveness and performance. However, despite efforts of adding controls in audio generation [43], the controllability of audio music is still relatively weak, com- 

224 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
1 Vision-to-Music Generation<br>Datasets Architecture Evaluation<br>_<br>GeneralVideos Motion Videos Images EncodingVision Vision-MusicProjection GenerationMusic objective 国 FAD, FD, KL, …Music-only CorrespondenceImageBind Score,CLAP Score, …Vision-music<br>Input CLIP Adaptor Diffusion subjective 心 Melody, Rhythm, Overall, … Emotion, Overall, ...Semantic, Rhythm,<br>Types Video Text +noise<br>CLIP Challenges<br>Symbolic Music Audio Music …… 101 Feature Auto-Regressive Standardized Dataset and Benchmark<br>Customization and Controllability<br>Output<br>Types Choice of Symbolic or Audio Forms<br>Modeling Vision-Music Relationships (Semantic, Rhythm)<br><!-- End of picture text -->

Figure 2: Overview of vision-to-music generation. 

pared to symbolic music where multiple control signals can be used, e.g. pitch, duration, instrument, rhythm, chord, etc. Moreover, the generated music is typically shorter due to sampling rate limitations, e.g. usually under 20 seconds for methods in Tab. 1, where symbolic methods can easily achieve whole-song length. 

## 3. METHODS 

In this section, we discuss the existing works on vision-tomusic generation. We summarize vision-to-music generation methods in Tab. 1. 

## 3.1 Tasks 

We begin by categorizing the methods based on the input types outlined in Sec. 2. 

General Video-to-Music. Early general video-to-music methods were usually symbolic [13, 15, 34, 35]. With the development of audio-form music generation [11, 12], a large number of audio-based general video-to-music works have emerged in the past few years [16–18, 36–39, 44–46]. Image-to-Music. Early image-to-music works were also primarily symbolic [47–50], where models analyze color, texture, and semantic content to generate music. Recent works [16, 38, 51, 52] generated audio-form music from multiple modalities (video, image, and text). 

Human Movement Video-to-music. For dance or sports videos, existing methods focus on extracting rhythmic patterns from dance videos and mapping them to musical rhythm generation [31, 53–59]. For music performance videos, current methods learn to reconstruct the original music from the silent videos [60–63]. 

## 3.2 Architecture 

The architecture of vision-to-music systems can be broken down into three major components: vision encoding, vision-music projection, and music generation. Vision Encoding. This stage is focused on extracting features from the input video or image. A commonly used vision encoder is CLIP [66], which is pretrained on massive image-text pairs to achieve open-domain visual 

understanding capabilities. Video understanding backbones [64,70,78,85,88,92,98] are also used to extract spatiotemporal features. Some also use additional encoders for color information [15], emotion information [46], or intermediate text features [37]. For human movement videos, it is important to extract motion features for rhythmic alignment, e.g., directly calculating first-order difference from human keypoints as motion velocity [31, 53], or using pre-trained motion encoder [14, 54]. 

Vision-Music Projection. This component involves mapping the visual features into the music space. Most methods directly use the visual features as the input of the music generation model, or through simple cross-attention mechanisms [15, 35, 37, 52]. Some methods design specialized adapters [16, 17, 36] for better feature alignment, e.g. to capture temporal-related or local features. Besides using feature-based mapping, some studies suggest using text as an intermediate representation of the visual features [18, 38, 44, 87] and subsequently utilizing text-tomusic models for music generation. Some symbolic music generation methods use symbolic elements as the visionmusic mapping [13, 99]. 

Music Generation. Once the visual and music features have been aligned, the next step is to generate the musical output. This stage can be tackled using auto-regressive or diffusion-based generative models. Auto-regressive models [40] can be used for both symbolic [13, 15, 99] and audio music generation [17, 18, 37, 39, 44, 45]. Diffusion models [42, 86] can be used for symbolic [35] music to directly generate piano rolls, but mostly for audio music [12, 38, 46, 101]. 

## 3.3 Vision-Music Relationships 

Vision-music relationships establish the correspondence between videos and music. Unlike the vision-music projection discussed in the previous section (which focuses on the architecture), the relationships discussed here focus on the overall correspondence between input and output. These relationships can be broadly classified into two categories: semantic relationships and rhythmic relationships. Semantic Relationships. This type of relationship focuses on how visual elements (such as color, objects, or scenes) 

225 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

Table 1: Methods for vision-to-music generation. Sem: Semantics. Rhy: Rhythm. AR: Auto-regressive. Diff.: Diffusion. 

|Method|Demo|Date|Input Type|Modality|Music<br>Length|Vision-Music<br>Relationships|Vision Encoding|Vision-Music<br>Projection|Music Generation|
|---|---|---|---|---|---|---|---|---|---|
|▼General Videos and Image|s:|||||||||
|CMT [13]|Link|2021/11|General Video|Symbolic|3min|Rhy|-|Elements|AR (CP [9])|
|V-MusProd [15]|Link|2022/11|General Video|Symbolic|6min|Sem, Rhy|CLIP2Video [64], Histogan [65]<br>|Feature|AR (CP [9])|
|V2Meow [14]|Link|2023/05|General Video|Audio|10sec|Sem, Rhy|CLIP [66], I3D Flow [67],<br>ViT-VQGAN [68]|Feature|AR|
|MuMu-LLaMA [51]<br>(M<sup>2</sup>UGen [16])|Link|2023/11|General Video, Image|Audio|30sec|Sem|ViT [69], ViViT [70]|Adapter|AR (LLaMA2 [71])|
|Video2Music [34]|Link|2023/11|General Video|Symbolic|5min|Sem, Rhy|CLIP [66]|Feature|AR|
|EIMG [72]|Link|2023/12|Image|Symbolic|15sec|Sem|ALAE [73],β-VAE [74], VQ-VAE [75]|Adapter|VAE (FNT [76], LSR [77])|
|Diff-BGM [35]|Link|2024/05|General Video|Symbolic|5min|Sem|VideoCLIP [78]|Feature|Diff. (Polyffusion [79])|
|Mozart’s Touch [44]|Link|2024/05|General Video, Image|Audio|10sec|Sem|BLIP [80]|Text|AR (MusicGen [11])|
|MeLFusion [52]|Link|2024/06|Image|Audio|10sec|Sem|DDIM [81] + T2I LDM [82]|Feature|Diff.|
|VidMuse [17]|Link|2024/06|General Video|Audio|20sec|Sem|CLIP [66]|Adapter|AR (MusicGen [11])|
|S2L2-V2M [83]|Link|2024/08|General Video|Audio|10sec|Sem|Enhanced Video Mamba|Adapter|AR (LLaMA2 [71])|
|VMAS [45]|Link|2024/09|General Video|Audio|10sec|Sem, Rhy|Hiera [84]|Feature|AR|
|MuVi [36]|Link|2024/10|General Video|Audio|20sec|Sem, Rhy|VideoMAE V2 [85]|Adapter|Diff. (DiT [86])|
|SONIQUE [87]|Link|2024/10|General Video|Audio|20sec|Sem, Rhy|Video-LLaMA [88], CLAP [89]|Text|Diff. (Stable Audio [90])|
|VEH [91]|-|2024/10|General Video|Symbolic|30sec|Sem|VideoChat [92]|Text|AR (T5 [93])|
|M2M-Gen [94]|Link|2024/10|Image (Manga)|Audio|1min|Sem|CLIP [66], GPT-4 [1]|Text|AR (MusicLM [95])|
|HPM [46]|Link|2024/11|General Video|Audio|10sec|Sem|CLIP [66], TAVAR [96], WECL [97]|Feature|Diff. (AudioLDM [29])|
|VidMusician [37]|Link|2024/12|General Video|Audio|30sec|Sem, Rhy|CLIP [66], T5 [93]|Adapter|AR (MusicGen [11])|
|MTM [38]|Link|2024/12|General Video, Image|Audio|30sec|Sem|InternVL2 [98]|Text|Diff. (Stable Audio Open [12])|
|XMusic [99]|Link|2025/01|General Video, Image|Symbolic|20sec|Sem, Rhy|ResNet [100], CLIP [66]|Elements|AR (CP [9])|
|GVMGen [39]|Link|2025/01|General Video|Audio|15sec|Sem|CLIP [66]|Adapter|AR (MusicGen [11])|
|AudioX [101]|Link|2025/03|General Video|Audio|10sec|Sem|CLIP [66]|Feature|Diff. (Stable Audio Open [12])|
|FilmComposer [18]|Link|2025/03|General Video|Audio|15sec|Sem, Rhy|Controllable Rhythm Transformer,<br>GPT-4v [1], Motion Detector|Text|AR (MusicGen [11])|
|▼Human Movement Videos:||||||||||
|Audeo [61]|Link|2020/06|Performance Video|Symbolic|30sec|Rhy|ResNet [100]|Feature|GAN|
|Foley Music [62]|Link|2020/07|Performance Video|Symbolic|10sec|Rhy|2D Body Keypoints|Feature|AR|
|Multi-Instrucment Net [60]|-|2020/12|Performance Video|Audio|10sec|Rhy|2D Body Keypoints|Feature|VAE|
|RhythmicNet [53]|Link|2021/06|Dance Video|Symbolic|10sec|Rhy|2D Body Keypoints|Feature|AR (REMI [102])|
|Dance2Music [57]|Link|2021/07|Dance Video|Symbolic|12sec|Rhy|2D Body Keypoints|Feature|AR|
|D2M-GAN [54]|Link|2022/04|Dance Video|Audio|2sec|Rhy|2D Body Keypoints, I3D [103]|Feature|GAN|
|CDCD [55]|Link|2022/06|Dance Video|Audio|2sec|Rhy|2D Body Keypoints, I3D [103]|Feature|Diff.|
|LORIS [31]|Link|2023/05|Movement Video|Audio|50sec|Rhy|2D Body Keypoints, I3D [103]|Feature|Diff.|
|VisBeatNet [56]|-|2024/01|Dance Video|Symbolic|Realtime|Rhy|2D Body Keypoints|Feature|AR|
|UniMuMo [104]|Link|2024/10|Dance Video|Audio|10sec|Rhy|2D Body Keypoints|Feature|Diff.|



relate to musical components (such as mood, melody, or chords). For music performance videos, the music is determined by the video instead of a general and implicit semantic relationship [61, 62]. For dance and movement videos, the semantics in the video is not utilized. Symbolic methods [15,34,99] explicitly define semantic, color, and emotion relationships extracted from pretrained models to utilize the controllability of symbolic music. Recent audio-based methods generally use a single vision encoder to extract semantic features. These semantic features are usually global and insensitive to semantic changes within the video. Some methods [17, 36, 39] also design special modules to enhance local semantic correspondence. However, for most audio methods generating 10-second music, the concept of “local” may not have a significant impact. 

Rhythmic Relationships. Rhythmic relationships mainly refer to the correspondence between the rhythm of the video (e.g. local movements, scene transitions, global video rhythm) and the rhythm of the music (e.g. local beats, global tempo). For human movement videos, such as dance or instrument playing, rhythmic relationships become significant, especially the correspondence between local rhythm and human movements. For general videos, early works [13–15, 45] use optical flow or RGB Difference to represent the video rhythm. Recent works mostly do not consider rhythm information or use frame-by-frame semantic features to implicitly provide local rhythm cor- 

respondence [17, 37], which is not prominent in the generated music. In methods that use text for vision-music projection [38, 87], the video content is used to generate requirements for musical rhythm, such as the rhythm of each scene or the overall tempo. 

## 4. DATASETS 

In this section, we introduce common datasets for visionto-music. Plenty of datasets have been proposed in the literature of the vision-to-music field, and different methods often use different datasets for training and testing. Therefore, it is necessary to organize and analyze these datasets. Common datasets are listed in Tab. 2. 

## 4.1 Input Categories 

Based on the types of videos/images in vision-music datasets, we categorize the datasets as follows: General Videos. Videos in these datasets are usually sourced from platforms like YouTube. Most datasets focus on Music Videos [15, 34, 35, 45, 105, 107], as they have satisfactory video-music alignment and are easier to collect. Other datasets include a variety of video types, such as trailers, advertisements, animations, and documentaries [17, 37], or subsets from larger datasets like AudioSet [108]. These videos offer better diversity, but the video-music alignment may be weaker, requiring strict fil- 

226 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

Table 2: Datasets for vision-to-music generation. 

|Dataset|Access|Date|Source|Modality|Size|Total Length<br>(hour)|Avg. Length<br>(second)|Annotations|
|---|---|---|---|---|---|---|---|---|
|▼General Videos:|||||||||
|HIMV-200K [105]|Link|2017/04|Music Video (Youtube-8M [106])|Audio|200K|-|-|-|
|MVED [107]|Link|2020/09|Music Video|Audio|1.9K|16.5|30|Emotion|
|SymMV [15]|Link|2022/11|Music Video|MIDI, Audio|1.1K|76.5|241|Lyrics, Genre, Chord,<br>Melody, Tonality, Beat|
|MV100K [14]|-|2023/05|Music Video (Youtube-8M [106])|Audio|110K|5000|163|Genre|
|MusicCaps [95]|Link|2023/01|Diverse Videos (AudioSet [108])|Audio|5.5K|15.3|10|Genre, Caption, Emotion,<br>Tempo, Instrument, Rhythm, ...|
|EmoMV [109]|Link|2023/03|Music Video (MVED [107], AudioSet [108])|Audio|6K|44.3|27|Emotion|
|MUVideo [16]|Link|2023/11|Diverse Videos (Balanced-AudioSet [108])|Audio|14.5K|40.3|10|Instructions|
|MuVi-Sync [34]|Link|2023/11|Music Video|MIDI, Audio|784|-|-|Scene Offset, Emotion, Motion, Semantic,<br>Chord, Key, Loudness, Density, ...|
|BGM909 [35]|Link|2024/05|Music Video|MIDI|909|-|-|Caption, Style, Chord, Melody, Beat, Shot|
|V2M [17]|-|2024/06|Diverse Videos|Audio|360K|18000|180|Genre|
|DISCO-MV [45]|-|2024/09|Music Video (DISCO-10M [110])|Audio|2200K|47000|77|Genre|
|FilmScoreDB [46]|-|2024/11|Film Video|Audio|32K|90.3|10|Movie Title|
|DVMSet [37]|-|2024/12|Diverse Videos|Audio|3.8K|-|-|-|
|HarmonySet [111]|Link|2025/03|Diverse Videos|Audio|48K|458.8|32|Description|
|MusicPro-7k [18]|Link|2025/03|Film Video|Audio|7K|-|-|Description, Melody, Rhythm Spots|
|▼Human Movement Videos|||||||||
|URMP [112]|Link|2016/12|Performance Video|MIDI, Audio|44|1.3|106|Instruments|
|MUSIC [113]|Link|2018/04|Performance Video|Audio|685|45.7|239|Instruments|
|AIST++ [114]|Link|2021/01|Dance Video (AIST [115])|Audio|1.4K|5.2|13|3D Motion|
|TikTok Dance-Music [54]|Link|2022/04|Dance Video|Audio|445|1.5|12|-|
|LORIS [31]|Link|2023/05|Dance Video, Sports Video<br>(AIST [115], FisV [116], FS1000 [117])|Audio|16K|86.43|19|2D Pose|
|▼Images|||||||||
|Music-Image [118]|Link|2016/07|Image (Music Video)|Audio|22.6K|377|60|Lyrics|
|Shuttersong [119]|Link|2017/08|Image (Shuttersong App)|Audio|586|-|-|Lyrics|
|IMAC [120]|Link|2019/04|Image (FI [121])|Audio|3.8K|63.3|60|Emotion|
|MUImage [16]|Link|2023/11|Image (Balanced-AudioSet [108])|Audio|14.5k|40.3|10|Instructions|
|EIMG [72]|Link|2023/12|Image (IAPS [122], NAPS [123])|MIDI|3K|12.5|15|VA Value|
|MeLBench [52]|Link|2024/06|Image (Diverse Videos)|Audio|11.2K|31.2|10|Genre, Caption|



tering [16,95]. FilmScoreDB and MusicPro-7k [18,46] focus on film scores, where the music has a deeper semantic correspondence with the video and serves as an accompaniment rather than being the primary focus, as in music videos. Recently, some datasets also provide textual descriptions of videos and music [38, 111, 124] to assist textbridged video-to-music generation methods. 3. Human Movement Videos. These videos can be divided into instrument performances and dance/sport categories. Instrument performance datasets [112, 113] aim to reconstruct music from instrumental performance videos. Dance/sport datasets [31,54,114] focus on generating music from dance or sports videos, emphasizing local rhythmic alignment while downplaying semantic relationships. 

Images. Existing image-to-music datasets are relatively scarce. Sources of the images are usually frames from music videos [52,118] or existing image datasets [16,72,120]. 

## 4.2 Music Domains 

Vision-music datasets can be divided into MIDI and audio based on the music modality. MIDI datasets [15, 34, 35] are created by transcribing audio into the MIDI format or sourced from existing music-only datasets [125]. Audio datasets contain only raw audio files. 

Compared to audio datasets, MIDI datasets have the following advantages: (1) More annotations like Chord, Melody, Beat, Tonality, etc; (2) Longer average duration enables generating longer music pieces; (3) Suitable for training both symbolic and audio music generation models. However, a significant limitation of MIDI datasets is 

their smaller scale (e.g. 1K songs, 100 hours vs. 100K-2M songs, 5K-50K hours) and relatively limited diversity. 

## 5. EVALUATION 

Common metrics for vision-to-music are categorized in Tab. 3 and 4. The evaluation of vision-to-music generation can be divided into two categories: objective and subjective. Objective evaluation uses fixed rule-based algorithms or existing models to extract features and calculate musical metrics. It is relatively objective and convenient for fair comparison, but has certain biases and cannot cover all aspects of music generation, often differing significantly from human subjective perception. Similar to other generation tasks [126, 127], subjective evaluation is typically used in vision-to-music generation for a more comprehensive assessment, i.e. conducting user studies where participants rate/compare music generated by different models. 

From another perspective, metrics can be divided into music-only and vision-music correspondence based on assessment purposes. The former only evaluates whether the music itself is pleasant/realistic/structurally complete, etc., while the latter focuses on the correspondence between the music and the visual input. 

For music-only objective metrics, symbolic music generation methods [13, 15, 35, 72, 83, 99] use some statistics-based methods to calculate certain pitch or rhythm-related statistical metrics of MIDI, such as Scale Consistency, Pitch Entropy, etc. These metrics are usually compared with ground truth music, and the closer they are, the more realistic the music is considered. Audio music 

227 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

Table 3: Objective metrics of vision-to-music generation. M: MIDI. A: Audio. V: Video. I: Image. T:Text. Pit: Pit. Rhy: Rhythm. Fid: Fidelity. Sem: Semantic. 

|Metric|Used in Paper|Input|Type|
|---|---|---|---|
|▼Music-only:||||
|Scale Consistency|[15,83]|M|Pit|
|Pit Entropy|[15,72,83]|M|Pit|
|Pit Class Histogram Entropy|[13,15,35,83,99]|M|Pit|
|Empty Beat Rate|[15,83,99]|M|Rhy|
|Average Inter-Onset Interval|[15,83]|M|Rhy|
|Grooving Pattern Similarity|[13,35,99]|M|Rhy|
|Structure Indicator|[13,35]|M|Rhy|
|Frechet Audio Distance (FAD)|[14,16–18,36,39,52]<br>[44–46,83,91,101]|A|Fid|
|Frechet Distance (FD)|[14,17,36–38,52,87,101]|A|Fid|
|Kullback-Leibler Divergence (KL)|[14,16–18,36–39,44–46]<br>[52,83,87,91,101]|A|Fid|
|Beats Coverage Score (BCS)|[36,46]|A|Rhy|
|Beats Hit Score (BHS)|[36,46]|A|Rhy|
|Inception Score (IS)|[36,46,101]|A|Fid|
|▼Vision-music Correspondence:||||
|ImageBind Score/Rank|[16–18,37,38,44,83,101]|A,V/I|Sem|
|CLAP Score|[37,87,91]|A,A/T|Sem|
|Video-Music CLIP Precision|[15,83]|A,V|Sem|
|Video-Music Correspondence|[35]|A,V|Sem|
|Cross-modal Relevance|[39]|A,V|Sem|
|Temporal Alignment|[39]|A,V|Rhy|
|Rhythm Alignment|[37]|A,V|Rhy|



generation methods widely adopt metrics such as Frechet Audio Distance (FAD), Frechet Distance (FD)<sup>2</sup> , and Kullback Leibler Divergence (KL) to evaluate the similarity between generated music and ground truth music. Some methods [36,46] also introduce metrics like BCS and BHS to measure rhythmic similarity based on music beats. 

Objective metrics for vision-music correspondence usually focus on the audio modality. The most commonly used are ImageBind Score/Rank and CLAP score, which leverage pretrained multimodal models like ImageBind [131] and CLAP [89] for similarity evaluation. Some methods [15,35,39,83] have also designed specific visionmusic retrieval evaluation metrics, with slight differences in model selection and retrieval methods. Additionally, GVMGen [39] and VidMusician [37] have designed objective metrics to evaluate the rhythmic correspondence between visions and music. However, since the pretrained models are usually trained with general audio data instead of specified music data, these objective metrics commonly do not perfectly align with human judgments. 

Subjective metrics mainly include MOS (generally using a 5-point Likert scale), pair preference (i.e. win rate), and ranking different music. Common subjective metrics in vision-to-music generation are given in Tab. 4. The selection of specific subjective metrics depends on the vision-music relationship emphasized by the method. 

## 6. CHALLENGES 

Despite advances in vision-to-music generation, we identify several key challenges for the academic community: Lack of Standardized Objective Datasets and Benchmarks: The training and evaluation datasets differ across 

> 2 The difference between FAD and FD is the feature extractor: FAD [128] uses VGGish [129], while FD uses PANNs [130]. 

Table 4: Subjective metrics of vision-to-music generation. 

|Metric|Used in Paper|
|---|---|
|▼Music-only:||
|Music Melody|[15,35]|
|Music Rhythm|[15,35]|
|Music Richness|[39,99]|
|Audio Quality|[17,36]|
|Overall Music Quality|[13,14,17,18,34,38,39,44,45,52,91,94]|
|▼Vision-music Correspon|dence:|
|Semantic Consistency|[15,18,35–38]|
|Rhythm Consistency|[15,18,34,35,38,91,99]|
|Emotion Consistency|[38,91,99]|
|Overall Correspondence|[13–18,34,39,44,45,52,83,87,94]|



models, sometimes leading to comparisons between models fine-tuned on proprietary datasets and those evaluated via zero-shot inference on other datasets. This disparity significantly undermines the fairness of model comparisons and makes it challenging to identify the state-of-theart. Besides, current evaluation metrics often do not align with actual human perception, e.g. FAD and KL are based on general audio data rather than on music-specific data, and symbolic metrics are statistically based and exhibit low correlation with human preferences. Though most papers provide demos for qualitative comparisons, they are prone to issues such as cherry-picked examples, insufficient sample size, and subjectivity in evaluating the outputs. Limited Customization and Controllability: Most existing models function as black boxes, making it challenging to personalize or control attributes of the generated music, such as style, instrumentation, and rhythm. This significantly affects the models’ practical applicability. 

Trade-off Between Symbolic and Audio Forms: As discussed in Sec. 2, audio-based methods benefit from largescale data but generally offer limited controllability and are constrained by the computational cost of high-fidelity generation, often resulting in shorter musical pieces. In contrast, symbolic approaches, while limited by available data, offer better controllability and can produce longer compositions. A promising direction is to combine symbolic and audio methods to achieve a better trade-off. 

Beyond academic challenges, exploring how to align these technologies with music industry applications (such as film and game scoring) and end-user products (like short-video platform background music) in consumer products offers significant commercial opportunities. 

## 7. CONCLUSION 

In this paper, we review the recent advancements in visionto-music generation, covering both symbolic and audiobased approaches. We identified key technical challenges in visual feature extraction, cross-modal projection, and music generation, and discussed the limitations in current datasets and evaluation metrics. We believe that addressing these challenges will pave the way for future research and applications on vision-to-music generation. 

228 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 8. ETHICAL STATEMENT 

This work is conducted with a clear awareness of the ethical challenges associated with vision-to-music generation technologies. As models learn to translate visual inputs—such as images, videos, or artworks—into music, they operate at the intersection of multiple cultural, legal, and emotional domains. One major concern is copyright infringement, particularly when models are trained on copyrighted music that closely resemble existing compositions without clear attribution or licensing. Given the creative and expressive nature of music, even stylistic mimicry may raise legal and ethical questions. 

In addition, these models risk amplifying cultural or stylistic biases present in the training data. For example, models trained primarily on western classical or pop music may marginalize non-western musical traditions or underrepresent diverse emotional and cultural expressions. The alignment between visual input and musical output can further reinforce problematic stereotypes or fail to capture culturally appropriate interpretations, especially when visual content carries religious or political significance. 

A third dimension involves emotional appropriateness. Music is a powerful emotional medium. Generating music from sensitive or traumatic visual content—such as scenes of violence, grief, or historical trauma—may result in emotionally discordant or insensitive outcomes. 

To mitigate these risks, we advocate for transparent data collection practices, inclusion of diverse musical and visual cultures, and evaluation frameworks that assess not only perceptual quality but also cultural and emotional alignment. We further encourage interdisciplinary collaboration between technologists, musicians, ethicists, and legal scholars to ensure the responsible development and deployment of these systems. 

## 9. REFERENCES 

- [1] J. Achiam, S. Adler, S. Agarwal, L. Ahmad, I. Akkaya, F. L. Aleman, D. Almeida, J. Altenschmidt, S. Altman, S. Anadkat et al., “Gpt-4 technical report,” arXiv preprint arXiv:2303.08774, 2023. 

- [2] H. Zhang, X. Li, and L. Bing, “Video-llama: An instruction-tuned audio-visual language model for video understanding,” arXiv preprint arXiv:2306.02858, 2023. 

- [3] G. Luo, X. Yang, W. Dou, Z. Wang, J. Liu, J. Dai, Y. Qiao, and X. Zhu, “Mono-internvl: Pushing the boundaries of monolithic multimodal large language models with endogenous visual pre-training,” arXiv preprint arXiv:2410.08202, 2024. 

- [4] X. Wang, X. Zhang, Z. Luo, Q. Sun, Y. Cui, J. Wang, F. Zhang, Y. Wang, Z. Li, Q. Yu et al., “Emu3: Next-token prediction is all you need,” arXiv preprint arXiv:2409.18869, 2024. 

- [5] Z. Wang, X. Zhu, X. Yang, G. Luo, H. Li, C. Tian, W. Dou, J. Ge, L. Lu, Y. Qiao, and J. Dai, “Parameter- 

inverted image pyramid networks for visual perception and multimodal understanding,” arXiv preprint arXiv:2501.07783, 2025. 

- [6] Y. Tang, A. Qu, Z. Wang, D. Zhuang, Z. Wu, W. Ma, S. Wang, Y. Zheng, Z. Zhao, and J. Zhao, “Sparkle: Mastering basic spatial capabilities in vision language models elicits generalization to composite spatial reasoning,” arXiv preprint arXiv:2410.16162, 2024. 

- [7] B. Kang, Y. Yue, R. Lu, Z. Lin, Y. Zhao, K. Wang, G. Huang, and J. Feng, “How far is video generation from world model: A physical law perspective,” arXiv preprint arXiv:2411.02385, 2024. 

- [8] Z. Borsos, R. Marinier, D. Vincent, E. Kharitonov, O. Pietquin, M. Sharifi, D. Roblek, O. Teboul, D. Grangier, M. Tagliasacchi et al., “Audiolm: a language modeling approach to audio generation,” IEEE/ACM transactions on audio, speech, and language processing, vol. 31, pp. 2523–2533, 2023. 

- [9] W.-Y. Hsiao, J.-Y. Liu, Y.-C. Yeh, and Y.-H. Yang, “Compound word transformer: Learning to compose full-song music over dynamic directed hypergraphs,” in Proceedings of the AAAI Conference on Artificial Intelligence, vol. 35, no. 1, 2021, pp. 178–186. 

- [10] A. Agostinelli, T. I. Denk, Z. Borsos, J. Engel, M. Verzetti, A. Caillon, Q. Huang, A. Jansen, A. Roberts, M. Tagliasacchi et al., “Musiclm: Generating music from text,” arXiv preprint arXiv:2301.11325, 2023. 

- [11] J. Copet, F. Kreuk, I. Gat, T. Remez, D. Kant, G. Synnaeve, Y. Adi, and A. Défossez, “Simple and controllable music generation,” Advances in Neural Information Processing Systems, vol. 36, pp. 47 704–47 720, 2023. 

- [12] Z. Evans, J. D. Parker, C. Carr, Z. Zukowski, J. Taylor, and J. Pons, “Stable audio open,” arXiv preprint arXiv:2407.14358, 2024. 

- [13] S. Di, Z. Jiang, S. Liu, Z. Wang, L. Zhu, Z. He, H. Liu, and S. Yan, “Video background music generation with controllable music transformer,” in Proceedings of the 29th ACM International Conference on Multimedia, 2021, pp. 2037–2045. 

- [14] K. Su, J. Y. Li, Q. Huang, D. Kuzmin, J. Lee, C. Donahue, F. Sha, A. Jansen, Y. Wang, M. Verzetti et al., “V2meow: meowing to the visual beat via video-tomusic generation,” in Proceedings of the AAAI Conference on Artificial Intelligence, vol. 38, no. 5, 2024, pp. 4952–4960. 

- [15] L. Zhuo, Z. Wang, B. Wang, Y. Liao, C. Bao, S. Peng, S. Han, A. Zhang, F. Fang, and S. Liu, “Video background music generation: Dataset, method and evaluation,” in Proceedings of the IEEE/CVF International Conference on Computer Vision, 2023, pp. 15 637– 15 647. 

229 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [16] S. Liu, A. S. Hussain, Q. Wu, C. Sun, and Y. Shan, “Mumu-llama: Multi-modal music understanding and generation via large language models,” arXiv preprint arXiv:2412.06660, 2024. 

- [17] Z. Tian, Z. Liu, R. Yuan, J. Pan, Q. Liu, X. Tan, Q. Chen, W. Xue, and Y. Guo, “Vidmuse: A simple video-to-music generation framework with long-shortterm modeling,” arXiv preprint arXiv:2406.04321, 2024. 

- [18] Z. Xie, Q. He, Y. Zhu, Q. He, and M. Li, “Filmcomposer: Llm-driven music production for silent film clips,” arXiv preprint arXiv:2503.08147, 2025. 

- [19] P. Esser, S. Kulal, A. Blattmann, R. Entezari, J. Müller, H. Saini, Y. Levi, D. Lorenz, A. Sauer, F. Boesel et al., “Scaling rectified flow transformers for high-resolution image synthesis,” in Forty-first international conference on machine learning, 2024. 

- [20] L. Zhuo, R. Du, H. Xiao, Y. Li, D. Liu, R. Huang, W. Liu, X. Zhu, F.-Y. Wang, Z. Ma et al., “Luminanext: Making lumina-t2x stronger and faster with nextdit,” in The Thirty-eighth Annual Conference on Neural Information Processing Systems. 

- [21] J. Chen, Y. Jincheng, G. Chongjian, L. Yao, E. Xie, Z. Wang, J. Kwok, P. Luo, H. Lu, and Z. Li, “Pixart-α: Fast training of diffusion transformer for photorealistic text-to-image synthesis,” in The Twelfth International Conference on Learning Representations. 

- [22] A. Polyak, A. Zohar, A. Brown, A. Tjandra, A. Sinha, A. Lee, A. Vyas, B. Shi, C.-Y. Ma, C.-Y. Chuang, D. Yan et al., “Movie gen: A cast of media foundation models,” arXiv preprint arXiv:2410.13720, 2024. 

- [23] W. Kong, Q. Tian, Z. Zhang, R. Min, Z. Dai, J. Zhou, J. Xiong, X. Li, B. Wu, J. Zhang et al., “Hunyuanvideo: A systematic framework for large video generative models,” arXiv preprint arXiv:2412.03603, 2024. 

- [24] Y. Ma, A. Øland, A. Ragni, B. M. Del Sette, C. Saitis, C. Donahue, C. Lin, C. Plachouras, E. Benetos, E. Shatri et al., “Foundation models for music: A survey,” arXiv preprint arXiv:2408.14340, 2024. 

- [25] S. Ji, X. Yang, and J. Luo, “A survey on deep learning for symbolic music generation: Representations, algorithms, evaluations, and challenges,” ACM Computing Surveys, vol. 56, no. 1, pp. 1–39, 2023. 

- [26] S. Ji, J. Luo, and X. Yang, “A comprehensive survey on deep music generation: Multi-level representations, algorithms, evaluations, and future directions,” arXiv preprint arXiv:2011.06801, 2020. 

- [27] C. Hernandez-Olivan and J. R. Beltran, “Music composition with deep learning: A review,” Advances in speech and music technology: computational aspects and applications, pp. 25–50, 2022. 

- [28] Y. Zhu, J. Baca, B. Rekabdar, and R. Rawassizadeh, “A survey of ai music generation tools and models,” arXiv preprint arXiv:2308.12982, 2023. 

- [29] H. Liu, Y. Yuan, X. Liu, X. Mei, Q. Kong, Q. Tian, Y. Wang, W. Wang, Y. Wang, and M. D. Plumbley, “Audioldm 2: Learning holistic audio generation with self-supervised pretraining,” IEEE/ACM Transactions on Audio, Speech, and Language Processing, 2024. 

- [30] X. Liu, K. Su, and E. Shlizerman, “Tell what you hear from what you see–video to audio generation through text,” arXiv preprint arXiv:2411.05679, 2024. 

- [31] J. Yu, Y. Wang, X. Chen, X. Sun, and Y. Qiao, “Longterm rhythmic video soundtracker,” in International Conference on Machine Learning. PMLR, 2023, pp. 40 339–40 353. 

- [32] Z. Tang, Z. Yang, C. Zhu, M. Zeng, and M. Bansal, “Any-to-any generation via composable diffusion,” NeurIPS, vol. 36, 2024. 

- [33] S. Wu, H. Fei, L. Qu, W. Ji, and T.-S. Chua, “Nextgpt: Any-to-any multimodal llm,” arXiv: 2309.05519, 2023. 

- [34] J. Kang, S. Poria, and D. Herremans, “Video2music: Suitable music generation from videos using an affective multimodal transformer model,” Expert Systems with Applications, vol. 249, p. 123640, 2024. 

- [35] S. Li, Y. Qin, M. Zheng, X. Jin, and Y. Liu, “Diff-bgm: A diffusion model for video background music generation,” in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2024, pp. 27 348–27 357. 

- [36] R. Li, S. Zheng, X. Cheng, Z. Zhang, S. Ji, and Z. Zhao, “Muvi: Video-to-music generation with semantic alignment and rhythmic synchronization,” arXiv preprint arXiv:2410.12957, 2024. 

- [37] S. Li, B. Yang, C. Yin, C. Sun, Y. Zhang, W. Dong, and C. Li, “Vidmusician: Video-to-music generation with semantic-rhythmic alignment via hierarchical visual features,” arXiv preprint arXiv:2412.06296, 2024. 

- [38] B. Wang, L. Zhuo, Z. Wang, C. Bao, W. Chengjing, X. Nie, J. Dai, J. Han, Y. Liao, and S. Liu, “Multimodal music generation with explicit bridges and retrieval augmentation,” arXiv preprint arXiv:2412.09428, 2024. 

- [39] H. Zuo, W. You, J. Wu, S. Ren, P. Chen, M. Zhou, Y. Lu, and L. Sun, “Gvmgen: A general video-tomusic generation model with hierarchical attentions,” arXiv preprint arXiv:2501.09972, 2025. 

- [40] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polosukhin, “Attention is all you need,” Advances in neural information processing systems, vol. 30, 2017. 

230 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [41] I. J. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley, S. Ozair, A. Courville, and Y. Bengio, “Generative adversarial nets,” Advances in neural information processing systems, vol. 27, 2014. 

- [42] J. Ho, A. Jain, and P. Abbeel, “Denoising diffusion probabilistic models,” Advances in neural information processing systems, vol. 33, pp. 6840–6851, 2020. 

- [43] S.-L. Wu, C. Donahue, S. Watanabe, and N. J. Bryan, “Music controlnet: Multiple time-varying controls for music generation,” IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 32, pp. 2692– 2703, 2024. 

- [44] J. Li, T. Xu, X. Chen, X. Yao, and S. Liu, “Mozart’s touch: A lightweight multi-modal music generation framework based on pre-trained large models,” arXiv preprint arXiv:2405.02801, 2024. 

- [45] Y.-B. Lin, Y. Tian, L. Yang, G. Bertasius, and H. Wang, “Vmas: Video-to-music generation via semantic alignment in web music videos,” arXiv preprint arXiv:2409.07450, 2024. 

- [46] F. Qi, L. Ni, and C. Xu, “Harmonizing pixels and melodies: Maestro-guided film score generation and composition style transfer,” arXiv preprint arXiv:2411.07539, 2024. 

- [47] X. Tan, M. Antony, and H. Kong, “Automated music generation for visual art through emotion.” in ICCC, 2020, pp. 247–250. 

- [48] A. Santos, H. Pinto, R. Pereira Jorge, and N. Correia, “Musyfi: music synthesis from images,” in Proceedings of the 12th International Conference on Computational Creativity, 2021, pp. 103–112. 

- [49] R. Zhang, Y. Zhang, K. Shao, Y. Shan, and G. Xia, “Vis2mus: Exploring multimodal representation mapping for controllable music generation,” arXiv preprint arXiv:2211.05543, 2022. 

- [50] Z. Xiong, P.-C. Lin, and A. Farjudian, “Retaining semantics in image to music conversion,” in 2022 IEEE International Symposium on Multimedia (ISM). IEEE, 2022, pp. 228–235. 

- [51] S. Liu, A. S. Hussain, C. Sun, and Y. Shan, “M<sup>2</sup> ugen: Multi-modal music understanding and generation with the power of large language models,” arXiv preprint arXiv:2311.11255, 2023. 

- [52] S. Chowdhury, S. Nag, K. Joseph, B. V. Srinivasan, and D. Manocha, “Melfusion: Synthesizing music from image and language cues using diffusion models,” in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2024, pp. 26 826–26 835. 

- [53] K. Su, X. Liu, and E. Shlizerman, “How does it sound?” Advances in Neural Information Processing Systems, vol. 34, pp. 29 258–29 273, 2021. 

- [54] Y. Zhu, K. Olszewski, Y. Wu, P. Achlioptas, M. Chai, Y. Yan, and S. Tulyakov, “Quantized gan for complex music generation from dance videos,” in European Conference on Computer Vision. Springer, 2022, pp. 182–199. 

- [55] Y. Zhu, Y. Wu, K. Olszewski, J. Ren, S. Tulyakov, and Y. Yan, “Discrete contrastive diffusion for cross-modal music and image generation,” in The Eleventh International Conference on Learning Representations, 2023. 

- [56] X. Liu, K. Su, and E. Shlizerman, “Let the beat follow you-creating interactive drum sounds from body rhythm,” in Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision, 2024, pp. 7187–7197. 

- [57] G. Aggarwal and D. Parikh, “Dance2music: Automatic dance-driven music generation,” arXiv preprint arXiv:2107.06252, 2021. 

- [58] S. Li, W. Dong, Y. Zhang, F. Tang, C. Ma, O. Deussen, T.-Y. Lee, and C. Xu, “Dance-to-music generation with encoder-based textual inversion,” in SIGGRAPH Asia 2024 Conference Papers, 2024, pp. 1–11. 

- [59] X. Liang, W. Li, L. Huang, and C. Gao, “Dancecomposer: Dance-to-music generation using a progressive conditional music generator,” IEEE Transactions on Multimedia, 2024. 

- [60] K. Su, X. Liu, and E. Shlizerman, “Multiinstrumentalist net: Unsupervised generation of music from body movements,” arXiv preprint arXiv:2012.03478, 2020. 

- [61] ——, “Audeo: Audio generation for a silent performance video,” Advances in Neural Information Processing Systems, vol. 33, pp. 3325–3337, 2020. 

- [62] C. Gan, D. Huang, P. Chen, J. B. Tenenbaum, and A. Torralba, “Foley music: Learning to generate music from videos,” in Computer Vision–ECCV 2020: 16th European Conference, Glasgow, UK, August 23–28, 2020, Proceedings, Part XI 16. Springer, 2020, pp. 758–775. 

- [63] A. S. Koepke, O. Wiles, Y. Moses, and A. Zisserman, “Sight to sound: An end-to-end approach for visual piano transcription,” in ICASSP 2020-2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2020, pp. 1838–1842. 

- [64] H. Fang, P. Xiong, L. Xu, and Y. Chen, “Clip2video: Mastering video-text retrieval via image clip,” arXiv preprint arXiv:2106.11097, 2021. 

- [65] M. Afifi, M. A. Brubaker, and M. S. Brown, “Histogan: Controlling colors of gan-generated and real images via color histograms,” in Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, 2021, pp. 7941–7950. 

231 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [66] A. Radford, J. W. Kim, C. Hallacy, A. Ramesh, G. Goh, S. Agarwal, G. Sastry, A. Askell, P. Mishkin, J. Clark et al., “Learning transferable visual models from natural language supervision,” in International conference on machine learning. PmLR, 2021, pp. 8748–8763. 

- [67] J. Carreira and A. Zisserman, “Quo vadis, action recognition? a new model and the kinetics dataset,” in proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, 2017, pp. 6299–6308. 

- [68] J. Yu, X. Li, J. Y. Koh, H. Zhang, R. Pang, J. Qin, A. Ku, Y. Xu, J. Baldridge, and Y. Wu, “Vectorquantized image modeling with improved vqgan,” arXiv preprint arXiv:2110.04627, 2021. 

- [69] A. Dosovitskiy, L. Beyer, A. Kolesnikov, D. Weissenborn, X. Zhai, T. Unterthiner, M. Dehghani, M. Minderer, G. Heigold, S. Gelly et al., “An image is worth 16x16 words: Transformers for image recognition at scale,” in International Conference on Learning Representations, 2021. 

- [70] A. Arnab, M. Dehghani, G. Heigold, C. Sun, M. Luˇci´c, and C. Schmid, “Vivit: A video vision transformer,” in Proceedings of the IEEE/CVF international conference on computer vision, 2021, pp. 6836–6846. 

- [71] H. Touvron, L. Martin, K. Stone, P. Albert, A. Almahairi, Y. Babaei, N. Bashlykov, S. Batra, P. Bhargava, S. Bhosale et al., “Llama 2: Open foundation and finetuned chat models,” arXiv preprint arXiv:2307.09288, 2023. 

- [72] Y. Wang, M. Chen, and X. Li, “Continuous emotionbased image-to-music generation,” IEEE Transactions on Multimedia, vol. 26, pp. 5670–5679, 2023. 

- [73] S. Pidhorskyi, D. A. Adjeroh, and G. Doretto, “Adversarial latent autoencoders,” in Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, 2020, pp. 14 104–14 113. 

- [74] I. Higgins, L. Matthey, A. Pal, C. Burgess, X. Glorot, M. Botvinick, S. Mohamed, and A. Lerchner, “betavae: Learning basic visual concepts with a constrained variational framework,” in International conference on learning representations, 2017. 

- [75] A. Van Den Oord, O. Vinyals et al., “Neural discrete representation learning,” Advances in neural information processing systems, vol. 30, 2017. 

- [76] H. H. Tan and D. Herremans, “Music fadernets: Controllable music generation based on high-level features via low-level feature modelling,” arXiv preprint arXiv:2007.15474, 2020. 

- [77] A. Pati and A. Lerch, “Latent space regularization for explicit control of musical attributes,” in ICML Machine Learning for Music Discovery Workshop (ML4MD), Extended Abstract, Long Beach, CA, USA, 2019. 

- [78] H. Xu, G. Ghosh, P.-Y. Huang, D. Okhonko, A. Aghajanyan, F. Metze, L. Zettlemoyer, and C. Feichtenhofer, “Videoclip: Contrastive pre-training for zero-shot video-text understanding,” arXiv preprint arXiv:2109.14084, 2021. 

- [79] L. Min, J. Jiang, G. Xia, and J. Zhao, “Polyffusion: A diffusion model for polyphonic score generation with internal and external controls,” arXiv preprint arXiv:2307.10304, 2023. 

- [80] J. Li, D. Li, C. Xiong, and S. Hoi, “Blip: Bootstrapping language-image pre-training for unified visionlanguage understanding and generation,” in International conference on machine learning. PMLR, 2022, pp. 12 888–12 900. 

- [81] J. Song, C. Meng, and S. Ermon, “Denoising diffusion implicit models,” in International Conference on Learning Representations, 2021. 

- [82] R. Rombach, A. Blattmann, D. Lorenz, P. Esser, and B. Ommer, “High-resolution image synthesis with latent diffusion models,” in Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, 2022, pp. 10 684–10 695. 

- [83] W.-H. Kai and K.-X. Xing, “Video-driven musical composition using large language model with memoryaugmented state space,” The Visual Computer, pp. 1– 13, 2024. 

- [84] C. Ryali, Y.-T. Hu, D. Bolya, C. Wei, H. Fan, P.Y. Huang, V. Aggarwal, A. Chowdhury, O. Poursaeed, J. Hoffman et al., “Hiera: A hierarchical vision transformer without the bells-and-whistles,” in International conference on machine learning. PMLR, 2023, pp. 29 441–29 454. 

- [85] L. Wang, B. Huang, Z. Zhao, Z. Tong, Y. He, Y. Wang, Y. Wang, and Y. Qiao, “Videomae v2: Scaling video masked autoencoders with dual masking,” in Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, 2023, pp. 14 549–14 560. 

- [86] W. Peebles and S. Xie, “Scalable diffusion models with transformers,” in Proceedings of the IEEE/CVF international conference on computer vision, 2023, pp. 4195–4205. 

- [87] L. Zhang and M. Fuentes, “Sonique: Video background music generation using unpaired audio-visual data,” arXiv preprint arXiv:2410.03879, 2024. 

- [88] H. Zhang, X. Li, and L. Bing, “Video-llama: An instruction-tuned audio-visual language model for video understanding,” arXiv preprint arXiv:2306.02858, 2023. 

- [89] B. Elizalde, S. Deshmukh, M. Al Ismail, and H. Wang, “Clap learning audio concepts from natural language supervision,” in ICASSP 2023-2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2023, pp. 1–5. 

232 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [90] Z. Evans, C. Carr, J. Taylor, S. H. Hawley, and J. Pons, “Fast timing-conditioned latent audio diffusion,” in Forty-first International Conference on Machine Learning, 2024. 

- [91] X. Tong, S. Chen, P. Yu, N. Liu, H. Qv, T. Ma, B. Zheng, F. Yu, and S.-C. Zhu, “Video echoed in harmony: Learning and sampling video-integrated chord progression sequences for controllable video background music generation,” IEEE Transactions on Computational Social Systems, 2024. 

- [92] K. Li, Y. He, Y. Wang, Y. Li, W. Wang, P. Luo, Y. Wang, L. Wang, and Y. Qiao, “Videochat: Chat-centric video understanding,” arXiv preprint arXiv:2305.06355, 2023. 

- [93] C. Raffel, N. Shazeer, A. Roberts, K. Lee, S. Narang, M. Matena, Y. Zhou, W. Li, and P. J. Liu, “Exploring the limits of transfer learning with a unified textto-text transformer,” Journal of machine learning research, vol. 21, no. 140, pp. 1–67, 2020. 

- [94] M. Sharma, M. T. Haseeb, G. Xia, and Y. Tsuruoka, “M2m-gen: A multimodal framework for automated background music generation in japanese manga using large language models,” arXiv preprint arXiv:2410.09928, 2024. 

- [95] A. Agostinelli, T. I. Denk, Z. Borsos, J. Engel, M. Verzetti, A. Caillon, Q. Huang, A. Jansen, A. Roberts, M. Tagliasacchi et al., “Musiclm: Generating music from text,” arXiv preprint arXiv:2301.11325, 2023. 

- [96] L. Li, Y. Huang, J. Wu, Y. Yang, Y. Li, Y. Guo, and G. Shi, “Theme-aware visual attribute reasoning for image aesthetics assessment,” IEEE Transactions on Circuits and Systems for Video Technology, vol. 33, no. 9, pp. 4798–4811, 2023. 

- [97] Z. Zhang, L. Wang, and J. Yang, “Weakly supervised video emotion detection and prediction via crossmodal temporal erasing network,” in Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, 2023, pp. 18 888–18 897. 

- [98] Z. Chen, W. Wang, H. Tian, S. Ye, Z. Gao, E. Cui, W. Tong, K. Hu, J. Luo, Z. Ma et al., “How far are we to gpt-4v? closing the gap to commercial multimodal models with open-source suites,” Science China Information Sciences, vol. 67, no. 12, p. 220101, 2024. 

- [99] S. Tian, C. Zhang, W. Yuan, W. Tan, and W. Zhu, “Xmusic: Towards a generalized and controllable symbolic music generation framework,” arXiv preprint arXiv:2501.08809, 2025. 

- [100] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image recognition,” in Proceedings of the IEEE conference on computer vision and pattern recognition, 2016, pp. 770–778. 

- [101] Z. Tian, Y. Jin, Z. Liu, R. Yuan, X. Tan, Q. Chen, W. Xue, and Y. Guo, “Audiox: Diffusion transformer for anything-to-audio generation,” arXiv preprint arXiv:2503.10522, 2025. 

- [102] Y.-S. Huang and Y.-H. Yang, “Pop music transformer: Beat-based modeling and generation of expressive pop piano compositions,” in Proceedings of the 28th ACM international conference on multimedia, 2020, pp. 1180–1188. 

- [103] J. Carreira and A. Zisserman, “Quo vadis, action recognition? a new model and the kinetics dataset,” in proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, 2017, pp. 6299–6308. 

- [104] H. Yang, K. Su, Y. Zhang, J. Chen, K. Qian, G. Liu, and C. Gan, “Unimumo: Unified text, music and motion generation,” arXiv preprint arXiv:2410.04534, 2024. 

- [105] S. Hong, W. Im, and H. S. Yang, “Content-based videomusic retrieval using soft intra-modal structure constraint,” arXiv preprint arXiv:1704.06761, 2017. 

- [106] S. Abu-El-Haija, N. Kothari, J. Lee, P. Natsev, G. Toderici, B. Varadarajan, and S. Vijayanarasimhan, “Youtube-8m: A large-scale video classification benchmark,” arXiv preprint arXiv:1609.08675, 2016. 

- [107] Y. R. Pandeya and J. Lee, “Deep learning-based late fusion of multimodal information for emotion classification of music video,” Multimedia Tools and Applications, vol. 80, no. 2, pp. 2887–2905, 2021. 

- [108] J. F. Gemmeke, D. P. Ellis, D. Freedman, A. Jansen, W. Lawrence, R. C. Moore, M. Plakal, and M. Ritter, “Audio set: An ontology and human-labeled dataset for audio events,” in 2017 IEEE international conference on acoustics, speech and signal processing (ICASSP). IEEE, 2017, pp. 776–780. 

- [109] H. T. P. Thao, G. Roig, and D. Herremans, “Emomv: Affective music-video correspondence learning datasets for classification and retrieval,” Information Fusion, vol. 91, pp. 64–79, 2023. 

- [110] L. Lanzendörfer, F. Grötschla, E. Funke, and R. Wattenhofer, “Disco-10m: A large-scale music dataset,” Advances in Neural Information Processing Systems, vol. 36, pp. 54 451–54 471, 2023. 

- [111] Z. Zhou, K. Mei, Y. Lu, T. Wang, and F. Rao, “Harmonyset: A comprehensive dataset for understanding video-music semantic alignment and temporal synchronization,” arXiv preprint arXiv:2503.01725, 2025. 

- [112] B. Li, X. Liu, K. Dinesh, Z. Duan, and G. Sharma, “Creating a multitrack classical music performance dataset for multimodal music analysis: Challenges, insights, and applications,” IEEE Transactions on Multimedia, vol. 21, no. 2, pp. 522–535, 2018. 

233 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [113] H. Zhao, C. Gan, A. Rouditchenko, C. Vondrick, J. McDermott, and A. Torralba, “The sound of pixels,” in Proceedings of the European conference on computer vision (ECCV), 2018, pp. 570–586. 

- [114] R. Li, S. Yang, D. A. Ross, and A. Kanazawa, “Ai choreographer: Music conditioned 3d dance generation with aist++,” in Proceedings of the IEEE/CVF international conference on computer vision, 2021, pp. 13 401–13 412. 

- [115] S. Tsuchida, S. Fukayama, M. Hamasaki, and M. Goto, “Aist dance video database: Multi-genre, multi-dancer, and multi-camera database for dance information processing.” in ISMIR, vol. 1, no. 5, 2019, p. 6. 

- [116] C. Xu, Y. Fu, B. Zhang, Z. Chen, Y.-G. Jiang, and X. Xue, “Learning to score figure skating sport videos,” IEEE transactions on circuits and systems for video technology, vol. 30, no. 12, pp. 4578–4590, 2019. 

- [117] J. Xia, M. Zhuge, T. Geng, S. Fan, Y. Wei, Z. He, and F. Zheng, “Skating-mixer: Multimodal mlp for scoring figure skating,” arXiv preprint arXiv:2203.03990, 2022. 

- [118] X. Wu, Y. Qiao, X. Wang, and X. Tang, “Bridging music and image via cross-modal ranking analysis,” IEEE Transactions on Multimedia, vol. 18, no. 7, pp. 1305– 1318, 2016. 

- [119] X. Li, D. Hu, and X. Lu, “Image2song: Song retrieval via bridging image content and lyric words,” in Proceedings of the IEEE International Conference on Computer Vision, 2017, pp. 5649–5658. 

- [120] G. Verma, E. G. Dhekane, and T. Guha, “Learning affective correspondence between music and image,” in ICASSP 2019-2019 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2019, pp. 3975–3979. 

   - [125] Z. Wang, K. Chen, J. Jiang, Y. Zhang, M. Xu, S. Dai, X. Gu, and G. Xia, “Pop909: A pop-song dataset for music arrangement generation,” in ISMIR, 2020. 

   - [126] D. Christodoulou and M. Kuhlmann-Jørgensen, “Finding the subjective truth: Collecting 2 million votes for comprehensive gen-ai model evaluation,” arXiv preprint arXiv:2409.11904, 2024. 

   - [127] V. Petsiuk, A. E. Siemenn, S. Surbehera, Z. Chin, K. Tyser, G. Hunter, A. Raghavan, Y. Hicke, B. A. Plummer, O. Kerret et al., “Human evaluation of textto-image models on a multi-task benchmark,” arXiv preprint arXiv:2211.12112, 2022. 

   - [128] K. Kilgour, M. Zuluaga, D. Roblek, and M. Sharifi, “Frechet audio distance: A metric for evaluating music enhancement algorithms,” arXiv preprint arXiv:1812.08466, 2018. 

   - [129] S. Hershey, S. Chaudhuri, D. P. Ellis, J. F. Gemmeke, A. Jansen, R. C. Moore, M. Plakal, D. Platt, R. A. Saurous, B. Seybold et al., “Cnn architectures for large-scale audio classification,” in 2017 ieee international conference on acoustics, speech and signal processing (icassp). IEEE, 2017, pp. 131–135. 

   - [130] Q. Kong, Y. Cao, T. Iqbal, Y. Wang, W. Wang, and M. D. Plumbley, “Panns: Large-scale pretrained audio neural networks for audio pattern recognition,” IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 28, pp. 2880–2894, 2020. 

   - [131] R. Girdhar, A. El-Nouby, Z. Liu, M. Singh, K. V. Alwala, A. Joulin, and I. Misra, “Imagebind: One embedding space to bind them all,” in Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, 2023, pp. 15 180–15 190. 

- [121] Q. You, J. Luo, H. Jin, and J. Yang, “Building a large scale dataset for image emotion recognition: The fine print and the benchmark,” in Proceedings of the AAAI conference on artificial intelligence, vol. 30, no. 1, 2016. 

- [122] P. J. Lang, M. M. Bradley, B. N. Cuthbert et al., “International affective picture system (iaps): Technical manual and affective ratings,” NIMH Center for the Study of Emotion and Attention, vol. 1, no. 39-58, p. 3, 1997. 

- [123] A. Marchewka, Ł. ˙Zurawski, K. Jednoróg, and A. Grabowska, “The nencki affective picture system (naps): Introduction to a novel, standardized, widerange, high-quality, realistic picture database,” Behavior research methods, vol. 46, pp. 596–610, 2014. 

- [124] X. Chi, Y. Wang, A. Cheng, P. Fang, Z. Tian, Y. He, Z. Liu, X. Qi, J. Pan, R. Zhang et al., “Mmtrail: A multimodal trailer video dataset with language and music descriptions,” arXiv preprint arXiv:2407.20962, 2024. 

234 

