import sys

input = sys.stdin.readline

N, K = map(int, input().split())
money_list = [int(input().strip()) for i in range(N)]
money_list.sort(reverse=True)

result = 0
for money in money_list:
    if K >= money:
        cnt = K // money
        result += cnt
        K -= money * cnt

print(result)