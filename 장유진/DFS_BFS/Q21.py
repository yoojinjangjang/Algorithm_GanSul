'''
인구 이동
'''

import sys
from collections import deque

input = sys.stdin.readline

n, l, r = map(int, input().split())
maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(maps):
    check_flag = False
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            queue = deque()
            queue.append((i, j))
            visited[i][j] = True
            union = [(i, j)]
            while queue:
                x, y = queue.popleft()
                for loc in range(4):
                    nx = x + dx[loc]
                    ny = y + dy[loc]
                    if nx < 0 or ny < 0 or nx >= n or ny >= n:
                        continue

                    if not visited[nx][ny] and (l <= (abs(maps[x][y] - maps[nx][ny])) <= r):
                        queue.append((nx, ny))
                        visited[nx][ny] = True
                        union.append((nx, ny))
                        check_flag = True

            if len(union) == 1:
                continue
            change = sum([maps[i][j] for i, j in union]) // len(union)
            for location in union:
                maps[location[0]][location[1]] = change
    return check_flag


days = 0
while True:
    check_flag = bfs(maps)
    if not check_flag:
        break
    days += 1

print(days)
