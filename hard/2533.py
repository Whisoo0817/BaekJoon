import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())
friends = [[] for _ in range(n + 1)]
for i in range(n-1):
    u, v = map(int, input().split())
    friends[u].append(v)
    friends[v].append(u)
dp = [[1, 0] for _ in range(n+1)] # [현재 노드가 어답터일때, 아닐때]
visited = [False]*(n+1)
def DFS(num):
    visited[num] = True
    for friend in friends[num]:
        if not visited[friend]:
            tmp = DFS(friend)
            dp[num][0] += min(tmp)
            dp[num][1] += tmp[0]
    return dp[num]
DFS(1)
print(min(dp[1]))



