import sys
input = sys.stdin.readline
A = ' ' + input().rstrip()
B = ' ' + input().rstrip()
a, b = len(A), len(B)
lcs = [[0]*a for _ in range(b)]

for i in range(1, b):
    for j in range(1, a):
        if A[j] == B[i]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

print(lcs[b-1][a-1])
