import sys
input = sys.stdin.readline
n,c = map(int,input().split())
house = sorted([int(input()) for _ in range(n)])
start = 0
end = house[-1] - house[0]
while start<=end:
    mid = (start+end)//2
    # print(start,end,mid)
    total = 0
    temp = house[0]
    for i in range(1,n):
        if house[i]-temp >= mid:
            temp = house[i]
            total+=1
    # print(total)
    if total < c-1:
        end = mid-1
    else:
        start = mid+1
print(end)





