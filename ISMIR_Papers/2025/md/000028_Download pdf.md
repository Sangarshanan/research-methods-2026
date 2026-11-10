---
paper_id: "000028"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706383/files/000028.pdf"
---

# EMERGENT MUSICAL PROPERTIES OF A TRANSFORMER UNDER CONTRASTIVE SELF-SUPERVISED LEARNING 

Yuexuan Kong<sup>1,2</sup> Gabriel Meseguer-Brocal<sup>1</sup> Vincent Lostanlen<sup>2</sup> Mathieu Lagrange<sup>2</sup> Romain Hennequin<sup>1</sup> 

1 Deezer Research, Paris, France 

2 Nantes Université, École Centrale Nantes, CNRS, LS2N, UMR 6004, F-44000 Nantes, France 

```
ykong@deezer.com
```

## ABSTRACT 

In music information retrieval (MIR), contrastive selfsupervised learning for general-purpose representation models is effective for global tasks such as automatic tagging. However, for local tasks such as chord estimation, it is widely assumed that contrastively trained generalpurpose self-supervised models are inadequate and that more sophisticated SSL is necessary; e.g., masked modeling. Our paper challenges this assumption by revealing the potential of contrastive SSL paired with a transformer in local MIR tasks. We consider a lightweight vision transformer with one-dimensional patches in the time– frequency domain (ViT-1D) and train it with simple contrastive SSL through normalized temperature-scaled crossentropy loss (NT-Xent). Although NT-Xent operates only over the class token, we observe that, potentially thanks to weight sharing, informative musical properties emerge in ViT-1D’s sequence tokens. On global tasks, the temporal average of class and sequence tokens offers a performance increase compared to the class token alone, showing useful properties in the sequence tokens. On local tasks, sequence tokens perform unexpectedly well, despite not being specifically trained for. Furthermore, high-level musical features such as onsets emerge from layer-wise attention maps and self-similarity matrices show different layers capture different musical dimensions. Our paper does not focus on improving performance but advances the musical interpretation of transformers and sheds light on some overlooked abilities of contrastive SSL paired with transformers for sequence modeling in MIR. 

## 1. INTRODUCTION 

We may categorize tasks in music information retrieval (MIR) as either local or global. Global tasks, such as music tagging and key estimation, are time-shift invariant and require a single prediction per piece of music. Local tasks, such as beat tracking and chord estimation, are time- 

> © . Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: , “Emergent musical properties of a transformer under contrastive self-supervised learning”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

shift equivariant and require frame-wise predictions, with a frame rate typically higher than 1 Hz [1]. 

To address these tasks, self-supervised learning (SSL) has recently emerged as a powerful alternative to supervised learning in MIR. SSL enables a model to learn informative representations through a pretext task without requiring labeled data. While these pretext tasks may not have direct practical relevance, solving them requires the model to capture one or various musical dimensions [2–7]. In general-purpose models, these learned representations are then useful for many different downstream tasks, requiring only a small amount of supervision. 

In general-purpose SSL for MIR, CLMR [8] and MULE [9] marked a first step forward, following the adoption of contrastive pretext task in computer vision [10, 11]. In contrastive learning, the model is enforced by a loss to project positive pair samples close together in the embedding space and pushing negative samples far apart. Their results showed the potential of contrastive SSL to generalize across various global music tasks. However, due to the properties of convolutional neural networks and global pooling layers, both models capture global music representations that summarize the entire sequence rather than preserving information at each time step. More generalpurpose SSL research further developed on contrastive pretext tasks by using a momentum-based paradigm [12], combining different musical stems [13], analyzing transformation in embedding space [14], and developing more effective training strategies [15]. Aforementioned papers only evaluate their systems on global tasks. In contrast, the potential of general-purpose contrastive SSL on local tasks remains understudied. 

Generative modeling and masked modeling are widely used for general-purpose SSL at the frame level. Generative models such as Jukebox [16] and Music2Latent [17] have showed that various musical dimensions are captured in their embedding space used for generation, by evaluating on multiple MIR tasks. MERT [18] is a music representation learning model that resembles the masking training scheme of Hu-BERT [19] from speech. M2D [20] employs a joint-embedding predictive architecture (JEPA) that jointly predicts from both a masked sample and the original sample. MusicFM [21] conducts a comparative study of different masked modeling approaches. Although these models handle both global and local tasks well, they 

235 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
Contrastive pretext task Downstreaming tasks<br>View 1 + tokenclass  sequence tokens Local tasks Beat<br>tracking<br>0 1 … T<br>Chord<br>Patch<br>(Seq) estimation<br>+  +  NT-Xent<br>View 2 Positional   Global tasks<br>embedding Tagging<br>0 1 … T or Key<br>(Cls) (Avg) estimation<br>MLP<br>ViT-1D<br>MLP<br><!-- End of picture text -->

Figure 1: Contrastive pre-training and probing for downstream tasks. The inputs (left) are mel-spectrograms, patched along vertical slices of frequency bins per time frame. Positional encoding and a class token (learnable parameters with the average of the sequence tokens) are added. NT-Xent loss is applied only to the class token. For downstream tasks, sequence tokens `(Seq)` (excluding the class token) are used for local tasks, while the class token `(Cls)` or the average of all tokens `(Avg)` is used for global tasks. 

have two shortcomings. First, large-scale architectures are necessary: the number of parameters typically ranges from 58M (Music2latent) to 5B (Jukebox). Secondly, training these models depends on sophisticated techniques such as exponential moving averages, teacher–student distillation, and multiple loss functions; requiring careful fine-tuning of hyperparameters and large computational resources. 

Transformers have been applied to contrastive pretext tasks [22,23] using the AST architecture [24] and for multimodal audio-text learning [25, 26]. In these cases, contrastive loss is applied only to the class token; i.e., a learnable token attached at the beginning of the sequence. Optimization of the loss brings paired audio-audio or audiotext closely in the embedding space. Computer vision researchers have reported emergent properties when training Vision Transformers (ViTs) [27]. Crucially, such properties do not emerge through supervised pretraining [28]. This approach has proven valuable, not only for global tasks such as classification, but also for local tasks such as image segmentation [28,29]. Attention maps are also studied to show the emergent local properties, providing insights into the local patterns and features which are learned during training. However, to our knowledge, these emergent properties in transformer tokens have not yet been explored on local tasks for music. 

In general-purpose SSL, we notice a gap between contrastive SSL and masked modeling in MIR, particularly regarding the ability of contrastive pretext task to capture both global and local properties. This gap leads us to the following questions: have we moved on too quickly from contrastive SSL to more complex approaches? Does it still hold more untapped potential while paired with a transformer? To answer them, we proceed in following ways: 

- Pretext task. We use a lightweight ViT with 1-D spectrogram patches as token inputs (ViT-1D). We train ViT-1D with with a normalized temperature-scaled cross-entropy loss (NT-Xent) only to the class token of positive and negative pairs (Section 2). 

- Downstream tasks. We evaluate the effectiveness of both the class token and sequence tokens on local and global downstream tasks. While the class token is time-invariant due to the pretext task formulation, 

we show that sequence tokens capture local musical properties (Section 3). 

- Emergent properties. To understand how local properties are captured, we conduct qualitative and quantitative analyses of attention maps (Section 5) and self-similarity matrices (Section 6).<sup>1</sup> 

## 2. CONTRASTIVE PRETEXT TASK 

Patching details: We compute the mel-frequency spectrogram for a segment of duration equal to d = 4 seconds, obtaining matrices x, with 128 frequency bins and a frame rate of ξ = 31.5 Hz. Unlike standard ViT, which uses 2D patches, we extract 1D patches by taking all 128 mel bins from a single frame and apply one convolutional layer fp, projecting into an embedding of size (Hp, Wp) = (192, 1) for each patch xp = fp(x) and xp ∈ R<sup>Hp×Wp</sup> . By using 1D patches, each patch is directly connected to all the frequency bins in a time frame. We obtain the patch sequence xp as [x<sup>1</sup> p<sup>, x2</sup> p<sup>, ..., xT</sup> p<sup>]withT=df=126,</sup> where each patch corresponds to one time frame in the mel-spectrogram. This sequence input to a transformer is commonly named as sequence tokens [27]. 

Encoder architecture: We use the original ViT implementation of the smallest version as encoder (with our patching method) with the embedding dimension equals to 192, 12 transformer blocks and 3 attention heads. Unlike commonly done in SSL, we attach no disposable projection head to the transformer encoder, which possibly reduces overall performance of the model as adding them during the pretext training benefits downstream tasks [10], in order to focus on the emergent properties purely in the transformer. We denote fe for our encoder. We prepend a class token, composed by learnable parameters and the average of other tokens, at the beginning of xp. Then, a 2D sinusoidal positional encoding on the frequency and time dimensions is added to all patches including the class token, obtaining the final input tokens of fe as [z<sup>0</sup> 0<sup>, z1</sup> 0<sup>, ..., zT</sup> 0<sup>]</sup> with T = 126. We define the output token sequence of transformer block k at time t as z<sup>t</sup> k<sup>where 0 < k≤12 and</sup> 

> 1 Code, checkpoint and more examples for Section 5 and 6 can be found at https://github.com/deezer/ emergent-musical-properties-transformer/tree/main. 

236 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

Table 1: Downstream performance comparison of different models on two global tasks (music tagging and key estimation) and two local tasks (beat detection and chord estimation). The row `Cls` corresponds to probing with the class token while the row `Avg` refers to probing with the average of all tokens. `Seq` refers to probing only with sequence tokens. 

||||||GLOBA|L|L|OCAL|
|---|---|---|---|---|---|---|---|---|
||#PARAM|DIM|MUS|IC TAGGI<br>MAP|NG<br>ROC|KEY ESTIMATION<br>W. ACC|BEAT TRACKING<br>F-SCORE|CHORD ESTIMATION<br>ACC|
|VIT-1D|5.3M|192|`(Cls)`<br>`(Avg)`|0.400<br>0.417|0.888<br>0.896|0.509<br>0.622|`(Seq)`0.723|0.319|
|CLMR-LIKE[30]|<br>2.8M|1024||0.427|0.898|0.459|0.313|0.148|
|M2D[20]|89M|3840||0.479|0.918|0.531|0.794|0.322|



0 ≤ t ≤ T . Notably, the class token (t = 0) is processed in the same manner as sequence tokens: it shares weights with them in the multi-layer perception layers following the attention block. This design allows the class token to integrate and summarize information [27]. The output of the model is [z<sup>0</sup> L<sup>, z1</sup> L<sup>, ..., zT</sup> L<sup>]wherez0</sup> L<sup>istheclasstoken</sup> and L = 12. 

Normalized temperature-scaled cross entropy loss (NT-Xent). For each piece of music, we extract two disjoint segments A and B of four seconds each as a pair of positive samples. No data augmentation is applied. All other segments from the same batch are negative samples. To study the emerging properties in the sequence tokens, we apply the loss only on the class tokens [22, 25, 26], defining our loss function for each pair as: 



<!-- Start of picture text -->
exp(sim(z 0 L , A , z0 L , B )/τ )<br>LA,B(fe) = − log<br>� k̸=B exp(sim(z L,A 0 , z0 L,k )/τ ) (1)<br><!-- End of picture text -->

where z<sup>0</sup> L,A<sup>andz0</sup> L,B<sup>aretheclasstokensofthepositive</sup> pair of segments A and B, sim is the cosine similarity function, and τ = 0.1 is the temperature parameter. 

Pre-training details We pretrain on a subset of Deezer’s catalog of music, with a batch size of 256 pairs of 4-second segments, a base learning rate of 3 × 10<sup>−4</sup> with a cosine decay until 5 × 10<sup>−7</sup> , and train for 300 epochs. 

## 3. DOWNSTREAM TASKS 

We focus on two types of downstream tasks, commonly used in general-purpose SSL for MIR. We select music tagging and key estimation as representative global tasks and we choose beat tracking and chord estimation as examples of local tasks. A good performance on these four tasks requires the model to encode both harmonic and rhythmic representations, and high-level musical concept, on both local an global levels. 

As discussed in Section 1, to the best of our knowledge, no prior study has explored the emerging properties of sequence tokens in a transformer in local tasks trained with a contrastive learning framework. As a matter of fact, testing on local tasks may seem counterintuitive, since positive samples are simply two segments from the same piece of music, without any explicit alignment of beats or chords, therefore the class tokens are trained to be time-shift invariant. This raises the possibility that local musical information may not be expected in the token sequence since there 

are no constraints to encourage this. However, our results challenge this assumption, showing that meaningful local representations do emerge despite the lack of direct supervision at the frame level. 

## 3.1 Music tagging 

Datasets. We use MagnaTagaTune [31] with the split proposed by Lee et al. [32]. 

Training methods. We compare two different probing methods that both use a single linear layer: 1) Probe only on the class token z<sup>0</sup> L<sup>(referredas</sup><sup>`Cls`inFigure1and</sup> in Table 1); 2) Probe on the average of the entire token sequence [z<sup>0</sup> L<sup>, z1</sup> L<sup>, ..., zT</sup> L<sup>], including the class token (referred</sup> as `Avg` in Figure 1 and in Table 1). Metrics. We use the area under the receiver operating characteristic curve (ROC-AUC) and mean average precision (mAP) in their macro-aggregated versions. 

## 3.2 Music key estimation 

Datasets. We use FMAKv2 [4] with a 9:1 split between training and validation. FMAKv2, a derivative of FMAK [33], contains 5489 songs from the Free Music Archive [34], spanning multiple genres. We test on GiantSteps [35], a dataset of 604 electronic dance music tracks. Training methods. We compare the same two training methods ( `Avg` and `Cls` ) as in music tagging. Metrics. We use the weighted accuracy from mir_eval [36], which assigns weights to some key prediction errors. 

## 3.3 Beat tracking 

Datasets. We use the Ballroom dataset [37] with a 9:1 split for training and validation, which contains 698 ballroom songs. For testing, we use GTZAN Rhythm [38], which includes beat annotations for 998 songs across 10 genres. Training methods. We exclude the class token and use only the sequence tokens [z<sup>1</sup> L<sup>, ..., zT</sup> L<sup>],referredas</sup><sup>`Seq`in</sup> Figure 1 and Table 1. Since beat tracking typically requires a higher frame rate than 31.5 Hz, we attach two independent heads to each zL, doubling the frame rate to 63 Hz. Additionally, we apply a standard smoothing method for beat tracking, where we increase the values of the two neighboring frames to 0.5 instead of 0. 

Metrics. We apply a Dynamic Bayesian Network (DBN) for post-processing to obtain beat locations [39]. We use 

237 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

F -score with a tolerance window of 70 ms as evaluation metrics from the mir_eval package [36]. 

## 3.4 Chord estimation 

Datasets. We collect 124 songs from the Real World Computing Pop (RWC-POP) and Schubert Winterreise Dataset (SWD) [40,41], limited to one performance per song. We apply a 8:1:1 split between training, validation, and test. We consider 24 classes of major and minor chords, exclude those that cannot be mapped to these classes (e.g., suspended chords), and include a "no chord" class, resulting in 25 classes. The chord vocabulary is the same as used in MusicFM [21]. 

Training methods. We exclude the class token and use only the sequence tokens [z<sup>1</sup> L<sup>, . . . , zT</sup> L<sup>].Theframerate</sup> of the encoder is sufficient for chord estimation, therefore only one single linear layer is used. 

Metrics. We use frame-level accuracy over 25 classes. 

## 4. RESULTS ON DOWNSTREAM TASKS 

Using the frozen output of the pretrained ViT-1D as input to a trainable linear layer for each task, we study whether sequence tokens capture local properties, despite the class token’s time-invariance. We also assess their contribution to global tasks. We compare this to two reference models, pretrained with contrastive learning and masked modeling, evaluating them on the same downstream tasks. It is important to note that during pretext training, our model does not include a projection head after the backbone, which is a common technique used to boost performance on downstream tasks [8, 9, 30]. However, we omit it in order to study more directly the emergent properties of the transformer backbone. 

CLMR [8] is a general-purpose contrastive framework introduced for musical representation learning. However, CLMR is trained using pitch shift as data augmentation for positive samples, making it invariant to pitch shift, resulting in low performance in tonality-related tasks. Therefore, for a more fair comparison, we use a CLMR-like contrastively trained ResNet [30], without any data augmentation, trained on the same dataset as ViT-1D, with the same sampling rate and audio length. For local tasks, we upsample its resolution from 0.25 Hz to the resolution of ViT-1D for both local tasks by attaching the necessary number of linear layers. It is important to note that this upsampling process results in much more parameters for downstream training than ViT-1D, which only uses 1 and 2 linear layers respectively. 

M2D [20] employs a JEPA architecture, which combines masked modeling with a teacher–student framework trained on general audio. It is the masked modeling model that has the least amount of parameters in Section 1. We use the results as a reference. It produces frame-wise predictions at a rate of 6.3 Hz. To adapt it for beat tracking and chord estimation, we train multiple independent linear layers to upsample to the same frame rate as ViT-1D. 



<!-- Start of picture text -->
60<br>90<br>120<br>30 60 90 120 0 30 60 90 120 0 30 60 90 120<br><!-- End of picture text -->

Figure 2: Attention matrices from the 3rd, 9th, and 12th transformer blocks (left to right). Lighter colors at position [i, j] indicate more attention from token i to token j. Diagonal lines in the left figure show local attention, while vertical lines across the map in the right figure indicate a shift to global attention in deeper layers. 

We observe two key findings from Table 1. 1) Sequence tokens show better performance than CLMR-like model and comparable results to M2D on local tasks. This suggests the emergence of local and temporal musical representations, in contrast to the time-invariant nature of the class token. The music tagging performance lags behind CLMR-like and M2D, however both models have a much larger size of embedding dimension, and CLMR-like model uses a projection head after the backbone. 2) For global tasks, performance improves when averaging the class token and all sequence tokens together. This implies that the information encoded in sequence tokens is not entirely captured by the class token alone and that incorporating sequence tokens contributes positively to global tasks. 

Local musical properties in the sequence tokens improve performance on global downstream tasks and yield unexpected good results for local tasks. This shows that, despite ViT-1D being trained with NT-Xent loss only on the class token and the positive sampling strategy making it time-invariant, useful local musical properties still emerge in the sequence tokens. This raises interest in further analyzing the emergent properties across different transformer layers through attention maps (Section 5) and in self-similarity matrices (Section 6). 

## 5. PROPERTIES IN ATTENTION MAPS 

We study the emergent properties of tokens in the transformer across different layers. ViT-1D has 12 layers in total. We select the 3rd, 6th, 9th, and 12th layers as representative points, as they are evenly spaced from shallower to deeper layers. A more comprehensive analysis of all 12 layers, as well as the potential performance gains from leveraging all layers, is left for future work. 

## 5.1 Qualitative analysis of attention maps 

The attention mechanism directs attention to meaningful token positions during training and are calculated via scaled dot-product self-attention [42]: 



<!-- Start of picture text -->
M h k (Qh k , Kh k ) = softmax Q h k Kh k ⊤ (2)<br>√ d<br><!-- End of picture text -->

where 0 < k ≤ L = 12 is the depth of transformer block, 0 < h ≤ 3 is the index of head and d = 64 is the dimension 

238 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

of the embeddings of each head. This results in an attention map M<sup>h</sup> k<sup>∈R(T +1)×(T +1)ofheadkaththtransformer</sup> block where T = 126. In this section, we aim to explore the question: with a simple contrastive pretext task applied to the class token, can attention be guided toward musically meaningful positions in the sequence? 

We show the attention matrices from 3rd, 9th and 12th layers of a 4-second polyphonic sample from RWC-Pop in Figure 2. Although we also study the 6th layer, it is omitted from the figure due to space limit. Similar properties are common across other samples. The value of M<sup>h</sup> k<sup>at row i</sup> and column j presents the attention of token zk<sup>ion z</sup> k<sup>j.</sup> 

We observe that in the shallow layers of the attention maps, as seen by the presence of short vertical lines along the diagonals, attention is primarily distributed to neighbor tokens. For a given token, only nearby tokens receive attention. However, in deeper layers, vertical lines extend across the entire attention map, indicating that attention is distributed more uniformly across all tokens. For a given token, tokens across the whole sequence can receive attention. A transition from local to global attention is observed from shallower to deeper layers, observed as well in transformers trained for sentence embeddings [43]. 



<!-- Start of picture text -->
30<br>60<br>90<br>120<br>0.1<br>0.0078<br>30 60 06 120 30 60 90 120<br><!-- End of picture text -->

Figure 3: Attention matrices of a trained ViT-1D (top left) and a randomly initialized one (top right), with brighter color indicating higher attention. The scales differ between the top figures, as shown in the bottom plots, which display averaged attention matrices by column. The bottom left shows clear peaks, while the bottom right has similar maximum and minimum values, indicating that attention is evenly distributed at random initialization and becomes more focused on temporal positions during training. 

||ATT. MAP|RANDOM|SPECTRAL FLUX|
|---|---|---|---|
|F-SCORE|0.877|0.501|0.720|



Table 2: F -score of onset detection (MAPS-MUS dataset) after peak picking from an attention map of trained ViT-1D (left), compared with a ViT-1D at random initialization (center) and a feature engineering baseline (right). 

## 5.2 Alignment of attention maps with onset events 

To quantitatively assess the emergence of temporal properties in attention maps, we use an attention head of an attention block to infer onset event timestamps. We use the MUS subset of the Midi-Aligned Piano Sounds (MAPSMUS) dataset [44], which contains 30 polyphonic classical piano recordings with aligned MIDI annotations. We select this dataset and task because it is simpler to build precise hypotheses and interpret attention maps when a single instrument is present and when time-aligned symbolic information is available. However it remains polyphonic, ensuring that the task is still non-trivial. 

Among the 4 layers we study, similar properties are shown across many heads from 9th and 12th layers, also across multiple models initialized differently. We choose the attention matrix of an attention head from the 9<sup>th</sup> layer, referred as Mi,j in the following. We exclude the class token, average the attention map per column, and obtain a pseudo-activation function a(i) = ~~-∑~~ 126 <mark>1</mark> 126j=1<sup>Mi,j,where</sup> 0 < i ≤ 126. This approach is motivated by the observation of vertical lines in deeper layers, indicating that tokens receiving higher attention are similar for all tokens. Figure 3 shows Mi,j and a(i) (left) and a ViT-1D at random initialization (right) for a specific sample. The attention map of the random initialized model exhibits a very narrow value range, and the activation function is almost flat, indicating no meaningful attention was placed at the beginning of the training. 

We use the peak picking function from SciPy [45] on a(i) to obtain onset position and the F -score in mir_eval for evaluation, with a tolerance window of 70 ms. For the sake of comparison, we compare this method with spectral flux implementation in librosa and with a ViT-1D at random initialization. We use F -score as a metrics with a tol- 

erance window of 70 ms, as implemented in mir_eval [36]. 

The comparison between the attention map and the spectral flux method shows a strong alignment between attention and onset events. Furthermore, the temporal properties useful for onset event detection do not appear at random initialization; rather, they emerge during training. A contrastive pretext task applied to the class token alone directs the attention from random to musically relevant positions, without the need for specific training to do so. 

## 6. PROPERTIES IN SELF-SIMILARITY MATRICS OF TOKENS 

## 6.1 Qualitative analysis 

We extract intermediate tokens [z<sup>1</sup> k<sup>, . . . , zT</sup> k<sup>] at layers k=</sup> 3, 6, 9, 12 (same as Section 5, denoted z3 to z12), along with tokens from a randomly initialized ViT-1D model, denoted zr. For each zk, we compute a self-similarity matrix (SSM) Sk[i, j] = sim(zk[i], zk[j]) using cosine similarity. Due to space limit, SSMs of the 6th and 9th layers are omitted but are available in the GitHub repository. We show S3, S12, Sr on two audio samples of 4 seconds in Figure 4 (S6 and S9 are omitted due to space limit). Sample 1 (top row) is a monophonic song sample from RWC Pop dataset where a clear melody line is presented. Sample 2 (bottom row) is a sample from ballroom where clear beats are shown by percussive instruments. We observe several properties of tokens from different layers from Figure 4: 

Randomly initialized model contains harmonic information. Sr for sample 1 contains block structures that correspond to note events, suggesting the model captures harmonic features early on. For sample 2, it fails to 

239 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 





Figure 4: Self-similarity matrices (SSM) of tokens at different layers. Sample 1 (top row) is a melody-dominant audio sample. Sample 2 (bottom row) is a percussion-only sample. From left to right, layer 3, layer 12 and output of a randomly initializated ViT-1D. We observe clearer block pattern on the SSM of layer 3 (top left) which signifies harmonic properties are captured in the tokens, and clearer subdiagonals on the SSM of layer 12 (bottom middle) which signifies rhythmic properties are more dominant. 

capture rhythmic events, which should manifest as evenly spaced subdiagonal structures. Notably, we observe that Sr closely resembles the SSM of the model’s input, the mel-spectrograms. This observation suggests that more harmonic information is present than rhythmic information in Sr. The reason might be that the ViT-1D model incorporates skip connections between transformer blocks, which causes the output of a randomly initialized model to closely mirror the mel-spectrogram. 

Different layers encode different information. S3 exhibits clearer block-like structures than S12 or Sr for sample 1, suggesting that similar harmonic frames are embedded by similar representations. In contrast, S12, which corresponds to a deeper layer, reveals clearer subdiagonal structures than others for sample 2. These subdiagonals are characteristic of rhythmic patterns that shows the regularity of beats. Shifting from harmonic to rhythmic features could reflect the hierarchical nature of the model, where harmonic features like pitch are learned in shallow layers, while higher-level abstractions and rhythmic features, are learned in the deeper layers. 

## 6.2 Downstream results on stacked tokens 

We aim to investigate 1) which properties emerge aside from those inherited from the mel-spectrograms; 2) if tokens from intermediate transformer blocks are beneficial for downstream tasks. 

To achieve this, we use the same downstream training schemes and datasets described in Section 3. Specifically, we evaluate zr and explore the effect of stacking intermediate tokens [z3, z6, z9, z12] to form representations of dimension 192 × 4 = 768 for downstream tasks. As observed in literature, stacking tokens from different layers help with certain tasks, since redundancy of information exist at the same layer [43, 46, 47]. We believe using 

||TAG|GING|KEY|BEAT|CHORD|
|---|---|---|---|---|---|
||ROC|MAP|W. ACC|F-SCORE|ACC|
|RANDOM|.273|.807|.487|.463|.290|
|TRAINLAST|.417|.896|.622|.723|.319|
|TRAINSTACK|.437|.902|.639|.728|.422|



Table 3: Downstream performance by using randomly initialized ViT-1D, the last layer of a trained ViT-1D (Section 3), and a stack tokens of 4 different layers (Section 6.2). The testing datasets and metrics are identical to Section 3. 

weighted sum of all intermediate layers could further boost performance, we leave that to future work. 

Table 3 shows that the model at random initialization performs slightly worse than our trained ViT-1D model on chord estimation, much worse on key estimation, but still has a reasonable performance. Harmonic information is by design embedded in mel-spectrograms and is transmitted through the skip connections. For music tagging and beat tracking, there is a significant performance gap between the randomly initialized and trained ViT-1D. This result is expected, as mel-spectrograms are not ideal representations of high-level musical concepts or rhythmic structures. Moreover, for trained ViT-1D, we observe stacking tokens together significantly improves performance in chord estimation, slightly less in key estimation, but still to a good extent. This indicates that shallow layers contribute to both global and local harmonic tasks. In contrast, performance on music tagging and beat tracking remains similar, suggesting the features captured in shallower layers focus less on rhythmic structures and higher-level musical concepts. 

The differences in features learned at various layers highlight that applying a contrastive pretext only to the class token can lead to emergent properties in sequence tokens at different levels. 

## 7. CONCLUSION 

In this paper, we show the ability of a general-purpose contrastive pretext task paired with a transformer to learn local musical representations. Applying NT-Xent loss only to the class token in a lightweight ViT-1D surprisingly enables sequence tokens to handle local tasks while contributing to global ones. Despite the class token’s timeinvariance, weight sharing and attention mechanisms allow temporal musical representations to emerge. 

By analyzing attention maps, we observe that onset events can be deduced. Self-similarity matrics show different layer tokens capture distinct musical dimensions. Stacking intermediate tokens improves performance on harmonic tasks, highlighting the importance of shallowlayer representations for downstream tasks. 

We provide exploratory insights into the emergent properties of a transformer trained contrastively. Future work could further study emergent properties in all layers and whether similar emergent properties exist in supervised pretraining. Additionally, leveraging these properties in contrastive pretraining could lead to more efficient pretraining strategies. 

240 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 8. REFERENCES 

- [1] V. Lostanlen, “Convolutional operators in the timefrequency domain,” Ph.D. dissertation, École normale supérieure, 2017. 

- [2] A. Riou, S. Lattner, G. Hadjeres, and G. Peeters, “Pesto: Pitch estimation with self-supervised transposition-equivariant objective,” in Proc. of theInternational Society for Music Information Retrieval Conference (ISMIR), 2023. 

- [3] E. Quinton, “Equivariant self-supervision for musical tempo estimation,” in Proc. of the International Society for Music Information Retrieval Conference (ISMIR), 2022. 

- [4] Y. Kong, V. Lostanlen, G. Meseguer-Brocal, S. Wong, M. Lagrange, and R. Hennequin, “STONE: Selfsupervised tonality estimator,” Proc. of the International Society for Music Information Retrieval Conference (ISMIR), 2024. 

- [5] Y. Kong, G. Meseguer-Brocal, V. Lostanlen, M. Lagrange, and R. Hennequin, “S-key: Self-supervised learning of major and minor keys from audio,” in ICASSP 2025 - IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2025, pp. 1–5. 

- [6] G. Meseguer-Brocal, R. Bittner, S. Durand, and B. Brost, “Data cleansing with contrastive learning for vocal note event annotations,” in Proceedings of the 21st International Society for Music Information Retrieval Conference, 2020. 

- [7] Y. Ma, A. Øland, A. Ragni, B. M. Del Sette, C. Saitis, C. Donahue, C. Lin, C. Plachouras, E. Benetos, E. Shatri et al., “Foundation models for music: A survey,” arXiv preprint arXiv:2408.14340, 2024. 

- [8] J. Spijkervet and J. A. Burgoyne, “Contrastive learning of musical representations,” in Proc. of the International Society for Music Information Retrieval Conference (ISMIR), 2021. 

- [9] M. C. McCallum, F. Korzeniowski, S. Oramas, F. Gouyon, and A. F. Ehmann, “Supervised and unsupervised learning of audio representations for music understanding,” 2022. 

- [10] T. Chen, S. Kornblith, M. Norouzi, and G. E. Hinton, “A simple framework for contrastive learning of visual representations,” CoRR, 2020. 

- [11] X. Chen and K. He, “Exploring simple siamese representation learning,” in Proc. of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2021. 

- [12] H. Zhao, C. Zhang, and B. Z. et al., “S3t: Selfsupervised pre-training with swin transformer for music classification,” in Proc. of the IEEE International 

Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2022. 

- [13] C. Garoufis, A. Zlatintsi, and P. Maragos, “Multisource contrastive learning from musical audio,” in Proc. of the Sound and Music Computing Conference (SMC), May 2023. 

- [14] M. C. McCallum, M. E. Davies, F. Henkel, J. Kim, and S. E. Sandberg, “On the effect of data-augmentation on local embedding properties in the contrastive learning of music audio representations,” in ICASSP 2024-2024 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2024. 

- [15] J. Choi, S. Jang, H. Cho et al., “Towards proper contrastive self-supervised learning strategies for music audio representation,” in 2022 IEEE International Conference on Multimedia and Expo (ICME). IEEE, 2022, pp. 1–6. 

- [16] P. Dhariwal, H. Jun, C. Payne, J. W. Kim, A. Radford, and I. Sutskever, “Jukebox: A generative model for music,” arXiv preprint arXiv:2005.00341, 2020. 

- [17] M. Pasini, S. Lattner, and G. Fazekas, “Music2latent: Consistency autoencoders for latent audio compression,” Proc. of the International Society for Music Information Retrieval Conference (ISMIR), 2024. 

- [18] Y. Li, R. Yuan, G. Zhang, Y. Ma, X. Chen, H. Yin, C. Lin, A. Ragni, E. Benetos, N. Gyenge, R. Dannenberg, R. Liu, W. Chen, G. Xia, Y. Shi, W. Huang, Y. Guo, and J. Fu, “Mert: Acoustic music understanding model with large-scale self-supervised training,” in Proc. of the International Conference on Learning representations (ICLR), 2023. 

- [19] W.-N. Hsu, B. Bolte, Y.-S. Chuang et al., “Hubert: Self-supervised speech representation learning by masked prediction of hidden units,” IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 29, pp. 3451–3460, 2021. 

- [20] D. Niizumi, D. Takeuchi, Y. Ohishi, N. Harada, and K. Kashino, “Masked Modeling Duo: Towards a Universal Audio Pre-training Framework,” IEEE/ACM Trans. Audio, Speech, Language Process., vol. 32, pp. 2391–2406, 2024. 

- [21] M. Won, Y.-N. Hung, and D. Le, “A foundation model for music informatics,” in Proc. of the IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2024. 

- [22] L. Wang, P. Luc, Y. Wu, A. Recasens, L. Smaira, A. Brock, A. Jaegle, J.-B. Alayrac, S. Dieleman, J. Carreira et al., “Towards learning universal audio representations,” in ICASSP 2022-2022 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2022, pp. 4593–4597. 

241 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [23] K. Koutini, J. Schlüter, H. Eghbal-zadeh, and G. Widmer, “Efficient training of audio transformers with patchout,” in Proc. Interspeech 2022, 2022, pp. 2753– 2757. 

- [24] Y. Gong, Y.-A. Chung, and J. Glass, “AST: Audio Spectrogram Transformer,” in Proc. of Interspeech, 2021, pp. 571–575. 

- [25] I. Manco, E. Benetos, E. Quinton, and G. Fazekas, “Contrastive audio-language learning for music,” in Proc. of the International Society for Music Information Retrieval Conference (ISMIR), 2022. 

- [26] Q. Huang, A. Jansen, J. Lee, R. Ganti, J. Y. Li, and D. P. Ellis, “MuLan: A joint embedding of music audio and natural language,” Proc. of the International Society for Music Information Retrieval Conference (ISMIR), 2022. 

- [27] A. Dosovitskiy, L. Beyer, A. Kolesnikov, D. Weissenborn, X. Zhai, T. Unterthiner, M. Dehghani, M. Minderer, G. Heigold, S. Gelly, J. Uszkoreit, and N. Houlsby, “An image is worth 16x16 words: Transformers for image recognition at scale,” in International Conference on Learning Representations, 2021. 

- [28] M. Caron, H. Touvron, I. Misra, H. Jégou, J. Mairal, P. Bojanowski, and A. Joulin, “Emerging properties in self-supervised vision transformers,” in Proc. of the IEEE/CVF international conference on computer vision, 2021, pp. 9650–9660. 

- [29] M. Oquab, T. Darcet, T. Moutakanni, H. V. Vo, M. Szafraniec, V. Khalidov, P. Fernandez, D. Haziza, F. Massa, A. El-Nouby, R. Howes, P.-Y. Huang, H. Xu, V. Sharma, S.-W. Li, W. Galuba, M. Rabbat, M. Assran, N. Ballas, G. Synnaeve, I. Misra, H. Jegou, J. Mairal, P. Labatut, A. Joulin, and P. Bojanowski, “Dinov2: Learning robust visual features without supervision,” 2023. 

- [30] G. Meseguer-Brocal, D. Desblancs, and R. Hennequin, “An experimental comparison of multi-view self-supervised methods for music tagging,” in Proc. of the IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2024. 

- [31] E. Law, K. West, M. I. Mandel, M. Bay, and J. S. Downie, “Evaluation of algorithms using games: The case of music tagging,” in Proc. of the International Society for Music Information Retrieval Conference (ISMIR), 2009, pp. 213–218. 

- [32] J. Lee, J. Park, K. L. Kim, and J. Nam, “Sample-level deep convolutional neural networks for music autotagging using raw waveforms,” 2017. 

- [33] S. Wong and G. Hernandez, “Fmak: A dataset of key and mode annotations for the free music archive– extended abstract,” in Proc. of the International Society for Music Information Retrieval Late-Breaking/Demo Session (ISMIR-LBD), 2023. 

- [34] M. Defferrard, K. Benzi, P. Vandergheynst, and X. Bresson, “Fma: A dataset for music analysis,” Proc. of theInternational Society for Music Information Retrieval Conference (ISMIR), 2017. 

- [35] P. H. R. V. S. B. F. H. M. L. G. Peter Knees, Ángel Faraldo, “Two datasets for tempo estimation and key detection in electronic dance music annotated from user corrections,” in Proc. of the International Society for Music Information Retrieval Conference (ISMIR), 2015. 

- [36] C. Raffel, B. McFee, E. J. Humphrey, J. Salamon, O. Nieto, D. Liang, D. P. Ellis, and C. C. Raffel, “Mir_eval: A transparent implementation of common mir metrics.” in Proc. of the International Society for Music Information Retrieval Conference (ISMIR), vol. 10, 2014, p. 2014. 

- [37] F. Gouyon and S. Dixon, “A review of rhythm description systems,” in Proc. of the International Society for Music Information Retrieval Conference (ISMIR), 2004. 

- [38] U. Marchand, Q. Fresnel, and G. Peeters, “Gtzanrhythm: Extending the gtzan test-set with beat, downbeat and swing annotations,” in Proc. of the International Conference on Music Information Retrieval Late-breaking/Demo (ISMIR-LBD), 2015. 

- [39] F. Krebs, S. Böck, and G. Widmer, “An efficient statespace model for joint tempo and meter tracking.” in Proc. of the International Society for Music Information Retrieval Conference (ISMIR), 2015, pp. 72–78. 

- [40] C. Weiß, F. Zalkow, V. Arifi-Müller, M. Müller, H. V. Koops, A. Volk, and H. G. Grohganz, “Schubert winterreise dataset: A multimodal scenario for music analysis,” Journal on Computing and Cultural Heritage (JOCCH), vol. 14, no. 2, pp. 1–18, 2021. 

- [41] M. Goto and H.Hashiguchi, “Rwc music database: Popular, classical, and jazz music databases,” Proc. of the International Conference on Music Information Retrieval Conference (ISMIR), 2002. 

- [42] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polosukhin, “Attention is all you need,” Advances in neural information processing systems, vol. 30, 2017. 

- [43] B. Wang and C.-C. J. Kuo, “Sbert-wk: A sentence embedding method by dissecting bert-based word models,” IEEE/ACM Transactions on Audio, Speech, and Language Processing, vol. 28, pp. 2146–2157, 2020. 

- [44] V. Emiya, R. Badeau, and B. David, “Multipitch estimation of piano sounds using a new probabilistic spectral smoothness principle,” IEEE Transactions on Audio, Speech, and Language Processing, vol. 18, no. 6, pp. 1643–1654, 2009. 

242 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [45] P. Virtanen, R. Gommers, T. E. Oliphant, M. Haberland, T. Reddy, D. Cournapeau, E. Burovski, P. Peterson, W. Weckesser, J. Bright, S. J. van der Walt, M. Brett, J. Wilson, K. J. Millman, N. Mayorov, A. R. J. Nelson, E. Jones, R. Kern, E. Larson, C. J. Carey,<sup>˙</sup> I. Polat, Y. Feng, E. W. Moore, J. VanderPlas, D. Laxalde, J. Perktold, R. Cimrman, I. Henriksen, E. A. Quintero, C. R. Harris, A. M. Archibald, A. H. Ribeiro, F. Pedregosa, P. van Mulbregt, and SciPy 1.0 Contributors, “SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python,” Nature Methods, vol. 17, pp. 261–272, 2020. 

- [46] A. Simoulin and B. Crabbé, “How many layers and why? An analysis of the model depth in transformers,” in Proc. of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing: Student Research Workshop. Association for Computational Linguistics, Aug. 2021, pp. 221–228. 

- [47] K. Clark, U. Khandelwal, O. Levy, and C. D. Manning, “What does bert look at? an analysis of bert’s attention,” in BlackBoxNLP@ACL, 2019. 

243 

