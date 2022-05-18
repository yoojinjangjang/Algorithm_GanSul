import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

# 가장 큰 수를 K 번 + 그 다음 큰 수 1 번 
sum = 0
cnt = 0
while cnt != M:
    sum += max(num_list) * K
    cnt += K
    sum += num_list[len(num_list) - 2]
    cnt += 1
    
print(sum)
