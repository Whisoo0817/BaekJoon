import sys
input = sys.stdin.readline
n = int(input())
wei = list(map(int, input().split()))
wei.sort()

res = wei[0]
if res > 1: # 반례: 2,3,4,5
    print(1)

else:
    for i in range(1, n):
        if wei[i] > res + 1:
            break
        res += wei[i]

    print(res+1)

# 반례: 1,2,4,8,16,32,64
