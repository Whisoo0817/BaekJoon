import sys
from collections import deque
input = sys.stdin.readline
n,m,r = map(int, input().split())
a = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split())
    a[u].append(v)
    a[v].append(u)
for i in range(1,n+1):
    a[i] = sorted(a[i])
visited = [False]*(n+1)
visited2 = [False]*(n+1)
q = deque([])
def dfs(a,r):
    visited[r] = True
    print(r,end=' ')
    for i in a[r]:
        if visited[i]==False:
            dfs(a,i)
def bfs(a,r):
    visited2[r] = True
    q.append(r)
    while q:
        x = q.popleft()
        print(x,end=' ')
        for i in a[x]:
            if visited2[i]==False:
                visited2[i]=True
                q.append(i)

dfs(a,r)
print()
bfs(a,r)
