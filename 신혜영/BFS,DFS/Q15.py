import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().strip().split())
graph = [[] for _ in range(N + 1)]
# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (N + 1)
distance[X] = 0

for i in range(M):
    node, vertex = map(int, input().split())
    graph[node].append(vertex)

queue = deque([X])
while queue:
    now = queue.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            queue.append(next_node)

print(distance)

