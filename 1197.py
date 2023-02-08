import sys
from collections import deque
input = sys.stdin.readline
V, E = map(int, input().split())
edge = []
parent = [i for i in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    edge.append([c, a, b])
edge.sort(reverse=True)
edge = deque(edge)
def find(a):
    if a==parent[a]:
        return a
    p = find(parent[a])
    parent[a] = p
    return parent[a]
def union(a,b):
    a = find(a)
    b = find(b)
    if a==b:
        return
    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
res = 0
while edge:
    w, a, b = edge.pop()
    if find(a)!=find(b):
        union(a,b)
        res+=w
print(res)
