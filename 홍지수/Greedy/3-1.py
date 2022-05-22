import sys

N = int(sys.stdin.readline())
cnt = 0
coin = [500, 100, 50, 10]
for i in coin:
    cnt += N // i
    N %= i
print(cnt)