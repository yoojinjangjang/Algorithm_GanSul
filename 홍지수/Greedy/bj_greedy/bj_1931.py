'''
회의실 배정 - [boj] 1931
'''

import sys

N = int(sys.stdin.readline())
arr = []
cnt = 0
endtime = 0

for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    arr.append((start, end))
arr.sort(key=lambda x: (x[1], x[0]))

for start, end in arr:
    if start >= endtime:
        endtime = end
        cnt += 1

print(cnt)
