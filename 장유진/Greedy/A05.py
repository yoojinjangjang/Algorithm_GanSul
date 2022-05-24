import sys

input = sys.stdin.readline

n,m = map(int,input().split())
data = list(map(int,input().split()))

count = [0] * m
for x in data:
    count[x-1] += 1
ans = 0
for i in range(m):
    res = count[i] * sum(count[i+1:-1])
    ans += res
    # n -= count[i]
    # ans += count[i] * n
print(ans)
