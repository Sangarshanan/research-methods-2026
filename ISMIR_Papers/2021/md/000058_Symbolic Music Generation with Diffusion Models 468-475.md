---
paper_id: "000058"
year: 2021
title: "Symbolic Music Generation with Diffusion Models 468-475"
source_url: "https://archives.ismir.net/ismir2021/paper/000058.pdf"
---

# **SYMBOLIC MUSIC GENERATION WITH DIFFUSION MODELS** 

**Gautam Mittal**<sup>1</sup><sup>_⋆_</sup> **Jesse Engel**<sup>2</sup> **Curtis Hawthorne**<sup>2</sup> **Ian Simon**<sup>2</sup> 1 University of California, Berkeley 2 Google Brain 

gbm@berkeley.edu, {jesseengel,fjord,iansimon}@google.com 

## **ABSTRACT** 

Score-based generative models and diffusion probabilistic models have been successful at generating high-quality samples in a variety of continuous domains. However, due to their Langevin-inspired sampling mechanisms, their application to discrete symbolic music data has been limited. In this work, we present a technique for training diffusion models on symbolic music data by parameterizing the discrete domain in the continuous latent space of a pre-trained variational autoencoder. Our method is nonautoregressive and learns to generate sequences of latent embeddings through the reverse process and offers parallel generation with a constant number of iterative refinement steps. We show strong unconditional generation and posthoc conditional infilling results compared to autoregressive language models operating over the same continuous embeddings. 

## **1. INTRODUCTION** 

Denoising diffusion probabilistic models (DDPMs) [1, 2] are a promising new class of generative models that can synthesize comparably high-quality samples by learning to invert a diffusion process from data to Gaussian noise. Unlike many existing deep generative models, DDPMs sample through an iterative refinement process inspired by Langevin dynamics [3], which enables post-hoc conditioning of models trained unconditionally [4–7] for creative applications. 

Despite these exciting advances, DDPMs have not yet been applied to symbolic music generation because their iterative refinement sampling process is confined to continuous domains such as images [2] and audio [8,9]. Similarly, DDPMs cannot take advantage of the recent advances in modeling long-term structure [10–12] that use a two-stage process of modeling discrete tokens extracted by a separate low-level autoencoder. 

In this paper, we demonstrate that it is possible to overcome these limitations by training DDPMs on the continuous latents of a low-level variational autoencoder (VAE) 

> _⋆_ Work completed during an internship at Google Brain. 

> © G. Mittal, J. Engel, C. Hawthorne, and I. Simon. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). **Attribution:** G. Mittal, J. Engel, C. Hawthorne, and I. Simon, “Symbolic Music Generation with Diffusion Models”, in _Proc. of the 22nd Int. Society for Music Information Retrieval Conf.,_ Online, 2021. 

to generate long-form discrete symbolic music. Our key findings include: 

- High-quality unconditional sampling of discrete melodice sequences (1024 tokens) with DDPMs through iterative refinement of lower-level VAE latents. 

- DDPMs outperforming strong autoregressive baselines (TransformerMDN) in hierarchical modeling of continuous latents, partly due to a lack of teacher forcing and exposure bias during training. 

- Post-hoc conditional infilling of melodic sequences for creative applications. 

## **2. BACKGROUND** 

## **2.1 Denoising Diffusion Probabilistic Models** 

DDPMs [1, 2] are a class of generative models that define latents _x_ 1 _, ..., xN_ of the same dimensionality as the data _x_ 0 _∼ q_ ( _x_ 0). Diffusion models are comprised of a **forward process** and a **reverse process** . The **forward process** starts from the data _x_ 0 and iteratively adds Gaussian noise according to a fixed noise schedule for _N_ diffusion steps: 



<!-- Start of picture text -->
q ( xt|xt− 1) =  N ( xt ; � 1  − βtxt− 1 , βtI ) (1)<br>N<br><!-- End of picture text -->



<!-- Start of picture text -->
q ( x 1: N |x 0) = � q ( xt|xt− 1) (2)<br>t =1<br><!-- End of picture text -->

where _β_ 1 _, β_ 2 _, ..., βN_ is a noise schedule that converts the data distribution _x_ 0 into latent _xN_ . The choice of noise schedule has been shown to have important effects on sampling efficiency and quality [2,8]. 

The **reverse process** is defined by a Markov chain parameterized by _θ_ that iteratively refines latent point _xN ∼ N_ (0 _, I_ ) into data point _x_ 0. The learned transition probabilities are defined as, 



<!-- Start of picture text -->
pθ ( xt− 1 |xt ) =  N ( xt− 1;  µθ ( xt, t ) , σθ ( xt, t )) (3)<br><!-- End of picture text -->



<!-- Start of picture text -->
N<br><!-- End of picture text -->



<!-- Start of picture text -->
pθ ( x 0: N ) =  p ( xN ) � pθ ( xt− 1 |xt ) (4)<br>t =1<br><!-- End of picture text -->

where the objective is to gradually denoise samples at each reverse diffusion step _t_ . In practice, _σθ_ is set to an untrained time-dependent constant based on the noise schedule, and [2] found _σθ_ ( _xt, t_ ) = _σt_ = 1 _−_ 1 _−α_ ¯ _αt_ ¯ _−t_ 1<sup>_βt_tohave</sup> reasonable practical results, where _αt_ = 1 _− βt_ , and _α_ ¯ _t_ =<sup>�</sup><sup>_t_</sup> _i_ =1<sup>_αi_.</sup> 

468 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 



<!-- Start of picture text -->
Gaussian<br>t = N<br>Noise<br>Forward Process Reverse Process<br>t = 1<br>VAE<br>Posterior o t = 0<br>Deno i sng Di f usion Model<br>4 4 4 4 4<br>32 Continuous<br>z,<br>Latents<br>MusicVAE MusicVAE MusicVAE MusicVAE MusicVAE<br>1024 Discrete<br>Melody Tokens<br><!-- End of picture text -->

**Figure 1** . A diagram of our proposed framework. We use the pre-trained 2-bar melody MusicVAE [13] to embed discrete musical phrases (64 bars, 1024 tokens) into a sequence of continuous latent codes (32 latents, 512 dimensions each). These embeddings are used to train a diffusion model that iteratively adds noise such that after _N_ diffusion steps the input embeddings are distributed _N_ (0 _, I_ ). To sample from this model, we initialize Gaussian noise and use the reverse process to iteratively refine the noise samples into a sequence of embeddings from the data distribution. These generated embeddings are fed through the MusicVAE decoder to produce the final MIDI sequence. 

The training objective is to maximize the log likelihood of _pθ_ ( _x_ 0) = _pθ_ ( _x_ 0 _, ..., xN_ ) _dx_ 1: _N_ , but the intractability of this marginalization leads to the following evidence lower bound (ELBO): 



<!-- Start of picture text -->
E [log  pθ ( x 0)]  ≥ E q log pθ ( x 0: N )<br>q ( x 1: N |x 0)<br>  (5)<br>= E q log pθ ( xt− 1 |xt )<br>∑ q ( xt|xt− 1)<br>log  p ( xN ) + t≥ 1 <br><!-- End of picture text -->

Additionally, [2] observed that the forward process can = be computed for any step _t_ such that _q_ ( _xt|x_ 0) _N_ ( _xt_ ;<sup>_~~√~~_</sup> _<u>α</u>_ <u>¯</u> _tx_ 0 _,_ (1 _− α_ ¯ _t_ ) _I_ ), which can be viewed as a stochastic encoder. To simplify the above variational bound, [2] propose training on pairs of ( _xt, x_ 0) to learn to parameterize this process with a simple squared L2 loss. The following objective is simpler to train, resembles denoising score matching [5, 14] and was found to yield higher-quality samples: 



<!-- Start of picture text -->
L ( θ ) = E x 0 ,ϵ,t 三 ϵ − ϵθ ( √ α ¯ tx 0 + √ 1  − α ¯ tϵ, t ) 2 (6)<br><!-- End of picture text -->

where _t_ is sampled uniformly between 1 and _N_ , _ϵ ∼ N_ (0 _, I_ ), and _ϵθ_ is the learned diffusion model. [8] found that instead of conditioning on a discrete diffusion step _t_ , it was beneficial to sample a continuous noise level _~~√~~ α_ ¯ _∼_ U(<sup>_~~√~~_</sup> _<u>α</u>_ <u>¯</u> _t−_ 1 _<u>,</u>_<sup>_~~√~~_</sup> _<u>α</u>_ <u>¯</u> _t_ <u>)</u> where _t ∼_ U( _{_ 1 _, ..., N }_ ) and _α_ ¯0 = 1. 

We refer readers to Algorithms 2 and 3 based on [8] in our supplementary material<sup>1</sup> for the full training and sampling procedure. 

> 1 Supplementary material including additional implementation details, audio, and tables is available at https://goo.gl/magenta/ symbolic-music-diffusion-examples 

## **2.2 Variational Autoencoders** 

Variational autoencoders [15] are generative models that define _p_ ( _y, z_ ) = _p_ ( _y|z_ ) _p_ ( _z_ ) where _z_ is a learned latent code for data point _y_ . Additionally, the latent code is constrained such that _z_ is distributed according to prior _p_ ( _z_ ) where the prior is usually an isotropic Gaussian. The VAE is comprised of an encoder _qγ_ ( _z|y_ ) which models the approximate posterior _p_ ( _z|y_ ) and a decoder _pθ_ ( _y|z_ ) which models the conditional distribution of data _y_ given latent code _z_ . 

The training objective is to maximize the log likelihood of _pθ_ ( _x_ ) = _pθ_ ( _y|z_ ) _p_ ( _z_ ) _dz_ , but this marginalization is intractable, and we use the following variational bound maximized with _qγ_ ( _z|y_ ) as the approximate posterior: 



<!-- Start of picture text -->
E [log  pθ ( y|z )]  − KL( qγ ( z|y ) ||p ( z ))  ≤ log  p ( y ) (7)<br><!-- End of picture text -->

The flexible implementation of variational autoencoders allows them to learn representations over a wide variety of domains. Of particular interest to us are sequential autoencoders [13, 16] which use long short-term memory cells [17] to model temporal context in sequential data distributions. 

In practice, there is a trade-off between the quality of reconstructions and the distance between the approximate posterior _qγ_ ( _z|y_ ) and the Gaussian prior _p_ ( _z_ ). This makes sampling more difficult for VAEs with better reconstructions due to latent “holes" in the approximate posterior and is one of the primary shortcomings of these models. 

## **3. MODEL** 

A diagram and description of our multi-stage diffusion model is shown in Figure 1. We refer readers to the sup- 

469 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

plement for full implementation details. 

## **3.1 Architecture** 

Our model learns to generate discrete sequences of notes (known as MIDI) by first training a VAE with parameters _γ_ on the sequences and then training a diffusion model to capture the temporal relationships among the _k_ VAE latents. Sequence VAEs such as MusicVAE are difficult to train on long sequences [13], which we overcome by pairing the short 2-bar MusicVAE model with a diffusion model capable of modeling dependencies between _k_ = 32 latents, thus modeling 64 bars in total. 

**MusicVAE embeddings:** Each musical phrase is a sequence of one-hot vectors with 16 quantized steps per measure and the vocabulary contains 90 possible tokens (1 note on + 1 note off + 88 pitches). We then parameterize each 2-bar phrase using the pre-trained 2-bar melody MusicVAE [13] and generate a sequence of continuous latent embeddings _z_ 1 _, ..., zk_ to parameterize an entire sequence. The MusicVAE model employs bidirectional recurrent neural networks as an encoder and autoregressive decoding as shown in Figure 4 in the supplement. As we use the pretrained model from the original work, full model details can be found in [13]. After encoding each 2-measure phrase into a latent _z_ embedding, we perform linear feature scaling such that the domain of each embedding is [ _−_ 1 _,_ 1]. This ensures consistently scaled inputs starting from the isotropic Gaussian latent _xN_ for the diffusion model. 

**Transformer diffusion model:** Our network _ϵθ_ ( _xt,_<sup>_~~√~~_</sup> _α_ ¯) : R<sup>_k×_42</sup> _×_ R _→_ R<sup>_k×_42</sup> is a transformer [18] where _k_ = 32 is the length of each sequence of 42dimensional preprocessed latent embeddings. The unperturbed data distribution used to train the diffusion model is _x_ 0 = [ _z_ 1 _, ..., zk_ ]. The network contains an initial fully-connected layer that projects the embeddings into a 128-dimensional space, followed by _L_ = 6 encoder layers each with _H_ = 8 self-attention heads and a residual fully-connected layer. All self-attention and fully-connected layers use layer normalization [19]. The output of the encoder is fed to _K_ = 2 noise-conditioned residual fully-connected layers which generate the reverse process output. Each fully-connected layer contains 2048 neurons. We use a 128-dimensional sinusoidal positional encoding similar to [18] where _j_ is the position index of a latent input embedding: 



<!-- Start of picture text -->
− 4 × 0 − 4 × 63<br>ω = 10 63 j, ...,  10 63 j ej = [sin( ω ) ,  cos( ω )] (8)<br>� �<br><!-- End of picture text -->

This positional encoding _e_ 1 _, e_ 2 _, ..., ek_ is added to inputs _xt_ before being fed through the transformer encoder layers allowing the model to capture the temporal context of the continuous inputs. 

**Noise schedule and conditioning:** As described in both the original diffusion model framework [2] and in [8], we use an additional sinusoidal encoding to condition the diffusion model on a continuous noise level during training and sampling. This noise encoding is identical to the positional encoding described above but with the frequency of 

each sinusoid scaled by 5000 to account for the updated domain. We use feature-wise linear modulation [20] to generate _γ_ (scale) and _ξ_ (shift) parameters given a noise encoding and apply the transformation _γφ_ + _ξ_ to the output _φ_ of each layer normalization block in each residual layer, allowing for effective conditioning of the diffusion model. Our model uses a linear noise schedule with _N_ = 1000 steps and _β_ 1 = 10<sup>_−_6</sup> and _βN_ = 0 _._ 01. 

## **3.2 Unconditional Generation** 

In the unconditional generation task, the goal is to produce samples that exhibit long-term structure. Because of our multi-stage approach, this works even in the scenario where the KL divergence between the marginal posterior _qγ_ ( _z_ ) and the Gaussian prior is quite large because the diffusion model accurately captures the structure of the latent space therefore improving the sample quality. Additionally, we extend the underlying VAE to samples longer than what it was trained to model by using the diffusion model to predict sequences of latent embeddings and attempt to generate unconditional samples with coherent patterns across a large number of measures. 

## **3.3 Infilling** 

One of the benefits of using a sampling process that iteratively refines noise into data samples is that the trajectory of the reverse process can be steered and arbitrarily conditioned without the need for retraining the diffusion model. In creative domains, this post-hoc conditioning is especially useful for artists without the computational resources to modify or re-train deep models for new tasks. We demonstrate the power of diffusion modeling applied to music with conditional infilling of latent embeddings using an unconditionally trained diffusion model. 

The infilling procedure extends the sampling procedure described in Algorithm 3 by incorporating information from a partially occluded sample _s_ . At each step of sampling, we diffuse the fixed regions of _s_ with the forward process _q_ ( _st|s_ ) = _N_ ( _st_ ;<sup>_~~√~~_</sup> _<u>α</u>_ <u>¯</u> _ts,_ (1 _− α_ ¯ _t_ ) _I_ ) and use a mask _m_ to add the diffused fixed regions to the updated sample _xt−_ 1. The final output _x_ 0 will be a version of _s_ with the occluded regions inpainted by the reverse process. 

We refer readers to Algorithm 1 for the modified sampling procedure that allows for post-hoc conditional infilling. 

**Algorithm 1** Infilling 

**Input:** mask _m_ , sample _s_ , _N_ steps, _β_ 1 _, ..., βN xN ∼N_ (0 _, I_ ) **for** _t_ = _N, ...,_ 1 **do** _ϵ_ 1 _, ϵ_ 2 _∼N_ (0 _, I_ <u>) if</u> _t >_ 1, else _ϵ_ 1 = _ϵ_ 2 = 0 _y_ =<sup>_~~√~~_</sup> _<u>α</u>_ <u>¯</u> _ts_ +<sup>_~~√~~_</sup> 1 _− α_ ¯ _tϵ_ 1 if _t >_ 1, else _s_ <u>1 1</u> _−αt xt−_ 1 = _~~√~~_ _<u>αt</u>_ � _xt −_ _~~√~~_ 1 _−α_ ¯ _t_<sup>_ϵθ_(</sup><sup>_xt,_</sup><sup>_~~√~~_</sup> _<u>α</u>_ <u>¯</u> _t_ <u>)�</u> + _σtϵ_ 2 _xt−_ 1 = _xt−_ 1 _⊙_ (1 _− m_ ) + _y ⊙ m_ **end for return** _x_ 0 

470 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

## **4. METHODS** 

## **4.1 Data** 

We use the Lakh MIDI Dataset (LMD) [21] for all experiments. The dataset contains over 170,000 MIDI files with 99% of those files used for training and the remaining used for validation. We extracted 988,893 64-bar monophonic sequences for training and 11,295 for validation from the provided MIDI files. Each sequence was encoded into 32 continuous latent embeddings using MusicVAE. We set the softmax temperature for MusicVAE to 0.001 for decoding generated embeddings in all experiments. A diagram of the MusicVAE architecture used is shown in the supplementary material. 

## **4.2 Autoregressive Baseline** 

We compare our model to an autoregressive transformer with a mixture density output layer [22] and train on the same dataset as the diffusion model. To ensure a fair comparison, we use the same architecture as our diffusion model with _L_ = 6, _H_ = 8, and _K_ = 2 with 2048 neurons for each fully-connected layer. The mixture density layer outputs a mixture of 100 Gaussians to ensure sufficient mode coverage. In total, our baseline model has 38M trainable parameters. While the model is the same as the diffusion model (25.58M trainable parameters) up until the output layer, the autoregressive model has more parameters due to the much larger output layer. We refer to this model as TransformerMDN. 

## **4.3 Training** 

All models were trained using Adam [23] with default parameters. We trained our diffusion model for 500K steps on a single NVIDIA Tesla V100 GPU for 6.5 hours using a learning rate of 10<sup>_−_3</sup> annealed with a decay rate of 0.98 every 4000 steps and batch size 64. Unlike the diffusion model, which is non-autoregressive, we train TransformerMDN with teacher forcing. We use a batch size of 128, learning rate 3 _×_ 10<sup>_−_4</sup> , and train for 250K steps on a single NVIDIA Tesla V100 GPU for 6.5 hours. 

We used the open-source implementation of MusicVAE written in TensorFlow [24] and the publicly available 2-bar melody checkpoints trained on LMD. We trained our diffusion and baseline models<sup>2</sup> with JAX [25] and Flax [26]. 

the piece. Within each 4-measure frame, we compute the mean and variance of both pitch, which captures melodic similarity, and duration, which captures rhythmic similarity. These statistics specify a Gaussian PDF for pitch and duration for each frame ( _pP_ ( _k_ ) _, pD_ ( _k_ )). We compute the Overlapping Area (OA) [27] of adjacent frames ( _k_ , _k_ + 1) where each frame’s statistics are modeled as _N_ ( _µ_ 1 _, σ_ 1<sup>2)</sup> and _N_ ( _µ_ 2 _, σ_ 2<sup>2), respectively:</sup> 



<!-- Start of picture text -->
OA( k, k  + 1) = 1  − erf + erf (9)<br>� c √  − 2 σµ 1 2 1 � � c √  − 2 σµ 2 2 2 �<br><!-- End of picture text -->

for both pitch (OA _P_ ) and duration (OA _D_ ), where erf is the Gauss error function and _c_ is the point of intersection between Gaussian PDFs with _µ_ 1 _< µ_ 2. For a set of MIDI samples, we infer the _Consistency_ and _Variance_ from the mean ( _µ_ OA) and variance ( _σ_ OA<sup>2)respectivelyofOAag-</sup> gregated over all adjacent frames. We then use these aggregate values to compute the normalized relative similarity of pitch and duration consistency and variance to the training set (GT): 



<!-- Start of picture text -->
Consistency = max(0 ,  1  − |µ OA  − µGT | )<br>µGT<br>(10)<br>OA − σ GT 2 |<br>V ariance  = max(0 ,  1  − |σ 2 )<br>σGT 2<br><!-- End of picture text -->

We clip _Consistency_ and _Variance_ such that samples with _µOA_ or _σOA_<sup>2with greater than 100% percent error from the</sup> ground truth are considered to have zero relative similarity. 

## **4.5 Latent Space Evaluation** 

We evaluate the similarity of latent embeddings generated by each of our models using the Fréchet distance (FD) [28] and Maximum Mean Discrepancy (MMD) [29] with a polynomial kernel, which are popular evaluation metrics in the generative modeling literature. These metrics measure the distance between the models’ continuous output distributions and the original data distribution in latent space. It is important to note that this metric does not measure long-term temporal consistency or quality of produced sequences and only measures the quality of the intermediate continuous representation before the final sequence is generated using the MusicVAE decoder. 

## **5. RESULTS** 

## **4.4 Framewise Self-similarity Metric** 

To evaluate the statistical similarity between our model’s qualitative output and the original training sequences, we present a metric that captures local self-similarity patterns across generated melodic sequences. Inspired by the statistical similarity evaluation described in [27], we evaluate our models with a modified framewise Overlapping Area (OA) metric. 

We use a sliding 4-measure window with 2-measure hop size to capture local pitch and duration statistics across 

> 2 Our implementation is available at https://github.com/ magenta/symbolic-music-diffusion 

## **5.1 Unconditional Generation** 

To evaluate unconditional sample quality, we compare batches of 1000 samples (32 latents each) generated by our proposed diffusion model with random draws from the training and test sets. We compare against a set of baseline generators including TransformerMDN, the independent _N_ (0 _, I_ ) MusicVAE prior, and spherical interpolation [30] between two MusicVAE embeddings at the start and end of an example from the test set. 

As seen in Table 1, the diffusion model quantitatively produces samples most similar to the training data according to the relative framewise overlapping area metrics for 

471 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 



<!-- Start of picture text -->
Example A Example B<br>72<br>Pihh (a) Pihh (al)<br>48<br>60<br>100 120 100 120<br>(MII)<br>pitch ( pitch (MIDI)<br>48 60<br>120 100 120<br>72<br>pitch (60 P i h (l)<br>60<br>100 120<br>96 108<br>84 96<br>84<br>72 72<br>60 60<br>(iICIh (ia)48 48<br>36 36<br>24<br>120<br>time (sec) time (sec)<br>Original<br>DDPM<br>Interpolation<br>Prior<br><!-- End of picture text -->

**Figure 2** . Example piano rolls of infilling experiments. For each example (A, B) the first and last 256 melody tokens are held constant, and the interior 512 tokens are filled in by the model (dashed red box). Even qualitatively, it is visually apparent that the diffusion model (second row) produces notes with a consistency and variance similar to the original data (first row), while the latent interpolation (third row) is too repetitive, and sampling independently from the prior (last row) produces outputs with too much variety and lack of local coherence. 

|Setting||Uncon|ditional|||Infil|iling||
|---|---|---|---|---|---|---|---|---|
|Quantity|Pit|ch|Dura|tion|Pit|ch|Dur|ation|
|Metric|C|Var|C|Var|C|Var|C|Var|
|Train Data|1.00|1.00|1.00|1.00|1.00|1.00|1.00|1.00|
|Test Data|1.00|0.96|1.00|0.91|1.00|0.96|1.00|0.91|
|Diffusion|**0.99**|**0.90**|**0.96**|**0.92**|**0.97**|**0.87**|**0.97**|**0.80**|
|Autoregression|0.93|0.68|0.93|0.76|-|-|-|-|
|Interpolation|0.85|0.23|0.91|0.34|0.94|0.78|0.96|**0.80**|
|_N_(0_, I_)Prior|0.84|0.19|0.90|0.67|0.89|0.19|0.94|0.54|



**Table 1** . Framewise self-similarity of consistency (C) and variance (Var), as defined in Equation 10, for note pitch and duration. For both unconditional sampling and infilling tasks, the diffusion model produces samples most similar to the real data. For diffusion samples, we use _N_ = 1000 sampling steps with _β_ 1 = 10<sup>_−_6</sup> and _βN_ = 0 _._ 01. For the TransformerMDN baseline we sample with a temperature of 1.0, meaning we sampled directly from the logits of mixture density layer. Absolute values of overlap area can be found in Table 2 in our supplementary material. 

note pitch and duration. The diffusion model outperforms TransformerMDN, which is challenged by modelling the relatively high-dimensional continuous latents autoregressively, even with a mixture of Gaussians output. The autoregressive models are also trained with teacher forcing that results in exposure bias, leading to divergence from the data distribution during sampling. This is reflected in the lower pitch and duration consistency and higher variance 

in the absolute overlapping area numbers seen in Supplemental Table 2. Additionally, the diffusion model is able to capture the joint dependencies of the sequences better because it learns to model all latents simultaneously as opposed to autoregressively. Note that the Gaussian prior also suffers from low consistency and high variance, due to lack of temporal dependencies, while the interpolated samples conversely suffer from low variance and too much consistency due to high repetition. 

Table 3 in our supplement presents latent space evaluations of our generated samples. The TransformerMDN outperformed all other models, likely due to the Gaussian mixture prior on its output layer whereas the diffusion model must learn the output distribution from scratch. Furthermore, the latent space metrics are limited by assumptions about the latent manifold distribution and are unable to fully capture the detail of the entire space, further highlighting the necessity of our quantitative framewise selfsimilarity metrics and qualitative evaluations. 

Figure 3 helps us to further understand the iterative refinement process by showing the improvement in sample quality as a function of iterative refinement time for both latent space and framewise self-similarity metrics. Interestingly, latent metrics improve steadily, while consistency similarity starts fairly high, and variance similarity only emerges at the end of refinement. We refer the reader to the supplementary material for extended visual and audio 

472 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 



<!-- Start of picture text -->
30<br>20<br>10<br>0<br>40<br>20<br>0<br>1.0<br>0.5<br>0.0<br>1.0<br>0.5<br>0.0<br>1.0<br>0.5<br>0.0<br>1.0<br>0.5<br>0.0<br>0 200 400 600 800 1000<br>Timestep<br>FD<br>MMD<br>Pitch<br> Consistency<br>Pitch<br> Variance<br>Duration<br> Consistency<br>Duration  Variance<br><!-- End of picture text -->

**Figure 3** . Sample quality improvement during iterative refinement. Latent space and framewise metrics evaluated at different stages of unconditional sampling. The metrics improve as the iterative refinement process progresses. We plot the means and standard deviations for 1000 samples. 

samples of the generated sequences from each model<sup>3</sup> . 

## **5.2 Infilling** 

To probe the diffusion model’s ability to perform post-hoc conditional generation, we remove the middle 32 measures (16 embeddings) and generate new embeddings following Algorithm 1 by conditioning on the first and last 8 embeddings. As in the unconditional setting, we compare to interpolation and independent samples from the prior. 

Figure 2 visualizes the task by plotting the resulting note sequences for two different examples. Even qualitatively, it is visually apparent that the diffusion model produces notes with a consistency and variance similar to the original data. Latent interpolation is very consistent but unrealistically repetitive, and sampling independently from the prior produces a sequence with extremely large variance that is inconsistent in both pitch and duration. 

The quantitative evaluations in Table 1 back up these observations. Similar to the unconditional generation task, the diffusion model outperforms the baselines in both consistency and variance similarity. We do not include the au- 

toregressive baseline because it is unable to condition on the final 8 embeddings. 

## **6. RELATED WORK** 

**Multi-stage learning:** Several models have achieved longterm structure by first modeling some intermediate representation and then using that to guide the final generative process. Wave2Midi2Wave [31] uses a transformer to generate MIDI-like symbolic data and then a WaveNet [32] to synthesize that symbolic data into audio. Jukebox [11] and DALL-E [12] use similar approaches for text-conditioned generative music audio and image models. There has also been work investigating the extension of a singlemeasure VAE to multiple measures by using an autoregressive LSTM with a mixture density output layer [33], similar to TransformerMDN. 

**Iterative refinement:** [34] use an orderless NADE with blocked Gibbs sampling to iteratively rewrite musical harmonies based on surrounding context. [35] use a gradientbased sampler combined with a restricted Boltzmann machine to generate polyphonic piano music. Similarly, [36] investigated the use of a score-based generative model [5] to generate Bach chorales with annealed Langevin dynamics. A key distinction between our method and prior work is the use of a VAE to parameterize the discrete space of musical notes for improved generation with a DDPM while previous methods have performed iterative refinement in the discrete space directly. 

**Conditional sampling from unconditional models:** We build on top of the breadth of material that investigate steering generation in the latent space of an unconditionally trained generative model [37–40]. Most similar to our work is [4,37,41] which train an additional model on top of a pre-trained variational autoencoder to steer generation in the latent space of that autoencoder. Our approach builds on top of this by not only improving sampling and generation of the underlying autoencoder but also extending generation to sequences much longer than those used to train the VAE. We also use a diffusion model to refine generation and provide conditional infilling while the works mentioned primarily used conditional GANs and VAEs to extend the underlying autoencoder for a single latent embedding as opposed to a sequence of latent embeddings. 

## **7. CONCLUSION** 

We have proposed and demonstrated a multi-stage generative model comprised of a low-level variational autoencoder with continuous latents modeled by a higher-level diffusion model. This approach enables using diffusion models on discrete data, and as priors for modeling longterm structure in multi-stage systems. We demonstrate that this model is useful for symbolic music generation, both in unconditional generation and conditional infilling. Future work will include extending this approach to other discrete data such as text, and exploring a greater array of approaches for post-hoc conditioning in creative applications. 

3 https://goo.gl/magenta/symbolic-musicdiffusion-examples 

473 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

## **8. ACKNOWLEDGEMENTS** 

We thank Anna Huang, Carrie Cai, Sander Dieleman, Doug Eck and the rest of the Magenta team for helpful discussions, feedback, and encouragement. 

## **9. REFERENCES** 

- [1] J. Sohl-Dickstein, E. Weiss, N. Maheswaranathan, and S. Ganguli, “Deep unsupervised learning using nonequilibrium thermodynamics,” in _Proceedings of the 32nd International Conference on Machine Learning_ , ser. Proceedings of Machine Learning Research, F. Bach and D. Blei, Eds., vol. 37. Lille, France: PMLR, 07–09 Jul 2015, pp. 2256–2265. [Online]. Available: http://proceedings.mlr.press/v37/ sohl-dickstein15.html 

- [2] J. Ho, A. Jain, and P. Abbeel, “Denoising diffusion probabilistic models,” in _Advances in Neural Information Processing Systems_ , H. Larochelle, M. Ranzato, R. Hadsell, M. F. Balcan, and H. Lin, Eds., vol. 33. Curran Associates, Inc., 2020, pp. 6840–6851. [Online]. Available: https://proceedings.neurips.cc/paper/2020/file/ 4c5bcfec8584af0d967f1ab10179ca4b-Paper.pdf 

- [3] M. Welling and Y. W. Teh, “Bayesian learning via stochastic gradient langevin dynamics,” in _Proceedings of the 28th International Conference on International Conference on Machine Learning_ , ser. ICML’11. Madison, WI, USA: Omnipress, 2011, p. 681–688. 

- [4] J. Engel, M. Hoffman, and A. Roberts, “Latent constraints: Learning to generate conditionally from unconditional generative models,” in _International Conference on Learning Representations_ , 2018. [Online]. Available: https://openreview.net/forum?id=Sy8XvGb0- 

- [5] Y. Song and S. Ermon, “Generative modeling by estimating gradients of the data distribution,” in _Advances in Neural Information Processing Systems_ , 2019, pp. 11 895–11 907. 

- [6] ——, “Improved techniques for training score-based generative models,” in _Advances in Neural Information Processing Systems 33: Annual Conference on Neural Information Processing Systems 2020, NeurIPS 2020, December 6-12, 2020, virtual_ , H. Larochelle, M. Ranzato, R. Hadsell, M. Balcan, and H. Lin, Eds., 2020. 

- [7] Y. Du and I. Mordatch, “Implicit generation and modeling with energy based models,” in _Advances in Neural Information Processing Systems_ , H. Wallach, H. Larochelle, A. Beygelzimer, F. d'AlchéBuc, E. Fox, and R. Garnett, Eds., vol. 32. Curran Associates, Inc., 2019. [Online]. Available: https://proceedings.neurips.cc/paper/2019/file/ 378a063b8fdb1db941e34f4bde584c7d-Paper.pdf 

- [8] N. Chen, Y. Zhang, H. Zen, R. J. Weiss, M. Norouzi, and W. Chan, “Wavegrad: Estimating gradients for waveform generation,” in _International Conference on Learning Representations_ , 2021. [Online]. Available: https://openreview.net/forum?id=NsMLjcFaO8O 

- [9] Z. Kong, W. Ping, J. Huang, K. Zhao, and B. Catanzaro, “Diffwave: A versatile diffusion model for audio synthesis,” in _International Conference on Learning Representations_ , 2021. [Online]. Available: https://openreview.net/forum?id=a-xFK8Ymz5J 

- [10] A. Razavi, A. van den Oord, and O. Vinyals, “Generating diverse high-fidelity images with vq-vae2,” in _Advances in Neural Information Processing Systems_ , H. Wallach, H. Larochelle, A. Beygelzimer, F. d'Alché-Buc, E. Fox, and R. Garnett, Eds., vol. 32. Curran Associates, Inc., 2019. [Online]. Available: https://proceedings.neurips.cc/paper/2019/ file/5f8e2fa1718d1bbcadf1cd9c7a54fb8c-Paper.pdf 

- [11] P. Dhariwal, H. Jun, C. Payne, J. W. Kim, A. Radford, and I. Sutskever, “Jukebox: A generative model for music,” _arXiv preprint arXiv:2005.00341_ , 2020. 

- [12] A. Ramesh, M. Pavlov, G. Goh, S. Gray, M. Chen, R. Child, V. Misra, P. Mishkin, G. Krueger, S. Agarwal, and I. Sutskever, “Dall·e: Creating images from text,” _OpenAI blog_ , 2021. [Online]. Available: https://openai.com/blog/dall-e 

- [13] A. Roberts, J. Engel, C. Raffel, C. Hawthorne, and D. Eck, “A hierarchical latent vector model for learning long-term structure in music,” in _Proceedings of the 35th International Conference on Machine Learning_ , ser. Proceedings of Machine Learning Research, J. Dy and A. Krause, Eds., vol. 80. PMLR, 10–15 Jul 2018, pp. 4364–4373. [Online]. Available: http://proceedings.mlr.press/v80/roberts18a.html 

- [14] P. Vincent, “A connection between score matching and denoising autoencoders,” _Neural computation_ , vol. 23, no. 7, pp. 1661–1674, 2011. 

- [15] D. P. Kingma and M. Welling, “Auto-encoding variational bayes,” in _Second International Conference on Learning Representations_ , 2014. 

- [16] S. R. Bowman, L. Vilnis, O. Vinyals, A. M. Dai, R. Jozefowicz, and S. Bengio, “Generating sentences from a continuous space,” 2016. 

- [17] S. Hochreiter and J. Schmidhuber, “Long short-term memory,” _Neural computation_ , vol. 9, no. 8, pp. 1735– 1780, 1997. 

- [18] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. Kaiser, and I. Polosukhin, “Attention is all you need,” 2017. 

- [19] J. L. Ba, J. R. Kiros, and G. E. Hinton, “Layer normalization,” _arXiv preprint arXiv:1607.06450_ , 2016. 

474 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

- [20] E. Perez, F. Strub, H. De Vries, V. Dumoulin, and A. Courville, “Film: Visual reasoning with a general conditioning layer,” in _Proceedings of the AAAI Conference on Artificial Intelligence_ , vol. 32, no. 1, 2018. 

- [21] C. Raffel, “Learning-based methods for comparing sequences, with applications to audio-to-midi alignment and matching,” Ph.D. dissertation, Columbia University, 2016. 

- [22] C. M. Bishop, “Mixture density networks,” 1994. 

- [23] D. P. Kingma and J. Ba, “Adam: A method for stochastic optimization,” _arXiv preprint arXiv:1412.6980_ , 2014. 

- [24] M. Abadi, P. Barham, J. Chen, Z. Chen, A. Davis, J. Dean, M. Devin, S. Ghemawat, G. Irving, M. Isard _et al._ , “Tensorflow: A system for large-scale machine learning,” in _12th {USENIX} symposium on operating systems design and implementation ({OSDI} 16)_ , 2016, pp. 265–283. 

- [25] J. Bradbury, R. Frostig, P. Hawkins, M. J. Johnson, C. Leary, D. Maclaurin, G. Necula, A. Paszke, J. VanderPlas, S. Wanderman-Milne, and Q. Zhang, “JAX: composable transformations of Python+NumPy programs,” 2018. [Online]. Available: http://github. com/google/jax 

- [26] J. Heek, A. Levskaya, A. Oliver, M. Ritter, B. Rondepierre, A. Steiner, and M. van Zee, “Flax: A neural network library and ecosystem for JAX,” 2020. [Online]. Available: http://github.com/google/flax 

- [27] K. Choi, C. Hawthorne, I. Simon, M. Dinculescu, and J. Engel, “Encoding musical style with transformer autoencoders,” in _International Conference on Machine Learning_ . PMLR, 2020, pp. 1899–1908. 

- [28] M. Heusel, H. Ramsauer, T. Unterthiner, B. Nessler, and S. Hochreiter, “Gans trained by a two time-scale update rule converge to a local nash equilibrium,” 2018. 

- [29] A. Gretton, K. M. Borgwardt, M. J. Rasch, B. Schölkopf, and A. Smola, “A kernel two-sample test,” _Journal of Machine Learning Research_ , vol. 13, no. 25, pp. 723–773, 2012. [Online]. Available: http://jmlr.org/papers/v13/gretton12a.html 

- [30] T. White, “Sampling generative networks,” _arXiv preprint arXiv:1609.04468_ , 2016. 

- [31] C. Hawthorne, A. Stasyuk, A. Roberts, I. Simon, C.-Z. A. Huang, S. Dieleman, E. Elsen, J. Engel, and D. Eck, “Enabling factorized piano music modeling and generation with the MAESTRO dataset,” in _International Conference on Learning Representations_ , 2019. [Online]. Available: https://openreview.net/forum?id=r1lYRjC9F7 

- [32] A. v. d. Oord, S. Dieleman, H. Zen, K. Simonyan, O. Vinyals, A. Graves, N. Kalchbrenner, A. Senior, and K. Kavukcuoglu, “Wavenet: A generative model for raw audio,” _arXiv preprint arXiv:1609.03499_ , 2016. 

- [33] H. Jhamtani and T. Berg-Kirkpatrick, “Modeling selfrepetition in music generation using generative adversarial networks,” 2019. 

- [34] C.-Z. A. Huang, T. Cooijmans, A. Roberts, A. Courville, and D. Eck, “Counterpoint by convolution,” in _Proceedings of ISMIR 2017_ , 2017. [Online]. Available: https://ismir2017.smcnus.org/wpcontent/uploads/2017/10/187_Paper.pdf 

- [35] S. Lattner, M. Grachten, and G. Widmer, “Imposing higher-level structure in polyphonic music generation using convolutional restricted boltzmann machines and constraints,” _arXiv preprint arXiv:1612.04742_ , 2016. 

- [36] E. Zhang and R. Sirohi, “Generative modeling of bach chorales by gradient estimation,” 2020. [Online]. Available: https://www.ekzhang.com/assets/ pdf/Generative_Music_Modeling.pdf 

- [37] A. Nguyen, J. Clune, Y. Bengio, A. Dosovitskiy, and J. Yosinski, “Plug & play generative networks: Conditional iterative generation of images in latent space,” in _Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition_ , 2017, pp. 4467–4477. 

- [38] N. Jaques, J. Engel, D. Ha, F. Bertsch, R. Picard, and D. Eck, “Learning via social awareness: improving sketch representations with facial feedback,” in _International Conference on Learning Representations_ , 2018, workshop Track. [Online]. Available: https://arxiv.org/abs/1802.04877 

- [39] A. Jahanian, L. Chai, and P. Isola, “On the" steerability" of generative adversarial networks,” _arXiv preprint arXiv:1907.07171_ , 2019. 

- [40] S. Dathathri, A. Madotto, J. Lan, J. Hung, E. Frank, P. Molino, J. Yosinski, and R. Liu, “Plug and play language models: A simple approach to controlled text generation,” _arXiv preprint arXiv:1912.02164_ , 2019. 

- [41] M. Dinculescu, J. Engel, and A. Roberts, Eds., _MidiMe: Personalizing a MusicVAE model with user data_ , 2019. 

- [42] M. D. Hoffman and M. J. Johnson, “Elbo surgery: yet another way to carve up the variational evidence lower bound.” 

- [43] A. Alemi, B. Poole, I. Fischer, J. Dillon, R. A. Saurous, and K. Murphy, “Fixing a broken elbo,” in _International Conference on Machine Learning_ . PMLR, 2018, pp. 159–168. 

475 

