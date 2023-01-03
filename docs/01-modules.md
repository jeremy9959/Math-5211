---
title: 1. Modules
nav_order: 1
parent: Course Content
layout: default
---


## Modules

- Modules are to rings as vector spaces are to fields.
- Modules are to rings as sets with group actions are to groups.

## Definition of (left) modules

**Definition:** Let $R$ be a ring (for now, not necessarily commutative and not necessarily having a unit).  A *left $R$-module* is an abelian group $M$ together with a map $R\times M\to M$ (written $(r,m)\mapsto rm$) such that:

- $r(m_1+m_2)=rm_1+rm_2$
- $(r_1+r_2)m = r_1 m + r_2 m$
- $r_1 (r_2 m) = (r_1 r_2) m$

If $R$ has a unit element $1$, we also require $1m=m$ for all $m\in M$.

<div>
<a href="slides/01-modules.html"> View as slides </a>
</div>