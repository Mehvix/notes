---
title: "14: Problem Solving, Creativity, & Decision Making"
weight: 14
---


# Problem Solving

### Steps involved

> Studies have found that college education improves people’s problem solving/reasoning ability
- The ability to reason that’s developed through learning about rules of reasoning, etc. in the natural and social sciences can generalize to other domains (e.g., everyday problems)
- May be one reason that those with a college education have been found to handle stress better than those who have not gone to college
* Every problem contains an initial state, goal state, and obstacles

### Approaches: use of algorithms vs. heuristics
{{< columns >}}<!-- mathjax fix -->



> **Algorithm**: a methodical, logical rule or procedure that guarantees a solution to a particular problem
- One example is exhaustive search
    - Trying to solve an anagram by testing out all possible letter combinations one by one
    - Problem with this is that it is very time-consumiang
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/problem/words.png)
{{< /columns >}}

> **Heuristic**: a rule-of-thumb strategy that allows one to reduce the number of operations that are tried in solving a problem
- Looking only for pronounceable letter combinations (like "le" or "sa" when trying to solve an anagram)
    - Most everyday problems are solved using heuristics
- *Heuristics are speedier but also more error-prone than algorithms*

## Strategies for improving problem solving

### Understand the problem

- Elevator in high rise building problem
![](/docs/cogsci-c100/problem/ele.png)

### Represent problem effectively using symbols

- Represent the problem effectively using symbols, matrices, diagrams, and visual images
- Example: Buddhist Monk Problem:
{{< columns >}}<!-- mathjax fix -->
- At sunrise one morning, a Buddhist monk began to climb a tall mountain.
- He sometimes climbed the path quickly, and he sometimes went more slowly. From time to time, he stopped along the way to rest or to eat the fruit he had brought with him. Finally he reached the temple, just a few minutes before sunset.
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/problem/hill.png)
{{< /columns >}}
  - At the temple, he meditated for several days. Then he began his descent back along the same path. He left the temple at sunrise and walked at a varying pace as before. Of course though, he walked down the hill more quickly than when he was walking up the hill.
  * Demonstrate that there must be a spot along the path that the monk will pass on both trips at exactly the same time of day.
>![](/docs/cogsci-c100/problem/graph.png)
> Represent the problem in a way that is appropriate to problem solver’s background knowledge

### Means-end heuristic

> **Means-end heuristic**: divide problem into sub-problems and try to reduce difference between initial state and goal state for each of sub-problems
* Newell and Simon developed General Problem Solver program (1957) asa way of solving complex problems using means-end analysis
- Hobbits-and-Orcs Problem:
    > Imagine that 3 Hobbits and 3 Orcs all arrive at the right side of a riverbank, and they all want to cross to the left side. Fortunately, there is a boat. However, the boat is small, and it can hold only two creatures at one time. Moreover, whenever there are more Orcs than Hobbits on one side of the river, the Orcs will immediately attack the Hobbits and gobble them up.. Therefore, you must be absolutely certain that you never leave more Orcs than Hobbits on any riverbank. How would you solve this dilemma?

    {{< details "Answer" >}}
Sometimes it may be necessary to move backwards (hobbits-and-orcs problem) -- problem-solvers are often unwilling to do this!
    {{< /details >}}
- Tower of Hanoi
![](/docs/cogsci-c100/problem/hanoi.png)

### Analogy approach

- **Analogy approach**: problem solving is often a matter of finding a useful analogy between the present problem or situation and some other problem or situation with which you are more familiar
{{< columns >}}<!-- mathjax fix -->
- Candle problem: find a way to attach the candle to a wall so that it burns properly using no other objects than those on the table
![](/docs/cogsci-c100/problem/match.png)
<---><!-- mathjax fix -->
{{< details "Answer" >}}
- Can find solution to candle problem through a deliberate search for a useful analogy: Shelf ➜ tack box
![](/docs/cogsci-c100/problem/match2.png)
{{< /details >}}
{{< /columns >}}


### Represent information efficiently

{{< columns >}}<!-- mathjax fix -->
- Represent information efficiently and find shortcuts
- **Stick-configuration problem**: remove exactly five sticks from the pattern so that only three squares are left, with no sticks left over
    * Can find solution to stick-configuration problem by using a heuristic that involves thinking in terms of squares rather than sticks: "Find three squares, out of the six available, which if preserved, would allow for the removal of exactly five sticks"
<---><!-- mathjax fix -->
{{< figure  src="/docs/cogsci-c100/problem/m1.png" >}}
{{< details "Answer" >}}
{{< figure  src="/docs/cogsci-c100/problem/m2.png" >}}
{{< /details >}}
{{< /columns >}}

### Promote use of parallel processing rather than serial processing

{{< columns >}}<!-- mathjax fix -->
- Promote use of parallel processing rather than serial processing
    - Expert anagram solvers say that solutions simply seem to "pop out" (parallel processing)
    - In contrast, novices generally use serial processing
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/problem/arst.png)
{{< /columns >}}

### Foster insight

> **Foster insight**: finding a solution is a matter of perceptual reorganization — any conditions that would allow your thought and perceptual processes to run more freely might help

## Obstacles to Problem Solving

> **Confirmation bias**: tendency to search for information that confirms one’s preconceptions
- Wason card problem
    - **Statement**: "If a card has vowel on one side, then it has an even number on the other side"
![](/docs/cogsci-c100/problem/69.png)
- Accuracy is enhanced when task describes a concrete social situation
- In general, research has found that humans tend to be much better at reasoning with deontic conditional than they are with ordinary, nondeontic conditionals (with the Wason card problem being one example)
    - Deontic conditionals have to do with permissions, prohibitions etc.

>![](/docs/cogsci-c100/problem/b.png)
>- **Statement**: "If a person is drinking beer, they must be over 21 years of age"
>   * 73% of students who tried drinking-age problem made correct selections, as opposed to 0% in the standard, abstract form of task

- Why are people are better at reasoning with deontic conditionals?
    - Theory that when we solve problems with deontic conditionals, we are using a specialized module for monitoring social exchanges and detecting cheaters
    - This is the **cheater detection module** (Cosmides and Tooby)
- Why should there be a cheater detection module?
    - Cooperative behavior presumably has a genetic basis
    - However, an individual who takes advantage of cooperators without reciprocating will likely do better than one who cooperates
        - Ex: They gain your trust, then steal all your bananas
    - So how could the genes for cooperative behavior ever have become established?
        * Enter the cheater detection module…

### Confirmation Bias And Social Judgments

- Study in which participants asked to interview other student to determine if interviewee was an introvert or extravert
    * Participants who tested for extraversion tended to find interviewees extraverted and vice versa because of tendency to ask questions that confirmed trait
- Rosenhan study
    - Confirmation bias may have important implication for medical diagnosis/psychotherapy
    - Therapist may form a less than accurate first impression of a patient and then only ask questions geared toward confirming that view
> **Be willing to entertain the possibility that you may be wrong!**

### Mental set

- **Mental set**: tendency to approach a problem in a particular way, especially a way that has been successful in the past but may not be helpful in solving a new problem
    >**Nine dot problem**: connect dots by drawing four continuous straight lines without lifting your pencil from the paper
    >![](/docs/cogsci-c100/problem/dots.png)

    > **Match-triangle problem**: assemble six matches to form four equilateral triangles, each side of which is equal to the length of one match
    >![](/docs/cogsci-c100/problem/twr.png)

    > **Horse-and-rider problem**: place B on A in such a way that the cowboys are correctly astride their horses
    >![](/docs/cogsci-c100/problem/a.png)


### Functional fixedness

> **Functional fixedness**: tendency to think of things only in terms of their usual functions; ex. Candle problem

## Insight vs. Non-Insight Problems

> **Insight**: a sudden and often novel realization of the solution to a problem
>    - Contrasts with strategy-based solutions
- Insight problems are solved when answer appears suddenly
- Non-insight problems are solved gradually (e.g., using means-end heuristics)

### Neural Basis of Insight

{{< columns >}}<!-- mathjax fix -->
- Some critical components of insight are preferentially associated with the **right cerebral hemisphere**
- At the moment when people solve problems by insight, relative to solving identical problems by analytic processing:
    - EEG shows a burst of highfrequency gamma-band EEG activity over the right anterior temporal lobe
    - fMRI shows a corresponding change in blood flow in this area (Kounios and Beeman, 2014)
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/problem/s.png)
{{< /columns >}}
- Direct stimulation of right frontal-temporal cortex coupled with inhibition of left frontal- temporal cortex enhances solving of insight problems
- Insightful individuals show greater right hemisphere activity at rest, relative to analytic individuals
----
{{< columns >}}<!-- mathjax fix -->
- Performance is enhanced or unaffected if you verbalize strategies while solving non-insight problem
- Performance is disrupted if you verbalize strategies while solving insight problem
> _Differences may perhaps be explained by hemispheric specialization – left hemisphere is especially skilled at logical reasoning and language processing; the right is more spatial and holistic_
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/problem/q.png)
{{< /columns >}}
- Priming people to think about the **distant future** biases them to think abstractly, causing them to perform better on insight and creativity tasks
- Conversely, priming people to think about the **near future** biases them to think concretely, causing them to perform better on analytic tasks (Förster, Jens, Friedman et al, 2004)

----

- Insightful individuals (Kounios and Beeman, 2014)
    - Show more externally oriented attention (reduced occipital alphaband EEG activity) than do analytical individuals during the resting state
    - Show **greater internal focus** of attention during the preparation phase prior to the presentation of the insight problem indicated by:
        - Activation of **anterior cingulate** (*detection of weak activation of nondominant solution possibilities*)
        - Increase in alpha-band activity over **right occipital cortex**
    * Probably analogous to common behavior of closing or averting one’s eyes to avoid distractions that would otherwise interfere with intense mental effort
- Positive mood facilitates insight, probably by increasing attentional scope to include weakly activated solution possibilities (i.e., "wide-angle vision")
- Relation between broad associations/insight and positive mood is bidirectional
    - Inducing faster reading by manipulating paced reading makes participants feel more positively (Bar, M., 2009)
        - Reading causes the activation of concepts, and presumably, faster reading activates more concepts, which could be seen as analogous to a massive increase in broad associative activation
    - In contrast, "rumination," which involves dwelling on a narrow theme, is associated with depression
- Similarity between insight and jokes in that both involve restructuring

# Creativity

## Definition of creativity

{{< columns >}}<!-- mathjax fix -->
> **Creativity**: finding a solution that is novel and useful
- To foster creativity and insight, promote conditions that allow thought and perceptual processes to run more freely
- **Increase intrinsic motivation:** Intrinsic motivation (measured by concentration on task, exploration, and enjoyment of task) promotes high levels of creativity
> "The labor of love aspect is important."<br>
> -- Nobel Laureate Arthur Schawlow
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/problem/idea.png)
{{< /columns >}}


### Reduce anxiety

{{< columns >}}<!-- mathjax fix -->
- Extrinsic motivation (being offered a reward for being creative) can reduce creativity (Glucksberg, 1962)
    - Participants who expected no particular reward for solving candle problem solved the problem more quickly than those who were told they might win a \$20 reward!
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/problem/20.png)
{{< /columns >}}

> Conditions that increase anxiety (knowing that your work will be evaluated, having someone watch while you work, being offered a reward for being creative) tend to reduce creativity

### Promote lightheartedness

{{< columns >}}<!-- mathjax fix -->
- Conditions that promote lightheartedness tend to facilitate solution
- Students who had just watched a comedy film were far more successful in solving candle problem than those who had seen either a serious film or no film(Isen, Daubman, &Nowicki, 1987)
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/problem/masks.png)
{{< /columns >}}


## Strategies for enhancing creativity

### Brainstorming

{{< columns >}}<!-- mathjax fix -->
> **Brainstorming**: where you get people together and just try to get ideas out, to get them up on the board -- and completely suspend criticism (nothing kills creativity like the threat of criticism!)
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/problem/p.png)
{{< /columns >}}


### Incubation

> Incubation: taking a break when you get stuck on a problem may encourage creativity
- Helps you break out of mental set and see problem in new way
- In one series of experiments, three groups of people read complex information (e.g., about apartments or European football matches)
    - Group 1 stated preference immediately after reading information about four possible options
    - Group 2, given several minutes to analyze the information, made slightly smarter decisions
    - Group 3, whose attention was distracted for a time, enabling their minds to engage in automatic, unconscious processing of the complex information, performed best (Strick, Dijksterhuis, & Baaren, 2010)


### Does a messy desk promote creativity?
- College students were randomly assigned to spend time in adjacent office spaces (Vohs, Redden & Rahinel, 2013)
{{< columns >}}<!-- mathjax fix -->
- One room was exquisitely neat, the other was wildly cluttered with papers and other work-related detritus
    * Those in messy spaces generated ideas that were significantly more creative, according to two independent judges
* Participants were also offered an apple or a chocolate bar as they exited
    * Those who sat in the orderly office were twice as likely to choose the apple than those who sat amid the mess)
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/problem/ein.png)
{{< /columns >}}

# Decision Making

> **Decision making**: assessing and choosing among several alternatives
> - Rules less clear than in logical reasoning

## Decision-making biases

1. Decision-making heuristics are typically useful in our daily lives
2. Errors occur because we use heuristics beyond the range for which they are intended

### Availability bias

> **Availability heuristic or bias**: estimating the likelihood of events based on their availability in memory: if instances come readily to mind, we presume such events are common
- Are tornados more likely to occur in Kansas or Texas?
- People’s estimates of violent crimes, insanity pleas
- Clinical applications
    - When people are encouraged to recall pleasant events form their past, they judge pleasant events to be more likely in their future
    - In contrast, when asked to recall unpleasant events, they judge unpleasant event to be more likely in future

### Framing

> **Framing**: Drawing different conclusions from the same information, depending on how that information is presented
- Imagine two surgeons explaining the risk of an upcoming surgery
{{< columns >}}<!-- mathjax fix -->
- One explains that during this type of surgery, 10% of people die
- The other explains that 90% survive
    * In real-life surveys, patients and physicians overwhelmingly say the risk is greater when they hear that 10% die
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/problem/choice.png)
{{< /columns >}}
- Choosing to save for retirement
    - U.S. companies once required employees who wanted to contribute to a retirement plan to opt in by choosing a lower take-home pay
    - A new law allowed employers to automatically enroll their employees in the plan but with the option of opting out
        * Either way, the decision to contribute is the employee’s, but under the new "opt-out" arrangement, one analysis of 3.4 million workers found that enrollments soared from 59% to 86%

### Base-rate fallacy

> **Base-rate fallacy**: tendency to ignore the base rate in evaluating information
- Problem:
{{< columns >}}<!-- mathjax fix -->
- A patient tests positive for a nasty disease
- The test has a 99% accuracy rate
- The disease afflicts 1 in 100 people
- What are the chances the patient actually has the disease?
<---><!-- mathjax fix -->
{{< details "Answer" >}}
The intuitive answer is 99%, but the correct answer is 50%
- Even though the test is highly reliable, it will still misdiagnose one person in every 100
- That means that, in a population of 10,000, there will be 99 people without the disease who will test positive
    - 99 people with the disease will also test positive
{{< /details >}}
{{< /columns >}}

{{< hint "info" >}}<!-- mathjax fix -->
#### Bayes’ Theorem

- $P(A)$ = probability of event A or probability of disease in general population
- $P(B)$ = probability of event B or probability of a positive test result
- $P(A|B)$ = probability of observing event A if B is true or probability of having disease if test is positive
- $P(B|A)$ = probability of observing event B if A is true or probability of testing positive if one has disease
{{< katex />}}

$$P(A|B) = \frac{P(B|A)}{P(A)} = \frac{0.99 \times 0.01}{198/10,000} = 50\\% $$

![](/docs/cogsci-c100/problem/chart.png)

- People generally do not answer the medical diagnosis question correctly, but there is evidence that biological systems, such as our visual perception, language learning, and reward systems may utilize Bayesian principles

{{< youtube "HZGCoVF3YvM" >}}
{{< /hint >}}

### Anchoring and adjustment bias

> **Anchoring and adjustment heuristic**: Relying too heavily on the first piece of information seen
- Study in which real estate agents asked to estimate value of a particular house with different list prices
- Real estate salesmen may show "set-up" properties first:
    - "The house I got them spotted for looks really great after they’ve first looked at a couple of dumps." (Northcraft & Neal, 1987)
![](/docs/cogsci-c100/problem/house.png)

### Overconfidence

> **Overconfidence**: tendency to overestimate the accuracy of one’s beliefs and judgments
- Has many potentially detrimental effects
    - Ex: In wars, each side tends to overestimate its own chances of success

> **Dunning-Kruger effect**: ignorance of one’s own incompetence
- Students scoring at the low end of grammar and logic tests believed they had scored in the top half (Williams, Dunning & Kruger, 2013)
- In a set of six studies looking at people’s confidence in their performance on intellectual tasks, participants completed tests involving logical reasoning, intuitive physics, or financial investment
    - Results: the more they approached such tasks in a "rational" (i.e., consistent, algorithmic) manner -- as opposed to more variable or ad hoc approaches -- the more confident they become, irrespective of whether they are correct (Kruger & Dunning, 1999)
- However, overconfidence may have adaptive value
    - People who err on the side of overconfidence live more happily and find it easier to make tough decisions (Anderson, Brion, & Moore, 2012)
    - Depressed people actually tend to be more accurate in judging their beliefs and judgments, as well as their degree of control over a situation (Alloy & Abramson, 1979; Gotlib & Meltzer, 1987)
    {{< columns >}}<!-- mathjax fix -->
> "The secret of success is to never face facts."<br>
> -- Gertrude Stein
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/problem/goat.png)
    {{< /columns >}}


### Belief perseverance

> **Belief perseverance**: clinging to one’s initial conceptions after the basis on which they were formed has been discredited
- High school students were shown either an effective or confusing instructional film attributed their success/failure on the post-test to innate ability -- even when **informed** by the researchers that the film was responsible for their success/failure
    * Once belief that "I’m not very smart" forms, it tends to persist
        - This has important implications for early childhood education
- Given supposedly new research findings on a controversial issue, such as capital punishment, climate change, or politics, that was mixed in its results, people inevitably saw the study as supporting their own beliefs

## Role of emotions in effective decision making

> Feelings are indispensable for rational decisions!
- Lack of emotional responses leads to poor decision-making
- The orbital frontal cortex (OFC) connects three major regions of the brain:
    1. The cortex (the thinking brain)
    2. The amydala (the emotional brain)
    3. The brain stem (the reptilian brain for automatic response)
- Patients with damage to the prefrontal-amygdala circuit
{{< columns >}}<!-- mathjax fix -->
- Make disastrous choices in their business and personal lives
- Can obsess endlessly over a decision as simple as when to make an appointment
- Case of neuropsych patient "Elliott"
    > "At the Supreme Court level where we work, 90% of any decision is emotional. The rational part of us supplies the reasons for supporting our predilections." <br> -- Justice William Douglas
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/problem/path.png)
{{< /columns >}}
- In making purchasing decisions, are you better off weighing all the pros and cons of the various options or going with your gut instinct?
{{< columns >}}<!-- mathjax fix -->
- Shoppers were asked after leaving different stores how much time they had spent deliberating before they bought what they bought
- Researcher called shoppers a few weeks later to find out how happy they were with their purchases (Dijksterhuis, Bos, Nordgren et al., 2006)
- Results:
    - In the case of low-cost items, like oven mitts and shampoo, the longer people had spent deliberating, the more satisfied they were with their purchases
    - The reverse was true of more complicated and expensive purchases, like furniture, cars, or homes
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/problem/shop.png)
![](/docs/cogsci-c100/problem/room.png)
{{< /columns >}}
    > "When making a decision of minor importance, I have always found it advantageous to consider all the pros and cons. In vital matters, however, such as the choice of a mate or a profession, the decision should come from the unconscious, from somewhere within ourselves. In the important decisions of personal life, we should be governed, I think, by the deep inner needs of our nature." -- Freud
