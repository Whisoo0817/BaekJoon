import sys
from collections import deque
input = sys.stdin.readline
def bfs():
    v, e = map(int, input().split())
    a = [[] for _ in range(v + 1)]
    for o in range(e):
        x, y = map(int, input().split())
        a[x].append(y)
        a[y].append(x)
    visited = [[False,True] for o in range(v+1)] # [방문여부, 색깔(빨강or파랑)]
    q = deque([])
    for i in range(1,v+1): #모든 노드가 연결되어 있지않을 수도 있어서 모두 확인 ex) 1 (2,3,4) 5
        if visited[i][0] == False:
            q.append(i)
            visited[i][0] = True
        while q:
            x = q.popleft()
            for k in a[x]:
                if visited[k][0] == False: # bfs
                    q.append(k)
                    if visited[x][1]:
                        visited[k] = [True, False]
                    else:
                        visited[k] = [True, True]
                else: # *** 인접한 노드 중에 같은 색깔 있는지 확인 ***
                    if visited[k][1] == visited[x][1]:
                        return False
    return True
for _ in range(int(input())):
    if bfs():
        print('YES')
    else:
        print('NO')


