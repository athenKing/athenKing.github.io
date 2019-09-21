---
layout: post
title: latex_paper_tech
date: 2019-09-10 11:27:19 +0800
categories: academic
---

## How to do references?

* Firstly, make a mybib.bib file in your working directory, then you add data into the file
as your reference database. Afterwards, add those codes into your latex coding:

	~~~
	\cite{mycite}

	\bibliography{mybib}

	\bibliographystyle{myStyle}//like: abbrv,ieeetr
	~~~

Then the setting for References is finished!

## How to divide a tex?

* Using \input command to include chapter or sections
 
## How to make a interacting protocol?