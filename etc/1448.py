import sys
input = sys.stdin.readline
nums = [int(input()) for i in range(int(input()))]
l = len(nums)
nums = sorted(nums, reverse=True)
for i in range(l-2):
    if nums[i] < nums[i+1] + nums[i+2]:
        print(nums[i] + nums[i+1] + nums[i+2])
        exit(0)
print(-1)