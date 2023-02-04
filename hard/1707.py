import sys
from collections import deque
input = sys.stdin.readline
def bfs():
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    for o in range(e):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    visited = [False] * (v+1) # ***False => 방문 x / 1,-1 => 색깔 구분 (0=False,1=-1=True)
    q = deque([])
    for i in range(1,v+1): #모든 노드가 연결되어 있지않을 수도 있어서 모두 확인 ex) 1 (2,3,4) 5
        if not visited[i]:
            q.append(i)
            visited[i] = 1
        while q:
            x = q.popleft()
            for k in graph[x]:
                if not visited[k]: # bfs
                    q.append(k)
                    visited[k] = visited[x] * -1
                elif visited[k] == visited[x]: # *** 인접한 노드 중에 같은 색깔 있는지 확인 ***
                    return False
    return True
for _ in range(int(input())):
    if bfs():
        print('YES')
    else:
        print('NO')


