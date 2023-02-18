import sys
input = sys.stdin.readline
n, k = map(int, input().split())
bag = [[0,0]] + [list(map(int,input().split())) for _ in range(n)]
bag.sort()
dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(1,k+1):
    for j in range(1, n + 1):
        w, v = bag[j][0], bag[j][1]
        if w > i:
            dp[j][i] = dp[j-1][i]
        else:
            dp[j][i] = max(dp[j-1][i], dp[j-1][i-w] + v)
# print()
# for i in dp:
#     print(i)

print(dp[n][k])


