'''
곱하기 혹은 더하기
'''

import sys

S = list(map(int, sys.stdin.readline().strip()))
ans = S[0]

for i in range(1, len(S)):
    if ans <= 1 or S[i] <= 1:
        ans += S[i]
    else:
        ans *= S[i]
print(ans)