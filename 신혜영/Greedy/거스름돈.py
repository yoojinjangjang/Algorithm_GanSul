import sys

money_list = [500, 100, 50, 10]
cnt = 0
N = int(sys.stdin.readline())

for money in money_list:
    cnt += N // money
    N %= money

print(cnt)
