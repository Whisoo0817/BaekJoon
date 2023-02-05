import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int,input().split())
q = deque([N])
visited = [1e9] * 100001
visited[N] = 0
while q:
    x = q.popleft()

    if x <= 50000 and (visited[x*2] > visited[x]):
        q.append(x*2)
        visited[x*2] = visited[x]
    if x < 100000 and (visited[x+1] > visited[x]+1):
        q.append(x+1)
        visited[x+1] = visited[x]+1
    if x > 0 and (visited[x-1] > visited[x]+1):
        q.append(x-1)
        visited[x-1] = visited[x]+1

print(visited[K])