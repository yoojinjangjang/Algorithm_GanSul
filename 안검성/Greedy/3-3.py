N, M = map(int, input().split())

data = []
temp = []
for i in range(N):
    temp = list(map(int, input().split()))
    data.append(temp)

min_data = []
for j in range(N):
    min_data.append(min(data[j]))

print(max(min_data))
