# LIS 문제
import sys
input = sys.stdin.readline
n = int(input())
port = list(map(int, input().split()))
def binary(arr, k):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if k == arr[mid]:
            return mid
        elif k > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return end + 1
dp = [port[0]]
for i in range(1, n):
    if dp[-1] >= port[i]:
        dp[binary(dp, port[i])] = port[i]
    else:
        dp.append(port[i])
print(len(dp))
