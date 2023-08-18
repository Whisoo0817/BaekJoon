# 보완할 점: combination 쓰지말고 백트래킹으로 조합을 구하면 중간에 'Y' 4번이상 나오면 가지치기 가능
# 이후 학생들이 연결되어 있는 지 체크하는 방식은 같음
import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque
arr = [list(input().strip()) for _ in range(5)]
dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
students = [(i, j) for i in range(5) for j in range(5)]
combs = list(combinations(students, 7))
def check(l):
    visited = [False] * 7
    q = deque([l[0]])
    visited[0] = True
    cnt = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if (ny, nx) in l and not visited[l.index((ny, nx))]:
                visited[l.index((ny, nx))] = True
                q.append((ny, nx))
                cnt += 1
    if cnt < 7:
        return False
    return True


def check2(l):
    cnt = 0
    for y, x in l:
        if arr[y][x] == 'S':
           cnt += 1
    if cnt >= 4:
        return True
    return False

res = 0
for comb in combs:
    if check2(comb):
        if check(comb):
            res += 1
print(res)


