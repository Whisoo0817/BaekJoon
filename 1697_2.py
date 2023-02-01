import sys
input = sys.stdin.readline
from collections import deque
MAX = 100000
tmp = [0] * (MAX+1)
n,k = map(int,input().split())
q = deque([])
q.append(n)
def bfs():
    while q:
        x = q.popleft()
        if x == k:
            return tmp[k]
        else:
            for nx in (x-1,x+1,x*2):
                if 0 <= nx <= MAX and tmp[nx] == 0:
                    tmp[nx] = tmp[x] + 1
                    q.append(nx)
print(bfs())