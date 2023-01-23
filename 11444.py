# 피보나치: F(n+m) = F(m-1)F(n) + F(m)F(n-1)
import sys
input = sys.stdin.readline
N = int(input())
dp = [[0,0],[1,1],[2,1],[3,2]]
def fibo(x):
    for i in range(len(dp)):
        if dp[i][0]==x:
            return dp[i][1]
    print(x)
    n = x // 2
    if x%2==0:
        res = fibo(n)*(fibo(n)+2*fibo(n-1))
    else:
        res = fibo(n)**2 + fibo(n+1)**2
    dp.append([x,res])
    return res%1000000007
print(fibo(N))