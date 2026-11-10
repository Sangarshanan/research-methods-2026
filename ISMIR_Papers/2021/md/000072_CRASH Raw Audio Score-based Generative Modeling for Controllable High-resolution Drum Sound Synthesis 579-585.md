---
paper_id: "000072"
year: 2021
title: "CRASH: Raw Audio Score-based Generative Modeling for Controllable High-resolution Drum Sound Synthesis 579-585"
source_url: "https://archives.ismir.net/ismir2021/paper/000072.pdf"
---

# **CRASH: RAW AUDIO SCORE-BASED GENERATIVE MODELING FOR CONTROLLABLE HIGH-RESOLUTION DRUM SOUND SYNTHESIS** 

## **Simon Rouard** 

Sony CSL - CentraleSupélec simon.rouard@student-cs.fr 

## **Gaëtan Hadjeres** 

Sony CSL 

gaetan.hadjeres@sony.com 

### **ABSTRACT** 

In this paper, we propose a novel score-base generative model for unconditional raw audio synthesis. Our proposal builds upon the latest developments on diffusion process modeling with stochastic differential equations, which already demonstrated promising results on image generation. We motivate novel heuristics for the choice of the diffusion processes better suited for audio generation, and consider the use of a conditional U-Net to approximate the score function. While previous approaches on diffusion models on audio were mainly designed as speech vocoders in medium resolution, our method termed CRASH (Controllable Raw Audio Synthesis with High-resolution) allows us to generate short percussive sounds in 44.1kHz in a controllable way. Through extensive experiments, we showcase on a drum sound generation task the numerous sampling schemes offered by our method (unconditional generation, deterministic generation, inpainting, interpolation, variations, class-conditional sampling) and propose the _class-mixing_ sampling, a novel way to generate “hybrid” sounds. Our proposed method offers flexible generation capabilities with lighter and easier-to-train models than GAN-based methods. 

### **1. INTRODUCTION AND RELATED WORK** 

After multiple works in the spectral domain [1, 2], deep generative models in the waveform domain have recently shown the ability to produce high fidelity results with different methods: autoregressive [3, 4], flow-based [5], energy-based [6] or based on Generative Adversarial Networks [7]. 

In the task of generating drum sounds in the waveform domain, GAN-based approaches have been explored in [7], [8] and [9]. Interactive sound design is often a major motivation behind these works: in [10] the authors use Variational Autoencoders (VAE) in order to generate spectrograms of drums apply a principal component analysis on the latent space of the VAE in order to explore the drum timbre space. One of the disadvantages of this model is 

> © Simon Rouard, Gaëtan Hadjeres. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). **Attribution:** Simon Rouard, Gaëtan Hadjeres, “CRASH: Raw Audio Score-based Generative Modeling for Controllable High-resolution Drum Sound Synthesis”, in _Proc. of the 22nd Int. Society for Music Information Retrieval Conf.,_ Online, 2021. 

that the reconstruction of the sounds by the VAE tends to be blurry. In [11], the authors use a VQ-VAE2 [12] in order to perform inpainting on instrument sound spectrograms. 

Score-based generative models [13–16] propose a different approach to generative modeling, which consists in estimating the gradient of noise-corrupted data logdensities (score function): by iteratively denoising a sampled noise, these approaches obtained promising results, but mainly on image data. 

To this day, only two score-based generative models in the waveform domain have been published [17, 18] and they are mostly focused on the task of neural vocoding with conditioning on a mel-spectrogram. In [17], the authors achieved the task of generating audio with an unconditioned model trained on the speech command dataset [19]. The inference scheme of [17] does not provide a flexible sampling scheme because it is trained on a fixed discrete noise schedule whereas [18] is trained on a continuous scalar indicating the noise level. 

In the image domain, [16] generalizes the works of [14, 15, 20] by framing the noise corruption procedure as stochastic differential equation. 

Score-based generative models offer the following advantages over GAN-based approaches: 

- Training time is reduced and training is more stable since there is only one network to train. 

- Class-conditioning generation can be achieved by training a classifier a posteriori, which lets us train a model only one time. 

- Data can be mapped to a latent space without the need to train an additional encoder compared to GANs [21], which makes the interpolation between two given input data readily available with only one model. 

These properties alleviate us to search for directions in the latent space as in [22] or to directly hardcode conditional features in the architecture as in [23]. This easily controllable latent space permits sound design applications. One downside of score-based models compared to GANs is their higher inference times to generate new samples. 

In this work, we extend the approach of [16] and propose CRASH (Controllable Raw Audio Synthesis with High-resolution), a score-based generative model adapted to the waveform domain. On a drum sound dataset, the numerous capabilities offered by this architecture allows for 

579 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

musically-relevant sound design applications. Our contributions are the following: 

- A score-based model for unconditional generation that can achieve high fidelity 44.1 kHz drum sounds directly in the waveform domain, 

- The use of a noise-conditioned U-Net to estimate the score function, 

- A novel _class-mixing_ sampling scheme to generate "hybrid" sounds. 

- Experimental and practical insights about the choice of the stochastic differential equation used to corrupt the data. 

with the following initial conditions _m_ (0) = 1 and _σ_<sup>2</sup> (0) = 0. The solutions for _m_ ( _t_ ) and _σ_ ( _t_ ) are : 



<!-- Start of picture text -->
m ( t ) =  e 0 t f ( s ) ds<br>σ 2 ( t ) =  e 0 t 2 f ( s ) ds 0 t g 2( u ) e 0 u − 2 f ( s ) ds du. (4)<br><!-- End of picture text -->

In [16], the authors define three types of SDEs which are presented in Tab. 1. For the Variance Preserving (VP) 

||_f_(_t_)|_g_(_t_)|
|---|---|---|
|VP|_−_<sup>1</sup><br>2<sup>_β_(</sup><sup>_t_)</sup>|_β_(_t_)|
|VE|0|_d_[_σ_<sup>2</sup>(_t_)]<br>_dt_|
|sub-VP|_−_<sup>1</sup><br>2<sup>_β_(</sup><sup>_t_)</sup>|_β_(_t_)(1_−e_<sup>_−_2</sup><br>_t_<br>0 <sup>_β_(</sup><sup>_s_)</sup><sup>_ds_</sup>)|



**Table 1** . Functions used in the VP, VE and sub-VP SDEs 

### **2. BACKGROUND** 

### **2.1 Score Based Modelling through Stochastic Differential Equations** 



<!-- Start of picture text -->
x(0) Forward SDE<br>x(0) Backward SDE x(T)<br><!-- End of picture text -->

**Figure 1** . Illustration of the noising and denoising processes of a kick sound with a VP schedule 

### _2.1.1 Forward Process_ 

Let _p_ data be a data distribution. Diffusion models consist in progressively adding noise to the data distribution to transform it into a known distribution from which we can sample from as shown in Fig. 1. In [16], the authors formalize this noising process as the following **forward** Stochastic Differential Equation (SDE): 



<!-- Start of picture text -->
d x  =  f ( t ) x dt  +  g ( t ) d w (1)<br><!-- End of picture text -->

where _f_ ( _t_ ) is a continuous negative function from [0 _, T_ ] _→_ R<sup>_−_</sup> , _g_ ( _t_ ) a continuous positive function from [0 _, T_ ] _→_ R<sup>+</sup> , and **w** is a standard Wiener process. Such approach can be understood as a continuous-time generalization of Denoising Diffusion Probabilistic Models (DDPMs) [14, 20] and denoising Score Matching with Langevin Dynamics (SMLD) [15]. For **x** (0) _∼ p_ data, the transition kernel of Eq. 1 is given by a normal distribution: 



<!-- Start of picture text -->
pt ( x ( t )  |  x (0)) =  N ( x ( t );  m ( t ) x (0) , σ 2 ( t ) I ) , (2)<br><!-- End of picture text -->

where _m_ ( _t_ ) and _σ_ ( _t_ ) follow the system: 



<!-- Start of picture text -->
dmdt =  f ( t ) m ( t )<br>dσdt 2 ( t ) = 2 f ( t ) σ 2 ( t ) +  g 2 ( t ) (3)<br><!-- End of picture text -->

and sub-Variance Preserving (sub-VP) schedules, _m_ ( _T_ ) _≈_ 0 and _σ_ ( _T_ ) _≈_ 1 which means that the original data distribution is transformed into a distribution close to a standard normal distribution i.e. _pT ≈N_ ( **0** _,_ **I** ). For the Variance Exploding (VE), _σ_<sup>2</sup> ( _T_ ) _≫ m ≈_ 1 which means that the original data is not discernable at _t_ = _T_ and that _pT ≈N_ ( **0** _, σ_<sup>2</sup> ( _T_ ) **I** ). 

### _2.1.2 Generation with the Reverse Process_ 

In order to sample from the data distribution, we can sample **x** _T ∼ pT_ and apply the associated reverse time SDE [24] given by: 



<!-- Start of picture text -->
d x  = [ f ( t ) x  − g 2 ( t ) ∇ x  log  pt ( x )] dt  +  g ( t ) d ˜w (5)<br><!-- End of picture text -->

where **˜w** is a standard Wiener process running backwards from T to 0 and _dt_ is an infinitesimal negative timestep. 

It means that by knowing _∇_ **x** log _pt_ ( **x** ), we can use a discretization of Eq. 5 to sample **x** (0) from _p_ 0 = _p_ data. = In practice, the score function _s_ ( **x** ( _t_ ) _, σ_ ( _t_ )) _∇_ **x** log _pt_ ( **x** ) is intractable and it is approximated by a neural network _sθ_ ( **x** ( _t_ ) _, σ_ ( _t_ )) parameterized by _θ_ . In order to train the network, [13] shows that for any t, minimizing 



<!-- Start of picture text -->
E pt ( x ) ∥sθ ( x , σ ( t ))  −∇ x  log  pt ( x ) ∥ 2 2 (6)<br><!-- End of picture text -->

is equivalent to minimizing 



<!-- Start of picture text -->
E ∥sθ ( x , σ ( t ))  −∇ x  log  pt ( x ( t )  |  x (0)) ∥ 2 2 (7)<br><!-- End of picture text -->

where the expectation is over **x** (0) _∼ p_ data, **x** ( _t_ ) _∼ pt_ ( **x** ( _t_ ) _|_ **x** (0)), and the latter distribution is given by Eq. 2. 

Now, in order to train the network for all _t ∈_ [0 _, T_ ] we consider the following mixture of Eq. 7 losses over all noise levels: 



<!-- Start of picture text -->
L ( θ ) = E λ ( t ) sθ ( x ( t ) , σ ( t ))  −∇ x ( t ) log  pt ( x ( t )  |  x (0)) 22 (8)<br><!-- End of picture text -->

where we sample _t ∼_ [0 _, T_ ], **x** (0) _∼ p_ data, **x** ( _t_ ) _∼ pt_ ( **x** ( _t_ ) _|_ **x** (0)) and where _λ_ ( _t_ ) is a weighting function. 

580 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

In [14–16], _λ_ ( _t_ ) is empirically set such that _λ_ ( _t_ )<sup>_−_1</sup> _∝_ E 二 _∇_ **x** ( _t_ ) log _pt_ ( **x** ( _t_ ) _|_ **x** (0)) 22<sup>_∝σ_2(</sup><sup>_t_)</sup><sup>_−_1whilein[25]</sup> the authors show that the maximum likelihood estimator is obtained with _λ_ ( _t_ ) = _g_<sup>2</sup> ( _t_ ) in _L_ ( _θ_ ). 

The training procedure is described in Alg. 1, where we reparameterize our neural network as _ϵθ_ ( **x** ( _t_ ) _, σ_ ( _t_ )) := _−σ_ ( _t_ ) _sθ_ ( **x** ( _t_ ) _, σ_ ( _t_ )) in order to estimate _ϵ_ . 

### **Algorithm 1** Training <u>procedure</u> 



<!-- Start of picture text -->
while  Training  do<br>Sample  t ∼U ([0 , T ]) ,  x (0)  ∼ p data , ϵ ∼N ( 0 ,  I )<br>Compute  x ( t ) =  m ( t ) x (0) +  σ ( t ) ϵ<br>2<br>√ λ ( t )<br>Gradient descent on  ∇θ σ ( t ) [ ϵθ ( x ( t ) , σ ( t ))  − ϵ ]<br>2<br>end while<br><!-- End of picture text -->

Once the network is trained, a N-step discretization of the **backward** SDE is done in order to unconditionally generate samples. This process is described in Alg. 2, it is non-deterministic since we obtain various sounds by starting from the same sample **x** ( _T_ ). 

### **Algorithm 2** Sampling via SDE 



<!-- Start of picture text -->
Choose  N , sample  x N ∼N ( 0 , σ 2 ( T ) I )<br>for  i  =  N − 1 , ...,  0  do<br>ti =  T N i , fi =  f ( ti ) , gi =  g ( ti ) , σi =  σ ( ti )<br>x i = (1  − fi N +1 ) x i +1  − Nσgi 2 + i +11 ϵθ ( x i +1 , σi +1)<br>if  i >  0  then<br>Sample  z i +1 ∼N ( 0 ,  I )<br>x i =  x i  + gi +1<br>√ N z i +1<br>end if<br>end for<br><!-- End of picture text -->

### **2.2 Deterministic Sampling via Score based Ordinary Differential Equation** 

As mentioned in [16], for any SDE, there exists a corresponding deterministic process which satisfies an ordinary differential equation (ODE): 



<!-- Start of picture text -->
d x  = [ f ( t ) x  − 1 (9)<br>2 g 2( t ) ∇ x  log  pt ( x )] dt<br><!-- End of picture text -->

This defines a flow _φ_<sup>_t_</sup> such that the marginal distributions _φ_<sup>_t_</sup> _∗_<sup>(</sup><sup>_p_data) are identical to the ones obtained by applying the</sup> SDE of Eq. 1. This mapping is interesting because it provides a latent representation for each **x** _∼ p_ data. 

The procedure of sampling via the N-step discretization of the ODE is described in Alg. 3. 

### **Algorithm 3** Sampling via ODE 



<!-- Start of picture text -->
Choose  N , sample  x N ∼N ( 0 , σ 2 ( T ) I )<br>for  i  =  N − 1 , ...,  0  do<br>ti =  T N i , fi =  f ( ti ) , gi =  g ( ti ) , σi =  σ ( ti )<br>x i = (1  − fi N +1 ) x i +1  − 2 Nσgi 2 + i 1+1 ϵθ ( x i +1 , σi +1)<br>end for<br><!-- End of picture text -->

### **2.3 Inpainting** 

Let’s imagine that we don’t like the attack of a kick (or any other part of a sound), the method of inpainting permits us to regenerate the desired part. In order to do that, we apply a reverse-time SDE or ODE discretization to an isotropic Gaussian and fix the part that we want to keep (with the associated noise corruption) after each denoising timestep. As presented in section 6, we obtain very diverse and coherent results. 

### **2.4 Interpolations** 

The flexibility of SDEs and ODEs allows to compute interpolations between sounds. In fact, there exists an infinity of latent spaces indexed by _t ∈_ [0 _, T_ ]. We present here two types of interpolations: ODE interpolation in the latent space of isotropic Gaussians and SDE interpolation in any t-indexed latent space. 



<!-- Start of picture text -->
x1 SOSBSIS x2<br>Forward ODE Forward ODE<br>↓€1 ↓€2<br>Reconstruction of Compute Reconstruction of<br>x1 spherical x2<br>kπinterpolationkπ<br>cos( 20)e1 + sin( )∈2<br>k =0, 1, . ., 10<br>Backward ODE Backward ODE<br>9 interpolations between the two sounds<br><!-- End of picture text -->

**Figure 2** . Interpolation of two sounds via Forward and Backward ODE 

### _2.4.1 ODE interpolation in the latent space of isotropic Gaussians_ 

Let _ϵ_ 1 and _ϵ_ 2 be two samples from a standard normal distribution of R<sup>_L_</sup> where _L_ is our space dimension and 0 _≤ λ ≤_ 1. We consider the spherical interpolation _ϵλ_ = _λϵ_ 1 + _~~√~~_ 1 _− λ_<sup>2</sup> _ϵ_ 2 and then apply the ODE sampling to it. We choose a spherical interpolation in order to preserve a variance close to 1 for _ϵλ_ . 

Morever, if we want to interpolate two sounds **x** 1 and **x** 2, we can apply the Forward ODE in order to obtain the corresponding latent codes _ϵ_ 1 and _ϵ_ 2, apply the desired spherical interpolation and then apply an ODE sampling. 

### _2.4.2 ODE interpolation in a t-indexed latent space_ 

In [17], the authors perform a linear interpolation between two sounds at a corresponding intermediate t-indexed latent space before applying Denoising Diffusion Probabilistic Model (DDPM is the discrete equivalent of a VP SDE). We adapt the method to the continuous framework with 

581 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

SDE and ODE. Here again, the interpolation can be done between two t-indexed latent codes or between sounds corrupted using the transition kernel of Eq. 2. 

### **2.5 Class-Conditional sampling with a classifier** 

For any class _y_ , we can train a noise-conditioned classifier on corrupted data **x** ( _t_ ). As a consequence, the output of the classifier gives us _pt_ ( _y |_ **x** ( _t_ )) for each class _y_ . We can use automatic-differentiation to differentiate this quantity and by the Bayes Formula, since _p_ ( _y_ ) is constant for each class _y_ , we have the following formula: 



<!-- Start of picture text -->
∇ x  log  pt ( x  | y ) =  ∇ x  log  pt ( x )+ ∇ x  log  pt ( y |  x ) (10)<br><!-- End of picture text -->

As a consequence, we can generate samples of one class by solving this reverse time SDE: 



<!-- Start of picture text -->
d x  = [ f ( t ) x  − g 2 ( t ) ∇ x  log  pt ( x  | y )] dt  +  g ( t ) d ˜w (11)<br><!-- End of picture text -->

This approach is flexible since it only requires to train a noise-conditioned classifier: there is no need to design and train a class-conditional score-based model as done in [17]. 

### **3. A DISCUSSION ABOUT CHOOSING THE RIGHT SDE: A GENERALIZATION OF THE SUB-VP SDE** 

In this section _T_ = 1. 

### **3.1 About the relation relation between** _m_ ( _t_ ) **and** _σ_ ( _t_ ) 

The VP SDE is the continuous version of the Denoising Diffusion Probabilistic Model (DDPM) used in [14] [17] [18]. One of the main features of this model is that the mean coefficient _m_ ( _t_ ) of the perturbation kernel is linked to the standard deviation _σ_ ( _t_ <u>) (or</u> noise-level) by the following equation _m_ ( _t_ ) = 1 _− σ_<sup>2</sup> ( _t_ ). Because the decrease of _m_ is relatively small on a large range of values for _σ_ , this means that a (very-noisy) drum sound audio must begin to appear after only a few steps of denoising during the sampling algorithm. (For instance if _σ_ = 0 _._ 8, _m_ = 0 _._ 6). We believe that this fast decay of the signal-tonoise ratio can be detrimental when sampling with Alg. 2 and 3. Moreover, without mentioning this fact, in [16] the authors introduce the sub-VP SDE which is characterized by the following formula _m_ ( _t_ ) = 1 _− σ_ ( _t_ ). The authors obtained state of the art results on the image generation task which corroborates our intuition that _m_ might be too large for values of _σ_ near 1 tends to be right. 

In this work, we explore the four relations between _m_ and _σ_ plotted in Fig. 3. The blue one corresponds to the VP SDE, the yellow is the sub-VP SDE and the green and red ones corresponds to a generalization of the sub-VP schedule. In Tab. 2 we write the functions _f_ ( _t_ ) and _g_ ( _t_ ) for each of these 4 relation. For the rest of the paper we take the convention _f_ ( _t_ ) := _−_<sup><u>1</u></sup> 2<sup>_β_(</sup><sup>_t_)inordertocomparetheVP</sup> and sub-VP schedules with ours. 



<!-- Start of picture text -->
1.0<br>0.8<br>m<br>0.6 should not<br>be too high<br>m in this zone<br>0.4<br>0.2 m = √1 � σ (VP)m = √1 �σ (sub-VP)<br>m = 1 � σ<br>0.0 m = (1 � σ)²<br>0.0 0.2 0.4 σ 0.6 0.8 1.0<br><!-- End of picture text -->

**Figure 3** . Different relations between _m_ and _σ_ 

|_m_-_σ_relation|_f_(_t_)|_g_(_t_)|
|---|---|---|
|_m_=<br>_~~√~~_<br>1_−σ_<sup>2 </sup>(VP)|_−_<sup>1</sup><br>2<sup>_β_(</sup><sup>_t_)</sup>|_β_(_t_)|
|_m_= <sup>_~~√~~_</sup><br>1_−σ_(sub-VP)|_−_<sup>1</sup><br>2<sup>_β_(</sup><sup>_t_)</sup>|_β_(_t_)(1_−e_<sup>_−_2</sup><br>_t_<br>0 <sup>_β_(</sup><sup>_s_)</sup><sup>_ds_</sup>)<br>V<br>∫|
|_m_= 1_−σ_(sub-VP 1-1)|_−_<sup>1</sup><br>2<sup>_β_(</sup><sup>_t_)</sup>|_β_(_t_)(1_−e_<sup>_−_1</sup><br>2<br>_t_<br>0 <sup>_β_(</sup><sup>_s_)</sup><sup>_ds_</sup>)<br>~~-∫~~|
|_m_= (1_−σ_)<sup>2 </sup>(sub-VP 1-2)|_−_<sup>1</sup><br>2<sup>_β_(</sup><sup>_t_)</sup>|_β_(_t_)(1_−_<sup>3</sup><br>2<sup>_e−_1</sup><br>2<br>_t_<br>0 <sup>_β_(</sup><sup>_s_)</sup><sup>_ds_ </sup>+ <sup>1</sup><br>2<sup>_e−_</sup><br>_t_<br>0 <sup>_β_(</sup><sup>_s_)</sup><sup>_ds_</sup>)<br>∫|



**Table 2** . Functions used in the VP, sub-VP and generalized sub-VP SDEs. 

### **3.2 Choosing the right functions for the SDE** 

Choosing a particular relation between _m_ and _σ_ , imposes a relation between _g_ and _β_ . The remaining free parameter is the function _β_ , needed to fully define the SDE. In [16], the authors use a linear schedule for _β_ ( _t_ ) because it is the continuous generalization of DDPMs. As presented in Fig. 4, this choice leads to a _σ_ ( _t_ ) function that rapidly grows to its maximum. In [26], the authors mention this fast growing _σ_ function as a potential shortcoming and propose a smoother function (the green one in Fig. 4). 



<!-- Start of picture text -->
1.0<br>0.8<br>0.6<br>σ<br>0.4<br>0.2 VP (Song)sub-VP (Song)<br>VP-like (Nichol)<br>0.0 ours<br>0.0 0.2 0.4 t 0.6 0.8 1.0<br><!-- End of picture text -->

**Figure 4** . Different choices for the _σ_ ( _t_ ) function 

Our approach differs from [16] in that the definition of our SDE is motivated by choosing a relatively smooth increasing function _σ_ ( _t_ ) such as _σ_ (0) = 0 and _σ_ (1) = 1 _− ϵ_ (where _ϵ_ is a small constant), together with a _m_ - _σ_ relation, from which all other quantities can be computed as shown in Tab. 2. If the two approaches are equivalent, we believe that these quantities are more interpretable. In the regime of a small number of discretization steps, a slow increasing 

582 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

function may induce less approximation errors. For our experiments we propose _σ_ ( _t_ ) =<sup><u>1</u></sup> 2<sup>[1</sup><sup>_−_cos((1</sup><sup>_−s_)</sup><sup>_πt_)] with</sup> _s_ = 0 _._ 006 which is the red plot in Fig. 4. We also sample t in the interval [ _η,_ 1] during the training where _η_ is chosen such that _σ_ ( _η_ ) = 10<sup>_−_4</sup> because 10<sup>_−_4</sup> is imperceptible. 

### **4. CLASS-MIXING SAMPLING WITH A CLASSIFIER** 

Drum classes are not perfectly distinct. For instance, the dataset contains drum sounds that are percussive enough to be seen as kicks but also sufficiently brilliant to be seen as snares and some kicks are combined with a hi-hat sound. We observe that our classifier (at the noise-level _σ_ = 0) sometimes outputs a mixed classes such as [0.3, 0.3, 0.4] and that it aligns well with our feeling when hearing the sound. 

We introduce the Class-Conditional sampling to a mixture of classes: For a given noisy sound **x** ( _t_ ), the vector _∇_ **x** ( _t_ ) log _pt_ ( _yi |_ **x** ( _t_ )) points out to the direction of the class _yi_ in the noisy t-indexed latent space. Now, assuming that we have N classes ( _yi_ ) _i_ =1 _,. . . ,N_ , let ( _λi_ ) _i_ =1 _,. . . ,N_ be positive real numbers such as ∑ _Ni_ =1<sup>_λi_=1,wedefinea</sup> mixture of classes that we note _{_ ( _yi, λi_ ) _}_ and the associated vector: 

|σ(t)|€estimated<br>x(t) = m(t)x(0) + σ(t)e<br>→FiLM→5 x 1 Conv (32)<br>3 x 1 Conv (32)|
|---|---|
|RFF embedding (64)<br>MLP|→FiLM→DBlock (128, /2)→Cat→UBlock (128, x2)<br>→FiLM→DBlock (128, /2)→Cat→UBlock (128, x2)<br>→FiLM→DBlock (256, /3)→ Cat→UBlock (128, x3)<br>→FiLM→DBlock (512, /5)→Cat→UBlock (256, x5)<br>→FiLM→DBlock (512, /5)→ Cat→UBlock (512, x5)|



**Figure 5** . Architecture of the Conditioned U-Net 

### **5.2 Noise conditioned classifier** 

Our noise-conditioned classifier closely mimics the architecture of our Conditioned U-Net presented in in Sect. 5.1. The classifier is composed of a succession of FiLMconditioned DBlocks followed by a projection layer and a softmax. 

### **6. EXPERIMENTS AND RESULTS** 



<!-- Start of picture text -->
N<br>∇ x  log  pt ( { ( yi, λi ) } |  x ) := λi∇ x  log  pt ( yi |  x )<br>∑<br>i =1<br>(12)<br><!-- End of picture text -->

In practice, we put this term in equation 10 in replacement of the last term and use equation 11 to sample class-mixed audios. It gives us interesting results with a great palette of sounds. 

### **5. ARCHITECTURE** 

### **5.1 Conditioned U-Net** 

Our model architecture is a conditioned U-Net [27], originally proposed for source separation. It takes two inputs: the noise level _σ_ ( _t_ ) and the noisy audio **x** ( _t_ ). The noiselevel is encoded by Random Fourier Features [28] followed by a Multi-Layer Perceptron. The noisy audio goes into FiLM-conditioned [29] Downsampling Blocks. Then, the signal goes into Upsampling Blocks that receive skip connections from the DBlocks of same levels. The output of the network is the estimated noise _ϵ_ estimated. 

This bears similarities with the architecture from [17] which has a similar succession of blocks with dilated convolutions but no downsampling or upsampling layers, which makes it slow in terms of computation. The architecture from [18] has a U-Net-like shape [30], but heavily depends on the spectrogram conditioning and relies on a different noise-conditioning scheme. The _σ_ -conditioned U-Net architecture seems to retain advantages from both approaches and is particularly suited for unconditional generation (see Fig. 5). 

Code is available at: https://github.com/ simonrouard/CRASH 

### **6.1 Dataset** 

For this work, we use an internal non-publicly available dataset of drum sounds which has also been used in [8]. It is composed of approximately 300.000 one-shot kick, snare and cymbal sounds in equal proportions. The samples have a sample rate of 44.1kHz and are recorded in mono. We restricted and padded the audio to 21.000 timesteps because most sounds last less than 0.5 second. We used 90% of the dataset in order to train our model. 

### **6.2 Models and process** 

We evaluate the influence of _σ_ ( _t_ ) and four _m_ - _σ_ schedules. The training of the network is done with a learning rate of 2 _._ 10<sup>_−_4</sup> and the Adam optimizer. In parallel, smoothed weights with exponential moving average (EMA) with a rate of 0.999 are computed and saved at each step. For each model, the network is trained for about 120 epochs and the weights are saved each 8 epochs. We generated drum sounds with the regular weights and with the EMA weights and we observed the same phenomenon as in [31]: for the regular weights the quality of the sounds is not necessarily increasing with the training time whereas the EMA weights provide better and more homogeneous Fréchet Audio Distance [32] (FAD) during training<sup>1</sup> . 

> 1 We use the original implementation [32] available at https: //github.com/google-research/google-research/ tree/master/frechet_audio_distance 

583 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

After generating 2700 sounds for each checkpoint of each model, we choose the best checkpoints and generate 27000 drum sounds for each. It takes 12 hours to generate 27000 drum sounds on a Nvidia RTX-3090 GPU with an ODE or SDE schedule of 400 steps and batches of 180 sounds per generation (maximum memory capacity). 

### **6.3 Quantitative Results** 

We report the FAD (lower is better) between the 27000 generated drum sounds and the test set for each unconditional generation with SDE and ODE (with a discretization of 400 steps) in the table 6.3. The cos schedule refers to the function _σ_ ( _t_ ) =<sup><u>1</u></sup> 2<sup>[1</sup><sup>_−_cos((1</sup><sup>_−s_)</sup><sup>_πt_)] (the red one in</sup> Fig. 4) and the exp schedule corresponds to the function _σ_ ( _t_ ) = _~~√~~_ 1 _− e_<sup>_−_0</sup><sup>_._1</sup><sup>_t−_9</sup><sup>_._95</sup><sup>_t_2</sup> used in [16] (the blue one in Fig. 4). 

|Schedule|SDE 400 steps|ODE 400 steps|
|---|---|---|
|VP expschedule(as in[16])|4.30|4.03|
|VP cos schedule|2.32|**1**_._**79**|
|sub-VP cos schedule|2.46|2.07|
|sub-VP 1-1 cos schedule|2.62|**1**_._**73**|
|sub-VP 1-2 cos schedule|2.56|**1**_._**75**|



**Table 3** . FAD comparison (lower is better) 

Choosing a smoother _σ_ function indeed improves the FAD of the generated sounds for a fixed number of discretization steps. 

By using the classifier that we trained, we observe that all models generate kicks, snares and cymbals in equal proportions but the generated samples are less diverse than in the original dataset. For a fixed number of discretization steps, we think that the cos schedule performs better because it is smoother than the exp schedule. 

### **6.4 Interactive sound design** 

Audio samples for all experiments described in this section can be heard on the accompanying website: https:// crash-diffusion.github.io/crash/. 

it with a SDE discretization from t to 0. We obtain then variations of the original sound. 

### _6.4.3 Inpainting_ 

We can also perform inpainting on a sound in order to regenerate any desired part. We show this method on Fig. 6 where we regenerate 6 endings of a snare sound. 



**Figure 6** . Six Inpaintings on the end of a snare sound 

This provides an innovative way to generate a variety of plausible sounds starting with the same attack. 

### _6.4.4 Class-Conditioning and Class-Mixing with a Classifier_ 

We trained a noise-conditioned classifier on the 3 classes (kick, snare, cymbal) and used it to generate classconditioned and class-mixing generation. Once again, by using the latent representation of a sound we can regenerate it (via ODE) with control on its "kickiness, snariness or cymbaliness". 



<!-- Start of picture text -->
M<br><!-- End of picture text -->

**Figure 7** . Transformation of a cymbal into a kick via classconditioning ODE 

### _6.4.1 Interpolations_ 

The relative lack of diversity of the unconditional generation is not dramatic since the model can still perform interactive sound design by modifying existing samples from the dataset. In order to do that, we apply the forward ODE to an existing sound and obtain its corresponding noise in the latent space of isotropic Gaussians. As presented in Fig. 7, we can perform spherical combinations on the latent codes and apply the backward ODE to obtain interpolations. Moreover the reconstructed sounds (at the left and right of the schema) are accurate. 

### _6.4.2 Obtaining Variations of a Sound by Noising it and Denoising it via SDE_ 

Let’s take a sound **x** (0). We can noise it at a desired noise level _σ_ ( _t_ ) via **x** ( _t_ ) = _m_ ( _t_ ) **x** (0) + _σ_ ( _t_ ) _ϵ_ and then denoise 

### **7. CONCLUSION** 

We presented CRASH, a score-based generative model for the generation of raw audio based on the latest developments in modeling diffusion processes via SDEs. We proposed novel SDEs, well-suited to drum sound generation with high-resolution, together with an efficient architecture for estimating the score function. We showcased how the many controllable sampling schemes offered new perspectives for interactive sound design. In particular, our proposed _class-mixing_ strategy allows the controllable creation of convincing "hybrid" sounds that would be hard to obtain with conventional means. We hope that these new methods will contribute to enrich the workflow of music producers. 

584 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

### **8. REFERENCES** 

- [1] S. Vasquez and M. Lewis, “Melnet: A generative model for audio in the frequency domain,” 2019. 

- [2] J. Engel, K. K. Agrawal, S. Chen, I. Gulrajani, C. Donahue, and A. Roberts, “Gansynth: Adversarial neural audio synthesis,” 2019. 

- [3] A. van den Oord, S. Dieleman, H. Zen, K. Simonyan, O. Vinyals, A. Graves, N. Kalchbrenner, A. Senior, and K. Kavukcuoglu, “Wavenet: A generative model for raw audio,” 2016. 

- [4] S. Mehri, K. Kumar, I. Gulrajani, R. Kumar, S. Jain, J. Sotelo, A. Courville, and Y. Bengio, “Samplernn: An unconditional end-to-end neural audio generation model,” 2017. 

- [5] R. Prenger, R. Valle, and B. Catanzaro, “Waveglow: A flow-based generative network for speech synthesis,” 2018. 

- [6] A. A. Gritsenko, T. Salimans, R. van den Berg, J. Snoek, and N. Kalchbrenner, “A spectral energy distance for parallel speech synthesis,” 2020. 

- [7] C. Donahue, J. McAuley, and M. Puckette, “Adversarial audio synthesis,” 2019. 

- [8] J. Nistal, S. Lattner, and G. Richard, “Drumgan: Synthesis of drum sounds with timbral feature conditioning using generative adversarial networks,” 2020. 

- [9] J. Drysdale, M. Tomczak, and J. Hockman, “Adversarial synthesis of drum sounds,” 2020. 

- [10] C. Aouameur, P. Esling, and G. Hadjeres, “Neural drum machine: An interactive system for real-time synthesis of drum sounds,” in _International Conference on Computational Creativity_ , 2019. 

- [11] T. Bazin, G. Hadjeres, P. Esling, and M. Malt, “Spectrogram inpainting for interactive generation of instrument sounds,” _arXiv preprint arXiv:2104.07519_ , 2021. 

- [12] A. Razavi, A. v. d. Oord, and O. Vinyals, “Generating diverse high-fidelity images with vq-vae-2,” _NeurIPS_ , 2019. 

- [13] P. Vincent, “A connection between score matching and denoising autoencoders,” pp. 1661–1674, 2011. 

- [14] J. Ho, A. Jain, and P. Abbeel, “Denoising diffusion probabilistic models,” 2020. 

- [15] Y. Song and S. Ermon, “Generative modeling by estimating gradients of the data distribution,” in _Advances in Neural Information Processing Systems_ , 2019, pp. 11 895–11 907. 

- [16] Y. Song, J. Sohl-Dickstein, D. P. Kingma, A. Kumar, S. Ermon, and B. Poole, “Score-based generative modeling through stochastic differential equations,” 2021. 

- [17] Z. Kong, W. Ping, J. Huang, K. Zhao, and B. Catanzaro, “Diffwave: A versatile diffusion model for audio synthesis,” 2021. 

- [18] N. Chen, Y. Zhang, H. Zen, R. J. Weiss, M. Norouzi, and W. Chan, “Wavegrad: Estimating gradients for waveform generation,” 2020. 

- [19] P. Warden, “Speech commands: A dataset for limitedvocabulary speech recognition,” 2018. 

- [20] J. Sohl-Dickstein, E. A. Weiss, N. Maheswaranathan, and S. Ganguli, “Deep unsupervised learning using nonequilibrium thermodynamics,” 2015. 

- [21] O. Tov, Y. Alaluf, Y. Nitzan, O. Patashnik, and D. Cohen-Or, “Designing an encoder for stylegan image manipulation,” _CoRR_ , vol. abs/2102.02766, 2021. [Online]. Available: https://arxiv.org/abs/2102. 02766 

- [22] E. Härkönen, A. Hertzmann, J. Lehtinen, and S. Paris, “Ganspace: Discovering interpretable gan controls,” 2020. 

- [23] M. Mirza and S. Osindero, “Conditional generative adversarial nets,” 2014. 

- [24] B. D. O. Anderson, “Reverse-time diffusion equation models,” pp. 313–326, 1982. 

- [25] C. Durkan and Y. Song, “On maximum likelihood training of score-based generative models,” 2021. 

- [26] A. Nichol and P. Dhariwal, “Improved denoising diffusion probabilistic models,” 2021. 

- [27] G. Meseguer-Brocal and G. Peeters, “Conditionedu-net: Introducing a control mechanism in the u- net for multiple source separations,” _ArXiv_ , vol. abs/1907.01277, 2019. 

- [28] M. Tancik, P. P. Srinivasan, B. Mildenhall, S. Fridovich-Keil, N. Raghavan, U. Singhal, R. Ramamoorthi, J. T. Barron, and R. Ng, “Fourier features let networks learn high frequency functions in low dimensional domains,” 2020. 

- [29] E. Perez, F. Strub, H. de Vries, V. Dumoulin, and A. Courville, “Film: Visual reasoning with a general conditioning layer,” 2017. 

- [30] O. Ronneberger, P. Fischer, and T. Brox, “U-net: Convolutional networks for biomedical image segmentation,” 2015. 

- [31] Y. Song and S. Ermon, “Improved techniques for training score-based generative models,” 2020. 

- [32] K. Kilgour, M. Zuluaga, D. Roblek, and M. Sharifi, “Fréchet audio distance: A metric for evaluating music enhancement algorithms,” 2019. 

585 

