---
paper_id: "000039"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706410/files/000039.pdf"
---

# TOMI: TRANSFORMING AND ORGANIZING MUSIC IDEAS FOR MULTI-TRACK COMPOSITIONS WITH FULL-SONG STRUCTURE 



<!-- Start of picture text -->
Qi He 1 Gus Xia 1 Ziyu Wang 1,2<br>1 Music X Lab, MBZUAI 2 New York University<br><!-- End of picture text -->

```
heqi201255@icloud.com,gus.xia@mbzuai.ac.ae,ziyu.wang@nyu.edu
```

## ABSTRACT 

Hierarchical planning is a powerful approach to model long sequences structurally. Aside from considering hierarchies in the temporal structure of music, this paper explores an even more important aspect: concept hierarchy, which involves generating music ideas, transforming them, and ultimately organizing them—across musical time and space—into a complete composition. To this end, we introduce TOMI (Transforming and Organizing Music Ideas) as a novel approach in deep music generation and develop a TOMI-based model via instructiontuned foundation LLM. Formally, we represent a multitrack composition process via a sparse, four-dimensional space characterized by clips (short audio or MIDI segments), sections (temporal positions), tracks (instrument layers), and transformations (elaboration methods). Our model is capable of generating multi-track electronic music with full-song structure, and we further integrate the TOMI-based model with the REAPER digital audio workstation, enabling interactive human-AI co-creation. Experimental results demonstrate that our approach produces higher-quality electronic music with stronger structural coherence compared to baselines.<sup>1</sup> 

## 1. INTRODUCTION 

Automatic music generation has advanced from producing short clips to composing entire pieces, yet long-term structure remains a major challenge. Unlike short-term generation, which focuses on capturing local patterns [1–6], longterm generation requires handling structure across multiple levels, from sectional repetition and cadence to the overall theme and whole narrative flow. The most common approach is to scale up models and data [7,8], yet even with vast training corpora, achieving truly structured compositions remains difficult. An alternative is to model the temporal hierarchy of music, where it evolves at multiple time 

> 1 Source code: `https://github.com/heqi201255/TOMI` . Demo page: `https://tomi-2025.github.io/` . 

> © Q. He, G. Xia, and Z. Wang. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: Q. He, G. Xia, and Z. Wang, “TOMI: Transforming and Organizing Music Ideas for Multi-Track Compositions with Full-Song Structure”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 



<!-- Start of picture text -->
Sections<br>s2 s3 s4<br>t1<br>Tracks<br>t3<br>t4<br>Features Clips Traior-<br>Music Ideas mations Final Composition<br><!-- End of picture text -->

Figure 1: Concept hierarchy in TOMI: music ideas developed from features to clips are transformed and integrated into the composition, organized by sections and tracks. 

scales, with different model components capturing context dependencies at each level [7,9–11]. 

But have we fully captured the hierarchical nature of music? While temporal hierarchy is essential, so is concept hierarchy, which often manifests in the development of motifs and music materials. As noted in [12], most pop songs are composed with a sparse and small set of core ideas, which are then evolved and repeated in an organized way. We illustrate this process in Figure 1, where music ideas, initially appearing as abstract features, are concretized as music clips, then transformed, and finally organized into a full composition. We refer to this concept hierarchy in music as TOMI (Transforming and Organizing Music Ideas). TOMI shares a spirit with David Cope’s recombinant music composition in EMI [13], an idea that deep learning has yet to truly embrace. 

In this paper, we propose a TOMI-based music generation system for full-song and multi-track electronic music composition, inspired by the prevalent use of MIDI and audio sample packs among electronic music producers. The system is built around four key elements: clips, transformations, sections, and tracks. Sections and tracks are first created to serve as the canvas for composition, similar to a digital audio workstation (DAW) interface. The system then selects music clips from a library of audio and MIDI samples. For each selected clip, a transformation function is defined and applied, then the transformed clip is placed in its designated section and track. On the backend, a structured data representation parameterizes clips, transformations, sections, and tracks, and links them dynamically to construct a full composition. We leverage a pre-trained text-based large language model (LLM) to operate on this data structure, using in-context learning (ICL) to fill in the parameters and create dynamic links. 

337 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

In sum, the contributions of this paper are as follows: 

1. We introduce TOMI to model music concept hierarchy and develop a deep learning-based system for structured electronic music generation. The proposed data structure integrates symbolic and audio representations and can be manipulated by text-based LLMs via ICL. 

2. We apply our system to generate high-quality electronic music with full-song structure. Objective and subjective evaluations show that songs generated by our model have clearer phrase boundaries, better phrase development, and higher music quality than the baselines. 

3. We integrate TOMI with the REAPER digital audio workstation, providing seamless connection with professional music software interface and enabling humanAI co-creation with high-resolution audio rendering. 

## 2. RELATED WORK 

In automatic music generation, many studies focus on generating coherent music segments [1–6], while fewer focus on modeling long-term structure under the temporal hierarchy of music. Jukebox [7] uses hierarchical VQ-VAE with time conditioning to enhance long-term coherence; Wang et al. [9] applies cascaded diffusion models for structured symbolic music generation. Some methods introduce explicit structure encoding in neural networks [14,15] or use efficient sampling techniques to generate structured variations [16]. However, the application of TOMI concepts in music generation remains largely unexplored. Related works include a rule-based recombinant music method [13], which reorganizes existing music elements based on stylistic constraints, and MELONS [17], which uses a structure graph to enforce long-term dependencies in melody generation but offers limited flexibility in musical transformation. 

In the context of co-creative music systems, existing generative models produce data in either symbolic (e.g., [1,2,4,9,17]) or waveform (e.g., [3,5,6]) format. Furthermore, these models lack intuitive interfaces for user cocreation and fine-grained control over musical elements, as found in modern DAWs. Composer’s Assistant [18] and its successor [19] integrate with REAPER to support cocreation but focus on generating symbolic phrases rather than full pieces. Our approach generates complete compositions containing both MIDI and audio phrases while also enabling user co-creation directly within REAPER. 

With recent advances in AI, text-based LLMs have emerged as a promising alternative for music creation. Previous studies like ChatMusician [20] and MuPT [21] employ ABC Notation [22] to represent music in text format and fine-tune LLaMA models [23]. While these approaches outperform generic LLMs in music tasks, their performance remains limited compared to LLMs trained exclusively on music data [24–26]. Other works have leveraged text-based LLMs for music analysis [27, 28], showing their capability to interpret music concepts through natural language. This motivates us to develop a textual hierarchical representation of music concepts to better integrate with text-based LLMs. 

## 3. METHODOLOGY 

In this section, we discuss TOMI in multi-track electronic music generation with full-song structure. The implementation consists of two main components: (1) a graph data structure named composition link that connects raw music ideas with the composition (Section 3.1), and (2) incontext learning to compose music by following this data structure (Section 3.2). We also demonstrate the integration with the REAPER DAW (Section 3.3). 

## 3.1 TOMI Data Structure 

The proposed data structure consists of four node types: clips, sections, tracks, and transformations. A composition link is a quadruple of these nodes, specifying a music clip (what) to be placed in a particular section (when) and on a specific track (where), undergoing certain transformations (how). Nodes are reusable across links, forming a structured representation of the full composition. 

## 3.1.1 Clip Node 

Clips are audio or MIDI samples sourced from databases. Each clip is a short music segment, such as a chord progression or a drum loop, described by a set of features. A MIDI clip can represent elements like chords, basslines, melodies, or arpeggios, with attributes such as tonality, duration, and root progression. An audio clip can be either a sample loop or a one-shot sound, with keywords describing its content. The blue-edged box in Figure 2a shows an example feature set for a chord clip. Once the features are specified by the LLM (discussed in Section 3.2), we can query the databases for the corresponding music material. 

## 3.1.2 Section Node 

The temporal divisions of a music composition are modeled by section nodes. A section node involves a duration and a phrase label, such as verse and chorus. A section node can appear multiple times within a composition, meaning its music content remains identical across instances. For example, as shown in Figure 2, the 16-bar verse section s2 is reused after the 16-bar chorus section s3, resulting in two identical verses with the same content. 

## 3.1.3 Track Node 

Track nodes represent the vertical layering of a composition and organize clips into MIDI or audio tracks (see the track axis in Figure 2b). MIDI tracks accept only MIDI clips and require instruments to generate sound, while audio tracks accept only audio clips and play them directly. 

## 3.1.4 Transformation Node 

A transformation node transforms clips before placing them on specific tracks and sections. Unlike pitch transposition and tempo adjustment, which are handled in the final stage (discussed in Section 3.3), transformation nodes perform more semantically meaningful manipulations and mainly serve three roles. First (and most importantly), it can control rhythmic patterns of the audio or MIDI clips 

338 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
LLM Output<br>name: IntroSection Clips<br>duration: 8 barslabel: Intro # Generating sections: /*repeat*/ eat feat<br>S2 S3<br>(intro, 8b) (verse, 16b) (chorus, 16b) (verse, 16b) Sample DB<br>name: GuitarRiff<br>track_type: Audio # Generating tracks:<br>name: ChordMotif<br>(Audio)(Audio) (Audio) (MIDI)<br>is_midi: True<br>content_type: Chord # Generating clip features and query DB: Tranons<br>tempo_range: 90 - 130duration: 4 bars feat eat feat<br>tonality: A Major<br>root_prog: (4, 5, 3, 1) (A)<br>Sample # Generating transformations: Sections<br>(Drum (General Tracks<br>Transform) Transform) Transform)<br># Generating composition links:<br>name: FourOnFloor<br>type: Drum Transform (A) := S2<br>action_sequence:<br>onset, rest-, rest-, rest-, (B) := S3 f2<br>onset, rest-, rest-, rest-,<br>onset, rest-, rest-, rest-, (C) := (S2<br>onset, rest-, rest-, rest-<br><!-- End of picture text -->

(a) Example of an LLM output following our ICL prompt structure. In clips, the LLM only generates features for clips, which are then used to query the sample databases for actual MIDI or audio clips. We also show three composition links, each as a tuple of (section, track, clip, and transformation). 

(b) Music generation process with composition links, illustrating how clips (top) are transformed and then organized into the arrangement (bottom). Links pAq and pCq each have two branches because section s2 appears twice in the section sequence, which means they are identical and share the same composition links. 

Figure 2: We show the structured LLM output in (a) with the corresponding music generation process in (b). We distinguish node types by color and shape, with a detailed attribute example for each type shown on the left of (a). We depict three composition link examples as colored arrows in (b), highlighting their results with rectangles in corresponding colors. 

with an action sequence of onsets, sustains, and rests (see f1 in Figure 2a). For example, it can convert MIDI chord clips with whole notes into rich rhythmic patterns or place a one-shot drum on each beat to create a four-on-the-floor rhythm. Second, it can handle the riser or faller sound effects commonly used in electronic music composition, which are placed either left- or right-aligned within a section, creating smooth transitions (see c3 in Figure 2b). Lastly, it dynamically handles the looping of a clip, determining whether it plays once at a specific time, loops throughout a section, or is trimmed to fit a shorter section. Our implementation defines three subclasses of transformations: (1) Drum transform (for one-shot drums), (2) Fx transform (for risers and fallers), and (3) General transform (for others), each following different transformation rules. We refer the reader to our demo page for details. 

## 3.1.5 Composition Link 

A composition link comprises one node each of section, clip, transformation, and track, showing the entire process of transforming and organizing a music idea in the composition. Since nodes are independent of the composition link, they can be reused across multiple links. Figure 2b shows the process of three composition links. Note that links pAq and pCq branches in the final composition because section s2 is used twice. This is an efficient way to represent complex arrangements, as a single clip can be referenced by multiple links, spanning different sections and tracks while adapting to various transformations. 

## 3.2 Music Generation with In-Context Learning 

The TOMI data structure, as defined above, can be fully represented in text format. A complete composition can be decomposed into a set of composition links, each represented as a quadruple of nodes, where each node corresponds to a set of textual attributes. By leveraging a text-based LLM with in-context learning, we can generate compositions directly as TOMI instances. Our ICL prompt systematically breaks down the data structure in steps, following the order: sections, tracks, clips, transformations, and composition links. It guides the LLM from planning the overall song structure and music ideas to organizing them into a full song. The LLM output follows these steps accordingly, as shown in Figure 2a. 

In our implementation, we elaborate our data structure with detailed examples and define a structured response schema in the prompt. We require the LLM to generate a unique name attribute for each node to reference in composition links. Moreover, we can specify additional contexts, such as tempo, mood, and custom song structures. To get robust results, we implement a rule-based validation to check the LLM output for syntax errors and invalid values. If issues are detected, an error report is generated, prompting the LLM to iteratively refine its output until no errors remain. At this point, we obtain an abstract representation of the composition in TOMI structure. To realize this, we initiate the sample retrieval process to get the actual clip materials. Then, we set a global tempo and key to unify the keys and tempos of clips within the DAW. 

339 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 3.3 Digital Audio Workstation Integration 

To support audio rendering and interactivity, we integrate the TOMI framework with the REAPER DAW. This allows the generated composition to be visualized in a professional DAW while benefiting users from REAPER’s editing and rendering capabilities. The composition links and nodes of a generated piece are converted to REAPER elements, including tracks, section markers, and clips with applied transformations. We use REAPER to automatically time-stretch loopable clips to fit the tempo setting and transpose melodic clips to align with the key setting. 

## 4. EXPERIMENT 

To implement the generation system, we prepare a MIDI database and an audio database for clip sample retrieval and use GPT-4o [29] to generate compositions in TOMI schema. We evaluate our approach with baseline methods and use both objective and subjective measurements to compare the music quality and structural consistency. 

## 4.1 System Preparation 

We collect multiple licensed MIDI and audio sample packs in the electronic music genre through online purchases.<sup>2</sup> We process the raw datasets into separate MIDI and audio databases using different feature extraction methods. For MIDI clips, we developed a script to analyze and extract musical features from them. Moreover, it can also extract music stems, such as bass, chord, and melody, from the source MIDI to augment the data. Then, we store the labeled data in a SQLite3 [30] database as our MIDI database. For audio samples, we use ADSR Sample Manager [31] to analyze and generate labels for them. The results are also exported as a SQLite3 database. The statistics of our MIDI database and audio database are shown in Table 1. Sample retrieval involves constructing a search query based on the clip’s attributes to fetch matching samples from the database. The clip node randomly selects one sample from the results. If no matches are found, the clip and its associated composition links are discarded. 

We limit all generated sections to the 4/4 time signature to simplify implementation. When exporting audio via REAPER, we randomly assign each MIDI track to one of eight virtual instrument presets (5 for chords, 2 for melody, and 1 for bass). We keep all REAPER settings at their defaults and apply no mixing plug-ins except for a limiter on the master track to prevent audio clipping. 

## 4.2 Baseline Method and Ablations 

We compare our approach with MusicGen [6] and two ablations in electronic music generation. Since our system integrates both audio and MIDI data, there is no directly comparable baseline. However, as our final output is rendered as audio, MusicGen is a suitable comparison, which 

> 2 We obtain sample packs from two music asset platforms: `https:` 

> `//splice.com/` and `https://www.loopmasters.com/` 

|Content Ty|pe<br>Count|Duration|Count|
|---|---|---|---|
|Chord|2604|4-bar|2947|
|Bass|209|8-bar|1417|
|Melody|1392|16-bar|68|
|Arpeggio|227|||
|Total|4432|Total|4432|
|(a) MIDI co|ntent types.|(b) MIDI d|urations.|
|Sample Type|Count|LoopDuratio|n<br>Count|
|Loop|104493|2-bar|24922|
|One-Shot|170187|4-bar|27214|
|||8-bar|24638|
|||16-bar|27719|
|Total|274680|Total|104493|



(c) Audio sample types. (d) Audio loop durations. 

Table 1: Statistics of sample databases. 

is capable of generating long-term and high-quality electronic music. This allows us to evaluate our method against state-of-the-art music generation systems. The ablations help us assess the individual contributions of the composition link representation and the LLM integration. 

- MusicGen We use the MusicGen-Large-3.3B model as the baseline with prompts specifying key, tempo, and section sequence. To generate longer audio beyond its duration limit, we apply a sliding window approach, where a 30-second window slides in 10-second chunks, using the previous 20 seconds as context. We modify its inference process to include the current generation’s position within the full composition and its corresponding phrase notations in the prompt at each step, guiding the model to align its output with the given structure. 

- Standalone LLM (TOMI w/o Composition Links) 

   - We remove the composition links representation from our system. We redesign the prompt to let the LLM generate a sequence of tracks and clip descriptions with position information (time point and track location) conditioned on a section sequence. The sample retrieval mechanism is also applied for clips. 

- Random (TOMI w/o LLM) We replace the LLM operations in our system with a rule-based method that uses randomized operations to generate music within the composition-links structure. The system creates 15–25 track nodes, populates sections with clips stochastically, and determines for each track whether to place, reuse, or generate a new clip. MIDI clips are assigned a random type (chord, bass, or melody) with bass derived from chords, while audio clips are selected from tonal, percussion, and sound effect feature labels. Each clip is then linked to one of four predefined transformations: general, drum, riser Fx, or faller Fx. 

We define 4 keys and 4 distinct section sequences, each consisting of 8 to 10 sections. Each section has a name, a phrase label, and a duration ranging from 4 to 16 bars. Then, using each method, we generate 4 sets of electronic music pieces at 120 BPM, with each set containing 8 pieces (2 per key), all conditioned on the same section sequence. In total, we generate 32 compositions for each method. 

340 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

|Method|FAD<sup>VGGish </sup>Ó|FAD<sup>CLAP </sup>Ó|ILS<sup>MERT </sup>Ò|ILS<sup>MS </sup>Ò|ILS<sup>WF </sup>Ò|
|---|---|---|---|---|---|
|TOMI|3.51|0.38|0.28˘0.12|0.36˘0.33|1.14˘0.73|
|MusicGen|5.31|0.62|0.06˘0.04|0.12˘0.07|0.28˘0.09|
|Standalone LLM|5.84|0.46|0.16˘0.11|0.10˘0.12|0.09˘0.16|
|Random|6.92|0.47|0.16˘0.09|0.22˘0.16|0.48˘0.28|



Table 2: Objective evaluation results of FAD with two models and ILS with three latent representations. 



<!-- Start of picture text -->
v1 ,p1, cl , v2 p2, c2 , b, c3 v1 p1, cl , v2 p2, c2 , b, c3 ,o v1 p1, cl, √2 p2, c2 , b, c3 v1 ,p1, cl , v2 p2, c2 ,b, c3<br>25<br>-0.7<br>ILSLLM = 0.093<br><!-- End of picture text -->

Figure 3: ILS similarity matrices example, where all four compositions are generated under the section sequence: i (intro), v1 (verse 1), p1 (pre-chorus 1), c1 (chorus 1), v2 (verse 2), p2 (pre-chorus 2), c2 (chorus 2), b (bridge), c3 (chorus 3), and o (outro). Darker colors indicate higher segment similarity. The blocks marked as yellow-edge boxes are same-label similarities, with diagonal values marked as red lines being excluded, and the remaining parts are different-label similarities. 

## 4.3 Objective Evaluation 

We evaluate the music quality and structural consistency of generated compositions. For music quality, we use the Fréchet Audio Distance metric (FAD) [32, 33] with a VGGish model [34] and a CLAP model [35] to compare human-composed electronic music and the music generated by each method. We randomly collected 329 songs as references from the Spotify Mint playlist [36], one of the most popular curated playlists dedicated to the electronic music genre. A lower FAD score indicates that the generated music is closer to human-composed music in quality. 

For structural consistency, we use the Inter-Phrase Latent Similarity metric (ILS) refined from [9]. ILS aims to compute a self-similarity matrix of musical features and evaluates if the average similarity between segments sharing the same phrase label is higher than those with different labels. Instead of measuring the ratio of same-label to overall similarities in the original metric, we use Cohen’s d [37] to compute the effect size of the difference between same-label and different-label similarities, excluding diagonal elements to avoid biases. This offers a scaleindependent measure that robustly captures the separation between groups. We extract latent representations from audio while preserving temporal structure, then compute a self-similarity matrix of them using cosine similarity. We evaluate ILS with MERT embeddings [38], Mel spectrograms, and raw waveforms, denoted as ILS<sup>MERT</sup> , ILS<sup>MS</sup> , and ILS<sup>WF</sup> , respectively. To compute the ILS score, we denote the cosine similarity between time-related latent elements i and j as Sij, the phrase label of element i as li, and the quantities of same-label and different-label elements as Nsame and Ndiff , respectively, excluding diagonal elements. A higher ILS score indicates better and more effective structural consistency. The formula is defined as: 



<!-- Start of picture text -->
X ¯ same ´ X ¯ diff<br>ILS “ , (1)<br>s<br><!-- End of picture text -->

where X<sup>`¯`</sup> same and X<sup>`¯`</sup> diff are the mean similarities of samelabel and different-label groups, respectively, defined as: 



<!-- Start of picture text -->
ř i‰ j Sij ¨ δpli “ ljq<br>X ¯ same “ , (2)<br>Nsame<br><!-- End of picture text -->



<!-- Start of picture text -->
ř i ,j Sij ¨ δpli ‰ ljq<br>X ¯ diff “ . (3)<br>Ndiff<br><!-- End of picture text -->

and s is the pooled standard deviation derived from the variances s<sup>2</sup> same<sup>and s2</sup> diff<sup>of the two groups, defined as:</sup> 



<!-- Start of picture text -->
p Nsame ´  1 q s 2 same `  p Ndiff ´  1 q s 2 dif<br>s “ (4)<br>d Nsame ` Ndiff ´  2<br><!-- End of picture text -->

We show the FAD scores and ILS with means and standard deviations in Table 2. The results show that our method achieves the lowest FAD scores and the highest ILS scores across all measurements, outperforming the baseline methods in both music quality and structural consistency. Notably, the ablation results show that even with high-quality music samples, lacking sufficient arrangement logic can still lead to poor FAD scores. This proves our approach’s ability to generate music with improved flow naturalness and arrangement coherence while preserving the expected long-term structures. Figure 3 provides a comparative visualization of ILS matrices for four compositions, with phrase labels on both axes, yellowedged boxes highlighting regions of same-label similarities, the red line marking the main diagonal, and the remaining areas representing different-label similarities. 

341 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
Standalone LLM MusicGen TOMI Random<br>5.0<br>pl. local p2.. same-Lb. ph.p3. diff–Lb. ph. overall<br>4.0<br>3.0<br>Rating2.0<br>1.0<br>0.0<br>Transition Structure<br>Naturalness Similarity Naturalness Creativity Naturalness Musicality<br>Clarity<br><!-- End of picture text -->

Figure 4: Subjective evaluation results of mean score with within-subject confidence intervals, where p1-p4 corresponds to four parts of our survey: p1. Local Music Quality, p2. Consistency Among Same-Label Phrases, p3. Contrast Between Different-Label Phrases, and p4. Overall Full-Song Evaluation. 

## 4.4 Subjective Evaluation 

We conduct a double-blind online survey to compare the music quality and structural consistency of compositions generated by the four methods. Since each composition is a full 3- to 4-minute song, which is too long to be evaluated in a single-question, we assess four compositions (one per method) throughout the survey. To ensure a comprehensive evaluation, we create three distinct question sets with the same survey structure but different compositions, resulting in a total of 12 compositions being evaluated. The survey is divided into four parts, each containing 4 to 12 questions, aiming to evaluate the piece from section-level music quality to overall structural alignment. All metrics are measured on a 5-point rating scale. The details are as follows: 

- Part 1. Local Music Quality This part consists of 3 subparts, each selecting the same section (e.g., intro) from each composition. Participants rate Naturalness to evaluate the similarity to human-composed music and the conformity to the typical electronic music style. 

- Part 2. Consistency Among Same-Label Phrases This part consists of 2 subparts, each selecting two sections with the same phrase label (e.g., verse 1 and verse 2) from each composition. Participants rate Similarity between the two sections. 

- Part 3. Contrast Between Different-Label Phrases 

   - This part consists of 2 subparts, each selecting two consecutive sections from the same position in each composition (e.g., intro and verse 1). Participants rate Transition Naturalness based on boundary clearness, transition smoothness, and phrase alignment. 

- Part 4. Overall Full-Song Evaluation This part shows the complete composition audios. Participants rate Structure Clarity for how well each section aligns with the given structure, Creativity for how creative the music is, Naturalness for how humanlike the music sounds, and Musicality for the overall music quality. 

We insert an intermediate page between evaluation parts to inform participants of their progress and help reduce listening fatigue. Additionally, we show the input conditions for music generation on each question page to remind par- 

ticipants of the expected song structure and tonality. We distributed the survey on multiple social media platforms and received a total of 73 responses. The demographic statistics of participants are as follows: 

- Age (ă18: 0%, 18-29: 69.86%, 30-44: 19.18%, 45-59: 

- 5.48%, ě60: 5.48%); 

- Gender (Female: 30.14%, Male: 65.75%, Non-binary: 

- 2.74%, Prefer not to say: 1.37%); 

- Music background (Amateur: 34.25%, Intermediate: 

- 41.1%, Professional: 24.66%); 

Years spent on studying music (None: 26.03%, 1 year: 6.85%, 2 years: 10.96%, 3-5 years: 13.7%, 6-10 years: 16.44%, ą10 years: 26.03%). 

The subjective evaluation results are shown in Figure 4, where the bar height represents the mean score, and the error bar represents the confidence intervals computed by within-subject ANOVA. The results show that our method significantly outperforms the baseline in most subjective metrics, proving the effectiveness of our system in generating high-quality electronic music with solid long-term structural consistency. 

## 5. CONCLUSION AND FUTURE WORK 

We contribute TOMI, a concept hierarchy paradigm for music representation, and combine it with an ICL approach to achieve the first system for generating long-term, multitrack electronic music with both MIDI and audio clips. Experimental results show that our approach achieves highquality generation with robust structural consistency. In addition, we integrate it with REAPER to support audio rendering and co-creation. However, harmonic coherence in our results can occasionally be disrupted by randomness and limited features during sample retrieval. Our system currently selects samples from local collections using a small feature set, which can lead to empty results or highly divergent samples. To improve this, we plan to integrate generative models for clips or use ML-based embedding models for MIDI and audio. Then, we aim to extend our model with a more sophisticated structural hierarchy to support advanced sound design and mixing. Lastly, we plan to train a TOMI-based neural network on music project files to enhance generation quality and scalability. 

342 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 6. REFERENCES 

- [1] Y. Huang, A. Ghatare, Y. Liu, Z. Hu, Q. Zhang, C. S. Sastry, S. Gururani, S. Oore, and Y. Yue, “Symbolic music generation with non-differentiable rule guided diffusion,” in Forty-first International Conference on Machine Learning, ICML 2024, Vienna, Austria, July 21-27, 2024. OpenReview.net, 2024. [Online]. Available: https://openreview.net/ forum?id=g8AigOTNXL 

- [2] L. Min, J. Jiang, G. Xia, and J. Zhao, “Polyffusion: A diffusion model for polyphonic score generation with internal and external controls,” in Proceedings of the 24th International Society for Music Information Retrieval Conference, ISMIR, 2023. 

- [3] S. Forsgren and H. Martiros, “Riffusion-stable diffusion for real-time music generation,” URL https://riffusion.com/about, 2022. 

- [4] G. Hadjeres, F. Pachet, and F. Nielsen, “DeepBach: a steerable model for Bach chorales generation,” in Proceedings of the 34th International Conference on Machine Learning, ser. Proceedings of Machine Learning Research, D. Precup and Y. W. Teh, Eds., vol. 70. International Convention Centre, Sydney, Australia: PMLR, 06–11 Aug 2017, pp. 1362–1371. [Online]. Available: http://proceedings.mlr.press/v70/ hadjeres17a.html 

- [5] A. Agostinelli, T. I. Denk, Z. Borsos, J. H. Engel, M. Verzetti, A. Caillon, Q. Huang, A. Jansen, A. Roberts, M. Tagliasacchi, M. Sharifi, N. Zeghidour, and C. H. Frank, “Musiclm: Generating music from text,” CoRR, vol. abs/2301.11325, 2023. [Online]. Available: https://doi.org/10.48550/arXiv.2301.11325 

- [6] J. Copet, F. Kreuk, I. Gat, T. Remez, D. Kant, G. Synnaeve, Y. Adi, and A. Défossez, “Simple and controllable music generation,” in Advances in Neural Information Processing Systems 36: Annual Conference on Neural Information Processing Systems 2023, NeurIPS 2023, New Orleans, LA, USA, December 10 - 16, 2023, A. Oh, T. Naumann, A. Globerson, K. Saenko, M. Hardt, and S. Levine, Eds., 2023. 

- [7] P. Dhariwal, H. Jun, C. Payne, J. W. Kim, A. Radford, and I. Sutskever, “Jukebox: A generative model for music,” CoRR, vol. abs/2005.00341, 2020. [Online]. Available: https://arxiv.org/abs/2005.00341 

- [8] R. Yuan, H. Lin, S. Guo, G. Zhang, J. Pan, Y. Zang, H. Liu, Y. Liang, W. Ma, X. Du, X. Du, Z. Ye, T. Zheng, Y. Ma, M. Liu, Z. Tian, Z. Zhou, L. Xue, X. Qu, Y. Li, S. Wu, T. Shen, Z. Ma, J. Zhan, C. Wang, Y. Wang, X. Chi, X. Zhang, Z. Yang, X. Wang, S. Liu, L. Mei, P. Li, J. Wang, J. Yu, G. Pang, X. Li, Z. Wang, X. Zhou, L. Yu, E. Benetos, Y. Chen, C. Lin, X. Chen, G. Xia, Z. Zhang, C. Zhang, W. Chen, X. Zhou, X. Qiu, R. Dannenberg, J. Liu, J. Yang, W. Huang, W. Xue, X. Tan, and Y. Guo, 

“Yue: Scaling open foundation models for longform music generation,” 2025. [Online]. Available: https://arxiv.org/abs/2503.08638 

- [9] Z. Wang, L. Min, and G. Xia, “Whole-song hierarchical generation of symbolic music using cascaded diffusion models,” in The Twelfth International Conference on Learning Representations, ICLR 2024, Vienna, Austria, May 7-11, 2024. OpenReview.net, 2024. [Online]. Available: https://openreview.net/forum?id=sn7CYWyavh 

- [10] S. Dai, Z. Jin, C. Gomes, and R. B. Dannenberg, “Controllable deep melody generation via hierarchical music structure representation,” in Proceedings of the 22nd International Society for Music Information Retrieval Conference, ISMIR 2021, Online, November 7-12, 2021, J. H. Lee, A. Lerch, Z. Duan, J. Nam, P. Rao, P. van Kranenburg, and A. Srinivasamurthy, Eds., 2021, pp. 143–150. [Online]. Available: https: //archives.ismir.net/ismir2021/paper/000017.pdf 

- [11] A. Roberts, J. H. Engel, C. Raffel, C. Hawthorne, and D. Eck, “A hierarchical latent vector model for learning long-term structure in music,” in Proceedings of the 35th International Conference on Machine Learning, ICML 2018, Stockholmsmässan, Stockholm, Sweden, July 10-15, 2018, ser. Proceedings of Machine Learning Research, J. G. Dy and A. Krause, Eds., vol. 80. PMLR, 2018, pp. 4361–4370. [Online]. Available: http://proceedings.mlr.press/v80/ roberts18a.html 

- [12] S. Dai, H. Yu, and R. B. Dannenberg, “What is missing in deep music generation? A study of repetition and structure in popular music,” in Proceedings of the 23rd International Society for Music Information Retrieval Conference, ISMIR 2022, Bengaluru, India, December 4-8, 2022, P. Rao, H. A. Murthy, A. Srinivasamurthy, R. M. Bittner, R. C. Repetto, M. Goto, X. Serra, and M. Miron, Eds., 2022, pp. 659–666. [Online]. Available: https: //archives.ismir.net/ismir2022/paper/000079.pdf 

- [13] D. Cope, “Recombinant music: Using the computer to explore musical style,” Computer, vol. 24, no. 7, pp. 22–28, 1991. [Online]. Available: https://doi.org/10. 1109/2.84830 

- [14] K. Chen, W. Zhang, S. Dubnov, G. Xia, and W. Li, “The effect of explicit structure encoding of deep neural networks for symbolic music generation,” in 2019 International Workshop on Multilayer Music Representation and Processing (MMRP). IEEE, Jan. 2019, p. 77–84. [Online]. Available: http: //dx.doi.org/10.1109/MMRP.2019.00022 

- [15] H. Chen, J. B. L. Smith, J. Spijkervet, J. Wang, P. Zou, B. Li, Q. Kong, and X. Du, “Sympac: Scalable symbolic music generation with prompts and constraints,” in Proceedings of the 25th International 

343 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

Society for Music Information Retrieval Conference, ISMIR 2024, San Francisco, California, USA and Online, November 10-14, 2024, B. Kaneshiro, G. J. Mysore, O. Nieto, C. Donahue, C. A. Huang, J. H. Lee, B. McFee, and M. C. McCallum, Eds., 2024, pp. 1029–1036. [Online]. Available: https://doi.org/10.5281/zenodo.14877507 

- [16] F. Pachet, A. Papadopoulos, and P. Roy, “Sampling variations of sequences for structured music generation,” in Proceedings of the 18th International Society for Music Information Retrieval Conference, ISMIR 2017, Suzhou, China, October 23-27, 2017, S. J. Cunningham, Z. Duan, X. Hu, and D. Turnbull, Eds., 2017, pp. 167–173. [Online]. Available: https://archives.ismir.net/ismir2017/paper/000050.pdf 

- [17] Y. Zou, P. Zou, Y. Zhao, K. Zhang, R. Zhang, and X. Wang, “Melons: Generating melody with long-term structure using transformers and structure graph,” in IEEE International Conference on Acoustics, Speech and Signal Processing, ICASSP 2022, Virtual and Singapore, 23-27 May 2022. IEEE, 2022, pp. 191–195. [Online]. Available: https://doi.org/10.1109/ ICASSP43922.2022.9747802 

- [18] M. Malandro, “Composer’s Assistant: An Interactive Transformer for Multi-Track MIDI Infilling,” in Proc. 24th Int. Society for Music Information Retrieval Conf., Milan, Italy, 2023, pp. 327–334. 

- [19] ——, “Composer’s Assistant 2: Interactive MultiTrack MIDI Infilling with Fine-Grained User Control,” in Proc. 25th Int. Society for Music Information Retrieval Conf., San Francisco, CA, USA, 2024, pp. 438– 445. 

- [20] R. Yuan, H. Lin, Y. Wang, Z. Tian, S. Wu, T. Shen, G. Zhang, Y. Wu, C. Liu, Z. Zhou, L. Xue, Z. Ma, Q. Liu, T. Zheng, Y. Li, Y. Ma, Y. Liang, X. Chi, R. Liu, Z. Wang, C. Lin, Q. Liu, T. Jiang, W. Huang, W. Chen, J. Fu, E. Benetos, G. Xia, R. B. Dannenberg, W. Xue, S. Kang, and Y. Guo, “Chatmusician: Understanding and generating music intrinsically with LLM,” in Findings of the Association for Computational Linguistics, ACL 2024, Bangkok, Thailand and virtual meeting, August 11-16, 2024, L. Ku, A. Martins, and V. Srikumar, Eds. Association for Computational Linguistics, 2024, pp. 6252–6271. [Online]. Available: https://doi.org/10.18653/v1/2024.findings-acl.373 

- [21] X. Qu, Y. Bai, Y. Ma, Z. Zhou, K. M. Lo, J. Liu, R. Yuan, L. Min, X. Liu, T. Zhang, X. Du, S. Guo, Y. Liang, Y. Li, S. Wu, J. Zhou, T. Zheng, Z. Ma, F. Han, W. Xue, and et al., “Mupt: A generative symbolic music pretrained transformer,” in The Thirteenth International Conference on Learning Representations, ICLR 2025, Singapore, April 24-28, 2025. OpenReview.net, 2025. [Online]. Available: https://openreview.net/forum?id=iAK9oHp4Zz 

- [22] ABC Wiki, “The abc notation system,” 2021. [Online]. Available: https://abcwiki.org/abc:syntax 

- [23] H. Touvron, T. Lavril, G. Izacard, X. Martinet, M.-A. Lachaux, T. Lacroix, B. Rozière, N. Goyal, E. Hambro, F. Azhar, A. Rodriguez, A. Joulin, E. Grave, and G. Lample, “Llama: Open and efficient foundation language models,” 2023. [Online]. Available: https://arxiv.org/abs/2302.13971 

- [24] P. Lu, X. Xu, C. Kang, B. Yu, C. Xing, X. Tan, and J. Bian, “Musecoco: Generating symbolic music from text,” 2023. [Online]. Available: https: //arxiv.org/abs/2306.00110 

- [25] H.-W. Dong, K. Chen, S. Dubnov, J. McAuley, and T. Berg-Kirkpatrick, “Multitrack music transformer,” in IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2023. 

- [26] J. Thickstun, D. L. W. Hall, C. Donahue, and P. Liang, “Anticipatory music transformer,” Trans. Mach. Learn. Res., vol. 2024, 2024. [Online]. Available: https: //openreview.net/forum?id=EBNJ33Fcrl 

- [27] S. Liu, A. S. Hussain, C. Sun, and Y. Shan, “Music understanding llama: Advancing text-to-music generation with question answering and captioning,” in IEEE International Conference on Acoustics, Speech and Signal Processing, ICASSP 2024, Seoul, Republic of Korea, April 14-19, 2024. IEEE, 2024, pp. 286–290. [Online]. Available: https: //doi.org/10.1109/ICASSP48485.2024.10447027 

- [28] Z. Kong, A. Goel, R. Badlani, W. Ping, R. Valle, and B. Catanzaro, “Audio flamingo: A novel audio language model with few-shot learning and dialogue abilities,” in Forty-first International Conference on Machine Learning, ICML 2024, Vienna, Austria, July 21-27, 2024. OpenReview.net, 2024. [Online]. Available: https://openreview.net/forum?id=WYi3WKZjYe 

- [29] OpenAI (2024), “Gpt-4o system card,” CoRR, vol. abs/2410.21276, 2024. [Online]. Available: https: //doi.org/10.48550/arXiv.2410.21276 

- [30] D. R. Hipp, “Sqlite,” 2004. [Online]. Available: https://www.sqlite.org 

- [31] ADSR, “Adsr sample manager,” n.d. [Online]. Available: https://www.adsrsounds.com/product/software/ adsr-sample-manager/ 

- [32] K. Kilgour, M. Zuluaga, D. Roblek, and M. Sharifi, “Fréchet audio distance: A reference-free metric for evaluating music enhancement algorithms,” in 20th Annual Conference of the International Speech Communication Association, Interspeech 2019, Graz, Austria, September 15-19, 2019, G. Kubin and Z. Kacic, Eds. ISCA, 2019, pp. 2350–2354. [Online]. Available: https://doi.org/10.21437/Interspeech.2019-2219 

344 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [33] H. H. Tan, “Frechet audio distance in pytorch,” https: //github.com/gudgud96/frechet-audio-distance, 2022. 

- [34] S. Hershey, S. Chaudhuri, D. P. W. Ellis, J. F. Gemmeke, A. Jansen, R. C. Moore, M. Plakal, D. Platt, R. A. Saurous, B. Seybold, M. Slaney, R. J. Weiss, and K. W. Wilson, “CNN architectures for large-scale audio classification,” in 2017 IEEE International Conference on Acoustics, Speech and Signal Processing, ICASSP 2017, New Orleans, LA, USA, March 5-9, 2017. IEEE, 2017, pp. 131–135. [Online]. Available: https://doi.org/10.1109/ICASSP. 2017.7952132 

- [35] Y. Wu, K. Chen, T. Zhang, Y. Hui, T. BergKirkpatrick, and S. Dubnov, “Large-scale contrastive language-audio pretraining with feature fusion and keyword-to-caption augmentation,” in IEEE International Conference on Acoustics, Speech and Signal Processing ICASSP 2023, Rhodes Island, Greece, June 4-10, 2023. IEEE, 2023, pp. 1–5. [Online]. Available: https://doi.org/10.1109/ICASSP49357.2023.10095969 

- [36] J. Joven, “Minty fresh: Spotify makes a new home for edm,” 2018. [Online]. Available: https://hmc.chartmetric.com/ minty-fresh-spotify-makes-a-new-home-for-edm/ 

- [37] J. Cohen, Statistical Power Analysis for the Behavioral Sciences, 2nd ed. Hillsdale, NJ: Lawrence Erlbaum Associates, 1988. 

- [38] Y. Li, R. Yuan, G. Zhang, Y. Ma, X. Chen, H. Yin, C. Xiao, C. Lin, A. Ragni, E. Benetos, N. Gyenge, R. B. Dannenberg, R. Liu, W. Chen, G. Xia, Y. Shi, W. Huang, Z. Wang, Y. Guo, and J. Fu, “MERT: acoustic music understanding model with large-scale self-supervised training,” in The Twelfth International Conference on Learning Representations, ICLR 2024, Vienna, Austria, May 7- 11, 2024. OpenReview.net, 2024. [Online]. Available: https://openreview.net/forum?id=w3YZ9MSlBu 

345 

