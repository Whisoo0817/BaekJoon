import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))
a.sort()

for i in check:
    start = 0
    end = n - 1
    ok=True
    while start<=end:
        mid = (start+end)//2
        if i<a[mid]:
            end = mid-1
            continue
        elif i>a[mid]:
            start = mid+1
        else:
            print(1)
            ok=False
            break
    if ok:
        print(0)

