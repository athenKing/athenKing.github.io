---
layout: post
title: psi_journey
date: 2019-08-22 14:13:27 +0800
categories: jekyll update
---

<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

## PSI(private set intersection) problem and it's solution

### Motivation from real life

>**Private set intersection (PSI) refers to the setting where two parties each hold sets of items and wish to learn nothing more than the intersection of these sets**. Today, PSI is a truly practical primitive, with extremely fast cryptographically secure implementations [PSSZ15]. Incredibly, these implementations are only a relatively small factor slower than than the naive and insecure method of exchanging hashed values. Among the problems of secure computation, PSI is probably the one most strongly motivated by practice.
>
> For example, in online advertisting business, we typically measures the success of ad campaigns by measuring the success of converting viewers into customers.Under insufficient conditions, the two parties(advertiser and mechant) can run a PSI protocol to compute conversion rates.
>
> A second example is that when a new user registers to a service it is often essential to identify current registered users who are also contacts of the new user. This operation can be done by simply revealing the user's contact list to the service, but can also be done in a privacy preserving manner by running a PSI protocol between the user's contact list and the registered users of the service.
>
> And in DNA testing, which I believe will be a widespread application in the near future. Including paternity testing as a service, other services also included massive Set Intersection in implementation, since genome data are very sensitive data for oneself, it defines almost your whole privacy.So a PSI protocol is requried to do such computation.
>
>Indeed, already today companies such as Facebook routinely share and mine shared information [Ops13, Yun15]. In 2012, (at least some of) this sharing was performed with insecure naive hashing. Today, companies are able and willing to tolerate a reasonable performance penalty, with the goal of achieving stronger security [Yun15]. We believe that the ubiquity and the scale of private data sharing, and PSI in particular, will continue to grow as big data becomes bigger and privacy becomes a more recognized issue.

### Related work

We classificate existing PSI protocols into categories as below.

#### (Insecure) Naive Hashing

Naive hashing is an *insecure* solution for PSI even most commonly used, except for rare cases.In the protocol,$$P_2$$ samples a random $$2k$$-bit salt $$k$$ and sends it to $$P_1$$. Both parties then use a cryptographic hash function $$H:\{0,1\}^* \rightarrow \{0,1\}^l$$ to hash their elements salted with k.Namely,$$P_1$$ computes $$h_i = H(x_i \oplus k)$$ for each element $$x_i$$.Similarly,$$P_2$$ does the same,$$P_1$$ then randomly computes the hash values $$h_i$$ and sends them to $$P_2$$, which computes the intersection as the elements for which there exists a j such that $$h_i=h_j^,$$.

