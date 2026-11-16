def is_prime(n):
    for divisor in range(2, n):
        if n % divisor == 0:
            return False
    return True