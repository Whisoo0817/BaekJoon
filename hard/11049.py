import sys
input = sys.stdin.readline
n = int(input())
a = [[0,0]]
for _ in range(n):
    r, c = map(int, input().split())
    a.append([r, c])
dp = [[0]*501 for _ in range(501)]
for i in range(1,n):
    for j in range(1,n-i+1):
        result = 1e9
        start, end = j, j+i
        for cut in range(start,end):
            result = min(result, dp[start][cut] + dp[cut+1][end] + a[start][0]*a[cut][1]*a[end][1])
        dp[start][end] = result
print(dp[1][n])
