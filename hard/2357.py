import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(int(input()) for _ in range(n))
tree = [0] * (n * 4)
tree2 = [0] * (n * 4)
def init(start, end, idx):
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]
    mid = (start + end) // 2
    tree[idx] = max(init(start, mid, idx*2), init(mid + 1, end, idx*2 + 1))
    return tree[idx]
def init2(start, end, idx):
    if start == end:
        tree2[idx] = arr[start]
        return tree2[idx]
    mid = (start + end) // 2
    tree2[idx] = min(init2(start, mid, idx*2), init2(mid + 1, end, idx*2 + 1))
    return tree2[idx]

init(0, n-1, 1)
init2(0, n-1, 1)

def find(start, end, idx, left, right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree[idx]
    mid = (start + end) // 2
    return max(find(start, mid, idx*2, left, right), find(mid+1, end, idx*2 + 1, left, right))
def find2(start, end, idx, left, right):
    if left > end or right < start:
        return 1e9
    if left <= start and right >= end:
        return tree2[idx]
    mid = (start + end) // 2
    return min(find2(start, mid, idx*2, left, right), find2(mid+1, end, idx*2 + 1, left, right))

for _ in range(m):
    a, b = map(int, input().split())
    print(find2(1, n, 1, a, b), end=' ')
    print(find(1, n, 1, a, b))

