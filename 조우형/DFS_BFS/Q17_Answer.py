'''
DFS/BFS 기출 문제 17. 경쟁적 전염
'''
from collections import deque
n, k = map(int, input().split())
graph = []
virus = []
for x in range(n):
    graph.append(list(map(int, input().split())))
    for y in range(n):
        if graph[x][y] != 0:
            virus.append([graph[x][y], 0, x, y])
print(graph)
s, ix, iy = map(int, input().split())
sec = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

virus.sort()
queue = deque(virus)

while queue:
    v, sec, x, y = queue.popleft()
    if sec == s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = v
                queue.append([v, sec+1, nx, ny])

print(graph[ix-1][iy-1])