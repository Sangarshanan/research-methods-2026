---
paper_id: "000058"
year: 2024
title: "Download pdf"
source_url: "https://zenodo.org/record/14877391/files/000058.pdf"
---

# PURPOSEFUL PLAY: EVALUATION AND CO-DESIGN OF CASUAL MUSIC CREATION APPLICATIONS WITH CHILDREN Michele Newman<sup>1</sup> Lidia Morris<sup>1</sup> Jun Kato<sup>2</sup> Masataka Goto<sup>2</sup> Jason Yip<sup>1</sup> Jin Ha Lee<sup>1</sup> 1 Information School, University of Washington, United States 2 National Institute of Advanced Industrial Science and Technology (AIST), Japan 

|`mmn13@uw.edu,` `ljmorris@uw.edu,` `jun.kato@aist.go.jp,`|
|---|
|`m.goto@aist.go.jp,` `jcyip@uw.edu,` `jinhalee@uw.edu`|



|ABSTRACT|
|---|



The rise of digital technologies has increased interest in democratizing music creation, but current creativity support tools often prioritize literacy and education over meeting children’s needs for casual creation. To address this, we conducted Participatory Design sessions with children aged 6-13 to explore their perceptions of casual music creation activities and identify elements of creative applications that support different expressions. Our study aimed to answer two key questions: (1) How do children perceive casual music creation activities and which elements of creative applications facilitate expression? and (2) What insights can inform the design of future casual music creation tools? Our findings indicate that children view casual music creation as involving diverse activities, with visuals aiding in understanding sounds, and engaging in various playful interactions leading to creative experiences. We present design implications based on our findings and introduce casual creation as "purposeful play". Furthermore, we discuss its implications for creative MIR. 

## 1. INTRODUCTION 

Digital technologies have sparked interest in democratizing creation as they enable diverse individuals to produce cultural objects [1–3], suggesting we may understand these tools as enhancers of human creativity [4–7]. For example, over the past two decades, there has been a rise in the development and study of Creativity Support Tools (CSTs) in the field of Human-Computer Interaction (HCI) [8]. Despite the abundance of music-related CSTs, including tools such as digital audio workstations [9–11], notation software [12, 13], style-specific composition/identification tools [14,15], and music generation systems [16,17], many fail to cater to children. 

© M. Newman, L. Morris, J. Kato, M. Goto, J. Yip, and J.H. Lee. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: M. Newman, L. Morris, J. Kato, M. Goto, J. Yip, and J.H. Lee, “Purposeful Play: Evaluation and Co-Design of Casual Music Creation Applications with Children”, in Proc. of the 25th Int. Society for Music Information Retrieval Conf., San Francisco, United States, 2024. 

|Children’s creative experiences are often shaped by a<br>limited understanding of social norms [18], implying that<br>systems designed for adults may not fully support their|
|---|
|creative endeavors. Moreover, many music applications|
|designed for youth primarily focus on literacy or are de-<br>ployed in formal education contexts [19, 20]. However,<br>previous work highlights the value of informal and ca-|
|sual music experiences in education [21, 22]. Building on<br>this work, we explore the potential of casual music experi-<br>ences for children, focusing on casual music creation. We|
|define casual music creation as creative musical experi-<br>ences prioritizing the process of enjoyment over product<br>outcome, drawing inspiration from Compton’s research on<br>casual creation systems [23,24]. While casual musical ex-|
|periences relate to informal learning [22], this study fo-|
|cuses on how music technology as part of CSTs supports|
|these experiences, providing new ways for children’s self-|
|expression rather than skill development. Research shows|
|that supporting creativity is vital for children, as it helps|
|to foster children’s identities [25, 26], develop confidence|
|in their creative abilities [27, 28], as well as support brain|
|development [29,30] and social skills [31].|



However, there is a gap in understanding children’s MIR needs. This is particularly true in creative MIR, or the use of retrieved music information for creative purposes [7, 32], despite growing interest in creative applications [7,33]. For instance, only two ISMIR papers address children: one develops the Children’s Song Dataset for song synthesis [34], and the other involves children in designing a music organization app [35]. While these studies provide insights to children’s experiences with MIR tasks, there is still a broader question about how children interact with MIR tasks to meet their unique creative needs. Building off this prior research in MIR, music education, and HCI, we utilized a method of Participatory Design (PD) called Cooperative Inquiry, a type of PD that focuses on designing technology with and for children [36]. As children are a growing user group of creative technologies, PD can generate developmentally appropriate design ideas and feedback [37, 38], boosting children’s self-esteem through facilitating design in a casual setting [39]. We examine children’s creative needs while using musical CSTs within creative MIR contexts through two PD sessions with children aged 6-13, addressing two questions: (1) How do chil- 

529 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

|dren perceive casual music creation activities and which el-|Pseudonym|Age|Gender|Ethnicity|Sessions|
|---|---|---|---|---|---|
|ements of creative applications facilitate expression? and<br>|Annie|6|Female|Latino|DS2|
|(2) What insights can inform the design of future casual|Emma|9|Female|Black / White|DS1, DS2|
|music creation tools? This paper contributes to the de-|Han<br>|10<br>|Male<br>|Latino<br>|DS2<br>|
|mocratization of music creation by addressing children’s|Jayden<br>|9<br>|Male<br>|Asian / Black<br>|DS2<br>|
|uniuecreativeneedsincasualmusicalicationdesin|Keon|9|Male|Asian / Black|DS1, DS2|
|q      pp g.<br>|Liam|9|Male|Asian / White|DS1|
|Furthermore, we present a set of design principles to sup-<br>|Jin|13|Female|Asian / White|DS1, DS2|
|port more playful interactions with music and discuss their|Taylor|10|Female|Asian / White|DS1, DS2|
|implications for future work in creative MIR.|Seiko<br>|10<br>|Female<br>|Asian<br>|DS1<br>|
||Zachary|8|Male|Asian / White|DS1, DS2|



## 2. RELATED WORK 

Table 1. Demographics of Child Participants 

## 2.1 Children’s Musical Creativity 

Creativity is the ability to generate original and valuable ideas [4]. In the realm of music, this translates to realizing such ideas through composition, analysis, or performance [40]. Scholars argue that musical creativity is embodied, meaning environmental factors play a role in shaping creative cognition in music [40–43]. Furthermore, music educator Peter Webster has suggested that musical creativity is more akin to creative processes, or what he terms as moving from a musical idea to a product [44]. 

For children, there has been a particular focus on understanding their creativity in reference to composition [45–47] in music education contexts. Yet, musical experiences begin early in childhood and are increasingly impacted by popular music experiences with new forms of technology [48–51]. Therefore, children experience music via playful interactions in a variety of modalities [52]. Notably, social-emotional environments, especially those shaped by parents and teachers, can serve as catalysts for children’s musical creativity through play [53–55], suggesting that children’s musical experiences are impacted by their development, environment, and interactions with technology. While play and technology are crucial in music education and cognitive development, questions remain about how CSTs can enhance casual music experiences and whether these interactions impact children’s creativity. 

## 2.2 Creativity Support Tools 

Creativity Support Tools (CSTs) are digital resources designed to enhance creativity [8]. Interactive musical systems (IMSs) have shown promise in supporting nonmusicians’ engagement in music making [56], but domain expertise can influence creativity [40, 57]. Hence, specialized tools have been developed to meet novices’ needs, often incorporating critique [58], such as those for novice filmmakers [59] or digital painting systems [60]. Recognizing the importance of personally meaningful creative activities, referred to as "mini-c" creativity, there is a growing emphasis on integrating this perspective into CST evaluation methods [61, 62]. This acknowledgment underscores the significance of understanding children’s creative experiences with musical CSTs and adapting design and evaluation approaches accordingly [63]. While technology’s impact on children’s creativity has been explored in areas like storytelling and video creation [64, 65], its effects on musical creativity remain relatively unexplored 

[50, 58, 66]. Though tools aiding children in music composition exist, they are often designed for general novices [63], even though previous work has suggested specific design recommendations for other musical acts by children, such as composition at home [45]. Previous research recognizes children’s unique creative needs and the potential of CSTs to foster creativity and learning. However, there is still uncertainty about the differences between children’s structured and casual creation with CSTs, and how these differences relate to creative MIR. 

## 3. METHODS 

## 3.1 Participatory Design 

For this study, we utilized Cooperative Inquiry (CI) [36, 67], a Participatory Design (PD) method facilitating collaboration between designers and users, thus democratizing the design process. CI specifically emphasizes allowing children and adults to design as equals. This method offers insights into children’s learning [67], empowering them to articulate thoughts on complex issues such as family finances [68], gender [69], and creativity [70, 71]. 

## 3.2 Participants 

The KidsTeam UW co-design group comprises adult design researchers (investigators, master’s students, and undergraduate students) and 10 child participants, using pseudonyms for confidentiality (see Table 1). Children were recruited through mailing lists and snowball sampling with parental consent and child assent obtained. The research received approval from the university’s Institutional Review Board. Two 90-minute design sessions were held in January and February 2024, with five to eight adult facilitators serving as design partners in each session. 

## 3.3 Design Sessions 

Our design sessions started with a 15-minute Snack Time for socializing, followed by a 15-minute Circle Time featuring a "Question of the Day" to warm up for the design activity. Then, participants engaged in small group design activities for 45 minutes in Design Time, followed by a 15-minute Full Group Discussion for presentations and reflection. 

530 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 <mark>Child App Name Description Annie Color Block Users compose by dragging and dropping colored blocks. Users can download the music to share. Emma Cat Choir An app where users may drag different clothing representing different sounds onto cats to compose songs.</mark> Han Mixtape Users create and share "mixtapes" by pulling music from streaming services and creating playlists. Also allows for composing with provided sounds and AI. <mark>Jayden Untitled Users organize their music and can search, f</mark> i <mark>lter, and create albums. They can also remix other songs. Keon Untitled An app to store music f</mark> i <mark>les, allowing users to drag and drop music f</mark> i <mark>les from other apps.</mark> Jin Dreamer A music composition app that acts as a game where users are able to manipulate different environments to create music for a story. Taylor Sing-a-Song Users can create songs by dragging instruments onto tracks and export them with a video or animated characters. Others can remix these songs. <mark>Zachary Piano God An app meant to help pianist practice songs using animations to tell users which keys to play.</mark> Table 2. Descriptions of Applications designed by children in DS2 

with a camera and took notes on a legal pad. Children’s thoughts were summarized during group discussions and collected on a Google Slides deck. 

## 3.3.1 Design Session 1: Playing with Casual Music CSTs 

Design Session 1 (DS1) took place in January 2024. We asked the children to play with four different casual music tools to elicit their feedback on different types of casual music applications. The first is TextAlive [72, 73], a website that automatically synchronizes lyrics text with music, detects timing information of beats and other musical elements, and allows users to interactively create “lyric videos” – music videos in which lyrics animate in sync with the music. The second tool, TextAlive Flow [74] (available on tablet and desktop), is an extension of TextAlive that has a more casual user interface. It allows users to touch the screen to change the video’s visuals (typography, colors, motion patterns, etc.) while listening to the music. Incredibox [75] lets users create songs by dragging and dropping outfits onto animated characters, combining pre-recorded beatbox sounds and melodies. Lastly, Sketcha-Song [76] is a tablet application that lets users tap and drag to add different pitches and sounds. These tools were selected to allow children to engage with various modes of interacting and making with music. During the session, we captured what the children liked, disliked, and design ideas for each app on a sticky note, organizing them into thematic groups on a whiteboard [36]. 

We utilized an inductive qualitative approach for data analysis [78]. The initial codebook was developed by the first author through inductively coding recorded session videos. Codes like “Musical Activities – Remixing” and “Control – Variety of Options” were included in the first iteration. Subsequently, two authors conducted consensus coding [79] on design artifacts, researcher memos, and session videos, adjusting the codebook as needed. In cases of disagreement, a third team member resolved discrepancies. This process led to the final version of the codebook. For example, we applied the code “App Elements – Control” to the quote “when you could see or hear a difference, it makes you feel like you’re in more control.” Further descriptions of design artifacts and applications of our codes can be found in our supplemental material.<sup>1</sup> 

## 4. FINDINGS 

## 4.1 Children’s Perceptions of Casual Music Creation 

Consistent with previous work [48,52], children saw music making as a holistic, process-focused experience [44], and expected to engage in multiple musical activities within a single app. Composing was the most referenced activity, as all DS2 apps except Keon’s, which stored music files, involved music composition. Listening to music was also prominent (Han, Jayden, Jin, & Taylor, DS2). Remixing, proposed only in Taylor’s and Jayden’s apps, was the least suggested activity. 

## 3.3.2 Design Session 2: Designing Casual Music CSTs 

Design Session 2 (DS2) took place in Februrary 2024. We asked the children to “design a casual music creation app.” We asked them to define what their app allowed them to do with music, and develop a user flow including how they moved between the homepage, creation interface, and to sharing their creations with others. We derived these design aspects from the themes that arose during DS1. Before breaking into our design groups, we shared an example of what a user flow looked like using TextAlive Flow. We supplied the children with a large bag with different craft materials and paper, asking them to engage in lowfidelity prototyping of their application [77]. 

Children’s views on the applications were shaped by their past experiences with music and technology, indicating their preferences often reflect experiences with other applications such as music streaming apps [48], as well as their cultural backgrounds and existing knowledge [80]. For example, many applications from DS2, shown in Table 2, also included references to other applications. Emma and Taylor’s applications referenced Incredibox and Sketch-a-Song respectively, imitating the drag and drop features for layering musical sounds. The interface of Zachary’s application was similar to the application Syn- 

## 3.4 Data Collection and Analysis 

drop features for layering musical sounds. The interface of Our hybrid design sessions utilized Zoom for video and Zachary’s application was similar to the application Synscreen recordings across three computers for each design group. We recorded a total of 6 hours and 10 minutes 1 Our supplemental material can be found at: `https://doi.org/` of video. Researchers also documented creative artifacts `10.17605/OSF.IO/5DNS6` . 531 

|Proceedings of the 25th ISMIR Conference,San Francisco,USA and Online,Nov 10-14,2024|
|---|



|thesia, with falling blocks that demonstrated which keys to<br>play on a piano keyboard. Additionally, there were various<br>ways suggested to supplement listening methods that were<br>similar to other applications such as organizing playlists|
|---|
|(Han & Jayden, DS2) or watching music videos (Jin &|
|Taylor, DS2). Additionally, some of the children refer-|
|enced their previous music education experiences. In our|
|study, Jin, who has taken piano lessons, found Sketch-a-|
|Song limiting due to its representation of musical pitches|
|stating it felt “pedantic” (DS1). Zachary’s app included|
|a piano in the interface, including letters for the different|
|keys. Similarly, Annie included solfège (i.e., do, re, mi) as|
|the notes for her app “Color Block.”|



While the children’s interactions initially focused on the process of exploring with music, they mentioned the importance of these customization options to give them a sense of control as they created. This was especially important as the children formed creative products. As an illustration, reflecting on TextAlive and Sketch-a-Song, Taylor noted “You can’t create your own song [in the apps], you’re just designing it, and even then, you don’t have much control over it” (DS1). 

|perform the song the user created (DS2). During the full|
|---|
|group discussion in DS1, Jin summed up the importance|
|of the visuals noting, “when you could see or hear a differ-|
|ence, it makes you feel like you’re in more control of what|
|is going on.”|



|Our analysis further suggests that the visual aspects of|
|---|
|an app act as a bridge to better understand musical possi-|
|bilities. One sticky note from DS1 captured that the kids|
|disliked that the “MVs [referencing the animation of the|
|characters in Incredibox] don’t seem to match/vibe [of the<br>music] naturally” with the sounds and that it was distract-|
|ing that the people were “not wearing clothes before you|
|dress them” (DS1). In DS2, children also considered colors<br>and aesthetics in their own designs. The sounds in Emma’s<br>remixed version of Incredibox, “Cat Choir,” were all re-|
|lated to cats and cat activities (e.g., scratching, meowing,|
|and purring), to match the sounds to the visuals of cats.|
|Similarly, Annie used different colors to represent differ-|
|ent pitches. Jin created the app “Dreamer,” a game that lets<br>users play through a young girl’s dreams. Each dream had|
|its own visual aesthetic or “vibe,” corresponding with the|
|sounds and instruments, such as clam shells as percussion|
|instruments in an “aquatic dream” as seen in Figure 1.|



## 4.2 Visuals as a Bridge to Music 

## 4.3 Interface Preferences and User Interactions 

|Within our sessions, we found a connection between vi-|
|---|
|suals and sounds, with children noting that the aesthet-|
|ics of an application changed the way the music was per-|
|ceived. For example, Jin stated: “I liked changing the col-<br>ors because even if you’re given this format [in TextAlive|
|Flow], since colors have a strong effect on how music is|
|portrayed, you can change the whole vibe, even if you are|
|restricted” (DS1). Other children noted changing colors to|
|fit their experience was important demonstrated by three<br>distinct sticky notes expressing appreciation for “many op-<br>tions for colors,” “all the color options,” and “cool color|
|range” when discussing customization in TextAlive. Dur-|
|ing DS1, an adult co-designer also noted that children also|
|became visibly excited when able to use animations in us-|
|ing TextAlive and TextAlive Flow, as evidenced by a sticky|
|that read the options for animation in TextAlive Flow “are|
|cool” and another that they liked the “active lyrics” as they<br>|
|moved across the screen (DS1 – Sticky Note <sup>2 </sup>). Anima-|
|tions also were added into some of the children’s apps,|
|such as Zachary, who had boxes that represented musical<br>notes "fly down" from the top of the screen.|



|Children also showed a preference for direct interac-|
|---|
|tions, preferring the ability to manipulate elements through|
|touch, drag, and drop actions. For example, Taylor noted|
|that she “like[ed] touching [the iPad] instead of the mouse|
|because the mouse was harder to use” (DS1). Similarly,|
|many of the children’s designs in DS2 also included the|
|ability to drag and drop elements, such as the outfits that|
|could be dragged onto cats in Emma’s application or the|
|color blocks that could be dragged in Annie’s app.|



|tions for colors,” “all the color options,” and “cool color<br>range” when discussing customization in TextAlive. Dur-<br>ing DS1, an adult co-designer also noted that children also<br>became visibly excited when able to use animations in us-<br>ing TextAlive and TextAlive Flow, as evidenced by a sticky<br>that read the options for animation in TextAlive Flow “are<br>cool” and another that they liked the “active lyrics” as they<br>moved across the screen (DS1 – Sticky Note <sup>2 </sup>). Anima-|When the gulf of execution [81] in the interfaces was<br>large (i.e., the interfaces do not afford what happens when<br>manipulated), children became frustrated. For example,<br>some disliked the "confusing" parameter tuning interface<br>of TextAlive that appears next to the video, sometimes forc-<br>ing them to tweak parameters indirectly. They favored<br>the more direct control of TextAlive Flow instead, which<br>allows them to touch the video and change the parame-<br>|
|---|---|
|tions also were added into some of the children’s apps,<br>such as Zachary, who had boxes that represented musical<br>notes "fly down" from the top of the screen.<br>Furthermore, the children in our study showed a<br>propensity toward characters and narrative to support their<br>experiences with music. Children noted the reason they<br>enjoyed Incredibox was because they “liked [the] incredi-|ters with their hands. They recommended design enhance-<br>ments to improve interface usability, citing dislikes such<br>as the absence of instrument labels and clarity on color-to-<br>instrument/note mapping in Sketch-a-Song (DS1 - Sticky<br>Note). In contrast, Emma noted a preference for Incredi-<br>box because it was "less frustrating" and "ignited creativ-<br>|
|box character’s designs” (DS1 – Sticky Note). Yet, other<br>children highlighted with their dislike of the “bad outfits,”<br>(DS1 – Sticky Note), suggesting they would like other op-<br>tions that suited their ideas. Children extended the idea of<br>characters into their own apps, such as Taylor and Emma<br>who included an option to have animated characters sing or|noises:clams shutting<br>(percussion), bubbles,<br>seaweed swaying,<br>aquatic dream|
|2 We use “DS1–Sticky Note” to refer to Likes/Dislikes/Design Ideas||
|captured on stickies during the design activity that were not attributed to<br>a specific child, but instead to the design group.|Figure 1. Jin’s app “Dreamer” from DS2|



|532|
|---|



Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

ity" by representing sounds with symbols rather than traditional instruments (DS1). This suggests that achieving a balance between visual interface design and a certain level of ambiguity is crucial to foster casual creative experiences. 

## 4.4 Sharing and Casual Creative Experiences 

In our study, participants highlighted the importance of sharing their creations and ensuring the quality of the final product. For example, children suggested that a sharing option should be added to Sketch-a-Song (DS1 – Sticky Note), a feature present in the application, though many of the children were unable to find it. During DS1, another adult facilitator noted some children physically left their groups to share their creations with friends, explaining interesting interactions and experiences documenting their creative choices while using the apps. Taylor and Seiko requested time to share their song from Sketch-a-Song with the entire group, indicating pride in their work (DS1), and noted that they felt that it sounded good enough to share. In DS2, Emma, Han, Taylor, and Jin incorporated features allowing users to share and listen to others’ creations or playlists in their apps as well. Jin and Taylor’s apps even enabled users to create songs with accompanying videos inspired by others (DS2). This suggests that though children were exploring, they also wanted the output of these casual systems to sound good enough to share with others. 

## 5. DISCUSSION 

## 5.1 Purposeful Play: From Process “to” Outcome 

Children in our study attempted to balance exploring the possibilities provided by the application with creating personal intermediate outcomes to help express themselves, seeing casual interactions with music as a form of purposeful play. We suggest that casual creation is better understood as a "process to outcome" rather than "process over outcome," as we initially stated. In this view, children see themselves as designers of creative works, with the play experience focused on expression. 

In our findings, we observed that children wanted the ability to have some sense of control over their experiences (4.1) but that these came via scaffolds such as the visuals of the application (4.2) and interactions with the application (4.3) that lead to shareable outcomes (4.4). This conception of supported play aligns with previous work within music education [22] as well as MIR. Cunningham and Zhang, who conducted PD sessions with children to create a music organizer called Kids Music Box suggested the final design of their application offered a “playground” for interaction while listening to songs [35, p.190]. Similarly, PlaceAndPlay, an application design for creating and recording music, focused on children’s ability to simply try things out, with their results noting “all children had a great time when allowed to just play with the system” [82, p.738]. Facilitating children’s enjoyment and understanding of musical involvement entail not only promoting play 

but also nurturing their comprehension of cultural contexts [18] and social conventions [25]. More broadly, play can be understood in relation to creative processes [83–85], as many of the cognitive and emotional functions linked to creativity are also evident during play [86]. 

Importantly, children also expressed a desire for their final product to be share-worthy (4.4), indicating an expectation that their experience would yield a creative product representing their musical experience and tastes (4.1). We suggest that what sets casual CSTs apart from other educational technologies are the creation of “intermediate products.” The term "intermediate" can be understood as creative products that move users from what Beghetto and Kaufman suggest are “intrapersonal creativity that is part of the learning process” [61], to products recognized by others as creative. This concept of creativity is increasingly integrated into the evaluation of CSTs [62]. Furthermore, our findings underscore the importance of ensuring that casual CSTs for children focus on helping users create intermediate creative outcomes that remain coherent and aesthetically pleasing to support users’ creative selfefficacy [28]. 

## 5.2 The Purposeful Play Design Toolbox 

In this section, we introduce four design principles, deemed “tools,” to foster the elements that lead to purposeful play, suggesting specific design features for each. 

## 5.2.1 Controlled Serendipity 

Previous work in creative MIR has shown that serendipity is a crucial aspect for supporting meaningful interactions with music information during the creative process [32]. This was an important element in supporting nonmusicians in musical creativity [56]. When surprised by an app, children in our study felt excited and inspired, like Emma’s excitement with Incredibox (4.3). However, they also wanted their creations to feel genuinely theirs, i.e., their individual exploration mattered (4.4). Therefore, casual music tools should offer structured control while guiding users towards aesthetically pleasing results that reflect their goals. Novices often do not have the domain knowledge to identify how to execute specific creative goals or whether those goals are domain relevant [87, 88]. Therefore, a system taking on the role of the guiding professional by supplying options that support a pleasing final product, may help children to feel excited about their creative outputs. For example, both Incredibox and Sketch-a-Song only supplied notes that corresponded to a specific chord progression, and as a result, any "seemingly" random combination of sound layers or feature options also sounded good to the children. Similarly, TextAlive and TextAlive Flow supplied templates or color combinations that looked aesthetically pleasing and matched the music. The carefully and intentionally constrained environment was able to provide the sense of serendipity but at the same time produce outcomes that children felt good about and wanted to show off. 

533 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

Design Features. Implementing structured guidelines alongside controlled randomness provides a framework for fostering creativity. Feedback mechanisms that allow transparency serve to facilitate children in revisiting and elaborating upon moments of unexpected discovery. 

visual scaffolds and potential direct interactions that lead to moments of play in digital creative systems. 

Design Features. Interactive elements such as dragand-drop functionalities, objects responding to user actions, and tactile interactions, will enhance children’s engagement and maintain their interest over time. 

## 5.2.2 Visual Scaffolds 

The term scaffold can be understood as the use of a temporary framework for supporting learners as they aim to gain new skills [89]. During our analysis, children expressed consideration of the role of an application’s visuals when creating (4.2). In a sense, musical experiences were “scaffolded” by the visual aesthetics of the application, since the intention of the musical technology is to encourage children to develop an aesthetic perspective [90] through clear and direct visual communication of the application’s possibilities for creation. When visuals do not align with the sounds, or at least align in a way that a child expected, such as when the animations in Incredibox did not align with the music, it can be distracting and take away from understanding of the music, even if the UI design in clear. Yet, as Emma noted (4.3), some ambiguity in the visual scaffolding can also spark creative experiences as well. Specifically, our results emphasize that color and characters are two visual scaffolds that are effective for children. Furthermore, our findings suggest that children perceive casual creation as encompassing multiple mediums, often utilizing sound and video, aligning with the conception of children’s musical experiences being multimodal [52]. Prior research advocates for multimedia authoring activities that enable collaborative reflection among children [91,92], promoting self-expression [93] at both individual and social levels. 

Design Features. Visual elements like real-time visualizations, character-based imagery, customizable aesthetics, and visual ambiguity, when integrated into features designed to evoke serendipitous moments, along with multimodal outputs like videos, can act as scaffolds to support children’s musical interest. 

## 5.2.4 Shareable Intermediate Outputs 

The children in our study wanted the ability to share the creative outputs they were proud of during their exploration of different tools (4.4). Allowing children to share their creative outputs can help build creative self-efficacy [28], which is essential to fostering their view of themselves as creators. Allowing children to share these objects encourages creativity at not only an individual level, but also a social level, which is particularly important as social-environmental factors have been shown to influence creativity of individuals [98]. This is particularly important for children as creativity is largely social for them [53,55]. 

Design Features. Sharing options (email, file downloads, replay), galleries of user-generated content, ability to remix or elaborate on others outputs will help support self-efficacy of children as developing creators. 

## 6. LIMITATIONS AND FUTURE WORK 

While our research follows established precedents, it has limitations. The small sample size of 10 children, while comparable to similar co-design studies [68, 69], may limit the generalizability of the result. Participants were mainly from a single geographic area, with privileged backgrounds, and familiar with technology and co-design, which may not represent diverse socio-economic perspectives. Future studies should include more diverse demographics, explore evaluation methods for supporting design principles, and investigate features tailored to different MIR tasks in support of purposeful play. 

## 7. CONCLUSION 

## 5.2.3 Direct Manipulation 

Children in our study preferred the ability to directly interact with the interface, which can be understood as a form of direct manipulation [94]. Shneiderman, who suggested the term, notes four features of user interfaces that utilize this concept: continuous representation of the object of interest, physical actions, immediate feedback, and the ability of novices to gain knowledge of the system quickly. Moreover, helping kids manipulate things effectively means showing clear connections within the subject area, which helps them link new skills with what they already know [95]. Furthermore, computer scientist Alan Kay [96] suggests that visuals play an important role in digital spaces–they offer representational systems that through manipulation lead to chains of abstract reasoning that creates symbols; in the semiotic terms, these symbols allow a user to externalize through the manipulation of representations [97]. This suggests a connection between the 

Our study explored the creative preferences of one user group, children, in casual music creation applications. Through two Participatory Design sessions, we observed children’s perceptions of casual musical creation as a personally-oriented process, where visuals and direct interactions allowed children to generate creative works they wished to share with others. We highlighted the importance of purpose in play duirng casual music creation, suggesting that casual creation applications should facilitate the process of exploration of music with the intention of expression. Additionally, we discussed the potential impact of this playful approach on creative MIR by presenting four design tools to support purposeful play and suggesting a set of design features that support these principles. We further believe that these insights transcend children, offering design implications for individuals of various musical skills and recreational adults who wish to explore musical experiences in a variety of ways. 

534 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

## 8. ACKNOWLEDGMENTS 

We thank the child participants and adult co-designers for their contributions to the study, without whom this work would not be possible. This material is based upon work supported by the Institute of Museum and Library Services under Award #LG-252291-OLS-22. This work was supported in part by JST CREST Grant Number JPMJCR20D4, Japan. 

## 9. REFERENCES 

- [1] H. Jenkins, Convergence Culture : Where Old and New Media Collide. New York University Press, 2006. 

- [2] T. J. Tanenbaum, A. M. Williams, A. Desjardins, and K. Tanenbaum, “Democratizing technology: pleasure, utility and expressiveness in diy and maker practice,” in Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, ser. CHI ’13. New York, NY, USA: Association for Computing Machinery, 2013, p. 2603–2612. [Online]. Available: https://doi.org/10.1145/2470654.2481360 

- [3] M. Resnick, M. Flanagan, C. Kelleher, M. MacLaurin, Y. Ohshima, K. Perlin, and R. Torres, “Growing up programming: democratizing the creation of dynamic, interactive media,” in CHI ’09 Extended Abstracts on Human Factors in Computing Systems, ser. CHI EA ’09. New York, NY, USA: Association for Computing Machinery, 2009, p. 3293–3296. [Online]. Available: https://doi.org/10.1145/1520340.1520472 

- [4] M. A. Boden, The Creative Mind: Myths and Mechanisms, 2nd ed. Routledge, 2004. 

- [5] J. Koch, J. Pearson, A. Lucero, M. Sturdee, W. E. Mackay, M. Lewis, and S. Robinson, “Where art meets technology: Integrating tangible and intelligent tools in creative processes,” in Extended Abstracts of the 2020 CHI Conference on Human Factors in Computing Systems, ser. CHI EA ’20. New York, NY, USA: Association for Computing Machinery, 2020, p. 1–7. [Online]. Available: https: //doi.org/10.1145/3334480.3375172 

- [6] L. Manovich, Software Takes Command: Extending the Language of New Media, ser. International Texts in Critical Media Aesthetics. Bloomsbury, 2013. 

- [7] E. J. Humphrey, D. Turnbull, and T. Collins, “A brief review of creative mir,” ISMIR Late-Breaking News and Demos, 2013. 

- [8] J. Frich, L. MacDonald Vermeulen, C. Remy, M. M. Biskjaer, and P. Dalsgaard, “Mapping the Landscape of Creativity Support Tools in HCI,” in Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems, ser. CHI ’19. Association for Computing Machinery, 2019, pp. 1–18. [Online]. Available: https://dl.acm.org/doi/10.1145/3290605.3300619 

- [9] Apple Inc., “Logic pro,” v. 10.8.1. [Online]. Available: https://www.apple.com/logic-pro/ 

- [10] Ableton, “Ableton live,” v. 10.8.112. [Online]. Available: https://www.ableton.com/en/live/ 

- [11] Adobe, “Audition,” v. 24.0. [Online]. Available: https://www.adobe.com/products/audition.html 

- [12] MakeMusic, Inc., “Finale,” v. 27.4. [Online]. Available: https://www.finalemusic.com/ 

- [13] Avid, “Sibelius,” v. 2024.3. [Online]. Available: https://www.avid.com/campaigns/ musical-notation-software 

- [14] C.-H. Chuan and E. Chew, “Quantifying the benefits of using an interactive decision support tool for creating musical accompaniment in a particular style.” in ISMIR, 2010, pp. 471–476. 

- [15] M. Alinoori and V. Tzerpos, “Music-star: a style translation system for audio-based re-instrumentation.” in Proceedings of the 23rd Int. Society for Music Information Retrieval Conf, 2022, pp. 419–426. 

- [16] J. Ens and P. Pasquier, “Flexible generation with the multi-track music machine.” in 21st International Society for Music Information Retrieval Conference (ISMIR), 2020. 

- [17] Z. Wang and G. Xia, “Musebert: Pre-training music representation for music understanding and controllable generation.” in Proceedings of the 22nd Int. Society for Music Information Retrieval Conf, 2021, pp. 722–729. 

- [18] V. T. Kudryavtsev, “The phenomenon of child creativity,” International Journal of Early Years Education, vol. 19, no. 1, pp. 45–53, 2011. [Online]. Available: http://offcampus.lib.washington.edu/login?url=https: //search.ebscohost.com/login.aspx?direct=true&db= eue&AN=62823302&site=ehost-live 

- [19] M. P. Downton, “The aesthetics, creativity and craftsmanship of fourth graders’ compositions,” Journal of Music, Technology & Education, vol. 8, no. 3, pp. 273– 286, 2015. 

- [20] J. Garcia, T. Tsandilas, C. Agon, and W. E. Mackay, “Structured observation with polyphony: a multifaceted tool for studying music composition,” in Proceedings of the 2014 conference on designing interactive systems, 2014, pp. 199–208. 

- [21] M. Callanan, C. Cervantes, and M. Loomis, “Informal learning,” Wiley Interdisciplinary Reviews: Cognitive Science, vol. 2, no. 6, pp. 646–655, 2011. 

- [22] E. Harwood and K. Marsh, “3.2 Children’s Ways of Learning Inside and Outside the Classroom,” in The Oxford Handbook of Music Education, Volume 1. Oxford University Press, 09 2012. [Online]. Available: https://doi.org/10.1093/oxfordhb/ 9780199730810.013.0020\_update\_001 

535 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

- [23] K. Compton, “Casual creators: Defining a genre of autotelic creativity support systems,” Ph.D. dissertation, University of California, Santa Cruz, 2019. 

- [24] K. Compton and M. Mateas, “Casual creators.” in ICCC, 2015, pp. 228–235. 

- [25] M. A. Runco and N. Cayirag, “The Development of Children’s Creativity,” in Handbook of Research on the Education of Young Children, O. N. Saracho and B. Spodek, Eds. Taylor & Francis Group, 2012, pp. 102–114. [Online]. Available: http://ebookcentral.proquest.com/lib/ washington/detail.action?docID=1114640 

- [26] S. C. Hurwitz, “To be successful–let them play!(for parents particularly),” Childhood Education, vol. 79, no. 2, pp. 101–103, 2002. 

- [27] M. Helfand, J. C. Kaufman, and R. A. Beghetto, “The four-C model of creativity: Culture and context,” in The Palgrave Handbook of Creativity and Culture Research, V. P. Gl˘aveanu, Ed. Palgrave Macmillan UK, 2016, pp. 15–36. [Online]. Available: https://doi.org/10.1057/978-1-137-46344-9_2 

- [28] P. Tierney and S. M. Farmer, “Creative Self-Efficacy: Its Potential Antecedents and Relationship to Creative Performance,” The Academy of Management Journal, vol. 45, no. 6, pp. 1137–1148, 2002. [Online]. Available: https://www.jstor.org/stable/3069429 

- [29] J. L. Frost, “Neuroscience, play, and child development.” 1998. [Online]. Available: https: //eric.ed.gov/?id=ED427845 

- [30] C. S. Tamis-LeMonda, J. D. Shannon, N. J. Cabrera, and M. E. Lamb, “Fathers and mothers at play with their 2-and 3-year-olds: Contributions to language and cognitive development,” Child development, vol. 75, no. 6, pp. 1806–1820, 2004. 

- [31] R. J. Erickson, “Play contributes to the full emotional development of the child.” Education, vol. 105, no. 3, 1985. 

- [32] H. K. G. Andersen and P. Knees, “Conversations with expert users in music retrieval and research challenges for creative MIR.” in 17th International Society for Music Information Retrieval Conference (ISMIR), 2016. 

- [33] C. Bauer, “Report on the ISMIR 2020 special session: How do we help artists?” in ACM SIGIR Forum, vol. 54, no. 2. ACM New York, NY, USA, 2021, pp. 1–7. 

- [34] S. Choi, W. Kim, S. Park, S. Yong, and J. Nam, “Children’s song dataset for singing voice research,” in International Society for Music Information Retrieval Conference (ISMIR), 2020. 

- [35] S. J. Cunningham and E. Zhang, “Development of a music organizer for children.” in ISMIR, 2008, pp. 185–190. 

- [36] M. L. Guha, A. Druin, and J. A. Fails, “Cooperative Inquiry revisited: Reflections of the past and guidelines for the future of intergenerational co-design,” International Journal of Child-Computer Interaction, vol. 1, no. 1, pp. 14–23, 2013. [Online]. Available: https://www.sciencedirect.com/science/article/ pii/S2212868912000049 

- [37] J.-S. Baek and K.-P. Lee, “A participatory design approach to information architecture design for children,” Co-Design, vol. 4, no. 3, pp. 173–191, 2008. 

- [38] M. Coenraad, J. Palmer, D. Franklin, and D. Weintrop, “Enacting identities: Participatory design as a context for youth to reflect, project, and apply their emerging identities,” in Proceedings of the 18th ACM International Conference on Interaction Design and Children, ser. IDC ’19. New York, NY, USA: Association for Computing Machinery, 2019, p. 185–196. [Online]. Available: https://doi.org/10.1145/ 3311927.3323148 

- [39] S. Schepers, K. Dreessen, and B. Zaman, “Fun as a user gain in participatory design processes involving children: a case study,” in Proceedings of the 17th ACM Conference on Interaction Design and Children, ser. IDC ’18. New York, NY, USA: Association for Computing Machinery, 2018, p. 396–404. [Online]. Available: https://doi.org/10.1145/3202185.3202763 

- [40] A. Schiavio and M. Benedek, “Dimensions of Musical Creativity,” Frontiers in Neuroscience, vol. 14, 2020. [Online]. Available: https://www.frontiersin.org/journals/ neuroscience/articles/10.3389/fnins.2020.578932 

- [41] D. van der Schyff, A. Schiavio, A. Walton, V. Velardo, and A. Chemero, “Musical creativity and the embodied mind: Exploring the possibilities of 4e cognition and dynamical systems theory,” Music & Science, vol. 1, p. 2059204318792319, 2018. 

- [42] A. Cox, Music & Embodied Cognition. Indiana University Press, 2017. 

- [43] A. L. Veloso, “Composing music, developing dialogues: An enactive perspective on children’s collaborative creativity,” British Journal of Music Education, vol. 34, no. 3, pp. 259–276, 2017. 

- [44] P. Webster, “Creative thinking,” Music Educators Journal, vol. 76, no. 9, pp. 21–37, 1990. 

- [45] C. Ford and N. Bryan-Kinns, “Identifying engagement in children’s interaction whilst composing digital music at home,” in Proceedings of the 14th Conference on Creativity and Cognition, ser. C&C ’22. New York, NY, USA: Association for Computing Machinery, 

536 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

2022, p. 443–456. [Online]. Available: https://doi.org/ 10.1145/3527927.3532794 

- [46] D. Miell and R. MacDonald, “Children’s creative collaborations: The importance of friendship when working together on a musical composition,” Social Development, vol. 9, no. 3, pp. 348–369, 2000. 

- [47] P. R. Webster, “Children as creative thinkers in music,” The Oxford handbook of music psychology, pp. 421– 428, 2009. 

- [48] P. Burnard, “Rethinking ‘musical creativity’and the notion of multiple creativities in music,” in Musical creativity: Insights from music education research. Routledge, 2016, pp. 27–50. 

- [49] ——, “Understanding children’s meaning-making as composers,” in Musical creativity. Psychology Press, 2006, pp. 127–149. 

- [50] W. G. Crow, “Remixing the music curriculum: The new technology, creativity, and perceptions of musicality in music education,” Ph.D. dissertation, Institute of Education, University of London, 2012. 

- [51] M. Hickey, “The computer as a tool in creative music making,” Research Studies in Music Education, vol. 8, no. 1, pp. 56–70, 1997. 

- [52] S. E. Trehub and M. W. Weiss, The Routledge Companion to Music Cognition. Taylor & Francis Group, 2017, ch. Music Cognition: Developmental and Miltimodal Perspectives, pp. 403 – 414. 

- [53] S. Young, “The interpersonal dimension: A potential source of musical creativity for young children?” Musicae Scientiae, vol. 7, no. 1_suppl, pp. 175–191, 2003. 

- [54] P. R. Webster, “Creative Thinking in Music, Twenty-Five Years On,” Music Educators Journal, vol. 102, no. 3, pp. 26–32, 2016. [Online]. Available: http://journals.sagepub.com/doi/10.1177/ 0027432115623841 

- [55] P. Burnard, “The Individual and Social Worlds of Children’s Musical Creativity,” in The Child as Musician: A Handbook of Musical Development, G. McPherson, Ed. Oxford University Press, 2006, p. 0. [Online]. Available: https://doi.org/10.1093/ acprof:oso/9780198530329.003.0018 

- [56] Y. Wu and N. Bryan-Kinns, “Supporting NonMusicians? Creative Engagement with Musical Interfaces,” in Proceedings of the 2017 ACM SIGCHI Conference on Creativity and Cognition. ACM, 2017, pp. 275–286. [Online]. Available: https: //dl.acm.org/doi/10.1145/3059454.3059457 

- [57] R. W. Hass, R. Reiter-Palmon, and J. KatzBuonincontro, “Chapter 12 - are implicit theories of creativity domain specific? Evidence and implications,” in The Creative Self, ser. Explorations 

   - in Creativity Research, M. Karwowski and J. C. Kaufman, Eds. Academic Press, 2017, pp. 219–234. [Online]. Available: https://www.sciencedirect.com/ science/article/pii/B9780128097908000121 

- [58] J. J. Y. Chung, S. He, and E. Adar, “The intersection of users, roles, interactions, and technologies in creativity support tools,” in Proceedings of the 2021 ACM Designing Interactive Systems Conference, ser. DIS ’21. New York, NY, USA: Association for Computing Machinery, 2021, p. 1817–1833. [Online]. Available: https://doi.org/10.1145/3461778.3462050 

- [59] N. Davis, A. Zook, B. O’Neill, B. Headrick, M. Riedl, A. Grosz, and M. Nitsche, “Creativity support for novice digital filmmaking,” in Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, ser. CHI ’13. New York, NY, USA: Association for Computing Machinery, 2013, p. 651–660. [Online]. Available: https://doi.org/10.1145/ 2470654.2470747 

- [60] L. Benedetti, H. Winnemöller, M. Corsini, and R. Scopigno, “Painting with bob: assisted creativity for novices,” in Proceedings of the 27th Annual ACM Symposium on User Interface Software and Technology, ser. UIST ’14. New York, NY, USA: Association for Computing Machinery, 2014, p. 419–428. [Online]. Available: https://doi.org/10.1145/ 2642918.2647415 

- [61] R. A. Beghetto and J. C. Kaufman, “Toward a broader conception of creativity: A case for" mini-c" creativity.” Psychology of aesthetics, creativity, and the arts, vol. 1, no. 2, p. 73, 2007. 

- [62] E. Cherry and C. Latulipe, “Quantifying the creativity support of digital tools through the creativity support index,” ACM Trans. Comput.-Hum. Interact., vol. 21, no. 4, jun 2014. [Online]. Available: https://doi.org/ 10.1145/2617588 

- [63] M. H. Hagen, D. S. Cruzes, L. Jaccheri, and J. A. Fails, “Evaluating digital creativity support for children: A systematic literature review,” International Journal of Child-Computer Interaction, p. 100603, 2023. 

- [64] C. Zhang, C. Yao, J. Wu, W. Lin, L. Liu, G. Yan, and F. Ying, “StoryDrawer: A Child–AI Collaborative Drawing System to Support Children’s Creative Visual Storytelling,” in CHI Conference on Human Factors in Computing Systems. ACM, 2022, pp. 1–15. [Online]. Available: https://dl.acm.org/doi/10.1145/ 3491102.3501914 

- [65] S. McRoberts, Y. Yuan, K. Watson, and S. Yarosh, “Behind the scenes: Design, collaboration, and video creation with youth,” in Proceedings of the 18th ACM International Conference on Interaction Design and Children, ser. IDC ’19. New York, NY, USA: Association for Computing Machinery, 2019, p. 

537 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

173–184. [Online]. Available: https://doi.org/10.1145/ 3311927.3323134 

[76] “Sketch-a-Song,” https://www.sketchasong.com, v. 3.1.0. 

- [66] C. K. Lam, “Technology-enhanced creativity in k- 12 music education: A scoping review,” International Journal of Music Education, vol. 0, no. 0, p. 02557614231194073, 0. 

- [67] A. Druin, “The role of children in the design of new technology,” Behaviour and Information Technology, vol. 21, no. 1, pp. 1–25, 2002. 

- [68] J. C. Yip, F. M. T. Ello, F. Tsukiyama, A. Wairagade, and J. Ahn, “"money shouldn’t be money!" : An examination of financial literacy and technology for children through co-design,” in Proceedings of the 22nd Annual ACM Interaction Design and Children Conference, ser. IDC ’23. New York, NY, USA: Association for Computing Machinery, 2023, p. 82–93. [Online]. Available: https://doi.org/10.1145/ 3585088.3589355 

- [69] C. A. Liang, K. Albertson, F. Williams, D. InwardsBreland, S. A. Munson, J. A. Kientz, and K. Ahrens, “Designing an online sex education resource for gender-diverse youth,” in Proceedings of the Interaction Design and Children Conference. New York, NY, USA: Association for Computing Machinery, 2020, pp. 108–120. 

- [70] P. Alves-Oliveira, P. Arriaga, A. Paiva, and G. Hoffman, “Yolo, a robot for creativity: A co-design study with children,” in Proceedings of the 2017 Conference on Interaction Design and Children, ser. IDC ’17. New York, NY, USA: Association for Computing Machinery, 2017, p. 423–429. [Online]. Available: https://doi.org/10.1145/3078072.3084304 

- [71] M. Newman, K. Sun, I. B. Dalla Gasperina, G. Y. Shin, M. K. Pedraja, R. Kanchi, M. B. Song, R. Li, J. H. Lee, and J. Yip, “"i want it to talk like darth vader": Helping children construct creative selfefficacy with generative ai,” in Proceedings of the CHI Conference on Human Factors in Computing Systems, ser. CHI ’24. New York, NY, USA: Association for Computing Machinery, 2024. [Online]. Available: https://doi.org/10.1145/3613904.3642492 

- [72] J. Kato, T. Nakano, and M. Goto, “Textalive: Integrated design environment for kinetic typography,” in Proceedings of the 33rd Annual ACM Conference on Human Factors in Computing Systems, ser. CHI ’15. New York, NY, USA: Association for Computing Machinery, 2015, p. 3403–3412. [Online]. Available: https://doi.org/10.1145/2702123.2702140 

- [73] “TextAlive,” https://textalive.jp. 

- [74] “TextAlive Flow,” https://flow.textalive.jp. 

- [75] “Incredibox,” https://www.incredibox.com. 

- [77] J. Yip, T. Clegg, E. Bonsignore, H. Gelderblom, E. Rhodes, and A. Druin, “Brownies or bags-of-stuff? domain expertise in cooperative inquiry with children.” in Proceedings of the 12th International Conference on Interaction Design and Children (IDC ’13), 2013. 

- [78] A. L. Strauss, Qualitative Analysis for Social Scientists. Cambridge University Press, 1987. 

- [79] C. E. Hill, S. Knox, B. J. Thompson, E. N. Williams, S. A. Hess, and N. Ladany, “Consensual qualitative research: An update,” Journal of Counseling Psychology, vol. 52, no. 2, pp. 196–205, 2005. [Online]. Available: http://offcampus.lib.washington.edu/login?url=https: //search.ebscohost.com/login.aspx?direct=true&db= pdh&AN=2005-03263-009&site=ehost-live 

- [80] N. González, L. C. Moll, and C. Amanti, Funds of knowledge: Theorizing practices in households, communities, and classrooms. Routledge, 2006. 

- [81] D. Norman, The design of everyday things: Revised and expanded edition. Basic books, 2013. 

- [82] Y. Akiyama and S. Oore, “Placeandplay: a digital tool for children to create and record music,” in Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, ser. CHI ’08. New York, NY, USA: Association for Computing Machinery, 2008, p. 735–738. [Online]. Available: https://doi.org/10.1145/1357054.1357170 

- [83] S. C. Robyn M. Holmes, Lynn Romeo and M. Grushko, “The relationship between creativity, social play, and children’s language abilities,” Early Child Development and Care, vol. 185, no. 7, pp. 1180–1197, 2015. 

- [84] L. S. Vygotsky, “Imagination and creativity in childhood,” Journal of Russian & East European Psychology, vol. 42, no. 1, pp. 7–97, 2004. 

- [85] L. G. Hammershøj, “Creativity in children as play and humour: Indicators of affective processes of creativity,” Thinking Skills and Creativity, vol. 39, p. 100784, 2021. [Online]. Available: https://www.sciencedirect. com/science/article/pii/S1871187120302583 

- [86] S. W. Russ, “Play and creativity: Developmental issues,” Scandinavian Journal of Educational Research, vol. 47, no. 3, pp. 291–303, 2003. 

- [87] C. Remy, L. MacDonald Vermeulen, J. Frich, M. M. Biskjaer, and P. Dalsgaard, “Evaluating creativity support tools in hci research,” in Proceedings of the 2020 ACM Designing Interactive Systems Conference, ser. DIS ’20. New York, NY, USA: Association for Computing Machinery, 2020, p. 457–476. [Online]. Available: https://doi.org/10.1145/3357236.3395474 

538 

Proceedings of the 25th ISMIR Conference, San Francisco, USA and Online, Nov 10-14, 2024 

- [88] J. Baer, “The importance of domain-specific expertise in creativity,” Roeper Review, vol. 37, no. 3, pp. 165– 178, 2015. 

- [89] D. Wood, J. S. Bruner, and G. Ross, “The role of tutoring in problem solving,” Journal of Child Psychology and Psychiatry, vol. 17, no. 2, pp. 89–100, 1976. [Online]. Available: https://onlinelibrary.wiley. com/doi/abs/10.1111/j.1469-7610.1976.tb00381.x 

- [90] C. hu Ko and M. ju Cho, “Aesthetics in young children’s lives: From music technology curriculum perspective,” International Journal of Management, Economics and Social Sciences, vol. 2, no. 4, pp. 265–273, 2013. 

- [91] A. Davis and D. Weinshenker, Digital Storytelling and Authoring Identity. Cambridge University Press, 2012, ch. Digital Storytelling and Authoring Identity, pp. 47 – 74. 

- [92] A. Druin and C. Solomon, Designing multimedia environments for children. New York: J. Wiley & Sons, 1996. 

- [93] N. Wardrip-Fruin, Expressive Processing : Digital Fictions, Computer Games, and Software Studies, ser. Software Studies. MIT Press, 2009. 

- [94] Shneiderman, “Direct Manipulation: A Step Beyond Programming Languages,” Computer, vol. 16, no. 8, pp. 57–69, 1983. [Online]. Available: http://ieeexplore. ieee.org/document/1654471/ 

- [95] J. Jacobs, S. Gogia, R. Mundefinedch, and J. R. Brandt, “Supporting expressive procedural art creation through direct manipulation,” in Proceedings of the 2017 CHI Conference on Human Factors in Computing Systems, ser. CHI ’17. New York, NY, USA: Association for Computing Machinery, 2017, p. 6330–6341. [Online]. Available: https://doi.org/10.1145/3025453.3025927 

- [96] A. Kay, “User interface: A personal view,” The art of human-computer interface design, pp. 191–207, 1990. 

- [97] Y. Yamamoto and K. Nakakoji, “Interaction design of tools for fostering creativity in the early stages of information design,” International Journal of HumanComputer Studies, vol. 63, no. 4, pp. 513–535, 2005. [Online]. Available: https://www.sciencedirect.com/ science/article/pii/S1071581905000480 

- [98] T. M. Amabile, Creativity in Context: Update to "The Social Psychology of Creativity". Westview Press, 1996. 

539 

