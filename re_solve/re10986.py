import sys
from math import comb
input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))
dp = [0]
for i in A:
    dp.append((dp[-1] + i) % M)
dp2 = [0] * M
for i in dp:
    dp2[i] += 1
res = 0
for i in dp2:
    res += comb(i, 2)
print(res)

