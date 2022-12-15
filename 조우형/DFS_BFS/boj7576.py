'''
BFS 백준 7576. 토마토

토마토 농장이 있다. 농장에 익은 토마토는 익지 않은 토마토에게 영향을 줘서 익게 한다.
하루가 지나면 익은 토마토의 상하좌우의 토마토들도 익은 토마토가 된다.
토마토 농장에 모든 토마토가 익게 되는데 필요한 최소 일수를 구하는 프로그램을 작성하세요.

Example)
input
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

output
8
'''
from collections import deque

m, n = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))


def check_state(n, m, graph):
    tomato_number = 0
    yes_tomato = 0  # 익은 토마토

    for i in range(n):
        for j in range(m):
            if graph[i][j] != -1:
                if graph[i][j] == 1:
                    yes_tomato += 1
                tomato_number += 1

    # 모든 토마토가 익어있는 상태면 0
    if tomato_number == yes_tomato:
        return 0
    # 토마토가 모두 익지 못하는 상황이면 -1
    else:
        return -1


def bfs(n, m, graph):
    queue = deque()
    day_queue = deque()
    res = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append((i, j))

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    day_queue.append((nx, ny))

        if not queue:
            for _ in range(len(day_queue)):
                queue.append(day_queue.popleft())
            res += 1

    if check_state(n, m, graph) == -1:
        return -1
    else:
        return res-1


if check_state(n, m, graph) == 0:
    print("0")
else:
    print(bfs(n,m,graph))

