import sys
input = sys.stdin.readline
key = list(input().rstrip())
code = list(input().rstrip())
sorting = [[key[i], i, 0, ''] for i in range(len(key))]
sorting.sort()
for i in range(len(key)):
    sorting[i][2] = i

l = len(code) // len(key)
for i in range(len(code)):
    sorting[i//l][3] += code[i]
sorting.sort(key=lambda x:x[1])

res = ''
for i in range(l):
    for j in range(len(sorting)):
        res += sorting[j][3][i]
print(res)
