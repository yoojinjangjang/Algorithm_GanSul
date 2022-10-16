'''
미로 탈출
'''

from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

maze = []
for i in range(n):
    maze.append(list(map(int,input().strip())))

loc = [(-1,0),(1,0),(0,-1),(0,1)] #  좌우상하

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for l in loc:
            nx = x+l[0]
            ny = y+l[1]
            if nx <0 or ny <0 or nx >= n or ny >= m:
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx,ny))
    return maze[n-1][m-1]

print(bfs(0,0))
print(maze)