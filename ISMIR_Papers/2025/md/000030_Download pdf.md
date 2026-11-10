---
paper_id: "000030"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706387/files/000030.pdf"
---

# GD-RETRIEVER: CONTROLLABLE GENERATIVE TEXT-MUSIC RETRIEVAL WITH DIFFUSION MODELS 

Julien Guinot<sup>∗,1,2</sup> 

Elio Quinton<sup>2</sup> György Fazekas<sup>1</sup> 

1 Centre for Digital Music, Queen Mary University of London, U.K. 

2 Music & Audio Machine Learning Lab, Universal Music Group, London, U.K. 

```
j.guinot@qmul.ac.uk
```

## ABSTRACT 

Multimodal contrastive models have achieved strong performance in text-audio retrieval and zero-shot settings, but improving joint embedding spaces remains an active research area. Less attention has been given to making these systems controllable and interactive for users. In text-music retrieval, the ambiguity of freeform language creates a many-to-many mapping, often resulting in inflexible or unsatisfying results. 

We introduce Generative Diffusion Retriever (GDR), a novel framework that leverages diffusion models to generate queries in a retrieval-optimized latent space. This enables controllability through generative tools such as negative prompting and denoising diffusion implicit models (DDIM) inversion, opening a new direction in retrieval control. GDR improves retrieval performance over contrastive teacher models and supports retrieval in audio-only latent spaces using non-jointly trained encoders. Finally, we demonstrate that GDR enables effective post-hoc manipulation of retrieval behavior, enhancing interactive control for text-music retrieval tasks. 



<!-- Start of picture text -->
Text Query εT 日<br>Audio Database<br>Text / Audio Encoders<br>Contrastive Retrieval<br>Similarity Search Retrieval<br>Generated Queries Similarity Search Retrieval<br>Text Query<br>Audio Database<br>Generative Retrieval<br>EA<br><!-- End of picture text -->

Figure 1: Overview of GD-Retriever’s proposal: Instead of encoding text queries and audio keys in a joint embedding space (top), we generate queries in the audio space directly through conditioning on a text query (bottom) 

## 1. INTRODUCTION 

Multimodal text-music joint embedding models have largely facilitated text-queried music retrieval applications [1–5]. Multimodal contrastive learning of text and music joint embedding spaces specifically have shown high performance on frozen probing tasks and promise for zeroshot classification approaches, with strong representation learning capacities. Despite the improvement in effectively encoding musical information, these approaches often lack controllability. Unsatisfactory results from text querying require re-prompting with a different query to refine retrieval, and it is difficult to navigate the latent space of joint-embedding models with interpretable controls, such as “I would like this retrieval result to be punchier” or “I would like the retrieval result to be similar to this track, but with an electric guitar instead of acoustic”. 

> cc © Julien Guinot, Elio Quinton, György Fazekas. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: Julien Guinot, Elio Quinton, György Fazekas, “GDRetriever: Controllable Generative Text-Music Retrieval with Diffusion Models”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

One field in which such controls are more extensively explored, efficient, and disentangled is the field of generative AI. Diffusion generative models, specifically, have not only been widely adopted by virtue of their high quality outputs and multimodal conditionability [6–12], but have also been the focus of an extensive range of controllability approaches which have incrementally added powerful, multimodal, and intuitive controls to generative diffusion models [10, 12–20]. In light of this observation, we are strongly motivated to combine the retrieval and diffusion paradigms. This work focuses on exploring the capabilities of generative text-music models for retrieval, with the motivation of enabling controllability mechanisms for interactive retrieval. For instance, this would enable discovering directions of modification of musical attributes in the latent space or being able to modify the genre or instrumentation of a retrieved musical piece without modifying other semantic attributes. 

We propose Generative Diffusion Retriever, a new mechanism for retrieval, in which we train a conditional latent diffusion model on a retrieval-optimized latent space. We prompt GD-Retriever to generate hypothetical queries in the audio latent space and retrieve nearest neighbours 

262 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

(See Figure 1). Our contributions are<sup>1</sup> : 

- 1 We present a generative diffusion retrieval framework that conditionally generates hypothetical queries in the latent space, leading to improved performance on in-domain text-music retrieval. 

- 2 We distinguish ourselves from previous approaches by directly generating embedding sequences over aggregated embeddings, promoting finer-grained text-music understanding. 

- 3 We show that we successfully unlock the array of controllability methods for generative models for retrieval through examples such as negative prompting and DDIM inversion [17]. 

- 4 Our approach is directly applicable to audio-only latent spaces, and can leverage text encoders that have not been jointly trained with an audio encoder. 

## 2. BACKGROUND 

## 2.1 Text-music contrastive learning and retrieval 

Multimodal contrastive learning has shown strong results in computer vision [6, 21–23], and has been successfully extended to audio and music domains [1,2,5]. These models encode paired text and audio inputs using encoders ET and EA, project them into a shared latent space, and apply a contrastive InfoNCE loss [24] on pooled embeddings (ZT , ZA) to align positive pairs while separating negative ones. 

Early text-audio/music models such as CLAP [3, 5], MusCALL [1], and MuLan [2] adopt CLIP-style training [21]. Later work improves alignment through better captions and token-/time fine grained mechanisms [4, 25–27]. Learned representations from these models are widely used for retrieval, in which the learned similarity metric between text and music encodings can be used to retrieve the most similar music key in a database of audio samples [1–3], generative conditioning [7, 8, 14, 15, 28], and retrieval-augmented captioning [29, 30]. 

## 2.2 Diffusion Models 

Diffusion models are powerful generative models that iteratively refine noisy inputs to generate high-quality outputs by learning a reverse Markov process [6, 31, 32]. These models corrupt data with noise over multiple steps and then learn to reconstruct the sample from the step information. 

The denoising process is modeled as a learned transition, where at each step, a generator G predicts either the original data x0 (sample objective) or the noise added to the original latent (ϵ objective). We adopt the sample prediction objective, where the model predicts the clean latent at each step, as in prior work [33, 34]. The diffusion process can be conditioned on auxiliary conditioning information such as text or other modalities [35, 36], typically applied with classifier-free guidance (CFG) [6] by interpolating between unconditional and conditional predictions at each denoising step. Latent diffusion models reduce com- 

> 1 Code is made available at https://github.com/Pliploop/GDRetriever 

putational costs by operating in a compressed latent space using pretrained autoencoders [7, 8, 14, 15, 37, 38]. 

## 2.3 Controllability for generation and retrieval 

Controllability in generation refers to how well generative models respond to human-guided interactions, allowing for attribute modification or refinement either during or after generation. In diffusion models, this includes techniques like text-based attribute editing [39–41], inpainting [42], inversion, and negative prompting [17, 43]. In music generation, controllability is an active area of research due to its potential for creative applications [12, 44–46]. 

While extensively studied in generation, controllability in retrieval—especially for music—remains underexplored. This involves enabling users to guide or modify retrieval results interactively, by specifying attributes of interest for retrieval in a disentangled way [47, 48] or applying latent transformations, e.g. tempo adjustments [49]. Generative retrieval has emerged in recent work to generate latent queries, mainly to improve performance in general audio retrieval [34] or add multimodal guidance [50], rather than enabling interactivity during or after retrieval. 

## 3. GENERATIVE DIFFUSION RETRIEVAL 

We propose an intuitive generative approach to retrieval using diffusion models, which we name Generative Diffusion Retriever. Using a pretrained latent space optimized for audio-audio retrieval, we train a generative diffusion model conditioned on text to generate audio latent embeddings in this space. At inference time, rather than encoding the text query into the shared latent space and retrieving the nearest audio [1, 3], we generate a “ghost” audio query in the latent space conditioned on the text query (Similar to [12, 50]) and retrieve the nearest neighbours in the audio space. By using a generative model as a retriever, we enable adaptation of audio-only latent spaces for textaudio retrieval without requiring multimodal pretraining. The generative modelling of retrieval allows for greater retrieval controllability through attribute modification and interactive refinement techniques from the generative domain. The approach is shown in Figure 2. 

Consider an audio, query caption pair {x<sup>q</sup> t<sup>, xa}anda</sup> conditioning text encoder ET which encodes the text query into a sequence of embeddings zT<sup>q.Let EAbe a pretrained</sup> and frozen audio encoder encoding xa into a sequence of audio embeddings zA. We train G with a diffusion loss to reconstruct zA conditioned on zT<sup>q, which we notatez˜</sup> A<sup>q:</sup> 



<!-- Start of picture text -->
LG = Eτ,Za,zT q �∥za −G(za,τ , τ, zT q )∥2 2� (1)<br><!-- End of picture text -->

Where τ is the diffusion step. We aggregate ˜zA<sup>qintoZ˜</sup> A<sup>q</sup> through averaging over the sequence timesteps and use Z<sup>˜</sup> A<sup>q</sup> as a query in the audio space to retrieve audio. 

## 3.1 Model architecture 

## 3.1.1 Diffusion backbone 

We use a well-established UNet with cross-attention conditioning [6–9] as our diffusion model. Early experi- 

263 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
conditioning conaiuing<br>Text Latents τ Text Latents<br>with supersaw synths""An EDM track ET ET with supersaw synths""An EDM track<br>Text query<br>za ∈ RT×dAudio Latents €(τ) ∼ N(0,1)<br>A 1<br>Diffusion UNet Diffusion UNet Average<br>pooling Similarity search retrieval<br>Denoising step In joint text-audio embedding space<br>(a) Stage 1 — Generative pretraining. (b) Stage 2 — Retrieval<br><!-- End of picture text -->

Figure 2: GD Retriever Method: We train a model to generate text-conditioned ghost queries for retrieval. Left: A diffusion model is trained to generate audio latents from text captions. Right: Using the frozen model, we generate audio embeddings from a caption to retrieve similar audio via ghost queries. 

mentation led to the design choice of a ∼40M parameter model. Models are conditioned on text embedding sequences through cross-attention. Compared to previous work [34, 50] that performs generative diffusion retrieval with aggregated embeddings, this enables more fine-grained interaction between audio and text [50], as we show in Section 4.2. Supported by results in [33], we find that a sample-objective (See Section 2) yields better retrieval results than ϵ-objective. 

## 3.1.2 Text and audio encoders 

We use three audio encoders: CLAP [3], MusCALL [1], and MULE [51]. CLAP uses an HTSAT backbone [52] with the publicly available Music checkpoint<sup>2</sup> . MusCALL is based on a ResNet50 encoder, and MULE is reimplemented and pretrained on MTG-Jamendo following [48]. For text encoders, we use CLAP’s RoBERTa-based encoder [53, 54], MusCALL’s 4-layer transformer, or a pretrained Flan-T5 model [53] from HuggingFace<sup>3</sup> . Flan-T5 is a fine-tuned T5 language model commonly used in music generation [8, 11, 55, 56]. 

## 3.2 Datasets 

We use two well-explored public music-caption pairs datasets as well as a private dataset for training and evaluation. Song Describer [57] (SD) is a dataset of 1100 crowd-sourced captions corresponding to 700 excerpts of 2 minute music clips. MusicCaps [58] is another musiccaption pair dataset consisting of 5500 pairs with 10s audio. Finally, we use a private large scale dataset of professionally-annotated song descriptions (PrivateCaps). Table 1 inventories dataset scales. For evaluation on PrivateCaps, we use a 5500-sample subset of the test set. 

## 3.3 Training details 

We extract latent embeddings from our training datasets (See Section 3.2) with the selected audio encoders. We extract za by sliding the encoder over the audio input at a frequency of 1Hz. GDR is trained on PrivateCaps with 

> 2 https://github.com/LAION-AI/CLAP 

> 3 https://huggingface.co/google/flan-t5-base 

|Dataset|#tracks|#captions|Hours|Training|Eval|
|---|---|---|---|---|---|
|SongDescriber [57]|0.7k|1.1k|23.3|✗|✓|
|MusicCaps [56]|5.5k|5.5k|15.3|✗|✓|
|PrivateCaps|251k|251k|12.5k|✓|✓|



Table 1: Dataset details - PrivateCaps is an internal dataset of full-length professionally annotated production tracks 

a batch size of 256 for 100k steps, with an early stopping mechanism on validation diffusion loss. Models are trained on a single A5000 GPU. We use AdamW and linear warmup the learning rate to 1e−4 over 5000 steps then cosine decay to 0. Our model is trained on latent sequences of length T = 64, i.e. 1 minute of audio. We use CFG on text conditioning [35] (masking probability 10%). 

## 4. EXPERIMENTS 

## 4.1 Retrieval 

|T→A||Ev|al datase|t|
|---|---|---|---|---|
|Model|Metric|PC|SD|MC|
||R@1↑|2.2|3.1|3.8|
|CLAP|R@5↑|7.2|13.7|12.9|
||R@10↑|12.3|23.2|19.5|
||MedR(%) ↓|3.7|4.0|1.4|
||R@1↑|6.9|4.7|2.7|
|GDRCLAP|R@5↑|17.1|15.3|7.6|
|-|R@10↑|22.9|24.7|11.5|
||MedR(%) ↓|1.6|3.8|2.9|
||R@1↑|10.1|3.6|1.0|
|MCALL|R@5↑|26.2|13.6|3.9|
|us|R@10↑|35.1|22.0|7.0|
||MedR(%) ↓|0.4|4.2|5.1|
||R@1↑|10.8|5.1|1.8|
|A|R@5↑|25.1|16.9|6.4|
|GDR-MusCLL|R@10↑|33.3|25.5|9.9|
||MedR (%)↓|0.6|3.5|3.4|



Table 2: Main retrieval results for GDR. We compare GDR-CLAP to CLAP and GDR-MusCALL to muscall for R@1,5,10 on the PC, SD and MC Datasets. 

We evaluate GD-Retriever’s retrieval performance against teacher models. We generate nq = 5 audio latent queries z˜A conditioned on zT<sup>qWeaveragez˜Aovertime</sup> and nq into Z<sup>˜</sup> A for retrieval. Teachers encode text and au- 

264 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

dio into embeddings ZT and ZA. . Results are shown in Table 2. While GD-Retriever outperforms teacher models in several in-domain scenarios—most notably on PrivateCaps (PC) and to a lesser extent SongDescriber (SD)—its retrieval performance degrades on out-of-domain MusicCaps (MC). In particular, GDR-CLAP underperforms on MC relative to the CLAP teacher, despite showing strong improvements on PC. Conversely, GDR-MusCALL underperforms on PC while providing stronger performance than the teacher baseline on MC and SD. Despite strong indomain results, these inconsistencies suggest that domain mismatch plays a role in limiting retrieval performance. 

## 4.1.1 Domain adaptation 

We identify two compounding sources of domain shift. First, pretrained contrastive models like CLAP and MusCALL often fail to generalize across datasets with differing audio and text distributions—a well-known issue in dense retrieval and multimodal learning [59, 60]. CLAP, trained on LAION-630k [3], performs worse than MusCALL on its in-domain evaluation set (PC), but shows similar performance on SD, and better performance on MC. 

Second, GD-Retriever learns a text-to-audio mapping on the teacher’s frozen embedding space during diffusion training. If the teacher suffers from domain mismatch (e.g., CLAP on PC), GDR can compensate by adapting to the training distribution. Conversely, when the teacher is wellaligned (e.g., MusCALL on PC), GDR tends to match, but not exceed, its performance. This explains why GDRCLAP, trained on PrivateCaps with a CLAP teacher, reproduces performance trends seen in MusCALL’s teacher embeddings—performing best on PC, acceptably on SD, and poorly on MC. 

|Dataset|Encoder Pair|FTD↓|FAD|R@5|FA|D↓|R@|5↑|
|---|---|---|---|---|---|---|---|---|
|||ZT|ZA|ZA|˜ZA|˜Z<sup>align</sup><br>A|˜ZA|˜Z<sup>align</sup><br>A|
|PC|CLAP|-|-|7.2|0.03|0.003|17.1|18.2|
|SD|CLAP|-|-|13.7|0.09|0.001|15.3|15.9|
|MC|CLAP|-|-|12.9|0.34|0.001|7.6|8.1|
|PC|MusCALL|0.008|0.002|26.2|0.02|∼0|25.1|25.3|
|SD|MusCALL|0.14|0.18|13.6|0.12|∼0|16.9|17.7|
|MC|MusCALL|0.32|0.20|3.9|0.17|∼0|6.4|7.2|



Table 3: Fréchet distances of ZA/ZT to the training distribution of teacher models, Fréchet audio distance (FAD) to the evaluation set, and retrieval performance (R@5) for generated queries (Z<sup>˜</sup> A), and aligned queries (Z<sup>˜</sup> A<sup>align</sup> ) across datasets and encoder pairs. We are unable to evaluate FAD on ZA for CLAP’s training set as LAION-630k is private. 

To test this hypothesis, we compute Frechet Distances between training and evaluation distributions, comparing (1) teacher audio embeddings of each evaluation set to the training distribution and (2) GDR-generated queries to the evaluation set, before and after a lightweight alignment step. Following prior domain adaptation work [61, 62], we apply a post-hoc shift in mean and covariance to Z<sup>˜</sup> A to match the evaluation set (notated ZA<sup>align</sup> ). This method is model-agnostic, efficient, and requires no retraining. 

We evaluate on joint encoder pairs to illustrate the joint text-audio domain generalization gap. As shown in Ta- 

ble 3, GDR-generated latents exhibit similar distribution shifts as the teacher. Alignment consistently reduces FAD and improves R@5, supporting our claim that retrieval degradation stems from inherited distribution divergence rather than a limitation of our approach. While not a complete solution, this provides both evidence for our diagnosis and a simple, effective mitigation. We leave broader generalization strategies for future work. 

## 4.1.2 Encoder pair variation 

Two core affordances of GDR are its ability to (1) operate in audio-only latent spaces not trained jointly with text, and (2) support arbitrary text encoders for conditioning. This is enabled by the diffusion model learning a generative mapping between text and audio embeddings, independent of any contrastive pre-training alignment. The generative retrieval objective imposes no constraints on the multimodality of the space or the choice of text encoder. To demonstrate this, we test several combinations of audio and text encoders that were not jointly trained: we replace the text encoder in GDR-CLAP with Flan-T5 (Section 3.1.2), and use the audio encoder to MULE paired with T5. Retrieval results are reported in Table 4. 

|T|−→A||Ev|al datas|et|
|---|---|---|---|---|---|
|Model|ET|Metric|PC|SD|MC|
|||R@1↑|8.1|4.9|2.3|
||T5|R@5↑|21.1|15.6|7.8|
|||R@10↑|29.2|25.1|11.7|
|GDR-CLAP||MR ↓|0.8|3.7|2.9|
|||R@1↑|6.9|4.7|2.7|
||CLAP|R@5↑|17.1|15.3|7.6|
|||R@10↑|22.9|24.7|11.5|
|||MR ↓|1.6|3.8|2.9|
|||R@1↑|7.6|4.1|1.6|
|GDRMULE|T5|R@5↑|18.5|13.9|6.2|
|-||R@10↑|25.3|21.8|11.0|
|||MR ↓|1.6|4.2|3.2|



Table 4: Comparison of retrieval performance across models and text encoders. GD-Retriever enables textconditioned retrieval on non-jointly trained encoders. 

Including T5 as the text encoder improves in-domain performance for GDR-CLAP, likely by regularizing the mapping between contrastively trained audio and text encoders. However, this benefit is more limited out-ofdomain, consistent with our findings in Section 4.1.1, where domain mismatch stems from training set distributions. We also find that GDR-MULE supports text-music retrieval and outperforms the CLAP teacher on PrivateCaps and SongDescriber. This demonstrates that joint retrieval spaces can be built from unimodal audio latents without large-scale multimodal pre-training—a key affordance of our approach. 

## 4.2 Quality of Generated Queries 

Beyond retrieval, we evaluate generated query quality using fidelity, diversity, and prompt adherence metrics. FAD captures audio fidelity, while CLAP score assesses alignment with input text. To evaluate diversity, we generate clusters of 10 audio queries per prompt and measure the intrasample cosine similarity (MICS) following previous 

265 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

work [50] and the normalized Vendi score (NVendi), along with its intracluster variant (MINVS), to assess the variation in generated queries [63]. 

We compare our diffusion-based UNet to two baselines: a regression UNet predicting sequences of audio embeddings from sequences of learned mask embeddings conditioned on zT<sup>q,andtwo1-hidden-layerMLP(GeLU,4096</sup> units), trained with respectively diffusion and regression objectives to reconstruct ZA conditioned on ZT<sup>q.All mod-</sup> els use the same training hyperparameters and CLAP T/A encoders. Table 5 shows results on PrivateCaps. Our diffusion UNet outperforms alternatives in retrieval and fidelity. While MLP Diffusion achieves higher diversity, it comes at the cost of realism and retrieval performance. 

||Metric|Diffu<br>UNet|sion<br>MLP|Regr<br>UNet|ession<br>MLP|
|---|---|---|---|---|---|
|Ril SD|R@5↑|15.3|11.3|9.1|7.1|
|etreva ()|NMedR ↓|3.8|5.5|5.6|5.1|
|Fidlit|FAD↓|0.09|0.13|0.13|0.13|
|ey|CLAP ↑|0.63|0.53|0.54|0.53|
||MICS↓|0.92|0.62|1|1|
|Diversity|MINVS↑|1.42|4.53|1|1|
||NVendi ↑|12.9|68.9|3|3.4|



Table 5: Fidelity, Retrieval, and Diversity metrics for CLAP-Retrievers trained on PrivateCaps. FAD is grounded on MTG-Jamendo [64]. 

## 4.3 Controllability 

## 4.3.1 Negative prompting 

Negative prompting is an off-the-shelf affordance of diffusion models related to CFG [35], which allows users to specify what they do not want to be in the generated output. Negative prompting modifies the CFG update by incorporating a negative conditioning signal zT<sup>q−.Givenaquery</sup> embedding zT<sup>q+, a denoising step is given by:</sup> 



<!-- Start of picture text -->
z˜A,τ NP +1 = (1 + w)G(˜zA,τ , τ + 1, z T q+)<br>(2)<br>−wG(˜zA,τ , τ + 1, zT q−)<br><!-- End of picture text -->

where w is the classifier free guidance strength [35]. This formulation removes undesired attributes by interpolating towards conditional generation and away from negatively conditioned outputs at each diffusion step (See Section 3). 

We evaluate the effectiveness of negative prompting in retrieval by curating 50 negative prompts across genre, mood, instrumentation, key, and tempo (e.g. “a rock song” as a negative prompt “removes” rock). Each category includes different phrasing formats. For each query q, we create new, modified query latents za<sup>mod</sup> using negative prompting and three additional modification methods as baselines, all applied with guidance strength w: 

Negative prompting (NP) modifies latents by applying Eq. 2 with zT<sup>−asnegativeconditioning.</sup> Text Interpolation (∆T ) interpolates from ZA away from Z<sup>T q−</sup> : ZA<sup>′=ZA+w∆T ,where∆T=Z</sup> T<sup>q+</sup> − ZT<sup>q−.Audio</sup> interpolation interpolates along the direction from Z<sup>˜</sup> A and away from Z<sup>˜</sup> A<sup>−:∆A=Z˜A−Z˜</sup> A<sup>−.Ourlastbaselineis</sup> 



<!-- Start of picture text -->
Z SΛ o Z ŽT,mod vs Ž{<br>1.0 NP Δr 0.4<br>PNP<br>0.8 0.2<br>CLAP 0.6 0.0<br>CLAP ( ↓)<br>-0.2<br>0.4<br>-0.4<br>0.2<br>GenreMood<br>InstrumentTempo genre instrumenttempo<br>High level high_level<br>Figure 3: CLAP score results between Za mod and Z ˜ A q+,<br>Za mod and Z ˜ a q− for negative prompting and baselines for<br>different categories.<br><!-- End of picture text -->

Prefix Negation Prompting (PNP): We modify the query by negating attributes (e.g., “a rock track” → “not a rock track”), then generate z˜A<sup>P NP</sup> with GDR. Za<sup>mod</sup> obtained from all modification methods is compared using CLAP score to ZA<sup>q+,Z˜</sup> A<sup>q+, and Z</sup> A<sup>q−, for which</sup> a higher CLAP score is better as it signifies higher similarity to the positive prompt. We also compare Za<sup>mod</sup> to Z<sup>˜</sup> A<sup>q−,</sup> and ZA<sup>q−, for which a lower CLAP score (less similar to the</sup> negative conditioning) is better. We also use FAD to assess the fidelity of ZA<sup>mod</sup> . A modified audio latent that is similar to the original ZA<sup>q+</sup> and dissimilar to ZA<sup>q−</sup> but is very far from any reasonable distribution (i.e. large FAD) will yield unrealistic or uncommon music results. CLAP score and FAD grounded on MTG-Jamendo are reported Table 6. Fine-grained category experiments are shown Table 3. 

|key||Z<sup>q+</sup><br>A|Mi|odifiedq|uery <sup>˜</sup>Z<sup>m</sup><br>A<br>˜|<sup>od</sup><br>|
|---|---|---|---|---|---|---|
||||NP|∆T|∆A|PNP|
||ZA|0.69|0.66|0.38|0.39|0.51|
|CLAP↑|˜ZA|1|0.85|0.65|0.62|0.49|
||ZT<br>|0.42|0.39|0.28|0.33|0.21|
|CLAP↓|˜Z<sup>n</sup><br>A|0.41|0.21|-0.02|-0.23|0.46|
||Z<sup>n</sup><br>T|0.17|0.08|-0.51|-0.04|0.21|
|Fidelity|FAD|0.11|0.12|3.12|0.60|0.12|



Table 6: Negative prompting experiments - CLAP score of modified queries zA<sup>mod</sup> vs original/negative ZA/ZT 

Negative prompting shows strong desirable results: The modified audio latent remains the most similar to the original prompt across modification baselines, while significantly distancing itself from the negative prompt. At the same time, NP-modified latents remain realistic and in distribution, as demonstrated by the lower FAD score. While ∆T and ∆A can lower the CLAP score relative to undesired attributes, they also degrade semantic alignment with the original prompt, as reflected in lower CLAP scores. In addition, this reduction is achieved unrealistically: higher FAD scores indicate the resulting latents deviate significantly from the grounding distribution. In retrieval, this would lead to unnatural or implausible results which are less relevant, even if less similar to the negative attribute. Moreover, a lower CLAP score to a negative prompt is not always desirable: Usually, a CLAP score of 0 denotes the absence of shared information between the two em- 

266 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

beddings, while a negative CLAP score signifies opposite information. Colloquially, a CLAP score of -1 for a reference embedding of ”guitar“ does not mean ”No guitar“, but rather ”the opposite of guitar”, which is ill-defined. 

## 4.3.2 DDIM Inversion 

One useful property of diffusion models is DDIM inversion, which enables user-controlled modifications while preserving semantic similarity [17]. By re-noising an embedding via an inverse DDIM scheduler, the latent returns to a noisier state where high-level features are established. From this pivot, applying new guidance during denoising yields outputs that better match the new prompt while remaining close to the original. 

This is valuable for retrieval, where users may want to refine a specific attribute of a query they are partly satisfied with. Current joint embedding retrieval models lack native support for such interaction. In contrast, GD-Retriever supports DDIM inversion directly, allowing for interactive and controllable retrieval refinement. 



<!-- Start of picture text -->
Audio to audio CLAP Audio to text CLAP<br>1.0 cosim( A, mod, r, +)) 0.40 cosim(ŻA, mod, τ, (*)<br>0.8 ·žA(↓) ŽA mod( ↑ )ZA(↓) 0.300.35 z{(t)Zτ(↓)Zr,moo( ↑)<br>CLAP0.6 CLAP0.200.25 Zτ(↓)<br>0.4 0.15<br>Adding noiseRemoving noise 0.10<br>0.2<br>0.05<br>0.0 0.00<br>10 20 10 0 10 20 10<br>Steps from start of inversion (τ) Steps from start of inversion (τ)<br>Noise level Noise level<br><!-- End of picture text -->

Figure 4: DDIM inversion example. Left: CLAP scores to audio from original and modified prompts. Right: CLAP scores to text prompts and added/removed words. 

To demonstrate DDIM inversion for retrieval, we apply it to a prompt from the Song Describer dataset: “A choppy beat-heavy acoustic guitar song with soft vocals.” From the generated latent z˜A<sup>q,weperforminversionus-</sup> ing an inversion prompt x<sup>q,</sup> T<sup>inv</sup> : “A smooth, solo acoustic guitar song with harsh vocals.” The aim is to produce a latent ZA<sup>mod</sup> that remains close to the original while aligning more with the modified prompt. We track CLAP scores between ZA<sup>mod</sup> (τ ) with τ the inversion step and both original and modified audio/text queries: Z<sup>˜</sup> A<sup>q,Z˜</sup> A<sup>q,inv</sup> , ZT<sup>q, Z</sup> T<sup>qinv</sup> , and the text encodings of added (ZT<sup>+)andremoved(Z</sup> T<sup>−)</sup> words. Results are shown in Figure 4. We observe a clear transition: CLAP similarity shifts from the original to the modified prompt while remaining high to the original, confirming the effectiveness of DDIM inversion for fine-grained control in retrieval. 

To validate the usability of DDIM inversion as a retrieval controllability tool on a larger scale. We now curate 50 prompts from the Song Describer dataset that would represent realistic use-cases for refining a search result for retrieval, and curate modified prompts representing realistic modifications to refine a query, either by modifying 

qualificatives or subjects, or adding more details. Original prompts are notated zT<sup>qand modified prompts</sup> zT<sup>q′(again,modifiedaudiolatentsarenotatedz</sup> a<sup>mod</sup> ). For inversion, we re-noise ˜zA<sup>qfor 20 out of 50 steps and denoise</sup> conditioned on zT<sup>q′.We use re-generation as a baseline by</sup> simply generating z˜A<sup>q′.We compare Z</sup> a<sup>mod</sup> to ZA<sup>q,Z˜</sup> A<sup>qand</sup> Z˜A<sup>q′foraudiocomparison,andZ</sup> T<sup>q,Z</sup> T<sup>q′fortext.Adesir-</sup> able result is for ZA<sup>mod</sup> to be similar to these embeddings, meaning semantic similarity to the original and modified prompts. Results are shown in Figure 5. 



<!-- Start of picture text -->
1.0 0.5<br>0.8 0.4<br>nnv 0.6 0.3<br>CLP (Z 0.4 CLAP 0.2 method<br>0.2 0.1 invert<br>regenerate<br>0.0 0.0<br>ZA žq žq inv bz Zq inv<br>Modified latent versus... Modified latent versus...<br><!-- End of picture text -->

Figure 5: Systematic evaluation of DDIM inversion on curated prompt modifications, comparing CLAP score of inverted latents and regenerated latents to (left: audio, right: text) original and modified latents. 

DDIM inversion, a native affordance of GDR, yields higher similarity to the original prompt compared to regeneration, which causes a drop in CLAP score between ZA<sup>regen</sup> and Z<sup>˜</sup> A<sup>q′.Incontrast,Z</sup> A<sup>invremainsclosetoZ˜</sup> A<sup>q.While</sup> both methods maintain similar alignment with the modified prompt, only inversion preserves semantic similarity to the original, making it a more faithful controllability mechanism. Additionally, we observe that both classifierfree guidance and the number of inversion steps modulate the strength of the effect, offering further control. While we use vanilla DDIM here, recent improvements in inversion techniques [17,39] can be directly applied to GDR for more realistic and fine-grained control. 

## 5. CONCLUSION AND FUTURE WORK 

We present GD-Retriever, a generative framework for text-to-music retrieval that uses diffusion models to produce latent queries in retrieval-relevant spaces. GDRetriever outperforms contrastive teacher models on indomain data and enables retrieval in unimodal audio spaces by leveraging independently pretrained text and audio encoders—removing the need for joint multimodal training. 

Beyond retrieval performance, GD-Retriever enables inference-time controllability through negative prompting and DDIM inversion, offering flexible and post-hoc manipulation of retrieval behavior. These affordances open the door to interactive and user-steerable music retrieval. While domain mismatch remains a challenge, our findings suggest this can be partially mitigated through latent alignment. We encourage future work to expand generative control in retrieval, aiming for more robust, adaptable, and expressive retrieval systems. 

267 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 6. ACKNOWLEDGEMENT 

This work is supported by the EPSRC UKRI Centre for Doctoral Training in Artificial Intelligence and Music (EP/S022694/1) and Universal Music Group. 

## 7. REFERENCES 

- [1] I. Manco, E. Benetos, E. Quinton et al., “Contrastive audio-language learning for music,” in Proceedings of the 23rd International Society for Music Information Retrieval Conference, ISMIR 2022, Bengaluru, India, December 4-8, 2022, 2022, pp. 640–649. 

- [2] Q. Huang, A. Jansen, J. Lee et al., “Mulan: A joint embedding of music audio and natural language,” in Proceedings of the 23rd International Society for Music Information Retrieval Conference, ISMIR 2022, Bengaluru, India, December 4-8, 2022, 2022, pp. 559– 566. 

- [3] Y. Wu, K. Chen, T. Zhang et al., “Large-scale contrastive language-audio pretraining with feature fusion and keyword-to-caption augmentation,” in ICASSP 2023-2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2023, pp. 1–5. 

- [4] J. Wu, W. Li, Z. Novack et al., “Collap: Contrastive long-form language-audio pretraining with musical temporal structure augmentation,” in ICASSP 20252025 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2025, pp. 1–5. 

- [5] B. Elizalde, S. Deshmukh, M. Al Ismail et al., “Clap learning audio concepts from natural language supervision,” in ICASSP 2023-2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2023, pp. 1–5. 

- [6] J. Ho, A. Jain, and P. Abbeel, “Denoising diffusion probabilistic models,” Advances in neural information processing systems, vol. 33, pp. 6840–6851, 2020. 

- [7] H. Liu, Z. Chen, Y. Yuan et al., “AudioLDM: Textto-audio generation with latent diffusion models,” Proceedings of the International Conference on Machine Learning, 2023. 

- [8] H. Liu, Y. Yuan, X. Liu et al., “Audioldm 2: Learning holistic audio generation with self-supervised pretraining,” IEEE/ACM Transactions on Audio, Speech, and Language Processing, 2024. 

- [9] K. Chen, Y. Wu, H. Liu et al., “Musicldm: Enhancing novelty in text-to-music generation using beat-synchronous mixup strategies,” arXiv preprint arXiv:2308.01546, 2023. 

- [10] S.-L. Wu, C. Donahue, S. Watanabe et al., “Music controlnet: Multiple time-varying controls for music generation,” IEEE/ACM Transactions on Audio, Speech, and Language Processing, 2024. 

- [11] D. Ghosal, N. Majumder, A. Mehrish et al., “Text-toaudio generation using instruction guided latent diffusion model,” in Proceedings of the 31st ACM International Conference on Multimedia, 2023, p. 3590–3598. 

- [12] J. Nistal, M. Pasini, C. Aouameur et al., “Diff-a-riff: Musical accompaniment co-creation via latent diffusion models,” in ISMIR, 2024, 2024. 

- [13] Z. Novack, J. McAuley, T. Berg-Kirkpatrick et al., “Ditto: diffusion inference-time t-optimization for music generation,” in Proceedings of the 41st International Conference on Machine Learning, 2024, pp. 38 426–38 447. 

- [14] Z. Evans, J. D. Parker, C. Carr et al., “Long-form music generation with latent diffusion,” in Proceedings of the 25th International Society for Music Information Retrieval Conference (ISMIR), 2024. 

- [15] Z. Evans, C. Carr, J. Taylor et al., “Fast timingconditioned latent audio diffusion,” in Proceedings of the 41st International Conference on Machine Learning, 2024, pp. 12 652–12 665. 

- [16] R. Gal, Y. Alaluf, Y. Atzmon et al., “An image is worth one word: Personalizing text-to-image generation using textual inversion,” arXiv preprint arXiv:2208.01618, 2022. 

- [17] R. Mokady, A. Hertz, K. Aberman et al., “Null-text inversion for editing real images using guided diffusion models,” in Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, 2023, pp. 6038–6047. 

- [18] F. Yang, S. Yang, M. A. Butt et al., “Dynamic prompt learning: Addressing cross-attention leakage for textbased image editing,” Advances in Neural Information Processing Systems, vol. 36, pp. 26 291–26 303, 2023. 

- [19] S. A. Baumann, F. Krause, M. Neumayr et al., “Continuous, subject-specific attribute control in t2i models by identifying semantic directions,” arXiv preprint arXiv:2403.17064, 2024. 

- [20] X. Zhang, X.-Y. Wei, J. Wu et al., “Compositional inversion for stable diffusion models,” in Proceedings of the AAAI Conference on Artificial Intelligence, vol. 38, no. 7, 2024, pp. 7350–7358. 

- [21] A. Radford, J. W. Kim, C. Hallacy et al., “Learning transferable visual models from natural language supervision,” in International conference on machine learning. PMLR, 2021, pp. 8748–8763. 

- [22] X. Zhai, B. Mustafa, A. Kolesnikov et al., “Sigmoid loss for language image pre-training,” in Proceedings of the IEEE/CVF International Conference on Computer Vision, 2023, pp. 11 975–11 986. 

268 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [23] I. Bica, A. Ili´c, M. Bauer et al., “Improving finegrained understanding in image-text pre-training,” in Proceedings of the 41st International Conference on Machine Learning, 2024, pp. 3974–3995. 

- [24] T. Chen, S. Kornblith, M. Norouzi et al., “A simple framework for contrastive learning of visual representations,” in International conference on machine learning. PMLR, 2020, pp. 1597–1607. 

- [25] Y. Yuan, Z. Chen, X. Liu et al., “T-clap: Temporalenhanced contrastive language-audio pretraining,” in 2024 IEEE 34th International Workshop on Machine Learning for Signal Processing (MLSP). IEEE, 2024, pp. 1–6. 

- [26] I. Manco, J. Salamon, and O. Nieto, “Augment, drop & swap: Improving diversity in llm captions for efficient music-text representation learning,” in Proceedings of the 25th International Society for Music Information Retrieval Conference (ISMIR), 2024. 

- [27] G. Zhu, J. Darefsky, and Z. Duan, “Cacophony: An improved contrastive audio-text model,” IEEE/ACM Transactions on Audio, Speech, and Language Processing, 2024. 

- [28] M. Comunità, Z. Zhong, A. Takahashi et al., “SpecMaskGIT: Masked Generative Modeling of Audio Spectrograms for Efficient Audio Synthesis and Beyond,” in Proceedings of the 25th International Society for Music Information Retrieval Conference (ISMIR), 2024. 

- [29] X. Li, W. Chen, Z. Ma et al., “Drcap: Decoding clap latents with retrieval-augmented generation for zero-shot audio captioning,” in ICASSP 2025-2025 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2025, pp. 1–5. 

- [30] S. Ghosh, S. Kumar, C. K. R. Evuru et al., “Recap: Retrieval-augmented audio captioning,” in ICASSP 2024-2024 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2024, pp. 1161–1165. 

- [31] P. Esser, R. Rombach, and B. Ommer, “Taming transformers for high-resolution image synthesis,” in Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, 2021, pp. 12 873–12 883. 

- [32] J. Yu, Y. Xu, J. Y. Koh et al., “Scaling autoregressive models for content-rich text-to-image generation,” Transactions on Machine Learning Research, 2022. 

- [33] A. Ramesh, P. Dhariwal, A. Nichol et al., “Hierarchical text-conditional image generation with clip latents,” arXiv preprint arXiv:2204.06125, vol. 1, no. 2, p. 3, 2022. 

- [34] S. Mo, Z. Chen, F. Bao et al., “Diffgap: A lightweight diffusion module in contrastive space for bridging 

cross-model gap,” in ICASSP 2025-2025 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2025, pp. 1–5. 

- [35] J. Ho and T. Salimans, “Classifier-free diffusion guidance,” in NeurIPS 2021 Workshop on Deep Generative Models and Downstream Applications, 2022. 

- [36] W. Peebles and S. Xie, “Scalable diffusion models with transformers,” in Proceedings of the IEEE/CVF International Conference on Computer Vision, 2023, pp. 4195–4205. 

- [37] R. Rombach, A. Blattmann, D. Lorenz et al., “Highresolution image synthesis with latent diffusion models,” in Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, 2022, pp. 10 684–10 695. 

- [38] F. Schneider, Z. Jin, and B. Schölkopf, “Moûsai: Text-to-music generation with long-context latent diffusion,” arXiv e-prints, pp. arXiv–2301, 2023. 

- [39] W. Dong, S. Xue, X. Duan et al., “Prompt tuning inversion for text-driven image editing using diffusion models,” in Proceedings of the IEEE/CVF International Conference on Computer Vision, 2023, pp. 7430–7440. 

- [40] A. Hertz, R. Mokady, J. Tenenbaum et al., “Promptto-prompt image editing with cross-attention control,” in The Eleventh International Conference on Learning Representations, 2022. 

- [41] D. Sridhar and N. Vasconcelos, “Prompt sliders for fine-grained control, editing and erasing of concepts in diffusion models,” arXiv preprint arXiv:2409.16535, 2024. 

- [42] A. Lugmayr, M. Danelljan, A. Romero et al., “Repaint: Inpainting using denoising diffusion probabilistic models,” in Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, 2022, pp. 11 461–11 471. 

- [43] D. Miyake, A. Iohara, Y. Saito et al., “Negativeprompt inversion: Fast image inversion for editing with text-guided diffusion models,” arXiv preprint arXiv:2305.16807, 2023. 

- [44] Y. Zhang, Y. Ikemiya, G. Xia et al., “Musicmagus: zero-shot text-to-music editing via diffusion models,” in Proceedings of the Thirty-Third International Joint Conference on Artificial Intelligence, 2024, pp. 7805– 7813. 

- [45] J. Nistal, M. Pasini, and S. Lattner, “Improving musical accompaniment co-creation via diffusion transformers,” arXiv preprint arXiv:2410.23005, 2024. 

- [46] L. Lin, G. Xia, Y. Zhang et al., “Arrange, inpaint, and refine: steerable long-term music audio generation and editing via content-based controls,” in Proceedings of the Thirty-Third International Joint Conference on Artificial Intelligence, 2024, pp. 7690–7698. 

269 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [47] J. Lee, N. J. Bryan, J. Salamon et al., “Disentangled multidimensional metric learning for music similarity,” in ICASSP 2020-2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2020, pp. 6–10. 

- [48] J. Guinot, E. Quinton, and G. Fazekas, “Leave-oneequivariant: Alleviating invariance-related information loss in contrastive music representations,” in ICASSP 2025-2025 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2025, pp. 1–5. 

- [49] M. C. McCallum, F. Henkel, J. Kim et al., “Similar but faster: manipulation of tempo in music audio embeddings for tempo prediction and search,” in ICASSP 2024-2024 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2024, pp. 686–690. 

- [50] X. Bao, J. Y. Li, Z. Y. Wan et al., “Diff4steer: Steerable diffusion prior for generative music retrieval with semantic guidance,” in ICASSP 2025-2025 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2025, pp. 1–5. 

- [51] M. C. McCallum, F. Korzeniowski, S. Oramas et al., “Supervised and unsupervised learning of audio representations for music understanding,” in Ismir 2022 Hybrid Conference, 2022. 

- [52] K. Chen, X. Du, B. Zhu et al., “Hts-at: A hierarchical token-semantic audio transformer for sound classification and detection,” in ICASSP 2022-2022 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2022, pp. 646–650. 

   - [58] A. Agostinelli, T. I. Denk, Z. Borsos et al., “MusicLM: Generating music from text,” arXiv preprint arXiv:2301.11325, 2023. 

   - [59] Y. Yu, C. Xiong, S. Sun et al., “Coco-dr: Combating distribution shifts in zero-shot dense retrieval with contrastive and distributionally robust learning,” in Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing, 2022, pp. 1462– 1479. 

   - [60] E. Khramtsova, S. Zhuang, M. Baktashmotlagh et al., “Selecting which dense retriever to use for zero-shot search,” in Proceedings of the Annual International ACM SIGIR Conference on Research and Development in Information Retrieval in the Asia Pacific Region, 2023, pp. 223–233. 

   - [61] Y. Zhou, J. Ren, F. Li et al., “Test-time distribution normalization for contrastively learned visual-language models,” Advances in Neural Information Processing Systems, vol. 36, pp. 47 105–47 123, 2023. 

   - [62] B. Sun, J. Feng, and K. Saenko, “Correlation alignment for unsupervised domain adaptation,” Domain adaptation in computer vision applications, pp. 153–171, 2017. 

   - [63] D. Friedman and A. B. Dieng, “The vendi score: A diversity evaluation metric for machine learning,” arXiv preprint arXiv:2210.02410, 2022. 

   - [64] D. Bogdanov, M. Won, P. Tovstogan et al., “The mtgjamendo dataset for automatic music tagging,” in Machine Learning for Music Discovery Workshop, International Conference on Machine Learning (ICML 2019), Long Beach, CA, United States, 2019. 

- [53] H. W. Chung, L. Hou, S. Longpre et al., “Scaling instruction-finetuned language models,” Journal of Machine Learning Research, vol. 25, no. 70, pp. 1–53, 2024. 

- [54] Y. Liu, M. Ott, N. Goyal et al., “Roberta: A robustly optimized bert pretraining approach,” arXiv preprint arXiv:1907.11692, 2019. 

- [55] J. Melechovsky, Z. Guo, D. Ghosal et al., “Mustango: Toward controllable text-to-music generation,” in Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), 2024, pp. 8286–8309. 

- [56] J. Copet, F. Kreuk, I. Gat et al., “Simple and controllable music generation,” Advances in Neural Information Processing Systems, vol. 36, pp. 47 704–47 720, 2023. 

- [57] I. Manco, B. Weck, S. Doh et al., “The song describer dataset: a corpus of audio captions for music-andlanguage evaluation,” NeurIPS Machine Learning for Audio Workshop, 2023. 

270 

