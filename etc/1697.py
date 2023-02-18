import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
a = [0] * 100001
a[k] = 1
q = deque([])
q.append([n,0])
while q:
    u = q.popleft()
    res = u[1]
    if a[u[0]] == 1:
        print(res)
        break
    a[u[0]] = 2 # visited
    if u[0] >= 1:
        if a[u[0]-1] != 2: # 같은 점을 방문하면 무한반복
            # 같은 점을 다른 경로로 찾더라도 무조건 시간이 더 느려 탐색할 필요가 없음
            q.append([u[0]-1,res+1])
    if u[0] < 100000:
        if a[u[0]+1] != 2:
            q.append([u[0]+1,res+1])
    if u[0] <= 50000:
        if a[u[0]*2] != 2:
            q.append([u[0]*2,res+1])