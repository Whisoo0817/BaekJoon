import sys
input = sys.stdin.readline
s = list(input().rstrip())
bomb = list(input().rstrip())
m, k = len(s), len(bomb)
dp = []
i, stack, len_dp = 0,0,0

while i<m:
    dp.append(s[i])
    i += 1
    len_dp += 1
    temp = []
    if dp[-1]==bomb[-1] and len_dp >= k:
        for _ in range(k):
            temp.append(dp.pop())
        temp.reverse()
        if temp != bomb:
            dp += temp
        else:
            len_dp -= k
if len(dp)==0:
    print('FRULA')
else:
    for i in dp:
        print(i,end='')


