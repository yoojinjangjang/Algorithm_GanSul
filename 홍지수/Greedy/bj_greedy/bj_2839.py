
'''
설탕배달 - [boj] 2839
'''

import sys

N = int(sys.stdin.readline())
ans = 0

while N >= 0:
    if N % 5 == 0:
        ans += N // 5
        print(ans)
        break
    N -= 3
    ans += 1

else:
    print(-1)