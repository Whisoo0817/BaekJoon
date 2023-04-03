import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort()
dp = [1e9]*100001
visited = [False]*100001
for coin in coins:
    dp[coin] = 1
def sol(x):
    visited[x] = True
    for coin in coins:
        if coin < x:
            if not visited[x-coin]:
                dp[x] = min(dp[x], sol(x-coin)+1)
            else:
                dp[x] = min(dp[x], dp[x-coin]+1)
        else:
            break
    return dp[x]
sol(k)
print(dp)
print(-1 if dp[k]==1e9 else dp[k])
