---
layout: post
title: avxOptimize
date: 2019-09-04 10:20:11 +0800
categories: tech
---


## How to do AVX optimization for cryptographic algorithms?Thorough knowledge about this.

* AVX Implementation vs General Implementation on FrodoKEM
	* Performance comparison (**normal** vs **avx optimized** )
	![normal](/assets/normal_frodo640.png)
	![normal](/assets/avx_frodo640.png)


* General avx2 optimization code and intructions

	* sha3 hash function is implemented x4 version.So Firstly just use it.
	* 



## Questions needed to be answered before work

* What's the scoring standard for the signature algorithm?
* Do we use hash3 cryptographic funciton?
* 