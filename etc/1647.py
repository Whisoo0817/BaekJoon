import sys
input = sys.stdin.readline
import heapq

res = []
n, m = map(int, input().split())
edge = [[] for _ in range(n+1)]
q = []

for _ in range(m):
    a, b, c = map(int, input().split())
    edge[a].append((c, b))
    edge[b].append((c, a))
visited = [False] * (n + 1)

for i in edge[1]:
    heapq.heappush(q, i)
visited[1] = True

while q:
    tmp = heapq.heappop(q)
    if not visited[tmp[1]]:
        visited[tmp[1]] = True
        res.append(tmp[0])
        if len(res) == n-1:
            break
        for i in edge[tmp[1]]:
            if not visited[i[1]]:
                heapq.heappush(q, i)

print(sum(res) - max(res))



