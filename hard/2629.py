import sys
input = sys.stdin.readline
n = int(input()) # n<=30
weight = list(map(int, input().split())) + [0] #중요*****
m = int(input()) # m<=7
marble = list(map(int, input().split()))
dp = [[0]*40001 for _ in range(31)]
def sol(i,w):
    if i > n:
        return
    if dp[i][w]:
        return
    dp[i][w] = 1
    sol(i+1,w)
    sol(i+1,w+weight[i])
    sol(i+1,abs(w-weight[i]))

sol(0,0)
for i in marble:
    if dp[n][i]==1:
        print('Y',end=' ')
    else:
        print('N', end=' ')