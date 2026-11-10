---
paper_id: "000002"
year: 2021
title: "A Contextual Latent Space Model: Subsequence Modulation in Melodic Sequence 27-34"
source_url: "https://archives.ismir.net/ismir2021/paper/000002.pdf"
---

# **A CONTEXTUAL LATENT SPACE MODEL: SUBSEQUENCE MODULATION IN MELODIC SEQUENCE** 

## **Taketo Akama** 

Sony Computer Science Laboratories, Tokyo, Japan taketo.akama@sony.com 

### **ABSTRACT** 

Some generative models for sequences such as music and text allow us to edit only subsequences, given surrounding context sequences, which plays an important part in steering generation interactively. However, editing subsequences mainly involves randomly resampling subsequences from a possible generation space. We propose a contextual latent space model (CLSM) in order for users to be able to explore subsequence generation with a sense of direction in the generation space, e.g., interpolation, as well as exploring variations—semantically similar possible subsequences. A context-informed prior and decoder constitute the generative model of CLSM, and a context position-informed encoder is the inference model. In experiments, we use a monophonic symbolic music dataset, demonstrating that our contextual latent space is smoother in interpolation than baselines, and the quality of generated samples is superior to baseline models. The generation examples are available online.<sup>1</sup> 

### **1. INTRODUCTION** 

Deep generative models permit sequences of decent quality to be generated such as music, lyrics, or text, where standard models generate sequences by sampling from left to right. However, to make creative works in humanmachine collaborative settings, controllability—such as modifying unsatisfactory portions with specified intentions—should be improved. 

Two major model classes of controllability are (i) latent space models [1–6] and (ii) positional constraint models [7–11]. Latent space models enable us to obtain variations or morphing/interpolations between generated sequences. Positional constraint models, on the other hand, allow us to resample a subsequence without changing the rest of the sequence ( _context sequences_ ), despite the fact that subsequences are sampled randomly and cannot be controlled with morphing/interpolation or variations. Each class of 

1 https://contextual-latent-space-model.github. io/demo/ 

_⃝_ c T. Akama. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). **Attribution:** T. Akama, “A Contextual Latent Space Model: Subsequence Modulation in Melodic Sequence”, in _Proc. of the 22nd Int. Society for Music Information Retrieval Conf.,_ Online, 2021. 



<!-- Start of picture text -->
pitch pitch<br>pitch<br>pitch pitch<br>pitch<br>pitch<br>pitch pitch<br>time (bars) time (bars)<br><!-- End of picture text -->

**Figure 1** : **Contextual Interpolation Examples.** Shaded regions are contexts. For both left and right figures, our CLSM first generates top and bottom melodies under constraints of contexts, and then it generates middle four interpolated points in way that is consistent with contexts. CLSM with _β_ = 0 _._ 012 is used. 

models has its own benefits for making generation systems flexible. 

Can we build a hybrid model that enjoys the best of both worlds as a step towards multifaceted controllability? We propose a contextual latent space model (CLSM) that allows for positional constraints while at the same time enables latent space exploration such as interpolation or variation. An example usage of CLSM’s interpolation is narrowing down the candidates of generated subsequences given context sequences. CLSM variation can be used for obtaining minor modifications of subsequences selected among generated ones, given context sequences. 

Our approach is based on the framework of variational inference, where our CLSM is composed of prior and decoder models for the generative model and an encoder model for the inference model. The prior model of CLSM outputs a latent distribution given context sequences. We refer to the support of the distribution as the _contextual latent space_ . The decoder model of CLSM generates subsequences that fit in with the context, given corresponding points in the contextual latent space. Finally the encoder model infers the latent space distribution given the entire sequence. 

We show the effectiveness of our approach using monophonic sequences in the Lakh MIDI dataset, a large symbolic music dataset [12]. Compared with the baseline methods, our CLSM achieves better performance in terms of the smoothness of the latent space and negative log- 

27 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 



<!-- Start of picture text -->
xT U<br>Lrec Decoder S] xCL xT xCB<br>Transformer pθD(xT|z, xC, τ);<br>Dec<br>u<br>SxCL xT xCR<br>Prior<br>D Lkl w pθp(z|xC, τ) Traditional Mask<br>Encoder Allow to attend<br>Prevent from attending<br>(qφ(z|x, τ) pξ(w|xC, τ)<br>Bi-LSTM Bi-LSTM xTxCR<br>Transformer Transformer<br>Enc Enc u<br>xCR xCR<br>Proposed Mask<br>(a) Model Overview (b) Self-Attention Masks for Decoder Model<br><!-- End of picture text -->

**Figure 2** : **Schematic Diagram of Contextual Latent Space Model (CLSM).** (a) Linear or MLP layers are omitted for brevity. (b) Masks indicate whether position _u_ attends to position _v_ . 

likelihood of the generated samples. In a listening test, participants favored the generated samples of our CLSM more than those of the baselines. 

Our contributions are (I) proposing a problem setting for learning a contextual latent space and providing its solution, (II) proposing novel architectures for the model, e.g., a masking strategy for the decoder and combinations of a transformer and LSTM for the encoder and prior, (III) proposing normalizing flows [13] for conditional priors in order to learn complex conditional priors, (IV) proposing an _interpolation edit distance ratio_ to quantitatively assess the smoothness of latent space, and (V) demonstrating reasonable performance with our CLSM in an application for symbolic music generation. 

### **2. METHODOLOGY** 

### **2.1 Problem Scenario** 

Let us consider an i.i.d dataset _D_ = _{_ **_x_**<sup>(</sup><sup>_i_)</sup> = ( _x_<sup>(</sup> 1<sup>_i_)</sup><sup>_, ..., x_(</sup> _K_<sup>_i_))</sup><sup>_∈AK}_</sup> _i_<sup>_N_</sup> =1<sup>of a sequence of symbols</sup><sup>_xk∈_</sup> _A_ of length _K_ , where _A_ is the alphabet set of symbols. We partition each sequence **_x_** into three subsequences **_x_** CL, **_x_** T, and **_x_** CR, such that **_x_** = **_x_** CL _⊕_ **_x_** T _⊕_ **_x_** CR, where _⊕_ denotes the concatenation of sequences. We refer to subsequences **_x_** CL and **_x_** CR as _context sequences_ and subsequence **_x_** T as the _target sequence_ . Let _τ_ denote a variable representing a set of indexes of the target sequence such that _τ_ = _{|_ **_x_** CL _|_ + 1 _, |_ **_x_** CL _|_ + 2 _, ..., |_ **_x_** CL _|_ + _|_ **_x_** T _|} ∈T_ , where _T_ is a set of all sets of indexes we would like to model with. For notational simplicity, we introduce the shorthand **_x_** C = _{_ **_x_** CL _,_ **_x_** CR _}_ . 

Our goal is to train a generative model with its generative process being (1) **_z_** ˜ _∼ p_ ( **_z_** _|_ **_x_** C _, τ_ ) and (2) **_x_** ˜ T _∼ p_ ( **_x_** T _|_ **_z_** ˜ _,_ **_x_** C _, τ_ ), where **_z_** _∈Z ⊂_ R<sup>_d_z</sup> captures the variability of **_x_** T given **_x_** C and _τ_ . We would also like some distance in the latent space of the prior model to represent the similarity of **_x_** T so that the model can be used for e.g., morphing/interpolation or variation generation. 

### **2.2 Model** 

Fig. 2 is a schematic illustration of our model. Our proposed approach is training a generative model by maximizing the marginal log-likelihood log _pθ_ ( **_x_** T _|_ **_x_** C _, τ_ ) = log _pθ_ D ( **_x_** T _|_ **_z_** _,_ **_x_** C _, τ_ ) _pθ_ P ( **_z_** _|_ **_x_** C _, τ_ ) _d_ **_z_** . Since its computation is intractable in the general case, we introduce the approximate posterior _qφ_ ( **_z_** _|_ **_x_** _, τ_ ) to derive the evidence lower bound (ELBO) [14]. Formally, 



<!-- Start of picture text -->
log  pθ ( x T | x C , τ )<br><!-- End of picture text -->



<!-- Start of picture text -->
= log pθ D ( x T | z ,  x C , τ ) pθ P( z | x C , τ ) d z<br><!-- End of picture text -->



<!-- Start of picture text -->
= log qφ ( z | x , τ ) pθ D ( x T | z ,  x C , τ ) pθ P ( z | x C , τ ) d z<br>qφ ( z | x , τ )<br>≥ qφ ( z | x , τ ) log pθ D ( x T | z ,  x C , τ ) pθ P ( z | x C , τ ) d z<br>qφ ( z | x , τ )<br>=  L rec  −L kl , (1)<br><!-- End of picture text -->

where 



<!-- Start of picture text -->
L rec = E qφ ( z | x ,τ ) [log  pθ D ( x T | z ,  x C , τ )]  , (2)<br><!-- End of picture text -->



<!-- Start of picture text -->
L kl = KL ( qφ ( z | x , τ ) ||pθ P( z | x C , τ ))  . (3)<br><!-- End of picture text -->

In practice, we introduce weighting factors in ELBO [15]. Then, our optimization problem is: 



<!-- Start of picture text -->
1<br>max θ,φ E x ∈D E τ ∈T | x T | L rec  − βL kl , (4)<br><!-- End of picture text -->

where _|_ **_<u>x</u>_** <u>1T</u> _|_<sup>isanormalizingfactor,and</sup><sup>_β_isabalancing</sup> factor of the two terms. The specific choices of _β_ are explained in Sec. 3.4. 

Since the conditional prior is generally multimodal and complex, we propose modeling the conditional prior using normalizing flows [13]: 



<!-- Start of picture text -->
∂ w<br>pθ P( z | x C , τ ) =  pξ ( w | x C , τ ) det , (5)<br>∂ z<br>w =  fλ ( z )  ∈W ⊂ R d z , (6)<br><!-- End of picture text -->

28 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

where _fλ_ : _Z → W_ is an invertible function, and _pξ_ ( _·|_ **_x_** C _, τ_ ) is a Gaussian distribution. We choose to use affine-coupling layers for _fλ_ , which was proposed for realvalued non-volume preserving (realNVP) [16]. 

The Gaussian distribution and the categorical distribution are used for the encoder model _qφ_ ( **_z_** _|_ **_x_** _, τ_ ) and the decoder model _pθ_ D ( **_x_** T _|_ **_z_** _,_ **_x_** C _, τ_ ), respectively. 

The network architectures for parametrizing each distribution are explained in Sec. 2.4. 

### **2.3 Applications** 

### _2.3.1 Contextual Interpolation_ 

Given **_z_** ˜<sup>(1)</sup> _,_ ˜ **_z_**<sup>(2)</sup> _∼ pθ_ P ( **_z_** _|_ **_x_** C _, τ_ ), we provide a procedure for generating contextual interpolations between **_x_** ˜<sup>(1)</sup> _∼_ and **_x_** ˜<sup>(2)</sup> , where **_x_** ˜<sup>(</sup><sup>_i_)</sup> = **_x_** CL _⊕_ **_x_** ˜<sup>(</sup> T<sup>_i_)</sup><sup>_⊕_</sup><sup>**_x_**C</sup> R<sup>with</sup><sup>**_x_**˜(</sup> T<sup>_i_)</sup> _pθ_ D ( **_x_** T _|_ **_z_** ˜<sup>(</sup><sup>_i_)</sup> _,_ **_x_** C _, τ_ ) for _i_ = 1 _,_ 2. 

First, the interpolated latent vector ˜ **_z_** ( _α_ ) with a blending ratio of _α ∈_ [0 _,_ 1] is given by 



<!-- Start of picture text -->
z ˜( α ) =  fλ − 1 (1  − α ) fλ (˜ z (1) ) +  αfλ (˜ z (2) ) , (7)<br>� �<br><!-- End of picture text -->

which means that linear interpolation is performed in the _W_ space, but not in the _Z_ space, achieving non-linear interpolation in the _Z_ space. Then, **_z_** ˜( _α_ ) is decoded and concatenated with the context sequence, yielding **_x_** ˜( _α_ ) = **_x_** CL _⊕_ **_x_** ˜ T( _α_ ) _⊕_ **_x_** CR with 



<!-- Start of picture text -->
x ˜ T( α )  ∼ pθ D ( x T | z ˜( α ) ,  x C , τ ) . (8)<br><!-- End of picture text -->

### _2.3.2 Contextual Variation_ 

Given **_z_** ˜ _∼ pθ_ P ( **_z_** _|_ **_x_** C _, τ_ ), we provide a procedure for generating contextual variations of **_x_** ˜, where **_x_** ˜ = **_x_** CL _⊕_ **_x_** ˜ T _⊕_ **_x_** CR with **_x_** ˜ T _∼ pθ_ D ( **_x_** T _|_ **_z_** ˜ _,_ **_x_** C _, τ_ ). Letting _δ ∈_ R _≥_ 0 and **_ϵ_** _∈_ R<sup>_d_z</sup> be a scaling factor of the variation amount and sampled noise from a normal distribution _N_ ( **0** _,_ Σ) with Σ denoting the covariance matrix of _pξ_ ( **_w_** _|_ **_x_** C _, τ_ ), a variation of the latent vector **_z_** ˜ is given by **_z_** ˜( _δ_ ) = _fλ_<sup>_−_1</sup> ( _fλ_ (˜ **_z_** ) + _δ_ **_ϵ_** ). Then, **_z_** ˜( _δ_ ) is decoded and concatenated in the same manner as Sec. 2.3.1. 

### **2.4 Network Architecture** 

### _2.4.1 Encoder Model_ 

As main architectures, we employ a two-layer “transformer encoder” with relative attention [17, 18], followed by a two-layer bidirectional LSTM network (Bi-LSTM) [19, 20]. **_x_** is first embedded and added by a positional embedding before being inputted to the transformer. The transformer uses no masks and a sequence of vectors **_E_** = ( **_e_** 1 _, ...,_ **_e_** _K_ ) is outputted. Let **_E_** T be a subsequence of **_E_** , consisting of **_E_** ’s elements, whose indexes are in _τ_ , i.e., **_E_** T = ( **_e_** _|_ **_x_** CL _|_ +1 _, ...,_ **_e_** _|_ **_x_** CL _|_ + _|_ **_x_** T _|_ ). Only the subsequence **_E_** T is fed to the Bi-LSTM. Let **_h_** l and **_h_** r denote the last outputs of the Bi-LSTM. They are concatenated to be fed to two multi layer perceptrons (MLPs; each for the mean and covariance of the normal 

distribution), yielding the encoder model _qφ_ ( **_z_** _|_ **_x_** _, τ_ ) = _N_ � **_z_** _|_ MLP( **_h_** l _⊕_ **_h_** r) _,_ diag(<sup><u>1</u></sup> 2<sup>exp(MLP(</sup><sup>**_h_**l</sup><sup>_⊕_</sup><sup>**_h_**r)))</sup> �. The MLPs consist of two layers with a SELU activation in between [21]. 

Concerning the hyper-parameters for the “transformer encoder,” the token embedding size, the hidden size, the number of heads, and the dropout rate are set to 128, 256, 8, and 0 _._ 1, respectively. The hidden size and the dropout rate for the Bi-LSTM are set to 256 and 0 _._ 1, respectively. The hidden size of the MLP and the number of dimensions of **_z_** are set to 512 and 128, respectively. 

### _2.4.2 Prior Model_ 

As can be seen in Eq. 5 and Eq. 6, _pξ_ ( **_w_** _|_ **_x_** C _, τ_ ) and _fλ_ ( **_z_** ) need to be defined for the prior model. 

For _pξ_ ( **_w_** _|_ **_x_** C _, τ_ ), as with the encoder model, a twolayer “transformer encoder” is followed by a Bi-LSTM. Unlike the encoder model, we replace each of the elements in the target sequence **_x_** T with a _positional constraint symbol p_ . In other words, **_x_** CL _⊕_ **_p_** _⊕_ **_x_** CR is fed to the “transformer encoder”, where **_p_** = ( _p, p, ..., p_ ) is a sequence of positional constraint symbols and _|_ **_p_** _|_ = _|_ **_x_** T _|_ . The hyperparameters for the “transformer encoder,” the Bi-LSTM, and the number of dimensions of **_z_** are set to the same values as in Sec. 2.4.1. 

To parameterize _fλ_ ( **_z_** ), four-layer affine-coupling layers are employed. Each of the scale and bias networks of the affine-coupling layers consists of a three-layer MLP, where each hidden size is 256, and the activations are leaky ReLUs with a negative slope of 0 _._ 01. For each of the scale networks, a tanh activation is used after the last linear layer. 

### _2.4.3 Decoder Model_ 

As a main architecture, we employ a two-layer “transformer decoder” with relative attention. Let _s_ be a symbol representing the start of a sequence. The concatenation _s ⊕_ **_x_** is embedded and added by positional embeddings before being inputted to the transformer. 

We propose using an effective encoder-decoder attention mechanism for the latent space. Each latent vector **_z_** ˜ sampled from the encoder model is first fed to a linear layer to map **_z_** ˜ _∈_ R<sup>_d_z</sup> to **_z_** ˜<sup>_′_</sup> _∈_ R<sup>_d_z</sup><sup>_l_z</sup> , which is reshaped to form **_Z_**<sup>˜</sup> _∈_ R<sup>_d_z</sup><sup>_×l_z</sup> , a sequence of _l_ z vectors, where the dimensionality of each vector is _d_ z. The sequence **_Z_**<sup>˜</sup> is then attended to by the transformer by means of encoderdecoder attention. We set _l_ z = 4 in experiments. 

We propose a masking strategy for modeling the decoder, as illustrated in the bottom of Fig. 2b. The positions whose inputs are _s_ , **_x_** CL, and **_x_** CR are allowed to attend to positions except those of **_x_** T. On the other hand, positions whose inputs are **_x_** T are allowed to attend to positions except the future positions of **_x_** T. 

= Let the output of the transformer denote **_D_** ( **_d_** 1 _, ...,_ **_d_** _K_ ). Let **_D_** T be a subsequence of **_D_** , consisting of **_D_** ’s elements whose indexes are in _τ_ , i.e., **_D_** T = ( **_d_** _|_ **_x_** CL _|_ +1 _, ...,_ **_d_** _|_ **_x_** CL _|_ + _|_ **_x_** T _|_ ). Let **_x_** T[ _i_ ] and **_D_** T[ _i_ ] denote 

29 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

the _i_ th elements of **_x_** T and **_D_** T, respectively. Then the decoder model is defined as follows: _pθ_ D ( **_x_** T _|_ **_z_** _,_ **_x_** C _, τ_ ) = � _|i_ **_x_** =1T _|_<sup>Cat(</sup><sup>**_x_**T[i]</sup><sup>_|_Softmax(Linear(</sup><sup>**_D_**T[i]))),whereCat</sup> and Linear denote a categorical distribution and a linear layer respectively. The hyper-parameters of the “transformer decoder” are set to be equal to those of the “transformer encoder” in Sec. 2.4.1. 

### **3. EXPERIMENTAL SETUP** 

### **3.1 Dataset** 

We created datasets from LMD-matched of the Lakh MIDI dataset [12], comprising 45,129 files matched to the song identity entries in the Million Song Dataset [22]. Each song has one or several different versions of MIDI files. We first extracted files with a 4/4 time signature, used the accompanying tempo information to determine beat locations, and quantized each beat into 4. We then split the song identities into a proportion of 11:1:6:1:1 to create train-1, validation-1, train-2, validation-2, and test datasets, respectively. The train-1 and validation-1 datasets were for training the proposed and baseline models, whereas the train-2 and validation-2 datasets were for training evaluation models. The test dataset was for input sequences when evaluating models. We filtered out non-monophonic tracks, bass or drum tracks, and tracks outside the pitch range of [55, 84]. We conducted data augmentation by transposing tracks to all possible keys if the transposed tracks stayed within the pitch range of [55, 84]. We retrieved 8-bar sliding windows (with a stride of 1 bar) from each track followed by filtering out windows that had more than one bar of consecutive rests. For encoding musical sequences, we adopted the melodico-rhythmic encoding proposed in [9], where we used the pitch of musical notes as symbols “55”,...,“84” and used “R” to represent a rest symbol. We added an extra symbol, “__” representing that a note is held and not replayed. 

### **3.2 Baseline Methods** 

### _3.2.1 VAE_ 

We trained a VAE [14], in which a two-layered Bi-LSTM and LSTM were used for the encoder and decoder, respectively. The decoder, encoder, and prior models used the categorical, normal, and standard normal distribution, respectively. The optimization problem is 



<!-- Start of picture text -->
max ψ,ω E x ∈D � | x 1 | � L VAE rec − γL VAE kl � � , (9)<br><!-- End of picture text -->

where _L_<sup>VAE</sup> rec = E _qω_ ( **_z_** _|_ **_x_** ) [log _pψ_ ( **_x_** _|_ **_z_** )], _L_<sup>VAE</sup> kl = KL ( _qω_ ( **_z_** _|_ **_x_** ) _||p_ ( **_z_** )), and _|_ **_<u>x</u>_** <u>1</u> _|_<sup>is a normalizing factor.</sup> 

Given **_x_** C, _τ_ , and **_z_** ˜<sup>(1)</sup> _,_ ˜ **_z_**<sup>(2)</sup> _∼ p_ ( **_z_** ), interpolation is conducted as follows. First, interpolated latent vector ˜ **_z_** ( _α_ ) is given by 



<!-- Start of picture text -->
z ˜( α ) = (1  − α )˜ z (1) +  α z ˜ (2) . (10)<br><!-- End of picture text -->

Then, **_z_** ˜( _α_ ) is decoded and concatenated with the context sequence: **_x_** ˜( _α_ ) = **_x_** CL _⊕_ **_x_** ˜ T( _α_ ) _⊕_ **_x_** CR with 



<!-- Start of picture text -->
x ˜ T( α )  ∼ pψ ( x T | z ˜( α ) ,  x CL) , (11)<br><!-- End of picture text -->

where _pψ_ ( **_x_** T _|_ **_z_** _,_ **_x_** CL) can be immediately obtained from the autoregressive decoder model of VAE. Note that the proposed CLSM has advantages over VAE in terms of probabilistic dependencies (i) the decoder model of VAE does not have dependencies on the right context **_x_** CR, and (ii) the prior model of VAE does not have dependencies on either the left context **_x_** CL or the right context **_x_** CR. The property of (i) motivates us to separately quantify the performance of models in two cases: (1) the case where only the left context exists, and (2) otherwise. In Sec. 4.1, Sec. 4.2, and Fig. 3b, we report the performance of these two cases separately. 

Random generation was conducted as follows. First, a latent vector was sampled from the prior distribution. Then, **_z_** ˜ was decoded and concatenated with context sequences in the same manner as the interpolation. 

The hyper-parameters of the LSTMs in VAE were set to be equal to those of the LSTMs in CLSM. 

### _3.2.2 ARNN_ 

Anticipation RNN (ARNN) [9] is a sequence generation model with positional constraints. Two-layered LSTMs were used for both Token-RNN and Constraint-RNN. The hyper-parameters of the LSTMs were set to be equal to those of the LSTMs in CLSM. 

### **3.3 2D Plane for Comparing CLSM and VAE** 

The balancing factors _β_ and _γ_ of CLSM and VAE consist in adjusting the trade-off between the reconstruction accuracy and other model performances. Which balancing factors of CLSM correspond to which ones of VAE? It is natural to compare models of similar reconstruction accuracies or compare models of similar performances (except reconstruction accuracies). Therefore, in Sec. 4.1, Sec. 4.2, and Fig. 3b, we plot reconstruction accuracies versus other performance metrics in 2D planes, where the more the plotted point is in the upper left corner, the better it is. As discussed in Sec. 3.2.1, CLSM and VAE have dependencies at least on the left context. To make the reconstruction accuracies of the CLSM and VAE mean basically identical, we used the _left-contextual reconstruction accuracy_ , which is the average of the reconstruction accuracies of sequences where target sequences end with index _|_ **_x_** _|_ , i.e., there is no right context and only the left context exists. 

### **3.4 Training Settings** 

For all models, teacher forcing was used, the batch size was set to 64, and training was conducted for 2 epochs, when the losses converged. The Adam optimizer [23] was used for all models, with the parameters ( _α, β_ 1 _, β_ 2) = (0 _._ 0005 _,_ 0 _._ 9 _,_ 0 _._ 999). For CLSM or VAE, we conducted 

30 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 



<!-- Start of picture text -->
CLSM VAE<br>ARNN<br>ARNNT<br>0.95 Data<br>0.90 CLSM β = 0.004<br>CLSM β = 0.006<br>0.85 CL5 =  08<br>left-contextual 0.80 CLSM β = 0.010<br>0.75 CLSMβ= 0.014CLSM β = 0.012<br>Left Context Only reconstruction a0.70 c uracy CLSM β = 0.016<br>0.951.00 VAE γ=0.2VAE γ = 0.1VAE γ=0.3<br>0.90 VAE γ=0.4<br>VAE γ = 0.5<br>0.85 VAE γ = 0.6<br>Otherwise 0.80 VAE γ = 0.7<br>VAE γ = 0.8<br>0.75 VAE γ=0.9<br>ARNN ARNNT reconstruction a c uracy0.70 VAE γ = 1.0<br>VAE γ=2.0<br>interpolation LM-NLL of<br>edit distance ratio generated samples<br>Data<br>(a) Generation Comparison (b) Objective Evaluation (c) Human Evaluation<br><!-- End of picture text -->

**Figure 3** : **Generation Comparison and Experimental Results.** (a) Shaded regions are contexts. For CLSM and VAE, _β_ = 0 _._ 012 and _γ_ = 0 _._ 4 are used. (b) For evaluating smoothness (to left), small, medium, and large marker are plots for number of divisions in interpolation _J_ = 8 _,_ 4 _,_ 2, respectively. See Sec. 4.1 and 4.2. (c) See Sec. 4.3. 

KL-annealing linearly from _β_ = 0 or _γ_ = 0 for 2 epochs [1]. 

cal distributions of the decoders. For ARNN, multinomial sampling with a temperature of 1 _._ 0 was used. 

### _3.4.1 CLSM (Ours)_ 

### **4. EXPERIMENTS AND RESULTS** 

At every iteration of the training, indexes of the target sequence _τ_ = _{|_ **_x_** CL _|_ + 1 _, |_ **_x_** CL _|_ + 2 _, ..., |_ **_x_** CL _|_ + _|_ **_x_** T _|} ∈T_ should be sampled. In the experiments, we chose to use either 1, 2, 3, or 4 bars as the target sequence length and used a stride of 1 bar for the starting index of the target sequence. Precisely, we sampled (i) _|_ **_x_** T _|_ uniformly from _{_ 16 _,_ 32 _,_ 48 _,_ 64 _}_ and then (ii) sampled _|_ **_x_** CL _|_ uniformly from _{_ 0 _,_ 16 _,_ 32 _, ...,_ 128 _−|_ **_x_** T _|}_ . Note that 128 corresponds to 8 bars (the sequence length) and that 16 corresponds to 1 bar. The balancing factor _β_ in Eq. 4 is set to _{_ 0 _._ 004 _,_ 0 _._ 006 _, ...,_ 0 _._ 016 _}_ in Secs. 4.1, 4.2 and 0 _._ 012 in Sec. 4.3. The expectations of the two terms in Eq. 4 were approximated with one sample from the encoder model. 

### _3.4.2 VAE (Baselines)_ 

The balancing factor _γ_ in Eq. 9 is set to _{_ 0 _._ 1 _,_ 0 _._ 2 _, ...,_ 1 _._ 0 _,_ 2 _._ 0 _}_ in Secs. 4.1, 4.2 and 0 _._ 4 in Sec. 4.3. The expectations of the reconstruction loss were approximated with one sample from the encoder model. The KL loss term was computed analytically. 

### _3.4.3 ARNN (Baseline)_ 

The vanilla ARNN is capable of imposing constraints of any positions. Since it would be possible that restricting constraints to those of our _T_ would be advantageous when evaluated over _T_ , we also trained and evaluated this model, which we refer to as ARNN _T_ . 

### **3.5 Generation Settings** 

For CLSM and VAE, each element of sequences was sampled by applying the argmax operation to the categori- 

### **4.1 Smoothness Analysis in Latent Space** 

To assess the smoothness of our latent space, we propose the _interpolation edit distance ratio R_ ( _J_ ), which is the ratio of the distance between adjacent interpolated points (sequences) to the distance of interpolation end points (sequences). Formally, _R_ ( _J_ ) is the normalized average edit distance _d_ edit( _·, ·_ ) of adjacent points in _J_ -divided interpolated points: 



<!-- Start of picture text -->
∑ Jj =0 − 1 d edit x ˜ T ( - Jj ) ,  ˜ x T ( j 一 + J 1 ))<br>R ( J ) = E , (12)<br>D ( J − n )<br><!-- End of picture text -->

where **_x_** ˜ T( _·_ ) is defined by Eqs. 7, 8 for CLSM and Eqs. 10, 11 for VAE, while _D_ is the edit distance between end points defined by _D_ = _d_ edit (˜ **_x_** T(0) _,_ ˜ **_x_** T( _J_ )). Here, the expectation is approximated by sampling **_z_** ˜<sup>(1)</sup> _,_ ˜ **_z_**<sup>(2)</sup> _∼ pθ_ P( **_z_** _|_ **_x_** C _, τ_ ) for CLSM and **_z_** ˜<sup>(1)</sup> _,_ ˜ **_z_**<sup>(2)</sup> _∼ p_ ( **_z_** ) for VAE, where 1K samples of **_x_** are uniformly sampled from the test dataset, and, for each **_x_** , _τ_ is uniformly sampled from _T_ . Since the edit distance _d_ edit ((- **_x_** ˜ T ~~)~~ _Jj_ ( _,_ ˜ **_x_** ~~—)~~ T _<u>j</u>_ <u>+</u> _J_ 1 ) sometimes becomes zero, we excluded cases through division by _J −n_ instead of _J_ as in Eq. 12, where _n_ is the number of edit distances that are zero among _j_ = 0 _,_ 1 _, ..., J −_ 1. We also excluded cases where _D_ ( _J −n_ ) = 0. The left scatter plot of Fig. 3b shows a comparison of CLSM and VAE. The small, medium, and large markers are plots for the number of divisions in interpolation _J_ = 8 _,_ 4 _,_ 2, respectively. For each _J_ , CLSM performed better than VAE. The plots of VAE _J_ = 8 overlap with those of CLSM _J_ = 4, indicating that even 4-divided interpolation of CLSM was as smooth as 8-divided interpolation of VAE. The results 

31 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

are similar in the two cases of “left context only” and “otherwise.” 

### **4.2 NLL Evaluation of Generated Samples** 

To evaluate the quality of generated samples, we computed the negative log-likelihood (NLL) of the generated samples. NLL was computed by using a separately trained vanilla transformer language model (LM) that had two layers and was autoregressive. The LM was trained by using the train-2 and validation-2 datasets defined in Sec. 3.1. The samples to be evaluated were the same as the 8-divided interpolated points in Sec. 4.1. Since ARNN is not capable of interpolation, only a random sampling of two points was performed per each context for ARNN. The right scatter plot of Fig. 3b shows a comparison of the CLSM, VAE, ARNNs, and the test dataset (Data). CLSM outperformed VAE by a large margin when we compared models that were close in terms of reconstruction accuracy or NLL—a reasonable strategy of comparison as we discuss in Sec. 3.3. Compared with the ARNNs, the performance of CLSM was superior in all settings. The results of VAE were better in the case of “left context only” than in the case of “otherwise.” In contrast, for the CLSM and ARNNs, there were only slight differences between the two cases. This empirically demonstrates that the decoder model of VAE has dependencies only on the left context but not on the right context, as we discuss in Sec. 3.2.1. 

### **4.3 Human Evaluation** 

To further assess the quality of sequences generated by each model, we conducted listening tests using Amazon Mechanical Turk. We sampled 32 sequences from the test dataset, for which context positions were randomly sampled, and the target sequence lengths were sampled from 1-4 bars. We conducted a pair-wise comparison of the generation results of each model using the same context sequences. We considered all possible combinations, yielding 320 pair-wise comparisons. The order within each pair was randomized. We chose to use _β_ = 0 _._ 012 for CLSM, since the performance trade-offs are well balanced according to the results in Sec. 4.1 and Sec. 4.2. As discussed in Sec. 3.3 since it is reasonable to choose a VAE model with a similar reconstruction accuracy to that of CLSM, we chose _γ_ = 0 _._ 4 for VAE. Participants with different levels of musical expertise were asked to rate “which music is better in terms of musicality, naturalness, and creativity” on a Likert scale. Fig. 3c shows a comparison of the CLSM, VAE, ARNNs, and the test dataset (Data). CLSM and Data performed the best in terms of the percentage of wins (Fig. 3c, top) as well as the percentage of wins and draws (Fig. 3c, bottom). Interestingly, the ARNNs tended to outperform VAE when the number of draws was included, whereas VAE tended to outperform the ARNNs when only the number of wins was considered. This might indicate that the performance of VAE tends to be extreme. 

### **5. RELATED WORK** 

T-CVAE is a transformer-based conditional VAE model for story completion [24]. VAEAC [25] is a CNN- or MLPbased VAE that enables us to impose any positional constraints. Although their probabilistic frameworks are similar to ours, the models and architectures are quite different. Unlike their models, CLSM is demonstrated to perform interpolation in the latent space. Moreover, the data domain of T-CVAE is story text, and the domains of VAEAC are image and feature classification/regression datasets, while ours is for sequence datasets and experimented on music. 

Although contexts are not considered for latent variables, there are several works that use transformers for learning a global latent variable for sequences using AE or VAE. For text-style transfer, a “transformer encoder” outputs are all fed to GRU to yield a latent vector, which is attended to by a decoder [26]. To learn the styles of piano performances, a “transformer encoder” outputs are summed to be attended to by a decoder [27]. In OPTIMUS for sentence modulation [28] and INSET [29] for sentence infilling, a CLS token is additionally fed to a “transformer encoder,” and the output at the position of the CLS yields a latent vector, which is fed to a decoder either by selfattention and/or by being added to word embeddings of the decoder (OPTIMUS) or by being inputted as the first token (INSET). 

For language processing, the authors of UniLM propose seq-to-seq LM, where they divide a whole sequence into first and second segments [30]. The self-attention masks are bidirectional and unidirectional for the first and second segments, respectively. Our decoder mask is different in that it divides a sequence into three segments, where the length of the first and third segments can be zero during the training or inference phase. Also, the training procedure of them is BERT-like, which is different from ours [31]. 

RealNVP has been used for the prior in VAE in order to improve the performance of VAE [32,33]. However, these works are not only in the domain of images but also use non-conditional priors, which differs from ours. 

### **6. CONCLUSION** 

We proposed a contextual latent space model (CLSM), in which the left and/or right contexts of sequences can be constrained to generate interpolations or variations. A context-informed prior and decoder constitute the generative model of CLSM and a context position-informed encoder is the inference model. 

The latent space of CLSM was quantitatively shown to be smoother than baselines. Furthermore, the generation fidelity was demonstrated to be superior to the baseline methods. It would be useful to apply our approach to other data domains such as polyphonic music, lyrics, or text. The benefits of the latent space model are not only enabling interpolations and variations but also enabling transformations of attributes or style transfer. It would be desirable to extend our approach to these kinds of applications. 

32 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

### **7. REFERENCES** 

- [1] S. R. Bowman, L. Vilnis, O. Vinyals, A. Dai, R. Jozefowicz, and S. Bengio, “Generating sentences from a continuous space,” in _Proceedings of The 20th SIGNLL Conference on Computational Natural Language Learning_ , 2016. 

- [2] A. Roberts, J. Engel, C. Raffel, C. Hawthorne, and D. Eck, “A hierarchical latent vector model for learning long-term structure in music,” in _Proc. of the 35th International Conference on Machine Learning_ , 2018. 

- [3] T. Akama, “Controlling symbolic music generation based on concept learning from domain knowledge,” in _Proceedings of the 20th International Society for Music Information Retrieval Conference, ISMIR_ , 2019. 

- [4] A. Pati and A. Lerch, “Attribute-based Regularization of Latent Spaces for Variational Auto-Encoders,” _Neural Computing and Applications_ , 2020. 

- [5] H. Tan and D. Herremans, “Music fadernets: Controllable music generation based on high-level features via low-level feature modelling,” in _ISMIR_ , 2020. 

- [6] T. Akama, “Connective fusion: Learning transformational joining of sequences with application to melody creation,” in _Proceedings of the 21st International Society for Music Information Retrieval Conference_ . ISMIR, 2020. 

- [7] B. Uria, I. Murray, and H. Larochelle, “A deep and tractable density estimator,” in _Proceedings of the 31st International Conference on Machine Learning_ , 2014. 

- [8] A. Wang and K. Cho, “BERT has a mouth, and it must speak: BERT as a markov random field language model,” _CoRR_ , vol. abs/1902.04094, 2019. 

- [9] G. Hadjeres and F. Nielsen, “Anticipation-rnn: enforcing unary constraints in sequence generation, with application to interactive music generation,” _Neural Computing and Applications_ , vol. 32, no. 4, pp. 995–1005, 2020. 

- [10] C. A. Huang, T. Cooijmans, A. Roberts, A. C. Courville, and D. Eck, “Counterpoint by convolution,” in _Proceedings of the 18th International Society for Music Information Retrieval Conference, ISMIR_ , 2017. 

- [11] A. Pati, A. Lerch, and G. Hadjeres, “Learning to traverse latent spaces for musical score inpainting,” _ISMIR_ , 2019. 

- [12] C. Raffel, “Learning-based methods for comparing sequences, with applications to audio-to-midi alignment and matching,” Ph.D. dissertation, 2016. 

- [13] D. Rezende and S. Mohamed, “Variational inference with normalizing flows,” in _Proceedings of the 32nd International Conference on Machine Learning_ , 2015. 

- [14] D. P. Kingma and M. Welling, “Auto-encoding variational bayes,” _CoRR_ , vol. abs/1312.6114, 2013. 

- [15] I. Higgins, L. Matthey, A. Pal, C. Burgess, X. Glorot, M. Botvinick, S. Mohamed, and A. Lerchner, “betavae: Learning basic visual concepts with a constrained variational framework,” in _5th International Conference on Learning Representations, ICLR_ , 2017. 

- [16] L. Dinh, J. Sohl-Dickstein, and S. Bengio, “Density estimation using real NVP,” in _5th International Conference on Learning Representations, ICLR 2017_ . 

- [17] P. Shaw, J. Uszkoreit, and A. Vaswani, “Self-attention with relative position representations,” in _Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 2 (Short Papers)_ . 

- [18] C.-Z. A. Huang, A. Vaswani, J. Uszkoreit, I. Simon, C. Hawthorne, N. Shazeer, A. M. Dai, M. D. Hoffman, M. Dinculescu, and D. Eck, “Music transformer,” in _International Conference on Learning Representations_ , 2019. 

- [19] S. Hochreiter and J. Schmidhuber, “Long short-term memory,” _Neural computation_ , vol. 9, pp. 1735–80, 12 1997. 

- [20] M. Schuster and K. Paliwal, “Bidirectional recurrent neural networks,” _IEEE Transactions on Signal Processing_ , vol. 45, no. 11, pp. 2673–2681, 1997. 

- [21] G. Klambauer, T. Unterthiner, A. Mayr, and S. Hochreiter, “Self-normalizing neural networks,” in _Advances in Neural Information Processing Systems_ , I. Guyon, U. V. Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan, and R. Garnett, Eds. Curran Associates, Inc., 2017. 

- [22] T. Bertin-Mahieux, D. P. Ellis, B. Whitman, and P. Lamere, “The million song dataset,” in _Proceedings of the 12th International Conference on Music Information Retrieval (ISMIR 2011)_ , 2011. 

- [23] D. P. Kingma and J. Ba, “Adam: A method for stochastic optimization,” in _3rd International Conference on Learning Representations, ICLR_ , 2015. 

- [24] T. Wang and X. Wan, “T-cvae: Transformer-based conditioned variational autoencoder for story completion,” in _Proceedings of the Twenty-Eighth International Joint Conference on Artificial Intelligence, IJCAI-19_ , 2019. 

- [25] O. Ivanov, M. Figurnov, and D. Vetrov, “Variational autoencoder with arbitrary conditioning,” in _International Conference on Learning Representations_ , 2019. 

- [26] K. Wang, H. Hua, and X. Wan, “Controllable unsupervised text attribute transfer via editing entangled latent representation,” in _Advances in Neural Information Processing Systems_ . Curran Associates, Inc., 2019. 

33 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

- [27] K. Choi, C. Hawthorne, I. Simon, M. Dinculescu, and J. Engel, “Encoding musical style with transformer autoencoders,” in _Proceedings of the 37th International Conference on Machine Learning_ , 2020. 

- [28] C. Li, X. Gao, Y. Li, X. Li, B. Peng, Y. Zhang, and J. Gao, “Optimus: Organizing sentences via pretrained modeling of a latent space,” in _EMNLP_ , 2020. 

- [29] Y. Huang, Y. Zhang, O. Elachqar, and Y. Cheng, “INSET: sentence infilling with inter-sentential transformer,” in _Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, ACL 2020_ , D. Jurafsky, J. Chai, N. Schluter, and J. R. Tetreault, Eds., 2020. 

- [30] L. Dong, N. Yang, W. Wang, F. Wei, X. Liu, Y. Wang, J. Gao, M. Zhou, and H.-W. Hon, “Unified language model pre-training for natural language understanding and generation,” in _Advances in Neural Information Processing Systems_ , vol. 32. Curran Associates, Inc., 2019. 

- [31] J. Devlin, M. Chang, K. Lee, and K. Toutanova, “BERT: pre-training of deep bidirectional transformers for language understanding,” in _Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, NAACL-HLT 2019_ . 

- [32] C.-W. Huang, A. Touati, L. Dinh, M. Drozdzal, M. Havaei, L. Charlin, and A. Courville, “Learnable explicit density for continuous latent space and variational inference,” 2017. 

- [33] H. Xu, W. Chen, J. Lai, Z. Li, Y. Zhao, and D. Pei, “On the necessity and effectiveness of learning the prior of variational auto-encoder,” 2019. 

34 

