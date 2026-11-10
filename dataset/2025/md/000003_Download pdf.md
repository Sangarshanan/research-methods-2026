---
paper_id: "000003"
year: 2025
title: "Download pdf"
source_url: "https://zenodo.org/record/17706323/files/000003.pdf"
---

# EXPANDING THE HAISP DATASET: AI’S IMPACT ON SONGWRITING ACROSS TWO AI SONG CONTESTS 

Lidia Morris<sup>1</sup> Michele Newman<sup>1</sup> Xinya Tang<sup>1</sup> Renee Singh<sup>1</sup> Marcel Vélez Vásquez<sup>2</sup> Rebecca Leger<sup>3</sup> Jin Ha Lee<sup>1</sup> 

1 Information School, University of Washington 

2 University of Amsterdam 

3 Fraunhofer Institute for Integrated Circuits 

```
CorrespondenceAuthor@ismir.edu,PossibleOtherAuthor@ismir.edu
```

## ABSTRACT 

As artificial intelligence (AI) continues to shape creative practices, understanding its role in human-AI songwriting remains crucial. This paper expands the Human-AI Songwriting Processes (HAISP) dataset by incorporating data from the 2024 AI Song Contest, building upon the original 2023 dataset. By analyzing new submissions, we provide further insights into AI’s evolving impact on songwriting workflows, creative decision-making, and control. A comparative study of AI tool usage and participant strategies between the 2023 and 2024 contests reveals shifts in collaboration patterns and tool effectiveness. Additionally, we assess the differences between general-purpose AI systems and personalized, fine-tuned tools, highlighting their impact on creative agency. Our findings offer key design implications for AI-assisted songwriting tools, providing actionable insights for AI developers and music practitioners seeking to enhance co-creative experiences. 

## 1. INTRODUCTION 

Artificial Intelligence (AI) has rapidly become an integral component of creative fields, reshaping artistic expression across various domains. From visual arts to literature, AIpowered tools are being leveraged to augment human creativity, raising new questions about authorship, originality, and the evolving nature of co-creation [1–3]. Nowhere is this transformation more evident than in music composition, where AI systems are increasingly employed to generate melodies, harmonies, lyrics, and entire song structures [4, 5]. These advancements have given rise to new forms of collaboration between human musicians and AI, necessitating a deeper understanding of the dynamics of human-AI co-creation in songwriting. 

The study of human-AI collaboration in music is particularly important due to the complex, often subjective 

> © L. Morris, M. Newman, X. Tang, R. Singh, M.A. Vélez Vásquez, R. Leger, and J.H Lee. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: L. Morris, M. Newman, X. Tang, R. Singh, M.A. Vélez Vásquez, R. Leger, and J.H Lee, “Expanding the HAISP Dataset: AI’s Impact on Songwriting Across Two AI Song Contests”, in Proc. of the 26th Int. Society for Music Information Retrieval Conf., Daejeon, South Korea, 2025. 

nature of the creative process. While AI can accelerate composition workflows and generate novel musical ideas, its role in enhancing versus replacing human creativity remains a critical area of investigation [6, 7]. Furthermore, questions regarding our changing definition of computational creativity and the role AI can play in the creative process as a tool or collaborator continue to loom large over the field [8, 9]. Addressing these concerns requires qualitative data that captures not just empirical information on the use of generative AI, but the lived experiences of creators working with AI in music production. 

To contribute to this growing field of study, the Human–AI Songwriting Processes (HAISP) dataset was introduced in 2024 as a curated resource designed to explore the interaction between human musicians and AI systems [10]. The dataset was derived from submissions to the AI Song Contest 2023, an annual competition that invites teams of musicians, data scientists, and researchers to explore the creative potential of AI in songwriting [11]. It comprises 34 coded entries documenting how teams used AI tools in their songwriting processes. It provides a structured framework for analyzing various aspects of AIassisted music creation, including: 

- The specific AI tools and models used in composition 

- The songwriting methodologies employed by human-AI teams 

- Reflections on ethical considerations and challenges related to AI in music 

- Teams’ assessments of their collaborative experience with AI 

The findings from the HAISP dataset highlighted the diverse ways in which AI is integrated into songwriting, with teams using AI for tasks ranging from melody generation to performance synthesis. However, the dataset also underscored the limitations of AI tools, such as lack of creative control, technical limitations, and concerns about originality. In addition, ethical concerns regarding the provenance of data and the transparency of AI-generated content emerged as key themes. 

28 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

Building on this foundation, the current study extends the HAISP dataset by incorporating new data from the 2024 AI Song Contest, offering a longitudinal perspective on the evolution of human-AI collaboration in songwriting. By comparing data from 2023 and 2024, this expanded dataset enables a deeper analysis of trends, emerging technologies, and shifting attitudes toward AI in creative work. Through this research, our goal is to provide valuable information for musicians, AI developers, creativity scholars, and beyond. 

## 2. BACKGROUND 

The intersection of AI and music composition represents a rapidly evolving field that has a long history to explore. AI-assisted music creation has progressed from early algorithmic experiments and academic electronic music centers [12] to sophisticated machine learning models capable of composing complete musical pieces by the broader public [13]. As these technologies become more accessible, they not only influence the way music is made but also raise critical ethical, cultural, and artistic questions about human-AI co-creation. 

## 2.1 Evolution of AI in Music Composition 

The application of computational techniques in music composition can be traced back to the mid-twentieth century, when early pioneers experimented with algorithmic approaches to sound generation [13], such as the work completed at the Columbia-Princeton Electronic Music Center, which laid the groundwork for a variety of composers careers and technological innovations [12, 14]. By the early 2000s, developments in machine learning facilitated the creation of models that could autonomously generate melodies, harmonies, and song structures [15,16]. 

The increasing sophistication of deep learning and generative AI in the past decade has further transformed the landscape of music composition. Notable advances include OpenAI’s MuseNet, Google’s Magenta, and Meta’s MusicGen, all of which employ transformer-based architectures to produce diverse compositions [17–19]. These tools enable musicians to collaborate with AI in various ways, from generating musical ideas to assisting with arrangement, and more [19]. The growing accessibility of these technologies has been showcased in platforms such as the AI Song Contest (AISC) [11]. 

an inexperienced music creator [2, 11, 21]. AI-generated music is often constrained by its training data, leading to concerns about predictability, stylistic homogenization, and the potential for AI to reinforce existing musical conventions rather than foster true innovation [22, 23]. Furthermore, the extent to which AI-generated compositions can be considered “creative” in the same sense as humanauthored works is still being questioned, especially when it comes to just how much of a role the AI plays in the compositional process [24,25]. 

## 2.3 Creativity Studies 

The increasing adoption of AI in creative domains has sparked debates about the nature of creativity and the role of machines in artistic expression [11,26–28]. Traditional views of creativity emphasize human intuition, cultural context, and emotional depth [29–31] - qualities that AI, as a statistical modeling system, does not inherently possess. Can AI truly be considered a creative agent, or is it merely an advanced tool for pattern recognition and recombination? Ethical concerns also extend to the implications of AI’s increasing role in the creative workforce [32, 33]. As AI-generated compositions become more sophisticated, there is a potential for automation to displace human musicians in certain commercial contexts [34]. In response to these challenges, scholars and industry professionals have called for greater transparency in AI training data, ethical guidelines for AI-assisted composition, and policies to ensure that human artists remain central to the creative process [35]. 

## 3. DATASET EXPANSIONS: METHODOLOGY 

The HAISP Dataset is accessible as a .csv and .xlsx on the Open Science Framework (OSF) under a Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC) license, which allows for broad access and utilization for research purposes [36]. 

We generated the dataset via consensus coding [37]. One researcher coded a selection of the data entries, collecting them into the dataset. A second coder then reviewed the initial coding, validating the coding by either marking agreement or disagreement with the coding choices within a comment on the code in the dataset, adding what they felt the coder was missing within their codes from the data. In the case of disagreement, a third researcher helped decide on the final code as a tie-breaker. 

## 2.2 AI Songwriting Tools and Methods 

Various AI-powered tools have emerged to facilitate human-AI collaboration in songwriting. OpenAI’s MuseNet [20] is a deep neural network capable of composing multi-instrumental pieces across multiple genres, while Google’s Magenta project provides open-source applications for AI-assisted melody generation, chord progression, and rhythm creation [18]. While these tools offer new creative possibilities, they also introduce challenges related to artistic control, originality, and the implications of AI as a co-creative entity, especially when the user is 

## 3.1 Data Collection 

Similarly to the 2023 practice, each team had to fill in the AI Song Contest 2024 Submission Form via Google Forms to participate in the contest [10]. The form consists of entry fields that cover all the basic information about teams and songs: 

- team (bio for the website, location, level of expertise, motivation to participate, how they heard about the AISC); 

29 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- song (title, length, link to music video/soundcloud/ blogpost, concept/idea, lyrics, live performance). 

Each team was additionally asked to generate a process document and save it as a PDF file, which mainly includes more detailed motivation, songwriting workflow and collaboration process, evaluation of co-creation, and ethical considerations. In this way, each team had more space to elaborate on their collaboration process than in previous submissions. 

Furthermore, all teams had to give their consent for their responses to be published in a scientific paper. The answers were collected into a Google Sheet with links to outstanding PDF files. In total, 67 submissions were collected, including 34 submissions that used text-to-music models such as Udio and/or Suno in the human-AI collaboration process and thus were considered disqualified due to the judges inability to "assess the level and manner of the use of AI in each entry" and an inability to obtain "a description of the data used to train the AI model." [38] After these 34 submissions were excluded, 33 effective participating teams remain in the 2024 edition. The completed questionnaires were then handed over to the research group excluding personal data. 

## 3.2 Methodology and Validation 

Due to the change in participant entry methods and submission format, the data dictionary from the initial HAISP dataset was adapted by the coders to better extract the data essential to the dataset from the written entries. The categories were evaluated one by one by the four researchers, iterating three times, with testing of each new adaptation to the dictionary before reaching final consensus. For each iteration of the data dictionary, two coders tested it on two sample entries to ensure that the categories were properly defined and applicable for the new data. 

## 3.3 Data Statistics 

The HAISP dataset for the 2024 edition consists of data from 33 teams, representing 22 different countries and regions. The United States has the highest representation, with 12 teams participating. The United Kingdom follows with four teams, while Switzerland has three. Germany and Spain are each represented by two teams. 

Other represented countries include the Netherlands (NLD), Colombia (COL), Japan (JPN), Italy (ITA), Brazil (BRA), Thailand (THA), Canada (CAN), France (FRA), Tunisia (TUN), Denmark (DNK), Hungary (HUN), Turkey (TUR), China (CHN), and Chile (CHL). 

The type of affiliation of the HAISP dataset 2024 edition reflects a significant shift compared to the 2023 edition. The most notable change is a clear trend away from participants typically coming from academic backgrounds toward those who work in the creative industry, suggesting a growing engagement of professional artists and creatives with AI-driven music composition, in artistic and commercial sectors rather than academic research setting. In 2023, 

58.8% of participants were affiliated with academia, making it the dominant category. However, in 2024, academic affiliation dropped to just 19.57%, while the creative industry surged to 58.7%, making it the largest represented category in this year’s dataset. 

The HAISP dataset for the 2024 edition of the AISC showcases a diverse array of AI models and tools employed by participating teams. Compared to the 2023 edition, which saw the usage of 74 different AI tools, the 2024 dataset reflects an even broader spectrum of AI applications with 82 different AI tools, excluding the other tools used by the disqualified participants. These tools include AI-powered music generation models, voice cloning software, AI-driven mixing and mastering tools, AI-assisted composition platforms, and more. Some teams utilized publicly available AI tools like Musicfy or Kits.ai, while others employed custom-built AI models tailored to their specific creative needs, like Purr Data. 

A significant portion (42%) of teams in 2024 continued to use ChatGPT and OpenAI’s GPT-based models for lyrics, structure, and creative assistance. Additionally, the rise of Stability AI models, such as Stable-Audio-Open 1.0 and Stable Diffusion XL, suggests a growing reliance on AI for both music generation and visual content creation. 

## 4. COMPARATIVE ANALYSIS 

The HAISP dataset reveals that while AI-assisted songwriting can enhance creativity and efficiency, musicians frequently encounter challenges related to control, transparency, and process integration when working with AI tools. Several recurring themes, as presented below, emerge from the dataset that highlight the limitations of current AI models. 

## 4.1 Control 

Twelve participating teams expressed frustration over the lack of fine-grained control over AI-generated outputs, especially when it comes to using the more popular and easily accessible AI systems. Users specifically choose systems that allow for greater control and flexibility over the outputs, highlighting systems whose affordances allow them to control “...mechanisms such as text/audio prompting and loop generation” (Team 63). With systems that do not allow for such user modifications, many feel that the results are limited, and “...mostly based on seed luck and good prompting” (Team 28). One team in particular noted that they chose to use an AI tool created by ElevenLabs [39] not only because they felt it allowed for “greater control,” (Team 52) but because of their ethical stance as a team, noting that ElevenLabs was more ethically transparent in the creation of its music database, using only licensed content from Shutterstock [40]. Decisions about tools are not only based on control over the process or output, but also on the team’s control over how to accommodate or apply their ethical positions. 

The 2024 HAISP dataset expansion reinforces many of the themes from the 2023 dataset, particularly in regards to 

30 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 



<!-- Start of picture text -->
Al Song Contest Participants by Affiliation<br>40<br>30 Affiliation<br>Academic<br>Creative Industry<br>20 Independent<br>Industry Research<br>Number of Part i cpants10<br>2023 2024<br>Year<br><!-- End of picture text -->

Figure 1. Bar Chart comparing the affiliation of AI Song Participants in 2023 and 2024, showcasing an increase in creative industry affiliation and decrease in academic affiliation. 

maintaining control over their creation process. In 2023, teams frequently encountered rigidity and limitations when working with AI tools, as exemplified by 2023’s Team 13’s experience working with Meta’s MusicGen. Initially “fascinated” by the outcomes that came from this tool, they soon realized the tool produced repetitive results, and further attempts to refine the output resulted in “...an unwelcome surplus of noise, leading to a sense of limitation.” This led them to switch to Google’s Magenta so they could have more control over the MIDI outputs. Other 2023 teams such as Team 16 also noted that text-to-music models frequently needed more specific and detailed prompting that included information on the key and tempo in order to avoid the “...incoherent and sometimes noisy outputs.” Overall, teams from both years show a stronger preference for AI tools that allow for real-time adjustments, iterative prompting, and clear ethical stances so they can actively and continuously make choices that give them the control they desire over the creative process. 

## 4.2 Applications of AI 

In the 2024 data, we noted that participants on average used 2-3 times more AI tools than the 2023 participants. 2024 AISC participants leveraged AI for melody and harmony generation, using models to produce initial musical ideas that were later refined through human music production stages like mixing and mastering. Voice synthesis was another key application, with AI tools transforming vocal performances or generating synthetic voices that could be adjusted to fit the song’s artistic vision. Unlike 2023, the majority of the tools used were openly available tools, and not custom-built and trained models. Tools like Stable Audio, ElevenLabs, and ChatGPT 3.5/4.0 were amongst the most commonly used tools in the 2024 dataset. 

In contrast, 2023’s teams often employed AI tools it- 

eratively, using them to refine compositions and lyrics throughout the process, which is described more as a recursive workflow than step-by-step, with their AI tool “...providing creative suggestions and helping us iterate more efficiently” (Team 26). The iterative process means that teams could listen to their AI-generated song elements and add on to them with human elements as their submission developed, rather than having the element be a generated piece that cannot be recreated exactly, even with the same prompts. 2024’s Team 38 described their frustration with this issue, writing that "The problem with all of this, and what makes this workflow so granular, is the AI starts to drift over time, losing sight of one aspect of the prompt in favor of another; outputs begin to differ in length, timbre, language (for some reason) but most importantly tempo." Additionally, many of the tools used by the 2023 participants were either built by the teams or were open source models that were trained by the team. In 2023, large-scale AI systems like ChatGPT were mostly used to create suggestions or generate ideas for song elements such as the melody, which was then played and recorded on real instruments by participants, or lyrics, which were then sung by a separate AI tool or human team member. 

## 4.3 Co-Creation vs. Automation 

The dataset indicates a strong preference for collaborative AI tools over fully automated music generators. Many artists want AI to function as an assistive tool rather than an autonomous composer. Users express interest in AI systems that respond dynamically to their inputs, rather than generating static musical pieces that require extensive manual revision. As Team 28 noted, it was not just that utilizing an AI tool that made the work co-creative, but the combination of their own musical training and skills and the work of the AI tools which allowed for "... a seamless 

31 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

blend [of] human artistry and technological innovation." 

## 5. DESIGN PRINCIPLES FOR MUSIC GENERATIVE AI 

## 5.1 Interactive and Adaptive AI Systems 

One issue with the 2024 dataset that highlights the distinction between co-creation and automation was the 34 teams that were disqualified due to their use of Suno or Udio, text-to-music AI model. Because Suno and Udio generate fully formed musical pieces - bypassing the creative decision-making process and critical discernment of data sourcing methods that the AISC expects teams to engage in - the use of the application, and other text-tomusic models, was highly discouraged unless participants could show they used their AI outputs in a creative manner. This highlights the shifting perceptions of ownership when it comes to AI-assisted songwriting, at least in some parts of the MIR community. While users often see AI as a tool to enhance their creative process, competitions like the AI Song Contest uphold a stricter interpretation of human-AI collaboration, emphasizing that AI should be used as an assistive technology rather than a replacement for human creativity. The question of ownership becomes especially complex in this context: participants engaging with co-creative AI tools see themselves as the primary authors, shaping and curating AI-generated elements, whereas models like Suno, which produce near-complete compositions, blur the boundaries of authorship. The contest’s decision to disqualify Suno users reflects an evolving discourse around the role of AI in music-making—-one that increasingly privileges human creative agency over AI-driven automation. 

In comparison, while some participants in the 2023 contest did use text-to-music generative models, their use was distinct from the fully automated approach, and still considered co-creative by the contest judges. For example, 2023’s Team 10 incorporated AudioLDM into their process to “generate background and atmosphere noises.” However, they deliberately curated, selected, and shaped the generated sounds, using them as elements within a much broader creative process. 2023’s Team 16 also utilized a text-to-music AI model to generate music segments corresponding to stanzas from the poem “Visit to the observatory” by Harry Martinson, but also included an AIgenerated voice and an improvisational song from one of the team members. The distinction between these uses of text-to-music models and those that were disqualified from 2024 suggests there is an evolving discourse on AI’s role in music-making, where tools that rely on iterative humanAI interaction are seen as more legitimate creative aids, while those that automate the process entirely undermine artistic authorship. This shows that the boundaries of AIassisted creativity are being continuously negotiated as the technology evolves, particularly in contexts where ownership, authorship, and human intervention remain central to creative legitimacy. 

Developers should focus on creating AI tools that allow for iterative co-creation, enabling musicians to provide realtime feedback and refine AI outputs [41, 42]. Instead of generating entire songs in a single pass, AI models for music creation could function more as collaborators, responding to user input and adapting to changes in style, emotion, and structure [43]. This may also contribute to human creators’ increased sense of agency, control and ownership over the final creation, and promote experimentation or exploration of different creative styles. 

## 5.2 Enhanced Transparency and Explainability 

To build trust and usability, AI tools should include explainability features that allow users to see the reasoning behind AI-generated suggestions [44]. Visual interfaces that display chord progressions, harmonic relationships, or AI decision pathways could help musicians better understand and manipulate AI-generated content. Instead of “democratizing” AI by having the AI system generate content beyond the user’s creative skill level, this could allow for the user to build domain knowledge of music and music creation [45]. As a result, they can engage more fully in a deeper collaboration with the system, rather than simply using it to fill in the gaps in a passive manner. 

## 5.3 Style Customization and Genre Flexibility 

To overcome stylistic biases, developers should expand AI training datasets to include a more diverse range of musical traditions, styles, and compositional techniques. This could help realize the goal of AI to bring fresh perspectives and promote innovation in music creation. Users should also have the ability to train AI models on their own sound libraries, allowing for greater personalization and genre flexibility. While custom built or adapted open systems do have this ability, giving users of these ready-made larger scale systems like Stable Audio or Google Magenta the ability to customize their model–even in small ways–could help make them feel more involved and connected with the creation process and output, rather than forcing them into a limited set of musical styles. 

## 5.4 Integration with Existing Creative Workflows 

The comparison highlights the shifting role that AI can play within the creative process, acting as either an assistive tool or as a automation of the creative process. In this case, we suggest that an important aspect of supporting the first case, allowing AI to function as a co-creator rather than something taking over the process, is to ensure that AI tools are adaptable enough to work within already established music creation workflows. 

A recurring aspect of the AISC dataset is the use of multiple tools for music creation, suggesting that it is important for designers of AI-based tools to ensure that they are 

32 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

not disrupting already established workflows of individual creators, as well as patterns of creation well utilized by communities. For example, AI tools that work within other software such as digital audio workstations (DAWs), MIDI controllers, and music notation software may be more easily integrated into existing workflows. For example, the ability to export portions of loops or stems from an AI tool are more useful for the production of music than fully generated pieces. Providing plugin-based solutions and flexible API integrations would make AI assistance more accessible to musicians at all skill levels. 

## 6. CONCLUSION AND FUTURE WORK 

Overall, the expansion of the HAISP dataset to include 2024 data allows for a more nuanced understanding of the evolving relationship between musicians and the use of AI for music creation. Comparative analysis between 2023 and 2024 submissions showed a shift in AI Song Contest submissions from primarily academia towards creative industry, highlighting increasing interest in the exploration and adoption of AI technologies in professional music production. 

Submissions showed use of a broad spectrum of AI tools, reflecting varying levels of adoption of AI in the creation process. Participants showed a preference for iterative feedback and customization, using AI tools to supplement areas they felt less experienced in to support their songwriting process while still maintaining creative control over the final composition. In general, participants’ use of AI is highly dependent on their creative philosophy and existing technical expertise, and for some, their ethical stances. 

For future development of AI music creation tools, designers should prioritize adaptive, transparent, and userdriven functionality to better align with a diverse range of needs. Future AI tools should focus on increasing personalization and flexibility, allowing musicians to integrate AI-generated outputs seamlessly into their existing workflows, and maintain transparency around ethical and responsible data sourcing for outputs. To support this process, further research could explore the long-term impact of AI on music composition across diverse musical genres and cultural contexts. Additionally, the development of open-source and customizable AI tools could provide musicians with more agency over their creative processes. By continuing to examine how AI shapes the artistic landscape, we can foster innovation that respects artistic integrity while leveraging the strengths of human-AI collaboration in music creation. 

As for the future of this project, we plan to publish a journal article that includes a comparative analysis of the data from both years to further explore emerging trends in AI-supported music creation, as well as analyzing the songs submitted to the contest. In light of the shift in industry participation and the evolving quality of submissions to the AI Song Contest, we also aim to develop more concrete guidelines for future entries that encourage creative methods and unique uses of AI. This will ensure greater 

consistency in the expansion of the data set and enhance the overall robustness of the HAISP dataset. 

## 7. ACKNOWLEDGMENTS 

We thank [redacted for blind review] for their contribution in organizing this event. 

## 8. REFERENCES 

- [1] P. Formosa, S. Bankins, R. Matulionyte, and O. Ghasemi, “Can chatgpt be an author? generative ai creative writing assistance and perceptions of authorship, creatorship, responsibility, and disclosure,” AI & SOCIETY, pp. 1–13, 2024. 

- [2] U. Messer, “Co-creating art with generative artificial intelligence: Implications for artworks and artists,” Computers in human behavior: artificial humans, vol. 2, no. 1, p. 100056, 2024. 

- [3] J. He, S. Houde, and J. D. Weisz, “Which contributions deserve credit? perceptions of attribution in human-ai co-creation,” arXiv preprint arXiv:2502.18357, 2025. 

- [4] P.-H. Chen and P.-L. P. Rau, “Using artificial intelligence in music creation? a survey based on copyright consciousness,” in International Conference on Human-Computer Interaction. Springer, 2024, pp. 210–225. 

- [5] S. Li, “The impact of ai-driven music production software on the economics of the music industry,” Information Development, p. 02666669241312170, 2025. 

- [6] N. Caporusso et al., “Generative artificial intelligence and the emergence of creative displacement anxiety,” Research in Psychology and Behavior, vol. 3, no. 1, 2023. 

- [7] K. Erickson, “Ai and work in the creative industries: digital continuity or discontinuity?” Creative Industries Journal, pp. 1–21, 2024. 

- [8] A. Cross, “Tool, collaborator, or participant: Ai and artistic agency,” British Journal of Aesthetics, p. ayae055, 2024. 

- [9] C. Anscomb, “Ai: artistic collaborator?” AI & SOCIETY, pp. 1–11, 2024. 

- [10] L. J. Morris, R. Leger, M. Newman, J. A. Burgoyne, R. Groves, N. Mangal, and J. H. Lee, “HAISP: A Dataset of Human-AI Songwriting Processes From the AI Song Contest,” Nov. 2024, publisher: ISMIR. [Online]. Available: https://zenodo.org/doi/10.5281/ zenodo.14877357 

- [11] C.-Z. A. Huang, H. V. Koops, E. Newton-Rex, M. Dinculescu, and C. J. Cai, “Ai song contest: Human-ai co-creation in songwriting,” arXiv preprint arXiv:2010.05388, 2020. 

33 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

- [12] R. J. Gluck, “The columbia—princeton electronic music center: Educating international composers,” Computer Music Journal, vol. 31, no. 2, pp. 20–38, 2007. 

- [13] R. T. Dean and A. McLean, The Oxford Handbook of Algorithmic Music. Oxford University Press, 2018. 

- [14] E. Lemmon, “The impact of institutional support on artistic research and creation: The columbia-princeton electronic music center and the rca mark-ii,” in International Computer Music Conference Proceedings, 2019. 

- [15] E. R. Miranda, “At the crossroads of evolutionary computation and music: Self-programming synthesizers, swarm orchestras and the origins of melody,” Evolutionary Computation, vol. 12, no. 2, pp. 137–158, 2004. 

- [16] R. L. De Mantaras and J. L. Arcos, “Ai and music: From composition to expressive performance,” AI magazine, vol. 23, no. 3, pp. 43–43, 2002. 

- [17] T. Sexton, “Musenet,” Music Reference Services Quarterly, vol. 26, no. 3-4, pp. 151–153, 2023. 

- [18] A. Roberts, J. Engel, Y. Mann, J. Gillick, C. Kayacik, S. Nørly, M. Dinculescu, C. Radebaugh, C. Hawthorne, and D. Eck, “Magenta studio: Augmenting creativity with deep learning in ableton live,” in Proceedings of the international workshop on musical metacreation (mume), 2019, p. 11. 

- [19] R. Mitra and I. Zualkernan, “Music generation using deep learning and generative ai: A systematic review,” IEEE Access, 2025. 

- [20] “MuseNet,” Sep. 2022. [Online]. Available: https: //openai.com/index/musenet/ 

- [21] R. Louie, A. Coenen, C. Z. Huang, M. Terry, and C. J. Cai, “Novice-ai music co-creation via ai-steering tools for deep generative models,” in Proceedings of the 2020 CHI conference on human factors in computing systems, 2020, pp. 1–13. 

- [22] A. Mehta, S. Chauhan, and M. Choudhury, “Missing melodies: Ai music generation and its" nearly" complete omission of the global south,” arXiv preprint arXiv:2412.04100, 2024. 

- [23] M. Bourreau, F. Moreau, and P. Wikström, “Does digitization lead to the homogenization of cultural content?” Economic Inquiry, vol. 60, no. 1, pp. 427–453, 2022. 

- [24] H. Wang, J. Zou, M. Mozer, A. Goyal, A. Lamb, L. Zhang, W. J. Su, Z. Deng, M. Q. Xie, H. Brown et al., “Can ai be as creative as humans?” arXiv preprint arXiv:2401.01623, 2024. 

- [25] D. Cropley, “Is artificial intelligence more creative than humans?: Chatgpt and the divergent association task,” Learning Letters, vol. 2, pp. 13–13, 2023. 

- [26] M. A. Boden, “Creativity and artificial intelligence,” Artificial intelligence, vol. 103, no. 1-2, pp. 347–356, 1998. 

- [27] R. Wingström, J. Hautala, and R. Lundman, “Redefining creativity in the era of ai? perspectives of computer scientists and new media artists,” Creativity Research Journal, vol. 36, no. 2, pp. 177–193, 2024. 

- [28] R. Latikka, J. Bergdahl, N. Savela, and A. Oksanen, “Ai as an artist? a two-wave survey study on attitudes toward using artificial intelligence in art,” Poetics, vol. 101, p. 101839, 2023. 

- [29] M. A. Runco, “Ai can only produce artificial creativity,” Journal of Creativity, vol. 33, no. 3, p. 100063, 2023. 

- [30] ——, “Updating the standard definition of creativity to account for the artificial creativity of ai,” Creativity Research Journal, vol. 37, no. 1, pp. 1–5, 2025. 

- [31] R. K. Sawyer and D. Henriksen, Explaining creativity: The science of human innovation. Oxford university press, 2024. 

- [32] S. Canyakan, “The role of ai in creative processes: ethical and legal perspectives in the music industry,” Journal of Music Theory and Transcultural Music Studies, pp. 143–158, 2024. 

- [33] F. Morreale, “Where does the buck stop? ethical and political issues with ai in music creation,” Transactions of the International Society for Music Information Retrieval, vol. 4, no. 1, 2021. 

- [34] H.-K. Lee, “Rethinking creativity: creative industries, ai and everyday creativity,” Media, Culture & Society, vol. 44, no. 3, pp. 601–612, 2022. 

- [35] H. H. Jiang, L. Brown, J. Cheng, M. Khan, A. Gupta, D. Workman, A. Hanna, J. Flowers, and T. Gebru, “Ai art and its impact on artists,” in Proceedings of the 2023 AAAI/ACM Conference on AI, Ethics, and Society, 2023, pp. 363–374. 

- [36] “Deed - Attribution-NonCommercial 4.0 International - Creative Commons.” [Online]. Available: https: //creativecommons.org/licenses/by-nc/4.0/deed.en 

- [37] C. E. Hill, S. Knox, B. J. Thompson, E. N. Williams, S. A. Hess, and N. Ladany, “Consensual qualitative research: An update,” Journal of Counseling Psychology, vol. 52, no. 2, pp. 196–205, 2005. 

- [38] A. Song, “Ai song contest,” 2024. [Online]. Available: https://www.aisongcontest.com/join 

- [39] “Free Text to Speech & AI Voice Generator,” Mar. 2025. [Online]. Available: https://elevenlabs.io 

- [40] Shutterstock, “Why ElevenLabs Leveraged Shutterstock’s Rich Data to Build Its Groundbreaking 

34 

Proceedings of the 26th ISMIR Conference, Daejeon, Korea, September 21-25, 2025 

AI Sound Effect Generator,” Nov. 2024. [Online]. Available: https://www.shutterstock.com/blog/ elevenlabs-shutterstock-ai-sound-effects-generator 

- [41] Y. Han, Z. Qiu, J. Cheng, and R. Lc, “When teams embrace ai: human collaboration strategies in generative prompting in a creative design task,” in Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems, 2024, pp. 1–14. 

- [42] Y. Fu, M. Newman, L. Going, Q. Feng, and J. H. Lee, “Exploring the collaborative co-creation process with ai: A case study in novice music production,” arXiv preprint arXiv:2501.15276, 2025. 

- [43] X. Hao, E. Demir, and D. Eyers, “Exploring collaborative decision-making: A quasi-experimental study of human and generative ai interaction,” Technology in Society, vol. 78, p. 102662, 2024. 

- [44] N. Bryan-Kinns, B. Zhang, S. Zhao, and B. Banar, “Exploring variational auto-encoder architectures, configurations, and datasets for generative music explainable ai,” Machine Intelligence Research, vol. 21, no. 1, pp. 29–45, 2024. 

- [45] J. Brusila, M. Cloonan, and K. Ramstedt, “Music, digitalization, and democracy,” Popular music and society, vol. 45, no. 1, pp. 1–12, 2022. 

35 

