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
INF = float("inf")
mem = [[INF] * N for i in range(N)]
for i in range(N):
    mem[i][i] = 0
for i in range(M):
    a, b, c = map(int, inputlines[i].split())
    mem[a][b] = c
    mem[b][a] = c
for k in range(N):
    for i in range(N):
        for j in range(N):
            mem[i][j] = min(mem[i][j], mem[i][k] + mem[k][j])
print(mem[K])
