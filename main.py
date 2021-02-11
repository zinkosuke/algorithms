import bisect
import collections
import itertools
import math
from sys import setrecursionlimit

setrecursionlimit(10 ** 5 + 1)


def divisors(n):
    r = set([1, n])
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            r.add(i)
            r.add(n // i)
        i += 1
    return r


def factorize(n):
    r = []
    j = 2
    while 1 < n:
        for i in range(j, int(math.sqrt(n) + 1)):
            if n % i == 0:
                n //= i
                r.append(i)
                j = i
                break
        else:
            r.append(n)
            break
    return r


def bitcount(x):
    x = (x & 0x55555555) + (x >> 1 & 0x55555555)
    x = (x & 0x33333333) + (x >> 2 & 0x33333333)
    x = (x & 0x0F0F0F0F) + (x >> 4 & 0x0F0F0F0F)
    x = (x & 0x00FF00FF) + (x >> 8 & 0x00FF00FF)
    x = (x & 0x0000FFFF) + (x >> 16 & 0x0000FFFF)
    return x


def t():
    """
    >>> bitcount(0), bitcount(0b111), bitcount(0b1010)
    (0, 3, 2)

    >>> factorize(1), factorize(12), factorize(10**9 + 7)
    ([], [2, 2, 3], [1000000007])

    >>> divisors(1), divisors(12), divisors(10**9 + 7)
    ({1}, {1, 2, 3, 4, 6, 12}, {1, 1000000007})


    >>> bisect.bisect_left(range(10), 4), bisect.bisect_right(range(10), 4)
    (4, 5)

    >>> collections.Counter([1, 1, 2, 2, 3, 4, 6])
    Counter({1: 2, 2: 2, 3: 1, 4: 1, 6: 1})

    >>> dq = collections.deque()
    >>> dq.appendleft(1)
    >>> dq.pop(), dq
    (1, deque([]))

    >>> list(itertools.combinations(range(3), 2))
    [(0, 1), (0, 2), (1, 2)]

    >>> list(itertools.permutations(range(3), 2))
    [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]

    >>> list(itertools.product(range(3), range(3)))
    [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

    >>> math.comb(5, 4)  # nCk
    5

    >>> math.factorial(5)  # n!
    120

    >>> math.gcd(12, 10)
    2

    # 小ネタ リストの両端から同じ位置
    >>> a = list(range(5))
    >>> a[0], a[~0]
    (0, 4)
    """
