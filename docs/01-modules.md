---
title: 1. Modules
nav_order: 1
parent: Course Content
layout: default
---


### Modules

- Modules are to rings as vector spaces are to fields.
- Modules are to rings as sets with group actions are to groups.

### Definition of (left) modules

**Definition:** Let $R$ be a ring (for now, not necessarily commutative and not necessarily having a unit).  A *left $R$-module* is an abelian group $M$ together with a map $R\times M\to M$ (written $(r,m)\mapsto rm$) such that:

- $r(m_1+m_2)=rm_1+rm_2$
- $(r_1+r_2)m = r_1 m + r_2 m$
- $r_1 (r_2 m) = (r_1 r_2) m$

If $R$ has a unit element $1$, we also require $1m=m$ for all $m\in M$.

### Right modules

A right module is defined by a map $M\times R\to M$ and written $(m,r)\mapsto mr$ and
satisfying the property
$$
(m r_1)r_2 = m(r_1 r_2).
$$

If $R$ is not commutative, these really are different, since for a left module:

-  $r_1 r_2$ acts by "first $r_2$, then $r_1$

while for a right module 

-  $r_1 r_2$ acts by "first $r_1$, then $r_2$."

### Left and Right modules

If $R$ is commutative, and $M$ is a left $R$-module, then we can define a right
$R$ module $M'$ with the same underlying abelian group $M$ and by defining $m' r=(r m)'$. 
This works because 

$$
(m'r_1) r_2 = (r_1 m)'r_2 = (r_2(r_1 m))'=((r_2 r_1)m)' =((r_1 r_2)m)' = m'(r_1 r_2)
$$ 

### Remarks

#### Vector spaces

If $R$ is a field, then a left (or right) $R$-module is the same as a vector space. 

#### Another definition

If $M$ is an abelian group, and $R$ is a ring, then a left $R$-module structure on $M$
is the same as a ring map 

$$R\to \End (M)$$. 

If $\phi_r$ is the endomorphism associated to $r\in R$,
then $rm=\phi_{r}(m)$.  The associativity comes from defining the ring structure on $$\End (M)$$
as the usual composition of functions:
$$
\phi_{r_1 r_2}=\phi_{r_1}\circ\phi_{r_2}.
$$

### Submodules

**Definition:** If $M$ is a left $R$-module, then a submodule $N$ of $M$ is a subgroup with the property that, if $n\in N$, then $rn\in N$ for all $r\in R$.

**Observation:** A ring $R$ is a left module over itself by ring multiplication.  The (left) ideals of $R$ are *exactly the left submodules of $R$*.

<div>
    <a href="beamer/01-modules.pdf"> View as slides </a>
</div>