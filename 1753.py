# 다익스트라가 dp인 이유 : 최단 거리는 여러개의 최단거리로 이루어져있다 (sub-problem)
import sys
import heapq
input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())
dist = [1e9] * (V+1)
edge = [[] for _ in range(V+1)]
heap = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edge[u].append([w, v])

def Dikstra(start):
    dist[start] = 0
    heapq.heappush(heap,(0,start))
    while heap:
        print(heap)
        wei, now = heapq.heappop(heap)
        if dist[now] < wei:
            continue
        for w, next_node in edge[now]:
            next_wei = w + wei
            if next_wei < dist[next_node]:
                dist[next_node] = next_wei
                heapq.heappush(heap, (next_wei, next_node))
Dikstra(K)
for i in range(1,V+1):
    print("INF" if dist[i]==1e9 else dist[i])