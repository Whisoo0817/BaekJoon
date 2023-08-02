import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
tree = [0] * (n * 4)
def init(start, end, idx):
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]
    mid = (start + end) // 2
    tree[idx] = min(init(start, mid, idx*2), init(mid+1, end, idx*2 + 1))
    return tree[idx]

init(0, n-1, 1)

def find(start, end, idx, left, right):
    if start > right or end < left:
        return 1e9 + 1                  # 각 정수 값들의 범위가 1~10^9 => 1e9 쓰면 틀림
    if left <= start and end <= right:
        return tree[idx]
    mid = (start + end) // 2
    return min(find(start, mid, idx*2, left, right), find(mid+1, end, idx*2+1, left, right))

for _ in range(m):
    a, b = map(int, input().split())
    print(find(1, n, 1, a, b))


