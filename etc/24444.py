import sys
from collections import deque
input = sys.stdin.readline
n,m,r = map(int,input().split())
a = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split())
    a[u].append(v)
    a[v].append(u)
for i in range(1,n+1):
    a[i] = sorted(a[i])
visited = [False]*(n+1)
ord = 1
res = [0]*(n+1)
q = deque([])
def bfs(a,r):
    global ord
    res[r] = ord
    ord += 1
    visited[r] = True
    q.append(r)
    while q:
        u = q.popleft()
        for v in a[u]:
            if visited[v] == False:
                visited[v] = True
                res[v] = ord
                ord += 1
                q.append(v)

bfs(a,r)
for i in range(1,n+1):
    print(res[i])