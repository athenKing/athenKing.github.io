---
layout: post
title: openssl-commands
date: 2020-05-31 23:33:41 +0800
categories: Crypto-Application
---

## Hash Algorithms

To get sha256 hash digest from a file exampleFile (Different digesting algotithms: sha, sha1, mdc2, ripemd160, sha224, sha256, sha384, sha512, md4, md5, blake2b, blake2s)

```
openssl dgst -sha256[sha, sha1, mdc2, ripemd160, sha224, sha256, sha384, sha512, md4, md5, blake2b, blake2s] exampleFile
```





<!-- --------------divide line----------divide line---------------------------------- -->

## RSA

### Generating KeyPairs:

*	Private KeyGen: 
	```
	openssl genrsa -out rsaprivate.pem 1024/2048
	```
	
	

*   Display details about privatekey:
	```
	openssl rsa -in rsaprivate.pem -text -inform PEM -noout
	```

*   Extract public key from PrivateKey: 

	```
	openssl rsa -in rsaprivate.pem -outform PEM -pubout -out public.pem
	```

* 	Display details about publicKey:

	```
	openssl rsa -pubin -text -modulus -in warmup -in public.pem
	```

### Encryption 

**!!!Public-key crypto is not for encrypting arbitrarily long files!!!**

On encypting m that [length(m) < RSA Moudlar N=1024,2048,4096...]

There are two equivalent ways in commandline  -pubin(tell it the key input is public key)

 ```
 openssl rsautl -encrypt -pubin -inkey public.pem -in alice.txt -out cipher.bin
 echo 'alice' | openssl rsautl -encrypt -pubin -inkey public.pem >cipher.bin
 ```

### Decryption

 ```
 openssl rsautl -decrypt -inkey rsaprivate.pem -in cipher.bin -out plain.txt
 ```


### Sign

We usually use rsaSignwithSHA256 etc

#### Hash a file using SHA256

 ```
 openssl dgst -sha256 alice.txt
 ``` 

#### Sign a SHA256 tag

 ```
 openssl dgst -sha256 alice.txt | openssl rsautl -sign -inkey rsaprivate.pem >sign.out
 ```

### Verify

 ```
 openssl rsautl -verify -pubin -inkey public.pem  -in sign.out
 ```


## DH parameters

* generating
```
openssl dhparam -2 2048 -out dh.param
```
* output in c-style
```
openssl dhparam -inform PEM -in dh.param -C  -out dh.c
```
* output in clear text
```
openssl dhparam -inform PEM -in dh.param -text  -out dh.txt
```