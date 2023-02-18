import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
a = [list(input().rstrip()) for _ in range(n)]
dx = [1,0,-1,0]
dy = [0,-1,0,1]
res = []
def dfs(a,x,y,k):
    res[k]+=1
    a[x][y] = '2'

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= n or ny >= n or nx < 0 or ny < 0 or a[nx][ny]!='1':
            continue
        else:
            dfs(a,nx,ny,k)
k = 0
for i in range(n):
    for j in range(n):
        if a[i][j]=='1':
            res.append(0)
            dfs(a,i,j,k)
            k+=1
res.sort()
print(len(res))
for i in res:
    print(i)