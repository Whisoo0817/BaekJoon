import sys
input = sys.stdin.readline
import heapq
n = int(input())
q = []
l=0
for i in range(n):
    k = int(input())
    if k<0:
        heapq.heappush(q,[abs(k),-1]) #절댓값이 같을 때는 음수를 먼저 출력해야해서
        l+=1                          #두번째 인자를 작게 (-1)
    elif k>0:
        heapq.heappush(q,[abs(k),1])
        l+=1
    else:
        if l==0:
            print(0)
        else:
            t = heapq.heappop(q)
            if t[1]==-1:
                print(-1*t[0])
            else:
                print(t[0])
            l-=1
