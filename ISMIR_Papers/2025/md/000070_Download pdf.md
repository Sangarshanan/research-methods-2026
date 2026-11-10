---
paper_id: "000070"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706531/files/000070.pdf"
---

# SHEET MUSIC BENCHMARK: STANDARDIZED OPTICAL MUSIC RECOGNITION EVALUATION 

|Juan C. Martin|ez-Sevilla<sup>1</sup><br>Joan Cerveto-Serrano<sup>1</sup><br>Noelia Luna<sup>1</sup>|
|---|---|
|Greg Chapman<sup>2</sup>|Craig Sapp<sup>3</sup><br>David Rizo<sup>1,4</sup><br>Jorge Calvo-Zaragoza<sup>1</sup>|
|1Pattern Recognit  i|ion and Artificial Intelligence Group, University of Alicante, Spain<br>2Self-employed|



- 3 Center for Computer Research in Music and Acoustics, Stanford University, USA 

- 4 Instituto Superior de Enseñanzas Artísticas de la Comunidad Valenciana, Spain 

```
{jcmartinez.sevilla,joan.cerveto,noelia.luna,drizo,jorge.calvo}@ua.es
```

- `gregc@mac.com, craig@ccrma.stanford.edu` 

## ABSTRACT 

In this work, we introduce the Sheet Music Benchmark (SMB), a dataset of six hundred and eighty-five pages specifically designed to benchmark Optical Music Recognition (OMR) research. SMB encompasses a diverse array of musical textures, including monophony, pianoform, quartet, and others, all encoded in Common Western Modern Notation using the Humdrum `**kern` format. Alongside SMB, we introduce the OMR Normalized Edit Distance (OMR-NED), a new metric tailored explicitly for evaluating OMR performance. OMR-NED builds upon the widely-used Symbol Error Rate (SER), offering a finegrained and detailed error analysis that covers individual musical elements such as note heads, beams, pitches, accidentals, and other critical notation features. The resulting numeric score provided by OMR-NED facilitates clear comparisons, enabling researchers and end-users alike to identify optimal OMR approaches. Our work thus addresses a long-standing gap in OMR evaluation, and we support our contributions with baseline experiments using standardized SMB dataset splits for training and assessing state-of-the-art methods. 

## 1. INTRODUCTION 

Optical Music Recognition (OMR) is a long-standing challenge within the field of Music Information Retrieval (MIR). It focuses on automatically extracting musical information from scanned images, manuscripts, or printed documents, converting this information into structured digital representations [1], such as Humdrum `**kern` [2], MEI [3], or MusicXML [4]. These machine-readable formats facilitate large-scale musical information retrieval, 

© J. C. Martinez-Sevilla, J. Cerveto-Serrano, N. Luna, G. Chapman, C. Sapp, D. Rizo, and J. Calvo-Zaragoza. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: J. C. Martinez-Sevilla, J. Cerveto-Serrano, N. Luna, G. Chapman, C. Sapp, D. Rizo, and J. Calvo-Zaragoza, “Sheet Music Benchmark: Standardized Optical Music Recognition Evaluation”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

enable advanced computational music analysis, and grant broader accessibility to extensive musical archives [5]. Traditionally, OMR methods were predominantly rulebased, involving steps such as staff line removal and primitive detection algorithms, which posed significant practical difficulties [6]. However, recent advancements in Deep Learning (DL) have successfully addressed many of these long-standing obstacles, leading to substantial improvements in OMR performance [7]. This is evidenced by the shift in the field towards end-to-end methods that attempt to solve the problem in a few steps, either by directly detecting musical objects in full images [8], or with singlestep transcription pipelines at both the region [9, 10] and page levels [11]. 

Given these advances and extensive ongoing research, one might consider OMR a mature and well-developed subfield of MIR. Nevertheless, unlike other MIR tasks, OMR still lacks a comprehensive, high-quality benchmark corpus, complicating rigorous performance assessment and qualitative comparison between systems. Such benchmarks have significantly benefited other MIR areas; notable examples include MAPS [12], ASAP [13], and MAESTRO [14] in automatic music transcription; Ballroom [15] and GTZAN [16] in beat tracking; or NSynth [17] for instrument classification, to name a few. These established benchmarks have greatly facilitated standardized comparisons and the systematic evaluation of novel approaches. 

To date, several attempts have been made to establish an OMR benchmark capable of addressing this gap. In their seminal work, Byrd and Simonsen proposed the OMRTestCorpus [18]; however, this corpus consists of only thirty-four pages with substantial graphical variability, rendering it insufficient and unsuitable for contemporary DLbased OMR approaches. Similarly, CVC-MUSCIMA [19] is only devised for the staff-line removal step, while its extension MUSCIMA++ [20] is object detection-oriented, with annotations not representing full musical scores. The PrIMuS dataset, although introduced as the first end-to-end OMR dataset, includes only monophonic samples at the staff-region level [21]. For pianoform end-to-end recog- 

604 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

nition, the GrandStaff dataset [11] was presented, but it is synthetically generated and lacks sufficient diversity, as the musical excerpts primarily originate from a limited set of composers. Recently, the OLiMPiC dataset [9] has been proposed for pianoform recognition tasks. Nevertheless, it also exhibits limited variety regarding repertoire and musical purposes, a restricted size, and is not truly end-to-end, since it relies on Linearized XML, a compact representation of MusicXML which requires additional processing to obtain a fully renderable music score. 

Considering the previously identified limitations and the existing gap in the field, in this work we introduce the Sheet Music Benchmark (SMB), a novel, full-page end-to-end dataset specifically designed for benchmarking modern DL-based OMR systems. SMB supports comprehensive evaluation, including layout analysis, region-level recognition, and full-page transcription. In addition to the dataset, we design a new evaluation metric: the OMR Normalized Edit Distance (OMR-NED). This metric pursues two main objectives: (i) summarizing the overall performance of an OMR system in a single numerical value, and (ii) enabling detailed profiling of OMR system errors by categorizing them into specific notation elements such as notes, rests, and measures, among others. To the best of our knowledge, the combination of SMB dataset and OMR-NED metric will significantly advance OMR research, similar to how established benchmarks have driven progress in other MIR areas, providing researchers and practitioners with a standardized and effective framework to rigorously evaluate OMR systems. 

## 2. BUILDING THE BENCHMARK 

SMB corpora is built upon KernScores [22], an online library of musical data encoded in `**kern` . This encoding format allows further processing with the Humdrum Toolkit for Music Research.<sup>1</sup> KernScores provides multiple representations for each piece, including a publicdomain scan of the sheet music (when available), the `**`<sup>`kern`encoding,andaMIDIfile.TobuildSMB,all</sup> the steps were performed by musically trained experts to ensure the quality of the annotations, such as the selection of the pieces, which included the linking process between the sheet music scan and its corresponding raw `**kern` encoding.<sup>2</sup> 

## 2.1 Annotation process 

The scanned scores were uploaded to HumanSignal,<sup>3</sup> a web platform specifically designed for data annotation. Each musical piece was manually labeled, starting with the assignment of a texture tag—Monophonic<sup>4</sup> , Pianoform, PianoAndVoice, Quartet, or Other.<sup>5</sup> Then, for each page, 

> 1 https://www.humdrum.org 

> 2 Here linking means that when the scan was not available, annotators looked for it in different sources. 

> 3 https://humansignal.com/ 

> 4 Most of the samples are single-staff and single-voice however homophony and polyphony can appear. 

> 5 Given the number of samples in the PianoAndVoice and Other texture tag, they will be referred to as Other for the rest of the paper. 



<!-- Start of picture text -->
Name: beethoven/sonata02_1 | Page: 0 History<br>SONATE<br>à dugt Beps 1) Vun0b1z8xG<br>N: 2<br>PAT<br>184<br> +2 <3 +3 4F8r<br>83.2422085881670<br><!-- End of picture text -->

Figure 1. Labeled piece example. In blue the bounding boxes that locate the regions of interest. In the top-right corner the raw `**kern` encoding of the first region of the page. 

the regions corresponding to individual staves or musical systems were delimited by bounding boxes and labeled with their content in raw `**kern` format (see Fig. 1). 

These annotations were performed at the staff level (sometimes referred to as line-level annotations). While full-page end-to-end digitization is the ultimate goal of any OMR system, it remains a highly complex challenge for most architectures. Nonetheless, SMB also provides “diplomatic”<sup>6</sup> full-page annotations, suitable for stafflevel and page-level transcription. These detailed annotations also allow Layout Analysis (LA) processes, making SMB appropriate for any modern OMR pipeline. 

## 2.2 The use of Humdrum **`**kern`** 

Music can be digitally represented in various formats, including Humdrum `**kern,` MEI, or MusicXML. However, `**kern` remains the most efficient and least verbose option, making it particularly suitable for OMR DL-based systems. This efficiency, combined with the extensive Humdrum ecosystem—–which includes rendering tools like Verovio Humdrum Viewer [23] and symbolic analysis frameworks such as humdrum-tools [24]— as well as partitura [25] and music21 [26], ensures `**kern` is both accessible and highly advantageous for OMR applications.<sup>7</sup> 

## 2.3 Postprocessing 

Once the annotation process was completed, compiling a robust, functional dataset for modern end-to-end OMR methods posed significant challenges. An important component in the extracted raw `**kern` fragments from KernScores is their fidelity to the original score, providing metadata such as the source, authorship, publication year, work titles, and more. However, for some DL experiments, the availability of this information together with the inherent ambiguity of the raw `**kern` encoding itself—which 

> 6 Annotations indicate where the staff breaks are in the source score. 

> 7 The use of `**kern` for OMR does not constrain the later usage of another encoding format. 

605 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
#a8 8a# 8#a #8a a8# a#8<br><!-- End of picture text -->

Figure 2. Possible `**kern` inconsistent representations for an A#4 eighth note. 

can represent the same symbol in multiple ways (see Fig. 2)—supposes a major drawback, and thus it needed to be addressed. 

For that reason, the construction of standardized, highquality `**kern` files, e.g., by constraining the representations of notes to reduce vocabulary size, is a key point of the SMB. The kernpy [27] package was a major pillar during the postprocessing process providing features that converted non-standardized fragmented `**kern` data—as it comes from the labeling process—into complete standardized encoding ready to use by the Humdrum ecosystem tools: including the proper `**kern` headers, spine paths<sup>8</sup> and changes in clefs, key signatures, and time signatures. 

In addition, this package was also used to enforce structural consistency and perform semantic tokenization across different music categories. This approach even allows for the possibility of performing custom selections for specific research tasks, such as enabling the use of a tailored set of categories or avoiding the inclusion of articulations, accidentals, dynamics, or pitches. Consequently, three formats emerged from this step: 

raw. Represents the original fragmented raw `**kern` KernScores encoding used for in the labeling steps without any change. 

kern. Standardized `**kern` file retrieved from the tokenized version obtained from kernpy package. Compatible with the Humdrum ecosystem toolkit. 

ekern. The "Extended `**kern` " is a standardized tokenized version of `**kern` where each musical symbol is spaced by “@” and “·” dividing semantic token categories of each symbol, i.e., duration, pitch or accidental. This approach reduces significantly the vocabulary size of the dataset, although increasing sequence lengths. 

Following automated data processing, the SMB underwent manual inspection at page and region levels to ensure error-free `**kern` and `**ekern` annotations. Encoding irregularities in problematic annotations were systematically solved. 

## 2.4 Data analysis 

In this subsection, we present a comprehensive analysis of SMB samples to provide insights into its features, distribu- 

8 https://www.humdrum.org/Humdrum/representations/kern.html 



<!-- Start of picture text -->
A0 C1 C2 C3 C4 C5 C6 C7<br>Pitch token<br>Count<br><!-- End of picture text -->

Figure 3. Pitch token frequency distribution in SMB. 

tion, and content. We depict key statistical properties, explore patterns within the data, and identify notable details given the standardized `**kern` encoding. This analysis serves to both validate the quality of the benchmark and illustrate in a clearer way the content of it. 

SMB spans 4039 regions which correspond to 685 pages. Table 1 provides a detailed description of the main features of this assortment in `**kern` format. As shown, the most representative texture is Pianoform. On one hand, it is one of the instruments with the broadest repertoire; on the other, it remains one of the most complicated textures to transcribe. Another point to highlight is that when increasing the number of instruments, i.e., Quartet texture, musicians do not usually play with the full score as they prefer to use parts. As a result, the number of annotated pages is lower than others. 

An interesting outcome is that the graphical features of higher-voice-count pages such as Quartet compared to Monophony, cause a drop in the number of regions by page, but the number of tokens by page remains similar. A key difference we find is the number of tokens per region as when the number of voices increases, the count rises drastically. 

In Figure 3 we show the Pitch token frequency distribution of SMB, where the most common pitches are the ones present between A3 and G5. 

Different composers, styles, and periods were considered to increase the variability in the data. The heterogeneity of the collection spans from the Baroque period to the Ragtime eras. In between, there is a set of various musical periods such as the Classical, the Romantic, or the Impressionist, which provide a wide range of musical pieces. Some of the available composers are: Carl Maria von Weber, Domenico Scarlatti, Frédéric Chopin, Joseph Haydn, W. A. Mozart, L. van Beethoven, and Scott Joplin, among others. 

The diversity present in SMB makes it to our best knowledge the first and most complete dataset in Common Western Modern Notation (CWMN) for OMR DL-based methodologies benchmarking, providing a set of diverse and complex scores. 

606 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

|Texture|Pages|Regions|Regions by page(µ±σ)|Tokens by page(µ±σ)|Tokens by region(µ±σ)|
|---|---|---|---|---|---|
|Monophony|115|972|8.4±3.5|1308.5±719.7|165.2±51.1|
|Pianoform|469|2686|5.7±1.1|1371.3±679.4|263.5±105.0|
|Quartet|79|304|3.8±0.5|1338.4±413.2|373.1±92.9|
|Other|22|77|3.5±1.5|1203.0±671.8|349.8±136.4|
|All|685|4039|5.8±2.2|1351.6±660.9|249.7±110.2|



Table 1. Results of SMB page, region and token count analysis in `**kern` encoding. 

## 2.5 Publication 

Ensuring accessibility and ease of use for the research community, SMB is available at Hugging Face Datasets platform.<sup>9</sup> 

## 3. EVALUATION METRIC 

One key aspect of building a successful OMR system is the way of measuring the quality of it. Measuring OMR performance remains an open problem due to a set of unanswered questions: What is considered a music symbol? How do we measure the correction effort? The answer to these questions remains an open topic that is being addressed in conjunction with musicologists. 

Until today, the most popular metric used when evaluating OMR has been the Symbol Error Rate (i.e. in some works referred to as Edit Distance, Character Error Rate, or Music Error Rate), that is computed as the average number of elementary operations (insertions, deletions, or substitutions) required to convert prediction ˆzi into reference zi, normalized by the length of the latter. 

Indeed, it still stands as the best metric to correlate the human correction effort that is necessary to obtain the desired score. However such correction effort does not indicate in which aspect of the transcription process the OMR is struggling, e.g., clefs, note heads, beams, accidentals, key signatures, or anything else. 

In this work, we leverage Music-Score-Diff [28] currently maintained by Greg Chapman and better known as MusicDiff 10 . MusicDiff computes the visual notation differences between two music scores; however, this tool has been known for having trouble processing the scores from OMR pipelines because it requires a parseable score (which is certainly not always the case with OMR systems). Due to this, and other shortcomings, we have improved MusicDiff significantly so it can now do the following: (i) it can compare non-parseable predicted `**kern` scores, (ii) it can compare all musical objects, not just notes/rests, (iii) it can compare all the notes in a measure without regard to voicing and/or membership in chords, and (iv) it can be told at what fine-grained level of detail it should compare the scores. We have also significantly changed how MusicDiff computes edit distance, and we have carefully audited and changed how music symbols are defined/counted. 

Hence we present the resultant metric score, referred to as the OMR Normalized Edit Distance (OMR-NED), designed specifically to allow visual score comparison and measuring in a fine-grained manner, therefore standing as the first alternative to the traditionally used SER. OMRNED defines a set of categories, and a detailed list of visual music symbols for each category, which can then be compared. Note that these music symbols are not defined in terms of `**kern` (or `**ekern` ). Instead, they are defined in terms of visual music notation, in a file format agnostic way. The OMR-NED metric for the score comparison can be computed as the average number of music symbol insertions and deletions required to convert the predicted score into the reference score, normalized by the sum of the number of music symbols in both: 



<!-- Start of picture text -->
I + D<br>OMR-NED = (1)<br>N1 + N2<br><!-- End of picture text -->

I and D are the total number of insertions and deletions of individual music symbols for all categories, and N1 + N2 is the total number of music symbols in the predicted and ground truth scores. We normalize using both scores’ music symbol counts, because when a symbol is changed (say there is a predicted 2/4 time signature, but the ground truth is a 3/4 time signature), instead of computing a substitution of one symbol, we compute a deletion of the “2” and an insertion of the “3”, for an edit distance of two symbols. 

MusicDiff can be pointed at a folder full of ground truth (reference) score files, and a folder full of same-named predicted score files. When running in this mode, MusicDiff will produce a CSV file containing a spreadsheet with a row for each score file comparison and a column for each category. Each column contains the edit distances for that category, with the total edit distance and OMR-NED metrics for all the score comparisons in the final columns. There is a summary row for the entire run of score comparisons at the bottom, with a total edit distance for each category across all the scores, and an overall OMR-NED metric for the entire run. 

## 3.1 OMR-NED categories 

In this subsection we present the categories related to music notes and rests and the non-notes ones. This will be further emphasized in the fine-grained analysis that OMRNED depicts. 

Notes/Rests: Notes and rests contain multiple categories, each with its own symbol count. MusicDiff only directly compares notes/rests that have the same pitch and 

9 huggingface.co/datasets/PRAIG/SMB 10 github.com/gregchapman-dev/musicdiff 

607 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

are on the same exact offset within the measure. This means that notes that are mismatched by pitch (or by offset within the measure) will have a larger edit distance because the entire note (and all its symbols) is deleted, and then the new note is inserted.<sup>11</sup> 

Available categories: Pitch — One symbol for the pitch. Accidental — One symbol for the accidental. Tie — One symbol if the note is tied to a subsequent note. Note head — One symbol for the note head type (quarter note, half note, whole note, etc). The note head type for eighth notes and smaller is still a quarter note head. The flags/beams category differentiates further between shorter notes. Note flags/beams — One symbol per flag or beam. Dots — One symbol per dot. Articulations — One symbol per articulation (staccato, tenuto, etc). Ornaments — One symbol per ornament (trill, mordent, etc). Grace — One symbol if a grace note; one more symbol if slashed. Non-Notes: Non-note objects are a single category each. MusicDiff only directly compares non-note objects that are at the same exact offset within the measure. So, for example, text directions that are shifted horizontally from each other are deleted/inserted, instead of returning the edit distance between the strings. 

Available categories: Dynamic — Dynamics such as p, fff , etc are one symbol only (not one symbol per character). Hairpin dynamic markings are one symbol for the hairpin direction plus an extra symbol for the hairpin duration. Clef — Clefs are one symbol. Key signature — Key signatures are one symbol per accidental. Time signature — Time signatures are one symbol for the top, one for the bottom (e.g. 12/8 is two symbols, C is one symbol). Slur — One symbol for duration. Ottava — Two symbols: one for ottava type (e.g. 8va, 8ba, etc), and one for duration. Direction — One symbol for each character in the string. Arpeggio — One symbol for arpeggio type (up, down, undirected, non-arpeggiated). One more symbol if arpeggio spans multiple staves. Chord symbol — One symbol. Lyric — One symbol for each character in the lyric syllable. One symbol for verse number/identifier. Ending — One symbol for each character in the ending name. One symbol for measure count. 

## 3.2 Edit distances 

Edit lists are calculated as a series of inserts/deletes of musical objects, with the edit distance being the total number of symbols inserted/deleted. For example, if a predicted note has a flag, but the matching ground truth note has a beam instead, the edit distance will be 2: delete the flag (one symbol) and insert the beam (one symbol). 

At a slightly higher level, if the predicted score has a note where the ground truth score has a rest, the edit will delete the note, and insert the rest. The edit distance in that case will be the number of symbols in the deleted note plus the number of symbols in the inserted rest. 

> 11 The description here is of the default categories. There can be more symbols per category (and more categories) if Style and/or Metadata is requested in addition to the default detail level. See gregchapmandev.github.io/musicdiff/musicdiff/detaillevel.html for more information about specifying detail levels to MusicDiff. 

At an even higher level, if the predicted score has an extra measure that does not exist in the ground truth score, that measure will be deleted, with an edit distance equal to the total number of symbols in that predicted measure. 

## 4. BASELINE RESULTS 

This work constitutes the first to introduce both the SMB benchmark dataset and the fine-grained metric evaluation OMR-NED. Therefore, in this section, we report a performance baseline using a state-of-the-art model, which serves as a reference for future work. 

While the recommended use of SMB is as test set, for the baseline we consider each texture type a subset of samples, namely Monophony, Pianoform, Quartet, and Other. These scores are used at the region level (assuming a previous LA step) and following a 5-fold cross validation framework, ensuring that every region takes part in the test split once. We train the framework both with `**kern` and `**`<sup>`ekern`encoding.</sup> 

For the learning framework, we resort to the state-ofthe-art Sheet Music Transformer [10]. This architecture consists of a encoder-decoder network. The encoder is in charge of retrieving the image features and the decoder is a conditioned language model that predicts the most probable music symbol in an auto-regressive fashion. 

The model was trained without the use of any pretrained weights. We iterate for 400 epochs, considering the ADAM optimizer with a fixed learning rate of 10<sup>−4</sup> . We keep the weights that minimize the SER metric in the validation partition, validating every 5 epochs. Finally, all experiments were run using the Python language (v. 3.12.3) with the PyTorch framework (v. 2.0.0) on a single NVIDIA RTX 4080 card with 20GB of video memory. 

Table 2 presents the average results obtained using the considered experimental baseline in terms of SER and the introduced OMR-NED. Regarding the (low) recognition rates, it is worth noting that Transformer architectures typically require large corpora to achieve convergence. Nevertheless, we report these values to facilitate future research using SMB. The results indicate ample room for improvement, highlighting the dataset as a challenging benchmark that should drive advancements in OMR. 

|Texture|Encoding|↓OMR-NED (%)|↓SER (%)|
|---|---|---|---|
|Monohon|`kern`|94.1±5.0|57.1±0.8|
|py|`ekern`|98.8±1.0|65.8±1.2|
|Pif|`kern`|57.4±6.0|31.4±1.5|
|anoorm|`ekern`|77.2±2.0|55.1±2.2|
|tt|`kern`|92.3±1.2|39.8±1.6|
|Quare|`ekern`|93.3±1.1|82.9±1.2|
|Oh|`kern`|89.6±2.4|60.2±6.2|
|ter|`ekern`|93.7±2.0|72.4±7.3|



Table 2. Results in terms of the SER (%) and OMR-NED (%) metrics when considering Monophony, Pianoform, Quartet and Other score textures. All cases are evaluated using 5-fold cross validation. 

608 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

|Groun|d truth|Scan|Render|Pred<br>||
|---|---|---|---|---|---|
|**kern|**text|||**kern|**text|
|*clefG2|*|||*clefG2|*|
|*k[b-e-a|-]<br>*|||*k[b-e-a|-]*|
|*M2/4|*|||*M2/4|*|
|=|=|||=|=|
|16B-'/LL|You||make|16B-'/LL <br>|.<br>■|
|16d'/|.||m|16d'/|.|
|16f'/<br>|.<br>||a<br>O|16f'/|.|
|16b-'/JJ <br>|make||h|16b-'/JJ|make|
|8an/|me||apy,|8bn/|ma|
|8r|.|||8r|.|
|=|=|||=|=|
|(16F/LL <br>|happy,||whe|(16F/LL <br>|hapy,<br>■|
|16An/|.||loo|16bn/|.|
|16c/|.||k<br>|16c/|.|
|16A/JJ|.||t|16b/JJ|.|
|16F/LL|.||my|16F/LL|.|
|16c/|when||ey|16c/|whe|
|16e-/|you||es|16e-/|.|
|16c/JJ)|look|||16c/JJ)|look|



Figure 4. Monophonic (with lyrics) region-level transcription example. Red boxes and circles represent transcription errors. 

## 5. CASE STUDY: OMR-NED VS. SER 

To better exhibit the pros and cons of using OMR-NED (at the region level) compared to traditionally employed SER, we study two different transcription examples. The first one (see Fig. 4) highlights the wrongly transcribed notes and lyrics in a monophonic score. If we look at the results obtained in Table 3 the different OMR-NED Categories permit the fine-grained analysis of this behavior. With 65% of the errors related to notes and 35% to lyrics mistranscriptions. 

Figure 5 shows an example of a pianoform transcription. In this case, most of the errors (88.2%) correspond to the note category, however, OMR-NED outlines problems in the extra category, indicating that there are also mistaken music symbols that comprehend dynamics or left-hand clef and key. It is worth mentioning that given the level of detail OMR-NED depicts and the procedure to calculate the different edit distances between hypothesis and ground truth (see Section 3), the overall score penalizes the transcription errors more than traditionally used SER. 

The comparative analysis of OMR-NED and SER through these case studies demonstrates the advantages of adopting a more refined and structured evaluation metric. While SER provides an acceptable measurement of transcription accuracy, OMR-NED enables a more granular understanding of the specific transcription error types. This is particularly evident in the first example, where OMR-NED differentiates between note and lyric errors. Similarly, the second example highlights OMR-NED’s ability to capture complex transcription issues in polyphonic pianoform music, particularly by exposing errors in musical symbols beyond pitch content—such as dynamics and clef misclassifications. OMR-NED as a more informative metric, encompasses the development of more robust OMR systems. 



<!-- Start of picture text -->
Ground truth Scan Render Pred<br>**kern **kern **dynam **kern **kern **dynam<br>*staff2 *staff1 *staff1 *staff2 *staff1 *staff1<br>*Ipiano *Ipiano *Ipiano *Ipiano *Ipiano *Ipiano<br>*clefF4 *clefG2 *clefG2 *clefF3 *clefG2 *clefG2<br>*k[f#c#] *k[f#c#] *k[f#c#] *k[] *k[f#c#] *k[f#c#]<br>*b: *b: *b: *b: *b: *b:<br>*M3/4 *M3/4 *M3/4 *M4/8 *M3/4 *M3/4<br>*MM208*MM208*MM208 *MM208*MM208*MM208<br>4=*p1red (=*41dd *.=1 A l egre t o. 4=*p1red (=*41dd *.=1<br>4BB 12ddL p 4BB 12ddL p<br>. 12ee . . 12aa .<br>. 12ddJ . . 12ddJ .<br>4F# 4d 4cc# . 4F# 4A 4cc# .<br>4*XFp# ed4d 4* b *. 1 4 *X G p # ed4d 4 * g *.<br>=*p2ed =* 2 *=2 =*p2ed =* 2 *=2<br>4FF# 8a#L . _4.FF# _4a# .<br>. 8g 8ggJ. . 8g 8gg .<br>4F# 4A# 4e 2f# 2ff#) . 4F# 4A# 4e 2f# 2ff#)  .<br>*4XFp# ed4A# *4e . *. *4XFp# ed4A# *4e . *.<br>=*p3ed =* 3 *=3 #2d. =*p3ed =* 3 *=3<br>. 8ddq/ . . 8ddq/ .<br>4BB (12ddL f 4BB (12ddL ff<br>. 12ee . . 12ee .<br>. 12ddJ . . 12aJ .<br>44*XFFp# # ed44dd 44* bcc# *.. 4 4*XF G p#  #  ed44dd 44* bcc# *..<br><!-- End of picture text -->

Figure 5. Pianoform region-level transcription example. Red boxes and circles represent transcription errors. 

|Examle||||OMR-NED|Catego|ries||Symbol|
|---|---|---|---|---|---|---|---|---|
|p|Note|Extra|Lyrics|Measure|Part|StaffGroup|OMR-NED|Error Rate|
|Fig. 4|65.0|0|35.0|0|0|0|13.6|9.0|
|Fig. 5|88.2|11.8|0|0|0|0|40.9|13.0|



Table 3. Results in terms of the SER (%) and OMR-NED Categories (%) metrics. Note that OMR-NED is prepared for full-page recognition thus some categories do not affect the OMR-NED score in the region-level scenario. 

## 6. CONCLUSION 

In this work, we addressed a long-standing gap in the Optical Music Recognition (OMR) literature by introducing the Sheet Music Benchmark (SMB), a collection of scores specifically designed for evaluating modern end-to-end OMR pipelines. SMB constitutes the first publicly available corpus that allows comprehensive end-to-end evaluation at multiple levels, including layout analysis as well as region-level and full-page transcription tasks. We also provided baseline results to guide future research efforts in this area. The reported performance with a state-of-theart methodology demonstrate the benchmark’s complexity and its effectiveness in assessing OMR systems targeting Common Western Modern Notation. 

Furthermore, we introduced a novel evaluation metric, the OMR Normalized Edit Distance (OMR-NED), which enables a fine-grained analysis of OMR system performance. OMR-NED decomposes the traditional edit distance calculation into distinct error categories, facilitating precise profiling of potential system deficiencies. As demonstrated in Sec. 5, the use of OMR-NED provides valuable insights into transcription errors, thereby enabling targeted improvements in OMR frameworks. 

The combined contributions of SMB and OMR-NED establish a standardized evaluation pipeline, facilitating clear performance comparisons among OMR systems. Thus, this work significantly advances the field by addressing a critical need within the OMR research community. 

609 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 7. ACKNOWLEDGMENTS 

This paper is supported by grant CISEJI/2023/9 from “Programa para el apoyo a personas investigadoras con talento (Plan GenT) de la Generalitat Valenciana”. 

## 8. REFERENCES 

- [1] J. Calvo-Zaragoza, J. H. Jr., and A. Pacha, “Understanding Optical Music Recognition,” ACM Comput. Surv., vol. 53, no. 4, pp. 77:1–77:35, 2021. 

- [2] D. Huron, “Humdrum and Kern: Selective Feature Encoding BT - Beyond MIDI: The handbook of musical codes,” in Beyond MIDI: The handbook of musical codes. Cambridge, MA, USA: MIT Press, jan 1997, pp. 375–401. 

- [3] A. Hankinson, P. Roland, and I. Fujinaga, “The Music Encoding Initiative as a Document-Encoding Framework,” in Proceedings of the 12th International Society for Music Information Retrieval Conference, ISMIR 2011, Miami, Florida, USA, October 24-28, 2011. University of Miami, 2011, pp. 293–298. 

- [4] M. Good et al., “MusicXML: An internet-friendly format for sheet music,” in Xml conference and expo. Citeseer, 2001, pp. 03–04. 

- [5] M. Alfaro-Contreras, D. Rizo, J. M. Iñesta, and J. Calvo-Zaragoza, “OMR-assisted transcription: a case study with early prints,” in Proceedings of the 22nd International Society for Music Information Retrieval Conference. Online: ISMIR, Nov. 2021, pp. 35–41. 

- [6] A. Rebelo, I. Fujinaga, F. Paszkiewicz, A. R. Marcal, C. Guedes, and J. S. Cardoso, “Optical music recognition: state-of-the-art and open issues,” International Journal of Multimedia Information Retrieval, vol. 1, pp. 173–190, 2012. 

- [7] E. Shatri and G. Fazekas, “Optical music recognition: State of the art and major challenges,” arXiv preprint arXiv:2006.07885, 2020. 

- [8] L. Tuggener, R. Emberger, A. Ghosh, P. Sager, Y. P. Satyawan, J. Montoya, S. Goldschagg, F. Seibold, U. Gut, P. Ackermann et al., “Real world music object recognition,” Transactions of the International Society for Music Information Retrieval, vol. 7, no. 1, pp. 1–14, 2024. 

- [9] J. Mayer, M. Straka, J. Hajic, and P. Pecina, “Practical End-to-End Optical Music Recognition for Pianoform Music,” in Document Analysis and Recognition - ICDAR 2024 - 18th International Conference, Athens, Greece, August 30 - September 4, 2024, Proceedings, Part VI, ser. Lecture Notes in Computer Science, E. H. B. Smith, M. Liwicki, and L. Peng, Eds., vol. 14809. Springer, 2024, pp. 55–73. 

- [10] A. Ríos-Vila, J. Calvo-Zaragoza, and T. Paquet, “Sheet music transformer: End-to-end optical music recognition beyond monophonic transcription,” in International Conference on Document Analysis and Recognition. Springer, 2024, pp. 20–37. 

- [11] A. Ríos-Vila, J. Calvo-Zaragoza, D. Rizo, and T. Paquet, “Sheet Music Transformer ++: End-to-End FullPage Optical Music Recognition for Pianoform Sheet Music,” CoRR, vol. abs/2405.12105, 2024. 

- [12] V. Emiya, N. Bertin, B. David, and R. Badeau, “MAPS - A piano database for multipitch estimation and automatic transcription of music,” -, Research Report, Jul. 2010. 

- [13] F. Foscarin, A. McLeod, P. Rigaux, F. Jacquemard, and M. Sakai, “ASAP: a dataset of aligned scores and performances for piano transcription,” in Proceedings of the 21th International Society for Music Information Retrieval Conference, ISMIR 2020, Montreal, Canada, October 11-16, 2020, J. Cumming, J. H. Lee, B. McFee, M. Schedl, J. Devaney, C. McKay, E. Zangerle, and T. de Reuse, Eds., 2020, pp. 534–541. 

- [14] C. Hawthorne, A. Stasyuk, A. Roberts, I. Simon, C. A. Huang, S. Dieleman, E. Elsen, J. H. Engel, and D. Eck, “Enabling factorized piano music modeling and generation with the MAESTRO dataset,” in 7th International Conference on Learning Representations, ICLR 2019, New Orleans, LA, USA, May 6-9, 2019. OpenReview.net, 2019. 

- [15] F. Gouyon, A. Klapuri, S. Dixon, M. Alonso, G. Tzanetakis, C. Uhle, and P. Cano, “An experimental comparison of audio tempo induction algorithms,” IEEE Trans. Speech Audio Process., vol. 14, no. 5, pp. 1832–1844, 2006. 

- [16] G. Tzanetakis and P. R. Cook, “Musical genre classification of audio signals,” IEEE Trans. Speech Audio Process., vol. 10, no. 5, pp. 293–302, 2002. 

- [17] J. H. Engel, C. Resnick, A. Roberts, S. Dieleman, M. Norouzi, D. Eck, and K. Simonyan, “Neural audio synthesis of musical notes with wavenet autoencoders,” in Proceedings of the 34th International Conference on Machine Learning, ICML 2017, Sydney, NSW, Australia, 6-11 August 2017, ser. Proceedings of Machine Learning Research, D. Precup and Y. W. Teh, Eds., vol. 70. PMLR, 2017, pp. 1068–1077. 

- [18] D. Byrd and J. Simonsen, “Towards a Standard Testbed for Optical Music Recognition: Definitions, Metrics, and Page Images,” Journal of New Music Research, vol. 44, 07 2015. 

- [19] A. Fornés, A. Dutta, A. Gordo, and J. Lladós, “CVCMUSCIMA: a ground truth of handwritten music score images for writer identification and staff removal,” Int. J. Document Anal. Recognit., vol. 15, no. 3, pp. 243– 251, 2012. 

610 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [20] J. Hajic and P. Pecina, “The MUSCIMA++ Dataset for Handwritten Optical Music Recognition,” in 14th IAPR International Conference on Document Analysis and Recognition, ICDAR 2017, Kyoto, Japan, November 9- 15, 2017. IEEE, 2017, pp. 39–46. 

- [21] J. Calvo-Zaragoza and D. Rizo, “Camera-PrIMuS: Neural End-to-End Optical Music Recognition on Realistic Monophonic Scores,” in Proceedings of the 19th International Society for Music Information Retrieval Conference, ISMIR 2018, Paris, France, September 23-27, 2018, E. Gómez, X. Hu, E. Humphrey, and E. Benetos, Eds., 2018, pp. 248–255. 

- [22] C. S. Sapp, “Online database of scores in the humdrum file format,” in ISMIR 2005, 6th International Conference on Music Information Retrieval, London, UK, 1115 September 2005, Proceedings, 2005, pp. 664–665. 

- [23] L. Pugin, R. Zitellini, and P. Roland, “Verovio: A library for engraving MEI music notation into SVG,” in Proceedings of the 15th International Society for Music Information Retrieval Conference, ISMIR 2014, Taipei, Taiwan, October 27-31, 2014, H. Wang, Y. Yang, and J. H. Lee, Eds., 2014, pp. 107–112. 

- [24] N. Condit-Schultz and C. Arthur, “humdrumr: a new take on an old approach to computational musicology,” in Proceedings of the International Society for Music Information Retrieval, 2019, pp. 715–722. 

- [25] C. E. Cancino-Chacón, S. D. Peter, E. Karystinaios, F. Foscarin, M. Grachten, and G. Widmer, “Partitura: A Python Package for Symbolic Music Processing,” in Proceedings of the Music Encoding Conference (MEC2022), Halifax, Canada, 2022. 

- [26] M. S. Cuthbert and C. Ariza, “Music21: A toolkit for computer-aided musicology and symbolic music data,” in Proceedings of the 11th International Society for Music Information Retrieval Conference, ISMIR 2010, Utrecht, Netherlands, August 9-13, 2010, J. S. Downie and R. C. Veltkamp, Eds. International Society for Music Information Retrieval, 2010, pp. 637–642. 

- [27] J. Cerveto-Serrano, D. Rizo, and J. Calvo-Zaragoza, “kernpy: a Humdrum **Kern Oriented Python Package for Optical Music Recognition Tasks,” in Proceedings of the Music Encoding Conference (MEC2025), London, United Kingdom, 2025. 

- [28] F. Foscarin, F. Jacquemard, and R. Fournier-S’niehotta, “A diff procedure for music score files,” in 6th International Conference on Digital Libraries for Musicology, 2019, pp. 58–64. 

611 

