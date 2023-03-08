---
layout: default
title: 8. Galois Theory Examples and Applications
nav_order: 8.0
parent: Course Content
---

## Examples and Applications

A few additional remarks on Galois Theory.

### The "general polynomial"

The polynomial $F_{n}(T)=(T-x_1)\cdots (T-x_n)$, where the $x_i$ are indeterminants, is called the general polynomial of degree $n$.
The group $S_{n}$ permutes the $x_{i}$ and acts as automorphisms of the field $E(x_1,\ldots, x_n)$ where $E$ is any field.

The coefficients of $F_{n}(T)$ are, up to sign, the elementary symmetric functions $s_{i}$ of the roots $x_{i}$. Therefore
the field $E(s_1,\ldots, s_n)$ is contained in the fixed field of $S_{n}$ on $E(x_1,\ldots, x_n)$. Therefore $[E(x_1,\ldots, x_n):E(s_1,\ldots, s_n)]\ge n!$.

On the other hand, $E(x_1,\ldots, x_n)$ is the splitting field of $F_{n}(T)$ over $E(s_1,\ldots, s_n)$. Therefore $[E(x_1,\ldots, x_n):E(s_1,\ldots, s_n)]\le n!$.

Thus the galois group of this extension is $S_{n}$.

In particular any symmetric function in the roots of a polynomial can be written in terms of the coefficients of the polynomial.

### The discriminant

The discriminant of a polynomial is the product of the differences of its distinct roots squared:

$$
\Delta=\prod_{i<j} (x_{i}-x_{j})^2
$$

It is a symmetric function of the roots.

If $\Delta$ is a square, then the galois group of the polynomial is contained in the alternating group.

<div>
<a href="slides/08-examplesAndapplications.html"> View as slides </a>
</div>
