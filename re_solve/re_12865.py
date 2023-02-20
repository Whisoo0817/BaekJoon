# import sys
# input = sys.stdin.readline
# n, k = map(int, input().split())
# item = [list(map(int, input().split())) for _ in range(n)]
# dp = [[0]*(k+1) for _ in range(n+1)]
# for w in range(1, k+1):
#     for j in range(1, n+1):
#         dp[j][w] = dp[j-1][w] # 중요 (아이템 무게가 커서 dp[j-1][w] = 0인 경우가 있어서 쭉 갖고 와야함)
#         if item[j-1][0] <= w:
#             dp[j][w] = max(dp[j][w], dp[j-1][w-item[j-1][0]]+item[j-1][1])
# print(dp[n][k])

N, K = map(int, input().split())
arr = [0] * 10
for i in range(N):
    w, v = map(int, input().split())
    for j in range(K-w, -1, -1): # 거꾸로 안하면 먼저 업데이트 된 값이 다음 업데이트에 이용될 수 있음
        arr[j+w] = max(arr[j+w], arr[j]+v)
    # print(arr)
print(arr[K])




