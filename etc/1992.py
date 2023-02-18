import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = []
for i in range(n):
    graph.append(input().rstrip())
res = deque()
def sol(n,x,y):
    global res
    if n==1:
        res.append(graph[x][y])
        return
    zero,one=0,0
    for i in range(n):
        for j in range(n):
            if graph[x+i][y+j]=='0':
                zero+=1
            else:
                one+=1
    if one==n*n:
        res.append('1')
    elif zero==n*n:
        res.append('0')
    else:
        res.append('(')
        sol(n // 2, x, y)
        sol(n // 2, x, y+n//2)
        sol(n // 2, x+n//2, y)
        sol(n // 2, x + n // 2, y + n // 2)
        res.append(')')
sol(n,0,0)
for i in res:
    print(i,end='')