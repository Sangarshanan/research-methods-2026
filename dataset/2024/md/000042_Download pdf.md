---
paper_id: "000042"
year: 2024
title: "Download pdf"
source_url: "https://zenodo.org/record/14877357/files/000042.pdf"
---

# HAISP: A DATASET OF HUMAN–AI SONGWRITING PROCESSES FROM THE AI SONG CONTEST 

Lidia Morris<sup>1</sup> `∗` Rebecca Leger<sup>2</sup> `∗` Michele Newman<sup>1</sup> John Ashley Burgoyne<sup>3</sup> Ryan Groves<sup>4</sup> Natasha Mangal<sup>5</sup> Jin Ha Lee<sup>1</sup> 1 University of Washington, USA 2 Fraunhofer IIS, Germany 3 University of Amsterdam, Netherlands 4 Infinite Album, Switzerland 5 CISAC, France 

```
ljmorris@uw.edu,rebecca.leger@iis.fraunhofer.de,mmn13@uw.edu,
```

```
j.a.burgoyne@uva.nl,ryan@infinitealbum.io,natasha.mangal@cisac.org,jinhalee@uw.edu
```

> ∗ denotes shared first authorship 

## ABSTRACT 

The advent of accessible artificial intelligence (AI) tools and systems has begun a new era for creative expression, challenging us to gain a better understanding of human-AI collaboration and creativity. In this paper, we introduce Human–AI Songwriting Processes Dataset (HAISP), consisting of 34 coded submissions from the 2023 AI Song Contest. This dataset offers a resource for exploring the complex dynamics of AI-supported songwriting processes, facilitating investigations into the possibilities and challenges posed by AI in creative endeavors. Overall, HAISP is anticipated to contribute to advancing understanding of human-AI co-creation from the users’ perspective. We suggest potential use cases for the dataset, including examining AI tools used in songwriting and exploring users’ ethical considerations and creative approaches. This could help inform academic research and practical applications in music composition and related fields. 

## 1. INTRODUCTION 

Open and easy to access artificial intelligence (AI) technologies have created new opportunities for creativity, challenging conventional notions of authorship, expression, and human-AI creativity [1]. Within this landscape, the AI Song Contest (AISC) has emerged as a unique platform where teams of musicians, data scientists, researchers and AI enthusiasts can leverage AI tools to compose original songs, providing a prolific ground for studying the interplay between human creativity and machine intelligence [2]. 

In this paper we present the Human-AI Songwriting 

© L. Morris, R. Leger, M. Newman, J. A. Burgoyne, R. Groves, N. Mangal and J. H. Lee. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: L. Morris, R. Leger, M. Newman, J. A. Burgoyne, R. Groves, N. Mangal and J. H. Lee, “HAISP: A Dataset of Human–AI Songwriting Processes from the AI Song Contest”, in Proc. of the 25th Int. Society for Music Information Retrieval Conf., San Francisco, United States, 2024. 

Processes Dataset (HAISP), a curated dataset extracted from the written process documentation of participants in the AI Song Contest. This dataset provides a useful resource for exploring various aspects of AI-supported songwriting processes. It consists of 34 submissions from the 2023 AISC teams, cleaned, organized, and crossannotated by four annotators using our data dictionary. The HAISP dataset includes information on the AI systems utilized, creative and technical inspirations, methodologies for working with AI, teams’ assessments of the songs, and reflections on ethical considerations in AI-generated content. This dataset provides researchers with a unique perspective into the complex relationship between human creativity and AI assistance in songwriting. By analyzing how songwriting processes are affected by the use of AI tools, scholars can gain insights into how AI systems may augment, complement, or challenge creative endeavors. The dataset also supports investigations into the ethical aspects of AI-generated music, including considerations like diversity in training data, intellectual property rights, and accessibility in music creation. It can serve as a valuable resource for scholars, practitioners, and enthusiasts alike, fostering deeper understanding, critical inquiry, and informed discourse in the burgeoning field of human-AI collaboration and creativity. Overall, it provides various insights and opportunities for further research, contributing to our understanding of the interaction between technology and creativity in the digital age. 

## 2. BACKGROUND 

## 2.1 Human–AI Music Creation 

Using computational methods for music creation that would be classified as AI today, began in the 1950s, with early examples including Iannis Xenakis using Markov Chains for composition [3] or David Cope’s Experiments in Musical Intelligence in the 1980s [4]. For more detail on the history of AI music we refer to The Oxford Handbook of Algorithmic Music by Roger Dean and Alex McLean [5]. Although the use of neural networks for mu- 

397 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

sic modeling was mentioned as early as 1989 [6], the recent progress in the field of deep learning led to an increase of powerful and easy-to-use AI tools for music creation [7], from accessible applications for a large audience [8], to tools intended for professional musicians (e.g. [9]). 

## 2.2 AI and Music Information Retrieval 

In the area of music composition, researchers have developed many methods [10] and machine learning-powered interfaces that enable interactive exploration of musical variations by mapping user inputs to musical structures. Other tools have recently emerged to assist in various aspects of the music creation process, including infilling missing parts of compositions [11–14], creating new instruments [15, 16], counterpoint improvisation [17], and generating and recommending chord progressions [18– 20], harmonies [21–23], and even accompaniment [24,25]. 

Many AI models have also been created to aid in music information retrieval (MIR) research. With the explosive growth of digital music archives and streaming platforms, the need for effective MIR systems has become increasingly pronounced, driving research efforts to develop more sophisticated methods for understanding and processing music data through AI, such as the utilization of deep learning, neural networks, and large language models [26–29]. Existing datasets in the realm of AI in MIR primarily focus on training data, such as audio features [30,31], music [32,33], and metadata [34,35]. 

## 2.3 AI Song Contest 

The AI Song Contest is an annual international music competition wherein teams from diverse musical traditions and disciplines collaborate to compose songs using AI methods. It was launched in 2020 by the Dutch public broadcaster VPRO [2], and has been organized independently afterwards every year. There have been 132 teams so far, with 35 from the 2023 edition included in the dataset. We plan to extend the dataset with the other year’s team entries in the future. To participate in the AI Song Contest 2023, teams had to submit their song, a team image, cover art, and an online form in which they described their team, their creative vision, their motivation to participate, the steps of composition, their impression of the human-AI cocreation process, their workflow, all AI tools and databases used and their ethical and cultural considerations. The form has been developed by the AI Song Contest organizing team, slightly modified for each new edition. After successful submission, the songs and process documents are sent to a jury. The top ten entries of the jury voting are open for a public online vote. Whichever team gets the most points from the jury voting combined with the public voting wins the AI Song Contest. 

## 3. OBJECTIVE AND SCOPE 

There is a growing recognition of the need for complementary data that provides insights into the qualitative aspects of human-AI collaboration in music creation – the 

human side of training and using these AI tools and systems. Recently, researchers have called for a cultural and ethical turn in MIR [36]. Rezwana and Maher [37] and Lee et al. [38] emphasize the importance of understanding not only perspectives but also expectations and ethical concerns of users of AI tools. 

To our knowledge, there is no dataset exploring the qualitative processes and reflections of those who have used AI tools for music creation. Recognizing this gap, we were motivated to curate the written submissions of AISC participants into a unique and publicly available dataset that would allow researchers to go behind the scenes and explore the AI-supported songwriting and creation processes of the teams, beyond the final song submissions. By complementing existing quantitative datasets in AI in MIR, the HAISP dataset contributes to a more holistic understanding of the role of AI in creative endeavors and facilitates deeper insights into the collaborative dynamics between human composers and AI systems. 

However, there are limitations to the data in this dataset. Firstly, the dataset relies solely on the words of the 34 participants in their written (subjective) process documentation. Compared to other datasets in MIR publications, this qualitative dataset is of limited size which might not lead to conclusions that are broadly applicable. Additionally, the dataset may not capture the full spectrum of AI tools and methodologies employed by participants, as teams may choose not to disclose certain details or may use proprietary technologies. Furthermore, the dataset represents a snapshot of a specific event and a specific outcome, the song, which may not fully generalize to other contexts of AI-supported music creation such as AI tools for jazz improvisation (e.g. see GenJam [39]). 

Nonetheless, the amount of detail and depth provides an extensive and rich insight into the creative experience of the teams. By compiling and analyzing the teams’ process documentation, we seek to illuminate the landscape of human-AI creative collaboration. Through the creation of this dataset, we aim to facilitate deeper insights into the collaborative dynamics between human composers and AI systems, thereby fostering a richer understanding of the potential, limitations, and societal implications of AI in music production. 

## 4. DATASET DESCRIPTION 

The HAISP Dataset is accessible as a .csv and .xlsx on OSF under a Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC) license, which allows for broad access and utilization for research purposes.<sup>1</sup> 

## 4.1 Data Collection 

For submission to the contest each team had to fill in the AI Song Contest 2023 Submission Form via Google forms. The form consists of entry fields to upload the song and 

1 `https://creativecommons` . `org/licenses/by-nc/ 4` . `0/` 

398 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

|Category|Subcategory|Definition|
|---|---|---|
||Team_ID|The given label of the team for the dataset.|
||Number<br>of<br>Team<br>Members|The number of team members in a team.|
|Team Data|Type of Affiliation|The given work or personal affiliation of the team members.|
||Country|The given country(s) of origin of the team.|
||Found<br>Out<br>About<br>Contest|The way that the team discovered or were informed of the AI Song Contest.|
||Motivation to Partici-<br>pate in the Contest|The reason the team gave for joining the competition.|
||Song Length|The length of the submitted song given in minutes and seconds.|
|Son Data|Song Description|The short description of the song written for the contest website.|
|g|Final Ranking|Denotes the final ranking of the team’s song in the competition.|
||Song Title|The title of the song submitted to the AI Song Contest.|
||Song Concept|The overarching idea or theme of the song.|
|Process|Creation Process|The given order in which the separate pieces of the song, or potentially the<br>whole song, was created, as described by the team.|
||Melody|Whether an AI system was used to generate the melody.|
||Harmony|Whether an AI system was used to generate the harmony.|
|S El|Bassline|Whether an AI system was used to generate the bassline.|
|ong ements<br>|Drums|Whether an AI system was used to generate drum patterns or rhythms.|
|Use of AI|Formal Structure|Whether an AI system was used to generate the formal structure.|
||Lyrics|Whether an AI system was used to generate the lyrics of the song.|
||Voice Synthesis|Whether an AI system was used to generate the singing voice of the song.|
||Idea Generation|Whether an AI system was used to generate the idea for the song.|
|S P|Composing/Arranging|Whether an AI system was used to organize the elements of the song.|
|ong rocess<br>|Evaluation|Whether an AI system was used to evaluate the output or final song.|
|Use of AI|Mixing & Mastering|Whether an AI system was used to do the mixing and mastering of the<br>song|
||Performance|Whether an AI system is or would be used for live performance.|
|AI Tools Used|Model Used|The AI models as used and indicated by the teams in the song creation<br>process.|
||Database(s) Used|The databases as used and indicated by the teams in the training and song<br>creation process.|
|Ethical<br>Considerations|Diversity,<br>Ethical,<br>and Cultural Consid-<br>erations|Ethical and cultural considerations stated by the teams regarding their pro-<br>cess and use of AI.|
||Evaluation of Output|The words that teams used to assess the output of the AI system(s).|
|Human<br>Evaluation of|Evaluation of Process|The words that teams used to assess the process of working with the AI<br>system(s).|
|AI Co-Creation|Ownership|Teams statements regarding ownership of the system output and/or final<br>song.|
||Motivation to Use AI|The reasons that teams mentioned why they used AI in the process.|
|Other|Other|Additional information that does not fit in another category.|



Table 1. Categories of HAISP Dataset. The HAISP dataset consists of data collected in 31 categories in total. 

399 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

visual material (team image and song cover), and a freetext and multiple choice questionnaire. The questions that the teams filled in covered everything in these categories: 

- team (bio for the website, location, level of expertise, motivation to participate, how they heard about the AISC); 

- song (title, length, link to music video/soundcloud/ blogpost, concept/idea, lyrics, live performance); 

- human–AI process (short description for the website, models and databases used, steps of the process, creative vision, capabilities/limitations of AI tools in the creative process, workflow, collaboration with team members and AI, input data, ownership and conflict with intellectual property law); 

- and diversity, ethical and cultural considerations 

All teams had to further give consent for their answers description to be published in a scientific paper. 

The answers were collected automatically in a Google Sheet. In total there were 40 submissions collected with one being a corrective submission replacing an existing entry and four submissions being incomplete. After unanswered inquiry these submissions were excluded, leading to 35 participating teams in the 2023 edition. Their complete questionnaires were then handed over to the research group excluding any personal data. One process documentation (teamID: 2023_14) was submitted in Spanish which was excluded from the dataset for linguistic consistency. 

## 4.2 Data Statistics 

The HAISP dataset consists of the data from 34 teams of the 2023 edition of the AISC. Looking at the team data, there is a total of 104 team members involved, with an average of three members per team, and 14 countries represented. Of the countries represented, eight teams were based in the United States, six were based in the United Kingdom, and four were based in Guatemala, Sweden, and Germany. Other countries represented included South Korea, Spain, North Macedonia, and more. 

Type of affiliation – the given work or personal affiliation of the team members – was determined by coders based on the data, with teams being assigned multiple affiliations based on team members. A majority of the team members (58.8%) were members of academic field (20 mentions), meaning they worked primarily within academic institutions; this included universities, archives, or museums. A partially overlapping 44.1% of the team members were artists or worked in the creative industries, 17.6% worked as researchers outside academia, and 8.8% were classified as independent, (i.e., working in fields unrelated to the study/research/creation of AI or the creation of music but rather participating out of their own curiosity, hobby, or interest). 

Teams had primarily heard about the contest from academia (29%), web search, or participation in prior editions of the AISC. The motivation for why teams used AI 

in their process and why they decided to take part in the competition can be described as exploratory, while seven teams were also participating in order to display the use of their own or institutionally-created software. 

Regarding the AI tools, there were 74 different tools used by teams in the 2023 edition. On average, there were 2.17 tools used per team. Half of the teams used a form of GPT by OpenAI (e.g., ChatGPT) and 38.24% of the teams used tools by Google Magenta (e.g., Magenta Studio, Tensorflow, DDSP). Other tools that were frequently used were TransformerXL [40] (14.1%), AIVA (11.4%) or MusicGen by Meta (3 teams). There were 57 models that have been only used once. 

Looking at the use of AI in the compositional process, illustrated in Figure 1, it shows that 21 teams used only AI or co-created with AI for arranging, 18 teams used AI for idea generation and 10 (would) use AI in a performance. Nine teams mentioned the use of AI for mixing/mastering while only four teams used AI for evaluation of the output. Co-creation means this part was created by the human working with AI, human that only human was involved, AI that only AI was involved. Failed attempts to use AI in a specific step of the process were mentioned only in one case. Interestingly, the number of using “AI only” for these steps are low, with most uses (8) for “idea generation”. Only one team, 2023_28, mentioned a failed attempt to use AI in a specific step of the process: mixing and mastering. 

Looking at the use of AI to create the elements of the songs – melody, harmony, bassline, drums, formal structure, lyrics, voice – depicted in Figure 2, 29 teams used AI, either in co-creation or solely for melody, while 19 used it for harmony and lyrics. Interestingly, while for melody, harmony, bassline, and drums the co-creation outweighs the AI-only approach, this is the opposite for formal structure, lyrics and voice synthesis. Team 2023_20 was the only team reporting a failed use of AI for creating harmony and voice synthesis with AI. 

The teams’ own writings on their song concepts, their described creation process, their evaluation of diversity and ethical issues within said process, their thoughts on ownership of the song, and their overall evaluation of their human-AI co-creation process and the outcome of said process can be found in the dataset and can be used for further analysis. 

## 4.3 Methodology and Validation 

After reviewing the initial survey responses, we proceeded to create the data dictionary through a mixed-methods approach. The categories were created inductively by five researchers, iterating four times to reach final consensus. For each iteration of the data dictionary, two coders tested it on two sample entries to ensure that the categories were properly defined and applicable for the data. 

We generated the dataset via consensus coding [41]. One researcher coded a selection of the data entries, collecting them into the dataset. A second coder then reviewed the initial coding, validating the coding by either 

400 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 



<!-- Start of picture text -->
Use of Al in the Process<br>Idea Generation 8 10 16<br>ComgAging 5 16 13<br>Al only<br>Evaluation13 HumanCo-Creation<br>Part of the Proce s Failed<br>Mixing & Mastering 3 6 16<br>Performance 3 18<br>0 5 10 15 20 25 0E 35<br>Number of Uses<br><!-- End of picture text -->

Figure 1. Overview of the Use of AI for the Compositional Process in HAISP: Idea Generation, Arrangement, Evaluation, Mixing & Mastering, Performance. 

citing a +1 for agreement with the coding choices or -1 for disagreement with the coding within the dataset, adding what they felt the coder was missing within their codes from the data. In the case of disagreement a third researcher helped decide on the final code as a tie-breaker. 

## 4.4 Ethical Considerations 

The study was approved by the university Institutional Review Board. When submitting to the contest, one question in the submission form asked directly and transparently for the team’s consent for their song and documentation to be used for research purposes. Teams gave consent by ticking a box in the form. While we erased all personal data from the dataset, song names are included due to their public availability on the AI Song Contest website. 

## 5. USE CASE AND APPLICATIONS 

Our dataset can be used to understand a variety of MIR tasks and work related to human-AI creative interactions, ranging from goals focused on research to practical creation of music. This section presents four possible use cases. 

## 5.1 Use Case 1: More Insights on the AI Tools used in the Songwriting Process 

HAISP lists not only all AI tools that teams used and indicated, but also contains the teams’ description of the process of utilizing said tools, with data showing which parts of the creative process (idea generation, composition, mixing/mastering, performance) AI was used on its own, in cocreation with the team, or even when co-creation with the AI system failed. Additionally, it reports the teams’ level of expertise and location. This provides not only valuable insights for tool developers and inspiration or guidance on using AI for other artists but also helps to answer research questions such as “How does the utilization of AI tools in music creation vary across different professional affiliations and stages of the creative process?” 



<!-- Start of picture text -->
Use of Al in the Process<br>Melody 10 19<br>Harmony 5 14<br>Bassline 3 10<br>Drums 4 6<br>Part of the SongFormal Structure 8 18<br>Lyrics 10 6 Al onlyCo-Creation<br>Human<br>Voice 9 Failed<br>0 5 10 15 20 25 30<br>Number of Uses<br><!-- End of picture text -->

Figure 2. Overview of the Use of AI for the Elements of the Song in HAISP: Melody, Harmony, Bassline, Drums, Formal Structure, Lyrics and Voice. 

## 5.2 Use Case 2: Understanding Attitudes and Impact of AI on the Creative Process 

Within our dataset, there is reference to how creators use AI within their process, as well as their perceptions around the capabilities and limitations of AI. Additionally, creators share their perceptions of the final creation resulting from their collaboration with AI, providing valuable insights into the impact of AI on artistic expression and creative outcomes. 

In their work Beyond Diverse Datasets [36], Huang et al. pose questions such as “What is valuable to those communities [that MIR investigates] and what is valuable to the community contributing to MIR?” and “How do musical communities wish for their practices to interact with emerging technologies (if at all), and what do they consider as potential misuses of their traditions?”. Our dataset offers a unique opportunity to start exploring these questions, drawing from the diverse perspectives of creators from various cultural, educational, and experiential backgrounds. By analyzing the reflections and experiences of creators documented in the dataset, researchers can gain insights into how different musical communities perceive and interact with AI technologies in their creative practices. 

## 5.3 Use Case 3: Gaining Insight into Users’ Understanding of Ethics Around H-AI Co-Creation 

Ethical considerations and questions about the validity of data were found frequently in the responses of AISC participants. Working with AI tools during the creation process can trigger questions around control [42], ownership of the final output [43], and freedom of personal expression [44]. Additionally, many participants spoke on the issue of AI systems and tools used during their process potentially being trained on datasets that violate the intellectual property rights of the original artists. 

By examining how creators navigate ethical considerations in their process, researchers can uncover how AI tools are adopted and used within different musical traditions. This deeper understanding can inform discussions around the ethical implications of AI in music creation and 

401 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

contribute to the development of responsible approaches to AI-driven creativity. One research question that this data can provide insight on is “What are the ethical considerations and challenges faced by creators when utilizing AI tools in their creative process, and how do these considerations impact their creative workflows?” 

## 5.4 Use Case 4: Execution of Creative Possibilities 

Our dataset can be used to understand the ways in which AI tools can expand the range of creative possibilities in songwriting and music creation. By leveraging this dataset, researchers can analyze how AI models have allowed users to generate innovative methods to address creative challenges, potentially expanding beyond the field of music creation into other creative fields. 

One research question that can be explored with this dataset is “How do AI tools, particularly those leveraging big data and machine learning techniques, expand the creative possibilities in songwriting and music creation, and what novel approaches to executing creative problems do they enable?”. Specifically, one can explore the utilization of big data and machine learning techniques to address challenges such as data processing, limited musical ability, and idea generation. For example, AI-powered algorithms can analyze vast amounts of musical data to identify patterns and trends, providing inspiration for melody creation, chord progressions, and rhythmic structures. Additionally, machine learning techniques can assist in data processing tasks focused on mechanisms of creation, enabling creators to focus more on the higher level of creation process in music composition [45]. 

Extending the scope of research beyond music creation into other creative fields, researchers can use HAISP to examine how AI algorithms are applied to address creative challenges and gain insight into the broader implications of AI for fostering creativity and innovation. 

## 6. COMPARISON WITH OTHER DATASETS 

There are extensive datasets of AI-based music tools that focus on the methods of the respective AI systems [7] or reviews of AI-based music tools that focus on the metadata of the publication [1]. Another way to approach the topic of AI-supported creative processes is analyzing interfaces of AI-supported tools for creative endeavors [37]. In the MIR community, datasets are common, especially quantitative datasets and training datasets. Apart from [2], who analyzed the creation process of the first AISC teams, there have been no datasets consisting of qualitative data of the human-AI co-creation process released in MIR venues. The HAISP dataset presented in this paper, is a qualitative dataset of a substantial amount of curated user data, including a subjective description and evaluation of the process, practices, and ethical issues around the creative process with AI. Due to the international character of the AISC – with teams from over 20 countries in the 2023 edition alone – these descriptions come from individuals with diverse cultural backgrounds and musical traditions, which 

is shown in their reflections and experiences. 

The limited amount of data makes HAISP unsuitable for making general and widely applicable statements about human-AI interaction in songwriting. Rather, we see HAISP as a dataset that can be used to extend existing research in various academic disciplines, as it gives very detailed and rich insights that are well-suited to compliment quantitative research insights. Therefore, we made HAISP publicly available and encourage researchers from different fields to work with the data, bringing in their respective perspectives and methods in order to foster an interdisciplinary dialogue on human-AI co-creation. 

## 7. CONCLUSION 

In conclusion, the Human-AI Songwriting Processes dataset stands as a potentially significant resource for the exploration of human-AI collaboration and creativity in music composition. Curated from submissions to the AI Song Contest, this dataset offers a view of the dynamics underlying AI-supported songwriting processes. It provides valuable insights into how creators from diverse backgrounds integrate AI tools into their creative workflows, reflecting on the capabilities, limitations, and ethical considerations inherent in human-AI collaboration. Furthermore, the adoption of the HAISP dataset has the potential to advance interdisciplinary inquiry, inspire further research, and contribute to ongoing discourse surrounding human-AI collaboration and creativity. By fostering critical inquiry and facilitating informed discourse, this dataset contributes to our understanding of technology’s role in creativity and innovation in the digital age. Future work on the Human-AI Songwriting Processes dataset will involve expanding the dataset to include information from participants in the AI Song Contest prior to 2023, enriching the dataset with a broader range of submissions and perspectives. Additionally, there are plans to conduct further analysis on the dataset, including analysis to explore the descriptive terminology used for AI tools and systems. In closing, the HAISP dataset holds promise for advancing our understanding of human-AI collaboration in music composition. Through its insights and reflections, it encourages continued exploration of the dynamic relationship between human creativity and machine intelligence. 

## 8. ACKNOWLEDGMENTS 

We thank all organizers and former co-organizers of the AI Song Contest, Anna Huang, Rujing Stacey Huang and Vincent Koops for their contribution in organizing this event. We also thank Aarushi Buddhavarapu for their contribution to the coding on this project. 

## 9. REFERENCES 

- [1] M. Civit, J. Civit-Masot, F. Cuadrado, and M. J. Escalona, “A Systematic Review of Artificial Intelligence-based Music Generation: Scope, Ap- 

402 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

plications, and Future Trends,” Expert Systems with Applications, vol. 209, pp. 118–190, 2022. 

- [2] C.-Z. A. Huang, H. V. Koops, E. Newton-Rex, M. Dinculescu, and C. J. Cai, “AI Song Contest: HumanAI Co-Creation in Songwriting,” in 21st International Society for Music Information Retrieval Conference, 2020. 

- [3] I. Xenakis, Formalized Music: Thought and Mathematics in Composition: Thoughts and Mathematics in Composition. Pendragon Press, 1992. 

- [4] E. Frid, C. Gomes, and Z. Jin, “Music Creation by Example,” in Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems, 2020, pp. 1–13. 

- [5] R. T. Dean and A. McLean, The Oxford Handbook of Algorithmic Music. Oxford University Press, 2018. 

- [6] J. J. Bharucha and P. M. Todd, “Modeling the Perception of Tonal Structure with Neural Nets,” vol. 13, no. 4, pp. 44–53, 1989, publisher: The MIT Press. 

- [7] J.-P. Briot, G. Hadjeres, and F.-D. Pachet, Deep Learning Techniques for Music Generation, ser. Computational Synthesis and Creative Systems. Cham: Springer International Publishing, 2020. 

- [8] C.-Z. A. Huang, C. Hawthorne, A. Roberts, M. Dinculescu, J. Wexler, L. Hong, and J. Howcroft, “The Bach Doodle: Approachable Music Composition with Machine Learning at Scale,” in 20th International Society for Music Information Retrieval Conference, 2019. 

- [9] T. Bazin and G. Hadjeres, “NONOTO: A Modelagnostic Web Interface for Interactive Music Composition by Inpainting,” in International Conference on Computational Creativity 2019, 2019, pp. 89–91. 

- [10] O. Lopez-Rincon, O. Starostenko, and G. A.-S. Martín, “Algoritmic music composition based on artificial intelligence: A survey,” in 2018 International Conference on Electronics, Communications and Computers (CONIELECOMP), 2018, pp. 187–193. 

- [11] G. Hadjeres, F. Pachet, and F. Nielsen, “DeepBach: a Steerable Model for Bach Chorales Generation,” in International Conference on Machine Learning. PMLR, 2017, pp. 1362–1371. 

- [12] A. Shaw, “A Multitask Music Model with Bert, transformer-xl and seq2seq,” 2019. [Online]. Available: https://towardsdatascience.com/a-multitaskmusic-model-with-bert-transformer-xl-and-seq2seq3d80bd2ea08e 

- [13] D. Ippolito, A. Huang, C. Hawthorne, and D. Eck, “Infilling Piano Performances,” in NIPS Workshop on Machine Learning for Creativity and Design, vol. 2, no. 5, 2018. 

- [14] C.-J. Chang, C.-Y. Lee, and Y.-H. Yang, “VariableLength Music Score Infilling via XLNet and Musically Specialized Positional Encoding,” in Proceedings of the 22nd International Society for Music Information Retrieval Conference, 2021. 

- [15] C. Donahue, I. Simon, and S. Dieleman, “Piano Genie,” in Proceedings of the 24th International Conference on Intelligent User Interfaces, 2019, pp. 160–164. 

- [16] K. Tahiroglu, M. Kastemaa, O. Koli et al., “Al-terity: Non-Rigid Musical Instrument with Artificial Intelligence Applied to Real-Time Audio Synthesis,” in International Conference on New Interfaces for Musical Expression, 2020, pp. 337–342. 

- [17] C. Benetatos and Z. Duan, “BachDuet: A Deep Learning System for Human-Machine Counterpoint Improvisation,” Proceedings of the International Conference on New Interfaces for Musical Expression, 2019. 

- [18] S. Fukayama, K. Yoshii, and M. Goto, “ChordSequence-Factory: A Chord Arrangement System Modifying Factorized Chord Sequence Probabilities,” in 14th International Society for Music Information Retrieval Conference, 2013, pp. 457–462. 

- [19] C.-Z. A. Huang, D. Duvenaud, and K. Z. Gajos, “ChordRipple: Recommending Chords to Help Novice Composers Go Beyond the Ordinary,” in Proceedings of the 21st International Conference on Intelligent User Interfaces, 2016, pp. 241–250. 

- [20] M. Navarro-Caceres, M. Caetano, G. Bernardes, and L. N. de Castro, “Chordais: An Assistive System for the Generation of Chord Progressions with an Artificial Immune System,” Swarm and Evolutionary Computation, vol. 50, p. 100543, 2019. 

- [21] C. M. Wilk and S. Sagayama, “Automatic Music Completion Based on Joint Optimization of Harmony Progression and Voicing,” Journal of Information Processing, vol. 27, pp. 693–700, 2019. 

- [22] H. V. Koops, J. P. Magalhaes, and W. B. De Haas, “A functional approach to automatic melody harmonisation,” in Proceedings of the first ACM Workshop on Functional Art, Music, Modeling, and Design, 2013, pp. 47–58. 

- [23] T.-P. Chen and L. Su, “Attend to Chords: Improving Harmonic Analysis of Symbolic Music Using Transformer-Based Models,” Transactions of the International Society for Music Information Retrieval, vol. 4, no. 1, pp. 1–13, 2021. 

- [24] I. Simon, D. Morris, and S. Basu, “MySong: Automatic Accompaniment for Vocal Melodies,” in Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, 2008, pp. 725–734. 

403 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

- [25] C.-H. Chuan and E. Chew, “A hybrid system for automatic generation of style-specific accompaniment,” in Proceedings of the 4th International Joint Workshop on Computational Creativity, 2007, pp. 57–64. 

- [26] S. Oramas, F. Barbieri, O. Nieto Caballero, and X. Serra, “Multimodal Deep Learning for Music Genre Classification,” Transactions of the International Society for Music Information Retrieval, pp. 4–21, 2018. 

- [27] D. Schneider, N. Korfhage, M. Mühling, P. Lüttig, and B. Freisleben, “Automatic Transcription of Organ Tablature Music Notation with Deep Neural Networks,” Transactions of the International Society for Music Information Retrieval, vol. 4, no. 1, pp. 14–28, 2021. 

- [28] H. Cuesta and E. Gómez Gutiérrez, “Voice Assignment in Vocal Quartets Using Deep Learning Models Based on Pitch Salience,” Transactions of the International Society for Music Information Retrieval, 2022. 

- [29] P. Torras, A. Baró, L. Kang, and A. Fornés, “On the Integration of Language Models into Sequence to Sequence Architectures for Handwritten Music Recognition,” in Proceedings of the 22nd International Society for Music Information Retrieval Conference, 2021, pp. 690–696. 

- [30] B. Meléndez-Catalán, E. Molina, and E. Gómez, “Open Broadcast Media Audio from TV: A Dataset of TV Broadcast Audio with Relative Music Loudness Annotations,” Transactions of the International Society for Music Information Retrieval, vol. 2, no. 1, pp. 43–51, 2019. 

- [31] S. Schwär, M. Krause, M. Fast, S. Rosenzweig, F. Scherbaum, and M. Müller, “A Dataset of Larynx Microphone Recordings for Singing Voice Reconstruction,” Transactions of the International Society for Music Information Retrieval, 2024. 

- [32] S. Rosenzweig, F. Scherbaum, D. Shugliashvili, V. Arifi-Müller, and M. Müller, “Erkomaishvili Dataset: A Curated Corpus of Traditional Georgian Vocal Music for Computational Musicology,” Transactions of the International Society for Music Information Retrieval, vol. 3, no. 1, pp. 31–41, 2020. 

- [33] Q. Kong, B. Li, J. Chen, and Y. Wang, “GiantMIDIpiano: A large-scale MIDI dataset for classical piano music,” Transactions of the International Society for Music Information Retrieval, vol. 5, no. 1, pp. 87––98, 2022. 

- [34] F. Zalkow, S. Balke, V. Arifi-Müller, and M. Müller, “MTD: A Multimodal Dataset of Musical Themes for MIR Research,” Transactions of the International Society for Music Information Retrieval, vol. 3, no. 1, pp. 180–192, 2020. 

- [35] G. Meseguer-Brocal, A. Cohen-Hadria, and G. Peeters, “Creating DALI, a Large Dataset of Synchronized Audio, Lyrics, and Notes,” Transactions of the International Society for Music Information Retrieval, vol. 3, no. 1, pp. 55–67, 2020. 

- [36] R. S. Huang, A. Holzapfel, B. L. T. Sturm, and A.-K. Kaila, “Beyond Diverse Datasets: Responsible MIR, Interdisciplinarity, and the Fractured Worlds of Music,” Transactions of the International Society for Music Information Retrieval, vol. 6, no. 1, pp. 43–59, 2023. 

- [37] J. Rezwana and M. L. Maher, “User Perspectives on Ethical Challenges in Human-AI Co-Creativity: A Design Fiction Study,” in C&C ’23: Creativity and Cognition, 2023, pp. 62–74. 

- [38] K. Lee, G. Hitt, E. Terada, and J. H. Lee, “Ethics of Singing Voice Synthesis: Perceptions of Users and Developers,” in Proceedings of the 23rd International Society for Music Information Retrieval Conference, 2022. 

- [39] J. A. Biles, “GenJam: A Genetic Algorithm for Generating Jazz Solos,” in Proceedings of the 1994 International Computer Music Conference, 1994, p. 8. 

- [40] Z. Dai, Z. Yang, Y. Yang, J. Carbonell, Q. V. Le, and R. Salakhutdinov, “Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context,” in Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics, 2019. 

- [41] C. E. Hill, S. Knox, B. J. Thompson, E. N. Williams, S. A. Hess, and N. Ladany, “Consensual qualitative research: An update,” Journal of Counseling Psychology, vol. 52, no. 2, pp. 196–205, 2005. 

- [42] N. Davis, C.-P. Hsiao, K. Y. Singh, and B. Magerko, “Co-Creative Drawing Agent with Object Recognition,” in Proceedings of the AAAI Conference on Artificial Intelligence and Interactive Digital Entertainment, vol. 12, no. 1, 2016, pp. 9–15. 

- [43] J. Rezwana and M. L. Maher, “User Perspectives of the Ethical Dilemmas of Ownership, Accountability, Leadership in Human-AI Co-Creation,” in Joint Proceedings of the ACM IUI Workshops, 2023. 

- [44] D. Buschek, L. Mecke, F. Lehmann, and H. Dang, “Nine Potential Pitfalls when Designing Human-AI Co-Creative Systems,” in Joint Proceedings of the ACM IUI 2021 Workshops, 2021. 

- [45] M. Newman, L. Morris, and J. H. Lee, “Human-AI Music Creation: Understanding the Perceptions and Experiences of Music Creators for Ethical and Productive Collaboration,” in Proceedings of the 24th International Society for Music Information Retrieval Conference, 2023, pp. 80–88. 

404 

