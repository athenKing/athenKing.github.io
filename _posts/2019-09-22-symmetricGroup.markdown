---
layout: post
title: symmetricGroup
date: 2019-09-22 15:21:49 +0800
categories: academic
---

<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>


Questions?

1. if $$ g^{n!} = I $$ Absolutely!! why again? Prove it.

for any x, it's we could construct the set $$ {x,x^2,...,x^{|G|}} $$

the set either be a repetition or as the same as G, enumerate the set, the number of 
all different elements is either |G| or less than |G|, in former cases, it must be x^{|G|} = e,
if not, we say x^d=e,then x^d+1=x,it's a contradiction.

And by the second cases, we say x^r = x^s, then x^{s-r} = e. and x^{s-r} is \in $$ {x,x^2,...,x^{|G|}} $$

so {a,..a^{s-r}} is a subgroup of G, by langrange's theorem, |sub| | |G|.


2. who is I ? keep-still operation is the identity.

3. the sub-group property of a group? Langrange's theorem

4. how many generators of a symmetic group? from [,|G| ]


5. difference about position permutation and elemental bijection?


for group of order 2, it must contains a,e where a^2 = e

for group of order 3, it must be with structure a1, a2, e where a1 * a2 = e

...

6.what's the juxtaposing representation of the permutations?

[1, 2, 3, 4]
(1)(2)(3)(4)
[2, 3, 4, 1]
(1234)
[3, 4, 1, 2]
(13)(24)
[4, 1, 2, 3]
(2143)

(12)&(23)

f(1)=3
f(2)=1
f(3)=2

132

6. what's the cayley graph?

7. Are there any commutative permutaitons exists?
Yes, disjoint permutations!!



## Symmetric Group

* A group whose elements are those bijection funciton of one set with Length n.

* This group is with total $$n!$$ elements.

* This group statisfies associativity, closure, identity, inversable axioms.

	* for $$ \forall g \in G, g^{n!} = I, in which (I = ) $$