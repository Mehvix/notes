---
title: "Main"
---

{{< katex />}}

# 08-28: Capturing Light... in man and machine

- Etymology
    - Photo means light
    - Graphy means drawing/writing
- We take many samples of an image, typically in `[0, 255]`
    - [Rolling shutter](http://en.wikipedia.org/wiki/Rolling_shutter) occurs when some object is moving noticeably faster than the sampling rate
    - Pictures are not a single instance

## The Eye
- **Saccadic eye movement**: Unlike an image, we see everything except what we're looking at is blurred
- **Iris**: colored annulus with radial muscles
- **Pupil**: the hole (aperture) whose size is controlled by the iris
- Photoreceptor cells (rods and cones) in the **retina** act as the 'film'
    - Inside-out retina (in humans, and most other animals) is messy:
        - Light has to pass through various layers of 'wiring'
        - Optical nerve produces blind spot (no rods or cones)
    - Two types of light-sensitive receptors:
        1. Cones
            - cone-shaped
            - less sensitive
            - operate in high light
            - color vision
            - concentrated in the **fovea** (center of the retina)
        2. Rods
            - rod-shaped
            - highly sensitive
            - operate at night
            - gray-scale vision
            - concentrated in the periphery of the retina
            > When looking at the night sky, you will be able to see more out of the corner of your eye because that's where there are more rods-- cones do very little to help you see the light from the stars.

## Physics of Light
- We can see 400-700 nanometers (visible light on the electromagnetic spectrum)
    - This is the range that the Sun radiates
- Color is psychophysical: it's a property of the brain, not the light
- Any patch of light can be completely described physically by its spectrum: the number of photons (per time unit) at each wavelength from 400 to 700 nm.
- The perceived color of an object corresponds to the spectrum of light that it reflects.
    - Small (blue), Medium (green), Large (red) cones then 'parse' the spectrum into color
        - M and L (green and red) are close to one another

## Color Vision

- Colorblind (not trichromatic) people have a different set of cones
    - Deuteranopia: green-blind, missing M cones
    - Protanopia: red-blind, missing L cones
    - Tritanopia: blue-blind, missing S cones
- “M” and “L” on the X-chromosome
    - Why men are more likely to be color blind
    - “L” has high variation, so some women are tetrachromatic
- Some animals have
    - 1 (night animals)
    - 2 (e.g., dogs)
    - 4 (fish, birds)
    - 5 (pigeons, some reptiles/amphibians)
    - 12 (mantis shrimp)
---
- Rods an cones act as a filter on the spectrum:
    > The “photometer metaphor” of color perception: Color perception is determined by the spectrum of light on each retinal receptor (as measured by a photometer
    - We can approximate the spectrum with a linear combination of the three cone responses
        - Most of the information is lost
    - As a result, two different spectra may appear indistinguishable
        - such spectra are known as **metamers**
- Distribution of color can be interpreted as...
    - Mean corresponds to the hue
    - Variance corresponds to the saturation
    - Area corresponds to the brightness
- **Color Constancy**: the ability to perceive the invariant color of a surface despite ecological Variations in the conditions of observation.
- Another of these hard **inverse problems**: Physics of light emission and surface reflection *underdetermine* perception of surface color

## Cameras

- White balancing
    - Manual
        - Choose color-neutral object to normalize
    - Automatic (AWB)
        - Grey world: force average color of scene to grey
        - White world: force brightest object to white
- Our eyes are most sensitive to green light, so we often have more green sensors (ex. [Bayer Filter](http://en.wikipedia.org/wiki/Bayer_filter))
- Storing values in a matrix; `x` corresponds to the columns and `y` corresponds to the rows

## Color Spaces
- RGB -- additive (light)
    - Easy for devices
    - But not perceptually uniform
        - Where do the grays live?
        - Where is hue and saturation?`
- CMYK (Cyan, Magenta, Yellow, Key) -- subtractive (ink)
    - Used in printing/painting
    - White is the background; black is the additive value of all colors
- HSV (Hue, Saturation, Value) -- cylindrical
    - Hue (kind of color) is the angle
        - Red: 0
        - Green: 120
        - Blue: 240
    - Saturation (purity) is the distance from the center
    - Value (lightness) is the total amount of light
- Lab (Luminance, a, b) -- perceptually uniform
    - Luminance is the amount of light
        - Humans are much more sensitive to changes L
    - a corresponds to red to green
    - b corresponds to blue to yellow

# 09-07: Convolution and Image Derivatives

* When calculating the moving average, it's smart to apply non-uniform weights (e.x gaussian) to account for outliers
    * $\sigma$ (std) determines the extent of smoothing
        * $\sigma \to 0$: more concentrated, single pixel (no smoothing)
        * $\sigma \to \infty$: box filter (blurry image)
    * Kernel (size of rectangle) should be $\approx 3 \sigma$
        * Too big: extra 1-weight around edges
        * Too small: doesn't cover full range

## Convolution

* Cross-correlation: $G = H \otimes F$
    * Signal $F$ and filter $H$
    * Not commutative (order matters)
* Convolution: $G = H \star F$
    * Commutative, associative, distributive over addition, scalars factor out
    * Associative shows us that applying multiple filters is equal to applying a single combined filter: $(((a\star b_1)\star b_2) \star b_3 \equiv a \star (b_1 \star b_2 \star b_3)$
    * Convolving with self is another Gaussian with $\sigma \sqrt 2$


## Downsampling

* Subsampling: lazy way of downsampling
    * Removes every other row/cols of pixels
    * Leads to ugly aliasing
* Undersampling: Occurs when too few samples taken
* Gaussian (lowpass) pre-filtering
    * Solution: filter (blur) the image then resample
        * Filter size should double for each 1/2 size reduction
        * Applying a blur filter is also smart when taking the gradient of an image
    * Image pyramids can also be implement to speed up process



# 9-12: The Frequency Domain

* Humans have a wacky non-linear/predictable perception of spatial frequencies
    * [Campbell-Robson contrast sensitivity curve](https://www.frontiersin.org/articles/10.3389/fnins.2021.626466/full#:~:text=The%20Campbell%2DRobson%20chart%20is%20a%20highly%20popular%20figure%20used,contrast%20from%20bottom%20to%20top.)
    * Humans have innate antialiasing
    * Cats have a left-shifted curve (more sensitive at lower frequencies) for hunting in the dark
    * Eagles have a right-shifted curve (more sensitive at higher frequencies) for seeing prey at a distance
* We can decompose an image into it's spatial domain ($n^2$ vectors)
    * We can transform this into a series of $sin/cos$ waves composing it's own basis
    * [Jean Baptiste Joseph Fourier (1768-1830)]() said "Any univariate function can be rewritten as a weighted sum of sines and cosines of different frequencies"
    * We can compose any signal as a sum of sines and cosines
        * $f(x) = A\sin(\omega x + \phi)$
        * $\omega$ is the frequency (change in $x$ per cycle)
        * $A$ is the amplitude
        * $\phi$ is the phase, captures spatial information -- what we discard when going to 'fourier-basis'
    * We take $f(x) \to_\text{FFT} F(\omega)$
{{< columns >}}<!-- mathjax fix -->
* For every $\omega$ from 0 to inf, $F(\omega)$ holds the amplitude $A$ and phase $\phi$ of the corresponding sine:
* $F(\omega) = R(\omega) + i l(\omega)$
    * $A = \pm \sqrt{R^2 + l^2}$
    * $\phi = \tan ^{-1}\left(\dfrac{l(\omega)}{R(\omega)}\right)$
<---><!-- mathjax fix -->
![](/docs/cs-194/ft-basis.png)
{{< /columns >}}
        * Sufficient, finite $\omega$ can be stored in a lookup table $\implies$ fast + low memory and very little loss of information
        * Technically drops some information that's overlapping, but this is okay because the approximation of the range of $\omega$ is very accurate
            * So basis/representation is not necessarily unique (but it is in most cases in the wild)
        * Storing/encoding image: $M \cdot f(x) = F(\omega)$
            * $f(x)$ is the input vector of the image
            * $M$ is the matrix of sines and cosines
            * $F(\omega)$ is the representation in new $\omega$ basis
        * Decoding image: $M^{-1} \cdot F(\omega) = \hat f(x)$
            * $M^{-1}$ is the inverse of the matrix of sines and cosines
            * $F(\omega)$ is the representation in new $\omega$ basis
            * $\hat f(x)$ is the output vector of the image
        * Now store basis of $F \times N$ vectors $\implies$ space complexity is $\mathcal O (FN)$ where $N$ is the number of $\omega$ values
            * $\mathcal O (FN) \ll \mathcal O(N^2)$
            * Inverse $M^{-1}$ is easy to compute when knowing $M$

> {{< figure  src="/docs/cs-194/trim.png" >}}
> Local change in one domain, courses global change in the other

> {{< figure  src="/docs/cs-194/filter.png" >}}
>Low (top) and High (bottom) Pass filtering

* The Convolution Theorem

* The Fourier transform of the convolution of two functions is the product of their Fourier transforms
$$F[g \star h] = F[g]F[h]$$
* The inverse Fourier transform of the product of two Fourier transforms is the convolution of the two inverse Fourier transforms
$$F^{-1}[gh] = F[g]^{-1}\star F[h]^{-1}$$
{{< figure  src="/docs/cs-194/conv.png" >}}
* We can transform our FFT basis into a series of gaussian

# 09-14: Pyramid Blending, Templates, NL Filters

## Hybrid Images

* We can get the details from an image by subtracting the smoothed version of the image from the original
* Then to sharpen an image we can add a scalar of the details back in
    * This is called an unsharp mask and results in a Laplacian of Gaussian (LoG) filter
* Laplacian Pyramid: We can take multiple samples of the difference between the original and increasingly smoothed version os the image (called the octaves)
    * We can then reconstruct the original image by adding the smoothed version of the image back to the details

## Blending

* Alpha blending: We can blend two images by linearly interpolating between the two images
    * $I_{blend} = \alpha I_1 + (1 - \alpha) I_2$
        * Total sums to 1 so we have full opacity
    * Window Size
        * Ideal size is equal to the largest prominent feature, $\phi$
        * The larger the window, the more ghosting
            * Minimal ghosting when window <= 2$\cdot \phi$
        * Too small of a window is a regular crop
    * Casting in Fourier domain
        * Largest frequency <= 2*smallest frequency
        * Image frequency content should occupy one 'octave' (power of two)
        * Laplacian Pyramid: Blending
            1. Build Laplacian pyramids LA and LB from images A and B
            2. Build a Gaussian pyramid GR from selected region R
               * High frequency (first level) has fine details, small blend window
               * Low frequency (last level) has blurry figures, large blend window
            3. Form a combined pyramid LS from LA and LB using nodes of GR as weights:
               - $LS(i,j) = GR(I,j,)\cdot LA(I,j) + (1-GR(I,j))\cdot LB(I,j)$
            4. Collapse the LS pyramid to get the final blended image
    * Two-band blending:
        * Alternatively to Laplacian Pyramid, you can use high and low frequencies w/o downsmampling
        * Blends low freq smoothly
        * Blends high freq with no smoothing; use binary $\alpha$
* Huffman coding: Lossless compression
    * Generate pixel histogram
    * Then generate pixel code based how often each pixel in the histogram occurs
        * Most common colors have fewer bits
    * Maximally 2x compression -- sounds good but not significant
* JPEG compression
    * Lossy compression -- takes advantage of human vision not being able to notice high frequencies
        * Colors layers are downsampled since people have bad resolution for colors
    * Cut into 8x8 blocks (standard) and subtract 128
        * Small block: faster; correlation exists between neighboring pixels
        * Large block; better compression in smooth regions
    * For each block...
        * Compute DCT (discrete cosine transform)
        * Quantize
            * More coarsely for high frequencies (tend to have smaller values anyways)
            * Many high frequency values will be 0
            * jpeg standard specifies the quantization table
        * Encode
            * i.e. with Huffman coding
            * Can decode with inverse DCT
            * Spatial dimension of color channels are reduced by 2

## Filters

* Smoothing filters
    * Gaussian: remove “high-frequency” components; “low-pass” filter
    * Values are non-negative and sum to 1
        * Constant regions are not affected by the filter
        * Weighted average of neighboring pixels
* Derivative filters
    * Derivatives of Gaussian
    * Values can be negative and sum to 0
        * No response in constant regions
    * High absolute value at points of high contrast

----

### Application: template matching
* Find some object (sub-image) in a larger image
* What is a good similarity or distance measure between two patches?
    * Correlation
        * $h[m,n] = \sum_{i,j} g[i,j]f[m+i,n+j]$
        * $f$ is the image, $g$ is the template
        * Results in smoothing filter
    * Zero-mean correlation
        * $h[m,n] \sum_{i,j} (g[i,j] - \bar g)f([m+i,n+j])$
        * Even if we subtract the mean, we have false-positives in brighter reasons
    * Sum Square Difference
        * $h[m,n] = \sum_{i,j} (g[i,j] - f[m+i,n+j])^2$
        * Doesn't scale well with varying brightness/intensity
    * Normalized Cross Correlation
        * $h[m,n] =  \dfrac{\sum_{i,j}(g[i,j] - \bar g)(f[m+i,n+j] - \bar f_{m,n})}{\sqrt{\sum_{i,j} (g[i,j] - \bar g)^2 \sum_{i,j} (f[m+i, n+j] - \bar f_{m,n})}}$
        * Slowest, invariant to local, invariant to local average intensity/contrast
* Denoising
    * With gaussian, still preserves 'salt and pepper' noise
    * Median filter
        * Replace each pixel with median of its neighbors
        * Robust to outliers




