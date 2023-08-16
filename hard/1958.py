# 2차원 LCS 2번 -> 예외 case
# => 3차원 LCS 1번
import sys
input = sys.stdin.readline
a = [''] + list(input().strip())
b = [''] + list(input().strip())
c = [''] + list(input().strip())
graph = [[[0] * len(c) for _ in range(len(b))] for _ in range(len(a))]

for i in range(1, len(a)):
    for j in range(1, len(b)):
        for k in range(1, len(c)):
            if a[i] == b[j] == c[k]:
                graph[i][j][k] = graph[i-1][j-1][k-1] + 1
            else:
                graph[i][j][k] = max(graph[i-1][j][k], graph[i][j-1][k], graph[i][j][k-1])
print(graph[-1][-1][-1])
# import sys
# input = sys.stdin.readline
# a = [''] + list(input().strip())
# b = [''] + list(input().strip())
# c = [''] + list(input().strip())
# LCS = [[''] * len(b) for _ in range(len(a))]
# for i in range(1, len(a)):
#     for j in range(1, len(b)):
#         if a[i] == b[j]:
#             LCS[i][j] = LCS[i-1][j-1] + a[i]
#         else:
#             if len(LCS[i-1][j]) >= len(LCS[i][j-1]):
#                 LCS[i][j] = LCS[i-1][j]
#             else:
#                 LCS[i][j] = LCS[i][j-1]
#
# tmp = [''] + list(LCS[-1][-1])
# graph = [[0] * len(c) for _ in range(len(tmp))]
# for i in range(1, len(tmp)):
#     for j in range(1, len(c)):
#         if tmp[i] == c[j]:
#             graph[i][j] = graph[i-1][j-1] + 1
#         else:
#             graph[i][j] = max(graph[i-1][j], graph[i][j-1])
# print(graph[-1][-1])




