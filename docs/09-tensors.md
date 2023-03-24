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

### Extension of scalars (More examples)

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

### Extension of scalars via tensor product

Our strategy is to make an abelian group whose elements are pairs $(s,m)$ modulo the relations above. The equivalence classes of this abelian group
are written $s\otimes m$ (or, in cases where we need more context, $s\otimes_{R} m$ or even $s\otimes_{f}m$). THe group itself is called $S\otimes_{R} M$.
So the following rules hold:

- $(s_1+s_2)\otimes m=s_1\otimes m+s_2\otimes m$.
- $s\otimes (m_1+m_2)=s\otimes m_1 + s\otimes m_2$
- $sr\otimes m=s\otimes rm$.

A typical element of $S\otimes M$ is a _sum_ of the form $\sum_{i=1}^{n} s_{i}\otimes m_{i}$. It is an $S$-module via multiplication by $S$ on the first factor.

We have a map $M\to S\otimes_{R} M$ given by $m\mapsto 1\otimes m$.

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
\xymatrix@=2cm{
M \ar[r]^{1\mapsto 1\otimes m}\ar[rd]^{f}& S\otimes M\ar[d]^{\phi} \\
& L \\
}
\end{xy}
$$

### More on the universal property

If $\iota: M\to S\otimes M$ is the map $m\mapsto 1\otimes m$, then $M/\ker(\iota)$ maps injectively in $S\otimes M$. This is the "largest" quotient of $M$ which embeds into an $S$-module.

**Example:** Let $G$ be a finitely generated abelian group. Then $G$ is isomoprhic to $\Z^{n}\oplus T$ where $T$ is a finite group. If we want to map $G$ to a $\Q$-vector space, the kernel has to include $T$.
And in fact the kernel of $\iota$ is $T$. Further, the $\Q$-dimension of the vector space $\Q\otimes G$ is the rank of the free part of $G$.

### More examples

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

### Tensor product of vector spaces

Suppose that $R$ is a field and $V$, $W$, are vector spaces over $R$ of dimensions $n$ and $m$ respectively. Let $v_1,\ldots, v_n$ be a basis for $V$ and $w_1,\ldots, w_m$ a basis for $W$.

If $L$ is another $F$-vector space, then a bilinear map $f:V\times W\to L$
is determined by its values on all pairs $(v_i,w_j)$.

The tensor product $V\otimes W$ is an $F$-vector space and is spanned by the tensors $v_{i}\otimes w_{j}$.

Now construct a bilinear map
$f_{ij}:V\times W\to F$ by setting

$$
f_{ij}(\sum a_{s}v_{s},\sum b_{s}w_{s})=a_{i}b_{j}.
$$

By the universal property we have $f_{ij}(v_{r}\otimes w_{s})=0$ unless $r=i$ and $s=j$ in which case it is one.

### Tensor product of vector spaces continued

Suppose that

$$
x=\sum c_{rs}v_{r}\otimes w_{s}=0.
$$

Then $f_{ij}(x)=c_{ij}=0$ for all pairs $i,j$ and therefore all $c_{rs}=0$; in other words, the $v_{r}\otimes w_{s}$ are linearly independent. Thus $V\otimes W$ is an $nm$ dimensional $F$-vector space.

### Endomorphisms

Let $V$ be a vector space and let $V^{\ast}$ be its dual. Then
there is an isomorphism

$$
V\otimes V^{\ast}\to \End(V)
$$

where
$(v\otimes f)(w)=f(w)v$.

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
for $N$.

This is the tensor product of the modules $M$ and $N$ -- remember it is an abelian group, NOT an $R$-module in general.

### Universal property

$M\otimes N$ still satisfies a universal property. Call a map $f:M\times N\to L$, where $M$ is a right $R$-module, $N$ is a left $R$-module, and $L$ is an abelian group, _balanced_ if $f$ is additive in $M$ and $N$
separately and satisfies $f(mr,n)=f(m,rn)$ for all $r\in R$.

Then given such a balanced map from $M\times N$ to $L$, there is a unique map of abelian groups $\phi : M\otimes N\to L$ such that the following diagram commutes.

$$
\begin{xy}
\xymatrix{
M\times N \ar[r]^{\iota}\ar[dr]^{f} & M\otimes N\ar[d]^{\phi}\\
& L\\
}
\end{xy}
$$

Here the map $M\times N\to M\otimes N$ is the expected one: $(m,n)\mapsto m\otimes n$.

As is always the case, the universal property characterizes the tensor product up to isomorphism.

### Bimodules

Now suppose that $S$ and $R$ are rings with unity and that $M$ is simultaneously a left $S$-module and a right $R$ module, so that $(sm)r=s(mr)$. Such an object $M$ is called
an $(S,R)$-bimodule.

For example, suppose $R=M_{2}(F)$,
$S=F$, and $M$ is the space $F^{2}$ viewed as row vectors with $R$ acting on the right as matrix multiplication and $S$ on the left as scalar multiplication.

### Tensor product of bimodules

If $N$ is a left $R$ module, we can form the tensor product $M\otimes_{R}N$ which is an abelian group; but we can furthermore let $S$ act by $s(m\otimes n)=(sm\otimes n)$.

This makes $M\otimes_{R}N$ into a left $S$-module. (If $N$ is an $(R,S)$-bimodule so that $R$ acts on the left and $S$ on the right, then $M\otimes_{R}N$ is a right $S$-module.)

If $R$ is commutative, and $M$ is a left $R$ module, it is also a right $R$-module via $(mr)=rm$. So it is automatically an $(R,R)$-bimodule. This is how $M\otimes_{R}N$ is automatically
an $R$-module if $R$ is commutative.

## General Properties

### Tensor product of maps

If $f:M\to M'$ and $g:N\to N'$ are maps of right/left $R$-modules, then $f\otimes g:M\otimes N\to M'\otimes N'$ defined by $(f\otimes g)(m\otimes n)=f(m)\otimes g(n)$ is a well defined group homomorphism.

If $M$ and $M'$ are $(S,R)$ bimodules and $f$ and $g$ are $S$-module homomorphismsm then $f\otimes g$ is an $S$-module homomorphism. (If $R$ is commutative all this is automatic).

Further, provided
everything makes sense, $(f\otimes g)\circ (f'\otimes g')=(f\circ f')\otimes (g\circ g').$

### The Kronecker Product

If $L$ and $M$ are matrices giving linear maps from $\R^{n}$ to $\R^{n'}$ and $\R^{m}$ to $\R^{m'}$.

Then the tensor product of these maps is a linear map from $\R^{n}\otimes \R^{m}$ to $\R^{n'}\otimes \R^{m'}$.

The standard bases of $\R^{k}$ give us bases $e_{i}\otimes e_{j}$ of $\R^{n}\otimes R^{m}$ and $\R^{n'}\otimes\R^{m'}$.
Thus the tensor product is represented as an $nm\times n'm'$ matrix. This is called the Kronecker Product
of the matrices $L$ and $M$.

### Associativity

The tensor product is associative in the sense that $(M\otimes_{R} N)\otimes_{T} L$ is isomorphic to $M\otimes_{R} (N\otimes_{T} L)$ provided that $M$ is a right $R$ module,
$N$ is an $(R,T)$ bimodule, and $L$ is a left $T$-module. If $R$ and $T$ are commutative this is automatic.

First check that both versions of the tensor product make sense.

Notice that $N\otimes_{T}L$ is a left $R$-module and $M\otimes_{R}N$ is a right $T$-module.

For fixed $l\in L$, the map $(m,n)\mapsto m\otimes (n\otimes l)$ is $R$-balanced, so there is a well-defined
map

$$
M\otimes_{R}N\to M\otimes_{R}(N\otimes_{T}L)
$$

This gives a well-defined map

$$
M\otimes_{R}N\times L \to M\otimes_{R}(N\otimes_{T}L)
$$

and by the universal property this translates to a map

$$
(M\otimes_{R}N)\otimes_{T}L\to M\otimes_{R}(N\otimes_{T}L).
$$

You can also reverse this construction to create the inverse map.

If $M$ is an $(S,R)$ bimodule then both constructions yield left $S$-modules. Then $M\otimes_{R}N$
is an $(S,T)$ bimodule and $(M\otimes_{R}N)\otimes_{T}L$ is a left $S$-module.

### Commutativity

If $R$ is commutative, the tensor product is commutative in the sense that $M\otimes N$ is isomorphic to $N\otimes M$.

### Distributive law

$(M\oplus M')\otimes N$ is isomorphic to $(M\otimes N)\oplus (M'\otimes N)$ and similarly if $N$ is a direct sum. By induction this extends to finite direct sums. With care it holds for infinite direct sums.

The proof of this uses the fact that there is a well-defined balanced map

$$
F: (M\oplus M')\times N \to (M\otimes N)\oplus (M'\otimes N)
$$

defined by $F((m,m'),n)=(m\otimes n,m'\otimes n)

$$
and so we have a map
$$

(M\oplus M')\otimes N\to (M\otimes N)\oplus (M'\otimes N).

$$

On the other hand we have balanced maps $M\times N\to (M\oplus M')\otimes N$ sending $m\otimes n$ to $(m,0)\otimes n$
and similarly for $M'\times N$.  These give a map from $M\otimes N\oplus M'\otimes N\to (M\oplus M')\otimes N$
which is inverse to the map above.


### Tensor product of algebras

If $A$ and $B$ are $R$ algebras where $R$ is commutative, then $A\otimes_{R}B$ is an $R$ algebra with multiplication $(a\otimes b)(a'\otimes b')=(aa')\otimes (bb')$. (remember that an $R$ algebra is a ring in which
$R$ is mapped into the center of the ring).

<div>
  <a href="slides/09-tensors.html"> View as slides </a>
  </div>
$$
