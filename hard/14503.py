import sys
input = sys.stdin.readline
N, M = map(int, input().split())
r, c, d = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
res = 0
def solution(r,c,d):
    global res
    if maps[r][c] == 0:
        res += 1
        maps[r][c] = -1
    stack = 0
    for i in range(4):
        nr = r + dx[i]
        nc = c + dy[i]
        if maps[nr][nc] == 0:
            stack += 1
    if stack > 0:
        if d==0: d = 3
        else: d -= 1
        nr = r + dx[d]
        nc = c + dy[d]
        if maps[nr][nc]==0:
            solution(nr,nc,d)
        else:
            solution(r,c,d)

    else:
        back_d = d
        if d>1: back_d -= 2
        else: back_d += 2
        nr = r + dx[back_d]
        nc = c + dy[back_d]
        if maps[nr][nc] == 1:
            return
        else:
            solution(nr,nc,d)

solution(r,c,d)

print(res)