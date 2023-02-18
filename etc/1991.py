import sys
input = sys.stdin.readline
n = int(input())
edge = [[] for _ in range(n+1)]
for i in range(n):
    a, b, c = input().strip().split()
    if b=='.':
        edge[ord(a)-64].append(0)
    else:
        edge[ord(a) - 64].append(ord(b) - 64)
    if c=='.':
        edge[ord(a) - 64].append(0)
    else:
        edge[ord(a) - 64].append(ord(c) - 64)

pre_res=''
def pre(s):
    global pre_res
    pre_res += chr(s+64)
    if edge[s][0]!=0:
        pre(edge[s][0])
    if edge[s][1]!=0:
        pre(edge[s][1])
pre(1)
print(pre_res)
inor_res=''
def inor(s):
    global inor_res
    if edge[s][0]!=0:
        inor(edge[s][0])
    inor_res += chr(s+64)
    if edge[s][1]!=0:
        inor(edge[s][1])

inor(1)
print(inor_res)

post_res=''
def post(s):
    global post_res
    if edge[s][0]!=0:
        post(edge[s][0])
    if edge[s][1]!=0:
        post(edge[s][1])
    post_res += chr(s + 64)

post(1)
print(post_res)
