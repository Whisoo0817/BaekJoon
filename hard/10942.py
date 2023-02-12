# 팰린드롬 = 좌우 대칭 => DP
# 반으로 나누게 되면 dp에 좌측 우측의 문자열을 저장하고 비교해야해서 메모리 초과
# => 첫번째 마지막 원소만 같은 지 비교하고 가운데는 dp로 확인
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
num = [0] + list(map(int, input().split()))
dp = [[0]*(n+1) for _ in range(n+1)]


for i in range(n):
    for j in range(1,n-i+1):
        if i==0:
            dp[j][j+i] = 1
        elif i==1:
            if num[j]==num[j+i]:
                dp[j][j+i] = 1
        else:
            if num[j] == num[j+i] and dp[j+1][j+i-1] == 1:
                dp[j][j+i] = 1
for i in range(int(input())):
    s, e = map(int, input().split())
    print(dp[s][e])









