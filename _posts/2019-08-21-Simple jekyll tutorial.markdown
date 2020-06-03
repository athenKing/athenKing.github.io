---
layout: post
title: jekyll tutorial
date: 2019-08-21 14:37:05 +0800
categories: Engineering-Pieces 
---



You’ll find this post in your `_posts` directory. Go ahead and edit it and re-build the site to see your changes. You can rebuild the site in many different ways, but the most common way is to run `jekyll serve`, which launches a web server and auto-regenerates your site when a file is updated.

To add new posts, simply add a file in the `_posts` directory that follows the convention `YYYY-MM-DD-name-of-post.ext` and includes the necessary front matter. Take a look at the source for this post to get an idea about how it works.

Jekyll also offers powerful support for code snippets:

{% highlight ruby %}
def print_hi(name)
  puts "Hi, #{name}"
end
print_hi('Tom')
#=> prints 'Hi, Tom' to STDOUT.
{% endhighlight %}

Check out the [Jekyll docs][jekyll-docs] for more info on how to get the most out of Jekyll. File all bugs/feature requests at [Jekyll’s GitHub repo][jekyll-gh]. If you have questions, you can ask them on [Jekyll Talk][jekyll-talk].

[jekyll-docs]: https://jekyllrb.com/docs/home
[jekyll-gh]:   https://github.com/jekyll/jekyll
[jekyll-talk]: https://talk.jekyllrb.com/



- TOC
{:toc}


<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>

Thi is paragraph
also a paragraph,even in a second line

## Concepts
* Bloom filter:
	memebership checker using two hash functions

* Cuckoo functions:
	using two functions to do hashing and storage key corresponding values

* Hamming weight:
	the occurence of 1 in a binary string, as the same as hamming **distance** from equal length 0's. 

* kramdown:
	Is just a fast, pure-ruby markdown-superset converter

## Hashing compare
In python,murmurhash is about 3 times faster than md5

## Some simple kramdown tutorials

* Making a code block with specifed language type
	~~~ ruby
	def what?
	  ruby
	end
	~~~
	~~~ python
	def md5():
	  print("this is python")
	end
	~~~
* Setting attributes of some content

	This is *red*{: style="color: red"}.

	This is <span style="color: purple">written in purple</span>.

* Abbreviations & footnotes & comments
	This is an HTML example.

	This is a text with a footnote[^1].
	<!-- { commenting here} -->

* Including latex
	
	**Before using latex, you must add below html codes**
	~~~ html
	<script type="text/javascript" async
	  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
	</script>
	~~~
$$
\begin{align*}
  & \phi(x,y) = \phi \left(\sum_{i=1}^n x_ie_i, \sum_{j=1}^n y_je_j \right)
  = \sum_{i=1}^n \sum_{j=1}^n x_i y_j \phi(e_i, e_j) = \\
  & (x_1, \ldots, x_n) \left( \begin{array}{ccc}
      \phi(e_1, e_1) & \cdots & \phi(e_1, e_n) \\
      \vdots & \ddots & \vdots \\
      \phi(e_n, e_1) & \cdots & \phi(e_n, e_n)
    \end{array} \right)
  \left( \begin{array}{c}
      y_1 \\
      \vdots \\
      y_n
    \end{array} \right)
\end{align*}
$$

* Inserting a video

<!-- <figure class="video_container">
  <iframe src="https://www.youtube.com/embed/enMumwvLAug" frameborder="0" allowfullscreen="true"> </iframe>
</figure> -->

* To use toc,just do things like this

	```
	 - TOC
	 {:toc}
	```

* To  quote ,like this

> Give whoever gives
>
> Grab whoever grabs


```
echo "PATH=$HOME/.gem/ruby/2.6.0/bin:$PATH" > ~/.bash_profile
```


<head> 
    <script defer src="https://use.fontawesome.com/releases/v5.0.13/js/all.js"></script> 
    <script defer src="https://use.fontawesome.com/releases/v5.0.13/js/v4-shims.js"></script> 
</head> 
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.13/css/all.css">

<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>



## TODO

* Find markdown check, wrong icon <i class="fas fa-check" style="color:#30fc03"></i>
	* fontawesome
	* google rgb color panel


* Thoroughly knowledge about using wildcards
	* Star wildcard(\*): arbitrary character with arbitrary length
	* question wildcard(?): one single arbitrary character
	* a pair of square brackets([a-f],[xyz]): represents a range or one of them

* The password management project


[math_latex link]: https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols





[^1]: And here is the definition.

*[HTML]: Hyper Text Markup Language