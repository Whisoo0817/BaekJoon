import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
bus = [[] for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    bus[a].append([c, b])
d = [[1e9]*(n+1) for _ in range(n+1)]
for i in range(n+1): # 출발지 = 도착지
    d[i][i] = 0
for i in range(1,n+1):
    for j in bus[i]:
        w, next_node = j[0], j[1]
        d[i][next_node] = min(d[i][next_node], w) # 같은 노선 다른 비용 주의
def p(d):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if d[i][j] == 1e9:
                print(0, end= ' ')
            else:
                print(d[i][j], end=' ')
        print()
def floid():
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
floid()
p(d)
