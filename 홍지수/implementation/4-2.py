'''
시각
'''
import sys

N = int(sys.stdin.readline())
h, m, s = 0, 0, 0
cnt = 0
for s in range(60):
    for m in range(60):
        for h in range(N+1):
            if '3' in (str(h) + str(m) + str(s)):
                cnt += 1

print(cnt)
