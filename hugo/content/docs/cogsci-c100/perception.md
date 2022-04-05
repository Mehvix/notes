---
title: "2: Perception"
weight: 2
---

# Definition of sensation and perception

- As humans, we are cognitive beings who...
    - **Acquire** information about the world around us (perception)
    - **Integrate** that information with prior knowledge from our stored memory
    - **Store** that knowledge in our memory so we can use it later to help us achieve our goals
- First step in this process of acquiring knowledge about the world involves sensation and perception
    - **Sensation:** process by which our sensory receptors and nervous system receive stimulus energies from the environment and transduce them into **neural impulses** (transduction). The inherent stimuli. Objective
    - **Perception:** process of _interpreting_ and _organizing_ sensory information through use of previous knowledge. What gives stimuli meaning. Subjective.

# Early models of object perception

- Lots of machines are built on these old theories
- The models aren't respected nowadays, but had useful tid-bits of information (for cogsci, ML, etc)

## Template matching model


{{< columns >}}<!-- mathjax fix -->
- **Template matching model:** object perception involves a comparison of the stimulus with set of templates or specific patterns stored in memory
- Static, unchanging
- _Problem:_ cannot account for complexity and flexibility of object recognition
    - e.g. individual differences in handwriting
<---><!-- mathjax fix -->
![Template](/docs/cogsci-c100/perception/template.png)
{{< /columns >}}

## Feature analysis model

- Feature-analysis model: discrimination of objects is based on _small number of distinct characteristics_ of stimuli
    - Are these two the same letter?: `G M`  `P R`
        - People are faster at deciding whether `G` and `M` are different than `P` and `R` because there are fewer similarities
    - Supported by neurological evidence: some neurons respond only to horizontal lines, others to diagonals, etc.
- _Problem:_ Cannot explain recognition of complex objects with features that move and distort (e.g., horse or kangaroo)
    ![](/docs/cogsci-c100/perception/roo.png)

## Recognition-by-components model

![](/docs/cogsci-c100/perception/geons.png)
{{< columns >}}<!-- mathjax fix -->
- **Recognition-by-components model:** view that an object is represented as an arrangement of simple 3-D shapes called [_geons_](https://en.wikipedia.org/wiki/Geon_(psychology))
- Six main geons above
>![](/docs/cogsci-c100/perception/cup.png)
> Cup/pail composed of cylinder and curved tube geons in a particular arrangement
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/perception/rbc-ex.png)
> Easier to tell the object from the rightmost column versus the center, despite the latter containing more lines
{{< /columns >}}

## David Marr’s Model of Visual Processing
{{< columns >}}<!-- mathjax fix -->
> Not on Exam
- The image is then transformed into a 3-D sketch in which the the axes of symmetry and elongation link the object parts
    - **Symmetry axis:**  line that divides an object into mirror image halves
    - **Elongation axis:** line defining direction along which main bulk or mass of a shape is distributed
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/perception/marr.gif)
{{< /columns >}}
- The 3-D sketch is object-centered – the object’s parts are described relative to one another and are linked on the basis of shared properties and axes
    - This solves the object constancy problem, allowing recognition of an object presented in different orientations and under different conditions, e.g., lighting changes


## Prototype model

- **Prototype model:** object perception involves a comparison of the stimulus with ideal, abstract example
    - People are faster at identifying sparrow as a bird than penguin
- One of the most famous models in all of cognitive psychology (and developed at Berkeley!)
- It has been hypothesized that our sensory systems act primarily as a **selective filtering mechanism**
    - Prototypes more easily pass this filter
    - This filter sorts things according to a limited number of variables (e.g., warm, unpleasant, green) out of which we construct our world
    - But prototype theory suggests that our minds can also perceive objects in a very different way...
    > _That which is essential is invisible to the eye._ – de Saint-Exupery

## Alternative modes of perception

{{< columns >}}<!-- mathjax fix -->
- **Alternative modes of perception:** Mindfulness is largely about seeing the “suchness” of things, that is, seeing things directly without conceptual filters
- What assumptions might you make about this woman if you were told she is from New England? from California?
    - Our preconceived notions prevent us from seeing the real person in front of us
    - Stereotyping
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/perception/women.png)
{{< /columns >}}


> _If the doors of perception were cleansed, everything would appear to man as it is, infinite._<br>
>
> _To see a World in a Grain of Sand,_ <br>
> _And a Heaven in a Wildflower,_ <br>
> _Hold Infinity in the palm of your hand,_ <br>
> _And Eternity in an hour._     -- Blake

## Neural Networks

> On Quiz 2!

- Artificial Neural Networks in Pattern Recognition
- Human neurons
{{< columns >}}<!-- mathjax fix -->
![](/docs/cogsci-c100/perception/syn.png)
<---><!-- mathjax fix -->
- Many different neurons connect to the dendrites of each neuron
    - Some produce excitatory effect; others produce inhibitory effect
    - There are also different levels of intensity of these effects
- Around a thousand connections are connected to each neurons
    - If the activation of the neuron reaches a certain minimum threshold, the neuron will fire
{{< /columns >}}

{{< details "16A Notes" >}}
>  Because circuit analysis translates to a wide range of fields, we can model many physical systems as electrical circuits, often gaining insight about the system. You may have heard of neural networks, an important machine learning tool that can be used to “learn” tasks such as image and voice recognition from examples instead of explicit programming. Neural networks are modeled after biological neural networks, which are fundamentally circuits operating on electrical signals within a brain:
> {{< figure  src="/docs/cogsci-c100/perception/16A.png" >}}
> In a general sense, studying circuits provides you with the conceptual and mathematical tools needed to analyze such networks. More broadly, circuit concepts are relevant to understanding network analysis and signal flows in systems, which can be applied to areas ranging from transportation analysis to social network analysis. ([from EECS16A Note0](https://eecs16a.org/lecture/Note0.pdf))
{{< /details >}}


{{< columns >}}<!-- mathjax fix -->
- Artificial neural networks (ANN)
    - The nodes or neurons are organized into layers in much the same way that human neural networks are
    - The **weights** attached to the connections between pairs of units in adjacent layers determine the overall behavior of the network
        - This is similar to the way in which _excitatory_ and _inhibitory_ neurons of various strengths connect to a particular neuron in human neural networks
    - The **bias term** indicates what the weighted sum needs to be before the node/neuron will activate
        - This is similar to the threshold necessary for activation of a neuron in human neural networks
<---><!-- mathjax fix -->
>![](/docs/cogsci-c100/perception/AANw.png)
> An artificial neural network is an interconnected group of nodes, inspired by a simplification of neurons in a brain. Here, each circular node represents an [artificial neuron](https://en.wikipedia.org/wiki/Artificial_neuron) and an arrow represents a connection from the output of one artificial neuron to the input of another.
{{< /columns >}}


### Ex: How might a computer recognize a “9” using neural networks?

{{< youtube "aircAruvnKk" >}}
- There is huge variety of ways in which people write 9’s
- To simplify things, we can represent the “9” by decomposing it to a grid of 28 x 28 pixels of varying shades of gray (between 0 and 1)

1. First (input) layer of network
{{< columns >}}<!-- mathjax fix -->
- Starts with bunch of neurons or nodes corresponding to an array of 28 x 28 pixels in the image
- Each node holds a number that represents the grayscale value of the corresponding pixel, ranging from 0 for black to 1 for white
- This is the neuron’s activation level
- Activations in one layer bring about activations in the next layer, which in turn bring about activations in the next layer...
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/perception/s1.png)
{{< /columns >}}
    - This is loosely analogous to how, in biological networks of neuron, some groups of neurons cause other neurons to fire
2. Second layer (or first “hidden layer”)
   - Each neuron in the second layer might pick up on whether there is an edge in one particular region
   - You assign a weight to each one of the connections between a particular neuron in the second layer and the neurons in the first layer
   - Then you take all the activations from the first layer and compute their weighted sum according to the weights
    {{< columns >}}<!-- mathjax fix -->
- Could make the weights associated with almost all of the pixels 0 except for some positive weights in target region
- To really pick up on whether there is an edge here, could also have some negative weights associated with the surrounding pixels
    - Sum is largest when those middle pixels are bright but surrounding pixels are darker
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/perception/s2.png)
{{< /columns >}}
{{< columns >}}<!-- mathjax fix -->
- But maybe you don’t want the neuron to light up anytime the sum is bigger than zero -- maybe you only want it to be active when the sum is bigger than say 10
- So you add in some other number (the bias), like -10, to the weighted sum
    - The bias tells you how high the weighted sum needs to be before the neuron starts getting meaningfully active
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/perception/s3.png)
{{< /columns >}}
    - The connections between the other layers also have weights and biases associated with them
3. Third layer (or second “hidden layer”)
    - When we recognize digits, we piece together various components
        - e.x: A “9” has a loop near the top and a line on the right whereas an “8” has a loop on the top and one below
    {{< columns >}}<!-- mathjax fix -->
- Each neuron in the third layer corresponds to one of these subcomponents
   - e.x: A particular neuron in the third layer might be activated by any generally loopy pattern toward the top
- These subcomponents are made up of the various edges from the second layer
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/perception/s4.png)
{{< /columns >}}
4. Last (output) layer
{{< columns >}}<!-- mathjax fix -->
- Has 10 neurons, each representing one of the digits
- The activation in these neurons – some number between 0 and 1 – represents how much the system thinks a given image corresponds with a given digit
- Learning is about getting the computer to find a setting for all of the different weights and biases so that it will actually solve the problem at hand
   - This is done through [**backpropagation**](https://en.wikipedia.org/wiki/Backpropagation)
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/perception/s5.png)
{{< /columns >}}

### Learning in Neural Nets: Backpropagation

- ANNs can compute any function that can be computed by a digital computer
    - However, it was not until the emergence of backpropagation learning algorithm that it became possible to train multilayer neural networks
- The strength or weight of the connections between neurons in adjacent layers varies: neural networks learn by modifying these weights
    - Learning algorithms that are programmed into the ANN change the weights of the connections between pairs of neurons in adjacent layers in order to reduce the “mistakes” that the network makes
    - The basic idea is that each hidden unit connected to an output unit bears a degree of “responsibility” for the error of that output unit
    - If the activation level of an output unit is too low, then the weight between the output unit and each hidden unit connected to it is increased to decrease the error
    - The network then assigns error levels to the next layer of hidden units, so the error is propagated back down through the network until the input layer is reached
- **tl;dr:** neural networks have to 'learn' by adjusting stimuli weights. When a network gets an answer wrong, it has to recursively pop back each layer and adjust the corresponding weights (increasing correct value weights, decreasing activated incorrect value weights)

### Other Neural Networks Q&A

{{< columns >}}<!-- mathjax fix -->
**Q:** How many neurons should there be in each hidden layer?<br>
**A:** There are a number of empirically-derived rules-of-thumb.  Of these, the most commonly relied on is “the optimal size of the hidden layer is usually between the size of the input and size of the output layers”
<---><!-- mathjax fix -->
**Q:** How many hidden layers are needed?  Are more layers better?<br>
**A:** No.  Situations in which performance improves with additional hidden layers are very few.  One hidden layer is sufficient most of the time.
<---><!-- mathjax fix -->
**Q:** Why are more hidden layers not necessarily better?<br>
**A:** Increasing the number of hidden layers much more than the sufficient number will cause the network to **overfit** the training set. It will learn the training data, but it won’t be able to generalize to new unseen data.
{{< /columns >}}

> Overfit Dataset:
>{{< figure  src="/docs/cogsci-c100/perception/fits.png" >}}


# Top-down processing in object recognition

- Limitations of models of object perception discussed above: assumes, in theory, perception is _objective_ and _accurate_; in real life, that is often not the case...
    - What we perceive, the way we perceive, is not always what would be predicted by these models
    - Our **concepts, expectations, and beliefs** play a much bigger role in perception than we usually realize
- Perception engages both top-down and bottom-up processing
    - **Bottom-up processing:** analysis of information coming from stimuli through sensory receptors
        - Object perception as combination of stimulus information from sensory receptors
        - Emphasizes the importance of information coming from the outside world
    - **Top-down processing:** information processing guided by higher-level processes, such as our beliefs, expectations, and memories
        - Our knowledge, beliefs about the world inform our perceptions
        - Emphasizes the importance of information coming from our minds
    - Note: we use both throughout everyday situations, rarely exclusively either or
        - Models can almost be sort of categorized/grouped by which of the two processing model they put emphasis on
    - E.x. you see a water bottle on your desk
        - You know it's a water bottle since it's physically there. You can see, and perhaps touch it
        - You know it's a water bottle because of it's features which have meaning to you through living in the modern world (perhaps owning a water bottle yourself!)
            - If you were an alien, or a homosapien from a very long time ago, you wouldn't know that the object was a water bottle (among other things...)

{{< details "Optional: Deductive versus Inductive Reasoning" >}}
1. **Deductive reasoning** works from the more general to the more specific, i.e., “top-down” approach.
    - In deductive reasoning there is usually a first premise, then a second premise (both of which are proven through observations), and finally an inference.
    - Ex: All men are mortal. Smerdley is a man. Therefore, Smerdley is mortal.
2. Inductive reasoning works the other way, moving from specific observations to broader generalizations and theories, i.e., “bottom-up” approach
    - Inductive reasoning extracts a likely (but not certain) premise from specific and  limited observations.
    - Ex: I have a bag of many coins, and I’ve pulled 10 at random and they’ve all been pennies, therefore this is probably a bag full of pennies.
{{< /details >}}


## “Objective reality” is often not as objective as we think...

> _A fool sees not the same tree that a wise man sees._  --- William Blake
- Reversible figures (e.g., Necker cube; vase/profiles)
- Ambiguous figures (e.g., old woman/young woman -- also old people tend to see the old figure first, and vis-versa)
    > {{< columns >}}<!-- mathjax fix -->
![](/docs/cogsci-c100/perception/beans.png)
![](/docs/cogsci-c100/perception/young-old.png)

<---><!-- mathjax fix -->
![](/docs/cogsci-c100/perception/rubin.png)
![](/docs/cogsci-c100/perception/necker.png)
{{< /columns >}}

    > {{< columns >}}<!-- mathjax fix -->
- Effect of expectations on perception
    - Perceptual set brain teasers: SOAK FOLK CROAK
    - Context effects (e.g. bea(r|n), [Presidential illusion](https://www.independent.co.uk/news/science/presidential-optical-illusion-offers-clues-to-how-brain-processes-faces-a191716.html))

![](/docs/cogsci-c100/perception/monster.png)
---
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/perception/prez.jpg)
![](/docs/cogsci-c100/perception/doggy.png)
{{< /columns >}}


## Effects of expectations, experience, emotional patterns, and beliefs on perception

- Effects of Prior Experience on Perception
    - Children who have been physically abused are significantly more likely to misperceive a fearful face as angry (Pollak)
        > ![](/docs/cogsci-c100/perception/fear.png)
- Cultural effects on perception
    - What is above the woman’s head?
    - Is this an indoor or outdoor scene? (Gregory and Gombrich, 1973)
        > ![](/docs/cogsci-c100/perception/outside.png)
- Rorscharch and Thematic Apperception Test (TAT)
    > {{< columns >}}<!-- mathjax fix -->
![](/docs/cogsci-c100/perception/woman.png)
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/perception/ink.png)
{{< /columns >}}
    - When angry, people more often perceive neutral objects as guns (Baumann & DeSteno, 2010)
    - Effect of beliefs/preconceived notions on perception
        - Rosenhan study on effects of psychological labeling


## Self-fulfilling prophecies

- **Self-fulfilling prophecies:** People generally think that it is our experiences and perceptions that create our beliefs, but often, it is actually our beliefs that create our experiences and perceptions
    {{< figure  src="/docs/cogsci-c100/perception/proph.jpg" >}}
- Our beliefs and expectations influence **others’** behavior
    - **The Pygmalion effect:** study found that students who were (randomly) labeled intellectual “spurters” showed significantly greater gains in IQ and academic performance after 8 months than controls
        - Follow-up: If teacher believed that girls learn to read faster than boys, they did
    - Children who were told they were neat and tidy became more neat and tidy than those who were told they should be neat and tidy
        - Follow-up: children who are told that they are good at math showed greater improvements in math scores than those who were told that they should try to become good at math
    - Those who over-idealize romantic partners as having many virtues and few faults tend to have happier and longer-lasting relationships (Miller, Niehuis, & Huston, 2006)
        - Moreover, the partners who are over-idealized tended to develop those traits over time! (Sandra Murray)
        - People live up to their expectations -- we tend to bring out what we focus on
- Our beliefs and expectations influence **our own** behavior
    - Study by Mark Snyder found that when a man was led to believe that a woman found him attractive, she was more likely to act as if she did
    - "[Gus Hansen refused to acknowledge the odds and the odds disappear](https://www.youtube.com/watch?v=bDt90EyZnWA&t=1295s)"
        > _Assume a virtue if you have it not._ – Shakespeare

## Perceptual Constancies

- **Perceptual constancy:** perceiving objects as unchanging (having consistent lightness, color, shape, and size) even as illumination and retinal images change
    - Many visual illusions result from the overuse of strategies employed to achieve perceptual constancy
        > ![](/docs/cogsci-c100/perception/tile.png)
        > Is Tile A or Tile B darker or are they the same color?
        > - Illusion results from visual system’s attempt to maintain lightness constancy: we perceive an object as having a constant color, even if changing illumination alters the wavelengths reflected by the object

{{< columns >}}<!-- mathjax fix -->
- **Shape constancy:** we perceive the form of familiar objects as constant even while our retinal images of them change
    - A door casts an increasingly trapezoidal image on our retinas as it opens, yet we still perceive it as rectangular
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/perception/door.png)
{{< /columns >}}
<br>
{{< columns >}}<!-- mathjax fix -->
- Müller-Lyer illusion:
    - Is line AB or line BC longer?
    - **Size-distance constancy:** Our brains are used to perceiving angles as corners that are near or far away and sees the inward-facing corners as more distant and therefore smaller

![](/docs/cogsci-c100/perception/ponzo.gif)
- Are the two parallelograms the same size and shape?
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/perception/MLw.png)
- Ponzo illusion:
    - Which line is longer?

![](/docs/cogsci-c100/perception/tables.png)
{{< /columns >}}

- **Moon illusion:** Does the moon appear larger near the horizon or when it is high in the sky?
    >![](/docs/cogsci-c100/perception/moon.png)
    >- When the moon is near the horizon we perceive it to be farther away from us than when it is high in the sky, but since the moon is actually the same size, our minds make it look bigger when it is near the horizon to compensate for the increased distance
- The Magical Kingdom of Salt
    >{{< columns >}}<!-- mathjax fix -->
![](/docs/cogsci-c100/perception/boot.png)
<---><!-- mathjax fix -->
<br>

- In the Salar de Uyuni of Bolivia, the world’s largest salt flat, with no other objects in sights, the human eye loses its ability to establish a proper field of depth.  The result is some bizarre pictures.
{{< /columns >}}


## Effects of color in marketing

- Assume that you are considering buying condoms
    - You enter a store and notice that the store doesn’t carry all the brands  you may be familiar with, so you’re going to have to make your  choice based on the product package alone
    - You are really interested in finding a brand that is considered
        - Durable, strong, and well built (“rugged” condition) OR
        - Classy, attractive, and refined (“sophisticated” condition)
- Which would you choose?
    ![](/docs/cogsci-c100/perception/condoms.png)
- Match the colors with the following
    ![](/docs/cogsci-c100/perception/match.png)
    {{< columns >}}<!-- mathjax fix -->
- Sincerity: white, yellow.$^1$
- Excitement: red, orange.$^1$
- Competence: blue
<---><!-- mathjax fix -->
- Sophistication: black, pink, purple
- Ruggedness: brown
- .$^1$Marginally significant
{{< /columns >}}

# Neurological disorders of visual perception

## Face perception and prosopagnosia

- Face recognition is “special”
    - Single-cell recordings of monkeys show activation of particular cells in lower temporal only when full-face photos of other monkeys are presented
- Recognition accuracy for faces and houses: parts vs. whole
    {{< columns >}}<!-- mathjax fix -->
- Study (Tanaka and Farah, 1993) in which participants were shown series of faces with person’s name and series of houses with owner’s name
- Later on recognition test, they showed greater recall of
    - _Parts of_ houses but
    - _Whole_ faces
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/perception/house.png)
{{< /columns >}}
  - Do people tend to perceive men or women more in “parts”? Women (Gervais, Vescio , Forster et al., 2012)
- **Prosopagnosia:** failure to recognize particular people by the sight of their faces
    - After stroke, sheep rancher could not recognize people but could recognize sheep
        - Someone would walk in the room and he wouldn't be able to tell if it was the wife/neighbor/robber/etc
    - Note: the eyes also play a special role in perception
        >![](/docs/cogsci-c100/perception/eyes.png)
        > 70-90% of famous portrait paintings sampled from the last five centuries have an eye at or within 5% of the painting’s exact centerline (Christopher W. Tyler)<br><br>
        > _Every man indicates in his eye the exact indication of his rank._  – Emerson

## Modular Processing

{{< columns >}}<!-- mathjax fix -->
- Visual illusions suggest that the mind is at least in part modular (Jerry Fodor)
    - That is, it is not solely organized in terms of faculties, such as memory and attention, that can process any type of information
    - Rather, there are specialized information-processing modules that
        - Respond automatically
        - Cannot be “switched off”
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/perception/cog-head.png)
{{< /columns >}}

{{< columns >}}<!-- mathjax fix -->
<br>

![](/docs/cogsci-c100/perception/break.png)
<---><!-- mathjax fix -->
Modular processes are usually characterized by...
- Fixed neural architecture
    - It is sometimes possible to identify determinate regions of the brain that are associated with particular types of modular processing
        - e.x: fusiform face area for face recognition
- Specific breakdown patterns
    - Modules can fail in highly determinate ways, which provide clues on the form and structure of processing
        - e.x: prosopagnosia
{{< /columns >}}


## Other Neurological Disorders Related to Visual Perception

- **Visual agnosia:** inability to recognize/identify visual objects despite relatively good visual perception
    - Usually due to damage in occipital or temporal lobes
        - “Mr. P” in Oliver Sacks’ Man Who Mistook His Wife for a Hat
        - Man with agnosia puzzling over a picture of a cow suddenly found himself making alternating up-and-down movements with fists.  He looked down at his hands and said, “Oh, a cow!”
        - Due to some error between vision and verbal communication
- **Visual neglect syndrome** or **unilateral spatial neglect**:
    - Tendency to ignore – or to be unaware of – information on one half of visual field, usually the left side
    - Typically occurs after damage (e.g., stroke) to right hemisphere, particularly damage to the parietal and frontal lobes
    - Relatively common, easy to test for
    {{< columns >}}<!-- mathjax fix -->
>![](/docs/cogsci-c100/perception/lines.png)
> Patients are asked to bisect each line.  Their markings are typically skewed to the right, as if they do not see the leftmost segment
<---><!-- mathjax fix -->
>![](/docs/cogsci-c100/perception/drawing.png)
> Patients are asked to draw from memory or to copy an illustration (Driver & Vuilleumier, 2001)
{{< /columns >}}
    {{< details "House" >}}
{{< columns >}}<!-- mathjax fix -->
![](/docs/cogsci-c100/perception/house0.png)
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/perception/house1.png)
{{< /columns >}}
> _Experimenter:_ Are the two houses the same or different?<br>
> _Patient:_ The same.<br>
> _Experimenter:_ Which house would you prefer to live in?<br>
> _Patient:_ The left house.
{{< /details >}}
---

- **Capgras syndrome:** characterized by belief that family and/or friends are imposters
    - Damage to pathway between visual cortex and amygdala, which regulates emotions
    - Emotional “glow” that we normally feel around people we are close to is missing
    - Ramachandran argues that this emotional “glow” is, to a large extent, what gives us a sense of continuity in our relationships
    - Classified as some kind of schizophrenia
- **Functional blindness** (conversion disorder): unexplained vision loss with no organic basis
    - Cambodian women who had witnessed horrible war atrocities became either partially or wholly blind
    - Impairs primarily body functions / processes
        - Psychological defense mechanism
- **Blindsight:** vision without awareness
{{< columns >}}<!-- mathjax fix -->
- Blindness resulting from damage to visual cortex
- When presented with various shapes like circles and square, or photos of faces of men and women, patient could not tell (or guess) what his eyes were gazing at
- However, when shown pictures of people with angry or happy faces, he was able to guess the emotions expressed, at a rate far better than chance
- Patients are also able to correctly “guess” the identity or location of particular objects
- Patients report that they get a “gut” feeling that allows them to perform these tasks
<---><!-- mathjax fix -->
> ![](/docs/cogsci-c100/perception/wander.png)
> Blindsight patient was able to meander around all the clutter in a hallway that he was told was empty (Weiskrantz)
{{< /columns >}}
    - A second pathway of visual perception may account for this phenomenon


## Two pathways of visual perception

{{< columns >}}<!-- mathjax fix -->
![](/docs/cogsci-c100/perception/waldo.png)
<---><!-- mathjax fix -->
- Study looked at speed with which people were able to find a specific hidden object among a group of similar objects
- Participants were instructed to
    1. Passively allow the target to just “pop” into their minds OR
    2. Actively direct their attention to the target
- Participants in Passive Group 1 outperformed those in Group 2 (Smilek, Enns, Eastwood et al., 2006)
{{< /columns >}}
    {{< details "Targets" >}}
![](/docs/cogsci-c100/perception/targets.png)
- Look for the circle with just one gap, and say whether the gap is on the left or the right
- Use “relax” strategy, then try active search strategy
{{< /details >}}
  - Proposed explanation:
    - Participants who were basically told to relax and go with their gut instinct used a secondary pathway of visual perception that
    - Does not go through the visual cortex
    - Instead simply makes a very short loop through the limbic system: the emotional, instinctual center of the brain
![](/docs/cogsci-c100/perception/proposed.png)

{{< columns >}}<!-- mathjax fix -->
![](/docs/cogsci-c100/perception/rat.png)
<---><!-- mathjax fix -->
- Research evidence for existence of two pathways:
    - Auditory cortex of rats was destroyed, then rats were exposed to tone paired with an electric shock
    - Rats quickly learned to fear tone, though they could not “hear” it!
    - Explanation: the sound took the direct route from ear to thalamus to amygdala, bypassing all higher avenues (Joseph Ledoux)
{{< /columns >}}

# Development of perception

{{< columns >}}<!-- mathjax fix -->
![](/docs/cogsci-c100/perception/restrict.png)
- Adults who were born blind and later gained vision through newly-developed surgical interventions (e.g., cataract surgery) usually have some difficulty recognizing objects
    - At age 3, Mike May lost his vision in an explosion.  Decades later, a new cornea restored vision to his right eye.
    - Unfortunately, although signals were now reaching his visual cortex, it lacked the experience to interpret them
        - May could not recognize expression, or faces, apart from features such as hair
        - Yet he can see an object in motion
    - Ended up committing suicide because he found himself in a world he didn't (couldn't) understand or comprehend
<---><!-- mathjax fix -->
<br>

- There is a critical period for normal sensory and perceptual development
- Kittens reared in a cylinder with only vertical black and white stripes later had difficulty perceiving horizontal bars
    - Kitten would play with rod only when it was held upright
    - As if they couldn't see the horizontal rod
<br>
<br>
<br>

![](/docs/cogsci-c100/perception/ball.png)
{{< /columns >}}
