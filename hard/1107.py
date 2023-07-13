import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
costs = []
for i in range(m):
    a, b, c = map(int, input().split())
    costs.append((c, a, b))
costs.sort()
p = [v for v in range(n + 1)]
res = 0

def find(u):
    if p[u] != u:
        p[u] = find(p[u]) # 만약 내 집단의 부모가 바뀌면, 모두 update 필요
    return p[u]
def union(u, v):
#    p[u] = p[v] : 안됨 (아직 바뀐 부모가 p에 update 안됐을 수도 있음)
    root1 = find[u]
    root2 = find[v]
    p[root2] = p[root1]

for edge in costs:
    cost, x, y = edge
    if find(x) != find(y):
        union(x, y)
        res += cost
print(res)

