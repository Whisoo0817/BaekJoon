# 구하는 값 : m
# a = 5m + k
# b = 7m + k
# c = 9m + k
# => a%m 과 b%m이 같다 = (a-b)이 m의 배수
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
a = [int(input()) for _ in range(n)]
sub = deque([])
for i in range(n-1):
    sub.append(abs(a[i+1]-a[i]))

def sol(x, y): #최대공약수(유클리드 호제법)
    while y>0:
        x, y = y, x%y
    return x

while len(sub)>1:
    x = sub.popleft()
    y = sub.popleft()
    sub.appendleft(sol(x,y))
k = sub[0] # 최대공약수

res = set()
res.add(k)
for i in range(2, int(k**0.5)+1):
    if k % i == 0:
        res.add(i)
        res.add(k//i)
res = sorted(list(res))
print(*res)




