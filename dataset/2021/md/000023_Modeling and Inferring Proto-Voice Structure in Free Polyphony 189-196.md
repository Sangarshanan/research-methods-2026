---
paper_id: "000023"
year: 2021
title: "Modeling and Inferring Proto-Voice Structure in Free Polyphony 189-196"
source_url: "https://archives.ismir.net/ismir2021/paper/000023.pdf"
---

# **MODELING AND INFERRING PROTO-VOICE STRUCTURE IN FREE POLYPHONY** 

## **Christoph Finkensiep** 

École Polytechnique Fédérale de Lausanne `christoph.finkensiep@epfl.ch` 

## **Martin Rohrmeier** 

École Polytechnique Fédérale de Lausanne `martin.rohrmeier@epfl.ch` 

### **ABSTRACT** 

Voice leading is considered to play an important role in the structure of Western tonal music. However, the explicit voice assignment of a piece (if present at all) generally does not reflect all phenomena related to voice leading. Instead, voice-leading phenomena can occur in free textures (e.g., in most keyboard music), or cut across the explicitly notated voices (e.g., through _implicit polyphony_ within a single voice). This paper presents a model of _proto-voices_ , voice-like structures that encode sequential and vertical relations between notes without the need to assume explicit voices. Proto-voices are constructed by recursive combination of primitive structural operations, such as insertion of neighbor or passing notes, or horizontalization of simultaneous notes. Together, these operations give rise to a grammar-like hierarchical system that can be used to infer the structural fabric of a piece using a chart parsing algorithm. Such a model can serve as a foundation for defining higher-level latent entities (such as harmonies or voice-leading schemata), explicitly linking them to their realizations on the musical surface. 

### **1. INTRODUCTION** 

A basic observation about tonal structure in music is that notes tend to form vertical and horizontal relations, which are generally not explicit in representations of the musical surface such as a score or a recording. An example of these relations can be seen in Figure 1. The initial line of sixteenth notes in the right hand, for example, forms an arpeggiation of a D-minor chord. A reduction or simplification of the piece might realize this chord as a single vertical entity, but the vertical relation between the notes D5, A4, F4, and D4 is not directly encoded in the score. Similarly, the two A4s of this arpeggiated chord are part of a line that first moves to the neighbor note B _♭_ 4 before returning to A4 on the fourth beat of the first bar. Again, this connection is not explicitly represented in the score, much less so in a recording. 

Sequential relations between notes are sometimes equated with _voices_ [1] that are either explicitly given (e.g. 

> © C. Finkensiep and M. Rohrmeier. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). **Attribution:** C. Finkensiep and M. Rohrmeier, “Modeling and Inferring Proto-Voice Structure in Free Polyphony”, in _Proc. of the 22nd Int. Society for Music Information Retrieval Conf.,_ Online, 2021. 



<!-- Start of picture text -->
� � � � �� � � � � �<br>� � � � � � � � � � � � �� � � � � �<br>�� �� � �<br>� � � � � � �<br>�<br><!-- End of picture text -->

**Figure 1** : An example of free polyphony in J. S. Bach’s Allemande BWV 812 I. Sequential structures (such as the A-B _♭_ -A motion across the first measure) are generally not explicit in the score. 

in monophonic melodies or strict polyphony), or inferred through voice separation [2, 3, 4, 5, 6, 7, 8, 9]. However, sequential relations do not always coincide with voices: A single voice can exhibit _implicit polyphony_ [10, p. 367][11] (also called implied or latent polyphony), i.e., consist itself of several implied sub-voices. For example, in the upper voice in Figure 1, the notes of the D-minor chord belong to separate voices on a more abstract level. Similarly, sequential connections can go across different voices, such as the A4 moving to B _♭_ 4 while the notated voice continues to C _♯_ 4. 

Implicit (or more generally free) polyphony is commonly understood as forming a set of parallel and independent _auditory streams_ [12, 13, 1] that are inferred from the musical surface by connecting notes into sequences. The present paper, in contrast, proposes a model of free polyphony that departs from this view in several respects: First, free polyphony is understood as a network of lines that can be connected to each other rather than a set of independent streams. Second, this network is not defined through inference from the surface, but rather explicitly constructed in a generative process that creates the network in successive steps. Inferring this network from a piece is then based on inverting this process, i.e., _parsing_ the piece. Third, connections between notes are not based on continuing a stream, but instead follow from _elaboration_ of existing structures through fundamental and musically interpretable operations, adopting a top-down view instead of a left-to-right view on voice-leading structure [14, 15]. We name the resulting lines in the network _protovoices_ , since – like voices – they connect notes to sequential lines but cannot be themselves implicitly polyphonic. This paper presents a formal definition of the proto-voice model as a recursive process, and describes a parsing algorithm that can infer the proto-voice structure from a score. 

189 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

This model does not yet account for other musical aspects such as rhythm and meter, harmony, form, or motivic and thematic material. However, it is intended to further the understanding of polyphonic structure on formal grounds, and could potentially serve as a module in a more complete system for musical analysis. 

The idea of modeling free polyphony as a recursively generated network of lines is central to Schenkerian analysis [16]. However, the constructions in Schenkerian analysis are specific to Western Common Practice music and more high-level than the generic operations that give rise to proto-voices. Thus, the proto-voice model can be understood as a formal foundation for describing richer concepts of musical structure (such as the ones appearing in Schenkerian analysis or other analytical frameworks), and it is applicable to a wider range of musical styles that make use of implicit or free polyphony (such as Jazz or melodies in Pop/Rock).<sup>1</sup> However, because of these similar ideas, the model presented here is related to models that formalize sub-systems of Schenkerian analysis [18, 19, 20, 21, 22, 23, 24, 25, 26, 27], and to grammatical models of musical structure in general [14, 15, 28, 29, 17, 30, 31, 32, 33]. While proto-voices inherit some of their concepts, most notably the interval-replacement method developed in [25], modeling the structure of free polyphony has yet been an unsolved problem. 

is maintained through the elaboration operations. _Passing edges_ indicate connections between two notes with an interval that is larger than a step (introducing a new, subordinate proto-voice). They must be filled with passing notes from either end until only stepwise connections remain. 

The generation of a piece starts with the empty piece ⋊ _→_ ⋉ and recursively applies one of several elaborations rules. _Single-sided_ rules pick a note and insert either a repetition or a neighbor note to its left or right: 



<!-- Start of picture text -->
x  = ⇒ x ′ → x repeat-before (1)<br><!-- End of picture text -->



<!-- Start of picture text -->
x  = ⇒ x → x ′ repeat-after (2)<br><!-- End of picture text -->



<!-- Start of picture text -->
x  = ⇒ n → x left-neighbor (3)<br><!-- End of picture text -->



<!-- Start of picture text -->
x  = ⇒ x → n right-neighbor (4)<br><!-- End of picture text -->

_Double-sided_ rules pick an edge and insert along it one new note and two new edges: 



<!-- Start of picture text -->
⋊ → ⋉ = ⇒ ⋊ → x → ⋉ root-note (5)<br><!-- End of picture text -->



<!-- Start of picture text -->
x 1 → x 2 = ⇒ x 1 → x ′ → x 2 full-repeat (6)<br><!-- End of picture text -->



<!-- Start of picture text -->
x → y = ⇒ x → y ′ → y repeat-before’ (7)<br><!-- End of picture text -->



<!-- Start of picture text -->
x → y = ⇒ x → x ′ → y repeat-after’ (8)<br>x 1 → x 2 = ⇒ x 1 → n → x 2 full-neighbor (9)<br><!-- End of picture text -->

_Passing_ rules, finally, fill passing edges with passing notes from either end until the progression is fully stepwise: 

### **2. THE PROTO-VOICE MODEL** 



<!-- Start of picture text -->
x  ��� y = ⇒ x → p  ��� y passing-left (10)<br><!-- End of picture text -->

### **2.1 Constructing Proto-Voices** 

At the core of the model proposed in this paper are a number of operations that establish primitive and strictly stepwise horizontal relations between notes. These relations include _repetitions_ , stepwise ornaments to a note ( _neighbor notes_ ), and notes that fill larger intervals stepwise ( _passing notes_ ). While the notion of a step generally depends on what is considered a step in the respective style, we consider a step to be a diatonic second for the purpose of modeling tonal music in the diatonic tradition. 

All of these operations relate notes to one or two reference notes, or _parents_ . Following Yust [25], operations with two parents are represented by _edge replacement_ : If the two parent notes _p_ 1 and _p_ 2 are connected by an edge _p_ 1 _→ p_ 2, then this edge can be replaced by a child note together with two new edges to the parents: _p_ 1 _→ c → p_ 2. 

Formally, proto-voices are represented as a graph that contains one vertex per note, one vertex each for the beginning (⋊) and the end (⋉) of the piece, and two types of edges: _Regular edges_ indicate a sequential connection between two notes (or ⋊ _/_ ⋉) that may be used for elaboration by introducing a repetition or a neighbor of either parent note (or of both if the parents have the same pitch). The interval along a regular edge is always within the range of a step (unless one of its vertices is ⋊ or ⋉), and this property 

> 1 The principle of recursive ornamentation is also used in non-Western styles, such as Indian classical music [17], the model presented here is specifically inspired by Western tonal music. However, some of the formal techniques presented here might also be useful for expressing structural relations specific to other styles. 



<!-- Start of picture text -->
x  ��� y = ⇒ x  ��� p → y passing-right (11)<br>x  ��� y = ⇒ x → p → y passing-final (12)<br><!-- End of picture text -->

In these rules, matching letters indicate matching pitches, indices disambiguate parent notes with the same pitch, and apostrophes mark inserted repetitions of parent notes. Neighbor notes _n_ must be a step away from their parents, (disregarding their octaves to allow for octave displacement). Similarly, passing notes _p_ must be a step from the parent(s) they are directly connected to and lie within the interval spanned by both parents. Note that none of these rules produce passing edges, which establish new connections between previously unconnected lines and thus require some additional structure (see Section 2.2. An example proto-voice derivation of the previous example (Figure 1) is shown in Figure 2. 

### **2.2 Temporal Organization** 

While proto-voices model the sequential organization of notes, they do not specify when notes are simultaneous. On the musical surface, simultaneity of notes is implied by their onsets and durations. However, notes that are temporally displaced on the surface can often be regarded as forming a vertical sonority on a higher level of abstraction, such as the arpeggiated d-minor chord in the beginning of Figure 1. In order to express these latent vertical configurations, simultaneity is modeled through _slices_ , segments of a piece in which the same notes sounds. A piece (or a reduction of a piece) is then represented as a sequence 

190 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 



<!-- Start of picture text -->
⋊ ⋉<br>a<br>⋊ f ⋉<br>d<br>a a<br>⋊ f f ⋉<br>d d<br>a a a<br>g<br>⋊ f f ⋉<br>e<br>d d<br>c ♯<br>a a a a<br>g g<br>⋊ f f ⋉<br>e e<br>d d d d<br>c ♯<br>b ♭ b ♭<br>a a a a<br>g g g<br>⋊ f f f ⋉<br>e e<br>d d d d d<br>c ♯<br>b ♭ b ♭<br>a a a a<br>g g g g<br>⋊ f f f f ⋉<br>e e e e<br>d d d d d d<br>c ♯<br><!-- End of picture text -->

**Figure 2** : A proto-voice derivation of the notes in Figure 1. The position of a note is chosen to indicate its pitch and onset in the piece. Later derivation steps hide some edges from earlier steps in the interest of readability. Note that each note is shown exactly once here, unlike in the final model, which represents each note once per slice it occurs in. Furthermore, pitches in different octaves have been merged to simplify the graph. 



<!-- Start of picture text -->
t tl tr<br>s<br>t<br>t ′ l s ′ t ′ r t ′ l s ′ l t ′ m s ′ r t ′ r t<br>(a)  split (b)  spread (c)  freeze<br><!-- End of picture text -->

**Figure 3** : The three operations on outer structure. The slices and transitions to be elaborated are shown at the top while the lower part shows the generated structure. 

of slices. Notes that are simultaneous with several nonsimultaneous notes (such as the bass note D in Figure 1) are split among the corresponding slices but remain connected by edges, thus ensuring that a surface note is generated through a single generation process. 

Proto-voices are integrated into the slice structure by attaching their edges to the _transitions_ between two slices. Note that transitions can only contain edges that connect notes in the slices adjacent to the transition. Long-distance edges are thus represented in latent transitions, i.e. transitions in a reduction of the piece. As a consequence, edges “vanish” in a well-defined manner during the generation process, namely whenever a transition is replaced through one of the generative operations. Since slices and transitions contain notes and edges, respectively, we call the slices and transitions _outer structure_ , and the notes and edges _inner structure_ . 

Formally, a slice _s_ is defined as a multiset (or bag) of pitches. A transition _t_ = ( _sl, e, sr_ ) relates two slices _sl_ and _sr_ and a configuration of edges _e_ = ( _e_ reg _, e_ pass), which in turn consists of a set of regular edges _e_ reg (which must be used at least once by a subsequent operation) and a multiset of passing edges (which must be used exactly once).<sup>2</sup> 

Outer structure is transformed by three operations: A `split` (Figure 3a) is a rule of the form 



<!-- Start of picture text -->
t −→ t ′ l s′ t r ′ (13)<br><!-- End of picture text -->

that replaces a transition _t_ by inserting a new slice _s_<sup>_′_</sup> and two new transitions _t_<sup>_′_</sup> _l_<sup>and</sup><sup>_t_</sup> _r_<sup>_′_.During this operation, each</sup> edge in the transition and each note in an adjacent slice can be elaborated by one or more inner operations. The resulting edges can either be discarded, or kept to form the new edges of _t_<sup>_′_</sup> _l_<sup>and</sup><sup>_t_</sup> _r_<sup>_′_.Asaresult,eachtransitiononly</sup> contains edges that will be used subsequently. 

A horizontalization, or `spread` (Figure 3b) has the form 



<!-- Start of picture text -->
tl s tr −→ t ′ l s′ l t′ m s′ r t′ r , (14)<br><!-- End of picture text -->

and replaces a slice _s_ by distributing its notes to two child slices _s_<sup>_′_</sup> _l_<sup>and</sup><sup>_s_</sup> _r_<sup>_′_. This way, a latent vertical configuration of</sup> notes can be sequentialized. In order to simplify parsing, a restriction is made on this distribution: At least one side must inherit all instances of a specific pitch, while the other may inherit fewer instances, i.e., 



<!-- Start of picture text -->
p k ∈ s ⇒ p k ∈ s ′ l p k−m ∈ s ′ r or (15)<br>p k ∈ s ⇒ p k−m ∈ s ′ l p k ∈ s ′ r , (16)<br><!-- End of picture text -->

2 Passing edges are treated differently to avoid filling a single passing edge several times. 

191 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 



<!-- Start of picture text -->
⋊ ⋉<br>split<br>{e,c}<br>spread<br>{e,c} {c}<br>split<br>split {b,d}<br>{c,d}<br>(a) Outer structure (slices and transitions).<br>e<br>⋊ d d ⋉<br>c c c<br>b<br>(b) Inner structure (notes and edges).<br>��� � � � � � � � � � � �� � � �<br><!-- End of picture text -->

(c) The derivation steps in abstracted Western notation. 

**Figure 4** : An example derivation of a short cadential phrase. In each `split` operation, the edges of the elaborated transition (grey in (b)) are replaced using inner elaboration operations. The passing edge from e to c is introduced during the `spread` of the top-level {e, c} slice. 

where _k_ denotes the number of occurrences of pitch _p_ in _s_ , and 0 _≤ m ≤ k_ . This way, the _s_ can always be inferred deterministically from _s_<sup>_′_</sup> _l_<sup>and</sup><sup>_s_</sup> _r_<sup>_′_bytakingforeachpitch</sup> the maximum number of occurrences in _s_<sup>_′_</sup> _l_<sup>or</sup><sup>_s_</sup> _r_<sup>_′_.</sup> 

In the process of a `spread` , passing edges may be introduced between arbitrary pairs of notes, and regular edges may be introduced between notes with the same pitch. This way, the introduction of passing edges becomes a local operation that is guaranteed to respect the temporal order of notes. Since all edges in a transition must be used, a `spread` is only allowed when no edges from the parent transitions _tl_ and _tr_ are lost by moving notes to the opposite side. While this operation does not change the contents of _tl_ and _tr_ , it replaces _s_ with _s_<sup>_′_</sup> _l_<sup>and</sup><sup>_s_</sup> _r_<sup>_′_respectively, which</sup> makes this operation context-sensitive. 

Finally, a `freeze` (Figure 3c) marks a transition as terminal, stopping the generation process for this transition: 



<!-- Start of picture text -->
t −→ t. (17)<br><!-- End of picture text -->

It is only allowed when the transition contains only repetition edges, which are turned into ties, creating notes that span several surface slices. 

An example derivation using these three operations can be seen in Figure 4. We use a notation similar to the maximal outerplanar graphs (MOPs) introduced in [25], with the root transition on top, surface of the piece on the bottom, and rule applications indicated by polygons. However, since the derivations here contain latent slices that do not occur on the surface, these derivation graphs are not outerplanar. 

### **3. A PARSING ALGORITHM FOR PROTO-VOICES** 

### **3.1 Representing Derivations** 

The parsing algorithm for the proto-voice model produces a set of possible derivations of the input score. Such a derivation can be represented as a list of rule applications in _leftmost derivation_ order. This representation is known from context-free grammars: the result of the derivation is obtained by applying each rule in the list to the leftmost non-terminal symbol of the current sequence. This is possible because the derivation below each non-terminal of a string is independent from the derivations below all other non-terminals of the string. In the proto-voice grammar, this independence property does not hold, because the context-sensitive operation `spread` can link two otherwise independent transitions (and all their ancestors). However, the idea of a leftmost derivation can still be applied here. 

The maximal left-hand side of a single rule consists of two transitions. Thus, instead of the leftmost nonterminal, we consider the two leftmost non-terminal transitions as the context for each rule application. Freezing the left of the two transitions moves the context to the right. A `spread` consumes both transitions of the context and pushes its children onto the list of open transitions. In order to allow the right parent of a `spread` to be the result of a `split` , `split` s can be applied to either the left or the right transition of the current context. However, in order to disambiguate the derivation order, we restrict right `split` s to always happen _after_ left `split` s or `freeze` s. If only a single transition is left, then only a `split` or `freeze` can be performed. Thus, the derivation shown in Figure 4a can be unambiguously described as the leftmost derivation `split` , `spread` , `freeze` , `split-left` , `split-left` , `freeze` , `freeze` , `freeze` , `freeze` . 

Under these restrictions, certain configurations are not possible. In particular, the right parent transition of a `spread` cannot be the left child transition of another `spread` . However, this _outer_ configuration is equivalent – with respect to the resulting _inner_ structure – to another configuration where the two `spread` s are applied in reverse order. Thus, the generative power of the grammar (with respect to proto-voice structure) is not restricted by excluding this non-leftmost configuration. 

A similar observation above can be made between `split` s and `spread` s: Whenever a `split` is made _after_ a `spread` (i.e. on its left or right child transition), it could as well have been made before the `spread` (generating its left or right parent transition, respectively), generating the same inner structure. Therefore, we can add another restriction on the derivation order that forbids `split` s to be applied to the left or right child transitions of a `spread` , further removing the redundancy between (internally) equivalent derivations. 

In a similar fashion, it is possible to reduce the number of derivations further by eliminating redundancy in the internal structure. For example, slices that are exact repetitions of one of their neighbors can be generated in two 

192 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

ways, either by a `split` that only uses `repeat-⁎` operations on one side, or by a `spread` that produces identical child slices. Since the latter is required for passing edges, the former case might be excluded as redundant. Similarly, the repeated horizontalization of a vertical configuration can generate the same surface configuration in many different ways, which can be prevented by restricting `spread` s to be strictly left- or right-branching (unless intercepted by a `split` ). Both of these restrictions, however, exclude some derivations with slightly different semantics than their permitted counterparts, so it depends on the use cases whether such restrictions are appropriate.<sup>3</sup> 

### **3.2 Parsing** 

Previous models of hierarchical tonal structure have relied on two approaches to structural inference: Grammar-based models use variants of classical parsing techniques such as chart parsing [28, 27] while MOP-based models work with triangulations of polygons [25, 21]. The proto-voice model can be parsed using a bottom-up chart parsing algorithm that is adapted to account for the context-sensitive `spread` operation. A _transition chart_ stores all potential latent transitions, similar to the non-terminal chart in a context-free parser. In addition, a _verticalization chart_ stores items that represent the “core” of a `spread` , i.e. the parent slice and the middle transition (including the two child slices). This core is then combined independently with the left and right child transitions, disentangling the two reductions and reducing the combinatorial complexity.<sup>4</sup> 

The items in the transition chart are tuples ( _t, σ, Il, Ir_ ), consisting of a transition _t_ , a _score σ_ , and two IDs _Il_ and _Ir_ that express combination restrictions on the left and the right of the transition, respectively. By default _Il_ and _Ir_ have a default value _∗_ which indicates that they can combine with other transitions with the default value. The left and the right parent transitions of a `spread` , however, depend on each other through a common child (the `spread` operation itself). They are therefore marked with a special ID on their adjacent sides and can only combine with other transitions with a compatible ID. IDs are based on the _left side_ of the verticalization, i.e. its left child slice and its parent slice. The details of the `spread` operation as well as the middle and right child transitions are stored in the item of the right parent transition, while the left parent transition only keeps a reference to the left child transition. This way, combining any pair of compatible left and right parent transitions restores a complete and valid `spread` operation with all its children. While this “trick” reduces complexity by exploiting some properties specific to the proto-voice grammar, it is not known whether it reduces the overall complexity of the parser from exponential to polynomial in the number of input slices. 

> 3 For example, with a strictly right-branching model, the expansion of the D-minor chord in Figure 1 must happen from left to right. If it is desired to split the chord first into quarter-note slices and then into eightnote slices (to respect the metric structure), strict right-branching does not work. 

> 4 For a given verticalization, instead of considering each pair of left and right transitions ( _|L| · |R|_ operations), the left and right transitions can be processed independently ( _|L|_ + _|R|_ operations). 

The score _σ_ of a transition represents the set of leftmost derivations from the transition to the surface it covers. It is computed bottom-up by combining the scores of the transition’s children. When two transitions are combined, their scores are combined by concatenating each alternative on the left with each alternative on the right.<sup>5</sup> When parsing a `split` operation, this result is prepended with the `split` itself, which yields the score of the parent transition. The score representing a `spread` operation, however, must be distributed across the two parent transitions. This follows the same scheme as described above: the left parent keeps the score of the left child _L_ ; the right parent takes the scores of the right child _R_ , the the middle child _M_ , and the rule application the `spread` itself _h_ . However, since the correct leftmost sequence of operations should apply the scores in the order _hLMR_ the scores of the parent edges are _partial_ , and the parser ensures that these fragmented derivations are handled in a way that always restores the correct sequence of derivation steps when recombined.<sup>6</sup> 

|**Algorithm 1**The steps of theparsingalgorithm.|
|---|



|_V ←_|_{}_|
|---|---|
|_T ←_|unfreeze each input transition|
|**for**_n_|from2to_|_input_| −_1**do**|
|_V _|_←∪_verticalizations of all_Tn_|
|_T _|_←∪_left vert. of all_Tn ⊗V≤n_ and_T<n ⊗Vn_|
|_T _|_←∪_right vert. of all_Vn ⊗T≤n_ and_V<n ⊗Tn_|
|_T _|_←∪_merges of all_Tn ⊗T≤n_ and_T<n ⊗Tn_|
|**retur**|**n**_T_⋊_→_⋉|



The parser fills the chart bottom-up using the algorithm shown in Algorithm 1. Here, _merge_ refers to the inverse of a `split` , _left_ and _right verticalization_ refer to combining a left or right child with a verticalization item, respectively. _Tn_ and _Vn_ refer to the sets of chart items with a surface coverage of _n_ slices, and _⊗_ creates the pairs of those items that are adjacent (i.e. their connecting slices match with respect to position and content) and have compatible IDs. 

The inner structure of each operation is parsed by inverting the operation, computing all possible inputs. For `spread` and `freeze` , this is trivial since their parent elements are unique, if they exist. For `split` , all possible parent transitions are computed that generate every note in _s_<sup>_′_</sup> using all mandatory edges in _t_<sup>_′_</sup> _l_<sup>and</sup><sup>_t_</sup> _r_<sup>_′_(and possibly other</sup> edges that have been dropped and thus not included in _t_<sup>_′_</sup> _l_ and _t_<sup>_′_</sup> _r_<sup>).</sup> 

A reference implementation of the parser written in Haskell is provided.<sup>7</sup> 

> 5 In the parser, this operation is represented symbolically, which is more efficient than actually computing all combinations of alternatives. 

> 6 In particular, since fragmented derivation sets are not always recombined right away, they need to combine with other operations such as `split` s and other `spread` s. The formal details of this are beyond the scope of this paper, but they are documented in the parser implementation. 

7 `https://github.com/DCMLab/protovoices-haskell/tree/ ismir2021` 

193 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

### **4. DISCUSSION AND CONCLUSION** 

The proto-voice model is flexible enough to express highly complex configurations of free polyphony. However, this generative power comes at the cost of being highly ambiguous. The suspension sequence in Figure 4, for example, has 131 valid derivations, while the first half measure (including the upbeat) of the Bach example (Figure 1) already has 119,940 derivations. While this flexibility of the model allows analysts to express very subtle interpretative nuances, it also generates the problem that a single piece or excerpt has too many derivations to reasonably compare, and that any non-trivial piece takes far too long to parse exhaustively in practice. The first problem can be solved by introducing a probabilistic variant of the model that weights derivations according to their probability [32, 28]. The second problem might be resolved by a heuristic parser that does not guarantee globally optimal solutions. 

There are structural configurations assumed in some theories that require an even higher flexibility than what is provided by the proto-voice model. For example, Schenkerian theory allows the _unfolding_ (i.e. horizontalization) of entire progressions (such as the parallel thirds 3-2 and 1-7 in Figure 4) into a single sequence (such as 1-7-3-2(-1)). Such an operation would either require the progression to be represented as a single entity (to which the operation could be applied), or the ability to apply operations to nonentity contexts (similar to how `spread` is applied to two transitions and a slice). 

The inner structure and operations of proto-voices are similar to those of MOP-based approaches [25, 21, 24] for monophonic and homophonic sequences. From these, the model inherits the ability to represent double parents and, by extension, lines of notes with a start and a goal. However, proto-voices use these ideas to solve the much more complex problem of free polyphony. The key insight that makes this extension possible is the separation of adjacency on the surface and adjacency in a line of notes, and the explicit representation of line adjacency in the protovoice graph. In monophonic sequences, surface and line adjacency seem to be the same, but even this assumption does not generally hold: As the example of implied polyphony shows, even monophonic voices can (and generally do) have a polyphonic latent structure. Put bluntly, there is no such thing as a monophonic melody. 

The outer structure (and its integration of inner operations) is similar to an approach presented by Marsden [27], that parses single-sided Schenkerian operations based on a grammar on slices. In particular, Marsden’s grammar uses _context notes_ to model conditions of two-sided operations, which makes the grammar context-sensitive in a very similar way as proto-voices.<sup>8</sup> While Marsden’s model does not rely on explicit voices – and thus in principle can parse inputs in free polyphony – it also does not generate voicelike structure among the notes, but rather individual bi- 

> 8 In [27], this context-sensitiveness is handled by parsing with a context-free parser and then removing inconsistent derivations, while the proto-voice parser only constructs consistent derivations, but this is just an implementation detail. 

nary dependency relations. A similar point can be made for models working on piano-roll representations such as many neural network approaches [34, 35, 36]: While they can work with freely polyphonic inputs, they generally do not explicitly establish polyphonic _structure_ among the notes in the score. 

There is, however, a deeper, more philosophical difference between the proto-voice model and the other approaches based on Schenkerian analysis: The proto-voices attempt to isolate and formalize the _structural principles_ and _primitives_ that give rise to free polyphony, instead of encoding the higher-level concepts and operations of a particular analytical framework. The two structural principles here are _elaboration_ and _recursion_ , where the former consists of the application of primitives and the latter just arises from the fact that elaboration can be applied to the output of a previous elaboration of the same kind. The structural primitives boil down to essentially two operations: stepwise insertion of notes (in all its variants) and horizontalization of simultaneous elements, which operate with the two basic relations on simultaneity and sequentiality in complementary ways. 

These operations are _primitive_ for two reasons: First, they provide what can be considered the lowest level of musically meaningful relations. Even more basic representations of music (such as audio or piano-roll representations) do not express musical relations (except incidental simultaneity) explicitly. Second, the basic entities and relations can be combined to express higher-level entities and relations from more specific analytical frameworks, such as different forms of harmonic analysis, Schenkerian analysis, or schema theory. A simple example of such a highlevel concept can be seen in Figure 4, which constructs the voice-leading pattern of a _2-3 suspension_ in a principled way: first, a progression is generated that moves two voices down in parallel thirds, then another time interval is inserted in which the upper voice moves while the lower voice remains, creating the dissonant second. Similarly, the derivation in Figure 2 explicitly constructs an _initial ascent_ [37] from D to F and the harmonic progression _I − V_<sup>7</sup> _− I_ , and describes their relation to the musical surface. The preparatory function of the dominant chord and its dependency on the tonic [15] are even reflected by its notes, which are all ornaments of the following tonic harmony. 

The structural principles and primitives postulated by this model are certainly not exhaustive. For one, they do not account for musical parameters such as harmony and key, timbre, or rhythm and meter. Furthermore, there might be additional structural primitives that establish other relations between objects than stepwise motion and simultaneity. Finally, there might be other relevant structural principles, such as abstraction of particular configurations into patterns, or the repetition of complex structures or patterns. However, since principles and primitives are generally orthogonal, the current model can be considered as a module of a more comprehensive model of musical structure. 

194 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

### **5. ACKNOWLEDGEMENTS** 

We thank all members of the Digital and Cognitive Musicology Lab at EPFL (in particular Petter Ericson and Daniel Harasim) as well as the anonymous reviewers for their valuable feedback, and Claude Latour for generously supporting this research. This project has received funding from the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme under grant agreement No 760081 – PMSB. 

### **6. REFERENCES** 

- [1] D. Huron. _Voice Leading: The Science Behind a Musical Art_ . MIT Press, Sept. 2, 2016. 273 pp. 

- [2] E. Chew and X. Wu. “Separating Voices in Polyphonic Music: A Contig Mapping Approach”. In: _Computer Music Modeling and Retrieval_ . Ed. by U. K. Wiil. Lecture Notes in Computer Science. Berlin, Heidelberg: Springer, 2005, pp. 1–20. DOI: `10.1007/978-3-540-31807-1_1` . 

- [3] R. de Valk and T. Weyde. “Deep Neural Networks with Voice Entry Estimation Heuristics for Voice Separation in Symbolic Music Representations”. In: _Proceedings of the 19th International Society for Music Information Retrieval Conference_ . 19th International Society for Music Information Retrieval Conference (ISMIR 2018). Paris, France, May 25, 2018. 

- [4] N. Guiomard-Kagan, M. Giraud, R. Groult, and F. Levé. “Comparing Voice and Stream Segmentation Algorithms”. In: _Proceedings of the 16th ISMIR Conference_ . International Society for Music Information Retrieval Conference (ISMIR 2015). Malaga, Spain, Oct. 2015, pp. 493–499. 

- [5] J. Kilian and H. H. Hoos. “Voice Separation-A Local Optimization Approach.” In: International Conference on Music Information Retreival. 2002. 

- [6] P. B. Kirlin and P. E. Utgoff. “VOISE: Learning to Segregate Voices in Explicit and Implicit Polyphony.” In: _Proceedings of the Sixth International Conference on Music Information Retreival_ . ISMIR. London, 2005, pp. 552–557. 

- [7] D. Makris, I. Karydis, and E. Cambouropoulos. “VISA3: Refining the Voice Integration/Segregation Algorithm”. In: _Proceedings of the Sound and Music Computing Conference 2016_ . Hamburg, Germany, 2016. 

- [8] A. McLeod and M. Steedman. “HMM-Based Voice Separation of MIDI Performance”. In: _Journal of New Music Research_ 45.1 (Jan. 2, 2016), pp. 17– 26. DOI: `10.1080/09298215.2015.1136650` . 

   - [10] E. Aldwell and A. Cadwallader. _Harmony and Voice Leading_ . Cengage Learning, 2018. 722 pp. 

   - [11] E. Cambouropoulos. “‘Voice’ Separation: Theoretical, Perceptual and Computational Perspectives”. In: Int. Conf. on Music Perception and Cognition (ICMPC). 2006, p. 12. 

   - [12] A. S. Bregman. _Auditory Scene Analysis: The Perceptual Organization of Sound_ . MIT press, 1994. 

   - [13] E. Cambouropoulos. “Voice And Stream: Perceptual And Computational Modeling Of Voice Separation”. In: _Music Perception_ 26.1 (Sept. 1, 2008), pp. 75–94. DOI: `10.1525/mp.2008.26.1.75` . 

   - [14] F. Lerdahl and R. S. Jackendoff. _A Generative Theory of Tonal Music_ . MIT press, 1985. 

   - [15] M. Rohrmeier. “Towards a Generative Syntax of Tonal Harmony”. In: _Journal of Mathematics and Music_ 5.1 (Mar. 1, 2011), pp. 35–53. DOI: `10.1080/ 17459737.2011.573676` . 

   - [16] H. Schenker. _Free Composition:(Der Freie Satz): Heinrich Schenker; Translated and Edited by Ernst Oster_ . Longman, 1979. 

   - [17] C. Finkensiep, R. Widdess, and M. Rohrmeier. “Modelling the Syntax of North Indian Melodies with a Generalized Graph Grammar”. In: _Proceedings of the 20th International Society for Music Information Retrieval Conference_ (Delft, The Netherlands). Delft, The Netherlands: ISMIR, Nov. 4, 2019, pp. 462–469. DOI: `10 . 5281 / zenodo . 3527844` . 

   - [18] R. E. Frankel, S. J. Rosenschein, and S. W. Smoliar. “Schenker’s Theory of Tonal Music—Its Explication through Computational Processes”. In: _International Journal of Man-Machine Studies_ 10.2 (Mar. 1, 1978), pp. 121–138. DOI: `10.1016/S00207373(78)80008-X` . 

   - [19] S. W. Smoliar. “A Computer Aid for Schenkerian Analysis”. In: _Proceedings of the 1979 Annual Conference_ . ACM ’79. New York, NY, USA: ACM, 1979, pp. 110–115. DOI: `10.1145/800177.810043` . 

   - [20] J. Rahn. “Logic, Set Theory, Music Theory”. In: _College Music Symposium_ 19.1 (1979), pp. 114– 127. 

   - [21] P. B. Kirlin and P. E. Utgoff. “A Framework for Automated Schenkerian Analysis”. In: (2008), p. 6. 

   - [22] P. B. Kirlin and J. Yust. “Analysis of Analysis: Using Machine Learning to Evaluate the Importance of Music Parameters for Schenkerian Analysis”. In: _Journal of Mathematics and Music_ 10.2 (May 3, 2016), pp. 127–148. DOI: `10 . 1080 / 17459737 . 2016.1209588` . 

- [9] D. Temperley. “A Unified Probabilistic Model for Polyphonic Music Analysis”. In: _Journal of New Music Research_ 38.1 (Mar. 1, 2009), pp. 3–18. DOI: `10.1080/09298210902928495` . 

195 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

- [23] P. B. Kirlin and D. D. Jensen. “Probabilistic Modeling of Hierarchical Music Analysis.” In: _Proceedings of the 12th International Society for Music Information Retrieval Conference_ . 12th International Society for Music Information Retrieval Conference (ISMIR 2011). 2011, pp. 393–398. 

- [24] P. B. Kirlin and D. L. Thomas. “Extending a Model of Monophonic Hierarchical Music Analysis to Homophony”. In: _Proceedings of the 16th International Society for Music Information Retrieval Conference, ISMIR 2015, Málaga, Spain, October 2630, 2015_ . Ed. by M. Müller and F. Wiering. 2015, pp. 715–721. 

- [25] J. D. Yust. “Formal Models of Prolongation”. University of Washington, 2006. 

- [26] A. Marsden. “Representing Melodic Patterns as Networks of Elaborations”. In: _Computers and the Humanities_ 35.1 (Feb. 1, 2001), pp. 37–54. DOI: `10.1023/A:1002705506386` . 

- [27] A. Marsden. “Schenkerian Analysis by Computer: A Proof of Concept”. In: _Journal of New Music Research_ 39.3 (Sept. 1, 2010), pp. 269–289. DOI: `10. 1080/09298215.2010.503898` . 

- [28] D. Harasim, M. Rohrmeier, and T. J. O’Donnell. “A Generalized Parsing Framework for Generative Models of Harmonic Syntax”. In: _Proceedings of the 19th International Society for Music Information Retrieval Conference, ISMIR 2018, Paris, France, September 23-27, 2018_ . Ed. by E. Gómez, X. Hu, E. Humphrey, and E. Benetos. 2018, pp. 152–159. 

- [29] D. Harasim, T. J. O’Donnell, and M. A. Rohrmeier. “Harmonic Syntax in Time: Rhythm Improves Grammatical Models of Harmony”. In: _Proceedings of the 20th ISMIR Conference_ . 20th International Society for Music Information Retrieval Conference. CONF. ISMIR, 2019, p. 335. DOI: `10 . 5281/zenodo.3527812` . 

   - [33] O. Melkonian. “Music as Language: Putting Probabilistic Temporal Graph Grammars to Good Use”. In: _Proceedings of the 7th ACM SIGPLAN International Workshop on Functional Art, Music, Modeling, and Design_ . FARM 2019. Berlin, Germany: Association for Computing Machinery, Aug. 23, 2019, pp. 1–10. DOI: `10.1145/3331543.3342576` . 

   - [34] W. Chi, P. Kumar, S. Yaddanapudi, S. Rahul, and U. Isik. “Generating Music with a Self-Correcting Non-Chronological Autoregressive Model”. In: _Proceedings of the 21st International Society for Music Information Retrieval Conference_ . International Society for Music Information Retrieval Conference (ISMIR 2020). Montreal, Canada: ISMIR, Oct. 11, 2020, pp. 893–900. DOI: `10 . 5281 / zenodo.4245578` . 

   - [35] Z. Wang, D. Wang, Y. Zhang, and G. Xia. “Learning Interpretable Representation for Controllable Polyphonic Music Generation”. In: _Proceedings of the 21st International Society for Music Information Retrieval Conference_ . International Society for Music Information Retrieval Conference (ISMIR 2020). Montreal, Canada: ISMIR, Oct. 11, 2020, pp. 662–669. DOI: `10.5281/zenodo.4245518` . 

   - [36] Z. Wang, Y. Zhang, Y. Zhang, J. Jiang, R. Yang, G. Xia, and J. Zhao. “PianoTree VAE: Structured Representation Learning for Polyphonic Music”. In: _Proceedings of the 21st International Society for Music Information Retrieval Conference_ . International Society for Music Information Retrieval Conference (ISMIR 2020). Montreal, Canada: ISMIR, Oct. 11, 2020, pp. 368–375. DOI: `10.5281/ zenodo.4245446` . 

   - [37] A. Cadwallader and D. Gagné. _Analysis of Tonal Music: A Schenkerian Approach_ . Third Edition. Oxford, New York: Oxford University Press, Mar. 24, 2011. 432 pp. 

- [30] É. Gilbert and D. Conklin. “A Probabilistic ContextFree Grammar for Melodic Reduction”. In: _International Workshop on Artificial Intelligence and Music, IJCAI-07_ . 2007. 

- [31] M. Granroth-Wilding and M. Steedman. “A Robust Parser-Interpreter for Jazz Chord Sequences”. In: _Journal of New Music Research_ 43.4 (Oct. 2, 2014), pp. 355–374. DOI: `10 . 1080 / 09298215 . 2014 . 910532` . 

- [32] S. Abdallah, N. Gold, and A. Marsden. “Analysing Symbolic Music with Probabilistic Grammars”. In: _Computational Music Analysis_ . Ed. by D. Meredith. Cham: Springer International Publishing, 2016, pp. 157–189. DOI: `10.1007/978-3-319-259314_7` . 

196 

