'''
연구소
'''

import sys
from itertools import combinations
input = sys.stdin.readline
from collections import deque
import copy
import itertools

n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))


dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(graph,queue):
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                queue.append((nx,ny))
    ans_graph = list(itertools.chain(*graph))
    return len(ans_graph) - ans_graph.count(1) - ans_graph.count(2)

location_0 = []
queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            location_0.append((i,j))
        if graph[i][j] == 2:
            queue.append((i,j))

maxx = -1
for com in list(combinations(location_0,3)):
    #temp_graph = graph.copy()
    temp_graph = copy.deepcopy(graph)
    temp_graph[com[0][0]][com[0][1]] = 1
    temp_graph[com[1][0]][com[1][1]] = 1
    temp_graph[com[2][0]][com[2][1]] = 1

    temp_queue = queue.copy()

    maxx = max(maxx,bfs(temp_graph,temp_queue))
print(maxx)

