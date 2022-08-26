import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 벽에 부딪혔을 때 멈춤
            if nx < 0 or ny < 0:
                continue
            if nx >= N or ny >= M:
                continue

            # 이동가능할 때
            if graph[nx][ny] == 1:
                queue.append([nx, ny])
                graph[nx][ny] = graph[x][y] + 1

    return graph[N - 1][M - 1]
graph = [list(map(int, input().strip())) for _ in range(N)]

print(bfs(0, 0))
