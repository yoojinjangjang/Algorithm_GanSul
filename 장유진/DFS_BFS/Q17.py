import sys
from collections import deque

input = sys.stdin.readline

n,k = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

s,x,y = map(int,input().split())

dx  = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(graph,queue):
    len_q = len(queue)
    while queue:
        a,b = queue.popleft()
        len_q -= 1
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx <0 or ny <0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[a][b]
                queue.append((nx,ny))
        if len_q == 0:
            return
    return

queue = deque()
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            queue.append((i,j))

queue = deque(sorted(queue,key=lambda a: graph[a[0]][a[1]]))
for _ in range(s):
    bfs(graph,queue)

print(graph[x-1][y-1])





