import sys
input = sys.stdin.readline
oasis = [int(input()) for _ in range(int(input()))]
stack = [] #(키, cnt)로 append
result = 0
for i in oasis:
    # 스택 끝 값보다 키가 크면 pop
    while stack and stack[-1][0] < i:
        result += stack.pop()[1]
    if not stack: # 스택이 비어있으면 해당 키 append하고 continue
        stack.append((i, 1))
        continue

    #스택 끝 값의 키와 같을 때 ***
    if stack[-1][0] == i:
        cnt = stack.pop()[1]
        result += cnt

        if stack: result += 1 # 7 6 5 5 5 + 5 에서 6때문에
        stack.append((i, cnt+1)) #자신까지 cnt에 +1
    #스택 끝 값의 키보다 작을 때
    else:
        stack.append((i,1))
        result += 1
print(result)

