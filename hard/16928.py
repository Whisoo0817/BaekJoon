import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
ladder = [[*map(int, input().split())] for _ in range(n)]
ladder2 = [ladder[i][0] for i in range(n)]
snake = [[*map(int, input().split())] for _ in range(m)]
snake2 = [snake[i][0] for i in range(m)]
q = deque([])
q.append(1)
tmp = [0]*101
nextN = 0
while q:
    x = q.popleft()
    if x in ladder2:
        nextN = ladder[ladder2.index(x)][1]
        if tmp[nextN]==0:
            tmp[nextN] = tmp[x]
        else:
            tmp[nextN] = min(tmp[nextN], tmp[x])
        q.append(nextN)
    elif x in snake2:
        nextN = snake[snake2.index(x)][1]
        if tmp[nextN]==0:
            tmp[nextN] = tmp[x]
        else:
            tmp[nextN] = min(tmp[nextN], tmp[x])
        q.append(nextN)
    else: # 22% Error : 사다리나 뱀이면 무조건 타야함(해당 자리에서 주사위 못굴림)
        for i in range(1,7):
            if x+i <= 100 and (tmp[x+i]==0 or tmp[x+i]>tmp[x]+1):
                # 처음 가거나 더 커서 갱신 가능할 때
    # 느린 루트인데 사다리를 타고 먼저 도착하는 케이스가 있어버림 => 모든 경우 돌리면서 최솟값 갱신 !!
                q.append(x+i)
                tmp[x+i] = tmp[x] + 1

print(tmp[100])