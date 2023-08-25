import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
def binary_search(k, arr):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if k == arr[mid]:
            return mid
        if k > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return end + 1
temp = [A[0]]
dp = [0]
for i in range(1, n):
    idx = binary_search(A[i], temp)
    dp.append(idx)
    if idx >= len(temp):
        temp.append(A[i])
    else:
        temp[idx] = A[i]
resn = len(temp) - 1
res = []
for i in range(n-1, -1, -1):
    if dp[i] == resn:
        res.append(A[i])
        resn -= 1
print(len(temp))
print(*res[::-1])
