import sys
input = sys.stdin.readline
n, m = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(n)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
visited = [[False] * m for _ in range(n)]
res = 0

def dfs(y, x, cnt, ssum): # DFS 4칸까지
    global res
    visited[y][x] = True
    cnt += 1
    ssum += blocks[y][x]
    if cnt == 4:
        res = max(res, ssum)
        visited[y][x] = False # ***
        return
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]:
            dfs(ny, nx, cnt, ssum)
    visited[y][x] = False

def check(y, x): # ㅗ,ㅏ,ㅓ,ㅜ 체크
    global res
    cnt, ssum = 1, 0
    ssum += blocks[y][x]
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= nx < m and 0 <= ny < n:
            cnt += 1
            ssum += blocks[ny][nx]
    if cnt < 4:
        return
    elif cnt == 4:
        res = max(res, ssum)
    elif cnt == 5:
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            res = max(res, ssum - blocks[ny][nx])

for i in range(n):
    for j in range(m):
        dfs(i, j, 0, 0)
        check(i, j)

print(res)