import sys

N, K = map(int, sys.stdin.readline().split())
data = []
result = 0

for i in range(N):
    data.append(int(sys.stdin.readline()))
data.sort()

if K % data[-1] == 0:
    result = K // data[-1]
    print(result)
    exit(0)

for i in range(N - 1, -1, -1):
    result += K // data[i]
    K %= data[i]
    if K == 0:
        break

print(result)
