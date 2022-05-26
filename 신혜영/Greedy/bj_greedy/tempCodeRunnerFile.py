import sys

N = int(sys.stdin.readline())
result = 0
while N != 0:
    if N < 0:
        result = -1
        break

    if N % 5 == 0:
        N -= 5
        result += 1
    elif (N -5) % 3 == 0:
        N -= 3
        result += 1
    elif (N -3) % 3 == 0:
        N -= 3
        result += 1
    else:
        N -= 3
print(result)
