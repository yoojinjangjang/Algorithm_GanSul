import sys

input = sys.stdin.readline

map_x, map_y = map(int, input().split())
x, y, direction = map(int, input().split())
four_points = [[-1, 0], [0, -1], [0, 1], [1, 0]]
result = 1

check_map = [[0] * map_x] * map_y
location = []
for i in range(map_y):
    location.append(list(map(int, input().split())))

def turn_left(now_direction):
    if now_direction == 0:
        return 3
    return now_direction - 1

def go(x, y, direction):
    return {'nx': x + four_points[direction][0], 'ny': y + four_points[direction][1]}

def back(x, y, direction):
    return {'nx': x - four_points[direction][0], 'ny': y - four_points[direction][1]}

while True:
    turn_left(direction) # turn left
    go(x, y, direction)

    if check_map[x][y] != 1 and location[x][y] != 1:
        check_map[x][y] = 1
        go(x, y, direction)
    else:
        back(x, y, direction)

    location[x][y] = 1

    breakpoint = True
    for four in four_points:
        if x + four[0] == 0 and y + four[1] == 0:
            breakpoint = False

    if breakpoint:
        break
            

print(result)

