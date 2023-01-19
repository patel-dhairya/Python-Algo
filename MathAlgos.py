def sum_all(n: int) -> int:
    """
    Sum of all natural numbers up to n
    :param n: int must be greater than or equal to 0
    :return: sum of all integers from 0 to n
    """
    assert n >= 0, f"number greater than 0 expected, received: {n}"
    return n * (n + 1) // 2


def fib(n: int) -> int:
    """
    Fibonacci number F(n) is defied by F(n) = F(n-1)+F(n-2)
    :param n:int must be greater than or equal to 0
    :return: returns nth fibonacci number
    """
    assert n >= 0, f"number greater than 0 expected, received: {n}"
    fibs = [0, 1]
    for i in range(2, n + 1):
        fibs[i % 2] = fibs[0] + fibs[1]
    return fibs[n % 2]


def gcd(a: int, b: int) -> int:
    """
    Returns greatest common divisor of two number
    :param a: int
    :param b: int
    :return: GCD of a and b
    """
    return a if b == 0 else gcd(b, a % b)


def ackermann(m: int, n: int) -> int:
    """
    In computability theory, the Ackermann function, named after Wilhelm Ackermann, is one of the
    simplest and earliest-discovered examples of a total computable function that is not primitive
    recursive.
    :param m: int
    :param n: int
    """
    print(f"ackermann function called for ({m},{n})")
    if not (m >= 0 and n >= 0):
        raise "m and n should be greater than 0 for ackermann function to work"
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))
