import sys
import math
input = sys.stdin.readline

n = int(input())
a = [False, False] + [True]*(n-1)
prime = []
# 에라토스테네스의 체
for i in range(2, n + 1):
    # 소수 여부를 prime이 아닌, a에만 나타내려면 (2, int(math.sqrt(n))+1)로 가능
    if a[i]:
        prime.append(i)
        j = 2
        while i*j <= n:
            a[i*j] = False
            j += 1
res = 0
# 투 포인터
s, e = 0, 0
while e <= len(prime):
    temp_sum = sum(prime[s:e])
    if temp_sum == n:
        res += 1
        e += 1
    elif temp_sum < n:
        e += 1
    else:
        s += 1
print(res)





