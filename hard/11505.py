import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
tree = [0] * (4*n)
R = 1000000007
def init(start, end, idx):
    if start == end:
        tree[idx] = arr[end]
        return tree[idx]
    mid = (start + end) // 2
    tree[idx] = init(start, mid, idx*2) * init(mid+1, end, idx*2 + 1) % R
    return tree[idx]
def mull(start, end, idx, left, right):
    if start > right or end < left:
        return 1
    if left <= start and end <= right:
        return tree[idx]
    mid = (start + end) // 2
    return mull(start, mid, idx*2, left, right) *\
            mull(mid+1, end, idx*2+1, left, right) % R
def update(start, end, idx, what, diff):
    if not (start <= what <= end):
        return
    if start == end:
        tree[idx] = diff
    else:
        mid = (start + end) // 2
        update(start, mid, idx*2, what, diff)
        update(mid+1, end, idx*2+1, what, diff)
        tree[idx] = tree[idx*2] * tree[idx*2 + 1] % R
init(0, n-1, 1)
for i in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(0, n-1, 1, b-1, c)
    else:
        print(mull(0, n-1, 1, b-1, c-1))





