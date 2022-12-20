def sum_all(n: int) -> int:
    """
    Sum of all natural numbers up to n
    :param n: int must be greater than or equal to 0
    :return: sum of all integers from 0 to n
    """
    assert n >= 0,  f"number greater than 0 expected, received: {n}"
    return n * (n + 1) // 2


def fib(n: int) -> int:
    """
    Fibonacci number F(n) is defied by F(n) = F(n-1)+F(n-2)
    :param n:int must be greater than or equal to 0
    :return: returns nth fibonacci number
    """
    assert n >= 0, f"number greater than 0 expected, received: {n}"
    fibs = [0, 1]
    for i in range(2, n+1):
        fibs[i % 2] = fibs[0] + fibs[1]
    return fibs[n % 2]
