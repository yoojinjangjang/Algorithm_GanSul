'''
특정 거리의 도시 찾기
'''

import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())
city = [[] for _ in range(N + 1)]
dis = [0] * (N + 1)
visited = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    city[a].append(b)


def bfs(city, X):
    q = deque()
    q.append(X)
    visited[X] = 1
    while q:
        X = q.popleft()
        for i in city[X]:
            if not visited[i]:
                dis[i] = dis[X] + 1
                visited[i] = 1
                q.append(i)


bfs(city, X)
if K not in dis:
    print(-1)
else:
    for i in range(1, N + 1):
        if dis[i] == K:
            print(i)
