---
paper_id: "000013"
year: 2022
title: "Download pdf"
source_url: "https://zenodo.org/record/7316610/files/000013.pdf"
---

# THE POWER OF DEEP WITHOUT GOING DEEP? A STUDY OF HDPGMM MUSIC REPRESENTATION LEARNING 

Jaehun Kim 

Delft University of Technology Multimedia Computing Group J.H.Kim@tudelft.nl 

Cynthia C. S. Liem Delft University of Technology Multimedia Computing Group 

C.C.S.Liem@tudelft.nl 

## ABSTRACT 

In the previous decade, Deep Learning (DL) has proven to be one of the most effective machine learning methods to tackle a wide range of Music Information Retrieval (MIR) tasks. It offers highly expressive learning capacity that can fit any music representation needed for MIR-relevant downstream tasks. However, it has been criticized for sacrificing interpretability. On the other hand, the Bayesian nonparametric (BN) approach promises similar positive properties as DL, such as high flexibility, while being robust to overfitting and preserving interpretability. Therefore, the primary motivation of this work is to explore the potential of Bayesian nonparametric models in comparison to DL models for music representation learning. More specifically, we assess the music representation learned from the Hierarchical Dirichlet Process Gaussian Mixture Model (HDPGMM), an infinite mixture model based on the Bayesian nonparametric approach, to MIR tasks, including classification, auto-tagging, and recommendation. The experimental result suggests that the HDPGMM music representation can outperform DL representations in certain scenarios, and overall comparable. 

## 1. INTRODUCTION 

Deep learning became one of the most popular and successful methodologies to tackle a various range of MIR tasks; music classification [1], music generation [2], recommendation [3] and more. Some of the known benefits are 1) the high expressiveness towards any data structure, 2) effective ways to handle the overfitting, and finally, 3) the rapidly improving infrastructural supports, including both hardware (i.e., accelerators such as GPU) and software (i.e., deep learning frameworks). Fuelled by these benefits, DL models can learn useful representations of diverse data, which is one of the key reasons for its success [4]. On the other hand, DL models often are criticized for their lack of interpretability [5], also for applications within the MIR domain [6,7]. 

> © J. Kim and C. C. S. Liem. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: J. Kim and C. C. S. Liem, ªThe power of deep without going deep? A study of HDPGMM music representation learningº, in Proc. of the 23rd Int. Society for Music Information Retrieval Conf., Bengaluru, India, 2022. 

According to [8,9], interpretability of a machine learning model can be defined as the degree to which a user can understand the underlying mechanism of its operation. In this regard, DL models would be substantially less interpretable due to their complex internal structure than simplerÐyet may be comparably expressiveÐalternatives such as hierarchical probabilistic models. 

The Bayesian Nonparametric (BN) approach is such an alternative to achieving what DL does well in an interpretable way. As a nonparametric method, it can overcome underfitting by unlimited model capacity, while resisting overfitting through its Bayesian nature [10]. At the same time, the model can be interpretable, as the probabilistic model structure hypothesizes the data generation process in a relatively simple and humanly understandable manner. 

In past decades, BN models have been applied in various MIR tasks. For example, they were applied to a latent representation of music audio in estimating music (self-) similarity [11, 12]. They also were employed to conduct harmonic and spectral analyses by decomposing the timefrequency representation of the music audio into a mixture of countable infinite latent components [13, 14]. These analyses also have shown to be useful for downstream tasks such as structural analysis [15] or music recommendation [16]. Further, a discriminative model based on the BN was developed for music emotion recognition [17]. 

While DL gained considerable popularity, it is striking BN models did not gain as much attention. As they promise similar high-level properties and strengths to DL, it will be worthwhile to explore to what extent they compare to modern DL models for MIR-relevant tasks. Therefore, in this work, we will assess music representations learned from BN models, and compare them under similar experimental control with modern deep neural network models. In particular, we consider the Hierarchical Dirichlet Process Gaussian Mixture Model (HDPGMM) [16,18, 19] as our model of interest. To concretize the comparison, we employ the transfer learning experimental framework [20±22], which is commonly used for assessing the potential of learned representations. The contributions of this work can be listed as follows: 

1. We explore and suggest insight into how ªgoodº and transferable the HDPGMM representation is for a range of MIR tasks. 

2. We provide an implementation of an efficient, GPU- 

116 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

accelerated inference algorithm for HDPGMM, which can handle large-scale music datasets. 

## 2. HDPGMM 

In this section,<sup>1</sup> we introduce the Hierarchical Dirichlet Process Gaussian Mixture Model (HDPGMM) [12, 19]. We first discuss the Dirichlet Process Mixture Model (DPMM) upon which the HDPGMM is extended. 

## 2.1 Dirichlet Process Mixture Model 

The Dirichlet Process (DP) is an well-known stochastic process that draws random probability distributions, which often is described as a distribution over distributions [10]. One of the most common applications of DP is the infinite mixture model, thanks to the property of DP that one can draw distributions of an arbitrary dimensionality. Thus, the Dirichlet Process Mixture Model (DPMM) can find the appropriate number of components K based on the set of observations as part of the learning process. 

Among several ways to represent DP, we introduce the stick-breaking construction [24]<sup>2</sup> . Stick-breaking constructs DP in a simple and general manner. Formally, it is as follows: 



<!-- Start of picture text -->
βk ′ ∼ Beta(1, γ) ϕk ∼ H<br>k−1 ∞ (1)<br>βk = βk ′ �(1 − βl ′) G0 = � βkδφk<br>l=1 k=1<br><!-- End of picture text -->

where the two equations in the left column represent the draw of infinite dimensional weights βk which sums to one. Notably, the distribution for β is also referred to β ∼ GEM(γ) [25]. In the right column, H denotes the base distribution from which variable ϕk ∈ Φ is drawn. The right bottom equation defines the draw of the probability measure G0, where δφk means the point mass centered at the component ϕk. Altogether, Eq. (1) constructs the DP G0 ∼ DP(γ, H). Figure 1 depicts the process in a graphical way. 



Figure 1: Illustration of stick-breaking construction. 

In the mixture model context, we want to infer mixture components {ϕ1, ϕ2, · · · , ϕk, · · · } that fit to the data observations {x1, x2, · · · , xn}, which are assumed to be 

> 1 We adopted most of the notations from [18,23]. 

> 2 Literature commonly chooses the Chinese Restaurant Process (CRP) as an illustrative metaphor for DP, as it is intuitive and explains various properties of DP well [10]. We discuss DP with the stick-breaking construction, due to its further usage in the model inference within the work. Other metaphorical descriptions of DP are given in [10,12] 

drawn from distributions F (ϕ) parameterized with variable ϕ (i.e., for a multivariate Gaussian F , ϕ = {µ, Σ}). We now can use DP for drawing the component ϕ that corresponds to xi by introducing the cluster assignment variable yi ∼ Mult(β): 



<!-- Start of picture text -->
β|γ ∼ GEM(γ) ϕk|H ∼ H<br>(2)<br>yi|β ∼ Mult(β) xi|yi, {ϕk} ∼ F (ϕyi )<br><!-- End of picture text -->

where ϕyi denotes the component parameter ϕ indexed by the assignment variable yi corresponding to the ith observation xi. 

## 2.2 Hierarchical DPMM 

In many data structures, groupings of atomic data points arise naturally (i.e., audio frames within a song, songs from an artist, words of lyrics). Hierarchical DP (HDP) is an extension of DP that models the ªgroupingsº by imposing group-level DPs derived from the ªcorpus-levelº DP as the global pool of components [19]. Following [18], the jth group-level DP can be expressed as follows: 



<!-- Start of picture text -->
πjt ′ ∼ Beta(1, α0) ψjt ∼ G0<br>t−1 ∞ (3)<br>πjt = πjt ′ �(1 − πjs ′ ) Gj = � πjtδψjt<br>s=1 t=1<br><!-- End of picture text -->

As seen above, HDP appears as the recursion of multiple levels of DPs<sup>3</sup> . Notably, the base distribution G0 of each group-level DP is from the corpus-level DP. This relationship allows mapping group-level atoms ψjt to the corpus-level atoms ϕk. Wang et al. [18] introduce indicator variables cjt ∼ Mult(β) which maps ψjt and ϕk by ψjt = ϕcjt , where β is drawn from the corpus-level DP in Eq. (1). It simplifies the model as we do not need to represent ψjt explicitly. Finally, we can represent HDPMM by introducing another indicator variable zjn ∼ Mult(πj) for the nth observation xjn within the jth group, similarly to Eq. (2): 



<!-- Start of picture text -->
πj|α0 ∼ GEM(α0) θjn = ψjzjn = ϕcjzjn<br>zjn|πj ∼ Mult(πj) xjn|zjn, cjt, {ϕk} ∼ F (θjn)<br>(4)<br><!-- End of picture text -->

where we use the indicator zjn to select ψjt, which eventually is mapped as ϕcjzjn that represents the parameter θjn to draw the observation xjn. HDPGMM is then defined by simply setting F as the (multivariate) Gaussian distribution and setting H as one of the distributions from which we can sample the mean and covariance (i.e., Gaussian-inverse Wishart distribution). Figure 2 depicts the HDPGMM graphically. 

## 2.3 Inference Algorithm 

We employ the online Variational Inference (VI) [18], which is a common and significantly faster choice than the Markov Chain Monte Carlo (MCMC) method to infer fully Bayesian models. VI approximates the true posterior by 

> 3 It implies naturally that multiple levels are possible (i.e., corpus - author - document) if it suits the data structure. 

117 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 



Figure 2: Illustration of 2-level HDPMM within corpussong context. The top row depicts the corpus-level DP. The second row describes the draw of second-level (songlevel) DPs per song from the corpus-level DP. Frame-level features are drawn from each song-level DPs, as depicted in the third row of the image. 

minimizing the Kullback-Leibler (KL) divergence between the approximation q(Z) and the true posterior p(Z|X), where Z denotes the set of latent variables and parameters that we want to find, and X refers a set of observations [23]. One of the popular simplifications is the full factorization of the distribution q(Z) =<sup>�|</sup> i<sup>Z</sup> =1<sup>|qi(Zi).In</sup> the context of HDPGMM, we have the following: 



<!-- Start of picture text -->
q(β ′ , π ′ , c, z, ϕ) = q(β ′ )q(π ′ )q(c)q(z)q(ϕ) (5)<br><!-- End of picture text -->

where β<sup>′</sup> , π<sup>′</sup> , c, z denote the corpus-level and group-level stick proportions, group-level component selection variable, and finally the observation-level component selection variable, respectively. ϕ refers to the parameter(s) for the F which draws the atomic observation, set as (multivariate) Gaussian in our context. Thus, ϕ includes the means µ and precision matrices Λ of each Gaussian component. We adopt the result from [23], where the Gaussian-Wishart distribution is used for the prior. 

Each variational distribution further factorizes into: 



<!-- Start of picture text -->
q(β ′ ) = � k K−1 Beta(βk ′ |uk, vk)<br>q(π ′ ) = � t T −1 Beta(πt ′|at, bt) (6)<br>q(c) = � j �t Mult(cjt|φjt)<br>q(z) = � j �n Mult(zjn|ζjn)<br><!-- End of picture text -->

where uk, vk, at, bt denote the variational parameters for the Beta distributions for corpus-level and group-level stick proportions, respectively. φjt ∈ R<sup>K</sup> , ζjn ∈ R<sup>T</sup> are the variational parameters for the Multinomial distribution to draw the selector c and z. Also, we truncate the infinite Beta distributions by K and T , which is a common way to avoid actually computing the infinite dimension [18]. With a sufficiently large number for the truncation, the model will still not be limited to the truncation and will only use the number of components optimal for the dataset. The final variational distribution is the Gaussian-Wishart distribution which draws the Gaussian parameters ϕ for F : 

q(ϕ) =<sup>�K</sup> k<sup>N(µk|mk, (λkΛk)−1)W(Λk|Wk, νk)</sup> (7) where we draw the precision Λk ∈ R<sup>d×d</sup> from the Wishart distribution with the variational parameter Wk ∈ R<sup>d×d</sup> and 

νk ∈ R, and the mean µk ∈ R<sup>d</sup> is drawn by the precision weighted by λk ∈ R and mean mk ∈ R<sup>d</sup> . 

We then can obtain the optimal model by maximizing the lower bound of the marginal log likelihood log p(X|Z) [23,26,27]: 

log p(X|Z) ≥ Eq[log p(X, β<sup>′</sup> , π<sup>′</sup> , c, z, ϕ)] + H(q) =<sup>�</sup> j �Eq[log (p(Xj|cj, zj, ϕ)p(cj|β<sup>′</sup> )p(zj|πj<sup>′)p(π</sup> j<sup>′|α0))]</sup> +H(q(cj)) + H(q(zj)) + H(q(πj<sup>′))</sup> � +Eq[log p(β<sup>′</sup> )p(ϕ)] + H(q(β<sup>′</sup> )) + H(q(ϕ)) (8) 

where H(·) denotes the entropy of given distribution, and Xj = {xj1, xj2, · · · , xjNj } is a set of observations within the jth group.<sup>4</sup> 

Using the standard result of VI [18, 23, 27], the update rules for group-level parameters are derived as follows: 



<!-- Start of picture text -->
ajt = 1 + � n ζjnt (9)<br>bjt = α0 + � n �Ts=t+1 ζjns (10)<br>φjtk ∝ exp( � n ζjntEq[log p(xjn|ϕk)] + Eq[log βk])<br><!-- End of picture text -->



<!-- Start of picture text -->
(11)<br><!-- End of picture text -->

ζjnt ∝ exp(<sup>�K</sup> k=1<sup>φjtkEq[log p(xjn|ϕk)] + Eq[log πjt])</sup> (12) 

Similarly, the update rules for the corpus-level parameters are as follows [23]: 



<!-- Start of picture text -->
uk = 1 + � j �Tt=1 φjtk (13)<br>vk = γ + � j �Tt �Kl=k+1 φjtl (14)<br>λk = λ0 + Nk (15)<br><!-- End of picture text -->



<!-- Start of picture text -->
mk = λ − k 1(λ0m0 + Nkx¯k) (16)<br><!-- End of picture text -->



<!-- Start of picture text -->
λ0Nk<br>Wk −1 = W0 −1 + NkSk + λ0 + Nk ( x¯k − m0)(¯xk − m0) ⊺<br><!-- End of picture text -->



<!-- Start of picture text -->
(17)<br><!-- End of picture text -->



<!-- Start of picture text -->
νk = ν0 + Nk (18)<br><!-- End of picture text -->

where λ0 ∈ R, m0 ∈ R<sup>d</sup> , ν0 ∈ R, W0 ∈ R<sup>d×d</sup> are the hyperparameters corresponding to the weight, location, degrees of freedom, and scale of Gaussian-Wishart distribution. The ªsufficient statisticsº and expectations in the update rules are defined as follows: 



<!-- Start of picture text -->
Eq[log βk] = Eq[log βk ′ ] + �k l=1 −1 Eq[log (1 − β l ′)]<br>Eq[log βk ′ ] = Ψ(uk) − Ψ(uk + vk)<br>Eq[log (1 − βk ′ )] = Ψ(vk) − Ψ(uk + vk)<br>Eq[log πjt] = Eq[log πjt ′ ] + � s t− =1 1 Eq[log (1 − π s ′ )]<br>Eq[log πjt ′ ] = Ψ(ajt) − Ψ(ajt + bjt)<br>Eq[log (1 − πjt ′ )] = Ψ(bjt) − Ψ(ajt + bjt)<br>Nk = � j �n rjnk<br>x¯k = N 1 k �j �n rjnkxjn<br>Sk = N 1 k �j �n rjnk(xjn − x¯k)(xjn − x¯k)⊺<br><!-- End of picture text -->

> 4 Thus, the terms inside the sum over the group would further factorize into sums of per-group observations. We do not write these out for legibility and space considerations. 

118 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

where Ψ(·) refers to the digamma function, and rjnk = �Tt=1<sup>ζjntφjtkistheinferredªresponsibilityºofthenth</sup> observation of the jth group on the kth component. A standard batch update would compute statistics across the entire corpus, and update the corpus-level parameters. However, it may be slow or may suffer from too large or small numbers accumulated from a large-scale corpus. 

We therefore employ the online VI, where corpus-level parameters are updated per mini-batch of groups passed. In this way, the early phase of model inference can be accelerated substantially compared to the full-batch update [18, 28]. The corpus-level update is then controlled by the learning rate ρt = (τ0 + t)<sup>−κ</sup> , which is decayed over iterations parameterized by the offset τ0 > 0 and the rate κ ∈ (0.5, 1]: 



<!-- Start of picture text -->
Zt = (1 − ρt)Zt−1 + ρtZ ˜ t (19)<br><!-- End of picture text -->

where Z<sup>˜</sup> t denotes one of the corpus-level parameters from Eq. (13) to (18), which is updated by the given mini-batch at tth iteration, while Zt−1 is the current parameter. To scale the update with respect to the mini-batch size, we weight Z<sup>˜</sup> by the factor of w =<sup><mark>|</mark></sup> |XX<sup>˜</sup> <mark>|</mark> |<sup><mark>,</mark>where |X|, | ˜X| denote</sup> the number of groups within the entire observation set X and the mini-batch of groups X<sup>˜</sup> . The overall inference algorithm is described in Algorithm 1. 

Al <mark>g</mark> orithm 1: Online VI for HDPGMM Initialize ϕ = (ϕk)k<sup>K</sup> =1<sup>, u = (uk)</sup> k<sup>K</sup> =1<sup>, v= (vk)</sup> k<sup>K</sup> =1 randomly and set t = 1. while Stopping criterion is not met do Fetch a random mini-batch of groups X<sup>˜</sup> repeat Update aj, bj, ζj and φj using Eq. (9) to (12) until mini-batch likelihood stops improving; Compute uk, vk, λk, mk, Wk, and νk using Eq. (13) to (18) Set ρt = (τ0 + t)<sup>−κ</sup> , t ← t + 1 Update uk, vk, λk, mk, Wk, and νk using Eq. (19) end 

Inspired by the implementation of [18, 27], we apply further regularization to the model. Specifically, we ªsplashº the uniform noise to the inferred responsibility rjn as it can be biased if the groups are corrupted or incomplete, such as the preview audio of the entire song: 



<!-- Start of picture text -->
r˜jn = (1 − ηt)rjn + ηte (20)<br><!-- End of picture text -->

where ηt is the regularization coefficient that determines the extent uniform noise e = (ek)<sup>K</sup> k=1<sup>ismixedintorjn.</sup> <mark>η0</mark> ∗10<sup>3</sup> ηt = (t+10<sup>3</sup> )<sup>alsoisdefinedasdecayingfunctionsimilar</sup> to the learning rate ρt. 

## 3. EXPERIMENTAL SETUP 

The overall experimental design is adopted from the recent music representation learning studies [20, 21, 29], where multiple downstream MIR tasks are tested with the feature set learned from the representation models.<sup>5</sup> 

> 5 The source code can be found at https://github.com/ eldrin/hdpgmm-music-experiments. 

## 3.1 Datasets, Features & Evaluation 

We use a subset of Million Song Dataset (MSD) [30] as the dataset for the representation learning; more specifically, the audio preview excerpts from the MSD ªtrainº subset introduced by [31, 32]<sup>6</sup> . For the evaluation of the representation, we employ three downstream tasks encompassing music genre classification, music auto-tagging, and music recommendation. For each target task, we chose the GTZAN dataset [33] with the fault-filtered split [34], the MagnaTagATune (MTAT) dataset [35] with the split from [36], and finally the Echo Nest taste profile subset as part of MSD (Echonest) [30] filtered by user and item frequency [37]. 

We evaluate the modeling using the cross-validation of task-specific prediction models. We fit the logistic regression models for GTZAN and MTAT datasets, taking the learned music representation as input and predicting the genre or music tags. We find the hyper-parameters of the logistic regression model by a randomized parameter search [38] for each run. As for the recommendation, we apply the item K Nearest Neighbor (item-kNN) method [39] where the song-song similarity is measured by the cosine similarity of the learned music representation. We adopt the data split introduced in [37]. For every trial, disjoint validation and test users are uniformly sampled, which includes 1142 users for each. Then 30% of listening records of these users are held out as testing records. We find the best K by conducting a grid search on the range K ∈{2<sup>4</sup> , 2<sup>5</sup> , 2<sup>6</sup> , 2<sup>7</sup> , 2<sup>8</sup> , 2<sup>9</sup> } by measuring the accuracy on the validation users. Using the best K, we compute the final score on the held out test records of testing users. We take the average score over 5 repetitions for each run to incorporate the random split effect. 

We repeat 5 evaluation runs for each learning trial to consider the various random effects (i.e., initialization, randomized search). We employ the commonly used accuracy measures in each task to assess them, which are further elaborated in Table 1. 

|Id|# Samples|# Classes/# Users|Acc. Measure|
|---|---|---|---|
|MSD|213,354|N/A|N/A|
|Echonest|40,980|571,355 <sup>7</sup>|nDCG [40]|
|GTZAN|1,000|10|F1 [41]|
|MTAT|25,863|50|AUROC[42]|



Table 1: Details on the datasets. We use the macro average strategy for F1 and Area Under Receiver Operating Characteristic curve (AUROC) measure, and we consider the top 500 recommended songs for computing the normalized Discounted Cumulative Gain (nDCG). 

We select a set of audio features to infer the HDPGMM and non-DL baseline models inspired by [17]. The further details of the features can be found in Table 2. We use the implementation of librosa [43] with the default parameters for all the features. 

> 6 Length of preview audio differs per clip, where about 70% of samples are approximately 30 seconds and the rest are 1 minute, with a small subset longer than 1 minute. 

> 7 This refers the number of users in the dataset. 

119 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

|Feature|Aspect|Dim.|Transform|
|---|---|---|---|
|MFCC|Timbre|13|-|
|∆MFCC|Timbre|13|-|
|∆∆MFCC|Timbre|13|-|
|Onset Strength [44]|Rhythm|1|log|
|Chroma[45]|Tonal|12|log|



Table 2: Details on the base audio features we employed for the experiment. 

## 3.2 Comparisons 

We evaluate 4 comparisons against HDPGMM, including DL-based and non-DL-based models. 

- G1 is the simplest model among the comparisons. The song-wise feature is represented by the concatenated parameters ϕ = {µ, Σ} of the single multivariate Gaussian fitted on the frame-level base audio feature vectors within a song. We chose the square root of the diagonal in covariance, which means the feature is the concatenation of mean µ ∈R<sup>52</sup> and standard deviation σ ∈R<sup>52</sup> of features. 

- VQ Codebook can be deemed as the approximation of HDPGMM models [12]. First, a corpus-wise K-means clustering is fitted on the frame level features. Then, song-level feature is represented by the normalized frequency of cluster assignment of each frame-level feature within the song.<sup>8</sup> We set K = 256. 

- KIM is a DL-based music representation trained in a simple self-supervised learning framework with a VGGlike [46] architecture [20]. We use the original implementation of the work, which takes the stereo melspectrogram of a 2.5 second-length clip as input. The representation is extracted from the last hidden layer before the prediction and summarized with global average and standard deviation pooling through the entire song. 

- CLMR [29] is a recent DL-based music representation employing self-supervised learning through the contrastive learning method [47]. We employ the original implementation of [29] that uses the 2.67 second-length raw audio samples as input feature.<sup>9</sup> The representation is drawn from the last hidden layer and pooled with the global average over the entire song excerpt. 

- HDPGMM uses the base audio feature with the whitening following [48]. As for song-level representation yj, we employ the exponentiation of y˜jk = exp(Eq[log p(Xj|cj, zj, ϕk)]) and normalize it = 

- over components and the length of the clip yjk Nj<sup>−1</sup> <mark>�</mark> Kk<sup>′</sup> <mark>y</mark> ˜=1 <mark>j</mark> k<sup>y˜jk′</sup><sup><mark>.</mark></sup> We adopt many hyper-parameter setups from the result of [18]; we set the truncation of components on the corpus level K and the song level T as 256 and 32 respectively, mini-batch size to 

8 It can be interpreted similarly to the inferred cluster assignment variable πj in Eq. (4). 

> 9 Unlike the original work, we reduce the dimensionality of the hidden layer, from which we extract the representation, from 512 to 256 to control the representation dimensionality with other comparisons. Also, we do not apply the data augmentation for a fair comparison and also as it is beyond the main scope of the work. However, as it is reported that it can meaningfully improve the representation, we assume that applying the method would benefit other models similarly. 

1024, learning rate parameters κ = 0.6 and τ0 = 64. We, however, explore the regularization rate η0 ∈ {10<sup>−4</sup> , 10<sup>−3</sup> , 10<sup>−2</sup> , 10<sup>−1</sup> } and total corpus size |X| ∈ {2 × 10<sup>3</sup> , 2 × 10<sup>4</sup> , 213354} to examine their effect on the representation.<sup>10</sup> 

For all the comparisons except G1, we repeat 3 learning trials in consideration of random effects. Within a trial, we iterated the update for 100 epochs for KIM, CLMR, and HDPGMM. Further, we set the representation’s dimensionality to 256, homogeneous across all comparisons except G1. Finally, we take the logarithm of the representation yˆj = log(max(yj, 10<sup>−8</sup> )) if it is given as the probability simplex (i.e., VQCodebook, HDPGMM). 

## 4. RESULT AND DISCUSSION 

## 4.1 Effect of Learning Factors 

Overall, we observe that the learning factors of HDPGMM can make a substantial difference. As Figure 3 shows, the result suggests that the additional regularization in Eq. (20) generally affects positively the performance of all the downstream tasks we tested. It implies that the entire song inputs would likely improve the representation further, as the regularization crudely masks the effect of the missing data due to the preview clipping to some extent. 

Further, we find that the number of training samples positively affects the performances in general. We measured the effect by repeatedly sub-sampling the training data 5 times in two different sizes mentioned in Section 3.2, and conducted the same evaluation applied for the full training set. The result shows that the positive effect is logarithmic, suggesting that the model should be learned with an exponentially larger dataset to get a linear improvement in the performance. The recommendation task, on the other hand, indicates the effect may not be linear, as we observe that the learning with 2 × 10<sup>3</sup> samples outperforms the 2 × 10<sup>4</sup> samples. However, the largest dataset leads to a better representation than the smallest datasets. 

## 4.2 Model Comparison 

|Dataset|Measure|Model|Mean(±SD)|
|---|---|---|---|
|||G1|0.0237 (±0.0011)|
|||VQCodebook|0.0155 (±0.0003)|
|Echonest|nDCG|KIM|0.0257 (±0.0015)|
|||CLMR|0.0362 (±0.0012)|
|||HDPGMM|0.0221(±0.0006)|
|||G1|0.5396 (±0.0049)|
|||VQCodebook|0.5777 (±0.0022)|
|GTZAN|F1|KIM|0.5420 (±0.0290)|
|||CLMR|0.6375 (±0.0368)|
|||HDPGMM|0.6467(±0.0069)|
|||G1|0.8441 (±0.0006)|
|||VQCodebook|0.8386 (±0.0013)|
|MTAT|AUROC|KIM|0.8014 (±0.0045)|
|||CLMR|0.8262 (±0.0026)|
|||HDPGMM|0.8482(±0.0020)|



Table 3: Evaluation results on downstream tasks. 

> 10 The implementation can be found at https://github.com/ eldrin/pytorch-hdpgmm. 

120 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

|Hip-Hop|country|female vocalists|pop|electronic|pop|oldies|
|---|---|---|---|---|---|---|
|pop|rock|singer-songwriter|female vocalists|dance|soul|blues|
|rnb|pop|pop|female vocalist|electronica|female vocalists|country|
|soul|oldies|acoustic|rock|funk|rnb|60s|
|male vocalists|indie|Mellow|Love|electro|dance|soul|
|rock|singer-songwriter|folk|dance|Hip-Hop|Hip-Hop|rock|
|0.0394|0.0308|0.0299|0.0269|0.0268|0.0248|0.0227|



Table 4: Top tags for a few mostly ªloadedº components (column-wise). The last row is the normalized total responsibility N˜k = <mark>Nk �</mark> Kk<sup>′Nk′</sup><sup><mark>,</mark>meaning the proportional amount of songs having the component.</sup> 



<!-- Start of picture text -->
Echonest GTZAN MTAT<br>0.6 6 0.8 5<br>0.02 2<br>0.02 0 0.6 3 0.8 4<br>0.6 0<br>0.01 8 0.8 3<br>0.01 6 0.5 7<br>0.8 2<br>0.01 4 0.5 4<br>η0 η0 η0<br>(a) Effect of regularization factor η0. (|X| = 213, 354)<br>Echonest GTZAN MTAT<br>0.02 3 0.6 6 0.8 5<br>0.02 2<br>0.6 4<br>0.02 1 0.8 4<br>0.6 2<br>0.02 0<br>0.8 3<br>0.01 9 0.6 0<br>0.01 8 0.5 8 0.8 2<br>#samples #samples #samples<br>1e−041e−031e−021e−01 1e−04 1e−03 1e−02 1e−01 1e−04 1e−03 1e−02 1e−01<br>2k 20k 213k 2k 20k 213k 2k 20k 213k<br>nDCG@500 F1[macro]<br>AUROC[macro]<br>nDCG@500 F1[macro]<br>AUROC[macro]<br><!-- End of picture text -->

(b) Effect of the number of training samples. (η0 = 10<sup>−1</sup> ) Figure 3: Effect of the learning factors on HDPGMM. Error bars indicate the standard deviations, and the grey dots are the raw data points. 

Model comparison suggests that the HDPGMM model is comparable to the DL representation on average and can outperform it in a few specific scenarios. For the comparison, we chose the best HDPGMM model according to the result in Section 4.1 by setting η0 = 10<sup>−1</sup> and using the entire dataset. As reported in Table 3, KIM achieves worse performance than HDPGMM on GTZAN and MTAT while performing better at recommendation (Echonest). On the other hand, CLMR, which adopts a more sophisticated learning strategy, achieves the best performance in Echonest, but performs worse than HDPGMM on MTAT and comparable on GTZAN. It is notable that the mixture model variants (VQCodebook, HDPGMM) perform particularly worse on the recommendation task. We hypothesize that the cosine similarity might not be an optimal choice for the probability simplex representation, or the feature set we consider may lack aspects that are crucial for the recommendation; this requires further study. 

Except for this case, HDPGMM outperforms the other non-DL comparisons in general. It especially achieves significant improvement over its simplified version (VQCodebook) for all tasks, and mostly outperforms G1. 

## 4.3 Component Interpretability 

Finally, we explore the interpretability aspect of the HDPGMM model. To achieve it, we employ the Lastfm- 

MSD music tag dataset [30] where we find the mapping between the MSD songs and the social music tags. All our MSD training samples have mappings to the social tags, whose vocabulary size reaches roughly half a million. We compute the most relevant music tags for each corpus-level component found by the HDPGMM model. We estimate the relevance by a proxy measure αtk = �j∈X:t∈j<sup>N −</sup> j<sup>1</sup> �n<sup>rjnk,wheretdenotesthetagindex</sup> and rjnk refers the responsibility computed in Eq. ( 20). To improve the clarity, we filter the most popular tags by weighting the measure by the Inverse Document Frequency (IDF) for each tag. 

Table 4 shows an example from one of the HDPGMM with high regularization (η0 = 10<sup>−1</sup> ). It suggests that the most frequent component (the first column) can be interpreted as the corpus-wide, universal topic. From second to the rest it represents a few other topics of music, such as country-rock (column 1), pop-female vocalist (column 2, 3, 5), and electronic-dance (column 4). Notably, several compatible topics (i.e., columns 2, 3, and 5) exist, which can be interpreted as the collection of slightly different sub-clusters of an umbrella topic. It suggests that the advanced BN methods such as the hierarchical latent component models using the nested HDP [49] would further improve the representation. 

## 5. CONCLUSION AND FUTURE WORK 

In this work, we explore the potential of a BN model in the MIR task space. The results suggest that the HDPGMM representation achieves comparable effectiveness over the DL equivalents and outperforms a few scenarios. It implies that the method can be as effective as DL models when used in the supervised learning setup as well, by, for instance, jointly maximizing the variational lower bound both for the data generation and the prediction tasks. It has already been shown that such a joint objective approach can outperform the separated feature learning and transfer strategy that we demonstrate in this work [17]. 

Notably, HDPGMM is one of the more simple models in the BN approach. As mentioned above, there are models that are ªdeeperº such as nested DP models, which allow for a hierarchical structure of latent components [49]. The model also can be improved by introducing a sequential model such as Hidden Markov Models (HMM) as a base distribution [11], as the HDPGMM model assumes the exchangeability of tokens (feature frames), which is not ideal for a music signal. We left these possibilities to future work. 

121 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

## 6. ACKNOWLEDGEMENT 

A part of this work was carried out on the Dutch national e- infrastructure with the support of the SURF Coorperative. 

## 7. REFERENCES 

- [1] M. Won, J. Spijkervet, and K. Choi, Music Classification: Beyond Supervised Learning, Towards Real-world Applications. https://musicclassification.github.io/tutorial, 2021. [Online]. Available: https://music-classification.github.io/tutorial 

- [2] J. Briot, G. Hadjeres, and F. Pachet, Deep Learning Techniques for Music Generation, ser. Computational Synthesis and Creative Systems. Springer International Publishing, 2019. 

- [3] M. Schedl, ªDeep learning in music recommendation systems,º Frontiers in Applied Mathematics and Statistics, vol. 5, 2019. 

- [4] E. J. Humphrey, J. P. Bello, and Y. LeCun, ªMoving beyond feature design: Deep architectures and automatic feature learning in music informatics,º in Proceedings of the 13th International Society for Music Information Retrieval Conference, ISMIR 2012, Mosteiro S.Bento Da Vitória, Porto, Portugal, October 8-12, 2012, F. Gouyon, P. Herrera, L. G. Martins, and M. Müller, Eds. FEUP Edições, 2012, pp. 403±408. 

- [5] L. H. Gilpin, D. Bau, B. Z. Yuan, A. Bajwa, M. A. Specter, and L. Kagal, ªExplaining explanations: An overview of interpretability of machine learning,º in 5th IEEE International Conference on Data Science and Advanced Analytics, DSAA 2018, Turin, Italy, October 1-3, 2018, F. Bonchi, F. J. Provost, T. EliassiRad, W. Wang, C. Cattuto, and R. Ghani, Eds. IEEE, 2018, pp. 80±89. 

- [6] B. L. Sturm, ªA simple method to determine if a music information retrieval system is a ªhorseº,º IEEE Trans. Multim., vol. 16, no. 6, pp. 1636±1644, 2014. 

- [7] ÐÐ, ªThe ªhorseº inside: Seeking causes behind the behaviors of music content analysis systems,º Comput. Entertain., vol. 14, no. 2, pp. 3:1±3:32, 2016. 

- [8] C. Molnar, Interpretable Machine Learning, 2nd ed., 2022. [Online]. Available: https://christophm.github. io/interpretable-ml-book 

- [9] T. Miller, ªExplanation in artificial intelligence: Insights from the social sciences,º Artif. Intell., vol. 267, pp. 1±38, 2019. 

- [10] Y. W. Teh, ªDirichlet process,º in Encyclopedia of Machine Learning and Data Mining, C. Sammut and G. I. Webb, Eds. Springer, 2017, pp. 361±370. 

- [11] Y. Qi, J. W. Paisley, and L. Carin, ªDirichlet process HMM mixture models with application to music analysis,º in Proceedings of the IEEE International Conference on Acoustics, Speech, and Signal Processing, 

ICASSP 2007, Honolulu, Hawaii, USA, April 15-20, 2007. IEEE, 2007, pp. 465±468. 

- [12] M. D. Hoffman, D. M. Blei, and P. R. Cook, ªContentbased musical similarity computation using the hierarchical dirichlet process,º in ISMIR 2008, 9th International Conference on Music Information Retrieval, Drexel University, Philadelphia, PA, USA, September 14-18, 2008, J. P. Bello, E. Chew, and D. Turnbull, Eds., 2008, pp. 349±354. 

- [13] ÐÐ, ªFinding latent sources in recorded music with a shift-invariant hdp,º in in International Conference on Digital Audio Effects (DAFx) (under review), 2009. 

- [14] M. Nakano, J. L. Roux, H. Kameoka, N. Ono, and S. Sagayama, ªInfinite-state spectrum model for music signal analysis,º in Proceedings of the IEEE International Conference on Acoustics, Speech, and Signal Processing, ICASSP 2011, May 22-27, 2011, Prague Congress Center, Prague, Czech Republic. IEEE, 2011, pp. 1972±1975. 

- [15] M. Nakano, Y. Ohishi, H. Kameoka, R. Mukai, and K. Kashino, ªBayesian nonparametric music parser,º in 2012 IEEE International Conference on Acoustics, Speech and Signal Processing, ICASSP 2012, Kyoto, Japan, March 25-30, 2012. IEEE, 2012, pp. 461±464. 

- [16] K. Yoshii and M. Goto, ªContinuous plsi and smoothing techniques for hybrid music recommendation,º in Proceedings of the 10th International Society for Music Information Retrieval Conference, ISMIR 2009, Kobe International Conference Center, Kobe, Japan, October 26-30, 2009, K. Hirata, G. Tzanetakis, and K. Yoshii, Eds. International Society for Music Information Retrieval, 2009, pp. 339±344. 

- [17] J. Wang, Y. Lee, Y. Chin, Y. Chen, and W. Hsieh, ªHierarchical dirichlet process mixture model for music emotion recognition,º IEEE Trans. Affect. Comput., vol. 6, no. 3, pp. 261±271, 2015. 

- [18] C. Wang, J. W. Paisley, and D. M. Blei, ªOnline variational inference for the hierarchical dirichlet process,º in Proceedings of the Fourteenth International Conference on Artificial Intelligence and Statistics, AISTATS 2011, Fort Lauderdale, USA, April 11-13, 2011, ser. JMLR Proceedings, G. J. Gordon, D. B. Dunson, and M. Dudík, Eds., vol. 15. JMLR.org, 2011, pp. 752± 760. 

- [19] Y. W. Teh, M. I. Jordan, M. J. Beal, and D. M. Blei, ªHierarchical dirichlet processes,º Journal of the American Statistical Association, vol. 101, no. 476, pp. 1566±1581, 2006. 

- [20] J. Kim, J. Urbano, C. C. S. Liem, and A. Hanjalic, ªOne deep music representation to rule them all? A comparative analysis of different representation learning strategies,º Neural Comput. Appl., vol. 32, no. 4, pp. 1067±1093, 2020. 

122 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

- [21] K. Choi, G. Fazekas, M. B. Sandler, and K. Cho, ªTransfer learning for music classification and regression tasks,º in Proceedings of the 18th International Society for Music Information Retrieval Conference, ISMIR 2017, Suzhou, China, October 23-27, 2017, S. J. Cunningham, Z. Duan, X. Hu, and D. Turnbull, Eds., 2017, pp. 141±149. 

- [22] S. Dieleman, P. Brakel, and B. Schrauwen, ªAudiobased music classification with a pretrained convolutional network,º in Proceedings of the 12th International Society for Music Information Retrieval Conference, ISMIR 2011, Miami, Florida, USA, October 2428, 2011, A. Klapuri and C. Leider, Eds. University of Miami, 2011, pp. 669±674. 

- [23] C. Bishop, Pattern Recognition and Machine Learning. Springer, January 2006. 

- [24] J. Sethuraman, ªA constructive definition of Dirichlet priors,º Statistica Sinica, vol. 4, pp. 639±650, 1994. 

- [25] J. Pitman, ªPoisson-dirichlet and gem invariant distributions for split-and-merge transformations of an interval partition,º Comb. Probab. Comput., vol. 11, no. 5, pp. 501±514, 2002. 

- [26] M. I. Jordan, Z. Ghahramani, T. S. Jaakkola, and L. K. Saul, ªAn introduction to variational methods for graphical models,º Mach. Learn., vol. 37, no. 2, pp. 183±233, 1999. 

- [27] D. M. Blei and M. I. Jordan, ªVariational inference for Dirichlet process mixtures,º Bayesian Analysis, vol. 1, no. 1, pp. 121 ± 143, 2006. 

- [28] M. D. Hoffman, D. M. Blei, and F. R. Bach, ªOnline learning for latent dirichlet allocation,º in Advances in Neural Information Processing Systems 23: 24th Annual Conference on Neural Information Processing Systems 2010. Proceedings of a meeting held 6-9 December 2010, Vancouver, British Columbia, Canada, J. D. Lafferty, C. K. I. Williams, J. Shawe-Taylor, R. S. Zemel, and A. Culotta, Eds. Curran Associates, Inc., 2010, pp. 856±864. 

- [29] J. Spijkervet and J. A. Burgoyne, ªContrastive learning of musical representations,º in Proceedings of the 22nd International Society for Music Information Retrieval Conference, ISMIR 2021, Online, November 7-12, 2021, J. H. Lee, A. Lerch, Z. Duan, J. Nam, P. Rao, P. van Kranenburg, and A. Srinivasamurthy, Eds., 2021, pp. 673±681. 

- [30] T. Bertin-Mahieux, D. P. Ellis, B. Whitman, and P. Lamere, ªThe million song dataset,º in Proceedings of the 12th International Conference on Music Information Retrieval (ISMIR 2011), 2011. 

- [31] J. Pons, O. Nieto, M. Prockup, E. M. Schmidt, A. F. Ehmann, and X. Serra, ªEnd-to-end learning for music audio tagging at scale,º in Proceedings of the 19th 

   - International Society for Music Information Retrieval Conference, ISMIR 2018, Paris, France, September 23-27, 2018, E. Gómez, X. Hu, E. Humphrey, and E. Benetos, Eds., 2018, pp. 637±644. 

- [32] J. Lee, J. Park, K. L. Kim, and J. Nam, ªSamplecnn: End-to-end deep convolutional neural networks using very small filters for music classification,º Applied Sciences, vol. 8, no. 1, 2018. 

- [33] G. Tzanetakis and P. R. Cook, ªMusical genre classification of audio signals,º IEEE Trans. Speech Audio Process., vol. 10, no. 5, pp. 293±302, 2002. 

- [34] C. Kereliuk, B. L. Sturm, and J. Larsen, ªDeep learning and music adversaries,º IEEE Trans. Multim., vol. 17, no. 11, pp. 2059±2071, 2015. 

- [35] E. Law, K. West, M. I. Mandel, M. Bay, and J. S. Downie, ªEvaluation of algorithms using games: The case of music tagging,º in Proceedings of the 10th International Society for Music Information Retrieval Conference, ISMIR 2009, Kobe International Conference Center, Kobe, Japan, October 26-30, 2009, K. Hirata, G. Tzanetakis, and K. Yoshii, Eds. International Society for Music Information Retrieval, 2009, pp. 387±392. 

- [36] J. Lee and J. Nam, ªMulti-Level and Multi-Scale Feature Aggregation Using Pretrained Convolutional Neural Networks for Music Auto-Tagging,º IEEE Signal Processing Letters, vol. 24, no. 8, pp. 1208±1212, Aug. 2017. 

- [37] D. Liang, R. G. Krishnan, M. D. Hoffman, and T. Jebara, ªVariational autoencoders for collaborative filtering,º in Proceedings of the 2018 World Wide Web Conference on World Wide Web, WWW 2018, Lyon, France, April 23-27, 2018, P. Champin, F. Gandon, M. Lalmas, and P. G. Ipeirotis, Eds. ACM, 2018, pp. 689±698. 

- [38] J. Bergstra and Y. Bengio, ªRandom search for hyperparameter optimization,º J. Mach. Learn. Res., vol. 13, pp. 281±305, 2012. 

- [39] M. Deshpande and G. Karypis, ªItem-based top-N recommendation algorithms,º ACM Trans. Inf. Syst., vol. 22, no. 1, pp. 143±177, 2004. 

- [40] K. Järvelin and J. Kekäläinen, ªCumulated gain-based evaluation of IR techniques,º ACM Trans. Inf. Syst., vol. 20, no. 4, pp. 422±446, 2002. 

- [41] C. J. van Rijsbergen, Information Retrieval. Butterworth, 1979. 

- [42] T. Fawcett, ªAn introduction to ROC analysis,º Pattern Recognit. Lett., vol. 27, no. 8, pp. 861±874, 2006. 

- [43] B. McFee, A. Metsai, M. McVicar, S. Balke, C. Thomé, C. Raffel, F. Zalkow, A. Malek, Dana, K. Lee, and et al., ªlibrosa/librosa: 0.9.1,º Feb 2022. 

123 

Proceedings of the 23rd ISMIR Conference, Bengaluru, India, December 4-8, 2022 

- [44] S. Böck and G. Widmer, ªMaximum filter vibrato suppression for onset detection,º in Proceedings of the 16th International Conference on Digital Audio Effects (DAFx-13), Maynooth, Ireland, September 2013. 

- [45] D. P. Ellis, Apr 2007, accessed: 2022-05-12. [Online]. Available: https://www.ee.columbia.edu/ ~dpwe/resources/matlab/chroma-ansyn 

- [46] K. Simonyan and A. Zisserman, ªVery deep convolutional networks for large-scale image recognition,º in 3rd International Conference on Learning Representations, ICLR 2015, San Diego, CA, USA, May 7-9, 2015, Conference Track Proceedings, Y. Bengio and Y. LeCun, Eds., 2015. 

- [47] T. Chen, S. Kornblith, M. Norouzi, and G. E. Hinton, ªA simple framework for contrastive learning of visual representations,º in Proceedings of the 37th International Conference on Machine Learning, ICML 2020, 13-18 July 2020, Virtual Event, ser. Proceedings of Machine Learning Research, vol. 119. PMLR, 2020, pp. 1597±1607. 

- [48] J. Nam, J. Herrera, M. Slaney, and J. O. S. III, ªLearning sparse feature representations for music annotation and retrieval,º in Proceedings of the 13th International Society for Music Information Retrieval Conference, ISMIR 2012, Mosteiro S.Bento Da Vitória, Porto, Portugal, October 8-12, 2012, F. Gouyon, P. Herrera, L. G. Martins, and M. Müller, Eds. FEUP Edições, 2012, pp. 565±570. 

- [49] J. W. Paisley, C. Wang, D. M. Blei, and M. I. Jordan, ªNested hierarchical dirichlet processes,º IEEE Trans. Pattern Anal. Mach. Intell., vol. 37, no. 2, pp. 256±270, 2015. 

124 

