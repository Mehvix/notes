---
title: "16: Cognition & Therapy"
weight: 16
---

# Use of AI in diagnosis and treatment of psychological disorders

## Expert Systems

> Expert systems programs are typically applied in narrowly defined domains to solve very determinate problems, such as diagnosing specific medical disorders

- MYCIN
    - Early expert system developed in 1970s to diagnose infectious diseases
    - Used knowledge base of about 600 heuristic rules about infectious diseases derived from clinical experts and textbooks
    - Accuracy rate of 69%, which turned out to be significantly higher than diagnoses by infectious disease experts
- Are expert systems now able to accurately diagnose psychological disorders?
    - Deep learning (a subtype of machine learning that we discussed earlier, remember?) has been used to integrate data obtained from multiple imaging modalities, such as fMRI, MRI, and PET, to effectively classify some psychological disorders
    - Most studies have focused on diagnosis of neurocognitive disorders and ADHD, probably due to accessibility of large publicly available neuroimaging data sets
    - Accuracy rates above 90% have been achieved in some studies
    - A few of these studies were also able to accurately predict disease trajectory
    - Studies classifying other mental disorders, including schizophrenia, autism, Parkinson’s, depression, substance abuse, and epilepsy, are also accumulating (Durstewitz, Koppe, and Meyer-Lindenberg, 2019)
- In addition, we’re nearing the point where we may be able to tailor treatment for psychological disorders based on neuroimaging data
    - People whose depression improved most after behavioral activation therapy had greater brain network connectivity between the anterior insular cortex (involved in assigning importance to events) and the middle temporal gyrus (involved in subjective experience of emotion)
    - Differences in brain structure and neural connectivity among different regions predicted how well CBT reduced symptoms of those with social anxiety disorder
        * Estimates of treatment outcome were five times more accurate than estimates using a behavioral assessment tool alone (Whitfield-Gabrieli, Ghosh, Nieto-Castanon et al., 2015)
    - In one study, participants with social anxiety disorder were asked to identify letters behind which occasionally lurked pictures of angry faces
        * Those who struggled most to avoid being distracted by the threatening stimuli—indicated by more activity in dorsal anterior cingulate cortex— showed the most symptom improvement when treated with CBT (Crowther, Smoski, Minkel et al., 2016) (Klumpp, Fitzgerald, Piejko et al, 2015)

## Network Neuroscience

- There has been a shift in recent years to studying networks or **functional connectivity**, that is, how different brain regions work together, rather than just brain regions themselves
- Traditional localizationist research almost always involves watching how brain activity changes while a person is engaged in a particular task
- Network research, in contrast, can be done when people are doing nothing at all
    - This gets closer to a person’s natural state
        * Ex: Someone with a psychological disorder will have the disorder even when they are not doing a working memory task
- The network approach has proven to be particularly well suited to understanding schizophrenia
{{< columns >}}<!-- mathjax fix -->
- Healthy human brains are generally small-world networks
    - Most nodes make only short-range connections to one another and tend to be clustered into densely connected modules
    - At least one node in each module, however, is a hub, which means that it makes long-range connections all over the network
- Researchers found that the brain of a person with schizophrenia tends to be measurably less of a small-world network
    - It still tends to be organized into modules, but those modules aren’t as densely connected (Liu, Lian, Zhou et al., 2008; Lynall, Bassett, Kerwin et al., 2010)
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/therapy/network.png)
{{< /columns >}}

### Frontoparietal network

- People with **major depressive disorder** tend to show
    - Reduced connectivity between regions in the frontoparietal network (FN), which is involved in cognitive control of attention and emotional regulation
    - Reduced connectivity between frontoparietal systems and parietal regions of dorsal attention network involved in attending to the external environment
    - Increased connectivity in the default network (DN), which is believed to support internally-oriented and self-referential thought, such as rumination
{{< columns >}}<!-- mathjax fix -->
* Above pattern may reflect deficits in emotional regulation and depressive biases toward ruminative thoughts at cost of attending to external world (Kaiser, Andrews-Hann, Wager et al., 2015)
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/therapy/dn.png)
Frontoparietal network (left), Default network (right)
{{< /columns >}}
- Patients experiencing **hallucinations** often have lesions in different parts of the brain, but in each case, the lesion was tightly associated with the extrastriate visual cortex
    * Symptoms often correlate with damage to a specific circuit, not a specific location (Boes, Prasad, Liu, 2015)

### Other important applications of network neuroscience:

- Networks can be used not just for diagnosis, but to identify PTSD patients who are unlikely to respond to psychotherapy
- If scientists can determine the circuits that a highly invasive technique like deep brain stimulation (DBS) is acting upon, they might be able to achieve similar results with a nonsurgical approach like TMS
{{< columns >}}<!-- mathjax fix -->
- Clinicians can access regions buried in the brain, like those targeted in DBS treatments for Parkinson’s, through areas closer to the surface (Etkin, Maron-Katz, Wu et al., 2019) (Michael Fox, neurologist at Harvard Medical School)
- Also, it might be that the best way to help a symptom that maps to a circuit is actually multiple electrodes, or multiple stimulation sites
    - Tumor problem
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/therapy/yell.png)
{{< /columns >}}

# Effects of Trauma on Cognition and Emotion

## The Neurobiology of Trauma

- Some psychologist have claimed that most, if not all, psychological disturbances are the result of trauma
- High rates of co-morbidity of PTSD with other psychological disorders
    - 58% of patients with depression; 54% with borderline personality disorder; 40% with bipolar disorder; 28% with schizophrenia
    - 58% of people with migraines experienced abuse as children
- Neurologically, the experience of trauma is characterized by:
    - State of hyperarousal
    - Dissociation

### Hyperarousal

{{< columns >}}<!-- mathjax fix -->
- PTSD is associated with hypersensitization of amygdala circuitry/HPA-axis
- PTSD is associated with oversecretion by hypothalamus of corticotropin-releasing hormone (CRH), the main stress hormone used to mobilize emergency fight-or-flight response
- The greater the degree of arousal during and immediately after a traumatic incident, the more likely it is that person will have PTSD or other neuropsychiatric symptoms following trauma
    * Symptoms less severe if patient is treated quickly after trauma (e.g., with propranolol)
* Neural changes of PTSD make a person more susceptible to further traumatizing: exposure to even mild stress when young makes person more vulnerable to trauma-induced brain changes later in life
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/therapy/pers.png)
![](/docs/cogsci-c100/therapy/brn.png)
{{< /columns >}}

### The role of glucocorticoids

![](/docs/cogsci-c100/therapy/glucocorticoids.png)

- A 20% reduction in volume of hippocampal formation has been found in combat veterans and those subjected to severe abuse in childhood
    - The hippocampus contains large numbers of glucocorticoid receptors and plays a key role in regulating production of glucocorticoids through negative feedback
- People who were abused as children have more methyl groups capping the genes for glucocorticoid receptors -- this prevents the cell from reading its DNA and is correlated with suicide risk
- PTSD is associated with low levels of glucocorticoids
    - Excessively low, as well as excessively high, levels of glucocorticoids can cause dysfunction
    - In general, glucocorticoids increase the stress response, but a certain amount of glucocorticoid is also necessary to turn off the stress response

### Sensitivity to Context

{{< columns >}}<!-- mathjax fix -->
- How good you are at taking into account the context in which you find yourself in regulating your emotional responses
    - Measures how attuned you are to the social environment, e.g., when a behavior might be socially acceptable vs. offensive
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/therapy/hippo.png)
{{< /columns >}}
- Associated with
    - Differences in hippocampal volume, particularly **anterior hippocampus** -- the part closest to the amygdala -- as well as strength of connections between hippocampus and other brain regions, especially the prefrontal
        - As mentioned, PTSD is associated with loss of hippocampal volume
    - In particular, the anterior hippocampus is involved in regulating **behavioral inhibition** in response to different contexts
        - The anxiety and even terror that people with PTSD feel is quite appropriate in certain contexts, such as a battleground
        - The problem is that they experience these feelings in nontraumatic contexts, such as if they hear pounding from a construction site
        - Both human toddlers and monkeys tend to freeze when they encounter an unfamiliar situation, a form of anxiety called behavioral inhibition

### Dissociative aspect of trauma

{{< columns >}}<!-- mathjax fix -->
- Little or no connections forms between the **neocortex and memory storage and emotional centers** (e.g., amygdala)
- In addition, PTSD is associated with overactivation of brain’s opioid system: this may cause a numbing of feelings, a sense of being cut off from life or from concern about others’ feelings
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/therapy/neo.png)
{{< /columns >}}

### Psychotherapy

>- Help patient understand that jumpiness and nightmares, hypervigilance and panics, are part of symptoms of PTSD -- this makes the symptoms themselves less frightening
>- Help patient regain some sense of control over what is happening to them (security measures)
>- Aid patient in mourning any loss that may have been brought on by the trauma
- Have patient retell and reconstruct the story of the trauma in an environment of safety (play therapy may be used with children)
    - Patient should be encouraged to retell the traumatic events as vividly as possible, retrieving every detail -- their emotional reactions as well as the events themselves
    - The goal is to put the entire memory into words to capture parts that may have been dissociated from conscious recall
        - By putting sensory details and feelings into words, memories are brought more under control of the neocortex, where the reactions they kindle can be rendered more manageable (Siegel, D., 2001)
    - Also, retelling the story in a surrounding of safety and security, in the company of a trusted therapist, enables a sense of security, rather than terror, to be experienced in connection with the trauma memories
- May need to focus more on Cognitive Behavior Therapy, relaxation techniques, or physical exercise initially, especially in cases of severe trauma

## Treatment of PTSD

- Recent Research suggests that it is the element of helplessness that makes a given event subjectively overwhelming
    - It’s the feeling that your life is in danger and there is nothing you can do to escape it -- that’s the moment the brain change begins
- Theory that trauma experience entails a tremendous urge to take action (fight or flight), at the same time that one is paralyzed by sense off helplessness
    * A number of newly developed therapies (bioenergetics, sensorimotor psychotherapy, etc.) thus focus on physical selfexpression as way to foster emotional release and heal trauma
- Therapeutic effects of emotional release through journaling -- Pennebacker study: undergraduates were told to write for 20 minutes each day for five days either about the most traumatic and stressful event of their life or about a trivial topic
    - Students who wrote about the traumatic event were more upset immediately following writing the essays and showed elevated blood pressure compared to those who wrote about trivial topics
    - However, over the following six months, they were significantly less likely to visit the student health service for illness and showed improved immune function
    - Greatest improvement shown by those who expressed both positive and negative emotions and who were able to weave a narrative and find meaning in the experience

# Cognition and emotion in therapy

{{< columns >}}<!-- mathjax fix -->
> **Psychodynamic therapy**: Focuses on helping patient gain cognitive insight into unconscious roots of problem (e.g., early childhood experiences)
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/therapy/beers.png)
{{< /columns >}}
- Tracing roots of negative thoughts and behaviors to allow you to see that they are based on beliefs that you simply picked up and not necessarily Truth with a capital T
- Based on view that the reason negative emotional patterns are so difficult to change is that they are not just established through conditioning, but are deeply interwoven into the way we try to gain love
    > "See, Mommy/Daddy, I’m not any better than you are. Now will you love me?"
    > "See, Mommy/Daddy, I’m a worthless guttersnipe just like you said I was. Now will you love me?
- Even when we rebel, we stay trapped in the same negative patterns
    - Ex: Woman with sexually repressive parents




- So how to release negative emotional patterns?
    - Become more aware of patterns of parental figures that you might have adopted
    - In addition, **transference** can be used to gain greater awareness of those negative patterns
{{< columns >}}<!-- mathjax fix -->
- Transference has to do with the way in which we internalize our parents and project them onto other people
- Ex: over-reacting to criticism/authority because that was the way our parent acted, and it made us feel worthless, powerless, not good enough, etc.
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/therapy/fere.png)
{{< /columns >}}


## Psychodynamic-Based Writing Exercise

- Writing exercise to help clients become aware of negative emotional patterns they have picked up from parents and to "reclaim their power"
    - What were your parents like during your childhood (personality, behavior)?
    - What forms of punishment did your parents use?
    - Describe a childhood scene in which you were angry with your parents
    - Describe a childhood scene in which you were hurt, rejected, and/or sad due to your Mother or Father in the first person present tense
* Follow-up visualization exercise:
    - What was it like for each of your parents growing up in their family? How did they feel? How were they punished?
> If we could read the secret history of our enemies, we should find in each man's life sorrow and suffering enough to disarm all hostility. -- Longfellow

## Client-centered Therapy

{{< columns >}}<!-- mathjax fix -->
- **Client-centered therapy**: therapist provides unconditional positive regard so client can feel free to express their inner thoughts and emotions and be themselves
    - This involves validating their emotional experience to strengthen their sense of identity -- not parroting their beliefs! "Just remember, son, it doesn’t matter whether you win or lose -- unless you want Daddy’s love."
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/therapy/cct.png)
{{< /columns >}}

![](/docs/cogsci-c100/therapy/cct2.png)

{{< columns >}}<!-- mathjax fix -->
- **Mirroring**: therapist’s reflecting back to the client an understanding of his inner state, leading patient to feel acknowledged and understood
    - This is not merely a matter of listening sympathetically and parroting the client!
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/therapy/bord.png)
{{< /columns >}}

## Emotionally Focused Therapy (EFT)

- It emphasizes "listening with the heart": meaning listening not for the literal meaning of a partner's words, but for the feelings that lie beneath their words
- **EFT is grounded in attachment theory**: it focuses on one’s need for security and one’s sense of dependency on one’s partner; it legitimates vulnerability
- Based on the premise that there is almost always a soft emotion behind a hard emotion, and that if that soft emotion can be accessed and then accepted by the partner, it almost always dissolves the conflict

## Cognitive Behavior Therapy

> **Cognitive Behavioral Therapy (CBT)**: changing negative emotions by identifying and challenging associated negative thoughts
- Aims to help one develop cognitive awareness -- the ability to see thoughts as simply thoughts, rather than the "Truth"
    - Ex: Woman with severe depression who thinks she will die if her husband leaves her
        * Therapist challenges this belief by reminding her that she was able to function very well before she married
    - Ex: Children with depression learn to tune into their thoughts when facing tough situations and to imagine alternatives to negative thought

---

- Ex: Client with Obsessive-Compulsive Disorder (OCD) is taught to:
    1. **Relabel:** identify what’s real and what isn’t and refuse to be misled by obsessive thoughts
        > "That compulsion is bothering me again," rather than "I feel like I need to wash my hands again"
    2. **Reattribute:** you understand that those thoughts and urges are merely false messages being sent from your brain
        > "That compulsion is bothering me because I have a medical condition called OCD that is related to a biochemical imbalance in my brain"
    3. **Refocus:** turn your attention to more constructive behavior, knowing that by doing so, you are actually changing the way your brain works in an extremely healthy and wholesome way
        > "Passing mental states become lasting neural traits"
    4. **Revalue:** you come to see compulsions and obsessive thoughts as the useless garbage they really are as soon as they arise

---

{{< columns >}}<!-- mathjax fix -->
> **Variant**: mindfulness: bringing emotions to cognitive behavior therapy
   - Thoughts and emotions are inextricably linked, but in mindfulness, you use emotions to guide your thoughts, rather than using thoughts to guide your emotions as in standard CBT
   - View that emotions are a foolproof guidance system telling you whether you are thinking a thought that is in line with your own best interests
- How does it feel when you criticize someone? How does it feel when you are praising someone or something out of a genuine sense of appreciation?
* Becoming more aware of the "feeling tone" behind thoughts makes it much easier to choose the positive thoughts and let go of the negative
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/therapy/nav.png)
![](/docs/cogsci-c100/therapy/vibe.png)
{{< /columns >}}


- One way to become more aware of the feeling tone behind thoughts is to reach for the "best feeling thought" that one can access at any given moment (on a deep, not superficial level, of course!)
    - It’s about becoming more aware of your emotions and giving yourself permission to feel good/prioritizing feeling good:
        > "Nothing is more important than that I feel good."

        {{< columns >}}<!-- mathjax fix -->
- This also means focusing more on how you feel and less on what other people may think
    > "Mental health is getting to the point where you don’t give a rip what anyone else thinks or says or does."
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/therapy/good.png)
{{< /columns >}}

### Mindfulness

> **Dialectical behavioral therapy (DBT)**: Variant of mindfulness therapy originally developed by Marsha Linehan to treat people with borderline personality disorder
- Combines standard cognitive-behavioral techniques for emotion regulation and reality-testing with concepts of distress tolerance, acceptance, and mindful awareness derived from Buddhist mediation practice
- DBT involves several different "dialectics" or oppositions, including:
    - Acceptance and openness to change
        - Therapist aims to accept and validate the client’s feelings at any given time while also informing the client that some feelings and behaviors are maladaptive, and showing them better alternatives
            > "Each of you is perfect the way you are ... and you can use a little improvement." -- S. Suzuki
    - You don’t have to like it -- you may not want to change, but you need to change in order to get what you want
- First therapy that has been empirically demonstrated to be effective in treating borderline personality disorder; also used to treat spectrum mood disorders, including self-injury
- Clients are taught to practice mindfulness to enhance distress tolerance
    - DBT focuses on helping clients to recognize and accept in a non-judgmental way negative situations and emotions, rather than becoming overwhelmed or hiding from them
- Includes many innovative techniques
    * Once clients become aware of negative emotional state, they can then effect a repair by engaging in some activity they enjoy, forcing themselves to think about something else, or doing something that has an intense feeling, e.g., taking a hot shower, snapping a rubber band against their wrist, or holding ice in their hand when they feel the urge to cut
- Therapy also incorporates boundary setting, e.g., client has option of calling therapist but only before they cut

### Affirmations


- In CBT, visualization is often used in conjunction with **affirmations**
{{< columns >}}<!-- mathjax fix -->
- **Examples**:
    > "I am full of radiant health and energy."
    > "Infinite riches are freely flowing into my life."
    > "The world is a safe and friendly place."
    > "I always communicate easily and effectively."
    > "Everything good is coming to me easily and effortlessly."
- **Basic rules**:
    1. Phrase affirmations in the present tense, not the future
    2. Phrase affirmations in the most positive way you can
        - e.g., don’t say, "I no longer oversleep in the morning," but rather "I now wake up on time and full of energy every morning."
    3. Keep it short and simple!
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/therapy/aff.png)
{{< /columns >}}

### Focus of attention

- **How to "win friends and influence people"**: shifting one’s focus of attention
- Research on CBT has shown that one of the most effective way to change another person’s behavior is to shift our focus of attention
    - More specifically, the trick is to accentuate the positive and ignore the negative
    - This is the basis of behavioral therapy, which is empirically validated to work on children and animals, as well as adults
        - [What Shamu Taught Me about a Happy Marriage](https://www.nytimes.com/2019/10/11/style/modern-love-what-shamu-taught-me-happy-marriage.html)

### Applying Principles of CBT

- Use what trainers call "approximations," rewarding small steps toward learning a new behavior
    - Behavior: husband leaves dirty clothes all over floor
    - Response: Thank him if he throws one dirty shirt into the hamper; if he throws in two, kiss him; step over soiled clothes on the floor without any sharp word
* Devise incompatible behaviors
    - Behavior: Husband has habit of hovering over you when you cook
    - Response: Pile up parsley for him to chop or cheese to grate at other end of kitchen island or set out bowl of chips and dip across the room
* Use least reinforcing syndrome (L.R.S.): any response, positive or negative, will fuel a behavior; if a behavior provokes no response, it typically dies away
    - Behavior: husband habitually loses keys and tears around in panic searching
    - Response: Ignore behavior, keep doing what you are doing
* Adopt animal trainers’ motto: "It’s never the animal’s fault"
    * You just need to brainstorm new strategies when your "puppy" misbehaves

### Positive aspects

- **Listing positive aspects**: practicing "seeing others as if the good in them were all of them"
    - Sister Mrosla story of "listing positive attributes" exercise in her ninth grade classroom
    ![](/docs/cogsci-c100/therapy/class.png)
* **CBT and mindfulness are methods of engaging in self-directed neuroplasticity: changing our mind to change our brain**

