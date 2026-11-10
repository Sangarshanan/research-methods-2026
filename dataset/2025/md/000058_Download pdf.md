---
paper_id: "000058"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706496/files/000058.pdf"
---

# KEYBOARD TEMPERAMENT ESTIMATION FROM SYMBOLIC DATA: A CASE STUDY ON BACH’S WELL-TEMPERED CLAVIER 

Peter van Kranenburg Utrecht University `p.vankranenburg@uu.nl` 

Gerben Bisschop Utrecht University `g.bisschop@uu.nl` 

## ABSTRACT 

In this paper we address the task of keyboard temperament estimation from symbolic data. The aim is to find a keyboard temperament that minimizes the deviations from pure intervals, given a corpus of music. The problem of finding a suitable temperament has been studied for centuries. Many solutions have been proposed. By taking a data-driven approach, we contribute a method to this field. We define a loss function that measures the deviation from pure intervals, with a reward for exactly pure intervals. Three optimization methods are explored: Basin Hopping, Differential Evolution, and Dual Annealing. We validate our method with synthetic data, and by comparing with c. 1,500 existing temperaments, including equal temperament. Our method improves on any existing temperament. As a case study, we apply the method to Bach’s Well-Tempered Clavier. Our findings show interesting correspondence to existing proposals in musicological literature. 



<!-- Start of picture text -->
K1 K3 K6 K8 K10<br>B" D♯ E" A♯<br>G♯<br>C♯ E♭ F♯ B♭<br>A♭<br>D♭ F! G♭ C!<br>B♯ C" D" E♯ F" G" A"<br>C D E F G A B<br>D! E! F♭ G! A! B! C♭<br>K0 K2 K4 K5 K7 K9 K11<br><!-- End of picture text -->

Figure 1. Standard Western keyboard layout with key indices (0-11). 

## 1. INTRODUCTION 

Keyboard instruments in the Western musical tradition, including harpsichords, organs, and pianos, typically feature twelve keys per octave, each generating a tone with a distinct, fixed fundamental frequency. Consequently, these instruments can produce twelve unique frequencies within each octave. Yet, Western music theory posits that more than twelve frequencies per octave are necessary to achieve in-tune performance across all prevalent tonalities. 

Figure 1 shows the standard layout of one octave of the keyboard. The second black key (K3), for example, is shared by D♯, E♭, and F♭♭. To play a major third with a B as root, the D♯ is needed, but for a minor third on a C, the E♭ is needed. To play these intervals pure (in-tune), we need different frequencies for the D♯ and the E♭, but they share the same key. Therefore, each choice of frequencies for the 12 keys (each temperament) is a compromise. It is impossible to chose the 12 frequencies such that all possible intervals are pure. 

> © P. van Kranenburg and G. Bisschop. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: P. van Kranenburg and G. Bisschop, “Keyboard Temperament Estimation from Symbolic Data: A Case Study on Bach’s WellTempered Clavier”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

This situation has caused a vast body of musicological literature, spanning many centuries [1]. Numerous solutions have been proposed, and music theorists got engaged in often heated debates about which solution to favor. A simplified reading of music history tells us that since the nineteenth century equal temperament has been in use. This is a temperament in which all intervals between the successive keys are tuned exactly equal in size. As a consequence of this ultimate compromise, all intervals are outof-tune. Modern musical hearing for modern music styles is tolerant for that. So, for much of contemporary Western music the question seems settled. However, for performing early music, non-equal temperaments are almost always possible and often crucial, especially if the aim is a historically informed performance. Composers made use of tension and release patterns between less and more intune intervals, which are lost in equal temperament. 

The modern performer’s choice for a particular temperament can be based on various sources. Many historic treatises have been preserved providing detailed descriptions of tuning systems, often based on mathematical and philosophical considerations. Another source of knowledge is the body of historic tuning instructions, which reflects practitioners’ approaches throughout the centuries. To a limited extent, surviving historic instruments offer some clues, but these remain often speculative. 

503 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

So, both from practical (instrument builders, tuners, performers) and theoretical (music historians, music theorists) points of view, the question how to find a suitable temperament is very actual. Instead of a historic or theoretic approach, in this paper we employ a data-driven method. The aim is to derive a temperament from the contents of a corpus of compositions. Given the inventory of all occurring intervals, we minimize a loss function that reflects to what extent the intervals deviate from pure. We explore several optimization algorithms, and we define various possibilities for a suitable loss function. 

Not much work on temperaments has been done within the field of Music Information Retrieval. A related Music Information Retrieval task is temperament estimation from audio recordings [2–4]. However, this is aimed at recognizing the actual temperament of an instrument from an audio recording. Rather, in most MIR studies that deal with pitch, the question is bypassed by e.g., binning of pitches in tasks such as F0 detection or chroma feature extraction, or by methods that are simply not precise enough to capture differences of a few cents. Musicological literature features several studies that employ statistical methods to deduce temperaments [5–7]. Particularly relevant is the work of Martínez Ruiz [8, pp. 110ff], who took a similar approach to ours. We extend these efforts by introducing an optimization approach that identifies the optimum within a continuous space instead of performing brute-force searches, and by formulating a loss function that incorporates an arbitrary set of intervals. 

To explore the affordance of our method, we focus on the two books of Das Wohltemperirte Clavier by Johann Sebastian Bach (1685–1750). Bach’s intended temperament remains unknown, which led to extensive discussions and speculation in musicological literature. We both assess a huge number of historic temperaments, and we examine the solutions of our method. 

In this paper, we illustrate that our proposed method serves not only as a MIR tool for deriving an optimal temperament but also as an experimental framework for investigating diverse hypotheses about what constitutes an optimal temperament. In this paper, we make a set of heuristic choices for interval ratios and for loss and reward calculations, but by manipulating these, and examining the outcome, a process of modeling is facilitated that has the potential to deepen our understanding of musical tuning systems and their perceptual effects, potentially leading to further refinements and innovations in both theoretical and practical applications of temperament design [9, Ch. 1]. 

## 2. METHOD 

In this section we present the method to computationally find an optimal temperament for a given corpus of music. First we define the representation of a temperament. Then we present the representation of a corpus of music. Next, we present the objective function, and we motivate the optimization algorithms we employ. Finally, we run several tests with synthetic data to validate the approach. 

## 2.1 Temperament representation 

We define a temperament as a vector p = (p0, p1, . . . , p11) where pi is the size of the interval of key K0 (the C) with Ki in cents. p0 is always zero (the interval of C with itself), but we keep it in the vector for convenience. 

There are different ways of representing the size of an interval: frequency differences, frequency ratios and cent values. In this paper we adopt ratios and cent values. The frequency ratio is that of the higher pitch to the lower. For example, for a pure perfect fifth this is 3/2. Cents measure pitch differences on a logarithmic scale, where the octave is divided in 1200 equal steps, each corresponding to 1¢. Thus the size of an interval in cents is computed as: 



<!-- Start of picture text -->
Cents = 1200 · log2 ¢,<br>� f f 21 �<br><!-- End of picture text -->

where f1 is the frequency of the lowest pitch and f2 the frequency of the highest pitch. For a pure perfect fifth, this results in 701.96¢. Using cent representations, the size of successive intervals can be computed by simple addition and subtraction 

## 2.2 Corpus Representation 

In this section, we discuss how to represent a corpus of music. Because we assume pure octaves, it is sufficient to consider all twelve possible intervals on each of the twelve keys within the octave, resulting in a set of 144 possible intervals. As notation for such an interval, we introduce Ij,k, indicating an interval of k keys (semitones) with Kj as root. E.g., I0,5 is the interval of 5 keys (mostly a perfect fourth) with K0 as root, and I7,2 is the interval of two keys (mostly a major second) with K7 as root. 

We represent a given corpus of music as the set of weighted occurrence rates of these 144 possible intervals. In counting the occurrence rates, we include both melodic intervals (between successive tones), and harmonic intervals (between simultaneously sounding pitches). 

For the extraction of the harmonic intervals, we make use of the music21 [10] chordify function. This function slices the score such that any change in any part starts a new slice, and collapses all simultaneous pitches for each slice in a single chord. We then examine all distinct ascending intervals in each resulting chord and update the counts in our interval repertory accordingly. For the melodic intervals, we simply take all successive intervals for all parts. 

We multiply each count with two weights. First to compensate for the different durations of the slices with harmonic intervals, we weigh the counts by the duration of the slice, measured in quarter note lengths. For melodic intervals we take the length of the shortest note as weight. Second, we weigh by auditory impact. To indicate two extremes, an interval that is formed by a passing 16th note on a metrically insignificant position has a different auditory impact than an interval in the final chord of a cadence. For the passing tone, the temperament can be more tolerable than for the prominent chord. To capture this nuance, we 

504 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

|Size|Interval|ratio|cents|Size|Interval|ratio|cents|Size|Interval|ratio|cents|
|---|---|---|---|---|---|---|---|---|---|---|---|
|0|P1|1|0|4|M3/d4|5/4|386.31|8|m6/A5|8/5|813.69|
|1|m2/A1|16/15|111.73|||81/64|407.82|||128/81|792.18|
|||17/16|104.96|5|P4|4/3|498.04|||11/7|782.49|
|||27/25|133.24|6|d5/A4|45/32|590.22|9|M6|5/3|884.36|
|||135/128|92.18|||7/5|582.51|||27/16|905.87|
|||256/243|90.22|||10/7|617.49|10|m7/A6|16/9|996.09|
|||25/24|70.67|||13/9|636.62|||9/5|1017.6|
|2|M2/d3|9/8|203.91|||18/13|563.38|11|M7|15/8|1088.27|
|||10/9|182.4|||25/18|568.72|||50/27|1066.76|
|3|m3/A2|6/5|315.64|||36/25|631.28|||243/128|1109.78|
|||19/16|297.51|||64/45|609.78|||||
|||32/27|294.13|7|P5|3/2|701.96|||||



Table 1. Intervals. Size is the size k of interval Ij,k on the keyboard, corresponding with the distance measured in number of keys (semitones). The column Interval shows some enharmonically equivalent intervals that are realized by the corresponding key pairs (P: Perfect, M: Major, m: Minor, d: diminished, A: augmented). The ratios are acceptable frequency ratios for this interval. The cents column shows the size of these ratios in cents. The ratios in bold form the set Tjust, which are the target ratios for the five-limit just intonation. 

weigh the count by the beatstrength ∈ (0, 1], which is the metric weight according to music21’s meter model [11]. For harmonic intervals, we take the beatstrength of the chord, for melodic intervals, we take the beatstrength of the second note, since that is heard in relation to the previous note. As a final step we normalize all weighted occurrence rates in our inventory such that the sum is 1. 

## 2.3 Target 

To define the loss function, we first must consider the target we are looking for. The primary goal of a temperament is to ensure all audible intervals are perceptually acceptable, while optimizing as many intervals as possible to approach pure consonance. The first question then is what determines whether an interval is pure. In general, intervals with ratios that can be written as fractions of low integers are considered preferable. Examples of such simple fractions are the perfect prime (1/1), perfect octave (2/1), prefect fifth (3/2), and major third (5/4). These fractions correspond with intervals between the lowest overtones in the harmonic series. 

We assembled a set of acceptable ratios for each of the 12 possible intervals within an octave. For most intervals, several fractions have been established in literature. For example, for the major third, next to 5/4, also the fraction 81/64 can occur. This is the major third that results from stacking four ascending fifths and two descending octaves (3/2)<sup>4</sup> ∗ (1/2)<sup>2</sup> = 81/64. Similarly, for other intervals there are multiple possibilities to derive a ratio. Table 1 shows all possible interval sizes in semitones on the keyboard within an octave, with for each interval a list of acceptable target ratios. A well-known subset is the five-limit just intonation, in which only octaves, fifths, and thirds are used to construct the intervals. The ratios in bold are a common choice for this intonation. Throughout the rest of this paper, we use two sets of targets: Tall, including all targets, and Tjust, including only the just target ratios. We denote the set of targets for an interval of s semitones as Tall,s and Tjust,s respectively. 

## 2.4 Loss Function 

As loss we take the mean squared error of the actual sizes of the intervals Ij,k with their nearest acceptable targets in cents. This gives us the following loss function: 



<!-- Start of picture text -->
LMSE(p) = � ri · [t∈minTx,s |ci − t|]2,<br>i<br><!-- End of picture text -->

where ri is the weighted occurrence rate of the i-th interval in the corpus inventory (see Section 2.2), ci = [(pk − pj) mod 1200] is the size in cents of that interval given temperament p, t ∈ Tx,s is the size in cents of the closest target, where s is the size of interval i in semitones. E.g., when using Tall, for any interval of 2 semitones the set of target sizes is Tall,2 = {203.91, 182.4} (see Table 1). Note that only intervals for which ri̸ = 0 contribute to the loss value. 

To stimulate the intervals in the resulting temperament to end up as close as possible to a just interval, we introduce an additional exponential reward term: 



<!-- Start of picture text -->
αi · e −β·[mint |ci−t|] if t ∈ Tjust,s,<br>Rpure =<br>�0 if t ∈/ Tjust,s.<br><!-- End of picture text -->

which rewards values close to a target value, but only if that closest target is in the set of just intervals. The intention is to ‘snap’ the interval to a just ratio when exploring the solution space. αi regulates the magnitude of the reward, and β the rate of decay. This reward term has a high value at the target, drops quickly for values close to the target and approaches 0 for large values. By setting different values for αi for the different intervals, we can for example favor pure thirds over pure fifths. In this paper we set all αi to 10 and β to 2, which gives a relatively steep slope close to the target, and a maximum reward of 10. We subtract the reward value from the squared error, because the loss function will be minimized. Thus, our full loss function is: 



<!-- Start of picture text -->
L(p) = � ri · ([mint |ci − t|] 2 − Rpure).<br>i<br><!-- End of picture text -->

For use with the Dual Annealing optimization method (see next Section), we add a further term that controls for 

505 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

boundaries of perfect fifths. We want to be able to set a lower and an upper boundary for the sizes of any of the perfect fifths that occur in the corpus. This is achieved by introducing a penalty for temperaments that cross these boundaries. This penalty term is defined as: 



<!-- Start of picture text -->
P7 = γ · � �1 − e −δvj �<br>j<br><!-- End of picture text -->

where vj represents the violation of the j-th perfect fifth beyond the bounds measured in cents, only including the fifths that occur in the corpus. For example, suppose we set the lower limit to 696¢, and we have two fifths of 691¢that occur in the corpus, and the other 10 fifths within the boundaries, we then have a penalty of P7 = γ · 2 · (1 − e<sup>−δ·5</sup> ). Parameter γ controls the height of the ‘plateau’ for larger deviations, and δ controls the steepness of the function. In this paper, we set γ to 100 and δ to 1. Note that in this way we could set bounds for any of the twelve intervals, but in this paper we only use bounds for fifths. Including this penalty, the loss function becomes: 



<!-- Start of picture text -->
Lbounded(p) = � ri · ([mint |ci − t|] 2 − Rpure) + P7.<br>i<br><!-- End of picture text -->

The values of α, β, and γ, could probably be further optimized. We did not do a full search, but we choose sensible values, which prove to deliver good results. 

## 2.5 Optimization Algorithm 

We employ three different approaches to find the global minimum of the loss function: Basin Hopping (BH) [12], Differential Evolution (DE) [13], and Dual Annealing (DA) [14]. These were selected because of their ability to handle non-linear problems in which the loss function is not continuously differentiable, as is the case in our loss function because of the min operator. We use the implementations as provided in the Python SciPy module [15]. 

BH explores the energy landscape by perturbing solutions and accepting moves based on a Metropolis criterion. A crucial parameter is the initial step size, which we set to 30¢ to allow a wide enough search space to overcome local minima. BH needs a local optimizer, for which we choose the COBYLA method [16] which is suited for objective functions that are not continuously differentiable. DA combines simulated annealing with a local search, introducing a generalized temperature schedule to escape local minima efficiently. For DA, we make use of our P7 term if we want to constraint the sizes of fifths, since the implementation in SciPy does not accept external constraints. A crucial parameter for DA is the initial temperature, which regulates the probability with which a proposed solution is accepted. If we include the fifths constraint P7, we set the initial temperature to 150 to deal with the high penalty γ for violating the bounds. If we do not constrain the fifths, we set it to 50. DE is a population-based method. It evolves candidate solutions through mutation, crossover, and selection, excelling in continuous optimization without requiring gradient information. In our application, we set the population size to 100 [17]. 

## 2.6 Validation 

We validate our method by comparing the loss value of our method with the loss values for a collection of existing temperaments, given two synthetic interval inventories. We generate an interval inventory CC that is representative for a piece in C major that includes modulations to the dominant, subdominant, and relative minor keys, and an inventory Cuni, which includes a uniform distribution over all possible 144 intervals. 

To generate CC, we adopt the Krumhansl-Kessler pitch profiles [18, 19] to estimate the probability of occurrence of scale tones. We interpret the profiles as probability distributions, and we sample a large amount pairs of pitches from the various scales in the proportion: 40% tonic, 30% dominant, 20% subdominant, and 20% relative minor. Within each scale, we only sample diatonic scale tones, taking the melodic minor scale for the relative minor. To reflect the different probabilities of occurrence of the different harmonic intervals, we weigh each counted interval with a harmonic score, ranging from 1 for the minor second, to 10 for perfect unisons and fifths. 

We use the collection of existing temperaments that is digitally available as part of the Scala software package.<sup>1</sup> This includes both historical and contemporary temperaments. From the entire set of over five thousand temperaments, we select those that define 12 pitches per octave, resulting in a subset of c. 1,500. These can be considered as solutions that already have been discovered. For each temperament, we calculate the loss given our synthetic corpora, and we compare the minium loss value as discovered by our method. We do this for both target sets Tall and Tjust. 

The results for 10 runs of each algorithm are shown in Table 2. Our method improves on all included existing temperaments from the Scala collection, indicating the success of the optimization. The discovered optima are comparable among the three algorithms. Differential Evolution has the huge advantage of a short running time (low µt), while Dual Annealing is generally more consistent in the optimum (lower σL), and Basin Hopping is the worst performing of the three methods. 

Noteworthy here is that for Cuni and Tall all resulting temperaments show one narrow wolf fifth (686.21¢), one equal tempered fifth (700¢), and two fifths slightly lower than equal. This implies that this temperament is optimal given the collection of ratios rather than given the corpus. For Cuni and Tjust, not unexpectedly, we find equal temperament for all runs. 

## 3. BACH’S “WOHLTEMPERIRTE CLAVIER” 

One of the most famous sets of compositions that cycles through the full set of 24 tonalities (one minor and one major piece for each of the 12 pitches within the octave) is Johann Sebastian Bach’s Wohltemperirte Clavier (WTC), consisting of two books (dated 1722 and 1742), 48 pieces in total. There is no historical record about the preferred 

> 1 `https://www.huygens-fokker.org/scala/ downloads.html#scales` 

506 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

|CC,Ta|ll: all target ratio|s||CC,Tjust: only|just target ra|tios||
|---|---|---|---|---|---|---|---|
|temp.|min(L)|σL|µt|temp.|min(L)|σL|µt|
|Dual Annealing|-7.2274|0.00022|360 s|Dual Annealing|27.7735|4.06e-6|204 s|
|Diff. Evolution|-7.2274|0.00137|59.9 s|Diff. Evolution|27.7735|5.98e-8|44.1 s|
|Basin Hopping|-7.212|0.0235|317 s|Basin Hopping|27.7823|0.00285|528 s|
|pyth_12|-7.1467|-|-|smithgw_well1|28.5731|-|-|
|parizek_jiwt2<br>raintree|-5.8116<br>-5.3601|-<br>-|-<br>-|sparschuh-442widefrench5th-a<br>scottd1|28.6816<br>28.7232|-<br>-|-<br>-|
|Cuni,T|all: all target ratio|s||Cuni,Tjust: only|just target r|atios||
|temp.|min(L)|σL|µt|temp.|min(L)|σL|µt|
|Dual Annealing|1.5571|1.874e-5|598 s|Dual Annealing|105.23|0|172 s|
|Diff. Evolution|1.5571|0.0421|148 s|Diff. Evolution|105.23|0|26.6 s|
|Basin Hopping|1.5726|0.0271|631 s|Basin Hopping|105.23|0|1072 s|
|ramis|1.6523|-|-|equal|105.23|-|-|
|schiassi|1.7727|-|-|neidhardt4|105.23|-|-|
|erlangen2|1.7727|-|-|hanfling-bumler|105.23|-|-|



Table 2. Results on the synthetic interval inventories CC (C major), and Cuni (uniform distribution). Existing temperaments and our methods are ordered according to loss value for both Tall and Tjust. min(L) is the lowest loss value out of 10 runs, σL is the standard deviation of the 10 loss values, and µt is the average runtime of the optimization algorithm. 



<!-- Start of picture text -->
T a ll T a ll (bounded) T just<br>ramis 0.47 kelletat1 10.27 marpurg-a 105.04<br>erlangen 0.84 kelletat 10.78 temp12b2w 105.61<br>erlangen2 1.13 sorge1 11.05 pykett_dorset 105.87<br>schiassi 1.28 dudon_comptine 11.12 handel2 106.19<br>marpurg-t1 1.41 dudon_comptine_h3 11.62 ellis_eb 106.3<br>kirnber g er1 1.41 scottd1 11.84 stevin 106.31<br><!-- End of picture text -->

Table 3. Highest scoring Scala temperaments, given WTC, using Tall, Tall with fifths bounded between 696 and 705¢, and Tjust. 

temperament by Bach himself. This caused extensive speculation in musicological literature. We take the full WTC as corpus for a case study to explore our method. We begin by assessing existing temperaments from the Scala collection, followed by the calculation of optimal temperaments using our proposed method. Then we discuss the experimental results in the context of musicological literature 

## 3.1 Experiment 1: Evaluating Existing Temperaments 

We compute the loss values for the existing temperaments. We do this, again, both for Tall and Tjust. The temperaments with the lowest values are shown in Table 3. An in-depth discussion of these temperaments would be highly interesting, but is beyond the scope of this article. It turns out that all of the results for Tall are variants of the historic temperament of Kirnberger (1766). This family of temperaments has one narrow fifth (680¢), one schismatic fifth (700¢), and 10 pure fifths (701.96¢). They only differ in the location of the tempered fifths. Given our result for Cuni, this is not surprising. Aiming for a ‘circular‘ temperament, i.e., one without wolf intervals, we bind all fifths between 696 and 705¢. Using these values as constraints, we find a temperament by Herbert Kelletat [20]. Kelletat’s solution fits the WTC very well because he places the narrower fifths on C, G, D, and A, which are the least frequent fifths in the WTC. Maybe surprisingly, the fifths on black keys are most frequent, with the fifth E♭/D♯–B♭/A♯ roughly twice as frequent throughout the WTC as the fifth G-D. 

## 3.2 Experiment 2: Estimating Optimal Temperament 

We run our optimization method given Bach’s WTC for Tall (both bounded and unbounded fifths) and Tjust. The resulting optimal temperaments are shown in Figure 2. We find for Tall a temperament with one narrow wolf fifth on G and two schismatic fifths on C and A (top row), for Tall with bounded fifths a temperament similar to Kelletat’s, which has tempered fifths on F, C, G, D, and A (middle row), and for Tjust a nearly equal temperament (bottom row), with two pure fifths on D and A. 

## 4. DISCUSSION 

The result we obtained both for our uniformly distributed collection of intervals Cuni, and for Bach’s WTC suggests that the optimal WTC temperament, given our loss function, and given our choice of acceptable ratios, is closely related to Johann Philipp Kirnberger’s unequal temperament from 1766, which, in a variety of variants, was used across Western Europe for a century. Could Bach’s WTC indeed have been tuned in Kirnberger’s temperament, as Herbert Kelletat claimed in 1960 [20]? 

The connection between Kirnberger’s temperament and Bach’s tuning dates back to the eighteenth century. Since Kirnberger, as Bach’s student, consistently preferred his unequal temperament over equal temperament starting in 1766 [22–24], later authors have inferred that Kirnberger represented Bach’s temperament. In the pen battle Kirnberger waged in the 1770s with his contemporary Wilhelm Friedrich Marpurg, Marpurg argued that Bach’s temperament was equal, claiming that Kirnberger himself stated Bach wanted all thirds tuned uniformly “high” [25]. Marpurg referred to “equal temperament” in the tradition of Werckmeister-Neidhardt-Rameau [26–28], and saw his position supported by contemporaries such as Johann Nicolas Forkel [29], Carl Philipp Emanuel Bach [30], and piano maker Barthold Fritz [31] (though their temperaments, individually, later proved not to be equal). 

Based on Marpurg’s widely accepted viewpoint, it 

507 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
WTC - All Ratios - Loss: -0.0124<br>P5 (701.96) M3 (386.31,407.82) m3 (315.64,297.51,294.13) M2 (203.91,182.4) m2 (111.73,104.96,133.24,92.18,90.22,70.<br>74 0 44 0 34 0 24 0 14 0<br>72 0 42 0 32 0 22 0 12 0<br>70 0 40 0 30 0 20 0 10 0<br>68 0 38 0 28 0 18 0 8 0<br>66 0 36 0 26 0 16 0 6 0<br>Ab Eb Bb F C G D A E B F# C# Ab Eb Bb F C G D A E B F# C# Ab Eb Bb F C G D A E B F# C# Ab Eb Bb F C G D A E B F# C# Ab Eb Bb F C G D A E B F# C#<br>WTC - All Ratios - Bounded Fifths - Loss: 9.9024<br>P5 (701.96) M3 (386.31,407.82) m3 (315.64,297.51,294.13) M2 (203.91,182.4) m2 (111.73,104.96,133.24,92.18,90.22,70.<br>74 0 44 0 34 0 24 0 14 0<br>72 0 42 0 32 0 22 0 12 0<br>70 0 40 0 30 0 20 0 10 0<br>68 0 38 0 28 0 18 0 8 0<br>66 0 36 0 26 0 16 0 6 0<br>Ab Eb Bb F C G D A E B F# C# Ab Eb Bb F C G D A E B F# C# Ab Eb Bb F C G D A E B F# C# Ab Eb Bb F C G D A E B F# C# Ab Eb Bb F C G D A E B F# C#<br>WTC - Five Limit Just Ratios - Loss: 104.5117<br>P5 (701.96) M3 (386.31) m3 (315.64) M2 (203.91) m2 (111.73)<br>74 0 44 0 34 0 24 0 14 0<br>72 0 42 0 32 0 22 0 12 0<br>70 0 40 0 30 0 20 0 10 0<br>68 0 38 0 28 0 18 0 8 0<br>66 0 36 0 26 0 16 0 6 0<br>Ab Eb Bb F C G D A E B F# C# Ab Eb Bb F C G D A E B F# C# Ab Eb Bb F C G D A E B F# C# Ab Eb Bb F C G D A E B F# C# Ab Eb Bb F C G D A E B F# C#<br>P5 Size (cents) M3 Size (cents) m3 Size (cents) M2 Size (cents) m2 Size (cents)<br>P5 Size (cents) M3 Size (cents) m3 Size (cents) M2 Size (cents) m2 Size (cents)<br>P5 Size (cents) M3 Size (cents) m3 Size (cents) M2 Size (cents) m2 Size (cents)<br><!-- End of picture text -->

Figure 2. Diagrams for the resulting optimal temperaments for WTC. Each row represents a temperament. The diagrams show the sizes of the various intervals given the root of the interval (inspired by Jos De Bie [21]). The dashed lines show the size(s) of the acceptable ratio(s) according to Table 1. The resulting p-vectors from top to bottom: Tall: `(0 , 90.22, 182.4, 294.13, 384.36, 498.04, 588.27, 700, 792.18, 884.36, 996.09, 1086.31)` , Tall with bounded fifths: `(0, 93.02, 192, 296.93, 387.15, 500.85, 591.07, 696, 794.98, 888, 998.89, 1089.11)` , and Tjust: `(0, 102.07, 200.05, 300.9, 403.96, 500.44, 602.71, 700.56, 801.53, 902.01, 1000.8, 1103.37)` . 

was unanimously concluded until the late 19th century that Bach’s Well-Tempered Clavier must have designated “equal temperament.” That is, until Bosanquet suggested in 1876 that Bach’s tuning could also have been circular without necessarily being “gleichschwebend” (equaltempered), a new definition increasingly adopted by authors [32]. In 1960, Herbert Kelletat first suggested Bach used Kirnberger’s unequal temperament, backed by Hans Krüger’s pre-1935 research. [20]. 

John Barnes began in 1979 with hypotheses about Bach’s ideal temperament by calculating which intervals occur most frequently in the WTC, attempting to derive the ideal WTC temperament from this [5] [8, p. 108]. In 1999, Sparschuh claimed to have discovered Bach’s temperament in the calligraphed title of WTC I [33]. A series of subsequent authors examined Sparschuh’s findings by turning the calligraphic WTC title page upside down or interpreting it differently [34–36], with Bradley Lehman gaining prominence with his article in the Journal Early Music [37]. Furthermore, Mark Lindley explored the WTC in 1993 using mathematical models, and Claudio di Veroli, building on Barnes, developed an algorithm to search all partitions of the octave in discrete steps of 2¢ [7], resulting in a temperament with a loss value of 67,147 according to our loss function using Tjust. Subsequently, hypothetical WTC temperaments and analyses were more often rejected because they were deemed difficult to justify from the perspective of historical performance practice. Other authors opted for a specific temperament of their own [8, pp. 108f.], Werckmeister [5, 38–40], Silbermann [41, 42], or offered a multiple-choice approach regarding Bach’s temperament [8]. Surprisingly, no author chose Neidhardt’s temperament as the ideal WTC temperament, despite its frequent historical link to Bach. 

In secondary literature, most authors ultimately chose a Kirnberger related temperament as the best candidate for the ideal WTC temperament [8, pp. 108f., 119f.]. However, none of these authors have so far explored the numerous 19th-century variants that must have made Kirnberger’s temperament sound more circular, as desired for the WTC. Kirnberger himself wrote a second variant in 1766 to distribute the dissonant wolf fifth D-A over two fifths: D-A-E. He faced criticism from violinists that the wolf fifth D-A sounded out of tune with the open fifths tuning of the violin’s four strings: (G-) D-A(-E). In a letter to his friend Forkel, he provided additional variants (Kirnberger III/IV), in which the wolf fifth, spread across four fifths, sounded even less dissonant. By the early 19th century, the name “Kirnberger” became a catch-all term for all unequal temperaments, and numerous international variants (often semi-Pythagorean) were cited in sources, further subdividing the wolf fifth(s). 

## 5. CONCLUSION AND FUTURE WORK 

We presented a framework to find an optimal keyboard temperament given a corpus of (symbolic) music, a set of acceptable frequency ratios, and conditions on the sizes of the intervals. We validated the method on two synthetic corpora. The optimization results improve on c. 1,500 existing temperaments. Our results on WTC support Kirnberger’s relevance, inviting a reconsideration of Kelletat’s 1960s proposal, next to the study of applicability of the many 19th century variants of Kirnberger’s unequal temperament to tune Bach’s WTC. Further future work includes dissonance-based loss functions, listening tests, and a thorough evaluation of historic proposals, including the many variants on Kirnberger’s temperament. 

508 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

Supplemental material for this paper can be found at: `https://github.com/pvankranenburg/ismir2025` . This includes the Python code, motivations for the selected acceptable ratios, selected synthesized examples from the WTC using the temperaments discussed in this paper, and a web application to explore temperaments, including acoustic feedback. 

## 6. REFERENCES 

- [1] O. Jorgensen, Tuning: Containing the Perfection of Eighteenth-Century Temperament, the Lost Art of Nineteenth-Century Temperament, and the Science of Equal Temperament. East Lansing, MI: Michigan State University Press, 1991. 

- [2] S. Dixon, D. Tidhar, and E. Benetos, “The temperament police: the truth, the ground truth, and nothing but the truth,” in Proceedings of the 12th International Conference on Music Information Retrieval (ISMIR 2011), Miami, 2011, pp. 281–286. 

- [3] S. Dixon, M. Mauch, and D. Tidhar, “Estimation of harpsichord inharmonicity and temperament from musical recordings,” The Journal of the Acoustical Society of America, vol. 131, no. 1, pp. 878–887, 2012. 

- [4] D. Tidhar, S. Dixon, E. Benetos, and T. Weyde, “The temperament police,” Early Music, vol. 42, no. 4, pp. 579–590, 2014. 

- [5] J. Barnes, “Bach’s keyboard temperament; internal evidence from the well-tempered clavier,” Early Music, pp. 236–249, April 1979. 

- [6] M. Lindley and R. Turner-Smith, Mathematical Models of Musical Scales, M. Vogel, Ed. Bonn: Verlag für systematische Musikwissenschaft Gmbh, 1993, vol. Band 66 der Orpheus Schriftenreihe zu Grundfragen der Musik. 

- [7] C. Di Veroli, Unequal Temperaments: Theory, History and Practice, 3rd ed. Bray, Ireland: Bray Baroque, 2013. [Online]. Available: http: //temper.braybaroque.ie/ 

- [8] S. Martínez Ruiz and J. Ballester i Gilbert, “Temperament in bach’s well-tempered clavier - a historical survey and a new evaluation according to dissonance theory,” July 2011. 

- [9] W. McCarty, Humanities Computing. Basingstoke: Palgrave Macmillan, 2005. 

- [10] M. S. Cuthbert and C. Ariza, “Music21: A toolkit for computer-aided musicology and symbolic music data,” in Proceedings of the 11th International Society for Music Information Retrieval Conference (ISMIR 2010), Utrecht, Netherlands, 2010, pp. 637– 642. [Online]. Available: http://ismir2010.ismir.net/ proceedings/ISMIR2010.pdf 

- [11] C. Ariza and M. S. Cuthbert, “Modeling beats, accents, beams, and time signatures hierarchically with music21 meter objects,” in Proceedings of the International Computer Music Conference, New York, 2010, pp. 216–223. [Online]. Available: http: //mit.edu/music21/papers/2010MeterObjects.pdf 

- [12] D. J. Wales and J. P. Doye, “Global optimization by basin-hopping and the lowest energy structures of lennard-jones clusters containing up to 110 atoms,” The Journal of Physical Chemistry A, vol. 101, no. 28, pp. 5111–5116, 1997. 

- [13] R. Storn and K. Price, “Differential evolution–a simple and efficient heuristic for global optimization over continuous spaces,” Journal of global optimization, vol. 11, pp. 341–359, 1997. 

- [14] Y. Xiang, D. Sun, W. Fan, and X. Gong, “Generalized simulated annealing algorithm and its application to the thomson model,” Physics Letters A, vol. 233, no. 3, pp. 216–220, 1997. 

- [15] P. Virtanen, R. Gommers, T. E. Oliphant, M. Haberland, T. Reddy, D. Cournapeau, E. Burovski, P. Peterson, W. Weckesser, J. Bright, S. J. van der Walt, M. Brett, J. Wilson, K. J. Millman, N. Mayorov, A. R. J. Nelson, E. Jones, R. Kern, E. Larson, C. J. Carey, ˙I. Polat, Y. Feng, E. W. Moore, J. VanderPlas, D. Laxalde, J. Perktold, R. Cimrman, I. Henriksen, E. A. Quintero, C. R. Harris, A. M. Archibald, A. H. Ribeiro, F. Pedregosa, and P. van Mulbregt, “Scipy 1.0: Fundamental algorithms for scientific computing in python,” Nature Methods, vol. 17, no. 3, pp. 261–272, 2020. [Online]. Available: https://doi.org/10.1038/s41592-019-0686-2 

- [16] M. J. D. Powell, “A direct search optimization method that models the objective and constraint functions by linear interpolation,” in Advances in Optimization and Numerical Analysis, S. Gomez and J.-P. Hennart, Eds. Dordrecht: Springer, 1994, pp. 51–67. 

- [17] A. P. Piotrowski, “Review of differential evolution population size,” Swarm and Evolutionary Computation, vol. 32, pp. 1–24, 2017. [Online]. Available: https://www.sciencedirect.com/science/article/ pii/S2210650216300268 

- [18] C. L. Krumhansl and E. J. Kessler, “Tracing the dynamic changes in perceived tonal organization in a spatial representation of musical keys,” Psychological Review, vol. 89, no. 4, pp. 334–368, 1982. 

- [19] C. L. Krumhansl, Cognitive Foundations of Musical Pitch. New York, NY: Oxford University Press, 1990. 

- [20] H. Kelletat, Zur musikalischen Temperatur insbesondere bei Johann Sebastian Bach. Kassel: J.G. Oncken Verlag, 1960. 

509 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [21] J. De Bie, “Historische orgelstemmingen: theorie & realiteit: Een onderzoek naar het gebruik van historische orgelstemmingen in vlaanderen, met een algemeen overzicht van de stemmingstheorie,” Diss. doct. kunstgeschiedenis en oudheidkunde: musicologie, Universiteit Gent, Gent, Belgium, 2004. [Online]. Available: http://lib.ugent.be/catalog/rug01:002001538 

- [22] J. P. Kirnberger, Johann Philipp Kirnbergers Clavierübungen mit der Bachischen Applicatur, in eine Folge von den leichtesten bis zu den schwersten Stücken. Berlin: bey Friedrich Wilhelm Birnstiel, Königl. privilegirten Buchdrucker, 1766, vol. Vierte Sammlung. 

- [23] ——, Die Kunst des reinen Satzes in der Musik, 1st ed. Berlin: In Commission bey Christian Friedrich Boß, 1771, vol. 1er Theil. 

- [24] J. P. Kirnberger and H. Bellermann, “Briefe von kirnberger an forkel (mitgetheilt von h. bellermann) (fortzetzung: Iii),” Allgemeine musikalische Zeitung, vol. VI, no. 36, pp. 565–572, September 1871. 

- [25] H.-J. Schulze, Bach-Dokumente, W. Neumann, Ed. Leipzig: Bärenreiter Kassel, Basel, Tours, London VEB Deutscher Verlag für Musik Leipzig, 1972, vol. Band III: Dokumente zum nachwirken Johann Sebastian Bachs 1750-1800. 

- [26] A. Werckmeister, Hypomnemata Musica oder musicalisches Memorial. Quedlinburg: In Verlegung Theodri Philippi Calvisii: Georg Olms Verlag, Hildesheim, 2015 Ausg., 1697. 

- [27] J. G. Neidhardt, Beste und leichteste Temperatur des Monochordi. Jena: Bey Johann Bielcken, 1706. 

   - [34] R. Böß, Die ungleichschwebende Originalstimmung von Johann Sebastian Bach: Das Wohltemperirte Clavier. Frankfurt am Main: Peter Lang, 2009. 

   - [35] E. Jobin, “Bach et le clavier bien tempéré, par emile jobin,” Retrieved March 25, 2025, from https: //www.clavecin-en-france.org/spip.php?article52, 2020–2025. 

   - [36] J. C. Francis, “Bach’s well tempered tuning,” Retrieved March 25, 2025, from https://www.eunomios. org/contrib/francis6/francis6.pdf, February 2011. 

   - [37] B. Lehman, “Bach’s extraordinary temperament: our rosetta stone,” Early Music, pp. 3–23 and 211–231, February and May 2005. 

   - [38] H. A. Kellner, Wie stimme ich selbst mein Cembalo?, 3rd ed., ser. Schriftenreihe Das Musikinstrument, Heft 19. Frankfurt am Main: Verlag Erwin Bochinsky, 1986. 

   - [39] K. Wegscheider, “Mit reinem herzen - reine terzen,” Retrieved March 25, 2025, from https://www.wegscheider.eu/storage/app/media/ Tannenbergvortrag%202004%20USA.pdf, March 2004. 

   - [40] J. Reinhard, Bach and Tuning, ser. Sources and Studies in Music History from Antiquity to the Present, Volume 47, E. Antokoletz and M. Albrecht, Eds. Frankfurt am Main: Peter Lang, 2016. 

   - [41] M. Tessmer, “Wie war bachs wohltemperiertes klavier gestimmt?” Acta Organologica, p. 194, 1994. 

   - [42] B. Billeter, Anweisung zum Stimmen von Tasteninstrumenten. Berlin, Kassel: Merseburger Verlag, 2010. 

- [28] J. P. Rameau, Génération harmonique. Paris: Chez Prault fils, 1737. 

- [29] J. N. Forkel, Ueber Johann Sebastian Bachs Lebens, Kunst und Kunstwerke. Leipzig: Bey Hoffmeister und Kühnel, 1802. 

- [30] C. P. E. Bach, Versuch über die wahre Art das Clavier zu spielen, 1st ed. Berlin: Königl. Hof-Buchdrucker Christian Friedrich Henning, 1753. 

- [31] B. Fritz, Anweisung, wie man Claviere, Clavecins, und Orgeln, nach einer mechanischen Art, in allen zwölf Tönen gleich rein stimmen könne, daß aus solchen allen sowohl dur als moll wohlklingend zu spielen sey, 2nd ed. Leipzig: Johann Gottlob Immanuel Breitkopf, 1757. 

- [32] R. H. M. Bosanquet and R. Rasch, On the Mathematical Theory of Temperament. Unknown, 1876, cited as Bosanquet & Rasch 1876, p. 29f. 

- [33] A. Sparschuh, “Stimm-arithmetik des wohltemperierten klaviers von j.s. bach,” in Deutsche Mathematikervereinigung Jahrestagung, 1999, pp. 154–155. 

510 

