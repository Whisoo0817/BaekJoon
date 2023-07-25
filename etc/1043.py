import sys
input = sys.stdin.readline
n, m = map(int, input().split())
know = set(input().split()[1:])
parties = []

for _ in range(m):
    parties.append(set(input().split()[1:]))

for _ in range(m): # m번 안하면 밑의 테스트 케이스 통과 못함
    for party in parties:
        if party & know:
            know = know.union(party)
cnt = 0
for party in parties:
    if party & know:
        continue
    cnt += 1

print(cnt)


# Test case
# 10 10
# 1 1
# 2 10 1
# 2 9 2
# 2 8  3
# 2 7  4
# 2 6  5
# 2 5  7
# 2 4  8
# 2 3 9
# 2 2 10
# 1 1

# Answer: 0