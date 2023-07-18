# MST 지름 구하는 방식 X -> 그래프에 루프가 존재하면 예외 발생
# 그냥 브루트포스...
import sys
from collections import deque
input = sys.stdin.readline
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
N, M = map(int, input().split())
Map = [list(input().strip()) for _ in range(N)]
cnt = 0
def bfs(i, j):
    global cnt
    q = deque()
    q.append((i, j))
    visited = [[-1]*M for _ in range(N)]
    visited[i][j] = 0
    while q:
        y, x = q.popleft()
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if 0 <= ny < N and 0 <= nx < M and Map[ny][nx] == 'L' and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))
                cnt = max(cnt, visited[ny][nx])

for i in range(N):
    for j in range(M):
        if Map[i][j] == 'L':
            bfs(i, j)
print(cnt)







