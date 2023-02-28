import sys
from collections import deque
import copy
input = sys.stdin.readline
N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [1,0,-1,0], [0,1,0,-1]
answer = 0
def infect(a,x,y):
    a[x][y] = 2
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if a[nx][ny] == 0:
                infect(a, nx, ny)
def test(map1):
    tmp = copy.deepcopy(map1)
    q = deque([])
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 2:
                q.append((i,j))
    while q:
        x, y = q.popleft()
        infect(tmp,x,y)
    res = 0
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 0:
                res += 1
    return res

def sol(wall):
    global answer
    if wall == 3:
        answer = max(answer, test(maps))
        return
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                maps[i][j] = 1
                sol(wall+1)
                maps[i][j] = 0
sol(0)
print(answer)










