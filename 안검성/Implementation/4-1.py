import sys

n = int(sys.stdin.readline())
move_plan = list(sys.stdin.readline().split())

result_x = 1
result_y = 1

for i in move_plan:
    if i == "L":
        if result_x <= 1:
            continue
        result_x -= 1
    elif i == "R":
        if result_x > n:
            continue
        result_x += 1
    elif i == "U":
        if result_y <= 1:
            continue
        result_y -= 1
    else:
        if result_y > 5:
            continue
        result_y += 1

print(result_y, result_x)
