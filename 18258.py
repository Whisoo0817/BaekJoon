# remove, slice,... => O(N) !!!
import sys
input = sys.stdin.readline
q= []
l=0
pop=0
def sol(a,q):
    global l
    global pop
    if len(a)>=6:
        x,y = a.split()
        q.append(y)
        l+=1
    elif a=='pop':
        if l==0:
            print(-1)
        else:
            print(q[pop])
            pop+=1
            l-=1
            if l<0:
                l=0
    elif a=='size':
        print(l)
    elif a=='empty':
        if l==0:
            print(1)
        else:
            print(0)
    elif a=='front':
        if l==0:
            print(-1)
        else:
            print(q[pop])
    elif a=='back':
        if l==0:
            print(-1)
        else:
            print(q[-1])

n = int(input())
for i in range(n):
    a = input().rstrip()
    sol(a,q)