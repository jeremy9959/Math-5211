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

### Overview of the proof

There are two "directions" we need to consider.

1.  Suppose $E/F$ is a separable splitting field extension. Then $\vert\Aut(E/F)\vert=[E:F]$.
2.  Suppose $E$ is a field and $G$ is a finite group of automorphisms of $E$. Then the fixed field
    $E^{G}$ satisfies $[E:E^{G}]=\vert G\vert$ and $E/E^{G}$ is a separable splitting field.

These mean together that:

- if we start with a separable extension $E/F$, compute its automorphism group $\Aut(E/F)$,
  and then take the fixed field in $E$ of that group, we get a subfield of $E$ that contains $F$ and has $[E:E^{\Aut(E/F)}]=[E:F]$, so $E^{\Aut(E/F)}=F$.
- if we start with a field $E$ and a group of automorphisms $G$,
  then $E/E^{G}$ is a separable splitting field extension so $\Aut(E/E^{G})$ has order $[E:E^{G}]=\vert G\vert$. Since $G$ is contained in $\Aut(E/E^{G})$, this means $\Aut(E/E^{G})=G$.

This is the prototype of the Galois correspondence.

### More on the proof - Step 1

The first assertion to consider is that, if $E/F$ is a separable splitting field, then $\vert\Aut(E/F)\vert=[E:F].$
This is a consequence of the theorem on extension of automorphisms. The proof is by induction.
Clearly if $E=F$ then $\Aut(E/F)$ is trivial and $[E:F]=1.$ Now suppose we know the result for all separable
splitting fields of degree less than $n$ and suppose $E/F$ has degree $n.$ Choose an element $\alpha\in E$
of degree greater than one over $F$ and let $f(x)$ be its minimal polynomial. Let $\beta$ be any other root
of $f(x)$. Since $E/F$ is a splitting field, $\beta\in E$. Consider the diagram:

$$
\begin{xy}
\xymatrix{
E \ar[r] & E \\
F(\alpha)\ar[r]\ar[u]&F(\beta)\ar[u] \\
F\ar[r]\ar[u] & F\ar[u] \\
}
\end{xy}
$$

Since $F(\alpha)$ is isomorphic to $F(\beta)$, the extension theorem says that there is an automorphism of $E$
carrying $\alpha$ to $\beta$. Since there are $[F(\alpha):F]$ choices of $\beta$, there are $n$ such extensions $\sigma_{\beta}$
corresponding to the $n$ roots $\beta$ of the minimal polynomial of $\alpha$ over $F$.

Now $E/F(\alpha)$ is still a separable splitting field, so our induction hypothesis
says that there are $[E:F(\alpha)]$ automorphisms of $E$ fixing $F(\alpha)$. Take any automorphism $\tau$ of $E/F$.
It carries $\alpha$ to some $\beta$, so $\sigma_{\beta}^{-1}\tau$ fixes $\alpha$ and therefore $\tau=\sigma_{\beta}\phi$ where $\phi\in\Aut(E/F(\alpha))$.

It's not hard to show that this representation is unique, and so

$$
\vert\Aut(E/F)\vert=\vert\Aut(E/F(\alpha))[F(\alpha):F] = [E:F(\alpha)][F(\alpha):F]=[E:F]
$$

### More on the proof - Step 2

Now we want to show that, if $G$ is a group of automorphisms of a field $E$, then $E/E^{G}$
is a separable splitting field of degree $\vert G\vert$. The key tool here is a result known
as _linear independence of characters_.

**Lemma:** Let $G$ be a group, let $L$ be a field,
and let $\sigma_1,\ldots, \sigma_n$ be distinct homomorphisms $G\to L^{\times}$. Then the $\sigma_{i}$ are linearly independent over $L$,
meaning that if $f=\sum_{i=1}^{n} a_{i}\sigma_{i}$ is the zero map for some collection of $a_{i}\in L$,
then all $a_{i}$ are zero.

**Proof:** Suppose that the $\sigma_{i}$ are dependent. Choose a linear relation of minimal length where all
the coefficients are nonzero:

$$
f=\sum a_{i}\sigma_{i} = 0
$$

Let $h\in G$ such that $\sigma_{1}(h)$ and $\sigma_{n}(h)$ are different. Now $f(g)=0$ for all $g\in G$,
and also $f(hg)=0$ for all $g\in G$ since it's the same set of elements. Therefore

$$
k=\sum a_{i}\sigma_{i}(h)\sigma_{i}=0.
$$

Now $k-\sigma_{n}(h)f$ is also identically zero. The coefficients of $\sigma_{n}$ in $k$ and $f$
are both $\sigma_{h}(h)a_{n}$ so they cancel. On the other hand, the coefficients of $\sigma_{1}$
are $a_{1}\sigma_{1}(h)$ and $a_{1}\sigma_{n}(h)$ which are different; so $k-\sigma_{n}(h)f$
is a relation among the $\sigma_{i}$ of shorter length. Thus the $\sigma_{i}$ are independent.

Notice that if $L$ is a field, $L^{\times}$ is a group and we can restrict an automorphism of $L$
to $L^{\times}$ to obtain a character $L^{\times}\to L$. Therefore distinct automorphisms of $L$
are linearly independent over $L$.

### More on the proof - Step 3

Now we want to prove that $[E:E^{G}]=\vert G\vert$. Let's use $F=E^{G}$ to simplify the notation.
Choose a basis $\alpha_{1},\ldots, \alpha_{n}$ for $E/F$ and let $\sigma_{1},\ldots, \sigma_{m}$ be the elements of $G$. Form $m\times n$ the matrix

$$
S=\left(\begin{matrix} \sigma_{1}(\alpha_{1}) & \sigma_{1}(\alpha_{2}) & \cdots & \sigma_{1}(\alpha_{n})\\
                     \sigma_{2}(\alpha_{1})  & \sigma_{2}(\alpha_{2}) & \cdots & \sigma_{2}(\alpha_{n}) \\
                     \vdots & \vdots & \vdots &\vdots \\
                     \sigma_{m}(\alpha_{1}) & \sigma_{m}(\alpha_{2}) & \cdots & \sigma_{m}(\alpha_{n}) \\
                     \end{matrix}\right)
$$

Let's first look at the row rank of this matrix. Suppose that

$$
[\beta_1\cdots\beta_m]S = 0.
$$

It follows that $\sum_{i=1}^{m} \beta_{i}\sigma_{i}(\alpha_{j})=0$ for all $\alpha_j$, and, since the $\alpha_{j}$
span $E/F$, we condlue
$\sum_{i=1}^{m}\beta_{i}\sigma_{i}(x)=0$ for all $x\in E$. By linear independence this means that all $\beta_{i}=0$
and so the row rank of $S$ is $m$.

Now let's look at the column rank. For this, notice that if $\sigma:E\to E$ is an automorphism, then $\sigma(S)$
(obtained by applying $\sigma$ to each entry of $S$) is obtained from $S$ by rearranging the rows. In other
words

$$
\sigma(S)=\Pi(\sigma)S
$$

where $\Pi(\sigma)$ is an $m\times m$ permutation matrix. Now suppose $\boldsymbol{\beta}=[\beta_{1},\ldots, \beta_{n}]$
satisfies

$$
S\boldsymbol{\beta}=S\left[\begin{matrix} \beta_{1} \\ \vdots \\ \beta_{n}\end{matrix}\right]=0.
$$

Then, for any $\sigma\in G$, we have

$$
\sigma(S\boldsymbol{\beta})=\sigma(S)\sigma(\boldsymbol{\beta})=\Pi(\sigma)S\boldsymbol{\beta}=0
$$

In other words, if $\boldsymbol{\beta}$ is in the (left) kernel of $S$, so is $\sigma(\boldsymbol{\beta})$.

Now suppose $\boldsymbol{\beta}$ is nonzero and satisfies $S\boldsymbol{\beta}=0$ and let $y=\sum_{i=1}^{m}\sigma_{i}(\boldsymbol{\beta})$. This is a column vector whose entries are $\sum_{i=1}^{m}\sigma_{i}(\beta_{j})$. These sums are
all fixed by $G$, since $\sigma(\sum_{i=1}^{m}\sigma_{i}(\beta_{j}))$ is just a permutation of the terms in the sum.
We can introduce a function $Y:E\to E$ by setting

$$
Y_j(x)=\sum_{i=1}^{m}\sigma_{i}(x\beta_{j})=\sum_{i=1}^{m}\sigma_{i}(\beta_{j})\sigma_{i}(x).
$$

Since $\boldsymbol{\beta}$ is nonzero, by linear independence at least one of $Y_{j}$ is nonzero
so there is an $x\in E$ such that

$$
\boldsymbol{Y}=\sum_{i=1}^{m}\sigma_{i}(x\boldsymbol{\beta})\not=0
$$

But $\boldsymbol{Y}$ is in $F^{n}$ and $S\boldsymbol{Y}=0$. This means

$$
\sigma_{i}(\sum_{j=1}^{n} Y_{j}(x)\alpha_{j})=0
$$

for all $i$; and since the $Y_{j}(x)\in F$ and the $\alpha_{j}$ are independent we must have $Y_{j}(x)=0$.
This contradiction means that there cannot be a nonzero $\boldsymbol{\beta}$ with $S\boldsymbol{\beta}=0$.
We conclude that the column rank of $S$ is $n$.

Since the row and column ranks of a matrix are the same, we have $n=m$.

### More on the proof - Step 4

We finally need to verify that $E/E^{G}$ is a separable splitting field.

<div>
<a href="slides/07-galoisextensions.html"> View as slides </a>
</div>
