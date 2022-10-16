
import sys
from collections import deque
input = sys.stdin.readline
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


distance = [-1] * (n+1)
distance[x] = 0

q = deque()
q.append(x)
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)


for i,val in enumerate(distance):
    if val == k:
        print(i)
if k not in distance:
    print(-1)