import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def DFS(num):
    global result
    cycle.append(num)
    visited[num] = True
    next_num = edge[num]
    if visited[next_num]:
        if next_num in cycle:
            result += cycle[cycle.index(next_num):]
    else:
        DFS(next_num)


for _ in range(int(input())):
    n = int(input())
    edge = [0] + list(map(int, input().split()))
    visited = [False] * (n+1)
    result = []
    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            DFS(i)
    print(n-len(result))





