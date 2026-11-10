---
paper_id: "000035"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706397/files/000035.pdf"
---

# UNIVERSAL MUSIC REPRESENTATIONS? EVALUATING FOUNDATION MODELS ON WORLD MUSIC CORPORA 

Charilaos Papaioannou<sup>1,2,3</sup> 

Emmanouil Benetos<sup>2</sup> Alexandros Potamianos<sup>1,3</sup> 

1 School of ECE, National Technical University of Athens, Greece 

2 Centre for Digital Music, Queen Mary University of London, UK 

3 Archimedes, Athena Research Center, Greece 

```
cpapaioan@mail.ntua.gr
```

## ABSTRACT 

Foundation models have revolutionized music information retrieval, but questions remain about their ability to generalize across diverse musical traditions. This paper presents a comprehensive evaluation of five state-of-the-art audio foundation models across six musical corpora spanning Western popular, Greek, Turkish, and Indian classical traditions. We employ three complementary methodologies to investigate these models’ cross-cultural capabilities: probing to assess inherent representations, targeted supervised fine-tuning of 1-2 layers, and multi-label few-shot learning for low-resource scenarios. Our analysis shows varying cross-cultural generalization, with larger models typically outperforming on non-Western music, though results decline for culturally distant traditions. Notably, our approaches achieve state-of-the-art performance on five out of six evaluated datasets, demonstrating the effectiveness of foundation models for world music understanding. We also find that our targeted fine-tuning approach does not consistently outperform probing across all settings, suggesting foundation models already encode substantial musical knowledge. Our evaluation framework and benchmarking results contribute to understanding how far current models are from achieving universal music representations while establishing metrics for future progress. 

## 1. INTRODUCTION 

The notion of music as a “universal language” remains contested among scholars [1, 2]. While some musical elements transcend cultural boundaries, traditions have evolved with distinct characteristics and semantic content [3,4]. This tension between universality and cultural specificity presents a complex challenge that modern artificial intelligence approaches offer a novel lens to investigate. 

Foundation models have emerged as a transformative paradigm across artificial intelligence (AI) domains [5], 

> © C. Papaioannou, E. Benetos, and A. Potamianos. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: C. Papaioannou, E. Benetos, and A. Potamianos, “Universal Music Representations? Evaluating Foundation Models on World Music Corpora”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

including music and audio [6–8]. In music information retrieval (MIR), these multipurpose models perform diverse tasks from beat tracking to automatic tagging [9,10]. Though implicitly claiming a form of universality, they largely neglect cultural dimensions while training predominantly on Western-centric data [10]. This raises a critical question: to what extent do foundation models actually provide universal music representations that generalize across diverse musical traditions? 

In this work, we evaluate five state-of-the-art audio models across six corpora spanning Western popular, Greek, Turkish, and Indian classical traditions, to quantitatively assess their cross-cultural capabilities and contribute to discussions about the universality of musical representations. We focus on automatic music tagging as our evaluation task and employ three complementary methodologies: (i) probing, which uses the models as frozen feature extractors with a trainable classifier, (ii) targeted supervised finetuning to assess adaptation potential, and (iii) multi-label few-shot learning to evaluate performance in low-resource scenarios common with world music collections. 

Our evaluation reveals both promising cross-cultural transfer capabilities as well as remaining gaps in universal music understanding, due to the decrease in performance for culturally distant domains and especially in lowresource scenarios. The contributions of this work can be summarized as follows: 

- This is the first comprehensive evaluation, to the best of our knowledge, of foundation models across culturally diverse music corpora. 

- We propose a methodological evaluation framework that integrates few-shot learning with traditional approaches, enabling systematic assessment of model representations under different training setups. 

- State-of-the-art results have been achieved by our approaches in five out of six datasets. 

- We have optimized multi-label few-shot learning, significantly reducing inference time and making it practical for large numbers of classes. 

- Our code is being made available<sup>1</sup> for reproducibility and to promote research on world music. 

- 1 `https://github.com/pxaris/FM-music-tagging` 

303 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 2. RELATED WORK 

Foundation models. Foundation models for music have emerged by leveraging large-scale self-supervised or contrastive learning on extensive audio datasets, enabling them to capture rich musical features applicable across diverse tasks. Representative works include JukeMIR [11], which explored representations from the Jukebox generative model [12], MULE [13], a self-supervised model pretrained on MusicNet dataset, and Music2Vec [14], which utilized masked prediction strategies with student-teacher approaches. Subsequent advancements like MusicFM [9] have scaled up both model size and training data, demonstrating effectiveness across multiple benchmark tasks. 

The landscape of current foundation models encompasses several architectural approaches: masked acoustic modeling, MERT [6], contrastive audio-text learning such as LAION-CLAP [7], and unified audio understanding with models like Qwen-Audio [8]. Despite their impressive performance on standard benchmarks, their crosscultural generalization capabilities remain largely unexplored, particularly regarding their effectiveness across diverse musical traditions beyond Western contexts. 

Automatic world music tagging. Automatic music tagging - predicting metadata such as genre, mood, and instrumentation from audio signals - is typically referred to as music auto-tagging [15–18] and constitutes a multilabel classification problem. Architectures addressing this task have evolved from convolutional models like VGGish [19] and Musicnn [20] to transformer-based approaches like AST [21] and more recent foundation models [9]. 

Research on world music computational analysis has grown in recent years [22], with studies focused on specific traditions including Turkish makam recognition [23, 24], Indian classical music classification [25], and analysis of Iranian and Korean traditional music [26, 27]. While a recent study applied auto-tagging across diverse musical datasets [28], this is the first time to the best of our knowledge where a comprehensive evaluation of foundation models on world music corpora is being conducted. 

To address the challenges of imbalanced tags and limited data inherent in world music research, we employ Label-Combination Prototypical Networks (LC-Protonets) [29] for few-shot learning. This approach extends Prototypical Networks [30] by creating prototypes for each label combination, rather than generating one prototype per label. While established benchmarks for evaluating representations on downstream tasks typically employ probing and fine-tuning methodologies [31–33], our work incorporates few-shot learning as a complementary evaluation approach, assessing foundation models’ capabilities in lowresource scenarios. 

## 3. METHODOLOGICAL FRAMEWORK 

Our methodological framework systematically evaluates whether foundation models can effectively represent musical characteristics across diverse cultural traditions. As shown in Figure 1, we employ three complementary 



<!-- Start of picture text -->
Foundation Model - MLP Probe<br>(1)Prob. 心<br>(2)SFT<br>tags<br>frozen last →0→1<br>layers layers hidden >1<br>sigmoid<br>(3)ML-FSL Prob.<br>PT SFT<br>frozen<br>trainable extendedtags 1010个：小个 0011个个个<br><!-- End of picture text -->

Figure 1. Architectural overview of our evaluation framework showcasing three methodologies: (1) Probing (Prob.), (2) Supervised Fine-Tuning (SFT), and (3) MultiLabel Few-Shot Learning (ML-FSL). The diagram indicates feature extraction points used by ML-FSL from either Pre-Trained (PT), trained Prob. or SFT models. 

methodologies: probing (Prob.), supervised fine-tuning (SFT), and multi-label few-shot learning (ML-FSL). Probing trains only an MLP classifier on frozen model representations, while SFT makes the model’s last layers trainable alongside the MLP. ML-FSL extracts representations from three contexts, i.e., pretrained model (PT), trained probing model (Prob.) and fine-tuned model (SFT) to evaluate performance on extended tag sets under data scarcity conditions. 

## 3.1 Models 

For our evaluation, we selected five state-of-the-art audio models spanning different architectures, pre-training approaches, and parameter scales: 

MERT. We evaluate two variants of MERT [6]: MERT95M<sup>2</sup> and MERT-330M<sup>3</sup> with 95M and 330M parameters respectively. These transformer-based models employ masked acoustic modeling, using an acoustic and a musical teacher, during pre-training. MERT-95M consists of 12 layers, while MERT-330M has 24 layers. 

LAION-CLAP. We include two variants: CLAP-Music<sup>4</sup> (CLAP-M), trained exclusively on music data, and CLAPMusic&Speech<sup>5</sup> (CLAP-M&S), which incorporates additional speech data [7]. Both utilize HTS-AT [34] for audio encoding, a transformer-based model with 4 groups of swin-transformer blocks [35], with 68M audio-specific parameters within a larger 194M parameter model. 

Qwen2-Audio. The largest model in our evaluation framework, Qwen2-Audio<sup>6</sup> [36], contains 637M audio-specific parameters within an 8.4B parameter architecture and features 32 transformer layers [37] in its audio tower. 

VGG-ish. As a baseline comparison, we include VGGish [17,38], a 3.6M parameter end-to-end model trained via supervised learning on mel-spectrograms to predict tags. For VGG-ish, we report results from the literature for the 

> 2 https://huggingface.co/m-a-p/MERT-v1-95M 

> 3 https://huggingface.co/m-a-p/MERT-v1-330M 

> 4 https://huggingface.co/laion/larger_clap_music 

> 5 https://huggingface.co/laion/larger_clap_music_and_speech 

> 6 https://huggingface.co/Qwen/Qwen2-Audio-7B 

304 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

same experimental setup used in our work [28, 29] rather than running new experiments. 

## 3.2 Datasets 

Our evaluation spans diverse traditions from six music datasets. For Western music, we utilize MagnaTagATune [39] (25,863 clips) and FMA-medium [40] (25,000 tracks). For world music traditions, we incorporate the Lyra dataset [41] with 1,570 recordings of Greek folk music, and three collections from the CompMusic project [42]: the Turkishmakam corpus [43, 44] (5,297 recordings) as well as Hindustani [45] (1,204 recordings) and Carnatic [45] (2,612 recordings) of Indian classical music. 

Following [28], we set maximum audio durations to achieve similar sizes between datasets and prepare their metadata for the auto-tagging task. For Probing and Supervised Fine-Tuning, we use the standard tag sets, i.e., 50 tags for MagnaTagATune, 30 for Lyra and Turkish-makam, and 20 for the rest of the datasets. Our ML-FSL experiments use extended tag sets that include previously unseen classes, summing up to: 80 tags for MagnaTagATune, 60 for Lyra and Turkish-makam, 40 for FMA-medium and Carnatic, and 35 for Hindustani, consistent with [29]. 

## 3.3 Evaluation methodologies 

Probing. Our first methodology (Prob.) evaluates how well foundation models inherently represent musical characteristics across cultures. We employ probing, where the model remains frozen while only training a classifier on top of the extracted representations. Specifically, we implement a shallow Multi-layer Perceptron (MLP) with a single hidden layer of 512 units followed by a sigmoid classification layer, optimized with binary cross-entropy loss. Supervised Fine-Tuning. To evaluate adaptation potential, we implement targeted supervised fine-tuning (SFT) by unfreezing a subset of model parameters. For MERT95M, we unfreeze the last two transformer layers, while for MERT-330M only the last layer. For both CLAP models, we unfreeze the last group of swin-transformer blocks of the audio encoder along with the normalization and two projection layers. In Qwen2-Audio, we fine-tune the last layer of the audio tower along with the normalization layer before multi-modal projection. These choices were constrained by RAM limitations affecting both trainable parameters and hyperparameter tuning. We use the same trainable MLP Probe architecture as in the Probing experiments, initializing it with the weights learned during that phase. This weight initialization strategy helps maintain previously learned knowledge while adapting to new domains, mitigating potential catastrophic forgetting issues [46]. We also employ learning rate warmup and cosine scheduling to ensure stable adaptation [47]. 

Multi-Label Few-Shot Learning. Our third methodology (ML-FSL) evaluates performance in low-resource scenarios by employing an optimized version of LC-Protonets [29] that is detailed in subsection 3.4. We extract representations from three different contexts: directly from the pretrained model (PT), from the hidden layer of the trained 



<!-- Start of picture text -->
89<br>Qwen2-Audio<br>(88.98)<br>88 MERT-95M<br>(87.25)<br>87<br>86 CLAP-Music&Speech<br>(86.47)<br>MERT-330M<br>85 VGG-ish<br>(84.45) (85.55)<br>Avg. ROC-AUC (Probing &SFT)84<br>101 102<br>Number of Audio Parameters (Millions)<br><!-- End of picture text -->

Figure 2. Relationship between model size and performance, averaged over Probing and Supervised FineTuning (SFT) tasks. The x-axis represents the number of audio-specific parameters on a logarithmic scale, while the y-axis reports the mean ROC-AUC (%) across all datasets. 

MLP Probe (Prob.), and from the fine-tuned model (SFT). Notably, this methodology involves no additional training during few-shot evaluation; the model acts as a frozen feature extractor that maps both the few examples and the unknown items to an embedding space where classification occurs utilizing the LC-Protonets approach. 

## 3.4 Multi-label few-shot learning optimization 

While the LC-Protonets method [29] offers significant performance advantages for multi-label few-shot learning, its computational complexity increases substantially with the number of labels due to the exponential growth of label combinations. In this work, we introduce an optimization that significantly improves inference efficiency while maintaining identical classification results. 

The original approach creates an LC-Prototype (LCP) for each label combination (LC-class) derived from the power sets of the few available examples’ labels. Each available example is called a support item and it is defined by (xi, yi), with xi being its input feature vector and yi the set of its labels. For the set of support items S, the set of all LC-classes L is computed as L = U (xi,yi)∈S<sup>P(yi),</sup> where P(yi) is the power set of the labels of the i-th support item, excluding the empty set. For each LC-class Lj, with j = 1, 2, ..., |L|, the LCP representation pj is computed by averaging the embeddings of all support items that include Lj in their power sets: 1 pj = fθ(xi), (1) |Sj| (xi,yi)∈Sj 

where Sj = {(xi, yi) ∈ S | Lj ∈P(yi)}, and fθ the embedding mapping model. 

Our key insight is that multiple LC-classes often share identical LCP representations despite representing different label combinations. This occurs because the same set of support items contributes to multiple label combinations derived from their power sets. For example, if a support item with labels {A, B, C} is the only item contributing 

305 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

to both {A, B} and {B, C} LCPs, these LCPs will have identical representations. 

We exploit this redundancy by maintaining a dictionary structure that maps unique LCP representations to their corresponding sets of LC-classes: 

UniqueLCPs = {pm �→{Lj | pj = pm}}, (2) 

where j = 1, 2, ..., |L| and m = 1, 2, ..., M with M being the number of unique LCPs and M ≪|L|. During inference, instead of computing distances between a query item, unseen during training, and all possible |L| LCPs, we only compute distances to the M unique LCP representations. For the nearest unique LCP, we then select the label combination with the maximum cardinality, consistent with the original LC-Protonets method. 

Our experiments show that this approach yields speed improvements of 10× for datasets with 20 labels, scaling to more than 100× for datasets with 60 labels, while producing identical classification results to the original method. We apply this optimization to the LC-Protonets repository<sup>7</sup> , making it practical for large label sets. 

## 4. EXPERIMENTAL SETUP 

Experiments and resources. We conducted 5 runs with different random seeds for both Probing and ML-FSL tasks, but a single run for SFT due to computational constraints. SFT trainable parameters varied: 14M for MERT-95M, 13M for MERT-330M, 25M for CLAP models, and 56M for Qwen2-Audio. All experiments ran on an NVIDIA RTX A5000 GPU, and we used Qwen2-Audio in half-precision (FP16) in all our methodologies to fit in this card. Most SFT training completed within 24 hours, with only 3 out of 30 experiments extending to about 36 hours. Dataset processing. We standardized Turkish-makam, Hindustani, and Carnatic datasets to approximately 200 hours each, matching MagnaTagATune and FMA-medium durations [28], while Lyra remained at its original 80 hours. We followed the training, validation, and test splits from [17,28]. For ML-FSL, evaluation items came exclusively from test sets [29] to prevent data leakage. 

Model-specific configurations. Each foundation model required specific preprocessing: MERT models use 30second windows at 24kHz, CLAP models 10-second windows at 48kHz, and Qwen2-Audio 30-second windows at 16kHz. All audio was converted to mono and resampled to the model’s required rate. 

Representation extraction strategies. For MERT models, we extract representations by summing the average, across time, hidden states of the last four layers of the models. For CLAP models, we extract them from the audio projection layer which takes as input the average pooled layer representation of the last hidden state. For Qwen2-Audio, we use the last hidden state embeddings averaged across all layers of the whole model, when passing a simple text prompt that includes nothing but the respective tags for audio processing, i.e., `<|audio_bos|><|AUDIO|><|audio_eos|>` . 

> 7 `https://github.com/pxaris/LC-Protonets` 

|Model|Params<br>Audio/Total|ROC-AU|C(%)|mAP|(%)|
|---|---|---|---|---|---|
|VGG-ish [28]|3.6M/3.6M|84.4|5|50.5|6|
|||Prob.|SFT|Prob.|SFT|
|MERT-95M|95M/95M|87.250.32|87.26|52.250.42|52.68|
|MERT-330M|330M/330M|85.400.68|85.69|49.620.83|50.47|
|CLAP-M|68M/194M|71.521.14|78.96|29.981.07|40.41|
|CLAP-M&S|68M/194M|86.780.31|86.15|53.120.87|51.99|
|Qwen2-Audio|637M/8.40B|88.590.47|89.37|56.480.63|58.73|



Table 1. Model performance comparison averaged across all datasets for Probing and SFT tasks. Values are averaged over multiple runs with subscripted standard deviations. Bold values indicate best performance per column. 

These representation extraction strategies, number of finetuned layers, and other design choices of our method were optimized through preliminary experiments. Hyperparameters. For Probing, we used Adam optimizer [48] (β1 = 0.9, β2 = 0.999, ϵ = 10<sup>−8</sup> ) with learning rate 10<sup>−3</sup> , batch size 16, early stopping patience 10, and maximum 200 epochs. For SFT, we used AdamW [49] with identical β parameters but learning rate 10<sup>−4</sup> , model-specific batch sizes (to fit maximum available resources) with gradient accumulation to simulate batch size 16 across all setups, patience 5, and maximum 30 epochs. We applied learning rate warmup and cosine scheduling for the first 5% of SFT epochs. ML-FSL evaluations used cosine distance with an N -way K-shot setup, with N being the number of extended tags per dataset and K equal to 3 examples per label in all experiments. We also attempted Low-Rank Adaptation [50] initially but abandoned it due to extensive hyperparameter tuning requirements across our 5 × 6 experimental matrix. 

Evaluation metrics. For the Probing and SFT methodologies, we report area under the receiver operating characteristic curve (ROC-AUC) and mean average precision (mAP). These metrics are particularly well-suited for multi-label classification tasks [51] and are consistent with prior work in music tagging [17, 28]. For ML-FSL evaluation, we report macro-F1 (M-F1) and micro-F1 (mF1) scores, which align with the LC-Protonets evaluation framework [29]. F1 score is the harmonic mean of the precision and recall scores. Macro-F1 gives equal weight to all classes, while micro-F1 accounts for class imbalance by calculating metrics globally across all instances. 

## 5. RESULTS 

## 5.1 Probing and Supervised Fine-Tuning 

Table 1 presents the performance of the evaluated foundation models averaged across all datasets for both Probing and SFT tasks. Overall, Qwen2-Audio achieves the highest performance with 88.59% ROC-AUC and 56.48% mAP in Probing, further improving to 89.37% ROC-AUC and 58.73% mAP after fine-tuning. This is followed by MERT95M and CLAP-Music&Speech with comparable performance, while CLAP-Music shows significantly lower performance without speech data in its training corpus. 

306 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

|Model|MagnaT<br>ROC-AUC|agATune<br>mAP|FMA-m<br>ROC-AUC|edium<br>mAP|Ly<br>ROC-AUC|ra<br>mAP|Turkish-<br>ROC-AUC|makam<br>mAP|Hindu<br>ROC-AUC|stani<br>mAP|Carn<br>ROC-AUC|atic<br>mAP|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|VGG-ish[28]|91.23|45.82|88.89|49.49|80.97|48.06|86.96|56.39|84.77|60.82|73.92|42.78|
||||||Probi|ng (Prob.)|||||||
|MERT-95M|90.460.10|44.160.21|91.680.08|51.430.43|85.610.66|53.340.61|88.220.23|57.890.34|86.590.52|60.260.56|80.960.35|46.410.35|
|MERT-330M|89.660.16|41.730.59|90.780.11|48.850.32|84.650.78|51.810.59|85.370.64|52.451.12|84.231.36|58.782.08|77.731.03|44.070.31|
|CLAP-M|80.070.21|25.820.13|77.420.15|22.890.38|64.181.29|31.160.43|77.310.51|38.771.00|68.694.05|33.434.21|61.470.60|27.830.30|
|CLAP-M&S|92.410.05|48.540.16|94.050.08|59.130.54|87.250.18|56.940.51|86.490.27|54.690.36|82.611.14|55.703.29|77.850.13|43.730.35|
|Qwen2-Audio|91.170.13|45.580.21|96.600.07|73.380.28|86.440.81|53.500.65|86.640.42|53.380.79|88.450.83|62.420.99|82.220.56|50.590.88|
|||||S|upervised F|ine-Tuning|(SFT)||||||
|MERT-95M|90.62|44.52|91.70|51.74|84.89|53.62|87.50|57.91|88.20|61.47|80.64|46.83|
|MERT-330M|89.55|41.93|91.12|49.56|84.74|52.54|86.17|53.80|85.49|61.33|77.05|43.66|
|CLAP-M|88.54|39.26|88.37|42.04|71.97|38.14|79.82|42.49|75.65|45.01|69.39|35.51|
|CLAP-M&S|91.77|47.54|92.86|57.11|85.35|52.86|86.69|54.93|83.73|56.91|76.51|42.58|
|Qwen2-Audio|92.03|48.27|97.02|75.94|87.57|57.04|87.95|56.10|88.32|64.35|83.35|50.66|
|(Previous)SOTA|92.7|46.54|92.4|53.7|85.4|54.3|87.7|57.7|86.5|63.1|77.0|43.9|



Table 2. Model performance on individual datasets for Probing and SFT tasks. For Probing, values are averaged over multiple runs with subscripted standard deviations, while SFT results are from single runs. Bold values indicate best performance per metric and dataset. SOTA values are from [52] for MagnaTagATune and [28] for the rest of the datasets. 

Figure 2 illustrates the relationship between model size (audio-specific parameters) and ROC-AUC performance, averaged across datasets and both Probing and SFT tasks. A generally positive correlation is revealed, with similar trends observed in both methodologies. Qwen2-Audio (637M parameters) consistently outperforms smaller models, achieving 88.98% average ROC-AUC score. Surprisingly, MERT-95M (87.25%) outperforms the much larger MERT-330M (85.55%). This is worth noting as [33] reported that both models performed on par for auto-tagging tasks, suggesting that our common representation extraction strategy for both MERT models may not optimally leverage the larger model’s capacity. Another potential explanation is that MERT-95M has been trained on open data whereas MERT-330M has been trained with additional proprietary data with a strong Western bias [6]. 

When examining Probing (Prob.) performance across individual datasets, in Table 2, we observe a consistent pattern of decreasing performance for music traditions that are culturally distant from the data used to pre-train the respective foundation models. Western music datasets (MagnaTagATune and FMA-medium) consistently achieve the highest performance across all models, with ROC-AUC values reaching 96.60% for Qwen2-Audio on FMA-medium. Greek (Lyra) and Turkish (makam) music datasets show moderate performance, while Indian classical music (Hindustani and Carnatic) datasets typically exhibit the lowest performance. This cultural performance gap is especially pronounced for CLAP-Music, where the ROC-AUC drops from 80.07% for MagnaTagATune to 61.47% for Carnatic. 

Applying Supervised Fine-Tuning (SFT) generally improves performance across all models and datasets, with an average gain of 1-2% in ROC-AUC for most models. Notably, CLAP-Music shows the largest improvement with SFT, indicating greater adaptation potential despite lower absolute performance. For other models, the modest gains suggest that they require broader fine-tuning to further shift their pre-trained representations towards different cultures. 

Importantly, our approaches achieve state-of-the-art performance in five out of six datasets, with MagnaTa- 

Model M-F1 m-F1 VGG-ish [29] 30.18 55.09 <mark>PT Prob. SFT PT Prob. SFT</mark> MERT-95M 23.901.52 28.051.74 28.281.80 46.591.57 52.161.43 52.561.63 MERT-330M 23.031.12 28.481.40 28.511.28 45.111.29 51.781.51 51.801.46 CLAP-M 17.711.20 18.431.40 21.581.13 38.801.37 39.971.20 46.571.20 CLAP-M&S 28.231.36 29.221.09 30.271.90 51.591.54 53.321.31 54.431.27 <mark>Q</mark> wen2-Audio 25.981.36 30.961.26 32.001.41 49.971.41 55.660.82 56.851.23 

Table 3. ML-FSL performance averaged across datasets on extended tag sets. Results show macro-F1 (M-F1) and micro-F1 (m-F1) across contexts (PT, Prob., SFT). Values are means with subscripted standard deviations. Bold indicates best performance per column. 

gATune being the only exception. However, their consistent performance decrease towards diverse cultures, suggests that their representations are still biased toward Western musical traditions. 

## 5.2 Multi-label few-shot learning 

Table 3 presents the ML-FSL evaluation results averaged across all datasets using extended tag sets. The results show consistent performance improvements moving from pre-trained models (PT) to trained probing models (Prob.) and then to supervised fine-tuned models (SFT) across all foundation models. The substantial gap between macro-F1 and micro-F1 metrics indicates considerable class imbalance in the extended tag sets, while the increased standard deviation stems from the support set sampling which can significantly impact the classification performance. 

Qwen2-Audio demonstrates the best overall performance in the ML-FSL task with 32.00% macro-F1 and 56.85% micro-F1 after fine-tuning, followed closely by CLAP-Music&Speech with 30.27% macro-F1 and 54.43% micro-F1. Notably, even the best foundation model’s performance (Qwen2-Audio) is comparable to a VGG-ish feature extractor trained via supervised learning on standard tags for each dataset. This stands in contrast to the Probing and SFT settings (Table 1), where foundation models clearly outperform VGG-ish, showing that ML-FSL tasks 

307 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

|Mdl|MagnaT|agATune|FMA-|medium|Ly|ra|Turkish|-makam|Hind|ustani|Car|natic|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|oe|M-F1|m-F1|M-F1|m-F1|M-F1|m-F1|M-F1|m-F1|M-F1|m-F1|M-F1|m-F1|
|VGG-ish[29]|26.40|37.31|29.12|45.37|46.05|69.03|30.07|56.22|31.33|58.38|18.13|64.25|
||||||Pre-Train|ed models|(PT)||||||
|MERT-95M<br>MERT-330M|18.761.04<br>18.170.78|28.371.38<br>26.991.36|16.240.64<br>16.240.69|35.370.94<br>31.151.51|46.872.59<br>44.221.45|66.072.25<br>65.481.57|20.691.77<br>20.142.01|40.951.80<br>39.711.95|25.872.45<br>25.081.40|51.501.92<br>50.141.08|14.970.64<br>14.320.41|57.261.10<br>57.210.28|
|CLAP-M|13.100.84|20.001.15|9.650.29|19.771.31|33.562.88|57.141.49|14.331.10|32.121.37|21.061.63|47.381.60|14.550.43|56.421.30|
|CLAP-M&S<br>Qwen2-Audio|25.900.55<br>21.290.51|36.550.61<br>32.090.26|28.781.66<br>29.762.23|42.952.02<br>47.501.86<br>T|48.032.02<br>39.991.05<br>rained Prob|69.041.54<br>64.241.07<br>ingmodels|24.191.73<br>19.891.71<br> (Prob.)|47.132.22<br>42.271.88|26.291.20<br>28.421.96|54.501.57<br>55.921.70|16.191.02<br>16.550.69|59.381.30<br>57.821.67|
|MERT-95M<br>MERT-330M|23.770.85<br>24.480.59|34.711.03<br>34.781.45|24.621.19<br>25.210.76|42.961.30<br>40.651.76|45.802.76<br>47.923.26|68.161.81<br>70.152.18|26.141.73<br>26.971.61|50.000.70<br>50.471.13|30.752.95<br>29.251.55|56.412.18<br>53.771.82|17.250.98<br>17.060.61|60.701.55<br>60.850.69|
|CLAP-M|14.840.49|22.671.00|11.550.50|22.721.48|34.854.03|57.731.37|16.680.81|36.001.22|18.771.42|44.960.95|13.871.16|55.741.15|
|CLAP-M&S<br>Qwen2-Audio|26.900.47<br>26.790.40|37.620.93<br>37.650.21|31.141.28<br>39.491.02|46.531.59<br>56.300.82|47.100.89<br>42.521.81|69.770.53<br>67.101.13|25.581.59<br>26.091.65|49.701.39<br>51.591.20|28.111.38<br>31.621.26|56.432.19<br>60.080.40|16.460.92<br>19.251.40|59.881.25<br>61.241.14|
|||||Sup|ervised Fin|e-Tuned mo|dels(SFT)||||||
|MERT-95M<br>MERT-330M<br>CLAP-M<br>CLAP-M&S<br>Qwen2-Audio|24.460.79<br>23.780.65<br>22.150.51<br>26.280.50<br>27.670.25|35.280.90<br>33.670.91<br>32.671.22<br>37.231.09<br>38.570.18|24.941.18<br>24.941.21<br>19.610.79<br>30.271.56<br>40.101.29|42.781.44<br>39.951.77<br>34.810.99<br>46.571.61<br>57.170.95|45.513.74<br>48.502.75<br>30.462.04<br>48.094.74<br>44.132.45|67.932.72<br>70.062.23<br>55.862.02<br>69.932.28<br>68.342.38|26.161.87<br>26.841.51<br>20.661.69<br>28.911.75<br>27.612.37|49.761.54<br>50.291.25<br>45.801.13<br>53.871.56<br>53.981.55|30.402.15<br>30.561.31<br>21.951.31<br>31.272.47<br>32.521.23|56.391.68<br>55.251.58<br>50.741.14<br>57.410.74<br>60.260.89|18.181.08<br>16.430.27<br>14.630.45<br>16.820.37<br>19.970.87|63.191.48<br>61.571.04<br>59.530.67<br>61.550.34<br>62.761.43|



Table 4. ML-FSL performance on extended tag sets per dataset. Results show macro-F1 (M-F1) and micro-F1 (m-F1) across three contexts. Values are means with subscripted standard deviations. Bold indicates best performance per column. 



<!-- Start of picture text -->
Number of LCPs vs N-labels<br>105 Time/query vs N-labels - Original 53640 105<br>Time/query vs N-labels - Optimized<br>104 7853 104<br>(ms/query)<br>103 time<br>102 102<br>LC-Prototypes# 17ms<br>101 2ms 4ms 101Inference<br>10020 30 40 50 60 100<br>N-labels<br><!-- End of picture text -->

Figure 3. Scalability metrics of the LC-Protonets method, averaged across all datasets. The x-axis represents the number of labels, the left y-axis shows the number of LCPs, and the right y-axis indicates the inference time per item with both y-axes using the same logarithmic scale. 

remain challenging for them despite their extensive pretraining. Supervised learning of a VGG-ish model on extended tag sets has not been conducted in the literature, likely due to the scarcity of examples for infrequent tags. 

When examining the ML-FSL results per dataset in Table 4, we observe that only on Western datasets (MagnaTagATune and FMA-medium) does the best foundation model (Qwen2-Audio) achieve significantly better performance than the VGG-ish baseline. For Turkish-makam, VGG-ish representations actually outperform foundation models, while for Lyra, Hindustani, and Carnatic, the results are comparable. This pattern provides additional clear evidence of the implicit Western-centric bias integrated into models due to their pre-training data. 

LC-Protonets optimization. Figure 3 illustrates the scalability metrics of our optimized LC-Protonets approach compared to the original method, averaged across datasets. As the number of labels increases from 20 to 60, the number of LC-Prototypes grows exponentially, from approximately 500 to over 50,000. This growth leads the origi- 

nal method to a corresponding increase from 21ms to over 2,000ms inference time per query item (dashed blue line). However, our optimization (solid blue line), leveraging the unique prototypes, mitigates the computational complexity issues, requiring only 2ms in the 20 labels cases and rising to no more than 20ms for 60 labels, a 100× improvement. 

## 6. CONCLUSIONS 

In this paper, we examined the universality of music representations in foundation models through a comprehensive methodological framework evaluating five state-of-the-art audio models across six world music corpora. Although these models achieved better performance than previous models for diverse music traditions, we found clear indicators of Western-centric bias. 

Our incorporation of ML-FSL tasks particularly revealed this limitation. When faced with these challenging scenarios, foundation models performed on par with significantly smaller and simpler models, with performance notably degrading further on non-Western datasets. 

To further enable ML-FSL evaluation, we substantially optimized the computational complexity of the utilized method, by forming unique prototypes representing multiple label combinations. We demonstrated that this change makes it practical for large sets of labels, a typical condition when studying world music datasets. 

Future work could extend our methodological framework by incorporating Low-Rank Adaptation (LoRA) and implement broader supervised fine-tuning to investigate further cultural adaptation. More tasks can also be included such as mode estimation, exploring the analogies between key on Western cultures and makam or raga recognition in other cultures. 

We hope this work brings attention to the cultural dimensions of foundation models while providing a framework for quantitatively assessing progress toward truly universal musical representations. 

308 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 7. ACKNOWLEDGMENTS 

We would like to thank the reviewers for their valuable and constructive feedback, which helped us improve our study. This work has been partially supported by project MIS 5154714 of the National Recovery and Resilience Plan Greece 2.0 funded by the European Union under the NextGenerationEU Program. 

## 8. REFERENCES 

- [1] S. A. Mehr, M. Singh, D. Knox, D. M. Ketter, D. Pickens-Jones, S. Atwood, C. Lucas, N. Jacoby, A. A. Egner, E. J. Hopkins, R. M. Howard et al., “Universality and diversity in human song,” Science, vol. 366, 2019. 

- [2] P. E. Savage, S. Brown, E. Sakai, and T. E. Currie, “Statistical universals reveal the structures and functions of human music,” Proceedings of the National Academy of Sciences, vol. 112, pp. 8987 – 8992, 2015. 

- [3] S. E. Trehub, J. Becker, and I. Morley, “Cross-cultural perspectives on music and musicality,” Philosophical Transactions of the Royal Society B: Biological Sciences, vol. 370, 2015. 

- [4] E. H. Margulis, P. C. M. Wong, C. Turnbull, B. M. Kubit, and J. D. McAuley, “Narratives imagined in response to instrumental music reveal culturebounded intersubjectivity,” Proceedings of the National Academy of Sciences of the United States of America, vol. 119, 2022. 

- [5] R. Bommasani, D. A. Hudson, E. Adeli, R. B. Altman, S. Arora, S. von Arx, M. S. Bernstein, J. Bohg, A. Bosselut, E. Brunskill, E. Brynjolfsson, S. Buch, D. Card, R. Castellon, N. S. Chatterji, A. S. Chen, K. Creel et al., “On the opportunities and risks of foundation models,” CoRR, vol. abs/2108.07258, 2021. 

- [6] Y. Li, R. Yuan, G. Zhang, Y. Ma, X. Chen, H. Yin, C. Xiao, C. Lin, A. Ragni, E. Benetos, N. Gyenge et al., “MERT: acoustic music understanding model with large-scale self-supervised training,” in ICLR. OpenReview.net, 2024. 

- [7] Y. Wu, K. Chen, T. Zhang, Y. Hui, T. Berg-Kirkpatrick, and S. Dubnov, “Large-scale contrastive languageaudio pretraining with feature fusion and keyword-tocaption augmentation,” in ICASSP. IEEE, 2023, pp. 1–5. 

- [8] Y. Chu, J. Xu, X. Zhou, Q. Yang, S. Zhang, Z. Yan, C. Zhou, and J. Zhou, “Qwen-audio: Advancing universal audio understanding via unified large-scale audio-language models,” CoRR, vol. abs/2311.07919, 2023. 

- [9] M. Won, Y. Hung, and D. Le, “A foundation model for music informatics,” in ICASSP. IEEE, 2024, pp. 1226–1230. 

- [10] Y. Ma, A. Øland, A. Ragni, B. M. Del Sette, C. Saitis, C. Donahue, C. Lin, C. Plachouras, E. Benetos, E. Quinton et al., “Foundation models for music: A survey,” CoRR, vol. abs/2408.14340, 2024. 

- [11] R. Castellon, C. Donahue, and P. Liang, “Codified audio language modeling learns useful representations for music information retrieval,” in ISMIR, 2021, pp. 88–96. 

- [12] P. Dhariwal, H. Jun, C. Payne, J. W. Kim, A. Radford, and I. Sutskever, “Jukebox: A generative model for music,” CoRR, vol. abs/2005.00341, 2020. 

- [13] M. C. McCallum, F. Korzeniowski, S. Oramas, F. Gouyon, and A. F. Ehmann, “Supervised and unsupervised learning of audio representations for music understanding,” in ISMIR, 2022, pp. 256–263. 

- [14] Y. Li, R. Yuan, G. Zhang, Y. Ma, C. Lin, X. Chen, A. Ragni, H. Yin, Z. Hu, H. He, E. Benetos, N. Gyenge, R. Liu, and J. Fu, “Map-music2vec: A simple and effective baseline for self-supervised music audio representation learning,” CoRR, vol. abs/2212.02508, 2022. 

- [15] K. Choi, “Deep neural networks for music tagging,” Ph.D. dissertation, Queen Mary University of London, UK, 2018. 

- [16] T. Kim, J. Lee, and J. Nam, “Sample-level CNN architectures for music auto-tagging using raw waveforms,” in ICASSP. IEEE, 2018, pp. 366–370. 

- [17] M. Won, A. Ferraro, D. Bogdanov, and X. Serra, “Evaluation of cnn-based automatic music tagging models,” CoRR, vol. abs/2006.00751, 2020. 

- [18] J. Lee, J. Park, K. L. Kim, and J. Nam, “Samplelevel deep convolutional neural networks for music auto-tagging using raw waveforms,” CoRR, vol. abs/1703.01789, 2017. 

- [19] S. Hershey, S. Chaudhuri, D. P. W. Ellis, J. F. Gemmeke, A. Jansen, R. C. Moore, M. Plakal, D. Platt, R. A. Saurous, B. Seybold et al., “CNN architectures for large-scale audio classification,” in ICASSP. IEEE, 2017, pp. 131–135. 

- [20] J. Pons and X. Serra, “musicnn: Pre-trained convolutional neural networks for music audio tagging,” CoRR, vol. abs/1909.06654, 2019. 

- [21] Y. Gong, Y. Chung, and J. R. Glass, “AST: audio spectrogram transformer,” in Interspeech. ISCA, 2021, pp. 571–575. 

- [22] M. Panteli, “Computational analysis of world music corpora,” Ph.D. dissertation, Queen Mary University of London, UK, 2018. 

- [23] E. Demirel, B. Bozkurt, and X. Serra, “Automatic makam recognition using chroma features,” in 8th International Workshop on Folk Music Analysis, 2018, pp. 19–24. 

309 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [24] K. K. Ganguli, S. Sentürk, and C. Guedes, “Critiquing task- versus goal-oriented approaches: A case for makam recognition,” in ISMIR, 2022, pp. 369–376. 

- [25] A. K. Sharma, G. Aggarwal, S. Bhardwaj, P. Chakrabarti, T. Chakrabarti, J. H. Abawajy, S. Bhattacharyya et al., “Classification of indian classical music with time-series matching deep learning approach,” IEEE Access, vol. 9, pp. 102 041–102 052, 2021. 

- [26] B. Nikzat and R. C. Repetto, “KDC: an open corpus for computational research of dastg¯ahi music,” in ISMIR, 2022, pp. 321–328. 

- [27] D. Han, R. C. Repetto, and D. Jeong, “Finding tori: Self-supervised learning for analyzing korean folk song,” in ISMIR, 2023, pp. 440–447. 

- [28] C. Papaioannou, E. Benetos, and A. Potamianos, “From west to east: Who can understand the music of the others better?” in ISMIR, 2023, pp. 311–318. 

- [29] ——, “LC-Protonets: Multi-label few-shot learning for world music audio tagging,” IEEE Open Journal of Signal Processing, vol. 6, pp. 138–146, 2025. 

- [30] J. Snell, K. Swersky, and R. S. Zemel, “Prototypical networks for few-shot learning,” in NIPS, 2017, pp. 4077–4087. 

- [31] J. Turian, J. Shier, H. R. Khan, B. Raj, B. W. Schuller, C. J. Steinmetz, C. Malloy, G. Tzanetakis, G. Velarde, K. McNally, M. Henry, N. Pinto, C. Noufi et al., “HEAR: holistic evaluation of audio representations,” in NeurIPS (Competition and Demos), ser. Proceedings of Machine Learning Research, vol. 176. PMLR, 2021, pp. 125–145. 

- [32] S. Yang, P. Chi, Y. Chuang, C. J. Lai, K. Lakhotia, Y. Y. Lin, A. T. Liu, J. Shi, X. Chang, G. Lin, T. Huang, W. Tseng, K. Lee et al., “SUPERB: speech processing universal performance benchmark,” in Interspeech. ISCA, 2021, pp. 1194–1198. 

- [33] R. Yuan, Y. Ma, Y. Li, G. Zhang, X. Chen, H. Yin, L. Zhuo, Y. Liu, J. Huang, Z. Tian, B. Deng, N. Wang, C. Lin, E. Benetos, A. Ragni et al., “MARBLE: music audio representation benchmark for universal evaluation,” in NeurIPS, 2023. 

- [34] K. Chen, X. Du, B. Zhu, Z. Ma, T. Berg-Kirkpatrick, and S. Dubnov, “HTS-AT: A hierarchical tokensemantic audio transformer for sound classification and detection,” in ICASSP. IEEE, 2022, pp. 646–650. 

- [35] Z. Liu, Y. Lin, Y. Cao, H. Hu, Y. Wei, Z. Zhang, S. Lin, and B. Guo, “Swin transformer: Hierarchical vision transformer using shifted windows,” in ICCV. IEEE, 2021, pp. 9992–10 002. 

- [36] Y. Chu, J. Xu, Q. Yang, H. Wei, X. Wei, Z. Guo, Y. Leng, Y. Lv, J. He, J. Lin, C. Zhou, and J. Zhou, “Qwen2-audio technical report,” CoRR, vol. abs/2407.10759, 2024. 

- [37] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. Kaiser, and I. Polosukhin, “Attention is All you Need,” in Advances in Neural Information Processing Systems, 2017. 

- [38] K. Simonyan and A. Zisserman, “Very deep convolutional networks for large-scale image recognition,” in ICLR, 2015. 

- [39] E. Law, K. West, M. I. Mandel, M. Bay, and J. S. Downie, “Evaluation of algorithms using games: The case of music tagging,” in ISMIR, 2009, pp. 387–392. 

- [40] M. Defferrard, K. Benzi, P. Vandergheynst, and X. Bresson, “FMA: A dataset for music analysis,” in ISMIR, 2017, pp. 316–323. 

- [41] C. Papaioannou, I. Valiantzas, T. Giannakopoulos, M. A. Kaliakatsos-Papakostas, and A. Potamianos, “A dataset for greek traditional and folk music: Lyra,” in ISMIR, 2022, pp. 377–383. 

- [42] X. Serra, “Creating research corpora for the computational study of music: the case of the compmusic project,” in Semantic Audio. Audio Engineering Society, 2014. 

- [43] B. Uyar, H. S. Atli, S. Sentürk, B. Bozkurt, and X. Serra, “A corpus for computational research of turkish makam music,” in DLfM@JCDL. ACM, 2014, pp. 1–7. 

- [44] S. Sentürk, “Computational analysis of audio recordings and music scores for the description and discovery of ottoman-turkish makam music,” Ph.D. dissertation, Pompeu Fabra University, Spain, 2017. 

- [45] A. Srinivasamurthy, G. K. Koduri, S. Gulati, V. Ishwar, and X. Serra, “Corpora for music information research in indian art music,” in ICMC. Michigan Publishing, 2014. 

- [46] J. Kirkpatrick, R. Pascanu, N. C. Rabinowitz, J. Veness, G. Desjardins, A. A. Rusu, K. Milan, J. Quan, T. Ramalho, A. Grabska-Barwinska, D. Hassabis, C. Clopath, D. Kumaran, and R. Hadsell, “Overcoming catastrophic forgetting in neural networks,” CoRR, vol. abs/1612.00796, 2016. 

- [47] K. Gupta, B. Thérien, A. Ibrahim, M. L. Richter, Q. Anthony, E. Belilovsky, I. Rish, and T. Lesort, “Continual pre-training of large language models: How to (re)warm your model?” CoRR, vol. abs/2308.04014, 2023. 

- [48] D. P. Kingma and J. Ba, “Adam: A method for stochastic optimization,” in ICLR, 2015. 

310 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [49] I. Loshchilov and F. Hutter, “Decoupled weight decay regularization,” CoRR, vol. abs/1711.05101, 2019. 

- [50] E. J. Hu, Y. Shen, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang, L. Wang, and W. Chen, “Lora: Low-rank adaptation of large language models,” in ICLR. OpenReview.net, 2022. 

- [51] J. Davis and M. Goadrich, “The relationship between precision-recall and roc curves,” in Proceedings of the 23rd international conference on Machine learning, 2006, pp. 233–240. 

- [52] Q. Huang, A. Jansen, J. Lee, R. Ganti, J. Y. Li, and D. P. W. Ellis, “Mulan: A joint embedding of music audio and natural language,” in ISMIR, 2022, pp. 559– 566. 

311 

