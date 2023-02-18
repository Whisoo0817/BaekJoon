import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
for i in range(n):
    a[i] = [a[i], i]
stack = []
res = [-1] * n
for i in range(n):
    while True:
        if stack: # ***
            k = stack.pop()
            if k[0] < a[i][0]:
                res[k[1]] = a[i][0]
            else:
                stack.append(k)
                break
        else:
            break
    stack.append(a[i])
print(*res)