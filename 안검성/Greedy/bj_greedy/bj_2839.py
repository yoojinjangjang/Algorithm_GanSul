import sys

N = int(sys.stdin.readline())

if N % 5 == 0:
    print(N // 5)
    exit(0)

for N_five_kilo_bag in range((N // 5), -1, -1):
    if (N - N_five_kilo_bag * 5) % 3 == 0:
        print(N_five_kilo_bag + ((N - N_five_kilo_bag * 5) // 3))
        exit(0)

print(-1)
