import sys
import bisect
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
dp = [0] * n
tmp = [nums[0]]
dp[0] = 1 # 해당 수가 최대가 되는 LIS 길이
len_dp = 1
for i in range(1,n):
    if nums[i] > tmp[-1]:
        tmp.append(nums[i])
        len_dp += 1
        dp[i] = len_dp
    else:
        idx = bisect.bisect_left(tmp, nums[i])
        tmp[idx] = nums[i]
        dp[i] = idx + 1
    # print(nums[i], "추가")
    # print("tmp:", tmp)
    # print("dp:", dp)
res = []
max_len = len(tmp) # = 만들 수 있는 LIS 길이 (12015번 문제)
for i in range(n-1,-1,-1):
    if dp[i] == max_len:
        res.append(nums[i])
        max_len -= 1
    if max_len < 1:
        break
print(len(res))
print(*res[::-1])



