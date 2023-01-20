from collections import deque
import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n,m=map(int,input().split())
    q = deque(list(map(int,input().split())))
    res=0
    while q:
        max_q = max(q)
        num = q.popleft()
        m-=1
        if num==max_q:
            res+=1
            if m<0:
                print(res)
                break
        else:
            q.append(num)
            if m<0:
                m = len(q)-1