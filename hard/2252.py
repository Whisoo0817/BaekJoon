import sys
input = sys.stdin.readline
from collections import deque

def dfs(s):
    visited[s] = True
    for i in edge[s]:
        if not visited[i]:
            dfs(i)
    ans.appendleft(s)
ans = deque()
n, m = map(int, input().split())
visited = [False]*(n+1)
edge = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    edge[a].append(b)

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
print(*ans)




