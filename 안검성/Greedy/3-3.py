N, M = map(int, input().split())

data = []
min_data = []
for i in range(N):
    temp = list(map(int, input().split()))
    data.append(temp)
    min_data.append(min(temp))

print(max(min_data))
