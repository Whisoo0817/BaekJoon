import sys
import heapq
input = sys.stdin.readline
def Dikstra(start):
    heap = []
    dist = [1e9] * (n+1)
    heapq.heappush(heap, (0, 0, start)) # g-h 구간을 지남 여부를 나타내는 flag 추가 (0 or -1)
    dist[start] = 0
    while heap:
        # print(heap)
        wei, flag, now = heapq.heappop(heap)
        if wei > dist[now]:
            continue
        for w, next_node in graph[now]:
            next_wei = wei + w
            if next_wei <= dist[next_node]:
                if (now, next_node)==(g,h) or (now, next_node)==(h,g):
                    heapq.heappush(heap, (next_wei, -1, next_node))
                    includeGH[next_node] = -1
                else:
                    if next_wei == dist[next_node] and includeGH[next_node]!=flag:# -1,0
                        heapq.heappush(heap, (next_wei, -1, next_node))
                        includeGH[next_node] = -1
                    elif next_wei == dist[next_node] and includeGH[next_node]==flag:
                        continue # 이거 안하면 시간초과
                    else:
                        heapq.heappush(heap, (next_wei, flag, next_node))
                        includeGH[next_node] = flag
                dist[next_node] = next_wei

    # print(includeGH)
    return includeGH
for _ in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for j in range(m):
        a, b, d = map(int, input().split())
        graph[a].append([d,b])
        graph[b].append([d,a])
    test = [int(input()) for _ in range(t)]
    includeGH = [0] * (n+1) # 최소 경로가 g-h를 포함하는지. -1이면 포함

    res = []
    FinalIncludeGH = Dikstra(s)
    for i in test:
        if FinalIncludeGH[i] == -1:
            res.append(i)
    res.sort()
    print(*res)



