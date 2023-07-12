import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
res = 0
level = 2
exp = 0 # 경험치
def find_shark(): # 아기상어(9)가 어디있는지
    for i in range(n):
        for j in range(n):
            if space[i][j] == 9:
                space[i][j] = 0
                return i, j
def bfs():
    global level, exp, res
    candidate = []
    y, x = find_shark()
    q = deque([(0, y, x)])
    visited = [[False]*n for _ in range(n)]
    while q:
        dis, y, x = q.popleft()
        visited[y][x] = True
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and space[ny][nx] <= level:
                visited[ny][nx] = True
                if 0 < space[ny][nx] < level: # 잡아먹은 경우 후보에 추가
                    candidate.append([dis + 1, ny, nx]) # 이것보다 멀리있는 먹이는 어차피 필요없음 -> 큐에 추가 X
                else: # 0이나 같은 숫자라서 잡아먹지 못하는 경우
                    q.append((dis + 1, ny, nx))

    if len(candidate) == 0: # 먹이가 없으면
        return False
    dis, ny, nx = sorted(candidate)[0] # 거리가 가장 가깝고, 가장 위쪽 왼쪽에 있는 먹이
    space[ny][nx] = 9 # 아기 상어 위치 갱신

    exp += 1
    if level == exp:
        level += 1
        exp = 0

    res += dis

    return True

while True:
    if not bfs():
        print(res)
        break

