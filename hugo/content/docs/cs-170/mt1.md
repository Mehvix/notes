---
title: "Midterm 1: Cheat Sheet"
---

{{< katex />}}

# Asymptotic Bound
{{< columns >}}<!-- mathjax fix -->
| Notation              | Meaning | Definition                                          |
| --------------------- | ------- | --------------------------------------------------- |
| $$\mathcal O(\cdot)$$ | $$\le$$ | $$\lim_{n \to \infty} \dfrac{f(n)}{g(n)} < \infty$$ |
| $$\Theta (\cdot)$$    | $$=$$   | $$\lim_{n \to \infty} \dfrac{f(n)}{g(n)} = c$$      |
| $$\Omega(\cdot)$$     | $$\ge$$ | $$\lim_{n \to \infty} \dfrac{f(n)}{g(n)}> 0$$       |
<---><!-- mathjax fix -->
$$\begin{aligned}
c &< \log^\star n \\\
&< \log n \\\
&< n^{1/3}\\\
&< n^{1/2} = \sqrt n\\\
&< 2^{\log{n}} = n\\\
&< n \log (n) = \log(n!) \\\
&< n^3\\\
&< 2^{\sqrt{n}}\\\
&< 2^n\\\
&< 3^n\\\
&< n!
\end{aligned}$$
{{< /columns >}}


## Master Theorem
$$\begin{aligned}
T(n) &= \overbrace{a\cdot T\left(\frac n b\right)}^\text{Divide into $a$ parts $\sim\  b^{-1}$} + \overbrace{C \cdot n^d}^{\text{Combining Work}} \\\
\text{Level 0: } & n^d \\\
\text{Level 1: } & n^d \frac a {b^d} \\\
\text{Level 2: } & n^d \left(\frac a {b^d}\right)^2
\\\ & \vdots \\\
\text{Level }k:\ & n^d \left(\frac a {b^d}\right)^k \qquad \text{(Base: } \frac n {b^k} \leq 1 \Longrightarrow k = \log_b n)\\\
\text{Total Work:}\ & n^d \cdot \sum_{i=0}^k \left(\frac a {b^d}\right)^i
\\\
\therefore\ T(n) &=
\begin{cases}
\Theta (n^d) & \dfrac a {b^d} < 1\ \equiv\ d>\log_b a\\\
\Theta (n^d \cdot \log n) & \dfrac a {b^d} = 1\ \equiv\ d= \log_b a \\\
\Theta (n^{\log_b a}) & \dfrac a {b^d} > 1\ \equiv\ d < \log_b a
\end{cases}
\end{aligned}$$

{{< details "Case Derivations" >}}
{{< columns >}}<!-- mathjax fix -->
### Case 1:
Geometric decaying sum, first term dominates
$$\begin{aligned}
& n^d \cdot \sum_{i=0}^k \left(\frac a {b^d}\right)^i \text{ with }  p= \dfrac a {b^d} < 1  \\\
&= n^d \cdot (1 +p+\dots+p^k) \\\
&=\ n^d \cdot \left(\frac{p^{k+1}-1}{p-1} \right)\\\
&= \Theta (n^d)
\end{aligned}$$
<---><!-- mathjax fix -->
### Case 2:
Same work at all levels
$$\begin{aligned}
& n^d \cdot \sum_{i=0}^k \left(\frac a {b^d}\right)^i \text{ with }  p= \dfrac a {b^d} = 1  \\\
 &= n^d \cdot (1^0 +1^1+\dots+1^k)) \text{ with } k=\log_b n  \\\
 &= n^d \cdot (k+1) \\\
 &= n^d \cdot (\log_bn + 1)\\\
&= \Theta (n^d \log n)
\end{aligned}$$
{{< /columns >}}
### Case 3:
Geometric growing sum, leafs dominate
$$\begin{aligned}
& n^d \cdot \sum_{i=0}^k \left(\frac a {b^d}\right)^i \text{ with }  p= \dfrac a {b^d} > 1  \\\
&= n^d \cdot (1 +p+\dots+p^k) \\\
&=\ n^d \cdot \left(\frac{p^{k+1}-1}{p-1} \right) \\\
&=\ \Theta \left(n^d \cdot \left(\frac{p^{k+1}-1}{1} \right)\right) \\\
&=\ \Theta \left(n^d \cdot p^{k+1}\right)  \\\
&=\ \Theta \left(n^d \cdot \left(\frac a {b^d}\right)^{k}\right) \\\
&=\ \Theta \left(n^d \cdot \left(\frac a {b^d}\right)^{\log_b n}\right) \\\
&=\ \Theta \left(n^d \cdot \left(b^{\log_b\left(\dfrac a {b^d}\right)}\right)^{\log_b n}\right) \\\
&=\ \Theta \left(n^d \cdot \left(b^{\log_b n}\right)^{\log_b\left(\dfrac a {b^d}\right)}\right)  \\\
&=\ \Theta \left(n^d \cdot n^{\log_b\left(\dfrac a {b^d}\right)}\right) \\\
&=\ \Theta \left(n^d \cdot (n^{\log_b a - \log_b b^d})\right) \\\
&=\ \Theta \left(n^d \cdot (n^{\log_b a - d})\right) \\\
&= \Theta\ (n^{\log_b a})
\end{aligned}$$
{{< /details >}}

# Representation

* $1 + p + p^2 + \cdots + p^k = \dfrac{p^{k+1}-1}{p-1}$
* Log facts
    * Change log base: $\log_b N = \dfrac{\log_a N}{\log_a b} \implies \log_a N = \log_b N \cdot \log_a b$
    * Represent $x$ using $\log$ of an arbitrary base: $x = b^{\log_b x}$
    * Expanding log division: $\log_a \left(\dfrac{x}{y}\right) = \log_a x - \log_a y$
    * Definitions:
        1. The power to which you need to raise 2 in order to obtain $N$
        2. Going backward, it can also be seen as the number of times you must halve N to get down to 1: $\lceil \log N \rceil$
        3. Number of bits in the binary representation of N: $\lceil \log(N+1)\rceil$
        4. Depth of a complete binary tree with N nodes: $\lfloor \log N \rfloor$
        5. $1 + \frac 1 2 + \frac 1 3 + \cdots + \frac 1 N = \ln N + \gamma$
    * Show $\log (n!) = \Theta (n \log n)$
        >{{< columns >}}<!-- mathjax fix -->
Upper:
$$\begin{aligned}n! &< n^n\\\ \log n! &< \log n^n \\\ &=\mathcal O (\log n^n) \\\ &=\mathcal O(n \log n) \end{aligned}$$
<---><!-- mathjax fix -->
Lower:
$$\begin{aligned}n! &> \frac n 2 ^{\frac n 2}\\\
\log n! &> \log (\frac n 2 ^{\frac n 2})\\\
&=\Omega \left(\frac n 2 \log \frac n 2 \right)\\\
&= \Omega (n \log n)\end{aligned}$$
{{< /columns >}}

* Fast Integer exponentiation using repeated squaring
    * Naive takes $\mathcal O(n)$ multiplies: $k^{n} = n\cdot n\cdot \dots n$
    * Base-2 decomp takes $\mathcal O(\lceil\log_2 k\rceil)$:
        * E.x. $k=71: 9^{71} = 9^{64} \cdot9^4\cdot9^2\cdot 9^1$
        * Use base-2 since $\log_{b} x = \log_{2} x / \log_{2} b$ is minimized when $b=2$.
* Show that in any base $b\ge 2$, the sum of any three single-digit numbers is at most two digits long.
    >$$\begin{aligned}
    \text{[sum of 3 digits in base b]} &\leq \text{[2-digit number]}\\\
    \text{argmax } x_b + y_b + z_b &\leq b\cdot\alpha + \beta\\\
    3(b-1) &\leq b^2-1 \qquad(1)\\\
    \text{Base:}\qquad\quad 3(2-1)&\leq 2^2 -1\\\
    3 &\leq 3\ \Box \\\
    \text{Hyp: }\quad3(k+1-1)&\leq (k+1)^2 -1\\\
    3k&\leq k^2+2k\\\
    k &\leq k^2\ \Box
    \end{aligned}$$
    > * $(1)$: $k$ digits in base $b$ can represent every number in  $[0, b^k) \equiv [b^k-1]$
* Show that any binary integer is at most four times as long as the corresponding decimal integer.
    > For any decimal (base-10) integer $x$ of length $n$, we know the number of bits to represent in base $b$ is $\lceil \log_b 10^n\rceil$; therefore...
    > $$\begin{aligned}
    \text{[length in base-2]}   &\leq 4\cdot \text{[length in base-10]}\\\
    \lceil \log_2 (x+1) \rceil  &\leq 4\cdot \lceil \log_{10} (x+1) \rceil\\\
    \log_2 10^n                 &\leq 4\cdot \log_{10} 10^n\\\
                                &\leq 4\cdot n\\\
    2^{\log_2 10^n}&\leq 2^{4\cdot n}\\\
    10^n                        &\leq 16^n\ \Box\end{aligned}$$
* Show that any d-ary tree with n nodes must have a depth of $Ω(\log n/ \log d)$
    > $$\begin{aligned}
    n           &= \sum_{i=1}^f d^i = d^1 + d^2+\dots+d^f\\\
                &= d^f-1\\\
    \log_d n+1  &= \log_d d^f\\\
    \log_dn+1   &= f\\\
    \Longrightarrow f &= \lfloor\log_d n\rfloor \\\
                &= \Omega \frac{\log n}{\log d}\end{aligned}$$


|            Operation            |    Adjacency Matrix     |               Adjacency List               |                       Notes                        |
| :-----------------------------: | :---------------------: | :----------------------------------------: | :------------------------------------------------: |
|             Memory              | $\mathcal O(n^2)$ bytes | $\mathcal O(n+m)$ machine words (pointers) |              Matrix better when dense              |
| Checking if edge $(u,v)$ exists |     $\mathcal O(1)$     |            $\mathcal O(d_u +1)$            |                                                    |
| Iterating all neighbors of $u$  |     $\mathcal O(n)$     |            $\mathcal O(d_u+1)$             |                                                    |
|               BFS               |    $\mathcal O(n^2)$    |             $\mathcal O(n+m)$              | Iterate over each neighbors (row) for all elements |


# Fast Fourier Transform (FFT)

> **Goal:** efficiently multiply two polynomials $A(x), B(x)$, of degrees $d_a, d_b$, in $\mathcal O(n\log n)$ time
1. **Selection:** Find points (roots of unity) $x_0, x_1, \dots, x_{n-1}$
    * $n = 2^{\lceil \log_2 (d_a + d_b + 1) \rceil} \le 2^{\lceil \log_2 (2d + 1) \rceil} $ where $d := \text{max}(d_a, d_b)$
        * Final polynomial $C(x)$ has maximum degree of $2d$, so we evaluate at $2d+1$ points
    * Zero-pad $A(x), B(x)$ with $n - d_a, n-d_b$ zeros respectively
2. **Evaluate** two polynomials at a set of points : $\mathcal O(n \log n)$
3. **Multiply** the evaluated points (for every point $w$ evaluated, compute $C(w) = A(w) \cdot B(w)$ : $\mathcal O(n)$
4. **Interpolate:** Take the resulting points and recover the polynomial they define with IFFT: $\mathcal O(n \log n)$

---

* Exam tips
    * Use FFT as a blackbox algorithm for polynomial multiplication
        * Frame problem as a polynomial problem, e.x. through cross-correlation
    * Anything better than $\mathcal O (n\log n)$ i.e. $\mathcal O(n^2)$ can be done with FFT


<!-- TODO Successive Dot Product (fa21-4) -->


# Depth First Search (DFS)


# Graph Theory

# Dijkstra

# Shortest Paths


# Divide and Conquer (D&C)



# Minimum Spanning Tree (MST)

# Bellman-Ford

# Huffman Encoding

# Union Find

# Quickselect










