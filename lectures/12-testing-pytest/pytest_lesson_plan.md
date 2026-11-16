# EE 3233: Introduction to Automated Testing with pytest

**Lesson title:** Does My Code Actually Work?  
**Instructor:** Van Tien Nguyen  
**Format:** 50-minute recitation with live coding and pair work  
**Context:** Teaching observation; introduction to automated testing  
**Assumptions:** Students can write Python functions, use imports, and run a script from a terminal. Adjust the timing if the observation period differs.

## Purpose

Students move from checking a program with a few print statements to writing repeatable tests with explicit expected results. A small `is_prime()` example connects the lesson to the recent prime-counting demonstration without requiring concurrency concepts.

**Driving question:** How can we find a bug in a function that seems to work?

## Learning objectives and evidence

By the end of class, students should be able to:

| Objective | Evidence collected during class |
| --- | --- |
| Write pytest test functions using `assert` and meaningful expected results. | Pair activity contains at least three tests with accurate expectations. |
| Run `python -m pytest -q` and identify the actual and expected values in a failure. | Students explain the deliberately failing test during the guided demo. |
| Choose ordinary and boundary inputs and explain why they matter. | Pair discussion and individual exit ticket. |
| Correct a simple defect and rerun the complete test suite. | Guided repair and demonstration of a regression. |

Explain that tests supply evidence for the inputs checked; passing tests do not prove that a function is correct for every input.

## Preparation before class

- Provide a starter folder containing `prime.py` and `test_prime.py`, with the activity tests left incomplete.
- Have students install pytest in their course virtual environment before class and check `python -m pytest --version`.
- Run the entire demo on the teaching computer beforehand, including the expected failure and repair.
- Keep an instructor solution and a copy of the expected terminal output available.
- If a student's setup fails, pair them with a classmate whose environment works. They can still predict results, choose cases, and write tests on paper.
- Use large terminal text and keep code and test output visible together.
- Keep pytest installation outside the main lesson; a brief launch check is sufficient.
- No GitHub account, Docker installation, or additional service is needed.

## Lesson sequence: 50 minutes

| Time | Instructor actions | Student actions | Check for understanding |
| --- | --- | --- | --- |
| 0–5 min | State the behavior of `is_prime()`. Show that the supplied implementation works for 7 and 8. Ask which other input could reveal a bug. | Think individually, compare with a partner, and suggest inputs and expected outputs. | Ask why 1 should return False. Invite more than one explanation. |
| 5–8 min | Share the learning objectives and explain why repeatable checks help when code changes. | Connect testing to debugging a previous assignment. | Ask what a print statement leaves the programmer to check manually. |
| 8–15 min | Introduce a test file, a `test_` function, `assert`, and `python -m pytest -q`. Run two tests for ordinary inputs. | Predict outcomes before each run and identify input, expected result, and actual result. | Ask what happens when the assertion is false. |
| 15–23 min | Add the test for 1. Run it, pause on the failure, and guide the class to the missing `n < 2` guard. Repair the function and rerun all tests. | Read the failure and propose a repair consistent with the function's stated behavior. | Ask whether the implementation or test expectation needs changing, and why. |
| 23–36 min | Give pairs a short test-writing task. Circulate and ask each pair to justify one selected input. | Write and run at least three tests, including 0, 2, and 9. Record expected outcomes and a reason for each case. | Check accurate expectations, distinct cases, and whether both partners can explain a test. |
| 36–43 min | Invite two pairs to share. Temporarily remove the guard and rerun the suite to demonstrate a regression; restore it afterward. | Explain which tests detect the reintroduced defect and which still pass. | Ask why all tests should run after a change. |
| 43–45 min | Revisit the objectives. Address the difference between a failed test and a mistaken expectation, and the limits of passing tests. | Summarize one thing a test result can tell them and one thing it cannot. | Ask whether ten tests of the same kind are necessarily better than three carefully selected cases. |
| 45–50 min | Collect a brief individual exit ticket. | Write one new test and explain its purpose. | Use responses to decide whether the next lesson needs more test-design practice. |

## The central example

State the contract before asking students to judge the code:

> For any integer n, return True exactly when n is prime. Integers less than 2 are not prime.

Do not introduce input-type validation in this lesson.

### Initial implementation: deliberately buggy

```python
# prime.py
def is_prime(n):
    for divisor in range(2, n):
        if n % divisor == 0:
            return False
    return True
```

This intentionally simple algorithm keeps attention on testing. It is not a performance example.

### Guided tests

Begin with the first two tests, then add the third after students predict its outcome.

```python
# test_prime.py
from prime import is_prime


def test_seven_is_prime():
    assert is_prime(7) is True


def test_eight_is_not_prime():
    assert is_prime(8) is False


def test_one_is_not_prime():
    assert is_prime(1) is False
```

Run with:

```bash
python -m pytest -q
```

Expected progression:

1. With the first two tests: **2 passed**.
2. After adding the test for 1: **1 failed, 2 passed**.
3. After the repair below: **3 passed**.

### Repair

```python
def is_prime(n):
    if n < 2:
        return False

    for divisor in range(2, n):
        if n % divisor == 0:
            return False
    return True
```

Prompts during the demo:

- What input did this test use?
- What did we expect, and what did the function actually return?
- Does the expectation match the contract?
- Why does the loop not run for 1?
- Which change handles all integers below 2?
- Why should we rerun the earlier tests after fixing this case?

## Pair activity

**Student task:** Add at least three tests to check 0, 2, and 9. Before running them, write the expected result and explain why each input is useful.

Use one driver to type and one navigator to check expectations; switch roles after the first test.

| Input | Expected result — instructor reference | Reason |
| --- | --- | --- |
| 0 | False | Checks the region below the smallest prime. |
| 2 | True | Checks the smallest prime and the boundary of the valid prime region. |
| 9 | False | Checks an odd composite; testing only even composites would miss some faulty rules. |
| 17 — optional | True | Adds another ordinary prime. |
| -3 — optional | False | Checks the stated behavior for negative integers. |

**Activity success criteria:**

- At least three runnable `test_` functions with accurate expectations.
- A passing run against the repaired implementation.
- A short explanation connecting each input to the function's behavior.
- Both partners can explain at least one test.

If a pair finishes early, ask them to describe a faulty implementation that one of their tests would catch. Keep parametrization as optional follow-up material.

## Individual exit ticket

Give students these prompts:

1. Write a pytest test for `is_prime(25)`.
2. Explain what kind of faulty behavior this test could detect that a test using only 8 might miss.
3. If every test passes, does that prove the function is correct for every integer? Explain briefly.

**Instructor reference:**

```python
def test_twenty_five_is_not_prime():
    assert is_prime(25) is False
```

An acceptable explanation is that 25 is an odd composite and would expose a function that incorrectly labels every odd number greater than 1 as prime. Passing tests establish only that the tested expectations hold for those cases.

Use the exit ticket as a quick formative check; do not spend the final minutes grading it aloud.

## Suggested 10-slide outline

| Slide | Focus |
| --- | --- |
| 1 | Hook: Does this function work? |
| 2 | Learning objectives and why automated tests help |
| 3 | Inputs, expected results, and the function contract |
| 4 | Anatomy of a pytest test: file, function, assertion |
| 5 | Running tests and reading the result |
| 6 | Guided demo: expose a bug, repair it, rerun |
| 7 | Choosing useful cases: ordinary inputs and boundaries |
| 8 | Pair activity instructions and success criteria |
| 9 | Debrief: regressions and the limits of passing tests |
| 10 | Individual exit ticket and reference links |

Use slides as prompts and instructions. Spend most of the middle of the lesson in the editor, terminal, and student activity.

## Scope and pacing

Teach only basic assertions, test discovery, running tests, reading failures, and choosing inputs. Save fixtures, mocking, coverage, and GitHub Actions for later lessons.

If the class falls behind, shorten pair presentations and omit optional cases. Preserve the individual exit ticket.

A natural next lesson is running the same test suite automatically with GitHub Actions.

## Official reference

- [pytest: Get Started](https://docs.pytest.org/en/stable/getting-started.html) — test naming, assertions, running tests, and interpreting failures.

The teaching sequence, activity, and timing above are a proposed lesson design, not an observation rubric.

