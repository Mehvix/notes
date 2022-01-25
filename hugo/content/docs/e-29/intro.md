---
title: "Introduction"
weight: 1
---

# 1-18: Course introduction

## Overview

<!-- **These are notes are also on [notes.mehvix.com/e-29/](https://notes.mehvix.com/e-29/)** -->
<!-- DSP note^ -->

This class focuses on three main components -- manufacturing processes, dimensional tolerances, and design communication -- and how they interact with one another.

{{< figure  src="/docs/e-29/0/about.png" >}}

The class is made up of 9 modules:
1. Fundamentals
2. Subtractive manufacturing processes
3. Additive manufacturing processes
4. Forming processes
5. Joining processes
6. Graphical visualization techniques
7. Metrology: measuring manufactured objects
8. Geometric dimensioning and tolerancing
9. The future of manufacturing

## Why manufacturing?

- In 2018, U.S. manufacturing accounted for 11.6% of the U.S. economy, 18.2% of global manufacturing output, and 8.2% of the U.S. workforce -- [source](https://www.thebalance.com/u-s-manufacturing-what-it-is-statistics-and-outlook-3305575)
- Manufacturing output is growing, and is returning to the U.S.; output increased >30% between end of 2008 and 2014
- 67% of U.S. R&D is funded by industry
- Even when production is offshore, design is often done here anyway
- Automation is increasing, yet there is a shortage of skilled (human) talent
- Even if you don't want to go into manufacturing industry, research and academia still require manufacturing knowledge 
- Even if the process if outsourced, design is still done in the US. To design well, you have to have a base-level understanding of manufacturing

{{< columns >}}<!-- mathjax fix -->
{{< figure  src="/docs/e-29/0/pew.png" >}}
> Manufacturing output and employment are rising
<---><!-- mathjax fix -->
{{< figure  src="/docs/e-29/0/covid.png" >}}
> Many companies have regionalized their supply chains since the pandemic
{{< /columns >}}


## Processes

In this class we will consider multiple families of processes:
![Processes](/docs/e-29/0/processes.png)
- This is a rapidly moving field that is always adapting
- This class should give you a top level overview so you can evaluate novel methods


## Materials
In this class we will consider multiple families of materials:
![Materials](/docs/e-29/0/materials.png)
- Materials choices influence performance
  - For example, consider the progress of the plane:
  - In 1903 the right brothers low-density wood with steel wire and silk
  - In 1935 the Douglas DC3 used aluminum alloy (since it became feasible to produce and manipulate)
  - Now the 2010 [Boeing 787 Dreamliner](http://www.boeing.com/commercial/787family/programfacts.html) is made up of 50 wt% composites 20 wt% aluminum 15 wt% titanium 20% lower fuel consumption per passenger mile
      - Composite materials are two(+) materials combined together to get best of both worlds, in aviation typically stiff/strong carbon fibers embed in tough/fatigue-resistant polymers.
- Materials choices influence market size
![Cams](/docs/e-29/0/cams.png)
  - There isn't always a best material; different materials fit different markets/needs
  - Opposite side of the coin: There may be multiple valid material choices for a particular function

## Tolerance

- Tolerancing is a formal way of specifying limits on the amount of dimensional variability allowable in manufactured parts
  - We need a range because measurements will never be 100% precise; we need to define an acceptable range
  - Some sources of variation
      - Human operator changes and/or errors
      - Tool wear
      - Environmental changes (temperature, humidity leads to tiny expansions / contractions)
      - Input material variability
      - Measurement error
- Affordable mass-production _relies on interchangeability of parts_
    - When mating parts of given designs, it should not matter which specific parts
- Therefore part dimensions must be consistent
    - But no manufacturing process is perfectly consistent
- If you don't understand the process of manufacturing and the capabilities of tools, then you will won't know how to create manufacturable designs

{{< hint "info" >}}<!-- mathjax fix -->
{{< figure  src="/docs/e-29/0/graph.png" >}}
- Tighter tolerances (closer tolerance limits) are generally more expensive to achieve
- The solid green line shows an ideal process
- The dotted green line shows the impact of an error shifting the distribution, shifting the tails to approach the tolerance upper / lower bound
- The red line shows a unsuitable process (even if it's calibrated accurately, the poor precision causes high variance that it's not really feasible; however, if outside of the limits an additive (or less common subtractive) could be used to )
{{< /hint >}}


### How E29 integrates manufacturing and tolerancing

- Tighter tolerances are more expensive
- The physics of a process determine how tight a tolerance is achievable and how much it costs
- Therefore we need to understand how manufacturing processes work in order to:
    - Select a suitable process for the application
    - Specify reasonable tolerances
    - Geometric Dimensioning and Tolerancing: a graphical language for specifying tolerances robustly

## Design Communication

- Important to effectively describe your ideas and designs graphically
    - Persuade -- we need to be able to show are perspective
    - Instruct -- we need an agreed an unambiguous way to communicate
    - Document -- we need to convey how to construct our final design 
    - Seek feedback -- we need to ensure everyone is on the same page
- Drawings can be 2D or 3D representations
    - Interpreting 2D drawings made by others
    - Creating 2D “working drawings” with unambiguous instructions
- Design communication is not only graphical
    - Oral, written
    - Manufacturing relies on teams
    - Teaming activities 


# 1-20: Tolerancing principles

- See [why we study tolerancing](1.md#tolerance) from yesterday's notes. tl;dr: 

> Tolerancing is the practice of specifying the acceptable range of values of a component’s physical parameter, such as a dimension. We need dimensional tolerancing to: 
> 1. Ensure that components will fit together satisfactorily in a vast majority of cases, and  
> 2. Communicate to manufacturers of the individual components how much effort they need to put into controlling dimensional variability, so that function is achieved without unnecessary cost. 

## Basic tolerancing

### Tolerance formats

> Conventionally toleranced dimensions define two values between which the size of a feature is allowed to lie. The range is often referred to as the 'tolerance', 'tolerance zone' or 'tolerance band'. Several formats can be used to write the toleranced dimension: 

1. Unilateral
   - e.g. Inches: .$.500^{+0.005}_{-0.000}$, Metric: .$35^{+0.05}_0$ (notice [sigfig](https://en.wikipedia.org/wiki/Significant_figures) notation)
2. Bilateral
   - Most common; start with nominal then you have some tolerance bounds above and below
   - Equal or unequal deviations from nominal dimension 
   - Same number of decimal places for upper and lower limits
   - e.g. Inches: .$.500 \pm .005$ or .$.500^{+0.005}_{-.010}$, Metric: .$35 \pm 0.05$ or .$35^{+0.05} _{-0.10}$
3. Limit
   - Given only bounds, not the nominal value
   - e.g. Inches: .$.250, .248$, Metric: .$35.05, 35.00$

### Tolerance buildup

> Some dimensions are more critical than others for the operation of a component. It is important that  these are directly toleranced so that they lie within required limits without imposing unduly tight tolerances on other dimensions.

- In the real world we have error, so the way we define dimensions have an impact
- Best dimensions to label depend on function
    - That is, dimensioning should be done intentionally such that _critical_ distances result in minimal error, 
    - e.g.suppose distance between .$X$ and .$Y$ is critical

{{< hint "info" >}}<!-- mathjax fix -->
![Side Projection](/docs/e-29/0/buildup.png)
- Chain is bad since the potential (and often times real world) maximum error is large
    - The errors compound since dimensions are in reference to other dimensions that ~~may~~ will contain error.
    - The more dimensions chained, the greater the possible error
- Baseline is better -- every feature references a single base. 
    - However the worst case is still significant 
    - .$X$ may be off by .$\pm .05$ and .$Y$ may be off .$\mp 05$, compounding to .$\pm 0.10$!
- Direct is ideal 
    - Depends on which dimensions are critical (that is, .$X, Y$)
{{< /hint >}}


## Relationship between tolerance and process

- Manufacturing processes have inherent variability that is a characteristic of the process and can come  from various sources 
    - e.g. operator error, uncontrolled thermal contraction, tool wear, material property  variability, or startup effects such as in injection molding machines
- This variability can be modeled statistically (often as a normal/Gaussian distribution, although other distributions may be a better fit for some processes). 
    - If the variability is Gaussian, it can be characterized by the stdiv .$\sigma$ of the distribution. 
    - The larger the ratio of the standard deviation to the tolerance, the more components will lie outside acceptable values and the more will have to be scrapped or re-worked. 
    - The **process capability** is the dimensionless ratio of the tolerance to .$6\sigma$

{{< columns >}}<!-- mathjax fix -->
- Tighter tolerances (closer tolerance limits) are generally more expensive to achieve
- The physics of **the process used determines the curve's characteristics**
    - .$\sigma$ is the [stdiv](https://en.wikipedia.org/wiki/Standard_deviation) (width) of this density
- .$\mu = x_0$ is the target (average) value we give
- This probability density characterizes how this function is distributed and the chance a given range of values occur 
    - The area under the curve in a given range is the probability the value falls within that range
    - Single values, i.e .$x_0$, have a 0% probability. We can only calculate ranges because this is a **density function**.
<---><!-- mathjax fix -->
> ![Distribution](/docs/e-29/0/distribution.png)
> Probability density, e.g. given by [Gaussian/Normal probability density function](https://en.wikipedia.org/wiki/Gaussian_function): 
> $$p(x) = \frac{1}{\sigma \sqrt{2\pi}}e^{-\frac{(x-x_0)^2}{2\sigma^2}}$$
{{< /columns >}}

- Why do we care about statistics?
    - We want to look at a process, look at tolerances, and figure out whether it's worth to manufacture using this process
    - If you know the distribution of a process, you can work out the probability a given part satisfies spec limits.
- There is no easy, exact analytical way to integrate the normal probability density function.
    - The probability that a randomly chosen member of a normally distributed population has a value .$\leq x$ is
    $$\int_{-\infty}^x p(x)\ dx = P(x) = Z\bigg(\frac{x-\mu}{\sigma}\bigg) = \frac{1}{2}\bigg[1 + \text{erf}\bigg(\frac{x-\mu}{\sigma\sqrt{2}}\bigg)\bigg]$$ 
      - .$\text{erf()}$ is the error function
      - .$Z$ is the [normal cumulative distribution function](https://en.wikipedia.org/wiki/Cumulative_distribution_function); values of .$Z$ are [tabulated in a Z table](https://en.wikipedia.org/wiki/Standard_normal_table)

{{< expand "Example probability of part lying between within spec limits" >}}
![Distribution Example](/docs/e-29/0/dist-ex.png)
{{< /expand >}}


### Process capability and tolerancing

- Sigma, .$\sigma$, is the standard deviation of dimensions actually produced by a process
- [Six sigma processes](https://en.wikipedia.org/wiki/Six_Sigma)
    > Six Sigma (6σ) is a set of techniques and tools for process improvement. [...] A six sigma process is one in which 99.99966% of all opportunities to produce some feature of a part are statistically expected to be free of defects. 
    - Specification limits are .$12\sigma$ apart. Here, 2 parts per billion lie outside specification limits if process is 'in control' (i.e. if mean output of process is centered between specification limits)
    - Arose because the cost of manufacturing, specifically the process that creates an error, has a cost. This cost can grow very large, very quickly, when mass-manufacturing. 
        - You're best off spending money improving the process so the distribution gets tighter 
        - The alternative is either (1) accepting errors (resulting in faulty products) or (2) testing all components to ensure they are 'good' and tossing out the bad ones
    - Process capability: .$C_p = \frac{\text{USL - LSL}}{6\sigma}$
    - Controlling processes to six-sigma levels is now commonplace in precision manufacturing. 
- **Processes can drift over time**, meaning that its mean output can shift. 
    - If it does so, a larger proportion of components will fall out of tolerance. 
    - Process variability (i.e. .$\sigma$) can also change, and if it increases, more components will also fail to meet specifications. 
    - Under either of these circumstances the process would be described as out of control. 
    - To know whether a process is in control, we do not necessarily have to measure every single manufactured component; rather, we can periodically sample the output of the process and infer the process mean and variance from these samples.  

## Classes of Fit

> When components fit together we usually have some requirement for how easily they need to be able to move relative to each other. The American National Standards Institution (ANSI) has defined a series of grades of fit for which tolerance zone sizes are specified in tables, and which are designed for specific applications. These grades and their associated tolerance zones are described and illustrated in the slides. 

- Tolerances should be...
    - Not too tight: tight tolerances are expensive
    - Not too loose: otherwise function is compromised

{{< hint "info" >}}<!-- mathjax fix -->
![Zones](/docs/e-29/0/zones.png)

1. **Clearance fit:** designed with space left between two components
    - e.g. a piston in a cylinder, or a bolt passing through a hole
    - In this case, a finite space must be left between the components, wherever their manufactured dimensions lie in their tolerance zones. 
2. **Interference (push) fit:** designed to be touching
    - You may want interference because you want the friction between the components; you want the two pieces to not move/rotate/etc
    - This type of fit can be used to achieve precise relative positioning and hold components together
    - How? Elastic or even plastic deformation. This leads to the components exert load on each other, resisting relative motion
    - e.g. two pieces may need to fit tightly with friction as to prevent vibrations, or Lego bricks clicking together
    - **Expansion fit:**
        - If there are large forces/torques acting on these two components so you want them **very tight**
            - e.g. fitting a cutting tool into a collet for a machine tool, or a gear on to a drive shaft
        - You may temporarily expand one component (e.x. with heat) to fit on/around the other, then it will shrink down
    - **Shrink fit:**
        - Same as expansion, but using some cooling process (e.x. liquid nitrogen)
        - Why do this over heat? 
            - It's typically more expensive to cool down
            - The material may deform / weaken; e.g. steel may be degraded if heated up, [annealing](https://en.wikipedia.org/wiki/Annealing_(materials_science)) may occur
    - Shrink/expansion fits fit enables a tight fit to be achieved without applying large loads/impulses to the components (e.g. with a hammer) to get them to mate. Thus, the risk of component damage can be reduced compared to a simple force fit
3. **Transition fit:** complete interchangeability is compromised to allow looser tolerance on individual components.
    - That is, the tolerance zones of the two components _partially overlap_, so that depending on where particular components lie in their tolerance zones, the fit could be either clearance or interference. 
    - If fit type is not critical.
    - But even then, why not choose one or the other? Because you don't want a large gap and the materials/parts cannot withstand the force needed to assemble them with an interference fit. 
    - The pieces are just for alignment -- think Ikea assembly pegs; they're just to align components. 
    - It's easier to manufacture these parts
{{< /hint >}}

4. **Snap fits:**
{{< columns >}}<!-- mathjax fix -->
- Involves temporary elastic deflection which enables parts to interlock, e.g. involving bending of one component
- Done often with molded parts
- Tends to involve Cantilever (e.g. casings), Annular (e.g. pen lids, take-out soup container lids)
<---><!-- mathjax fix -->
![Snap](/docs/e-29/0/snap.png)
{{< /columns >}}
    - Designed to be assembled once, and typically not disassembled (multiple times) -- irreversible. 
    - Relatively simple: you don't need screws/glues/etc. -- useful for rapid prototyping since you don't have to consider fasteners
    - Takes advantage of the fact that the material has some elasticity
        - You need to stay within the elasticity limits of the material
        - Most 3D plastics have 'enough' give
        - You (generally) want to design such that the stress is from bending, not stretching
    - [More](https://coloringchaos.github.io/form-fall-16/joints), [additional](https://www.pinterest.com/Gilson_Design/), [extra](https://www.hubs.com/knowledge-base/how-design-snap-fit-joints-3d-printing/), [readings](https://productdesignonline.com/wp-content/uploads/2019/08/Snap-Fit-Design-Manual.pdf)


### Terminology Definitions

> Don't stress about memorizing these !

{{< hint "info" >}}<!-- mathjax fix -->
![Clearance and interference fits](/docs/e-29/0/fit-ex.png)
- **Maximum material condition _(MMC)_:** The greatest allowable amount of material left on the part (max size for a shaft; min size for a hole)
- **Minimum/least material condition _(LMC)_:** The least allowable amount of material left on the part (min size for a shaft; max size for a hole)
    - Important with MMC since they tell us how much they're able to 'slosh around'
- **Basic size:** Exact theoretical size from which limits are derived 
    - Different form nominal since basic refers to the standard table which gives respective upper and lower bounds (MMC and LMCs)
    - Hole basis: Basic size is minimum size of hole
    - Shaft basis: Basic size is maximum size of shaft -- used when many components need to fit on to one shaft.
    - Basic size could be chosen to be in-between hole and shaft basis
- **Tolerance:** Allowable variation of one particular dimension
- **Fundamental deviation:** Difference between basic size and the closer of the MMC and LMC
- **Allowance:** Difference between maximum material conditions of the two components
{{< /hint >}}


### Types of fit

- These types are created by ANSI: American National Standards Institute
- Exact values are tabulated in many source

---
- RC: Running and sliding clearance fits
    - Nine categories:
        - RC1: Close sliding: assemble without perceptible “play” (e.g. watches) 
            - Less than a 1/1000". 
            - Basically impossible for air, let alone liquids, through. 
        - RC2: Sliding fits: seize with small temperature changes (e.g. )
        - RC3: Precision running: not suitable for appreciable temperature differences
        - RC4: Close running: moderate surface speeds and pressures
        - RC5/6: Medium running: higher speed/pressure
        - RC7: Free running: where accuracy not essential and/or temperature variations large
        - RC8/9: Loose running
  - Go for lower if you want minimal vibration/gaps -- no perceivable play. 
  - Has drawbacks: 
      - The less clearance, the easier it is to seize up -- especially if two components are touching and made up of different materials (different expansion/contraction rates).
      - Susceptible to dust, you would have to seal the machine or use it in clean conditions.
  - If you go less precise, you don't need to go slow, cheaper operator costs, cheaper tooling
  - {{< expand "RC Chart" >}}
![RC fits -- from Machinery’s Handbook, Industrial Press](/docs/e-29/0/rc.png)
  {{< /expand >}}
  - {{< expand "RC Table" >}}
![Table](/docs/e-29/0/rc-table.png)
  {{< /expand >}}
- LC: Locational clearance fits
    - Normally stationary, but freely assembled/disassembled
    - Used when you need clearance to dis able and clean
    - {{< expand "LC Chart" >}}
![Classes of LC fit](/docs/e-29/0/lc.png)
    {{< /expand >}}

{{< columns >}}<!-- mathjax fix -->
- LT: Location transition fits
    - Accuracy of location important
    - Small amount of clearance or interference OK
    - e.g. ikea furniture pegs
- LN: Locational interference
    - When you need friction
    - Accuracy of location is critical
<---><!-- mathjax fix -->
![Other classes of fit](/docs/e-29/0/misc-fits.png)
{{< /columns >}}
- FN: Force fits
    - When you need to hold a load (typically uses temporary heating)
    - Designed to transmit frictional loads from one part to another

{{< expand "Example: Which type of fit?" >}}
![](/docs/e-29/0/ex-fit.png)
{{< /expand >}}


## Process selection

- How do we relate physical processes and tools to these values?
- A manufacturing process needs to be chosen carefully based on its inherent variability, the required tolerance, and the cost of scrapping or re-working.
> {{< figure  src="/docs/e-29/0/processes-tol.png" >}}
> From _MF Ashby, Materials Selection in Mechanical Design_

### Roughness

- In some cases, the average value of a dimension (e.g. the diameter of a turned shaft) might be tightly controlled by a skilled operator, but the roughness (variability of surface position within a feature) might still be considerable (e.g. because of machine vibration) and could introduce additional dimensional variability. 
    - This variability could adversely affect our ability to achieve a desired fit!
- So, how do we define roughness? You may use tool that uses a tiny needle to 'scan' the surface, measuring deflections as you go
> {{< figure  src="/docs/e-29/0/roughness.png" >}}
> From _MF Ashby, Materials Selection in Mechanical Design_
- **RMS roughness:** root mean square of deviations over the measured surface length
    - i.e.: .$R^2 = L^{-1} \int_0^L y^2\ dx$
    - Usually, tolerance, .$T$, lies between 5R and 1000R
    - The RMS is a simple and useful metric although it gives no information about the lateral length scales of any roughness.
- The rule-of-thumb is that the **surface roughness should be no more than about 20% of the tolerance zone**, and ideally 
considerably less than that. 
- Generally, if you go high rotation speed and slow translational speed you get less rough surfaces




