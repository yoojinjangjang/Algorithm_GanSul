'''
DFS/BFS 기출 문제 15. 특정 거리의 도시 찾기

n = 도시의 수
m = 도로 개수
k = 최단 거리
x = 출발 도시
'''
import sys
from collections import deque
n, m, k, x = map(int, sys.stdin.readline().split())
graph = []

for i in range(n+1):
    graph.append([])

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

cities = [0] * (n+1)


queue = deque()
queue.append(x)
while queue:
    start = queue.popleft()
    break

    for g in graph[start]:
        queue.append(g)
        cities[g] += 1

