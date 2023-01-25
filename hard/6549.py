import sys
input = sys.stdin.readline

def sol(start,end):
    if start==end:
        return height[start]
    # 경계 부분을 무조건 포함하는 사각형의 최대넓이 구하기
    mid = (start+end)//2
    i, j = mid-1, mid+2
    mid_min = min(height[mid],height[mid+1])
    mid_max = mid_min * 2
    while start <= i or j <= end:
        if i < start:
            mid_min = min(mid_min, height[j])
            j += 1
        elif j > end:
            mid_min = min(mid_min, height[i])
            i -= 1
        elif height[i] < height[j]:
            mid_min = min(mid_min, height[j])
            j += 1
        else:
            mid_min = min(mid_min, height[i])
            i -= 1
        mid_max = max(mid_max, mid_min*(j-i-1))
    #좌우 분할
    l = sol(start,mid)
    r = sol(mid+1,end)
    k = max(l,r)
    return max(k,mid_max)

while True:
    height = list(map(int, input().split()))
    if len(height)==1 and height[0]==0:
        break
    print(sol(1,height[0]))