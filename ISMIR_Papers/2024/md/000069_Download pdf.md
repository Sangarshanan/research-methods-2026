---
paper_id: "000069"
year: 2024
title: "Download pdf"
source_url: "https://zenodo.org/record/14877411/files/000069.pdf"
---

# A KALMAN FILTER MODEL FOR SYNCHRONIZATION IN MUSICAL ENSEMBLES 

Hugo T. Carvalho<sup>1∗</sup> Min S. Li<sup>2</sup> Massimiliano di Luca<sup>3</sup> Alan M. Wing<sup>3</sup> 1 Department of Statistical Methods, Federal University of Rio de Janeiro, Brazil 

2 Bristol Interaction Group, School of Computer Science, University of Bristol, United Kingdom 3 Virtual Reality Lab, School of Psychology, University of Birmingham, United Kingdom 

> ∗ Corresponding author: `hugo@dme.ufrj.br` 

## ABSTRACT 

The synchronization of motor responses to rhythmic auditory cues is a fundamental biological phenomenon observed across various species. While the importance of temporal alignment varies across different contexts, achieving precise temporal synchronization is a prominent goal in musical performances. Musicians often incorporate expressive timing variations, which require precise control over timing and synchronization, particularly in ensemble performance. This is crucial because both deliberate expressive nuances and accidental timing deviations can affect the overall timing of a performance. This discussion prompts the question of how musicians adjust their temporal dynamics to achieve synchronization within an ensemble. This paper introduces a novel feedback correction model based on the Kalman Filter, aimed at improving the understanding of interpersonal timing in ensemble music performances. The proposed model performs similarly to other linear correction models in the literature, with the advantage of low computational cost and good performance even in scenarios where the underlying tempo varies. 

## 1. INTRODUCTION 

Synchronization of motor responses to rhythmic auditory cues represents a biological phenomenon found across various species [1], and social collectives often engage in activities necessitating precise temporal coordination among members, a crucial factor for successful group endeavors. For example, in scenarios such as rowing eights, temporal alignment may not be the primary focus, but individual timing remains tied to collective timing dynamics [2]. In domains like musical performances, achieving precise temporal synchronization serves as a prominent goal [3]. 

Typically, musicians do not adhere strictly to the exact timing of note onsets as indicated in the musical score: due to expressiveness, they often introduce deviations from the 

> © H. T. Carvalho, M. S. Li, M. di Luca, and A. M. Wing. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: H. T. Carvalho, M. S. Li, M. di Luca, and A. M. Wing, “A Kalman Filter model for synchronization in musical ensembles”, in Proc. of the 25th Int. Society for Music Information Retrieval Conf., San Francisco, United States, 2024. 

prescribed timing [4]. These fluctuations require a high level of control over relative timing, where the phase of notes produced by the musician deviating from the timing aligns differently with the phases of other musicians. Rehearsals often involve reaching a consensus on expressive variations, ensuring that timing deviations are synchronized among players while maintaining relative timing [5]. Nevertheless, even with a unified understanding of the musical interpretation, individual musicians may opt to vary the timing of note onsets in specific passages between different performances [5,6]. Musical performance timing is also susceptible to inadvertent variations due to factors such as rhythmic intricacies, technical demands beyond timing (e.g., pitch, volume), lapses in concentration, and the inherent variability of biological timing [7]. While extensive individual practice can mitigate some of these unintended variations, complete elimination is unlikely. 

The previous discussion raises the inquiry: how do musicians within an ensemble modulate their temporal dynamics to achieve synchronization with one another? In this paper a novel feedback correction model is presented, based on the Kalman Filter and aimed at improving timing accuracy in ensemble music performances. The proposed model generalizes the linear autoregressive model in [8] with the improvement of allowing two important quantities, the phase and period correction gains, to vary along time, since it makes the model suitable to describe synchronization in scenarios where the underlying tempo greatly varies (a realistic case in ensemble performance). 

The paper is organized as follows: Section 2 recalls some linear models for synchronization, and the dynamic generalization of the model in [8] is presented, which is formulated as a Kalman Filter in Section 4; the fundamentals of the Kalman Filter are briefly recalled in Section 3; the computational experiments are shown and discussed in Section 5; conclusions are presented in Section 6. Directions for future work are identified throughout the paper. 

## 2. LINEAR MODELS FOR ENSEMBLE SYNCHRONIZATION 

The starting point for contextualizing the proposed model is [9], where a phase-correction model is presented as a method for an individual performer to achieve synchrony with a periodic metronome click or with another performer 

618 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

(see also [10]). The fundamental concept revolves around utilizing the asynchrony, termed as a phase error, between a tone onset and the metronome click (or between two tone onsets produced by different performers) in a feedback mechanism, that guides the performer to adjust the time interval preceding the next tone onset. Consequently, the performer either decreases or increases the interval leading up to the subsequent tone onset proportionally to the preceding asynchrony. This process aims to achieve greater synchrony (“in phase”) between the next tone onset and the metronome click (or pair of tone onsets). This synchronization scheme can be represented by Equation (1): 



<!-- Start of picture text -->
tn = tn−1 + Tn − αAn−1 + εn, (1)<br><!-- End of picture text -->

where tn and tn−1 represent the current and previous observed tone onset event times respectively, Tn denotes the time interval generated by an internal timekeeping mechanism, α is the phase correction strength or phase correction gain, An−1 refers to the asynchrony of the previous onset event, and εn represents a random error term, which includes the internal timekeeper noise. The complete reduction of asynchrony to zero hinges on the value assigned to the gain, α, since this parameter determines the proportion of the preceding phase error that the performer endeavors to eliminate. 

Following [11], period correction can also be incorporated in the model in Equation (1), by imposing that 



<!-- Start of picture text -->
Tn = Tn−1 − βAn−1, (2)<br><!-- End of picture text -->

where β is the period correction strength or period correction gain. Phase correction involves a local, within-cycle adjustment to the timing, while period correction entails a more enduring alteration to the underlying tempo, influencing subsequent cycles as well. Phase correction typically occurs automatically, without the need for conscious awareness of synchronization discrepancies. However, period correction appears to be more cognitively demanding, relying on the conscious detection of tempo variations in the external rhythm [12,13]. 

As previously mentioned, Equations (1) and (2) model the asynchrony correction of an individual tapping according to a periodic metronome, or between two individuals tapping together. In [8] it is argued that the same modeling framework is also suited to describe synchronization in music ensemble performance, where a specific musician now tries to reduce asynchrony between him/her and every other performer. Therefore, Equations (1) and (2) can be jointly generalized to an ensemble of K performers as: 



<!-- Start of picture text -->
K<br>ti,n = ti,n−1 + Ti,n − � αijAij,n−1 + εi,n (3)<br>i=1<br>j̸=i<br><!-- End of picture text -->



<!-- Start of picture text -->
K<br>Ti,n = Ti,n−1 − � βijAij,n−1, (4)<br>i=1<br>j̸=i<br><!-- End of picture text -->

where i = 1, . . . , K indicate a specific performer, ti,n and ti,n−1 are respectively the current and previous ob- 

served tone onset event times for player i, Ti,n is the timekeeper interval for player i at time instant n, Aij,n−1 = (ti,n−1 − tj,n−1) is the asynchrony at the time instant n−1 between players i and j, αij and βij are respectively the phase and period correction gain applied by player i to compensate for Aij,n−1, and εi,n is a noise term identified with the internal timekeeper. Estimation of the values of αij and βij can be performed using the bounded Generalized Least Squares method (bGLS) [14,15]. 

In [8], the model in Equation (3) is implemented and largely investigated for the case of a string quartet ensemble playing a homophonic section from the string quartet Op. 74 no. 1 by Joseph Haydn (fourth movement, bars 13–24), as this part has a steady tempo and all player’s quarter notes are aligned. In [14] the coupling of Equations (3) and (4) is investigated, with a simulated string quartet data with mild tempo changes, and the bGLS algorithm is shown to be capable of recovering the values of α and β. However, due to the nature of the bGLS algorithm, the authors point out that many data points are necessary for robust estimation of these variables, which may not be available or is an unrealistic aim in the case of a real-time implementation of the correction model (eg. for a virtual reality musical ensemble). In [16] the ADAM model (ADaptation and Anticipation Model) is proposed, including not only correction terms but also anticipatory ones, and in [17] this model is tested with tempo-changing tapping data, but since there is no adaptation of the bGLS algorithm to this new set of equations, the parameter estimation is done by exhaustive search, which is infeasible for real-life applications. Moreover, due to the nature of its parameters, the ADAM model is non-identifiable, meaning that more than one configuration of the parameters leads to the same estimate. 

In order to circumvent the aforementioned issues, an alternative is to consider not a single value of α and β for each pair of performers through time, but time-dependent correction gains. Developing this intuition, a dynamic αij allows that a performer changes the phase correction at each onset, and a dynamic βij would allow him/her to correct differently for tempo variations during the performance of an excerpt. To model a dynamic variable, a good balance between simplicity and accuracy is a random walk, and in this case phase and period correction occur according to Equations (3) and (4), respectively, but with additional equations to allow the evolution of both correction gains. This new model is summarized in Equations (5), (6), (7), and (8): 



<!-- Start of picture text -->
K<br>ti,n = ti,n−1 + Ti,n − � αij,nAij,n−1 + εi,n (5)<br>i=1<br>j̸=i<br><!-- End of picture text -->



<!-- Start of picture text -->
K<br>Ti,n = Ti,n−1 − � βij,nAij,n−1 (6)<br>i=1<br>j̸=i<br><!-- End of picture text -->



<!-- Start of picture text -->
αij,n = αij,n−1 + wij,n (α) (7)<br><!-- End of picture text -->



<!-- Start of picture text -->
βij,n = βij,n−1 + wij,n (β) , (8)<br><!-- End of picture text -->

619 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

where wij,n<sup>(α)andw</sup> ij,n<sup>(β)areindependentzero-meanGaus-</sup> sian random variables, allowing the evolution of αij,n and βij,n through time, respectively (notice the novel subscript “n” in both αij and βij). 

However, in the model proposed in Equations (5), (6), (7), and (8), it is not clear how to employ the bGLS method to obtain estimate of the variables of interest, and two distinct paths can now be followed: generalize the bGLS algorithm to this new situation, or resort to estimation techniques within the theory of dynamic models [18]. This work follows the latter, adopting the Kalman Filter as a framework to analyze Equations (5), (6), (7), and (8), due to its balance between flexibility and simplicity, as well as its simple and highly interpretable update equations. Section 3 recalls the basics of the Kalman Filter and Section 4 formulates the proposed model in this scenario. 

The KF dynamically estimates variables θn and yn based on observations up to time n − 1, and updates the estimate of θn when the observation at time n is available. This process is done accordingly to Equations (11), (12) and (13), called the filtering equations:<sup>2</sup> 

Prediction step for hidden variables: 



<!-- Start of picture text -->
θn|y1:n−1 ∼ N (an, Rn) (11)<br><!-- End of picture text -->

Prediction step for observed variables: 



<!-- Start of picture text -->
yn|y1:n−1 ∼ N (fn, Qn) (12)<br><!-- End of picture text -->



<!-- Start of picture text -->
Update step (compare predictions to measurements):<br>θn|y1:n ∼ N (kn, Cn), (13)<br><!-- End of picture text -->

where<sup>3</sup> 



<!-- Start of picture text -->
an = Gnkn−1 (14)<br><!-- End of picture text -->



<!-- Start of picture text -->
Rn = GnCn−1G T n + Wn (15)<br><!-- End of picture text -->

## 3. A BRIEF RECALL ON THE KALMAN FILTER 

The Kalman Filter (KF) was developed in the 1960’s, and served originally as a way to produce accurate estimates of variables of interest (eg. position of an object) by reaching a consensus between physical models and noisy measurements [19]. More generally, the KF can be seen as a statespace dynamic model, employed to describe more general time-series as a dynamic linear regression model as function of an underlying Markov model [18]. 

The main contribution of this paper is to propose the model in Equations (5), (6), (7), and (8), and formulate it as a KF, employing its filtering and smoothing equations to estimate the phase and period correction gains through time. The choice of a KF to achieve this goal are: linear nature of the model in Equations (5), (6), (7), and (8), high interpretability of the KF and its update equations, and potential low computational cost of its implementation. 

The notation and basic equations of the KF are now briefly recalled, following [18]. In what follows, the index n ranges from 1 to N . Let yn ∈ R<sup>m</sup> be a sequence of observed variables (or measurements), and θn ∈ R<sup>p</sup> be a sequence of unobserved vectors, which are called the hidden (or state) variables. The KF model assumes that these two entities are related by Equations (9) and (10): 



<!-- Start of picture text -->
yn = Fnθn + vn (9)<br><!-- End of picture text -->



<!-- Start of picture text -->
θn = Gnθn−1 + wn, (10)<br><!-- End of picture text -->

where Fn ∈ R<sup>m×p</sup> and Gn ∈ R<sup>p×p</sup> are sequences of known matrices (observation model and the statetransition model, respectively). Vectors vn ∈ R<sup>m</sup> and wn ∈ R<sup>p</sup> are independent observation and process noise terms, respectively, and it is assumed that they follow Gaussian probability distributions, that is, vn ∼ N (0, Vn) and wn ∼ N (0, Wn),<sup>1</sup> where Vn ∈ R<sup>m×m</sup> and Wn ∈ R<sup>p×p</sup> are sequences of known covariance matrices of the observation and process noise terms respectively. 

> 1 The symbol ∼ means “follows the probability distribution”, and N (µ, Σ) denotes a multivariate Gaussian distribution with mean vector µ and covariance matrix Σ. The dimension of the support of the random vector is omitted, and compatibility between dimensions of µ and Σ is always assumed. 



<!-- Start of picture text -->
fn = Fnan (16)<br><!-- End of picture text -->



<!-- Start of picture text -->
Qn = FnRnF T n + Vn (17)<br><!-- End of picture text -->



<!-- Start of picture text -->
kn = an + �RnF T n Q− n 1 � en (18)<br><!-- End of picture text -->



<!-- Start of picture text -->
en = yn − fn (19)<br><!-- End of picture text -->



<!-- Start of picture text -->
Cn = Rn − �RnF T n Q− n 1 � FnRn, (20)<br><!-- End of picture text -->

assuming that the initial state is chosen according to a normal distribution, that is, θ0 ∼ N (k0, C0). For more details on the KF, see [18,19]. 

One of the appealing aspects of the KF is its ability to perform estimation and forecasting sequentially, as new data emerge. However, if observations yn for n = 1, . . . , N are available beforehand, one is also able to retrospectively reconstruct the system’s states, in order to analyze its behavior given all the observations. For this purpose, a backward-recursive algorithm can be employed to compute the conditional distributions of θn given y1:N , for any n < N [18,19]. The main ingredient of this algorithm is the smoothing equation (21): 



<!-- Start of picture text -->
θn|y1:N ∼ N (sn, Sn), (21)<br><!-- End of picture text -->

where 



<!-- Start of picture text -->
sn = kn + CnG T n+1 R− n+1 1 [sn+1 − an+1] (22)<br>Sn = Cn − CnG T n+1 R− n+1 1 ×<br>[Rn+1 − Sn+1] R − n+1 1 Gn+1Cn, (23)<br><!-- End of picture text -->

assuming that θn+1|y1:N ∼ N (sn+1, Sn+1). Notice that since the smoothing is performed backwards, it is necessarily to previously filter the set of observations to gain access to vectors kn and an, and matrices Cn and Rn. 

## 4. KALMAN FILTER MODEL FOR ENSEMBLE SYNCHRONIZATION 

Equations (5), (6), (7), and (8) can be written as a KF by considering proper choices for the observed and hidden 

> 2 The conditional distribution of u given z is denoted by u|z, and i : j means “observations from time instants i to j”, both extremes included. 

> 3 The superscript T after a vector or matrix denotes its transpose; the superscript<sup>−1</sup> after a matrix denotes its inverse. 

620 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

variables, as well as the observation and state-transition matrices. The main goal of this section is to construct a sequence of matrices Fn and Gn, as well as vectors yn and θn of observed and hidden variables respectively, such that Equations (9) and (10) recover the model proposed in Equations (5), (6), (7), and (8). Firstly, to simplify the formulation of the model, the observed variables are not the tone onset times for each player, but rather the interonset-intervals (IOIs), denoted by ri,k = ti,n − ti,n−1, for i = 1, . . . , K. These values are assembled as in Equation (24): 



<!-- Start of picture text -->
yn = [r1,n . . . rK,n] ∈ R K . (24)<br><!-- End of picture text -->

The hidden variable θn can be written as in Equation (25): 



<!-- Start of picture text -->
θn = �T T n �� rnT �� αnT �� βnT �T ∈ R2K2 , (25)<br><!-- End of picture text -->

where 



<!-- Start of picture text -->
Tn = [T1,n . . . tK,n] T ∈ R K (26)<br><!-- End of picture text -->



<!-- Start of picture text -->
rn = [r1,n . . . rK,n] T ∈ R K (27)<br><!-- End of picture text -->



<!-- Start of picture text -->
αn = [αij,n in the lexicographical order on ij,<br><!-- End of picture text -->



<!-- Start of picture text -->
for 1 ≤ i, j ≤ K, i̸ = j] ∈ R K(K−1) (28)<br><!-- End of picture text -->



<!-- Start of picture text -->
βn = [βij,n in the lexicographical order on ij,<br>for 1 ≤ i, j ≤ K, i̸ = j] ∈ R K(K−1) . (29)<br><!-- End of picture text -->

The relation between θn and yn is described by the observation matrix in Equation (30):<sup>4</sup> 



<!-- Start of picture text -->
Fn = �0K �� IK �� 0K×K(K−1) �� 0K×K(K−1)� . (30)<br><!-- End of picture text -->

Notice that matrices Fn ∈ R<sup>K×2K2</sup> are constant through time. The evolution of the hidden variables in θn is modelled by a sequence of state-transition matrices Gn ∈ R<sup>2K2×2K2</sup> , described in Equation (31): 



<!-- Start of picture text -->
 IIKK 00KK 0K×GK rα n(K−1) GG T β n rβ n <br>0K(K−1)×K 0K(K−1)×K IK(K−1) 0K(K−1)<br>0K(K−1)×K 0K(K−1)×K 0K(K−1) IK(K−1) , (31)<br><!-- End of picture text -->

where matrices G<sup>T β</sup> n<sup>, Grα</sup> n<sup>, and Grβ</sup> n<sup>(of dimensions K×</sup> K(K − 1) each) describe the interaction between variables in their respective superscripts. These three matrices are equal to the matrix in Equation (32): 



<!-- Start of picture text -->
−A T · · ·<br>1:,n−1 01×(K−1) 01×(K−1)<br> −A T · · · <br>01×(K−1) 2:,n−1 01×(K−1)<br>(32)<br>... ... ... ...<br>· · · −A T<br>01×(K−1) 01×(K−1) K:,n−1 ,<br><!-- End of picture text -->

where each Ai:,n−1 ∈ R<sup>K−1</sup> contain the asynchronies Aij,n−1 of player i to all players j, for j̸ = i, at time n − 1. Vector Ai:,n−1 is made explicit in Equation (33): 



<!-- Start of picture text -->
� Ai1,n−1 . . . Ai(i−1),n−1Ai(i+1),n−1 . . . AiK,n−1�T. (33)<br><!-- End of picture text -->

4 The identity matrix of dimensions L×L is denoted by IL; the matrix of dimensions L × M filled with zeros is denoted by 0L×M ; a square null matrix of dimensions L × L is abbreviated by 0L. 

A simple (but tedious) verification using Equations (9) and (10) with these choices for Fn, Gn, yn, and θn ensures that the model in Equations (5), (6), (7), and (8) is recovered. It is also established that when K = 1 the model in Equations (1) and (2) is recovered, with the improvement of dynamic α and β. 

When compared to the bGLS algorithm [14, 15], the state-of-the-art to estimate parameters in the scenario of sensorimotor synchronization, the KF model presents a great advantage, that is the possibility of performing online estimation as more data become available: this feature can be important if one desires to implement real-time synchronization schemes. When the complete time-series of onset times/IOIs is available, one can apply the smoothing equation (21), in order to dynamically estimate the parameters of interest throughout the performance, as well as estimate them by applying the filtering equations (11), (12), and (13), for example, to simulate an online scenario. 

Notice that the dimensions of Fn, Gn, and θn scale quadratically with the number of performers, which may render the model overly complicated or cause computational issues when computing the KF update/filtering equations.<sup>5</sup> However, due to the sparsness of matrices Fn and Gn, block-multiplication will highly reduce the number of operations when computing Equations (14) to (20), mitigating the latter issue. Regarding the complexity of the model, notice that in real large-scale scenarios (eg. a symphony orchestra) it is not realistic to assume that each musician synchronizes with every other, thus allowing for potential simplifications, like considering a group of instruments as a single unity and synchronizing with every other group. This procedure would diminish the value of K from approximately 100 to less than 20. A useful topic for future research would be to investigate the possibility of modeling the synchronization scheme between performers (or group of performers) in a graph, in order to decrease even more the number of relevant connections. 

Another issue that is important to point out is the design of the covariance matrices for the observation and process noises, Vn and Wn respectively. On a first view, it makes sense to consider Vn as diagonal matrices, for simplicity, since the interaction between the performers is already “captured” by the correction gains in the hidden variables; however, it is not clear if Wn should be a sequence of diagonal matrices, since it makes sense to consider at least correlations between both correction gains of the same performer. This work employs a particular choice for these covariance matrices, as will be further discussed in Section 5. Further investigation on this question could involve coupling the Expectation-Maximization algorithm with the KF in order to estimate not only matrices Vn and Wn but also Fn and Gn [20]. However a disadvantage would be that these estimates would need to be static through time, requiring a large amount of data, and being highly dependent of the piece of music being analyzed. 

> 5 Other computational issues on the Kalman Filter are largely discussed in [18]. 

621 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 



<!-- Start of picture text -->
Deadpan Normal Speed<br>0.3 0 0.3 0 0.3 0<br>0.2 5 0.2 5 0.2 5<br>0.2 0 0.2 0 0.2 0<br>12 12 12<br>13 13 13<br>0.1 5 0.1 5 0.1 5<br>14 14 14<br>0 10 20 30 40 0 10 20 30 40 0 10 20 30 40<br>0.3 0 0.3 0 0.3 0<br>0.2 5 0.2 5 0.2 5<br>0.2 0 0.2 0 0.2 0<br>21 21 21<br>23 23 23<br>0.1 5 0.1 5 0.1 5<br>24 24 24<br>0 10 20 30 40 0 10 20 30 40 0 10 20 30 40<br>0.3 0 0.3 0 0.3 0<br>0.2 5 0.2 5 0.2 5<br>0.2 0 0.2 0 0.2 0<br>31 31 31<br>32 32 32<br>0.1 5 0.1 5 0.1 5<br>34 34 34<br>0 10 20 30 40 0 10 20 30 40 0 10 20 30 40<br>0.3 0 0.3 0 0.3 0<br>0.2 5 0.2 5 0.2 5<br>0.2 0 0.2 0 0.2 0<br>41 41 41<br>42 42 42<br>0.1 5 0.1 5 0.1 5<br>43 43 43<br>0 10 20 30 40 0 10 20 30 40 0 10 20 30 40<br>IOI IOI IOI<br><!-- End of picture text -->

Figure 1. Smoothed time-series for the phase correction gain on three performance styles of an excerpt of the fourth movement of the string quartet Op. 74 no. 1, by Joseph Haydn. See Section 5 for discussion. 

## 5. RESULTS 

To illustrate the effectiveness of the proposed model, a set of simulations was performed, using an excerpt of the dataset presented in [21], similar to the one used in [8]: the homophonic section from the fourth movement of the string quartet Op. 74 no. 1 by Joseph Haydn, from bars 13 to 24. In this excerpt the instruments play a sequence of 47 quarter notes in rhytmic unison, with the first violin breaking the pattern near the end with an adornment of four sixteenth notes, which are disregarded in this study. 

Three performance styles are considered: Normal condition (concert-style performance); Speed condition (including a spontaneous accelerando and ritardando initiated by a single musician – the designated leader, that can be the first or second violin); and Deadpan condition (performances with minimal expression in tempo and articulation). All the simulation were performed on a computer equipped with a 12th Generation Intel Core™i7 processor and 16GB of RAM, running Windows 11 Pro™; the implementations were conducted in Python version 3.11.7.<sup>6</sup> 

Regarding the parameters of the KF, the covariance matrix for the process noise, Wn, plays an important role, since it indicates how the variables in θ interact. Based on the interpretation of the hidden variables, a reasonable choice for all the Wn is the block-diagonal matrix in Equation (34):<sup>7</sup> 



<!-- Start of picture text -->
W (T ) W r <br>(34)<br>W α<br> W β  ,<br><!-- End of picture text -->

where W<sup>(T )</sup> and W<sup>r</sup> are given respectively by σT<sup>2IKand</sup> σr<sup>2IK,beingσ</sup> T<sup>2thetimekeepervarianceandσ</sup> r<sup>2themo-</sup> tor variance. Since it is known that the motor variance is way smaller than the timekeeper variance [8, 14, 15], the conservatively high values σT<sup>2=500andσ</sup> r<sup>2=25</sup> were considered. Both W<sup>α</sup> and W<sup>β</sup> are also blockdiagonal matrices, consisting of K blocks, each of dimen- 

> 7 Off-diagonal blocks are null matrices, that were omitted exceptionally here, to avoid a line-break in the number of the equation. Moreover, notation W<sup>(T )</sup> means to avoid confusion with the transpose matrix. 

6 Codes available at https://github.com/arme-project/ismir-2024. 

622 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

sions (K − 1) × (K − 1) and as in Equation (35): 



<!-- Start of picture text -->
v c · · · c<br>c v · · · c<br>(35)<br>... ... ... ...<br>c c · · · v ,<br><!-- End of picture text -->

where v represents the variance of each αij (or βij) and c is the covariance between two distinct αij (or βij). 

The rationale behind this construction for W<sup>α</sup> and W<sup>β</sup> is that it makes sense to assume that for performer i there is a correlation only between the αij (or βij) for j̸ = i. This means that all the correction gains for performer i interact among themselves, but not directly with the correction gains of other performers. Also, it is expected that the correlation between two distinct αij (or βij) is negative, since increasing correction towards a specific performer may cause a decrease of the synchronization towards the others. With this in mind, for matrix W<sup>α</sup> the value of v was chosen as 10<sup>−4</sup> ; the value of c was chosen such that the correlation between any two distinct αij is equal to −0.1.<sup>8</sup> 

In this preliminary set of experiments with the KF, the effect of the βij was disregarded, by considering W<sup>β</sup> a null matrix. It is known that the effect of the phase correction is way more relevant than the effect of the period correction [8, 14, 15], with the βij coefficients being usually much smaller than the αij. Also, preliminary experiments with artificial data also indicate that the dynamic values of the phase correction may render the period correction unnecessary. Since this is a point to be further investigated, it seemed safe to first experiment only with phase correction. 

Matrices Vn were chosen to be constant and equal to 10<sup>−5</sup> IK: since the block W<sup>r</sup> in matrix Wn already captures the motor variance, Vn should be a sequence of null matrices, but a negligible diagonal term was added to avoid numerical errors. Finally, the initialization of vector θ was done by choosing its first K components and the components from K + 1 to 2K to be equal to the first IOI of each of the K instruments, all the αij were initially set to 0.25, and all the βij to zero. This initialization of αij is supported by [8], where optimal correction values for ensembles of size K were derived. 

Figure 1 summarizes one experiment performed in the aforementioned scenario. Three repetitions of the Haydn quartet excerpt were analyzed, being one for each of the three performance conditions, having the second violin as the leader in the “Speed” case. Each performance consists of a sequence of 46 four-dimensional vectors containing the IOIs for each instrument. Since it is not the goal of this set of experiments to evaluate online performance of the proposed model, these three sequences were smoothed by the KF,<sup>9</sup> according to Equation 21. Each panel of Figure 1 displays the evolution of the αij, for j̸ = i, organized as follows: each column contains a performance condition (made explicit at its top), and each row displays the evolution of αij for j̸ = i and a fixed value of i. The condi- 

> 8 This procedure will not always lead to a positive-definite matrix, for sufficiently high value of K and depending on c – not the case here. 

> 9 The computational time of each smoothing is less than 100ms. 

tioning of each αij on y1:N is omitted, and the instruments are abbreviated by numbers, where 1, 2, 3, and 4 refers to the first violin, second violin, viola, and cello, respectively. On each panel of Figure 1 the values of αij promptly deviates from the optimal initialization of 0.25 (but still varies around it), and their respective behavior are now discussed. 

In “Speed” condition (third column in Figure 1), on each panel the phase correction parameter toward the second violin (αi2, for i = 1, 3, 4) shows a small increase by the end of the performance, when the change in speed occurs, since the second violin is assigned as the leader to initiate this change in speed. Notice also that his/her phase correction parameters towards the other performers (α2j, for j = 1, 3, 4) decrease through time, specially near the last notes, reinforcing its leadership in this tempo change. 

In the “Normal” condition (second column in Figure 1) it is noticeable that the second violin, viola, and cello are systematically synchronizing mainly to the first violin, which plays the melody in this excerpt: notice the almost constant value for αi1, for i = 2, 3, 4. While the cello is synchronizing mainly with the first and second violin, it presents the weaker “synchronization attractor”, as seen by the significant decrease in αi4 through time, for i = 1, 2, 3. 

Finally, in the “Deadpan” condition (first column in Figure 1) the first and second violin and the cello are synchronizing mainly to the viola (steady increase of αi3 for i = 1, 2, 4, and decrease in α3j for j = 1, 2, 4), which may be the cause of the cello synchronizing systematically with all the three other instruments. 

This experiment indicates that the proposed model is capable of capturing local fluctuations in tempo, reinforces the role of the phase correction gain in interpreting synchronization mechanisms in musical ensembles, and assess qualitatively the validity of a time-varying model to the problem of ensemble synchronization. As a next step in this new direction for the field, the proposed model will be broadly tested and systematically compared with other models. Some issues to be addressed in future work are: perform experiments with other data contained on [21]; compare filtering and smoothing procedures, as well as investigate if the filtered estimates make sense from a music cognition perspective; implement tools from the theory of dynamic linear models to automatically estimate the covariance matrices Vn and Wn [18]; perform a systematic comparison with the bGLS and ADAM algorithms. 

## 6. CONCLUSION 

This paper presented a novel model, based on the Kalman Filter, for analysing asynchrony correction in music ensemble performances. The proposed model is founded on well-established models in the literature, and has the advantage of considering dynamic phase and period correction gains. A set of experiments (using only phase correction) on a homophonic section of a string quartet by J. Haydn was conducted, illustrating the capabilities of the model in explaining synchronization schemes within musical ensembles. 

623 

## Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

## 7. ACKNOWLEDGMENTS 

The ARME Project (Augmented Reality Music Ensemble – https://arme-project.co.uk/) is funded by the EPSRC grant with reference EP/V034987/1. We would like to thank the University of Birmingham for the scholarship awarded to the first author through the Brazil Visiting Fellows Scheme. We also would like to thank the reviewers and meta-reviewers for the useful insights and suggestions to improve this paper. 

## 8. REFERENCES 

- [1] A. D. Patel, J. R. Iversen, M. R. Bregman, and I. Schulz, “Experimental evidence for synchronization to a musical beat in a nonhuman animal,” Current Biology, vol. 19, no. 10, pp. 827–830, 2009. 

- [2] A. M. Wing and C. Woodburn, “The coordination and consistency of rowers in a racing eight,” Journal of Sports Sciences, vol. 13, no. 3, pp. 187–197, 1995. 

- [3] E. Goodman, “Ensemble performance,” in Musical performance: a guide to understanding, J. Rink, Ed. Cambridge, UK: Cambridge University Press, 2002, pp. 153–167. 

- [4] C. Palmer, “Music performance,” Annual Review of Psychology, vol. 48, pp. 115–138, 1997. 

- [5] J. W. Davidson and J. M. M. Good, “Social and musical co-ordination between members of a string quartet: An exploratory study,” Psychology of Music, vol. 30, no. 2, pp. 186–201, 2002. 

- [6] J. K. Murnighan and D. E. Conlon, “The dynamics of intense work groups: A study of british string quartets,” Administrative Science Quarterly, vol. 36, no. 2, pp. 165–186, 1991. 

- [7] J. Gibbon, C. Malapani, C. L. Dale, and C. R. Gallistel, “Toward a neurobiology of temporal cognition: advances and challenges,” Current Opinion in Neurobiology, vol. 7, no. 2, pp. 170–184, 1997. 

- [8] A. M. Wing, S. Endo, A. Bradbury, and D. Vorberg, “Optimal feedback correction in string quartet synchronization,” Journal of the Royal Society Interface, vol. 11, no. 20131125, 2014. 

- [9] D. Vorberg and H. H. Schulze, “Linear phase correction in synchronization: predictions, parameter estimation, and simulations,” Journal of Mathematical Psychology, vol. 46, no. 1, pp. 56–87, 2002. 

   - [12] B. H. Repp, “Processes underlying adaptation to tempo changes in sensorimotor synchronization,” Human Movement Science, vol. 20, no. 3, pp. 277–312, 2001. 

   - [13] B. H. Repp and P. E. Keller, “Adaptation to tempo changes in sensorimotor synchronization: effects of intention, attention, and awareness,” Quarterly Journal of Experimental Psychology, vol. 57, no. 3, pp. 499– 521, 2004. 

   - [14] N. Jacoby, N. Tishby, B. H. Repp, M. Ahissar, and P. E. Keller, “Parameter estimation of linear sensorimotor synchronization models: Phase correction, period correction, and ensemble synchronization,” Timing & Time Perception, vol. 3, no. 1–2, pp. 52–87, 2015. 

   - [15] N. Jacoby, P. E. Keller, B. H. Repp, M. Ahissar, and N. Tishby, “Lower bound on the accuracy of parameter estimation methods for linear sensorimotor synchronization models,” Timing & Time Perception, vol. 3, no. 1–2, pp. 32–51, 2015. 

   - [16] M. C. van der Steen and P. E. Keller, “The ADaptation and Anticipation Model (ADAM) of sensorimotor synchronization,” Frontiers in Human Neuroscience, vol. 7, 2013. 

   - [17] B. Harry and P. E. Keller, “Tutorial and simulations with ADAM: an adaptation and anticipation model of sensorimotor synchronization,” Biological Cybernetics, vol. 113, pp. 397–421, 2019. 

   - [18] G. Petris, S. Petrone, and P. Campagnoli, Dynamic Linear Models with R. Berlin/Heidelberg, Germany: Springer, 2009. 

   - [19] M. S. Grewal and A. P. Andrews, Kalman Filtering: Theory and Practice with MATLAB. New Jersey, USA: Wiley-IEEE Press, 2014. 

   - [20] W. Mader, Y. Linke, M. Mader, L. Sommerlade, J. Timmer, and B. Schelter, “A numerically efficient implementation of the expectation maximization algorithm for state space models,” Applied Mathematics and Computation, vol. 241, pp. 222–232, 2014. 

   - [21] M. Tomczak, M. S. Li, and M. D. Luca, “Virtuoso strings: A dataset of string ensemble recordings and onset annotations for timing analysis,” in Extended Abstracts for the Late-Breaking Demo Session of the 24th Int. Society for Music Information Retrieval Conf., Milan, Italy, 2023. 

- [10] D. Vorberg and A. M. Wing, “Modeling variability and dependence in timing,” in Handbook of perception and action, vol. 2, H. Heuer and S. Keele, Eds. New York, USA: Academid Press, 1996, pp. 181–262. 

- [11] J. Mates, “A model of synchronization of motor acts to a stimulus sequence,” Biological Cybernetics, vol. 71, p. 186, 1994. 

624 

