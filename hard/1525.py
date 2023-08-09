# 해시를 사용하면 좋은 경우
# 1. list[1]은 되지만 list["123"]은 안됨
# 2. Dictionary의 시간복잡도는 대부분 O(1)
import sys
input = sys.stdin.readline
from collections import deque
arr = ""
for _ in range(3):
    arr += input().strip().replace(" ", "")
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
visited = {arr: 1}
q = deque([(0, arr)])
def bfs():
    while q:
        cnt, tmp = q.popleft()
        if tmp == "123456780":
            return cnt
        pos = tmp.find("0")
        x = pos // 3
        y = pos % 3
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 3 and 0 <= ny < 3:
                nxt = nx * 3 + ny
                new = list(tmp)
                new[pos], new[nxt] = new[nxt], new[pos]
                new = "".join(new)
                if visited.get(new, 0) == 0: # 없으면 0
                    visited[new] = 1
                    q.append((cnt+1, new))
    return -1
print(bfs())
