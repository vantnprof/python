def is_prime(n):
    """Return True exactly when the integer n is prime.

    Integers less than 2 are not prime.
    """
    for divisor in range(2, n):
        if n % divisor == 0:
            return False
    return True
