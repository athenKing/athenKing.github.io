---
layout: post
title: trojan optimization
date: 2020-06-03 22:20:18 +0800
categories: Engineering-Pieces
---

## using internal vps server as a relay:

* Use iptable to relay network flow on specified server port
```
https://github.com/arloor/iptablesUtils
```
* Set up the firewall strategy on the server end to meet the needs above.
***Notice that if your relay server was wit not certificated,the certificate verification would fail!!So you need to turn off 'verify field' in the local config file.***


## Optimize trojan client efficiency by turning on a few compiling flags

* Turn on tcp fast open option (this would decrease one round cost when establing a tcp connection)

* Turn on ENABLE_TLS13_CIPHERSUITES option (this would guarantee the state of the art security)