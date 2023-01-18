import sys
input = sys.stdin.readline
a = list(input().rstrip())
res = 0
r = False
temp = ''
for i in range(len(a)):
    if a[i]=='-':
        if r==False:
            res+=int(temp)
        else:
            res-=int(temp)
        temp = ''
        if r==False:
            r = True
    elif a[i]=='+':
        if r:
            res-=int(temp)
            temp=''
        else:
            res+=int(temp)
            temp=''
    else:
        temp+=a[i]
if r:
    res -=int(temp)
else:
    res+=int(temp)
print(res)



