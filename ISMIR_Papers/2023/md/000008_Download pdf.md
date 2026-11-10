---
paper_id: "000008"
year: 2023
title: "Download pdf"
source_url: "https://zenodo.org/record/10265227/files/000008.pdf"
---

# HUMAN-AI MUSIC CREATION: UNDERSTANDING THE PERCEPTIONS AND EXPERIENCES OF MUSIC CREATORS FOR ETHICAL AND PRODUCTIVE COLLABORATION 

Michele Newman Lidia Morris Jin Ha Lee University of Washington University of Washington University of Washington `mmn13@uw.edu ljmorris@uw.edu jinhalee@uw.edu` 

## ABSTRACT 

Recently, there has been a surge in Artificial Intelligence (AI) tools that allow creators to develop melodies, harmonies, lyrics, and mixes with the touch of a button. The reception of and discussion on the use of these tools - and more broadly, any AI-based art creation tools - tend to be polarizing, with opinions ranging from enthusiasm about their potential to fear about how these tools will impact the livelihood and creativity of human creators. However, a more desirable future path is most likely somewhere in between these two polar opposites where productive and ethical human-AI collaboration could happen through the use of these tools. To explore this possibility, we first need to improve our understanding of how music creators perceive and utilize these types of tools in their creative process. We conducted case studies of a range of music creators to better understand their perception and usage of AI-based music creation tools. Through a thematic analysis of these cases, we identify the opportunities and challenges related to the use of AI for music creation from the perspective of the musicians and discuss the design implications for AI music tools. 

## 1. INTRODUCTION 

In the past few years, there has been an increase in the creation of AI tools that support various musical activities. These activities are varied, including music recommendation/organization [1], sound synthesis [2], composition [3–5], and mixing [6, 7]. Current discourse on the use of AI-based tools in music production often presents two polarized perspectives: one that sees AI as an opportunity for innovation and progress [8, 9], while the other views it as a threat to the artistic creativity and livelihood of human creators [10–12]. However, a more nuanced and desirable approach entails a productive and ethical collaboration between humans and AI in the creative process, allowing both human creators and AI tools to create something neither could easily do alone. 

© M. Newman, L. Morris, and J.H. Lee. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: M. Newman, L. Morris, and J.H. Lee, “Human-AI Music Creation: Understanding the Perceptions and Experiences of Music Creators for Ethical and Productive Collaboration”, in Proc. of the 24th Int. Society for Music Information Retrieval Conf., Milan, Italy, 2023. 

Discussion around the perception of AI and music creativity tends to be focused on evaluation of the product of the AI [13–15], legal issues [14, 16], or human-computer interaction [17], and not on the implications and connections these factors have on the creative thinking of musicians, though there is growing interest in this domain [18, 19]. Additionally, while there has been discussion within the MIR community around the ethical implications of AI in music creation [18, 20], the experience of using AI to perform songwriting tasks [17], and the perspectives of expert users in creative music information retrieval [21, 22], there is still a need to further understand how creative MIR tasks are impacted by AI tools based on creative context. Even within the ISMIR community, in the last decade, there were fewer than 20 publications that discussed AI music creation tools, and less than half of them considered the creator’s perspective before developing the tool. 

Musicians engage in creativity in many different ways through generating products such as compositions, analyses, and performances [23]. Our paper aims to address the impact of AI tools on the perception and work of one such domain: composition. Within composition we explore the impact of AI on what Peter R. Webster [23, p. 22] describes as "Creative Thinking," or "the mental processes associated with creative production." We will refer to those who engage in this act of creative thinking in composition as creators, their environment/creation goals as creative context, and the act of creative thinking as the creative process. This paper addresses three research questions: (1) In what way do creators perceive and envision the use of AI tools during their compositional process?, (2) How does their creative context influence their use of AI? and (3) What design implications can we derive to inform the creation of AI tools for music creators? 

Our paper extends knowledge about how AI impacts the creative process of musical creators and adds to the discussion of expert users of creative MIR and human-AI collaboration in music creation acts. [19,21,22,24,25] To address these questions we conducted six case studies across a selection of creative contexts and our results are collected in a model that emphasizes the fluidity of roles that AI can play across creative thinking in composition and represents the start of future work aimed at building a dynamic model of human-ai musical creativity. 

80 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

## 2. RELATED WORK 

The idea of using computational means in composition is not a recent development. Over the course of music history, creators have considered various ways to develop algorithmic procedures to help with their process [26]. Since the early days of the computer, programmers and music creatives alike have utilized their skills to create programs that allowed them to continuing this tradition; creating computer-aided compositions (CAC) and computer-aided algorithmic compositions (CAAC). As a whole, CAC tools require user intervention - correction to misnoted parts, adjustment of autotuned voices, and creators choosing which electronic instruments to employ and when [27]. CAAC tools, unlike CAC tools, are intended to be used to help "make music with minimal human intervention" [28]. Popular examples of CAAC tools include programs such as Opusmodus [29] - a library for real-time computer-aided composition in Max [30] - and more. These tools are extremely distinct in their purpose and use, helping to algorithmically aid creators, with rhythmic trees, polymetric notation, and data visualizations of algorithmicallygenerated material. When defining algorithmic composition, Pearce et al. [31] state: 

Many who write programs for music composition are motivated by artistic goals: these programs are used to generate novel musical structures, compositional techniques and even genres of music...The composer may use an existing computer program or she may write a program herself: since identical motivations are involved, we count both of these as algorithmic composition. [31, p. 5] 

In both cases, the question arises: What is creativity and what does it mean for computers to be part of the creative process? This question has been discussed in many ways in multiple fields, as scholars from the humanities [32,33], the sciences [34–36] , HCI [37,38] and MIR [21,22] have speculated for years over how the use of computer systems changes the creation process. 

Through their exploration of using AI to co-songwrite, Micchi et al. [17] list two potential ways in which AI tools could assist creators: through (1) automation and (2) AI as suggestion. They note that while AI as automation is more akin to the tasks given to AI outside of the artistic field, the idea of AI as suggesting solutions to compositional tasks, acting as a partner in the process, is unique to the use of AI within creative pursuits. As Tipei et al. [39] discuss in their paper where student composers utilized DISSCO (Digital Instrument for Sound Synthesis and Composition), compositions were still considered by users to be collaborative, as participants were able to add, modify, or reject contributions made by the software and other users. Researchers compared this interaction to the process of collective improvisation, with the software playing a key role as a collaborator and manager in this compositional process - "[the computer/software]...becomes part of the process not only by performing a vast number of operations very quickly, 

|AI as Collaborator|Democratization|
|---|---|
|Meaning of Creativity|Bias in AI|
|Creative Control|Corporatization of Art|
|Influence|Knowledge of AI|
|Mechanism|Creating Opportunities|
|Old vs. New AI|Sharing of Tools|
|Types of AI Contributions|Current State of AI|



Table 1. Final Codebook for Interviews 

but also as a consequential contributor to the creative effort" [39]. More specifically, this implies that AI simultaneously acts as a collaborator in the process and as a tool, allowing the creator to explore different possibilities of how AI can be applied within their workflow. 

## 3. STUDY DESIGN AND METHODS 

We employed a exploratory, multi-subject case study method [40] to examine how creators perceive the use of AI tools within their compositional process. Using multiple-subject case studies allows us to better explore the phenomenon of AI within the compositional process across a variety of contexts in order to build a stronger basis of understanding and is useful for formulating concepts for theory construction [40,41]. 

Our case selection strategy was focused on representing diverse cases within the varied creative contexts of both western art music and western popular/commercial music traditions [42]. Our cases included a classical/jazz music composer, a film and video game music composer, an interactive media composer, an electroacoustic composer, a sound artist, and a DJ. Due to the scope of the study and resources, we did not include case studies of programmers, listeners, or creators outside the western context, though these communities will be explored in further studies. 

There were a total of six creators, one for each case, all of which were over eighteen years of age and recruited via email. Of the recruited participants, all had heard of AI tools and five worked actively with AI tools within their process. While all creators were actively working within the music field professionally, the film music creator and the intermedia creator were the only ones not affiliated with an academic institution as a student, though both had been trained within western academic music schools. All participants had been composing over five years at the time of the interview. 

For each case, we conducted in-depth, semi-structured interviews between 60 and 90 minuets. Interview questions for this study were generated via a review of the existing literature on the use of AI in music composition and production, where we identified relevant themes and topics (e.g., definitions of AI, AI creativity, typical tools in music creation). Topics ranged from participants’ experiences with AI-based tools in music production, their perceptions of the advantages and disadvantages of using AI, and their views on the ethical implications of AI in music creation. Both descriptions of the case contexts and interview questions can be found at 

81 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

the url: `https://github.com/michelenewman/ ISMIR23_supplemental_material` . 

All interviews were conducted online over Zoom and fully transcribed and edited for clarity. We created the codebook using a mix of the inductive and deductive approach [43]. Initially, two of the authors created the first draft of the codebook using thematic analysis of the transcribed interviews. The codebook was iteratively refined by adjusting and aligning the themes that emerged from the interview data with those from existing literature. Using the final codebook, we first coded the interviews separately on the qualitative coding software ATLAS.ti, then came together to discuss any discrepancy with a goal of reaching an agreement and assigning final codes following the consensus model [44]. 

## 4. RESULTS 

During analysis, 12 categories emerged which were grouped into two main sets: AI as Collaborator and Democratization of Music Creation. The themes were influenced by the current or lack of use of AI by the creators and the reasoning behind their choices. Themes that arose such as tool sharing are common practice among communities of creators, especially on the internet [45, 46], but within the this study, refers specifically the sharing of AI and ML tools. 

Coding the interview transcripts led to the insight that creators had specific creative tasks with which they would or would not feel comfortable utilizing AI tools, as well as parts of the process in which they would consider the use of AI. The most common code within our analysis was "Types of AI Contribution" in which the creators reflected on how they would personally use AI within their own process. This included tasks such as creating repositories (P4) and mastering songs (P6). The least common code was "Sharing of Tools." As a whole, all participants had some knowledge of what AI was, and all but the jazz/classical creator had utilized it in some capacity within their workflow. Three of the creators used also used non-musical AI (such as text-based AI) in their process. 

Based on our analysis, we present the Human-AI Creative Collaboration Model (Figure 1) to represent the use of AI tools throughout the compositional process of music creators situated within the western tradition of composition who may employ computer assisted tools. The model is comprised of three parts: Factors on Influences, AI Roles, and Creation as Process. 



<!-- Start of picture text -->
Factors on Influences to Creative Process Higher Level<br>Influences<br>Idea Generation Control<br>PersonalContext PrototypingAnalysisEditing X Performance PersonalityProcessIntent Creationas<br>Social Mechanisms of Creation Process<br>Context<br>Efficiency<br>Data Housekeeping Tasks<br>Goal Information Retrieval<br>Replicating Sounds Lower Level<br><!-- End of picture text -->

Figure 1. Human-AI Creative Collaboration Model 

## 4.1.1 Personal Context 

The Personal Context is defined by the individual creator’s familiarity with their own creative process and their music literacy. When reflecting on whether or not participants thought that an AI tool would be helpful to them, they considered where it would fall into their process and how much control they would be able to maintain over the final product. Because our participants had been composing for over five years, they already had a strong idea of how their process worked and a familiarity with their personal context of musical creation. Creators commented on their desire to have AI tools that are flexible enough to work within their current creative process, are interoperable with existing compositional software, and have clear and concise interfaces to help with facilitating their adoption and use. 

For example, the film music creator and DJ who work in more commercial settings, with tighter schedules, mentioned utilizing AI tools that were already integrated within software they used such as Ozone [7] and Logic’s Drummer [47]. If integration is not possible, they suggested AI should be designed in a way that it does not interfere with the use of a primary creation tool. The electroacoustic creator, interactive music creator, and sound artist preferred to use older forms of AI due to developer transparency. The participants differentiated older models from the newer models, suggesting that newer models were hidden behind a corporate "black box" in order to work. These creators preferred supervised learning algorithms to unsupervised learning algorithms, so that they could change the open source code and exert more creative control (P5). As they had more experience with AI, they were more open to learning and working with AI tools. All participants also commented that current AI tools were not able to support their process in the ways that they wanted due to the lack of control and low-fidelity outputs. 

## 4.1.2 Social Context 

## 4.1 Factors on Influences 

The far-most left section of our model represents the various contextual factors that impact creators’ perception on where AI should fall within their creative process. These factors are broken into three parts within our model: personal context, social context, and creative goal. While all creation contexts are different, these are the three most common aspects that arose from our analysis. 

Creators also consider Social Context; this includes their current community of practice where they often converse and share their art with (other creators, their audience) and their educational and musical upbringing. Many aspects of the act of creativity are tied to the sociocultural aspects of making music [48]. Those whose communities were most open to using AI tools, often in more experimental creative contexts such as in academic experimental com- 

82 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

munities, were much more willing to engage with the idea of AI in different parts of their process. The jazz/classical composer was adamant that they were very skeptical of AI in part because the community around them was also very skeptical, especially with a strong tradition of composition within the western art context. 

Similarly, they decided on what was an appropriate use of AI by comparing the impact the tool had on others. Participants raised the issue of bias in AI and using the creative works of others. All creators noted that most largescale models rely on Eurocentric training data that may not align with their individual artistic expressions or requirements, feeling that the AI would "flatten" their work with it has "biases and this kind of Eurocentric Westernization of aesthetics" (P5). P4 noted, "There’s been a big problem in the past couple of weeks with people coming out talking about how that’s not right, to be able to use someone’s likeness and their voice however you want." This sentiment highlights the worry that there was oversight in the ways in which these models are being created and distributed, leading to potential harms in taking the intellectual property of others and using it to quickly make financial gains, a sentiment echoed by others in the music industry [15]. Furthermore, participants expressed worry about the impact of such rapidly generated artworks on not only their personal work, but also on the general public’s perception of art as a whole. 

Participants also talked about how AI tools opened up the potential for more types of creators to get involved in the music creation process. Our DJ participant discussed their use of the AI tool Ozone, which he uses to digitally master his songs. While the tool costs 50 USD to purchase, the participant could use it to process all of his songs and have them match the audio specifications needed to upload to streaming services such as Spotify within seconds, whereas if it was sent to a mastering engineer, each song would cost him hundreds of dollars to master. In the same vein, multiple participants mentioned that one of the potential abilities of AI music tools would be the ways it could potentially allow entry-level musicians to bypass some of the extensive music education they would need before being able to create music, including the cost and time investment of said education. "I think it can really accelerate the learning process, the process of studying music and experiencing all this music that we’ve documented...I think it can kind of build each person’s personal vocabulary of what music is." (P1). These participants qualified their statements by clarifying that this would not mean users should bypass the whole process of learning the art of composition. Rather, the ability to create music without networking and funding as a necessity in the creative process is a kind of "freedom" one participant noted, one which begun with the advent of the personal computer and has only continued to expand as the process is simplified (P2). 

## 4.1.3 Creative Goal 

Lastly, Goal refers to creators’ specific reason for composing (i.e. for a film, for a commission, a performance). The 

goal can put pressure on creation time, influence the social practices and expectations, and change the personal workflow of the creator. 

## 4.2 Potential AI Roles: Influences and Mechanisms 

At the center of the model, we present the different ways that AI could potentially be used in the creation process. Participants expressed an overall positive view towards the potential of AI tools as collaborators. Participants also personified the AI in their process stating it was similar to having a "second person" check over their work or a way to bounce off other ideas with the AI tools. While the list is not exhaustive, these represent the most common tasks that creators in our study talked about. These roles were primarily impacted by the concept of "control" of a creative output across the process. All participants agreed that computational creativity cannot supplant human creativity. While participants recognized that AI can "create something" and output a product that mirrors human creativity, such as P4 stating that they were "...sure AI could create something like a poem, for example, that would be really hard for me to tell if it was from a human or from an AI," they highlighted that AI lacks the deliberate decisionmaking of human creators, continuing they would have a hard time "emotionally connect[ing] with it." 

In the former case, participants discussed engaging in a process of "play" with the AI, which allowed them to explore a variety of prompts and generate a collection of potential options that they could later modify or combine to achieve their artistic goals. P5 noted: "So sometimes when I’m stuck, I like to grab some of the models I pretrained and just ask it something." The creators used the tools to explore, both as a way to spark new ideas and as a way to generate a large repository of content to remix in their own way. Within this process though, the creators emphasized the AI does not make the final choice. The final decision was always made by the creator to maintain their artistic agency. 

For all of the participants, within the context of their own compositional process, intention and choice was as important as the creative product. One participant stated, "You can have [AI] generate some sort of electronic music code for you and that sort of just skips for me a whole important step in the process, because in my process of creating live electronic music, there’s sort of an interplay between my coding and my writing. I think a lot will be lost if you just take out an entire part of that process" (P3). Another participant remarked, "For me, creativity also involves the decision-making in a big way. And then to determine where to end things. It doesn’t seem that my experience with AI so far affords these possibilities" (P6). 

Elaborating on this idea of creative control, P6 noted: "I feel that it doesn’t sound like me, or especially with music compositions and working with some of these AI that will give you a MIDI file, you know?", implying some kind of loss in the creator’s personality in automatically generated music pieces. P1 stated that "AI seems to be something that’s designed to do some of that channeling of an idea for 

83 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

you. It seems like AI is kind of trying to be designed to do the human part of the process." Personality Theory related to intellectual property, put forward by thinkers like Emmanual Kant and George Hegel [49], suggests that a person’s personality is incorporated into their creative work during the labor process, and is therefore an essential part of their work. When an AI takes that labor away from the creator, creators felt that the work now no longer has their personality, and thus is no longer their creation. 

## 4.2.1 Influences to Creative Process 

The top section Influences to Creative Process lists tasks that directly influence the final artistic product, allowing for integrity of expression by the creator. On the left side are acceptable influences. These tasks involve aspects that help prompt ideas or create inspiration. Tasks that fall within the acceptable influences do not need to be as integrated with the programs creators already use, though they should integrate with the overall creative process - especially in the ideation phase, where many creators felt AI influences fit best. These tools should allow for continuous reiteration, with understandable in-tool design signifiers that indicate the ways they can edit, change, and manipulate the AI’s data before and after each iteration. Once this ideation phase is over, there should be a clear way to export their ideas into a new software or system, again allowing for the interoperability that is vital for music creator’s process; this could be done in a number of ways such as using MIDI files, WAV files, or MusicXML. 

Participants also discussed ways that AI tools could go beyond what humans are traditionally capable of, and in that way become a partner in the expansion of their compositional capabilities. One potential function as noted by a participant was the ability to use AI as a music analysis tool, helping users pinpoint things they were not aware of or even able to perceive with human hearing, such as "the sound field...expanding from the front to the back" (P6). Another participant described how their current use of AI as part of their process has changed how they see the world around them, gaining a new understanding around what could be used or turned into data which allows them to create patterns and connections within their music (P5). AI tools also helped many creators find relationships between sounds, found materials, words, and pictures. One participant explained it as a "feedback loop" (P6). 

The right side displays aspects of the creative process where creators are not comfortable engaging in Human-AI collaboration. They felt using AI with these tasks negatively affect the creative process by taking away an essential component of their creations. This includes losing the ability to control their intent and choices, not being able to specify performance parameters/low-fidelity outputs, and interfering with their process and creative personality. 

## 4.2.2 Mechanisms of Creation 

The lower section is titled Mechanisms of Creation. It includes types of Human-AI collaborations where our participants had little issue if AI took over the process com- 

pletely, often searching for and utilizing AI that could complete these tasks. In general, mechanisms are tasks that occur within the creative process that do not require direct decision-making by the music creators, including housekeeping tasks such as file naming, information retrieval tasks such as looking for electronic instruments, and replicating sounds. Many participants noted they would use AI to complete tasks to help speed up their process or complete tasks they did not want to do. These tasks often had to do with analyzing data in some way. For example, P3 noted "I have an idea that I want to do, and I just use the AI to make that idea happen faster." 

## 4.3 Creation as Process 

Lastly, on the far right side is a spectrum representing what we call "Creation as Process," emphasizing the role of iteration and thinking that happens during the process of writing music [23, 32]. For all of the participants, within the context of their own creative process, intention and choice was as important as the creative product. One participant stated, "You can have [AI] generate some sort of electronic music code for you and that sort of just skips for me a whole important step in the process, because in my process of creating live electronic music, there’s sort of an interplay between my coding and my writing. I think a lot will be lost if you just take out an entire part of that process" (P3). Another participant remarked, "For me, creativity also involves the decision-making in a big way. And then to determine where to end things. It doesn’t seem that my experience with AI so far affords these possibilities" (P6). 

The spectrum represents the level of intellectual engagement needed in each task, ranging from highly intentional choices to mechanical and repetitive tasks. Within the process of creating, the given AI tasks may move to higher or lower levels along the spectrum, sometimes influencing the process more and other times receding to lower levels of impact. The creative process is fluid, meaning that both the factors and roles of the AI can change over the course of creation. 

## 5. DISCUSSION 

Although our focus on only six case-studies of music creators in specific creative contexts presents a limitation to our study, we believe that our focus allowed us to explore possible applications of AI tools to creators’ needs, and allowed us to form initial insights into the perception of the use of AI tools in the creative process. Musical creativity is not a monolith and it is our belief that in order to understand how to design specific AI systems that support creative musical tasks, we need to know how creative thinking is conceived by those engaging in these types of musical activities. Our main contribution in this paper is to begin to situate certain AI tasks as potential helpful or potentially harmful to the creative process of those who create. 

In this study, we argue that the discussion around the threat that AI poses to both the jobs of creators and artis- 

84 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

tic integrity is of importance to creators; emphasizing that co-creation of music in the context of music composition is dependent not only on the larger creative context, but on the process of creative thinking as well. Our work suggest that Andersen and Knees [21, 127] notion of the importance of an "individual user[s’] models of music perception as well as a solid understanding of usage context" is not only needed for exploring dissimilarity in search, but also for understanding AI systems in the other forms creative endeavors. Knees et al.’s [50] consideration of the use of "strangeness" for artists recommendations is useful in AI systems as so far the AI is helping to generate new ideas for creators; though strangeness is one aspect of many needs that a creative engages with in AI music systems. Other tasks such as analysis and editing are also elements of creative MIR tasks that may be helpful to facilitating the creative process, though often can occur at different points or simultaneously with the task of idea generation. We argue that there is a need to understand how specific creative processes view and interact with AI at all stages. While there are some aspects of the use of AI that many of our cases agreed on, such as allow AI to take over tasks that have little to no control over the final product of creative thinking which is echoed in other literature [50, 51], our study also indicated that the role of AI is also dependent upon personal, social, and creative goal related factors that are constantly in flux. The Human-AI Collaboration Model demonstrates our belief that the role that AI plays on creative thinking is highly flexible within music creation and that without a clear understanding of how creators are thinking, AI systems can hurt musical creative practices of musicians. 

Oliver Bown has warned against the possible negative affect that AI tools can have if it disrupts cultural applications and creation of music. [33]. If music AI systems are designed to limit creator control, intent, or process, they could potentially lead to Schröter’s notion of the "(possible) automatization of artistic work" [52]. Full control over the final artistic product and an understanding of the creator’s emphasis on their process are the most important aspects to developing tools that can support, instead of harm, human creativity - as noted by Knees, it is important that the user is given agency in the process of "co-creation" with high-level control of the generative process [19]. 

While it is true that the concept of "Explainable AI" [53–55] can help to educate those who worry about the role AI plays in future creative endeavors, it is not a full solution to the lack of user trust or changing user hesitancy in tool adoption. Recent fears over data misuse by generative AI, backed up by online discussions and even legal investigations into data scraping [56] and intellectual property [57] have made creators fear utilizing AI tools, with creators fearing that AI is trained on data that does not meet their personal artistic goals or actively hurts other artists. Increasing common knowledge about the functions of AI tools would create more trust in these systems and encourage users to integrate them more into their creative process [58], but there is also a need to design in systems 

in such a way that creators feel they can ethically use these systems in their own work. This means ethically sourcing material and allowing for the control of elements within AI systems. 

Designers of AI tools for creators should consider what role they expect for their tool to play within specific creation processes and make choices that support this. The specific inputs, outputs, and needs of an AI system will change over the creative process. Because AI tasks can move up and down in importance, that means that it is highly possible to have a mismatch of the execution and evaluation of AI systems that may lead to less cohesion between the creator and the AI as they will continually need to reevaluate how these systems fit in their workflow. 

## 6. CONCLUSION AND FUTURE WORK 

Our findings support that creators have concerns surrounding the transparency of and lack control within AI tools, but that there is still much to do in relation to understanding the exact needs of creative users. In order to develop useful AI tools, designers must consider the specific creation context, existing processes of creators, control of creator, and the fluidity of creating. Our Human-AI Creative Collaboration Model is designed to help developers and researchers who create AI systems to consider the variety of factors and influences that exist on creative process and how they might intersect with a creators experience. We hope that this work encourages developers and other MIR researchers to continue to consider advancing Human-AI collaborations that align with music creators’ needs. There are a variety of tasks that AI can perform, and considering if tasks are impacting creative thinking in a different phases of creation will allow for a more ethical and productive experience for music creators. 

While we interviewed different creation contexts within our case studies, there is still a need for future work to consider how differences in cultural background, musical training, and experience with AI factor into Human-AI creative thinking. Composing music can happen in a variety of other contexts not explored in this study, including as part of music education and cultural situations. Yet, composition is only one form of creative thinking within music and future work might will continue work to identify the differences that arise when using AI systems within different forms of creation such as music analysis and performance. Creators may be utilizing all these forms of thinking across the creative process in non-linear ways. There is still much to learn about the impact that AI will have on music as an art; if designed and deployed ethically, AI offers the opportunity to enhance human creation and provide new avenues for creating and learning about music. But, in order for AI to support musicians in any form of creative thinking, we need to ensure we are designing AI tools with creators in mind. 

85 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

## 7. REFERENCES 

- [1] “Cyanite ai-based music tagging system,” https:// cyanite.ai/, accessed: 2023-03-30. 

- [2] “VOCALOID ai engine,” https://www.vocaloid.com/ en/news/news_001/, accessed: 2023-03-30. 

- [3] A. Roberts, J. Engel, Y. Mann, J. Gillick, C. Kayacik, S. Nørly, M. Dinculescu, C. Radebaugh, C. Hawthorne, and D. Eck, “Magenta Studio: Augmenting Creativity with Deep Learning in Ableton Live,” in Proceedings of the 6th International Workshop on Musical Metacreation. Charlotte, United States: MUME, Jun. 2019, p. 7. [Online]. Available: https://doi.org/10.5281/zenodo.4285266 

- [4] “AIVA artificial intelligence composer,” https://www. aiva.ai/, accessed: 2023-03-30. 

- [5] “Sony Flow Composer,” https://www. flow-machines.com/history/projects/ flowcomposer-composing-with-ai/, accessed: 202303-30. 

- [6] “LANDR mastering software,” https://www.landr. com/online-audio-mastering/, accessed: 2023-03-30. 

- [7] “Ozone izotope mastering software,” https://www. izotope.com/en/products/ozone.html, accessed: 202303-30. 

- [8] J. Hong, “Bias in perception of art produced by artificial intelligence,” in International Conference on Human-Computer Interaction: Interaction in Context, 2018. 

- [9] C. Moruzzi, “Should human artists fear ai? : A report on the perception of creative ai,” in xCoAx 2020 : Proceedings of the Eighth Conference on Computation, Communication, Aesthetics & X, M. Verdicchio, M. Carvalhais, L. Ribas, and A. Rangel, Eds. Porto: Universidade do Porto, 2020, pp. 170–185. [Online]. Available: https://2020.xcoax.org/xCoAx2020.pdf 

- [10] M. Mazzone and A. Elgammal, “Art, creativity, and the potential of artificial intelligence,” Arts, vol. 8, no. 1, p. 26, 2019. 

- [11] J. Hong, Q. Peng, and D. Williams, “Are you ready for artificial mozart and skrillex? an experiment testing expectancy violation theory and ai music,” New Media & Society, vol. 23, no. 7, pp. 1920–1935, 2021. 

- [12] H. Zuli´c, “How ai can change/improve/influence music composition, performance and education: Three case studies,” INSAM Journal of Contemporary Music, vol. 1, no. 2, pp. 100–114, 2019. 

- [13] D. Zlatkov, J. Ens, and P. Pasquier, “Searching for human bias against ai-composed music,” in Artificial Intelligence in Music, Sound, Art and Design: 12th International Conference, EvoMUSART 2023, Held 

   - as Part of EvoStar 2023, Brno, Czech Republic, April 12–14, 2023, Proceedings. Berlin, Heidelberg: Springer-Verlag, 2023, p. 308–323. [Online]. Available: https://doi.org/10.1007/978-3-031-29956-8_20 

- [14] F. Tigre, F. Moura, and C. Maw, “Artificial intelligence became beethoven: how do listeners and music professionals perceive artificially composed music?” Journal of Consumer Marketing, vol. 38, no. 2, pp. 137–146, 2021. 

- [15] K. Lee, G. Hitt, E. Terada, and J. Lee, “Ethics of singing voice synthesis: Perceptions of users and developers,” in Proc. of the 23rd Int. Society for Music Information Retrieval Conf., Bengaluru, India, 2022, pp. 733–740. 

- [16] E. Drott, “Copyright, compensation, and commons in the music ai industry,” Creative Industries Journal, vol. 14, no. 2, pp. 190–207, 2021. 

- [17] G. Micchi, L. Bigo, M. Giraud, R. Groultand, and F. Levé, “I keep counting: An experiment in human/ai co-creative songwriting,” Transactions of the International Society for Music Information Retrieval, vol. 4, no. 1, p. 263–275, 2021. 

- [18] M. Rohrmeier, “On creativity, music’s ai completeness, and four challenges for artificial musical creativity,” Transactions of the International Society for Music Information Retrieval, vol. 5, no. 1, p. 50–66, 2022. 

- [19] P. Knees, M. Schedl, and M. Goto, “Intelligent user interfaces for music discovery,” Transactions of the International Society for Music Information Retrieval, vol. 3, no. 1, p. 165–179, 2020. 

- [20] F. Morreale, “Where does the buck stop? ethical and political issues with ai in music creation,” Transactions of the International Society for Music Information Retrieval, vol. 4, no. 1, p. 105–113, 2021. 

- [21] P. K. Kristina Andersen, “Conversations with expert users in music retrieval and research challenges for creative mir,” in 17th International Society for Music Information Retrieval Conference, 2016, pp. 122–128. 

- [22] C.-E. Cella, “Music information retrieval and contemporary classical music: A successful failure.” Transactions of the International Society for Music Information Retrieval, vol. 3, no. 1, pp. 126–136, 2020. 

- [23] P. R. Webster, “Creativity as creative thinking,” Music Educators Journal, vol. 76, no. 9, pp. 22–28, 1990. 

- [24] A.-M. Gioti, “From artificial to extended intelligence in music composition,” Organised Sound, vol. 25, no. 1, p. 25–32, 2020. 

- [25] P. Pasquier, A. Eigenfeldt, O. Bown, and S. Dubnov, “An introduction to musical metacreation,” Comput. Entertain., vol. 14, no. 2, jan 2017. [Online]. Available: https://doi.org/10.1145/2930672 

86 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

- [26] G. Nierhaus, “Historical development of algorithmic procedures,” in Algorithmic Composition: Paradigms of Automated Music Generation. Vienna, Austria: Springer Vienna, 2008, pp. 7–66. 

- [27] D. Bouche, J. Nika, A. Chechile, and J. Bresson, “Computer-aided composition of musical processes,” Journal of New Music Research, vol. 46, no. 1, pp. 3– 14, 2017. 

- [28] A. Alpern, “Techniques for algorithmic composition of music,” Hampshire College, 1995. 

- [29] Janusz Podrazik, “Opusmodus.” [Online]. Available: https://opusmodus.com/ 

- [30] Cycling 74, “Max.” [Online]. Available: https: //cycling74.com/products/max 

- [31] M. Pearce, D. Meredith, and G. Wiggins, “Motivations and methodologies for automation of the compositional process,” Musicae Scientiae, vol. 6, no. 2, pp. 119–147, 2002. [Online]. Available: https://doi.org/10.1177/102986490200600203 

- [32] D. Cope, Computer models of musical creativity. MIT Press, 2005. 

- [33] O. Bown, “Sociocultural and design perspectives on aibased music production: Why do we make music and what changes if ai makes it for us?” in Handbook of Artificial Intelligence for Music, E. R. Miranda, Ed. Cham: Springer, 2021. 

- [34] F. Carnovalini and A. Rodà, “Computational creativity and music generation systems: An introduction to the state of the art,” Frontiers in Artificial Intelligence, vol. 3, no. 14, pp. 111–222, April 2020. 

- [35] C. Lamb, D. G. Brown, and C. L. A. Clarke, “Evaluating computational creativity: An interdisciplinary tutorial,” ACM Computing Surveys, vol. 51, no. 2, feb 2018. 

- [36] F. Nake, “Creativity in algorithmic art,” in Proceedings of the Seventh ACM Conference on Creativity and Cognition, Berkeley, California, USA, 2009, pp. 97–106. 

- [37] M. Lee, P. Liang, and Q. Yang, “Coauthor: Designing a human-ai collaborative writing dataset for exploring language model capabilities,” in Proceedings of the 2022 CHI Conference on Human Factors in Computing Systems, ser. CHI ’22. New York, NY, USA: Association for Computing Machinery, 2022. [Online]. Available: https://doi.org/10.1145/3491102.3502030 

- [38] G. A. Wiggins, “A preliminary framework for description, analysis and comparison of creative systems,” Know.-Based Syst., vol. 19, no. 7, p. 449–458, nov 2006. [Online]. Available: https: //doi.org/10.1016/j.knosys.2006.04.009 

- [39] S. Tipei, A. Craig, and P. Rodriguez, “Using highperformance computers to enable collaborative and interactive composition with dissco.” Multimodal Technologies and Interaction, vol. 5, no. 24, 2006. 

- [40] R. K. Yin, Base Study Research and Applications : Design and Methods. Sage Publications, 2017. 

- [41] B. E. White, S. J. Gandhi, A. Gorod, V. Ireland, and B. Sauser, “On the importance and value of case studies,” in 2013 IEEE International Systems Conference (SysCon), 2013, pp. 114–122. 

- [42] J. Seawright and J. Gerring, “Case selection techniques in case study research: A menu of qualitative and quantitative options,” Political Research Quarterly, vol. 61, no. 2, p. 294–308, 2008. 

- [43] J. Corbin and A. Strauss, Basics of Qualitative Research: Techniques and Procedures for Developing Grounded Theory. Sage Publications, 2014. 

- [44] C. E. Hill, S. Knox, B. Thompson, E. Williams, S. Hess, and N. Ladany, “Consensual qualitative research: An update,” Journal of Counseling Psychology, vol. 52, no. 2, p. 196–205, 2005. 

- [45] J.-P. Fourmentraux, “Internet artworks, artists and computer programmers: Sharing the creative process,” Leonardo, vol. 39, no. 1, p. 44–50, 2021. 

- [46] Y. Kjus, “The use of copyright in digital times: A study of how artists exercise their rights in norway,” Popular Music and Society, vol. 44, no. 3, pp. 241–257, 2021. 

- [47] “Logic Pro virtual drummer,” https://support.apple. com/guide/logicpro/drummer-lgcpa4324884/mac, accessed: 2023-03-30. 

- [48] V. P. Gl˘aveanu, “Creativity as a sociocultural act,” The Journal of Creative Behavior, vol. 49, no. 3, pp. 165–180, 2015. [Online]. Available: https: //onlinelibrary.wiley.com/doi/abs/10.1002/jocb.94 

- [49] J. Hughes, “The philosophy of intellectual property,” Georgetown Law Journal, vol. 77, p. 287, 1988. 

- [50] P. Knees, K. Andersen, and M. Tkalˇciˇc, ““I’d like it to do the opposite”: Music-Making Between Recommendation and Obstruction,” in Proceedings of the 2nd International Workshop on Decision Making and Recommender Systems, vol. 1533. Charlotte, United States: MUME, 2015. [Online]. Available: CEUR-WS.org. 

- [51] D. Buschek, L. Mecke, F. Lehmann, and H. Dang, “Nine potential pitfalls when designing human-ai cocreative systems,” CoRR, vol. abs/2104.00358, 2021. [Online]. Available: https://arxiv.org/abs/2104.00358 

- [52] J. Schröter, “Artificial intelligence and the democratization of art,” in The Democratization of Artificial Intelligence: Net Politics in the Era of Learning Algorithms, A. Sudmann, Ed. Transcript publishing, 2019, pp. 297–311. 

87 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

- [53] C. Zednik, “Solving the black box problem: A normative framework for explainable artificial intelligence,” Philosophy & Technology volume, vol. 34, p. 265–288, 2021. 

- [54] A. Holzinger, “From machine learning to explainable ai,” in 2018 World Symposium on Digital Intelligence for Systems and Machines (DISA), 2018, pp. 55–66. 

- [55] W. Samek, G. Montavon, A. Vedaldi, L. K. Hansen, and K.-R. Müller, Explainable AI: Interpreting, explaining and Visualizing Deep Learning. Springer, 2019. 

- [56] C. Fiesler, N. Beard, and B. C. Keegan, “No robots, spiders, or scrapers: Legal and ethical regulation of data collection methods in social media terms of service,” Proceedings of the International AAAI Conference on Web and Social Media, vol. 14, p. 187–196, 2020. 

- [57] T. Zipper, “Mind Over Matter: Addressing Challenges of Computer-Generated Works Under Copyright Law,” Wake Forest Journal of Business and Intellectual Property Law, aug 7 2022, https://jbipl.pubpub.org/pub/zn744tze. 

- [58] E. Ruane, A. Birhane, and A. Ventresque, “Conversational ai: Social and ethical considerations,” in Irish Conference on Artificial Intelligence and Cognitive Science, 2019. 

88 

