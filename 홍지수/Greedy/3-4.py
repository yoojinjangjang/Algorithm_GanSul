'''
1이 될 때까지
'''

import sys

N, K = map(int, sys.stdin.readline().split())
cnt = 0
while (N > 1):
    if N % K != 0:
        N -= 1
        cnt += 1
    N = N // K
    cnt += 1

print(cnt)