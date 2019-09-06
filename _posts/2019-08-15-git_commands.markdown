---
layout: post
title:  "common commands of git"
<!-- date:  -->
categories: tech
---

## what to do when you create an empty directory?

echo "# athenKing.github.io" >> index.html
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/athenKing/athenKing.github.io.git
git push -u origin master

echo "PATH=$HOME/.gem/ruby/2.6.0/bin:$PATH" > ~/.bash_profile


## how to download github resources?

Typically, the resource content is contructed like this >https://raw.githubusercontent.com/user/repository/branch/filename,

So you need to combine it's browser style link like >https://github.com/nailperry-zd/The-Economist/blob/master/2019-08-31/TE_20190831.pdf

to make it like this>