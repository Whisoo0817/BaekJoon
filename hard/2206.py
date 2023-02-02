import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
a = [list(input().rstrip()) for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
tmp = [[[0]*2 for _ in range(m)] for o in range(n)]
q = deque([])
q.append([0,0,0])
tmp[0][0][0] = 1
while q:
    u = q.popleft()
    x,y = u[0],u[1]
    # print(tmp[x][y]) # BFS는 경로길이를 하나씩 늘려가며 최단경로를 찾는 방법!!
    if x==n-1 and y ==m-1:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= n-1 and 0 <= ny <= m-1:
            if u[2]==0:
                if a[nx][ny] == '0' and tmp[nx][ny][0] == 0:
                    q.append([nx,ny,0])
                    tmp[nx][ny][0] = tmp[x][y][0] + 1
                elif a[nx][ny] == '1' and tmp[nx][ny][1] == 0:
                    q.append([nx,ny,1])
                    tmp[nx][ny][1] = tmp[x][y][0] + 1
            else:
                if a[nx][ny] == '0' and tmp[nx][ny][1] == 0 and tmp[nx][ny][0]==0:
                    q.append([nx,ny,1])
                    tmp[nx][ny][1] = tmp[x][y][1] + 1
res = []
for i in tmp[n-1][m-1]:
    if i!=0:
        res.append(i)
if len(res)==0:
    print(-1)
else:
    print(min(res))
# for i in tmp:
#     print(i)

# 5 8
# 00000000
# 11111110
# 00000000
# 01111111
# 00000000