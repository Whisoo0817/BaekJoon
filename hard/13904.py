import sys
input = sys.stdin.readline
from queue import PriorityQueue
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort()
q = PriorityQueue()
idx = 0

for day in range(1, arr[-1][0] + 1):
    if idx == n:
        break
    while arr[idx][0] == day: # 일단 해당 day 과제 모두 큐에 put
        q.put(arr[idx][1])
        idx += 1
        if idx == n:
            break
    while q.qsize() > day: # day 개수 만큼 남을 때까지 가장 낮은 과제 pop
        tmp = q.get()

res = 0
while q.qsize() > 0:
    res += q.get()
print(res)
