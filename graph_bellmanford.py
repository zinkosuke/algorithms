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
edges = []
for i in range(M):
    a, b, c = map(int, inputlines[i].split())
    edges.append((a, b, c))
    edges.append((b, a, c))
mem = [INF] * N
mem[K] = 0
while True:
    update = False
    for i in range(len(edges)):
        a, b, c = edges[i]
        if mem[a] != INF and mem[a] + c < mem[b]:
            mem[b] = mem[a] + c
            update = True
    if not update:
        break
    # TODO 負の閉路
print(mem)
