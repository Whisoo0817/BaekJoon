# 가장 긴 증가하는 부분 수열의 '길이'
import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))
tmp = [A[0]]

def binary(k):
    start, end = 0, len(tmp) - 1
    while start <= end:
        if start == end:
            return end
        mid = (start + end) // 2
        if k <= tmp[mid]:
            end = mid
        else:
            start = mid + 1
    return end

for i in range(1, n):
    if A[i] > tmp[-1]:
        tmp.append(A[i])
    else:
        idx = binary(A[i])
        tmp[idx] = A[i]
print(len(tmp))


