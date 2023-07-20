import sys
import heapq # 힙큐의 push와 pop의 시간복잡도는 O(N)
input = sys.stdin.readline
lq, rq = [], [] # 왼쪽 최대힙 / 오른쪽 최소힙
l_len, r_len = 0, 0
r_min = -1e9 # 첫 입력을 rq에 넣기 위해서
# 계획: 오른쪽 최소힙 중 최소를 출력할 계획
for i in range(int(input())):
    k = int(input())
    if k >= r_min: # rq에 push
        heapq.heappush(rq, k)
        r_len += 1
        r_min = rq[0]
    else: # lq에 push
        heapq.heappush(lq, (-k, k))
        l_len += 1

    if l_len == r_len: # 두 힙 길이가 같으면 안됨 (1 2 3 | 4 5 6) -> 3을 rq로
        heapq.heappush(rq, heapq.heappop(lq)[1])
        l_len -= 1
        r_len += 1
        r_min = rq[0]
    elif l_len + 2 < r_len: # rq가 lq보다 2개 더 많을 때까지 허용 가능
        tmp = heapq.heappop(rq)
        heapq.heappush(lq, (-tmp, tmp))
        l_len += 1
        r_len -= 1
        r_min = rq[0]
    print(r_min)
