from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
q = deque()
for i in range(n):
    q.append(i+1)

len_q = n
while len_q>1:
    q.popleft()
    len_q-=1
    q.append(q.popleft())
print(q[0])


