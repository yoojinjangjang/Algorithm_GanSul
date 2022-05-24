'''
볼링공 고르기
'''
import sys

import itertools

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
comb = list(itertools.combinations(arr, 2))
ans = len(comb)
for i in comb:
    if i[0] == i[1]:
        ans -= 1
print(ans)