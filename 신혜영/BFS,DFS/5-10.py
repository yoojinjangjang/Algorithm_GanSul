"""
bfs 0이면 cnt += 1
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().strip())) for _ in range(N)]

def bfs(x, y):
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]


        if nx < 0 or ny < 0:
            return False
        if nx >= N or ny >= M:
            return False
        
        if graph[x][y] == 0:
            graph[x][y] = 1
            bfs(nx, ny)
            return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        if bfs(i, j) == True:
            result += 1

print(result)