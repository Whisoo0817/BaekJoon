import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n,m,r = map(int,input().split())
a =[[]] + [[] for i in range(1,n+1)]
for _ in range(m):
    u,v = map(int,input().split())
    a[u].append(v)
    a[v].append(u)
for i in range(1,n+1):
    if a[i]:
        a[i] = sorted(a[i])
visited = [False] * (n+1)
ord = 1
res = [0]*(n+1)
def dfs(a,r):
    global ord
    res[r] = ord
    ord+=1
    visited[r] = True
    for i in a[r]:
        if visited[i] == False:
            dfs(a,i)
    return
dfs(a,r)
for i in range(1,n+1):
    print(res[i])