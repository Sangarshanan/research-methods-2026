---
paper_id: "000090"
year: 2021
title: "MuseBERT: Pre-training Music Representation for Music Understanding and Controllable Generation 722-729"
source_url: "https://archives.ismir.net/ismir2021/paper/000090.pdf"
---

# **MUSEBERT: PRE-TRAINING OF MUSIC REPRESENTATION FOR MUSIC UNDERSTANDING AND CONTROLLABLE GENERATION** 

**Ziyu Wang** 

Music X Lab, NYU Shanghai ziyu.wang@nyu.edu 

**Gus Xia** 

Music X Lab, NYU Shanghai gxia@nyu.edu 

## **ABSTRACT** 

BERT has proven to be a powerful language model in natural language processing and established an effective pre-training & fine-tuning methodology. We see that music, as a special form of language, can benefit from such methodology if we carefully handle its highly-structured and polyphonic properties. To this end, we propose MuseBERT and show that: 1) MuseBERT has detailed specification of note attributes and explicit encoding of music relations, without presuming any pre-defined sequential event order, 2) the pre-trained MuseBERT is not merely a language model, but also a controllable music generator, and 3) MuseBERT gives birth to various downstream music generation and analysis tasks with practical value. Experiment shows that the pre-trained model outperforms the baselines in terms of reconstruction likelihood and generation quality. We also demonstrate downstream applications including chord analysis, chord-conditioned texture generation, and accompaniment refinement. 

## **1. INTRODUCTION** 

BERT [1] has proven to be one of the leading language models in natural language processing, which learns natural language representation in an unsupervised manner and achieved state-of-the-art results in many downstream language understanding tasks. The methods involved in BERT are not unfamiliar in the music domain. For example, the “masked language model” (MLM) objective in BERT is similar to the Bach chorale inpainting studies [2–4], where the grids in a four-part piano-roll are randomly masked and the model is trained to reconstruct them from context. The Transformer architecture has also been applied to different styles of music generation [5,6]. 

We aim to develop a pre-trained music-domain BERT for better music understanding and generation. A straightforward approach is to use existing music representations used in existing Transformer-based models, such as MIDIlike representations [5,7], REMI [6], or CP [8], and simply train the original BERT model. However, we argue that 

> © Z. Wang, and G. Xia. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). **Attribution:** Z. Wang, and G. Xia, “MuseBERT: Pre-training of Music Representation for Music Understanding and Controllable Generation”, in _Proc. of the 22nd Int. Society for Music Information Retrieval Conf.,_ Online, 2021. 

such approach overlooks major distinctions between music and natural language. Firstly, unlike natural language, music (especially polyphony) does not follow a unique sequential order; abruptly flatten music into a 1-d sequence imposes extra protocol and often undermines the local structure of music, adding extra burden to the model. Secondly, music involves rich relations and contexts. A single music event is barely meaningful, and common music concepts such as rhythmic patterns and harmonies are established upon relative positions of notes. However, current sequential models, in particular Transformer-based models, still struggle to capture these relations [9]. 

To overcome the limits above, we propose MuseBERT, a Transformer-based pre-trained model with tailored handling of music positional information and music relations.<sup>1</sup> Since the innate music positions are expressed in the time-frequency space, we use onset and pitch information as the absolute positional encoding, which can be masked at the input and then reconstructed at the output. Moreover, multiple musical relations are represented via the design of _generalized_ relative positional encoding (RPE) modified from the original RPE design [10]. In our implementation, we find the traditional sequential positional encoding unnecessary, and thus our model does not rely on any pre-defined sequential assumptions. 

Under such tailored design, we show the pre-trained MuseBERT is not merely a language model but also a controllable music generator. In the fine-tuning stage, the model naturally empowers a wide spectrum of finetuning tasks, involving both music analysis and generation. Specifically, we showcase that MuseBERT can perform polyphonic music generation controlled by chord and texture, chord extraction, and accompaniment refinement. In summary, the contributions of this paper are: 

- We demonstrate the possibility and importance of training a Transformer-based music language model in an _unordered_ approach. 

- We develop generalized RPE for BERT-like models, which not only reveals music relations from multiple perspectives but also has a potential to be adopted to other domains. 

- We show MuseBERT, as a controllable music generator, giving the fine-tuning procedure practical music meanings. 

> 1 Code and demos can be accessed via https://github.com/ ZZWaang/musebert. 

722 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

## **2. DATA REPRESENTATION** 

Unlike natural language processing, there is not a common way to tokenize symbolic music. A music piece is generally considered as a combination of note events, where each note event is a tuple of attributes. Note-based tokenization is commonly seen in music-tailored packages [11,12], softwares [13–15], and researches [8,16,17]. On other occasions, mainly for the ease of neural network modeling, music is also simplified as a sequence of controls with pre-defined order, such as MIDI-like event representation [5,7] (including its follow-up methods [6]), and frame-wise piano-roll representations [2,18–20]. 

In MuseBERT, we consider note-based tokenization without presumption of any sequential order. Specifically, we invent two note-based music representations for MuseBERT: _basic data representation_ and _factorized data representation_ , denoted by _R_ base and _R_ fac respectively. A music input is first encoded as _R_ base, and then converted into _R_ fac, serving as the input format to MuseBERT. 

In this paper, we primarily consider 2-bar music segments in 4/4 time signature. Longer music and richer time signatures can be generalized and we leave it for future study. 

## **2.1** _R_ **base and** _R_ **fac** 

_R_ base represents a music segment _X_ as an _unordered set_ of note events _{xi}_<sup>_N_</sup> _i_ =1<sup>,and a note event</sup><sup>_xi∈X_consists</sup> of three attributes: onset (o), pitch (p), and duration (d), where o _∈_ [0 _.._ 31] and d _∈_ [0 _.._ 32] are counted by semiquavers, and p _∈_ [0 _.._ 127] is the MIDI note number.<sup>2</sup> We denote the _attribute set_ of _R_ base by _A_ base := _{_ o _,_ p _,_ d _}_ and use _xi.a, a ∈A_ base to indicate the attribute _a_ of a note event _xi_ . 

_R_ base is not the MuseBERT input data format because the representation is _ambiguous_ for BERT-like models to reconstruct well. Consider, for example, two simultaneous quarter notes in a music segment that are unordered (by definition of _R_ base) and whose attributes except p are the same. When their pitch attributes are masked at the input, the two tokens have completely the same encoding and are unable to be distinguished by BERT, in which case BERT will yield the same output distributions. 

We therefore invent _R_ fac which is unambiguous for MuseBERT (proved in section 4). _R_ fac also represents a music segment as an unordered set of note events, but it uses a more detailed attribute set _A_ fac (discussed in section 2.2), and contains a stack of relation matrices storing pairwise note relations (discussed in section 2.3). 

## **2.2 Factorized Attributes** 

In _R_ fac, onset, pitch, and duration, due to their hierarchical nature [21,22], are regarded as meta-attributes to be factorized. The factorization operation we will introduce is analogous to storing a number by its digits (e.g., 49 _�→_ [4 _,_ 9]), 

> 2 We use [ _a..b_ ] to denote the integer interval _{x|a ≤ x ≤ b, x ∈_ Z _}_ including both endpoints. 

so that we can mask partial information at certain hierarchy (e.g., [4 _,_ MASK]) and the remaining information is still retained. In music, musicians sometimes prefer to interpret 49 as 50 _−_ 1 rather than 40 + 9, depending on the context. Such subtlety is welcomed by our design. 

## _2.2.1 Onset and Duration Factorization_ 

We factorize onset (o) into _beat position_ (o_bt _∈_ [0 _.._ 8]) and _subdivision_ (o_sub _∈_ [0 _.._ 4]), and duration d into _half note counts_ (d_hlf _∈_ [0 _.._ 4]) and _the remainder semiquaver counts_ (d_sqv _∈_ [0 _.._ 7]), satisfying 



<!-- Start of picture text -->
o = (4  ×  o_bt + o_sub), (1)<br><!-- End of picture text -->



<!-- Start of picture text -->
d = (8  ×  d_hlf + d_sqv). (2)<br><!-- End of picture text -->

We allow o_sub to take both positive and negative values, since a subdivision can be interpreted as an “off-beat” of the current downbeat, or an “upbeat” preceding the next downbeat. Consequently, the o attribute can be mapped to multiple _{_ o_bt _,_ o_sub) pairs, e.g., _{_ o :1 _}_ maps to _{_ o_bt : 0 _,_ o_sub :1 _}_ or _{_ o_bt :1 _,_ o_sub : _−_ 3 _}_ . 

In our implementation, we _non-deterministically_ sample one of the factorizations. In the future, a posterior distribution of _p_ (o_bt _,_ o_sub _|_ o _, X_ ) can be explored in finer detail. 

## _2.2.2 Pitch Factorization_ 

We factorize pitch in a similar fashion into three attributes: 1) _pitch highness_ (p_hig _∈_ [0 _.._ 6]): voice types (e.g., SATB), 2) _pitch register_ (p_reg _∈_ [0 _.._ 2]): the relative octave given p_hig, and 3) _pitch degree_ (p_deg _∈_ [0 _.._ 11]), satisfying: 



<!-- Start of picture text -->
24 + 12  ×  (p_hig ++ p_regp_deg) , 0  ≤ p_hig  ≤ 4<br>p = 12108 + 12  ×  p_reg  ×  p_reg + p_deg + p_deg , , p_higp_hig = 5 = 6.<br>(3)<br><!-- End of picture text -->

Here, 0 _≤_ p_hig _≤_ 4 corresponds to the pitch range of a standard piano (MIDI pitch 24-107), and p_hig = 5 and p_hig = 6 handles the extra-low or extra-high regions, respectively. Similar to onset, pitch factorization is also handled non-deterministically, since a pitch can be interpreted as a lower voice type having a high register, or a higher voice type having a low register. 

To summarize, _R_ fac uses the attribute set: 



<!-- Start of picture text -->
A fac :=  { o_bt ,  o_sub ,  p_hig ,  p_reg ,<br>p_deg ,  d_hlf ,  d_sqv } . (4)<br><!-- End of picture text -->

## **2.3 Note Event Relations** 

Music is rich in relations and we explicitly represent the most fundamental relations in _R_ fac. We consider less-than, equal-to, and greater-than relations on a subset of attributes _S_ := _{_ o _,_ o_bt _,_ p _,_ p_hig _}_ . Specifically, _∀a ∈S_ , we define a mapping _γa_ from an input note event pair ( _xi, xj_ ) to their relation symbol:<sup>3</sup> 

> 3 When _a_ = o, _xi._ o is a shorthand notation interpreted as the return value of Eqn (1). A similar case holds when _a_ = p. 

723 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 



<!-- Start of picture text -->
Basic Data Representation Factorized Data Representation<br>Music Observation ReadWrite 𝑋𝑥𝑥𝑥𝑥𝑥𝑥!"#$%& $"%& 12 o 00478 647265646462 p d 1243144 ④①Deterministic MappingStochastic mapping 𝑥𝑥𝑥𝑥𝑥𝑥𝑋!"#$%& !"# o_bt 001223 o_sub -100000 p_hig 343333 p_reg 111111 p_deg 405442 d_hlf 010000 d_sqv 443144 𝑥𝑥𝑥𝑥𝑥𝑥!"#$%&𝑅≡>>≡≡<𝒮 ≡>≡≡≡≡><≡<<<< ≡≡>>>>><≡<<<<≡<>≡<<<𝑥≡≡>>>>>!≡≡>>>>>≡>≡≡≡≡>≡>>≡≡<𝑥≡≡>>>>>"<<≡>>>>≡>≡≡≡≡>≡>>≡≡<𝑥<<≡>>>>#<<<≡>>>≡>≡≡≡≡>>>>>>≡𝑥<<<≡≡>>$<<<<≡>>≡>≡≡≡≡><><<<<𝑥<<<≡≡>>%<<<<<≡≡<≡<<<<≡ 𝑥<<<<<≡≡&<<<<<≡≡ 𝑥<<<<<≡≡'<br>ℛ$"%& 𝑥' 12 71 4 ℛ!"# 𝑥' 3 0 4 0 11 0 4 𝑥' > < > > > > ≡<br>② Data Corruption<br>Corrupted Factorized Data 1 ③ Reconstruction<br>𝑋𝑥𝑥𝑥𝑥𝑥𝑥!"#$%& ∗ o_bt 0122?? o_sub -10002? p_hig 33333? p_reg 101110 p_deg 40544? d_hlf 00000? d_sqv 4314?? 𝑥𝑥𝑥𝑥𝑥𝑥!"#$%&𝑅≡<>≡≡?𝒮∗ ≡>≡≡≡≡>>≡>>>? ≡≡>>>>>≡≡<<<<≡<<≡<<<𝑥≡≡>>>>>!≡≡>>>>>≡>≡≡≡≡>≡<>≡≡<𝑥≡>>>>>?"<<≡>>>>≡>≡≡≡≡>≡<>≡≡?𝑥<<≡>>>>#<<<≡>>>≡>≡≡≡≡>>>≡???𝑥<<<≡≡>>$<<<<≡>>>≡≡≡≡>?<<<<<?𝑥<<<≡≡>>%<<<<<≡≡<≡<<<<≡𝑥<<<<<≡≡&<<<<<≡? 𝑥<<<<<≡?' MuseBERT Embs(R3)Embs(Rs)EmbK(Rs)Emby(R}) Emb(xi)£1Trans former Encoder LayerTrans fomer Encoder LayerEmb(x2)x2 Emb(x)x7x×<br>𝑥' 3 0 4 0 11 0 4 𝑥' > > > > > ? ≡<br>ℛ!"#∗ xi<br><!-- End of picture text -->

**Figure 1** . The workflow of MuseBERT pre-training. 



<!-- Start of picture text -->
 < a , xi.a < xj.a<br>γa ( xi, xj ) = ≡ a , xi.a ≡ xj.a (5)<br> > a , xi.a > xj.a .<br><!-- End of picture text -->

The relation symbols are stored using a stack of _N × N relation matrices_ , denoted by _RS_ := _{Ra|a ∈S}_ , where _Ra_ = _{rij_<sup>_a}_and</sup><sup>_r_</sup> _ij_<sup>_a_=</sup><sup>_γa_(</sup><sup>_xi, xj_).</sup> 

matrix may be required so as to maintain matrix symmetry and align with the attributes that are replaced with other values. 

We denote the representation after corruption as _R_<sup>_∗_</sup> fac<sup>,</sup> and the resulting note events and relation matrices as _X_<sup>_∗_</sup> and _RS_<sup>_∗_, respectively.</sup> 

## **3.2 Overall Model Architecture** 

## **3. PRE-TRAINING MUSEBERT** 

Figure 1 shows the overall pre-training stage. A music data is first read as _R_ base format as _X_<sup>base</sup> , and then stochastically converted to _R_ fac consisting of unordered note events _X_<sup>fac</sup> and relation matrices _RS_ . Similar to BERT, the pre-training stage uses “masked language model” (MLM) training objective, where _X_<sup>fac</sup> and _RS_ will be corrupted before fed into MuseBERT, which is trained to reconstruct the original music segment. 

The model adopts the bi-directional Transformer encoder architecture based on the original Transformer implementation described in [23]. The input to the model is the embedding of a corrupted music segment _X_<sup>_∗_</sup> = _{x_<sup>_∗_</sup> _i_<sup>_}N_</sup> _i_ =1<sup>.</sup> The embedding is computed as the sum of all attribute embeddings: 



<!-- Start of picture text -->
Emb( x ∗ i ) = Emb a ( x ∗ i .a ). (6)<br>∑<br>a∈A fac<br><!-- End of picture text -->

## **3.1 Data Corruption** 

The original BERT randomly selects a part of the input tokens to be corrupted. In MuseBERT, data corruption has finer controls: 1) it operates on individual attributes of a note event rather than an entire token, and 2) it corrupts relation matrices as well. 

For note events _X_<sup>fac</sup> , the corrupter randomly selects 15% of the note events _C ⊂ X_ , and corrupts their attributes _{xi.a|xi ∈ C, a ∈A_ fac _}_ in one of the three ways: 1) masked with [MASK] _a_ 80% of the time, 2) replaced with a random token 10% of the time, and 3) kept unchanged 10% of the time. Each attribute is corrupted independently of the choice of the other attributes. For relation matrices _RS_ , each matrix entry will be masked 30% of the time independently. Before corruption, a re-computation of the 

Here Emb _a_ ( _·_ ) are linear embedding layers and the default absolute positional encoding is _not_ applied due to unorderedness. _RS_<sup>_∗_is fed into the model as</sup><sup>_generalized rel-_</sup> _ative positional encoding_ to be discussed in detail in section 3.3. 

The output is a distribution of reconstructed note events in _R_ fac, denoted by _X_<sup>ˆ</sup> = _{x_ ˆ _i}_<sup>_N_</sup> _i_ =1<sup>.Specifically,let</sup><sup>_h_1:</sup><sup>_N_</sup> be the last hidden vector of the Transformer encoder, each note attribute is reconstructed by a separate linear transformation normalized with a softmax layer: 



<!-- Start of picture text -->
p model(ˆ xi.a|X ∗ , RS ∗ ) = softmax(FFN a ( hi )). (7)<br><!-- End of picture text -->

The training loss is the mean of the negative log-likelihood on corrupted attributes _{xi.a|xi ∈ C, a ∈A_ fac _}_ only: 

724 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 



<!-- Start of picture text -->
L (  X ˆ |X ∗ , RS ∗ ) =<br>− 1<br>|C| � �� log  p model( x fac i .a|X ∗, R S ∗ ) �, (8)<br>{i|x ∗ i ∈C} a∈A fac<br><!-- End of picture text -->

From the denoising autoencoder perspective [24], we define the reconstruction distribution _p_ recon( _X_<sup>ˆ</sup> _|X_<sup>_∗_</sup> _, RS_<sup>_∗_) in-</sup> duced from Eqn (7) for later analysis purposes: 



<!-- Start of picture text -->
N<br>p recon(  X ˆ |X ∗ , RS ∗ ) := � p recon(ˆ xi|X ∗ , RS ∗ ), where<br>i =1<br>p recon(ˆ xi|X ∗ , RS ∗ ) := � p recon(ˆ xi.a|X ∗ , RS ∗ ) and<br>a∈A fac<br>p model(ˆ xi.a|X ∗ , RS ∗ ) , xi ∈ C<br>p recon(ˆ xi.a|X ∗ , RS ∗ ) :=<br>� 1 {x ˆ i.a≡x ∗ i .a},  otherwise.<br>(9)<br><!-- End of picture text -->

In other words, during inference, we sample from _p_ model for corrupted tokens while simply keeping the uncorrupted tokens. 

## **3.3 Generalized Relative Positional Encoding** 

Let _h_ 1: _N_ be the hidden vectors at any Transformer layer. We add additional _key-relation embeddings_ Emb<sup>_K_</sup> _S_<sup>(</sup><sup>_·_)of</sup> the relations in the query-value product term by 



<!-- Start of picture text -->
hiW Q � hjW K + � a∈S Emb a K ( r ij a ) � T<br>eij = , (10)<br>√ dz<br><!-- End of picture text -->

where _dz_ is the hidden vector size of attention heads, _W_<sup>_Q_</sup> _, W_<sup>_K_</sup> are query and key transformations, and _eij_ is used to compute attention weights. 

Similarly, we also add _value-relation embeddings_ Emb<sup>_V_</sup> _S_<sup>(</sup><sup>_·_) in the attention weight application:</sup> 



<!-- Start of picture text -->
N<br>zi = � αij � hjW V + � Emb V a ( r ij a ) �, (11)<br>j =1 a∈S<br><!-- End of picture text -->

where _αij_ = softmax _j_ ( _eij_ ), _W_<sup>_V_</sup> is the value transformation, and _zi_ is fed into the position-wise feed-forward sublayer to compute the next layer’s _hi_ . 

In our implementation, both key-relation embeddings and value-relation embeddings are linear transforms. In addition, for different attention layers and attention heads, we train different embeddings. 

We call the above operation _generalized_ relative positional encoding (RPE) because the summation of keyrelation and value-relation embeddings allows us to hint the MuseBERT from multiple musical perspectives (attribute relations), which is not considered in the original RPE implementation [10]. 

BERT model to handle unordered data. We further show that MuseBERT is a powerful controllable music generator, giving birth to various fine-tuning tasks with musical merits. 

## **4.1 Well-definedness of MuseBERT** 

The fundamental assumption made in MuseBERT is the refusal of traditional _sequential_ positional encoding. In return, the mathematical property of MuseBERT we gain is _permutation invariance_ , i.e., the input order will not change the model output. On the other hand, a natural downside of a permutation invariant model is _ambiguity_ : without extra efforts, masked tokens will have the same output distributions and hence not distinguishable. 

The problem is solved by factorized data representation and generalized RPE because the former allows us to specify music in more detail. We summarize the discussion with the well-definedness theorem of MuseBERT. Part one of the theorem is maintained by the property of Transformer [25], and part two is self-evident from the discussion so far. 

**Theorem 1 (Well-definedness)** _Pre-training MuseBERT is well-defined: Let_ ( _X_<sup>_∗_</sup> _, RS_<sup>_∗_)</sup><sup>_beacorruptedmusicseg-_</sup> _ment in Rfac:_ 

_1) (Permutation invariance) Let σ_ ( _·_ ) _be an arbitrary permutation. The reconstruction distribution is unchanged after permutation:_ 



<!-- Start of picture text -->
precon (  X ˆ |X ∗ , RS ∗ )  ≡ precon ( σ ( ˆ X ) |σ ( X ∗ ) ,σ ( R S ∗ ))<br><!-- End of picture text -->

_2) (Unambiguity) For arbitrary pair of xi, xj ∈ X_<sup>_∗_</sup> _, whose attributes are corrupted but their note relations are not, the reconstruction distributions of the two tokens are not always the same, i.e., there exists a set of model parameters such that_ 



<!-- Start of picture text -->
precon (ˆ xi|X ∗ , RS ∗ ) ̸  =  precon (ˆ xj|X ∗, R S ∗ ) .<br><!-- End of picture text -->

## **4.2 MuseBERT as a Music Generator** 

The operations of MuseBERT can be regarded as a single round of a Markov chain transition which alternatively adds noise and denoises (as shown in Figure 1), consisting of four steps: 1) stochastic data conversion to _R_ fac, 2) data corruption, 3) MuseBERT reconstruction, and 4) deterministic data conversion to _R_ base. 

Benjio et al. [26] showed such transition induced from denoising autoencoder is a special type of Generative Stochastic Network and proved that under mild condition, the transition operations form a Markov Chain whose stationary distribution is the true data distribution. Hence, we conclude the pre-training MuseBERT can be used as the MCMC transition operator, and generates music via iterative sampling. 

## **4.3 Controllability of MuseBERT** 

## **4. THEORETICAL ANALYSIS** 

In this section, we first show that _R_ fac and generalized relative positional encoding are theoretical necessities for a 

Moreover, we show that MuseBERT is a Constraint Optimization Problem (COP) solver [27] by regarding uncorrupted attributes or relations as unary or binary constraints, 

725 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

respectively. The COP has the form: 



<!-- Start of picture text -->
max X ˆ p recon(  X ˆ |X ∗ ) (12)<br>s.t. x ˆ i.a  =  x ∗ i .a , ∀x ∗ i ∈/ C, a ∈A fac<br>γa ( xi, xj ) =  γa ( xi ∗, x∗ j ),<br>∀a ∈S if  γa ( x ∗ i , x∗ j ) uncorrupted.<br><!-- End of picture text -->

Apparently, music continuation and in-painting can be formalized as a special COP problem, and monophony, melodic directions, rhythmic patterns, texture, etc. are all expressible concepts by MuseBERT constraints. Hence, MuseBERT, as a music generator, is also controllable, which can be fine-tuned to solve problem-specific generation tasks and controls. 

## **5. FINE-TUNING MUSEBERT** 

By defining problem-specific data corrupters, we can finetune the model for a wide spectrum of conditioned music generation tasks, such as music continuation, inpainting, rhythm or texture-conditioned music generation. In this section, we in turn show two less obvious applications by fine-tuning, in which we extend the vocabulary of _R_ fac to represent chord and vocal tracks, and apply MuseBERT for both generation and analysis. 

## **5.1 Case 1: Texture Generation and Chord Analysis** 

MuseBERT can be fine-tuned for chord and texture controls, which are commonly-studied controlling factors in automatic music generation [28, 29]. The fine-tuning task is set by slight modification from the pre-training stage in two steps: 1) We represent chord progression as _R_ fac events and prepend it to the music segment. Specifically, we define p_hig = 7 for chord event, with p_reg = 0 _,_ p_reg = 1 _,_ p_reg = 2 for chord root, chroma, and bass, respectively. 2) We apply an additional “in-chord” inter-relation to indicate whether a note event is a chordtone or not. The conditioned generation can be trained by masking all the attributes from the music segment while keeping the chord attributes and all relations. Figure 2 shows an example of music generation conditioned on the texture in Figure 2(a) and the chord F major. The generated segment keeps the textural property and deals with inner voices smoothly (shown by the red boxes). 

Similarly, by corrupting the chord events and “inchord” relation, while maintaining the music segment and the other relations, the model can learn to extract chord progressions from a given piece. The fine-tuning result on POP909 [30] shows the model has a 99.35% accuracy on token-wise (MIDI) chord extraction (99.37% for root, 99.05% for chroma and 99.35% for bass). 

## **5.2 Case 2: Accompaniment Refinement** 

In the accompaniment refinement task, we want to refine an imperfect accompaniment according to a given lead melody. To achieve this, we represent the melody and the accompaniment both as _R_ fac and concatenate them 



<!-- Start of picture text -->
F#m<br>a) An original piece in F#m chord.<br>F Pitch relation maintained by "“add4"<br>b) The generated piece in F chord using<br>the texture of a).<br><!-- End of picture text -->

**Figure 2** . An example of controlled generation by specifying chord and texture. 

together. We then randomly corrupt some accompaniment attributes while keeping the melody and relations unchanged during training. Figure 3 shows an example of accompaniment refinement from a corrupted sample Figure 3(a). In (a), the red note heads mark the note being replaced and the masked notes are replaced by rests. The result shows that the generated piece is more consistent with the melody while keeps the original musical content. 



<!-- Start of picture text -->
a) A corrupted accompaniment.<br>b) The generated accompaniment.<br><!-- End of picture text -->

**Figure 3** . An example of accompaniment refinement conditioned on melody. 

## **6. EXPERIMENTAL RESULT** 

## **6.1 Dataset and Training** 

We collect around 5K classical and popular piano pieces from Musicalion<sup>4</sup> and the POP909 dataset [30]. We only keep the pieces with 2/4 and 4/4 meters and cut them into 8-beat music segments. In all, we have 19.8K samples. We randomly split the dataset (at song-level) into training set (90%) and test set (10%). All training samples are further augmented by transposing to all 12 keys. 

We pre-train our MuseBERT using 12 Transformer layers with 8 attention heads, 0.1 dropout rate, and GELU ac- 

> 4 Musicalion: https://www.musicalion.com. 

726 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

tivation [31]. The hidden dimensions of self-attention and position-wise feed-forward layers are _d_ model = 256 and _d_ ff = 512. We train with a batch size of 128 and Adam optimizer with learning rate of 5e-4 and linear learning rate decay to 5e-6 after 15K warmup steps. The pre-training takes 20 epochs to converge. 

In fine-tuning tasks, we kept the same hyperparameters except the initial learning rate is 2e-4 without warmup. The epochs to fine-tune the model are task-specific, approximately 4 epochs on average. 

## **6.2 Objective Evaluation** 

Given that _R_ fac and data corruption are stochastic, we evaluate the expectation of reconstruction likelihood in terms of token-wise onset, pitch and duration, similar to the algorithm in [4]. We compare among 1) the pre-trained MuseBERT, 2) the fine-tuned models using attribute-specific data corrupters, and three baseline models ablating the use of factorized attributes _A_ fac and binary relations. Table 1 summarizes the results where we see our pre-trained model outperforms the baselines on all three criteria and the finetuned model can perform even better. The use of _A_ fac and binary relations not only makes the model well-defined, but also are crucial for high-quality reconstruction. 

|Models|**Onset**|**Pitch**|**Duration**|
|---|---|---|---|
|_A_fac w/ rel (ours)|**0.902**_±_**0.002**|**0.813**_±_**0.003**|**0.815**_±_**0.003**|
|_A_fac w/o rel<sup>_∗_</sup>|0.472_±_0.002|0.740_±_0.004|0.743_±_0.003|
|_A_base w/ rel|0.856_±_0.001|0.785_±_0.004|0.785_±_0.003|
|_A_base w/o rel<sup>_∗_</sup>|0.488_±_0.003|0.733_±_0.003|0.733_±_0.002|
|_A_fac w/ rel (fine-tuned)|**0.958**_±_**0.001**|**0.924**_±_**0.002**|**0.927**_±_**0.002**|



**Table 1** . Objective evaluation of the expectation of reconstruction likelihood. Here, “w/ rel” and “w/o rel” indicates whether generalized RPE is applied, and “ _∗_ ” indicates the ill-defined models. 

## **6.3 Self-attention Visualization** 

We observe that different attention heads of multiple layers in the pre-trained MuseBERT captures high-level music knowledge. As shown in Figure 4, metrical structure is revealed in (a) & (b), and voice-leading can be seen in (c) & (d). We show the attention matrices on a piano-roll for better interpretability, where an arrow _xi → xj_ shows the ( _j, i_ ) entry and the brightness indicates the attention strength. 

## **6.4 Subjective Evaluation of Music Generation** 

We invite people to subjectively rate the generation quality of the pre-trained model through a double-blind online survey. During the survey, the subjects listen to 8 groups of samples, each containing 4 generated segments together with a ground-truth human composition. The generated segments come from the four models (the same as in Table 1 excluding the fine-tuned model) with the same initial corruption state (60% of the total tokens) from the original piece. Both the order of groups and the sample order within each group are randomized. After listening 



<!-- Start of picture text -->
0.6<br>a) (layer: 4, head: 5) of a piece X. b) (layer: 4, head: 5) of another piece Y.<br>0.4<br>0.2<br>c) (layer: 5, head: 7) of X. d) (layer: 5, head: 7) of Y.<br><!-- End of picture text -->

**Figure 4** . Visualization of attention matrices on selected self-attention layers in pre-trained MuseBERT. 



<!-- Start of picture text -->
Human composition Atac w/o rel Abase w/o rel<br>Afac w/ rel (our method) Abase w/ rel<br>Creativity Naturalness Musicality<br><!-- End of picture text -->

**Figure 5** . Subjective evaluation results on pre-trained MuseBERT. 

to each sample, the subjects rate them based on a 5-point scale from 1 (very low) to 5 (very high) according to three criteria: _creativity_ , _naturalness_ and _musicality_ . 

A total of 37 subjects (15 females and 22 males) with different musical backgrounds have completed the survey. The aggregated result (as shown in Figure 5) shows that the pre-trained models considering music relations (the well-defined models) are significantly better than the models without relations (the ill-defined models) (with p-value _<_ 0 _._ 005), and are marginal to the human composition (with p-value _>_ 0 _._ 05). 

## **7. CONCLUSION** 

In conclusion, we contributed MuseBERT, a full treatment of BERT in the music domain as a powerful music understanding and generation model. The main novelty lies in the proposed _generalized_ relative positional encoding, which successfully reveals the non-sequential, polyphonic structure of music and at the same time turns the masked language model objective into a well-defined controllable generative framework. Also, with the music-tailored factorized data representation, the controls are fine-grained. Furthermore, by fine-tuning MuseBERT, we demonstrate that the model is _general purpose_ , capable of various downstream tasks such as chord analysis, accompaniment generation and refinement etc. as long as the constraints can be expressed via binary relations of different music attributes. 

727 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

## **8. REFERENCES** 

- [1] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, “Bert: Pre-training of deep bidirectional transformers for language understanding,” _arXiv preprint arXiv:1810.04805_ , 2018. 

- [2] G. Hadjeres, F. Pachet, and F. Nielsen, “Deepbach: a steerable model for bach chorales generation,” in _International Conference on Machine Learning_ . PMLR, 2017, pp. 1362–1371. 

- [3] Y. Yan, E. Lustig, J. VanderStel, and Z. Duan, “Partinvariant model for music generation and harmonization.” in _19th International Society for Music Information Retrieval_ , 2018, pp. 204–210. 

- [4] C.-Z. A. Huang, T. Cooijmans, A. Roberts, A. Courville, and D. Eck, “Counterpoint by convolution,” _arXiv preprint arXiv:1903.07227_ , 2019. 

- [5] C.-Z. A. Huang, A. Vaswani, J. Uszkoreit, N. Shazeer, I. Simon, C. Hawthorne, A. M. Dai, M. D. Hoffman, M. Dinculescu, and D. Eck, “Music transformer,” _arXiv preprint arXiv:1809.04281_ , 2018. 

- [6] Y.-S. Huang and Y.-H. Yang, “Pop music transformer: Generating music with rhythm and harmony,” _arXiv preprint arXiv:2002.00212_ , 2020. 

- [7] I. Simon and S. Oore, “Performance rnn: Generating music with expressive timing and dynamics,” https:// magenta.tensorflow.org/performance-rnn, 2017. 

- [8] W.-Y. Hsiao, J.-Y. Liu, Y.-C. Yeh, and Y.-H. Yang, “Compound word transformer: Learning to compose full-song music over dynamic directed hypergraphs,” _arXiv preprint arXiv:2101.02402_ , 2021. 

- [9] J. Jiang, G. Xia, and T. Berg-Kirkpatrick, “Discovering music relations with sequential attention,” in _Proceedings of the 1st workshop on NLP for music and audio (NLP4MusA)_ , 2020, pp. 1–5. 

- [10] P. Shaw, J. Uszkoreit, and A. Vaswani, “Self-attention with relative position representations,” _arXiv preprint arXiv:1803.02155_ , 2018. 

- [11] C. Raffel and D. P. Ellis, “Intuitive analysis, creation and manipulation of midi data with pretty midi,” in _15th International Society for Music Information Retrieval conference late breaking and demo papers_ , 2014, pp. 84–93. 

- [12] M. S. Cuthbert and C. Ariza, “music21: A toolkit for computer-aided musicology and symbolic music data,” 2010. 

- [13] “Garageband for mac.” [Online]. Available: https: //www.apple.com/mac/garageband/ 

- [14] “Logic pro.” [Online]. Available: https://www.apple. com/logic-pro/ 

- [15] “Cubase guides you on your music production journey.” [Online]. Available: https://new.steinberg. net/cubase/ 

- [16] Z. Wang, Y. Zhang, Y. Zhang, J. Jiang, R. Yang, J. Zhao, and G. Xia, “Pianotree vae: Structured representation learning for polyphonic music,” _arXiv preprint arXiv:2008.07118_ , 2020. 

- [17] D. Jeong, T. Kwon, Y. Kim, and J. Nam, “Graph neural network for music score data and modeling expressive piano performance,” in _International Conference on Machine Learning_ . PMLR, 2019, pp. 3060–3070. 

- [18] H. H. Mao, T. Shin, and G. Cottrell, “Deepj: Stylespecific music generation,” in _IEEE 12th International Conference on Semantic Computing_ . IEEE, 2018, pp. 377–382. 

- [19] E. S. Koh, S. Dubnov, and D. Wright, “Rethinking recurrent latent variable model for music composition,” in _IEEE 20th International Workshop on Multimedia Signal Processing_ . IEEE, 2018, pp. 1–6. 

- [20] H.-W. Dong, W.-Y. Hsiao, L.-C. Yang, and Y.-H. Yang, “Musegan: Multi-track sequential generative adversarial networks for symbolic music generation and accompaniment,” in _32nd AAAI Conference on Artificial Intelligence_ , 2018. 

- [21] F. Lerdahl and R. S. Jackendoff, _A Generative Theory of Tonal Music, reissue, with a new preface_ . MIT press, 1996. 

- [22] F. Lerdahl, _Tonal pitch space_ . Oxford University Press, 2004. 

- [23] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. Kaiser, and I. Polosukhin, “Attention is all you need,” _arXiv preprint arXiv:1706.03762_ , 2017. 

- [24] P. Vincent, H. Larochelle, Y. Bengio, and P.-A. Manzagol, “Extracting and composing robust features with denoising autoencoders,” in _International Conference on Machine Learning_ , 2008, pp. 1096–1103. 

- [25] J. Lee, Y. Lee, J. Kim, A. Kosiorek, S. Choi, and Y. W. Teh, “Set transformer: A framework for attentionbased permutation-invariant neural networks,” in _International Conference on Machine Learning_ . PMLR, 2019, pp. 3744–3753. 

- [26] Y. Bengio, E. Laufer, G. Alain, and J. Yosinski, “Deep generative stochastic networks trainable by backprop,” in _International Conference on Machine Learning_ . PMLR, 2014, pp. 226–234. 

- [27] S. Russell and P. Norvig, “Artificial intelligence: a modern approach,” 2002. 

- [28] Z. Wang, D. Wang, Y. Zhang, and G. Xia, “Learning interpretable representation for controllable polyphonic music generation,” _arXiv preprint arXiv:2008.07122_ , 2020. 

728 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

- [29] I. Simon, A. Roberts, C. Raffel, J. Engel, C. Hawthorne, and D. Eck, “Learning a latent space of multitrack measures,” _arXiv preprint arXiv:1806.00195_ , 2018. 

- [30] Z. Wang, K. Chen, J. Jiang, Y. Zhang, M. Xu, S. Dai, X. Gu, and G. Xia, “Pop909: A pop-song dataset for music arrangement generation,” _arXiv preprint arXiv:2008.07142_ , 2020. 

- [31] D. Hendrycks and K. Gimpel, “Gaussian error linear units (gelus),” _arXiv preprint arXiv:1606.08415_ , 2016. 

729 

