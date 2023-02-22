import sys
input = sys.stdin.readline
code = input().rstrip()
n = int(input())
voca = [input().rstrip() for _ in range(n)]
def decode(a, b):
    if ord(a)+b > 122:
        return chr(ord(a)+b-26)
    else:
        return chr(ord(a)+b)
def find(small, big):
    goal = len(small)
    k = 0
    l = 0
    len_big = len(big)
    while l < len_big:
        if small[k] == big[l]:
            k += 1
            if k == goal:
                return True
        else:
            k = 0
        l += 1
    return False
def sol():
    for i in range(1,27):
        res = ''
        for j in code:
            res += decode(j, i)
        for j in voca:
            if find(j, res):
                return res
print(sol())




