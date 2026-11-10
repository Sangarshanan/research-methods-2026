---
paper_id: "000071"
year: 2021
title: "A Formal Model of Extended Tonal Harmony 569-578"
source_url: "https://archives.ismir.net/ismir2021/paper/000071.pdf"
---

# **A FORMAL MODEL OF EXTENDED TONAL HARMONY** 

**Martin Rohrmeier** 

Digital and Cognitive Musicology Lab, EPFL 

martin.rohrmeier@epfl.ch 

## **Fabian C. Moss** 

Digital and Cognitive Musicology Lab, EPFL fabian.moss@epfl.ch 

### **ABSTRACT** 

Extended tonality is a central system that characterizes the music from the 19th up to the 21st century, including styles like popular music, film music or Jazz. Developing from classical major-minor tonality, the harmonic language of extended tonality forms its own set of rules and regularities, which are a result of the freer combinatoriality of chords within phrases, non-standard chord forms, the emancipation of dissonance, and the loosening of the concept of key. These phenomena posit a challenge for formal, mathematical theory building. The theoretical model proposed in this paper proceeds from Neo-Riemannian and Tonfeld theory, a systematic but informal music-theoretical framework for extended tonality. Our model brings together three fundamental components: the underlying algebraic structure of the Tonnetz, the three basic analytical categories from Tonfeld theory (octatonic and hexatonic collections as well as stacks of fifths), and harmonic syntax in terms of formal language theory. The proposed model is specified to a level of detail that lends itself for implementation and empirical investigation. 

### **1. INTRODUCTION** 

Harmony is a central latent structure governing Western music since centuries until today [1]. While a considerable amount of research has focused on theoretical, mathematical, and computational exploration of harmony in common-practice major-minor tonality, comparably less attention has been devoted to the challenges that come with the paradigm shift of extended tonality, as it is in place since the 19th century up until the present day in various styles like Jazz, popular or film music. 

Extended tonality exhibits harmonic sequences that defy the logic of common-practice (major-minor) tonality. In this paper, we address the problem of accounting for such phenomena with a grammar approach that bridges formal language theory and (mathematical) music theory. 

### **1.1 The Challenge of Extended Tonality** 

Briefly construed, harmonic progressions in pieces in diatonic common-practice tonality involve chords that are 

> © M. Rohrmeier and F. C. Moss. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). **Attribution:** M. Rohrmeier and F. C. Moss, “A Formal Model of Extended Tonal Harmony ”, in _Proc. of the 22nd Int. Society for Music Information Retrieval Conf.,_ Online, 2021. 

mostly stacks of thirds derived from the seven diatonic degrees of major or minor scales. Larger harmonic structures emerge through modulations between different keys that are usually close to one another on the line of fifths [1–4], thus forming a system that governs the global hierarchy of pieces [5–9]. 

In contrast, pieces employing extended tonality may rely on a variety of different scales (e.g., pentatonic, hexatonic, and octatonic scales; see Section 2), freely use harmonies that are not necessarily construed by stacking diatonic thirds, and modulate to or immediately combine chords from relatively distant keys [10–13]. For example, late-Romantic pieces often distinguish themselves from earlier diatonic ones by featuring frequent enharmonic exchanges of pitches, resulting in uncommon chord combinations [14–16], and by the frequent usage of symmetrical scales that impede a listener’s orientation towards a unique tonic, possibly resulting in multiple parallel tonal centers [17,18]. 

However, extended tonality is not restricted to late 19th-century pieces, but reaches into many more recent styles, in particular in Jazz with its highly chromatic harmonies [19, 20], and film music, such as scores by Korngold or Williams [21–24]. It also plays a role in Rock and Pop [25–27], and minimalist music, such as by Glass, Frahm or Richter. Extended tonality thus describes not a historical time span but rather captures characteristic features of a harmonic language that extends commonpractice major-minor tonality with a variety of phenomena reaching from the late 18th century until the present day [28]. 

### **1.2 Related Work** 

### _1.2.1 The Tonnetz and Neo-Riemannian Theory_ 

A major analytical approach to extended tonality is neoRiemannian theory (NRT), which models harmonic progressions between pairs of triads or keys through parsimonious voice-leading transformations [16, 29, 30]. For instance, the _relative_ transformation _R_ converts C major into A minor, the _parallel_ transformation _P_ converts C major into C minor, and the _leading-tone exchange_ transforms C major into E minor. All transformations are involutions, i.e. they are self-inverse. Repeated application of (combinations of) NRT transformations leads to patterns on the _Tonnetz_ (Section 2.1) that visualize a particular analysis. 

Figure 1 shows an excerpt of the Tonnetz. Note that the alternation of _P_ and _R_ transformations creates a pattern 

569 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

on the Tonnetz that covers all pitches from an octatonic scale (shown in blue), the alternation of _P_ and _L_ transformations creates a path on the Tonnetz that contains all members of a hexatonic scale (shown in orange), and combinations of _R_ and _L_ transformations generate a sequence of triads that modulates through all diatonic scales (not shown; the diatonic is encompassed by a horizontal line of six fifths or two adjacent horizontal lines connecting 6 triangles ). The green rectangle delineates a stack of fifths (see below). Due to its focus on triadic transformations, and in particular those that form hexatonic or octatonic cycles, NRT analyses are commonly restricted such that the assumed algebraic spaces imposes some inflexibility with regard to the chord form. Further, stacks of fifths (see below) are commonly not addressed in NRT. Also, though some analyses work with reductions and abstractions from the score, there is no formalized theory of harmonic hierarchy in NRT. In further work, mathematical spaces have been extended or generalized [31–33], used in computational models of harmony or tonality [34–38], or explored empirically [39–42]. 

### _1.2.2 Tonfeld Theory_ 

Another recent theory addressing the challenges of extended tonality is Tonfeld theory (TFT) [43–49]. Unlike NRT, it does not fundamentally rely on triads or keys. Instead, it departs directly from three so-called _Tonfelder_ (‘tone fields’) that correspond to hexatonic, octatonic, and fifths-related (e.g., pentatonic, diatonic) tone collections (see Section 2.2 for details) that are assumed to govern segments of pieces at the granularity of the pitch level. It mostly focuses on late 19th-century compositions but some analyses for 18th and 20th century pieces exist as well [28,50,51]. Moreover, TFT subscribes to a fundamentally hierarchical conception of compositions by analyzing a piece’s tonal coherence through the presence and interactions of Tonfelder on several structural levels of abstraction/reduction. This allows in principle for the expression of nested structures and non-local dependencies. 

### _1.2.3 Harmonic Syntax_ 

Syntactic formalisms derive musical (e.g. harmonic or melodic) sequences through generative models that result in trees or similar hierarchical dependency structures [6, 52–57]. They frequently adopt frameworks from formal language theory and adapt them to the particular needs for the case of music. In recent years, several formal and computational approaches have been developed for Western classical music [7, 58, 59], Blues [60, 61], Jazz [20, 62–65]. We build on such previous approaches and expand their scope to extended tonality. 

Accordingly, every just interval can be expressed by a frequency ratio: 



<!-- Start of picture text -->
f 1 /f 2 = 2 x ·  3 y ·  5 z , x, y, z ∈ Z . (1)<br><!-- End of picture text -->

Since the factor 2 defines the octave, the two other integer factors _y_ and _z_ span a coordinate system of pitch classes (modulo the octave) that defines an infinite plane of fifths and major thirds. Taking into account that a fifth is composed of a major and a minor third, the plane corresponds to a triangular graph such that there are three main axes of major, minor thirds and fifths, in which each triangle defines a major or minor triad (see Figure 1). 



<!-- Start of picture text -->
A ♯ E ♯ B ♯ F ♯♯ C ♯♯ G ♯ ♯<br>F ♯ C ♯ G ♯ D ♯ A ♯ E ♯<br>A E B F ♯ C ♯ G ♯<br>F C G D A E<br>A ♭ E ♭ B ♭ F C G<br><!-- End of picture text -->

**Figure 1** : The Tonnetz and the construction of the three types of _Tonfeld_ structures. The pitch class set shaded in blue defines one octatonic, the set shaded in orange defines one hexatonic, the set in green defines a stack of fifths. 

The Tonnetz defines an _infinite_ space of spelled pitch classes none of which are identical, i.e. different nodes in the graph with the same label are indeed distinct. If one identifies nodes with the same labels, the infinite line of fifths wraps itself around the so-called _Spiral Array_ [37]. If, further, enharmonic equivalence is assumed (e.g. _D♯ ≡ E♭_ ), the space becomes a torus [39, 68] and the resulting pitch-class space is isomorphic to Z12. 

### **2.2 The Tonfelder** 

Tonfeld theory comprises three fundamental concepts that are expressed in terms of pitch collections: octatonic, hexatonic, and stacks of fifths. This section introduces these building blocks that the theory operates on. All concepts are formulated in the toroidal Z12 pitch space, yet they could be easily generalized to the spelled pitch space and the infinite Tonnetz. At first, a stack of intervals _SI_ is defined by a starting pitch _p_ , and an interval _i_ with _k_ iterations. If the iterations reach the starting pitch, _SI_ defines a cyclic group (simply written as _SI p,i_ ).<sup>1</sup> 



<!-- Start of picture text -->
SI p,i,k :=  {p  +  im | m ≤ k ;  k, m ∈ N0 } (2)<br><!-- End of picture text -->

### **2. THE MODEL** 

### **2.1 The Tonnetz** 

One foundation of the present model is the _Tonnetz_ . It goes back to Leonard Euler’s definition of intervals in just intonation [66], leading to an abstract pitch class space [67]. 

Interval cycles are musically meaningful units to ground a tonal theory [69, 70]. Here, the three Tonfelder are constructed from the three directions in the Tonnetz. The _octatonic_ is defined by shifting a fifth along the axis of minor 

1 An analogous definition in the infinite Tonnetz space would not result in a cyclic group. 

570 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

thirds, the _hexatonic_ by shifting a fifth along the axis of major thirds, and the _stack of fifths_ by collecting consecutive fifths along the axis of fifths (see Figure 1). 

_Oct p_ := _{i, i_ + 7 _| i ∈ SI p,_ 3 _} ≡ SI p,_ 3 _⊎ SI p_ +7 _,_ 3 (3) _Hex p_ := _{i, i_ + 7 _| i ∈ SI p,_ 4 _} ≡ SI p,_ 4 _⊎ SI p_ +7 _,_ 4 (4) _Fif p,k_ := _SI p,_ 7 _,k_ (5) 

Notably, all three Tonfelder are based on the foundational tonal interval of the fifth. This construction results in the three different octatonic (halftone–wholetone) scales and the four hexatonic (minor-third–halftone) scales ( _Oct i_ = _Oct i_ +3; _Hex i_ = _Hex i_ +4): 



<!-- Start of picture text -->
Oct 0 = {C, D♭, E♭, E♮, G♭, G♮, A, B♭} (6)<br>Oct 1 = {D♭, D, E♮, F, G, A♭, B♭, C♭} (7)<br>Oct 2 = {C, D, E♭, F, G♭, A♭, A♮, B} (8)<br>Hex  0 = {C, E♭, E, G, A♭, B} (9)<br><!-- End of picture text -->



<!-- Start of picture text -->
Hex  1 = {C♯, E, F, G♯, A, C} (10)<br><!-- End of picture text -->



<!-- Start of picture text -->
Hex  2 = {D, F, F♯, A, B♭, C♯} (11)<br><!-- End of picture text -->



<!-- Start of picture text -->
Hex  3 = {E♭, F♯, G, B♭, B♮, D} (12)<br><!-- End of picture text -->

Since stacks of fifths do not form a mode of limited transposition [71], there are 12 different types of stacks of fifths until the whole chromatic is reached. 



<!-- Start of picture text -->
=<br>Fif C, 2 {C, G, D} (13)<br><!-- End of picture text -->

such as the “Tristan chord”, the “Petrouchka chord”, Scriabin’s “mystical chord” as well as many upper structure chords in Jazz (e.g. _G_ - _F_ - _B_ - _D_ - _E_ - _G♯_ - _B_ ) [75], are captured within the octatonic set. Non-diatonic minor chords with major sevenths as they occur in Jazz are captured by the hexatonic set. The set of all chords derived by suitable filters (for the particular surface to be modeled) from a Tonfeld _t ∈_ T is denoted by _Ct_ . This definition encompasses occurrences of non-standard chord forms, such as the ones above. 

Tonfelder further bear generalizing expressive power with respect to central tonal relations. The set of chords with a dominant function may, for instance, involve _V_ , _V_<sup>7</sup> , _vii_<sup>0</sup> , _♭VII_ , _♭II_<sup>_7_</sup> (tritone substitution), or _III_<sup>7</sup> . Similar, subdomantic/pre-dominantic chords may, e.g., involve, _IV_ , _ii_ , _II_ , _iv_<sup>6</sup> , _♭VI_ . Both of these sets of equivalences are all encompassed by the set of chords from the two octatonics neighboring the reference tonic chord [44, 70]. Therefore, the octatonic Tonfeld can be understood as a generalization over the concept of tonal harmonic function (tonic, dominant, predominant) as well as intra-functional prolongation/substitution (within the same octatonic). 

Conversely, Neo-Riemannian theories (as well as TFT) have identified chords from the hexatonic to establish contrastive relationships, such as the hexatonic pole (e.g., _C_ major – _A♭_ minor), [14, 76]. Such relations between harmonies are the basis of the hierarchical dependencies that are modelled by the grammar outlined in the next subsection. 



<!-- Start of picture text -->
=<br>Fif C, 3 {C, G, D, A} (14)<br><!-- End of picture text -->



<!-- Start of picture text -->
=<br>. . . Fif C, 5 {C, G, D, A, E, B} (15)<br><!-- End of picture text -->

The set of all Tonfelder T is defined as T := _{Oct_ 0 _, Oct_ 1 _, Oct_ 2 _} ∪{Hex_ 0 _, . . . , Hex_ 3 _} ∪{Fif p,k | p ∈_ 0 _, . . . ,_ 11 _, k ∈_ 2 _, . . . ,_ 10 _}_ . One can apply _filters_ to a Tonfeld _t_ to arrive at basic musical units, such as triads or tetrads. For instance, all triads in a Tonfeld are filtered out by 

_f_ : _t �→{{a, b, c} | iv_ ( _{a, b, c}_ ) = (0 _,_ 0 _,_ 1 _,_ 1 _,_ 1 _,_ 0) _}_ (16) 

where _iv_ is the interval vector of a given pitch-class set, which counts all possible interval classes [72]. One can easily define filters for other chord types or, in fact, arbitrary pitch-class sets [72,73]. 

In terms of common chord types, the octatonic scale yields four major, minor, dominant seventh, minor seventh and half-diminished chords each, all related by minor thirds, and two fully diminished tetrads a fifth/a semitone apart. The hexatonic scale in turn yields three major, minor, major seventh, minor-major-seventh chords a major third apart, and two augmented triads a fifth/a semitone apart. Stacks of fifths yield chords that are often classified as _sus_ -chords or quartal voicings in Jazz harmony terminology,<sup>2</sup> and also cover complex add 6, 9th or 11th chords as they appear in Jazz [74]. Notably, also complex chords 

> 2 The stack of fifths chords (e.g. _C − G − D_ ) are technically not suspension chords since they do commonly not imply a resolution of the dissonant fourth into a third as in standard common-practice. [3] 

### **2.3 The Grammar** 

The proposed harmonic grammar formalism is based on abstract context-free grammars (ACFGs) [63] and extends previous models of harmonic syntax [7,20,58]. It consists of four components: _G_ = ( _K,_ Σ _, P, s_ ), non-terminal categories _K_ , terminal symbols Σ, production rules _P_ , and a start symbol _s ∈ K_ . The set of all terminals Σ encompasses all (potentially non-standard) chords derived from the Tonfelder: Σ := _{c | c ∈ Ct ∀t ∈_ T _}_ . 

There are three kinds of non-terminal category symbols: _K_ = _{s} ∪{_ Θ _t | t ∈_ T _} ∪{ct | c ∈ Ct, t ∈_ T _}_ . _s_ denotes the abstract start symbol. Except for the start symbol, nonterminal category symbols have a feature _t_ , which indicates the assigned Tonfeld of the category. Abstract Tonfeld categories Θ _t_ ( _∈{_ Θ _}×_ T) define an unspecific Tonfeld _t ∈_ T that has not yet been instantiated in terms of a concrete chord category. Chord categories _ct_ ( _∈_ Σ _×_ T) are defined in terms of any chord symbol _c_ derived from its assigned Tonfeld _t_ . 

In ACFGs, the production rules _P_ are defined as functions mapping the left-hand side to the right-hand side. Here, _P_ involves three kinds of rules: general rules ( _start_ , _instantiation_ , _Tonfeld cast_ , _termination_ ), rules characterizing hierarchical functional relations ( _prolongation_ , ( _substitution_ ), _preparation_ , _plagal dependency_ , _contrast_ ), and rules with set operations for manipulating stacks of fifths ( _fifth shift_ , _fifth expansion & contraction_ , _fifth split_ ). Notably, it is not necessary to formally assume substitution 

571 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

because substitutable equivalences are already expressed at the level of the octatonic Tonfeld. The following paragraphs define each rule type: 

### _2.3.1 General Rules_ 

**Start.** A piece is modeled as a sequence of different Tonfeld categories Θ. 



<!-- Start of picture text -->
s −→ Θ (1) t 1 . . . Θ ( tn n ) (17)<br><!-- End of picture text -->

Note that in contrast to previous (diatonic) syntax theories [7], there is no requirement of an overarching single tonic node of a derivation tree (although this ‘downward compatability’ can be achieved by a single overarching octatonic chord category). This comes from the different logic of Tonfeld structures [28,44]. Thus, the top level may consist in a sequence of different Tonfelder. For abridged derivations or analyses of partial sequences, the trees can also directly be headed by a single Tonfeld or chord category, omitting the start symbol (see the examples below). **Tonfeld instantiation.** An abstract Tonfeld symbol Θ _t_ of the Tonfeld _t_ may be instantiated with one or more member chords from its set. 



<!-- Start of picture text -->
Θ t −→ Yt (1) . . . Yt ( n ) (18)<br><!-- End of picture text -->

**Tonfeld casting.** Generalizing modulations, a chord category can change its underlying Tonfeld and recursively yield different generations. Importantly, this operation can only be performed over chord categories, since the abstract Tonfeld categories are ambiguous with regard to their chord instantiation, and therefore their cast to a different Tonfeld is not well-defined. An abstract Tonfeld category can only be cast into another through _instantiation_ in terms of a pivot chord category. Therefore, Tonfeld casting necessarily involves the set intersection of two Tonfelder (which in turn enforces the chord type category for _X_ ). 



<!-- Start of picture text -->
Xm −→ Xk, X ∈ Cm ∩ Ck (19)<br><!-- End of picture text -->

**Terminal rules.** The grammar needs to ensure that the sequence generation terminates. The production can terminate when there are no more abstract categories in the sequence. Since chord categories are already absolute chords matching surface chord forms, the only final step is to cast the chord category into a terminal chord without a Tonfeld feature: _Xt −→ X_ . For stacks of fifths, the resulting chord forms may be non-standard, e.g. non-triadic (see Figure 6). 

### _2.3.2 Rules for functional relations_ 

**Prolongation.** Going beyond previous models [7,20], prolongation need not only combine identical categories but may combine elements of the same Tonfeld. Following the generalization by Steedman, prolongation can be understood as an instance of syntactic coordination [62, 77]. Prolongation can be established with two different types, abstract Tonfeld categories and chord categories, and may combine two or more categories. 

**(Substitution.)** The octatonic moreover generalizes over possible substitutions of certain sets of chords. It is useful to formulate this as a rule even though, in most cases, the direct derivation of dominant or subdominant substitutions may be achieved directly though the preparation- and plagal-dependency rules (and therefore, the rule may not be necessary in computational implementations). 



<!-- Start of picture text -->
XOct a −→ YOct a , X̸ =  Y (22)<br><!-- End of picture text -->

**Preparation.** The octatonic generalizes over the class of chords that may prepare other chords [20]. Since there are only three different octatonics (3) there are only two possible preparations (motions between them): preparation and plagal dependency (see below). A preparation is derived as the preceding left child of the prepared chord. The types of _X_ and _Y_ can be an abstract octatonic Tonfeld Θ _Oct a_ or a chord category _ct_ . 



<!-- Start of picture text -->
XOct a −→ YOct a +1  XOct a (23)<br><!-- End of picture text -->

**Plagal dependency.** The octatonic also generalizes over the set of subdominants. A plagal dependency/relaxation into a chord is modeled as its left child. Although the plagal relaxation has a similar form as the preparation rule, its semantics is different. This implies that the semantic of the applied dependency type (preparation or plagal) cannot be inferred from its shape in the tree (i.e. a left child is not necessarily a dominant – pace GTTM [6]). Similarly to the preparation rule, the types of _X_ and _Y_ can either be both abstract octatonic Tonfelder or chord categories. 



<!-- Start of picture text -->
XOct a −→ YOct a− 1  XOct a (24)<br><!-- End of picture text -->

**Contrast.** The hexatonic and the stack of fifths allow for the instantiation of the relation of a contrast to a given element. For the hexatonic, contrast is established _within_ the same hexatonic. The most frequent form of the hexatonic contrast is the _hexatonic pole_ [78]. For the stack of fifths, contrast is established between two quasi-complementary stacks of fifths ( _fifth flipover_ ). 



<!-- Start of picture text -->
XHex i −→ YHex i XHex i , X̸ =  Y (25)<br>XHex i −→ XHex i YHex i , X̸ =  Y (26)<br>Θ Fif a,b −→ Θ Fif c,d Θ Fif a,b , if  inv ( Fif a,b, Fif c,d ) (27)<br>Θ Fif a,b −→ Θ Fif a,b Θ Fif c,d , if  inv ( Fif a,b, Fif c,d ) (28)<br><!-- End of picture text -->

The Boolean _inverse_ relation _inv_ between two stacks of fifths _Fif p,k_ and _Fif q,l_ is fulfilled if they are sufficiently distinct for some distance function _d_ and threshold _δ_ (29). Since the stacks are sets, a suitable candidate is the Jaccard distance (30). 



<!-- Start of picture text -->
inv ( Fif p,k, Fif q,l ) := d ( Fif p,k, Fif q,l )  ≤ δ (29)<br>|A ∩ B|<br>d ( A, B ) := (30)<br>|A ∪ B|<br><!-- End of picture text -->

### _2.3.3 Rules for Stacks of Fifths_ 



<!-- Start of picture text -->
Θ t → Θ t . . . Θ t (20)<br>Xt → Yt (1) . . . Yt ( n ) , Xt = Θ t ∨∃i  :  Y ( i ) =  X (21)<br><!-- End of picture text -->

**Fifth shift.** A stack of fifths can be shifted one step in either direction of the circle of fifths. The rule can instantiate 

572 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

an instance before or after the parent category. 



<!-- Start of picture text -->
Θ Fif p,k −→ Θ Fif p,k Θ Fif p± 7 ,k (31)<br><!-- End of picture text -->



<!-- Start of picture text -->
Θ Fif p,k −→ Θ Fif p± 7 ,k Θ Fif p,k (32)<br><!-- End of picture text -->

**Fifth expansion and contraction.** A stack of fifths can be extended or reduced by a number of fifths. This results in a stack of fifths with a different number _m_ of fifths, respecting the defining criterion of a stack of fifths of 2 _< m <_ 11. Fifth expansion and contraction may propagate to the left or the right within the sequence. 



<!-- Start of picture text -->
Θ Fif p,k −→ Θ Fif p,k Θ Fif p,m , m̸  =  k (33)<br>Θ Fif p,k −→ Θ Fif p,m Θ Fif p,k , m̸  =  k (34)<br><!-- End of picture text -->

**Fifth split.** A stack of fifths can be split into two different, potentially overlapping, stacks of fifths. 



<!-- Start of picture text -->
Θ Fif p,k −→ Θ Fif q,l Θ Fif r,m , Fif q,l ∪ Fif r,m =  Fif p,k (35)<br><!-- End of picture text -->

### **3. EXAMPLES** 

Figure 2 illustrates how the use of the octatonic generalizes over remote variants of authentic preparation progressions or cadences, without requiring modulation, borrowing, tritone substitutions, or chromatic operations. 



<!-- Start of picture text -->
COct 0 COct 0 COct 0<br>Θ Oct 1 C Θ Oct 1 C Θ Oct 1 C<br>Θ Oct 2 Θ Oct 1 Θ Oct 2 Θ Oct 1 Θ Oct 2 Θ Oct 1<br>Θ Oct 0 Θ Oct 2 G 7 Θ Oct 0 Θ Oct 2 D♭ 7 Θ Oct 0 Θ Oct 2 B♭<br>Am D 7 E♭ 7 D 7 E♭ 7 A♭<br><!-- End of picture text -->

**Figure 2** : Generalizing over 3 preparatory progressions. 

One example that well illustrates the octatonic set is given by two phrases from the second movement of Antonin Dvoˇrák’s ninth Symphony (Figure 3). It illustrates (a) that the chords used in sequence defy a purely diatonic (e.g. D _♭_ major) analysis, thus requiring a different analytical framework, and (b) that the two excerpts sound very similar even though they use different and remote chords at the surface. Our analysis illuminates that the chords stem from two octatonic Tonfelder which are identical for both examples. The very similar impression of both excerpts is modeled by the identical deep structure of the tree derivations. Further octatonic examples include Schubert’s _Ganymed_ D544 and Scriabin’s _Prelude_ op. 74/2. 

One paradigmatic example for hexatonic Tonfelder is John Coltrane’s piece “Giant Steps” (Figure 5). Similarly to the previous example, the chord sequence here also defies diatonic derivations because of the overarching majorthird relations of the harmonic centers _B_ major, _G_ major and _E♭_ major. Notably, the piece abandons the sense of an overarching key, osciallating between the harmonic centers establishing an overarching _abstract_ hexatonic Tonfeld instead. The tree analysis demonstrates that the chord sequence is simple to derive once hexatonic relations are assumed at the top level. The local _ii −V −I_ progressions are 



<!-- Start of picture text -->
D♭Oct 1<br>D♭Oct 1 D♭Oct 1<br>EOct 1 B♭Oct 1 EOct 1 D♭Oct 1 Θ Oct 0 D♭Oct 1<br>E B♭ E D♭ AOct 0 F♯mOct 0 F♯m 6 Oct 0 D♭<br>A F♯m F♯m 6<br><!-- End of picture text -->





<!-- Start of picture text -->
D♭Oct 1<br>D♭Oct 1 D♭Oct 1<br>D♭Oct 1 GOct 1 D♭Oct 1 B♭Oct 1 Θ Oct 0 D♭Oct 1<br>D♭ G D♭ B♭ G♭Oct 0 E♭mOct 0 E♭m 6 Oct 0 D♭<br>G♭ E♭m E♭m 6<br><!-- End of picture text -->



**Figure 3** : Dvoˇrák, Symphony IX, op. 95–II, mm. 22-25, mm. 120-123 



<!-- Start of picture text -->
Θ Hex 0<br>A♭Hex 0 EHex 0 A♭mHex 0 EHex 0<br>A♭ E A♭m E<br><!-- End of picture text -->



**Figure 4** : Chord progression for Aragorn and Arwen’s love scene from _Lord of the Rings_ (Howard Shore). 

well-modeled with octatonic preparatory relations. Thus, this example also illustrates a case of hierarchical intertwining of two different types of Tonfelder. 

Another example for a hexatonic progression is taken from Howard Shore’s score to the film _Lord of the Rings_ for the scene in which the characters Aragorn and Arwen, a couple that embodies contrast (human/mortal vs. elf/immortal), engage in intimate conversation. Underlying this scene is a loop of the chord progression _A♭ − E − A♭m − E_ . Similar to the octatonic example above, these chords can not be subsumed under a single key and an analysis where each chord change entails a key modulation seems implausible. Rather, these chords are all taken from the hexatonic Tonfeld _Hex_ 0, as shown by the analysis in Figure 4. Not all triads possible in this Tonfeld do occur but the sequence expresses all pitch classes from _Hex_ 0, except _G_ . Further hexatonic examples can be found 

573 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 



<!-- Start of picture text -->
Θ Hex 3<br>Θ Hex 3 Θ Hex 3<br>Θ Hex 3 Θ Hex 3 E♭Hex 3 GHex 3 BHex 3 E♭Hex 3<br>BHex 3 GHex 3 E♭Hex 3 GHex 3 E♭Hex 3 BHex 3 E♭Oct 0 GOct 1 BOct 2 E♭Oct 0<br>GOct 1 E♭Oct 0 GOct 1 E♭Oct 0 BOct 2 B♭ 7 Oct 1 E♭Oct 0 DOct 7 2 GOct 1 F♯ 7 Oct 0 BOct 2 B♭ 7 Oct 1 E♭Oct 0<br>DOct 7 2 GOct 1 B♭ 7 Oct 1 E♭Oct 0 DOct 7 2 GOct 1 B♭ 7 Oct 1 E♭Oct 0 F♯ 7 Oct 0 BOct 2 Fm 7 Oct 2 B♭ 7 Oct 1 AmOct 0 DOct 7 2 C♯mOct 1 F♯ 7 Oct 0 FmOct 2 B♭ 7 Oct 1<br>Am 7 Oct 0 DOct 7 2<br>B D 7 G B♭ 7 E♭ Am 7 D 7 G B♭ 7 E♭ F♯ 7 B Fm 7 B♭ 7 E♭ Am D 7 G C♯m F♯ 7 B Fm B♭ 7 E♭<br>B D G B♭ E♭ A- D G B♭ E♭ F♯ B F- B♭ E♭ A- D G C♯- F♯ B F- B♭ E♭ C♯- F♯<br>                                         <br><!-- End of picture text -->

**Figure 5** : John Coltrane’s “Giant Steps”. The three harmonic centers _B_ , _G_ , _E♭_ span a complete hexatonic _Hex_ 3. 

in the prelude of Wagner’s _Parsifal_ and Bruckner’s _Ecce Sacerdos Magnus_ WAB 13. As shown in [25], octatonic and hexatonic structures occur frequently in Popular music, e.g. _Shake the Disease_ by Depeche Mode, _Easy Meat_ by Frank Zappa, _Creep_ by Radiohead, or _Lay, Lady, Lay_ by Bob Dylan. 

“Maiden Voyage” by Herbie Hancock provides a good illustration for the use of stacks of fifths (Figure 6). First, none of the _sus_ chords in the leadsheet are proper _suspension_ chords because they do not imply a resolution to an omitted harmonic interval. In fact, they are implicit notations for quartal voicings, which are in fact stacks of fifths. Both chord pairs in both sections constitute a _split_ of an overarching stack of fifths. The relation between both parts is that the overarching _prolonged_ stack of fifths is contrasted by _fifth flipover_ . Other examples for this Tonfeld are Bartók’s _Boating_ from Mikrokosmos V, Tailleferre’s _Pastorale_ , Ligeti’s piano etude no. 8, Kraftwerk’s _Trans Europa Express_ , Zimmer’s film music to _Interstellar_ . 



<!-- Start of picture text -->
Θ Fif E♭, 6<br>Θ Fif E♭, 6 Θ Fif E♭, 6<br>Θ Fif C, 3 Θ Fif E♭, 3 Θ Fif C♭, 5 ( inv ) Θ Fif E♭, 6<br>Θ Fif D♭, 3 Θ Fif C♭, 3 Θ Fif C, 3 Θ Fif E♭, 3<br>D 7 sus 4 F 7 sus 4 E♭ 7 sus 4 D♭ 7 sus 4 D 7 sus 4 F 7 sus 4<br>D��� F��� E♭���<br>1. 2.<br>                      <br>  <br>13 D♭��� D��� F���<br>                     <br><br><!-- End of picture text -->

**Figure 6** : Analyzing Herbie Hancock’s “Maiden Voyage” illustrating operations on stacks of fifths. 

### **4. CONCLUSION** 

We present a model of extended tonality bridging music theoretical accounts and formal grammars. It captures chord forms and chord sequences that are challenging for 

other (diatonic) approaches. While some details, e.g. cases not yet covered, may be subject to debate, we argue that the core innovation and main benefit lies in providing a well-formalized hierarchical model of extended tonal harmony. As an aside, our model offers an explanation why some previous computational models find octatonic and hexatonic structures as efficient structures in their latent space [40,42]. 

Our model is based on three Tonfelder as construed from the Tonnetz and the foundational interval of the perfect fifth, both of which we consider fundamental for extended tonality. We argue that the collections that can be constructed from the Tonnetz have a special status in establishing (extended) tonality compared with the manifold other scales. For instance, the whole-tone scale cannot be directly represented on the Tonnetz, and we argue that it can thus not form a deep structure, despite appearing on the surface. Our model constitutes an extension of formal grammars for diatonic music, meaning that it can also generate purely diatonic sequences, in analogy to extended tonal compositions containing also purely tonal sections. 

The aim of the theory is to not only capture musical surface events but to model the kinds of underlying dependencies with theoretically meaningful concepts and assumptions, i.e. _strong generativity_ [79]. Similarly to previous syntactic theories of music, the latent analytic derivations link _structure_ and _interpretation_ in terms of dependencies and chord functions (e.g. preparation, contrast) [20,80,81]. Because of the expressive richness of the model multiple concurrent analyses are possible for a given sequence. This makes it possible to express diverging hearings and nuances of a passage that different listeners may experience. The theory will not suffice as a forward generative model for computational composition on its own. It would require additional (inferable) style-specific parameters, since extended harmony works differently in Dvoˇrák, Ravel, the Beatles, Coltrane, or Richter, and may as well benefit from a joint model of rhythm [20,82]. The theory is sufficiently well-specified such that it is testable, debatable, and lends itself for empirical investigation in a probabilistic formulation in future work. 

574 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

### **5. ACKNOWLEDGMENTS** 

This project has received funding from the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (GA No 760081), and from the Swiss National Science Foundation (GA No 182811). We thank Claude Latour for supporting this research through the Latour Chair in Digital Musicology. We thank Christoph Finkensiep, Gabriele Cecchetti and Markus Neuwirth for many valuable discussions. 

### **6. REFERENCES** 

- [1] C. Dahlhaus, J. Anderson, C. Wilson, R. Cohn, and B. Hyer, “Harmony,” in _The New Grove Dictionary of Music and Musicians_ , 2nd ed., S. Sadie and J. Tyrrell, Eds. London: Macmillan Publishers, 2001, pp. 858– 877. 

- [2] B. Hyer, “Tonality,” in _The New Grove Dictionary of Music and Musicians_ , 2nd ed., S. Sadie and J. Tyrrell, Eds. London: Macmillan Publishers, 2001, pp. 583– 594. 

- [3] E. Aldwell, C. Schachter, and A. Cadwallader, _Harmony and Voice Leading_ , 4th ed. Cengage Learning, 2010. 

- [4] D. Temperley, “The Line of Fifths,” _Music Analysis_ , vol. 19, no. 3, pp. 289–319, Oct. 2000. 

- [5] H. Schenker, _Der Freie Satz_ . Wien: Universal Edition, 1935. 

- [6] F. Lerdahl and R. S. Jackendoff, _A Generative Theory of Tonal Music_ . Cambridge, MA: MIT Press, 1983. 

- [7] M. Rohrmeier, “Towards a generative syntax of tonal harmony,” _Journal of Mathematics and Music_ , vol. 5, no. 1, pp. 35–53, Mar. 2011. 

- [8] R. Lieck and M. Rohrmeier, “Modelling Hierarchical Key Structure with Pitch Scapes,” in _Proceedings of the 21st International Society for Music Information Retrieval Conference (ISMIR 2020)_ , Montreal, Canada, 2020, pp. 811–818. 

- [9] C. Viaccoz, D. Harasim, F. C. Moss, and M. Rohrmeier, “Wavescapes: A Visual Hierarchical Analysis of Tonality using the Discrete Fourier Transformation,” _Musicae Scientiae_ , accepted. 

- [10] A. Schoenberg, _Structural Functions of Harmony_ , L. Stein, Ed. Faber and Faber, 1969. 

- [11] F. Lerdahl, _Tonal Pitch Space_ . Oxford: Oxford University Press, 2001. 

- [12] D. Harrison, _Harmonic Function in Chromatic Music: A Renewed Dualist Theory and an Account of Its Precedents_ . Chicago and London: University of Chicago Press, 1994. 

- [13] A. T. Katz, _Challenge to Musical Tradition - A New Concept of Tonality_ . New York: Alfred Knopf, 1945. 

- [14] R. Cohn, _Audacious Euphony: Chromatic Harmony and the Triad’s Second Nature_ . Oxford: Oxford University Press, 2012. 

- [15] D. Harrison, “Nonconformist Notions of NineteenthCentury Enharmonicism,” _Music Analysis_ , vol. 21, no. 2, pp. 115–160, 2002. 

- [16] S. Rings, _Tonality and Transformation_ . New York: Oxford University Press, 2011. 

- [17] J. Horton, “Form and Orbital Tonality in the Finale of Bruckner’s Seventh Symphony,” _Music Analysis_ , vol. 37, no. 3, pp. 271–309, Oct. 2018. 

- [18] F. C. Moss, “Tonality and functional equivalence: A multi-level model for the cognition of triadic progressions in 19th century music,” in _International Conference of Students of Systematic Musicology - Proceedings_ , vol. 1, London, 2014, pp. 1–8. 

- [19] D. Terefenko, _Jazz Theory: From Basic to Advanced Study_ . New York: Routledge, 2014. 

- [20] M. Rohrmeier, “The Syntax of Jazz Harmony: Diatonic Tonality, Phrase Structure, and Form,” _Music Theory and Analysis (MTA)_ , vol. 7, no. 1, pp. 1–63, Apr. 2020. 

- [21] F. M. Lehman, “Schubert’s SLIDEs: Tonal (Non-) Integration of a Paradoxical Transformation,” _Music Theory & Analysis_ , vol. 1, no. I & II, pp. 61–100, 2014. 

- [22] E. Heine, “Chromatic Mediants and Narrative Context in Film,” _Music Analysis_ , vol. 37, no. 1, pp. 103–132, 2018. 

- [23] F. Lehman, _Hollywood Harmony: Musical Wonder and the Sound of Cinema_ . Oxford: Oxford University Press, 2018. 

- [24] S. Murphy, “Scoring Loss in Some Recent Popular Film and Television,” _Music Theory Spectrum_ , vol. 36, no. 2, pp. 295–314, 2014. 

- [25] G. Capuzzo, “Neo-Riemannian Theory and the Analysis of Pop-Rock Music,” _Music Theory Spectrum_ , vol. 26, no. 2, pp. 177–200, 2004. 

- [26] D. Temperley, _The Musical Language of Rock_ . Oxford: Oxford University Press, Feb. 2018. 

- [27] N. Biamonte, “Triadic Modal and Pentatonic Patterns in Rock Music,” _Music Theory Spectrum_ , vol. 32, no. 2, pp. 95–110, Oct. 2010. 

- [28] B. Haas, “Zur Sonatenform II mit analytischen Bemerkungen zum ersten Satz von Mozarts Sonate KV 570,” in _Funktionale Analyse: Music - Malerei - Antike Literatur_ , B. Haas and B. Haas, Eds. Hildesheim, Zürich, New York: Olms, 2010, pp. 261–291. 

575 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

- [29] R. Cohn, “Neo-riemannian operations, parsimonious trichords, and their "Tonnetz" representations,” _Journal of Music Theory_ , vol. 41, no. 1, pp. 1–66, 1997. 

- [30] ——, “Introduction to Neo-Riemannian Theory: A Survey and a Historical Perspective,” _Journal of Music Theory_ , vol. 42, no. 2, pp. 167–180, 1998. 

- [31] D. Tymoczko, _A Geometry of Music: Harmony and Counterpoint in the Extended Common Practice_ . Oxford: Oxford University Press, 2011. 

- [32] D. Harasim, S. E. Schmidt, and M. Rohrmeier, “Bridging scale theory and geometrical approaches to harmony: The voice-leading duality between complementary chords,” _Journal of Mathematics and Music_ , vol. 10, no. 3, pp. 193–209, 2016. 

- [33] D. Harasim, T. Noll, and M. Rohrmeier, “Distant Neighbors and Interscalar Contiguities,” in _Mathematics and Computation in Music_ , ser. Lecture Notes in Computer Science, M. Montiel, F. Gomez-Martin, and O. A. Agustín-Aquino, Eds. Cham: Springer International Publishing, 2019, pp. 172–184. 

- [34] J. Bragg, E. Chew, and S. Shieber, “Neo-riemannian cycle detection with weighted finite-state transducers,” in _Proceedings of the 12th International Society for Music Information Retrieval Conference (ISMIR 2011)_ , 2011, pp. 399–404. 

- [35] R. Lieck, F. C. Moss, and M. Rohrmeier, “The Tonal Diffusion Model,” _Transactions of the International Society for Music Information Retrieval_ , vol. 3, no. 1, pp. 153–164, 2020. 

- [36] A. J. Milne and S. Holland, “Empirically testing _Tonnetz_ , voice-leading, and spectral models of perceived triadic distance,” _Journal of Mathematics and Music_ , vol. 9737, no. April, pp. 1–27, 2016. 

- [37] E. Chew, “Towards a mathematical model of tonality,” Doctoral Dissertation, Massachusetts Institute of Technology, 2000. 

- [38] M. Navarro-Cáceres, M. Caetano, G. Bernardes, M. Sánchez-Barba, and J. Merchán Sánchez-Jara, “A Computational Model of Tonal Tension Profile of Chord Progressions in the Tonal Interval Space,” _Entropy_ , vol. 22, no. 11, p. 1291, Nov. 2020. 

- [39] C. L. Krumhansl and E. J. Kessler, “Tracing the dynamic changes in perceived tonal organization in a spatial representation of musical keys.” _Psychological Review_ , vol. 89, no. 4, pp. 334–368, 1982. 

- [40] F. Korzeniowski and G. Widmer, “Improved Chord Recognition by Combining Duration and Harmonic Language Models,” in _Proceedings of the 19th ISMIR Conference_ , Paris, France, 2018, pp. 10–17. 

- [41] P. Janata, J. Birk, J. V. Horn, M. Leman, J. D. Van Horn, M. Leman, B. Tillmann, and J. J. Bharucha, “The cortical topography of tonal structures underlying Western music,” _Science_ , vol. 298, no. 5601, pp. 2167–2170, Dec. 2002. 

- [42] G. Bernardes, D. Cocharro, M. Caetano, C. Guedes, and M. E. Davies, “A multi-level tonal interval space for modelling pitch relatedness and musical consonance,” _Journal of New Music Research_ , vol. 8215, no. July, pp. 1–14, 2016. 

- [43] A. Simon, “Béla Bartók: ›Secondes mineures – septièmes majeures‹ (Mikrokosmos, VI/144),” _Schweizerische Musikzeitung - Revue musicale suisse_ , vol. 123, pp. 82–86, 1983. 

- [44] B. Haas, _Die Neue Tonalität von Schubert Bis Webern: Hören Und Analysieren Nach Albert Simon_ . Wilhelmshaven: Florian Noetzel, 2004. 

- [45] M. Polth, “The Individual Tone and Musical Context in Albert Simon’s Tonfeldtheorie,” _Music Theory Online_ , vol. 24, no. 4, 2018. 

- [46] ——, “»Tonalität der Tonfelder. Anmerkungen zu Bernhard Haas, Die neue Tonalität von Schubert bis Webern. Hören und Analysieren nach Albert Simon, Wilhelmshaven: Noetzel 2004«,” _Zeitschrift der Gesellschaft für Musiktheorie_ , vol. 3, no. 1, pp. 167– 178, 2006. 

- [47] J. Schild, “"... zum Raum wird hier die Zeit." Tonfelder in Wagners Parsifal,” in _Funktionale Analyse: Musik - Malerei - Antike Literatur_ , B. Haas and B. Haas, Eds. Hildesheim, Zürich, New York: Georg Olms Verlag, 2010, pp. 313–373. 

- [48] D. Schiltknecht, “›Konstrukt‹ und ›Funktion‹ – Eine Herleitung der Simonschen Tonfelder,” _2Zeitschrift der Gesellschaft für Musiktheorie_ , vol. 8, no. 2, pp. 351– 363, 2011. 

- [49] F. C. Moss, “"Theorie der Tonfelder" nach Simon und "Neo-Riemannian Theory": Systematik, historische Bezüge und analytische Praxis im Vergleich,” MA Thesis, Hochschule für Musik und Tanz Köln, Nov. 2012. 

- [50] M. Polth, “Zur Artikulation von Tonfeldern bei Brahms, Debussy und Stockhausen,” _Zeitschrift der Gesellschaft für Musiktheorie [Journal of the Germanspeaking Society of Music Theory]_ , vol. 8, no. 2, pp. 225–265, 2011. 

- [51] ——, “„nicht tonal und nicht atonal“ Zur Bedeutung der Quinten in Ligetis Etüde Nr. 8 „Fém“,” _Studia Musicologica_ , vol. 57, no. 1-2, pp. 121–138, Jun. 2016. 

- [52] M. Rohrmeier and M. Pearce, “Musical Syntax I: Theoretical Perspectives,” in _Springer Handbook of Systematic Musicology_ , R. Bader, Ed. Berlin: Springer, 2018, pp. 473–486. 

576 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

- [53] J. Katz and D. Pesetsky, “The Identity Thesis for Language and Music,” _Draft published online,: lingBuzz/000959_ , no. January, 2011. 

- [54] C. Finkensiep, R. Widdess, and M. A. Rohrmeier, “Modelling the Syntax of North Indian Melodies with a Generalized Graph Grammar,” in _Proceedings of the 19th International Society for Music Information Retrieval Conference_ , no. CONF. ISMIR, Nov. 2019, p. 462. 

- [55] K. Hirata, S. Tojo, and M. Hamanaka, “Implementing "A Generative Theory of Tonal Music",” _Journal of New Music Research_ , vol. 35, no. 4, pp. 249–277, 2006. 

- [56] S. Abdallah, N. Gold, and A. Marsden, “Analysing symbolic music with probabilistic grammars,” in _Computational Music Analysis_ , D. Meredith, Ed. Springer, 2016, pp. 157–189. 

- [57] A. Marsden and G. A. Wiggins, “Schenkerian reduction as search,” _Fourth Conference on Interdisciplinary Musicology (CIM08)_ , no. July, 2008. 

- [58] M. Rohrmeier and M. Neuwirth, “Towards a Syntax of the Classical Cadence,” in _What Is a Cadence?_ , M. Neuwirth and P. Bergé, Eds. Leuven: Leuven University Press, 2015, pp. 285–336. 

- [59] D. Quick and P. Hudak, “Grammar-based automated music composition in Haskell,” _Proceedings of the first ACM SIGPLAN workshop on Functional art, music, modeling & design - FARM ’13_ , pp. 59–70, 2013. [Online]. Available: http://dl.acm.org/citation. cfm?doid=2505341.2505345 

- [60] M. Steedman, “The blues and the abstract truth: Music and mental models,” _Mental models in cognitive science: essays in honour of Phil Johnson-Laird_ , p. 305, 1996. 

- [61] J. Katz, “Harmonic Syntax of the Twelve-Bar Blues Form,” _Music Perception: An Interdisciplinary Journal_ , vol. 35, no. 2, pp. 165–192, Dec. 2017. 

- [62] M. Granroth-Wilding and M. Steedman, “A robust parser-interpreter for jazz chord sequences,” _Journal of New Music Research_ , 2014. 

- [63] D. Harasim, M. Rohrmeier, and T. J. O’Donnell, “A Generalized Parsing Framework for Generative Models of Harmonic Syntax,” in _Proceedings of the 19th International Society for Music Information Retrieval Conference (ISMIR 2018)_ , Paris, France, Sep. 2018, pp. 152–159. 

- [64] B. De Haas, M. Rohrmeier, R. Veltkamp, and F. Wiering, “Modeling harmonic similarity using a generative grammar of tonal harmony,” in _Proceedings of the 10th International Society for Music Information Retrieval Conference (ISMIR 2009)_ , K. Hirata and G. Tzanetakis, Eds., 2009. 

- [65] Y. Ogura, H. Ohmura, Y. Uehara, S. Tojo, and K. Katsurada, “Expectation-based parsing for jazz chord sequences,” in _The Proceedings of 17th SMC Sound and Music Computing Conference_ , 2020. 

- [66] L. Euler, “De harmoniae veris principiis per speculum musicum repraesentatis,” in _Novi Commentarii Academiae Scientiarum Petropolitanae_ , St. Petersburg, 1774, vol. 18, pp. 330–353. 

- [67] C. Longuet-Higgins, “The Three Dimensions of Harmony,” in _Mental Processes: Studies in Cognitive Science_ . Cambridge, MA: MIT Press, 1987, pp. 59–63. 

- [68] J. Douthett and P. Steinbach, “Parsimonious graphs: A study in parsimony, contextual transformations and modes of limited transposition,” _Journal of Music Theory_ , vol. 42, no. 2, pp. 241–263, 1998. 

- [69] M. Woolhouse, “Wagner in the Round: Using Interval Cycles to Model Chromatic Harmony,” in _Proceedings of the 12th International Conference on Music Perception and Cognition and the 8th Triennial Conference of the European Society for the Cognitive Sciences of Music_ , E. Cambouropoulos, C. Tsougras, P. Mavromatis, and K. Pastiadis, Eds., Thessaloniki, 2012, pp. 1142– 1145. 

- [70] E. Lendvai, _Béla Bartók: An Analysis of His Music_ . London: Kahn & Averill, 1971. 

- [71] O. Messiaen, _Technique de Mon Langage Musical_ . Paris: Alphonse Leduc, 1944, vol. 1. 

- [72] J. N. Straus, _Introduction to Post-Tonal Theory_ , 3rd ed. New York: Pearson Prentice Hall, 2005. 

- [73] A. Forte, _The Structure of Atonal Music_ . New Haven and London: Yale University Press, 1977. 

- [74] M. Levine, _The Jazz Theory Book_ . Sebastopol, CA: O’Reilly Media, 2011. 

- [75] ——, _The Jazz Piano Book_ . Sher Music Co. / Advance Music, 1990. 

- [76] R. Cohn, “Hexatonic poles and the uncanny in Parsifal,” _Opera Quarterly_ , vol. 22, no. 2, pp. 230–248, Apr. 2006. 

- [77] M. Steedman, _The Syntactic Process_ . Cambridge, MA: MIT press, 2000. 

- [78] R. Cohn, “On Hexatonic Poles,” _Music Analysis_ , vol. 0, pp. 1–5, 2016. 

- [79] N. Chomsky, “Formal properties of grammar,” in _Handbook of Mathematical Psychology_ , R. Luce, R. Bush, and E. Galanter, Eds. New York: Wiley, 1963, pp. 323–418. 

- [80] M. Rohrmeier, “Towards a formalization of musical rhythm,” in _Proceedings of the 21st International Society for Music Information Retrieval Conference_ , 2020. 

577 

Proceedings of the 22nd ISMIR Conference, Online, November 7-12, 2021 

- [81] S. Tojo, “Modal logic for tonal music,” in _Perception, Representations, Image, Sound, Music: 14th International Symposium, CMMR 2019, Marseille, France, October 14–18, 2019, Revised Selected Papers 14_ . Springer International Publishing, 2021, pp. 113–128. 

- [82] D. Harasim, T. J. O’Donnell, and M. A. Rohrmeier, “Harmonic Syntax in Time: Rhythm Improves Grammatical Models of Harmony,” in _Proceedings of the 20th ISMIR Conference_ , no. CONF. ISMIR, 2019, p. 335. 

578 

