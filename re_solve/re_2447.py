def sol(N):
    if N==1:
        return ["*"]
    last = sol(N//3)
    L = []
    for a in last:
        L.append(a*3)
    for a in last:
        L.append(a+" "*len(last)+a)
    for a in last:
        L.append(a*3)
    return L
N=int(input())
print('\n'.join(sol(N)))

# import sys
# input = sys.stdin.readline
# N = int(input())
# res = [''] * N
# def sol(f,n):
#     print(f,n)
#     global res
#     if n == 1:
#         res[f] += "*"
#         return
#     for _ in range(3):
#         sol(f, n//3)
#     sol(f+n//3, n//3)
#     for i in range(n//3):
#         res[f+n//3+i] += ' ' * (n//3)
#     sol(f+n//3, n//3)
#     for _ in range(3):
#         sol(f+(n//3)*2, n//3)
# sol(0, N)
# for i in res:
#     print(i)
