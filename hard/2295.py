# a+b+c = d => a+b = d-c
# set과 dictionary 에서의 in 연산의 시간복잡도는 O(1)~O(N)이다.
import sys
input = sys.stdin.readline
n = int(input())
nums = [int(input()) for _ in range(n)]

a_b_sum = set()
for i in nums:
    for j in nums:
        a_b_sum.add(i+j)

res = set()
for i in nums:
    for j in nums:
        if (i-j) in a_b_sum:
           res.add(i)
print(max(list(res)))
