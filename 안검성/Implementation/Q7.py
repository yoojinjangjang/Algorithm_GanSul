import sys
from turtle import left

n = sys.stdin.readline()

n_len = len(n)

left_n = 0
right_n = 0

for i in range(n_len // 2):
    left_n += int(n[i])
    right_n += int(n[i + n_len // 2])

if left_n == right_n:
    print("LUCKY")
else:
    print("READY")
