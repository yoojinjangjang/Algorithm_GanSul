'''
DFS/BFS 기출 문제 17. 경쟁적 전염
N x N  크기의 시험관이 있습니다. 시험관에는 1~K번까지 K가지의 바이러스가 있습니다.
시험관에 모든 바이러스는 1초마다 상,하,좌,우의 방향으로 증식합니다.
번호가 낮은 바이러스가 먼저 증식하며, 바이러스가 있는 곳에는 다른 바이러스가 증식할 수 없습니다.
시험관의 크기와 바이러스의 위치 정보가 주어졌을 때, S초가 지난 후에 (X, Y)에
존재하는 바이러스의 종류를 출력하는 프로그램을 작성하세요.

Ex)
3 3
1 0 2
0 0 0
3 0 0
2 3 2

Result = 3
'''
from collections import deque
n, k = map(int, input().split())
graph = [[0]*n]
virus = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
s, x, y = map(int, input().split())
sec = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for x in range(n):
    for y in range(n):
        if graph[x][y] != 0:
            virus.append([x, y])

virus.sort()
queue = deque(virus)

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx > 0 and nx <= n and ny > 0 and ny <= n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]
                queue.append([nx, ny])