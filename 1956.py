import sys
input = sys.stdin.readline
V, E = map(int, input().split())
edge = [[] for _ in range(V+1)]
for i in range(E):
    a, b, c = map(int, input().split())
    edge[a].append([c, b])
d = [[1e9]*(V+1) for _ in range(V+1)]
for i in range(1,V+1):
    d[i][i] = 0
for i in range(1,V+1):
    for j in edge[i]:
        w, next_node = j[0], j[1]
        d[i][next_node] = w
def Floid():
    for k in range(1,V+1):
        for i in range(1,V+1):
            for j in range(1,V+1):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
Floid()
res = []
for i in range(V+1):
    for j in range(V+1):
        if i!=j and d[i][j]!=1e9 and d[j][i]!=1e9:
            res.append(d[i][j] + d[j][i])
if len(res)==0:
    print(-1)
else:
    print(min(res))

