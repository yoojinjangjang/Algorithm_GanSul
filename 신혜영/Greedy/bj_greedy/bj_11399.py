# 5
# 3 1 4 3 2
import sys

input = sys.stdin.readline
N = input()
wait = list(map(int, input().split()))

wait.sort()

result = 0
stop_index = 0
sum = 0
for index, value in enumerate(wait):
    sum += wait[index]
    result += sum

print(result)