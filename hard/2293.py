import sys
input = sys.stdin.readline
n, k = map(int,input().split())
v = [int(input()) for _ in range(n)]
dp = [0]*10001
dp[0] = 1
for i in v: #(1+1)+2 = 2+(1+1) 처럼 겹치면 안되기 때문에 동전 하나씩
    for j in range(i,k+1):
        # print(j,j-i)
        dp[j] += dp[j-i]
print(dp[k])
