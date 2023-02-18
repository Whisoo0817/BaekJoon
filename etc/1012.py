import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
dx = [1,0,-1,0]
dy = [0,-1,0,1]
def dfs(x,y):
    a[x][y] = 2
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= n or ny >= m or nx < 0 or ny < 0 or a[nx][ny] != 1:
            continue
        else:
            dfs(nx,ny)
for _ in range(int(input())):
    m,n,k = map(int,input().split())
    a = [[0]*m for j in range(n)]
    for i in range(k):
        x,y = map(int,input().split())
        a[y][x] = 1
    res = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                dfs(i,j)
                res += 1
    print(res)
