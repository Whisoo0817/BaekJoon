import sys
input = sys.stdin.readline
N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
res = 1e9
# 1번집이 어떤 색으로 칠하는 지
# (한번에 update 하게 되면 1번집과 마지막 집의 색 비교가 어려움)
for i in range(3):
    dp = [[1e9, 1e9, 1e9] for _ in range(N)]
    dp[0][i] = cost[0][i]
    for j in range(1, N):
        dp[j][0] = cost[j][0] + min(dp[j - 1][1], dp[j - 1][2])
        dp[j][1] = cost[j][1] + min(dp[j - 1][0], dp[j - 1][2])
        dp[j][2] = cost[j][2] + min(dp[j - 1][0], dp[j - 1][1])
    for k in range(3):
        if k != i:
            res = min(res, dp[-1][k])
print(res)
