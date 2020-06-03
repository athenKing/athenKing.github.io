---
layout: post
title: Crypto scenerio in normal life
date: 2020-05-13 12:17:53 +0800
categories: Crypto-Application
---

### How to set up ssh login with certificate keys?

* Firstly generate public-key crptographic key pairs satisfying ssh specification
	 ```
	 ssh-keygen -t rsa -b 4096
	 ssh-keygen -t dsa
	 ssh-keygen -t ecdsa -b 521
	 ssh-keygen -t ed25519
	 ```

* Then put PK on server and OK inside client keychains


### Solve wget **use --no-check-certificate** warning

In confige file \~/.wgetrc add line
```
 ca-certificate = /etc/ssl/cert.pem
```

### Verify the validity of chrome certificate signature manually

* 1.Drag the chrome certificates directly into local directory, then you get issuer and current node's certificate in format
```
xx.cer
```
If you want to change the cer der formatted file into a pem formatted file
```
openssl x509 -inform der -in XXX.cer -out XXX.pem
```

* 2.How to extract the public-key
```
openssl x509 -in xxx.pem -pubkey -noout > pubkey.pem
```
Display the signature and algorithms used inside the same certificate file (
This is much the same like the browser display)
```
openssl x509  -in xxx.pem -text -nocert
```
If you want to specify the sigature Algorithm output,
```
openssl x509 -in XXX.pem -text -noout -certopt ca_default -certopt no_validity -certopt no_serial -certopt no_subject -certopt no_extensions -certopt no_signame
``` 

* 3.Dump the signature into a binary file
```
#extract hex of signature
SIGNATURE_HEX=$(openssl x509 -in XXX.pem -text -noout -certopt ca_default -certopt no_validity -certopt no_serial -certopt no_subject -certopt no_extensions -certopt no_signame | grep -v 'Signature Algorithm' | tr -d '[:space:]:')
#create signature dump
echo ${SIGNATURE_HEX} | xxd -r -p > cert-sig.bin
```

* 4.Verifying the signature with issuer's public key
```
openssl rsautl -verify -inkey issuer.pem -in cert-sig.bin -pubin > cert-sig-decrypted.bin
```
Then we parse the decrepted output
```
openssl asn1parse -inform der -in cert-sig-decrypted.bin
0:d=0  hl=2 l=  49 cons: SEQUENCE          
2:d=1  hl=2 l=  13 cons: SEQUENCE          
4:d=2  hl=2 l=   9 prim: OBJECT            :sha256
15:d=2  hl=2 l=   0 prim: NULL              
17:d=1  hl=2 l=  32 prim: OCTET STRING      [HEX DUMP]:0640F8D13C0789FF0ED5437CF4BC9F2827D52146DDDFF38AEFC2C17747D45F28
```
The certificate info be like this
```
openssl asn1parse -i -in XXX.pem
```
We can extract this data and store it to disk like so
```
openssl asn1parse -in XXX.pem -strparse 4 -out cert-body.bin -noout
```
Finally we can run the same hash algorithm to determine the digest
```
openssl dgst -sha256 cert-body.bin
SHA256(cert-body.bin)= 0640f8d13c0789ff0ed5437cf4bc9f2827d52146dddff38aefc2c17747d45f28
```



















