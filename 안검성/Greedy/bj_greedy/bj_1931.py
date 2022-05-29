import sys

N = int(sys.stdin.readline())

data = []
for i in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))
data.sort(key=lambda row: row[1])

end = data[0][1]
result = 1

for i in range(1, N):
    if end <= data[i][0]:
        end = data[i][1]
        result += 1

print(result)
