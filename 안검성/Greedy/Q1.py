N = int(input())
data = list(map(int, input().split()))

data.sort()
result = 0
current_data = []

while True:
    current_data.append(min(data))
    data.remove(min(data))

    if max(current_data) <= len(current_data):
        current_data.clear()
        result += 1

    if min(data) > len(data):
        break

print(result)
