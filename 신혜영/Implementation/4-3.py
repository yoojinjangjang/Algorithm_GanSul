import sys

position = sys.stdin.readline()

x = position[0]
y = int(position[1])

row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
x = row.index(x) + 1

case_list = [[2, 1], [2, -1], [-2, 1], [-2, -1], [-1, 2], [-1, -2], [1, 2], [1, -2]]
result = 0

for case in case_list:
    next_x = x + case[0]
    next_y = y + case[1]
    if next_x >= 1 and next_x <= 8 and next_y >= 1 and next_y <= 8:
        result += 1

print(result)
