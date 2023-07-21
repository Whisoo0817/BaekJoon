import sys
import heapq
input = sys.stdin.readline
n = int(input())
q = list(int(input()) for _ in range(n))
heapq.heapify(q)
res = 0
while n > 1:
    x = heapq.heappop(q)
    y = heapq.heappop(q)
    heapq.heappush(q, x+y)
    res += (x+y)
    n -= 1
print(res)


