import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
parent = [i for i in range(n)]
def find(a):
    if a == parent[a]:
        return a
    p = find(parent[a])
    parent[a] = p
    return parent[a]
def union(a,b):
    a = find(a)
    b = find(b)
    if a==b:
        return 1
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return 0
done = False
for _ in range(m):
    a, b = map(int, input().split())
    if union(a,b):
        print(_+1)
        done = True
        break
if not done:
    print(0)


