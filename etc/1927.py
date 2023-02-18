import sys
input = sys.stdin.readline
import heapq
n = int(input())
q = []
l=0
for i in range(n):
    k = int(input())
    if k!=0:
        heapq.heappush(q,k)
        l+=1
    else:
        if l==0:
            print(0)
        else:
            print(heapq.heappop(q))
            l-=1
