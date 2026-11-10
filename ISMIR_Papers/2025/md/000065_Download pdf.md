---
paper_id: "000065"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706519/files/000065.pdf"
---

# ADAPTIVE PATH OF PREDICTION: AN UNSUPERVISED METHOD FOR MODELING NOTE-LEVEL INFORMATIONAL HIERARCHY OF POLYPHONY 

## Xiaoxuan Wang 

EPFL 

```
xiaoxuan.wang@epfl.ch
```

## Martin Rohrmeier 

EPFL 

```
martin.rohrmeier@epfl.ch
```

### ABSTRACT 

Polyphonic music presents a unique challenge for computational modeling due to the complex interactions of multiple simultaneous musical streams and the need to capture both local and global structural relationships. We propose Adaptive Path of Prediction, a discrete diffusion model that learns the informational hierarchy of polyphony in an unsupervised manner. By training the model to find optimal note-removal paths, and to reversibly reconstruct these selectively removed notes, we reveal how critical musical events, which persist until later stages of data corruption, maximize the preserved information and guide the prediction of remaining content. Drawing on compression learning theory, we posit that such adaptively-discovered “anchor notes” reflect the system’s ability to make an explicit abstraction of polyphonic music. Our experiments demonstrate that the model converges on consistent noteimportance distinctions and can achieve better reconstruction performance in selected denoising paths than random ones. Furthermore, the model’s assignment of note importance during the training process increasingly aligns with a reductive music analysis dataset, suggesting that our unsupervised framework can uncover structural hierarchies consistent with established music-theoretical views. 

### 1. INTRODUCTION 

Polyphony describes a very common musical phenomenon in which multiple streams of notes occur simultaneously. When perceiving a polyphonic piece, a cognitive system experienced with the complexity of polyphony identifies the interactions and relationships between musical structures, thereby forming an understanding of their roles and structural hierarchy [1, 2]. Using machine learning methods to model the structural understanding of polyphony is non-trivial because of the scarcity of note-level labels of structural hierarchy for supervised learning and the inherent complexity of polyphony, which demands systems ca- 

> © X. Wang, and M. Rohrmeier. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: X. Wang, and M. Rohrmeier, “Adaptive Path of Prediction: An unsupervised method for modeling note-level informational hierarchy of polyphony”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

pable of capturing both local and long-distance structural relationships [3,4]. 

The lack of labeled data and the fact that human music acquisition usually happens without explicit instructions about structural relationships between notes highlight the importance of unsupervised learning on this problem. Most unsupervised learning models for melody, rhythm, or harmony structure (e.g., n-gram models [5]) rely on two assumptions: (a) perfect perception, meaning the model captures all input information and uses all of the information to update the parameters regardless of complexity, and (b) autoregressive prediction, meaning the model always makes left-to-right predictions using the previous context of the sequence, which only allows unidirectional dependencies P (xt|x<t) ≈ P (xt|x1, x2, . . . , xt−1). 

With multiple simultaneous lines unfolding in time, our cognitive system is unlikely to process all note-level information and relationships in one pass [6]. This challenges assumption (a). However, a highly important feature of music, and music listening, is repetition; compositions often repeat musical phrases, and listeners frequently revisit pieces. Repetition allows listeners to focus on different elements to discern how notes are organized into polyphonic structures [7, 8]. During this process, notes at different time points may be explicitly remembered. This memory enables the use of bi-directional information when forming predictions, which challenges assumption (b). In other words, due to the complex nature of polyphony that invites repeated listening, a purely autoregressive method— one that lacks an explicit mechanism for retaining and reusing previously attended notes—may provide an incomplete picture of polyphonic relationships, especially from a cognitive science perspective. 

Recognizing the importance of bi-directional information, a natural question to ask is how to determine which notes should be explicitly memorized. Compression learning theory [9] suggests that a cognitive system is internally rewarded when it discovers the regularities of the complex environment and learns to optimally compress it. Therefore, acquiring an adaptive abstraction and generative capability for a particular class of data (e.g., tonal music) can be highly advantageous as it removes the need to devise a separate compression scheme for each data point. Therefore, if a system can quickly identify a set of explicit “anchor notes” that encapsulate a polyphonic phrase’s fundamental information distributions and long-distance depen- 

565 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

dencies, these anchors can guide predictions for less critical details. In other words, anchor notes are the system’s explicit abstraction of the phrase, they reflect the system’s understanding of note-level informational hierarchy. 

Motivated by these considerations, we propose the Adaptive Path of Prediction, an unsupervised model that learns the informational hierarchy of notes and can explicitly report them. We adopt Diffusion Denoising [10], a generative framework that iteratively corrupts the input data and learns to reconstruct it. 

In this study, we investigate an optimized path for data corruption and reconstruction for symbolic music. We replace the conventional random corruption process with a system that learns to preserve the structurally important elements to benefit the reconstruction process. Our proposed model has two parts: a Diffusion Ordering Network and a Denoising Network. Specifically, the Diffusion Ordering Network is trained using reinforcement learning, leveraging feedback from the Denoising Network to optimize the selection of the data corruption path. 

To allow an accurate discrete diffusion for polyphony, we avoid sequential methods for temporal encoding. Instead, we develop a new encoding method for symbolic music: a musical graph that minimizes time dependencies between notes. 

To summarize, our contributions include: (1) the first unsupervised method that learns to explicitly report notelevel informational hierarchy in polyphony; (2) the first investigation of using non-autoregressive prediction to model structural cognition of polyphony; and (3) a novel graph-based symbolic representation of polyphony that minimizes temporal dependencies between notes. 

### 2. RELATED WORKS 

### 2.1 Compression learning theory 

To maintain stability in a dynamic environment, biological agents are driven to minimize long-term sensory surprise by refining their predictive capabilities [11]. In doing so, we naturally adopt encoding strategies that enhance our ability to predict sequences of events [12]. However, given our limited cognitive resources, we must develop concise and generalized representations that capture input regularities, rather than creating a unique encoding for each event sequence [9,13]. This drive to optimize our encoding strategy fuels our curiosity: rather than permanently increasing cognitive load, temporarily allocating resources to extract the regularities of novel stimuli ultimately refines our adaptive model of environmental patterns and reduces the cognitive load [14, 15]. In other words, our innate curiosity motivates us to encounter unfamiliar music not merely to learn its specific structure, but also to refine a flexible strategy of listening—one that enhances our ability to understand, predict, and appreciate diverse musical works. Moreover, compression learning is inherently generative and creative. By mastering a succinct representation of regularities, the cognitive system is empowered to synthesize novel content based on an abstracted framework [16]. 

This capability contrasts sharply with conventional statistical models, which are typically restricted to reproducing the patterns they have already encountered [3]. 

### 2.2 Modeling music long-distance dependencies and structural hierarchy 

Theoretical frameworks like musical grammars have been used to model long-distance dependencies and structural hierarchy [17, 18], yet unsupervised approaches for capturing note-level hierarchy in polyphony remain scarce. A notable exception is the Music Transformer [19], which utilizes self-attention mechanisms to capture both local and long-distance relationships between notes in polyphonic music. Although visualizations of self-attention provide insights into these relationships and corresponding notes’ importance [20], such analyses yield an indirect interpretation of the model’s understanding. Moreover, while Transformer-based models can, in principle, represent long-range dependencies through self-attention, they still rely on an autoregressive decoding order. Our motivation is to propose a framework where the structure of prediction itself is order-adaptive and interpretable. 

### 2.3 Diffusion denoising models 

Diffusion denoising models [10, 21] have opened a new path for generative modeling. Although most early applications focused on continuous domains (e.g., images), discrete diffusion methods have now emerged to handle symbolic data [22]. Discrete diffusion has also been applied in the symbolic music generation task [23]. 

Diffusion denoising models generally follow an abstract-to-concrete generation scheme. Due to this nature, it has been used to generate music in explicit hierarchical steps, from form to phrases, and melodies and accompaniments [24]. However, there are no existing studies that use the diffusion denoising model as a tool for unsupervised learning of the structural hierarchy of polyphony. 

An important variant of discrete diffusion models is the autoregressive discrete diffusion model [25], which sequentially absorbs one dimension at a time in forward diffusion. It keeps the diffusion model’s non-sequential generation capability while limiting the number of diffusion steps to at most the input data’s dimensionality. Recent work in molecular graph generation has extended this framework by introducing Diffusion Ordering Networks that learn optimal, data-dependent absorption trajectories [26]. These learned paths provide a powerful mechanism for explicitly modeling structural dependencies—an ability conceptually aligned with compression learning theory. Unlike the variational autoencoder [27], which compresses data into a latent space, this approach offers the potential to produce explicit and interpretable compressed representations of music. This motivates our work, which applies discrete diffusion and learned ordering mechanisms to the unsupervised learning of note-level informational hierarchies in polyphonic music, thereby revealing the inherent structural dependencies of polyphonic compositions. 

566 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
Diffusion Ordering Network Average<br>(deletes one note per step) Denoising<br>Performance<br>ood<br>Trajectory 1<br>Trajectory 2<br>0<br>Trajectory 3<br>Bad<br>Denoising Network Denoising<br>(predicts the deleted note) performance<br><!-- End of picture text -->

Figure 1. Illustration of a training step of our model 

### 3. METHOD 

### 3.1 Adaptive Ordering for Music Discrete Diffusion 

Our model adapts absorbing state diffusion (as in D3PMs, [22]) for symbolic music by introducing two key modifications. First, rather than using an absorbing state mask for data corruption, we simply delete notes. We think the deletion process is conceptually closer to the music reduction analysis, which may encourage the model to better exploit the remaining note information and learn an explicit informational hierarchy. The feasibility of deletion action rests on our graph-based data representation, which will be discussed in the next subsection. Second, We replace the random forward diffusion process q(xt|xt−1) with an adaptive Diffusion Ordering Network qφ(nt|xt, x0) [26], that selects, at each step t, the note nt to remove. 

Our system comprises two co-evolving components: the Diffusion Ordering Network and the Denoising Network pθ(nt−1|xt). The Denoising Network predicts the most recently removed note nt−1 given the current input xt, while the Diffusion Ordering Network learns a structurally-dependent note removal order that benefits reconstruction. In training, the ordering network’s direct goal is to remove less-important notes at each step, thereby indirectly preserving “anchor notes.” 

Figure 1 illustrates a single training step for the Diffusion Ordering Network, where it samples M trajectories. In every step t of every trajectory m, the denoising network generates a probability distribution of its predictions of the pitch label, the onset position, and the offset position of the removed note nt−1. The negative cost of these predictions in all steps and trajectories will be accumulated and serve as the feedback for the reinforcement learning of the Diffusion Ordering Network, therefore, we define the reward Rt,m in Eq. (1) as: 



<!-- Start of picture text -->
Rt,m = − − ( T T  −t ) log pθ n ( t− m 1 ) x t (m) . (1)<br><!-- End of picture text -->

Note that Rt,m is also weighted by the position<sup><mark>(</mark>T</sup> T<sup>−t</sup><sup><mark>)</mark></sup> in the trajectory to emphasize the effectiveness of the preserved “anchor notes” for data reconstruction. 

To reduce variance in the raw stepwise rewards, we adopt an advantage actor-critic (A2C) paradigm [28]: we introduce a Critic Network Vψ(x) that estimates the value of the current input x. The advantage at step t of trajectory m is then 



<!-- Start of picture text -->
At,m = Rt,m + γ Vψ xt+1 − Vψ xt , (2)<br>where the discount factor γ controls how strongly future<br>rewards are weighted relative to immediate rewards.<br><!-- End of picture text -->

The Diffusion Ordering Network qφ(nt|xt, x0) plays the role of the actor. Under the advantage actor-critic framework, its parameters are updated by ascending the advantage-weighted log-likelihood: 



<!-- Start of picture text -->
M T<br>1<br>∆φ ← At,m ∇φ log qφ nt xt, x0 .<br>M T ∑∑ m=1 t=1<br>(3)<br><!-- End of picture text -->

Meanwhile, the Critic Network Vψ(x) is updated by minimizing the temporal-difference error (i.e., squared advantage) between its prediction and the bootstrapped return: 



<!-- Start of picture text -->
M T<br>1 2<br>L(ψ) = At,m . (4)<br>M T<br>∑ m=1 ∑( t=1<br><!-- End of picture text -->

Minimizing Eq. (4) ensures that the Critic Network accurately estimates the true return, stabilizing the advantage used in the actor update (Eq. (3)). Together, these updates define the Diffusion Ordering Network’s parameter update. 

We now turn to the Denoising Network’s updates. During the update iteration for the Denoising Network, in each step t of every trajectory m, the Denoising Network pθ predicts the probability of the removed note nt−1 given the current musical input xt. We measure the negative loglikelihood and accumulate it across all steps and trajectories. Here, we again use the weight factor<sup><mark>(</mark>T</sup> T<sup>−t</sup><sup><mark>)</mark></sup> <mark>.</mark> Hence, the total training loss of the Denoising Network over M sampled trajectories can be written as: 



<!-- Start of picture text -->
M T<br>1<br>L(θ) = M T − ( T T  −t ) log pθ n ( t− m 1 ) x t (m )) ) .<br>∑ m=1 ∑ t=1 (<br>(5)<br><!-- End of picture text -->

567 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

To update the parameters θ of the Denoising Network, we take gradient steps that minimize L(θ): 



<!-- Start of picture text -->
∆θ ←−∇θ L(θ). (6)<br><!-- End of picture text -->

This step is performed separately from the reinforcement learning update of the Diffusion Ordering Network qφ (Eq. (3)). By alternating the two training procedures in time, we ensure that the Denoising Network’s gradients do not interfere with the Diffusion Ordering Network’s policy gradients. Specifically, in one training iteration: 

1. Sampling for the Diffusion Ordering Network: Sample M trajectories using qφ and, for each trajectory, compute the rewards {Rt,m} and advantages {At,m} (see Eqs. (1) and (2)). 

2. Updating the Diffusion Ordering Network: Update the actor parameters φ and critic parameters ψ (see Eqs. (3) and (4)). 

3. Sampling for the Denoising Network: Sample M trajectories using qφ. 

4. Updating the Denoising Network: Compute the total denoising loss L(θ) over trajectories as in Eq. (5) and update the parameters θ (see Eq. (6)). 

### 3.2 Data Representation 

Previous studies proposed graph-based encodings of symbolic music by linking notes via relative temporal relationships [29, 30]. While effective for certain tasks, these encodings become inflexible when supporting dynamic operations like note deletion, where temporal edges must be constantly updated. To address this, we propose a metricaltree-based representation that encodes timing via hierarchical metrical nodes, aiming to minimize temporal dependencies and support flexible note deletion. 

Metrical nodes are generated from the measure level through successive binary and ternary divisions. The type of division is distinguished by the edge type, and node labels encode their layer information. Each pitch-labeled note node connects via onset and offset edges to the shallowest relevant metrical node, encoding its rhythmic position. 

Note nodes interconnect through directed interval edges labeled by octave-invariant pitch intervals, facilitating the capture of long-distance musical relationships while reducing edge-type complexity. Although these interval edges assist predictive modeling, their reconstruction is not required for the Denoising Network. 

All edges are directed for the graph neural network to flexibly capture relationships. Edges that seem bidirectional in the visualization actually represent overlapping pairs of directed edges. 

Figure 2 illustrates a simplified example of this representation. For visual clarity, interval edges (with distinct labels) are colored uniformly, and only three metrical levels are shown, without triplet subdivisions; the full training graphs contain four metrical levels with comprehensive divisions. 



<!-- Start of picture text -->
①efefefff<br>E5<br>G4 G4 G4<br>E4 妇<br>C4<br>1M<br>-L1<br>L3+<br><!-- End of picture text -->

Figure 2. A simplified example of our music graph representation. 

### 3.3 Network Architecture 

For input encoding, the actor component of the Diffusion Ordering Network incorporates the original music graph and previously deleted nodes differentiated by sinusoidal positional encodings [31]. The Denoising Network introduces a special "super node" labeled "mask", connected via "mask" edges to all remaining nodes to aggregate global information. The actor and critic components of the Diffusion Ordering Network, along with the Denoising Network, share a similar encoder architecture but maintain separate parameters. Each encoder transforms node labels into 256-dimensional embeddings, which are subsequently processed through an alternating sequence (with residual connections) of three Relational Graph Convolutional Network [32] layers (corresponding to distinct graph edge types) and three Graph Attention Network [33] layers, each with 4 attention heads. 

Decoding methods differ per component: the actor of the Diffusion Ordering Network decodes node embeddings through a four-layer MLP (dimension 256) with ReLU, employing an output mask to restrict selections to currently available note nodes. The critic compresses via mean pooling and a four-layer MLP with ReLU to get a scalar value estimating the graph value. Due to the complexity of the Denoising Network’s task, we apply additional refinement of embeddings through a 4-layer MLP. Decoding in this network is divided into pitch selection, directly derived from the super node embedding processed through a 3- layer MLP; and onset-offset predictions, which stack embeddings from attachable metrical nodes (metrical nodes without vertical parent onset nodes) with the super node embedding. These combined embeddings are independently processed through specialized onset and offset 3- layer MLP decoders, each finalized with softmax activation. 

### 3.4 Training Details 

We train our model using a combined dataset comprising Bach chorales and Bach English and French Suites sourced 

568 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

from the Distant Listening Corpus [34] for one epoch. Four-measure musical segments are represented as graphs, employing a sliding window technique to avoid segmentation bias. During each training step, we use a batch size of 4 and sample 16 trajectories per graph for the diffusion ordering network. The discount factor γ for Eq. (2) is set to 0.99. All networks are optimized using the AdamW optimizer with a learning rate of 2e-4. Training is conducted on an RTX 4080 Laptop GPU for 122 hours. 

### 4. EXPERIMENTS 

### 4.1 Objective Measurements 

### 4.1.1 Consistency of Note Importance Assignment 

To evaluate whether the Diffusion Ordering Network finds a consistent strategy for ordering note-removal (i.e., assigning note importance), we measure the divergence of its note-removal trajectories on unseen data. Every 20 training iterations, we perform a validation step on 8 graphs, randomly selected from the validation dataset. For each graph, the Diffusion Ordering Network will sample 16 trajectories. We then compute the pairwise edit distance between these trajectories, and get the averaged edit distance as a metric of trajectory divergence. For comparison, we also collect the averaged edit distance of 16 randomly sampled trajectories. 



<!-- Start of picture text -->
80<br>Diffusion Ordered Trajectories<br>Random Trajectories<br>Edit Distance70 0 50 0 30<br>20<br>0 100 200 300 400 500<br>Iteration<br><!-- End of picture text -->

Figure 3. Comparison of trajectory divergence 

As Figure 3 shows, as the training proceeds, the Diffusion Ordering Network’s arrangement of note removal order in different sampling trajectories gradually converges. At the end of training, we test with the entire test set. The Diffusion Ordering Network achieves an average divergence of 15.25 ± 5.19, while the random baseline yields 50.64 ± 14.03. These results demonstrate that our model learns a note removal ordering strategy that is generalized to unseen polyphonic music. 

### 4.1.2 Reconstruction Performance 

To assess whether the note removal order identified by the Diffusion Ordering Network benefits the reconstruction performance of the Denoising Network, we train a baseline model without the Diffusion Ordering Network (with a random forward diffusion q(xt|xt−1), all other training settings remain the same), and we examine their reconstruction/denoising performance by measuring teacher- 

|Model|Raw NLL|Scaled NLL|
|---|---|---|
|Diffusion Ordered|9.89±1.22|4.92±0.60|
|Baseline|10.96±1.05|5.64±0.49|



Table 1. Comparison of reconstruction performance 

forcing negative log-likelihood (NLL) in the test set. For each test sample, we generate 16 trajectories. 

We evaluate both the raw and weighted NLL (see Eq. (5)). With the same training iteration, our model that uses a Diffusion Ordering Network demonstrates lower NLL in both raw and weighted measures. 

### 4.2 Visualizing the Importance of Notes 



<!-- Start of picture text -->
17 19 2 12 1 7 16 10 4 15 final9<br>(a)<br>final<br>3 14 5 11<br>17 19 12 21 1610 15 final<br>(b)<br>final<br>14 11<br>(c)<br><!-- End of picture text -->

Figure 4. Minuet in G major, BWV Anh. 114 in (a) full score with order of removal, (b) top 50 percent reserved notes, and (c) reductive analysis by Kirlin [35]. 

Figure 4 illustrates the model-identified notes information hierarchy in the first four measures of Christian Petzold’s Minuet in G major (BWV Anh. 114). In panel (a), each note is labeled by the order in which it is removed; darker notes and higher numerical labels (or “final”) indicate notes retained until later stages of the data corruption process. In panel (b), we show only the top 50 percent of these retained notes. Panel (c) shows Kirlin’s reductive analysis of the phrase following Schenkerian analysis [35]. Musical reductive analyses, such as those of Schenker, provide a framework by which ornamental notes are progressively absorbed to reveal the condensed structural foundations of a melody or harmony [36]. In this example, the notes retained by the Diffusion Ordering Network closely align with those that a human analyst (i.e., Kirlin) would label as foundational to the structure of the musical phrase. 

### 4.3 Comparison with Reductive Music Analysis 

To examine our model’s note importance assignment with music reduction analyses on a larger scale, we employ the largest available Schenkerian analysis dataset available in machine-readable format [37]. Although the dataset is primarily based on note sequences (melodies or sequences 

569 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

that only imply multiple voices) rather than full polyphony, it still offers a useful resource to test our model. 

Every 20 training iterations, we perform a validation step, where we run our Diffusion Ordering Network on the music example of the dataset. We use Spearman’s Rho with repeated ranks to measure the correlation between the Diffusion Ordering Network’s note removal order and the hierarchical depth labels. In the annotations of [37], higher hierarchical depth indicates greater structural importance. 



<!-- Start of picture text -->
0.35<br>Rho0.250.30<br>0.20<br>0.15<br>0.10<br>Spearman's 10.05<br>0.00 0 100 200 300 400 500<br>Iteration<br><!-- End of picture text -->

Figure 5. The correlation change between note removal order and the labeled notes depth from [37] during training 

Figure 5 shows an increasing correlation between note removal order and depth labels. Although the final average Spearman’s Rho only reaches 0.34, it should be emphasized that our model is trained without any explicit labels of notes’ structural importance. 

### 5. DISCUSSION 

The above experiments show that the cooperative training of the Denoising Network and the Diffusion Ordering Network discovers a generalized strategy to order notes based on informational importance for unseen data. Learning this ordering can improve data reconstruction performance. And the correlation of this order with music reduction analysis shows that our unsupervised approach can at least partially uncover structural hierarchies consistent with established music theory. Taken together, these results indicate that the order found by the collaborative optimization of our two networks actually exploits the dependencies in polyphonic music, rather than reaching an arbitrary agreement on a random order. 

One likely reason for the moderate correlation level is the continuous nature of the note-removal path, whereas reductive annotations commonly group notes into discrete levels of structural importance. Music reduction’s discrete grouping of importance implies that human perception of notes’ hierarchy may also be discretized, prompting future work on segmenting our continuous order of importance into discrete layers. One potential method could be analyzing the change in information content and entropy in the adaptive order of prediction. A remaining challenge is the lack of large-scale, standardized subjective ratings of note-level importance, which makes it difficult to fully validate our unsupervised framework against human perception. Consequently, exploring behavioral paradigms to 

access participants’ assignment of note importance hierarchies would provide deeper insights into how well the learned hierarchy reflects real-world listening experiences. 

The mathematical foundation of this study references the approach described in [26], yet our focus differs substantially. Whereas [26] is primarily concerned with the efficient prediction of new molecular structures, our work aims at modeling the structural understanding of a given musical stimulus. Consequently, our method introduces three primary innovations relative to its framework: (1) a graph representation and action space tailored to musically meaningful factors, (2) an Advantage ActorCritic (A2C) update scheme [28] rather than simple REINFORCE (without baselines) [38] to stabilize the diffusion order, and (3) newly proposed validation and visualization methods specifically designed to assess the effectiveness of the adaptive note-removal order. 

Despite operating on limited computational resources and a relatively small, genre-specific dataset, our method stands out as one of the first unsupervised approaches that explicitly models note importance in polyphonic music. Compared to earlier research on music reduction and hierarchical modeling, our approach uses a fully data-driven, reinforcement-learning paradigm. Expanding the training corpus both in size and stylistic diversity could help the model learn more robust, cross-composer adaptive strategies. Meanwhile, building separate models for different genres or composers may also reveal how stylistic conventions influence hierarchical note-importance assignments. 

Finally, although we showcase our approach in a graphbased representation, it could readily extend to other symbolic representations (e.g., pianoroll variants or OctupleMIDI [39]) that encode time with minimal betweennote dependencies, potentially broadening applicability. 

### 6. CONCLUSION 

In this paper, we introduced a discrete diffusion framework, Adaptive Path of Prediction, that learns to model note-level informational hierarchy in polyphonic music without relying on any explicit labels. Through a collaborative training process, the Diffusion Ordering Network and Denoising Network converge on an adaptive noteremoval path, which, in turn, enhances reconstruction performance. Our experiments demonstrate that the learned ordering aligns—at least partially—with established music reduction analyses, suggesting that the ordering successfully captures rhythmic, melodic, and harmonic structural dependencies. 

Our method is readily adaptable to other symbolic representations. And it could benefit from the introduction of additional constraints reflecting music psychological or theoretical principles. Our proposed framework highlights that controlled diffusion approaches can explicitly report the learned structural hierarchies previously latent in the deep learning modeling of music. It paves the way for larger, broader, and more nuanced unsupervised models for structural analysis of music. 

570 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

### 7. ACKNOWLEDGEMENTS 

We thank all members of the Digital and Cognitive Musicology Lab at EPFL for their valuable feedback. This research was supported by the Swiss National Science Foundation within the project “Distant Listening: Transitions of Tonality” (Grant no. 215701). In part, this project has received funding from the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme under grant agreement No 760081 – PMSB. The authors thank Mr. Claude Latour for generously supporting this research through the Latour chair in digital musicology. 

### 8. REFERENCES 

- [1] E. J. Crawley, B. E. Acker-Mills, R. E. Pastore, and S. Weil, “Change detection in multi-voice music: the role of musical structure, musical training, and task demands.” Journal of Experimental Psychology: Human Perception and Performance, vol. 28, no. 2, p. 367, 2002. 

- [2] S. Koelsch, M. Rohrmeier, R. Torrecuso, and S. Jentschke, “Processing of hierarchical syntactic structure in music,” Proceedings of the National Academy of Sciences, vol. 110, no. 38, pp. 15 443– 15 448, 2013. 

- [3] M. Rohrmeier and S. Koelsch, “Predictive information processing in music cognition. a critical review,” International Journal of Psychophysiology, vol. 83, no. 2, pp. 164–175, 2012. 

- [4] C. Finkensiep and M. A. Rohrmeier, “Modeling and inferring proto-voice structure in free polyphony,” in Proceedings of the 22nd International Society for Music Information Retrieval Conference. ISMIR, 2021, pp. 189–196. 

- [5] M. T. Pearce, “Statistical learning and probabilistic prediction in music cognition: mechanisms of stylistic enculturation,” Annals of the New York Academy of Sciences, vol. 1423, no. 1, pp. 378–395, 2018. 

- [6] K. C. Barrett, R. Ashley, D. L. Strait, E. Skoe, C. J. Limb, and N. Kraus, “Multi-voiced music bypasses attentional limitations in the brain,” Frontiers in neuroscience, vol. 15, p. 588914, 2021. 

- [7] E. H. Margulis, On repeat: How music plays the mind. Oxford University Press, 2013. 

- [8] V. N. Salimpoor, D. H. Zald, R. J. Zatorre, A. Dagher, and A. R. McIntosh, “Predictions and the brain: how musical sounds become rewarding,” Trends in cognitive sciences, vol. 19, no. 2, pp. 86–91, 2015. 

- [9] J. Schmidhuber, “Driven by compression progress: A simple principle explains essential aspects of subjective beauty, novelty, surprise, interestingness, attention, curiosity, creativity, art, science, music, 

jokes,” 2009. [Online]. Available: https://arxiv.org/ abs/0812.4360 

- [10] J. Ho, A. Jain, and P. Abbeel, “Denoising diffusion probabilistic models,” 2020. [Online]. Available: https://arxiv.org/abs/2006.11239 

- [11] K. Friston, “The free-energy principle: a unified brain theory?” Nature reviews neuroscience, vol. 11, no. 2, pp. 127–138, 2010. 

- [12] H. B. Barlow et al., “Possible principles underlying the transformation of sensory messages,” Sensory communication, vol. 1, no. 01, pp. 217–233, 1961. 

- [13] J. Rissanen, “Modeling by shortest data description,” Automatica, vol. 14, no. 5, pp. 465–471, 1978. 

- [14] J. Gottlieb, P.-Y. Oudeyer, M. Lopes, and A. Baranes, “Information-seeking, curiosity, and attention: computational and neural mechanisms,” Trends in cognitive sciences, vol. 17, no. 11, pp. 585–593, 2013. 

- [15] A. Modirshanechi, K. Kondrakiewicz, W. Gerstner, and S. Haesler, “Curiosity-driven exploration: foundations in neuroscience and computational modeling,” Trends in Neurosciences, vol. 46, no. 12, pp. 1054– 1066, 2023. 

- [16] J. Schmidhuber, “Formal theory of creativity, fun, and intrinsic motivation (1990–2010),” IEEE transactions on autonomous mental development, vol. 2, no. 3, pp. 230–247, 2010. 

- [17] F. Lerdahl and R. S. Jackendoff, A Generative Theory of Tonal Music, reissue, with a new preface. MIT press, 1996. 

- [18] M. Rohrmeier, “Towards a generative syntax of tonal harmony,” Journal of Mathematics and Music, vol. 5, no. 1, pp. 35–53, 2011. 

- [19] C.-Z. A. Huang, A. Vaswani, J. Uszkoreit, N. Shazeer, I. Simon, C. Hawthorne, A. M. Dai, M. D. Hoffman, M. Dinculescu, and D. Eck, “Music transformer,” 2018. [Online]. Available: https://arxiv.org/abs/1809. 04281 

- [20] A. Huang, M. Dinculescu, A. Vaswani, and D. Eck, “Visualizing music self-attention,” in Proc. NeurIPS Workshop on Interpretability and Robustness in Audio, Speech, and Language, vol. 1, 2018, p. 4. 

- [21] J. Sohl-Dickstein, E. A. Weiss, N. Maheswaranathan, and S. Ganguli, “Deep unsupervised learning using nonequilibrium thermodynamics,” 2015. [Online]. Available: https://arxiv.org/abs/1503.03585 

- [22] J. Austin, D. D. Johnson, J. Ho, D. Tarlow, and R. van den Berg, “Structured denoising diffusion models in discrete state-spaces,” 2023. [Online]. Available: https://arxiv.org/abs/2107.03006 

571 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [23] M. Plasser, S. Peter, and G. Widmer, “Discrete diffusion probabilistic models for symbolic music generation,” 2023. [Online]. Available: https://arxiv. org/abs/2305.09489 

- [24] Z. Wang, L. Min, and G. Xia, “Whole-song hierarchical generation of symbolic music using cascaded diffusion models,” 2024. [Online]. Available: https://arxiv.org/abs/2405.09901 

- [25] E. Hoogeboom, A. A. Gritsenko, J. Bastings, B. Poole, R. van den Berg, and T. Salimans, “Autoregressive diffusion models,” 2022. [Online]. Available: https://arxiv.org/abs/2110.02037 

   - [37] S. Ni-Hahn, W. Xu, J. Yin, R. Zhu, S. Mak, Y. Jiang, and C. Rudin, “A new dataset, notation software, and representation for computational schenkerian analysis,” arXiv preprint arXiv:2408.07184, 2024. 

   - [38] R. J. Williams, “Simple statistical gradient-following algorithms for connectionist reinforcement learning,” Machine learning, vol. 8, pp. 229–256, 1992. 

   - [39] M. Zeng, X. Tan, R. Wang, Z. Ju, T. Qin, and T.-Y. Liu, “Musicbert: Symbolic music understanding with largescale pre-training,” arXiv preprint arXiv:2106.05630, 2021. 

- [26] L. Kong, J. Cui, H. Sun, Y. Zhuang, B. A. Prakash, and C. Zhang, “Autoregressive diffusion model for graph generation,” 2023. [Online]. Available: https://arxiv.org/abs/2307.08849 

- [27] D. P. Kingma, M. Welling et al., “Auto-encoding variational bayes,” 2013. 

- [28] V. Mnih, A. P. Badia, M. Mirza, A. Graves, T. P. Lillicrap, T. Harley, D. Silver, and K. Kavukcuoglu, “Asynchronous methods for deep reinforcement learning,” 2016. [Online]. Available: https://arxiv.org/abs/1602.01783 

- [29] D. Jeong, T. Kwon, Y. Kim, and J. Nam, “Graph neural network for music score data and modeling expressive piano performance,” in International conference on machine learning. PMLR, 2019, pp. 3060–3070. 

- [30] E. Karystinaios and G. Widmer, “Graphmuse: A library for symbolic music graph processing,” arXiv preprint arXiv:2407.12671, 2024. 

- [31] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polosukhin, “Attention is all you need,” Advances in neural information processing systems, vol. 30, 2017. 

- [32] M. Schlichtkrull, T. N. Kipf, P. Bloem, R. van den Berg, I. Titov, and M. Welling, “Modeling relational data with graph convolutional networks,” 2017. [Online]. Available: https://arxiv.org/abs/1703.06103 

- [33] P. Veliˇckovi´c, G. Cucurull, A. Casanova, A. Romero, P. Liò, and Y. Bengio, “Graph attention networks,” 2018. [Online]. Available: https://arxiv.org/abs/1710. 10903 

- [34] J. Hentschel, Y. Rammos, M. Neuwirth, and M. Rohrmeier, “The distant listening corpus,” 2024. [Online]. Available: https://doi.org/10.5281/zenodo. 13845439 

- [35] P. B. Kirlin, A probabilistic model of hierarchical music analysis. University of Massachusetts Amherst, 2014. 

- [36] H. Schenker, Neue musikalische Theorien und Phantasien. Universal-edition ag, 1910, vol. 2. 

572 

