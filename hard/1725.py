from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
a = [int(input()) for _ in range(n)]
def binary_search(s, e, num):
    start = s
    end = e
    while start<=end:
        mid = (start+end)//2
        if num==stack[mid][0]:
            return [mid,True] #일치하는 값이 있으면 그 값의 index return
        elif num > stack[mid][0]:
            start = mid+1
        else:
            end = mid-1
    return [end,False] #일치하는 값이 없으면 새로운 값이 들어갈 index return
res = 0
stack = deque([[a[0],0]])
len_stack = 1
for i in range(1,n):
    # print(stack, len_stack, res)
    if stack:
        if a[i] > stack[-1][0] :
            stack.append([a[i], i])
            len_stack += 1
        elif a[i] < stack[-1][0]:
            k = binary_search(0, len_stack, a[i])
            if k[0]==-1: j = len_stack # a[i]보다 큰 수가 없을 때
            elif k[1]==False: j = len_stack-k[0]-1 # a[i]와 같은 수가 없을 때
            else: j = len_stack-k[0] # a[i]와 같은 수가 있을 때, 그 수까지 pop
            temp = i
            for _ in range(j): #pop하면서 result 업데이트
                tmp = stack.pop()
                res = max(res, tmp[0] * (i - tmp[1]))
                len_stack -= 1
                if _ == j-1:
                    temp = tmp[1]
            stack.append([a[i], temp]) #temp = 마지막으로 pop되는 것의 index 이어받기
            len_stack += 1
for i in range(len_stack):
    res = max(res, stack[i][0] * (n - stack[i][1])) #마지막으로 result 업데이트 (필수)
print(res)