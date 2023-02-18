import sys
input = sys.stdin.readline
n = int(input())
paper = []
for i in range(n):
    paper.append(list(map(int, input().rstrip().split())))
blue,white = 0,0
def sol(n,x,y):
    global blue,white
    zero,one=0,0
    for i in range(n):
        for j in range(n):
            if paper[x+i][y+j] == 0:
                zero+=1
            else:
                one+=1
    if one==n*n:
        blue+=1
    elif zero==n*n:
        white+=1
    else:
        if n!=1:
            sol(n // 2, x, y)
            sol(n // 2, x + n // 2, y)
            sol(n // 2, x + n // 2, y + n // 2)
            sol(n // 2, x, y + n // 2)
sol(n,0,0)
print(white)
print(blue)