---
layout: post
title: private set intersection
date: 2019-08-22 14:13:27 +0800
categories: Crypto-theory
---

<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

## what-have-I-learned-as-a-cryptomania-so-far?

* Garbled circuits
* General public key cryptography and security modeling
* several security protocols
* secret sharing technique


## Idea Incubator

* Authorized PSI techinique? **Each element in the client set must be authorized for sharing by some recoginzed**

* Feasible attacking method on current PSI problem

* Privately computing set operations
	* Privately computing set union cardinality
	* Privately computing set intersection cardinality combing with general two number add using simple homomorphic encryption
		* <span style="color: red">Using OPRF protocl and bloom filter, then firstly get a permuation of $$BF_A$$, then bitwise OR of $$BF_B \: and \: BF_A$$,finally get set union cardinality.</span>
	* Using bloom filter


	
# Engineering part of libOTe
To make vs code works for detecting including path in c/c++ extension gui, set
	"includePath": [
	                "/usr/include",
	                "/usr/local/include",
	                "${env:PYTHON_LIB_TENSORFLOW}/include/",
	                "${env:PYTHON_LIB_TENSORFLOW}/include/external/nsync/public",
	                "${workspaceRoot}"
	            
	 }

Trying to figure out difference between Arithmetic & Bool & Yao of [ABY Framwork][ABY Link].


## Paper lists  regarding engineering of MPC
	* ABY – A Framework for Efficient Mixed-Protocol Secure Two-Party Computation_( From the paper [DSZ15][DSZ15 link])
	* **Thomas Schneider** famous doctoral paper: Engineering Secure Two-Party Computation Protocols

Paper Names | Amateur review  | Valuable parts  | unknown or what being too hard
--------------|:-----:|-----:| ----
Secure Two-Party Computation is Practical | The author improve secure computation under malicious adversary. Feasible AES computation under malicious adversary. A protocol with security under covert adversary |   |    
Engineering Secure Two-Party Computation Protocols |  |  -- |   
Efficient Oblivious Transfer Protocols(Naor Pinkas OT)  | using C/PK_0 technique and random oracle, successfully constructing a efficient OT(1,N) | one by one improvement in protocols| implementing distance from reality  
OT: The Simplest Protocol for Oblivious Transfer| | | 
IKNP protocl: Extending Oblivious Transfers Efficiently| | | 


## Definition of OT
Oblivious Transfer (OT) is a cryptographic primitive defined as follows: in its simplest flavour, 1-out-of-2 OT, a sender has two input messages M0 and M1 and a receiver has a choice bit c. At the end of the protocol the receiver is supposed to learn the message Mc and nothing else, while the sender is supposed to learn nothing.

## Applicaitons of OT
* Serves as a fundamental cryptographic primitive for secure 2-party computation
* garbled circuit private key retrieval
* private information retrieval
* GMW protocol [O. Goldreich, S. Micali and A. Wigderson. How to play any mental game – A completeness theorem for protocols with honest majority. In 19th STOC, 218–229, 1987.]


## Concrete implementations of OT
Different OTs are implemented from different papers:
*  Naor-Pinkas [M. Naor, B. Pinkas: Efficient oblivious transfer protocols. SODA 2001: 448-457]
*  Peikert-Vaikuntanathan-Waters [C. Peikert, V. Vaikuntanathan, B. Waters: A Framework for Efficient and Composable Oblivious Transfer. CRYPTO 2008: 554-571] 
*  Chou-Orlandi [T. Chou, C. Orlandi: The Simplest Protocol for Oblivious Transfer] ![diagram](/assets/simplest_OT.png)

### Explore the simplest OT protocol

Follow the [LibOTe][LibOTe Link], and to compatiate with ABY and libOTE,then I need to degrade boost to version 1.69.0 ,so trying compatiency with boost 1.70.0 <**But it turns out these 2 versions are compatiable**>

	cmake . -DENABLE_NASM=OFF -DENABLE_SIMPLESTOT=ON

but when ENABLE_SIMPLESTOT is switched on, I encountered "SimplestOT/fe25519_nsquare.s:503:1: error: 32-bit absolute addressing is not supported in 64-bit mode" issue, this being too techincal for me to solve. So I have to go back to test the other base OT protocols.

### Explore IKNP OT(Not base OT)

This seems to be an extention of OT, it could convert a large scale of OTs to a smaller OTs, 

Related work & Basic idea & Refined idea & Security proof 


What's the essece of code implementation of secure computation? 
	The author's knowledge of every protocol and a few programming skill and engineering technique.

	What kind of usage does it have? Two news,bad or good news every time,Use OT transfer to fetch message

And how do we learn them?

### Explore Naor-Pinkas OT(Not base OT)![naorpinkas](/assets/noar_pinkas_0.png)
Improved efficiency of applications
Provided that first two round of OT doesn't rely on random oracle model

processing engineering issues:
	when compile my own pure project, found that ecc lib is not enabled,
	so begin to rely on miracl library firstly,but unsuccessful, 
	then forward to rely on relics library, firstly relic is compiled, then in cmakelists command it to rely on the built library.
	Then go forward to install into system path, and things worked alright.
	New errors when making a pure target, meeting with various errors,so finally abort this task.

	Finally under the old framework, combing cryptotools and librelic constructed this ot transfer successfully, but got probability running with some errors.


## Efficiency comparaion of the aforementioned OTS <fill sender and receiver with long bitlen>






Then we proceed to OT techinical details.

[DSZ15 link]: localhost://../summerlearning/
[ABY Link]: https://github.com/encryptogroup/ABY
[LibOTe Link]: https://github.com/osu-crypto/libOTe





## Reviewing the codes of naor-pinkas ot, but just realizing it to be invaluable because:
* bad codes style
* latent bugs
* not really helpful to comprehend this protocol

## Then I go to PSI review, intended to compare the latest protocol with the low-quality paper on Rational numbers PSI
* work is still going on...




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
