import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(N-1):
    x, y, d = map(int, input().split())
    graph[x].append([y, d])
    graph[y].append([x, d])
def sol(s,e,dist):
    if s==e:
        print(dist)
        return
    visited[s] = True
    for i in graph[s]:
        if not visited[i[0]]:
            sol(i[0],e,dist+i[1])


for i in range(M):
    s, e = map(int, input().split())
    visited = [False] * (N+1)
    sol(s,e,0)
