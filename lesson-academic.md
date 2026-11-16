---
marp: true
theme: pycourse-academic
paginate: true
size: 16:9
math: katex
title: "Lecture 09 · Hashing"
description: "How dictionaries find things in constant time."
author: Van Tien Nguyen
footer: "Python Course · Lecture 09 · Hashing"
style: |
  /* Accent colour. The original academic theme used #800000 (maroon). */
  section { --color-highlight: #1e3a8a; }
---

<!-- _class: lead -->
<!-- _paginate: false -->
<!-- _footer: "" -->

# Hashing: finding things in **constant time**

### How Python's `dict` and `set` look up a key without searching

**Van Tien Nguyen**
Python Course · Lecture 09
November 2026

---

<!-- _class: toc -->
<!-- _header: Outline -->

## Outline

1. Hash functions _3_
2. Collisions and their cost _4_
3. Hashing in Python _5_
4. Pitfalls _6_
5. References _8_

---

<!-- _header: 1. Hash functions -->

## What is a hash function?

<div class="definition" data-title="Hash function">

A function $h : U \to \{0, 1, \dots, m-1\}$ that maps every key in a large universe $U$ to one of $m$ **buckets**.

</div>

A good hash function is _fast_, _deterministic_ and spreads keys evenly.<sup>1</sup>

```pycon
>>> hash(42), hash(-1)
(42, -2)
```

> <sup>1</sup> CPython randomises `hash()` for `str` between runs unless `PYTHONHASHSEED` is set: a defence against collision attacks.

---

<!-- _header: 2. Collisions and their cost -->

## The cost of a collision

<div class="columns">
<div>

<div class="theorem" data-title="Chaining">

Under simple uniform hashing, an unsuccessful search with chaining takes expected time $\Theta(1 + \alpha)$, where $\alpha = n/m$ is the **load factor**.<sup>2</sup>

</div>

</div>
<div>

<div class="proof">

Each key lands in a given bucket with probability $1/m$, so the expected chain length is $n/m = \alpha$. Hashing costs $O(1)$, then we scan the chain.

</div>

</div>
</div>

Keep $\alpha$ small by resizing the table, and lookups stay $O(1)$ on average.

> <sup>2</sup> Cormen et al., _Introduction to Algorithms_, ch. 11 [1].

---

<!-- _class: hl-3 -->
<!-- _header: 3. Hashing in Python -->

## `dict` does the hashing for you

<div class="columns">
<div>

```python
ages = {}
ages["Ada"] = 36  # → bucket
ages["Ada"]       # same bucket
"Grace" in ages   # O(1) avg
```

</div>
<div>

| Strategy        | Used by            |
| --------------- | ------------------ |
| Chaining        | Java `HashMap`     |
| Open addressing | CPython `dict` [3] |
| Cuckoo hashing  | some databases     |

</div>
</div>

---

<!-- _header: 4. Pitfalls -->

## Pitfalls

<div class="columns">
<div>

<div class="alertblock" data-title="Mutable keys">

```python
d = {[1, 2]: "x"}
# TypeError: unhashable type: 'list'
```

A list can change, so its hash could change.

</div>

</div>
<div>

<div class="exampleblock" data-title="Use a tuple instead">

```python
d = {(1, 2): "x"}
d[(1, 2)]  # 'x'
```

Tuples of hashable values are hashable.

</div>

</div>
</div>

---

<!-- _class: big invert -->
<!-- _header: Key takeaway -->

## A `dict` lookup doesn't _search_. It **computes** where to look.

Hash the key, jump to the bucket, done.

---

<!-- _class: references -->
<!-- _header: References -->

## References

1. T. H. Cormen, C. E. Leiserson, R. L. Rivest, C. Stein. _Introduction to Algorithms_, 4th ed. MIT Press, 2022.
2. Python Software Foundation. _The Python Language Reference_, `object.__hash__`. docs.python.org
3. CPython source, `Objects/dictobject.c`: notes on the open-addressing probe sequence. github.com/python/cpython
