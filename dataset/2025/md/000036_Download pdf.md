---
paper_id: "000036"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706401/files/000036.pdf"
---

# A THEORETICAL MODEL OF MUSICAL FORM 

## Martin Rohrmeier 

Digital and Cognitive Musicology Lab École Polytechnique Fédérale de Lausanne `martin.rohrmeier@epfl.ch` 

## Markus Neuwirth 

Institute for Theory and History Anton Bruckner University, Linz 

```
markus.neuwirth@bruckneruni.at
```

### ABSTRACT 

Musical form is one of the most central aspects of musical structure, as it concerns the overarching organization principles of music across genres and styles. Therefore, understanding the formal characterization of musical form is a central topic in music theory, computational music analysis, MIR, and music generation. This paper makes a theoretical contribution proposing a formal model that characterizes the main aspects of musical form. We characterize musical form by the following aspects: Grouping structure, rhythmic partitioning, formal functions, repetition structure, schemata, and harmonic anchor points. As the structures of hierarchical segmentation as well as formfunctionality have previously been conceptualized in terms of a recursive tree-shaped hierarchy, we ground our model in abstract generative grammars. Our model extends this hierarchical analysis by an account of the rhythmical properties of form as well as repetition structure. The harmonic layout defines constraints for motivic content (pitch and rhythm). Our approach also addresses repetition structure by modeling the location and degree of variation of repeated ideas. This is achieved via variable binding. We exemplify our theoretical contribution by a detailed analysis. 

### 1. INTRODUCTION 

The term “musical form” is complex and has a variety of uses in musical practice and research. For instance, Jazz musicians may negotiate the form they perform as Blues form, Rhythm changes, or A A B A or A A forms. Such schemata characterize form with regard to grouping and rhythmic partitioning, concrete chords or defined harmonic anchor positions, as well as repetition patterns for melody or entire parts. For instance, Rhythm changes may be characterized as a 32-bar A A B A schema, where A instantiates an 8-bar unit with a core melody and particular tonal anchor points (a tonic at the beginning and the end) and where a middle section B displays a Fonte schema (i.e., a specific variant of a descending-fifths sequence [1]). Notably, there are also certain abstract formal functions (such 

> © M. Rohrmeier and M. Neuwirth. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: M. Rohrmeier and M. Neuwirth, “A Theoretical Model of Musical Form”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

as beginnings, middles, and endings) that are expressed with the help of specific harmonic and voice-leading patterns [2]. Also, there are formal templates, such as concerto form, rondo form, or sonata form, which have a stronger focus on thematic and tonal (modulation) plans. Such form types, however, also embody aspects of overall dramaturgic trajectories as well as prototypical rhythmic styles and instrumentation. 

Presently, there is no ready-to-use theoretical model of musical form that lends itself for computational implementation and application. Also, from the perspective of computational generation, form is still a challenge, since as of yet overarching long-term coherence is hard to achieve, e.g. for deep-learning approaches. Addressing this gap, our paper proposes a theoretical contribution, outlining a grammar-based model of musical form at the symbolic level. We propose a characterization of musical form in tonal music from the (extended) common practice, taking into account the features of grouping structure, rhythmic partitioning, formal functions, repetition structure, schemata, and harmonic anchor points. 

### 1.1 Related literature 

In music theory, there are numerous studies that address specific questions of form-building in a wide variety of repertoires (e.g., in classical and romantic styles or in Pop/Rock and Jazz; [2–4]). Similarly, in the domain of computational musicology and MIR important components of musical form (such as segmentation, repetition, and cadences) are being tackled (e.g., [5]). Yet both fields still lack a comprehensive model of musical form, and there are only few datasets of formal annotations available (e.g., [6–9]). The following overview lists such partial approaches to form. 

There are several approaches modeling segmentation. Cambouropoulos proposes a rule-based model for rhythmic boundary detection [10]. Bod models segmentation in the Essen folksong collection by probabilistic grammars [11, 12]. Hamanaka et al. [13, 14] have developed a computational model of grouping structure from the GTTM [15]. Feisthauer et al. rely on rhythmic, textural, and harmonic features in order to infer structural breaks in sonataform movements. To detect these moments of caesura, they draw on a dataset of 27 string-quartet movements by Mozart, training an LSTM neural network [16]. 

Several studies address formal boundaries by focusing on cadences. Hentschel et al. [17] offer a corpus of all 

312 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

Mozart piano sonatas featuring expert-labels of harmonic, phrase, and cadence analyses. Raz et al. [18] present a large dataset of Mozart’s instrumental works with historically informed expert annotations of cadential moments. Other studies are devoted to the automatic detection of cadences and cadence types [19–21]. 

Few studies explicitly model repetition in a symbolic fashion. Since repetition requires a model of at least context-sensitive complexity [22,23], recent contributions model repetition in music with variable binding for specific subtrees [24,25]. 

There are recent approaches analyzing keys and key trajectories by way of hierarchical scape plots [26–29]. Weiß et al. use visualizations of local key characteristics in audio recordings to explore the traditional sonata-form model in relation to historical accounts of form based on selected Beethoven sonatas [30]. Allegraud et al. model sonata form by using Hidden Markov Models trained on a labeled dataset [31]. 

### 2. MODELING MUSICAL FORM 

Our proposed model characterizes musical form in terms of grouping structure [15], rhythmic partitioning (based on [32]), formal functions, repetition structure, schemata, and harmonic anchor points. It models the interplay of these parameters in generating the formal outline of a musical piece. More specifically, we conceptualize form as a kind of latent structure that models segmentation and casts concrete constraints for the placement of repetition, anchor chords, and specific musical schemata. Hence, the result of the form model is understood as a layout (a cloze) of these musical features. Such a form layout may be relevant for music generation; conversely, form analysis consists in inferring the layout and latent form parameters from a given piece. 

Our model adopts hierarchical structures, as they are well-suited to express containment relationships essential for musical form. We found previously, however, that the different kinds of hierarchical structures identified in music cannot be subsumed under a single overarching tree model. Specifically, while the repetition structure and the harmonic dependencies of a piece of music can each be modeled in terms of hierarchical trees [24, 33, 34], the branchings of these trees, however, often do not match, implying that these are mutually independent structural domains. Moreover, the parse of top-level structure of harmonic trees is often highly ambiguous. This ambiguity can, however, be resolved by reference to musical form [35, 36], as the top level of the harmonic tree commonly reflects the outline of the formal prototype [34]. This holds for many pieces, though there are examples (e.g., “Solar” or “Blues for Alice”), where the harmonic tree can be mostly independent of the form hierarchy. 

Taking these findings into account, our proposed solution to modeling form and maintaining the mutual independence of grouping/repetition structure and harmonic hierarchy lies in the following approach: There is a joint toplevel form tree, which is guided by rhythmic grouping and 

formal functions [37] and generates the core organization of the piece or segment. This involves a layout/cloze of the core chords, repetitions, and schemata at certain locations, which constitutes a binding interface for the harmonic and repetition trees. This core structure is then filled in by generating harmony and repetition structure as separate trees, beginning from the joint form tree. 

Concretely, our model operates in four stages of generation: (1) generate a template of the overarching grouping and form-functional design for the whole piece (or segment) with harmonic, schematic and repetition anchor points. (2) This top-level layout is used to generate the harmonic structure of the piece, including repetitions of harmonic progressions when required by the formal template. (3) A model of figurative repetition structure takes the top-level form layout (from (1)) and generates a layout of the grouping and repetition of ideas, taking account of harmony when necessary. These steps result in a detailed description of the piece at the tonal, harmonic, and figurative levels, which we consider a full characterization of its form and its implications for the musical material. A final step for music generation (which is not part of this paper) would be (4) to instantiate this structure with concrete musical material. 

### 2.1 The grammar 

Our formalism employs abstract context-free grammars [38] and defines a grammar G := (F, R, f0) as a set of nonterminal symbols of form categories F, a set of rule functions R, and a start symbol f0 ∈F. In the special case of this grammar, there are no dedicated terminal symbols, since the generation merely results in a sequence of formcategory symbols, which subsequently are further used to generate harmonic and figurative trees. In other words, any form-category symbol except for the start symbol can be terminal, and the generation can stop at any point in the context of this joint top-level form tree. 

We define form categories (c ∈F) as a composite structure that combines features of formal functions, rhythmic categories, schema, harmony, and repetition. Specifically, adapting [37], it is assumed that form-functionality subdivides into four categories (beginning, middle, end, whole), while only the start symbol instantiates the value whole. Using the formal model of rhythm in [32], the rhythmic feature encodes categories involving timespan and its hypermeter. The set of schema features S is an enumeration type of form prototypes (e.g., binary, ternary, sentence, period, presentation, continuation) and voiceleading schemata (e.g., sequences such as Fonte, Monte, descending fifths, etc. [1], and cadences such as PAC, HC, etc. [17]). The repetition feature encodes a set of identifiers (V) for variables that guide the repetition of subtrees or repetition of figurative ideas (see 2.6). The harmony feature encodes chord symbols and keys [34,39]. The start symbol f0 defines the formal function whole, the duration of the piece or segment, the only repetition identifier that cannot be repeated, and tonic I and key of the piece; it may optionally encode a form schema (e.g., binary or ternary). 

313 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
 functionrhythm : : [∈upbeat[beg, mid, end, whole : body : coda], M] <br>c := schema : s ∈S<br>harmony : chord ∈H<br> repetition : v ∈V  ∈F<br><!-- End of picture text -->

The production of a form category with rule function r acts in such a way that the features of the child categories are successively filled. (1) The formal functions are generated, which also sets the grouping cardinality. (2) The rhythmic proportion of the split is decided. (3) The schema feature is set (or left empty). (4) Harmony is set; and (5) Repetition constraints are set if required by the form schema (e.g., a period). If the parent form category invokes a specific schema, the rewrite takes place by inserting an entire template subtree (see 2.5), following the formalism with variable binding described by [24]. Similarly, if the repetition feature of the parent category requires a repetition, the respective repeated subtree is inserted. 

### 2.2 Formal functions 

The three formal functions beg, mid, end guide the grouping structure and the production process (whole only applies to the start of the derivation). Formalizing [2], the following production rules govern the production of formal functions. The start symbol whole can only be rewritten in terms of the general rules (1–3). 



<!-- Start of picture text -->
__ −→ beg [mid] [mid] end (1)<br>__ −→ beg beg mid end (2)<br>__ −→ beg mid end end (3)<br>beg −→ beg mid | mid end (4)<br>mid −→ mid mid | mid end (5)<br>end −→ mid end | end end (6)<br><!-- End of picture text -->

Formal functions cast implications on harmonic anchor points (e.g., tonic statements at beginnings, sequences or tonal transitions at middles, and cadences at ends), which we model by setting constraints for the harmony feature of the category. Crucially, harmonic features can only be set if they are also licensed (i.e., derivable) by the rules of the harmonic grammar [33, 34]. For instance, a rewrite beghar=I → beg mid end may set harmonic anchors I, V , I respectively; and this is possible because the progression I V I is derivable by the harmonic rules I → I I and I → V I in the following derivation sequence: I → I I → I V I. Accordingly, implications on harmonic anchors encompass rules like the following examples:<sup>1</sup> 



<!-- Start of picture text -->
c_beg =⇒ c_har:=I|I∗ (7)<br>c_mid =⇒ c_har:=V |I (8)<br>c_end =⇒ c_har:=I (9)<br><!-- End of picture text -->

> 1 Note that I∗ implies an open tonic constituent that may be followed by an unresolved V (no right-branch tonic closure; see [35]). 

Formal functions may also have implications for different harmonic/voice-leading schemata (e.g., middle schemata or cadences). The form-functionality and recursive nature of the form tree have an impact on the closural strength of such cadential endings: for instance, the end of an antecedent (beg) of a first section (beg) may be weak, implying either a HC or an IAC; the end of the consequent (end) of a first section (beg) may be the strongest of its section, but weaker than the final cadence at the end of the final part (end) of the second section (end). Hence, it requires the setup of a style-specific function closure(c) �→ CAD that selects the cadence type with the appropriate degree of closural strength [40] based on the formal functions of the ancestry of the form category c. In our model, we assume the following set of closure schemata (ordered from strong to weak closure): CAD = {PAC, IAC, HC, DEC, EVAD, PLAG, TC}, which stand for perfect authentic, imperfect authentic cadence, half, deceptive, evaded, plagal cadences, as well as tonic completion. Formal functions also have implications on other style-specific schemata, such as sequences or transitions (SEQ, TRANS), which constitute middles. Rules to encompass such schematic implication have the form shown in the following examples: 



<!-- Start of picture text -->
c_end =⇒ c_schema:=closure(c) (10)<br><!-- End of picture text -->



<!-- Start of picture text -->
c_mid =⇒ c_schema:=SEQ|TRANS (11)<br><!-- End of picture text -->

### 2.3 Grouping structure and rhythmic partitioning 

The grouping structure characterizes the containment relationships of units as well as the subunits that a larger unit consists of, and is reflected in the branching structure of the tree. In our model, the rewrite of formal functions defines the grouping structure. 

Based on the cardinality of the subdivision, the rhythmic model completes the temporal partitioning of the child categories. For this purpose, a simplified version of the hierarchical model of rhythm proposed by [32] is adopted, which only employs the split rule. The central condition of the rhythmic partitioning is that the sum of the durations assigned to the children matches the duration of the parent category.<sup>2</sup> Hence, the partition of rhythmic features ti of the respective categories obeys the following requirement: 



<!-- Start of picture text -->
t0 −→ t1 t2 | t1 t2 t3 | t1 t2 t3 t4, � ti =| t0 | (12)<br><!-- End of picture text -->

The proportions of the splits are preferably simple integer ratios: 1:1, 1:1:1, 1:1:1:1, 2:1, 2:1:1, 2:1:2:1, 3:1, etc., in line with results from previous computational research [41]. Based on our prior exploration, all form splits could be explained with the simple ratios based on {1, 2, 3}. 

### 2.4 Harmonic anchors 

The form tree places harmonic anchors that the harmonic grammar (or other model) is required to respect. These an- 

> 2 Following [32], the duration of a timespan category in units of beats is defined as |[a : b : c]| := b − a + c. 

314 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

chors are defined along with the generation of each subdivision in the form tree. Based on the branching and its formal functions, harmonic anchors are defined that govern the head of the harmonic structure of the timespan of the category. The harmonic anchor labels follow the rules of harmonic grammars outlined in previous work [34,35,39]. For example, a rewrite endhar=i → mid end could be matched with a rewrite of the harmonic features as I → V I, such that the new children have the features midhar=V , endhar=I . This conceptualization implements the proposal by [34] that the top-level structures of harmonic and form trees should match. Accordingly, production rules of formal functions select appropriate harmonic rewrites, that match harmonic implications of formal functions as defined in [2,37]. As outlined in 2.2, in the special case of ternary or quarternary branching (harmonic dependencies are normally binary), there needs to exist a valid derivable harmonic subtree, that matches the sequence of harmonic anchors. This generation procedure ensures that the harmonic features alone produce a valid harmonic subtree, which could then generate finer details originating from the form layout. 

### 2.5 Schemata and templates 

It is an essential characteristic of form that certain aspects are repeated or schematized as full templates. This concerns standardized form units, such as phrase and theme types, harmonic or voice-leading schemata (e.g., cadences or sequences), and repeated parts (with or without variation), such as in ABA forms [2]. All of these have in common that entire subtrees are inserted, which come either from stylistic templates or from the piece itself [25], similar to reuse grammars in linguistics [42]. These aspects could be represented in the form tree in two ways: First, symbols that invoke such templates or repetitions should be inserted by the independent harmonic or repetition trees (such as PAC or i1, i1). Second, if the form itself requires a repetition, such as in a period, the repetition is directly placed into the form tree using the same mechanism for variable bound repetition [24]. The detailed example in Figure 2 illustrates the working of such templates in terms of cadences (PAC), a Fonte sequence in the middle, and a sentence phrase schema for the first 8 measures. An advantage of this conceptualization is that it makes it possible to express common form prototypes [2] in terms of tree templates of our form grammar. For instance, two prominent thematic prototypes can be expressed in terms of two template trees: 



<!-- Start of picture text -->
periodI sentence,I<br>Aant,beg,I∗|I A ′ cons,end,I Apres,beg,I Bcont,end,I<br>i1 i2,HC|IAC i1 i ′ 2,P AC i1 i ′ 1,HC|IAC|T C i2,mid i3,PAC<br><!-- End of picture text -->

These templates express that the period is characterized by its two almost identical parts (antecedent, consequent), the former with a beg function and a weak ending (HC, IAC), the latter with an end function and a strong close (PAC); the sentence template exhibits two different parts, 

with the first (beg) featuring motivic repetition of its two parts and weak closure (TC), the latter a middle function, and a strong close in the second subpart. Figure 2 illustrates an instance of the sentence prototype. 

### 2.6 Figurative and motivic repetition 

The previous section outlined the way in which repetition may be encoded in the form tree. This section describes how the representation of motivic variation is modeled and how the independent repetition tree is built (step (3) of the generation process) based on the model of repetition structure in [24]. 

We model motivic variation in terms of a set of primary musical ideas and the composition of functions that derive composite ideas from simple ones. The set of primary ideas may represent original ideas (motives or smaller figures) for the specific piece to be modeled as well as general schematic material (such as cadences or clausulae, etc.). The set η defines the entire set of ideas that is built from primary ideas and composite ones. The entire piece and the constitutive parts thereof are modeled as a primary or composite idea. This way of characterizing motivic relationships establishes an ancestry representation capturing the components and operations ideas are built from. 

The core functions to model the construction of new ideas from previous or primary ideas are concatenation (concat), exact chromatic transposition (transp), diatonic transposition inside the current scale (dtransp), adaptation to specific harmonies (adapt), fragmentation (frag), inverse (inv), retrograde (retro), diminution (dim), augmentation (aug), and variation (var) for other kinds of changes. All of these functions map one or more ideas from η to a composite idea that is to be appended to η. Accordingly, the following defines the signatures of these functions (where iv is the set of musical intervals, and C the set of chords). 



<!-- Start of picture text -->
conc : η × η �→ η (13)<br>transp, dtransp : η × iv �→ η (14)<br>adapt : η × C �→ η (15)<br><!-- End of picture text -->



<!-- Start of picture text -->
frag, inv, retro, dim, aug, var : η �→ η (16)<br><!-- End of picture text -->

The repetition tree models containment relations that express how larger parts are composed of smaller ones, extending previous approaches [24]. The nodes in the tree constitute variables that indicate repeated elements, as well as transformations that indicate variation of content. The repetition tree algorithm begins with the tree shape of the form tree and an empty set of repetition variables (ik). The algorithm operates in recursive depth-first left-branching tree generation/expansion. Every time a leaf is reached, it decides whether to add another subdivision (until a reasonable end is reached, e.g., a 1-measure limit), or to choose to establish and insert a new variable in+1, or to draw one from the existing pool of variables that matches the duration. If a new variable is created, it is added to the pool. If an existing variable is chosen, the algorithm selects whether or not to vary this variable. If yes, it is varied according to the function composition below. Once all 

315 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
adapt & var<br>adapt<br>adapt dtranspvar var<br>aug<br>dtransp<br>concat concat concat inv & transp var & transp<br>concat transp<br>augment<br>i1 dtransp i3 var & var i1 dtransp i<br>(compress<br>adapt)<br>concat<br>concat concat adapt & var var & dtransp<br>i2 (i)<br>concat<br>i5 var<br><!-- End of picture text -->

Figure 1. Dependency and derivation graph of the ideas in Mozart’s minuet, K. 1 (see Figure 2 for the full piece). 

branches of a subtree are complete, the algorithm decides to create a new identifier for the head of the subtree and adds it to the pool. For the subsequent recursive generation, the algorithm can also decide at heads of subtrees to repeat a subtree if there is a length-matching variable in the pool, thus completing this branch. Finally, if the form tree has set constraints on the repetition, the algorithm has to respect these constraints in its definition of repetitions. 



<!-- Start of picture text -->
(i ′ 1 )t := dtransp(i′ 1 , −1) (19)<br>i2 := concat(i1, i t 1 ); i t 2′ := adapt(var(i2)) (20)<br>i3 := concat(α, dtransp(α, −2)), (21)<br>α := adapt(frag(i1)) = adapt(β1)<br>i ′ 3 := var(i 3 ); (i ′ 3 )′ := var(aug(i′ 3 )) (22)<br>i t 3 := transp(i 3 , −7); (23)<br>((i ′ 3 )t)′ := inv(transp(i′ 3 , 5)) (24)<br><!-- End of picture text -->



<!-- Start of picture text -->
(((i ′ 3 )′)t)′ := var(transp((i′ 3 )′, 5) (25)<br><!-- End of picture text -->



<!-- Start of picture text -->
i4 := concat(i3, i ′ 3 , (i′ 3 )′); (26)<br><!-- End of picture text -->

### 3. EXAMPLE ANALYSIS 

Figure 2 shows a detailed analysis of an early Mozart minuet, K. 1, to illustrate the formalism. The piece constitutes a 16-measure two-part (=binary) form. The first section consists of 8 measures (conforming to the thematic prototype of a sentence), which in turn are subdivided into two 4-measure units: a presentation phrase and a continuation phrase. The second section of the piece encompasses 8 measures, too, and consists of a harmonic and melodic sequence, which forms the middle of 4 measures, and a final part of 4 measures, which closes the piece. Each large 8-measure section closes with a cadence (a perfect authentic cadence, PAC), while the initial 4-measure unit of each section projects only a weak sense of closure (TC). Notably, the form and repetition trees reveal that both parts share the same abstract features, resembling the period template. Further note that the sequence part repeats the initial motives, which is a decision taken at the level of the repetition tree rather than the form layout (see Fig. 2). 

Figure 1 and the following dependency definitions model the figurative repetition structure and exemplify the working of the function composition formalism. 



<!-- Start of picture text -->
i1 := concat(β1, β2); i t 1 := transp(i 1 , −1) (17)<br><!-- End of picture text -->



<!-- Start of picture text -->
i ′ 1 := concat(adapt(β 1 ), adapt(var(β 2 ))) (18)<br><!-- End of picture text -->



<!-- Start of picture text -->
i ′ 4 := var(dtransp(i 4 , 5)) (27)<br><!-- End of picture text -->



<!-- Start of picture text -->
[= concat(i3 t , ((i′ 3 )t)′, (((i′ 3 )′)t)′)]<br><!-- End of picture text -->



<!-- Start of picture text -->
i5 := concat(i2, i4) (28)<br><!-- End of picture text -->



<!-- Start of picture text -->
i ′ 5 := var(i 5 ) = var(concat(i 2 , i 4 )) (29)<br><!-- End of picture text -->



<!-- Start of picture text -->
[= concat(i2 t ′, i′4 )]<br><!-- End of picture text -->

### 4. CONCLUSION 

Our model of musical form seeks to account for essential form-determining factors and their complex interplay. Importantly, our model is not a model of composition, although it could be useful in an overall music generation pipeline. Also, the model needs to be tested by implementation, and the implementation needs to be probabilistic in order to be able to dynamically capture stylistic details. Unsupervised rule inference methods may even achieve better results [35]. Since the core stylistic scope of the model concerns tonal music of the (extended) common practice, it will be necessary to test its applicability beyond that repertoire. The fact that the model encompasses general categories (such as the basic formal functions of beginning, middle, and end) renders it sufficiently flexible to be useful for the characterization of other (potentially even non-Western) styles. Further steps include modeling insertions that expand formal prototypes as well as incorporating polyphony and voice-leading. 

316 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
Ikey=G : 16<br>I∗ : 8 I : 8<br>I : 4 V : 4, PAC I : 4, SEQ, TC I : 4, PAC<br>I∗ : 2, beg I : 2, TC Ikey=V V : 3 I : 1 I : 2, mid I : 2, PAC<br>I : 1 vii o6 : 1 vii o : 1 I : 1 I : 2, mid I : 2, PAC ii : 2 V : 1 V 6 : 5 3 I : 3 1 V : 1 I : 1<br>V 6 : 3 5 I : 1 3 V : 1 I : 1 V/ii : 1 ii : 1 ii : 2 3 V 6 : 3 3 ii : 1 3 V : 3 2<br>ii 6 : 3 2 V 6 : 3 3 IV : 3 1 V : 2 3<br>↑<br> fun:rhy: whole ( 2 8 : 16 · 3 : − 2 8 ) <br>schema: binary<br>har: Ikey=Gmaj<br>(((((((((rep:((__(hhhhhhhhhhhh<br> fun:rhy: beg ( 8 2 : 8 · 3 : − 1 4 )   fun:rhy: end ( 8 2 : 8 · 3 : − 4 1 ) <br>schema: antecedent, sentence type: consequent<br>har: I∗ har: I<br> rep: µ1   rep: µ ′ 1 <br>XXXXXXX XXXXXXX<br> fun:rhy: beg ( 2 8 : 4 · 3 : − 1 4 )   fun:rhy: end ( 8 2 : 4 · 3 : − 1 4 )   fun:rhy: mid ( 2 8 : 4 · 3 : 0)   fun:rhy: end(0 : 4 · 3 : − 16 1 ) <br>schema: presentation, TC schema: continuation, PAC schema: sequence, TC schema: continuation, PAC<br>har: I har: V = IDmaj har: I har: I<br>′<br> rep:����__ HHHH   rep:����µ3 bbb   �rep:���__HHHH   rep:���µ� t 3 bbb <br> (1 : 6 : −beg1)  (1 : 6 : −end1)  (1 : 6 :mid0)  (0 : 6 : −end1)  (1 : 6 : −mid1)  (1 : 6 : −mid1)  (1 : 6 :mid0)  (0 : 6 : −end1) <br>I__∗ TCI Ikey=__V IkeyPAC=V SEQ__ SEQ, TCI __I PACI<br> µ2  µ t 2  __  __  __  __  __  __ <br>↓<br>i6 : 16<br>i5 : 8(= µ1) i ′ 5 : 8(= µ 1 ′ )<br>i2 : 4 i4 : 4(= µ3) (i t 2 )′ : 4 i ′ 4 : 4(= µt 3′)<br>i1 : 2(= µ1) i t 1 : 2(= µt 2 ) i3 : 1 i ′ 3 : 1 (i ′ 3 )′ : 2 i ′ 1 : 2 (i ′ 1 )t′ : 2 i t 3 : 1 ((i ′ 3 )t)′ : 1 (((i ′ 3 )′)t)′ : 2<br>Form layout<br>measure: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16<br>schema: binary<br>schema: antecedent, sentence consequent<br>schema: presentation continuation sequence continuation<br>schema: TC PAC SEQ, TC PAC<br>harmony: I I Ikey=V Ikey=V I I I<br>re p etition: µ 1 µ t 1 µ 3 µ t 3 ′<br>re p etition: i1 i t 1 i3 i ′ 3 ( i ′ 3 )′ i ′ 1 ( i ′ 1 )t i t 3 (( i ′ 3 )t)′ ((( i ′ 3 )′)t)′<br>harmon y : I vii o6 vii o I V: [ ii V 6 - -V 6 I IV V I ] I:V / ii ii V 7 I ii V 6 − −V 6 I ii V I<br>                            3                                  <br>3<br>                                               <br><br><!-- End of picture text -->

Figure 2. Example analysis of Mozart, Minuet in G, K. 1, showing the form analysis (middle), the partially matching (dashed) harmonic tree (top) and the partially matching repetition tree (above form layout). All three hierarchical models combine to construct the form layout (bottom) that captures the core formal properties of the piece (for analysis or genera317 tion). 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

### 5. ACKNOWLEDGMENTS 

This research is part of the project “Towards a Unified Model of Musical Form: Bridging Music Theory, Digital Corpus Research, and Computation” (grant no. 10000183; 2024-2028), a collaboration between the École Polytechnique Fédérale de Lausanne and the Anton Bruckner University in Linz, funded by the Swiss National Science Foundation (SNSF) via the Sinergia program. In part, this project has received funding from the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme under grant agreement No 760081 – PMSB. We thank Mr. Claude Latour for generously supporting this research through the Latour chair in digital musicology. 

### 6. REFERENCES 

- [1] R. O. Gjerdingen, Music in the Galant Style. New York: Oxford University Press, 2007. 

- [2] W. E. Caplin, Classical Form: A Theory of Formal Functions for the Instrumental Music of Haydn, Mozart, and Beethoven. New York: Oxford University Press, 2001. 

- [3] J. Yust, Organized Time: Rhythm, Tonality, and Form. Oxford: Oxford University Press, 2018. 

- [4] D. Nobile, “Teleology in Verse–Prechorus–Chorus Form, 1965–2020,” Music Theory Online, vol. 28, no. 3, 2022. 

- [5] M. Giraud, R. Groult, and F. Levé, “Computational analysis of musical form,” in Computational Music Analysis. Springer, 2016, pp. 113–136. 

- [6] M. Gotham and M. Ireland, “Taking form: A representation standard, conversion code, and example corpus for recording, visualizing, and studying analyses of musical form,” in 20th International Society for Music Information Retrieval Conference, Delft, 2019, pp. 633–699. 

- [7] D. Tymoczko, M. Gotham, M. S. Cuthbert, and C. Ariza, “The RomanText format: A flexible and standard method for representing roman numeral analyses,” 20th International Society for Music Information Retrieval Conference, Delft, pp. 123–129, 2019. 

- [8] F. C. Moss, W. F. Souza, and M. Rohrmeier, “Harmony and Form in Brazilian Choro: A Corpus-Driven Approach to Musical Style Analysis,” Journal of New Music Research, pp. 1–22, 2020, publisher: Taylor & Francis. 

- [9] C. Harte, M. Sandler, S. Abdallah, and E. Gomez, “Symbolic Representation of Musical Chords. A Proposed Syntax for Text Annotations,” in Proceedings of the 6th International Conference on Music Information Retrieval, London, 2005, pp. 66–71. 

- [10] E. Cambouropoulos, “Musical rhythm: A formal model for determining local boundaries, accents and metre in a melodic surface,” in Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), 1997, iSSN: 16113349. 

- [11] R. Bod, “Memory-Based Models of Melodic Analysis: Challenging the Gestalt Principles,” Journal of New Music Research, vol. 30, no. 3, pp. 27–36, 2001. 

- [12] ——, “A unified model of structural organization in Language and Music,” Journal of Artificial Intelligence Research, vol. 17, pp. 289–308, 2002. 

- [13] M. Hamanaka, K. Hirata, and S. Tojo, “Automatic generation of grouping structure based on the GTTM,” in Proceedings of the International Computer Music conference 2004, 2004, pp. 141–144. 

- [14] ——, “Implementing Methods for Analysing Music Based on Lerdahl and Jackendoff’s Generative Theory of Tonal Music,” in Computational Music Analysis, D. Meredith, Ed. Cham: Springer, 2016, pp. 221–249. 

- [15] F. Lerdahl and R. Jackendoff, A Generative Theory of Tonal Music. Cambridge, MA: MIT Press, 1983. 

- [16] L. Feisthauer, L. Bigo, and M. Giraud, “Modeling and learning structural breaks in sonata forms,” in Proceedings of the International Society for Music Information Retrieval Conference, 2019, pp. 398–404. 

- [17] J. Hentschel, M. Neuwirth, and M. Rohrmeier, “The Annotated Mozart Sonatas: Score, Harmony, and Cadence,” Transactions of the International Society for Music Information Retrieval, vol. 4, no. 1, pp. 67–80, 2021. 

- [18] O. Raz, D. Chawin, and U. B. Rom, “The Mozart Expositional Punctuation Corpus: A Dataset of Interthematic Cadences in Mozart’s Sonata-Allegro Exposition,” Empirical Musicology Review, vol. 16, no. 1, 2021. 

- [19] D. R. Sears, M. T. Pearce, W. E. Caplin, and S. McAdams, “Simulating Melodic and Harmonic Expectations for Tonal Cadences Using Probabilistic Models,” Journal of New Music Research, vol. 47, no. 1, pp. 29–52, 2018. 

- [20] L. Bigo, L. Feisthauer, M. Giraud, F. Levé, L. Bigo, L. Feisthauer, M. Giraud, F. Levé, D. Picardie, and J. Verne, “Relevance of musical features for cadence detection To cite this version : HAL Id : hal01801060,” no. Ismir, 2018. 

- [21] B. Duane, “Melodic patterns and tonal cadences: Bayesian learning of cadential categories from contrapuntal information,” Journal of New Music Research, vol. 48, no. 3, pp. 197–216, 2019, publisher: Taylor & Francis. 

318 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [22] J. E. Hopcroft and J. D. Ullman., Formal Languages and their Relation to Automata. Addison-Wesley Longman Publishing, 1969. 

- [23] M. Sipser, Introduction to the Theory of Computation. Boston, MA: Cengage Learning, 2012. 

- [24] C. Finkensiep, M. Haeberle, F. Eisenbrand, M. Neuwirth, and M. A. Rohrmeier, “RepetitionStructure Inference with Formal Prototypes,” in Proceedings of the 24th International Society for Music Information Retrieval Conference (ISMIR 2023), Milan, Italy, 2023. 

- [25] Z. Ren, Y. Rammos, and M. A. Rohrmeier, “Formal Modeling of Structural Repetition using Tree Compression,” in Proceedings of the 25th International Society for Music Information Retrieval Conference (ISMIR 2025), San Francisco, United States, 2024. 

- [26] C. S. Sapp, “Harmonic Visualizations of Tonal Music,” the International Computer Music Conference (ICMC), pp. 423–430, 2001. 

- [27] ——, “Visual hierarchical key analysis,” Computers in Entertainment (CIE), vol. 3, no. 4, pp. 1–19, 2005, publisher: ACM New York, NY, USA. 

- [28] D. Chawin and U. B. Rom, “Sliding-Window PitchClass Histograms as a Means of Modeling Musical Form,” Transactions of the International Society for Music Information Retrieval, vol. 4, no. 1, 2021. 

- [29] R. Lieck and M. Rohrmeier, “Modelling Hierarchical Key Structure with Pitch Scapes,” in Proceedings of the 21st International Society for Music Information Retrieval Conference (ISMIR 2020), Montreal, Canada, 2020, pp. 811–818. 

- [30] C. Weiß, S. Klauk, M. Gotham, M. Müller, and R. Kleinertz, “Discourse not dualism: An interdisciplinary dialogue on sonata form in beethoven’s early piano sonatas.” in ISMIR, 2020, pp. 199–206. 

- [31] P. Allegraud, L. Bigo, L. Feisthauer, M. Giraud, R. Groult, E. Leguy, and F. Levé, “Learning sonata form structure on mozart’s string quartets,” Transactions of the International Society for Music Information Retrieval, vol. 2, no. 1, 2019, publisher: Ubiquity Press. 

   - [34] ——, “The Syntax of Jazz Harmony: Diatonic Tonality, Phrase Structure, and Form,” Music Theory and Analysis (MTA), vol. 7, no. 1, pp. 1–63, Apr. 2020. [Online]. Available: https://www.ingentaconnect.com/ content/10.11116/MTA.7.1.1 

   - [35] D. Harasim, “The Learnability of the Grammar of Jazz : Bayesian Inference of Hierarchical Structures in Harmony,” PhD Thesis, École Polytechnique Fédérale de Lausanne, 2020. 

   - [36] W. B. De Haas, “Music Information Retrieval Based on Tonal Harmony,” PhD Thesis, Utrecht University, 2012. 

   - [37] W. E. Caplin, “What Are Formal Functions?” in Musical Form, Forms & Formenlehre: Three Methodological Reflections, P. Bergé, Ed. Leuven: Leuven University Press, 2009, pp. 21––40. 

   - [38] D. Harasim, M. Rohrmeier, and T. J. O’Donnell, “A Generalized Parsing Framework for Generative Models of Harmonic Syntax,” in Proceedings of the 19th International Society for Music Information Retrieval Conference, 2018, pp. 152–159. 

   - [39] M. Rohrmeier and M. Neuwirth, “Towards a Syntax of the Classical Cadence,” in What Is a Cadence? Theoretical and Analytical Perspectives on Cadences in the Classical Repertoire, M. Neuwirth and P. Bergé, Eds. Leuven: Leuven University Press, 2015, pp. 285–336, tex.urlyear: 2019-08-23. [Online]. Available: http://www.jstor.org/stable/10.2307/j.ctt14jxt45 

   - [40] D. R. W. Sears, “The classical cadence as a closing schema: Learning, memory, and perception,” Ph.D. dissertation, McGill University, Montreal, Canada, 2017. 

   - [41] D. Harasim, T. J. O’Donnell, and M. Rohrmeier, “Harmonic syntax in time rhythm improves grammatical models of harmony,” in Proceedings of the 20th International Society for Music Information Retrieval Conference, ISMIR 2019, 2019. 

   - [42] T. J. O’Donnell, Productivity and Reuse in Language: A Theory of Linguistic Computation and Storage. Cambridge, MA: MIT Press, 2015. 

- [32] M. Rohrmeier, “Towards a formalization of musical rhythm,” in Proceedings of the 21st International Society for Music Information Retrieval Conference, 2020, pp. 621–629. 

- [33] ——, “Towards a generative syntax of tonal harmony,” Journal of Mathematics and Music, vol. 5, no. 1, pp. 35–53, 2011. [Online]. Available: http://www.tandfonline.com/doi/abs/10.1080/ 17459737.2011.573676 

319 

