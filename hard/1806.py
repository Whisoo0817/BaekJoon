import sys
input = sys.stdin.readline
n, s = map(int,input().split())
a = [0] + list(map(int,input().split()))
for i in range(1,n+1):
    a[i] = a[i-1]+a[i]
res = 1e9
start, end = 0, 1

while end <= n:
    if a[end] - a[start] < s:
        end += 1
    else:
        res = min(res,end-start)
        start += 1
print(res if res!=1e9 else 0)

