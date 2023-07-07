import sys
input = sys.stdin.readline
from itertools import combinations
n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
res = 1e9
house, chicken = [], []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])

for comb in combinations(chicken, m):
    chi_dis = 0
    for home in house:
        dis = 1e9
        for chi in comb:
            dis = min(dis, abs(chi[0]-home[0]) + abs(chi[1]-home[1]))
        chi_dis += dis
    res = min(res, chi_dis)
    
print(res)






