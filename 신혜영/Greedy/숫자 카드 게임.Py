import sys

input = sys.stdin.readline
N, M = map(int, input().split())
result = []
for i in range(N):
    num_list = map(int, input().split())
    result.append(min(num_list))

print(max(result))
