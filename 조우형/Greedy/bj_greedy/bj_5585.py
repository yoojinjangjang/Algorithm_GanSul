'''
백준 그리디 5585
거스름돈
'''
import sys
b = int(sys.stdin.readline())
m = [500, 100, 50, 10, 5, 1]
res = 0
b = 1000 - b
for i in m:
    res += b//i
    b %= i
print(res)