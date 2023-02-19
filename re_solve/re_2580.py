import sys
input = sys.stdin.readline
a = [list(map(int, input().split())) for _ in range(9)]

def check(k):
    nums = [False] *10
    for i in range(9):
        nums[a[k[0]][i]] = True
        nums[a[i][k[1]]] = True
    m, n = (k[0]//3)*3, (k[1]//3)*3
    for i in range(3):
        for j in range(3):
            nums[a[m+i][n+j]] = True
    noNum = []
    for i in range(1, 10):
        if not nums[i]:
            noNum.append(i)
    return noNum

q = []
for i in range(9):
    for j in range(9):
        if a[i][j] == 0:
            q.append((i, j))
len_q = len(q)
def sol(ord):
    if ord == len_q:
        for i in a:
            print(*i)
        exit(0) # 중요 => return 사용 시, 모두 0일 때 시간 초과
    candids = check(q[ord])
    for candid in candids:
        a[q[ord][0]][q[ord][1]] = candid
        sol(ord+1)
        a[q[ord][0]][q[ord][1]] = 0 # 백트래킹에서 가장 중요한 부분!!
sol(0)





