---
layout: post
title:  "Comparation between circuits"
<!-- date:   2019-08-15 12:38:34 +0800 -->
categories: jekyll update
---


Trying to figure out difference between Arithmetic & Bool & Yao of [ABY Framwork][ABY Link].


## Paper lists  regarding engineering of MPC
	* Secure Two-Party Computation is Practical
	* ABY – A Framework for Efficient Mixed-Protocol Secure Two-Party Computation_( From the paper [DSZ15][DSZ15 link])
	* **Thomas Schneider** famous doctoral paper: Engineering Secure Two-Party Computation Protocols
Advances in Design, Optimization, and Applications of .
	* The Simplest Protocol for Oblivious Transfer
	* IKNP protocl: Extending Oblivious Transfers Efficiently
Then proceed to understand the basic primitives from OT.

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

### Explore IKNP OT 

## Efficiency comparaion of the aforementioned OTS <fill sender and receiver with long bitlen>






Then we proceed to OT techinical details.

[DSZ15 link]: localhost://../summerlearning/
[ABY Link]: https://github.com/encryptogroup/ABY
[LibOTe Link]: https://github.com/osu-crypto/libOTe
