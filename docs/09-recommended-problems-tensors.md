---
layout: default
title: Recommended Problems
nav_order: 9.5
parent: Course Content
---

## Recommended Problems

### Problem 1 (DF, problem 6, p. 375)

Let $R$ be an integral domain with field of fractions $Q$. Prove that $(Q/R)\otimes_{R} (Q/R)=0.$ In particular $\Q/\Z\otimes\Q/\Z=0$.

### Problem 2 (DF, problem 5, p. 375)

Let $G$ be a finite abelian group and let $p^{k}$ be the highest power of a prime $p$ dividing $\vert G\vert$. Prove that $Z/p^{k}\Z\otimes G$ is the
Sylow $p$-subgroup of $G$.

### Problem 3 (DF, Problem 8, p. 375ff)

Suppose $R$ is an integral domain with quotient field $Q$ and let $N$ be any $R$ module. Let $U=R^{\ast}$ be the nonzero elements in $R$
and let $U^{-1}N$ be the set of equivalence classes of pairs $(u,n)$ with $(u,n)\sim (u',n')$ if and only if $u'n=un'$.

- Show that $UN^{-1}$ is an abelian group with $(u_1,n_1)+(u_2,n_2)=(u_1u_2,u_2n_1+u_1n_2)$ and that the operation $r(u,n)=(u,rn)$ makes
  $U^{-1}N$ into an $R$-module.

- Show that the map $Q\times N\to U^{-1}N$ sending $(a/b,n)\to (b,an)$ is $R$-balanced and so yields a unique map $Q\otimes N\to U^{-1}N$.
  Show that the map $(u,n)\to u^{-1}\otimes n$ is a well-defined inverse, and so $Q\otimes N$ is isomorphic to $U^{-1}N$.

- Show that $(1/d)\otimes n=0$ if and only if there is $r\in R$ so that $rn=0$.

- Show that $\Q\otimes A=0$ (where $A$ is an abelian group) if and only if $A$ is torsion.

### Problem 4 (DF Problem 16 pg. 376)

Let $R$ be commutative and let $I$ and $J$ be ideals. Prove that every element of $R/I\otimes R/J$ has the form $1\otimes r$ for $r\in R$.
Then show that $R/I\otimes R/J$ is isomorphic to $R/(I+J)$ via the map sending $r\otimes r'$ to $rr'$.

### Problem 5 (DF, Problem 17 and 19, pg. 37

Let $R=\Z[x]$ and let $I=(2,x)$. Show that the map $\phi:I\times I\to \Z/2\Z$ given by

$$
\phi(fg)=f(0)g'(0)/2\pmod{2}
$$

is $R$-bilinear. Thus it gives a map $I\otimes I\to \Z/2\Z$. Conclude that $2\otimes x$ and $x\otimes 2$ are not equal in $I\otimes I$.

Now show that the element $2\otimes x-x\otimes 2$ in $I\otimes I$ is killed by $2$ and by $x$ and that therefore it generates a submodule of $I\otimes I$
isomorphic to $R/I$.
