---
paper_id: "000082"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706567/files/000082.pdf"
---

# HUMAN VS. MACHINE: COMPARING SELECTION STRATEGIES IN ACTIVE LEARNING FOR OPTICAL MUSIC RECOGNITION 

Juan P. Martinez-Esteso<sup>1</sup> Francisco J. Castellanos<sup>1</sup> 

Alejandro Galan-Cuenca<sup>1</sup> Carlos Pérez-Sancho<sup>11</sup> Antonio Javier Gallego<sup>1</sup> 

1 University Institute for Computing Research, University of Alicante, Spain 

```
{juan.martinez11,a.galan}@ua.es,{cperez,fcastellanos,jgallego}@dlsi.ua.es
```

## ABSTRACT 

Optical Music Recognition (OMR) systems rely on accurate layout analysis (LA) to segment different information layers in music score images. While deep learning approaches have improved performance, they remain heavily dependent on large amounts of annotated data. In this work, we propose the integration of a Few-Shot Learning (FSL) architecture into an active learning framework for LA. This enables interactive and iterative training, allowing the model to progressively improve from minimal annotated data. We evaluate how this approach enhances recognition accuracy and reduces annotation effort, and we study the impact of different sample selection criteria within this framework, comparing data selected by five expert annotators against four automated strategies: random, sequential, ink density-based, and entropy-based. Experiments across three diverse music score datasets show that entropy-based selection consistently outperforms human choices, achieving an F1-score of 81.1% with only 8 labeled patches, while humans required at least 16 to reach similar performance. Our method improves over existing FSL approaches by up to 21.6% and substantially reduces annotation time. These results suggest that automated strategies can offer more efficient alternatives to human selection in OMR annotation workflows. 

## 1. INTRODUCTION 

Optical Music Recognition (OMR) aims to automatically transcribe music score images into digital formats, enabling access to vast collections of musical heritage for analysis, search, and retrieval [1]. A crucial step in this pipeline is Layout Analysis (LA), which segments score images into layers such as staff lines, symbols, lyrics, and background [2]. The diversity of historical and modern manuscripts, with their varying notational styles and print techniques, adds substantial complexity to this task. 

© J.P. Martinez-Esteso, A. Galan-Cuenca, C. PérezSancho, F.J. Castellanos, and A.J. Gallego. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: J.P. Martinez-Esteso, A. Galan-Cuenca, C. Pérez-Sancho, F.J. Castellanos, and A.J. Gallego, “Human vs. Machine: Comparing Selection Strategies in Active Learning for Optical Music Recognition”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

Modern approaches to LA rely heavily on deep learning [3], which requires large annotated datasets for training. However, manually labeling music score images is time-consuming, labor-intensive, and demands domain expertise to ensure accuracy [4]. To alleviate this burden, several strategies have been explored. Domain adaptation techniques [5] have shown promising results in specific scenarios but often suffer from unstable training and performance. Synthetic data generation and data augmentation [6, 7] can increase training data variability but struggle when labeled data is scarce or when the target domain significantly differs in appearance. Few-Shot Learning (FSL) approaches [8, 9] have also been proposed, achieving promising results by maximizing model performance from minimal labeled data. 

Recent works have adapted FSL to LA for text documents [10,11] and music [12], with the latter reducing annotation to small image patches rather than full pages. By combining masking and oversampling, this proposal enables models to generalize from minimal annotated data. However, it relies on a fixed, sequentially selected training set, leaving open whether performance could be further improved through more informed sample selection and interactive training. 

Active learning [13, 14] addresses this by iteratively choosing the most informative samples. Instead of relying on predefined or random choices, sample selection is guided by a human expert or an automated strategy, aiming to maximize model improvement. The process typically begins with a single labeled sample and proceeds through cycles of training, evaluation, and selection. In the context of OMR, however, the comparative effectiveness of human versus automated selection remains unexplored [15,16]. 

In this work, we propose the integration of an FSL architecture into an active learning framework for LA in OMR, enabling interactive, iterative training. We assess its impact on accuracy and annotation effort compared to the baseline FSL approach, focusing on the comparison of human decision-making against automated selection strategies. We specifically assess whether human annotators— five domain experts in our case—are capable of selecting the most informative image patches for training in comparison with four automated strategies. 

Experiments were conducted on three music score datasets with distinct characteristics, including mensural and neumatic notations. Performance was evaluated across 

703 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

four key layers: musical symbols, lyrics, staff lines, and background. In addition to accuracy, annotation time was measured using a custom-developed pixel-level labeling interface to assess the practical efficiency of each strategy. 

In summary, this work makes four main contributions: (i) the adaptation of an FSL architecture to an active learning setting; (ii) a detailed analysis of human versus automated selection strategies; (iii) a study on annotation efficiency using a purpose-built labeling tool; and (iv) a new state-of-the-art result in FSL for LA. 

## 2. METHODOLOGY 



<!-- Start of picture text -->
Unlabeled Dataset U Patch selection Manual annotation<br>I i P x P y<br>Oracle<br>add<br>No (P x , P y )<br>Training process<br>Finish Yes m ≥ σetric L A mode FSAE l dataset trainingD<br><!-- End of picture text -->

Figure 1: General scheme of the active learning process. 

Figure 1 provides a general overview of the active learning workflow. The process begins with a pool of unlabeled images, denoted as U . In each iteration, a patch is selected, annotated, and used to retrain the model, progressively improving its performance. This cycle is repeated until a predefined stop criterion is met. Specifically, the following steps are performed: 

1. Patch selection: A strategy determines which image Ii from the set U and which patch Px within the image should be annotated. The effectiveness of this selection is the focus of this study, where different criteria are compared, as detailed in later sections. 

2. Annotation: A human expert—often referred to as the oracle in related literature—performs pixel-wise annotations for each information layer of the selected patch, yielding the labeled pair (Px, Py). 

3. Model update: The new annotated patch is added to the training set D and used to retrain and update the weights of the LA model. 

4. Performance evaluation: The model’s accuracy is assessed against a predefined performance threshold σ. If it meets or exceeds σ, or a maximum number of iterations is reached, the process stops; otherwise, the selection-annotation-training cycle repeats. 

The following sections detail the different selection strategies analyzed in this study, the model architecture, and the training procedure. 

## 2.1 Selection Criteria 

Within this active learning framework, the objective of this study is to assess the impact of the patch selection strategy on model performance and to compare the decision- 

making ability of human annotators against automated selection methods. To this end, we evaluate a human-driven approach—in which annotator Hi, based on their expert intuition, manually selects the patch they believe will most increase the diversity of dataset D and yield the greatest improvement—alongside four automated selection strategies: 

- Random selection: Patches are randomly selected from the dataset, serving as a comparison baseline. 

- Sequential selection: Patches are selected in a fixed sequential order by traversing each image from left to right and top to bottom, ensuring an even distribution across the dataset. This criterion was originally proposed for FSL [12], and it is included as an additional baseline for comparison. 

- Ink density-based selection: Patches are chosen based on the amount of ink in the target layer, prioritizing those with higher quantity.<sup>1</sup> 

- Entropy-based selection: Patches are chosen based on their predicted uncertainty, using entropy as a measure of informativeness. This value is calculated using the method described in [17] for each candidate patch. 

Additionally, a threshold range [λ1, λ2] is defined for all the automated selection criteria, ensuring that selected patches contain a minimum ink density (λ1) for the target layer while avoiding patches that are fully saturated with ink (λ2), which might lack discernible structures. This check emulates the decision of a human annotator, who would reject system-proposed patches that either lack relevant information or are entirely filled with ink. 

It is important to note that while Figure 1 illustrates the selection of a single patch across all layers for simplicity, different patches may be chosen for each layer depending on the selection strategy. This applies to all selection criteria. For example, a human annotator may choose different patches for each layer based on which they consider most informative; in the ink density-based strategy, patches are ranked and selected according to the ink density of the target layer; and in the sequential and entropy-based strategies, although the patch order is predefined, only those within the threshold range [λ1, λ2] for the target layer are selected, which also results in different patches being chosen for each layer. 

## 2.2 LA model 

To maximize learning efficiency with minimal annotations, we adopt the Few-shot Selectional Auto-encoder (FSAE) approach proposed by [12]. This FSL architecture, specifically designed for LA, trains a specialized model for each information layer and then combines their predictions at the pixel level using a maximum a posteriori approach weighted by the confidence of each prediction. This makes FSAE particularly well-suited for the proposed active learning framework, as it allows selective annotation 

> 1 This strategy simulates human behavior, where annotators tend to focus on regions with more information (i.e., ink) in the layer. To mimic this behavior, ink density is calculated using the ground truth. 

704 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

for each layer, optimizing the labeling effort. 

To enhance learning and generalization with limited data, FSAE integrates two key techniques: a masking layer and an oversampling strategy. Each model is trained on the labeled patch set D<sup>l</sup> , where l refers to the annotated patches for a specific layer. The oversampling strategy extracts multiple random samples around each labeled patch to enrich the training data, while the masking layer prevents unannotated regions outside the labeled areas from influencing the learning process. 

Originally, this method was designed to learn from a fixed—and limited—dataset. We propose its integration into an active learning framework, enabling iterative training as described in Figure 1. Within this framework, two strategies are introduced to improve model training: 

- Validation set for overfitting prevention: To mitigate overfitting with few samples, a validation set is also selected with one labeled sample. For this, in the first iteration, the annotator selects two samples: one for training and one for validation. In later iterations, the validation sample is added to D, and the new selected sample becomes the validation set. Experimental results indicate that this strategy enhances training robustness by enabling early stopping based on validation performance. 

- Iterative model selection: From the second iteration onward, the performance of the current model is compared against the previous iteration. The bestperforming model is retained as the baseline for subsequent training cycles. Empirical evaluations demonstrate that this strategy improves training stability and final performance. 

originary from the Cathedral of Our Lady of the Pillar in Zaragoza, Spain, using mensural notation.<sup>4</sup> 

In all cases, we used 6 images for training and validation (from where the patches are selected), and the remaining for testing. Based on the original configuration of the LA model employed [12], we used a patch size of 256 × 256 pixels to extract samples from these images. 

|||||Layers|(%)||
|---|---|---|---|---|---|---|
|Corpus|# imgs|Resol.|Bg|St|No|Te|
|EINSIEDELN|9|6 496×4 872|87.9|3.5|2.7|5.9|
|SALZINNES|10|5 847×3 818|87.6|2.4|2.5|7.5|
|CAPITAN|10|2 126×3 065|85.7|6.6|5.1|2.6|



Table 1: Details of the corpora considered including the number of images (# imgs), the average resolution and the proportion of pixels for each layer of interest, with Bg for background, St for staff lines, No for notes, and Te for text. 







<!-- Start of picture text -->
(a) EINSIEDELN (b) SALZINNES<br>(c) CAPITAN<br><!-- End of picture text -->

## 3. EXPERIMENTAL SETUP 

This section presents the experimental setup used in this study, including the datasets used for evaluation, the metrics employed to assess performance, and the implementation details of the model. 

## 3.1 Corpora 

For the experiments, we considered the following 3 datasets with manual pixel-wise annotations of 4 layers of information ( `staff` , `notes` , `text` , and `background` ). Table 1 includes a summary of their details, while Figure 2 shows examples of regions from the original images to better visualize their particularities. 

- EINSIEDELN: 9 high-resolution scanned pages of neumatic notation belonging to the Einsiedeln, Stiftsbibliothek, Codex 611(89), from 1314.<sup>2</sup> 

- SALZINNES: 10 high-resolution images of pages from the Salzinnes Antiphonal manuscript (CDMHsmu M2149.14), in neumatic notation. It is available in the Cantus Ultimus platform.<sup>3</sup> 

- CAPITAN [18]: Set of 10 double-page images from music manuscripts of the 17th and 18th centuries, 

> 2 `http://www.e-codices.unifr.ch/en/sbe/0611/` 

> 3 `https://cantus.simssa.ca/manuscript/123723/` 

Figure 2: Examples of regions extracted from the original images in the corpora described in Table 1. 

## 3.2 Metrics 

To evaluate the performance, we resort to the F-score (F1) as the evaluation metric, ensuring a balanced assessment despite class imbalances in the datasets (see Table 1). In a binary classification setting, F1 is defined as: 



<!-- Start of picture text -->
2 · TP<br>F1 = (1)<br>2 · TP + FP + FN ,<br><!-- End of picture text -->

where TP, FP, and FN represent True Positives, False Positives, and False Negatives, respectively. 

Since our task involves multiple layers rather than a simple binary classification, we employed the macroaveraged F-score (F<sup>m</sup> 1<sup>).ThismetriccomputestheF1sep-</sup> arately for each layer and averages the results, ensuring equal weighting regardless of class distribution. 

## 3.3 Implementation details 

The LA model used follows the FSAE architecture proposed by [12], utilizing a separate Selectional Auto- 

> 4 RISM Code “E-Zac” is accesible at `https://rism.info` . 

705 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

Encoder (SAE) [19] for each of the four layers, with each model specialized in a specific layer. A masking layer is included at the input to ignore unannotated regions, and an oversampling process is applied during training to increase patch variability. After preliminary experiments, we determined to extract 1 024 random samples per epoch around the annotated areas for each iteration. Input images are normalized to [0, 1], with the masking layer allowing values in {−1} ∪ [0, 1], where −1 marks ignored pixels. 

Each network is trained using binary cross-entropy loss for up to 200 epochs, with early stopping after 20 epochs of no improvement on the validation set. The stochastic gradient descent optimizer [20] is used with a learning rate of 0.01 and a batch size of 32. Standard data augmentation techniques, including random rotations (±45<sup>◦</sup> ), zoom (0.8x–1.2x), and horizontal/vertical flips, are applied to increase data diversity. 

Patches of size 256 × 256 pixels are extracted using thresholds λ1 = 5% and λ2 = 95%. The stopping criterion σ is set to F<sup>m</sup> 1<sup>= 100%, so the training will only stop if</sup> perfect accuracy is achieved. However, a maximum of 32 iterations is imposed, as this is also the maximum considered in the original FSL approach [12]. 

## 4. RESULTS 

This section presents the results of this study, beginning with an analysis of the annotation time, followed by a comparison of selection strategies, and concluding with a qualitative examination of the selected patches. 



Figure 3: Developed tool for pixel-level annotation, showing a zoomed-in area of the image. 

average annotation time per layer and the total average annotation time per patch, along with the standard deviation, spent by each annotator. As shown, staff and notes take the longest to annotate due to overlapping regions requiring boundary marking. These are followed by the text layer, which does not usually overlap, and the background, which is easily auto-filled with minor edge adjustments. The average annotation time per patch is 8:18±2:06. 

|||Time p|er layer|||
|---|---|---|---|---|---|
|Ann.|`Staff`|`Notes`|`Text`|`Bg.`|Total|
|H1|2:33±1:02|2:18±1:42|1:34±1:03|1:10±1:05|7:36±3:14|
|H2|3:09±2:15|1:43±1:02|1:10±0:42|0:19±0:14|6:21±2:47|
|H3|2:28±2:22|2:26±0:45|1:26±1:02|1:05±0:43|7:26±3:43|
|H4|3:37±1:51|2:34±2:01|3:00±1:48|1:43±1:00|10:55±3:57|
|H5|2:49±2:06|3:21±0:53|1:57±0:58|1:06±1:24|9:13±3:58|
|Avg.|2:55±1:08|2:28±0:07|1:49±0:30|1:05±0:30|8:18±2:06|



## 4.1 Annotation Time 

To assess the time required for the annotation process, we conducted a study with 5 annotators with expertise in the task. Each annotator labeled 15 patches (5 per dataset) at the pixel level for the 4 layers considered, recording the time taken for each layer individually. For this purpose, we developed a specialized annotation tool, publicly available to the community ( `https://github. com/cperezs/pixel-level-annotator` ). While pixel-level annotation is often done using general-purpose graphic editors like GIMP, Photoshop, or Pixelmator, or proprietary tools developed by institutions [4], these are either too generic or not openly accessible. Some documentspecific tools, like PixLabeler [21], are available, but they are too simplistic, limited to direct pixel filling, and lack features that facilitate annotation based on color similarity or automatic region completion. 

Our tool is designed specifically for this task (see Figure 3) and includes a wide range of features to make annotation easier and faster. Users can define custom layers, use an adjustable brush tool, apply threshold selection, and auto-fill for completing layers. Additionally, it offers a quick-review mode to identify unannotated pixels, an option to prevent overwriting existing annotations, and intuitive keyboard shortcuts for switching between tools, layers, and settings such as brush size and threshold. 

Table 2 presents the results of this study, reporting the 

Table 2: Average annotation time (mm:ss) per patch for each annotator Hn. The table shows the mean time to manually annotate 15 patches for each individual layer, with the total average time per patch in the last column and the overall average across all annotators in the last row. 

Based on these times, annotating the maximum of 32 patches considered in this study would take about 4.5 hours. However, annotating entire pages from one of the datasets, given their high resolution (see Table 1), could take up to a month of work for the CAPITAN dataset, or two to three months for SALZINNES and EINSIEDELN. 

As a reference, we compared the agreement between the annotations performed by the five annotators, resulting in an average agreement of 95.7%±3.2% across all layers. This is quite high, and the differences observed are limited to slight discrepancies along the edges of each layer. 

## 4.2 Human vs. Automated Sample Selection 

This section presents the results of the study comparing the human selection criterion with the automatic methods, following the active learning framework and experimental setup described in Sections 2 and 3. 

Figure 4a shows the results obtained by human annotators, who sequentially selected patches from 1 to 32, retraining the LA model after each selection. Each curve rep- 

706 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

resents the average performance for one expert across the 4 layers and 3 datasets, along with the overall mean (dashed line). The results show notable variability: 2 annotators achieved the best results, 2 intermediate, and 1 performed worse. The gap between the best and worst performance reaches up to 17%, with an average difference of 13±2% across all iterations. These differences are especially relevant considering that, as discussed in the next section, the selected samples seem quite similar across annotators. 

Figure 4b compares the average results of human annotators (dashed line) with those from automatic selection methods, as well as the results from the original FSL approach (FSAE), which used sequential selection without incremental training. The automatic method based on entropy achieves the best results, followed by random selection, which even outperforms human experts. The inklevel-based method performs worse initially but improves after 15 labeled samples. The methods with the worst performance are those based on sequential selection, including the original FSL method. In contrast, a simple random selection criterion performs much better. Notably, the gap between the best (entropy) and worst (sequential) methods reaches up to 22%, with an average difference of 18±3% across all iterations. 

This reinforces the importance of the order in which samples are chosen. Methods as the sequential criterion fail to capture representative samples from the entire document. The original FSL method (based on this criterion) yields even worse results, likely due to the lack of iterative training, which hinders progressive model refinement. The ink-level-based selection is also not an adequate criterion. Human annotators likely use a similar approach, prioritizing patches with more representation of a layer’s information. In contrast, methods like entropy and random selection aim to select samples with more variability of information. Among these, entropy performs the best by targeting the most informative samples while maintaining a balanced representation of the layer’s information. 

Table 3 summarizes the F<sup>m</sup> 1<sup>scores for 1, 2, 4, 8, 16, and</sup> 32 labeled samples, along with the time required for labeling. The entropy-based method generally yields the best results, though random selection outperforms it for 2 and 4 samples. From 8 samples onward, entropy consistently outperforms all methods. According to these results, with just 8 labeled samples (or 16 for further improvements), a competitive model can be achieved, with up to a 4.3% F<sup>m</sup> 1<sup>improvement over human selection and up to a 21.6%</sup> improvement over the current FSL state of the art [12]. 

## 4.3 Qualitative analysis 

This section presents a qualitative comparison of the patches selected by human annotators and those chosen by the automatic methods. Figure 5 illustrates an example for the “Text” layer of the EINSIEDELN dataset, highlighting with different colors the patches that coincide between methods. Complete examples of the selected patches across all layers and datasets are available as supplementary material at Zenodo: `https://doi.org/` 

|||F<sup>m</sup><br>1 <sup>per</sup>|<sup>number o</sup>|<sup>f labeled s</sup>|<sup>amples</sup>||
|---|---|---|---|---|---|---|
|Method|1|2|4|8|16|32|
|Humans|57.0|63.4|69.1|76.8|82.0|85.3|
|Random|57.4|65.2|70.7|78.1|82.7|84.6|
|Ink-level|58.1|64.0|68.0|71.7|82.9|86.0|
|Sequent.|55.5|57.1|57.2|62.4|71.1|72.0|
|Entropy|59.5|63.4|68.9|81.1|84.4|86.4|
|FSAE [12]|53.7|49.3|57.4|59.7|67.7|68.4|
|Tmp.|0:08:18|0:16:36|0:33:12|1:06:24|2:12:48|4:25:36|



Table 3: Results of F<sup>m</sup> 1<sup>for the different selection methods</sup> compared, based on the number of labeled samples (1, 2, 4, 8, 16, and 32). The “Tmp.” row indicates the estimated time (hh:mm:ss) required for labeling based on Table 2. 

## `10.5281/zenodo.15735893` . 

In general, all the selected patches seem appropriate, as they contain text, which does not explain the worse performance of some criteria. A closer look reveals that the inklevel-based method tends to select decorative letters, which have higher ink levels, or cases with two lines of text (last row). However, these cases are less common in the dataset. The random and sequential methods select similar patches, yet sequential selection performs worse. Their selections also resemble those made by the entropy-based method in terms of ink levels and layer examples, but with the difference that entropy selection seems to favor samples with more noise, stains, or degradation. 

Regarding the human annotators, the selected patches are quite similar across annotators and also to the automatic methods, especially to the entropy-based criterion. Notably, annotators H4 and H5 (with H4 being the best performer and H5 having intermediate results) selected two patches that overlap with the entropy-based method. Even for H2, the poorest performer, the selected samples seem quite appropriate from a human perspective, showing text as well as examples of degradation. Thus, the reason for H2’s poorer performance is not immediately apparent. 

This analysis highlights that identifying the best samples is not always straightforward. The results suggest that selection criteria based on layer representation or ink level may not always capture the most informative samples, and that human judgment tends to focus on characteristics that may not be the most suitable for training neural networks. 

## 5. CONCLUSIONS 

This work proposes an active learning framework for layout analysis (LA) in Optical Music Recognition (OMR), building upon an existing Few-Shot Learning (FSL) method. By integrating this approach into an iterative training process—where new samples are progressively selected and annotated—we aim to make the most of limited labeled data and improve the original algorithm’s accuracy. 

A central focus of the study is the comparison between human and automated sample selection strategies within this active learning setup. While selection is typically carried out by human annotators in this context, our findings suggest that their choices do not always align with the requirements of neural networks for effective learning and 

707 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
9 0 9 0<br>8 0 8 0<br>7 0 7 0<br>H1<br>H2<br>H3<br>6 0 6 0<br>H4 Humans Entropy<br>H5 Random Sequential<br>Avg. Ink-level FSAE<br>5 0 5 0<br>0 5 10 15 20 25 30 0 5 10 15 20 25 30<br>Iteration Iteration<br>mF1 mF1<br><!-- End of picture text -->

(a) Comparison of the results for the five human annotators in this study, along with the overall mean (dashed line). 

(b) Comparison of the average results obtained by human annotators with those from the automatic selection methods. 

Figure 4: Graphs showing the average F<sup>m</sup> 1<sup>resultsforthefourannotationlayersacrossthethreedatasets.Eachline</sup> represents a different selection method. The horizontal axis indicates the number of selected patches, ranging from 1 to 32. 



<!-- Start of picture text -->
H1 H2 H3 H4 H5 Random Ink Sequential Entropy<br>ato:<br>1<br>2<br>4<br>8<br>16<br>32 in<br><!-- End of picture text -->

Figure 5: Example of the patches selected for the EINSIEDELN dataset, specifically for the “Text” layer, by the five human annotators and the different automatic selection methods compared, for the samples 1, 2, 4, 8, 16, and 32. Patches that coincide across different selection criteria are highlighted with distinct colors. 

reliable model performance. Results vary notably depending on the individual, with performance differences of up to 17%, and an average variance of 13% between annotators across all iterations. 

In contrast, simple automated methods—particularly entropy-based selection—consistently outperform human strategies. Entropy selection reached a competitive F<sup>m</sup> 1<sup>of</sup> 81.1% with only 8 labeled patches, while humans needed 16 or more for similar results. This represents a substantial reduction in annotation effort and time. Furthermore, our approach improves upon existing FSL methods by up to 21.6%, thanks to the enhanced selection strategy and its 

integration into an iterative and incremental training loop. 

Overall, this study demonstrates that automated active learning strategies can remarkably optimize OMR workflows, reduce manual annotation time, and enhance model performance beyond what human intuition can achieve. These findings encourage the integration of machinedriven sample selection into annotation pipelines and question the assumption that human judgment is inherently superior in data selection tasks. As future work, we aim to explore more advanced, model-aware selection strategies that dynamically adapt to the current performance of the model to identify the most informative samples. 

708 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 6. ACKNOWLEDGMENTS 

This research was supported by the Spanish Ministry of Science and Innovation through the LEMUR project (PID2023-148259NB-I00). Juan P. Martinez-Esteso acknowledges support from the Generalitat Valenciana through the SmallOMR project (CIAICO/2023/255). Alejandro Galan-Cuenca also acknowledges support from the Generalitat Valenciana through grant CIACIF/2023/090. 

## 7. REFERENCES 

- [1] D. Bainbridge and T. Bell, “The challenge of optical music recognition,” Computers and the Humanities, vol. 35, no. 2, pp. 95–121, 2001. 

- [2] G. M. Binmakhashen and S. A. Mahmoud, “Document layout analysis: a comprehensive survey,” ACM Computing Surveys (CSUR), vol. 52, no. 6, pp. 1–36, 2019. 

- [3] F. J. Castellanos, A. J. Gallego, and I. Fujinaga, “Deep learning for optical music recognition: A review,” Feb. 2025. [Online]. Available: http://dx.doi.org/10.36227/ techrxiv.174077177.78767136/v1 

- [4] Z. Saleh, K. Zhang, J. Calvo-Zaragoza, G. Vigliensoni, and I. Fujinaga, “Pixel.js: Web-based pixel classification correction platform for ground truth creation,” in 2017 14th IAPR International Conference on Document Analysis and Recognition (ICDAR), vol. 02, 2017, pp. 39–40. 

- [5] F. J. Castellanos, A. J. Gallego, and J. Calvo-Zaragoza, “Unsupervised domain adaptation for document analysis of music score images,” in Proceedings of the 22nd International Society for Music Information Retrieval Conference, ISMIR 2021, Online, November 7- 12, 2021, 2021, pp. 81–87. 

- [6] C. Wick, A. Hartelt, and F. Puppe, “Staff, symbol and melody detection of medieval manuscripts written in square notation using deep fully convolutional networks,” Applied Sciences, vol. 9, no. 13, p. 2646, 2019. 

- [7] F. J. Castellanos, C. Garrido-Munoz, A. Ríos-Vila, and J. Calvo-Zaragoza, “Region-based layout analysis of music score images,” Expert Syst Appl., vol. 209, p. 118211, 2022. 

- [8] Y. Wang, Q. Yao, J. T. Kwok, and L. M. Ni, “Generalizing from a few examples: A survey on few-shot learning,” ACM Comput. Surv., vol. 53, no. 3, 2020. 

- [9] X. Li, L. Yu, C.-W. Fu, M. Fang, and P.-A. Heng, “Revisiting metric learning for few-shot image classification,” Neurocomputing, vol. 406, pp. 49–58, 2020. 

- [10] A. De Nardin, S. Zottin, M. Paier, G. L. Foresti, E. Colombi, and C. Piciarelli, “Efficient few-shot learning for pixel-precise handwritten document layout analysis,” in Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (WACV), January 2023, pp. 3680–3688. 

- [11] A. De Nardin, S. Zottin, C. Piciarelli, E. Colombi, and G. L. Foresti, “Few-shot pixel-precise document layout segmentation via dynamic instance generation and local thresholding,” International Journal of Neural Systems, vol. 33, no. 10, p. 2350052, 2023. 

- [12] F. J. Castellanos, A. J. Gallego, and I. Fujinaga, “A few-shot neural approach for layout analysis of music score images,” in Proceedings of the 24th International Society for Music Information Retrieval Conference, Milan, Italy, November 5-9, 2023, 2023, pp. 106–113. 

- [13] J. Zhu, H. Wang, and E. H. Hovy, “Learning a stopping criterion for active learning for word sense disambiguation and text classification,” in Third International Joint Conference on Natural Language Processing, IJCNLP 2008, Hyderabad, India, January 7-12, 2008. The Association for Computer Linguistics, 2008, pp. 366–372. 

- [14] B. Settles, “Active learning literature survey,” University of Wisconsin-Madison, Department of Computer Sciences, Tech. Rep. 1648, 2009. 

- [15] J. Calvo-Zaragoza, K. Zhang, Z. Saleh, G. Vigliensoni, and I. Fujinaga, “Music document layout analysis through machine learning and human feedback,” in 2017 14th IAPR International Conference on Document Analysis and Recognition (ICDAR), vol. 02, 2017, pp. 23–24. 

- [16] I. Fujinaga and G. Vigliensoni, “The art of teaching computers: The SIMSSA optical music recognition workflow system,” in 27th European Signal Processing Conference, EUSIPCO, A Coruña, Spain, September 2-6. IEEE, 2019, pp. 1–5. 

- [17] R. M. Gray, Entropy and Information Theory. Springer, 2011. 

- [18] A. E. Esteban, Ed., Música de la Catedral de Barcelona a la Biblioteca de Catalunya. Barcelona: Biblioteca de Catalunya, 2001. 

- [19] A. J. Gallego and J. Calvo-Zaragoza, “Staff-line removal with selectional auto-encoders,” Expert Syst Appl., vol. 89, pp. 138–148, 2017. 

- [20] L. Bottou, “Large-scale machine learning with stochastic gradient descent,” in Proceedings of COMPSTAT’2010. Springer, 2010, pp. 177–186. 

- [21] E. Saund, J. Lin, and P. Sarkar, “Pixlabeler: User interface for pixel-level labeling of elements in document images,” in 2009 10th International Conference on Document Analysis and Recognition. IEEE, 2009, pp. 646–650. 

709 

