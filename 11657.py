import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
d = [[1e9]*(N+1) for _ in range(N+1)]
for i in range(N+1):
    d[i][0],d[i][1] = 0, 0

for i in range(1,N+1):
    for j in range(1,N+1):
        if d[i-1][j] != 1e9:
            for k in graph[j]:
                w, next_node = k[0], k[1]
                d[i][next_node] = min(d[i][next_node], d[i-1][j] + w)
def res():
    for i in range(1,N+1):
        if d[N-1][i] != d[N][i]:
            print(-1)
            return
    for i in range(2,N+1):
        print(d[N-1][i] if d[N-1][i]!=1e9 else -1)
res()





