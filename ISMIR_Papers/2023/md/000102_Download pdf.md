---
paper_id: "000102"
year: 2023
title: "Download pdf"
source_url: "https://zenodo.org/record/10265423/files/000102.pdf"
---

# THE MUSIC META ONTOLOGY: A FLEXIBLE SEMANTIC MODEL FOR THE INTEROPERABILITY OF MUSIC METADATA 

## Jacopo de Berardinis<sup>1</sup> Valentina Anita Carriero<sup>2</sup> Albert Meroño-Penuela<sup>1</sup> Andrea Poltronieri<sup>2</sup> Valentina Presutti<sup>2</sup> 

1 King’s College London, UK 

2 University of Bologna, Italy 

```
jacopo.deberardinis@kcl.ac.uk,andrea.poltronieri2@unibo.it
```

### ABSTRACT 

The semantic description of music metadata is a key requirement for the creation of music datasets that can be aligned, integrated, and accessed for information retrieval and knowledge discovery. It is nonetheless an open challenge due to the complexity of musical concepts arising from different genres, styles, and periods – standing to benefit from a lingua franca to accommodate various stakeholders (musicologists, librarians, data engineers, etc.). To initiate this transition, we introduce the Music Meta ontology, a rich and flexible semantic model to describe music metadata related to artists, compositions, performances, recordings, and links. We follow eXtreme Design methodologies and best practices for data engineering, to reflect the perspectives and the requirements of various stakeholders into the design of the model, while leveraging ontology design patterns and accounting for provenance at different levels (claims, links). After presenting the main features of Music Meta, we provide a first evaluation of the model, alignments to other schema (Music Ontology, DOREMUS, Wikidata), and support for data transformation. 

### 1. INTRODUCTION 

A music analyst, a computational musicologist, a music librarian, and a data engineer are working on a joint project. They need to contribute data from various musical sources, ranging from music libraries, annotated corpora and tune books, to audiovisual archives, radio broadcasts, and music catalogues. All data is eventually merged/aggregated as interconnected corpora, and linked to online music databases (e.g. MusicBrainz, Discogs) and knowledge bases (e.g. Wikidata). This creates opportunities to link cultural heritage artefacts to music industry data (streaming services, music professionals, etc.) and viceversa. 

This plot subsumes a recurring challenge for musical heritage projects [1]. Besides the individual requirements 

of each stakeholder – possibly rooted in different music genres, periods and datasets, a fundamental requirement is the interoperability of music metadata. 

Music metadata (alias bibliographic, or documentary music data) is used to consistently identify and describe musical works, their artists, recordings, and performances. For music industry, it allows for efficient management and distribution of music, which facilitate search and recommendation [2]. When metadata is accurate, it ensures that artists receive proper credit and compensation [3]. For musical heritage, metadata allows for the preservation and dissemination of musical works and traditions, but also aid in the research and study of music history and culture [4]. When integrating both views, metadata can help to promote diversity and inclusivity in the music industry by highlighting lesser-known genres and artists, while integrating information and artefacts of cultural interest [5]. 

Hence, a model that can consistently describe metadata is highly desirable – as it enables linking entities and concepts from various datasets (e.g. a composer is linked to a tune that has no authors in another collection). Semantic Web technologies can help achieve interoperability, as they facilitate data access and integration, resource discovery, semantic reasoning and knowledge extraction [6]. In the Resource Description Framework [7], data is described as `<subject-predicate-object>` triples using ontologies, and released as Knowledge Graphs (KGs). 

To achieve interoperability, one possibility akin to [8] is to let stakeholders design their own domain-specific ontologies, then use alignment algorithms to find connections between them (e.g. `MusicalWork` and `Composition` referring to the same concept). However, this approach comes with three major drawbacks: (i) ontology alignment is error-prone, hence links would still require manual inspection; (ii) even when alignment is sound, the semantics of classes and relationships may vastly differ across domains, which in turn, may create inconsistent alignments; (iii) it does not address the problem in the long-term. 

> © J. de Berardinis, V.A. Carriero, A. Meroño-Peñuela, A. Poltronieri, and V. Presutti. Licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). Attribution: J. de Berardinis, V.A. Carriero, A. Meroño-Peñuela, A. Poltronieri, and V. Presutti, “The Music Meta Ontology: a flexible semantic model for the interoperability of music metadata”, in Proc. of the 24th Int. Society for Music Information Retrieval Conf., Milan, Italy, 2023. 

### 1.1 Challenges and requirements for interoperability 

Another possibility is to reuse current ontologies for music metadata, such as the Music Ontology (MO) [9] and the DOREMUS ontology [10]. However, modelling music metadata across different genres and historical periods, to 

859 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

accommodate various use cases over heterogeneous data sources poses a number of challenges. First of all, it requires a perspective that harmonises all requirements from different stakeholders – to design a model that can be tailored to different data sources rather than to a single type of dataset. We categorise the main challenges and requirements for metadata interoperability as follows. 

### 1.1.1 Domain specificity hampers interoperability 

When looking at current ontologies, MO leans towards modelling discographic data with a focus on contemporary music, whereas DOREMUS is inherently rooted in classical music. These ontologies have been demonstrated to model metadata from MusicBrainz and BBC Music [11], and from classical music libraries and radio broadcasts for concerts programming [12], respectively. Their specificity makes them appealing when downstream applications show considerable overlap in terms of requirements and data. Examples include the reuse of MO in the WASABI project [13], to support the semantic annotation of audio music (emotions, lyrics, structures), but also for music recommendation [14] and listening [15]; and the adoption of DOREMUS by Philarmonie de Paris, Biblioteque National de France, and Radio France. 

Nevertheless, when drifting from discographic data and classical music, or attempting to reuse both models, addressing e.g. cultural heritage requirements while fostering interoperability becomes difficult. Indeed, a model reflecting the view and the interpretations ascribable to a musical genre, stakeholder, or dataset type may be difficult to reuse and extend to other domains. For instance, a music artefact may originate from oral transmission or be the result of a creative process that does not necessarily entail a formal composition process. The latter is common in songwriting, but also in folk music whenever a set of tunes (collected from different manuscripts) allows for the identification of a tune family [16]. Similarly, when expressing relationships between musical artefacts (alias derivations), it is important not to impose any modelling bias that may constrain possible interpretations (e.g. an arrangement having proper musical identity vs simply providing a different instrumentation). This is commonly referred to as “dominance of concept” [12], whose definition should be left to users depending on their data and domain expertise. 

Rather than attempting to achieve consensus on musical concepts and jargon, accounting for the interoperability calls for an abstraction layer for music metadata (“zoomout”) that can then be specialised, extended, and adapted to address domain-specific requirements (“zoom-in”). 

### 1.1.2 Expressivity is needed at different levels 

Another requirement for interoperability and reuse across various data sources is providing expressivity at different degrees, i.e. the possibility to conveniently describe music metadata at the right level of detail. For example, one data source may have granular/detailed information that requires high semantic expressivity (a composition process spread over different time, places, and involving more 

artists); whereas others may have basic (only the name of an artist is known) or even incomplete and uncertain information (a composition tentatively attributed to an artist). 

Here, the WikiProject Music<sup>1</sup> has been successful in providing expressivity to represent music metadata from different sources. As an extreme case of ontological flexibility, the schema underlying Wikidata – an open-ended, multi-domain KG built collaboratively like Wikipedia – is not specified in a previously agreed ontology, and the high expressivity overly adds complexity to the model. This is due to Wikidata’s scope being the most general. 

### 1.1.3 Provenance is fundamental for data integration 

Accounting for provenance is a central requirement for both cultural heritage and music industry. This becomes fundamental when integrating Knowledge Graphs from different datasets and stakeholders – as every single bit of data (each triple) should be attributable to a dataset/KG. Furthermore, integrating provenance is also needed within the context of a single dataset, at least for claims and links. 

Claims-Interpretations. Cultural heritage applications often require representing debatable statements or claims [17, 18]. These are usually the result of an interpretation process based on factual or documentary evidence (a dataset, a manuscript, etc.), and following a methodology and/or theory. Examples include personal information (e.g. the year/place of birth of a composer), and authorship claims (e.g. a composition being attributed to an artist). 

Links and identifiers. These includes links to artists’ official websites, fan pages, discussion forums, music reviews, record shops; as well as identifiers from music databases (e.g. MusicBrainz, Discogs, AllMusic), streaming platforms (e.g. Deezer, Spotify), and authoritative sources (e.g. ISNI, ISWC, ISRC). As most links and identifiers are crowdsourced or automatically inferred by entity linking algorithms, modelling provenance here promotes traceability and accountability of data sources. 

Notably, Wikidata addresses both these requirements, as every triple is considered a statement per se, for which so-called references can be appended and ranked. References may include information on the source, whether a computational method was used, and a date of retrieval. 

### 1.2 Our contribution 

We leverage the expertise and complementary views of various music stakeholders (musicologists, data engineers, music analysts, and heritage archivists) to contribute: 

- The Music Meta ontology, a rich flexible model to describe Western music metadata and its provenance at different levels of granularity. 

- An example-driven validation of the model, focused on the data elicited from four different stakeholders. 

- Code support to create Music Meta KGs without expert knowledge of the model, with automatic alignments to the MO, DOREMUS, and Wikidata. 

1 `https://en.wikipedia.org/wiki/Wikipedia: WikiProject_Music` 

860 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

### 2. RELATED WORK 

Besides metadata, the use of Semantic Web technologies in the music domain has contributed several ontologies, covering a variety of musical aspects and spanning both symbolic and audio music. 

Among them, the Music Theory Ontology [19] describe theoretical concepts of compositions, whereas the Music Score [20] and Music Notation [21] propose granular ontologies to represent elements of music scores. OMAC expresses features of musical entities but also musicological claims [22], while the OMRAS project [23] contributed ontologies to describe music chords as well as concepts related to tonality and temperament. 

In the audio domain, ontologies describe music production [24], audio features [25], effects [26]; an also model listening habits/taste [27], music-induced emotions [28], music structure [29,30], and musical similarities [31]. 

These ontologies have specific focus, and many were developed as stand-alone projects, with little or no alignment [32]. Instead, some ontologies focus on achieving interoperability between notations, taxonomies, and formats. These include the Internet of Musical Things [33], where heterogeneous musical objects are envisioned to coexist; the Music Annotation Pattern [34] which allows to model music annotations in the JAMS format [35]; and the Hamse ontology [36] describing musical features for musicological research. Similarly, [37] models abstract annotations of musical works, rather than concrete encodings. 

Interoperability at the level of musical content level resulted in successful MIR applications, such as the MIDI Linked Data Cloud [38] – integrating MIDI music to learn embeddings over the resulting KG [39]; and ChoCo [40] – a chord corpus integrating 18 chord datasets and enabling novel workflows for computational creativity [41]. 

### 3. THE MUSIC META ONTOLOGY 

To derive requirements from various music stakeholders, we leverage the domain expertise and views in Polifonia – a European H2020 project aiming to connect “music, people, places and events” from the 16th century. The interdisciplinarity of Polifonia, involving data engineers, anthropologists, ethnomusicologists, historians of music, linguists, musical heritage archivists, cataloguers, and creative professionals – makes it an ideal testbed for this work. 

Music Meta is part of the Polifonia Ontology Network [42], from which we reuse the CORE module. This is done to consistently reuse general-purpose elements of design (e.g. Person, Time, Place) and ontology design patterns. The reuse of this module also ensures alignment with other foundational models (FOAF, Dublin Core, etc.). 

The ontology (prefixed as `mm` ) is available at the following URI: `https://w3id.org/polifonia/ ontology/music-meta/` , and is released as open source project under the `CC-BY 4.0` on GitHub<sup>2</sup> . 

### 3.1 Methodology 

The development of Music Meta is driven by eXtreme Design (XD) [43], an agile ontology engineering methodology that makes extensive use of ontology design patterns (ODPs) – small ontologies that work as reusable templates for recurrent modelling problems. An ODP is intuitive and compact, clearly and formally defined, tackles a specific (sub)set of requirements, and is designed for a modular reuse, enabling a pragmatic cognitive analysis [44]. 

In XD, a story-based approach guides the collection of requirements. A story is a framework for customers to describe their needs, and is composed of 4 sections: (i) the persona, a description of a typical user; (ii) the overarching goal they need to address; (iii) the scenario, describing how the goal will be address; (iv) the competency questions (CQs) translating needs into formal requirements. Ontology modelling starts iteratively from the CQs, and is based on the reuse of ODPs and existent templates. 

### 3.1.1 From FRBR to Information Objects/Realisations 

At the core of Music Meta lies the use of the InformationRealisation (IR) ODP [45]. An information object is a nonphysical social object carrying information that can have one or multiple materialisations (information realisations). Each realisation is a particular physical object, or event, realising the the information object, or involving the latter as a participant. Both information object and realisation are intended as information entities (IE), i.e. (social) objects created and/or used to communicate, reason, and specify new entities. This allows to distinguish between a piece of information (e.g. the content of a composition) from how it is materialised (e.g. as a performance). 

On the other hand, both the Music Ontology [9] and DOREMUS [12] are built on top of different flavours of FRBR [46] (FRBRer and FRBRoo, respectively). FRBR is a conceptual model describing bibliographic resources at four levels: Work, Expression, Manifestation, andItem. In contrast, the two levels of the IR pattern map to Expression and Item, since Work and Manifestation are said to provide non-informative conceptualisations [45]. Moreover, [47] argues that FRBR’s Works – intended as “entities that preexist expressions”, cannot represent improvisations or traditional music, as they do not derive from a formal composition process leading to a realisation. FRBR’s Work is often ambiguously intended as an entity retrospectively created for grouping multiple expressions for cataloguing needs. As for the Manifestation level, while its representation is straightforward in the bibliographic domain (e.g. the printed version of a book), its correspondence in the music domain is not fully intuitive, as it may relate to either a recording, a score, a compact disc, or all the above – thereby introducing complexity and ambiguity. 

Nevertheless, being aligned to two levels of FRBR, the IR ODP makes our model leaner and flexible, while still achieving interoperability with FRBR-based (music) ontologies. In fact, IE patterns are meant to boost the semantic integration of contents, tools, platforms, resources that are silo-ed or non-interoperable [45]. 

2 `https://github.com/polifonia-project/ music-meta-ontology` 

861 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 



<!-- Start of picture text -->
Prefixes<br>core:MusicDataset core:Place core:Person rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#<br>rdfs: http://www.w3.org/2000/01/rdf-schema#<br>owl: http://www.w3.org/2002/07/owl#<br>mm:isTrainedOn mm:wasFormedIn rdfs:subClassOf core:mm: https://w3id.org/polifonia/ontology/core/https://w3id.org/polifonia/ontology/music-meta/<br>* *<br>core:isMemberOf core:isMemberOf<br>mm:MusicAlgorithm mm:MusicEnsemble mm:Musician *<br>core:hasMember core:hasMember<br>core:TimeInterval<br>rdfs:subClassOf<br>core:hasTimeInterval<br>core:Alias core:hasLanguage core:Language mm:Award core:Role<br>mm:MusicEnsembleMembership<br>core:name core:hasAlias mm:nominatedForAward core:involvesRole<br>mm:receivedAward<br>mm:involvesMusic core:involvesRole<br>Ensemble<br>xsd:string core:name mm:MusicArtist core:involvesAgent core:AgentRole mm:involvesMemberOf<br>MusicEnsemble<br>mm:MusicEnsemble core:Role<br>mm:hasGenre mm:isInfluencedBy core:activityStartDate<br>mm:MusicGenre mm:hasCollaboratedWith core:activityEndDate xsd:dateTime mm:MusicArtist<br><!-- End of picture text -->

Figure 1. Describing music artists as musicians, music ensembles, and algorithms using the Graffoo notation (yellow boxes are classes, blue/green arrows are object/datatype properties, purple circles are individuals, green polygons are datatypes). 

### 3.2 Main elements of design 

From Polifonia’s CQs<sup>3</sup> , we identified those related to metadata, and aimed for a model capable to address the requirements in Section 1.1. Music Meta follows a hierarchical design (where each level extends the former to add expressiveness) and is complemented by data transformation rules to conveniently translate one level into another. To enable data integration from existing knowledge bases and datasets, we align Music Meta to other ontologies: the Music Ontology, DOREMUS, and Wikidata, after having identified common/similar classes and properties. 

### 3.2.1 Music artists 

To represent music creatives the class `mm:MusicArtist` generalises over musicians ( `mm:Musician` ), ensembles ( `mm:MusicEnsemble` ), and computational methods ( `mm:MusicAlgorithm` ), as illustrated in Figure 1. Musicians are seen as a specialisation of persons who can optionally be associated to a medium of performance (e.g. voice, guitar), and be part of a music ensemble (e.g. `MusicGroup` , `Orchestra` , `Choir` ). Depending on the data available, the latter can be expressed either through a membership relationship ( `core:isMemberOf` ), a specialisation of the former, such as `mm:isSingerOf` , or through a `mm:MusicEnsembleMembership` when the period of participation of the musician is available. 

All music artists can be associated to (one or more) `mm:MusicGenre` (s), express influences or collaborations, and share a period of activity. Here, the start date refers to the foundation for music ensembles, whereas the end date is used for discontinued projects for algorithms. 

### 3.2.2 Music inception 

The focal point of Music Meta is the `mm:MusicEntity` class (Figures 2 and 3). This class represents an Information Object, which is defined as the sum of all the elements that make up a piece of music. A Music Entity is composed of several components, including lyrics (generalised 

3 `https://github.com/polifonia-project/stories` 

through `mm:Text` to also account for `mm:Libretto` ), the entailed musical content ( `mm:AbstractScore` ) and its instrumentation ( `mm:Instrumentation` ). 

A `mm:AbstractScore` provides an abstraction to describe the musical properties of an entity, such as the form of a piece ( `mm:FormType` ), its constituents parts (e.g. `mm:Movement` or `mm:Section` ), and its key ( `mm:Key` ). Datatype properties also describe the tempo of the composition ( `mm:tempo` ) and its order ( `mm:orderNumber` ). A `mm:Instrumentation` can instead be formalised in a `mm:Score` , which can be either digital or paper. Through the score, the instrumentation describes one or more `mm:MediumOfPerformance` , each of which has a cardinality (e.g. 3 violins). 

It is also possible to describe relationships between different Music Entities, defined by parthood ( `mm:hasPart` ) and derivation ( `mm:isDerivedFrom` ). Derivations are used at the user’s discretion, based on the dominance of concept [12] (whose criteria attribute proper identity to a musical entity) and can be of different types: revision, transposition, cover, reconstruction, reduction, etc. This makes it possible to describe different types of compositions, rearrangements and modifications of an original piece, as well as influences and more complex types of derivations. For example, the production of a cover song (e.g. in a different musical genre) may keep the lyrics and introduce a new composition and instrumentation, hence resulting in a new `mm:MusicEntity` . In addition, Music Entities can be organised in `mm:Collection` , according to a `mm:CollectionConcept` that binds them together. 

In sum, the model provides flexibility across periods and genres as the proposed classes allow generalisations to be made about the text, the musical composition and its arrangement. (c.f. Section 1.1.1). Through the specialisation of classes, depending on the target domain/application, specificity can easily be achieved (c.f. Section 1.1.2). For example, a tune family can be seen as a `mm:Collection` encompassing several tunes (as music entities) based on specific criteria (e.g. similarity, provenance). 

862 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 



<!-- Start of picture text -->
core:Role<br>core:involvesRole<br>core:AgentRole mm:MusicArtist core:Task<br>core:has core:isInvolvedIn core:involvesAgent rdfs:subClassOf mm:LyricsWriting<br>AgentRole mm:MusicWriting<br>core:TimeIndexedSituation rdfs:subClassOf mm:CreativeProcess CreativeActionmm:involves mm:CreativeAction core:executesTask core:CreativeTask rdf:type mm:Instrumentation<br>mm:Orchestration<br>mm:creates core:hasTime mm:Remix<br>core:hasTimeInterval Interval core:hasPlace mm:Rearrangement<br>mm:MusicEntity core:TimeInterval core:Place<br><!-- End of picture text -->

Figure 2. Abstracting music inception as an product of a creative process, involving music artists in activities (music writing, instrumentation, etc.), defined in time and space and according to different roles. 



<!-- Start of picture text -->
mm:TextFragment mm:Lyrics mm:FormType<br>core:hasSource<br>mm:CollectionConcept mm:CreativeProcess core:hasPart<br>mm:creates mm:Text rdfs:subClassOf mm:Libretto mm:CompositionPart<br>core:isDefinedBy rdfs:subClassOf mm:Movement<br>core:hasPart<br>core:isDerivedFrom mm:hasText rdfs:Literal<br>mm:tempo rdfs:subClassOf mm:Section<br>mm:Collection core:isMemberOf mm:MusicEntity core:hasPart mm:AbstractScore<br>mm:hasKey mm:Key<br>mm:orderNumber<br>mm:hasOpusStatement mm:hasDedicationStatement mm:hasInstrumentation xsd:string<br>mm:isRealisedIn<br>mm:DigitalScore<br>mm:OpusStatement mm:DedicationStatement mm:Instrumentation mm:hasScore mm:Score rdfs:subClassOf<br>mm:opusSubNumber mm:opusNumber core:text mm:isDedicatedTo mm:isRealisedIn mm:hasScorePart mm:MusicSheet<br>xsd:integer rdfs:Literal core:Person mm:MediumOfPerformance mm:hasMedium mm:ScorePart mm:mediumCardinality xsd:integer<br>mm:hasFormType<br>core:hasPart<br><!-- End of picture text -->

Figure 3. Describing a music entity and the elements it contains: Text, AbstractScore and Instrumentation. 

### 3.2.3 From performance to recording and broadcast 

The realisation of a `mm:MusicEntity` is exemplified by `mm:MusicalPerformance` , which can be either live ( `mm:LivePerformance` ) or in a studio ( `mm:StudioPerformance` ). As illustrated in Figure 4, the place and time interval of a performance are described by `core:Place` and `core:TimeInterval` – involving one or more music artists (optionally, with a specific role). A performance may also create a new `mm:MusicEntity` if, e.g., the execution differs significantly from the original version. 

A Music Entity can also be recorded by means of a `mm:RecordingProcess` , which is a subclass of a `mm:CreativeProcess` . This makes it possible to describe information about both the production (e.g., producers) and the technical aspects of it (e.g., sound engineer, equipment used). The recording process produces a `mm:Recording` , which is contained in a `mm:Release` . 

Information about the broadcasting of a recording is modelled through the `mm:BroadcastingSituation` class (an instance of the Situation ODP [48]), which describes when and where the song was broadcast, and by which broadcaster ( `mm:Broadcaster` ). 

### 3.2.4 Publishing and licensing information 

The `mm:PublicationSituation` class describes information about the publication of a release, which is common to the publication of a `mm:Score` (c.f. Figure 4). For both a release and a score, it describes when and where they were published, and by a `mm:Publisher` . 

Licence information is described by the `mm:License` class, which applies to records, releases and scores. 

### 3.2.5 Modelling links and integrating provenance 

We propose a pattern based on RDF* [49] to describe the provenance at different levels (Figure 5). The use of RDF* is particularly useful for this purpose, as it allows to embed provenance information to every triple in the dataset. This simplifies and streamlines the model, eliminating the need for n-ary relations or reification for each triple. 

The proposed pattern is straightforward and comprises the class `core:Reference` , which describes the source of the reference (using the class `core:Source` ) and the method used to obtain the annotation (using the class `core:SourceMethod` ). Additionally, the datatype properties `core:confidence` and `core:retrievedOn` describe the confidence of the annotation and the date it was produced, respectively. 

863 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 



<!-- Start of picture text -->
mm:hasLicense<br>mm:CreativeProcess rdfs:subClassOf mm:RecordingProcess mm:producesRecording mm:Recording mm:isPartOfRelease mm:Release mm:Score mm:License<br>mm:creates mm:hasEquipment<br>mm:isRecordedBy<br>rdfs:subClassOf mm:MusicEntity mm:RecordingEquipment mm:isBroadcastedIn core:title cor e :title mm:hasPublicationSituation core:Agent<br>core:Place rdfs:subClassOf<br>mm:is core:hasPlace<br>RealisedBy core:hasTime mm:BroadcastingSituation core:hasDuration xsd:string mm:PublicationSituation mm:hasPublisher mm:Publisher<br>core:InformationRealisation rdfs:subClassOf Performancemm:Musical core:TimeInterval Interval<br>mm:hasBroadcaster core:hasTime core:hasPlace<br>rdfs:subClassOf Interval<br>Performancemm:Studio Performancemm:Live core:Agent rdfs:subClassOf mm:Broadcaster mm:MusicAnnotationTimeInterval core:TimeInterval core:Place<br><!-- End of picture text -->

Figure 4. Describing performance, recording, broadcasting, publication, and licensing. 



<!-- Start of picture text -->
owl:Thing disputableRelation owl:Thing<br>mm:hasReference<br>core:Reference mm:retrievedOn xsd:Date<br>mm:collectedBy mm:hasSource<br>mm:confidence<br>mm:Annotation<br>xsd:decimal core:Source<br>Method<br>Crowdsourced, A source can be a dataset,<br>computationally inferred a document, an annotation, etc.<br><!-- End of picture text -->

Figure 5. Our pattern to describe provenance with RDF*. 

### 3.3 Conversion rules and code support 

To facilitate the reuse of Music Meta and its data conversion into OWL/RDF Knowledge Graphs, we developed `PyMusicMeta` – a library to map arbitrary music metadata into RDF triples. This enables a practical and scalable workflows for data lifting to create Music KGs without expert knowledge of our ontological model. The library is developed in Python as an extension of RDF-Lib [50]. 

With each triple, `PyMusicMeta` adds alignments to the supported schema whenever possible. For example, the pseudo triple `<DavidBowieURI, rdf:type, mm:Musician>` in Music Meta will be complemented with `<DavidBowieURI, rdf:type, http://purl.org/ontology/mo/MusicArtist>` for Music Ontology, `<DavidBowieURI, rdf:type, http://erlangen-crm.org/E21_Person>` for DOREMUS (via the Erlangen Conceptual Reference Model [51]) and `<DavidBowieURI, rdf:type, https://www.wikidata.org/wiki/Q639669>` for Wikidata; to achieve interoperability of the Music KG. 

### 4. VALIDATION AND ADOPTION 

Following the XD methodology (c.f. Section 3.1), we validate Music Meta against the competency questions (CQs) driving its design. In this context, testing consists in formulating logical statements for each competency question – using the ontology as a formal model. Logical statements are encoded as SPARQL queries to evaluate the 

model. Examples of tested CQs include “In which time interval did the creation process take place?” and “Which is the language of the name/alias of a music artist?”. The complete list of CQs, together with their correspondent SPARQL queries can be found in the project’s repository. This also contributes a test framework where the ontology is automatically tested using the available SPARQL queries [52], whenever changes occur or new requirements are supported in future versions of Music Meta. 

Music Meta has already been used in ChoCo [40], the largest Harmony KG to date, obtained from the integration of 18 MIR datasets<sup>4</sup> . The ontology has also been specialised for folk metadata (Tunes Ontology) and extended to describe music datasets (CoMeta Ontology). All ontologies are part of the Polifonia Ontology Network (PON) and can be found at `https://github.com/ polifonia-project/ontology-network` . We also provide documentation, examples, and tutorials<sup>5</sup> . 

### 5. CONCLUSIONS 

The interoperability of metadata is an essential requirement for the integration of music datasets, which is currently hampered by the specificity of existent ontologies. Our work addresses interoperability requirements for the design of the Music Meta ontology – a rich and flexible semantic model for (Western) music metadata across different genres and periods, for various stakeholders and music datasets. The model is based on the InformationRealisation ontology design pattern, allowing to reduce complexity while maintaining alignment to other ontologies (Music Ontology, DOREMUS). We validate Music Meta following the XD methodology, to demonstrate the support of requirements collected from various stakeholders (music analysts, archivists, musicologists, and data engineers). The model has modular design – allowing users to describe music data depending on their specificity and type, while providing provenance support through RDF*. We are extending the evaluation of Music Meta across cultural heritage and music industry datasets, while working with our stakeholders to specialise the model for the integration and release of Music Knowledge Graphs. 

> 4 `https://github.com/smashub/choco` 

> 5 `https://polifonia-project.github.io/ ontology-network/` 

864 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

Acknowledgements This project has received funding from the European Union’s H2020 research and innovation programme under grant agreement No 101004746. The authors also acknowledge Philippe Rigaux, Peter van Kranenburg, Marco Gurrieri, and Mari Wigham for their support and feedback throughout the design of Music Meta. 

### 6. REFERENCES 

- [1] T. Bottini, V. A. Carriero, J. Carvalho, P. Cathé, F. Ciroku, E. Daga, M. Daquino, A. Davy-Rigaux, M. Guillotel-Nothmann, Gurrieri, P. van Kemenade, E. Marzi, A. Meroño Peñuelala, P. Mulholland, E. Musumeci, V. Presutti, and A. Scharnhorst, “D1.1 roadmap and pilot requirements 1st version,” EU Commission, The Polifonia consortium, Tech. Rep., 2021. 

- [2] F. Pachet, “Knowledge management and musical metadata,” Idea Group, vol. 12, 2005. 

- [3] C. Sitonio and A. Nucciarelli, The impact of blockchain on the music industry. Calgary: International Telecommunications Society (ITS), 2018. 

- [4] S. Giannoulakis, N. Tsapatsoulis, and N. Grammalidis, “Metadata for intangible cultural heritage,” in Proceedings of the 13th international joint conference on computer vision, imaging and computer graphics theory and applications (VISAPP 2018), 2018, pp. 634–645. 

- [5] B. de Miguel-Molina and R. Boix-Doménech, “Introduction: Music, from intangible cultural heritage to the music industry,” Music as Intangible Cultural Heritage: Economic, Cultural and Social Identity, pp. 3–8, 2021. 

- [6] T. Berners-Lee, J. Hendler, and O. Lassila, “The semantic web,” Scientific american, vol. 284, no. 5, 2001. 

- [7] O. Lassila, R. R. Swick et al., “Resource description framework (RDF) model and syntax specification,” 1998. 

- [8] N. Corthaut, S. Govaerts, K. Verbert, and E. Duval, “Connecting the Dots: Music Metadata Generation, Schemas and Applications.” in ISMIR, 2008, pp. 249– 254. 

- [9] Y. Raimond, S. A. Abdallah, M. B. Sandler, and F. Giasson, “The Music Ontology.” in ISMIR, vol. 2007. Vienna, Austria, 2007, p. 8th. 

- [10] M. Achichi, R. Bailly, C. Cecconi, M. Destandau, K. Todorov, and R. Troncy, “Doremus: Doing reusable musical data,” in ISWC: International Semantic Web Conference, 2015. 

- [11] Y. Raimond and M. Sandler, “Evaluation of the music ontology framework,” in The Semantic Web: Research and Applications: 9th Extended Semantic Web Conference, ESWC 2012, Heraklion, Crete, Greece, May 27-31, 2012. Proceedings 9. Springer, 2012. 

- [12] P. Choffé and F. Leresche, “DOREMUS: connecting sources, enriching catalogues and user experience,” in 24th IFLA World Library and Information Congress, 2016, pp. 1–20. 

- [13] M. Buffa, E. Cabrio, M. Fell, F. Gandon, A. Giboin, R. Hennequin, F. Michel, J. Pauwels, G. Pellerin, M. Tikat et al., “The WASABI dataset: cultural, lyrics and audio analysis metadata about 2 million popular commercially released songs,” in The Semantic Web: 18th International Conference, ESWC 2021, Virtual Event, June 6–10, 2021, Proceedings 18. Springer, 2021, pp. 515–531. 

- [14] M. Á. Rodríguez-García, L. O. Colombo-Mendoza, R. Valencia-García, A. A. Lopez-Lorca, and G. Beydoun, “Ontology-based music recommender system,” in Distributed Computing and Artificial Intelligence, 12th International Conference. Springer, 2015, pp. 39–46. 

- [15] A. Adamou, S. Brown, H. Barlow, C. Allocca, and M. d’Aquin, “Crowdsourcing Linked Data on listening experiences through reuse and enhancement of library data,” International Journal on Digital Libraries, vol. 20, no. 1, pp. 61–79, 2019. 

- [16] P. van Kranenburg, B. Janssen, A. Volk et al., “The Meertens tune collections: The annotated corpus (mtcann) versions 1.1 and 2.0. 1,” Meertens Online Reports, vol. 2016, no. 1, 2016. 

- [17] M. Daquino, V. Pasqual, and F. Tomasi, “Knowledge Representation of digital Hermeneutics of archival and literary Sources,” Knowledge Representation of digital Hermeneutics of archival and literary Sources, pp. 59– 76, 2020. 

- [18] M. Daquino, V. Pasqual, F. Tomasi, and F. Vitali, “Expressing Without Asserting in the Arts,” in CEUR WORKSHOP PROCEEDINGS, vol. 3160, 2022. 

- [19] S. M. Rashid, D. De Roure, and D. L. McGuinness, “A Music Theory Ontology,” in Proceedings of the 1st International Workshop on Semantic Applications for Audio and Music, ser. SAAM ’18. New York, NY, USA: Association for Computing Machinery, 2018, p. 6–14. 

- [20] J. Jones, D. de Siqueira Braga, K. Tertuliano, and T. Kauppinen, “MusicOWL: The Music Score Ontology,” in Proceedings of the International Conference on Web Intelligence, ser. WI ’17. New York, NY, USA: Association for Computing Machinery, 2017. 

- [21] S. S.-s. Cherfi, C. Guillotel, F. Hamdi, P. Rigaux, and N. Travers, “Ontology-Based Annotation of Music Scores,” in Proceedings of the Knowledge Capture Conference, ser. K-CAP 2017. New York, NY, USA: Association for Computing Machinery, 2017. 

865 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

- [22] E. M. Sanfilippo and R. Freedman, “Ontology for analytic claims in music,” in New Trends in Database and Information Systems, S. Chiusano, T. Cerquitelli, R. Wrembel, K. Nørvåg, B. Catania, G. Vargas-Solar, and E. Zumpano, Eds. Cham: Springer International Publishing, 2022, pp. 559–571. 

- [23] G. Fazekas, Y. Raimond, K. Jacobson, and M. Sandler, “An overview of Semantic Web activities in the OMRAS2 project,” Journal of New Music Research, vol. 39, 12 2010. 

- [24] G. Fazekas and M. B. Sandler, “The Studio Ontology Framework,” in Proceedings of the 12th International Society for Music Information Retrieval Conference, ISMIR 2011, Miami, Florida, USA, October 24-28, 2011. University of Miami, 2011. 

- [25] A. Allik, G. Fazekas, and M. B. Sandler, “An Ontology for Audio Features,” in Proceedings of the 17th International Society for Music Information Retrieval Conference, ISMIR 2016, New York City, United States, August 7-11, 2016, 2016. 

- [26] T. Wilmering, G. Fazekas, and M. B. Sandler, “The Audio Effects Ontology,” in Proceedings of the 14th International Society for Music Information Retrieval Conference, ISMIR 2013, Curitiba, Brazil, November 4-8, 2013, 2013. 

- [27] Òscar Celma and X. Serra, “FOAFing the music: Bridging the semantic gap in music recommendation,” Journal of Web Semantics, vol. 6, no. 4, pp. 250–256, 2008, semantic Web Challenge 2006/2007. [Online]. Available: https://www.sciencedirect.com/ science/article/pii/S1570826808000711 

- [28] S. Song, M. Kim, S. Rho, and E. Hwang, “Music Ontology for Mood and Situation Reasoning to Support Music Retrieval and Recommendation,” in 2009 Third International Conference on Digital Society, 2009, pp. 304–309. 

- [29] B. Fields, K. R. Page, D. D. Roure, and T. Crawford, “The segment ontology: Bridging music-generic and domain-specific,” in Proceedings of the 2011 IEEE International Conference on Multimedia and Expo, ICME 2011, 11-15 July, 2011, Barcelona, Catalonia, Spain. IEEE Computer Society, 2011. 

- [30] N. Harley and G. Wiggins, “An ontology for abstract, hierarchical music representation,” in Demo at the 16th International Society for Music Information Retrieval Conference (ISMIR 2015), Malaga, Spain, 2015. 

- [31] K. Jacobson, Y. Raimond, and M. B. Sandler, “An Ecosystem for Transparent Music Similarity in an Open World,” in Proceedings of the 10th International Society for Music Information Retrieval Conference, ISMIR 2009, Kobe International Conference Center, Kobe, Japan, October 26-30, 2009, K. Hirata, G. Tzanetakis, and K. Yoshii, Eds. International 

Society for Music Information Retrieval, 2009, pp. 33–38. [Online]. Available: http://ismir2009.ismir.net/ proceedings/OS1-2.pdf 

- [32] V. A. Carriero, F. Ciroku, J. de Berardinis, D. S. M. Pandiani, A. Meroño-Peñuela, A. Poltronieri, and V. Presutti, “Semantic Integration of MIR Datasets with the Polifonia Ontology Network,” in ISMIR Late Breaking Demo, 11 2021. 

- [33] L. Turchet, F. Antoniazzi, F. Viola, F. Giunchiglia, and G. Fazekas, “The internet of musical things ontology,” Journal of Web Semantics, vol. 60, p. 100548, 2020. 

- [34] J. de Berardinis, A. M. Penuela, A. Poltronieri, and V. Presutti, “The Music Annotation Pattern,” in The Semantic Web–ISWC 2022 21st International Semantic Web Conference: 13th Workshop on Ontology Design and Patterns (WOP2022), 2022. 

- [35] E. J. Humphrey, J. Salamon, O. Nieto, J. Forsyth, R. M. Bittner, and J. P. Bello, “JAMS: A JSON Annotated Music Specification for Reproducible MIR Research.” in ISMIR, 2014, pp. 591–596. 

- [36] A. Poltronieri and A. Gangemi, “The HaMSE Ontology: Using Semantic Technologies to support Music Representation Interoperability and Musicological Analysis,” arXiv preprint arXiv:2202.05817, 2022. 

- [37] D. Lewis, E. Shibata, M. Saccomano, L. Rosendahl, J. Kepper, A. Hankinson, C. Siegert, and K. Page, “A model for annotating musical versions and arrangements across multiple documents and media,” in Proceedings of the 9th International Conference on Digital Libraries for Musicology, ser. DLfM ’22. New York, NY, USA: Association for Computing Machinery, 2022, p. 10–18. [Online]. Available: https://doi.org/10.1145/3543882.3543891 

- [38] A. Meroño-Peñuela, R. Hoekstra, A. Gangemi, P. Bloem, R. de Valk, B. Stringer, B. Janssen, V. de Boer, A. Allik, S. Schlobach, and K. Page, “The MIDI Linked Data Cloud,” in The Semantic Web – ISWC 2017. Cham: Springer International Publishing, 2017. 

- [39] P. Lisena, A. Meroño-Peñuela, and R. Troncy, “MIDI2vec: Learning MIDI embeddings for reliable prediction of symbolic music metadata,” Semantic Web, vol. 13, no. 3, pp. 357–377, 2022. 

- [40] J. de Berardinis, A. Meroño-Peñuela, A. Poltronieri, and V. Presutti, “ChoCo: a Chord Corpus and a Data Transformation Workflow for Musical Harmony Knowledge Graphs,” in Manuscript under review, 2023. 

- [41] ——, “The Harmonic Memory: a Knowledge Graph of harmonic patterns as a trustworthy framework for computational creativity,” in Proceedings of the ACM Web Conference 2023 (WWW ’23), April 30-May 4, 2023, Austin, TX, USA, 2023. 

866 

Proceedings of the 24th ISMIR Conference, Milan, Italy, November 5-9, 2023 

- [42] J. de Berardinis, V. A. Carriero, N. Jain, N. Lazzari, A. Meroño-Peñuela, A. Poltronieri, and V. Presutti, “The polifonia ontology network: Building a semantic backbone for musical heritage,” in Manuscript under review, 2023. 

- [43] E. Blomqvist, K. Hammar, and V. Presutti, “Engineering Ontologies with Patterns-The eXtreme Design Methodology.” Ontology Engineering with Ontology Design Patterns, no. 25, 2016. 

- [44] V. A. Carriero, M. Daquino, A. Gangemi, A. G. Nuzzolese, S. Peroni, V. Presutti, and F. Tomasi, “The Landscape of Ontology Reuse Approaches,” in Applications and Practices in Ontology Design, Extraction, and Reasoning, ser. Studies on the Semantic Web, G. Cota, M. Daquino, and G. L. Pozzato, Eds. Amsterdam: IOS Press, 2020, vol. 49, pp. 21–38. 

- [45] A. Gangemi and S. Peroni, “The Information Realization Pattern,” in Ontology Engineering with Ontology Design Patterns - Foundations and Applications, ser. Studies on the Semantic Web, P. Hitzler, A. Gangemi, K. Janowicz, A. Krisnadhi, and V. Presutti, Eds. IOS Press, 2016, vol. 25, pp. 299–312. [Online]. Available: https://doi.org/10.3233/978-1-61499-676-7-299 

- [46] “Genius website,” https://www.ifla.org, accessed: 2023-04-14. 

- [47] J. Riley, “Application of the Functional Requirements for Bibliographic Records (FRBR) to Music.” in ISMIR, 2008, pp. 439–444. 

- [48] A. Gangemi, N. Guarino, C. Masolo, A. Oltramari, and L. Schneider, “Sweetening ontologies with dolce,” in Knowledge Engineering and Knowledge Management: Ontologies and the Semantic Web, A. GómezPérez and V. R. Benjamins, Eds. Berlin, Heidelberg: Springer Berlin Heidelberg, 2002, pp. 166–181. 

- [49] O. Hartig, “Foundations of RDF* and SPARQL* (An Alternative Approach to Statement-Level Metadata in RDF),” in Alberto Mendelzon Workshop on Foundations of Data Management, 2017. 

- [50] C. Boettiger, rdflib: A high level wrapper around the redland package for common rdf applications, 2018. [Online]. Available: https://doi.org/10.5281/zenodo. 1098478 

- [51] J. Merges, M. Scholz, and G. Goerz, “Erlangen implementation of frbroo,” in CIDOC 2012, 2012. 

- [52] A. Fernández-Izquierdo, “Ontology testing based on requirements formalization in collaborative development environments.” in DC@ ISWC, 2017. 

867 

