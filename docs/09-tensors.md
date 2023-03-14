---
layout: default
title: 9. Tensor Products
nav_order: 9.0
parent: Course Content
---

## Tensor Products I: Extension of Scalars

### Restriction of scalars

Suppose $R$ and $S$ are rings with unity (but not necessarily commutative), that we have ring homomorphism
$f:R\to S$ and that $M$ is an $S$ module. Then $M$ is an $R$ module by "restricting scalars" so that $r\cdot m=f(r)m$.

- Any $\R$-vector space is a $\Q$ vector space.
- Any vector space over $\Z/p\Z$ is a module over $\Z$.
- There is a ring map $\C\to M_{2}(R)$ sending

  $$i\to\left(\begin{matrix} 0 & 1 \\ -1 & 0\end{matrix}\right)$$

  and so any left module over $M_{2}(\R)$ can be viewed as a complex vector space. There are other elements in $M_{2}(\R)$ satisfying $x^2+1=0$,
  and so there are lots of ways to view a left module over $M_{2}(\R)$ as a $\C$-vector space.

  ### Extension of scalars

  Suppose that $f:R\to S$ is a map of rings with unity, and $M$ is an $R$-module. Is there a way to make $M$ into an $S$-module? Maybe
  a better way to say it is: can we find a "smallest" $S$-module $N$ together with a map $M\to N$?

  **Example:** Suppose that $V$ is a finite dimensional real vector space. Choose a $v_1,\ldots, v_n$ for $V$. So $V$ is isomorphic to $\R^{n}$ using this basis.
  So we can think of $V$ as inside $\C^{n}$. If we chose a different basis, we'd get a different map $V\to \C^{n}$, but the two maps would be related by a change of basis
  transformation so in some sense these are "isomomorphic".

  **Example:** Suppose that $M$ is an abelian group (hence a $\Z$-module). Can we embed $M$ in a $\Q$-module? Sometimes, yes: if $M$ is $\Z^{n}$ for some $n$, then
  $M$ embeds in $\Q^{n}$. On the other hand if $M$ is finite, there are no maps from $M\to \Q^{n}$ for any $n$. If $M$ is a mixture of free and torsion parts, we can embed the free part of
  $M$ in $\Q^{n}$ but not the torsion part.

  **Example:** If $M$ is an abelian group, can we embed $M$ into a vector space over $\Z/p\Z$ -- here the map $R\to S$ is the map $\Z\to \Z/p\Z$? Sometimes yes -- if $M$ is $p$-torsion, we can do it,
  but for general $M$ no.

### Universal approach

To study this in general we take a (left) $R$-module $M$ and a ring map $f:R\to S$ and ask: how can we make an $S$-module out of $M$ and the map $f:R\to S$?

An $S$-module structure on $M$ means we need a map

$$
S\times M\to M
$$

satisfying the axioms

- $(s,(m_1+m_2))=(s,m_1)+(s,m_2)$
- $(s_1+s_2,m)=(s_1,m)+(s_2,m)$
- $(sr,m)=(s,rm)$ for $r\in R$.

### Extension of scalars tensor product

So our strategy is to make an abelian group whose elements are pairs $(s,m)$ modulo the relations above. The equivalence classes of this abelian group
are written $s\otimes m$ (or, in cases where we need more context, $s\otimes_{R} m$ or even $s\otimes_{f}m$). THe group itself is called $S\otimes_{R} M$.
So the following rules hold:

- $(s_1+s_2)\otimes m=s_1\otimes m+s_2\otimes m$.
- $s\otimes (m_1+m_2)=s\otimes m_1 + s\otimes m_2$
- $sr\otimes m=s\otimes rm$.

A typical element of $S\otimes M$ is a _sum_ of the form $\sum_{i=1}^{n} s_{i}\otimes m_{i}$. It is an $S$-module via multiplication by $S$ on the first factor.

We have a map $M\to $S\otimes_{R} M$ given by $m\mapsto 1\otimes m$.

**Important:** The elements $s\otimes m$ belong to a quotient group and so the representation of an element as a sum of "simple tensors" $s\otimes m$ need not be unique!
In fact it's quite possible for $s\otimes m$ to be zero.

### Some examples

Suppose that $M=\Z^{n}$ and $R\to S$ is $\Z\to \Q$. Then $\Q\otimes M$ consists of sums of elements $a\otimes m$. But $a=\frac{x}{y}$ where $x\in \Z$, so we can write
$a\otimes m=\frac{1}{y}\otimes xm$. $\Q\otimes M$ is isomorphic to $\Q^{n}$.

Suppose that $M$ is a finite group of order $n$. Then any element of $\Q\otimes M$ can be written $a\otimes m$ where $a\in \Q$. But $a=n(a/n)$. Therefore

$$
a\otimes m = (a/n)n\otimes m = (a/n)\otimes nm=0
$$

so $\Q\otimes M$ is the zero module.

### The universal property

The idea is that $S\otimes M$ is the _smallest_ $S$ module containing $M$, where the action of $R$ comes via the map $R\to S$. In other words, if $L$ is any other $S$ module and
there is an $R$-module map $f:M\to L$, then there is a unique $S$-module map $\phi:S\otimes M\to L$ so that this triangle commutes:

$$
\begin{xy}
\xymatrix {
M \ar[r]^{1\mapsto 1\otimes m}\ar[rd]^{f}& S\otimes M\ar[d]^{\phi} \\
& L \\
}
\end{xy}
$$

### More on the universal property

If $\iota: M\to S\otimes M$ is the map $m\mapsto 1\otimes m$, then $M/\ker(\iota)$ maps injectively in $S\otimes M$. This is the "largest" quotient of $M$ which embeds into an $S$-module.

**Example:** Let $G$ be a finitely generated abelian group. Then $G$ is isomoprhic to $\Z^{n}\oplus T$ where $T$ is a finite group. If we want to map $G$ to a $\Q$-vector space, the kernel has to include $T$.
And in fact the kernel of $\iota$ is $T$. Further, the $\Q$-dimension of the vector space $\Q\otimes G$ is the rank of the free part of $G$.

**Example:** Let $M$ be an $R$ module and let $f:R\to R/I$ be the quotient map. Then $R/I\otimes M$ is isomorphic to $M/IM$. First notice that if $x\in IM$, then $1\otimes x=1\otimes im=i\otimes m=0$,
so $IM$ is in the kernel of $\iota$. Therefore we have a map $M/IM\to R/I\otimes M$. We have a map in the opposite direction $R/I\otimes M\to M/IM$ given by $(r+I)\otimes m\mapsto rm+IM$.
So if $G$ is a finite abelian group, then $\Z/p\Z\otimes G$ is $G/pG$ which is zero if $G$ has no $p$-torsion.

**Example:** If $V$ is a vector space over $F$ of dimension $n$, and $F\to E$ is a field extension, then $E\otimes V$ is an $n$-dimensional vector space over $E$.

## Tensor products of modules

### The commutative case

Assume for the moment that $R$ is a _commutative_ ring with unity. Suppose that $M$ and $N$ are $R$-modules. If $L$ is yet another $R$-module, a bilinear map

$$
f: M\times N \to L
$$

is a map that is linear in each variable separately and also satisfies $f(rm,n)=f(m,rn)$ for $r\in R$. The tensor product $M\otimes_{R} N$ of $M$ and $N$ is the free abelian group on pairs $(m,n)$
modulo the relations:

- $(m_1+m_2,n)=(m_1,n)+(m_2,n)$
- $(m,n_1+n_2)=(m,n_1)+(m,n_2)$
- $(rm, n)=(m,rn)$

The equivalence class of the pair $(m,n)$ is written $m\otimes n$. $M\otimes N$ is an $R$ module via the action $r(m\otimes n)=(rm\otimes n)=(m\otimes rn)$ and

$$
r(\sum m_{i}\otimes n_{i})=\sum r(m_{i}\otimes n_{i}).
$$

### Universal property

If $f:M\times N\to L$ is bilinear, then we can defined $\overline{f}:M\otimes N\to L$ by $\overline{f}(m\otimes n)=f(m,n)$. This is well defined and it converts a bilinear map into a module homomorphism.
To go in the other direction, there is a map $B:M\times N\to M\otimes N$ which is bilinear, sending $(m,n)\to m\otimes n$. This is the ``universal" bilinear map. The universal property says that,
if $f:M\times N\to L$ is any bilinear map, there is a unique module homomorphism $\overline{f}:M\otimes N\to L$ such that $\overline{f}B=f.$

$$
\begin{xy}
\xymatrix{
M\times N \ar[r]^{B}\ar[dr]^{f} & M\otimes N\ar[d]^{\overline{f}}\\
& L\\
}
\end{xy}
$$

### The noncommutative case

Now suppose that $R$ is a noncommutative ring. If $M$ and $N$ are left modules, then we have a problem defining a bilinear map $M\times N\to L$ where $L$ is also a left module. Namely, on the one hand, we would need:

$$
f(rsm,n)=rf(sm,n)=f(sm,rn)=sf(m,rn)=f(m,srn)
$$

but on the other hand

$$
f((rs)m,n)=(rs)f(m,n)=f(m,(rs)n)
$$

and since $sr$ and $rs$ are different we can't define this consistently.

### The noncommutative case continued

In the non-commutative case (with unity) we have to make some compromises:

- First, we assume $M$ is a _right_ module and $N$ is a _left_ module.
- Next, we are only going to construct an _abelian group_, not a module, from $M$ and $N$.
- Finally, we are going to consider maps $f:M\times N\to L$, where $L$ is an abelian group, that are _balanced_, meaning that $f(mr,n)=f(m,rn)$ for $r\in R$.

We create an abelian group spanned by $m\otimes n$ subject to the relations $mr\otimes n=m\otimes rn$ together with the additivity $(m+m')\otimes n=m\otimes n + m'\otimes n$ and similarly
for $N$. This is the tensor product of the modules $M$ and $N$ -- remember it is an abelian group, NOT an $R$-module in general.

### Universal property

$M\otimes N$ still satisfies a universal property. Call a map $f:M\times N\to L$, where $M$ is a right $R$-module, $N$ is a left $R$-module, and $L$ is an abelian group, _balanced_ if $f$ is additive in $M$ and $N$
separately and satisfies $f(mr,n)=f(m,rn)$ for all $r\in R$. Then given such a balanced map from $M\times N$ to $L$, there is a unique map of abelian groups $\phi : M\otimes N\to L$ such that the following diagram commutes.

$$
\begin{xy}
\xymatrix{
M\times N \ar[r]^{\iota}\ar[dr]^{f} & M\otimes N\ar[d]^{\phi}\\
& L\\
}
\end{xy}
$$

Here the map $M\times N\to M\otimes N$ is the expected one: $(m,n)\mapsto m\otimes n$.

<div>
  <a href="slides/09-tensors.html"> View as slides </a>
  </div>
