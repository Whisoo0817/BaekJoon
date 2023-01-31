import sys
input = sys.stdin.readline
n = int(input())
people = [[int(input()), 1] for _ in range(n)]
def binary_search(start,end,num): #reverse
    end -=1
    while start <= end:
        mid = (start+end)//2
        if s[mid][0]==num:
            return mid
        elif s[mid][0]<num:
            end = mid - 1
        else:
            start = mid + 1
    return end
s = [[people[0][0], 1]]
lenS = 1
res = 0
for i in range(1,n):
    # print(s,lenS,res)
    if people[i][0] > s[-1][0]:
        k = binary_search(0,len(s),people[i][0])
        if k == -1:
            s.clear()
            res += lenS
            lenS = 0
        else:
            while s:
                l = s.pop()
                if l[0]<people[i][0]:
                    res += l[1]
                    lenS -= l[1]
                else:
                    s.append(l)
                    break
        if s:
            if s[-1][0] == people[i][0]:
                if lenS == s[-1][1]:
                    res += s[-1][1]
                else:
                    res += (s[-1][1]+1)
                s[-1][1] += 1
                lenS += 1
            else:
                s.append([people[i][0],1])
                lenS+=1
                res+=1
        else:
            s.append([people[i][0],1])
            lenS+=1
    elif people[i][0] < s[-1][0]:
        s.append(people[i])
        res += 1
        lenS += 1
    else:
        if lenS==s[-1][1]:
            res+=s[-1][1]
            s[-1][1]+=1
        else:
            s[-1][1] += 1
            res += s[-1][1]
        lenS += 1
print(res)