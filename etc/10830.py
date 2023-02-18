import sys
input = sys.stdin.readline
N, b = map(int, input().split())
a = []
for i in range(N):
    a.append(list(map(int, input().split())))
def mul(x,y):
    l = len(x)
    mul_res = [[0]*l for _ in range(l)]
    for i in range(l):
        for j in range(l):
            for k in range(l):
                mul_res[i][j] += x[i][k] * y[k][j]
            mul_res[i][j] %= 1000
    return mul_res
def sol(a,b):
    if b==1:
        for i in range(N):
            for j in range(N):
                a[i][j] = a[i][j]%1000
        return a
    temp = sol(a,b//2)

    if b%2==0:
        return mul(temp,temp)
    else:
        return mul(mul(temp,temp),a)
res = sol(a,b)
for i in res:
    for j in i:
        print(j,end=' ')
    print()
