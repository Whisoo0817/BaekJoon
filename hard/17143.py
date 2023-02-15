# speed 줄이는 게 중요
# move 함수 O(1)에 계산 해야함!
import sys
input = sys.stdin.readline
R, C, M = map(int, input().split())
sharks = [list(map(int, input().split())) for _ in range(M)]
sharkMap = [[[-1, -1] for _ in range(C+1)] for _ in range(R+1)]
for i in range(M):
    sharkMap[sharks[i][0]][sharks[i][1]] = [sharks[i][4], i] # 처음 맵 초기화
    if sharks[i][3] <= 2: # 속도 줄이기(중요)
        sharks[i][2] = sharks[i][2] % ((R-1)*2)
    else:
        sharks[i][2] = sharks[i][2] % ((C - 1) * 2)

def move(shark):
    dy, dx = [0,-1,1,0,0], [0,0,0,1,-1]
    y, x, speed, way, size = shark
    x += speed*dx[way]
    y += speed*dy[way]
    while not (1<=x<=C):
        if x < 1:
            x = 2 - x
            way -= 1
        if x > C:
            x = 2*C - x
            way +=1
    while not (1<= y <= R):
        if y < 1:
            y = 2 - y
            way += 1
        if y > R:
            y = 2 * R - y
            way -= 1
    return (y, x, way)

res = 0
for human in range(1, C+1):
    for depth in range(1, R+1):
        if sharkMap[depth][human][0] != -1: # 땅에서 가장 가까운 상어를 찾으면
            sharks[sharkMap[depth][human][1]][0] = -1 # 잡힌 상어 죽이고
            res += sharks[sharkMap[depth][human][1]][4] # 사이즈 더해주고
            sharkMap[depth][human] = [-1, -1] # 잡힌 상어 자리 초기화
            break
    for i in range(M): # 상어 이동하기 전에 맵 초기화(이전 위치가 영향을 줌)
        if sharks[i][0] != -1:
            sharkMap[sharks[i][0]][sharks[i][1]] = [-1, -1]

    for i in range(M):
        if sharks[i][0] != -1: #안 잡힌 상어만
            ny, nx, nway = move(sharks[i]) # 이동
            sharks[i][3] = nway  # 새로운 방향
            if sharkMap[ny][nx][0] == -1: # 새 자리에 상어가 없으면
                sharks[i][0], sharks[i][1] = ny, nx # 상어 정보 갱신
                sharkMap[ny][nx] = [sharks[i][4], i] # 맵 갱신
            else:
                if sharkMap[ny][nx][0] > sharks[i][4]: # 더 작으면
                    sharks[i][0] = -1 # 죽음
                else: # 더 크면
                    sharks[sharkMap[ny][nx][1]][0] = -1 # 작은 상어 잡아먹고
                    sharks[i][0], sharks[i][1] = ny, nx  # 상어 정보 갱신
                    sharkMap[ny][nx] = [sharks[i][4], i] # 맵 갱신

print(res)








