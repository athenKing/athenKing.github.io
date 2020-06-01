---
layout: post
title: commonCryptoEngineer
date: 2020-05-13 12:17:53 +0800
categories: academic
---


## How to set up ssh login with certificate keys without login password?


### Enginneering approach:

prepare public-key cryptography pairs:

1. on your client terminal, use: **ssh-keygen** , then it will create rsa-3072

2. Choosing an Algorithm and Key Size

SSH supports several public key algorithms for authentication keys. These include:

rsa - an old algorithm based on the difficulty of factoring large numbers. A key size of at least 2048 bits is recommended for RSA; 4096 bits is better. RSA is getting old and significant advances are being made in factoring. Choosing a different algorithm may be advisable. It is quite possible the RSA algorithm will become practically breakable in the foreseeable future. All SSH clients support this algorithm.

dsa - an old US government Digital Signature Algorithm. It is based on the difficulty of computing discrete logarithms. A key size of 1024 would normally be used with it. DSA in its original form is no longer recommended.

ecdsa - a new Digital Signature Algorithm standarized by the US government, using elliptic curves. This is probably a good algorithm for current applications. Only three key sizes are supported: 256, 384, and 521 bits. We would recommend always using it with 521 bits, since the keys are still small and probably more secure than the smaller keys (even though they should be safe as well). Most SSH clients now support this algorithm.

ed25519 - this is a new algorithm added in OpenSSH. Support for it in clients is not yet universal. Thus its use in general purpose applications may not yet be advisable.

The algorithm is selected using the -t option and key size using the -b option. The following commands illustrate:

'' ssh-keygen -t rsa -b 4096
ssh-keygen -t dsa
ssh-keygen -t ecdsa -b 521
ssh-keygen -t ed25519 ''


### Theory under the hood:

authentication and info encryption



## On problem of 'wget' cannot verify github.com's certificate when paring https downloading?

Set wget confige file  in \~/.wgetrc; and add line

ca-certificate = /etc/ssl/cert.pem

## Openssl related commands 

### Using openssl commandline tools 

生成RSA公私钥对:

openssl genrsa -out rsakeys.pem 2048



To get sha256 hash digest from a file exampleFile (Different digesting algotithms: sha, sha1, mdc2, ripemd160, sha224, sha256, sha384, sha512, md4, md5, blake2b, blake2s)

openssl dgst -sha256 exampleFile


抽取上一级证书(\*.cer)的公钥:

openssl x509 -inform der -in GTS.cer -pubkey -noout > pubkey.pem

openssl x509 -inform der -in example.cer -pubkey -noout > pubkey.pem


显示证书里的细节:

openssl x509 -inform der -in GTS\ CA\ 1O1.cer -text -nocert


用一个私钥给文件签名:

openssl dgst -sha256 -sign rsaprivatekey.pem -sigopt rsa_padding_mode:pss -out signature.txt crtGTS.crt


用对应的公钥验证签名:

openssl dgst -sha256 -verify rsapk.pem -sigopt rsa_padding_mode:pss -signature signature.txt crtGTS.crt

抽取证书里的签名并转换成二进制格式:

# extract hex of signature
SIGNATURE_HEX=$(openssl x509 -inform der -in GTS\ CA\ 1O1.cer -text -noout -certopt ca_default -certopt no_validity -certopt no_serial -certopt no_subject -certopt no_extensions -certopt no_signame | grep -v 'Signature Algorithm' | tr -d '[:space:]:')

# create signature dump
echo ${SIGNATURE_HEX} | xxd -r -p > cert-sig.bin

从签名还原到文件:
openssl rsautl -verify -inkey pubkey.pem -in cert-sig.bin -pubin > cert-sig-decrypted.bin
openssl asn1parse -inform der -in cert-sig-decrypted.bin


抽取签名证书的主体:(即除去signature之外的部分,以二进制格式输出)
openssl asn1parse -inform der -in google.cer -strparse 4 -out cert-body.bin -noout

验证该主体部分的hash值:
openssl dgst -sha256 cert-body.bin


获取openssl x509 标准相关解析:

openssl x509 -help


## 如何使用Trojan中转vps来传递流量:

使用iputils 项目简单设置 iptables转发表，并配合vps云控制平台设置 需要开放的防火墙端口

https://github.com/arloor/iptablesUtils

中间存在 SSL handshake failed with lets-do-it.online:3333: certificate verify failed问题，需要将trojan配置中的verify选项设为false
(原因暂且未明)


### 如何优化Trojan，达到最佳优化效果

recompile trojan codes, then modify cmakefile.txt(fix openssl location error) to turn on tcp fast open option, open TLS1.3 options,

But still now session reuse is not possible for now, need to figure it out.



### 验证Trojan里的dh parameter的数据信息

#### 输出c代码形式的dh参数

openssl dhparam -inform PEM -in dh.param -C  -out dh.c

#### 输出明文形式的dh参数

openssl dhparam -inform PEM -in dh.param -text  -out dh.txt


#### 生成dh参数

openssl dhparam -2 2048 -out dh.gen


### 弄清楚Trojan里面tls1.3 cipher suite的选择及使用

server select one of the cipher suites or give it to client.

**Trojan无法代理非https形式之外的外网请求**




## 密码学算法理论(安全性，数学技巧)及其高效工程实现

### 签名

#### 带RSA加密的SHA-256

签名输入:(pk,sk)，pk to verify，sk to sign a file, output a signature Sign

sha-256(m)--> constant length-->integer in [1,q] domain

plain text M + Enc_sk{(sha256(m))}

### EC




















