import sys
import heapq
input = sys.stdin.readline
def Dikstra(start):
    heap = []
    dist = [1e9] * (n+1)
    heapq.heappush(heap, (0, start))
    dist[start] = 0
    while heap:
        wei, now = heapq.heappop(heap)
        if wei > dist[now]:
            continue
        for w, next_node in graph[now]:
            next_wei = wei + w
            if next_wei < dist[next_node]:
                dist[next_node] = next_wei
                heapq.heappush(heap, (next_wei, next_node))
    return dist
for _ in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for j in range(m):
        a, b, d = map(int, input().split())
        graph[a].append([d,b])
        graph[b].append([d,a])
    test = [int(input()) for _ in range(t)]
    res = []
    dis_start = Dikstra(s)
    dis_g = Dikstra(g)
    dis_h = Dikstra(h)
    for i in test:
        if dis_start[i]==dis_start[g]+dis_g[h]+dis_h[i] or dis_start[i]==dis_start[h]+dis_h[g]+dis_g[i]:
            res.append(i)
    res.sort()
    print(*res)




