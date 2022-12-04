import sys
input = sys.stdin.readline

N, x = map(int, input().split())
l = list(map(int, input().split()))


count = 0
start = 0
end = N-1
# 어떻게 해야 하지
# 1 1 2 2 2 2 3
# 0 1 2 3 4 5 6

# 2보다 작은 것 중애 가장 큰 것 idx
# 2보다 크것 중에 가장 작은 것 idx
# 아래 - 위 - 1

small_idx = 0
while start <= end:
    mid = (start + end) // 2
    if l[mid] >= x:  # 작은 것을 찾는 것이므로 크거나 같으면 왼쪽 리스트 찾기
        end = mid - 1
        continue

    if l[mid] < x:
        if l[small_idx] <= l[mid]:
            small_idx = mid
        start = mid + 1

start = 0
end = N-1
big_idx = N - 1
while start <= end:
    mid = (start + end) // 2
    if l[mid] <= x:  # 큰 것을 찾는 것이므로 작거나 같으면 오른쪽 리스트 찾기
        start = mid + 1
        continue

    if l[mid] > x:
        if l[big_idx] >= l[mid]:
            big_idx = mid
        end = mid - 1


print(big_idx - small_idx - 1)
