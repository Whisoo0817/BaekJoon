import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
a = [list(input().rstrip()) for _ in range(n)]
q = deque([])
dx = [1,0,-1,0]
dy = [0,-1,0,1]
def bfs(x,y):
    a[x][y] = '2'
    q.append([x,y,1])
    while q:
        u = q.popleft()
        x1,y1,cnt = u[0],u[1],u[2]
        if x1 == n-1 and y1 == m-1:
            return cnt
        for i in range(4):
            nx = x1 + dx[i]
            ny = y1 + dy[i]
            if nx >= n or ny >= m or nx < 0 or ny < 0 or a[nx][ny] != '1':
                continue
            else:
                a[nx][ny] = '2'
                q.append([nx,ny,cnt+1])
print(bfs(0,0))