import sys

S = sys.stdin.readline().strip()
result = 1
for i in range(0, len(S)):
    if int(S[i:i+1]) != 0:
        result *= int(S[i:i+1])

print(result)
