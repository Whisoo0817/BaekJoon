import sys
input= sys.stdin.readline
v = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(v):
    tmp = list(map(int,input().split()))
    l = 1
    while True:
        if tmp[l] == -1:
            break
        else:
            graph[tmp[0]].append([tmp[l], tmp[l+1]])
            l += 2
visited = [False] * (v+1)
visited[1] = True
res = 0
def dfs(s):
    global res
    neighbor = []
    for i in graph[s]:
        next, w = i[0], i[1]
        if not visited[next]:
            visited[next] = True
            neighbor.append(w + dfs(next))

    if len(neighbor)==0:
        return 0
    elif len(neighbor)==1:
        res = max(res, neighbor[0])
        return neighbor[0]
    else:
        neighbor.sort(reverse=True)
        res = max(res, neighbor[0] + neighbor[1])
        return neighbor[0]
dfs(1)
print(res)


