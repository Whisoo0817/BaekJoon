#출력 간단히, reverse() => O(N) 주의
from collections import deque
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    p = list(input().rstrip())
    n = int(input())
    a = input().rstrip()[1:-1].split(',') #한줄로
    b=deque()
    if a!=['']:
        for i in a:
            b.append(i)
    error=False

    i=0
    l=len(p)
    lb=len(b)
    error=False
    reverse=False
    while i<l:
        if p[i]=='R':
            if reverse:
                reverse=False
            else:
                reverse=True
        else:
            if lb == 0:
                print('error')
                error=True
                break
            if reverse:
                b.pop()
            else:
                b.popleft()
            lb-=1
        i+=1
    if error==False:
        if reverse:
            b.reverse()
        print("["+",".join(b)+"]") #한줄로




