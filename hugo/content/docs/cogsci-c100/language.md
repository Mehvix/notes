---
title: "13: Language"
weight: 13
---

{{< hint "info" >}}<!-- mathjax fix -->
# Controversies in Cognitive Science
> How is language acquired and how do we process words when reading?
* Is language learning innate, and if so, to what extent?
* How do we learn language?
    - **Skill building hypothesis**: Language is acquired as a result of learning language skills, such as vocabulary and grammar
    - **Comprehension hypothesis**: Language skills such as vocabulary and grammar, result from language acquisition
* How are words processed when we read?
    - **Direct access hypothesis**: Readers recognize words directly from the printed letters
    - **Indirect access hypothesis**: Readers convert the printed letters into a phonological code to access the word and its meaning
{{< /hint >}}

## Language

![](/docs/cogsci-c100/language/lang.png)
> **Language**: our spoken, written, or signed words and the ways we combine them to communicate meaning
- Trivia:
    * How many words does the average person know?
    * How many languages exist in the world today?
    * What percentage of the world’s children are bilingual? Of American children?
    * Do bilingual children perform better or worse on tests of language ability (in first language)? Of mathematical ability? Of following instructions?
{{< details "Answers to language trivia questions" "..." >}}
- Average adult has an active vocabulary of around 20,000 words and a passive vocabulary of around 40,000 words
    - That averages to nearly 7 new words per day between ages 2 and 18!
- Linguists estimate that 6500 languages exist in the world today
    - 250 languages are spoken by more than 1 million people
    - Only 600 languages have speaking populations robust enough to support their survival past the end of the century. Languages need at least 100,000 speakers to survive the ages.
- 66% of the world’s children are raised as bilingual speakers; only 6.3% of U.S. residents are bilingual
{{< /details >}}



# Development of Language

## Prenatal language comprehension

- "Dr. Seuss" study in which pregnant women read one of three children’s stories aloud once every day during the last 6 weeks of pregnancy (Decasper & Spence, 1986)
    - Infants tested when 2 days old
    - They were played two stories through earphones, one of which was the one they had heard
    - By changing their sucking patterns, they could control which story they heard
        * Newborns showed preference for the story they had heard prenatally
- Sound of a newborn baby’s cry may depend on the language the parents speak: babies imitate the general sound of their parents’ language (Mampe, Friederici, Christophe et al., 2009)
    - French babies cry with a rising melody
    - German babies prefer a falling melody

## Speech perception in infancy

- We are all born with the ability to recognize speech sounds or **phonemes** (e.g., b vs. p) from all the world’s languages but gradually lose this ability
    - Adult Hindi-speakers and young infants from English-speaking homes can easily discriminate two Hindi t sounds not spoken in English. By age one, however, English-speaking listeners rarely perceive this sound difference
    - Japanese speakers have difficulty distinguishing between English r and l
    - At birth or a few weeks after, infants can perceive almost all (95%) of the subtle phoneme differences in nonnative languages. However, by 8-10 months, accuracy drops to 70% and, by 10-12 month, to 20% (Werker, J.F., 1989)
    - Chinese adoptees living in Canada since age 1 process Chinese sounds as do native speakers, even if they have no conscious recollection of Chinese words (Pierce, Klein, Chen et al., 2014)
![](/docs/cogsci-c100/language/eng.png)
* **In general, it’s much easier to learn a language at an early age**

## Child-directed speech (motherese)

- Language comprehension and motherese (child-directed speech)
{{< columns >}}<!-- mathjax fix -->
- **Motherese or child-directed speech**: characterized by repetition, simple vocabulary and syntax, clear pronunciation, slow pace, high pitch with varying intonation, a focus on the here and now, and exaggerated facial expressions
    - Designed to make it easier for infant to decode the language
- Even young children will do this when speaking to younger siblings/playmates
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/language/baby.png)
{{< /columns >}}
![](/docs/cogsci-c100/language/summ.png)

# Theories of Language Development

## Chomsky’s Nativist View

- Children are born with an innate understanding of grammar and a predisposition to learn language (Language Acquisition Device)
- There is a **critical learning period** for the acquisition of language -- Evidence against this view:
    - Competency in a second language can be attained even when initial exposure to the language happens relatively late
        - However, those who learn a second language during early childhood are less likely to have an accent (Flege, Yeni-Komshiam, & Lui, 1999)
        - Also, in general, the older the age at immigration, the poorer the grammatical mastery of the second language (Johnson & Neport, 1991)

{{< figure  src="/docs/cogsci-c100/language/gx.png" >}}

- Evidence in support of critical learning period:
    - Cases of child abuse where a child is kept isolated from birth. When child is discovered and rescued early (before age 6), s/he can learn language but attempts at rehabilitation are not so successful when child kept in seclusion till later childhood (age 12)
    - Deaf children born to non-signing family never become grammatically fluent in sign language

---

- Chomsky’s **nativist view** (i.e., view that language learning is innate) is based on poverty of stimulus arguments: young children are simply not exposed to enough information to allow them to learn a language
    - Much of the speech that children hear is actually ungrammatical, but not flagged as such
    - Children are typically only exposed to positive information, i.e., they are not told what counts as ungrammatical (e.g., the bell ringed)

### Arguments against nativist view
1. Connectionist models demonstrate that it is possible to learn complex linguistic skills without having any explicit linguistic rules encoded in it
    - The learning trajectory of these networks strongly resembles the learning trajectory of human infants
         - Ex: learning how to form the past tense of English verbs, both regular and irregular
    - Children learning the English past tense go through three easily identifiable stages:
        - **Stage 1**: They employ a small number of very common verbs in the past tense (e.g., "got," "gave," "went," "was")
            - Most of these verbs are irregular, and assumption is that children learn these by rote
            - At this stage, children are not capable of generalizing from the words they have learned. They also tend not to make too many mistakes.
        - **Stage 2**: They use a much greater number of verbs in the past tense, some of which are irregular but most of which employ the regular past tense ending of "-ed"
            - During this stage, they can generate a past tense for an invented word (e.g., "ricked")
            - Children at this stage take a step backward and make mistakes on the past tense of irregular verbs that they had previously given correctly (overregularization errors),
                - Ex: saying, "gived" instead of "gave"
        - **Stage 3**: They learn more verbs and cease to make overregularization errors
        {{< figure  src="/docs/cogsci-c100/language/bbl.png" >}}
2. Bayesian (probabilistic) models of language learning demonstrate that a surprising amount can be learned through sensitivity to statistical regularities in heard speech
    - One of the most basic challenges in understanding speech is word segmentation: segmenting a continuous stream of sounds into individual words
        - In English, an actual physical event, such as a pause, marks a word boundary less than 40% of the time
        - How does 8-month-old infant (which is when this skill starts to emerge) figure out which combinations of syllables make words, and which ones don’t?
        - Can be explained by model of transitional probabilities
            - The transitional probability between any two sounds is the probability that the second will follow the first sound
            - High transitional probabilities will tend to indicate syllables occurring within a word, while low transitional probabilities will tend to occur across the boundaries of words
            - Infants are exquisitely sensitive to the frequency of correlations, and they exploit this sensitivity to parse streams of sound into words
        - Transitional probabilities may also be used by adults to map the boundaries of _phrases_
    - Research indicates that babies do show a remarkable ability to learn statistical aspects of human speech (Erickson & Thiessen, 2015; Werker, Gunthert, & German, 2012)
        - They are able to discern word breaks
            - As mentioned, an actual physical event, such as a pause, marks a word boundary less than 40% of the time in English
        - They statistically analyze which syllables -- as in hap-py-ba-by -- most often go together (Safran, 2009; Safran, Aslin, & Newport, 1996
            - 8-month-olds were exposed to 2 minutes of a computer voice speaking an unbroken, monotone string of nonsense syllables (bidakupadotigolabubidaku…)
            * Were able to recognize (as indicated by attentional measures) three-syllable sequences that appeared repeatedly
{{< figure  src="/docs/cogsci-c100/language/snd.png" >}}

## Vygotsky’s view

> Vygotsky argued that language is the foundation for the development of higher human thought: children use words as a way to learn to think
- Children of about 4 or 6 often talk aloud in a non-communicative manner
    - When children are drawing at a table, one might say, "I’ll make it green" without indicating what he would make green; another looking at his own drawing, might respond, "Horses like sugar and oats."
- Vygotsky contended that this type of non-communicative speech is a transition phase to the development of verbal thought
    - Consistent with this view, researchers have found that first and secondgraders who manifested the most muttering and lip movement while solving arithmetic problems showed the greatest improvements in their arithmetic ability over the course of a year
- Inner speech and spoken language eventually become independent

### Language as means of developing thinking

- Effect of Early Exposure of Language on Cognitive Development (Hart, & Risley, 1995, 2003)
- By age 3, a child growing up in poverty would have heard 30 million fewer words in his home environment than a child from a professional family
- Also, the greater the number of words children heard from their parents or caregivers before they were 3, the higher their IQ and the better they did in school
- TV talk not only doesn’t help, it is detrimental
    - Study found that infants (12-18 months) actually could not learn vocabulary by merely watching (bestselling) DVD in which spoken words were linked with appropriate objects (DeLoache, Chiong, Sherman et al., 2010)
    * Some researchers have argued that the racial and socioeconomic gap in academic performance can be wholly accounted for by disparities in exposure to language alone!
        - New intervention programs target this problem

## Cognitive-functional approach: the importance of meaning

> **The cognitive-functional approach**: emphasizes that the function of human language is to communicate meaning to other individuals
- There is no such thing as a perfect synonym or two identical sentences

{{< figure  src="/docs/cogsci-c100/language/syn.png" >}}

### Second Language Acquisition

> How do we learn language?

- **Skill building hypothesis**: Language is acquired as a result of learning language skills, such as vocabulary and grammar
    - **Use skill building**: learn grammar, study vocab lists, do drills, take tests
    > "No pain, no gain"
    * General public (and government) believe this is the way to learn language
- **Comprehension hypothesis (Stephen Krashen)**: language skills such as vocabulary and grammar, result from language acquisition -- we acquire language in one and only one way: when we understand messages
    - **Use "comprehensible input"**: listen to stories, read books, have conversations, watch movies
    - **Immediate gratification**: have a good time -- the more you enjoy it, the better your comprehension will be
* **Comprehensible input has won in pretty much every single study comparing the two methods**
- Some evidence in support of comprehensible input
    - Complexity of language learning, e.g., of vocab and grammar, wipes out skill building as a possibility
        - Average native English speaker knows 40,000+ words
    - Study found that second language readers who read a lot have larger vocabularies than native speakers who didn’t read a lot
    - It’s possible to acquire language without any conscious learning
- Implications:
    - What is of primary importance is not pushing a person to speak from
    - Rather, it is **listening**, picking up comprehensible input

### Natural language approach to second language learning

#### 1. Storytelling

{{< hint "info" >}}<!-- mathjax fix -->
- Find language partner who is fluent in language you are trying to learn, e.g., friend, family member, or language exchange partner
- Find magazines (20%), then children’s stories (80%) with tons of pictures, e.g., travel magazine with pictures related to travel, food, clothing, etc.
- Language partner is not going to translate story; will describe pictures and ask you simple questions, and you will ask simple questions
    - Partner doesn’t just describe what is in pictures: they describe the picture the way they might to a young child they love
        - Ex: "This is a spare tire. A spare tire is very important. You could have a blowout and then you would need to use that spare tire." (Jeff Brown)
{{< /hint >}}
- Rules to tell language partner
    - No English
        - If we don’t understand each other, we’ll use gestures and act or draw
        - If we still can’t understand, we’ll say "It’s not important" in target language
    - No grammar: don’t teach me any grammar
    - No corrections: don’t correct me at any time
- Factors that affect language acquisition
    - **Motivation**: positive correlation
    - **Self-esteem**: positive correlation
    - **Anxiety**: negative correlation
        * **For language acquisition to really succeed, anxiety should be zero**
- Affective filter
    - Somewhere in brain is a language acquisition device, according to Chomsky. Our job is to get input into that device. High anxiety blocks the input.
        - If a student thinks language class is a place where his weaknesses will be revealed, he may understand the input, but it won’t penetrate

#### 2. Read, read, read -- whatever is of interest to you
> "Free voluntary reading is the most powerful tool we have in all of language education"
- Read things that you’re passionate about
    - Watch baseball game, then go read about it in newspaper
        * This is also the key to teaching kids who don’t want to learn to read

### TPR

> **TPR (Total Physical Response)**: acquiring a language through movement
- Ask language partner to give you a list of commands or actions
    > Ex: Jump, walk, run, turn around, sit down, stand up, dance, talk, yell, complain, look, watch TV, turn TV on, turn TV off, cry, laugh
- Can use hands to pantomime movements
- Can also use gestures to represent words
- Do 50-100 per session

## Social context of speech

{{< columns >}}<!-- mathjax fix -->
> **Social context of speech**: learning language is not merely a matter of learning vocabulary and grammar -- the goal is not just to express one’s thoughts but must take into account other people’s thoughts, feelings, and beliefs

- Establishing common grounds
- We have social rules for the format of our conversations ("winding down" a conversation before saying "good-bye" on the phone)
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/language/context.png)
{{< /columns >}}
- Phrasing of directives, a sentence that requests someone to do something
    > _Could you give me a ride? vs. Will you give me a ride?_
- Use of indirect speech acts
    > _I wonder if there’s any butter in the refrigerator? and It’s cold in here_
- There are gender differences in the use of directives

# Speech Perception and AI

> Speech perception is an extremely complicated process (which is why computer voice recognition systems are often problematic!)
- Need to separate voice of speaker from irrelevant background noises, which might include other simultaneous conversations
- Pronunciation varies, depending on vocal characteristics of speaker
- Speakers often slur or mispronounce words
- Pronunciation of specific phoneme depends in large on previous and following phonemes, e.g., d in idle vs. d in don’t
- As mentioned, an actual physical event, such as a pause, marks a word boundary less than 40% of the time
    - Children’s mispronunciations of lyrics in Christmas carols and Pledge of Allegiance
- People use visual cues to facilitate speech perception
{{< columns >}}<!-- mathjax fix -->
- Study in which participants watched video of woman making one sound (ga) while different sound played (ba)
    * Responses reflected compromise (participants reported hearing da) (McGurk & MacDonald, 1976)
<---><!-- mathjax fix -->
{{< figure  src="/docs/cogsci-c100/language/viz.png" >}}
{{< /columns >}}
- Lipnet, developed by team at Oxford’s AI lab, can now also lipread (i.e., translate lip movements to text) with 95% accuracy
- Computers can now replicate human voices extremely accurately
    - Company Lyrebird has created program that can replicated voices of people, including powerful political figures, after analyzing only one minute of audio
- More challenging to replicate associated facial movements
    - Creating video of Obama required 14 hours of Obama high quality footage to train system to translate audio into mouth shapes

# Reading

>{{< figure  src="/docs/cogsci-c100/language/read.png" >}}
> - The eye makes saccadic movements ("jumps" that occur every 1/4 second) during reading
> - Good readers show fewer fixations, larger saccadic jumps, and fewer regressions than poor readers

- Readers use contextual cues to extract meaning
    > I cdnuolt blveiee taht I cluod aulaclty uesdnatnrd waht I was rdanieg. The phaonmneal pweor of the hmuan mnid. Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy, it deosn't mttaer inwaht oredr the ltteers in a wrod are, the olny iprmoatnt tihng is taht the frist and lsat ltteer be in the rghit pclae. The rset can be a taotl mses and you can sitll raed it wouthit a porbelm. Tihs is bcuseae the huamn mnid deos not raed ervey lteter by istlef, but the wrod as a wlohe. Amzanig huh? yaeh and I awlyas tghuhot slpeling was ipmorantt!

## Word Processing in Reading: Dual-route approach

- Dual-route approach to reading: **direct** vs. **indirect** access hypotheses
    - Do readers recognize a word directly from the printed letters (direct access)?
    - Or do they convert the printed letters into a phonological code to access the word and its meaning (indirect access)?
- Petersen, Fox, Posner, et al. (1988) explored this question in PET study
    - Condition 1 (looking): Participants asked to focus on a fixation point (a small crosshair) in the middle of a screen
    - Condition 2a (reading silently): Participants were presented with words flashed on the screen but told not to make any response
    - Condition 2b (listening): Participants listened to the same words being spoken
    - Condition 3 (reading out loud): Participants were asked to say out loud the word appearing on the screen
    - Condition 4 (speaking): Participants were presented with nouns on the screen and asked to utter an associated verb
        - Ex: Saying "turn" when presented with word "handlebars"
    - Results:
        - Areas of activation in Conditions 3 and 4 (speaking words) did not include areas in Condition 2a and 2b (reading silently and listening to words, respectively)
    - Conclusions:
        - Patterns of activation identified across the different tasks thus supported a parallel rather than a serial model of single-word processing
        - In addition, the results support the direct access hypothesis: we do not need to sound words out (or subvocalize) to access meaning of words
    - Moreover, research in general has indicated that, though readers use both direct and indirect access when reading, direct access is more efficient
        - Skilled adult readers are more likely to use direct access
        - Beginning and less skilled readers are likely to sound out words to understand meaning
{{< figure  src="/docs/cogsci-c100/language/tzt.png" >}}

## Dyslexia

> The direct and indirect approaches are reflected in two different types of dyslexia (learning disability that interferes with reading despite average or above average intelligence)
- **Phonological dyslexia** manifests as severe impairment in reading phonetic script (similar to alphabetic system), but preserved ability in reading pictographic script
- **Surface dyslexia** manifests as impairment in reading pictographic script (characters)

![](/docs/cogsci-c100/language/dis.png)

# Neurolinguistics

> **Neurolinguistics**: study of relationship between the brain and language
![](/docs/cogsci-c100/language/lig.png)

## Hemispheric Specialization

- Left hemisphere typically performs most language processing (95% for the right-handed; 50% for the left-handed)
- However, right hemisphere interprets a message’s emotional tone, decodes metaphors, and resolves ambiguities



## Aphasias

> **Aphasia**: difficulty in producing or comprehending speech caused by brain damage
- **Broca’s aphasia**, or expressive aphasia
{{< columns >}}<!-- mathjax fix -->
- Speech is meaningful, but halting, ungrammatical; function words (e.g., a, the, in, about) are omitted
    > "Buy bread store"
- Associated with damage to portion of left frontal lobe
- Recent research indicates area is also involved in resolving representational conflict (e.g., Stroop), processing mental imagery and music
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/language/areas.png)
{{< /columns >}}
- **Wernicke’s aphasia**, or fluent aphasia
    - Loss of ability to understand speech and to produce meaningful words; speech is fluent and grammatical but consists of empty words: word salad
        > "I called my mother on the television and did not understand the door. It was not too breakfast, but they came from far to near."
    - Wernicke patients do not appear to recognize that they cannot produce meaningful speech or understand others. As a result, they can become quite paranoid.
    - Associated with damage to part of left posterior superior temporal lobe
{{< figure  src="/docs/cogsci-c100/language/actv.png" >}}
- There are many different kinds of aphasia, associated with damage to different cortical areas
    - Some can speak but cannot read; others can read but cannot speak
    - Some can write but not read; others can read but not write
    - Some can read numbers but not letters
    - Some can sing but not speak
    - Language is complex and many different areas serve different language functions

# Bilingualism

> **Bilingualism**: ability to use two languages that differ
- If you’re fluent in two languages, your brain processes them in similar areas
- If you learned a second language after the first, you process them in different areas

## Disadvantages of bilingualism

- May pronounce some speech sounds slightly differently
- May take longer to make some language-processing decisions (Berken, Gracco, Chen et al., 2015)


## Advantages of bilingualism
- Early belief that bilingual education was "expensive, ineffective, and harmful"
    - Early study found that bilingual French-Canadians had lower IQ’s than monolingual English-Canadians, but turned out this was primarily due to fact that French-Canadian bilinguals came from a lower socio-economic class
- Bilinguals tend to acquire greater expertise in their native (first) language
- Bilinguals also show superior performance on measures of ability to follow instructions, as well as certain types of concept formation and problem solving tasks
    - Students in French immersion programs in Canada had higher aptitude scores not only in language but also in math than children with comparable abilities in control groups
- Bilingual education: children in "two-way" schools develop higher self-esteem, drop out less frequently and eventually attain higher levels of academic achievement and English proficiency
- A number of studies have indicated that lifelong use of two languages delays the onset of dementia by 4-5 years (Kim, Jeong, Nam et al, 2019)


# Language and Thought

> Be impeccable with your word: Speak with integrity. Say only what you mean. Avoid using the word to speak against yourself or to gossip about others. Use the power of your word in the direction of truth and love. -- Don Miguel Ruiz (The Four Agreements)

## Sapir-Whorf hypothesis
> **Sapir-Whorf hypothesis**: view that language determines thought
- Underlying assumption of use of affirmations in cognitive therapy
    - **Language and color**:
        - Natives in New Guinea who have words for two different shades of yellow more speedily perceive and better recall variations between the two yellows
        - Those who speak Russian, which has distinct names for various shades of blue, remember the blues better (Davidoff, Davies, & Roberson, 1999) (Winawer, Witthoft, Frank et al., 2007)
- People who are bilingual may think differently in different languages
    - Bilinguals reveal different personalities when taking the same personality test in their two languages (Chen & Bond, 2010)
        - China-born students at University of Waterloo were asked to describe themselves in English or Chinese
            - When describing themselves in English, they expressed mostly positive self-statements and moods
            - When responding in Chinese, they reported more agreement with Chinese values and roughly equal positive and negative self-statements and moods (Ross, Xun, & Wilson, 2002)
    - Bilinguals often switch languages, depending on which emotion they want to express (Chen, Kennedy, & Zhou, 2012)
    - When responding in their second language, bilingual people’s moral judgments reflect less emotion -- they respond with more "head" than "heart" (Costa, Foucart, Hayakawa et al., 2014)

# Animal’s use of language
> Can animals learn language?

## Chimpanzees

- Baby chimpanzee, Washoe, was taught American Sign Language
    - By age of five, she had learned more than 130 signs
- Other chimpanzees trained to use lexigrams (geometrical shapes displayed on a keyboard and linked to a computer) as words showed performances similar to Washoe
- In general, chimpanzees seem to be able to acquire a vocabulary and comprehension roughly equivalent to a 2-1/2- year-old child

## Gorillas

- Koko had a working vocabulary of over 1000 signs
- Understood approximately 2,000 words of spoken

## African grey parrot

- Alex -- a parrot with an "attitude" that apparently had an understanding of what he said
- Could correctly answer questions about an object’s shape, color, or material
