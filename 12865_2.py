N,K = map(int,input().split())

arr = [0] * (15) # 1차원

for i in range(N): # 아이템을 하나씩 추가
    w,v = map(int,input().split())

    for j in range(K-w,-1,-1): #거꾸로 안하면 중복 업데이트될 수도 있음
        arr[j+w] = max(arr[j+w],arr[j]+v)
    # print(arr)
print(max(arr))