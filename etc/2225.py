import sys
input = sys.stdin.readline
N, K = map(int, input().split())
dp = [[0]*201 for _ in range(201)]
def sol(n,k):
    if dp[n][k] != 0:
        return dp[n][k]
    if k == 1:
        return 1
    res = 0
    for i in range(n+1):
        res += sol(n-i, k-1)
    dp[n][k] = res % (10**9)
    return dp[n][k]
print(sol(N,K))