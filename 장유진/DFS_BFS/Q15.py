'''
특정 거리의 도시 찾기
'''

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


def dfs(graph, start, visited, end):
    if end in graph[start]:
        return 1
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            tmp = dfs(graph, i, visited, end)
            if tmp != 0:
                return 1 + dfs(graph, i, visited, end)
    return 0


answer = [0] * (n + 1)

for i in range(1, n + 1):
    if i == x:
        continue
    visited = [False] * (n + 1)
    visited[0] = True
    answer[i] = dfs(graph, x, visited, i)

print(answer)
for i,val in enumerate(answer):
    if val == k:
        print(i)
if k not in answer:
    print(-1)
