import sys

input = sys.stdin.readline

N = int(input())
data = list(map(int,input().split()))

count = 0
data.sort()
ans = 0

for i in data:
    count += 1
    if count >= i:
        ans += 1
        count = 0
print(ans)