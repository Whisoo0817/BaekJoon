import sys
import heapq
input = sys.stdin.readline
N, E = map(int, input().split())
edge = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    edge[a].append([c, b]) # 인자 순서 주의
    edge[b].append([c, a])
v1, v2 = map(int, input().split())
def Dikstra(start, end):
    dist = [1e9] * (N+1)
    dist[start] = 0
    heap = []
    heapq.heappush(heap, (0, start)) # 최소힙에서 정렬해야하므로 첫번째 인자가 현재 dist
    while heap:
        wei, now = heapq.heappop(heap)
        if wei > dist[now]:
            continue
        for w, next_node in edge[now]:
            next_wei = wei + w
            if next_wei < dist[next_node]:
                dist[next_node] = next_wei
                heapq.heappush(heap, (next_wei, next_node))
    return dist[end]
a = Dikstra(1,v1) + Dikstra(v1,v2) + Dikstra(v2,N)
b = Dikstra(1,v2) + Dikstra(v2,v1) + Dikstra(v1,N)
print(-1 if a+b >= 1e9 else min(a,b))


