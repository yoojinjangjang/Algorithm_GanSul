'''
문자열 뒤집기 - 백준
'''

import sys
from math import ceil

S = list(map(str, sys.stdin.readline().strip()))
cnt = 0

for i in range(len(S) - 1):
    if S[i] != S[i - 1]:
        cnt += 1
print(ceil(cnt / 2))
