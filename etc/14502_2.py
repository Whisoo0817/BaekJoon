import sys
from collections import deque
import copy
from itertools import combinations
input = sys.stdin.readline
N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [1,0,-1,0], [0,1,0,-1]
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
def sol(maps):
    res = 0
    zero_list = []
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                zero_list.append((i,j))
    zero_comb = list(combinations(zero_list, 3))
    for i in zero_comb:
        for k in range(3):
            maps[i[k][0]][i[k][1]] = 1
        res = max(res, test(maps))
        for k in range(3):
            maps[i[k][0]][i[k][1]] = 0
    return res
print(sol(maps))


