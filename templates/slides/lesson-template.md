---
marp: true
theme: pycourse
paginate: true
size: 16:9
math: katex
title: "Lecture 04 · Functions"
description: "Package logic into reusable, testable pieces."
author: Van Tien Nguyen
header: "Lecture 04 · Functions"
footer: "Python Course · Phase 2 — Core Programming"
style: |
  /* Pick the phase colour: --phase-1 … --phase-6 */
  section { --phase: var(--phase-2); }
---

<!-- _class: cover -->
<!-- _paginate: false -->
<!-- _footer: "Lecture 04 · Phase 2 — Core Programming" -->

###### 04_functions.py

# Functions: name it *once*, use it everywhere

Package logic into reusable, testable pieces.

`Van Tien Nguyen` `⏱ 90 min` `🧱 Core Programming`

<!--
Speaker notes go in HTML comments like this one.
They show up in presenter view (Marp CLI --preview, or the HTML export).
-->

---

<!-- _class: agenda -->

###### Today

## The plan

1. Why functions? *5 min*
2. Anatomy of a function *15 min*
3. Parameters, return values & errors *20 min*
4. Quick check *5 min*
5. Your turn: build a mini toolkit *30 min*
6. Recap & what's next *5 min*

---

<!-- _class: objectives -->

###### Learning objectives

## By the end of this lecture you can…

1. **Explain** why functions make code shorter, clearer and easier to test
2. **Write** a function with parameters, defaults and a return value
3. **Tell apart** `print` and `return`, and pick the right one
4. **Read** a `TypeError` traceback and fix the call

---

<!-- _class: divider -->

###### 01

# Why functions?

From copy-paste to *name it once*.

---

<!-- _class: big -->

###### The idea

# If you wrote it **twice**, give it a name.

Copy-pasted code drifts apart. A function keeps one source of truth.

---

<!-- _class: hl-4 -->

###### Anatomy

## Anatomy of a function

<div class="cols wide-left">
<div>

```python
def area(width: float, height: float = 1.0) -> float:
    """Return the area of a rectangle."""
    result = width * height
    return result

print(area(3, 4))   # 12.0
print(area(5))      # 5.0
```

</div>
<div>

- `def` starts it
- `width`, `height`: **parameters**
- `= 1.0`: a *default value*
- `"""…"""`: the **docstring**

</div>
</div>

<div class="note br">

No `return`? You get **`None`** back!

</div>

<!-- The hl-4 class spotlights line 4 of the code block. -->

---

<!-- _class: steps -->

###### Under the hood

## What happens when you call `area(3, 4)`?

1. **Bind** `width = 3` and `height = 4` in a fresh local scope
2. **Run** the body, top to bottom
3. **Return** the value to whoever called
4. **Forget** the local variables: the scope is gone

---

###### Maths vs Python

## A function is a **machine**: input → output

<div class="cols middle">
<div class="card">

### In maths

$$
f(x) = x^2 + 1
$$

$f(3) = 10$: same input, same output, every time.

</div>
<div>

```python
def f(x):
    return x ** 2 + 1

f(3)  # 10
```

</div>
</div>

<div class="callout key">

A *pure* function only depends on its inputs: easy to reason about, easy to test.

</div>

---

###### Common mistake

## `print` is not `return`

<div class="cols">
<div class="bad">

```python
def add(a, b):
    print(a + b)

total = add(2, 3)   # shows 5
total * 10          # TypeError!
```

`total` is `None`: nothing came back.

</div>
<div class="good">

```python
def add(a, b):
    return a + b

total = add(2, 3)
total * 10          # 50
```

Return the value; let the caller decide what to do with it.

</div>
</div>

---

<!-- _class: traceback -->

###### Read the error

## **TypeError**: area() missing 1 required argument

```pytb
Traceback (most recent call last):
  File "toolkit.py", line 7, in <module>
    print(area())
          ^^^^^^
TypeError: area() missing 1 required positional argument: 'width'
```

<div class="callout">

Read tracebacks **bottom-up**: the last line says *what* went wrong, the lines above say *where*.

</div>

---

###### Parameters

## Five ways to pass arguments

| Kind | Definition | Call |
| --- | --- | --- |
| Positional | `def f(a, b)` | `f(1, 2)` |
| Keyword | `def f(a, b)` | `f(b=2, a=1)` |
| Default | `def f(a, b=0)` | `f(1)` |
| Any positional | `def f(*args)` | `f(1, 2, 3)` |
| Any keyword | `def f(**kwargs)` | `f(x=1, y=2)` |

<div class="note pink br">

Never `def f(x=[])`: that list is **shared**!

</div>

---

<!-- _class: chat -->

###### Scope, explained

## A chat with the interpreter

- **You** I set `count = 10` inside my function. Why is it gone afterwards?
- **Python** Variables created inside a function are *local*. They live only while it runs.
- **You** So how do I get the value out?
- **Python** `return count`, then catch it: `total = my_function()`

---

<!-- _class: quiz -->

###### Quick check · 1 min

## What does this print?

```python
def greet(name="world"):
    return f"Hello, {name}!"

print(greet() + " " + greet("Ada"))
```

- `Hello, world!`
- **`Hello, world! Hello, Ada!`**
- `Hello, name! Hello, Ada!`
- `TypeError`

<!-- Let students vote with fingers (1-4) before revealing. -->

---

<!-- _class: quiz reveal -->

###### Quick check · answer

## What does this print?

```python
def greet(name="world"):
    return f"Hello, {name}!"

print(greet() + " " + greet("Ada"))
```

- `Hello, world!`
- **`Hello, world! Hello, Ada!`**
- `Hello, name! Hello, Ada!`
- `TypeError`

---

<!-- _class: dark -->

###### In the terminal

## Try it in the REPL

```console
$ python3
>>> def square(x):
...     return x * x
...
>>> list(map(square, range(5)))
[0, 1, 4, 9, 16]
>>> help(square)
```

Press <kbd>Ctrl</kbd> + <kbd>D</kbd> to leave the REPL.

---

<!-- _class: divider -->

###### 02

# Practice

Learn by writing code.

---

<!-- _class: exercise -->

###### ⏱ 30 min · pairs · ★★☆

## Your turn: a mini text toolkit

Create `toolkit.py` and write these functions:

1. `word_count(text)` returns the number of words
2. `shout(text, times=1)` returns the text upper-cased, repeated `times` times
3. `initials(full_name)` turns `"Ada Lovelace"` into `"A.L."`
4. Add a docstring and type hints to each one

> **Stretch goal:** write a test for each function with `pytest` (see Lecture 12).

---

<!-- _class: recap -->

###### 🏆 Achievement unlocked · Functions · +100 XP

## What we covered

- Functions turn repeated code into **one named, reusable block**
- Parameters can be positional, keyword, default, `*args` or `**kwargs`
- `return` hands a value back; `print` only shows it
- Read tracebacks **bottom-up** to find what broke and where

---

<!-- _class: lead -->
<!-- _paginate: false -->

![w:76](../../assets/logo.svg)

###### Up next · Lecture 05

# *Recursion*: functions that call themselves

Bring your `toolkit.py`. We'll build on it.

`📦 Materials: course site` `💬 Questions: Discussions`
