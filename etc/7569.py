import sys
input = sys.stdin.readline
from collections import deque
m, n, h = map(int, input().split())
a = [[list(map(int, input().split())) for _ in range(n)] for o in range(h)]
dx = [0,-1,0,1,0,0]
dy = [1,0,-1,0,0,0]
dz = [0,0,0,0,1,-1]
today = deque([])
tmp = [[[0]*m for _ in range(n)] for oo in range(h)] # 해당 토마토가 익을 때까지 걸린 날짜

def sol():
    total = 0 # 안익은 토마토 개수
    for o in range(h):
        for i in range(n):
            for j in range(m):
                if a[o][i][j] == 1:
                    today.append([o, i, j])
                elif a[o][i][j] == 0:
                    total += 1
    if total == 0:
        return 0
    while today:
        u = today.popleft()
        z, x, y = u[0], u[1], u[2]
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<=n-1 and 0<=ny<=m-1 and 0<=nz<=h-1 and a[nz][nx][ny] == 0:
                a[nz][nx][ny] = 1
                today.append([nz,nx,ny])
                tmp[nz][nx][ny] = tmp[z][x][y] + 1 # 익은 토마토가 옆에 있으면 다음날 익어짐
                total -= 1
                if total ==0: # 다 익었으면
                    return tmp[nz][nx][ny]
    if total!=0: # 다 익히는게 불가능한 경우
        return -1
print(sol())

