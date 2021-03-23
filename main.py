import bisect
import collections
import itertools
import math
from sys import setrecursionlimit

setrecursionlimit(10 ** 5 + 1)


def bitcount(x):
    # TODO ビット数カウント 意味不明
    x = (x & 0x55555555) + (x >> 1 & 0x55555555)
    x = (x & 0x33333333) + (x >> 2 & 0x33333333)
    x = (x & 0x0F0F0F0F) + (x >> 4 & 0x0F0F0F0F)
    x = (x & 0x00FF00FF) + (x >> 8 & 0x00FF00FF)
    x = (x & 0x0000FFFF) + (x >> 16 & 0x0000FFFF)
    return x


def divisors(n):
    # 約数列挙
    r = set([1, n])
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            r.add(i)
            r.add(n // i)
        i += 1
    return r


def extgcd(a, b):
    # 拡張ユークリッドの互除法
    # ax + by = gcd(a, b)
    # bx' + (a%b)y' = gcd(a, b)
    #   a%b = a - (a/b)b より
    # ay' + b(x' - (a/b)y')
    if b:
        d, x, y = extgcd(b, a % b)
        return d, y, x - a // b * y
    return a, 1, 0


def factorize(n):
    # 素因数分解
    # TODO sqrt使わない
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


def modinv(a, mod):
    # 非再帰拡張ユークリッドの互除法による逆元
    # TODO 仕組みわかってない ...x**-1 = x**(P-2)でいけるらしい
    b, u, v = mod, 1, 0
    while b:
        t = a // b
        a -= t * b
        u -= t * v
        a, b = b, a
        u, v = v, u
    u %= mod
    if u < 0:
        u += mod
    return u


def modpow(a, n, mod):
    # 二分累乗法
    # bin(45) == '0b101101'
    # 3**45 == 3**(2**0 + 2**2 + 2**3 + 2**5)
    # .     == 3**(2**0) * 3**(2**2) * 3**(2**3) * 3**(2**5)
    r = 1
    while n:
        if n & 1:
            r = r * a % mod
        a = a * a % mod
        n >>= 1
    return r


def sieve_eratosthenes(n):
    # エラトステネスの篩
    if n < 3:
        return [0, 0, 1]
    p = [i % 2 for i in range(n + 1)]
    p[1], p[2] = 0, 1
    for i in range(3, n + 1, 2):
        if not p[i]:
            continue
        j = 3
        is_i_prime = True
        while j ** 2 <= i:
            if not i % j:
                is_i_prime = False
                break
            j += 1
        if not is_i_prime:
            k = 1
            while i * k <= n:
                p[i * k] = 0
                k += 1
    return p


def t():
    """
    >>> bitcount(0), bitcount(0b111), bitcount(0b1010)
    (0, 3, 2)

    >>> divisors(1), divisors(12), divisors(10**9 + 7)
    ({1}, {1, 2, 3, 4, 6, 12}, {1, 1000000007})

    >>> extgcd(12, 10)
    (2, 1, -1)

    >>> factorize(1), factorize(12), factorize(10**9 + 7)
    ([], [2, 2, 3], [1000000007])

    >>> modinv(2, 13), modinv(2, 13) * 2 % 13
    (7, 1)

    >>> modpow(3, 45, 10**9 + 7)
    644897553

    >>> sieve_eratosthenes(12)
    [0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0]

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

    >>> math.factorial(5)  # n!
    120

    >>> math.comb(5, 4)  # nCk
    5

    >>> math.gcd(12, 10)
    2

    >>> 12 * 10 / math.gcd(12, 10)  # lcm
    60.0

    # 小ネタ リストの両端から同じ位置
    >>> a = list(range(5))
    >>> a[0], a[~0]
    (0, 4)

    # map(int, input().split())
    # list(map(int, input().split()))
    # int(input())
    """
