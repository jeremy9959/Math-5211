---
title: 12. Localization
layout: default
nav_order: 12
parent: Course Content
---

## Localization

Localization in commutative algebra is the algebraic version of restricting functions to open sets. Throughout this section, $R$ is a commutative ring with unity,
and ring maps send $1$ to $1$.

**Definition:** A subset $D\subset R$ is multiplicatively closed if $1\in D$ and $x,y\in D$ implies $xy\in D$. If $D$ is multiplicatively closed,
then $D^{-1}R$ is the quotient of $R\times D$ by the relation $(x,y)\sim (x',y')$ if there is a $d\in D$ so that $d(xy-x'y)=0$.

**Proposition:** $D^{-1}R$ is a commutative ring with unity. The operations treat $(x,y)$ as if it was a fraction $x/y$, so that

$$
(x/y)(x'/y')=(xx'/yy')
$$

and

$$
(x/y)+(x'/y')=(xy'+x'y)/(yy').
$$

There is a natural map $u: R\to D^{-1}R$ that sends $x\to (x,1)$. If $x\in D$, then $(x,1)$ is a unit in $D^{-1}R$, with inverse $(1,x)$.

The ring $D^{-1}R$ satsifies a universal property. Given any map $f:R\to S$ such that the images $f(d)$ for $d\in D$ are units in $S$,
there is a unique map $\phi:D^{-1}R\to S$ such that $\phi\circ u=f$.

**Examples:**

If $R$ is an integral domain, and $D$ consists of all nonzero elements of $R$, then $D^{-1}R$ is the field of fractions of $R$.

Suppose that $R=\mathbb{Z}/6\mathbb{Z}$ and $D=\{1,2,4\}$, the powers of $2$. Then $(3,1)=(0,1)$ in $D^{-1}R$ because $2(3-0)=0$.
However, $(2,1)$ is not zero. So that map $R\to D^{-1}R$ is not injective. Its kernel is the set $(a,1)$ where $2a=0$, and
therefore $D^{-1}R=\mathbb{Z}/3\mathbb{Z}$.

More generally, suppose we are in the general situation and $(x,1)$ is in the kernel of the map $R\to D^{-1}R$. Then there
is an element $d\in D$ such that $dx=0$. If $x\not=0$, this means that $D$ contains a zero divisor (or zero). If $0\in D$,
then $D^{-1}R$ is the zero ring.

If $R$ is a comm. ring with $1$ and $f\in R$, then $R_{f}$ is another notation for $D^{-1}R$ where $D$ consists of $1$ and all powers of $f$.
If $f$ is not a zero divisor, this ring contains a copy of $R$ and also $1/f$. In fact $R_{f}=R[x]/(fx-1)$.

If $P$ is a prime ideal, then the complement $D$ of $P$ is multiplicatively closed. We write $R_{P}$ for $D^{-1}R$ in this case. Elements of $R_{P}$
are rational functions that are defined on the algebraic variety arising from $P$

If $R=k[x_1,\ldots, x_n]$ and $M=(x_1-a_1,\ldots, x_n-a_n)$ is a maximal ideal, then the localization $R_{M}$ is the ring of rational functions
that are defined at that point corresponding to $M$.

### Ideals and Localization

The ideals of a quotient $R/I$ are the ideals of $R$ containing $I$. We sill see that, if $P$ is a prime ideal, the ideals of $R_{P}$ are the ideals
of $R$ contained in $P$. So localization allows us to focus on a limited set of primes in a ring.

**Proposition:** Let $J$ be an ideal of $D^{-1}R$. Then

1. $\pi^{-1}J$ is an ideal of $R$, and $(\pi^{-1}J)D^{-1}R=J$. If two ideals $I$ and $I'$ of $D^{-1}R$ have $I\cap R = I'\cap R$, then $I=I'$.

It's always the case that the inverse image of an ideal is an ideal; and since $\pi(\pi^{-1}(J)\subset J)$ we know that $\pi^{-1}JD^{-1}R$ is contained in $J$.
So suppose $(a,d)\in J\subset D^{-1}R$. Then $(a,1)=d(a,d)\in J$, so $a\in \pi^{-1}J\subset R$. But then $(a,1)$ is in $\pi^{-1}JD^{-1}J$ so $(a,1)(1,d)=(a,d)$ is
in the extended ideal.

- If $J$ is an ideal of $R$, then $(\pi(I)D^{-1}R)\cap R$ consists of all elements of $R$ such that $dx\in J$ for some $d\in D$.

If $dx\in J$, then in $D^{-1}R$ we have $x=(1/d)y$ where $y\in J$ so $x$ is in the extended ideal, and then in intersection back to $R$. Conversely, if
$x$ is in the intersection back to $R$ then $x=a/d$ where $a\in J$ and $d\in D$. This means that there is an $e\in D$ so that $e(xd-a)=0$ or $exd=ea$. Now
$ed$ is in $D$, and $ea$ is in $J$, so $x$ has the property that a $D$-multiple of it lands in $J$.

- There is a bijective correspondence between the primes of $R$ disjoint from $D$ and the primes of $D^{-1}R$.

If $Q$ is prime in $D^{-1}R$, the $Q\cap R$ is prime. So the map in that direction takes prime ideals to prime ideals. Now suppose $P$ is a prime of $R$
and suppose that $(x/d)(y/d')$ is in $PD^{-1}R$. Then $xy/dd'=c/d$ where $c\in P$ and $d\in D$. Then there is a $u\in D$ with $u(dxy-cdd')=0$. This means
that $(ud)(xy)$ is in $P$. Since $P$ does not meet $D$, that means $xy$ is in $P$. That in turn means either $x$ or $y$ is in $P$, so either $x/d$ or $x'/d'$ is in $PD^{-1}R$,
so that ideal is prime.

- If $R$ is Noetherian, so is $D^{-1}R$.

This follows from (1) since an ascending chain of ideals of $D^{-1}R$ contracts to one in $R$, which then terminates; and the extension of that termination
gives a termination of the original chain.

### Localization of modules

Let $M$ be a module over the ring $R$ and let $D$ be a multiplicatively closed subset of $R$.

**Definition:** $D^{-1}M$ is the module $M\times D/\sim$ where the equivalence relation $\sim$ is given by $(m,d)\sim (m',d')$ if there is an $x\in D$ so that
$x(md'-dm')=0$. There is a natural map $M\to D^{-1}M$ sending $m\to (m,1)$. $D^{-1}M$ is a $D^{-1}R$ module via the action $(r,d)(m,d')=(rm,dd')$.

As in the case of rings above, the kernel of the map $M\to D^{-1}M$ is the subset of $M$ such that $dm=0$ for some $d\in D$.

Given a map $f:M\to N$, there is a map $f:D^{-1}M\to D^{-1}N$ defined by $f(m,d)=(f(m),d)$.

**Proposition:** $D^{-1}M$ is isomorphic to $D^{-1}R\otimes_{R}M$.

**Proof:** The map $D^{-1}R\times M \to D^{-1}M$ given by $((r,d),m)\mapsto (rm,d)$ is bilinear and so yields a map from the tensor product to $D^{-1}M$.
The inverse map sends $(m,d)\to (1,d)\otimes m$. (If (m,d)=(m',d') then $u(md'-dm')=0$ for some $u\in D$. But $(m,d)$ maps to $(1,d)\otimes m$ and $(m',d')$ maps to
$(1,d')\otimes m'$. So $1/d\otimes m = 1/udd'\otimes ud'm=1/udd'\otimes udm' = 1/d'\otimes m'$). These maps are $D^{-1}R$ module homomorphisms.

**Functorial properties of localization:**

1.  Localization commutes with finite sums and intersections of ideals.

2.  Localization commutes with radicals: the radical of $D^{-1}I$ is $D^{-1}(\mathrm{rad} I)$.

3.  Localization commutes with finite sums, intersections, and quotients of modules.

4.  Localization commutes with finite direct sums.

5.  Localization is flat.

### Local Rings

**Definition:** A commutative ring with unity that has a unique maximal ideal is called a _local ring._

**Proposition:** TFAE:

- $R$ is local with maximal ideal $M$
- The units of $R$ are exactly the elements of $R$ outside $M$.
- there is a maximal ideal $M$ of $R$ wuch that $1+m$ is a unity for $m\in M$.

**Proposition:** Let $R$ be a commutative ring with 1 and let $R_P$ be the localization of $R$ at $P$.

- $R_P$ is local with maximal ideal $P^e=PR_P$. The map $R\to R_P$ induces an injection $R/P\to R_P/PR_P$.
  $R_P/PR_P$ is a field equal to the quotient field of $R/P$.

- If $R$ is an integral domain, so is $R_P$. The map $R\to R_P$ is injective.

- The prime ideals of $R_P$ are in bijective correspondence with the prime ideals of $R$ contained in $P$.

- If $P$ is a maximal ideal then $R/M$ is isomorphic to $R_M/MR_M$.

**Lemma:** Let $M$ be an $R$ module. Then TFAE:

- $M=0$
- $M_P=0$ for all primes $P$ of $R$
- $M_m=0$ for all maximal ideals $m$ of $R$.

**Proposition:** Let $R$ be an integral domain.  Then $R$ is integrally closed if and only if $R_P$ is integrally closed for all prime ideals iff $R_M$ is integrally
closed for all maximal ideals.
