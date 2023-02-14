import sys
import heapq
input = sys.stdin.readline
n, m = map(int, input().split())
inDegree = [0]*(n+1)
edge = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    edge[a].append(b)
    inDegree[b] += 1
q = []
res = []
for i in range(1,n+1):
    if inDegree[i] == 0:
        q.append(i)
while q:
    a = heapq.heappop(q)
    res.append(a)
    for i in edge[a]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            heapq.heappush(q, i)
print(*res)