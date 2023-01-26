import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    k = int(input())
    file = [0] + list(map(int, input().split()))
    subSum = [0] * 501
    for i in range(k):
        subSum[i+1] = subSum[i]+file[i+1]
    minCost = [[0]*501 for _ in range(501)]
    for i in range(1,k):
        for j in range(1,k-i+1):
            start, end = j, j+i
            result = 1e9
            for cut in range(start,end):
                result = min(result, minCost[start][cut] + minCost[cut+1][end] + subSum[end] - subSum[start-1])
            minCost[start][end] = result
    print(minCost[1][k])


