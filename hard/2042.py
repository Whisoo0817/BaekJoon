import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
arr = [int(input()) for i in range(n)]
tree = [0] * (n * 4)
def init(start, end, idx):
    if start == end:
        tree[idx] = arr[end]
        return tree[idx]
    mid = (start + end) // 2
    tree[idx] = init(start, mid, idx*2) + init(mid + 1, end, idx*2 + 1)
    return tree[idx]

def summ(start, end, idx, left, right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree[idx]
    mid = (start + end) // 2
    return summ(start, mid, idx*2, left, right) \
           + summ(mid + 1, end, idx*2 + 1, left, right)

def update(start, end, idx, what, before, after): # ***
    if not (start <= what <= end):
        return
    tree[idx] += (after - before) # ***
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, idx*2, what, before, after)
    update(mid+1, end, idx*2 + 1, what, before, after)
init(0, n-1, 1)
for i in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        k = summ(0, n-1, 1, b-1, b-1)
        update(0, n-1, 1, b-1, k, c)
    else:
        print(summ(0, n-1, 1, b-1, c-1))



