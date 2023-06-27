import sys
input = sys.stdin.readline
from queue import PriorityQueue
import math
res = 0
n = int(input())
coordinate = [list(map(float, input().split())) for _ in range(n)]
cost = [[] for _ in range(n)]
for i in range(n): # cost: 각 별 사이의 거리
    for j in range(n):
        if i == j:
            cost[i].append(0)
        else:
            cost[i].append(math.sqrt((coordinate[i][0] - coordinate[j][0])**2 +\
                           (coordinate[i][1] - coordinate[j][1])**2))
visited = [False] * n
q = PriorityQueue()
# 시작별 = 0번 별
visited[0] = True
cnt = 1
for i in range(n):
    if cost[0][i] != 0:
        q.put((cost[0][i], i)) # (거리, 도착별)

while cnt < n: # 모든 별이 연결될 때까지
    temp = q.get()
    if visited[temp[1]]: # 방문 check
        continue
    visited[temp[1]] = True
    cnt += 1
    res += temp[0]
    for i in range(n):
        if not visited[i]:
            q.put((cost[temp[1]][i], i))
print(round(res, 2))


