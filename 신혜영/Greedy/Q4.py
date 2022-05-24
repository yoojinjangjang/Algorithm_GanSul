import sys

input = sys.stdin.readline

N = input()
money_list = list(map(int, input().split()))
money_list.sort()

result = [False] * max(money_list)

for money in money_list:
    result[money - 1] = True # if has --> true
    

