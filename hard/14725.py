import sys
input = sys.stdin.readline
feed = []
for i in range(int(input())):
    feed.append(input().strip().split()[1:])
tmp = []
for i in sorted(feed):
    count = 0
    for j in range(len(tmp)):
        if tmp[j] == i[j]:
            count += 1
        else:
            break
    cnt = count
    for j in range(count, len(i)):
        print('--'*cnt + i[j])
        cnt += 1
    tmp = i
