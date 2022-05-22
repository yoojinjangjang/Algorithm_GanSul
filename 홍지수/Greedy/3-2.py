'''
큰 수의 법칙
'''

import sys

N, M, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort(reverse=True)
ans = 0

for i in range(M // (K + 1)):
    for j in range(K):
        ans += arr[0]
    ans += arr[1]
if M % (K + 1) != 0:
    ans += arr[0] * (M % (K + 1))

print(ans)
