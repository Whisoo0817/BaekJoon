import sys
input = sys.stdin.readline
t = int(input())
def sol(a):
    stack=0
    if len(a)%2==1:
        print('NO')
        return
    else:
        for i in a:
            if i=='(':
                stack+=1
            else:
                stack-=1
            if stack<0:
                print('NO')
                return
        if stack==0:
            print('YES')
        else:
            print('NO')
    return
for _ in range(t):
    a = list(input().strip())
    sol(a)


