---
title: "Trig Calculus"
weight: 100
---

# Derivatives

$$\frac{d}{dx} \tan(x) = 1 + \tan^2(x) = \sec^2(x)$$
$$\frac{d}{dx} \csc(x) = -\cot(x) \cdot \csc(x)$$
$$\frac{d}{dx} \sec(x) = \frac{\sin(x)}{\cos^2(x)} = \tan(x) \cdot \sec(x)$$
$$\frac{d}{dx} \cot(x) = -\csc^2(x)$$
$$\frac{d}{dx} \log_a(x) = \frac{1}{x\cdot \ln(a)}$$
$$\frac{d}{dx} a^u = a^x \cdot \ln (a) du$$
$$\frac{d}{dx} \sin^2(x) = \sin(2x)$$
$$\frac{d}{dx} \cos^2(x) = -\sin(2x)$$
$$\frac{d}{dx} \tan^2(x) = 2\tan(x)\cdot \sec^2(x)$$
<!-- $$\frac{d}{dx} $$ -->

# Integrals

$$\int a^x dx = \bigg(\frac{1}{\ln(a)}\bigg) a^x + C $$
$$\int \tan(x) dx = -\ln\vert \cos(x) \vert + C$$
$$\int \tan^2(x) dx = \tan(x) - x + C$$
$$\int \csc(x) dx = \ln\vert \csc(x) - \cot(x)\vert + C = \ln \bigg\vert \tan\bigg(\frac{x}{2}\bigg)\bigg\vert + C$$
$$\int \csc^2(x) dx = -\cot(x) + C$$
$$\int \sec(x) dx = -\ln\vert \sec(x) + \tan(x)\vert + C$$
$$\int \sec^2(x) dx = \tan(x) + C$$
$$\int \cot(x) dx = \ln\vert \sin(x) \vert + C$$
$$\int \cot^2(x) dx = -\cot(x) - x + C$$
$$\int \frac{1}{\sin(ax)\cos(ax)} = \frac{1}{a} \ln\vert\tan(ax)\vert + C$$
$$\int \frac{1}{x\sqrt{x^2-a^2}} dx = \frac{1}{a} \sec^{-1}\bigg( \frac{\vert x \vert}{a}\bigg) + C$$
$$\int \frac{1}{\sqrt{a^2-x^2}} dx = \sin^{-1}\bigg( \frac{x}{a} \bigg) + C$$
$$\int \frac{1}{a^2 + x^2} dx = \frac{1}{a} \tan^{-1}\bigg( \frac{x}{a} \bigg) + C$$

[Many more integrals](https://en.wikipedia.org/wiki/List_of_integrals_of_trigonometric_functions)

# Triangle Sub

$$\sqrt{b^2x^2-a^2} \Longrightarrow x = \frac{a}{b}\cdot\sec\theta; \theta \in \[0, \pi/2), (\pi/2, \pi\]$$
$$\sqrt{a^2-b^2x^2} \Longrightarrow x = \frac{a}{b}\cdot\sin\theta; \theta \in \[-\pi/2, \pi/2\]$$
$$\sqrt{a^2+b^2x^2} \Longrightarrow x = \frac{a}{b}\cdot\tan\theta; \theta \in \(-\pi/2, \pi/2\)$$

