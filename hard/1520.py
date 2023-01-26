import sys
input = sys.stdin.readline
m, n = map(int, input().split())
a = []
for _ in range(m):
    a.append(list(map(int,input().split())))
dx = [1,0,-1,0]
dy = [0,1,0,-1]
dp = [[0]*n for _ in range(m)]

def find(x,y):
    total = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < m and nx >= 0 and ny < n and ny >= 0:
            if a[x][y] > a[nx][ny]:
                if dp[nx][ny] == -1: # 진행해도 어차피 갈 곳이 없는 경우
                    continue
                elif nx==m-1 and ny==n-1: #목표지점
                    total += 1
                elif dp[nx][ny] > 0: # 다시 갈 필요 없음(dp)
                    total += dp[nx][ny]
                else:
                    total += find(nx,ny) #처음가는 곳
    if total == 0 and (x!=0 or y!=0): #답이 0일 때 (0,0)의 dp값이 -1이 나오면 안됨
        dp[x][y] = -1
        return 0
    else:
        dp[x][y] += total
        return total
find(0,0)
print(dp[0][0])
