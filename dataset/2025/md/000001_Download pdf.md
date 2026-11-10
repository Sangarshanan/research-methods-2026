---
paper_id: "000001"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706316/files/000001.pdf"
---

# GLOBALMOOD: A CROSS-CULTURAL BENCHMARK FOR MUSIC EMOTION RECOGNITION 

Harin Lee<sup>1,2,3</sup> Elif Çelen<sup>1</sup> Peter Harrison<sup>4</sup> Manuel Anglada-Tort<sup>5</sup> Pol van Rijn<sup>1</sup> Minsu Park<sup>6</sup> Marc Schönwiesner<sup>3</sup> Nori Jacoby<sup>1,7</sup> 1MPI Empirical Aesthetics 2MPI for Human Cognitive and Brain Sciences 3Leipzig University 4University of Cambridge 5Goldsmiths, University of London 6New York University Abu Dhabi 7Cornell University 

## ABSTRACT 

Human annotations of mood in music are essential for music generation and recommender systems. However, existing datasets predominantly focus on Western songs with terms derived from English, which may limit generalizability across diverse linguistic and cultural backgrounds. We introduce ‘GlobalMood’, a novel cross-cultural benchmark dataset comprising 1,180 songs sampled from 59 countries, with large-scale annotations collected from 2,519 individuals across five culturally and linguistically distinct locations: U.S., France, Mexico, S. Korea, and Egypt. Rather than imposing predefined emotion and mood categories, we implement a bottom-up, participant-driven approach to organically elicit culturally specific music-related emotion terms. We then recruit another pool of human participants to collect 988,925 ratings for these culture-specific descriptors. Our analysis confirms the presence of a valencearousal structure shared across cultures, yet also reveals significant divergences in how certain emotion terms (despite being dictionary equivalents) are perceived crossculturally. State-of-the-art multimodal models benefit substantially from fine-tuning on our cross-culturally balanced dataset, particularly in non-English contexts. Broadly, our findings inform the ongoing debate on the universality versus cultural specificity of emotional descriptors, and our methodology can contribute to other multimodal and crosslingual research. 

## 1. INTRODUCTION 

Music evokes diverse emotional responses in listeners, spanning a wide spectrum beyond basic emotional categories [1, 2]. A central challenge in Music Information Retrieval (MIR) is designing algorithms that can replicate this emotional sensitivity. This is crucial for building recommendation systems that align with listeners’ mood and 

© H. Lee, E. Çelen, P. Harrison, M. Anglada-Tort, P. van Rijn, M. Park, M. Schönwiesner, and N. Jacoby. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: H. Lee, E. Çelen, P. Harrison, M. Anglada-Tort, P. van Rijn, M. Park, M. Schönwiesner, and N. Jacoby, “GlobalMood: A cross-cultural benchmark for music emotion recognition”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

context [3–5], and for generating music that resonates with individual preferences [6]. More broadly, understanding how music conveys emotion is a core question in the science of music [7–9]. To date, however, most algorithms have been trained on datasets derived from Western listeners and Western music, using taxonomies primarily based on English language (e.g., MIREX [10]). 

A significant challenge is creating cross-cultural models capable of handling non-Western music and emotion vocabularies beyond English. Addressing this challenge is essential to developing algorithms that accurately reflect global users’ preferences, including those whose musical tastes extend beyond the limited range of styles currently represented in training datasets. Moreover, without capturing culturally specific nuances of emotion, especially those difficult to translate, key aspects of musical meaning may be missed entirely. Direct dictionary translations of English terms may be insufficient, as terms describing emotions are deeply cultural and may lack exact equivalents [11–14]. 

To address these issues, we introduce ‘GlobalMood’,<sup>1</sup> a new benchmark dataset designed to support culturally inclusive and linguistically diverse emotion and mood recognition in music. Our contribution innovates along three key dimensions: (i) the diversity of musical stimuli, drawn from 59 countries; (ii) the diversity of annotators, spanning five distinct regions (with plans to extens to over 20 languages and locations in future); (iii) a data-driven approach for collecting descriptors, generated organically by participants in their own language during the annotation process. 

Data were collected through two stages involving a total of 2,519 participants and 1,180 songs balanced evenly across 59 countries: In the first stage (Section 4.1; Figure 1), using a smaller subset of 200 songs, we employed our recently developed iterative task that combines openended elicitation with collective refinement [13, 15, 16]. Rather than asking listeners to choose from a fixed list of pre-defined emotion terms, we asked them to describe the perceived emotion conveyed in the music using free-text tags in their native language, and at the same time, rate the 

> 1 All code and data: `https://github.com/harin-git/ GlobalMood` 

11 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
★★★ ★★★★<br>A ★★★★ Dreamy Sad Dreamy Sad<br>Dreamy Ballad Mellow Smooth<br>Local music e Dreamy Ballad Sad<br>Chain 1<br>Music sample Foreign music initial relevant moodParticipant 1 adds tag of Participant 1.Participant 2 rates Participant 3 ratesand flags “Ballad" as High-quality tags thatare rated and validated<br>N countries = 59 d tag(s) Adds more tags inappropriate (notdescribing mood) remain at the end ofchain<br>Chain 200<br>B<br>US (English) France (French) Mexico (Spanish) S.Korea (Korean) Egypt (Arabic)<br>upbeat upbeat rythmé rhythmic alegria joy 2号 rhythmic enthusiasm<br>longinghappyjoyful joyfullonginghappy entraînantdansantjoie catchyjoydancing felicidadamorbaile dance 喜对是 sorrowtulcheerfulexciting njoymentsadnesslove<br>love love festif festive fiesta 空全 appealing C joy<br>excitement excitement étranger foreign ritmo rhythm pleasant romance<br>energetic energetic nostalgie nostalgia relajacion relaxation lively C fun<br>rhythmic mhythmic joyeux tranquilidad tranquility longing dance<br>romantic romantic amour nostalgia nostalgia sad happiness<br>festive festive cool cool emocion emotion sweet warmth<br>calm calm moderne modern tristeza sadness intense 34 calmness<br>sad latino latino pasion passion 0 exotic celebratory<br>reflective reflective calme calm romance romance emotional NY pain<br>fun un agréable pleasant movida lively 稳位位 calm delight<br>passionate passionate doux soft sensualidad sensuality soft 3 passion<br>relaxed relaxed triste raro strange strength<br>smooth smooth ensoleillé sunny esperanza hope energetic youth<br>intense intense amusant melancolía melancholy 7 feel-good excitement<br>chill chill bonheur happiness diversion fun lovely loud<br>emotional emotional mélancolie melancholy paz peace peaceful active<br>200 400 600 100200 300 400 0 200 400 600 100 200300 400 500 0 200 400 600<br>Tag Score<br><!-- End of picture text -->

Figure 1. Elicitation and refinement of music emotion terms through iterative participant chains. (A) Schematic illustration of the collaborative tagging process within a participant chain. Participants contribute new emotion-related word tags for each song, rate the relevance of existing tags, and can also flag irrelevant content, creating a dynamic refinement system. (B) Twenty most reliable emotion tags in each language, ranked by their tag scores. Y-axis labels display tags in their original language (left) and English translations (right). 

tags provided by previous listeners. This approach was key to uncovering emotion terms that would otherwise be overlooked by predefined, English-based taxonomies (such as ‘appeal/plead’ that appears in Korean only). 

In the second stage (Section 4.2; Figure 2), we selected the top 20 elicited terms per language and crowdsourced ratings for each tag across the entire set of 1,180 songs. This resulted in a total of 988,925 ratings, creating the most comprehensive open-source cross-cultural emotion annotation dataset in Music Emotion Recognition (MER) to date. 

We leveraged GlobalMood to test several recent multimodal and multilingual models (Gemini, CLAP) by evaluating their performance under zero-shot, few-shot, and fine-tuned scenarios (Section 4.3; Figure 3). Models trained only on English data performed poorly in some cultural contexts, but fine-tuning with our cross-cultural data greatly improved their performance in non-English settings. This highlights the critical importance of crosscultural data in both training MER models and establishing appropriate benchmarks for their evaluation. 

## 2. RELATED WORKS 

## 2.1 Music Emotion and Mood Annotation Datasets 

Several datasets have been developed for MER systems with varying annotation approaches.<sup>2</sup> Early examples in- 

> 2 Note that databases often extend the concept of emotion to include related constructs such as mood or feeling. Here we adopt this broader 

clude the widely used MIREX 2007 mood dataset [10] with 240-250 Western songs in five mood clusters derived from AllMusic’s English tags (e.g., ‘passionate–rousing’, ‘wistful–bittersweet’), and CAL500 [17] with 500 Western pop/rock songs annotated using 18 English mood terms by U.S. undergraduate listeners. Over time, larger datasets appeared: the DEAM corpus (MediaEval ‘Emotion in Music’ dataset [18]) containing 2,058 song excerpts with continuous valence/arousal annotations; mood tags mined from large corpora of Spotify music playlists [19]; and the MTG-Jamendo dataset [20], which provides mood/theme tags for 18,486 songs. Notably, Jamendo’s tags were freely crowdsourced (56 unique mood labels), which introduced more label variety but still almost entirely in English. 

A common limitation across these datasets is their reliance on predefined English descriptors, many of which stem from Western music psychology (for an exception, see Strauss et al. [21]). For instance, the Geneva Emotional Music Scale (GEMS) defines 45 emotion descriptors (e.g., ‘joyful activation’) based on studies with European listeners [1], and this taxonomy has been used to annotate datasets like Emotify [22]. Similarly, the mood categories in MIREX and CAL500 were fixed in advance (drawn from AllMusic or prior literature) and presented to annotators as a closed set of options. Consequently, these top-down approaches restrict annotators to the moods the researchers envisioned, leaving any unlisted mood nuances 

perspective, while acknowledging that subtle distinctions between them do exist. 

12 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
A High Arousal & Positive Valence GlobalMood<br>fun excitingcheertulenergetic着7社 dance enthusiasm loud strengthintense N raters = 1,741 N songs = 1,180<br>pleasantdiversionlively E un喜是 energetic active excitement youth US (English)France (French) How well does this song<br>0.5 joyfulhappyjoyeuxamusant hlappyjoyalegriafestivejoy +festive*festifdancecatchy 2happinessdelightそ猫8号にrhythmiccelebratory 异free modernemodernintense + Mexico (Spanish)Korea (Korean)Egypt (Arabic) è nostalgiaalegríapaz<br>Dim.1 latinolatino ensoleillésunnycoolcoolfeel-good *7#蛋号joiehappinessbonheurhappinessfelicidademocionemotiondancingdansantextrainantrhythmritmorhythmicrythmé rhythmicsensualityenjoymentY exoticforeign B<br>pleasant sensualidad étranger<br>agréable<br>passion fun<br>hope + pasion rhythmic<br>romanceesperanza lovely passionsmooth 0.5<br>-0.5 romance peacelut love amorlove love love passionate appealing空全创 happy<br>-1.0Positive ValenceLow Arousal & relajacionrelaxationpeacepaz tranquilidadtranquilitydouxsoft 早amourchillcalmnessrelaxed210星是calm94sweet romanticnostalgialonging melancholyユ2号romanceostalgialonging melancholymélancoliereflectivemelancoliasorrowfulnostalgieemotionalpainYIsas sseuads+ sadnesstristezatriste Negative ValenceLow Arousal & Dim.1 0.0 -0.5-1.0 love1+0calm sad<br>-0.5 0.0 0.5 -0.5 0.0 0.5<br>Dim.2 Dim.2<br><!-- End of picture text -->

Figure 2. Association between emotion terms across languages. (A) MDS visualization of the emotion terms based on mean ratings across the full song set. Terms positioned closer together exhibit similar rating patterns across songs, suggesting similar interpretations across languages. (B) Comparison of terms with direct translation equivalents across languages. The area size indicates the degree of semantic divergence despite apparent translation equivalence. 

## uncaptured and undocumented. 

Acknowledging these limitations, recent research has begun exploring MER beyond the Western-centric scope. Hu et al. [23] examined mood annotations of K-pop songs provided by both Korean and American listeners. Their approach involved translating the original MIREX mood categories into Korean for local annotators. Although this allowed direct comparisons of mood classification between Korean and American listeners, it inherently restricted Korean annotations to terms originally defined within Western contexts. 

More recently, we compiled a balanced set of American, Brazilian, and Korean songs and gathered mood annotations across nine categories, where annotators rated songs both from their own and the other two countries [12]. We showed that certain mood terms like ‘energetic’ and ‘sad’ are highly consistent across cultures, while more abstract concepts like ‘love’ and ‘dreamy’ diverge considerably. Similar findings have been reported by other studies [13, 14], highlighting that when mood descriptors are imposed from one language onto another, important meanings can simply be ‘lost in translation’. 

In summary, while existing MER datasets and research have laid a solid groundwork, they remain limited by insufficient linguistic and cultural diversity. Because many are predominantly English-based and rely on top-down annotation strategies, they may overlook how people in other cultural contexts perceive emotion and mood in music. 

## 2.2 Audio LLMs: the New Frontier in Music Tagging 

Recent advances in multimodal large language models (LLMs) have opened promising avenues for downstream 

MIR tasks, including emotion recognition. These models combine the reasoning capabilities of LLMs with audio perception systems (audio LLMs), enabling more flexible and nuanced music understanding than traditional classification approaches [24–26]. 

Models like MuLan [27] and MERT [24] have demonstrated potential for zero-shot music emotion and mood classification by embedding audio and natural language descriptions in a shared semantic space. However, comprehensive benchmarks such as the MuChoMusic [25] highlight a crucial limitation: these models rely heavily on language modality and do not attend sufficiently to audio, often failing with more nuanced audio examples for downstream MIR tasks. This limitation could be particularly critical for non-Western music and non-English emotion descriptors, given that their training data are largely from Western contexts. 

Similarly, closed-source models (e.g., Gemini) have shown promise in psychological textual analysis in multilingual contexts [28], while evaluations in specialized domains such as MIR remain scarce. The proprietary nature of their training data complicates thorough assessment of cross-lingual or cross-cultural performance. We aim to address these fundamental gaps by providing a large set of diverse, multilingual descriptors and annotations to support broader cross-cultural generalizability of audio LLMs. 

## 3. METHOD 

## 3.1 Participants 

We recruited two independent sets of participants across the two stages of our data collection: Stage 1 for emo- 

13 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

tion term elicitation (N = 778; see Section 4.1) and Stage 2 for subsequent ratings on top 20 terms (N = 1,741; see Section 4.2). Participants had to be at least 18 years old, reside in the target country, and speak the target language as their primary language. Participants from the US were recruited through Prolific, while participants from the other four countries (France, Mexico, S. Korea, and Egypt) were recruited through the CINT platform. All participants provided informed consent under an approved protocol (see Section 7). Participants were instructed to wear headphones and had to pass a headphone screening task [29], and a language proficiency test [30] before being eligible for the main experimental task. Experiments were conducted in each participant’s native language (English, French, Spanish, Korean, and Egyptian Arabic), with instructions translated using GPT-4o. Code to replicate the experiment through the PsyNet framework [31] and all data are available at `https://github.com/ harin-git/GlobalMood` 

## 3.2 Globally Representative Song Selection 

To create a globally representative music dataset, we used weekly YouTube top 100 music charts (year 2017-2023) from 59 countries, spanning six continents. To ensure each country’s charts reflected its distinct popular music, we excluded any track appearing in more than one country’s chart. This left us with a country-exclusive pool of songs. From this pool, we sampled 20 songs per country, yielding 1,180 songs in total. This diverse set is designed to capture a wide range of musical traditions and serve as a robust testbed for cross-cultural emotion recognition. Each 15second audio excerpt was trimmed from a random starting point in the full track, and normalized at -5dB loudness. 

## 3.3 Model Evaluation 

We used the resulting GlobalMood dataset to evaluate several recent multimodal and multilingual models capable of music understanding. Specifically, we assessed Google’s Gemini models (1.5 Flash, 2.0 Flash, and the latest 2.5 Pro), a family of multimodal large language models capable of processing and reasoning across text and audio (but also image and video).<sup>3</sup> We compared zero-shot and fewshot approaches, where the latter included 10 human-rated emotion terms as examples. 

Given that Gemini is closed-source, we also included CLAP (Contrastive Language-Audio Pretraining) [34] as an alternative, open-source model that learns joint audiotext embeddings. CLAP has demonstrated promise in MIR applications [35] and serves as the foundation for musicspecific models like CLaMP [36]. Here, we conducted zero-shot evaluations through: (1) extracting audio embeddings from CLAP, (2) computing cosine similarities with text embeddings of emotion terms, and (3) comparing these scores to human ratings. 

> 3 Preliminary tests with other recent multimodal models showed performance issues—Flamingo 2 [32] struggled with rating consistency and GPT-4o [33] failed to generate musical descriptions or ratings from audio alone—thus we excluded them from further analysis. 

We also fine-tuned CLAP on GlobalMood (train–test split = 1,000:180) to assess potential performance improvements. To preserve the continuous nature of our ratings, we represented each term in proportion to its mean rating (e.g., the term ‘calm’, with a mean rating of 3.0, appeared three times in the text). This method retained the nuanced information in our soft labels rather than reducing them to binary categories. To improve generalizability, we created 10 augmented variations of each song through pitch shifting (range of ±3 semitones), loudness adjustment (range of ±15dB), and the addition of Gaussian noise (amplitude of 0.005). Each augmented variant randomly included one or two of these modifications. 

## 4. RESULTS 

## 4.1 Bottom-up Term Elicitation Across Languages 

## 4.1.1 Tagging pipeline 

Many existing studies on music emotions rely on predefined taxonomies or web-scraped data that offer limited linguistic diversity [10, 19]. To overcome this limitation, we employed a bottom-up, participant-driven tagging method [13, 15, 16]. Specifically, we asked participants in each country to complete independent ‘chains’ of iterative annotations. A subsample of 200 songs from the 1,180 entire set was used as stimuli. This subsample consisted of 180 balanced songs across countries, with an additional 20 local songs drawn from the participating country’s pool. This was to ensure that local participants encounter enough music strongly tied to their background, allowing them to elicit culturally specific emotion descriptors. 

Figure 1A illustrates one such chain: (i) The first participant annotates the song using single-word emotion tags in their native language; (ii) The second participant (from the same country) rates the relevance of these tags (1–5 scale), flag irrelevant tags (e.g., genre- or lyrics-related rather than emotion), add new tags as necessary; (iii) The third participant sees all tags from earlier participants and repeats these steps; (iv) This iterative process continues through ten participants per chain, systematically refining and validating emotion terms. In each country, we ran the entire elicitation experiment twice and aggregated the results to increase the diversity of responses from a larger pool of participants. 

## 4.1.2 Top emerging terms 

Following the removal of tags flagged by more than two participants in a chain, our STEP-Tag process yielded an extensive, culturally specific lexicon of emotion terms across languages (N unique terms: English = 644; French = 528; Spanish = 870; Korean = 629; Arabic = 283). To identify the most salient terms in each language, we calculated a composite score for every term by multiplying its frequency of occurrences across chains by its mean relevance rating. Higher scores indicate terms frequently mentioned and consistently rated as highly relevant. 

We consolidated closely related morphological variants (e.g., ‘happy’ and ‘happiness’ in English; gendered 

14 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

forms such as ‘joyeux’ and ‘joyeuse’ in French) manually with native speakers. Figure 1B presents the resulting 20 highest-ranking tags per language, displaying both the original word and English translations to facilitate crosscultural comparisons. 

Despite being explicitly asked to provide emotion terms, participants often gave broader affective descriptors like moods or feelings (e.g., ‘soft’ and ‘festive’). This aligns with prior MIR literature that often includes both emotion and mood, and given its relevance for practical use, we did not enforce a strict distinction. 

## 4.2 Large-scale Diverse Human Ratings 

## 4.2.1 Cross-cultural ratings across the entire set 

Having identified the top 20 terms for each language, we next gathered exhaustive ratings for the entire 1,180 songs of GlobalMood. We recruited 1,741 new participants (see Section 3.1) who listened to the 15-second excerpts and rated how effectively each excerpt conveyed a given emotion and mood term (1–5 scale). For each stimulus, participants evaluated seven randomly selected terms from the relevant language set. This systematic approach ensured that, on average, each song in each language received 8.38 (SD = 2.40) unique participant ratings, resulting in an extensive collection of 988,925 ratings spanning across five languages. 

## 4.2.2 Is ‘happy’ in my language the same ‘happy’ in your language? 

To investigate differences in how each culture interprets these terms, we constructed 100 rating vectors (5 languages × 20 terms per language). Each vector was 1,180dimensional, capturing the mean rating per term across the 1,180 song set. We then performed non-metric multidimensional scaling (MDS) using correlation as the distance metric, projecting these vectors in a two-dimensional space. In this emotion ‘space,’ terms that position close to one another—even those from different languages—reflect similar rating patterns across the musical examples, suggesting comparable emotional interpretations across cultures. 

Figure 2A visualizes this emotion space. The terms cluster into two main regions: one region of high arousal and high valence (e.g., happy, energetic, and lively; upper region of the figure) and a second region of low arousal that spans positive valence (e.g., peaceful; bottom left) to negative (e.g., sad; bottom right). Notably, many translated ‘equivalents’ appear close together, which might suggest a general cross-cultural consensus on what music evokes what emotions. 

However, examining six commonly shared terms that have direct translations in at least four of the five languages (fun, happy, rhythmic, love, sad, and calm) revealed varying degrees of cross-cultural agreement (see Figure 2B). For each of these terms, between-country agreement (rbetween) was computed as the average of pairwise correlation coefficients, while within-country agreement (rwithin) was calculated using split-half reliability with 

Spearman-Brown formula. Effectively, rwithin serves as measurement error to compare as baselines when evaluating rbetween. 

The term calm showed the highest average agreement (rbetween = 0.52 [0.49, 0.55]; rwithin = 0.49 [0.38, 0.57]), followed by fun (rbetween = 0.46 [0.39, 0.53]; rwithin = 0.44 [0.27, 0.54]), love (rbetween = 0.44 [0.41, 0.47]; rwithin = 0.47 [0.33, 0.66]), sad (rbetween = 0.41 [0.37, 0.45]; rwithin = 0.43 [0.32, 0.58]), rhythmic (rbetween = 0.38 [0.30, 0.45]; rwithin = 0.43 [0.25, 0.53]), and notably happy (rbetween = 0.37 [0.28, 0.45]; rwithin = 0.45 [0.24, 0.59]). 

Overall, considering within-country agreement (mean rwithin = 0.43–0.48), most of these terms were comparable in their between-country agreement (mean rbetween = 0.39–0.52). However, despite being considered a basic universal human emotion [37], happy exhibited a considerable gap between between- and within-country agreement. This emphasizes the necessity of incorporating diverse cultural perspectives when modeling nuanced musical emotional responses. Reliance on either dictionary translation or LLM-based translation alone could overlook important, context-specific nuances in emotion and mood perception—particularly relevant when building models for global audiences. 



<!-- Start of picture text -->
A Gemini<br>(closed-source)<br>US (English) France (French) Mexico (Spanish) Korea (Korean) Egypt (Arabic)<br>0.6<br>Co r elation<br>(Human vs. Gemini)<br>1.5 Flash2.0 Flash 2.5 Pro 1.5 Flash2.0 Flash 2.5 Pro 1.5 Flash2.0 Flash 2.5 Pro 1.5 Flash2.0 Flash 2.5 Pro 1.5 Flash2.0 Flash 2.5 Pro<br>B CLAP<br>(open-source)<br>US (English) France (French) Mexico (Spanish) Korea (Korean) Egypt (Arabic)<br>0.6<br>0.4<br>Co r elation 0.2<br>壬<br>(Human vs. CLAP)<br>Zero-shotFinetuned Zero-shot Zero-shotFinetuned Zero-shotFinetuned Zero-shotFinetuned<br><!-- End of picture text -->

Figure 3. Correlations between human ratings and multimodal model predictions. (A) Gemini models with zeroshot prompting showing increase in performance with newer models. (B) CLAP models in zero-shot and finetuned scenarios showing how the use of multilingual annotations can substantially increase performance. Gray dashed lines represent split-half reliability of human ratings using the Spearman-Brown formula as baseline reference of correlations achieved between humans. Error bars indicate 95% CI of mean correlation across songs. 

## 4.3 Human vs. Multimodal Models 

Recent benchmarks have evaluated the capabilities of audio LLMs across various downstream MIR tasks, but these evaluations have also been restricted to English [25]. We 

15 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

evaluated both closed-source (Gemini) and open-source (CLAP) models against our GlobalMood multilingual human ratings (see Section 3.3 for model details). 

For Gemini (Figure 3A), we replicated our human study protocol by prompting the model with ‘Rate from a scale of 1 to 5 how well this song expresses or conveys the emotion [...]’ independently for the five native languages. We then evaluated how well the model’s outputs predict human judgments. We observed consistent improvement with each new model version. The earliest model, 1.5 Flash, demonstrated modest alignment with human judgments (mean correlation across countries: r = 0.34 (95% CI = [0.27, 0.42]). This model struggled particularly with Korean language ratings (r = 0.27 [0.21, 0.33]). The subsequent 2.0 Flash version bridged this gap in Korean (r = 0.42 [0.36, 0.47]), and achieved a substantially higher mean correlation of r = 0.42 [0.36, 0.48]. The latest 2.5 Pro model demonstrated another leap with a mean correlation of r = 0.50 [0.45, 0.55]. Few-shot approach with 10 human-rated examples using 2.5 Pro did not improve the results (r = 0.47 [0.42, 0.52]). This consistent upward trajectory across model iterations provides compelling evidence that these general-purpose systems are progressively developing more sophisticated understanding of musical emotions across diverse linguistic and cultural contexts. 

This level of correlations between Gemini and human ratings are on par with algorithms specifically designed for MER, such as Spotify’s mood estimation [12, 38]. Moreover, given the subjective nature of emotion and mood perception in music (where even humans often disagree), the latest Gemini model already reaches human-level performance, matching the theoretical upper bound defined by inter-rater human agreement (gray dashed lines in Figure 3). 

For CLAP, an open-source alternative (Figure 3B), we evaluated both a zero-shot approach and a fine-tuned version trained on our GlobalMood dataset (see Section 3.3 for fine-tuning details). The zero-shot approach measured the similarity between the emotion term’s text embedding and the song’s audio embedding. This zero-shot CLAP performed poorly (mean r = 0.08 [0.03, 0.13]), while finetuning with GlobalMood substantially improved the performance (mean r = 0.31 [0.19, 0.44]). As a control experiment, we also fine-tuned CLAP using a dataset where all non-English emotion terms were first translated into English using an LLM without any musical context (instead of original emotion terms collected from native speakers). This translation-based approach failed to improve performance (mean r = 0.13 [-0.05, 0.32]), showing that the performance gains from fine-tuning come from culturallyspecific information rather than from mere increase in data volume. 

Importantly, improvements through finetuning were most pronounced for non-English languages. Based on Fisher’s z test for correlation comparisons, Arabic showed the largest increase from r = 0.11 to 0.46 (z = 0.39), followed by Spanish (from 0.04 to 0.32; z = 0.29) and Korean (from 0.06 to 0.32; z = 0.27). The least substantial 

increase was observed for French (from 0.07 to 0.17; z = 0.10). These observations demonstrate the promising potential of how native-language terms and ratings from our GlobalMood dataset can be used to generalize to new cultures and languages, when modeling MER systems. 

## 5. DISCUSSION 

We introduce GlobalMood, a novel cross-cultural benchmark dataset comprising emotion and mood descriptors and ratings collected from a large and globally diverse participant pool through a data-driven approach. Consistent with previous research in music consumption and perception [39–44] and music emotion [12–14, 45, 46], our findings highlight both cross-cultural similarities and differences. Specifically, we demonstrate that music emotion descriptors across languages are broadly organized around clusters relating to valence and arousal [8,37]. 

Relying on dictionary translations for music emotion terms may face limitations (e.g., [45]), where cross-lingual agreement varied across terms. For instance, despite happy being a basic emotion, it exhibited a relatively large gap between cross- and within-country agreement. This highlights the need for incorporating multilingual descriptors from diverse annotators. Our future work aims to expand GlobalMood to reach over 20 languages [30, 47] and a broader range of musical styles, including works from different historical periods, which will be critical for developing more robust tools that can generalize across diverse cultural contexts. 

Notably, fine-tuning CLAP on cross-cultural data significantly boosted performance in non-English contexts, highlighting the value of GlobalMood. These findings point to the potential for culturally-sensitive MER systems, moving beyond one-size-fits-all models. Future work should investigate more varied prompting and data augmentation techniques, and alternative LLM architectures. 

Our tagging pipeline is quick to deploy across cultures and uses a bottom-up approach that helps minimize researcher bias. This offers an advantage over predefined term lists, which often fail to capture the cultural subtleties of emotion terms [48]. However, it has drawbacks: early participants can bias the tag pool and there’s no theoretical guarantee that all tags reflect clear emotion concepts (e.g., ‘étranger’ in French). Unlike structured systems for crowdsourcing tags (e.g., TagATune [49]), our approach trades control for flexibility and cultural responsiveness. 

Beyond MIR, the GlobalMood and associated pipeline offer timely implications for broader multimodal and cross-lingual research, particularly in Natural Language Processing (NLP) communities [50]. As NLP increasingly tackles multimodal tasks involving audio–text modeling and cross-cultural applications, our dataset may provide a useful benchmark for evaluating language–audio models across diverse contexts. The iterative annotation pipeline can also serve as an effective framework for collecting representative samples and annotations in other domains [15,16,31,51]. 

16 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

## 6. ACKNOWLEDGMENTS 

H.L. was funded by the Max Planck Society. M.P. was partially supported by the NYUAD Center for Interacting Urban Networks (CITIES), funded by Tamkeen under the NYUAD Research Institute Award CG001. 

## 7. ETHICS STATEMENT 

We conducted our human experiment according to ethical best practices. All participants recruited via Prolific or CINT provided informed consent based on an approved protocol (Max Planck Ethics Council #202142). Participant data was collected anonymously (except for Prolific or CINT IDs), and all published data are fully anonymized. Models were accessed through commercial APIs, with fine-tuning performed locally. Conducting cross-cultural research requires sensitivity to diverse ethical considerations [52], and this study was designed accordingly. We acknowledge that machine learning models and training datasets may contain biases originating from participants, data selection processes, and the models themselves. Despite these potential biases, our study aims to address critical limitations and societal risks within current MIR technologies, which predominantly focus on English-language music and raters despite serving diverse global populations [48,53,54]. 

## 8. REFERENCES 

- [1] M. Zentner, D. Grandjean, and K. R. Scherer, “Emotions evoked by the sound of music: Characterization, classification, and measurement,” Emotion, vol. 8, no. 4, pp. 494–521, 2008. 

- [2] A. S. Cowen, X. Fang, D. Sauter, and D. Keltner, “What music makes us feel: At least 13 dimensions organize subjective experiences associated with music across different cultures,” Proceedings of the National Academy of Sciences, vol. 117, no. 4, pp. 1924–1934, Jan 2020. 

- [3] T. Eerola and P. Saari, “What emotions does music express? structure of affect terms in music using iterative crowdsourcing paradigm,” PLOS ONE, vol. 20, no. 1, p. e0313502, Jan 2025. 

- [4] H. Tran, T. Le, A. Do, T. Vu, S. Bogaerts, and B. Howard, “Emotion-aware music recommendation,” in Proceedings of the AAAI Conference on Artificial Intelligence, vol. 37, no. 13, 2023, p. 13. 

- [5] J. Kang and D. Herremans, “Are we there yet? a brief survey of music emotion prediction datasets, models and outstanding challenges,” 2024. [Online]. Available: https://arxiv.org/abs/2406.08809 

- [6] Y. Sun, M. Kuo, X. Wang, W. Li, and Q. Bai, “Emotion-conditioned MusicLM: Enhancing emotional resonance in music generation,” in 2024 IEEE Congress on Evolutionary Computation (CEC), Jun 2024, pp. 1–8. 

- [7] P. N. Juslin and D. Västfjäll, “Emotional responses to music: The need to consider underlying mechanisms,” Behavioral and brain sciences, vol. 31, no. 5, pp. 559– 575, 2008. 

- [8] T. Eerola and J. K. Vuoskoski, “A review of music and emotion studies: Approaches, emotion models, and stimuli,” Music Perception: An Interdisciplinary Journal, vol. 30, no. 3, pp. 307–340, 2012. 

- [9] M. Park, J. Thom, S. Mennicken, H. Cramer, and M. Macy, “Global music streaming data reveal diurnal and seasonal patterns of affective preference,” Nature human behaviour, vol. 3, no. 3, pp. 230–236, 2019. 

- [10] X. Hu and J. S. Downie, “Exploring mood metadata: Relationships with genre, artist and usage metadata,” in International Society for Music Information Retrieval Conference, Dec 2007. 

- [11] J. C. Jackson, J. Watts, T. R. Henry, J.-M. List, R. Forkel, P. J. Mucha, S. J. Greenhill, R. D. Gray, and K. A. Lindquist, “Emotion semantics show both cultural variation and universal structure,” Science, vol. 366, no. 6472, pp. 1517–1522, 2019. 

- [12] H. Lee, F. Höger, M. Schönwiesner, M. Park, and N. Jacoby, “Cross-cultural mood perception in pop songs and its alignment with mood detection algorithms,” in Proceedings of the International Society for Music Information Retrieval Conference, Nov 2021, pp. 366–373. 

- [13] E. Celen, P. van Rijn, H. Lee, and N. Jacoby, “Are expressions for music emotions the same across cultures?” 2025. [Online]. Available: https: //arxiv.org/abs/2502.08744 

- [14] J. S. Gómez-Cañón, E. Cano, P. Herrera, and E. Gómez, “Joyful for you and tender for us: the influence of individual characteristics and language on emotion labeling and classification,” in Proceedings of the International Society of Music Information Retrieval Conference, Oct 2020. 

- [15] R. Marjieh, P. van Rijn, I. Sucholutsky, T. R. Sumers, H. Lee, T. L. Griffiths, and N. Jacoby, “Words are all you need? language as an approximation for human similarity judgments,” in The Eleventh International Conference on Learning Representations, 2023. 

- [16] P. van Rijn, S. Mertes, K. Janowski, K. Weitz, N. Jacoby, and E. André, “Giving robots a voice: Humanin-the-loop voice creation and open-ended labeling,” in Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems, 2024, pp. 1–34. 

- [17] D. Turnbull, L. Barrington, D. Torres, and G. Lanckriet, “Towards musical query-by-semantic-description using the CAL500 data set,” in Proceedings of the 30th annual international ACM SIGIR conference on Research and development in information retrieval, ser. 

17 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

   - SIGIR ’07. New York, NY, USA: Association for Computing Machinery, Jul 2007, pp. 439–446. 

- [18] A. Aljanaki, Y.-H. Yang, and M. Soleymani, “Developing a benchmark for emotional analysis of music,” PLOS ONE, vol. 12, no. 3, p. e0173392, Mar 2017. 

- [19] J. Affolter and M. A. Rohrmeier, “Utilizing listenerprovided tags for music emotion recognition: A datadriven approach,” in Proceedings of the International Society for Music Information Retrieval Conference, Nov 2024, pp. 547–554. 

- [20] D. Bogdanov, M. Won, P. Tovstogan, A. Porter, and X. Serra, “The MTG-Jamendo dataset for automatic music tagging,” in Machine Learning for Music Discovery Workshop, International Conference on Machine Learning (ICML 2019), Long Beach, CA, United States, 2019. [Online]. Available: http: //hdl.handle.net/10230/42015 

- [21] H. Strauss, J. Vigl, P.-O. Jacobsen, M. Bayer, F. Talamini, W. Vigl, E. Zangerle, and M. Zentner, “The Emotion-to-Music mapping atlas (EMMA): A systematically organized online database of emotionally evocative music excerpts,” Behav. Res. Methods, vol. 56, no. 4, pp. 3560–3577, Apr. 2024. 

- [22] A. Aljanaki, F. Wiering, and R. C. Veltkamp, “Studying emotion induced by music through a crowdsourcing game,” Information Processing & Management, vol. 52, no. 1, pp. 115–128, Jan 2016. 

- [23] X. Hu, J. H. Lee, K. Choi, and J. S. Downie, “A crosscultural study on the mood of K-POP songs,” in Proceedings of the International Society for Music Information Retrieval Conference, Oct 2014, pp. 385–390. 

- [24] Y. LI, R. Yuan, G. Zhang, Y. Ma, X. Chen, H. Yin, C. Xiao, C. Lin, A. Ragni, E. Benetos, N. Gyenge, R. Dannenberg, R. Liu, W. Chen, G. Xia, Y. Shi, W. Huang, Z. Wang, Y. Guo, and J. Fu, “MERT: Acoustic music understanding model with large-scale self-supervised training,” in The Twelfth International Conference on Learning Representations, 2024. 

- [25] B. Weck, I. Manco, E. Benetos, E. Quinton, G. Fazekas, and D. Bogdanov, “MuChoMusic: Evaluating music understanding in multimodal audiolanguage models,” in Proceedings of the International Society for Music Information Retrieval Conference, Nov 2024. 

- [26] S. Doh, K. Choi, J. Lee, and J. Nam, “LP-MusicCaps: LLM-based pseudo music captioning,” in Proceedings of the International Society for Music Information Retrieval Conference, 2023. 

- [27] Q. Huang, A. Jansen, J. Lee, R. Ganti, J. Y. Li, and D. P. W. Ellis, “MuLan: A joint embedding of music audio and natural language,” in Proceedings of the International Society for Music Information Retrieval Conference, 2022. 

- [28] S. Rathje, D.-M. Mirea, I. Sucholutsky, R. Marjieh, C. E. Robertson, and J. J. Van Bavel, “GPT is an effective tool for multilingual psychological text analysis,” Proceedings of the National Academy of Sciences, vol. 121, no. 34, p. e2308950121, Aug. 2024. 

- [29] A. E. Milne, R. Bianco, K. C. Poole, S. Zhao, A. J. Oxenham, A. J. Billig, and M. Chait, “An online headphone screening test based on dichotic pitch,” Behavior Research Methods, vol. 53, no. 4, pp. 1551–1562, 2021. 

- [30] P. van Rijn, Y. Sun, H. Lee, R. Marjieh, I. Sucholutsky, F. Lanzarini, E. André, and N. Jacoby, “Around the world in 60 words: A generative vocabulary test for online research,” in Proceedings of the Annual Meeting of the Cognitive Science Society, 2023. 

- [31] P. M. C. Harrison, R. Marjieh, F. Adolfi, P. van Rijn, M. Anglada-Tort, O. Tchernichovski, P. LarrouyMaestri, and N. Jacoby, “Gibbs sampling with people,” in Advances in Neural Information Processing Systems, 2020, pp. 10 659–10 671. 

- [32] S. Ghosh, Z. Kong, S. Kumar, S. Sakshi, J. Kim, W. Ping, R. Valle, D. Manocha, and B. Catanzaro, “Audio Flamingo 2: An audio-language model with long-audio understanding and expert reasoning abilities,” 2025. [Online]. Available: https://arxiv.org/ abs/2503.03983 

- [33] A. Hurst, A. Lerer, A. P. Goucher, A. Perelman, A. Ramesh, A. Clark, A. Ostrow, A. Welihinda, A. Hayes, A. Radford et al., “GPT-4o system card,” arXiv preprint arXiv:2410.21276, 2024. 

- [34] Y. Wu, K. Chen, T. Zhang, Y. Hui, T. Berg-Kirkpatrick, and S. Dubnov, “Large-scale contrastive languageaudio pretraining with feature fusion and keyword-tocaption augmentation,” in ICASSP 2023 - 2023 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, Jun. 2023, pp. 1–5. 

- [35] J. Barnett, H. F. Garcia, and B. Pardo, “Exploring musical roots: Applying audio embeddings to empower influence attribution for a generative music model,” in Proceedings of the International Society for Music Information Retrieval Conference, Nov 2024. 

- [36] S. Wu, Z. Guo, R. Yuan, J. Jiang, S. Doh, G. Xia, J. Nam, X. Li, F. Yu, and M. Sun, “CLaMP 3: Universal music information retrieval across unaligned modalities and unseen languages,” 2025. [Online]. Available: https://arxiv.org/abs/2502.10362 

- [37] P. Ekman, “Are there basic emotions?” Psychological Review, vol. 99, no. 3, pp. 550–553, 1992. 

- [38] D. Duman, P. Neto, A. Mavrolampados, P. Toiviainen, and G. Luck, “Music we move to: Spotify audio features and reasons for listening,” PLoS One, vol. 17, no. 9, p. e0275228, Sep. 2022. 

18 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [39] N. Jacoby, E. A. Undurraga, M. J. McPherson, J. Valdés, T. Ossandón, and J. H. McDermott, “Universal and non-universal features of musical pitch perception revealed by sung reproduction,” Current Biology, vol. 29, no. 19, pp. 3229–3243, 2019. 

- [40] S. A. Mehr, M. Singh, D. Knox, D. M. Ketter, D. Pickens-Jones, S. Atwood, C. Lucas, A. A. Egner, N. Jacoby, E. J. Hopkins et al., “Universality and diversity in human song,” Science, vol. 366, no. 6468, p. eaax0868, 2019. 

- [41] N. Jacoby, R. Polak, J. A. Grahn, D. J. Cameron, K. M. Lee, R. Godoy, E. A. Undurraga, T. Huanca, T. Thalwitzer, N. Doumbia et al., “Commonality and variation in mental representations of music revealed by a crosscultural comparison of rhythm priors in 15 countries,” Nature Human Behaviour, vol. 8, no. 5, pp. 846–877, 2024. 

- [42] P. E. Savage, S. Brown, E. Sakai, and T. E. Currie, “Statistical universals reveal the structures and functions of human music,” Proceedings of the National Academy of Sciences, vol. 112, no. 29, pp. 8987–8992, 2015. 

- [43] J. H. McDermott, A. F. Schultz, E. A. Undurraga, and R. A. Godoy, “Indifference to dissonance in native amazonians reveals cultural variation in music perception,” Nature, vol. 535, no. 7613, pp. 547–550, 2016. 

- [44] H. Lee, N. Jacoby, R. Hennequin, and M. Moussallam, “Mechanisms of cultural diversity in urban populations,” Nature Communication, vol. 16, no. 1, p. 5192, Jun. 2025. 

- [45] A. S. Cowen, X. Fang, D. Sauter, and D. Keltner, “What music makes us feel: At least 13 dimensions organize subjective experiences associated with music across different cultures,” Proceedings of the National Academy of Sciences, vol. 117, no. 4, pp. 1924–1934, 2020. 

sound annotation,” in Proceedings of the International Conference on Music Information Retrieval, 2007, pp. 361–364. 

   - [50] D. Hershcovich, S. Frank, H. Lent, M. de Lhoneux, M. Abdou, S. Brandl, E. Bugliarello, L. Cabello Piqueras, I. Chalkidis, R. Cui, C. Fierro, K. Margatina, P. Rust, and A. Søgaard, “Challenges and strategies in cross-cultural NLP,” in Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), S. Muresan, P. Nakov, and A. Villavicencio, Eds. Dublin, Ireland: Association for Computational Linguistics, May 2022, pp. 6997–7013. 

   - [51] D.-M. Huang, P. Van Rijn, I. Sucholutsky, R. Marjieh, and N. Jacoby, “Characterizing similarities and divergences in conversational tones in humans and LLMs by sampling with people,” in Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), L.-W. Ku, A. Martins, and V. Srikumar, Eds. Bangkok, Thailand: Association for Computational Linguistics, Aug. 2024, pp. 10 486–10 512. [Online]. Available: https://aclanthology.org/2024.acl-long.565/ 

   - [52] N. Jacoby, E. H. Margulis, M. Clayton, E. Hannon, H. Honing, J. Iversen, T. R. Klein, S. A. Mehr, L. Pearson, I. Peretz et al., “Cross-cultural work in music cognition: Challenges, insights, and recommendations,” Music Perception, vol. 37, no. 3, pp. 185–195, 2020. 

   - [53] J. Henrich, S. J. Heine, and A. Norenzayan, “Most people are not WEIRD,” Nature, vol. 466, no. 7302, pp. 29–29, 2010. 

   - [54] B. Amiri, N. Shahverdi, A. Haddadi, and Y. Ghahremani, “Beyond the trends: Evolution and future directions in music recommender systems research,” IEEE Access, 2024. 

- [46] T. Fritz, S. Jentschke, N. Gosselin, D. Sammler, I. Peretz, R. Turner, A. D. Friederici, and S. Koelsch, “Universal recognition of three basic emotions in music,” Current Biology, vol. 19, no. 7, pp. 573–576, 2009. 

- [47] J. P. Niedermann, I. Sucholutsky, R. Marjieh, E. Celen, T. Griffiths, N. Jacoby, and P. van Rijn, “Studying the effect of globalization on color perception using multilingual online recruitment and large language models,” in Proceedings of the Annual Meeting of the Cognitive Science Society, vol. 46, 2023. 

- [48] D. E. Blasi, J. Henrich, E. Adamou, D. Kemmerer, and A. Majid, “Over-reliance on English hinders cognitive science,” Trends in Cognitive Sciences, vol. 26, no. 12, pp. 1153–1170, 2022. 

- [49] E. L. M. Law, L. von Ahn, R. B. Dannenberg, and M. Crawford, “TagATune: A game for music and 

19 

