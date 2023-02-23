---
layout: default
parent: Course Content
title: Recommended Problems
nav_order: 6.5
---

## Recommended Problems

### Problem 1

Find the splitting fields of the following polynomials over $\Q$:

#### a. $x^4-2$

Hints:

- irreducible by Eisenstein
- $\Q(\sqrt[4]{2})$ is real of degree $4$.
- If $\alpha=\sqrt[4]{2}$, then the four roots are $\pm \alpha$, $\pm i\alpha$.

#### b. $x^4+2$

Hints:

- irreducible by Eisenstein
- If $\alpha=\sqrt[4]{-2}$, then the four roots are $\pm \alpha$, $\pm i\alpha$.
- The square root of $i$ is $e^{\pi/4}=\sqrt{2}/2+i\sqrt{2}/2$, so in fact $\Q(\sqrt[4]{2})$ is in $\Q(i,\alpha)$.

#### c. $x^4+x^2+1$

Hints:

- If $\alpha$ is a root of this polynomial, then $\alpha^2$ is a root of $x^2+x+1=0$ and the roots of this polynomial are

  $$
  \frac{-1\pm\sqrt{-3}}{2}=e^{\pm 2\pi i/3}.
  $$

#### d. $x^6-4$

Hints:

- this polynomial is $(x^3-2)(x^3+2)$.

### Problem 2 (DF, Problem 6, page 545)

Prove that, if $K_1/F$ and $K_2/F$ are splitting fields, then so are the composite $K_1K_2$ and the intersection
$K_1\cap K_2$.
