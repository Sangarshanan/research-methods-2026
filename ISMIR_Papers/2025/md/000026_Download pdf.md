---
paper_id: "000026"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706377/files/000026.pdf"
---

# GENERATING SYMBOLIC MUSIC FROM NATURAL LANGUAGE PROMPTS USING AN LLM-ENHANCED DATASET 

Weihan Xu<sup>1</sup> Julian McAuley<sup>2</sup> Taylor Berg-Kirkpatrick<sup>2</sup> Shlomo Dubnov<sup>2</sup> Hao-Wen Dong<sup>3</sup> 1Duke University 2UC San Diego 3University of Michigan 

```
weihan.xu@duke.edu
```

### ABSTRACT 

Recent years have seen many audio-domain text-to-music generation models that rely on large amounts of text-audio pairs for training. However, symbolic-domain controllable music generation has lagged behind partly due to the lack of a large-scale symbolic music dataset with extensive metadata and captions. In this work, we present MetaScore, a new dataset consisting of 963K musical scores paired with rich metadata, including free-form userannotated tags, collected from an online music forum. To approach text-to-music generation, We employ a pretrained large language model (LLM) to generate pseudonatural language captions for music from its metadata tags. With the LLM-enhanced MetaScore, we train a textconditioned music generation model that learns to generate symbolic music from the pseudo captions, allowing control of instruments, genre, composer, complexity and other free-form music descriptors. In addition, we train a tagconditioned system that supports a predefined set of tags available in MetaScore. Our experimental results show that both the proposed text-to-music and tags-to-music models outperform a baseline text-to-music model in a listening test. While a concurrent work Text2MIDI [1] also supports free-form text input, our models achieve comparable performance. Moreover, the text-to-music system offers a more natural interface than the tags-to-music model, as it allows users to provide free-form natural language prompts. 

## 1 Introduction 

Recent work has been investigating the potential of conditional music generation with state-of-the-art machine learning models. In particular, we have seen major progress in audio-domain controllable music generation [2, 3], largely thanks to the vast amount of text-audio pairs for training. Unlike audio-domain music generation, sym- 

> © Weihan Xu, Julian McAuley, Taylor Berg-Kirkpatrick, Shlomo Dubnov and Hao-Wen Dong. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: Weihan Xu, Julian McAuley, Taylor Berg-Kirkpatrick, Shlomo Dubnov and Hao-Wen Dong, “Generating Symbolic Music from Natural Language Prompts using an LLM-Enhanced Dataset”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 



<!-- Start of picture text -->
Difficulty<br>Instrument This is an easy classical<br>piano piece composed by MetaScore<br>Composer wolfgang amadeus mozart.<br>MetaScore<br>Transformer<br><!-- End of picture text -->

Figure 1. Leveraging the LLM-enhanced MetaScore dataset, our proposed MetaScore Transformer (MST) model generates symbolic music using natural language prompts with difficulty, genre, instrument and composer controls. The symbolic music outputs allow the user to further edit and complete the composition. 

bolic music generation systems generate music in editable formats that can be further completed by the users, making it easier for musicians to integrate such systems into their creative workflow. However, symbolic-domain controllable music generation has been hindered by the lack of a large, public symbolic music dataset with rich metadata. In this paper, we intend to build a natural language based symbolic music generation system with our new public dataset MetaScore. MetaScore contains 963K musical scores paired with rich metadata collected from the MuseScore forum<sup>1</sup> as well as extensive metadata such as genre, composer, complexity, time signature, key signature, tempo and user interaction statistics (e.g., number of views, likes and comments).<sup>2</sup> In order to approach text to music generation, we further enhance the MetaScore dataset by completing missing genre metadata using a machine learning-based genre tagging algorithm and we leverage large language models to convert the metadata into natural language captions. 

Enabled by the metadata provided in MetaScore, we explore text-conditioned music generation with controllable attributes such as instrument, genre, composer, complexity, and other free-form musical descriptors expressed in natural language. With the LLM-enhanced dataset, we train a transformer-based text-to-music model using a pretrained large language model to encode the input text 

> 1 `https://musescore.com/` 

> 2 We note a concurrent work, MidiCaps [4], which contains 168K MIDI files annotated with genre, emotion tags, and LLM-generated captions. However, it does not include composer names, complexity levels, user statistics, and free-form user-annotated tags (see Table 1). 

215 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

|||||Multi-|||Met|adata|||
|---|---|---|---|---|---|---|---|---|---|---|
||Format|Genre|Samples|track|Genre|Composer|Emotion|Complexity|UIS<sup>‡</sup>|Caption|
|LMD [5]|MIDI|Misc.|176,581|✓|×<sup>†</sup>|×<sup>†</sup>|×|×|×|×|
|MetaMIDI [6]|MIDI|Misc.|437K|✓|✓|✓|×|×|×|×|
|WikiMusicText [7]|ABC|Misc.|1,010<sup>∗</sup>|×|✓|✓|×|×|×|✓|
|EMOPIA [8]|MIDI|Pop|1,087|×|✓|×|✓|×|×|×|
|MAESTRO [9]|MIDI|Classical|1,276|×|✓|✓|×|×|×|×<br>|
|MidiCaps [4]|MIDI|Misc.|168K|✓|✓|×|✓|×|×|✓<sup>§</sup>|
|MetaScore|XML|Misc.|1.27M|✓|✓|✓|×|✓|✓|✓<sup>§</sup>|
|∗Only a small subs<br>†Available through e|et of WikiM<br>rror-prone m|usicText is pu<br>apping to Mi|blicly availab<br>llion Song Da|le at`http`<br>taset [5,10|`s://hugg`<br>]<br>‡User|`ingface.co/`<br>interaction st|`datasets/s`<br>atistics<br>§L|`ander-wood/w`<br>LM-generated (|`ikimusi`<br>see Secti|`ctext`<br>on3.4)|



Table 1. Comparison of commonly used publicly available symbolic music datasets 

||Model<br>size|Public<br>training data|Open<br>source|Supports<br>drums|Supports free<br>text prompts|Instrument|C<br>Genre|ontrols<br>Composer|Complexity|
|---|---|---|---|---|---|---|---|---|---|
|FIGARO [11]|88.30M|✓|✓|×|×|✓|×|×|×|
|MuseCoco [12]|203M|×|✓|✓|×|✓|✓|✓|×|
|BART-based [13]|139M|✓|✓|×|✓|✓|✓|×|×|
|MST-Tags|87.36M|✓|✓|✓|×|✓|✓|✓|✓|
|MST-Text|87.44M|✓|✓|✓|✓|✓<sup>∗</sup>|✓<sup>∗</sup>|✓<sup>∗</sup>|✓<sup>∗</sup>|
|||∗T|hese can be|achieved by f|ree-form text prom|pts.||||



Table 2. Comparison of controllable music generation systems. 

prompts (see Figure 1). In addition, we train a transformerbased tags-to-music model by prepending the input tags to our proposed music representation. Leveraging the LLMgenerated captions for training, the proposed text-to-music model achieves competitive performance against the tagbased model while offering a natural language-based interface that allows free-form text inputs. 

To evaluate our proposed models, we compare them with an open-source text-to-symbolic music system [13] and a concurrent work [1] in subjective listening studies. In these studies, we demonstrate that our proposed models outperform the baseline model in terms of coherence, arrangement, adherence, and overall quality, while achieving performance comparable to that of the concurrent work [1]. 

tion, which does not support multitrack music natively. Although MetaMIDI [6] comprises around 437K multitrack music pieces in MIDI format, it only includes genre and composer information, lacking natural language captions, which are important for training text-to-music generation models. Although EMOPIA [8] provides emotion information, it is small and contains only pop music. Although MidiCaps [4] contains captions, it does not contain userannotated free-form tags that are crucial for free-form textto-music generation. In this work, we present a new, large multitrack and multi-genre symbolic music dataset with rich metadata, including genre, composer, complexity, key signature, time signature, tempo, user interaction statistics, free-form user annotated tags and pseudo captions. 

Our contributions can be summarized as follows: 

   - We present a new publicly available dataset with musical scores paired with rich metadata and LLMgenerated natural language captions. 

- We train two new models for tag- and text-based controllable symbolic music generation that support instrument, genre, composer and complexity controls. 

- The MetaScore dataset, codebase, and audio samples 

- can be found on our website.<sup>3</sup> 

## 2 Related Work 

### 2.1 Symbolic Music Datasets 

We compare commonly used symbolic music datasets in Table 1. WikiMusicText [7] pairs music with genre, composer, and captions. However, its publicly released version is small, and the musical scores are in ABC nota- 

> 3 `https://wx83.github.io/MetaScore_Official/` 

### 2.2 Controllable Symbolic Music Generation 

Controllable symbolic music generation include attributebased music generation, free-form text to music generation and music infilling. We compare our model with existing controllable music generation system in Table 2. EMOPIA [8] is designed to generate music that aligns with specific emotional states, defined within the valencearousal plane. This psychological model categorizes emotions by valence, indicating their positivity or negativity, and arousal, which measures their intensity from calm to excited. FIGARO [11] can generate samples based on a fine-grained description of the characteristics of the desired music. MuseCoco [12] first classifies a fixed set of predefined musical attributes using multiple classification heads and then employs an attribute-to-music model to generate symbolic music. Recent work on music infilling [14] can condition generation on attributes including: instrument type, musical style, note density, polyphony level, 

216 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
Complexity Distribution Most Common 10 Tempo # Views Distribution<br>0-5<br>Easy<br>Most Common 10 Instruments Views 5-10<br>10-100<br>Piano<br>100-+<br>Complexity Level<br>Flute  0.5 1.0 1.5Count2.0 2.5 3.0 0.0 0.5 1.0 1.5Count2.0 2.5 3.0 ×10°<br>Trombone Count ×103<br>Most Common 10 Key Signature # Comments Distribution<br>Violin 0-1<br>Tuba 1-5<br>Instruments Viola Comments10-1005-10<br>Keygte Sure<br>Oboe 100-+<br>Count<br>Bass Count ×104 Count<br>Bassoon<br>Most Common 10 Genre (Raw) Most Common 10 Time Signature 0-5<br>Timpani0.0 0.5 1.0Count1.5 2.0 ×1052.5 FavVorsS10-1005-10<br>100-+<br>Count 2Count ×20° 0.0 0.5 1.0Count1.5 2.0 ×10<br><!-- End of picture text -->

Figure 2. Statistics of the metadata available in MetaScore-Raw. Note that not all songs include complete metadata. We derive exact keys by merging user annotations with the MusicXML key element (fifths + mode). C major and A minor are underrepresented because we include only pieces with explicitly specified keys. 

and note duration. In this work, we explore free-form text conditioned music generation with LLM-generated natural language music captions. Additionally, we present a tag-conditioned music generation model that can generate music based on four conditions: genre, instrument, complexity and composer. 

## 3 Dataset 

### 3.1 Dataset Collection 

We scraped our dataset from an open source and free music notation software MuseScore.<sup>1</sup> To evaluate the quality of our dataset, we leverage the rating entry (MetaScore-Raw) as an indicator. This rating, which ranges from 1 to 5 (with 5 being the highest), serves as a structured measure of perceived music quality. To demonstrate that even lower-rated entries can still be suitable for use, we randomly selected 10 samples from three categories: low/missed ratings (below 3 or not rated), mid-range ratings (3–4), and high ratings (above 4). We show qualitative examples on our demo page.<sup>3</sup> These examples illustrate the overall usability and diversity of the dataset across different rating levels. 

### 3.2 Collecting and Preprocessing the Dataset 

We collect 963K songs paired with musical scores and metadata from the MuseScore forum. We will refer to this original dataset as MetaScore-Raw. MetaScore-Raw contains extensive metadata such as genre, composer, complexity, key signature, time signature, tempo, user interaction statistics (e.g., number of views, likes and comments) and free-form user annotated tags. We provide statistics of the metadata in Figure 2, and we note that not all songs come with complete metadata. 

From the raw MSCZ files, we extract key signature, time signature, tempo and musical instrumentation. We 

|Type|Dataset|Adherence↑|
|---|---|---|
|Ground truth genre tags|MetaScore-Genre|3.11±0.49|
|Auto-generated genre tags|MetaScore-Plus<sup>∗</sup>|3.05±0.54|
|LLM-generated captions|MetaScore-Plus|3.23±0.49|
|∗We only include songs wi|th auto-generated genre|tags here.|



Table 3. Subjective evaluation results on tags/text-music adherence of the dataset are measured on a Likert scale of 1 to 5. We report the mean values and 95% confidence intervals. 

only retain those instruments that are compatible with the General MIDI standard. Regarding composers, we first filter the composer tags to ensure they are formatted as human names and convert them to lowercase. We also standardize the names of well-known musicians to their full names; for instance, “mozart” is changed to “wolfgang amadeus mozart.” 

### 3.3 Inferring Missing Genre Tags in MetaScore-Raw 

While MetaScore-Raw provides rich metadata information, we notice that not all songs come with complete metadata. For example, only 181K (18.8%) out of 963K songs in MetaScore-Raw contain genre metadata. As genre is one of the most intuitive ways for a user to control the style for a music generation system, we want to complete the genre information for songs without a genre label in MetaScore-Raw. Therefore, we train a genre tagger that is based on the Multitrack Music Transformer (MMT) [15], where we remove the causal mask used for autoregressive modeling and append a multi-label classification layer. We select the threshold of the multi-label classification layer for each class based on the F1 score on the validation set. 

To infer genre labels for music pieces lacking such tags, we adopt a data-driven approach by training a genre tag- 

217 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

ger on MetaScore-Genre. The genre tagger is based on the Multitrack Music Transformer (MMT) [15], where we remove the casual mask used for autoregressive modeling and append a multi-label classification layer. MMT represents a music piece as a sequence of events x = (x1, . . . , xn), where each event xi comprises six attributes: type, beat, position, pitch, duration, and instrument. To create the input sequence, we extract tokens from the start, middle, and end sections of each music pieces, selecting 341 tokens from each to form a concatenated sequence of 1,023 tokens. Instrument information, important for genre identification, is also incorporated as a prefix condition to these sequences. 

During training, genres with scarce presence or high ambiguity, such as “darkwave” and “experimental,” are excluded to avoid noise. We extract notes from the MSCZ files using MusPy [15]. When we extract notes, we exclude broken files containing negative pitches. Moveover, to enhance generalizability, we include additional 22,000 samples from the LMD dataset [5], all tagged with genres. Due to the rarity or ambiguity of certain genres, we merge specific genre types from these two datasets into 8 classes.<sup>4</sup> For the training process, we allocate 90% of the samples for training, with 5% each reserved for validation and testing. We select the threshold of multi-label classification layer for each class based on the performance on the validation set. 

To evaluate the performance of genre tagging, we first compute the precision, recall and F1-score on the test set, where we achieve a micro-averaged precision of 61.94, recall of 63.03, and F1 score of 62.48. In addition, we conduct a subjective listening test to compare the quality of the auto-generated genre tags with the user-annotated tags in MetaScore-Raw. The 22 participants are instructed to answer the following question in a Likert scale of 1 to 5: “How well do you think this piece of music aligns with the following genre?”. From Table 3, we can see that the autogenerated genre tags in MetaScore-Plus achieves a lower tags-music adherence compared to the ground truth tags in MetaScore-Genre(defined in Section 4), but the difference did not reach statistical significance in our setup. 

### 3.4 Generating Pseudo Captions using LLMs 

To enable text-based downstream tasks (e.g., music captioning and text-to-music generation), we leverage large language models to convert the metadata into natural language captions. We follow LP-MusicCaps [16] and CLAP [17] and adopt an in-context learning-based approach [18] using a pretrained large language model. We form the input prompt string by combining genre, composer, complexity, time signature, key signature, tempo, and freeform user-specified tags.<sup>5</sup> As shown on the demo page,<sup>3</sup> 

> 4 We define the eight genres as follows: “Classical & traditional”: classical, religious, new age; “Soundtrack & stage”: soundtrack, comedy; “Rock& Metal”: pop, rock, metal; “Folk & country”: folk, country; “Urban”: hip hop, r&b, funk&soul; “Electronic & dance”: electronic, disco; “World”: world music, reggae&ska; “Jazz & blues”: jazz, blues. 

> 5 We have an old version of LLM-generated captions from tags. MSTText was trained on an old version of LLM-generated captions in which 

we provide five examples of input-output pairs to facilitate in-context learning with Bloom [19], where the examples are used to provide guidance for the LLM to capture the one-to-many mapping between the input tags and natural language captions. We generate the pseudo captions using the Hugging Face API [20]. We exclude non-English and corrupted captions generated by Bloom [19] and truncate the output sequence to a maximum of 32 tokens. 

## 4 Versions of MetaScore 

We will release the following three versions of MetaScore: 

- MetaScore-Raw (963K): The raw MuseScore files and metadata scraped from the MuseScore forum as well as the corresponding musicxml file for future research. 

- Metascore-Genre (181K): A subset of MuseScoreRaw containing files with user-annotated genres. Additionally, we discard any songs composed by a composer that has less than 100 compositions in MetaScore-Raw. We also provide LLM-generated captions based on information extracted from the metadata in Metascore-Genre. 

- MetaScore-Plus (963K): MetaScore-Raw where missing genre tags are completed by the trained genre tagger described in Section 3.3. We also provide LLM-generated captions based on information extracted from the metadata in MetaScore-Plus. 

Due to copyright concerns, we will publicly release music scores and metadata that are in the public domain (228K) or licensed with a Creative Commons licenses (46K) from MetaScore-Plus. The rest of the dataset will be provided upon request for research purpose. 

## 5 Method 

We represent a music piece as a one-dimensional array of integers using an event-based representation adapted from REMI+ [11] and MMT [15]. REMI+ [11] represents notes with six consecutive tokens encoding note position, pitch, velocity, duration, instrument and time-signature information. However, it cannot provide control over tags such as genre, composer and complexity. MMT [15] represents a sequence of six-dimension events, with each event xi encoded as a tuple of variables (x<sup>type</sup> , x<sup>beat</sup> , x<sup>position</sup> , x<sup>pitch</sup> , x<sup>duration</sup> , x<sup>instrument</sup> ). However, MMT cannot model the interdependencies within these fields for a specific note as it predicts the six fields in parallel. In this work, we adapt the REMI+ representation [11] to provide controls over genre, instrument, composer and complexity, while preserving the expressiveness offered by REMI+ [11]. Similar to MMT [15], we decompose note-on events to beat and position to reduce the size of the vocabulary and to help the model learn the rhythmic structure of music. In addition, we exclude the “tempo” and “chord” events as such information is sometimes unavailable in our dataset. 

captions are generated from genre, instrument, complexity, copyright, and free-form descriptors with in-context learning. 

218 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

Following REMI+ [11], we use beat, position, instrument, pitch and duration events for representing musical notes for non-drum tracks. We represent drum notes as beat, position, instrument, drum_pitch. 

To enable free-form text controls, for each music piece with text, we use a pretrained sentence transformer [21] (specifically, the “all-MiniLM-L6-v2” version [22]) to extract the text embedding. Then we add a linear layer to project the text embedding to the input token embedding space, where the projected text embedding is added to the previous generated token embedding along with the positional encoding. Then we feed the encoded sequence into a decoder-only linear transformer. We will refer to this model as MetaScore Transformer-Text (MST-Text). 

Additionally, we train a tag-conditioned music generation model. To enable tag-based controls, we prepend the input tags to our proposed music representation. We introduce four tag events, including tag_genre, tag_composer, tag_complexity and tag_instrument to specify conditions. Further, we use the standardized composer names to limit the vocabulary size, and we keep only 47 composers that have more than 100 training samples. We use a tag_{missing_tag}_None event for music pieces that do not contain all four tags. In addition to these data tokens, we have six special structural events: The start-ofsong event signals the onset of a song, leading into a sequence marked by start-of-genre, start-of-composer, startof-complexity, start-of-instrument events, each followed by their respective tag lists, with start-of-notes concluding the tag lists and end-of-song indicating the completion of the song. To facilitate controllability in the model, we prepend these control tokens at the start of the data representation. The control tokens include genre, composer, complexity and instruments. Then we feed the sequence with these prepending tags into a decoder-only linear transformer which capitalizes on the autoregressive nature of the transformer model, enabling the integration of these tokens during the inference process. We will refer to this model as MetaScore Transformer-Tags (MST-Tags). 

## 6 Experiments and Results 

### 6.1 Baselines 

We compare our model with two text-to-symbolic music generation approaches. The first is a BART-based model [13] trained on a paired text and symbolic dataset using ABC notation, with evaluation presented in Section 6.2 and Section 6.3. The second is a concurrent approach, Text2MIDI [1], which directly generates MIDI files from natural language prompts, with evaluation presented in Section 6.4. MuseCoco [12] first classifies a fixed set of predefined musical attributes using multiple classification heads and then employs an attribute-to-music model to generate symbolic music. This approach does not support free-form natural language inputs for symbolic music generation. The BART-based model [13] leverages pretrained language models for generating symbolic music in ABC notation. To ensure a fair comparison, we generate 

||Pitch class<br>entropy|Scale<br>consistency|Groove<br>consistency|
|---|---|---|---|
|MST-Tags-Small|2.88±0.08|0.89±0.02|0.92±0.01|
|MST-Tags|2.93±0.07|0.89±0.02|0.90±0.01|
|BART-based [13]|2.54±0.06|0.99±0.00|1.00±0.00|
|MST-Text|2.70±0.06|0.95±0.01|0.92±0.01|
|Ground truth|2.67±0.06|0.95±0.01|0.92±0.01|



Table 4. Objective evaluation results on music quality with conditions from MST test set. We report the mean values and 95% confidence intervals. 

music using the BART-based model [13] via the Hugging Face API [22] and then convert the ABC outputs to multitrack MIDI using the Melobytes tool [23]. 

### 6.2 Objective Evaluations 

Following [15, 24, 25], we assess the quality of generated music using pitch class entropy, scale consistency, and groove consistency, where values closer to the ground truth indicate better performance. To ensure a fair comparison, we randomly sampled 100 conditions from the MST test set and generated corresponding music for evaluation. As reported in Table 4, we find that MST-Text most closely matches the ground truth in terms of pitch class entropy and scale consistency, while MST-Tags-Small and MSTText perform similarly on groove consistency. Additionally, our proposed MST-Text outperforms the BART-based [13] model across all three metrics. 

### 6.3 Subjective Evaluation 

We conduct a subjective test where 22 participants are instructed to evaluate five songs under each scenario. Out of the 22 participants, 19 people have experience in playing instruments, with two being professional musicians. We ask the participants to evaluate the audio samples in terms of coherence, arrangement, adherence and overall quality in a Likert scale of 1 to 5. 

We report the subjective evaluation results in Table 5. When contrasting MST-Tags-Small with MSTTags, we observe that MST-Tags achieves better performance in coherence and arrangement, but we see a decrease in adherence, possibly due to the incorporation of some auto-generated tags. This comparison illustrates the trade-off between employing a smaller, highquality dataset (MetaScore-Genre) versus a larger yet noisy dataset (MetaScore-Plus). However, comparing the overall quality score of MST-Tags-Small and MST-Tags, we see that training with a larger dataset leads to an increase in the overall quality of music generation. 

For text-conditioned music generation, MST-Text outperforms the BART-based [13] approach, in terms of coherence, arrangement, adherence, and overall quality. We observe that the text-conditioned system MST-Text has a lower adherence against MST-Tags-Small and MST-Tags. This implies that text-to-music generation is a more challenging task than tag-to-music generation as a text-to- 

219 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

||Model size|Training samples|Coherence↑|Arrangement↑|Adherence↑|Overall quality↑|
|---|---|---|---|---|---|---|
|MST-Tags-Small|87.36M|150K|3.87±0.36|3.98±0.38|3.86±0.38|3.57±0.37|
|MST-Tags|87.36M|901K|4.01±0.37|4.06±0.39|3.60±0.49|3.66±0.45|
|BART-based [13]|139M|283K|3.86±0.30|3.63±0.39|2.81±0.50|3.29±0.42|
|MST-Text|87.44M|560K|3.93±0.28|3.88±0.33|3.35±0.44|3.69±0.33|



Table 5. Subjective evaluation results in a Likert scale of 1 to 5 

||Model|CL|AP Sco|re↑|Cohe|rence|(%)↑|Arra|ngem|ent(%)↑|Adh|erenc|e(%)↑|Ove|rall qu|ality(%)↑|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||size|M|T|M+T|M|T|M+T|M|T|M+T|M|T|M+T|M|T|M+T|
|Text2MIDI [1]|159M|0.23|0.20|0.22|0|40|20|40|50|45|40|80|60|40|60|50|
|MST-Text|87.44M|0.36|0.13|0.24|100|60|80|60|50|55|60|20|40|60|40|50|



Table 6. Comparison of MST-Text and Text2MIDI [1] on three prompt sets: 1) M: five prompts from our test set, 2) T: five prompts from the Text2MIDI [1] test set, and 3) M+T: the union of these two prompt sets. We report the winning rates in a subjective A/B listening test described in Section 6.4. 

music generation system needs to learn to interpret the free-form text inputs. 

Overall, the tag-conditioned systems, MST-Tags and MST-Tags-Small, demonstrate strong performance across multiple dimensions, including coherence, arrangement, adherence to prompts, and overall music quality. These results highlight the high quality of our constructed dataset. Notably, MST-Text achieves the highest score in overall quality, indicating that our text-conditioned model performs on par with the tag-conditioned variants. This underscores the effectiveness of our approach, which leverages a large language model to generate natural language captions, enabling end-to-end training for high-quality text-tomusic generation. 

### 6.4 Comparison to Text2MIDI 

In this section, we compare our proposed MST-Text with a concurrent work Text2MIDI [1] that also supports text-tosymbolic music generation. For a fair comparison, we create three test sets: 1) five text prompts randomly selected from our test set, 2) five text prompts randomly selected from the Text2MIDI test set, and 3) the union of the previous two test sets (i.e., five prompts from each test set). 

Objective Evaluation. We compare music quality of our MST-Text and Text2MIDI [1] using pitch class entropy, scale consistency, and groove consistency, and report the results in Table 7. In addition, to assess the alignment between text and symbolic music, we report the average semantic similarity computed with CLAP [17]. We find that MST-Text better matches the ground truth in terms of pitch class entropy and scale consistency, while Text2MIDI better matches the ground truth in terms of groove consistency. Additionally, MST-Text shows better alignment performance when prompts are taken from the MST-Text test set and the joint test set. 

Subjective Evaluation. We compare our model MSTText with Text2MIDI [1] via an A/B test on coherence, arrangement, adherence, and overall quality. Eleven participants (9 with musical experience, including one professional) evaluated 5 prompts from our test set and 5 from the 

||Pitch class<br>entropy|Scale<br>consistency|Groove<br>consistency|
|---|---|---|---|
|Text2MIDI [1]|2.44±0.19|0.89±0.03|0.94±0.01|
|MST-Text|2.65±0.08|0.96±0.02|0.92±0.01|
|Ground truth|2.71±0.07|0.96±0.02|0.94±0.01|



Table 7. Objective evaluation results on music quality for the joint test set. We report the mean values and 95% confidence intervals. 

Text2MIDI test set, with results summarized in Table 6. 

Our experiments show that MST-Text produces more coherent results and achieves equal or superior arrangement performance compared to Text2MIDI [1]. However, when it comes to adherence, Text2MIDI outperforms MST-Text on the Text2MIDI test set and the joint test sets, while MST-Text performs better on MST-Text test set. Overall, both models deliver comparable quality. 

## 7 Conclusion 

In this paper, we have introduced MetaScore, a new publicly available dataset containing rich metadata and LLMgenerated captions. We also present a new music generation model that can generate symbolic music from freeform text, allowing controls over instruments, genre, composer, complexity, among other music descriptors. In addition, the LLM-generated pseudo captions contain information provided in free-form user-annotated tags, which can pose a challenge to systems that adopt a predefined set of tags [12]. Our objective and subjective evaluation results show the effectiveness of the proposed tags-to-music and text-to-music models. Our proposed text-to-music model outperforms a baseline text-to-music model [13] and achieves comparable performance with a concurrent work [1]. In addition, the proposed text-to-symbolic music generation model trained with LLM-generated pseudo captions achieves competitive performance against the proposed tags-to-music model trained using only the ground truth tags. 

220 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 8 Ethics Statement 

We note that MetaScore contains many copyrighted contents. This raises concerns of potential misuse of this dataset that can lead to severe copyright infringements. To minimize such risks, we will release those in public domain only and those not in public domain will be shared upon request and only use for research pruporse. Further, music generation systems built upon the MetaScore dataset may infringe the copyright held by the content creators, and thus we must be careful about adopting these systems in commercial applications. However, we would like to point out that when used properly and with caution, a text-to-music generation system can also make a positive impact to society by enabling new opportunities and interfaces for music creation, as demonstrated in [26]. Given the editable nature of symbolic music, we hope our proposed text-to-symbolic music models will open up new pathways towards human-AI music co-creation. 

- [9] C. Hawthorne, A. Stasyuk, A. Roberts, I. Simon, C.Z. A. Huang, S. Dieleman, E. Elsen, J. Engel, and D. Eck, “Enabling factorized piano music modeling and generation with the MAESTRO dataset,” in Proc. ICLR, 2019. 

- [10] T. Bertin-Mahieux, D. P. Ellis, B. Whitman, and P. Lamere, “The million song dataset,” in Proc. ISMIR, 2011. 

- [11] D. von Rütte, L. Biggio, Y. Kilcher, and T. Hofmann, “FIGARO: Controllable music generation using learned and expert features,” in Proc. ICLR, 2023. 

- [12] P. Lu, X. Xu, C. Kang, B. Yu, C. Xing, X. Tan, and J. Bian, “MuseCoco: Generating symbolic music from text,” in arXiv preprint arXiv:2306.00110, 2023. 

- [13] S. Wu and M. Sun, “Exploring the efficacy of pretrained checkpoints in text-to-music generation task,” in arXiv preprint arXiv:2211.11216, 2022. 

## 9 References 

- [1] K. Bhandari, A. Roy, K. Wang, G. Puri, S. Colton, and D. Herremans, “Text2midi: Generating symbolic music from captions,” 2024. [Online]. Available: https://arxiv.org/abs/2412.16526 

- [2] S.-L. Wu, C. Donahue, S. Watanabe, and N. J. Bryan, “Music controlnet: Multiple time-varying controls for music generation,” in arXiv preprint arXiv:2311.07069, 2023. 

- [3] Z. Novack, J. McAuley, T. Berg-Kirkpatrick, and N. J. Bryan, “DITTO: Diffusion inference-time t- optimization for music generation,” in arXiv preprint arXiv:2401.12179, 2024. 

- [4] J. Melechovsky, A. Roy, and D. Herremans, “Midicaps: A large-scale midi dataset with text captions,” 2024. [Online]. Available: https://arxiv.org/abs/2406.02255 

- [5] C. Raffel, “Learning-based methods for comparing sequences, with applications to audio-to-MIDI alignment and matching,” Ph.D. dissertation, Columbia University, 2016. 

- [6] J. Ens and P. Pasquier, “Building the MetaMIDI dataset: Linking symbolic and audio musical data,” in Proc. ISMIR, 2021. 

- [7] S. Wu, D. Yu, X. Tan, and M. Sun, “Clamp: Contrastive language-music pre-training for cross-modal symbolic music information retrieval,” in Proc. ISMIR, 2023. 

- [8] H.-T. Hung, J. Ching, S. Doh, N. Kim, J. Nam, and Y.H. Yang, “EMOPIA: A multi-modal pop piano dataset for emotion recognition and emotion-based music generation,” in Proc. ISMIR, 2021. 

- [14] P. Pasquier, J. Ens, N. Fradet, P. Triana, D. Rizzotti, J.-B. Rolland, and M. Safi, “Midi-gpt: A controllable generative model for computer-assisted multitrack music composition,” 2025. [Online]. Available: https: //arxiv.org/abs/2501.17011 

- [15] H.-W. Dong, K. Chen, S. Dubnov, J. McAuley, and T. Berg-Kirkpatrick, “Multitrack music transformer,” in Proc. ICASSP, 2023. 

- [16] S. Doh, K. Choi, J. Lee, and J. Nam, “LP-MusicCaps: LLM-based pseudo music captioning,” in Proc. ISMIR, 2023. 

- [17] Y. Wu, K. Chen, T. Zhang, Y. Hui, M. Nezhurina, T. Berg-Kirkpatrick, and S. Dubnov, “Large-scale contrastive language-audio pretraining with feature fusion and keyword-to-caption augmentation,” in Proc. ICASSP, 2023. 

- [18] Q. Dong, L. Li, D. Dai, C. Zheng, Z. Wu, B. Chang, X. Sun, J. Xu, L. Li, and Z. Sui, “A survey on incontext learning,” in arXiv preprint arXiv:2301.00234, 2023. 

- [19] T. L. Scao, A. Fan, C. Akiki, E. Pavlick, S. Ili´c, D. Hesslow, and et al., “Bloom: A 176b-parameter open-access multiliguai language model,” in arXiv preprint arXiv:2211.05100, 2022. 

- [20] BigScience, T. L. Scao, A. Fan, C. Wolf, T. Rush, S. Biderman, G. B. Black, S. Curtis, D. Elbayad, T. Gao et al., “BLOOM: A 176b-parameter open-access multilingual language model,” https://huggingface.co/ bigscience/bloom, 2022, accessed: 2025-03-25. 

- [21] N. Reimers and I. Gurevych, “Sentence-BERT: Sentence embeddings using siamese bert-networks,” in Proc. EMNLP, 2019. 

221 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [22] ——, “all-minilm-l6-v2: A lightweight sentence embedding model,” https://huggingface.co/ sentence-transformers/all-MiniLM-L6-v2, 2021, accessed: 2025-03-25. 

- [23] “Melobytes ABC to MIDI Converter,” https: //melobytes.com/en/app/abc2midi, accessed: 2025-0325. 

- [24] O. Mogren, “C-RNN-GAN: Continuous recurrent neural networks with adversarial training,” in Proc. NeurIPS Workshop on Constructive Machine Learning, 2016. 

- [25] S.-L. Wu and Y.-H. Yang, “The Jazz Transformer on the front line: Exploring the shortcomings of AIcomposed music through quantitative measures,” in Proc. ISMIR, 2020. 

- [26] C.-Z. A. Huang, H. V. Koops, E. Newton-Rex, M. Dinculescu, and C. J. Cai, “Ai song contest: Human-ai co-creation in songwriting,” 2020. [Online]. Available: https://arxiv.org/abs/2010.05388 

222 

