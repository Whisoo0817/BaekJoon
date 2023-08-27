import sys
input = sys.stdin.readline
from itertools import combinations
n, c = map(int, input().split())
item = list(map(int, input().split()))
left, right = item[:n//2], item[n//2:]
left_sum, right_sum = [], []

def sum_list(arr, arr_sum):
    for i in range(len(arr)+1):
        combs = list(combinations(arr, i))
        for comb in combs:
            arr_sum.append(sum(comb))
sum_list(left, left_sum)
sum_list(right, right_sum)
right_sum.sort()

res = 0
for sub in left_sum:
    if c - sub < 0:
        continue
    start, end = 0, len(right_sum)
    while start < end:
        mid = (start + end) // 2
        if right_sum[mid] <= c - sub:
            start = mid + 1
        else:
            end = mid
    res += start
print(res)


