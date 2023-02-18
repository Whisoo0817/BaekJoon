# 전체 개수 - 교차하지 않는 최대 집단 = 없애야할 최소 개수
import sys
n = int(sys.stdin.readline())
a=[]
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    a.append([x, y])
a.sort()
# print()
# for i in a:
#     print(i)
dp = [1] * n # 1 == 본인
for i in range(1,n):
    for j in range(i):
        if a[i][1] > a[j][1]:
            dp[i] = max(dp[i], dp[j]+1)
print(n - max(dp))
