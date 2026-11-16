from prime import is_prime


def test_seven_is_prime():
    assert is_prime(7) is True


def test_eight_is_not_prime():
    assert is_prime(8) is False

def test_one_is_not_prime():
    assert is_prime(1) is False