'''
동전 0 - [boj] 11047
'''

import sys

N, K = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(N)]
cnt = 0
for i in reversed(arr):
    cnt += K // i
    K %= i
print(cnt)
