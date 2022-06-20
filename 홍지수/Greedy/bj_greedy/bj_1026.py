'''
보물 - [boj] 1026
'''
import sys

N = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
B = sorted(list(map(int, sys.stdin.readline().split())))
cnt = 0

for i in range(N):
    cnt += A[i] * B[i]
print(cnt)
