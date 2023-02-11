import sys
input = sys.stdin.readline
r, c = map(int,input().split())
board = []
for i in range(r):
    board.append(list(input().strip()))
visited = [False] * 26
dx = [0,1,0,-1]
dy = [1,0,-1,0]
result = 0
def sol(x,y,res):
    global result
    visited[ord(str(board[x][y]))-65] = True
    result = max(result, res)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < r and ny < c and not visited[ord(str(board[nx][ny]))-65]:
            sol(nx,ny,res+1)
            visited[ord(str(board[nx][ny]))-65] = False
sol(0,0,1)
print(result)

