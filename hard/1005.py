import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def DFS(num):
    if dp[num]!=-1:
        return dp[num]
    if rule[num]:
        dp[num] = cost[num]
        tmp = []
        for k in rule[num]:
            tmp.append(DFS(k))
        dp[num] += max(tmp)
        return dp[num]
    else:
        dp[num] = cost[num]
        return dp[num]

for _ in range(int(input())):
    n, k = map(int, input().split())
    cost = [0] + list(map(int, input().split()))
    rule = [[] for _ in range(n+1)]
    dp = [-1]*(n+1)
    for i in range(k):
        x, y = map(int, input().split())
        rule[y].append(x)
    W = int(input())
    DFS(W)
    print(dp[W])


