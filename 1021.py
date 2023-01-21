from collections import deque
import sys
input = sys.stdin.readline
n,m=map(int,input().split())
a = list(map(int,input().split()))
q = deque([i for i in range(1,n+1)])
res=0
done = 0

while done<m:
    if q[0]==a[done]:
        q.popleft()
        done+=1
    else:
        if q.index(a[done]) < (len(q)//2+1):
            q.append(q.popleft())
            res+=1
        else:
            q.appendleft(q.pop())
            res+=1
print(res)