import sys
import copy
from collections import deque
input = sys.stdin.readline
n = int(input())
B = []
dx, dy = [0,-1,0,1], [-1,0,1,0]
res = 0
for i in range(n):
    B.append(list(map(int, input().split())))
for i in B:
    res = max(res,max(i))

def move(i, board, x, y):
    global added
    global res
    if board[x][y] != 0:
        nx, ny = x + dx[i], y + dy[i]
        moved = False
        while board[nx][ny]==0:
            if 0<=nx+dx[i]<n and 0<=ny+dy[i]<n:
                nx += dx[i]
                ny += dy[i]
                moved = True
            else:
                break
        if board[nx][ny] == 0:
            board[nx][ny] = board[x][y]
            board[x][y] = 0
            added = False
        elif board[nx][ny]==board[x][y] and added==False:
            board[nx][ny] *= 2
            res = max(res, board[nx][ny])
            board[nx-dx[i]][ny-dy[i]] = 0
            board[x][y] = 0
            added = True
        else:
            if moved:
                board[nx-dx[i]][ny-dy[i]] = board[x][y]
                board[x][y] = 0
                added = False
def move2(i,board):
    global added
    tmp = copy.deepcopy(board)
    if i == 0:
        for x in range(n):
            added = False
            for y in range(1, n):
                move(i, tmp, x, y)
    elif i == 1:
        for y in range(n):
            added = False
            for x in range(1, n):
                move(i, tmp, x, y)

    elif i == 2:
        for x in range(n):
            added = False
            for y in range(n - 2, -1, -1):
                move(i, tmp, x, y)

    else:
        for y in range(n):
            added = False
            for x in range(n - 2, -1, -1):
                move(i, tmp, x, y)
    # print()
    # for i in tmp:
    #     print(i)
    return tmp



def bfs():
    q = deque()
    q.append((B, 0))
    while q:
        tmp, cnt = q.pop()
        if cnt < 5:
            for i in range(4):
                k = move2(i,tmp)
                if tmp != k:
                    q.appendleft((move2(i, tmp), cnt + 1))


bfs()
print(res)


