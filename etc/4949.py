import sys
input = sys.stdin.readline
while True:
    res='yes'
    stack = []
    k = list(input().rstrip())
    if len(k)==1 and k[0]=='.':
        break
    for i in k:
        if i=='(':
            stack.append('(')
        elif i=='[':
            stack.append('[')
        elif i==')':
            if len(stack)==0:
                res='no'
                break
            else:
                if stack[-1]=='(':
                    del stack[-1]
                else:
                    res='no'
                    break
        elif i==']':
            if len(stack)==0:
                res='no'
                break
            else:
                if stack[-1] == '[':
                    del stack[-1]
                else:
                    res = 'no'
                    break

    if res=='yes' and len(stack)==0:
        res='yes'
    else:
        res='no'
    print(res)

