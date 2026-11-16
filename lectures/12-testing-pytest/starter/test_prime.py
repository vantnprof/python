from prime import is_prime


def test_seven_is_prime():
    assert is_prime(7) is True


def test_eight_is_not_prime():
    assert is_prime(8) is False


# ---------------------------------------------------------------------
# Pair activity: add at least three tests, for the inputs 0, 2 and 9.
# Before you run them, write the expected result and why each input
# is useful as a comment above the test.
# ---------------------------------------------------------------------
