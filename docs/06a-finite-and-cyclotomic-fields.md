---
layout: default
title: 6A. Finite and Cyclotomic Fields
nav_order: 6.5
parent: Course Content
---

## Finite and Cyclotomic Fields

### Finite fields are perfect

**Lemma:** Let $F$ be a finite field. Then every element of $F$ is a $p^{th}$ power.

**Proof:** The map $\phi(x)=x^{p}$ is a field homomorphism from $F$ to itself. Since it is injective
and $F$ is finite, it is surjective.

**Lemma:** Every irreducible polynomial over $F$ is separable.

**Proof:** If $f(x)$ is irreducible and inseparable, then $f'(x)=0$ so $f(x)=g(x^p)$. But then $f(x)=g(x)^p$, contradicting
irreducibility.

### Existence and uniqueness of finite fields

**Proposition:** Let $p$ be a prime. Then there is a unique (up to isomorphism) finite field with $p^n$ elements for every $n\ge 1$.

**Proof:** If $F$ is a finite field of characteristic $p$, it is a finite dimensional vector space over $F_p$ so has $p^{n}$ elements where $n=[F:F_p]$.
Consider the splitting field $F$ of the polynomial $x^{p^{n}}-x$ over $F_p$. It is separable since its derivative is $-1$.
Thus it has $p^{n}$ distinct roots. Notice that, if $\alpha$ and $\beta$ are roots of this polynomial, so are $\alpha\beta$, $\alpha+\beta$,
and $\alpha^{-1}$. Thus the $p^{n}$ roots of the polynomial form a field. Thus $F$ is exactly this set of $p^{n}$ roots.
Finally, let $F$ be any finite field of characteristic $p$ with $p^{n}$ elements. The nonzero elements of $F$ satisfy $x^{p^{n}-1}-1=0$ since $F^{*}$ is a finite
abelian group with $p^{n}-1$ elements. Therefore (including zero) the elements of $F$ are the roots of $x^{p^{n}}-x$ so $F$ is the splitting field
of this polynomial. Since splitting fields are unique, all finite fields of order $p^{n}$ are isomorphic.

We commonly write $F_{p^{d}}$ or $\mathbb{F}_{p^{d}}$ for this unique field with $p^{d}$ elements.

### Multiplicative groups of finite fields are cyclic

Suppose $F$ has $p^{n}$ elements. Suppose that $d|(p^{n}-1)$ so $x^{d}-1$ divides $x^{p^{n}-1}-1$.
If $F^{\times}$ has an element of order $d$, it generates a cyclic subgroup of order $d$, and the elements
of that cyclic subgroup are all roots of $x^{d}-1$. In this case the number of elements of order $d$ is $\phi(d)$.
If $\psi(d)$ is the number of elements of order $d$, then we see that $\psi(d)$ is either $\phi(d)$ or zero, and in
particular is at most $\phi(d)$.

Now by Lagrange's Theorem

$$
p^{n}-1=\sum_{d|(p^{n}-1)} \psi(d).
$$

On the other hand, by counting the elements of order $d$ for each divisor of $p^{n}-1$ in a cyclic group of order
$p^{n}-1$, we have

$$
p^{n}-1=\sum_{d|(p^{n}-1)} \phi(d).
$$

We conclude that $\psi(d)=\phi(d)$ for all $d$, so $\phi(p^{n}-1)\ge 1$.

### Cyclotomic Polynomials and roots of unity

We let $\mu_n$ denote the complex roots of the polynomial $x^n-1$. These are called the $n^{th}$ roots of unity.
If $\zeta\in\mu_n$, then

$$
\zeta=e^{2\pi i a/n}
$$

for some integer $a$.

The set $\mu_n$ is in fact a cyclic group of order $n$. Its generators are called the primitive $n^{th}$ roots of unity.
If $\zeta\in \mu_n$ is a primitive root of unity then

$$
\zeta=e^{2\pi i a/n}
$$

where $(a,n)=1$.

### The cyclotomic polynomials

The cyclotomic polynomial $\Phi_{n}(x)$ is the polynomial whose roots are the primitive $n^{th}$ roots of unity.

**Lemma:** For all $n\ge 1$, the degree of $\Phi_{n}(x)$ is $\phi(n)$, and

$$
x^{n}-1=\prod_{d|n} \Phi_{d}(x)
$$

This is because there are $\phi(n)$ primitive roots of unity in $\mu_{n}$ and every $n^{th}$ root of unity is primitive of order $d$ for some $d|n$.

### Cyclotomic polynomials have integer coefficients

**Lemma:** $\Phi_{n}(x)$ is monic and belongs to $\Z[x]$.
