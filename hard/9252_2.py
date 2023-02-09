# 배열에 LCS 길이(숫자)가 아닌 문자열 자체를 저장하는 방법
import sys
input = sys.stdin.readline
a = [''] + list(input().strip())
b = [''] + list(input().strip())
LCS = [['']*len(b) for _ in range(len(a))]
for i in range(1,len(a)):
    for j in range(1,len(b)):
        if a[i] == b[j]:
            LCS[i][j] = LCS[i-1][j-1] + a[i]
        else:
            if len(LCS[i-1][j]) >= len(LCS[i][j-1]):
                LCS[i][j] = LCS[i-1][j]
            else:
                LCS[i][j] = LCS[i][j-1]
result = LCS[-1][-1]
print(len(result), result, sep='\n')