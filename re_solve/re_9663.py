import sys
input = sys.stdin.readline
n = int(input())
row = [-1] * n # idea: 퀸이 행의 몇 열에 있는지
visited = [False] * n
def check(x):
    for i in range(x): # 윗줄만 확인 !!!!
        if row[i] == row[x] or abs(x-i) == abs(row[x]-row[i]): # 대각선
            return False
    return True
res = 0
def sol(x):
    global res
    if x == n:
        res += 1
        return
    for i in range(n):
        if not visited[i]:
            row[x] = i
            if check(x):
                visited[i] = True
                sol(x+1)
                # row[x] = 0 어차피 윗줄만 확인 => 필요 X
                visited[i] = False

sol(0)
print(res)








