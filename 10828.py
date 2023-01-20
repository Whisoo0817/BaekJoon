import sys
input = sys.stdin.readline
stack = []
def sol(a,stack):
    l = len(stack)
    if len(a)>=6:
        x,y = a.split()
        stack.append(int(y))
    elif a=='top':
        if l==0:
            print(-1)
        else:
            print(stack[-1])
    elif a=='size':
        print(l)
    elif a=='empty':
        if l==0:
            print(1)
        else:
            print(0)
    elif a=='pop':
        if l==0:
            print(-1)
        else:
            print(stack[-1])
            del stack[-1]

n = int(input())
for i in range(n):
    a = input().strip()
    sol(a,stack)





