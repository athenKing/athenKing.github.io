---
layout: post
title: psi_journey
date: 2019-08-22 14:13:27 +0800
categories: academic
---

<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

## PSI(private set intersection) problem and it's solution

Most of the content are from these 3 papers:
* [PSZ14] Faster private set intersection based on OT extension[^PSZ14].
* [PSSZ15]Phasing: Private Set Intersection using Permutation-based Hashing[^2]
* Efficient Batched Oblivious PRF with Applications to Private Set Intersection[^3]
* SpOT-Light: Lightweight Private Set Intersection from Sparse OT Extension [^4]
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


## Preliminaries

* OPRF

<span style="color: red">An oblivious pseudorandom function (OPRF)  is a protocol in which a sender learns (or chooses) a random PRF seed s while the receiver learns $$F(s,r)$$, the result of the PRF on a single input r chosen by the receiver. While the general definition of an OPRF allows the receiver to evaluate the PRF on several inputs, in this paper we consider only the case where the receiver can evaluate the PRF on a single input.That is, the receiver has an input $$r \in \{0,1\}^* $$ and learns the value $$R(r)$$, while the sender obtains the ability to evaluate $$R(r^')$$ for any string $$r^'$$, where R is a pseudorandom function.</span>


## Related work

We classificate existing PSI protocols into categories as below.

#### (Insecure) Naive Hashing

Naive hashing is an *insecure* solution for PSI even most commonly used, except for rare cases.In the protocol,$$P_2$$ samples a random $$2k$$-bit salt $$k$$ and sends it to $$P_1$$. Both parties then use a cryptographic hash function $$H:\{0,1\}^* \rightarrow \{0,1\}^l$$ to hash their elements salted with k.Namely,$$P_1$$ computes $$h_i = H(x_i \oplus k)$$ for each element $$x_i$$.Similarly,$$P_2$$ does the same,$$P_1$$ then randomly computes the hash values $$h_i$$ and sends them to $$P_2$$, which computes the intersection as the elements for which there exists a j such that $$h_i=h_j^,$$.

<span style="color: red">Security:</span> Because both parties share the same salt k, then $$P_2$$ could bruce attack the protocol by simply computing $$ \forall x \in X, 1 \leq i \leq n_1 H(x \oplus k) \stackrel{?}{=} h_i$$. Thus for some domain, it's insecure. And this attack is relevant for many settings, say, where the inputs are ip addresses, credit card numbers,names, social security numbers, etc. Also *forward-security is not guaranteed*{: style="color:red"}, since an attacker can compute wheter a specific element was part of the other party's set if the attacker learns the element after the protocol execution.

#### Server-aided PSI

#### Public-key Cryptography bashed PSI

#### PSI based on Generic Protocols

#### OT-based PSI

#### *Batched Oblivious PRF based PSI Combining Cuckcoo hash functions*{: style="color:red"}

* In general overview
	OPRF + Cuckoo Hashing


## Main results of PSZ14

* The Basic PEQT(private equality test) Protocol

 Assume two Party $$P_1$$ with $$X$$ ,$$P_2$$ with $$Y$$, their message length is $$l$$. Then execuate $$(_1^2)OT_l^\sigma$$ according to the bits of receiver $$m_l$$.
 $$ P_1 $$ then computes $$m_{P_1} = \oplus{_{i=1}^\sigma}s{_{x[i]}^i}$$,$$P_2$$ does the same,so they finally could compute the equality privately.

 *Improvement: Hashing the values into several shorter bits on several hash functions before comparing PEQT*{: style="color: red"}


* The Basic Private Set Inclusion Protocol

 Parallel invocation of the above PEQT Protocol which use the same round of $$ (_N^1)OT$$ but longer random string inside.
Additionally only final hashing results is added compared with original PQET.

* The final OT-Based PSI Protocol

 	Simply invokes the private set inclusion protocol for every $$ y \in Y$$.

* Hashing scheme used in PSI

* This technique is used to reduce the comparasion times in the final intersection checking phase. Reduce complexity from $$ \mathcal{O}(n_1 n_2)$$ to $$ \mathcal{O}(c \cdot min(n_1,n_2))$$ 


## Main results of PSSZ15

**We must carefully analyse the failure situation when hashing (still in inserting conflict when hashing under a guideline)**

* Reducing the bit-length of the stored items based on a permutation-based hashing technique. a.k.a hashing schemes.

* Just one mask for per bin when masking two hashing tables

* Use 3 cuckoo hashing functions for optimized efficiency

## Main results of [KKRT16]

* Just one 1-out-of-2 OT to do arbitrary length OPRF(Which need tons of OTs in the past PSI protocols) 

<!-- <span style="color: red"></span> -->

## Remaining questions?

* Is any symmetric technique used in PSI protocol construction?
	
	<span style="color: red">(There indeed got some in garbled circuit, but not be in PSI here too!)</span>

* The main contribution of PSZ14 when using OT?
	* naive using to construct PEQT protocol, and then the inclusion protocol, then the intersection protocol

*  

[^PSZ14]:Benny Pinkas, Thomas Schneider, and Michael Zohner. Faster private set intersection based on OT extension. In Kevin Fu and Jaeyeon Jung, editors, 23rd USENIX Security Symposium, USENIX Security 14, pages 797–812. USENIX Association, 2014

[^2]:Pinkas, Benny, et al. "Phasing: Private set intersection using permutation-based hashing." 24th {USENIX} Security Symposium ({USENIX} Security 15). 2015.

[^3]:Kolesnikov, Vladimir, et al. "Efficient batched oblivious PRF with applications to private set intersection." Proceedings of the 2016 ACM SIGSAC Conference on Computer and Communications Security. ACM, 2016

[^4]: Pinkas, Benny, et al. "SpOT-Light: Lightweight Private Set Intersection from Sparse OT Extension." (2019).
 


