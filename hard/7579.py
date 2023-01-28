# 중복 x => 0/1 냅색
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
sl = [[0,0]] + sorted([[cost[i], memory[i]] for i in range(n)])
dp = [[0]*10001 for _ in range(n+1)]
def sol():
    for i in range(0,sum(cost)+1):
        for j in range(1,n+1):
            dp[j][i] = dp[j-1][i]
            if sl[j][0] <= i:
                dp[j][i] = max(dp[j][i], dp[j-1][i-sl[j][0]] + sl[j][1])
                if dp[j][i] >= m:
                    return i

print(sol())




