class SegTree:
    INF = float("inf")

    def __init__(self, n):
        x = 1
        while x < n:
            x *= 2
        self.n = x
        self.r = [self.INF] * (2 * x - 1)

    def update(self, k, v):
        k += self.n - 1
        self.r[k] = v
        while 0 < k:
            k = (k - 1) // 2
            self.r[k] = min(self.r[2 * k + 1], self.r[2 * k + 2])

    def query(self, a, b):
        return self.__query(a, b, 0, 0, self.n)

    def __query(self, a, b, k, l, r):
        if r <= a or b <= l:
            return self.INF
        if a <= l and r <= b:
            return self.r[k]
        m = (l + r) // 2
        vl = self.__query(a, b, 2 * k + 1, l, m)
        vr = self.__query(a, b, 2 * k + 2, m, r)
        return min(vl, vr)


def t():
    """
    木として簡単に扱うため, n=n+k==2**xになるようにkかさ増ししている.
    リストの先頭は区間の管理用にn-1個使う, 全体で2n-1個.
    INFとminの部分は用途に応じて変更.

    >>> tr = (10, 2, 9, 4, 5, 8, 3)
    >>> st = SegTree(len(tr))
    >>> for i, t in enumerate(tr):
    ...     st.update(i, t)
    >>> st.r
    [2, 2, 3, 2, 4, 5, 3, 10, 2, 9, 4, 5, 8, 3, inf]
    >>> st.query(-1, 10**9), st.query(2, 5)
    (2, 4)
    >>> st.update(4, 1)
    >>> st.r
    [1, 2, 1, 2, 4, 1, 3, 10, 2, 9, 4, 1, 8, 3, inf]
    """
