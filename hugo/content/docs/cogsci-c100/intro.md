---
title: "Introduction"
weight: 1
---

# Overview and Fields

- **Cognitive Science:** Study of the mind and cognition that integrates a number of different academic disciplines:
{{< columns >}}<!-- mathjax fix -->
  - Neuroscientists study the mind’s biological machinery
  - Psychologists directly study mental processes, such as perception, learning/memory, judgement and decision-making
  - Computer scientists explore how those processes can be simulated and modeled in computers
  - Philosophers ask critical questions about the nature of the mind -- what is mind? how does it interface with body? is is purely the brain?
  - Evolutionary biologists and anthropologists speculate about how the mind evolved
<---><!-- mathjax fix -->
![Processes](/docs/cogsci-c100/intro/areas.png)
{{< /columns >}}
- The job of cognitive science is to provide a framework for bringing all those perspectives on the mind together
- Each of the various academic disciplines that comprise cognitive science use different methods, examples:
    - _Philosophers_ look at where the unity of their discipline comes from
        - A commitment to **rigorous argument and analysis**
        - Particularly in the so-called analytic tradition-- the tradition most relevant to cognitive science
        - Certain problems that are standardly accepted as philosophical
    - In contrast, the unity of _psychology_ comes from a shared set of **experimental techniques** and paradigms
    - (Different branches of) _Neuroscience_ employ different tools appropriate to the level of organization at which they are studying the brain; These tools and techniques generally vary in...
        - **Spatial resolution** (y-axis): the scale on which they give precise measurement (varying scale: single neurons, e.x. light microscopy; to looking at parts of the brain in general -- which lobe/area is there activity?)
        - **Temporal resolution** (x-axis): time intervals to which they are sensitive (the frequency at which you make observations: EEG is very high, to where fMRI/PETS where the effects are measured over a longer scale)
        {{< figure  src="/docs/cogsci-c100/intro/neuro-chart.png" >}}
    - Cognitive Science includes the study of _anthropology_ and cultural differences
        - Conclusions derived from Western psychology experiments may not be very representative of humanity as a whole
        - Typical research participants tend to be **WEIRD:** Western, Educated, Industrialized, Rich, and Democratic

---

## Summary

> _Ideally, Cognitive Science would involve integration of these disparate methods:_
* Philosophers -- Deductive reasoning
* Psychologists -- Scientific method
* Cognitive psychologists -- Modeling
* AI researchers -- Computer models
* Neuroscientists -- Case studies, lesion methods, brain imaging
* Roboticists -- Build and test machines


# History of Cognitive Psychology/Cognitive Science

> _Cognition is mental activity – the acquisition, storage, transformation, and use of knowledge_

## Early History

- Attempts to understand mind go back at least to the ancient Greeks
    - Discovered laws of learning and memory, e.g., [method of loci](https://en.wikipedia.org/wiki/Method_of_loci) -- using imagery to enhance your memory capacity
    - Described human thinking in terms of mechanical _'manipulation of symbols'_
- Study of mind remained province of philosophy until 19th century
- In **1879**, Wundt established first psychology laboratory
    - One of few important dates (this is the birth date of psychology!)
    - Studied mental processes systematically using technique of _introspection_ 
        - Not what we would consider rigorous now adays
        - e.x. scientist would play a note on an instrument, then ask "how does this make you feel?"
- Within decades, however, experimental psychology became dominated by **behaviorism**-- a view that virtually denied the existence of the mind
    - Believe that psychology should study relation between **observable stimuli and observable behavioral responses**
    - **Mind** was banished from respectable scientific discussion -- you can't tell what's in that black box, so ignore it!
- However, in 1950’s, people started to become disenchanted with behaviorism (e.x. [Little Albert](https://en.wikipedia.org/wiki/Little_Albert_experiment)) + more experimental research was being done, so cognitive psychology began to emerge
    - Result of growth of interest in memory and developmental psychology, linguistics and computer science
        - [The Magical Number Seven, Plus or Minus Two](https://en.wikipedia.org/wiki/The_Magical_Number_Seven,_Plus_or_Minus_Two) -- proved you could study the mind experimentally. 
        - Discovered that people universally learned things at similar ages
    - View that mental processes can best be understood by comparison with a computer
        - A particular cognitive process can be represented by information flowing through a series of stages

## Development of Computational Model of Mind

- Alan Turing
    - In article published in 1936-37, conceived of information processing as an algorithmic or rule-based calculation process (Turing machine)
        > A Turing machine has a set of instructions (machine table) that determines what the machine will do when it encounters a particular symbol in a particular cell, depending upon which internal state it is in
    - Together with advances that were made in designing and building digital computers during and after World War II, this led to development of view that **cognition involves an algorithmic process of information processing**
- Parallel distributed processing (PDP) and connectionist models/**neural networks** became popular in 1990’s
    - That is, processing can happen parallel, simultaneously -- contrast with serial processing approach
    - Hold that cognitive processes operate in a parallel fashion 
        - e.x: face recognition -- cognitive processes can be completed even when supplied information is incomplete or faulty; your friend dyes their hair, but you still recognize them next time you see them.
- Research in AI and Machine Learning boomed in early 21st century due to growth in computing power and availability of large data sets
    - We knew how to do this way before, but didn't have the data sets nor computational power til now
- Classifications:
{{< columns >}}<!-- mathjax fix -->
  - **Artificial Intelligence (AI):** tries to design computer models that accomplish the same cognitive tasks that humans do
  - **Machine Learning:** a subset of AI that allows computers to "learn" (i.e. progressively improve performance on a specific task) by creating new algorithms to produce a desired output based on structured (or unstructured) data that is provided
      - Relies on labeled data set and human input to differentiate classifications (e.x telling the computer cats have pink noses while dogs have black, etc.)
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/intro/set.png)
  - **Deep Learning:** a subset of Machine Learning involving numerous layers of algorithms
      - Machine does not need to be provided with structured data -- doesn't required labeled data set, harder to do
{{< /columns >}}
  - **Neural Networks:** Networks of algorithms that are similar to the neural networks present in the human brain

## The Turn to the Brain in Cognitive Science
- Early models of cognitive functions, such as visual perception, focused on top-down analysis and included relatively little discussion of neural implementation -- not based on scientific method
{{< hint "info" >}}<!-- mathjax fix -->
{{< figure  src="/docs/cogsci-c100/intro/brain-methods.png" >}}
{{< columns >}}<!-- mathjax fix -->
Neuroimaging techniques that emerged in the 1980s and 1990s, such as PET and fMRI, allowed neuroscientists to begin establishing large-scale correlations between types of cognitive functioning and specific brain areas
<---><!-- mathjax fix -->
Other techniques, such as single-cell recordings, have made it possible to study brain activity in nonhuman animals at the level of the single neuron
{{< /columns >}}
{{< /hint >}}

### The Cerebral Cortex

{{< hint "warning" >}}<!-- mathjax fix -->
This will be on the exam!
{{< /hint >}}


{{< columns >}}<!-- mathjax fix -->
![Brain](/docs/cogsci-c100/intro/cerebral.png)
<---><!-- mathjax fix -->
- **Frontal lobes:** involved in __speaking & muscle movements__ and in __making plans & judgments__ -- directly proportional to social network
- **Parietal lobes:** include the sensory cortex, important in __spatial navigation__
- **Occipital lobes:** include the __visual areas__, which receive visual information from the opposite visual field
{{< /columns >}}
- **Temporal lobes:** include the __auditory areas__ and mystical (out of body) experiences
- **Motor cortex:** area at the rear of the frontal lobes that controls __voluntary movements__
- **Sensory cortex:** area at the front of the parietal lobes that __registers & processes body sensations__


{{< columns >}}<!-- mathjax fix -->
### Limbic System

- **Limbic cortex:** phylogenetically older part of cortex
- **Amygdala:** Two almond-shaped neural clusters that are components of the limbic system and are linked to __emotion__, particularly fear and aggression
- **Hippocampus:** Donut-shaped structure that is important in __memory__
<---><!-- mathjax fix -->
![Brain](/docs/cogsci-c100/intro/limbic.png)
{{< /columns >}}

### Are our behaviors determined by brain function?

> Or, is brain function determined by our behaviors? (Which came first-- the chicken or the egg?)

- Physiological correlates can almost always be found for psychological states
    - If we haven't figured it out yet, we probably will very soon
- Penfield found that stimulating various parts of the brain with electrodes give rise to specific thoughts, emotions, images, or motor movements
    - Done on epilepsy patients in preparation for surgery (so they didn't remove any parts that were crucial)
    - Abnormal EEG patterns seen in those with schizophrenia, depression, obsessive-compulsive disorder (OCD), and attention deficit-hyperactivity disorder (ADHD)
    - **However, this does not necessarily mean that brain states cause mental states!**
        - e.x. psychotherapy and drug therapy produce similar types of brain changes (e.g., in studies of treatment of depression, OCD, and ADHD)
        - Recalling sad memories makes your brain temporarily look like the brain of someone with depression
        - Psychotherapy (talk therapy) produces the same brain state that meditation does

### Controversies in CogSci

> Do the benefits of cognitive neuroscience justify the costs?

- Neuroimaging studies can be quite outrageously expensive, and many of these studies do not provide direct practical benefits
    - To run an hour PET on someone, it costs $20-30k per subject and you need many subjects for research
- Some researchers claim that cognitive neuroscience has not really helped to develop psychological theories -- people are just wowed by pictures of brains


## Limitations of the experimental method

{{< columns >}}<!-- mathjax fix -->
- Artificiality of experiments (lack of ecological validity -- doesn't apply to real-world scenarios): the more you control the environment, the less like real life it becomes
- Argument that the best things in life (e.g., love, beauty, truth, joy) cannot be quantified
<---><!-- mathjax fix -->
> There was an awful rainbow once in heaven:<br>
> We know her woof, her texture; she is given<br>
> In the dull catalogue of common things.<br>
> Philosophy will clip an Angel’s wings.

--[John Keats](https://en.wikipedia.org/wiki/John_Keats)
{{< /columns >}}
- Belief as a confounding variable: [Magellan’s diary](https://www.northcoastjournal.com/humboldt/myth-of-the-invisible-ships/Content?oid=2129921)
    - When Magellan interacted with native people, they could not see (perceive) his large ships
    - The idea is that the ships were so alien to their experience that "... their highly filtered perceptions couldn't register what was happening, and they literally failed to 'see' the ships." (JZ Knight, What the Bleep Do We Know?)
    - **Certain things have to be believed until they can be seen**


## SQ3R technique

- Steps:
    1. **Survey:** Scan material; Read headings, figures, summaries
    2. **Question:** Pose questions to yourself
    3. **Read:** Look for answers to questions as you read; Read actively, not word-by-word (key to speed-reading!)
    4. **Recite:** Practice rehearsal (tell someone about the material)
    5. **Review:** Go over answers to questions; Review material again a day or several days later
- Fallacies:
    - You have to read every word.
    - The slower you read, the higher your comprehension.
    - It’s a 'sin' to skip around when you are reading.

