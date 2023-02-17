import sys
from collections import deque
input = sys.stdin.readline
feed = []
for i in range(int(input())):
    feed.append(list(input().strip().split()))
    feed[i].remove(feed[i][0])
feed.sort()
new = []
for i in range(len(feed)):
    new.append(deque([]))
    for j in range(len(feed[i])):
         new[-1].append("--"*j + feed[i][j])

while len(new[-1])>0:
    total = 0
    for i in range(len(new)):
        if new[i] and total == 0:
            tmp = new[i].popleft()
            total = 1
            print(tmp)
        elif new[i] and total != 0:
            if new[i][0] != tmp:
                break
            else:
                new[i].popleft()
