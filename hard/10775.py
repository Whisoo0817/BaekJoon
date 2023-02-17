import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
G = int(input())
P = int(input())
g = [int(input()) for _ in range(P)]
parent = [i for i in range(100001)]
def find(a):
    if parent[a] == a:
        return a
    p = find(parent[a])
    parent[a] = p # 갱신
    return parent[a]
res = 0
for i in range(P):
    k = find(g[i])
    parent[k] = k-1
    if k-1 < 0:
        break
    res += 1
print(res)





