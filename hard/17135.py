import sys
import copy
import heapq
from itertools import combinations
input = sys.stdin.readline
N, M, D = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
maps.append([0]*M)
castle = [i for i in range(M)]
arrow = list(combinations(castle,3))
def shoot(a, pos,round):
    enemy = []
    if pos-D+1<0:
        k = 0
    else:
        k = pos-D+1
    for i in range(k, pos+D):
        for j in range(D - abs(pos-i)):
            x = N-1-round-j
            y = i
            if 0<=x<N and 0<=y<M:
                if a[x][y]==1:
                    d = abs(j+1) + abs(i-pos)
                    heapq.heappush(enemy, (d, y, x))
    if len(enemy)>0:
        return heapq.heappop(enemy)
    else:
        return -1

def sol(a,poss):
    removed = 0
    for round in range(N):
        enemys = set()
        for k in range(3):
            t = shoot(a, poss[k], round)
            if t != -1:
                enemys.add((t[2],t[1]))
        for k in enemys:
            a[k[0]][k[1]] = 0
            removed += 1
    return removed
res = 0
for i in arrow:
    tmp = copy.deepcopy(maps)
    res = max(res, sol(tmp,i))
print(res)






