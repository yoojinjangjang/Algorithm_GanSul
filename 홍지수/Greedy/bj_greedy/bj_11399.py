'''
ATM - [boj] 11399
'''

import sys

N = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))
ans = 0
for i in range(1, N + 1):
    ans += sum(arr[:i])
print(ans)
