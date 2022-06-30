import sys

S = sys.stdin.readline().strip()
alphabet = []
num = []

for i in range(len(S)):
    num.append(int(S[i])) if ord(S[i]) >= 49 and ord(S[i]) <= 57 else alphabet.append(S[i])

print(''.join(sorted(alphabet)) + str(sum(num)))