import sys
input = sys.stdin.readline
L, C = map(int, input().split())
a = sorted(list(input().strip().split()))

def sol(idx,odd,even,l,word):
    # print(idx,odd,even,l,word)
    if l==L:
        if odd >= 2 and even >= 1:
            print(word)
        return

    for i in range(idx,C):
        if a[i] not in ['a','e','i','o','u']:
            sol(i+1,odd+1,even,l+1,word+a[i])
        else:
            sol(i+1,odd,even+1,l+1,word+a[i])
sol(0,0,0,0,'')

