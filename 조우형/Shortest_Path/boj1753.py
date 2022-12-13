'''
Dijkstra 백준 1753. 최단경로

방향 그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를
구하는 프로그램을 작성하세요.

'''
import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())
graph = [[] for i in range(v+1)]
INF = int(1e9)
distance = [INF] * (v+1)
for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(k)

for d in range(1, v+1):
    if distance[d] == INF:
        print("INF")
    else:
        print(distance[d])