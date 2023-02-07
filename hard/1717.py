# union 굳이 합칠 필요 없고 부모만 바꿔주기
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
parent = [i for i in range(n+1)]
def find(a):
    if a == parent[a]:
        return a
    p = find(parent[a]) # 중요: 갱신 안해주면 쓸데없이 계속 또 돌아서 RecursionError
    parent[a] = p
    return parent[a]
def union(a,b):
    a = find(a)
    b = find(b)
    if a==b:
        return
    elif a<b:
        parent[b] = a
    else:
        parent[a] = b
for _ in range(m):
    what, a, b = map(int, input().split())
    if what == 0:
        union(a,b)
    else:
        if find(a)==find(b):
            print('YES')
        else:
            print('NO')
