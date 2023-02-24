import sys
import heapq
input = sys.stdin.readline
for _ in range(int(input())):
    k = int(input())
    q1, q2 = [], []
    visited = [False] * 1000001
    for i in range(k):
        command, n = input().rstrip().split()
        n = int(n)
        if command == 'I':
            heapq.heappush(q1, (n, i))
            heapq.heappush(q2, (n*-1, i))
            visited[i] = True
        else:
            if n == 1:
                while q2:
                    tmp = heapq.heappop(q2)
                    if visited[tmp[1]]:
                        visited[tmp[1]] = False
                        break
            else:
                while q1:
                    tmp = heapq.heappop(q1)
                    if visited[tmp[1]]:
                        visited[tmp[1]] = False
                        break
    res = []
    while q1:
        tmp = heapq.heappop(q1)
        if visited[tmp[1]]:
            res.append(tmp[0])
    if len(res)==0:
        print('EMPTY')
    else:
        print(res[-1], res[0])








