import sys
input = sys.stdin.readline
n, m = map(int, input().split())
tree = list(map(int, input().split()))
start = 0
end = max(tree)
while start <= end:
    mid = (start+end)//2
    total = 0
    for i in tree:
        if i-mid >0:
            total+=(i-mid)
            if total>m: #pypy3이면 없어도 됨
                break
    if total < m:
        end = mid-1
    else: # 만족했으면 그 밑은 이제 안봐도 됨 (:최대 구하는 문제)
        start = mid+1
    print(start, end, mid)

print(end)