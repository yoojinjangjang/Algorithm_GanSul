import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))

P.sort()

sum = 0
result = 0
for i in range(N):
    sum += P[i]
    result += sum

print(result)
