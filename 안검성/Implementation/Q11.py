import sys

n = int(sys.stdin.readline())

k = int(sys.stdin.readline())
k_location = []
for i in range(k):
    x, y = sys.stdin.readline().split()
    k_location.append([int(x) - 1, int(y) - 1])

l = int(sys.stdin.readline())
l_location = []
for i in range(l):
    x, c = sys.stdin.readline().split()
    l_location.append([int(x), c])

t = 1
snake_location = [[0, 0]]
direction = "r"
snake_head = [0, 0]

while 1:
    if len(l_location) > 0:
        if t - 1 == l_location[0][0]:
            if l_location[0][1] == "L":
                if direction == "r":
                    direction = "u"
                elif direction == "d":
                    direction = "r"
                elif direction == "l":
                    direction = "d"
                else:
                    direction = "l"

            elif l_location[0][1] == "D":
                if direction == "r":
                    direction = "d"
                elif direction == "d":
                    direction = "l"
                elif direction == "l":
                    direction = "u"
                else:
                    direction = "r"
            l_location.pop(0)

    if direction == "r":
        snake_head[1] += 1
    elif direction == "d":
        snake_head[0] += 1
    elif direction == "l":
        snake_head[1] -= 1
    else:
        snake_head[0] -= 1

    # Hit snake body
    if snake_location[-1] == snake_head:
        break
    for i in range(0, len(snake_location) - 1):
        if snake_head == snake_location[i]:
            break

    # Out of bound
    if (
        snake_head[0] >= n
        or snake_head[0] < 0
        or snake_head[1] >= n
        or snake_head[1] < 0
    ):
        break

    snake_location.insert(0, snake_head.copy())

    # Eat apple
    for j in range(len(k_location)):
        if snake_head == k_location[j]:
            k_location.pop(j)
            break
    if len(k_location) < k:
        k -= 1
    else:
        snake_location.pop()
    t += 1

print(t)