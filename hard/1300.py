import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
def check(num): #O(N)
    small, equal = 0, 0
    if n >= num:
        for i in range(1,num+1):
            if num % i == 0:
                equal +=1
            small += num//i
    else:
        for i in range(1,n+1):
            if num % i == 0:
                if num//i <= n:
                    equal += 1
            small += min(n, num//i)
    return [small, equal]

start,end = 1, n**2
mid = (start+end)//2
while start<=end:
    mid = (start+end)//2
    temp = check(mid)
    # print(start,end,mid,temp)
    if temp[0]-temp[1] >= k:
        end = mid-1
    elif temp[0] < k:
        start = mid+1
    if temp[0]-temp[1] < k <= temp[0]:
        break
print(mid)



# 1 2 3  4
# 2 4 6  8
# 3 6 9  12
# 4 8 12 16