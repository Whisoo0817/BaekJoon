import sys
input = sys.stdin.readline
a = []
n = int(input())
for i in range(n):
    a.append(int(input()))
k = 1
h = 0
stack = [1]
res=['+']
while h<n and k<=n:
    if len(stack)>0 and stack[-1]==a[h]:
        res.append('-')
        del stack[-1]
        h+=1
    else:
        k+=1
        stack.append(k)
        res.append('+')
if len(stack)==0:
    for i in res:
        print(i)
else:
    print('NO')




