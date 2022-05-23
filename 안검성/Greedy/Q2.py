S = input()

result = 0

for i in range(len(S)):
    if int(S[i]) <= 1 or result == 0:
        result += int(S[i])
    else:
        result *= int(S[i])

print(result)
