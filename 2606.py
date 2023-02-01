import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
m = int(input())
a = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split())
    a[u].append(v)
    a[v].append(u)
visited = [False]*(n+1)
q = deque([])
res = 0
def bfs(a,r):
    global res
    visited[r] = True
    q.append(r)
    while q:
        u = q.popleft()
        for v in a[u]:
            if visited[v]==False:
                visited[v] = True
                q.append(v)
                res+=1
bfs(a,1)
print(res)