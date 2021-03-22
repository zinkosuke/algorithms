class SegTreeLazy:
    def __init__(self, v):
        n = len(v)
        x = 1
        while x < n:
            x *= 2
        self.n = x
        self.lazy = [0] * (2 * x - 1)
        self.node = [0] * (2 * x - 1)
        for i in range(n):
            self.node[i + x - 1] = v[i]
        for i in range(x - 2, -1, -1):
            self.node[i] = self.node[2 * i + 1] + self.node[2 * i + 2]

    def eval(self, k, l, r):
        if not (0 <= k < 2 * self.n - 1 and self.lazy[k]):
            return
        self.node[k] += self.lazy[k]
        if 1 < r - l:
            self.lazy[2 * k + 1] += self.lazy[k] // 2
            self.lazy[2 * k + 2] += self.lazy[k] // 2
        self.lazy[k] = 0

    def add(self, a, b, x):
        self.__add(a, b, x, 0, 0, self.n)

    def __add(self, a, b, x, k, l, r):
        self.eval(k, l, r)
        if r <= a or b <= l:
            return
        if a <= l and r <= b:
            self.lazy[k] += (r - l) * x
            self.eval(k, l, r)
        else:
            m = (l + r) // 2
            self.__add(a, b, x, 2 * k + 1, l, m)
            self.__add(a, b, x, 2 * k + 2, m, r)
            self.node[k] = self.node[2 * k + 1] + self.node[2 * k + 2]

    def get_sum(self, a, b):
        return self.__get_sum(a, b, 0, 0, self.n)

    def __get_sum(self, a, b, k, l, r):
        if r <= a or b <= l:
            return 0
        self.eval(k, l, r)
        if a <= l and r <= b:
            return self.node[k]
        m = (l + r) // 2
        vl = self.__get_sum(a, b, 2 * k + 1, l, m)
        vr = self.__get_sum(a, b, 2 * k + 2, m, r)
        return vl + vr


def t():
    """
    遅延評価

    >>> st = SegTreeLazy((10, 2, 9, 4, 5, 8, 3))
    >>> st.node
    [41, 25, 16, 12, 13, 13, 3, 10, 2, 9, 4, 5, 8, 3, 0]
    >>> st.add(2, 5, 3)
    >>> st.node
    [50, 31, 19, 12, 19, 16, 3, 10, 2, 9, 4, 8, 8, 3, 0]
    >>> st.lazy
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0]
    >>> st.get_sum(0, 3), st.get_sum(3, 5)
    (24, 15)
    >>> st.node
    [50, 31, 19, 12, 19, 16, 3, 10, 2, 12, 7, 8, 8, 3, 0]
    >>> st.lazy
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    """
