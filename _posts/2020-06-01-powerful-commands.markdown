---
layout: post
title: powerful-commands
date: 2020-06-01 08:50:40 +0800
categories: academic
---


## downloading in terminal continually

proxy wget -c -t 0 -O MacTeX.pkg http://tug.org/cgi-bin/mactex-download/MacTeX.pkg

## file split and catenate

split -b *blocksize*(23 or 2k or 40m)  filename

cat split1 split2 > mergedFileName


## how to download github resources?

Typically, the resource content is contructed like this >https://raw.githubusercontent.com/user/repository/branch/filename,

So you need to combine it's browser style link like >https://github.com/nailperry-zd/The-Economist/blob/master/2019-08-31/TE_20190831.pdf
