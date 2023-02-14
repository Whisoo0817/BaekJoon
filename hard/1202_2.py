import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
jewel = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]
jewel.sort()
bags.sort()

q = []
res = 0
for bag in bags:
    while jewel and jewel[0][0] <= bag:
        heapq.heappush(q, heapq.heappop(jewel)[1] * - 1)
    if q:
        res -= heapq.heappop(q)
print(res)

