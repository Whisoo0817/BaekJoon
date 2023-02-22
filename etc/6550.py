import sys
from collections import deque
input = sys.stdin.readline

def sol():
    s, t = input().strip().split()
    s = deque(s)
    for k in t:
        if not s:
            break
        if k == s[0]:
            s.popleft()
    if not s:
        return 'Yes'
    else:
        return 'No'

while True:
    try:
        print(sol())
    except:
        break