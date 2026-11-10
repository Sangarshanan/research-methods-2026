---
paper_id: "000104"
year: 2022
title: "Download pdf"
source_url: "https://zenodo.org/record/7316800/files/000104.pdf"
---

# REPRESENTATION LEARNING FOR THE AUTOMATIC INDEXING OF SOUND EFFECTS LIBRARIES 

## Alison B. Ma 

Music Informatics Group 

Georgia Institute of Technology ama67@gatech.edu 

## Alexander Lerch 

Music Informatics Group 

Georgia Institute of Technology 

alexander.lerch@gatech.edu 

### ABSTRACT 

Labeling and maintaining a commercial sound effects library is a time-consuming task exacerbated by databases that continually grow in size and undergo taxonomy updates. Moreover, sound search and taxonomy creation are complicated by non-uniform metadata, an unrelenting problem even with the introduction of a new industry standard, the Universal Category System. To address these problems and overcome dataset-dependent limitations that inhibit the successful training of deep learning models, we pursue representation learning to train generalized embeddings that can be used for a wide variety of sound effects libraries and are a taxonomy-agnostic representation of sound. We show that a task-specific but dataset-independent representation can successfully address data issues such as class imbalance, inconsistent class labels, and insufficient dataset size, outperforming established representations such as OpenL3. Detailed experimental results show the impact of metric learning approaches and different cross-dataset training methods on representational effectiveness. 

### 1. INTRODUCTION 

Sound effects libraries are collections of prerecorded audio assets curated and meant for use by sound designers and editors. In application, a user will search for sounds necessary for their project by querying the library with a computer or other commercial tools for sound search, which helps organize sounds or allow for varying modes of querying the database [1±4]. Examples of typical classes include ambience, foley, and sci-fi. Libraries are often used in game audio and audio post-production applications because access to raw audio assets facilitates efficiency in the creative process, accommodates lacking resources for recording equipment, and alleviates barriers to inconvenient recording locations necessary for particular sounds. 

We identify two main problems with sound effects libraries in our work. First, interviews with dataset providers for this research revealed that too much time is spent labeling, re-labeling, and performing quality assurance on 

> © A.B. Ma and A. Lerch. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: A.B. Ma and A. Lerch, ªRepresentation Learning for the Automatic Indexing of Sound Effects Librariesº, in Proc. of the 23rd Int. Society for Music Information Retrieval Conf., Bengaluru, India, 2022. 

databases that continually grow in size and undergo taxonomy updates. One potential solution to this could be the application of machine learning and, more specifically, deep learning for automating sound classification. However, such machine learning models face several particular taskrelated challenges, such as (i) the size of available datasets can dramatically vary in terms of audio data and number of classes, (ii) data class distributions are often highly imbalanced, (iii) data labels are sometimes of poor quality or inconsistent, and (iv) training dedicated models on every existing sound effects library can be time-consuming. 

Second, non-uniform metadata in sound effects libraries complicate the successful sound search for a user and the creation of a useful taxonomy for a vendor. The recent introduction of the Universal Category System (UCS)<sup>1</sup> attempts to address this problem. UCS is an industry-proposed solution to standardize taxonomies designed by and for sound designers and editors. It is designed to be complete and sufficient for sound effects library categorization. However, adopting this standard has been slow; while several sound effects libraries have already converted to this new industry standard, others continue using their own proprietary taxonomies for convenience or preference. 

We address problems that arise when using a machine learning approach, training generalized embeddings that can represent any sound effects library and work on any taxonomy for sound classification. To build a powerful learned representation, we investigate two main methods for representation learning with a (i) metric-learning and (ii) cross-dataset training approach. 

Our work has the following main contributions: 

- the introduction of a powerful new representation for use in sound effects libraries trained on relevant, commercially available data, 

- the investigation of UCS’ generalizability (the industry’s first approach to unifying metadata), and 

- the presentation of extensive results emphasizing the positive impact of cross-dataset training, an underresearched aspect of representation learning. 

The remainder is structured as follows. In Sect. 6.2, we analyze if metric learning models will learn a betterstructured embedding space and produce higher classification results than a Cross-Entropy (CE) model. In Sect. 6.3, we see if a cross-dataset training scenario will outperform 

> 1 universalcategorysystem.com, last accessed May 10, 2022. 

866 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

all other training scenarios and discuss novel UCS-specific findings. In Sect. 6.4, we evaluate the impact of 3 different cross-dataset training methods. See Sect. 5.3.1 for data mixing methods, which explores accommodating for encoder bias with data training order, Sect. 5.3.2, which investigates accommodating for various dataset characteristics by ‘Focal’ dataset regularization, and Sect. 5.3.3, which experiments with using dataset-independent BatchNorm layers. We compare our best representations against OpenL3 Stateof-The-Art (SoTA) deep audio embeddings in Sect. 6.5. 

### 2. RELATED WORK 

We present an in-depth literature review regarding sound effects libraries and two aspects of representation learning. 

### 2.1 Sound Effects Libraries 

While there is a plethora of work on sound event classification, there is little work that conducts extensive research for a sound effects library application. Peeters and Reiss conducted sound effects classification by focusing on the discrimination between two classes, ambience and sound effects; audio features were manually selected [5]. Audio tagging work has been done on Freesound [6], the BBC sound effects library [7], and other online collaborative sound collections [8,9]. Some have designed features and taxonomies to improve sound classification. Moffat et al. tried to address the issue of a non-unified metadata labeling scheme with the Adobe Sound Effects Library.<sup>2</sup> They created a hierarchical taxonomy for sound effects based on the unsupervised learning of sonic attributes, using decision trees to assess audio and label semantic similarity [10]. Others that do not target a specific sound effects library application have experimented with psychoacoustic approaches to feature design using actions, material, and mood [3,11±14]. Meanwhile, the rest of the work regarding sound effects libraries does not focus on classification but explores sound search, query, and retrieval. Pearce et al. investigated user search queries on Freesound [15], reducing these descriptors into timbral features to aid sound search [16]. Lafay et al. and Zhang et al. researched methods to effectively query databases without keywords or by vocal imitation [2, 4]. Yang et al. recently presented a new system for indexing sound effects libraries, evaluating their work on users [1]. 

### 2.2 Representation Learning 

Representation learning aims to learn a highly discriminative embedding space that can generalize to various downstream tasks. Two examples of powerful deep audio embeddings are VGGish and OpenL3 [17±19], which have proven to be useful for many music information retrieval (MIR) and cross-modal tasks, e.g., classification, tagging, few-shot learning, and continual learning [20±23]. 

### 2.2.1 Metric Learning 

A popular method for representation learning is metric learning, where methods include the Contrastive, Triplet, and Cir- 

> 2 goo.gl/TzQgsB, last accessed May 10, 2022. 

cle loss. Contrastive loss minimizes the distance between similar classes’ feature vectors and maximizes the similarity between different classes’ feature vectors, training on pairs of positive or negative input samples [24±26]. Triplet loss optimizes both positive and negative inputs simultaneously and adds an additional anchor input in its loss computation [27±29]. Circle loss tries to improve upon the Triplet loss, featuring more flexible optimization, more definite convergence, and tries to unify the goals of a metric learning and classification loss into one [30]. Although metric learning losses can be used in a self-supervised [25,31±34] or un-supervised [24] manner, it is common to combine a metric learning loss with a classification loss to better fit a supervised learning problem. Khosla et al. have explored training methods to regularize and better structure the embedding space, introducing a Two-Step and Joint-Training method [26]. Furthermore, other works have explored the adoption of a contrastive approach to regression [35]. 

### 2.2.2 Cross-Dataset Training 

Furthermore, training on large amounts of diverse data is a crucial aspect of representation learning [17±19]. This can be addressed with cross-dataset training; we note many similarities between cross-dataset training and multi-task learning. Though there are scattered works amongst various fields in the deep learning literature that combine multiple different datasets for training, only a few papers have explored proposing methodologies for this. Namely, most work has only been explored in the computer vision domain; there is little work in audio. Working on symbolic music generation, Dong et al. found that stratified sampling mixing alleviated the source imbalance problems that come with combining datasets of various sizes; this worked better than simply concatenating datasets for training [36]. Ranftl et al. explored a multi-task learning setup with Pareto-optimal mixing and a multi-objective loss, evaluating success in a zero-shot scenario for a monocular depth estimation task. Their multi-task learning setup and mixing strategy, which ensures that decreasing the loss on one dataset necessitates increasing the loss on another, produced results superior to a naive mixing strategy where they trained on minibatches of equally sampled datasets. They found that this method was better at leveraging the act of adding more datasets for training [37]. Wan et al. introduced a MultiReader method for a speaker verification task to support training with datasets of different keywords and languages. They regularized the datasets to address insufficient and imbalanced dataset sizes but only experimented with two heterogeneous data sources. Moreover, they do not explicitly illustrate a method of reweighing datasets, resorting to hyperparameter tuning [38]. Lastly, Wang et al. introduced a Dataset-Aware Block, which uses dataset-invariant convolutional layers and dataset-specific BatchNorm layers. They concluded that preserving heterogenous dataset characteristics improves performance [39]. To the best of our knowledge, cross-dataset training has not been explored extensively in audio-related tasks. 

867 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
CNN_9layers_MaxPooling (Encoder) MLP Loss<br>timeSteps × freqBins CE<br>Cross-Entropy<br>Contrastive<br>Contrastive + Cross-Entropy<br>Triplet<br>Triplet + Cross-Entropy<br>Circle<br>Conv2D (kernel: 3, stride: 1) Circle + Cross-Entropy<br>ConvBlock MaxPool2D (kernel: 2)ReLU<br>Learned representation/embedding<br>dim = 64<br>dim = 128<br>dim = 256<br>dim = 512<br>Mel Spectrogram Mean (dim = 3) Max (dim = 2) Linear (1 × 256) Linear (1 × 128)<br>Linear (1 × numClasses)<br><!-- End of picture text -->

Figure 1. Network architecture: CNN9-max encoder, MLP classifier head, and loss functions. 

### 3. METHOD 

Our best pre-trained model is freely available online.<sup>3</sup> 



<!-- Start of picture text -->
i) PSE S9 3,600HPX P 1,816ROD iii)<br>7,815 3,964<br>SDLY CART<br>7,384 4,942<br>5,462UMIX 13,223STRM PSE: 78SDLY: 79UMIX: 69<br>S6 UCS CART<br>17,049 ii) 80 81<br>HPX<br>STRM 153<br>UCS Non-UCS 172 PROD<br>25<br>Alex Lane, All You Can Eat Audio, UMIX 116S9<br>Articulated Sounds, Audio Shade,<br>aXLSound,  Big  Sound  Bank,  S6<br>Bonson, BOOM Library, Frick & Traa,  631<br>InspectorJ, Kai Paquin, KEDR Audio,<br>Nikola Simikic, Penguin Grenade,<br>Thomas Rex Beverly, Tim Nielsen.<br><!-- End of picture text -->



Figure 2. Imbalanced UCS & Non-UCS dataset statistics, (i) Number of audio-files per training dataset, (ii) Number of classes per taxonomy, (iii) Class distribution sorted from most to least classes among training datasets. 

### 3.1 Model Architecture 

Our encoder architecture adapts the Convolutional Neural Network CNN9-max architecture from a DCASE 2019 baseline system for multi-class classification and is displayed in Fig. 1 [40]. We pre-train the encoder with one Multi-Layer Perceptron (MLP) classifier head per dataset. After training, we freeze the encoder and pass the representations to a simple Nearest Neighbor classifier to train and test the learned embedding space. Models were trained with Python, PyTorch, and the PyTorch metric learning library.<sup>4</sup> 

### 3.2 Input Representation 

All audio files were re-sampled to 44.1 kHz, down-mixed, and normalized. Mel-spectrograms were computed with a block size of 46 ms, hop size of 23 ms, 96 Mel-Bins, and span the audible frequency range [41]. We used min-max normalization for spectrograms and z-score standardization for extracted embeddings. Spectrogram input dimensions to the network are (100, 96) and span approximately 2 s of audio. This length was determined in pilot experiments. 

### 3.3 Training Procedure 

We trained all models with a batch size of 64, the Adam optimizer, and early stopping. Model checkpoints used for inference correspond to the best validation loss. For crossdataset training, we save the best average validation loss from all datasets. Hyper-parameters for pre-training were found via 20 trials of random search. During pre-training, 2 s frames of audio files are randomly sampled whenever a batch is retrieved. We re-shuffle the dataset per epoch. We compute embeddings with 50% overlap at inference time. 

### 3.4 Evaluation Metrics 

The macro F-1 score over classes in a dataset is our predominant metric for evaluating classification performance, as all datasets have imbalanced class distributions. We also monitor the Davies-Bouldin Index (DBI) to evaluate the quality of the embedding space structure, i.e., clustering. 

> 3 github.com/alisonbma/aiSFX, last accessed August 11, 2022. 

> 4 kevinmusgrave.github.io/pytorch-metric-learning, last accessed May 10, 2022. 

The DBI measures the average similarity between a cluster and its most similar cluster. 

### 4. DATASETS & TAXONOMIES 

We address our goal of training generalized embeddings by training and testing with 9 datasets and 7 taxonomies. We emphasize that we use a diverse assortment of datasets for this research and present corresponding data statistics in Fig. 2. We use 3 UCS-compliant datasets: Pro Sound Effects (PSE), Soundly (SDLY), UCS Mixed (UMIX), and 6 Non-UCS datasets from the Sound Ideas library: Cartoon Express (CART), HPX Digital (HPX), Production Elements (PROD), Series 6000 (S6), Series 9000 (S9), Soundstorm (STRM). For UCS-compliant datasets, we use UCSv8.1 Category labels as ground truth. 

Preliminary experiments with UCS lead us to use experimental subsets of 150 or fewer datapoints per class. We pre-train and evaluate embeddings on the full imbalanced subsets (65k audio files) except in Cross-Dataset training scenarios, where we use class-balanced versions for NonUCS data. A stratified train validation test split of 8:1:1 was conducted. For UCS-compliant datasets, the fine CatID labels determined stratification. 

We select PSE as the base dataset for UCS-Transfer experiments because of its larger number of datapoints and classes, cleaner labels compared to Non-UCS datasets, better generalization when evaluated against other UCS datasets, and more even distribution among both levels of the UCS 2-level class hierarchy. 

### 5. EXPERIMENTAL SETUP 

We list our research questions and hypotheses below using the following experimental variables: 

- Metric learning loss functions (Fig. 1, Sect. 5.1), 

- Variable training scenarios (Sect. 5.2), and 

- Cross-dataset training methods (Sect. 5.3). 

### 5.1 RQ1: Impact of Metric Learning 

We first ask whether metric learning loss functions that learn distances instead of absolute class labels will improve 

868 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

classification results. We hypothesize that metric learning approaches will learn a more discriminative embedding space compared to CE models and that this better-structured embedding space will improve classification results. 

(i) Data mixing (X-Sequential, X-Joint), (ii) ‘Focal’ dataset regularization (FDR), and (iii) Dataset-independent BatchNorm layers (BN). 

### 5.3.1 Data Mixing 

### 5.1.1 Training Parameterization 

We train all metric learning models with Khosla’s JointTraining scheme that optimizes a hybrid sum of a metric learning loss function and Cross-Entropy loss as it has been shown to be more effective than a Two-Step training method [26,33,35,42,43]. Fig. 1 illustrates our experiments with the joint metric learning losses (i) Contrastive, (ii) Triplet, and (iii) Circle. 

The metric learning losses optimize cosine similarity. Positive and negative samples are computed from all possible pairs or triplets between samples in a batch. Accordingly, we find that our batch size is sufficient for training from initial experiments. Model training utilized online mining and the regularface embedding regularizer [44]. 

In addition to re-shuffling the dataset per epoch and randomly selecting 2 s frames, we re-sample the dataset so that it randomly selects new datapoints per class per epoch. Here, we equally sample 4 datapoints per class so that a single batch includes 16 different classes; we found minimal difference from weighted sampling. 

### 5.2 RQ2: Impact of Cross-Dataset Training 

Secondly, we ask whether cross-dataset training will improve our best Cross-Entropy and metric learning results in all training scenarios. We hypothesize that a Cross-Dataset training scenario will outperform all others, including UCSTransfer (see definition below), improving upon both UCS & Non-UCS dataset results. Our rationale is that representations generated from Cross-Dataset models will have seen a more significant quantity and variety of data from different sound taxonomies, producing more generalized representations. Moreover, we hypothesize that UCS-Transfer will yield decent classification results as UCS is a standardized taxonomy for sound effects libraries. We denote CrossDataset models with the prefix, X. 

### 5.2.1 Training Scenario Definitions 

We conduct experiments with 3 training scenarios: (i) Within-Dataset training: Pre-train and evaluate the encoder on the same dataset, (ii) UCS-Transfer: Pre-train the encoder on a UCS-compliant dataset and evaluate on other datasets in a transfer learning scenario, and (iii) CrossDataset training: Pre-train the encoder on all datasets and taxonomies, evaluate the encoder on any dataset. 

### 5.3 RQ3: Impact of Cross-Dataset Training Methods 

Datasets used for training may have varying characteristics. For example, they may use taxonomies of dissimilar scopes and biases and have different dataset sizes, all of which an effective classifier must adapt to. Our final question is whether training scenarios accommodating dataset characteristics will improve classification results. We experiment with 3 methods as introduced in the following subsections, 

We use two variations of data mixing. Sequential trains on all datapoints from a single dataset before training on the next, i.e., concatenate datasets, while Joint trains on datapoints from all datasets in mixed order, similar to stratified sampling in the literature [36]. We limit mixing for Joint so that all datapoints in a batch must correspond to the same dataset. We affirm that backpropagation is called per batch. 

### 5.3.2 ‘Focal’ Dataset Regularization 

We regularize the datasets by ‘difficulty’ and reweigh them by a dataset’s training convergence speed in epochs. Inspired by Focal Loss [38,45,46] and mining for hard pairs or triplets in metric learning [29,47±49], easier datasets are down-weighted so that training focuses on difficult datasets. 



<!-- Start of picture text -->
αd = 1 − β ne (1)<br>1 − β<br><!-- End of picture text -->

We modify the reweighting function shown in Eqn. 1 to re-balance the datasets and initialize these weights with ne, the epoch at which a dataset’s training set macro F-1 score crosses a threshold of 90% [50]. These weights may be adjusted with hyperparameter β to reduce or heighten the difference between dataset weights. ad is the unnormalized reweighing factor per dataset, d. As previously done in the literature, we normalize αd so that<sup>�D</sup> d=1<sup>αd= D, keeping</sup> the loss in roughly the same range. D represents the total number of datasets used for pre-training [45,50]. 

### 5.3.3 Dataset-Independent BatchNorm Layers 

Similar to selecting the correct classifier head per dataset when pre-training the encoder, we select a dataset’s corresponding BatchNorm layers. This is equivalent to turning each ConvBlock in Fig. 1 into a Dataset-Aware Block [39]. 

### 5.4 RQ4: Comparison to SoTA 

We select OpenL3 features as our reference to SoTA deep audio embeddings because L<sup>3</sup> -Net is said to ªconsistently outperform VGGish and SoundNet on environmental sound classificationº [18]. We use the default OpenL3 parameters as they yield the highest frame-level classification results and select the Music content type embeddings for comparison (6144 dimensionality, 0.1 s hop size, and 256 Mel Bins) [18]. We aggregate these features to represent 2 s of an audio file for consistency with our input representation. 

### 6. RESULTS 

All results are computed at the frame-level, i.e., aggregated over each 2 s frame extracted from audio files in the holdout test set. Boxplot datapoints indicate results for a single dataset. Metric learning plots, Fig. 4 and 5, only show X- Sequential results for the Cross-Dataset training scenario. 

869 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
UCSUCS Non-UCSNon-UCS<br>PSEPSE SDLYSDLY UMIXUMIX CARTCART HPXHPX PRODPROD S6S6 S9S9 STRMSTRM<br>1.001.0 0 Encoder Label, MEncoder 2, FrameCE (Baseline) 0.950.95 0.91<br>0.90 0.91<br>0.9 0<br>0.80<br>0.700.8 0 0.67<br>0.600.7 0 0.53 0.67 0.51 0.53 0.55 0.59<br>0.500.400.300.60.5 00 0.43 0.53 0.51 0.53 0.55 0.59<br>0.20 0.43<br>0.4 0<br>0.10<br>0.3 0<br>Macro F-1Macro F-1<br><!-- End of picture text -->

Figure 3. Baseline macro F-1 score classification results using Cross-Entropy loss, CE (Within-Dataset). 

### 6.1 Baseline Results 

Fig. 3 displays baseline classification results where each model is trained and tested on only one dataset, itself. Plots for the following experiments only show the change from this baseline plot. 

### 6.2 RQ1: Impact of Metric Learning 

Fig. 4 shows how metric learning models improve upon the baseline’s embedding space structure to different degrees. A lower DBI indicates a better embedding space structure. Contrastive improves the space for most datasets in all training scenarios. Triplet results in a slightly higher average DBI in all but the UCS-Transfer training scenario. Circle performs significantly better in a Within-Dataset training scenario with an average DBI decrease of 0.43. However, it performs surprisingly poorly in UCS-Transfer & CrossDataset, suggesting that it is not ideal for generalization, a prime motivator of representation learning. 

Contrary to our hypothesis, a better-structured embedding space (lower DBI) does not always improve classification results (higher macro F-1), shown in Fig. 5. We only see that metric learning models improve classification results in the UCS-Transfer training scenario. We specifically note that Circle significantly improves the embedding space structure compared to Contrastive in Within-Dataset. However, both embedding spaces still yield similar classification performance, an average of -1.75% and -1.50% from CE, respectively. We note other work by Lee et al. regarding the similarities between metric learning and classification [51]. Focusing on classification results, we identify Triplet 



<!-- Start of picture text -->
Contrastive Triplet Circle<br>0.7<br>0.5<br>0.3<br>0.1<br>-0.1<br>-0.3<br>-0.5<br>-0.7<br>Training Scenario<br>-0.9 WithinWithin-Dataset<br>-1.1 UCS-TUCS-Transfer<br>CrossCross-Dataset<br>Within UCS-T Cross Within UCS-T Cross Within UCS-T Cross<br>DBI Change<br>n T q n T q n T q<br><!-- End of picture text -->

Figure 4. DBI change of metric learning models relative to CE in different training scenarios. 

as our ‘best’ metric learning loss with a slightly higher average performance than Contrastive. Triplet performs on par with CE in Within-Dataset and Cross-Dataset (less than 1% difference on average), and has an average of 4.25% improvement from CE in UCS-Transfer. Therefore, Contrastive and Circle loss results will be omitted in the following sections. 

### 6.3 RQ2: Impact of Cross-Dataset Training 

Results for cross-dataset training are shown in Fig. 6. Matching our hypothesis, we find that for CE models, CrossDataset outperforms Within-Dataset models for the majority of datasets by approximately 4-5%. We find that Triplet models also tend to improve by 1-3% except for X-Joint-BN + Triplet. This confirms that cross-dataset training indeed leads to better generalization across all sound taxonomies. 

### 6.3.1 UCS Insights 

We preface this section with preliminary results on UCS. We find that the UCS-compliant datasets in this study use the standardized UCS taxonomy in a non-uniform way. Without fine-tuning another classifier head, one cannot use a UCS taxonomy-trained model on other UCS-compliant datasets. This corroborates the need for generalized representations that can adapt to any taxonomy of sound. 

With this said, Fig. 6 also shows that UCS-Transfer can achieve results considerably better than random. Although it under-performs Within-Dataset training by an average of 7.48% with CE models, we find that there is only an average of -1.62% difference from CE with Triplet models. Alongside, we also verify that other UCS-compliant libraries, SDLY and UMIX, can be used as base sets to achieve decent generalization in a transfer learning scenario. 

We note some dataset-specific details for UCS-Transfer + Triplet compared to our best Cross-Dataset Triplet model, X-Joint + Triplet. Both perform similarly (around 1% worse) on Non-UCS CART, HPX, PROD, and STRM datasets. UCS-Transfer performs around 5-6% worse on UCS-compliant SDLY and UMIX, a substantial improvement from previous results that did not re-train a classifier head. Lastly, it performs around 7% worse on Non-UCS S6, likely because S6 exhibits the highest number of classes amongst all datasets while PSE only has 78 classes. 



<!-- Start of picture text -->
ContrastiveContrastive TripletTriplet CircleCircle<br>0.100.1 0<br>0.060.0 6<br>0.020.0 2<br>-0.02-0.0 2<br>-0.06-0.0 6<br>-0.10-0.1 0<br>-0.14-0.1 4<br>-0.18-0.1 8 Training ScenarioWithinWithin-Dataset<br>-0.22-0.2 2 UCS-TUCS-Transfer<br>CrossCross-Dataset<br>Within UCS-T Cross Within UCS-T Cross Within UCS-T Cross<br>Macro F-1 ImprovementMacro F-1 Improvement<br><!-- End of picture text -->

Figure 5. Macro F-1 score improvement of metric learning models relative to CE in different training scenarios. 

870 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



<!-- Start of picture text -->
CE Triplet<br>0.22 Training ScenarioUCS-TUCS - Transfer<br>0.18 CrossCross-Dataset (X-)<br>0.14<br>0.10<br>0.06<br>0.02<br>-0.02<br>-0.06<br>-0.10<br>-0.14<br>-0.18<br>UCS-TX-Sequential X-Joint X-Joint-FDR X-Joint-BN UCS-TX-Sequential X-Joint X-Joint-FDR X-Joint-BN<br>Macro F-1 Improvement<br><!-- End of picture text -->

Figure 6. Macro F-1 score improvement of various training scenarios from Within-Dataset. 

### 6.4 RQ3: Impact of Cross-Dataset Training Methods 

We experiment to see if accommodating different dataset characteristics with 3 cross-dataset training methods will further improve results. We compare all cross-dataset training methods to X-Sequential in our discussion. 

First, sensitivity to encoder bias and training order does not severely impact results for our task. Data mixing results note an average 1% difference between X-Sequential and X-Joint in CE and Triplet. 

Second, reweighing datasets as proposed in Sect. 5.3.2 does not lead to observable consistent trends. We show results that use β = 0.999. Looking at difficult datasets, the performance of SDLY worsens by 2.96%, while STRM improves by 3.27% despite having similar convergence speeds and being the second-ranked most ‘difficult’ datasets. We also observe an unfortunate worsening of results for faster-converging datasets, i.e., HPX decreases by 1.77% (Triplet), S9 decreases by 2.32% (CE) and 6.20% (Triplet). 

Third, we verify that independent BatchNorm layers do preserve dataset-specific characteristics. Unlike other work in the literature [39], we find that this may not always be beneficial as it may exacerbate dataset-specific problems. Shown in Fig. 6, we specifically note decreases in performance for Non-UCS HPX, PROD, S6, and S9, which we attribute to messier inconsistent labels and insufficient training data, apparent in Fig. 2. This decrease can be quite dramatic with S9 dropping by 7.53% (CE) and 24.4% (Triplet). Alongside, we find that UCS-compliant PSE and SDLY, as well as Non-UCS STRM experience a 2-3% increase in performance, which we attribute to both the cleaner UCS taxonomy and datasets having sufficient training data. 

### 6.5 RQ4: Comparison to SoTA 

Overall, our work reveals that our best model is X- Sequential + CE. We compare X-Sequential + CE and OpenL3 in Fig. 7 and provide a commonly used benchmark dataset, ESC-50 [52], to extend the assessment of our work in a non-task-specific audio application. Unlike the rest of our datasets, we show the 5-fold cross-validation results for ESC-50 as commonly reported in the literature. Ultimately, we observe that our best model outperforms OpenL3 on all datasets. In addition, we note that our model requires fewer resources to achieve its results. While both models have 



<!-- Start of picture text -->
UCS Non-UCS Other<br>PSE SDLY UMIX CART HPX PROD S6 S9 STRM ESC-50<br>1.00 Encoder Label, Metric Enc Encoder En coderoder Label, Metric2, Frame 2,  X-Sequential + CE (Ours)OpenLCross-Joint-CE (Ours)GlobalFrame 3 0.95 0.93<br>0.90<br>0.80 0.77<br>0.70<br>0.70<br>0.60 0.56 0.58 0.94 0.92 0.55 0.58 0.58<br>0.50<br>0.50 0.66<br>0.40 0.51 0.52 0.47 0.52 0.60 0.56 0.53<br>0.30<br>Macro F-1<br><!-- End of picture text -->

Figure 7. Our best model compared to OpenL3 audio embeddings. Blue bars illustrate the amount in which we outperform OpenL3. 

a similar number of parameters (4.7M), our best model is trained on approximately 7x less data (39k audio-files vs. 296k videos) [18]. 

### 7. CONCLUSION 

We introduce a new pre-trained representation for automatic sound effects library classification. Our task-specific representation outperforms OpenL3 on both UCS & NonUCS taxonomies across diverse datasets. Moreover, we show the effectiveness of cross-dataset training with CrossEntropy loss over metric learning for this task. Results suggest that the quality and diversity of datasets are key to pre-training robust representations, supportive of preliminary experimental results where pre-training on increasing quantities of similar data yielded improvements with diminishing returns. Our contributions include that we are the first to conduct extensive deep learning experiments on UCS, experiment on relevant data for a current problem, and investigate an under-researched aspect of representation learning with cross-dataset training in the audio domain. 

We believe cross-dataset training is a prerequisite for future work. Our current research does not leverage all datasets available to us nor the abundance of taxonomies they are comprised of given that many datasets did not have sufficient labels for training. To leverage these resources, methods to effectively work with large amounts of diverse data become increasingly essential. Selecting optimal cross-dataset training methods is fundamental before introducing new techniques, such as semi-supervised or self-supervised learning to work with datasets of varying label quality [53,54]. Accordingly, we would like to (i) look into the connection between multi-task learning and crossdataset training to understand the specific advantages and drawbacks of these approaches and (ii) conduct experiments to assess the impact of increasing the amount of training data, observing the relationship of this with more complex network architectures and other pre-training methods [55]. Finally, we hope to deepen our understanding of UCS by investigating the non-uniformity of class labels between UCS-compliant datasets in this study, looking at the interpretability and disentanglement of our representations [51], and exploring the concept of a generalized embedding from the perspective of taxonomy conversion [56]. 

871 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

### 8. REFERENCES 

- [1] J. Yang, Y. Zhang, and Y. Hai, ªRetrieval and management system for layer sound effect library,º Cognitive Computation and Systems, vol. 2, no. 4, pp. 247±253, 2020. 

- [2] G. Lafay, N. Misdariis, M. Lagrange, and M. Rossignol, ªSemantic browsing of sound databases without keywords,º Journal of the Audio Engineering Society, September 2016. 

- [3] S. Säger, B. Elizalde, D. Borth, C. Schulze, B. Raj, and I. Lane, ªAudiopairbank: towards a large-scale tag-pairbased audio content analysis,º EURASIP Journal on Audio, Speech, and Music Processing, p. 12, 2018. 

- [4] Y. Zhang, J. Hu, Y. Zhang, B. Pardo, and Z. Duan, ªVroom!: A search engine for sounds by vocal imitation queries,º in Proceedings of the 2020 Conference on Human Information Interaction and Retrieval (CHIIR). Association for Computing Machinery, 2020, pp. 23± 32. 

- [5] G. G. Peeters and J. D. Reiss, ªA deep learning approach to sound classification for film audio post-production,º Journal of the Audio Engineering Society, May 2020. 

- [6] E. Fonseca, M. Plakal, F. Font, D. P. W. Ellis, X. Favory, J. Pons, and X. Serra, ªGeneral-purpose tagging of freesound audio with audioset labels: Task description, dataset, and baseline,º arXiv preprint arXiv:1807.09902, 2018. 

- [7] D. Turnbull, L. Barrington, D. Torres, and G. Lanckriet, ªSemantic annotation and retrieval of music and sound effects,º IEEE Transactions on Audio, Speech, and Language Processing, vol. 16, no. 2, pp. 467±476, 2008. 

- [8] X. Favory, F. Font, and X. Serra, ªSearch result clustering in collaborative sound collections,º in Proceedings of the 2020 International Conference on Multimedia Retrieval (ICMR ’20), 2020, pp. 207±214. 

- [9] F. Font, G. Roma, and X. Serra, Sound Sharing and Retrieval. Cham: Springer International Publishing, 2018, pp. 279±301. 

- [10] D. Moffat, D. Ronan, and J. D. Reiss, ªUnsupervised taxonomy of sound effects,º in Proceedings of the 20th International Conference on Digital Audio Effects (DAFx), 2017. 

- [11] G. Lemaitre and L. M. Heller, ªEvidence for a basic level in a taxonomy of everyday action sounds,º Experimental Brain Research, vol. 226, no. 2, pp. 253±264, 2013. 

- [12] O. Bones, T. J. Cox, and W. J. Davies, ªSound categories: Category formation and evidence-based taxonomies,º Frontiers in Psychology, vol. 9, pp. 1664± 1078, 2018. 

- [13] B. Elizalde, R. Revutchi, S. Das, B. Raj, I. Lane, and L. M. Heller, ªIdentifying actions for sound event classification,º in 2021 IEEE Workshop on Applications of Signal Processing to Audio and Acoustics (WASPAA), 2021, pp. 26±30. 

- [14] B. M. Elizalde, ªNever-ending learning of sounds,º Ph.D. dissertation, Carnegie Mellon University, 2020. 

- [15] F. Font, G. Roma, and X. Serra, ªFreesound technical demo,º in Proceedings of the 21st ACM International Conference on Multimedia (MM). Association for Computing Machinery, 2013, pp. 411±412. 

- [16] A. Pearce, T. Brookes, and R. Mason, ªTimbral attributes for sound effect library searching,º Journal of the Audio Engineering Society, June 2017. 

- [17] S. Hershey, S. Chaudhuri, D. P. W. Ellis, J. F. Gemmeke, A. Jansen, R. C. Moore, M. Plakal, D. Platt, R. A. Saurous, B. Seybold, M. Slaney, R. J. Weiss, and K. Wilson, ªCnn architectures for large-scale audio classification,º in Proceedings of the IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP), 2017, pp. 131±135. 

- [18] J. Cramer, H.-H. Wu, J. Salamon, and J. P. Bello, ªLook, listen, and learn more: Design choices for deep audio embeddings,º in Proceedings of the IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP), 2019, pp. 3852±3856. 

- [19] R. Arandjelovic and A. Zisserman, ªLook, listen and learn,º in Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 2017, pp. 609± 617. 

- [20] Y. Wang, N. J. Bryan, M. Cartwright, J. P. Bello, and J. Salamon, ªFew-shot continual learning for audio classification,º in Proceedings of the IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP), 2021, pp. 321±325. 

- [21] Y. Wang, N. Bryan, J. Salamon, M. Cartwright, and J. Bello, ªWho calls the shots? rethinking few-shot learning for audio,º in 2021 IEEE Workshop on Applications of Signal Processing to Audio and Acoustics (WASPAA), 2021, pp. 36±40. 

- [22] S. Gidaris and N. Komodakis, ªDynamic few-shot visual learning without forgetting,º in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2018, pp. 4367±4375. 

- [23] H. F. Garcia, A. Aguilar, E. Manilow, and B. Pardo, ªLeveraging hierarchical structures for few-shot musical instrument recognition,º in Proceedings of the 22nd International Society for Music Information Retrieval Conference (ISMIR), 2021, pp. 220±228. 

- [24] E. Fonseca, D. Ortego, K. McGuinness, N. E. O’Connor, and X. Serra, ªUnsupervised contrastive learning of sound event representations,º in Proceedings of the 

872 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

   - IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP), 2021, pp. 371±375. 

- [25] J. Spijkervet and J. A. Burgoyne, ªContrastive learning of musical representations,º in Proceedings of the 22nd International Society for Music Information Retrieval Conference (ISMIR), 2021, pp. 673±681. 

- [26] P. Khosla, P. Teterwak, C. Wang, A. Sarna, Y. Tian, P. Isola, A. Maschinot, C. Liu, and D. Krishnan, ªSupervised contrastive learning,º in Advances in Neural Information Processing Systems (NeurIPS), H. Larochelle, M. Ranzato, R. Hadsell, M. F. Balcan, and H. Lin, Eds., vol. 33. Curran Associates, Inc., 2020, pp. 18 661± 18 673. 

- [27] E. Hoffer and N. Ailon, ªDeep metric learning using triplet network,º in International Workshop on Similarity-Based Pattern Recognition. Springer International Publishing, 2015, pp. 84±92. 

- [28] K. Q. Weinberger, J. Blitzer, and L. Saul, ªDistance metric learning for large margin nearest neighbor classification,º in Advances in Neural Information Processing Systems (NeurIPS), Y. Weiss, B. Schölkopf, and J. Platt, Eds., vol. 18. MIT Press, 2005. 

- [29] A. Hermans, L. Beyer, and B. Leibe, ªIn defense of the triplet loss for person re-identification,º arXiv preprint arXiv:1703.07737, 2017. 

- [30] Y. Sun, C. Cheng, Y. Zhang, C. Zhang, L. Zheng, Z. Wang, and Y. Wei, ªCircle loss: A unified perspective of pair similarity optimization,º in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2020, pp. 6398±6407. 

- [31] R. Zhang, H. Wu, W. Li, D. Jiang, W. Zou, and X. Li, ªTransformer based unsupervised pre-training for acoustic representation learning,º in Proceedings of the IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP), 2021, pp. 6933±6937. 

- [32] A. Saeed, D. Grangier, and N. Zeghidour, ªContrastive learning of general-purpose audio representations,º in Proceedings of the IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP), 2021, pp. 3875±3879. 

- [33] D. Niizumi, D. Takeuchi, Y. Ohishi, N. Harada, and K. Kashino, ªByol for audio: Exploring pre-trained general-purpose audio representations,º arXiv preprint arXiv:2204.07402, 2022. 

- [34] L. Wang, P. Luc, Y. Wu, A. Recasens, L. Smaira, A. Brock, A. Jaegle, J. Alayrac, S. Dieleman, J. Carreira, and A. van den Oord, ªTowards learning universal audio representations,º in Proceedings of the IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP), 2022, pp. 4593±4597. 

- [35] P. Seshadri and A. Lerch, ªImproving music performance assessment with contrastive learning,º in Proceedings of the 22nd International Society for Music Information Retrieval Conference (ISMIR), 2021, pp. 634±641. 

- [36] H.-W. Dong, K. Chen, J. McAuley, and T. BergKirkpatrick, ªMuspy: A toolkit for symbolic music generation,º in Proceedings of the 21st International Society for Music Information Retrieval Conference (ISMIR), 2020, pp. 101±108. 

- [37] R. Ranftl, K. Lasinger, D. Hafner, K. Schindler, and V. Koltun, ªTowards robust monocular depth estimation: Mixing datasets for zero-shot cross-dataset transfer,º IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 44, no. 3, pp. 1623±1637, 2022. 

- [38] L. Wan, Q. Wang, A. Papir, and I. L. Moreno, ªGeneralized end-to-end loss for speaker verification,º in Proceedings of the IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP), 2018, pp. 4879±4883. 

- [39] L. Wang, D. Li, Y. Zhu, L. Tian, and Y. Shan, ªCross-dataset collaborative learning for semantic segmentation in autonomous driving,º arXiv preprint arXiv:2103.11351, 2021. 

- [40] Q. Kong, Y. Cao, T. Iqbal, Y. Xu, W. Wang, and M. D. Plumbley, ªCross-task learning for audio tagging, sound event detection and spatial localization: DCASE 2019 baseline systems,º arXiv preprint arXiv:1904.03476, 2019. 

- [41] D. Bogdanov, N. Wack, E. Gómez, S. Gulati, P. Herrera, O. Mayor, G. Roma, J. Salamon, J. Zapata, and X. Serra, ªEssentia: an audio analysis library for music information retrieval,º in Proceedings of the 14th International Society for Music Information Retrieval Conference (ISMIR), 2013, pp. 493±498. 

- [42] P. Khosla, P. Teterwak, C. Wang, A. Sarna, Y. Tian, P. Isola, A. Maschinot, C. Liu, and D. Krishnan, ªSupervised contrastive learning,º in Advances in Neural Information Processing Systems (NeurIPS), H. Larochelle, M. Ranzato, R. Hadsell, M. F. Balcan, and H. Lin, Eds., vol. 33. Curran Associates, Inc., 2020, pp. 18 661± 18 673. 

- [43] J. Fan, E. Nichols, D. Tompkins, A. E. M. Méndez, B. Elizalde, and P. Pasquier, ªMulti-label sound event retrieval using a deep learning-based siamese structure with a pairwise presence matrix,º in Proceedings of the IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP), 2020, pp. 3482±3486. 

- [44] K. Zhao, J. Xu, and M.-M. Cheng, ªRegularface: Deep face recognition via exclusive regularization,º in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2019, pp. 1136± 1144. 

873 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

- [45] T.-Y. Lin, P. Goyal, R. Girshick, K. He, and P. Dollár, ªFocal loss for dense object detection,º in Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 2017, pp. 2999±3007. 

- [46] K. Nada, K. Imoto, R. Iwamae, and T. Tsuchiya, ªMultitask learning of acoustic scenes and events using dynamic weight adaptation based on multi-focal loss,º in Proceedings of the 13th Asia-Pacific Signal and Information Processing Association Annual Summit and Conference (APSIPA ASC). IEEE, 2021, pp. 1156±1160. 

- [47] C.-Y. Wu, R. Manmatha, A. J. Smola, and P. Krahenbuhl, ªSampling matters in deep embedding learning,º in Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 2017, pp. 2840±2848. 

- [48] H. Xuan, A. Stylianou, and R. Pless, ªImproved embeddings with easy positive triplet mining,º in Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (WACV), 2020, pp. 2474±2482. 

- [49] X. Wang, X. Han, W. Huang, D. Dong, and M. R. Scott, ªMulti-similarity loss with general pair weighting for deep metric learning,º in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2019, pp. 5022±5030. 

- [50] Y. Cui, M. Jia, T.-Y. Lin, Y. Song, and S. Belongie, ªClass-balanced loss based on effective number of samples,º in Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2019, pp. 9260±9269. 

- [51] J. Lee, N. Bryan, J. Salamon, Z. Jin, and J. Nam, ªMetric learning vs classification for disentangled music representation learning,º in Proceedings of the 21st International Society for Music Information Retrieval Conference (ISMIR), 2020, pp. 439±445. 

- [52] K. J. Piczak, ªEsc: Dataset for environmental sound classification,º in Proceedings of the 23rd ACM International Conference on Multimedia (MM). New York, NY, USA: Association for Computing Machinery, 2015, pp. 1015±1018. 

- [53] K. Sohn, D. Berthelot, N. Carlini, Z. Zhang, H. Zhang, C. A. Raffel, E. D. Cubuk, A. Kurakin, and C.-L. Li, ªFixmatch: Simplifying semi-supervised learning with consistency and confidence,º in Advances in Neural Information Processing Systems (NeurIPS), vol. 33, 2020, pp. 596±608. 

- [54] S. Gururani and A. Lerch, ªSemi-supervised audio classification with partially labeled data,º in 2021 IEEE International Symposium on Multimedia (ISM), 2021, pp. 111±114. 

- [55] T. Chen, Y. Xie, S. Zhang, S. Huang, H. Zhou, and J. Li, ªLearning music sequence representation from text supervision,º in Proceedings of the IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP), 2022, pp. 4583±4587. 

- [56] L. Xue, N. Constant, A. Roberts, M. Kale, R. Al-Rfou, A. Siddhant, A. Barua, and C. Raffel, ªmT5: A massively multilingual pre-trained text-to-text transformer,º in 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL). "Association for Computational Linguistics", 2021, pp. 483±498. 

### 9. ACKNOWLEDGMENTS 

We would like to thank those who provided the data required to conduct this research as well as those who took the time to share their insights and software licenses for tools regarding sound search, query, and retrieval. 

Alex Lane<sup>5</sup> 

All You Can Eat Audio<sup>6</sup> 7 Articulated Sounds<sup>8</sup> 

Audio Shade<sup>9</sup> 10 aXLSound<sup>11</sup> Big Sound Bank<sup>12</sup> BaseHead<sup>13</sup> Bonson<sup>14</sup> 15 BOOM Library<sup>16</sup> 

Frick & Traa<sup>17</sup> 

> 5 Alex Lane, Resonant Rusty Door. [Dataset]. Available: https://www.alex-lane.com. [Accessed: September 15, 2021]. 

> 6 All You Can Eat Audio, It’s A Plain Phone. [Dataset]. Available: https://allyoucaneataudio.com/library-packs/it-is-a-plain-phone-p04. [Accessed: September 15, 2021]. 

> 7 All You Can Eat Audio, Cuff ’Em. [Dataset]. Available: https://allyoucaneataudio.com/library-packs/cuff-em. [Accessed: September 15, 2021]. 

> 8 Articulated Sounds, Starter Pack. [Dataset] Available: https://articulatedsounds.com/audio-royalty-free-library/sfx/freeglobal-sample-pack. [Accessed: September 15, 2021]. 

> 9 Audio Shade, Bravo Dramatic Audiences. [Dataset]. Available: https://audioshade.com/shop. [Accessed: September 15, 2021]. 

> 10 Audio Shade, Brutality - Gore and Combat FX Toolkit. [Dataset]. Available: https://audioshade.com/shop. [Accessed: September 15, 2021]. 

> 11 aXLSound, Planes - Takeoffs & Landings. [Dataset]. Available: https://axlsound.com. [Accessed: September 15, 2021]. 

> 12 Big Sound Bank, Big Sound Bank. [Dataset]. Available: https://bigsoundbank.com. [Accessed: September 15, 2021]. 

13 baseheadinc.com, last accessed September 15, 2021. 

> 14 Bonson, Wings. [Dataset]. Available: https://www.bonson.ca/product/wings. [Accessed: September 15, 2021]. 

> 15 Bonson, Moves. [Dataset]. Available: https://www.bonson.ca/product/moves. [Accessed: September 15, 2021]. 

> 16 BOOM Library, Cyber Weapons. [Dataset]. Available: https://www.boomlibrary.com/sound-effects/cyber-weapons. [Accessed: September 15, 2021]. 

> 17 Frick & Traa, City Bicycles. [Dataset]. Available: https://www.frickandtraa.com/webshop/sound-libraries. [Accessed: September 15, 2021]. 

874 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

Hzandbits<sup>18</sup> InspectorJ<sup>19</sup> Kai Paquin<sup>20</sup> KEDR Audio<sup>21</sup> 22 23 24 25 Krotos Audio<sup>26</sup> 27 Nikola Simikic<sup>28</sup> Penguin Grenade<sup>29</sup> 30 31 Pro Sound Effects<sup>32</sup> Rick Allen Creative<sup>33</sup> Sononym<sup>34</sup> Sound Ideas<sup>35</sup> Soundly<sup>36</sup> Soundminer<sup>37</sup> Storyblocks<sup>38</sup> Tim Nielsen<sup>39</sup> 40 41 42 

Thomas Rex Beverly<sup>43</sup> 44 ZapSplat<sup>45</sup> 

18 C. Hagelskjaer, "Interview with Christian Hagelskjaer," July 28, 2021. 19 InspectorJ, 96 General Library. [Dataset]. Available: https://inspectorj.sellfy.store/p/96-general-library-bundle. [Accessed: September 15, 2021]. 20 K. Paquin, Kailibrary. [Dataset]. 21 KEDR Audio, Cinemaphone. [Dataset]. Available: https://www.asoundeffect.com/sound-library/cinemaphone-ringtonesnotifications. [Accessed: September 15, 2021]. 22 KEDR Audio, Kinetics: Construction Kit. [Dataset]. Available: https://www.asoundeffect.com/sound-library/kinetics-constructionkit. [Accessed: September 15, 2021]. 23 KEDR Audio, Kinetics: Cinematic Tension. [Dataset]. Available: https://www.asoundeffect.com/sound-library/kinetics-cinematictension. [Accessed: September 15, 2021]. 24 KEDR Audio, Radio Nomad. [Dataset]. Available: https://www.asoundeffect.com/sound-library/radio-nomad. [Accessed: September 15, 2021]. 25 KEDR Audio, Vibrations. [Dataset]. Available: https://www.asoundeffect.com/sound-library/vibrations. [Accessed: September 15, 2021]. 26 Krotos Audio, Ammo and Reloads. [Dataset]. Available: https://www.krotosaudio.com/products/ammo-reloads-sound-effectslibrary. [Accessed: September 15, 2021]. 27 Krotos Audio, Mechanical, 1. [Dataset]. Available: https://www.krotosaudio.com/products/mechanical-sound-effectslibrary-vol-1. [Accessed: September 15, 2021]. 28 N. Simikic, Nikola Simikic Sound Library. [Dataset]. 29 Penguin Grenade, Arcs and Sparks. [Dataset]. Available: https://www.asoundeffect.com/sound-library/arcs-and-sparks. [Accessed: September 15, 2021]. 30 Penguin Grenade, Explosive Energy. [Dataset]. Available: https://www.asoundeffect.com/sound-library/explosive-energy. [Accessed: September 15, 2021]. 31 Penguin Grenade, Holograms. [Dataset]. Available: https://www.asoundeffect.com/sound-library/holograms. [Accessed: September 15, 2021]. 32 Pro Sound Effects, CORE 2, Pro. [Dataset]. Available: https://www.prosoundeffects.com/core-2. [Accessed: September 15, 2021]. 33 R. Allen, "Interview with Rick Allen Creative," August 06, 2021. 34 B. Nñsby, "Interview with Bjùrn Nñsby from Sononym," September 10, 2021. 35 Sound Ideas, Sound Ideas Library. [Dataset]. Available: https://www.sound-ideas.com. [Accessed: February 01, 2022]. 

> 36 Soundly, Soundly. [Dataset]. Available: https://www.soundly.com. [Accessed: February 01, 2022]. 

37 store.soundminer.com, last accessed September 15, 2021. 

38 storyblocks.com, last accessed September 15, 2021. 

> 39 T. Nielsen, Early Mother Communicator. [Dataset]. 

> 40 T. Nielsen, Ether. [Dataset]. 

> 41 T. Nielsen, Yellowstone. [Dataset]. 

> 42 T. Nielsen, Baltic. [Dataset]. 

> 43 T. R. Beverly, Maine Bundle. [Dataset]. Available: https://thomasrexbeverly.com/collections/soundlibraries/products/maine-bundle. [Accessed: September 15, 2021]. 

> 44 T. R. Beverly, Wild Animal Calls. [Dataset]. Available: https://thomasrexbeverly.com/products/wild-animal-calls. [Accessed: September 15, 2021]. 

45 A. McKinny, "Interview with Alan McKinny from ZapSplat," July 30, 2021. 

875 

