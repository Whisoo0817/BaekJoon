import sys
input = sys.stdin.readline
k = int(input())
stack = []
for i in range(k):
    a = int(input())
    if a==0:
        if len(stack)!=0:
            del stack[-1]
    else:
        stack.append(a)
print(sum(stack))