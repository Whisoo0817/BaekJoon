import sys
input = sys.stdin.readline
n = int(input())
graph = []
for i in range(n):
    graph.append(input().rstrip().split())
a,b,c=0,0,0
def sol(n,x,y):
    global a,b,c
    if n==1:
        if graph[x][y]=='0':
            a+=1
        elif graph[x][y]=='1':
            b+=1
        else:
            c+=1
        return
    zero,one,minus=0,0,0
    for i in range(n):
        for j in range(n):
            if graph[x+i][y+j] == '0':
                zero+=1
            elif graph[x+i][y+j] == '1':
                one+=1
            else:
                minus+=1
    if zero==n*n:
        a+=1
    elif one==n*n:
        b+=1
    elif minus==n*n:
        c+=1
    else:
        sol(n//3,x,y)
        sol(n//3,x,y+n//3)
        sol(n//3,x,y+(n//3)*2)
        sol(n // 3,x+n//3,y)
        sol(n // 3,x+n//3,y+n//3)
        sol(n // 3,x+n//3,y+(n//3)*2)
        sol(n // 3,x+(n//3)*2,y)
        sol(n // 3,x+(n//3)*2,y+n//3)
        sol(n // 3,x+(n//3)*2,y+(n//3)*2)
sol(n,0,0)
print(c)
print(a)
print(b)