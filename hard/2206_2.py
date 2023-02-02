# BFS는 경로길이를 1씩 늘려가며 최단경로를 찾는 방법 !!
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    delta = ((-1,0), (1,0), (0,-1), (0,1))
    q = deque([(0, 0, 1, False)])
    visited = [[[False]*2 for _ in range(m)] for _ in range(n)]
    # [True,False] => 벽 안 부신 경로로 방문 했음
    # [True,True] => 벽 부신 경로, 안 부신 경로 모두 방문 했음
    visited[0][0][0] = True

    while q:
        x, y, cnt, flag = q.popleft() # 문법
        # print(x,y,cnt,flag)
        if x == n-1 and y == m-1:
            return cnt

        for dx, dy in delta: # 문법
            nx, ny = dx + x, dy + y
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny][flag]: #현재 flag 방문 안했으면
                visited[nx][ny][flag] = True
                if maze[nx][ny] == 0:
                    q.append((nx,ny,cnt+1,flag))
                elif maze[nx][ny] == 1 and not flag: # 1이고 현재 flag가 True(1)가 아니라면
                    q.append((nx,ny,cnt+1,True))

    return -1

n, m = map(int, input().split())
maze = [list(map(int,input().strip())) for _ in range(n)]
print(bfs())
