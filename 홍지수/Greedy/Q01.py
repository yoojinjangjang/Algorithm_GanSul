'''
모험가 길드
'''
import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort(reverse=True)

cnt = 0
for i in range(len(arr)):
    N -= arr[i]
    cnt += 1
    if N == 0:
        break

print(cnt)

# N = int(sys.stdin.readline())
# data = list(map(int, sys.stdin.readline().split()))
# res = 0
# cnt = 0
# for i in data:
#     cnt += 1
#     if cnt >= i:
#         res += 1
#         cnt = 0
# print(res)