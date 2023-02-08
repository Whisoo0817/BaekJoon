import sys
input = sys.stdin.readline
a = [''] + list(input().strip())
b = [''] + list(input().strip())
graph = [[0]*(len(a)) for _ in range(len(b))]
res = ''
for i in range(1, len(b)):
    for j in range(1, len(a)):
        if a[j] == b[i]:
            graph[i][j] = graph[i-1][j-1] + 1
        else:
            graph[i][j] = max(graph[i-1][j], graph[i][j-1])
i, j = len(b)-1, len(a)-1
print(graph[i][j])
res = ''
while i>=1 and j>=1:
    if a[j]==b[i]:
        res += a[j]
        i -= 1
        j -= 1
    else:
        if graph[i-1][j] >= graph[i][j-1]:
            i -= 1
        else:
            j -= 1
print(res[::-1])
