import sys

n = int(sys.stdin.readline())

result = 0
for h in range(n + 1):
    for m in range(60):
        for s in range(60):
            if "3" in str(h) or "3" in str(m) or "3" in str(s):
                result += 1
print(result)
