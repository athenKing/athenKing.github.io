---
layout: post
title: openssl-commands
date: 2020-05-31 23:33:41 +0800
categories: academic
---

### Generating KeyPairs:

*	Private KeyGen: 

	openssl genrsa -out rsaprivate.pem 1024/2048

*   Display details about privatekey:

	openssl rsa -in rsaprivate.pem -text -inform PEM -noout

*   Extract public key from PrivateKey: 
	
	openssl rsa -in rsaprivate.pem -outform PEM -pubout -out public.pem

* 	Display details about publicKey:

	openssl rsa -pubin -text -modulus -in warmup -in public.pem


### Encrypt/decrypt from pubkey:

#### Encryption 

**Public-key crypto is not for encrypting arbitrarily long files**

**The encryption limit of RSA encrypt input is:XX(no more than rsa N:1024,2048,4096...)**

-pubin(tell it the key input is public key)

two equivalent ways

* 	openssl rsautl -encrypt -pubin -inkey public.pem -in alice.txt -out cipher.bin

*	echo 'alice' | openssl rsautl -encrypt -pubin -inkey public.pem >cipher.bin

#### Decryption

openssl rsautl -decrypt -inkey rsaprivate.pem -in cipher.bin -out plain.txt


### Sign/vrify within RSA by openssl:

**Surely, you can use rsa sign directly, but this just calls RSA_private_encrypt**

**So we usually use rsaSignwithSHA256 etc.**

#### Hash a file using SHA256

* openssl dgst -sha256 alice.txt 

#### Sign a SHA256 tag

* openssl dgst -sha256 alice.txt|openssl rsautl -sign -inkey rsaprivate.pem >sign.out

#### Verify a rsa signature

* openssl rsautl -verify -pubin -inkey public.pem  -in sign.out