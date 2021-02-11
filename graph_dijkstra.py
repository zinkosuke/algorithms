from heapq import heappop
from heapq import heappush

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
costs = [[INF] * N for i in range(N)]
for i in range(M):
    a, b, c = map(int, inputlines[i].split())
    costs[a][b] = c
    costs[b][a] = c
mem = [INF] * N
mem[K] = 0
que = [(0, K)]
while que:
    cost, i = heappop(que)
    if mem[i] < cost:
        continue
    for j in range(N):
        if costs[i][j] == INF:
            continue
        if mem[i] + costs[i][j] < mem[j]:
            mem[j] = mem[i] + costs[i][j]
            heappush(que, (mem[j], j))
print(mem)
