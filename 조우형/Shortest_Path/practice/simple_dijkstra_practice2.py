import sys
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
visited = [False]*(n+1)
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def get_shortest_path():
    dist = INF
    index = 0

    for i in range(1, n+1):
        if distance[i] < dist and not visited[i]:
            index = i
            dist = distance[i]

    return index


def dijkstra(start):

    distance[start] = 0
    visited[start] = True

    for i in graph[start]:
        distance[i[0]] = i[1]

    for i in range(n-1):
        now = get_shortest_path()
        visited[now] = True

        for j in graph[now]:
            dist = distance[now] + j[1]
            if dist < distance[j[0]]:
                distance[j[0]] = dist

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])









