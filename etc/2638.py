import sys
sys.setrecursionlimit(10**6) # 필요
input = sys.stdin.readline
N, M = map(int ,input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
air = [[0]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]
visited2 = [[False]*M for _ in range(N)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
total = 0
for i in range(N):
    for j in range(M):
        if Map[i][j] == 1:
            total += 1 # 처음 치즈 총 개수

def dfs(y, x): # 인접한 외부 공기들 DFS
    air[y][x] = 1 # == 공기 노출 True
    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]
        if 0 <= ny < N and 0 <= nx < M and Map[ny][nx] == 0 \
                and not visited2[ny][nx]:
            visited2[ny][nx] = True
            dfs(ny, nx)


def check(y, x): # 외부 공기 노출 체크 DFS
    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]
        if 0 > ny or N <= ny or 0 > nx or M <= nx: # 노출
            dfs(y, x) # 인접 공기들 전부 DFS
            return
        if 0 <= ny < N and 0 <= nx < M and\
                Map[ny][nx] == 0 and not visited[ny][nx] and air[ny][nx] == 0:
            visited[ny][nx] = True
            air[ny][nx] = -1 # dfs 안한 공기는 내부 공기(노출X)
            check(ny, nx)

def hour():
    global total
    # 공기 외부 내부 구분
    for i in range(N):
        for j in range(M):
            if Map[i][j] == 0 and air[i][j] == 0:
                check(i, j)
    for i in range(N):
        for j in range(M):
            if air[i][j] == 0: # if 치즈
                cnt = 0
                for k in range(4):
                    ni, nj = i + dy[k], j + dx[k]
                    if air[ni][nj] == 1:
                        cnt += 1
                if cnt >= 2: # 두 변 이상 노출 시 사라짐
                    Map[i][j] = 0
                    total -= 1
res = 0
while total > 0:
    hour()
    air = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    visited2 = [[False] * M for _ in range(N)]
    res += 1
print(res)
