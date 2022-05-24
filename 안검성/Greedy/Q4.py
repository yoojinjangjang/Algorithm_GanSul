N = int(input())
data = list(map(int, input().split()))

data.sort()

result = 1

for i in range(len(data)):
    if result < data[i]:
        break
    result += data[i]

print(result)
