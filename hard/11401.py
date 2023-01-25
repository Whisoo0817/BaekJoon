# p가 소수일 때 : a^(p-1) = 1 (mod p) ... 1번
# a*b (mod p) = {a (mod p) * b (mod p)} (mod p) ... 2번
# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ해설ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
# 이항계수(n,k)
# = nCk
# = n!/(k!*(n-k)!)
# 2번으로는 곱으로 된 수의 나머지만  구할 수 있는데, 분모(나머지)가 있음 => 없애줘야함
# 분자에 *1을 해줌 => 1번에 따르면 1 = a^(p-1)
# => n! * 1 /(k!*(n-k)!)
# = n! * (k!*(n-k)!)^p-1 / /(k!*(n-k)!)
# = n! * (k!*(n-k)!)^p-2
import sys
input = sys.stdin.readline
MOD = 1000000007
n, k = map(int, input().rstrip().split())
a = 1
for i in range(1,n+1):
    a = a * i % MOD
b = 1
for i in range(1,k+1):
    b = b * i % MOD
c = 1
for i in range(1,n-k+1):
    c = c * i % MOD
def pow(a,b): #by 1629번 문제 (분할정복으로 거듭제곱 풀기)
    if b==1:
        return a
    temp = pow(a,b//2)
    if b%2==0:
        return temp*temp % MOD
    else:
        return temp*temp*a % MOD
print((a * pow(b*c % MOD, MOD-2)) % MOD)