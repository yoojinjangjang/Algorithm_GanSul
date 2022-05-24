import sys

S = sys.stdin.readline().strip()
print(len(S))
cnt = 0
for i in range(1, len(S) - 1):
    if S[i-1:i] != S[i] and S[i] == S[i:i+1]:
        cnt += 1
        break

print(cnt)