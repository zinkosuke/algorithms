class UnionFind:
    def __init__(self, n):
        self.r = [-1] * n

    def root(self, x):
        if self.r[x] < 0:
            return x
        self.r[x] = self.root(self.r[x])
        return self.r[x]

    def unite(self, x, y):
        x, y = self.root(x), self.root(y)
        if x == y:
            return False
        if self.r[y] < self.r[x]:
            x, y = y, x
        self.r[x] += self.r[y]
        self.r[y] = x
        return True

    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    def size(self, x):
        return -self.r[self.root(x)]


def t():
    """
    >>> uf = UnionFind(7)
    >>> uf.r
    [-1, -1, -1, -1, -1, -1, -1]

    >>> uf.unite(1, 3)
    True
    >>> uf.unite(2, 3)
    True
    >>> uf.unite(5, 6)
    True
    >>> uf.unite(5, 6)
    False
    >>> uf.r
    [-1, -3, 1, 1, -1, -2, 5]

    >>> uf.is_same(1, 3)
    True
    >>> uf.is_same(2, 3)
    True
    >>> uf.is_same(2, 5)
    False

    >>> uf.size(1)
    3
    >>> uf.size(3)
    3
    >>> uf.size(0)
    1
    """
    pass
