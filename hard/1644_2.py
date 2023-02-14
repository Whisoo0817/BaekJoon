import sys
import math
input = sys.stdin.readline

n = int(input())
arr = [True]*(n+1)

# 에라토스테네스의 체
for i in range(2, int(math.sqrt(n)) + 1):
    if arr[i]:
        j = 2
        while i*j <= n:
            arr[i*j] = False
            j+= 1
prime = []
for i in range(2,n+1):
    if arr[i]:
        prime.append(i)
res = 0
s = len(prime)
for k in range(s):
    total = 0
    while total < n and k < s:
        total += prime[k]
        if total == n:
            res += 1
        k += 1
print(res)