def is_prime(n):
    # NOTE: O(n).
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def is_prime(n):
    # NOTE: O(sqrt(n)).
    if n == 1:
        return False

    for i in range(2, n):
        # NOTE: If a number n does not have a divisor less than sqrt(n),
        # Then it does not have a divisor greater than sqrt(n).
        if (
            i * i > n
        ):  # NOTE: Since both sides of the inequality are positive, this is equivalent to [i > sqrt(n)].
            # NOTE: Calculation of sqrt is expensive and error prone, so we simply avoid it.
            break
        if n % i == 0:
            return False

    return True


def get_smaller_primes(n):
    """Obtain all primes in the interval [2, n]."""
    # NOTE: Use Era Sieve for a more optimal prime generation.
    #
    return [candidate for candidate in range(2, n + 1) if is_prime(candidate)]


def era_sieve(n):
    """Obtain all primes in the interval [2, n]."""
    # NOTE: This is Era sieve.

    assert n >= 2
    contenders = [n for n in range(n + 1)]
    contenders[0], contenders[1] = False, False

    num = 2

    while num <= n:
        if contenders[num]:
            for index in range(2 * num, n + 1, num):
                contenders[index] = False

        num += 1

    return contenders


def era_sieve_optimized(n):
    """Obtain all primes in the interval [2, n]."""
    # NOTE: This is Era sieve optimized.

    assert n >= 2
    contenders = [n for n in range(n + 1)]
    contenders[0], contenders[1] = False, False

    num = 2

    while num <= n:
        if contenders[num]:
            for index in range(num * num, n + 1, num):
                contenders[index] = False

        num += 1

    return contenders


# NOTE: Magic.
def get_least_primes_linear(n):
    lp = [0] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
        for p in primes:
            x = p * i
            if (p > lp[i]) or (x > n):
                break
            lp[x] = p
    return primes, lp


if __name__ == "__main__":
    print(era_sieve(20))
    print(era_sieve(19))
    print(era_sieve(21))

    print(era_sieve_optimized(20))
    print(era_sieve_optimized(19))
    print(era_sieve_optimized(21))
