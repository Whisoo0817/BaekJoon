#이분 그래프 DFS 버전
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start, color):
    visited[start] = color
    for i in graph[start]:
        if not visited[i]:
            a = dfs(i, color * -1) # 인접한 노드 다른 색으로 칠하고 재귀
            if not a:
                return False
        elif visited[i] == visited[start]:
            return False
    return True

for _ in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    for o in range(e):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    visited = [False] * (v + 1)  # ***False => 방문 x / 1,-1 => 색깔 구분 (0=False,1=-1=True)
    result = True
    for i in range(1,v+1):
        if not visited[i]:
            result = dfs(i,1)
            if not result: # result가 False가 나오면 더 이상 수행할 필요 x
                break
    print('YES' if result else 'NO')