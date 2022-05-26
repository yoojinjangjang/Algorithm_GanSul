'''
만들 수 없는 금액
'''

import sys
import itertools

N = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))
comb = []
ans = []
key = 1

for i in range(1, N):
    comb = list(itertools.combinations(arr, i))
    for j in comb:
        ans.append(sum(j))

for _ in ans:
    if key in ans:
        key += 1

print(key)