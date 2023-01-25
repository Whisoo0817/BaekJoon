# 답의 범위는 1 ~ max 길이 (a~b) => 이분 탐색
import sys
input = sys.stdin.readline
k, n = map(int, input().split())
l = []
for i in range(k):
    l.append(int(input()))
a = 1
b = max(l)
while a<=b:
    m = (a+b)//2
    # print(a, b, "mid=", m)
    s = 0
    for i in l:
        s += i//m
    if s<n:
        b = m-1
    else: # 만족했으면 오른쪽만 보면 됨 (:최대 구하는 문제)
        a = m+1
print(b)