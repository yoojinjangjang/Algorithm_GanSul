import sys

input = sys.stdin.readline

N = int(input())
graph = [list(input().strip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

def dfs(x, y, color, visited):
    if 0 <= x < N and 0 <= y < N:
        if not visited[x][y] and graph[x][y] == color:
            visited[x][y] = True
            dfs(x + 1, y, color, visited)
            dfs(x - 1, y, color, visited)
            dfs(x, y + 1, color, visited)
            dfs(x, y - 1, color, visited)

            return True
    return False

cnt = 0
cnt2 = 0

for i in range(N):
    for j in range(N):
        if dfs(i, j, 'R', visited):
            cnt += 1
        if dfs(i, j, 'G', visited):
            cnt += 1
        if dfs(i, j, 'B', visited):
            cnt += 1
            cnt2 += 1

# 초기화
visited2 = [[False] * N for _ in range(N)]

# 변경
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'


for i in range(N):
    for j in range(N):
        if dfs(i, j, 'G', visited2):
            cnt2 += 1

print(cnt, cnt2, end = ' ')
