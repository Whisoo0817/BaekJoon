import sys
from collections import deque
input = sys.stdin.readline
dx = [-2,-1,1,2,2,1,-1,-2]
dy = [1,2,2,1,-1,-2,-2,-1]
for _ in range(int(input())):
    n = int(input())
    sx,sy = map(int,input().split())
    lx,ly = map(int,input().split())
    q = deque([])
    a = [[0]*n for _ in range(n)]
    tmp = [[0] * n for _ in range(n)]
    q.append([sx,sy])
    while q:
        u = q.popleft()
        x,y = u[0],u[1]
        if x== lx and y == ly:
            print(tmp[x][y])
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx <= n-1 and ny <= n-1 and tmp[nx][ny]==0:
                tmp[nx][ny] = tmp[x][y] + 1
                q.append([nx,ny])



