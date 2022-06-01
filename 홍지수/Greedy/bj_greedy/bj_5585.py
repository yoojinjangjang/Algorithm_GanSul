'''
거스름돈 - [boj] 5585
'''
import sys

money = 1000 - int(sys.stdin.readline())
arr = [500, 100, 50, 10, 5, 1]
cnt = 0
for i in arr:
    cnt += money // i
    money %= i
print(cnt)