import sys
input = sys.stdin.readline
n = int(input())
array = []
dic = {}
for _ in range(n):
    a, b = map(int, input().split())
    array.append((a, b))
    dic[b] = a
array = sorted(array)
arr = [array[i][1] for i in range(n)]

def binary_search(k, temp):
    start = 0
    end = len(temp)-1
    while start <= end:
        mid = (start + end) // 2
        if temp[mid] == k:
            return mid
        if temp[mid] < k:
            start = mid + 1
        else:
            end = mid - 1
    return end + 1

tmp = [arr[0]]
dp = [0]
for i in range(1, n):
    idx = binary_search(arr[i], tmp)
    if idx + 1 > len(tmp):
        tmp.append(arr[i])
    else:
        tmp[idx] = arr[i]
    dp.append(idx)

cnt = len(tmp) - 1
k = len(arr)-1
removed = []
while cnt >= 0:
    if dp[k] == cnt:
        removed.append(dic.get(arr[k]))
        cnt -= 1
    k -= 1
res = sorted(list(set(dic.values()) - set(removed)))
print(len(res))
for k in res:
    print(k)


# 4
# 1 2
# 2 3
# 3 4
# 4 1

