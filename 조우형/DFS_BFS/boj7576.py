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
m, n = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))
print("done")
def check_tomato(m, n, graph):
    yes_tomato = 0
    no_tomato = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                yes_tomato += 1
            elif graph[i][j] == -1:
                no_tomato

    if (m*n)-no_tomato == yes_tomato:
        return 0
    elif yes_tomato == 0:
        return -1




def bfs(m, n, graph):
    day = []

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                day.append((i, j))

    queue = deque()
    queue.append(day)

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    res = 0
    while queue:
        print(queue)
        q = queue.popleft()
        day = []

        for i in q:
            x = i[0]
            y = i[1]
            print(x, y)

            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]
                print("nx = {}, ny = {}".format(nx, ny))

                if 0 <= nx < n and 0 <= ny < m:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = 1
                        day.append((nx, ny))
                print("뿅", day)
        print(day)
        if len(day) != 0:
            queue.append(day)
        res += 1

    if check_tomato(m, n, graph) == 0:
        return res
    else:
        return -1

if check_tomato(m, n, graph) == 0:
    print(0)
elif check_tomato(m,n,graph) == -1:
    print(-1)
else:
    print(bfs(m,n,graph))




