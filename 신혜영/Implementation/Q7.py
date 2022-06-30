import sys

N = sys.stdin.readline().strip()

N_list = [int(N[i]) for i in range(len(N))]
num1 = 0
num2 = 0

for i in range(len(N)//2):
    num1 += N_list[i]

for i in range(len(N)//2, len(N)):
    num2 += N_list[i]

print('LUCKY' if num1 == num2 else 'READY')