# 인터넷 BFS 풀이 (진입차수가 0이 되면 선행조건 완료 => 큐에 삽입)
# 내 DFS 풀이는 목표부터 거꾸로 시작해서 필요없는 탐색을 안함 => 좀 더 빠름
import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    cost = [0] + list(map(int, input().split()))
    rule = [[] for _ in range(n+1)]
    dp = [0]*(n+1)
    indegree = [0]*(n+1) #진입차수
    for i in range(k):
        x, y = map(int, input().split())
        rule[x].append(y)
        indegree[y] += 1
    q = deque()
    for i in range(n+1):
        if indegree[i]==0:
            q.appendleft(i)
            dp[i] = cost[i]
    while q:
        a = q.pop()
        for i in rule[a]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[a] + cost[i])
            if indegree[i]==0:
                q.appendleft(i)

    W = int(input())
    print(dp[W])