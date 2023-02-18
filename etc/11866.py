from collections import deque
import sys
input = sys.stdin.readline
n,k = map(int,input().split())
q = deque()
for i in range(n):
    q.append(i+1)
res = []
while len(q)>0:
    for i in range(k-1):
        q.append(q.popleft())
    res.append(q.popleft())
print('<',end='')
for i in res:
    if i==res[-1]:
        print(''.join([str(i),'>']))
    else:
        print(''.join([str(i),',',' ']),end='')