---
layout: post
title:  "common commands of git"
<!-- date:  -->
categories: tech
---

# what to do when you create an empty directory?

echo "# athenKing.github.io" >> index.html
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/athenKing/athenKing.github.io.git
git push -u origin master

echo "PATH=$HOME/.gem/ruby/2.6.0/bin:$PATH" > ~/.bash_profile