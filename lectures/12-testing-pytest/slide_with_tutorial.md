---
marp: true
theme: pycourse
paginate: true
size: 16:9
title: "Lecture 12 · Does My Code Actually Work?"
description: "Introduction to automated testing with pytest."
author: Van Tien Nguyen
header: "Lecture 12 · Testing with pytest"
style: |
  section { --phase: var(--phase-4); }

  /* number line for the "choosing cases" slide */
  .numline { display: grid; grid-template-columns: repeat(14, 1fr); gap: 6px; margin: 10px 0 6px; }
  .numline span {
    display: grid; place-items: center; height: 58px; border-radius: 10px;
    font: 700 22px "JetBrains Mono", monospace;
    background: #fff; border: 2px solid var(--line); color: var(--ink);
  }
  .numline .low  { background: #ffe4e6; border-color: #fecdd3; color: #9f1239; }
  .numline .edge { background: var(--yellow); border-color: #f59e0b; color: var(--navy); }
  .numline-labels {
    display: grid; grid-template-columns: 5fr 1fr 8fr; gap: 6px; margin-bottom: 26px;
    font: 600 17px/1.3 "JetBrains Mono", monospace; text-align: center; color: var(--muted);
  }
  .numline-labels span:first-child { color: #9f1239; }
  .numline-labels span:nth-child(2) { color: #b45309; }
---

<!-- _class: cover -->
<!-- _paginate: false -->
<!-- _footer: "Lecture 12" -->

###### test_prime.py

# Writing tests in Python

<!-- An introduction to automated testing with pytest. -->
`🛠️ EE 3233. System Programming for Enginnerings`

<!--
50-minute recitation: live coding + pair work.
Have the starter folder open (lectures/12-testing-pytest/starter), terminal text large,
code and test output visible together.
-->

---

## Does this function **work**?

<div class="cols middle">
<div>

```python
def is_prime(n):
    for divisor in range(2, n):
        if n % divisor == 0:
            return False
    return True
```

</div>
<div>

```pycon
>>> is_prime(7)
True
>>> is_prime(8)
False
```

</div>
</div>

<div class="callout key">

Which **other input** could reveal a bug? Write down the input **and** the result you expect.

</div>

<!--
Show 7 and 8 working live. Students think alone (30 s), then compare with a partner.
Collect a few suggestions and their expected outputs.
Check: "Why should 1 return False?" Invite more than one explanation.
-->

---

<!-- _class: objectives -->

## By the end of class you can…

1. **Write** pytest test functions with `assert` and a meaningful expected result
2. **Run** `python -m pytest -q` and find the **actual** and **expected** values in a failure
3. **Choose** ordinary and boundary inputs, and explain why they matter
4. **Fix** a simple bug and rerun the whole test suite

<!--
Why automated tests: they are repeatable checks you can rerun every time the code changes.
Connect to debugging a previous assignment.
Check: "What does a print statement leave you to check manually?"
-->

---

<!-- _class: steps -->

## Every test compares two things

<div class="callout key">

**Contract:** for any integer `n`, return `True` exactly when `n` is prime. Integers less than 2 are not prime.

</div>

1. **Input** the value we call the function with: `is_prime(7)`
2. **Expected** what the contract says should happen: `True`
3. **Actual** what the code really returns
4. **Compare** the same: the test passes. Different: it fails

<!--
State the contract BEFORE judging the code.
Do not introduce input-type validation in this lesson.
-->

---

<!-- _class: hl-6 -->

## A pytest test: file, function, **assertion**

<div class="cols wide-left">
<div>

```python
# test_prime.py
from prime import is_prime


def test_seven_is_prime():
    assert is_prime(7) is True


def test_eight_is_not_prime():
    assert is_prime(8) is False
```

</div>
<div>

- **File** name starts with `test_`
- **Function** name starts with `test_` and says what it checks
- **`assert`** input → expected result
- No `print`, no `main()`: pytest finds the tests by name

</div>
</div>

---

<!-- _class: compact -->

## Installing pytest on Linux

Run these commands from your project folder:

```bash
# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install pytest
python -m pip install pytest

# Verify the installation
python -m pytest --version
```

**Ready when:** the last command prints the installed pytest version.

Keep the environment activated when running your tests.

---

## Run the tests, then **read the result**

```console
$ python -m pytest -q
..                                                       [100%]
2 passed in 0.00s
```

<div class="cols c3">
<div class="card">

### `.`

One dot per test that **passed**.

</div>
<div class="card">

### `F`

A test that **failed**: its assertion was false.

</div>
<div class="card">

### Summary

How many passed, how many failed, and how long it took.

</div>
</div>

<!--
Ask students to predict the outcome before every run.
Check: "What happens when the assertion is false?"
-->

---

<!-- _class: traceback compact -->

## **AssertionError**: is_prime(1) returned True

```text
..F                                                      [100%]
    def test_one_is_not_prime():
>       assert is_prime(1) is False
E       assert True is False
E        +  where True = is_prime(1)

test_prime.py:13: AssertionError
FAILED test_prime.py::test_one_is_not_prime - assert True is False
1 failed, 2 passed in 0.02s
```

<div class="callout">

Find the **input**, the **expected** result and the **actual** result. Is the mistake in the **code** or in the **test**?

</div>

<!--
Add test_one_is_not_prime right after test_eight_is_not_prime (it lands on line 13), predict, run.
Pause on the failure. Prompts:
- What input did this test use?
- What did we expect, and what did the function actually return?
- Does the expectation match the contract?
- Why does the loop not run for 1?  (range(2, 1) is empty → falls through to return True)
-->

---

## Fix the **code**, not the test

<div class="cols">
<div class="bad">

```python
def is_prime(n):
    for divisor in range(2, n):
        if n % divisor == 0:
            return False
    return True
```

1 slips through: the loop never runs.

</div>
<div class="good">

```python
def is_prime(n):
    if n < 2:
        return False

    for divisor in range(2, n):
        if n % divisor == 0:
            return False
    return True
```

</div>
</div>

Rerun **all** the tests, not just the new one: `3 passed` ✅

<!--
Prompts:
- Which change handles ALL integers below 2? (n < 2, not n == 1)
- Why rerun the earlier tests after fixing this case?
Check: "Does the implementation or the test expectation need changing, and why?"
-->

---

## Choosing useful **cases**

<div class="numline">
<span class="low">-3</span><span class="low">-2</span><span class="low">-1</span><span class="low">0</span><span class="low">1</span><span class="edge">2</span><span>3</span><span>4</span><span>5</span><span>6</span><span>7</span><span>8</span><span>9</span><span>10</span>
</div>
<div class="numline-labels"><span>n < 2: the contract decides</span><span>boundary</span><span>ordinary inputs</span></div>

<div class="cols c3">
<div class="card">

### Ordinary

A typical prime and a typical composite.

</div>
<div class="card">

### Boundaries

Where the rule changes: just below, at, and just above.

</div>
<div class="card">

### Different kinds

Not only even composites: a faulty rule can hide there.

</div>
</div>

---

<!-- _class: exercise -->

## Your turn: test 0, 2 and 9

1. **Before running**, write the expected result and **why** each input is useful
2. Add a `test_` function for each one in `test_prime.py`
3. Run `python -m pytest -q`; swap driver and navigator after the first test
4. Done when: 3+ tests pass on the repaired code, and you can **both** explain one

> Describe a faulty `is_prime` that one of your tests would catch.

<!--
Instructor reference (do not show):
  0  → False  below the smallest prime
  2  → True   smallest prime, boundary of the prime region
  9  → False  odd composite; only even composites would miss some faulty rules
  17 → True   (optional) another ordinary prime
  -3 → False  (optional) negative integers per the contract
Circulate: ask each pair to justify one input.
Keep parametrization as optional follow-up only.
-->

---

## What if the bug **comes back**?

<div class="cols wide-left middle">
<div>

```python
def is_prime(n):
    # if n < 2:          ← someone deletes this
    #     return False

    for divisor in range(2, n):
        if n % divisor == 0:
            return False
    return True
```

</div>
<div>

- Which of our tests **fail** now?
- Which still **pass**?
- Why run **every** test after **every** change?

</div>
</div>

<div class="note br">

A bug that comes back is a **regression**.

</div>

<!--
Invite two pairs to share first. Then temporarily remove the guard live and rerun the suite; restore it afterwards.
Expected: tests for 1 and 0 (and -3 if added) fail; 2, 7, 8, 9 still pass.
-->

---

<!-- _class: big -->

# Passing tests are **evidence**, not proof.

They show the expected results hold **for the inputs we checked**. Are ten tests of the same kind better than three careful ones?

<!--
Also address: a failed test vs a mistaken expectation. Sometimes the test is wrong, so check it against the contract.
Ask each student: one thing a test result can tell you, and one thing it cannot.
-->

---

<!-- _class: compact -->

## pytest versus unittest

<div class="cols">
<div>

### Python's built-in `unittest`

**Structured, class-based**, and included in the standard library.

```python
from unittest import TestCase

class TryTesting(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)

    def test_always_fails(self):
        self.assertTrue(False)
```

</div>
<div>

### Plain functions with `pytest`

**Simple syntax**, flexible, with powerful features.

```python
def test_always_passes():
    assert True


def test_always_fails():
    assert False
```

</div>
</div>

**Predict:** how many pass and how many fail?

Read more: [pytest vs. unittest](https://www.geeksforgeeks.org/software-testing/difference-between-pytest-and-unittest)

<!--
Answer: each file gives one passed and one failed test (the failure is intentional).
Allow about 2 minutes.
Use this comparison to explain the framework, not TestCase inheritance.
Run each warm-up file separately so its intentional failure does not enter
the prime test suite. Pytest can run unittest-style tests as well.
Primary compatibility reference:
https://docs.pytest.org/en/stable/how-to/unittest.html
-->

---

<!-- _class: steps -->

## Arrange–Act–Assert

<div class="cols wide-left">
<div>

```python
def test_one_is_not_prime():
    # Arrange
    n = 1
    expected = False

    # Act
    actual = is_prime(n)

    # Assert
    assert actual is expected
```

</div>
<div>

**Arrange** the input and the expected result.

**Act** by calling the function.

**Assert** the expected behavior.

</div>
</div>

The specification determines what we expect. 
The function produces the actual result.

<!--
Allow about 2 minutes.
Revisit the test students already understand from the original lesson.
Ask students to identify each part before reading the labels.
For a short test, combining Act and Assert in one line is fine.
No change to the prime contract or implementation is needed.
Primary test-anatomy explanation:
https://docs.pytest.org/en/stable/explanation/anatomy.html
-->

---

<!-- _class: compact -->

## Several cases in one test

```python
import pytest
from prime import is_prime


@pytest.mark.parametrize("n, expected", [
    (0, False), (1, False),
    (2, True), (9, False),
    (17, True),
])
def test_prime_cases(n, expected):
    assert is_prime(n) is expected
```

Each tuple supplies `n` and `expected`. Pytest reports **five separate results**.

<!--
Optional extension, about 2–3 minutes.
25 is left out on purpose: it is the exit-ticket question.
Introduce after students can write ordinary test functions.
Run the example against the repaired prime implementation.
Expected: 5 passed. The decorator's names match the function arguments.
The tutorial uses palindrome inputs to motivate parametrization.
This adaptation reuses the class's prime inputs to avoid a new algorithm.
Primary syntax reference:
https://docs.pytest.org/en/stable/how-to/parametrize.html
-->

---

<!-- _class: compact -->

## Application: formatting records for display

A program receives people records and prepares readable directory entries.

<div class="cols">
<div>

```python
def format_people(people):
    rows = []
    for person in people:
        name = (
            f"{person['given']} "
            f"{person['family']}"
        )
        rows.append(
            f"{name}: {person['role']}"
        )
    return rows
```

</div>
<div>

```python
def test_directory_entry():
    people = [{
        "given": "Emma",
        "family": "Wilson",
        "role": "Engineer",
    }]

    assert format_people(people) == [
        "Emma Wilson: Engineer"
    ]
```

</div>
</div>

**Your next case:** what should the function return for an empty list?

<!--
About 3 minutes, or use as additional practice.
Demo files: code/formatters.py and code/test_formatters.py.
This adapts the tutorial's real-application data-formatting scenario.
The names and records here are synthetic classroom data.
The contract for this exercise: preserve record order, output one string per
record, and use the given/family/role fields exactly as supplied.
Assume those fields exist and contain strings. Empty input returns [].
Ask students to identify Arrange, Act, Assert. The test uses in-memory data
representative of an API response. No live service is required.
A second function in the example module exports the same records to CSV.
-->

---

<!-- _class: compact -->

## A fixture supplies reusable test data

<div class="cols">
<div>

```python
import pytest
import formatters as fmt


@pytest.fixture
def people():
    return [{
        "given": "Emma",
        "family": "Wilson",
        "role": "Engineer",
    }]
```

</div>
<div>

```python
def test_display(people):
    assert fmt.format_people(people) == [
        "Emma Wilson: Engineer"
    ]


def test_csv(people):
    expected = (
        "given,family,role\n"
        "Emma,Wilson,Engineer\n"
    )
    assert fmt.export_csv(people) == expected
```

</div>
</div>

The test requests `people` as an argument. **Pytest calls the fixture** and supplies its result.

<!--
Optional extension, about 3 minutes.
This demonstrates the motivation for a fixture: two transformations use the
same representative input records. Both functions live in formatters.py.
The included export_csv uses Python's csv module, so CSV quoting is handled.
For this classroom contract, the header is given,family,role and line endings
are newline characters. That keeps the expected string platform-independent.
The default fixture scope creates a fresh list for each test.
Explain only the decorator and the matching argument name. Keep fixture scopes,
conftest.py, mocking, markers, durations, and plugins for later study.
Primary fixture behavior:
https://docs.pytest.org/en/stable/how-to/fixtures.html
-->

---

<!-- _class: compact -->

## What we covered

| Topic | Key idea |
|---|---|
| **Unit tests** | Use `test_` functions and `assert` to check behavior. |
| **Arrange–Act–Assert** | Prepare inputs, call the function, compare results. |
| **Test cases** | Check ordinary inputs, boundaries, and special cases. |
| **Failures and regressions** | Read the failure, fix the bug, rerun the suite. |
| **Parametrization** | Run one test with several input–expectation pairs. |
| **Fixtures** | Request reusable test data through named arguments. |

**Passing tests provide evidence for the cases we checked.**

---

<!-- _class: exercise -->

## Before you leave

1. Write a pytest test for `is_prime(25)`
2. What faulty behavior could it catch that a test using only `8` might miss?
3. If every test passes, does that prove the function is correct for every integer? Explain briefly.

> 📚 [pytest: Get Started](https://docs.pytest.org/en/stable/getting-started.html) · **Next:** run this test suite automatically with GitHub Actions (Lecture 15)

<!--
Reference:
  def test_twenty_five_is_not_prime():
      assert is_prime(25) is False
25 is an odd composite: it exposes a function that wrongly labels every odd number > 1 as prime.
Passing tests only show the tested expectations hold for those cases.
Use as a formative check; don't grade aloud.
-->
