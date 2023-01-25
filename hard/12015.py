# longest increasing subsequence
# DP => O(n^2)
# 이분탐색 => O(nlogn) - 암기 필요
import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
def update(num): #이분탐색으로 O(logn)으로 위치 찾기
    global l
    start, end = 0, l-1
    while start<=end:
        mid = (start+end)//2
        if b[mid] == num: # 같으면 배열 b 업데이트 x
            return -1
        elif b[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    return start

b = [a[0]]
l = 1
for i in range(1, n):
    if a[i] < b[-1]:
        k = update(a[i])
        if k!=-1:
            b[k] = a[i]
    elif a[i] > b[-1]:
        b.append(a[i])
        l+=1
print(len(b))
