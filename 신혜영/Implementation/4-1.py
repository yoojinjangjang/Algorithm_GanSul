import sys

input = sys.stdin.readline

N = int(input())
A = list(input().split())
start_x = 1
start_y = 1

for road in A:
    if road == 'L' and start_y > 1:
        start_y -= 1
    elif road == 'R' and start_y < N:
        start_y += 1
    elif road == 'U' and start_x > 1:
        start_x -= 1
    elif road == 'D' and start_x < N:
        start_x += 1

print(start_x, start_y)
