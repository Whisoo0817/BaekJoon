# 최소신장트리이지만 DFS로 가능
import sys
input = sys.stdin.readline
res = 0
def DFS(start):
    global res
    visited[start] = True
    for country in cost[start]:
        if not visited[country]:
            DFS(country)
            res += 1
for _ in range(int(input())):
    n, m = map(int, input().split())
    cost = [[] for _ in range(n+1)]
    for i in range(m):
        a, b = map(int, input().split())
        cost[a].append(b)
        cost[b].append(a)
    visited = [False] * (n+1)
    DFS(1)
    print(res)
    res = 0

