import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
dp = [0]*1000001
for i in a:
    dp[i] += 1
b = []
for i in range(n):
    b.append([dp[a[i]], i]) # [NGF, 원래위치]
stack = []
res = [-1] * n
for i in range(n):
    while True:
        if stack:
            k = stack.pop()
            if k[0] < b[i][0]:
                res[k[1]] = a[i]
            else:
                stack.append(k)
                break
        else:
            break
    stack.append(b[i])
print(*res)