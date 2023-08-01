import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
edge = [[] for _ in range(n+1)]
degree = [0] * (n + 1)
visited = [False] * (n + 1)
res = deque()
for _ in range(m):
    tmp = list(map(int, input().split()))
    for i in range(1, tmp[0]):
        edge[tmp[i]].append(tmp[i+1])
        degree[tmp[i+1]] += 1

q = deque()
for i in range(1, n+1):
    if degree[i] == 0:
        q.append(i)
        visited[i] = True

while q:
    tmp = q.popleft()
    visited[tmp] = True
    res.append(tmp)
    for k in range(len(edge[tmp])):
        degree[edge[tmp][k]] -= 1
        if degree[edge[tmp][k]] == 0 and not visited[edge[tmp][k]]:
            q.append(edge[tmp][k])

if len(res) < n:
    print(0)
else:
    while res:
        print(res.popleft())
