import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
B = [list(map(str, input().strip())) for _ in range(N)]
dx, dy = [-1,1,0,0], [0,0,-1,1]
q = deque()
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
def init():
    rx, ry, bx, by = 0, 0, 0, 0
    for i in range(N):
        for j in range(M):
            if B[i][j] == 'R':
                rx,ry = i,j
            elif B[i][j] == 'B':
                bx,by = i,j
    q.append((rx,ry,bx,by,1))
    visited[rx][ry][bx][by] = True
def move(x,y,dx,dy):
    cnt = 0
    while B[x+dx][y+dy] != '#' and B[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt
def BFS():
    init()
    while q:
        rx, ry, bx, by, depth = q.pop()
        if depth > 10:
            break
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
            if B[nbx][nby] != 'O': # 순서 중요(파란구슬이 0이면 빨강이 0이어도 실패)
                if B[nrx][nry] == 'O':
                    print(depth)
                    return
                if nrx == nbx and nry == nby: # 겹쳤을 때 (미친 아이디어)
                    if rcnt > bcnt: # 이동거리 많은 것을
                        nrx -= dx[i] # 한 칸 뒤로
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]

                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    q.appendleft((nrx, nry, nbx, nby, depth+1))
    print(-1)
BFS()













