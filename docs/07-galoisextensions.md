---
layout: default
title: 7. Galois Extensions
nav_order: 7.0
parent: Course Content
---

## Galois Extensions

### Automorphisms

Let $K/F$ be an extension fields and let $\Aut(K/F)$ be the group of field homomorphisms $\sigma: K\to K$ which are the identity when restricted to $F$.

Some basics:

- If $\alpha\in K$ is algebraic over $F$ with minimal polynomial $p(x)$ over $F$, then $\sigma(\alpha)$ is also a root of $p(x)$.
- If $H\subset\Aut(K/F)$ is a subgroup, then the set $K^{H}=\lbrace x\in K : \sigma(x)=x\forall \sigma\in H\rbrace$ is a subfield of $K$.
- If $H_1\subset H_2$ are subgroups of $\Aut(K/F)$, then $K^{H_{2}}\subset K^{H_{1}}$.

### Galois Extensions

**Proposition:** Let $E/F$ be the splitting field over $F$ of some polynomial $f(x)\in F[x]$. Then

$$
\vert \Aut(E/F)\vert\le [E:F].
$$

If $f(x)$ is separable, then this is an equality.

**Definition:** $E/F$ is called a Galois extension if $\vert\Aut(E/F)\vert=[E:F]$. In this case the automorphism
group is called the _Galois group_ of the extension.

Proposition 5 says that separable splitting fields are Galois extensions.

### The Galois correspondence

Let $E/F$ be a Galois extension with Galois group $G$. Then there is a bijective (inclusion reversing) correspondence
between:

- subfields $L$ of $E$ containing $F$
- subgroups of $G$

The correspondence is given by $H\to E^{H}$ for $H\subset G$ in one direction, and $L\to \Aut(E/L)\subset G$ in the other direction.

Further:

- If $L=E^{H}$ then $E/L$ is Galois with group $H$.
- If $L=E^{H}$ then $[E:L]=\vert H\vert$ so $E$ is Galois over $L$.
- If $L$ is a subfield of $E$ containing $F$, then $\vert\Aut(E/L)\vert=[E:L]$ so $E$ is Galois over $L$.
- The fixed field $L=E^{H}$ is Galois over $F$ if and only if $H$ is a normal subgroup of $G$, and in that case $\Aut(L/F)=G/H$.

### Some examples

- Quadratic extensions
- $\Q(\sqrt{2},\sqrt{3})$.
- The splitting field of $x^3-2$ over $\Q$.
- The splitting field of $x^4-2$ over $\Q$.
- The field $\Q(\zeta_p)$ where $\zeta_p$ is a $p^{th}$ root of unity.
- The fields of eigth and ninth roots of unity.
- Finite fields.

<div>
<a href="slides/07-galoisextensions.html"> View as slides </a>
</div>
