import sys
input = sys.stdin.readline
n = int(input())
dp = [0] * 31
dp[2] = 3
def sol(k):
    if k % 2 == 1 or k <= 3:
        return
    if k >= 4:
        dp[k] += dp[k-2] * 3
    h = k-4
    while h > 0:
        dp[k] += dp[h] * 2
        h -= 2
    dp[k] += 2

for i in range(1, 31):
    sol(i)
print(dp[n])





