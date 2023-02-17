# https://chanhuiseok.github.io/posts/baek-28/
# 1. lines를 start가 아닌, end 지점 기준으로 정렬
#    => 큐에 하나씩 순차적으로 담을 수 있음 (start 기준으로 하면 처음에 어디까지 탐색해야할지 애매함)
# 2. 우선순위 큐 사용(시작점 기준)
#    => 큐에 들어있는 line들 중 start지점이 삐져나오면 pop해야함
import sys
import heapq
input = sys.stdin.readline
n = int(input())
lines = []
for i in range(n):
    tmp = list(map(int, input().split()))
    lines.append([min(tmp), max(tmp)])
lines.sort(key=lambda x:x[1])
D = int(input())
q = []
res = 0
for i in range(n):
    start, end = lines[i][0], lines[i][1]
    if end - start <= D:
        heapq.heappush(q, lines[i])
    while q:
        tmp = heapq.heappop(q)
        if tmp[0] >= end - D:
            heapq.heappush(q, tmp)
            break
    res = max(res, len(q))
print(res)