import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
def sol(l):
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if l[i] > l[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return dp
left = sol(a)
right = sol(a[::-1])[::-1]
for i in range(n):
    left[i] += right[i]
print(max(left) - 1)
