---
paper_id: "000073"
year: 2021
title: "Curriculum Learning for Imbalanced Classification in Large Vocabulary Automatic Chord Recognition 586-593"
source_url: "https://archives.ismir.net/ismir2021/paper/000073.pdf"
---

# **CURRICULUM LEARNING FOR IMBALANCED CLASSIFICATION IN LARGE VOCABULARY AUTOMATIC CHORD RECOGNITION** 

## **Luke Rowe** 

University of Victoria lukerowe@uvic.ca 

**George Tzanetakis** University of Victoria gtzan@cs.uvic.ca 

### **ABSTRACT** 

A problem inherent to the task of large vocabulary automatic chord recognition (ACR) is that the distribution over the chord qualities typically exhibits power-law characteristics. This intrinsic imbalance makes it difficult for ACR systems to learn the rare chord qualities in a large chord vocabulary. While recent ACR systems have exploited the hierarchical relationships that exist between chord qualities, few have attempted to exploit these relationships explicitly to improve the classification of rare chord qualities. 

In this paper, we propose a convolutional Transformer model for the task of ACR trained on a dataset of 1217 tracks over a large chord vocabulary consisting of 170 chord types. In order to address the class imbalance of the chord quality distribution, we incorporate the hierarchical relationships between chord qualities into a curriculum learning training scheme that gradually learns the rare and complex chord qualities in the dataset. We show that the proposed convolutional Transformer model achieves stateof-the-art performance on traditional ACR evaluation metrics. Furthermore, we show that the proposed curriculum learning training scheme outperforms existing methods in improving the classification of rare chord qualities. 

### **1. INTRODUCTION** 

The task of automatic chord recognition (ACR) has been an active area of research in the field of music information retrieval (MIR) for over 20 years [1]. This task automates the process of chord sequence annotation, which can be time consuming when done manually. ACR systems have been shown to be useful in other MIR applications, as chord annotations can be used as descriptive low-level features to assist other MIR tasks, such as key detection, harmonic analysis, and even style analysis [2]. Typically, an ACR system takes as input the audio signal corresponding to a musical recording. Then, the system outputs a time-aligned sequence of chord labels describing the underlying harmonic structure of the musical recording. 

> © L. Rowe and G. Tzanetakis. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). **Attribution:** L. Rowe and G. Tzanetakis, “Curriculum Learning for Imbalanced Classification in Large Vocabulary Automatic Chord Recognition”, in _Proc. of the 22nd Int. Society for Music Information Retrieval Conf.,_ Online, 2021. 



<!-- Start of picture text -->
1,400,000-<br>1,200,000-<br>1,000,000<br>800,000<br>600,000<br>Number o f  rames<br>400,000-<br>200,000 Chord Quality<br>min dim7minmaj7<br><!-- End of picture text -->

**Figure 1** : Top: Power-law distribution of chord qualities in BRIM (see Section 3 for details). Bottom: Hierarchy of chord qualities. 

Most early ACR systems operated over a small chord vocabulary consisting of only major and minor chords and lacked the complexity needed for more complex chords. Recently, the focus has shifted to large vocabulary ACR, which includes a wider variety of chord qualities, such as augmented, diminished, sixth, seventh, and suspended chords. A critical issue with large vocabulary ACR is that the distribution over the chord qualities – and hence over the chord classes – exhibits a power-law distribution (see Figure 1). This imbalance is not specific to any particular ACR dataset but is intrinsic to large vocabulary ACR. Specifically, chord progressions seen across almost all genres of music overwhelmingly favor the major and minor chord qualities, which makes it difficult for ACR systems to learn the rare chord qualities. 

Despite the complexities that arise in large vocabulary ACR, important structural relationships exist between the chord qualities in a large chord vocabulary [3]. As outlined in Figure 1, the chord qualities can be arranged into a hierarchical structure consisting of _base_ chord qualities, or triads, (in rectangles) and _extended_ chord qualities, or tetrads, (in ovals). Given an extended chord quality _qE_ and a base chord quality _qB_ , we say _qE extends qB_ if the set of intervals that defines _qE_ is a superset of the set of intervals that defines _qB_ . Each extended chord quality extends a corresponding base chord quality, with the _extends_ relationship indicated by an arrow in Figure 1. We hypothesize that an ACR model can better learn an extended chord quality when it has sufficiently learned its corresponding 

586 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

base chord quality. The underlying intuition is that the base chord quality can be viewed as a harmonic base for the extended chord quality, and thus each extended chord quality can be interpreted as a more complex variant of its corresponding base chord quality. For example, the extended chord quality 7 can be viewed as a variant of base chord quality maj, where an additional b7 interval is included. 

Each extended chord quality is _rarer_ in frequency than its corresponding base chord quality as can be seen in Figure 1. Based on this observation, we introduce a curriculum learning (CL) reweighting scheme that gradually converges from the initial distribution to a balanced chord quality distribution. This way, the curriculum allows the model to learn the base chord qualities prior to learning its corresponding extended chord qualities. The proposed scheme is integrated with a convolutional Transformer model which is trained over a chord vocabulary of 170 chord types. We show that the proposed model achieves state-of-the-art performance on traditional ACR evaluation metrics. Moreover, we show that the proposed CL scheme outperforms existing methods in improving the classification of rare chord qualities. 

### **2. RELATED WORK** 

Kwok addressed this problem by implementing an “evenchance” training scheme, which ensures that each chord type has an even chance of being chosen at the beginning of each training sample [14]. Jiang _et al._ combined their structured chord representation with a reweighting scheme to reduce the model learning bias induced by the imbalanced distribution of each structured component [11]. 

### **2.2 Curriculum Learning** 

CL was first proposed by Bengio _et al._ in [23], where they demonstrated that for certain tasks with an established difficulty metric, introducing training data from easy to hard difficulty in a deep neural network can lead to faster convergence and guide training towards better local minima. To the best of our knowledge, the only existing application of CL to the task of ACR is in [24]. In [24], McVicar _et al._ designed a curriculum to train an ACR system using ground-truth annotations with noisy alignments. CL has recently been utilized to address the imbalanced classlearning problem. In [25], Wang _et al._ proposed a CL training scheme for the task of human attribute recognition, which gradually converges from the training distribution to a balanced distribution to improve the classification performance of sparsely-labelled classes. 

### **2.1 Automatic Chord Recognition** 

### **3. DATA PREPARATION** 

Most ACR systems have two stages: feature extraction and chord sequence decoding. Arguably the most notable recent advancement in ACR is the replacement of traditional machine learning with deep learning for both stages of the ACR pipeline. For example, recent ACR systems have utilized deep neural networks [4–6], convolutional neural networks [7–11], and deep belief networks [12,13] to produce robust feature representations that outperform earlier conventional methods. Moreover, recurrent neural networks [4, 9–14] and conditional random fields (CRFs) [8, 10, 11] have largely replaced hidden Markov models to capture the temporal dependencies in the chord sequence decoding process. Inspired by the recent success of Transformer-based models in the field of natural language processing [15–18], recent approaches have applied end-to-end Transformer-based models to the task of ACR [19] and to the related tasks of symbolic chord recognition and functional harmony recognition [20,21]. 

Recent focus has shifted to the large vocabulary variant of the ACR task [3, 9, 11, 13, 14]. Since the chord quality distribution over a large chord vocabulary is extremely skewed, these systems must explicitly overcome the _imbalanced class-learning problem_ , whereby model learning is biased towards the frequently-labelled classes, resulting in poor classification performance of the sparsely-labelled classes [22]. To address this problem within large vocabulary ACR, recent approaches have incorporated auxiliary training targets by decomposing chords into structured components [9,11]. However, these structured training methods still provide limited exposure to the rare chord qualities, and thus model learning is still heavily biased towards the frequently-labelled chord qualities. Deng and 

The ground-truth chord labels are mapped to a chord vocabulary _V_ of 170 chords [9]. _V_ includes chords that span all 12 pitch classes and the following 14 chord qualities _Q_ : _maj, min, dim, aug, min6, maj6, min7, minmaj7, maj7, 7, dim7, hdim7, sus2,_ and _sus4_ . Additionally, _V_ contains two extra labels: _N_ (no chord) and _X_ (unknown chord). Our model also integrates the structured chord representation proposed in [9], whereby each chord label is decomposed into its root, bass, and pitch structured components. 

For training and evaluation, we use the dataset collected by Humphrey and Bello [9, 11, 26], which comprises of 1217 tracks from the **B** illboard, **R** WC Pop, **I** sophonics, and **M** ARL collections. We refer to this collected dataset as **BRIM** . We augment the training data using MUDA [27] by pitch-shifting each audio track across _−_ 6 to +5 semitones. To properly compare the performance on traditional ACR metrics with previous methods, we use the same 5- fold cross-validation split that is used in [9,11,26]. 

We employ a separate 5-fold cross-validation split for the imbalanced class-learning ACR experiments. Since the chord-type distribution in BRIM is extremely imbalanced, it is imperative for proper evaluation that this distribution is maintained across each fold of our 5-fold split. However, since the 5-fold split occurs at the _track_ level but the distribution is measured at the _frame_ level, we found stratifying over the chord types to be intractable. Therefore, we propose an approximate 5-fold stratification algorithm that instead ensures that the distribution over the _chord qualities_ in BRIM is approximately maintained across each fold. The proposed algorithm (Algorithm 1) takes as input a set of _chord quality profiles P_ = _{Pt}_ , where _Pt_ [ _q_ ] is the pro- 

587 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

Fold 0 _Fold 1 Fold 2 Fold 3 Fold 4 **Algorithm 1:** _N_ -Fold Chord Quality Stratification 0.4 **Input:** Number of folds: _N_ ; set of chord qualities: _Q_ ; set of tracks _T_ ; chord quality profiles: _P_ = _{Pt}_ ; rarest chord Proportion<sup>0.2-</sup> quality: _qr_ . 0.0 **for** _i_ initialize empty list = 0 **to** _N −_ 1 **do** _folds_ [ _i_ ] dim7hdim7<sup>maj</sup> maj6maj7 min6 minmaj7 sus4 initialize fold profile _Fi_ , where for each _q ∈ Q_ , (a) 5-fold split used in [9,11,26]. _Fi_ [ _q_ ] = 0 0.4 _T_ sorted = SortDescending( _T_ , by= _P_ [ _qr_ ]) 0.2 **for** _i_ = 0 **to** _N −_ 1 **do** Proportion append _T_ sorted[ _i_ ] to _folds_ [ _i_ ] 0.0 remove _Fi_ [ _q_ ] = _T F_ sorted _i_ [ _q_ ] +[ _i_ ] _P_ from _T_ sorted _T_ [ _i_ ][ _q_ ] for each _q ∈ Q_ aug<sup>dim</sup> dim7hdim7majmaj6maj7minmin6min7minmaj7sus2sus4 **while** _T̸_ = _∅_ **do** (b) 5-fold Stratified Split. _q_<sup>_′_</sup> = argmax Var( _F_ 0[ _q_ ] _, . . . , FN −_ 1[ _q_ ]) _q∈Q_ **Figure 2** : 5-fold splits of BRIM. The height of each bar at _t_ min = argmin _Pt_ [ _q_<sup>_′_</sup> ] chord quality _q_ corresponds to the proportion of _q_ chords _t∈T_ contained in the corresponding fold. _i_ max = argmax _Fi_ [ _q_<sup>_′_</sup> ] _i∈{_ 0 _,...,N −_ 1 _}_ append _t_ min to _folds_ [ _i_ max] convolutional encoder is passed through a stack of _N_ bi- _Fi_ max[ _q_ ] = _Fi_ max[ _q_ ] + _Pt_ min[ _q_ ] for each _q ∈ Q_ directional self-attention layers proposed in [19]. Details remove _t_ min from _T_ of this layer can be found in [19]. We replace the absolute **for** each remaining fold _i̸_ = _i_ max **do** positional encoding used in [19] with relative positional _t_<sup>_′_</sup> = argmin _Pt_ [ _q_<sup>_′_</sup> ] + _Fi_ [ _q_<sup>_′_</sup> ] _− Fi_ max[ _q_<sup>_′_</sup> ] _t∈T_ encoding [16], which has been shown to offer better genappend _t_<sup>_′_</sup> to _folds_ [ _i_ ] eralization capabilities by taking into account the relative _Fi_ [ _q_ ] = _Fi_ [ _q_ ] + _Pt′_ [ _q_ ] for each _q ∈ Q_ positions between frames in the self-attention mechanism. remove _t_<sup>_′_</sup> from _T_ The model facilitates structured training of the root **return** _<u>folds</u>_ note, bass note, and pitch classes as is done in [9]. Un- 

**Figure 2** : 5-fold splits of BRIM. The height of each bar at chord quality _q_ corresponds to the proportion of _q_ chords contained in the corresponding fold. 

convolutional encoder is passed through a stack of _N_ bidirectional self-attention layers proposed in [19]. Details of this layer can be found in [19]. We replace the absolute positional encoding used in [19] with relative positional encoding [16], which has been shown to offer better generalization capabilities by taking into account the relative positions between frames in the self-attention mechanism. 

The model facilitates structured training of the root note, bass note, and pitch classes as is done in [9]. Unlike in [9], we multiply the pitch structured loss by _γ >_ 1 to assign more priority to the pitch structured component. The model learns to jointly minimize the cross-entropy chord label loss _L_ label and the cross-entropy structured loss _L_ struct, where _L_ struct is the sum of the cross entropy losses for the pitch, root, and bass structured components. For each frame _t_ , the model outputs a softmax distribution _y_ ˆ<sup>(</sup><sup>_t_)</sup> _∈_ [0 _,_ 1]<sup>_|V |_</sup> over _V_ . At evaluation time, the system predicts the label with the highest activation in _y_ ˆ<sup>(</sup><sup>_t_)</sup> for each frame _t_ . An overview of the model is shown in Figure 3. 

portion of _q_ chords in track _t_ over BRIM, for each _q ∈ Q_ . The algorithm iteratively builds up a fold profile _Fi_ for each fold _i_ , where _Fi_ [ _q_ ] is the proportion of _q_ chords in fold _i_ over BRIM, for each _q ∈ Q_ . At each iteration, one track is added to each fold. At iteration 1, we take the 5 tracks with the highest proportion of the rarest chord quality _qr_ and add one track to each fold. Each subsequent iteration can be viewed as a “correction step,” whereby one track is added to each fold to minimize the variance of the highestvariance chord quality over the folds. The result of the 5-fold chord quality stratification is shown in Figure 2b. 

### **4.2 Curriculum Learning** 

The idea of CL is to train the _easy_ samples before the _hard_ samples. Loosely, we define an easy sample as a frame where the ground-truth chord quality is a _base_ chord quality, and a hard sample as a frame where the groundtruth chord quality is an _extended_ chord quality. We want to ensure that for each extended chord quality, the system first sufficiently learns its corresponding base chord quality. A critical observation in Figure 1 is that each extended chord quality is rarer than its corresponding base chord quality. Based on this observation, we propose a CL reweighting scheme that gradually converges from the training distribution to a balanced chord quality distribution, similar to the scheme proposed by Wang _et al._ in [25]. The proposed scheme enables the model to put emphasis on the frequently-labelled chord qualities at the beginning of training and put increasingly more emphasis on the rare chord qualities as training converges. Since the pitch- 

### **4. METHODS** 

### **4.1 Convolutional Transformer (CT)** 

The proposed system uses the log-power Constant Q- Transform (CQT) spectrogram as its input feature representation. We apply a convolutional-residual encoder shown in Figure 3b to capture short-term context and induce sufficient temporal smoothing of the spectrogram. The encoder first applies batch-normalization (BN) [28] to the input CQT. We then apply a series of convolutional layers and add 3 skip connections [29] to ease the training process. Each convolutional layer is zero-padded to preserve the spatial dimension of the CQT. After each convolutional layer, a BN layer followed by a Rectified Linear Unit (ReLU) activation is applied. The output of the 

588 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 



<!-- Start of picture text -->
CQT 3x3 conv, 16<br>Convolutional Encoder (b) 3x3 conv, 16<br>Bi-directional Self- ×N 3x3 conv, 32<br>Attention Layer [19] 3x3 conv, 32<br>Pitch Root Bass↓<br>Dense + Dense + Dense + 5x5 conv, 64<br>Sigmoid Softmax Softmax<br>5x5 conv, 64<br>Concatenated Features<br>1x1 conv, 1<br>Dense + Softmax<br>Softmax Distribution over V Dense<br>(a) (b)<br><!-- End of picture text -->

**Figure 3** : Proposed CT architecture. (a) outlines the endto-end architecture and (b) outlines the layers of the proposed convolutional encoder. 

shifting data augmentation eliminates the root bias in the training data, then balancing the chord-quality distribution also balances the chord-type distribution during training. 

The proposed scheme runs for _E_ epochs. At epoch _e_ = 1, the target distribution is the training distribution ( _i.e._ an imbalanced chord quality distribution). As _e_ approaches _E_ , the system gradually modifies the target chord quality distribution to be more balanced; this is achieved by reweighting samples by placing higher weights on the frames where the ground-truth chord quality is sparselylabelled and lower weights on the frames where the ground-truth chord quality is frequently-labelled. At epoch _e_ = _E_ , the chord quality distribution is balanced. 

Let _Q_<sup>_′_</sup> = _Q ∪{N, X}_ . Let _Cq_ be the number of frames in the training set with chord quality _q ∈ Q_<sup>_′_</sup> and let _qmin ∈ Q_<sup>_′_</sup> be the chord quality with the least number of frames in the training set. We define the chord quality training _Cq_ distribution _D_ train by _D_ train _,q_ = _Cqmin_<sup>for all</sup><sup>_q∈Q′_.</sup> 

Let _De_ be the target chord quality distribution at epoch _e_ . Then _D_ 1 = _D_ train. During model training, the target chord quality distribution gradually transfers to a balanced distribution with the following function: 



<!-- Start of picture text -->
De,q = ( D train ,q ) g ( e ) ∀q ∈ Q ′ (1)<br><!-- End of picture text -->

where _e_ is the epoch number and _g_ ( _e_ ) is the curriculum scheduler function. The scheduler function is a monotonically decreasing function from 1 to 0 that sets the pace of the curriculum. We experiment with three scheduler functions (visualized in Figure 4): _g_ ( _e_ ) = 0 (baseline, fixed balanced chord quality distribution), _g_ ( _e_ ) = 1 _− E_<sup>_<u>e−</u>_</sup> _−_<sup><u>1</u></sup> 1<sup>(lin-</sup> ear schedule), and _g_ ( _e_ ) = _φ_<sup>_e_</sup> _− φ_<sup>_E_</sup> (convex schedule), where _φ_ is a hyperparameter. Observe that for all three scheduler functions, _g_ ( _E_ ) = 0 and thus _DE,q_ = 1 for all _q_ ; _i.e._ the target chord quality distribution is balanced. 

At epoch _e_ , to facilitate training with target chord quality distribution _De_ , we reweight the samples such that for chord class _i ∈ V_ having chord quality _q ∈ Q_<sup>_′_</sup> , the class weight _wi_ assigned to _i_ in _L_ label is defined by: 



<!-- Start of picture text -->
wi =  De,q/D train ,q (2)<br><!-- End of picture text -->

As the training set chord quality distribution is extremely 

g(e) = 0 linear (ə)b convex 

**Figure 4** : Proposed curriculum scheduler functions. 

imbalanced, the variation in the magnitude of the weights _wi_ across the different chord classes _i ∈ V_ is extremely large at epoch _e_ = _E_ . We hypothesize that this may cause the temporal smoothness of the output predictions to be impaired. Therefore, we train an additional CRF decoder on top of the output logits to smooth the output predictions, in the same way as [8]. 

The proposed CL scheme differs from [25] in three critical ways. First, the training set statistics are used for computing the reweighting terms _wi_ , whereas [25] uses batch statistics. Using batch statistics is suboptimal for ACR since batches typically consist of a small number of sequences, and the frames of each sequence are highly interdependent. Therefore, we believe that the training statistics are more representative of the true chord quality imbalance. Second, in [25], the frequently-labelled samples are _down-sampled_ by setting some samples to have weight 0 and the remaining to have weight 1. Down-sampling is ill-advised for ACR as this would disrupt the temporal coherence of the training sequence. Therefore, the proposed scheme instead employs a fully reweighted approach so that the continuity of the training sequences are preserved. Third, the proposed scheme employs a CRF decoder to smooth the output predictions at model convergence. 

### **5. EXPERIMENTS** 

### **5.1 Model Evaluation** 

To compare the proposed CT model with previous methods, evaluation is conducted using mir_eval [30]. We obtain Weighted Chord Symbol Recall (WCSR) scores for: Root, Thirds, Triads, Sevenths, Tetrads, Maj-Min, and MIREX. We average the results of each metric across the folds, as is done in [19]. For the methods addressing the imbalanced class-learning problem, we utilize two evaluation metrics proposed in [11]: the mean frame-wise accuracy (accframe) and mean class-wise accuracy (accclass) over _V_ . accframe is defined by: 



<!-- Start of picture text -->
ni =1 Ci<br>accframe = n (3)<br>MM<br>i =1 Fi<br><!-- End of picture text -->

where _n_ is the number tracks for evaluation, _Fi_ is the number of frames in track _i_ , and _Ci_ is the number of correctlypredicted frames in track _i_ over vocabulary _V_ . accclass is defined by: 



<!-- Start of picture text -->
1 ni =1 C i v<br>accclass = n (4)<br>|V | v∈V i =1 F v i<br>-∑ MM<br><!-- End of picture text -->

where _Fi_<sup>_v_is the number of frames in track</sup><sup>_i_with ground-</sup> truth chord label _v_ and _Ci_<sup>_v_is the number of frames in track</sup> 

589 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

|Metric|CT|CT_−_RE|CT_−_RE,S|CT_−_RE,S,C<br>(BTC) [19]|CR2S+A [9]|CRNN<sup>_∗_</sup>[11]|
|---|---|---|---|---|---|---|
|Root|**0.838**|0.836|0.831|0.829|0.821|0.837|
|Thirds|**0.809**|0.807|0.802|0.798|0.784|0.803|
|Triads|**0.767**|0.764|0.759|0.754|0.742|0.759|
|Sevenths|**0.714**|0.711|0.709|0.700|0.677|0.694|
|Tetrads|**0.650**|0.646|0.644|0.638|0.615|0.630|
|Maj-Min|**0.826**|0.823|0.819|0.813|0.802|0.822|
|MIREX|**0.832**|0.828|0.825|0.820|0.803|0.812|



_i_ that are correctly predicted as _v_ . Further, we define an additional metric termed the mean quality-wise accuracy (accquality) over _V_ to be used in the CL experiments. We define accquality by: 



<!-- Start of picture text -->
MIREX 0.832 0.828 0.825 0.820 0.803 0.812<br>1 � ni =1 C i q<br>accquality = � (5)<br>|Q| � ni =1 F i q Table 1 : WCSR scores averaged across 5 folds. − RE de-<br>q∈Q<br>notes removal of relative positional encoding. − S denotes<br>is the number of frames in track  i  with ground- removal of structured training. − C denotes removal of<br>quality q and Cii q is the number of frames in the convolutional encoder. ∗ operates over a larger chord-<br>correctly predicted as having ground-truth vocabulary  V ′ consisting of 301 chord types [11].<br><!-- End of picture text -->

where _Fi_<sup>_q_is the number of frames in track</sup><sup>_i_with ground-</sup> truth chord quality _q_ and _Cii_<sup>_q_isthenumberofframesin</sup> track _i_ that are correctly predicted as having ground-truth chord quality _q_ . As previously outlined in [11, 14], when addressing the imbalanced class-learning problem within the task of large vocabulary ACR, we want to maximize the accclass while still maintaining the accframe. 

|Method|accframe|accclass|
|---|---|---|
|CT|**0.677**|0.347|
|CT+CLBaseline|0.647|0.427|
|CT+CLLinear|0.658|0.439|
|CT+CLConvex|0.657|**0.449**|
|CT+EC [14]|0.650|0.379|
|CRNN0_._5_,_10 [11]|0.630|0.321|



### **5.2 Implementation Details** 

Using librosa [31], audio is transformed into a logpower constant-Q spectrogram spanning 6 octaves with 36 bins per octave. The sample rate is 44100 _Hz_ , and the hop size is 4096. We tune the hyperparameters of the bi-directional self-attention layers (optimized to BRIM): number of self-attention layers _N_ = 6, number of selfattention heads _nh_ = 8, hidden dimension _d_ = 512, and dropout probability _p_ = 0. The CT model is trained using the Adam optimizer [32] with initial learning rate 1e4. The learning rate is reduced by a factor of 10 when the validation _L_ label loss does not improve after 10 consecutive epochs. Model training terminates when the validation _L_ label loss does not improve after 20 consecutive epochs. We save the model weights with the lowest validation _L_ label loss for evaluation. In each epoch, a contiguous 248-frame segment is randomly sampled from each training track, and a mini-batch consists of 32 such segments. Structured training is conducted in the same way as [9], with the exception that we set _γ_ = 7. We set the _L_ label class weights to _wi_ = 1 for all _i ∈ V_ . 

**Table 2** : accframe and accclass scores over _V_ for all databalancing methods using stratified split over BRIM. 

which we call CRNN. As BRIM is significantly larger than the dataset used to train the BTC model, the BTC model is re-trained on BRIM as described in Section 5.2. We evaluate these models using the WCSR metrics and the same 5-fold split of BRIM that is used in [9,11,26]. 

All CL experiments are trained and evaluated with the CT model. We denote the models with convex and linear scheduler functions as CT+CLConvex and CT+CLLinear, respectively. The baseline model with scheduler function _g_ ( _e_ ) = 0 is denoted CT+CLBaseline. We also evaluate the even-chance training scheme proposed in [14], which we call CT+EC. Specifically, we adjust the CT model training procedure so that each chord type _v ∈ V_ has an even chance of being selected at the beginning of each training segment. accquality is used as the validation metric for the CT+EC model. Further, we evaluate the reweighting scheme of [11] on the CRNN model. We experiment with the best-reported reweighting configuration ( _γ, w_ max) = (0 _._ 5 _,_ 10 _._ 0), which we call CRNN0 _._ 5 _,_ 10. For evaluation we use the accframe and accclass metrics using the stratified 5- fold split of BRIM. 

For the CL experiments, we set _E_ = 90 and _φ_ = 0 _._ 95. Since only the _chord qualities_ of the 5-fold split are stratified, the imbalance in the root distribution across the folds may cause accclass to be an unreliable validation metric. Thus, we instead use accquality. The training details remain the same with a few exceptions. Namely, the learning rate is reduced by a factor of 10 when the validation accquality has not improved for 10 consecutive epochs. For the linear and convex scheduler functions, we save the model weights at convergence (epoch _e_ = _E_ ) for evaluation. For the baseline scheduler function _g_ ( _e_ ) = 0, we save the model weights with the highest validation accquality for evaluation. We train the CRF using Adam with a learning rate of 1e-2. We terminate training the CRF once the validation accquality stops improving. Our implementation is available at https://github.com/ RLuke22/curriculum-learning-acr. 

### **5.4 Results** 

The WCSR scores for all models considered are shown in Table 1. Table 1 also includes an ablation study that outlines the performance degradation with the removal of each novel component in the CT architecture; _i.e._ the convolutional encoder (C), structured training (S), and relative positional encoding (RE). Note that the CT architecture without all three novel components (and with the inclusion of global z-normalization) is equivalent to BTC [19]. Table 1 shows that the CT model outperforms existing ACR systems across all WCSR metrics. Further, the ablation study indicates that each novel component offers a gradual, yet consistent improvement to the CT model. 

### **5.3 Methods under Comparison** 

We compare our proposed CT architecture with CR2S+A [9], BTC [19] and the best-performing model of [11], 

Table 2 shows the results of the methods that address 

590 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

|||||||Chord|Quality|Accuracy|||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Method|maj|min|7|min7|maj7|sus4|maj6|min6|sus2|dim|aug|hdim7|dim7|minmaj7|
|CT|**0.801**|**0.637**|0.518|0.576|0.570|0.277|0.102|0.134|0.034|0.365|0.236|0.357|0.031|0.031|
|CT+CLConvex|0.735|0.626|**0.537**|**0.595**|**0.634**|0.406|**0.275**|**0.288**|**0.261**|**0.395**|**0.517**|**0.476**|0.181|**0.229**|
|CT+CLBaseline|0.727|0.618|0.512|0.581|0.604|**0.411**|0.250|0.264|0.235|0.386|0.460|0.450|**0.209**|0.151|



**Table 3** : Chord quality accuracies of various CT models over BRIM at evaluation. Chord quality accuracy is defined as the proportion of frames where the predicted chord quality matches the ground-truth chord quality. 

imbalanced class-learning including a baseline CT model ( _i.e._ no reweighting). Unsurprisingly, the CT model performs the best in the accframe metric. This is consistent with previous works that have shown that optimizing the class-wise accuracy typically harms the frame-wise accuracy [11,14]. The best-performing CL model CT+CLConvex provides substantial improvement (10.2%) in the classwise accuracy, with only a modest degradation (2.0%) in the frame-wise accuracy. This indicates that the CL scheme considerably suppresses the learning bias in the model induced by the imbalanced chord quality distribution without significantly impairing the performance of the frequently-labelled classes. Moreover, both CL configurations CT+CLConvex and CT+CLLinear offer improvements in the accframe and accclass metrics over the baseline CT+CLBaseline. This indicates that by having the model sufficiently learn the base chord qualities prior to the corresponding extended chord qualities, the model better generalizes on both the frequently-labelled and sparsely-labelled chord qualities. This is further confirmed in Table 3, which shows that CT+CLConvex outperforms CT+CLBaseline in chord quality accuracy on every chord quality except for sus4 and dim7. 

In Figure 5, we evaluate the chord quality accuracies of the CT+CLConvex model at different epochs in the curriculum. Note that the dim base chord quality accuracy (in dark green) improves substantially from epochs 1 to 10, followed by an improvement in the hdim7 (in red) and dim7 (in purple) extended chord qualities from epochs 10 to 20 and 10 to 40, respectively. Similar trends can be observed for the maj and min base chord qualities. This indicates that sufficient learning of the base chord qualities leads to performance improvements in the corresponding extended chord qualities. We hypothesize that the convex scheduler function outperforms the linear scheduler function in class-wise accuracy because the extreme imbalance in the chord quality distribution warrants a faster curriculum pace at the beginning of training. As shown in Table 2, the proposed CT+CLConvex model convincingly outperforms previous methods in the accclass metric. Note that the CRNN0 _._ 5 _,_ 10 results in Table 2 differ from the results reported in [11] as we run CRNN0 _._ 5 _,_ 10 over a different chord vocabulary _V_ than the one used in [11]. 

To validate the inclusion of the CRF decoder in the CL scheme, we count the number of chord changes in BRIM predicted by the CT model, the CT+CLConvex model, and the CT+CLConvex model without the CRF (denoted CT+CLConvex-CRF). Table 4 shows that the model weights at CL convergence disrupt the smoothness of the output chord-label predictions, as evidenced by the substan- 



<!-- Start of picture text -->
0.8<br>aug<br>0.6 majmaj6<br>maj7<br>min<br>min6<br>min7<br>minmaj7<br>sus2<br>sus4<br>Chord Quality A c uracy0.2 dim<br>dim7<br>hdim7<br>0.0<br>10 20 30 40<br>Epoch<br><!-- End of picture text -->

**Figure 5** : Chord quality accuracies of CT+CLConvex evaluated at different points along the curriculum. 

|Method|Chord Changes|
|---|---|
|CT|170,287|
|CT+CLConvex|123,350|
|CT+CLConvex-CRF|235,885|
|Ground-Truth|122,231|



**Table 4** : Predicted chord changes over BRIM. 

tially larger number of predicted chord changes by the CT+CLConvex-CRF model. 

### **6. CONCLUSION** 

We propose a convolutional Transformer architecture for ACR and a novel CL reweighting scheme to handle the imbalanced chord quality distribution. The proposed scheme exploits the hierarchical relationships between chord qualities by gradually converging from the initial distribution to a balanced chord quality distribution. The proposed curriculum outperforms existing methods and non-CL baselines in improving the classification performance of rare chord qualities without significantly degrading the classification performance of the frequently-labelled chord qualities. Although the proposed method considerably diminishes the model-learning bias induced by the imbalanced chord quality distribution, the model still generally favors the frequently-labelled chord qualities. We believe this is primarily an issue of data scarcity. Therefore, a promising future direction to handle the imbalanced classlearning problem for ACR is to generate more annotated data either synthetically or by leveraging the vast amount of publically-available unannotated audio tracks. 

591 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

### **7. ACKNOWLEDGEMENTS** 

We would like to thank the Natural Sciences and Engineering Research Council of Canada (NSERC) for their generous funding and support of this work. We would also like to thank Brian McFee for providing us with the BRIM dataset, Quinton Yong for his helpful insights on the stratification algorithm, and the anonymous reviewers for their insightful and constructive feedback. 

### **8. REFERENCES** 

- [1] T. Fujishima, “Real-time chord recognition of musical sound: A system using common lisp music,” in _Proceedings of the International Computer Music Conference (ICMC)_ , 1999, pp. 464–467. 

- [2] C. Weiß, F. Brand, and M. Müller, “Mid-level chord transition features for musical style analysis,” in _IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)_ , 2019, pp. 341–345. 

- [3] T. Carsault, J. Nika, and P. Esling, “Using musical relationships between chord labels in automatic chord extraction tasks,” in _Proceedings of the 19th International Society for Music Information Retrieval Conference (ISMIR)_ , 2018, pp. 18–25. 

- [4] S. Sigtia, N. Boulanger-Lewandowski, and S. Dixon, “Audio chord recognition with a hybrid recurrent neural network,” in _Proceedings of the 16th International Society for Music Information Retrieval Conference (ISMIR)_ , 2015, pp. 127–133. 

- [5] X. Zhou and A. Lerch, “Chord detection using deep learning,” in _Proceedings of the 16th International Society for Music Information Retrieval Conference (ISMIR)_ , 2015, pp. 52–58. 

- [6] F. Korzeniowski and G. Widmer, “Feature learning for chord recognition: The deep chroma extractor,” in _Proceedings of the 17th International Society for Music Information Retrieval Conference (ISMIR)_ , 2016, pp. 37–43. 

- [7] E. Humphrey and J. P. Bello, “Rethinking automatic chord recognition with convolutional neural networks,” in _11th International Conference on Machine Learning and Applications (ICMLA)_ , 2012, pp. 357–362. 

- [8] F. Korzeniowski and G. Widmer, “A fully convolutional deep auditory model for musical chord recognition,” in _26th IEEE International Workshop on Machine Learning for Signal Processing_ , 2016, pp. 1–6. 

- [9] B. McFee and J. P. Bello, “Structured training for largevocabulary chord recognition,” in _Proceedings of the 18th International Society for Music Information Retrieval Conference (ISMIR)_ , 2017, pp. 188–194. 

- [10] Y. Wu and W. Li, “Automatic audio chord recognition with midi-trained deep feature and BLSTM-CRF sequence decoding model,” _IEEE ACM Transactions_ 

_on Audio, Speech, and Language Processing_ , vol. 27, no. 2, pp. 355–366, 2019. 

- [11] J. Jiang, K. Chen, W. Li, and G. Xia, “Largevocabulary chord transcription via chord structure decomposition,” in _Proceedings of the 20th International Society for Music Information Retrieval Conference (ISMIR)_ , 2019, pp. 644–651. 

- [12] N. Boulanger-Lewandowski, Y. Bengio, and P. Vincent, “Audio chord recognition with recurrent neural networks,” in _Proceedings of the 14th International Society for Music Information Retrieval Conference (ISMIR)_ , 2013, pp. 335–340. 

- [13] J. Deng and Y. Kwok, “A hybrid gaussian-HMM-deep learning approach for automatic chord estimation with very large vocabulary,” in _Proceedings of the 17th International Society for Music Information Retrieval Conference (ISMIR)_ , 2016, pp. 812–818. 

- [14] ——, “Large vocabulary automatic chord estimation with an even chance training scheme,” in _Proceedings of the 18th International Society for Music Information Retrieval Conference (ISMIR)_ , 2017, pp. 531–536. 

- [15] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. Kaiser, and I. Polosukhin, “Attention is all you need,” in _Advances in Neural Information Processing Systems 30: Annual Conference on Neural Information Processing Systems_ , 2017, pp. 5998–6008. 

- [16] Z. Dai, Z. Yang, Y. Yang, J. Carbonell, Q. Le, and R. Salakhutdinov, “Transformer-xl: Attentive language models beyond a fixed-length context,” in _Proceedings of the 57th Conference of the Association for Computational Linguistics_ , 2019, pp. 2978–2988. 

- [17] J. Devlin, M. Chang, K. Lee, and K. Toutanova, “BERT: pre-training of deep bidirectional transformers for language understanding,” in _Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies_ , 2019, pp. 4171–4186. 

- [18] Z. Yang, Z. Dai, Y. Yang, J. Carbonell, R. Salakhutdinov, and Q. Le, “Xlnet: Generalized autoregressive pretraining for language understanding,” in _Advances in Neural Information Processing Systems 32: Annual Conference on Neural Information Processing Systems_ . 

- [19] J. Park, K. Choi, S. Jeon, D. Kim, and J. Park, “A bi-directional transformer for musical chord recognition,” in _Proceedings of the 20th International Society for Music Information Retrieval Conference (ISMIR)_ , 2019, pp. 620–627. 

- [20] T. Chen and L. Su, “Harmony transformer: Incorporating chord segmentation into harmony recognition,” in 

592 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

   - _Proceedings of the 20th International Society for Music Information Retrieval Conference (ISMIR)_ , 2019, pp. 259–267. 

- [21] ——, “Attend to chords: Improving harmonic analysis of symbolic music using transformer-based models,” _Transactions of the International Society for Music Information Retrieval_ , vol. 4, no. 1, pp. 1–13, 2021. 

      - M. Vollrath, and A. Weiss, “librosa/librosa: 0.7.1,” Oct. 2019. [Online]. Available: https://doi.org/10. 5281/zenodo.3478579 

   - [32] D. Kingma and J. Ba, “Adam: A method for stochastic optimization,” in _3rd International Conference on Learning Representations, (ICLR)_ , 2015. 

- [22] H. He and E. Garcia, “Learning from imbalanced data,” _IEEE Transactions on Knowledge and Data Engineering_ , vol. 21, no. 9, pp. 1263–1284, 2009. 

- [23] Y. Bengio, J. Louradour, R. Collobert, and J. Weston, “Curriculum learning,” in _Proceedings of the 26th Annual International Conference on Machine Learning (ICML)_ , 2009, pp. 41–48. 

- [24] M. McVicar, Y. Ni, T. D. Bie, and R. SantosRodriguez, “Leveraging noisy online databases for use in chord recognition,” in _Proceedings of the 12th International Society for Music Information Retrieval Conference (ISMIR)_ , 2011, pp. 639–644. 

- [25] Y. Wang, W. Gan, J. Yang, W. Wu, and J. Yan, “Dynamic curriculum learning for imbalanced data classification,” in _2019 IEEE/CVF International Conference on Computer Vision (ICCV)_ , 2019, pp. 5016–5025. 

- [26] E. Humphrey and J. P. Bello, “Four timely insights on automatic chord estimation,” in _Proceedings of the 16th International Society for Music Information Retrieval Conference (ISMIR)_ , 2015, pp. 673–679. 

- [27] B. McFee, E. Humphrey, and J. P. Bello, “A software framework for musical data augmentation,” in _Proceedings of the 16th International Society for Music Information Retrieval Conference (ISMIR)_ , 2015, pp. 248–254. 

- [28] S. Ioffe and C. Szegedy, “Batch normalization: Accelerating deep network training by reducing internal covariate shift,” in _Proceedings of the 32nd International Conference on Machine Learning, (ICML)_ , 2015, pp. 448–456. 

- [29] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image recognition,” in _2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)_ , 2016, pp. 770–778. 

- [30] C. Raffel, B. McFee, E. Humphrey, J. Salamon, O. Nieto, D. Liang, and D. Ellis, “Mir_eval: A transparent implementation of common MIR metrics,” in _Proceedings of the 15th International Society for Music Information Retrieval Conference, (ISMIR)_ , 2014, pp. 367– 372. 

- [31] B. McFee, V. Lostanlen, M. McVicar, A. Metsai, S. Balke, C. Thomé, C. Raffel, D. Lee, F. Zalkow, K. Lee, O. Nieto, J. Mason, D. Ellis, R. Yamamoto, E. Battenberg, R. Bittner, K. Choi, J. Moore, Z. Wei, S. Seyfarth, P. Friesch, F. Stöter, D. Hereñú, T. Kim, 

593 

