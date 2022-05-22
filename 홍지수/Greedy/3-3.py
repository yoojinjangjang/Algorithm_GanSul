'''
숫자 카드 게임
'''

import sys

N, M = map(int, sys.stdin.readline().split())
arr = []
ans = []

for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

for column in arr:
    ans.append(min(column))

print(max(ans))
