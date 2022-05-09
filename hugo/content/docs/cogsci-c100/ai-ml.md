---
title: "17: Artificial Intelligence & Machine Learning"
weight: 17
---


# Basic definitions

- **Artificial Intelligence (AI)**: tries to design computer models that accomplish the same cognitive tasks that humans do
- **Machine Learning**: a subset of AI that allows computers to "learn" (i.e., progressively improve performance on a specific task) by creating new algorithms to produce a desired output based on structured (or unstructured) data that is provided
- **Deep Learning**: a subset of Machine Learning involving numerous layers of algorithms
    * Computer does not need to be provided with structured data
- **Neural Networks**: Networks of algorithms that are similar to the neural networks present in the human brain
{{< figure  src="/docs/cogsci-c100/ai-ml/hoops.png" >}}

## Artificial Intelligence Formulations

> There are a number of different artificial intelligence formulations
- **Strong AI**: General purpose AI
    - Machines that possess artificial general intelligence (AGI)
    - Would be just as smart as humans across the board with the ability to understand and learn any task that a human can
- **Applied AI**: AGI isn't going to be created any time soon, but machine learning has made it possible for machines to learn how to master complex tasks (expert systems), including
    - Playing the ancient Chinese board game Go
    - Identifying human faces
    - Translating text into practically every language
    - Driving cars
- **Computer replication**: Understand how the mind works and replicate its functions in machine or organic form

## Machine Learning

{{< figure  src="/docs/cogsci-c100/ai-ml/a.png" >}}

- Problem: How can a computer learn to distinguish between pictures of dogs and cats?
- Approach: You label pictures of dogs and cats with specific defining characteristics (e.g., length of ear, color of nose), then feed this structured data through the computer

## Deep Learning

- You feed the computer pictures labeled as dogs or cats without additional structured data
- Data is sent through different layers of the artificial neural network corresponding to different layers of abstraction, from low level (e.g., does this part of picture contain a brown spot?) to more complex, e.g., (is there a nose in this part of the picture?)

{{< figure  src="/docs/cogsci-c100/ai-ml/b.png" >}}
{{< figure  src="/docs/cogsci-c100/ai-ml/c.png" >}}


## Supervised, Unsupervised, and Deep Reinforcement Learning

- In supervised learning, network receives explicit feedback on how successful it is
- In unsupervised learning, network does not receive explicit feedback; instead it learns to detect patterns in data
- Reinforcement learning is distinct from both of the above in that
    - It does depend upon a feedback signal
    - However, the feedback signal does not tell the network exactly what it has done wrong; instead, the network is driven by a reward signal
        - The job of the network is to maximize the reward, but it is not told how to do that
        - It has to work out for itself which outputs are most profitable
    - Ex: Atari breakout

### AlphaGo

> In 2016 and 2017, AlphaGo program created by Google’s Deep Mind research group beat the world’s leading human experts at the game of Go
- These victories were widely recognized as historic achievements for AI
- Go is an abstract strategy board game for two players, in which the aim is to surround more territory than the opponent
    - It is one of world’s most complex games
    - Chess has 10^123 possible moves; Go has 10^360
- AlphaGo used a mixture of supervised learning and reinforcement learning
    - Was initially trained on a database of 30 million moves from an online server using supervised learning -- received explicit feedback on how successful it was
    - Once AlphaGo had achieved a relatively high level of playing strength, training shifted to reinforcement learning
        - In reinforcement learning, network will not increase its reward simply by repeating what has worked in the past
        - It needs to engage in trial and error to discover new reward-generating strategies
        - Reinforcement learning was achieved by getting the network to play games of Go against former versions of itself
- New version, AlphaGo Zero, incorporated zero supervised learning
    - After three days (and 4.9 million games played against itself), it was able to beat the version of AlphaGo that had defeated the leading human expert in 2016 -- 100 games to 0!
    - Within 40 days, it was able to beat all existing versions of AlphaGo

{{< columns >}}<!-- mathjax fix -->
{{< figure  src="/docs/cogsci-c100/ai-ml/d.png" >}}
<---><!-- mathjax fix -->
{{< figure  src="/docs/cogsci-c100/ai-ml/e.png" >}}
{{< /columns >}}


# Applications of AI
## Healthcare

- Diagnosis of disorders, e.g., IBM Watson
    - Computers found to be as good or better than doctors at detecting tiny lung cancers on CT scans
    - **Potential hazard**: A radiologist who misreads a scan may harm one patient, but a flawed A.I. system in widespread use could injure many
- Determining optimal treatment, including
    - Type and dosage of drugs
    - Best diet for individual, e.g., to avoid glucose spikes after eating
        - This may vary, depending on patient’s unique gut microbiome
- Precision surgery without human artifacts like handshaking
    - Study comparing computer-controlled robots with human surgeons in performing intestinal surgery on a pig found that the robot sutures were much better—more precise and uniform with fewer chances for breakage, leakage, and infection (Shademan, Decker, Opfermann et al., 2016)

## Brain Computer Interface

{{< columns >}}<!-- mathjax fix -->
> Brain Computer Interface (BCI) or Brain Machine Interface (BMI): "neural prosthetics"
- Computer chip is implanted in motor cortex and communicates directly with external device
- Allows animal (or person) to directly control a robotic arm with their thoughts
<---><!-- mathjax fix -->
{{< figure  src="/docs/cogsci-c100/ai-ml/f.png" >}}
{{< /columns >}}
> A cap with electrodes can now be used instead of implants, but an extensive calibration process is required
>{{< figure  src="/docs/cogsci-c100/ai-ml/g.png" >}}

> Direct brain-to-brain communication in humans is also now possible
- Two research participants are are positioned in two different buildings on campus
    - The sender, left, thinks about firing a cannon at various points throughout a computer game
    - That signal is sent over the Web directly to the brain of the receiver, right, whose hand hits a touchpad to fire the cannon (Rao, Stucco, Ryan et al., 2014)
{{< figure  src="/docs/cogsci-c100/ai-ml/h.png" >}}

## Psychotherapy

> Diagnosis/identification of psychological disorders
- AI system that analyzed Facebook posts of consenting patients in an emergency department was able to generate predictions of depression risk that were as accurate as standard depression screening tests (Reece & Danforth, 2017)
    - Indicators included references to sadness, loneliness, hostility, rumination, and increased self-reference, e.g., words like "alone," "ugh," "tears," and higher frequency of use of "I" and "me"
    - Length and timing of posts were also considered (Eichstaedt, Smith, Merchant et al., 2018)
- AI has also been used to analyze Instagram photos to successfully screen for depression
    - Photos posted by depressed individuals tended to be bluer, darker, and grayer
    - The more comments Instagram posts received, the more likely they were posted by depressed participants, but the opposite was true for likes received
    - Depressed participants were more likely to post photos with faces, but had a lower average face count per photo than healthy participants
    > The screening models created from the data were able to outperform general practitioners in correctly diagnosing depression without the assistance of assessment instruments

----

> A.I.-driven voice analysis
- Researchers are currently working on developing voice analysis programs that can help identify psychological disorders
    - In depression, speech is generally more monotone, with reduced pitch range and lower volume; there may be more pauses
    - In anxiety, speech tends to be faster, and there may be evidence of difficulty breathing
    - Programs may also be used to predict other mental illnesses like schizophrenia and PTSD
- Use of deep-learning algorithms can uncover patterns that might not be evident even to trained experts
    - "The technology that we’re using now can extract features that that even the human ear can’t pick up on."
- Potential problems:
    - It can be difficult to know why your vocal levels fluctuate, e.g., you may just be trying to speak quietly
    - Issue of bias: need to ensure that programs work for all patients, regardless of age, gender, ethnicity, etc.
    - Deep learning algorithms work in ways that even the developers themselves can’t fully explain, that is, knowing which features are being used to make the predictions


### Treatment of psychological disorders

- Apps that can administer Cognitive Behavioral Therapy for disorders like depression or social anxiety, e.g., Woebot
- Virtual therapists, e.g., Ellie
- These programs may analyze tone of voice, breathing pattern, smartphone keystrokes and communication, and/or physical movements in making diagnoses and generating responses
- Pros:
    - Easy accessibility and affordability
    - Research has indicated that people would rather share their innermost secrets with an avatar than a human being
- Cons:
    - Can’t really replace human empathy
    - Adherence to treatment may be poor


## Transportation

> Self-driving cars
  - 2018 was the target date proposed in 2015 both by Elon Musk of Tesla and by Google for introduction of self-driving cars
  - But a series of widely publicized crashes, some fatal, have delayed release
> Are self-driving cars really a viable option?
  - The great successes of deep learning have all been in relatively circumscribed domains, including chess and Go, and even things like image recognition, which primarily involves identifying patterns in a data set, then projecting those patterns onto new exemplars
  - Some believe that self-driving cars (and other autonomous vehicles, like drones) need more than sensitivity to patterns and the ability to learn from experience
    * They **need to be able to deal with the unexpected** -- completely unpredictable behavior from other drivers, pedestrians, cyclist, and even wild animals
  - Also, human drivers are constantly exploiting their knowledge of how physical objects move and behave (folk physics), as well as their knowledge of other drivers and road-users (mindreading)
    * Perhaps a key challenge, perhaps the key challenge, for designers of self-driving cars is how to equip their vehicles with this kind of general knowledge

{{< columns >}}<!-- mathjax fix -->
- Pros:
    - Less human error = more lives saved
    - Accessible to those who cannot drive
    - Can engage in other activities during commute
<---><!-- mathjax fix -->
- Cons:
    - Criminal hacking or system glitches
    - Loss of jobs
    - High initial cost
    - Fewer people using public transportation
{{< /columns >}}

>### Moral issues
>    - Cars will need to make "moral" decisions in unavoidable accidents
>    - Which person to sacrifice, the pedestrian or the driver?
>{{< figure  src="/docs/cogsci-c100/ai-ml/i.png" >}}

## Robots

- Social robots
- Home robots: cooking, cleaning, fetching…
    - Moley learns to cook by using data from the motion-capturing gloves and wristbands of a master chef

### Other applications

- **Language processing:** Use of natural language processing of speech to synthesize notes in professional settings
- **Advertising:** Tracking customer behavior to target them with personalized promotions
- **Customer service:** Help lines; providing information to consumers
- **Finance and economics:**
    - Record keeping
    - Fraud detection
    - Optimizing profits in online trading
    - Predicting market supply and demand


# Risks and Dangers of AI

- Deliberate programming of AI to be hostile, e.g., by terrorist group
- Sci-fi scenario: If human behavior contradicts one of AI’s preprogrammed goals, AI could turn malicious
    - In 2017, two Facebook computers started communicating with each other in a language they had developed on their own
- Simulation of government leader’s image and voice issuing unauthorized orders, e.g., military action
- Generation of fake emails, phone calls, video chats
- Loss of privacy
- Loss of jobs
    - Some AI experts predict that AI will replace or eliminate 40% of jobs within 15 years
    - Greatest impact will be on jobs involving tasks that are repetitive and can be automated

----

- Other AI-related risk: Development of computer technology has meant an increase in the amount of time we spend looking at computer screens, and that may be harmful
    - Recent study published in JAMA Pediatrics found that after controlling for age, gender and income, 3-5 year old children with higher use of screen-based media
        - Had lower measures of structural integrity and myelination
        - Scored lower on cognitive tests (Hutton, Dudley, Horowitz-Kraus et al., 2020)
    - Similarly, in older adults, increased television viewing was found to be correlated with cognitive impairment and poor verbal memory (Fancourt and Steptoe, 2019)
    - In fruit flies, daily blue-light exposure (such as is used in computer screens) causes brain neurodegeneration, as well as shortening of lifespan (Nash, Chow, Law et al., 2019)

{{< hint "info" >}}<!-- mathjax fix -->
American Academy of Pediatrics recommendations:
- Children under 18 months should avert their eyes from TV and screen media at all times
- For children 2 to 5, screen time should be limited to no more than 1 hour per day
{{< /hint >}}

### Issue of biases

- Back in 2015, software engineer Jacky Alciné pointed out that the image recognition algorithms in Google Photos were classifying his African American friends as "gorillas"
    - Google said it was "appalled" at the mistake, apologized to Alciné, and promised to fix the problem
    - However, three years later, Google still had not really fixed anything – the company simply blocked its image recognition algorithms from identifying gorillas altogether
        - Baboons, gibbons, and marmosets were all correctly identified, but gorillas and chimpanzees were not
- Try typing things like "why Black/Latinx/Asian women/men/boys/girls ..." on Yahoo or Bing
    - You’ll get really biased, racist and discriminatory auto-suggestions
    - These are now blocked on Google, but not on other search engines

# AI and jobs

{{< columns >}}<!-- mathjax fix -->
- On the other hand, AI has also created new jobs, e.g., AI designer, software engineer, cybersecurity developer, machine relations manager
- Unfortunately though, people whose jobs are taken away may not necessarily be those who get new jobs created by AI development
<---><!-- mathjax fix -->
![](/docs/cogsci-c100/ai-ml/j.png)
{{< /columns >}}

## Jobs that Are Hard to Replace

- Emotionally demanding jobs
    - Therapist
        - Depends on individual (some veterans like talking to AI)
    - Taking care of babies/children
    - Human Resources
    - Politician
- Creative jobs
    - Writer
    - Software/graphic designer

# Things We Can Do that AI Cannot Do Well

- Feel or show empathy
- Have insights
    - As Anthony Goldbloom puts it, machines cannot "connect seemingly disparate threads to solve problems they have never seen before"
    - Machines can’t tackle novel situations
    - Need to learn from large volumes of past data
        - Percy Spencer was working on radar during World War II when he noticed a magnetron (used to generate radio signals) melting his chocolate bar
        - This led to the discovery of the Microwave oven!
- Make plans for the distant future
    - Humans can plan their lives years in advance
    - Robots tend to focus only on completing the immediate task at hand
- Be conscious (?)
    - Whether machines can have consciousness depends on the definition of consciousness
    - No machine today meets all the criteria that we may give to consciousness and that humans have
