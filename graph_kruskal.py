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


inputlines = """
0 1 2
0 2 5
1 2 4
1 3 6
1 4 10
2 3 2
3 5 1
4 5 3
4 6 5
5 6 9
""".strip().splitlines()

# 頂点, 辺, 開始
N, M, K = 7, len(inputlines), 0
costs = [list(map(int, inputlines[i].split())) for i in range(M)]
costs.sort(key=lambda x: x[2])
uf = UnionFind(N)
ans = 0
for i in range(M):
    a, b, c = costs[i]
    if not uf.is_same(a, b):
        uf.unite(a, b)
        ans += c
print(ans)
