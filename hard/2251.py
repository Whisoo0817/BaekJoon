import sys
from collections import deque
input = sys.stdin.readline
a = list(map(int, input().split()))
res = []
visited = [[[False]*201 for _ in range(201)] for l in range(201)]
q = deque([])
q.append([0, 0, a[2]])
visited[0][0][a[2]] = True
def move(t,k,p):
    tmp = [t[0], t[1], t[2]]
    tmp[p] += tmp[k]
    over = tmp[p] - a[p]
    if over > 0:
        tmp[p] = a[p]
        tmp[k] = over
    else:
        tmp[k] = 0
    return tmp
while q:
    t = q.popleft()
    if t[0] == 0:
        res.append(t[2])
    for i in range(3):
        if t[i] > 0:
            for j in range(3):
                if i != j:
                    r = move(t, i, j)
                    if not visited[r[0]][r[1]][r[2]]:
                        visited[r[0]][r[1]][r[2]] = True
                        q.append(r)
print(*sorted(res))











