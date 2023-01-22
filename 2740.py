import sys
input = sys.stdin.readline
n,m = map(int,input().split())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
m,k = map(int,input().split())
b = []
for i in range(m):
    b.append(list(map(int,input().split())))
res = [[0]*k for _ in range(n)]
for i in range(n):
    for j in range(k):
        for l in range(m):
            res[i][j]+=a[i][l]*b[l][j]
for i in res:
    for j in i:
        print(j,end=' ')
    print()