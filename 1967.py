import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
visited = [-1]*(n+1)
def dfs(s,y):
    for i in graph[s]:
        next, w = i[0], i[1]
        if visited[next] == -1:
            visited[next] = w + y
            dfs(next, w+y)
visited[1] = 0
dfs(1,0)
next = visited.index(max(visited))
visited = [-1]*(n+1)
visited[next]=0
dfs(next,0)
print(max(visited))
