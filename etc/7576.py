import sys
input = sys.stdin.readline
from collections import deque
m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dx = [0,-1,0,1]
dy = [1,0,-1,0]
today = deque([])
tmp = [[0]*m for _ in range(n)] # 해당 토마토가 익을 때까지 걸린 날짜

def sol():
    total = 0 # 안익은 토마토 개수
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                today.append([i, j])
            elif a[i][j] == 0:
                total += 1
    if total == 0:
        return 0
    while today:
        u = today.popleft()
        x, y = u[0], u[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<=n-1 and 0<=ny<=m-1 and a[nx][ny] == 0:
                a[nx][ny] = 1
                today.append([nx,ny])
                tmp[nx][ny] = tmp[x][y] + 1 # 익은 토마토가 옆에 있으면 다음날 익어짐
                total -= 1
                if total ==0: # 다 익었으면
                    return tmp[nx][ny]
    if total!=0: # 다 익히는게 불가능한 경우
        return -1
print(sol())

