import sys
input = sys.stdin.readline
r, c = map(int,input().split())
board = [list(map(str, input().strip())) for _ in range(r)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]
cnt = 1
def bfs():
    global cnt
    q = set() # set => 중복 제거
    q.add((0, 0, board[0][0]))
    while q:
        x,y,z = q.pop()
        cnt = max(cnt, len(z)) # 최댓값 갱신
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<r and 0<=ny<c and board[nx][ny] not in z:
                q.add((nx, ny, board[nx][ny] + z))

bfs()
print(cnt)