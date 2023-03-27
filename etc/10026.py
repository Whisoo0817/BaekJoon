import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
a = [input().strip() for _ in range(N)]
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
visited = [[False]*N for _ in range(N)]
visited2 = [[False]*N for _ in range(N)]
def dfs(x,y):
    visited[x][y] = True
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny] and a[x][y] == a[nx][ny]:
                dfs(nx,ny)
def dfs2(x,y):
    visited2[x][y] = True
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            if a[x][y] == 'B':
                if not visited2[nx][ny] and a[nx][ny] == 'B':
                    dfs2(nx,ny)
            else:
                if not visited2[nx][ny] and a[nx][ny] != 'B':
                    dfs2(nx,ny)
res, res2 = 0, 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(i,j)
            res += 1
        if not visited2[i][j]:
            dfs2(i,j)
            res2 += 1
print(res,res2)


