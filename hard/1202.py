# 아이디어: 작은 가방부터 채워야함
import heapq
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
jewel = [[] for _ in range(1000001)]
for i in range(n):
    m, v = map(int, input().split())
    heapq.heappush(jewel[m], v)

bag = []
for i in range(k):
    heapq.heappush(bag, int(input()))

def sol():
    res = 0
    variable = []
    k = len(bag)
    for i in range(1000001):
        for j in jewel[i]:
            heapq.heappush(variable, j*-1)
        while bag[0] == i:
            heapq.heappop(bag)
            k -= 1
            if variable:
                res += abs(heapq.heappop(variable))
            if k==0:
                return res

print(sol())


