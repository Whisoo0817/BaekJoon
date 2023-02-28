# str()의 시간복잡도 = O(log(n)) (자릿수)
import sys
input = sys.stdin.readline
from collections import deque
for _ in range(int(input())):
    A, B = map(int, input().split())
    visited = [False]*10001
    q = deque([])
    q.append([A, ''])
    visited[A] = True
    while q:
        tmp, cmd = q.popleft()
        if tmp == B:
            print(cmd)
            break
        if tmp*2 > 9999:
            if not visited[(tmp * 2) % 10000]:
                q.append([(tmp*2) % 10000, cmd+'D'])
                visited[(tmp * 2) % 10000] = True
        else:
            if not visited[tmp*2]:
                q.append([tmp*2, cmd+'D'])
                visited[tmp*2] = True
        if tmp == 0:
            if not visited[9999]:
                q.append([9999, cmd+'S'])
                visited[9999] = True
        else:
            if not visited[tmp-1]:
                q.append([tmp-1, cmd+'S'])
                visited[tmp-1] = True

        first = tmp//1000
        l = (tmp%1000)*10 + first
        if not visited[l]:
            q.append([l, cmd+'L'])
            visited[l] = True
        last = tmp%10
        r = last*1000 + tmp//10
        if not visited[r]:
            q.append([r, cmd+'R'])
            visited[r] = True


